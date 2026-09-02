### Tip

Keep in mind that cost is not always a downside to on-premises solutions. In some cases, it might be the best cost-efficient solution if configured and managed with high quality standards as well as software-aware and hardware-aware best practices. For example, in 2023, [X (formerly known as Twitter) announced that it implemented a cloud exit strategy](https://oreil.ly/JWqKY) by moving data and workload out from the cloud and onto its own on-premises servers. The move resulted in a 60% decrease in cloud data storage size and a 75% decrease in cloud data processing costs.

The second downside is scalability. In an on-premises setting, institutions have a certain number of servers that they manage. As long as the infrastructure can handle the load, there should be no problems. However, if the load increases much more than the current server infrastructure can handle, then either the system will experience downtime issues or more servers need to be added. Adding more servers can be costly and time-consuming; and once added, they can’t simply be removed and returned. One solution to this issue is to overprovision by having extra server capacity all the time. However, this strategy can lead to extra costs due to unused resources.

The third drawback is that institutions may find themselves spending less time on product and feature development and more time on server maintenance and time-consuming technical, bureaucratic processes. Large financial institutions may tolerate this; however, for smaller institutions such as FinTech firms, the burden may not be sustainable.

# Mainframe Architecture

As far as the financial sector is concerned, it is hard to avoid mentioning *mainframes*. In a few words, a mainframe is a highly performant, scalable, and resilient computer endowed with large amounts of memory and processing power. The main advantage of mainframe computers is their ability to handle massive volumes of simultaneous transactions and requests while at the same time ensuring reliability, security, availability, high throughput, and low latency.

This feature makes mainframes well-suited for core financial applications such as banking, customer order processing, payment processing, and various mission-critical tasks that process billions of transactions on a daily basis. If you have ever interacted with an automated teller machine (ATM) or point-of-sale terminal at a retail shop, your request likely involved a mainframe at some point.

The market pioneer in mainframes is [IBM](https://oreil.ly/XEeAp), which has been producing mainframe computers since 1952. IBM mainframes have evolved over time to meet the diverse requirements of resilience, security, and performance. The primary mainframe system offered by IBM is the IBM Z System, which includes various generations such as the IBM z15, IBM z14, and IBM z13. Complementing these mainframes are a range of related IBM offerings, including IBM’s proprietary operating system, known as IBM z/OS; IBM’s transaction processing system, known as the Customer Information Control System (CICS); IBM’s relational database management system DB2; and the middleware communication system IBM MQ. This integrated and secure ecosystem has enabled IBM to maintain a significant market share within the financial sector, particularly for payment and transaction processing.

### Cloud computing

A major alternative and competitor of the on-premises model is the cloud. In this book, we define the cloud as:

> A general-purpose technology that enables the development and delivery of computing and storage services over a networked system.

In this definition, the term *general-purpose technology* refers to a technology whose adoption and impact span many sectors within the economy, substantially impacting preexisting social and economic structures. The best examples of general-purpose technologies are electricity, the internet, and artificial intelligence. The cloud is already a general-purpose technology, given its wide range of applications and adoption in businesses, governments, hospitals, research centers, financial institutions, educational institutions, the military, and many more.5

The most important thing about the cloud is how it’s delivered, not just the services it delivers. Many of the underlying technologies powering the cloud already exist and are utilized in various applications. This includes, for example, software and hardware virtualization technologies, multicore technologies, networking (network computing, software-defined networking, software-defined security, WAN), data centers, database management systems, file storage systems, open source tools, machine learning, and DevOps, to name a few. However, with the cloud, such technologies have been abstracted and architectured in a novel way that allows for the delivery of scalable, highly available, managed, and pay-as-you-go services through a networked system. The public internet is the primary delivery network, but it is also possible to establish a private cloud that operates on premises or in a data center managed by a cloud provider. In the next section, we will explore in detail the differences among public, private, and hybrid clouds.

Cloud products can be classified into three main categories:

Software-as-a-service (SaaS):   SaaS products are delivered to customers via the internet and are entirely managed and maintained by the cloud provider. With a SaaS solution, users can easily get started with the product, often instantly upon confirming a subscription plan, and they do not need to worry about configuration, software licensing, installation, or upgrades. Users might still need to confirm who can access their SaaS and what privileges they have. Examples of SaaS products include Gmail, GDrive, BigQuery, Dropbox, Snowflake, and many more. Sometimes, SaaS solutions get assigned more precise names, such as database-as-a-service and AI-as-a-service.

Platforms-as-a-service (PaaS):   PaaS provides online platforms for developing applications via APIs and operating system services. Consumers of PaaS control the settings of the hosting environment, the application, and access policies but not the infrastructure, storage, and networking. SaaS apps are typical users of PaaS. Examples of PaaS include the Google App Engine and DigitalOcean App Platform.

Infrastructure-as-a-service (IaaS):   IaaS is the lowest level of cloud offering and provides raw physical resources (CPU, RAM, storage, and networking) as a service, with the user having nearly complete control over the configuration of the instances. The majority of SaaS and PaaS apps are based on IaaS. Examples of IaaS include AWS EC2 and Google Compute Engine.

### Note

The cloud market is growing into a complex landscape of providers, services, and products. It is important to keep in mind that there are differences between a cloud provider and a cloud-based service provider. Cloud providers own and provide a large number of data centers distributed all over the world. These providers are called [hyperscalers](https://oreil.ly/KjHx1) and include major players such as AWS, Microsoft, and Google. On the other hand, there exist a large number of cloud-based service providers that develop and offer services through the cloud. The best example is Snowflake, which offers a cloud-based data warehouse solution that runs on AWS, Google, or Microsoft.

In the financial sector, cloud computing has drawn a lot of interest, especially as a means to boost innovation and save expenses. According to a 2022 [report by McKinsey](https://oreil.ly/KrOKg), the adoption of the cloud is on most financial institutions’ agendas. A large number of strategic partnerships have been announced between major cloud providers/service providers and financial institutions. For example, BlackRock, the largest asset manager in the world, has [partnered with Snowflake](https://oreil.ly/khbtY), a cloud data warehouse provider, to offer a cloud-based version of its investment platform Aladdin; Goldman Sachs [established a collaboration with AWS](https://oreil.ly/KhXXg) to create cloud-based data management and analytics solutions for the financial sector; JPMorgan Chase [established Fusion](https://oreil.ly/wuqCb), and State Street [created Alpha](https://oreil.ly/0ryAI), both cloud-based integrated platforms for investment and financial data management.

Migrating to the cloud can bring a large number of benefits for financial institutions. These include the following:

* Quicker time to market, facilitated by the ease with which resources can be provisioned and managed.
* More innovation as developers can test and experiment with new ideas without having to buy hardware and incur unnecessary costs.
* Continuous access to novel technologies developed by cloud providers, which would otherwise be very costly to develop in-house.
* Cost savings due to the pay-as-you-go model, where users pay only for what they use. This shifts the cost structure from fixed IT capital expenditure to variable operating costs based on demand.
* Scalability, where users can scale resources up and down based on their current and planned needs without having to purchase physical servers.
* Better collaboration as the cloud allows for easy and quick sharing of resources, files, and proof-of-concept demonstrations.
* Advanced security and data protection features such as Identity and Access Management (IAM), backups, encryption, centralized management, and audit logs.
* Cloud providers offer multiregion options for data storage and resource provisioning. This increases operational resilience as it reinforces availability. Such a feature is quite crucial for financial applications. For example, for a digital banking firm that is *branchless,* online services must always be on and available at any time of the day.
* Compliance: cloud computing’s multiregion feature allows financial institutions to pin their customer data to a specific region to meet the data privacy requirements of that location.

Logically, as with most technologies, cloud computing has its drawbacks. Examples include the following:

* Internet access, which raises the risk of access loss in case of internet or service downtime
* Lack of full control over the underlying infrastructure and data
* Security and privacy concerns
* Regulatory constraints
* Integration challenges with existing systems
* Vendor lock-in
* Unforeseen costs and consumption patterns that defy the original migration goals

# Is the Cloud Secure?

One of the major perceptions about cloud technologies is their lower degree of security compared to hosting data in-house on an on-premises infrastructure. The fundamental justification for this opinion is that shifting data to a third-party location entails giving up complete ownership and control of that data as well as opening it to the public since you are likely to access it via the internet.

Even though such concerns are rational, cloud computing isn’t that insecure. Cloud service providers make significant investments in cloud security, regularly hire security professionals, and use cutting-edge security measures. For example, in August 2023, Google [blocked a massive denial-of-service attack (DoS) on its infrastructure](https://oreil.ly/aCui1) that reached 398 million requests per second (rps). To put things in perspective, this two-minute attack generated more requests than the total amount of Wikipedia page views during the entire month of September 2023.

Nevertheless, cloud security should be carefully examined and assessed before making any major decision. I highly recommend checking the cloud vendor certifications and compliance with the different security regulations and standards for different sectors. Examples of security certifications include the following:

[ISO/IEC 27001:2022](https://oreil.ly/1SWTc):   Information security, cybersecurity, and privacy protection

[ISO/IEC 27017:2015](https://oreil.ly/CesIB):   Guidelines for information security controls applicable to the provision and use of cloud services

[ISO/IEC 27018:2019](https://oreil.ly/9qMpk):   Code of practice for protection of personally identifiable information (PII) in public clouds acting as PII processors

Cloud providers often include a comprehensive list of their compliance offerings grouped by country, sector, region, and more. Examples include the following:

* Google [compliance offerings for financial services](https://oreil.ly/wf8w2)
* AWS [compliance programs and certifications](https://oreil.ly/8vtR8)
* Microsoft [compliance offerings](https://oreil.ly/QZv90)

Additionally, most cloud providers have offerings tailored to the needs of the financial sector. Examples include IBM’s [Cloud for Financial Services](https://oreil.ly/6M6FM), Google’s [Cloud for Financial Services](https://oreil.ly/HnZ3k), [AWS’s Cloud Solutions for Financial Services](https://oreil.ly/S8hVs), [Microsoft Cloud for Financial Services](https://oreil.ly/0nkv6), and [Snowflake’s AI Data Cloud for Financial Services](https://oreil.ly/woB82). What distinguishes these cloud offerings is the focus on data protection, privacy, security, fraud detection, and several other features that financial institutions require.

To evaluate the suitability of cloud services for highly confidential financial data, Ilya Epshteyn from AWS [proposed a framework consisting of five key factors](https://oreil.ly/xMNi-), which I recommend as an example of a general guideline.

When considering a cloud migration decision, keep in mind that it must be done through a cloud migration strategy that matches your institution’s goals and requirements with what the cloud offers. Otherwise, migration efforts might easily run into unexpected issues such as excessive costs, technological limitations, security and compliance issues, scalability, and control.

A full treatment of cloud migration strategies is beyond the scope of the book.6 However, from a high-level view, a cloud strategy is, in the first place, an economic strategy.7 If moving to the cloud is going to increase your costs or not have a major impact on your costs or revenues, then it might not be worth it. Consider calculating your cloud strategy’s [return on investment (ROI)](https://oreil.ly/Qm9o2) and proceed gradually based on your analysis. For example, it might initially seem more appealing to migrate your analytical data to a cloud-based managed data warehouse service for machine learning purposes. Successively, other types of data can be migrated to a data lake, NoSQL database, and other data stores. Should this be beneficial, you might consider migrating your virtual machines and gradually the rest (or a significant part) of your infrastructure.8

Second, consider analyzing the potential impact of cloud migration on your business models and the value creation logic. For example, businesses need to get used to the idea of web-based services and delivery mechanisms, pay-per-use expenditure models, managed services, and the shared responsibility model.9

Third, consider the technological limitations of the cloud and their impact on your business needs. Cloud technologies are very powerful, but they have limitations. Some of these limitations are inherently derived from the technology itself (e.g., the connection limit in a PostgreSQL database) or cloud-related limitations, such as the shared resources model of the cloud, which might limit the amount of RAM or CPU dedicated to a virtual machine.

Fourth, your strategy must carefully assess your company’s data governance and compliance requirements to ensure you keep your system resilient and secure. Cloud services are user-friendly and relatively easy to use. But with such ease comes a challenge, which is the risk of misusing cloud services and creating chaotic architectures. This, in turn, might impact the level of control and quality of the data and infrastructure you host in the cloud.

## Criterion 4: Public Versus Private Versus Hybrid Cloud

With the adoption of cloud computing worldwide, three cloud models have emerged: public, private, and hybrid. In this section, we will explore the main features of each model and illustrate their relevance to financial institutions.

### Public cloud

In a public cloud model, the underlying infrastructure (compute, storage, networks, etc.) is owned and managed by a third-party vendor and accessible by users over the public internet. Examples of public cloud providers include Amazon Web Services, Google Cloud, Microsoft Azure, IBM Cloud, and Oracle. The public cloud is the most popular model and is often the default choice.

A key feature of the public cloud is [*multitenancy*](https://oreil.ly/T0Y0_), meaning that cloud service users share the underlying infrastructure while remaining isolated through virtualized environments. Multitenancy allows the cloud vendor to optimize the use of resources and reduce costs.

Due to multitenancy, the public cloud model advocates the *shared responsibility principle*, wherein both the cloud provider and users assume distinct yet overlapping responsibilities to safeguard the security of services and data hosted in the public cloud. The cloud provider oversees physical infrastructure security and maintains a logical separation between client data and resources. Simultaneously, clients are responsible for ensuring application-level security, such as user access and permissions, data encryption, backups, and multifactor authentication.

The main advantages of the public cloud include the following:

Simplicity:   Public cloud providers focus on making their services user-friendly to cater to the diverse needs of all sectors and clients they serve.

Flexible pricing:   Public cloud users can pay on demand while also capitalizing on discounts offered for committed usage, where they reserve a resource for a predetermined duration.

Scalability:   Cloud providers strategically plan and provision their infrastructure to accommodate variable resource needs, ensuring clients can access the necessary resources whenever needed.

Minimal configuration and maintenance burden:   The cloud provider manages and maintains the data centers hosting the physical servers.

On the negative side, the public cloud may not be ideal for the following reasons:

* Data confidentiality and security, as data is stored at a third-party location and accessed through the public internet
* Excessive costs, which may arise with large-scale applications, miscalculated resource needs, or unexpected spikes in demand
* Limited infrastructure control

Given their security and confidentiality requirements, financial institutions looking to adopt the cloud might find the public cloud the most risky option. However, the public cloud might be a good solution if used for less confidential types of data, e.g., machine learning. Among financial institutions, FinTech firms are major public cloud users, given the extra features it provides in terms of products and flexibility, which are ideal for innovation.

# Misconfiguration Risk in Public Clouds: The Capital One Data Breach Case

The most critical security threat when using public cloud services is [cloud misconfiguration](https://oreil.ly/XdBYd). Since the public cloud is built on the shared responsibility principle, customers may incorrectly set access to their resources, leaving them vulnerable to cybercriminals’ attacks. For example, a common misconfiguration happens when a resource is accidentally made public or given excessive permissions that can be easily exploited to gain access to sensitive data.

In 2019, over 100,000 social security numbers, credit card details, and client financial information were stolen as a consequence of a cloud [data breach at the US financial company Capital One](https://oreil.ly/LMLpt). The breach was possible thanks to a misconfiguration in permission settings that allowed one resource to access data stored in the storage service AWS S3 that Capital One used to store its client data. The misconfigured resource was attacked and used to gain access to client data in S3.

Cloud providers have [implemented measures to help users detect and mitigate cloud misconfiguration issues](https://oreil.ly/Ujadc). Nevertheless, if you use a public cloud service, I highly recommend that you assign primary importance to cloud misconfiguration and vulnerability risks.

### Private cloud

In the private cloud model, an organization has a dedicated cloud infrastructure that is not shared with others. The dedicated infrastructure can be owned and hosted by the organization itself, owned by the organization and hosted at a third-party vendor, or owned by the vendor and rented by the organization. The rise of the private cloud primarily stemmed from large corporations with data centers seeking to replicate the public cloud model internally.

The private cloud’s main advantages are control and security, which makes it an ideal solution for many regulated industries, such as financial services. If a financial institution builds and deploys a private cloud on its data centers, then security is the full responsibility of the institution. If a private cloud is deployed at a third-party data center, then the servers’ physical security is the cloud provider’s responsibility. In both cases, the security of the data and user access management is the responsibility of the institution.

As a main downside of the private cloud, it is considerably harder to set up and deploy, especially if managed fully by the institution in-house. The private cloud might require significant up-front investment in infrastructure and IT talent and lead to ongoing costs in terms of maintenance and personnel.

The private cloud has received considerable attention among financial institutions, which tend to favor security and compliance over other features. Large financial institutions already owning big data centers might benefit greatly from switching or adapting to a private cloud setting. For example, Bank of America invested heavily in building an internal private cloud, which, according to a [*Business Insider* article](https://oreil.ly/p-dNZ), helped save $2 billion in annual infrastructure expenditure and reduced the number of servers from 200,000 to 70,000 and its data centers from 60 to 23. This reduction was possible through the use of virtualization technologies, which led to a reduced need for servers.

As a viable and more practical alternative, cloud providers offer the option to deploy a [*Virtual Private Cloud* (VPC)](https://oreil.ly/wUnFN), which is deployed within a public cloud infrastructure. A VPC offers the best of both worlds: the private cloud’s security and reliability and the public cloud’s scalability and convenience. A VPC can allow a financial institution to isolate compute resources and network traffic for customers’ workloads that involve highly confidential data.

### Hybrid cloud

The hybrid cloud model combines public and private clouds to take advantage of both. In a hybrid setting, a private cloud is often used for operations that involve confidential data, such as client transactions and financial reporting, while the public cloud is used for high-volume and less sensitive operations, such as log analysis, machine learning, and web-based applications. The public cloud can also be dedicated to handle occasional spikes in workload from the applications running in a private cloud, a technique known as *cloud bursting*.

A hybrid cloud can be an ideal solution for financial institutions, offering the flexibility and scalability of the public cloud while ensuring regulatory compliance and security through the private cloud. Moreover, the hybrid cloud model allows for cost optimization by allocating resources and workload between public and private cloud based on demand and circumstances.

The main disadvantages of a hybrid cloud are the cost involved in building and maintaining it and the additional operational complexity that derives from the need to coordinate and orchestrate two clouds. Alternatively, a company can build a hybrid cloud via a combination of a VPC and public cloud. In this case, the maintenance burden of the private cloud is lower as the cloud vendor maintains the underlying infrastructure.

## Criterion 5: Single Versus Multi-Cloud

Multi-cloud is a cloud strategy whereby an organization uses services from multiple cloud providers.

Starting with a single cloud provider is often the default and simplest solution. This is because most cloud providers offer similar products, e.g., virtual machines, managed SQL databases, file storage, and access management. However, as new business requirements and features get added, limitations might emerge in the cloud offerings of the trusted cloud provider. A company that uses cloud provider A might discover that a database service from provider B aligns more closely with the technical and cost prerequisites of the business, thus making it a more favorable option.

### Note

The choice of a public cloud provider may depend on factors that are not necessarily technology related. For example, among large financial institutions, it is common to see a preference for Microsoft Azure cloud services. This is due to the long-standing relationship of trust and security that many companies have developed with Microsoft. When formulating a cloud migration strategy, consider an approach that encompasses trust and relationships, as well as considerations regarding offerings, technology, features, and pricing.

A multi-cloud strategy can also be more economical. For example, Google’s warehouse solution BigQuery charges the user based on the amount of bytes that their queries fetch. On the other hand, Snowflake’s data warehouse solution charges based on the duration of the query. If your queries are data-intensive but fast, then Snowflake might be more economical, while if your queries take some time but don’t fetch large amounts of data, then BigQuery might be more appealing.

Cloud pricing can be tricky and hard to understand. Before making your choice, consider carefully all costs involved in purchasing a cloud service, particularly managed database services. A large number of factors might impact costs other than the single-unit on-demand price reported on the vendor’s website. Even though the individual cost might seem low, if you can’t predict your scaling needs, costs can easily accumulate to a large sum. Additionally, pay careful attention if you decide to use cloud cost benchmarking, as it might be [misleading](https://oreil.ly/7NNOh) or biased if you don’t understand the settings or context in which they were conducted.

In some cases, multi-cloud can be a feature of a cloud-based product itself. For example, Snowflake cloud-based data warehousing relies on the principle of separation between storage and computing. This means that data can be stored and managed independently of the compute resources that are required to interact with the data. Snowflake allows clients to [choose the cloud platform (Azure, AWS, or Google) on which to deploy the Snowflake service](https://oreil.ly/nAR99). This strategy makes it more appealing for clients to use Snowflake, as their data doesn’t need to leave their cloud infrastructure of choice.

A multi-cloud strategy can mitigate the risk of vendor lock-in. The term *vendor lock-in* refers to a situation where the cost and effort needed to switch from one cloud provider to another is so high that the client is essentially stuck with the current cloud provider. Vendor lock-in may be disadvantageous in case the provider makes changes to their services, increases price, or incurs downtime issues. By adopting a multi-cloud strategy, you maintain your flexibility to adapt to changes introduced by a given provider and make use of each provider’s best features.

The main drawback of the multi-cloud strategy is the additional management and operational burden needed to maintain the resources hosted on different cloud platforms. Using two clouds means securing both and making sure access is coordinated and managed properly. Establishing a secure and private connection between multiple clouds can be both complex and expensive, often requiring intricate VPN configurations or other advanced networking solutions. Additionally, consistency and reliability checks must be implemented if data needs to be moved between clouds. Moreover, if resources hosted on different clouds become tightly coupled, this may easily increase costs, impact performance, and jeopardize maintainability.

# Case Study: Multi-Cloud Strategy at Wells Fargo

In 2021, Wells Fargo, a US multinational financial services company, [announced a new digital infrastructure strategy](https://oreil.ly/hbdy3) that uses services from two public cloud providers as well as third-party-owned data centers for private cloud and traditional hosting services.

Wells Fargo’s strategy relies predominantly on Microsoft Azure’s public cloud to drive innovation across all departments and ensure a secure and trusted environment for strategic business workloads. It uses Azure Cloud as the main foundation for most day-to-day data and analytical needs and to empower employee collaboration. However, it also leverages the Google Cloud platform for more advanced data and analytical workloads, such as artificial intelligence, and to develop personalized customer solutions.

Furthermore, Wells Fargo’s digital strategy complements its public cloud infrastructure with third-party-owned data centers, leveraging private cloud and traditional hosting services to create a secure, reliable, and flexible digital foundation.

In general, Wells Fargo’s hybrid multi-cloud architecture is viewed as a promising future trend in cloud computing since it provides the greatest flexibility for meeting business demands in terms of performance, security, cost, scalability, and innovation. To explore this trend in detail, I highly recommend the excellent work of Paul Zikopoulos, Christopher Bienko, Chris Backer, Chris Konarski, and Sai Vennam, [*Cloud Without Compromise*](https://oreil.ly/CApGt) (O’Reilly, 2021).

## Criterion 6: Monolithic Versus Modular Codebase

A major decision that companies have to make when building a data infrastructure is the organizational style of the codebase and application assets. Codebase organization style is not concerned with how the software works but rather how it is structured, linked, and deployed. Code structure can be crucial in determining the application’s readability, scalability, and reliability. To this end, two main codebase styles are often proposed, primarily *monolithic* and *modular,* which I briefly illustrate in this section.

### Monolith architecture

In a monolith architecture, the codebase is typically organized in a single location and is characterized by tight coupling between its constituent elements. As a consequence, when making a change to a monolith, it is very likely that you will have to deploy the entire application and not just the part that you changed. In its simplest state, you can think of a monolith as a single GitHub repository that stores the entire application codebase.

It is also possible to have a distributed monolith, which organizes the codebase in multiple locations, but due to tight coupling, a change in one place requires changes and redeployment of all or several of the other locations.

Monolith architectures may provide a number of advantages, such as the following:

* Ease of deployment, as you don’t deal with the pitfalls of distributed systems
* High levels of cohesion and consistency
* Simpler development workflow, as all components of the code are visible to the developer
* Easier to monitor
* Easier to test (e.g., end-to-end)
* High throughput and performance (no need to communicate with many other services)
* Simplifies code reusability (all code is in one place; use what you need!)

The monolith architecture may be ideal for simple and lightweight financial applications, both for developers and for the application’s extensibility and performance.

Nevertheless, monolith architectures may lead to a very complex and hard-to-predict application codebase, making it quite challenging to scale, extend, understand, and debug. The more components and dependencies an application has, the harder it is to understand the impact of a local change on the system’s overall behavior.