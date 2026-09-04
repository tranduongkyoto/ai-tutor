# Practice Test #1 — AWS Certified Solutions Architect Associate
**Total: 65 Questions**

---

## Question 1
**Domain:** Design Secure Architectures

An enterprise runs a microservices-based application on Amazon EKS, deployed on EC2 worker nodes. The application includes a frontend UI service that interacts with Amazon DynamoDB and a data-processing service that stores and retrieves files from Amazon S3. The organization needs to strictly enforce least privilege access: the UI Pods must access only DynamoDB, and the data-processing Pods must access only S3.
Which solution will best enforce these access controls within the EKS cluster?

A. Create separate Kubernetes service accounts for the UI and data services. Use IAM Roles for Service Accounts (IRSA) to map each service account to an IAM role with only the required permissions. Assign DynamoDB access to the UI Pods and S3 access to the data Pods **(CORRECT)**
B. Attach an IAM policy directly to each Pod using Kubernetes annotations. Assign the S3 policy to data-service Pods and the DynamoDB policy to UI Pods
C. Create IAM policies for DynamoDB and S3 access, and attach both to the EC2 instance profile used by the EKS nodes. Use Kubernetes role-based access control (RBAC) to control service-level permissions within the cluster
D. Create one Kubernetes service account shared across all Pods. Attach a single IAM role to this account with both AmazonS3FullAccess and AmazonDynamoDBFullAccess policies

**Answer:** A
---

## Question 2
**Domain:** Design Secure Architectures

The flagship application for a gaming company connects to an Amazon Aurora database and the entire technology stack is currently deployed in the United States. Now, the company has plans to expand to Europe and Asia for its operations. It needs the 
games
 table to be accessible globally but needs the 
users
 and 
games_played
 tables to be regional only.
How would you implement this with minimal application refactoring?

A. Use an Amazon Aurora Global Database for the 
games
 table and use Amazon Aurora for the 
users
 and 
games_played
 tables **(CORRECT)**
B. Use an Amazon Aurora Global Database for the 
games
 table and use Amazon DynamoDB tables for the 
users
 and 
games_played
 tables
C. Use a Amazon DynamoDB global table for the 
games
 table and use Amazon Aurora for the 
users
 and 
games_played
 tables
D. Use a Amazon DynamoDB global table for the 
games
 table and use Amazon DynamoDB tables for the 
users
 and 
games_played
 tables

**Answer:** A
---

## Question 3
**Domain:** Design Secure Architectures

A development team requires permissions to list an Amazon S3 bucket and delete objects from that bucket. A systems administrator has created the following IAM policy to provide access to the bucket and applied that policy to the group. The group is not able to delete objects in the bucket. The company follows the principle of least privilege.
    "Version": "2021-10-17",
    "Statement": [
        {
            "Action": [
                "s3:ListBucket",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::example-bucket"
            ],
            "Effect": "Allow"
        }
    ]
Which statement should a solutions architect add to the policy to address this issue?

A. {
    "Action": [
        "s3:*"
    ],
    "Resource": [
        "arn:aws:s3:::example-bucket/*"
    ],
    "Effect": "Allow"
}
B. {
    "Action": [
        "s3:DeleteObject"
    ],
    "Resource": [
        "arn:aws:s3:::example-bucket*"
    ],
    "Effect": "Allow"
}
C. {
    "Action": [
        "s3:DeleteObject"
    ],
    "Resource": [
        "arn:aws:s3:::example-bucket/*"
    ],
    "Effect": "Allow"
} **(CORRECT)**
D. {
    "Action": [
        "s3:*Object"
    ],
    "Resource": [
        "arn:aws:s3:::example-bucket/*"
    ],
    "Effect": "Allow"
}

**Answer:** C
---

## Question 4
**Domain:** Design High-Performing Architectures

The engineering team at an in-home fitness company is evaluating multiple in-memory data stores with the ability to power its on-demand, live leaderboard. The company's leaderboard requires high availability, low latency, and real-time processing to deliver customizable user data for the community of users working out together virtually from the comfort of their home.
As a solutions architect, which of the following solutions would you recommend? (Select two)

A. Power the on-demand, live leaderboard using Amazon Neptune as it meets the in-memory, high availability, low latency requirements
B. Power the on-demand, live leaderboard using Amazon ElastiCache for Redis as it meets the in-memory, high availability, low latency requirements **(CORRECT)**
C. Power the on-demand, live leaderboard using Amazon DynamoDB with DynamoDB Accelerator (DAX) as it meets the in-memory, high availability, low latency requirements **(CORRECT)**
D. Power the on-demand, live leaderboard using Amazon DynamoDB as it meets the in-memory, high availability, low latency requirements
E. Power the on-demand, live leaderboard using Amazon RDS for Aurora as it meets the in-memory, high availability, low latency requirements

**Answer:** B, C
---

## Question 5
**Domain:** Design Secure Architectures

An IT security consultancy is working on a solution to protect data stored in Amazon S3 from any malicious activity as well as check for any vulnerabilities on Amazon EC2 instances.
As a solutions architect, which of the following solutions would you suggest to help address the given requirement?

A. Use Amazon GuardDuty to monitor any malicious activity on data stored in Amazon S3. Use security assessments provided by Amazon GuardDuty to check for vulnerabilities on Amazon EC2 instances
B. Use Amazon Inspector to monitor any malicious activity on data stored in Amazon S3. Use security assessments provided by Amazon Inspector to check for vulnerabilities on Amazon EC2 instances
C. Use Amazon GuardDuty to monitor any malicious activity on data stored in Amazon S3. Use security assessments provided by Amazon Inspector to check for vulnerabilities on Amazon EC2 instances **(CORRECT)**
D. Use Amazon Inspector to monitor any malicious activity on data stored in Amazon S3. Use security assessments provided by Amazon GuardDuty to check for vulnerabilities on Amazon EC2 instances

**Answer:** C
---

## Question 6
**Domain:** Design Resilient Architectures

A healthcare analytics company centralizes clinical and operational datasets in an Amazon S3–based data lake. Incoming data is ingested in Apache Parquet format from multiple hospitals and wearable health devices. To ensure quality and standardization, the company applies several transformation steps: anomaly filtering, datetime normalization, and aggregation by patient cohort. The company needs a solution to support a code-free interface that enables data engineers and business analysts to collaborate on data preparation workflows. The company also requires data lineage tracking, data profiling capabilities, and an easy way to share transformation logic across teams without writing or managing code.
Which AWS solution best meets these requirements?

A. Use AWS Glue Studio’s visual canvas to design data transformation workflows on top of the Parquet files in Amazon S3. Configure Glue Studio jobs to run these transformations without writing code. Share the job definitions with team members for reuse. Use the visual job editor to track transformation progress and inspect profiling statistics for each dataset column
B. Create Amazon Athena SQL queries to perform transformation steps directly on S3. Store queries in AWS Glue Data Catalog and share saved queries with other users through Amazon Athena's query editor
C. Use Amazon AppFlow to move and transform Parquet files in S3. Configure AppFlow transformations and mappings within the visual interface. Share flows with collaborators through AWS IAM policies and scheduled executions
D. Use AWS Glue DataBrew to visually build transformation workflows on top of the raw Parquet files in S3. Use DataBrew recipes to track, audit, and share the transformation steps with others. Enable data profiling to inspect column statistics, null values, and data types across datasets **(CORRECT)**

**Answer:** D
---

## Question 7
**Domain:** Design Cost-Optimized Architectures

A media agency stores its re-creatable assets on Amazon Simple Storage Service (Amazon S3) buckets. The assets are accessed by a large number of users for the first few days and the frequency of access falls down drastically after a week. Although the assets would be accessed occasionally after the first week, but they must continue to be immediately accessible when required. The cost of maintaining all the assets on Amazon S3 storage is turning out to be very expensive and the agency is looking at reducing costs as much as possible.
As an AWS Certified Solutions Architect – Associate, can you suggest a way to lower the storage costs while fulfilling the business requirements?

A. Configure a lifecycle policy to transition the objects to Amazon S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days
B. Configure a lifecycle policy to transition the objects to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days **(CORRECT)**
C. Configure a lifecycle policy to transition the objects to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) after 7 days
D. Configure a lifecycle policy to transition the objects to Amazon S3 Standard-Infrequent Access (S3 Standard-IA) after 7 days

