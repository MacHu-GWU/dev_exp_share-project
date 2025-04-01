The Ultimate Python Project Development Workflow
==============================================================================


Overview
------------------------------------------------------------------------------
In this blog post, I'll introduce the tools and philosophy I've used to successfully manage over 500 Python projects, including 150+ open source repositories, 200+ closed-source proof-of-concept initiatives, 100+ enterprise-grade applications, and 50+ production systems that consistently deliver value. I'll demonstrate how I maintain exceptionally high quality across all projects through production-grade dependency management, robust CI/CD pipelines, and documentation-as-code practices. These techniques have enabled me to achieve what typically requires an entire team - all as a single developer.


Challenge and Motivation
------------------------------------------------------------------------------
**The Enterprise Onboarding Maze**

If you've worked in enterprise environments, you're familiar with the onboarding process for new projects: asking about Git branching strategies, dependency management approaches, coding standards, testing methodologies, and CI/CD pipelines. Even when focusing solely on Python projects, there are countless different implementation approaches. Teams may have different folder structures, prefer different dependency management tools (Poetry, Pipenv, UV, PDM), and utilize various frameworks for testing, packaging, and deployment.

**Beyond Single Team Boundaries**

This diversity exists within a single team at one enterprise. Throughout my career, I've encountered a much wider variety of project types - enterprise applications, open-source libraries, internal reusable components, standalone applications, and personal projects. Each type requires different tooling choices and setup configurations. The sheer variety makes it impossible to memorize every approach, and adapting to different styles consumes valuable time and mental energy.

**Common Patterns, Different Implementations**

Taking a step back, I realized that despite these differences, all Python projects share fundamental needs: setting up virtual environments, managing dependencies, running tests, packaging code, and implementing CI/CD. The concepts remain consistent, but the specific CLI commands or scripts vary based on project style and type. This insight led me to ask: Could I create lightweight adapters that would allow me to memorize only key concepts—each represented by a simple, concise command—while a tool handles the implementation details behind the scenes?

**The Setup Bottleneck**

However, even these simplified commands require a properly structured repository with the right folder organization, tool configuration, and script placement. Setting this up for each new project is time-consuming, especially when you're juggling dozens or hundreds of projects. I wondered: What if I could create template projects for each type? Then, whenever I need a new project, I could execute a single command, specify a name, and have everything configured automatically. This would allow me to focus on development rather than setup, using those same abstract commands to handle all the complex operations behind the scenes.

**A 15-Year Evolution**

This approach - templates combined with simplified workflow commands - is what I've built and refined over the past 15 years. In this document, I'll explain my design philosophy and methodology in detail, showing how this system has enabled me to efficiently manage hundreds of projects of varying types and requirements while maintaining consistently high quality.


System Architecture: Template Based Project Automation
------------------------------------------------------------------------------
**Two-Tier Framework**

The architecture consists of two key components working together to streamline project development and management: template repositories and an automation library. This approach separates project structure from operational workflows, creating a scalable system for handling multiple project types.

**Template Repositories**

Template repositories provide the foundation for each project type - whether open source, enterprise, or proof-of-concept. Each template includes pre-configured folder structures, configuration files, and essential scripts. By simply entering basic information like project name and email, you can generate a fully structured project ready for development, eliminating repetitive setup tasks.

**Automation Library Design**

The automation library serves as a command abstraction layer, wrapping complex CLI operations in simple, memorable Python functions. Built using Python's subprocess module, it transforms multi-parameter commands into streamlined operations with minimal arguments. The library incorporates intelligent conditional logic to assess the current project state and execute appropriate commands accordingly.

**Evolution From Embedded to Standalone**

Initially, I embedded automation code directly within each template repository for transparency. However, I discovered that automation logic rarely changes for a specific project type. To reduce code duplication across hundreds of projects, I extracted these components into standalone, installable libraries—dramatically reducing the template's footprint while maintaining functionality.

**Integration Mechanics**

Together, these components create a powerful development ecosystem. Template repositories simplify project creation, while the automation library normalizes day-to-day operations across all projects. This standardization allows me to focus on development rather than remembering project-specific commands or procedures, dramatically increasing productivity when managing hundreds of projects simultaneously.



