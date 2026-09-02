### Data cleaning

Data cleaning involves the detection and correction of data quality issues such as errors, biases, duplicates, invalid formats, outliers, incorrect/corrupt values, missing data, and many others.

Data cleaning is a crucial step in the transformation layer, and it should be handled carefully. First of all, you need to make sure that all data quality issues are properly identified and understood. This assessment can vary based on your business problem; therefore, it needs to be discussed with the business team and the data consumers.5 Once an agreement has been reached, quality checks and corrective measures need to be put in place. The nature of these remedial measures is often dependent on the severity of the data quality issue. For example, in the context of fraud detection, a data outlier might signal potentially suspicious activity that should be investigated further. But if we take intraday high-frequency price data, you could easily find outliers, but they often don’t have a significant impact.

# Deciding When to Clean Financial Data

Determining when and which data to clean within your financial data infrastructure is a critical aspect of data integrity. While it may seem intuitive to perform cleaning as early as possible, this approach requires careful consideration. Often, the rationale for cleaning early is that downstream systems may struggle to identify data issues originating from upstream sources, especially if they lack the necessary contextual information to diagnose the problem.

Consider high-frequency market data as an example. While academic research often highlights the importance of data cleaning and anomaly detection for such data, advances in modern data infrastructure are reducing this need. Electronic trading has greatly reduced data anomalies, and data feed providers receive quick feedback from clients—particularly trading firms that promptly test new feeds, protocols, and connections. This immediate feedback allows for quick fixes, meaning that data feeds may not always need cleaning.

However, there are exceptions. For example, if you’re working with data from a redistributor that modifies the raw data, cleaning becomes essential. This is also the case for OTC markets or those with outdated systems. Additionally, data that requires manual entry or scraping (e.g., SEC filings) should be cleaned to ensure accuracy.

When data cleaning is applied only to historical data, but real-time data feeds are processed differently, discrepancies may occur, potentially undermining the reliability of your application and analysis. This issue arises because the cleaned historical data might not align with real-time data due to variations in the treatment of anomalies or errors.

Seen from a different angle, it’s even more effective to delegate the identification and handling of “anomalies” to downstream consumers, such as trading units. In many cases, these anomalies represent real market behavior that convey useful information. Moreover, data errors and outliers may serve as input to incorporate within your trading strategies to adapt them to handle issues like market disruptions and trading interruption events (e.g., gateway failures and failovers, trading and regulatory halts, position limit breaches, sequence gaps, circuit breakers, and order book failures).6

Generally, there are three types of actions used to clean financial data:

Deletion:   Low-quality records are deleted from the dataset. Examples include erroneous quotes, invalid prices, duplicate transactions, etc. When performing deletion, make sure to consider its impact on the analytical integrity and consistency of the data.

Correction:   Low-quality records are replaced with their correct values. For example, a negative price is replaced with a positive one. Corrections need to be based on well-thought-out assumptions about the data (e.g., a price cannot be negative). In some instances, corrections may require notifying the entity that submitted incorrect data to resubmit it in the proper format (e.g., reporting financial data that doesn’t conform to a financial messaging standard).

Enrichment:   New fields are added to assist in detecting or mitigating the impact of low-quality records. This approach is useful when errors are difficult to detect, allowing the final data consumer to decide how to handle them. For example, if outlier detection is complex, a statistical model can generate an outlier probability for each record, which is then stored in a new column.

When performing data cleaning, it is important to keep in mind the two data governance principles of lineage and ownership (which we discussed in Chapter 5). Data lineage eliminates the possibility of data cleaning becoming a mystery box by guaranteeing visibility of the cleaning steps, decisions, and rules. Similarly, data ownership ensures that only the data owners have the authority to determine and implement data cleaning procedures, which makes assigning accountability for the data quality process more straightforward.

### Data adjustments

Data adjustments are transformations applied to the data to account for specific data characteristics, events, and rules, or to produce more informative or analytically desired features.