**Answer:** B
---

## Question 8
**Domain:** Design High-Performing Architectures

A research group runs its flagship application on a fleet of Amazon EC2 instances for a specialized task that must deliver high random I/O performance. Each instance in the fleet would have access to a dataset that is replicated across the instances by the application itself. Because of the resilient application architecture, the specialized task would continue to be processed even if any instance goes down, as the underlying application would ensure the replacement instance has access to the required dataset.
Which of the following options is the MOST cost-optimal and resource-efficient solution to build this fleet of Amazon EC2 instances?

A. Use Amazon Elastic Block Store (Amazon EBS) based EC2 instances
B. Use Amazon EC2 instances with Amazon EFS mount points
C. Use Instance Store based Amazon EC2 instances **(CORRECT)**
D. Use Amazon EC2 instances with access to Amazon S3 based storage

**Answer:** C
---

## Question 9
**Domain:** Design Resilient Architectures

The development team at an e-commerce startup has set up multiple microservices running on Amazon EC2 instances under an Application Load Balancer. The team wants to route traffic to multiple back-end services based on the URL path of the HTTP header. So it wants requests for https://www.example.com/orders to go to a specific microservice and requests for https://www.example.com/products to go to another microservice.
Which of the following features of Application Load Balancers can be used for this use-case?

A. Path-based Routing **(CORRECT)**
B. Query string parameter-based routing
C. Host-based Routing
D. HTTP header-based routing

**Answer:** A
---

## Question 10
**Domain:** Design High-Performing Architectures

An e-commerce company manages a digital catalog of consumer products submitted by third-party sellers. Each product submission includes a description stored as a text file in an Amazon S3 bucket. These descriptions may include ingredient information for consumable products like snacks, supplements, or beverages. The company wants to build a fully automated solution that extracts ingredient names from the uploaded product descriptions and uses those names to query an Amazon DynamoDB table, which returns precomputed health and safety scores for each ingredient. Non-food items and invalid submissions can be ignored without affecting application logic. The company has no in-house machine learning (ML) experts and is looking for the most cost-effective solution with minimal operational overhead.
Which solution meets these requirements MOST cost-effectively?

A. Use Amazon Lookout for Vision to scan the uploaded text files in the S3 bucket and extract entities. Invoke this workflow using an S3-triggered Lambda function. Parse the output and use Amazon API Gateway to push updates to the frontend in real time
B. Create a workflow where Amazon Transcribe is used to convert synthetic audio versions (created from text of the product descriptions) back into text. Analyze the transcripts manually or using simple keyword matching within a Lambda function. Use Amazon SNS to notify the content moderation team for each processed file
C. Use Amazon SageMaker with a custom-trained NLP model to identify ingredients from the uploaded descriptions. Use Amazon EventBridge to invoke a Lambda function that forwards the document content to a SageMaker endpoint and stores the results in DynamoDB. Fine-tune the model using labeled ingredient datasets from open-source repositories and retrain it monthly
D. Configure S3 Event Notifications to trigger an AWS Lambda function whenever a new product description is uploaded. Inside the function, use Amazon Comprehend's custom entity recognition feature to extract ingredient names. Store these names in the DynamoDB table and let the front-end application query for health scores **(CORRECT)**

**Answer:** D
---

## Question 11
**Domain:** Design High-Performing Architectures

A large financial institution operates an on-premises data center with hundreds of petabytes of data managed on Microsoft’s Distributed File System (DFS). The CTO wants the organization to transition into a hybrid cloud environment and run data-intensive analytics workloads that support DFS.
Which of the following AWS services can facilitate the migration of these workloads?

A. Amazon FSx for Lustre
B. Microsoft SQL Server on AWS
C. Amazon FSx for Windows File Server **(CORRECT)**
D. AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD)

**Answer:** C
---

## Question 12
**Domain:** Design Resilient Architectures

A leading carmaker would like to build a new car-as-a-sensor service by leveraging fully serverless components that are provisioned and managed automatically by AWS. The development team at the carmaker does not want an option that requires the capacity to be manually provisioned, as it does not want to respond manually to changing volumes of sensor data.
Given these constraints, which of the following solutions is the BEST fit to develop this car-as-a-sensor service?

A. Ingest the sensor data in Amazon Kinesis Data Firehose, which directly writes the data into an auto-scaled Amazon DynamoDB table for downstream processing
B. Ingest the sensor data in Amazon Kinesis Data Streams, which is polled by an application running on an Amazon EC2 instance and the data is written into an auto-scaled Amazon DynamoDB table for downstream processing
C. Ingest the sensor data in an Amazon Simple Queue Service (Amazon SQS) standard queue, which is polled by an application running on an Amazon EC2 instance and the data is written into an auto-scaled Amazon DynamoDB table for downstream processing
D. Ingest the sensor data in an Amazon Simple Queue Service (Amazon SQS) standard queue, which is polled by an AWS Lambda function in batches and the data is written into an auto-scaled Amazon DynamoDB table for downstream processing **(CORRECT)**

**Answer:** D
---

## Question 13
**Domain:** Design Cost-Optimized Architectures

A video analytics company runs data-intensive batch processing workloads that generate large log files and metadata daily. These files are currently stored in an on-premises NFS-based storage system located in the company's primary data center. However, the storage system is becoming increasingly difficult to scale and is unable to meet the company's growing storage demands. The IT team wants to migrate to a cloud-based storage solution that minimizes costs, retains NFS compatibility, and supports automated tiering of rarely accessed data to lower-cost storage. The team prefers to continue using existing NFS-based tools and protocols for compatibility with their current application stack.
Which solution will meet these requirements MOST cost-effectively?

A. Use Amazon FSx for Windows File Server to replace the NFS workload. Enable data deduplication and automatic backups. Use Amazon S3 Glacier to move snapshots to a cost-efficient storage tier. Reconfigure the analytics application to access files using SMB protocol
B. Deploy an AWS Storage Gateway File Gateway on premises. Configure it to present an NFS-compatible file share to the workloads. Store the uploaded files in Amazon S3, and use S3 Lifecycle policies to automatically transition infrequently accessed objects to lower-cost storage classes **(CORRECT)**
C. Deploy an AWS Storage Gateway Volume Gateway in cached mode. Attach it as a block device to an on-premises file server and mount NFS on top. Store snapshots in Amazon S3 Glacier Deep Archive, and use AWS Backup to manage recovery operations and tiering
D. Provision an Amazon Elastic File System (Amazon EFS) file system with the One Zone–IA storage class. Use AWS DataSync to migrate the NFS data to EFS. Configure the application to mount the file system over NFS and activate lifecycle management to tier infrequently accessed files

**Answer:** B
---

## Question 14
**Domain:** Design Secure Architectures

A financial services company operates a containerized microservices architecture using Kubernetes in its on-premises data center. Due to strict industry regulations and internal security policies, all application data and workloads must remain physically within the on-premises environment. The company’s infrastructure team wants to modernize its Kubernetes stack and take advantage of AWS-managed services and APIs, including automated Kubernetes upgrades, Amazon CloudWatch integration, and access to AWS IAM features — but without migrating any data or compute resources to the cloud.
Which AWS solution will best meet the company’s requirements for modernization while ensuring that all data remains on premises?

A. Deploy Amazon ECS with Fargate in a nearby AWS Local Zone. Use CloudWatch Logs to forward events to the primary region. Connect the Local Zone to the company’s data center over a VPN. Configure containers to pull data from on-premises storage through a mounted file share
B. Set up a dedicated AWS Direct Connect connection between the on-premises environment and an AWS Region. Deploy Amazon EKS in the cloud and connect it to the local Kubernetes cluster. Use IAM roles and API Gateway to integrate authentication and traffic flow for hybrid workloads
C. Use an AWS Snowball Edge Compute Optimized device to run EKS-compatible Docker containers on-site. Periodically export application logs and container snapshots to Amazon S3 using Snowball’s offline data transfer features. Use the Snowball console to orchestrate workloads in batches
D. Install an AWS Outposts rack in the company’s data center. Use Amazon EKS Anywhere on Outposts to run containerized workloads locally while integrating with AWS APIs **(CORRECT)**

