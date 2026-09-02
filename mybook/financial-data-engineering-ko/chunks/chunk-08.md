### Figure 3-8. Structural breakdown of the CFI code

![Figure 3-8. Structural breakdown of the CFI code](images/fden_0308.png)

## Financial Instrument Short Name

The *Financial Instrument Short Name* (FISN), defined in [ISO 18774](https://oreil.ly/OGcgl), is a human-readable code used to provide a consistent, uniform, and global description of financial instruments. Since July 1, 2017, the FISN has been globally assigned alongside the ISIN and CFI at the time of issuance of a new financial instrument.

Unlike ISINs, which are primarily used for clearing and settlement, FISNs are utilized by market participants to enhance the readability, efficiency, reliability, data consistency, and transparency of financial services transactions and reference data.

The FISN code has a maximum length of 35 alphanumeric characters. Of these, 15 are reserved for the issuer name, and 19 for the description of the instrument, with the character “/” as the separator between the issuer name and description. [Figure 3-9](#ch03_figure_9_1724776826858152) illustrates the structure of the FISN code.

### Figure 3-9. Structural breakdown of the FISN code

![Figure 3-9. Structural breakdown of the FISN code](images/fden_0309.png)

## Committee on Uniform Security Identification Procedures

The *Committee on Uniform Security Identification Procedures* (CUSIP) is a nine-character alphanumeric code used to identify financial securities in the United States and Canada. CUSIP codes are mainly used for trading, settlement, and clearing. They are issued and managed by [CUSIP Global Services (CGS)](https://oreil.ly/poJ_k), which acts as the US national numbering agency and is operated by FactSet Research Systems, Inc., as of the time this book was written.

The first six characters of a CUSIP uniquely identify an issuer (company, municipality, agency). The seventh and eighth characters identify the instrument type and issue using a hierarchical alphanumeric convention. The last character is a check digit.

For US securities, the CUSIP number makes up the middle nine characters of a US ISIN. For example, Amazon’s ISIN is US0231351067, and Amazon’s CUSIP is 023135106. [Figure 3-10](#ch03_figure_10_1724776826858170) offers a visual representation of the CUSIP code.

### Figure 3-10. Structural breakdown of the CUSIP code

To check the validity of a CUSIP code, the following steps are required:

1. Convert non-numeric characters to digits according to their ordinal position in the alphabet plus 9 (e.g., A = (1 + 9) = 10).
2. Convert the characters \* to 36, @ to 37, and # to 38.
3. Multiply every even digit by 2. If the result is a two-digit number, add the digits together (e.g., 13 → 1 + 3 = 4).
4. Get the sum of all values.
5. Get the floored value of the sum: (10 – (sum modulo 10)) modulo 10.

A Python implementation for ISIN check digit validation is available [in the GitHub repo for this book](https://oreil.ly/ACvCK).

Recently, a new identifier, called *CUSIP Entity Identifier* (CEI), was [introduced by CGS](https://oreil.ly/7oU7C) to identify legal parties involved in the syndicated lending market.8 The CEI was developed in collaboration with the Loan Syndications and Trading Association (LSTA) and syndicated loan solution providers.

## Legal Entity Identifier

The *Legal Entity Identifier* (LEI), defined in [ISO 17442](https://oreil.ly/UKFb9), is a 20-character alphanumeric code used to identify legal entities engaged in financial transactions. Each LEI contains information about an entity’s ownership structure and thus answers the questions of “who is who” and “who owns whom.” This concept aligns closely with know your customer (KYC) practices in financial markets, which aim to verify the identity of clients within financial institutions. The LEI identifier is a global, unique, and freely accessible identifier. Its official maintainer is the Global Legal Entity Identifier Foundation (GLEIF).

As illustrated in [Figure 3-11](#ch03_figure_11_1724776826858188), the first four characters of the LEI form a prefix that identifies the Local Operating Unit (LOU) that issued the LEI. Characters 5 to 18 constitute the entity identifier assigned by the LOU. Finally, characters 19 and 20 are two check digits.

### Figure 3-11. Structural breakdown of the LEI identifier

![Figure 3-11. Structural breakdown of the LEI identifier](images/fden_0311.png)

ISO 17442 [classifies](https://oreil.ly/VSXaQ) the following as legal entities:

* All financial intermediaries
* Banks and finance companies
* International branches
* All entities that issue equity, debt, or other securities for other capital structures
* All entities listed on an exchange
* All entities that trade financial instruments or are otherwise parties to financial transactions, including business entities, pension funds, and investment vehicles such as collective investment funds (at umbrella and subfund levels) and other special purpose vehicles that have a legal form
* All entities under the purview of a financial regulator and their affiliates, subsidiaries, and holding companies
* Sole traders (as an example of individuals acting in a business capacity)

On April 4th, 2019, ANNA and GLEIF launched a collaborative initiative to associate ISIN identifiers with the LEI identifiers of their issuers. This initiative aims to enhance market transparency by establishing a direct link between the issuer and the issuance of securities.

# Lehman Brothers and the Establishment of the Legal Entity Identifier

The introduction of the LEI has been celebrated as a major milestone in financial markets, generating numerous discussions and publications about its beneficial impact on improving market efficiency and stability. The question is, why all this attention?

The issue started shortly after the collapse of Lehman Brothers in 2008. As explained by a [McKinsey report](https://oreil.ly/vsiLd), “After Lehman’s demise, participants in the global financial system could not assess their exposure to Lehman, its subsidiaries, and each other because there was no standard system for identifying counter parties in the maze of subsidiaries and affiliates from which banks, insurers, asset managers, and other market participants transact.”

To give an illustrative example, when Lehman Brothers collapsed in 2008, it had an [estimated 8,000 subsidiaries working in various jurisdictions](https://oreil.ly/mirmV), while Morgan Stanley had roughly 3,500 subsidiaries. Consider the potential number of bilateral agreements and transactions between any of Lehman’s 8,000 subsidiaries and Morgan Stanley’s 3,500 and assume that such agreements are specified using different identification systems. Now, assume that you want to calculate the total exposure of Morgan Stanley to Lehman Brothers. This would require aggregating millions of positions, each identified using the subsidiary’s convention.

Unsurprisingly, it took quite a lot of time for Lehman Brothers’s counter parties to calculate their total exposure to the consolidated entity. To mitigate this issue and ensure that financial institutions can quickly aggregate their exposures and risk information, the ISO led an initiative to develop an international legal entity identification standard, resulting in the LEI.

In addition to the LEI, the ISO created the *Entity Legal Forms* (ELF), described in [ISO 20275](https://oreil.ly/3Aal3), to uniquely identify entity forms/types globally using a standardized four-character code. GLEIF maintains ELF codes that can be accessed and downloaded from its [web page](https://oreil.ly/dUb8y).

## Transaction Identifiers

Identifiers are the backbone of the lifecycle of financial transactions. During its processing, a single transaction often traverses various systems and parties. Consequently, the same transaction might be recorded with different IDs as it moves from one system to the next. This makes it difficult to unambiguously identify transactions and all related messages across disparate systems and databases. To overcome this issue, unique transaction identifiers have been developed.

One example is the *Unique Swap Identifier* (USI),9 specific to the United States and [mandated](https://oreil.ly/DSry9) by the Commodity Futures Trading Commission (CFTC) and the Securities and Exchange Commission (SEC) as part of the Dodd-Frank Act. The USI is a fixed-length identifier assigned to all swap transactions, identifying the transaction uniquely throughout its lifecycle. To expand the scope of the USI identifier for global reporting of financial transactions, the *Unique Trade Identifier* (UTI) was [introduced](https://oreil.ly/9N5Eb).

To ensure consistency across different jurisdictions and reporting platforms, the ISO introduced the [ISO 23897](https://oreil.ly/3E2U8)—the *Unique Transaction Identifier* (UTI) standard. It provides specifications aimed at standardizing transaction identifiers globally, ensuring unique identification throughout a financial transaction’s lifecycle. This is essential for facilitating transaction reporting, improving traceability, and reducing operational errors, especially as cross-border trading expands.10

The format of these transaction identifiers is generally similar. ISO 23897 specifies a max length of 52 characters for UTI code, but a variable length is possible. There is a consensus that a unique transaction identifier should include a prefix identifying the issuing entity, followed by a string that uniquely identifies the transaction. A market preference has emerged in favor of using international standards such as LEI identifiers for the prefix part.11 For example, in 2013, the ISDA working group [proposed a best practice recommendation for the UTI](https://oreil.ly/kMRUi), where the prefix consists of characters 7–16 of the LEI, followed by a 32-character string, as illustrated in [Figure 3-12](#ch03_figure_12_1724776826858208).

### Figure 3-12. ISDA-based Unique Trade Identifier structure

![Figure 3-12. ISDA-based Unique Trade Identifier structure](images/fden_0312.png)

## Stock Exchange Daily Official List

The *Stock Exchange Daily Official List* (SEDOL) is a seven-character alphanumeric code mainly used to identify securities traded on the London Stock Exchange (LSE) and other smaller exchanges in the UK. The LSE (the National Numbering Agency of the UK) assigns SEDOL codes upon request from the security issuer.12

Over the years, the SEDOL system has expanded, and SEDOL codes can now be issued at the country level to represent securities listed in multiple jurisdictions. SEDOLs are issued globally across all jurisdictions and multiple asset classes. If a security is traded on a different exchange in a different country, it will be assigned a separate SEDOL code. This makes SEDOLs unique across countries, which is ideal for international trading and security identification.

For UK securities, SEDOLs are embedded within the UK ISIN codes by adding the country code at the beginning, followed by two padding zeros, then the SEDOL, and finally, the ISIN check code. For example, the UK banking group HSBC has a SEDOL code of 0540528 and an ISIN code of GB0005405286.13

SEDOL codes issued prior to March 2004 were exclusively numeric. Afterward, the SEDOL system moved to an alphanumeric format that starts with an alphabetic character, followed by five alphanumeric characters and a trailing numeric check digit. [Figure 3-13](#ch03_figure_13_1724776826858225) illustrates the structure of SEDOL.

### Figure 3-13. The structural breakdown of the SEDOL identifier

![Figure 3-13. The structural breakdown of the SEDOL identifier](images/fden_0313.png)

To check if a SEDOL is valid, the check digit is chosen to make the weighted sum of all SEDOL characters a multiple of 10. The steps to validate a SEDOL are as follows:

1. Convert non-numeric characters to digits according to their ordinal position in the alphabet plus 9 (A = (1 + 9) = 10).
2. Multiply each of the first six numbers by their corresponding weight: 1 for first position, 3 for second, 1 for third, 7 for fourth, 3 for fifth, 9 for sixth.
3. Get the sum of all values.
4. Get the floored value of sum: (10 – (sum modulo 10)) modulo 10.

A Python implementation for SEDOL check digit validation is available [in the GitHub repo for this book](https://oreil.ly/iTLnc).

## Ticker Symbols

A ticker symbol is a short and unique series of letters assigned to financial securities (mostly stocks) for listing and trading purposes. There is no standard for tickers, and they can be generated and assigned by various organizations, including exchanges and trading venues, financial data providers, and financial institutions.

The allocation process and formatting conventions of tickers are specific to each issuing organization. Among US exchanges, tickers are typically one to four characters long, and they resemble the company name when possible. For example, the ticker for Apple, Inc. on the NYSE is AAPL, while Ford Motor has the ticker F. Some exchanges, such as NASDAQ, [add a fifth symbol to their tickers](https://oreil.ly/G9hMy) to convey information about the trading status and special features of the stock. For example, in BRK.A, the first three represent the stock symbol for Berkshire Hathaway, Inc. (BRK), and the last letter (.A) indicates that the shares are of class A type, which traditionally holds more voting rights.

In addition to exchanges, financial data providers assign proprietary ticker symbols to financial instruments. For example, Bloomberg created its own Bloomberg ticker to identify a financial entity uniquely within the Bloomberg ecosystem. A Bloomberg ticker can include the exchange-specific ticker, the market sector, the exchange code, instrument-specific information (e.g., bond maturity, option expiry, option type, etc.), and the Bloomberg database (e.g., EQUITY for stocks).

Another well-known proprietary ticker symbol is the *Refinitiv Instrument Code* (RIC), which is issued and maintained by LSEG. RIC tickers are mainly used to look up information on specific financial instruments on LSEG platforms. The main component of the RIC is the security’s ticker symbol with an optional character that identifies the exchange. For example, the RIC symbol IBM.N refers to IBM stock (IBM) traded on the New York Stock Exchange (.N).

Stock tickers can vary by exchange and country, which implies that they may not be unique across different exchanges and countries. As a result, to reliably identify a stock, both the ticker and the exchange or country of listing are often required.

Tickers are not immutable and might change to reflect corporate actions such as mergers and acquisitions. For example, prior to the 1999 merger with Mobil Oil, Exxon used the phonetic spelling of the company (XON) as its ticker symbol. After the merger, the symbol changed to XOM.

Importantly, tickers are not guaranteed to remain unique, as they can be reassigned over time. For example, until 2017, the ticker SNOW was assigned by NYSE to ​​Intrawest Resorts Holdings, Inc. In May 2017, Henry Crown and Company and KSL Capital Partners acquired Intrawest and transformed it into a privately owned company. After delisting Intrawest, the ticker SNOW was reassigned to Snowflake. A Wikipedia search of both company names would confirm this, as illustrated in [Figure 3-14](#ch03_figure_14_1724776826858244).

### Figure 3-14. NYSE tickers for Intrawest and Snowflake

![Figure 3-14. NYSE tickers for Intrawest and Snowflake](images/fden_0314.png)

## Derivative Identifiers

Derivatives are among the most exchanged financial securities in financial markets. As a quick reminder, a derivative is a contract that derives its value from an underlying financial asset or variable such as stocks, commodities, foreign exchange, interest rates, indexes, and many more.

Crucially, identifying derivative instruments is more challenging than identifying other types of financial instruments. First, several constituent elements must be considered to identify a derivative instrument. Second, due to their flexible and customizable nature, derivatives can easily turn into very complex products. Third, a substantial deal of derivatives is traded OTC, complicating their tracking and identification. Nonetheless, as I will demonstrate next, market participants have developed various initiatives to identify both exchange-traded and OTC derivative instruments.

### Option symbol

Option symbols are derived symbols used to identify an option and its characteristics on a given exchange.14 The current market standard for option symbols is based on the *Options Clearing Corporation*’s (OCC) *Options Symbology Initiative* (OSI). The OSI format consists of a 21-character alphanumeric code that can be split into four parts:

* A root (ticker) symbol of the underlying stock or ETF (exchange-traded fund).
* An expiration date, which is six digits in the format YYMMDD.
* An option type, either C for a call or P for put.
* The strike price. This is represented by the price times 1,000, with the front padded with 0s to 8 digits. The decimal point falls three places from the right in the options symbol: 00000.000.

The structure of the OSI option symbol is illustrated in detail in [Figure 3-15](#ch03_figure_15_1724776826858262).

### Figure 3-15. The structural breakdown of the OSI option symbol

![Figure 3-15. The structural breakdown of the OSI option symbol](images/fden_0315.png)

### CFI, UPI, and OTC ISIN

To identify OTC derivatives, a combined identification scheme has been put in place that relies on three identifiers:

OTC ISIN:   This is allocated by the *Derivatives Service Bureau* (DSB), with the initial two characters starting with the custom “EZ” code.

Unique Product Identifier (UPI):   This is defined in [ISO 4914](https://oreil.ly/V-dgy) for the identification of OTC derivative products.

Classification of financial instruments (CFI):   This is generated by the DSB as part of the OTC ISIN generation process.

The three identifiers are combined to provide different levels of detail. Malavika Solanki, of the management team at the DSB, [illustrated the combined use of the three identifiers with the following example](https://oreil.ly/_qMRN): at the highest level, the CFI can tell that a derivative instrument is a “single currency, fix-float, interest rate swap with a constant notional schedule and cash delivery.” The UPI would tell a bit more about the product, for example, that it has a “three-month reference rate term, a USD reference rate, and that the name of the reference rate was USD-LIBOR-BBAR.” Finally, the OTC ISIN can provide more granular details about the specific instrument that has been transacted, such as “the standardized ISO reference rate name, the price multiplier associated with the instrument, the full name and short names of the instrument, the expiry date.”

### Alternative Instrument Identifier

The *Alternative Instrument Identifier* (AII) has been adopted within the European Union for reporting purposes to identify derivatives traded on regulated markets without an ISIN assigned to them. Rather than being a code, the AII is a concatenation of descriptive fields that identify the instrument. The fields include the exchange code, exchange product code, derivative type, put/call identifier, expiry/delivery/prompt date, and strike price, as illustrated in [Figure 3-16](#ch03_figure_16_1724776826858281).

### Figure 3-16. The structural breakdown of the AII identifier

![Figure 3-16. The structural breakdown of the AII identifier](images/fden_0316.png)

## Financial Instrument Global Identifier

The *Financial Instrument Global Identifier* (FIGI) is a 12-character alphanumeric ID covering hundreds of millions of active and inactive instruments around the world.

The history of FIGI started in 2009 when Bloomberg decided to release its Open Symbology (BSYM) system for identifying financial securities across asset classes. The BSYM provides a library of identifiers for hundreds of millions of securities, known as Bloomberg Global Identifiers (BBGIDs). In 2014, the BSYM symbology system was adopted by the Object Management Group (OMG), a nonprofit standards consortium, in order to promote it as an open industry standard. Subsequently, the BBGID was renamed to FIGI. Since its introduction, FIGI has received a lot of market attention. For example, the Accredited Standards Committee X9 [adopted FIGI as an official US data identification standard](https://oreil.ly/f6-_a).

FIGI codes are unique across all markets and countries and remain unchanged once issued. For example, if IBM stock is traded on 12 stock exchanges, there will be 12 different FIGIs.

Furthermore, FIGI was designed as a global system capable of identifying any type of financial instrument, including stocks, bonds, derivatives, loans, indexes, funds, and digital assets. FIGIs are also free to access. An open source tool called [OpenFIGI](https://oreil.ly/VPX6F) was released to identify, map, and request a free FIGI via an API.

The FIGI identification system has a hierarchical structure composed of three levels:

Global FIGI:   This is the most granular level, identifying a financial asset at the trading-venue level. It is unique to a specific instrument at a particular trading venue.

Composite global FIGI:   This level aggregates multiple venue-level FIGI identifiers within the same country, providing a broader identification that encompasses all trading venues for a specific instrument within that country.

Share class global FIGI:   This level further aggregates FIGI identifiers to cover financial instruments across multiple countries. It provides a global view of a single instrument regardless of the country and venue.

For example, Amazon trades on multiple stock exchanges in the US. When Amazon common stock trades on the New York Stock Exchange, it has the FIGI code BBG000BVPXP1. When the same stock trades on the NASDAQ Global Select exchange, it has a FIGI of BBG000BVQ4Z3. But if you don’t care about which US exchange Amazon trades on, you can use the Amazon composite FIGI (BBG000BVPV84) to generically reference Amazon stock traded in the US. If you want to globally identify Amazon common stock regardless of trading venue and country, the share class code (BBG001S5PQL7) can be used.15 [Figure 3-17](#ch03_figure_17_1724776826858298) illustrates the hierarchical structure of FIGI.

### Figure 3-17. Hierarchical representations of FIGI

![Figure 3-17. Hierarchical representations of FIGI](images/fden_0317.png)

All three levels of FIGI identifiers have the same structure and limitations. The identifier may contain only letters in [B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z], and zero to nine digits.

The structure of FIGI codes is as follows:

* The first two characters identify the certified issuer that created the FIGI code. Currently, Bloomberg generates the majority of FIGI codes, hence the presence of the prefix BB in most identifiers.
* The third character is the letter G, used to indicate that it’s a global identifier.
* Characters 4–11 are alphanumeric characters that constitute the reference ID.
* A trailing check digit.

[Figure 3-18](#ch03_figure_18_1724776826858316) illustrates this structure visually.

### Figure 3-18. The structural breakdown of FIGI

![Figure 3-18. The structural breakdown of FIGI](images/fden_0318.png)

The check digit procedure is based on the Luhn algorithm, following five steps:

1. Get the identifier, e.g., BBG000BLNQ16, and remove the check digit, BBG000BLNQ1.
2. Convert non-numeric characters to digits according to their ordinal position in the alphabet plus 9 (A = (1 + 9) = 10). In our example, we get [11][11][16][0][0][0][11][21][23][26][1].
3. Double every second digit: [11][22][16][0][0][0][11][42][23][52][1].
4. Compute the sum of the resulting values: 1 + 1 + 2 + 2 + 1 + 6 + 0 + 0 + 0 + 1 + 1 + 4 + 2 + 2 + 3 + 5 + 2 + 1 = 34.
5. Get the floored value of the sum: (10 – (34 modulo 10)) modulo 10 = 6, which is the check digit attached to the identifier.

A Python implementation for FIGI check digit validation is available in this book’s [GitHub repo](https://oreil.ly/-BwrQ).

## FactSet Permanent Identifier

The [*FactSet permanent identifier*](https://oreil.ly/LNMqf) is a proprietary identification system developed by FactSet to offer a stable and unified identifier. It includes three levels:

Security:   Identifying the security globally

Regional:   Identifying the security at the regional level per currency (e.g., US/USD)

Listing:   Identifying the security at the market level (e.g., US/NYSE/USD)

FactSet provides the [FactSet Symbology API](https://oreil.ly/QHQAn), a symbol/identifier resolution service that allows users to map a wide variety of identifiers to FactSet’s native symbology or third-party identifiers such as CUSIPs, SEDOLS, ISINs, Bloomberg FIGI, and many more. In addition, FactSet offers the [FactSet Concordance API](https://oreil.ly/UbD3r), which enables users to programmatically match the FactSet identifier for a specific entity based on attributes, such as name, URL, and location.

## LSEG Permanent Identifier

The [*Permanent Identifier* (PermID)](https://permid.org) is a unique identifier used within the London Stock Exchange Group (LSEG) information model to identify and reference various objects, including organizations, instruments, funds, issuers, and people. It ensures that these objects are accurately and unambiguously referenced and linked together, even as their relationships change time.

What makes PermID especially valuable is that it’s linked to a unique web address or Uniform Resource Identifier (URI), offering a permanent, direct link to the identified entity. LSEG has made PermID open source, enabling access via web pages or through API-based entity search and matching services.

For example, the following PermID URLs can be used to retrieve information about the technology company Apple:

https://permid.org/1-4295905573:   Provides organizational details identifying Apple, Inc.

https://permid.org/1-8590932301:   Contains instrument details identifying Apple’s ordinary shares.

https://permid.org/1-25727408109:   Includes quote information identifying Apple’s ordinary shares on the New York Stock Exchange.

## Digital Asset Identifiers

Following the emergence and diffusion of blockchain and distributed ledger technologies, *digital assets* have been established as a new type of financial market entity. According to the [ISO 22739 vocabulary for blockchain](https://oreil.ly/--xjQ), a digital asset is an “asset that exists only in digital form or which is the digital representation of another asset.” In many cases, digital assets are referred to as *digital tokens*. A digital token can be *fungible* if it’s identical and interchangeable with similar assets (e.g., one dollar in New York is the same as one dollar in Australia), or *nonfungible* if they are unique and nondivisible (e.g., a painting or a boat). The most common for exchanging digital assets is a *blockchain*, which, according to ISO 22739 vocabulary, refers to a “distributed ledger with confirmed blocks organized in an append-only, sequential chain using cryptographic links.”16 The process of converting something to a digital asset and adding it to a blockchain system is called *tokenization*.

Over the past years, a wide variety of fungible digital assets have been developed, for example the following:

Crypto assets:   Assets developed using cryptographic techniques. The most notable examples are cryptocurrencies such as Bitcoin and Ethereum. Crypto assets can serve as a means of payment or investment.

Security token:   A financial security or instrument converted into a digital token and exchanged on a distributed ledger like blockchain (e.g., Microsoft Stock Token). Similar to traditional security certificates, security tokens represent an ownership right in a company or asset.

Nonfungible tokens:   These represent ownership rights over a unique digital asset such as images, videos, and games.

Utility token:   A token used to access a specific service or feature within a blockchain-based ecosystem.

As digital assets have grown in popularity, the requirement to identify the issued, stored, and transacted digital tokens and crypto assets has become more urgent. A first initiative was established with the introduction of the *Digital Token Identifier* (DTI), defined in [ISO 24165-1](https://oreil.ly/Y1yar), to identify fungible tokens and digital ledgers. In defining the DTI, the ISO realized the need for a new methodology for assigning the identifier. This is because digital assets are often not associated with a particular issuing entity, such as central banks, unlike traditional assets.

The standard helps in reducing confusion and increasing trust in the crypto assets market by providing a universal method of identification.

## Industry and Sector Identifiers

Industry and sector identifiers are classification frameworks used to categorize and group businesses into various categories and subcategories. Financial firms use industry identifiers to analyze market exposure, classify stocks, measure concentration risks, and understand cross-industry differences. Two main industry classification frameworks are widely used: the *Standard Industrial Classification* (SIC) and the *North American Industry Classification System* (NAICS).

The SIC identifier is a four-character numerical code used to classify industries based on their primary activities. The SIC system was created in 1937 by the US government to facilitate economic analysis across industries and agencies and to promote standardization and uniformity in the collection and recording of industrial data.

As illustrated in [Figure 3-19](#ch03_figure_19_1724776826858334), the official SIC classification code consists of three parts. The first two digits, which are mandatory, identify the major sector group. The third digit further categorizes the business into an industry group. The fourth digit provides the most granular classification, specifying the particular sector of the business. For example, [SIC code 6021 (National Commercial Banks)](https://oreil.ly/aqQWh) belongs to industry group 602 (Commercial Banks), which is part of major group 60 (Depositary Institutions), which belongs to the division of (Finance, Insurance, and Real Estate).

### Figure 3-19. The structural breakdown of the SIC code

![Figure 3-19. The structural breakdown of the SIC code](images/fden_0319.png)

The SIC system had several shortcomings. First, it produced ambiguous, mismatched, and overlapping classifications generated by SIC. Second, the four-digit system restricted the addition of new, emerging business sectors and industries. To overcome these issues, the SIC system was replaced in 1997 by the North American Industrial Classification System (NAICS), which introduced a more flexible six-character numeric code.

As shown in [Figure 3-20](#ch03_figure_20_1724776826858352), the first two digits of an NAICS code indicate the major sector of the business. The third digit indicates the subsector, and the fourth digit designates the industry group. The fifth digit indicates the specific industry of operation, while the sixth code specifies the national industry. For example, [NAICS code 522110](https://oreil.ly/0V87L) is used to identify commercial banks. The first two digits, 52, define the sector (Finance and Insurance), the first three digits (522) identify the subsector (Credit Inter mediation and Related Activities), the first four digits (5221) define the industry group (Depository Credit Inter mediation), and the last two digits identify the industry (Commercial Banking).

### Figure 3-20. The structural breakdown of the NAICS code

Other industrial classification frameworks are in use worldwide. These include the Statistical Classification of Economic Activities in the European Community, known as NACE and predominantly used in the European Union, the UK Standard Industrial Classification of Economic Activities (UK SIC), and the Australian and New Zealand Standard Industrial Classification (ANZSIC).