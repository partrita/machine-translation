## Dimension 3: Data Biases

Data biases refer to inherent distortions that impact the representation of the subjects/entities that constitute the data. These biases can result in erroneous conclusions, skewed patterns, biased decisions, and discrimination.

A large number of biases may emerge in financial data. To illustrate with an example, let’s say you want to analyze the performance of fund managers (a common area of study in finance) and get a dataset for your study from a data provider. Interestingly, many commercial fund datasets are collected via a voluntary reporting mechanism. In this setting, fund managers may or may not decide to report their performance highlights to the data vendor.

For instance, when a fund performs well, and the manager aims to attract more capital, they may disclose its figures to draw market attention. Conversely, if the fund underperforms or the manager prefers not to attract new investors, they might opt not to report the performance figures. This kind of behavior might lead to self-selection bias. Such bias will distort the dataset and give the impression that some funds are always outperforming.

As institutional investors, hedge funds are exposed to a number of risks, and in some cases, this might lead to failure/bankruptcy. If a hedge fund dataset systematically excludes/removes failed or poorly performing funds from its archive, this could lead to a type of bias called *survivorship bias,* where only the successful funds appear in the dataset. Similar to self-selection bias, survivorship bias may convey an over-optimistic image of the fund industry’s performance.

In some cases, a new hedge fund could be added to the dataset together with its full history. Even though it looks natural, this behavior might lead to *backfilling* bias, also known as *instant history bias*. This bias can be relevant if only funds with a strong track record choose to join the database, which would distort historical performance statistics for the hedge fund industry.

Another significant bias in financial data is *look-ahead bias*, which occurs when conducting historical studies using information that would not have been accessible during the analyzed period. For instance, consider a scenario where a company releases its annual report for the year 2019 in March 2020, as is typically the case. Suppose you’re a financial analyst conducting backtesting to evaluate your investment strategy’s performance. In that case, it’s crucial to avoid assuming that the company’s annual report was available before March 2020 (e.g., December 31, 2019), even if you’re analyzing data from a later date.

Detecting and correcting biases in financial data is a challenging task. As a financial data engineer or analyst, make sure you understand how the data was generated and recorded. Consider collecting more data to adjust for possible biases. Furthermore, if you are extracting a data sample from a large dataset, design a methodology that proactively prevents biases, for example, by assessing the data sample representation. Another good practice is to compare two datasets to check for potential bias that exists in one but not the other.10 Finally, I highly recommend keeping an eye on the latest research on bias and fairness in data analysis and machine learning.11

