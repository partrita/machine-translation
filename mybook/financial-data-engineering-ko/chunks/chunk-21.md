## Principle 1: Business Requirements

Although data engineering appears to be a strictly technological discipline, the truth is that it is highly driven by business requirements and customer needs. I highly recommend that you do not proceed with the design of a DSS without first including the business team’s feedback into your decision-making process. As a financial data engineer, you don’t necessarily need to be a business expert, but by knowing just enough to understand business expectations, you are likely to make the best design choices.

Business requirements can vary in terms of complexity (e.g., what and how many features are required?), flexibility (are they strict requirements?), technical feasibility (are there technical limitations?), predictability (can you anticipate the requirements in advance?), timing (have the requirements already been formulated?), and stability (do requirements change with time?).

Examples of data-related business requirements include the following:

* Ease of data access (e.g., a user interface)
* Schema flexibility (e.g., a new feature requires a new field in the data schema)
* User scalability (e.g., a high number of concurrent users)
* Speed of data access (e.g., for high-frequency trading)
* Querying capabilities (e.g., complex analytical queries and filters)
* Storage needs (e.g., storing a massive dataset such as market transactions)
* Data sharing (e.g., to collaborate with external companies)
* Data aggregation (e.g., for regulatory reporting)

DSS design and business requirements are matched through an iterative and collaborative approach. To succeed in this process, financial data engineers need to communicate in business terms and translate the requirements into technical implementation. Along the way, they need to spot all possible bottlenecks or technical limitations and reach an agreement with the business team to achieve feasibility.

## Principle 2: Data Modeling

Data modeling is a crucial, yet often underestimated, practice in DSS design. In general, data modeling focuses on how data is organized, connected, and stored to meet both technical and business requirements. Importantly, the data engineering community still lacks a widely recognized data modeling framework. Nevertheless, market practitioners have typically relied on a popular approach that breaks down data modeling into three sequential phases: *conceptual*, *logical*, and *physical*. These phases are developed as one progresses from business needs to a comprehensive data storage specification, which is the desired end state.

The conceptual phase is technology independent and involves a communicative process where data engineers and stakeholders together discuss all their data needs. Think of the conceptual phase as a whiteboard session where various members of your team meet to discuss the initial data requirements. The main outcome of this phase is identifying a model for data, relationships, constraints, and querying needs that are essential to the business application. At this stage, no decisions are made about how the data will be stored or which DSS will be used for this purpose.

Subsequently, during the logical phase, the conceptual model is mapped to a blueprint of structured and technical constructs such as rows, columns, tables, and documents that a DSS can implement. At the end of the logical phase, you still haven’t picked a specific DSS, but you should clearly know how the data will appear in the DSS and what DSM to use (for example, relational or document models). Later in this chapter, we will discuss DMSs in detail.

Finally, the physical phase translates the logical model into the DSS language, which is often known as *Data Definition Language* (DDL). This stage’s main outcome involves choosing a specific DSS (e.g., a relational database management system) and developing a clear understanding of how data is stored (e.g., on disk, in memory, or hybrid), and how data is replicated, sharded, partitioned, or distributed.

# Data Modeling Use Case in Finance: Reference Data and Financial Standards

In Chapter 2, we discussed the well-known problem of financial reference data, i.e., metadata used to describe financial instruments. The main challenge with reference data is the lack of a universally accepted framework for its representation and formatting, especially for complex financial instruments like derivatives. This issue is an excellent example of a financial domain problem that can be addressed through data modeling. Data modeling offers a robust solution by providing structured and standardized conceptual models for representing, collecting, and storing reference data. For an excellent treatment of this topic, I recommend Robert Mamayev’s book *Data Modeling of Financial Derivatives: A Conceptual Approach* (Apress, 2013), in which he illustrates how to structure and describe derivatives such as futures, forwards, options, swaps, and forward rate agreements using advanced data modeling techniques.

