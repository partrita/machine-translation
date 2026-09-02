## Financial APIs

API stands for *application programming interface,* and it refers to a wide range of software implementations that allow one software component to interact with another. An API defines the rules, protocols, and methods for interacting between two software types.

At the highest level, an API can be described in terms of a client and a server. A client using one application sends a request to a server operating in another application. The server processes the request and returns a response to the client. For instance, when you open a social media application to upload a new image, you (the client) interact with the app provider’s server via an API.

Technically, there are several approaches to designing and implementing APIs. These include SOAP APIs, RPC APIs, GraphQL, WebSocket APIs, and REST APIs. Among these, REST APIs, which stands for Representational State Transfer, are the most popular. REST APIs primarily use the HTTP protocol for communication. They can implement various HTTP request methods such as GET (to retrieve data, e.g., account balance or transaction history), POST (to initiate a backend process), and PUT (to create or update a resource on the backend).

### Note

Although both PUT and POST can be used to create or update a resource, the main difference is that PUT is *idempotent*. This means that making the same PUT request multiple times will produce the same result each time. For example, if you submit a request through your banking application to pay an electricity bill, submitting the same request again should not result in the bill being paid twice.

APIs can be written in most programming languages, including Java, C, C++, Node.js, and Python. Java and Python APIs are quite common among data engineers. Within the Python ecosystem, frameworks such as Flask, FastAPI, and Django are widely used to program web-based APIs. To provide a short example, consider the following statement:

```
# Bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '[{"idType": "TICKER", "idValue": "AAPL", "exchCode": "UN"}]' \
     https://api.openfigi.com/v2/mapping
```