Overview
------------------------------------------------------------------------------
在大约 2010 年左右, 当时 Python 的社区的工具链还不发达的时候, 由于我同时维护着多个 Python 项目, 我就意识到需要一种 Consistent 的方式作为我的标准工作流以在所有项目中进行复用. 特别是工作流中那些复杂的命令行命令和参数. 后来, 随着我职业生涯中维护的项目越来越多 (超过 800 个开源和闭源项目, 150 多个开源 Python 库), 我的工作流和工具链也变得越来越重要. 十几年间更新换代了 4-5 个大版本, 架构设计也更新了 3-4 版.

由于整个的经历太长, 中间的思考和结论也在不断迭代, 所以我觉得我需要一篇文档来记录一下这个迭代的过程, 帮助我理解为什么我最新的设计是这个样子的.


History
------------------------------------------------------------------------------
1. 最早的时候, 我还没有探索出复用工作流的方法, 当时我是用一个 `开源文档 <https://github.com/MacHu-GWU/Python-OpenSource-Project-Developer-Guide>`_ 的形式把所有的细节都用文档的形式记录下来, 然后在我的每个项目中都使用这个文档作为参考.
2. 后来, 我意识到人手动操作总会出错, 所以有必要用一个 Python 包的形式将这些操作打包, 这样新项目只需要一个 CLI 命令就可以了. 于是我就创建了 `pygitrepo (pgr) <https://github.com/MacHu-GWU/pygitrepo-project?tab=readme-ov-file>`_ 项目. 并且我还创建了一个 Git Repo Template `cookiecutter-pygitrepo <https://github.com/MacHu-GWU/cookiecutter-pygitrepo>`_.
3. 再后来, 我发现 pygitrepo 的库的架构设计不够成熟, 无法在保持兼容性的情况下扩展. 所以我又创建了 `pyproject_ops <https://github.com/MacHu-GWU/pyproject_ops-project>`_ 项目, 并且配套了一个 Git Repo Template `cookiecutter-pyproject <https://github.com/MacHu-GWU/cookiecutter-pyproject>`_.
4. 再后来, 由于 pyproject_ops 只是为开源项目设计的, 而很多私有项目并不适合, 而 ``pyproject_ops`` 的扩展性还是不够好, 所以我在私有项目中把 pyproject_ops 的源代码复制了一份, 然后直接对其进行了修改.


The New Way - Python Workflow (pywf) Library Collection
------------------------------------------------------------------------------
The Python Workflow (pywf) library Collection addresses a common challenge faced by developers managing multiple Python projects: the inconsistency of workflows across different project types. In my experience maintaining approximately 150 open source projects, 50 closed source projects, and 30 application-type projects, I've observed that while the high-level concepts remain consistent, the implementation details vary significantly. For example, when installing dependencies, an open source project might use a simple `pip install -r requirements.txt` command, while an application project requiring deterministic dependencies might use ``Pipenv``, ``poetry``. Similarly, documentation hosting differs - public projects typically leverage GitHub and ReadtheDocs, while private projects need separate private hosting solutions. These differences create cognitive overhead when switching between projects, as developers must remember different commands and processes for essentially the same conceptual task.

The pywf library solves this problem by normalizing these common behaviors through a unified command interface. Regardless of which project I'm working on, I can simply type ``make install`` to install dependencies, and the appropriate underlying mechanism (pip, Pipenv, etc.) will be used based on the project type. Similarly, ``make test`` will run unit tests using the project's preferred testing framework. This approach dramatically reduces the mental burden of context-switching between projects while ensuring consistent and reproducible workflows. Each project type has its own dedicated pywf library that implements the lower-level operational logic, abstracting away the implementation details while maintaining the conceptual similarity. Additionally, I've created cookiecutter templates for each project type that automatically wire up the appropriate pywf library, enabling rapid creation of new project skeletons. This comprehensive system ensures that whether I'm developing a pip-installable library, a private package published to a private repository, or a deployable application that doesn't need pip installation at all, the day-to-day development commands remain consistent and intuitive.


