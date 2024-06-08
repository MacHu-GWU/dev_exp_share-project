.. _data-compliance-overview-en:

Data Compliance Overview EN
==============================================================================

This article kicks off our Data Compliance series, designed to provide a comprehensive understanding of data compliance in the modern business landscape.

.. dropdown:: Data Compliance Series Links

    - :ref:`data-compliance-overview-en`
    - :ref:`ccpa-and-gdpr-compliance-in-data-industry-en`
    - :ref:`worm-compliance-in-data-industry-en`


Overview
------------------------------------------------------------------------------
The explosive growth of the big data industry from 2005 to 2015 was accompanied by a wave of public incidents involving data leaks and security breaches. Some of these incidents had severe consequences, even leading to corporate bankruptcies. To address these issues, government regulators worldwide introduced various compliance requirements to govern how companies manage user data. While some of these requirements are country-specific or limited to certain U.S. states, others have a broader reach, such as those effective throughout the European Union.

Establishing internal compliance departments has become a common practice for companies seeking to mitigate compliance risks, as penalties for non-compliance discovered during audits can be substantial. Data Architects play a crucial role in ensuring a company's data compliance, as they are responsible for designing the underlying data systems.

**Given the vast array of compliance requirements and the diverse technical methods needed to ensure compliance across different data systems, it is not feasible to cover all compliance requirements and technical methods in a single article. Therefore, this article will focus on introducing broadly applicable information relevant to all situations.**


When to Check WORM Compliance
------------------------------------------------------------------------------
**To better prepare for data compliance, let's first consider the circumstances under which a company typically faces data compliance audit requirements from the perspective of its shareholders.**

Companies usually receive data compliance audit requirements in the following situations, which include both regular inspections and incident-triggered audits:

1. **Regular regulatory audits**: Many industries, such as finance, healthcare, and energy, are subject to regular compliance audit requirements. Regulatory agencies conduct routine inspections at specified intervals (e.g., annually or quarterly) to ensure companies' data management practices continue to comply with relevant laws and standards. These audits typically have clear schedules and scopes, allowing companies to prepare in advance.
2. **Incident or complaint-triggered audits**: If a major data security incident (e.g., data breach or hacker intrusion) occurs or a complaint is received from customers, employees, or other relevant parties, regulatory agencies or law enforcement may initiate a special compliance audit. These audits are often sudden, requiring the company to respond promptly and cooperate with the investigation.
3. **Changes in regulations**: When significant changes occur in data compliance regulations applicable to a company, regulatory agencies may require the company to undergo a special audit to ensure its data management practices have been promptly adjusted to meet the new requirements.
4. **Significant business changes**: If a company undergoes significant business changes, such as mergers, acquisitions, reorganizations, or the launch of new products or services, regulatory agencies may require a compliance audit to assess the impact on data management and ensure continued compliance.
5. **Contractual or agreement requirements**: Some commercial contracts or service agreements may include compliance audit clauses. For example, if a company processes sensitive data for a client, the client may require periodic compliance audits to ensure their data is properly protected.
6. **Voluntary audits**: Some companies, driven by their own risk management or compliance goals, may proactively engage third-party auditors to independently assess their data management practices. These voluntary audits can help identify and correct compliance issues early and improve data governance.

In summary, data compliance audits can be regular or triggered by specific events or circumstances. Companies should establish a comprehensive data governance system and always be prepared for audits. Simultaneously, companies should closely monitor relevant regulatory developments and industry best practices, and proactively conduct self-assessments and improvements, rather than passively waiting for external audits. By integrating compliance requirements into daily data management practices, companies can more efficiently and confidently meet various audit requirements.


Consequences of CCPA Non-Compliance and Real-World Examples
------------------------------------------------------------------------------
**If a company is found to be non-compliant by regulators during an audit, what are the potential consequences?**

For instance, if a California-based company is found to be non-compliant with the California Consumer Privacy Act (CCPA), it may face the following consequences:

