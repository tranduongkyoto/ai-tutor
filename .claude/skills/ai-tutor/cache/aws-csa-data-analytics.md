# Data & Analytics - AWS CSA Content Cache

## Services & Concepts

### Amazon Athena
- **Serverless** query service to analyze data stored in Amazon S3
- Uses standard SQL language (built on Presto)
- Supports: CSV, JSON, ORC, Avro, Parquet
- Pricing: **$5.00 per TB of data scanned**
- Commonly paired with Amazon QuickSight for reporting/dashboards
- Use cases: BI/analytics/reporting, query VPC Flow Logs, ELB Logs, CloudTrail trails
- Federated Query: run SQL across relational, non-relational, object, and custom data sources (AWS or on-premises) using Lambda-based Data Source Connectors; results stored back in S3

### Amazon Redshift
- Based on PostgreSQL but **OLAP** (not OLTP) — data warehousing
- **10x** better performance than other data warehouses; scales to **PBs** of data
- Columnar storage + parallel query engine
- Two modes: **Provisioned cluster** or **Serverless cluster**
- SQL interface; integrates with QuickSight, Tableau
- vs Athena: faster queries/joins/aggregations thanks to indexes
- **Cluster architecture**: Leader Node (query planning, results aggregation) + Compute Nodes (execute queries, send results to leader); accessed via JDBC/ODBC
- **Redshift Spectrum**: query data already in S3 without loading it; requires an existing Redshift cluster; query submitted to thousands of Spectrum nodes
- **Snapshots**: point-in-time backups stored in S3, incremental; restore creates a new cluster
  - Automated: every 8 hours, every 5 GB, or on schedule; retention 1–35 days
  - Manual: retained until deleted
  - Cross-region copy: configure automatic copy of snapshots to another AWS Region
- Multi-AZ mode available for some clusters
- **Loading data best practices**: large inserts far better than small ones
  - Via Kinesis Data Firehose (through S3 copy)
  - Via S3 COPY command (without Enhanced VPC Routing = over internet; with = through VPC)
  - Via EC2 JDBC driver (write in batches)

### Amazon OpenSearch Service
- Successor to Amazon ElasticSearch
- **Search any field, even partial matches** (unlike DynamoDB which only queries by primary key/index)
- Typically used as a complement to another database
- Two modes: **managed cluster** or **serverless cluster**
- Does **not** natively support SQL (can enable via plugin)
- Ingestion from: Kinesis Data Firehose, AWS IoT, CloudWatch Logs
- Security: Cognito & IAM, KMS encryption, TLS
- Includes **OpenSearch Dashboards** for visualization

### Amazon EMR
- "Elastic MapReduce" — creates Hadoop clusters (Big Data) on hundreds of EC2 instances
- Bundled with: Apache Spark, HBase, Presto, Flink
- Handles provisioning, configuration, auto-scaling; integrates with Spot instances
- Use cases: data processing, machine learning, web indexing, big data
- **Node types**:
  - Master Node: manage cluster, coordinate, manage health — long running
  - Core Node: run tasks and store data — long running
  - Task Node (optional): run tasks only — typically Spot instances
- **Purchasing options**: On-demand (reliable), Reserved (min 1 year, auto-used if available), Spot (cheaper, can be terminated)
- Can be long-running cluster or transient (temporary) cluster

### Amazon QuickSight
- **Serverless**, ML-powered BI service for interactive dashboards
- Fast, auto-scalable, embeddable; **per-session pricing**
- In-memory computation via **SPICE engine** when data is imported
- Enterprise edition: **Column-Level Security (CLS)**
- **Data sources (AWS)**: RDS, Aurora, Redshift, Athena, S3, OpenSearch, Timestream
- **Data sources (SaaS)**: Salesforce, Jira
- **Data sources (imports)**: XLSX, CSV, JSON, TSV, ELF & CLF log formats
- **On-premises**: databases via JDBC (e.g., Teradata)
- **Dashboard vs Analysis**:
  - Users (standard) and Groups (enterprise) exist within QuickSight — NOT in IAM
  - Dashboard = read-only snapshot of an analysis; preserves filtering, parameters, controls, sort
  - Must publish dashboard before sharing
  - Users who see dashboard can also see underlying data

