# Chapter 6. Overview of the Financial Data Engineering Lifecycle

As a financial data engineer, navigating the multitude, diversity, and complexity of available technological options can be overwhelming. Without a systematic approach in mind, this complexity may lead to chaotic situations and accumulating costly technical debt. Therefore, this chapter introduces a structured approach to financial data engineering, organizing its components into a layered architecture called the *financial data engineering lifecycle* (FDEL). This framework draws inspiration from the foundational [work of Joe Reis and Matt Housley](https://oreil.ly/9Nuvv) on data engineering lifecycles.

In this chapter, I will introduce the FDEL and outline its four layers: ingestion, storage, transformation and delivery, and monitoring. Following this, I will discuss specific criteria that financial data engineers can consider when selecting technologies to support the FDEL. Please note that since there is so much information to cover, I’ll save the details of each FDEL layer for Chapters 7 through 10.

# Financial Data Engineering Lifecycle Defined

Data engineering is a fast-moving and continuously evolving field. However, if there is one constant that characterizes and defines the job of a data engineer, it is the fact that it revolves around systems that perform a series of actions for the extraction, transformation, storage, and consumption of data.

To move beyond the simple view of data engineering as merely a series of data-related tasks, authors Joe Reis and Matt Housley [introduced the *Data Engineering Lifecycle* (DEL)](https://oreil.ly/9Nuvv). This concept offers a structured framework that formalizes the various stages of data engineering. According to the authors, the DEL “comprises stages that turn raw data ingredients into a useful end product, ready for consumption by analysts, data scientists, ML engineers, and others.”

### Note

It is essential to differentiate between the data lifecycle and the data engineering lifecycle. While they are related, the data lifecycle is a conceptual model that describes the stages data goes through from creation to archival or deletion. On the other hand, the data engineering lifecycle is a practical framework that outlines the processes, patterns, and tools used to manage data throughout its lifecycle, ultimately delivering a final product to data consumers.

The DEL can be adapted to incorporate several processes or stages depending on how complicated the data lifecycle and business needs are. In their original work, Joe Reis and Matt Housley divided the DEL into five stages: data generation, storage, ingestion, transformation, and serving.

When applied to the financial domain, the data engineering lifecycle needs to be adapted to account for a number of domain-specific elements. These originate from the strict data governance and regulatory requirements for financial institutions, legal and content licensing constraints, the complexity of the financial data landscape, industry-specific software standards and protocols, and the unique demands for low latency, high throughput, and other performance constraints that characterize financial operations.

To offer a domain-focused perspective that incorporates these considerations, this book introduces the *financial data engineering lifecycle* (FDEL), a layered framework1 consisting of four layers: *ingestion layer, storage layer, transformation and delivery layer,* and *monitoring layer*. [Figure 6-1](#ch06_figure_1_1724776831611460) illustrates this framework.

In the ingestion layer, data engineers design and implement an infrastructure for handling the generation and reception of data coming from different sources and in different formats, volumes, and frequencies. This layer is quite critical, as errors or performance bottlenecks in ingestion are likely to propagate downstream and impact the entire FDEL. In Chapter 7, we will explore the ingestion layer in depth, covering various ingestion processes, patterns, technologies, and formats.

Following is the storage layer, where the focus is on selecting and optimizing data storage models and technologies to meet various business requirements. Choosing the right data storage system for a given problem is one of the most important decisions throughout the FDEL. A poor data storage choice can very easily translate into bottlenecks, degraded performance, and rocketing costs, which in turn can jeopardize product development and analytical capabilities. Chapter 8 will detail the varieties of data storage models and illustrate their data modeling principles, internal features, and financial use cases.

### Figure 6-1. Layers of the financial data engineering lifecycle

![Figure 6-1. Layers of the financial data engineering lifecycle](images/fden_0601.png)

Next is the transformation and delivery layer, which performs a number of business-defined transformations and computations that produce high-quality data that is ready for consumption by its intended data consumers. In Chapter 9, I will thoroughly explore this layer, examining the key types of transformations applicable to financial data, the computational demands of different transformation processes, and the various mechanisms for data delivery.

Finally, the monitoring layer is there to make sure that issues related to data processing, data quality, performance, costs, bugs, and analytical errors are all monitored and tracked to allow efficient and timely fixes. Chapter 10 will be dedicated to this layer.

The FDEL framework will provide several advantages if correctly applied. You may benefit greatly, for instance, in terms of modularity and separation of responsibility. The larger the firm is, the larger and more complex its data engineering processes are going to become. This suggests that, from an organizational perspective, it could be feasible to assign distinct teams to each FDEL layer. For example, a team may be dedicated to optimizing and securing the ingestion layer, another for ensuring the performance, scalability, and security of the storage layer, and so on. It is important to note that the FDEL is an *iterative* process where feedback and requirements from one layer may impact the design, constraints, and implementation of another layer.

Over the next four chapters, I will detail these layers, highlighting the domain-specific challenges they present in financial markets, and offering concrete examples to provide deeper insights.

# Criteria for Building the Financial Data Engineering Stack

When implementing the FDEL, it’s essential to choose the best tools and technologies to design and architect each layer, i.e., the technological stack. This is no small feat. If you want to learn about data engineering technologies and you do a quick search, you will find hundreds of different tools and frameworks. This makes it hard to know where to start since there is practically a jungle of tools to choose from. To make it more complex, these diverse tools can be used together and sometimes compete to process financial data throughout its lifecycle.

In this section, I will outline six criteria that financial institutions can employ to inform their technological decisions. These criteria serve as a fundamental and general guideline but are not exhaustive. Depending on your organization’s unique needs, you may need to identify additional criteria. Furthermore, in the following five chapters, I will discuss more granular criteria that are tailored to each layer of the FDEL.

## Criterion 1: Open Source Versus Commercial Software

A crucial and highly debated decision in financial institutions concerns the choice between proprietary commercial software and open source software. Proprietary commercial software is distributed under a purchased license that restricts user access to the source code. On the other hand, open source software is typically distributed with a license to access, use, modify, sell, and distribute the source code.

The main advantages of commercial software include the following:

Vendor accountability:   The software provider ensures frequent updates, bug fixes, security, and customer support. This is typically ensured via a *Service-Level Agreement* (SLA), which is a guarantee by the vendor to commit to a certain level of quality, availability, and performance of the offered service. Vendors might need to pay a penalty if their SLA is not met. SLAs and security are two of the most important factors behind the widespread reliance on proprietary software by the financial sector, given the risk aversion culture in financial markets that is driven by regulatory and security concerns. Vendor accountability and SLAs can help financial institutions measure and manage their operational risks, which is a regulatory requirement under frameworks such as Basel III.2

Product integrations:   The vendor guarantees seamless integration between different commercial products, which in turn can be a major cost-saving factor. Financial institutions rely heavily on trust when conducting a new activity or project. Therefore, they are more likely to adopt a new product or service that integrates with their current offerings if it is offered by a reliable software provider.

Enterprise-grade features:   The vendor offers specific features for large corporations, including scalability, security, and compliance. This is particularly relevant for financial institutions operating on a large scale, with stringent requirements of audit and monitoring.

User-friendly experience:   Commercial products are often offered with an easy-to-use interface and offer rich documentation and guides. Employees at financial institutions are often users rather than developers; therefore, a user-friendly interface is likely to be more welcomed than a complex one.

On the negative side, commercial software may come with disadvantages such as the following:

Cost:   Commercial software licenses can be very expensive and include a variable part that is hard to predict (e.g., support fees, hidden features). For large financial institutions that have critical applications, the risks can easily outweigh the costs.

Bulky products:   Many commercial software tools come in a single package that includes a large number of features. Some financial institutions (e.g., FinTech firms) may not need all of these features and end up using only a fraction of what the tool offers.

Vendor lock-in:   The more a company relies on commercial tools, the harder it is to switch to other options, including open source. Vendor lock-in gets stronger for factors such as network effect (where product value increases with its user base), and risk aversion (uncertainty from switching to another solution).

Lack of customization:   Commercial software is proprietary, meaning that financial clients may not able to adapt or modify the product to their unique needs or client expectations.

Traditionally, financial institutions have been skewed toward proprietary software because internal control rules, policies, standards, procedures, and IT audit checklists all lay out strict requirements for support agreements. The top financial services software vendors include Microsoft, FIS Global, SAP, Oracle, IBM, and NCR Corporation.

# The Oracle Database: Why Is It Widely Used by Banks?

To illustrate why financial institutions have traditionally preferred commercial software, let’s take as an example the Oracle Database. If you have ever wondered what type of database systems big banks use for their core operations, the answer is likely to include a mention of Oracle. It is perhaps the most popular enterprise-level database system among financial institutions. Interestingly, [according to the DB-Engines ranking](https://oreil.ly/P7VQJ), as of 2024, Oracle is considered the most popular database system in the world.

The Oracle Database, a commercial SQL database management system by Oracle Corporation, is predominantly used by financial institutions for online transaction processing (OLTP) purposes. It is used to store and manage core business data encompassing credit, accounts, loans, and transactions.

Over time, new database systems have emerged in the market, and some are gaining traction. However, to date, Oracle remains the gold standard for financial services.

First of all, Oracle has been in the market since 1979; therefore, it is considered a mature and reliable product. Throughout its history, Oracle has consistently [added features to its flagship products](https://oreil.ly/Mdv-a), placing the company at the forefront of database technology. By offering many features, the Oracle database could fit the many applications, requirements, and use cases that have emerged in the financial sector.

Second, the Oracle Database is flexible because it can run on Windows and various flavors of Unix. Additionally, a variety of Oracle database editions are [available](https://oreil.ly/IQvIY), ranging from large-scale editions such as the Oracle Database Enterprise Edition to single-user editions like the Oracle Database Personal Edition. Oracle Database products are available on Oracle hardware as well as being offered by several service providers on premises, on cloud, or as a hybrid cloud installation.

Third, Oracle clients can access Oracle support services through the company’s own support team or third-party consultants. This allows financial institutions to develop a feeling of trust and security as they have a reliable partner to call when needed.

In conclusion, maturity, stability, and support offer reliability against failures and risks, which is essential for critical applications such as finance. This explains the high popularity of Oracle among financial institutions and in the market in general.

The main alternative to commercial financial software is open source software. Unlike proprietary solutions, open source is typically licensed for free, and its development and maintenance is led by the public and/or by associations such as the Apache Foundation. The most popular type of open source license is the [Apache 2.0 license](https://oreil.ly/gsFzS), which allows users to obtain, modify, distribute, sublicense, and patent the software as well as use it for commercial purposes that can include proprietary software.

A large number of open source software options are available. Examples include Linux, PostgreSQL, Firefox, Kubernetes, PyTorch, Apache Spark, Apache Cassandra, Apache Airflow, and many more.

The main advantages of open source include the following:

Cost:   Open source software is often available under free licensing. Nevertheless, compared to commercial software, open source might entail indirect costs such as maintenance, upgrades, and feature development costs.

Customization:   Because the source code is available to anyone to use and modify, companies can introduce new features that accommodate their business needs.

Community:   Open source software tends to have a large community of developers who actively add new features and fix existing bugs. The main advantage of community contributions is that they aggregate the skills and knowledge of multiple people from different backgrounds and experiences. This, in turn, can guarantee that the final solution is very likely the best in the market.

Transparency:   Because the entire codebase is available to the public, open source software tends to offer more transparency into its internal workings, unlike proprietary software, which is a black box.

On the other hand, open source software could face the following drawbacks:

Support:   Users can freely report a bug or ask for a new feature in open source software, but this usually takes time as contributors tend to dedicate a variable amount of time to maintain the software. For mission-critical applications such as financial payments, this may not be acceptable.

Documentation:   Open source projects may lack up-to-date, detailed documentation and usage instructions.

Complexity:   The evolution of open source projects is characterized by frequent updates to address bugs and introduce new functionalities. Consequently, as the codebase grows with additional features, it may become increasingly complex to comprehend.

Compatibility:   A major issue with open source software is compatibility with other software applications, which can jeopardize product development and integration efforts.

Security:   With open source software, malicious actors and cybercriminals find and exploit code vulnerabilities more easily.

Confidentiality:   Open source is based on the idea of community-driven collaboration and knowledge sharing. For financial institutions, sharing their codebase might be impossible if it becomes confidential or provides a competitive advantage that the institution wants to protect.

The use of open source software in financial services has significantly increased in the last few years. According to a [report published by the Fintech Open Source Foundation (FINOS)](https://oreil.ly/Kz3sU), 2022 saw a 43% increase in the number of GitHub repositories with code contributors from the financial services industry. The report indicates that most of the contributions financial institutions make to open source projects are related to web development, cloud and containerization software, AI/ML, and continuous integration/continuous delivery (CI/CD).

Having said all of this, how would you choose between open source and proprietary software?

First, the pros and cons of open source and proprietary software can vary depending on the specific business problem and context; therefore, no single solution can fit all circumstances. In some cases, certain problems can have a well-accepted solution among market participants. For example, if your application requires high standards of security and reliable 24/7 customer support, then commercial software might be the right choice. On the other hand, if you are exploring the possibility of employing AI to build new product features, you might want to use open source libraries. Nowadays, it is common for the same financial institution to use both commercial and open source software.

### Note

Some commercial software products are based on open source frameworks. These frameworks can either be provided as managed services by vendors or form the foundation for distinct solutions. For instance, PostgreSQL, an open source database management system, serves as the basis for Amazon’s Relational Database Service (RDS) for PostgreSQL, a managed service offered by AWS. Conversely, Amazon Redshift, a proprietary data warehousing service, is built on top of PostgreSQL but is a separate product offered by AWS.

Second, consider your budget. If you are a small startup developing cutting-edge financial technology, you will likely be limited in your budget. In this case, using open source might be the best option. On the other hand, if you are a large multinational financial institution with big teams and departments, spending the money on commercial software might be more efficient as it will save the team time and effort when fixing bugs and dealing with security issues. Large corporations prefer to use commercial products as they offer a solution that standardizes internal operations across departments and teams.

Third, the level of technical expertise is a crucial factor. If you are planning on developing software that managers and accountants will use, then unless there is a big IT department, these professionals are likely to have limited expertise in software development to understand and interact with the codebase. In this case, vendor software is likely to cause fewer headaches. On the other hand, if your institution is well-equipped with software engineers who can support and help users, it would be possible to take advantage of the flexibility and developmental freedom that open source software offers.

Fourth, consider the urgency and impact on the competitive advantage of adopting a given software tool. If a financial institution feels behind compared to the market with open source adoption, then it might need to accelerate the adoption process. However, if the company is currently experimenting with open source for potential uses, then it might be possible to do it slowly.

# In-House Proprietary Financial Software

A lot of innovative financial institutions create their own in-house software, mainly in response to customer demand and changing client expectations, which can be challenging to fulfill by relying on third-party software vendors. For example, to boost the time-to-market of its new financial products, the US financial institution JPMorgan Chase developed [Kapital](https://oreil.ly/bfOBV), an advanced financial risk management and pricing software system. More recently, JPMorgan Chase leveraged the Python ecosystem to build Athena, a cross-asset platform for trading, risk management, and analytics used internally as well as by external clients. According to a [presentation given by Misha Tselman](https://oreil.ly/eLLz5), executive director at JPMorgan Chase, at PyData 2017, Athena has thousands of users, more than 1,500 Python developers contributing to it, and uses over 150,000 Python modules.

Another prominent example is [Aladdin](https://oreil.ly/S3wGr), an end-to-end portfolio and investment management platform developed by the largest asset manager in the world, BlackRock. Given its significant success and reliability, the Aladdin platform is no longer only an internal tool; rather, it is significantly influencing the way the financial sector works. Scholars use the term *platform economy* to describe such a scenario, where platforms play a major role in facilitating market activities.

If you are interested in learning more about this topic, I highly recommend the paper by Dirk A. Zetzsche, William A. Birdthistle, Douglas W. Arner, and Ross P. Buckley, [“Digital Finance Platforms: Toward a New Regulatory Paradigm”](https://oreil.ly/ZuO0F), European Banking Institute (EBI) Working Paper Series No. 58 (2020): 273.

## Criterion 2: Ease of Use Versus Performance

When choosing software or data technology, a frequent tradeoff arises between complexity and performance. Software technology can be complex if it has a steep learning curve: it may be difficult to understand or master the syntax, many elements must be managed in the code, it is demanding to set up and use, hard to debug, challenging to rerun on other machines, difficult to integrate with other software, and hard to extend with new features, deploy, or share with others. On the other hand, software is performant if it optimizes dimensions such as execution time, latency, throughput, I/O access, memory usage/footprint, carbon footprint, dependency and package management, scalability, security, or other custom metrics specific to the business operations.

The reason why there is a tradeoff between complexity and performance is that performance optimization often requires low-level interaction and configuration of the technology. Consider, for example, the difference between driving a manual versus an automatic car. To make a more concrete example, let’s think about programming languages. A programming language such as C can be considered by many as a challenging language to work with due to its strict syntax requirements, exposure to low-level details, manual garbage collection, static typing, and memory management. Once you learn how to work with languages like C, your performance advantages could be substantial.

On the other hand, programming languages such as Python are well-known for their friendly syntax, usability, automatic garbage collection, and ease of integration. However, a number of features of Python make it less performant in terms of speed than C, such as the reliance on dynamic typing and the multistep compilation process to machine code.

The same logic applies to hardware. For example, engineers can leverage different computer processors and accelerators such as Central Processing Units (CPUs), Graphical Processing Units (GPUs), and Field Programmable Gate Arrays (FPGAs) to perform various tasks.3 The CPU is the computer’s main processor, and it excels in performing a wide range of tasks. However, certain applications might require custom optimizations (e.g., high parallelism or low latency), which can be achieved through the use of specialized processors such as a GPU and FPGA. Crucially, using a GPU and FPGA is more complex and requires good knowledge of their internals, cost, and implementation principles.

### Note

When comparing hardware and software technologies, pay close attention. Not everything is as easy as it looks on the surface. For instance, it’s not unusual to come across articles that claim something like a GPU outperforms a CPU, or C# is superior to Python, and so forth. Even though they could have some truth to them, these generalizations have three problems. First, it might be challenging to compare technologies that are created according to different design principles. Second, technologies and the concepts behind their design change throughout time, and as a result, a technology that was once superior to another may not be any longer. Third, depending on the task that they are assessed against, technologies may perform differently. What I recommend in this case is to find a trusted reference from literature that you can rely on to derive a solid foundation for comparison.

Traditionally, financial market participants and researchers have thoroughly tested and benchmarked a number of technologies to certain business and technological requirements. For example, with time-critical or large-scale financial applications such as algorithmic trading, Monte Carlo simulations, asset pricing, and fraud detection, financial institutions might prefer to use performant languages such as C, C++, Rust, and Java.4 However, for less critical or small applications or situations where users are not highly skilled in software engineering internals, a more user-friendly language such as Python, R, or Julia might be a better choice.

# The Quest for Low Latency in Financial Markets

Low latency is a key differentiator when it comes to performance in financial markets. Generally speaking, the notion of latency is often used to describe the time it takes for a request to travel over a network to its destination and receive a response back from it. In many financial domains, a firm’s ability to grasp market opportunities or otherwise lose money is largely dependent on how quickly it reacts to market events. This is particularly the case in electronic trading systems, and more specifically, high-frequency and algorithmic trading.

There are several aspects to latency. First, it may concern the speed at which financial data is harvested and distributed to the many players involved in the trading system. The faster a financial institution can access market data and make trading choices, the more probable it is to capitalize on important short-term opportunities. The second aspect relates to the speed of the order execution flow. The faster an order reaches its destination, the more likely it is that the firm will make profits out of it. A millisecond difference in data access and trade processing time can equate to millions of dollars of gain or loss. For example, when executing an arbitrage strategy to profit from tiny differences in asset prices in two or more markets, the investing firm will have a tiny temporal window before the market reaches parity.

What markets consider “low” latency is not well defined but rather an evolving paradigm. Different financial market segments may operate and make improvements at different orders of time magnitude, such as the second, millisecond (thousandth of a second), microsecond (millionth of a second), and nanosecond (billionth of a second). For example, real-time payments may be considered fast at the second or millisecond level, while high-frequency traders are chasing the microsecond and nanosecond.

Numerous variables can influence latency in the financial markets. For example, a trading firm that speculates on short-term market opportunities will be impacted by the distance between its trading system and the trading venue, the distance between trading venues (in case of arbitrage), the choice of the programming language (e.g., C++ or Rust), hardware (e.g., CPU or FPGA), the efficiency of the trading program (e.g., time complexity), and cabling (e.g., copper versus fiber versus microwave).

Due to the potential for large returns, low-latency trading firms constantly invest a great deal of resources and effort to accelerate their trading systems. One approach is called *Direct Market Access* (DMA), a trading arrangement that allows traders and investors to place orders directly into the order book of an exchange, bypassing intermediaries such as brokers.

Standardized communication protocols, such as FIX, are essential for DMA, as they allow traders, brokers, and exchanges to exchange trade-related data using a unified language (we discuss FIX in Chapter 7). DMA usually involves a sophisticated and costly technology setup. Consequently, it is commonly offered as a service by sell-side firms and specialized technology providers.

In addition, to provide markets with the opportunity to gain a speed advantage, stock exchanges started providing trading firms with the option to position their trading servers in close proximity to, or even within the same data center as, the exchange servers.

This strategy, called *colocation*, allows trading firms to access financial data through data feeds that stream data right from the source as soon as it appears in the exchange server. Colocation has [raised some issues of fairness in financial markets](https://oreil.ly/OpInR), as the average investor or market maker will get the information at a later date, when they will have less advantage to react.

Another direction toward low latency in financial markets relies on the use of specialized hardware such as a field-programmable gate array (FPGA). An FPGA is a configurable type of integrated circuit that can be programmed after manufacturing to suit whatever purpose and needs you want. As such, FPGAs have been widely adopted by financial markets to build systems that react to market events and process orders in nanoseconds, as well as to perform complex/parallel computations efficiently.

## Criterion 3: Cloud Versus On Premises

In today’s technological landscape, a major and critical technological choice often emerges between cloud-based and on-premises infrastructures. In an on-premises server infrastructure, the firm owns, controls, and maintains a group of servers (often called commodity servers) for its storage and computing purposes. Alternatively, a firm can use the cloud to host or lease servers at a third-party cloud provider or use the vendor’s managed servers and services directly.

There are pros and cons to using either on premises or the cloud, and making the right decision may be quite challenging. Generally speaking, on premises is viewed by many as the traditional (or legacy) way of managing server infrastructure, while the cloud represents the modern and user-friendly approach. This, however, doesn’t mean that on premises is bad and the cloud is good. Let’s explore in more detail the main differences and features of both solutions.

### On premises

In an on-premises setting, the financial institution is fully responsible for its servers and data infrastructure. This means that the institution owns, configures, and manages its servers, computing environments, networking, security, scalability policies, logs, and user access.

As you might have guessed, the main advantage of this infrastructure choice is that you have full control of your digital assets. If managed properly, an on-premises infrastructure can guarantee maximum security. Having all your data and software reside within your organization’s premises provides a feeling of safety and peace. Security is a major concern for highly regulated businesses like finance; hence, on premises is a very typical choice.

Nevertheless, the on-premises approach has a number of potential downsides. Cost is perhaps the main issue. To maintain an on-premises infrastructure, institutions need to have a dedicated IT department responsible for software and hardware maintenance, availability, updates, security, license purchases, and user support. Such costs might rise exponentially, especially in large institutions or in the presence of poor management and usage practices.