Hudi Writer How it Works
==============================================================================
本文将深入探究 Hudi 到底是如何实现 Upsert 的. 在写入文件的过程中到底做了什么?

我下面以使用 AWS S3 作为存储为例, 先介绍 COW 和 MOR 两种模式通用的一些内容, 然后再分别讨论两个模式下的详细步骤和差异.


Hudi Table Folder Structure
------------------------------------------------------------------------------
我们举个例子, 我们有一个表, 它按照时间顺序每天产生一个 partition. 我们假设这个 Hudi 表在 S3 上的根目录是 ``s3://bucket/root/``. 那么这个 S3 目录下面看起来就是这个样子::

    s3://bucket/root/
    s3://bucket/root/.hoodie/
    s3://bucket/root/.hoodie/.aux/
    s3://bucket/root/.hoodie/.aux/.bootstrap
    s3://bucket/root/.hoodie/.aux/.bootstrap/.fields
    s3://bucket/root/.hoodie/.aux/.bootstrap/.partitions
    s3://bucket/root/.hoodie/.temp/
    # 下面都是 Instant file, 文件名是时间戳, 精确到秒, 如果同一秒有多个 commit 则会自动加上 1, 2, 3 自增后缀
    s3://bucket/root/.hoodie/20220727183745.commit
    s3://bucket/root/.hoodie/20220727183745.commit.requested
    s3://bucket/root/.hoodie/20220727183745.inflight
    s3://bucket/root/.hoodie/20220727183747.commit.requested
    s3://bucket/root/.hoodie/20220727183747.inflight
    s3://bucket/root/.hoodie/20220727183747.commit
    # 下面是一个 partition
    s3://bucket/root/${yyyy-mm-dd-1}/
    s3://bucket/root/${yyyy-mm-dd-1}/.hoodie_partition_metadata
    # 下面前面 UUID 一样的就是一个 file group
    s3://bucket/root/${yyyy-mm-dd-1}/7b7afd5e-3b00-4ded-beed-caa155cf1d1b-0_0-0-0_20220726183745.parquet
    s3://bucket/root/${yyyy-mm-dd-1}/7b7afd5e-3b00-4ded-beed-caa155cf1d1b-0_0-0-0_20220726183747.parquet
    # 这又是一个分区, 和上面的 partition 相同
    s3://bucket/root/${yyyy-mm-dd-2}/
    s3://bucket/root/${yyyy-mm-dd-2}/.hoodie_partition_metadata
    s3://bucket/root/${yyyy-mm-dd-2}/ce84409f-33aa-492f-baf6-a7d8580c23a5-0_0-0-0_20220726183745.parquet
    s3://bucket/root/${yyyy-mm-dd-2}/ce84409f-33aa-492f-baf6-a7d8580c23a5-0_0-0-0_20220726183747.parquet
    
.. note::

    这里没有展示 ``.index`` 索引文件, 以后再详细介绍.

我们定义下列术语 (不是 Hudi 官方的, 仅仅是为了在本文中表述方便)

- Table root: 例如 ``s3://bucket/root/``
- Partition root: 单个 partition 的根目录, 例如 ``s3://bucket/root/${yyyy-mm-dd-1}/``.

**File Group**

由于 Hudi 会定期做 Compaction (将小文件合并成大文件), 所以 Hudi 在 Partition 下面又创造了 File Group 概念. 第一次写入数据时, 会生成一个 File Group. 在后续数据持续写入 判断该 File Group 的 DataFiles 文件是否超出一个设定的阈值大小 (可以是文件总大小也可以是文件数量), 未超出则在此 File Group 中继续写入数据文件. 超出阈值就会重新生成一个新的 File Group. 而后来的系统优化 Compaction 实际上就是将 File Group 中的所有文件合并成大文件.

**Base File**

在数据第一次写入到一个 Partition 时创建的基础文件. 在 COW 模式下每次 Upsert 都会把变化和新增数据都在 Base File 中进行更新. 而在 MOR 模式下如果是第一次写则会创建 Base File, 之后的写都是创建 Log file.

**Log File**

MOR 模式下独有的文件. 记录了第二次写到同一个 File Group 中的时候的 Update 和 Insert 的所有数据 (注意不是 delta 哦). 在读的时候会自动将其和 Base File Merge 到一起.

**Index**

有了 Partition, File Group, Base File, Log File 的概念之后, 你可以想象进行 update 的关键是判断一个 record_id 在过去有没有出现过. 而高效的做这件事情的关键是维护一个 record_id 到 File Group 映射关系的 的 Index. 因为任何一个新的 record_id 进来, 我们关键是要知道它是 insert 还是 update. 如果在 Index 里, 那肯定是 update, 那么我们就能找到 File Group 的 Id, 在 COW 模式下就可以找到对应的 File Group 里的 Base file 进行 Upsert, 在 MOR 模式下就在对应的 File Group 中追加 Log File. 如果不在 Index 里, 那就是 insert.

每当你写入新数据时候, Hudi 都会更新这个 index.

这个 Index 有多重实现方式, 适合不同的应用场景, Hoodie 允许你自由选择.

这个 Index 有两种模式, Global 和 Partition (全局和分区模式). Global 就是维护一个所有 Partition 中的 record_id 的大索引. Partition 就是维护单个 Partition 下的 record_id. 换言之 Global 模式下所有的 record_id 都是必须是唯一的, 而 Partition 模式下则只能保证 Partition 下的 record_id 唯一. 显然 Partition 模式下的性能会更高. 但是代价就是, 如果遇到了在 Partition 1 (P1) 中有一个 record_id_1, 然后你的数据里面本来就有错误, 出现了一个需要写入到 P2 但是 record_id 一样 (还是 record_id_1) 的情况, Partition 模式是发现不了这个错误的. Global 模式适合小表, Partition 模式适合大表.

Reference:

- `File Management <https://hudi.apache.org/docs/concepts/#file-management>`_: Hudi 官方文档对 File Management 的简略介绍.
- `File Layout Hierarchy <https://hudi.apache.org/tech-specs/#file-layout-hierarchy>`_
- `Index <https://hudi.apache.org/docs/concepts/#index>`_

``s3://bucket/root/${yyyy-mm-dd-1}/7b7afd5e-3b00-4ded-beed-caa155cf1d1b-0_0-0-0_20220726183745.parquet`` 数据文件中的


COW
------------------------------------------------------------------------------


MOR
------------------------------------------------------------------------------


Reference
------------------------------------------------------------------------------
- `Writer Expectations <https://hudi.apache.org/tech-specs/#writer-expectations>`_: Hudi 官方文档对 Writing 的简要介绍.
- `Hudi Concepts <https://hudi.apache.org/docs/concepts/>`_: Hudi 官方文档对 Timeline, Instant, File Group 等概念的介绍.