# **Enterprise Architecture and Cost Analysis: Jira Data Integration via Azure Database for PostgreSQL**

## **1\. Architectural Context and Data Footprint**

The modernization of enterprise operational systems demands highly scalable, intelligent, and compliant data architectures. When migrating and integrating substantial volumes of Jira data—comprising DevOps, operational, and resourcing metrics—from Amazon S3 into an Azure Database for PostgreSQL environment, organizations must balance infrastructural costs with advanced analytical and generative AI capabilities.  
The current data footprint establishes a critical baseline for this architectural design. The historical dataset (spanning 2022 to the present) occupies 90 GB of raw storage, containing approximately 25 million rows in the core history tables. Operational velocity dictates an anticipated growth rate of 18 GB annually, driven by a daily influx of 200,000 to 400,000 Jira interaction records. Moving this dataset into a multi-model Azure Database for PostgreSQL Flexible Server environment requires a comprehensive evaluation of ingestion economics, concurrent user performance, generative AI integration via Amazon Bedrock, regulatory compliance, and total cost of ownership (TCO).

## **2\. Data Extraction, Ingestion, and Network Economics**

The foundation of the proposed architecture relies on the efficient extraction and transfer of raw Jira data. Currently, AWS Glue is utilized to minimally transform the data extract before loading it into an Amazon S3 bucket. Transitioning this data from an Amazon Web Services (AWS) environment into a Microsoft Azure ecosystem introduces the risk of substantial data transfer (egress) fees, which must be carefully modeled.

### **AWS Glue Operations and Storage Costs**

AWS Glue operates as a serverless data integration service, billing execution time based on Data Processing Units (DPUs). Glue jobs for data preparation, including Python Shell or Apache Spark ETL jobs, are priced at $0.44 per DPU-hour, billed per second with a one-minute minimum.1 Given that the Jira dataset is minimally transformed, the compute requirements for Glue remain relatively low. A standard Spark job utilizes a minimum of 2 DPUs, resulting in an operational floor of $0.88 per hour of execution.1 For organizations utilizing the AWS Glue Data Catalog to manage schemas, the first one million objects are stored free of charge, with subsequent objects costing $1.00 per 100,000 objects monthly.1 Furthermore, AWS Glue Crawlers, which automatically infer database schemas, are also billed at $0.44 per DPU-hour.2 If an organization requires delayed execution, Glue version 3.0 offers a flexible execution model for non-urgent batch jobs that reduces costs by 34% to $0.29 per DPU-hour.3  
Amazon S3 standard storage costs remain highly predictable at $0.023 per gigabyte per month for the first 50 TB.5 The 90 GB baseline therefore incurs a negligible pure storage cost of approximately $2.07 per month. However, standard S3 internet egress pricing presents a larger financial variable and is often where cloud bills become unexpectedly expensive.7 AWS allows the first 100 GB of internet egress per month for free, aggregated across all services.9 Subsequent egress to the public internet is billed at $0.09 per gigabyte for the first 10 TB.9 With an initial transfer of 90 GB, the first bulk migration falls entirely within the free tier. The ongoing annual growth of 18 GB (approximately 1.5 GB per month) similarly remains well below the egress billing threshold, assuming no other AWS services consume the account-wide 100 GB free tier.

### **Delta Sharing as an Advanced Ingestion Mechanism**

While direct S3-to-Azure transfers via standard internet egress are mathematically cost-effective for this specific 90 GB volume, utilizing a Delta Share endpoint provides significantly superior architectural advantages for the Azure environment. Delta Sharing is an open, vendor-neutral protocol for secure data sharing that allows organizations to share live data stored in Delta Lake formats across diverse cloud providers (Azure, AWS, Google Cloud) without requiring data replication.11  
By exposing the Jira data through a Delta Share endpoint directly on S3, the data producer avoids traditional extract-and-load pipeline overhead.12 Instead of copying files over the internet, Azure Databricks or Microsoft Fabric can read this data in place.12 This avoids the large-scale data movement that typically drives cloud egress charges, as egress occurs only when the data is actively queried across clouds.12  
To completely immunize the architecture against cross-cloud query latency and recurring egress costs, the Delta Share configuration can be utilized to synchronize local replicas of the shared data into the target Azure region. By utilizing the DEEP CLONE SQL command, Azure can copy the source table data and metadata incrementally.13 Deep clones enable highly efficient incremental updates by identifying only new data in the source S3 table and refreshing the target Azure PostgreSQL database accordingly.13 This pattern severely minimizes ongoing network traffic, restricting egress solely to the daily 200,000 to 400,000 new interaction records rather than full table scans.

## **3\. Multi-Model Database Architecture: Azure Database for PostgreSQL**

Enterprise Jira datasets are notoriously complex, blending rigid transactional metadata with highly fluid, user-defined custom fields and unstructured conversational text. Azure Database for PostgreSQL Flexible Server provides a robust foundation by operating across three distinct database paradigms within a single engine, eliminating the need for polyglot persistence and fragmented data silos.

### **Relational (SQL) Capabilities**

The foundational layer utilizes standard relational tabular structures. This paradigm efficiently houses the 25 million rows of historical interaction data, optimizing aggregation queries for reporting metrics such as creation dates, predefined status transitions, assignee IDs, and resolution timestamps. The relational model ensures ACID compliance, maintaining absolute transactional integrity as the 200,000 daily records are ingested.

### **Document (NoSQL via JSONB)**

Jira issues inherently possess fluid, deeply nested schemas due to project-specific custom fields, varying issue types, and agile metadata. Traditional relational modeling would require hundreds of sparse columns or complex Entity-Attribute-Value (EAV) anti-patterns. PostgreSQL’s native JSONB data type allows the storage of raw Jira extracts as document payloads.14 This provides NoSQL flexibility while retaining robust SQL query capabilities, enabling developers to index specific JSON keys and extract operational metrics without strict schema enforcement.14 Recent updates to Azure infrastructure preserve these native PostgreSQL types—including JSON and JSONB—without requiring intermediate string encoding, ensuring full-fidelity replication of semi-structured Jira data.14

