Universal Near Real-Time Data Synchronization: From Operational Databases to Analytics Data Stores
====================================================================================================


Objective
------------------------------------------------------------------------------
本文旨在探讨如何将 Business Operational Database 中的单个表格数据以近实时的方式同步到 Analytics Data Store. 这种方法能够在不影响 Business Operational Database 性能的前提下, 充分利用 Analytics Data Store 进行高效数据分析.

为便于理解, 我们先明确两个关键概念:

- **Business Operational Database (简称 "Database")**: 支持日常业务运营的数据库系统. 通常具备事务 (Transaction) 功能, 包括关系型数据库 (如 Oracle, DB2, MSSQL, MySQL, PostgresSQL 等) 和 NoSQL 数据库 (如 MongoDB, Amazon DynamoDB 等).
- **Analytics Data Store (简称 "Datalake")**: 专为数据分析而设计的存储系统. 常见形式包括各种数据仓库产品 (如 Snowflake, Amazon Redshift, Google Big Query) 和数据湖方案 (如 Delta Lake, Hudi, Iceberg 等).

在我们深入探讨解决方案之前, 我们需要先了解一下数据模型的关键要素. 这些要素对于实现高效的数据同步至关重要.


Data Model
------------------------------------------------------------------------------
业务数据的 Data Model 一定要包含以下三个 Attribute:

- id: 每个 Record 都要有一个全局唯一的标识符. 这个是必须要有的, 不然 Transaction (事务) 保证就无从谈起了. 它不一定是 Record 中的 单个 Attribute, 也可以是多个 Attribute 的组合 (compound key).
- create_time: 这条 Record 的创建时间. 这个值一旦被创建后就不会再改变. 这个字段可以用来做 Data Partition 的.
- update_time: 这条记录的最后更新时间. 如果这条记录是第一次被创建, 那么这个时间和 create_time 是一样的. 在数据同步时的 CDC Event 的时间本质上就是 update_time.

理解了数据模型的基本结构后, 我们现在可以概览整个解决方案的框架. 这个方案旨在有效地将数据从业务数据库同步到分析数据存储中.


Solution Overview
------------------------------------------------------------------------------
本节概述了这个解决方案的核心思路, 主要包含三个关键步骤:

1. **配置 CDC (Change Data Capture) Stream**:
   - 从指定的时间点 ("Initial Time") 开始, 持续捕获数据变更.
   - 将捕获的 CDC 数据发送到流处理系统.
   - 使用 Consumer 将 CDC 数据按预定义的目录结构持久化到对象存储中.
   - 这些持久化的 CDC 数据文件我们称为 "CDC Time Slice File".

2. **创建 Initial Datalake**:
   - 选择一个特定时间点 ("Snapshot Cutoff Time").
   - 使用该时间点的数据库快照创建初始的数据湖.

3. **建立 CDC Data Pipeline**:
   - 持续处理 "CDC Time Slice File" 中的数据.
   - 将所有晚于 "Snapshot Cutoff Time" 的数据不断写入到数据湖中.
   - 确保数据湖与源数据库保持同步.

有了对整体解决方案的宏观理解, 我们现在可以深入探讨第一个关键步骤: 配置 CDC Stream 和 CDC Data Persistence Consumer. 这个步骤是实现近实时数据同步的基础.


Create CDC Stream and CDC Data Persistence Consumer
------------------------------------------------------------------------------
本节详细介绍如何配置 CDC (Change Data Capture) Stream 以及 CDC Data Persistence Consumer, 这是实现近实时数据同步的关键步骤. 


CDC Stream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CDC Stream 的主要功能是从指定的时间点 ("Initial Time") 开始, 持续捕获数据变更并将其发送到流处理系统中. 每个 CDC 事件的 "Event Time" 对应数据中的 "update_time". 

对于大规模数据库, 通常需要配置多个 stream partition 来提高数据吞吐量以确保数据能够被及时处理. 关于 stream partitioning 的详细讨论, 请参考下一节.


