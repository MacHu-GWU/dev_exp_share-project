ML Ops Product Vendor Evaluation Tracker
==============================================================================


Background
------------------------------------------------------------------------------
作为一个 Enterprise Architect, 我需要选择一个 Vendor 作为公司的 ML Ops Platform Software 的提供商. 我通过一系列的调研, 以及跟内部的  Stack holder 和 User 开会, 心中对这个 Platform 的要求已经比较清晰了. 现在有 2 - 3 个 Vendor 在我心中比较有竞争力. 我需要对这些 Vendor 进行评估, 然后根据评估的结果做出最终的选择. 并且我需要对 C 级别的人汇报这个决策, 所以我需要能用浅显易懂的语言来支持我的决策.

我希望根据企业的需求, 列出所有需要的 Features, 然后评估每个 Vendor 是否能满足我们的要求. 我们一共可能有 50 多个 features 需要评估, 我一个人是没有时间和精力来一个个的评估的, 所以我需要写一篇细致的文档, 对每一个 Feature 进行说明, 并且给出评估的标准. 这篇文档可以用于指导其他的 Engineer 来帮助我完成评估的工作. 我希望对于每一个 Feature 的说明足够细致, 确保能在尽量避免面对面沟通的情况下, 让其他 Engineer 能够精准的理解我的要求. 然后我的评估标准一定要是可以量化, 可以复现的, 可以追溯. 例如可以用一段简单的代码进行测试, 可以引用一篇官方文档的说明作为论据.

由于有 50 多个 Features, 这篇文档的工作量很大, 所以我希望能用 AI 来帮助我完成这个文档的写作. 本文记录了我是如何使用 AI 来帮助我完成这个文档的写作的过程.


AI Powered Workflow
------------------------------------------------------------------------------


1. 决定文章的结构大纲
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
根据我的思考这篇文档的大纲结构如下:

1. What is this: 介绍这篇文档的目的和背景.
2. ML Architect read this: 这篇文档的读者主要有三类: ML Architect 架构师, 设定评估的框架以及做出最后的决策; ML Engineer 工程师, 负责具体的评估工作, 工作量较大; Project Manager 项目经理, 负责协调工作, 确保评估工作的顺利进行. 所以我需要写明这三类读者应该怎样来使用这篇文档.
3. ML Engineer read this: 同上.
4. Project managers read this: 同上.

接下来就是列出所有的 Requirements, 并且针对每一个 Requirements 都要有下面四个部分:

1. Description: 简短介绍这个 requirements
2. Instruction: 介绍如何评估这个 requirements, 以及评估的标准
3. Conclusion: 留空, 供评估人员填写
4. Reference: 留空, 供评估人员填写

其中我要写的部分是 Description, Instruction.


1. Improve My Prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Input:

    I am writing an prompt to guide the AI to do some architecture design tasks, help me improve my prompt, and focus on fixing my gramma and make it more likely to generate high quality response. Below is my prompt draft:

    # Objective

    I am doing a work to evaluate a ML Ops product's capability in ML Visibility, logging and monitoring. I have a long list of bullet points about the product's capability in mind. For each bullet point, I will put a brief description about why I care this capability. I need to assign the evaluation task to other engineers on my team.

    Could you come up with a short description, and a few actionable items for each topic, so that these information can instruct the engineer to do their work?

    # Instruction

    1. I will provide one bullet point at a time.

    2. The description should be on high level and easy to understand. It should be no more than three sentences.

    3. Give at most three actionable items for each topic. The actionable items should be specific, executable, reproducable and measureable.

    # Output Guideline

    The output should be in markdown format. Below is an example:

    <example-output>
    ## Model Management - Model Artifacts Management

    - Description: <put the short description here>

    - Instruction:

    - <actionable item 1>

    - <actionable item 2>

    - <actionable item 3>

    - Conclusion: <intentionally left blank>

    - Reference: <intentionally left blank>

    </example-output>

Output:

    Here's the improved version of your prompt with better grammar and clarity:

    # Objective

    I am evaluating an ML Ops product's capabilities in ML Visibility, logging, and monitoring. I have a long list of bullet points in mind, each representing a specific capability of the product. For each bullet point, I will provide a brief description explaining why that particular capability is important to me. I need to assign the evaluation tasks to other engineers on my team.

    Could you help me create a short description and a few actionable items for each topic? This information will guide the engineers in performing their evaluation work effectively.

    # Instructions

    1. I will provide one bullet point at a time.

    2. For each bullet point, create a high-level description that is easy to understand. The description should be concise, consisting of no more than three sentences.

    3. Provide a maximum of three actionable items for each topic. The actionable items should be specific, executable, reproducible, and measurable.

    # Output Guidelines

    Please provide the output in markdown format. Below is an example of the expected output structure:

    <example-output>

    ## Model Management - Model Artifacts Management

    - Description: <put the short description here>

    - Instructions:
      - <actionable item 1>
      - <actionable item 2>
      - <actionable item 3>

    - Conclusion: <intentionally left blank>

    - Reference: <intentionally left blank>

    </example-output>

    By following this format, you will create a standardized and easy-to-follow guide for the engineers to perform their evaluation tasks effectively.

