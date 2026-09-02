### Figure 12-12. JupyterLab main overview page

![Figure 12-12. JupyterLab main overview page](images/fden_1212.png)

In the terminal, type the following command and hit Enter:

```
# Bash
python3 database/create_tables.py
```

You should see a few logs that say “SQL executed successfully.” This means that the tables we want for our OMS have been created in Postgres.

Next, we want to insert some data into the customers and inventory tables. This is needed because, later on, we will be executing our workflow with orders that already contain the customer and product information. Again, in the terminal, type the following command, then press Enter to execute it:

```
# Bash
python3 database/populate_tables.py
```

The customer and product tables are now populated with data. If you wish to view the content of these files that you have just executed, you can navigate to the database folder using the right sidebar, as shown in [Figure 12-12](#ch12_figure_12_1724776837382053). If, in addition, you want to see the populated tables in the database, switch to the tab with *http://localhost:8081/* and log in with the PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD values, which you can find in the *.env* file of the project. Once logged in, proceed with the same steps you learned in the first project to create a server and explore your tables.

The next step is to create and register our microservice workflow. First, we need to implement each mircoservice individually. This has been done for you, with each microservice residing within its respective folder within the *workflow* directory. You can use the left sidebar in JupyterLab to navigate to the *workflow* directory. You’ll find five folders in there, each corresponding to one of the previously defined microservices. Within each microservice folder, you’ll discover two scripts: one named *service.py*, which contains the microservice’s code, and the other named *worker.py*, containing the Conductor [worker program](https://oreil.ly/sJlB_) for the respective microservice. Each worker is tasked with executing a specific task, where the task corresponds to a microservice in our context.

### Note

To keep things simple, the logic defined in each *service.py* contains a database insert/update operation. In real business problems, you will obviously need to include more functionality and business logic in your microservices. This may involve computations, transformations, API calls, database calls, and various other operations.

Moving to our workflow, to see how it is defined using Conductor, open the *order\_workflow.py* file in the *workflow* directory from the sidebar. You will see how each task is defined by passing a reference name and the values for its parameters. The first task (acknowledge order) receives its input from the workflow input, while the other tasks take their input from the output of their previous tasks. More on passing input to tasks in Conductor is available in the [Conductor documentation](https://oreil.ly/MOuaK). Using Conductor, it is possible to create a linear flow using the >> operator. You can see how this is done at the bottom of the *order\_workflow.py* file*.*

Now that our workflow is ready to be created, the next thing you can do is register the workflow in the Conductor database. To do so, go back to the Terminal screen in JupyterLab and paste the following command:

```
# Bash
python3 workflow/register_order_workflow.py
```

You should see a log message saying that the workflow has been successfully registered. To review your newly created workflow, go to the tab running *http://localhost:5000/*. There, you’ll find the Conductor UI, which lets you check and monitor your workflow and task definitions and executions. Once there, use the top toolbar and navigate to the Definitions tab. You will find a table containing your workflows in your local instance. Click on the Order Workflow button to see the full details of the OMS workflow you created. [Figure 12-13](#ch12_figure_13_1724776837382071) illustrates what this page looks like.

### Figure 12-13. Order Workflow definition details page in Conductor

![Figure 12-13. Order Workflow definition details page in Conductor](images/fden_1213.png)

On the left side of [Figure 12-13](#ch12_figure_13_1724776837382071), you will see a lot of workflow definition parameters, many of which can be configured. To avoid extra complexity, we won’t be setting any custom variables in this project. On the right side, you will see a visual representation of our OMS workflow. As you can see, it’s a linear flow where tasks run in a sequence.

Now that we have our workflow registered, let’s execute it. To do so, we need to run the file called *execute\_order\_workflow.py,* which you can find in the *workflow* folder. If you open this file, you will see that I already prepared a dummy workflow input with customer\_id, products, payment amount, and delivery address. You can change these input values if you wish, but you need to make sure that the customer and products you add to the order exist in the database.

To execute our workflow, navigate to the Terminal tab in your JupyterLab and paste the following command:

```
# Bash
python3 workflow/execute_order_workflow.py
```

You should see a few log messages being printed that inform you about the successful outcome of the different microservices.

Now that you have executed the workflow, you can check the results in the database using pgAdmin. You’ll find a record of your order in the orders table, payment details linked to your order in the payments table, updates in the inventory and stock bookings tables, and a booked shipment in the delivery table.

Finally, you can review the details of your workflow execution via the Conductor UI. Simply visit *http://localhost:5000/* and click on Executions from the top toolbar. In the table displayed on that page, you’ll find a record corresponding to your workflow execution. Click on the ID listed under the workflowid column to access the details of this particular workflow execution. You should see a page similar to [Figure 12-14](#ch12_figure_14_1724776837382088).

### Figure 12-14. Order Workflow execution details page in Conductor

![Figure 12-14. Order Workflow execution details page in Conductor](images/fden_1214.png)

As shown in [Figure 12-14](#ch12_figure_14_1724776837382088), our workflow execution has completed successfully. By clicking on a specific task in the diagram on the left side, you can view its execution details, including the input it received, the output it produced, its logs, and its task definition details.

## Project 3: Clean Up

Run the following command in the root directory of Project 3:

```
# Bash
docker compose down
```

## Project 3: Summary

This project aimed to familiarize you with the process of building and executing microservice workflows. In real-world situations, you’ll likely tackle similar projects but with more complex requirements. For example, you are likely to deploy each of the services we defined into a separate environment, such as Cloud Functions or container-based deployment services, and configure security and access policies to allow them to communicate. Moreover, you will need to have a way to handle concurrency and dependencies in distributed transactions that span multiple services. Additionally, you might need to configure the workflow and task definitions to handle issues such as failure, retries, timeouts, etc.

# Project 4: Designing a Financial Reference Data Store with OpenFIGI, PermID, and GLEIF APIs

In this project, you will develop a basic reference data store that holds information for identifying financial instruments and various entities, including the following:

* The full list of ISO 3166 Country Codes.
* The FIGIs, ISINs, Thomson Reuters Open Perm IDs, and RICs for the [S&P 100 stocks](https://oreil.ly/RYylN). The S&P 100 is a primary stock index comprising 100 of the largest and most established companies listed on US stock exchanges.
* ISO 17442 Legal Entity Identifiers.
* ISO 10383 Market Identifier Codes.
* LEI-to-ISIN mappings.
* LEI-to-BIC mappings.

Throughout this project, you will be using three open APIs:

* [OpenFIGI for retrieving FIGI data](https://oreil.ly/VPX6F)
* [Open PermID for retrieving PermIDs and RICs](https://oreil.ly/Zvx15)
* [GLEIF API for retrieving LEI and country code identifiers](https://oreil.ly/jCttr)

If you are not familiar with financial identifiers, I strongly recommend reading Chapter 3 before beginning this project.

## Project 4: Prerequisites

The only prerequisite for this project is to obtain a PermID API token. To do so, follow these steps:

1. Go to *https://permid.org*.
2. From the top right, click on REGISTER and follow the steps to complete your sign-up.
3. Once completed, go back again to *https://permid.org* and sign in with your login credentials.
4. Once signed in, from the top menu, click on APIs → Display my API Token (see [Figure 12-15](#ch12_figure_15_1724776837382104) for an illustration).

### Figure 12-15. Finding your API token on PermID.org

![Figure 12-15. Finding your API token on PermID.org](images/fden_1215.png)

In the following section, you’ll use this token to communicate with the PermID API.

## Project 4: Local Testing

To start, navigate to the project directory in your terminal:

```
# Bash
cd {path/to/book/repo}/FinancialDataEngineering/book/chapter_12/project_4
```

Once you are in the main project directory, you will find an *.env* file with a variable called PERMID_API_KEY. Without using quotes, you must assign this variable the API access token you got from PermID (i.e., PERMID_API​_KEY=YOUR_API_TOKEN).

Run our containers with the following command:

```
# Bash
docker compose up -d
```

Throughout this project, you will be mainly interacting with JupyterLab notebooks. To begin, open your preferred browser and visit *http://localhost:8888/* to access JupyterLab.

The first thing we want to do is to create our tables in the database. These tables will store the various types of reference data that we will be loading. From the main JupyterLab overview page, open a Terminal and execute the following command:

```
# Bash
python3 scripts/create_tables.py
```

To view the tables, log in to pgAdmin on *http://localhost:8081/* using the PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD credentials you find in the *.env* file of the project. Once logged in, create a server with the POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD credentials following similar steps as in Project 1. When done, you can check the tables using the left sidebar (Databases → reference\_data → Schemas → public → Tables).

Now that you’ve created the tables, it’s time to populate them. To accomplish this, you’ll need to run multiple notebooks that have already been prepared for you. In JupyterLab, navigate to the *scripts* folder using the left navigation sidebar. Inside the scripts folder, you’ll find several directories. Open the first one named *country*. Inside, locate a file named *country.ipynb*. Double-click to open it. Then, from the top menu, select Run → Run All Cells. This action will execute all the code cells in your notebook, fetching and uploading the ISO 3166 Country Codes from the GLEIF API.

Follow the same steps with these files:

* *scripts/figi/figi.ipynb*
* *scripts/lei/lei.ipynb*
* *scripts/lei\_bic/lei\_bic.ipynb*
* *scripts/lei\_isin/lei\_isin.ipynb*
* *scripts/mic/mic.ipynb*
* *scripts/permid/permid.ipynb*

After running all these scripts, our reference data store should be ready. Switch to the pgAdmin tab and examine the contents of the tables to observe the data in action.

## Project 4: Clean Up

Run the following command in the same root directory as Project 3:

```
# Bash
docker compose down
```

## Project 4: Summary

This project was designed to offer you an introduction to the world of financial reference data. Constructing and managing reference data stores are essential and common tasks in the financial industry. Although the reference data used in this project was simple and limited, handling reference data often presents much more complex challenges. For more information on this topic, refer to the section “Reference Data”.

# Conclusion

Congratulations on finishing the final chapter of the book! This is a significant milestone, and I want to thank you for your dedication and commitment to completing this journey.

Throughout the first 11 chapters of this book, you’ve gained knowledge about a range of foundational and finance domain-specific subjects essential for your journey as a financial data engineer. In this final chapter, you worked on hands-on projects crafted to solidify your understanding from earlier sections and refine your abilities through practical implementation.

Although this chapter concludes our journey through this book, your exploration of financial data engineering is just beginning. This field is continuously evolving with new trends that will shape the future of financial markets. In “The Path Forward: Trends Shaping Financial Markets”, I’ll briefly highlight these emerging trends, providing you with a glimpse of what lies ahead.

# Follow Updates on These Projects

If the projects featured in this chapter undergo any updates or changes, I’ll document them on the [GitHub page](https://oreil.ly/c7TJt). Feel free to refer to it if you encounter any issues.

# Report Issues or Ask Questions

Should you encounter any challenges while setting up or executing any step in the projects outlined in this chapter, please don’t hesitate to create an issue on the project’s GitHub [repository](https://oreil.ly/XCV4f). I will make sure to reply to you in a very short time.

# The Path Forward: Trends Shaping Financial Markets

As we look toward the future, the financial industry is expected to undergo significant transformations, driven by technological advances, regulatory changes, evolving consumer demands, and shifting market dynamics. Financial data engineering will be central to these changes, playing a key role in guiding and shaping the financial landscape. The skills and knowledge you have gained through this book will equip you to tackle these future challenges head-on. Let’s take a quick look at these major trends on the horizon.

# Financial Integration

The global financial system is becoming more interconnected, breaking down barriers among different markets, regions, and institutions. This trend toward financial integration is driven by the need for seamless cross-border transactions and investments.

# Digitalization of Financial Markets and Cloud Adoption

The shift to digital financial markets is accelerating, with cloud technologies emerging as the key driver of innovation. This digital transformation enhances scalability, reduces costs, and improves access to financial services.

# Financial Regulation

Regulations in the financial industry are becoming more stringent and complex, with increased demands for privacy protection, transparency, accountability, and risk management. Ensuring compliance through accurate data collection, storage, security, protection, and reporting will be essential.

# Financial Data Sharing and Marketplaces

Data sharing is reshaping financial markets by boosting collaboration, innovation, transparency, and efficiency. Financial data marketplaces are emerging as key platforms for sharing and exchanging data, providing easy access to financial data for those who need it.

# Financial Standardization

Standardization is key to achieving interoperability and reducing complexity in financial data management. The financial services industry has fallen behind other sectors in collaborating to create and adopt comprehensive interoperable standards for storing and exchanging information. However, this is beginning to change, with initiatives such as the adoption of the Legal Entity Identifier (LEI) and ISO 20022 marking significant progress in this direction.

# Artificial Intelligence and Language Models

Artificial intelligence is revolutionizing financial markets by addressing a wide range of applications such as trading, risk management, fraud detection, customer service, and financial advising. Generative AI and LLMs are set to redefine the future of financial services, revolutionizing everything from front-office customer interactions and trading strategies to back-office operations such as risk management and compliance.

Regulations such as the EU AI Act are being established to ensure that AI systems are safe, transparent, and ethically sound. Additionally, standards for AI are being developed, with ISO creating the ISO/IEC JTC 1/SC 42 committee to oversee AI standardization. The committee introduced [ISO/IEC 42001](https://oreil.ly/9WXAX), the first global standard for AI management systems, providing guidelines for managing AI technologies effectively and ethically.

# Architectures for Specific Business Domains

In financial institutions, distinct business units—such as trading, risk management, compliance, and retail banking—have specific data needs and regulatory requirements. Adopting a domain-oriented approach allows for scalable and efficient data management by customizing the architecture to meet the particular needs of each unit.

# Data Collection

The scope of data collection in financial markets is expanding rapidly, encompassing everything from market transactions and customer interactions to alternative data sources like social media and IoT devices. This broader data collection offers financial institutions and regulators deeper insights, enabling more detailed analysis of market trends and risks.

# Speed and Efficiency

Speed and efficiency are in high demand within financial markets, reflected in the ongoing push for rapid, real-time transactions, fast access to market data, and the ability to quickly respond to market changes and opportunities. Efficient financial processes enhance customer satisfaction, enable the development of optimal trading strategies, allow for prompt and accurate fraud detection, and ensure the stability and efficiency of the financial system.

# Tokenization, Blockchain, and Digital Currencies

The future of financial markets will be profoundly influenced by tokenization, blockchain technology, and digital currencies, which promise to revolutionize transaction security, enable decentralized finance (DeFi) innovations, and enhance transparency across the financial ecosystem. These advancements will facilitate more efficient asset management, streamline cross-border transactions, and create new avenues for investment and financial inclusion.

Regulations are being introduced to provide legal certainty and consumer protection for crypto-assets and their service providers. The best example is the EU’s *Markets in Crypto-Assets* (MiCA) regulation, which aims to establish a uniform set of rules for the issuance, trading, and custody of crypto-assets across EU member states.

# What Can You Do Next?

Now that you have acquired the skills and knowledge outlined in this book, it’s your turn to explore the diverse and dynamic world of financial data engineering. The trends and challenges discussed here present numerous opportunities to make a meaningful impact. Dive into the various data problems faced by financial markets, identify the areas that excite you the most, and think about how you can contribute to solving these issues.

Whether it’s developing innovative solutions for financial integration, leveraging cloud technologies, ensuring regulatory compliance, facilitating data sharing, or harnessing the power of AI, the possibilities are endless. As a financial data engineer, you have the power to shape the future of finance. Embrace the challenge, push the boundaries of what’s possible, and become a key player in the next chapter of financial innovation.

The future is in your hands—go out there and make a difference!

# Afterword

As you reach the conclusion of *Financial Data Engineering*, I trust your answer to the question, “Are you ready to navigate today’s complex financial data landscape?” is a resounding “yes.” Like Tamer Khraisha and myself, you’ve likely realized by now that the journey of a financial data engineer is one without a clear endpoint. There is no final “pot of gold” waiting at the end of this path. Instead, the true reward lies in the continuous development of creativity, skills, and insights. Each step you take in mastering the intricacies of financial data is a reward in itself, contributing not only to your own growth but also to the ongoing evolution of the financial industry.

At the intersection of finance, digital data diversity, and data engineering lies an exciting and dynamic frontier. The opportunities for innovation are limitless, and each new challenge brings with it fresh insights. In an industry driven by data, transformation is constant, and we are all part of this exhilarating change.

Tamer Khraisha’s contributions to this field are a testament to the importance of embracing this journey. From his mastery of network science, analysis of lending practices, and numerous financial and technical analyses, to his pivotal work, “A Holistic Approach to Financial Data Science: Data, Technology, and Analytics,” published in *The Journal of Financial Data Science,* Spring 2020, Tamer has provided a critical foundation for understanding the relationship between data, technology, and finance. His motivation to develop this book reflects a desire to share knowledge, offer guidance, and inspire future financial data engineers.

As we continue to wrestle with the transition from traditional representations of value—such as coins and bills—to a purely data-driven financial ecosystem, it becomes clear that finance is now an information industry at its core. Data is no longer just a reflection of value; it is value. In this book, Tamer provides a comprehensive guide that combines finance domain expertise with software engineering, data science, and analytical techniques. These tools are crucial for extracting insights from financial systems and evaluating data-driven hypotheses.

The industry itself is a marvel. Despite countless complexities, idiosyncrasies, and convoluted relationships between financial entities, it operates smoothly on the backbone of data. This is where the power of financial data engineering shines, and Tamer’s book draws from personal experience, as well as the shared experiences of many professionals in this field, to help us navigate these complexities.

Part one of the book lays the essential foundations: an understanding of finance, the key concepts of financial data engineering, and the interrelationships between financial entities. Tamer brings order to the chaotic, diverse nature of financial data, identifying patterns and structures within the financial ecosystem. It is within this “primordial soup” of data that infinite creativity, innovation, and financial ingenuity thrive.

In part two, the book shifts to the technical frameworks and technologies needed to manage financial data. Tamer outlines critical decisions regarding the shape, size, and velocity of data and provides practical examples for applying data engineering techniques. These hands-on exercises are invaluable for deepening your understanding of real-world financial data solutions.

Finally, Tamer guides us into the future of the financial industry, where ongoing digital transformation demands ever greater mastery of data engineering. Financial system integration, product innovation, and technological advancements will continue to drive the need for financial data engineers who can navigate this new world with confidence and expertise.

You now possess a deeper understanding of the financial data landscape and the analytical frameworks needed to unlock its potential. The tools and skills you’ve gained from this book have empowered you to analyze complex data and derive actionable insights that will contribute to the financial industry’s future.

Your journey, like Tamer’s and mine, will be one of continuous learning, adaptation, and exploration. The world of financial data is vast, and the challenges it presents are complex—but the rewards for those who embrace these challenges are profound. This book is just the beginning of what promises to be an exciting and fruitful career as a financial data engineer. Take with you the inspiration, creativity, and innovation that define this field, and know that every discovery you make brings you closer to designing the art and mastering the science of financial data engineering.