# Practice Exam Re-Test — Design High-Performing Architectures

**Date:** 2026-06-24 | **Questions:** 18 | **Source:** Udemy Practice Exams 1 & 2
**Status:** IN_PROGRESS | **Score:** _/18

---

## Q1/18 [Exam 1 - Q6]

**A healthcare analytics company centralizes clinical and operational datasets in an Amazon S3–based data lake. Incoming data is ingested in Apache Parquet format from multiple hospitals and wearable health devices. To ensure quality and standardization, the company applies several transformation steps: anomaly filtering, datetime normalization, and aggregation by patient cohort. The company needs a solution to support a code-free interface that enables data engineers and business analysts to collaborate on data preparation workflows. The company also requires data lineage tracking, data profiling capabilities, and an easy way to share transformation logic across teams without writing or managing code. Which AWS solution best meets these requirements?**

A) Use AWS Glue Studio’s visual canvas to design data transformation workflows on top of the Parquet files in Amazon S3. Configure Glue Studio jobs to run these transformations without writing code. Share the job definitions with team members for reuse. Use the visual job editor to track transformation progress and inspect profiling statistics for each dataset column

B) Create Amazon Athena SQL queries to perform transformation steps directly on S3. Store queries in AWS Glue Data Catalog and share saved queries with other users through Amazon Athena's query editor

C) Use Amazon AppFlow to move and transform Parquet files in S3. Configure AppFlow transformations and mappings within the visual interface. Share flows with collaborators through AWS IAM policies and scheduled executions

D) Use AWS Glue DataBrew to visually build transformation workflows on top of the raw Parquet files in S3. Use DataBrew recipes to track, audit, and share the transformation steps with others. Enable data profiling to inspect column statistics, null values, and data types across datasets

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q2/18 [Exam 1 - Q8]

**A research group runs its flagship application on a fleet of Amazon EC2 instances for a specialized task that must deliver high random I/O performance. Each instance in the fleet would have access to a dataset that is replicated across the instances by the application itself. Because of the resilient application architecture, the specialized task would continue to be processed even if any instance goes down, as the underlying application would ensure the replacement instance has access to the required dataset. Which of the following options is the MOST cost-optimal and resource-efficient solution to build this fleet of Amazon EC2 instances?**

A) Use Amazon Elastic Block Store (Amazon EBS) based EC2 instances

B) Use Amazon EC2 instances with Amazon EFS mount points

C) Use Instance Store based Amazon EC2 instances

D) Use Amazon EC2 instances with access to Amazon S3 based storage

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** C
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q3/18 [Exam 1 - Q15]

**The product team at a startup has figured out a market need to support both stateful and stateless client-server communications via the application programming interface (APIs) developed using its platform. You have been hired by the startup as a solutions architect to build a solution to fulfill this market need using Amazon API Gateway. Which of the following would you identify as correct?**

A) Amazon API Gateway creates RESTful APIs that enable stateless client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server

B) Amazon API Gateway creates RESTful APIs that enable stateful client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server

C) Amazon API Gateway creates RESTful APIs that enable stateless client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server

D) Amazon API Gateway creates RESTful APIs that enable stateful client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** C
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q4/18 [Exam 1 - Q20]

**A gaming company is looking at improving the availability and performance of its global flagship application which utilizes User Datagram Protocol and needs to support fast regional failover in case an AWS Region goes down. The company wants to continue using its own custom Domain Name System (DNS) service. Which of the following AWS services represents the best solution for this use-case?**

A) AWS Global Accelerator

B) Amazon Route 53

C) AWS Elastic Load Balancing (ELB)

D) Amazon CloudFront

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q5/18 [Exam 1 - Q30]

**An ivy-league university is assisting NASA to find potential landing sites for exploration vehicles of unmanned missions to our neighboring planets. The university uses High Performance Computing (HPC) driven application architecture to identify these landing sites. Which of the following Amazon EC2 instance topologies should this application be deployed on?**

A) The Amazon EC2 instances should be deployed in a partition placement group so that distributed workloads can be handled effectively

B) The Amazon EC2 instances should be deployed in an Auto Scaling group so that application meets high availability requirements