**Answer:** D
---

## Question 15
**Domain:** Design High-Performing Architectures

The product team at a startup has figured out a market need to support both stateful and stateless client-server communications via the application programming interface (APIs) developed using its platform. You have been hired by the startup as a solutions architect to build a solution to fulfill this market need using Amazon API Gateway.
Which of the following would you identify as correct?

A. Amazon API Gateway creates RESTful APIs that enable stateless client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server
B. Amazon API Gateway creates RESTful APIs that enable stateful client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server
C. Amazon API Gateway creates RESTful APIs that enable stateless client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server **(CORRECT)**
D. Amazon API Gateway creates RESTful APIs that enable stateful client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server

**Answer:** C
---

## Question 16
**Domain:** Design Resilient Architectures

The payroll department at a company initiates several computationally intensive workloads on Amazon EC2 instances at a designated hour on the last day of every month. The payroll department has noticed a trend of severe performance lag during this hour. The engineering team has figured out a solution by using Auto Scaling Group for these Amazon EC2 instances and making sure that 10 Amazon EC2 instances are available during this peak usage hour. For normal operations only 2 Amazon EC2 instances are enough to cater to the workload.
As a solutions architect, which of the following steps would you recommend to implement the solution?

A. Configure your Auto Scaling group by creating a scheduled action that kicks-off at the designated hour on the last day of the month. Set the desired capacity of instances to 10. This causes the scale-out to happen before peak traffic kicks in at the designated hour **(CORRECT)**
B. Configure your Auto Scaling group by creating a simple tracking policy and setting the instance count to 10 at the designated hour. This causes the scale-out to happen before peak traffic kicks in at the designated hour
C. Configure your Auto Scaling group by creating a scheduled action that kicks-off at the designated hour on the last day of the month. Set the min count as well as the max count of instances to 10. This causes the scale-out to happen before peak traffic kicks in at the designated hour
D. Configure your Auto Scaling group by creating a target tracking policy and setting the instance count to 10 at the designated hour. This causes the scale-out to happen before peak traffic kicks in at the designated hour

**Answer:** A
---

## Question 17
**Domain:** Design Secure Architectures

A company uses Amazon S3 buckets for storing sensitive customer data. The company has defined different retention periods for different objects present in the Amazon S3 buckets, based on the compliance requirements. But, the retention rules do not seem to work as expected.
Which of the following options represent a valid configuration for setting up retention periods for objects in Amazon S3 buckets? (Select two)

A. You cannot place a retention period on an object version through a bucket default setting
B. Different versions of a single object can have different retention modes and periods **(CORRECT)**
C. When you use bucket default settings, you specify a 
Retain Until Date
 for the object version
D. When you apply a retention period to an object version explicitly, you specify a 
Retain Until Date
 for the object version **(CORRECT)**
E. The bucket default settings will override any explicit retention mode or period you request on an object version

**Answer:** B, D
---

## Question 18
**Domain:** Design Secure Architectures

An organization wants to delegate access to a set of users from the development environment so that they can access some resources in the production environment which is managed under another AWS account.
As a solutions architect, which of the following steps would you recommend?

A. Create new IAM user credentials for the production environment and share these credentials with the set of users from the development environment
B. It is not possible to access cross-account resources
C. Both IAM roles and IAM users can be used interchangeably for cross-account access
D. Create a new IAM role with the required permissions to access the resources in the production environment. The users can then assume this IAM role while accessing the resources from the production environment **(CORRECT)**

**Answer:** D
---

## Question 19
**Domain:** Design Cost-Optimized Architectures

A company runs a data processing workflow that takes about 60 minutes to complete. The workflow can withstand disruptions and it can be started and stopped multiple times.
Which is the most cost-effective solution to build a solution for the workflow?

A. Use Amazon EC2 spot instances to run the workflow processes **(CORRECT)**
B. Use AWS Lambda function to run the workflow processes
C. Use Amazon EC2 on-demand instances to run the workflow processes
D. Use Amazon EC2 reserved instances to run the workflow processes

**Answer:** A
---

## Question 20
**Domain:** Design High-Performing Architectures

A gaming company is looking at improving the availability and performance of its global flagship application which utilizes User Datagram Protocol and needs to support fast regional failover in case an AWS Region goes down. The company wants to continue using its own custom Domain Name System (DNS) service.
Which of the following AWS services represents the best solution for this use-case?

A. AWS Global Accelerator **(CORRECT)**
B. Amazon Route 53
C. AWS Elastic Load Balancing (ELB)
D. Amazon CloudFront

**Answer:** A
---

## Question 21
**Domain:** Design High-Performing Architectures

A retail company runs a customer management system backed by a Microsoft SQL Server database. The system is tightly integrated with applications that rely on T-SQL queries. The company wants to modernize its infrastructure by migrating to Amazon Aurora PostgreSQL, but it needs to avoid major modifications to the existing application logic.
Which combination of actions should the company take to achieve this goal with minimal application refactoring? (Select two)

A. Use AWS Glue to convert T-SQL queries to PostgreSQL-compatible SQL during the migration
B. Deploy Babelfish for Aurora PostgreSQL to enable support for T-SQL commands **(CORRECT)**
C. Use Amazon Aurora Global Database to replicate data across regions for compatibility
D. Use AWS Schema Conversion Tool (AWS SCT) along with AWS Database Migration Service (AWS DMS) to migrate the schema and data **(CORRECT)**
E. Configure Amazon Aurora PostgreSQL with a custom endpoint that emulates Microsoft SQL Server behavior

**Answer:** B, D
---

## Question 22
**Domain:** Design Resilient Architectures

The engineering team at a Spanish professional football club has built a notification system for its website using Amazon Simple Notification Service (Amazon SNS) notifications which are then handled by an AWS Lambda function for end-user delivery. During the off-season, the notification systems need to handle about 100 requests per second. During the peak football season, the rate touches about 5000 requests per second and it is noticed that a significant number of the notifications are not being delivered to the end-users on the website.
As a solutions architect, which of the following would you suggest as the BEST possible solution to this issue?

A. Amazon SNS message deliveries to AWS Lambda have crossed the account concurrency quota for AWS Lambda, so the team needs to contact AWS support to raise the account limit **(CORRECT)**
B. The engineering team needs to provision more servers running the AWS Lambda service
C. Amazon SNS has hit a scalability limit, so the team needs to contact AWS support to raise the account limit
D. The engineering team needs to provision more servers running the Amazon SNS service

**Answer:** A
---

## Question 23
**Domain:** Design Cost-Optimized Architectures

An audit department generates and accesses the audit reports only twice in a financial year. The department uses AWS Step Functions to orchestrate the report creating process that has failover and retry scenarios built into the solution. The underlying data to create these audit reports is stored on Amazon S3, runs into hundreds of Terabytes and should be available with millisecond latency.
As an AWS Certified Solutions Architect – Associate, which is the MOST cost-effective storage class that you would recommend to be used for this use-case?

A. Amazon S3 Standard
B. Amazon S3 Standard-Infrequent Access (S3 Standard-IA) **(CORRECT)**
C. Amazon S3 Intelligent-Tiering (S3 Intelligent-Tiering)
D. Amazon S3 Glacier Deep Archive

**Answer:** B
---

## Question 24
**Domain:** Design High-Performing Architectures

A data analytics company measures what the consumers watch and what advertising they’re exposed to. This real-time data is ingested into its on-premises data center and subsequently, the daily data feed is compressed into a single file and uploaded on Amazon S3 for backup. The typical compressed file size is around 2 gigabytes.
Which of the following is the fastest way to upload the daily compressed file into Amazon S3?

A. Upload the compressed file using multipart upload with Amazon S3 Transfer Acceleration (Amazon S3TA) **(CORRECT)**
B. Upload the compressed file in a single operation
C. Upload the compressed file using multipart upload
D. FTP the compressed file into an Amazon EC2 instance that runs in the same region as the Amazon S3 bucket. Then transfer the file from the Amazon EC2 instance into the Amazon S3 bucket

**Answer:** A
---

