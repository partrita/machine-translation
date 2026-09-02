# Summary

This chapter discussed the third layer in the financial data engineering lifecycle: the transformation and delivery layer. Key topics covered include data querying patterns, query optimization, transformation operations and patterns, data consumers, and delivery mechanisms. Throughout the chapter, these concepts are applied within the context of financial markets, providing practical examples and case studies for better insights.

One thing to keep in mind is that financial data transformations, along with their associated patterns and optimizations, are fundamentally driven by business requirements. Custom transformations may need to be developed to specifically address unique business needs and challenges. This adaptive approach ensures that the financial data engineering lifecycle effectively supports and aligns with business objectives in the dynamic financial landscape.

As you learned toward the end of this chapter, once data has been transformed and prepared for its intended purposes, it is delivered to its final consumers, seemingly marking the end of its lifecycle. At this point, you might wonder if additional steps are still required. Crucially, ensuring optimal and flawless functioning across the ingestion, storage, transformation, and delivery layers is never completely assured. This underscores the critical importance of the final layer—monitoring—which will be the focus of the next chapter.

1 A simple moving average is the average of the previous K data points. For example, take the vector [1,2,3,4,5]. The moving average over two data points becomes [1, 1.5, 3, 4.5, 6].

2 Try it yourself on [CoderPad](https://oreil.ly/ZxWWV).

3 Logarithmic speed, denoted as O(ln(n)), is widely regarded as efficient in terms of performance. To illustrate this concept in simple terms, imagine you have a very large table and you’re searching for a specific row. Now suppose that you perform your search in multiple iterations, and at each iteration, you divide the table in half and only search one half. This approach dramatically reduces the search space with each iteration. Any algorithm that operates in this manner achieves logarithmic complexity. While structures like B-trees are more complex, they share the same underlying strategy of efficiently narrowing down search areas to quickly find desired data.

4 For a good reference on database internals, I highly recommend Alex Petrov’s [*Database Internals: A Deep-Dive into How Distributed Data Systems Work*](https://oreil.ly/UjmhQ) (O’Reilly, 2019).

5 Some authors suggested adopting a data consumer-centric approach to data quality definition and management. To learn more about this topic, I highly recommend Richard Y. Wang and Diane M. Strong’s [“Beyond Accuracy: What Data Quality Means to Data Consumers”](https://oreil.ly/iYXyQ), *Journal of Management Information Systems* 12, no. 4 (1996): 5–33.

6 For more on this topic, check the excellent article by Lou Lindley, [“Working with High-Frequency Market Data: Data Integrity and Cleaning (Part 1)”](https://oreil.ly/lcNBQ).

7 For a practical guide to this topic, I recommend reading Jason Brownlee’s articles on the [de-trending](https://oreil.ly/lukxN) and [de-seasonalization](https://oreil.ly/wRdcv) of time series.

8 In financial data, several seasonal behaviors have been observed. For example, the [January Effect](https://oreil.ly/q7YdE) refers to a seasonal pattern where prices of stocks tend to increase during the month of January of each year.

9 To read more about this topic, I recommend John Y. Campbell, Andrew W. Lo, and A. Craig MacKinlay’s *The Econometrics of Financial Markets*, vol. 2. (Princeton University Press, 1997).

10 For more on this topic, see William M. Cready and Ramachandran Ramanan’s [“The Power of Tests Employing Log-Transformed Volume in Detecting Abnormal Trading”](https://oreil.ly/vMZpt), *Journal of Accounting and Economics* 14, no. 2 (June 1991): 203–214.

11 Factors are often employed in an investment strategy called factor investing. To learn more about this, I recommend David Blitz and Milan Vidojevic’s [“The Characteristics of Factor Investing”](https://oreil.ly/ajjX-), *Journal of Portfolio Management* 45, no. 3 (2019): 69–86.

12 For an insightful overview of financial markets, I recommend reading Nikita Ivanov, [“In-Memory Computing Can Digitally Transform Financial Services and FinTech Applications for Capital Markets”](https://oreil.ly/fyFqV), *Forbes*, January 5, 2021.

13 For more on this topic, I recommend reading A. Madhavi and T. Sivaramireddy’s [“Real-Time Credit Card Fraud Detection Using Spark Framework”](https://oreil.ly/p6kJ7), in *Machine Learning Technologies and Applications: Proceedings of ICACECS 2020* (Springer, 2021): 287–298.

14 For more context regarding this issue, I recommend the paper by John W. Lockwood, Adwait Gupte, Nishit Mehta, Michaela Blott, Tom English, and Kees Vissers, [“A Low-Latency Library in FPGA Hardware for High-Frequency Trading (HFT)”](https://oreil.ly/2UEtd), in the *2012 IEEE 20th Annual Symposium on High-Performance Interconnects* (IEEE, 2012): 9–16.

15 For more on database throughput, see Felipe Cardeneti Mendes, Piotr Sarna, Pavel Emelyanov, and Cynthia Dunlop’s *Database Performance at Scale: A Practical Guide* (Apress, 2023): 254.

# Chapter 10. The Monitoring Layer

After designing and implementing the ingestion, storage, transformation, and delivery layers, the final layer to build is the *monitoring layer*. This layer is crucial for tracking and reporting on the financial data infrastructure’s performance, reliability, and quality.

Data monitoring is a continuous task requiring close collaboration between financial data engineers and business teams. It enables financial institutions to operate securely, compliantly, and efficiently in a rapidly changing environment. More specifically, monitoring is needed for the following functions:

Operational continuity and efficiency:   As financial data infrastructures grow in complexity, monitoring becomes vital to ensure operational continuity, system availability, efficiency, cost optimization, and optimal performance.

Compliance:   Effective monitoring is crucial for financial institutions to meet regulatory requirements. It enables the detection and prevention of fraud and other suspicious activities, while also facilitating accurate and timely regulatory reporting.

Risk management:   Financial institutions face a range of risks, including financial, credit, fraud, and operational risks, each with potentially significant costs. Monitoring plays a critical role in promptly and effectively detecting and mitigating these risks.

When designing this layer, the first question you should ask yourself is what components of your financial data infrastructure you need to monitor. This question is critical since monitoring can be a resource-intensive and costly commitment, so you must be clear on your monitoring plan from the start.

### Note

Monitoring every possible issue may not be feasible, which is an important consideration when designing the monitoring layer. There is always the potential for unexpected and unforeseen problems to arise.

There is no one-size-fits-all approach to monitoring, as financial data infrastructures may differ in terms of design patterns, data management maturity, software components, level of automation, and data governance policies. However, the following five categories are applicable to (almost) all monitoring approaches: (1) metrics, events, logs, and traces, (2) data quality monitoring, (3) performance monitoring, (4) cost monitoring, and (5) business and analytical monitoring. The following sections will examine each of these in more depth.

# Metrics, Events, Logs, and Traces

The main building blocks of monitoring revolve around the generation and utilization of four fundamental types of data: metrics, events, logs, and traces. These elements provide essential inputs for financial data engineers to diagnose, understand, and resolve technical and nontechnical issues within the financial data infrastructure.

## Metrics

Metrics are quantitative measurements that provide information about a particular aspect of a system, process, variable, or activity. Metric values are typically observed over a specific time interval or frequency, such as daily, hourly, or in real time. In addition, metric observations are often enriched with metadata represented as a set of key-value pairs, called tags. Tags are used to identify a given instance of a metric. A unique combination of a metric and its associated tags is called a *time series.* [Table 10-1](#ch10_table_1_1724776835701165) illustrates this concept by displaying a time series view of the 30-day volatility metric across three distinct stocks traded on NASDAQ. Specifically, the table contains three separate time series: the initial two rows for AAPL-NASDAQ, the subsequent two rows for GOOGL-NASDAQ, and the final row for MSFT-NASDAQ.

Table 10-1. Metrics

| Timestamp           | Metric              | Value | Tags                            |
| ------------------- | ------------------- | ----- | ------------------------------- |
| 2023-07-09 09:00:00 | Volatility (30-day) | 0.025 | Ticker: AAPL, Exchange: NASDAQ  |
| 2023-07-10 09:00:00 | Volatility (30-day) | 0.027 | Ticker: AAPL, Exchange: NASDAQ  |
| 2023-08-11 09:00:00 | Volatility (30-day) | 0.020 | Ticker: GOOGL, Exchange: NASDAQ |
| 2023-08-12 09:00:00 | Volatility (30-day) | 0.022 | Ticker: GOOGL, Exchange: NASDAQ |
| 2023-03-11 09:00:00 | Volatility (30-day) | 0.014 | Ticker: MSFT, Exchange: NASDAQ  |

Interestingly, this way of organizing metrics as time series is a key reason why many engineers prefer using time series databases for tracking and managing metrics. Common examples include Prometheus, Graphite, and InfluxDB. Advanced visualization tools like Grafana can be configured to retrieve data from the metric time series database, allowing users to explore and visualize metrics.

# Data Monitoring with InfluxDB: Case Studies from Financial Markets

Financial institutions worldwide employ and continually invest in data monitoring technologies. One common choice involves using time series databases such as InfluxDB.

A good example is PayPal, a global leader in the international online payments sector, serving hundreds of millions of customers in over 200 markets around the world. When PayPal decided to become container-based to modernize its infrastructure, the IT team sought a scalable monitoring solution that could unify metric collection, storage, visualization, and smart alerting within the same platform. The final [solution](https://oreil.ly/ZVIvR) involved using InfluxDB Enterprise (the enterprise version of InfluxDB) and InfluxData’s open source plug-ins, such as [Telegraf](https://oreil.ly/qLL4r).

Another example is Capital One, a US financial institution specializing in credit cards, car loans, and other products. Capital One generates a large amount of infrastructure, application, and business process metrics. This data plays a crucial role in maintaining high-performance systems and ensuring uninterrupted service. Capital One sought an advanced monitoring solution capable of ensuring high resilience and availability across multiple regions, while also integrating seamlessly with its machine learning systems to analyze data and generate predictive metrics. To this end, Capital One [created a fault-tolerant system with disaster recovery features](https://oreil.ly/9XaVz) based on InfluxDB Enterprise, AWS, and the visualization tool [Grafana](https://oreil.ly/ORBrH).

Another notable example is ProcessOut, a platform specializing in payment analytics and routing. ProcessOut [provides two main products](https://oreil.ly/QFdZU): Telescope, which analyzes transaction data to aid clients in understanding payment failures, and Smart Router, which assists clients in selecting the optimal payment system provider for specific transactions. ProcessOut [chose InfluxDB](https://oreil.ly/xYx16) to provide its consumers with the finest service while proactively monitoring and alerting them, depending on their payment actions. InfluxDB offers the functionality to collect, store, and manage critical payment information (logs, metrics, and events).

Examples like these, which you can check out [online](https://oreil.ly/xhPZj), highlight the critical role of data monitoring in the financial sector. Financial institutions prioritize monitoring not just as a necessity, but as a means to create business value and drive innovation.

## Events

Events are structured data emitted by an application during runtime. They are usually triggered by a specific type of activity and tend to belong to a predefined list of possible values. Examples include client HTTP requests such as POST and GET, response status (e.g., 404 NotFound), cloud resource operation (e.g., Amazon S3 object-level API activity such as GetObject, DeleteObject, and PutObject), and user permission changes (e.g., AmazonS3ReadOnlyAccess).

The structured nature of events makes them well-suited for storage and retrieval in tabular representations. That’s why event data is commonly stored in SQL databases.

## Logs

Logs are semi-structured data emitted by an application during runtime, providing greater flexibility in terms of content, structure, and triggering mechanisms compared to events. Logs are typically classified into five standard levels based on the severity of the issue. These levels, arranged from lowest to highest severity, are listed here:

Debug logs:   Used for diagnosing system issues in testing and development environments.

Info logs:   Information on normal system operations, which can be useful in case something doesn’t look normal. For example, you may want to log detailed records about transactions, including timestamps, amounts, trade submissions, account details and updates, and status (success/failure). Such information can be critical for auditing, compliance reporting, and resolving disputes or discrepancies.

Warning logs:   Information about potential issues that might lead to future problems if not addressed. These are used when something unexpected happens, but you want your application to continue running.

Error logs:   Information about serious issues that affect the operation being executed but not the service or the application as a whole. They require a developer’s intervention to fix. Examples include errors in processing a payment, a trade, or a loan application.

Critical logs:   Information about issues affecting the entire service or application and requiring immediate intervention, for example, if the primary database of a web application becomes completely inaccessible.

The extra flexibility of logs compared to events makes them essential for uncovering the root causes of issues. Logs can be general-purpose, such as errors related to software bugs or missing resources. They can also be software-specific, such as database-related errors like deadlocks, transaction conflicts, query timeouts, and the maximum connection limits reached.

A variety of tools can be used to store and query logs. Many companies use the ELK stack: Elasticsearch, Logstash, and Kibana. Cloud-based tools are also common, including Azure Monitor Logs, Google Cloud Logging, and Amazon CloudWatch.

## Traces

Traces represent a more advanced form of system behavior records, capturing comprehensive details about each step taken by a process as it progresses through one or more systems. Examples include the following:

Business operation traces:   Store information describing the steps involved in completing a business operation. For instance, tracing a trade order lifecycle from submission until execution or failure; tracing a payment flow initiation, authorization, processing, validation, and settlement; and tracing a loan application from submission through credit scoring, approval, and final disbursement.

Application traces:   Store information about an application’s behavior as it executes multiple components. This includes function calls, API requests, condition checks, input/output, resource usage, timeout, and execution time.

Security incident traces:   Store information on the events and activities associated with security incidents within a system.

# Unique Transaction Identifiers: Cornerstones of Effective Transaction Tracing

To ensure effective tracing, a trace identifier, also referred to as a transaction ID or correlation ID, is essential for uniquely identifying and monitoring the path of a particular transaction or request across a complex system. Such identifiers ensure that all related activities can be linked together, providing a complete view of the transaction’s lifecycle and ensuring transparency throughout the process.

In Chapter 3, you learned about transaction identifiers such as the Unique Transaction Identifier (UTI) defined in ISO 23897. The UTI was developed to offer a consistent reference that interlinks all related messages in an end-to-end financial transaction, allowing every party involved to refer to the transaction easily. This unique identifier remains unchanged throughout the various events of a transaction lifecycle, including amendments and version changes, thereby enhancing transparency and visibility across the settlement and reconciliation value chain.

Several frameworks, technologies, and tools come into play when designing a solution for storing and managing traces. OpenLineage is an open platform designed for collecting and analyzing data lineage. It tracks events related to data pipelines, including datasets, jobs, and executions. Apache Atlas is a metadata management and data governance tool that helps with data lineage, classification, and auditing. Apache NiFi enables the automated and efficient movement of data between systems, aiding in data lineage and flow management. For distributed tracing, Jaeger and Zipkin are widely used to monitor and troubleshoot errors and identify performance and latency bottlenecks in complex, microservices-based architectures.

# Data Quality Monitoring

Data generated and used by financial institutions must consistently meet high quality standards. Chapter 5 focused on financial data governance and extensively addressed the topic of data quality, discussing dimensions such as errors, duplicates, relevance, biases, completeness, timeliness, and outliers.

The traditional approach to data quality monitoring starts with the definition and development of *Data Quality Metrics* (DQMs). These metrics are quantitative measures used to assess and summarize the quality of specific aspects or dimensions of data. Defining the right DQMs depends on several factors that relate to client expectations (e.g., a data quality clause in an SLA), business requirements (e.g., complete sales and customer data), and technical standards (e.g., formatting, decimals, etc.). For this reason, there isn’t a fixed list of DQMs that fit all purposes. Instead, they are defined in an iterative and continuous process that involves financial data engineers, the business team, and data analysts/machine learning experts.

While there’s no one-size-fits-all approach, there are several DQM techniques that are commonly utilized. The usage of *ratios* is one such approach. For example, the *error ratio* indicates the percentage of erroneous records in a dataset, the *duplicate ratio* computes the percentage of duplicated records compared to all records within a dataset, and a *missing values ratio* can be used to measure the rate of available data compared to a fully complete dataset. Temporal data quality metrics may also be used. For example, to ensure data timeliness, metrics can be constructed to measure the age of a data item in a dataset and compare it against a reference date (e.g., < 1 week ago). Another metric may check data arrival time against an expected arrival time (e.g., every day at 10 a.m.).

Once DQMs have been defined, a corresponding monitoring process must be implemented. A well-known approach in this regard is *data profiling*. This involves parsing and checking a given dataset to understand its content, formatting, structure, and the relationships between its records. By performing data profiling, potential data quality issues within the dataset can be identified. Profiling can be performed column-wise, where each column is examined separately, or row-wise, where all columns and their relationships are analyzed. At the end of a data profiling check, a short report can be generated to summarize the main features and issues of the input dataset and provide recommendations for addressing such issues. [Figure 10-1](#ch10_figure_1_1724776835691982) illustrates some of the elements a typical data profile report might contain.

### Figure 10-1. A simple example of a data profile report

![Figure 10-1. A simple example of a data profile report](images/fden_1001.png)

Data profiling is a comprehensive procedure that scans the whole dataset to understand its data quality attributes. However, a complete data profile report may not always be required. Alternatively, a simpler approach could be to define and test data quality rules against one or more data records. A rule could state, for example, that the error ratio should not exceed 1%.

Once DQMs and the data quality monitoring process have been established, the next step is selecting a data quality tool or developing custom scripts to identify, validate, and flag any data quality issues. Commercial data quality tools include the Ataccama ONE Data Quality Suite, Informatica Data Quality, Precisely Trillium, SAS Data Quality, and Talend Data Fabric. There are also open source data quality tools such as the Python libraries Great Expectations, Soda Core, and DataCleaner.

It is essential to recognize that data quality monitoring is a continuous and evolving process. As the financial data landscape changes, with new data types, quality dimensions, and business requirements emerging, it is crucial to regularly revisit and refine your data quality monitoring process. This practice ensures the continued relevance and effectiveness of your data quality monitoring in safeguarding the quality of your data.

# Performance Monitoring

Performance refers to the ability of the financial data infrastructure to meet key operational criteria such as speed, latency, throughput, availability, scalability, and resource utilization. These performance indicators directly impact business performance by influencing critical aspects such as the following:

Time to Insight (TTI):   The time it takes to obtain actionable insights from data from the point it was generated. A shorter TTI enables fast delivery of financial data to end users, ensuring efficient decision-making, customer satisfaction, timely reporting, and revenue growth.

Time to Market (TTM):   The time it takes for a product to progress from a conceptualized idea to its introduction into the market.

Innovation velocity:   The pace at which data-driven innovations are generated and implemented

Data cycle time:   The time required to complete an entire cycle of data analysis, starting from problem formalization to obtaining actionable insights.

Various metrics are frequently used to monitor data infrastructure performance. Some are software-agnostic and apply to any type of application:

RAM usage:   The amount of memory being used by the application

CPU usage:   The percentage of CPU being used by the application

Storage usage:   The amount of disk storage being used by the application

Execution time:   The time needed to execute a task or process a request

Requests per second (RPS):   The number of requests made to an application every second

Ingress/egress bytes (bytes/sec):   The amount of network traffic (in bytes) entering and leaving an application

Uptime/downtime:   The ratio of time a system is operational to the total time observed

API response time:   The time it takes for an API endpoint to process and respond to a request

Concurrent users:   The number of users accessing an application simultaneously

Additionally, performance metrics can be tailored to specific software systems. For example, database management systems may have metrics such as the following:

Read/write operations:   Count of read and write operations performed on the database within a specific temporal window

Active connections:   Number of currently open database connections

Connection pool usage:   Utilization of connections within a connection pool

Query count:   Total number of queries processed by the database during a specified interval

Transaction runtime:   Duration taken to execute a database transaction

Replication lag:   The delay between the time data is written to the primary database instance and the time it is synched with read replicas

You can even have more granular metrics defined for a specific software component. For example, database queries may be monitored via metrics such as the following:

Records read:   The number of data records read by the database.

Blocks read:   The number of data blocks read by the database.

Bytes scanned:   The total number of bytes fetched by a query.

Number of output rows:   The final number of rows returned by a query.

Scan time:   The time spent by the database scanning the data.

Sort time:   The time spent by the database sorting the data.

Aggregation time:   The time spent by the database aggregating the data.

Peak memory:   The maximum amount of memory used during query execution.

Query plans:   The execution steps that a data storage system follows to fetch data in response to a query. Monitoring query plans can help detect costly queries and unused DB objects such as indexes and provide insights into query performance.

Additionally, you can implement performance metrics specific to your business’s technical needs. Examples from financial markets include the following:

Trade execution latency:   The time taken from when a trade order is placed until it is executed, which is critical for optimizing trading strategies and minimizing execution risks.

Trade execution error rate:   The frequency of failed transactions or trade orders, indicating operational inefficiencies.

Trade settlement time:   The duration from when a trade is executed to when it is settled, reflecting the efficiency of the settlement process.

Market data latency:   The time it takes for financial market data to be received from the exchange or data provider to the trading system, which impacts the speed of decision-making.

Algorithmic trading performance:   Includes metrics such as algorithm execution time and success rate, which can highlight the effectiveness and reliability of algorithmic trading strategies.

Risk exposure calculation time:   The time taken to compute and update risk exposure metrics, which is critical for managing and mitigating financial risks in real time.

Customer transaction processing time:   The duration from when a customer initiates a transaction (e.g., deposit, withdrawal) to its completion, which can impact customer satisfaction and operational efficiency.

# Case Study: Monitoring Real-Time Financial Data Feeds

In today’s fast-paced financial markets, real-time data feeds have become increasingly popular for providing the critical information necessary for making timely decisions. These feeds deliver up-to-the-second market data, including prices, volumes, and order book information, which are indispensable for traders, financial institutions, and automated trading systems. The reliance on accurate and timely data to capture market opportunities and manage risks effectively makes financial market feeds integral to the modern financial ecosystem. To ensure efficient and timely data delivery, providers of data feeds and related infrastructure need to thoroughly monitor the performance of their systems. Among the most important data feed performance metrics to monitor are the following.

Network Metrics

Packets per second (PPS):   The number of data packets transmitted and received per second.

Packet size distribution:   The size of data packets being transmitted and received.

Round-trip time (RTT):   The time for a signal to travel from sender to receiver and back.

One-way latency:   Tracks the time for a signal to travel from sender to receiver.

Bandwidth utilization:   Measures how much of the available network bandwidth is being used. Network bandwidth refers to the maximum rate at which data can be transmitted over a network connection in a given amount of time. Bandwidth utilization is about efficiency and capacity usage.

Data transfer rate (throughput):   Measures the actual amount of data transmitted per second. It’s about the speed of data movement.

System Metrics

CPU usage:   Percentage of CPU capacity used.

CPU time in I/O wait (iowait):   Time CPU spends waiting for I/O operations to complete.

CPU interrupt time (irq):   Time CPU spends handling software interrupts.

Memory utilization:   Percentage of memory being used.

Processing Metrics

Backpressure:   Tracks the system’s ability to handle incoming data rates. Backpressure occurs if the system receives more message requests than it can handle.

Buffer/queue sizes:   Monitor data waiting to be processed.

A particular type of performance metrics are incident response and management metrics, which are used to evaluate the effectiveness of an organization at tackling and preventing system downtime/outage issues. Examples include the following:

Mean Time to Detect (MTTD):   The expected time it takes to detect an issue or incident after it has occurred.

Mean Time Before Failure (MTBF):   The expected time between two failures/downtime in a repairable system. The higher the MTBF, the more reliable and available the system is, and the more effective the data engineering team is at preventing future issues.

Mean Time to Recovery (MTTR):   The expected time before a system recovers from a failure and becomes fully operational. A low MTTR indicates that the engineering team is quite effective at resolving the problem and that issue-fixing is efficient (e.g., through DevOps, DataOps, automated testing, etc.).

Mean Time to Failure (MTTF):   The expected time until a nonrepairable failure occurs. A nonrepairable failure requires replacing the failed system with a new one.

Mean Time to Acknowledge (MTTA):   The expected time from when an incident is reported to when someone starts working on the issue. A low MTTA indicates high team responsiveness and an effective alerting system.

Incident metrics are of primary importance in today’s always-on financial market infrastructures. The costs associated with outages and downtime in financial markets can be substantial, potentially leading to significant repercussions, especially given the interconnected and high-frequency/high-volume nature of financial activities.

Turning to technological implementations, there are numerous tools and frameworks designed for performance monitoring. Some are integrated into data engineering tools; for example, Apache Spark includes a UI interface for monitoring cluster status and resource usage. Open source tools such as [Prometheus](https://oreil.ly/Y6EJ6), designed primarily for metrics data, provide a rich set of monitoring and alerting features, including a multidimensional data model, flexible query language (PromQL), and multiple modes of dashboarding and visualizations. Another common approach involves using time series databases like InfluxDB, alongside advanced visualization tools such as Grafana.

Another popular and user-friendly option is cloud-based monitoring solutions. Using the cloud, it is possible to establish an alerting policy to get notified when performance-related issues occur. For example, Google Cloud provides a [managed alerting service](https://oreil.ly/2qrj6) where you can create an *alerting policy* that defines the circumstances under which an incident is created and the notification channel through which you want to be notified.