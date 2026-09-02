## Alternative Data

Alternative data refers to a variety of nonconventional data that can be used for financial analysis, investment, or forecasting. It is regarded as nonconventional since it does not primarily originate within the traditional context of financial markets, such as trading, prices, transactions, and corporate finance operations. Examples include news, social media posts, satellite images, patents, Google trends, consumer behavior, technology analysis, political analysis, environmental and reliability scores, and many more. A large number of alternative datasets are available through data vendors, but it is also possible to extract similar data from the internet and other public repositories.

The main advantage of alternative data lies in its novelty and diversity. A financial institution equipped with the expertise and resources to extract and clean alternative data sources stands to gain a competitive informational advantage, which can significantly improve portfolio analysis and returns. For example, one [study](https://oreil.ly/FH1iQ) used satellite image data to show that the number of cars in the parking lots of a sample of public US companies may be used as a predictor of financial performance.

A variety of challenges might be encountered when working with alternative data. The main issue is that these datasets are often available in an unstructured and raw format, necessitating substantial investment to structure the data and extract valuable insights. Another challenge is the lack of standardized entity identifiers and references, unlike conventional financial datasets. Moreover, alternative data can be imbalanced or incomplete because its observations and events are not consistently captured, unlike the systematic data collection for traditional datasets such as publicly traded stocks. Finally, alternative datasets can easily be biased yet provide no additional information to detect such biases.13

## Reference Data

Financial reference data is a type of metadata used to identify, classify, and describe financial instruments, products, and entities. It is crucial for various financial operations, including transactions, trading, clearing and settlement, regulatory reporting and compliance, data consolidation, and investment.

To understand what reference data is, it’s helpful first to review the concept of a financial instrument. Simply put, a financial instrument is a contract between two parties that has monetary value and can be traded on financial markets. Examples include debt instruments such as bonds and loans, equity instruments such as stocks, derivative instruments such as options and futures, and foreign exchange instruments such as currency pairs and currency futures. Importantly, each financial instrument comes with its own set of terms and conditions that define its contractual specifications. In this context, reference data is typically used as a metadata resource to describe these terms and conditions. [Table 2-9](#ch02_table_10_1724776825557850) presents a few examples of reference data for several financial assets.

Table 2-9. Reference data for different asset classes

| Asset category       | Reference data fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Fixed income (bonds) | * *Issuer information:* name, country, sector * *Security identifiers:* ISIN; CUSIP, etc. * *Instrument information:* issue date, maturity date, coupon rate and frequency, currency, current price, yield to maturity, accrued interest * *Bond features:* callable, putable, convertible, payment schedule, settlement terms * *Credit information:* credit rating, credit spread                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Stocks               | * *Basic information:* identifiers such as ticker or ISIN, company name, exchange, sector, industry * *Price and volume information:* current, open, close, high, low prices, volume, average volume * *Dividend information:* dividend yield, dividend per share, dividend payment date, ex-dividend date * *Corporate actions:* stock splits, dividend distribution, buybacks, and mergers and acquisitions * *Fundamental information:* earnings per share, price-to-earnings ratio, book value per share                                                                                                                                                                                                                                                                                                 |
| Funds                | * *Fund structure:* umbrella fund, subfunds, share classes * *Identification information:* fund/subfund/share class name, type, identifiers such as ISIN, inception date, currency, domiciliation * *Fund management:* fund manager, management company, custodian, distributor, investment strategy, and fees such as management and advisory fees * *Performance:* net asset value (NAV), NAV calculation frequency, historical returns, benchmark index * *Holdings and allocation:* top holdings, sector, geographical, and asset allocation * *Risk profile:* volatility, Sharpe ratio, beta, alpha, hedging policy * *Investment, distribution, and dividends*: distribution frequency, distribution restrictions, dividend yield, subscription and redemption terms, cutoff times, minimum investment |
| Derivatives          | * *Basic information:* instrument type, underlying asset, identifiers, classification * *Contract specifications:* contract size, expiration date, settlement date, exercise style, strike price * *Pricing information:* premium, mark-to-market price, bid/ask price * *Underlying asset information:* underlying asset price, volatility, dividend yield * *Risk metrics:* delta, gamma, theta, implied volatility, etc. * *Trading information:* open interest, volume * *Counterparty information:* name, credit rating, collateral requirements * *Corporate action adjustments:* stock splits on the underlying asset                                                                                                                                                                                 |

Managing reference data is one of the most outstanding challenges in financial markets. In some cases, reference data is simple. For example, a stock is a standard financial instrument widely understood to represent an ownership stake in a firm. Stock reference data includes identifiers such as its ticker, the dividend rate if it pays dividends, and the legal issuing entity. Nevertheless, exotic and more complex financial instruments have been introduced with the evolution of financial markets. This is particularly the case with financial derivative instruments. For example, identifying an option contract requires information about the underlying asset, strike price, expiration date, option type (e.g., call or put), style (American versus European), and possibly other factors such as dividend yields or implied volatility. Furthermore, derivative instruments come in great variety, each with unique characteristics and terms. Such characteristics might even change with time, either through contractual adjustments or market events, or be customized to meet clients’ specific needs.14

Many financial transactions and settlements fail due to operational errors, often linked to poor reference data. These errors can stem from inaccuracies in settlement instructions, trade-specific details, client and counterparty information, instrument data, or corporate actions data. For example, incorrect client details, mismatched account information, or erroneous security identifiers can lead to misrouted payments and failed trades. Consequently, maintaining accurate and up-to-date reference data is crucial for smooth transaction processing and minimizing operational risks.15

This has led to the development of proprietary or firm-specific reference data descriptions. As a result, market participants and regulators have struggled to agree on standard terms, definitions, and formats for financial instruments, which is the primary challenge in reference data management.

Another significant challenge with reference data is the absence of a unified identification system for financial instruments. Various financial identifiers have been created, each serving different purposes and possessing unique features. Market participants’ use of different identifiers makes it increasingly difficult to match financial instruments across different identification systems. This issue is explored in greater detail in Chapter 3.

Several initiatives have been launched to address the challenges of reference data in financial markets. The International Organization for Standardization [established a dedicated committee](https://oreil.ly/Gwb_E), ISO/TC 68/SC 8, whose scope is “standardization in the field of reference data for financial services.” In the United States, the Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010 mandated that the *Office of Financial Research* (OFR) [prepare and publish a financial instrument reference database](https://oreil.ly/nRGOx). In the European Union, the *Financial Instruments Reference Data System* (FIRDS) was established to [collect and publish reference data on financial instruments](https://oreil.ly/VbSMb). This system operates under Article 27 of Regulation (EU) No 600/2014 (MiFIR) and Article 4 of Regulation (EU) No 596/2014 (MAR). Managed by the European Securities and Markets Authority (ESMA), FIRDS ensures the availability and transparency of financial instrument data, aiding in regulatory compliance and market supervision.

In the financial data market, several commercial reference data solutions stand out. Notable examples include Bloomberg’s [reference data](https://oreil.ly/OC0r7) and LSEG’s [reference data](https://oreil.ly/IDpuM) offerings. Reference data could be offered in a form that matches the requirements set by specific regulatory regimes, such as MiFID II, Europe’s Securities Financing Transactions Regulation (SFTR), and the Basel Committee’s Fundamental Review of the Trading Book (FRTB). Additionally, some reference data services focus on financial entities, such as [SwiftRef](https://oreil.ly/NEwa1), which provides comprehensive international payment reference data. SwiftRef offers detailed information on BICs (Business Indentifier Codes), IBAN (International Bank Account Number) validation, and various other identifiers crucial for identifying entities involved in global payments.

In Chapter 3, we will explore the most essential types of reference data, focusing specifically on financial security identifiers.

## Entity Data

Entity data includes information about corporate entities and their characteristics. It is frequently used alongside reference data to offer more detailed insights into a specific entity. Examples of entity data elements include the company name, identifiers, year of establishment, legal corporate form, ownership structure, sector classification, associated individuals, credit rating, ESG score, risk exposures, major corporate events, and more.

A number of commercial entity datasets are available, such as LSEG’s [legal entity data and services](https://oreil.ly/OwcOq), Moody’s [Orbis database](https://oreil.ly/2-G-_), and SwiftRef’s [entity data](https://oreil.ly/WRxWt). These datasets are used for many useful purposes such as corporate finance analysis, risk management (e.g., supplier or credit risk), and compliance and financial crime prevention through anti-money laundering (AML), know your customer (KYC), and client due diligence (CDD).

# Benchmark Financial Datasets

As you have seen from our discussion thus far, financial data is abundantly available from multiple sources and in a variety of types and structures. To extract analytical and economic value from this data, commercial vendors, financial institutions, and researchers create *financial datasets*. I define a financial dataset as a bundled collection of variables and data points that provide information on a specific financial entity or topic, such as loans, stock prices, index prices, bond markets, and derivative markets. A financial dataset can include a mix of data types, such as fundamentals, market data, transactions, analytics, reference data, and entity data.

A considerable number of financial datasets already exist in the market, and new datasets are continuously being created and published. Next, I’ll provide an overview of some of the world’s most trusted and used financial datasets.

## Center for Research in Security Prices

Financial datasets provided by the Center for Research in Security Prices (CRSP) are among the most prominent and trusted sources of market data. In particular, the [CRSP US Stock dataset](https://oreil.ly/syxTE) provides comprehensive daily and monthly stock market data on over 32,000 securities listed on US stock exchanges such as the NYSE and NASDAQ and on a broad range of market indexes. The CRSP US Stock dataset contains information on price and quote data as well as external identifiers, shares outstanding, market capitalization, delisting information, and corporate action details.

## Compustat Financials

[Compustat Financials](https://oreil.ly/2vVPz), also called Compustat Fundamentals or Compustat Global, is the world benchmark dataset for company fundamentals. It provides standardized information on more than 80,000 international public companies. Compustat provides point-in-time snapshots of fundamental data, allowing researchers to conduct reliable historical and backtesting analyses. The dataset is quite comprehensive, with over 3,000 fields conveying information on financial statements, ratios, corporate actions, industry specifications, identifiers, and more.

## Trade and Quote Database

The daily [Trade and Quote (TAQ) dataset](https://oreil.ly/dak4D) provides daily high-frequency data on all trades and quotes that take place on the NYSE, NASDAQ, and other regional exchanges. TAQ data is available starting from 2003. The distinguishing feature of TAQ is the time precision it offers: seconds (HHMMSS) since 1993, milliseconds (HHMMSSxxx) since 2003, microseconds (HHMMSSxxxxxx) since 2015, and nanoseconds (HHMMSSxxxxxxxxx) since 2016.

## Institutional Brokers’ Estimate System

The [Institutional Brokers’ Estimate System (I/B/E/S)](https://oreil.ly/DnDlJ) is a database maintained by LSEG, serving as the market benchmark for stock analysts’ earnings estimates for publicly traded companies. Over 950 firms and more than 19,000 analysts from 90+ countries regularly contribute to the I/B/E/S. The database provides extensive coverage of over 60,000 companies, with data available from 1976 for North America and from 1987 for international markets.

## IvyDB OptionMetrics

[IvyDB](https://oreil.ly/11soK) is the market benchmark dataset for historical equity and index options data. The most popular version of IvyDB is the US database, but since 2008, IvyDB Europe has been available as well. IvyDB provides a rich set of options data fields, such as daily quotes, identifiers, volume, computed implied volatility, option Greeks, open interest, interest rates, maturity, exercise, and exercise price. Information on the underlying instruments is also available, including closing prices, dividends, and corporate action information.

## Trade Reporting and Compliance Engine

[Trade Reporting and Compliance Engine (TRACE)](https://oreil.ly/4_NLG) is a financial dataset on bond and fixed-income transactions. TRACE represents an indispensable data source as most bond transactions happen OTC, making it a less transparent market than centrally exchanged instruments such as stocks.

TRACE itself is a program created by the Financial Industry Regulatory Authority (FINRA) to enable market participants who are FINRA members to report their fixed-income OTC transactions. FINRA members are required to report their transactions within 15 minutes of execution, which is then made available in real time to TRACE subscribers. Data available via TRACE includes fields such as execution time, price, volume, and bond yield.

## Orbis Global Database

[Orbis](https://oreil.ly/FI-K0) is the industry’s primary resource for global entity data. Published by Moody’s Analytics, it contains information on more than 450 million private and listed companies worldwide, offering detailed financial information for many of them.

In addition to its global coverage, Orbis provides comparable information on company ownership structure and financial strength metrics. Orbis collects data from more than 170 data providers and hundreds of its own data sources. The data is further enriched and standardized to enable easy querying, analysis, and comparison.

## SDC Platinum

[SDC Platinum](https://oreil.ly/Cn-I2), offered by the London Stock Exchange Group (LSEG), is a premier source of comprehensive global corporate finance and market deal event data. It provides detailed information on various financial transactions, including mergers and acquisitions, alliances, private equity, venture capital, new issues, leveraged buyouts, and syndicated loans, among many others.

## Standard & Poor’s Dow Jones Indices

[Standard & Poor’s Dow Jones Indices (SPDJI)](https://oreil.ly/C_qDU) is a leading global index provider and a primary source of historical index data, offering a wide range of indexes across various markets, including equities, derivatives, fixed income, and commodities. Examples include the S&P 500, S&P MidCap 400, and S&P SmallCap 600, which are widely recognized as leading indicators of US equity market performance. S&P DJI provides detailed data features such as index names, constituents and their weights, closing prices, market capitalization, constituent company information, and index-related events.

## Alternative Datasets

The datasets illustrated so far are general in scope and generated through the traditional mechanisms of financial markets. Interestingly, alternative, more specialized datasets have been gaining popularity among market participants. Let’s look at a few examples.

### BitSight Security Ratings

[BitSight Security](https://oreil.ly/L_6K8) is a world leader in cybersecurity rating and related analytics. BitSight ratings convey comparable insights and visibility into a company’s cybersecurity risk. It provides adaptive ratings correlated with the changing ransomware risk landscape. BitSight ratings are calculated using objective and observable factors such as server software, open ports, TLS/SSL (Transport Layer Security/Secure Sockets Layer) certificates and configuration, web application headers, and system security.

### Global New Vehicle Registrations

The [Global New Vehicle Registrations dataset](https://oreil.ly/MeRvC), offered by S&P Global Mobility, provides daily information and analysis on vehicle registrations from more than 150 countries, 350 brands, multiple fuel types (diesel, petrol, etc.), and body types (e.g., car, van, SUV). The dataset provides valuable information that can be used to analyze trends in the automotive market, such as the transition to electric vehicles.

### Weather Source

The [Weather Source dataset](https://oreil.ly/8WBKh) provides hourly and daily weather-related data for a large number of locations worldwide. Weather Source collects and standardizes weather data from many input sources and provides weather insights relevant to different businesses.

### Patent data

Patent data is unstructured data that conveys information on patent details such as the inventor and assignee name, related patent citations, patent abstract, patent summary, detailed description, and claims. This data is often used to understand technological innovation problems. In recent years, the use of patent data has gained increasing importance in financial analysis. One of the primary sources of patent data is the [United States Patent and Trademark Office (USPTO)](https://oreil.ly/GEOi5), which provides public access to detailed patent and trademark information. Another useful source is Google Patents, which aggregates patent data from a variety of sources, including the USPTO, and makes it easily searchable via its search engine.

In conclusion, it’s important to keep in mind that the number of datasets created and used by financial markets is immense, and we have only scratched the surface in this section. As a financial data engineer, one of the most valuable skills that you can develop is the ability to search and navigate the financial data landscape and identify the right dataset for a particular business problem.

# Summary

This chapter provided an overview of the financial data landscape, which we can summarize as follows:

* Classifying and explaining the sources of financial data
* Distinguishing between the different structures used to represent financial data
* Illustrating the main types of financial data generated by the various market activities
* Providing a short of benchmark datasets widely recognized among market participants and researchers

Now that you have an understanding of what financial data engineering entails and the intricacies of the financial data ecosystem, we’ll shift gears with the next few chapters, where you will learn about specific financial data engineering topics. The following three chapters will address in depth the following problems, which have been selected based on their prominent importance for financial markets:

* Financial identification systems and their main features and challenges (Chapter 3)
* The process and methods for financial entity recognition and resolution (Chapter 4)
* Financial data governance through data quality, integrity, privacy, and security (Chapter 5)

Let’s keep going!

1 If interested in this topic, I recommend Itay Goldstein and Liyan Yang’s article, [“Information Disclosure in Financial Markets”](https://oreil.ly/_Qo5F), *Annual Review of Financial Economics* 9 (November 2017): 101–125, and Anat R. Admati and Paul Pfleiderer’s [“Forcing Firms to Talk: Financial Disclosure Regulation and Externalities”](https://oreil.ly/QlzH1), *The Review of Financial Studies* 13, no. 3 (July 2000): 479–519.

2 If interested in learning more about portfolio theory, I recommend the excellent book by Jack Clark Francis and Dongcheol Kim, *Modern Portfolio Theory: Foundations, Analysis, and New Developments* (Wiley, 2013).

3 For a good introduction to network science, I highly recommend Mark Newman’s book *Networks*, 2nd ed. (Oxford University Press, 2018).

4 For more on this topic, see Celina M.H. de Figueiredo’s article [“The P versus NP—Complete Dichotomy of Some Challenging Problems in Graph Theory”](https://oreil.ly/x5dU1)*,* *Discrete Applied Mathematics* 160, no. 18 (December 2012): 2681–2693.

5 For a good introduction to the different sources of financial text data, I recommend Mirjana Pejić Bach, Živko Krstić, Sanja Seljan, and Lejla Turulja’s article, [“Text Mining for Big Data Analysis in Financial Sector: A Literature Review”](https://oreil.ly/HsYET)*,* *Sustainability* 11, no. 5 (January 2019): 1277.

6 More on this topic in Marjan Van de Kauter, Diane Breesch, and Véronique Hoste’s [“Fine-Grained Analysis of Explicit and Implicit Sentiment in Financial News Articles”](https://oreil.ly/vts8V), *Expert Systems with Applications* 42, no. 11 (July 2015): 4999–5010.

7 To see a real example, check out the [information provided by Yahoo Finance for Google stock](https://oreil.ly/sq3Fr).

8 For a more comprehensive list, check CME Group’s [list of match algorithms](https://oreil.ly/-Llzc).

9 For a deeper explanation of the order book mechanism, I recommend Jean-Philippe Bouchaud, Julius Bonart, Jonathan Donier, and Martin Gould’s book, *Trades, Quotes and Prices: Financial Markets Under the Microscope* (Cambridge University Press, 2018).

10 For an excellent reference on this topic, I recommend Aswath Damodaran’s *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset*, 3rd ed. (Wiley, 2012).

11 To calculate the NBBO, stock exchanges report their best bid/ask prices to a system called the Securities Information Processor (SIP), which aggregates all the quotes in a single NBBO and releases it to the market.

12 Readers interested in a comprehensive coverage of the financial transaction lifecycle can read the excellent book by Robert P. Baker, *The Trade Lifecycle: Behind the Scenes of the Trading Process* (Wiley, 2015).

13 For more on this topic, see Ashby Monk, Marcel Prins, and Dane Rook’s article, [“Rethinking Alternative Data in Institutional Investment”](https://oreil.ly/Q_Oil), *Journal of Financial Data Science* 1, no. 1 (Winter 2019): 14–31.

14 For example, consider a stock option with a strike price of $100 and 100 shares underlying it. If a two-for-one stock split event takes place, managing reference data involves adjusting the option specifications to reflect 200 shares with a new strike price of $50, ensuring all related systems and records are updated accurately.

15 A more detailed discussion of this problem can be found in Allan D. Grody, Fotios Harmantzis, and Gregory J. Kaple’s article, [“Operational Risk and Reference Data: Exploring Costs, Capital Requirements and Risk Mitigation”](https://oreil.ly/1TUB7), *Journal of Operational Risk* 1, no. 3 (2006).

# Chapter 3. Financial Identification Systems

A key aspect of financial data, such as prices and transactions, is that it can provide informational value only if we can reliably assign each record to its corresponding entity. Being able to filter a dataset to get data for a specific entity unlocks the ability to analyze the data in meaningful ways.

To this end, financial market participants have developed and employed different types of financial identifiers. Nevertheless, data identification remains notably challenging and is widely regarded as one of the most critical problems in financial data management. The outstanding issue of reference data management, presented in the previous chapter, fundamentally revolves around financial identification and the matching of various identifiers that reference the same financial market entity.

This chapter will discuss the problem of financial data identification, illustrate the desired properties of financial identification systems, and examine the key features and limitations of current systems.

If you are going to become a financial data engineer, dealing with financial identifiers and knowing how to manage their shortcomings will be one of the main challenges you will regularly face. So, let’s dive into this issue.

# Financial Identifiers

The predominantly digital nature of financial market operations and transactions necessitates recording and querying them through information and database systems. At its heart, a reliable financial information system is an identification system: a way of telling who interacts with whom, a way of distinguishing one financial entity from another, and a way of finding all records that belong to the same entity. Consequently, well-identified financial data will deliver valuable insights and a significant competitive edge. To learn more, let’s further detail what financial identifiers and identification systems are, why they are essential for financial markets, and who creates and maintains financial data identification systems.

## Financial Identifier and Identification System Defined

From our discussion so far, you’ve seen how financial data is produced in large volumes and various formats, which are subsequently organized into more coherent collections known as financial datasets. Typically, each financial dataset must have an *observation unit* (or *statistical unit*) that represents the object for which information (*data points*) is available. For example, a company fundamentals dataset would have the company as the unit of observation. To distinguish data points for one unit from the others, such as company A’s data from company B’s, a data identifier (company identifier in our example) should be attached to each data point. Without an identifier, financial datasets would be of no practical use. [Figure 3-1](#ch03_figure_1_1724776826857986) illustrates the concept. The tables shown in the figure convey information about the annual revenues of different companies observed at multiple periods. The data in the left table is not very useful as it is hard to determine which firm the statistics are referencing. When the company\_id identifier is added in the right table, it becomes possible to distinguish between several companies that the data references.

### Figure 3-1. Unidentified dataset versus identified dataset

![Figure 3-1. Unidentified dataset versus identified dataset](images/fden_0301.png)

In this book, I define a financial identifier and financial identification system as follows:

> A financial identifier is a character sequence associated with a particular financial entity (e.g., company, individual, transaction, asset, document, sector group, event, etc.), enabling accurate identification of said entity across one or more financial datasets or information systems. A financial identifier can be any combination of numeric digits (0-9), alphabet letters (a-z, A-Z), and symbols. A financial identification system creates principles and procedures for generating, interpreting, storing, assigning, and maintaining financial identifiers.

There are a few more key terms that are important to establish. First, calling an identifier a code, ID, or symbol is common. Second, financial identification systems can generate identifiers following an *encoding* system or as *arbitrary IDs*. An encoding system converts words, letters, numbers, and symbols into a short, standardized format for identification, communication, and storage. The reverse process is decoding, which converts the code sequence back to its original form to make it easier to understand. Identifiers that do not adhere to an encoding system are often described as arbitrary; they are randomly created and assigned and have no particular meaning. Third, the field that deals with building financial identification systems is frequently referred to as *symbology*, a term you will often hear when learning and working with financial identifiers.

## The Need for Financial Identifiers

Financial data identifiers serve various purposes, one of the most common being the identification of financial instruments and entities involved in market transactions. This type of identification data is often referred to as reference data, as we discussed in Chapter 2.

In any financial transaction, it is crucial to include the identifiers of the exchanged instruments and the entities participating in the agreement. Additionally, the transaction itself may be assigned an identifier for tracking purposes. As a result, identifiers are integral throughout the entire lifecycle of a financial transaction, from pre-trade to trade to post-trade settlement. They facilitate swift and efficient market transactions, enhance communication among market participants, increase transparency, and reduce operational costs and errors.1

Another important use of financial identifiers is for reporting purposes. Regulatory authorities can demand various information from financial institutions, such as market exposure, capital, risk concentration, liquidity, assets and liabilities, and trades. Financial institutions need to aggregate data from multiple sources and divisions to prepare the required report. Financial identifiers are crucial in this situation since they enable data collection and consolidation, ensuring accurate and timely reporting. In addition, by adding identifiers to the reported data, regulators would find it simple to examine the information and judge the reporting institution’s compliance. Several regulatory frameworks, such as MiFID II, mandate that reporting institutions use certain financial identities when reporting data. This, in turn, imposes an extra obligation on reporting institutions to establish a reliable financial identification system.2

Financial identifiers are essential for exchange listing and trading purposes. To list and trade a financial security on a trading venue, it must be assigned an identifier. This enables investors, traders, and market makers to easily locate, track, buy, sell, and analyze financial instruments.

Last but not least, financial identifiers are required as an essential data field when performing financial data analysis. A substantial portion of financial analysis is cross-sectional, where the focus is on studying the behavior and differences among different financial entities (e.g., assets, companies, etc.). Using financial identities would enable the analyst to pick the right data sample, run quality checks and filters, eliminate duplicates, and match the same entity across numerous datasets.

## Who Creates Financial Identification Systems?

Various organizations, spanning both public and private sectors, may generate and assign a financial identifier. Some organizations develop recommendations for financial identification systems but do not issue the identifier for those who require it; others issue identifiers based on existing standards or recommendations; and still others develop and issue the identifier. Let’s explore this variety of roles and functions with some examples.

### International Organization for Standardization

The *International Organization for Standardization* (ISO) is an independent organization that creates and promotes voluntary and consensus-based international standards for various technical and nontechnical fields. It is composed of representatives from the national standards organizations of 169 countries.

Throughout the years, the ISO has demonstrated considerable interest and involvement in developing international financial identifiers. For example, the ISO standard known as the International Securities Identification Number (ISIN) has emerged as the leading identifier in international security trading, clearing, and settlement. Later in this chapter, I will cover the ISIN identifier as well as other ISO-based identifiers in detail.

Crucially, the ISO does not issue and assign identifiers for market participants; instead, this job is delegated to so-called National Numbering Agencies, which we will examine in the following section.