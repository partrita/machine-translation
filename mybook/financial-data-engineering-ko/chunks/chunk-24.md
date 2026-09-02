### Technological implementations of time series databases

A variety of time series database implementations have been developed in the market. These can be divided into native and non-native implementations.

A non-native implementation is not primarily designed for time series data, but it can be used for this purpose. For example, it is possible to use an SQL database such as PostgreSQL to create a time series table like the one shown in [Table 8-1](#ch08_table_1_1724776834176432). To boost performance, an index like a B-tree or BRIN (Block Range Index) can be created on one or more tag columns plus the timestamp column. Furthermore, PostgreSQL supports index-based table clustering, which can enhance the efficiency of queries that filter by a given temporal interval. Similarly, a document database such as MongoDB can be used to store a time series as a set of documents in a collection indexed by time and tag keys.

Crucially, while SQL and document databases may be able to handle time series data, they are not optimized for this purpose. Two options are available to overcome this issue. First is time series extensions created on top of general-purpose databases. A prominent example is TimescaleDB, which extends PostgreSQL with time series characteristics. TimescaleDB is quite popular due to its performance, scalability, and compatibility with PostgreSQL and the SQL query language. As another example, MongoDB introduced [time series collections](https://oreil.ly/4CJmg), which allow for optimized storage and retrieval of time series data. To do this, MongoDB time series collections use a columnar storage format and store data in time order. Moreover, upon the creation of a time series collection, MongoDB automatically creates a composite index on the time and metadata fields.

The second and most reliable option for handling time series data is native purpose-built time series databases. A good example is kdb+, developed and maintained by KX. Kdb+ is designed with high performance and scalability features in mind. It stores the data in a columnar format, allowing for efficient data compression and fast queries. In addition, it uses an in-memory compute engine for fast processing and querying in real time. Furthermore, kdb+ supports the q language, which is known for its powerful and efficient querying capabilities.

# In-Memory Databases

Some database systems may frequently be referred to as in-memory databases or as having in-memory characteristics. What this means is that the database system keeps all or part of its data in memory (i.e., RAM). By storing data in memory, the database achieves very low response times (i.e., low latency) by eliminating the need to fetch the data from disk. It is well-known empirically that RAM-based access is substantially faster than disk access, precisely random disk access. In-memory data access capabilities can be crucial for time-critical applications such as trading and online stores. A common data management strategy with in-memory databases involves storing the most current data in memory while keeping historical data in a separate location.

There are different types of in-memory databases. On the one hand, there are native in-memory databases such as Redis and kdb+. Among financial institutions, the [Oracle TimesTen in-memory database](https://oreil.ly/76R41) has been widely used. Alternatively, there are in-memory extensions designed to improve the performance of existing DSSs. For example, the Amazon DynamoDB Accelerator was created to add in-memory capabilities to DynamoDB tables. To boost the performance of their primary database product, Db2, IBM introduced BLU Acceleration, which adds in-memory processing capabilities and columnar storage to enhance the speed of data analytics. Open source in-memory storage and computing frameworks such as Apache Ignite also exist.

Two things are worth noting when working with in-memory databases. First, they are not to be treated as a primary DSS as data in memory is considered volatile (if the machine is shut down, the data will be lost). Second, data stored in memory may become invalid and require a refresh. Such a practice is called [cache invalidation](https://oreil.ly/_u7PF) and may be a challenging issue if not understood properly.

Another popular time series database is InfluxDB, developed and marketed by InfluxData. InfluxDB is a native time series database designed for high performance and intuitiveness. InfluxData uses *InfluxQL*, an SQL-like query language for querying data in InfluxDB databases. InfluxDB implements a data model that organizes data around buckets, databases, retention policies, series, measurements, tag keys, tag values, and field keys. InfluxDB’s engine relies on an optimized data storage format called a Time-Structured Merge Tree (TSM) and an indexing technique called Time Series Index (TSI).21

### Financial use cases of time series databases

Time series databases were originally developed for financial applications. As new market structures such as high-frequency and electronic trading mechanisms emerged, the volume of trades, quotes, and prices experienced a substantial increase. For example, the NYSE, which currently allows trading for all 8,000+ US securities, reports that [an average of 2.4 billion shares exchange hands on a daily basis](https://oreil.ly/grEbF). In addition to volume, the speed of data generation has also increased. Nowadays, high-frequency trading at the NYSE occurs at the nanosecond level (i.e., one-billionth of a second). Consequently, a single second of trading can have hundreds of trades and quotes and reveal a variety of market patterns.

Multiple firms, in particular those involved in high-frequency and algorithmic trading, can leverage this fine-grained market view. However, to stay competitive, rapid data access is crucial. This is where highly performant DSSs, such as time series databases, are required.

Kdb+ has become a primary choice for financial markets, particularly in high-frequency trading, due to its exceptional performance and speed.22 One of the main [challenges](https://oreil.ly/uT61x) that firms using kdb+ face is the need for fast access and analysis of critical market data in real time.

## The Message Broker Model

In distributed systems, it is common for multiple applications to need to communicate with each other to complete specific tasks. A typical scenario involves one type of application, known as *producers,* generating and storing data messages asynchronously23 in a shared data store, and another type of application, called *consumers,* reading and processing the messages from the same store. This communication pattern is known as the *producer-consumer pattern*. [Figure 8-6](#ch08_figure_6_1724776834148599) provides an example.

A DSM that follows the producer-consumer pattern is called a message broker DSM, and a technology that implements the message broker DSM is simply called a *message broker*. In the next few sections, you will learn about the main features of message brokers, their data modeling principles, technological implementations, and, lastly, their use cases in the financial sector.

### Figure 8-6. The message broker model

![Figure 8-6. The message broker model](images/fden_0806.png)

### Why message brokers?

Message brokers are widely used in developing data-intensive systems, particularly in event-driven, distributed, and streaming architectures. In these contexts, data is generated and consumed by various applications following different patterns and scales. To meet such requirements, message brokers offer the ideal features in terms of simplicity, speed, and scalability. Importantly, a message broker is not to be used as a primary or persistent DSS but rather as an intermediary that facilitates the exchange of messages between applications.

By decoupling data production and consumption, message brokers enable producer and consumer applications to work and scale independently. If a small number of messages are being produced, a few consumers can handle the workload. However, if the number of messages increases significantly, additional consumers can be added to handle the increased load. Moreover, producers need not worry about who the consumers of the data will be, which allows for flexibility in adding different types of consumers based on business needs.

A distinguishing feature of message brokers is their fault tolerance. Consumers and producers can be easily replaced in case of failure without impacting the state of the message broker. Moreover, message brokers are quite simple to use as applications only need to know the topic for publishing or consuming messages. Let’s discuss message topics in the next section.

### Data modeling with message brokers

Message broker data modeling revolves around two main concepts: topics and message schema, which I will illustrate in this section.

## Topic modeling

Topics are the main building blocks of message brokers. A topic is a unique container of messages that publishers and subscribers need to specify when communicating with each other. Think of topics as the equivalent of tables in SQL databases.

Topic modeling involves defining the topics and their target consumers and producers. They can be created based on business requirements. In some cases, certain message brokers support multiple types of topics, each optimized for a specific need. For example, suppose you have an online application offering customer support for five categories of issues, each handled by a different backend system. If you decide to use a message broker, then you may want to create five topics, each handling a different type of client request. In this case, if Topic 1 handles issues of Type A, then only messages related to issue Type A will be published to that topic, and only backend systems that handle issue Type A will be able to process messages from Topic 1.

Naturally, large-scale applications can have hundreds or even thousands of topics. In this case, establishing data governance policies for topic management becomes critical. This might include the people and methods involved in creating a topic, the producer and consumer applications that are permitted to use it, the type and format of data that can be submitted to the topic, data quality checks and validations, data anonymization, encryption, and data loss management.

## Message schemas

Message brokers do not enforce a schema on message structure, offering flexibility in message definition. However, if consumers don’t know what information to expect from producers, things might get out of control. This situation may force applications to manage multiple formats, which adds unnecessary complexity.

Therefore, it is a good practice to define a message schema for each topic initially and then implement validators on both the producer and consumer sides. These validators ensure that the message content is checked for correctness before it is published or consumed.

The most popular format for message definition is JSON. However, it is also possible to use XML or other formats.

# Message Schema Registry

One of the best practices in designing message brokers is the establishment of a message schema registry. This consists of a centralized repository for storing, managing, versioning, and validating schemas for topic message data. Think of the schema registry as data governance practices that allow producers and consumers to communicate over a well-defined data contract in the form of a schema.

Apache Kafka, which is discussed in more detail later in this section, is a leading example of a message broker that [supports a schema registry](https://oreil.ly/d1UZx). The schema registry in Kafka facilitates schema evolution and compatibility, enabling producers and consumers to update their schemas while preserving data integrity and cross-version compatibility. This capability is especially valuable for ensuring that data written to Kafka remains well structured and can be accurately interpreted by downstream consumers.

A technical aspect to keep in mind about message brokers is that they typically require messages to be serialized before being submitted to a topic. The message consumer then deserializes the message back into its original structure. Serialization is the process of converting a data object into a format optimized for transmission and storage, typically a byte stream. Deserialization reverses this process, converting the byte stream back into the original data object. While custom serializers and deserializers can be created, it is common to use built-in ones for formats such as JSON, Avro, and Protocol Buffers.24

### Technological implementations of message brokers

Several technological options are available for implementing a message broker. Examples include Apache Kafka, RabbitMQ, Redis, Google Pub/Sub, Apache ActiveMQ, Amazon SQS, Amazon SNS, and Azure Service Bus. Making a full comparison between such technologies is beyond the scope of this book. However, the following criteria can be used to perform a technical assessment:

Business need:   Some message brokers are designed for specific use cases, such as message queues (e.g., AWS SQS), while others are better suited for multiconsumer notifications (e.g., AWS SNS).

Performance:   Message brokers differ in throughput and message read/write latency. For instance, Apache Kafka excels in throughput, whereas Redis is known for its low latency.

Delivery mode:   Message brokers offer different levels of message delivery guarantees, such as “At Most Once,” “At Least Once,” and “Exactly Once.” For more details, refer to Cloudflare’s [documentation page](https://oreil.ly/-dvZz).

Message persistence:   Some message brokers purge messages from their store upon delivery to consumers (e.g., Apache ActiveMQ and RabbitMQ), while others store messages in a commit log where the same message can be consumed by multiple consumers and at a later point in time.

Scalability:   Message brokers can vary in their scaling capabilities. Some excel at scaling message production, enabling the publication of a large number of messages per second, while others are more effective at scaling consumption, allowing for many concurrent consumers. For example, Apache Kafka is well-known for its scalability features. One way this can be achieved is by allowing a topic to be further divided into partitions. This way, instead of having one consumer blocking a topic, partitions allow multiple consumers to read messages from the same topic by referencing the partition ID within the topic from which they want to consume data.

Message prioritization:   Some message brokers, such as RabbitMQ and ActiveMQ, offer message prioritization features whereby high-priority messages are consumed before low-priority messages.

Message ordering:   Message ordering refers to the order in which messages are consumed from a topic. While some message brokers may not enforce any specific ordering, others ensure that messages are consumed following a specific order, such as consuming the first messages received first.

When developing a cloud-based data infrastructure, managed cloud message brokers can be an excellent choice. These solutions are specifically engineered to seamlessly integrate with other cloud services. For example, you can configure topics to automatically receive messages when a file is uploaded to cloud storage. Then, a cloud function can consume that message from the same topic to perform a specific task related to that file.

### Financial use cases of message brokers

Message brokers have found a variety of applications in the financial sector, particularly in the development of event-driven and real-time systems. They are extensively used for managing operations involving a continuous stream of high-volume data such as payments, credit card transactions, loan applications, ATMs, and mobile notifications. Message brokers can streamline tasks such as fraud analysis, application and transaction approvals or rejections, credit authorizations, and client notifications.

For example, At PayPal, [Apache Kafka has been used extensively](https://oreil.ly/3Xh7Y) to support various critical operations such as first-party tracking, metrics streaming, database synchronization, log aggregation, batch processing, risk management, and analytics, with each of these use cases processing over 100 billion messages daily. PayPal’s Kafka infrastructure includes 1,500 brokers across 85+ clusters, 20,000 topics, and nearly 2,000 Mirror Maker nodes, achieving 99.99% availability. In the 2022 Retail Friday, PayPal’s Kafka processed a traffic volume of 21 million messages per second, which totaled about 1.3 trillion messages in a single day. Similarly, Cyber Monday of the same year resulted in 19 million messages per second, totaling 1.23 trillion messages in a single day.

Another significant application of message brokers in finance is the development of highly scalable and efficient applications that handle real-time financial data sharing, messaging, and streaming. For example, a financial data provider can leverage Apache Kafka to offer various types of data by organizing them into different topics. Subsequently, clients are subscribed to a specific topic based on their subscription plan. Kafka uses *Access Control Lists* (ACLs) as an authorization mechanism to determine which users are allowed to perform which actions on Kafka resources. Moreover, within the same topic, it is possible to further categorize the data into partitions (e.g., by ticker) and offer clients the option to subscribe to a subset of the partitions. Kafka has the concept of a *consumer group*, which can be used to allow different clients to consume the same data from the same topic/partition using a Kafka consumer offset. An offset is just a pointer that indicates the position within a partition of the next message to be consumed by a consumer group.25

# Case Study: Real-Time Fraud Detection at ING Group with Apache Kafka

ING Group is a Dutch multinational financial services corporation that provides a wide range of services such as retail and commercial banking, investment banking, and insurance services. ING, like other commercial banking firms, has a mechanism in place to identify fraud in its online banking activities. However, over time, this system became overly complex, expensive, unreliable, and challenging to scale effectively to manage the growing volume of data required for real-time fraud detection.

To overcome these issues, the ING engineering team decided to leverage Apache Kafka as the main *event bus* to support real-time fraud detection and other data streaming use cases. In a [presentation given by ING experts Timor Timuri and Richard Bras in 2018](https://oreil.ly/9J6_3), they illustrated the high-level use case of Apache Kafka.

To handle client-sensitive data, the ING team introduced security into the messages stored in Kafka via a symmetric end-to-end encryption module. This works by first encrypting the data before publishing it to a topic and then decrypting it upon consumption by the consumer.

The Protocol Buffers (protobuf) format was chosen for message serialization/deserialization. Before publishing, messages are serialized into protobuf, and when consumers receive the message, they deserialize it.

In addition, the ING engineering team created a number of predefined client settings to allow users who just want to use Kafka and do not care about the details (e.g., publish messages to a topic). This was provided via a simple and easy-to-use interface. Furthermore, test components were developed to simulate message publication, and monitoring was introduced to evaluate Kafka’s performance. For compliance purposes, all events are persisted in a Cassandra data store.

To ensure availability, ING’s team adopted a multi–data center strategy to replicate data and ensure availability in case of downtimes or disasters.

Crucially, while Kafka initially served for real-time fraud detection at scale, it later expanded to become a primary development platform supporting a wide array of applications. By 2018, ING managed 200 topics, processing 1 billion messages daily with peak rates of 20,000 messages per second. Kafka is utilized across over 100 teams at ING, catering to 120 distinct use cases.

## The Graph Model

In Chapter 2, we explored graph data, illustrating its structures, types, and financial applications. One of the main advantages of graph data is its ability to reveal complex patterns and mechanisms that simpler data types (e.g., time series) cannot uncover. As a result, a wide range of applications have been created, the primary functionality of which revolves around the storing and processing of graph data. The graph DSM is intended for such use cases. A technology that implements the graph DSM is known as a graph DSS or, more commonly, a *graph database*.

In the following sections, we will examine the key aspects of the graph DSM, graph databases, graph data modeling principles, technological implementations, and, finally, financial use cases.

### Why a graph model?

The graph DSM is used when designing graph-oriented applications that prioritize the storing and analysis of data relationships. Examples of such requirements include the following:

Centrality analysis:   This aims at identifying the most important nodes in a network. For instance, it can be applied to identify *Systemically Important Financial Institutions* (SIFIs), whose failure could potentially disrupt the entire financial system, or market participants who play major roles as intermediaries, facilitating various transactions.

Search and pathfinding:   This aims at locating nodes with specific attributes or determining the most efficient path between two nodes within a graph. A widely used approach is shortest path analysis, which identifies the path between nodes with the fewest edges or minimal weights.

Community detection:   This aims at finding cohesive regions or subgraphs of connected nodes within a graph. Such subgraphs are called communities. Examples include stock market clusters (stocks that move together), interbank lending clusters (e.g., banks that frequently transact with each other), and fraud detection (e.g., groups of transactions that might be linked to fraud rings).

Contagion analysis:   This examines how a shock impacting one or a set of nodes propagates throughout the rest of the network. Applications include financial stress testing, cascade failures, and systematic risk analysis.

Link prediction:   This aims at identifying pairs of nodes that are likely to establish a link in the future (e.g., two financial institutions establishing a correspondence banking relationship).

It’s important to remember that the graph data element must be crucial to your application to justify using a graph DSM. If your application needs to store graph data but does not require specialized graph capabilities, then a general-purpose model such as SQL may suffice.

For instance, consider a financial graph where nodes represent banks and links represent asset exposure (e.g., how many assets bank A holds at bank B). If bank A is primarily concerned with its direct exposure to the network, an SQL DSM can handle this efficiently. You can create a table with three columns: source\_bank, target\_bank, and exposure. To get your bank’s total exposure, you simply run SELECT target_bank, exposure WHERE source_bank = "YOUR_BANK_NAME". However, if you need to calculate the exposure of a bank to which your bank is exposed (similar to finding the friends of your friend), the SQL model would require complex joins and recursive operations to achieve this. This is where the graph DSM excels, as its storage and processing logic is specifically designed for such tasks.

### Data modeling with graph databases

Graph data modeling is quite intuitive and flexible. It [involves defining a *domain* that consists of nodes and links](https://oreil.ly/XyquJ), each with their own attributes and labels. Graph data modeling is often called whiteboard friendly, as it can be visually drawn on a whiteboard.

Graph data modeling involves two primary aspects: node modeling and link modeling. In node modeling, you define the different categories of nodes that can exist in the graph, such as persons, organizations, countries, or assets. Each node category is characterized by specific attributes that provide descriptive information, including category labels and additional fields for unique identification.

In link modeling, the focus shifts to defining the relationships or connections between different node categories. This involves specifying the types of links that can exist and assigning link attributes that describe the characteristics of these connections. [Figure 8-7](#ch08_figure_7_1724776834148618) provides an example of graph data modeling.

### Figure 8-7. An example graph data model

![Figure 8-7. An example graph data model](images/fden_0807.png)

Keep in mind that the graph DSM does not enforce a rigid schema, as is the case with the SQL model. New types of nodes and links can be easily added by defining their label and attributes, and existing nodes and links can be adapted to reflect new business requirements.

To enhance performance, graph data modeling may include the definition of indexes on nodes and links. These indexes are typically based on attributes associated with nodes or links.

### Technological implementations of graph databases

The graph DSM can be implemented using a variety of technological options. The simplest but least performant approach involves the use of multi-model non-native DSSs such as relational databases. In this case, nodes, links, and their attributes are defined in normalized tables, and indexes can be added to improve search performance. If you recall the section on graph data in Chapter 2, this would be similar to the *edge list* graph representation. This solution is recommended if your application doesn’t prioritize graph data processing or if you want to perform basic graph queries.

Some relational databases have ad hoc extensions that provide graph database functionalities. The best example is [Apache AGE](https://oreil.ly/jHh9D), a PostgreSQL extension developed to provide graph processing and analytics capabilities. AGE provides users with the capability to compose graph queries using a hybrid query language that integrates SQL with openCypher, an open source implementation of the Cypher graph query language originally developed by Neo4j.

Non-native graph implementations have several limitations. In particular, relational databases are built on the assumption of independence between the records, which explains their good performance when querying a set of rows. However, graph data revolves around relationships between data points. This led to the development of native graph databases designed specifically to handle such interconnected data structures.

Neo4j, created by Neo4j, Inc., is the leading native graph DSS, known for its extensive feature set that supports diverse graph-based applications. Neo4j uses a proprietary querying language called *Cypher* to query data stored in a Neo4j database. To boost performance, Neo4j’s processing engine relies on a special indexing strategy called [*index-free adjacency*](https://oreil.ly/-ZhlJ). It works by assigning each node a direct reference to its adjacent nodes, which implies that accessing relationships and associated data is as simple as a memory pointer lookup. In addition, Neo4j supports simple and composite node and link attributes indexes, constraints, and atomic transactions, as well as functions, subqueries, patterns, and clauses.26 For more advanced graph algorithms and machine learning tasks, the [Neo4j Graph Data Science library](https://oreil.ly/H7Yd1) is available.

### Note

A major challenge with graph DSSs is scalability. Solutions such as Neo4j can scale to handle billions of nodes and links, which is more than enough for the vast majority of use cases. However, sharding is not native to graph databases. Unlike relational databases, where rows are independent, graph data is interconnected, making it difficult to partition efficiently as graph density increases. Mathematically speaking, the problem of partitioning a graph dataset across a set of nodes is near impossible (NP-complete) to perform for large graphs.27 Nevertheless, several graph database technologies (e.g., TigerGraph) have made progress along this way and offer distributed graph processing capabilities.

Another implementation of graph storage systems is managed services. One example is *Amazon Neptune*, which offers a scalable, secure, and cost-efficient managed graph database. Neptune allows users to query data using the popular graph query languages Apache TinkerPop Gremlin, W3C’s SPARQL, and openCypher. Another prominent example is *TigerGraph*, which provides a rich platform for native graph data storage and analysis at scale.

### Financial use cases of graph databases

Graph databases have been applied to solve a variety of problems in the financial sector. One prominent use case is fraud detection. Many forms of financial fraud exist: credit card fraud, loan fraud, wire fraud, tax fraud, identity theft, insurance fraud, and money laundering. In simple scenarios, fraud is easy to detect with traditional tools and databases. However, in today’s environment, fraudsters use sophisticated techniques and tricks to commit their crimes and hide their actions and identities.

The best way to detect such complex patterns is by designing a framework that combines network analysis with a graph database to build a [fraud graph](https://oreil.ly/WCTUL). Such a graph records the connections between the actors, transactions, and other pertinent data to help experts capture anomalous trends in the data and create applications that can identify fraudulent activity. [Figure 8-8](#ch08_figure_8_1724776834148635) naively illustrates the concept. In this example, the real account holder is associated with a unique set of information such as address, email, phone number, SSN, etc. A fraudster, however, might use a variety of addresses, phone numbers, and other pieces of information and combine them in complex ways to hide their activities. When represented as a graph, such hidden relationships can be detected more easily. This task can be represented as an entity resolution problem where the goal is to match nodes that represent the same entity.

### Figure 8-8. Graph-based fraud detection

![Figure 8-8. Graph-based fraud detection](images/fden_0808.png)

Graph databases also find applications in financial risk analysis. For instance, financial assets can be structured hierarchically, bundled into new assets, segmented into tranches, and distributed across complex networks of ownership and transactions. This complicates the task of risk management and reduces regulatory oversight. One approach to address this challenge involves constructing a [financial assets graph](https://oreil.ly/Vp-Lk). This graph models and stores the relationships among different types of financial assets, enabling financial institutions to track their assets and account for dependencies in their pricing models. Additionally, graph databases are useful for simulating various shocks and scenarios to test the stability of correlated asset portfolios, interbank networks, and various types of systemic risks.28