1. **Fines**: Each violation can result in a fine of up to $2,500, or up to $7,500 per intentional violation. These fines can quickly accumulate for large-scale data breaches or systemic non-compliance.
2. **Lawsuits**: Under the CCPA, if a data breach occurs due to a company's failure to implement reasonable security measures, consumers have the right to sue the company. Successful lawsuits can result in damages of $100 to $750 per consumer per incident, or actual damages, whichever is greater.
3. **Reputational damage**: Failure to comply with data privacy regulations can lead to negative publicity, erode consumer trust, and potentially impact the company's profits.
4. **Injunctions**: Courts may issue injunctions forcing the company to comply with the CCPA, which can disrupt business operations and be costly to implement.

Notable CCPA enforcement actions include:

- In August 2022, Sephora settled with the California Attorney General's office for $1.2 million after being accused of failing to disclose that it sells consumers' personal information and not properly handling opt-out requests.
- In 2020, children's clothing company Hanna Andersson and its e-commerce platform Salesforce agreed to pay $400,000 to settle a class-action lawsuit related to a data breach, alleging violations of the CCPA.

These examples highlight the consequences of non-compliance with the CCPA, a California-specific law. In contrast, fines imposed by the European Union's GDPR on large multinational companies such as Google and Apple can reach tens or even hundreds of millions of euros.


Common Data Compliance Regulations
------------------------------------------------------------------------------
Having understood the impact of data compliance on business owners, let's explore some common compliance requirements in the industry.

1. **General Data Protection Regulation (GDPR)**: The GDPR is a data protection law enacted by the European Union, aimed at strengthening individual data rights. It applies to all organizations processing personal data of EU residents, regardless of their location. Key points include consent, data minimization, data subject rights, and the appointment of a Data Protection Officer.
2. **The Health Insurance Portability and Accountability Act (HIPAA)**: HIPAA is a U.S. law enacted by Congress to protect the privacy and security of patient health information. It applies to all healthcare providers, health plans, and health information clearinghouses. Key points include the Privacy Rule, the Security Rule, and breach notification.
3. **The California Consumer Privacy Act (CCPA)**: The CCPA is a privacy law enacted by the state of California, aimed at enhancing consumer control over their personal information. It applies to companies doing business in California that meet certain criteria. Key points include consumer rights, notice requirements, and enforcement provisions.
4. **The Sarbanes-Oxley Act (SOX)**: SOX is a U.S. law enacted by Congress to protect investors from corporate financial misconduct. It applies to all companies listed on U.S. stock exchanges. Key points include corporate responsibility, enhanced financial disclosures, and internal control assessments.
5. **Payment Card Industry Data Security Standards (PCI-DSS)**: PCI-DSS is a global standard issued by the Security Standards Council founded by major credit card companies to protect cardholder data security. It applies to all organizations that process, store, or transmit credit card information. Key points include building and maintaining a secure network, protecting cardholder data, and regularly monitoring and testing networks.
6. **Children's Online Privacy Protection Act (COPPA)**: COPPA is a regulation issued by the U.S. Federal Trade Commission (FTC) to protect the online privacy of children under 13. It applies to organizations operating websites or online services directed at children. Key points include obtaining parental consent, privacy policy disclosures, and data retention limits.
7. **Family Educational Rights and Privacy Act (FERPA)**: FERPA is a U.S. law enacted by Congress to protect the privacy of student education records. It applies to all educational institutions that receive funding from the U.S. Department of Education. Key points include student access to education records, limitations on information disclosure, and record amendment procedures.
8. **Gramm-Leach-Bliley Act (GLBA)**: GLBA is a U.S. law enacted by Congress to protect consumers' personal financial information. It applies to all companies providing financial products or services. Key points include privacy notices, opt-out options, and information security requirements.
9. **Personal Information Protection and Electronic Documents Act (PIPEDA)**: PIPEDA is a privacy law enacted by the Canadian government to protect the collection, use, and disclosure of personal information. It applies to private-sector organizations in Canada, but some provinces have their own privacy laws that may supersede PIPEDA. Key points include informed consent, data protection, and individual access rights.
10. **Brazil's General Data Protection Law (LGPD)**: LGPD is a privacy law enacted by the Brazilian government to protect personal data and give individuals more control over their data. It applies to all organizations processing personal data in Brazil, regardless of where they are located. Key points include lawful processing, consent requirements, and data subject rights.