### **Vector Database (PgVector)**

To support the Generative AI interaction model, the pgvector extension facilitates the storage, indexing, and querying of high-dimensional vector embeddings.15 When unstructured Jira data (e.g., bug descriptions, acceptance criteria, resolution notes) are embedded using an AI model, pgvector allows the database to perform semantic similarity searches.15 This transforms the PostgreSQL instance into the primary retrieval engine for Retrieval-Augmented Generation (RAG) pipelines, enabling users to query the database for "issues similar to the authentication bug reported last week" based on semantic meaning rather than exact keyword matches.

## **4\. Evaluation of LLM Interaction Layers**

The architectural design requires the integration of Large Language Models—specifically Claude Sonnet 4.6 and Opus 4.6 to 4.8 via Amazon Bedrock—to interact with the PostgreSQL database. The user has requested guidance on whether to route this interaction through the Model Context Protocol (MCP), Azure Functions, or Azure Databricks. Each option presents distinct trade-offs regarding governance, latency, and cost.

### **Option A: Direct Model Context Protocol (MCP) Integration**

Anthropic’s Model Context Protocol (MCP) is an open-source standard designed to build secure, two-way connections between AI models and external data sources.16 An MCP PostgreSQL server runs as a lightweight process holding a connection pool to the database, exposing specific tools to the LLM agent, such as list\_schemas, describe\_table, and execute\_read\_only\_query.18

* **Pros:** Highly standardized, natively understood by Claude models, and eliminates the need to manually paste schemas into chat contexts.16 Security is maintained via read-only transactions.19  
* **Cons:** Pure MCP servers are mechanically simple processes. For production use, vanilla PostgreSQL MCPs lack scoped write permissions, advanced network safety perimeters, and mechanisms for non-SQL operations (like authentication and detailed logging).18

### **Option B: Azure Databricks**

Azure Databricks could serve as the intelligence layer, utilizing its own AI/BI Genie and Spark compute to handle the natural language processing before pushing queries down to PostgreSQL.

* **Pros:** Unparalleled capability for processing massive, distributed datasets. Integrates natively with Delta Sharing.12  
* **Cons:** Databricks introduces significant compute costs. For a use case focused on Natural Language to SQL generation against a 90 GB PostgreSQL database, spinning up Databricks Spark clusters represents a massive over-provisioning of resources and introduces unnecessary latency into conversational AI queries.

### **Option C: Azure Functions (Recommended Hybrid Approach)**

Azure Functions provides a serverless compute tier that can act as the orchestrator between Amazon Bedrock and the PostgreSQL database.

* **Pros:** By wrapping the MCP server logic within an Azure Function, the enterprise achieves an optimal hybrid. The Azure Function acts as a secure, event-driven middle tier that handles user authentication, API key rotation, and request logging. When a user sends a prompt, the Azure Function calls the Amazon Bedrock API, passing the MCP-formatted toolset. Claude generates the SQL, and the Azure Function executes it against PostgreSQL. This isolates the database from direct exposure to the LLM, ensuring strict enterprise governance while maintaining the low-latency benefits of serverless architecture.

## **5\. Agentic Workflows and Natural Language to SQL**

With the orchestration layer established via Azure Functions and MCP, Claude Sonnet 4.6 and Opus 4.8 can execute complex agentic workflows. Instead of merely answering questions, agentic tools allow the model to autonomously inspect the Jira schema, formulate SQL queries, execute them, read the results, and iterate if errors occur.18

### **Success Rates and Benchmarks for NL-to-SQL**

While the conceptual appeal of Natural Language to SQL (NL-to-SQL) is high, production success rates vary heavily based on the implementation methodology.

1. **Zero-Shot Prompting:** Providing a raw schema to the model yields a success rate of 70% to 85%.20 It is fast and requires no infrastructure, but it is highly prone to hallucinating non-existent columns or misunderstanding domain-specific Jira statuses.  
2. **Few-Shot \+ RAG (Retrieval-Augmented Generation):** By providing the model with a vector-indexed library of past successful queries and utilizing pgvector to retrieve similar context, the accuracy ceiling rises to 80%–90%.20  
3. **Multi-Agent/Agentic Frameworks:** Utilizing advanced reasoning models like Claude Opus 4.8 in a multi-step agentic loop—where the model writes the query, tests it against the database, reads the execution error, and rewrites it—achieves 85%–91% accuracy against complex enterprise schemas.20  
4. **Semantic Models (YAML):** Implementing an intermediate semantic layer (where business logic, relationships, and definitions are mapped in YAML files) provides the highest accuracy for BI/analytics use cases, consistently achieving a 90%+ success rate.20

Benchmarks from Microsoft and Databricks validate this progression. For instance, Databricks AI/BI Genie exhibits a mere 9.5% accuracy when operating in empty spaces with no metadata.21 However, when column descriptions and domain knowledge are added, accuracy jumps to 69.23%.21 By implementing a feedback mechanism that stores SQL patterns and joins from previous iterations, accuracy reaches 88.50%.21  
A critical caveat in NL-to-SQL benchmarks is the phenomenon of "semantic failures." Academic datasets (like Spider 1.0) often show LLMs hitting 85%+ accuracy because they measure strict syntactical correctness.20 However, in a production Jira environment, a syntactically perfect query might execute and return data, but suffer a semantic failure—for example, calculating "cycle time" by excluding weekends when the specific operational business logic requires calendar days.20 Therefore, achieving production readiness requires governing the queries the AI writes, teaching the AI the business context via a semantic layer, and providing an interface that supports iterative follow-up questions.20

