Intelligent Document Processing Platform Solution Design
==============================================================================


Overview
------------------------------------------------------------------------------
这是我在 AWS 工作室设计, 开发, 部署的一套生产可用的 Intelligent Document Process 平台. 已经在多个 AWS 的客户的生产环境中成功部署并运行良好了. 本问详细记录了这套 Solution 的架构.


Related Project
------------------------------------------------------------------------------
- `aws_textract_pipeline <https://github.com/MacHu-GWU/aws_textract_pipeline-project>`_: 这套 Solution 的底层 Python 实现. 不包含 AWS 的服务, 只是在内存里的纯计算. 这套实现可以用任何平台部署, 不局限于 AWS 平台. 并且既可以用虚拟机或容器的形式作为 Batch Job 部署, 也可以用 Event driven 的架构用于实时处理.


Architecture Diagram
------------------------------------------------------------------------------
.. raw:: html
    :file: ./Intelligent-Document-Processing-Solution-Design.drawio.html