.. _stream-partitioning:

Stream Partitioning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
大多数流处理系统都是分布式的, 底层采用分区机制. 这种机制只能保证单个分区内的 Record 顺序一致, 但无法保证跨分区的顺序.

为了确保同一条记录的 CDC 事件顺序正确, 我们通常使用 "id" 作为 partition key. 这样, 同一 Record 的所有 CDC 事件都会被分配到同一个 partition.

.. note::

    这里的 Partition 指的是 Stream Partition, 与数据湖中的 Data Partition 是不同的概念. 


CDC Data Persistence Consumer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CDC Data Persistence Consumer 的主要职责是将 CDC 数据持久化到对象存储系统中. 具体步骤如下: 

1. 按 "update_time" 对数据进行排序. 
2. 将数据按固定时间间隔 (如每分钟, 后面都会假设一个 Time Slice 是 1 分钟) 划分.
3. 将划分后的数据持久化为 "CDC Time Slice File". 

例如, 你可能会有如下命名的数据文件:

- ``2024-01-01T00:00-to-2024-01-01T00:01``
- ``2024-01-01T00:01-to-2024-01-01T00:02``
- ...

这些文件存储的位置被称为 "CDC Event Persistence Area". 以 AWS S3 为例, 其文件夹结构可能如下: 

``s3://datalake-bucket/cdc-event/${database_name}/${schema_name}/${table_name}/${stream_partition_id}/${cdc_time_slice_file}.csv|json|parquet|...``

关于 Stream Consumer 的更多细节, 请参考下一节. 


.. _stream-consumer:

Stream Consumer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Stream Consumer 通常会将接收到的数据转换为列式存储格式 (如 Parquet) 后再持久化, 而不是直接使用 CDC 事件中的原始格式 (如 JSON, CSV, XML) . 这样做的目的是为了加速后续的 ETL 处理. 由于 Consumer 不需要立即处理接收到的数据, 而是在一定的时间窗口内进行聚合后再处理, 因此有足够的时间进行数据格式转换, 这个过程带来的额外时间开销可以忽略不计.

每个 Stream Partition 对应一个 Consumer, 因此最终的 "CDC Time Slice File" 会是每分钟每个 Partition 生成一个. 例如, 如果 Stream 有 10 个 Partition, 每分钟就会生成 10 个 "CDC Time Slice File".

即使某个 Consumer 出现故障导致 "CDC Time Slice File" 数量不足, CDC Data Pipeline 仍可正常运行. 这是因为缺失的数据只来自于同一个 Partition, 其他 Partition 的数据不会包含相同的 id.


Write Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
由于 Stream Partition 的存在, 同一个 Time Slice 下会有多个 Slice File. 为了优化写入 Data Lake 的性能, 我们采用以下策略: 

1. 对每个 Slice File 先进行 id 的 group by 操作, 保留每个 id 的最新数据. 
2. 合并处理后的 Slice File. 
3. 根据 Data Partition key 将数据分成多份. 
4. 利用多 CPU 并行写入不同的 Data Partition. 

这种优化策略能够显著提高写入效率. 值得注意的是, 许多现代数据处理引擎 (如 Spark, DeltaLake, Hudi 等) 都内置了根据 Data Partition key 自动分割数据的功能, 无需手动实现 #3, #4.


Create Initial Datalake
------------------------------------------------------------------------------
本节我们将详细介绍如何从数据库快照 (Database Snapshot) 创建初始数据湖 (Initial Data Lake). 这个过程提供了一个通用的方法论, 适用于各种类型的数据库快照.

数据库快照到数据湖的转换过程概述:

任何形式的数据库快照都可以被转换成多个小型文件, 每个文件包含部分数据. 我们将这些文件称为"快照数据文件" (Snapshot Data File). 通常, 每个快照数据文件的大小都适中, 可以被单台机器轻松处理.