## **6\. In-Database Machine Learning: Pre-Tagging Jira Hygiene and Flow**

A profound advantage of Azure Database for PostgreSQL is the azure\_ai extension, which enables the database to natively invoke large language models and machine learning services without shifting data to an external application tier.15 This capability is critical for proactively evaluating Jira Hygiene and identifying operational Flow Problems, such as high Work-In-Progress (WIP) limits.

### **Automated Entity Extraction for Jira Hygiene**

The azure\_ai.extract() function allows the database to read unstructured text within Jira tickets (e.g., descriptions, acceptance criteria, comment threads) and extract structured entities based on user-defined labels.22 By configuring the extension to communicate with an Azure OpenAI endpoint or an Azure Machine Learning custom endpoint, the database can autonomously evaluate records using generative AI.22 Authentication to these endpoints can be secured using system-assigned managed identities (SAMI) via Microsoft Entra ID, ensuring API keys are not hardcoded into the database.22  
For instance, an automated nightly SQL job can pass new Jira records through the azure\_ai.extract() function. The SQL command can prompt the model with an array of expected features, commanding the LLM to identify "missing acceptance criteria," "vague user story descriptions," or "stale status updates." The output is a structured JSONB object appended to the record, effectively "pre-tagging" the ticket for poor Jira Hygiene.22

### **Identifying Flow Problems and Bottlenecks**

Similarly, the azure\_ai.generate() and azure\_ai.is\_true() functions can be employed for advanced classification.22 azure\_ai.is\_true() evaluates the likelihood that a specific statement is true, returning a boolean value.22 An automated query can feed a Jira ticket's transition history into the function with the prompt: *"Is it true that this ticket has been bouncing between 'In Progress' and 'Code Review' for more than 5 days without resolution?"*.22  
Furthermore, azure\_ai.generate() can generate structured JSON outputs enforcing strict schemas.22 By prompting the model with the historical status transition logs of a specific epic or assignee, the AI can evaluate the likelihood of bottlenecks. If an assignee possesses a high volume of tickets in an active state, the model can generate a structured warning flag (e.g., {"flow\_problem": "High WIP", "severity": "Critical"}) directly into a designated database column.22 This transforms static Jira tracking into a proactive, AI-monitored project management engine.

## **7\. Proactive Alerting and Notification Mechanisms**

Operationalizing Jira data requires real-time alerting mechanisms to notify stakeholders of the critical flow problems and hygiene issues detected by the machine learning models, as well as monitoring the health of the database infrastructure itself.

### **Database-Driven Webhooks (pg\_net)**

The PostgreSQL pg\_net extension enables the database engine to execute asynchronous HTTP and HTTPS requests directly from SQL.23 It utilizes an unlogged queue table (net.http\_request\_queue) to manage outbound requests without incurring heavy disk I/O penalties.23  
When the aforementioned machine learning triggers detect a "High WIP" flow problem, a PostgreSQL stored procedure can use pg\_net to automatically dispatch an asynchronous HTTP POST request.23 The procedure constructs a JSON payload containing the alert details (Assignee, Ticket IDs, Severity) and posts it to an external webhook, enterprise email gateway, or Microsoft Teams channel.23 This architectural pattern eliminates the need for an external polling service or cron job to constantly query the database for new flow problems, ensuring immediate, push-based notifications.23

### **Infrastructural Monitoring via Azure Monitor**

For maintaining the operational health of the PostgreSQL instance, Azure Monitor natively tracks vital statistics such as CPU usage, Active Connections, Storage IOPS, and Backup Storage Used.24 Metrics are emitted at one-minute intervals and retained for 93 days, though charts can only display a maximum 30-day window per query.25  
Administrators can construct alert rules within the Azure Portal that trigger when thresholds are crossed—for example, if active connections exceed 90% of the maximum limit, or if disk queue lengths indicate I/O bottlenecks.26 These alerts are highly customizable, supporting automated email deliveries to service administrators, co-administrators, and custom distribution lists, or triggering external webhooks for incident response automation.26

## **8\. Concurrent User Performance Profiling**

As the user base interacting with the NL-to-SQL system scales, the Azure Database for PostgreSQL Flexible Server must be appropriately sized. A critical architectural element in this sizing is connection management.  
Each connection to a PostgreSQL instance, regardless of whether it is actively executing a query or sitting idle, consumes a substantial amount of server memory and CPU resources.28 High concurrency, particularly when connections are short-lived (less than 60 seconds), creates massive CPU spikes due to the overhead of establishing and tearing down connection processes.28 Exceeding connection limits triggers fatal errors and lock contention.28  
To handle high volumes of concurrent connections without exhausting database memory, Azure provides a built-in connection pooling solution: PgBouncer.24 PgBouncer acts as a proxy, maintaining a pool of warm connections to the database. Instead of each client opening a heavy, dedicated physical connection to the Postgres engine, they connect to PgBouncer, which multiplexes many logical client connections onto a smaller, optimized set of physical database connections.28 It is highly recommended to run PgBouncer in **transaction mode** for optimal performance under high concurrency.28  
The following analysis details the performance characteristics and compute tier recommendations across varying ranges of concurrent users querying the 25 million row dataset. By default, Azure reserves 15 connections for physical replication and monitoring, meaning the available user connections are always the maximum limit minus 15\.28

### **1 to 20 Concurrent Users**

At this highly localized scale, compute demands are minimal. A Burstable tier instance, such as the B2s (2 vCores, 4 GiB memory), natively allows up to 414 user connections.28 However, burstable instances operate on a restrictive CPU credit model; credits accumulate when usage is below a baseline and are rapidly consumed during spikes.29 Sustained analytical NL-to-SQL queries will quickly exhaust these credits, restricting the VM to baseline performance and causing severe degradation and connection timeouts.29 Furthermore, critical features like Query Performance Insights and PgBouncer cannot be enabled on Burstable tiers.28 Therefore, it is strictly recommended to utilize the General Purpose tier (e.g., D2ds\_v5 with 2 vCores, 8 GiB memory, 844 user connections) even at low user counts to ensure query predictability.28

