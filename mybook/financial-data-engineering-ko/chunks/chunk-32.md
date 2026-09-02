# Prerequisites

All projects in this chapter will be packaged and isolated with all their dependencies into Docker containers. Docker is the most popular open source software for operating system (OS) virtualization (aka containerization). It is available for Windows, macOS, and Linux through *Docker Desktop*. Therefore, to run the projects on your machine, you must install the Docker Desktop version that is compatible with your operating system. Please follow the instructions in the official [Docker documentation](https://oreil.ly/bWa1c) to complete the installation. Furthermore, as you will be running more than one container in each project, you will be using a specific multi container orchestration tool called [Docker Compose](https://oreil.ly/KzSYO), which is ideal for local testing and development.

The other prerequisite is to clone this book’s GitHub repository onto your local machine. First, make sure you have [Git](https://oreil.ly/7Xnmv) installed. Then, open a terminal in your computer, navigate to the location where you want to pull the project files, and finally, clone the [repository](https://oreil.ly/UeQyE).

# Project 1: Designing a Bank Account Management System Database with PostgreSQL

Account management is a core functionality for banks, allowing them to handle and oversee customer accounts, balances, and transactions. In this project, you will design and implement a relational database system for managing bank accounts. You will be using the conceptual/logical/physical data modeling approach discussed in Chapter 8.

## Conceptual Model: Business Requirements

In the conceptual phase, the focus is on understanding business requirements and defining the high-level structure of the database system. Operational and business models vary from one banking institution to another, and not all banks offer the same products and services. As such, you will design a simple and generic bank account management system for this project.

We’ll assume that stakeholders have defined their requirements and that these have been formalized them into entities, relationships, and constraints. Let’s explore each in greater depth.

### Entities

Our bank account management system needs to store data for seven types of entities: accounts, customers, loans, transactions, branches, employees, and cards.

Accounts are the most essential product that banks offer to their customers. For this reason, the account entity is needed to maintain detailed records of the various account types offered by the bank (e.g., savings, checking), along with account IDs, associated customers, balances, and more.

Loans are also a key banking product. Thus, the loan entity is needed to store information such as loan ID, terms (including amount, duration, interest rate, payment schedule, and start and end dates), type (such as mortgage or personal loan), and other relevant details.

In addition to accounts and loans, most banks provide a range of payment cards to their clients. As a result, the card entity is crucial for storing card-related information, including cardholder ID, associated accounts, card numbers, issuance and expiration dates, and other relevant details.

Customers represent the bank’s client base, including both individuals and organizations. Therefore, the customer entity is essential for storing vital client information, such as IDs, names, addresses, statuses (e.g., active, inactive), and contact details (e.g., email addresses and phone numbers).

Employees are the individuals hired by the bank to deliver various services to customers. To manage employee information, the employee entity is required to store attributes such as employee IDs, names, job titles, and the branch where they are assigned.

Branches are the bank’s physical locations where customers engage with employees to perform various transactions. The branch entity is essential for managing branch information, including branch IDs, names, addresses, and phone numbers.

Lastly, banks must track all transactions associated with customer accounts. Therefore, the transaction entity is vital for recording transaction details such as transaction IDs, associated account IDs, employee IDs (for transactions initiated by employees), timestamps, and amounts.

### Relationships

The business team has requested that the following relationships be established between entities:

* Each account should be linked to a customer.
* Each loan should be linked to a customer.
* Each loan payment should be linked to a transaction and an account.
* Each employee should be affiliated with a branch.
* Each card should be associated with both a customer and an account.

These relationships ensure data integrity and facilitate efficient data retrieval and management.

### Constraints

The business team has outlined the following constraints to be enforced within the database implementation:

* Account balances must never go below a customer-specific minimum amount.
* All entity records (e.g., accounts, loans, transactions) must be identified with a unique ID.
* Data redundancy should be minimized.
* Null values are not permitted for certain fields.
* Specific fields, such as email addresses, must be unique across records.

Constraints play a pivotal role in ensuring high data quality, consistency, integrity, and compliance, which in turn contributes to the reliability of the account management system.

## Logical Model: Entity Relationship Diagram

Now that we have stakeholder agreement on the account management conceptual model, the next step is to build the logical model. This stage focuses on selecting the data storage model most suitable for our system (a concept discussed in Chapter 8).

After a thorough evaluation, the financial data engineering team has concluded that the relational model is the best fit. This model effectively organizes various entities into distinct tables and ensures data integrity through database constraints. Moreover, the relational model supports the implementation of a normalized data structure, which is essential for our system.

To implement this, we need to create the *Entity Relationship Diagram* (ERD) for our logical model. An ERD is a visual representation used to model the structure of a database. It illustrates the entities (such as tables or objects) within a system, their attributes (such as fields or properties), and the relationships among these entities. An ERD is constructed using information collected and summarized from the previous conceptual phase. Various tools are available for drawing ERDs, including Lucidchart, Creately, DBDiagram, ERDPlus, DrawSQL, QuickDBD, and EdrawMax. [Figure 12-1](#ch12_figure_1_1724776837381855) illustrates the ERD of our account management system.

### Figure 12-1. Entity Relationship Diagram of our example bank account management system

![Figure 12-1. Entity Relationship Diagram of our example bank account management system](images/fden_1201.png)

With the ERD design complete, let’s move on to the next step: selecting the database technology and translating our ERD into database queries.

## Physical Model: Data Definition and Manipulation Language

With our logical data model ready, it’s time to choose a relational database technology and write the queries to create and populate our tables. Let’s assume the financial data engineering team has selected PostgreSQL as the database management system due to its high reliability and strong adherence to SQL standards.

Now, let’s shift gears and test things on your machine.

## Project 1: Local Testing

To interact with PostgreSQL, you will need to run two Docker containers: one for the PostgreSQL database instance and another for pgAdmin, a user-friendly UI for interacting with PostgreSQL.

To launch the two containers, open a terminal and navigate to the following path:

```
# Bash
cd {path/to/book/repo}/FinancialDataEngineering/book/chapter_12/project_1
```

Then execute the following [docker compose command](https://oreil.ly/x3kBG) to run our project containers:

```
# Bash
docker compose up -d
```

After that, open a browser and paste the URL *http://localhost:8080/* into a new tab. Wait until you see the pgAdmin UI and log in using the dummy credentials (PGADMIN\_DEFAULT\_EMAIL and PGADMIN\_DEFAULT\_PASSWORD) in the [*.env* file](https://oreil.ly/eRzH-). Remember that this setting is for local testing purposes, and you should never share or store passwords publicly or explicitly in your project files.

Once logged in, click on Add New Server and insert the following values:

* In the General tab, give a name to the server (e.g., Bank Account).
* In the Connections tab, set:

  + Host name/address = *postgres*
  + Port = *5432*
  + Maintenance database = *bank\_account*
  + Username = *admin*
  + Password = *password*

These are the values that you set in the project’s environmental variables file *.env.* In the upcoming projects, we’ll utilize pgAdmin, and you’ll need to configure it by following similar steps. However, you’ll need to use the credentials provided in the *.env* file specific to each project. Once completed, click on Save. [Figure 12-2](#ch12_figure_2_1724776837381887) illustrates these steps.

### Figure 12-2. Creating a new server in pgAdmin

![Figure 12-2. Creating a new server in pgAdmin](images/fden_1202.png)

After that, from the left sidebar, follow these steps (as shown in [Figure 12-3](#ch12_figure_3_1724776837381906)):

1. Navigate to Servers → Bank Account → Databases → bank\_account → Schemas → public → Tables.
2. Right-click on Tables and select Query Tool.

Now, we are ready to create our tables. In SQL, using the term *Data Definition Language* (DDL) to denote statements that create or alter database objects is common. DDL statements include CREATE, ALTER, and DROP. The full list of table creation queries is available on this book’s [GitHub repo](https://oreil.ly/ZltsM). You will need to copy and paste all the queries into the Query Tool and click the Run arrow on the top, as illustrated in [Figure 12-3](#ch12_figure_3_1724776837381906). This will create all the tables for our bank account management system. To see the tables, right-click Tables from the left sidebar and hit Refresh. Then you will be able to see the 16 tables, as illustrated in [Figure 12-4](#ch12_figure_4_1724776837381925).

### Figure 12-3. Opening the Query Tool editor

![Figure 12-3. Opening the Query Tool editor](images/fden_1203.png)

### Figure 12-4. Creation and visualization of the tables

![Figure 12-4. Creation and visualization of the tables](images/fden_1204.png)

### Note

In this project, you’ll manually copy and execute SQL commands directly within pgAdmin’s query console. This approach was intentionally chosen to familiarize you with the SQL syntax. It’s worth noting that databases can also be interacted with programmatically. For example, in the upcoming projects, we’ll utilize Python’s database driver, psycopg2, to interact with PostgreSQL.

As you will see, 16 tables were created. To have an idea about our DDL queries, let’s take a closer look at the CREATE TABLE statement for the account table:

```
-- PostgreSQL
CREATE TABLE Account (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES Customer(id),
    branch_id INT NOT NULL REFERENCES Branch(id),
    type INT NOT NULL REFERENCES AccountType(id),
    currency VARCHAR NOT NULL,
    number VARCHAR NOT NULL UNIQUE,
    balance DECIMAL(10,2) NOT NULL,
    minimum_balance DECIMAL(10,2) NOT NULL DEFAULT 0,
    date_opened DATE NOT NULL,
    date_closed DATE,
    status INT NOT NULL REFERENCES AccountStatusType(id)
    CHECK (balance >= minimum_balance)
);
```

As you can see, the table has a serial ID as a primary key. This is used to automatically generate an increasing sequence of integers. Moreover, the table has four foreign keys referencing the IDs of four distinct tables: Customer, Branch, AccountType, and AccountStatusType. These keys are crucial for ensuring data integrity. Should, for example, a customer with ID 202 not exist in the customer table, the Customer ID foreign key will prevent the creation of an account associated with this customer. Lastly, a key feature of this table is the account balance, which specifies a minimum balance requirement for each customer. A check constraint is added to ensure the balance never falls below the customer-specific minimum. Any attempt to update the balance to a value lower than the specified minimum will result in an error.

Now, let’s populate the tables with some data. In SQL, it is common to use the term DDL to indicate statements that add, update, and delete records in a database. For most tables in our system, the insert operations are quite simple. For example, to add a new customer, you would need to run the following:

```
-- PostgreSQL
INSERT INTO Customer (
  customer_type_id, name, country, city, street,
  phone_number, email, status
) VALUES (
  1, 'John Smith', 'US', 'New York',
  '123 Main St', '123-456-7890', 'john@example.com', 1
);
```

The full script of the insert queries is available in this GitHub [file](https://oreil.ly/Hrgjp). Copy all the insert queries, paste them into the Query Tool, and run the operation again. To see the data, right-click on a table name → View/Edit Data → All Rows. See [Figure 12-5](#ch12_figure_5_1724776837381941) for an illustration.

### Figure 12-5. Visualization of table rows

![Figure 12-5. Visualization of table rows](images/fden_1205.png)

Interestingly, some insert queries consist of multiple statements. For example, a payment transaction needs to be recorded in the transactions table and requires a concurrent update of the account balance in the account table. To this end, both statements need to be wrapped with an explicit SQL transaction. It is called explicit because PostgreSQL executes any statement by default within an implicit transaction. Here is an example where a transaction of 40 USD is recorded for the account with ID = 1:

```
-- PostgreSQL
BEGIN;
INSERT INTO transaction (account_id, type, currency, date, amount)
VALUES (1, 4, 'USD', '2022-01-01 08:00:00', -40.00);
UPDATE account
SET balance = balance - 40.00
WHERE id = 1;
COMMIT;
```

Last but not least, an even more complex operation is the loan payment. Here, we need to record the payment in the loan payment table, then store it as a transaction in the transaction table, and finally update the customer’s balance in the account table. To illustrate, here is an example of a loan payment of 1,000 USD recorded for the account with ID = 1:

```
-- PostgreSQL
BEGIN;
DO $$
DECLARE
    payment_amount DECIMAL := 1000.00;
BEGIN
    WITH inserted_transaction AS (
        INSERT INTO Transaction (account_id, type, currency, amount)
        VALUES (1, 1, 'USD', -payment_amount)
        RETURNING id
    )
    INSERT INTO LoanPayment (
      loan_id, transaction_id, payment_amount, scheduled_payment_date,
      payment_date, principal_amount, interest_amount, paid_amount
    )
    SELECT
      1, id, payment_amount, '2022-04-01', '2022-04-01',
      900.00, 100.00, payment_amount
    FROM inserted_transaction;

    UPDATE account
    SET balance = balance - payment_amount
    WHERE id = 1;
END$$;
COMMIT;
```

To create more transactions, run the queries in [this GitHub file](https://oreil.ly/nr_CS). The query for creating a loan payment is available in [this book’s GitHub repo](https://oreil.ly/9K_yn).

## Project 1: Clean Up

Once you are done with the project and you want to move to the next one, make sure you run the following [command](https://oreil.ly/iiFm2) in the same root directory of Project 1:

```
# Bash
docker compose down
```

This command will stop and remove containers, networks, volumes, and images created by docker compose up.

## Project 1: Summary

The goal for this project was to familiarize you with practical data modeling, database design, DDL and DML (Data Manipulation Language), and multi statement transactions. While this project provided a foundational understanding, it’s important to note that a real-world bank account management system demands more extensive development. For example, implementing database security features like user roles and permissions, authentication, and data encryption will be necessary. Moreover, you will need a database optimization strategy that involves indexing, clustering, and typing. Finally, you will need to establish a reliable integration between the database and your application. This involves using database connectors, clients, connection pooling, object-relational mappers (e.g., SQLAlchemy), and more. Tackling all of these features is beyond the scope of this book and would require a lot more detailed explanation.

# Project 2: Designing a Financial Data ETL Workflow with Mage and Python

In this project, you will design and implement a financial data ETL workflow. This involves retrieving historical stock price data from a financial API, applying various transformations, and ultimately storing the processed data in a database.

More specifically, we will be fetching the intraday open, close, high, and low prices, alongside trading volume, for four prominent stocks: Google, Amazon, IBM, and Apple. The source of our data will be the free version of the [Alpha Vantage Stock Market API](https://oreil.ly/f_GVm). Subsequently, we’ll aggregate the intraday values to derive daily averages. Both the raw data and the transformed daily data will be stored in a PostgreSQL database. Let’s assume that the workflow must be run once at the start of each month to retrieve data for the previous month.

## Project 2: Workflow Definition

This project’s workflow will have a linear structure consisting of the following steps:

1. Data retrieval

   * Fetch adjusted intraday time series history for the past month using the [TIME_SERIES_INTRADAY endpoint](https://oreil.ly/jWueo). As the free API version allows for 25 requests per day, we’ll query data for 4 stocks: Amazon, IBM, Apple, and Google. The API request specifies the following parameters:

     + A one-minute time interval between consecutive data points.
     + `adjusted=true` to retrieve a time series adjusted by historical split and dividend distributions.
     + The month parameter is set to the past month for monthly data retrieval.
     + `outputsize=full` to obtain the full intraday history of the specified month.
     + `datatype=csv` to receive the time series as a CSV file.
2. Raw data storage

   * Store the raw data in the database, recording the ingestion timestamp.
3. Data aggregation

   * Select the required columns for the primary transformation task, which will involve aggregating intraday values to compute daily averages.
   * Compute daily aggregates by averaging the open, close, high, low, and volume columns, grouped by date and ticker symbol.
4. Deduplication

   * Select columns for deduplication to address the aggregation step’s behavior of computing aggregates without row grouping, where each row receives the corresponding aggregate of its group.
   * Deduplicate the data, retaining the aggregated columns
5. Data export

   * Export the daily averages to the database for further analysis.

We will execute each one of these steps in a linear sequence.

## Project 2: Database Design

In our database, we will need two tables: one to store the raw intraday data retrieved from the API and another to store the transformed daily data produced at the end of our workflow. [Figure 12-6](#ch12_figure_6_1724776837381957) illustrates the ERD of these tables.

### Figure 12-6. ERD of the API stock data

![Figure 12-6. ERD of the API stock data](images/fden_1206.png)

Let’s move ahead to test our workflow in action.

## Project 2: Local Testing

To begin testing, the initial step is to claim your Alpha Vantage API key on the [Alpha Vantage website](https://oreil.ly/N-SW2). Follow the instructions you find on the page, and you will receive an API key that you need to keep as a secret and never share it with anyone else.

Once you have the API key, you will need to navigate to the project’s main directory. As before, this can be done by typing in the following command in your terminal:

```
# Bash
cd {path/to/book/repo}/FinancialDataEngineering/book/chapter_12/project_2
```

Once you are in the main project directory, you will find an *.env* file with a variable called ALPHAVANTAGE_API_KEY. Without using quotes, you must assign this variable the API key you get from Alpha Vantage (i.e., ALPHAVANTAGE​_API​_KEY=YOUR_API_KEY).

After that, run the project containers with the following command:

```
docker compose up -d
```

Once completed, you will have three running containers:

* [Mage](https://oreil.ly/-s1mz) running on *http://localhost:6789/*. Mage is an open source data pipeline tool renowned for its user-friendly UI, ease of use, and extensive feature set, making it an ideal option for ETL workflows.
* A PostgreSQL instance where we will store the data.
* The pgAdmin client running on *http://localhost:8080/*. As before, you will use pgAdmin to create the project tables and explore the outcome of your workflow data outputs.

To begin, let’s create our tables. Open a tab in your browser and navigate to *http://localhost:8080/*. Log in with the PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD that you have in your project’s *.env* file. Follow the same steps as you did in the first project to create a server, and from the left sidebar, open the database called *stock\_data*, then navigate to the schema called *public*. From there, you should be able to open a query tool and execute the queries you find in the [*create\_tables.sql* file](https://oreil.ly/YQ5Z7) to create the tables.

Once the tables are created, it’s time to move on to build our ETL workflow. Open another browser tab and navigate to *http://localhost:6789/*. You should be able to see Mage’s overview page, as illustrated in [Figure 12-7](#ch12_figure_7_1724776837381974). From the top left, click on “+ New pipeline” and select “Standard (batch).” You will be asked to give your pipeline a name; let’s call it *Adjusted Stock Data.* Once done, click on Create.

### Figure 12-7. Mage overview page

![Figure 12-7. Mage overview page](images/fden_1207.png)

After creating your pipeline, you will be redirected to the pipeline edit page, as shown in [Figure 12-8](#ch12_figure_8_1724776837381989).

### Figure 12-8. Pipeline edit page

![Figure 12-8. Pipeline edit page](images/fden_1208.png)

From the left sidebar, open the file called *io\_config.yaml*, delete all its content, and add the content of the [*io\_config.yaml* file](https://oreil.ly/6O8RI) to it. Once done, from the top menu, click File → “Save file” and then close the file editor. The [*io\_config* file](https://oreil.ly/7gBzq) is used by Mage to store and access credentials required to connect to databases and various storage systems.

After this, you will need to create the different components of our ETL workflow. From the same pipeline edit page ([Figure 12-8](#ch12_figure_8_1724776837381989)), you can see different buttons that can be used to create an operator, such as data loader, exporter, and transformer. Let’s create what we need as follows:

1. Create the API data loader:

   1. Click on +Data loader → Python → API.
   2. Name it *Load Data from Alpha Vantage* and then click “Save and add.”
   3. In the code editor that appears, delete all code and replace it with the code in [*fetch\_intraday\_data.py*](https://oreil.ly/W_AE-).
   4. From the top menu, click File → Save pipeline.
   5. Use the small up arrow (^) on the top right of the data loader block to close it so you can better see the structure of your pipeline.
   6. In the subsequent phases, repeat steps d and e.
2. Create the raw data exporter:

   1. Click on +Data exporter → Python → PostgreSQL and call it *Export Raw Data*.
   2. Delete the content of the editor that appears and replace it with the code in [*export\_intraday\_data.py*](https://oreil.ly/bhB6W).
3. Create the aggregation column selection transformer:

   1. Click on +Transformer → Python → Column removal → Keep columns and name it *Select Aggregation Columns.*
   2. Paste the code from [*select\_columns\_for\_aggregation.py*](https://oreil.ly/fJHCE) into the editor.
4. Perform the aggregation:

   1. Click on +Transformer → Python → Aggregate → Aggregate by average value and name it *Compute Averages.*
   2. Paste the code from [*compute\_daily\_aggregates.py*](https://oreil.ly/jAy8K) into the editor.
5. Create the deduplication column selection transformer:

   1. Click on +Transformer → Python → Column removal → Keep columns and name it *Select Deduplication Columns*.
   2. Paste the code from [*select\_columns\_for\_deduplication.py*](https://oreil.ly/awAQa) into the editor.
6. Drop the columns that contain duplicates:

   1. Click on +Transformer → Python → Rows actions → Drop duplicates and name it *Drop Duplicates.*
   2. Paste the code from [*drop\_duplicates.py*](https://oreil.ly/6eW39) into the editor.
7. Export the daily average data to the database:

   1. Click on +Data exporter → Python → PostgreSQL and call it *Export Daily Data.*
   2. Paste the code from [*export\_daily\_data.py*](https://oreil.ly/DFsyG) into the editor.

Once these steps are done, your workflow is complete and ready to be executed. It should look like [Figure 12-9](#ch12_figure_9_1724776837382006).

### Figure 12-9. Overview of the full financial data pipeline

![Figure 12-9. Overview of the full financial data pipeline](images/fden_1209.png)

To perform a workflow execution test, navigate to the Pipelines section using Mage’s left sidebar. Locate your pipeline named adjusted\_stock\_data. Click on the pipeline name, then select Run@once from the top menu, and confirm by clicking “Run now.” A new execution line with a random name will appear in the table. Click on the name displayed, then patiently observe the execution progress as it advances through the seven steps.

Once completed with success, navigate to the pgAdmin tab in your browser and check the data in the database. You should see that both tables are populated with the data produced by your pipeline.

## Project 2: Clean Up

Run the following command in the same root directory of Project 2:

```
# Bash
docker compose down
```

## Project 2: Summary

Throughout this project, you’ve gained hands-on experience building a financial ETL workflow with Alpha Vantage API, Mage, Python, and PostgreSQL. In real-world scenarios, you’ll probably design and build similar pipelines. Yet, you will very likely need to incorporate more complex transformers and data quality validations. Additionally, you’ll need to deal with challenges in pipeline management, such as scheduling, variable and secret management, triggers, scaling, concurrency, and data integration, among others. I strongly advise consulting the official Mage [documentation](https://oreil.ly/-s1mz) to learn about these subjects and beyond.

# Project 3: Designing a Microservice Workflow with Netflix Conductor, PostgreSQL, and Python

In this project, you will implement a microservice-based order management system (OMS) to process orders for an online store. Any online company that wants to streamline the entire order fulfillment process must have an OMS.

It’s important to note that microservice workflows often entail more complexity than other types of workflows. Additionally, because microservices tend to be distributed in nature and deployed across diverse environments, accurately replicating microservice architectures locally can be quite challenging. Nonetheless, this project will offer a minimal example to provide insight into the structure and characteristics of microservices.

## Project 3: Workflow Definition

The first step in designing a microservice workflow is to define its structure. To this end, let’s start by outlining the microservices that will constitute our OMS system. Here are the five microservices we’ll need:

Order acknowledgement service:   Handles the acknowledgment of customer orders. It receives a client order, persists it in the database, and returns an acknowledgment message to the customer.

Payment processing service:   Processes customer payment transactions and returns a message informing the customer about the status of their payment operation.

Stock and inventory service:   Manages the inventory and stock levels of products available for sale. It tracks and checks the quantity of each product in stock, books and updates inventory based on incoming orders, and returns a message to the customer about the stock booking.

Shipping service:   Manages the shipment of orders. This service coordinates with shipping carriers to book a delivery, generate a tracking number, and update the delivery status of orders. It returns a message informing the client about their upcoming delivery.

Notification service:   Sends notifications to customers at various stages of the order fulfillment process.

As a next step, we need to define the dependency structure among our services. To keep things simple, we will design a linear workflow that executes one service after another. Once an order is submitted, it first gets acknowledged, then the payment gets processed, then the stock gets booked, and finally, a delivery is scheduled. [Figure 12-10](#ch12_figure_10_1724776837382022) illustrates the workflow.

### Figure 12-10. OMS workflow structure

![Figure 12-10. OMS workflow structure](images/fden_1210.png)

## Project 3: Database Design

A reliable database system is required to store and manage order-related data. In line with the other projects in this chapter, PostgreSQL stands out as our database solution of choice. Different database design patterns exist for microservices. While some advocate for a dedicated database per service, others favor a unified database shared across all microservices. To simplify our microservice structure, let’s proceed with the latter approach—the single shared database pattern.

In our database, we will have five tables:

* The orders table stores orders along with their unique identifiers.
* The payments table stores transactional data related to order payments.
* The inventory table stores product inventory details.
* The stock bookings table stores the allocation of order items within the inventory.
* The delivery schedule table stores tracking delivery and shipment details.
* The notifications table stores customer notifications.

[Figure 12-11](#ch12_figure_11_1724776837382037) illustrates the ERD of our OMS database.

### Figure 12-11. OMS database ERD

![Figure 12-11. OMS database ERD](images/fden_1211.png)

Next, let’s move on to see our microservice system in action.

## Project 3: Local Testing

As usual, you will need to navigate to the project directory in your terminal:

```
# Bash
cd {path/to/book/repo}/FinancialDataEngineering/book/chapter_12/project_3
```

Then, run our containers with the following command:

```
# Bash
docker compose up -d
```

Once completed, you will have three services running that we will be interacting with:

* JupyterLab to program and execute our workflow in Python. It will be running on *http://localhost:8888/*.
* Conductor orchestrator to explore and monitor workflows and executions via a user-friendly UI. It will be running on *http://localhost:5000/*.
* PgAdmin client UI to explore the data generated by executions. It will be running on *http://localhost:8081/*.

Open three browser tabs and paste the three localhost URLs into each. We will be interacting mostly with JupyterLab, so navigate first to the tab for *http://localhost:8888/*. Once it’s ready, open a terminal from the Launcher tab. Consult [Figure 12-12](#ch12_figure_12_1724776837382053) for an illustration.