# Cost Monitoring

Cost monitoring is the process of keeping an eye on a financial data infrastructure’s expenditures to ensure that they are within acceptable bounds and to spot patterns of excessive usage. The significance of cost monitoring has grown alongside the widespread adoption and migration to cloud services. While the cloud provides a plethora of accessible services with flexible on-demand pricing, managed scalability, and simplified configuration, there exists a potential risk of unforeseen, excessive, or misinterpreted cost structures.

To illustrate the issue, let’s consider one of the most attractive cloud computing strategies: *serverless computing*. This term refers to a cloud-based application development model where the cloud provider takes full care of infrastructure configuration and management. This includes all features such as load balancing, auto-scaling, availability, security, operating system management, logging, monitoring, and storage management. Services such as AWS Lambda and Google BigQuery are among the most popular services that people often associate with serverless computing.

Crucially, the economics of serverless computing can be misunderstood, potentially resulting in unforeseen expenses. This is due to the variability in cost-effectiveness of the serverless model, which is dependent on factors like execution patterns and workload volume. Pennies can add up to thousands of dollars when running a massive number of jobs.

Furthermore, in services like AWS Lambda, pricing isn’t solely determined by the frequency and duration of function invocations, as many might assume with *pay-as-you-go* models. You also indirectly pay based on the memory allocated to your function, which directly influences the cost of your function executions. Moreover, additional charges may be added if AWS Lambda reads data from AWS storage or transfers data between regions.