Similarly, the development and formulation of financial standards like ISO 20022 can be viewed through the lens of data modeling. As discussed in Chapter 7, creating an ISO 20022 message model involves conceptual, logical, and physical stages, mirroring the methodology outlined in this section.

An important thing to keep in mind is that data modeling is an iterative process. Data engineers and business teams may continually reorganize, restructure, and optimize data models to fit new or revised business needs.1

## Principle 3: Transactional Guarantee

One of the most important features of a DSS is its ability to ensure data consistency and reliability. In other words, the data must always accurately reflect its true state. For example, if you have $10,000 in your bank account and purchase a book for $50, your new balance should be $9,950, not $9,000. Similarly, if you purchase a book for $50 and at the same time you also purchase a car for $10,000, then you either end up with $9,950 or $0 but not –$50.

This feature is known as a *transactional guarantee*. Here, “transaction” describes an internal DSS mechanism that allows the bundling together of multiple instructions into a single, all-or-nothing operation.2 In the data technology landscape, transactional guarantees are commonly implemented using two main models: *ACID* and *BASE*.

ACID is the most popular model,3 and it stands for:

Atomicity:   A DSS transaction either succeeds completely (gets committed) or, in case of a fault, gets entirely aborted, reverting the DSS to the state before the transaction started. In our previous book and car example, atomicity would mean that either both items are bought (a book and a car) or neither is bought and the account balance remains intact. A violation of atomicity would occur if we attempted to purchase both the book and the car in a single transaction, where the purchase of the book succeeds but the car purchase fails.

Consistency:   DSS transactions need to preserve structural integrity and enforce defined constraints. Consider again our previous example of a $10,050 transaction with an available balance of $10,000. Assume that the account balance has a non-negative constraint. In this scenario, the transaction should fail to prevent the balance from becoming negative, ensuring consistency. Maintaining this consistency is typically the responsibility of DSS engineers, who establish and implement data consistency checks, constraints, and validations based on business requirements, both at the DSS level as well as within the applications that interact with it.

Isolation:   Concurrent DSS transactions get executed in isolation from one another while ensuring integrity and resolving conflicts. For instance, if you attempt two separate transactions—one to buy a book and another to buy a car—and only one can succeed, the DSS identifies this conflict and ensures proper resolution. Maintaining isolation is primarily the responsibility of the DSS. A notable strategy is *snapshot isolation*, where each transaction within the DSS perceives a consistent snapshot of data that includes all committed changes up to the transaction’s initiation.4

Durability:   The DSS preserves and persists the committed transactions even in case of a system failure (e.g., a power outage or crash). In our example, suppose you just completed the book purchase for $50. If the transaction is completed and you receive a notification of success, then the DSS must ensure that your purchase has been recorded in nonvolatile storage such as a hard drive or SSD. One of the most reliable techniques for ensuring durability is *Write-Ahead-Logging* (WAL), whose main idea is to first “log” all changes to be applied to the data before persisting them to disk.

ACID properties are of primary importance for the design of financial DSSs. Examples include financial transaction processing, where money or ownership of financial instruments is transferred between customer accounts, and order matching systems that execute buy and sell orders. In all of these applications, it’s critical to maintain a consistent state of the data by ensuring that transactions either complete entirely or not at all. Throughout this chapter, I will provide detailed technical illustrations of how various DSSs implement and ensure ACID properties.

### Warning

Many data storage solution providers make the ACID compliance promise. However, they don’t all implement it in the same manner. Some may use a portion of the ACID properties (e.g., atomicity) or develop their own version of ACID. When designing a financial application with strict requirements in terms of data consistency and a transactional guarantee, ensure you thoroughly comprehend the ACID features of the chosen solution. If not, this might influence your product’s market reputation.

In some cases, enforcing ACID compliance may impact performance or may not even be that necessary. In other cases, ACID might even be impractical to achieve. This is where a lighter version of ACID, called BASE, has been introduced.

BASE stands for:

Basically available:   Instead of enforcing immediate consistency, BASE-modeled DSSs focus on ensuring availability by distributing and replicating data across a set of nodes in a data storage cluster. In the event of a failure in one node, data would still be available through another node that holds a replica of the data.