These additional compliance requirements, along with those mentioned earlier, form important frameworks for global data privacy and security. In essence, some compliance regulations are regionally specific (based on the origin of user data, e.g., user data from Europe is subject to EU compliance regulations), while others are industry-specific.


Navigating the Data Compliance Audit Process
------------------------------------------------------------------------------
Most readers of this article have likely not personally experienced a regulatory audit process. Here's a brief introduction to the typical stages and activities involved when a regulatory agency or third-party auditor initiates a data compliance audit of your company:

1. **Notification Phase**:
    - The government audit department sends a formal audit notice to the company, outlining the purpose, scope, and requirements of the audit.
    - The company's senior management, including the Chief Executive Officer (CEO), Chief Compliance Officer (CCO), and Chief Information Officer (CIO), receive the notice and begin preparing to respond.
2. **Preparation Phase**:
    - The company establishes an internal compliance audit working group, typically comprising representatives from compliance, IT, legal, and business departments.
    - The working group collects and organizes the required documents and records, such as data management policies, procedure documents, and technical configuration records.
    - The working group may engage external legal counsel or compliance consultants for professional guidance and support.
    - The IT department begins preparing the environment and data needed for system demonstrations and technical reviews.
3. **On-site Audit Phase**:
    - Government auditors arrive at the company for on-site audits.
    - Auditors meet and interview company management and key employees to understand the company's data management practices.
    - Auditors review the documents and records provided by the company, assessing their completeness and compliance.
    - IT personnel demonstrate the functionality and configuration of the data management system to auditors and answer technical questions.
    - Auditors may sample a portion of the data for in-depth inspection and analysis.
4. **Issue Clarification and Rectification Phase**:
    - Auditors may request clarification or supplementary materials from the company regarding issues or concerns identified.
    - The company's working group needs to respond to these requests promptly, providing additional documents, explanations, or evidence.
    - If compliance issues are discovered during the audit, auditors may require the company to submit a rectification plan.
    - The company needs to communicate with auditors to agree on rectification measures and timelines.
5. **Audit Report and Follow-up Action Phase**:
    - After completing the on-site work, auditors prepare a detailed audit report outlining the findings and conclusions.
    - The report is submitted to the company's management and relevant regulatory agencies.
    - If the audit reveals significant compliance issues, regulatory agencies may take further enforcement actions, such as fines or business restrictions.
    - The company needs to address all identified compliance issues promptly, in accordance with the audit report recommendations and rectification plan.
    - The company's compliance and internal audit departments need to continuously monitor and evaluate the implementation of rectification measures.
6. **Ongoing Compliance Phase**:
    - The company should learn from the audit experience and improve its data governance and compliance management system.
    - Compliance should become an integral part of the company's culture and daily operations, not just a response to external audits.
    - The company should conduct regular internal compliance assessments and training to ensure employees understand and adhere to the latest data management requirements.
    - The company should maintain open and transparent communication with regulatory agencies, promptly reporting significant changes and events.

A data compliance audit can span weeks or even months, involving multiple internal and external stakeholders. The company must fully mobilize resources and work closely with auditors while also using the compliance audit as an opportunity to improve internal controls and enhance data governance. Sustainable compliance can only be achieved by deeply integrating compliance into corporate culture and operations.