整个转换流程分为两个主要步骤:

1. 快照数据处理: 处理快照数据文件, 将数据重新分配到不同的暂存区 (Staging Area) 的数据分区中.
2. 数据压缩和优化: 对暂存区中每个数据分区的多个小文件进行合并 (compaction), 合并成更大的 Parquet 文件, 并在生成过程中对数据进行排序.

第一步: 快照数据处理

对每一个 "快照数据文件" 进行以下处理:

1. 数据加载和处理:
   - 将所有记录加载到内存中.
   - 识别或计算每条记录的关键字段, 如"id", "create_time", "update_time"等 (字段名可能因数据库而异).
   - 计算所有分区键值对 (partition key value pair). 关于 Data Partition 的详细讨论请参考 :ref:`data-partition`.
   - 根据分区键将数据分割成子集, 写入不同的分区.
   - 在写入前, 对每个子集按 update_time 进行排序, 这有助于加速后续的合并排序过程.
   - 生成的文件称为"暂存数据文件" (Staging Data File).

2. 文件命名规则: 生成的每个暂存数据文件按以下格式命名: ``${path_to_table}/${partition_key_value}/.../${snapshot_data_file_id}``. 这种命名方式确保文件名不会重复. 关于 datalake 中的数据文件目录结构的详细讨论请参考 :ref:`datalake-storage-folder-structure`.

3. 处理架构: 采用 Orchestrator + Worker 的架构来处理数据:
    - Orchestrator 将所有快照数据文件转换为任务 (Task), 存入数据库.
    - 每 10 秒查询一次数据库, 检查未处理的任务和正在处理的任务数量.
    - 根据预设的并发数 (如 20) 动态启动新任务.
    - 调度间隔和并发数可根据数据量调整, 可通过对快照数据文件的初步分析来确定这些参数.
    - 这个流程可以使用各种编排工具实现, 如 Airflow, AWS Step Functions 等.

第二步: 数据压缩和优化

对每一个 "数据分区" 进行以下处理:

1. 数据合并和 Parquet 文件生成:
- 读取分区下的所有数据到内存.
- 按 update_time 对数据进行排序.
- 生成 Parquet 文件:
  * 如果分区总数据量小于 128 MB, 生成一个文件.
  * 如果大于 128 MB, 生成多个文件. 文件数量计算方法: 总大小 / 128 MB, 向上取整.
- 文件大小估算: 基于第一步中处理的记录数量和暂存数据文件大小, 可以预估最终生成的 Parquet 文件数量和大小.

2. 处理架构: 同样采用 Orchestrator + Worker 架构:
- Orchestrator 将所有暂存数据文件转换为任务, 存入数据库.
- 任务调度逻辑与第一步中处理快照数据文件的 Orchestrator 类似.

通过这个两步流程, 我们可以有效地将数据库快照转化为结构化, 优化的数据湖, 为后续的数据分析和处理奠定基础. 这种方法不仅可以处理大规模数据, 还能确保数据的有序性和可查询性, 从而提高数据湖的整体性能和可用性.


.. _data-partition:

Data Partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
数据分区 (Data Partitioning) 是数据湖中的一个关键概念, 它通过将大型数据集分割成更小, 更易管理的部分来优化数据存储和查询性能. 这种策略允许分布式系统中的多个工作节点并行处理不同的分区, 显著提高处理效率. 在查询时, 分区支持谓词下推 (Predicate Pushdown), 能够在数据扫描前就过滤掉大量不相关的分区, 大幅减少需要处理的数据量, 从而提升查询速度. 此外, 通过控制每个分区的数据量, 可以使数据更均匀地分布, 更适合分布式处理, 提高整体系统的可扩展性和性能. 这种方法不仅优化了存储利用率, 还为大规模数据分析提供了更高的效率和灵活性.

