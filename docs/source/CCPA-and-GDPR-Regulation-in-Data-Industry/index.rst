CCPA and GDPR Regulation in Data Industry
==============================================================================


Overview
------------------------------------------------------------------------------
随着大数据技术的发展, 企业可以收集和处理海量的用户数据, 这也带来了数据滥用和侵犯用户隐私的风险. 为了规范数据的收集和使用, 保护用户隐私, 欧盟和美国加州分别出台了 GDPR 和 CCPA 两项重要的数据保护法案, 对企业的数据管理提出了严格要求. 作为大数据从业者, 我们有必要了解 GDPR, CCPA 的核心要求, 以及如何通过数据湖等技术手段来满足合规要求. 


What is CCPA and GDPR?
------------------------------------------------------------------------------
CCPA 全称 California Consumer Privacy Act, 是美国加州于2018年通过的消费者隐私保护法案. CCPA 赋予了加州消费者更多对个人信息的控制权, 包括知情权, 访问权, 删除权和拒绝出售个人信息的权利等. 

GDPR 全称 General Data Protection Regulation, 是欧盟制定的数据保护条例. 2018年5月正式生效, 被称为史上最严格的数据保护法案. GDPR 适用于所有处理欧盟公民个人数据的企业, 无论企业所在地区. 它要求企业以"设计和默认"的方式进行数据保护, 并赋予了数据主体许多权利, 如知情权, 访问权, 删除权等. 

Feature Requirements to be CCPA and GDPR Compliant
------------------------------------------------------------------------------
为满足 CCPA 和 GDPR 合规要求, 数据平台需具备以下关键功能:

1. 细粒度数据访问控制: 不同用户可访问不同粒度的脱敏数据, 严格控制敏感数据访问
2. 数据血缘追踪: 记录数据全生命周期路径, 可快速定位数据来源
3. 数据加密存储: 敏感数据列级或行级加密, 防泄露
4. 数据版本与快照: 可回滚到历史版本, 防误删
5. 彻底删除能力: 根据用户要求, 不留痕迹地删除其数据
6. 数据使用审计: 记录数据使用情况, 便于合规审计


How does Apache Hudi meet CCPA and GDPR requirements?
------------------------------------------------------------------------------
Apache Hudi 是一个开源的流式数据湖方案, 提供了如下特性来满足 CCPA 和 GDPR 合规:

1. 通过 Hudi 的列级 ACL, 可实现敏感列的访问控制, 不同角色看到不同的数据视图. 配合 AWS Glue Catalog + AWS Lake Formation 可以实现行级的访问控制.
2. Hudi 天然维护每次 Upsert 的 commit 元数据, 记录数据变更的来源, 可追踪数据血缘.
3. Hudi 支持删除特定文件, 配合 `专门的加密存储系统 <https://hudi.apache.org/docs/encryption/>`_, 可实现列级的加密存储.
4. 每次写入 Hudi 都产生一个新版本, 可基于版本和时间戳快速回滚到历史数据.
5. 利用 Hudi 的 `Delete <https://hudi.apache.org/blog/2020/01/15/delete-support-in-hudi/>`_ 和 Bootstrap, 可以从数据湖中彻底删除用户数据.
6. Hudi 的 timeline 和 compaction 审计日志, 记录了数据的变更历史, 可用于事后审计.


Reference
------------------------------------------------------------------------------
- `CCPA 官网 <https://oag.ca.gov/privacy/ccpa#:~:text=The%20California%20Consumer%20Privacy%20Act,how%20to%20implement%20the%20law.>`_
- `GDPR 官网 <https://gdpr-info.eu/>`_  
- `CCPA vs. GDPR: Similarities and Differences Explained <https://www.okta.com/blog/2021/04/ccpa-vs-gdpr/>`_: 一篇博文.
