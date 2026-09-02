### Note

Monolith architectures tend to be seen as a bad thing by default. This, however, is not necessarily true. A monolith architecture is a choice. It can be pretty good in some contexts but should be treated carefully and on a case-by-case basis to avoid its pitfalls. In 2023, Amazon Prime Video [decided to switch to a monolith architecture from a distributed microservices architecture](https://oreil.ly/-QaAT). The move to a monolith architecture helped achieve higher scalability and resilience, and reduced infrastructure costs by 90%.

### Modular architecture

In a modular architecture, an application is split into smaller modules that can be developed, deployed, tested, and scaled separately. Different teams may own different modules and manage the resource and feature requirements of each separately.

The most popular modular architecture pattern is the *microservices*, a term used to describe small, autonomous applications that work together to achieve a common goal. In many cases, a microservice architecture is produced from refactoring a complex monolith codebase that has reached the limits of scalability and performance. In Chapter 11, we will talk about microservice workflows, where you will learn more about microservice-related concepts and design patterns.

### Tip

If you are considering a refactoring project of your monolith to a microservice architecture, make sure you plan the migration ahead of time and produce the necessary software architecture metrics and evaluations. A number of best practices exist in this regard. For example, [software architecture evaluation techniques](https://oreil.ly/cMF9R) can be used to assess the quality and reliability requirements of a proposed/chosen software architecture. Moreover, tools such as the Modularity Maturity Index (MMI), fitness functions, and [software metrics](https://oreil.ly/ZwSYY) can be used to assess which components of the system need to be refactored, replaced, or left as they are.

# Summary

This chapter provided a general overview of the technical implementation aspects of financial data engineering. It covered the financial data engineering lifecycle as a framework for organizing the various layers of a financial data infrastructure: ingestion, storage, transformation and delivery, and monitoring.

Following that, the chapter outlined a set of six criteria intended to assist financial institutions in making informed decisions when evaluating technological alternatives for the FDEL stack. These criteria serve as a general guideline applicable to all layers of the FDEL. In the next chapters, you will learn about additional criteria specific to each layer within the FDEL.

The next four chapters will cover each of the four FDEL layers in depth to provide more technical details. More specifically, Chapter 7 will cover the ingestion layer, Chapter 8 the storage layer, Chapter 9 the transformation and delivery layer, and Chapter 10 the monitoring layer.

1 Layered architectures are quite common in software engineering. Their main advantages include simplicity, maintainability, familiarity, and cost. To learn more about this topic, I recommend Mark Richards and Neal Ford’s [*Fundamentals of Software Architecture: An Engineering Approach*](https://oreil.ly/cuPFF) (O’Reilly, 2020).

2 According to the [Basel framework](https://oreil.ly/i1WO6), operational risk is defined as “the risk of loss resulting from inadequate or failed internal processes, people and systems or from external events.”

3 For a high-level introduction to the CPU, GPU, and FPGA, I recommend Intel’s article [“Compare Benefits of CPUs, GPUs, and FPGAs for Different oneAPI Compute Workloads”](https://oreil.ly/S1Z6h).

4 For a benchmark study, I recommend S. Borağan Aruoba and Jesús Fernández-Villaverde’s [“A Comparison of Programming Languages in Macroeconomics”](https://oreil.ly/cTLy8), *Journal of Economic Dynamics and Control* 58 (September 2015): 265-273.

5 For a detailed study on the cloud as a general-purpose technology, I recommend Federico Etro’s [“The Economic Impact of Cloud Computing on Business Creation, Employment and Output in Europe”](https://oreil.ly/55cZq), *Review of Business and Economics* no. 2 (January 2009): 179–208.

6 For a good introduction, see Jamil Mina, Armin Warda, Rafael Marins, and Russ Miles’ [*Digitalization of Financial Services in the Age of Cloud*](https://oreil.ly/qp8wK) (O’Reilly, 2022).

7 An excellent reference on cloud economics is Joe Weinman’s *Cloudonomics: The Business Value of Cloud Computing, + Website* (Wiley Online Library, 2012).

8 To learn more about cloud migration strategies, see [“What Is a Cloud Migration Strategy?”](https://oreil.ly/PfGKC) by VMware.

9 For an interesting read on this topic, I recommend Thomas Boillat and Christine Legner’s [“From On-Premise Software to Cloud Services: The Impact of Cloud Computing on Enterprise Software Vendors’ Business Models”](https://oreil.ly/3bFI9), *Journal of Theoretical and Applied Electronic Commerce Research* 8, no. 3 (December 2013): 39–58.

# Chapter 7. Data Ingestion Layer

In Chapter 2, we learned about the different sources and mechanisms that generate financial data. This included public, market, alternative, and internal sources. Once data is generated at the source, its lifecycle within a financial data infrastructure begins with ingestion. As this chapter will show, data ingestion isn’t as simple as the term may sound. In today’s complex financial data landscape, data ingestion has expanded to encompass a large variety of data transmission and arrival processes as well as ingestion technologies, mechanisms, and formats.

Data ingestion serves as the foundational layer for information exchange in financial market operations. It facilitates communication among financial institutions and market participants for initiating transactions like payments, settlements, and trades. It also supports the exchange of inquiries and notifications between financial entities. Furthermore, compliance with regulatory requirements relies on efficient data ingestion practices, enabling financial firms and brokers to transmit various financial details and compliance reports to regulatory bodies. In addition, data ingestion is essential for disseminating market data and delivering real-time updates, critical for maintaining liquidity and operational efficiency throughout financial markets.

This chapter will examine the data ingestion layer as the primary entry point for receiving transmitted data and as a crucial bridge facilitating communication and information exchange among financial institutions and other entities.

# Data Transmission and Arrival Processes

Data ingestion is a process wherein data gets transmitted from a given source, travels over a network, and arrives at its destination. Understanding the details of such a process is critical for designing a reliable financial data infrastructure that meets different business and technical requirements. With such knowledge, financial data engineers can optimize time and mission-critical financial applications, design cost-effective and efficient data pipelines, anticipate scalability needs, manage security, and guide technology choices such as database management systems.

In this section I’ll explain the standard transmission protocols that enable most data transactions worldwide and will provide an examination of the many types of data arrival patterns.

## Data Transmission Protocols

When designing a system that transmits and receives data, transmission protocols, also known as communication protocols or network protocols, are an essential component. Simply put, a transmission protocol is a set of rules, techniques, and definitions that allow two or more agents or machines to exchange data over a network such as the internet.

Understanding industry transmission protocols is crucial to mastering the art of data ingestion. A data infrastructure is reliable only if it can access, deliver, and ingest data over a network. This is particularly relevant to the financial industry, which relies substantially on data transfers due to the large volume of financial transactions.

Various communication protocols and standards are employed throughout the data transmission lifecycle, each serving specific purposes. A variety of models have been developed to establish a reference framework. Such models rely on the idea of organizing network protocols and the technologies used to implement them into distinct layers. In such a design, each protocol belongs to one layer, and each layer is interested in the services that it offers to the layer above. This defines the *service model* of the layer. In this architecture, each service performs certain actions that belong to it, uses input/instructions from the service below, and conforms to the requirements of the service above. For example, the service model of layer N might involve encrypted message delivery between systems. This could be realized by implementing nonencrypted message delivery at layer N-1 and incorporating layer N functionality to encrypt messages.

The most popular internet protocol model is the seven-layer *Open Systems Interconnection* (OSI) model, defined in standard [ISO/IEC 7498](https://oreil.ly/H4hHw), and the four-layer internet protocol suite known as the *TCP/IP*, developed by the Department of Defense (DoD). Both models are illustrated in [Figure 7-1](#ch07_figure_1_1724776832717088).

### Figure 7-1. Seven-layer OSI model versus four-layer TCP/IP model

![Figure 7-1. Seven-layer OSI model versus four-layer TCP/IP model](images/fden_0701.png)

### Note

Keep in mind that communication layer models such as OSI and TCP/IP are conceptual frameworks intended to discuss networking in a structured way. Reality may be more complex than a model. For example, some protocols or functionalities might be hard to place in one single layer and multiple layers may duplicate the same functionality. Additionally, layers might have dependencies that could blur the line between them. Nevertheless, reference models are very useful for thinking about such a complex topic.

In the following sections, I will briefly discuss the various network layers of the TCP/IP model. I chose to illustrate the TCP/IP model rather than OSI due to its simplicity and popularity among engineers.

### Application layer

This is the topmost layer, where network applications and their protocols reside. Applications in this layer are distributed over multiple end systems, and they exchange packets of information via the service protocols. Such protocols include the following:

Hypertext Transfer Protocol (HTTP):   Used to serve web page requests

Simple Mail Transfer Protocol (SMTP):   Used to send and exchange emails

File Transfer Protocol (FTP):   Used to transfer files between two systems

Domain Name System (DNS):   Used to resolve web page names into their address

Secure Shell (SSH):   Used to secure login to remote servers and execute commands, or secure file transfer through the *Secure File Transfer Protocol* (SFPT)

Advanced Message Queuing Protocol (AMQP):   Used for message-oriented communication between applications

Message Queuing Telemetry Transport (MQTT):   Designed for lightweight, message-oriented communication

### Transport layer

This layer is responsible for transferring application layer packets between application endpoints in a reliable, optimized, and guaranteed way. Transport layer messages are commonly called *segments*. The most important transport layer protocols include the *Transmission Control Protocol* (TCP) and *User Datagram Protocol* (UDP). TCP is a *connection-oriented* protocol, meaning that the sender and receiver must establish a continuous connection before exchanging data segments. This feature makes TCP a reliable protocol, as it acknowledges message reception and resends data again in case it doesn’t arrive. TCP breaks down an information packet from the application layer into a small set of segments and submits it for delivery to the next layer, the network layer. In the network layer, segments are represented as datagrams.

Additionally, TCP offers functionalities such as flow and congestion control, which regulate the data transmission rate and dynamically adapt to network congestion through message segmentation and breakdown. Furthermore, TCP ensures secure delivery by keeping track of all transmitted segments and confirming their successful delivery.

On the other hand, UDP is a faster but less reliable protocol than TCP. UDP is a *connectionless* protocol, meaning that data transmission happens via a fire-and-forget mechanism without establishing a continuous connection. This means that it offers fewer delivery guarantees compared to TCP.

A significant improvement over TCP is the *Transport Layer Security* (TLS) protocol, also referred to as TLS/SSL, which is designed to facilitate secure communication across insecure networks. TLS can be positioned between the application and transport layers. It encrypts data before transmission via TCP and decrypts it upon arrival at the transport layer of the receiving end. In addition to encryption, TLS also manages identity verification (authentication), facilitates the exchange of encryption keys between hosts, and mitigates Man-in-the-Middle (MITM) attacks through the [TLS handshake process](https://oreil.ly/gqnmF).

TLS is very important to understand because you will encounter it several times when designing a financial data infrastructure. A common use case for TLS is enabling encrypted connections to a database engine.1 Similarly, when using HTTPS instead of HTTP to serve web requests and design APIs, you are adding a TLS/SSL layer for encryption.

# Electronic Banking Internet Communication Standard

Internet protocols are essential in developing financial communication protocols. A good example in this context is the *Electronic Banking Internet Communication Standard* (EBICS), developed in Germany and adopted by France, Switzerland, and other countries to exchange instructions between financial institutions and corporations over the internet. The EBICS standard has been primarily used to initiate *Single Euro Payments Area* (SEPA) exchanges over the internet, such as SEPA Direct Debits and SEPA Credit Transfers.

According to the [official technical specifications](https://oreil.ly/9MIgQ), the TCP/IP internet protocol suite had a decisive influence on the design of EBICS. Data is transmitted as packages via IP addresses or URLs that get resolved to IPs. Package transfer and delivery are monitored and guaranteed via the TCP protocol. The client and the EBICS server communicate using the HTTP protocol at the application layer. The XML file format has been selected as the protocol language at the application layer. To ensure security and data encryption, EBICS relies on TLS to secure communications via HTTPS.

### Network layer

This layer moves information units known as *datagrams* between two hosts. When a source host wants to send data to a target host, it includes a transport layer segment along with the target host’s address. Upon reception, the network layer ensures the segment is delivered to the transport layer on the target host.

The most prominent network layer protocol is the *internet protocol* (IP), with its version 4 (IPv4) being the most prevalent. IPv6 serves as its successor and has been progressively integrated into the public internet infrastructure since around 2006. To add an extra encryption layer on top of the IP protocol, the *IPsec* can be used. IPsec is commonly used with Virtual Private Networks (VPNs).

The IP protocol submits datagrams independently to the receiving host. A datagram might include several fields about its content, destination, and relevant details for the receiving end. Once received by the host, the datagrams are assembled again through the TCP protocol at the transport layer.

Understanding IP addressing is of primary importance for financial data engineers, particularly in the context of designing distributed systems such as Apache Cassandra for distributed databases or Apache Spark for distributed computing environments. In these setups, a typical strategy involves provisioning a defined number of nodes (machines) and linking them to form a cluster. Each node in the cluster is uniquely identified by an IP address, which can be used by the cluster manager and the worker nodes to establish connections and communicate with each other.

Another interesting use case of IP addressing is with Virtual Private Clouds (VPCs). One of the main concepts behind VPCs is the *subnet*, which refers to a range of IP addresses assigned to the VPC. IP addresses within a subnet are private, meaning they are inaccessible via the public internet but solely accessible through the VPC’s internal network. When you provision and launch an instance of a given resource into a VPC, a primary private IP address from the subnet range is assigned to the instance.2

### Network access layer

In this layer, datagrams coming from the network layer get routed through a network of routers that connect the network layer interfaces of the source and target. Datagrams are moved from one node (router) to the next until they reach their destination. Examples of network interface protocols include the Ethernet, WiFi, and Data Over Cable Service Interface Specification (DOCSIS) protocols employed in cable access networks.

The physical transmission of the individual data bits through the network happens via hardware devices that directly interface with a network, such as coaxial, optical, fiber, or twisted pair cables.

# Speed Physics in Financial Markets

You might wonder how the physical networking layer is relevant to financial markets. Interestingly, it holds significant relevance and has been transforming certain market infrastructures, such as trading.

An illustrative example is the establishment of the transatlantic fiber-optic line [Hibernia Express](https://oreil.ly/m8oFR), designed to link London and New York with ultra-low latency in response to demand from banks, exchanges, and trading firms. Thanks to Hibernia Express, London and New York experienced a five-millisecond reduction in latency compared to existing high-speed network services. In the era of automated trading, even a five-millisecond difference holds substantial importance to computers.

High-frequency traders, who have been engaged in a technical arms race to accelerate trade execution time, are [speculating on an experimental form of fiber-optic cable](https://oreil.ly/sKaY5), called *hollow-core fiber*, to speed up their trades by billionths of a second.

## Data Arrival Processes

Data may arrive at the ingestion layer with different temporal and structural patterns. In this section, I will use the *data arrival process* (DAP) concept to identify and describe the characteristics of a certain data ingestion pattern. A variety of DAPs may exist. Let’s examine six that are particularly relevant to financial data engineering.

### Scheduled data arrival process

In a scheduled DAP, data is ingested into the system according to a predetermined schedule and ingestion specifications. This process is generally more manageable as it follows a predictable pattern, with known details such as the arrival time, data type, format, volume, and ingestion method.

Scheduled DAPs are quite common in financial markets. For example, they may be used in the following circumstances:

* Arrival of company annual report filings at specific intervals such as by the end of the year, the end of March of each year, or at a future announced date
* Arrival of historical financial data snapshots from a financial data vendor on a daily, weekly, monthly, or yearly basis
* Arrival of financial institutions’ required regulatory filings on a predefined date
* Arrival of data from continuous model training, stress testing, scenario analysis, and other financial quantitative analysis

Knowing when the data is expected to arrive can greatly enhance financial data engineers’ jobs. This is because they can plan data ingestion jobs, anticipate the capacity and computational needs of the data infrastructure, and provision the necessary resources on a predictable basis (e.g., on a specific day of the week).

The main drawback of scheduled DAPs is the delay between data generation and arrival, which can impact data timeliness. Additionally, if scheduled jobs run without fetching any data, it can waste resources.

### Event-driven data arrival process

When the arrival of data is contingent upon the occurrence of an event that cannot be predicted in advance, the DAP becomes event-driven. Event-driven DAPs are very common in financial markets. These include the arrival of the following types of data:

* Trade and quote data upon submission and execution in the market
* Financial information messages
* Transaction data upon the execution of a financial operation, such as payments, transfers, and others
* Client files for loan and credit card applications
* Data streams from financial data vendors
* News data
* Company updates and announcements
* Social media posts

The primary advantage of event-driven DAPs is that data is available shortly (or immediately) after its generation. This allows financial institutions to act promptly in response to new information and have the most recent, up-to-date market and operational insights. For this reason, event-driven systems are often associated with real-time systems. A system is considered real-time if its response time—typically set at a very low value—is essential to its proper functioning. Moreover, event-driven DAPs can save costs and optimize resource allocation as they switch resource utilization from a fixed to an on-demand pattern.

# What Exactly Is a Real-Time System?

The term *real-time* is used widely in a variety of contexts. To many people, real-time would mean “instantaneously” or “immediately.” For software and system engineers, real-time may refer to time-related characteristics of a system or application, such as processing time, response time, or latency. Given the significance of real-time systems in finance, I will provide a detailed description to clear up any misconceptions. To do so, I will draw a summary from the seminal work of Seppo J. Ovaska and Philip A. Laplante, *Real-Time Systems Design and Analysis: Tools for the Practitioner* (Wiley-IEEE Press, 2011).

Authors Laplante and Ovaska define a real-time system as “a mapping of a set of inputs into a set of outputs.” The time between a system’s reception of input and the generation of the final output is called the system’s response time. The nature and speed of the response time depend on the system’s features and purpose.

Building on this, the authors define a real-time system as a “computer system that must satisfy bounded response-time constraints or risk severe consequences, including failure.” Failure, in this case, means that the system is not able to function or meet one of the requirements of its design specifications. More specifically, a failed real-time system is one that cannot satisfy timing or deadline constraints established in its specifications. In short, a system does not necessarily need to respond instantaneously to be considered real-time; it must simply define and meet response time criteria in its specifications.

At this point, however, all systems may be considered real-time as there is always some sort of time constraint. To further clarify this point, Laplante and Ovaska classify real-time systems into three categories:

Soft real-time systems:   A failure to meet a response time constraint leads to performance degradation but not system failure.

Hard real-time systems:   A failure to meet a single deadline can lead to complete or major system failure.

Firm real-time systems:   Missing a few deadlines may not be consequential, but missing more than a few may lead to complete or major system failure.

According to business and operational considerations, real-time systems can be categorized as soft, hard, or firm. For instance, if an ATM machine occasionally fails to respond to requests within its internal time limit (e.g., 10 seconds), it might lead to some customer dissatisfaction, but it remains tolerable, thus qualifying as a soft real-time system.

Conversely, in the context of a hedge fund engaged in high-frequency trading, delays in receiving data beyond expected deadlines could result in significant financial losses, necessitating the classification of the system as hard or firm. Another example is financial systems that involve Forex currency conversions. This process frequently includes a *Request for Quote* (RFQ), where a market participant requests a price quote from a liquidity provider or Forex broker to either buy or sell a specified amount in a particular currency pair. RFQs include an expiry time, during which the liquidity provider commits to honoring the quoted price. Failing to settle a Forex transaction within the RFQ’s expiry time can expose the requesting institution to market risks, potentially resulting in financial losses.

Importantly, it is still common for people (even engineers) to think of real-time systems as being “instantaneous.” To understand why, let’s take the technological concept of *real-time payments* (RTPs). According to [Stripe](https://oreil.ly/T9K7B), RTPs are “instant payments that are processed immediately and continuously, 24/7.” In this context, instant refers to the fact that money is moved between bank accounts in seconds instead of hours or days (as is the case with traditional payment systems). For humans, several seconds may feel instantaneous, thus the use of the term instant in this context.

Nonetheless, I highly recommend following a systematic approach similar to the one outlined above when creating real-time financial systems. Software and data engineers must carefully understand and incorporate time constraints and limitations into their systems and investigate potential ways to change a soft real-time system into a hard or firm one, or vice versa.

With the emergence of cloud computing, event-driven data processing technologies have remarkably increased in popularity. These include message brokers (detailed in Chapter 8), such as Amazon Simple Notification Service (SNS), Amazon Managed Streaming for Apache Kafka (MSK), and Google Pub/Sub, as well as event-driven serverless computing platforms (illustrated in Chapter 9), such as AWS Lambda and Google Cloud Functions.

As event-driven DAPs are unpredictable, designing an event-driven financial data infrastructure requires careful attention. One essential feature to focus on concerns the ability of the infrastructure to scale to accommodate varying workloads and occasional spikes. Moreover, due to the data-intensive nature of event-driven DAPs, data quality issues such as errors, outliers, and timeliness may easily arise. Furthermore, event-driven DAPs may incur the issue of duplicate or concurrent ingestions, which happens when the same data or file gets ingested twice or more. This requires careful attention when designing the data infrastructure, as it might impact data consistency and potentially cause system failures.3

### Homogeneous data arrival process

In a homogenous DAP, the ingested data has predetermined consistent properties. For example, if you purchase a subscription to a dataset provided by a financial data provider, you are likely to know the kind of data, the schema, the ingestion format, and other details.

A homogeneous DAP is simpler to manage and maintain, and it helps ensure data integrity and consistency. In the financial industry, a number of projects have been underway to standardize and universalize data input and exchange formats. The section [“Data Ingestion Formats”](#ch07_data_ingestion_formats_1724776832765674) will illustrate examples of standardized financial data formats.

Importantly, you should avoid overfitting your financial data architecture to handle only one type or format of data. This may cause problems if a data attribute changes or a new data type is ingested.

### Heterogeneous data arrival process

In a heterogeneous DAP, ingested data may possess variable attributes such as extension, format, type, content, schema, and others. Heterogeneous DAPs are quite common in finance. For example, financial data vendors provide their data in different formats and structures. In addition, for optimization purposes, different types of data may be stored and transmitted in specific formats (a topic that will be covered in the section [“Data Ingestion Formats”](#ch07_data_ingestion_formats_1724776832765674) in this chapter). Furthermore, different internal systems within financial institutions may generate data with their unique formats and structures.4

When designing for heterogeneous DAPs, the financial data infrastructure must account for various ingestible data types and possess the necessary capability to handle each. This complexity makes optimizing the infrastructure more challenging, but it also increases the financial institution’s flexibility to ingest and accommodate new data sources.

Such flexibility is critical in today’s fast-changing financial data landscape, where new data sources emerge regularly, and the amount and speed with which data is generated has grown significantly. Being able to accommodate a new data source means adding new analytical capabilities, developing new products, and gaining comprehensive insights into market trends, sales, customers, and operations.

### Single-item data arrival process

In a single-item DAP, data is ingested either on a record-at-a-time or file-at-a-time basis. Think, for example, about the arrival of information related to a payment transaction, bank loan application, market order, analytical report, or piece of news.

The main advantages of single-item DAPs are traceability and transactional guarantee. When the ingestion process concerns a single data item, it is typically easier to trace its lifecycle through system logs. Moreover, inserting one record at a time allows for easier data integrity and constraint checks.

As an illustration, let’s say we have a database that stores customer financial transactions. A simple SQL-based single-item ingestion into this table would look like this:

```
-- PostgreSQL
INSERT INTO customer_transactions (
  user_id,
  transaction_id,
  time,
  transaction_type,
  amount,
  communication
  ) VALUES (
    195,
    'XT4h4Y453',
    '2024-01-20 10:09:42',
    '1985-02-10',
    'Credit Transfer',
    'online course subscription fees'
  )
```

In some circumstances, single-item DAPs may lead to performance bottlenecks. For example, if the number of data ingestions is remarkably high, then it may jeopardize the system’s ability to handle all incoming requests. This can happen due to a max connection limit on the database side (discussed in Chapter 8) or quota limit on an API side (covered in section [“Data Ingestion Technologies”](#ch07_data_ingestion_technologies_1724776832766491) in this chapter). Additionally, ingesting a large number of records one at a time can be very slow, which in turn can impact data quality dimensions such as timeliness.