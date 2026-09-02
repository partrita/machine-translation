### Technological implementations of data lakes

As a DSM, a data lake is an abstract idea that conceptualizes a centralized repository for storing raw data, independent of any specific technology. If a data lake aligns with your use case, the next step would involve selecting a technology to implement it. The classical solution has traditionally been the [*Hadoop Distributed File System* (HDFS)](https://oreil.ly/HMySV). HDFS is a part of the Hadoop ecosystem, which is extensively used to build big data applications. It is an open source, distributed, scalable, and fault-tolerant file storage solution for working with large amounts of data. It runs on commodity servers (mostly on premises), thus making it a cost-effective solution. It is written in Java and has several configuration options that can match various business needs. In addition to HDFS, other prominent open source data lake solutions include MooseFS, Ceph, and GlusterFS.

With the emergence of the cloud, a major preference shift occurred toward building data lakes using managed cloud storage solutions. Examples include AWS’s Simple Storage Service (S3), Azure Blob Storage, Google Cloud Storage, and DigitalOcean Spaces. Cloud-based data lakes are considerably easier to build and use; they scale seamlessly and require minimal configuration and maintenance. You can even create a basic cloud data lake in less than a minute if you already have an account!

Nevertheless, don’t get overexcited with the simplicity of cloud storage solutions. When designing an enterprise-wide data lake solution, quite a few challenges and factors need to be considered to avoid building a monster. Two things worth discussing in this regard are data modeling and data governance, which I will cover in more detail in the next two sections.

### Data modeling with data lakes

When designing data lakes, data modeling is rarely a major discussion point. The reason is that data lakes are not assumed to enforce a specific schema or structure on the ingested data. Even though this might be a valid point, data lakes can still have their own data models and architecture. To illustrate how data modeling works for data lakes, let’s take a cloud-based data lake solution such as AWS S3 as our desired technological implementation.

To start with data lake data modeling, bucket architecture is the first thing to consider. Buckets are the main containers of objects stored in S3. Think of buckets as the logical data model for your data lake, which are distinguished based on your business requirements and can be assigned user permissions independently of the other buckets. For example, one bucket may be dedicated to storing log data, another for financial vendor data, and a third for analytics data. Alternatively, it is common to organize buckets into [zones](https://oreil.ly/xzDhh), such as landing zones for raw files, staging zones for enriched files, business zones for analytics and research data, and trusted zones for anonymized and analysis-ready data.13

### Tip

There is no single recipe for how and how many buckets to create, but I can recommend keeping in mind architecture simplicity: don’t create too many buckets such that you won’t know which data is where, and don’t create one huge bucket to store all kinds of data.

The second element of data lake modeling is a folder structure that organizes data items based on their categories and relationships. The most common folder structure is the tree-like hierarchical structure where parent folders contain subfolders, which in turn may contain other subfolders and so on. A simplistic zone-based folder structure might look like this:

Landing zone:   Stores files at the second level, e.g., */landing\_bucket/year/month/day/hour/minute/second*

Staging zone:   Cleans and aggregates the data at the daily level, e.g., */staging\_bucket/year/month/day*

Business zone:   Splits daily data based on business areas, e.g., */business\_bucket/business\_area/year/month/day*

In the landing zone, raw files have schema on read rather than schema on write. This is because they are stored as they arrive without any modification. As data gets transformed in the staging and business zones, it is a good practice to implement schema on write, meaning that you enforce data schema into the files. If you want to apply anonymization to the data, you may want to create a trusted zone where you store data that has been anonymized for safe use and analysis.

A good practice when organizing your data lake folder structure is to avoid having different file formats within the same folder. For example, assume that the ingestion layer loads files in gzip, CSV, and TXT formats. To model this properly, consider a landing zone structure like the following:

* gzip files: */landing\_bucket/gzip/year/month/day/hour/minute/second*
* CSV files: */landing\_bucket/csv/year/month/day/hour/minute/second*
* TXT files: */landing\_bucket/txt/year/month/day/hour/minute/second*

By design, a data lake may accommodate any type of data from any source. All you have to do is specify a bucket name and drop data in it. However, this simplicity can potentially lead to several issues. Think of the *Downloads* folder on your PC; if you are like me, then it is simply a big dump of files of all types and formats; you don’t know what’s in there, whether it is in the right place, and how to navigate and search for files. Similarly, without the right controls in place, data lakes can easily turn into *data swamps*: an out-of-control place for dumping any data from any source without any checks or validation rules. To avoid this issue, you need to implement a data governance layer on top of a data lake. Let’s discuss this topic in more detail.

### Data governance

Creating and using a data lake might sound very easy: (1) log in to AWS, (2) select S3, (3) create a bucket, (4) drop files there! This works, and I did it many times. However, architecting a reliable and scalable enterprise-wide data lake is a much more challenging task than this. Large data lakes, in particular, are likely to pose significant issues to users, especially when it comes to understanding things like the following:

* Metadata (information about the data)
* Sources and movements of the data
* Transformations and changes applied to the data
* The architecture of the data (buckets, folders, formats, etc.)
* The level of data quality, consistency, and integrity
* Data access and retrieval methods, which are less intuitive than just using SQL

To address these issues, it is recommended to implement a data governance layer on top of the data lake. Common considerations to keep in mind include the following:

Privacy:   Data coming from various sources may include sensitive user information, such as personally identifiable information (PII). Therefore, the data lake should be designed to anonymize and store this data in compliance with predefined privacy rules. For instance, you can separate buckets that store sensitive data from those that store anonymized data.

Security:   Data lakes must be protected against malicious attacks, data loss, and unauthorized access. This is especially important given the extensive use of cloud-based data lakes, which are vulnerable to the risks associated with cloud misconfiguration, i.e., the improper or incorrect setup of cloud resources, services, or settings. Policies to achieve this include encrypting data both at rest and in transit, implementing access controls to specify who can read, upload, and delete files, and establishing data retention rules, such as security locks, to ensure that archived data is never deleted.

Quality controls:   Data must be checked for quality issues as it gets ingested into the data lake. Note, however, that quality controls may not be needed for all types of data. For instance, while log data generally does not require quality checks, business and financial data do benefit from them.

Data cataloging:   A data catalog is a valuable tool that provides users of a data lake with functionalities to search for data, metadata, versions, ingestion history, and other attributes associated with the data stored within the data lake.

Importantly, there is no one-size-fits-all approach to implementing a data governance layer on top of a data lake. I suggest beginning with the four elements previously mentioned (privacy, security, quality control, and data cataloging). Keep in mind that for complex data lakes, data governance might be a substantial investment. Some cloud services, such as AWS Lake Formation*,* provide data lake solutions that include built-in data governance capabilities.

Continuous technological advancements are consistently enhancing the reliability of data lakes. For example, the *data lakehouse* model was created to introduce more structure into data lakes. The main idea of a data lakehouse is to create an integrated data architecture that combines a data lake, data warehouse (covered later in this chapter), and related analytics and processing services.

For example, using AWS, you can build an architecture where you upload and store raw CSV files in an S3 bucket (data lake) and query them with SQL queries using services such as Amazon Athena or Amazon Redshift Spectrum. Another example is Snowflake, which allows users to interact with data stored in a data lake of choice using the Snowflake compute layer. A recommended approach to achieve this is by storing the data in Apache [Iceberg tables](https://oreil.ly/mT5RP) that use the Apache Parquet format. Apache Iceberg is an open source table format for massive analytic datasets, supporting features such as ACID transactions, schema evolution, partitioning, and table snapshots. Similarly, technologies such as [Apache Hudi](https://oreil.ly/jdFMy) were introduced to bring database and data warehouse capabilities such as ACID transactions and record-level data updates/deletes to data lakes.

### Financial use cases of data lakes

Data lakes have [attracted significant attention within the financial industry](https://oreil.ly/FmW_g). Many financial institutions are increasingly investing in building their own data lakes, often leveraging managed cloud storage solutions.

Several reasons can explain the financial sector’s excitement for data lakes. An important factor is cloud migration. As many financial institutions are moving to the cloud, data lake solutions such as AWS S3 appear to be particularly appealing because they are simple to set up and can store any type or size of data.

Second, financial institutions process a large amount of unstructured data, such as reports, prospectuses, client files, news data, logs, and more. Data lakes offer an efficient and reliable solution for storing, sharing, and archiving such data.

The third factor is data aggregation, which is both a regulatory requirement and an enabler of innovation. By consolidating data in one location, financial institutions can quickly respond to regulatory inquiries that demand aggregated information, such as total risk exposure. Moreover, emerging trends in data-driven product development and analytics require data from diverse sources, often scattered across decentralized silos within financial institutions. Data lakes enable these institutions to seamlessly consolidate and aggregate data from various sources and silos into a centralized, accessible, and scalable repository.

Fourth is compliance. Financial institutions have a lot of compliance requirements that relate to data privacy, security, retention, and protection. Data lakes may offer a number of desired compliance-related features. For example, AWS S3 [offers *Write-Once-Read-Many* (WORM) storage features](https://oreil.ly/abujc) such as S3 Glacier Vaults and S3 Object Lock to ensure the integrity of archived data in accordance with [US SEC and FINRA rules](https://oreil.ly/DadEH). A number of features are also available to ensure security. For example, S3 provides the *Block Public Access* feature, which simply blocks all public access to S3 buckets. In this case, financial institutions deploy their S3 data lake within a VPC and enable access through [VPC endpoints for Amazon](https://oreil.ly/Iamsb).

# Case Study: NASDAQ Data Lakehouse with AWS S3 and Redshift Spectrum

NASDAQ is a multinational financial services firm operating several financial market platforms worldwide, particularly the NASDAQ Stock Exchange. NASDAQ manages the matching of buy and sell operations on a massive scale and at a rapid speed while providing data-feeding services for its prices and quotes. As a result, a large number of daily records are generated, including orders, quotes, trades, and cancellations. By 2020, NASDAQ was processing around 70,000 records on a daily basis. These records need to be loaded for reporting and billing purposes before the market opens the following day.

To support its large-scale data needs, NASDAQ [invested in a data lake solution leveraging AWS S3](https://oreil.ly/fYya9). This strategic decision enabled NASDAQ to decouple the compute layer from the storage layer, allowing independent scaling of each component. Using S3, NASDAQ gained the capability to manage numerous concurrent read and write operations on large datasets seamlessly, without encountering contention issues.

Using AWS Identity and Access Management (AWS IAM), NASDAQ established a comprehensive access control policy for data stored on S3. Additionally, NASDAQ took advantage of the lower costs of archival storage offered through Amazon S3 Glacier. Moreover, NASDAQ leveraged the [Amazon S3 Object Lock feature](https://oreil.ly/fBX6P) to protect objects from deletion or modification, ensuring compliance.

For the compute layer, NASDAQ chose [Amazon Redshift Spectrum](https://oreil.ly/IpoxH), a service that allows users to perform SQL queries on data stored in Amazon S3 buckets. The resulting architecture is a data lakehouse that combines a data lake (S3) with a data warehouse (Redshift Spectrum), each scalable independently to support various levels of storage and computing.

## The Relational Model

The popular and highly trusted DSSs are built on the relational DSM, which organizes data in rows and columns, forming a table or relation. These tables can be related to each other through a common attribute (column), hence the term “relational.” [Figure 8-1](#ch08_figure_1_1724776834148484) illustrates the concept.

### Figure 8-1. Components of the relational DSM

A collection of tables, along with other objects such as views, indexes, stored procedures, and functions, within a relational model is often referred to as a *schema*. Multiple schemas can coexist within the same *database*. For this reason, it is common to refer to a relational DSS as a *relational database management system* (RDMS) or relational database.

Interaction with a relational database happens through a *declarative* language known as *Structured Query Language*, or more commonly SQL. For this reason, relational databases are also commonly called SQL databases.

The relational DSM foundations were laid out by IBM’s expert Edgar Codd in the 1970s. After extensive research on the relational model, Codd [proposed a list of 12 rules](https://oreil.ly/Z_l3f) that must be observed to develop a true relational database.

### Why relational databases?

Relational databases are widely trusted and heavily relied upon by financial market participants, often serving as the default choice for data storage. Let’s explore the reasons behind this preference.

## SQL standards

The origins of the SQL language go back to 1974 when Donald Chamberlin and Raymond Boyce from IBM released the essay “SEQUEL: A Structured English Query Language.” Chamberlin and Boyce relied on Codd’s framework to develop an intuitive and user-friendly language to interface with relational databases.14

As the language gained wide popularity and a strong reputation among market participants, the *American National Standards Institute* (ANSI) intervened in 1986 to develop and promote a standard for SQL. The ANSI Database Technical Committee (ANSI X3H2) within the Accredited Standards Committee (ASC) X3 developed the first SQL standard, known as ANSI X3.135-1986. In 1987, the ISO started developing an international version of SQL standards, further solidifying SQL’s presence on the global stage. Since then, the standard has been defined and revised under [ISO/IEC 9075](https://oreil.ly/duMsM). What ISO/IEC 9075 offers is a set of features and requirements that need to be implemented in order for a database to become SQL compliant. [Figure 8-2](#ch08_figure_2_1724776834148518) illustrates the historical evolution of SQL standards.

Thanks to ISO/IEC 9075, the SQL language has evolved along a path of continuous improvement, resulting in a rich array of features that continue to make SQL a favored choice among engineers and financial markets to this day. One thing to keep in mind is that SQL standards are advisory, not mandatory technical specifications. It is quite possible to create an SQL database system that implements only a subset of SQL standards.

### Figure 8-2. Overview of SQL standards

![Figure 8-2. Overview of SQL standards](images/fden_0802.png)

## ACID transactions

By design, relational databases offer the strongest ACID transactional guarantee among all DSSs.

Atomicity is guaranteed by executing each statement or block of statements within a single transaction. A transaction either succeeds completely or is aborted without leaving partial or incomplete results. This is possible thanks to a transaction log mechanism known as *Write-Ahead-Logging* (WAL). Before a transaction is executed, it is logged into the WAL log. The database system may utilize the WAL to roll back changes and return the database to its initial state if a transaction fails or is interrupted. Otherwise, the transaction is marked as committed.

Consistency is primarily achieved via the use of constraints such as uniqueness, non-null values, primary key, foreign keys, and checks. Foreign key constraints are a distinguished feature in SQL used to ensure [*referential integrity*](https://oreil.ly/ebw9S). This integrity ensures that references are valid, i.e., if the presence of one value in table A requires the presence of a specific referenced value in table B, then the value in table B must exist. For example, within a customer order table, a foreign key constraint would prevent recording an order for a product referenced from another table (such as the products table) if that product does not exist in the referenced products table.

Consistency is also guaranteed via concurrency control mechanisms that handle the concurrent execution of transactions. Among the most popular concurrency control mechanisms is *Multi-Version Concurrency Control* (MVCC), a snapshot-based mechanism that allows each transaction to see a snapshot of the data (data version) at the time of the transaction initiation, regardless of what changes take place later. This way, transactions are protected against data inconsistencies that might emerge from the actions of other concurrent transactions.

Isolation is guaranteed via mechanisms such as locking, snapshot isolation (e.g., MVCC), and isolation levels. Database locks are a mechanism that allows a given transaction to place a flag on a database object (e.g., table or row) to prevent others from concurrently performing specific actions on the same object. Locking is termed *implicit* when performed automatically by the database and *explicit* when intentionally initiated by the user. Furthermore, locking is called *pessimistic* if the lock is placed while changing a DB object and *optimistic* if placed only when the changes are being committed to the DB.

### Warning

Explicit locking may be complex and may affect your application’s reliability. Key concerns in this area include lock contention, suspension, timeouts, and deadlocks. Deadlocks, where two transactions are waiting on one another to release locks, are particularly common. Additionally, locks differ in terms of the set of lock modes with which they conflict; therefore, make sure you understand the side effects of using a specific lock.

*Isolation levels* are used to control the visibility of concurrent transactions. The SQL standard defines four isolation levels: *Read Uncommitted*, *Read Committed*, *Repeatable Read*, and *Serializable*. These levels are defined in terms of four phenomena: *dirty read*, *nonrepeatable read*, *phantom read*, and *serialization anomaly*. As this topic is a bit long to illustrate in detail, I refer the reader to the excellent documentation page of PostgreSQL on [transaction isolation](https://oreil.ly/-jRyE).

Finally, durability is ensured via mechanisms such as WAL. By first logging transaction steps into the WAL log, there is a guarantee that once a transaction is committed, its results will not be lost even in the event of subsequent failures.

## Analytical querying

One of the strongest arguments in favor of using SQL databases is their advanced querying capabilities. This includes table joins, aggregations, window functions, common table expressions, subqueries, stored procedures, functions, views, and many more. One major advantage of such querying features is the flexibility they provide in terms of data modeling. This is because you don’t need to guess all your queries in advance before designing and creating an SQL database. Other types of DSM, such as the document model, require queries to be defined in advance in order to obtain good performance.

## Schema enforcement

Relational databases require and enforce a data schema, which defines table structure, column names, data types, constraints, and more. This is an essential feature if data needs to adhere to a predefined structure. Schema enforcement improves data quality and integrity by ensuring consistency in how data is stored and accessed.

Keep in mind, however, that in many real-world applications, schemas can change quite often due to changing business needs. This is an important factor to consider when assessing the suitability of the relational model to your business problem.

With later revisions of the SQL standard, new data types such as [JSON](https://oreil.ly/bQ8sT) were added, which introduced some sort of schema flexibility into SQL databases. By creating a column of type JSON, an SQL database allows users to store data with variable structures, just like a JSON file.

### Data modeling with relational databases

Data modeling is predominantly used in SQL databases. This is because of their standardized design principles and features, the flexibility they offer in terms of table organization, and the business and technical intuitiveness of the relational DSM.

As we discussed earlier in this chapter, data modeling is a technique used to define and assess the data requirements necessary to support various business operations within the corresponding data infrastructure of financial institutions. That said, data modeling needs to always start with a business discussion (conceptual phase) that you later translate into an actual database design (logical and physical phases). We can discuss a lot about how to define and fulfill each of these three phases. However, to keep things simple and within scope, I will limit my treatment of SQL data modeling to the following techniques: normalization, constraints, and indexing. For each technique, I will briefly illustrate a few business use cases.

## Normalization

Normalization is the most popular SQL data modeling technique. It defines a table structure following several so-called *normal forms*. Normalization ensures that the following conditions are met:

* Data redundancy and repetition are minimized
* Data is organized in small tables instead of one large table
* Tables have well-defined relationships and references
* Updating or adding data will be done in as few places as possible
* Ability to add and remove data without altering or refactoring the tables
* Tables are neutral to queries (i.e., your table design is not constrained by the queries you want to perform)
* Tables offer clear and informative data for business users
* You avoid the problem of insertion, update, and delete anomalies15

There are several types of normal forms; however, most databases are normalized using the following three forms:16

First normal form (1NF):   This form ensures that all columns are single valued. A field may not contain composite values or nested records. If such nested values exist, they should be expanded to multiple rows. An example is illustrated in [Figure 8-3](#ch08_figure_3_1724776834148542). The table on the left is not in 1NF as it contains a multivalued column (transaction\_id), while the table on the right is in 1NF as it contains no multivalued records.

    ###### Figure 8-3. First normal form conversion

![Figure 8-3. First normal form conversion](images/fden_0803.png)

Second normal form (2NF):   This form eliminates *partial dependency*. If a table has a composite primary key with two or more columns, then all the columns (not included in the primary key) must depend on the entire composite primary key and not on a part of it. A table exhibits partial dependency when a nonprimary key column depends on only a portion of the primary key. [Figure 8-4](#ch08_figure_4_1724776834148562) shows an example. The right table has a composite primary key including account\_id and account\_type\_id. In this case, the column account\_type\_description depends only on account\_type\_id, hence generating a partial dependency. To normalize in 2NF, the account\_type\_id should be stored in a separate table, as illustrated on the right side of the figure.

    ###### Figure 8-4. Second normal form conversion

![Figure 8-4. Second normal form conversion](images/fden_0804.png)

Third normal form (3NF):   This form eliminates *transitive dependency*. All columns should only depend on the primary key, not on any nonprimary key columns. If a nonprimary key column depends on another nonprimary key column, the table is said to have a transitive dependency. See [Figure 8-5](#ch08_figure_5_1724776834148580) for an example. The table on the left side of the figure has a single-column primary key defined for transaction\_id. Both account\_id and amount depend on transaction\_id, but max\_transaction\_limit depends on account\_id, which is not a primary key. This generates transitive dependency. To normalize in 3NF, we need to create a separate table that stores the max\_transaction\_limit, as illustrated on the right side of the figure.

    ###### Figure 8-5. Third normal form conversion

![Figure 8-5. Third normal form conversion](images/fden_0805.png)

Relational database systems often prioritize normalization as their main modeling strategy. By eliminating redundancy, normalization ensures data integrity by minimizing the number of places that store the same piece of data and establishing reliable relationships between the tables. Think of this from a compliance perspective. For example, if a client of a financial institution requests that their personal data be updated or erased, the institution will only need to check one or a few tables (e.g., a client table) to find all of the individual’s information. If data was not normalized, the same personal information may be duplicated in many places, making it difficult to find, aggregate, update, or delete.

## Constraints

Constraints are a crucial feature of relational databases. They enforce data integrity and consistency during insert, update, and delete operations. The main advantage of defining constraints at the database level is that it decouples the constraint checks and management from the application that interacts with and manipulates the database.

Examples of SQL constraints include the following:

* The not-null constraint ensures that values in a given column are never null.
* The uniqueness constraint ensures that values in a given column are unique.
* The check constraint ensures that values in a given column satisfy a given value condition (e.g., >=0).
* The primary key constraint ensures that values in one or more columns can be used as the primary unique identifier in the table.
* The foreign key constraint ensures that values in one or more columns in one table match the values in a given column in another table.

For a comprehensive overview of these constraints and how to create them, I recommend the official PostgreSQL [documentation on constraints](https://oreil.ly/4uXHE). Keep in mind that constraints may have an impact on performance as they add additional work for the DB to do. The best way to approach DB constraints is by mapping them to business constraints during data modeling. For example, a check constraint may be added to ensure that the account balance never goes below zero, while a foreign key constraint may be added to guarantee that a product is not sold if it’s not in the inventory, and so on.