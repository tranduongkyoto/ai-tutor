# Timed Mode Set 5 – AWS Certified Solutions Architect Professional (Tutorials Dojo)

**Kết quả:** 31/75 câu đúng (41.33%) — ❌ Chưa đạt

## Điểm theo domain

| Domain | Tỉ lệ đúng |
|---|---|
| CSAP – Accelerate Workload Migration and Modernization | 27.78% |
| CSAP – Continuous Improvement for Existing Solutions | 52.94% |
| CSAP – Design for New Solutions | 36.36% |
| CSAP – Design Solutions for Organizational Complexity | 50% |

## Bảng tổng hợp

| Câu | Kết quả | Bạn chọn | Đáp án đúng |
|---|---|---|---|
| 1 | ❌ Sai | B | D |
| 2 | ✅ Đúng | A | A |
| 3 | ✅ Đúng | A, D | A, D |
| 4 | ❌ Sai | C | A |
| 5 | ❌ Sai | B, C | C, D |
| 6 | ✅ Đúng | D, E | D, E |
| 7 | ✅ Đúng | D | D |
| 8 | ❌ Sai | D | B |
| 9 | ❌ Sai | B, E | A, C |
| 10 | ❌ Sai | A | C |
| 11 | ✅ Đúng | C | C |
| 12 | ❌ Sai | B, C | A, D |
| 13 | ❌ Sai | A, D | B, E |
| 14 | ❌ Sai | D | C |
| 15 | ❌ Sai | A | C |
| 16 | ❌ Sai | A | D |
| 17 | ✅ Đúng | A | A |
| 18 | ❌ Sai | D | A |
| 19 | ❌ Sai | C | B |
| 20 | ❌ Sai | D | B |
| 21 | ❌ Sai | A, E | C, E |
| 22 | ❌ Sai | D | C |
| 23 | ❌ Sai | A, B, C | A, B, F |
| 24 | ❌ Sai | B | C |
| 25 | ✅ Đúng | A | A |
| 26 | ✅ Đúng | A | A |
| 27 | ✅ Đúng | B | B |
| 28 | ❌ Sai | B, D | B, C |
| 29 | ❌ Sai | C | A |
| 30 | ❌ Sai | D, E, F | C, D, E |
| 31 | ❌ Sai | D, E, F | A, B, D |
| 32 | ❌ Sai | D | C |
| 33 | ❌ Sai | D, E, F | B, C, D |
| 34 | ✅ Đúng | B | B |
| 35 | ❌ Sai | D, E | B, E |
| 36 | ❌ Sai | D, E | A, D |
| 37 | ✅ Đúng | C | C |
| 38 | ❌ Sai | D, E | B, D |
| 39 | ✅ Đúng | C | C |
| 40 | ✅ Đúng | B, C | B, C |
| 41 | ✅ Đúng | A | A |
| 42 | ❌ Sai | A | D |
| 43 | ✅ Đúng | C | C |
| 44 | ✅ Đúng | B | B |
| 45 | ✅ Đúng | B | B |
| 46 | ✅ Đúng | C | C |
| 47 | ✅ Đúng | C | C |
| 48 | ❌ Sai | A | B |
| 49 | ❌ Sai | A | B |
| 50 | ✅ Đúng | B, C | B, C |
| 51 | ❌ Sai | C | A |
| 52 | ✅ Đúng | A | A |
| 53 | ✅ Đúng | B | B |
| 54 | ❌ Sai | A | B |
| 55 | ❌ Sai | D | A |
| 56 | ✅ Đúng | A, C | A, C |
| 57 | ❌ Sai | C | A |
| 58 | ❌ Sai | A, E | B, E |
| 59 | ✅ Đúng | D | D |
| 60 | ✅ Đúng | B | B |
| 61 | ❌ Sai | C | D |
| 62 | ❌ Sai | D, E | C, D |
| 63 | ❌ Sai | C | B |
| 64 | ✅ Đúng | A | A |
| 65 | ✅ Đúng | A | A |
| 66 | ✅ Đúng | A | A |
| 67 | ❌ Sai | B, D | D, E |
| 68 | ❌ Sai | A | D |
| 69 | ❌ Sai | C | A |
| 70 | ✅ Đúng | C | C |
| 71 | ✅ Đúng | D | D |
| 72 | ❌ Sai | C | D |
| 73 | ❌ Sai | D | A |
| 74 | ❌ Sai | A | D |
| 75 | ✅ Đúng | D | D |

**Các câu sai (44):** 1, 4, 5, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 28, 29, 30, 31, 32, 33, 35, 36, 38, 42, 48, 49, 51, 54, 55, 57, 58, 61, 62, 63, 67, 68, 69, 72, 73, 74

---

# Chi tiết từng câu

## Câu 1 — ❌ SAI

### Câu hỏi

A company offers financial services and big data analytics for its partners. It receives about 4,000 credit card transaction records every 15 minutes from its partners which are stored on an encrypted Amazon S3 bucket. This data contains sensitive information such as the primary account number (PAN). The company needs to mask the PAN immediately before sending the data to another S3 bucket for additional processing. The next step is to remove and merge specific fields, and then transform each transaction record in JSON format. More fields are expected to be added in the future so the solution must be easily expandable to accommodate the transformation requirements.

Which of the following options is the recommended solution to meet the company requirements?

### Các phương án

- **A.** Use AWS Data Exchange to acquire the data and store it in an Amazon S3 bucket. Upon file delivery, perform an Amazon Athena query to start an Amazon EMR ETL job to transform each record according to requirements. Set the output to JSON format, and send it to another S3 bucket for additional processing. Scale down the EMR cluster afterward.
- **B.** Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. Configure AWS Fargate to automatically scale depending on the number of messages on the SQS queue. Have the Fargate application transform each record according to requirements and send the JSON formatted output to another S3 bucket for additional processing. 👈 *(bạn chọn)*
- **C.** Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. For each message received on the SQS queue, run another Lambda function to transform the data according to requirements and store the results in a temporary S3 bucket. Trigger a final Lambda function for each delivery on the temporary S3 bucket to convert the data into JSON format. Send the final output to another S3 bucket.
- **D.** Configure an AWS Glue crawler and add a custom classifier based on the data format to build a matching table definition. Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it trigger an AWS Glue ETL job to transform each record according to requirements. Set the output to JSON format. After completion, configure the ETL job to send the results to another S3 bucket for additional processing. ✅

> **Bạn chọn:** B  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Glue is a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams. AWS Glue consists of a central metadata repository known as the AWS Glue Data Catalog, an ETL engine that automatically generates Python or Scala code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries. AWS Glue is serverless, so there’s no infrastructure to set up or manage.

You can use a crawler to populate the AWS Glue Data Catalog with tables. This is the primary method used by most AWS Glue users. A crawler can crawl multiple data stores in a single run. Upon completion, the crawler creates or updates one or more tables in your Data Catalog. A classifier reads the data in a data store. If it recognizes the format of the data, it generates a schema. The classifier also returns a “certainty” number to indicate how certain the format recognition was.

Therefore, the correct answer is: Configure an AWS Glue crawler and add a custom classifier based on the data format to build a matching table definition. Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it trigger an AWS Glue ETL job to transform each record according to requirements. Set the output to JSON format. After completion, configure the ETL job to send the results to another S3 bucket for additional processing. AWS Glue is designed for these ELT jobs and the crawler helps build a data catalog. The output of a classifier includes a string that indicates the file’s classification such as JSON format.

The option that says: Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. For each message received on the SQS queue, run another Lambda function to transform the data according to requirements and store the results in a temporary S3 bucket. Trigger a final Lambda function for each delivery on the temporary S3 bucket to convert the data into JSON format. Send the final output to another S3 bucket is incorrect. It is possible to use a series of functions for the transform job, however, this can be cumbersome to expand in the future as you will need to update the Lambda functions code for every field that needs to be transformed.

The option that says: Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. Configure and AWS Fargate service to automatically scale depending on the number of messages on the SQS queue. Have the Fargate application transform each record according to requirements and send the JSON formatted output to another S3 bucket for additional processing is incorrect. This may be possible, however, you will need to update the application and deploy the Fargate service for any transformation requirements in the future. Maintaining a Fargate cluster is not cost-effective compared to other solutions.

The option that says: Use AWS Data Exchange to acquire the data and store it in an Amazon S3 bucket. Upon file delivery, perform an Amazon Athena query to start an Amazon EMR ETL job to transform each record according to requirements. Set the output to JSON format, and send it to another S3 bucket for additional processing. Scale down the EMR cluster afterward is incorrect because AWS Data Exchange, which is primarily used for data transfer, does not provide any functionality to process or transform the data before it is stored in the S3 bucket. Moreover, it is not cost-effective to use Amazon Athena queries and an Amazon EMR cluster for a periodic ETL job. An AWS Glue ETL job is a more cost-effective solution.

 

References:

https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html

https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html

https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html

 

Check out this AWS Glue Cheat Sheet:

https://tutorialsdojo.com/aws-glue/

---

## Câu 2 — ✅ ĐÚNG

### Câu hỏi

An e-commerce enterprise is in the process of migrating its flagship application from a local data center to the AWS cloud. The web application architecture includes a load balancer, operates on a Linux-based environment, and utilizes a PostgreSQL database for data storage. The application handles high traffic volumes, especially during peak shopping seasons, requiring the infrastructure to scale efficiently and seamlessly.

The application needs a robust NFS-compatible storage system for its digital assets, such as product images and user-generated content. The proposed cloud infrastructure needs to have the flexibility to scale from 3 to 50 Amazon EC2 instances to handle unexpected traffic surges, without allowing any modifications to the application. Additionally, it must ensure data integrity and availability, safeguarding against data loss.

Which of the following options would fulfill the given requirements?

### Các phương án

- **A.** Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Transition the web application onto AWS Elastic Beanstalk, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage .ebextensions configuration files to mount the EFS onto the EC2 instances. Establish an Amazon Aurora database with PostgreSQL compatibility, separate from the Elastic Beanstalk setup. ✅ 👈 *(bạn chọn)*
- **B.** Use Amazon Elastic Block Store (EBS) with Multi-Attach capability. Transition the web application to AWS Elastic Beanstalk, incorporating a Network Load Balancer and an Auto Scaling group for adaptive scalability. Utilize .ebextensions scripts to mount the EBS volume to the EC2 instances. Within the Elastic Beanstalk environment, set up an Amazon RDS configured for PostgreSQL.
- **C.** Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Establish a launch template and an Auto Scaling group to initiate EC2 instances for the web application. Set up a Network Load Balancer for traffic management. Configure an Amazon Aurora database with PostgreSQL compatibility. Employ an EC2 Auto Scaling scale-in lifecycle hook to mount the EFS to the EC2 instances.
- **D.** Use Amazon S3 to serve as the file storage infrastructure. Transition the web application onto AWS Lambda, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage AWS SAM templates to mount the S3 bucket onto the Lambda functions. Establish an Amazon RDS database with PostgreSQL compatibility, separate from the Lambda setup.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon Elastic File System (EFS) is a fully managed service that makes it easy to set up and scale file storage in the Amazon Cloud. It’s designed to provide massively parallel shared access to thousands of Amazon EC2 instances, enabling your applications to achieve high levels of aggregate throughput and IOPS with consistent low latencies. This makes it a suitable choice for a robust NFS-compatible storage system for the application’s digital assets.

AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. This service would allow the e-commerce enterprise to easily migrate their web application to the cloud.

An Application Load Balancer operates at the application layer, which is the topmost layer in the Open Systems Interconnection (OSI) model. When a request arrives, the load balancer checks its set of listener rules in the order of their priority to determine which rule to apply. Once the appropriate rule is identified, the load balancer then chooses a target from the corresponding target group to handle the request. This, in combination with an Auto Scaling group, provides the flexibility to scale from 3 to 50 Amazon EC2 instances to handle unexpected traffic surges.

The .ebextensions configuration files are used to customize the software that runs on the EC2 instances of your Elastic Beanstalk environment. You can use .ebextensions configuration files to mount the EFS onto the EC2 instances.

Amazon Aurora is a relational database compatible with MySQL and PostgreSQL. It is designed for the cloud and offers the performance and availability of traditional enterprise databases along with the simplicity and cost-effectiveness of open-source databases. This makes it an ideal choice for the PostgreSQL database needed for the application.

Hence, the correct answer is: Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Transition the web application onto AWS Elastic Beanstalk, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage .ebextensions configuration files to mount the EFS onto the EC2 instances. Establish an Amazon Aurora database with PostgreSQL compatibility, separate from the Elastic Beanstalk setup.

The option that says: Use Amazon Elastic Block Store (EBS) with Multi-Attach capability. Transition the web application to AWS Elastic Beanstalk, incorporating a Network Load Balancer and an Auto Scaling group for adaptive scalability. Utilize .ebextensions scripts to mount the EBS volume to the EC2 instances. Within the Elastic Beanstalk environment, set up an Amazon RDS configured for PostgreSQL is incorrect because EBS with Multi-Attach is not NFS-compatible, which is a requirement for the application’s digital assets.

The option that says: Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Establish a launch template and an Auto Scaling group to initiate EC2 instances for the web application. Set up a Network Load Balancer for traffic management. Configure an Amazon Aurora database with PostgreSQL compatibility. Employ an EC2 Auto Scaling scale-in lifecycle hook to mount the EFS to the EC2 instances is incorrect because lifecycle hooks are not designed for mounting file systems, which is necessary for the application’s operation.

The option that says: Use Amazon S3 to serve as the file storage infrastructure. Transition the web application onto AWS Lambda, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage AWS SAM templates to mount the S3 bucket onto the Lambda functions. Establish an Amazon RDS database with PostgreSQL compatibility, separate from the Lambda setup is incorrect because Amazon S3 is not NFS-compatible and transitioning to AWS Lambda would require modifications to the application, which is against the requirements.

 

References:

https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/services-efs.html

 

Check out these Amazon EFS and AWS Elastic Beanstalk Cheat Sheets:

https://tutorialsdojo.com/amazon-efs/

---

## Câu 3 — ✅ ĐÚNG

### Câu hỏi

A company has developed an Optical Character Recognition (OCR) application that allows users to upload PDF files to an Amazon S3 bucket. The user-facing website is hosted on S3, and its content is distributed by Amazon CloudFront. When a user initiates an OCR job, the application makes a call to a REST API in Amazon API Gateway (Regional), which in turn invokes an AWS Lambda function asynchronously to start the OCR process. The OCR output’s S3 path is then stored in an Amazon DynamoDB table

Currently, the application stack is deployed in the us-east-1 AWS region. The company wants to expand its user base to include users from Asia and the Middle East and aims to improve latency for these users.

Which combination of steps is the most cost-effective approach that would meet this requirement? (Select TWO.)

### Các phương án

- **A.** Enable S3 Transfer Acceleration on the S3 bucket and update the application code to use the Transfer Acceleration endpoint. ✅ 👈 *(bạn chọn)*
- **B.** Upload the PDF files to an Amazon EBS-backed Amazon EC2 instance in the us-east-1 region. Create an AWS Global Accelerator for the EC2 instance. Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.
- **C.** Deploy additional Lambda functions and S3 buckets in Asia and Middle East regions. Set up cross-region S3 replication. Configure Route 53 Geolocation Routing to direct users to the closest regional resources.
- **D.** Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint. ✅ 👈 *(bạn chọn)*
- **E.** Migrate the DynamoDB table to Amazon Aurora Serverless and use an Amazon RDS Proxy in front of the Lambda function.

> **Bạn chọn:** A, D  
> **Đáp án đúng:** A, D  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon S3 Transfer Acceleration can speed up content transfers to and from Amazon S3 by as much as 50% – 500% for long-distance transfer of larger objects. Customers who have either web or mobile applications with widespread users or applications hosted far away from their S3 bucket can experience long and variable upload and download speeds over the Internet.

S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrive at an edge location, they are routed to Amazon S3 over an optimized network path.

In the given scenario, since Amazon CloudFront is already in use for distributing content, the focus for reducing latency should be on the user’s interactions with the API and the S3 bucket where PDF files are uploaded. Enabling Amazon S3 Transfer Acceleration (S3TA) would speed up file uploads to the bucket, while switching the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint would enhance API call performance for users worldwide, including those in Asia and the Middle East

Hence, the correct answers are:

– Enable S3 Transfer Acceleration on the S3 bucket and update the application code to use the Transfer Acceleration endpoint.

– Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.

The option that says: Migrate the DynamoDB table to Amazon Aurora Serverless and use an Amazon RDS Proxy in front of the Lambda function is incorrect. Simply switching to a relational database would not address the latency concerns for users in Asia and the Middle East.

The option that says: Upload the PDF files to an Amazon EBS-backed Amazon EC2 instance in the us-east-1 region. Create an AWS Global Accelerator for the EC2 instance. Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint is incorrect. The use of an EC2 instance would not only introduce additional operational overhead but also incur higher costs. AWS Global Accelerator is unnecessary since CloudFront is already handling global content distribution and latency reduction for HTTP/HTTPS content.

The option that says: Deploy additional Lambda functions and S3 buckets in Asia and Middle East regions. Set up cross-region S3 replication. Configure Route 53 Geolocation Routing to direct users to the closest regional resources is incorrect. Cross-region replication in Amazon S3 is typically used for disaster recovery, data archiving, or data migration purposes. Having multiple copies of data in different regions would increase storage costs.

 

References:

https://aws.amazon.com/s3/transfer-acceleration/

https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html

 

Check out these Amazon S3 and Amazon API Gateway Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-api-gateway/

---

## Câu 4 — ❌ SAI

### Câu hỏi

A company operates an on-premises VMware vSphere environment and is now mandated to move certain applications to Amazon EC2 instances. Any software stacks and configurations installed on the VMs must be preserved on the EC2 instances.

Which set of actions will meet the requirements?

### Các phương án

- **A.** Export Virtual Machines as an Open Virtualization Format (OVF). Create an S3 bucket in the same AWS Region as the target EC2 instances. Set up an IAM role for the VM Import/Export service. Run the AWS CLI import-image command. ✅
- **B.** Set up AWS Storage Gateway File Gateway on the on-premises VMware environment. Expose a Common Internet File System (CIFS) to share data to an S3 bucket. Run the CreateRestoreImageTask EC2 command.
- **C.** Install the Systems Manager Agent on the on-premises virtual machines and perform hybrid activation to register them as managed instances. Utilize EC2 Image Builder to create a golden AMI that mirrors the on-premises setup. Deploy EC2 instances using the golden AMI. 👈 *(bạn chọn)*
- **D.** Deploy an AWS DataSync agent to facilitate the synchronization of the on-premises Server Message Block (SMB) share to an S3 bucket. Spin up an EC2 instance and utilize the AWS SDK to access the data stored in the S3 bucket. Create an Amazon Machine Image (AMI) from the configured EC2 instance.

> **Bạn chọn:** C  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

VM Import/Export enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances and export them back to your on-premises environment. This offering allows you to leverage your existing investments in the virtual machines that you have built to meet your IT security, configuration management, and compliance requirements by bringing those virtual machines into Amazon EC2 as ready-to-use instances. You can also export imported instances back to your on-premises virtualization infrastructure, allowing you to deploy workloads across your IT infrastructure.

The general steps for importing using VM Import/Export are as follows:

Export your existing VM using a supported format.
Create an S3 bucket in the Region where you want to import your VMs
Set up an IAM role that gives the VM Import/Export service permission to access the S3 bucket.
Run the AWS CLI import-image command to import the VM image into an EC2 instance.

Hence, the correct answer in this scenario is: Export Virtual Machines as an Open Virtualization Format (OVF). Create an S3 bucket in the same AWS Region as the target EC2 instances. Set up an IAM role for the VM Import/Export service. Run the AWS CLI import-image command.

The option that says: Set up AWS Storage Gateway File Gateway on the on-premises VMware environment. Expose a Common Internet File System (CIFS) to share data to an S3 bucket. Run the CreateRestoreImageTask EC2 command is incorrect. AWS Storage Gateway File Gateway is primarily used for connecting on-premises systems with cloud-based storage. It’s not designed to import VM images and their configurations into EC2, which is what the scenario calls for. Moreover, the CreateRestoreImageTask EC2 command is used for restoring an Amazon Machine Image (AMI), not an imported VM image.

The option that says: Deploy an AWS DataSync agent to facilitate the synchronization of the on-premises Server Message Block (SMB) share to an S3 bucket. Spin up an EC2 instance and utilize the AWS SDK to access the data stored in the S3 bucket. Create an Amazon Machine Image (AMI) from the configured EC2 instance is incorrect. AWS DataSync is simply a data transfer service that makes it easier for you to move data between on-premises storage and Amazon S3 or Amazon EFS. While it’s effective for data synchronization, it doesn’t capture the state or configuration of a VM.

The option that says: Install the Systems Manager Agent on the on-premises virtual machines and perform hybrid activation to register them as managed instances. Utilize EC2 Image Builder to create a golden AMI that mirrors the on-premises setup. Deploy EC2 instances using the golden AMI is incorrect. AWS Systems Manager primarily helps you manage AWS resources and on-premises servers. While it does provide functionalities like automation, configuration, and patch compliance, it does not facilitate the direct import of virtual machines (VMs) from an on-premises environment to EC2 instances. Moreover, creating a golden AMI that mirrors an on-premises setup is a complicated and error-prone process. Even if you manage to create an AMI that is functionally similar, it won’t be a direct import of the on-premises VM. This means there’s a risk that the software stacks and configurations may not be preserved exactly as they are.

 

References:

https://aws.amazon.com/ec2/vm-import/

https://docs.aws.amazon.com/vm-import/latest/userguide/how-vm-import-export-works.html

https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html

---

## Câu 5 — ❌ SAI

### Câu hỏi

A media company has a pipeline that extracts information on photos uploaded to an Amazon S3 bucket. Each upload on the S3 bucket sends a notification to an Amazon SNS topic. The pipeline includes several AWS Lambda functions that are subscribed to the SNS topic. For each notification message, the functions are triggered to extract the metadata information from the corresponding S3 object which is then written to the Amazon RDS MySQL DB instance. During peak traffic, the users complain that metadata updates are slow or are sometimes lost. This is because the RDS CPU utilization becomes very high which causes the AWS Lambda invocations to fail.

Which of the following steps should be implemented to resolve this issue? (Select TWO.)

### Các phương án

- **A.** Create additional Amazon RDS read replicas in order to accommodate the increased load traffic during peak hours.
- **B.** Configure the Delivery Retry Policy of the SNS Topic to have multiple retries with exponential backoff. Set the Message Delivery Status Logging option of the SNS topic to allow the Lambda functions to retry processing the object. 👈 *(bạn chọn)*
- **C.** Implement an Amazon RDS Proxy in front of the Amazon RDS instance. Configure the AWS Lambda functions to use this proxy when connecting to the RDS instance. ✅ 👈 *(bạn chọn)*
- **D.** For each AWS Lambda function, implement an Amazon SQS standard queue that is subscribed to the Amazon SNS topic. Configure each Lambda function to consume the message from their corresponding SQS queue. ✅
- **E.** Ensure that RDS Data API is enabled for the Amazon RDS instance. Configure the AWS Lambda functions to use RDS Data API when connecting to the RDS instance.

> **Bạn chọn:** B, C  
> **Đáp án đúng:** C, D  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon RDS Proxy is a fully managed, highly available database proxy for Amazon Relational Database Service (RDS) that makes applications more scalable, more resilient to database failures, and more secure. Many applications, including those built on modern serverless architectures, can have a large number of open connections to the database server and may open and close database connections at a high rate, exhausting database memory and compute resources. By using Amazon RDS Proxy, you can allow your applications to pool and share database connections to improve their ability to scale.

RDS Proxy makes applications more resilient to database failures by automatically connecting to a standby DB instance while preserving application connections. RDS Proxy also enables you to enforce AWS Identity and Access Management (IAM) authentication for databases and securely store credentials in AWS Secrets Manager.

Using RDS Proxy, you can handle unpredictable surges in database traffic that otherwise might cause issues due to oversubscribing connections or creating new connections at a fast rate. RDS Proxy establishes a database connection pool and reuses connections in this pool without the memory and CPU overhead of opening a new database connection each time. To protect the database against oversubscription, you can control the number of database connections that are created.

RDS Proxy queues or throttles application connections that can’t be served immediately from the pool of connections. Although latencies might increase, your application can continue to scale without abruptly failing or overwhelming the database.

The option that says: Implement an Amazon RDS Proxy in front of the Amazon RDS instance. Configure the AWS Lambda functions to use this proxy when connecting to the RDS instance is correct. RDS Proxy allows applications to pool and share connections established with the database, improving database efficiency and application scalability, especially during write operations. 

The option that says: For each AWS Lambda function, implement an Amazon SQS standard queue that is subscribed to the Amazon SNS topic. Configure each Lambda function to consume the message from their corresponding SQS queue is correct. This will help pool the metadata information until the AWS Lambda functions can process and write them to the Amazon RDS instance.

The option that says: Configure the Delivery Retry Policy of the SNS Topic to have multiple retries with exponential backoff. Set the Message Delivery Status Logging option of the SNS topic to allow the Lambda functions to retry processing the object is incorrect. The retries from Lambda functions may alleviate the lost metadata problem; however, this will still result in slow metadata updates because the RDS instance is overwhelmed with write requests. 

The option that says: Ensure that RDS Data API is enabled for the Amazon RDS instance. Configure the AWS Lambda functions to use RDS Data API when connecting to the RDS instance is incorrect. RDS Data API is designed to be used for Aurora Serverless service, not for RDS instances. 

The option that says: Create additional Amazon RDS read replicas in order to accommodate the increased load traffic during peak hours is incorrect. RDS read replicas are read-only instances, they can’t accept the write requests from the Lambda functions. 

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html

https://aws.amazon.com/rds/proxy/

https://aws.amazon.com/about-aws/whats-new/2021/03/amazon-rds-proxy-adds-read-only-endpoints-for-amazon-aurora-replicas/

 

Check out the Amazon RDS Cheat Sheet:

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

---

## Câu 6 — ✅ ĐÚNG

### Câu hỏi

A digital marketing firm is planning to integrate its local servers with AWS for better scalability. The firm has chosen a 200 Mbps AWS Direct Connect connection for this integration. The proposed setup includes a transit gateway and a Direct Connect gateway to ensure smooth communication between several Amazon VPCs and the local servers.

The firm needs to make sure that its local servers can interact with the VPC resources through a transit virtual interface (VIF) using the Direct Connect connection.

Which two actions should the firm take to achieve these requirements? (Select TWO.)

### Các phương án

- **A.** Use the same Connection Key Name (CKN) and Connectivity Association Key (CAK) for all Direct Connect connections.
- **B.** Upgrade the Direct Connect connection from 200 Mbps to 500 Mbps.
- **C.** Configure the Direct Connect connection by setting the MACsec encryption mode parameter to must_encrypt.
- **D.** Advertise the allowed prefixes to a range that is the same or wider than the VPC CIDR block on the Direct Connect gateway. ✅ 👈 *(bạn chọn)*
- **E.** Advertise the VPC prefixes list on the Direct Connect gateway for the transit gateway association. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** D, E  
> **Đáp án đúng:** D, E  
> **Kết quả:** ✅ Đúng

### Giải thích

The prefix list, which includes IPv4 and IPv6 addresses, is a filter that permits the same or a smaller range of CIDRs to be promoted to the Direct Connect gateway. When setting up a Direct Connect gateway, it’s important to set the allowed prefixes to a range that is the same or wider than the VPC CIDR block. This ensures that all IP addresses within the VPC can be reached from the local servers.

If you want to connect your AWS Direct Connect connection to the VPCs or VPNs that are attached to your transit gateway, you can use an AWS Direct Connect gateway. To do this, you need to associate a Direct Connect gateway with the transit gateway and create a transit virtual interface for your AWS Direct Connect connection to the Direct Connect gateway.

Provisioning the allowed prefixes list on the Direct Connect gateway is a necessary step. This list is used to route on-premises traffic to or from a Direct Connect gateway to the transit gateway, even when the VPCs attached to the transit gateway do not have assigned CIDRs. This setup ensures that the local servers can interact with the AWS VPC resources through the transit VIF.

Hence, the correct answers are:

– Advertise the allowed prefixes to a range that is the same or wider than the VPC CIDR block on the Direct Connect gateway.

– Advertise the VPC prefixes list on the Direct Connect gateway for the transit gateway association.

The option that says: Upgrade the Direct Connect connection from 200 Mbps to 500 Mbps is incorrect because while upgrading the connection speed typically improves performance, it is not necessary for the local servers to interact with the AWS VPC resources. The question does not indicate that the current speed is insufficient.

The option that says: Configure the Direct Connect connection by setting the MACsec encryption mode parameter to must_encrypt is incorrect because it is not necessary for the local servers to interact with the Amazon VPC resources through a transit virtual interface (VIF) using the Direct Connect connection. The encryption mode parameter does not affect the interaction between the servers and VPC resources.

The option that says: Use the same Connection Key Name (CKN) and Connectivity Association Key (CAK) for all Direct Connect connections is incorrect because the CKN and CAK are primarily used for MACsec encryption. Using the same keys for all connections would not be a good security practice, and it is not necessary for the local servers to interact with the AWS VPC resources.

 

References:

https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html

https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html

 

Check out this AWS Direct Connect Gateway Cheat Sheet:

https://tutorialsdojo.com/aws-direct-connect/

---

## Câu 7 — ✅ ĐÚNG

### Câu hỏi

A company uses Amazon EC2 instances to host development and production workloads in the us-east-1 region. The instances are spread across multiple AWS accounts under the AWS Organization of the main company account. Every VPC on the us-east-1 region hosts either a development or production workload. All EC2 instances under the organization that have the same environment must be able to communicate with each other, while EC2 instances in different environments must not be able to communicate with each other. To accomplish this requirement, the company created a common network account and used the AWS Transit Gateway service. A transit gateway is created in the us-east-1 region and with the help of AWS Resource Access Manager, it is shared with the entire AWS Organization. Each VPC is then attached to the transit gateway to allow communication between the EC2 instances. However, this also allowed communication between the production and development EC2 instances.

Which of the following implementation would ensure that the development traffic is isolated from the production traffic?

### Các phương án

- **A.** Create a network tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Configure the AWS Transit Gateway route table to allow production tagged attachments to communicate with other production tagged attachments. Set up the same configuration for development tagged attachments.
- **B.** Create an env tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Create policies to restrict traffic between the development and production VPCs based on the tag by using the AWS Transit Gateway Network Manager.
- **C.** Configure the attached security groups of the production Amazon EC2 instances to block traffic from the development EC2 instances. Configure the attached security groups of the development EC2 instances to block traffic from the production EC2 instances.
- **D.** Delete each account’s route propagation and association to the default route table of the AWS Transit Gateway. Create two separate transit gateway route tables for development and production environments. Attach each VPC to their respective route tables and enable route propagation for each attachment. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

A transit gateway enables you to attach VPCs and VPN connections in the same Region and route traffic between them. A transit gateway works across AWS accounts, and you can use AWS RAM to share your transit gateway with other accounts. After you share a transit gateway with another AWS account, the account owner can attach their VPCs to your transit gateway. A user from either account can delete the attachment at any time.

You can enable multicast on a transit gateway, and then create a transit gateway multicast domain that allows multicast traffic to be sent from your multicast source to multicast group members over VPC attachments that you associate with the domain.

Each VPC or VPN attachment is associated with a single route table. That route table decides the next hop for the traffic coming from that resource attachment. A route table inside the transit gateway allows for both IPv4 or IPv6 CIDRs and targets. The targets are VPCs and VPN connections. When you attach a VPC or create a VPN connection on a transit gateway, the attachment is associated with the default route table of the transit gateway.

You can create additional route tables inside the transit gateway, and change the VPC or VPN association to these route tables. This enables you to segment your network. For example, you can associate development VPCs with one route table and production VPCs with a different route table. This enables you to create isolated networks inside a transit gateway similar to virtual routing and forwarding (VRFs) in traditional networks.

Therefore, the correct answer is: Delete each account’s route propagation and association to the default route table of the AWS Transit Gateway. Create two separate transit gateway route tables for development and production environments. Attach each VPC to their respective route tables and enable route propagation for each attachment. This enables you to segment your network. With this method, you can associate development VPCs with one route table and production VPCs with a different route table.

The option that says: Create an env tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Create policies to restrict traffic between the development and production VPCs based on the tag by using the AWS Transit Gateway Network Manager is incorrect. AWS Transit Gateway Network Manager is used to monitor network activity into a single dashboard. It is not used for creating network policies.

The option that says: Configure the attached security groups of the production Amazon EC2 instances to block traffic from the development EC2 instances. Configure the attached security groups of the development EC2 instances to block traffic from the production EC2 instances is incorrect. Security groups can only allow traffic, not block traffic.

The option that says: Create a network tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Configure the AWS Transit Gateway route table to allow production tagged attachments to communicate with other production tagged attachments. Set up the same configuration for development tagged attachments is incorrect. You can tag your VPC attachments to identify them on the AWS Console, however, this tag cannot be used as a basis for network routing. 

 

References:

https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html

https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html

https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html

 

Check out this AWS Transit Gateway Cheat Sheet:

https://tutorialsdojo.com/aws-transit-gateway/

---

## Câu 8 — ❌ SAI

### Câu hỏi

A company uses an AWS Step Functions workflow for its transaction processing system, which relies on several interconnected Lambda functions. The company wants to understand the memory consumption patterns of these Lambda functions to optimize cost.

They require a weekly CSV report detailing the average memory utilization of each function, recommended memory configurations based on historical performance, and potential cost savings between the current and recommended settings.

How can the company achieve this reporting requirement in the least amount of development overhead?

### Các phương án

- **A.** Enroll in the AWS Business Support plan. Collaborate with AWS support to analyze the Lambda function's resource utilization. Manually document insights and optimization suggestions in a CSV file stored in an Amazon S3 bucket.
- **B.** Analyze the Lambda function’s resource utilization using AWS Compute Optimizer. Set up an EventBridge rule to trigger a Lambda function weekly. Use the ExportLambdaFunctionRecommendations API within the function to export recommendations as CSV files in an Amazon S3 bucket. ✅
- **C.** Extract the Billed Duration and Max Memory Use metrics from the Lambda function logs in CloudWatch Logs using a weekly scheduled job. Use this data with Amazon SageMaker Canvas to predict future memory usage patterns and estimate potential savings. Download the forecast as a CSV file.
- **D.** Enable CloudWatch Lambda Insights for the Lambda functions. Configure an EventBridge rule to trigger a Lambda function weekly, which compiles the findings into a CSV file and stores them in an Amazon S3 bucket. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Compute Optimizer helps you identify the optimal AWS resource configurations, such as Amazon Elastic Compute Cloud (EC2) instance types, Amazon Elastic Block Store (EBS) volume configurations, task sizes of Amazon Elastic Container Service (ECS) services on AWS Fargate, and AWS Lambda function memory sizes, using machine learning to analyze historical utilization metrics. AWS Compute Optimizer provides a set of APIs and a console experience to help you reduce costs and increase workload performance by recommending the optimal AWS resources for your AWS workloads.

In the scenario, utilizing the ExportLambdaFunctionRecommendations API within a scheduled function ensures an automated approach to data extraction. Automating the export process through a scheduled function eliminates the need for manual intervention and ensures that the report is generated consistently on a weekly basis, as required

Hence, the correct answer in this scenario is: Analyze the Lambda function’s resource utilization using AWS Compute Optimizer. Set up an EventBridge rule to trigger a Lambda function weekly. Use the ExportLambdaFunctionRecommendations API within the function to export recommendations as CSV files in an Amazon S3 bucket.

The option that says: Enroll in the AWS Business Support plan. Collaborate with AWS support to analyze the Lambda function’s resource utilization. Manually document insights and optimization suggestions in a CSV file stored in an Amazon S3 bucket is incorrect. Engaging AWS support every week would be cumbersome. AWS Business Support is generally meant to provide technical assistance, architectural guidance, and escalated issue resolution rather than weekly performance analysis and manual report generation. Additionally, AWS support doesn’t have access to your function logs, so you would need to share any relevant logs or data, which adds extra steps to the process.

The option that says: Enable CloudWatch Lambda Insights for the Lambda functions. Configure an EventBridge rule to trigger a Lambda function weekly, which compiles the findings into a CSV file and stores them in an Amazon S3 bucket is incorrect. CloudWatch Lambda Insights is primarily designed for monitoring and troubleshooting Lambda functions. It provides deeper visibility into the execution environment of your Lambda functions, allowing you to diagnose and resolve issues more efficiently. However, it’s not capable of generating recommendations for memory configurations or potential cost savings between current and recommended settings.

The option that says: Extract the Billed Duration and Max Memory Use metrics from the Lambda function logs in CloudWatch Logs using a weekly scheduled job. Use this data with Amazon SageMaker Canvas to predict future memory usage patterns and estimate potential savings. Download the forecast as a CSV file is incorrect. This option typically requires parsing and managing logs and integrating with Amazon SageMaker Canvas adds more overhead compared to simply using AWS Compute Optimizer. Furthermore, it doesn’t directly provide memory configuration recommendations.

 

References:

https://aws.amazon.com/compute-optimizer/

https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportLambdaFunctionRecommendations.html

 

Check out this AWS Compute Optimizer Cheat Sheet:

https://tutorialsdojo.com/aws-compute-optimizer/

---

## Câu 9 — ❌ SAI

### Câu hỏi

An organization is redesigning its application to a multi-region architecture to enhance disaster recovery and high availability. The application’s infrastructure, which includes an Amazon RDS for MySQL database, is managed across primary and secondary regions using AWS CloudFormation. The architecture must meet a Recovery Time Objective (RTO) of 30 minutes and a Recovery Point Objective (RPO) of 1 hour. The application’s traffic is managed using Amazon Route 53.

What combination of actions should a Solutions Architect take to meet the requirements? (Select TWO.)

### Các phương án

- **A.** Create a cross-region read replica of the Amazon RDS for the MySQL database in the secondary region. Promote the cross-region RDS for MySQL database read replica automatically via an AWS Lambda Function. ✅
- **B.** Create an AWS Lambda function to backup the database to S3 in the secondary region every hour. Create Amazon Route 53 to perform health checks and redirect traffic to the standby database if the primary database fails. 👈 *(bạn chọn)*
- **C.** Create a Route 53 failover policy for the database DNS record with the primary database endpoint as the main and the read replica endpoint as backup. ✅
- **D.** Provision an additional RDS instance in the primary region for redundancy, configuring bi-directional replication between it and the primary database.
- **E.** Create an AWS Lambda function to perform database health checks. If a failure is detected, restore the latest snapshot from the secondary region and update Route 53 DNS records accordingly. 👈 *(bạn chọn)*

> **Bạn chọn:** B, E  
> **Đáp án đúng:** A, C  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Lambda is a service that enables you to write and execute code without worrying about managing servers. You can write Lambda functions in Node.js, Python, Java, and other languages.

Amazon RDS is an AWS database service for setting up, operating, and scaling relational databases like MySQL, MariaDB, Oracle, SQL Server, and PostgreSQL in the cloud.

A cross-region read replica is a read-only copy of the source database that is replicated to a different AWS region. This allows serving reads from the secondary region for lower latency and acts as a disaster recovery solution if the primary region goes down. The replication is asynchronous and cross-region read replicas can be created for MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server databases on Amazon RDS.

