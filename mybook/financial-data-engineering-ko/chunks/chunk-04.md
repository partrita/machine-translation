# Case Study: Morningstar Data Acquisition Process

[Morningstar, Inc.](https://oreil.ly/z8IVA), is a well-known financial data vendor that collects, analyzes, and provides financial market data, in particular stock and fund data. In [one of their 8-K filings](https://oreil.ly/Jc-P2), Morningstar experts provided a detailed overview of their data collection and acquisition process. Here’s an excerpt from the original filing:

> We [Morningstar] collect most of our data from original source documents that are publicly available, such as regulatory filings and fund company documents. This is the main source of operations data for securities in our open-end, closed-end, exchange-traded fund, and variable annuity databases, as well as for financial statement data in our equity database. This information is available at no cost.
>
> For performance-related information (including total returns, net asset values, dividends, and capital gains), we receive daily electronic updates from individual fund companies, transfer agents, and custodians. We don’t need to pay any fees to obtain this performance data. In some markets we supplement this information with a standard market feed such as Nasdaq for daily net asset values, which we use for quality assurance and filling in any gaps in fund-specific performance data. We also receive most of the details on underlying portfolio holdings for mutual funds, closed-end funds, exchange-traded funds, and variable annuities electronically from fund companies, custodians, and transfer agents.
>
>...Our separate account and hedge fund databases require more specialized information, which we obtain by sending surveys to the management companies. We also survey for some specialized portfolio and operations data in our other databases to enhance our proprietary portfolio statistics. We supplement information gathered electronically or through surveys by licensing a few third-party data feeds for market indices and individual securities.

As you can see, financial data vendors rely on a variety of data sources in their data collection process. This is done to supplement and enhance their data offers. Clearly, financial data vendors are continually expanding their offerings and services by including new and larger datasets derived from new sources.

Compared to other data sources, commercial datasets offer the following advantages:

* Providing structured and standardized data that is highly suited for analysis, thus reducing the need for extensive data cleaning and preprocessing
* Enriching financial datasets with additional fields and identifiers for better analysis
* Providing comprehensive documentation on data usage and field metadata
* Providing a wide range of data delivery options and formats that can suit various business applications
* Providing customized solutions and packages that fit different business needs
* Providing customer support

There is a large variety of financial data vendors, some of which create their own content (often called data providers); others specialize in aggregating or distributing data, while others act as both distributors and creators of financial data. Generally speaking, financial data companies compete along the following axes:

Data coverage:   The universe of financial instruments, entities, sectors, and variables is quite massive. Some vendors focus on a subset of financial data (e.g., asset classes, geographical areas, and sectors), while others tend to act as global aggregators or serve as a one-stop shop, offering a breadth of financial data coverage (such as prices, quotes, news, press releases, macroeconomic data, ratings, and volatility indicators).

Delivery mechanisms:   Different providers offer their data via one or more delivery mechanisms. These may include SFTP (Simple File Transfer Protocol), cloud, data feed, API, desktop, web access, and others.

Delivery formats:   Providers can differ in the file formats they use for data delivery. Examples include CSV (comma-separated values), XML, HTML, JSON, SQL query, and Zip Archive.

Data history:   Some providers, especially older ones, could have longer historical coverage than others. Additionally, some providers might provide point-in-time snapshots of their data, while others provide only the latest data releases.

Delivery frequency:   Data can be provided continuously (real time) or with fixed frequency such as second, minute, day, market closing time, week, or month.

Data standardizations and adjustments:   Some providers might apply data transformations or standardization, while others would deliver the data in its original format. Here are a few examples:

Adjusted stock prices:   A vendor might deliver adjusted stock prices that take into account corporate events such as stock splits and dividends, while another provider would leave the data unadjusted.

Data aggregation:   Some vendors provide data at the exchange level, while others aggregate the data across exchanges. If you are interested in trading on a specific exchange, you might want to check if a data provider sells data for that exchange.

Standardization of accounting figures across countries:   This might impact analysis if a company uses a specific accounting method that gets lost during standardization.

Data reliability and quality:   Accuracy, quality, and timely access to financial data are crucial to financial institutions. Providers who guarantee high data quality, low error and bias rates, and high availability are likely to be more trusted.

Value-added services:   Providers who enrich the data with extra fields, identifiers, documentation, and customer support are likely to have a competitive advantage.

Pricing:   Many subscription plans are available, and they vary by vendor. Some offer large packages that can be more expensive, while others offer various package sizes that can fit multiple usage patterns and needs.

Technical limitations:   Vendors might impose certain limits and quotas on their servers, such as the maximum daily requests, the maximum number of instruments that can be queried, or the request timeout.

The market for financial data is competitive and innovative, and it is continuously evolving to accommodate new products, markets, technologies, data types, and delivery mechanisms. One of the winning strategies that financial data vendors seem to invest in is the *one-stop shop* model, where a financial data vendor provides an integrated platform with access to a wide range of financial data as well as complementary services such as analytics and insights, export options, artificial intelligence tools, visualizations, messaging and chatting, trading, and search capabilities. Another competitive strategy is the *network effect*, where the value of a data vendor’s solution increases as more people use it. The more users and traders engage with a specific data vendor platform, the more appealing it becomes for new customers to join.

A significant share of the financial data market is dominated by a few players. This includes Bloomberg, LSEG, FactSet, S&P Global Market Intelligence, Morningstar, SIX Financial Information, Nasdaq Data Link, NYSE, Exchange Data International (EDI), Intrinio, and WRDS. There are also smaller players that tend to offer innovative products focused on a specific market niche. For example, firms such as PitchBook and DealRoom provide private market data on startups, private equity, and venture capital.

Next, I’ll present an introductory overview of some of the most important providers in the market.

### Bloomberg

Bloomberg is the whale in the financial data market, comprising almost one-third of the total market share. Bloomberg’s flagship product is the [Bloomberg Terminal](https://oreil.ly/3xxgA), a computer system well-known for its black interface that provides users with access to real-time market data, news, quotes, insights, and a number of valuable complementary services. Bloomberg is best suited for buy-side and asset management professionals such as traders and portfolio managers.

A valuable feature of Bloomberg is Instant Bloomberg (IB), a messaging service that allows users to chat with a large pool of financial professionals who are using the Bloomberg Terminal. Additionally, users of the Bloomberg Terminal can place trading orders via an end-to-end secure trading service (Tradebook). Recently, Bloomberg introduced BloombergGPT, an AI-powered language model that helps financial professionals with challenging language tasks such as sentiment analysis, news classification, question answering, and more. Additionally, Bloomberg provides [API services](https://oreil.ly/YbjkC) that allow developers to access Bloomberg data programmatically using various programming languages.

### LSEG Eikon

[LSEG Eikon](https://oreil.ly/VELTQ) is Bloomberg’s main competitor, and it holds a significant market share. Similar to Bloomberg, Eikon has a rich collection of financial datasets, a feature-rich user interface, developer APIs, an instant messaging service (LSEG Messenger), and trade execution capabilities. Compared to Bloomberg, Eikon has much cheaper options for more limited offerings.

### FactSet

[FactSet](https://oreil.ly/DHaNW) offers an affordable solution to access real-time financial data, combining proprietary, third-party, and user data. Some of FactSet’s advantages include the user-friendly UI, PowerPoint integrations for PitchBooks, personalization options, a large variety of alternative datasets, and portfolio analysis tools.

### S&P Global Market Intelligence

[S&P Global Market Intelligence](https://oreil.ly/DZSU7) is a leading financial data and market intelligence service provider. It provides financial and industry data, analytics, news, and research. Among the most well-known solutions of S&P GMI is Capital IQ, a web-based platform that provides a rich set of data points on company financials, transactions, estimates, private company data, ownership data, and more.

### Wharton Research Data Services

[Wharton Research Data Services (WRDS)](https://oreil.ly/15CjL) is the leading platform in financial and business research and analysis and is among the most popular data distributors in finance. WRDS offers a globally accessed, user-friendly web interface with more than 600 datasets from more than 50 data vendors across multiple domains, with a particular focus on finance. Through WRDS, users can access multiple data sources, documentation, analytics, and query-building tools simultaneously. WRDS establishes distribution and resale agreements with data vendors and allows their clients to access vendor data directly through their platform. For some datasets, WRDS requires their clients to buy and maintain a separate license for the data.

# How Do I Choose a Financial Data Vendor?

Most financial institutions use services from at least one financial data vendor. However, finding and choosing the right vendor can be quite challenging. My advice is to start by formalizing your company’s or project’s financial data needs. Then, using the vendor differentiating criteria mentioned previously, you can ask yourself some key questions:

What type of data am I looking for?:   For example, if you are looking for data on Chinese stock prices, you might want to find a local data provider specializing in the Chinese market.

Which fields are mandatory, and which are optional?:   For example, if you want adjusted stock prices, you need to choose a data provider that provides already adjusted data or the necessary fields to perform the adjustment.

What is the universe of assets that I want?:   For example, if you want data on European and American stocks, as well as fixed-income data, you might need a global data provider with international coverage (e.g., Bloomberg).

Do I need data quality guarantees?:   Some providers ensure their data is free from errors, biases, and other quality issues, while others offer less assurance, necessitating data cleaning.

What is the planned budget?:   For example, if your company has a limited budget, you might need to look for a data provider that offers small packages or on-demand pricing.

What purpose do I need the data for?:   For example, buy-side professionals (e.g., traders) often need a wide variety of data, such as prices, news, macroeconomic variables, and market volatility, while sell-side professionals (e.g., investment bankers) need more specific data, such as asset prices and corporate events.

What data update frequency do I want?:   For example, if you have a machine learning model that you train weekly, then there is no need for very frequent updates. However, if you are working at an algorithmic trading company, then data would be needed at a very high frequency.

Do I need specific delivery mechanisms?:   For example, if you are developing a web application, you will very likely need to fetch data via an API. However, if you have data extraction running in the background, receiving files via SFTP or direct website download should work fine.

Do I need predictable delivery performance?:   Some providers may offer guarantees on latency, throughput, and uptime, which are crucial for time-sensitive applications.

Can I tolerate vendor limitations?:   For example, if your workload is predictable, you can adapt your application and consumption patterns to the limitations established by the data vendor. However, if your data needs are unpredictable or growing, you might want to find a data vendor that does not impose strict limitations or negotiate custom quotas.

Do I need a simple solution?:   For example, if you want a simple user interface with Microsoft Excel or CSV export capabilities, you may not want to choose a very sophisticated financial data solution.

## Survey Data

A survey is a set of questions designed to collect information from a specific group of people on a particular topic. Survey data can enhance existing datasets and provide deeper insights. For instance, banks might ask clients to complete a survey to assess their financial knowledge and risk appetite level. This information can help assess and tailor investment plans to fit each customer’s profile. Similarly, financial data vendors may rely on surveys as a mechanism to gather data from companies by sending them questions related to their operations, performance, and structure.

Survey data could serve as the main ingredient in creating other types of data. For example, the Institute for Supply Management (ISM) publishes the [*Purchasing Managers’ Index* (PMI)](https://oreil.ly/lTAND), a monthly figure used by market agents as an indicator of the direction of the economy. To calculate the PMI, the ISM sends a survey to a list of companies that make up a representative sample of the entire economy. Once respondents return the filled-in surveys, the index is computed by aggregating and weighing the individual responses.

The main advantage of survey data is its flexibility, enabling the questioner to design the questions to guarantee valuable answers and organize the information optimally. However, a few challenges might arise. For example, if the survey is voluntary, some respondents might have no incentive to provide answers, which can bias the final outcome. In other cases, some candidates may choose not to complete the survey. This could be due to a reluctance to report poor financial performance, organizational inertia, concerns about reputational risk, competition, or issues related to security and confidentiality. Additionally, the questioner might (intentionally or unintentionally) induce *framing bias* in the survey by choosing questions intended to force the respondent to give a desired answer. For this reason, a strong emphasis on ethical practices and bias checks is highly recommended when conducting surveys.

## Alternative Data

In recent years, the term “alternative data” has emerged in the financial world to describe data sources not traditionally used in financial analysis and investment. These nonconventional data sources are not inherently embedded within the financial system, unlike trading venues, payment systems, and commercial banking. The sources of alternative data are quite heterogeneous. A few are mentioned here:

* Satellites (e.g., collecting shipping images)
* Social media (e.g., tweets)
* Articles
* Blog posts (e.g., Medium, Substack)
* News channels (e.g., Thomson Reuters, Bloomberg)
* Weather observers
* Online clicking patterns and browsing history
* Shipping and pipeline trackers
* Emails and chats
* Product and service reviews
* Security, social, and environmental scores and ratings

## Confidential and Proprietary Data

Financial institutions generate and store large amounts of data when conducting their internal operations. The most essential and valuable type of internal data involves contextual, nontransactional information about the various business entities. This includes, for example, data about clients, employees, suppliers, products, subscriptions, offerings, discounts, pricing, financial structures (e.g., cost centers), and locational information (e.g., branches).

A second type of internal business data is *transactions*. In performing their daily activities, financial institution clients generate a large amount of transaction data, such as payments, deposits, trading, purchases, credit card transactions, and money transfers.

Finally, financial institutions might collect *internal analytical data* from research teams and analysts conducting market and financial analysis. This includes, for example, sales analysis and forecasting, customer segmentation, credit scoring, default probabilities, investment strategies, stock predictions, macroeconomic analysis, and customer churn probabilities.

In specific situations, financial institutions must report various types of confidential data to regulatory bodies. This includes trade details, large transaction information, suspicious activity reports, data gathered during anti-money laundering (AML) and know your customer (KYC) processes, as well as information related to tax, compliance, liquidity, risk management, and capital adequacy.

Now that you have an idea about the different sources of financial data, the next section will discuss the various structures in which financial data can be represented.

# Structures of Financial Data

Financial data can be stored and represented using various structures. These may range from simple data structures such as tabular times series, cross-section, or panel data to more complex structures such as matrices, graphs, and text. Throughout this section, we will explore these structures in detail.

## Time Series Data

A time series is a collection of records for one or more variables associated with a single entity, observed at specific intervals over time. Time series are indexed in time order and can be represented mathematically as follows:

𝐗 =

X 1, X 2,...., X N

where *N* is the length of the time series and *X* is the observed variable, or:

𝐗 =

X t, t ∈ T

where *T* is a time index set and *X* is the observed variable.

In tabular format, a time series with *S* variables observed over *N* periods can be represented as shown in [Table 2-1](#ch02_table_1_1724776825557649). The first column stores the temporal dimension ( T N ), while the other columns ( X S ) store the time series values for each variable. A single cell ( X SN ) records the time series values observed at a specific time for a given variable.

Table 2-1. Tabular representation of time series

**Time/variable** X 1 X 2 X 3 … X S T 1 X 11 X 21 X 31 … X S1 T 2 X 12 X 22 X 32 … X S2 … … … … … … T N X 1N X 2N X 3N … X SN

The time series is the most common data structure in financial markets, mainly due to the dynamic and transactional nature of financial activities that happen over time. Examples of financial activities that generate time-series data include trading, pricing, payment, investment, estimation, valuation, risk measures, volatility figures, corporate events, performance and accounting, and many more.

Extensive literature on financial time series has been produced where a large number of temporal phenomena have been investigated. For an excellent treatment of financial time series analysis, I recommend the seminal book *Analysis of Financial Time Series* by Ruey Tsay (Wiley, 2010).

## Cross-Sectional Data

A cross-section is a collection of records for one or more variables observed across multiple entities at a single point in time. In cross-sectional data, the time series dimension is irrelevant, and the emphasis is on the variables themselves. Entities in a cross-section often share common characteristics, such as firms within the same sector, investments in a specific strategy, fund managers, and more.

A cross-section dataset can be represented mathematically as follows:

X t=z,i,j, i = 1,..., N, j = 1,....., S

where *t* is the time index (fixed), *i* is the entity index, and *j* is the variable index.

In tabular format, we can draw a cross-section of *N* entities and *S* variables as shown in [Table 2-2](#ch02_table_2_1724776825557690). The first column stores the names of the entities ( E N ), while the other columns store the cross-section value of the *S* variables ( V S ). A table cell ( X i,j ) stores the cross-section value of a given entity for a given variable.

Table 2-2. Tabular representation of cross-section data

**Entity/variable** V 1 V 2 V 3 … V S E 1 X 11 X 21 X 31 … X S1 E 2 X 12 X 22 X 32 … X S2 … … … … … … E N X 1N X 2N X 3N … X SN

Financial cross-section data is generated from the presence of many participants in financial markets, including financial institutions, brokers, investors, consumers, traders, and managers, as well as a variety of other entities such as financial assets, investment strategies, and consumer and firm choices and behaviors, among others.

Financial cross-sectional data can be used to understand and explain significant point-in-time differences between financial entities, such as why different stocks have different returns, why firms behave differently, or why performance across fund managers varies. Furthermore, cross-sectional analysis is a key tool for identifying correlations, causations, or anomalies across different entities, which can be critical for investment decisions, policy formulation, and understanding market dynamics.

## Panel Data

Panel data combines both time series and cross-sectional structures, representing data for a set of variables across multiple entities at different points in time. Mathematically, a panel has the following form:

X i,j,t, i = 1,..., N, j = 1,....., S, t = 1,....., T

where *i* is the entity index, *j* is the variable index, and *t* is the time index.

In tabular format, we can draw a panel of two entities, two time periods, and three variables as shown in [Table 2-3](#ch02_table_3_1724776825557715). The first column stores the names of the entities, the second column stores the time, and the last three columns store the observed panel values for all three variables. This panel representation is called *wide format*, as it expands horizontally when new variables are added to the panel. Another option is the long format, where the variable name and value are stored in separate columns, expanding the table vertically with new entries. An example is shown in [Table 2-4](#ch02_table_4_1724776825557736).

Table 2-3. Wide tabular representation of panel data

**Entity** **Time** V 1 V 2 V 3 E 1 t=1 X 111 X 112 X 113 E 1 t=2 X 121 X 122 X 123 E 2 t=1 X 211 X 212 X 213 E 2 t=2 X 221 X 222 X 223

Table 2-4. Long tabular representation of panel data

| Entity | Time | Variable name | Variable value |
| ------ | ---- | ------------- | -------------- |
| E 1    | t=1  | V 1           | X 111          |
| E 1    | t=2  | V 2           | X 122          |
| E 2    | t=1  | V 1           | X 211          |
| E 2    | t=2  | V 2           | X 222          |

Financial panel data arises from numerous market entities engaging in various activities over time. For instance, stocks are continuously traded and priced, companies regularly submit quarterly and annual reports, and individuals conduct daily payments and transactions. Hence, most financial datasets are essentially panel datasets.

Panel data may vary in terms of their cross-section and time series components. For example, annual balance sheets tend to have a large cross-section component (many firms) and a small history. On the other hand, some stock price panel datasets tend to have a long history (e.g., high-frequency trading prices) and a smaller cross-section component (asset universe).

An important characteristic of panel datasets is their degree of [balance](https://oreil.ly/lwqFA). Assume a panel has N entities, T time periods, and S variables. The panel is said to be *balanced* if all N × T × S observations are available; otherwise, the panel is called *unbalanced*. [Table 2-5](#ch02_table_5_1724776825557754) shows a balanced panel where data are available for all entities, time periods, and variables. [Table 2-6](#ch02_table_6_1724776825557773) instead illustrates an unbalanced panel as it has six cells with null values, resulting in half of the observations being missing.

Table 2-5. Balanced panel

**Entity** **Time** V 1 V 2 V 3 E 1 t=1 X 111 X 112 X 113 E 1 t=2 X 121 X 122 X 123 E 2 t=1 X 211 X 212 X 213 E 2 t=2 X 221 X 222 X 223

Table 2-6. Unbalanced panel

**Entity** **Time** V 1 V 2 V 3 E 1 t=1 Null X 112 Null E 1 t=2 X 121 X 122 X 123 E 2 t=1 X 211 Null X 213 E 2 t=2 Null Null Null

Similar to time-series data, a large literature, both theoretical and empirical, has been produced for panel data analysis. For an excellent introduction, I highly recommend Badi H. Baltagi’s seminal book *Econometric Analysis of Panel Data* (Springer, 2021).

## Matrix Data

A matrix is a two-dimensional array of elements arranged as rows and columns. Here is an example:

(

3 )

This is a matrix with three rows and three columns, often referred to as a 3 × 3 matrix.

The use of matrix structures is quite common in finance. The best example is perhaps portfolio optimization theory, in particular Markowitz’s mean-variance optimization (MVO). According to MVO, when constructing a financial investment portfolio, three elements should be taken into consideration:

* The expected return on the assets in the portfolio
* The variance (risk) of the asset returns
* The covariances between the asset returns

For example, let’s imagine a portfolio with three assets: A, B, and C. Let’s denote the expected return of any asset *i* with

E ( R i ), the variance with

v a r ( R i ), and the covariance between two assets *i* and *j* with

c o v ( R i, R j ). Using MVO, two matrix representations would be constructed as follows:

* 3 × 1 portfolio return matrix

(

E ( R A )

E ( R B )

E ( R C ) )

* 3 × 3 covariance matrix

(

v a r ( R A )

c o v ( R A, R B )

c o v ( R A, R C )

c o v ( R B, R A )

v a r ( R B )

c o v ( R B, R C )

c o v ( R C, R A )

c o v ( R C, R B )

v a r ( R C ) )

Using these matrix representations, MVO relies on matrix algebra to optimize the portfolio’s expected return for a given level of risk appetite. Portfolio optimization means choosing the best asset allocation strategy (how much to invest in each asset) to achieve a desired investment goal.2

## Graph Data

Financial markets are an outstanding example of a complex system of myriad relationships, transactions, dependencies, and flows. Understanding such complex interactions can provide valuable information and insights into market structures, systematic risks, contagion mechanisms, dominant market positions, fraudulent behavior, and market inefficiencies.

The kind of analysis that focuses on studying the complex interactions in a system is called *network analysis* or *network science.*3 To employ network science in finance, traditional time-series or cross-section data would lack the depth and granularity required to build and analyze financial networks. To this end, graph data is required. This type of data is also frequently referred to as connections, networks, or nodes and links. A graph dataset consists of two sets of data: a set of nodes (aka vertices) together with node attributes (e.g., name, country, type, and so on), and a set of links (aka edges) with link attributes (e.g., type, value, sign, and so on).

When working with graph data, an important challenge concerns the decision about how to structure the data for quick access and analysis. Structuring nodes’ data and their attributes is straightforward, and a tabular structure will do the job. However, things get more complicated when it comes to structuring link data. To this end, special graph structures are often used. Generally speaking, a graph dataset can be represented in four main ways:

Network visualization:   A 2-D drawing of the nodes (often as circles) and links (using straight lines). This method is useful for illustrative purposes and works best with small networks.

Adjacency matrix:   An N × N matrix (N being the number of nodes). If there is a link between nodes i and j, it stores 1 at positions (i, j) and (j, i).

Adjacency list:   An array of length N (N being the number of nodes) where each item in the array contains the index of the node and a list of its neighbors represented via a linked list.

Edge list:   A simple array that stores all edges of a graph. An item of an edge list is a tuple where the first element is the source node and the second is the target, with optional elements that may represent link attributes such as weight, sign, and time.

[Figure 2-1](#ch02_figure_1_1724776825532264) visually illustrates these four types of graph data representations.

### Figure 2-1. Different representations of graph data

![Figure 2-1. Different representations of graph data](images/fden_0201.png)

Financial markets rely on a range of graph data types and representations. In the upcoming sections, I will discuss six pertinent graph structures: simple, directed, weighted, temporal, multipartite, and multiplex.

### Simple graphs

A simple graph consists of a set of homogeneous nodes (nodes of the same type, e.g., companies) and a set of homogeneous, unweighted, and undirected links. [Figure 2-2](#ch02_figure_2_1724776825532301) illustrates an example with two nodes (A, B).

### Figure 2-2. A simple graph with two nodes

The adjacency matrix, adjacency list, and edge list representations of simple graphs are similar to those shown in [Figure 2-1](#ch02_figure_1_1724776825532264). In financial markets, simple graphs can represent the *presence* of relationships between entities, such as payment agreements between banks, partnership agreements, and statistical correlations between financial assets.

### Directed graphs

In a directed graph, links have a direction indicating an *orientation* between the nodes. Directed graphs are used to represent relationships where nodes at each end of the link play different roles. For example, A borrows from B, where A is the borrower and B is the lender. [Figure 2-3](#ch02_figure_3_1724776825532323) illustrates an example with two nodes, A and B, where node A points to node B but not vice versa.