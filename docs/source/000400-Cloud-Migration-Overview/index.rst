.. _cloud-migration-overview:

Cloud Migration Overview
==============================================================================
Keywords:


Overview
------------------------------------------------------------------------------
到写本文的时候 (2024 年), 前云时代已经过去了, 各个公有云已经非常成熟了. 虽然互联网的流量有很大一部分已经转移到云上了, 但是还是有很多企业的应用还是有上云需求.

这篇文档主要是对 Cloud Migration 技术进行一个概述. 具体的案例我们会在其他文档中进行详细介绍.


Migration Strategy
------------------------------------------------------------------------------
业内有六种主要的迁徙模式. 因为每个模式的名字都是以 R 开头, 所以也被叫做 6 R's:

1. Re-host (life and shift), 对服务器的硬盘做 比特级 的复制, 然后再云上运行.
2. Re-platform (lift-tinker-and-shift), 换一个平台, 例如将数据库从自家数据中心的虚拟机上迁徙到 AWS RDS 上.
3. Repurchasing, 购买新的产品, 例如抛弃过去的 CMS 员工管理系统, 使用 Salesforce.
4. Refactoring / Re-architect, 重新设计架构, 例如从 monolithic 模式迁徙到 microservice 模式.
5. Retire (Get rid of): 关闭不再使用的系统.
6. Retain (Usually this means "revisit" or do nothing for now): 啥也不做, 暂时不迁徙.

最常见的几种模式是 #1, #2, #3.


Common Migration Task
------------------------------------------------------------------------------
根据 Cloud Migration 的对象和目标, 我们可以将迁徙项目分为以下几类:

1. Storage: 存储, 包括文件存储, 块存储, 对象存储, 文件系统, 数据库等等.
2. Compute: 计算, 包括虚拟机, 容器, 函数, 编排等等.
3. Network: 网络.

以上的每一类的每一中任务都有很多具体的需求. 下面列出了一些需求, 我们这里不展开说:

- 系统是否能够暂时停机?
- 物理位置是不是跨 Region 转移了?

而按照 Application 的类型, 我们可以将迁徙项目分为以下几类:

存储:

- Relational Database to Cloud:
- NoSQL Database to Cloud:
- File Server to Cloud: 文件服务器.
- SFTP Server to Cloud: SFTP 服务器.
- EMC Storage to S3:
- Data Warehouse to Cloud:

计算:

- Web Applications:
- VM Server:
- Container Application:
- Server Cluster Application to Cloud: Kafka, Airflow, Spark, Hadoop, etc.
- CI/CD Pipeline to Cloud:
- Orchestration Tool to Cloud:
- Machine Learning Application to Cloud:

网络:

- Network Firewall to Cloud:
- Load Balancer to Cloud:
- CDN to Cloud:


What is Next
------------------------------------------------------------------------------
现在我们知道我们可以从两个维度 Migration Strategy 和 Migration Task 来考虑 Cloud Migration. 下面我们会针对每个维度中的不同选项, 介绍一下常用的策略和技术. 然后我们会把两个维度结合起来, 通过一些案例来介绍如何进行 Cloud Migration.


Reference
------------------------------------------------------------------------------
- `6 Strategies for Migrating Applications to the Cloud - by Stephen Orban | on 01 NOV 2016 <https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/>`_
- `7 Strategies for Migrating Applications to the Cloud, introducing AWS Mainframe Modernization and AWS Migration Hub Refactor Spaces - by Jonathan Allen | on 30 NOV 2021 <https://aws.amazon.com/blogs/enterprise-strategy/new-possibilities-seven-strategies-to-accelerate-your-application-migration-to-aws/>`_
