### Anonymization strategy

Interestingly, if you check any reference about data anonymization, you will notice that there exists a large discrepancy in the presentation and categorization of data anonymization techniques. Consequently, to establish a baseline, I will initially outline the key factors to consider when devising or choosing a data anonymization approach.

The first element of an anonymization strategy is the *identifiability spectrum*. At one end of the identifiability spectrum, data is completely identifiable. One way to achieve full identifiability is via *direct identifiers*, which refer to values in a dataset that can directly identify a data object without additional information. Examples of direct identifiers could be client name, social security number, financial security identifier, company name, and credit card number. For example, if you know that the ISIN of a company is US5949181045, then you can easily find out that this is Microsoft Corporation. On the other hand, *indirect identifiers or quasi-identifiers* are values that, when combined with other variables in the data, can identify a data object. Examples of indirect identifiers include company domiciliation, market capitalization, price, and the name of the CEO. If your data has information about a company whose CEO in 2023 is Satya Nadella, then it is very likely that we are talking about Microsoft Corporation. Following this logic, we can place direct identifiers on one extreme of the spectrum followed by indirect identifiers. As you obscure or remove data identifiers, you anonymize the data more and more, and it becomes more difficult to identify data objects. At the other end of the spectrum, data is completely anonymized and it is not possible to distinguish one data object from another. To decide where to be on the spectrum of identifiability, you need to consider the risks and costs of reidentification. The higher such risks and costs, the higher the threshold is on the spectrum.25

The second element of a data anonymization strategy is *analytical integrity*. Suppose that a financial institution agrees to share some of its internal data with a group of external researchers working on a specific project. To this end, the institution decides to anonymize the data. In this case, the anonymization strategy should take into account the fact that data should still be valid for analysis. For example, if the dataset encompasses certain correlations between the variables that cannot be randomly altered, then it is important to use an anonymization technique that preserves such features in the data.

*Reversibility* is the third element, which denotes the possibility of reversing the anonymization process by reidentifying the data. If the anonymization is done for data-sharing purposes, then it may not be necessary to reverse the process as it concerns a copy of the data intended for external use. However, if anonymization is done for internal purposes, e.g., credit card numbers, then it may be necessary to introduce reversibility into the anonymization strategy.

The fourth element is *simplicity*. A large number of anonymization techniques are available and they differ in their implementation complexity and interpret ability. Simple methods are easy to implement and reverse, while complex techniques require more time and effort.

Fifth, anonymization can be performed statically or dynamically. In static anonymization, data is anonymized and then stored in the final destination for safe future use. Dynamic anonymization, also called interactive anonymization, applies anonymization on the fly to the result of a query or request and not to the entire dataset. When dynamic anonymization is used, an important variable that needs to be taken into account is performance and the speed at which data gets anonymized.

Finally, anonymization can be applied in a deterministic or nondeterministic way. In deterministic anonymization, the outcome of anonymization is always the same even if repeated multiple times. For example, if the name John Smith gets replaced by XXYREQ12, then repeating the process again would replace John Smith with XXYREQ12. In a nondeterministic anonymization, this is not a requirement. For example, the name John Smith can be replaced by a randomly generated string that can change every time you implement the anonymization.

### Tip

Data anonymization is an investment that requires effort, expertise, and integration into your financial data infrastructure. For efficiency reasons, I recommend that you first classify your data based on its sensitivity/confidentiality (e.g., Class A is public data, Class B is for internal use, Class G is strictly confidential, etc.) and then anonymize just the most critical data classes.

### Anonymization techniques

After outlining your anonymization needs, you can employ a range of techniques for implementation. But before moving forward, it’s important to differentiate between an anonymization technique and a measure of its effectiveness.

An anonymization technique takes a raw dataset as input and returns an anonymized dataset as output. An anonymization effectiveness measure evaluates the level of anonymity of an anonymized dataset. Examples of anonymization effectiveness techniques include *k-anonymity*, *l-diversity*, and *t-closeness.* To illustrate the idea, *k*-anonymity, for example, checks whether the information for each data object contained in the dataset cannot be distinguished from at least *k* – 1 data objects whose information also appears in the dataset.26