Data Architects: Key Players in Compliance Audits
------------------------------------------------------------------------------
Ultimately, data systems are built by people, and Data Architects play a critical role in ensuring that these systems meet compliance requirements. Once management decides that the company's data systems need to comply with regulations, a Data Architect typically designs a system architecture that satisfies these requirements. In essence, the Data Architect must understand the specific compliance requirements and ensure the solution meets each requirement when designing the system architecture.

When a company is audited by regulatory authorities, the Data Architect plays a key role in the company's internal compliance audit working group and needs to work closely with the group throughout the audit process, providing technical expertise and support. To better understand what needs to be done during the compliance audit process, let's switch to the perspective of the Data Architect. With this understanding, Data Architects can adequately prepare before a compliance audit arrives. The following are the main responsibilities and deliverables of Data Architects at each stage:

1. Preparation Phase:
    - Participate in developing data management policies and procedure documents, ensuring they meet compliance requirements.
    - Provide detailed documentation of data architecture and data flows, including data models, data dictionaries, ETL processes, etc.
    - Prepare technical configuration documents for the data management system, such as hardware specifications, software versions, security settings, etc.
    - Assist in identifying and collecting system logs, audit trails, and other records relevant to compliance.
    - Coordinate with the IT department to prepare the system demonstration environment and test data.
2. On-site Audit Phase:
    - Introduce the overall design of the data architecture and data management system to auditors.
    - Demonstrate key functions of the data management system, such as data ingestion, version control, retention period management, deletion, etc.
    - Answer auditors' questions about data models, data flows, metadata management, etc.
    - Provide detailed explanations of system configurations, proving they meet compliance requirements.
    - Assist auditors in extracting and analyzing data samples.
3. Issue Clarification and Rectification Phase:
    - Provide clarification and supplementary explanations for technical questions or concerns raised by auditors.
    - Assist in preparing additional technical documents or evidence.
    - Participate in developing rectification plans, proposing technical solutions and implementation steps.
    - Assess the impact of rectification measures on data architecture and system performance.
4. Audit Report and Follow-up Action Phase:
    - Review the technical section of the audit report to ensure the accuracy of findings and conclusions.
    - Assist in developing a detailed technical rectification plan, including required resources, timelines, and milestones.
    - Oversee the implementation of rectification measures, ensuring they meet compliance requirements.
    - Conduct comprehensive testing and validation of the rectified data management system.
    - Prepare a rectification completion report, demonstrating that all technical issues have been resolved.
5. Ongoing Compliance Phase:
    - Incorporate compliance requirements into data architecture design and development processes.
    - Regularly review and update data management policies and procedures to ensure they remain consistent with the latest compliance requirements.
    - Establish monitoring and early warning mechanisms for data compliance to promptly identify and address potential compliance risks.
    - Conduct regular compliance self-assessments and internal audits of the data management system.
    - Provide training and guidance on data compliance to IT personnel and business users.

Throughout the audit process, Data Architects must provide technical leadership, ensuring that all provided documents, demonstrations, and explanations clearly and accurately prove the company's data management practices comply with requirements. Data Architects must also proactively identify and resolve technical compliance issues and drive the implementation of data compliance requirements in daily data management work. By working closely with the compliance audit working group, Data Architects can help the company successfully pass compliance audits and establish a sustainable data compliance management system.


What's Next
------------------------------------------------------------------------------
In the upcoming articles, we will dive deeper into each common data compliance regulation, detailing their specific requirements and using real-world examples to illustrate how to design a data system that meets compliance standards.


References
------------------------------------------------------------------------------
- `IBM - What is data compliance? <https://www.ibm.com/topics/data-compliance>`_
- `Kiteworks - Understanding Key Aspects of Data Compliance <https://www.kiteworks.com/regulatory-compliance/data-compliance/>`_
- `Palo Alto Networks - What Is Data Compliance? <https://www.paloaltonetworks.com/cyberpedia/data-compliance>`_
