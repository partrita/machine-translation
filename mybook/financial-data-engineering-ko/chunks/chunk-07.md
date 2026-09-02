# How Does the ISO Develop a Standard?

Familiarity with industry standards is essential for a financial data engineer to excel. However, how do organizations such as the ISO create a standard? As reported by the official [website](https://oreil.ly/blG7M), the ISO does not unilaterally decide when to create a standard; instead, it responds to a market need raised by stakeholders such as companies, consumer associations, academia, NGOs, and government and consumer groups. A typical scenario involves an industry group reporting the need for a standard to its national member, who subsequently approaches the ISO.

Once a market need for a standard emerges, the ISO appoints a committee composed of independent technical experts nominated by ISO members. A committee may have subcommittees and working groups. For example, ISO/TC 68 is the ISO committee tasked with overseeing financial services standards globally, and it has three main subcommittees:

ISO/TC 68/SC 2:   Covers information security in financial services

ISO/TC 68/SC 8:   Covers reference data for financial services

ISO/TC 68/SC 9:   Covers information exchange for financial services

The nominated committee starts the process by discussing the nature, scope, and key elements of the standard and submitting a draft proposal that meets the market need. The draft is then shared for further review and recommendations. Reaching a final agreement is consensus based and relies on a voting mechanism. If a consensus is not reached, then the draft will be modified and voted on again. Developing an ISO standard typically takes three years from initial proposal to final publication.

### National Numbering Agencies

A *National Numbering Agency* (NNA) is a national organization that issues and promotes ISO-based financial identifiers. Each country is free to assign the role of NNA to a local market player, which can be a stock exchange, central bank, regulator, clearing, financial data provider, or custodian. For example, the UK NNA is the London Stock Exchange, and Luxembourg’s is Clearstream Banking (a central securities depositary). Some countries don’t have an NNA; in such cases, a Substitute Numbering Agency (SNA) is appointed. Examples of SNAs include CUSIP Global Services in the US and WM Datenservice in Germany.

The Association of National Numbering Agencies (ANNA) was established to coordinate between the different national NNAs. ANNA collects and aggregates identifier data from all its members into a global centralized dataset called the ANNA Service Bureau (ASB) to ensure data quality and guarantee global interoperability.

### Financial data vendors

Most financial data vendors create their own identification systems to support the development of their products and services. For instance, when aggregating data from many sources, the data vendor might face the issue of identifier heterogeneity, which can be hard to resolve. It may also be the case that the data has no identifier, for example, when working with unstructured data such as news and text. Additionally, external identifiers might lack some of the properties the vendor needs (e.g., uniqueness). In such cases, creating a new vendor-based identification system is a common practice. Vendors such as S&P Global Market Intelligence, LSEG, Bloomberg, and FactSet all have their own in-house identifiers.

In certain instances, financial data vendors develop their identifiers because they create, rather than aggregate, their content. For example, news analytics providers such as RavenPack create and provide structured news and event data from unstructured content for a large number of entities. Since RavenPack independently extracts entities from text, it has developed its proprietary unique entity identifier system, known as the RavenPack Unique Entity Identifier.

Finally, given the increasing value of financial identifier data (e.g., for reference data management), financial data vendors may find it a profitable opportunity to create and license their financial identifiers.

### Financial institutions

Financial institutions create identifiers to facilitate internal processes, such as transactions, account management, client identification, and payment card number generation. Additionally, they might collect financial data from various sources, both internal and external, which may come with different identifiers. In these cases, a financial institution may opt to create its internal identification system to allow for a flexible design that matches business requirements and enables easy data retrieval and aggregation.

In conclusion, financial identifiers are critical to the efficiency, interoperability, and transparency of financial markets. All market participants deal with identifiers, either as users or as participants in their development. At this point, you may be wondering why it is so difficult to design a financial identification system that works in all circumstances and meets all market demands. To answer this question, we must first examine the desirable attributes of financial identification systems and understand the various constraints and challenges involved. This is what I’ll talk about next.

# Desired Properties of a Financial Identifier

Designing and maintaining a good financial identification system is one of the most persistent challenges in the financial industry. The difficulty stems from the need to balance various desirable properties, each of which may conflict with others. In this section, I build upon the framework proposed in the seminal work of Jules J. Berman, *Principles and Practice of Big Data* (Academic Press), to derive a minimal set of desired properties for a financial identification system. These properties include uniqueness, globality, scalability, completeness, accessibility, authenticity, granularity, permanence, immutability, and security. Let’s explore each property in detail.

## Uniqueness

Uniqueness refers to the quality of being one of a kind. For instance, fingerprints are unique to each human; no two humans on earth can have the same fingerprint. In the same way, a financial identification system must uniquely identify financial entities and never assign the same identifier to distinct entities. [Figure 3-2](#ch03_figure_2_1724776826858019) illustrates the concept of uniqueness. The identification system on the left is not unique since it assigns the identifier 56H128 to two separate entities: WTK Inc. and XYZ Inc. However, the system on the right is unique as it assigns a distinct identifier to all three financial entities.

### Figure 3-2. Unique versus nonunique identification systems

![Figure 3-2. Unique versus nonunique identification systems](images/fden_0302.png)

Crucially, the concept of a unique identifier can become ambiguous when applied to financial markets. To illustrate how, let’s consider the following scenarios:

* A company is listed on two stock exchanges, A and B. Should the listed stock have two identifiers, one for each market, or a single identifier for both?
* A financial instrument is trading in two countries; do we need separate identifiers for each country?
* A financial instrument can have multiple issues. Should we treat each issue as a unique instrument or use a single identifier for all?
* Following a company merger or acquisition, does the resulting entity represent a new, unique company or maintain the identity of the original?
* A financial transaction contains multiple instructions that relate to various instruments. Should each instruction have its own identifier or simply use the parent transaction identifier?

Quite challenging, no? Now, I imagine that you might have a solution for the above scenarios. But this is exactly where the issue lies; different market participants make different assumptions about what a unique financial identifier should be, and this has led to the development and adoption of numerous identifiers that differ in the way they define uniqueness. This can explain the common practice of using multiple identifiers within a dataset, for example, to identify the security with one identifier and the market where it is traded with another. If you are designing a financial identification system, my advice for you is to carefully think about the concept of uniqueness and discuss it with your business team to avoid serious shortcomings that might arise later.

## Globality

Financial markets are complex and dynamic systems that are in continuous evolution and expansion. To illustrate how, let’s consider the following facts:

* New companies are established and listed on the market.
* New financial instruments are created, listed, and traded in different markets and jurisdictions.
* Trading activities take place in various venues, such as centralized exchanges, trading platforms, and OTC markets.
* Consumer demand and preferences for financial products and services are constantly evolving, creating opportunities for the introduction of new offerings.
* Financial transactions span multiple countries, markets, and jurisdictions.
* New markets are established for exchanging new financial products.
* New financial entities are recognized and extracted from financial data.
* New exchange platforms and mechanisms gain popularity (e.g., cryptocurrencies).
* New types of data on financial activities are recorded and consumed.
* New financial regulatory requirements are published and enforced.
* New market standards are released, promoted, and adopted.
* New financial technologies emerge and diffuse among market participants.

These dynamics, among others, have contributed to a significant increase in the number and variety of financial entities that require identification. To meet this demand, a financial identification system must be able to accommodate the expanding ecosystem of financial activities and entities. I call such property *globality*. For example, a global identification system can do the following things:

* Expand from assigning identifiers at a national level to an international scale
* Expand its scope from assigning identifiers solely within centralized markets to OTC and other types of markets
* Expand its coverage to include various financial instruments such as indices, derivatives, digital assets, and loans

[Figure 3-3](#ch03_figure_3_1724776826858041) illustrates a straightforward example showcasing the concept of globality. The system on the top is global, as it expands its coverage to new areas that emerge from market expansion. The system on the bottom is nonglobal, as it covers only three areas and can’t expand further.

### Figure 3-3. Global versus nonglobal identification systems

![Figure 3-3. Global versus nonglobal identification systems](images/fden_0303.png)

Several identifiers, in particular vendor-specific identifiers, are limited to certain markets (e.g., stocks, bonds), exchanges (e.g., NYSE trades and quotes), or jurisdictions (e.g., US stocks, UK stocks). However, some identifiers have been developed to cover a broader range of market entities. The best example is perhaps Bloomberg’s Financial Instrument Global Identifier (FIGI), which we will discuss in more detail later in this chapter.

## Scalability

A scalable financial identification system does not exhaust its pool of assignable identifiers. Several reasons could lead to a shortage in the available supply of identifiers in a financial identification system:

Rapid market growth:   If the number of financial entities requiring identifiers increases rapidly, the identification system may struggle to keep up with the demand. One example is the issuance of a high volume of short-term financial instruments, such as commercial papers, repurchase agreements, and certificates of deposit. These instruments typically have short maturities and are frequently rolled over, creating a constant demand for new identifiers. If each instrument requires a unique identifier, it can quickly reduce the available pool of new identifiers.

Limited character length:   If the identifier format is limited in character length, exclusively employs numeric characters, or imposes format constraints, there may be a finite number of possible combinations, causing the identification system to exhaust its identifiers soon. For example, the Issuer Identification Number (IIN), presented later in this chapter, was expanded from a six-digit to an eight-digit format due to a [shortage in the supply of assignable identifiers](https://oreil.ly/FsiM_). Another example is the SEDOL identifier, discussed later in this chapter, which was changed from a numeric to an alphanumeric format following plans to expand its market coverage.

Poor allocation strategy:   If the identification system does not allocate the identifiers optimally, it might lead to early exhaustion. Examples of poor allocation strategies include the following:

Category-based allocation:   Allocating identifiers based on specific categories (e.g., different types or classes of stocks, bonds, derivatives) can lead to the exhaustion of available identifiers for a particular category if it grows more quickly than others. For instance, if bond instruments are allocated identifiers from 00000-29999 and stock instruments from 30000-49999, the bond category might run out of identifiers much earlier if there is a surge in bond issuance.

Reserved ranges:   Reserving large ranges of identifiers for future use or specific purposes, such as special market events, regulatory reporting, or new financial instruments, can significantly reduce the pool of identifiers available for general use.

Addressing these issues entails proactive planning, market growth projection, periodic evaluations, and adaptability of the identification system to the ever-changing financial market ecosystem.

## Completeness

Completeness requires that an identifier be assigned to each uniquely identifiable entity covered by the identification system. In other words, if an identification system is created to identify a set of financial entities, then each entity in the set must have an identifier. [Table 3-1](#ch03_table_1_1724776826875567) illustrates the concept by comparing complete and incomplete identifiers. Identification system A is incomplete because it lacks identifiers for entities 3, 4, and 6. In contrast, Identification system B is complete, as it assigns identifiers to all six entities.

Table 3-1. Comparing complete and incomplete identifiers

| Entity   | Identifier A (incomplete) | Identifier B (complete) |
| -------- | ------------------------- | ----------------------- |
| Entity 1 | 19982243                  | A5J234HS                |
| Entity 2 | 87987924                  | B5J874GS                |
| Entity 3 | NULL                      | T3H7Z589                |
| Entity 4 | NULL                      | GQ16B437                |
| Entity 5 | 23987912                  | N9M3F16S                |
| Entity 6 | NULL                      | K485GV1Z                |

A financial identification system may suffer from incompleteness for various reasons. For instance, a newly established company identification system might not backfill the history of its covered universe because some companies have failed, gone bankrupt, delisted, merged with other companies, or changed their names. Another common scenario arises when merging different datasets with different identifiers. For example, if you join data using a US-based identifier with data using a global identifier, many entities might lack the US identifier.

## Accessibility

Financial identifier data should be accessible, meaning it should not be restricted by license fees or usage limits, or monopolized by market players. Limited access to financial identifiers can result in market inefficiencies and a lack of transparency when conducting transactions and reporting.3 Logically, there are situations where financial identifiers, like credit card numbers or bank account IDs, must be secured.

In some cases, financial identifiers are freely available (e.g., on online trading platforms or stock exchange websites). However, collecting and aggregating this data in a structured format for a large number of entities can be overwhelming. Financial data vendors provide such products, often sold as reference data, but these are often subscription based.

Some market players launched initiatives to promote open-access financial identifiers. For example, LSEG openly [released its Permanent Identifier (PermID) system](https://oreil.ly/Zvx15), which provides comprehensive coverage across a wide variety of entity types, including companies, financial instruments, issuers, funds, and people. Another example is OpenFIGI, an open-access system that allows anyone to request Bloomberg’s Financial Instrument Global Identifier (FIGI), which I discuss later in this chapter.

## Timeliness

The timeliness of a financial identification system refers to its ability to process and generate identifiers quickly and efficiently. When a new financial entity enters the market or is created within a system (e.g., a new issue of a financial instrument), a timely financial identification system should do the following:

* Enable market participants to request an identifier quickly, ideally in real or near-real time
* Process requests quickly, allowing the issuing entity to allocate identifiers promptly
* Make accessible the newly allocated identifiers to other market participants without delay

Efficient and timely generation and dissemination of financial identifiers are essential for enhancing the efficiency of financial market operations and transactions.

## Authenticity

An authentic financial identification system can confirm whether a specific identifier was generated by it. To draw an analogy, this is the same as telling whether a watch displaying the label *Rolex* is indeed an authentic Rolex.

Financial identifiers are often designed following a specific symbology specification, which can be a formula or standardized format. This, in turn, enables the development of programs that can verify the identifier’s adherence to these specifications. A common practice involves the addition of a *check digit* to the identifier string. When a check digit is included, typically at the end of the identifier, an algorithm can be used to authenticate the identifier based on this digit. Later in this chapter, I will illustrate various examples of identifier check digits and their calculation logic.

## Granularity

In financial markets, it is quite common to observe hierarchical arrangements and structures within and between entities:

* Asset origination chain (e.g., issuing company → securities → stocks → common stocks → issues).
* Trading context (e.g., international → continental → national → market).
* Pyramid organizational structures (e.g., CEO → president → vice-president → middle management → team leaders → employees).
* Company ownership structures (e.g., parent company A owns B (child), B owns D, and D owns F, G, K).
* Asset classifications, where assets are organized in groups, categories, and subcategories (e.g., derivatives → options → stock options → call stock option).
* Sector classifications, which structure economic sectors using an industry taxonomy (e.g., sectors → industry groups → industries → sub-industries).
* Packaged transactions such as syndicated loans (package →facilities).
* Complex financial instruments such as multi-leg options or interest rate swaps, where the same instrument has multiple child instruments.
* In the fund industry, an umbrella fund structure allows for the creation of multiple subfunds, each with distinct investment strategies, further divided into various share classes tailored to different investor needs.4

A financial identification system is *granular* if it can scale to provide different levels of details that reflect market hierarchies. [Figure 3-4](#ch03_figure_4_1724776826858060) illustrates this concept. In this example, the entity requiring identification should be recognizable at international, national, and market levels. The identification system on the left is nongranular because it uses the same identifier for the entity across all levels. In contrast, the system on the right is granular because it assigns a unique identifier to the entity at each level.

### Figure 3-4. Granular versus nongranular financial identification systems

![Figure 3-4. Granular versus nongranular financial identification systems](images/fden_0304.png)

## Permanence

A reliable financial identification system must ensure that identifiers and their associated data are permanent and durable. This is essential for guaranteeing market trust and confidence and allowing the tracking and referencing of financial instruments and transactions over time. For example, a bank client should be able to go to the bank at any time and ask for a statement about their past transactions. If the customer closes their accounts with the bank, their identification data should not disappear from the system.

In some cases, a financial identifier can be interrupted; for example, a commercial data vendor might stop maintaining an identifier as they develop a new identification system or switch to using an industry-wide system. Additionally, an identification system might be replaced with a new one if it fails to meet certain desired properties, such as uniqueness, globality, and granularity. The concept of permanent versus nonpermanent identifiers is shown in [Figure 3-5](#ch03_figure_5_1724776826858078). The identification system on the left is permanent as it could return the associated data at time t and time t+n. In contrast, the system on the right is nonpermanent as it returns data at time t but returns none at time t+n.

### Figure 3-5. Permanent versus nonpermanent identification systems

![Figure 3-5. Permanent versus nonpermanent identification systems](images/fden_0305.png)

## Immutability

A robust financial identification system must ensure the immutability of its identifiers over time. This means that an identifier associated with a specific entity should neither change nor be reassigned to another entity. If the identified entity ceases to exist, its identifier should never be reused. Such a property is essential for maintaining transparency, traceability, and effective monitoring.

Besides temporal immutability, identifiers must persist through all stages of financial activities. For example, a transaction’s lifecycle, which typically comprises multiple steps from initiation, through execution, to settlement, should consistently use the same identifier. [Table 3-2](#ch03_table_2_1724776826875621) illustrates the concept of mutable versus immutable identifiers. Identifier A is immutable, as all three entities have the same identifier in 2005 and 2022. Identifier B is not mutable, as entities 1 and 3 changed their identifier in 2022. Moreover, the identifier of entity 1 used in 2005 was reassigned to entity 3 in 2022.

Table 3-2. Mutable versus immutable identifiers

| Entity   | Year | Identifier A (immutable) | Identifier B (mutable) |
| -------- | ---- | ------------------------ | ---------------------- |
| Entity 1 | 2005 | XZY743                   | XZY743                 |
| Entity 2 | 2005 | ABC376                   | ABC376                 |
| Entity 3 | 2005 | MNT098                   | MNT098                 |
| Entity 1 | 2022 | XZY743                   | KKH654                 |
| Entity 2 | 2022 | ABC376                   | ABC376                 |
| Entity 3 | 2022 | MNT098                   | XZY743                 |

### Note

Corporate events such as mergers, acquisitions, spin-offs, corporate restructurings, and rebranding might change a company’s structure, potentially resulting in the creation of a new entity. In these cases, a new identifier may be assigned.

## Security

Security must be prioritized when designing a financial identification system, as these systems are vulnerable to malicious attacks. Consider the damage that an attacker could inflict, for instance, if they succeeded in hacking an identification system and irreversibly changing its identifiers. Even worse is the scenario in which sensitive identifying data is compromised and utilized to commit financial crimes against the entities identified in the data.

To summarize, developing an optimal financial identification system is challenging since it involves multiple complex properties that may be difficult to achieve in a single system. For this reason, financial markets have developed a plethora of financial identification systems, each serving a particular purpose and offering unique characteristics. Some of these systems are widely adopted, while others are gaining attention in response to evolving market needs. The next section will provide you with an overview of current financial identification systems.

# Financial Identification Systems Landscape

The current landscape of financial identification systems is extensive, comprising open source and proprietary systems designed with different properties and for various purposes. Several standardization efforts have been initiated, yet a universally accepted standard has not been established. To give you an idea of the current scale, a Wikipedia [search for “security identifier”](https://oreil.ly/a5vsU) yields results for 16 different identifiers. The ISO conducted an [inventory of the current national and international financial identification standards](https://oreil.ly/qE18s) and identified a total of 19 different systems. These identifiers and several others are illustrated in [Figure 3-6](#ch03_figure_6_1724776826858098).

### Figure 3-6. Financial identification systems in use globally

![Figure 3-6. Financial identification systems in use globally](images/fden_0306.png)

In the following sections, I will discuss some of the most important financial identification systems used by markets, along with their key characteristics and challenges.

## International Securities Identification Number

The *International Securities Identification Number* (ISIN) is a 12-character alphanumeric code, defined in [ISO 6166](https://oreil.ly/Lov0_), that uniquely identifies a wide range of financial securities such as stocks, bonds, derivatives, fund share classes, and indexes.

In principle, an ISIN should represent a set of fungible financial instruments. For instance, the common stocks of a given company are fungible with each other, regardless of the issuance date, as they all share the same specifications. In this scenario, the same ISIN is typically used to represent the company’s common stock. However, if the company issues different classes of stocks, such as preferred stocks, each class would receive a different ISIN. Similarly, multiple bond issues from the same company would have distinct ISINs, since each issue has unique specifications such as the start date, end date, and interest rate. The same principle applies to more complex financial products, such as derivatives.

ISIN codes are issued and maintained by each country’s National Numbering Agency or the Substitute Numbering Agency. The ISIN system has gained widespread market adoption and is increasingly recognized as the global standard for financial instrument identification. Due to their reliability, ISIN identifiers are predominantly used for trading, settlement, clearing, and regulatory reporting.

The 12 characters of an ISIN can be divided into three parts: the first two characters are the [ISO 3166-1 alpha-2 code](https://oreil.ly/K-_mq) of the issuing country. The middle nine alphanumeric characters represent the security identifier. This nine-digit alphanumeric code is often called the National Securities Identifying Number (NSIN). Examples of NSINs include CUSIP in the USA, SEDOL in the UK, and WKN (“Wertpapierkennnummer”) in Germany.5 The last character is a check digit computed using the modulus 10 double-add-double or Luhn algorithm. [Figure 3-7](#ch03_figure_7_1724776826858117) offers a visual breakdown of the ISIN.

### Figure 3-7. Structural breakdown of the ISIN code

![Figure 3-7. Structural breakdown of the ISIN code](images/fden_0307.png)

One potential drawback of the ISIN is its international scope, which means it does not specify the trading location or currency. If a given stock trades on multiple different exchanges, the associated ISIN will be the same. For instance, IBM’s common stock is listed on almost 25 trading platforms and exchanges around the world. In this case, some identifiers for IBM stock would vary depending on where it is traded (e.g., the ticker). However, IBM stock will have only one ISIN for each security.6 To overcome this limitation, the *Market Identifier Code* (MIC), defined in [ISO 10383](https://oreil.ly/oLO28), is commonly used alongside the ISIN to specify exchanges, trading venues, and both regulated and nonregulated markets.

Another limitation is that the ISIN does not provide detailed information about the contract terms or variations within a particular type of security. In other words, an ISIN cannot describe a contract uniquely.

An ISIN might become inactive or be replaced with a new one following corporate actions such as mergers and acquisitions, company name changes, stock splits, and the redemption/conversion of debt instruments.

Another limitation of the ISIN is that it does not cover all instruments, especially over-the-counter instruments. In this case, alternative instrument identifiers are often used.7

# Luhn Algorithm: The Industry Standard for Financial Identifier Validation

The Luhn algorithm or Luhn formula, also known as the modulus 10 or mod 10 algorithm, named after its creator, IBM scientist Hans Peter Luhn, and specified in [ISO/IEC 7812-1](https://oreil.ly/M-JO_), is a widely used checksum formula for financial identifier validation. The algorithm is not meant to be a security measure against malicious attacks but rather a mechanism to protect against errors and distinguish valid identifiers from incorrect ones.

To validate an identifier such as ISIN using the Luhn formula, six steps are required:

1. If the identifier already contains the check digit, remove it. In most cases, the check digit is located at the end of the string. The remaining string constitutes the *payload*.
2. Starting from the rightmost digit in the payload, double the value of every second digit.
3. If doubling the digit results in a number that is greater than 9 (e.g., 18), then sum the digits of the doubled number to get a single digit (e.g., 12 becomes 1 + 2 = 3).
4. Sum all the digits.
5. Compute the sum’s modulus 10 as (10 − ( sum mod 10 )) mod 10. The result of this operation can be interpreted as the smallest number that needs to be added to the sum (possibly 0) to make it a multiple of 10.
6. If the modulus 10 obtained in step 5 is equal to the check digit, then the number is valid. Otherwise, it’s not.

For an example, let’s validate the ISIN of Microsoft, US5949181045:

1. To get a numerical string, we convert the country letters to digits by taking the ASCII code (American Standard Code for Information Interchange) of the capital letter and subtracting 55. The ASCII code for U is 85, while for S, it’s 83; therefore, the new digit is [85-55][83-55]5949181045 = 30285949181045.
2. Remove the check digit (=5) to get the payload → 3028594918104.
3. Starting from the right, we double the value of each second digit, and we get [6] 0 [4] 8 [10] 9 [8] 9 [2] 8 [2] 0 [8].
4. Take the sum of the multidigit numbers (>9). We have one, which is [10], and by summing 1 + 0, we get 1; therefore, the new sequence is [6] 0 [4] 8 [1] 9 [8] 9 [2] 8 [2] 0 [8].
5. Add up all the digits: 6 + 0 + 4 + 8 + 1 + 9 + 8 + 9 + 2 + 8 + 2 + 0 + 8 = 65.
6. Calculate the check digit using the formula: 10 – (65 mod 10) mod 10 = 5.
7. As the final result (5) is equal to the check digit, we can tell that the identifier is a valid ISIN.

A Python implementation for this ISIN check digit validation is available [in the GitHub repo for this book](https://oreil.ly/8Ym6G).

## Classification of Financial Instruments

The *Classification of Financial Instruments* (CFI) is a six-letter code defined in [ISO 10962](https://oreil.ly/oldKF) that describes and classifies financial instruments. It was developed to address a major problem in financial markets, namely the need for a uniform and consistent approach to categorizing and grouping financial instruments. The ISO has appointed SIX Group, the national numbering agency of Switzerland, as the maintenance agency for the CFI code. SIX publishes a list of all CFI codes and modifications on [its website](https://oreil.ly/ZMrOf).

Since July 1, 2017, CFI codes are globally assigned alongside the ISIN when a new financial instrument is issued. In most cases, an instrument’s CFI remains unmodified during its lifespan. However, corporate-related events such as changes to voting rights or ownership restrictions could cause a CFI to change.

In a CFI code, the first letter indicates the instrument category, the second denotes the subcategory, and the remaining letters indicate various attributes of the instrument. Both the second and remaining letters are optional. For example, the CFI code ESVXXX is for equity (E), common/ordinary share (S) with voting right (V), while code FXXXXX indicates a future (F), and OCXXXX is an option (O) of type call (C). [Figure 3-8](#ch03_figure_8_1724776826858134) offers a visual illustration of the CFI code.