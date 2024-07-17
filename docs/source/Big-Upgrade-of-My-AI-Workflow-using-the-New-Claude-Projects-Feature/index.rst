Big Upgrade of My AI Workflow using the New Claude Projects Feature
==============================================================================
注: 本文就是用文中提到的新工作流在 AI 的帮助下生成的. 从构思到定稿共计花费了 10 分钟.


Overview
------------------------------------------------------------------------------
在 AI 辅助工作流程中, 我们经常需要重复使用相同的 prompt 来处理不同的任务. 然而, 在 OpenAI 的 ChatGPT 和早期版本的 Anthropic Claude 网页应用中, 这个过程往往繁琐且耗时. **每次启动新任务时, 用户都需要创建一个新的 session, 重新输入 prompt, 然后才能开始处理特定的用户数据. 这种方法不仅效率低下, 而且在长时间使用后还会因为 context window 过长而导致输出速度显著降低**.

更令人沮丧的是, 当一个 session 变得过长时, 之前的 context 可能与当前任务无关, 这时用户不得不重新开始一个 session 并再次输入 prompt. 这个过程不仅耗时, 而且容易打断工作流程, 影响整体效率.

为了解决这些问题, Anthropic 于 2024 年 6 月 25 日推出了一项革命性的新功能 —— `Collaborate with Claude on Projects <https://www.anthropic.com/news/projects>`_. 这个创新功能彻底改变了用户与 AI 助手的交互方式. 通过允许用户预先设定 Instruction (Prompt), Context, 和 Artifacts, **Claude Projects 使得用户可以基于同一个 project 创建多个 session, 从而消除了每次都需要手动输入 prompt 的繁琐步骤**.

这一功能的推出不仅大幅提高了工作效率, 还为 prompt 的重复利用开辟了新的可能性. 用户现在可以更轻松地管理和优化他们的 prompt, 使 AI 辅助工作流程更加流畅和高效. 在接下来的章节中, 我们将深入探讨 Claude Projects 的工作原理, 以及如何将其整合到现有的工作流程中, 从而最大化 AI 辅助工具的潜力.


How Claude Projects Works
------------------------------------------------------------------------------
Claude Projects 的核心在于其革新性的设计, 旨在简化用户与 AI 之间的交互过程. 根据 Anthropic 官方文档的说明, 这个功能主要包含两个关键组成部分: Custom Instruction 和 Artifacts. 让我们详细了解一下这两个功能:

**Custom Instruction**

Custom Instruction 允许用户为整个 project 设置一个统一的指令集. 这相当于为 AI 助手设定了一个长期有效的 "工作模式". 具体来说:

1. **持久性**: 一旦设置, Custom Instruction 将在该 project 的所有 session 中持续有效, 无需重复输入.
2. **灵活性**: 用户可以随时更新或修改 Custom Instruction, 以适应不断变化的需求.
3. **一致性**: 确保在同一 project 下的所有工作都遵循相同的指导原则, 提高输出的一致性.
4. **效率**: 大大减少了重复输入相同指令的时间, 使用户可以更快地进入实际工作.

**Artifacts**

Artifacts 功能本质上是一个知识库, 为 AI 助手提供额外的上下文和信息. 这个功能的主要特点包括:

1. **多样性**: 支持多种文件格式, 如文本文档、PDF、图片等.
2. **可访问性**: AI 助手可以随时访问这些 artifacts, 用于回答问题或完成任务.
3. **扩展性**: 用户可以随时添加、更新或删除 artifacts, 使知识库保持最新状态.
4. **上下文增强**: 通过提供额外的背景信息, 帮助 AI 生成更准确、更相关的回答.

这两个功能的结合使得 Claude Projects 成为一个强大的协作平台. 用户可以创建针对特定任务或领域的专门 project, 设置相应的 Custom Instruction, 并上传相关的 Artifacts. 这样, 每次启动新的 session 时, AI 助手已经准备就绪, 可以立即开始工作, 而无需重新配置或输入大量背景信息.

