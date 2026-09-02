### Probabilistic linkage

When a unique identifier is missing or the data contains errors and missing values, deterministic record linkage may deliver poor results. *Probabilistic linkage*, also known as *fuzzy matching*, was developed to overcome this issue. Probabilistic methods have demonstrated superior linkage quality compared to deterministic approaches.

Probabilistic linkage takes a statistical approach to data matching by computing probability distributions and weights of the different attributes in the data. For example, assuming there are many fewer people with the surname “Bloomberg” than there are people with the surname “Smith” in any two datasets, the weight given for the agreement of values should be smaller when two records have the surname value “Smith” than when two records have the surname value “Bloomberg.” This is because it is considerably more likely that two randomly selected records will have the surname value “Smith” than it is that they will have the surname value “Bloomberg.”

To formalize these concepts, a variety of probabilistic linkage techniques have been developed.12 However, to illustrate the main idea, let’s take as an example the well-known [framework of Fellegi-Sunter (a theory of record linkage)](https://oreil.ly/7bWIA). Fellegi and Sunter proposed a decision-theoretic linkage theory that classifies a candidate comparison pair into one of three categories: link, non-link, and possible link. Pairs are analyzed independently. In their analysis, Fellegi and Sunter demonstrated that optimal matching can be achieved via a threshold-based strategy of likelihood ratios under the assumption that the attributes are independent of each other. To illustrate the main idea, let’s first define what the likelihood ratio is.

Let λ represent the agreement/disagreement pattern between two records in a given pair. Agreement can be expressed as a binary value (0 or 1) or, if needed, using more specific values. Using a binary agreement scale, if we have three attributes, then λ can be (1,1,1) if both records agree on all attributes, (1,1,0) if they agree on the first two but not the third, and so on. Let’s denote the set of all possible agreement patterns by δ. For example, our three attributes can be represented in

δ = 8 (2 × 2 × 2) agreement patterns.

Let’s assume we have two datasets we want to match, A and B. We create the product space as A ×B to obtain all possible comparison pairs (assume we don’t do indexing, for the sake of simplicity). Then, we partition the product space into two sets: matches (M) and non-matches (U).

Denote by

P ( λ ∈ δ ∣ s ∈ M ) the probability of observing the agreement pattern λ for a pair of records that are actually a match, and

P ( λ ∈ δ ∣ s ∈ U ) the probability of observing λ for a pair of records that is not a match. The likelihood ratio is then defined as:

R = P(λ∈δ∣s∈M) P(λ∈δ∣s∈U)

For example, if we consider our three attributes to be market capitalization, exchange market, and name, then the likelihood of a pair in full agreement can be written as:

R = P(agreeoncapitalization, agreeonname, agreeonexchange∣s∈M) P(agreeoncapitalization, agreeonname, agreeonexchange∣s∈U).

If they agree on all attributes but the exchange, then the likelihood is:

R = P(agreeoncapitalization, agreeonname, disagreeonexchange∣s∈M) P(agreeoncapitalization, agreeonname, disagreeonexchange∣s∈U)

The ratio R is referred to as *matching weight.* Based on likelihood ratios, Fellegi and Sunter proposed the following decision rule:

* If

R ⩾ t upper, then call the pair a link (match).

* If

R ⩽ t lower, then call the pair a non-link (non-match).

* If

t lower < R < t upper, then call the pair a potential link.

For details on how to calculate the probabilities and thresholds, I refer the reader to the seminal work of Thomas N. Herzog, Fritz J. Scheuren, and William E. Winkler, *Data Quality and Record Linkage Techniques* (Springer).

### Supervised machine learning approach

A limitation of deterministic and probabilistic approaches is that they tend to be specific to the datasets at hand and fail when there are complex relationships between the data attributes. Machine learning approaches excel in this area, as they are mainly focused on generalization and pattern recognition.

The supervised machine learning approach to record linkage trains a binary classification model to predict and classify matches in the datasets. As a supervised technique, it requires training data containing the true match status (match or non-match). Once trained on the labeled data, the model can be used to predict new matches for unlabelled data. Tree-based models,13 support vector machines,14 and deep learning15 techniques are among the most popular machine learning approaches used in ER.

Developing a supervised machine learning model for ER can be quite challenging. First, the model needs to consider the imbalanced nature of the data-matching problem, where most pairs correspond to true non-matches, while only a small fraction are true matches. Second, obtaining labeled training data can be quite challenging and time-consuming, especially for large datasets. Third, labeled data may not be available or accessible due to privacy issues. To solve this issue, a special type of ER, called privacy-preserving record linkage, has been proposed.16 Finally, an ML-based approach to ER might present interpret ability and explain ability challenges, especially when employing advanced techniques such as deep learning and boosted trees.17

## Entity Resolution Software Libraries

Entity resolution is a well-known problem with a lengthy history of development and application. Many software programs for ER have been developed by individuals and organizations. As of the time of writing this book, there are open source tools like fastLink, Dedupe, Splink, JedAI, RecordLinkage, Zingg, Ditto, and DeepMatcher. Additionally, on the commercial side, several vendors offer ER tools and solutions such as TigerGraph, Tamr, DataWalk, Senzing, Hightouch, and Quantexa.

# Summary

In this chapter, you learned about two primary challenges commonly encountered by financial institutions: named entity recognition (NER) and entity resolution (ER). NER entails extracting and identifying financial entities from both structured and unstructured financial datasets. Conversely, ER focuses on the critical task of matching data pertaining to the same entity across multiple financial datasets.

The landscape of challenges and solutions in financial NER and ER is dynamic, evolving alongside data, technologies, and changing market requirements. To excel at these tasks and gain a competitive edge, it’s essential that you stay current with the latest updates, methodologies, technologies, and industry best practices around financial NER and ER. Consider exploring machine learning techniques and natural language processing tools, and enrich your financial domain knowledge to enhance the accuracy and efficiency of your NER and ER systems.

Looking ahead, the next chapter will present and discuss the critical problem of financial data governance, exploring concepts and best practices for ensuring data quality, integrity, security, and privacy in the financial domain.

1 [Ashitha Shivaprasad and Sherin Elizabeth Varghese, “Gold Climbs Over 1% After Fed Signals End of Rate Hikes”](https://oreil.ly/isQBl), Reuters (December 2023).

2 Have a look at the confusion matrix [Wikipedia page](https://oreil.ly/IUCXZ) for more details.

3 For a detailed discussion on how to design features for NER, see Lev Ratinov and Dan Roth’s article, [“Design Challenges and Misconceptions in Named Entity Recognition”](https://oreil.ly/FBOOo), in *Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL-2009)*: 147–155, and Rahul Sharnagat’s [“Named Entity Recognition: A Literature Survey”](https://oreil.ly/gXgGK), *Center For Indian Language Technology* (June 2014): 1–27.

4 To learn more about context aggregation, see the method proposed in Hai Leong Chieu and Hwee Tou Ng’s [“Named Entity Recognition with a Maximum Entropy Approach”](https://oreil.ly/rqs0C), in *Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL 2003*: 160–163.

5 To learn more about this advanced technique, see Radu Florian, Abe Ittycheriah, Hongyan Jing, and Tong Zhang’s [“Named Entity Recognition Through Classifier Combination”](https://oreil.ly/BWMFm), in *Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL* 2003: 168–171.

6 For a good survey of the use of deep learning in NER, see Jing Li, Aixin Sun, Jianglei Han, and Chenliang Li’s [“A Survey on Deep Learning for Named Entity Recognition”](https://oreil.ly/vCBtQ), *IEEE Transactions on Knowledge and Data Engineering* 34, no. 1 (January 2020): 50–70.

7 A good read on the use of Transformers for NER is offered by Cedric Lothritz, Kevin Allix, Lisa Veiber, Jacques Klein, and Tegawendé François D. Assise Bissyande in [“Evaluating Pretrained Transformer-Based Models on the Task of Fine-Grained Named Entity Recognition”](https://oreil.ly/MHueQ), in *Proceedings of the 28th International Conference on Computational Linguistics* (2020): 3750–3760.

8 One thing to keep in mind is that AutoML may be too generic to deal with the peculiarities of NER. For more on this issue, see Matteo Paganelli, Francesco Del Buono, Marco Pevarello, Francesco Guerra, and Maurizio Vincini’s [“Automated Machine Learning for Entity Matching Tasks”](https://oreil.ly/Slvk4), in the *Proceedings of the 24th International Conference on Extending Database Technology (EDBT 2021),* Nicosia, Cyprus, March 23–26, 2021: 325–330.

9 For a good read on this topic, please see Erhard Rahm and Hong Hai Do’s article, [“Data Cleaning: Problems and Current Approaches”](https://oreil.ly/F8Ilg), *IEEE Data Eng. Bull*. 23, no. 4 (December 2000): 3–13.

10 For more on this topic, refer to Mikhail Bilenko, Beena Kamath, and Raymond J. Mooney’s [“Adaptive Blocking: Learning to Scale Up Record Linkage”](https://oreil.ly/SagB_), in the *Sixth International Conference on Data Mining (ICDM’06)* (IEEE, 2006): 87–96.

11 The LCS implementation used to compute the similarities is the Python SequenceMatcher class in the [difflib package](https://oreil.ly/bEfgs).

12 For an overview on this topic, have a look at Olivier Binette and Rebecca C. Steorts’ [“(Almost) All of Entity Resolution”](https://oreil.ly/_1fbt), *Science Advances* 8, no. 12 (March 2022): eabi8021.

13 A good example is Kunho Kim and C. Lee Giles’ [“Financial Entity Record Linkage with Random Forests”](https://oreil.ly/7GWUI), in *Proceedings of the Second International Workshop on Data Science for Macro-Modeling* (June 2016): 1–2.

14 A good example is Peter Christen’s [“Automatic Record Linkage Using Seeded Nearest Neighbour and Support Vector Machine Classification”](https://oreil.ly/Xy4_8), in *Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (August 2008): 151–159.

15 A good read on deep learning for ER is Nihel Kooli, Robin Allesiardo, and Erwan Pigneul’s [“Deep Learning Based Approach for Entity Resolution in Databases”](https://oreil.ly/-wlbG), in *Asian Conference on Intelligent Information and Database Systems (ACIIDS 2018*), Lecture Notes in Computer Science, vol. 10752 (Springer, 2018): 3–12.

16 For a good overview on this topic, I recommend Aris Gkoulalas-Divanis, Dinusha Vatsalan, Dimitrios Karapiperis, and Murat Kantarcioglu’s [“Modern Privacy-Preserving Record Linkage Techniques: An Overview”](https://oreil.ly/AGFbg), *IEEE Transactions on Information Forensics and Security* 16 (September 2021): 4966–4987.

17 Some effort has been made in this direction, for example Amr Ebaid, Saravanan Thirumuruganathan, Walid G. Aref, Ahmed Elmagarmid, and Mourad Ouzzani’s [“Explainer: Entity Resolution Explanations”](https://oreil.ly/kge1X), in the *2019 IEEE 35th International Conference on Data Engineering (ICDE)* (IEEE, 2019): 2000–2003.

# Chapter 5. Financial Data Governance

As financial markets expand, so do the methods and use cases for how financial data is collected, stored, and used. This has generated concerns within the financial industry as well as broader governing bodies that are pushing for solid data controls, quality assurance, privacy rules, and increased security measures. As a result, data governance frameworks have emerged as a promising approach to defining and implementing rules and principles for guiding data practices within financial institutions.

This chapter will provide a practical framework for financial data governance based on three key components: data quality, data integrity, and data security and privacy. First, I’ll cover the basics of financial data governance. Then, I’ll go into depth about each of the three components in the sections that follow.

# Financial Data Governance

Data governance is critical to securing financial data, ensuring regulatory compliance, and fostering trust among stakeholders. By implementing robust data governance practices, financial institutions can safeguard sensitive information, adhere to legal requirements, and maintain the integrity of their financial operations.

## Financial Data Governance Defined

Before defining what financial data governance is, let’s examine a few existing definitions. For example:

> Data governance is everything you do to ensure data is secure, private, accurate, available, and usable. It includes the actions people must take, the processes they must follow, and the technology that supports them throughout the data life cycle.
>
> [Google Cloud](https://oreil.ly/NUcA2)
>
> Data governance is, first and foremost, a data management function to ensure the quality, integrity, security, and usability of the data collected by an organization.
>
> [Eryurek et al., *Data Governance: The Definitive Guide* (O’Reilly, 2021)](https://oreil.ly/os5mM)

As you can see, data governance can be considered a data management function, a process, or simply a set of technological and cultural practices. Interestingly, all the above definitions share a common purpose, that of ensuring data quality, security, integrity, availability, and usability. Building on these ingredients, I define financial data governance as follows:

> Financial data governance is a technical and cultural framework that establishes a set of rules, roles, practices, controls, and implementation guidelines to ensure the quality, integrity, security, and privacy of financial data in compliance with both general and financial domain–specific internal and external policies, standards, requirements, and regulations.

There isn’t a one-size-fits-all solution for financial data governance frameworks. Two financial institutions may follow the same set of principles to establish financial data governance; however, the final implementations are very likely to be unique to each institution. The reason has to do with the nature of the issues that different financial institutions might face in terms of data quality, security, privacy, integrity, and more. It also depends on the financial institution’s internal organizational structure, culture, process standardization and harmonization, senior management support, and participation.

## Financial Data Governance Justified

Defining and enforcing an effective financial data governance framework requires a nonnegligible investment. On the one hand, a concrete and functional data governance framework needs to be defined, implemented, and integrated within the financial institution’s data infrastructure. On the other hand, employees and data users need to be trained and prepared to adhere to the established data governance principles in their daily work. As such, it is important to first understand the value proposition of a financial data governance framework for your institution.

Importantly, financial organizations are among those that require and benefit from data governance the most. This can be explained by two main factors: performance and risk management.

Financial data governance impacts performance in several ways. First, data governance drives high data quality standards, which is a major input to most financial operations and decisions. Brian Buzzelli [attributes *operational inefficiency* (inefficient use of input to produce output) in the financial industry to poor data quality](https://oreil.ly/x6-md). It impacts financial institutions’ ability to conduct business efficiently, gain insights into market activity, make informed investment decisions, respond on time to new events, and communicate accurate figures to stakeholders. Second, financial data governance saves employees the nuisance of constantly checking and rechecking data quality, integrity, privacy, and security. Third, with solid data governance principles in place, developers and business teams feel more confident in the quality and compliance of their applications and products.

Another critical reason for implementing data governance in financial institutions is to effectively manage risks associated with data, which can have significant implications for these institutions. Such risks include the following:

* Cyberattacks intended to steal data, damage organizational resources, or interfere with the operation of confidential systems
* Data breaches where sensitive data falls into the hands of unauthorized persons or organizations
* Discriminatory biases built into financial applications
* Erratic data injected in models that distorts the results
* Data loss due to lack of backups, snapshots, or archives
* Absence of firm-level risk oversight due to decentralized data processes
* Lack of visibility into the data processing steps
* Privacy risks when sharing data with third parties
* Impact on model prediction quality due to bad data
* Financial and reputational risks due to nonconformance with legal and regulatory requirements

Regulators around the world have put forth substantial efforts toward creating and enforcing laws and regulations that address the above risks. Some examples are listed here:

* Sarbanes–Oxley Act
* Bank Secrecy Act
* Basel Committee on Banking Supervision’s standard number 239 (BCBS 239)
* European Union’s (EU’s) Solvency II Directive
* California Consumer Privacy Act (CCPA)
* EU’s General Data Protection Regulation (GDPR)

In order to adhere to these regulations, financial institutions must now establish and implement robust data governance frameworks. Consequently, compliance has emerged as the primary driver for the adoption of data governance within the financial sector.

The topic of data governance is quite vast and can be complex to navigate. Practitioners, researchers, financial institutions, and consulting firms regularly publish data governance studies and guidelines. In this chapter, I will present a practical data governance framework centered on three major areas that are common to all financial institutions: data quality, data integrity, and data security and privacy.

# Data Quality

Data quality measures how well a dataset satisfies its intended use in various operational and analytical applications. For financial institutions, data has a primary role as input in the decision-making and product development process. Consequently, the problem of financial data quality needs to be handled with care by financial data engineers, analysts, and machine learning experts. Some use the term *data downtime* to refer to periods during which data is not accessible or is unusable due to quality-related issues. In a data-driven financial institution, prolonged or frequent data downtimes can severely impact efficiency, erode customer trust, interrupt research endeavors, and influence management and investment decisions.

A *Data Quality Framework* (DQF) is required to ensure financial data quality. The definition and specifications of a DQF may vary from one institution to another based on internal and external factors.1 In this chapter, I will share the main ingredients that you, as a financial data engineer, can leverage to define and build a DQF. Such ingredients are often called *data quality dimensions* (DQDs). A DQD refers to those attributes or indicators of data quality that, if measured correctly, can convey information about the overall quality of financial data.

There isn’t a fixed list of DQDs. As new requirements and data issues emerge, various DQDs can be identified and measured. Furthermore, the relevance of particular quality dimensions can vary depending on the specific problem being addressed and the needs of data consumers.2 For example, certain aspects of data quality can have a greater influence on the performance of machine learning models.3

Therefore, educating your team on defining DQDs can greatly benefit your financial institution. To establish a baseline, in the following sections, I will present nine DQDs that are particularly relevant to financial data: errors, outliers, biases, granularity, duplicates, availability and completeness, timeliness, constraints, and relevance. Note that while the needs of your organization are unique and may vary, these DQDs are fairly universal and likely to apply to your business.

## Dimension 1: Data Errors

Data errors are digital records that have been recorded erroneously, and therefore reflect invalid or incorrect values. The presence of data errors can compromise the value, accuracy, and reliability of the data and negatively impact reporting, analysis, and decision-making.

Data errors are quite common in financial data and represent the most frequent data quality issue for financial institutions. A [global survey](https://oreil.ly/xTpLA) of over 1,100 financial executives and professionals conducted by BlackLine in 2018 revealed that 55% of respondents were not completely confident in their institution’s ability to spot financial data errors before reporting results. The survey shows that 7 in 10 respondents believe that their institution made important decisions based on inaccurate or out-of-date financial data. The majority of C-level respondents agreed that there would be a negative impact if financial inaccuracies were not detected before reporting. The negative impacts included harm to the company’s image, trouble obtaining new investments, rising debt levels, penalties, and even jail time.

There isn’t a fixed list of financial data error types; rather, they materialize with the introduction of data sources, products, pipelines, and various manipulation and transformation operations. But to give a few examples, financial data errors can involve the following issues:

* Random measurement errors (e.g., $9.345 instead of $9.335)
* Wrong decimal places (e.g., a price of $111.34 instead off $11.134)
* Decimal precision (e.g., an exchange rate of 1.345 instead of 1.3458)
* Negative prices (e.g., one Apple stock is worth $-200)
* Dummy and test quotes (submitted to test latency or other technical specifications)4
* Extra or removed digits (e.g., $10000 instead of $1000)
* Invalid date (e.g., option maturity on 01-01-1345)
* Inverted exchange rates (e.g., 1 dollar equals 1.27 pounds instead of 1 pound equals 1.27 dollars)
* Rounding (e.g., price of $1.01 rounded to $1)
* Misspelled entity names (e.g., Bnk of America)
* Typos (e.g., $0900)
* Invalid formatting (e.g., 01-2022-01)

Let’s walk through an example. Suppose you want to convert one billion euros to dollars. Let’s assume that the Forex quote you are supposed to use is 1 EUR = 1.07291 USD. Using this exchange rate, the converted sum is $1,072,910,000. Now, assume that the exchange rate is slightly different due to a data error, say 1.07191. In this case, the newly converted sum is $1,071,909,999, which is $1,000,000 less! Similarly, if a decimal precision error happens, say the exchange rate is 1.072, the converted sum would be $1,072,000,000, leading to a loss of $910,000.

### Note

An important aspect to keep in mind about financial data is the nature of its correctness or trueness. While certain financial variables possess an absolute and indisputable value in specific scenarios—like the number of shares sold in a market transaction—others, such as derivative prices or Forex quotes, are subject to estimates, averages, or provider-specific values. For instance, a EUR/USD quote may differ among Forex brokers, with no universal market quote for reference. Therefore, it’s vital to assess financial data errors against the appropriate reference value.

Data errors can also significantly impact the robustness of financial analysis. For instance, a [research article from the *Journal of Fixed Income*](https://oreil.ly/46tEh) estimates that around 7.7% of transaction reports in the Trade Reporting and Compliance Engine (TRACE) database are erroneous records. If these errors are not considered, liquidity measurements based on this data may be skewed toward indicating a more liquid market than is the case.

To handle financial data errors, a few steps are required. In the first step, you need to identify and detect data errors. Error detection in financial data can occur at either the single-record or dataset level, with the former focusing on individual data points (e.g., an error with a single transaction) and the latter analyzing multiple records simultaneously, often producing aggregated error metrics like the error ratio (e.g., for statistical analysis purposes).

Crucially, financial data errors vary in complexity, making detection difficult at times. For example, a computer algorithm can easily detect an intraday price jump from $100 to $0.100. However, a more subtle error might require a more in-depth investigation, such as an intraday price of $50, followed by three prices of $40 and then a fifth price of $50. For simple errors, rule-based approaches are often used (e.g., if the price is negative → error). For more complex errors, statistical and data mining techniques have been traditionally employed, such as Pearson correlation, z-score, percentile analysis, and Mahalanobis distance.5 A more advanced technique involves the computation of the value of the erroneous record using theoretical or quantitative models such as financial asset pricing.

Once detected, errors need to be checked against business-defined tolerance and impact levels. A tolerance level can be something like an error ratio < 0.01%. Once the error is checked against the tolerance ratio, the next action depends on its business priority. An error with a Forex exchange rate may significantly impact the business if it converts large sums of money and, therefore, it needs to be given high priority.

A challenging situation arises when the data containing errors comes from a third party and is not produced by the final data consumer. In this case, detecting and correcting the errors might be difficult as there is no valid ground truth to compare the data against. When this happens, a useful approach is cross-dataset validation, which consists of comparing data from one source against an alternative data source that records similar but high-quality data. In a [research article from the *Journal of Finance*](https://oreil.ly/eW2ec), the authors analyzed error rates in CRSP (a stock price dataset) and Compustat (a company fundamentals dataset) and found that errors happen with a very low frequency, but the impact of existing errors is substantial. In the same paper, the authors suggest that their methodology could be generalized as a means of data quality assessment for competing databases.

## Dimension 2: Data Outliers

In basic terms, a data outlier is a data observation that differs significantly from the others. For example, consider a stock price time series with 100 observations, 99 of which have a value than 1000, but one record has a value of 1,000,000. It is typical to refer to this last observation as an outlier. The presence of outliers in financial data may adversely affect the robustness of statistical analysis and bias machine learning models.

Outliers within financial data might arise due to various factors. In market and transaction time series, outliers commonly result from the inherent high noise level in the data. Additionally, outliers may signal fraudulent or anomalous financial activities like money laundering and credit card fraud. Furthermore, some records may seem like outliers due to systematic issues (e.g., data transmission errors), structural breaks (sudden shifts in market conditions), poorly formatted or unadjusted data, or measurement errors (e.g., errors in price quoting).

To identify financial data outliers, researchers have proposed several methods. Some use statistical techniques such as principal component analysis, z-score, percentile analysis, and kurtosis, while others use machine learning techniques such as clustering, classification, and anomaly detection.6 Keep in mind that financial outlier detection might be a challenging task whose difficulty depends on the type and structure of the data. For example, outliers in financial time series data are different in terms of detection and treatment than in cross-section data.7

Once detected, outliers need to be treated following a specific method. The most common outlier treatment methods among financial researchers are *winsorization* and *trimming*. Trimming is the simplest approach, which works by removing outliers from the dataset. The main challenge with trimming is that if you trim too much, you risk altering the statistical properties or coverage of the dataset, while if you trim too little, you might still end up with an unstable and noisy dataset.8

Winsorization, on the other hand, involves limiting extreme values in the data to a specified percentile. In a 90% winsorization, for instance, all observations above the 95th percentile are set to equal the value of the 95th percentile, and all observations below the 5th percentile are set to equal the value of the 5th percentile.9

Another popular and reliable technique is *scaling*. This can be performed by taking a dataset’s logarithm or square root value. Scaling helps to normalize the data distribution and reduce the impact of extreme values. For instance, consider a dataset containing stock prices where some stocks have significantly higher prices than others. By applying logarithmic scaling to the stock prices, the dataset’s range can be compressed, making it easier to compare and analyze percentage changes or returns across different stocks. This normalization step helps in recognizing trends and patterns without being heavily impacted by the extreme values of high-priced stocks.

Another technique involves trimmed estimators, which are statistical measures created by excluding a portion of the extreme values from the dataset through truncation. For instance, the 5% trimmed mean is computed by averaging the values within the 5% to 95% range, removing the lowest and highest 5% of the data.