在存储中的文件路径一般遵循 ``${path_to_table}/${partition_key1}=${partition_key1_value}/${partition_key2}=${partition_key2_value}/.../${data_file}`` 这样的形式. 例如一种常见的 partition 策略是按照 Record create_time 的 year, month, day 来分区. 那么最终的目录结构就像 ``${path_to_table}/year=2024/month=01/day=01/${data_file}``. 而 ``${path_to_table}/year=2024/month=01/day=01/`` 目录被称作 "Data Partition Dir".

通常, create_time 的 year, month, day (数据量特别大的话还可能会用到 hour, minutes) 是一定会被用作 partition key 的. 因为用 create_time 对数据进行过滤是最常见的查询模式. 而因为 partition key 只能基于 immutable 的字段 (不然一旦发生 update 这条数据就要被移动到其他 partition 了, 造成了大量的数据移动), 所以 update_time 不能用做 partition key.

用作 partition key 的字段一定是 low cardinality 的, 不然会导致 partition 的总数过多, 生成大量小文件导致查询性能地下. 例如你有一个 category 的字段, 里面的值只有 5 种可能, 那么它就很适合做 partition key, 但是如果里面的值有 1000 种可能, 除非你确保你的每个查询里都必带 category 这个字段, 不然它不适合做 partition key.

当你除了 create_time 还有 category 字段的 partition key 时, 在 folder structure 中谁在前, 谁在后就是一个问题. 通常 object storage 都支持基于 prefix 的查询. 所以我们要把能过滤掉更多的数据的字段放在 folder structure 的前面. 例如如果你的查询中一定会带 category 字段, 那么你可以把 category 放在前面像 ``${path_to_table}/category=1/year=2024/...`` 这样. 而如果你的查询中带有 create_time 的概率更高, 那么你应该使用 ``${path_to_table}/year=2024/.../category=1/...`` 这样的结构.


.. _datalake-storage-folder-structure:

Datalake Storage Folder Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
现代数据湖通常构建在对象存储 (Object Storage) 之上. 对象存储因其分布式特性而具有几乎无限的扩展能力, 相比传统的 HDFS 更易于使用和管理. 这使得对象存储成为了业界数据湖存储后端的事实标准.

数据湖的文件夹结构通常类似于数据库中的层级关系: database -> schema -> table -> partition -> data. 以下是一个基于 AWS S3 的数据湖文件夹结构示例:

    s3://datalake-bucket/datalake/${database_name}/${schema_name}/${table_name}/${partition_key1}=${partition_key1_value}/${partition_key2}=${partition_key2_value}/.../${data_file}

这种结构清晰地组织了数据, 便于管理和查询. 每一层级都代表了数据的不同属性或分类, 从而实现了高效的数据组织和访问.

.. seealso::

    :ref:`data-partition`


Create CDC Data Pipeline
------------------------------------------------------------------------------
创建 CDC Data Pipeline 是整个解决方案的最后一步, 也是确保数据湖与源数据库保持同步的关键环节. 本节我们将详细介绍如何构建和运行这个 pipeline.


创建中心化的 Metadata Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
首先, 我们需要创建一个中心化的 metadata store, 它将作为分布式锁来管理 Pipeline 的运行状态. 这个 metadata store 可以是一个关系型数据库或者是一个分布式键值存储系统, 例如 MySQL, PostgreSQL, 或者 Redis.

metadata store 中至少需要包含以下信息:

- 最后处理的 "CDC Time Slice File" 的时间戳
- 当前是否有 Worker 正在运行
- 锁的状态 (是否被占用)


创建 Orchestrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Orchestrator 是整个 CDC Data Pipeline 的调度中心. 它负责监控新的 "CDC Time Slice File" 是否可用, 并在适当的时候启动 Worker 进行处理.

Orchestrator 可以是一个独立的服务, 也可以是一个定时任务. 它应该具备以下功能:

