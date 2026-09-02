## Principle 2: Data Backups

One of the primary operational risks faced by financial institutions is the loss of data, which can occur for various reasons. For example, data may be destroyed by accident, corrupted, converted incorrectly, overwritten with a later version, mixed with the incorrect sort of data, lost during a hardware failure, or simply buried in a large pile of log files where it is hard to detect.

*Data backups* are an effective method for mitigating the risk of data loss. A data backup is a copy of the original data stored in a different place that can be recovered in a case of a data loss accident.

A number of factors need to be considered when building a data backup strategy. I recommend approaching the problem through a *data backup lifecycle*. This includes defining data backup steps and elements such as when to back up (e.g., scheduled, on demand, or event driven), what data to back up (operational, analytical, client), the number of backups to create, backup security (e.g., through encryption), backup storage locations (multizones, geographies, data centers), recovery tests and plans, retention time, and deletion.

## Principle 3: Data Archiving

A variety of data within financial institutions may reach a point where they are no longer actively utilized but are still necessary for future reference, reviews, audits, electronic discovery, litigation, and compliance purposes. Examples include financial transactions, customer information, and regulatory reports.

In addition, regulatory frameworks such as the Bank Secrecy Act (BSA), Federal Deposit Insurance Corporation Improvement Act (FDICIA), and General Data Protection Regulation (GDPR) have established several data retention requirements that financial institutions need to comply with.

To manage this data retention challenge, a common approach is *data archiving*, which refers to the process of moving data that is no longer actively used out of production systems and onto a separate long-term storage system.

### Note

Data archives should not be confused with data backups. Although both are concerned with keeping data in secondary storage, they serve different purposes. Data backups are part of a disaster recovery strategy and are meant to manage data loss accidents. Data archives, on the other hand, serve a data retention purpose.

In addition to compliance and risk management, data archiving lowers storage costs by moving data from more costly high-performance primary storage to significantly less expensive secondary storage (e.g., hard disk drives [HDDs]).