### **21 to 40 Concurrent Users**

As concurrency doubles, analytical complexity generally increases. A General Purpose D4ds\_v5 instance (4 vCores, 16 GiB memory) provides an optimal balance.28 This configuration supports up to 1,703 user connections natively.28 At this scale, direct connections to the database remain stable, though enabling the built-in PgBouncer is recommended to optimize memory allocation for caching Jira payload data rather than managing connection overhead.28

### **41 to 60 Concurrent Users**

Approaching mid-tier enterprise utilization, the workload demands a robust memory footprint, especially if concurrent users are invoking complex AI-generated aggregate queries over 25 million rows. A Memory Optimized E4ds\_v5 (4 vCores, 32 GiB memory) or General Purpose D8ds\_v5 (8 vCores, 32 GiB memory, 3,422 user connections) is required.28 PgBouncer becomes strictly necessary in transaction mode to shield the database engine from connection churn, ensuring that the heavy NLP-generated analytical queries have dedicated compute cycles.28

### **61 to 80 Concurrent Users**

At this stage, the system is managing substantial continuous load. A General Purpose D16ds\_v5 instance (16 vCores, 64 GiB memory, 4,985 user connections) accommodates this concurrency effectively.28 The connection pooler configuration must be tuned aggressively. Microsoft advises setting the PgBouncer connection limit to a multiple of 2 to 5 times the number of vCores.28 Thus, for a 16-vCore system, the optimal physical connection pool is between 32 and 80, smoothly multiplexing the hundreds of logical client connections.28

### **80 to 100 Concurrent Users**

Heavy concurrent analytical read operations necessitate a transition to higher Memory Optimized tiers to prevent disk I/O bottlenecks. An E16ds\_v5 (16 vCores, 128 GiB memory) ensures that a significant portion of the active Jira dataset (currently 90 GB) is cached directly in RAM.28 This eliminates the latency of disk retrieval, drastically accelerating the response time of agentic AI workflows that rapidly interrogate the database schema and data tables. To optimize disk operations, administrators should tune parameters like effective\_io\_concurrency (setting it to 200 for SSD storage) to allow PostgreSQL to issue parallel I/O requests.31

### **100 to 450 Concurrent Users**

Operating at a massive enterprise scale with up to 450 concurrent analytical users querying 25 million rows requires significant infrastructural investment. The system will face intense CPU and memory strain. A General Purpose D48ds\_v5 (48 vCores, 192 GiB memory) or a Memory Optimized E32ds\_v5 (32 vCores, 256 GiB memory) is strictly required.28  
At this tier, PgBouncer is mandatory. While the max\_connections parameter natively supports up to 4,985 user connections on these sizes 28, attempting to hold 450 active, simultaneous analytical queries without a connection pooler will result in CPU starvation and out-of-memory errors. The underlying SSD storage must also be upgraded to Azure Premium SSD v2. Premium SSD v2 allows administrators to decouple capacity from performance, provisioning up to 80,000 IOPS and 1,200 MB/s throughput independently of the storage volume size to handle the immense disk reading requirements of simultaneous aggregations.32

## **9\. Business Intelligence Integration: Microsoft Fabric and Power BI**

To democratize data access and ensure maximum ease of use for non-technical business stakeholders, the architecture deeply integrates with Microsoft Fabric and Power BI, allowing users to build visual dashboards alongside the conversational LLM interfaces.

### **Microsoft Fabric Mirroring**

Microsoft Fabric introduces "Mirroring," a zero-ETL, low-latency turnkey solution that continuously replicates the Azure Database for PostgreSQL flexible server directly into Fabric OneLake.34 When configured in the Azure Portal, a background PostgreSQL process creates an initial snapshot of the selected tables and ships it to the OneLake landing zone in Parquet format.34 Subsequent transactional changes in the Jira database are continuously captured and streamed in batches, converting them into Delta tables.34  
This mirroring process operates efficiently; the background Fabric compute used to replicate the data into OneLake is free and does not consume the organization's standard Fabric capacity units.35 Crucially, recent updates to Fabric Mirroring preserve PostgreSQL-native data types, including JSON and JSONB.14 This ensures that the highly nested Jira operational data is replicated with full fidelity, without requiring intermediate schema transformations or error-prone string encoding.14

### **Power BI: Import vs. DirectQuery**

Once mirrored into Fabric, the data is instantly available to Power BI for enterprise reporting. When connecting Power BI to PostgreSQL or Fabric, organizations must choose between Import mode and DirectQuery mode.

1. **DirectQuery Mode:** This method queries the database in real-time without storing data in the Power BI model.36 While ideal for real-time visibility on massive datasets, DirectQuery suffers from significant performance degradation during complex transformations, lacks support for query caching, and restricts date-time granularity to seconds rather than milliseconds.39 Most critically, it imposes a hard limit of one million rows returned per query.39  
2. **Import Mode:** Microsoft's official guidance highly recommends Import mode for enterprise reporting scenarios.39 In this mode, the data is loaded directly into Power BI’s highly optimized VertiPaq in-memory engine.36 Although data is not strictly real-time, scheduled refreshes can easily handle the daily growth of 200,000 to 400,000 Jira records. Import mode provides drastically superior performance, enables complex DAX (Data Analysis Expressions) calculations, allows for cross-table modeling, and gracefully handles the entire 25 million row dataset without query timeouts or row-limit truncation.36 For business users, Import mode ensures dashboards load instantly, maximizing ease of use.

## **10\. Regulatory Compliance: FINRA 4511 Controls**

