### Bulk data arrival process

In a bulk DAP, data is ingested in large chunks. Rather than processing one record at a time, a bulk DAP handles blocks of data or files that may contain hundreds or even millions of records simultaneously.

Bulk DAP offers performance advantages by processing large data volumes in a single request, saving overhead costs. This is ideal for tasks like bulk data loading, migration between storage systems, data archival processes, and regulatory reporting. For instance, when switching database systems, dumping data in a format compatible with the new system is far more efficient than copying records individually.

To give an example, let’s consider how Snowflake’s bulk loading works.5 Assume you have a bunch of CSV files stored in the Amazon cloud storage service AWS S3, and you are using Snowflake as a data warehouse. You wish to upload the data from your CSV files into your Snowflake table.

The first thing to do is to create a FILE FORMAT object in Snowflake that describes the type and format of the data to be loaded. Let’s say that our CSVs use the semicolon, “;”, as a field delimiter, and we want to inform Snowflake to skip the first line in each file as it represents the header. The following command creates the desired format object:

```
-- Snowflake SQL
CREATE OR REPLACE FILE FORMAT s3csvformat
   TYPE = 'CSV'
   FIELD_DELIMITER = ';'
   SKIP_HEADER = 1;
```

Next, we want to create the so-called stage object, which tells Snowflake the location where the files are stored (staged). Snowflake provides several [types of stage objects](https://oreil.ly/IQ79x), but in this example, we will use the recommended Named stage,6 which may be created as follows:

```
-- Snowflake SQL
CREATE OR REPLACE STAGE s3_csv_stage
  FILE_FORMAT = s3csvformat
  URL = 's3://snowflake-docs';
```

Finally, to load the data from the stage location into the Snowflake table, we can execute the following command:

```
-- Snowflake SQL
COPY INTO destination_table
  FROM @s3_csv_stage/myfiles/
  PATTERN='.*daily_prices.csv'
  ON_ERROR = 'skip_file';
```

The PATTERN clause specifies that the command should load data from any file that matches the specified regular expression .*daily_prices.csv, which matches any file that ends with daily_prices.csv. Furthermore, the command specifies that if an error occurs when loading a specific file, skip it and proceed with the remaining files.

Now that we’ve covered the various data transmission and arrival processes, let’s explore the different types of data formats that can be ingested into a financial data infrastructure.

# Data Ingestion Formats

Data can be ingested in a variety of formats. A data format is used to indicate the extension or encoding used to store the data on a machine. In general, there is no standardized classification of the many data formats that a financial data infrastructure may support. To establish a baseline, this section will illustrate the most common types of data formats that financial data engineers might encounter when working with financial data.

## General-Purpose Formats

General-purpose formats are widely used data formats with broad applicability and extensive adoption within the financial markets. Examples include the following:

* Comma-separated values (CSV) files are text files with comma-separated values (,).
* Tab-separated values (TSV) files are text files with tab-separated values (\t).
* Text files (TXT) are text files with lines delimited by a line separator (\n).
* JavaScript Object Notation (JSON) files are structured as a collection of name/value pairs.
* Extensible Markup Language (XML) files structure and store data in a hierarchical format using custom tags.
* Microsoft Excel files work with [Microsoft Excel (e.g., XLSX and XLS)](https://oreil.ly/lcybD).
* Compressed files are compressed using a compression algorithm such as GZip or Zip.

Financial markets use these formats for a variety of reasons and purposes. For example, Microsoft Excel files are [quite popular](https://oreil.ly/03GEu) among financial professionals and accountants due to their reliability (Microsoft as maintainer), simplicity, and advanced analytical capabilities. CSV and TSV formats are widely used for storing and sharing financial time series and tabular data. TXT files are used to store textual financial content such as reports, news, entity and reference data, and many more. JSON and XML are widely used for programmatic and web-based financial data exchange due to their user-friendly nature and dependable technical specifications. Consequently, they frequently form the basis for financial data standards.7

The downside of using general-purpose formats is that their flexibility increases the chance of data errors or quality issues. Moreover, these formats may not be efficient when dealing with large data volumes. To address this concern, more specialized formats can be employed, which will be discussed in the following sections.

## Big Data Formats

General-purpose formats such as CSV and XML can easily encounter performance issues when ingesting and exchanging large amounts of data. To solve this issue, several big data formats have been developed, including Apache Parquet, Apache Avro, and ORC.

Apache Parquet is an open source, column-oriented data file format that supports efficient and economical data storage and retrieval. Parquet offers efficient data compression, decompression, schema evolution, and encoding algorithms to handle complex and large data. Parquet is accessible in several languages, including Python, C++, and Java. Parquet files are widely used. For example, the leading cloud data warehouse provider, Snowflake, [reports that Parquet is the file format most often used by its customers](https://oreil.ly/k8YFb) to upload data to the Snowflake platform.

# Column-Oriented Versus Row-Oriented File Formats

When dealing with file formats, it’s important to understand the difference between column-oriented and row-oriented formats. In row-oriented formats (e.g., PostgreSQL’s internal data format), data is stored on disk row by row. These formats are preferable for small datasets, strict data consistency requirements, or applications with heavy write/update operations, such as financial systems handling transactions like payments and clearing.

In contrast, column-oriented formats like Parquet store data on disk column by column. This format is highly advantageous for read-intensive and big data applications. Queries are more efficient and economical because read-intensive applications often retrieve only a subset of columns, avoiding unnecessary querying of other columns. Additionally, column-wise storage enhances compression efficiency as it optimally compresses data of the same type within a single column, unlike row-oriented formats, which compress heterogeneous data within a single row.

Apache Avro is another common big data format known for its row-oriented structure and compact binary encoding, which helps reduce file storage size. Avro stores data definitions, types, and protocols in an easily readable JSON format, while the actual data is stored in a highly optimized binary format. Avro is schema dependent, meaning that the data and its schema are stored and transmitted together in the same file. As a result, Avro is preferred over Parquet when frequent schema changes occur, as merging schemas from multiple files can be quite costly.8

A third common big data format is Optimized Row Columnar (ORC), a column-oriented, binary format primarily used for storing Hive data in Hadoop environments. ORC is [renowned for its exceptional performance](https://oreil.ly/61P0Y) in terms of data processing speed and storage efficiency, making it well-suited for handling large volumes of data.

## In-Memory Formats

In many applications, data is frequently read and processed in memory. Crucially, different software programs may store data in memory using different formats. If data moves from one application to another during a data processing pipeline, then each application needs to convert the data to its in-memory format before processing it. This is a costly operation as it often involves data serialization and deserialization, which in turn can impact performance.

To solve this issue, a variety of in-memory data formats have been developed. A prominent example is [Apache Arrow](https://oreil.ly/4Vf72), a standardized, column-oriented, language-agnostic data format for structuring and representing tabular datasets in memory. Apache Arrow can be used to develop a data infrastructure that processes data across multiple systems using an out-of-the-box standardized format.

Another noteworthy example is the [Resilient Distributed Dataset (RDD) abstraction](https://oreil.ly/THRcv) created for Apache Spark to enable reliable, fault-tolerant, and parallel computations in memory.

## Standardized Financial Formats

Market participants can exchange financial information in any of the formats covered thus far, such as CSV, JSON, TXT, and XML. However, if each financial institution employs its own convention to structure its financial messages and communications, markets will incur significant costs in understanding and extracting information from each and every format. For instance, imagine a network of one thousand trading firms where each firm submits trade request messages using its own JSON or XML structure. This scenario would result in hundreds of different message formats that every trader would need to understand.

To address this challenge, financial market participants have been working on creating standardized formats for financial information. This effort is often described by industry experts as establishing a “common financial language” for data exchange.9 Several initiatives have been proposed, leading to the development and adoption of multiple standards. Examples include the following:

* Financial products Markup Language (FpML)
* Financial Information eXchange (FIX)
* Interactive Financial eXchange (IFX)
* Market Data Definition Language (MDDL)
* Financial Electronic Data Interchange (FEDI)
* Open Financial Exchange (OFX)
* eXtensible Business Reporting Language (XBRL)
* Financial transaction card-originated messages (ISO 8583)
* Securities—Scheme for messages (ISO 15022)
* Universal Financial Industry Message Scheme (ISO 20022)
* SWIFT proprietary messages

In the following sections, we will go over some of these financial data standards in depth.

### Financial Information eXchange

[Financial Information eXchange (FIX)](https://oreil.ly/LDBs7) is an electronic communication protocol widely used to exchange financial transaction information between financial institutions such as banks, trading firms, brokers/dealers, security exchanges, and even regulators. FIX is a nonproprietary open standard owned and maintained by the FIX Trading Community member firms. FIX was originally developed to exchange pre-trade and trade equities trading messages. Over time, its scope has expanded to include support for post-trade activities, as well as transactions in fixed income, foreign exchange, and listed derivatives markets.

A full account of the [technical specifications of the FIX infrastructure](https://oreil.ly/gY00B) is beyond the scope of this section. However, the FIX system can be broken down into (1) a standardized message format, (2) a FIX order routing network, and (3) a FIX engine necessary to submit and receive FIX messages. The classical encoding of FIX messages is called *tagvalue encoding*, which structures a message as a chain of tag/value pairs. Tags are integers that identify the field, followed by the “=” character (hexadecimal 0x3D), and finally, the value of that field, encoded in the ISO 8859-1 character set. Each tag/value pair is separated by the ISO 6429:1992 Start of Heading control character <SOH> (hexadecimal value 0x01). Other encodings include FIXML, which leverages XML and JSON to format the message.

For example, a single buy order FIX message looks like this:10

```
8=FIX.4.2^A 9=145^A 35=D^A 34=4^A 49=ABC_DEFG01^A 52=20090323-15:40:29^A 56=CCG^A 115=XYZ^A 11=NF 0542/03232009^A 54=1^A 38=100^A 55=CVS^A 40=1^A 59=0^A 47=A^A 60=20090323-15:40:29^A 21=1^A 207=N^A 10=139^A
```

The fields can be broken down as follows:

```
8=FIX.4.2 FIX version number
9=145 Body Length: 145 bytes
35=D Message Type: New Order - Single
34=4 Message Sequence Number: 4
49=ABC_DEFG01 Sender Company ID: ABC_DEFG01
52=20090323-15:40:29 Sending Time: March 23, 2009, 15:40:29
56=CCG Target Company ID: CCG
115=XYZ On Behalf Of Company ID: XYZ
11=NF 0542/03232009 Client Order ID: NF 0542/03232009
54=1 Side: Buy
38=100 Order Quantity: 100 shares
55=CVS Symbol: CVS
40=1 Order Type: Market
59=0 Time In Force: Day
47=A Special Instructions: Agency single order
60=20090323-15:40:29 Transaction Time: March 23, 2009, 15:40:29
21=1 Handling Instructions: Automated execution
207=N Security Exchange: NASD OTC
10=139 Checksum: 139
```

According to the FIX protocol, to exchange FIX messages between two financial institutions, both must have a FIX engine that communicates over a FIX routing network. Several FIX network routing options are available, including the internet, leased lines, point-to-point VPNs, and Hub-and-Spoke. The FIX engine needs to be implemented and connected to the selected routing network to exchange messages.11

### eXtensible Business Reporting Language

[eXtensible Business Reporting Language (XBRL)](https://oreil.ly/y9Tp6) is an XML-based open international standard for digital business and financial reporting. XBRL is managed and maintained by XBRL International, a nonprofit consortium. In a nutshell, XBRL provides a standardized, accurate, and reliable way to represent and exchange business and accounting data in both human-readable and machine-readable formats. XBRL is widely used by regulators, companies, governments, data providers, investors, analysts, and accountants.

The main building block of XBRL is an XBRL *instance*, which refers to the collection of business facts that an XBRL document contains. More technically, an XBRL is an XML file whose root element is <xbrli:xbrl>.

Another important element is XBRL *facts*, which represent individual pieces of information in an XBRL instance. For example, a fact may say that Heckler & Brothers Inc.’s 2018 revenues were $5 billion. The fact is reported as a value of 5b against a corresponding concept representing “Revenues,” in addition to associated contextual information for the units (dollars), the period (2018), and the entity (“Heckler & Brothers Inc.”). Technically, facts are represented by elements in an XBRL document.

Additionally, there are XBRL *concepts*, which can be used to describe the meaning of facts. For instance, “Assets,” “Liabilities,” and “Net Income” are examples of these concepts. Technically, concepts are represented as element definitions in an XML schema.

Finally, XBRL *taxonomies* correspond to collections of concept definitions. Taxonomies are typically created to represent a given reporting regime, such as international financial reporting standards (IFRS) and generally accepted accounting principles (GAAP) standards, as well as for reporting requirements of various regulators and government agencies. A taxonomy is used to define what needs to be reported clearly. At a technical level, a taxonomy is an XML schema document containing element definitions and a collection of XML documents with additional information associated with concept definitions.

XBRL allows for defining business rules that can constrain and verify what kind of data can be reported. Rules can be logical or mathematical, and they are often used to control the data quality of XBRL documents.12

### Financial products Markup Language

[Financial products Markup Language (FpML)](https://oreil.ly/9ozTa) is an open source, XML-based information exchange standard designed for the electronic trading and processing of financial derivatives instruments. The standard is defined and maintained by the FpML Standards Committee.

Among the most distinguishing aspects of derivative markets is the flexibility in defining and shaping derivative contracts to meet specific client requirements. Moreover, a large portion of derivative trading happens over the counter (OTC), meaning that such transactions are conducted business-to-business and not through a centralized trading venue.

With such flexibility comes a large variety of data communication and representation styles. On the one hand, this has been considered necessary as it allows two parties to customize a derivative product to meet specific client needs. Consequently, attempts to standardize OTC derivative communications have not gained much traction, as they were doomed to become obsolete quite fast once new requirements emerged. This situation has led to a manual data exchange process between trading parties, which is prone to errors.

However, with the increase in derivative trading volume and the establishment of new requirements for derivative trade processing, standardization became more appealing. In this regard, FpML was introduced to automate the flow of information across the entire derivative trading network (of partners and clients), independent of the underlying software or hardware infrastructure supporting the related activities. The standard was initially developed for interest rate derivatives such as swaps, but it has been extended to other classes of derivatives, structured products, bonds, and commercial loans since then. Moreover, FpML has evolved to cover the different stages of a derivative transaction, such as pre-trade, trade, and post-trade.

An FpML message is encoded using Unicode Transformation Format (UTF)-8 or UTF-16 and uses XML as the file format. FpML may include a number of elements whose values are restricted to a limited set of values (e.g., currencies). Such restricted sets are called *domains*. FpML relies on two types of domain codings. First are domains that don’t change frequently throughout the life of the specification, which are coded using XML schema enumerations. The second type is domains coded using a strategy defined by the Architecture Working Group, referred to as *schemes*. A scheme is associated with a Uniform Resource Identifier (URI). Three categories of coding schemes exist:

* External coding scheme with a URI assigned by an external body such as an open standards organization or a market participant
* External coding scheme without a URI; in such a case, FpML assigns a URI
* An FpML-defined coding scheme, defined and versioned by FpML, which also assigns the URI

For example, an FpML-defined scheme is *actionTypeScheme,* which codes the action types as defined by the European Securities and Markets Authority (ESMA).13 As of the time this book was written, the URI for this scheme is *http://www.fpml.org/coding-scheme/action-type-1-0,* and its coding scheme is shown in [Table 7-1](#ch07_table_1_1724776832733168).

Table 7-1. FpML-defined action type scheme

| Code | Description                                                                     |
| ---- | ------------------------------------------------------------------------------- |
| C    | Cancel (a termination of an existing contract)                                  |
| E    | Error (a cancellation of a wrongly submitted report)                            |
| M    | Modify (a modification of details of a previously reported derivative contract) |
| N    | New (a derivative contract reported for the first time)                         |
| O    | Other (any other amendment to the report)                                       |
| V    | Valuation update (an update of a contract valuation)                            |
| Z    | Compression (a compression of the reported contract)                            |
| C    | Cancel (a termination of an existing contract)                                  |

FpML’s flexibility, enabled by its use of schemes, makes it well-suited for handling custom exchange definitions and requirements in the derivatives markets. Those interested in exploring the specifics of these schemes can refer to the [comprehensive FpML Coding Schemes documentation](https://oreil.ly/RjvBJ).

### Open Financial Exchange

[Open Financial Exchange (OFX)](https://oreil.ly/S8-Uu) is a widely adopted open standard for the electronic exchange of financial data and instructions between financial institutions, businesses, and customers. OFX allows direct connection between customers and institutions without requiring an intermediary.

Open Financial Exchange relies on open specifications that anyone can implement (e.g., financial institution, software development firm, transaction processor, or other party). A client-server model is used to design the OFX system. The client submits a request (e.g., HTTP) to an OFX server, and the server replies with a response to the client. OFX defines the request/response message structure and provides guidelines for building the infrastructure for supporting message exchange. OFX uses widely accepted open standards for networking (such as TCP/IP and HTTP), data formatting (such as XML), and TLS.

OFX is widely utilized by financial institutions for a variety of applications and use cases. Since 1997, it has been the [leading direct API standard](https://oreil.ly/yrM2p) for banks to provide data to financial applications. It is currently in use at over 7,000 financial institutions. OFX can be implemented and adapted across a wide range of frontend applications and platforms. Moreover, it is an extensible standard, allowing for the straightforward addition of new services as needed.

Readers are encouraged to check the [official documentation](https://oreil.ly/-UqIZ) for more details on OFX’s technical implementation and message structure.

### Universal Financial Industry Message Scheme

As messaging standards increased in scale, sophistication, and variety, financial market participants, in collaboration with the ISO, initiated discussions to make uniform the message standardization process. This resulted in the introduction of the highly celebrated [ISO 20022—Universal Financial Industry Message Scheme](https://oreil.ly/Z2k6L).

ISO 20022 is an open and global standard that aims to streamline financial market communication and messaging using a common language. Its general-purpose design makes it suitable for the majority of use cases, irrespective of the business domain, communication network, or counterparty.

A distinguishing feature of ISO 20022 is its model-based approach. When you use ISO 20022 to develop a new message, the outcome is a model that defines and describes all parts of the message exchange and communication protocol between participants. The modeling method consists of four levels: scope, conceptual, logical, and physical. These levels are developed as one progresses from the business process and its associated features and components to the development of the final instance of the message model in a given syntax (typically XML).

Having said this, it is important to remember that ISO 20022 is not a single communication standard in and of itself but rather a standard that describes a development methodology for creating financial message models.

ISO 20022 models and their related message components are available online via a central [repository](https://oreil.ly/e-bhU) organized into two areas:

The Data Dictionary:   Contains industry model elements such as business concepts, message concepts, and data types. These elements are called dictionary items and serve as reusable components for future models.

The Business Process Catalog:   Contains model message definitions and syntax implementations.

According to the [official ISO documentation](https://oreil.ly/vIenF), the modeling methodology of ISO 20022 consists of eight parts:

ISO 20022-1:   Metamodel for all models and the repository

ISO 20022-2:   UML profile to create models that conform to the ISO 20022-1 Metamodel

ISO 20022-3:   Modeling method to produce models

ISO 20022-4:   XML schema generation rules to transform a logical-level model into a physical-level implementation

ISO 20022-5:   Reverse engineering guidelines to extract relevant information from existing messages

ISO 20022-6:   Message transport characteristics

ISO 20022-7:   Registration process description

ISO 20022-8:   Abstract Syntax Notation One (ASN.1) generation rules to transform a logical model into an ASN.1-based physical level

ISO 20022 messages follow a four-block convention for naming. For instance, a well-known message is the “FinancialInstitutionToFinancialInstitutionCustomerCreditTransfer” message, represented in the ISO 20022 convention, as shown in [Figure 7-2](#ch07_figure_2_1724776832717118). In this example, “PACS” denotes “Payment Clearing and Settlement,” indicating the message’s business domain of payment and settlement instructions. The “008” segment serves as the message type identifier, specifying the type of transaction—in this case, a financial institution to financial institution customer credit transfer. The “001” designation represents the variant number, indicating the global message definition. Lastly, “12” identifies the message version within the ISO system.

### Figure 7-2. Structure of an ISO 20022 message

# ISO 20022 Variants

[Variants](https://oreil.ly/9Z9Fe) and versions are pivotal aspects of ISO 20022, allowing for the creation of simplified and purpose-specific versions of the global message to suit specific requirements.

One of ISO 20022’s nicest features is the concept of a variant. Each ISO 20022 message has a *global message definition*, typically represented with variant number 001. Other variants (>001) can be created to produce restricted versions of a global message definition. For example, a straight-through processing (STP) variant of a global message definition may exclude all the options that would require manual processing of the message instance, and thus ensures the STP of the messages.

Each variant can have multiple versions, which is the last component you see in the message identifier shown in [Figure 7-2](#ch07_figure_2_1724776832717118). Versions are independent of the variant; for example, variant 001 can have versions 001.001 and 001.002, while variant 002 may have versions 002.001, 002.002, and 002.003.

ISO 20022 variants play a crucial role by enabling customization of global message definitions to align with specific operational and processing needs in financial transactions. In addition, they simplify the adoption of ISO 20022 message definitions by reducing complexity and providing clarity on how to apply message definitions in specific contexts.

Examples of some of the most used ISO 20022 messages include the following:

pain.001—Credit Transfer:   Customer-initiated credit transfers to banks

pain.013—Request to Pay:   Requests payment from a payer

pain.002—Payment Status Report:   Status updates on initiated payments

pacs.008—FI to FI Customer Credit Transfer:   Customer credit transfers between banks

pacs.003—FI to FI Customer Direct Debit:   Direct debit transactions between banks

pacs.002—FI to FI Payment Status Report:   Status updates on financial institution payments

camt.05x:   Various account reporting messages (e.g., *camt.054—Bank to Customer Debit/Credit* can be used to notify an account holder of debit and/or credit entries reported to their account)

Here is a simple XML snippet that illustrates a PACS.008.001 message. Each tag within the message has been annotated with a comment detailing its meaning or purpose:14

```
<FIToFICstmrCdtTrf>  Financial Institution Credit Transfer
    <GrpHdr>  Group Header
      <MsgId>123456789</MsgId>  Message Identification
      <CreDtTm>2022-05-20T14:30:00</CreDtTm>  Creation Date and Time
      <NbOfTxs>1</NbOfTxs>  Number of Transactions
      <CtrlSum>1000.00</CtrlSum>  Control Sum (Total Amount)
    </GrpHdr>
    <CdtTrfTxInf>  Credit Transfer Transaction Information
      <PmtId>  Payment Identification
        <EndToEndId>00001</EndToEndId>  End-to-End Identification
      </PmtId>
      <Amt>  Amount
        <InstdAmt Ccy="USD">1000.00</InstdAmt>  Instructed Amount
      </Amt>
      <Cdtr>  Creditor
        <Nm>John Smith</Nm>  Name of the Creditor
      </Cdtr>
      <CdtrAcct>  Creditor Account
        <Id>  Identification
          <IBAN>GB29NWBK60161331926819</IBAN>  IBAN Number
        </Id>
      </CdtrAcct>
      <RmtInf>  Remittance Information
        <Ustrd>Invoice payment for services rendered.</Ustrd>
      </RmtInf>
    </CdtTrfTxInf>
  </FIToFICstmrCdtTrf>
```

Any community user or organization can use the ISO 20022 modeling methodology to develop and submit a proposal for a new model or a modification of an existing model. Candidate models are reviewed and approved by three registration bodies: the Registration Management Group (RMG), the Registration Authority (RA), and the Standards Evaluation Groups (SEGs).15

ISO 20022 has seen remarkable adoption and acceptance among market participants. This includes all domains where financial data is exchanged, including payments, securities trading and settlement, credit and debit card transactions, foreign exchange transactions, and many more.16 For example, SWIFT introduced ISO 20022 in March 2023 and [established a migration plan](https://oreil.ly/6EtRB) in which both SWIFT proprietary MT (message type/text) messages and ISO 20022 will coexist until November 2025. After that, SWIFT messages will be completely based on ISO 20022.

# Case Study: Society for Worldwide Interbank Financial Telecommunication

A good example demonstrating the use of messages in financial markets is the Society for Worldwide Interbank Financial Telecommunication (SWIFT). SWIFT is a Belgium-based cooperative that provides a secure and reliable messaging system for financial transactions worldwide. SWIFT does not hold or manage financial assets. Instead, it offers a platform for exchanging financial messages, such as money and securities transfer instructions. Over 11,000 financial institutions globally are connected to the SWIFT system.

SWIFT provides different messaging formats and schemas. The most common is the FIN message, which follows a store-and-forward mode: messages sent from the source are stored at a central intermediary location before being transmitted to the recipient. Another format is InterAct, which is XML-based and offers features such as real-time messaging and query-and-response capabilities. Finally, FileAct messages are used to transfer files, such as large batches of messages or other payment-related files. Many of SWIFT’s messaging formats are based on ISO standards, such as ISO 15022 and, more recently, ISO 20022.

SWIFT messages are categorized using the [convention MT (message type/text)](https://oreil.ly/7v4oO), followed by three digits that indicate the message category, group, and type (e.g., MTxxx). There are nine message categories in the SWIFT system; for example, MT1xx is for customer payments and checks, and MT5xx is for securities market transactions.

Consider a scenario where Corporation A wants to send $500,000 to Corporation B. Corporation A initiates the transaction by submitting payment instructions to its bank (Bank 1) using an MT101 message (or ISO 20022 pain.001). Upon receiving the message, Bank 1 issues a credit transfer request to Corporation B’s bank (Bank 2) using an MT103 message (or ISO 20022 pacs.008). [Figure 7-3](#ch07_figure_3_1724776832717137) illustrates the flow.

### Figure 7-3. A SWIFT transfer

![Figure 7-3. A SWIFT transfer](images/fden_0703.png)

In this example, it was assumed that Bank 1 and Bank 2 have a corresponding banking relationship, which allows them to directly exchange messages such as MT101 and MT103. However, if they do not have a corresponding banking [relationship](https://oreil.ly/UJ8wM), the payment process would involve one or more intermediary or correspondent banks. Recently, SWIFT launched SWIFT GPI (Global Payments Innovation) to enhance the cross-border payment experience, addressing the industry’s demands for greater speed, traceability, and transparency.

Now that you have an understanding of data ingestion processes and formats, let’s explore the various technological options for integrating a data ingestion mechanism into a financial data infrastructure.

# Data Ingestion Technologies

To enable and integrate data ingestion capabilities into a financial data infrastructure, one or more ingestion mechanisms need to be implemented. To this end, a number of technological options are available to meet varying business and technical needs. In this section, I will discuss six of the most common ingestion technologies used in financial markets.