C) The Amazon EC2 instances should be deployed in a spread placement group so that there are no correlated failures

D) The Amazon EC2 instances should be deployed in a cluster placement group so that the underlying workload can benefit from low network latency and high network throughput

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q6/18 [Exam 1 - Q36]

**A junior scientist working with the Deep Space Research Laboratory at NASA is trying to upload a high-resolution image of a nebula into Amazon S3. The image size is approximately 3 gigabytes. The junior scientist is using Amazon S3 Transfer Acceleration (Amazon S3TA) for faster image upload. It turns out that Amazon S3TA did not result in an accelerated transfer. Given this scenario, which of the following is correct regarding the charges for this image transfer?**

A) The junior scientist does not need to pay any transfer charges for the image upload

B) The junior scientist only needs to pay S3TA transfer charges for the image upload

C) The junior scientist only needs to pay Amazon S3 transfer charges for the image upload

D) The junior scientist needs to pay both S3 transfer charges and S3TA transfer charges for the image upload

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q7/18 [Exam 1 - Q40]

**A gaming company is developing a mobile game that streams score updates to a backend processor and then publishes results on a leaderboard. The company has hired you as an AWS Certified Solutions Architect Associate to design a solution that can handle major traffic spikes, process the mobile game updates in the order of receipt, and store the processed updates in a highly available database. The company wants to minimize the management overhead required to maintain the solution. Which of the following will you recommend to meet these requirements?**

A) Push score updates to an Amazon Simple Notification Service (Amazon SNS) topic, subscribe an AWS Lambda function to this Amazon SNS topic to process the updates and then store these processed updates in a SQL database running on Amazon EC2 instance

B) Push score updates to Amazon Kinesis Data Streams which uses an AWS Lambda function to process these updates and then store these processed updates in Amazon DynamoDB

C) Push score updates to Amazon Kinesis Data Streams which uses a fleet of Amazon EC2 instances (with Auto Scaling) to process the updates in Amazon Kinesis Data Streams and then store these processed updates in Amazon DynamoDB

D) Push score updates to an Amazon Simple Queue Service (Amazon SQS) queue which uses a fleet of Amazon EC2 instances (with Auto Scaling) to process these updates in the Amazon SQS queue and then store these processed updates in an Amazon RDS MySQL database

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** B
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q8/18 [Exam 1 - Q44]

**The solo founder at a tech startup has just created a brand new AWS account. The founder has provisioned an Amazon EC2 instance 1A which is running in AWS Region A. Later, he takes a snapshot of the instance 1A and then creates a new Amazon Machine Image (AMI) in Region A from this snapshot. This AMI is then copied into another Region B. The founder provisions an instance 1B in Region B using this new AMI in Region B. At this point in time, what entities exist in Region B?**

A) 1 Amazon EC2 instance, 1 AMI and 1 snapshot exist in Region B

B) 1 Amazon EC2 instance and 2 AMIs exist in Region B

C) 1 Amazon EC2 instance and 1 AMI exist in Region B

D) 1 Amazon EC2 instance and 1 snapshot exist in Region B

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q9/18 [Exam 1 - Q45]

**A retail analytics company operates a large-scale data lake on Amazon S3, where they store daily logs of customer transactions, product views, and inventory updates. Each morning, they need to transform and load the data into a data warehouse to support fast analytical queries. The company also wants to enable data analysts to build and train machine learning (ML) models using familiar SQL syntax without writing custom Python code. The architecture must support massively parallel processing (MPP) for fast data aggregation and scoring, and must use serverless AWS services wherever possible to reduce infrastructure management and operational overhead. Which solution best meets these requirements?**

A) Use a daily AWS Glue job to transform and clean the data stored in Amazon S3. Load the transformed dataset into Amazon Redshift Serverless, which offers MPP capabilities in a serverless model. Enable analysts to use Amazon Redshift ML to build and train ML models

B) Run a daily AWS Glue job to process and transform the raw files in S3 and register the outputs as Amazon Athena tables in AWS Glue Data Catalog. Allow analysts to build ML models using Amazon Athena ML, with SQL-based predictions on top of S3 data without moving it to a warehouse

