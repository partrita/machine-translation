### Variety

The third feature that defines big data is variety, which refers to the presence of many data types, formats, or structures. To better describe this concept, let’s illustrate the three types of structures that data can have:

Structured data:   This data has a clear format and data model, is easy to organize and store, and is ready to analyze. The most common example is tabular data organized as rows and columns.

Semi-structured data:   This type of data lacks a straightforward tabular format but has some structural properties that make it manageable. Often, semi-structured data is parsed and stored in a tabular format for ease of use. Examples include XML and JSON, which store data in a hierarchical tree-like format.

Unstructured data:   This data lacks any predefined structure or formatting and requires parsing and preprocessing using specialized techniques before analysis. The majority of data worldwide is unstructured, including formats like PDF, HTML, text, video, and audio.

The variety of financial data has significantly increased in recent years. For example, the US Securities and Exchange Commission’s Electronic Data Gathering, Analysis, and Retrieval system (EDGAR) receives and [handles about two million filings a year](https://oreil.ly/v0BjW). Such filings can be complex documents, many of which contain multiple attachments, scores of pages, and several thousands of pieces of information or details. Another example is alternative data sources such as news, weather, satellite images, social media posts, and web search activities, which have been shown to be highly valuable for financial analysis and product development.6

Increased variety in financial data opens up new opportunities:

* Incorporating new variables into financial analysis for enhanced predictions
* Capturing new economic and financial activities that can’t be analyzed using structured data alone
* Facilitating the development and integration of innovative financial products like news analytics, fraud detection, and financial networks
* Enhancing regulatory capabilities to capture complex market structures for more effective oversight

However, data variety also presents several data engineering challenges:

* Building a data infrastructure capable of efficiently storing and managing diverse types of financial data, including structured, semi-structured, and unstructured formats
* Implementing data aggregation systems to consolidate different data types into a single access point
* Developing methodologies for cleaning and transforming new structures of financial data
* Establishing specialized pipelines to process varied types of financial data, such as natural language processing for text and deep learning for images
* Implementing identification and entity management systems to link entities across a wide range of data sources

# Be Wary of the Curse of Dimensionality in Financial Data

Although the volume of financial data has experienced significant growth in recent decades, special consideration should be given to the ratio of data observations to the number of variables. For example, assume we have an initial sample of 10 firms and 5 features about their performance (e.g., revenues, net profit, and so on). If data increases in size both in terms of observations (more firms) and variables (more features), then we can conduct reliable analysis using the new, larger sample. However, if the increase in data size concerns mainly the features and not the observations (i.e., no more firms added to the dataset), then we might encounter the issue known as the [*curse of dimensionality*](https://oreil.ly/TnxXI). It states that for a statistical or machine model to produce valid predictions, the number of observations needs to grow exponentially with the number of features. Some researchers have [argued](https://oreil.ly/jE62C) that this has been the case in some financial applications, such as asset management. A number of techniques can be used to counteract the curse of dimensionality: *data augmentation* (collecting or generating more data) and *dimensionality reduction* (reducing the number of features in the data).

## Finance-Specific Data Requirements and Problems

The financial industry has always witnessed constant transformation: new players joining and disrupting the competitive landscape, new technologies emerging and revolutionizing the way financial markets function, new data sources expanding the space of opportunities, and new standards and regulations getting released, promoted, and enforced.

Given these dynamics, the financial industry sets itself apart in terms of the issues and challenges that its participants face. A few key ones are listed here:

* There is a lack of a standardization in some key areas:

  + Identification system for financial data
  + Classification system for financial assets and sectors
  + Financial information exchange
* Lack of established data standards for financial transaction processing
* Dispersed and diverse sources of financial data
* Adoption of multiple data formats by companies, data vendors, providers, and regulators
* Complexity in matching and identifying entities within financial datasets
* Lack of reliable methods to define, store, and manage financial reference data (discussed in Chapter 2)
* Lack of relevant data for understanding and managing various financial problems due to poor data collection processes (e.g., granular data on financial market dependencies and exposures necessary for systemic risk analysis)
* The constant need to adapt data and tech infrastructure to meet new market and regulatory demands (e.g., the EU’s *Instant Payments Regulation* requires all payment service providers to offer 24/7 euro payments within seconds, necessitating upgrades to legacy systems)
* The constant need to record, store, and share financial data for various regulatory and market purposes (e.g., the EU’s *Central Electronic System of Payment Information* mandates payment system providers to track cross-border payment data and share it with the tax authorities of EU member states).
* Absence of standardized practices for cleaning and ensuring the quality of financial data
* Difficulty in aggregating data across various silos and divisions within financial institutions
* Creating consolidated tapes, which integrate market data from multiple sources including trade and quote information across various venues, continues to pose technological and market challenges
* Balancing innovation and competitiveness with regulatory compliance
* Persisting concerns regarding security, privacy, and performance in cloud migration strategies
* Continued reliance on legacy technological systems due to organizational inertia and risk aversion

Over the years, a number of industry and regulatory initiatives were proposed to tackle these issues. For example, to facilitate a standardized delivery of financial services and products, the United States established the [*Accredited Standards Committee X9* (ASC X9)](https://oreil.ly/_xsi6) to create, maintain, and promote voluntary consensus standards for the financial industry. In addition to setting national standards in the United States, ASC X9 can submit standards to the International Organization for Standardization (ISO) in Geneva, Switzerland, to be considered an international ISO standard. ASC X9 develops standards for many different areas and technologies, including electronic legal orders for financial institutions, electronic benefits and mobile payments, financial identifiers, fast payment systems, cryptography, payment messages, and more.

Additionally, international agencies such as the Association of National Numbering Agencies (ANNA) were established to coordinate and foster the adoption of ISO-based financial identifiers (covered in Chapter 3). Frameworks such as *eXtensible Business Reporting Language* (XBRL) (discussed in Chapter 7) were developed to standardize the communication and reporting of business information. Following the financial crisis of 2007–2008, the financial industry realized the need for a standardized identifier for legal entities involved in market transactions, which led to the [development](https://oreil.ly/-GmxD) of the celebrated Legal Entity Identifier (LEI), discussed in Chapter 3.

Furthermore, financial market players have also been actively contributing and providing solutions to the above-mentioned problems. To give a few examples, Bloomberg is currently promoting its *Financial Instrument Global Identifier* (FIGI) as an open standard for identifying financial instruments; LSEG released its *Permanent Identifier* (PermID) to complement existing market identifiers; and financial institutions such as JPMorgan have been pioneers in promoting market practices such as [Value at Risk (VAR)](https://oreil.ly/_KbIQ) in the 90s, and more recently the use of [financial APIs](https://oreil.ly/iuFY_) to support fast, real-time data transactions.

## Financial Machine Learning

Machine learning (ML) stands out as one of the most promising investments for shaping the future of the financial industry. To understand what machine learning is, it’s better first to understand what artificial intelligence (AI) is. Although there is no well-accepted definition of artificial intelligence, in its simplest form, AI aims to understand the nature of intelligence to build systems that can reliably perform tasks that usually would require human intelligence, such as speech recognition, visual perception, decision-making, and language understanding. [Figure 1-4](#ch01_figure_4_1724776823880086) illustrates the various fields of inquiry in artificial intelligence.

### Figure 1-4. An outline of artificial intelligence fields

![Figure 1-4. An outline of artificial intelligence fields](images/fden_0104.png)

Machine learning stands out as a highly popular and significant subfield within AI. It focuses on building systems that can discover patterns from data, learn from their mistakes, and make predictions. The key word in machine learning is *learning*, which the computer scientist Tom Mitchell eloquently illustrates as follows:7

> A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.

Machine learning scientists and practitioners often develop models based on three types of learning: supervised, unsupervised, and reinforcement learning. Let’s explore each in detail.

### Supervised learning

Supervised learning describes a learning approach that relies on an annotated (labeled) dataset comprised of a set of explanatory variables (called *features*) and a response variable (called a *label*). In a supervised setting, the model is trained to identify patterns using explanatory variables. The training process involves showing the model the actual value (label) it should have predicted, hence the term “supervised,” and allowing it to learn from its mistakes (as illustrated in [Figure 1-5](#ch01_figure_5_1724776823880102)).

### Figure 1-5. Supervised learning process

![Figure 1-5. Supervised learning process](images/fden_0105.png)

When building a supervised system, modelers start by fitting one or more models on training data, where features and labels are known, via a selected optimization process such as *gradient descent*. Successively, the fit model(s) is tested on a second chunk of the data, called the validation dataset. The goal of the validation dataset is to allow the machine learning expert to fine-tune the so-called model *hyperparameters* via a process called *regularization*. Regularization is a technique used to achieve a balance between *bias* (how well a model learns the training data) and *variance* (how good the model is at generalizing to new instances unseen during training). Finally, a test dataset is used to evaluate the performance of the model that did best on the validation dataset. Performance metrics include accuracy, precision, root mean square error (RMSE), and mean square error (MSE), to name a few.8

Supervised learning can be divided into two categories: *classification*, which predicts a class label for a categorical variable, and *regression*, which predicts a quantity for a numerical variable. Linear regression, autoregressive models, generalized additive models, neural networks, and tree-based models are well-known regression methods. For classification tasks, methods such as logistic regression, support vector machines, linear discriminant analysis, tree models, and artificial neural networks are commonly used.

In finance, supervised learning is extensively employed for both classification and regression tasks. Examples of financial regression problems include stock price forecasting, volatility estimation and prediction, asset pricing, and risk assessment. Classification problems are also plenty in finance, for example, credit scoring, default prediction, corporate action prediction, fraud detection, and credit risk rating.

### Unsupervised learning

Unsupervised learning is used to extract patterns and relationships within data without relying on known target response values (labels). Unlike supervised learning, it does not have a teacher (supervisor) correcting the model based on knowledge of the correct answer (as illustrated in [Figure 1-6](#ch01_figure_6_1724776823880120)).

### Figure 1-6. Unsupervised learning process

![Figure 1-6. Unsupervised learning process](images/fden_0106.png)

There are two main types of unsupervised learning: *clustering*, where a model is trained to learn and find groups (clusters) in the data, and *density estimation*, which tries to summarize the distribution of the data. Examples of clustering techniques include k-means, k-nearest neighbor, principal component analysis, and hierarchical clustering, while the kernel density estimator is perhaps the most common example of density estimation techniques.9

Unsupervised learning applications in finance are still in their early stages, but the future trend is promising. For example, clustering can be used to group similar financial time series, cluster stocks into groups based on sector or risk profile, analyze customer and market segmentation, and find similar firms or customers to assign similar scores or ratings.

### Reinforcement learning

In reinforcement learning, an artificial agent is placed in an environment where it can perform a sequence of actions over a state space and learn to make better decisions via a feedback mechanism. The key difference between this technique and supervised learning is that the feedback from the teacher is not about providing the right answer (true label); instead, the agent is given a reward (positive or negative) in order to encourage certain behaviors (actions) and punish others (see [Figure 1-7](#ch01_figure_7_1724776823880136)).

### Figure 1-7. Reinforcement learning process

![Figure 1-7. Reinforcement learning process](images/fden_0107.png)

As many financial activities entail decision-making by agents, there has been a considerable interest among financial practitioners and researchers in reinforcement learning, which centers on optimal decision-making. Financial applications of reinforcement learning include portfolio selection and optimization, optimal trade execution, and market-making.10

# Generative AI and Large Language Models in Finance

Recently, an emerging field of AI, known as generative AI, has received remarkable attention following the introduction by OpenAI of the large language model (LLM) ChatGPT. In generative AI, a system is trained to generate one or more outcomes, such as text, image, and video, in response to prompts. In the case of ChatGPT, the user interacts with a chatting machine in a conversational way, where the machine can answer a wide variety of questions, solve problems, generate code, make and challenge statements, admit its mistakes, and at the same time reject inappropriate prompts.

Language modeling is quite popular in finance. For example, it’s used in sentiment analysis, news classification, named entity recognition, fraud detection, and question answering. However, as of the time of writing of this book, no LLM has been tuned and adapted for the financial domain. As a first step in this direction, Bloomberg developed [BloombergGPT](https://oreil.ly/8FnP-), a 50-billion parameter LLM developed with a mixed approach that focuses on financial domain-specific capabilities, while also maintaining a competitive performance on general-purpose tasks.

BloombergGPT was trained on a massive dataset consisting of English financial documents such as filings, news, press releases, web-scraped documents, and social media pulled from the Bloomberg archives. This data was augmented with public datasets such as The Pile, the Colossal Clean Crawled Corpus (C4), and Wikipedia. In total, this has led to a comprehensive dataset of almost 700 billion tokens, half domain-specific and half general-purpose. The resulting model has outperformed existing open source models on financial-specific tasks while guaranteeing on par and sometimes better performance on general language tasks.

As an alternative to BloombergGPT, a group of researchers, in collaboration with the AI4Finance Foundation, developed and released [FinGPT](https://oreil.ly/tkWun), an open source framework that allows the development of LLMs for the financial domain. The data sources used to develop FinGPT include financial news, social media, filings, trends, and academic datasets.

GenAI applications are rapidly expanding within the finance industry. For instance, FactSet, a leading data and analytics provider, has launched [Portfolio Commentary](https://oreil.ly/69jEt). This tool uses AI to generate explanations of portfolio performance attribution analysis—the practice of explaining portfolio performance relative to a benchmark—within FactSet’s renowned Portfolio Analytics application.

Applied machine learning systems rely on data and computational resources; thus, having access to more data and computing power leads to better and faster predictions. In finance, where computational resources and datasets have grown, financial machine learning has emerged as a promising yet challenging area of research and practice.

According to [Marcos López de Prado](https://oreil.ly/255DX), a leading hedge fund manager and quantitative analyst, financial machine learning has proven to be very successful and is likely to be a major factor in shaping the future of financial markets, but it shouldn’t be ignored that it presents major challenges that need to be taken into consideration. Perhaps the most relevant challenge that’s worth mentioning is the problem of false discoveries. This refers to the practice of finding what seems like a valid pattern in the data, yet in reality is a spurious relationship.11 Other challenges include the interpretability/explainability of the models, performance, costs, and ethics.

For financial institutions to effectively invest in and leverage financial machine learning, they must ensure they are machine learning ready. This involves having the right team with expertise in both finance and machine learning, a sufficient quality and quantity of financial data for ML algorithms, a robust data infrastructure, dedicated ML-oriented data pipelines, DevOps (or MLOps) practices for seamless deployment and integration, and monitoring tools. With this foundation, financial data engineering becomes crucial. Financial data engineers collaborate closely with financial ML scientists and ML engineers to define data requirements, automate data transformations, perform quality checks, and structure ML workflows for fast and high-performance computations.

## The Disruptive FinTech Landscape

Following the 2007–2008 financial crisis, traditional financial institutions have faced a significant increase in regulatory requirements. Consequently, the focus of market participants has shifted substantially toward compliance. At the same time, as customers became more accustomed to using services online, demand for simple and user-friendly online financial products has increased. These factors paved the way for a new wave of technological innovation in the financial sector, commonly known as *FinTech*.

The term FinTech has emerged as a market portmanteau to describe both innovative technologies developed for the financial sector and the startup firms that develop these technologies. FinTech firms have attracted particular attention in the media and the market due to their innovative, flexible, and experimental approach. Not being constrained by regulatory debt, FinTechs have been employing modern and nonconventional approaches to solving and improving a wide range of financial problems, such as payments, lending, investment, fraud detection, and cryptocurrency. Traditional financial institutions would lack this flexibility due to factors such as organizational inertia, regulatory constraints, security concerns, and a lack of innovative culture.

The main distinguishing features of FinTech services are *specialization* and *personalization*. As small firms, FinTechs tend to focus on penetrating only specific and niche areas of the financial system. [Figure 1-8](#ch01_figure_8_1724776823880154) illustrates the different areas of specialization of FinTech firms. As the figure illustrates, the FinTech landscape spans all segments of the financial sector, from fundamental functions such as payments and investment to more specialized areas such as regulatory compliance (often called *regtech*) and analytics.

### Figure 1-8. A breakdown of the main FinTech investment areas

![Figure 1-8. A breakdown of the main FinTech investment areas](images/fden_0108.png)

Moreover, the FinTech business model has demonstrated competitiveness through its customizable and personalized offerings. For example, digital wealth management platforms like Betterment and Wealthfront provide clients with detailed surveys to assess their financial goals and risk preferences, enabling them to offer investment plans tailored to each investor’s unique objectives and expectations.

Overall, the FinTech market has seen rapid growth since its inception. According to a [report published by Boston Consulting Group](https://oreil.ly/rzLUV), as of 2023, there were roughly 32,000 FinTech firms globally, securing more than $500 billion in funding. The same report predicts that by 2030, the annual revenue of the FinTech sector is expected to reach $1.5 trillion, with banking FinTech representing 25% of the overall banking evaluations.

# Payments: The Dynamic Heart of Innovation in Financial Technology

In the rapidly evolving landscape of financial technology, payments represent the most active and vibrant area of innovation. As the central mechanism for the exchange of value, payments have undergone a dramatic transformation, driven by technological advancements, changing consumer expectations, and regulations. Today, the payments sector is not merely about transferring money; it is about creating the seamless, secure, and instantaneous financial experiences that are integral to our daily lives.

With the proliferation of smartphones, the rise of ecommerce, and the demand for real-time transactions, the payments industry is at the forefront of FinTech innovation. This sector is pioneering the use of cutting-edge technologies such as cloud computing, real-time systems, blockchain, open banking APIs, biometric authentication, and artificial intelligence to enhance security, efficiency, and user experience. As a result, payments are reshaping the financial ecosystem, promoting financial inclusion, and driving economic growth.

There are many types of entities involved in the payment ecosystem. Examples include the following:

Issuers:   Financial institutions that provide consumers with payment cards (credit, debit, or prepaid), such as JPMorgan Chase, Bank of America, and Citibank.

Acquirers:   Financial institutions that manage and process payment transactions for merchants, like Wells Fargo Merchant Services, First Data, and Elavon.

Payment processors:   Companies that handle the technical aspects of processing transactions between issuers and acquirers, including PayPal, Square, and Stripe.

Payment networks:   Networks that connect issuers and acquirers to facilitate card transactions, such as Visa, Mastercard, and American Express.

Payment gateways:   Services that act as an intermediary in electronic financial transactions. Examples include Authorize.net, Braintree, and Cybersource.

Digital wallet providers:   Companies offering electronic devices or software for storing payment information and making transactions, such as Apple Pay, Google Wallet, and Samsung Pay.

FinTech startups:   Innovative companies creating new payment solutions using advanced technology, including Revolut, Stripe, and Square.

Settlement institutions:   Entities that facilitate the final transfer of funds between financial institutions to complete payment transactions, such as Fedwire and the Clearing House Interbank Payments System (CHIPS).

Payment infrastructures:   Systems and networks that facilitate the processing, authorization, and settlement of financial transactions between parties. Examples include the Society for Worldwide Interbank Financial Telecommunication (SWIFT) for financial messaging and interbank communication and Australia’s New Payments Platform (NPP) for fast payments.

Additionally, there are several payment-related regulatory frameworks currently being developed and adopted. For instance, the European Union is moving forward with the following regulations:

Instant Payments Regulation:   Requires all payment service providers (PSPs) to offer the capability to send and receive euro payments within seconds, 24/7, across the EU.

Central Electronic System of Payment Information (CESOP):   Mandates payment system providers to track cross-border payment data and share it with the tax authorities of EU member states.

Markets in Crypto-Assets (MiCA) regulation:   Aims to harmonize EU market rules for crypto-assets.

Eurosystem Collateral Management System (ECMS):   A unified system for managing assets used as collateral in Eurosystem credit operations.

Third Payment Services Directive (PSD3) and Payment Services Regulation (PSR):   Seek to further harmonize the payment market and reduce national variations.

E-Money Directive:   Provides the legal framework for issuing and managing electronic money within the European Union.

For financial data engineering aspirants, diving into payments promises not just a career path but a gateway to shaping the future of digital transactions and financial services on a global scale.

To thrive in this technology-intensive, high-performance, and data-driven landscape, aspiring FinTech companies must prioritize their software and data engineering strategies. To compete with and/or collaborate with incumbent financial institutions, FinTechs must ensure the highest standards of quality, reliability, and security. In this context, financial data engineers play a crucial role by designing efficient and reliable data ingestion, processing, and analysis pipelines that can scale and seamlessly integrate with other solutions.

## Regulatory Requirements and Compliance

Financial institutions, and banks in particular, have a special status in the economic system. This is justified by the fact that the financial sector forms a complex network of asset cross-holdings, ownerships, investments, and transactions among financial institutions. As a consequence, a market shock that leads to the failure of one or more financial institutions can trigger a cascade of failures that might destabilize the entire financial system and cause an economic meltdown.12 The global financial crisis of 2007–2008 is the best example of such a scenario.

To avoid costly financial crises, the financial sector has been subjected to a large number of regulations, both national and international. Crucially, a significant part of financial regulatory requirements concerns the way banks should collect, store, aggregate, and report data. For example, following the financial crisis of 2007–2008, the Basel Committee on Banking Supervision noted that banks, and in particular *Global Systemically Important Banks* (G-SIBs), lacked a data infrastructure that could allow for quick aggregation of risk exposures to identify hidden risks and risk concentrations. To overcome this problem, the Basel Committee [issued a list of 13 principles on data governance and infrastructure](https://oreil.ly/dSCF7) that banks need to implement to strengthen their risk data aggregation and reporting capabilities.

Beyond banks, other financial institutions are also considered systemically important. These include *Financial Market Infrastructures* (FMIs), which facilitate the processing, clearing, settlement, and custody of payments, securities, and transactions. Examples of FMIs are stock exchanges, multilateral trading facilities, central counter parties, central securities depositories, trade repositories, payment systems, clearing, securities settlement systems, and custodians. FMIs are critical to the functioning of financial markets and the broader economy, making them subject to extensive regulation.13

Occasionally, regulators may require financial institutions to collect new types of data. For example, the European directive known as the [Markets in Financial Instruments Directive](https://oreil.ly/U-AMN), or MiFID, requires firms providing investment services to collect information regarding their clients’ financial knowledge to assess whether their level of financial literacy matches the complexity of the desired investments.

To comply with regulations, financial institutions need dedicated financial data engineering and management teams to design and implement a robust data infrastructure. This infrastructure must capture, process, and aggregate all relevant data and metadata from multiple sources while ensuring high standards of security and operational and financial resilience. It should enable risk and compliance officers to quickly and accurately access the data needed to demonstrate regulatory compliance. Financial data engineers will also be tasked with creating and enforcing a financial data governance framework that guarantees data quality and security, thereby increasing trust among management, stakeholders, and regulators. In Chapter 5, Financial Data Governance, we will explore these topics in detail.

# The Financial Data Engineer Role

The financial data engineer is at the core of everything we’ve discussed so far. Working in the financial industry can be a very rewarding and exciting career. A decade ago, the most in-demand roles in finance were analytical, such as financial engineers, quantitative analysts (or quants), and analysts. But with the digital revolution that took place with big data, the cloud, and FinTech, titles such as data engineer, data architect, data manager, and cloud architect have established themselves as primary roles within the financial industry. In this section, I will provide an overview of a financial data engineer’s role, responsibilities, and skills.

## Description of the Role

The role of a financial data engineer is in high demand, though the title, required skills, and responsibilities can vary significantly between positions. For example, the title of a financial data engineer could be any of the following:

* Financial data engineer
* Data engineer, finance
* Data engineer, fintech
* Data engineer, finance products
* Data engineer, data analytics, and financial services
* Financial applications data engineer
* Platform data engineer, financial services
* Software engineer, financial data platform
* Software engineer, financial ETL pipelines
* Data management developer, FinTech
* Data architect, finance platform

In many cases, other titles that don’t include the term “data engineering” involve, to a large extent, practices and skills related to financial data engineering. For example, the role of a machine learning engineer could involve many responsibilities concerning the creation, deployment, and maintenance of reliable analytical data pipelines for machine learning. The role of quantitative developer, common among financial institutions, often involves tasks relating to developing data pipelines, data extraction, and data transformations.

It is important to know that the role of a financial data engineer is neither a closed circle nor a professional lock-in. Even though financial domain knowledge is a major plus for financial data engineering roles, many financial institutions would accept people with data engineering experience who come from different backgrounds. Similarly, working as a financial data engineer would easily allow you to fit into other domains, given the rich variety of technical problems and challenges you might encounter in the financial industry.

## Where Do Financial Data Engineers Work?

The demand for financial data engineers primarily arises from financial institutions that generate and store data and are willing or required to invest in data-related technologies. Let’s consider a few examples.

### FinTech

FinTech firms are technology oriented and data driven; therefore, they are one of the best places to work as a financial data engineer. One of the main advantages of working for a FinTech is that you get to witness the entire lifecycle of product development. This provides engineers a solid overview of how data, business, and technology are combined to make a successful product. Another advantage is that you get to contribute original ideas and solutions to major infrastructural and software problems (e.g., choosing a database or finding a financial data vendor).