### AWS Glue
- **Managed ETL** (extract, transform, load) service; **fully serverless**
- Prepares and transforms data for analytics
- **Glue Data Catalog**: central metadata repository (databases + table metadata)
  - Populated by Glue Data Crawler scanning S3, RDS, DynamoDB, JDBC sources
  - Used by Athena, Redshift Spectrum, EMR for data discovery
- **Glue ETL Jobs**: transform data (e.g., CSV → Parquet) and load to destinations
- **Glue Job Bookmarks**: prevent re-processing old data
- **Glue DataBrew**: clean and normalize data using pre-built transformations (no code)
- **Glue Studio**: GUI to create, run, and monitor ETL jobs
- **Glue Streaming ETL**: built on Apache Spark Structured Streaming; compatible with Kinesis Data Streams, Kafka, MSK

### AWS Lake Formation
- Fully managed service to set up a **data lake** (central analytics store) in days
- Built on top of AWS Glue
- Automates: collecting, cleansing, moving, cataloging, de-duplicating (ML Transforms)
- Combines structured and unstructured data
- Out-of-the-box source blueprints: S3, RDS, Relational & NoSQL DB
- **Fine-grained Access Control**: row and column-level security; centralized permissions
- Architecture: Data Sources → Lake Formation (source crawlers + ETL + data catalog + security/access control) → Data Lake (stored in S3) → consumed by Athena, Redshift, EMR, Spark

### Amazon Managed Service for Apache Flink
- Previously: Kinesis Data Analytics for Apache Flink
- Flink (Java, Scala, or SQL) framework for processing data streams
- Managed cluster on AWS: provisioned compute, parallel computation, auto-scaling
- Application backups via checkpoints and snapshots
- Sources: **Kinesis Data Streams**, **Amazon MSK (Apache Kafka)**
- **Important: Flink does NOT read from Amazon Data Firehose**

### Amazon MSK (Managed Streaming for Apache Kafka)
- Alternative to Amazon Kinesis; fully managed Apache Kafka on AWS
- Creates/manages Kafka broker nodes and Zookeeper nodes
- Deployed in VPC, **multi-AZ (up to 3)** for HA
- Automatic recovery from common Kafka failures
- Data stored on EBS volumes **indefinitely** (as long as you want)
- **MSK Serverless**: no capacity management; auto-provisions and scales compute & storage
- **MSK Consumers**: Kinesis Data Analytics for Apache Flink, AWS Glue Streaming ETL (Spark Streaming), Lambda, EC2/ECS/EKS applications

---

## Key Configurations

- **Athena file size**: use files > 128 MB to minimize overhead
- **Athena partitioning**: `s3://bucket/table/<PARTITION_COL>=<VALUE>/` — enables virtual column querying
- **Athena compression**: bzip2, gzip, lz4, snappy, zlip, zstd
- **Athena federated query connectors**: ElastiCache, DocumentDB, DynamoDB, Redshift, HBase in EMR, Aurora, SQL Server, MySQL, on-premises databases
- **Redshift snapshot retention**: automated snapshots 1–35 days; manual retained until deleted
- **Redshift automated snapshots trigger**: every 8 hours OR every 5 GB of changes
- **QuickSight SPICE**: in-memory engine only active when data is imported (not live connections)
- **QuickSight users/groups**: exist only within QuickSight — not IAM users
- **MSK message size**: 1 MB default; configurable higher (e.g., 10 MB)
- **Kinesis Data Streams message size**: 1 MB hard limit
- **MSK multi-AZ**: up to 3 AZs

---

## Architectural Patterns

### Serverless Analytics Stack
- IoT Devices → Kinesis Data Streams → Kinesis Data Firehose (every ~1 min) → S3 (ingestion bucket) → SQS (optional) → Lambda → Athena → S3 (reporting bucket) → QuickSight / Redshift Serverless

### Big Data ETL Pipeline
- S3 / RDS (CSV source) → Glue ETL Job (converts to Parquet) → S3 (output) → Athena (SQL analysis)
- Trigger options: S3 event notification → Lambda → trigger Glue job; or EventBridge