- 定期检查 metadata store 中的状态
- 决定是否需要启动新的 Worker
- 启动 Worker 的能力 (例如通过 AWS Lambda, 或者在 Kubernetes 集群中创建新的 Pod)


创建 CDC Data Processing Worker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CDC Data Processing Worker 是实际执行数据处理和写入的组件. 每个 Worker 应该是一个独立的进程或服务, 能够独立完成一个 "CDC Time Slice File" 的处理.

Worker 应该具备以下能力:

- 读取 "CDC Event Persistence Area" 中的 "CDC Time Slice File" 中的数据
- 对数据进行必要的转换和处理
- 将处理后的数据写入到数据湖中
- 更新 metadata store 中的状态


Worker 的业务逻辑
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Worker 的具体业务逻辑如下:

1. 尝试获取锁:
   Worker 启动后, 首先尝试从 metadata store 中获取锁. 如果获取失败, 说明有其他 Worker 正在运行, 当前 Worker 应该立即退出.

2. 处理数据:
   如果成功获取锁, Worker 将执行以下步骤:
   a. 根据 metadata store 中记录的上一次处理的 "CDC Time Slice File", 找到下一个需要处理的文件.
   b. 使用乐观锁的方式在 metadata store 中标记当前正在处理的文件.
   c. 读取 "CDC Time Slice File" 中的数据.
   d. 对数据进行预处理:
      - 按照 id 对数据进行分组
      - 只保留每个 id 的最新一条数据, 过滤掉不必要的中间状态
   e. 将处理后的数据写入数据湖, 执行 UPSERT 操作.
   f. 更新 metadata store 中的状态, 记录最新处理的文件时间戳.
   g. 释放锁.

注意事项:

- 整个处理过程假设处理一个 "CDC Time Slice File" 的时间小于文件中的事件时间间隔 (在本例中为 1 分钟). 如果处理时间超过这个间隔, 说明处理能力跟不上数据生成速度, 需要考虑使用分而治之的方式来提高并行度.
- 数据预处理步骤 (按 id 分组并保留最新数据) 通常在内存中进行, 因为单个时间片的数据量一般不会太大, 这个操作通常很快.


Orchestrator 的调度逻辑
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Orchestrator 的主要职责是确保新的 "CDC Time Slice File" 能够及时被处理. 其调度逻辑如下:

1. 定期检查:
   每隔一定时间 (例如 10 秒) 检查一次是否有新的 "CDC Time Slice File" 需要处理.

2. 确定处理需求:
   通过比较 metadata store 中记录的最新处理文件时间戳与当前时间, 判断是否有新文件需要处理.

3. 启动 Worker:
   如果发现有新文件需要处理, Orchestrator 将启动一个新的 Worker 来处理数据.

4. 监控和错误处理:
   Orchestrator 还应该监控 Worker 的运行状态, 处理可能出现的错误情况, 例如 Worker 异常退出或处理超时等.

通过以上设计, CDC Data Pipeline 能够持续不断地将源数据库的变更同步到数据湖中, 保证数据的及时性和一致性. 这种方法不仅能够处理大规模数据, 还具有良好的可扩展性和容错能力.

通过以上详细的介绍, 我们已经全面阐述了这个近实时数据同步解决方案的各个方面. 为了进一步总结和澄清关键点, 我们将在下面三个小节中对目录结构, 后端灵活性和关键术语进行总结.


Object Store Folder Structure Summary
------------------------------------------------------------------------------
在整个解决方案中, 我们使用了多个不同的目录结构来组织和管理数据. 以下是主要的目录结构概览: 