This curl command is making a POST request to the OpenFIGI API (https://api.openfigi.com/v2/mapping) to fetch mapping information for the financial instrument with the ticker symbol AAPL (Apple Inc.) on the exchange with code UN (New York Stock Exchange). To test this API request, open a terminal or command line window on your computer, paste the command, and press Enter. The response is expected to have a structure similar to this:

```
[
  {
    "data": [
      {
        "figi": "BBG000B9XVV8",
        "name": "APPLE INC",
        "ticker": "AAPL",
        "exchCode": "UN",
        "compositeFIGI": "BBG000B9XRY4",
        "uniqueID": null,
        "securityType": "Common Stock",
        "marketSector": "Equity",
        "shareClassFIGI": "BBG001S5N8V8",
        "uniqueIDFutOpt": null,
        "securityType2": "Common Stock",
        "securityDescription": "AAPL"
      }
    ]
  }
]
```

APIs are everywhere. In finance, they are extensively used for all kinds of purposes. Payment APIs, often known as payment gateway APIs, are a major application field. In simple terms, a payment gateway is a technology that facilitates the acceptance and processing of electronic payments between merchants and financial institutions. This includes credit and debit card payments, digital wallets, and bank transfers. At the core of a payment gateway technology is an API that handles all the payment lifecycle phases and allows the involved entities (merchant, processor, gateway, financial institution, etc.) to talk to each other. Among the most known payment gateway APIs are Square, Stripe, PayPal, Authorize.Net, and Adyen.

APIs play a pivotal role in accessing data from financial data vendors. These APIs are designed to allow clients to retrieve and import data programmatically, enabling the development of data-driven financial applications. For instance, Bloomberg offers the [Server API (SAPI)](https://oreil.ly/HwBFO) to allow customers to access Bloomberg Terminal data through both proprietary and third-party applications. Similarly, LSEG (formerly Refinitiv) provides the [Eikon Data API](https://oreil.ly/Dd94Z), a Python-based library that enables users to access Eikon data using Python.

### Tip

When ingesting financial data from external sources, check if the data provider has an API in place. Using the API can be quite convenient and accelerate development. At the same time, make sure you check any vendor-specific API limitations that might impact your application, such as a single-request size limit (e.g., 100 prices per request), request rate limits (e.g., 1K requests/day), request timeout, and maximum concurrent requests. If you’d like to learn more, check the FactSet’s Formula API limitations available on the vendor’s official [web page](https://oreil.ly/fpfkn).

# Financial Data Sharing with Open Finance, Open Banking, and Financial APIs

Recently, there has been [growing interest](https://oreil.ly/Srug5) among financial market participants in open finance initiatives. These initiatives seek to establish a digital ecosystem that enables seamless sharing of financial data between financial institutions and third-party service providers. The primary driver of this new paradigm is to foster collaboration among market participants to produce better goods and services driven by financial data.

The most popular example of an open finance initiative is commonly referred to as [*open banking*](https://oreil.ly/X5d0V), in which traditional banking institutions and third-party service providers such as FinTech firms collaborate to provide innovative financial products. To facilitate collaboration, banks and FinTechs share data using ad hoc financial APIs.

Various regulatory frameworks have been developed to promote open finance. For example, the [second Payment Services Directive (PSD2)](https://oreil.ly/v3G1E), adopted in 2015 by the EU, imposed an obligation on banks to facilitate access to payment data for third-party service providers via a secure interface. To promote a wider open finance ecosystem that goes beyond payment account data, the EU proposed the [Financial Data Access legislation](https://oreil.ly/t0Ai6), whose main goal is “to establish a framework governing access to and use of customer data in finance.”

Special types of open banking enablers, regulated under frameworks such as PSD2 in Europe, include *Account Information Service Providers* (AISPs) and *Payment Initiation Service Providers* (PISPs). An AISP, or a company with an AIS license, collects, aggregates, and facilitates access to a user’s financial information across accounts held with various institutions. PISPs, on the other hand, facilitate direct payments from the consumer’s bank account to online merchants.

Various enablers have emerged to offer platforms for open banking. For instance, Tink, a Swedish company later acquired by Visa, facilitates connections to over 6,000 banks throughout Europe. Another example is Powens, a French company that connects over 1,800 institutions across numerous European countries, providing an open finance platform to its clients.

Crucially, it is important to keep in mind that financial APIs are not simply a bunch of FastAPI or Flask methods. Instead, APIs should be designed with business, user, and application requirements in mind. For example, JPMorgan Chase [classifies financial APIs into data and service APIs](https://oreil.ly/UbV9U). Data APIs are mainly used to request financial data, but they can be designed in a way that they can be essential tools for building applications, enable external collaborations, and be reusable across multiple departments, channels, and product lines. Service APIs, on the other hand, are used to create and trigger an instance of a service, such as initiating a payment, a balance inquiry, or requesting a change from the bank. Many firms use the term *API integration* to denote a strategy where applications are connected via their APIs. The goal is to create an infrastructure in which data exchange and communication occur seamlessly through APIs, facilitating creativity and innovation.

When designing a financial API, the two most important elements to consider are performance and security. API performance is often measured by the ability of the system to scale to a large number of concurrent requests, as well as its request response time. Measures such as “hits per sec and “requests per sec” are often used for this purpose. The idea is to measure the ability of an API to handle a large number of requests/hits in one second. Common API performance optimization techniques involve load balancing, caching, rate limiting, and throttling, among others.17

As for security, the primary elements to consider are authentication and authorization to control how and who can interact with the API. Tools such as firewalls, authentication tokens, OAuth 2.0, API keys, and API gateways are often used for this purpose.18 In addition, APIs need to be protected against advanced malicious attacks such as SQL injection (SQLi). In SQLi, a cybercriminal exploits application vulnerabilities to inject malicious input into an API request that alters the behavior of a backend SQL query. For example, let’s take a naive scenario where the user is required to insert their user ID to access their account balance. Upon providing such credential (e.g., user ID: 267), an API request is sent to the backend, which then executes the following SQL query:

```
-- SQL
SELECT first_name, last_name, account_balance
FROM user_accounts
WHERE user_id = 267
```

Now, if the API doesn’t handle SQL injection properly, then it is possible to provide input such as user ID “267 OR 1=1”. In this case, your backend may end up executing the following query:

```
-- SQL
SELECT first_name, last_name, account_balance
FROM user_accounts
WHERE user_id = 267 OR 1=1
```

Because the SQL condition 1=1 always evaluates to TRUE, the entire WHERE statement will be true, regardless of whether the provided user ID is correct. In this case, the entire list of users and their account balances will be queried, which may lead to major data breaches.19

## Financial Data Feeds

In the financial industry, the term “data feed” refers to a mechanism designed to deliver the latest financial data and updates to traders, investment firms, and financial institutions. The main sources of data feeds include stock exchanges, financial news providers, and market data vendors.

Financial data feeds can be designed to transmit data either as historical snapshots or, more commonly, in live mode. When provided in live mode, a data feed offers a continuous stream of real-time data, essential in scenarios where timely data access is critical. Moreover, data feeds often include features that allow users to configure the timing, location, and specific data they want to receive. Financial data feeds may vary in terms of latency, throughput, and delivery guarantees.

Examples of financial data feeds include S&P Global’s [Xpressfeed](https://oreil.ly/YSXP4), which offers access to over 200 datasets and allows users to customize data extraction and delivery locations. LSEG’s [Real-Time – Ultra Direct](https://oreil.ly/5b6MT) is another example, providing a high-performance, low-latency real-time market data feed. In addition, Bloomberg provides the [Bloomberg Market Data Feed (B-PIPE)](https://oreil.ly/sPpaE). Exchange venues also offer market data feeds, such as the NYSE [Trades Data Feed](https://oreil.ly/bqaDN) and NASDAQ [Market Data Feeds](https://oreil.ly/h3pK6), which stream trading data as it happens and often provide the lowest latency due to being the original data source. Finally, news feeds, like those from [MT Newswires](https://oreil.ly/Yx7Vk), are a common type of data feed, delivering real-time news headlines and text.

One challenge when dealing with financial data feeds is information overload. This happens when a large volume of data from one or more feeds overwhelms the existing financial data infrastructure. The adoption of cloud technology has alleviated this issue by allowing financial institutions to store and retrieve data at any scale without the need to manage and maintain the underlying infrastructure.20

## Secure File Transfer

File transfer is one of the most frequent and regular operations in the financial sector. Banks, for example, transfer files for loan applications, transaction history, and account information; investment firms transfer trade data, portfolio composition, and intellectual property files like investment strategy or trading algorithms; insurance companies transfer client policy and personal information files; and regulated financial institutions must submit various filings to comply with regulatory reporting requirements.

Importantly, files transferred by financial institutions often contain sensitive information. As a result, file sharing needs to be secured to meet the financial sector’s security and privacy requirements. To this end, a widely used technology is the *Secure File Transfer Protocol* (SFTP), which leverages the SSH protocol to encrypt data and commands that one machine submits to another. SFTP is secure, reliable, and platform independent.

File transfer via SFTP is a good solution for bulk and large file transfers. It is also often used when there isn’t an API available for data exchange. Crucially, SFTP may not be the best option for all use cases. For example, it may not be ideal in high-speed and large-volume data-driven systems characterized by demanding workloads. Furthermore, SFTP may require a security policy to manage passwords, keys, and user access, which can increase the complexity of file transfer.

Various alternatives have been proposed to address these issues. For instance, managed SFTP solutions, like [Managed File Transfer (MFT)](https://oreil.ly/wehCT), provide enhanced enterprise-level functionality for security, performance, compliance, and reporting beyond what standard SFTP offers. Additionally, protocols such as FTPS (a more secure form of FTP), SCP (Secure Copy Protocol), and WebDAV (Web Distributed Authoring and Versioning) can be utilized depending on the specific business requirements.

## Cloud Access

With the widespread adoption of cloud computing across nearly every sector, cloud-based data sharing and access has emerged as a reliable and convenient way to exchange data. In its simplest setup, a data provider creates a storage bucket or cloud database within a dedicated and isolated cloud environment. It then uploads the data and authorizes the target user to access and manipulate it. Subsequently, whenever new data updates are available, the provider uploads them to the storage location, enabling immediate access for the user.

One convenient aspect of this access method is that users can leverage various cloud-based features when working with the data, including user interfaces, querying capabilities, data management, search functions, and more. Furthermore, there are cost-saving benefits and seamless integration experience with other cloud services, particularly for clients already utilizing the cloud. For instance, if your data pipelines are already processed in the cloud, having a new data source accessible directly through the cloud simplifies workflow management. Additionally, data updates occur continuously with minimal intervention required on the user’s part.

Here are a few examples. In 2022, Bloomberg and Google announced a new [partnership](https://oreil.ly/4s0DX) that will allow mutual customers to easily access B-PIPE, Bloomberg’s real-time market data feed, through Google Cloud. Similarly, CME Group, the world’s leading derivatives marketplace, [partnered with Google Cloud](https://oreil.ly/g71UV) to provide fast and reliable market data access to their customers.

# Case Study: FactSet Integration with AWS Redshift and Snowflake

FactSet is a well-known financial data vendor that provides content to more than 160,000 investment professionals worldwide. FactSet has expanded its data delivery options in the past few years to include cloud-based access. For example, it is now possible to access 100+ FactSet proprietary and third-party financial datasets through popular cloud data warehouse services such as [AWS Redshift](https://oreil.ly/li3AQ) and [Snowflake](https://oreil.ly/zdMKq).

With this cloud-based delivery, FactSet saves its clients the need to clean, model, and normalize the data. It is already populated in SQL tables and is ready for users to query. Data is constantly updated and added to existing tables. In addition, if the user relies on both FactSet proprietary data and third-party vendor data offered via FactSet, cloud delivery allows centralization and integration of disparate data sources into a single platform such as Redshift or Snowflake.

Cloud providers have recently increased their market competition in the financial data market. This is expressed by the emergence of the so-called financial data marketplaces. These managed cloud solutions allow financial data providers to distribute and share their data through a single cloud interface. This may be convenient for financial data providers as it eliminates the need to build and maintain an infrastructure for data storage, distribution, billing, and user management. Examples include [AWS Data Exchange for Financial Services](https://oreil.ly/d2clm) and [Google Cloud Datashare for financial services](https://oreil.ly/dFU-K). Cloud marketplace data can be delivered in a variety of ways. For example, Google Datashare distributes data in batches through its managed warehouse solution BigQuery and in real time through its managed messaging service Pub/Sub.

## Web Access

A user-friendly and straightforward way to access financial data is through a dedicated web page provided by a financial institution or data vendor. In this web access mode, financial data can be downloaded in file format, queried and visualized using a query builder, or quickly parsed and analyzed by the user.

This mode is convenient for handling small datasets or when speed is not critical, such as for scheduled data extractions. However, for faster data access or bulk file downloads, alternative data ingestion technologies like SFTP, API, or cloud-based solutions are more suitable.

## Specialized Financial Software

In certain financial data exchange settings, specialized or dedicated software is implemented. This is particularly common when setting up standardized systems for secure financial messaging, payments, transactions, and other market operations.

An example of specialized financial software is [FIX engines](https://oreil.ly/wt8SS), which are software applications that enable two institutions to exchange FIX messages (discussed in the previous section). The FIX engine handles the network connection, transmits and receives FIX messages, and validates the submitted messages against the FIX protocol and format.

# Data Ingestion Best Practices

When building a data ingestion layer, it is important to make sure it is rock solid. A poorly designed data ingestion layer may easily become the bottleneck of your infrastructure and impact the entire financial data engineering lifecycle. Adhering to best practices can help ensure the resilience of this layer. This section discusses a few.

## Meet Business Requirements

First of all, the data ingestion layer needs to meet the business requirements established by your financial institution. Don’t overcomplicate the ingestion layer; if your organization wants to work and exchange CSV and Excel files, then build a simple ingestion layer that can process these formats. If an API is not going to bring great benefits, don’t build one and instead use a simple filesystem or cloud storage solution. However, if your company has complex data ingestion needs, consider building an extensible and flexible layer that can handle new types of formats and ingestion mechanisms.

## Design for Change

Change is a constant in financial markets. New practices, standards, and regulations are continually taking place across the industry. For example, it is not unusual for markets to begin migrating to a newly published standard, and, in the meantime, a new standard emerges to replace it.21 For this reason, always consider the change dynamics that might affect your data ingestion layer. There isn’t a fixed recipe for managing change, but you can consider best practices such as the following:

Incremental change:   Make small and gradual changes.

Isolated change:   Make sure you develop and test your changes in isolation and avoid release incompatibility.

Documented change:   Make sure you describe the what, how, and why of your changes so others can understand what will change.

Zero downtime:   Roll out changes using a reliable technique with a rollback option to ensure zero downtime and avoid disruption to end users. Examples include Blue/Green, Canary, and Rolling deployment techniques.22

## Enforce Data Governance

Enforcing data governance at the ingestion layer is recommended in financial applications. Examples of good practices include the following:

Data validation:   Add validators to check the conformity of ingested data to defined acceptance criteria. For example, you can validate if a file format is CSV or XML, validate an ingested message against standard requirements (e.g., FIX or XBRL), or validate ingested data against errors and quality issues.

Logging and reporting:   Consider having an audit log that records all ingestion events. This is useful for tracking wrongful or malicious ingestions and for regulatory reporting.

Lineage and visibility:   Implement a mechanism that allows ingested data to be traced back to its origin. The goal is to determine when, how, and where a particular piece of data entered the system.

Security:   The data ingestion layer is the entry point for your financial data infrastructure. This means that it can be exploited by cybercriminals to ingest malicious data or software. To this end, ensuring the security of your data ingestion needs to be a top priority. Malicious data can be ingested in different ways, such as malware files, SQL ingestion, and data poisoning.23 Security can be ensured via proper authentication and authorization policies, user permission management, virus scanning, allowed file formats (e.g., you may want to discard zip or pickled files), API security, and more.

## Perform Benchmarking and Stress Testing

A good practice when building a data ingestion layer is performing a stress test to check the infrastructure’s ability to handle variable workloads and ingestion scenarios. This is particularly essential when designing an event-driven or real-time data ingestion layer. A useful testing technique is benchmarking, which can be useful when choosing between different ingestion technologies. A benchmarking tool can be used for assessing the performance of a given ingestion technology by simulating a realistic workload scenario.24

# Summary

In this chapter, you explored the first layer of the FDEL: ingestion. This layer acts as the entry point to a financial data infrastructure, enabling data to be ingested through various arrival processes, transmission protocols, formats, and technologies. This chapter covered various aspects of ingestion specific to financial data, focusing on the unique requirements and preferences of market participants.

The ingestion layer should be regarded as a vital component of your FDEL. Bottlenecks at this stage can lead to performance issues further downstream. Additionally, a robust ingestion system is becoming increasingly essential for financial institutions due to the growing trends in data sharing, the expanding variety of data formats and arrival processes, and the increasing volumes of ingested data.

At this point, you may be asking yourself, “Where does the ingested data go?” This takes us to the next layer, storage, which will be covered in Chapter 8. In this layer, a data storage system is used to store and retrieve data according to specific business and technical requirements. As you might have guessed, this is the layer where you implement the most popular technology in data engineering: a database.

Let’s continue!

1 For more on this topic, I recommend reading this blog post by Google Cloud: [“Authorize with SSL/TLS Certificates”](https://oreil.ly/acqDy).

2 To learn more about VPCs and subnets, I recommend checking the documentation of AWS on [IP addressing for your VPCs and subnets](https://oreil.ly/4doEy).

3 Systems that can handle duplicate ingestions reliably are often called *idempotent.* To learn more about this topic, I recommend the article [“Idempotency and Ordering in Event-Driven Systems”](https://oreil.ly/4NBlF), by Wade Waldron.

4 For a detailed study on this topic, I recommend Sunila Gollapudi’s [“Aggregating Financial Services Data Without Assumptions: A Semantic Data Reference Architecture”](https://oreil.ly/w_D42), in the *Proceedings of the 2015 IEEE 9th International Conference on Semantic Computing* (IEEE, 2015): 312–315.

5 The full guide is available on Snowflake’s [website](https://oreil.ly/WCto4) and it assumes you have satisfied all the necessary requisites such as granting roles and permissions between Snowflake and AWS S3, creating the Snowflake table, and other tasks.

6 To upload files into a stage location, you need to use the Snowflake [PUT command](https://oreil.ly/S1shG).

7 XML’s popularity has remarkably increased in recent years. To read more about this topic, see [“Making Life Easier in an XML World”](https://oreil.ly/rDSVR), by Denise Warzel.

8 For a comparison of Avro and Parquet formats, see [“AVRO vs. PARQUET” by Snowflake](https://oreil.ly/m7AU9).

9 See, for example, Aldane Haldane, Robleh D. Ali and Paul Nahai-Williamson’s [“Towards a Common Financial Language”](https://oreil.ly/Xy3id), presented at the Securities Industry and Financial Markets Association Symposium on “Building a Global Legal Entity Identifier Framework,” New York, 2012.

10 The sample message was taken from the [“Sample Messages Document”](https://oreil.ly/2_9YW), by NYSE. A dictionary of all FIX tags and their meaning is [available online](https://oreil.ly/ykUfo).

11 Detailed technical specifications on FIX networks and engines are available at the [FIX community website](https://oreil.ly/wt8SS).

12 For more details, check the [official XBRL Essentials guide](https://oreil.ly/PeX4W).

13 The source of this example is the [official FpML Coding Schemes documentation](https://oreil.ly/RjvBJ).

14 To see the full message body and have a more detailed idea about the meaning of the tags, download the full message data [online](https://oreil.ly/ZEQIf).

15 To learn more about the ISO 20022 registration process, see the official web page on the [development of new ISO 20022 message definitions](https://oreil.ly/zkMX3).

16 For a detailed analysis, I recommend checking the implications of ISO 20022 on the payment industry. For this reason, I highly recommend the paper by Steve Goswell, [“ISO 20022: The Implications for Payments Processing and Requirements for Its Successful Use”](https://oreil.ly/PQ4k-), *Journal of Payments Strategy & Systems* 1, no. 1 (Autumn 2006): 42–50.

17 To learn more about these and other API optimization topics, I highly recommend the book by De Brajesh, *API Management: An Architect’s Guide to Developing and Managing APIs for Your Organization* (APress, 2017).

18 For a good reference on API security, see Neil Madden’s *API Security in Action* (Manning, 2020).

19 For a detailed analysis of SQL injection, I recommend the seminal paper by William G. Halfond, Jeremy Viegas, and Alessandro Orso, [“A Classification of SQL Injection Attacks and Countermeasures”](https://oreil.ly/OEjX1), in the *Proceedings of the International Symposium on Secure Software Engineering*, vol. 1, (March 2006): 13–15.

20 For an overview of this issue, see [“The Relentless Rise of Real-Time Data”](https://oreil.ly/YbMMX), by LSEG.

21 For a good reference on this problem, I recommend Chris Pickles’ [“Securities Standards Migration: ISO 15022 vs ISO 20022”](https://oreil.ly/s9Rcc), *Journal of Securities Operations & Custody* 1, no. 3 (Spring 2008): 289–300.

22 To learn about these techniques, I suggest Chaitanya K. Rudrabhatla’s [“Comparison of Zero Downtime Based Deployment Techniques in Public Cloud Infrastructure”](https://oreil.ly/G_3aC), in the *2020 Fourth International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud)* (IEEE, 2020): 1082–1086.

23 Data poisoning is a type of attack where data is intentionally ingested to alter the performance or behavior of a machine learning model. For more on this topic, I recommend Antonio Emanuele Cinà, Kathrin Grosse, Ambra Demontis, Sebastiano Vascon, Werner Zellinger, Bernhard A. Moser, Alina Oprea, Battista Biggio, Marcello Pelillo, and Fabio Roli’s [“Wild Patterns Reloaded: A Survey of Machine Learning Security Against Training Data Poisoning”](https://oreil.ly/BZzlz), *ACM Computing Surveys* 55, no. 13s (July 2023): 1–39.

24 For a reference on benchmarking financial data ingestion, I recommend Manuel Coenen, Christoph Wagner, Alexander Echler, and Sebastian Frischbier’s [“Benchmarking Financial Data Feed Systems”](https://oreil.ly/gw2JN), in the *Proceedings of the 13th ACM International Conference on Distributed and Event-based Systems* (June 2019): 252–253.

# Chapter 8. Data Storage Layer

In the previous chapter, you learned how the data ingestion layer works, including the mechanisms, technologies, and formats used to ingest data into a financial data infrastructure. Once ingested, data must be stored and persisted in a storage location for further processing and querying. This is where the data storage layer comes into the picture.

To help you understand how to build a robust storage layer, this chapter will provide you with the necessary fundamentals and concepts, along with illustrations of technologies and their applications in finance. First, you’ll learn how to approach the design of a data storage system (DSS) using appropriate criteria. Next, the concept of a data storage model (DSM) and its categorization criteria will be introduced. Then, I will present a comprehensive list of DMSs relevant to the financial industry, highlighting each DMS’s key features, data modeling concepts, technical implementations, and financial applications.

# Principles of Data Storage System Design

Throughout this book, I use the term *data storage system* (DSS) to denote a software implementation that enables the storage and retrieval of data. In many cases, people use the term “database” to refer to a storage solution. However, databases are only one type of DSS, albeit a popular one.

As a financial data engineer, knowing how to assess, choose, design, and implement a DSS should be one of your primary skills and areas of knowledge. The DSS is a core component in several financial applications, such as trading, payment, and messaging platforms. Making the wrong DSS choice can be quite costly and lead to a notable impact on the performance and reliability of your infrastructure. If a change is required later, you might find yourself dealing with a complex and expensive data migration project that wastes resources and time. This is particularly true when other applications and layers have already been built on top of the existing DSS.

Designing the appropriate DSS may look overwhelming at first glance. This is because of the vast number of technologies, patterns, constraints, business requirements, and marketing materials that affect the decisions around a DSS. To address this challenge, this section will provide a set of universally applicable principles that can guide your DSS design and implementation strategy.