Ultimate
------------------------------------------------------------------------------
**这样设计的好处**

- 对于不同类型的项目可以有不同的工作流, 每个工作流都是由 一个开源库 + 一个 Git Repo Template 组成的.
- 每当需要一个新的项目, 先确定这个项目要使用哪个工作流, 然后用对应的 Template 创建 Repo. 接下来在项目中 ``pip install`` 对应的开源库, 然后用 ``Makefile`` 来把这个开源库的 CLI 命令集成到项目中, 使得在不同的工作流中最终使用的命令都是类似的.


Workflow - Develop A Reusable Project Template
------------------------------------------------------------------------------
这一节我们详细介绍如何从 0 开始开发一个可复用项目模板供以后使用. 这里我们就拿我们最常用的 open_source 项目模板举例. 对于 open_source 项目, Workflow 一般包含这么几步:

- 创建虚拟环境
- 安装依赖
- 进行测试
- 用 GitHub Action 进行 CI
- 用 CodeCov 来生成测试覆盖率报告
- 用 Readthedocs 来 Host 文档网站
- 将项目发布到 PyPI
- 将项目发布到 GitHub Release

要开发并长期维护一个 Workflow, 一般需要三个 GitHub Repo:

1. Seed repo, 也就是一个真实的, 将要发布到 PyPI 的 Open Source 项目, 但是里面没有任何实际的业务逻辑, 只是用于测试 Workflow 的正确性. Workflow 所有的 Action 的自动化逻辑会被作为一个 Python 库放在 ``bin/`` 目录下.
2. Automation Library, 是一个将 Workflow 的每个 Action 的自动化逻辑封装好的一个 Python 库, 用于安装到全局 Python 环境中, 使得我们可以轻松的用同意的命令来执行 Action. 它类似 poetry 的作用. 这个库的核心代码是从 Seed repo 中的 ``bin/`` 目录下拷贝过来的 (一行也不要改).
3. Cookiecutter Template, 是一个使用 `cookiecutter_maker <https://github.com/MacHu-GWU/cookiecutter_maker-project>`_ 工具, 从 Seed repo 反过来生成的 `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ 模板. 以后每次创建新的项目都是从这个模板开始的.

这样设计的好处是, 在开发的时候, 所有 Workflow 的 Action 命令实现和测试都是在 Seed repo 中的进行的. 当我们觉得这些逻辑都成熟了以后, 将其具体实现拷贝到 Automation Library 进行发布. 然后最后在 Cookiecutter Template 中将 Seed repo 反过来变成 Template. 在发布 Cookiecutter Template 之前, 可以本地用 Template 回头生成一个跟 Seed repo 一摸一样的项目, 并拷贝回去用 Git diff 进行比较, 如果没有任何差异 (当然 Workflow Action 也都可以顺利运行), 那么就可以发布了. 而一旦以后要进行任何修改, 都是按照 1, 2, 3 的顺序再来一遍就可以了.

这三个 Git Repo 的命名最好遵循一定的规则. 例如这个 Workflow 是为 Open Source 服务的, 那么这三个 Repo 的名字可以分别是:

1. Seed repo: `cookiecutter_pywf_open_source_demo-project <https://github.com/MacHu-GWU/cookiecutter_pywf_open_source_demo-project>`_, 加 ``cookiecutter`` 前缀, ``demo`` 后缀.
2. Automation Library: `pywf_open_source-project <https://github.com/MacHu-GWU/pywf_open_source-project>`_, 叫 ``pywf_${workflow_name}``.
3. Cookiecutter Template: `cookiecutter_pywf_open_source-project <https://github.com/MacHu-GWU/cookiecutter_pywf_open_source-project>`_, 加 ``cookiecutter`` 前缀.


Workflow List
------------------------------------------------------------------------------
- pywf_open_source (cli = pyos)
    - GitHub Repo 是 Public 还是 Private: Public
    - Public / Private CICD
    - Public / Private Document
- pywf_close_source (cli = pycs)
- pywf_aws_lambda (cli = pyawslbd)