A *data archival policy* is often established to manage data archival. It comprises elements  such as a [data retention policy](https://oreil.ly/S9p9A), data archival software, and data access and discovery functionalities.

## Principle 4: Data Aggregation

Financial institutions engage in diverse operations, including lending, payments, investments, risk management, insurance, proprietary trading, portfolio management, and more. Often, a single institution performs multiple activities simultaneously. For instance, a commercial bank may accept deposits, offer loans, market financial investment products, and provide insurance.

In traditional settings, individual activities within a financial institution are often overseen within distinct organizational silos, each maintaining data about its operations using separate systems. An inherent challenge with such silos is the complexity involved in consolidating data across a large number of business units, legal entities, and disparate data storage systems. This, in turn, may jeopardize a financial institution’s capacity to generate an aggregated view of its activities and risks. Such constraints were one of the primary reasons that banks could not adequately assess their risk exposures and concentration before and during the 2007–2008 financial crisis.

### Note

One thing to keep in mind is that data aggregation is a capability of a data infrastructure, and it doesn’t necessarily mean having all data in the same place.

In response, the Basel Committee published a set of [13 principles](https://oreil.ly/dSCF7) for designing and implementing data aggregation capabilities in financial institutions, primarily banks. Logically, the final implementation of these principles will vary from one financial institution to another. In addition, variations in internal structures among banks may facilitate or hinder the complete implementation of all 13 principles. Indeed, in assessing the adherence to the guidelines, the Basel Committee [observed that banks were not fully compliant](https://oreil.ly/jWYFT), mainly due to the complexity of their internal IT infrastructure.

Several other practices in financial markets emphasize the aggregation of data. For instance, asset and fund managers typically maintain an *Investment Book of Record* (IBOR), a centralized database consolidating investment-related information like transactions, positions, and holdings. Another example is the *Accounting Book of Records* (ABOR), which aggregates accounting-related data on assets, liabilities, transactions, costs, net asset value, and charts of accounts. Another good example are *consolidated tapes*, which refer to systems that aggregate data from different trading venues, offering a unified source of information on trading activity across multiple markets.

## Principle 5: Data Lineage

As a financial data engineer, a practical way to think about data is through the *data lifecycle* approach, also called the *information lifecycle*. The term data lifecycle is [frequently used in industry](https://oreil.ly/8_t-B) to indicate the different phases that data goes through from the initial creation, or ingestion, onward. Based on each financial institution’s particular context, the data lifecycle’s phases and complexity may vary. At a high level, there are five main phases: extraction, transformation, storage, usage, and archiving. However, this process can quickly evolve into a complex chain of steps involving a multitude of actions and operations. Consequently, maintaining visibility into the data lifecycle becomes increasingly challenging, potentially exposing financial institutions to costly risks and errors.

To gain visibility into the data lifecycle, financial institutions need to develop a *data lineage* framework. The term data lineage is used to describe the discrete steps involved in the generation, movement, transformation, storage, delivery, and archiving of data. In other words, it is a feature of the data infrastructure that allows users and engineers to track a given data object throughout its lifecycle. Knowing how the data was generated and what actions were applied to it at each step builds confidence in the data infrastructure, pipelines, and lifecycle. Nowadays, the visibility of data lineage is a valuable feature that is top of mind for consumers, managers, and regulators.

Data lineage can be implemented in a number of ways. The most appealing and user-friendly approach is *lineage graphs*, which display a graphical visualization of data processing history. Importantly, visualization tools may not be performant when the processing logic becomes more complex and intricate. In such cases, detailed step-by-step descriptions of the processing logic are required.

# Audit Trails: A Financial Data Lineage Approach

When working in finance, a common term that you might frequently encounter is [*audit trail*](https://oreil.ly/YmtR4). An audit trail is a special implementation of data lineage that builds a chronological step-by-step data recording system that tracks financial activities such as accounting transactions, financial transactions, trades, buy and sell quote submissions, and any financial activity that can be tracked from its origination onward. An audit trail is often used when an auditor or regulator wants to examine the origin of a certain figure (e.g., earnings per share) or a given financial activity (e.g., quote to sell a specific number of securities). The importance of audit trails has increased remarkably after the flash crash of 2010, where a trader intentionally [submitted an exceptional set of orders (a practice called *spoofing*)](https://oreil.ly/XSfca) in order to manipulate the market in their favor. Thanks to audit trails, regulators were able to identify the person responsible for the orders. Systems such as the Order Audit Trail System (OATS) and Consolidated Audit Trail (CAT) were established to automate the recording of information on orders, quotes, and other trade-related data from all shares traded on the National Market System (NMS). Such systems streamline the lifecycle of an order from reception through execution or cancellation for simple tracking and auditing.

## Principle 6: Data Catalogs

Financial institutions produce and consume vast quantities and varieties of financial, economic, operational, and business data. To create an efficient and reliable data-driven culture, data producers and consumers must be able to search and find all the data they need quickly.

In this context, the idea of *data catalogs* has received particular attention. In simple terms, a data catalog is a set of metadata (i.e., data that describes or summarizes other data) combined with search and data management tools that allow a data producer or consumer to find and document a data asset within a financial institution. In other words, you can think of a data catalog as a central and searchable inventory of all data assets.

Data catalogs can be implemented in a variety of ways based on your data consumption needs and the complexity of your data assets. For instance, it can be a database where you store and search the metadata directly or a full-fledged application with features such as a UI, search and discovery, metadata management, user permission, and API integration. For a practical example of such tools, have a look at the open-source Python-based library [Comprehensive Knowledge Archive Network (CKAN)](https://oreil.ly/uQ7Xn). To see a minimal data catalog in action, check the [online data catalog of LSEG Data & Analytics](https://oreil.ly/Vpu9W).

Crucially, the more advanced and complex a data catalog, the higher the maintenance and curation burden. Conversely, having a sparse or out-of-date data catalog may lead to higher resource use and more wasted time than not having any.16

## Principle 7: Data Ownership

Data ownership is one of the most valuable data governance practices for data-driven organizations. It’s important to note that the term data ownership is used in two different contexts. On the one hand, it can refer to the legal owner of a given data asset. This topic emerged following the considerable increase in data collection practices and the adoption of third-party storage solutions such as the cloud. As more and more data is collected about people and organizations, concerns have emerged regarding who the final owner of the data is. Similarly, with the widespread adoption of public cloud storage solutions, questions have emerged regarding who owns the data stored in the cloud.17

Looking at it differently, data ownership involves designating an individual or team with the task of overseeing the collection, cleansing, maintenance, sharing, and management of a particular data asset within a financial institution. These individuals are often known as *data owners* and are typically selected for their domain expertise. The rationale is that data owners, being subject matter experts, are better equipped and motivated to maintain and manage a specific data asset compared to a centralized team that may lack the requisite domain knowledge to comprehend the data fully.18

## Principle 8: Data Contracts

One of the main factors that can significantly impact the quality of data within organizations is the communication structure. A well-known adage, called [*Conway’s law*](https://oreil.ly/ckLje), is often cited in this context. It states that “organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.” Following this principle, the term *data contract* has recently emerged as a promising approach to organizing requirements and expectations around data. Let’s consider how industry experts define data contracts:

> Data contracts are API-like agreements between Software Engineers who own services and Data Consumers that understand how the business works in order to generate well-modeled, high-quality, trusted, real-time data.
>
> [Chad Sanderson, “The Rise of Data Contracts”](https://oreil.ly/9i_TG)
>
> A data contract is an agreed interface between the generators of data and its consumers. It sets the expectations around that data, defines how it should be governed and facilitates the explicit generation of quality data that meets the business requirements.
>
> Andrew Jones, *Driving Data Quality with Data Contracts* (Packt, 2023)

With a data contract, data consumers can define their data-related needs (e.g., structure, semantics, relations, formatting, fields, frequency, typing, rounding, privacy, and terms of use) and establish an agreement with data engineers to receive data that matches their expectations. This allows data consumers to concentrate on analysis and product development rather than worrying about data generation and engineering. Data engineers, on the other hand, do not need to be concerned about making modifications to the database or data model that may lead to production issues. This is why it is called a contract: both sides agree to it and each needs to hold their end of the deal. Naturally, a data contract can be revised and changed (e.g., a new field is required, a new owner is assigned, etc.) which would result in a new modified agreement.

Currently, general guidelines for implementing data contracts don’t exist. Depending on the institution and its data strategy, different data contract definitions may be established.19 To give an illustrative example, assume that the analytics team needs daily price data for the top 100 US stocks by market capitalization, with no null prices, a price range of 0–1000000 and no missing observations, and the data must be ready by 10:00 a.m. on each working day. In this case, following the data contract specification [proposed by Jochen Christ and Simon Harre](https://oreil.ly/-Rgzk), we can build a basic contract as follows:

```
dataContractSpecification: 0.0.1
id: stock-price-extraction
info:
  title: Daily Adjusted Stock Price Extraction
  version: 0.0.1
  description: daily extraction of the adjusted stock price of the top 100 U.S
               stocks by market capitalization.
  owner: Analytics Team
  contact:
    name: John Smith (Analytics Team Lead)
    email: john.smith@example.com
servers:
  production:
    type: Snowflake
    project: daily_adjusted_prices_prod
    dataset: snowflake_adjusted_prices_top_100_latest_v1
terms:
  usage: Data can be used for financial analysis, backtesting, and machine
         learning use cases.
  sla: 10:00 AM of each working day.
  daily_record_count: 100 observations
  limitations: >
    Not suitable for intra-day financial time series analysis.
    Data may be missing some identifiers such as ISIN.
    Max data processing per day: 10 Gigabytes.
    Max instrument requests per day: 1000 instruments.
  cost: 0.01$ per instrument request
schema:
  type: json-schema
  specification:
    adjusted_prices_top_100:
      description: One record per instrument and date.
      type: object
      fields:
        price_date:
          type: timestamp
          format: date-time
          nullable: false
          description: time of the price observation
        adjusted_price:
          type: numeric
          precision: 4 decimals
          range: 0-1000000
          nullable: false
          description: The adjusted price value.
        instrument_ticker:
          type: string
          description: The ticker identifier of the stock
          nullable: false
```

It’s important to note that data contracts are not about specs or tools, but rather are a design pattern that emphasizes automating data quality and governance across various systems. The final specifications and the tools you will employ depend on your specific business requirements.

## Principle 9: Data Reconciliation

In financial markets, the same financial record often appears across different systems owned by various counter parties, posing challenges for maintaining consistent records. This issue is addressed through data reconciliation, which involves aligning diverse sets of records to create a unified view of financial transactions and balances. This process helps minimize errors and discrepancies, thereby ensuring operational integrity, financial stability, compliance, and customer trust.

A typical data reconciliation process in financial markets is portfolio reconciliation, where records of holdings, transactions, and positions are compared and verified between two or more counter parties, such as financial institutions or investment managers. The International Swaps and Derivatives Association (ISDA) has identified portfolio reconciliation as one of the most advantageous practices in mitigating operational and credit risks in OTC markets.20

For instance, in the fund industry, multiple entities may hold the same portfolio exposure data for a specific fund, such as a management company and a custodian. For instance, suppose a mutual fund is managed by Management Company A, and its assets are held in custody by Custodian B. Management Company A reports a $50 million exposure in technology stocks for the fund, while Custodian B, responsible for safekeeping and reporting the fund’s assets, shows a $49.5 million exposure in the same sector. To ensure consistency and accuracy, portfolio reconciliation is necessary. This process involves comparing the data from both Management Company A and Custodian B to resolve any discrepancies and provide a unified view of the fund’s holdings.

Similarly, in payment processes, multiple entities are involved in storing ledger records, often resulting in discrepancies in ledger balances among banks, FinTech companies, and service providers like BaaS providers. These discrepancies can stem from data duplication, incomplete or inaccurate record-keeping practices, delays or errors during system upgrades, and the inherent complexity of reconciling multiple systems of record.21

# Data Security and Privacy

Financial institutions deal with highly sensitive and valuable data such as customer financial data, money transfers, transactions, investment strategies, and credit card numbers. Consequently, the financial industry has traditionally been a primary target for cyberattacks. To give a few examples, according to a [report by Capgemini](https://oreil.ly/FEpjo), Citigroup US suffered a data breach in 2011 that resulted in data on more than 360K customers being leaked. Citigroup Japan reported a similar breach that affected around 92K customers. Again in 2011, Bank of America suffered a data breach that cost the bank around $10mln.

Additionally, certain aspects of the financial industry make it particularly vulnerable to security threats. First, safeguarding intellectual property through patents and copyrights has been [shown to be more challenging and ambiguous](https://oreil.ly/I4Xfb) in the financial industry than in other industries such as manufacturing. Second, due to the complex inter dependencies of financial systems, a security breach in one financial institution may cause a cascading shock that affects the entire system. Third, the monetary impact of a security breach at a financial institution can be consequential, given that financial data is directly connected to client funds.

Given these considerations, data security and privacy have traditionally been regarded as a top priority by financial institutions and regulatory bodies. If you have worked at a financial institution, you must have noticed that security is given significant weight in practically all discussions. Importantly, while the terms privacy and security may be used interchangeably, they actually refer to distinct problems. To illustrate the difference, I will rely on international standards developed specifically for information security and privacy.

In terms of data security, standard [ISO 27001—*Information Security Management Systems* (ISMS)](https://oreil.ly/1SWTc) is the primary worldwide reference. It specifies a set of guidelines for developing an ISMS system that protects data from cyber threats. The standard guides organizations through the stages required for ISMS development, such as assessing vulnerability risks, developing policies and procedures for data protection, training employees, and managing incidents.

On the other hand, standard [ISO 27701 on developing a *Privacy Information Management System* (PIMS)](https://oreil.ly/kk9xJ) builds on top of ISO 27001 to ensure that a system is in place to ensure that *personally identifiable information* (PII) is handled in accordance with data legislation and regulations (we discuss PII in detail in the [“Data Privacy”](#ch05_data_privacy_1724776831012387) section). The standard guides organizations through the steps needed to ensure the protection of PII, compliance with data regulations, and transparency about how organizations handle personal data.

From the two standards presented above, we can deduce that in designing for security and privacy, we consider different risks. When designing for security, we presume that an adversary may launch a cyberattack against our organization. When designing for privacy, we assume that personal data is not being handled in accordance with the law.

# What Types of Cyberattacks Are Committed Against Financial Institutions?

Financial institutions can be exposed to a variety of cyberattacks. These include but are not limited to the following:

Malware:   Malicious software installed on a device connected to the internal institution system. It can be a virus, spyware, Trojan, or other. If installed successfully, malware can enable the hacker to access sensitive data and compromise critical systems.

Ransomware:   A special type of malware where the hacker gains access to the institution’s data and holds it hostage in exchange for the payment of a ransom.

Spoofing:   When a cybercriminal manages to impersonate and replicate the website of a financial institution (often banks) that looks and functions the same way. If users are not careful, they may end up providing their personal information to the fake website.

Spam and phishing:   An email-based cybercrime where a person sends emails to random people soliciting them to send banking or credit card details.

Distributed denial-of-service attack (DDoS):   This occurs when a cybercriminal floods a financial institution’s server with internet requests.

Corporate account takeover:   When a cybercriminal gains access to a corporate account associated with a financial institution. This may allow the attacker to initiate fraudulent money transfers and other transactions.

Brute force attacks:   When a hacker tries to guess the access credentials of a user via trial and error. Although it might seem outdated, it might still work if passwords are not strong enough.

SQL injection:   A code injection technique where malicious SQL statements are inserted into a specific part of the application accessible to the user in order to manipulate the final query submitted to the backend database. A successful SQL injection attack might lead to data loss, a breach, or corruption.

An important thing to keep in mind is that cybercriminals are creative (newer ways of conducting cyberattacks are continuously being invented) and adaptive (workarounds are developed to circumvent existing security measures). For this reason, ensuring data security at financial institutions requires continuous monitoring, testing, and reinforcement.

The literature and practices surrounding data security and privacy are vast. Different financial organizations may confront different security issues and approach privacy in various ways. Furthermore, planning for security and privacy frequently involves a large number of individuals, including managers, chief information officers, chief security officers, chief technology officers, security experts, network experts, infrastructure engineers, software engineers, data engineers, data architects, and data analysts. This book will concentrate on four major issues of interest to financial data engineers: data privacy regulations, data anonymization, data encryption, and access control.

## Data Privacy

Data privacy is a data governance practice that ensures data is collected, stored, processed, and shared in accordance with data protection laws and regulations, as well as the data subject’s general interests. Data privacy guarantees that sensitive information is not used for reasons other than those consented to by the data subject or established by law. *Personally identifiable information* (PII) is possibly the most sensitive sort of information. PII refers to any data that can be used either alone or in combination with other data to identify an individual. This can include direct identifiers such as a person’s name, address, social security number, or email address, as well as indirect identifiers like birth date, phone number, IP address, or biometric data. In the context of financial markets, financial PII may refer to bank account details, credit card numbers, investment account information, and any other identifiers that could potentially reveal an individual’s financial identity.

A number of data regulations and laws have been devised and put into effect internationally in recent years. The most prominent and comprehensive framework is the European Union’s [*General Data Protection Regulation* (GDPR)](https://oreil.ly/VRxDM).22 In a nutshell, GDPR’s main goal is to give EU citizens more control over their personal data. It applies to all EU citizens as well as the entities that do business with them, including those not based in EU countries. GDPR distinguishes between two types of data processing entities: a *data controller* and a *data processor*. A data controller is an entity that collects personal data and determines the purposes (why) for which and the means (how) by which personal data is processed. If multiple data controllers are involved, then the entity is called a *joint controller*. On the other hand, a data processor is an entity that processes data on behalf of the controller. In most cases, the data processor is an external third-party entity (e.g., a payroll company).

Individual rights defined in GDPR relate mostly to the collection, usage, sharing, transfer, and deletion of personal data. Such rights can be grouped into three categories that you are likely to encounter:

Right to access:   EU individuals have the right to access and request a copy of their personal data, as well as clarifications on how their data is processed, stored, and used.

Right to be forgotten:   EU individuals have the right to request the deletion of their personal data or reject having their data processed.

Data portability:   When feasible, EU individuals should have the right to have their personal data transmitted from one data controller to another.

A variety of similar data protection laws have been introduced worldwide, such as:

* The California Consumer Privacy Act (CCPA) in the US
* The Gramm–Leach–Bliley Act
* Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA)
* Japan’s Act on Protection of Personal Information (APPI)
* Brazil’s General Data Protection Law

With the adoption of these regulations, the demand for privacy-preserving features in system design has increased considerably. As a financial data engineer, your responsibility within this context is related to data collection, visibility, and utilization. For example, if a user consents to the usage of their data for marketing purposes only, then such a restriction needs to be taken into account in the data pipeline(s) that process customer data. A good approach to enforcing data privacy is through data contracts, where all privacy-related requirements are established and agreed upon by both data producers and consumers.

When integrating data privacy elements into system design, a tradeoff might emerge between data confidentiality and data sharing. While limiting data sharing might increase data security and confidentiality, it can also limit prospects for meaningful innovation, both within the financial institution and with external partners. On the other side, enabling excessive data sharing exposes the company to security breaches, legal penalties, and reputational risks.

Ensuring privacy requires having a culture of privacy in the first place. Explaining the impact that privacy infringement can have on the employees is an essential first step. This encourages a due diligence mindset when handling data. Additionally, having management support and interest in enforcing data privacy plays a crucial role. Depending on these and other factors, various financial institutions may invest differently in data privacy standards.23

On the methodological side, a variety of data privacy techniques exist. The most effective of such techniques is data anonymization, which I explain in detail in the next section.

## Data Anonymization

Data anonymization is a data governance practice that ensures both data security and privacy via transformations that obscure the identifiability of the data. If data is properly anonymized, then it loses its essential identification elements and cannot be linked to specific data objects. This in turn makes it useless if it falls into the wrong hands. In financial institutions, anonymization can be adopted as a good data practice, but it may also be mandated by law. For example, GDPR [states](https://oreil.ly/Kb-fJ) that for data to be exempt from certain GRPD privacy restrictions, it needs to be anonymized.24