For financial institutions and large enterprises subject to regulatory oversight, Financial Industry Regulatory Authority (FINRA) Rule 4511, aligned with SEC Rule 17a-4, governs recordkeeping.40 The rule mandates that electronic records, including digital communications and AI-generated content used in decision-making, must be preserved for a default retention period of six years.40 Crucially, these records must be stored in an immutable, write-once-read-many (WORM) format, ensuring they are protected from alteration or deletion, and they must be highly searchable and auditable for regulatory requests.40

### **Implementing an Immutable JSONL Worklog**

To achieve FINRA 4511 compliance within Azure Database for PostgreSQL, the system must capture a comprehensive audit trail of all Jira interactions (inserts, updates, deletes) without allowing any subsequent alteration of the log.43 Regulators do not accept audit logs that can be edited after the fact.45  
The architecture fulfills this requirement by establishing a specialized audit\_log table combined with row-level security and restricted database triggers. The audit table is designed to store the precise state of a record before and after modification using JSON, which can be easily extracted in JSONL (JSON Lines) format for regulators.43 The table captures the operation type, timestamp, user ID, and the raw old\_data and new\_data in JSONB format.43  
To populate this table securely, a generic audit trigger function is bound to the Jira data tables.43 This function is created with SECURITY DEFINER privileges.46 Unlike standard triggers that run with the permissions of the invoking user, a SECURITY DEFINER function runs with the privileges of the user who *created* it (typically a highly restricted daemon role).46 This allows the trigger to write to the audit\_log even if the user modifying the Jira ticket does not have write access to the audit table.  
To satisfy the "immutable" requirement, the audit\_log table is placed under strict access control. A PostgreSQL CHECK constraint or a specialized INSTEAD OF trigger is applied to explicitly reject any UPDATE or DELETE commands directed at the audit table.44 Even database administrators lack the basic SQL permissions to alter the historical record.44 This cryptographically secure, append-only architecture ensures that every Jira metadata change is captured accurately, enabling the organization to generate compliant JSONL exports for regulators upon request.44

## **11\. Copilot Ecosystem Integration**

The ease of use for both business users and technical developers is further enhanced through integrations with Microsoft and GitHub Copilot ecosystems, abstracting complex SQL into conversational interfaces.

### **Microsoft 365 Copilot Integration**

Business users can interact with the Jira data directly from their daily workspace using the PostgreSQL Microsoft 365 Copilot connector.47 This connector securely indexes records from the PostgreSQL database using a customized SQL query.47

* **Mechanism:** A Microsoft Graph Connector Agent (which must be updated to version 3.1.5.0 or later) facilitates the connection from the on-premises or cloud network to Microsoft 365\.47 To prevent database overload, the connector utilizes a watermarking column (e.g., a timestamp) to perform incremental crawls every 15 minutes, with full crawls daily.47  
* **Security and Limits:** The connector strictly enforces record-level permissions by mapping SQL query-defined Access Control Lists (ACLs) via User Principal Names (UPN), Microsoft Entra IDs, or Active Directory Security IDs, ensuring users only retrieve Jira data they are authorized to view.47 It is designed exclusively for Online Transaction Processing (OLTP) workloads; analytical queries that take longer than 40 seconds to execute are unsupported.47 The connector is currently in preview, requiring the tenant's AI Administrator to enable the Targeted Release ring.47

### **GitHub Copilot Integration**

For developers and data engineers, the PostgreSQL extension for Visual Studio Code integrates natively with GitHub Copilot.48 Utilizing "Agent Mode," Copilot can autonomously connect to the database, visualize complex schema relationships, perform bulk CSV loads, and analyze execution plans.48 Developers can utilize natural language prompts in the Copilot chat to generate complex DAX or SQL queries, dramatically accelerating the development of the underlying views that power the Power BI dashboards.49

## **12\. Total Cost of Ownership (TCO) and Pricing Analysis**

A robust understanding of the pricing dynamics across AWS, Azure, and Amazon Bedrock is essential for accurate FinOps modeling. The following cost estimates operate on the assumption of a large enterprise utilizing on-demand and pay-as-you-go pricing (Amazon and Azure market rates for 2026).

### **A. Data Ingestion and Transformation Costs (AWS)**

The costs associated with keeping data synchronized from AWS to Azure depend heavily on the extraction method.

| Service Component | Metric | Estimated Cost / Unit | Notes |
| :---- | :---- | :---- | :---- |
| **AWS Glue ETL** | DPU-Hour | $0.44 | Minimum 2 DPUs per Spark job, billed per second (1-minute min).1 Flex execution reduces this to $0.29.4 |
| **AWS Glue Data Catalog** | Objects Stored | $1.00 per 100k \> 1M | First 1 million objects are free.1 |
| **Amazon S3 Storage** | GB / Month | $0.023 | Approx. $2.07/mo for the 90 GB baseline.5 |
| **AWS S3 Internet Egress** | GB / Month | $0.09 | First 100 GB is free. Egress scales dynamically as extraction size grows, peaking at $90 per TB.9 |
| **Delta Sharing Egress** | Transfer | Variable | Bypasses S3 egress entirely if read locally via Databricks in-region, minimizing transfer penalties.11 |

### **B. Generative AI Token Costs (Amazon Bedrock)**

Interacting with the PostgreSQL database using Bedrock's Claude models introduces token-based consumption costs. The model choice significantly influences the budget.

| Model Version | Input Tokens (Per 1 Million) | Output Tokens (Per 1 Million) | Use Case Alignment & Notes |
| :---- | :---- | :---- | :---- |
| **Claude Sonnet 4.6** | $3.00 | $15.00 | Standard NL-to-SQL generation, data extraction tasks, and general conversational analytics.52 |
| **Claude Opus 4.8** | $6.00 | $25.00 | High-complexity multi-agent reasoning, deep schema contextualization, and intricate logic verification.55 |
| **Claude Opus 4.8 (Cache Read)** | $0.60 | N/A | Substantial 90% discount when leveraging prompt caching for recurring database schema context.55 |
| **Batch Processing** | 50% Discount | 50% Discount | Batch discounts apply across all models for non-urgent analytics.52 |