### OpenSearch + DynamoDB Pattern
- CRUD → DynamoDB Table → DynamoDB Stream → Lambda → OpenSearch
- API: retrieve items from DynamoDB; search items via OpenSearch

### OpenSearch + CloudWatch Logs
- Real-time: CloudWatch Logs → Subscription Filter → Lambda (AWS-managed) → OpenSearch
- Near real-time: CloudWatch Logs → Subscription Filter → Kinesis Data Firehose → OpenSearch

### OpenSearch + Kinesis
- Near real-time: Kinesis Data Streams → Kinesis Data Firehose (+ Lambda data transformation) → OpenSearch
- Real-time: Kinesis Data Streams → Lambda → OpenSearch

### Lake Formation Centralized Permissions
- Data sources (S3, RDS, Aurora) → Lake Formation (access control + column-level security) → Data Lake (S3) → Athena → QuickSight → Users

### Apache Kafka (MSK) Architecture
- Producers (Kinesis, IoT, RDS, custom code) → write to Kafka topic → MSK Cluster (Broker 1/2/3 with replication) → poll from topic → Consumers (your code) → EMR, S3, SageMaker, Kinesis, RDS

---

## Important Numbers & Limits

| Service | Parameter | Value |
|---|---|---|
| Athena | Pricing | $5.00 per TB scanned |
| Athena | Recommended file size | > 128 MB |
| Redshift | Performance vs other DW | 10x better |
| Redshift | Max scale | Petabytes (PBs) |
| Redshift | Automated snapshot: time interval | Every 8 hours |
| Redshift | Automated snapshot: data interval | Every 5 GB |
| Redshift | Snapshot retention (automated) | 1–35 days |
| MSK | Default message size | 1 MB |
| MSK | Configurable message size | Up to 10 MB (example) |
| MSK | Max AZs for HA | 3 |
| Kinesis Data Streams | Max message size | 1 MB (hard limit) |
| Amazon Connect | Cost vs traditional CC | 80% cheaper |
| Firehose | Near real-time delivery interval | ~1 minute |

---

## Diagram Descriptions

### Athena Federated Query Diagram
- Central: Amazon Athena queries a Lambda Data Source Connector
- Lambda connects to: ElastiCache, DocumentDB, DynamoDB, Redshift, HBase in EMR, Aurora, SQL Server, MySQL, on-premises databases
- Results stored back in S3 bucket

### Redshift Cluster Diagram
- Query enters via JDBC/ODBC → Leader Node (inside cluster) → distributes to multiple Compute Nodes → results return to Leader Node → returned to client

### Redshift Spectrum Diagram
- Query → Redshift Cluster (Leader + Compute Nodes) → Compute Nodes fan out to N Redshift Spectrum nodes → Spectrum nodes read directly from Amazon S3

### Redshift Snapshot Cross-Region DR Diagram
- Region us-east-1: Redshift Cluster (Original) → Take Snapshot → Cluster Snapshot
- Automated/Manual Copy → Region eu-west-1: Copied Snapshot → Restore → Redshift Cluster (New)

### Glue Data Catalog Diagram
- Sources (S3, RDS, DynamoDB, JDBC) → Glue Data Crawler → writes metadata to Glue Data Catalog (Databases + Tables metadata)
- Glue Data Catalog used by: Glue ETL Jobs, Amazon Athena, Redshift Spectrum, EMR

### Glue CSV to Parquet Pipeline Diagram
- S3 PUT → Input S3 Bucket → S3 event notification → Lambda (or EventBridge) → trigger Glue ETL Job → Glue ETL converts CSV to Parquet → Output S3 Bucket → Amazon Athena analyzes

### Lake Formation Architecture Diagram
- Data Sources (S3, RDS, Aurora, On-Premises SQL & NoSQL) → ingest into Lake Formation (source crawlers, ETL, data catalog, security settings, access control) → Data Lake (stored in S3) → consumed by Athena, Redshift, EMR, Apache Spark → Users

