# Preface

With this book, you will learn fundamental concepts, common challenges, best practices, innovative frameworks, and cutting-edge technologies essential for successfully designing and building data-driven financial products and services. This book is intended to establish foundational knowledge that is accessible to individuals from diverse backgrounds, be they finance, computer science, software engineering, or academic research. It covers a wide range of carefully selected topics chosen for their market, technological, and scientific relevance. Each concept in the book is presented in straightforward language, accompanied by case studies and finance-specific examples for deeper insights. Moreover, to facilitate practical application, the final chapter presents four hands-on projects addressing various data-driven challenges related to financial markets.

To fully appreciate the story, read the chapters in order, though each chapter can also be read on its own if you prefer.

# Who Should Read This Book?

This book serves a wide audience. This includes individuals working at institutions such as banks, investment firms, financial data providers, asset management companies, security exchanges, regulatory bodies, financial software vendors, and many more. It is designed for data engineers, software developers, quantitative developers, financial analysts, and machine learning practitioners who are managing and/or working with financial data and financial data-driven products. Furthermore, the book appeals to scholars and researchers working on data-driven financial analysis, reflecting the growing interest in big data research in the financial sector. Whether you’re a practitioner seeking insights into data-driven financial services, a scholar investigating finance-related problems, or a newcomer eager to venture into the financial field with a technology-oriented role, this book is designed to meet your needs.

# Part I. Foundations of Financial Data Engineering

The first part of this book consists of five chapters, focusing on the core concepts and fundamental elements of financial data, along with the challenges associated with its management. These chapters discuss the various systems and practices employed across financial markets to manage financial data effectively.

Chapter 1 provides an introduction to the fundamentals of finance, highlighting its unique data challenges and the foundational ideas of financial data engineering. Chapter 2 dives into the complexities of the financial data ecosystem, examining its structure and key characteristics. Chapters 3 and 4 discuss financial identification and entity systems, emphasizing their significance as critical data engineering challenges within financial markets. Lastly, Chapter 5 presents a detailed framework for establishing robust data governance practices within financial institutions.

Together, these chapters establish the basic principles and concepts required to understand and practice financial data engineering.

# Chapter 1. Financial Data Engineering Clarified

