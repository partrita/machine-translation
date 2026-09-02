### Entity categorization

Once all candidate entities in the text have been extracted, the next step is to accurately map each valid entity to its corresponding entity type. For example, “Bank of America” should be classified as a company (COMP), “United States” as a country (LOC), “Bill Gates” as a person (PER), and any other token should be labeled as “O” to indicate that it is not a relevant entity.

The main challenge in this step is language ambiguity. For example, the words *bear* and *bull* are frequently used to indicate two species of animals. However, in financial markets, the word bull is often used to indicate an upward trend in the market, while bear describes a receding market.

Another example involves similar names that could refer to different entities. For instance, “JP Morgan” might describe the well-known financial institution JPMorgan Chase, but it could also refer to John Pierpont Morgan, the American financier who founded J.P. Morgan Bank.

To illustrate the NER process up to this step, we should be able to take a text such as…

> Gold prices rose more than 1% on Wednesday after the U.S. Federal Reserve flagged an end to its interest rate hike cycle and indicated possible rate cuts next year.1

…and produce a structured categorization, as illustrated in [Table 4-4](#ch04_table_4_1724776828463910). In this example, five types of entities were extracted: commodity (CMDTY), variable (VAR), nationality (NAL), organization (ORG), and miscellaneous (O).

Table 4-4. Outcome of entity extraction and categorization of a news title

| entity\_type | text                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------ |
| CMDTY        | Gold                                                                                       |
| VAR          | Prices                                                                                     |
| NAL          | U.S.                                                                                       |
| ORG          | Federal Reserve                                                                            |
| O            | rose more than 1% on Wednesday after the                                                   |
| O            | flagged an end to its interest rate hike cycle and indicated possible rate cuts next year. |

### Entity disambiguation

If you aim to extend beyond merely extracting entities, which is crucial in numerous financial applications, you must proceed to disambiguate the identified and validated entities. This involves establishing a link between each correctly recognized entity in the data and its unique real-world counterpart.

The entity disambiguation step can present some challenges. One major issue is name variations. For example, a company can be mentioned in multiple ways, such as Bank of America, Bank of America Corporation, BoA, or BofA. Entity ambiguity is another challenge. For example, Bloomberg can refer to the company Bloomberg L.P. or its CEO, Michael Bloomberg. Finally, the knowledge bases used to disambiguate the entities might not always contain up-to-date information on all specific or novel entities that emerge in the market.

If we take our example, illustrated in [Table 4-4](#ch04_table_4_1724776828463910), adding entity disambiguation would result in real-world references, as illustrated in [Table 4-5](#ch04_table_5_1724776828463957). This example is illustrative, and more precise references could be used. For instance, the spot and future prices could be linked to a specific commodity exchange such as CME.

Table 4-5. Outcome of an entity extraction, categorization, and disambiguation of a news title

| entity\_type | text                                                                                       | reference                                          |
| ------------ | ------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| CMDTY        | Gold                                                                                       | Chemical element with symbol AU                    |
| VAR          | Prices                                                                                     | Spot price and future price on commodity exchanges |
| NAL          | U.S.                                                                                       | Country in North America                           |
| ORG          | Federal Reserve                                                                            | Central Bank of the United States of America       |
| O            | rose more than 1% on Wednesday after the                                                   |                                                    |
| O            | flagged an end to its interest rate hike cycle and indicated possible rate cuts next year. |                                                    |

### Evaluation

Evaluating the performance of NER systems in terms of their accuracy and efficiency is the last step in NER. An accurate NER system should detect and recognize all valid entities, correctly assign them to the appropriate entity types, and optionally link them to their real-world counterparts. Besides analytical performance, NER systems must also be assessed based on their computational efficiency, which includes runtime, memory consumption, storage requirements, CPU usage, and scalability to handle large-scale financial applications with millions of records.

To compute performance metrics for an NER system, four kinds of results are needed:

False positive (FP):   An instance incorrectly identified as an entity by the NER system

False negative (FN):   An instance that the NER system fails to classify as an entity, even though it is an actual entity in the ground truth

True positive (TP):   An instance correctly identified as an entity by the NER system

True negative (TN):   An instance correctly identified as a nonentity, consistent with the ground truth

These four values are often represented in a special tabular format known as a *confusion matrix*, as illustrated in [Figure 4-5](#ch04_figure_5_1724776828398439).

### Figure 4-5. Confusion matrix of NER

![Figure 4-5. Confusion matrix of NER](images/fden_0405.png)

### Note

To compute the confusion matrix of a given NER model, you need to have a ground truth dataset with the actual values. The ground truth is mainly used for model training, where predicted values are compared against their true counterparts. This is usually a major challenge in NER, especially if you have big datasets. You, as a financial data engineer, will play a primary role in building and maintaining a labeled database to be used as the ground truth for NER systems.

Using the confusion matrix, the following performance evaluation metrics can be computed:

Accuracy:   Accuracy measures the overall performance of the NER model and answers the question, “Out of all the classifications that were made, how many were correct?” In NER, this can be used as a measure of the ability of the model to distinguish between what is an entity from what is not. Accuracy works well as an evaluation metric if the cost of false positives and false negatives is more or less similar. This can be represented as a formula as follows:

A c c u r a c y = TP+TN TP+TN+FP+FN

Precision:   Precision measures the proportion of true positives to the number of all positives that the model predicted. It answers the question, “Of all instances that were classified as true positives, how many are correct?” In NER, this could be interpreted as the percentage of tokens (words or sentences) that were correctly recognized as entities out of all the tokens that are actually entities. A low precision value would indicate that the model is not good at avoiding false positives. Precision is a good measure when the cost of false positives is quite high. This can be represented as a formula as follows:

P r e c i s i o n = TP FP+TP

Recall:   Recall measures the true positive rate of the model by answering the question, “Out of all instances that should be classified as true positives, how many were correctly classified as such?” Low recall indicates that the model is not good at avoiding false negatives. The recall is a good measure to use when the cost of a false negative is high. This can be represented as a formula as follows:

R e c a l l = TP TP+FN

F1 score:   The F1 score is a harmonic mean of precision and recall. It is widely used when the class representation in the data is imbalanced or when the cost of both false positives and false negatives is high. In financial NER, this is likely to be the case, as the vast majority of data tokens are not entities and the cost of mistakes is high. This can be represented as a formula as follows:

F 1 s c o r e = 2\*(Recall\*Precision) Recall+Precision

Additional evaluation metrics can be derived from the confusion matrix.2 In many research papers on NER, the F1 score is used as the default metric. However, I highly recommend that you compute all four metrics to have an overview of your NER performance from different angles. For example, a low precision might tell you that you have a rule in your model that easily classifies a token as an entity. Similarly, a low recall might tell you that your model hardly classifies an entity as such; maybe your rules are too strict.

Now that you understand the necessary steps for developing an NER system, let’s explore the main modeling approaches that can be employed to build and operationalize an NER system.

## Approaches to Named Entity Recognition

Numerous NER methods and techniques have been proposed in academic literature and by market participants. Frequently, these solutions are tailored or fine-tuned to suit particular domains. In this book, I will offer a taxonomy of seven modeling approaches: lexicon-based, rule-based, feature-engineering-based machine learning, deep learning, large language models, wikification, and knowledge graphs.

One thing to keep in mind is that these approaches aren’t necessarily mutually exclusive. In many cases, especially when building complex NER systems, developers employ a combination of techniques. In the upcoming sections, I will discuss each of the seven approaches with some level of detail.

### Lexicon/dictionary-based approach

This approach works by first constructing a lexicon or dictionary of vocabulary using external sources and then matching text tokens with entity names in the dictionary. A financial dataset, like reference or entity datasets, can function as a lexicon. Lexicons are flexible and can be tailored to any domain. For this reason, this approach could be a good choice for domain-specific tasks where the universe of entities is small or constant, or evolves slowly. Examples include sector names, financial instrument classes, and company names. Other examples might include accounting or legal texts, which rely on standard principles and formal language that doesn’t change much over time.

Lexicons serve a dual purpose in NER. They can function as the primary extraction method or complement other techniques, as I’ll illustrate later. Furthermore, a lexicon can be used for entity disambiguation. For example, a lexicon mapping company names to their identities can handle both recognition and disambiguation tasks.

The main advantages of lexicons are processing speed and simplicity. If you have a lexicon, then the extraction process can be viewed as a simple dictionary lookup. Keep in mind, however, that lexicons cannot recognize new entities that are not in the dictionary (e.g., new types of financial instruments). Additionally, lexicons are highly sensitive to the quality of data preprocessing and the presence of errors. As they cannot deal with exceptions or erratic data types, lexicons tend to guarantee better performance on high-quality data. Finally, lexicons might produce false positives if the context is not taken into account. For example, a stock ticker lexicon might contain the symbol AAPL for Apple, Inc. However, the abbreviation AAPL may also refer to “American Association of Professional Landmen” or “American Academy of Psychiatry and the Law.”

### Rule-based approach

The rule-based approach employs a set of rules, created either manually or automatically, to recognize the presence of an entity in text. For example:

* *Rule N.1:* the number after currency symbols is a monetary value, e.g., $200.
* *Rule N.2:* the word after Mrs. or Mr. is a person’s name.
* *Rule N.3:* the word before a company suffix is a company name, e.g., Inc., Ltd., Inc., Incorporated, Corporation, etc.
* *Rule N.4:* alphanumeric strings could be security identifiers if they match the length of the identifier and can be validated with a check-digit method.

Similar to the lexicon approach, rule-based methods tend to be domain-specific, making their transfer ability to other domains challenging. They are also particularly sensitive to data preprocessing issues, exceptions, and textual ambiguity, which can result in an large set of rules. Complex rule-based approaches are difficult to maintain, hard to understand, and can be slow to run. Therefore, they are recommended in cases where the language is either simple or subject to formal standards, such as accounting, annual reports, or SEC filings.

### Feature-engineering machine learning approach

Lexicon- and rule-based methods commonly face challenges when complex data patterns need to be identified for accurate NER. In such cases, modeling presents a compelling alternative. One prominent method involves feature-engineering machine learning, wherein a multiclass classification model is trained to predict and categorize words in a text. Being supervised, this approach requires the existence of labeled data for training.

To apply supervised machine learning, the modeler must select, and in most cases engineer, a set of features for each token.3 To give a few examples, features can be something like the following:

* Part-of-speech tagging (noun, verb, auxiliary, etc.)
* The word type (all-capitalized, all-digits, alphanumeric, etc.)
* Whether it’s a courtesy title (Mr., Ms., Miss, etc.)
* The word match from a lexicon or gazetteer (e.g., San Francisco: City in California)
* Whether the previous word is a courtesy title
* Whether the word is a currency symbol ( ¥, $, etc.)
* Whether the previous word is a currency symbol
* Whether the word is at the beginning or end of the paragraph
* Context aggregation features that capture the surrounding context of a word (e.g., the previous and subsequent *n* words)4
* Prediction of another ML classifier5

Once all relevant features have been carefully engineered, a variety of algorithms can be used. Among the most popular choices are logistic regression, Random Forests, Conditional Random Fields, Hidden Markov Models, support vector machines, and Maximum Entropy Models.

Feature-based models offer several advantages, such as speed of training and feature interpret ability. However, several challenges might arise, such as the need for financial domain expertise, the complexity of feature engineering, difficulty modeling nonlinear patterns, and the inability to capture complex contexts for longer sentences. This is where more advanced machine learning techniques, such as deep learning, come into play, which I will introduce next.

### Deep learning approach

In recent years, deep learning (DL) has established itself as the state-of-the-art approach for NER.6 DL is a prominent subfield of machine learning that works by learning a hierarchical representation of data via a neural network composed of multiple layers and a set of activation functions. A neural network can be thought of as a computational graph where each layer of nodes performs nonlinear function compositions of simpler functions produced at the previous layer. Interestingly, this process of repeated composition of functions has significant modeling power, which has contributed to the success of deep learning in solving complex problems.

There are several advantages to applying DL to NER. First, the modeler doesn’t need to worry about the complexities involved in feature engineering, as deep neural networks are capable of learning and extracting features automatically. Second, DL can model a large number of complex and nonlinear patterns in the data. Third, neural networks can capture long-range correlations and context dependencies in the text. Fourth, DL offers high flexibility through network specifications (depth, width, layers, hyper parameters, etc.), which allows the modeling of a large number of domain-specific problems on large datasets.

A wide variety of network structures exist within the DL field. The ones that have shown remarkable success in NER-related tasks are Recurrent Neural Networks and their variants, such as Long Short-Term Memory, Bidirectional Long Short-Term Memory, and, most recently, attention mechanism-based models, such as Transformers.7

Deep learning is a powerful and advanced technique. However, I advise against using it by default for your NER task. DL models are hard to interpret and may require special hardware (e.g., a graphics processing unit, or GPU) and time to train. Try a simple approach first. If it doesn’t work, then use more complex techniques.

Given the remarkable performance of complex models like DL in text-related tasks, development has extended to even more sophisticated models, such as large language models (LLMs), which I’ll explore next.

### Large language models

A large language model (LLM) is an advanced type of generative artificial intelligence model designed to learn and generate human-like text. Most LLMs leverage a deep learning architecture known as a Transformer, proposed in the seminal paper [“Attention Is All You Need”](https://oreil.ly/58cuk). Techniques such as Reinforcement Learning from Human Feedback (RLHF) are often used to align LLMs to human preferences. LLMs may also utilize other techniques such as transfer learning, active learning, ensemble learning, embeddings, and others.

LLMs are quite massive, often trained on vast amounts of text data and comprising millions or even billions of parameters. General-purpose LLMs are commonly known as *foundational models*, highlighting their versatility and wide-ranging applicability across numerous tasks. Prominent examples include OpenAI’s Generative Pre-trained Transformer (GPT) series, such as GPT-3 and GPT-4, Google’s BERT (Bidirectional Encoder Representations from Transformers), Meta’s Llama, Mistral, and Claude. LLMs are capable of performing a wide range of general-purpose natural language processing tasks, including text generation, summarization, entity recognition, translation, question answering, and more.

LLMs can also be fine-tuned to specific domains. Fine-tuning is the process of retraining a pre-trained LLM on a domain-specific dataset, allowing it to adapt its knowledge and language understanding to suit better the terminology, vocabulary, syntax, and context of the target domain. For example, the [FinBERT](https://oreil.ly/J5vhT) is a domain-specific adaptation of the BERT model, fine-tuned specifically for the financial domain. It is trained on a vast amount of financial texts, such as news articles, earnings reports, and financial statements, to understand and process financial language and terminology effectively. FinBERT can be used for various tasks in the financial domain, including sentiment analysis, named entity recognition, text classification, and more.

LLMs can be a powerful technique for financial NER. This is because they are able to understand and process complex and domain-specific language, recognizing entities such as financial instruments, accounting, and regulatory terms, as well as company and person names within the context of financial markets. For example, an LLM may be able to distinguish “Apple Inc.” as a tech company listed on NASDAQ from the word “apple” as a fruit, using contextual clues from surrounding text. They can also identify financial terms such as “S&P 100,” “NASDAQ Composite,” and “Dow Jones Industrial Average” as indexes rather than just random phrases. Similarly, LLMs may be able to distinguish between terms like “call option” and “put option,” understanding that they refer to specific types of financial derivatives, despite their similar structure.

Crucially, while LLMs may show outstanding performance in many financial language processing tasks, they can still encounter challenges with specialized and evolving financial terminology. For example, financial terms such as “interest rate swap” (CDS), “collateralized debt obligation” (CDO), and “mortgage-backed securities” (MBS) necessitate a deep understanding of financial instruments and their contexts. Similarly, terms such as “bonds” and “equity” have completely different meanings in finance than in the general sense. Furthermore, terms like “bitcoin,” “blockchain,” “cryptocurrency,” and “DeFi” (decentralized finance) have emerged relatively recently and require continuous model updates to stay current.

# Retrieval-Augmented Generation

Retrieval-augmented generation (RAG) is an advanced technique employed to enhance the factual grounding, contextual relevance, and response accuracy of language models, especially in specialized domains like finance. RAG operates by retrieving relevant information from external sources, such as databases or documents, and incorporating this data into a language model’s input prompt, thereby providing additional context to produce more accurate and contextually relevant responses.

In finance-specific tasks like financial NER, RAG enhances accuracy by disambiguating entities, staying up-to-date with rapidly changing information, and integrating domain-specific knowledge from financial documents and databases. This capability makes RAG particularly effective for identifying financial entities and handling complex jargon. Crucially, the success of RAG largely depends on the availability of reliable external data sources, highlighting its foundation in data engineering.

Another major challenge with LLMs is *hallucination*, which happens when an LLM generates irrelevant, factually wrong, or inconsistent content. Interpret ability and transparency represent additional challenges, particularly in finance, where regulatory compliance and trust in decision-making are crucial.

### Wikification

Wikification is an entity disambiguation technique that links recognized named entities to their corresponding real-world Wikipedia page. [Figure 4-6](#ch04_figure_6_1724776828398485) illustrates this technique through an example. In the first step (entity recognition), two entities (Seattle and Amazon) are identified. In the next step, the identified entities are linked to their unique matching Wikipedia page.

### Figure 4-6. Wikification process

![Figure 4-6. Wikification process](images/fden_0406.png)

Several wikification techniques have been proposed, the majority of which utilize similarity metrics to determine which Wikipedia page is most similar to the recognized entity. One prominent implementation was first presented in [Silviu Cucerzan’s groundbreaking work](https://oreil.ly/BIhsI). Cucerzan proposed a knowledge base that incorporates the following elements:

Article entity/concept:   Most Wikipedia articles have an entity/concept associated with them.

Entity class:   Person, location, organization, and miscellaneous.

Entity surface forms:   The terms used to reference the entity in text.

Contexts:   Terms that co-occur or describe the entity.

Tags:   Subjects the entity belongs to.

For example, the term [*Berkeley*](https://oreil.ly/vT5eq) can refer to a large number of real-world entities, including places, people, schools, and hotels. Assume we are interested in identifying the University of California, Berkeley. In this case, the entity type is school or university; the context could be California, a public university, or a research university; tags might include education, research, science, and others; and the entity surface form might be simply Berkeley.

An entity is disambiguated by first identifying its surface form. Subsequently, two vector representations that encode contexts and tags are constructed: one for the Wikipedia context that occurs in the document and another for the Wikipedia entity. Finally, the assignment to a Wikipedia page is made via a process that maximizes the similarity between the document and entity vectors.

### Knowledge graphs

Knowledge graphs have become an essential technique in internet-based information search and have been widely applied in entity disambiguation. There isn’t yet a clear [definition of what a knowledge graph is](https://oreil.ly/xHyFe). Still, it basically involves gathering different types of facts, knowledge, and content from many sources, organizing them into a network of nodes and links, and using it to provide more information to users upon submitting a search query. In other words, a knowledge graph can be thought of as a network of real-world entities—i.e., persons, locations, materials, events, and organizations—related together via labeled directed edges. [Figure 4-7](#ch04_figure_7_1724776828398536) presents a simple illustrative example of a knowledge graph around the company Dell Technologies. The graph illustrates Dell Technologies and several related entities, such as its CEO, Michael Dell, and its supplier, Intel Corporation.

### Figure 4-7. Illustrative example of a knowledge graph

![Figure 4-7. Illustrative example of a knowledge graph](images/fden_0407.png)

The power of knowledge graphs stems from their extreme flexibility, which allows them to encompass a wide range of elements and interactions. This, in turn, can improve search results and reveal hidden data links that might otherwise go undetected using more traditional approaches.

Knowledge graphs have been proposed as an advanced approach to entity disambiguation within NER systems. A well-known implementation is the [Accurate Online Disambiguation of Named Entities](https://oreil.ly/Kzd_0), or AIDA. It constructs a “mention-entity” graph, where nodes represent mentions of entities found in the text, as well as the potential entities these mentions could refer to. These nodes are connected with weighted links based on the similarity between the context of the mention and the context of each entity. This helps the system figure out which entity the mention is most likely referring to. Additionally, AIDA connects the entities themselves with each other using weighted links. This allows AIDA to capture coherence among entities within the graph, aiding in the disambiguation process.

AIDA utilizes the *densest subgraph algorithm* to search the mention-entity graph. The densest subgraph algorithm helps identify the most densely connected subgraph within the larger graph. In the context of AIDA, this subgraph represents the set of mentions and entities that are most closely related to each other based on their connections and similarities. By identifying this densest subgraph, AIDA can determine the most coherent and relevant set of mentions and entities for a given context.

Two challenges may arise when finding such dense subgraphs. First, you need a reliable definition of the notion of a dense subgraph that ensures coherence and context similarity. Second, dense-subgraph problems are computationally expensive and almost NP-hard problems. This means that a heuristic or efficient algorithm is needed to guarantee a fast graph search to find the optimal dense subgraph.

## Named Entity Recognition Software Libraries

Practitioners in industry and academia have created several software tools for NER. Several open source tools are available, including spaCy, NLTK, OpenNLP, CoreNLP, NeuroNER, polyglot, and GATE.

In addition to open source solutions, financial institutions and data providers build proprietary NER solutions. The most famous example is RavenPack analytics, which we discussed earlier in this chapter. Another prominent example is [NERD (Named Entity Recognition and Disambiguation)](https://oreil.ly/9lpaZ), developed by S&P Global’s AI accelerator, Kensho. NERD is one of the few entity recognition and disambiguation tools tailored specifically for financial entities. NERD takes a text document as input and identifies mentions of named entities such as companies, organizations, and people. It also links the extracted entities to their real-world entries in the S&P Global comprehensive Capital IQ database.

FactSet provides a [Natural Language Processing API](https://oreil.ly/7l-f7) that can be used to recognize and locate a wide range of entities in structured and semi-structured texts. This includes companies, people, locations, health conditions, drug names, numbers, monetary values, and dates. In addition to NER, the API allows entity disambiguation by finding the best matching FactSet identifiers for companies and people found in the text.

Another tool that might be used for NER is *Automated Machine Learning* (AutoML). These solutions offer simple and user-friendly interfaces to automatically choose, train, and tune the best ML model/algorithm for a particular problem. One of the main advantages of AutoML is that it allows nonexperts to use sophisticated ML models. Examples of AutoML tools include open source libraries such as Auto-sklearn, AutoGluon, AutoKeras, and H20 AutoML, as well as cloud-based managed solutions such as Google AutoML and Amazon Sagemaker.8

AWS offers a specialized NLP AutoML service called Amazon Comprehend. Comprehend already has trained NER capabilities that you can immediately interact with, and it also offers the option to customize an NER system to your specific task (e.g., detecting financial entities). In addition, AWS introduced Bedrock, a managed service that allows users to build and fine-tune generative AI applications with foundation models.

# Financial Entity Resolution

Once entities have been recognized and identified, a system should be available whereby the data associated with a unique entity in one dataset can be matched with data held in another dataset for the same unique entity. This process is very common in finance and is known as entity resolution (ER). In this section, you will learn what ER is and why it is important in finance. Then, you will learn how ER systems work and the different approaches to ER. Finally, I will present a list of software libraries and tools available for performing ER.

## Entity Resolution Described

Entity resolution, also known as record linkage or data matching, refers to the process of identifying and matching records that refer to the same unique entity within a single data source or across multiple sources, particularly when a unique identifier is unavailable. When ER is applied to a single dataset, it is often done to identify and remove duplicate records (*record deduplication*). When it is applied to multiple datasets, the goal is to match and aggregate all relevant information about an entity (*record linkage*).

Mathematically, let’s represent two data sources as A and B and denote records in A as a and records in B as b. The set of records that represent identical entities in A and B can be written as:

M =

( a, b ); a = b; a ∈ A; b ∈ B

And the set of records that represent distinct entities as:

U =

( a, b ); a ≠ b; a ∈ A; b ∈ B

As we will see later in this chapter, the main objective of an ER system is to distinguish the set of matches *M* from the set of non-matches *U*.

## The Importance of Entity Resolution in Finance

Entity resolution is a common practice and represents a main challenge in the finance domain. As a financial data engineer, you will likely encounter the need to develop an ER system. Various industry initiatives have been established to address the financial ER problem. For instance, the [Financial Entity Identification and Information Integration (FEIII) Challenge](https://oreil.ly/dTFQB) was initiated to create methodologies for aligning the various financial entity identification schemes and identifiers. Despite these efforts, the problem remains unresolved for several reasons, which I will outline next.