### Big Data Ingestion Pipeline Diagram
- IoT Devices → real-time → Kinesis Data Streams → every 1 minute → Kinesis Data Firehose (+ Lambda transformation) → S3 Ingestion Bucket → SQS (optional) → Lambda trigger → Athena → S3 Reporting Bucket
- Pull path: S3 Reporting Bucket → Amazon Redshift Serverless → Amazon QuickSight → Users

### MSK Architecture Diagram
- Producers (Kinesis, IoT, RDS, etc.) write to Kafka topics in MSK Cluster (Broker 1, 2, 3 with replication between them)
- Consumers poll from topics → route to EMR, S3, SageMaker, Kinesis, RDS

---

## Machine Learning Services

### Amazon Rekognition
- Find objects, people, text, scenes in **images and videos** using ML
- Facial analysis and facial search: user verification, people counting
- Create database of "familiar faces" or compare against celebrities
- Use cases: Labeling, Content Moderation, Text Detection, Face Detection/Analysis (gender, age, emotions), Face Search/Verification, Celebrity Recognition, Pathing (sports analysis)
- **Content Moderation**: set Minimum Confidence Threshold; flag items for manual review via Amazon Augmented AI (A2I)

### Amazon Transcribe
- Speech-to-text using **Automatic Speech Recognition (ASR)** deep learning
- Automatically removes PII using **Redaction**
- Supports Automatic Language Identification for multi-lingual audio
- Use cases: transcribe customer service calls, closed captioning, searchable media archives

### Amazon Polly
- Text-to-speech using deep learning (lifelike speech)
- **Pronunciation Lexicons**: customize word pronunciation (stylized words, acronyms); used in SynthesizeSpeech API
- **SSML (Speech Synthesis Markup Language)**: emphasize words, phonetic pronunciation, breathing sounds, whispering, Newscaster speaking style

### Amazon Translate
- Natural and accurate language translation
- Localizes content (websites, apps) for international users; handles large volumes efficiently

### Amazon Lex
- Same technology powering Alexa
- ASR (speech to text) + NLU (Natural Language Understanding) to recognize intents
- Build chatbots and call center bots
- Flow: Phone call → Amazon Connect → stream → Lex (intent recognized) → invoke Lambda → schedule in CRM

### Amazon Connect
- Cloud-based virtual contact center
- Receive calls, create contact flows
- Integrates with CRM systems and AWS
- No upfront payments; **80% cheaper than traditional contact centers**

### Amazon Comprehend
- **NLP** (Natural Language Processing); fully managed and serverless
- Detects: language, key phrases, places, people, brands, events
- Sentiment analysis (positive/negative)
- Tokenization, parts of speech analysis
- Topic modeling (auto-organizes text files by topic)
- Use cases: analyze customer emails, group articles by topic

### Amazon Comprehend Medical
- Variant specialized for **unstructured clinical text**: physician notes, discharge summaries, test results, case notes
- Detects **PHI (Protected Health Information)** via DetectPHI API
- Integrates with: S3 (batch), Kinesis Data Firehose (real-time), Transcribe (audio → text → analysis)

### Amazon SageMaker AI
- Fully managed service for developers/data scientists to build ML models
- End-to-end ML workflow: label data → build model → train and tune → apply model → predictions
- Solves complexity of doing all ML steps in one place + server provisioning

### Amazon Kendra
- Fully managed **document search** powered by ML
- Extracts answers from documents (text, PDF, HTML, PowerPoint, MS Word, FAQs)
- Natural language search capabilities
- **Incremental Learning**: learns from user interactions/feedback to improve results
- Fine-tune search results (data importance, freshness, custom)
- Data sources: S3, RDS, Google Drive, MS SharePoint, MS OneDrive, Salesforce, ServiceNow, 3rd party

### Amazon Personalize
- Fully managed ML service for **real-time personalized recommendations**
- Same technology used by Amazon.com
- Data ingestion: S3 (batch) + Personalize API (real-time)
- Outputs via: websites, apps, mobile apps, SMS, email marketing
- Implement in days (no need to build/train/deploy custom ML)
- Use cases: retail stores, media and entertainment

