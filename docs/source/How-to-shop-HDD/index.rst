How to Shop Storage
==============================================================================


Overview
------------------------------------------------------------------------------
本文记录了我在研究如何选购存储硬盘来扩充我的电脑存储空间时学到的一些知识. 以便我以后有购买需求时查阅.


Available Options
------------------------------------------------------------------------------
从底层硬盘类型来看, 一般分 HDD (机械硬盘), SSD (固态硬盘) 两类.

- HDD 容量大, 便宜, 速度相对较慢.
- SSD 容量小, 价格高, 但是速度极快, 读写次数上限比 HDD 小 (但一般人根本达不到).

从产品形态来看一般分:

- Internal, 内置, 安装在电脑里, 或者专门的外壳里, 没有独立电源, 由宿主供电, 不能用一个 USB 跟你的电脑直连. 在了解产品特性和参数的时候, 主要看对应的 Internal 内置盘的特性和参数既可, 因为其他两种都是在 Internal 盘的基础上进行的封装.
- External, 外置, 自带硬盘盒, 有自己独立的电源, 通过 USB 或者其他接口跟电脑连接), 一般 External 的本质是一个 Internal 硬盘 + 一个硬盘盒, 所以同等价位和性能 External 肯定要更贵, 并且读写速度受到数据线 (USB 或 Thunderbolt) 的限制, 一般比不上 Internal 跟电脑直接用 PCIe 总线的速度.
- Portable, 便携, 也就是移动硬盘.

所以两者合起来看就有大约 2*3, 六种产品类型.

而每一种产品类型一般又分不同的系列, 根据其读写性能, 容量大小, 可靠程度, 有没有为特定场景优化 (例如游戏, 图像, 数据, 小文件) 又分很多种.


Quick Links
------------------------------------------------------------------------------
对于以上 6 种产品类型, 我以 Western Digital 西部数据为例 (它们 2016 年收购了 Sandisk 移动 SSD 的新锐厂商), 用它们官网的对每种产品类型下的不同的型号的产品的介绍来作为参考.

- `Learn more about SSD <https://shop.sandisk.com/solutions/solid-state-drives>`_
- `Compare Internal SSD <https://shop.sandisk.com/solutions/solid-state-drives/internal-ssds>`_
- `Compare External SSD <https://shop.sandisk.com/solutions/solid-state-drives/external-ssds>`_
- `Compare Portal SSD <https://shop.sandisk.com/solutions/solid-state-drives/portable-ssds>`_
- `Learn more about HDD <https://www.westerndigital.com/solutions/hard-drives>`_
- `Compare Internal HDD <https://www.westerndigital.com/solutions/hard-drives/internal-hdd>`_
- `Compare External HDD <https://www.westerndigital.com/solutions/hard-drives/external-hdd>`_
- `Compare Portable HDD <https://www.westerndigital.com/solutions/hard-drives/portable-hdd>`_

- `Learn more about NAS <https://www.westerndigital.com/solutions/network-attached-storage>`_


Western Digital Internal HDD
------------------------------------------------------------------------------
Ref:

- https://www.westerndigital.com/solutions/hard-drives/internal-hdd

1. 黑盘(WD Black):
    - 应用场景: 高性能计算机,游戏PC
    - 特性: 高速度,大缓存,适合频繁读写
2. 蓝盘(WD Blue):
    - 应用场景: 日常使用的台式机和笔记本电脑
    - 特性: 性能和价格平衡,适合普通用户
3. 红盘(WD Red):
    - 应用场景: NAS(网络附加存储)设备,小型服务器
    - 特性: 专为24/7连续运行设计,低功耗,抗震
4. 紫盘(WD Purple):
    - 应用场景: 视频监控系统
    - 特性: 针对视频流优化,支持全天候工作
5. WD Gold (金盘):
    - 应用场景:
    - 特性:
        - 企业级数据中心
        - 大规模云存储系统
        - 高端服务器环境
6. WD Ultrastar (超星系列):
    - 应用场景:
        - 大规模数据中心
        - 云存储系统
        - 企业级服务器
        - 大数据分析平台
        - 高性能计算环境
    - 特性:
        - 超高容量: 提供市场上最大容量的硬盘选项之一
        - 卓越性能: 针对数据密集型应用优化
        - 极高可靠性: 设计用于24/7不间断运行
        - 先进技术: 如充氦技术(部分型号),提高容量和能效
        - 企业级耐用性: 能够承受高工作负载
        - 多接口选项: 通常提供SATA和SAS接口版本
        - 增强的数据安全性: 包括自加密驱动器(SED)选项
    - 目标用户:
        - 大型企业和组织
        - 云服务提供商
        - 数据中心运营商
        - 需要处理海量数据的研究机构

还有两种磁盘底层类型指的注意, 特别是用于冷备份的 SMR 盘, 你如果是日常使用, 可千万别买 SMR.

CMR (传统磁记录):

- 性能: 写入速度稳定, 无需重新整理数据. 
- 兼容性: 大多数系统和应用程序都能直接支持. 
- 可预测性: 写入操作直接, 不存在管理重叠磁道的复杂性. 
- 应用场景: 适合需要频繁随机写入操作的应用. 

SMR (叠瓦式磁记录):

- 密度: 由于磁道重叠, 可以实现更高的存储容量. 
- 成本效益: 由于盘片密度增加, 每TB的成本降低. 
- 顺序写入: 在以顺序写入为主的场景下表现良好. 
- 应用场景: 适合存档存储、备份任务和不频繁写入操作的场合. 

简单来说: 

- CMR硬盘更适合需要频繁读写, 性能要求高的场景, 如日常使用的电脑, 工作站等.
- SMR硬盘更适合需要大容量存储, 但不经常进行写入操作的场景, 如数据备份, 长期存档等.