## Question 25
**Domain:** Design Secure Architectures

A new DevOps engineer has joined a large financial services company recently. As part of his onboarding, the IT department is conducting a review of the checklist for tasks related to AWS Identity and Access Management (AWS IAM).
As an AWS Certified Solutions Architect – Associate, which best practices would you recommend (Select two)?

A. Enable AWS Multi-Factor Authentication (AWS MFA) for privileged users **(CORRECT)**
B. Use user credentials to provide access specific permissions for Amazon EC2 instances
C. Configure AWS CloudTrail to log all AWS Identity and Access Management (AWS IAM) actions **(CORRECT)**
D. Grant maximum privileges to avoid assigning privileges again
E. Create a minimum number of accounts and share these account credentials among employees

**Answer:** A, C
---

## Question 26
**Domain:** Design Resilient Architectures

A healthcare company uses its on-premises infrastructure to run legacy applications that require specialized customizations to the underlying Oracle database as well as its host operating system (OS). The company also wants to improve the availability of the Oracle database layer. The company has hired you as an AWS Certified Solutions Architect – Associate to build a solution on AWS that meets these requirements while minimizing the underlying infrastructure maintenance effort.
Which of the following options represents the best solution for this use case?

A. Leverage cross AZ read-replica configuration of Amazon RDS for Oracle that allows the Database Administrator (DBA) to access and customize the database environment and the underlying operating system
B. Leverage multi-AZ configuration of Amazon RDS Custom for Oracle that allows the Database Administrator (DBA) to access and customize the database environment and the underlying operating system **(CORRECT)**
C. Deploy the Oracle database layer on multiple Amazon EC2 instances spread across two Availability Zones (AZs). This deployment configuration guarantees high availability and also allows the Database Administrator (DBA) to access and customize the database environment and the underlying operating system
D. Leverage multi-AZ configuration of Amazon RDS for Oracle that allows the Database Administrator (DBA) to access and customize the database environment and the underlying operating system

**Answer:** B
---

## Question 27
**Domain:** Design Secure Architectures

A media company runs a photo-sharing web application that is accessed across three different countries. The application is deployed on several Amazon Elastic Compute Cloud (Amazon EC2) instances running behind an Application Load Balancer. With new government regulations, the company has been asked to block access from two countries and allow access only from the home country of the company.
Which configuration should be used to meet this changed requirement?

A. Configure the security group on the Application Load Balancer
B. Configure the security group for the Amazon EC2 instances
C. Use Geo Restriction feature of Amazon CloudFront in a Amazon Virtual Private Cloud (Amazon VPC)
D. Configure AWS Web Application Firewall (AWS WAF) on the Application Load Balancer in a Amazon Virtual Private Cloud (Amazon VPC) **(CORRECT)**

**Answer:** D
---

## Question 28
**Domain:** Design Cost-Optimized Architectures

A biotechnology firm runs genomics data analysis workloads using AWS Lambda functions deployed inside a VPC in their central AWS account. The input data for these workloads consists of large files stored in an Amazon Elastic File System (Amazon EFS) that resides in a separate AWS account managed by a research partner. The firm wants the Lambda function in their account to access the shared EFS storage directly. The access pattern and file volume are expected to grow as additional research datasets are added over time, so the solution must be scalable and cost-efficient, and should require minimal operational overhead.
Which solution best meets these requirements in the MOST cost-effective way?

A. Create a second Lambda function in the research partner's account that mounts the EFS file system locally. Have the main Lambda function in the central account invoke this secondary Lambda via Amazon API Gateway for data access and computation. Use IAM cross-account permissions to allow invocation
B. Use Amazon EFS resource policies to allow cross-account access to the file system from the central account. Attach the EFS mount target to a shared VPC or peered VPC, and mount the file system in the Lambda function configuration using an EFS access point **(CORRECT)**
C. Package the genomic input data as a Lambda layer and publish it in the research partner's account. Share the layer across accounts by modifying its resource policy and attach the layer to the Lambda function in the central account to access the data during execution
D. Set up an Amazon S3 bucket in the research partner’s account and periodically copy EFS contents into the bucket using scheduled AWS DataSync jobs. Use Amazon S3 Access Points to expose the data to the Lambda function in the central account, allowing access via S3 API calls instead of file system mounts

**Answer:** B
---

## Question 29
**Domain:** Design Secure Architectures

A software company has a globally distributed team of developers, that requires secure and compliant access to AWS environments. The company manages multiple AWS accounts under AWS Organizations and uses an on-premises Microsoft Active Directory for user authentication. To simplify access control and identity governance across projects and accounts, the company wants a centrally managed solution that integrates with their existing infrastructure. The solution should require the least amount of ongoing operational management.
Which approach best meets the company’s requirements?

A. Deploy an open-source identity provider (IdP) on Amazon EC2. Synchronize it with the on-premises Active Directory and use SAML to federate access to AWS accounts. Assign IAM roles to federated users based on SAML assertions
B. Use AWS Control Tower to enable account access for developers. Create AWS IAM roles in each member account and manually assign permissions. Instruct developers to assume roles across accounts using the AWS CLI
C. Deploy AWS Directory Service for Microsoft Active Directory in AWS. Establish a trust relationship with the on-premises Active Directory. Use IAM roles linked to AD groups to control access to AWS resources
D. Use AWS Directory Service AD Connector to connect AWS to the on-premises Active Directory. Integrate AD Connector with AWS IAM Identity Center. Use permission sets to assign access to AWS accounts and resources based on Active Directory group membership **(CORRECT)**

**Answer:** D
---

## Question 30
**Domain:** Design High-Performing Architectures

An ivy-league university is assisting NASA to find potential landing sites for exploration vehicles of unmanned missions to our neighboring planets. The university uses High Performance Computing (HPC) driven application architecture to identify these landing sites.
Which of the following Amazon EC2 instance topologies should this application be deployed on?

A. The Amazon EC2 instances should be deployed in a partition placement group so that distributed workloads can be handled effectively
B. The Amazon EC2 instances should be deployed in an Auto Scaling group so that application meets high availability requirements
C. The Amazon EC2 instances should be deployed in a spread placement group so that there are no correlated failures
D. The Amazon EC2 instances should be deployed in a cluster placement group so that the underlying workload can benefit from low network latency and high network throughput **(CORRECT)**

**Answer:** D
---

## Question 31
**Domain:** Design Cost-Optimized Architectures

A leading social media analytics company is contemplating moving its dockerized application stack into AWS Cloud. The company is not sure about the pricing for using Amazon Elastic Container Service (Amazon ECS) with the EC2 launch type compared to the Amazon Elastic Container Service (Amazon ECS) with the Fargate launch type.
Which of the following is correct regarding the pricing for these two services?

A. Both Amazon ECS with EC2 launch type and Amazon ECS with Fargate launch type are charged based on Amazon EC2 instances and Amazon EBS Elastic Volumes used
B. Both Amazon ECS with EC2 launch type and Amazon ECS with Fargate launch type are charged based on vCPU and memory resources that the containerized application requests
C. Amazon ECS with EC2 launch type is charged based on EC2 instances and EBS volumes used. Amazon ECS with Fargate launch type is charged based on vCPU and memory resources that the containerized application requests **(CORRECT)**
D. Both Amazon ECS with EC2 launch type and Amazon ECS with Fargate launch type are just charged based on Elastic Container Service used per hour

**Answer:** C
---

## Question 32
**Domain:** Design Resilient Architectures

A healthcare startup needs to enforce compliance and regulatory guidelines for objects stored in Amazon S3. One of the key requirements is to provide adequate protection against accidental deletion of objects.
As a solutions architect, what are your recommendations to address these guidelines? (Select two) ?

A. Create an event trigger on deleting any Amazon S3 object. The event invokes an Amazon Simple Notification Service (Amazon SNS) notification via email to the IT manager
B. Enable multi-factor authentication (MFA) delete on the Amazon S3 bucket **(CORRECT)**
C. Enable versioning on the Amazon S3 bucket **(CORRECT)**
D. Change the configuration on Amazon S3 console so that the user needs to provide additional confirmation while deleting any Amazon S3 object
E. Establish a process to get managerial approval for deleting Amazon S3 objects