2. Generate Description and Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Input:

    # Objective

    I am evaluating an ML Ops product's capabilities in ML Visibility, logging, and monitoring. I have a long list of bullet points in mind, each representing a specific capability of the product. For each bullet point, I will provide a brief description explaining why that particular capability is important to me. I need to assign the evaluation tasks to other engineers on my team.

    Could you help me create a short description and a few actionable items for each topic? This information will guide the engineers in performing their evaluation work effectively.

    # Instructions

    1. I will provide one bullet point at a time.

    2. For each bullet point, create a high-level description that is easy to understand. The description should be concise, consisting of no more than three sentences.

    3. Provide a maximum of five actionable items for each topic. The actionable items should be specific, executable, reproducible, and measurable.

    # Output Guidelines

    Please provide the output in markdown format. Below is an example of the expected output structure:

    <example-output>
    ## Model Management - Model Artifacts Management

    - Description: <put the short description here>

    - Instructions:

    - <actionable item 1>

    - <actionable item 2>

    - <actionable item 3>

    - Conclusion: <intentionally left blank>

    - Reference: <intentionally left blank>

    </example-output>
    By following this format, you will create a standardized and easy-to-follow guide for the engineers to perform their evaluation tasks effectively.

    # My write Up

    <my-write-up>
    LLM Visibility - LLM API Call Logging: the product should be able to send the input, output of LLM API call event to a stream data processing pipeline or analytics data store for future analysis. If it can automatically capture other data points like timestamp, sender ID, metadata of the LLM model been used, it is a big plus. If the logging activity can be done out-of-the-box of effortlessly integrated with enterprise's existing system, it is a big plus.

    </my-write-up>

Output:

    ## LLM Visibility - LLM API Call Logging

    - Description: The product should have the capability to log LLM API call events, including input, output, and additional metadata, to a stream data processing pipeline or analytics data store. Automatic capture of relevant data points and seamless integration with existing enterprise systems are highly desirable.

    - Instructions:
      - Verify if the product can log the input and output of LLM API calls to a designated data store or processing pipeline.
      - Check if the product automatically captures additional data points such as timestamp, sender ID, and metadata of the LLM model used during the API call.
      - Investigate the ease of integration between the product's logging functionality and the enterprise's existing stream data processing pipeline or analytics data store.
      - Assess the level of effort required to set up and configure the logging functionality, considering factors like configuration complexity and the need for custom development.
      - Evaluate the performance impact of enabling logging on the overall system and ensure it doesn't introduce significant latency or resource overhead.

    - Conclusion: <intentionally left blank>

    - Reference: <intentionally left blank>

3. Fine Tune the Description and Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Input:

    I want to update these two bullets. The idea is actually good. But I want to make it more clear. What I want to mention in #1 is that, let's say I want to send the API event to an existing enterprise stream processing pipeline or data warehouse, what is the integration method? What is the level of effort it takes. What I want to mention in #2 is that, let's say we already have some LLM API call application, now we want to add logging capability, how can we do that? what is the level of effort it takes? Could you reword these two bullets?

    1. Investigate the ease of integration between the product's logging functionality and the enterprise's existing stream data processing pipeline or analytics data store.
    2. Assess the level of effort required to set up and configure the logging functionality, considering factors like configuration complexity and the need for custom development.

Output:

    Here are the updated bullets based on your clarification:

    1. Evaluate the integration methods available for sending LLM API call events from the product to an existing enterprise stream processing pipeline or data warehouse. Assess the level of effort required for integration, considering factors such as supported protocols, APIs, and connectors, as well as any necessary configuration or mapping of data formats.

    2. Investigate the process and effort required to add logging capabilities to an existing LLM API call application. Determine if the product provides libraries, SDKs, or plugins that can be easily integrated into the application code. Assess the level of code changes, configuration, and any additional dependencies needed to enable logging functionality in the existing application.

4. Final Write Up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example:

    LLM Visibility - LLM API Call Logging

    - Description: The product should have the capability to log LLM API call events, including input, output, and additional metadata, to a stream data processing pipeline or analytics data store. Automatic capture of relevant data points and seamless integration with existing enterprise systems are highly desirable.
    - Instruction:
        - Verify if the product can log the input and output of LLM API calls to a designated data store or processing pipeline.
        - Check if the product automatically captures additional data points such as timestamp, sender ID, and metadata of the LLM model used during the API call.
        - Evaluate the performance impact of enabling logging on the overall system and ensure it doesn't introduce significant latency or resource overhead.
        - Evaluate the integration methods available for sending LLM API call events from the product to an existing enterprise stream processing pipeline or data warehouse. Assess the level of effort required for integration.
        - Investigate the process and effort required to add logging capabilities to an existing LLM API call application. Determine if the product provides libraries, SDKs, or plugins that can be easily integrated into the application code. Assess the level of code changes, configuration, and any additional dependencies needed to enable logging functionality in the existing application.
    - Conclusion:
    - Reference:
