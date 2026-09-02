# Apache Spark: An In-Memory Computing Framework

When discussing data computing frameworks, it is difficult to avoid mentioning *Apache Spark,* a unified framework for large-scale data analytics. A bit of history is important to help understand the emergence of Spark. Early efforts at processing large data volumes led to the development of *Apache Hadoop*, a rich ecosystem of open source tools designed for managing multinode clusters and processing massive datasets. Hadoop’s ecosystem incorporates two key components: the Hadoop Distributed File System (which we discussed in Chapter 8) for distributed storage with high-throughput access to data, and MapReduce for large-scale parallel data processing. Crucially, MapReduce’s internal design processes data on disk, which was a major downside in terms of performance. In response, Apache Spark emerged as the next evolution in the Hadoop ecosystem. Compared to Hadoop MapReduce, Spark has demonstrated [significant performance improvements](https://oreil.ly/5tbsw).

One of Spark’s primary advantages is its native ability to perform computations in memory. While Spark can handle computations on disk when data exceeds memory capacity, data engineers typically configure sufficiently large Spark clusters to enable in-memory processing. Spark’s core memory data abstraction is known as the *Resilient Distributed Dataset* (RDD), which is immutable and can be distributed across nodes within a Spark cluster.

Spark is a rich framework that combines Spark Core (execution engine), Spark SQL (for structured data querying and processing), Spark Streaming (for streaming processing), the Spark machine learning library, MLib (for building machine learning models), and GraphX (for graph data processing).

Furthermore, Spark seamlessly integrates with several programming languages such as Scala, Java, Python, and R, allowing developers to write Spark programs in any of these languages. Among data engineers, the Python API known as PySpark is particularly popular and widely used.

Spark can be deployed on premises and on the cloud (e.g., using a cluster of Amazon EC2 instances). Managed cloud solutions such as Amazon EMR allow users to configure a Spark cluster without the need to deal with cluster and node configurations. Additionally, some cloud-based AI and analytics frameworks are powered by Apache Spark, for example, Databricks and Azure Synapse Analytics.

Apache Spark has multiple applications in finance. For example, it can be used to perform fast data transformations that involve massive financial datasets, such as high-frequency trades and quotes. Fraud detection is another use. For an illustrative architecture design, consider starting with a Spark ML model, such as logistic regression, designed for fraud detection. Data begins by entering an event stream through a message broker like Kafka, continues to Spark Streaming for real-time processing, and finally undergoes fraud verification using the deployed Spark ML model.13

Another scenario that requires deciding between in-memory and disk-based transformations involves choosing whether to perform transformations dynamically in memory or precomputing and storing them in a database beforehand. This can be the case, for example, when performing feature engineering. Doing feature engineering dynamically in memory can be advantageous for large and changing datasets, enabling real-time processing without the overhead of storing and managing precomputed features. This approach allows flexibility in adapting to changing data requirements and quality, but it may require substantial computational resources (e.g., RAM) and execution time. On the other hand, precomputing and persisting features in a DSS can enhance performance by reducing computation time and memory consumption during model training and inference, which is optimal in scenarios involving expensive queries and complex feature engineering steps. Furthermore, this approach ensures consistency and reproducibility of features across different stages of model development and deployment. Therefore, the choice should be guided by balancing computational efficiency, reproducibility, traceability, data freshness, and scalability needs.

### Full versus incremental data transformations

In a full data transformation pattern, the entire dataset (or its complete history) is transformed in one go, regardless of whether parts of it have been modified. This approach is typically used with small datasets that don’t change frequently. Its main advantages are simplicity (no need for sophisticated logic to process parts of the data), consistency (the entire dataset is processed uniformly), and simpler error handling (if an error occurs during transformation, it’s easy to detect since the entire operation will fail). This approach has drawbacks such as being resource intensive (especially with large datasets), limited scalability (if the dataset becomes large, processing it as a whole can become impractical or time-consuming), and potential latency issues (which may affect time-critical applications).

Alternatively, incremental data transformation involves transforming only new or updated data, rather than the entire dataset. This approach is commonly used with large datasets or applications that continuously generate and update data. Its main advantages include resource efficiency, scalability, low latency, and reduced costs. Note, however, that incremental data transformation may introduce additional complexity, as it requires implementing a change detection mechanism (e.g., Change Data Capture), data ingestion logic to handle only new or updated records, and data processing logic capable of inserting or updating records without overwriting existing ones.

# Change Data Capture

[*Change Data Capture* (CDC)](https://oreil.ly/CZowR) is an essential concept in data engineering. It refers to the capability of a data infrastructure to detect changes—such as inserts, updates, or deletes—in an upstream data source and propagate them across downstream systems that consume the data. A common scenario is the propagation of changes from an operational database to an analytical system such as a warehouse or a data lake. CDC is extensively used to ensure data consistency and integrity across various systems, support up-to-date real-time analytics, and help organizations migrate from on-premises to the cloud.

A CDC mechanism can operate in either a push or pull manner. In a push-based CDC, the source data storage system sends data changes to downstream applications. In a pull-based CDC, downstream applications regularly poll the source data storage system to retrieve data changes.

Several methods exist for implementing CDC. A straightforward approach involves adding a timestamp column that records the time of the latest changes. Downstream systems can then capture updates by querying data with timestamps greater than the last extracted timestamp. The main disadvantage of this method is that it may not effectively capture deletes.

Another common method relies on database triggers. A trigger is a stored procedure in a database that executes a specific function when certain events, such as inserts, updates, or deletes, occur. Triggers can propagate changes immediately but may add additional load to the source database. Some data storage solutions, such as [Mon⁠go­DB](https://oreil.ly/CFEIY), implement a separate trigger layer that scales independently of the database server.

Finally, a highly reliable CDC approach involves using database logs. To ensure durability and consistency, many database systems log all changes into a transaction log before persisting them to the database. Logs are quite reliable as they capture all changes made to the data, along with metadata about who made the changes and when. The main challenge with this approach is the potential complexity of setting it up and maintaining it.

## Computational Requirements

When designing the transformation layer, you must assess and plan your computational requirements. The main factors to consider are computing environments and performance.

### Computational performance

Having a framework that outlines performance requirements and optimization strategies is essential for a reliable transformation layer. This framework should include features such as computational speed, throughput, efficiency, and scalability.

## Computational speed

Speed is a critical requirement for financial data transformations. It is typically measured by the time difference between the start and end time of a data transformation execution. A related and more specific concept is *latency*, which denotes the time it takes for a signal or message to travel over a network to its destination and receive a response back from it. Common latency metrics include the *average latency*, which is the mean time it takes for two systems to exchange messages, and *latency jitter*, which is the variation in latencies around the average value.

Throughout the rest of this section, I will use the term computational speed to describe the difference between the expected and the actual processing time of a given data transformation. This presupposes that you, as a financial engineer, should discuss and determine the ideal execution time for the many financial data transformations and keep an eye on your infrastructure to make sure it performs up to par. This can be linked to the data timeliness dimension that you learned about in Chapter 5.

### Note

In general, the higher the computational speed you aim for, the more technically challenging it becomes. It is simpler to reduce computation time from hours to minutes than from seconds to microseconds. For this reason, treat it as an economic problem by estimating the marginal gain from every unit of improvement in computational speed. Certain types of financial data transformations (e.g., monthly price extractions) may not require significant computational speed.

To guarantee fast data transformations, a common practice involves the definition of a Service-Level Agreement (SLA) that outlines the average duration of data transformations (e.g., five seconds) or the time by which a specific data transformation should have been finished (every Friday at 10 a.m.).

# The Cost of Speed in Financial Markets

Speed in financial markets comes with its own set of risks. For instance, the drive toward instant payment and settlement processes increases exposure to fraud risks, as the system has limited time to analyze, detect, and prevent fraudulent activities and ensure compliance. Moreover, this can expose participants to liquidity, market, and credit risks. For example, during settlement, financial institutions must ensure they have sufficient liquidity to handle instant payments, particularly during peak times. Instant payments also expose market participants to credit risk if counter parties fail to settle transactions promptly.

High-frequency trading is another area where speed is key, with rapid data access and quick decision-making being critical elements. However, relying on real-time market data for fast trading might, in some cases, be risky because the data may contain errors or noise, leaving the trading system with limited time to properly assess the quality of the data.

Furthermore, fast trading systems like high-frequency and algorithmic trading can amplify market volatility, particularly during periods of stress. In addition, the pursuit of speed has contributed to events like flash crashes, where market prices drop sharply and recover within minutes. The reliance on sophisticated algorithms and high-speed trading infrastructure increases the risk of technical failures, such as software bugs, hardware malfunctions, or connectivity issues.

Fast order execution in trading poses challenges for regulatory compliance as well. For instance, rapid order cancellations or modifications by high-frequency traders can strain market surveillance systems responsible for upholding fair market practices and preventing market manipulation.

These examples highlight the distinctive characteristics of data engineering in finance compared to other industries. While speed may not pose major risks in certain sectors, in finance, rapid transactions and decisions can introduce substantial risks that must be carefully considered when designing financial data infrastructures.

Once an SLA is defined, the next step would be to compare the actual data transformation time against the SLA specification. Should the SLA be violated, you, as a financial data engineer, need to understand the main causes and propose potential solutions. Factors that might impact data transformation execution time include the following:

* Low-quality data that requires more steps to clean
* Poor querying patterns that take more time than necessary
* Dispersed data that requires multiple queries to collect
* A wrong data storage model (e.g., using a data lake instead of a data warehouse for structured data)
* Large batch jobs
* Limitations on the database side (e.g., max concurrent connections)
* Poor database design (e.g., missing or bad indexes)
* Too much complexity in the transformation logic
* Insufficient compute resources (e.g., low RAM or CPU)
* Shared resources that need to respond to requests coming from a variety of applications
* Bad queuing strategy (e.g., jobs are not ordered and executed in the right priority, big or time-consuming batch jobs run before small interactive requests, lack of asynchronous or parallel execution capabilities)
* Wrong transformation patterns (e.g., executing data transformations with synchronous blocking can slow down performance compared to asynchronous event-driven or streaming solutions; more on this in Chapter 11)
* Network issues
* Too many processing layers
* Inefficient data distribution among data centers (data is far from the processing engine)

Ideally, you should anticipate and test for such issues in advance. As discussed in Chapter 8, changing your data storage system is a costly operation that should be avoided. Similarly, once your data transformation layer is defined and implemented, you don’t want to migrate or alter it.

## Throughput

In data-intensive applications, an important performance measure is throughput. This refers to the amount of data that a system can process in a given time interval. Applications designed for high throughput emphasize the total amount of work that can be done in a given period of time. This is often measured using metrics such as bits per second (bit/s or bps), megabytes per second, or records per second.

In today’s financial markets, especially trading systems, high throughput is essential due to the continuous influx of a massive number of orders that require immediate processing.14 From an engineering perspective, it’s crucial to define the desired level of throughput clearly. Simply aiming for “high throughput” is not specific enough. As such, it’s essential to define a target throughput level through discussions with your business team and stakeholders.

The level of throughput may depend on a variety of factors, including the characteristics of the physical and networking infrastructure, the size and type of the data being processed in each request, and the type of operation being performed. For instance, when optimizing database read/write throughput, it is important to keep in mind that reading and writing have different internal mechanisms.15

## Computational efficiency

The term computational efficiency is used to describe how well data transformations make use of available resources. An efficient data transformation minimizes resource consumption, which is increasingly important given the current emphasis on the environmental impact of data computations, such as carbon footprint.

The term *algorithmic efficiency* is often used in this context to measure the computational resources that an algorithm uses. Generally speaking, the more time and space an algorithm consumes, the less efficient it is. Interestingly, in 2020, a group of researchers from MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL) presented evidence showing that [data-intensive tasks benefit more from algorithmic efficiency than hardware improvement](https://oreil.ly/xiNDo).

# High-Performance Computing in Finance

Finance has a lot of computationally expensive problems. Examples include risk valuation, derivative pricing, stress testing, scenario analysis, and Credit Value Adjustments (CVAs). Such problems are computationally expensive due to their nonlinear and high-dimensional nature, which results in a massive number of computations that need to be performed. I won’t go into the details of these problems, but for those interested, I suggest reading the S&P Global blog entry [“Accelerating CVA Calculations Using Quasi Monte Carlo Methods”](https://oreil.ly/nTBF-) on accelerating CVA calculations that illustrates the complexity of computing CVAs.

To address such computational challenges, the industry has responded with two streams of improvement: software-side and hardware-side improvements. Software-side improvements often entail the development of more efficient algorithms and computational models. On the hardware side, financial markets have expressed interest in what is called *High-Performance Computing* (HPC). HPC refers to the practice of aggregating and connecting multiple computing resources to solve complex computation problems efficiently. HPC isn’t just one technology, but rather [a model to build powerful computing environments](https://oreil.ly/de-8e).

Designing an HPC cluster leverages several concepts and technologies such as parallel computing, distributed computing, virtualization, Central Processing Units (CPUs), Graphics Processing Units (GPUs), in-memory computation, networking, and many more.

An HPC cluster can be implemented in a variety of ways. For example, an Apache Spark cluster can be considered an HPC. A cluster of connected EC2 instances is also an HPC environment. More complex forms of HPC clusters combine heterogeneous types of machines that serve different purposes (e.g., compute-optimized with high CPU count, memory-optimized, GPU-accelerated). Some organizations develop custom-built HPC supercomputers, highly optimized for superior speed and performance compared to standard computing systems. Supercomputers are often benchmarked using the [*floating-point operations per second* (FLOPS) measure](https://oreil.ly/EM8Jx).

For more on HPC in finance, see Michael Alan Howarth Dempster, Juho Kanniainen, John Keane, and Erik Vynckier, eds., *High-Performance Computing in Finance: Problems, Methods, and Solutions* (CRC Press, 2018).

## Scalability

Computational performance is very often dependent on the scalability features of the underlying infrastructure. When there is an increase in the number of data transformations or sudden peaks in workload, the computational capacity needs to scale proportionally to efficiently manage the increased load.

Taking a cloud context as a reference, scalability can be achieved by either adding more resources (e.g., additional EC2 instances or cloud functions) or by upgrading the capacity of existing resources (e.g., replacing smaller EC2 instances with larger ones). Scalability can be implemented following different strategies, such as the following:

Manual scaling:   Where you manually scale existing resources to meet new demands

Dynamic scaling:   Where you configure an autoscaling policy to automatically provision more resources in reaction to larger demands (e.g., if total CPU usage > 90% → provision X resources)

Scheduled scaling:   When you configure an autoscaling policy to provision more resources on a given schedule (e.g., every Wednesday between 9 a.m. and 4 p.m., provision 200 more EC2 instances)

Predictive scaling:   Where a machine learning model is used to predict and provision resources based on historical usage patterns

Scalability requires careful consideration. In particular, when planning the scaling requirements for the transformation layer, it’s important to also assess the scalability features of the storage layer. For example, if you have a max concurrency limit on the data storage layer (e.g., 500 concurrent requests), it’s essential to properly manage the number of concurrent requests arriving from the transformation layer to avoid overloading the storage layer. Ideally, the design of both the storage and transformation layers should be iterative, ensuring compatibility in scalability features to achieve optimal performance.

### Computing environments

Once you have identified your computational requirements, the next step is choosing a computing environment that aligns with these specifications. Such an environment typically comprises three key components: software (e.g., operating system, programming language, libraries, frameworks), hardware (e.g., storage, RAM, CPU, GPU), and networking (e.g., TCP/IP, VPC, etc.).

There is a large variety of computing environments that can be configured to run the transformation layer tasks. Traditionally, many financial institutions, in particular banks, have [relied on mainframe computing environments](https://oreil.ly/HCSU2) that run on languages such as Common Business Oriented Language (COBOL). However, modern financial applications are leveraging open source technologies and the cloud as a viable and simpler alternative.

If we choose to leverage cloud infrastructure, there are several approaches to consider when setting up the computing environment for the data transformation layer. The most flexible strategy is infrastructure-as-a-service (IaaS), where you provision and configure several computing machines to perform the data transformations. In this setting, you will be responsible for installing the required programming languages (e.g., Python, Java, Go, etc.), configuring security policies (e.g., ingress and egress rules), and installing all necessary packages (e.g., PySpark, Apache Airflow, etc.). The main advantage of IaaS is the extra control it offers over environment configuration. However, managing, configuring, and securing your instances under IaaS can potentially lead to a waste of time and effort.

As an alternative to IaaS, cloud providers offer several managed services that alleviate the need to configure and maintain the compute instances. In such settings, the user interacts with a declarative interface where they define the desired configuration of their environment. The cloud provider takes responsibility for provisioning, scaling, and managing the underlying infrastructure, offering greater convenience and often reducing administrative overhead for users compared to the IaaS model. For example, AWS offers *Managed Workflows for Apache Airflow* (MWAA), a managed service for running the data workflow management solution Apache Airflow (which we will discuss in “Extract-Transform-Load Workflows”).

Another popular choice for cloud-based computing environments is serverless cloud functions, which allow users to deploy and run code in a variety of languages without provisioning or managing servers. Cloud functions are ideal for short-time data transformation operations (several seconds or minutes). Examples include AWS Lambda and Google Cloud Functions (first and second generations). One of the main advantages of cloud functions is that they can be integrated with a wide range of other services and handle event-based workloads. For example, it is possible to configure a cloud function to run upon the arrival of a file in storage (e.g., Amazon S3), upon the arrival of a message in a queue (e.g., Amazon Kinesis), or with database updates (e.g., Amazon DynamoDB).

# Case Study: FINRA’s Transition to AWS Lambda for OATS Data Validation

The Financial Industry Regulatory Authority (FINRA) is a US nongovernmental organization responsible for protecting investors and ensuring market integrity by overseeing and regulating broker-dealers. To monitor the trading practices of member firms, FINRA has an integrated audit trail system of orders, quotes, and trade events for National Market System (NMS) stocks and over-the-counter (OTC) equities. To record such data, FINRA’s audit trail relies on the Order Audit Trail System (OATS). Using OATS data, along with other sources of market and reference data, FINRA is able to reconstruct the lifecycle of a trade—from origination through completion or cancellation—and monitor the practices of its members.

Member firms submit daily OATS data to FINRA, totaling more than 50,000 files each day. Upon receipt, FINRA verifies the data’s completeness and proper formatting against more than 200 rules, processing up to half a trillion validations daily. To handle the significant and variable processing demands, [FINRA needed a scalable, cost-efficient, and secure solution](https://oreil.ly/PfIlQ).

Three options were explored—Apache Ignite on Amazon EC2, Apache Spark on Amazon EMR, and AWS Lambda. AWS Lambda emerged as the optimal choice due to its scalability, efficient data partitioning, robust monitoring, high performance, cost-effectiveness, and minimal maintenance needs. This choice supported FINRA’s goal of transitioning to a real-time processing model.

Security was a critical factor, and AWS met FINRA’s stringent data-protection requirements, including encryption of data in transit and at rest. The new system was developed in three months, with data ingested into Amazon S3 via FTP and validated using AWS Lambda functions. A controller, running on Amazon EC2, manages data feeds into AWS Lambda and outgoing notifications, as well as external data sources like stock symbol reference files.

To ensure continuous operation and reduce processing time, the new architecture leverages AWS Lambda’s data-caching abilities and uses Amazon SQS for input/output notifications.

# Data Delivery

Once data has been transformed, the next step is to deliver it to the final consumers to extract actionable insights. Financial data engineers must determine who the ultimate data consumers are and understand their specific needs, and then create the appropriate mechanisms to deliver the data. The following two sections will provide a brief overview of this process.

## Data Consumers

Any user, application, business unit, team, or system that makes use of data generated by their company’s data infrastructure is considered a data consumer. Human data consumers can engage in the data engineering lifecycle to varying extents. For example, compliance officers and marketing teams often specify their data needs and rely on data engineers to handle the rest. In contrast, analysts and machine learning specialists may be more involved in defining the data source, type, and necessary transformations.

Data consumers may also differ in terms of their data governance duties and responsibilities. For instance, senior individuals in control of the data in a certain domain are known as data owners. In a bank, for instance, the finance director may be the owner of client financial data. A related role is that of the *data steward,* who is responsible for maintaining and guaranteeing the quality and consistency of data as defined by the data owner. Data custodians are in charge of protecting the data by adhering to the rules outlined in the data governance framework.

Financial data engineers, being the data producers, must ensure that data consumers have clear and well-defined expectations and requirements to facilitate effective data delivery. A reliable way to formalize such an agreement between data consumers and producers is through data contracts, which were discussed in Chapter 5. A data contract can detail all consumer requirements such as the data type, fields, formats, constraints, conversions, SLA, and many more. Data contracts are often owned by the data owner or delegated to the data steward. With a data contract, one can be sure data producers know exactly what data consumers want, thus avoiding miscommunication issues around the data.

## Delivery Mechanisms

Data can be delivered to its final consumers in a variety of ways. These include the following:

* Direct database access via a user interface (e.g., Snowflake UI, pgAdmin for PostgreSQL, Compass for MongoDB, etc.). This mechanism is often intended for people with basic SQL knowledge who want to conduct exploratory data analysis.
* Direct file access via a user interface (e.g., the S3 web interface). This is intended for easy interaction and sharing of the data.
* Programmatic access to databases and file repositories via APIs, JDBC (Java Database Connectivity), ODBC (Open Database Connectivity), and client libraries such as AWS Boto3. This delivery mechanism is widely used by applications, software engineers, and data engineers alike.
* Reports that contain essential summaries and aggregations of data used for supporting decision-making.
* Dashboard access that displays metric and summary data in a visual format, typically via a single web page. Dashboards are feature rich, and come with a variety of tools to visualize, explore, filter, compare, zoom, and query the data in a user-friendly way. They are quite useful for stakeholders who don’t have much expertise or the time to perform raw data querying and analysis.
* Email delivery.

An important thing to keep in mind when designing a delivery mechanism is the need to provide users with the means to search and find the data they are looking for. As more data gets generated and stored in various locations, it becomes harder for data consumers to know where to find what they are looking for. Some good practices can be adopted in this regard. For example, the final location of the data needs to be specified in the data contract. Additionally, a data catalog can be created as a central search engine that allows users to search and find the data they are seeking.