**Answer:** B, C
---

## Question 33
**Domain:** Design High-Performing Architectures

A logistics company is building a multi-tier application to track the location of its trucks during peak operating hours. The company wants these data points to be accessible in real-time in its analytics platform via a REST API. The company has hired you as an AWS Certified Solutions Architect Associate to build a multi-tier solution to store and retrieve this location data for analysis.
Which of the following options addresses the given use case?

A. Leverage Amazon QuickSight with Amazon Redshift
B. Leverage Amazon API Gateway with Amazon Kinesis Data Analytics **(CORRECT)**
C. Leverage Amazon API Gateway with AWS Lambda
D. Leverage Amazon Athena with Amazon S3

**Answer:** B
---

## Question 34
**Domain:** Design Secure Architectures

One of the biggest football leagues in Europe has granted the distribution rights for live streaming its matches in the USA to a silicon valley based streaming services company. As per the terms of distribution, the company must make sure that only users from the USA are able to live stream the matches on their platform. Users from other countries in the world must be denied access to these live-streamed matches.
Which of the following options would allow the company to enforce these streaming restrictions? (Select two)

A. Use georestriction to prevent users in specific geographic locations from accessing content that you're distributing through a Amazon CloudFront web distribution **(CORRECT)**
B. Use Amazon Route 53 based weighted routing policy to restrict distribution of content to only the locations in which you have distribution rights
C. Use Amazon Route 53 based failover routing policy to restrict distribution of content to only the locations in which you have distribution rights
D. Use Amazon Route 53 based geolocation routing policy to restrict distribution of content to only the locations in which you have distribution rights **(CORRECT)**
E. Use Amazon Route 53 based latency-based routing policy to restrict distribution of content to only the locations in which you have distribution rights

**Answer:** A, D
---

## Question 35
**Domain:** Design Cost-Optimized Architectures

A leading video streaming service delivers billions of hours of content from Amazon Simple Storage Service (Amazon S3) to customers around the world. Amazon S3 also serves as the data lake for its big data analytics solution. The data lake has a staging zone where intermediary query results are kept only for 24 hours. These results are also heavily referenced by other parts of the analytics pipeline.
Which of the following is the MOST cost-effective strategy for storing this intermediary query data?

A. Store the intermediary query results in Amazon S3 One Zone-Infrequent Access storage class
B. Store the intermediary query results in Amazon S3 Glacier Instant Retrieval storage class
C. Store the intermediary query results in Amazon S3 Standard storage class **(CORRECT)**
D. Store the intermediary query results in Amazon S3 Standard-Infrequent Access storage class

**Answer:** C
---

## Question 36
**Domain:** Design High-Performing Architectures

A junior scientist working with the Deep Space Research Laboratory at NASA is trying to upload a high-resolution image of a nebula into Amazon S3. The image size is approximately 3 gigabytes. The junior scientist is using Amazon S3 Transfer Acceleration (Amazon S3TA) for faster image upload. It turns out that Amazon S3TA did not result in an accelerated transfer.
Given this scenario, which of the following is correct regarding the charges for this image transfer?

A. The junior scientist does not need to pay any transfer charges for the image upload **(CORRECT)**
B. The junior scientist only needs to pay S3TA transfer charges for the image upload
C. The junior scientist only needs to pay Amazon S3 transfer charges for the image upload
D. The junior scientist needs to pay both S3 transfer charges and S3TA transfer charges for the image upload

**Answer:** A
---

## Question 37
**Domain:** Design Secure Architectures

An IT company wants to review its security best-practices after an incident was reported where a new developer on the team was assigned full access to Amazon DynamoDB. The developer accidentally deleted a couple of tables from the production environment while building out a new feature.
Which is the MOST effective way to address this issue so that such incidents do not recur?

A. Use permissions boundary to control the maximum permissions employees can grant to the IAM principals **(CORRECT)**
B. Only root user should have full database access in the organization
C. The CTO should review the permissions for each new developer's IAM user so that such incidents don't recur
D. Remove full database access for all IAM users in the organization

**Answer:** A
---

## Question 38
**Domain:** Design High-Performing Architectures

The engineering team at an e-commerce company wants to establish a dedicated, encrypted, low latency, and high throughput connection between its data center and AWS Cloud. The engineering team has set aside sufficient time to account for the operational overhead of establishing this connection.
As a solutions architect, which of the following solutions would you recommend to the company?

A. Use AWS site-to-site VPN to establish a connection between the data center and AWS Cloud
B. Use AWS Direct Connect to establish a connection between the data center and AWS Cloud
C. Use AWS Direct Connect plus virtual private network (VPN) to establish a connection between the data center and AWS Cloud **(CORRECT)**
D. Use AWS Transit Gateway to establish a connection between the data center and AWS Cloud

**Answer:** C
---

## Question 39
**Domain:** Design Secure Architectures

A company has moved its business critical data to Amazon Elastic File System (Amazon EFS) which will be accessed by multiple Amazon EC2 instances.
As an AWS Certified Solutions Architect - Associate, which of the following would you recommend to exercise access control such that only the permitted Amazon EC2 instances can read from the Amazon EFS file system? (Select two)

A. Use VPC security groups to control the network traffic to and from your file system **(CORRECT)**
B. Use network access control list (network ACL) to control the network traffic to and from your Amazon EC2 instance
C. Use Amazon GuardDuty to curb unwanted access to Amazon EFS file system
D. Set up the IAM policy root credentials to control and configure the clients accessing the Amazon EFS file system
E. Use an IAM policy to control access for clients who can mount your file system with the required permissions **(CORRECT)**

**Answer:** A, E
---

## Question 40
**Domain:** Design High-Performing Architectures

A gaming company is developing a mobile game that streams score updates to a backend processor and then publishes results on a leaderboard. The company has hired you as an AWS Certified Solutions Architect Associate to design a solution that can handle major traffic spikes, process the mobile game updates in the order of receipt, and store the processed updates in a highly available database. The company wants to minimize the management overhead required to maintain the solution.
Which of the following will you recommend to meet these requirements?

A. Push score updates to an Amazon Simple Notification Service (Amazon SNS) topic, subscribe an AWS Lambda function to this Amazon SNS topic to process the updates and then store these processed updates in a SQL database running on Amazon EC2 instance
B. Push score updates to Amazon Kinesis Data Streams which uses an AWS Lambda function to process these updates and then store these processed updates in Amazon DynamoDB **(CORRECT)**
C. Push score updates to Amazon Kinesis Data Streams which uses a fleet of Amazon EC2 instances (with Auto Scaling) to process the updates in Amazon Kinesis Data Streams and then store these processed updates in Amazon DynamoDB
D. Push score updates to an Amazon Simple Queue Service (Amazon SQS) queue which uses a fleet of Amazon EC2 instances (with Auto Scaling) to process these updates in the Amazon SQS queue and then store these processed updates in an Amazon RDS MySQL database

**Answer:** B
---

## Question 41
**Domain:** Design Secure Architectures

A healthcare company is developing a secure internal web portal hosted on AWS. The application must communicate with legacy systems that reside in the company's on-premises data centers. These data centers are connected to AWS via a site-to-site VPN. The company uses Amazon Route 53 as its DNS solution and requires the application to resolve private DNS records for the on-premises services from within its Amazon VPC.
What is the MOST secure and appropriate way to meet these DNS resolution requirements?

A. Create a Route 53 private hosted zone for the on-premises domain. Associate the hosted zone with the VPC to allow the application to resolve DNS names of the on-premises services
B. Configure a Route 53 Resolver inbound endpoint and create a DNS forwarding rule. Enable recursive DNS resolution in the VPC to access on-premises services
C. Create a Route 53 Resolver outbound endpoint. Define a forwarding rule that routes DNS queries for on-premises domains to the on-premises DNS server. Associate the rule with the VPC **(CORRECT)**
D. Create a hybrid connectivity gateway and attach the on-premises DNS servers to Route 53 as authoritative zones for internal domains

**Answer:** C
---

## Question 42
**Domain:** Design High-Performing Architectures