In finance, the most frequently applied adjustment concerns [corporate actions](https://oreil.ly/gahJJ). Such actions refer to important decisions made by companies that can significantly impact their stock value. The two most common types of corporate actions are *stock splits* and *dividend distributions*. A stock split involves the issuance of several new stocks for each existing stock to increase liquidity and make it more affordable for investors to buy the company’s shares. For example, a 1:2 split means that each stock will be split in two, so if an investor holds 10 stocks, after the split they will end up with 20 stocks. A stock split does not change the total market capitalization of the company, but it impacts the stock price. To adjust for a split, the price of the stock needs to be divided by the split ratio. For example, if the price of a stock is $400 and a stock split of 1:2 takes place, the new stock price is $200.

Similarly, a dividend distribution event happens when a company decides to distribute part of its earnings to its shareholders. In such a case, the stock price needs to be adjusted to take into account the paid dividends. The standard approach to dividend adjustment consists of subtracting the dividend amount per share from the stock price. For example, if a company announces a dividend distribution equal to $1 per share, and the stock price is $11, the dividend-adjusted price will be 11 – 1 = $10.

When working with stock price data, pay particular attention to corporate action adjustments. First, determine whether the data source you are using incorporates these adjustments. Second, if the data is unadjusted, ensure this is clearly communicated and documented, and consider sourcing corporate action data separately. Some data sources, such as [CRSP US Stock Databases](https://oreil.ly/mCntU), provide both stock price data and corporate actions information. There are also specialized sources for corporate actions, such as S&P’s [Managed Corporate Actions](https://oreil.ly/Z8j7m), LSEG’s [Equity Corporate Actions](https://oreil.ly/i8w1K), and NYSE’s [Corporate Actions](https://oreil.ly/DmIzY), among many others.

Another common technique is [calendar adjustment](https://oreil.ly/ugLmQ), which modifies a financial time series to remove calendar effects. For instance, the number of working days in a month can vary each year due to holidays, making it difficult to compare total production across months. One solution is to adjust the dataset by calculating the monthly average or considering daily figures.

### Data standardization

Data standardization is a critical transformation step that seeks to store and format data according to a predefined set of conventions and standards. Examples of standardizations applied to financial data include the following:

* Date and time are formatted using the [ISO 8601—Date and Time Format standard](https://oreil.ly/hYbHP), which follows the YYYY-MM-DD convention.
* Country names are represented following the [ISO 3166—Country Codes standard](https://oreil.ly/K-_mq) (e.g., US for the United States of America).
* Currencies are represented using the [ISO 4217—Currency Codes standard](https://oreil.ly/J4mas) (e.g., USD for US dollars).
* Table and column names are lowercase, and spaces are replaced with an underscore (e.g., first\_name).
* Monetary values are [standardized](https://oreil.ly/7ovwS) to use one numerical format (e.g., EUR 10 million, EUR 10,000,000, or EUR 10000000).
* Monetary values are rounded off to a specified level of precision to ensure consistency and comparability across financial records.
* Standardized identifiers are used for financial instruments, such as ISIN or FIGI.

These standardizations help maintain data quality, facilitate data integration, and ensure compatibility across different financial systems and applications.

# How Simple Is It to Round Financial Data?

Rounding is one of the most common transformations applied to financial data. Interestingly, despite its apparent simplicity, rounding might actually require careful consideration. First of all, [a large variety of rounding algorithms exist](https://oreil.ly/kmwpb), each tailored to a specific use case. Certain methods, such as *Bankers’ Rounding*, are quite common in finance. This method aims to evenly distribute rounding errors, thereby reducing potential bias in the data. For example, 2.5 would be rounded to 2, while 3.5 would be rounded to 4.

Furthermore, deciding on the rounding precision might depend on the specific financial variable and accepted market practices. For example, a common practice is to set the rounding precision in line with the *Minimum Price Increment* (MPI), also called minimum tick size. This represents the smallest possible price change in a financial instrument’s price. MPIs vary depending on the asset class, market regulations, and the specific trading venue. For example, in the United States, the MPI is typically $0.01 for stocks priced above $1, while for stocks priced below $1, it can be $0.0001. In Forex markets, the term *Point in Percentage* (PIP) is used to denote the smallest amount by which the quote can change. A typical PIP is equal to one basis point, or 0.0001, but it can vary among trading venues and Forex brokers depending on the currency pair and the lot size traded. Following this logic, you might decide to set the rounding precision equal to the MPI; for example, an MPI of 0.0001 means a decimal precision of 4.

In addition, rounding might depend on whether you want to round ​​the decimal places or significant figures. To illustrate, let’s consider a currency pair in which one currency has a much higher value than the other, say 0.00247839. It is possible to round this number to five decimal places, in which case it becomes 0.00248. But if we want to round to five significant figures, we would get 0.0024784.

To further explore this topic, I highly recommend the book by Brian Buzzelli, [*Data Quality Engineering in Financial Services*](https://oreil.ly/QYdkg) (O’Reilly, 2022).

In today’s financial markets, a key data engineering challenge is harmonizing and standardizing the diverse data formats, structures, and types from various sources. Whether it’s market data, transactions, or external feeds, achieving consistency and interoperability is essential for accurate analysis and AI-driven insights. To give a recent example of how markets are approaching this problem, J.P. Morgan’s Fusion, a cloud-native data platform for institutional investors, launched data containers in May 2024. These containers use a common semantic layer to model and normalize data across multiple providers, sources, and formats—giving investors a consistent, integrated view of their data.

### Data filtering

Data filtering is an analytical transformation step whereby a financial dataset is examined to exclude or rearrange its records according to predefined criteria. In other words, data filtering applies a filter to a dataset, transforming it into a new dataset based on the filter criteria.

A wide range of data filters are used in finance. Here are a few examples:

Company filter:   This consists of excluding companies from a financial dataset that don’t satisfy certain conditions. For instance, an [article written by Priyank Gandhi and Hanno Lustig](https://oreil.ly/88XFm) details a study using the CRSP dataset, excluding inactive firms (legal entities without business activities) and firms incorporated outside the US to ensure a uniform regulatory regime.

Calendar filter:   This filter is used to align accounting standards across firms in a dataset. For example, in an [article written by Laura Xiaolei Liu and Lu Zhang](https://oreil.ly/nKxIK), they excluded firms that do not have a December fiscal year-end.

Liquidity filter:   This filter is used to ensure that the securities included in a data sample have at least a certain number of active trading days during a specific time interval. In one [research paper](https://oreil.ly/F-qjO), the authors applied a filter to exclude stocks with less than two hundred days of active trading in a year to have a sample with enough data for computing liquidity measures. Similarly, when working with option data, it is common to filter out options whose expiration falls outside a given interval (e.g., between 10 and 400 days) as such options might behave erratically near expiry due to liquidity features (the article [“The Puzzle of Index Option Returns”](https://oreil.ly/6AJQX) provides a good example).

Size filter:   This filter excludes firms whose market capitalization is below or above a certain value, for example, when studying a specific segment of the market. In one [study](https://oreil.ly/HNhEA), the authors excluded microcap stocks, defined at the fifth percentile of market capitalization within each country. This was done because minicap stocks often suffer from stale prices and volumes due to market illiquidity as well as their negligible economic significance (<0.04%) on the overall market value.

Coverage filter:   This filter excludes firms that do not have enough observations in the dataset. This is often done to reduce the impact of noise generated by such observations. For example, the authors of a [study on factors that drive global stock returns](https://oreil.ly/nmn_S) applied a similar filter by requiring a stock to have at least 12 monthly observations within the sample period to be considered for inclusion in the study.

Sector filter:   This involves including entities belonging to a particular sector, market segment, industry, or subindustry. This filter is applied because certain sectors can be subject to special regulation or have different asset and investment structures. For example, in their seminal work, *The Cross-Section of Expected Stock Returns* (Wiley), Fama and French conducted their analysis by excluding financial firms, as high leverage for these firms does not indicate the same thing for nonfinancial firms, i.e., distress.

When applying data filters, it’s essential to understand their purpose and the potential impact on data quality and integrity. Improper filtering can introduce biases, such as nonrepresentative sample bias or imbalanced datasets. As a financial data engineer, you should discuss these considerations with the end users of the data. Additionally, ensure that filters are applied correctly and do not modify or delete the original data. If a filtered dataset is needed, create a new table for it.

### Feature engineering

Feature engineering is an advanced analytical transformation step used to extract new features from raw data to support statistical and machine learning modeling. Feature engineering is often necessary when existing features do not adequately represent the problem at hand. A feature is a variable or measurable quantity used as input in various modeling tasks. It can be numeric, categorical, binary, or text based. In database terms, a feature can be thought of as a new column in a given table. It is a well-known empirical fact that [the performance of machine learning systems is heavily dependent on the feature representation of the input data](https://oreil.ly/mggoX).

The practice of feature engineering is quite flexible; data analysts and machine learning experts have the freedom to experiment with and derive novel features from a given dataset to represent different aspects of the data that are relevant to the situation at hand.

Feature engineering can be data driven (e.g., based on statistical correlations or patterns in the data) or domain driven (e.g., based on a financial theory). Moreover, feature engineering requirements may vary based on the type of data being analyzed. For example, there is feature engineering for text data, visual data, time series data, graph data, and stream data. A full account of these techniques is beyond the scope of this book, and for this, I recommend the excellent reference *Feature Engineering for Machine Learning and Data Analytics*, edited by Guozhu Dong and Huan Liu (CRC Press, 2018). Nevertheless, to give it a minimal treatment, let’s go through some examples of feature engineering.

The most general techniques for feature engineering include the following:

Normalization:   Rescaling the data to fit within a predefined range, e.g., [0–1]. This is often done to prevent some features from having a dominant impact during model training.

Scaling:   Rescaling the data to have a similar scale, such as a standard deviation of 1, to ensure a model considers all features equally. Common scaling techniques include *min-max scaling* and *standard scaling*.

Encoding:   Transforming a feature from categorical to numerical representation; e.g., female is 1 and male is 2. Common encoding techniques include *one-hot encoding* and *label encoding*.

Dimensionality reduction:   Transforming a set of features from a high-dimensional space into a lower-dimensional one. Examples include *principal component analysis* and *t-SNE*.

Embedding:   A technique used to create numerical representations of complex real-world objects that machine learning systems can use in model training. As an illustrative example, an embedding might take an image, audio, text, or a graph and convert it into multidimensional numerical representations known as vectors. Using vectors, machine learning systems can efficiently process input data and identify similarities among different data items (e.g., two similar images). A special type of database, called a [vector database](https://oreil.ly/cu6ry), has been developed to allow ML-driven applications to store and retrieve vector datasets.

In finance, a wide range of domain-specific feature engineering techniques are often applied. For example, when conducting financial time series analysis, it is common to perform steps such as *de-trending* and *de-seasonalization.*7 De-trending is the process of removing a trend cycle from the data. A trend cycle refers to a consistent increase or decrease of a financial time series over time. On the other hand, de-seasonalization removes seasonal patterns from the time series. A seasonal pattern refers to a specific event in the time series that occurs with a fixed and known frequency such as daily, weekly, every January, etc.8 By applying de-trending and de-seasonalization, new features are created.

Another widely used technique in finance is stationary differentiation. This involves calculating the difference between each consecutive pair of observations over time (i.e.,

x t - x t-1, x t-1 - x t-2,.... ). It is commonly used to transform a non-stationary financial time series into a stationary one. In simple words, a stationary time series is a series whose statistical properties do not change time. Stationarity is a desired property, as it makes it simpler to perform data analysis using classical statistical methods (e.g., inferential statistics). Converting a price time series to a return series is one such application of differentiation that financial analysts often perform. This is done by taking the percentage difference between two consecutive prices (i.e.,

( x t - x t-1 ) / x t-1 ).9

In addition, a popular feature engineering technique applied by financial analysts is log transformation, where each value x is replaced with log(x). Expressing data on a logarithmic scale can be helpful for analytical purposes. For example, if a price time series is expressed in a log scale, the difference between two log prices approximates the percentage change (i.e.,

l o g

( p t ) - l o g

( p t-1 ) ∼

( p t - p t-1 ) / p t-1 ). Furthermore, the log transformation is frequently used to transform skewed financial data to conform to normality, which is a desired feature in financial analysis.10

Finally, an advanced form of feature engineering in finance is the creation of factors. In financial investment literature, “factors” refer to common asset characteristics that explain variations in returns and risks across stocks, bonds, and other assets. They can explain why certain assets go up or down at the same time and why certain assets may yield higher returns compared to others.

There are two main types of factors: macroeconomic factors and style factors. Macroeconomic factors capture risks that affect broad segments of the financial markets and impact multiple asset classes simultaneously. Examples include interest rate (the impact of interest rate changes), inflation (the effect of price level changes), and economic growth (variations in the business cycle). Style factors, on the other hand, explain returns and risks within individual assets or asset classes. Examples include value (assets undervalued relative to their fundamentals), momentum (assets with upward price trends), low volatility (assets with a lower risk profile), quality (assets of financially robust companies), and growth (assets or companies with strong earnings growth potential). These factors are engineered features derived from fundamental or market data to enhance portfolio returns and manage risk.11

### Advanced analytical computations

An advanced type of data transformation may involve the computation of one or more quantities based on an algorithm or a model. Generally speaking, financial data engineers seldom perform scientific modeling or develop machine learning algorithms. However, with the rise of data products, data platforms, and analytics engineering, there are contexts where financial data engineers, particularly those with interdisciplinary backgrounds, might become involved in the modeling process.

Examples of financial applications that require advanced computations include the following:

* Algorithmic trading
* Financial recommender systems (e.g., robo advisors)
* Fraud detection
* Anti-money laundering
* Named entity recognition
* Entity resolution
* Optical character recognition (e.g., recognizing the digits on a credit card image)

To develop such systems, financial data engineers may need to handle tasks such as data collection, cleaning, quality assurance, and control checks. They are also responsible for selecting suitable DSMs and DSSs tailored to each application’s requirements. Furthermore, financial data engineers may be involved in building machine learning pipelines, deploying them in production, and collecting metrics and model artifacts.

## Transformation Patterns

The next stage after defining your transformation operations is to design and implement your transformation patterns. A transformation pattern defines how a given data infrastructure handles and performs transformations. To illustrate the concept, let’s have a look at a few examples.

### Batch versus streaming transformations

In batch transformation, data is divided into discrete chunks (batches) that undergo separate processing. A data chunk can be defined in various ways. For instance, if data is received in file formats like CSV or JSON, each file can be treated as a chunk and processed individually. Alternatively, if the files can be grouped based on specific criteria (e.g., by date), a chunk might encompass all files belonging to a particular group (e.g., all files for a given day). Batch file transformation is a common practice in finance, especially when data is delivered through files. Examples include financial data vendors, which distribute their data in daily, weekly, and monthly file batches, and financial reporting, which is often done via files submitted to the regulator’s data infrastructure.

Batch transformations are often used with scheduled data arrival processes, which we discussed in Chapter 7. In this case, the batch transformation is scheduled to run on a predefined interval (e.g., hourly, daily, weekly). Alternatively, a batch can be transformed once it is complete. For instance, a file batch with a maximum size of 10 will be transformed when it contains 10 files.

When data needs to be transformed as soon as it arrives, and not wait for a batch to complete, then a *streaming transformation* is used. In this case, there is no fixed schedule for data transformation; it runs continuously and processes data immediately upon its arrival. Streaming transformations are most commonly used with event-driven arrival processes, which were also covered in Chapter 7. This is the case, for example, with real-time financial applications such as payments, fraud detection, price feeds, and news. In these applications, the system needs to respond with minimum latency and, therefore, cannot wait for a batch to complete.

Streaming transformations are often performed on independent data. For instance, in a scenario where a bank allows clients to submit loan applications online, each application can be processed immediately upon submission, without the need to wait for other applications to form a batch.

In certain scenarios, data arrival may occur in real time or be event driven, yet streaming transformation may not be necessary. For instance, when bank clients fill out a questionnaire to evaluate their financial literacy, the data does not require immediate processing. Instead, it can be processed in batches at regular intervals or as soon as a batch is complete. Using batch transformation to process real-time or event-driven data is a common practice employed to handle massive volumes of data or reduce the costs of continuous monitoring for new data arrivals.

[Figure 9-3](#ch09_figure_3_1724776835082703) illustrates how batch and streaming transformations work. In batch transformation (top), data files arrive and get ingested into a data lake. Subsequently, files are grouped in separate batches based on date. After that, each batch is transformed separately in the transformation layer. Once transformed, the data is stored in a given target location, such as a warehouse. In the streaming transformation case (bottom), data arrives in JSON format. Each JSON gets immediately ingested into a message broker. Subsequently, each message is processed as soon as possible in the transformation layer and stored in the final data warehouse.

### Figure 9-3. Standard batch and streaming transformation patterns

![Figure 9-3. Standard batch and streaming transformation patterns](images/fden_0903.png)

### Memory-based versus disk-based transformations

A given data transformation, whether batch or streaming, can be processed either completely in memory or involving intermediary disk persistence steps. The best way to show the difference is with an illustrative example, as shown in [Figure 9-4](#ch09_figure_4_1724776835082722). A basic disk-based transformation is illustrated in the figure’s upper part. In this setting, files are first ingested into a data lake. Subsequently, the transformation layer applies two transformation iterations on the files (e.g., cleaning + feature engineering) and saves the final results in a data warehouse. Note, however, that between the two iterations, the transformation layer had to store intermediary results back to the data lake and read it again for the second iteration. In the lower part of the figure, a memory-based transformation does the same thing, but instead of saving intermediary results to the data lake, it keeps it in memory and passes it as such to the next interaction.

### Figure 9-4. Disk-based versus memory-based data transformations

![Figure 9-4. Disk-based versus memory-based data transformations](images/fden_0904.png)

You might be wondering by now why this is necessary. The answer lies in the significant difference in data access speed between RAM and disk (random disk access, to be precise). This is the reason why in-memory software solutions for data storage and processing are quite popular.12

Many financial applications rely on memory-based data transformations, especially in time-critical scenarios like trading and fraud detection. For instance, in high-frequency and algorithmic trading, real-time data from feeds is processed directly in memory for immediate action. If data were to be stored on disk first, then the speed advantage would be lost.

### Note

Disk-based access modes don’t all operate slowly. When compared to RAM access, random disk access—where data is retrieved at random locations on disk—is especially sluggish. Sequential disk access, on the other hand, is very quick since data records are retrieved in a predetermined order. Sequential disk access is leveraged by technologies like [Apache Kafka](https://oreil.ly/EnkF1) in order to achieve high-performance data read/write operations.