Amazon Route 53 is a highly scalable and available DNS service provided by AWS. Route 53 can be used for domain registration, where you can register domain names and select domain registrars. It also provides DNS routing capabilities, where you can route traffic to different resources like web servers, load balancers, etc., based on various factors.

Some common routing policies in Route 53 include simple routing to direct traffic to a single resource, failover routing to configure active-passive failover for high availability, latency routing to route traffic to regions providing the lowest latency, and weighted routing to distribute traffic among multiple resources in specified proportions.

To create a highly available architecture that meets specified RTO and RPO requirements, the Solutions Architect should create a cross-region read replica of the Amazon RDS for MySQL database in the secondary region. This would allow serving reads from that region to improve latency for users there. Promoting the read replica automatically via an AWS Lambda function would enable failing over to the secondary region in case of a primary region outage, meeting the 30-minute RTO. Additionally, configuring a Route 53 failover policy with the primary database endpoint as the main and read replica endpoint as backup would route traffic to the available region based on health checks, improving availability.

Hence, the correct answers are:

– Create a cross-region read replica of the Amazon RDS for the MySQL database in the secondary region. Promote the cross-region RDS for MySQL database read replica automatically via an AWS Lambda Function.

– Create a Route 53 failover policy for the database DNS record with the primary database endpoint as the main and the read replica endpoint as backup.

The option that says: Create an AWS Lambda function to backup the database to S3 in the secondary region every hour. Create Amazon Route 53 to perform health checks and redirect traffic to the standby database if the primary database fails is incorrect because backing up the database to S3 does not provide a live database instance that can serve traffic immediately after a failover. The time to restore a database from an S3 backup would likely exceed the specified RTO.

The option that says: Create an AWS Lambda function to perform database health checks. If a failure is detected, restore the latest snapshot from the secondary region and update Route 53 DNS records accordingly is incorrect as the time to restore from a snapshot typically exceeds 30 minutes, thus failing to meet the RTO requirement.

The option that says: Provision an additional RDS instance in the primary region for redundancy, configuring bi-directional replication between it and the primary database is incorrect. While it suggests redundancy, the use of bi-directional replication is not a standard practice with Amazon RDS and can lead to data conflicts.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

https://tutorialsdojo.com/aws-lambda/

https://tutorialsdojo.com/amazon-route-53/

---

## Câu 10 — ❌ SAI

### Câu hỏi

A company hosts an SFTP server in an Amazon EC2 instance with an Elastic IP address inside a VPC. The SFTP server acts as a central repository for uploading inventory data of its partners. The partner companies connect to the server via the Elastic IP address and use SSH for authentication. The security group of the EC2 instance is restricted to allow only the IP addresses of the partner companies. The solutions architect has been tasked to improve the current solution, increase the availability of the server, and minimize the management complexity of the infrastructure. The company wants minimal disruption for its partners and it should retain the current process on how the partners connect to the SFTP server.

Which of the following implementations will meet the company requirements?

### Các phương án

- **A.** Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family SFTP-enabled server with a publicly accessible endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket. 👈 *(bạn chọn)*
- **B.** Create an Auto Scaling group of Amazon EC2 instances that run the SFTP server and place it behind a Network Load Balancer. Create a multi-attach Amazon EBS volume to be mounted on all the EC2 instances in the cluster. Sync all the SFTP server files to the multi-attach volume. Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Auto Scaling group to allow only the IP addresses of the partner companies.
- **C.** Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family server inside the VPC with an internet-facing endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Create a security group for the endpoint to allow only the IP addresses of the partner companies. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket. ✅
- **D.** Create an AWS Fargate task definition to run the SFTP server. Create a new Amazon Elastic File System (EFS) volume and add it as a mount point in the task definition. Sync all the SFTP server files to the EFS volume. Create a Fargate service using the task definition and place it behind a Network Load Balancer (NLB). Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Fargate service to allow only the IP addresses of the partner companies.

> **Bạn chọn:** A  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services. AWS Transfer Family supports transferring data from or to the following AWS storage services – Amazon Simple Storage Service (Amazon S3) storage and Amazon Elastic File System (Amazon EFS) Network File System (NFS) file system.

AWS Transfer Family supports transferring data over the following protocols:

-Secure Shell (SSH) File Transfer Protocol (SFTP) (AWS Transfer for SFTP)

-File Transfer Protocol Secure (FTPS) (AWS Transfer for FTPS)

-File Transfer Protocol (FTP) (AWS Transfer for FTP)

You can host your server’s endpoint inside a virtual private cloud (VPC) to use for transferring data to and from an Amazon S3 bucket or Amazon EFS file system without going over the public internet. If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and a server. You can then use this server to transfer data over your client to and from your Amazon S3 bucket without going over the public internet.

Using Amazon VPC, you can launch AWS resources in a custom virtual network. You can use a VPC to control your network settings, such as the IP address range, subnets, route tables, and network gateways. In addition, if you choose to make your server’s endpoint internet-facing, you can associate Elastic IP addresses with your endpoint. Doing this lets clients outside of your VPC connect to your server. You can use VPC security groups to control access to authenticated users whose requests originate only from allowed addresses.

Therefore, the correct answer is: Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family server inside the VPC with an internet-facing endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Create a security group for the endpoint to allow only the IP addresses of the partner companies. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket. Creating an internet-facing endpoint inside a VPC allows you to associate an Elastic IP address and security groups to the AWS Transfer Family server. This is highly available, scalable, and has less operational overhead.

The option that says: Create an Auto Scaling group of Amazon EC2 instances that run the SFTP server and place it behind a Network Load Balancer. Create a multi-attach Amazon EBS volume to be mounted on all the EC2 instances in the cluster. Sync all the SFTP server files to the multi-attach volume. Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Auto Scaling group to allow only the IP addresses of the partner companies is incorrect. This may be possible as the Auto Scaling group increases the availability but it adds complexity to the overall infrastructure. You will have to manage the multi-attach EBS manually should you need to increase volume size in the future. 

The option that says: Create an AWS Fargate task definition to run the SFTP server. Create a new Amazon Elastic File System (EFS) volume and add it as a mount point in the task definition. Sync all the SFTP server files to the EFS volume. Create a Fargate service using the task definition and place it behind a Network Load Balancer (NLB). Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Fargate service to allow only the IP addresses of the partner companies is incorrect. Although this may be possible, this increases operation complexity since you will have to create a Fargate cluster, EFS volume, and the NLB configuration. 

The option that says: Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family SFTP-enabled server with a publicly accessible endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket is incorrect. It is not safe to have a public-facing AWS Transfer family endpoint without any restrictions. 

 

References:

https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html

https://aws.amazon.com/premiumsupport/knowledge-center/sftp-enable-elastic-ip-addresses/

https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html

 

Check out this AWS Transfer Family Cheat Sheet:

https://tutorialsdojo.com/aws-transfer-family/

---

## Câu 11 — ✅ ĐÚNG

### Câu hỏi

A large company has thousands of Amazon EC2 instances with Amazon Elastic Block Storage (EBS) in its AWS account. The instances are spread across different regions and multiple VPCs. Hundreds of these are very large, high-memory instances that host database clusters in active/passive configurations. The company wants to analyze how efficiently the business is using these resources and take appropriate actions based on the results. Currently, the company has no baseline pattern on how the applications utilize the databases.

Which of the following options is the recommended action to meet the company requirements in a cost-effective manner?

### Các phương án

- **A.** Enable Amazon CloudWatch detailed monitoring for all Amazon EC2 instances to enable monitoring of its memory and EBS volumes. Create a new dashboard on Amazon CloudWatch to view metrics based on CPU, Memory, and Disk usage. Resize the EC2 instances based on the identified usage patterns and peak loads on the metrics.
- **B.** Create visualizations associated with Amazon CloudWatch metrics of the CPU, Memory, and EBS utilization of the Amazon EC2 instances. Set up a new monitoring dashboard using AWS Systems Manager OpsCenter. Review this dashboard to identify usage patterns and peak loads, then rightsize the EC2 instances accordingly.
- **C.** Ensure that the Amazon CloudWatch agent is installed on all Amazon EC2 instances. In the company AWS account, opt-in for the AWS Compute Optimizer and wait for at least 12 hours. Rightsize the EC2 instances based on the recommendations from the Compute Optimizer service. ✅ 👈 *(bạn chọn)*
- **D.** Enable the extended features of AWS Trusted Advisor and the AWS Systems Manager Incident Manager by signing up the company AWS account with the AWS Enterprise Support plan. Wait for at least 12 hours for Trusted Advisor to populate recommendations. Resize the EC2 instances based on its recommendations to save on cost.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Compute Optimizer helps you choose the optimal AWS Compute resources for your workloads. Compute Optimizer delivers intuitive and actionable recommendations to help you identify the optimal AWS Compute resources. When you access the AWS Compute Optimizer console for the first time, you are asked to opt-in, using the account that you’re signed in with, before you can use the service.

After you opt-in, Compute Optimizer starts to scan your AWS infrastructure and generates recommendations. It may take up to 12 hours for Compute Optimizer to deliver recommendations for all supported AWS Compute resources.

You can use the dashboard in the Compute Optimizer console to evaluate and prioritize the optimization opportunities for the supported resource types in your account. The findings section displays the findings classifications count and percentage for resource types in your account. Compute Optimizer classifies EC2 instances, Auto Scaling groups, and Lambda functions as under-provisioned, over-provisioned, or optimized. Amazon EBS volumes are classified as not optimized or optimized. You can improve your recommendation by installing the Amazon CloudWatch agent to enable memory metrics for your EC2 instances.

Therefore, the correct answer is: Ensure that the Amazon CloudWatch agent is installed on all Amazon EC2 instances. In the company AWS account, opt-in for the AWS Compute Optimizer and wait for at least 12 hours. Rightsize the EC2 instances based on the recommendations from the Compute Optimizer service. AWS Compute Optimizer can show recommendations for sizing your EC2 instances, Auto Scaling groups, Lambda functions, and EBS volumes.

The option that says: Create visualizations associated with Amazon CloudWatch metrics of the CPU, Memory, and EBS utilization of the Amazon EC2 instances. Set up a new monitoring dashboard using AWS Systems Manager OpsCenter. Review this dashboard to identify usage patterns and peak loads, then rightsize the EC2 instances accordingly is incorrect. The AWS Systems Manager OpsCenter service simply enables you to view, investigate, and resolve operational work items (OpsItems) related to AWS resources. It is not intended to be used for analyzing EC2 usage efficient patterns and it does not provide recommendations for EC2 sizing.

The option that says: Enable Amazon CloudWatch detailed monitoring for all Amazon EC2 instances to enable monitoring of its memory and EBS volumes. Create a new dashboard on Amazon CloudWatch to view metrics based on CPU, Memory, and Disk usage. Resize the EC2 instances based on the identified usage patterns and peak loads on the metrics is incorrect. This may be possible however you will have to manually review the dashboards and graphs for each instance. You don’t have automated recommendations with this approach.

The option that says: Enable the extended features of AWS Trusted Advisor and the AWS Systems Manager Incident Manager by signing up the company AWS account with the AWS Enterprise Support plan. Wait for at least 12 hours for Trusted Advisor to populate recommendations. Resize the EC2 instances based on its recommendations to save on cost is incorrect. Recommendations for rightsizing your EC2 instances is actually a feature of AWS Compute Optimizer, not AWS Trusted Advisor. In addition, the AWS Systems Manager Incident Manager service is totally separate from AWS Trusted Advisor so upgrading to the AWS Enterprise Support plan is not a prerequisite in order to use it.

 

References:

https://aws.amazon.com/compute-optimizer/getting-started/

https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html

https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/

 

Check out this Amazon EC2 Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

---

## Câu 12 — ❌ SAI

### Câu hỏi

A company hosts a web application service in the AWS eu-east-1 region. The application serves weather maps to users. The maps are updated every 1 hour and are stored in an Amazon S3 bucket along with static web content. The web application is behind an Amazon CloudFront distribution. The company has expanded and now provides the same service to North American users. Reports indicate that the viewing experience for weather maps is slow at times in this region.

Which combination of actions can provide the LEAST latency between the users and the application? (Select TWO.)

### Các phương án

- **A.** Configure S3 cross-region replication from the eu-east-1 bucket to a new bucket in the us-east-1 region. ✅
- **B.** Create a new AWS Global Accelerator endpoint for the us-east-1 bucket and add it as an origin for the CloudFront distribution. Use Lambda@Edge to modify North American requests to use this new origin. 👈 *(bạn chọn)*
- **C.** Create a Lambda@Edge function that modifies requests from North American users to use the S3 Transfer Acceleration endpoint of the S3 bucket in the us-east-1 region. 👈 *(bạn chọn)*
- **D.** Create a Lambda@Edge that modifies requests from North American users to retrieve files from a new us-east-1 S3 bucket. ✅
- **E.** Create a new AWS Global Accelerator endpoint for the eu-west-1 S3 bucket. Configure additional endpoint groups in the us-east-1 S3 bucket for TCP port 443.

> **Bạn chọn:** B, C  
> **Đáp án đúng:** A, D  
> **Kết quả:** ❌ Sai

### Giải thích

Lambda@Edge is a feature of Amazon CloudFront that lets you run code closer to your application’s users, improving performance and reducing latency. With Lambda@Edge, you don’t have to provision or manage infrastructure in multiple locations around the world. You pay only for the compute time you consume—there is no charge when your code is not running.

One of the use cases for Lambda@Edge is for intelligent request routing. This capability allows developers to customize how requests are handled at AWS network edge locations, making it possible to dynamically alter the flow of traffic based on various criteria, such as the geographic location of the requester, device type, or request headers. By processing these requests closer to the user, Lambda@Edge enables the implementation of optimizations like content localization, A/B testing, and adaptive responses based on user-agent.

Amazon S3 Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. Buckets that are configured for object replication can be owned by the same AWS account or by different accounts. Objects may be replicated to a single destination bucket or multiple destination buckets. Destination buckets can be in different AWS Regions or within the same Region as the source bucket.

S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different AWS Regions. CRR can help you do the following:

– Meet compliance requirements — Although Amazon S3 stores your data across multiple geographically distant Availability Zones by default, compliance requirements might dictate that you store data at even greater distances.

– Minimize latency — If your customers are in two geographic locations, you can minimize latency in accessing objects by maintaining object copies in AWS Regions that are geographically closer to your users.

– Increase operational efficiency — If you have compute clusters in two different AWS Regions that analyze the same set of objects, you might choose to maintain object copies in those Regions.

In the scenario, by setting up Cross-Region Replication (CRR), you replicate the weather map data to a bucket in us-east-1, bringing it geographically closer to North American users. Then, you can configure a Lambda@Edge function to reroute requests from North American users to the us-east-1 bucket. Together, this solution significantly reduces latency, as the data being accessed is much closer to the users, ensuring an improved user experience.

Hence, the correct answers are:

– Create a Lambda@Edge that modifies requests from North American users to retrieve files from a new us-east-1 S3 bucket. By having the data replicated in a geographically closer region (us-east-1), the data retrieval time is significantly decreased for users in that region.

– Configure S3 cross-region replication from the eu-east-1 bucket to a new bucket in the us-east-1 region. This approach dynamically routes requests based on the user’s geographic location. By using the S3 Transfer Acceleration endpoint, which is designed to speed up the transfer of files over long distances between the client and the S3 bucket, North American users can experience faster access to the weather maps.

The option that says: Create a new AWS Global Accelerator endpoint for the us-east-1 bucket and add it as an origin for the CloudFront distribution. Use Lambda@Edge to modify North American requests to use this new origin is incorrect. While AWS Global Accelerator can improve performance for some use cases, it typically front-ends applications or load balancers. Simply creating a Global Accelerator endpoint for a new S3 bucket does not address the crucial need to replicate or store the updated objects in a bucket closer to the users.

The option that says: Create a new Global Accelerator endpoint for the eu-west-1 S3 bucket. Configure additional endpoint groups in the us-east-1 S3 bucket for TCP port 443 is incorrect because it references a different region (eu-west-1) instead of the specified eu-east-1 origin, and configuring additional endpoint groups for a bucket alone does not resolve the fundamental latency issue.

The option that says: Create a Lambda@Edge function that modifies requests from North American users to use the S3 Transfer Acceleration endpoint of the S3 bucket in the us-east-1 region is incorrect. While S3 Transfer Acceleration (S3TA) can typically optimize the transfer of data to and from S3 buckets, especially over long distances, it does not change the geographic location of the data. With this approach, you are still essentially retrieving files from a distant bucket. Consequently, the latency experienced will likely be higher compared to retrieving data from a source that is geographically closer to you.

 

References:

https://aws.amazon.com/blogs/networking-and-content-delivery/dynamically-route-viewer-requests-to-any-origin-using-lambdaedge/

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html

 

Check out these Amazon S3 and Amazon CloudFront Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-cloudfront/

---

## Câu 13 — ❌ SAI

### Câu hỏi

A company is planning to host a two-tier application on AWS. They’ve chosen to use the LAMP (Linux, Apache, MySQL, PHP) stack, wherein a stateful application will run on Amazon EC2 instances, and the database will be managed using Amazon Aurora.

The customer base is expected to grow rapidly, which would likely result in unprecedented traffic spikes. The design must ensure that both the application and the database tiers can scale automatically in response to changes in demand.

Which combination of solutions will meet the requirements? (Select TWO.)

### Các phương án

- **A.** Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy that will automatically scale the Aurora writer instances 👈 *(bạn chọn)*
- **B.** Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy and apply it to the Amazon Aurora DB cluster to automatically scale Aurora read replicas. ✅
- **C.** Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable Client Port preservation and select round-robin as the load balancing algorithm.
- **D.** Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to a Network Load Balancer (NLB). Enable sticky sessions and select Least Outstanding Requests (LOR) as the load balancing algorithm. 👈 *(bạn chọn)*
- **E.** Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable sticky sessions and select round-robin as the load balancing algorithm for the target groups. ✅

> **Bạn chọn:** A, D  
> **Đáp án đúng:** B, E  
> **Kết quả:** ❌ Sai

### Giải thích

Aurora Auto Scaling enables your Aurora DB cluster to handle sudden increases in connectivity or workload by dynamically adjusting the number of its Aurora Replicas. This feature is available for both Aurora MySQL and Aurora PostgreSQL. You define and apply a scaling policy to an Aurora DB cluster. The scaling policy defines the minimum and maximum number of Aurora Replicas that Aurora Auto Scaling can manage. Based on the policy, Aurora Auto Scaling adjusts the number of Aurora Replicas up or down in response to actual workloads, determined by using Amazon CloudWatch metrics and target values.

An Auto Scaling group contains a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

Target groups route requests to one or more registered targets, such as EC2 instances, using the protocol and port number that you specify. You can register a target with multiple target groups. You can configure health checks on a per-target group basis. Health checks are performed on all targets registered to a target group that is specified in a listener rule for your load balancer.

By default, the round-robin routing algorithm is used to route requests at the target group level. You can specify the least outstanding requests routing algorithm instead.

Consider using least outstanding requests (LOR) when the requests for your application vary in complexity or your targets vary in processing capability. Round robin is a good choice when the requests and targets are similar or if you need to distribute requests equally among targets. You can compare the effect of round robin versus the least outstanding requests using the following CloudWatch metrics: RequestCount, TargetConnectionErrorCount, and TargetResponseTime.

In the scenario, using Auto Scaling groups would help ensure that you have the correct number of Amazon EC2 instances available to handle the load for the application. By attaching the ASG to an ALB, you can distribute incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. Sticky sessions enable the load balancer to bind a user’s session to a specific instance, ensuring that all requests from the user during the session are sent to the same instance. This is crucial for the correct operation of stateful applications, especially if you’re not using any external session store.

Hence the correct answers are:

– Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy and apply it to the Amazon Aurora DB cluster to automatically scale Aurora read replicas.

– Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable sticky sessions and select round-robin as the load-balancing algorithm for the target groups.

The option that says: Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy that will automatically scale the Aurora writer instances is incorrect because having multiple Amazon Aurora writer instances is not fully supported in Amazon Aurora or Amazon RDS. You can only enable Aurora Auto Scaling at the DB cluster level, not on the writer instances.

The option that says: Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to a Network Load Balancer (NLB). Enable sticky sessions and select Least Outstanding Requests (LOR) as the load balancing algorithm is incorrect. A Network Load Balancer (NLB) operates at the transport layer (Layer 4) of the OSI model and is primarily designed to handle TCP traffic. It lacks built-in support for HTTP and HTTPS protocols, which is a crucial requirement for a LAMP-based application.

The option that says: Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable Client Port preservation and select round-robin as the load balancing algorithm is incorrect. Client Port Preservation simply preserves the source client port, allowing backend applications to see the original client-side source port. It’s not for binding user sessions to a specific EC2 instance.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html

 

Check out these Cheat sheets for Amazon Aurora and AWS Auto Scaling:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/aws-auto-scaling/

---

## Câu 14 — ❌ SAI

### Câu hỏi

A global streaming company uses a Java application on an Amazon EC2 instance to transcode videos for its platform. The application starts processing the videos to different resolutions every time they are uploaded to an Amazon S3 bucket. It takes approximately 40 minutes to transcode each video. The application keeps track of the transcoded videos and will only process each file once.

Upon reviewing Amazon CloudWatch metrics, a solutions architect noted that the EC2 instance is idle for 35% of the time on average. The solutions architect is required to make the workload highly available and scalable, and reduce management overhead.

What should the architect recommend for the MOST cost-effective solution?

### Các phương án

- **A.** Build a container image out of the video transcoding application. Deploy and run the container image on an EC2 instance. Configure the container to continuously poll the S3 bucket for new videos and to transcode the files.
- **B.** Create an equivalent script of the application workflow and deploy it as an AWS Lambda function. Use an S3 event notification to start the processing when a new video is uploaded.
- **C.** Build a container image out of the video transcoding application. Deploy and run the container image on Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. Create an AWS Lambda function that calls the Fargate RunTask API operation when the S3 bucket receives the file upload event notification. ✅
- **D.** Create an Amazon Simple Queue Service (Amazon SQS) queue and configure Amazon S3 to send event notifications to the SQS queue. Set up an EC2 Auto Scaling group with a minimum size of one instance. Modify the video transcoding application to continuously poll the SQS queue, and start transcoding the files in S3 that the SQS message links to. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Fargate is a service that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. With AWS Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing. Amazon ECS, using Fargate, allows you to run containers without managing the underlying infrastructure. It automatically scales based on demand.

One use case for ECS task definitions is on video transcoding workloads. To use video transcoding workloads on Amazon ECS, register Amazon EC2 VT1 instances. This will allow running live and pre-rendered video transcoding workloads as tasks on Amazon ECS.

Because of its scaling capability, AWS Fargate can be used to run event-driven workloads at scale. For use cases when a workload cannot be run by AWS Lambda alone because of limitations on runtime, such as Lambda’s current 15-minute memory limit, a Lambda function can be triggered and invoke an ECS task.

Using S3 event notifications to trigger the Lambda function ensures that the transcoding process starts as soon as a new video is uploaded, improving efficiency.

Therefore, the correct answer is: Build a container image out of the video transcoding application. Deploy and run the container image on Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. Create an AWS Lambda function that calls the Fargate RunTask API operation when the S3 bucket receives the file upload event notification.

The option that says: Create an Amazon Simple Queue Service (Amazon SQS) queue and configure Amazon S3 to send event notifications to the SQS queue. Set up an EC2 Auto Scaling group with a minimum size of one instance. Modify the video transcoding application to continuously poll the SQS queue, and start transcoding the files in S3 that the SQS message links to is incorrect. Although this approach decouples the components, is scalable, and ensures each file is processed only once, it is not cost-effective for the EC2 instances to continuously poll the SQS queue.

The option that says: Create an equivalent script of the application workflow and deploy it as an AWS Lambda function. Use an S3 event notification to start the processing when a new video is uploaded is incorrect. AWS Lambda currently has a function execution time limit of 900 seconds or 15 minutes before it is automatically terminated. The scenario talks about a long-running workload, and using AWS Lambda cannot fulfill this requirement.

The option that says: Build a container image out of the video transcoding application. Deploy and run the container image on an EC2 instance. Configure the container to continuously poll the S3 bucket for new videos and to transcode the files is incorrect. This solution allows for full control of the container application in the EC2 image, but it is not cost-effective as it requires the EC2 instance to be constantly running. There is also an additional management overhead of scaling the EC2 instances, which is not the best practice.

References:

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-vt1.html

https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-event-driven-and-scheduled-workloads-at-scale-with-aws-fargate.html

 

Check out this article on Amazon Elastic Container Service:

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

---

## Câu 15 — ❌ SAI

### Câu hỏi

An e-commerce platform experiences significant traffic spikes during peak shopping seasons, leading to performance bottlenecks and impacting user experience. The application is hosted on Amazon ECS and uses Amazon CloudFront as its CDN. The platform has two main modules: product browsing and checkout, with the browsing module experiencing substantially higher loads. Sessions are managed using JSON Web Tokens (JWT), which encodes user roles and access levels. This load imbalance causes performance issues, affecting overall availability.
A Solutions Architect needs to enhance scalability and reliability for both modules during high-traffic periods to maintain optimal performance and cost efficiency.

Which solution will most effectively address this challenge?

### Các phương án

- **A.** Implement API Gateway in front of ECS services, using AWS Lambda authorizer to authenticate users based on JWT. Utilize API Gateway's caching and traffic management capabilities, directing requests based on JWT attributes to the correct module. 👈 *(bạn chọn)*
- **B.** Refactor the application to use AWS Lambda for both modules, with API Gateway routing requests based on JWT. Use CloudFront for static content delivery and JWT validation.
- **C.** Create separate ECS services for browsing and checkout modules, each with its own auto-scaling configuration. Use CloudFront Functions to inspect JWT, route requests to the appropriate ECS service based on the requested module, user access level, and load. ✅
- **D.** Transition the platform to Amazon Elastic Kubernetes Service, separating the product browsing and checkout functionalities into distinct Kubernetes pods. Implement ECS Service Connect to orchestrate service communication within the cluster, enabling mutual TLS (mTLS) to secure pod-to-pod interactions. Configure the Service Connect virtual service to utilize JWT for authenticating requests, directing them from the browsing pod to the checkout pod based on user permissions and session data encoded in the JWT.

> **Bạn chọn:** A  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon ECS is a fully managed, opinionated container orchestration service that delivers the easiest way for organizations to build, deploy, and manage containerized applications at any scale on AWS. By creating separate ECS services for the browsing and checkout modules, you can independently scale each service based on its specific load requirements, ensuring optimal resource utilization and cost-efficiency.

Automatic scaling is the ability to automatically increase or decrease the desired count of tasks in your Amazon ECS service. Amazon ECS leverages the Application Auto Scaling service to provide this functionality.

Amazon CloudFront Functions allow lightweight JavaScript code to run directly at CloudFront edge locations. This enables fast, low-latency customization of requests and responses—such as inspecting JWTs, modifying headers, or routing—without invoking additional services.

Lambda@Edge, by contrast, runs more powerful AWS Lambda functions associated with CloudFront events. While Lambda@Edge supports more complex logic and integrations, it generally has higher latency and cost than CloudFront Functions.

JSON Web Tokens (JWT) is a popular open standard for securely sharing information as a JSON object between different parties.

By creating separate ECS services for the browsing and checkout modules, you can effectively isolate the two components, allowing them to scale independently based on their respective load requirements. This separation of concerns ensures that the high-traffic browsing module does not adversely impact the performance of the checkout module and vice versa.

Each ECS service can have its own auto-scaling configuration tailored to its specific load patterns and resource requirements. This ensures that resources are allocated efficiently, preventing over-provisioning or under-provisioning of resources for either module. During peak traffic periods, the browsing module can scale up seamlessly without affecting the checkout module’s performance.

By leveraging CloudFront Functions, you can inspect the JWT to extract user roles, access levels, and the requested module. Based on this information, CloudFront Functions can intelligently route requests to the appropriate ECS service, ensuring that users are directed to the correct module based on their permissions and the requested functionality.

This solution leverages the existing infrastructure, including Amazon ECS and Amazon CloudFront, minimizing the need for significant architectural changes or migrations. This approach reduces complexity and potential risks associated with transitioning to new services or platforms.

Hence, the correct answer is: Create separate ECS services for browsing and checkout modules, each with its own auto-scaling configuration. Use CloudFront Functions to inspect JWT, route requests to the appropriate ECS service based on the requested module, user access level, and load.

The option that says: Transition the platform to Amazon Elastic Kubernetes Service, separating the product browsing and checkout functionalities into distinct Kubernetes pods. Implement ECS Service Connect to orchestrate service communication within the cluster, enabling mutual TLS (mTLS) to secure pod-to-pod interactions. Configure the Service Connect virtual service to utilize JWT for authenticating requests, directing them from the browsing pod to the checkout pod based on user permissions and session data encoded in the JWT is incorrect because Amazon ECS Service Connect is primarily designed to work with Amazon ECS clusters, not Kubernetes clusters. EKS uses Kubernetes-native tools for service communication and discovery, not ECS-specific services. Therefore, ECS Service Connect cannot be used in an EKS environment.

The option that says: Implement API Gateway in front of ECS services, using AWS Lambda authorizer to authenticate users based on JWT. Utilize API Gateway’s caching and traffic management capabilities, directing requests based on JWT attributes to the correct module is incorrect. While API Gateway and Lambda authorizers can handle JWT authentication and request routing, this approach may simply introduce additional latency and complexity compared to using CloudFront Functions. Additionally, API Gateway’s caching and traffic management capabilities may not be as efficient as CloudFront’s edge caching and routing capabilities for this specific use case. Lastly, introducing API Gateway as an additional layer between the client and ECS services may increase operational overhead and potential points of failure.

The option that says: Refactor the application to use AWS Lambda for both modules, with API Gateway routing requests based on JWT. Use CloudFront for static content delivery and JWT validation is incorrect. This option requires a significant refactoring of the application to use AWS Lambda, which may not be feasible or cost-effective for an existing e-commerce platform. Transitioning to a serverless architecture with Lambda may only introduce challenges in managing state and handling long-running processes, which are common in e-commerce applications.

 

References:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html

https://aws.amazon.com/ecs/faqs/

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-cloudfront/

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

---

## Câu 16 — ❌ SAI

### Câu hỏi

A multinational company has hundreds of AWS accounts that are managed under one AWS Organization. The company has 25 technical teams that are designated with their own Organization Unit (OU) in the AWS Organizations. Each team manages several AWS accounts to be used for their projects. The upper management wants a solution that enables each Team Leader to examine the breakdown of AWS resource charges across all the AWS accounts under their OU.

Which of the following options should the solutions architect implement to meet this requirement?

### Các phương án

- **A.** Using AWS Resource Access Manager, generate an AWS Cost and Usage Report (CUR) for each OU. Upload the report in Amazon QuickSight and create the dashboard. Share the dashboard with each OU Team Lead. 👈 *(bạn chọn)*
- **B.** Using AWS Systems Manager in the management account, generate an AWS Cost and Usage Report (CUR) for each OU. Create a dashboard on AWS Systems Manager OpsCenter to visualize the report. Share the dashboard with each OU Team Lead.
- **C.** For each member account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in AWS Systems Manager Explorer and create a dashboard. Allow each Team Leader to view the dashboards.
- **D.** From the management account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in Amazon QuickSight and create a dashboard. Allow each Team Leader to view the dashboard. ✅

> **Bạn chọn:** A  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

The AWS Cost & Usage Report contains the most comprehensive set of AWS cost and usage data available, including additional metadata about AWS services, pricing, credit, fees, taxes, discounts, cost categories, Reserved Instances, and Savings Plans. The AWS Cost & Usage Report (CUR) itemizes usage at the account or Organization level by product code, usage type, and operation. With the right access, users can access CUR at management and member account levels, which saves management account holders from having to generate CUR reports for member accounts.

AWS delivers the AWS Cost & Usage Report to whichever Amazon Simple Storage Service (S3) bucket you specify during setup and updates the reports at least once per day. You can configure your Cost & Usage Reports to integrate with Amazon Athena. When you integrate with Redshift, all the necessary commands are provided to you in the RedshiftCommands.sql file that is stored alongside your manifest file in S3 and in the Redshift fileHelper file in the Billing and Cost Management console. Your AWS Cost & Usage Report can also be integrated directly with Amazon QuickSight.

Therefore, the correct answer is: From the management account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in Amazon QuickSight and create a dashboard. Allow each Team Leader to view the dashboard. The management account can create a dashboard based on the CUR to allow the team leaders to visualize the AWS charges under their OU.

The option that says: Using AWS Resource Access Manager, generate an AWS Cost and Usage Report (CUR) for each OU. Upload the report in Amazon QuickSight and create the dashboard. Share the dashboard with each OU Team Lead is incorrect. AWS Resources Access Manager (RAM) is used to share AWS resources such as transit gateways, subnets, AWS License Manager license configurations, and Amazon Route 53 Resolver rules. It can’t be used to generate an AWS Cost and Usage Report.

The option that says: For each member account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in AWS Systems Manager Explorer and create a dashboard. Allow each Team Leader to view the dashboards is incorrect. Using a member account may be possible but is not optimal because there will be a CUR dashboard for each account, and the team leader will have to view them individually. You have to create a CUR for each management account instead to avoid this unnecessary operational overhead. Moreover, the AWS Systems Manager Explorer is a customizable operations dashboard that reports information about your actual AWS resources (e.g., Amazon EC2, Amazon RDS, etc.). This service does not gather cost and management information of the member accounts within your AWS Organization.

The option that says: Using AWS Systems Manager in the management account, generate an AWS Cost and Usage Report (CUR) for each OU. Create a dashboard on AWS Systems Manager OpsCenter to visualize the report. Share the dashboard with each OU Team Lead is incorrect. You can’t generate an AWS Cost and Usage Report in AWS Systems Manager. Additionally, the Systems Manager OpsCenter does not support importing CUR. A better solution for this is to use an Amazon QuickSight dashboard instead.

 

References:

https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html

https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/

https://aws.amazon.com/about-aws/whats-new/2020/12/cost-and-usage-report-now-available-to-member-linked-accounts/

 

Check out these AWS Organizations and AWS Billing and Cost Management Cheat Sheets:

https://tutorialsdojo.com/aws-organizations/

https://tutorialsdojo.com/aws-billing-and-cost-management/

---

## Câu 17 — ✅ ĐÚNG

### Câu hỏi

A company has several Amazon FSx for Windows File Server deployments in multiple AWS accounts. The solutions architect is conducting a performance review on all Amazon for FSx file deployments to comply with the company policy that requires all file systems to be configured to be highly available in at least two Availability Zones. The solutions architect found some Amazon FSx file systems that use a deployment type of Single-AZ. These must be corrected while minimizing downtime that could affect other application components.

Which of the following option is the recommended action to meet the company requirements?

### Các phương án

- **A.** Use AWS DataSync to copy data to a new Amazon FSx file system that uses a Multi-AZ deployment type. After copying, point the applications to use the new Amazon FSx share. ✅ 👈 *(bạn chọn)*
- **B.** Take a backup of the current Amazon FSx file system. Restore this backup to a new Amazon FSx file system with a deployment type of Multi-AZ. After restoration, point the applications to use the new Amazon FSx share.
- **C.** Use AWS DataSync to continuously sync data to a second Amazon FSx file system that uses a Single-AZ deployment type. In the event of failure, point the applications to use the second Amazon FSx share.
- **D.** On the AWS management console, update the Amazon FSx file system to use a Multi-AZ deployment type.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon FSx for Windows File Server offers two file system deployment types: Single-AZ and Multi-AZ.

With Single-AZ file systems, Amazon FSx automatically replicates your data within an Availability Zone (AZ) to protect it from component failure. It continuously monitors for hardware failures and automatically replaces infrastructure components in the event of a failure. Amazon FSx also uses the Windows Volume Shadow Copy Service to make highly durable backups of your file system daily and store them in Amazon S3.

Multi-AZ file systems support all the availability and durability features of Single-AZ file systems. In addition, they are designed to provide continuous availability to data, even when an Availability Zone is unavailable. In a Multi-AZ deployment, Amazon FSx automatically provisions and maintains a standby file server in a different Availability Zone. Any changes written to disk in your file system are synchronously replicated across Availability Zones to the standby. With Amazon FSx Multi-AZ deployments can enhance availability during planned system maintenance, and help protect your data against instance failure and Availability Zone disruption. If there is planned file system maintenance or unplanned service disruption, Amazon FSx automatically fails over to the secondary file server, allowing you to continue accessing your data without manual intervention.

Multi-AZ file systems are ideal for business-critical workloads that require high availability to shared Windows file data. Examples of these include business applications, web serving environments, and Microsoft SQL Server.

Therefore, the correct answer is: Use AWS DataSync to copy data to a new Amazon FSx file system that uses a Multi-AZ deployment type. After copying, point the applications to use the new Amazon FSx share. AWS DataSync will continuously replicate data between the FSx share until you are able to point the application to the new share.

The option that says: Take a backup of the current Amazon FSx file system. Restore this backup to a new Amazon FSx file system with a deployment type of Multi-AZ. After restoration, point the applications to use the new Amazon FSx share is incorrect. This is possible, however, after the data backup is complete, new data may have been written on the original FSx share. You should use AWS Data Sync to sync data between the shares.

The option that says: Use AWS DataSync to continuously sync data to a second Amazon FSx file system that uses a Single-AZ deployment type. In the event of failure, point the applications to use the second Amazon FSx share is incorrect. This is still non-compliant because the FSx file system is deployed on a Single-AZ. It will also introduce unnecessary downtime if you can’t detect the failure of the primary FSx share.

The option that says: On the AWS management console, update the Amazon FSx file system to use a Multi-AZ deployment type is incorrect. It is not possible to update the deployment type of the FSx file system once it is created. You will need to re-create the file system for this scenario.

 

References:

https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html

https://aws.amazon.com/blogs/aws/amazon-fsx-for-windows-file-server-update-new-enterprise-ready-features/

https://aws.amazon.com/fsx/windows/faqs/

 

Check out these Amazon FSx and AWS DataSync Cheat Sheets:

https://tutorialsdojo.com/amazon-fsx/

https://tutorialsdojo.com/aws-datasync/

---

## Câu 18 — ❌ SAI

### Câu hỏi

An international enterprise is leveraging AWS Organizations for the administration of its various AWS accounts. Their primary IT operations account has a VPC where multiple applications are deployed. This VPC is linked to a transit gateway. As part of a new initiative, they have established a staging server environment in a staging account that requires connectivity to the applications in the primary IT operations account.

Due to the nature of the staging process, resources in the staging account will be frequently terminated and re-provisioned. The staging team also requires the capability to reconfigure their connection to the primary IT operations account as needed.

What approach would satisfy these conditions?

### Các phương án

- **A.** Enable automatic acceptance for the transit gateway attachments in the staging account and share the transit gateway with the staging account using AWS Resource Access Manager (AWS RAM). ✅
- **B.** Establish Direct Connect connections from the staging account to each application in the primary IT operations account.
- **C.** Create a new transit gateway from the staging account to the primary IT operations account for each connection. For each connection, send a peering request from the staging account’s transit gateway to the primary IT operations account’s transit gateway.
- **D.** Enable automatic acceptance for the transit gateway attachments in the staging account and create a VPC endpoint in the staging account for each application in the primary IT operations account. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Transit Gateway is a service that enables customers to connect their Amazon Virtual Private Clouds (VPCs) and their on-premises networks to a single gateway. When you create attachments to a transit gateway, you can configure automatic acceptance for shared attachments, which means that the attachments are automatically accepted and the connection is established.

