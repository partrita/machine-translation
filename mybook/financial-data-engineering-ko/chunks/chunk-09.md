## Bank Identifiers

Banks are the cornerstones of financial markets. They provide a secure and reliable place for individuals and organizations to deposit, transfer, and invest money, obtain loans, and make credit and debit card payments. Additionally, they support various online applications and offer a platform for FinTech firms to offer their services. Therefore, bank identifiers are essential for identifying banks, customers, and payment cards.

The most prominent example is the *Business Identifier Code* (BIC), also called SWIFT or Bank Identifier Code. This alphanumeric code, defined in [ISO 9362](https://oreil.ly/vnegN), is used to identify banks, financial institutions, and nonfinancial institutions worldwide when conducting international money transfers and routing exchanging messages. SWIFT issues BIC codes.

A SWIFT/BIC consists of either 8 or 11 alphanumeric characters that identify the country, city, bank, and optionally the branch:

Bank code:   Four-character alphabetic characters identifying the bank. It usually looks like a shortened version of that bank’s name.

Country code:   A two-character ISO 3166-1 alpha-2 code indicating the country where the bank is located.

Location code:   Two-character alphanumeric code that designates where the bank’s main office is.

Branch code:   An optional three-character alphanumeric code representing a specific branch. XXX is used to indicate the bank’s head office.

[Figure 3-21](#ch03_figure_21_1724776826858370) illustrates the structure of the BIC. The example shown refers to the Italian bank UniCredit Banca. The displayed code can be read as follows: UNCR identifies UniCredit Banca, IT is the country code for Italy, MM is the office location code for Milan, and XXX indicates the head office.

### Figure 3-21. The structural breakdown of the BIC code

![Figure 3-21. The structural breakdown of the BIC code](images/fden_0321.png)

The use of the BIC code to identify financial institutions is quite common, especially when identifying financial institutions in international transactions. Nevertheless, certain countries employ their own local bank or branch identification codes. For instance, Australia uses the *Bank State Branch* (BSB), a six-digit code, to identify branches of Australian financial institutions. Similarly, in the United States, financial institutions involved in various payment operations are identified using the *ABA Routing Number*, consisting of nine digits.

Another well-known bank identifier is the *International Bank Account Number* (IBAN). It is defined in [ISO 13616](https://oreil.ly/PXeiy) and serves as an international system of unique codes used to identify bank accounts when conducting money transfers. The IBAN system was originally developed for use within the EU, but it was later adopted by regions such as the Caribbean and Middle East.

The length of the IBAN varies by country, but it cannot exceed 34 characters. For instance, Belgian IBANs have 16 alphanumeric characters, Luxembourg’s are 20, and Germany’s are 22.

An IBAN code is composed of three main parts (see [Figure 3-22](#ch03_figure_22_1724776826858389) for an illustration):

* Country code following the ISO 3166-1 alpha-2 convention.
* Two check digits.
* *Basic Bank Account Number* (BBAN)—up to 30 alphanumeric characters that include the bank code, branch identifier, and account number. The length of BBAN may vary across countries.

### Figure 3-22. The structural breakdown of the IBAN number for Luxembourg

![Figure 3-22. The structural breakdown of the IBAN number for Luxembourg](images/fden_0322.png)

An IBAN code is validated through a mod-97 algorithm (as described by [ISO 7064](https://oreil.ly/OESpA)) that works as follows:

1. Make sure the IBAN has a valid length. For example, let’s take a random Luxembourgish IBAN: LU280019400644750000. The length is 20, which matches the country’s specified length.
2. Move the first four characters to the end of the string → 0019400644750000LU28.
3. Convert non-numeric characters to digits according to their ordinal position in the alphabet plus 9 (A = (1 + 9) = 10). In our example, we get 0019400644750000213028.
4. Treat the result as an integer and check if the modulo 97 of the number is equal to 1, 19400644750000213028 mod 97 = 1.

A Python implementation for IBAN validation is available in the [GitHub repo for this book](https://oreil.ly/7JbCy).

Last but not least, an important bank identifier is the payment card number or *Primary Account Number* (PAN), defined in [ISO/IEC 7812](https://oreil.ly/M-JO_). This is used to define payment cards and identify their issuer and cardholder. Most payment cards, such as credit, debt, and gift cards, have their PAN laser-printed on the front (yes, it’s your credit card number!).

The PAN is a numeric code with variable length ranging from 8 to 19 digits. The first six to eight digits represent the *Issuer Identification Number* (IIN), which identifies the card issuer. The first digit in the IIN is the *Major Industry Identifier* (MII), which identifies the industry/sector of the card issuer (for example, 4 and 5 are commonly used to identify financial institutions). The remaining characters are the individual account numbers used to identify the cardholder’s account. The last digit is a check digit, which can be validated using the Luhn algorithm.17 [Figure 3-23](#ch03_figure_23_1724776826858409) illustrates the structure of the PAN.

### Figure 3-23. The structural breakdown of a 16-digit PAN Identifier

![Figure 3-23. The structural breakdown of a 16-digit PAN Identifier](images/fden_0323.png)

# Summary

This chapter offered an in-depth treatment of financial identifiers and identification systems, which can be summarized as follows:

* Defining financial identifiers and identification systems and highlighting their critical role in financial market operations.
* Providing an overview of the entities involved in the creation, issuance, and maintenance of financial identifiers and identification systems.
* Outlining the desired properties of an optimal financial identification system.
* Discussing existing financial identification systems in detail, highlighting their main features and shortcomings.

The key takeaway from this chapter is that financial identification presents significant challenges for financial markets. In addition, as new products and market requirements emerge, the complexity of the issue continues to evolve. I highly recommend you stay informed about emerging trends in the development, standardization, and adoption of financial identification systems, as well as the evolving characteristics of existing systems.

Now that you have a solid understanding of financial identification systems, let’s move on to explore another related and crucial problem in financial markets: financial entity systems. You build a financial entity system when you want to extract, recognize, identify, and match financial entities within and across various sources of financial data.

The next chapter is all about financial entity systems—let’s keep moving!

1 If you are interested in this topic, I highly recommend Martijn Groot’s book, *Managing Financial Information in the Trade Lifecycle: A Concise Atlas of Financial Instruments and Processes* (Elsevier, 2008).

2 For an interesting read, see Richard Young’s article, [“The Identifier Challenge: Attributes of MiFID II That Cannot Be Ignored”](https://oreil.ly/mBYIs), *Journal of Securities Operations & Custody* 9, no. 4 (Autumn 2017): 313–320.

3 In 2011, the European Commission [concluded](https://oreil.ly/n1hi0) that Standard and Poor’s (S&P) was abusing its dominant position and violating antitrust rules as the unique issuing agency of US security ISINs by charging European financial institutions high access fees. The Commission made it legally binding for S&P to abolish licensing fees paid by banks for using US ISINs.

4 For more details, see Angeliki Skoura,, Julian Presber, and Jang Schiltz’s article, [“Luxembourg Fund Data Repository”](https://oreil.ly/AyR5B), *Data* 5, no. 3 (July 2020): 62.

5 CUSIP and SEDOL are discussed in the next few sections. For details on WKN, refer to the [definition offered by Börse Frankfurt](https://oreil.ly/uic6Y).

6 Example taken from the [ISIN organization web page](https://oreil.ly/z26Fb).

7 Keep in mind that many financial identification systems are always expanding, so just because an identifier doesn’t cover a certain market segment now doesn’t imply it won’t tomorrow.

8 The syndicated lending market is where a group of financial institutions (the syndicate) jointly extend a loan (often large loans) to a single borrower.

9 In finance, a swap is a type of derivative instrument in which two parties agree to exchange financial instruments, cash flows, or payments over a specified period of time.

10 To explore the utility of UTIs in financial markets, I recommend reading Swift’s article on [“The Unique Transaction Identifier and Its Value in Securities Settlement”](https://oreil.ly/00Rob).

11 Refer to BIS (editors): Committee on Payments and Market Infrastructures Board of the International Organization of Securities Commissions Technical Guidance, [“Harmonisation of the Unique Transaction Identifier”](https://oreil.ly/QlZK8), February 2017.

12 Sedol technical documentation is available on the [LSE website](https://oreil.ly/PHL4m).

13 Information taken from the [official company page of HSBC on the LSE website](https://oreil.ly/t2xTa).

14 An option is financial derivative instrument that gives its holder the right, but not the obligation, to buy or sell a specific quantity of an underlying asset at a given strike price on or before a specified future date, depending on the option style.

15 To explore for yourself, please use [this link](https://oreil.ly/p1La-).

16 More on blockchain internals will be discussed in Chapter 8.

17 Here is an exercise: take the Luhn algorithm that we defined previously in the International Securities Identification Number and use it to validate a credit or debt card number (BE CAREFUL: don’t use your own card number; a list of test credit card numbers is [available online](https://oreil.ly/8Smmy)).

# Chapter 4. Financial Entity Systems

In the last chapter, you learned about financial identifiers and identification systems and their critical role in financial markets. Importantly, before a financial entity can be identified, it must first be extracted and ready for identification. However, in finance, it’s quite common for data to exist in an unstructured format, where entities are not immediately identifiable. In fact, analysts [estimate](https://oreil.ly/5ZUgg) that the vast majority of data in the world exists in unstructured formats, such as text, video, audio, and images. Moreover, it is quite frequent that different identifiers are used to reference the same financial entity across both structured and unstructured data. These factors collectively pose significant challenges when trying to extract value and insights from the data.

To this end, many financial institutions develop systems to extract, recognize, identify, and match financial entities within financial datasets. These systems, which I will call *financial entity systems* (FESs), constitute the main topic of this chapter. As a financial data engineer, understanding FESs and the challenges they entail is essential in navigating today’s complex financial data landscape.

In the first part of this chapter, I will clarify the notion of financial entities and provide an overview of their various types. Next, I will illustrate the problem of financial entity extraction and recognition using a popular FES called *named entity recognition*. After that, I’ll cover the issue of financial data matching and record linkage using another FES known as *entity resolution*.

# Financial Entity Defined

Generally speaking, the term *entity* refers to any real-world object that can be recognized and identified. By narrowing the scope to financial markets, we can use the term *financial entity* to denote any real-world entity operating within financial markets. In this book, I define financial entity and financial entity systems as follows:

> A financial entity is a real-world object that may be recognized, identified, referenced, or mentioned as an essential part of financial market operations, activities, reports, events, or news. A financial entity may be human or not. It can be tangible (e.g., an ATM machine), intangible (e.g., common stock), fungible (e.g., one-dollar bills), or infungible (e.g., loans). A financial entity system is an organized set of technologies, procedures, and methods for extracting, identifying, linking, storing, and retrieving financial entities and related information from different sources of financial data and content.

As financial markets evolve and expand, so do the diversity and types of financial entities. A frequently used [benchmark classification system](https://oreil.ly/kinx6) categorizes entities into four main groups: individuals (PER), corporations (ORG), places (LOC), and miscellaneous entities (MISC).

Naturally, based on your institution’s needs, it might be necessary to categorize entities into a broader or more granular range. For example, let’s say that your financial institution decides to collect data on the digital asset market. In this case, you might want to create a new entity type (digital asset) to represent objects such as cryptocurrencies, digital currency, utility tokens, security tokens, stablecoins, bitcoin, and many more. Other examples include the following:

* *Persons*, e.g., bankers, traders, directors, account holders, investors, market makers, regulators, brokers, financial advisors
* *Locations*, e.g., New York, Japan, Africa, Benelux (Belgium, the Netherlands, and Luxembourg)
* *Nationalities,* e.g., Italian, Australian, Chinese
* *Companies*, e.g., Bloomberg L.P., JPMorgan Chase & Co., Aramco, Ferrero
* *Organizations*, e.g., Securities and Exchange Commission, European Central Bank, London Stock Exchange, International Monetary Fund
* *Sectors*, e.g., financial services, food industry, agriculture, construction, microchips
* *Currency*, e.g., dollar ($), pound (£), euro (€)
* *Commodity*, e.g., gold, copper, silver, wheat, coffee, oil, steel
* *Financial security*, e.g., stocks, bonds, derivatives
* *Corporate events*, e.g., mergers, acquisitions, leveraged buyouts, syndicated loans, alliances, partnerships
* *Financial variables*, e.g., interest rate, inflation, volatility, index value, rating, profits, revenues
* *Investment strategies*, e.g., passive investment, active investment, value investing, growth investing, indexing
* *Corporate and market hierarchies*, e.g., parent company, holding company, subsidiary, branch
* *Products*, e.g., iPhone, Alexa, Siri, Dropbox, Gmail

Now that you know what financial entities are and how to categorize them, let’s move on to understand how to identify and extract these entities from financial data. As previously mentioned, the systems designed for this purpose are referred to as *named entity recognition* (NER) systems.

# Financial Named Entity Recognition

As a financial data engineer, if you ever get assigned to a project that involves recognizing and identifying financial entities from unstructured or semi-structured text, you will likely design and build an NER system. In this section, I will first define NER and give a few illustrative examples. Then, I will describe how NER works and the steps involved in designing an NER system. Third, I will give an overview of the available methods and techniques for conducting NER. Lastly, I will discuss a few examples of open source and commercial software libraries and tools that you can use to do NER.

## Named Entity Recognition Described

NER, also known as entity extraction, entity identification, or entity chunking, is the task of detecting and recognizing named entities in text, such as persons, companies, locations, events, symbols, time, and more. NER is a key problem in finance, given the large volumes of finance-related text generated on a daily basis (e.g., filings, news, reports, logs, communications, messages) combined with the [growing demand](https://oreil.ly/413sX) for advanced strategies for working with unstructured and text data.

The outcome of NER analysis is used in a variety of financial applications, such as enriching financial datasets with entity data, information extraction (e.g., extracting relevant financial information from financial reports and filings), text summarization (e.g., ensuring adherence to legal requirements), fraud detection (identifying suspicious entities and transactions), adverse media screening (i.e., screening an entity against a negative source of information), sentiment analysis (assessing market sentiment from news and social media), risk management (e.g., recognizing potential financial risks and exposures), and extracting actionable insights from financial news, market events, players, competition, trends, and products.

# RavenPack Analytics: The Market Leader in Financial Named Entity Recognition

The market for products and services that depend on named entity recognition methods is rapidly expanding. Prominent names in this field include RavenPack, Info­N⁠gen, OptiRisk Systems, and LSEG’s Machine Readable News.

[RavenPack News Analytics (RNA)](https://oreil.ly/paVLa) is the world-leading news insights and analytics resource. RavenPack collects and analyzes unstructured content from more than 40,000 sources such as Dow Jones Newswires, the *Wall Street Journal*, *Barron’s*, MT Newswires, PR Newswire, Alliance News, MarketWatch, The Fly, and providers of regulatory news, press releases, and articles.

RavenPack News Analytics computes 20+ years of point-in-time data and provides event and sentiment data on more than 350,000 entities in over 130 countries, including the following:

* 110,000+ global, public, and private companies across all sectors
* 165,000+ macro entities such as places, currencies, persons, and organizations
* 7,000+ key business and geopolitical and macroeconomic events detected and enriched with sentiment and relevance scores

For each record in RavenPack News Analytics, information is available on:

* The entity (e.g., name, domicile, RavenPack’s unique entity identifiers, and other identifiers)
* Event Category
* Event Sentiment Score (how negative or positive an event is [range -1 → 1])
* Event Similarity Days (how novel is the event, measured as the number of days passed [range 0 → 365] since a similar event occurred)
* Event Relevance Score (how relevant is an event [range 0 → 100] based on where it occurs—e.g., a headline has a high ERS)

To identify and extract these relevant aspects from news data, RavenPack built a proprietary named entity recognition system. RavenPack maintains a database of predefined entities with more than 50 distinct entity types to provide timely and high-quality data. Moreover, RavenPack expands and extends its database as new and relevant types of entities or events appear in the market.

In building its NER system, RavenPack faced a special requirement for the financial sector: entity names may change time, and the same name may refer to different entities at different times. This might lead to problems such as survivorship bias, where only the latest assignee or an identifier or surviving entities are considered, skewing the data and the analysis. To solve this issue, RavenPack constructed a point-in-time-aware NER system.

The main idea behind NER is to take an annotated text such as…

> Google has invested more than $1 Billion in Renewable Energy projects in the United States over the past 5 years

… and produce a new block of text that highlights the position and type of entities, as illustrated in [Figure 4-1](#ch04_figure_1_1724776828398223). In this example, six types of entities are recognized: company, currency, amount, sector, time, and location.

### Figure 4-1. An illustration of the outcome of NER

![Figure 4-1. An illustration of the outcome of NER](images/fden_0401.png)

For the sake of illustration, let’s walk through a practical example. A well-known financial dataset is [LSEG Loan Pricing Corporation DealScan](https://oreil.ly/vyDek), which offers comprehensive coverage of the syndicated loans market. A syndicated loan (also known as a syndicated facility) is a special type of loan where a group of lenders (the syndicate) jointly provide a large loan to a company or an organization. Within the syndicate, different agents assume various roles (e.g., participating bank, lead arranger, documentation agent, security agent, etc.). LSEG and similar data providers collect information about syndicated loans from multiple sources, with SEC filings such as 8-Ks as the primary source.

Let’s consider a scenario where your team is tasked with creating a dataset on syndicated loans using a collection of SEC filings. Your first step involves extracting data from the text, identifying various elements that characterize a syndicated facility, and then organizing this information into a structured format. Let’s take the following example of an SEC filing for a syndicated facility agreement given to an Australian company (the text below is quoted and highlighted from the [SEC filing](https://oreil.ly/Bq5ER)):

> *Exhibit 10.1*
>
> *SYNDICATED FACILITY AGREEMENT*
>
> *dated as of*
> ***September 18, 2012***
>
> *among*
>
> ***THE MAC SERVICES GROUP PTY LIMITED***
> *,*
>
> *as Borrower,*
>
> *THE LENDERS NAMED HEREIN,*
>
> *J*
> ***.P. MORGAN AUSTRALIA LIMITED***
> *,*
>
> *as*
> ***Australian Agent***
> *and*
> ***Security Trustee***
> *,*
>
> ***JPMORGAN CHASE BANK, N.A.***
> *,*
>
> *as*
> ***US Agent***
> *,*
>
> *JPMORGAN CHASE BANK, N.A.,*
>
> *as*
> ***Issuing Bank***
>
> *and*
>
> *JPMORGAN CHASE BANK, N.A.,*
>
> *as*
> ***Swing Line Lender***
>
> ***J.P. MORGAN SECURITIES LLC***
> *,*
>
> *as*
> ***Lead Arranger***
> *and*
> ***Sole Bookrunner***
>
> *…*
>
> *The Borrower has requested the Lenders to extend credit, in the form of*
> ***Loans or Credits***
> *(as hereinafter defined), to the Borrower in an aggregate principal amount at any time outstanding not in excess of*
> ***AUD$300,000,000***
> *.*

As you can see, the text includes details regarding the borrower, lenders, and their respective roles, as well as information about the facility type, amount, and currency. Leveraging NER, we can extract this information and construct a structured dataset. For simplicity, let’s design a dataset with three tables: one to store facility data, another for borrower details, and a third for lender information. [Figure 4-2](#ch04_figure_2_1724776828398296) shows what the *Entity Relationship Model* of our dataset looks like. In the facility table, the facility\_id is an arbitrarily assigned unique identifier. In the borrower and lender tables, the facility\_id is present as a foreign key, meaning that records will exist in these tables only for facilities that exist in the facility table.

### Figure 4-2. Entity Relationship Model of the syndicated loan database

![Figure 4-2. Entity Relationship Model of the syndicated loan database](images/fden_0402.png)

The result of a successful NER-based entity extraction would look like the data present in Tables [4-1](#ch04_table_1_1724776828463752), [4-2](#ch04_table_2_1724776828463812), and [4-3](#ch04_table_3_1724776828463853).

Table 4-1. Facility table

facility\_id facility\_date facility\_amount facility\_currency facility\_type 89763 2012-09-18 300,000,000 AUD Loans or Credits

Table 4-2. Borrower table

| facility\_id | borrower\_name                     | borrower\_country |
| ------------ | ---------------------------------- | ----------------- |
| 89763        | The Mac Services Group PTY Limited | Australia         |

Table 4-3. Lender table

| facility\_id | lender                        | lender\_role                          |
| ------------ | ----------------------------- | ------------------------------------- |
| 89763        | J.P. Morgan Australia Limited | Australian Agent and Security Trustee |
| 89763        | JPMorgan Chase Bank, N.A.     | US Agent                              |
| 89763        | JPMorgan Chase Bank, N.A.     | Issuing Bank                          |
| 89763        | JPMorgan Chase Bank, N.A.     | Swing Line Lender                     |
| 89763        | J.P. Morgan Securities LLC    | Lead Arranger                         |
| 89763        | J.P. Morgan Securities LLC    | Bookrunner                            |

Crucially, although an NER system can identify the occurrence of a specific entity in the text, it typically does not link it to the corresponding real-world object. For example, if you refer back to [Figure 4-1](#ch04_figure_1_1724776828398223), Google was labeled as COMPANY, but at this point, we still don’t know which real-world company this is. To accomplish this task, an additional technique, called *named entity disambiguation* (NED) or entity linking, is often used.

Many books treat NED as a separate problem from NER and dedicate a separate section to it. However, for financial applications, linking the identified entities to their real-world matches is essential. For this reason, I consider NED an additional step in the NER process. [Figure 4-3](#ch04_figure_3_1724776828398346) demonstrates how NED works in conjunction with NER to link the recognized entity (COMPANY) to its specific real-world counterpart (Google).

### Figure 4-3. Named entity recognition and disambiguation

![Figure 4-3. Named entity recognition and disambiguation](images/fden_0403.png)

In NED, entities identified in the text are mapped to their unique real-world counterparts using a *knowledge base*. A knowledge base is a central repository that contains information about a vast array of subjects. These can be general-purpose or specialized and may be public or private. For example, Wikipedia is a well-known public, general-purpose knowledge base, while Investopedia serves a similar role but focuses specifically on finance. Other notable examples include GeoNames, Wikidata, DBpedia, and YAGO. Financial institutions and data vendors may also create proprietary knowledge bases tailored to their specific needs using their own data​.

## How Does Named Entity Recognition Work?

In this section, we will explore the various steps involved in building an NER system. As illustrated in [Figure 4-4](#ch04_figure_4_1724776828398392), the first step is data preprocessing, which ensures the data is structured, cleaned, harmonized, and ready for analysis. The second step, entity extraction, involves identifying the locations of all candidate entities. In the third step, these candidate entities are categorized into their respective entity types. Subsequently, the quality and completeness of the extracted data and the performance of the model are assessed in the evaluation step. Finally, the recognized entities can optionally be linked to their unique real-world counterparts through the disambiguation process.

Note that NER is an iterative process. Once the model is evaluated, the modeler can determine if improvements in data preprocessing, model selection, or training techniques are necessary to enhance the NER system’s performance.

### Figure 4-4. Named entity extraction and disambiguation process

![Figure 4-4. Named entity extraction and disambiguation process](images/fden_0404.png)

### Data preprocessing

Methodologically speaking, NER is a [subtask of the field of *natural language processing* (NLP)](https://oreil.ly/NbKiz). As with most NLP tasks, NER achieves good results if applied to clean and high-quality data. A variety of NLP-specific data preparation techniques can be used with NER. These include the following:

Tokenization:   Tokenization is the process of breaking down the text into smaller units called *tokens*. Word tokenization breaks down the text into single words; for example, “Google invests in Renewable Energy” becomes [“Google”, “invests”, “in”, “Renewable”, “Energy”]. Sentence tokenization breaks down text into smaller individual sentences; for example, “Google invests in Renewable Energy” gets converted into [“Google”, “invests in”, “Renewable Energy”].

Stop word removal:   Stop words are common and frequent words that have very little or no value for modeling or performance. For example, the English words “is,” “the,” and “and” are often classified as stop words. In most NLP tasks, including NER, stop words are filtered out.

Canonicalization:   In NLP, the form and conjugation of the word are often of no value. For example, the words “invest, investing, invests, invested” convey the same type of action; therefore, they can all be mapped to their base form, i.e., “invest.” The process of mapping words in a text to their root/base forms is known as *canonicalization*.:   Two types of canonicalization techniques are often used: *stemming* and *lemmatization*. Stemming is a heuristic technique that involves removing affixes from a word to produce its stem. This method is quick and efficient but can produce imprecise results, as it often leads to over-stemming (reducing words too much) or under-stemming (not reducing them enough). To address the limitations of stemming, lemmatization techniques are often used. Using vocabulary and morphological analysis, a lemmatizer tries to infer the dictionary form (lemma) of words based on their intended meaning. There are several common lemmitization techniques:

Lowercase conversion:   This consists of converting all words to lowercase.

Synonym replacement:   This technique involves replacing words with one of their synonyms.

Contractions removal:   Contractions are words written as a combination of a shortened word with another word. Contraction removal consists of transforming the words in a contraction into their full-length form, e.g., “she’d invest in stocks” becomes “she would invest in stocks.”

Standardization (normalization) of date and time formats:   For example, dates are converted to YYYYMMDD format, and timestamps to YYYMMDDHH24MMSS.

### Note

NER is highly sensitive to data preprocessing, where even minor changes can significantly impact the results. It’s essential to carefully assess the consequences of each preprocessing step. For example, converting all words to uppercase could disrupt rules dictating entity characteristics, such as the expectation that country names begin with uppercase letters.

### Entity extraction

During entity extraction, an algorithm is applied to a corpus of clean text to detect and locate candidate entities. In this step, the NER system designer should know which type of entities they are looking for in the text. The extraction process is a *segmentation* problem, where the goal is to find all meaningful segments of text that represent an entity. In this case, the name “Bank of England” needs to be identified as a single entity, even if the word “England” could also be a meaningful entity.

Since the goal of this step is to locate references to an entity, it might produce correct yet imperfect results. For example, unnecessary tokens might be included, as in “Banking giant JP Morgan Chase”. In other cases, some tokens might be omitted, such as missing “Inc.” in “JP Morgan Chase Inc.” or “Michael” in “Michael Bloomberg.”