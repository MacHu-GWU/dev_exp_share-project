WORM Compliance in Data Industry
==============================================================================


Overview
------------------------------------------------------------------------------
在数据合规领域, WORM (Write Once Read Many) 是一个很常见的合规术语. 本文从 数据架构师, 合规审查人员, 企业主 等多个视角出发, 介绍了 WORM 合规性的概念, 特性要求. 并且我本人作为数据架构师, 也分享了一些关于如何设计符合 WORM 合规性要求的数据架构的经验.


What is WORM Compliance
------------------------------------------------------------------------------
WORM (Write Once Read Many) 合规性是一种数据存储策略, 要求数据一旦写入后就不能修改或删除, 只能读取. 这是为了确保数据的完整性, 真实性和不可否认性, 在许多行业如金融, 医疗, 法律等都有严格的监管要求.

注意, WORM 跟 CCPA 和 GDPR 这些著名的数据合规法案不同, 它不是一个特定的法律条文, 而是对一种数据合规性要求的描述. 例如: `SEC Rule 17a-4 <https://www.sec.gov/investment/amendments-electronic-recordkeeping-requirements-broker-dealers>`_ 就做出了关于 WORM 的要求. `FINRA rules <https://www.finra.org/rules-guidance/key-topics/books-records>`_ 也有类似的要求.

简单来说 WORM 有三点要求:

- **Immutable storage**: Once data is written, it becomes immutable, meaning it cannot be modified or deleted.
- **Time-defined data retention**: Data stored using WORM technology has a predetermined retention period during which it cannot be altered.
- **Audit trails**: WORM backup solutions often include audit trails, ensuring transparency and traceability of data access and modifications.


Feature Requirements to be WORM Compliant
------------------------------------------------------------------------------
下面我列出了当一个监管部门审查企业数据系统是否符合 WORM 规范时, 会看那些特性. 而企业的 Data   Architect 就可以在设计数据系统时参考这些特性来确保合规. 以下是一些关键的特性:

1. **数据不可篡改性**: 确保一旦数据写入, 就无法修改或删除. 需要检查:
    - 是否存在防止数据被覆盖或篡改的技术控制措施, 如版本控制, 条件写入等.
    - 数据删除是否仅限于自动过期删除, 而非人为删除.
    - 是否存在完整的数据变更记录和审计跟踪.
2. **数据保留期管理**: 评估数据的保留期是否符合法规要求. 需要检查:
    - 是否为不同类型的数据设置了适当的保留期.
    - 过期数据是否按照保留政策自动删除, 删除过程是否不可逆.
    - 保留期是否符合行业特定法规, 如 SOX, HIPAA, FINRA 等.
3. **数据备份和恢复**: 评估数据备份策略是否完善, 以确保数据可恢复. 需要检查:
    - 备份是否定期进行, 备份数据是否不可篡改.
    - 是否制定了数据恢复程序, 并定期测试.
    - 备份数据是否存储在独立的, 安全的位置.
4. **访问控制和权限管理**: 审查对 WORM 数据的访问控制是否严格. 需要检查:
    - 是否实施了最小权限原则, 严格限制写入和删除权限.
    - 访问控制是否遵循职责分离原则.
    - 是否定期审查和调整用户权限.
5. **数据安全和加密**: 评估数据是否受到适当的安全保护. 需要检查:
    - 静态数据和传输中的数据是否使用强加密算法加密.
    - 加密密钥管理是否安全和规范.
    - 是否定期进行安全风险评估和渗透测试.
6. **物理安全**: 如果使用自建数据中心, 您还需要审查物理安全措施, 如:
    - 数据中心的访问控制是否严格.
    - 是否提供适当的环境控制, 如温度, 湿度监测等.
    - 是否制定了充分的灾难恢复和业务连续性计划.
7. **第三方风险管理**: 如果企业使用外包服务或云服务, 需要审查:
    - 服务提供商是否符合 WORM 和其他相关合规要求.
    - 是否与服务提供商签订了适当的服务级别协议 (SLA).
    - 是否定期评估服务提供商的合规性和绩效表现.
8. **员工培训和意识**: 评估企业是否提供了充分的员工培训. 需要检查:
   - 员工是否接受过数据管理和合规性方面的培训.
   - 是否定期开展数据安全意识教育.
   - 是否建立了明确的数据管理政策和程序, 并有效传达给员工.


Data Systems
------------------------------------------------------------------------------
对于不同的数据系统, 满足合规需求的解决方案也不相同. 例如 RDBMS 系统就很容易满足合规需求, 而让 Data warehouse 和 Data Lake 合规就比较难一点 (因为它们天生不是 transactional 的).

接下来我会一一介绍不同的数据系统如何满足合规需求.


RDBMS Architecture for WORM Compliance
------------------------------------------------------------------------------
我们以 RDBMS 为例, 来看看如何设计一个符合 WORM 合规性要求的数据架构. 我会先给出架构设计, 然后会参考 "Feature Requirements to be WORM Compliant" 中提到的特性, 将这些特性一一映射到 Solution 上.

总的来说有两种思路.

1. 数据库依然允许 UPDATE. 满足数据不可篡改性是通过将 Write ahead log 导出到 immutable 的存储上实现. 这种方案最成熟, 也最容易实现.
2. 在数据库表设计层面引入不可篡改性. 通过创建一个 version 字段, 让每一个 Update 都变成 Insert. 这种方案比较复杂, 需要在业务层面考虑的很全面, 业务逻辑需要做出改变来适配这种设计. 并且没有一个唯一的方案, 需要根据具体表结构具体讨论.