AWS RAM is a service that enables you to easily and securely share AWS resources with any AWS account or within your AWS Organization. You can share AWS Transit Gateways, Subnets, AWS License Manager configurations, and more. You retain ownership of shared resources, and you can revoke access at any time.

Hence, the correct answer is: Enable automatic acceptance for the transit gateway attachments in the staging account and share the transit gateway with the staging account using AWS Resource Access Manager (AWS RAM). By enabling automatic acceptance for the transit gateway attachments, the staging account can easily connect to the primary IT operations account. This approach allows for easy reconfiguration of connections as needed, which is a requirement in the question. Furthermore, by sharing the transit gateway with the staging account using AWS RAM, the staging account can access the resources in the primary IT operations account, providing the necessary connectivity for the staging process.

The option that says: Create a new transit gateway from the staging account to the primary IT operations account for each connection. For each connection, send a peering request from the staging account’s transit gateway to the primary IT operations account’s transit gateway is incorrect because creating a new transit gateway for each connection would be inefficient and unnecessary. It would also complicate the process of reconfiguring connections, which is something the staging team needs to be able to do easily.

The option that says: Enable automatic acceptance for the transit gateway attachments in the staging account and create a VPC endpoint in the staging account for each application in the primary IT operations account is incorrect because while this option does involve enabling automatic acceptance for the transit gateway attachments, creating a VPC endpoint in the staging account for each application in the primary IT operations account is not the most efficient or flexible solution. It would require a significant amount of configuration and wouldn’t easily allow for reconfiguration of connections.

The option that says: Establish Direct Connect connections from the staging account to each application in the primary IT operations account is incorrect because while Direct Connect does provide a dedicated network connection from a network to AWS, it’s not as flexible or easily reconfigurable. It’s also typically used for more stable, long-term connections rather than a frequently changing staging environment.

 

References:

https://repost.aws/knowledge-center/transit-gateway-sharing

https://docs.aws.amazon.com/ram/latest/userguide/what-is.html

 

Check out these AWS Transit Gateway and AWS Resource Access Manager Cheat Sheets:

https://tutorialsdojo.com/aws-transit-gateway/

---

## Câu 19 — ❌ SAI

### Câu hỏi

A company has hundreds of AWS accounts in an organization in AWS Organizations. The accounts are associated with one of the three Organization Units (OU): PROD, DEV, and UAT. The company uses the vpc-sg-open-only-to-authorized-ports AWS Config managed rule, deployed as part of a Config conformance pack, to determine if a security group that allows incoming traffic at ‘0.0.0.0/0’ is created on any of the OUs. An Amazon SNS topic is configured to send email alerts to the security team when a security group is flagged as non-compliant.

There are critical security groups that must not be modified by users. The security team wants to prevent accounts in the PROD OU from altering the rules of these security groups.

Which solution would meet the requirements?

### Các phương án

- **A.** Apply a remediation action to the Config rule using the AWSConfigRemediation-RemoveUnrestrictedSourceIngressRules AWS System Manager Automation document.
- **B.** Tag the security groups using the key value ‘scope:private’. Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:ResourceTag/scope”: “private” condition key. Attach the SCP to the PROD OU. ✅
- **C.** Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:SourceIp”: “0.0.0.0/0” condition key. Attach the SCP to the PROD OU. 👈 *(bạn chọn)*
- **D.** Create an AWS Lambda function that calls the RevokeSecurityGroupIngress on security groups that have an inbound rule allowing traffic from 0.0.0.0/0. Subscribe the Lambda function to the SNS topic.

> **Bạn chọn:** C  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

Service control policies (SCPs) in AWS Organizations are a means of centrally controlling permissions to services and actions across multiple AWS accounts. They allow you to manage permissions in your organization centrally by applying policies to organizational units (OUs) and accounts.

In this scenario, the company wants to prevent specific security groups within the PROD OU from being modified. To achieve this, you can implement a Service Control Policy (SCP) that denies the ec2:AuthorizeSecurityGroup* actions. This policy targets only the security groups tagged with a specific label, such as ‘scope:private’. Note that ‘scope:private’ is merely an example of a tag name; you can choose any name that fits your organizational structure or naming conventions. By tagging the crucial security groups accordingly and referencing this tag in the SCP, you can prevent unauthorized modifications.

Hence, the correct answer is: Tag the security groups using the key value ‘scope:private’. Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:ResourceTag/scope”: “private” condition key. Attach the SCP to the PROD OU.

The option that says: Apply a remediation action to the Config rule using the AWSConfigRemediation-RemoveUnrestrictedSourceIngressRules AWS System Manager Automation document is incorrect. This option is a reactive measure, not a proactive one. It does not prevent security groups that allow traffic from 0.0.0.0/0 being created in the first place. Instead, it identifies non-compliant resources after they’ve been created and then attempts to fix them. Therefore, it does not meet the security team’s requirement to prevent the creation of such security groups.

The option that says: Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:SourceIp”: “0.0.0.0/0” condition key. Attach the SCP to the PROD OU is incorrect. This option would restrict modification of security groups that have a source IP of 0.0.0.0/0 for everyone in the organization, not just the PROD OU. It’s too broad and doesn’t specifically target the critical security groups.

The option that says: Create an AWS Lambda function that calls the RevokeSecurityGroupIngress on security groups that have an inbound rule allowing traffic from 0.0.0.0/0. Subscribe the Lambda function to the SNS topic is incorrect. Similar to one of the incorrect options, this one is only a reactive measure rather than a proactive one. The security group allowing all incoming traffic would still be created initially, and then the Lambda function would remove the ingress rule.

 

References:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html

https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/

 

Check out this AWS Organizations Cheat Sheet:

https://tutorialsdojo.com/aws-organizations/

---

## Câu 20 — ❌ SAI

### Câu hỏi

A global financial institution hosts a critical trading platform in a single AWS Region. The platform uses Amazon EC2 instances behind an Application Load Balancer (ALB) for the front end, an Amazon RDS SQL Server for the database, and an Amazon S3 bucket for storing compliance reports.

The market analysis team performs extensive data analysis on the database, especially during market volatility which impacts platform performance. Regulatory requirements demand data availability and integrity during disasters. A solutions architect must develop a disaster recovery plan that minimizes data loss during regional disruptions and addresses the slowdown caused by the team’s data analysis.

What approach would best satisfy these requirements?

### Các phương án

- **A.** Establish a scheduled job that generates snapshots of the RDS DB instance on an hourly basis. Copy the snapshots to another Region. Integrate Amazon ElastiCache with the RDS database. Create AMIs from the EC2 instances and replicate them in another Region. Enable S3 Cross-Region Replication (CRR) to sync data from the primary S3 bucket to a bucket in the other Region. In case of a regional disruption, restore the database from the latest RDS snapshot, launch EC2 instances from the replicated AMIs, set up an ALB to serve the application, and update the application to use the new S3 bucket.
- **B.** In a different AWS Region, establish a read replica of the RDS DB instance. Direct the market analysis team to execute their queries on this read replica. Generate AMIs from the EC2 instances that are running the application frontend and replicate these AMIs to the new Region. Implement S3 Cross-Region Replication (CRR) to duplicate data from the original S3 bucket to a newly created S3 bucket in the new Region. In the event of a disaster, promote the read replica to a standalone DB instance. Create EC2 instances using the replicated AMIs and set up an ALB to serve the application to the end users. Adjust the application settings to reference the new S3 bucket. ✅
- **C.** Take a snapshot of the RDS DB instance and export it to an S3 bucket. Direct the market analysis team to perform their queries on the exported snapshot. Schedule an AWS Lambda function to periodically sync the data from the primary S3 bucket to a new S3 bucket in the alternate Region. Launch EC2 instances and set up an ALB in the alternate Region. Reconfigure the application to access data from the new S3 bucket.
- **D.** Migrate the existing database to Amazon DynamoDB and utilize DynamoDB global tables. Direct the market analysis team to interact with a global table in an alternate Region. Establish an AWS Lambda function that periodically syncs the data of the primary S3 bucket with a secondary S3 bucket in the alternate Region. Initiate EC2 instances and establish an ALB in the alternate Region. Adjust the application’s settings to reference the secondary S3 bucket. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon RDS Read Replica allows you to create one or more read-only copies of your database instance. This can be within the same AWS Region or in a different one. This helps to offload read traffic from the primary database instance, thereby improving the performance of the application.

An Amazon Machine Image (AMI) contains the necessary information to launch a virtual server instance in the cloud. You must specify an AMI when you launch an instance. In the context of the question, AMIs of the EC2 instances that host the application frontend are created and copied to a separate Region.

Amazon S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different AWS Regions. CRR can help ensure that data is available in different regions and can be accessed with minimal latency. In the given scenario, CRR duplicates data from the original S3 bucket to a newly created S3 bucket in the new Region.

In the scenario, by creating a read replica of the RDS SQL Server in a different AWS Region, the analysis team can perform their intensive queries without affecting the primary database’s performance. This setup also enhances disaster recovery capabilities; in the event of a regional disruption, the read replica can be quickly promoted to a standalone DB instance, minimizing downtime and data loss. Additionally, replicating AMIs of the EC2 instances and implementing S3 Cross-Region Replication for compliance reports ensures that all components of the application can be redeployed in the secondary region, maintaining data integrity and availability as per regulatory requirements.

Hence, the correct answer is: In a different AWS Region, establish a read replica of the RDS DB instance. Direct the market analysis team to execute their queries on this read replica. Generate AMIs from the EC2 instances that are running the application frontend and replicate these AMIs to the new Region. Implement S3 Cross-Region Replication (CRR) to duplicate data from the original S3 bucket to a newly created S3 bucket in the new Region. In the event of a disaster, promote the read replica to a standalone DB instance. Create EC2 instances using the replicated AMIs and set up an ALB to serve the application to the end users. Adjust the application settings to reference the new S3 bucket.

The option that says: Migrate the existing database to Amazon DynamoDB and utilize DynamoDB global tables. Direct the market analysis team to interact with a global table in an alternate Region. Establish an AWS Lambda function that periodically syncs the data of the primary S3 bucket with a secondary S3 bucket in the alternate Region. Initiate EC2 instances and establish an ALB in the alternate Region. Adjust the application’s settings to reference the secondary S3 bucket is incorrect. While this setup provides built-in multi-region redundancy, the migration from a relational database system to a NoSQL database could involve substantial changes to the application architecture, potentially introducing significant complexity and compatibility issues.

The option that says: Establish a scheduled job that generates snapshots of the RDS DB instance on an hourly basis. Copy the snapshots to another Region. Integrate Amazon ElastiCache with the RDS database. Create AMIs from the EC2 instances and replicate them in another Region. Enable S3 Cross-Region Replication (CRR) to sync data from the primary S3 bucket to a bucket in the other Region. In case of a regional disruption, restore the database from the latest RDS snapshot, launch EC2 instances from the replicated AMIs, set up an ALB to serve the application, and update the application to use the new S3 bucket. is incorrect because while this could help in a disaster recovery scenario, it won’t much help with the performance issues due to the market analysis team’s operations. Additionally, the recovery time could be longer compared to the correct option, as it involves restoring the database from a snapshot.

The option that says: Take a snapshot of the RDS DB instance and export it to an S3 bucket. Direct the market analysis team to perform their queries on the exported snapshot. Schedule an AWS Lambda function to periodically sync the data from the primary S3 bucket to a new S3 bucket in the alternate Region. Launch EC2 instances and set up an ALB in the alternate Region. Reconfigure the application to access data from the new S3 bucket is incorrect This approach is not practical for a trading platform that requires near-real-time data analysis. Querying directly on exported snapshots does not allow for dynamic or interactive querying capabilities which is important for timely market analysis. Furthermore, the periodic sync of S3 data via Lambda does not enhance the platform’s ability to handle regional disruptions smoothly or efficiently.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html

 

Check out this AWS Disaster Recovery Cheat Sheet:

https://tutorialsdojo.com/aws-well-architected-framework-disaster-recovery/

---

## Câu 21 — ❌ SAI

### Câu hỏi

A media organization operates a content delivery system that experiences peak loads whenever new content is released. The release dates and times for the content are pre-set and automatically triggered. The system is hosted on an Amazon ECS (Elastic Container Service) cluster, consisting of Amazon EC2 On-Demand Instances within an ASG (Auto Scaling Group) that uses a predictive scaling policy. The Amazon ECS cluster frequently retrieves data from an Amazon S3 bucket located in the same AWS Region. All traffic routes through a NAT gateway.

The organization aims to reduce platform costs, all while ensuring that availability is not compromised.

What combination of steps can be taken to achieve this goal? (Select TWO.)

### Các phương án

- **A.** Enable S3 Intelligent-Tiering to move objects to cheaper storage tiers automatically. 👈 *(bạn chọn)*
- **B.** Replace the NAT gateway with a NAT instance hosted on an Amazon EC2 On-Demand Capacity Reservation.
- **C.** Switch from the predictive scaling policy to a scheduled scaling policy. ✅
- **D.** Create a new ECS capacity provider using an Auto Scaling Group of Spot Instances, and adjust the strategy to distribute weight evenly.
- **E.** Replace the NAT gateway with a Gateway VPC Endpoint for Amazon S3. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** A, E  
> **Đáp án đúng:** C, E  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon EC2 Auto Scaling provides several methods to scale your Auto Scaling group. Here are the main ways you can scale your Auto Scaling group:

Manual Scaling: You can manually adjust the desired capacity of your Auto Scaling group. This method is useful when you need to make immediate changes to your group’s capacity.
Scheduled Scaling: This method allows you to set up scheduled actions to scale your group at specific times. It’s ideal for predictable load changes that occur at fixed times.
Dynamic Scaling: This approach automatically adjusts capacity in response to changing demand. There are three types of dynamic scaling policies: a. Target Tracking Scaling: Adjusts capacity to maintain a specific metric at a target value. b. Step Scaling: Uses step adjustments to scale based on the size of the alarm breach. c. Simple Scaling: Adjusts capacity based on a single scaling adjustment.
Predictive Scaling: This method uses machine learning to forecast future traffic and automatically provisions the right number of EC2 instances in advance. It’s useful for handling cyclical traffic patterns.

In this case, the organization is aware of the specific dates and times for content releases, enabling them to predict peak loads accurately. Currently, the Auto Scaling Group (ASG) employs a predictive scaling policy, which uses machine learning to anticipate traffic patterns. While this approach is effective, it can be more expensive compared to scheduled scaling, especially when the timing of peak loads is known. Transitioning to a scheduled scaling policy would allow the organization to scale resources precisely when needed, thereby reducing unnecessary scaling and costs.

Gateway VPC Endpoints are specifically designed for Amazon S3 and DynamoDB. They enable resources within a Virtual Private Cloud (VPC) to communicate with S3 or DynamoDB without going through the public internet. Gateway endpoints use prefix lists in the VPC route table to direct traffic to the target service. This setup provides a secure and cost-effective way to access S3 or DynamoDB from within a VPC.

The media organization frequently retrieves data from an Amazon S3 bucket. Their current setup involves a NAT gateway, which can lead to significant data transfer costs. By replacing the NAT gateway with a Gateway VPC Endpoint for Amazon S3, the organization can keep data traffic within the AWS network, thereby reducing data transfer costs and improving performance. This change maintains availability while aligning with the goal of cost reduction.

Hence, the correct answers are:

– Replace the NAT gateway with a Gateway VPC Endpoint for Amazon S3.

– Switch from the predictive scaling policy to a scheduled scaling policy.

The option that says: Replace the NAT gateway with a NAT instance hosted on an Amazon EC2 On-Demand Capacity Reservation is incorrect. While NAT instances may be less expensive than NAT gateways, they can also pose a single point of failure. Moreover, managing and patching a NAT instance typically involves extra operational overhead, which can lead to potential availability risks. Also, since Gateway VPC Endpoint is free, it’s a much cheaper alternative to using a NAT instance or NAT gateway.

The option that says: Create a new ECS capacity provider using an Auto Scaling Group of Spot Instances, and adjust the strategy to distribute weight evenly is incorrect. While spot instances can significantly reduce costs, there is a risk of interruption. If capacity is reclaimed, availability can suffer unless a robust fallback plan exists. The question’s scenario explicitly states that the organization wants to maintain availability without interruption.

The option that says: Enable S3 Intelligent-Tiering to move objects to cheaper storage tiers automatically is incorrect. Although S3 Intelligent-Tiering can primarily reduce S3 storage costs, it does not address the NAT Gateway charges or the immediate scaling needs. The main cost driver in the scenario is traffic going through the NAT gateway and the ECS cluster’s scaling strategy.

 

References:

https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-create-scheduled-action.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-vpc/

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

---

## Câu 22 — ❌ SAI

### Câu hỏi

An aerospace company launched hundreds of satellites into orbit. At regular intervals, the satellites send telemetry data to the earth base station which then uploads everything to an Amazon S3 bucket. Each satellite has a unique identification number that is used as a prefix for the data being received. For compliance purposes, another S3 bucket was created in a secondary region and S3 replication was configured to copy all data from the primary S3 bucket. One of the satellites was identified as a “master” satellite and its data must be completely replicated to the secondary bucket within 30 minutes of the initial upload to the primary S3 bucket.

Which of the following options is the recommended solution in order to meet the above requirements?

### Các phương án

- **A.** Configure AWS DataSync agent on the earth base station to copy the data from the primary Amazon S3 bucket to the secondary S3 bucket. Choose “Use available” to allow DataSync to use all network bandwidth for copying data. Monitor the status of the task using Amazon EventBridge. Create a rule that will trigger an alert when the TRANSFERRING status exceeds 30 minutes.
- **B.** Create another Amazon S3 bucket to store the data from the “master” satellite. Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold.
- **C.** Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Select the S3 Replication Time Control option when setting the destination bucket. Monitor the maximum replication time to the secondary bucket by creating an Amazon EventBridge rule that will trigger an alert when the replication time exceeds the 30 min threshold. ✅
- **D.** On the primary S3 bucket, enable Amazon S3 Transfer Acceleration. Configure the base station to filter the data based on the prefix of the “master” satellite and upload this data to the transfer acceleration endpoint. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

S3 Replication Time Control (S3 RTC) helps you meet compliance or business requirements for data replication and provides visibility into Amazon S3 replication times. S3 RTC replicates most objects that you upload to Amazon S3 in seconds and 99.99 percent of those objects within 15 minutes.

With S3 RTC, you can monitor the total number and size of objects that are pending replication and the maximum replication time to the destination Region. Replication metrics are available through the AWS Management Console and Amazon CloudWatch, in which you can configure alerts. S3 RTC by default, includes S3 replication metrics and S3 event notifications, with which you can monitor the total number of S3 API operations that are pending replication, the total size of objects pending replication, and the maximum replication time. Replication metrics can be enabled independently of S3 RTC.

With S3 RTC, Amazon S3 events can notify you in the rare instance when objects do not replicate within 15 minutes and when those objects replicate successfully to their destination Region.

Therefore, the correct answer is: Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Select the S3 Replication Time Control option when setting the destination bucket. Monitor the maximum replication time to the secondary bucket by creating an Amazon EventBridge rule that will trigger an alert when the replication time exceeds the 30 min threshold. S3 RTC is backed by an SLA that ensures most objects uploaded in S3 are replicated within seconds, with 99.99 percent of those objects in within 15 minutes.

The option that says: Configure AWS DataSync agent on the earth base station to copy the data from the primary Amazon S3 bucket to the secondary S3 bucket. Choose “Use available” to allow DataSync to use all network bandwidth for copying data. Monitor the status of the task using Amazon EventBridge. Create a rule that will trigger an alert when the TRANSFERRING status exceeds 30 minutes is incorrect. This approach does not have a distinction for the “master” satellite’s data and just replicates everything. The replication for the “master” satellite’s data can be delayed if other objects are replicated first.

The option that says: Create another Amazon S3 bucket to store the data from the “master” satellite. Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold is incorrect. Without S3 RTC, you can’t guarantee the replication to be completed in 30 minutes because S3 replication can sometimes take a couple of hours.

The option that says: On the primary S3 bucket, enable Amazon S3 Transfer Acceleration. Configure the base station to filter the data based on the prefix of the “master” satellite and upload this data to the transfer acceleration endpoint. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold is incorrect. This may be possible, but it involves unnecessary changes to the base station configuration. Without S3 RTC, you can’t guarantee the replication to be completed in 30 minutes because S3 replication can sometimes take a couple of hours.

 

References:

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-time-control.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough-5.html

https://aws.amazon.com/s3/features/replication/

 

Check out these Amazon S3 and Amazon CloudWatch Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-cloudwatch/

---

## Câu 23 — ❌ SAI

### Câu hỏi

A global energy firm aggregates sensor readings from its offshore wind turbines and stores the data in an Amazon S3 data lake governed by AWS Lake Formation. The research department runs analytics on Amazon EC2 instances in two private subnets within a VPC. The EC2 instances already have an IAM role with permission to access the S3 bucket.

Corporate security mandates that only specific, approved networks be used when retrieving turbine data. The research team must be able to continue to access the data lake without exposing it to public internet traffic.

What combination of actions will meet these requirements? (Select THREE.)

### Các phương án

- **A.** Configure a Gateway VPC endpoint for Amazon S3 within the research team's VPC. ✅ 👈 *(bạn chọn)*
- **B.** Update the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointArn matches the correct S3 access point. ✅ 👈 *(bạn chọn)*
- **C.** Create a NAT Gateway and modify the VPC’s route table to direct traffic from the private subnets to the NAT Gateway. 👈 *(bạn chọn)*
- **D.** Modify the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointAccount matches the research team’s AWS account.
- **E.** Encrypt the data lake objects using AWS Key Management Service (AWS KMS) and reassign the key to the research team's IAM role
- **F.** Set up an S3 access point in the research team's AWS account and reference its Amazon Resource Name (ARN) when retrieving objects. ✅

> **Bạn chọn:** A, B, C  
> **Đáp án đúng:** A, B, F  
> **Kết quả:** ❌ Sai

### Giải thích

S3 Access Points are unique network endpoints for Amazon S3 buckets that make data access management easier for shared datasets. Each access point is linked to a single S3 bucket and has its own access policy. This allows you to create custom access policies tailored to different applications or user groups that access the same bucket. Access points also include network origin control and Block Public Access settings, making them beneficial for managing access in complex scenarios, such as multi-tenant applications or data lakes.

Gateway VPC Endpoints are specifically designed for Amazon S3 and DynamoDB. They enable resources within a Virtual Private Cloud (VPC) to communicate with S3 or DynamoDB without going through the public internet. Gateway endpoints use prefix lists in the VPC route table to direct traffic to the target service. This setup provides a secure and cost-effective way to access S3 or DynamoDB from within a VPC. Unlike interface endpoints, gateway endpoints do not require elastic network interfaces and do not utilize AWS PrivateLink technology.

Combining S3 Access Points with Gateway VPC Endpoints enhances security and simplifies access management for applications using shared datasets in Amazon S3.

Creating a Gateway VPC endpoint for Amazon S3 within the research team’s VPC ensures that all traffic between the EC2 instances and the S3 data lake remains private and does not traverse the public internet. Setting up an S3 access point simplifies access management and enforces restrictions by allowing policies tied to VPCs, ensuring only approved networks can retrieve the data. Additionally, updating the S3 bucket policy to validate the s3:DataAccessPointArn ensures data access is explicitly routed through the approved access point. Together, these measures fulfill the requirements for secure, restricted, and private access to the S3 data lake while maintaining compliance with corporate policies.

Therefore, the correct answers are:

– Configure a Gateway VPC endpoint for Amazon S3 within the research team’s VPC.

– Set up an S3 access point in the research team’s AWS account and reference its Amazon Resource Name (ARN) when retrieving objects.

– Update the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointArn matches the correct S3 access point.

The option that says: Modify the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointAccount matches the research team’s AWS account is incorrect. Using the condition s3:DataAccessPointAccount allows access based on the AWS account associated with the S3 access point. While this limits access to resources within the specified account, it does not enforce fine-grained control. This means that resources in other VPCs within the account could potentially use the access point to retrieve data, provided they have permissions.

The option that says: Encrypt the data lake objects using AWS Key Management Service (AWS KMS) and reassign the key to the research team’s IAM role is incorrect. While encryption improves security, it does not directly address the requirement to restrict network access to the data lake. The research team’s IAM role already has permissions to access the bucket, so this step is unnecessary.

The option that says: Create a NAT Gateway and modify the VPC’s route table to direct traffic from the private subnets to the NAT Gateway is incorrect because. A NAT Gateway would allow resources in the private subnets to access the internet, contradicting the requirements. Using a Gateway VPC endpoint would solve this problem as it provides a private connection between the VPC and Amazon S3.

 

References:

https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html

 

Check out these Amazon VPC and Amazon S3 Cheat Sheets:

https://tutorialsdojo.com/amazon-vpc/

---

## Câu 24 — ❌ SAI

### Câu hỏi

A company is planning to use Amazon WorkSpaces along with virtual desktop infrastructure (VDI) to replace their outdated workstations. The employees use these workstations to access proprietary software that handles sensitive financial data. The company’s security policy mandates that access to this software must be limited to only the corporate headquarters and its satellite offices. The corporation is also considering opening a new satellite office in the next quarter.

Which solution would provide the highest operational efficiency while meeting these requirements?

### Các phương án

- **A.** Establish a connection using Amazon WorkSpaces with a WorkSpaces directory and AWS Direct Connect for secure access to the proprietary software from the corporate headquarters and its satellite offices.
- **B.** Utilize Windows Firewall with a custom WorkSpace image to restrict access to the proprietary software from the corporate headquarters and its satellite offices. 👈 *(bạn chọn)*
- **C.** Configure Amazon WorkSpaces with a WorkSpaces directory and apply IP access control group rules to restrict access to the proprietary software from the corporate headquarters and its satellite offices. ✅
- **D.** Deploy Amazon EC2 instances with Elastic IP addresses for each employee, and restrict access to the proprietary software to these IP addresses.

> **Bạn chọn:** B  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon WorkSpaces allows you to control which IP addresses your WorkSpaces can be accessed from. By using IP address-based control groups, you can define and manage groups of trusted IP addresses and only allow users to access their WorkSpaces when connected to a trusted network.

An IP access control group acts as a virtual firewall that controls the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can associate each IP access control group with one or more directories. You can create up to 100 IP access control groups per Region per AWS account. However, you can only associate up to 25 IP access control groups with a single directory.

Each directory is associated with a default IP access control group, which includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory. If you don’t associate an IP access control group with your directory, the default group is used. If you associate an IP access control group with a directory, the default IP access control group is disassociated.

Hence, the correct answer is: Configure Amazon WorkSpaces with a WorkSpaces directory and apply IP access control group rules to restrict access to the proprietary software from the corporate headquarters and its satellite offices.

The option that says: Deploy Amazon EC2 instances with Elastic IP addresses for each employee, and restrict access to the proprietary software to these IP addresses is incorrect because while it’s possible to use Amazon EC2 instances with Elastic IP addresses, this approach doesn’t align with the company’s plan to use Amazon WorkSpaces and VDI. Moreover, managing individual EC2 instances for each employee can be operationally inefficient and costly.

The option that says: Establish a connection using Amazon WorkSpaces with a WorkSpaces directory and AWS Direct Connect for secure access to the proprietary software from the corporate headquarters and its satellite offices is incorrect. Although AWS Direct Connect provides a dedicated network connection from the corporate headquarters to AWS, it doesn’t inherently limit access to the proprietary software to only the corporate headquarters and its satellite offices. Additional configuration would be needed to enforce this restriction, which could complicate the setup and management.

The option that says: Utilize Windows Firewall with a custom WorkSpace image to restrict access to the proprietary software from the corporate headquarters and its satellite offices is incorrect because while Windows Firewall can help secure a system, it’s not designed to restrict access based on geographic location. Moreover, managing firewall rules on individual WorkSpaces can be operationally complex and doesn’t provide a centralized way to enforce the company’s security policy.

 

References:

https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html

https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html

 

Check out this Amazon WorkSpaces Cheat Sheet:

https://tutorialsdojo.com/amazon-workspaces/

---

## Câu 25 — ✅ ĐÚNG

### Câu hỏi

A healthcare insurance company plans to implement a blockchain-based system to store patient records using Amazon Managed Blockchain. The system must allow patient records to be exchanged among various private entities while ensuring that the data is securely stored, transparent, and immutable.

What solution would meet these requirements?

### Các phương án

- **A.** Use AWS Lambda functions to store a hash of each PII data on an Amazon Managed Blockchain network. Store the PII data off-chain in an Amazon DynamoDB table. ✅ 👈 *(bạn chọn)*
- **B.** Store all patient data on an Amazon Managed Blockchain network. Use EC2 Arbitrum Nodes to encrypt and decrypt data before they are stored in the blockchain network. Use an Application Load Balancer (ALB) to access the EC2 nodes in an HTTPS endpoint.
- **C.** Store all patient data on an Amazon Managed Blockchain network.
- **D.** Store only the patient’s name and ID on an Amazon Managed Blockchain network. Store all other PII data off-chain in an Amazon DynamoDB table.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon Managed Blockchain is a fully managed service that helps build and manage Web3 applications with blockchain frameworks. With Amazon Managed Blockchain, you can securely transact and share data on a distributed and immutable ledger.

You can deploy a REST API to provide a simple interface to read and write to the blockchain network. One implementation of building REST APIs is with a serverless architecture using AWS Lambda and Amazon API Gateway. Lambda has built-in fault tolerance and provides high availability for the service itself and the functions it operates, allowing developers to focus on developing the business logic. An API Gateway provides a layer of security to AWS Lambda, allowing for features such as authentication and rate-limiting.

In this scenario, sensitive patient data is processed in two main environments: on-chain and off-chain. The on-chain component involves storing a hashed version of the Personally Identifiable Information (PII), such as patient names, on Amazon Managed Blockchain. This ensures data integrity and immutability, as each hash is a unique representation of the data that cannot be altered.

For the off-chain component, the actual PII is stored in Amazon DynamoDB. This approach leverages DynamoDB’s scalability and fast access to secure and manage sensitive patient data. The reference to the on-chain hash ensures that any data retrieved can be verified against its immutable blockchain record.

AWS Lambda functions serve as the intermediary that processes the PII. First, they generate a hash of the data and store it on-chain in the blockchain. Second, Lambda functions encrypt the PII before storing it off-chain in DynamoDB. They manage the encryption process using secure algorithms and AWS Key Management Service (KMS) for key management, ensuring that the data is protected throughout its lifecycle.

Therefore, the correct answer is: Use AWS Lambda functions to store a hash of each PII data on an Amazon Managed Blockchain network. Store the PII data off-chain in an Amazon DynamoDB table.

The option that says: Store all patient data on an Amazon Managed Blockchain network is incorrect. This approach could lead to privacy concerns since blockchains are inherently transparent and could be accessible to all participants in the network. This approach may not comply with regulations such as HIPAA in the healthcare industry, which require strict privacy controls over patient information.

The option that says: Store only the patient’s name and ID on an Amazon Managed Blockchain network. Store all other PII data off-chain in an Amazon DynamoDB table is incorrect. Patient names and IDs are still considered personally identifiable information (PII) and are subject to data protection regulations. It is best practice not to store these in plaintext on blockchain.

The option that says: Store all patient data on an Amazon Managed Blockchain network. Use EC2 Arbitrum Nodes to encrypt and decrypt data before they are stored in the blockchain network. Use an Application Load Balancer (ALB) to access the EC2 nodes in an HTTPS endpoint is incorrect. Storing all patient data directly is not the best practice due to privacy and security regulations. Also, using Arbitrum is not appropriate in the context of Amazon Managed Blockchain, which already provides support for the underlying infrastructure that utilizes blockchain technology. Using an ALB with the EC2 nodes is also incorrect, as these do not provide any implementation of proper authentication and authorization for data access.

 

References:

https://aws.amazon.com/managed-blockchain/faqs

https://aws.amazon.com/blogs/database/building-a-serverless-blockchain-application-with-amazon-managed-blockchain/

---

## Câu 26 — ✅ ĐÚNG

### Câu hỏi

A company has hundreds of AWS accounts and numerous S3 buckets scattered across multiple AWS Regions. The organization is struggling to understand its storage usage, and they’ve noticed a significant increase in S3 costs. They are interested in obtaining historical trends and comparing differences in storage usage and activity over the last 6 months.

Which solution can be used to accomplish this objective with the least amount of development overhead?

### Các phương án

- **A.** Use Amazon S3 Storage Lens to create a customized dashboard that aggregates data from all the organization's AWS accounts and regions. Configure the dashboard to include advanced metrics ✅ 👈 *(bạn chọn)*
- **B.** Enable Storage Class Analysis on S3 buckets. Use the Amazon S3 console storage usage visualizations for trend analysis. Move objects between storage classes based on reports.
- **C.** Use IAM Access Analyzer for S3 to review bucket-level permissions and monitor for policy changes. Download the findings in CSV format and store them in an S3 bucket. Visualize the data using Amazon QuickSight.
- **D.** Enable Amazon S3 Inventory to generate object-level metadata reports. Follow AWS Trusted Advisor recommendations for cost optimization.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide visibility into object-storage usage and activity. You can use S3 Storage Lens metrics to generate summary insights, such as finding out how much storage you have across your entire organization or which are the fastest-growing buckets and prefixes.

You can also use S3 Storage Lens metrics to identify cost-optimization opportunities, implement data protection and security best practices, and improve the performance of application workloads. For example, you can identify buckets that don’t have S3 Lifecycle rules to expire incomplete multipart uploads that are more than 7 days old. You can also identify buckets that aren’t following data-protection best practices, such as using S3 Replication or S3 Versioning. S3 Storage Lens also analyzes metrics to deliver contextual recommendations that you can use to optimize storage costs and apply best practices for protecting your data.

In the scenario, the organization wants to understand its S3 storage spread over multiple accounts and regions for the past 6 months. S3 Storage Lens meets these needs effectively by aggregating data and providing a unified view with the ability to look back up to 15 months using the advanced metrics tier.

Therefore, the correct answer is: Use Amazon S3 Storage Lens to create a customized dashboard that aggregates data from all the organization’s AWS accounts and regions. Configure the dashboard to include advanced metrics

The option that says: Use IAM Access Analyzer for S3 to review bucket-level permissions and monitor for policy changes. Download the findings in CSV format and store them in an S3 bucket. Visualize the data using Amazon QuickSight is incorrect. IAM Access Analyzer for S3 simply focuses on reviewing bucket-level permissions. While it provides security insights, it does not offer detailed storage usage, historical trends, or comparisons over time.

The option that says: Enable Amazon S3 Inventory to generate object-level metadata reports. Follow AWS Trusted Advisor recommendations for cost optimization is incorrect. While you can use S3 Inventory to track storage to some extent and analyze object types, the complexity involved in aggregating and analyzing this data for hundreds of accounts makes this approach less suitable for the task.

The option that says: Enable Storage Class Analysis on S3 buckets. Use the Amazon S3 console storage usage visualizations for trend analysis. Move objects between storage classes based on reports is incorrect. Storage Class Analysis can help in optimizing storage costs by suggesting what objects to move between storage classes; however, it doesn’t offer a comprehensive view for understanding storage usage, historical trends, or comparisons over multiple AWS accounts and regions.

 

References:

https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html

https://aws.amazon.com/blogs/aws/s3-storage-lens/

 

Check out this Amazon S3 Cheat Sheet:

https://tutorialsdojo.com/amazon-s3/

---

## Câu 27 — ✅ ĐÚNG

### Câu hỏi

A company runs an auction website using AWS Fargate fronted by an Application Load Balancer (ALB). The company manages an Amazon Route 53 hosted zone for its domain, which it presents to users. The domain is linked to a CloudFront distribution that points to the ALB as the origin.

Lately, there have been reports of intermittent HTTP 502 (Bad Gateway) errors. Initial investigation revealed that a misconfiguration in the Fargate task definition is causing the problem. This results in users seeing the ALB’s default error page.

To improve user experience, the company wants users to be redirected to a custom error page while they troubleshoot the issue. The solution must be achieved in the least amount of operational overhead.

Which solution would meet the requirements?

### Các phương án