Soft state:   As the requirement of immediate consistency is relaxed, the BASE model delegates the responsibility of achieving data consistency to the engineer instead of the DSS itself. In other words, it is the developer’s problem to ensure data consistency, and it is no longer a feature of the DSS itself.

Eventually consistent:   Even though BASE does not aim for immediate consistency, this does not mean that it never achieves it: it is eventually achieved, meaning that data will converge to a consistent state at some point in the future. No guarantee is made, however, about when consistency will be achieved.

The BASE model is quite useful for designing distributed and big data storage solutions, especially for analytical purposes where speed and scalability are more important than strict consistency. For instance, a trading platform might analyze vast amounts of data to provide traders with insights and market trends. In this scenario, the BASE model could be suitable, as it prioritizes processing large datasets quickly, even if some data might be slightly outdated.

## Principle 4: Consistency Tradeoffs

A distributed DSS consists of several machines, or nodes, working together to store and manage data collectively. Designing and building such systems can be highly complex. Several consistency tradeoff theorems have been formalized to assist engineers with this challenge. The most prominent is the CAP theorem, which stands for consistency, availability, and partition tolerance. According to the CAP theorem, if a *network partition* occurs, where some nodes in a distributed DSS are unable to communicate due to a network failure, the system can guarantee at most two out of the following features:

Consistency:   All users always see the same latest version of the data, regardless of which node they interact with.

Availability:   The DSS responds to all user requests at all times, though it may not always provide the most recent data.

Partition tolerance:   The data storage system continues to operate even when there is a network partition.

### Note

Keep in mind that consistency in ACID is different from consistency in the CAP theorem. In the CAP theorem, consistency means that all nodes maintain a consistent view of the data. Conversely, in the context of ACID, consistency ensures that the database remains in a valid and correct state.

To illustrate the CAP theorem with an example, suppose we have a bank with two ATMs connected over a network.5 Assume the bank requires that customer balances never drop below zero, but there is no central database system to ensure this condition. Instead, a copy of the database is stored on both ATM instances, and as users carry out their operations on their accounts, the two ATMs communicate over the network to ensure consistency.

Now, suppose that a network partition happens, and the two ATMs can no longer communicate. In such a case, you, as the designer of the DSS, need to decide whether to prioritize consistency or availability. If you prioritize consistency, you are likely to refuse all ATM operations (withdrawal, deposit, balance checks) until the partition is resolved. This guarantees balance consistency, but the ATM services will not be available to customers. If, on the other hand, you favor availability, then you may allow each ATM to perform deposit and withdrawal operations but at the risk of ending in an inconsistent state until the partition is resolved (e.g., withdrawing the entire balance from both ATMs, ending up with a negative balance).

Keep in mind that the CAP theorem is quite simplistic and basic. In real applications, tradeoffs might be more complex than just 100% availability or 100% consistency. For example, in our ATM example, rather than completely blocking or allowing all ATM operations, the bank may still allow for balance inquiry or small money withdrawals during a partition and only refuse large withdrawals and deposits.

As an extension of the CAP theorem, the PACELC theorem was introduced. PACELC considers two system scenarios: first, if the system has a network partition, it must decide how to trade off consistency and availability; second, if the system is running normally without a network partition, it must still decide how to trade off consistency and latency. The latency/consistency tradeoff exists only if the distributed DSS replicates data.6