通过这种方式, Claude Projects 不仅提高了效率, 还增强了 AI 辅助工作的连贯性和深度. 它为用户提供了一个更加结构化和可管理的方式来利用 AI 技术, 使复杂的, 长期的项目变得更加容易处理.


Integrate with My Own Prompt Management System
------------------------------------------------------------------------------
在 Claude Projects 推出之前, 我一直使用自己开发的 prompt management 系统来管理和组织我的 AI 工作流程. 这个系统主要基于 `Airtable <https://airtable.com/app6Ny0rzgQJRk0T3/tblVyWsExEMJBy39J/viwNDU3oanFhq01Xe?blocks=hide>`_, 它允许我以结构化的方式存储和检索各种 prompt. 然而, 这个系统虽然有效, 但仍然存在一些限制和不便之处.

原有系统的工作流程:

1. 在 Airtable 中创建和组织 prompt
2. 需要使用 AI 时, 打开一个新的 ChatGPT 或 Claude session
3. 从 Airtable 复制所需的 prompt
4. 将 prompt 粘贴到 AI chat interface
5. 开始与 AI 交互

这个过程虽然可行, 但每次都需要手动复制粘贴, 特别是在处理多个相关任务时, 这种方法显得尤为繁琐.

集成 Claude Projects 后的新工作流程:

1. 将 Airtable 中的每个 prompt 转化为一个 Claude Project
2. 设置 Project 的 Custom Instruction, 将原有的 prompt 内容转化为持久化的指令
3. 如果需要, 上传相关的 Artifacts 到 Project
4. 需要使用 AI 时, 直接在 Claude 界面中选择相应的 Project
5. 立即开始工作, 无需复制粘贴 prompt

新的工作流程带来了几个明显的优势:

1. **效率提升**: 消除了复制粘贴的步骤, 大大加快了工作开始的速度.
2. **一致性**: 确保每次使用特定 prompt 时都保持一致, 减少人为错误.
3. **易于更新**: 如果需要修改 prompt, 只需更新 Project 的 Custom Instruction, 立即生效于所有未来的 session.
4. **更好的组织**: Project 功能提供了一个直观的方式来组织和管理不同的 prompt 和工作流程.
5. **知识积累**: 通过 Artifacts 功能, 可以不断积累和更新与特定 prompt 相关的信息和资源.

这种集成不仅提高了我的工作效率, 还为我的 prompt management 系统带来了新的维度. 它使得长期项目的管理变得更加容易, 同时也为 prompt 的迭代和优化提供了更好的平台.

虽然从 Airtable 到 Claude Projects 的迁移需要一定的时间和精力, 但考虑到长期的效率提升和功能增强, 这无疑是一个值得的投资. 随着时间的推移, 我预计这种新的工作方式将大大提高我在使用 AI 辅助工具时的生产力和创造力.


How do I use Claude Projects
------------------------------------------------------------------------------
为了最大化 Claude Projects 的效益, 我采用了一个结构化的方法来组织和使用这个功能. 这个方法基于我之前的 prompt 分类系统, 但进行了优化以适应 Claude Projects 的特性. 我的 prompt 组织结构采用了三层分类法:

1. 第一层: 应用场景的粗粒度描述. 这一层描述了最广泛的应用领域. 例如:

- Technical Writing
- Work Messaging
- Creative Writing
- Data Analysis

2. 第二层: 具体的应用场景描述. 这一层进一步细化了应用场景. 例如:

- Tech Blog Writing
- Chinese to English Translation
- Resume Writing
- Market Research Analysis


3. 第三层: 具体应用场景中的特定任务. 这一层描述了在特定场景下的具体任务. 例如, 在 "Tech Blog Writing" 场景下:

- Brain Storming
- Draft Writing
- Language and Grammar Improvement
- Style Tuning

