### Figure 2-3. A simple directed graph with two nodes

The adjacency matrix of a directed network will have a value of 1 at position (i, j) if there is a link pointing from node i to j, but will have a value of 0 in position (j, i) if j doesn’t have a link pointing toward i. Similarly, a directed graph’s adjacency and edge list will only store records for nodes that point toward other nodes. [Figure 2-4](#ch02_figure_4_1724776825532341) illustrates the four representations for a directed graph.

### Figure 2-4. Directed graph representations

![Figure 2-4. Directed graph representations](images/fden_0204.png)

Directed graphs can represent a variety of financial activities, such as cross-holding among banks, transfers, transactions, and interbank lending.

### Weighted graphs

In weighted graphs, links are assigned a numerical value to indicate the relationship’s magnitude or strength. When representing a weighted graph, the weight needs to be added to the adjacency matrix, adjacency list, and edge list as illustrated in [Figure 2-5](#ch02_figure_5_1724776825532359).

### Figure 2-5. Weighted graph representations

![Figure 2-5. Weighted graph representations](images/fden_0205.png)

Most types of graphs can be weighted (including simple and directed graphs). In finance, weights can represent the value of the assets one bank holds at another in a cross-holding network, the amount of money transferred in a transaction, or the number of securities sold in a market trade.

### Multipartite graphs

A graph representation is called *multipartite* when it includes more than one type of node and only allows links between different types of nodes. Graphs with two types of nodes are referred to as *bipartite*, those with three types of nodes as *tripartite*, and the generalized case with *k* types is called *k-partite*. A *k-partite projection*, often applied to bipartite graphs, is a common operation that builds a graph that contains one type of the *k* available node types, and edges exist based on whether two nodes share a common link to another type of node in the original network. [Figure 2-6](#ch02_figure_6_1724776825532376) presents a bipartite graph along with its projected graph and adjacency matrix.

### Figure 2-6. Bipartite graph representations

![Figure 2-6. Bipartite graph representations](images/fden_0206.png)

The leftmost graph in [Figure 2-6](#ch02_figure_6_1724776825532376) has two types of nodes, shaded and white, and links exist only between a shaded and a white node. The middle graph illustrates a bipartite projection on one type of node (the shaded nodes in the leftmost graph). The projected graph shows that nodes A and C have a link because in the bipartite graph on the left, both A and C share a connection to K. The same goes for C and B, which share a connection to M. The adjacency matrix in [Figure 2-6](#ch02_figure_6_1724776825532376) has a block structure, where links between the same type of nodes will be absent and represented with zeros (shaded blocks) whereas links between different types of nodes exist in the white blocks.

Examples of bipartite relationships in finance include the following:

Interlocking directorate:   Nodes of type “person” (node type 1) act as a member of the board of directors (link) of one or more firms (node type 2).

Syndicated lending:   Multiple lenders (node type 1) jointly provide a loan (link) to one or more borrowing entities (node type 2).

Corporate control hierarchies:   Parent firms (node type 1) have ownership rights (link) over child firms (node type 2).

Correspondence banking:   A correspondent banking relationship is an arrangement between two banks, typically in different countries, where one bank (the correspondent bank) provides services on behalf of another bank (the respondent bank).

Working with multipartite graphs is much easier when nodes are labeled by category, often referred to as a colored graph in mathematics. For instance, a bipartite graph can be colored with two colors, where each node category has the same color. Without such labels, identifying a k-partite graph can be challenging, especially when k is greater than two.4

### Temporal graphs

In a temporal graph, links have a temporal dimension indicating the time at which they were active. The network representation of temporal graphs is snapshot based or time based. As illustrated in [Figure 2-7](#ch02_figure_7_1724776825532393), both the network and adjacency representations are temporal snapshots storing the state of links at each time period. For example, nodes A and B established a link at times t1, t3, and t4, but they didn’t interact at time t2. The adjacency matrix is represented as a multidimensional matrix storing a snapshot for each time period. The edge list stores all links and the time at which they were active.

### Figure 2-7. Temporal graph representations

![Figure 2-7. Temporal graph representations](images/fden_0207.png)

Many financial relationships are temporal in nature, such as interbank lending, trading, payments, transactions, and many more.

### Multilayer graphs

A multilayer graph is a complex structure used to represent relationships between different types of nodes and links. The most common type is the *multiplex* graph, where nodes are of the same type but have different types of links depending on the interaction context. For instance, a financial institution may operate in various markets such as commercial banking, wealth management, and financial consulting.

Multilayer network representations are very useful in finance. They can reveal potential cascading mechanisms that might amplify a local shock, help understand power structures spanning multiple areas, and enhance fraud detection (e.g., when the same individual operates in different systems using the same connection patterns). An illustration of multiplex graph representation is provided in [Figure 2-8](#ch02_figure_8_1724776825532410).

### Figure 2-8. Multiplex graph representation

![Figure 2-8. Multiplex graph representation](images/fden_0208.png)

# What Are the Sources of Financial Graph Data?

An important feature of financial graph data is that it is often derived from other types of data sources. For example, to build a graph of the [interbank loan market](https://oreil.ly/lK30D), you would need a historical panel of interbank transactions containing information on borrowers, lenders, and the transaction amount and time. Similarly, say you want to build a bipartite network of [interlocking directorates](https://oreil.ly/dXg-J) to see which directors sit on multiple boards, then you would need a dataset (e.g., the LSEG Officers and Directors dataset) that contains information on executive individuals and the companies they are associated with. In some cases, more work is required. For example, if you want to build a network of [similarities between stocks](https://oreil.ly/cFN3H), you would first need a historical panel of price data (e.g., CRSP), and then you need to compute the pair-wise similarity (correlation) between the stocks in order to get the links needed to build the graph.

It is possible in some cases to find connection datasets curated by financial data vendors. For example, S&P Global [provides a number of datasets about business and company relationships](https://oreil.ly/sydqG), such as ownership, supply chain, investment, and many more types of relationships.

## Text Data

Text data refers to information available in any unstructured or semi-structured format. Its extensive use and versatility make it [arguably the most available type of data in financial markets](https://oreil.ly/5ZUgg). With the advent of generative AI and large language models (LLMs), the importance of text data has significantly increased. Generative models such as GPT-4 and BloombergGPT are trained on massive amounts of text data. For specialized financial tasks such as fraud detection, sentiment analysis, know your customer (KYC), and anti-money laundering (AML), finance domain-specific text data is essential for customizing and fine-tuning an LLM.

It can be any text-based medium, including news, analyst reports, company filings, prospectus documents, emails, social media posts, system logs, patent documents, legal and technical documents, research papers, web pages, blog posts, and much more.5

Text data can take various forms, including plain text consisting of words and sentences, semi-structured documents with keys and values, tabular formats, or complex specialized data structures like [word embeddings](https://oreil.ly/5Ajf5).

Financial text data exhibits certain characteristics that set it apart from other forms of textual data. Terms such as “liability,” “risk,” “default,” and “exposure” may carry negative connotations in certain contexts, yet they are commonly used and frequent terminology in financial markets. Additionally, financial documents can contain both explicit content (such as a firm merging with another) and implicit content (factual information implying a positive or negative emotion).6

Now that you’re familiar with financial data’s main sources and structures, the following section will explore the various types of financial data employed for analytical and operational purposes.

# Types of Financial Data

The financial data structures we discussed in the previous section can represent a variety of financial variables, content, and phenomena. This section will categorize these financial phenomena by discussing the most crucial types of financial data in detail, illustrating their features and challenges.

## Fundamental Data

Financial fundamental data, also called financial statements data, balance sheet data, or corporate finance data, conveys information about firms’ structures, operations, and performance. Firms themselves generate and produce fundamental data, partly because it’s a regulatory requirement and partly because it helps the management understand the financial and operational situation of the firm. Many companies have accounting departments liable for generating and maintaining financial statements, but it is also possible to do so via accounting service providers such as consulting and audit firms. In general, there are three main financial statements:

Balance sheet:   Provides figures on what a firm owns (assets), what it owes (liabilities), and what its shareholders own (*shareholders’ equity*)

Income statement:   Provides figures on a firm’s financial performance over a specific period, such as the annual revenues and net profit

Cash flow statement:   Provides information on a firm’s cash movements (in and out), which can help determine whether the firm is generating enough cash to carry out its operations

Each financial statement contains a large number of items representing different quantities. A special type of financial statement item is *ratios,* which represent relationships between two or more items. For example, a popular ratio is *Return on Equity* (ROE), which is calculated by dividing the company’s net income by the value of its shareholders’ equity. A high ROE is an indicator that the company is efficient at generating net income using shareholders’ equity.

Financial fundamental data statements have a number of characteristics that need to be taken into account. First, due to the time it takes to prepare them, fundamental data statements are released with *low frequency,* such as quarterly, each semester, or yearly. Second, fundamental data reports are often published with a *time lapse*, meaning that data for a specific period is released at a future date. Data can be reported in the form of *reinstatements*, which happens when a figure gets revised and corrected after it has been released. Data *backfilling* can also take place, which happens when a firm and its entire fundamental data history get added to a dataset that has never had information on that firm before.

If not handled properly, these characteristics could lead to [*non-point-in-time* (PIT) fundamental data](https://oreil.ly/BH6U0). PIT data is data that is recorded with a timestamp reflecting the filing or release data. With PIT data, one can ask the questions “When was the data released?” and “What data was known at that time?” On the other hand, non-PIT data is stamped with the fiscal year-end date or the latest update date. Non-PIT data reflects the latest data release, and it gets overwritten when an update or reinstatement happens. [Table 2-7](#ch02_table_7_1724776825557790) illustrates the difference. With three versions of the data available, a PIT dataset would keep track of all historical snapshots (101, 110, 120), while a non-PIT dataset would show only the latest version (120).

Table 2-7. PIT versus non-PIT data

| Data type | Preliminary result | Fiscal year-end release | Correction |
| --------- | ------------------ | ----------------------- | ---------- |
| Version   | 101                | 110                     | 120        |
| PIT       | 101                | 110                     | 120        |
| Non-PIT   | 120                | 120                     | 120        |

Non-PIT data poses several challenges. First is the problem of *look-ahead bias*, which happens when conducting historical studies and assuming that data was known at a specific historical moment, which, due to a release time lapse, may not be the case. Second is *reproducibility*, which becomes challenging if non-PIT data used for past research is updated and may not yield the same results. The third challenge is *transparency*, which may be an issue if, for example, a company updates an accounting record to hide past fraudulent behavior.

# Reading Financial Highlights from a Bank Annual Report

Being able to understand the main items in an annual report is a good skill, even for financial data engineers. The table below illustrates the annual financial highlights of an imaginary bank, ADK. If you check the annual report of any real bank, you will find a similar table. Examining the figures for 2020, we can see that the bank realized more *total net revenues* compared to 2021 ($bln 102 versus 99) but with a lower *net income* ($bln 23 versus 25). This translates into lower returns for shareholders, which we can see from the *return* *on common equity* figure of 11% compared to 16% in 2019. ADK is quite a large bank, which we can see from the *total assets* figure that equals $2,987,245 million (almost $3 trillion) and the *headcount* of 150,432. Moreover, ADK seems to be financially stable, which we can infer from the *Tier 1 capital ratio* of 15%, a measure introduced by the Basel III accord, which tells how stable a financial institution is by comparing its core equity against its risk-weighted assets. Basel III established that the Tier 1 capital ratio must be at least 6%. ADK probably has a large market share, which we can see from its considerable market capitalization of $240,876 million (roughly $240 billion). A dividend was distributed every year to shareholders, which we know from the *cash dividends per share* figure.

| Item                               | 2020      | 2019      | 2018      |
| ---------------------------------- | --------- | --------- | --------- |
| Total net revenue ($ mln)          | 102,000   | 99,340    | 96,345    |
| Total noninterest expense ($ mln)  | 55,000    | 49,000    | 45,865    |
| Net income ($ mln)                 | 23,100    | 25,987    | 19,628    |
| Cash dividends per share ($)       | 3.5       | 2         | 1.7       |
| Return on common equity            | 11%       | 16%       | 8%        |
| Tier 1 capital ratio               | 15.0%     | 14.1%     | 14%       |
| Total capital ratio                | 18.9%     | 17%       | 17%       |
| Loans ($ mln)                      | 986,865   | 956,586   | 916,865   |
| Deposits ($ mln)                   | 1,298,456 | 1,187,456 | 1,062,456 |
| Total assets ($ mln)               | 2,987,245 | 2,445,853 | 2,200,119 |
| Total stockholders’ equity ($ mln) | 72,876    | 71,664    | 70,345    |
| Market capitalization ($ mln)      | 250,876   | 300,897   | 280,986   |
| Headcount                          | 150,432   | 144,983   | 139,709   |

## Market Data

Market data includes price and related information for financial instruments traded on market venues such as the New York Stock Exchange (NYSE) or in off-exchange OTC markets. It is extensively available for many types of instruments, such as stocks, derivatives, indexes, currencies, bonds, and funds. Moreover, market data is released frequently, often becoming available just seconds after its generation.

A financial instrument’s market data may include fields such as the following:

* Identifiers such as tickers, e.g., IBM
* Trading venue code such as the exchange code, e.g., NYSE
* Last day (adjusted) closing price, e.g., $40.30
* Current day open price, e.g., $40.15
* Current day highest price, e.g., $42.30
* Current day lowest price, e.g., $39.42
* Current day price range, e.g., $39–42.30
* Current day volume, e.g., 50,000
* Latest bid/ask prices and quantities, e.g., bid of $40.02 × 2200 and ask of $40.03 × 3000
* Last trade/quote date, e.g., today at 14:12:10 p.m.

### Note

In financial markets, the term *bid* is used to indicate the price at which buyers are willing to buy a financial asset, while the *ask* is the price at which sellers are willing to sell an asset.

Some stock exchanges and media platforms enrich market data with fundamentals such as market capitalization, revenues, and net profit, as well as various financial ratios and corporate event dates, such as the latest dividend date.7

At the core of market data generation lies the *order book*, an electronic ledger of buy and sell orders for a specific security at a given trading venue. Order books have two representations: *Market by Order* (MBO) and *Market by Price* (MBP). MBO shows each individual order separately, detailing the price, quantity, and time of entry for each buy and sell order. In contrast, MBP aggregates orders by price level, consolidating them into price buckets to display the total quantity of orders at each price level instead of showing each order individually.

Orders in an order book can be matched through an *Order Matching System* (OMS), which uses algorithms to ensure the best execution. The two most common match algorithms are price/time priority (also known as First In, First Out, or FIFO) and pro rata.8 Price/time priority matches orders based on price first, and then by the time of entry at the same price level; for example, if two buy orders are placed at the same price, the earlier one gets matched first. Pro rata matching, on the other hand, matches orders at the same price level proportionally based on their sizes; for instance, if there are two buy orders at the same price, one for 100 shares and another for 200 shares, and a sell order for 150 shares arrives, the matching will be split proportionally, giving 50 shares to the first order and 100 shares to the second.9

An example of an order book is illustrated in [Table 2-8](#ch02_table_9_1724776825557828). The example shows that the highest bid price level is $55.11, while the lowest ask price level is $55.13. The highest bid and lowest ask are called the *top of the book*, while the difference between them is called the *bid/ask spread* (=$0.02). The *order book depth* is a measure of the number of distinct price levels available in an order book. Another term, the *market depth,* is often used as an indicator of liquidity and is defined as the size of market orders that can be executed without causing a large impact on the price level.

Table 2-8. Example of an order book

| Buy-side       |               | Sell-side     |                |
| -------------- | ------------- | ------------- | -------------- |
| **Bid volume** | **Bid price** | **Ask price** | **Ask volume** |
| 220            | $ 55.11       | $ 55.13       | 1000           |
| 1000           | $ 55.11       | $ 55.14       | 500            |
| 50             | $ 55.9        | $ 55.66       | 200            |
| 20             | $ 55.55       | $ 55.66       | 10             |
| 560            | $ 55.1        | $ 66.68       | 50             |
| …              | …             | …             | …              |

Different types of orders can be submitted to an order book. For example, a *market order* is used to buy or sell at the best bid/ask price available. A *limit order* is an order to sell at a specified minimum ask price or buy at a maximum bid price. A *stop-loss order* is triggered and submitted to buy or sell if the price level reaches a predefined maximum or minimum value. A *trailing stop order* is triggered if the market price moves up or down by a specific percentage or dollar amount.

Market data exhibits several features that are worth considering. First, market data, such as prices, are computed quantities. When an investment firm submits an order to buy or sell a financial asset, the order price is often calculated using a specific valuation method. For example, company stock prices can be calculated using methods such as the net present value, earning multiples, the dividend discount model, or the discounted cash flow model.10

Importantly, when different market participants submit orders with varying prices across different markets, determining the final market price for investors becomes crucial. Ideally, the bid price is the highest among all bid prices, and the ask price is the lowest among ask prices. To enforce this rule, regulators such as the SEC passed the [Regulation National Market System (NMS) regulation](https://oreil.ly/VE01I), which introduced the *National Best Bid and Offer* (NBBO). With the NBBO in action, brokers are required to ensure that their client orders are executed against the best bid and ask prices, which need to be at least equal to the NBBO.11

Nevertheless, not all financial markets ensure an NBBO. This is particularly true in OTC markets like foreign exchange (Forex) markets where currencies are traded. There is no enforced exchange rate for a currency pair in the Forex market. The exchange rate you will get is specific to the Forex quote provider, which can be your bank or, most commonly, a *Forex broker*. This means that the quote you see on Google for EUR/USD is not the market price, and you should not expect it to match the one you get offered when you convert money from one currency to another.

*Price discreteness* is another important attribute of market data. It means that the price of a listed stock cannot change by less than a specific amount known as *tick size.* For example, according to [SEC Rule 612 on the minimum pricing increment](https://oreil.ly/U_vBG):

> The Rule prohibits market participants from displaying, ranking, or accepting quotations, orders, or indications of interest in any NMS stock priced in an increment smaller than $0.01 if the quotation, order, or indication of interest is priced equal to or greater than $1.00 per share. If the quotation, order, or indication of interest is priced less than $1.00 per share, the minimum pricing increment is $0.0001.

Finally, a quite important feature of market data, and in particular price data, is its *nonsynchronous history*. This means that given two securities, A and B, security A could trade at least once every minute, while security B trades only once every five hours. Such discrepancies in market behavior are often due to market liquidity varying from one security to another.

## Transaction Data

A financial transaction is a legal agreement between two or more parties to exchange financial securities, services, goods, risks, or commodities in return for money. Financial markets generate massive volumes of transaction data triggered by activities such as investments, payments, trading, hedging, speculation, and lending.

Most financial transactions are conducted either fully or partially electronically. Generally speaking, a financial transaction can be characterized by at least five elements: transaction specifications, transaction parties, initiation date, settlement date, and settlement method.12 Next, we discuss each of these five elements in detail.

### Transaction specifications

Before initiating a transaction, parties agree on its details and specifications. In securities exchange, this phase is often called pre-trade. To provide examples, a stock purchase transaction would specify the name and identifiers of the shares being exchanged, the quantity of each share, the price, and the currency. For financial instruments such as options on stocks, additional details would be needed, such as option type (call versus put), expiry date, and exercise price. For cross-border payments, parties may need to agree on the amount, currency pair, Forex conversion rate, and any spread margin.

### Initiation date

The initiation date of a transaction is the date at which parties enter into an agreement to execute a transaction.

### Settlement date

The settlement date is when a transaction is finalized, and the exchange of money and transfer of ownership takes place. In securities exchange, this phase is called post-trade. Importantly, in many financial transactions, the settlement date falls on a future date, following the initiation date. Such a delay can be due to various reasons such as the transaction verification process, technological constraints, errors due to missing information, bureaucratic steps such as the issuance of a certificate of ownership (e.g., stock certificate), lengthy payment process, and any manual intervention steps that may be necessary (e.g., review).

Financial market participants have been investing in technologies to shorten the transaction settlement time. The term *straight-through processing* (STP) is often used to designate the ideal transaction processing system that does not involve manual intervention, leading to decreased processing time, reduced operational risks, and lowered costs. Additionally, financial markets have adopted common conventions for settlement periods. For example, the current convention in securities transactions is *T+2 (trade date plus two days),* which indicates that a security transaction should be settled two business days after the transaction initiation date. Recently, the term *same-day affirmation* (SDA) or *T0* has received attention from markets and regulators as it promotes the idea of completing the transaction verification process on the same day the transaction took place. Reducing the time of financial transaction lifecycles via STP and SDA can be quite challenging, as it requires significant investments by multiple market participants in a data infrastructure that provides real-time transaction data, while at the same time meeting the requirements of security and reliability (luckily, this is the topic of this book!).

### Settlement method

Financial market transactions can be settled differently based on the transaction type. In securities markets, the most common settlement method is *Delivery versus Payment* (DVP), which guarantees that the cash payment for securities is made either before or at the same time as the delivery of the securities. In a *Delivery versus Free* (DVF) mechanism, the delivery of securities occurs for free, for example, when delivering the collateral to a securities loan.

In payments, multiple settlement mechanisms exist. A common example is *Payment versus Payment* (PvP), widely used in Forex transactions. In a PvP system, the payment of one currency occurs only if the payment of the corresponding currency takes place. Another prominent mechanism is *Real-Time Gross Settlement* (RTGS), where funds are transferred in real time on a gross basis, meaning transactions are processed continuously throughout the day and settled individually. Conversely, in a *Deferred Net Settlement* (DNS) mechanism, transactions are accumulated over a period (e.g., end of the day) and then settled in batches at specific intervals. In DNS, only the net difference between debits and credits is settled. For example, if Citibank is to pay JPMorgan Chase $1.5 million, and JPMorgan Chase is to pay Citibank $1 million, a DNS system would aggregate this to a single payment of $500,000 from Citibank to JPMorgan Chase. Conversely, an RTGS system would require two separate payments for the full amounts ($1.5 million to JPMorgan Chase and $1 million to Citibank).

### Transaction parties

Financial market transactions are often conducted by two parties, the buyer and the seller. However, transactions are not risk free. The term *settlement risk* refers to the risk that one side of a transaction does not honor their contractual obligation, e.g., failure to pay the amount due, failure to pay on time, or failure to transfer the asset ownership. To mitigate such risk, a third party is often involved in financial transactions to act as a guarantor. Examples include the following:

Clearinghouse:   Clearinghouses act as intermediaries between sellers and buyers. They facilitate and guarantee a successful settlement of transactions by acting as buyers for the seller and sellers for the buyer. Examples of clearing include exchange clearing divisions such as Nasdaq Clearing and CME Clearing, as well as credit card clearing such as Visa and Mastercard.

Central Securities Depository (CSD):   A CSD is a specialized financial institution that holds financial securities such as shares and derivatives on behalf of other institutions. Similar to a clearing, CSDs act as a third party to financial transactions to guarantee successful settlement and transfer of security ownership against the payment of money. A prominent example of a CSD is Clearstream.

Custodian:   A custodian or custodian bank is a financial institution that offers securities and post-trade services to institutional investors, asset managers, banks, and other financial institutions. Custodians provide a range of services, such as holding and safekeeping their client’s securities, conducting transactions on their client’s behalf, and providing clearing and settlement services.

Payment systems:   Payment systems facilitate the secure transfer of funds between financial institutions while effectively managing settlement risks. The most prominent example is RTGS systems such as the Federal Reserve’s Fedwire in the United States, the Bank of England’s CHAPS in the UK, and the European Central Bank’s T2 (part of TARGET2 services). RTGSs are typically preferred for fast transactions and reduced settlement risk. Other services allow for deferred and netted payments, such as the US Clearing House Interbank Payments System (CHIPS). These systems are typically used for less-time-critical payments, which makes them less expensive than RTGSs.

## Analytics Data

A valuable type of financial data is analytics data, which is often derived from other types of data such as fundamental, market, and transaction data. This data is typically computed using simple formulas, statistical models, machine learning techniques, and financial theories. Examples include news and market sentiment analytics (novelty, score, relevance, impact), financial risk measures (e.g., Value at Risk, option Greeks, bond duration, implied volatility), market indexes (e.g., MSCI Global Indexes), ESG (environmental, social, and governance) scores, stock analysis, company valuation, estimates (e.g., Institutional Brokers’ Estimate System estimates), and competition analysis.

The main advantage of analytics data is that it offers pre-calculated patterns and signals, ready for immediate use in decision-making. Nevertheless, the calculation methodology used by the analytics data provider might be proprietary, which makes it a mystery box. Furthermore, as the same data becomes accessible to all market participants, maintaining a sustainable competitive advantage becomes increasingly difficult (sooner or later, someone will get the same data and replicate your strategy).