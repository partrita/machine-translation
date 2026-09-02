### Multiple identifiers

As you learned in Chapter 3, financial markets rely on a large number of data identification systems, each developed with a specific goal, structure, and scope. As such, it is typical that different financial datasets come with different identifiers. One financial identifier is typically sufficient to identify and distinguish unique entities when working with a single dataset. However, in many cases, people need to work with multiple datasets at once. For example, financial analysts or machine learning experts might require a sample of data and features that span multiple data sources. To this end, different datasets might need to be merged via an ER system to create a comprehensive dataset for the analysis.

[Figure 4-8](#ch04_figure_8_1724776828398589) illustrates a basic ER example where two datasets with different identifiers are matched. The table on the left contains six records identified by identifier B, while the table on the right holds data for the same records but uses identifier A. ER is performed by matching identifiers A and B, as depicted by the arrows. The resulting identifier mapping is as follows: 111 maps to BBB, 333 maps to AAA, and 222 maps to CCC.

### Figure 4-8. Entity resolution in the presence of two different identifiers

![Figure 4-8. Entity resolution in the presence of two different identifiers](images/fden_0408.png)

Keep in mind that if the datasets you want to merge use the same data identifier, then the task becomes a simple database join operation, and there would be no need to develop an ER system.

### Missing identifiers

In some cases, a financial dataset may lack a proper identifier or may have an arbitrary identifier that does not match the specific one you need. For instance, data generated from nonregulated or decentralized markets, such as OTC, may not include appropriate data identifiers. A stock prices dataset might use the stock ticker as an identifier, while you may require the ISIN. Another common scenario involves agents engaged in financial activities who may intentionally obscure their identities to commit fraud. In such cases, an ER system is essential to identify entities based on the available data attributes. [Figure 4-9](#ch04_figure_9_1724776828398640) illustrates the process of ER where identifiers are assigned to an unidentified dataset. The table on the right displays multiple features without entity identifiers. Using ER, records are mapped to their corresponding identifiers, as indicated by the arrows.

### Figure 4-9. Entity resolution with unidentified data

![Figure 4-9. Entity resolution with unidentified data](images/fden_0409.png)

# Entity Resolution for Fraud Detection and Identify Verification

One of the most important applications of ER in finance is fraud detection and identity verification. ER can help identify financial records that can be linked to the same real-life person or company using features such as name, email, bank account, country code, address, phone number, etc. Additionally, ER can identify anomalous activities when criminals attempt to conceal their identity and unlawful intentions by omitting crucial information or presenting it in an inaccurate manner.

One of the most common types of financial crimes is *money laundering*, an activity that makes illegally generated money look as if it comes from a legitimate source. A variety of money laundering schemes exist, and they continue to emerge over time. A typical example involves the same individual appearing as the owner of numerous companies, some of which provide no actual service but only shift money between different ends.

In banking, it is a common practice to verify the identity of an applicant when opening a bank account or conducting a financial transaction to ensure they are who they claim to be. This process is known as *know your customer* (KYC) and is aimed at preventing a pervasive form of fraud known as *identity fraud*. ER can be used for KYC to identify potential fraudsters who use different identities, email addresses, phone numbers, and other patterns to open new bank accounts and conduct financial transactions.

### Data aggregation and integration

Information regarding various operations and activities within financial institutions is typically decentralized and scattered across multiple divisions. Data integration refers to the process of combining these multiple data sources to provide a comprehensive view of the organization. This process is highly relevant for financial institutions for purposes such as regulatory reporting and risk monitoring. In Chapter 5, you will learn more about the importance of data aggregation in the financial sector.

To facilitate data integration, an ER system would be needed to match data across the different units and divisions within a financial institution. [Figure 4-10](#ch04_figure_10_1724776828398693) provides a simple example illustrating this process. In this scenario, data originates from two divisions, 1 and 2. The data from each division is initially mapped to a common identifier before being merged into a single unified dataset.

### Figure 4-10. Entity resolution for data aggregation

![Figure 4-10. Entity resolution for data aggregation](images/fden_0410.png)

### Data deduplication

A frequent problem with financial data is the presence of duplicates, i.e., multiple records that convey the same information about an entity. Duplicate records are often encountered when using nonstandard identifiers such as person or company names, which can be recorded with multiple variations. Chapter 5 will have a dedicated section detailing the problem of financial data duplicates.

The process of identifying and removing data duplicates is called data deduplication. Since deduplication requires matching similar entities in the same dataset, it can be treated as an ER problem. [Figure 4-11](#ch04_figure_11_1724776828398744) shows an example illustrating this process. The table on the left contains two duplicate instances, (1,2) and (7,8). Using ER, it is possible to identify these duplicates and perform data deduplication, as shown in the table on the right.

### Figure 4-11. Entity resolution for data deduplication

![Figure 4-11. Entity resolution for data deduplication](images/fden_0411.png)

## How Does Entity Resolution Work?

A typical ER process involves five iterative steps, which I illustrate in [Figure 4-12](#ch04_figure_12_1724776828398793). In the first step, *preprocessing* is applied to the input datasets to ensure their high quality for the task. The second step, *blocking*, is often required to reduce computational complexity when matching large datasets. In the third step, candidate pair records are *generated* and *compared* using a selected methodology. Successively, comparisons are *classified* into matches, non-matches, or possible matches. Finally, in the fifth step, the goodness of the matching process is *evaluated*. In the next few sections, we will explore each of these five steps in detail.

### Figure 4-12. Entity resolution process

![Figure 4-12. Entity resolution process](images/fden_0412.png)

### Data preprocessing

ER is highly sensitive to the quality of the input datasets. Therefore, before starting the matching process, it is crucial that the necessary rules are established and applied for quality assessment and data standardization. Such rules are particularly important for the data fields that will be used in the matching process, especially identifier fields. [Table 4-6](#ch04_table_6_1724776828463997) illustrates an example where three datasets store data about the same financial entity using different formatting styles.

Table 4-6. Nonstandardized data representations

|           | Entity name             | Headquarter       | Market capitalization | Ex-dividend date |
| --------- | ----------------------- | ----------------- | --------------------- | ---------------- |
| Dataset 1 | JP Morgan Chase         | New York City     | $424.173B             | Jul 05, 2023     |
| Dataset 2 | JPMorgan Chase & Co.    | New York City, NY | $424,173,000,000      | 2023-07-05       |
| Dataset 3 | J.P. Morgan Chase & Co. | New York          | $424,000.173M         | 5/7/23           |

As the table shows, the three records are the same but look different as they use different formats. Keep in mind that formatting heterogeneity may occur within the same dataset.9

To guarantee optimal data-matching results, data should be standardized using a consistent formatting method. The most common approach involves rule-based techniques, which employ a set of data transformation rules such as the following:

* Remove dots from entity names (e.g., J.P. Morgan Chase & Co. → JP Morgan Chase & Co).
* Remove stop words (e.g., The Bank of America → Bank of America).
* Expand abbreviations (e.g., Corp. → Corporation).
* Remove postfixes (e.g., FinTech firm → FinTech).
* Names should appear as “Given name, Surname”.
* Convert dates to the format “YYYY/MM/DD”.
* Parse fields into smaller segments (e.g., divide a field that contains full addresses like “270 Park Avenue, New York, NY” into multiple fields for the city, state, and street).
* Infer missing fields (e.g., zip code can be inferred from the street address).
* Remove duplicate records.

### Tip

When performing data preprocessing, make sure you don’t modify the original tables. Instead, make a new copy of the data and apply the transformations to it.

### Indexing

Once the input datasets are cleaned and standardized, they should be ready for matching. In a typical scenario, the matching process will involve a comparison between each element in the first dataset with all elements in the second one. If the datasets at hand are small, then such a comparison can be done in a reasonable amount of time. However, with large datasets, the computational complexity may increase significantly. Consider a scenario where you want to match two datasets with 500k records each. If all pair-wise comparisons were to be performed, there would be a total of 500,000 × 500,000 or 250 billion candidate comparisons. Even at a processing speed of one million comparisons per second, it would still take 69 hours to match the two datasets. If both datasets have one million records each, then it will take around 11 days!

Crucially, in most ER problems, the majority of pair-wise comparisons will result in non-matches. This is because records in the first dataset often match a small subset of records in the second dataset. For this reason, it is common to observe that the number of pair-wise comparisons increases quadratically with the number of data records (i.e., O(x^2), where x approximates the number of records in the datasets to match), while the number of true matches increases linearly.10

To overcome this issue, a number of data optimization techniques have been developed. Such techniques are often referred to as *indexing*, which aims to reduce the number of pair-wise comparisons needed by generating pair records that are likely to match and filter out the rest. The most common indexing technique is called *blocking*. It works by splitting the datasets to match into a smaller number of blocks and performing pair-wise comparisons among the records within each block only. To perform the splitting, a *blocking key* needs to be defined using one or more features from the datasets. For example, a blocking key might place records in the same block if they have the same zip code or country.

Blocking presents a few challenges. First, it is highly sensitive to data quality. Small [variations in the data](https://oreil.ly/uucpQ) might lead a blocking key to place a record in the wrong block. Second, blocking might entail a [tradeoff between computational complexity and block granularity](https://oreil.ly/aYJjs). By defining a very specific blocking key, you will end up with many blocks, which is good for performance. But this comes at the risk of excluding true matches. On the other hand, using a more generic blocking key could result in a small number of blocks, which will lead to a large number of pair-wise comparisons that increase computational complexity.

[Figure 4-13](#ch04_figure_13_1724776828398849) illustrates a simple blocking process. In this example, we have two datasets, A and B, that contain company information such as the market capitalization, the headquarters’ country, and the exchange market on which the company is listed. If we were to perform all pair-wise comparisons, we would need to do 6 × 6 = 36 comparisons. However, using blocking criteria that group records in blocks based on the headquarters’ country and exchange market, we reduce the number of pair comparisons to five.

### Figure 4-13. A simple blocking process

![Figure 4-13. A simple blocking process](images/fden_0413.png)

In addition to blocking, a number of other indexing techniques have been [developed](https://oreil.ly/iV2wo). Examples include Sorted Neighborhood Indexing, Q-Gram-Based Indexing, Suffix Array-Based Indexing, Canopy Clustering, and String-Map-Based Indexing.

### Comparison

Once the candidate pairs have been generated, the next step involves the actual comparison between the records. The traditional approach to record comparison is based on pair similarity. This is often performed by aggregating all features into a single string and then comparing the string similarity between the pairs. Alternatively, comparing pair features individually by computing their similarities and combining them into a single similarity score is also possible.

Generally speaking, similarity scores are normalized to be between 0 and 1. A pair has a perfect match if its similarity score is 1, whereas a non-match is indicated by a score of 0. The comparison is called *exact matching* if it only allows for either a match or a non-match. Crucially, it is normal for similarity ratings to fall within the 0–1 range, in which case the matching is *approximate* or *fuzzy*. Approximate matching may occur due to differences in the datasets, such as the number of features (one dataset has a feature that the other does not), different formats (e.g., values reported in different currencies), information granularity (i.e., one dataset has a more granular identifier than the other), and information precision (one dataset rounds values to two decimals while the other uses three).

During the comparison phase, there are three types of matching scenarios:

One-to-one:   Each record in the first dataset can only have one match in the second dataset (e.g., matching the same financial transaction in two datasets).

One-to-many:   One record in the first dataset may have numerous matches in the second dataset (e.g., matching all transactions in one dataset associated with a specific credit card in another dataset).

Many-to-many:   Numerous records from the first dataset can be matched to multiple records from the second dataset (e.g., matching multiple transactions within a trade recorded in a broker’s database with transactions recorded by the clearing or stock exchange).

As an illustrative example, [Table 4-7](#ch04_table_7_1724776828464040) shows the similarity scores for the five candidate pairs from [Figure 4-11](#ch04_figure_11_1724776828398744). Records are first standardized (numbers expressed without decimals or multiples; all letters are uppercase), and then concatenated in a single string. Successively, the similarity is calculated between the concatenated strings using the *Longest Common Substring* (LCS) algorithm.11

Table 4-7. Illustration of record comparison

| Record pair | Pair string                                             | Similarity score |
| ----------- | ------------------------------------------------------- | ---------------- |
| (a1, b3)    | a1: “$200000000000USANYSE”  b3: “$200110000000USANYSE”  | 0.9              |
| (a3, b1)    | a4: “$55200000000UKLSE”  b1: “$552000000000PORTUGALLSE” | 0.75             |
| (a4, b2)    | a4: “$300550000000USANYSE”  b2: “$300550000000USANYSE”  | 1                |
| (a5, b6)    | a5: “$100000000FRANCELSE”  b6: “£95000000FRANCELSE”     | 0.81             |
| (a6, b4)    | a6: “$900000000JAPANCME”  b6: “$199876000JAPANNASDAQ”   | 0.51             |

In addition to the LCS algorithm, there are several other methods available for computing pair similarities. These include Jaro–Winkler approximate string comparison, Levenshtein distance, edit distance, Jaccard similarity, Q-gram distance, and more.

### Classification

Once all similarities have been computed, the next step is the classification of the candidate pairs into matching categories. In its most basic form, classification is binary: match or non-match. However, a less restrictive approach allows for three classes: match, non-match, and potential match. In either case, a match indicates a pair that refers to the same real-world entity in both datasets, while a non-match means that records in the pair refer to two different entities. A potential match is a pair of records that are likely to be a match but require a final clerical review for confirmation.

A variety of pair classification methods have been proposed, including the threshold-based approach, rule-based approach, probabilistic approach, and machine learning approach. Later in this chapter, we will discuss these models in more detail. To make a simple example, let’s use a basic threshold-based approach to classify the results of the previous step (comparison) that were reported in [Table 4-7](#ch04_table_7_1724776828464040). Let’s assume that a match has a similarity score greater than or equal to 0.9, a potential match has a score of 0.8 and above, and anything below 0.8 is a non-match. Using this approach, the outcome of the classification is illustrated in [Table 4-8](#ch04_table_8_1724776828464085).

Table 4-8. Illustration of a threshold-based pair classification

| Record pair | Similarity score | Classification  |
| ----------- | ---------------- | --------------- |
| (a1, b3)    | 0.9              | MATCH           |
| (a3, b1)    | 0.75             | NON-MATCH       |
| (a4, b2)    | 1                | MATCH           |
| (a5, b6)    | 0.81             | POTENTIAL MATCH |
| (a6, b4)    | 0.51             | NON-MATCH       |

### Evaluation

The final step in an ER process is performance evaluation. A highly performant ER system is able to find and correctly classify all valid matches in the input datasets. Additionally, it needs to ensure computational efficiency in terms of runtime, memory consumption, storage needs, and CPU usage.

In most cases, ER systems are implemented for real-world financial applications; therefore, they need to scale to large applications with millions of records. Measuring computational complexity (e.g., in terms of O() notation) is fundamentally important, even if optimization techniques such as indexing are applied. This is especially important when developing a streaming-based real-time record linkage system. In this case, complexity metrics and disk and memory usage figures can orient the implementation in terms of hardware, data infrastructure, and algorithmic optimizations. Additionally, as proposed by Elfeky et al. in their [research paper](https://oreil.ly/qz5Ld), performance can be measured in terms of the effectiveness of indexing techniques in reducing the number of record pairs to be matched (*reduction ratio*) while at the same time capturing all valid matches (*pair completeness*).

To evaluate the quality of the matching results of an ER system, a common practice is to use the binary classification quality metrics employed in machine learning and data mining, which we used for evaluating NER systems. In building such metrics, four numbers need to be calculated. *True positives* are the number of pairs correctly classified as matches, while *true negatives* are pairs correctly classified as non-matches. Similarly, *false positives* are non-matches that were mistakenly classified as matches, while *false negatives* are pairs that were classified as non-matches, but in reality, they refer to actual matches. [Figure 4-14](#ch04_figure_14_1724776828398908) shows the confusion matrix representation of these figures.

### Figure 4-14. Confusion matrix of ER

![Figure 4-14. Confusion matrix of ER](images/fden_0414.png)

Based on these four metrics, a variety of quality measures can be [calculated](https://oreil.ly/CxnpK). For example, accuracy detects the ability of the system to make a correct classification (match vs. non-match). Precision measures the ability of the system to correctly classify true matches (i.e., how good the system is at avoiding false positives). Recall is another metric that measures the ability of the system to detect all true matches (i.e., how good the system is at avoiding false negatives). The F1 score is a harmonic mean of precision and recall and is used to find a balance between recall and precision.

Let’s use our [Table 4-8](#ch04_table_8_1724776828464085) example to compute these four metrics. As illustrated in [Table 4-9](#ch04_table_9_1724776828464131), the final predictions are available in the column called “Predicted class after human review,” while the ground truth values are available in the column “Ground truth class.”

Table 4-9. Final ER classifications and their ground truth value

| Record pair | Predicted class | Predicted class after human review | Ground truth class |
| ----------- | --------------- | ---------------------------------- | ------------------ |
| (a1, b3)    | MATCH           | MATCH                              | MATCH              |
| (a3, b1)    | NON-MATCH       | NON-MATCH                          | NON-MATCH          |
| (a4, b2)    | MATCH           | MATCH                              | MATCH              |
| (a5, b6)    | POTENTIAL-MATCH | MATCH                              | MATCH              |
| (a6, b4)    | NON-MATCH       | NON-MATCH                          | MATCH              |

From the data in [Table 4-7](#ch04_table_7_1724776828464040), we can compute the confusion matrix values as follows:

* TP: 3
* TN: 1
* FP: 0
* FN: 1

Then, we can compute the four quality metrics, as illustrated in [Table 4-10](#ch04_table_10_1724776828464172).

Table 4-10. Computed quality metrics

| Quality measure | Value |
| --------------- | ----- |
| Accuracy        | 0.8   |
| Precision       | 1     |
| Recall          | 0.75  |
| F1 score        | 0.85  |

As a general performance metric, an accuracy of 0.8 is not bad, but it wouldn’t be ideal in a critical application. The precision value of 1 tells us that the model doesn’t produce false positives; if a pair is classified as a match, then it will be a match with 100% certainty. Recall tells us that the model couldn’t find all true matches and made a few false negative classifications. The F1 score of 0.85 shows an OK model performance, but one that is still not ideal for a good ER system.

## Approaches to Entity Resolution

Numerous ER techniques have been proposed in the literature and by market participants. Such techniques are often named and classified differently; therefore, I summarize them into three categories: deterministic linkage, probabilistic linkage, and machine learning. These aren’t necessarily mutually exclusive, and they can be combined to build an ER system. For example, a simple rule-based approach can be used to match high-quality records, while a probabilistic or machine learning approach is used for records with poor data quality. In the following sections, I will illustrate each approach in some detail.

### Deterministic linkage

The simplest ER technique, known as deterministic linkage, performs data matching via a set of deterministic rules based on the available data fields. Various deterministic linkage methods have been proposed, including link tables, exact matching, and rule-based matching, which I’ll cover next.

## Link tables

A link table contains a mapping between two or more data identifiers. If two datasets use different identifiers mapped in a link table, then the datasets can be matched via an SQL join operation between them and the link table. [Figure 4-15](#ch04_figure_15_1724776828398970) illustrates this approach.

For financial applications, link tables need to be built with a *point-in-time* feature to keep track of the possibility that identifiers might change, get reassigned, or become inactive. To this end, a good financial link table would include additional information such as the start and end date of the link, the link status, and any additional comments. For example, [Table 4-11](#ch04_table_11_1724776828464213) illustrates a link table that contains three links, where only one link (a1, b55) is active and has no end date, while link (a4, a20) ended in 31-12-2007 as the stock got delisted, and link (199, b44) ended in 20-01-1995 because the company merged with another one.

### Figure 4-15. An ER process using a link table

![Figure 4-15. An ER process using a link table](images/fden_0415.png)

Table 4-11. Example of a link table

Identifier A Identifier B Link start date Link end date Status Comment a1 b55 01-02-1990 - Active a4 b20 20-01-2005 31-12-2007 Inactive Stock delisted a99 b44 20-01-1995 20-01-1995 Inactive Merged with another company

The main advantages of link tables are simplicity, performance, and readability. However, they might be laborious to construct and require extensive maintenance and updating.

Financial institutions might create their own link tables internally. This is where you, as a financial data engineer, will play a major role. Additionally, a variety of financial link tables are available as commercial products. This includes, for example, reference datasets that match different financial identifiers and other instrument characteristics. Another example is the famous data distributor Wharton Research Data Services (WRDS), which has created its own [linking suite](https://oreil.ly/8QLGK) to enable users to link tables between the most popular databases on the WRDS platform.

Another notable example involves the series of initiatives [established](https://oreil.ly/Nseut) by the Global Legal Entity Identifier Foundation (GLEIF) in partnership with market participants to link the LEI with other financial identifiers. The result includes a list of open source link tables, such as the BIC-to-LEI, ISIN-to-LEI, and MIC-to-LEI mappings.

# Case Study: CRSP/Compustat Merged Link Table

One of the most common use cases of entity resolution in finance is merging stock price data with company fundamentals data. If you have ever checked a financial news website, you will notice that data about stock close/open prices, bid/ask prices, and volume are available, together with fundamental data such as market capitalization and dividend distributions. This is done by matching data across price and fundamental datasets for the same entity.

A good example of a price/fundamentals ER system is the [CRSP/Compustat Merged Database (CCM)](https://oreil.ly/zXBdq). The CCM database is a link table that matches historical events and market data from the CRSP database with company fundamentals data from S&P’s Compustat database (both discussed in Chapter 2). As described by the vendor [documentation](https://oreil.ly/SpJtG), the identifiers used in creating the link table are the following:

GVKEY:   Compustat’s company identifier.

ID:   Compustat’s issue identifier. One GVKEY may be associated with multiple GVKEYs.

PRIMISS:   Compustat’s primary security identifier.

PERMCO:   CRSP’s company identifier.

PERMNO:   CRSP’s issue identifier. One PERMCO may be associated with multiple PERMNOs.

The resulting link table matches all security identifiers with information on the link start date, link end date, CRSP identifiers, and Compustat identifiers.

## Exact matching

In exact matching, records in two datasets are linked via a common unique identifier or via a [linkage key](https://oreil.ly/RcS2R) that combines a set of data attributes into a single matching key. If a common unique identifier is available in both datasets, then the matching process becomes a simple SQL join operation on the unique key. The issue here is that financial datasets often use different identifiers. Additionally, an identifier may exist only from a certain point in time, and old records might lack identification. The same procedure can be followed with a linkage key, but instead of a unique identifier, a linkage key is constructed to merge the datasets. For linkage keys to provide good results, data must be of high quality (complete, standardized, deduplicated, and without errors).

## Rule-based matching

A less restrictive approach to deterministic linking is the rule-based approach, where a set of rules is established to determine whether a pair of records constitutes a match. The primary benefits of this approach include the flexibility to define and incorporate rules, speed, interpret ability, and simplicity. On the negative side, defining the rules may require considerable time and dataset-related domain knowledge. Moreover, as the datasets increase in complexity and vary in quality, you might end up with a large number of rules that can impact maintainability and performance.

A simple rule-based approach involves computing the similarity between records and classifying a pair as a match if it exceeds a given threshold (e.g., if the similarity is > 0.8, then it’s classified as a match; otherwise, it’s a non-match). This method offers a good alternative to exact matching as it accommodates minor variations in the data attributes.