# Summary

This chapter covered the second layer of the financial data engineering lifecycle: storage. This layer facilitates the choice and implementation of various data storage models and systems, supporting the storage and retrieval of data within a financial data infrastructure.

Crucially, data is not merely ingested and stored. To unlock its full potential in driving informed decision-making and operational excellence, data must undergo a systematic transformation into structures that align with the diverse needs of stakeholders within financial institutions. This takes us to the next layer: transformation and delivery. This layer serves as the bridge between raw data ingestion and its utilization by end users.

Let’s explore this critical layer further in the next chapter.

1 For a comprehensive overview of data modeling, I highly recommend Graeme Simsion and Graham Witt’s *Data Modeling Essentials*, 3rd ed. (Morgan Kaufmann, 2004).

2 This definition is derived from the one provided by PostgreSQL [documentation](https://oreil.ly/Q5cDP).

3 The acronym ACID was coined in 1983 by Andreas Reuter and Theo Härder in their seminal work, [“Principles of Transaction-Oriented Database Recovery”](https://oreil.ly/rKOKj), *ACM Computing Surveys (CSUR)* 15, no. 4 (December 1983): 287–317.

4 The definition I present for snapshot isolation is provided in an operational way, which is done for the sake of simplicity. This concept can be further explored from a more rigorous, mathematical point of view; for example, see Andrea Cerone and Alexey Gotsman’s [“Analysing Snapshot Isolation”](https://oreil.ly/5TxT-), *Journal of the ACM (JACM)* 65, no. 2 (January 2018): 1–41.

5 This example was inspired by the excellent [illustration of the CAP theorem by ByteByteGo on YouTube](https://oreil.ly/mUNyi).

6 To learn more about consistency tradeoffs, I highly recommend Daniel Abadi’s [“Consistency Tradeoffs in Modern Distributed Database System Design: CAP Is Only Part of the Story”](https://oreil.ly/td_3V), *Computer* 45, no. 2 (February 2012): 37–42.

7 To learn more about database stress testing, see Bert Scalzo’s *Database Benchmarking and Stress Testing: An Evidence-Based Approach to Decisions on Architecture and Technology* (Apress, 2018).

8 See, for example, [“How We Stress Test and Benchmark CockroachDB for Global Scale”](https://oreil.ly/oOGNN), by Stan Rosenberg, Alexander Shraer, William Kulju, and Alex Lunev.

9 For more on this topic, read Yishan Li and Sathiamoorthy Manoharan’s [“A Performance Comparison of SQL and NoSQL Databases”](https://oreil.ly/4Y1ps), in the *2013 IEEE Pacific Rim Conference on Communications, Computers and Signal Processing (PACRIM)* (IEEE, 2013): 15–19.

10 For more details, see Rick Cattell’s [“Scalable SQL and NoSQL Data Stores”](https://oreil.ly/Pq3l8), *ACM SIGMOID Record* 39, no. 4 (May 2011): 12–27.

11 For example, Netflix created an orchestration engine called Conductor which uses Dynomite for primary persistence storage. On top of that, Elasticsearch is used as a secondary indexing database to allow workflow search and discovery. For more on Conductor, read the [official documentation](https://oreil.ly/jbjHG).

12 Example inspired by the excellent article [“Native vs. Non-Native Graph Database”](https://oreil.ly/swtye), by John Stegeman.

13 For more details on this data lake architecture pattern, I recommend reading Franck Ravat and Yan Zhao’s [“Data Lakes: Trends and Perspectives”](https://oreil.ly/fI7Fu), in *Database and Expert Systems Applications: 30th International Conference, DEXA 2019*, *Proceedings*, Part I (August 2019): 304–313.

14 To learn more about the history of SQL, I highly recommend Donald D. Chamberlin’s [“Early History of SQL”](https://oreil.ly/fwBZj), *IEEE Annals of the History of Computing* 34, no. 4 (October–December 2012): 78–82.

15 For a good read on this topic, see [“Anomalies in Relational Model”](https://oreil.ly/sS4HR) by GeeksForGeeks.

16 For an excellent illustration of these normal forms with examples, I suggest checking the article [“Normalization in DBMS”](https://oreil.ly/uNOel) by Study Tonight.

17 For a good overview of SQL database indexing, see the official PostgreSQL [documentation on indexes](https://oreil.ly/fNQpi).

18 For a good comparison between relational database management system features, consult [Wikipedia](https://oreil.ly/mYQEJ).

19 A detailed account of this problem is offered in the blog post [“Why Sharding Is Bad for Business”](https://oreil.ly/bX0qM), by Michelle Gienow.

20 For a general overview, consult the official MongoDB [page on indexing](https://oreil.ly/IfapL).

21 To learn more, read InfluxDB’s documentation on the [InfluxDB storage engine](https://oreil.ly/STcKh).

22 For a comparative study on this topic, I recommend Fazl Barez, Paul Bilokon, and Ruijie Xiong’s [“Benchmarking Specialized Databases for High-frequency Data”](https://oreil.ly/KLZBD), *arXiv* preprint; arXiv:2301.12561 (January 2023).

23 In asynchronous communication, an application sends a request or message in a *fire-and-forget* mode, meaning that a response isn’t expected from the target receiver or consumer.

24 For more on this topic, consult the [Confluent Developer website](https://oreil.ly/6ENFr).

25 For an interesting real-world application of this idea, I highly recommend watching the [presentation given by two AWS experts](https://oreil.ly/R1Jl1) on how to build a real-time financial data feed as a service on AWS.

26 For more details on these features, consult the official [Neoo4j documentation page](https://oreil.ly/KSpxm).

27 To learn more about this topic, see David Montag’s [“Understanding Neo4j Scalability”](https://oreil.ly/63X8H) white paper, *Neotechnology* (January 2013).

28 An example of a company that offers such services is [Financial Network Analysis (FNA)](https://oreil.ly/uJC55).

29 For a comprehensive comparative study of the difference between Inmon and Kimball models, see Lamia Yessad and Aissa Labiod’s [“Comparative Study of Data Warehouses Modeling Approaches: Inmon, Kimball and Data Vault”](https://oreil.ly/Bmsi5), in *2016 International Conference on System Reliability and Science (ICSRS)* (IEEE, 2016): 95–99.

30 For an excellent reference on dimensional modeling, I recommend Ralph Kimball and Margy Ross’s *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling*, 3rd ed. (Wiley, 2013).

31 For instance, the NYSE transitioned to IBM Netezza to manage its growing data volumes, which traditional SQL databases were unable to handle effectively. Read more in [“At NYSE, the Data Deluge Overwhelms Traditional Databases”](https://oreil.ly/pcP2w), by Tom Groenfeldt.

32 For a deeper understanding of how and why columnar formats are used in data warehouses, I highly recommend reading about Google BigQuery’s columnar storage format [Capacitor](https://oreil.ly/1Mq_3).

33 For a good introduction to cryptocurrencies, I highly recommend Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, and Steven Goldfeder’s *Bitcoin and Cryptocurrency Technologies: A Comprehensive Introduction* (Princeton University Press, 2016).

34 For a deeper introduction to blockchain databases, I highly recommend Chapter 26 of Avi Silberschatz, Henry F. Korth, and S. Sudarshan’s 2019 *Database Systems Concepts*, 7th ed. (McGraw Hill, 2019).

35 For more on performance-related issues in blockchains, read Mayank Raikwar, Danilo Gligoroski, and Goran Velinov’s [“Trends in Development of Databases and Blockchain”](https://oreil.ly/RfFIG), in the *2020 Seventh International Conference on Software Defined Systems (SDS)* (IEEE, 2020): 177–182.

36 To learn more about blockchain database design patterns, I recommend MongoDB’s guide [“Blockchain Database: A Comprehensive Guide”](https://oreil.ly/klrQS).

# Chapter 9. Data Transformation and Delivery Layer

By now, you should be familiar with the first two layers of the financial data engineering lifecycle: ingestion and storage. The next layer is the transformation and delivery layer, where two major things happen: first, the data undergoes a range of transformations, from basic preprocessing and cleaning to complex analytical calculations; second, the data is delivered to its end users following pre-established agreements. Keep in mind that all layers can impact one another based on business needs and technical limitations. As a result, the decisions you make in the ingestion and storage layers are likely to have an impact on this layer and vice versa.

Throughout this chapter, you will learn the essential concepts of data transformation and delivery and their applications in the financial domain. This includes data querying patterns, query optimization, transformations, computational requirements, data consumers, and delivery mechanisms.

# Data Querying

The most common operation performed in the transformation and delivery layer is data querying. Before making any modifications, data is always queried. The performance of a financial data infrastructure is largely dependent on querying patterns and optimization. Therefore, as a financial data engineer, you will play a vital role in defining and optimizing the querying needs and patterns for your team and data consumers. Let’s find out how.

## Querying Patterns

A data querying pattern is a repeated request for information made by several data consumers on a regular basis. A pattern can be either detected by analyzing user requests or anticipated during an early design phase. Being able to understand and anticipate querying patterns will provide you with great input for the choice and design of your data storage model as well as optimizing the cost and execution time of your data queries.

There is no fixed catalog for querying patterns; they are primarily determined by business requirements and data consumer needs. However, in this section, I will introduce several common querying patterns that you might encounter in financial applications.

### Time series queries

Time series queries are essential in finance, used to retrieve data for a specific financial entity or quantity over a given period of time. Using standard SQL pseudocode, we can express a basic time series query:

```
-- SQL
SELECT time_column, attribute_1, attribute_2
FROM financial_entity_table
WHERE entity_name = 'A'
AND date BETWEEN '2022-01-01' AND '2022-02-01'
```

Financial use cases for time series queries include the following:

* Give me the closing adjusted price for stock A from January 2022 until February 2022.
* Give me all transactions for client A for the past month.
* Give me a company’s sales and revenues over the past six months.

### Cross-section queries

A cross-section query is used to obtain data for a set of financial entities at a specific point in time. A simplified SQL pseudocode for a cross-section query might look something like this:

```
-- SQL
SELECT entity_name, attribute_1, attribute_2
FROM financial_entity_table
WHERE entity_name in ('A', 'B', 'C', 'D')
AND date = '2022-02-01'
```

Cross-section queries are commonly used to investigate differences between financial entities at a given point in time. Examples include the following:

* Give me the market capitalization of the top five companies listed at the NYSE for February 1, 2022.
* Give me the credit rating of all publicly traded companies in the pharmaceutical sector in the United States on January 10, 2022.

### Panel queries

A panel query combines time series and cross-section dimensions. The user asks for data on multiple financial entities for a range of dates. A pseudo-SQL for a panel query may look like this:

```
-- SQL
SELECT time_coluumn, entity_name, attribute_1, attribute_2
FROM financial_entity_table
WHERE entity_name in ('A', 'B', 'C', 'D')
AND date BETWEEN '2022-01-01' AND '2022-02-01'
```

Panel queries are mainly used to analyze the intertemporal differences between financial entities—for example the following:

* Give me the online purchasing activities of our top 1,000 clients in the past month.
* Give me the volume of trades for stocks A, B, and C over the past month.

### Analytical queries

Analytical queries are advanced statements that perform computations on the data. They are often supported and used in SQL and data warehousing systems as well as specialized databases such as time series and graph databases.

The most common type of analytical query is grouping, in which rows that have the same values are grouped into summary rows using an aggregation function such as sum, min, max, average, standard deviation, and others. For instance, if you want to find the maximum daily price for each unique combination of stock symbols and dates in your database, you would write an SQL query similar to this:

```
-- SQL
SELECT stock_symbol, date, MAX(price)
FROM price_table
GROUP BY stock_symbol, date
```

Grouping reduces the number of rows into a set of groups based on your aggregation fields. In some cases, you don’t want the number of rows to shrink, but rather want to apply an aggregation query that spans multiple time windows. For example, suppose you want to calculate the simple moving average of the adjusted closing price for each stock in your dataset.1 In this case, a special type of SQL method, called *window functions*, can be used. Here is how it works:2

```
-- SQL
create table adjsted_price (date DATE, symbol VARCHAR(5), price NUMERIC);
insert into adjsted_price (date, symbol, price) values ('2022-02-10', 'A', 1);
insert into adjsted_price (date, symbol, price) values ('2022-02-11', 'A', 2);
insert into adjsted_price (date, symbol, price) values ('2022-02-12', 'A', 3);
insert into adjsted_price (date, symbol, price) values ('2022-02-13', 'A', 4);
insert into adjsted_price (date, symbol, price) values ('2022-02-10', 'B', 10);
insert into adjsted_price (date, symbol, price) values ('2022-02-11', 'B', 20);
insert into adjsted_price (date, symbol, price) values ('2022-02-12', 'B', 30);
insert into adjsted_price (date, symbol, price) values ('2022-02-13', 'B', 40);

SELECT symbol, date, AVG(price)
OVER (PARTITION BY symbol ORDER BY date ASC ROWS BETWEEN 2
PRECEDING AND CURRENT ROW) AS "Moving Average"
FROM adjsted_price
ORDER BY symbol, date ASC
```

A variety of data storage systems implement window and analytical functions. For example, relational DSSs like PostgreSQL implements the SQL standard window functions, while others such as Oracle implement [additional functions](https://oreil.ly/WmwMa) on top of the standard ones. Specialized databases, such as InfluxDB time series database, offer an impressive [collection of time-based analytical functions](https://oreil.ly/IwwI4). Similarly, graph databases such as Neo4j offer a wide range of [graph-oriented functions](https://oreil.ly/LoTnA) that can be executed with the Cypher language, as well as a specialized library called Graph Data Science that offers advanced graph algorithms and visualization features that can be used to solve advanced business problems such as fraud detection.

Recently, cloud data warehouse solutions such BigQuery and [Snowflake](https://oreil.ly/hG3RV) have introduced features enabling users to create and interact with machine learning models using advanced analytical SQL queries. These capabilities allow users to build various models (e.g., regression, classification, anomaly detection, etc.) and make predictions on new data, all seamlessly integrated within the data warehouse environment. Using [BigQuery](https://oreil.ly/gs-hW), the syntax for creating a model may look like the following:

```
-- SQL
-- Create a linear regression model
CREATE MODEL `mydataset.my_model`
OPTIONS(MODEL_TYPE='LINEAR_REG') AS
SELECT
  feature_column1,
  feature_column2,
  label
FROM
  `mydataset.my_training_table_data`;
```

When calling the model, the syntax would look like this:

```
-- SQL
SELECT *
FROM
  ML.PREDICT(MODEL `mydataset.my_model`, (
    SELECT
      feature_column1,
      feature_column2
    FROM
      `mydataset.my_test_table_data`
  ));
```

Before moving to the next section, an essential thing to keep in mind is that data querying needs can evolve and change time. It’s impractical and costly to switch data storage systems due to query limitations. Therefore, it’s essential to consider the broader context, prioritize the needs of the business and data consumers, and develop a strategy to manage both current and future query requirements effectively.

## Query Optimization

Once you’ve identified your querying needs and patterns, the next step is to think about and implement a query optimization strategy. If queries are not optimized, their performance can be significantly impacted. For simplicity, I will define performance in terms of query speed and cost. A query optimization strategy can be approached from two perspectives: the database side and the user side. Let’s explore each in detail.

### Database-side query optimization

On the database side, there are three main query optimization techniques: indexing, partitioning, and clustering. Indexing is the most common technique. To understand the need for indexing, let’s illustrate its main use case. Imagine you have a database that contains price data for 1,000 stocks. You want to run a time series query that fetches data for one stock (stock A). The database engine doesn’t know where the data for stock A is physically located on disk. For this reason, the only way to execute the query is to read all data for all stocks and keep stock A’s records only. This type of data read is called *full-scan*, as the entire table is scanned. As you can imagine, this is an expensive operation, given the time it takes to do a full scan. Can we do better? Yes, we need to add an index!

An index is an optimized data structure that holds information about the disk location of the data stored in your database. When the right index is added, the database engine will try to use it to look up the location of the data and avoid querying unnecessary records. Now you might wonder, how do I know which index to add? The answer depends on your querying patterns. A rule of thumb is to add an index on the columns that you use in your WHERE clause. For example, let’s consider the following query:

```
-- SQL
SELECT time_column, attribute_1, attribute_2
FROM financial_entity_table
WHERE entity_name = 'A'
AND date BETWEEN '2022-01-01' AND '2022-02-01'
```

As you can see, the WHERE clause uses two columns: entity_name and date. For this reason, it makes sense to add an index on both columns. In this case, the index is called *composite* as it is created on multiple columns. If your query were to only filter by entity_name, then it’s better to create a single-column index instead. Now you might ask, how do I know what type of index I need to add? There are indeed a variety of database indexes. To illustrate with an example, let’s take PostgreSQL as a reference as it has a [large variety of index types](https://oreil.ly/-iaLi).

The standard index implementation in PostgreSQL is *B-tree,* a tree-based data structure that achieves logarithmic complexity.3 The reason behind the popularity of B-tree indexes is their ability to handle a wide range of query operators: less than (<), less than or equal to (<=), equal to (=), greater than (>), greater than or equal to (>=), and between. Other types of data storage systems, such as MongoDB and Neo4,j use B-tree as their default index implementation. Therefore, unless you have any special query needs, the B-tree is generally a good indexing strategy. Keep in mind, however, that indexes are stored on disk and grow in size as your data does. In addition, indexes get updated as you update, insert, and delete records from the database. For this reason, you must aim to create the least number of indexes when possible.

Other types of indexes are often used for more specific use cases. For example, the *Block Range Index* (BRIN) is a lightweight index that can be used with very large tables, where the indexed columns have a strong correlation with the physical order of data in the table. A typical scenario might involve a large stock price time series dataset where data is organized by date. When performing time series queries involving a wide temporal range (e.g., last month), PostgreSQL can utilize the BRIN index to quickly identify and skip over data blocks that do not contain relevant dates.

In some cases, indexes such as B-tree and BRIN are complemented with [*clustering*](https://oreil.ly/6mLiT), which involves physically rearranging data based on one or more columns, often those used to create an index. This rearrangement is advantageous when your queries frequently access a range of ordered values, such as in time series queries. It’s important to remember that clustering is a one-time operation. If the data is updated, re-clustering will be required.

Last but not least, a powerful database optimization technique is *partitioning*. It works by dividing the data into logical and physical partitions/tables using one or more partition keys. Queries filtering by these keys will exclusively scan relevant partitions, minimizing unnecessary data access. A partition key is often chosen to minimize the number of scanned partitions. For example, suppose you have high-frequency stock price data that arrives daily, and assume that most of your queries include a day range filter (e.g., the last three days, first 10 days of last month,...). In this case, it makes sense to partition your table by date to have one partition for each day. This way, even if you have 1,000 partitions, if you query data for one date, then only one partition will be scanned.

# Query Planner

You might ask yourself, how do databases figure out the most optimal way to execute a query and choose which index and scanning strategy to perform? This is all done by the so-called query planner/optimizer.

Each database system implements its own query planner, which is responsible for figuring out the most efficient execution plan for each user query. Typically, query planners represent queries as trees, allowing for multiple execution strategies that yield identical results. These trees are typically read from the bottom up, with data being retrieved initially from one or more locations, and then aggregated as you move upwards to produce the final results. The query planner’s goal is to select the optimal plan for execution, which may involve substituting the original query with one or more optimized versions to enhance performance. Some databases implement more complex techniques. For example, PostgreSQL’s query planner might resort to an advanced optimization technique based on genetic algorithms when planning for complex queries (e.g., when there is a large number of join operations).

Common strategies that query planners often rely on include the following:

Sequential scan:   Scans the entire table. This is used when the table is small or if indexing is not properly done.

Index scan:   Performs an index traversal to find all matching records. The planner might perform an index scan if any index satisfies the WHERE condition.

Index-only scan:   Performed if all queried columns are part of an index, returning tuples directly from index entries.

Parallel scan:   Multiple processes fetch a subset of the requested data simultaneously, thereby speeding up query execution.

Partition pruning:   Used with partitioned database systems (e.g., BigQuery and Snowflake) to minimize the number of partitions to scan.

Block pruning:   Used mostly with clustered tables, and determines which blocks of data to read, thus saving disk access and accelerating query execution.

Many database systems offer a command called EXPLAIN, which provides a detailed breakdown of the execution plan that the query planner generates for a given query statement. To read more about query planners, I recommend having a look at PostgreSQL’s [Planner/Optimizer](https://oreil.ly/926mb), BigQuery’s [Dremel engine](https://oreil.ly/rKUpU), and Redshift’s [query optimizer](https://oreil.ly/P-K5v).

In conclusion, it is essential to remember that database optimization may be a time-consuming and challenging task (yet fun as well!). As such, give it some serious thought and include the business team to ensure that all of their demands are met. Furthermore, be sure to provide a summary of all the technical limitations that may arise along the way, and consider how they can affect future data and querying needs.

### User-side query optimization

Database-side optimization is only half the story; the other half concerns optimizing the way users interact with the data. You can have the best indexing, clustering, and partitioning strategy in place, but users need to follow the right querying approach to benefit from such optimizations. There is no unique recipe for telling users how to query the data—it’s all based on the querying needs and the database optimization put in place. Let me give you a few illustrative examples.

## Scenario 1

If you add a single-column index on column A, try to avoid queries that do not reference column A in their search conditions. While there’s no guarantee the query planner will use the index every time, doing so could potentially result in notable performance gains.

## Scenario 2

If you add a composite index on columns A, B, and C, then make sure that you filter by the leading (leftmost) columns such as [A], [A, B], or [A, B, C]. Filtering by [B] or [C] or [B, C] will lead to inefficient index scans. I highly recommend that you read more about this topic, and the PostgreSQL [documentation page](https://oreil.ly/yAK5f) is a good place to start.

## Scenario 3

When querying, select only the necessary columns rather than performing SELECT *. This is particularly relevant when working with column-oriented databases that store data on disk column-wise. In this case, querying only a small subset of the columns will significantly improve your query speed and reduce inefficient data reads.

## Scenario 4

If you use the SQL pattern matching operator LIKE, then try to anchor the constant string at the beginning; for example, do column LIKE 'ABC%', but not column LIKE '%ABC'. With ABC%, an index such as B-tree is very likely to know which records to consider as it knows what they start with, but with %ABC, the index doesn’t know which strings end with ABC, and it might need to scan the full index. You can read more about this topic in the [PostgreSQL documentation](https://oreil.ly/EAFTa).

## Scenario 5

When processing large amounts of data, try to modularize your queries. For example, say you have a very large stock price time series table and you want to perform a given transformation on the entire table. In this case, consider using an incremental loading and processing approach instead of applying your operation to the entire table in one run. For instance, you can query your data one day or one month at a time and apply the transformations on each batch separately. The main advantage of this approach is that in case of a failure with one batch, you don’t need to query the entire dataset again.

## Scenario 6

When performing complex queries that involve joins and aggregations, make sure to process a minimal amount of data. For instance, consider a scenario where you need to get monthly transaction amounts for specific customers using two tables: transactions and customers. As illustrated in [Figure 9-1](#ch09_figure_1_1724776835082651), one way to do this is by first joining the transaction and customer tables, then aggregating the results by month and customer, and finally filtering for the desired customers. One issue with this approach is that you might join potentially large tables, which can be a resource- and time-intensive operation. A more efficient strategy would involve delaying the join operation to a later stage and applying filtering up front to reduce the queried dataset size.

### Figure 9-1. An inefficient versus efficient data processing approach

![Figure 9-1. An inefficient versus efficient data processing approach](images/fden_0901.png)

Based on your institution’s requirements and the needs of data consumers, you, as a financial data engineer, should be able to anticipate and assess additional scenarios and use cases. I recommend consistently striving to understand and discover ways to improve the efficiency of your queries. Use the EXPLAIN command to analyze the query optimizer plans, try to learn about database internals and optimization strategies, and pick up some advanced SQL knowledge.4

# Data Transformation

Once you have determined your querying strategy and optimized your database accordingly, the next step is to develop and implement your data transformations. The main purpose of data transformations is to prepare data for various use cases across your organization’s departments and teams. In this section, you will learn about the different types of transformation operations and patterns commonly used in finance, along with the computational requirements essential for their implementation.

## Transformation Operations

In its most basic form, a data transformation involves converting a raw, unprocessed dataset into a structured format suitable for its intended business application. Importantly, there isn’t a universal list of transformations that you need to apply to your data. Therefore, as a financial data engineer, one of your key responsibilities will be to discuss and define the specific transformations to implement based on business requirements and the needs of data consumers.

### Warning

Avoid applying any transformation directly to the raw data. Instead, store the raw data in an archive location and apply your transformations on a copy of the data.

I’ll provide a general overview in the following sections, outlining some of the fundamental transformations typically applied to financial data.

### Format conversion

The first transformation applied to financial data typically involves format conversion. It consists of converting the data from its source format into another format that is easier to work with. For example, you might convert data in CSV format to SQL tables, or convert data in JSON format into a collection in a document database. Once the data is converted into the desired format, subsequent transformations become easier. [Figure 9-2](#ch09_figure_2_1724776835082682) illustrates a common format conversion scenario in the financial industry, where raw data arriving in CSV or XLSX (Excel) formats is transformed into a tabular format within a relational database.

### Figure 9-2. An example of format conversion

![Figure 9-2. An example of format conversion](images/fden_0902.png)