### Amazon Textract
- Extracts **text, handwriting, and structured data** from scanned documents using AI/ML
- Extracts data from forms and tables
- Processes: PDFs, images, and other document types
- Use cases: Financial Services (invoices, reports), Healthcare (medical records, insurance), Public Sector (tax forms, ID documents, passports)

---

## Exam-Relevant Details

### Service Selection Signals

| Keyword/Scenario | Service |
|---|---|
| "serverless SQL on S3" | Athena |
| "analyze VPC Flow Logs / CloudTrail / ELB logs" | Athena |
| "data warehouse", "OLAP", "complex joins/aggregations" | Redshift |
| "query S3 without loading into Redshift" | Redshift Spectrum |
| "ETL", "transform data for analytics", "CSV to Parquet" | AWS Glue |
| "data lake", "centralized data governance", "row/column security" | Lake Formation |
| "full-text search", "partial match search", "complement to DynamoDB" | OpenSearch |
| "Hadoop", "Spark", "big data processing cluster" | EMR |
| "BI dashboards", "interactive visualizations" | QuickSight |
| "real-time stream processing", "Apache Flink" | Managed Service for Apache Flink |
| "managed Kafka", "Kafka alternative" | Amazon MSK |
| "face detection", "image/video analysis", "content moderation" | Rekognition |
| "speech to text", "audio transcription" | Transcribe |
| "text to speech" | Polly |
| "language translation" | Translate |
| "chatbot", "call center bot", "NLU intent" | Lex |
| "virtual contact center", "cloud call center" | Connect |
| "NLP", "sentiment analysis", "key phrase extraction" | Comprehend |
| "clinical text", "PHI detection", "medical NLP" | Comprehend Medical |
| "build custom ML model", "train ML model" | SageMaker |
| "ML-powered document search", "natural language Q&A over docs" | Kendra |
| "personalized recommendations", "recommendation engine" | Personalize |
| "extract text from scanned documents", "OCR", "form/table extraction" | Textract |

### Tricky Distinctions

- **Redshift is PostgreSQL-based but NOT for OLTP** — it's OLAP; exam will try to use "PostgreSQL" to make it seem like a relational DB choice
- **Athena vs Redshift**: Athena = ad-hoc serverless queries on S3 (pay per scan); Redshift = persistent data warehouse with indexes (faster for complex queries, but requires cluster)
- **Redshift Spectrum vs Athena**: both query S3 with SQL — Spectrum requires existing Redshift cluster; Athena is fully serverless standalone
- **OpenSearch does NOT natively support SQL** (plugin required) — don't confuse with Athena/Redshift
- **Apache Flink does NOT read from Amazon Data Firehose** — reads from Kinesis Data Streams or MSK only
- **MSK vs Kinesis**: MSK allows message sizes > 1 MB (configurable); Kinesis hard-capped at 1 MB; MSK partitions can only be added (not removed); Kinesis supports shard splitting AND merging
- **QuickSight users/groups are NOT IAM users** — they exist only within QuickSight
- **Lake Formation is built ON TOP of Glue** — adds governance/security layer; Glue is the underlying ETL engine
- **Glue Job Bookmarks** prevent re-processing already-processed data (important for incremental loads)
- **Redshift cross-region snapshots**: you configure automatic copy — snapshots in source region get copied to destination region; restore creates a new cluster
- **EMR Task Nodes** do not store data — only run tasks; ideal for Spot instances
- **EMR Core Nodes** store data AND run tasks — must be long-running (not Spot)
- **CloudWatch Logs → OpenSearch real-time**: use Lambda (managed by AWS); near real-time: use Kinesis Data Firehose
- **Rekognition Content Moderation**: confidence threshold + optional manual review via A2I (Amazon Augmented AI)
- **Transcribe removes PII** automatically (Redaction feature) — not Comprehend
- **Comprehend Medical** specifically handles clinical/healthcare text and PHI; regular Comprehend is general NLP
- **Kendra** answers questions from documents (Q&A); **OpenSearch** does keyword/full-text search — different use cases
- **Personalize** = recommendations (what to buy next); **Kendra** = document Q&A; **Comprehend** = text analysis