*Cost Extrapolation Example:* If a business workflow generates 2,000 input tokens (schema definitions, instructions) and 500 output tokens (SQL queries) per interaction using Claude Sonnet 4.6, the cost per interaction is approximately $0.0135.54 Across 450 users querying the database 10 times daily, the monthly LLM expenditure would be roughly $1,800. Utilizing Claude Opus 4.8 with prompt caching for the schema definitions can dramatically increase accuracy while keeping input costs contained.

### **C. Database Infrastructure Costs (Azure PostgreSQL Flexible Server)**

The cost of Azure Database for PostgreSQL scales dramatically based on the compute tier selected to support the required concurrent user load.

| User Concurrency Target | Suggested Compute Tier | vCores | Memory | Estimated Monthly Cost (Pay-As-You-Go) | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **1 to 20 Users** | General Purpose (D2ds\_v5) | 2 | 8 GiB | \~$140 \- $150 | Burstable tiers ($12-$99) are heavily discouraged for production.29 |
| **21 to 40 Users** | General Purpose (D4ds\_v5) | 4 | 16 GiB | \~$280 \- $300 | Requires PgBouncer activation for stability.28 |
| **41 to 80 Users** | General Purpose (D16ds\_v6) | 16 | 64 GiB | $1,308.16 | Ideal for sustained NL-to-SQL aggregation queries.57 |
| **80 to 150 Users** | General Purpose (D32ds\_v6) | 32 | 128 GiB | $2,616.32 | 3-year reserved instances offer \~60% savings ($1,046.30/mo).57 |
| **150 to 450 Users** | General Purpose (D64ds\_v6) | 64 | 256 GiB | $5,232.64 | 3-year reserved instance reduces cost to $2,092.59/mo.57 |

*Note: Storage costs on Azure are billed separately based on provisioned capacity and IOPS for Premium SSD v2. The 90 GB dataset will incur minor storage capacity charges, but organizations must budget for the provisioned IOPS required to support 450 concurrent users.*  
By meticulously configuring Azure Functions to govern MCP interactions, leveraging deep clones via Delta Sharing to eliminate S3 egress, and sizing the PostgreSQL instance properly with PgBouncer, the enterprise can deliver a highly intelligent, FINRA-compliant, generative AI-powered operational system at a predictable and optimized cost.

#### **Works cited**