The rest of this section will focus on five common anonymization techniques: generalization, suppression, distortion, swapping, and masking. To illustrate each of these, let’s take an initial data sample ([Table 5-1](#ch05_table_1_1724776830959628)) and see how each technique applies to it.

### Tip

You can always implement your own anonymization technique. However, before crafting your own solution, you should first consider the available solutions and their use cases. Data anonymization is a major field of study, and you are very likely going to find what you need in the literature.

Table 5-1. Original data before anonymization

| ID     | Company name                 | CEO           | Headquarters | Revenues | Market capitalization |
| ------ | ---------------------------- | ------------- | ------------ | -------- | --------------------- |
| XYA12F | Standard Steel Corporation   | John Smith    | New York     | $45 mln  | $400 mln              |
| BFG76D | Northwest Bank               | Lesly Charles | Las Vegas    | $5.5 bln | $50 bln               |
| M47GK  | General Bicycles Corporation | Mary Jackson  | Chicago      | $650 mln | $10 bln               |

Using the generalization technique involves substituting values with less specific yet consistent alternatives. For example, instead of indicating the exact numbers for revenues and market capitalization, we can use ranges. [Table 5-2](#ch05_table_2_1724776830959664) illustrates the outcome of this generalization strategy.

Table 5-2. Anonymized data after generalization

| ID     | Company name                 | CEO           | Headquarters | Revenues   | Market capitalization |
| ------ | ---------------------------- | ------------- | ------------ | ---------- | --------------------- |
| XYA12F | Standard Steel Corporation   | John Smith    | New York     | $0–100 mln | $0–1 bln              |
| BFG76D | Northwest Bank               | Lesly Charles | Las Vegas    | $5–10 bln  | $0–100 bln            |
| M47GK  | General Bicycles Corporation | Mary Jackson  | Chicago      | $0–1 bln   | $0–50 bln             |

Another technique is *suppression*, which simply removes or drops an entire field from a dataset. For example, in our data sample, we may want to suppress the direct identifiers ID and company name by replacing all values with \*\*\*\*\*\*\*\*. [Table 5-3](#ch05_table_3_1724776830959688) illustrates the outcome of suppression.

Table 5-3. Anonymized data after suppression

ID Company name CEO Headquarters Revenues Market capitalization \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* John Smith New York $45 mln $400 mln \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* Lesly Charles Las Vegas $5.5 bln $50 bln \*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\* Mary Jackson Chicago $650 mln $10 bln

Another effective technique is *distortion*, which applies mostly to numerical fields and works by adding a certain noise to the values to alter their true value. For example, one can simply generate a random number from a given probability distribution and add it to the value of each record in the column. A large number of formulas can be used for distortion. For illustrative purposes, let’s assume that we want to alter the values for revenues by multiplying each number by 1.1, and market capitalization by 1.3. The outcome of this anonymization process is shown in [Table 5-4](#ch05_table_4_1724776830959713).

Table 5-4. Anonymized data after distortion

| ID     | Company name                 | CEO           | Headquarters | Revenues  | Market capitalization |
| ------ | ---------------------------- | ------------- | ------------ | --------- | --------------------- |
| XYA12F | Standard Steel Corporation   | John Smith    | New York     | $49.5 mln | $520 mln              |
| BFG76D | Northwest Bank               | Lesly Charles | Las Vegas    | $6.05 bln | $65 bln               |
| M47GK  | General Bicycles Corporation | Mary Jackson  | Chicago      | $715 mln  | $13 bln               |

The next technique is swapping, which works by shuffling the data within one or more fields. For example, in our original data, we could shuffle the company and CEO names as illustrated in [Table 5-5](#ch05_table_5_1724776830959730).

Table 5-5. Anonymized data after swapping

| ID     | Company name                 | CEO           | Headquarters | Revenues | Market capitalization |
| ------ | ---------------------------- | ------------- | ------------ | -------- | --------------------- |
| XYA12F | Northwest Bank               | John Smith    | New York     | $45 mln  | $400 mln              |
| BFG76D | General Bicycles Corporation | Lesly Charles | Las Vegas    | $5.5 bln | $50 bln               |
| M47GK  | Standard Steel Corporation   | Mary Jackson  | Chicago      | $650 mln | $10 bln               |

One of the more popular techniques is masking, which obfuscates sensitive data by using a modified version with modified characters. For example, the ID field in our data sample can be masked by keeping the first character and replacing numbers with 0 and alphabetic characters with 1, as shown in [Table 5-6](#ch05_table_6_1724776830959749).

Table 5-6. Anonymized data after masking

| ID     | Company name                 | CEO           | Headquarters | Revenues | Market capitalization |
| ------ | ---------------------------- | ------------- | ------------ | -------- | --------------------- |
| X11001 | Standard Steel Corporation   | John Smith    | New York     | $45 mln  | $400 mln              |
| B11001 | Northwest Bank               | Lesly Charles | Las Vegas    | $5.5 bln | $50 bln               |
| M0011  | General Bicycles Corporation | Mary Jackson  | Chicago      | $650 mln | $10 bln               |

In addition to these basic techniques, a variety of more advanced options are available. One prominent example is *differential privacy*, a mathematically rigorous technique that has proven to be quite reliable.27 Another special technique that has found applications in finance, and in particular financial machine learning, is [synthetic data](https://oreil.ly/UkZIy). Synthetic data is machine-generated data that mirrors the properties of original sensitive data. For example, if we are able to infer the probability distribution of a sensitive dataset (e.g., user account balance), then we can use such probability distribution to generate a synthetic sample that preserves the same statistical properties of the original dataset.

# Payment Tokenization

One of the most important applications of data anonymization in finance is payment tokenization. This is a security technique that uses cryptographic algorithms to convert sensitive payment information such as credit card and bank account data into a unique, random string of characters called a “token.” Successively, when conducting payment transactions, the token is used instead of the real payment details. If an unauthorized party gets their hands on a token, they won’t be able to do anything with it.

Within the payment industry, several participants provide tokenization services, including payment processors and third-party tokenization vendors. Some payment services providers, such as [Stripe](https://oreil.ly/4sMcX), provide tokenization-enabled payment hardware or software as part of their service. Once payment tokens are generated, they are stored and secured in a secure vault managed by the tokenization service provider.

With payment tokenization, a business only needs to store the tokens of their customers. When processing client transactions, the business can send the token to the tokenization service provider, which in turn maps the token to the original payment data securely. This technique can be quite useful for businesses that process recurring transactions such as subscriptions or store customer profile details.

Various methods can be employed to generate tokens in payment tokenization. The simplest approach is Random Number Generation (RNG), where tokens are generated using a random number generator to produce a string of numbers or alphanumeric characters. For added security, mathematical algorithms such as hashing or encryption can be employed. A technique called Format-Preserving Encryption (FPE) can be used to encrypt the card number in such a way that the resulting token retains the format of the original card number (e.g., same length and structure).

### Warning

Don’t take it for granted that anonymization is bulletproof. Always keep in mind that reidentification risks are present and can change and evolve as a result of multiple factors. For example, in 2006, Netflix launched a one-million-dollar open competition to enhance its movie recommender engine. To this end, Netflix publicly disclosed one hundred million records exposing hundreds of thousands of user ratings from 1999 to 2005. Although the released dataset contained no direct identifiers, two researchers were able to [reidentify a subset of people in the data by cross-referencing Netflix data with *IMDB.com* ratings](https://oreil.ly/k2aus).

## Data Encryption

Data encryption is a fundamental practice in information security and privacy. It involves converting data into an unreadable format, rendering it meaningless to unauthorized individuals. Essentially, encryption transforms plain-text (unencrypted) data into ciphertext (encrypted) using a cryptographic algorithm. This process utilizes an encryption key to encode the data and a decryption key to decode it back to plain text. This way, if encrypted data falls into the wrong hands, then without the decryption key, they will simply see gibberish text. However, this assumes that the decryption key is kept safe!

Data can be encrypted in different states: at rest, in transit, and in use. Data at rest refers to data residing in a storage location such as a hard disk or cloud storage. Data in transit refers to data that is being transferred from one location to another over a network. Data in use is any data that is being processed or data that is temporarily held in memory.

The field of cryptography is quite vast, and a full discussion of encryption methods and techniques is beyond the scope of this book.28 Nevertheless, to ensure the security of a financial data infrastructure, financial data engineers will benefit from having a basic understanding of the essential concepts and principles of data encryption.

An important distinction to understand is between *symmetric* and *asymmetric* encryption. In symmetric encryption, only one (symmetric) key is used to encrypt and decrypt the data. Symmetric keys are often considered more efficient to generate and faster at data encryption/decryption. However, they need to be shared and stored carefully. This might occasionally necessitate encrypting the key itself using a different encryption key, which could result in a cycle of dependency. The most popular symmetric encryption method is the Advanced Encryption Standard (AES), developed by the US National Institute of Standards and Technology (NIST). Notably, companies like Google [utilize the AES to encrypt their data at the storage level](https://oreil.ly/tHwxx).

On the other hand, *asymmetric encryption* uses a pair of keys, called public and private, to encrypt and decrypt the data. Anyone with the public key can encrypt and send data; however, only the private key can decrypt the data. Due to this double-key feature, asymmetric encryption is often considered more secure. However, asymmetric encryption could be more computationally expensive, especially for large data packets, as it relies on large encryption keys.

The most popular asymmetric encryption technique is *Rivest–Shamir–Adleman* (RSA). RSA generates the keys via a factorization operation of two prime numbers. The public RSA can be used to encrypt the data, but only the person who knows the prime numbers can decrypt the data. RSA keys can be very large (e.g., 2,048 or 4,096 bits are typical sizes), and thus their usage might have an impact on performance.

Nowadays, the use of data encryption has become a default and recommended practice both for data security and compliance purposes. This goes without saying for the financial sector. To give an example, let’s take the well-known standard, [ISO 9564—Personal Identification Number (PIN) management and security](https://oreil.ly/14uGr). ISO 9564 specifies principles and requirements for reliable and secure management of cardholder Personal Identification Numbers (PINs). PIN codes are used in many places such as automated teller machine (ATM) systems, point-of-sale (POS) terminals, and vending machines. When inserting the PIN, it needs to be transmitted to the issuer for verification. To secure PIN transmission, ISO 9564 requires that the PIN be encrypted, and specifies a list of [approved encryption algorithms](https://oreil.ly/YjxnA): Triple Data Encryption Algorithm (TDEA), RSA, and Advanced Encryption Standard (AES).

## Access Control

Access control is a data security practice that allows firms to manage access to their data and related resources. A secure access control policy defines who has access to what, what type of access privileges are assigned, and a disaster management strategy to deal with access anomalies or incidents.

The two main components of access control are *authentication* and *authorization*. Authentication is an identity verification process that checks who is making the access request. Once a user has been authenticated, authorization verifies which resources the user has access to and what access privileges they have.

Access control management is a continuous and primary function within any financial institution. The typical approach to access control involves creating and enforcing a set of guidelines and protocols to be followed when granting access and privileges, as well as a monitoring system to alert against unauthorized access or excessive rights. Although such procedures might differ from one institution to another, a number of best practices have emerged over the years. For example, a quite effective principle is that of [*least privileges*](https://oreil.ly/26NAp), which states that a user or application should be granted the minimal amount of permissions required to perform their tasks. Excess privileges can be quite dangerous and lead to consequential incidents, especially if the user is not aware of them. For example, if a new user is given access and read/write/update/delete privileges to the production database, then data is exposed to deletion or corruption risk.

Another best practice is [*multifactor authentication*](https://oreil.ly/f2TKO), which requires going through separate factors to log in—for example, logging in via email plus entering a code that is sent to a linked mobile device. Of similar importance is the practice of [access control audit logs](https://oreil.ly/YKVTN), which involves monitoring and collecting information on user activities to detect anomalous or unexpected privileges.

# Case Study: Payment Card Industry Data Security Standard

To give an empirical overview of how the financial industry formulates data security requirements and policies, let’s illustrate the widely used Payment Card Industry Data Security Standard, or for short, PCI DSS.

PCI DSS is a set of policies and procedures intended to ensure the security of payment card transactions and associated data. PCI DSS is defined by the PCI Security Standards Council (SSC). Compliance with PCI DSS is not mandatory by law or regulation. However, it is highly recommended for any institution that stores, processes, and transmits cardholder data. In some cases, such institutions might be required to comply with PCI DSS due to a contractual clause. Furthermore, businesses that demonstrate compliance with PCI DSS are more likely to be trusted in the market.

Cardholder data can be identification data such as PAN, cardholder name, expiry date, and service code, as well as authentication data such as the magnetic stripe data, card verification code (CVC), and PIN code.

To comply with PCI DSS, 12 requirements have been established, which can be grouped into 6 major goals:

* Build and maintain secure networks for conducting card transactions. The recommended approach suggests installing reliable firewalls to block and prevent unauthorized access to the network.
* Protect cardholder data. The standard recommends storing only what’s necessary for business operations. Card authentication data should never be stored. When transmitting card data over a network, it should be encrypted.
* Maintain a vulnerability management program to protect against attacks, and perform regular updates and patches of antivirus and operating systems.
* Implement strong access measures via access policies, authentication, and authorization, and ensure the physical security of data.
* Regularly monitor and test networks by tracking all access to network resources and cardholder data and testing security systems.
* Maintain an information security policy that highlights the duties and responsibilities of the personnel and the potential consequences of noncompliance.

For more details on the standard specifications, consult the PCI DSS Quick Reference Guide available on the official PCI DSS [web page](https://oreil.ly/H5RcF).

Ongoing efforts are continuously improving security within financial markets. For instance, the European Union is planning to introduce the [Digital Operational Resilience Act (DORA)](https://oreil.ly/uoEzk) to enhance the digital operational resilience of financial institutions. DORA sets requirements for ICT risk management, incident reporting, and testing to ensure firms can withstand, respond to, and recover from all types of ICT-related disruptions.

# Summary

This chapter provided an overview of financial data governance, which we can summarize as follows:

* Defining financial data governance and illustrating its critical importance within the financial domain
* Introduction to data quality, with a discussion of nine dimensions relevant to financial data
* Examination of data integrity through the lens of nine fundamental principles pertinent to financial data
* Illustration of primary security and privacy challenges and best practices affecting most financial institutions

Financial data governance can apply to any aspect of your institutions’ data infrastructure, strategy, and business operations. As you read further in this book, you will observe how the different practices and principles discussed in this chapter are employed.

Over the next five chapters, we will go through the financial data engineering lifecycle, where you will learn about the different layers you will need to implement when designing a financial data infrastructure.

1 For an overview of data quality frameworks, see Corinna Cichy and Stefan Rass’ [“An Overview of Data Quality Frameworks”](https://oreil.ly/IoVPH), *IEEE Access* 7 (2019): 24634–24648.

2 This approach of defining data quality attributes based on the needs of data consumers, rather than on theoretical findings, is brilliantly illustrated in the work of Richard Y. Wang and Diane M. Strong in their paper [“Beyond Accuracy: What Data Quality Means to Data Consumers”](https://oreil.ly/iYXyQ), *Journal of Management Information Systems* 12, no. 4, (1996): 5–33.

3 For a good read on this, see Lukas Budach, Moritz Feuerpfeil, Nina Ihde, Andrea Nathansen, Nele Noack, Hendrik Patzlaff, Felix Naumann, and Hazar Harmouch, [“The Effects of Data Quality on Machine Learning Performance”](https://oreil.ly/VP3h5), *arXiv* preprint arXiv:2207.14529 (July 2022).

4 If you want to learn more about this issue, I recommend Ramazan Gençay, Michel Dacorogna, Ulrich A. Muller, Olivier Pictet, and Richard Olsen’s *An Introduction to High-Frequency Finance* (Elsevier, 2001).

5 For a good introduction to this topic, I recommend reading Chapter 9 of Pang-Ning Tan, Michael Steinbach, Vipin Kumar, and Anuj Karpatne’s *Introduction to Data Mining*, 2nd ed. (Pearson Education, 2019).

6 For more on this topic, see Carson Kai-Sang Leung, Ruppa K. Thulasiram, and Dmitri A. Bondarenko’s [“An Efficient System for Detecting Outliers from Financial Time Series”](https://oreil.ly/6Os2f), in *Flexible and Efficient Information Handling: Proceedings of the 23rd British National Conference on Databases, BNCOD ‘06*, Belfast, Northern Ireland, UK, July 18–20, 2006. (Springer Berlin Heidelberg, 2006): 190–198.

7 For more on this topic, see Kangbok Lee, Yeasung Jeong, Sunghoon Joo, Yeo Song Yoon, Sumin Han, and Hyeoncheol Baik’s [“Outliers in Financial Time Series Data: Outliers, Margin Debt, and Economic Recession”](https://oreil.ly/Tlrdm), *Machine Learning with Applications* 10 (December 2022): 100420.

8 For a good read on this topic, see Christian T. Brownlees and Giampiero M. Gallo’s [“Financial Econometric Analysis at Ultra-High Frequency: Data Handling Concerns”](https://oreil.ly/5WgP1), *Computational Statistics & Data Analysis* 51, no. 4 (December 2006): 2232–2245.

9 For more on this topic, I highly recommend John Adams, Darren Hayunga, Sattar Mansi, David Reeb, and Vincenzo Verardi’s [“Identifying and Treating Outliers in Finance”](https://oreil.ly/cEJoe), *Financial Management* 48, no. 2 (March 2019): 345–384.

10 For more on this topic, see Sagar P. Kothari, Jay Shanken, and Richard G. Sloan’s [“Another Look at the Cross‐Section of Expected Stock Returns”](https://oreil.ly/mDCB5), *The Journal of Finance* 50, no. 1 (March 1995): 185–224.

11 For a good read, start with Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, and Aram Galstyan, [“A Survey on Bias and Fairness in Machine Learning”](https://oreil.ly/BbZkM), *ACM Computing Surveys (CSUR)* 54, no. 6 (July 2021): 1–35.

12 For more on the Lipper database, see Mila Getmansky, Andrew W. Lo, and Shauna X. Mei’s chapter, [“Sifting Through the Wreckage: Lessons from Recent Hedge-Fund Liquidations”](https://oreil.ly/waZYV), in *The World of Hedge Funds: Characteristics and Analysis*, H Gifford Fong, ed. (World Scientific Publishing Company, 2005): 7–47.

13 To test the code quickly online, you can use [OneCompiler](https://oreil.ly/Pc9d5).

14 For a good read on this topic, see Pat Langley’s [“Selection of Relevant Features in Machine Learning”](https://oreil.ly/b65da), in *Proceedings of the AAAI Fall Symposium on Relevance (1994),* vol. 184 (AAAI Press, 1994): 245–271.

15 To learn more about trading strategies and their data requirements, I recommend Eugene A. Durenard’s *Professional Automated Trading: Theory and Practice* (Wiley, 2013).

16 For an excellent treatment of data catalogs, I recommend Ole Olesen-Bagneux’s [*The Enterprise Data Catalog*](https://oreil.ly/2Xgu-) (O’Reilly, 2023).

17 For more on this topic, see Ali M. Al-Khouri’s [“Data Ownership: Who Owns “My Data?”](https://oreil.ly/H5yAJ), *International Journal of Management & Information Technology* 2, no. 1 (November 2012): 1-8.

18 For a detailed study on this topic, I recommend Marshall Van Alstyne, Erik Brynjolfsson, and Stuart Madnick’s [“Why Not One Big Database? Principles for Data Ownership”](https://oreil.ly/Hce45), *Decision Support Systems* 15, no. 4 (December 1995): 267-284.

19 For a good read on data contracts, I highly recommend the book by Andrew Jones, *Driving Data Quality with Data Contracts: A Comprehensive Guide to Building Reliable, Trusted, and Effective Data Platforms* (Packt, 2023).

20 To read more about portfolio reconciliation and the technological side of it, I recommend the ISDA’s paper, [“Portfolio Reconciliation in Practice”](https://oreil.ly/sp57g).

21 For more on payment reconciliation, see [“Payment Reconciliation 101: How It Works and Best Practices for Businesses”](https://oreil.ly/kFLb4), by Stripe.

22 For a practical introduction to GDPR, I strongly recommend Paul Voigt and Axel von dem Bussche’s *The ER General Data Protection Regulation (GDPR): A Practical Guide*, 1st ed. (Springer, 2017).

23 For a comparative study on this topic, I recommend Lorrie Faith Cranor, Kelly Idouchi, Pedro Giovanni Leon, Manya Sleeper, and Blase Ur’s [“Are They Actually Any Different? Comparing Thousands of Financial Institutions’ Privacy Practices”](https://oreil.ly/s6pSA), presented at the 12th Annual Workshop on the Economics of Information Security (WEIS 2013).

24 A key distinction to remember under GDPR is the difference between anonymization and pseudonymization. According to GDPR, anonymization refers to the process of irreversibly removing personal identifiers from data so that individuals can no longer be identified, making the data completely anonymous and not subject to GDPR. Pseudonymization, on the other hand, involves processing data in such a way that individuals cannot be identified without additional information, which is kept separately and protected. Unlike anonymized data, pseudonymized data is still considered personal data under GDPR and remains subject to its regulations, as the potential to reidentify individuals exists if the additional information is accessed.

25 For an introduction to risk-based data anonymization techniques, I highly recommend the book by Khaled El Emam and Luk Arbuckle, [*Anonymizing Health Data: Case Studies and Methods to Get You Started*](https://oreil.ly/T4yiS) (O’Reilly, 2013).

26 To learn more about these measures, I highly recommend the publication by Ninghui Li, Tiancheng Li, and Suresh Venkatasubramanian, [“t-Closeness: Privacy Beyond k-Anonymity and l-Diversity”](https://oreil.ly/_Vd92), in the *2007 IEEE 23rd International Conference on Data Engineering* (IEEE, 2006): 106-115.

27 See for example Cynthia Dwork’s [“Differential Privacy: A Survey of Results”](https://oreil.ly/IM4s1), in the *Proceedings of the 5th International Conference on the Theory and Applications of Models of Computation* (Springer, 2008): 1–19.

28 Interested readers are encouraged to read Jonathan Katz and Yehuda Lindell’s *Introduction to Modern Cryptography: Principles and Protocols* (Chapman and Hall/CRC, 2021).

# Part II. The Financial Data Engineering Lifecycle

In the first part of this book, we explored the major ideas and problems around the management of financial data, including the complexity of the financial data landscape, the diversity and nonuniversality of financial data identifiers, the problems of financial entity recognition and resolution, and financial data governance.

In the second part of this book, spanning Chapters 6 through 12, the focus shifts to the technological aspects of financial data engineering. This includes the models, tools, frameworks, software systems, hardware components, libraries, design patterns, and networking systems needed to design and implement a financial data infrastructure.

Chapter 6 will begin by introducing the financial data engineering lifecycle (FDEL), a conceptual framework that will be used to organize the many components of a financial data infrastructure into four structured layers: ingestion, storage, transformation and delivery, and monitoring. Subsequently, Chapters 7 through 10 will cover each of these layers in detail. After that, Chapter 11 will discuss the various workflow architectures that are commonly used to implement the FDEL. Chapter 12 concludes with four hands-on projects designed to familiarize you with key practices and technologies in financial data engineering.