When working with distributed DSSs, several of them offer the option to tune the consistency level. For example, Azure Cosmos DB [offers five levels of consistency guarantees](https://oreil.ly/8wo-0), which, from strongest to weakest, are strong, bounded staleness, session, consistent prefix, and eventual; Amazon DynamoDB offers either strong or eventual consistency levels; and Cassandra [offers several consistency levels](https://oreil.ly/pRt15) that also range from weak to strong.

## Principle 4: Scalability

Scalability is a highly desired property of DSSs. Generally, a system is considered scalable if it can effectively handle varying or increasing amounts of workload. Importantly, scalability can be achieved differently depending on the component or layer of the DSS. To simplify, we can categorize DSS scalability into two main aspects: storage scalability and compute scalability.

A DSS achieves storage scalability if it can seamlessly store increasing volumes of data without hitting a space limitation. In more practical terms, storage scalability means that the system can store data at any scale: gigabytes, terabytes, or even petabytes.

Conversely, compute scalability in a DSS refers to its ability to efficiently handle varying data read and write requests. A common measure of compute scalability is the maximum number of concurrent read/write requests that the DSS can accommodate.

Scalability can be achieved in multiple ways. One approach is vertical scalability, where a single machine is replaced with a bigger one that has more storage, CPU, and RAM. On the other hand, horizontal scalability requires a distributed system that scales by adding a new node to an existing cluster of connected nodes.

When designing a DSS, it is crucial to evaluate its capability to handle anticipated workloads. This is often done via stress testing and benchmarking. A database stress test works by simulating the generation of a large amount of data, queries, and concurrent requests while observing how the DSS behaves in terms of response time, errors, and reliability. The goal, in lay terms, is to stress the DSS to identify its operational limits and where it may encounter system failures or breakpoints.

A *database benchmark* is a special type of database stress test that relies on well-defined and industry-accepted testing methodology. Examples include [Transaction Processing Performance Council (TPC) standards](https://oreil.ly/f1hUS) such as TPC-C and TPC-E.7 TPC-C simulates an order-entry environment where a population of users concurrently submit a variety of transactions against a database. Transactions may vary in complexity and include placing and fulfilling orders, keeping track of payments, confirming order status, and checking the level of stock in the warehouse. TPC-C evaluates performance based on the number of new-order transactions processed per minute.

TPC-E is a more sophisticated benchmark that simulates a brokerage firm receiving and fulfilling various customer transactions related to trades, account inquiries, and market research. To execute client requests, the brokerage firm interacts with financial markets and updates account information. Performance is measured using the transactions per second (TPS) metric.

A best practice is to conduct both industry benchmark tests and internally defined ad hoc tests to gain insights into specific behaviors of the DSS that may not be fully addressed by standardized benchmarks. Commercial database vendors frequently employ this dual approach to showcase the robustness and reliability of their products.8

## Principle 5: Security

Ensuring strong database security is crucial in financial applications. When designing for security, a variety of processes, tools, and controls can be put in place to protect a DSS against malicious or accidental threats. These include, for example, the following:

* Data encryption at rest (e.g., customer account information residing in a database)
* Data encryption in transit (e.g., when transmitting payment information over a network)
* Database access permissions and roles
* Separation of database servers from other application servers
* Backups and data recovery plans
* Real-time security information and event monitoring

Data security features vary across different DSSs. Therefore, it’s essential to stay informed about your institution’s specific security requirements and ensure that the chosen DSS can effectively meet them.

# Data Storage Modeling

To implement a DSS, a large number of technological choices are available. However, comparing such technologies is not trivial. Some technologies share several features, yet others may be based on noncomparable design principles. Additionally, on occasion, even the lines between the different data technologies might become blurry as they introduce more of the same features. To this end, this book will take a different approach by relying on the concept of *data storage models* (DSMs) rather than data storage technologies.

A DSM refers to the logical design and structure of a DSS, which determines the manner in which data can be stored, modeled, optimized, accessed, and manipulated. The concept of a DSM is closely related to the general practice of data modeling discussed earlier. To better contextualize things, consider a DSM as a focused subset within data modeling that specifically addresses the logical data modeling phase.

DSMs are technology agnostic, allowing them to be implemented using a variety of technologies, with the possibility of employing the same technology for implementing different DSMs. As a result, conceptualizing in terms of DSM is considerably easier and less susceptible to technology-specific limitations.

In today’s data engineering landscape, a variety of DSMs are available. In the following sections, I will cover eight DSMs in depth, highlighting their main features and applications in finance. But first, let’s illustrate a number of popular criteria that are often used to categorize DSMs.

## SQL Versus NoSQL

If you are part of the data engineering community, you often hear discussions comparing NoSQL and SQL. However, many argue that the SQL versus NoSQL comparison lacks a clear technical basis. But to illustrate the main idea, I will briefly explain its origin.

In data engineering, the most trusted type of DSSs have traditionally been relational database management systems, or more simply, SQL databases (illustrated in detail in the section [“The Relational Model”](#ch08_the_relational_model_1724776834233954)). With the massive increase in data volume, variety, and velocity, traditional SQL databases hit scalability and performance limitations. In a nutshell, SQL databases could only scale vertically, which is a limited scaling strategy since it is constrained by the maximum capacity of a single server.

To overcome this issue, people began exploring more scalable and high-performance alternatives. This led to the development of a new family of database technologies such as document, graph, key-value, and wide-column databases. To distinguish these database technologies from traditional SQL databases, they were grouped under the label NoSQL, which stands for “Not only SQL.” NoSQL databases tackled the issue of scalability by adopting a horizontal scaling approach that relies on distributed systems and partitioning principles.

Importantly, SQL databases adhere to internationally recognized SQL standards, which have contributed to their reliability and trust within the data engineering community. In contrast, NoSQL databases are diverse and lack standardized behavior or common standards. Moreover, to ensure high performance, some NoSQL databases sacrifice several of the core features that gained SQL popularity, such as integrity constraints, ACID transactions, and advanced querying capabilities. Keep in mind, however, that NoSQL is not always more performant than SQL; it mostly depends on the function for which it is used.9 Additionally, it is worth noting that later developments in database technologies made it possible for SQL databases to scale horizontally, thus reducing the gap between SQL and NoSQL.10

## Primary Versus Secondary

A primary DSS is designed to act as the secure and permanent repository for data storage.

Think of the primary DSS as the stronghold of your data. But in many cases, the primary DSS may not have all the features needed to interact with the data. This is where a secondary DSS comes into the scene. A secondary DSS reads and stores a copy of data from a primary database and allows users to perform more advanced data querying and filtering operations.

A secondary DSS may not maintain the same level of data consistency as the primary DSS, but it is generally intended for use cases where this discrepancy does not cause significant issues.

A secondary DSS is typically utilized in situations where the primary DSS stores massive amounts of log or text data, which might be valuable if analyzed using sophisticated search queries. In this scenario, a search engine-like secondary DSS (e.g., Elasticsearch) may be implemented to regularly fetch and index log data from the primary DSS (more on Elasticsearch in [“The Document Model”](#ch08_the_document_model_1724776834234987)). Every time you see an additional monitoring dashboard bundled with an application such as an orchestration engine or a managed database, it’s very likely that a secondary database is used for this purpose.11

## Operational Versus Analytical

A DSS can be designed to handle different types of business processes. In data engineering, a distinction is often made between operational and analytical processes. Operational processes refer to the day-to-day operations and transactions within a business. Examples may include the following:

* Find customer account details.
* Update the account balance.
* Record and track financial transactions.
* Execute a payment or fund transfer orders.

Analytical processes, on the other hand, are concerned with understanding what is going on within a business; for example:

* Assess the performance of the trading desk.
* Monitor the effect of different investment strategies.
* Understand the main cost and profit drivers.

DSSs intended to handle operational processes are often called *online transaction processing* (OLTP), while those designed for analytical processes are known as *online analytical processing* (OLAP). Generally speaking, OLTPs prioritize reliability and transactional guarantee, while OLAPs favor speed and advanced querying capabilities. A typical scenario involves the use of OLTP as a primary DSS for business transactions and an OLAP as a secondary DSS that stores a copy of OLTP data for analytical purposes.

## Native Versus Non-Native

A DSS can serve a single function or a variety of functions. For instance, it might be designed for storing and querying tabular data exclusively, or it could handle document, graph, and key-value data as well. Crucially, various types of design optimizations may be required for supporting each function. This is where a relevant distinction is often drawn between *native* and *non-native* DSSs.

To illustrate the difference, let’s say we want a DSS to store and query graph data. A DSS that is specifically designed and optimized for graph data (e.g., Neo4j) is called *native*, whereas a DSS that is capable of handling graph data but was not primarily designed for graphs in mind (e.g., PostgreSQL) is called non-native.12

Choose a native DSS when your application’s core functionality relies on an optimized DSS tailored for specific tasks (for example, choosing a native graph DSS for a network analysis application).

## Multi-Model Versus Polyglot Persistence

Having in mind the difference between native and non-native DSSs, another important distinction is often made between multi-model and polyglot persistence DSS patterns. Polyglot persistence uses different native DSSs for each function. For instance, you can use PostgreSQL for storing user account information data, Neo4j for managing social network data and graph-based queries, MongoDB for storing and querying user-generated content and posts, and Redis for caching frequently accessed data for improved performance.

Alternatively, a multi-model DSS supports multiple DSMs within a single integrated environment. Such a system may offer support for different DSMs either natively or through extensions. For example, PostgreSQL is a native relational DSS, but it also offers extensions for geospatial data (PostGIS) and image data (PostPic). On the other hand, solutions such as Microsoft Azure Cosmos DB offer native support for document, graph, and key-value data models.

The polyglot persistence approach offers better performance, but it may add significant overhead. In contrast, the multi-model is much simpler but may end up behaving like the proverbial “Jack of all trades, master of none,” which means that while it can accomplish a lot, it won’t provide outstanding performance at any one function.

### Note

Keep in mind that data storage technologies are continuously evolving and adding new features and functionalities. If a given data storage technology doesn’t support a specific feature today, it doesn’t mean it won’t tomorrow. A missing feature is often an optimization choice that can be changed in a future release.

# Data Storage Models

Now that you understand what a DSM is, let’s explore the various types of DSMs you might encounter when building a DSS for financial data. Remember, these models are not mutually exclusive. Financial institutions often use a mix of DSMs to construct DSSs for a range of operational and analytical purposes.

## The Data Lake Model

A data lake serves as a centralized repository capable of storing massive amounts of data in raw, unprocessed formats. Data lakes are the most flexible type of DSS since they allow for reliable and cheap storage of any type of data: big or small, structured or unstructured, static or stream. In a typical scenario, data lakes are used to store large amounts of miscellaneous data, including files, news text, documents, logs, data snapshots, archives, and backups.

### Why data lakes?

Data lakes provide several features that financial institutions often seek. These include the following:

Data variety and agility:   Data lakes offer a flexible storage solution to ingest, store, and analyze any type of data without the need to define a schema or enforce a structure. Data lakes are said to implement *schema on read,* meaning that the data schema is generated on the fly during data query*.* This is in contrast to *schema on write,* where data is first modeled and structured before being stored.

Simple data ingestion:   Data ingestion into a data lake is simple and cost-effective because it does not necessitate transformations or harmonization, thereby lowering data ingestion expenses.

Data integration:   Data lakes are useful for organizations that want to consolidate all their data in one central place. This can be practical for purposes such as compliance, data aggregation, risk management, and customer analysis, as well as experimenting with new ideas and datasets. Moreover, it eliminates data silos within the organization.

Data archiving:   Data lakes offer a cost-effective solution for data archiving and retention.

Data analysis and insights:   Data lakes store data in their original raw format. This allows organizations to perform ad hoc data querying and transformation and access historical snapshots of data.

Data governance:   Data lakes can be designed with data governance practices, including access control, cataloging, auditing, reporting, and compliance.

Separation of storage and compute:   Data lakes can scale to accommodate large volumes of data and access patterns. If you implement a computation layer on top of a data lake, this means that you have a separation of storage and compute layers. With such separation, you can scale and manage storage and computation independently.

It’s important to remember, however, that data lakes are not query-optimized in the same manner as relational databases or data warehouses. Furthermore, performance may be impacted by a data lake’s growing size or deeply nested hierarchical structure.