C) Provision and run a daily Amazon EMR cluster with Apache Spark to process and transform the S3 data. Load the results into Amazon Redshift (provisioned). Enable ML model development by integrating Redshift with Amazon SageMaker notebooks for advanced modeling tasks

D) Use an AWS Glue job to transform and load data into Amazon RDS for PostgreSQL. Allow analysts to run machine learning models using Amazon Aurora ML integrated with PostgreSQL, leveraging Amazon SageMaker endpoints behind the scenes

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q10/18 [Exam 1 - Q46]

**A retail company's dynamic website is hosted using on-premises servers in its data center in the United States. The company is launching its website in Asia, and it wants to optimize the website loading times for new users in Asia. The website's backend must remain in the United States. The website is being launched in a few days, and an immediate solution is needed. What would you recommend?**

A) Use Amazon CloudFront with a custom origin pointing to the on-premises servers

B) Migrate the website to Amazon S3. Use S3 cross-region replication (S3 CRR) between AWS Regions in the US and Asia

C) Use Amazon CloudFront with a custom origin pointing to the DNS record of the website on Amazon Route 53

D) Leverage a Amazon Route 53 geo-proximity routing policy pointing to on-premises servers

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q11/18 [Exam 1 - Q51]

**The sourcing team at the US headquarters of a global e-commerce company is preparing a spreadsheet of the new product catalog. The spreadsheet is saved on an Amazon Elastic File System (Amazon EFS) created in us-east-1 region. The sourcing team counterparts from other AWS regions such as Asia Pacific and Europe also want to collaborate on this spreadsheet. As a solutions architect, what is your recommendation to enable this collaboration with the LEAST amount of operational overhead?**

A) The spreadsheet on the Amazon Elastic File System (Amazon EFS) can be accessed in other AWS regions by using an inter-region VPC peering connection

B) The spreadsheet data will have to be moved into an Amazon RDS for MySQL database which can then be accessed from any AWS region

C) The spreadsheet will have to be copied into Amazon EFS file systems of other AWS regions as Amazon EFS is a regional service and it does not allow access from other AWS regions

D) The spreadsheet will have to be copied in Amazon S3 which can then be accessed from any AWS region

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q12/18 [Exam 1 - Q57] (Select 2)

**A digital event-ticketing platform hosts its core transaction-processing service on AWS. The service runs on Amazon EC2 instances and stores finalized transactions in an Amazon Aurora PostgreSQL database. During periods of high user activity - such as flash ticket sales or holiday promotions - the application begins timing out, causing failed or delayed purchases. A solutions architect has been asked to redesign the backend for scalability and cost-efficiency, without reengineering the database layer. Which combination of actions will meet these goals in the most cost-effective and scalable manner? (Select two)**

A) Modify the application to publish purchase events to an Amazon SQS queue. Launch an Auto Scaling group of EC2 workers that poll the queue and process purchases asynchronously

B) Use an Amazon ElastiCache cluster to cache database queries. Configure the application to store purchase transactions in the cache before writing to the database

C) Deploy read replicas for the Aurora database in another Region and configure EC2 instances to read and write from the nearest replica based on latency

D) Implement Amazon RDS Proxy between the application and the Aurora PostgreSQL cluster. Deploy EC2 instances in an Auto Scaling group to retry transactions as needed

E) Deploy an Amazon API Gateway with throttling and usage plans to slow down incoming purchase requests during peak times and maintain application stability

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** A, D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q13/18 [Exam 1 - Q58] (Select 2)

**A software engineering intern at an e-commerce company is documenting the process flow to provision Amazon EC2 instances via the Amazon EC2 API. These instances are to be used for an internal application that processes Human Resources payroll data. He wants to highlight those volume types that cannot be used as a boot volume. Can you help the intern by identifying those storage volume types that CANNOT be used as boot volumes while creating the instances? (Select two)**

A) Cold Hard disk drive (sc1)

B) General Purpose Solid State Drive (gp2)

C) Instance Store

D) Provisioned IOPS Solid state drive (io1)

