Transition from Solution Architect to Enterprise Architect
==============================================================================


Background
------------------------------------------------------------------------------
在我的架构师职业生涯前期, 我主要是偏重于技术方面的 Solution Architect (SA). 也就是说当企业有一个复杂的业务需求, 我能将其转化为技术语言, 并独立设计一个解决方案, 并主导系统的具体实现. 下一步, 我准备转向 Enterprise Architect (EA) 岗位. 这个岗位更偏重于业务和架构的整体规划, 以及对整个企业的技术战略的制定. 这个岗位的工作内容更加宏观, 也更加复杂. 本文将讨论我在这个转变过程中的一些思考和经验..


Difference between Solution Architect and Enterprise Architect
------------------------------------------------------------------------------
下面是我问 ChatGPT 所获得的回答, 答案已经经过我的审查并且修改过了.

**Question**

I am an Principal AWS Solution Architect. I am transitioning to a new role called Enterprise Architect. I want to know the difference between these two role and trying to figure out how could I become a successful Enterprise Architect in general.

**Solution Architect**

    **Responsibilities**

    - Works on large-scale projects or leads a team of architects.
    - Responsible for the overall design of a project, ensuring it meets requirements.
    - Provides mentorship and guidance to less experienced architects.

    **Experience and Qualifications**:

    - Typically has many years of experience in the field.
    - May hold a professional license.
    - Bachelor’s degree in architecture, engineering, or related field is common.
    - Some pursue certifications through organizations like the American Institute of Architects (AIA) or the National Council of Architectural Registration Boards (NCARB).

    **Focus**:

    Primarily on designing buildings, structures, and environments to fulfill company needs.

**Enterprise Architect**:

    **Responsibilities**:

    - Designs, plans, and implements enterprise-wide systems and solutions.
    - Collaborates with stakeholders to understand business needs.
    - Creates holistic solutions by integrating multiple technologies.
    - Works with developers to ensure correct system implementation.
    - Selects and implements enterprise-wide solutions.

    **Experience and Qualifications**:

    - Requires a deep understanding of various technologies.
    - Often deals with the business side of operations.
    - Focuses on overview of the entire organization.

    **Focus**:

    On strategic planning and system integration across the enterprise.

**Key Differences**:

- Scope: Principal Architects focus on project design, while Enterprise Architects oversee enterprise-wide systems.
- Depth: Enterprise Architects dive into technology integration and business needs.

**Advice for Becoming a Successful Enterprise Architect**:

    **Broaden Your Knowledge**:

    - Understand business processes, organizational goals, and industry trends.
    - Learn about emerging technologies and their impact on enterprises.

    **Develop Soft Skills**:

    - Communication: Articulate complex ideas to stakeholders.
    - Leadership: Guide teams and influence decision-making.
    - Problem-Solving: Address organizational challenges.

    **Stay Current**:

    - Continuously learn about cloud computing, security, data management, and architecture patterns.
    - Attend conferences, webinars, and workshops.

    **Network and Collaborate**:

    - Connect with other architects, business leaders, and technology experts.
    - Share knowledge and learn from others.

**My Understanding**

在我看来, SA 和 EA 的核心区别如下:

- SA 倾向于 IT 技术本身, 无论什么技术难题都能功课. EA 倾向于企业需求和业务目标, 服务于特定的企业.
- SA 的工作日常内容多为原型设计, 代码实现. 而 EA 的工作日常多为企业需求, 和各个技术部门的头开会, 以及制定技术战略, 以及 Roadmap.


How to be a good EA - High Level
------------------------------------------------------------------------------
Good. I am trying to come up with an framework to use in my day to day enterprise architecture work.

This framework is designed for the following use case.

Starting with an high level, strategy business objective, how could I fully lead the activities to delivery a successful IT system that fullfill the business goals and making values.

Below are my structure of the framework. Could you help me improve it and add any missing piece? Please add a short description to describe the purpose for each step. I want the output in Restructured Format.

- Step1: Clarify the business objectives and goals.
- Step2: System and Architecture Design.
- Step3: Implementation Planning
- Step4: Execute the Implementation
- Step5: Implementation Review



- Step1: Clarify the business objectives and goals.
    - The main goal in this step is to Convert the vague business objective description into clear, measurable, trackable, actionable goals.
    - Unlike an IT solution that is easy to define without uncertainty, the mapping from strategic business goals to IT solution are often not strateforward, may slightly change overtime, and may have to compromise between limited resources and business confliction. So create some room for flexibility and change.
    - This step mostly involves a lot of meeting with business stackholders, product owner and engineering lead.
    - The outcome would be a business objectives document that describes:
        - The business goals and objectives.
        - Key stakeholders that involved in this project.
        - Key systems that are involved in this project.
        - Feature requirements
        - Non feature requirements
        - How to measure the success
        - Maybe more
- Step2: System and Architecture Design.
    - The main goal in this step is to come up the detailed System and Architecture Design that can be reviewed by the business stakeholder, engineer leads and end users. So that we can planning the implementation strategy and the roadmap based on this.
    - The user of the final system are mostly internal enterprise. Unlike general IT solution, it may have wide range of users from different department of the organization. It is very important to communicate with the end users and understand their expectation. You don't have to strictly meet all the requirements, which usually impossible. But you have to make sure that the final system is acceptable to the end users.
    - Due to the scope of impact of the system, you have many users that may have difference preference. You may need to evaluate multiple approach / products / technologies to meet the requirement. The final decision might not be just one, but a combination of multiple approach.
    - Unlike a regular Cloud Architecture design, The Enterprise solution design usually have multiple tier.
    - Due to the complexity of the system, The architecture diagram should be in three format:
        - system architecture (from engineering point of view)
        - data flow architecture (from data point of view)
        - product architecture (from user point of view)
- Step3: Runaway Planning
    - The main goal in this step is to come up with a detailed road map that can be executed by engineer team to delivery the solution.
    - Split the system into sub-system and components, define the boundary and the external interface of each sub-system and components, considering them as a black box.
    - Determine the implementation lead of each sub-systems.
    - Implementation guide line,  transfer knowledge in verbose or written to make sure the implementation lead can understand the design and the requirement.
- Step4: Implementation
- Step5: System Review


Below are my structure of the framework. Could you help me improve what I am missing? I want the output in Restructured Format.