这里我们重点讨论一下 #1. 因为对于满足 Worm 合规来说, #1 的方法不仅适用于 RDBMS, 还适用于 NoSQL 和各种 Transactional Data Lake (例如 Hudi, Delta Lake, Iceburg).

**Solution Walkthrough**

1. Business Operation 业务都由一个 "主表" 负责, 所有 增删插改 操作都正常进行.
2. 给 "主表" 配置一个 Capture of Data Change Stream. 对于 Insert 会记录新数据, 对于 Update 会记录更新前后的数据, 对于 Delete 会记录被删除前的数据.
3. Stream 中的数据会严格按照时间顺序被消费.
4. Stream 会按照时间进行 partition 将其保存在 S3 上. 这些 S3 上的数据构成了完整的 Change Log / Audit Log. 我们可以从 Log 将表恢复到任意时间点的状态.
5. 我们的 S3 bucket 开启了 versioning, 确保了数据不会被意外覆盖.
6. 我们使用了 `S3 object lock <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html>`_, 其中 retention 可以确保在一定时间内历史数据无法被删除, 其中 governance mode 能确保连 AWS 的 Admin 都无法删除该历史数据.
7. 我们使用了 `S3 life cycle policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html>`_, 它能确保数据在到期后被永久删除.
8. 我们在消费数据时会将同一时间段的数据按照列式存储的格式将不同的 column 保存为不同的文件. 这样可以做到为不同的 column 配置不同的过期时间策略.
9. 为 S3 bucket 配置了合理的 ACL 和 bucket policy, 确保只有极少的授权用户 (通常是管理员和审计人员) 能够读取这些文件, 但是没有覆盖和删除文件的权限.
10. 为 S3 bucket 配置了 `replicating <https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html>`_, 历史数据被同步备份到了多个 AWS region, 进一步确保了数据的安全性.
11. 我们使用了 KMS 对 S3 上的数据进行了加密, 并且数据在传输过程中也是加密的.

**Reviewing Solution for WORM Compliance**

1. **数据不可篡改性**: 确保一旦数据写入, 就无法修改或删除. 需要检查:
    - 是否存在防止数据被覆盖或篡改的技术控制措施, 如版本控制, 条件写入等.
        - Answer: 所有数据修改历史记录都备份到了 S3, 并且 S3 object lock + ACL + bucket policy 保证了数据不会被覆盖和意外删除.
    - 数据删除是否仅限于自动过期删除, 而非人为删除.
        - Answer: 数据由 S3 life cycle policy 确保自动删除, 而非人为删除.
    - 是否存在完整的数据变更记录和审计跟踪.
        - Answer: 在 S3 上由完整的数据变更记录, 可以对任意时间点的历史数据进行审计.
2. **数据保留期管理**: 评估数据的保留期是否符合法规要求. 需要检查:
    - 是否为不同类型的数据设置了适当的保留期.
        - Answer: 是的, 列示存储的方式可以为不同的 attribute 配置不同的删除策略.
    - 过期数据是否按照保留政策自动删除, 删除过程是否不可逆.
        - Answer: 是的, 按照政策历史数据到期后被永久删除, 不可恢复 (我们也可以做到可以恢复, 合规怎么要求我们就怎么做)
    - 保留期是否符合行业特定法规, 如 SOX, HIPAA, FINRA 等.
3. **数据备份和恢复**: 评估数据备份策略是否完善, 以确保数据可恢复. 需要检查:
    - 备份是否定期进行, 备份数据是否不可篡改.
        - Answer: 备份数据是实时进行的, 并且 S3 object lock 确保了备份数据不可被篡改.
    - 是否制定了数据恢复程序, 并定期测试.
        - Answer: 我们会定期从 S3 恢复整个 DynamoDB 作为测试.
    - 备份数据是否存储在独立的, 安全的位置.
        - Answer: 是, 备份数据会横跨多个 AWS region, 以确保数据的安全性.
4. **访问控制和权限管理**: 审查对 WORM 数据的访问控制是否严格. 需要检查:
    - 是否实施了最小权限原则, 严格限制写入和删除权限.
        - Answer: 如果 IAM 设计的没问题那么就没问题.
    - 访问控制是否遵循职责分离原则.
        - Answer: 如果 IAM 设计的没问题那么就没问题.
    - 是否定期审查和调整用户权限.
        - Answer: 对 IAM 的审查可以自动化.
5. **数据安全和加密**: 评估数据是否受到适当的安全保护. 需要检查:
    - 静态数据和传输中的数据是否使用强加密算法加密.
        - Answer: 原生支持 encrypt in transit 和 at rest.
    - 加密密钥管理是否安全和规范.
        - Answer: KMS 足够好了.
    - 是否定期进行安全风险评估和渗透测试.
        - Answer: 是.


DynamoDB Architecture for WORM Compliance
------------------------------------------------------------------------------
我们以 Amazon DynamoDB 为例, 来看看如何设计一个符合 WORM 合规性要求的数据架构.

**Solution Walkthrough**

这套方案跟 RDBMS 的方案 90% 是一样的. 下面我列出了不同点:

1. RDBMS 的 Stream 是 WAL. DynamoDB 用的是 `DynamoDB stream <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html>`_.
2. RDBMS 的权限管理不仅有 IAM, 还有数据库内部的 User / Group / Permission.

**Reviewing Solution for WORM Compliance**

这个跟 RDBMS 的结论是一致的. 我不再冗述.
