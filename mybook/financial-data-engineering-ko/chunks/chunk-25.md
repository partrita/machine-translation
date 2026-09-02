# Case Study: Anti–Money Laundering at Banking Circle with Neo4j

[Banking Circle (BC)](https://oreil.ly/exb5l) is a banking-as-a-service (BaaS) company that offers real-time and low-cost payment services by providing the clients with direct access to clearing in multiple jurisdictions. BC serves a large client base, including over 250 regulated businesses, financial institutions, and marketplaces. It allows clients to move and convert money in real time securely and compliantly. In 2021, BC processed over 250 billion euros in payment volume. Importantly, as the volume of payments that BC processed increased, so did the number of fraud attempts.

To detect fraud, BC initially relied on a [traditional rule-based approach](https://oreil.ly/HhmvY), which worked by assigning risk scores by searching and catching certain words, amounts, and locations and sending them to fraud analysts for manual review. However, the company realized that this approach was slow, expensive, and generated a high level of false positives. As a result, it decided to adopt a data-driven AML approach that leverages graph and machine learning techniques. The outcome was a modern framework called SCAM, or System for Catching Attempted Money laundering, which consisted of an ensemble of different machine learning models.

To capture complex relationships, SCAM relies on multiple network representations of various data features (e.g., accounts, payments, entities, countries, etc.). Using Neo4j’s [Graph Data Science (GDS) framework](https://oreil.ly/m-fYF), BC was able to conduct various types of advanced graph analysis.

For example, community detection algorithms were used to generate features that detect high-risk clusters within the network. A community detection algorithm works by finding clusters of similar nodes; for example, if a fraudster uses similar profile attributes, they are likely to fall within the same cluster. This technique, combined with other network features such as risk scores of neighboring nodes and distances to tax havens and known fraudsters, has significantly improved the reliability of SCAM.

BC was able to transform a laborious, sluggish procedure into a data-driven, scalable, flexible solution that leverages cutting-edge technology. False negatives were reduced by 10–25% and the number of overall alerts escalated for manual review was halved. BC continues to experiment with Neo4j algorithms and plans to add more graph features to tune their model further.

## The Warehouse Model

One of the most common business needs in data-driven organizations is an enterprise-wide system for integrated and structured data storage, access, analytics, and reporting. The most popular solution to this need is *data warehousing*, a concept that has been around since the 1970s. Bill Inmon and Ralph Kimball, the two pioneers of this field, define a data warehouse as:

> A data warehouse is a subject-oriented, integrated, nonvolatile, and time-variant collection of data in support of management’s decisions.
>
> Bill Inmon
>
> A data warehouse is a copy of transaction data specifically structured for query and analysis.
>
> Ralph Kimball

I will use the term *warehouse DSM* to describe a system that periodically gathers, consolidates, and structures data from various sources within a company into a central repository intended for various analytical purposes. A DSS system used to implement the warehouse DSM is called a warehouse DSS or data warehouse. [Figure 8-9](#ch08_figure_9_1724776834148654) illustrates a typical data warehouse architecture. As the figure shows, data from heterogeneous sources (left side) get organized into a central data warehouse (middle) which then serves a variety of analytical data needs (right side).

### Figure 8-9. A data warehouse architecture

![Figure 8-9. A data warehouse architecture](images/fden_0809.png)

### Why data warehouses?

The warehouse DSM offers several advantages, including the following:

Structure:   Data warehouses introduce a consistent structure to data, regardless of the original formats provided by the source systems.

Advanced analytics:   Performing advanced data queries for business intelligence and reporting is a fundamental and frequent activity within organizations. Data warehouses provide intuitive SQL-like querying capabilities that enable a wide range of data queries.

Scalability:   Data warehouses can scale to handle large volumes of data and complex read/write operations.

Subject-oriented:   Data warehouses are often designed to allow users to query and analyze data about a particular subject or functional area (such as sales, customers, payments, etc.)

Integrated:   Data warehouses consolidate, structure, and harmonize data from different sources (e.g., departments or business units) while ensuring consistency and data quality.

Nonvolatile:   Once data is uploaded to a data warehouse, it remains stable and does not change. If any changes occur to a data record, a new record is added instead of updating the existing ones.

Time-variant:   Data warehouses record data with a timestamp, allowing users to perform accurate point-in-time historical analysis.

At this point, you might be wondering about the difference between the warehouse DSM and other models that have similar features, such as the data lake or SQL DSMs. Similar to data warehouses, data lakes can also be used to consolidate data into a central location. Data lakes lack default mechanisms to ensure data structure consistency and homogeneity, and they do not offer advanced querying capabilities like a data warehouse does.

The primary difference between a relational DSM and a data warehouse DSM can be understood through the distinction between OLAP and OLTP. The relational DSM is primarily meant for OLAP-oriented applications, emphasizing transactional guarantees and single-row lookups/inserts/updates (often called *Data Manipulation Language*, or DML). The data warehouse DSM is instead aimed toward OLAP-oriented applications that require complex analytical read/write operations with less focus on point lookups and DML. However, it’s important to note that both the relational and warehouse models can coexist. In many cases, a significant portion of the data ingested into a data warehouse originates from relational databases that support day-to-day business operations.

### Data modeling with data warehouses

When building a data warehouse, data modeling is critical. Over the years, two competing approaches to data modeling have emerged for data warehouses: the *subject modeling approach* of Bill Inmon and the *dimensional modeling approach* of Ralph Kimball.29

In the Inmon approach, data is sourced from various operational systems across the organization and integrated into a centralized data warehouse. Subsequently, based on the specific needs of individual departments or business units, dedicated data marts are derived from the data warehouse. In this model, the data warehouse and the data marts are physically separate entities, each with its own storage and characteristics. Data within the data marts is considered consistent and reliable, as it originates from the centralized source of truth—the data warehouse itself. Users from different departments typically employ specialized tools to access and analyze the data within their respective data marts. [Figure 8-10](#ch08_figure_10_1724776834148673) offers an illustration of the Inmon architecture. The main advantage of this approach is flexibility, as new data marts can be created to meet new business needs. On the negative side, such an architecture introduces a maintenance burden due to the physical separation between the data warehouse and the data marts.

The Kimball approach takes a different perspective. Instead of isolating the data warehouse from the data marts, Kimball suggested a user requirement-driven approach that defines the data marts in advance and integrates them within the data warehouse itself. [Figure 8-11](#ch08_figure_11_1724776834148691) illustrates the concept.

### Figure 8-10. Inmon data warehouse architecture

![Figure 8-10. Inmon data warehouse architecture](images/fden_0810.png)

### Figure 8-11. Kimball data warehouse architecture

![Figure 8-11. Kimball data warehouse architecture](images/fden_0811.png)

The definition of data marts is done via a technique called *dimensional modeling*. Its main idea is to divide data into *fact* and *dimension* tables. A fact table contains data on quantifiable business entities or events, while a dimension table stores data related to the context of the events. Examples of facts include financial payments, monetary transfers, and online sales. Dimensions may be information such as product, user, and country details. Facts and dimensions may be used to categorize data into data mart–specific tables based on various business processes such as revenues, products, sales, employees, suppliers, and branches.

In dimensional modeling, two primary types of data warehouse schemas are prevalent: the star schema and the snowflake schema. The star schema features a central fact table connected directly to multiple dimension tables, resembling a star-shaped architecture. On the other hand, the snowflake schema is a normalized version of the star schema that has a single fact table and several direct and indirect dimension tables. [Figure 8-12](#ch08_figure_12_1724776834148709) illustrates the difference.

### Figure 8-12. Star schema versus snowflake schema

![Figure 8-12. Star schema versus snowflake schema](images/fden_0812.png)

Star schemas are generally easier to understand and simpler to query because they involve fewer table JOIN operations. Snowflake schemas, on the other hand, can be more effective at ensuring data integrity and consistency as they remove redundancy through data normalization.30

### Technological implementations of data warehousing

Due to the high demand for data warehousing, numerous technological implementations have been developed. As data warehouses emphasize structured data and advanced querying capabilities, most technologies in this domain support SQL and relational data modeling. Leading commercial solutions include high-performance integrated systems like IBM Netezza, IBM Integrated Analytics System (IAS), Db2, Teradata, Oracle Exadata, and Micro Focus Vertica Enterprise. Financial institutions often rely on these solutions for high-performance processing of large datasets.31

In recent years, cloud-based data warehousing solutions have seen a notable increase in popularity. Examples include Amazon Redshift, Snowflake, Google BigQuery, and Azure Synapse Analytics. This surge is largely attributed to the convenient features that the cloud offers in terms of scalability, managed infrastructure, on-demand pricing, reliability, and seamless integration with other cloud services. For example, with a data warehousing service such as Google BigQuery, you can easily create a database and begin writing and reading data to it in a matter of minutes. As a serverless platform, BigQuery handles all infrastructure management, so you don’t have to worry about provisioning or scaling resources.

Cloud-based data warehouses commonly adopt column-oriented storage, enhancing query performance and reducing costs by retrieving only the columns requested by users. This storage method also benefits from efficiency gains through compression and deduplication techniques, optimizing data storage on disk.32

Cloud data warehouses achieve scalability by decoupling the compute and storage layers. For example, using Snowflake as a data warehouse, your data will be stored and managed in [separate persistence storage (e.g., AWS S3)](https://oreil.ly/6UHJF). In contrast, compute resources are virtualized and can be independently scaled up or down by the user, separate from storage.

To enhance storage efficiency and query performance, cloud warehouses leverage the concept of data *partitioning* and *clustering*. The idea is to split a table into a set of storage units called partitions that can be managed and queried separately. With clustering, data within each partition is physically ordered into small blocks of data. When a query is executed against a table, the database engine will first filter the partitions to scan (partition pruning) and then apply block filtering (pruning) to each partition. This way, only the minimum amount of data is queried, thus increasing performance and reducing query cost. BigQuery [requires the user to configure the partitioning and clustering keys (from existing columns)](https://oreil.ly/caYnO), while Snowflake implements a more dynamic and managed approach to partitioning and clustering called [*micro-partitioning*](https://oreil.ly/A_h2H).

### Note

When using cloud data warehouses, it’s crucial to consider vendor-specific limits, quotas, and usage guidelines. For instance, as OLAP systems, data warehouses are optimized for running complex analytical queries with moderate frequency. Attempting to support thousands of concurrent users may exceed maximum connection limits. For example, BigQuery allows up to 100 concurrent connections for interactive queries, while Snowflake, with auto-scaling, supports up to 80 concurrent connections. Furthermore, while data warehouses do support data updates and DML operations, they are not primarily designed for these tasks.

### Financial use cases of data warehouses

Data warehouses are extensively used in the financial sector to address various business needs. One major use case is the consolidation of data from diverse business silos (e.g., risk, revenue, loans) into a unified data warehouse that serves as the primary source for analytics. This consolidation facilitates the extraction of valuable business insights from the vast volumes of data generated through daily operations within financial institutions. For instance, this enables business teams to effectively understand and manage different types of risks such as credit, financial, operational, and compliance risks. In Chapter 5 on financial data governance, we discussed how data aggregation and consolidation capabilities have become a regulatory requirement for banks following the crisis of 2007–2008.

Data warehouses can enable financial institutions to track financial, operational, and data quality indicators over time. Maintaining point-in-time historical data is a common business requirement in financial markets. A well-designed data warehouse may ensure this by enforcing an append-only policy, which allows new data to be written while maintaining the immutability of existing data. This principle also applies to externally sourced financial data. For instance, financial vendor data is intended for reading and analysis rather than modification, making a data warehouse an ideal solution for such use cases.

Furthermore, data warehouses are widely used in financial markets for facilitating data sharing. For example, various financial data vendors now offer the option to deliver their data to clients via the cloud. This delivery mechanism is particularly convenient with cloud-based data warehouses. Refer to the section “Data Ingestion Technologies” to learn more about this topic.

# Case Study: BlackRock’s Aladdin Data Cloud Powered by Snowflake

BlackRock is the world’s largest and leading investment management firm and a provider of financial technology. As of 2023, BlackRock’s assets under management [reached around 8.5 trillion US dollars](https://oreil.ly/4j0fV). BlackRock’s jewel technology is known as *Aladdin*, an integrated solution that combines sophisticated risk analysis features with portfolio management, trading, and operations tools in a single platform. Aladdin has established itself as one of the most prominent examples of financial technologies. In particular, during the 2008 financial crisis, Aladdin showed its remarkable capabilities by allowing companies like Microsoft to [aggregate their risk exposures to different banks (a feature that many financial institutions lacked at the time)](https://oreil.ly/c0AZe).

To enhance Aladdin’s data-driven capabilities, BlackRock launched *Aladdin Data Cloud*, a managed data solution that allows users to combine Aladdin portfolio data with non-Aladdin data, perform timely analysis, and develop custom dashboards and applications using Aladdin Studio—BlackRock’s platform for developers. To this goal, BlackRock [decided to partner with the cloud-based data warehousing company Snowflake](https://oreil.ly/WaUHG). The main reasons for choosing Snowflake were performance, scalability, and concurrency management.

By bringing together Aladdin, a leader in investment management technology, and Snowflake’s Data Cloud, the Aladdin Data Cloud is set to allow its clients to expand the range of data-driven applications across their organizations. Each Aladdin Data Cloud client receives an independent, centrally managed data store preloaded with rich front-to-back Aladdin datasets, which can then be supplemented with proprietary and other third-party data sources, allowing organizations to access and query their business-critical data on a single, cloud-based platform.

Snowflake has several features that make it attractive for building data applications. For example, it isolates work environments via [virtual warehouses](https://oreil.ly/oBrcL), which are clusters with dedicated CPU, memory, and temporary storage. In a simple setup, each client can be dedicated to a separate virtual warehouse. Virtual warehouses offer the flexibility to scale resources up and down, thus customizing work environments for different client needs. In addition, Snowflake has advanced and secure [data-sharing functionalities](https://oreil.ly/jBDj3), making it ideal for working with a large base of users and accounts. Moreover, Snowflake developed [its own SQL language](https://oreil.ly/Ai-zH) with rich command features and SQL standard-compliant syntax. Additionally, Snowflake provides a [list of configurable parameters](https://oreil.ly/CrTk_) that can be tuned to control the behavior of a user account, queries, sessions, and objects.

## The Blockchain Model

Blockchain is one of the most promising technological trends in today’s financial services landscape. It is the underlying technology that enables the so-called *cryptocurrencies,* such as Bitcoin and Ethereum.33 In this section, I will briefly walk through the basic idea behind blockchain and its applicability as a data storage system for financial data.34

At the most basic level, a blockchain is a data structure that stores data as a chain of linked information blocks. The most prominent application of blockchain technology is in the creation of *digital ledgers*. A digital ledger is a record-keeping book of accounts that keeps track of a business’s financial transactions. Think, for example, of when you deposit or withdraw money from your bank account. As per common sense, you trust that your bank will maintain a correct and truthful ledger and not modify it by deleting or updating book records.

A blockchain data ledger performs a similar function and guarantees data immutability, but following different design principles. To illustrate the idea, let’s represent a blockchain as a linked list of information blocks, as illustrated in [Figure 8-13](#ch08_figure_13_1724776834148729). The first block in a blockchain is called the *genesis block*. Each subsequent block contains its own data (e.g., transaction records) as well as a *hash pointer* that stores both a pointer to the previous block and a hash of that older block. A hashing function, H(), is used to create a cryptographic hash of each block’s data. A block hash serves as a unique identifier of each block.

### Figure 8-13. Blockchain as a linked list

![Figure 8-13. Blockchain as a linked list](images/fden_0813.png)

To illustrate why this structure is tamper resistant, consider an adversary attempting to manipulate the blockchain by altering data entries in block 2. This will automatically update the block’s hash. As a result, the hash pointer in block 3 will no longer correspond to the updated hash of block 2. To conduct a successful attack, the adversary must alter all hash pointers up to the most recent block in the list (i.e., the head).

In addition to data immutability, blockchain-based data ledgers have shown high reliability when implemented as a distributed system. The term *distributed ledger technology* (DLT) is often used to describe these systems. In a DLT, a decentralized network of nodes cooperatively maintains the integrity of the ledger. Each node keeps a copy of the blockchain and can verify and validate any operation that alters the blockchain. For example, if a node wants to add a new block to the chain, the other nodes in the network need to agree and reach a consensus on such an operation. The same applies to our earlier example of the adversary attack: even if the adversary were able to change all the hash pointers, the changes would still need to be validated and accepted by the other nodes in the network. A variety of consensus mechanisms are available, including Proof of Work, Proof of Stake, and Byzantine Consensus.

As a financial data engineer, you might be wondering if blockchain is a good solution as a data storage system. Technically speaking, a blockchain can be used to store financial transaction data, but it comes with a price. First, blockchains have very limited data querying capabilities. Second, as more nodes are added to the network, performance may get worse in terms of throughput, latency, or capacity.35 For example, the decentralized nature of blockchain introduces latency in both storing and retrieving data. In applications requiring fast data access, the time taken for reaching consensus, propagating blocks, and verifying transactions can lead to slower response times.

To overcome these issues, blockchain-based databases (or blockchain databases for short) were introduced. The main idea behind a blockchain database is to combine the best of both worlds: the performance and power of a traditional database system (e.g., SQL or document databases) with the immutability, cryptographic verifiability, integrity, decentralized control, and transaction traceability of a blockchain.

Crucially, when deployed internally within a financial institution, a blockchain database doesn’t need to be decentralized. The institution in this case acts as the administrative authority that controls the blockchain.36

A few commercial solutions for blockchain databases already exist. The most prominent is [BigchainDB](https://oreil.ly/ZcpNm), which uses MongoDB as the distributed database under the hood and offers blockchain characteristics. Another example is [Amazon Quantum Ledger Database (QLDP)](https://oreil.ly/LGhUz), a fully managed ledger database for creating an immutable, transparent, and cryptographically verifiable transaction log.

# Ripple: A Blockchain-Based Global Payment Ecosystem

A successful story in the commercial implementation of blockchain technology is Ripple. Behind this is an American company called Ripple Labs, Inc. It is a unique player in this industry as it created the first financial services platform and network that leverages blockchain, tokenization, and cryptocurrency technologies for enterprises. Ripple’s primary use case is to enable secure, instant, and low-cost cross-border financial transactions and settlements.

Ripple’s primary offering is RippleNet, a blockchain-based infrastructure for payments. As of the end of 2024, RippleNet connects a network of over 500 participants.

XRP is Ripple Labs’s native cryptocurrency (digital asset). It is used as a bridge currency in Ripple’s ecosystem to facilitate liquidity for cross-border transactions. XRP is independent of RippleNet but can be utilized within the network for certain services. XRP is a [bridge asset](https://oreil.ly/_grQh), or an asset that businesses and financial institutions can use to make a bridge transfer between two different fiat currencies. In this scenario, a financial institution can purchase an equivalent amount of XRP and send it through Ripple’s network.

The underlying blockchain ledger technology that powers Ripple is called XRP Ledger (XRPL). Interestingly, [XRPL differs from Bitcoin’s blockchain](https://oreil.ly/oLZhy). Bitcoin relies on an energy-intensive Proof-of-Work (PoW) mechanism for transaction validation, while Ripple uses the faster and more efficient mechanism known as the [XRP Ledger Consensus Protocol](https://oreil.ly/KO_vH), or XRP LCP for short. For an intuitive introduction to XRP LCP, see the [CoinBrain website](https://oreil.ly/B9SPu). This consensus mechanism is key to XRPL’s efficiency, enabling rapid transactions at low costs. XRPL has been released to the public, and it is now an [open source blockchain protocol](https://oreil.ly/3t-5j).

To illustrate an example (sourced from the [Ripple website](https://oreil.ly/jq5-z)), let’s say that Bank A intends to transfer $10,000 to Bank B in euros using the Ripple platform. The banks agree on a Forex rate on Ripple, following which Bank A converts the USD to XRP at the agreed rate and transfers it via the XRP Ledger to Bank B. Upon receipt, which happens in a matter of seconds, Bank B converts the XRP to euros, with minimal transaction fees compared to traditional banking methods. This use of XRP as a bridge currency via RippleNet demonstrates its role in facilitating fast and cost-effective cross-border transactions.

Ripple has helped countries create their own [central bank digital currencies (CBDCs)](https://oreil.ly/Otp-V) through its Ripple CBDC platform. Furthermore, Ripple is a member of the ISO 20022 Standards Body, becoming the first member of the ISO organization dedicated to Distributed Ledger Technology (DLT).

In conclusion, blockchain presents a complex landscape with ongoing efforts aimed at exploring its feasibility for high-storage and high-performance applications. Researchers and developers are actively investigating various approaches to enhance blockchain’s capabilities, such as sharding, optimizing consensus algorithms, Layer 2 protocols, and sidechains, and are exploring hybrid architectures that combine blockchain with traditional databases.