A digital wallet company plans to launch a new cloud-based service for processing user cash transfers and peer-to-peer payments. The application will receive transaction requests from mobile clients via a secure endpoint. Each transaction request must go through a lightweight validation step before being forwarded for backend processing, which includes fraud detection, ledger updates, and notifications. The backend workload is compute- and memory-intensive, requires scaling based on volume, and must run for a longer duration than typical short-lived tasks. The engineering team prefers a fully managed solution that minimizes infrastructure maintenance, including provisioning and patching of virtual machines or containers.
Which solution will meet these requirements with the LEAST operational overhead?

A. Create an Amazon API Gateway endpoint to receive transaction requests from mobile devices. Use AWS Lambda to validate the transactions. For backend processing, deploy the application on Amazon EKS Anywhere, running on on-premises servers in the company’s data center. Use a custom provisioning script to scale Kubernetes worker nodes based on transaction volume
B. Expose an Amazon API Gateway REST API endpoint to receive transaction requests from mobile clients. Integrate the API with AWS Lambda to perform basic validation. For backend processing, deploy the long-running application to Amazon ECS using the Fargate launch type, allowing ECS to manage compute and memory provisioning automatically, with no server management required **(CORRECT)**
C. Build a REST API using Amazon API Gateway. Integrate it with an AWS Step Functions state machine for validation. Launch the backend application using Amazon EKS with self-managed nodes, and use Kubernetes Jobs to handle transaction processing workflows. Manually scale the cluster based on demand
D. Configure Amazon SQS to receive encrypted payment notifications from mobile devices. Use Amazon EventBridge rules to extract the payload and perform validation. Route the messages to a backend system hosted on Amazon Lightsail instances with dynamic scaling policies based on memory thresholds and instance health checks

**Answer:** B
---

## Question 43
**Domain:** Design Resilient Architectures

The DevOps team at an e-commerce company wants to perform some maintenance work on a specific Amazon EC2 instance that is part of an Auto Scaling group using a step scaling policy. The team is facing a maintenance challenge - every time the team deploys a maintenance patch, the instance health check status shows as out of service for a few minutes. This causes the Auto Scaling group to provision another replacement instance immediately.
As a solutions architect, which are the MOST time/resource efficient steps that you would recommend so that the maintenance work can be completed at the earliest? (Select two)

A. Delete the Auto Scaling group and apply the maintenance fix to the given instance. Create a new Auto Scaling group and add all the instances again using the manual scaling policy
B. Suspend the 
ScheduledActions
 process type for the Auto Scaling group and apply the maintenance patch to the instance. Once the instance is ready, you can you can manually set the instance's health status back to healthy and activate the 
ScheduledActions
 process type again
C. Put the instance into the Standby state and then update the instance by applying the maintenance patch. Once the instance is ready, you can exit the Standby state and then return the instance to service **(CORRECT)**
D. Take a snapshot of the instance, create a new Amazon Machine Image (AMI) and then launch a new instance using this AMI. Apply the maintenance patch to this new instance and then add it back to the Auto Scaling Group by using the manual scaling policy. Terminate the earlier instance that had the maintenance issue
E. Suspend the 
ReplaceUnhealthy
 process type for the Auto Scaling group and apply the maintenance patch to the instance. Once the instance is ready, you can manually set the instance's health status back to healthy and activate the 
ReplaceUnhealthy
 process type again **(CORRECT)**

**Answer:** C, E
---

## Question 44
**Domain:** Design High-Performing Architectures

The solo founder at a tech startup has just created a brand new AWS account. The founder has provisioned an Amazon EC2 instance 1A which is running in AWS Region A. Later, he takes a snapshot of the instance 1A and then creates a new Amazon Machine Image (AMI) in Region A from this snapshot. This AMI is then copied into another Region B. The founder provisions an instance 1B in Region B using this new AMI in Region B.
At this point in time, what entities exist in Region B?

A. 1 Amazon EC2 instance, 1 AMI and 1 snapshot exist in Region B **(CORRECT)**
B. 1 Amazon EC2 instance and 2 AMIs exist in Region B
C. 1 Amazon EC2 instance and 1 AMI exist in Region B
D. 1 Amazon EC2 instance and 1 snapshot exist in Region B

**Answer:** A
---

## Question 45
**Domain:** Design High-Performing Architectures

A retail analytics company operates a large-scale data lake on Amazon S3, where they store daily logs of customer transactions, product views, and inventory updates. Each morning, they need to transform and load the data into a data warehouse to support fast analytical queries. The company also wants to enable data analysts to build and train machine learning (ML) models using familiar SQL syntax without writing custom Python code. The architecture must support massively parallel processing (MPP) for fast data aggregation and scoring, and must use serverless AWS services wherever possible to reduce infrastructure management and operational overhead.
Which solution best meets these requirements?

A. Use a daily AWS Glue job to transform and clean the data stored in Amazon S3. Load the transformed dataset into Amazon Redshift Serverless, which offers MPP capabilities in a serverless model. Enable analysts to use Amazon Redshift ML to build and train ML models **(CORRECT)**
B. Run a daily AWS Glue job to process and transform the raw files in S3 and register the outputs as Amazon Athena tables in AWS Glue Data Catalog. Allow analysts to build ML models using Amazon Athena ML, with SQL-based predictions on top of S3 data without moving it to a warehouse
C. Provision and run a daily Amazon EMR cluster with Apache Spark to process and transform the S3 data. Load the results into Amazon Redshift (provisioned). Enable ML model development by integrating Redshift with Amazon SageMaker notebooks for advanced modeling tasks
D. Use an AWS Glue job to transform and load data into Amazon RDS for PostgreSQL. Allow analysts to run machine learning models using Amazon Aurora ML integrated with PostgreSQL, leveraging Amazon SageMaker endpoints behind the scenes

**Answer:** A
---

## Question 46
**Domain:** Design High-Performing Architectures

A retail company's dynamic website is hosted using on-premises servers in its data center in the United States. The company is launching its website in Asia, and it wants to optimize the website loading times for new users in Asia. The website's backend must remain in the United States. The website is being launched in a few days, and an immediate solution is needed.
What would you recommend?

A. Use Amazon CloudFront with a custom origin pointing to the on-premises servers **(CORRECT)**
B. Migrate the website to Amazon S3. Use S3 cross-region replication (S3 CRR) between AWS Regions in the US and Asia
C. Use Amazon CloudFront with a custom origin pointing to the DNS record of the website on Amazon Route 53
D. Leverage a Amazon Route 53 geo-proximity routing policy pointing to on-premises servers

**Answer:** A
---

## Question 47
**Domain:** Design Secure Architectures

A US-based healthcare startup is building an interactive diagnostic tool for COVID-19 related assessments. The users would be required to capture their personal health records via this tool. As this is sensitive health information, the backup of the user data must be kept encrypted in Amazon Simple Storage Service (Amazon S3). The startup does not want to provide its own encryption keys but still wants to maintain an audit trail of when an encryption key was used and by whom.
Which of the following is the BEST solution for this use-case?

A. Use server-side encryption with AWS Key Management Service keys (SSE-KMS) to encrypt the user data on Amazon S3 **(CORRECT)**
B. Use server-side encryption with customer-provided keys (SSE-C) to encrypt the user data on Amazon S3
C. Use server-side encryption with Amazon S3 managed keys (SSE-S3) to encrypt the user data on Amazon S3
D. Use client-side encryption with client provided keys and then upload the encrypted user data to Amazon S3

**Answer:** A
---

## Question 48
**Domain:** Design Resilient Architectures

A new DevOps engineer has just joined a development team and wants to understand the replication capabilities for Amazon RDS Multi-AZ deployment as well as Amazon RDS Read-replicas.
Which of the following correctly summarizes these capabilities for the given database?

A. Multi-AZ follows synchronous replication and spans at least two Availability Zones (AZs) within a single region. Read replicas follow asynchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region **(CORRECT)**
B. Multi-AZ follows asynchronous replication and spans one Availability Zone (AZ) within a single region. Read replicas follow synchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region
C. Multi-AZ follows asynchronous replication and spans at least two Availability Zones (AZs) within a single region. Read replicas follow synchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region
D. Multi-AZ follows asynchronous replication and spans at least two Availability Zones (AZs) within a single region. Read replicas follow asynchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region

