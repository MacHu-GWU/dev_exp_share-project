.. _pick-an-open-source-license-for-python-project:

Pick An Open Source License For Python Project
==============================================================================


Overview
------------------------------------------------------------------------------
Since I actively maintain hundreds of open-source, closed-source, and commercial projects, I wrote this document as a reference for myself—so I can quickly choose a license for any new Python project.

In general:

- If I want to publish an open-source project and don’t mind if people use it commercially, I choose ``MIT``.
- If I want to keep it open-source and allow customization for non-commercial use only—while preventing big tech from using it in SaaS products—I choose ``AGPL-3.0-or-later``.
- If it’s a closed-source project, I choose ``Proprietary``.


MIT
------------------------------------------------------------------------------
``pyproject.toml``

.. code-block:: python

    license = "MIT"
    ...
    classifier = [
        ...
        "License :: OSI Approved :: MIT License",
        ...
    ]

.. dropdown:: ``LICENSE.txt``

    .. literalinclude:: ./MIT.txt
       :linenos:


AGPL 3.0 or later
------------------------------------------------------------------------------
``pyproject.toml``

.. code-block:: python

    license = "AGPL-3.0-or-later"
    ...
    classifier = [
        ...
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        ...
    ]

.. dropdown:: ``LICENSE.txt``

    .. literalinclude:: ./GNU Affero General Public License v3.0.txt
       :linenos:

**Then Put this at the top of your source code (Every single one)**:

.. code-block:: python

    # Copyright (C) [YEAR] [YOUR NAME / YOUR COMPANY NAME / YOUR EMAIL]
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    # GNU Affero General Public License for more details.
    #
    # You should have received a copy of the GNU Affero General Public License
    # along with this program. If not, see <https://www.gnu.org/licenses/>.

**防范对象 / 行为, 描述**:

1. 闭源 SaaS 提供商: 防止公司将你的代码部署成在线服务 (如 Web 应用, SaaS 产品) 后不公开源码. 这是与 GPLv3 的最大区别.
2. 不公开的修改: 强制任何人, 只要他们运行了修改后的版本 (无论是否发行), 都必须开放源代码, 尤其是网络部署场景.
3. "SaaS 漏洞": 弥补了 GPLv3 的 "软件即服务" (SaaS loophole), 即使用 GPL 软件提供在线服务时可以不发布源码的问题. AGPL 要求你必须发布源码.
4. 再许可为闭源代码: 不允许将 AGPL 授权的软件更改后发布为闭源软件或在闭源项目中使用 (除非遵循 AGPL 条款).
5. 动态链接闭源库: 与 GPL 类似, AGPL 强制所有 **派生作品（包含链接）**也使用 AGPL 许可 (除非使用通用接口如 REST API).
6. 内部修改不共享 (仅限网络提供): 即使是公司内部对代码进行了修改, 只要用户通过网络访问, 就必须开放这些修改过的代码.
7. 把开源变成商业黑盒产品: 防止公司将开源代码商业包装、部署给用户使用而不给任何技术贡献或代码反馈.
8. 静默安全修复隐藏: 如果有人发现安全漏洞并修复后部署了修改版服务, 也必须发布源码, 防止用户使用了潜在危险的闭源版本.
9. 被动侵占开源社区成果: 保护开源社区的集体劳动成果不被大企业 "掠夺性" 使用并重新商品化 (比如拿开源项目包装成商业服务).
10. 再打包分销商: 防止公司或开发者以修改后的方式打包成自己的品牌分发而不开放其修改内容.


Proprietary
------------------------------------------------------------------------------
``pyproject.toml``

.. code-block:: python

    license = "Proprietary"
    ...
    classifier = [
        ...
        "License :: Other/Proprietary License",
        ...
    ]

.. dropdown:: ``LICENSE.txt``

    .. literalinclude:: ./Proprietary.txt
       :linenos:


Reference
------------------------------------------------------------------------------
- `Choosing the right license <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>`_: GitHub 的官方文档, 介绍了怎么选择开源协议.
- `Choose an Open Source license <https://choosealicense.com/>`_: GitHub 创建的网站, 教你如何选择开源协议.
- `License Templates <https://github.com/licenses/license-templates>`_: GitHub 维护的开源协议文档模板.
- `PyPI Classifier <https://pypi.org/classifiers/>`_: 在 Python 的包管理系统 PyPI 中, 在 ``classifier`` 字段中, 有很多关于开源协议的分类, 这里包含了所有有效的值的列表
- `Python Package User Guide - License <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license>`_: Python 官方关与如何选 license 的介绍.
- `SPDX License List <https://spdx.org/licenses/>`_: Python 的包管理系统中 ``license`` 字段的有效值的列表.
