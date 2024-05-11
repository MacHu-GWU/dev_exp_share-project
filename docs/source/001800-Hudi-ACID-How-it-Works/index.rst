Hudi ACID How it Works
==============================================================================


Overview
------------------------------------------------------------------------------
本文详细揭示了 Hudi 是如何实现 ACID 一致性的.


Timeline and Timestamp Conflict
------------------------------------------------------------------------------
Hudi 官方文档说 "Hudi serializes all actions performed on a table into an event log - called the Timeline.", 也就是写操作是 **序列化执行** 的. 分布式系统用序列化来执行所有操作是很常见的设计, 一般是按照收到写请求的时间戳顺序执行. 而 Hudi 这里稍微不太一样, 因为 Hudi 里的写操作是由多个 Spark 写入程序执行的, 它并不像传统数据库一样是由客户端把请求发送给数据库, Hudi 并没有一个中心化的服务端.

这也就意味着多个写入程序的时间戳由于每个程序的时间可能不准而造成冲突. 不要小看这一问题, 虽然默认 Hudi 的时间戳是精确到微秒, 看似一秒钟内有 1000 个随机值. 但你只要了解过同一天生日概率的问题就会知道, 出现冲突的概率比你想象的高得多. 例如如果平均的并发数是 5, 那么每秒就有 1% 的几率出现冲突, 而这意味着每 100 秒就很有可能出现一次冲突. 所以 Hudi 也推荐在高并发系统中使用逻辑时间戳 (因为时间戳的作用只是提供一个单调递增的排序, 值到底是多少不重要. Hudi 推荐使用中心化的时间戳生成器, 例如 DynamoDB, ZooKeeper 来实现, 也就是写入程序写入时去中心化的生成器系统中拿号.

.. code-block:: python

    # -*- coding: utf-8 -*-

    def 生日概率(人数: int, 一年有多少天: int):
        p = 1 / 一年有多少天
        n = 人数
        total = 1
        for i in range(n):
            prob = 1 - i * p
            total = total * prob
        total = 1 - total
        print(f"{total*100:.2f}%")

    生日概率(人数=23, 一年有多少天=365) # 50.73%
    生日概率(人数=60, 一年有多少天=365) # 99.41%
    生日概率(人数=5, 一年有多少天=1000) # 1.00%
    生日概率(人数=10, 一年有多少天=1000) # 4.41%


Isolation Level
------------------------------------------------------------------------------
Hudi 的 Isolation Level 使用的时 Snaoshot Isolation. 也就是说当多个写入程序没有交集时则可以并发, 有交集时则序列化执行. 这里的交集在 Hudi 中指的是 File Group. 也就是两个 Writer 如果是写入到不同的 File Group, 则可以并行执行. 这里我们只讨论两个 Writer 同时写入到同一个 File Group 的情况.

这里假设你已经熟悉了 COW 和 MOR 的底层实现. 如果不熟悉请先阅读 :ref:`hudi-writer-how-it-works`. 首先我们知道有多个写入到一个 File Group 的 Writer 的时候它们是按照时间戳顺序执行的, 前一个执行完了才能进行下一个. 这里我们专注于 Hudi 是如何把包含写入多个文件的动作封装成一个 Transaction 的.

对于一个 File Group 的写入任务, Hudi 有 3 个 State, ``requested`` 类似于请求已经收到, 但没有执行, ``inflight`` 类似于正在执行, ``completed`` 类似于 finished, 可能成功了也可能失败了. 这也是你在 S3 上看到的这些文件::

    s3://bucket/root/.hoodie/20220727183745.commit
    s3://bucket/root/.hoodie/20220727183745.commit.requested
    s3://bucket/root/.hoodie/20220727183745.inflight

你看到的这些以时间戳开头的文件的文件格式都是符合 ``[Action timestamp].[Action type].[Action state]`` 这一规范的. Action Timestamp 不用说, Action State 则是我们刚才提到的 ``requested``, ``inflight``, ``completed``. Action Type 除了上面例子中的 commit, 还有 ``deltacommit``, ``rollback``, ``savepoint``, ``restore`` 等一堆. 而如果你只看到 ``[Action timestamp].[Action type]``, 那么 Action state 其实是 ``completed``, 只不过被省略了. 而如果你只看到 ``[Action timestamp].[Action state]``, 那么 Action type 其实是 ``commit``, 只不过被省略了.

你还记得吗, 在写入过程中 Hudi 从来不会删除文件, 在 COW 模式下只会追加 base file, MOR 模式下也只会追加 log file (虽然 COW 中的 clean up 会清除掉无用的旧文件, MOR 模式下的 merge 会合并 base file log file, 这两个操作都不是写入, 而是由另外的程序执行的), 那么 Hudi 是如何保证在写入的过程中同时读, 只能读到之前的版本或是之后的版本, 而不会读到中间的版本呢? 这是因为每个 Parition 中的 ``s3://bucket/root/${yyyy-mm-dd-1}/.hoodie_partition_metadata`` 文件记录了这些 File Group 中哪些 Base file 是 active 的, 哪些是 retired 了. 而数据文件全部写入完成后对 ``.hoodie_partition_metadata`` 的更新才算是真正 commit 结束了. 当然这里又会有 ``.hoodie_partition_metadata`` 和 ``20220727183745.commit`` 文件双写的问题, 具体 Hudi 是如何实现的我们就不得而知了.


Reference
------------------------------------------------------------------------------
- `Transaction Log (Timeline) <https://hudi.apache.org/tech-specs/#transaction-log-timeline>`_
- `超硬核解析Apache Hudi 的一致性模型 (第一部分) <https://cloud.tencent.com/developer/article/2414205>`_