1. AWS Glue Pricing 2026: ETL Jobs, Data Catalog, and Crawlers | Wring Blog, accessed July 10, 2026, [https://www.wring.co/blog/aws-glue-pricing-guide](https://www.wring.co/blog/aws-glue-pricing-guide)  
2. AWS Glue Pricing, accessed July 10, 2026, [https://aws.amazon.com/glue/pricing/](https://aws.amazon.com/glue/pricing/)  
3. AWS Glue Pricing: How Much Does AWS Glue Really Cost in 2026 | Integrate.io, accessed July 10, 2026, [https://www.integrate.io/blog/aws-glue-pricing/](https://www.integrate.io/blog/aws-glue-pricing/)  
4. AWS Glue Pricing Breakdown: The Comprehensive Guide for 2025 \- Cloudchipr, accessed July 10, 2026, [https://cloudchipr.com/blog/aws-glue-pricing](https://cloudchipr.com/blog/aws-glue-pricing)  
5. Amazon S3 pricing \- AWS, accessed July 10, 2026, [https://aws.amazon.com/s3/pricing/](https://aws.amazon.com/s3/pricing/)  
6. AWS S3 Pricing in 2026: What You'll Actually Pay \- Filebase, accessed July 10, 2026, [https://filebase.com/blog/aws-s3-pricing-in-2026-what-youll-actually-pay/](https://filebase.com/blog/aws-s3-pricing-in-2026-what-youll-actually-pay/)  
7. AWS S3 pricing in 2026: complete breakdown \- Nubbo, accessed July 10, 2026, [https://nubbo.app/blog/aws-s3-pricing-2026/](https://nubbo.app/blog/aws-s3-pricing-2026/)  
8. AWS S3 Pricing Guide: Mastering Cloud Storage Costs in 2026 \- Hyperglance, accessed July 10, 2026, [https://www.hyperglance.com/blog/aws-s3-pricing-guide/](https://www.hyperglance.com/blog/aws-s3-pricing-guide/)  
9. AWS Data Transfer & Egress Pricing Explained (2026) | EgressCost.com, accessed July 10, 2026, [https://egresscost.com/aws/](https://egresscost.com/aws/)  
10. S3 Egress Cost | Calculator, Tiered Rates, and Reduction Strategies | Usage.ai, accessed July 10, 2026, [https://www.usage.ai/blogs/s3-egress-cost/](https://www.usage.ai/blogs/s3-egress-cost/)  
11. Monitor and manage OpenSharing egress costs (for providers) | Databricks on AWS, accessed July 10, 2026, [https://docs.databricks.com/aws/en/opensharing/manage-egress](https://docs.databricks.com/aws/en/opensharing/manage-egress)  
12. Databricks Delta Sharing: Enabling Cost Efficient Cross Cloud Data Access, accessed July 10, 2026, [https://techcommunity.microsoft.com/blog/azurearchitectureblog/databricks-delta-sharing-enabling-cost-efficient-cross-cloud-data-access/4511400](https://techcommunity.microsoft.com/blog/azurearchitectureblog/databricks-delta-sharing-enabling-cost-efficient-cross-cloud-data-access/4511400)  
13. Monitor and manage OpenSharing egress costs (for providers) \- Azure Databricks, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/databricks/opensharing/manage-egress](https://learn.microsoft.com/en-us/azure/databricks/opensharing/manage-egress)  
14. General Availability Refresh: Mirroring Azure Database for PostgreSQL in Microsoft Fabric, accessed July 10, 2026, [https://techcommunity.microsoft.com/blog/adforpostgresql/general-availability-refresh-mirroring-azure-database-for-postgresql-in-microsof/4511726](https://techcommunity.microsoft.com/blog/adforpostgresql/general-availability-refresh-mirroring-azure-database-for-postgresql-in-microsof/4511726)  
15. From data to insights: Enhancing PostgreSQL with Azure AI extensions \- Medium, accessed July 10, 2026, [https://medium.com/data-science-at-microsoft/from-data-to-insights-enhancing-postgresql-with-azure-ai-extensions-8d2ad477bf5f](https://medium.com/data-science-at-microsoft/from-data-to-insights-enhancing-postgresql-with-azure-ai-extensions-8d2ad477bf5f)  
16. Connect Claude Code to tools via MCP, accessed July 10, 2026, [https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)  
17. Introducing the Model Context Protocol \- Anthropic, accessed July 10, 2026, [https://www.anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol)  
18. Claude Code Postgres MCP in 2026: Connect, Query, and Ship a Real Backend \- Totalum, accessed July 10, 2026, [https://www.totalum.app/blog/claude-code-postgres-mcp-2026](https://www.totalum.app/blog/claude-code-postgres-mcp-2026)  
19. I built a read-only Postgres MCP server — would love feedback (and for someone to try breaking it), accessed July 10, 2026, [https://www.reddit.com/r/mcp/comments/1tvijqq/i\_built\_a\_readonly\_postgres\_mcp\_server\_would\_love/](https://www.reddit.com/r/mcp/comments/1tvijqq/i_built_a_readonly_postgres_mcp_server_would_love/)  
20. Natural Language to SQL: The Complete 2026 Guide \- BlazeSQL AI, accessed July 10, 2026, [https://www.blazesql.com/blog/natural-language-to-sql](https://www.blazesql.com/blog/natural-language-to-sql)  
21. SQL query generation from natural language \- ISE Developer Blog, accessed July 10, 2026, [https://devblogs.microsoft.com/ise/llm-sql-query-generation/](https://devblogs.microsoft.com/ise/llm-sql-query-generation/)  
22. azure\_ai Extension in Azure Database for PostgreSQL flexible ..., accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/azure-ai/generative-ai-azure-overview](https://learn.microsoft.com/en-us/azure/postgresql/azure-ai/generative-ai-azure-overview)  
23. GitHub \- supabase/pg\_net: A PostgreSQL extension that enables asynchronous (non-blocking) HTTP/HTTPS requests with SQL, accessed July 10, 2026, [https://github.com/supabase/pg\_net](https://github.com/supabase/pg_net)  
24. Flexible server performance \- Microsoft Q\&A, accessed July 10, 2026, [https://learn.microsoft.com/en-us/answers/questions/2119423/flexible-server-performance](https://learn.microsoft.com/en-us/answers/questions/2119423/flexible-server-performance)  
25. Monitor using Metrics and Logs in Azure Database for PostgreSQL flexible server, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/monitor/concepts-monitoring](https://learn.microsoft.com/en-us/azure/postgresql/monitor/concepts-monitoring)  
26. Configure alerts \- Azure Cosmos DB for PostgreSQL \- Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/howto-alert-on-metric](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/howto-alert-on-metric)  
27. Configure alerts \- Azure portal \- Azure Database for PostgreSQL | Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/monitor/how-to-alert-on-metrics](https://learn.microsoft.com/en-us/azure/postgresql/monitor/how-to-alert-on-metrics)  
28. Limits in Azure Database for PostgreSQL flexible server \- Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-limits](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-limits)  
29. Compute options in Azure Database for PostgreSQL flexible server \- Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-compute](https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-compute)  
30. Confused why PostgreSQL flexible server is so expensive vs running own on digitalocean droplet. : r/AZURE \- Reddit, accessed July 10, 2026, [https://www.reddit.com/r/AZURE/comments/14vl9mo/confused\_why\_postgresql\_flexible\_server\_is\_so/](https://www.reddit.com/r/AZURE/comments/14vl9mo/confused_why_postgresql_flexible_server_is_so/)  
31. How to Tune Performance Parameters in Azure Database \- OneUptime, accessed July 10, 2026, [https://oneuptime.com/blog/post/2026-02-16-how-to-tune-performance-parameters-in-azure-database-for-postgresql-flexible-server/view](https://oneuptime.com/blog/post/2026-02-16-how-to-tune-performance-parameters-in-azure-database-for-postgresql-flexible-server/view)  
32. Plan Azure Database for PostgreSQL flexible server Deployments for Operational Performance \- Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-optimal-performance](https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-optimal-performance)  
33. Storage options \- Azure Database for PostgreSQL, accessed July 10, 2026, [https://docs.azure.cn/en-us/postgresql/compute-storage/concepts-storage](https://docs.azure.cn/en-us/postgresql/compute-storage/concepts-storage)  
34. Mirroring in Microsoft Fabric \- Azure Database for PostgreSQL ..., accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/integration/concepts-fabric-mirroring](https://learn.microsoft.com/en-us/azure/postgresql/integration/concepts-fabric-mirroring)  
35. Mirroring \- Microsoft Fabric, accessed July 10, 2026, [https://learn.microsoft.com/en-us/fabric/mirroring/overview](https://learn.microsoft.com/en-us/fabric/mirroring/overview)  
36. Power BI Import vs Direct Query: Which Should You Use? \- New Horizons, accessed July 10, 2026, [https://www.newhorizons.com/resources/blog/power-bi-import-vs-direct-query](https://www.newhorizons.com/resources/blog/power-bi-import-vs-direct-query)  
37. Should I use DirectQuery or Import Option? \- Microsoft Fabric Community \- Power BI forums, accessed July 10, 2026, [https://community.powerbi.com/t5/Power-Query/Should-I-use-Power-Query-or-Import-Option/td-p/2016325](https://community.powerbi.com/t5/Power-Query/Should-I-use-Power-Query-or-Import-Option/td-p/2016325)  
38. DirectQuery in Power BI: When to Use, Limitations, Alternatives \- Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-directquery-about](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-directquery-about)  
39. Power BI DirectQuery vs. Import Mode: Differences, Limitations \- AtScale, accessed July 10, 2026, [https://www.atscale.com/blog/power-bi-direct-query-vs-import-mode/](https://www.atscale.com/blog/power-bi-direct-query-vs-import-mode/)  
40. What is FINRA Rule 4511? A 2026 Guide | Concentric AI, accessed July 10, 2026, [https://concentric.ai/finra-4511-compliance-with-concentric-ai/](https://concentric.ai/finra-4511-compliance-with-concentric-ai/)  
41. FINRA Rule 4511: Recordkeeping Requirements & Compliance Guide \- Smarsh, accessed July 10, 2026, [https://www.smarsh.com/regulations/finra-rule-4511/](https://www.smarsh.com/regulations/finra-rule-4511/)  
42. FINRA Compliance Solution for all data sources \- ZL Tech, accessed July 10, 2026, [https://www.zlti.com/regulations/finra-compliance/](https://www.zlti.com/regulations/finra-compliance/)  
43. How to Implement Audit Trails with Triggers in PostgreSQL \- OneUptime, accessed July 10, 2026, [https://oneuptime.com/blog/post/2026-01-25-postgresql-audit-trails-triggers/view](https://oneuptime.com/blog/post/2026-01-25-postgresql-audit-trails-triggers/view)  
44. Immutable Audit Logs in PostgreSQL with Pgcli \- hoop.dev, accessed July 10, 2026, [https://hoop.dev/blog/immutable-audit-logs-in-postgresql-with-pgcli](https://hoop.dev/blog/immutable-audit-logs-in-postgresql-with-pgcli)  
45. Financial Compliance: Audit Trail Guide | Velt June 2026, accessed July 10, 2026, [https://velt.dev/blog/financial-audit-trail-compliance-guide](https://velt.dev/blog/financial-audit-trail-compliance-guide)  
46. Is there a way to disable updates/deletes but still allow triggers to perform them?, accessed July 10, 2026, [https://stackoverflow.com/questions/17886529/is-there-a-way-to-disable-updates-deletes-but-still-allow-triggers-to-perform-th](https://stackoverflow.com/questions/17886529/is-there-a-way-to-disable-updates-deletes-but-still-allow-triggers-to-perform-th)  
47. PostgreSQL connector for Microsoft Search \- Microsoft 365 Copilot ..., accessed July 10, 2026, [https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/postgresql-connector](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/postgresql-connector)  
48. Copilot Tools Reference for the PostgreSQL Extension for Visual Studio Code \- Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/development/vs-code-extension/reference/copilot-tools](https://learn.microsoft.com/en-us/azure/postgresql/development/vs-code-extension/reference/copilot-tools)  
49. New PostgreSQL extension for VS Code with GitHub Copilot Capabilities for PostgreSQL \- YouTube, accessed July 10, 2026, [https://www.youtube.com/watch?v=iF68qNT\_zAs](https://www.youtube.com/watch?v=iF68qNT_zAs)  
50. Copilot Integration \- PostgreSQL extension for Visual Studio Code | Microsoft Learn, accessed July 10, 2026, [https://learn.microsoft.com/en-us/azure/postgresql/development/vs-code-extension/copilot-integration](https://learn.microsoft.com/en-us/azure/postgresql/development/vs-code-extension/copilot-integration)  
51. S3 Pricing Comparison (2026): AWS, Azure & 20+ S3 Storage Providers, accessed July 10, 2026, [https://www.s3compare.io/](https://www.s3compare.io/)  
52. Pricing \- Claude Platform Docs, accessed July 10, 2026, [https://platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing)  
53. AWS Bedrock Pricing 2026: Claude, Llama, and Mistral Costs \- PE Collective, accessed July 10, 2026, [https://pecollective.com/tools/aws-bedrock-pricing/](https://pecollective.com/tools/aws-bedrock-pricing/)  
54. AWS Bedrock Pricing Explained: What You'll Actually Pay in 2026 \- Medium, accessed July 10, 2026, [https://medium.com/@aiengineeringonaws/aws-bedrock-pricing-explained-what-youll-actually-pay-in-2026-39377a27cdbd](https://medium.com/@aiengineeringonaws/aws-bedrock-pricing-explained-what-youll-actually-pay-in-2026-39377a27cdbd)  
55. Amazon Bedrock Pricing \- AWS, accessed July 10, 2026, [https://aws.amazon.com/bedrock/pricing/](https://aws.amazon.com/bedrock/pricing/)  
56. Claude On AWS: Bedrock Vs. Claude Platform Costs Compared (2026) \- CloudZero, accessed July 10, 2026, [https://www.cloudzero.com/blog/claude-on-aws-bedrock/](https://www.cloudzero.com/blog/claude-on-aws-bedrock/)  
57. Pricing \- Azure Database for PostgreSQL Flexible Server, accessed July 10, 2026, [https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/](https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/)  
58. Azure Database for PostgreSQL Pricing Details, accessed July 10, 2026, [https://www.azure.cn/en-us/pricing/details/postgresql/](https://www.azure.cn/en-us/pricing/details/postgresql/)  
59. Pricing \- Azure Database for PostgreSQL Flexible Server, accessed July 10, 2026, [https://azure.microsoft.com/en-in/pricing/details/postgresql/flexible-server/](https://azure.microsoft.com/en-in/pricing/details/postgresql/flexible-server/)