E) Throughput Optimized Hard disk drive (st1)

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A, E
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q14/18 [Exam 2 - Q1]

**An IT company has an Access Control Management (ACM) application that uses Amazon RDS for MySQL but is running into performance issues despite using Read Replicas. The company has hired you as a solutions architect to address these performance-related challenges without moving away from the underlying relational database schema. The company has branch offices across the world, and it needs the solution to work on a global scale. Which of the following will you recommend as the MOST cost-effective and high-performance solution?**

A) Spin up Amazon EC2 instances in each AWS region, install MySQL databases and migrate the existing data into these new databases

B) Use Amazon Aurora Global Database to enable fast local reads with low latency in each region

C) Use Amazon DynamoDB Global Tables to provide fast, local, read and write performance in each region

D) Spin up a Amazon Redshift cluster in each AWS region. Migrate the existing data into Redshift clusters

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** B
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q15/18 [Exam 2 - Q20]

**A retail company wants to rollout and test a blue-green deployment for its global application in the next 48 hours. Most of the customers use mobile phones which are prone to Domain Name System (DNS) caching. The company has only two days left for the annual Thanksgiving sale to commence. As a Solutions Architect, which of the following options would you recommend to test the deployment on as many users as possible in the given time frame?**

A) Use AWS CodeDeploy deployment options to choose the right deployment

B) Use Elastic Load Balancing (ELB) to distribute traffic across deployments

C) Use Amazon Route 53 weighted routing to spread traffic across different deployments

D) Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q16/18 [Exam 2 - Q21]

**A video conferencing platform serves users worldwide through a globally distributed deployment of Amazon EC2 instances behind Network Load Balancers (NLBs) in several AWS Regions. The platform's architecture currently allows clients to connect to any Region via public endpoints, depending on how DNS resolves. However, users in regions far from the load balancers frequently experience high latency and slow connection times, especially during session initiation. The company wants to optimize the experience for global users by reducing end-to-end latency and load time while keeping the existing NLBs and EC2-based application infrastructure in place. Which solution will best meet these requirements?**

A) Deploy Amazon CloudFront with HTTP caching enabled in front of the NLBs. Use CloudFront edge locations to serve user requests faster and reduce the load on the backend EC2 instances

B) Replace all Network Load Balancers (NLBs) with Application Load Balancers (ALBs) in each Region. Register the EC2 instances as targets behind the ALBs and use cross-zone load balancing for latency distribution

C) Configure Amazon Route 53 with latency-based routing policies to direct users to the Region with the lowest response time. Use health checks to fail over to another Region if a specific NLB becomes unhealthy

D) Deploy a standard accelerator in AWS Global Accelerator and register the existing regional NLBs as endpoints. Use the accelerator to route user requests through AWS’s global edge network to the closest healthy Regional NLB

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q17/18 [Exam 2 - Q38] (Select 2)

**An engineering team wants to examine the feasibility of the user data feature of Amazon EC2 for an upcoming project. Which of the following are true about the Amazon EC2 user data configuration? (Select two)**

A) By default, user data runs only during the boot cycle when you first launch an instance

B) When an instance is running, you can update user data by using root user credentials

C) By default, scripts entered as user data do not have root user privileges for executing

D) By default, user data is executed every time an Amazon EC2 instance is re-started

E) By default, scripts entered as user data are executed with root user privileges

<details>
<summary>Original Result</summary>

- **Your answer:** B, D
- **Correct answer:** A, E
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q18/18 [Exam 2 - Q50]

**A company is developing a global healthcare application that requires the least possible latency for database read/write operations from users in several geographies across the world. The company has hired you as an AWS Certified Solutions Architect Associate to build a solution using Amazon Aurora that offers an effective recovery point objective (RPO) of seconds and a recovery time objective (RTO) of a minute. Which of the following options would you recommend?**

A) Set up an Amazon Aurora provisioned Database cluster

B) Set up an Amazon Aurora multi-master Database cluster

C) Set up an Amazon Aurora serverless Database cluster

D) Set up an Amazon Aurora Global Database cluster

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 18 |
| Correct | _ |
| Wrong | _ |
| Score | _% |
| Improvement | _ |