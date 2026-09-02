## Indexing of relational databases

If you are going to work with relational databases, indexing is a must-have strategy. SQL databases physically organize data on disk in *data* *files,* with each row called a *record* and each column within a row called a *field*. To search for a specific record, an SQL database can perform a full scan of all data files. However, this is an expensive operation, especially when the data size gets very large. This is where indexing is needed.

An index is a specialized data structure stored separately from data files in index files. It is optimized to enable rapid search and retrieval of specific data records. Indexing is typically applied to the column(s) that you will use in your filtering statement. For example, suppose you are tasked with the creation of a bank transactions table that stores the transaction\_id, user\_id, transaction type, transaction\_time, and transaction\_amount. Your business team tells you that they want to query this transaction table by filtering on the user\_id. Without an index, a query will scan the entire transaction table, which may be extremely slow and costly. To overcome this issue, you can add an index on the user\_id column. If the business team tells you that they want instead to query user\_id for a given time interval, then consider adding a *composite* index on both the user\_id and transaction\_time columns.

Relational databases offer a variety of indexes, and you can add as many indexes as you want.17 However, it is important to keep in mind that indexes get regularly updated when you add, modify, or delete records. If such operations are quite frequent, then index updates might impact performance. Additionally, be careful how you define composite indexes. For example, if you create a composite index on columns A, B, and C, then a query that filters by B only, or C only, or B and C, is likely to not benefit from the index. Furthermore, if you create an index on a column of one type (e.g., integer) and then cast the column to another type during a query (e.g., string), then the index is likely to be useless. A recommended practice is to monitor index usage to see if it’s being utilized by the DSS.

### Technological implementations of relational databases

A large number of database technologies have been developed following the relational DSM. These include commercial solutions such as Oracle Database, Microsoft SQL Server, IBM Db2, IBM Informix, and MySQL Enterprise Edition as well as open source alternatives such as PostgreSQL, MySQL, and MariaDB.