Given all the payments, transfers, trades, and numerous financial activities that take place on a daily basis, can you imagine how much data the global financial sector generates? According to a [2011 report by *McKinsey Global Institute*](https://oreil.ly/UCWHq), the banking and investment sector in the US alone stores and manages more than one exabyte of data. To put that in perspective, an exabyte is the equivalent of one billion gigabytes, and it translates into trillions of digital records. The same report shows that on average, financial services firms generate and store more data than firms in other sectors. Some statistics are even more astonishing; for instance, JPMorgan Chase, the largest bank in the United States by market capitalization, [manages more than 450 petabytes of data](https://oreil.ly/b3IWP). Bank of New York Mellon, a global financial services company specializing in investment management and investment services, [manages over 110 million gigabytes of global financial data](https://oreil.ly/svSHz).

Naturally, we might extrapolate these estimates and figures to tens or even hundreds of exabytes if we take into account the global context and the constantly expanding financial landscape. As a result, data sits at the heart of the financial system, serving as both the input for different financial operations and the output generated from them. Importantly, to guarantee a healthy and well-functioning system, a reliable and secure data infrastructure is needed for generating, exchanging, storing, and consuming all kinds of financial data. In addition, this infrastructure must adhere to the financial sector’s specific requirements, constraints, practices, and regulations. This is where financial data engineering comes into the scene. To get started, this chapter will introduce you to finance, financial data engineering, and the role and skills of the financial data engineer.

# Defining Financial Data Engineering

Data engineering has always been a vibrant and innovative field from both industry and research standpoints. If you are a data engineer, you are likely aware of how many data-related technologies are released and popularized every year. Several factors drive these developments:

* The growing importance of data as a key input in the creation of digital products and services
* Large digital companies, such as LinkedIn, Netflix, Google, Meta, and Airbnb, transitioning the data frameworks they developed internally to handle massive volumes of data and traffic to open source projects
* The impressive success of open source alternatives, which has fueled interest from individuals and businesses in developing and evaluating new tools and ideas

As an industry practice, data engineering has undergone several conceptual and technological evolution episodes. Without offering a detailed historical account, I would simply say that the birth of data engineering started with the introduction of Structured Query Language (SQL) and data warehousing in the 1970s/1980s. Companies like IBM and Oracle were early pioneers in the field, playing a key role in developing and popularizing many of the fundamental principles of data engineering.

Until the early 2000s, data engineering responsibilities were primarily handled by information technology (IT) teams. Roles such as database administrator, database developer, and system administrator were prevalent in the data job market.

With the global rise and adoption of the internet and social media, the so-called *big data* revolution marked a major step toward contemporary data engineering. Using the release date of Apache Hadoop as a reference, I would say that the big data era started around 2005. Pioneers like Google, Airbnb, Meta, Microsoft, Amazon, and Netflix have popularized a more specialized and advanced version of data engineering. This includes big data frameworks, open source tools, cloud computing, alternative data, and streaming technologies.

The financial sector has actively participated in this dynamic environment as both an observer and an adopter of data technologies. This active involvement stems from the financial industry’s continuous evolution in response to market demands and regulatory changes, which often necessitates the adoption of new technologies. Importantly, data engineering practices in finance are heavily domain driven, given the distinct requirements of the financial sector in terms of security, governance, and regulation, as well as the complex nature of the financial data landscape and financial data management challenges.

Considering these factors, this book will present financial data engineering as a domain-driven field within data engineering, specifically tailored to the financial sector, thereby setting it apart from traditional data engineering. To further justify the need for financial data engineering, the upcoming sections will provide a brief introduction to the finance domain, outline the data-related challenges encountered in financial markets, offer definitions of data engineering and financial data engineering, and provide an overview of the role and responsibilities of a financial data engineer.

## First of All, What Is Finance?

Despite the extensive use of the term *finance*, there could be a lot of confusion about what it really means. This is because finance is a multifaceted concept that can be approached from different angles (see [Figure 1-1](#ch01_figure_1_1724776823880011)). To prepare you with a basic domain knowledge, the next sections present a short conceptual illustration of finance from four main perspectives: economics, market, science, and technology.

### Figure 1-1. Main areas of finance

![Figure 1-1. Main areas of finance](images/fden_0101.png)

### Finance as an economic function

In economic theory, finance is an institution that mediates between agents who are in *deficit* (who need more money than they have) and those in *surplus* (who have more money than they spend). To secure funds, agents in deficit offer to borrow money from agents with a surplus in exchange for an interest payment.

This perspective highlights the vital role of finance in the economy: it offers individuals a means to invest their savings, allows families to purchase a house through a mortgage, provides businesses with capital to get started, empowers universities to invest their assets and expand their campus, and enables governments to finance public projects to fulfill societal needs.

For economists, finance is one of the primary drivers of *economic growth*. This is why good economies tend to have large, efficient, and inclusive financial markets. To ensure financial markets’ stability and fairness, several regulatory agencies and regulations were established.

A major subject that financial economists often investigate is *market equilibrium*, which describes a state where demand and supply intersect, resulting in a stable market price. In financial markets, this price is commonly represented by the interest rate, with supply and demand reflecting the quantity of money in circulation. When demand exceeds supply, interest rates typically rise, whereas if supply surpasses demand, interest rates tend to decrease. Entities such as central banks were established to implement monetary policies aimed at maintaining market interest rates as closely aligned with equilibrium as possible.

### Finance as a market

To enable individuals and companies to engage efficiently in financial activities, *financial markets* have emerged, hosting a vast array of financial institutions, products, and services. Nowadays, if we take a well-developed financial sector, we can find a large variety of market players. These may include the following:

* Commercial banks (e.g., HSBC, Bank of America)
* Investment banks (e.g., Morgan Stanley, Goldman Sachs)
* Asset managers (e.g., BlackRock, The Vanguard Group)
* Security exchanges (e.g., New York Stock Exchange [NYSE], London Stock Exchange, Chicago Mercantile Exchange)
* Hedge funds (e.g., Citadel, Renaissance Technologies)
* Mutual funds (e.g., Vanguard Mid-Cap Value Index Fund)
* Insurance companies (e.g., Allianz, AIG)
* Central banks (e.g., Federal Reserve, European Central Bank)
* Government-sponsored enterprises (e.g., Fannie Mae, Freddie Mac)
* Regulators (e.g., Securities and Exchange Commission)
* Industry trade groups (e.g., Securities Industry and Financial Markets Association)
* Credit rating agencies (e.g., S&P Global Ratings, Moody’s)
* Data vendors (e.g., Bloomberg, London Stock Exchange Group [LSEG])
* FinTech companies (e.g., Revolut, Wise, Betterment)
* Big tech companies (e.g., Amazon Cash, Amazon Pay, Apple Pay, Google Pay)

### Note

The terms “financial institution,” “financial firm,” “financial company,” and “financial organization” might often be used interchangeably. However, from an economic theory standpoint, “financial institution” may be the most appropriate term to use, as it represents an abstract concept encompassing any company, agency, firm, or organization that serves a specific purpose or function within financial markets. For this reason, I will be mostly using the term “financial institution” throughout this book.

The primary unit of exchange in financial markets is commonly referred to as a financial *asset*, *instrument, or security*. There is a large number of financial assets that can be bought and sold in financial markets. Here are a few:1

* Shares of companies (e.g., common stocks)
* Fixed income instruments (e.g., corporate bonds, treasury bills)
* Derivatives (e.g., options, futures, swaps, forwards)
* Fund shares (e.g., mutual funds, exchange-traded funds)

Given the large and diverse number of financial instruments and transactions, financial markets are further classified into categories, such as the following:

* Money markets (for liquid short-term exchanges)
* Capital markets (long-term exchanges)
* Primary markets (for new issues of instruments)
* Secondary markets (for already issued instruments)
* Foreign exchange markets (for trading currencies)
* Commodity markets (for trading raw materials such as gold and oil)
* Equity markets (for trading stocks)
* Fixed-income markets (for trading bonds)
* Derivatives markets (for trading derivatives)

# Investopedia: The Online Resource for Financial Education

If you want a quick introduction to a specific financial term, [Investopedia](https://oreil.ly/oO9gS) is the place to go. Investopedia is the world’s leading source of online financial and investment content. This includes information on financial terminology, definitions, news, investments, and financial education. Investopedia is a valuable resource for anyone interested in learning more about finance, whether they are a novice learner or an investor looking to gain more in-depth financial knowledge. Investopedia’s articles are written, reviewed, and fact-checked by financial experts, which adds to the credibility and quality of the published content.

Interestingly, financial markets are highly reliant on and driven by research and methodologies developed by finance departments at prominent universities and specialized finance institutes. The next section will briefly explore the nature and key areas of financial research.

### Finance as a research field

Finance is a well-known and extensive field of academic and empirical research. One major area of investigation is *asset pricing theory*, which aims to understand and calculate the price of claims to risky (uncertain) assets (e.g., stocks, bonds, derivatives, etc.). Within this theory, low prices often translate into a high rate of return, so we can think of financial asset pricing theory as a way to explain why certain financial assets pay (or should pay) higher average returns than others.

Another major field of financial research is *risk management*, which focuses on measuring and managing the uncertainty around the future value of a financial asset or a portfolio of assets. Other areas of investigation include portfolio management, corporate finance, financial accounting, credit scoring, financial engineering, stock prediction, and performance evaluation.

To publish financial research findings, a variety of peer-reviewed journals have been established. Some of these journals offer broad coverage, while others are more specialized. Here are some examples:

The Journal of Finance:   Covers theoretical and empirical research on all major areas of finance

The Review of Financial Studies:   Covers theoretical and empirical topics in financial economics

The Journal of Banking and Finance:   Covers theoretical and empirical topics in finance and banking, with a focus on financial institutions and money and capital markets

Quantitative Finance:   Covers theoretical and empirical interdisciplinary research on quantitative methods of finance

The Journal of Portfolio Management:   Covers topics related to finance and investing, such as risk management, portfolio optimization, and performance measurement.

The Journal of Financial Data Science:   Covers data-driven research in finance using machine learning, artificial intelligence, and big data analytics

The Journal of Securities Operations & Custody:   Covers topics and issues related to securities trading, clearing, settlement, financial standards, and more

In addition to academic journals, a large number of conferences, events, and summits are regularly held to share and discuss the latest developments in financial research. Examples include the Western Finance Association meetings, the American Finance Association meetings, and the Society for Financial Studies Cavalcades. Furthermore, globally renowned certifications like the Chartered Financial Analyst (CFA) are available to aspirant financial specialists who wish to acquire strong ethical and technical foundations in investment research and portfolio management.

### Finance as a technology

Finally, finance can refer to the set of technologies and tools enabling all kinds of financial transactions and activities. Examples include the following:

* Payment systems (mobile, contactless, real-time, digital wallets, gateways, etc.)
* Blockchain and distributed ledger technology (DLT)
* Financial market infrastructures (e.g., Euroclear, Clearstream, Fedwire, T2, CHAPS)
* Trading platforms
* Stock exchanges (e.g., NYSE, NASDAQ, Tokyo Stock Exchange)
* Stock market data systems
* Automated teller machine (ATM)
* Order management systems (OMSs)
* Risk management systems
* Algorithmic trading and high-frequency trading (HFT) systems
* Smart order routing (SOR) systems

This diverse array of technologies in the financial sector is crucial for maintaining the efficiency and reliability of global financial markets.

## Defining Data Engineering

Now that we have a foundational understanding of finance, let’s explore what financial data engineering is. To do this, I’ll first explain traditional data engineering, as it is a widely recognized term in the industry.

If we Google the words “what is data engineering,” we get more than two billion search results. That’s quite a lot, but to be more pragmatic, we can do a more advanced inquiry by searching Google Scholar for all papers and books where the term “data engineering” occurs in the title. Such a query returns a relatively large number of results (around 2,290 scientific publications), as shown in [Figure 1-2](#ch01_figure_2_1724776823880046).

### Figure 1-2. Google Scholar search for publications with data engineering in the title

I highly recommend you read some of the publications that Google Scholar returns for data engineering. Interestingly, you will quickly notice that there is quite a high variety of definitions for data engineering. This is expected, as the field of data engineering sits at the intersection between multiple fields, including software engineering, infrastructure engineering, data analysis, networking, software and data architecture, data governance, and other data management-related areas.2

For illustrative purposes, let’s consider the following selected definitions:

> Data engineering is the development, implementation, and maintenance of systems and processes that take in raw data and produce high-quality, consistent information that supports downstream use cases, such as analysis and machine learning. Data engineering is the intersection of security, data management, DataOps, data architecture, orchestration, and software engineering.
>
> [Joe Reis and Matt Housley, *Fundamentals of Data Engineering*](https://oreil.ly/wfug6) (O’Reilly, 2022)

> Data engineering is all about the movement, manipulation, and management of data.
>
> [Lewis Gavin, *What Is Data Engineering?*](https://oreil.ly/svCMj) (O’Reilly 2019)

> Data engineering is the process of designing and building systems that let people collect and analyze raw data from multiple sources and formats. These systems empower people to find practical applications of the data, which businesses can use to thrive.
>
> [Dremio](https://oreil.ly/GW18h)

As you can see, all three definitions are quite different, but if we make an effort to extract the main defining elements, we can infer that data engineering revolves around the *design* and *implementation* of an *infrastructure* that enables an organization to *retrieve* data from one or more sources, *transform* it, *store* it in a target destination, and make it *consumable* by end users. Naturally, in practice, the complexity of such a process would depend on the technical and business requirements and constraints, which vary on a case-by-case basis. Given this context, I will use the following definition of data engineering throughout this book:

> Data engineering is a field of practice and research that focuses on designing and implementing data infrastructure intended to reliably and securely perform tasks such as data ingestion, transformation, storage, and delivery. This infrastructure is tailored to meet varying business requirements, industry practices, and external factors such as regulatory compliance and privacy considerations.

Throughout this book, we’ll focus on the concept of *financial data infrastructure* as the cornerstone of financial data engineering. Along the way, we will examine the *components* of a financial data infrastructure, which include physical (hardware) and virtual (software) resources and systems for storing, processing, managing, and transmitting financial data. Furthermore, we will discuss the essential *capabilities* and *features* of a financial data infrastructure, such as security, traceability, scalability, observability, and reliability.

With this definition in mind, let’s now proceed to clarify the meaning of financial data engineering.

## Defining Financial Data Engineering

Financial data engineering shares most of the traditional data engineering tools, patterns, practices, and technologies. However, when designing and building a financial data infrastructure, relying only on traditional data engineering is not sufficient. You are very likely going to deal with domain-specific issues such as the complex financial data landscape (e.g., a large number of data sources, types, vendors, structures, etc.), the regulatory requirements for reporting and governance, the challenges related to entity and identification systems, the special requirements in terms of speed and volume, and a variety of constraints on delivery, ingestion, storage, and processing.3

Given such domain-driven particularities, financial data engineering deserves to be treated as a specialized field that sits at the intersection between traditional data engineering, financial domain knowledge, and financial data (as illustrated in [Figure 1-3](#ch01_figure_3_1724776823880067)). More formally, this book defines financial data engineering as follows:

> Financial data engineering is the domain-driven practice of designing, implementing, and maintaining data infrastructure to enable the collection, transformation, storage, consumption, monitoring, and management of financial data coming from mixed sources, with different frequencies, structures, delivery mechanisms, formats, identifiers, and entities, while following secure, compliant, and reliable standards.

### Figure 1-3. Financial data engineering and related fields

![Figure 1-3. Financial data engineering and related fields](images/fden_0103.png)

### Note

Don’t confuse financial data engineering with financial engineering. Financial engineering is an interdisciplinary applied field that uses mathematics, statistics, econometrics, financial theory, and computer science to develop financial investment strategies, financial products, and financial processes.4

# Domain-Driven Design

Designing software systems following domain-specific knowledge and requirements is a common practice. The most prominent approach in this context is *Domain-Driven Design* (DDD). DDD emphasizes modeling and designing the business domain to ensure that the software aligns with business requirements in terms of quality and features. This approach necessitates close collaboration between engineers and domain experts to establish a common understanding and a unified language, known as the “ubiquitous language,” which is consistently used throughout the project.

DDD divides a given business problem into domains. A domain is the problem space that the software application is being developed to solve. For example, in a banking application, domains could be accounts, payments, transactions, customers, cash management, and liquidity management. Domains can further be decomposed into subdomains; for example, cash management may have subdomains such as collections management and cash flow forecasting, which are bounded by a given context.

Now that you know what financial data engineering is, you may be wondering why it matters to financial institutions and markets and why we should write a book about it. The next section addresses these questions in detail.

# Why Financial Data Engineering?

One of the main goals of this book is to illustrate how financial data engineering is unique in terms of the domain-driven elements that characterize it. To understand why the market demands financial data engineering, it is crucial to examine the main factors shaping and driving data-driven needs and trends in the financial sector. The next few sections will provide a detailed account of these factors.

## Volume, Variety, and Velocity of Financial Data

One of the primary factors that have been transforming the financial sector is *big data*. In this book, big data is simply defined as a combination of three attributes: large size (*volume*), high dimensionality and complexity (*variety*), and speed of generation (*velocity*). Let’s explore each of these Vs in detail.

### Volume

When referencing big data, it is hard to deny that it is primarily about size. Data can be large, either in *absolute* or *relative* terms. Data is said to be large in absolute terms if it gets generated in a remarkably enormous and nonlinear quantity. An absolute increase in data size is often the result of socio-technological changes that induce a structural alteration to the data generation process. For example, in the past, card payments were primarily reserved for major purchases and were relatively limited, whereas today, the widespread adoption of card and mobile payment methods has transformed everyday transactions, with people now using cards and phones to pay for almost everything, from groceries to electronics. This, in turn, has led to a (remarkable) absolute increase in the amount of payment data being generated and collected.

In addition, the rapid development and adoption of digital automated technologies, in particular electronic exchange mechanisms, have resulted in an absolute increase in the sheer volume of financial data generated. The emergence of high-frequency trading is a good example. For instance, a single day’s worth of data from the New York Stock Exchange’s [high-frequency dataset](https://oreil.ly/4a0B1), Trade and Quotes (TAQ), comprises approximately 2.3 billion records. With the implementation of high-frequency trading technologies, financial data began to be recorded at incredibly fine intervals, including the millisecond (one-thousandth of a second), microsecond (one-millionth of a second), and even nanosecond (one-billionth of a second) levels.

On the other hand, data is considered relatively large if its size is big compared to other existing datasets. Improved data collection is perhaps the main driver behind the relative increase in financial data volumes. This has been facilitated by technological advancements enabling more efficient data collection, regulatory requirements imposing stricter data collection and reporting requirements, the increasing complexity of financial instruments necessitating the collection of data for risk management, and the growing demand for data-driven insights within the financial sector. As an example, the Options Price Reporting Authority (OPRA), which collects and consolidates all the trades and quotes from member option exchanges in the United States, reported an astonishing peak rate of 45.9 million messages per second in February 2024.5

With large volumes of financial data comes a new space of opportunities:

* Overcoming sample selection bias that might exist in small datasets
* Enabling investors and traders to access high-frequency market data
* Capturing patterns and financial activities not represented in small datasets
* Monitoring and detecting frauds, market anomalies, and irregularities
* Enabling the use of advanced machine learning and data mining techniques that can capture complex and nonlinear signals
* Alleviating the problem of high dimensionality in machine learning, where the number of features is significantly high compared to the number of observations
* Facilitating the development of financial data products that are derived from data, improve with data, and produce additional data

However, such opportunities come with technical challenges, mostly related to data engineering:

* Collecting and storing large volumes of financial data from various sources efficiently
* Designing querying systems that enable users to retrieve extensive datasets quickly
* Building a data infrastructure capable of handling any data size seamlessly
* Establishing rules and procedures to ensure data quality and integrity
* Aggregating large volumes of data from multiple sources
* Linking records across multiple high-frequency datasets

The frequency at which data is generated and collected greatly impacts financial data volumes. A process that produces one million records per second generates significantly larger data volumes compared to a process that produces one thousand records per second. This rate of data generation is known as data *velocity* and will be discussed in the following section.

### Velocity

Data velocity refers to the speed at which data is generated and ingested. Recent years have seen an increase in the velocity of data generation in financial markets. High-frequency trading, financial transactions, financial news feeds, and finance-related social media posts all produce data at high speeds.

With increased financial data velocity, new opportunities emerge:

* Quicker reaction times as data arrives shortly after generation
* Deeper and more immediate insights into intraday dynamics, such as price fluctuations and patterns emerging within an hour, minute, or second
* Enhanced market monitoring
* Development of new trading strategies, including algorithmic trading and high-frequency trading

Crucially, high data velocity introduces critical challenges for data infrastructures:

Volume:   How to build event-driven systems that can handle the arrival of large amounts of data in real time

Speed:   How to build a data infrastructure that can reliably cope with the speed of information transmission in financial markets

Reaction time:   How to build pipelines that can react as quickly as possible to new data arrival yet guarantee quality checks and reliability

Variety/multistream:   How to handle the arrival of many types of data from multiple sources in real time

The exponential increase in financial data volumes and the velocity of data generation doesn’t occur uniformly. Alongside this growth, new data types, formats, and structures have emerged to fulfill various business and technical requirements. The following section will explore this diversity of data in depth.