As of the time of writing this book, invoking an [on-demand AWS Lambda function](https://oreil.ly/znW-C) costs $0.0000000021 per millisecond for 128 MB of RAM and $0.0000000167 per millisecond for 1,024 MB of RAM. This looks relatively cheap. However, costs can escalate significantly based on the nature of your workload. When assessing application scalability, a commonly used metric is transactions per second (TPS), also referred to as hits per second (HPS) or requests per second (RPS). Suppose our application processes a specific number of RPS over a total of 100,000 seconds in a month. Using this information, let’s explore a few scenarios:

Scenario 1: 100 RPS with a duration of 10 seconds each:   * *Cost per invocation*: $0.0000000021 × 10,000 milliseconds (10 seconds) = $0.000021
    * *Monthly cost*: $0.000021 × 100 RPS × 100,000 seconds = $210

Scenario 2: Increasing execution time to 1 minute (60 seconds):   * *Cost per invocation*: $0.0000000021 × 60,000 milliseconds (60 seconds) = $0.000126
    * *Monthly cost*: $0.000126 × 100 RPS × 100,000 seconds = $1,260

Scenario 3: Increasing allocated memory to 1,024 MB (1 GB):   * *Cost per invocation*: $0.0000000167 × 60,000 = $0.001002
    * *Monthly cost*: $0.001002 × 100 RPS × 100,000 seconds = $10,020

These calculations show how increasing execution time and memory allocation can significantly impact the monthly cost of running AWS Lambda functions. Adjustments in these parameters should be carefully considered based on performance requirements and budget constraints. Additionally, when assessing solutions like Lambda and other alternatives, it is important to consider your future scaling needs rather than just your current usage.1

Various practices and tools are available to manage cloud costs. For instance, cloud providers offer [budgeting options](https://oreil.ly/mkoVK) that let users set target budgets and receive notifications if costs exceed predefined thresholds. Another promising approach is FinOps, a recent trend in cloud cost monitoring and management, which has been defined by the [FinOps Foundation](https://oreil.ly/gJSWy) as:

> An operational framework and cultural practice which maximizes the business value of cloud, enables timely data-driven decision making, and creates financial accountability through collaboration between engineering, finance, and business teams.

A FinOps framework requires five pillars:

* Cross-functional collaboration among engineering, finance, and business teams to enable fast product delivery while ensuring financial and cost control.
* Each team takes ownership of its cloud usage and costs.
* A central team establishes and promotes FinOps best practices.
* Teams take advantage of the cloud’s on-demand and variable cost model while optimizing the tradeoffs among speed, quality, and cost in their cloud-based applications.
* Decisions are driven by the cloud’s business value, such as increased revenue, innovative product development, reduced fixed costs, and faster feature releases.

FinOps is an iterative and learning-driven process. Within organizations, the maturity of FinOps is commonly assessed using the [FinOps Maturity Model (FMM)](https://oreil.ly/E3VgV), which consists of three stages: Crawl, Walk, and Run. As an organization progresses from Crawl to Run level, it moves from being reactive, where issues are fixed as they occur, to being proactive, where teams are able to anticipate cloud usage patterns and expenses and incorporate such information into their cloud architecture design decisions.

# Case Study: Financial Transaction Cost Monitoring with Abel Noser

Transaction cost monitoring and analysis is a common practice in financial markets. It entails monitoring and analyzing the expenses related to executing financial transactions, such as trades and investments. This process is vital for investment firms, asset managers, brokers, and other financial institutions to ensure that they are achieving optimal execution while minimizing costs.

Several companies specialize in transaction monitoring services for the financial sector. An industry leader in this market is [Abel Noser](https://oreil.ly/HAJej), now part of Trading Technologies. Financial institutions submit their transaction data to Abel Noser, which conducts comprehensive cost analysis and returns insights to the clients. Over 350 global clients from the US, as well as other parts of the world, report their data to Abel Noser.

Abel Noser is also a data vendor, providing institutional investor datasets that contain transaction-related information such as the instrument traded, price, quantity, date, trade direction (buy or sell), commissions paid, and other market fields. Abel Noser’s data is an essential source for scientific research on institutional trading.

# Business and Analytical Monitoring

A more advanced form of data monitoring involves observing statistical, analytical, and business-related dimensions. This monitoring approach ensures that not only is the raw data monitored, but also the contextual and analytical insights that drive strategic decision-making.

For example, commercial banks must diligently and continuously monitor the status of their lending activities to ensure clients make timely payments and detect/predict defaulting clients. Moreover, to ensure resiliency and regulatory compliance, banks need to monitor their financial, credit, and operational risks as well as their exposures, risk concentration, capital adequacy, and leverage situation. Similarly, institutions such as investment firms need to continuously monitor their portfolio performance, asset allocation, diversification, and investment strategies.

# Risk Monitoring in Financial Institutions: Data Engineering Challenges

Risk is an inherent aspect of financial institution operations, particularly in the banking sector. Consequently, most banking regulations emphasize principles and frameworks to ensure banks’ resilience against the classes of risks they are exposed to.

The primary [framework for international banking regulation](https://oreil.ly/7XqUv) consists of the three Basel Accords—Basel I, Basel II, and the more recent Basel III. The Basel framework groups bank risks into three broad categories:

Market risk:   The risk of financial loss deriving from movements in market prices.

Credit risk:   The risk of financial loss deriving from a borrower or counterparty not being able to meet the agreed-upon obligations.

Operational risk:   The risk of financial loss resulting from poorly designed or failed internal processes, people, and systems or from external events.

To be managed, these risks must be quantitatively measured. To do this, risk data is needed. Each risk category requires different sets of data fields. Market risk measurement requires data such as portfolio composition, historical prices, volatility, interest rates, and correlations. Credit risk measurement requires data such as credit ratings, credit scores, exposure data, collateral data, default data, probability of default data (likelihood of creditors defaulting on their obligations), and loss given default data (losses incurred in case of a default event). Finally, operational risk measurement requires detailed operational loss and risk event data as well as internal control data.

Importantly, effectively managing the diverse types of risk data poses significant data engineering challenges related to data collection, aggregation, integration, normalization, quality assurance, and timely delivery. In Chapter 5, we discussed the problem of data aggregation in financial institutions and illustrated how it mainly applies to risk data. As a reminder, Basel III introduced the [*Principles for Effective Risk Data Aggregation and Risk Reporting*](https://oreil.ly/dSCF7) to ensure the adequacy of financial institutions’ data infrastructure for managing and aggregating risk data efficiently.

To address operational risk, a common strategy involves establishing and maintaining an *operational event risk* *database*, which stores historical records stemming from operational incidents. This database may contain elements such as the event date, description (e.g., what happened), primary causes (e.g., human error), business line (e.g., risk management), and control point (e.g., trading desk). To learn more about this, consult the paper by Niclas Hageback, [“The Operational Risk Framework Under a Retail Perspective”](https://oreil.ly/mYnHH).

Financial institutions relying on data analytics and machine learning must actively monitor the statistical, quality, and performance aspects of both their data and models. Within the machine learning community, concepts such as *concept drift* and *data drift* are frequently used in the monitoring and detection of changes in the underlying data distribution or model relationships.

Concept drift occurs when a machine learning model no longer accurately reflects the original problem it was trained to solve. For example, a well-performing fraud detection model trained on a specific financial dataset may become less effective over time if fraudsters adapt and modify their fraudulent tactics. As a result, the model’s predictions may become less accurate because the underlying problem it was designed to address has evolved.

Data drift happens when the input data distribution to a machine learning model changes over time. Consider an ML model trained to forecast a company’s stock price based on a given data sample. Suppose that throughout this sample, the stock price was relatively stable (low volatility). If the market becomes more volatile over time, the model might struggle to predict accurately because the statistical characteristics of the data have changed.

Interestingly, the ideas of concept and data drift are relatively familiar to finance. In financial markets, particularly among risk managers, the term *model risk* is used to describe the risk that financial models used in asset pricing, trading, forecasting, and hedging will generate inconsistent or misleading results.2

One prevalent area of business monitoring among financial institutions involves the monitoring of various fraudulent and illegal activities when conducting transactions. Examples include the following:

Money laundering:   The process of concealing the origins of illegally obtained money, typically by means of transfers involving foreign banks or offshore companies.

Terrorism financing:   Providing financial support to terrorist organizations or individuals to facilitate acts of terrorism.

Fraud:   Deceptive practices intended to secure unfair or unlawful financial gain, often involving misrepresentation or omission of information.

Corruption:   Dishonest or fraudulent conduct by those in power, typically involving bribery, embezzlement, or abuse of authority for personal gain.

Another good example is market manipulation and securities fraud practices, which involve illegally influencing the supply or demand of financial instruments to gain advantage from market reactions. Examples include the following:

Pump and dump:   This involves artificially inflating the price of a stock or other asset through false or misleading statements (pump). Once the price is high enough, the manipulator sells their holdings at a profit (dump), causing the price to collapse, and leaving other investors with losses.

Spoofing:   This involves placing orders without the intention of executing them in order to create a false impression of demand or supply in the market. Once other traders react to these orders, the spoofer cancels or modifies their original orders.

Insider trading:   Trading securities based on material nonpublic information, which can generate unfair advantages and distortions in market prices.

Front running:   When a broker or trader executes orders on a security for their own account while taking advantage of inside knowledge of a future transaction that is expected to impact the security’s price substantially.

Churning:   Excessive trading of a client’s brokerage account by a broker to generate commissions without regard for the client’s investment goals.

Wash trading:   Simultaneously buying and selling the same financial instruments to create artificial trading volume or a false impression of market activity without having exposure to market risk.

Lastly, an integral aspect of financial institution monitoring revolves around evaluating investment portfolio performance. This entails selecting, calculating, and monitoring key performance indicators like the Sharpe ratio, Sortino ratio, Treynor ratio, and information ratio. To illustrate one example, the Sharpe ratio is a measure of risk-adjusted return, indicating how well an investment performs relative to its risk level. These metrics allow institutions to assess the effectiveness of their investment strategies, enabling informed and timely decisions for optimizing portfolio composition and performance.

# Data Observability

As the technological stacks supporting data infrastructures have grown in complexity and scale, the requirements for monitoring have evolved accordingly. This has led to the emergence of a more advanced and comprehensive monitoring approach known as *observability*.

Observability elevates monitoring to a new level, allowing software and data engineering teams to handle issues proactively and gain deep insights into the internal state and behavior of a given software application or infrastructure. Authors Charity Majors, Liz Fong-Jones, and George Miranda ([*Observability Engineering*](https://oreil.ly/oBMut), O’Reilly, 2022) describe a software system as observable if you can do the following (the following list is a direct quote):

* Understand the inner workings of your application
* Understand any system state your application may have gotten itself into, even new ones you have never seen before and couldn’t have predicted
* Understand the inner workings and system state solely by observing and interrogating with external tools
* Understand the internal state without shipping any new custom code to handle it (because that implies you needed prior knowledge to explain it)

Observability can be applied across various dimensions of IT systems, encompassing data, applications, infrastructure, networks, security, and business. *Data observability* is a vital area in this regard. Author Andy Petrella of [*Fundamentals of Data Observability*](https://oreil.ly/bmJ0X) (O’Reilly, 2023) defines data observability as:

> The capability of a system to generate information on how the data influences its behavior and, conversely, how the system affects the data.

With data observability, financial data engineers and other team members should easily be able to ask and answer questions such as: “Why is workflow A running slowly?”, “Why is data not available yet for client X?”, “What caused the data quality issue in dataset Y?”, “Why is the data pipeline for report Z delayed?”, or “Where is the bottleneck in a transformation or ingestion process?”

The main building blocks of data observability are metrics, events, logs, and traces.

In addition, data observability systems leverage concepts such as automated monitoring and logging, root cause analysis, data lineage, contextual observability, Service-Level Agreements (SLAs), telemetry/OpenTelemetry, instrumentation, tracking, tracing, and alert analysis and triaging.

# OpenTelemetry: The Open Source Standard for Observability

[OpenTelemetry](https://oreil.ly/STFq-) is an open source, vendor-neutral framework comprising a set of APIs, SDKs, libraries, agents, and tools to enable observability in software applications. It allows engineers to collect telemetry data, such as traces, metrics, and logs, from their applications and services to gain insights into their behavior, performance, and reliability. OpenTelemetry provides standardized instrumentation and integration capabilities for various programming languages, frameworks, and platforms, making it easier to instrument applications consistently across different environments. It allows exporter applications to send telemetry data to various backends and observability platforms for storage, analysis, visualization, and alerting.

A properly implemented data observability system can bring a lot of benefits for financial institutions, such as the following:

* Higher data quality (e.g., by observing data quality metrics)
* Operational efficiency (e.g., reduced TTD and TTR)
* Facilitated communication and trust between different team members (e.g., risk management and trading desk)
* Gains in client trust by being able to detect and understand the issues they might face
* Enabling complex data ingestion and transformation while maintaining reliability and visibility into the system
* Regulatory compliance (e.g., by keeping data privacy and security under control)

Financial data engineers play a vital role in embedding data observability capabilities within the financial data infrastructure. Observability is fundamentally a data engineering challenge. It entails instrumenting systems to generate vast amounts of heterogeneous data points, which must be efficiently indexed, stored, and queried in near-real time. This ensures comprehensive visibility into the behavior of various components of the financial data infrastructure, including data ingestion, storage, processing systems, workflows, quality, compliance, and governance.3

It’s important to remember that implementing a data observability system requires a significant investment in both technology and people. For this reason, I highly recommend you evaluate your business needs, technical constraints, and growth perspectives before investing in a large-scale data observability system. In many cases, a simple monitoring strategy is all you need. As your organization grows and its technological stack becomes more complex, investing in data observability becomes increasingly beneficial and, eventually, essential.

# Summary

This chapter discussed the final layer in the financial data engineering lifecycle: monitoring. Monitoring is critical for guaranteeing the reliability, performance, security, and compliance of financial data infrastructures.

This chapter explained and illustrated the significance of metric, event, log, and trace monitoring in tracking application activities and diagnosing and solving potential issues. Furthermore, it explored the key components of data quality, performance, and cost monitoring, outlining their techniques and giving practical advice and financial use cases.

In addition, it emphasized the importance of business and analytical monitoring in providing actionable insights and supporting informed decision-making within financial institutions. Finally, the chapter included a brief review of data observability, an emerging topic, highlighting its crucial role in providing deep insights into the internals and behavior of various data infrastructure components.

By this point of the book, you should have a solid grasp of the various layers comprising the financial data engineering lifecycle. To further simplify and enhance the modularity of financial data infrastructures, smaller data processing components, known as data workflows, are commonly developed. The next chapter will cover these data workflows in detail.

1 To learn more about the economics of serverless computing, I highly recommend Adam Eivy and Joe Weinman’s [“Be Wary of the Economics of ‘Serverless’ Cloud Computing”](https://oreil.ly/ASKET), *IEEE Cloud Computing* 4, no. 2 (March–April 2017): 6–12.

2 For more on model risk, see Jon Danielsson, Kevin R. James, Marcela Valenzuela, and Ilknur Zer’s [“Model Risk of Risk Models”](https://oreil.ly/UfmCx), *Journal of Financial Stability* 23 (April 2016): 79–91.

3 For a comprehensive discussion of observability data management systems, I highly recommend Suman Karumuri, Franco Solleza, Stan Zdonik, and Nesime Tatbul’s [“Towards Observability Data Management at Scale”](https://oreil.ly/N9OXj), *ACM Sigmod Record* 49, no. 4 (March 2021): 18–23.

# Chapter 11. Financial Data Workflows

Throughout this part of the book, you have explored the fundamental layers of the financial data engineering lifecycle: ingestion, storage, transformation and delivery, and monitoring. Adhering to this structured framework is crucial for building and maintaining efficient financial data infrastructures.

Importantly, as your company expands, the financial data infrastructure will become larger and more complex, generating many inter dependencies and links between the different layers. To address this challenge, further refinement is required to build multiple independent and specialized data processing components. Data engineers call these components data pipelines or workflows.

This chapter will explore the foundational concepts of data workflows, introducing the ideas of workflow-oriented software architectures and workflow management systems. Then, it will cover the main types and characteristics of financial data workflows that can be implemented to handle financial data processing tasks.

# Workflow-Oriented Software Architectures

Before explaining workflows, it’s important to understand the business rationale behind their practicality. First, as a natural part of the growth journey of any digital company, the technological stack tends to increase in size and complexity, creating numerous inter dependencies, logical flows, and interactions among various system components. For this reason, the software development community has identified the need for architectural designs and tools that organize software transactions into structured workflows that can be defined, coordinated, managed, monitored, and scaled following a specific business logic. In this book, I will use the term *workflow-oriented software architecture* (WOSA) to describe this design pattern.

The concept of WOSA is highly applicable to financial markets, where many financial operations are organized as a series of actions carried out in a specific sequence. A notable example is financial transactions, which generally follow a defined workflow consisting of multiple steps. Examples follow:

* The lifecycle of financial trades involves several steps such as trade initiation, order placement, trade execution, trade capture, enrichment, validation, verification, confirmation, clearing, and settlement.
* The lifecycle of credit card payments involves a chain of steps that may involve the customer, merchant, payment gateway, payment processor, acquiring bank, issuing bank, and card network. Along the way, the same payment goes through several steps that start with submission, authorization, balance and fraud checks, confirmation or rejection, clearing, and settlement.

In essence, WOSAs focus on organizing and executing complex processes through structured workflows, enhancing modularity, efficiency, and manageability in software systems. An important category within workflows is the data workflow, designed specifically for the processing and management of data. Let’s examine some of its technical aspects and concepts in the following section.

# What Is a Data Workflow?

A data workflow is a repeatable process that involves applying a structured sequence of data processing steps to an initial dataset, producing a desired output dataset.

Data workflows are fundamental to data engineering. As a financial data engineer, you will frequently build financial data workflows. To excel at this task, an important skill to learn is workflow abstraction. This involves defining a conceptual framework for your workflow that disregards technological implementation details to guarantee generalization. It is similar to how concepts of data storage models and data storage systems were used in Chapter 8 to abstract the specifics of storage technologies.

One of the most widely adopted data workflow abstractions is the [*dataflow paradigm*](https://oreil.ly/lyCsV). Its core principle involves organizing an application into a directed computational graph. In this graph, nodes represent individual computation steps, while links express data dependencies or the flow of data between these computations. Typically, the computational graph underlying a workflow is designed without cycles. When structured in this manner, the graph is referred to as a Directed Acyclic Graph (DAG).

The most basic type of computational DAG is the linear DAG. It organizes tasks in a sequential order where each task N can have at most one preceding task (N–1) and one subsequent task (N+1). [Figure 11-1](#ch11_figure_1_1724776836317836) illustrates a three-task linear computational DAG.

### Figure 11-1. Linear DAG

Frequently, computational DAGs are more complex than the linear case. For example, a specific computing task may depend on multiple preceding tasks. [Figure 11-2](#ch11_figure_2_1724776836317865) illustrates such a scenario, where computation task 6 relies on tasks 3, 4, and 5.

### Figure 11-2. Complex DAG

![Figure 11-2. Complex DAG](images/fden_1102.png)

When defining a computational DAG, a fundamental question arises: “What constitutes a task?” While there isn’t a universal answer to this question, several best practices have been suggested. For example, a task needs to be an atomic unit of execution, meaning that it either succeeds or fails as a whole. Furthermore, it is considered a best practice to ensure that tasks are idempotent, meaning that running the same task multiple times will yield the same result as running it once, without causing any unexpected or undesirable side effects. This can be useful since it can allow you to add task checkpoint features to your DAG, allowing you to resume DAG execution from the failed step rather than execute it all over again.

Another consideration is the size of tasks within a computational DAG. They should strike a balance: they need to be small enough to facilitate debugging and traceability, but not so small that they introduce unnecessary overhead and degrade DAG performance. Conversely, overly large tasks simplify the DAG structure but can constrain debuggability and lead to costly retry operations.

Moreover, a good practice is to associate tasks with business logic. This can involve basic tasks such as data quality checks or more complex computations like modeling and analytics.

# Workflow Management Systems

Once a workflow abstraction has been defined, the next step is to design a system that provides the infrastructure and tools necessary for building, orchestrating, and monitoring a WOSA. In this context, I’ll use the term *workflow management system* (WMS) to refer to such systems. When developing a WMS, various properties must be considered. In the following subsections, I will briefly discuss the most common ones.

## Flexibility

A flexible WMS is capable of managing a diverse range of tasks and workflows. For instance, it should support the creation of simple linear workflows as well as more complex ones. Additionally, it should offer flexibility in how workflows are initiated, allowing for scheduled executions as well as triggering based on specific events, such as the arrival of files or data in designated storage locations.

## Configurability

A configurable WMS enables users to define workflow specifications according to their needs. For instance, many WMSs allow users to define workflows and tasks using infrastructure-as-code (IaC) methodologies. This can be achieved through programming languages like Python or Domain-Specific Languages (DSLs) such as JSON.

With IaC, users can programmatically define workflow and task specifications such as dependency structure, input/output parameters, error handling, timeout policy, retry logic, status update, workflow triggers, concurrent execution limit, logging, and many more. [Figure 11-3](#ch11_figure_3_1724776836317885) illustrates a typical approach to workflow and task definition, which contains all the information necessary to define the behavior of a workflow.

### Figure 11-3. A workflow and task definition template

![Figure 11-3. A workflow and task definition template](images/fden_1103.png)

## Dependency Management

WMSs vary in how they manage and configure dependencies between tasks and workflows. In simple WMSs, users are only able to define static and linear workflows. However, more advanced WMSs may allow for parallel workflow/task execution, dynamic and conditional task creation, and information passing between tasks. To illustrate, (a) in [Figure 11-4](#ch11_figure_4_1724776836317905) displays a workflow where tasks 3 and 4 are conditionally executed after task 2, depending on whether a specific condition is satisfied; if not, task 5 follows task 2. In contrast, (b) in [Figure 11-4](#ch11_figure_4_1724776836317905) illustrates a workflow that dynamically generates a variable number of tasks (N) at runtime, based on the input received from task 1.

### Figure 11-4. Workflow with conditional tasks, and workflow with dynamic tasks

![Figure 11-4. Workflow with conditional tasks, and workflow with dynamic tasks](images/fden_1104.png)

## Coordination Patterns

In every WMS, components like workflows and tasks are designed to interact with each other. Various communication patterns have been developed to describe how these interactions occur. Two notable patterns are the *Synchronous Blocking Pattern* (SBP) and the *Asynchronous Non-Blocking Pattern* (ANBP).

The SBP involves one component calling another and waiting for a response, which is typical in systems using HTTP and RESTful APIs. In a WOSA relying on an SBP, each task within a workflow is executed sequentially within the same process, with each task waiting for the previous one to complete before proceeding.

Conversely, the Asynchronous Non-Blocking Pattern operates in a fire-and-forget mode, where a component sends a request or message to another component without waiting for a response or confirming its processing. In a WMS, this pattern can be implemented by running each workflow task independently on separate processes or machines and having a dedicated task queue that gathers incoming messages for execution. [Figure 11-5](#ch11_figure_5_1724776836317924) provides a visual representation of this concept.

### Figure 11-5. Synchronous Blocking Pattern versus Asynchronous Non-Blocking Pattern

![Figure 11-5. Synchronous Blocking Pattern versus Asynchronous Non-Blocking Pattern](images/fden_1105.png)

## Scalability

WMS scalability is typically assessed based on its capacity to handle concurrent executions of workflows and tasks. The scalability requirements vary depending on the nature of the WMS. Event-driven and high-volume WMSs, for instance, demand robust scalability capabilities to manage large volumes of tasks triggered by real-time events or continuous streams of data. In contrast, scheduled batch-oriented WMSs may have less stringent scalability needs as they operate on predefined schedules and process tasks in batches.

## Integration

A highly desired feature of WMSs is their capability to seamlessly integrate with other tools and technologies, especially those that the WMS is designed to manage or coordinate. For example, when orchestrating applications in the cloud, it might be more convenient to rely on a cloud-based WMS as it will easily integrate with the cloud services running the applications.

Many WMSs incorporate operators, which are predefined tasks enabling seamless integration with a variety of technologies. These operators facilitate common and essential operations within workflows. For instance, a database operator allows users to establish connections and interact with specific types of databases like Postgres, Redshift, Snowflake, and BigQuery. This capability streamlines workflow execution by providing ready-made functionalities for interacting with diverse technological environments.

Now that you have established a foundational understanding of workflows, let’s explore some of the most common types of data workflows, outlining their key characteristics, the technologies they employ, and their applications in the financial domain.