基于这个分类结构, 我为每个第三层的具体任务创建一个 Claude Project. Project 的命名遵循以下格式:

``${第一层} - ${第二层} - ${第三层}``

例如:

- "Technical Writing - Tech Blog Writing - Brain Storming"
- "Work Messaging - Meeting Organizer  - Formal Email"

使用 Claude Projects 的工作流程:

1. **项目初始化**:
   - 创建新的 Claude Project
   - 设置 Custom Instruction, 包含该特定任务的详细指导
   - 上传相关的 Artifacts, 如参考文档、风格指南等

2. **日常使用**:
   - 在 Claude 界面搜索所需的 Project
   - 决定是继续之前的 session 还是开始新的 session
   - 直接开始工作, 无需重新输入 prompt

3. **维护和更新**:
   - 定期审查和更新 Project 的 Custom Instruction
   - 根据需要添加或更新 Artifacts
   - 对不再需要的 Project 进行归档或删除

这种结构化的方法带来了几个关键优势:

1. **高效检索**: 三层结构使得快速定位所需的 Project 变得简单直观.
2. **一致性**: 确保相同类型的任务始终使用一致的指令和上下文.
3. **灵活性**: 可以轻松地在不同层级添加新的类别或任务.
4. **可扩展性**: 随着工作领域的扩展, 这个结构可以轻松适应新的需求.
5. **知识管理**: 每个 Project 都成为了该特定任务的知识中心, 积累经验和最佳实践.

通过这种方式使用 Claude Projects, 不仅提高了我的工作效率, 还帮助我更系统地组织和利用 AI 辅助工具. 它为长期项目和反复出现的任务提供了一个理想的管理框架, 使得 AI 辅助工作流程更加流畅和高效.


Conclusion
------------------------------------------------------------------------------
Claude Projects 的推出标志着 AI 辅助工具在用户体验和工作流程优化方面迈出了重要的一步. 通过将 prompt management 与持续性 session 管理相结合, 这一功能为用户提供了一个更加高效, 一致且易于管理的 AI 协作环境.

回顾本文的主要观点:

1. Claude Projects 解决了传统 AI chat interfaces 中重复输入 prompt 和管理长 session 的问题.
2. Custom Instruction 和 Artifacts 功能为每个 project 提供了持久化的上下文和知识基础.
3. 将现有的 prompt management 系统集成到 Claude Projects 中可以显著提高工作效率和一致性.
4. 采用结构化的三层分类法来组织 Projects 可以实现高效的任务管理和知识积累.

这种新的工作方式不仅提高了效率, 还为 AI 辅助工作开辟了新的可能性:

- **长期项目管理**: 可以更容易地维护和迭代复杂的长期项目.
- **知识沉淀**: 每个 Project 都成为特定任务领域的知识中心, 促进经验积累和最佳实践的形成.
- **协作增强**: 团队可以更容易地共享和标准化 AI 使用方法, 提高协作效率.
- **个性化 AI 助手**: 通过精心设计的 Projects, 用户可以创建高度专业化和个性化的 AI 助手.

然而, 值得注意的是, 有效利用 Claude Projects 需要初期投入一定的时间和精力来设置和组织. 用户需要仔细考虑如何最好地结构化他们的工作流程, 以及如何设计最有效的 Custom Instructions.

展望未来, 我们可以期待看到更多基于这种模式的创新. 例如, 更高级的 Project 模板共享功能, 或者与其他生产力工具的深度集成. 随着用户逐渐适应这种新的工作方式, 我们可能会看到 AI 辅助工作在效率和创造性方面的显著提升.

总的来说, Claude Projects 代表了 AI 辅助工具向更加成熟和用户友好的方向发展的重要一步. 它不仅解决了当前的使用痛点, 还为未来更广泛、更深入的 AI 应用铺平了道路. 对于那些经常使用 AI 工具的专业人士来说, 掌握和充分利用这一功能无疑将成为提高工作效率和质量的关键因素.