A full account of the differences between all these technologies is beyond the scope of this book. A general criterion that I recommend following is the degree of compliance with the SQL standard. Some database technologies, such as PostgreSQL, are well-known for their high compliance with the SQL standard. Others, such as MySQL, may [exclude some aspects of the standard](https://oreil.ly/EOxBR) in return for reliability or speed, as well as include features and extensions that are not necessarily part of the standard.

The database’s technological specifications are another distinguishing criterion. One SQL database system may have a functionality that others may not have. These specifications include the following:18

* The operating system that the database system can run on (e.g., Linux, Windows, etc.)
* ACID properties
* Concurrency control and locking mechanisms
* Data size limits (e.g., max table size, max row size, etc.)
* Supported data types (e.g., varchar, integer, numeric, JSON, etc.)
* Supported constraints (e.g., foreign keys, etc.)
* Data connectors
* Security, roles, access control, and encryption
* Data replication and partitioning
* Backup and recovery
* Support for materialized views
* Supported index types (other than basic B-tree indexes)

An essential factor that might impact the choice of your relational database technology is scalability. Traditionally, relational databases have supported vertical scaling, where a small machine is replaced with a larger one with more RAM, CPU, and storage. This strategy has several advantages, such as simplicity and data consistency and integrity. However, it also has some drawbacks. First, it creates a single point of failure as it involves a single machine; second, it can easily hit capacity and load balancing limits if the workload grows quickly or unexpectedly; third, there are physical limitations in terms of how much CPU and RAM a single machine can have. This is where horizontal scaling comes into play.

In horizontal scaling, the database system relies on a system of connected machines/nodes to distribute the load. If the workload grows, additional nodes can be added to handle the increased demand. A typical approach for achieving SQL horizontal scaling is through *read replicas*, which are additional copies of the primary database that are regularly synchronized with it, either synchronously or asynchronously. These replicas are often dedicated to handling read operations (such as SELECT queries), while the primary database continues to handle write operations (such as INSERT, UPDATE, DELETE). It is also possible for some systems to have read/write replicas.

Another horizontal scaling strategy is [*sharding*](https://oreil.ly/twWdt), which involves partitioning the database into chunks (shards) based on a shard key (e.g., date range) and distributing them across multiple machines. This way, the traffic load gets distributed among the shards. Importantly, sharding-based horizontal scalability can be difficult to manage.19 For example, a significant amount of maintenance effort may be needed to ensure the database’s integrity, involving operations such as data resharding, rebalancing, and partitioning. Furthermore, it may require incorporating complicated logic into your application’s read/write methods to route requests to the relevant shard.

To overcome this issue, a new generation of horizontally scalable SQL databases emerged: *distributed SQL databases*. These databases offer native built-in scalability without the need to manually manage shards. Examples include Google Spanner, YugabyteDB, and CockroachDB. If your scalability needs are remarkably large, then such databases may be the ideal solution. For example, Deutsche Bank leveraged Google Spanner to achieve [one of the biggest IT migrations](https://oreil.ly/8UakC) in the history of the European banking industry, involving 19 million Postbank (Deutsche Bank’s retail branch) product contracts alongside the data of 12 million customers.

### Financial use cases of relational databases

Relational databases are extensively used within the financial sector. This can be explained by a number of factors. First, a significant part of financial data is tabular time series and panel data, which is perfectly suited for the relational DSM.

Second, financial professionals perform a lot of analysis related to business intelligence, forecasting, pricing, risk management, and modeling. Relational databases are an ideal solution for these tasks due to their powerful and intuitive analytical querying capabilities.

Third, relational databases offer a lot of the reliability features that most financial applications require, such as data consistency, integrity, and a transactional guarantee. For example, financial payment applications require transactions to be idempotent, meaning if they are executed multiple times, the outcome should be consistent. If you purchase an item for $100 and the application processes your payment twice, idempotency ensures your account is debited only once for $100. SQL databases can achieve idempotency through mechanisms like uniqueness constraints and idempotency tokens. For instance, if each payment is assigned a unique idempotency token and the column storing these tokens has a uniqueness constraint, any attempt to insert the same payment twice will be rejected by the database due to the violation of the uniqueness constraint.

# Case Study: Payment Processing Applications with CockroachDB

Payments are one of the most essential operations in financial markets. A large number of players are involved in payment processing, including SaaS applications, online shops, ecommerce websites, retailers, payment gateways, card networks, payment processors, and payment service providers. Crucially, designing a payment system can be quite challenging, as it needs to ensure the following:

* Scalability (imagine how easily the volume of payments can increase)
* Data durability (people won’t like it if they can’t find their historical payment records)
* High availability and zero downtime (it’s not a pleasant experience if you can’t pay)
* Data consistency and correctness (people won’t tolerate mistakes with their money)

How do you build a payment system that meets all the above requirements? First, let’s try to understand how payments are processed. According to [Stripe](https://oreil.ly/_N9-W), a typical card payment transaction involves the following steps:

1. The customer initiates a payment by providing their payment details (e.g., credit card) at the business payment channel (e.g., online shop).
2. A payment gateway receives the transmitted information, encrypts it, and passes it to the payment processor.
3. The payment processor forwards the information to the acquiring bank (the online shop’s bank), which in turn forwards the information to the issuing bank (the customer bank) through the relevant card network (e.g., Visa or Mastercard).
4. The issuing bank verifies the request and responds with an approval or rejection message sent back to the payment processor via the same path (card network and acquiring bank).
5. The payment processor communicates the transaction outcome to the business, which proceeds to conclude the purchase or inform the customer of any issue.
6. If the transaction is concluded, a clearing and settlement process takes place in which the transaction amount is transferred from the issuing bank into the acquiring bank, which in turn deposits the funds into the business’s account.

Importantly, when data passes through this chain of information exchange, some of the involved entities store a portion of the payment data for reasons such as transaction reviewing, reporting, reconciliation, and fraud detection. Due to the mission-critical nature of payments, a highly available, scalable, and reliable database system is required. This is where distributed SQL databases can excel.

A prominent solution in this market is CockroachDB, a cloud native, distributed database based on standard SQL and developed by [Cockroach Labs](https://oreil.ly/Xnkoe). CockroachDB offers a number of valuable features for mission-critical applications:

* Simple horizontal scalability where users can add additional nodes as needed. Interestingly, even though it’s a distributed system, CockroachDB works as a single logical database, enabling data access from any node, regardless of its location.
* Support for transaction-heavy workloads with [distributed atomic transactions](https://oreil.ly/7XDlb).
* High availability with no downtime, achieved via a [consensus algorithm](https://oreil.ly/6Xw8O).
* Multiactive availability (each node can serve both read and write requests).
* Support for multiregion and multi-cloud (ideal for compliance that restricts data residency to a specific region).

To give an example of the application of CockroachDB in the financial sector, let’s take the case of [Shipt](https://oreil.ly/vJWLE), an American delivery service owned by Target Corporation. As an online ecommerce company, Shipt payment services are core to its business model. The Shipt team was tasked with the creation of a distributed database system that meets the requirements of a reliable payment system, in line with what we discussed earlier in this section. In particular, Shipt wanted a multiregion payment service that could ensure [correctness](https://oreil.ly/_DZDm) throughout the entire payment cycle.

By leveraging CockroachDB, the Shipt engineering team managed to build a reliable, correct, cloud native, multiregion, and highly available payment data management system. Regional replication allowed Shipt to achieve lower transaction latency. Furthermore, to ensure idempotency throughout the payment lifecycle, Shipt relied on idempotency [tokens](https://oreil.ly/WQpnt). Overall, by building its system on top of CockroachDB, Shipt can now support its business growth across different regions and markets with a resilient and scalable payment architecture.

## The Document Model

A highly reputable DSM is the document model, which stores information in a document format such as JSON or XML. This section will specifically focus on JSON-based DSMs, which are the predominant choice in the industry. A document looks like the following:

```
{
     "document_id": 1,
     "legal_name": "Microsoft Corporation",
     "type": "public company",
     "isin": "US5949181045",
     "symbol": "MSFT",
     "sector": "Information technology",
     "products": [
            "Software development",
            "Computer hardware",
            "Social networking",
            "Cloud computing",
            "Video games"
     ]
}
```

A DSS designed to store and query documents is called a document-oriented database, or simply a document database.

### Why document databases?

Document databases are extensively used for all kinds of purposes, powering some of the world’s largest applications. Among their most desired features are the following:

Schema flexibility:   A document database can store any document, regardless of its content structure. In other words, document databases do not enforce schemas natively, unlike SQL databases. This allows businesses to quickly develop an application and easily change its logic. You can add, change, or rename the document fields based on your business requirements. Make sure, however, to be aware of the potential side effects of such flexibility; if not managed properly, it might impact data integrity and consistency. At some point, you might even want to enforce a schema in the documents. This is often achieved via a schema validation mechanism implemented on the application side.

Document modeling:   Document formats such as JSON are quite familiar and might be easier to work with. Moreover, unlike relational or other types of data storage formats, documents map directly to objects such as hash tables or classes in most popular programming languages, without the need to add an *Object Relational Mapping* (ORM) layer to your application.

Horizontal scalability:   Document databases are distributed by design, which means that they can scale horizontally. This makes them an ideal choice for modern data-intensive applications. Moreover, being distributed, document databases provide resiliency and availability through multinode data replication.

ACID (atomic) transactions:   Document databases support ACID transactions, at least for single-document transactions, and in many cases for multidocument transactions as well. Crucially, it is often a less strict version of ACID that focuses on achieving data consistency via atomicity and an isolation guarantee (e.g., using snapshot isolation).

Performance:   Document databases are quite performant when it comes to high-volume data reads/writes. This can be partly explained by the distributed architecture of document databases, which splits the load among the many nodes that make up the system. Furthermore, unlike traditional SQL databases, document databases do not necessarily enforce schema checks, standards, constraints, and ACID properties, which in turn increases query performance. Keep in mind that this is not a shortcoming, but rather a design choice.

### Data modeling with document databases

In document databases, data modeling must be seen from a somewhat different viewpoint than that of the SQL DSM. Technically speaking, document databases are not designed for performing complex queries and table joins as is customary with SQL databases. This means that the range of queries that you can perform in a document database will be constrained by your data model. For this reason, the first step in document data modeling needs to be a business discussion to think and define in advance the queries and filters that users will want to perform. This is often called *query-driven data modeling*. User-defined queries should serve as the foundation for the subsequent data modeling stages. In this section, I will discuss three document data modeling techniques: document and collection structure, denormalization, and indexing.

## Document and collection structure

The central concept of a document database is the *document*. You can think of documents as the equivalent of rows in the relational model. A document stores data objects as a set of key-value pairs. It can store many types of data, including strings, integers, dates, Booleans, arrays, and even subdocuments. Documents are then organized in *collections*, which are the equivalent of tables in the relational model.

Unlike SQL databases, there are no standardized rules for modeling a document database. In this case, the modeling process is mostly driven by business needs. As far as collections are concerned, the main thing to consider is that document databases do not allow for performing joins; therefore, collections should be modeled in a way that minimizes inter-collection relationships and at the same time maximizes intra-collection data cohesion. For example, a separate collection may be created for each business entity, such as users, products, transactions, subscriptions, reference data, prices, and quotes.

### Note

Managing schema changes in a NoSQL database can be challenging, especially in environments where the schema is not strictly enforced and evolves over time. A number of good practices can be adopted to mitigate this issue. One such practice is schema versioning, which can be implemented by defining and storing your document schema in a separate location, and adding a schema\_version field to your documents. Each version of the schema should have a unique identifier. Furthermore, you can implement schema validation on the application side to check if your document matches the referenced schema. Make sure you document and communicate schema changes clearly within the team.

## Denormalization

To ensure intra-collection cohesion, all related data needs to be stored in the same document. This strategy is often called *denormalization*, as it involves making redundant copies of the data in multiple collections to increase performance and avoid data joins. As an alternative, it is possible to use *references* that link documents across collections. You can think of references as a soft version of foreign keys in SQL databases. For example, a user ID field in the *transactions* collection can be used to find a related document in the *contacts* collection.

## Indexing of document databases

Document databases are designed for large amounts of data. As such, indexes are often used to improve query performance. An index stores a small portion of the collection data in an easy-to-traverse data structure. Without appropriate indexing, a document database will have to scan the entire collection when searching for a specific document.

The two primary types of indexes often supported by document databases are *single-field* indexes and *composite* indexes. Deciding which and how many indexes to create depends on your queries and it is crucial for improving the performance of your application. If a large number of your queries filter by a single field only, then it’s better to create a single-field index for each of these fields. If you also have queries that repeatedly filter by multiple fields, then you can create a composite index on those fields. Other types of advanced document indexes exist. For example, multikey indexes are used to index array fields, while text indexes are used to support text search queries on string content.20

Importantly, there are a few factors to consider while indexing a document database. First, although indexes improve read performance, they will negatively impact write operations as they must also update the index. This is especially the case for applications with a high write-to-read ratio. Second, several document databases impose a limit on the number of indexes that a collection can have. If you run out of indexes, then you might not be able to meet your business or performance requirements anymore. Third, indexing might become more challenging if you have a highly nested or complex document structure. For this reason, consider making your documents as flat as possible to achieve optimal indexing results.

### Technological implementations of document databases

There are a large number of data storage technologies that implement and support the document model. The most prominent examples include open source options such as MongoDB and Apache CouchDB, as well as managed commercial solutions such as Amazon DynamoDB, Azure Cosmos DB, and Google Cloud Firestore. Cloud-based solutions such as DynamoDB, Google Firestore, and Azure Cosmos DB are commonly preferred as they offer tight integration with other cloud services as well as reduced infrastructure and security overheads.

Moreover, a few specialized document-oriented data storage options are available. The most prominent example is *Elasticsearch*, which can be described as a distributed search and analytics engine. It is built on the Apache Lucene search software, which implements a well-known technique called inverted indexing. Elasticsearch is often used as a secondary DSS, where data from one or more primary DSSs is regularly pulled and indexed to allow easy and fast searching.

### Financial use cases of document databases

Document databases have received considerable attention within the financial industry. This is particularly the case for financial applications that require scalability, latency, availability, schema flexibility, and integration capabilities, which are characteristic of document databases.

Let’s take MongoDB, for example. Financial institutions have leveraged MongoDB for various business applications. A common example is the [development of payment systems](https://oreil.ly/K5fSa). MongoDB’s flexible data schema enables payment applications to accept and enrich any payment data structure and type. In addition, MongoDB may offer the necessary scalability and availability features that are essential to payment systems. Moreover, MongoDB’s API-based data management is an ideal fit for the payment business, which relies significantly on APIs.

# Case Study: Wells Fargo’s Next-Generation Card Payments System with MongoDB

Wells Fargo is a well-known financial services corporation with a remarkable global reach. To modernize its credit card payment system, Wells Fargo launched the *Cards 2.0* initiative. Based on an industry [case study](https://oreil.ly/igLCJ), the main goals of the initiative were the following:

* Ensuring a seamless multichannel experience for credit card customers (branch, mobile, digital, etc.)
* Reusable and scalable data APIs to enable the quick rollout of changes across multiple channels
* Reduced dependency on third-party card processors

To achieve success with Cards 2.0, Wells Fargo had to reduce its reliance on mainframe infrastructures. The reason, according to the case study, is that “while mainframes hold critical System of Record (SOR) data, they often bring technical debt, dependencies, and are increasingly costly to manage—not least because there’s a shortage of people with the right skills to maintain them.”

While the bank is responsible for issuing the cards, the gateway that tracks all the transactions is the Fiserv mainframe system. Relying on data ingestion mechanisms based on a mainframe was not ideal for modern multichannel applications. To solve this problem, the engineering team at Wells Fargo designed a modern data infrastructure powered by MongoDB. The new solution included batch (Apache Spark) and real-time (Apache Kafka) systems that listen and pull the data from the mainframe and upload it to MongoDB. The resulting MongoDB-based DSS was an Operational Data Store (ODS) that could serve data to many business channels.

The Wells Fargo team didn’t expose MongoDB collections directly to data consumers. Instead, data APIs were designed to serve various types of data (e.g., accounts, transactions, etc.). Such data APIs are then imported and used in the various microservices. Using MongoDB, Wells Fargo was able to handle over 20+ terabytes of daily data and move from a monolith architecture to a modular architecture of more than 80 microservices.

Another noteworthy example of a reliable and scalable document database technology for financial services is AWS DynamoDB. DynamoDB is a key-value and document-oriented database designed for high speed, throughput, availability, scalability, and millisecond latency. To illustrate its capabilities, on 2022 Amazon Prime Day, Amazon DynamoDB reliably [handled 105.2 million requests per second](https://oreil.ly/gntiZ) across trillions of API calls with single-digit millisecond performance. In addition, DynamoDB can be natively integrated with AWS Lambda to execute a data processing logic each time a DynamoDB table is updated. For example, the Amazon finance technologies (FinTech) payment transmission team, which supports and manages products for the accounts payable (AP) team, [implemented a similar architecture](https://oreil.ly/5nmM-) to ensure the scalability and timely processing of remittances at Amazon.

## The Time Series Model

In Chapter 2, we talked about time series data and illustrated its main characteristics. In essence, a time series is a sequence of measurements or observations of one or more variables tracked at increments in time. Examples include temperature, resource consumption by a computer, events, clicks, and stock prices.

Financial time series data such as stock prices are now generated in large volumes and velocities and are widely employed to analyze temporal market dynamics. This includes the analysis of historical trends, averages, variances, anomalies, correlations, stationarity, and cycles.

Moreover, as financial time series data has increased in volume, variety, and velocity, its range of application has significantly expanded. Time series analysis is now integral to financial analysis and forecasting and can be used in predicting stock prices, market risks, interest rates, foreign exchange fluctuations, and many more.

As a result, demand has emerged for a new type of a DSM to enable efficient storing, manipulating, and querying of time series data. I shall refer to this model as the *time series DSM*. A notable increase in the popularity of time series databases has been [observed in recent years](https://oreil.ly/_5sY0). To understand why, the next section will highlight the key characteristics that distinguish time series databases.

### Why time series databases?

A time series database is a specialized type of DSS designed specifically to implement the time series DSM. Time series databases offer several advantages, such as the following:

* A specialized engine designed for storing and processing time series data, providing substantial performance enhancements tailored for applications that handle large volumes of time series data, such as trading systems.
* Built-in functionalities to perform efficient time-based aggregations, such as temporal grouping of data (yearly, monthly, daily,..) and temporal transformations (e.g., simple moving average, exponential moving average, cumulative sum, percentile).
* Fast queries enabled through optimized time series indiexs and in-memory caching.
* Simple data model based on the time association of entities.
* Data immutability: time series databases are often designed for immutability and append-only behavior—i.e., once recorded, data is rarely updated.
* Efficient data lifecycle management by keeping recent data in memory, and deleting or compressing old data for efficient storage.

Keep in mind that the time series DSM is a specialized model; therefore, it should be considered only when your business and application requirements are centered around the efficient storage and processing of time series data. If the time series dimension of your application is just one of many aspects, then you might want to go for a more general-purpose DSM such as the SQL or document model.

### Data modeling with time series

Data modeling in the time series DSM is as simple as the structure of time series data: a timestamp and associated data. The equivalent of a table in a time series database is often called a *measurement*. A measurement is a container of at least three main elements: time, fields, and metadata. [Table 8-1](#ch08_table_1_1724776834176432) illustrates an example.

Table 8-1. A measurement in a time series database

Time Price Ticker Exchange 2019-02-18T16:12:01Z 15.45 ABC NYSE 2019-02-18T16:13:01Z 15.41 ABC NYSE 2019-02-18T16:20:01Z 15.44 ABC NYSE 2019-03-06T17:33:20Z 345.45 ZYK NYSE 2019-03-06T17:33:25Z 345.47 ZYK NYSE

In [Table 8-1](#ch08_table_1_1724776834176432), the first column is time, which in a time series database must always be present. The next column, price, is a field. Field values represent the actual data in a measurement, and each measurement should have at least one field. In our example, we are observing the price of stocks over time. The final two columns, ticker and exchange, are referred to as metadata or tags. Tags are optional, although they are quite useful. Most time series databases construct indexes based on tags rather than time or field columns. A single row in a measurement is called a *point*. A set of points that share the same set of tag values is called a *series*. For example, the first three rows in the measurement shown in [Table 8-1](#ch08_table_1_1724776834176432) form a series, since they hold data related to the price of the ticker ABC on the NYSE exchange.