- **A.** Upload the error HTML page to an Amazon S3 bucket and enable static website hosting. Update the existing Route 53 record by adding a failover policy that routes traffic to the S3 website endpoint when health checks become unhealthy.
- **B.** Upload an error HTML page to an Amazon S3 bucket that is configured with static website hosting. Modify the CloudFront distribution by adding a new origin for the S3 bucket and enforcing Origin Access Control (OAC). Create a CloudFront custom error response that returns the error page when the application returns a 502 HTTP error code as an origin failover ✅ 👈 *(bạn chọn)*
- **C.** Create a Lambda function that adds a redirection rule to the path of the error page within the application. Configure a CloudWatch alarm to trigger this Lambda function when the Application Load Balancer (ALB) metric HTTPCode_Target_5XX_Count registers a value of one.
- **D.** Modify the Application Load Balancer’s rules by adding a condition for the path /*. Configure a fixed-response action that returns a 502 response code and a custom error message in the response body.

> **Bạn chọn:** B  
> **Đáp án đúng:** B  
> **Kết quả:** ✅ Đúng

### Giải thích

Normally, when an object served through CloudFront is unavailable, the web server will return an HTTP status code to CloudFront to indicate the problem. For example, if a client requests an invalid URL, your web server would return an HTTP 404 (Not Found) status code to CloudFront, and CloudFront would relay that status code back to the client.

However, with CloudFront’s custom error response feature, you can configure CloudFront to return a custom error page to the viewer instead. This customization can be done by updating your CloudFront distribution to specify the custom error page.

You can specify an origin group for your CloudFront origin if, for example, you want to configure origin failover for scenarios when you need high availability. Use origin failover to designate a primary origin for CloudFront plus a second origin that CloudFront automatically switches to when the primary origin returns specific HTTP status code failure responses.

In the given scenario, the most straightforward approach to displaying a custom error page is by uploading the page to an Amazon S3 bucket, and then adding that bucket as an origin in the existing CloudFront distribution. Then, you configure a custom error response within CloudFront, pointing it to the path of the error page stored in the S3 bucket. This method has minimal operational overhead and does not require any coding.

Therefore, the correct answer is: Upload an error HTML page to an Amazon S3 bucket that is configured with static website hosting. Modify the CloudFront distribution by adding a new origin for the S3 bucket and enforcing Origin Access Control (OAC). Create a CloudFront custom error response that returns the error page when the application returns a 502 HTTP error code as an origin failover.

The option that says: Create a Lambda function that adds a redirection rule to the path of the error page within the application. Configure a CloudWatch alarm to trigger this Lambda function when the Application Load Balancer (ALB) metric HTTPCode_Target_5XX_Count registers a value of one is incorrect. This option presents unnecessary development overhead for the purpose of simply displaying a custom error page. This solution also doesn’t provide an instant response to users experiencing a 502 error, as there might be a delay between the error occurrence and the CloudWatch alarm triggering the Lambda function.

The option that says: Upload the error HTML page to an Amazon S3 bucket and enable static website hosting. Update the existing Route 53 record by adding a failover policy that routes traffic to the S3 website endpoint when health checks become unhealthy is incorrect. This approach is more suited for scenarios where there is a complete failure of the primary endpoint rather than intermittent errors. The health checks may not register a failure if the 502 errors are sporadic and the system is generally operational, thus the failover might not be triggered.

The option that says: Modify the Application Load Balancer’s rules by adding a condition for the path /*. Configure a fixed-response action that returns a 502 response code and a custom error message in the response body is incorrect. Although this could provide some level of customization, it does not fully meet the requirement of redirecting users to a custom error page. Instead, it just modifies the response body of the error. Moreover, using a fixed-response rule at the root path will return a 502 response for all requests, regardless of their paths, essentially blocking all requests.

 

References:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GeneratingCustomErrorResponses.html

https://aws.amazon.com/blogs/aws/custom-error-pages-and-responses-for-amazon-cloudfront/

 

Check out the Amazon CloudFront Cheat Sheet:

https://tutorialsdojo.com/amazon-cloudfront/

---

## Câu 28 — ❌ SAI

### Câu hỏi

A company is managing a hybrid environment comprising on-premises servers and Amazon EC2 instances. Their servers are a mix of Linux and Windows systems. The company utilizes AWS Security Hub as its cloud security posture management (CSPM) service to automate security best practice checks, aggregate alerts, and enables automated remediation.

Separate teams handle the environment, each using different tools for patching. The company wants to simplify this process and requires a consolidated view of patch statuses across all servers.

Which combination of actions will meet the requirements? (Select TWO.)

### Các phương án

- **A.** Create an AWS Systems Manager Automation document for running patching jobs. Use Amazon EventBridge to schedule these jobs and configure the AWS Systems Manager OpsCenter to generate patch compliance reports.
- **B.** Generate patch compliance reports using AWS System Manager Patch Manager. ✅ 👈 *(bạn chọn)*
- **C.** Register all servers as managed nodes in AWS System Manager. Use AWS System Manager Patch Manager for handling patch operations. ✅
- **D.** Create a custom AWS Config rule for detecting non-compliant patches across servers. Set up an AWS Config remediation rule using AWS Systems Manager Automation documents to apply patches. Configure AWS Config to send patch compliance reports to an Amazon S3 bucket. 👈 *(bạn chọn)*
- **E.** Generate patch compliance reports using Amazon Inspector. Use Amazon Athena for aggregating and viewing patch compliance reports.

> **Bạn chọn:** B, D  
> **Đáp án đúng:** B, C  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Systems Manager allows you to manage your hybrid environment as it can work with both on-premises servers and AWS instances. AWS Systems Manager Patch Manager, a feature of AWS Systems Manager, enables you to automate the process of patching managed instances with both security related and other types of updates.

You can use Patch Manager to apply patches for both operating systems and applications (On Windows Server, application support is limited to updates for applications released by Microsoft.) You can use Patch Manager to install Service Packs on Windows nodes and perform minor version upgrades on Linux nodes. You can patch fleets of Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, on-premises servers, and virtual machines (VMs) by operating system type. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

Patch Manager provides a convenient view of patch status in the console and lets you export this data as a CSV file for analysis.

In the scenario, using Patch Manager allows you to both conduct patching operations and generate a consolidated view of patch statuses. This simplifies the overall patching process.

Hence, the correct answers are:

– Register all servers as managed nodes in AWS System Manager. Use AWS System Manager Patch Manager for handling patch operations.

– Generate patch compliance reports using AWS System Manager Patch Manager.

The option that says: Create a custom AWS Config rule for detecting non-compliant patches across servers. Set up an AWS Config remediation rule using AWS Systems Manager Automation documents to apply patches. Configure AWS Config to send patch compliance reports to an Amazon S3 bucket is incorrect. AWS Config is primarily designed for assessing, auditing, and evaluating the configurations of AWS resources, not specifically for managing patch operations. While it could provide some level of oversight for patch compliance, it would not simplify the patching process itself nor provide a straightforward, consolidated view of patch statuses.

The option that says: Create an AWS Systems Manager Automation document for running patching jobs. Use Amazon EventBridge to schedule these jobs and configure the AWS Systems Manager OpsCenter to generate patch compliance reports is incorrect. This option would simplify the patching process to some extent. However, setting up this integration would likely have more overhead compared to using AWS Systems Manager Patch Manager, which is designed specifically for managing patches and can provide a more streamlined and integrated solution.

The option that says: Generate patch compliance reports using Amazon Inspector. Use Amazon Athena for aggregating and viewing patch compliance reports is incorrect. Amazon Inspector is mainly a security vulnerability assessment service, not a tool for patch management. Moreover, Amazon Inspector is not capable of scanning on-premises servers.

 

References:

https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-reports.html

 

Check out this AWS Systems Manager Cheat Sheet:

https://tutorialsdojo.com/aws-systems-manager/

---

## Câu 29 — ❌ SAI

### Câu hỏi

An enterprise uses AWS Organizations to manage hundreds of AWS accounts. Each division falls under a corresponding Organizational Unit (OU) with different permissions for accessing AWS services.

The analytics division has a data analysis tool within each VPC where the enterprise has its workloads running. This tool operates on EC2 instances and runs at least once a week. The collected data is sent to an AWS account dedicated to the analytics division and stored in an Amazon Redshift data warehouse.

The accounting division needs to determine how much it costs to run the analysis tool, so they can bill the analytics division accordingly. All analytics-related resources are already tagged using the AWS tag "expenseUnit": "analytics".

Which set of actions would meet the requirements?

### Các phương án

- **A.** Enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console of the management account. Use AWS Cost and Usage Reports to generate the monthly billing report to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics". ✅
- **B.** In the AWS account of the accounting division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. In the management account, generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics".
- **C.** Create an AWS Resource group of resources tagged with the "expenseUnit": "analytics" in the management account. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics". 👈 *(bạn chọn)*
- **D.** In the AWS account of the analytics division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics".

> **Bạn chọn:** C  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

A tag is a label that you or AWS assigns to an AWS resource. Each tag consists of a key and a value. For each resource, each tag key must be unique, and each tag key can have only one value. You can use tags to organize your resources and cost allocation tags to track your AWS costs on a detailed level.

After you or AWS applies tags to your AWS resources (such as Amazon EC2 instances or Amazon S3 buckets) and you activate the tags in the Billing and Cost Management console, AWS generates a cost allocation report as a comma-separated value (CSV file) with your usage and costs grouped by your active tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services.

In the scenario, the organization is using AWS Organizations to manage multiple accounts, necessitating cross-account cost calculation. The management account, with its organization-wide visibility, is best suited for this task. By enabling the "expenseUnit": "analytics" cost allocation tag at this level, all analytics-related resources across accounts can be tracked. AWS Cost and Usage Reports can then be generated from the management account, with data filtered by the tag, yielding the precise cost for running the analysis tool.

Hence, the correct answer is: Enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console of the management account. Use AWS Cost and Usage Reports to generate the monthly billing report to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics".

Only a management account in an organization and single accounts that aren’t members of an organization have access to the cost allocation tags manager in the Billing and Cost Management console. Hence, the following options are both incorrect:

– In the AWS account of the analytics division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics".

– In the AWS account of the accounting division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. In the management account, generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics".

The option that says: Create an AWS Resource group of resources tagged with the "expenseUnit": "analytics" in the management account. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics" is incorrect. AWS Resource Groups are typically used to manage and automate tasks on a large collection of AWS resources at once. They are not primarily used for cost calculation purposes. It is more straightforward and accurate to use the AWS Cost and Usage Reports, which provide detailed cost information and allow filtering by tags.

 

References:

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html

https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-allocation-blog-series-2-aws-generated-vs-user-defined-cost-allocation-tag/

 

Check out this AWS Billing and Cost Management Cheat sheet:

https://tutorialsdojo.com/aws-billing-and-cost-management/

---

## Câu 30 — ❌ SAI

### Câu hỏi

A company is running a stateless application on Amazon ECS with AWS Fargate. The Fargate cluster runs behind an Application Load Balancer (ALB) that serves internet traffic. The Amazon Aurora MySQL database cluster is on a private subnet in the same VPC.  To connect to the database, the database hostname is passed to the application using the DB_HOST environment variable. The database password is encrypted in AWS Secrets Manager and is passed to the application using the DB_PASSWORD environment variable. Upon running the Fargate tasks, the application was unable to access the database.

Which of the following actions should be taken in order to resolve this issue? (Select THREE.)

### Các phương án

- **A.** Set the “DB_PASSWORD” environment variable as “ValueFrom” with the secret name from AWS Secrets Manager.
- **B.** Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database instance endpoint.
- **C.** Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database cluster endpoint. ✅
- **D.** Configure the Aurora MySQL database security group to allow inbound traffic from the AWS Fargate cluster on the TCP port 3306. ✅ 👈 *(bạn chọn)*
- **E.** Set the “DB_PASSWORD” environment variable as “ValueFrom” with the ARN of the secret from AWS Secrets Manager. ✅ 👈 *(bạn chọn)*
- **F.** Configure the AWS Fargate cluster security group to allow inbound traffic from the Amazon Aurora MySQL cluster on the TCP port 3306. 👈 *(bạn chọn)*

> **Bạn chọn:** D, E, F  
> **Đáp án đúng:** C, D, E  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon Aurora typically involves a cluster of DB instances instead of a single instance. Each connection is handled by a specific DB instance. When you connect to an Aurora cluster, the host name and port that you specify point to an intermediate handler called an endpoint.

Each Aurora DB cluster has one cluster endpoint and one primary DB instance. A cluster endpoint (or writer endpoint) for an Aurora DB cluster connects to the current primary DB instance for that DB cluster. This endpoint is the only one that can perform write operations such as DDL statements. Because of this, the cluster endpoint is the one that you connect to when you first set up a cluster or when your cluster only contains a single DB instance.

An instance endpoint connects to a specific DB instance within an Aurora cluster. Each DB instance in a DB cluster has its own unique instance endpoint. So there is one instance endpoint for the current primary DB instance of the DB cluster, and there is one instance endpoint for each of the Aurora Replicas in the DB cluster.

Amazon ECS enables you to inject sensitive data into your containers by storing your sensitive data in AWS Secrets Manager secrets and then referencing them in your container definition. Sensitive data stored in Secrets Manager secrets can be exposed to a container as environment variables or as part of the log configuration.

When you inject a secret as an environment variable, you can specify the full contents of a secret, a specific JSON key within a secret, or a specific version of a secret to inject.

Within your container definition, you can specify the following:

-The secrets object containing the name of the environment variable to set in the container.

-The Amazon Resource Name (ARN) of the Secrets Manager secret.

-Additional parameters that contain the sensitive data to present to the container.

The option that says: Set the “DB_PASSWORD” environment variable as “ValueFrom” with the ARN of the secret from AWS Secrets Manager is correct. The environment variable should contain the ARN from AWS Secrets Manager.

The option that says: Configure the Aurora MySQL database security group to allow inbound traffic from the AWS Fargate cluster on the TCP port 3306 is correct. You need to ensure that the Aurora database is open to accept connections from the Fargate cluster.

The option that says: Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database cluster endpoint is correct. The cluster endpoint should be used as “Value” of the environment variable. This is the main endpoint that accepts read/write connections. 

The option that says: Set the “DB_PASSWORD” environment variable as “ValueFrom” with the secret name from AWS Secrets Manager is incorrect. You should use the ARN of the secret from the Secrets Manager, not the secret name.

The option that says: Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database instance endpoint is incorrect. Amazon Aurora has different instance endpoints for write and reader nodes. It is recommended to use the cluster endpoint here because this is the one that can perform both read/write operations. 

The option that says: Configure the AWS Fargate cluster security group to allow inbound traffic from the Amazon Aurora MySQL cluster on the TCP port 3306 is incorrect. The AWS Fargate cluster will connect to the database, therefore, the database must allow connections from the Aurora cluster.

 

References:

https://aws.amazon.com/premiumsupport/knowledge-center/ecs-data-security-container-task/

https://docs.aws.amazon.com/AmazonECS/latest/userguide/specifying-sensitive-data-secrets.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html

 

Check out these Amazon Aurora and AWS Fargate Cheat Sheets:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/aws-fargate/

---

## Câu 31 — ❌ SAI

### Câu hỏi

A company has a designated AWS account for each project of its development team. All of these AWS accounts are linked to the main AWS account under the same AWS Organizations. The CFO allocates a budget for each project owner. Each project owner is allowed to provision any cloud resources that they need but all resources should have the Project tag which is used for cost allocation. After a recent audit, several team members are not adding the Project tag on their Amazon EC2 instances which results in inaccurate cost reports.

Which of the following steps should be implemented to identify instances with the missing tag and to prevent the creation of instances without the Project tag? (Select THREE.)

### Các phương án

- **A.** Apply an SCP to the AWS Organization that will deny the ec2:RunInstances action if the Project tag is not applied. ✅
- **B.** Configure an AWS Config aggregator for the AWS organization to generate a list of all EC2 instances without the Project tag. ✅
- **C.** Create an IAM policy on each project account that will deny the ec2:RunInstances action if the Project tag is not applied.
- **D.** Create an AWS Config rule on each project account to flag any resources if the Project tag is not applied. ✅ 👈 *(bạn chọn)*
- **E.** Leverage AWS Security Hub as an aggregator to generate a list of all EC2 instances without the Project tag. 👈 *(bạn chọn)*
- **F.** Create an assessment in Amazon Inspector to scan the AWS Organization and generate a list of all EC2 instances with the missing Project tag. 👈 *(bạn chọn)*

> **Bạn chọn:** D, E, F  
> **Đáp án đúng:** A, B, D  
> **Kết quả:** ❌ Sai

### Giải thích

Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. SCPs help you to ensure your accounts stay within your organization’s access control guidelines. SCPs are available only in an organization that has all features enabled. SCPs aren’t available if your organization has enabled only the consolidated billing features.

By denying the action to run instances without the Project tag, you enforce tagging policies and prevent non-compliant resource creation.

An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from the following:

-Multiple accounts and multiple regions.

-Single account and multiple regions.

-An organization in AWS Organizations and all the accounts in that organization which have AWS Config enabled.

Hence, the correct answers are:

– Create an AWS Config rule on each project account to flag any resources if the Project tag is not applied. AWS Config rules allow you to continuously monitor and evaluate your AWS resource configurations. By setting up a rule to flag resources without the Project tag, you ensure that any non-compliant resources are identified promptly.

– Apply an SCP to the AWS Organization that will deny the ec2:RunInstances action if the Project tag is not applied. The SCP applied to the organization will deny members from spawning EC2 instances without the Project tag.

– Configure an AWS Config aggregator for the AWS organization to generate a list of all EC2 instances without the Project tag. An aggregator can collect AWS Config configuration and compliance data from multiple AWS accounts and regions. AWS Config can identify EC2 instances if they have the required Project tag or not.

The option that says: Create an assessment in Amazon Inspector to scan the AWS Organization and generate a list of all EC2 instances with the missing Project tag is incorrect. AWS Inspector is primarily used for scanning vulnerabilities inside EC2 instances, and not about proper cost allocation tagging.

The option that says: Create an IAM policy on each project account that will deny the ec2:RunInstances action if the Project tag is not applied is incorrect because while IAM policies can control access, using SCPs at the organization level is typically more effective for enforcing such rules across multiple accounts. IAM policies would need to be individually managed in each account, which is less efficient.

The option that says: Leverage AWS Security Hub as an aggregator to generate a list of all EC2 instances without the Project tag is incorrect. This service performs security best practice checks, aggregates alerts, and enables automated remediation, but it is not suitable for tag checking of AWS resources.

 

References:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html
https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html

Check out these AWS Config Cheat Sheet and SCP vs IAM comparison:

https://tutorialsdojo.com/aws-config/
https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

---

## Câu 32 — ❌ SAI

### Câu hỏi

A company is using an on-premises Windows file server to store 1 TB of data. About 5 GB worth of new data is being produced every day. The company has an AWS Direct Connect connection from the on-premises network to the AWS VPC. As part of the ongoing migration process, about half of its Windows-based workload has been migrated to the AWS cloud. The data stored on the on-premises server needs to be available on a file system for the servers in AWS.

Which of the following options is the recommended migration strategy for this scenario?

### Các phương án

- **A.** Create a new Amazon Elastic File System (EFS) share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon EFS. Mount the EFS share on the Windows servers.
- **B.** Create an Amazon S3 bucket on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon S3. Use AWS Transfer Family to access the files.
- **C.** Create an Amazon FSx for Windows File Server share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon FSx. ✅
- **D.** Use AWS Storage Gateway – File Gateway to create an SMB share on the on-premises data center to replace the existing Windows file server. Point the existing file shares to the new file gateway share. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS storage services, and also between AWS storage services. DataSync can copy data between Network File System (NFS), Server Message Block (SMB) file servers, Hadoop Distributed File System (HDFS), self-managed object storage, AWS Snowcone, Amazon Simple Storage Service (Amazon S3) buckets, Amazon EFS file systems, and Amazon FSx for Windows File Server file systems.

Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system. FSx for Windows File Server has the features, performance, and compatibility to easily lift and shift enterprise applications to the AWS Cloud. A Windows file share is a specific folder (and its subfolders) within your file system that you make accessible to your compute instances with SMB.

The primary resources in Amazon FSx are file systems and backups. A file system is where you store and access your files and folders. A file system is made up of one or more Windows file servers and storage volumes. FSx for Windows File Server backups are file-system-consistent, highly durable, and incremental. To ensure file system consistency, Amazon FSx uses the Volume Shadow Copy Service (VSS) in Microsoft Windows.

Therefore, the correct answer is: Create an Amazon FSx for Windows File Server share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon FSx. Amazon FSx for Windows File Server can replicate data between on-premises networks and AWS. Once the whole migration is complete, all Windows-based servers on the cloud can seamlessly use the FSx shares with completely synced data.

The option that says: Create a new Amazon Elastic File System (EFS) share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon EFS. Mount the EFS share on the Windows servers is incorrect. Windows servers by default do not typically support the mounting of NFS shares.

The option that says: Create an Amazon S3 bucket on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon S3. Use AWS Transfer Family to access the files is incorrect because Amazon S3 is an object storage service, not a file system. While S3 is primarily used for storing and retrieving large amounts of data, it doesn’t provide the same file system interface that Windows applications typically require. Additionally, using AWS Transfer Family adds unnecessary complexity to the setup.

The option that says: Use AWS Storage Gateway – File Gateway to create an SMB share on the on-premises data center to replace the existing Windows file server. Point the existing file shares to the new file gateway share is incorrect. This may be possible, however, the data in the file gateway is sent to Amazon S3. Once all Windows-based workloads are migrated to the AWS cloud, you will still need to set up a new Windows File server for file sharing. This can cause an interruption to your applications.

 

References:

https://aws.amazon.com/fsx/windows/

https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html

https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

 

Check out these Amazon FSx and AWS DataSync Cheat Sheets:

https://tutorialsdojo.com/amazon-fsx/

https://tutorialsdojo.com/aws-datasync/

---

## Câu 33 — ❌ SAI

### Câu hỏi

A solutions architect is planning the migration of hundreds of Hyper-V servers from an on-premises data center to AWS. To design an effective AWS infrastructure, the solutions architect needs to understand the type of running processes, CPU and memory load, and network dependencies between each server. 

What steps should the architect take to collect and analyze this data? (Select THREE.)

### Các phương án

- **A.** Create a custom PowerShell script to collect basic server inventory from the Hyper-V servers. Upload the generated inventory file to AWS Transform for migration assessment.
- **B.** Create a migration assessment job in AWS Transform by using the discovery data. ✅
- **C.** Deploy the AWS Transform discovery tool on the on-premises Hyper-V servers to collect server data. ✅
- **D.** Use AWS Transform migration assessment results, chat-based analysis, and generated reports to evaluate right-sizing recommendations, dependencies, costs, and migration wave plans. ✅ 👈 *(bạn chọn)*
- **E.** Install the Amazon CloudWatch agent on the on-premises Hyper-V servers to collect system-level metrics. Use AWS System Manager OpsCenter to export the collected data to an Amazon S3 bucket. 👈 *(bạn chọn)*
- **F.** Create an AWS Glue Extract, Transform, Load (ETL) job to prepare the data for querying. Use Amazon Athena to run SQL queries on the transformed data for deeper analysis. 👈 *(bạn chọn)*

> **Bạn chọn:** D, E, F  
> **Đáp án đúng:** B, C, D  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Transform is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.

With AWS Transform, you can:

Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS
Migrate VMware workloads to Amazon EC2
Modernize .NET applications to Linux-ready cross-platform .NET
Assess workloads for migration readiness

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.

The AWS Transform discovery tool automatically identifies server inventory within your organization to prepare for migration. The tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To use the discovery tool, you’ll configure one or more discovery sources, let the tool run, and then review the results in the Discovered Inventory pane.

Once you’ve set up a discovery source, the discovery tool begins collecting information. The time required for the tool to analyze your network completely depends on the size of your environment. For a directional migration business case, you can utilize the Migration Portfolio Assessment (MPA) files that the tool generates once server collection is complete.

AWS Transform assessments help you evaluate the cost, feasibility, and business value of migrating your on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinements through chat.

You can use migration assessments to:

– Obtain cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx

– Receive automated right-sizing recommendations

– Assess business value and sustainability impact

– Compare multiple migration scenarios side by side

– Refine assessments interactively through chat

– Generate executive presentations and detailed reports

Hence, the correct answers are:

– Deploy the AWS Transform discovery tool on the on-premises Hyper-V servers to collect server data.

– Create a migration assessment job in AWS Transform by using the discovery data.

– Use AWS Transform migration assessment results, chat-based analysis, and generated reports to evaluate right-sizing recommendations, dependencies, costs, and migration wave plans.

The option that says: Create a custom PowerShell script to collect basic server inventory from the Hyper-V servers. Upload the generated inventory file to AWS Transform for migration assessment is incorrect. While it’s technically possible, this approach is significantly more complex and less comprehensive than using the AWS Transform discovery tool.

The option that says: Install the Amazon CloudWatch agent on the on-premises Hyper-V servers to collect system-level metrics. Use AWS System Manager OpsCenter to export the collected data to an Amazon S3 bucket is incorrect. Although CloudWatch can be used to collect system-level metrics, it doesn’t provide detailed, in-depth discovery information needed for migration planning, such as dependencies, configurations, and utilization of on-premises servers. Furthermore, AWS Systems Manager OpsCenter typically provides a central location where you can manage and resolve operational issues, but it’s not a migration tool.

The option that says: Create an AWS Glue Extract, Transform, Load (ETL) job to prepare the data for querying. Use Amazon Athena to run SQL queries on the transformed data for deeper analysis is incorrect. AWS Glue’s ETL capabilities are unnecessary for this task because AWS Transform primarily provides the data in a format that is ready for analysis. There is no need to transform the data before running SQL queries.

 

References:

https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html

https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html

https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html

 

Check out the AWS Migration Services Cheat Sheet:

https://tutorialsdojo.com/aws-cheat-sheets-migration-services/

---

## Câu 34 — ✅ ĐÚNG

### Câu hỏi

An e-commerce company experiences operational disruptions during peak shopping periods. The web application, serving a global customer base, is currently hosted on a single Amazon EC2 instance, which often becomes unresponsive under heavy load. The application makes read-intensive calls to an Amazon RDS for PostgreSQL database.

A Solutions Architect must enhance the application’s reliability with minimal development effort.

Which of the following solutions meets this requirement?

### Các phương án

- **A.** Upgrade the EC2 instance type to a more powerful and larger instance type. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations.
- **B.** Deploy the application across multiple EC2 instances managed by an Auto Scaling group, with an Elastic Load Balancer to distribute traffic. Migrate the database to Amazon Aurora and utilize Aurora Replicas for handling read-intensive tasks. ✅ 👈 *(bạn chọn)*
- **C.** Set up an Auto Scaling group for the EC2 instances that host the application. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations.
- **D.** Upgrade the EC2 instance type to a more powerful and larger instance type. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. Migrate the database to Amazon Aurora and utilize Aurora Replicas to handle read-intensive tasks.

> **Bạn chọn:** B  
> **Đáp án đúng:** B  
> **Kết quả:** ✅ Đúng

### Giải thích

Auto Scaling Groups: Auto Scaling groups help ensure that you have the correct number of Amazon EC2 instances available to handle your application’s load. You can create launch configurations that serve as templates for launching instances. The Auto Scaling group can automatically increase or decrease the number of instances based on user-defined policies, schedules, and health checks.

Elastic Load Balancing: Elastic Load Balancing automatically distributes incoming application traffic across multiple Amazon EC2 instances in one or more Availability Zones. It provides high availability by routing traffic to healthy instances and monitors the health of registered instances.

Amazon CloudFront: Amazon CloudFront is a content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds. It caches content at edge locations around the world, reducing the load on the origin servers.

Amazon RDS Multi-AZ Deployment: Amazon RDS Multi-AZ deployment provides enhanced availability and data durability for DB instances. It creates a primary database instance and synchronously replicates the data to a standby instance in a different Availability Zone.

Amazon Aurora: Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud. It combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open-source databases.

Amazon Aurora Replicas: Aurora Replicas are independent endpoints in an Aurora DB cluster, capable of driving read operations and offloading read workloads from the primary instance. They can help scale read operations and improve overall performance.

The solution, which combines Auto Scaling groups, Elastic Load Balancing, Amazon Aurora, and Aurora Replicas, provides the most comprehensive solution to meet the requirements of:

Enhancing reliability: By distributing the application across multiple EC2 instances managed by an Auto Scaling group, the solution ensures that the application can automatically scale resources based on demand, reducing the risk of operational disruptions during peak periods.

Improving performance and handling heavy loads: The Elastic Load Balancer distributes traffic across multiple instances, ensuring that the application can handle heavy loads without becoming unresponsive.

Addressing the performance bottleneck for read-intensive operations: By migrating the database to Amazon Aurora, the solution leverages a database service designed for better performance and scalability compared to traditional relational databases.

Utilizing Aurora Replicas: Aurora Replicas are used to handle read-intensive tasks, offloading the read workload from the primary instance and improving overall performance.

Minimal development effort: This solution leverages managed services and does not require significant code changes, minimizing the development effort required.

Hence, the correct answer is: Deploy the application across multiple EC2 instances managed by an Auto Scaling group, with an Elastic Load Balancer to distribute traffic. Migrate the database to Amazon Aurora and utilize Aurora Replicas for handling read-intensive tasks.

The option that says: Set up an Auto Scaling group for the EC2 instances that host the application. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations is incorrect. While this option addresses the scalability and high availability concerns for the web application and database, it does not fully resolve the read-intensive performance bottleneck. Using the standby instance of the Multi-AZ RDS deployment for read operations may provide some relief, but it is not as efficient as using dedicated read replicas like Aurora Replicas. Additionally, using CloudFront is not necessary for this use case, as it is primarily designed for content delivery and caching static assets. Lastly, you cannot directly use an Auto Scaling group (ASG) as the origin for an Amazon CloudFront distribution.

The option that says: Upgrade the EC2 instance type to a more powerful and larger instance type. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. Migrate the database to Amazon Aurora and utilize Aurora Replicas to handle read-intensive tasks is incorrect. This option addresses the read-intensive database performance bottleneck by using Aurora Replicas, which is a good solution. However, it suggests upgrading the EC2 instance type instead of using an Auto Scaling group and Elastic Load Balancer. Upgrading the instance type may provide temporary relief, but it does not address the scalability and high availability concerns for the web application. Additionally, just like the previous option, using CloudFront is not necessary for this use case.

The option that says: Upgrade the EC2 instance type to a more powerful and larger instance type. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations is incorrect. While it addresses high availability for the database using Multi-AZ deployment, just like the previous option that uses Amazon RDS, it does not fully resolve the read-intensive performance bottleneck, and it is not as efficient as using dedicated read replicas like Aurora Replicas. Additionally, upgrading the EC2 instance type alone may not be sufficient to handle peak loads, and it does not provide the same level of flexibility and automatic scaling as an Auto Scaling group combined with an Elastic Load Balancer.

 

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Overview.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

---

## Câu 35 — ❌ SAI

### Câu hỏi

A media company has a serverless video encoding system. When a video clip is uploaded to an S3 bucket, an AWS Lambda function written in Python is automatically invoked to process the clip. The Lambda function encodes the video for different aspect ratios suitable for various screen devices. After processing, the application saves the S3 location of the encoded videos into a DynamoDB table.

Recently, the company started processing longer video clips, leading to Lambda function timeouts despite having set the maximum timeout limit. The company wants a redesigned architecture that ensures timeout issues will never happen again, all without having to manage the underlying infrastructure.

Which combination of actions should be taken to redesign the application’s architecture? (Select TWO.)

### Các phương án

- **A.** Implement an AWS Step Functions state machine. Use a combination of Map and Parallel states to break down the video encoding process into smaller tasks. Configure provisioned concurrency to pre-warm Lambda functions associated with each state.
- **B.** Containerize the video encoding logic into a Docker image. Push the Docker image to the Amazon Elastic Container Registry (Amazon ECR). ✅
- **C.** Rewrite the existing code to use Java. Update the Lambda function’s runtime setting to use the Java runtime. Enable AWS Lambda SnapStart
- **D.** Use Amazon SQS to queue the video encoding tasks and deploy an auto-scaling group of EC2 instances running the encoding logic. Set CloudWatch alarms to scale in and out based on the queue length and use S3 event notifications to enqueue tasks. 👈 *(bạn chọn)*
- **E.** Create an ECS task definition to use the new image stored in ECR and configure it to run tasks using the Fargate launch type. Create a Lambda function that is triggered by S3 PUT events to initiate the ECS task. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** D, E  
> **Đáp án đúng:** B, E  
> **Kết quả:** ❌ Sai

### Giải thích

Elastic Container Registry (ECR) serves as a fully-managed Docker container registry, making it easier for developers to store, manage, and deploy Docker container images. Amazon Elastic Container Service (ECS) is a container management service that enables you to run Docker containers in a distributed manner across a fleet.

ECS and ECR work seamlessly together: ECS can pull Docker images stored in ECR to instantiate containers as part of tasks defined in ECS.

In the scenario, the company is experiencing timeouts with AWS Lambda due to the processing of longer video clips. Using ECS with the Fargate launch type allows for long-running tasks that go beyond the 15-minute limit imposed by Lambda. Containerizing the video encoding logic and storing the image in ECR simplifies the deployment and scaling of this service. A Lambda function triggered by S3 events can initiate these ECS tasks, thus providing a serverless architecture that satisfies the requirements of not having to manage the underlying infrastructure while eliminating the timeout issue.

Thus, the correct answers are:

– Containerize the video encoding logic into a Docker image. Push the Docker image to the Amazon Elastic Container Registry (Amazon ECR).

– Create an ECS task definition to use the new image stored in ECR, and configure it to run tasks using the Fargate launch type. Create a Lambda function that is triggered by S3 PUT events to initiate the ECS task.

The option that says: Implement an AWS Step Functions state machine. Use a combination of Map and Parallel states to break down the video encoding process into smaller tasks. Configure provisioned concurrency to pre-warm Lambda functions associated with each state is incorrect. AWS Step Functions with Map and Parallel states can indeed help break down tasks into smaller parts that can be executed by individual Lambda functions. However, even with provisioned concurrency, Lambda functions would still be subjected to a maximum execution timeout, making this option not entirely reliable for longer videos.

The option that says: Rewrite the existing code to use Java. Update the Lambda function’s runtime setting to use the Java runtime. Enable AWS Lambda SnapStart is incorrect. While switching to Java and enabling AWS Lambda SnapStart could reduce start-up latency, this approach doesn’t eliminate the risk of timeout errors. Lambda functions remain constrained by a maximum execution time, regardless of the runtime or optimizations used.

The option that says: Use Amazon SQS to queue the video encoding tasks and deploy an auto-scaling group of EC2 instances running the encoding logic. Set CloudWatch alarms to scale in and out based on the queue length and use S3 event notifications to enqueue tasks is incorrect. Using Amazon SQS with an auto-scaling group of EC2 instances does enable the handling of long-running tasks, but this approach requires the management of EC2 instances, including their scaling policies and lifecycle

 

References:

https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html

https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html

 

Check out this Amazon ECR and AWS Fargate Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-container-registry-amazon-ecr/

https://tutorialsdojo.com/aws-fargate/

---

## Câu 36 — ❌ SAI

### Câu hỏi

A company plans to migrate an application consisting of an AWS Lambda function and an Amazon Aurora MySQL database from one AWS account to another. Both accounts belong to the same organization in AWS Organizations. The company intends for the target account to deploy the application in the same AWS region as the source account. The Lambda function is created from a ZIP deployment package stored in Amazon S3.

Which combination of actions should be performed to migrate the application with the least amount of downtime? (Select TWO.)

### Các phương án

- **A.** Use AWS Resource Access Manager (AWS RAM) to share the Aurora MySQL DB cluster with the target AWS account. Create an Aurora clone in the target account. ✅
- **B.** Use the mysqldump utility to export the data and schema from the Aurora MySQL database into a SQL dump file. Transfer the SQL dump file to the target AWS account and import it into a newly created Aurora MySQL database instance.
- **C.** Use AWS Resource Access Manager (AWS RAM) to share the Lambda function with the target account.
- **D.** Download the ZIP deployment package and upload it to the target account's S3 bucket. Create a new Lambda function in the target account using the ZIP package. ✅ 👈 *(bạn chọn)*
- **E.** Create a snapshot of the existing Aurora MySQL database and share the snapshot with the target AWS account. Restore the database from the snapshot in the target account. 👈 *(bạn chọn)*

> **Bạn chọn:** D, E  
> **Đáp án đúng:** A, D  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon Aurora cloning allows you to create a new cluster that uses the same Aurora cluster volume and has the same data as the original. The process is designed to be fast and cost-effective. The new cluster with its associated data volume is called a clone.

Creating a clone is faster and more space-efficient than physically copying the data using other techniques, such as restoring from a snapshot like you would in Amazon RDS or using the native mysqldump utility.

AWS Resource Access Manager (AWS RAM) is a service that enables you to securely share your AWS resources across AWS accounts or within your organization. It simplifies the resource and policy management required for sharing resources, ensuring that only intended accounts have access to shared items. It’s important to note that only certain types of resources can be shared using AWS RAM, and a list of these resources is available on the AWS documentation.

In the scenario, by using AWS RAM to share the existing Aurora MySQL DB cluster with the target account, the database can be cloned swiftly in the target account. This cloning process is recommended for cross-account migrations within the same AWS region. Moreover, for the Lambda function, the ZIP deployment package can be downloaded and uploaded to the S3 bucket in the target AWS account. A new Lambda function can then be created using this deployment package.

Therefore, the correct answers are:

– Use AWS Resource Access Manager (AWS RAM) to share the Aurora MySQL DB cluster with the target AWS account. Create an Aurora clone in the target account.

– Download the ZIP deployment package and upload it to the target account’s S3 bucket. Create a new Lambda function in the target account using the ZIP package.

The option that says: Use the mysqldump utility to export the data and schema from the Aurora MySQL database into a SQL dump file. Transfer the SQL dump file to the target AWS account and import it into a newly created Aurora MySQL database instance is incorrect. This approach is more time-consuming, particularly for large databases. Restoring from a SQL dump file into a newly created Aurora MySQL database instance in the target account would also require additional time, extending the duration of the migration process.

The option that says: Create a snapshot of the existing Aurora MySQL database and share the snapshot with the target AWS account. Restore the database from the snapshot in the target account is incorrect. While restoring from a snapshot is a viable method for data migration, sharing the snapshot won’t be helpful in this scenario as both the source and target accounts are within the same organization and AWS region already. Performing Aurora Cloning via AWS RAM offers a quicker approach since the source and target accounts are in the same AWS region.

The option that says: Use AWS Resource Access Manager (AWS RAM) to share the Lambda function with the target account is incorrect because AWS AWS RAM does not support direct sharing of Lambda functions between accounts.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.html

https://aws.amazon.com/blogs/aws/amazon-aurora-fast-database-cloning/

https://aws.amazon.com/blogs/database/cross-account-amazon-aurora-mysql-migration-with-aurora-cloning-and-binlog-replication-for-reduced-downtime/

 

Check out this Amazon Aurora Cheat Sheet:

https://tutorialsdojo.com/amazon-aurora/

---

## Câu 37 — ✅ ĐÚNG

### Câu hỏi

A global e-commerce company has a complex microservices architecture deployed on multiple AWS accounts. Each microservice has its own VPC, and all VPC flow logs are sent to a centralized Amazon S3 bucket in Text format. These logs are compressed using the gzip compression method and are kept indefinitely for compliance reasons.

A data analytics team frequently uses Amazon Redshift Spectrum to analyze and query these logs. However, as the number of logs increases, the performance of their data visualizations is decreasing. The company’s lead architect is tasked with improving the performance of the data visualizations and reducing the storage space used by the VPC flow logs.

Which solution will provide the MOST significant improvement in performance?

### Các phương án

- **A.** Store the VPC flow logs in multiple S3 buckets instead of a single centralized bucket.
- **B.** Compress the VPC flow logs using a different compression method like bzip2 instead of gzip.
- **C.** Update the log configuration on the VPC Flow log to output in Parquet format and partition the data by hour. ✅ 👈 *(bạn chọn)*
- **D.** Implement AWS Glue to catalog the VPC flow logs.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

VPC Flow Logs allow you to capture information about the IP traffic going to and from network interfaces in your VPC. This can be useful for a variety of reasons, such as understanding network traffic patterns, identifying potential security issues, auditing usage, and diagnosing network connectivity issues.

These logs are often sent directly to Amazon S3 for long-term storage. However, they are initially stored as raw text files in GZIP format. While this format is useful for certain use cases, it can add complexity and increase costs when it comes to analyzing the log data.

Apache Parquet is an open-source file format that is optimized for use with big data processing frameworks. It stores data in a columnar format, which means it organizes the data by columns rather than by rows. This can lead to significant performance improvements when executing analytical queries.

In addition, Parquet provides different encoding types and supports predicate filtering, which allows non-relevant data to be skipped during queries. This results in fewer reads on Amazon S3 and improved query performance. Furthermore, due to its efficient encoding and good compression ratios, storing VPC flow logs in Parquet format can also help reduce your Amazon S3 storage costs.

Hence, the correct answer is: Update the log configuration on the VPC Flow log to output in Parquet format and partition the data by hour.

The option that says: Compress the VPC flow logs using a different compression method like bzip2 instead of gzip is incorrect because while bzip2 might provide slightly better compression ratios than gzip, the difference is not significant enough to result in a substantial performance improvement. Also, the time taken to compress and decompress bzip2 files is generally more than gzip, which could offset any gains from the slightly better compression ratio.

The option that says: Store the VPC flow logs in multiple S3 buckets instead of a single centralized bucket is incorrect because storing VPC flow logs in multiple S3 buckets would not improve the performance of data visualizations. It might even complicate the data management process without providing any significant benefits.

The option that says: Implement AWS Glue to catalog the VPC flow logs is incorrect because while AWS Glue can be used to catalog data, it does not inherently improve the performance of data visualizations. AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load your data for analytics, but it does not optimize the data for these operations.

 

References:

https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/

https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

 

Check out this Amazon VPC Cheat Sheet:

https://tutorialsdojo.com/amazon-vpc/

---

## Câu 38 — ❌ SAI

### Câu hỏi

A company manages thousands of AWS accounts using AWS Organizations. To ensure compliance and maintain a uniform environment, each member account requires a standardized Virtual Private Cloud (VPC) with specific networking configurations.

The company’s DevOps team has already prepared an AWS CloudFormation template for creating the VPC. They want the deployment of the CloudFormation template to be automated in a consistent manner across the organization. Moreover, the template must be automatically deployed in newly joined accounts.

Which combination of actions will meet the requirements? (Select TWO.)

### Các phương án

- **A.** Enable Service Catalog as a trusted service on AWS Organizations. Provision service-managed permissions.
- **B.** Enable CloudFormation StackSet as a trusted service on AWS Organizations. ✅
- **C.** Create a portfolio in AWS Service Catalog and associate the CloudFormation template as a product. Grant access to this portfolio to all AWS accounts in the organization.
- **D.** In the management account, set up a stack set using the CloudFormation template. Use the service-managed permission model to create the stack. Activate Automatic deployment and set the Organizations as the deployment target. ✅ 👈 *(bạn chọn)*
- **E.** In the member accounts, set up a stack set using the CloudFormation template. Use a self-managed permission model to create the stack. Use Stackset drift detection to enable deployment to new accounts. Specify each Organization Unit (OU) as a deployment target. 👈 *(bạn chọn)*

> **Bạn chọn:** D, E  
> **Đáp án đúng:** B, D  
> **Kết quả:** ❌ Sai

### Giải thích

AWS CloudFormation StackSets extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation. Using an administrator account, you define and manage an AWS CloudFormation template and use the template as the basis for provisioning stacks into selected target accounts across specified regions.

A stack set lets you create stacks in AWS accounts across regions by using a single AWS CloudFormation template. All the resources included in each stack are defined by the stack set’s AWS CloudFormation template. As you create the stack set, you specify the template to use, as well as any parameters and capabilities that the template requires.

In the scenario, in order for StackSets to have the necessary permissions to perform operations in AWS Organizations’ accounts, it must be enabled as a trusted service. To ensure the template is automatically deployed to all accounts (including newly joined ones), a stack set should be created in the management account with service-managed permissions. The AWS Organizations should be set as the deployment target, and automatic deployments should be enabled.

Hence, the correct answers are:

– Enable CloudFormation StackSet as a trusted service on AWS Organizations.

– In the management account, set up a stack set using the CloudFormation template. Use the service-managed permission model to create the stack. Activate Automatic deployment and set the Organizations as the deployment target.

The option that says: Enable Service Catalog as a trusted service on AWS Organizations. Provision service-managed permissions is incorrect. While AWS Service Catalog can be used to create and manage catalogs of IT services, it doesn’t inherently offer a solution for automatic deployments across AWS accounts in an organization, especially for newly joined accounts. The requirement in the question is specifically about deploying AWS CloudFormation templates across multiple accounts and not about managing a service catalog.

The option that says: In the member accounts, set up a stack set using the CloudFormation template. Use a self-managed permission model to create the stack. Use Stackset drift detection to enable deployment to new accounts. Specify each Organization Unit (OU) as a deployment target is incorrect. Setting up a stack set in each member account manually defeats the purpose of AWS CloudFormation StackSets, which is designed to manage resources centrally from a single AWS account. Additionally, StackSet drift detection is used for checking configuration consistency, not for enabling deployment to new accounts.

The option that says: Create a portfolio in AWS Service Catalog and associate the CloudFormation template as a product. Grant access to this portfolio to all AWS accounts in the organization is incorrect. While this option might provide a way to standardize the deployment of services, it still doesn’t address the need for automatic deployment, especially for new accounts joining the organization.

 

References:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started.html

 

Check out this AWS CloudFormation Cheat Sheet:

https://tutorialsdojo.com/aws-cloudformation/

---

## Câu 39 — ✅ ĐÚNG

### Câu hỏi

A company is using a custom software framework to write its web application. The framework is needed as a dependency in order for the application to work. Currently, the framework is installed by an Amazon EC2 user data script and takes about 15-20 minutes to complete. This process has become a bottleneck in the application deployment process. The developers want to have a faster deployment time in order to deliver more frequent application updates.

Which of the following implementations can improve the deployment process?

### Các phương án

- **A.** Compress the custom software framework installation files to make them smaller and store them in an Amazon S3 bucket. Update the user data script to pull the installation files from the S3 bucket.
- **B.** Create an AWS Elastic Beanstalk environment to deploy the application.
- **C.** Create an AWS Systems Manager Automation task and use the AWS-CreateImage document to build a custom AMI with the framework installed. Use this AMI as a baseline for application deployments. ✅ 👈 *(bạn chọn)*
- **D.** Create a pipeline in AWS CodePipeline to parallelize the installation of the software framework and the application during the deployment.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Systems Manager (formerly known as SSM) is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects.

A Systems Manager Automation runbook defines the automation (the actions that Systems Manager performs on your managed instances and AWS resources). Automation includes several pre-defined runbooks that you can use to perform common tasks like restarting one or more Amazon EC2 instances or creating an Amazon Machine Image (AMI). You can create your own runbooks as well. Runbooks use JavaScript Object Notation (JSON) or YAML, and they include steps and parameters that you specify.

Therefore, the correct answer is: Create an AWS Systems Manager Automation task and use the AWS-CreateImage document to build a custom AMI with the framework installed. Use this AMI as a baseline for application deployments. Creating a custom AMI with the software framework pre-installed will significantly speed up the application deployment process. 

The option that says: Compress the custom software framework installation files to make them smaller and store them in an Amazon S3 bucket. Update the user data script to pull the installation files from the S3 bucket is incorrect. Downloading the software framework may be faster from the S3 bucket but extracting the zip file and installation will still take a lot of time. 

The option that says: Create a pipeline in AWS CodePipeline to parallelize the installation of the software framework and the application during the deployment is incorrect. The software framework is a dependency of the application so the software framework needs to be installed first. 

The option that says: Create an AWS Elastic Beanstalk environment to deploy the application is incorrect because while Elastic Beanstalk does simplify the deployment process, it doesn’t address the issue of the time it takes to install the framework.

 

References:

https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-ami-automation/

https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html

 

Check out the AWS Systems Manager Cheat Sheet:

https://tutorialsdojo.com/aws-systems-manager/

---

## Câu 40 — ✅ ĐÚNG

### Câu hỏi

An organization operates an application on AWS Environment. The backend consists of AWS Lambda functions triggered by Amazon API Gateway, with product data stored in an Amazon RDS for MySQL database.

During high-traffic events, the application receives an exponential increase in requests, causing slowdowns. The organization noticed high Lambda invocations, database connections, and CPU utilization on RDS through Amazon CloudWatch. A Solutions Architect must implement a solution to improve the performance of the application.

Which combination of steps in the following options would meet this requirement most efficiently? (Select TWO.)

### Các phương án

- **A.** Enable Amazon RDS Multi-AZ deployments for higher availability and failover support.
- **B.** Modify the Lambda function to use an RDS Proxy endpoint for database queries. ✅ 👈 *(bạn chọn)*
- **C.** Cache frequently accessed data to the RDS database with an Amazon ElastiCache for Redis cluster. ✅ 👈 *(bạn chọn)*
- **D.** Adjust the Lambda function's timeout settings and increase concurrent execution limits.
- **E.** Adjust the memory allocation for Lambda functions and ensure database connections are closed after data retrieval.

> **Bạn chọn:** B, C  
> **Đáp án đúng:** B, C  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon RDS Proxy is a service that allows applications to pool and share database connections, improving their ability to scale and making them more resilient to database failures. When an application connects to an RDS Proxy, the proxy maintains a pool of connections to the database and reuses these connections across requests.

RDS Proxy handles unpredictable spikes in database traffic and queue connections when the maximum limit is reached. This maintains predictable performance for the database. The proxy also enforces AWS Identity and Access Management (IAM) authentication for databases and securely stores credentials in AWS Secrets Manager.

To use RDS Proxy with Lambda functions, you first need to create a proxy and grant necessary permissions to the Lambda execution role. Then, modify the Lambda function code to connect to the proxy endpoint instead of the database endpoint. No other code changes are required. The proxy takes care of connection pooling and throttling traffic between the Lambda function and the database.

Amazon ElastiCache is a web service that makes it easy to set up, manage, and scale distributed in-memory caches.

Amazon ElastiCache for Redis: ElastiCache provides a managed service that handles tasks like provisioning, monitoring, and patching Redis nodes. You can either use serverless caching, which automatically scales a Redis cluster, or design your own clusters by choosing node types and configurations. Redis supports data persistence through replication and snapshots.

Two steps can be taken to improve application performance during high-traffic events. First, cache frequently accessed data in Amazon ElastiCache for Redis cluster to reduce the load on the database. Second, modify the Lambda function to use an RDS Proxy endpoint for database queries, which allows Lambda functions to reuse connections and prevents overloading the database.

Hence, the correct answers are:

– Cache frequently accessed data to the RDS database with an Amazon ElastiCache for Redis cluster.

– Modify the Lambda function to use an RDS Proxy endpoint for database queries.

The option that says: Adjust the memory allocation for Lambda functions and ensure database connections are closed after data retrieval is incorrect. While memory adjustments may enhance Lambda performance slightly, they don’t directly tackle scalability or connection management issues during peak loads. Similarly, closing database connections after retrieval is a good practice but doesn’t efficiently handle connection management in high-traffic scenarios. In contrast, ElastiCache’s data caching reduces database load by serving frequently accessed data from cache, while RDS Proxy optimizes connection management, addressing the specific challenges faced during high-traffic events more effectively. Therefore, opting for RDS Proxy and ElastiCache provides a more robust solution for improving application performance under heavy loads in an AWS Lambda and RDS environment.

The option that says: Adjust the Lambda function’s timeout settings and increase concurrent execution limits is incorrect. Adjusting timeout settings and concurrency might help to some extent but does not tackle the core issues of database load and efficient data retrieval during high traffic, thus not as effective as using RDS Proxy and ElastiCache.

The option that says: Enable Amazon RDS Multi-AZ deployments for higher availability and failover support is incorrect. While Multi-AZ deployments provide high availability and failover capabilities, they are not primarily aimed at improving performance under high load, which is the requirement in this scenario.

References:

https://docs.aws.amazon.com/lambda/latest/operatorguide/traffic-server-based.html

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-elasticache/

https://tutorialsdojo.com/aws-lambda/

---

## Câu 41 — ✅ ĐÚNG

### Câu hỏi

A large media company plans to migrate its infrastructure from its on-premises data center to AWS. The company wants to use different AWS accounts to separate resources for different business units and centrally manage them using AWS Organizations. Initially, the solutions architect will create three accounts. As other business units migrate, more accounts will be added.

A Solutions Architect needs to ensure that AWS CloudTrail is enabled in all existing and future AWS accounts.

Which of the following options is the MOST operationally efficient solution?

### Các phương án

- **A.** Configure an organizational trail in the management account of AWS Organization. ✅ 👈 *(bạn chọn)*
- **B.** Create a custom script running on an Amazon EC2 instance that periodically checks for new AWS accounts and configures CloudTrail trails in each.
- **C.** Configure an Amazon EventBridge rule to trigger an AWS Lambda function. The function will periodically check and create a CloudTrail trail under the organization.
- **D.** Configure a CloudTrail trail in each business unit's AWS account manually when a new account is added and apply an SCP to enforce the logging.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Organization is a useful feature of AWS that enables the consolidation of multiple AWS accounts into a single organizational unit for better management and billing. With this feature, you can create organizational units (OUs) that represent different departments or teams within your organization. Each OU can have its own AWS accounts, which can be subject to the same policies and settings, making it easier to manage and control access to resources.

AWS CloudTrail is a powerful service that allows you to record all API calls and CLI commands made in your AWS account. The service conveniently delivers log files to an S3 bucket, which means you can easily monitor and analyze your account activity. AWS CloudTrail captures all actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. You have the option to create two types of trails – single region trails, which log activity in one region only, or multi-region trails that log across all regions.

An organizational trail in AWS CloudTrail is a type of trail that logs and monitors activity across all AWS accounts within an AWS Organization. The management account or delegated admin can create an organization trail that automatically enables logging in all current and future member accounts of the organization.

The CloudTrail trail configuration includes settings like the S3 bucket for log delivery, log file encryption, event selectors to choose which API calls to log, etc. For organization trails, these settings apply uniformly to all member accounts.

Configuring an organizational trail in the management account is the most effective way to ensure CloudTrail is enabled in all existing and future AWS accounts while maintaining operational efficiency. An organizational trail applies CloudTrail configuration uniformly across all member accounts in the organization. Once created, it will automatically enable CloudTrail to log in new accounts as they are added to the organization without any manual steps. This provides a centralized way to monitor and audit activity in all accounts from a single location. The logs from all accounts will be delivered to the single S3 bucket specified for the organizational trail.

Hence, the correct answer is: Configure an organizational trail in the management account of AWS Organization.

The option that says: Configure an Amazon EventBridge rule to trigger an AWS Lambda function. The function will periodically check and create a CloudTrail trail under the organization is incorrect. While this option seems to automate the process of enabling CloudTrail, it is overly complex and potentially costly because it requires custom coding and continuous monitoring. It might not catch all new accounts immediately upon creation, depending on the periodic check interval.

The option that says: Configure a CloudTrail trail in each business unit’s AWS account manually when a new account is added and apply an SCP to enforce the logging is incorrect. This method is manual, error-prone, and inefficient. Relying on manual processes for each new account increases the risk of human error and inconsistencies in configuration. While using a Service Control Policy (SCP) to enforce logging is a good practice, it does not automate the creation of CloudTrail trails.

The option that says: Create a custom script running on an Amazon EC2 instance that periodically checks for new AWS accounts and configures CloudTrail trails in each is incorrect. Similar to the previous option, this approach involves custom scripting and maintaining an EC2 instance, leading to additional complexity and costs. It also does not guarantee immediate configuration of CloudTrail upon account creation, and continuous operation of an EC2 instance may be less efficient compared to using native AWS services.

 

References:

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html

https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html

 

Check out these AWS Organizations and AWS CloudTrail Cheat Sheets:

https://tutorialsdojo.com/aws-organizations/

https://tutorialsdojo.com/aws-cloudtrail/

---

## Câu 42 — ❌ SAI

### Câu hỏi

An e-commerce company runs its website on Amazon EC2 instances. Each of the two AWS Regions has its own set of instances managed by an Application Load Balancer (ALB). The company wants to ensure that customers are served by the closest region for the fastest response times. Customers should be served from the other Region if the website becomes unavailable in the closest Region.

Which of the following solutions should be implemented?

### Các phương án

- **A.** Create geolocation-based routing records in Amazon Route 53 to direct users to the nearest ALB and rely on periodic Amazon Route 53 health checks to remove an ALB from service during outages. 👈 *(bạn chọn)*
- **B.** Configure an Amazon Route 53 health check for each Region and use a Route 53 failover routing record with Evaluate Target Health enabled to switch traffic only when the primary Region becomes unhealthy.
- **C.** Use Amazon API Gateway in front of both ALBs and configure a regional endpoint to redirect users to the nearest Region.
- **D.** Configure Amazon Route 53 health checks for each ALB and create a Route 53 latency alias record with Evaluate Target Health enabled to route traffic to the closest healthy Region. ✅

> **Bạn chọn:** A  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon Route 53 health checks monitor the health of your resources, such as web servers and email servers. You can specify values that define how you want the health check to work, such as the IP address or domain name of the endpoint that you want Route 53 to monitor, the protocol that you want Amazon Route 53 to use to perform the check, how often you want Route 53 to send a request to the endpoint, and how many consecutive times the endpoint must fail to respond to requests before Route 53 considers it unhealthy. If a health check determines that the underlying resource is unhealthy, Route 53 routes traffic from the associated record. This ensures high availability and failover support for DNS records.

Latency-based routing in Amazon Route 53 allows you to improve performance for your users by serving their requests from the AWS Region that provides the lowest latency. When Route 53 receives a DNS query for your domain or subdomain, it determines which AWS Regions you’ve created latency records for, determines which Region gives the user the lowest latency, and then selects a latency record for that Region. Route 53 responds with the value from the selected record, such as the IP address for a web server. This ensures customers are served by the region closest to them for the fastest response times.

If you enabled the Evaluate Target Health, this causes Route 53 to determine whether there are any healthy resources in a region before trying to route traffic there. If not, Route 53 chooses a healthy resource in the other region.

Hence, the correct answer is: Configure Amazon Route 53 health checks for each ALB and create a Route 53 latency alias record with Evaluate Target Health enabled to route traffic to the closest healthy Region. Latency-based routing ensures customers are directed to the Region with the lowest latency, while health checks with Evaluate Target Health provide automatic failover to the other Region if the closest one becomes unhealthy.

The option that says: Create geolocation-based routing records in Amazon Route 53 to direct users to the nearest ALB and rely on periodic Amazon Route 53 health checks to remove an ALB from service during outages is incorrect because geolocation routing in Route 53 primarily directs traffic based on the user’s IP location mapping to a geographic region, not on actual network latency. This means a customer might be routed to a Region that is geographically closest, but not necessarily the one with the lowest latency.

The option that says: Use Amazon API Gateway in front of both ALBs and configure a regional endpoint to redirect users to the nearest Region is incorrect because API Gateway does not have built-in functionality to route users to the nearest Region. It can expose endpoints regionally, but DNS-based latency routing is still required. This solution does not meet the requirement for automatic latency-based routing and failover.

The option that says: Configure an Amazon Route 53 health check for each Region and use a Route 53 failover routing record with Evaluate Target Health enabled to switch traffic only when the primary Region becomes unhealthy is incorrect because failover routing only supports primary/secondary configurations. It does not consider latency, so customers would always be directed to the primary Region regardless of proximity, which fails the requirement for fastest response times.

 

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html

 

Check out this Amazon Route 53 Cheat Sheet:

https://tutorialsdojo.com/amazon-route-53/

---

## Câu 43 — ✅ ĐÚNG

### Câu hỏi

A digital services provider manages many AWS accounts via AWS Organizations. The company’s policy mandates that only personnel in supervisory roles can execute IAM actions across all AWS accounts. The cloud management team wants to enforce this policy while ensuring that non-supervisory roles are restricted from executing IAM actions.

What would be the most effective approach to implement this policy with minimal administrative effort?

### Các phương án

- **A.** Use AWS Identity and Access Management (IAM) to create a single IAM role with the necessary permissions and assign this role to all supervisory personnel across all AWS accounts.
- **B.** Use IAM permissions boundaries to restrict IAM actions to supervisory roles.
- **C.** Implement AWS Service Control Policies (SCPs) at the root Organizational Unit (OU) level that deny all non-supervisory roles from executing IAM actions. ✅ 👈 *(bạn chọn)*
- **D.** Assign AWS Service Control Policies (SCPs) directly to individual IAM users in each AWS account.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Service Control Policies (SCPs) are a type of policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization, allowing you to ensure your accounts stay within your organization’s access control guidelines. By applying the SCP at the root OU level, it ensures that the policy is enforced across all accounts in the organization, which aligns with the company’s policy.

You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies account management. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization and OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another.

Hence, the correct answer is: Implement AWS Service Control Policies (SCPs) at the root Organizational Unit (OU) level that deny all non-supervisory roles from executing IAM actions.

The option that says: Use IAM permissions boundaries to restrict IAM actions to supervisory roles is incorrect because IAM permissions boundaries are only used to delegate permissions management to other users, but they do not inherently restrict IAM actions to specific roles.

The option that says: Assign AWS Service Control Policies (SCPs) directly to individual IAM users in each AWS account is incorrect because SCPs cannot be assigned directly to individual users. SCPs are simply designed to be applied at the organizational level, not at the user level, making this option technically invalid.

The option that says: Use AWS Identity and Access Management (IAM) to create a single IAM role with the necessary permissions and assign this role to all supervisory personnel across all AWS accounts is incorrect because while this could grant the necessary permissions to supervisory personnel, it does not inherently restrict all other non-supervisory roles from executing IAM actions. Therefore, this would not ensure that only supervisory roles can execute IAM actions.

 

References:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html

Check this Service Control Policies (SCP) vs IAM Policies Cheat Sheet:

https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

---

## Câu 44 — ✅ ĐÚNG

### Câu hỏi

A global corporation manages numerous operation groups, each with unique IT requirements. The corporation uses AWS Organizations to assign individual groups to their respective Organizational Units (OUs). Each OU contains thousands of AWS accounts. A solutions architect is tasked with designing a solution that allows each OU to view and analyze a detailed breakdown of AWS usage and costs for its member accounts.

Which set of actions will satisfy the requirements?

### Các phương án

- **A.** Use AWS Trusted Advisor in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard.
- **B.** Create an AWS Cost and Usage Report (CUR) in the management account. Store the CUR in a central Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard. ✅ 👈 *(bạn chọn)*
- **C.** Create a Lambda function in the management account. Configure the function to create an AWS Cost and Usage Report (CUR) in the member's account. Schedule the function using Amazon EventBridge.Store the CUR in a central Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard.
- **D.** Use AWS Systems Manager OpsCenter in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard.

> **Bạn chọn:** B  
> **Đáp án đúng:** B  
> **Kết quả:** ✅ Đúng

### Giải thích

The AWS Cost and Usage Reports (AWS CUR) contains the most comprehensive set of cost and usage data available. You can use Cost and Usage Reports to publish your AWS billing reports to an Amazon Simple Storage Service (Amazon S3) bucket that you own. You can receive reports that break down your costs by the hour, day, or month, by product or product resource, or by tags that you define yourself. AWS updates the report in your bucket once a day in comma-separated value (CSV) format. You can view the reports using spreadsheet software such as Microsoft Excel or Apache OpenOffice Calc, or access them from an application using the Amazon S3 API.

The CUR tracks your AWS usage and provides estimated charges associated with your account. Each report contains line items for each unique combination of AWS products, usage type, and operations that you use in your AWS account. You can customize the AWS Cost and Usage Reports to aggregate the information either by hour, day, or month.

In the scenario, by generating a single CUR in the management account, the corporation can effectively simplify the process and ensure complete coverage of cost and usage data across all member accounts, thereby providing each OU with the ability to analyze their respective AWS usage and costs.

Hence, the correct answer is: Create an AWS Cost and Usage Report (CUR) in the management account. Store the CUR in a central Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard.

The option that says: Use AWS Systems Manager OpsCenter in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard is incorrect because AWS Systems Manager OpsCenter is primarily used for managing and resolving operational issues, not for generating CURs.

The option that says: Use AWS Trusted Advisor in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard is incorrect. AWS Trusted Advisor is simply a service that gives guidance in provisioning resources that follows AWS best practices. It’s not capable of generating CURs.

The option that says: Create a Lambda function in the management account. Configure the function to create an AWS Cost and Usage Report (CUR) in the member’s account. Schedule the function using Amazon EventBridge. Store the CUR in a central Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard is incorrect. This approach is unnecessarily complicated when you can generate a single CUR in the management account for all member accounts. Furthermore, Amazon QuickSight provides better visualization options for cost and usage data than a custom CloudWatch Dashboard. CloudWatch Dashboards might technically be feasible for simple visualizations, but they won’t offer the same level of detail, insight, and interactive analysis capability that Amazon QuickSight can.

 

References:

https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html

https://aws.amazon.com/blogs/enterprise-strategy/the-aws-cost-usage-report-the-next-step-on-your-cost-management-journey/

https://repost.aws/knowledge-center/quicksight-cost-usage-report

 

Check out this AWS Billing and Cost Management Cheat Sheet:

https://tutorialsdojo.com/aws-billing-and-cost-management/

---

## Câu 45 — ✅ ĐÚNG

### Câu hỏi

A Solutions Architect is configuring a multi-account AWS environment using AWS CloudFormation. The setup requires deploying an IAM role in the primary account (Account A), which should be assumed by an EC2 instance in a secondary account (Account B). The EC2 instance uses an instance profile that incorporates the necessary IAM role.

After deploying the CloudFormation template in Account A, the EC2 instance in Account B encounters permissions issues when attempting to assume the specified IAM role.

The Solutions Architect needs to ensure the EC2 instance in Account B can successfully assume the role created in Account A.

Which actions should the Solutions Architect take?

### Các phương án

- **A.** In the CloudFormation template, include both 'CAPABILITY_IAM' and 'CAPABILITY_NAMED_IAM' capabilities.
- **B.** In Account A, update the trust policy of the IAM role to include the ARN of the IAM role associated with the EC2 instance in Account B to allow the AssumeRole action. ✅ 👈 *(bạn chọn)*
- **C.** In Account A, modify the trust policy of the IAM role to allow the AssumeRole action from Account B’s root principal.
- **D.** In Account B, update the trust policy of the IAM role to include the primary Account A as a trusted entity and specify the EC2 instance as the principal.

> **Bạn chọn:** B  
> **Đáp án đúng:** B  
> **Kết quả:** ✅ Đúng

### Giải thích

IAM Roles and Cross-Account Access: An IAM role is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumed by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.

You can use IAM Roles to delegate access to users, applications, or services that don’t normally have access to your AWS resources. For example, you might want to grant users in your AWS account access to resources they don’t usually have or grant users in one AWS account access to resources in another account.

An instance profile is a container that passes an AWS Identity and Access Management (IAM) role to an Amazon Elastic Compute Cloud (EC2) instance. It is used to securely provide temporary AWS credentials to the EC2 instance, allowing it to access other AWS services.

The issue in the given scenario is that the EC2 instance in Account B is unable to assume the IAM role in Account A due to insufficient permissions. This problem can be resolved by modifying the trust policy of the IAM role in Account A to grant the necessary permissions to Account B.

A trust policy is associated with an IAM role, which defines the principals (accounts, users, or services) that can assume the role. By default, a newly created role does not have any trust policy statements, which means that no principal can assume the role.

By adding the ARN of the IAM role associated with the EC2 instance in Account B as a trusted entity in the trust policy of the IAM role in Account A, the EC2 instance will be able to assume the role successfully.

Hence, the correct answer is: In Account A, update the trust policy of the IAM role to include the ARN of the IAM role associated with the EC2 instance in Account B to allow the AssumeRole action.

The option that says: In Account B, update the trust policy of the IAM role to include the primary Account A as a trusted entity and specify the EC2 instance as the principal is incorrect because the trust policy of an IAM role is managed in the account where the role is created, not in the account that assumes the role. In this case, the IAM role is created in Account A, so the trust policy should be updated in Account A, not in Account B.

The option that says: In Account A, modify the trust policy of the IAM role to allow the AssumeRole action from Account B’s root principal is incorrect because allowing the AssumeRole action from Account B’s root principal would allow any identities in Account B to assume the IAM role in Account A. Such strategy does not follow the principle of least privilege. It’s better to grant permissions to specific IAM roles or users.

The option that says: In the CloudFormation template, include both ‘CAPABILITY_IAM’ and ‘CAPABILITY_NAMED_IAM’ capabilities is incorrect. While these capabilities are required when creating or updating IAM resources using CloudFormation, they do not directly address the issue of cross-account role assumption. Including these capabilities ensures that the CloudFormation deployment succeeds, but it does not resolve the permissions issues encountered when the EC2 instance in Account B attempts to assume the role in Account A.

References:

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html

Check out this AWS IAM Cheat Sheet:

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

---

## Câu 46 — ✅ ĐÚNG

### Câu hỏi

A company has several legacy virtual machines running on VMware infrastructure in its on-premises data center. There is also a storage server with SMB shares that is used as a central logging and backup destination. The company wants to migrate its production workload to Amazon EC2 instances. For this migration, the solutions architect has been tasked to preserve the software and configuration settings of the servers.

Which of the following options should the solutions architect implement to meet the company requirements?

### Các phương án

- **A.** Install the AWS Systems Manager agent on all on-premises servers. Utilize AWS SSM to create a managed-instance activation for hybrid environment and register all the virtual machines in Systems Manager. Configure AWS Backup to create an AMI backup of all the registered instances. Launch Amazon EC2 instances based on the created AMIs.
- **B.** Export all the virtual machines using the VMware vSphere client and save the images as Open Virtualization Format (OVF). Upload the VM images to an Amazon S3 bucket on the destination region. Create an IAM role that has permissions to use VM Import/Export. Use AWS CLI to import the VM images and launch them as EC2 instances.
- **C.** Create an Amazon FSx for Windows File Server. Set up the AWS DataSync agent in the on-premises data center to start replication to AWS. Create VM images and upload them to an Amazon S3 bucket in the destination region. Use AWS VM Import/Export to import the images and launch them as EC2 instances. ✅ 👈 *(bạn chọn)*
- **D.** Create an AWS Storage Gateway – File Gateway and configure a Common Internet File System (CIFS). Sync the SMB server files to this share. Create a snapshot of the virtual machines in VMware and copy them to the File Gateway. On the AWS Management Console, launch EC2 instances and select the snapshots as the AMI.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS Storage services, as well as between AWS Storage services. DataSync can copy data between Network File System (NFS) shares, Server Message Block (SMB) shares, self-managed object storage, AWS Snowcone, Amazon Simple Storage Service (Amazon S3) buckets, Amazon Elastic File System (Amazon EFS) file systems, and Amazon FSx for Windows File Server file systems.

These are some of the main use cases for AWS DataSync:

Data migration – Move active datasets rapidly over the network into Amazon S3, Amazon EFS, or FSx for Windows File Server.

Archiving cold data – Move cold data stored in on-premises storage directly to durable and secure long-term storage such as Amazon S3 Glacier or S3 Glacier Deep Archive.

Data protection – Move data into any Amazon S3 storage class, choosing the most cost-effective storage class for your needs.

Data movement for timely in-cloud processing – Move data into or out of AWS for processing when working with systems that generate data on-premises. This approach can speed up critical hybrid cloud workflows across many industries.

VM Import/Export enables you to import virtual machine (VM) images from your existing virtualization environment to Amazon EC2 and then export them back. This enables you to migrate applications and workloads to Amazon EC2, copy your VM image catalog to Amazon EC2, or create a repository of VM images for backup and disaster recovery.

Therefore, the correct answer is: Create an Amazon FSx for Windows File Server. Set up the AWS DataSync agent in the on-premises data center to start replication to AWS. Create VM images and upload them to an Amazon S3 bucket in the destination region. Use AWS VM Import/Export to import the images and launch them as EC2 instances. 

The option that says: Create an AWS Storage Gateway – File Gateway and configure a Common Internet File System (CIFS). Sync the SMB server files to this share. Create a snapshot of the virtual machines in VMware and copy them to the File Gateway. On the AWS Management Console, launch EC2 instances and select the snapshots as the AMI is incorrect. This may be possible; however, it is unnecessary to create a File Gateway on your on-premises data center if you want to sync an SMB to the AWS cloud. AWS DataSync offers a managed service that is designed for copying data from SMB shares to AWS.

The option that says: Export all the virtual machines using the VMware vSphere client and save the images as Open Virtualization Format (OVF). Upload the VM images to an Amazon S3 bucket on the destination region. Create an IAM role that has permissions to use VM Import/Export. Use AWS CLI to import the VM images and launch them as EC2 instances is incorrect. This may be possible; however, there is no mention of how to migrate the SMB share data. The data inside the SMB share can change while doing any snapshot so it is better to use AWS DataSync for the migration.

The option that says: Install the AWS Systems Manager agent on all on-premises servers. Utilize AWS SSM to create a managed-instance activation for hybrid environment and register all the virtual machines in Systems Manager. Configure AWS Backup to create an AMI backup of all the registered instances. Launch Amazon EC2 instances based on the created AMIs is incorrect. AWS Backup only supports backing up AWS services. It cannot create AMIs from on-premises virtual machines.

 

References:

https://aws.amazon.com/datasync/

https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

https://docs.aws.amazon.com/vm-import/latest/userguide/what-is-vmimport.html

 

Check out the AWS DataSync and Cheat Sheet:

https://tutorialsdojo.com/aws-datasync/

---

## Câu 47 — ✅ ĐÚNG

### Câu hỏi

A large company runs its mission-critical Microsoft SQL Server Always On cluster on its on-premises data center servers. The management is planning to migrate its core applications, including the database servers, to the AWS cloud. The management specifically requested to use AWS managed services whenever possible to save on operational overhead costs. The Solutions Architect must create a heterogeneous database migration strategy to AWS.

Which of the following options is the recommended solution that will meet the above requirements?

### Các phương án

- **A.** Utilize the native SQL Server backup utility to create a copy of the current database. Upload the created backup file to an Amazon S3 bucket. Create a new Amazon RDS for MySQL instance. Use AWS Glue to load S3 data into the RDS MySQL Table.
- **B.** Create a backup copy of the on-premises SQL Server. Use AWS DataSync to transfer the backup files directly to an Amazon S3 bucket. Create an Amazon RDS for MySQL instance. Use the SQL Server BULK INSERT feature to load data from the S3 bucket to the RDS instance.
- **C.** Install the AWS Schema Conversion Tool on the on-premises data center to convert the database schema from Microsoft SQL Server to MySQL. Create an Amazon RDS for MySQL instance. Migrate the on-premises database to the RDS instance using AWS Database Migration Service (AWS DMS). ✅ 👈 *(bạn chọn)*
- **D.** Establish a secure VPN connection from the on-premises network to Amazon VPC. Create a new Amazon RDS for MySQL instance. Use the AWS DataSync service to replicate the SQL server database to AWS. Promote the RDS instance as a master database once replication is completed.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

You can use the AWS Schema Conversion Tool (AWS SCT) to convert your existing database schema from one database engine to another. You can convert relational OLTP schema or data warehouse schema. Your converted schema is suitable for an Amazon Relational Database Service (Amazon RDS), MySQL, MariaDB, Oracle, SQL Server, PostgreSQL DB, an Amazon Aurora DB cluster, or an Amazon Redshift cluster. The converted schema can also be used with a database on an Amazon EC2 instance or stored as data on an Amazon S3 bucket.

AWS Database Migration Service (AWS DMS) is a cloud service that makes it easy to migrate relational databases, data warehouses, NoSQL databases, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud or between combinations of cloud and on-premises setups.

With AWS DMS, you can perform one-time migrations, and you can replicate ongoing changes to keep sources and targets in sync. If you want to migrate to a different database engine, you can use the AWS Schema Conversion Tool (AWS SCT) to translate your database schema to the new platform. You then use AWS DMS to migrate the data. Because AWS DMS is a part of the AWS Cloud, you get the cost efficiency, speed to market, security, and flexibility that AWS services offer. At a basic level, AWS DMS is a server in the AWS Cloud that runs replication software. You create a source and target connection to tell AWS DMS where to extract from and load into.

Therefore, the correct answer is: Install the AWS Schema Conversion Tool on the on-premises data center to convert the database schema from Microsoft SQL Server to MySQL. Create an Amazon RDS for MySQL instance. Migrate the on-premises database to the RDS instance using AWS Database Migration Service (AWS DMS). The AWS SCT can convert the database schema to MySQL, and the AWS DMS can be used to easily migrate the converted database to an RDS MySQL instance.

The option that says: Utilize the native SQL Server backup utility to create a copy of the current database. Upload the created backup file to an Amazon S3 bucket. Create a new Amazon RDS for MySQL instance. Use AWS Glue to load S3 data into the RDS MySQL Table is incorrect because AWS Glue is primarily designed for ETL (Extract, Transform, Load) jobs, which are better suited for data transformation rather than direct migration of SQL Server backups to an RDS MySQL database.

The option that says: Create a backup copy of the on-premises SQL Server. Use AWS DataSync to transfer the backup files directly to an Amazon S3 bucket. Create an Amazon RDS for MySQL instance. Use the SQL Server BULK INSERT feature to load data from the S3 bucket to the RDS instance is incorrect because DataSync is typically intended for file transfer and not database migration. The BULK INSERT feature only supports loading data from an S3 bucket to a SQL server instance, not an RDS MySQL instance.

The option that says: Establish a secure VPN connection from the on-premises network to Amazon VPC. Create a new Amazon RDS for MySQL instance. Use the AWS DataSync service to replicate the SQL server database to AWS. Promote the RDS instance as a master database once replication is completed is incorrect. AWS DataSync can facilitate the copying of data from on-premises data stores to the AWS cloud, but it can’t be used to replicate an on-premises database to AWS.

 

References:

https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html

https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.HighLevelView.html

 

Check out this AWS Database Migration Service Cheat Sheet:

https://tutorialsdojo.com/aws-database-migration-service/

---

## Câu 48 — ❌ SAI

### Câu hỏi

A retail company is using Amazon OpenSearch Service to analyze its sales and inventory data. Every week, new data from an Amazon S3 Standard bucket is indexed and loaded into a 20-data node Amazon OpenSearch cluster. Read-only queries are performed on this data to monitor recent trends. After 1 week, it’s occasionally accessed for identifying long-term patterns. After three months, the index containing the older data is deleted from the system. However, due to audit requirements, the company needs to keep a complete copy of all processed data.

The company is looking for strategies to reduce storage costs without abandoning Amazon OpenSearch. A slower query response time on infrequently accessed data is acceptable as long as it can be retrieved on demand.

Which solution fits the requirements while being the MOST cost-effective?

### Các phương án

- **A.** Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Infrequently Access tier. 👈 *(bạn chọn)*
- **B.** Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive. ✅
- **C.** Reconfigure the OpenSearch cluster by replacing all data nodes with a mix of UltraWarm nodes and cold storage nodes. Use the UltraWarm node for indexing and the cold storage for reading. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive.
- **D.** Upsize the OpenSearch cluster by adding UltraWarm nodes to improve read performance. Use an S3 lifecycle policy to delete data older than 3 months.

> **Bạn chọn:** A  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon OpenSearch Service offers three storage tiers:

-Hot – provides the fastest possible performance for indexing and searching new data. Standard data nodes use hot storage, which takes the form of instance store or Amazon EBS volumes attached to each node.

-UltraWarm – uses Amazon S3 with related caching solutions to improve performance. UltraWarm offers significantly lower costs per GiB for read-only data that you query less frequently and don’t need the same performance as hot storage. Data stored in UltraWarm is immutable.

-Cold – optimized to store infrequently accessed or historical data at a cheaper price per GB per month. When you use cold storage, you detach your indexes from the UltraWarm tier, making them inaccessible. You can reattach these indexes when you need to query that data.

In the scenario, since the company is primarily performing read-only queries and the data is less frequently accessed after 1 week, it would benefit from reducing the number of data nodes and adding more cost-effective UltraWarm storage. Using Index State Management (ISM) policies to transition data to cold storage after 1 week would ensure efficient use of resources. Moreover, transitioning data older than 3 months to the S3 Glacier Deep Archive meets the company’s requirements to keep a complete copy of all processed data for audit purposes. Amazon S3 Glacier Deep Archive is a secure, durable, and extremely low-cost Amazon S3 cloud storage class, designed for the long-term retention of data that is accessed once or twice a year.

Therefore, the correct answer is: Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive.

The option that says: Upsize the OpenSearch cluster by adding UltraWarm nodes to improve read performance. Use an S3 lifecycle policy to delete data older than 3 months is incorrect. This option is not cost-effective as it would increase the infrastructure costs without necessarily bringing significant benefits, as the company is okay with slower query response times for infrequently accessed data. Moreover, it only uses an S3 lifecycle policy to delete data older than 3 months, which does not fulfill the company’s requirement to keep a complete copy of all processed data for auditing purposes.

The option says: Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Infrequently Access tier is incorrect. Although the S3 IA tier costs less than Standard S3, it is more expensive than the S3 Glacier Deep Archive. Considering the company’s requirement to store data for at least three months and only occasionally access it, the Glacier Deep Archive would be a more cost-effective choice.

The option that says: Reconfigure the OpenSearch cluster by replacing all data nodes with a mix of UltraWarm nodes and cold storage nodes. Use the UltraWarm node for indexing and the cold storage for reading. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive is incorrect. This approach is not valid because UltraWarm nodes are designed to work on read-only data.

 

References:

https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html

https://aws.amazon.com/blogs/big-data/choose-the-right-storage-tier-for-your-needs-in-amazon-opensearch-service/

 

Check out this Amazon OpenSearch Cheat Sheet:

https://tutorialsdojo.com/amazon-opensearch-service/

---

## Câu 49 — ❌ SAI

### Câu hỏi

A financial services company is migrating 18 internal business applications to AWS as part of a data center consolidation project. The applications include Spring Boot Java and Node.js services that currently run across several virtual machine clusters.

The majority of the applications are used only during weekly financial reconciliation and quarter-end reporting, with minimal usage outside those periods. Most services require less than 1 GiB of memory, but a few Java-based applications can temporarily require up to 3 GiB of memory while generating large reports. One Java application produces regulatory compliance reports by aggregating data from multiple databases and typically runs for 2 to 4 hours. The company wants to minimize infrastructure costs, standardize deployment across all applications, and automatically adjust compute capacity based on demand.

Which solution will meet these requirements in the MOST cost-effective way?

### Các phương án

- **A.** Deploy all applications on Amazon EC2 instances behind Application Load Balancers. Use EC2 Auto Scaling with an Auto Scaling group, and purchase Reserved Instance capacity matching the maximum capacity defined by the Auto Scaling group’s GroupMaxSize parameter. 👈 *(bạn chọn)*
- **B.** Containerize each application and deploy it as an Amazon ECS task on an Amazon EC2 cluster. Configure EC2 Auto Scaling to scale cluster capacity based on memory utilization and monitor workloads by using Amazon CloudWatch. ✅
- **C.** Deploy the Java applications on Amazon EC2 instances and the Node.js applications on AWS App Runner to optimize each runtime separately. Use separate deployment pipelines for each platform.
- **D.** Containerize each application and deploy it to AWS Lambda as container images. Configure provisioned concurrency for all functions to reduce startup latency during reporting periods.

> **Bạn chọn:** A  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon ECS (Elastic Container Service) can manage the scaling of Amazon EC2 (Elastic Compute Cloud) instances that are registered to your cluster, a feature known as Amazon ECS cluster auto-scaling. To enable managed scaling, you activate it when creating the Amazon ECS Auto Scaling group capacity provider. After that, you set a target percentage (the targetCapacity) for instance utilization within this Auto Scaling group. Amazon ECS generates two custom CloudWatch metrics and establishes a target tracking scaling policy for your Auto Scaling group. This allows Amazon ECS to automatically manage the scale-in and scale-out actions based on the resource utilization of your tasks.

When using Amazon EC2 instances for your capacity, Auto Scaling groups help in managing the EC2 instances registered to your clusters. Auto Scaling ensures you have the appropriate number of Amazon EC2 instances available to handle your application load effectively.

You have the option to use the managed scaling feature to allow Amazon ECS to manage the scale-in and scale-out actions of the Auto Scaling group, or you can choose to handle the scaling actions manually.

A task definition serves as a blueprint for your application. It is a text file in JSON format that outlines the parameters and configurations for one or more containers that make up your application.

You can monitor your Amazon ECS resources through Amazon CloudWatch, which collects and processes raw data from Amazon ECS into readable, near-real-time metrics. These statistics are recorded for two weeks, enabling you to access historical information and gain better insights into the performance of your clusters or services. Amazon ECS metric data is automatically sent to CloudWatch at one-minute intervals.

Hence, the correct answer is: Containerize each application and deploy it as an Amazon ECS task on an Amazon EC2 cluster. Configure EC2 Auto Scaling to scale cluster capacity based on memory utilization and monitor workloads by using Amazon CloudWatch. Containerization standardizes deployment across all applications, Auto Scaling ensures compute capacity adjusts automatically to demand, and EC2 scaling based on memory utilization minimizes costs by scaling down during idle periods while still supporting applications that temporarily need more memory.

The option that says: Deploy the Java applications on Amazon EC2 instances and the Node.js applications on AWS App Runner to optimize each runtime separately. Use separate deployment pipelines for each platform is incorrect because it introduces operational complexity by splitting runtimes and pipelines. This prevents standardized deployment across all applications and increases management overhead, which goes against the requirement to minimize costs and streamline operations.

The option that says: Containerize each application and deploy it to AWS Lambda as container images. Configure provisioned concurrency for all functions to reduce startup latency during reporting periods is incorrect because although AWS Lambda primarily supports container images and can handle workloads up to 10 GiB of memory, it is not well‑suited for long‑running applications like the Java compliance report that runs for 2–4 hours. Lambda has a maximum execution time of 15 minutes per invocation, which makes it incompatible with multi‑hour reporting jobs. Additionally, configuring provisioned concurrency for all functions would keep capacity allocated even during idle periods, increasing costs unnecessarily. This contradicts the requirement to minimize infrastructure costs while supporting variable workloads.

The option that says: Deploy all applications on Amazon EC2 instances behind Application Load Balancers. Use EC2 Auto Scaling with an Auto Scaling group, and purchase Reserved Instance capacity matching the maximum capacity defined by the Auto Scaling group’s GroupMaxSize parameter is incorrect because purchasing Reserved Instances for maximum capacity typically locks in costs even when workloads are idle. This eliminates the cost savings from scaling down and leads to overprovisioning, making it the least cost‑effective choice.

 

References:

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-auto-scaling.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html

 

Check out this Amazon Elastic Container Service Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

---

## Câu 50 — ✅ ĐÚNG

### Câu hỏi

A healthcare research institute is building a machine learning model for predicting disease outbreaks. A fleet of small Amazon EC2 instances fetches URLs of health-related articles and research papers from an Amazon SQS queue using a web-crawling process. After fetching the articles and research papers from the provided URLs, the instances analyze the documents, extract features, and store the results as .json files in an Amazon EFS volume, which is accessible to all instances within the fleet.

An automated system feeds the URLs of the health-related articles and research papers into the SQS queue based on real-time updates from various health organizations. Each instance processes the data within 5 minutes. However, there are periods when the instances are idle due to low volumes of health updates. A cloud engineer is tasked to restructure the system to reduce operational costs.

What actions should the cloud engineer take to ensure the most cost-effective solution? (Select TWO.)

### Các phương án

- **A.** Use Amazon Neptune to store the .json files instead of Amazon EFS.
- **B.** Replace the EC2 instances with AWS Lambda functions to fetch and process data from the SQS queue. ✅ 👈 *(bạn chọn)*
- **C.** Use Amazon S3 to store the .json files instead of Amazon EFS. ✅ 👈 *(bạn chọn)*
- **D.** Employ Amazon EC2 Spot Instances for executing the web-crawling process.
- **E.** Use Amazon RDS to store the .json files instead of Amazon EFS.

> **Bạn chọn:** B, C  
> **Đáp án đúng:** B, C  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Lambda is a serverless compute service that lets you run your code without provisioning or managing servers. It automatically scales your application in response to the volume of incoming messages in the SQS queue. This would be more cost-effective during periods of low health update volumes.

Amazon S3 offers an easy-to-use web services interface for storing and accessing large amounts of data from anywhere on the internet at any time. It provides developers with access to Amazon’s highly scalable, reliable, and cost-effective data storage infrastructure, which powers its global network of websites. The service is designed to leverage the advantages of scale and make them available to developers.

Hence, the correct answers are:

– Replace the EC2 instances with AWS Lambda functions to fetch and process data from the SQS queue.

– Use Amazon S3 to store the .json files instead of Amazon EFS.

The option that says: Employ Amazon EC2 Spot Instances for executing the web-crawling process is incorrect because Spot Instances are subject to availability in the Spot pool and can be interrupted with two minutes of notification when EC2 needs the capacity back. This could disrupt the real-time updates needed for the system.

The option that says: Use Amazon Neptune to store the .json files instead of Amazon EFS is incorrect because Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. It’s not designed for storing .json files.

The option that says: Use Amazon RDS to store the .json files instead of Amazon EFS is incorrect because Amazon RDS is a relational database service and is not suitable for storing .json files. It would also likely be more expensive than using EFS or S3.

References:

https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html

https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html

 

Check out these AWS Lambda and Amazon S3 Cheat Sheets:

https://tutorialsdojo.com/aws-lambda/

https://tutorialsdojo.com/amazon-s3/

---

## Câu 51 — ❌ SAI

### Câu hỏi

A company hosts its core business applications on a fleet of Linux-based Amazon EC2 instances managed in AWS Systems Manager Fleet Manager. One day, an employee who maintained these instances abruptly resigned. The company is concerned that the employee who left might still possess a copy of the key pairs used to SSH to these instances, as this raises a security risk.
Which of the following options should the Solutions Architect implement to rotate the SSH keys successfully?

### Các phương án

- **A.** Generate a new key pair in the EC2 Console. Extract the public key from the newly created key pair and write a shell script that will update the authorized_keys in the .ssh directory with the new public key. Utilize AWS Systems Manager Run Command and choose the AWS-RunShellScript document to execute the shell script on these EC2 instances. ✅
- **B.** Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances.
- **C.** Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Run Command and choose AWS-RunShellScript document to execute the shell script on these EC2 instances. 👈 *(bạn chọn)*
- **D.** Manually generate a new key pair and write a shell script that will update the authorized_keys in the .ssh directory based on the new public key value. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances.

> **Bạn chọn:** C  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

A key pair, consisting of a public key and a private key, is a set of security credentials that you use to prove your identity when connecting to an Amazon EC2 instance. Amazon EC2 stores the public key on your instance, and you store the private key. For Linux instances, the private key allows you to securely SSH into your instance.

AWS Systems Manager has an extensive collection of features and capabilities to manage your AWS and hybrid systems. This service allows you to centralize operational data from various AWS services and automate manual tasks on both your on-premises and AWS resources. One of its capabilities is the AWS Run Command, which can be used to remotely and securely manage the configuration of your managed nodes.

A managed node is any Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, or on-premises server or virtual machine (VM) in your hybrid environment that has been configured for Systems Manager. Run Command allows you to automate common administrative tasks and perform one-time configuration changes at scale. You can use Run Command from the AWS Management Console, the AWS Command Line Interface (AWS CLI), AWS Tools for Windows PowerShell, or the AWS SDKs. Run Command is offered at no additional cost.

AWS Run Command has a document called AWS-RunShellScript that can be used to run Linux shell scripts or specify the path to a script to run.

Therefore, the correct answer is: Generate a new key pair in the EC2 Console. Extract the public key from the newly created key pair and write a shell script that will update the authorized_keys in the .ssh directory with the new public key. Utilize AWS Systems Manager Run Command and choose the AWS-RunShellScript document to execute the shell script on these EC2 instances.

The option that says: Manually generate a new key pair and write a shell script that will update the authorized_keys in the .ssh directory based on the new public key value. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances is incorrect because the AWS-RunShellScript document can’t be used in SSM Automation runbooks.

The option that says: Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Run Command and choose AWS-RunShellScript document to execute the shell script on these EC2 instances is incorrect because the downloaded pem key from the EC2 Console is just a private key. When your instance boots for the first time, the public key is placed on the Linux instance in an entry within ~/.ssh/authorized_keys, not the private key.

The option that says: Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances is incorrect because the downloaded pem key from the EC2 Console is only a private key. When your instance boots for the first time, the public key is placed on the Linux instance in an entry within ~/.ssh/authorized_keys, not the private key. Also, the AWS-RunShellScript document can’t be used in SSM Automation runbooks.

 

References:

https://aws.amazon.com/systems-manager/

https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-plugins.html

 

Check out these AWS Systems Manager Cheat Sheets:

https://tutorialsdojo.com/aws-systems-manager/

---

## Câu 52 — ✅ ĐÚNG

### Câu hỏi

A company has a suite of services hosted on its on-premises data center. These services run on a network of virtualized Ubuntu and Windows servers. To benefit from AWS’ scaling capabilities, the company decides to migrate its entire system to AWS.

The migration strategy aims to precisely understand the actual usage and deeply analyze application components and the dependencies within its on-premises workload. The company also wants to right-size its Amazon EC2 instances to avoid unnecessary expenses for underutilized resources.

Which set of actions will meet the requirements?

### Các phương án

- **A.** Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves, and use AWS Transform migration assessments to generate EC2 right-sizing and cost recommendations. ✅ 👈 *(bạn chọn)*
- **B.** Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves. After the workloads are migrated to EC2, use AWS Compute Optimizer to generate EC2 right-sizing recommendations.
- **C.** Install the AWS Systems Manager Agent on both the physical servers and Virtual machines to perform an application-level assessment. Utilize Systems Manager Application Manager to logically separate servers into different applications. Input server size data into the AWS Pricing calculator and adhere to its recommendations.
- **D.** Use AWS Transform MGN to install replication agents on the source servers and immediately start continuous block-level replication to AWS. After the servers are launched on EC2, use AWS Compute Optimizer to recommend instance sizes.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Transform is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.

With AWS Transform, you can:

– Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS

– Migrate VMware workloads to Amazon EC2

– Modernize .NET applications to Linux-ready cross-platform .NET

– Assess workloads for migration readiness

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.

The AWS Transform discovery tool automatically identifies server inventory within your organization to prepare for migration. The tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To use the discovery tool, you’ll configure one or more discovery sources, let the tool run, and then review the results in the Discovered Inventory pane.

Once you’ve set up a discovery source, the discovery tool begins collecting information. The time required for the tool to analyze your network completely depends on the size of your environment. For a directional migration business case, you can utilize the Migration Portfolio Assessment (MPA) files that the tool generates once server collection is complete.

The Migration Planning job step within AWS Transform for VMware provides a collaborative, chat-based experience designed for planning large migrations. AWS Transform agents utilize AWS Prescriptive Guidance to assist customers in transitioning from analyzing on-premises data to finalizing migration wave plans.

Once the Discover on-premises data job successfully completes, AWS Transform employs the discovery data to categorize applications into migration waves. The service guides you through the steps of analyzing and scoping your servers, grouping them into applications, creating move groups, and developing migration waves. During the analysis of your on-premises environment, you can ask questions to gain insights into how AWS Transform evaluated your installed software, including aspects such as server dependencies and network architecture.

AWS Transform assessments help you evaluate the cost, feasibility, and business value of migrating your on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinements through chat.

You can use migration assessments to:

– Obtain cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx

– Receive automated right-sizing recommendations

– Assess business value and sustainability impact

– Compare multiple migration scenarios side by side

– Refine assessments interactively through chat

– Generate executive presentations and detailed reports

Hence, the correct answer is: Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves, and use AWS Transform migration assessments to generate EC2 right-sizing and cost recommendations.

The option that says: Install the AWS Systems Manager Agent on both the physical servers and Virtual machines to perform an application-level assessment. Utilize Systems Manager Application Manager to logically separate servers into different applications. Input server size data into the AWS Pricing calculator and adhere to its recommendations is incorrect. The AWS Systems Manager agent does not provide a deep understanding of current resource usage and application dependencies as the AWS Application Discovery Agent. AWS Systems Manager Application Manager is primarily designed for application lifecycle management, not necessarily for grouping servers into applications as part of a migration strategy. Also, the AWS Pricing calculator gives cost estimates based on input parameters but does not provide sophisticated EC2 instance sizing recommendations that are based on actual performance and usage data.

The option that says: Use AWS Transform MGN to install replication agents on the source servers and immediately start continuous block-level replication to AWS. After the servers are launched on EC2, use AWS Compute Optimizer to recommend instance sizes is incorrect because AWS Transform MGN is typically a rehost migration service that replicates source servers to AWS using block-level replication. This option begins replication immediately and skips the required discovery, dependency analysis, application grouping, and migration wave planning. In addition, AWS Compute Optimizer analyzes CloudWatch metrics from running AWS resources, so it is better suited for optimization after workloads are already running in AWS, not for the required pre-migration assessment.

The option that says: Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves. After the workloads are migrated to EC2, use AWS Compute Optimizer to generate EC2 right-sizing recommendations is incorrect because it correctly uses AWS Transform discovery and migration planning, but it delays right-sizing until after the workloads have already been migrated to Amazon EC2. AWS Compute Optimizer provides recommendations for optimal AWS resource utilization based on historical usage data. In this case, the company has not yet migrated to AWS, so there’s no historical usage data for the Compute Optimizer to base its recommendations on.

 

References:

https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html

https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html

https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html

 

Check out this AWS Migration Services Cheat Sheet:

https://tutorialsdojo.com/aws-cheat-sheets-migration-services/

---

## Câu 53 — ✅ ĐÚNG

### Câu hỏi

A financial company is migrating its banking application to the cloud. The application will be deployed on medium-sized Amazon EC2 instances with an Amazon Aurora for PostgreSQL database. The company aims to increase the resiliency of the application by creating a disaster recovery plan to failover across different AWS regions. As part of compliance, the recovery point objective (RPO) should be under one minute, while the recovery time objective (RTO) should be a maximum of 15 minutes only.

What solution will fulfill these requirements MOST cost-effectively?

### Các phương án

- **A.** Deploy an identical infrastructure in multiple regions and keep the regions actively serving traffic. Use global load balancers to distribute requests between regions.
- **B.** Build the infrastructure using AWS CloudFormation templates to allow provisioning the resources in a DR region in the event of a disaster. Create an Aurora global database with the primary instance in the production region and a secondary (read-only) instance in the DR region. Configure AWS Elastic Disaster Recovery to continuously replicate the EC2 instances from the production region to the DR region, and setup an auto-scaling group in the DR region. Use Amazon Route 53 failover routing policy to direct traffic to DR in case of a disaster. ✅ 👈 *(bạn chọn)*
- **C.** Set up a scaled-down replica of the infrastructure in another AWS region. Keep the replica in a warm state by keeping at least one EC2 instance running and an Aurora for PostgreSQL instance active. Enable data replication from the primary database to the secondary database.
- **D.** Periodically take snapshots of the EC2 instances and Aurora for PostgreSQL database to serve as backups. In the event of a disaster, restore the system by launching EC2 instances from the snapshots and restoring the Aurora database from the database backup.

> **Bạn chọn:** B  
> **Đáp án đúng:** B  
> **Kết quả:** ✅ Đúng

### Giải thích

By default, AWS CloudFormation operates within a specific AWS region, and resources managed by the CloudFormation stack must reside in the same region as the stack. To achieve cross-region deployments, AWS CloudFormation StackSets can be used to deploy stacks across multiple accounts and regions. CloudFormation templates can include cross-region resource references. Nested stacks can also be used to organize resources logically and reference outputs across regions. Elastic Disaster Recovery is an AWS service that allows for a fast and reliable recovery of resources, increasing resilience. It has a Point in Time (PIT) state schedule, as low as 10 minutes for the last hour.

Amazon Aurora global databases span multiple AWS Regions, enabling low latency global reads and providing fast recovery from the rare outage that might affect an entire AWS Region. An Aurora global database has a primary DB cluster in one Region and up to five secondary DB clusters in different Regions. An Aurora global database provides more business continuity and disaster recovery (BCDR) protection than the standard high availability provided by an Aurora DB cluster in a single AWS Region. By using an Aurora global database, you can plan for and recover from true Regional disasters or complete service-level outages quickly. Amazon Route 53 allows a routing policy called Failover routing which allows routing traffic to a healthy resource or a different resource when the first resource is detected to be unhealthy.

Hence, the correct answer is: Build the infrastructure using AWS CloudFormation templates to allow provisioning the resources in a DR region in the event of a disaster. Create an Aurora global database with the primary instance in the production region and a secondary (read-only) instance in the DR region. Configure AWS Elastic Disaster Recovery to continuously replicate the EC2 instances from the production region to the DR region, and setup an auto-scaling group in the DR region. Use Amazon Route 53 failover routing policy to direct traffic to DR in case of a disaster.

The option that says: Deploy an identical infrastructure in multiple regions and keep the regions actively serving traffic. Use global load balancers to distribute requests between regions is incorrect. While this approach primarily achieves zero downtime during failover, it is the most expensive option. Running a full-scale infrastructure in multiple regions incurs high costs.

The option that says: Set up a scaled-down replica of the infrastructure in another AWS region. Keep the replica in a warm state by keeping at least one EC2 instance running and an Aurora for PostgreSQL instance active. Enable data replication from the primary database to the secondary database is incorrect. Although this approach can typically achieve the specified objectives of recovery time and recovery point, there is no automatic failover in place, which can add to the recovery time of the infrastructure in the DR region.

The option that says: Periodically take snapshots of the EC2 instances and Aurora for PostgreSQL database to serve as backups. In the event of a disaster, restore the system by launching EC2 instances from the snapshots and restoring the Aurora database from the database backup is incorrect. While this approach is cost-effective, the recovery point objective (RPO) and recovery time objective (RTO) may not be met since restoring from snapshots takes more time.

 

References:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/disaster-recovery-resiliency.html

https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html

 

Check out this AWS Disaster Recovery Cheat Sheet:

https://tutorialsdojo.com/aws-well-architected-framework-disaster-recovery/

---

## Câu 54 — ❌ SAI

### Câu hỏi

A company that operates a multi-cloud environment uses an on-premises Microsoft Active Directory for user authentication. As part of its expansion plans, the company is preparing to launch services in AWS. They want to leverage its existing Active Directory to control the permissions of those who wish to access AWS resources. There’s already a Direct Connect connection in place between the company’s on-premises data center and its AWS networks.

The company wants to enforce a security policy where access to accounts is regulated based on user group membership and assigned roles. Moreover, they must have the ability to manage user identities in a centralized location.

Which solution will meet these requirements?

### Các phương án

- **A.** Export the user list from the on-premises Active Directory and import it into a new AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). Configure trust relationships between AWS Managed Microsoft AD and AWS accounts. Use AWS Identity and Access Management (IAM) to manage user access and permissions. 👈 *(bạn chọn)*
- **B.** Connect to the Active Directory using AWS IAM Identity Center with SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use attribute-based access controls (ABACs) to grant access to the AWS accounts. ✅
- **C.** Create a PowerShell script that creates a separate identity provider for connecting to the Active Directory. Set up IAM user accounts manually in each AWS account and synchronize them with the identities in Active Directory.
- **D.** Create an AWS Cognito User Pool and connect it to Active Directory using SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use a Cognito Identity pool to grant access to the AWS accounts.

> **Bạn chọn:** A  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

With AWS IAM Identity Center (successor to AWS Single Sign-On), you can manage sign-in security for your workforce identities, also known as workforce users. IAM Identity Center provides one place where you can create or connect workforce users and centrally manage their access across all their AWS accounts and applications.

Both SCIM and SAML are important considerations for configuring IAM Identity Center.

You can use AWS IAM Identity Center (successor to AWS Single Sign-On) to authenticate identities from the IdPs through the Security Assertion Markup Language (SAML) 2.0 standard. This enables your users to sign in to the AWS access portal with their corporate credentials. They can then navigate to their assigned accounts, roles, and applications hosted in external IdPs.

IAM Identity Center supports automatic provisioning (synchronization) of user and group information from your identity provider (IdP) into IAM Identity Center using the System for Cross-domain Identity Management (SCIM) v2.0 protocol. When you configure SCIM synchronization, you create a mapping of your identity provider (IdP) user attributes to the named attributes in IAM Identity Center. This causes the expected attributes to match between IAM Identity Center and your IdP.

To allow users to use their Active Directory credentials in accessing AWS Accounts within AWS Organizations, you should establish a trust relationship between your on-premises Active Directory and AWS by setting up AWS IAM Identity Center with SAML 2.0.

To synchronize user attributes, such as username, email address, or group membership, enable System for Cross-domain Identity Management (SCIM) v2.0 automatic provisioning, which allows the management of user identities in a centralized location. To ensure access to accounts is constrained based on the user’s membership in particular groups and assigned roles AWS IAM Identity Center provides attribute-based access controls (ABACs), which let you define policies that grant access to AWS Accounts based on attributes like group membership or assigned roles in the Active Directory.

Hence, the correct answer is: Connect to the Active Directory using AWS IAM Identity Center with SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use attribute-based access controls (ABACs) to grant access to the AWS accounts.

The option that says: Create an AWS Cognito User Pool and connect it to Active Directory using SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use a Cognito Identity pool to grant access to the AWS accounts is incorrect. Although AWS Cognito can integrate with an existing Active Directory, it’s typically used for building sign-up and sign-in functionality for mobile app and web app users. Cognito can be an alternative solution when you want to authenticate users using their Active Directory credentials, but it will not provide the same level of centralized control as AWS IAM Identity Center in terms of user management and access control across AWS Organizations.

The option that says: Create a PowerShell script that creates a separate identity provider for connecting to the Active Directory. Set up IAM user accounts manually in each AWS account and synchronize them with the identities in Active Directory is incorrect. This approach is labor-intensive and could lead to consistency issues due to manual synchronization. Furthermore, this does not provide centralized identity management, as you would need to manage IAM user accounts in each AWS account separately

The option that says: Export the user list from the on-premises Active Directory and import it into a new AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). Configure trust relationships between AWS Managed Microsoft AD and AWS accounts. Use AWS Identity and Access Management (IAM) to manage user access and permissions is incorrect. This option doesn’t fully leverage the existing Active Directory, as it requires creating a new AWS Managed Microsoft AD. While AWS Managed Microsoft AD could potentially serve the requirements, this approach would likely lead to redundant management and potential synchronization issues. This also increases the complexity and cost of the solution, as the company would have to manage two separate Active Directory environments (on-premises and AWS Managed Microsoft AD).

 

References:

https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html

https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html

 

Check out this AWS IAM Cheat Sheet:

https://tutorialsdojo.com/aws-identity-and-access-management-iam

---

## Câu 55 — ❌ SAI

### Câu hỏi

An organization operates web and mobile platforms for online sales, inventory management, order processing, and shipping logistics. The platforms are running on Amazon EC2 instances across multiple regions. The organization’s databases include a MySQL database for the e-commerce site and a PostgreSQL database for analytics, both managed on EC2 instances.

A solutions architect requires a solution to transition the organization’s architecture to an event-driven, serverless architecture to improve efficiency and data processing speeds, enable real-time analytics, and streamline application data flows. The company also plans to launch a multi-cloud configuration that runs additional clusters on other cloud service providers to further improve the site’s performance.

Which of the following options would most efficiently meet these requirements?

### Các phương án

- **A.** Migrate to microservices with Amazon EKS and Fargate. Use Aurora Serverless MySQL for e-commerce and Redshift Serverless for analytics. Use Amazon EventBridge to streamline and manage data flows. ✅
- **B.** Create Auto Scaling groups for each platform component with specific EC2 instance numbers. Migrate e-commerce MySQL and analytics PostgreSQL databases to Amazon Aurora PostgreSQL. Use Amazon SNS to route incoming data to the right EC2 instances and databases.
- **C.** Use Amazon ECS with Fargate to repackage applications as microservices. Migrate e-commerce and analytics databases to Aurora Serverless MySQL and Redshift Serverless. Manage data flow between services using Amazon EventBridge.
- **D.** Migrate app components to microservices with Amazon EKS using AWS Fargate. Change e-commerce MySQL to Amazon Aurora MySQL and analytics DB to Amazon Redshift. Use Amazon Kinesis for real-time data streaming. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon EKS is a service that helps you run Kubernetes on AWS without having to set up or manage your own Kubernetes control plane. EKS allows you to concentrate on containers while AWS handles the underlying Kubernetes infrastructure. Amazon ECS on the other hand supports Docker containers, making it easier to run and scale containerized applications without worrying about managing virtual machine clusters.

ECS may be better if you want to use AWS-specific features. At the same time, EKS gives you more portability to move workloads on and off AWS if needed.

AWS Fargate is a serverless compute engine for containers. You can use containers without having to manage servers or clusters. AWS manages your containers, you only pay for the resources needed to run them. Fargate works with ECS and EKS.

Aurora Serverless is a serverless database that automatically scales capacity up or down to match your application’s needs. It is fully managed by AWS and provides high availability and auto-scaling for databases. Amazon Redshift Serverless is a fully managed serverless data warehousing service from AWS. With Redshift Serverless, you can run analytics and get insights from data without needing to provision and manage data warehouse infrastructure.

Amazon EventBridge is a serverless event bus service that allows you to connect applications together using data from various sources.

To improve the system, the applications can be migrated to a microservices architecture. By doing this, each microservice can be containerized and deployed to EKS on AWS Fargate, providing scalability and high availability without the need to manage servers. Additionally, the EKS is cloud-agnostic —meaning it is easier to integrate with other cloud service providers like Azure and GCP. For easy management, the transactional MySQL database can be migrated to Aurora Serverless. It provides the same capabilities as MySQL in a managed database that automatically scales based on usage. Similarly, the analytics data from transactions can be migrated to Redshift Serverless, which enables running ad-hoc queries and analytics on the data without having to worry about managing database capacity. To capture events from microservices and send relevant data to Aurora Serverless for transactions and Redshift Serverless for analytics, use EventBridge. This provides a central way to capture and route events and data between various services.

Hence, the correct answer is: Migrate to microservices with Amazon EKS and Fargate. Use Aurora Serverless MySQL for e-commerce and Redshift Serverless for analytics. Use Amazon EventBridge to streamline and manage data flows.

The option that says: Use Amazon ECS with Fargate to repackage applications as microservices. Migrate e-commerce and analytics databases to Aurora Serverless MySQL and Redshift Serverless. Manage data flow between services using Amazon EventBridge is incorrect. Although this option also suggests using Aurora Serverless, Amazon EventBridge, and Redshift Serverless, the container service being used is Amazon ECS, which typically does not support multi-cloud deployments, unlike EKS. While ECS with Fargate allows for container orchestration and management, it doesn’t fully address the requirement of explicit multi-cloud integration. In contrast, Amazon EKS (Elastic Kubernetes Service) with Fargate offers a more suitable platform for multi-cloud configuration with cost-effective serverless computing.

The option that says: Create Auto Scaling groups for each platform component with specific EC2 instance numbers. Migrate e-commerce MySQL and analytics PostgreSQL databases to Amazon Aurora PostgreSQL. Use Amazon SNS to route incoming data to the right EC2 instances and databases is incorrect. This solution fails to meet the serverless and event-driven architecture requirement as it still primarily relies on managing EC2 instances.

The option that says: Migrate app components to microservices with Amazon EKS using AWS Fargate. Change e-commerce MySQL to Amazon Aurora MySQL and analytics DB to Amazon Redshift. Use Amazon Kinesis for real-time data streaming is incorrect. Although the option suggests changing the e-commerce MySQL database to Amazon Aurora MySQL and the analytics database to Amazon Redshift, it doesn’t specifically mention utilizing the serverless variants of these databases. Leveraging Aurora Serverless MySQL and Redshift Serverless would provide better scalability and cost optimization, aligning more closely with the organization’s goal of streamlining data processing and achieving real-time analytics. Additionally, while Amazon Kinesis is suitable for real-time data streaming, it doesn’t address the requirement for efficient event-driven data flow management and integration between services in an event-driven architecture. Utilizing Amazon EventBridge would be more appropriate for managing data flows in such an architecture. Therefore, this option lacks full alignment with the requirements for transitioning to an event-driven, serverless architecture due to the omission of specific serverless database options and the choice of real-time data streaming service.

 

References:

https://docs.aws.amazon.com/solutions/latest/constructs/aws-fargate-eventbridge.html

https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/event-driven-architectures.html

https://aws.amazon.com/blogs/mt/moving-to-event-driven-architectures-with-serverless-event-aggregators/

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/amazon-redshift/

https://tutorialsdojo.com/amazon-elastic-kubernetes-service-eks/

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

https://tutorialsdojo.com/aws-fargate/

---

## Câu 56 — ✅ ĐÚNG

### Câu hỏi

A company is developing a serverless application that is deployed on AWS Lambda. The application consists of several Lambda functions that resize, watermark, and process images. The metadata generated from the functions is written in an Amazon DynamoDB table. The company deployed an Amazon Neptune DB cluster in three private subnets inside a VPC. A new feature was developed that requires the Lambda functions to access the Neptune DB cluster.

Which of the following options are possible solutions to allow the Lambda functions to access both the DynamoDB table and Neptune DB cluster? (Select TWO.)

### Các phương án

- **A.** Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Create a DynamoDB VPC endpoint and update the route table for routing DynamoDB requests. ✅ 👈 *(bạn chọn)*
- **B.** Deploy the AWS Lambda functions into three new public subnets in the same VPC. Update the Amazon Neptune DB security group to allow connections from the Lambda security group. Route internet traffic to the Internet Gateway.
- **C.** Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Route the internet traffic of the Lambda functions through a NAT gateway. ✅ 👈 *(bạn chọn)*
- **D.** Keep the AWS Lambda functions outside the VPC. Create a VPC endpoint for the Amazon Neptune service. Update the Lambda functions to use this endpoint to send requests to the Neptune DB cluster.
- **E.** Keep the Lambda functions outside the VPC. Configure the Neptune DB security group to allow inbound access from the AWS Lambda IP range.

> **Bạn chọn:** A, C  
> **Đáp án đúng:** A, C  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Neptune is a purpose-built, high-performance graph database engine. This engine is optimized for storing billions of relationships and querying the graph with milliseconds latency.

You can configure a Lambda function to connect to private subnets in a virtual private cloud (VPC) in your AWS account. Use Amazon Virtual Private Cloud (Amazon VPC) to create a private network for resources such as databases, cache instances, or internal services. Connect your function to the VPC to access private resources while the function is running.

When you connect a function to a VPC, Lambda assigns your function to a Hyperplane ENI (elastic network interface) for each subnet in your function’s VPC configuration. Lambda creates a Hyperplane ENI the first time a unique subnet and security group combination is defined for a VPC-enabled function in an account.

Internet access from a private subnet requires network address translation (NAT). To give internet access to an Amazon VPC-connected Lambda function, route its outbound traffic to a NAT gateway or NAT instance in a public subnet. Lambda functions do not, and cannot, have public IP addresses. You cannot send traffic to the internet, which happens via the VPC’s Internet Gateway, unless you have a public IP.

The option that says: Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Create a DynamoDB VPC endpoint and update the route table for routing DynamoDB requests is correct. In the private subnet, the Lambda functions can directly access the Neptune DB cluster, and the DynamoDB table via the DynamoDB VPC endpoint.

The option that says: Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Route the internet traffic of the Lambda functions through a NAT gateway is correct. Since DynamoDB is accessed via HTTPS API calls on the internet, you can use a NAT gateway to allow private resources, such as the Lambda functions, to route their traffic to the internet.

The option that says: Deploy the AWS Lambda functions into three new public subnets in the same VPC. Update the Amazon Neptune DB security group to allow connections from the Lambda security group. Route internet traffic to the Internet Gateway is incorrect. You can deploy Lambda functions on a public subnet. However, since Lambda functions typically do not have a public IP, they can’t directly access the internet even if you associate an internet gateway to the VPC.

The option that says: Keep the AWS Lambda functions outside the VPC. Create a VPC endpoint for the Amazon Neptune service. Update the Lambda functions to use this endpoint to send requests to the Neptune DB cluster is incorrect. Since the Neptune DB cluster is in a private subnet, it is not exposed to the outside world. A VPC endpoint is exposed only to resources inside a VPC, so Lamdba functions can’t connect to it either.

The option that says: Keep the Lambda functions outside the VPC. Configure the Neptune DB security group to allow inbound access from the AWS Lambda IP range is incorrect. Lambda functions by default are created outside a VPC and they can’t access any resources that are inside a VPC.

References:

https://docs.aws.amazon.com/neptune/latest/userguide/intro.html

https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html

https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/

Check out these Amazon VPC and AWS Lambda Cheat Sheets:

https://tutorialsdojo.com/amazon-vpc/

https://tutorialsdojo.com/aws-lambda/

---

## Câu 57 — ❌ SAI

### Câu hỏi

A company has an on-premises data center and uses a single 1 Gbps AWS Direct Connect connection to connect to its cloud resources in the us-east-1 region. The AWS Direct Connect connection uses a single private virtual interface to establish a connection to the VPC in us-east-1. The company has plans to expand and create a new VPC in the us-west-1 region. The solutions architect must design a solution that will add redundancy to the current AWS Direct Connect connection and use the same network to provide connectivity to the new VPC in the new region.

Which of the following should the solutions architect implement to meet the requirements?

### Các phương án

- **A.** Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection. Create a Direct Connect gateway. Create a new private virtual interface for each connection and associate them both to the Direct Connect gateway. Create a virtual private gateway for each region’s VPC and connect them to the Direct Connect gateway. ✅
- **B.** Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new public virtual interface for the second connection. Connect the us-west-1 VPC to the new public virtual interface.
- **C.** Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for the second connection. Create virtual private gateways on each VPC and associate both of them to the two private VIFs. 👈 *(bạn chọn)*
- **D.** Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for each Direct Connect connection. Create a transit gateway for each region’s VPC. Connect both private VIFs to the transit gateways.

> **Bạn chọn:** C  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Direct Connect makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs in the same region.

A Direct Connect gateway is a globally available resource to enable connections to multiple Amazon VPCs across different regions or AWS accounts. This feature also allows you to connect to any participating VPCs from one private VIF, reducing AWS Direct Connect management, as shown in the following figure.

Use AWS Direct Connect gateway to connect your VPCs. You associate an AWS Direct Connect gateway with either of the following gateways:

-A transit gateway when you have multiple VPCs in the same Region

-A virtual private gateway

A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any Region and access it from all other Regions. In the diagram, each VPC has a virtual private gateway that connects to the Direct Connect gateway using a virtual private gateway association. The Direct Connect gateway uses a private virtual interface for the connection to the AWS Direct Connect location. There is an AWS Direct Connect connection from the location to the customer data center.

Therefore, the correct answer is: Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection. Create a Direct Connect gateway. Create a new private virtual interface for each connection and associate them both to the Direct Connect gateway. Create a virtual private gateway for each region’s VPC and connect them to the Direct Connect gateway. A Direct Connect gateway is needed to connect VPCs from separate regions into a single (or redundant) Direct Connect connection using a private virtual interface.

The option that says: Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for the second connection. Create virtual private gateways on each VPC and associate both of them to the two private VIFs is incorrect. You can’t directly connect two virtual private gateways from two different regions to a private VIF. You will need to have a Direct Connect gateway for this.

The option that says: Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for each Direct Connect connection. Create a transit gateway for each region’s VPC. Connect both private VIFs to the transit gateways is incorrect. Transit gateway can be used to connect multiple VPCs from multiple regions, however, you will need a Direct Connect gateway and a transit virtual interface for this, not a private virtual interface.

The option that says: Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new public virtual interface for the second connection. Connect the us-west-1 VPC to the new public virtual interface is incorrect. Depending on the configuration for the VPCs in each region, you will only use a private VIF or a transit VIF to meet the company requirements. You do not need a public VIF. 

 

References:

https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html

https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html

https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html

https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html

 

Check out this AWS Direct Connect Cheat Sheet:

https://tutorialsdojo.com/aws-direct-connect/

---

## Câu 58 — ❌ SAI

### Câu hỏi

A company has built a REST API that retrieves data from an Amazon Aurora MySQL database. The API uses an AWS Lambda function as its backend and is served via an API Gateway Regional endpoint. The API is deployed in an AWS region close to its primary user base for optimal performance. During beta testing, the developers have noticed many idle database connections during periods of high demand, which impacts the application.

Which set of solutions could the company take to fix the issue? (Select TWO)

### Các phương án

- **A.** Reconfigure the API Gateway to use an edge-optimized endpoint and set a larger rate limit value. 👈 *(bạn chọn)*
- **B.** Initialize the code for database connection outside the event handler of the Lambda function. ✅
- **C.** Allocate Provisioned Concurrency for the Lambda function.
- **D.** Increase the Reserved Concurrency for the Lambda function and set a higher memory allocation.
- **E.** Create an RDS Proxy for the Aurora database. Modify the function to use the proxy endpoint. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** A, E  
> **Đáp án đúng:** B, E  
> **Kết quả:** ❌ Sai

### Giải thích

When using AWS Lambda, initializing the database connection outside the event handler leverages Lambda’s ability to reuse containers for multiple invocations. This approach promotes connection reuse, reducing the overhead of constantly establishing new connections with every invocation. By doing so, you can minimize cold start latencies and avoid rapidly exhausting the database’s connection limits, especially during traffic spikes.

Another way of fixing many idle connections is to use RDS Proxy. Opening a connection consumes resources on the database server. Since Lambda functions can scale to tens of thousands of concurrent connections, your database needs more resources to open and maintain connections instead of executing queries. The maximum number of connections a database can support is largely determined by the amount of memory allocated to it. Upgrading to a database instance with higher memory is a straightforward way of solving the problem. Another approach would be to maintain a connection pool that clients can reuse.

RDS Proxy helps you manage a large number of connections from Lambda to an RDS database by establishing a warm connection pool to the database. Your Lambda functions interact with RDS Proxy instead of your database instance. It handles the connection pooling necessary for scaling many simultaneous connections created by concurrent Lambda functions. This allows your Lambda applications to reuse existing connections rather than creating new connections for every function invocation.

Thus, the correct answers are:

– Initialize the code for database connection outside the event handler of the Lambda function.

– Create an RDS Proxy for the Aurora database. Modify the function to use the proxy endpoint.

The option that says: Allocate Provisioned Concurrency for the Lambda function is incorrect. This option ensures that a specified number of Lambda instances are always warm and ready to serve requests. While this could reduce cold start latencies, it wouldn’t resolve the issue of many idle database connections.

The option that says: Reconfigure the API Gateway to use an edge-optimized endpoint and set a larger rate limit value is incorrect. Using an Edge-optimized endpoint would simply help decrease latency for clients in multiple geographical locations. It’s not a solution for the issue of many idle database connections. Moreover, increasing the rate limit may exacerbate the problem if the Lambda function creates more connections during periods of high demand.

The option that says: Increase the Reserved Concurrency for the Lambda function and set a higher memory allocation is incorrect. Increasing the reserved concurrency limit without connection pooling might lead to more simultaneous database connections, which is counterproductive. Also, increasing the Lambda function’s memory would only make it run processes faster and won’t have a significant effect on getting rid of the error.

 

References:

https://aws.amazon.com/rds/proxy/

https://aws.amazon.com/blogs/compute/using-amazon-rds-proxy-with-aws-lambda/

https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html

 

Check out this Amazon RDS Cheat Sheet:

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

---

## Câu 59 — ✅ ĐÚNG

### Câu hỏi

A company hosts a .NET REST API in AWS. Currently, the business logic of the API is deployed on three EC2 instances distributed across different Availability Zones. The application is monolithic in nature, and some functions tend to consume more resources than others during operation. Clients interact with the API by calling its domain name. This domain is registered with Route 53, which uses a multi-value answer policy to route each request to one of the available EC2 instances.

The application experiences non-constant traffic throughout the day and becomes unresponsive during periods of peak demand. A solutions architect is tasked with redesigning the architecture to be more cost-effective and to have the least amount of operational overhead.

Which solution will meet these requirements?

### Các phương án

- **A.** Register the existing EC2 instances in an Auto Scaling group and use it as a target for an Application Load Balancer (ALB). Configure a dynamic scaling policy based on the ALB’s RequestCountPerTarget metric. Update Route 53 to direct traffic to the ALB’s endpoint.
- **B.** Create a custom routing accelerator in AWS Global Accelerator, targeting the subnets housing the EC2 instances. Place the EC2 instances into an Auto Scaling group with a policy that scales based on average CPU utilization. Update the Route 53 records to resolve to the IP address provided by the Global Accelerator.
- **C.** Move the API on an Amazon Elastic Kubernetes Service (EKS) cluster that uses EC2 Spot Instances. Configure a Kubernetes Ingress controller for request routing and create a corresponding ingress resource. Update Route 53 to point to the external IP provided by the Ingress controller.
- **D.** Split the API into multiple AWS Lambda functions to handle different components. Provision an Amazon API Gateway REST API to act as the interface for these Lambda functions. Configure a custom domain in API Gateway, then update the Route 53 record to map to this custom domain. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Lambda is a serverless compute service that lets you run your code without provisioning or managing servers. It executes your code only when needed and scales automatically, from a few requests per day to thousands per second. Amazon API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs at any scale. It acts as a “front door” for applications to access data, business logic, or functionality from your backend services, such as Lambda functions, web applications, or real-time communication services. In combination, Lambda and API Gateway provide a powerful, scalable, and cost-effective solution to build and expose APIs without the need for server management.

In the scenario, by transitioning from monolithic to microservices using multiple AWS Lambda functions managed through Amazon API Gateway, the architecture becomes serverless. This significantly reduces operational overhead and costs for fluctuating traffic as you pay only for what you use. Additionally, breaking down the monolithic API into Lambda functions allows for fine-grained scalability. Unlike in a monolithic architecture where the entire application must scale as a unit, individual Lambda functions can scale independently based on the demand for that specific function.

Hence, the correct answer in this scenario is: Split the API into multiple AWS Lambda functions to handle different components. Provision an Amazon API Gateway REST API to act as the interface for these Lambda functions. Configure a custom domain in API Gateway, then update the Route 53 record to map to this custom domain.

The option that says: Register the existing EC2 instances in an Auto Scaling group and use it as a target for an Application Load Balancer (ALB). Configure a dynamic scaling policy based on the ALB’s RequestCountPerTarget metric. Update Route 53 to direct traffic to the ALB’s endpoint is incorrect. The use of EC2 instances to host a monolithic application presents a limitation in that you cannot scale individual components independently. If a function within the application overwhelms the resources of one of the EC2 instances, you’re forced to scale the entire application by adding more EC2 instances. Thus, this approach is less cost-effective.

The option that says: Create a custom routing accelerator in AWS Global Accelerator, targeting the subnets housing the EC2 instances. Place the EC2 instances into an Auto Scaling group with a policy that scales based on average CPU utilization. Update the Route 53 records to resolve to the IP address provided by the Global Accelerator is incorrect. AWS Global Accelerator is primarily used for improving the availability and performance of applications with global users by routing user traffic through AWS’s network infrastructure. However, unless the application has a global user base that would benefit from such optimized routing, incorporating Global Accelerator could add unnecessary complexity and cost.

The option that says: Move the API on an Amazon Elastic Kubernetes Service (EKS) cluster that uses EC2 Spot Instances. Configure a Kubernetes Ingress controller for request routing and create a corresponding ingress resource. Update Route 53 to point to the external IP provided by the Ingress controller is incorrect. Deploying the API on an Amazon EKS cluster would introduce considerable operational complexity. Kubernetes is powerful but has a steep learning curve and high operational overhead, making it less aligned with the goal of minimizing operational tasks. Moreover, although using Spot Instances can be cost-effective, they’re not suitable for all types of workloads, especially for applications that cannot tolerate disruptions.

 

References:

https://aws.amazon.com/blogs/compute/migrating-a-monolithic-net-rest-api-to-aws-lambda/

https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html

 

Check out these AWS Lambda and Amazon API Gateway Cheat Sheets:

https://tutorialsdojo.com/aws-lambda/

https://tutorialsdojo.com/amazon-api-gateway/

---

## Câu 60 — ✅ ĐÚNG

### Câu hỏi

An advertising company has terabytes of data on its Amazon S3 data lake. Its partner companies upload customer preference data over a custom SFTP server every night. The SFTP URL is reachable via the Amazon Route 53 domain name sftp.tutorialsdojo.com. It is hosted on an Amazon EC2 instance in a public subnet inside a VPC. There is a cron job script on the ec2 instance that sends the uploaded files from the SFTP server to the Amazon S3 data lake.

Which of the following implementations will improve the reliability and scalability of the SFTP server?

### Các phương án

- **A.** Create a TCP listener on a Network Load Balancer (NLB) and place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the NLB domain name.
- **B.** Use AWS Transfer for SFTP service instead to serve as the SFTP server. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the server endpoint hostname. ✅ 👈 *(bạn chọn)*
- **C.** Create an HTTPS listener on an Application Load Balancer (ALB) and place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the ALB domain name.
- **D.** Migrate the SFTP server to an AWS Storage Gateway file gateway and expose its endpoint URL. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the storage gateway endpoint.

> **Bạn chọn:** B  
> **Đáp án đúng:** B  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services. AWS Transfer Family supports transferring data from or to the following AWS storage services – Amazon Simple Storage Service (Amazon S3) storage and Amazon Elastic File System (Amazon EFS) Network File System (NFS) file system.

AWS Transfer Family supports transferring data over the following protocols:

-Secure Shell (SSH) File Transfer Protocol (SFTP) (AWS Transfer for SFTP)

-File Transfer Protocol Secure (FTPS) (AWS Transfer for FTPS)

-File Transfer Protocol (FTP) (AWS Transfer for FTP)

Common use cases for Transfer Family with Amazon S3 are the following:

-Data lakes in AWS for uploads from third parties such as vendors and partners.

-Subscription-based data distribution with your customers.

-Internal transfers within your organization.

AWS Transfer Family supports up to 3 Availability Zones and is backed by an auto scaling, redundant fleet for your connection and transfer requests. With Transfer Family, you get access to a file transfer protocol-enabled server in AWS without the need to run any server infrastructure. You can use this service to migrate your file transfer-based workflows to AWS while maintaining your end users’ clients and configurations as is. You first associate your hostname with the server endpoint, then add your users and provision them with the right level of access. After you do this, your users’ transfer requests are serviced directly out of your Transfer Family server endpoint.

Therefore, the correct answer is: Use AWS Transfer for SFTP service instead to serve as the SFTP server. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the server endpoint hostname. This is a fully managed, highly scalable solution for hosting SFTP services in AWS. 

The option that says: Create a TCP listener on a Network Load Balancer (NLB), place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the NLB domain name is incorrect. This is possible to implement, however, it will require unnecessary work and configuration to set up correctly. Using the AWS Transfer for SFTP service is designed for these types of scenarios.

The option that says: Create an HTTPS listener on an Application Load Balancer (ALB), place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the ALB domain name is incorrect. The SFTP service uses the TCP protocol so an HTTPS listener on an ALB will not work in this scenario. 

The option that says: Migrate the SFTP server to an AWS Storage Gateway file gateway and expose its endpoint URL. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the storage gateway endpoint is incorrect. The AWS Storage Gateway file gateway is ideal for on-premises scenarios requiring data to be sent to AWS. There is no exposed SFTP endpoint for the file gateway. 

 

References:

https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html

https://docs.aws.amazon.com/transfer/latest/userguide/how-aws-transfer-works.html

https://docs.aws.amazon.com/transfer/latest/userguide/transfer-file.html

 

Check out this AWS Transfer Family Cheat Sheet:

https://tutorialsdojo.com/aws-transfer-family/

---

## Câu 61 — ❌ SAI

### Câu hỏi

A forecasting agency is struggling to meet the Service Level Agreement (SLA) of its online platform. To avoid penalties and maintain credibility, they aim to develop a recovery plan that assures a Recovery Time Objective (RTO) of no more than 30 minutes.

Their platform runs on an Auto Scaling Group (ASG) connected to an Application Load Balancer (ALB). Data is stored in an Amazon RDS PostgreSQL database. An identical environment exists in a secondary region where the ASG’s capacity limits are set to zero. A read replica of the RDS database is deployed in this backup region as well. A Route 53 alias record is configured to route domain traffic to the ALB.

The agency cannot afford an active-active failover and is opting for a more cost-effective way of switching over to the backup region.

Which strategy would meet these requirements?

### Các phương án

- **A.** Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Set up a CloudWatch alarm that triggers the function when the HTTPCode_ELB_502_Count ALB metric becomes greater than or equal to 1.
- **B.** Set up an Amazon CloudWatch alarm that tracks the HTTPCode_Target_5XX_Count metric of the ALB in the primary Region. Create a secondary Route 53 record with identical values as the primary record. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Route 53 health check that sends an Amazon SNS notification to a Lambda function that will promote the read replica to the primary.
- **C.** Update the routing policy of the alias record to Weight with a value of 100. Create a new alias record for the application’s domain with a Weight routing policy initialized to 0. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Lambda function for weight adjustment and read replica promotion. Set up a Route 53 health check that sends an Amazon SNS notification to the Lambda function. 👈 *(bạn chọn)*
- **D.** Add a failover policy in the alias record to redirect traffic to the Application Load Balancer in the secondary Region. Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Monitor the application status with a Route 53 health check that uses Amazon SNS to invoke the Lambda function when the application becomes unhealthy. ✅

> **Bạn chọn:** C  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

On Amazon Route 53, after you create a hosted zone for your domain, such as tutorialsdojo.com, you create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain. You can create a record that points to the DNS name of your Application Load Balancer on AWS.

When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:

Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.

Failover routing policy – Use when you want to configure active-passive failover.

Geolocation routing policy – Use when you want to route traffic based on the location of your users.

Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.

Latency routing policy – Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.

Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.

Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify.

You can use Route 53 health checks to configure active-active and active-passive failover configurations. You configure active-active failover using any routing policy (or combination of routing policies) other than failover, and you configure active-passive failover using the failover routing policy.

In the scenario, an active-passive failover can be achieved by adding a failover policy to the existing record. This policy will redirect traffic to the Application Load Balancer in the secondary region when the primary application becomes unhealthy. A Lambda function is used to increase the Auto Scaling Group’s capacity limits in the secondary region and to promote the RDS read replica to become the primary database. The application’s health status is monitored by a Route 53 health check, which uses Amazon SNS to invoke the Lambda function in case of any issues. This strategy ensures a swift response to application failures, meeting the required Recovery Time Objective (RTO) in a cost-effective manner.

Therefore, the correct answer is: Add a failover policy in the alias record to redirect traffic to the Application Load Balancer in the secondary Region. Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Monitor the application status with a Route 53 health check that uses Amazon SNS to invoke the Lambda function when the application becomes unhealthy.

The option that says: Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Set up a CloudWatch alarm that triggers the function when the HTTPCode_ELB_502_Count ALB metric becomes greater than or equal to 1 is incorrect. This ALB metric is too specific and may not cover all the potential reasons for a failover. The application could become unhealthy due to various other reasons not related to HTTP 502 errors. Therefore, this solution does not provide comprehensive coverage for application health monitoring.

The option that says: Update the routing policy of the alias record to Weight with a value of 100. Create a new alias record for the application’s domain with a Weight routing policy initialized to 0. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Lambda function for weight adjustment and read replica promotion. Set up a Route 53 health check that sends an Amazon SNS notification to the Lambda function is incorrect. This is not cost-effective since you’re constantly running and paying for a minimal capacity in the secondary region. The process of adjusting weights also could potentially delay the recovery time, affecting the desired RTO.

The option that says: Set up an Amazon CloudWatch alarm that tracks the HTTPCode_Target_5XX_Count metric of the ALB in the primary Region. Create a secondary Route 53 record with the same name, the same type, and the same routing policy as the primary record. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Route 53 health check that sends an Amazon SNS notification to a Lambda function that will promote the read replica to primary is incorrect. This option actually suggests an active-active setup, where both environments are running simultaneously. In this setup, Route 53’s health checks would monitor both environments and if one becomes unhealthy, Route 53 will route traffic only to the healthy environment. This setup costs a lot more since two environments are running at the same time. The scenario specifically mentioned that the agency cannot afford an active-active failover and is opting for a more cost-effective way of switching over to the backup region.

 

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html

https://aws.amazon.com/blogs/networking-and-content-delivery/manual-failover-and-failback-strategy-with-amazon-route53/

 

Check out the Amazon Route 53 Cheat Sheet:

https://tutorialsdojo.com/amazon-route-53/

---

## Câu 62 — ❌ SAI

### Câu hỏi

An organization uses AWS Organizations and the Organizations API to manage its IT resources across multiple member accounts. The management account occasionally uses the RemoveAccountFromOrganization operation to detach member accounts when necessary. In addition, the organization deploys virtual appliances as part of its centralized networking strategy. The appliances are critical for the company’s network security and must scale dynamically to meet fluctuating traffic demands. The virtual appliances operate in a centralized networking account connected through a transit gateway to various member account VPCs.

Recently, a misconfigured script accidentally terminated all instances of the virtual appliances, causing operational downtime. In response, the organization revised the startup scripts for the appliances to enhance resilience and scalability.

A solutions architect must find a solution to efficiently scale the virtual appliances horizontally, ensure secure and private connections across accounts, and minimize manual configuration.

Which combination of steps will meet these requirements? (Select TWO.)

### Các phương án

- **A.** Configure VPC peering between the centralized networking account and member accounts to streamline network traffic routing.
- **B.** Use an Application Load Balancer to distribute traffic to the virtual appliances based on demand.
- **C.** Set up an Auto Scaling group using a launch template with the updated script as user data to automate the configuration of virtual appliances, linking to a target group with instance-based targets. ✅
- **D.** Provision a Gateway Load Balancer within the centralized networking account and integrate it with an endpoint service via AWS PrivateLink for secure traffic routing. ✅ 👈 *(bạn chọn)*
- **E.** Implement AWS Direct Connect to establish a dedicated network connection between the centralized networking account and member account VPCs. 👈 *(bạn chọn)*

> **Bạn chọn:** D, E  
> **Đáp án đúng:** C, D  
> **Kết quả:** ❌ Sai

### Giải thích

A Gateway Load Balancer operates at the network layer (layer 3) of the OSI model to distribute traffic to virtual appliances like firewalls and intrusion prevention systems. Gateway Load Balancer Endpoints provide private connectivity between appliances in one VPC and servers in another VPC.

PrivateLink enables private connectivity between VPCs and AWS services without an internet gateway, NAT device, VPN connection, or AWS Direct Connect. Interface endpoints provide a private IP address from your VPC that acts as an entry point for the service.

An Auto Scaling group is a collection of EC2 instances that are managed together by Auto Scaling. It ensures the number of instances matches the target capacity. Auto Scaling groups can be configured to scale based on metrics, schedules or other triggers.

To provide scalability of virtual appliances while maintaining consistent security policies across different accounts, a solutions architect should use a combination of Gateway Load Balancer, AWS PrivateLink, and Auto Scaling group. The Gateway Load Balancer would distribute traffic to the virtual appliances, allowing them to scale horizontally behind the load balancer as traffic increases. Using AWS PrivateLink, the virtual appliances would be accessible to other accounts in a private and secure manner without exposing them publicly. Configuring an Auto Scaling group with the updated startup script would enable automatic scaling of the virtual appliance instances, linking to a target group associated with the Gateway Load Balancer. Together, these steps would eliminate manual work and provide scalability of the appliances, along with secure and private connections across accounts.

Hence, the correct answers are:

– Set up an Auto Scaling group using a launch template with the updated script as user data to automate the configuration of virtual appliances, linking to a target group with instance-based targets.

– Provision a Gateway Load Balancer within the centralized networking account and integrate it with an endpoint service via AWS PrivateLink for secure traffic routing.

The option that says: Implement AWS Direct Connect to establish a dedicated network connection between the centralized networking account and member account VPCs is incorrect because AWS Direct Connect primarily facilitates a dedicated network link between the AWS environment and an organization’s data center, not specifically for scaling virtual appliances within AWS.

The option that says: Configure VPC peering between the centralized networking account and member accounts to streamline network traffic routing is incorrect. While VPC peering typically helps in traffic routing between VPCs, it does not aid in scaling or automated configuration of virtual appliances.

The option that says: Use an Application Load Balancer to distribute traffic to the virtual appliances based on demand is incorrect because an Application Load Balancer is more suitable for application-level traffic management and does not specifically cater to the unique requirements of network appliances or inter-VPC network security and routing capabilities that a Gateway Load Balancer offers.

 

References:

https://aws.amazon.com/blogs/publicsector/implementing-third-party-firewall-appliances-aws-comparing-two-methods/

https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-gateway-load-balancer/

https://tutorialsdojo.com/aws-auto-scaling/

---

## Câu 63 — ❌ SAI

### Câu hỏi

A manufacturing company operates an on-premises application on a self-managed Kubernetes cluster. The application includes a MySQL database for order processing and a MongoDB database for inventory tracking. The company plans to migrate the workloads to Amazon Elastic Kubernetes Service (Amazon EKS) cluster to improve scalability and manageability. Both environments are expected to maintain a fixed number of nodes to meet performance and capacity requirements.

Before proceeding with the migration, the company must assess the Total Cost of Ownership (TCO) for running the Kubernetes clusters and databases on AWS.

Which solution provides the most effective way to assess the Total Cost of Ownership (TCO)?

### Các phương án

- **A.** Use AWS Transform MGN to initiate the migration process for your on-premises servers. Add the servers as source instances and perform a test migration. Generate a TCO report from Transform MGN to evaluate the cost of running your workloads in AWS.
- **B.** Ask for access to the Migration Evaluator to begin the TCO assessment. Use the Migration Evaluator Collector to gather data from your on-premises and then import the data. Export a Migration Evaluator Quick Insights report to evaluate the Total Cost of Ownership (TCO) for migrating workloads to AWS. ✅
- **C.** Leverage AWS Application Discovery Service (Application Discovery Service) to collect detailed information about your on-premises environment. Use the data from the discovery service to assess migration costs and generate a TCO report for moving to AWS. 👈 *(bạn chọn)*
- **D.** Visit the AWS Cloud Economics Center to explore the AWS Cloud Value Framework. Use this framework to understand the economic benefits of cloud migration. From there, create an AWS Cost and Usage report to assess the costs of running your Kubernetes clusters and databases on AWS.

> **Bạn chọn:** C  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Migration Evaluator, formerly the TCO Calculator, is a tool designed to help businesses estimate the total cost of ownership (TCO) for migrating their on-premises workloads to AWS. This service allows users to assess the financial implications of moving their infrastructure and applications from on-premises data centers to the AWS cloud.

By collecting key data points about an organization’s current infrastructure, such as the number of servers, storage requirements, and network configuration, the Migration Evaluator generates detailed reports comparing the costs of running workloads on AWS with those of the existing on-premises environment.

The Migration Evaluator Collector facilitates the gathering of data from on-premises environments. It collects detailed information on infrastructure usage and resource consumption, which can then be imported into the Migration Evaluator. Once the data is collected, the tool analyzes it. Produces a Quick Insights report, highlighting potential cost savings and providing a side-by-side comparison of the on-premises environment versus the proposed AWS environment. This analysis helps businesses make informed decisions about migration, budgeting, and resource planning, ensuring they understand the financial benefits and trade-offs of moving to the cloud.

In addition to cost estimates, the tool offers insights into optimization opportunities, assisting companies in refining their cloud strategy. It simplifies the complex process of evaluating cloud costs, enabling businesses to make more informed choices about their infrastructure and future cloud investments.

Hence, the correct answer is: Ask for access to the Migration Evaluator to begin the TCO assessment. Use the Migration Evaluator Collector to gather data from your on-premises and then import the data. Export a Migration Evaluator Quick Insights report to evaluate the Total Cost of Ownership (TCO) for migrating workloads to AWS.

The option that says: Use AWS Transform MGN to initiate the migration process for your on-premises servers. Add the servers as source instances and perform a test migration. Generate a TCO report from Transform MGN to evaluate the cost of running your workloads in AWS is incorrect. AWS Transform MGN is primarily focused on migration execution and rehosting workflows, not simply producing a formal pre-migration TCO assessment for Kubernetes clusters and databases.

The option that says: Visit the AWS Cloud Economics Center to explore the AWS Cloud Value Framework. Use this framework to understand the economic benefits of cloud migration. From there, create an AWS Cost and Usage report to assess the costs of running your Kubernetes clusters and databases on AWS is incorrect. While this option offers valuable insights into the general economic advantages of migrating to AWS, such as cost savings and flexibility, it does not focus on detailed, granular TCO calculations for specific workloads. The AWS Cloud Value Framework helps organizations evaluate cloud adoption at a high level, but it lacks the comprehensive cost estimation and comparison features Migration Evaluator offers for TCO assessment.

The option that says: Leverage AWS Application Discovery Service (Application Discovery Service) to collect detailed information about your on-premises environment. Use the data from the discovery service to assess migration costs and generate a TCO report for moving to AWS is incorrect. AWS Application Discovery Service gathers detailed information about your on-premises environment, including application dependencies, resource utilization, and system configurations. It is a critical tool for planning and mapping out complex migration scenarios but does not generate TCO reports alone. The service only focuses on discovering and cataloging the environment rather than directly assessing migration costs. While it helps gather the data necessary for a TCO analysis, it does not provide the final cost comparison or detailed TCO insights, which is the primary need in the scenario.

 

References:

https://aws.amazon.com/migration-evaluator/

https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-pricingtco-tools.html

 

Check out this Migration Evaluator Cheat Sheet:

https://tutorialsdojo.com/migration-evaluator-cheat-sheet/

---

## Câu 64 — ✅ ĐÚNG

### Câu hỏi

A company is developing a containerized web application using the .NET Core framework which is packaged as a Docker container. This application will serve public traffic and the management wants to deploy it in AWS. The application requires a highly-available Microsoft SQL Server as its database backend. As a security best practice, the SQL Server connection string should not be saved inside the container to avoid exposing the database password.

Which of the following options should the Solutions Architect implement to deploy the application in AWS while satisfying the company requirements?

### Các phương án

- **A.** Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the Fargate service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers. ✅ 👈 *(bạn chọn)*
- **B.** Deploy the SQL Server in an AWS Fargate cluster with Service Auto Scaling. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create another Fargate Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers.
- **C.** Deploy the SQL Server in an Auto Scaling group of Amazon EC2 instances. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers.
- **D.** Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create an Amazon EKS Distro cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an IAM role associated with the EKS service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s pod definition. Create an empty non-persistent volume attachment in the pod definition. This allows EKS to write the database credentials to the non-persistent volume when starting the containers.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon RDS supports DB instances running several versions and editions of Microsoft SQL Server. Amazon RDS currently supports Multi-AZ deployments for SQL Server using SQL Server Database Mirroring (DBM) or Always On Availability Groups (AGs) as a high-availability, failover solution.

AWS Secrets Manager enables you to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. This helps ensure the secret can’t be compromised by someone examining your code because the secret no longer exists in the code. Also, you can configure Secrets Manager to automatically rotate the secret for you according to a specified schedule. This enables you to replace long-term secrets with short-term ones, significantly reducing the risk of compromise.

Amazon ECS enables you to inject sensitive data into your containers by storing your sensitive data in AWS Secrets Manager secrets and then referencing them in your container definition. Sensitive data stored in Secrets Manager secrets can be exposed to a container as environment variables or as part of the log configuration. In the Task Definition, you can instruct Fargate tasks to securely grab secrets from Secrets Manager so that these secrets are never exposed in the wild—not even in private configuration files. This frees you from the burden of having to implement the undifferentiated heavy lifting of securing these secrets.

When you inject a secret as an environment variable, you can specify the full contents of a secret, a specific JSON key within a secret, or a specific version of a secret to inject. This helps you control the sensitive data exposed to your container.

Therefore, the correct answer is: Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the Fargate service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers.

The option that says: Deploy the SQL Server in an AWS Fargate cluster with Service Auto Scaling. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create another Fargate Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers is incorrect. Deploying the SQL Server in a Fargate cluster is not recommended because you will need persistent and durable storage. You should use Amazon RDS for SQL Server instead.

The option that says: Deploy the SQL Server in an Auto Scaling group of Amazon EC2 instances. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers is incorrect. This solution is feasible, but deploying the SQL Server in an Auto Scaling group of EC2 instances is not recommended. You should use Amazon RDS for SQL Server with Multi-AZ instead so that AWS can manage the replication and availability of the cluster.

The option that says: Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create an Amazon EKS Distro cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an IAM role associated with the EKS service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s pod definition. Create an empty non-persistent volume attachment in the pod definition. This allows EKS to write the database credentials to the non-persistent volume when starting the containers is incorrect because using Amazon EKS Distro adds complexity as it’s not a managed service. Storing credentials in a non-persistent volume could lead to loss of data if the pod is terminated. It might be simpler to use a service more integrated with Docker, like Amazon ECS or AWS Fargate, given that your application is a Docker container.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html

https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html

https://docs.aws.amazon.com/AmazonECS/latest/userguide/specifying-sensitive-data-secrets.html

https://aws.amazon.com/blogs/compute/securing-credentials-using-aws-secrets-manager-with-aws-fargate/

 

Check out these AWS Fargate and AWS Secrets Manager Cheat Sheets:

https://tutorialsdojo.com/aws-fargate/

https://tutorialsdojo.com/aws-secrets-manager/

---

## Câu 65 — ✅ ĐÚNG

### Câu hỏi

A startup develops a new web application that manages job listings for contractors and seasonal workers. The application source code is stored on a GitHub repository. For continuous integration, the developers trigger a pipeline on AWS CodePipeline. This pipeline includes a build stage that generates an artifact that is sent to an Amazon S3 bucket. The developers want to improve this process and have requested the solutions architect to create a strategy that meets the following requirements:

– Create a pipeline to accommodate Feature-Driven Development (FDD) process for the app

– Feature development must not affect the existing production application

– Must include a stage for continuous unit testing

– Create separate development and production artifacts

– Maintain the capability of integrating development and production code.

Which of the following options is the recommended solution to meet the company’s requirements?

### Các phương án

- **A.** Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage for AWS CodeBuild to run unit testing and stage the generated artifacts in an S3 bucket in a separate testing AWS account. ✅ 👈 *(bạn chọn)*
- **B.** Create a new repository in GitHub for features development. Use Amazon CodeGuru to review and improve your code. Then, use the commits on this repo as triggers for AWS CodeBuild to build and test the artifacts. Use AWS CodeDeploy to stage the artifacts on a separate S3 bucket in the production AWS account.
- **C.** Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage that will trigger AWS Lambda functions to perform unit testing on the generated artifacts. Use AWS CodeDeploy to stage the artifacts on an S3 bucket in a separate testing AWS account.
- **D.** Create a new pipeline in Jenkins that is triggered by the “feature” tags from GitHub. Add a stage that will run unit testing on the generated artifacts. Send the artifacts to a staging S3 bucket in a separate AWS account using the AWS Well-Architected Tool.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS CodePipeline is a continuous delivery service that you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

AWS CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers.

You can automate your release process by using AWS CodePipeline to test your code and run your builds with AWS CodeBuild. You can use the AWS suite of CI/CD services to compile, build, and install a version-controlled Java application onto a set of Amazon Elastic Compute Cloud (Amazon EC2) Linux instances via a fully automated and secure pipeline. With these tools, you can promote a code commit or change to pass through various automated stage gates all the way from development to production environments across AWS accounts.

The following diagram illustrates the workflow:

– A change or commit to the code in the GitHub repository triggers CodePipeline through a webhook event.

– The pipeline downloads the code from the GitHub repository, initiates the Build and Test action using CodeBuild, and securely saves the built artifact on the S3 bucket.

– If the preceding step is successful, the pipeline triggers the Deploy in Dev action using CodeDeploy and deploys the app in the dev account.

– If successful, the pipeline triggers the Deploy in Prod action using CodeDeploy and deploys the app in the prod account.

Therefore, the correct answer is: Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage for AWS CodeBuild to run unit testing and stage the generated artifacts in an S3 bucket in a separate testing AWS account.

The option that says: Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage that will trigger AWS Lambda functions to perform unit testing on the generated artifacts. Use AWS CodeDeploy to stage the artifacts on an S3 bucket in a separate testing AWS account is incorrect. This is possible; however, it is not necessary to write Lambda code for unit testing. You just need to include the tests on the CodeBuild stage, which will perform the unit testing.

The option that says: Create a new pipeline in Jenkins that is triggered by the “feature” tags from GitHub. Add a stage that will run unit testing on the generated artifacts. Send the artifacts to a staging S3 bucket in a separate AWS account using the AWS Well-Architected Tool is incorrect. Using a separate Jenkins instance to run your pipeline is not recommended. AWS CodePipeline is an AWS-managed service that can automate code builds, unit testing, and deployments on your behalf. Moreover, the AWS Well-Architected Tool simply allows you to monitor the status of multiple workloads across your organization and helps you understand potential risks. This is not meant to send artifacts to a staging S3 bucket located in a separate AWS account.

The option that says: Create a new repository in GitHub for features development. Use Amazon CodeGuru to review and improve your code. Then, use the commits on this repo as triggers for AWS CodeBuild to build and test the artifacts. Use AWS CodeDeploy to stage the artifacts on a separate S3 bucket in the production AWS account is incorrect. You don’t need to create a separate repository for your feature development. This will just duplicate your GitHub storage and can add complexity to your deployments. It is recommended to create a feature branch instead and use it to test and deploy new features. Moreover, while CodeGuru can help improve code quality, it’s not explicitly required to meet the stated requirements. The scenario doesn’t mention the need for code review or performance optimization, which are the primary functions of CodeGuru. Therefore, while CodeGuru could be beneficial in a general sense for improving code quality, it’s not strictly necessary based on the specific requirements given in the question.

 

References:

https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html

https://aws.amazon.com/about-aws/whats-new/2018/05/aws-codepipeline-supports-push-events-from-github-via-webhooks/

https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html

 

Check out these AWS CodePipeline and AWS CodeBuild Cheat Sheets:

https://tutorialsdojo.com/aws-codepipeline/

https://tutorialsdojo.com/aws-codebuild/

---

## Câu 66 — ✅ ĐÚNG

### Câu hỏi

A company hosts an e-commerce application on an Auto Scaling group (ASG) of EC2 instances behind an Application Load Balancer (ALB). The ASG is set to maintain 10 EC2 instances at all times. It uses Elastic Load Balancing (ELB) health checks to detect and replace any unhealthy instances. Each EC2 instance has a CloudWatch agent installed that sends application logs to Amazon CloudWatch Logs at 5-minute intervals.

The operations team is unable to recover logs that were stored in terminated instances. This prevents them from conducting proper troubleshooting. For this reason, they require a solution that can automatically collect and back up relevant log data from instances that are about to be terminated.

Which solution would meet the requirements?

### Các phương án

- **A.** Add a lifecycle hook to the Auto Scaling Group for the autoscaling:EC2_INSTANCE_TERMINATING event and set the default result to CONTINUE. Implement a script using an AWS Systems Manager Automation document to backup log data to an Amazon S3 bucket. Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating:Wait state. Configure the function to call the SendCommand API to run the automation document. ✅ 👈 *(bạn chọn)*
- **B.** Change the interval at which the CloudWatch Logs agent sends data to 1 minute. Increase the deregistration delay of the Application Load Balancer. SSH into the instance to run the script for backing up the log data to an S3 bucket.
- **C.** Use an AWS Systems Manager Automation document to create the script for backing up log data to an Amazon S3 bucket. Create an OpsItem for EC2 termination events in AWS Systems Manager OpsCenter. Configure a remediation runbook that calls the CompleteLifecycleAction Auto Scaling API with ABANDON to pause the termination of instance and SendCommand System Manager API to run the automation document.
- **D.** Create a shell script for backing up log data to an S3 bucket. Install the script to the EC2 instance’s user data. Run the script using a Lambda function via Remote Call Procedure (RPC). Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating state.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

The EC2 instances in an Auto Scaling group have a path, or lifecycle, that differs from that of other EC2 instances. The lifecycle starts when the Auto Scaling group launches an instance and puts it into service. The lifecycle ends when you terminate the instance, or the Auto Scaling group takes the instance out of service and terminates it.

You can add a lifecycle hook to your Auto Scaling group so that you can perform custom actions when instances launch or terminate.

When Amazon EC2 Auto Scaling responds to a scale out event, it launches one or more instances. These instances start in the Pending state. If you added an autoscaling:EC2_INSTANCE_LAUNCHING lifecycle hook to your Auto Scaling group, the instances move from the Pending state to the Pending:Wait state. After you complete the lifecycle action, the instances enter the Pending:Proceed state. When the instances are fully configured, they are attached to the Auto Scaling group and they enter the InService state.

When Amazon EC2 Auto Scaling responds to a scale in event, it terminates one or more instances. These instances are detached from the Auto Scaling group and enter the Terminating state. If you added an autoscaling:EC2_INSTANCE_TERMINATING lifecycle hook to your Auto Scaling group, the instances move from the Terminating state to the Terminating:Wait state. After you complete the lifecycle action, the instances enter the Terminating:Proceed state. When the instances are fully terminated, they enter the Terminated state.

In the scenario, we can use AWS Auto Scaling lifecycle hooks, specifically the autoscaling:EC2_INSTANCE_TERMINATING event, to intercept the instance before termination. During this intercepted state, AWS Systems Manager Automation can run a script to backup logs to an Amazon S3 bucket. To automate this process, an Amazon EventBridge rule can be set to trigger a Lambda function when the instance enters the Terminating:Wait state. This Lambda function can then call the SendCommand API to run the automation document, ensuring that the logs are backed up before termination.

Hence, the correct answer is: Add a lifecycle hook to the Auto Scaling Group for the autoscaling:EC2_INSTANCE_TERMINATING event and set the default result to CONTINUE. Implement a script using an AWS Systems Manager Automation document to backup log data to an Amazon S3 bucket. Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating:Wait state. Configure the function to call the SendCommand API to run the automation document.

The option that says: Create a shell script for backing up log data to an S3 bucket. Install the script to the EC2 instance’s user data. Run the script using a Lambda function via Remote Call Procedure (RPC). Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating state is incorrect. This approach does not guarantee the script to be executed before the instance is terminated. Termination can occur very quickly, and it’s very likely that the script won’t have time to run and back up the logs.

The option that says: Change the interval at which the CloudWatch Logs agent sends data to 1 minute. Increase the deregistration delay of the Application Load Balancer. SSH into the instance to run the script for backing up the log data to an S3 bucket is incorrect. Having to SSH into instances manually isn’t a scalable or reliable solution. If there are many instances, or if the instances are frequently scaled in or out, this method becomes unmanageable. Moreover, it doesn’t provide a solution for automatic collection and backup of logs.

The option that says: Use an AWS Systems Manager Automation document to create the script for backing up log data to an Amazon S3 bucket. Create an OpsItem for EC2 termination events in AWS Systems Manager OpsCenter. Configure a remediation runbook that calls the CompleteLifecycleAction Auto Scaling API with ABANDON to pause the termination of instance and SendCommand System Manager API to run the automation document is incorrect. In this solution, the runbook remediation is triggered upon instance termination events. This means that the termination may have already proceeded past a point where it could be halted so the backup script can be executed. Moreover, the use of Systems Manager OpsCenter adds unnecessary complexity to the solution. OpsCenter is more oriented towards incident management rather than an operational activity like capturing logs.

 

References:

https://aws.amazon.com/blogs/infrastructure-and-automation/run-code-before-terminating-an-ec2-auto-scaling-instance/

https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/cloud-watch-events.html#terminate-successful

https://aws.amazon.com/premiumsupport/knowledge-center/auto-scaling-delay-termination/

 

Check out this AWS Auto Scaling Cheat Sheet:

https://tutorialsdojo.com/aws-auto-scaling/

---

## Câu 67 — ❌ SAI

### Câu hỏi

A company uses AWS Organizations to manage hundreds of AWS accounts. The company plans to designate a central network account where a shared VPC will be created. Accounts under the Customers Organization Unit (OU) are allowed to create resources on the shared VPC, but they should not be able to manage it.

The AWS Security Hub has also been configured to provide the company with a comprehensive view of their security state in AWS and to help them verify their AWS workloads against security industry standards and best practices. There’s also a Security Hub administrator account that has already been designated in AWS Organizations to view data from its member accounts.

Which combination of steps would meet the company’s objectives? (Select TWO.)

### Các phương án

- **A.** Create a separate VPC within each individual account in the Customers OU. Set up a Resource Access Manager (RAM) resource share for a Transit Gateway in the management account and share it with the Customers OU. Establish VPC peering connections between all VPCs.
- **B.** Create a service control policy (SCP) within AWS Organizations and attach it to the Customers OU. This SCP should contain statements for denying management actions to a VPC. 👈 *(bạn chọn)*
- **C.** Configure a managed prefix list in the central network account, specifying the IP ranges that align with the desired network configuration. Use AWS Resource Access Manager (RAM) to share this prefix list with the Customers OU.
- **D.** Configure the management account to enable AWS Resource Access Manager (RAM) resource sharing with AWS Organizations. ✅ 👈 *(bạn chọn)*
- **E.** Use AWS Resource Access Manager (RAM) to create a resource share in the management account. Include all subnets of the shared VPC and set the Customers OU as the principal. ✅

> **Bạn chọn:** B, D  
> **Đáp án đúng:** D, E  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Resource Access Manager (AWS RAM) helps you securely share your resources (e.g., AWS Transit Gateways, Subnets, AWS License Manager configurations) across AWS accounts, within your organization or organizational units (OUs), and with AWS Identity and Access Management (IAM) roles and users for supported resource types. If you have multiple AWS accounts, you can create a resource once and use AWS RAM to make that resource usable by those other accounts. If your account is managed by AWS Organizations, you can share resources with all the other accounts in the organization or only those accounts contained by one or more specified organizational units (OUs).

In this scenario, the company wants to have a central shared VPC that other AWS accounts can use, but not manage. We can use AWS RAM to achieve this. By enabling resource sharing with AWS Organizations from the management account, the company can share the resources, like subnets of the shared VPC, across the entire organization. Creating a resource share in the management account, including all subnets of the shared VPC, and setting the Customers OU as the principal would allow the accounts under the Customers OU to use the shared VPC without having the ability to manage it.

Hence, the correct answers are:

– Configure the management account to enable AWS Resource Access Manager (RAM) resource sharing with AWS Organizations.

– Use AWS Resource Access Manager (RAM) to create a resource share in the management account. Include all subnets of the shared VPC and set the Customers OU as the principal.

The option that says: Create a service control policy (SCP) within AWS Organizations and attach it to the Customers OU. This SCP should contain statements for denying management actions to a VPC is incorrect. SCPs are used to set fine-grained permissions for AWS Organizations and can indeed deny specific actions. However, in the context of a shared VPC using AWS RAM, it’s AWS RAM that manages the permissions, and the shared accounts do not have management permissions for the VPC by default. Therefore, denying VPC management actions via an SCP would be unnecessary in this scenario.

The option that says: Create a separate VPC within each individual account in the Customers OU. Set up a Resource Access Manager (RAM) resource share for a Transit Gateway in the management account and share it with the Customers OU. Establish VPC peering connections between all VPCs is incorrect. While this setup would enable network communication between all the accounts in the Customers OU, it doesn’t meet the company’s stated objective to use a central shared VPC. Furthermore, this approach would result in multiple VPCs that need to be individually managed rather than a single shared VPC, thus increasing complexity and potentially introducing configuration inconsistencies.

The option that says: Configure a managed prefix list in the central network account, specifying the IP ranges that align with the desired network configuration. Use AWS Resource Access Manager (RAM) to share this prefix list with the Customers OU is incorrect. Sharing a managed prefix list doesn’t prevent the individual accounts from managing the shared VPC, nor does it provide them with the ability to use a centrally managed shared VPC. The managed prefix list can control what IP ranges are allowed or denied access, but it doesn’t restrict the ability to create or manage resources within the VPC itself.

 

References:

https://docs.aws.amazon.com/ram/latest/userguide/what-is.html

https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/

 

Check out the AWS Resource Access Manager (RAM) Cheat Sheet:

https://tutorialsdojo.com/aws-resource-access-manager/

---

## Câu 68 — ❌ SAI

### Câu hỏi

A company hosts its application on a fleet of Amazon EC2 instances in an Auto Scaling group. The Quality Assurance (QA) team performs stress tests on the application. As part of the testing, several temporary environments are created from multiple AWS regions. With the current process, only the QA manager assumes an IAM role that has permission to use AWS CloudFormation, Amazon EC2, and Auto Scaling APIs. The QA manager launches CloudFormation stacks to create temporary environments. The upper management wants to make the testing process more efficient by allowing the QA members to create their own environments.

Which of the following options is the recommended action to allow the QA members to create their own temporary environments while following the principle of least privilege?

### Các phương án

- **A.** Use the environment templates to create applications in AWS Elastic Beanstalk. Grant the QA team’s IAM group permission to use only Elastic Beanstalk APIs. Instruct the QA members to use Elastic Beanstalk CLI for a secure and automated launching of multiple environments. 👈 *(bạn chọn)*
- **B.** Create a dedicated Amazon S3 bucket to store the AWS CloudFormation templates. Grant permissions for the QA members to assume the QA Manager’s IAM role but add restrictions to allow access to the templates and only the resources they created. Instruct the QA members to launch the templates using the CloudFormation console.
- **C.** Create multiple Amazon EC2 instances for each environment. Use AWS Systems Manager Automation runbook to configure the environments. Grant the QA team’s IAM group permission to use Amazon EC2 and AWS SSM APIs. Instruct the QA members to launch the environments by provisioning the EC2 instances.
- **D.** Create a product catalog that includes the AWS CloudFormation templates in AWS Service Catalog. Configure a launch constraint to the AWS Service Catalog product and grant the QA team’s IAM group permission to use Service Catalog APIs. Instruct the QA members to launch the templates using the AWS Service Catalog console only. ✅

> **Bạn chọn:** A  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for AWS. These IT services can include everything from virtual machine images, servers, software, databases, and more to complete multi-tier application architectures.

AWS Service Catalog allows organizations to centrally manage commonly deployed IT services and helps organizations achieve consistent governance and meet compliance requirements. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.

AWS Service Catalog supports the following types of users:

Catalog administrators (administrators) – Manage a catalog of products (applications and services), organizing them into portfolios and granting access to end users. Catalog administrators prepare AWS CloudFormation templates, configure constraints, and manage IAM roles for products to provide for advanced resource management.

End users – Receive AWS credentials from their IT department or manager and use the AWS Management Console to launch products to which they have been granted access. Sometimes referred to as simply users, end users may be granted different permissions depending on your operational requirements. For example, a user may have the maximum permission level (to launch and manage all of the resources required by the products they use) or only permission to use particular service features.

Therefore, the correct answer is: Create a product catalog that includes the AWS CloudFormation templates in AWS Service Catalog. Configure a launch constraint to the AWS Service Catalog product and grant the QA team’s IAM group permission to use Service Catalog APIs. Instruct the QA members to launch the templates using the AWS Service Catalog console only. With Service Catalog, the users can use CloudFormation templates to launch the environments. Access can be restricted by the Service Catalog administrator.

The option that says: Create a dedicated Amazon S3 bucket to store the AWS CloudFormation templates. Grant permissions for the QA members to assume the QA Manager’s IAM role but add restrictions to allow access to the templates and only the resources they created. Instruct the QA members to launch the templates using the CloudFormation console is incorrect. This is possible; however, it is not recommended. Assuming a role will mean that all resources will be created by that role. Therefore, all other members assuming the role will have access to all resources created by other team members.

The option that says: Create multiple Amazon EC2 instances for each environment. Use AWS Systems Manager Automation runbook to configure the environments. Grant the QA team’s IAM group permission to use Amazon EC2 and AWS SSM APIs. Instruct the QA members to launch the environments by provisioning the EC2 instances is incorrect. This approach would not be efficient or scalable, as it would require manual management of each EC2 instance. Also, it doesn’t take advantage of the automation and resource management features provided by AWS CloudFormation, which can simplify the process of creating and managing AWS resources.

The option that says: Use the environment templates to create applications in AWS Elastic Beanstalk. Grant the QA team’s IAM group permission to use only Elastic Beanstalk APIs. Instruct the QA members to use Elastic Beanstalk CLI for a secure and automated launching of multiple environments is incorrect. This may be possible but not recommended, as this will require converting the CloudFormation templates to Elastic Beanstalk applications. This is difficult to maintain and time-consuming in case you need to modify multiple EB applications.

 

References:

https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html

https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html

https://docs.aws.amazon.com/servicecatalog/latest/userguide/launch-stacksets.html

 

Check out this AWS Service Catalog Cheat Sheet:

https://tutorialsdojo.com/aws-service-catalog/

---

## Câu 69 — ❌ SAI

### Câu hỏi

An e-commerce company operates its core infrastructure within a private data center. This infrastructure is linked to AWS through a combination of AWS Direct Connect and a secure IPSec VPN, ensuring that sensitive customer data remains off the public internet. As part of its strategic growth, the company aims to extend its proprietary services to other e-commerce businesses hosted on AWS.

Which networking solution aligns with the company’s requirements?

### Các phương án

- **A.** Establish a VPC Endpoint Service for the company’s applications and associate it with a Network Load Balancer that manages TCP traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect. ✅
- **B.** Set up a NAT Gateway in a VPC for the company’s applications and secure it with network access control and security group rules.
- **C.** Set up a VPC Endpoint Service for the company’s applications and link it with an Application Load Balancer that handles HTTP or HTTPS traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect. 👈 *(bạn chọn)*
- **D.** Use AWS Direct Connect to link the company’s data center to a VPC in AWS. Within the VPC, set up security group rules to manage access to the company’s applications.

> **Bạn chọn:** C  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

A VPC Endpoint Service allows the company’s applications to be accessed securely within the AWS network. This is a crucial component in the solution as it enables the company’s services to be exposed to other businesses on AWS without exposing the data to the public internet. This is particularly important given the sensitive nature of the data handled by the company.

The Network Load Balancer operates at the fourth layer of the Open Systems Interconnection (OSI) model and can handle millions of requests per second. By efficiently managing TCP traffic, the Network Load Balancer ensures high availability and fault tolerance of the applications. This is critical for maintaining a high-quality user experience, especially as the company expands its services to other businesses on AWS.

AWS Direct Connect provides a dedicated, private link from the company’s data center to AWS. This ensures secure and efficient data transfer, which is vital for the company given the sensitive nature of its data. By maintaining a secure connection between the company’s data center and AWS using Direct Connect, the company can ensure that its sensitive data remains secure while still being able to extend its services to other businesses on AWS.

Hence, the correct answer is: Establish a VPC Endpoint Service for the company’s applications and associate it with a Network Load Balancer that manages TCP traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect.

The option that says: Set up a VPC Endpoint Service for the company’s applications and link it with an Application Load Balancer that handles HTTP or HTTPS traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect is incorrect because the Application Load Balancer cannot be used to create a VPC Endpoint Service. VPC Endpoint Services require Network Load Balancers.

The option that says: Use AWS Direct Connect to link the company’s data center to a VPC in AWS. Within the VPC, set up security group rules to manage access to the company’s applications is incorrect because it does not provide a way for the company to extend its services to other businesses on AWS. While AWS Direct Connect and security group rules provide secure connectivity and access control, they do not enable the company to expose its applications as services that other AWS users can consume.

The option that says: Set up a NAT Gateway in a VPC for the company’s applications and secure it with network access control and security group rules is incorrect because a NAT Gateway is used to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances. However, the question specifies that the company’s data cannot traverse the public internet. While network access control and security group rules add a layer of security, they do not provide the necessary private connectivity for the company’s sensitive data.

 

References:

https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.htmhttps://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html
https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

 

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/aws-direct-connect/
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

---

## Câu 70 — ✅ ĐÚNG

### Câu hỏi

A leading streaming service provider is utilizing GitHub Actions for the CI/CD pipeline, which orchestrates deployments across multiple AWS regions. The provider has been using an IAM user with an access key for authentication. An IAM role with the necessary permissions to manage Amazon S3 buckets is already in place.

Following a security audit, the provider’s security team requires the replacement of static IAM user keys with a dynamic, short-lived credential system. Additionally, the team wants to integrate GitHub Actions to automate the process of obtaining and using these dynamic credentials seamlessly. The solutions architect needs to comply with the new security policy and ensure the CI/CD pipeline remains functional and secure.

Which of the following options will meet the specified requirements while minimizing operational overhead?

### Các phương án

- **A.** Configure AWS Security Token Service (STS) to issue temporary security credentials that the GitHub Actions CI/CD pipeline can use for deployments.
- **B.** Configure AWS IAM Identity Center and integrate it with GitHub. Create an IAM role with the required permissions and assign it to a user group in AWS IAM Identity Center. Update GitHub Actions to authenticate using AWS IAM Identity Center credentials before executing deployments.
- **C.** Configure an IAM OpenID Connect (OIDC) Identity Provider (IdP) in AWS IAM, associated with GitHub. Create an IAM role with a trust policy for the sts:AssumeRoleWithWebIdentity AWS STS API calls from the GitHub OIDC IdP. Modify the GitHub Actions CI/CD pipeline to use this IAM role for its deployment processes. ✅ 👈 *(bạn chọn)*
- **D.** Configure Amazon Cognito as an OpenID Connect (OIDC) Identity Provider and create a Cognito user pool. Create an IAM role with a trust policy that allows sts:AssumeRoleWithWebIdentity for authentication through Cognito. Modify the GitHub Actions CI/CD pipeline to authenticate via Cognito and assume the IAM role for deployments.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

IAM OIDC identity providers are entities in IAM that describe an external identity provider (IdP) service supporting the OpenID Connect (OIDC) standard. You would use an IAM OIDC identity provider when you want to establish trust between an OIDC-compatible IdP and your AWS account. This is useful when creating a mobile app or web application that requires access to AWS resources. In this case, the streaming service provider needs to establish trust between GitHub (which is acting as the IdP) and their AWS account. This is done by configuring an IAM OIDC IdP in AWS IAM and associating it with GitHub.

After creating an IAM OpenID Connect (OIDC) identity provider, the next step is to create an IAM role with the sts:AssumeRoleWithWebIdentity action and a trust policy that allows GitHub Actions to assume the role securely. The sts:AssumeRoleWithWebIdentity action is an AWS Security Token Service (STS) API operation that allows a web identity (OIDC or SAML-based identity provider) to assume an IAM role and receive temporary security credentials. This action is commonly used when applications, third-party services (e.g., GitHub Actions, Kubernetes, mobile apps), or federated identities need access to AWS resources without requiring long-lived IAM credentials. The IAM role is dynamically assigned to a federated user that is authenticated by the organization’s IdP. The policies assigned to the role determine what the federated users are allowed to do in AWS.

GitHub Actions is a platform for continuous integration and continuous delivery (CI/CD). It enables you to automate your build, test, and deployment processes. With GitHub Actions, you can create workflows to build and test every pull request to your repository and deploy merged pull requests to production. In this case, the streaming service provider is using GitHub Actions for their CI/CD pipeline. After creating the IAM role, the GitHub Actions CI/CD pipeline needs to be updated to assume this IAM role for deployments.

This approach not only adheres to the new security policy by replacing static IAM user keys with a dynamic credential system but also leverages existing AWS services, thereby minimizing operational overhead. It ensures secure and authenticated communication between GitHub and AWS services, facilitating reliable deployment workflows. This solution is in line with best practices for managing access keys and enhancing security in AWS environments.

Hence, the correct answer is: Configure an IAM OpenID Connect (OIDC) Identity Provider (IdP) in AWS IAM, associated with GitHub. Create an IAM role with a trust policy for the sts:AssumeRoleWithWebIdentity AWS STS API calls from the GitHub OIDC IdP. Modify the GitHub Actions CI/CD pipeline to use this IAM role for its deployment processes.

The option that says: Configure AWS IAM Identity Center and integrate it with GitHub. Create an IAM role with the required permissions and assign it to a user group in AWS IAM Identity Center. Update GitHub Actions to authenticate using AWS IAM Identity Center credentials before executing deployments is incorrect because AWS IAM Identity Center is primarily designed for human user authentication and does not natively support workload-to-workload authentication, such as GitHub Actions assuming a role. AWS IAM Identity Center requires interactive authentication via a web-based login, which is not feasible for an automated CI/CD pipeline. The correct approach is to use IAM OIDC with GitHub for seamless and automated authentication.

The option that says: Configure Amazon Cognito as an OpenID Connect (OIDC) Identity Provider and create a Cognito user pool. Create an IAM role with a trust policy that allows sts:AssumeRoleWithWebIdentity for authentication through Cognito. Modify the GitHub Actions CI/CD pipeline to authenticate via Cognito and assume the IAM role for deployments is incorrect because Amazon Cognito is primarily used for user authentication in applications, not for service-to-service authentication like GitHub Actions. Cognito user pools are designed for managing human users, and it does not provide a seamless way for GitHub Actions to assume an IAM role dynamically. This adds unnecessary complexity and does not align with AWS best practices for CI/CD authentication.

The option that says: Configure AWS Security Token Service (STS) to issue temporary security credentials that the GitHub Actions CI/CD pipeline can use for deployments is incorrect because while AWS STS does provide temporary security credentials, it does not specify how these credentials are associated with an IAM role. The CI/CD pipeline needs to assume an IAM role with the necessary permissions for deployments, and this option does not address that requirement.

 

References:

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html

https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html

https://aws.amazon.com/blogs/devops/integrating-with-github-actions-ci-cd-pipeline-to-deploy-a-web-app-to-amazon-ec2/

 

Check out this AWS Identity and Access Management Cheat Sheet:

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

---

## Câu 71 — ✅ ĐÚNG

### Câu hỏi

A company has integrated AWS Directory Service for Microsoft Active Directory with its on-premises Active Directory.

The company wants to grant employees access to internal applications hosted within its AWS Virtual Private Cloud (VPC) from any geographical location. The company’s security protocols mandate that access to these resources must be via a VPN, which requires multi-factor authentication (MFA).

Which solution in the following options should a solutions architect implement to comply with these requirements?

### Các phương án

- **A.** Configure two or more AWS Site-to-Site VPN connections using AWS VPN CloudHub. Integrate AWS VPN CloudHub with AWS Directory Service for Microsoft Active Directory and utilize AWS Copilot to establish the VPN connections.
- **B.** Integrate AWS Site-to-Site VPN with AWS Directory Service for Microsoft Active Directory and use Amazon WorkSpaces with Multi-Factor Authentication enabled for the VPN connection.
- **C.** Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via AWS Direct Connect and enable Multi-Factor Authentication for the VPN connections.
- **D.** Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via the AD Connector for the VPN connection, and enable Multi-Factor Authentication for the AD Connector. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Directory Service is a managed service that makes it easy to set up and run Microsoft Active Directory (AD) in the AWS cloud or connect your AWS resources to an existing on-premises Microsoft AD.

AWS Directory Service supports several directory types:

– Simple AD allows you to easily launch a new Active Directory forest in the AWS cloud.

– Microsoft AD allows you to run an existing on-premises AD in the AWS cloud.

– AD Connector allows you to connect your AWS resources to an existing on-premises AD.

– Amazon Cognito is an AWS service that helps you manage user sign-up, authentication, and account management for your mobile and web applications.

It reduces the need for complex directory administration. The directories are automatically deployed across Availability Zones for high availability. AWS handles daily backups and software patching.

It allows you to integrate your directories with other AWS services, such as Amazon WorkSpaces, Amazon WorkMail, etc., for user management and access control. You can enable access to these services from the AWS Directory Service console.

The directories store information about users, groups, devices, etc., and administrators can use them to centrally manage access to information and resources across AWS accounts and services.

AWS Client VPN is a service that allows you to securely connect to your AWS resources and your on-premises network from any location. It is a client-based VPN service that uses an OpenVPN-based VPN client to enable easy access to your resources. With Client VPN, you can ensure your connection is always secure and reliable.

Using AWS Directory Service in conjunction with AD Connector allows for seamless single sign-on for users. The AWS Client VPN endpoint creates a secure IPsec VPN tunnel between the on-premises network and the VPC. Enabling Multi-Factor Authentication (MFA) on the Active Directory (AD) connector ensures that only authorized and authenticated users can access resources within the Virtual Private Cloud (VPC). These measures work together to provide a secure and hassle-free way for employees to access internal applications from anywhere while complying with the company’s security protocols for VPN access and MFA.

Hence, the correct answer is: Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via the AD Connector for the VPN connection, and enable Multi-Factor Authentication for the AD Connector.

The option that says: Integrate AWS Site-to-Site VPN with AWS Directory Service for Microsoft Active Directory and use Amazon WorkSpaces with Multi-Factor Authentication enabled for the VPN connection is incorrect because AWS Site-to-Site VPN is only designed for connecting entire networks to each other, rather than providing individual user access.

The option that says: Configure two or more AWS Site-to-Site VPN connections using AWS VPN CloudHub. Integrate AWS VPN CloudHub with AWS Directory Service for Microsoft Active Directory and utilize AWS Copilot to establish the VPN connections is incorrect because it overcomplicates the solution. AWS VPN CloudHub is generally used for multiple site-to-site connections and does not directly address the need for individual secure remote access with MFA.

The option that says: Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via AWS Direct Connect and enable Multi-Factor Authentication for the VPN connections is incorrect. While integrating AWS Client VPN with AWS Directory Service for Microsoft Active Directory is feasible, doing so through AWS Direct Connect is unconventional for this purpose, as Direct Connect is primarily used for establishing a dedicated network link, not for securing or managing VPN connections.

 

References:

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html

https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html

 

Check out this AWS Directory Service Cheat Sheet:

https://tutorialsdojo.com/aws-directory-service/

---

## Câu 72 — ❌ SAI

### Câu hỏi

An IT company provides on-demand video training materials to its employees. High-resolution MP4 format videos are created monthly to increase the topics covered in the video library. Most employees that will view the videos are working remotely from different countries. The video application installed on the employee laptops requires the videos to be in HTTP Live Streaming (HLS) format. The management asked the solutions architect to design a cost-effective solution that will transcode the training videos into the proper format.

Which of the following architectures meet the above requirements while maintaining high availability and good quality video transmission?

### Các phương án

- **A.** Create a pipeline in AWS CodePipeline with stages that transcode the high-resolution MP4 videos into the HLS format and send the transcoded videos to an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Then, set up an endpoint in AWS Wavelength and configure it to serve the transcoded videos from the S3 bucket.
- **B.** Create a pipeline on Amazon Elastic Transcoder to transcode the high-resolution MP4 videos into the HLS format. Host the transcoded videos on large EBS volumes attached to Amazon EC2 instances. Configure automated EBS snapshots to back up the video files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos.
- **C.** Create a Jenkins pipeline to transcode the high-resolution MP4 videos. Use an SQS queue to distribute the transcoding job to a set of Amazon EC2 instances in an Auto Scaling group that scales based on the length of the queue. Store the transcoded videos on EBS volumes and configure automated snapshots to back up the files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos. 👈 *(bạn chọn)*
- **D.** Create a queue in AWS Elemental MediaConvert to transcode the high-resolution MP4 videos into the HLS format. Store the transcoded videos on an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Create an Amazon CloudFront distribution and set the S3 bucket as the origin to serve the transcoded videos. ✅

> **Bạn chọn:** C  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

AWS Elemental MediaConvert is a file-based video transcoding service with broadcast-grade features. It provides a comprehensive suite of advanced transcoding features with on-demand rates. It allows you to easily create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale. The service combines advanced video and audio capabilities with a simple web services interface and pay-as-you-go pricing. With AWS Elemental MediaConvert, you can focus on delivering compelling media experiences without having to worry about the complexity of building and operating your own video processing infrastructure. MediaConvert is optimized to improve scalability, which allows you to process more files in parallel.

Amazon Elastic Transcoder uses pipelines to manage transcoding jobs. When you create a job, you specify the pipeline that you want to submit the job to. Pipelines are closely tied to an S3 bucket that you specify. Queues in AWS Elemental MediaConvert are similar to pipelines. The number of concurrent jobs processed in a given queue is determined based on the number of queues in your account. However, one of the key differences is that queues are not tied to a specific S3 bucket. This means that you can submit jobs that reference input files in different S3 buckets to the same queue. In Elastic Transcoder, you select the playlist version upon job creation. In MediaConvert, the HLS version will change as you enable features that require a specific version.

Therefore, the correct answer is: Create a queue in AWS Elemental MediaConvert to transcode the high-resolution MP4 videos into the HLS format. Store the transcoded videos on an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Create an Amazon CloudFront distribution and set the S3 bucket as the origin to serve the transcoded videos. AWS Elemental MediaConvert is a new file-based video transcoding service aimed to replace Amazon Elastic Transcoder. Additionally, storing the transcoded videos on S3 buckets is highly durable and cost-effective, as you don’t have to pay for EC2 instance costs.

The option that says: Create a Jenkins pipeline to transcode the high-resolution MP4 videos. Use an SQS queue to distribute the transcoding job to a set of Amazon EC2 instances in an Auto Scaling group that scales based on the length of the queue. Store the transcoded videos on EBS volumes and configure automated snapshots to back up the files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos is incorrect. AWS has managed services to automate video transcoding for you. Additionally, using large EBS volumes to store the transcoded videos is not very cost-effective compared to using an S3 bucket.

The option that says: Create a pipeline on Amazon Elastic Transcoder to transcode the high-resolution MP4 videos into the HLS format. Host the transcoded videos on large EBS volumes attached to Amazon EC2 instances. Configure automated EBS snapshots to back up the video files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos is incorrect. This may be possible, however, using large EBS volumes to store the transcoded videos is not very cost-effective compared to using an S3 bucket. Additionally, the performance of the EC2 instance may vary depending on the traffic load.

The option that says: Create a pipeline in AWS CodePipeline with stages that transcode the high-resolution MP4 videos into the HLS format and send the transcoded videos to an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Then, set up an endpoint in AWS Wavelength and configure it to serve the transcoded videos from the S3 bucket is incorrect. AWS CodePipeline is primarily designed for CI/CD pipelines to deploy new application versions. You can’t directly create a stage that will transcode videos to a specific format. Moreover, AWS Wavelength is designed to provide ultra-low latency for applications on 5G networks. It’s ideal for applications that require minimal latency over mobile networks. However, in your scenario, the employees are located in various countries and may not necessarily be using 5G networks.

 

References:

https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/

https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-s3-glacier-storage-class-amazon-s3-glacier-flexible-retrieval/

 

Check out this Amazon CloudFront Cheat Sheet:

https://tutorialsdojo.com/amazon-cloudfront/

---

## Câu 73 — ❌ SAI

### Câu hỏi

A company has a marketing service that schedules and posts content on a social media platform. The service currently runs on a collection of Amazon EC2 instances within an Auto Scaling group behind an Application Load Balancer (ALB). This ALB responds to webhook calls from the social media platform when specific events occur, such as mentions, shares, or specific hashtag uses. The company wants to migrate this service to a serverless architecture to lessen administrative overhead.

Which action would be the most operationally efficient way to meet the requirements?

### Các phương án

- **A.** Run the service using AWS Lambda. Generate a Lambda Function URL for each webhook. Configure the platform to send webhook calls to the function URLs. ✅
- **B.** Use AWS Lambda to run the service. Create a single AWS AppSync GraphQL API endpoint and connect it to the Lambda functions. Configure the platform to send webhook calls to the AppSync endpoint.
- **C.** Run the service using AWS Lambda. Create an Amazon Gateway REST API that uses proxy integration with AWS Lambda. Create an API resource for each webhook. Configure the platform to send webhook calls to the REST API endpoint.
- **D.** Replace the Amazon EC2 instances with AWS Fargate tasks. Create an Amazon Gateway HTTP API and integrate it with the Application Load Balancer. Configure the platform to send webhook calls to the HTTP API endpoint. 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

Lambda function URLs are HTTP(S) endpoints dedicated to your Lambda function. You can easily create and set up a function URL using the Lambda console or API. Once created, Lambda generates a unique URL endpoint for your use.

Function URLs are dual stack-enabled, supporting IPv4 and IPv6. After you configure a function URL for your function, you can invoke your function through its HTTP(S) endpoint via a web browser, curl, Postman, or any HTTP client.

In the scenario, exposing Lambda functions directly using function URLS eliminates the need for intermediaries like Amazon API Gateway. This approach significantly simplifies the architecture, reduces latency, and lessens administrative overhead. Each webhook can be configured to send calls to specific Lambda function URLs, providing a response mechanism for various social media events.

Hence, the correct answer is: Run the service using AWS Lambda. Generate a Lambda Function URL for each webhook. Configure the platform to send webhook calls to the function URLs.

The option that says: Use AWS Lambda to run the service. Create a single AWS AppSync GraphQL API endpoint and connect it to the Lambda functions. Configure the platform to send webhook calls to the AppSync endpoint is incorrect. AWS AppSync is a just managed service that uses GraphQL to make it easy for applications to get exactly the data they need. While you can use it with Lambda, this solution is not as straightforward as directly triggering Lambda functions using function URLs. Using AppSync might introduce unnecessary complexity for this use case which is about responding to webhook calls from a social media platform, not handling GraphQL queries from a client application.

The option that says: Replace the Amazon EC2 instances with AWS Fargate tasks. Create an Amazon Gateway HTTP API and integrate it with the Application Load Balancer. Configure the platform to send webhook calls to the HTTP API endpoint is incorrect. While AWS Fargate is a serverless compute engine for containers, it wouldn’t be the most efficient choice in the scenario. Using Fargate would require you to containerize the application, which adds an additional layer of development and management overhead

The option that says: Run the service using AWS Lambda. Create an Amazon Gateway REST API that uses proxy integration with AWS Lambda. Create an API resource for each webhook. Configure the platform to send webhook calls to the REST API endpoint is incorrect. Although this option could work, it introduces additional complexity by using Amazon API Gateway as an intermediary. In this scenario, a fully-fledged REST API is not necessary. Instead of creating an API resource for each webhook, it would be simpler and more efficient to directly trigger specific AWS Lambda functions thru Lambda function URLs.

 

References:

https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html

https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html

 

Check out this AWS Lambda Cheat Sheet:

https://tutorialsdojo.com/aws-lambda/

---

## Câu 74 — ❌ SAI

### Câu hỏi

A company recently migrated a legacy application from a data center to AWS. The application, which is hosted on an EC2 instance, uses a Simple Mail Transfer Protocol (SMTP) server for sending promotional emails. The application communicates with the SMTP server over port 25 without TLS encryption. As part of its replatforming strategy, the company has opted to replace the SMTP server with Amazon Simple Email Service (SES). The SES domain is already created and has been validated.

What steps should be taken next to enable communication between the application and Amazon SES?

### Các phương án

- **A.** Create an IAM Role for the application with ses:SendEmail and ses:SendRawEmail permissions and attach it to the EC2 instance. Update the SMTP settings in the application to connect to the Amazon SES SMTP. Update the port number to 465 to use TLS Wrapper. 👈 *(bạn chọn)*
- **B.** Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential. Use the AWS SDK for Amazon SES to send emails.
- **C.** Create an IAM user and grant it permission to send emails through Amazon SES. Generate access keys for this IAM user. Update the application to use these access keys and connect to the Amazon SES SMTP endpoint. Change the port to 587 to use STARTTLS.
- **D.** Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential and update the connection to the Amazon SES SMTP endpoint. Change the port settings to 587 to use STARTTLS. ✅

> **Bạn chọn:** A  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon Simple Email Service (Amazon SES) is a scalable and secure cloud-based email-sending service designed to help businesses send marketing, transactional, and other types of professional emails.

The Amazon SES SMTP endpoint requires that all connections be encrypted using Transport Layer Security (TLS). Amazon SES supports two mechanisms for establishing a TLS-encrypted connection: STARTTLS and TLS Wrapper.

STARTTLS is a means of upgrading an unencrypted connection to an encrypted connection. To set up a STARTTLS connection, the SMTP client connects to the Amazon SES SMTP endpoint on port 25, 587, or 2587, issues an EHLO command, and waits for the server to announce that it supports the STARTTLS SMTP extension. The client then issues the STARTTLS command, initiating TLS negotiation. When negotiation is complete, the client issues an EHLO command over the new encrypted connection, and the SMTP session proceeds normally.

Amazon SES supports sending emails through two main interfaces: the Simple Mail Transfer Protocol (SMTP) and the SES API.

In the scenario, since the company’s legacy application is already configured to connect to an SMTP server, they can simply replace the existing SMTP settings with those of Amazon SES. This involves generating new SMTP credentials via the Amazon SES console and updating the application to use them. Additionally, it is recommended to switch from the currently used port 25 to port 587 for STARTTLS encryption. This is beneficial not only for enhanced security but also because Amazon EC2 instances are throttled on port 25, and using port 587 avoids the need to request the lifting of these limitations.

Hence, the correct answer is: Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential and update the connection to the Amazon SES SMTP endpoint. Change the port settings to 587 to use STARTTLS.

When using the SMTP interface to send email through Amazon SES, SMTP credentials should be used, and not IAM roles or IAM user credentials. SMTP credentials are separate and are used specifically for connecting to the Amazon SES SMTP interface. Thus, the following options are incorrect:

– Create an IAM Role for the application with ses:SendEmail and ses:SendRawEmail permissions and attach it to the EC2 instance. Update the SMTP settings in the application to connect to the Amazon SES SMTP. Update the port number to 465 to use TLS Wrapper.

– Create an IAM user and grant it permission to send emails through Amazon SES. Generate access keys for this IAM user. Update the application to use these access keys and connect to the Amazon SES SMTP endpoint. Change the port to 587 to use STARTTLS.

The option that says: Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential. Use the AWS SDK for Amazon SES to send emails  is incorrect. This approach would mean that you’re sending through the API and not through the SMTP interface. This would require the application to use AWS access key credentials, either from an IAM role attached to the EC2 instance or from an IAM user, not an SMTP credential.

References:

https://docs.aws.amazon.com/ses/latest/DeveloperGuide/security.html

https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-connect.html

https://docs.aws.amazon.com/ses/latest/dg/send-using-smtp-programmatically.html

 

Check out this Amazon SES Cheat Sheet:

https://tutorialsdojo.com/amazon-ses/

---

## Câu 75 — ✅ ĐÚNG

### Câu hỏi

A company is using AWS Organizations to manage multiple AWS accounts, each belonging to a different department within the organization. As part of a new cloud spending strategy, the company wants to implement a billing reporting system with the following requirements:

Each department head must receive email notifications if their account’s spending exceeds a predefined threshold.

Each department head should receive a monthly billing report of their respective account.

The company is looking for a centralized, cost-effective solution.

Which of the following options achieves these requirements in the most cost-effective manner?

### Các phương án

- **A.** In each department account, configure AWS Budgets to set spending thresholds and send SNS alerts to department leaders when limits are breached. Use AWS Cost Explorer within each department account to generate monthly billing reports
- **B.** In each department account, enable AWS Cost and Usage Reports (CUR) to capture detailed billing data. Use an AWS Lambda function in each department account to analyze CUR data and trigger Amazon SNS notifications to the department leaders when spending thresholds are breached
- **C.** Enable cost allocation tags in the management account and apply them to departmental resources. Use AWS Cost and Usage Reports (CUR) to filter expenses by tags. In each department account, set up AWS Lambda to analyze CUR data and trigger SNS alerts for cost overruns.
- **D.** In the management account, use AWS Budgets with budget filters to set spending thresholds for each member account. Configure these alerts to send email notifications to department heads. Use AWS Cost Explorer to generate monthly billing reports for each member account. ✅ 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Budgets allows you to set custom budgets to track your AWS spending, and it can alert you via email or SNS notifications if your costs exceed or are projected to exceed your budget. AWS Cost Explorer is a tool that provides detailed information about your AWS costs and usage, enabling you to visualize and understand your spending patterns.

In the scenario, using AWS Budgets in the management account offers a centralized way to manage and monitor spending across multiple departmental accounts. You can create budget alerts specifically for each member account using budget filters, fulfilling the requirement to notify department heads when spending exceeds predefined thresholds.

Alongside this, AWS Cost Explorer can be filtered by linked accounts to generate monthly billing reports, providing each department head with a detailed understanding of their respective account’s spending.

Hence, the correct answer in this scenario is: In the management account, use AWS Budgets with budget filters to set spending thresholds for each member account. Configure these alerts to send email notifications to department heads. Use AWS Cost Explorer to generate monthly billing reports for each member account.

The option that says: In each department account, enable AWS Cost and Usage Reports (CUR) to capture detailed billing data. Use an AWS Lambda function in each department account to analyze CUR data and trigger Amazon SNS notifications to the department leaders when spending thresholds are breached is incorrect because this is not a centralized approach. This is also more complicated to implement and incurs additional costs due to the use of Lambda functions to process billing data.

The option that says: Enable cost allocation tags in the management account and apply them to departmental resources. Use AWS Cost and Usage Reports (CUR) to filter expenses by tags. In each department account, set up AWS Lambda to analyze CUR data and trigger SNS alerts for cost overruns is incorrect. Cost allocation tags are particularly useful when you need granular visibility into your AWS spending. They allow you to attribute costs to specific projects, departments, or other categories within your organization. However, if the primary goal is simply to monitor overall spending at the account level, then cost allocation tags may introduce unnecessary complexity. Moreover, this approach would require ongoing maintenance to ensure that all new resources are correctly tagged for cost allocation.

The option that says: In each department account, configure AWS Budgets to set spending thresholds and send SNS alerts to department leaders when limits are breached. Use AWS Cost Explorer within each department account to generate monthly billing reports is incorrect. This is a viable solution but it uses a decentralized approach. This means that each department account would have to separately manage its own AWS Budgets and Cost Explorer settings.

 

References:

https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html

https://docs.aws.amazon.com/cost-management/latest/userguide/ce-access.html

https://aws.amazon.com/blogs/mt/manage-cost-overruns-part-1/

 

Check out this AWS Billing and Cost Management Cheat Sheet:

https://tutorialsdojo.com/aws-billing-and-cost-management/

---