**Answer:** A
---

## Question 49
**Domain:** Design Secure Architectures

An IT consultant is helping the owner of a medium-sized business set up an AWS account. What are the security recommendations he must follow while creating the AWS account root user? (Select two)

A. Create a strong password for the AWS account root user **(CORRECT)**
B. Send an email to the business owner with details of the login username and password for the AWS root user. This will help the business owner to troubleshoot any login issues in future
C. Encrypt the access keys and save them on Amazon S3
D. Create AWS account root user access keys and share those keys only with the business owner
E. Enable Multi Factor Authentication (MFA) for the AWS account root user account **(CORRECT)**

**Answer:** A, E
---

## Question 50
**Domain:** Design Cost-Optimized Architectures

A technology blogger wants to write a review on the comparative pricing for various storage types available on AWS Cloud. The blogger has created a test file of size 1 gigabytes with some random data. Next he copies this test file into AWS S3 Standard storage class, provisions an Amazon EBS volume (General Purpose SSD (gp2)) with 100 gigabytes of provisioned storage and copies the test file into the Amazon EBS volume, and lastly copies the test file into an Amazon EFS Standard Storage filesystem. At the end of the month, he analyses the bill for costs incurred on the respective storage types for the test file.
What is the correct order of the storage charges incurred for the test file on these three storage types?

A. Cost of test file storage on Amazon EFS < Cost of test file storage on Amazon S3 Standard < Cost of test file storage on Amazon EBS
B. Cost of test file storage on Amazon S3 Standard < Cost of test file storage on Amazon EFS < Cost of test file storage on Amazon EBS **(CORRECT)**
C. Cost of test file storage on Amazon S3 Standard < Cost of test file storage on Amazon EBS < Cost of test file storage on Amazon EFS
D. Cost of test file storage on Amazon EBS < Cost of test file storage on Amazon S3 Standard < Cost of test file storage on Amazon EFS

**Answer:** B
---

## Question 51
**Domain:** Design High-Performing Architectures

The sourcing team at the US headquarters of a global e-commerce company is preparing a spreadsheet of the new product catalog. The spreadsheet is saved on an Amazon Elastic File System (Amazon EFS) created in 
us-east-1
 region. The sourcing team counterparts from other AWS regions such as Asia Pacific and Europe also want to collaborate on this spreadsheet.
As a solutions architect, what is your recommendation to enable this collaboration with the LEAST amount of operational overhead?

A. The spreadsheet on the Amazon Elastic File System (Amazon EFS) can be accessed in other AWS regions by using an inter-region VPC peering connection **(CORRECT)**
B. The spreadsheet data will have to be moved into an Amazon RDS for MySQL database which can then be accessed from any AWS region
C. The spreadsheet will have to be copied into Amazon EFS file systems of other AWS regions as Amazon EFS is a regional service and it does not allow access from other AWS regions
D. The spreadsheet will have to be copied in Amazon S3 which can then be accessed from any AWS region

**Answer:** A
---

## Question 52
**Domain:** Design High-Performing Architectures

An Electronic Design Automation (EDA) application produces massive volumes of data that can be divided into two categories. The 'hot data' needs to be both processed and stored quickly in a parallel and distributed fashion. The 'cold data' needs to be kept for reference with quick access for reads and updates at a low cost.
Which of the following AWS services is BEST suited to accelerate the aforementioned chip design process?

A. Amazon FSx for Windows File Server
B. Amazon EMR
C. Amazon FSx for Lustre **(CORRECT)**
D. AWS Glue

**Answer:** C
---

## Question 53
**Domain:** Design Resilient Architectures

While consolidating logs for the weekly reporting, a development team at an e-commerce company noticed that an unusually large number of illegal AWS application programming interface (API) queries were made sometime during the week. Due to the off-season, there was no visible impact on the systems. However, this event led the management team to seek an automated solution that can trigger near-real-time warnings in case such an event recurs.
Which of the following represents the best solution for the given scenario?

A. Create an Amazon CloudWatch metric filter that processes AWS CloudTrail logs having API call details and looks at any errors by factoring in all the error codes that need to be tracked. Create an alarm based on this metric's rate to send an Amazon SNS notification to the required team **(CORRECT)**
B. Run Amazon Athena SQL queries against AWS CloudTrail log files stored in Amazon S3 buckets. Use Amazon QuickSight to generate reports for managerial dashboards
C. Configure AWS CloudTrail to stream event data to Amazon Kinesis. Use Amazon Kinesis stream-level metrics in the Amazon CloudWatch to trigger an AWS Lambda function that will trigger an error workflow
D. AWS Trusted Advisor publishes metrics about check results to Amazon CloudWatch. Create an alarm to track status changes for checks in the Service Limits category for the APIs. The alarm will then notify when the service quota is reached or exceeded

**Answer:** A
---

## Question 54
**Domain:** Design Cost-Optimized Architectures

A retail company has developed a REST API which is deployed in an Auto Scaling group behind an Application Load Balancer. The REST API stores the user data in Amazon DynamoDB and any static content, such as images, are served via Amazon Simple Storage Service (Amazon S3). On analyzing the usage trends, it is found that 90% of the read requests are for commonly accessed data across all users.
As a Solutions Architect, which of the following would you suggest as the MOST efficient solution to improve the application performance?

A. Enable ElastiCache Redis for DynamoDB and ElastiCache Memcached for Amazon S3
B. Enable ElastiCache Redis for DynamoDB and Amazon CloudFront for Amazon S3
C. Enable Amazon DynamoDB Accelerator (DAX) for Amazon DynamoDB and Amazon CloudFront for Amazon S3 **(CORRECT)**
D. Enable Amazon DynamoDB Accelerator (DAX) for Amazon DynamoDB and ElastiCache Memcached for Amazon S3

**Answer:** C
---

## Question 55
**Domain:** Design Resilient Architectures

A government agency is developing a online application to assist users in submitting permit requests through a web-based interface. The system architecture consists of a front-end web application tier and a background processing tier that handles the validation and submission of the forms. The application is expected to see high traffic and it must ensure that every submitted request is processed exactly once, with no loss of data.
Which design choice best satisfies these requirements?

A. Implement an Amazon SQS standard queue to reliably buffer and deliver form submissions from the web application layer to the processing tier
B. Leverage Amazon EventBridge to send events from the web application to the processing tier for asynchronous form handling
C. Implement an Amazon SQS FIFO queue to reliably buffer and deliver form submissions from the web application layer to the processing tier **(CORRECT)**
D. Leverage Amazon API Gateway to pass the form submissions to AWS Lambda for processing in real time

**Answer:** C
---

## Question 56
**Domain:** Design Cost-Optimized Architectures

A news network uses Amazon Simple Storage Service (Amazon S3) to aggregate the raw video footage from its reporting teams across the US. The news network has recently expanded into new geographies in Europe and Asia. The technical teams at the overseas branch offices have reported huge delays in uploading large video files to the destination Amazon S3 bucket.
Which of the following are the MOST cost-effective options to improve the file upload speed into Amazon S3 (Select two)

A. Create multiple AWS Direct Connect connections between the AWS Cloud and branch offices in Europe and Asia. Use the direct connect connections for faster file uploads into Amazon S3
B. Use Amazon S3 Transfer Acceleration (Amazon S3TA) to enable faster file uploads into the destination S3 bucket **(CORRECT)**
C. Create multiple AWS Site-to-Site VPN connections between the AWS Cloud and branch offices in Europe and Asia. Use these VPN connections for faster file uploads into Amazon S3
D. Use multipart uploads for faster file uploads into the destination Amazon S3 bucket **(CORRECT)**
E. Use AWS Global Accelerator for faster file uploads into the destination Amazon S3 bucket

**Answer:** B, D
---

## Question 57
**Domain:** Design High-Performing Architectures

A digital event-ticketing platform hosts its core transaction-processing service on AWS. The service runs on Amazon EC2 instances and stores finalized transactions in an Amazon Aurora PostgreSQL database. During periods of high user activity - such as flash ticket sales or holiday promotions - the application begins timing out, causing failed or delayed purchases. A solutions architect has been asked to redesign the backend for scalability and cost-efficiency, without reengineering the database layer.
Which combination of actions will meet these goals in the most cost-effective and scalable manner? (Select two)