.. code-block:: python

    s3://datalake-bucket/
        cdc-event/
            ${database_name}/
                ${schema_name}/
                    ${table_name}/
                        ${stream_partition_id}/
                            ${cdc_time_slice_file}.csv|json|parquet|...
        db-snapshot/
            ${database_name}/
                ${schema_name}/
                    ${table_name}/
                        ${snapshot_id}/
                            ${snapshot_data_file}
        staging-area/
            ${database_name}/
                ${schema_name}/
                    ${table_name}/
                        {snapshot_id}/
                            ${partition_key1}=${partition_key1_value}/
                                ${partition_key2}=${partition_key2_value}/
                                    .../
                                        ${staging_data_file}
        datalake/
            ${database_name}/
                ${schema_name}/
                    ${table_name}/
                        ${partition_key1}=${partition_key1_value}/
                                ${partition_key2}=${partition_key2_value}/
                                    .../
                                        ${data_file}

这些目录结构清晰地展示了数据在不同处理阶段的组织方式, 从 CDC 事件到最终的数据湖存储. 


Backend Agnostic
------------------------------------------------------------------------------
这个解决方案的一个关键优势是其后端的灵活性. 所有组件都有多种选择, 无需锁定在特定的编程语言, 工具或服务提供商上: 

- Database: 大多数支持事务的数据库 (包括事务型 NoSQL 如 DynamoDB, MongoDB 等) 都支持 CDC Stream.
- CDC Data Capture: Debezium, Amazon DMS 等.
- Stream: 可选用 Kafka, Pulsar, AWS Kinesis 等. 
- CDC Data Persistence Consumer: 可使用各种计算资源, 如 AWS Lambda Function. 
- DataLake and Storage: 可选用各种对象存储 (如 S3, GCS, Azure Blob Storage) 和支持 ACID 及 Upsert 的数据湖技术 (如 Delta Lake, Hudi, Iceberg). 
- CDC Data Pipeline Orchestrator: 可使用各种编排工具, 如 Airflow, AWS Step Functions 或简单的 AWS Lambda Function. 
- CDC Data Pipeline Worker:
  - 编程语言: 可使用 Spark 与 Java/Scala/Python 配合. 
  - 计算资源: 可选用 AWS Lambda Function, ECS, EMR/Glue 等. 
- CDC Data Pipeline Metadata Store: 可使用各种持久化的中等性能 KV Store, 如 DynamoDB, Zookeeper, ETCD. 

这种灵活性使得解决方案能够适应不同的需求和环境, 避免了供应商锁定. 


Glossary
------------------------------------------------------------------------------
General:

- Business Operational Database (简称 "Database"): 支持日常业务运营的数据库系统, 包括关系型数据库和 NoSQL 数据库.
- Analytics Data Store (简称 "Datalake"): 专为数据分析设计的存储系统, 包括数据仓库产品和数据湖方案. 
- Record: 业务运营数据库中的一条记录, 在不同类型的数据库中可能有不同的称呼 (如行, 文档, 项目) . 
- Attribute: Record 中的一个字段, 在不同类型的数据库中也可能有不同的称呼 (如列, 字段, 属性) .

CDC Stream:

- CDC (Change Data Capture): 捕获数据变更的技术.
- Initial Time: CDC Stream 开始捕获数据变更的起始时间点.
- Stream Partition: 流处理系统中的数据分区, 用于并行处理.
- CDC Event Persistence Area: 用于存储 CDC Time Slice File 的专门区域, 通常位于对象存储系统中.
- CDC Time Slice File: 持久化的 CDC 数据文件, 按时间间隔划分.

Initial Datalake

- Snapshot Cutoff Time: 创建初始数据湖时选择的特定时间点, 用于确定数据库快照的时间范围.
- Snapshot Data File: 数据库某一时间点快照转换而成的小文件.
- Data Partition: 数据湖中的数据分区, 用于优化查询性能.
- Data Partition Dir: 一个数据分区的目录, 其下直接包含数据文件而非更多子目录.
- Staging Area: 数据处理过程中的临时存储区域.
- Staging Data File: 在数据处理过程中生成的中间文件, 存储在 Staging Area 中, 用于后续的数据合并和优化.

CDC Data Pipeline

- UPSERT: 更新插入操作, 如果记录存在则更新, 不存在则插入.