On the data vendors’ side, efforts have been made to detect and correct biases in their products. For example, among the most reputable hedge fund data sources is LSEG’s [Lipper Fund Data](https://oreil.ly/N0eMI), formerly known as the *Trading Advisor Selection System* (TASS) database. Lipper tracks and publishes fund-related information such as its profile, performance, and investment strategies. Funds report to Lipper voluntarily, which, as we saw earlier in this section, can lead to various biases. To account for this issue, Lipper keeps two separate databases: the *graveyard* database, which records data on defunct funds or funds that haven’t been reported for a long time, and the *live* database, which records data for actively reporting funds.12

## Dimension 4: Data Granularity

Data granularity describes the level of detail within a dataset, with highly granular data offering detailed observations about individual entities, while low-granularity data typically provides summarized or aggregated information at a higher level. To better illustrate the concept within the finance domain, let’s consider a few examples:

Financial portfolios:   A financial portfolio is a collection of investments created to achieve a specific financial goal, considering elements such as diversification, risk appetite, and expected returns. Portfolio data can be available either in aggregated form, providing an overview of portfolio performance, risk, and investment strategy, or in a more detailed form, including details about individual portfolio constituents and their respective allocations, such as Apple stock at 5%, US government bonds at 20%, and so on.

Financial indices:   A financial index is a single aggregated metric constructed to represent and track the performance of a specific category of financial assets. For example, the S&P 500 index offers an aggregated metric of the top 500 public companies in the United States by market capitalization. Index data may be available at the index level (single metric) or at the constituent level (the individual assets included in the index and their corresponding weights).

Financial exposures:   Financial institutions hold assets with each other, such as interbank loans, securities, and cash. A financial institution might disclose its total exposure to another institution at the aggregated level (Bank A holds $1bln assets with the rest of the system) or at the individual institution level (e.g., Bank A holds $1mln at Bank B, $33mln at Bank C, and so on).

Financial time series:   These can be recorded with high temporal accuracy, such as every second, minute, or hour, or with lower granularity, such as daily, weekly, or monthly aggregates.

Financial transactions:   These can be stored at the individual transaction level or as summaries, such as monthly purchases.

The level of data granularity is an essential factor in determining the type of analysis that can be performed on the data. Highly granular data enables deeper insights and the identification of meaningful patterns utilizing advanced analytical approaches. Importantly, granular data comes with increased storage requirements, processing time, and the potential for privacy concerns. Therefore, it is recommended to keep in mind the challenges and tradeoffs associated with managing and analyzing highly granular data.

Granular financial data may not always be available. Portfolio composition data, for example, may not be disclosed since it would reveal the firm’s investment strategy, which might harm its competitive position. Another reason this information may be withheld is data confidentiality, like with customer transaction details. In some cases, detailed data may not be collected in the first place, for example, in noncentralized markets such as OTC markets.

To overcome the issue of data granularity, you can try to collect detailed data. Alternatively, aggregated data may be decomposed into its constituent elements using statistical and machine learning techniques. For example, network scientists who analyze financial networks are often limited by privacy issues when collecting data about the topology of a financial network. As mentioned earlier, the best example is banks’ exposures to each other, where data is available at the aggregate level only. To overcome this issue, researchers have proposed [network reconstruction](https://oreil.ly/vXWdd) and [link prediction](https://oreil.ly/avoq0) methods to infer and construct the network structure at the bank-to-bank level.

## Dimension 5: Data Duplicates

Data duplicates are repeated records that represent the same data observation. Duplicate data is a widespread issue in finance, and its consequences can range from negligible to severe. For example, a duplicate record in a data sample used in a financial study may not lead to serious consequences; however, if a financial transaction appears multiple times on a user account, then it might impact the available balance.

Data duplicates may occur for a variety of reasons. First, there are human errors, which happen when a person adds the same data entry into a system multiple times. Second, duplicates may be inserted automatically by a machine when the system is not properly built to ensure data uniqueness. For example, a household submits a loan application twice. Third, data duplicates might emerge when merging multiple data sources improperly, for example, using nonunique identifiers.

Crucially, despite the apparent simplicity of the problem, detecting duplicates may be quite challenging. In the simplest case, a data record is considered duplicate if the values of all its fields exactly match those of another record. For example, two financial accounts are considered duplicates if they match the account holder’s first name, last name, social security number, and account number. In a more complex scenario, two duplicate records may be recorded differently, thus making it harder to identify. For example, if names are recorded with different formatting (e.g., J.P. Morgan versus JPMorgan), then the duplicate records would have a nonperfect match. In other cases, the presence of exact duplicates may be due to inconsistency in the data recording mechanism. For example, an investment of $10,000 in stock A may be recorded as an investment of $5,000 in stock A twice, while an investment of $10,000 in stock B is recorded only once.

Detecting and treating duplicate records can also vary in complexity. The best strategy is to always think in advance about the duplicate generation mechanism and add the necessary checks, constraints, and validations to prevent duplication. For example, having a well-defined unique identifier for each record is a good practice. If the unique identifier is not sufficient, then it is possible to add constraints on a subset of data fields that ensure no two records share the same set of values. Let’s walk through an example of how to prevent duplicates before data insertion in PostgreSQL:13

```
-- PostgreSQL
CREATE EXTENSION btree_gist;
CREATE TABLE company(
   record_key INT PRIMARY KEY,
   company_id VARCHAR NOT NULL,
   company_name VARCHAR NOT NULL,
   dividend_date DATE NOT NULL,
   dividend_amount DECIMAL(10,2) NOT NULL,
   EXCLUDE USING gist (company_id WITH =, company_name WITH <>)
);
INSERT INTO company VALUES(1, 'JPM', 'JP Morgan', '2020-11-20', 10);
INSERT INTO company VALUES(2, 'BOA', 'Bank of America', '2022-01-08', 5);
INSERT INTO company VALUES(1, 'JPM', 'JP Morgan', '2019-05-01', 8);
INSERT INTO company VALUES(3, 'JPM', 'J.P. Morgan', '2023-06-01', 3);
```

```
psql:commands.sql:12: ERROR:  duplicate key value violates unique constraint "company_pkey" DETAIL:  Key (record_key)=(1) already exists.
psql:commands.sql:12: ERROR:  conflicting key value violates exclusion constraint "company_company_id_company_name_excl"
DETAIL:  Key (company_id, company_name)=(JPM, J.P. Morgan) conflicts with existing key (company_id, company_name)=(JPM, JP Morgan).
```

In this example, we created a table that stores data on company dividend distributions. Each company has a unique ID and a human-readable name, while each record has a unique record key. We want to avoid having two records with the same record key or the same company ID but with a different company name. To achieve this, we can add a primary key constraint on the record key field and an *exclusion constraint* on the company ID and company name. After that, we test the implementation by trying to make four inserts, two of which violate the two constraints.

The first two insert statements will execute successfully, and two records will be created. However, for the third statement, we will get an error that says the uniqueness constraint was violated as they share the same record key (= 1). For the fourth insert, we will get an error saying that you are trying to insert a record with a new format (J.P. Morgan and JP Morgan).

If data has already been generated and stored with potential duplicates, then a variety of solutions are possible. In the simplest case, duplicates share the same field values. To identify them, we can use aggregation or analytical queries. Let’s consider the following example:

```
-- PostgreSQL
-- create
CREATE TABLE company (
  company_id INTEGER PRIMARY KEY,
  company_name VARCHAR,
  company_headquarters VARCHAR
);

-- insert
INSERT INTO company VALUES (1, 'Company A', 'New York');
INSERT INTO company VALUES (2, 'Company B', 'California');
INSERT INTO company VALUES (3, 'Company A', 'New York');

-- fetch
SELECT company_name, company_headquarters, count(company_id) AS record_count
FROM company
GROUP BY company_name, company_headquarters
```

```
 company_name | company_headquarters | record_count
--------------+----------------------+--------------
 Company B    | California |            1
 Company A    | New York |            2
```

In the above table, two duplicates store the same data for Company B. To detect these duplicates, we used a GROUP BY statement that counts the number of records that share the same company name and company headquarters.

The GROUP BY is an aggregation tool that reduces the number of rows to summary groups. If we want to keep the original data without aggregation, we can use a window function such as [ROW_NUMBER()](https://oreil.ly/SJLSW) to assign an ordered sequential number to each record in a group. This way, deduplication can be performed by taking the records with row_num = 1 and discarding those with higher row numbers. Here is an illustrative example:

```
SELECT company.*,
ROW_NUMBER() OVER (PARTITION BY company_name, company_headquarters) AS row_num
FROM company
ORDER BY company_name, company_headquarters, row_num
```

```
 company_id | company_name | company_headquarters | row_num
------------+--------------+----------------------+---------
          1 | Company A    | New York |       1
          3 | Company A    | New York |       2
          2 | Company B    | California |       1
```

A more challenging scenario occurs when a dataset contains duplicates, but they cannot be directly identified due to data quality issues. For example, we might know the subset of columns that could identify duplicates, but the data may be recorded differently, so it won’t be detected via an exact match. In this case, the data deduplication process becomes an entity resolution (data matching) task. We discussed entity resolution systems in Chapter 4. One thing to keep in mind is that data deduplication is a [special type of entity resolution](https://oreil.ly/Bf64q), as it involves only one dataset that is matched against itself to resolve similar entities.

Another subtle scenario with duplicates happens when two records look the same, but they are not duplicates because a distinguishing field is missing. Examples include transaction data where the date of the transaction is available but the time is missing; multiple data at the security level (e.g., company stocks) that look like duplicates but, in reality, refer to different security issues (e.g., different stock issues) that are missing issue IDs; or a financial option is available twice, but one is a call (buy-side), and another is a put (sell-side).

## Dimension 6: Data Availability and Completeness

A crucial dimension of data quality is the completeness of a dataset, indicating whether it contains all necessary information required for its intended analytical or operational purposes. A dataset is considered incomplete or unavailable when essential data attributes or observations are missing. In finance, issues of data availability and incompleteness are quite [common](https://oreil.ly/EMS9m). This happens for a variety of reasons, such as the following:

Voluntary data reporting:   If the data collection process involves a voluntary data reporting mechanism, e.g., survey data, then it is likely that some respondents will decline to report their data for one reason or another, e.g., to hide bad performance. Additionally, respondents might report data with different frequencies (e.g., Firm A responds to all surveys, while Firm B responds to some and skips others).

Security and confidentiality concerns:   Unless enforced by law, financial firms might have a number of concerns about the security and confidentiality of their data. This might generate a high level of risk aversion toward data sharing.

Market factors:   Market factors such as liquidity, sentiment, and risk might impact the data generation process. For example, a liquid stock that trades frequently will have a large number of price observations per day, while an illiquid instrument might trade once every six hours and have a few daily records. This type of behavior is called [nonsynchronous trading](https://oreil.ly/CEymv).

Technological reasons:   If a financial firm or the market lacks adequate data collection infrastructure, it can lead to data collection gaps. For instance, a considerable amount of data on over-the-counter (OTC) market transactions remains unrecorded due to the absence of a centralized entity responsible for collecting and aggregating such data.

Publication delay:   If there is a latency between the time data is created and the time it is published, it could be considered unavailable. This might happen with company fundamental data, created at the end of the fiscal year but released a few months later.

Data Time to Live (TTL):   TTL is a database mechanism that sets a period of time after which data will be considered expired and no longer visible to queries and database statistics. TTL doesn’t necessarily mean that the data was deleted, as this might happen at a later point in time.

In certain circumstances, the existence of a specific type of data may be optional; in these situations, the consequences of missing data are minor and may not require any correction effort. However, in many cases, incomplete or missing data can cause a number of problems for financial institutions. For example, missing data may lead to biased and unreliable financial models, which in turn can impact investment decisions and product development. Incomplete data may also mean less visibility and insight into market activities and patterns, thus foregoing potentially profitable opportunities and reducing trust in the data within a financial institution. Gaps in customer-related data may impact the business and sales teams’ ability to understand consumer segments and offer personalized services. Moreover, missing data may delay reporting and releases, which can impact market sentiment and expert estimations.

To effectively deal with missing financial data, it is crucial to understand the mechanisms that cause data missingness. Following the [existing literature](https://oreil.ly/5xfqc), three forms of missing data are often discussed:

Missing Completely at Random:   Data on variable *X* is said to be Missing Completely at Random (MCAR) if the mechanism that leads to observations of *X* being missing is independent of *X* itself and any other variable in the dataset, whether observable or missing. The missingness happens randomly and without any systematic pattern. For example, a hedge fund that reports its performance data to a data provider might incur a technical issue preventing some of its data from being submitted.

Missing at Random:   If data on variable *X* is Missing at Random (MAR), then the missingness mechanism is independent of *X* itself but is systematically related to one or more features in the dataset. For instance, a hedge fund firm might opt not to disclose performance data due to confidentiality concerns surrounding its investment strategy. Here, the missingness is unrelated to the fund’s performance but rather to its investment secrets.

Missing Not at Random:   This happens when observations on variable *X* are missing for reasons related to *X* itself. To continue with our example, a hedge fund might decide not to report its performance data because it had a bad performance and wants to hide it from investors or because they are doing very well and they don’t want to attract more investors or media coverage.

A variety of techniques have been [developed for treating missing financial data](https://oreil.ly/6lGnq). The simplest and most common technique is *likewise deletion*, where observations with missing data are removed from the dataset. Another technique is the *omitted variable approach*, which drops the variable with missing values from the dataset. In some cases, dropping observations or variables might lead to biased or sparse datasets. A family of techniques called *imputation* is often used to overcome this issue. Imputation aims to estimate the missing values in a dataset using a specific method. One basic imputation technique is the *mean substitution*, which replaces missing values for variable *X* with the average value of *X*. Another imputation technique is filling in a missing value in one dataset with another value in another dataset, e.g., via entity resolution. Last but not least, a practical approach to data imputation is regression, where a model is used to produce an estimate of the missing value. Models can be machine learning based (e.g., linear regression) or financial models (e.g., Capital Asset Pricing Model, Value at Risk, etc.).

## Dimension 7: Data Timeliness

Timeliness of data is a critical dimension of data quality within financial institutions. This section will discuss two key aspects related to data timeliness:

* Is the data available and accessible at the time it is expected to be?
* Does the data reflect the most recent observations?

Many financial datasets are used in a time-critical context, e.g., algorithmic trading, and if data is not available in the expected window, then the data is of no use. On the other hand, if the available data does not reflect the latest facts, e.g., the latest Forex quote or the latest analyst estimate, then it might lead to wrong business decisions and lost revenues. Financial markets use the term *stale price* to describe an outdated or no longer accurate quoted value of a financial asset or instrument.

A variety of factors may influence financial data timeliness. The most common factors are latency, market closure, time lags, or lengthy processes in the data generation, ingestion, and transformation mechanisms. For example, complex data pipelines are likely to be time-consuming and delay data availability. Another factor is the data *refresh rate*, which is the frequency with which data is refetched and updated to reflect the latest observations. Refresh frequencies may vary from real time to regular schedules.

Furthermore, many applications rely on *data caching*, a strategy where a copy of the data is stored in a temporary storage location that allows fast access. However, cached data can become outdated over time, requiring periodic updates or replacements to ensure alignment with the most recent data. This problem, known as *cache invalidation*, poses one of the most common [challenges in software development](https://oreil.ly/jCOIG).

## Dimension 8: Data Constraints

The data constraints dimension reflects the degree to which data conforms to predefined technical and business rules and limitations. Examples of such constraints include the following:

Extension constraint:   Data is stored in allowed formats only (e.g., CSV files).

Schema constraint:   Data follows a predefined schema structure that defines the mandatory fields and their data type.

Non-null constraint:   A data field does not contain null values.

Range constraint:   A data field contains values that fall within a given range (e.g., price >=0, year >=1990).

Value choice constraint:   A field can assume values from a fixed list of choices (e.g., country names).

Uniqueness constraint:   A record must be unique across a dataset.

Referential integrity constraint:   Values in one field are allowed only if they exist in another referenced field. For example, an online purchase transaction cannot be stored if it contains a nonexistent product.

Regular expression patterns:   A field contains values that match a given string pattern (e.g., an email pattern, a financial identifier pattern).

Cross-field validation:   This ensures that a field satisfies a certain condition in relation to one or more fields. For example, the date of issuance of a derivative contract cannot be earlier than the date of expiry.

Based on your business needs, additional constraints may be defined. An important thing to remember is that violating a given constraint may not always signal a bad data quality issue. For example, a schema change that involves adding or deleting a given field might be done to enrich data quality and correct existing errors. As another example, a value choice constraint may be violated if the list of allowed options is outdated.

## Dimension 9: Data Relevance

Data relevance is an important data quality dimension, determining the degree to which available data aligns with the specific problem or purpose it aims to address. Relevance ensures that the data is actionable and contributes effectively to gaining insights and understanding the problem at hand. For example, in his interesting analysis published in *Getting It Wrong: How Faulty Monetary Statistics Undermine the Fed, the Financial System, and the Economy* (MIT Press, 2011), William Barnett illustrates how the lack of adequate financial data to assess financial systemic risks has been identified as one of the main factors leading to the great financial crisis of 2007–2008.

In the following years, several initiatives have been launched to review and enhance the data collection processes in financial markets. For example, in 2020 the Bank of England conducted a [Data Collection review](https://oreil.ly/3XLLR) to identify the challenges the industry faces in providing data, the issues the bank encounters in receiving and using it, and the necessary steps to address these problems. As another example, in response to the significant impact of swaps, especially credit default swaps, during the 2007–2008 financial crisis, the Dodd-Frank Wall Street Reform and Consumer Protection Act (Dodd-Frank Act) established [*swap data repositories* (SDRs)](https://oreil.ly/4gtMz) to serve as entities responsible for swap data reporting and recordkeeping. According to the Dodd-Frank Act, all swaps, whether cleared or uncleared, must be reported to registered SDRs.

In recent years, the importance of data relevance has increased alongside the rise of machine learning and generative AI. If the available data features (variables) are not pertinent to the analytical problem or do not provide insights into the patterns analysts aim to capture, developing accurate models becomes challenging.14 Similarly, fine-tuning a language model requires contextual data that matches the specific requirements and conditions of the task or problem at hand.

The question of what data is relevant is ultimately a function of the problem at hand. For example, investment firms may employ a range of trading strategies, each of which requires different types of data. For instance, *day trading* demands real-time intraday price, volume, volatility, and market liquidity data. *Swing trading* relies on technical and fundamental indicators, market sentiment, and medium-term price trends. *Trend trading* depends on moving averages, trend lines, and momentum indicators. *Arbitrage trading* needs data on order books, market liquidity, transaction costs, trading fees, real-time price discrepancies, and Forex rates. *Mean reversion trading* uses data on moving averages, Relative Strength Index (RSI), Bollinger Bands, and Moving Average Convergence Divergence (MACD); *systematic trading* requires time series data for transactions (price and volume), orders, and news (economic releases and events).15

# Data Integrity

Throughout its lifecycle, data goes through a number of transformations, movements, and adjustments as well as aggregation, matching, and more. In this context, the concept of *data integrity* is often used to indicate a set of principles established to ensure consistent, traceable, usable, and reliable data. Depending on the institution type and business requirements, there may be a number of ways data integrity could be ensured. To offer a general overview, this section outlines nine key data integrity principles—standards, backups, archiving, aggregation, lineage, catalogs, ownership, contracts, and reconciliation—all of which hold significant relevance within the financial sector.

## Principle 1: Data Standards

As financial markets have grown in size and complexity, the terms *standard* and *standardization* have become keywords. According to authors Spivak and Brenner in their book *Standardization Essentials* (CRC Press, 2001), the term standard “denotes a uniform set of measures, agreements, conditions, or specifications between parties.” The process of formulating, developing, and implementing standards is called standardization. Standards differ in their nature, function, and acceptance. Spivak and Brenner provide a general framework by categorizing standards into the following taxonomy:

* Physical standards or units of measure
* Terms, definitions, classes, grades, ratings, or symbols
* Test methods, recommended practices, guides, and other applications to products and processes
* Standards for systems and services, in particular, quality standardization and related aspects of management system standards for quality and the environment
* Standards for health, safety, consumers, and the environment

Financial industry participants have [made several calls for standardization](https://oreil.ly/ZoCQI), acknowledging its role in increasing market efficiency, confidence, and stability and reducing costs. For example, [research conducted by McKinsey](https://oreil.ly/PYotd) found that the adoption of the Legal Entity Identifier standard (which we discussed in detail in Chapter 3) could save the global banking industry around USD $2–4 billion annually in client onboarding costs.

Furthermore, standards play a crucial role in financial markets by promoting consistency across key aspects of processes, products, and services, including quality, compatibility, interoperability, comparability, and reliability. For instance, the [ISO 21586 standard](https://oreil.ly/c6FeC), which specifies the description of banking products or services, was introduced to ensure uniformity in descriptions of banking products and services (BPoS) across various financial institutions, enabling customers to understand and compare them effectively.

Furthermore, as domain experts develop standards, they distill best practices and codify the most recent technologies and expertise, which saves market participants the effort of reinventing the wheel. A few great examples of this are accounting standards (e.g., *generally accepted accounting principles*, or GAAP), risk management standards (e.g., value at risk, or VAR), and data quality standards (e.g., ISO 8000: Data Quality).