A. Modify the application to publish purchase events to an Amazon SQS queue. Launch an Auto Scaling group of EC2 workers that poll the queue and process purchases asynchronously **(CORRECT)**
B. Use an Amazon ElastiCache cluster to cache database queries. Configure the application to store purchase transactions in the cache before writing to the database
C. Deploy read replicas for the Aurora database in another Region and configure EC2 instances to read and write from the nearest replica based on latency
D. Implement Amazon RDS Proxy between the application and the Aurora PostgreSQL cluster. Deploy EC2 instances in an Auto Scaling group to retry transactions as needed **(CORRECT)**
E. Deploy an Amazon API Gateway with throttling and usage plans to slow down incoming purchase requests during peak times and maintain application stability

**Answer:** A, D
---

## Question 58
**Domain:** Design High-Performing Architectures

A software engineering intern at an e-commerce company is documenting the process flow to provision Amazon EC2 instances via the Amazon EC2 API. These instances are to be used for an internal application that processes Human Resources payroll data. He wants to highlight those volume types that cannot be used as a boot volume.
Can you help the intern by identifying those storage volume types that CANNOT be used as boot volumes while creating the instances? (Select two)

A. Cold Hard disk drive (sc1) **(CORRECT)**
B. General Purpose Solid State Drive (gp2)
C. Instance Store
D. Provisioned IOPS Solid state drive (io1)
E. Throughput Optimized Hard disk drive (st1) **(CORRECT)**

**Answer:** A, E
---

## Question 59
**Domain:** Design Resilient Architectures

A major bank is using Amazon Simple Queue Service (Amazon SQS) to migrate several core banking applications to the cloud to ensure high availability and cost efficiency while simplifying administrative complexity and overhead. The development team at the bank expects a peak rate of about 1000 messages per second to be processed via SQS. It is important that the messages are processed in order.
Which of the following options can be used to implement this system?

A. Use Amazon SQS standard queue to process the messages
B. Use Amazon SQS FIFO (First-In-First-Out) queue in batch mode of 4 messages per operation to process the messages at the peak rate **(CORRECT)**
C. Use Amazon SQS FIFO (First-In-First-Out) queue in batch mode of 2 messages per operation to process the messages at the peak rate
D. Use Amazon SQS FIFO (First-In-First-Out) queue to process the messages

**Answer:** B
---

## Question 60
**Domain:** Design Resilient Architectures

An e-commerce company is looking for a solution with high availability, as it plans to migrate its flagship application to a fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances. The solution should allow for content-based routing as part of the architecture.
As a Solutions Architect, which of the following will you suggest for the company?

A. Use an Auto Scaling group for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure a Public IP address to mask any failure of an instance
B. Use an Auto Scaling group for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure an elastic IP address (EIP) to mask any failure of an instance
C. Use an Application Load Balancer for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure Auto Scaling group to mask any failure of an instance **(CORRECT)**
D. Use a Network Load Balancer for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure a Private IP address to mask any failure of an instance

**Answer:** C
---

## Question 61
**Domain:** Design Cost-Optimized Architectures

The IT department at a consulting firm is conducting a training workshop for new developers. As part of an evaluation exercise on Amazon S3, the new developers were asked to identify the invalid storage class lifecycle transitions for objects stored on Amazon S3.
Can you spot the INVALID lifecycle transitions from the options below? (Select two)

A. Amazon S3 Standard-IA => Amazon S3 One Zone-IA
B. Amazon S3 Standard => Amazon S3 Intelligent-Tiering
C. Amazon S3 Intelligent-Tiering => Amazon S3 Standard **(CORRECT)**
D. Amazon S3 One Zone-IA => Amazon S3 Standard-IA **(CORRECT)**
E. Amazon S3 Standard-IA => Amazon S3 Intelligent-Tiering

**Answer:** C, D
---

## Question 62
**Domain:** Design Secure Architectures

A biotech research company needs to perform data analytics on real-time lab results provided by a partner organization. The partner stores these lab results in an Amazon RDS for MySQL instance within the partner’s own AWS account. The research company has a private VPC that does not have internet access, Direct Connect, or a VPN connection. However, the company must establish secure and private connectivity to the RDS database in the partner’s VPC. The solution must allow the research company to connect from its VPC while minimizing complexity and complying with data security requirements.
Which solution will meet these requirements?

A. Set up VPC peering between the company’s VPC and the partner’s VPC. Use AWS Transit Gateway in the partner's account to route traffic from the company’s VPC to the database. Modify the RDS subnet route tables to allow access from the company’s CIDR block
B. Instruct the partner to create a Network Load Balancer (NLB) in front of the Amazon RDS for MySQL instance. Use AWS PrivateLink to expose the NLB as an interface VPC endpoint in the research company’s VPC **(CORRECT)**
C. Configure a client VPN endpoint in the company’s account. Have researchers connect to the VPN from their local machines. Establish a Direct Connect gateway to the partner’s VPC and route RDS traffic via this connection
D. Instruct the partner to enable public access on the Amazon RDS instance and add a security group rule to allow inbound access from the company’s IP range. The company accesses the database over the public internet through a NAT Gateway configured in a private subnet

**Answer:** B
---

## Question 63
**Domain:** Design High-Performing Architectures

The engineering team at a data analytics company has observed that its flagship application functions at its peak performance when the underlying Amazon Elastic Compute Cloud (Amazon EC2) instances have a CPU utilization of about 50%. The application is built on a fleet of Amazon EC2 instances managed under an Auto Scaling group. The workflow requests are handled by an internal Application Load Balancer that routes the requests to the instances.
As a solutions architect, what would you recommend so that the application runs near its peak performance state?

A. Configure the Auto Scaling group to use target tracking policy and set the CPU utilization as the target metric with a target value of 50% **(CORRECT)**
B. Configure the Auto Scaling group to use simple scaling policy and set the CPU utilization as the target metric with a target value of 50%
C. Configure the Auto Scaling group to use a Amazon Cloudwatch alarm triggered on a CPU utilization threshold of 50%
D. Configure the Auto Scaling group to use step scaling policy and set the CPU utilization as the target metric with a target value of 50%

**Answer:** A
---

## Question 64
**Domain:** Design High-Performing Architectures

A file-hosting service uses Amazon Simple Storage Service (Amazon S3) under the hood to power its storage offerings. Currently all the customer files are uploaded directly under a single Amazon S3 bucket. The engineering team has started seeing scalability issues where customer file uploads have started failing during the peak access hours with more than 5000 requests per second.
Which of the following is the MOST resource efficient and cost-optimal way of addressing this issue?

A. Change the application architecture to create a new Amazon S3 bucket for each day's data and then upload the daily files directly under that day's bucket
B. Change the application architecture to use Amazon Elastic File System (Amazon EFS) instead of Amazon S3 for storing the customers' uploaded files
C. Change the application architecture to create a new Amazon S3 bucket for each customer and then upload each customer's files directly under the respective buckets
D. Change the application architecture to create customer-specific custom prefixes within the single Amazon S3 bucket and then upload the daily files into those prefixed locations **(CORRECT)**

**Answer:** D
---

## Question 65
**Domain:** Design High-Performing Architectures

The DevOps team at an e-commerce company has deployed a fleet of Amazon EC2 instances under an Auto Scaling group (ASG). The instances under the ASG span two Availability Zones (AZ) within the 
us-east-1
 region. All the incoming requests are handled by an Application Load Balancer (ALB) that routes the requests to the Amazon EC2 instances under the Auto Scaling Group. As part of a test run, two instances (instance 1 and 2, belonging to AZ A) were manually terminated by the DevOps team causing the Availability Zones (AZ) to have unbalanced resources. Later that day, another instance (belonging to AZ B) was detected as unhealthy by the Application Load Balancer's health check.
Can you identify the correct outcomes for these events? (Select two)

A. Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously
B. As the resources are unbalanced in the Availability Zones, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application **(CORRECT)**
C. Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it
D. As the resources are unbalanced in the Availability Zones, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched
E. Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance **(CORRECT)**

**Answer:** B, E