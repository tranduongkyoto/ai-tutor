# Mixed Unseen Mock #1 — source (TD layout)

## Question 1

**Category:** CSAP – Continuous Improvement for Existing Solutions

An analytics company wants to leverage ElastiCache for Redis in cluster mode to enhance the performance and scalability of its existing two-tier application architecture. The ElastiCache cluster is configured to listen on port 6379. The company has hired you as an AWS Certified Solutions Architect Professional to build a secure solution so that the cache data is secure and protected from unauthorized access.

Which of the following steps would address the given use-case? (Select three)

- **A. Configure the security group for the ElastiCache cluster with the required rules to allow inbound traffic from the cluster itself as well as from the cluster's clients on port 6379** ✅
- **B. Configure the ElastiCache cluster to have both in-transit as well as at-rest encryption** ✅
- C. Enable CloudTrail to monitor the API Calls for the ElastiCache cluster
- D. Enable CloudWatch Logs to monitor the security credentials for the ElastiCache cluster
- E. Configure the security group for the ElastiCache cluster with the required rules to allow outbound traffic to the cluster's clients on port 6379
- **F. Create the cluster with auth-token parameter and make sure that the parameter is included in all subsequent commands to the cluster** ✅

### Explanation

Correct options:

Configure the ElastiCache cluster to have both in-transit as well as at-rest encryption

You can use both in-transit as well as at-rest encryption to guard against unauthorized access of your data on the server. In-transit encryption encrypts your data whenever it is moving from one place to another, such as between nodes in your cluster or between your cluster and your application. At-rest encryption encrypts your on-disk data during sync and backup operations.


via - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/encryption.html

Create the cluster with auth-token parameter and make sure that the parameter is included in all subsequent commands to the cluster

Redis authentication tokens enable Redis to require a token (password) before allowing clients to run commands, thereby improving data security. You can require that users enter a token on a token-protected Redis server. You also need to include it in all subsequent commands to the replication group or cluster.


via - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html

Configure the security group for the ElastiCache cluster with the required rules to allow inbound traffic from the cluster itself as well as from the cluster's clients on port 6379

You can create a VPC security group to restrict access to the cluster instances. Configure rules that only allow inbound traffic from the cluster itself as well as from the cluster's clients on port 6379. Typically the ElastiCache cluster is accessed from the web servers running on EC2 instances. You can configure the security groups like so:


via - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-vpc-accessing.html

Incorrect options:

Configure the security group for the ElastiCache cluster with the required rules to allow outbound traffic to the cluster's clients on port 6379 - As mentioned in the explanation above, you need to create a security group that allows inbound traffic from the cluster itself as well as from the cluster's clients on port 6379. Creating a security group rule that allows outbound traffic from the cluster on port 6379 is not relevant to the use-case.

Enable CloudWatch Logs to monitor the security credentials for the ElastiCache cluster

Enable CloudTrail to monitor the API Calls for the ElastiCache cluster

Both these options are added as distractors since both CloudWatch Logs and CloudTrail can be used for post-facto analysis to ascertain the series of access events relevant to the cluster. These options will not prevent unauthorized access.

References:

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/encryption.html

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-vpc-accessing.html

---

## Question 2


**Category:** CSAP – Continuous Improvement for Existing Solutions

A research company specializing in agricultural innovation operates a fleet of IoT devices across experimental farms to automate and monitor water distribution, temperature regulation, and humidity control. The collected telemetry data is stored in Optimized Row Columnar (ORC) format within the Hadoop Distributed File System (HDFS), running on a persistent Amazon EMR cluster. The company’s data analytics team runs SQL queries using Apache Presto on the same always-on EMR environment. These queries scan large datasets, complete within 15 minutes, and are executed only between 6 PM and 2 AM as part of the company’s nightly analysis routine.
With cloud costs climbing, the research company’s leadership seeks a more cost-effective solution to support these recurring SQL-based data queries. A solutions architect must recommend the most economical approach while maintaining query performance and compatibility with the existing ORC data format.
What is the most cost-effective recommendation that the solutions architect can make?

- **A. Persist data in Amazon S3, and execute SQL-based analytics through Amazon Athena, using schema definitions stored in the AWS Glue Data Catalog.** ✅
- B. Load your datasets into Amazon Redshift and perform analytics directly within the Redshift data warehouse environment.
- C. Use AWS Glue ETL jobs to ingest the ORC files into Amazon Aurora and enable SQL-based querying.
- D. Use AWS Lambda functions to convert the ORC files into JSON and store them in Amazon DynamoDB for querying.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds.
Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. Athena scales automatically, running queries in parallel, so results are fast, even with large datasets and complex queries.

Athena can read data directly from Amazon S3 in ORC format, making it highly compatible with the company’s existing dataset. The AWS Glue Data Catalog serves as the centralized metadata store, allowing Athena to interpret and query the structure of the ORC files. Since the research company only needs to run queries during a narrow time window each night, keeping a persistent EMR cluster active is simply wasteful. Athena is cost-effective because the company is billed just for the data scanned per query, and the infrastructure does not need to run continuously, reducing compute-related expenses.
Hence, the correct answer is: Persist data in Amazon S3, and execute SQL-based analytics through Amazon Athena, using schema definitions stored in the AWS Glue Data Catalog.
The option that says: Load your datasets into Amazon Redshift and perform analytics directly within the Redshift data warehouse environment is incorrect. Amazon Redshift is a provisioned data warehouse that incurs ongoing compute and storage costs, regardless of whether queries are being executed. It is primarily designed for high-throughput, continuous analytical workloads, not intermittent query patterns that only occur during a specific time window. Additionally, Redshift does not natively support querying ORC files stored in HDFS. The data must be loaded into Redshift tables, introducing unnecessary overhead.
The option that says: Use AWS Glue ETL jobs to ingest the ORC files into Amazon Aurora and enable SQL-based querying is incorrect. Amazon Aurora is a relational database optimized for transactional workloads, not for large-scale analytics on ORC-formatted files. Using AWS Glue ETL jobs to transform and load ORC data into Aurora introduces processing and storage costs that are simply unnecessary for the use case. Aurora does not support the high-volume data scanning common in big data SQL workloads, making this solution technically inappropriate and financially inefficient.
The option that says: Use AWS Lambda functions to convert the ORC files into JSON and store them in Amazon DynamoDB for querying is incorrect. Amazon DynamoDB is a NoSQL key-value and document database optimized primarily for low-latency, high-throughput transactional operations, not for complex SQL-based analytics across large datasets. Converting ORC files to JSON introduces unnecessary transformation overhead, and using Lambda for this task is simply unsuitable due to its memory and execution time limits, especially when handling large ORC files. Additionally, DynamoDB does not support SQL or efficient data scanning for analytical queries, making this solution technically invalid and economically impractical for the company’s use case.
 
References:
https://docs.aws.amazon.com/athena/latest/ug/what-is.html
https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html
 
Check out this Amazon Athena Cheat Sheet:
https://tutorialsdojo.com/amazon-athena/

---

## Question 3

**Category:** CSAP – Accelerate Workload Migration and Modernization

A legacy web application runs 24/7 and it is currently hosted on an on-premises server with an outdated version of the Operating System (OS). The OS support will end soon and the team wants to expedite migration to an Amazon EC2 instance with an updated version of the OS. The application also references 90 TB of static data in the form of images that need to be moved to AWS.

How should this be accomplished most cost-effectively?

- A. Use AWS Application Migration Service to migrate the application and all its data to Amazon EC2 instance
- **B. Replatform the server to Amazon EC2 while choosing an AMI of your choice to cater to the OS requirements. Use AWS Snowball to transfer the image data to Amazon S3** ✅
- C. Set up the application on AWS Fargate for a serverless solution and use AWS Snowball to transfer the image data to Amazon S3
- D. Use AWS Direct Connect to establish a dedicated connection between on-premises systems and AWS. Transfer data to Amazon S3 using this link. Migrate the application to Amazon EC2 instance

### Explanation

Correct option:

Replatform the server to Amazon EC2 while choosing an AMI of your choice to cater to the OS requirements. Use AWS Snowball to transfer the image data to Amazon S3

Re-platforming the server to Amazon EC2 instances is the best choice here since the use case speaks about updating the existing operating system. Amazon provides pre-configured AMIs to choose different flavors of OS to cater to each requirement. Also, Amazon EC2 is the least expensive of all options.

Key differences between Rehosting and Replatforming:

via - https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

AWS Snowball, a part of the AWS Snow Family, is an edge computing, data migration, and edge storage device that comes in two options. Snowball Edge Storage Optimized devices provide both block storage and Amazon S3-compatible object storage, and 40 vCPUs. They are well suited for local storage and large-scale data transfer.

Amazon Snowball is a data transport solution that accelerates moving terabytes to petabytes of data into and out of Amazon Web Services services using storage devices designed to be secure for physical transport. Using Snowball helps to eliminate challenges that can be encountered with large-scale data transfers including high network costs, long transfer times, and security concerns.

Snowball is the right data transfer choice if you need to securely and quickly transfer terabytes to many petabytes of data to Amazon Web Services services. Snowball can also be the right choice if you don’t want to make expensive upgrades to your network infrastructure.

Finally, transfer the image data from Snowball to Amazon S3, which is the most cost-effective storage solution offered on AWS, when combined with lifecycle policies to further accelerate cost savings.

Incorrect options:

Use AWS Direct Connect to establish a dedicated connection between on-premises systems and AWS. Transfer data to Amazon S3 using this link. Migrate the application to Amazon EC2 instance - AWS Direct Connect is an overkill for a one-time migration requirement. Also, Direct Connect takes time to provision and is cost-prohibitive for this use case.

Set up the application on AWS Fargate for a serverless solution and use AWS Snowball to transfer the image data to Amazon S3 - AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). AWS Fargate makes it easy to focus on building your applications. Using Fargate implies changing the architecture of the solution, so it would need separate development effort along with the associated cost. In addition, Fargate is costlier than hosting on Amazon EC2 instance when the application runs 24/7 - as mentioned in the given use case.

Use AWS Application Migration Service to migrate the application and all its data to Amazon EC2 instance - AWS Application Migration Service (AWS MGN) is the primary migration service recommended to lift and shift your applications to AWS. Customers considering CloudEndure Migration are encouraged to use AWS Application Migration Service for future migrations. For the current use case, we are not only looking for lift and shift but for replatforming too. Hence, this option is incorrect.

References:

https://aws.amazon.com/snowball/

https://aws.amazon.com/application-migration-service/

https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

https://blogs.perficient.com/2021/06/17/aws-cost-analysis-comparing-lambda-ec2-fargate/

---

## Question 4

**Category:** CSAP – Continuous Improvement for Existing Solutions

A social media company has a serverless application stack that consists of CloudFront, API Gateway and Lambda functions. The company has hired you as an AWS Certified Solutions Architect Professional to improve the current deployment process which creates a new version of the Lambda function and then runs an AWS CLI script for deployment. In case the new version errors out, then another CLI script is invoked to deploy the previous working version of the Lambda function. The company has mandated you to decrease the time to deploy new versions of the Lambda functions and also reduce the time to detect and rollback when errors are identified.

Which of the following solutions would you suggest for the given use-case?

- A. Set up and deploy a CloudFormation stack containing a new API Gateway endpoint that points to the new Lambda version. Test the updated CloudFront origin that points to this new API Gateway endpoint and in case errors are detected then revert the CloudFront origin to the previous working API Gateway endpoint
- B. Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. Use pre-traffic and post-traffic test functions of the change set to verify the deployment. Rollback in case CloudWatch alarms are triggered
- **C. Use Serverless Application Model (SAM) and leverage the built-in traffic-shifting feature of SAM to deploy the new Lambda version via CodeDeploy and use pre-traffic and post-traffic test functions to verify code. Rollback in case CloudWatch alarms are triggered** ✅
- D. Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. In case the Lambda function errors out, rollback the CloudFormation change set to the previous version

### Explanation

Correct option:

Use Serverless Application Model (SAM) and leverage the built-in traffic-shifting feature of SAM to deploy the new Lambda version via CodeDeploy and use pre-traffic and post-traffic test functions to verify code. Rollback in case CloudWatch alarms are triggered

The AWS Serverless Application Model (SAM) is an open source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. You define the application you want with just a few lines per resource and model it using YAML. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax. Then, CloudFormation provisions your resources with reliable deployment capabilities.

To address the given use-case, you can use the traffic shifting feature of SAM to easily test the new version of the Lambda function without having to manually move 100% of the traffic to the new version in one shot.

You can use CodeDeploy to create a deployment process that publishes the new Lambda version but does not send any traffic to it. Then it executes a PreTraffic test to ensure that your new function works as expected. After the test succeeds, CodeDeploy automatically shifts traffic gradually to the new version of the Lambda function. This workflow address one of the key requirements of reducing the time to detect errors. You can roll back to the previous version in case the new version errors out.


via - https://aws.amazon.com/blogs/compute/implementing-safe-aws-lambda-deployments-with-aws-codedeploy/

Incorrect options:

Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. In case the Lambda function errors out, rollback the CloudFormation change set to the previous version - You can use CloudFormation change sets to preview how proposed changes to a stack might impact your running resources, for example, whether your changes will delete or replace any critical resources, AWS CloudFormation makes the changes to your stack only when you decide to execute the change set, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another change set.

This option does not help in reducing the time to detect any potential deployment errors as you would not know about any potential failures until you actually deploy the stack.


via - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

Instead, you should use SAM to create your serverless application as it comes built-in with CodeDeploy to provide gradual Lambda deployments. Also, you can define pre-traffic and post-traffic test functions to verify that the newly deployed code is configured correctly and your application operates as expected. You can roll back the deployment if CloudWatch alarms are triggered.

Set up and deploy a CloudFormation stack containing a new API Gateway endpoint that points to the new Lambda version. Test the updated CloudFront origin that points to this new API Gateway endpoint and in case errors are detected then revert the CloudFront origin to the previous working API Gateway endpoint - This option does not help in reducing the time to detect any potential deployment errors as you would not know about any potential failures until you actually deploy the stack and point to the new endpoint.

Instead, you should use SAM to create your serverless application as it comes built-in with CodeDeploy to provide gradual Lambda deployments. Also, you can define pre-traffic and post-traffic test functions to verify that the newly deployed code is configured correctly and your application operates as expected. You can roll back the deployment if CloudWatch alarms are triggered.

Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. Use pre-traffic and post-traffic test functions of the change set to verify the deployment. Rollback in case CloudWatch alarms are triggered - This option has been added as a distractor, since CloudFormation change sets do not have pre-traffic and post-traffic test functions. Therefore this option is incorrect.

References:

https://aws.amazon.com/blogs/compute/implementing-safe-aws-lambda-deployments-with-aws-codedeploy/

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html

---

## Question 5

**Category:** CSAP – Continuous Improvement for Existing Solutions

A retail company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for managing a serverless application that consists of multiple API gateways, Lambda functions, S3 buckets and DynamoDB tables. The company is getting reports from customers that some of the application components seem to be lagging while loading dynamic images and some are timing out with the "504 Gateway Timeout" error. As part of your investigations to identify the root cause behind this issue, you can confirm that DynamoDB monitoring metrics are at acceptable levels.

Which of the following steps would you recommend to address these application issues? (Select two)

- A. Process and analyze the VPC Flow Logs to determine if there is packet loss between the Lambda function and S3
- **B. Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals** ✅
- C. Enable execution logging for the API Gateway. Process and analyze the execution logs in the API Gateway for HTTP errors to determine the root cause of the errors
- D. Enable access logging for the API Gateway. Process and analyze the access logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **E. Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors** ✅

### Explanation

Correct options:

Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals

To help you troubleshoot failures in a function, the Lambda service logs all requests handled by a Lambda function and also automatically stores logs generated by your code through Amazon CloudWatch Logs. You can insert logging statements into your code to determine processing times for requested images. These logs can then be processed at certain pre-configured intervals for further analysis.


via - https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html

Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors

You can use AWS X-Ray to visualize the components of your application, identify performance bottlenecks such as the one described in the use-case for processing images and troubleshoot those requests that resulted in an error. Your Lambda functions send trace data to X-Ray, and X-Ray processes the data to generate a service map and searchable trace summaries.


via - https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html

Incorrect options:

Enable execution logging for the API Gateway. Process and analyze the execution logs in the API Gateway for HTTP errors to determine the root cause of the errors

Enable access logging for the API Gateway. Process and analyze the access logs in the API Gateway for HTTP errors to determine the root cause of the errors

For an API Gateway, a "504 Gateway Timeout" error implies an "Endpoint Request Timed-out Exception".


via - https://docs.aws.amazon.com/apigateway/api-reference/handling-errors/

To troubleshoot an API Gateway REST API or WebSocket API that you're developing, enable execution logging and access logging to Amazon CloudWatch Logs. Execution logs contain helpful information that you can use to identify and fix most errors with your APIs. Access logs contain details about who accessed your API and how they accessed it, which you can also use for troubleshooting.


via - https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-cloudwatch-logs/

However, neither execution logs nor access logs at the API Gateway level will provide information to identify the root cause for the "504 Gateway Timeout" error as it needs to be analyzed at the source system level which is Lambda function for the given use-case, as that's where the images are being processing and the application is lagging or timing out for some of those images. Another thing to note is that only access logs are available for HTTP APIs, so you do not have access to execution logs for the given use-case.

Therefore, both of these options are incorrect.

Process and analyze the VPC Flow Logs to determine if there is packet loss between the Lambda function and S3

VPC Flow Logs allow you to capture information about the IP traffic going to and from network interfaces in your VPC. You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.


via - https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

This option has been added as a distractor as you cannot use VPC Flow Logs to determine packet loss. AWS has a built-in tool called AWSSupport-SetupIPMonitoringFromVPC that you can use to monitor metrics such as latency and the percentage of packet loss across a network path. It monitors the selected target IP addresses by continuously running ping, MTR, TCP traceroute, and tracepath network diagnostic tests.

References:

https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html

https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html

https://docs.aws.amazon.com/apigateway/api-reference/handling-errors/

https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-cloudwatch-logs/

https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/

https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

---

## Question 6

**Category:** CSAP – Continuous Improvement for Existing Solutions

An e-commerce web application is hosted on Amazon EC2 instances that are fronted by Application Load Balancer (ALB) configured with an Auto Scaling group (ASG). Enhanced security is provided to the ALB by AWS WAF web ACLs. As per the company's security policy, AWS CloudTrail is activated and logs are configured to be stored on Amazon S3 and CloudWatch Logs.

A discount sales offer was run on the application for a week. The support team has noticed that a few of the instances have rebooted taking down the log files and all temporary data with them. Initial analysis has confirmed that the incident took place during off-peak hours. Even though the incident did not cause any sales or revenue loss, the CTO has asked the security team to fix the security error that has allowed the incident to go unnoticed and eventually untraceable.

What steps will you implement to permanently record all traffic coming into the application?

- A. To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring
- **B. Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking** ✅
- C. Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking
- D. Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting

### Explanation

Correct option:

Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking

The logging destinations that you can choose from for your AWS WAF logs are:


Amazon CloudWatch Logs
Amazon Simple Storage Service
Amazon Kinesis Data Firehose


To send logs to Amazon Kinesis Data Firehose, you send logs from your web ACL to an Amazon Kinesis Data Firehose with a configured storage destination. After you enable logging, AWS WAF delivers logs to your storage destination through the HTTPS endpoint of Kinesis Data Firehose.

One AWS WAF log is equivalent to one Kinesis Data Firehose record. If you typically receive 10,000 requests per second and you enable full logs, you should have 10,000 records per second setting in Kinesis Data Firehose.

Incorrect options:

Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking - As discussed above, the logging destinations that you can choose from for your AWS WAF logs are Amazon CloudWatch Logs, Amazon Simple Storage Service, and Amazon Kinesis Data Firehose. Amazon CloudTrail is not a valid destination for WAF ACL logs.

To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring - VPC Flow You should also note that VPC Flow Logs cannot capture all traffic coming into the application as these can only capture information about the IP traffic going to and from network interfaces in your VPC. In addition, VPC Flow Logs can be directly published only to the following destinations: Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose. So this option is incorrect.

Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting - Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. Elastic Load Balancing access logs are stored in Amazon S3 buckets and it is not possible to directly write the logs to Kinesis Data Firehose.

References:

https://aws.amazon.com/about-aws/whats-new/2021/12/awf-waf-cloudwatch-log-s3-bucket/

https://docs.aws.amazon.com/waf/latest/developerguide/logging-destinations.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

---

## Question 7

**Category:** CSAP – Design for New Solutions

A data analytics company needs to set up a data lake on Amazon S3 for a financial services client. The data lake is split in raw and curated zones. For compliance reasons, the source data needs to be kept for a minimum of 5 years. The source data arrives in the raw zone and is then processed via an AWS Glue based ETL job into the curated zone. The business analysts run ad-hoc queries only on the data in the curated zone using Athena. The team is concerned about the cost of data storage in both the raw and curated zones as the data is increasing at a rate of 2 TB daily in each zone.

Which of the following options would you implement together as the MOST cost-optimal solution?
(Select two)

- **A. Setup a lifecycle policy to transition the raw zone data into Glacier Deep Archive after 1 day of object creation** ✅
- B. Create a Lambda function based job to delete the raw zone data after 1 day
- C. Setup a lifecycle policy to transition the curated zone data into Glacier Deep Archive after 1 day of object creation
- D. Use Glue ETL job to write the transformed data in the curated zone using CSV format
- **E. Use Glue ETL job to write the transformed data in the curated zone using a compressed file format** ✅

### Explanation

Correct options:

Setup a lifecycle policy to transition the raw zone data into Glacier Deep Archive after 1 day of object creation

You can manage your objects so that they are stored cost-effectively throughout their lifecycle by configuring their Amazon S3 Lifecycle. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. For example, you might choose to transition objects to the S3 Standard-IA storage class 30 days after you created them, or archive objects to the S3 Glacier storage class one year after creating them.

For the given use-case, the raw zone consists of the source data, so it cannot be deleted due to compliance reasons. Therefore, you should use a lifecycle policy to transition the raw zone data into Glacier Deep Archive after 1 day of object creation.

Please read more about S3 Object Lifecycle Management:

via - https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html

Use Glue ETL job to write the transformed data in the curated zone using a compressed file format

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics.

You cannot transition the curated zone data into Glacier Deep Archive because it is used by the business analysts for ad-hoc querying. Therefore, the best optimization is to have the curated zone data stored in a compressed format via the Glue job. The compressed data would reduce the storage cost incurred on the data in the curated zone.

Please see this example for a Glue ETL Pipeline:

via - https://aws.amazon.com/glue/

Incorrect options:

Create a Lambda function based job to delete the raw zone data after 1 day - As mentioned in the use-case, the source data needs to be kept for a minimum of 5 years for compliance reasons. Therefore the data in the raw zone cannot be deleted after 1 day.

Setup a lifecycle policy to transition the curated zone data into Glacier Deep Archive after 1 day of object creation - You cannot transition the curated zone data into Glacier Deep Archive because it is used by the business analysts for ad-hoc querying. Hence this option is incorrect.

Use Glue ETL job to write the transformed data in the curated zone using CSV format - It is cost-optimal to write the data in the curated zone using a compressed format instead of CSV format. The compressed data would reduce the storage cost incurred on the data in the curated zone. So, this option is incorrect.

References:

https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html

https://aws.amazon.com/glue/

---

## Question 8

**Category:** CSAP – Design for New Solutions

A digital media company wants to use AWS Cloudfront to manage its content. Firstly, it would like to allow only those new users who have paid the annual subscription fee the ability to download the application installation file. Secondly, only the subscribers should be able to view the files in the members' area.

As a Solutions Architect Professional, which of the following would you recommend as the MOST optimal solutions to deliver restricted content to the bona fide end users? (Select two)

- **A. Use CloudFront signed cookies to restrict access to all the files in the members' area of the website** ✅
- **B. Use CloudFront signed URLs to restrict access to the application installation file** ✅
- C. Require HTTPS for communication between CloudFront and your S3 origin
- D. Use CloudFront signed cookies to restrict access to the application installation file
- E. Use CloudFront signed URLs to restrict access to all the files in the members' area of the website

### Explanation

Correct options:

Use CloudFront signed URLs to restrict access to the application installation file

Use CloudFront signed cookies to restrict access to all the files in the members' area of the website

Many companies that distribute content over the internet want to restrict access to documents, business data, media streams, or content that is intended for selected users, for example, users who have paid a fee.

To securely serve this private content by using CloudFront, you can do the following:

Require that your users access your private content by using special CloudFront signed URLs or signed cookies.

You should use a signed URL if you want to restrict access to individual files, for example, an installation download for your application. A signed URL includes additional information, for example, expiration date and time, that gives you more control over access to your content.

On the other hand, CloudFront signed cookies allow you to control who can access your content when you don't want to change your current URLs or when you want to provide access to multiple restricted files, for example, all of the files in the members' area of a website.


via - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-choosing-signed-urls-cookies.html

Incorrect options:

Use CloudFront signed cookies to restrict access to the application installation file

Use CloudFront signed URLs to restrict access to all the files in the members' area of the website

These two options contradict the description provided in the explanation above, so these options are incorrect.

Require HTTPS for communication between CloudFront and your S3 origin

Requiring HTTPS for communication between CloudFront and your custom origin (or S3 origin) only enables secure access to the underlying content. You cannot use HTTPS to restrict access to your private content. So this option is incorrect.

References:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-choosing-signed-urls-cookies.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.html

---

## Question 9


**Category:** CSAP – Design Solutions for Organizational Complexity

A global enterprise oversees at least six hundred AWS accounts via AWS Organizations. Recently, the governance team granted product owners the ability to configure Amazon S3 Access Points within the assigned accounts. These access points must be accessible only from within VPCs (Virtual Private Clouds), and any access from the Internet must be restricted.
What is the most operationally scalable and manageable approach to enforce this control efficiently across the organization?

- **A. At the root level of the organization, implement a Service Control Policy (SCP) that blocks s3:CreateAccessPoint except if the s3:AccessPointNetworkOrigin is equal to VPC** ✅
- B. Modify the bucket’s resource policy to block any attempt to perform the s3:CreateAccessPoint operation, except when the s3:ResourceAccount condition is explicitly matched to VPC
- C. Use AWS Config rules combined with AWS Lambda to detect and revert S3 Access Points that are not restricted to VPC-only access
- D. Use an S3 Object ACL to block the creation of access points unless the request originates from a VPC by checking the s3:AccessPointNetworkOrigin condition

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for the IAM users and IAM roles in your organization. SCPs help ensure your accounts stay within your organization’s access control guidelines.
SCPs do not grant permissions to your organization’s IAM users and IAM roles. An SCP defines a permission guardrail or limits the actions your organization’s IAM users and IAM roles can perform.

By applying this SCP at the root level, the enterprise ensures that no user or role in any account, regardless of their IAM policies, can create an S3 Access Point unless it is explicitly configured to be VPC-only. This method is highly scalable and manageable because it requires a single policy update at the organizational root to enforce the rule across hundreds of accounts. It also aligns perfectly with the requirement to restrict access to S3 Access Points from the internet, thereby ensuring compliance and reducing the risk of misconfiguration by individual product teams.
Hence, the correct answer is: At the root level of the organization, implement a Service Control Policy (SCP) that blocks s3:CreateAccessPoint except if the s3:AccessPointNetworkOrigin is equal to VPC.
The option that says: Modify the bucket’s resource policy to block any attempt to perform the s3:CreateAccessPoint operation, except when the s3:ResourceAccount condition is explicitly matched to VPC is incorrect. First, S3 bucket policies only control access to bucket-level and object-level operations (such as s3:GetObject, s3:PutObject, or s3:ListBucket). They do not govern actions related to creating or managing S3 Access Points, such as s3:CreateAccessPoint. That action is handled at the account level, not the bucket level, so attempting to restrict it through a bucket policy is fundamentally ineffective. Second, using the s3:ResourceAccount condition key is also inappropriate. s3:ResourceAccount refers to the AWS account that owns the resource, not the network origin or access type. The correct condition key for enforcing network-based restrictions during access point creation is s3:AccessPointNetworkOrigin, not s3:ResourceAccount. Therefore, this option fails on both policy scope and condition logic levels, making it an invalid approach for enforcing VPC-only access point creation across an organization.
The option that says: Use AWS Config rules combined with AWS Lambda to detect and revert S3 Access Points that are not restricted to VPC-only access is incorrect. While this method is technically feasible and can enforce compliance after the fact, it is only reactive and not preventive. AWS Config rules monitor resource configurations and can trigger AWS Lambda functions for remediation, but they do not block the creation of non-compliant access points in real-time. This means an S3 Access Point that allows internet access could exist, even briefly, before being detected and corrected, which introduces operational and security risks. Additionally, deploying and maintaining AWS Config rules and remediating Lambda functions across hundreds of accounts requires significant effort. It involves ensuring that Config is enabled and configured correctly in each account, managing the lifecycle of custom remediation functions, handling errors or exceptions, and maintaining consistency. Compared to a centralized and proactive mechanism like a Service Control Policy (SCP), this method introduces more moving parts, complexity, and operational overhead. Therefore, while it may serve as a supplementary compliance check, it is not the most efficient or scalable approach to enforce VPC-only S3 Access Point creation across an enterprise-wide AWS Organizations structure.
The option that says: Use an S3 Object ACL to block the creation of access points unless the request originates from a VPC by checking the s3:AccessPointNetworkOrigin condition is incorrect. This approach reflects a misunderstanding of both S3 Object ACLs and the mechanics of S3 Access Point creation. S3 Object ACLs manage access control at the object level, allowing or denying access to specific users or AWS accounts for actions such as s3:GetObject or s3:PutObject. They cannot control IAM-level operations like s3:CreateAccessPoint, an account-level API call not associated with individual objects or even directly with the bucket. Furthermore, ACLs do not support conditional logic based on context keys like s3:AccessPointNetworkOrigin. That condition key applies only to IAM policies, SCPs, or resource-based policies on access points, not to ACLs. Therefore, this option is incorrect in its proposed enforcement mechanism and invalid in how it misuses a condition key in a context where it cannot be applied. It would not work at all to restrict access point creation, regardless of network origin, making it entirely ineffective for meeting the stated requirement.
 
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html
https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html
 
Check out this AWS Organizations Cheat Sheet:
https://tutorialsdojo.com/aws-organizations/

---

## Question 10

**Category:** CSAP – Accelerate Workload Migration and Modernization

A payment service provider company has a legacy application built on high throughput and resilient queueing system to send messages to the customers. The implementation relied on a manually-managed RabbitMQ cluster and consumers. The system was able to process a large load of messages within a reasonable delivery time. The cluster and consumers were both deployed on Amazon Elastic Compute Cloud (Amazon EC2) instances. However, when the messages in the queue piled up due to network failures on the customer side, the latency of the overall flow was affected, resulting in a breach of the service level agreement (SLA). The development team had to manually scale the queues to resolve the issue. Also, while doing manual upgrades on RabbitMQ and the hosting operating system, the company faced downtimes.

The company is growing and has to maintain a strict delivery time SLA. The company is now looking for a serverless solution for its messaging queues. The queue functions of handling concurrency, message delays and retries, maintaining message order, secure delivery, and scalability are needed in the proposed solution architecture.

Which of the following would you propose for a cost-effective solution for the requirement?

- A. Design a cost-effective, serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Classic
- **B. Design the serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Fargate. To save costs, run the Amazon SQS FIFO queues and Amazon ECS Fargate tasks only when needed** ✅
- C. Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Fargate. To save costs, run the Amazon MQ for RabbitMQ queues and Amazon ECS Fargate tasks only when needed
- D. Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Classic

### Explanation

Correct option:

Design the serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Fargate. To save costs, run the Amazon SQS FIFO queues and Amazon ECS Fargate tasks only when needed - Amazon Simple Queue Service (SQS) with Amazon ECS Fargate offers the serverless solution that the company is looking for. This solution is correct for the following reasons:


While doing manual upgrades on RabbitMQ and the hosting operating system, the company sometimes faced downtimes. By using Amazon SQS, messaging infrastructure became automated, reducing the need for maintenance operations.
To save costs, Amazon SQS FIFO queues and Amazon ECS Fargate tasks run only when needed. These services process data in smaller units and run them in parallel. They can scale up efficiently to handle peak traffic loads. This will satisfy most architectures that handle non-uniform traffic without needing additional application logic.


Migrating a self-managed message broker to Amazon SQS:

via - https://aws.amazon.com/blogs/architecture/migrating-a-self-managed-message-broker-to-amazon-sqs/

Incorrect options:

Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Classic

Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Fargate. To save costs, run the Amazon MQ for RabbitMQ queues and Amazon ECS Fargate tasks only when needed

Design a cost-effective, serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Classic

None of the above three solutions come under serverless options since Amazon MQ for RabbitMQ will require configuring and scaling of Amazon MQ broker. A broker is a message broker environment running on Amazon MQ. It is the basic building block of Amazon MQ. The combined description of the broker instance class (m5, t3) and size (large, micro) is a broker instance type (for example, mq.m5.large).

ECS Classic uses Amazon EC2 instances, making it unsuitable for a serverless requirement.

References:

https://aws.amazon.com/blogs/architecture/migrating-a-self-managed-message-broker-to-amazon-sqs/

https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-rabbitmq.html

---

## Question 11


**Category:** CSAP – Continuous Improvement for Existing Solutions

An international e-commerce company relies on Amazon CloudFront to deliver its multi-regional Amazon ECS-based web store with fast, scalable performance. Over recent months, customers around the globe have started reporting sluggish page load times, particularly during flash sales and heavy promotional events.
The performance reliability team has spotted a troubling pattern: CloudFront’s cache hit ratio has consistently decreased. Amazon CloudWatch metrics reveal the root cause: query strings in some request URLs are inconsistent. Parameter order shifts unpredictably, and values alternate between mixed-case and lowercase.
Which steps should be implemented to rapidly restore CloudFront’s cache hit/ratio with the least operational overhead and cost?

- **A. Configure a CloudFront Function on the Viewer Request event that alphabetically sorts all query parameter keys and enforces lowercase for both parameter names and values** ✅
- B. Attach a Lambda@Edge handler to the CloudFront distribution’s Viewer Request event that alphabetically sorts each query string parameter and converts all names and values to lowercase to ensure consistent cache key generation
- C. Place a reverse proxy layer downstream of the load balancer to intercept incoming URLs and rewrite all query string characters to lowercase
- D. Modify the CloudFront distribution’s cache or origin-request policy to stop including query-string parameters in the cache key

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		With CloudFront Functions, you can write lightweight functions in JavaScript for high-scale, latency-sensitive CDN customizations. Your functions can manipulate the requests and responses that flow through CloudFront, perform basic authentication and authorization, generate HTTP responses at the edge, and more. The CloudFront Functions runtime environment offers submillisecond startup times, scales immediately to handle millions of requests per second, and is highly secure. CloudFront Functions is a native feature of CloudFront, which means you can build, test, and deploy your code entirely within CloudFront.
When you associate a CloudFront function with a CloudFront distribution, CloudFront intercepts requests and responses at CloudFront edge locations and passes them to your function. You can invoke CloudFront Functions when the following events occur:
When CloudFront receives a request from a viewer (viewer request)
Before CloudFront returns the response to the viewer (viewer response)

Using a CloudFront Function at the Viewer Request event to alphabetically sort and lowercase query parameters is the optimal solution for this specific problem. CloudFront Functions are lightweight, execute in sub-millisecond time, and cost-efficient (~$0.10 per million requests). This option delivers the fastest remediation with minimal complexity or overhead.
Hence, the correct answer is: Configure a CloudFront Function on the Viewer Request event that alphabetically sorts all query parameter keys and enforces lowercase for both parameter names and values.
The option that says: Attach a Lambda@Edge handler to the CloudFront distribution’s Viewer Request event that alphabetically sorts each query string parameter and converts all names and values to lowercase to ensure consistent cache key generation is incorrect. Using Lambda@Edge is actually a technically sound approach: CloudFront calculates the cache key at that viewer-level stage, so normalizing the query string there ensures identical URLs map to the same cache key, reducing cache fragmentation and improving the cache hit ratio. However, this option is suboptimal compared to CloudFront Function. Deploying a CloudFront Function at the Viewer Request event achieves the same normalization (sorting and lowercasing query strings) but is far more lightweight, faster, and cost-effective. A CloudFront Function runs in sub-millisecond time at every edge location, whereas Lambda@Edge incurs a 1 to 2-millisecond cold-start latency and costs around 6 times. For a task as simple as query-string normalization, relying on Lambda@Edge introduces unnecessary latency and overhead compared to the more efficient CloudFront Function alternative.
The option that says: Modify the CloudFront distribution’s cache or origin-request policy to stop including query-string parameters in the cache key is incorrect. Disabling query-string–based caching can lead to wrong content being served, not just performance issues. When CloudFront excludes query strings from the cache key, every request, regardless of its unique query data, receives the same cached response. If one user’s request carries specific parameters (e.g., ?user=alice), CloudFront might cache that particular version and then serve it to another user requesting the same path without those parameters. In effect, CloudFront treats what could be distinct content as identical.
The option that says: Place a reverse proxy layer downstream of the load balancer to intercept incoming URLs and rewrite all query string characters to lowercase is incorrect. Placing a reverse proxy layer downstream of the load balancer to normalize URLs won’t improve cache hit ratios because CloudFront computes its cache key before forwarding requests to any backend. As a result, any normalization done later in the request pipeline simply does not affect caching at all. Without normalization at the edge, cache fragmentation persists. This approach is ineffective.
 
References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html
 
Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

---

## Question 12

**Category:** CSAP – Continuous Improvement for Existing Solutions

An e-commerce company is investigating user reports of its Java-based web application errors on the day of the Thanksgiving sale. The development team recovered the logs created by the EC2 instance-hosted web servers and reviewed Aurora DB cluster performance metrics. Some of the web servers were terminated before logs could be collected and the Aurora metrics were inadequate for query performance analysis.

Which of the following steps would you recommend to make the monitoring process more reliable to troubleshoot any future events due to traffic spikes? (Select three)

- A. Enable detailed monitoring for Amazon EC2 instances to send data points to CloudWatch every minute. Track the metric 'CPUUtilization' to know when the auto-scaling process can kick in
- B. Use CloudTrail and configure a trail to deliver Amazon Aurora query activity to an Amazon S3 bucket. Process and analyze these real-time log streams using Amazon Kinesis Data Streams
- **C. Configure the Aurora MySQL DB cluster to publish slow query and error logs to Amazon CloudWatch Logs** ✅
- D. Enable Aurora lab mode which will then publish all logs and activity on Aurora DB to CloudWatch logs
- **E. Set up the AWS X-Ray SDK to trace incoming HTTP requests on the EC2 instances as well as set up tracing of SQL queries with the X-Ray SDK for Java** ✅
- **F. Install and configure an Amazon CloudWatch Logs agent on the EC2 instances to send the application logs to CloudWatch Logs** ✅

### Explanation

Correct options:

Configure the Aurora MySQL DB cluster to publish slow query and error logs to Amazon CloudWatch Logs

You can configure your Aurora MySQL DB cluster to publish general, slow, audit, and error log data to a log group in Amazon CloudWatch Logs. With CloudWatch Logs, you can perform real-time analysis of the log data, and use CloudWatch to create alarms and view metrics. You can use CloudWatch Logs to store your log records in highly durable storage.

To publish logs to CloudWatch Logs, the respective logs must be enabled. Error logs are enabled by default, but you must enable the other types of logs explicitly. The slow query logs and error logs can be used to identify the root cause behind the given issue.

Install and configure an Amazon CloudWatch Logs agent on the EC2 instances to send the application logs to CloudWatch Logs

You can collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch agent. The unified CloudWatch agent enables you to collect internal system-level metrics from Amazon EC2 instances across operating systems. The metrics can include in-guest metrics, in addition to the metrics for EC2 instances. You can collect logs from Amazon EC2 instances and on-premises servers, running either Linux or Windows Server. The application logs (via the CloudWatch logs) can be used to identify the root cause behind the given issue.

Set up the AWS X-Ray SDK to trace incoming HTTP requests on the EC2 instances as well as set up tracing of SQL queries with the X-Ray SDK for Java

You can use the X-Ray SDK to trace incoming HTTP requests that your application serves on an EC2 instance. Use a Filter to instrument incoming HTTP requests. When you add the X-Ray servlet filter to your application, the X-Ray SDK for Java creates a segment for each sampled request. This segment includes timing, method, and disposition of the HTTP request. You can also instrument your SQL database queries by adding the X-Ray SDK for Java JDBC interceptor to your data source configuration. X-Ray tracing for the HTTP requests as well as the SQL queries can help in identifying the root cause behind the given issue.

Incorrect options:

Use CloudTrail and configure a trail to deliver Amazon Aurora query activity to an Amazon S3 bucket. Process and analyze these real-time log streams using Amazon Kinesis Data Streams - You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. You can identify who or what took which action, what resources were acted upon, when the event occurred, and other details to help you analyze and respond to activity in your AWS account. CloudTrail provides a record of actions taken by a user, role, or AWS service in Amazon Aurora. However, CloudTrail does not capture any query activity in Aurora, so this option is incorrect.

Enable detailed monitoring for Amazon EC2 instances to send data points to CloudWatch every minute. Track the metric 'CPUUtilization' to know when the auto-scaling process can kick in - Tracking the 'CPUUtilization' parameter is irrelevant to the given use case as it would not point to the root cause behind the given issue.

Enable Aurora lab mode which will then publish all logs and activity on Aurora DB to CloudWatch logs - Aurora lab mode is used to enable Aurora features that are available in the current Aurora database version but are not enabled by default. These features are tested in development/test environments. Aurora lab mode is not relevant for capturing the log activity of Aurora DB. This option has been added as a distractor.

References:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html

https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-filters.html

https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-sqlclients.html

---

## Question 13

**Category:** CSAP – Design for New Solutions

A solutions architect at a retail company has configured a private hosted zone using Route 53. The architect needs to configure health checks for record sets within the private hosted zone that are associated with EC2 instances.

How can the architect build a solution to address the given use case?

- A. Configure a Route 53 health check that monitors an SNS topic which in turn notifies a CloudWatch alarm when the EC2 StatusCheckFailed metric fails
- B. Configure a Route 53 health check to a private IP associated with the instances inside the VPC to be checked
- C. Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric and then configure a health check that monitors the status of the metric
- **D. Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric, add an alarm to the metric, and then configure a health check that monitors the state of the alarm** ✅

### Explanation

Correct option:

Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric, add an alarm to the metric, and then configure a health check that monitors the state of the alarm

A private hosted zone is a container that holds information about how you want Amazon Route 53 to respond to DNS queries for a domain and its subdomains within one or more VPCs that you create with the Amazon VPC service.


via https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html

Amazon Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources. Each health check that you create can monitor one of the following:

The health of a specified resource, such as a web server.

The status of other health checks.

The status of an Amazon CloudWatch alarm.

Additionally, with Amazon Route 53 Application Recovery Controller, you can set up routing control health checks with DNS failover records to manage traffic failover for your application.

For the given use case, you need to create a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric, add an alarm to the metric, and then create a health check that is based on the data stream for the alarm. To improve resiliency and availability, Route 53 doesn't wait for the CloudWatch alarm to go into the ALARM state. The status of a health check changes from healthy to unhealthy based on the data stream and the criteria in the CloudWatch alarm.


via https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html

Incorrect options:

Configure a Route 53 health check that monitors an SNS topic which in turn notifies a CloudWatch alarm when the EC2 StatusCheckFailed metric fails - As mentioned above, the Route 53 health checks cannot monitor an SNS topic, so this option is incorrect.

Configure a Route 53 health check to a private IP associated with the instances inside the VPC to be checked - Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC. Therefore, you cannot configure a Route 53 health check to a private IP associated with an instance.

Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric and then configure a health check that monitors the status of the metric - Route 53 health checks can monitor CloudWatch alarms. The Route 53 health checks cannot directly monitor the CloudWatch metrics, so this option is incorrect.

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html

---

## Question 14

**Category:** CSAP – Design for New Solutions

An e-commerce company wants to rollout and test a blue-green deployment for its global application in the next couple of days. Most of the customers use mobile phones which are prone to DNS caching. The company has only two days left before the big sale will be launched.

As a Solutions Architect Professional, which of the following options would you suggest to test the deployment on as many users as possible in the given time frame?

- A. Use Route 53 weighted routing to spread traffic across different deployments
- B. Use AWS CodeDeploy deployment options to choose the right deployment
- C. Use Elastic Load Balancer to distribute traffic across deployments
- **D. Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment** ✅

### Explanation

Correct option:

Blue/green deployment is a technique for releasing applications by shifting traffic between two identical environments running different versions of the application: "Blue" is the currently running version and "green" the new version. This type of deployment allows you to test features in the green environment without impacting the currently running version of your application. When you’re satisfied that the green version is working properly, you can gradually reroute the traffic from the old blue environment to the new green environment. Blue/green deployments can mitigate common risks associated with deploying software, such as downtime and rollback capability.

Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment - AWS Global Accelerator is a network layer service that directs traffic to optimal endpoints over the AWS global network, this improves the availability and performance of your internet applications. It provides two static anycast IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, such as your Application Load Balancers, Network Load Balancers, Elastic IP addresses or Amazon EC2 instances, in a single or in multiple AWS regions.

AWS Global Accelerator uses endpoint weights to determine the proportion of traffic that is directed to endpoints in an endpoint group, and traffic dials to control the percentage of traffic that is directed to an endpoint group (an AWS region where your application is deployed).

While relying on the DNS service is a great option for blue/green deployments, it may not fit use-cases that require a fast and controlled transition of the traffic. Some client devices and internet resolvers cache DNS answers for long periods; this DNS feature improves the efficiency of the DNS service as it reduces the DNS traffic across the Internet, and serves as a resiliency technique by preventing authoritative name-server overloads. The downside of this in blue/green deployments is that you don’t know how long it will take before all of your users receive updated IP addresses when you update a record, change your routing preference or when there is an application failure.

With AWS Global Accelerator, you can shift traffic gradually or all at once between the blue and the green environment and vice-versa without being subject to DNS caching on client devices and internet resolvers, traffic dials and endpoint weights changes are effective within seconds.

Incorrect options:

Use Route 53 weighted routing to spread traffic across different deployments - Weighted routing lets you associate multiple resources with a single domain name (example.com) or subdomain name (acme.example.com) and choose how much traffic is routed to each resource. This can be useful for a variety of purposes, including load balancing and testing new versions of the software. As discussed earlier, DNS caching is a negative behavior for this use case and hence Route 53 is not a good option.

Use Elastic Load Balancer to distribute traffic across deployments - An ELB can distribute traffic across healthy instances. You can also use the ALB weighted target groups feature for blue/green deployments as it does not rely on the DNS service. In addition you don’t need to create new ALBs for the green environment. As the use-case refers to a global application, so this option cannot be used for a multi-Region solution which is needed for the given requirement.

Use AWS CodeDeploy deployment options to choose the right deployment - In CodeDeploy, a deployment is the process, and the components involved in the process, of installing content on one or more instances. This content can consist of code, web and configuration files, executables, packages, scripts, and so on. CodeDeploy deploys content that is stored in a source repository, according to the configuration rules you specify. Blue/Green deployment is one of the deployment types that CodeDeploy supports. AWS CodeDeploy performs deployments with AWS resources located in the same region, so this option is ruled out.

References:

https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-global-accelerator-to-achieve-blue-green-deployments

https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted

---

## Question 15

**Category:** CSAP – Accelerate Workload Migration and Modernization

A company wants to migrate its on-premises resources to AWS. The IT environment consists of 200 virtual machines (VMs) with a combined storage capacity of 50 TB. While the majority of VMs may be taken down for migration since they are only used during business hours, others are mission-critical, so the downtime must be minimized. The on-premises network engineer has allocated 10 Mbps of internet bandwidth for the migration. The capacity of the on-premises network has peaked and increasing it would be prohibitively expensive.

You have been hired as an AWS Certified Solutions Architect Professional to develop a migration strategy that can be implemented in the next three months. Which of the following would you recommend?

- A. Export the VMs locally, starting with the most mission-critical servers first. Configure a 1.25 Gbps AWS site-to-site VPN to securely upload each VM to Amazon S3 after they are exported. Use VM Import/Export to import the VMs into Amazon EC2
- **B. Migrate mission-critical VMs using AWS Application Migration Service (MGN). Export the other VMs locally and transfer them to Amazon S3 using AWS Snowball Edge. Leverage VM Import/Export to import the VMs into Amazon EC2** ✅
- C. Leverage AWS Migration Hub to analyze each application for further refactoring and optimizations using AWS services or AWS Marketplace solutions
- D. Create a 10 Gbps AWS Direct Connect connection and then configure a private virtual interface. Leverage AWS Server Migration Service (SMS) to migrate the VMs into Amazon EC2

### Explanation

Correct option:

Migrate mission-critical VMs using AWS Application Migration Service (MGN). Export the other VMs locally and transfer them to Amazon S3 using AWS Snowball Edge. Leverage VM Import/Export to import the VMs into Amazon EC2

AWS Application Migration Service (MGN) simplifies and expedites your migration to AWS by automatically converting your source servers from physical, virtual, or cloud infrastructure to run natively on AWS. It further simplifies your migration and reduces costs by enabling you to use the same automated process for a wide range of applications, without changes to applications, their architecture, or the migrated servers. You can use AWS Application Migration Service to perform non-disruptive tests before cutover. After testing, you can use AWS Application Migration Service to quickly lift and shift your applications to the cloud during a short cutover window, typically measured in minutes.

Application Migration Service:

via - https://aws.amazon.com/application-migration-service/

Snowball Edge Storage Optimized is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. It provides up to 80 TB of usable HDD storage, 40 vCPUs, 1 TB of SATA SSD storage, and up to 40 Gb network connectivity to address large-scale data transfer and pre-processing use cases. As each Snowball Edge Storage Optimized device can handle 80 TB of data, you can order 1 such device to take care of the data transfer for all applications. AWS Snowball Edge is suitable for offline data transfers, for customers who are bandwidth constrained or transferring data from remote, disconnected, or austere environments.

You can use VM Import/Export to import virtual machine (VM) images from your virtualization environment to Amazon EC2 as Amazon Machine Images (AMI), which you can use to launch instances. Subsequently, you can export the VM images from an instance back to your virtualization environment.

For the given use case, you can migrate mission-critical VMs using AWS Application Migration Service (MGN) as the limited bandwidth of 10 Mbps would be able to support this migration of the most critical VMs without any significant downtime. You can then export the other non-critical VMs locally by copying the VM images into the AWS Snowball Edge device which is later transferred to Amazon S3. Lastly, you can use the VM Import/Export to import the VM images from S3 into Amazon EC2.

Incorrect options:

Create a 10 Gbps AWS Direct Connect connection and then configure a private virtual interface. Leverage AWS Server Migration Service (SMS) to migrate the VMs into Amazon EC2

AWS Direct Connect links your on-premises data center to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. With this connection, you can create virtual interfaces directly to public AWS services (for example, to Amazon S3) or Amazon VPC, bypassing internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the Region with which it is associated.


via - https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

Given that the capacity for the on-premises network has peaked and only 10 Mbps of internet bandwidth is available for the migration task, therefore provisioning a 10 Gbps Direct Connect connection will not help as the constraint of 10 Mbps persists for the on-premises network. At this max bandwidth of 10 Mbps, you can only migrate 106060*24 = 864000 Mb or 864 MB or approx 1 GB of data per day. This is not sufficient to transfer 50 TB of data within the stipulated time of 3 months. Hence this option is incorrect.

Leverage AWS Migration Hub to analyze each application for further refactoring and optimizations using AWS services or AWS Marketplace solutions - AWS Migration Hub provides a single place to store IT asset inventory data while tracking migrations to any AWS Region. It simplifies the discovery of existing applications and infrastructure and their dependencies, assessment of an application’s ability to be migrated and modernized, and recommendations for modernization strategies. Given that the IT environment consists of 200 virtual machines (VMs), it is not feasible to refactor all applications running on these VMs to use AWS services within the stipulated timeframe of three months. Hence this option is not the right fit.

AWS Migration Hub:

via - https://aws.amazon.com/migration-hub/

Export the VMs locally, starting with the most mission-critical servers first. Configure a 1.25 Gbps AWS site-to-site VPN to securely upload each VM to Amazon S3 after they are exported. Use VM Import/Export to import the VMs into Amazon EC2 - AWS Site-to-Site VPN enables you to securely connect your on-premises network or branch office site to your Amazon Virtual Private Cloud (Amazon VPC). You can securely extend your data center or branch office network to the cloud with an AWS Site-to-Site VPN connection. AWS Site-to-Site VPN supports throughput up to 1.25 Gbps, although the actual throughput can be lower for VPN connections that are in different geolocations from the AWS region. This is because the internet path between them has to traverse multiple networks.

Given that the capacity for the on-premises network has peaked and only 10 Mbps of internet bandwidth is available for the migration task, therefore provisioning a 1.25 Gbps AWS site-to-site VPN connection will not help as the constraint of 10 Mbps persists for the on-premises network. At this max bandwidth of 10 Mbps, you can only migrate 106060*24 = 864000 Mb or 864 MB or approx 1 GB of data per day. This is not sufficient to transfer 50 TB of data within the stipulated time of 3 months. Hence this option is incorrect.

References:

https://aws.amazon.com/application-migration-service/

https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html

https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

https://aws.amazon.com/blogs/architecture/improve-vpn-network-performance-of-aws-hybrid-cloud-with-global-accelerator/

---

## Question 16


**Category:** CSAP – Continuous Improvement for Existing Solutions

A tech company that performs large-scale analytics uses an Amazon Redshift cluster with reserved nodes to support its daily data workloads. A recently hired director has initiated a new requirement: generating a deep audit analysis report. This new reporting initiative has introduced complex read queries that are highly CPU-intensive, resulting in unexpected bursts of usage on the Redshift cluster.
The existing setup must continue to handle both read and write queries consistently, even during performance spikes. A solutions architect must propose the most cost-effective solution to address the rising CPU metrics while maintaining system responsiveness and minimizing operational cost.
What is the most economical approach to manage the increased workload introduced by this new reporting initiative?

- A. Launch additional Amazon EC2 instances to scale horizontally Redshift for query parallelization.
- B. Export data from Redshift and import it into Amazon RDS PostgreSQL for deep audit analysis during periods of high load.
- C. Deploy an Amazon EMR cluster to offload high-load transformation jobs from the main analytics pipeline.
- **D. Enable concurrency scaling in the Redshift setup to handle spikes in concurrent query loads without impacting performance.** ✅

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		With Amazon Redshift’s Concurrency Scaling feature, you can support thousands of concurrent users and queries with consistently fast query performance. When you turn on concurrency scaling, Redshift automatically adds additional cluster capacity to process an increase in both read and write queries. Users see the most current data, whether the queries run on the main or concurrency-scaling clusters.
You’re charged for concurrency-scaling clusters only when they’re actively running queries.

Enabling concurrency scaling in Amazon Redshift is the most cost-efficient and operationally elegant solution to address CPU-intensive workload spikes, such as the deep audit analysis report. This feature is designed for situations where query demand temporarily exceeds cluster capacity. It works by automatically adding transient clusters to handle excess read workloads, ensuring that the main cluster can continue to service both read and write operations without latency or disruption. The beauty of this approach lies in its simplicity. This ensures the system remains responsive without permanently overprovisioning resources.
Hence, the correct answer is: Enable concurrency scaling in the Redshift setup to handle spikes in concurrent query loads without impacting performance.
The option that says: Deploy an Amazon EMR cluster to offload high-load transformation jobs from the main analytics pipeline is incorrect. Amazon EMR is robust for distributed data processing, but would only introduce unnecessary complexity in this case. The issue is not about transformation or ETL pipelines. It is about read query concurrency and CPU bottlenecks within the Redshift cluster itself. Offloading workloads to EMR simply doesn’t solve the immediate pressure on Redshift’s compute layer, nor is it primarily focused on short-term spikes. Additionally, EMR adds extra infrastructure to manage and incurs costs, making it neither the simplest nor the most cost-effective option.
The option that says: Launch additional Amazon EC2 instances to scale horizontally Redshift for query parallelization is incorrect. Scaling Amazon Redshift by launching EC2 instances fundamentally misunderstands how Redshift is designed to operate. Redshift is a managed data warehouse that cannot be scaled horizontally through EC2 the way traditional application servers might be. Redshift scaling is handled through built-in features like Elastic Resize or Concurrency Scaling, not EC2 fleets. Trying to scale Redshift with EC2 is not just incorrect; it’s not even technically possible. This option simply doesn’t apply to the way Redshift architecture works.
The option that says: Export data from Redshift and import it into Amazon RDS PostgreSQL for deep audit analysis during periods of high load is incorrect. Exporting Redshift data to Amazon RDS PostgreSQL during high-load periods may sound like an alternative strategy, but it’s a step in the wrong direction. RDS PostgreSQL is designed primarily for transactional workloads, not for handling CPU-heavy, complex analytical queries. Attempting to mirror Redshift’s analytical capabilities in RDS would result in performance degradation, additional data movement pipelines, and more operational overhead. This approach is not only technically mismatched but also simply adds more cost and complexity without addressing the core issues of query concurrency and CPU pressure within Redshift itself.
 
References:
https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html
https://docs.aws.amazon.com/redshift/latest/dg/welcome.html
 
Check out this Amazon Redshift Cheat Sheet:
https://tutorialsdojo.com/amazon-redshift/

---

## Question 17

**Category:** CSAP – Accelerate Workload Migration and Modernization

A web development studio runs hundreds of Proof-of-Concept (PoC) and demo applications on virtual machines running on an on-premises server. Many of the applications are simple PHP, JavaScript or Python web applications which are no longer actively developed and serve little traffic.

As a Solutions Architect Professional, which of the following approaches would you suggest to migrate these applications to AWS with the lowest infrastructure cost and least development effort?

- A. Leverage VM Import/Export to create AMIs for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image
- B. Leverage AWS Server Migration Service (SMS) to create AMIs for each virtual machine and run each application on a dedicated EC2 instance
- **C. Dockerize each application and then deploy to an ECS cluster running behind an Application Load Balancer** ✅
- D. Migrate the application code to use a serverless stack comprising of Lambda functions and DynamoDB

### Explanation

Correct option:

Dockerize each application and then deploy to an ECS cluster running behind an Application Load Balancer

Amazon Elastic Container Service (ECS) is a highly scalable, high performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of Amazon EC2 instances.

How ECS Works:

via - https://aws.amazon.com/ecs/

Using an ECS cluster running behind an Application Load Balancer offers advantages such as Application Load Balancers allow containers to use dynamic host port mapping so that multiple tasks from the same service are allowed per container instance. This reduces the number of instances required for migration and therefore reduces the overall costs.


via - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html

Incorrect options:

Migrate the application code to use a serverless stack comprising of Lambda functions and DynamoDB - It would take significant development effort to migrate the existing applications to a serverless stack. In addition, some of the web applications, such as those built using PHP are not supported by Lambda functions (unless you use custom runtime). So, this option is incorrect.

Leverage AWS Server Migration Service (SMS) to create AMIs for each virtual machine and run each application on a separate EC2 instance - AWS Server Migration Service automates the migration of your on-premises VMware vSphere, Microsoft Hyper-V/SCVMM, and Azure virtual machines to the AWS Cloud. AWS SMS incrementally replicates your server VMs as cloud-hosted Amazon Machine Images (AMIs) ready for deployment on Amazon EC2. As this solution provisions a separate EC2 instance for each application, so it is a costly migration solution.

Leverage VM Import/Export to create AMIs for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image - VM Import/Export enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances. You can use Elastic Beanstalk to quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.

A single-instance environment doesn't have a load balancer, which can help you reduce costs compared to a load-balanced, scalable environment. Use a single-instance environment if you expect your production application to have low traffic or if you are doing remote development. For the given use-case, you will end up creating as many instances as the number of applications, which will turn out to be a really costly solution.

References:

https://aws.amazon.com/ecs/

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html

---

## Question 18

**Category:** CSAP – Continuous Improvement for Existing Solutions

A company has hired you as an AWS Certified Solutions Architect Professional to develop a deployment plan for its flagship application deployed on EC2 instances across multiple Availability Zones in the us-east-1 Region. Your solution must meet these constraints:

1) A 300 GB static dataset must be available to the application before it can be started

2) The application layer must scale on-demand with the least amount of starting time possible

3) The development team must be able to change the code multiple times in a day

4) Any patches for critical operating systems (OS) must be applied within 24 hours of release

Which of the following represents the best solution for this requirement?

- A. Leverage an Amazon-provided AMI for the OS and set up an Auto Scaling group to scale with traffic. Replace existing instances after each updated Amazon-provided AMI release. Use AWS CodeDeploy to push the application code to the instances. Configure an Amazon EC2 user data script to download the static dataset from Amazon S3
- B. Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Configure an Amazon EC2 user data script to download the static dataset from Amazon S3
- **C. Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Store and access the static dataset using Amazon EFS** ✅
- D. Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Store and access the static dataset using Amazon EBS

### Explanation

Correct option:

Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Store and access the static dataset using Amazon EFS

You can use AWS Systems Manager to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources.

For the given use case, you can leverage AWS Systems Manager to create a maintenance window, and then register an Automation task to automate the creation of the AMI. This process is applicable for both Windows and Linux instances. You can create and run a Systems Manager runbook that patches the AMI on an ongoing basis. You can then add a step that updates an Auto Scaling group with the newly patched AMI. This approach ensures that new images are automatically made available to different computing environments that use Auto Scaling groups. You can further automate the deployment of the new AMI by using a Lambda function to gracefully terminate existing instances, thereby ensuring that all instances use the latest patched AMI.


via - https://aws.amazon.com/application-migration-service/

AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers. You can use CodeDeploy to push the application code to the instances.

While EFS is a managed elastic file system designed for use across different machines and Availability Zones, EBS is designed as a fast and reliable block storage volume for single machines (although you could use EBS Multi-Attach that allows you to attach a single Provisioned IOPS SSD (io1 or io2) volume to multiple instances that are in the same Availability Zone). EFS is the right fit for the given use case as the instances are spread across multiple Availability Zones. Loading the 300 GB dataset on EFS would also ensure that this dataset is immediately available to the application on all new instances.

How EFS works:

via - https://aws.amazon.com/efs/

Incorrect options:

Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Store and access the static dataset using Amazon EBS - EBS is designed as a fast and reliable block storage volume for single machines (although you could use EBS Multi-Attach which allows you to attach a single Provisioned IOPS SSD (io1 or io2) volume to multiple instances that are in the same Availability Zone). EBS is not the right fit for the given use case as the instances are spread across multiple Availability Zones.

Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Configure an Amazon EC2 user data script to download the static dataset from Amazon S3 - Leveraging EC2 user data to download the static dataset from Amazon S3 would lead to a delay in getting the application up and running on new instances since the application depends on this static dataset before it can be started. So this option is not the best fit.

Leverage an Amazon-provided AMI for the OS and set up an Auto Scaling group to scale with traffic. Replace existing instances after each updated Amazon-provided AMI release. Use AWS CodeDeploy to push the application code to the instances. Configure an Amazon EC2 user data script to download the static dataset from Amazon S3 - It is more efficient to use the Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Leveraging EC2 user data to download the static dataset from Amazon S3 would lead to a delay in getting the application up and running on new instances since the application depends on this static dataset before it can be started. So this option is not the best fit.

References:

https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-walk-patch-windows-ami-autoscaling.html

https://aws.amazon.com/codedeploy/

---

## Question 19

**Category:** CSAP – Design for New Solutions

A global multi-player gaming application runs on UDP protocol and it needs to add functionality where you can assign multiple players to a single session on a game server based on factors such as geographic location, player skill, and a few more configurable parameters. The application is accessed by players spread out across different regions of the world.

What is the BEST way to configure this requirement?

- **A. Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC subnet endpoints** ✅
- B. Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC sharing
- C. Use custom routing accelerator of Global Accelerator in front of Network Load Balancer (NLB) to route traffic that can maintain session data
- D. Use Application Load Balancer (ALB) with sticky sessions enabled to maintain player session data. Configure Global Accelerator to front the ALB for cross-region elasticity

### Explanation

Correct option:

Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance - A custom routing accelerator is a new type of accelerator in Global Accelerator. It allows you to use your own application logic to deterministically route one or more users to a specific Amazon EC2 instance destination in a single or multiple AWS Regions. This is useful for use cases where you want to control which session on an EC2 instance your user traffic is sent to.

One example is a multi-player gaming application where you want to assign multiple players to a single session on a game server, based on factors such as geographic location, player skill, and gaming configuration. Other examples are VoIP, EdTech, and social media applications that assign multiple users to a specific media server to initiate voice, video, and messaging sessions. With a custom routing accelerator, you can direct multiple users to a unique port on your accelerator, and their traffic will be routed to a specific destination IP address and port that your application session is running on.

Custom routing accelerators support only VPC subnet endpoints, each containing one or more EC2 instances that are running your application. Each VPC subnet endpoint, which could be in a single or multiple Regions, contains the IP addresses of the EC2 instances that host your application. With a custom routing accelerator, you can put your accelerator in front of up to thousands of EC2 instances running in a single or multiple VPCs. Custom routing accelerators support VPC subnet endpoints with a maximum size of /17 and route traffic only to EC2 instances within each subnet.

Incorrect options:

Use Application Load Balancer (ALB) with sticky sessions enabled to maintain player session data. Configure Global Accelerator to front the ALB for cross-region elasticity - Application Load Balancer (ALB) cannot be used for UDP traffic. It works for HTTP and HTTPS traffic only.

Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC sharing - VPC sharing allows multiple AWS accounts to create their application resources, such as Amazon EC2 instances, Amazon Relational Database Service (RDS) databases, Amazon Redshift clusters, and AWS Lambda functions, into shared, centrally-managed virtual private clouds (VPCs). Custom routing accelerator supports only VPC subnet endpoints.

Use custom routing accelerator of Global Accelerator in front of Network Load Balancer (NLB) to route traffic that can maintain session data - As discussed above, Custom routing accelerator supports only VPC subnet endpoints.

Reference:

https://aws.amazon.com/global-accelerator/features/

---

## Question 20


**Category:** CSAP – Continuous Improvement for Existing Solutions

A bank has received a security directive to harden its cloud infrastructure in response to a wave of cyberattacks targeting financial institutions. As part of this initiative, the bank is integrating third-party firewall appliances sourced from the AWS Marketplace to perform deep inspection and control of outbound internet traffic originating from all internal workloads.
The strategy involves centralizing these firewall appliances inside a shared services VPC, serving as a security chokepoint across the organization’s cloud infrastructure. The bank’s network team has already implemented VPC routing that funnels traffic from spoke VPCs into the shared services VPC.
The cloud security engineer must design a secure and highly available inspection architecture within a single AWS Region to satisfy security requirements and uptime guarantees.
Which of the following should the cloud engineer implement to meet these goals?

- A. Provision firewall appliances across two different Availability Zones in the shared services VPC. Set up a Network Load Balancer linked to a target group that includes the appliances. Deploy a VPC interface endpoint and configure the route table to direct incoming VPC traffic to this endpoint as the next hop.
- B. Launch both firewall appliances in a single Availability Zone within the shared services VPC. Configure an Application Load Balancer and link it to a target group containing the appliances. Deploy a VPC interface endpoint and update the route table to forward traffic from connected VPCs to the endpoint as the next hop.
- C. Launch both firewall appliances in one Availability Zone within the shared services VPC. Configure a Gateway Load Balancer and associate it with a target group containing the appliances. Provision a Gateway Load Balancer endpoint and update the shared services VPC route table to use it as the next hop for incoming traffic from connected VPCs.
- **D. Place two firewall appliances in different Availability Zones in the shared services VPC. Set up a Gateway Load Balancer and link it to a target group containing both appliances. Then, deploy a Gateway Load Balancer endpoint and configure the shared services VPC route table to forward inter-VPC traffic to this endpoint as the next hop.** ✅

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		Gateway Load Balancers (GWLB) enable you to deploy, scale, and manage virtual appliances like firewalls, intrusion detection and prevention systems, and deep packet inspection systems. It combines a transparent network gateway (a single entry and exit point for all traffic) and distributes traffic while scaling your virtual appliances with the demand.
A Gateway Load Balancer operates at the third layer of the Open Systems Interconnection (OSI) model, the network layer. It listens for all IP packets across all ports and forwards traffic to the target group specified in the listener rule.
You can create a Gateway Load Balancer endpoint to connect to endpoint services powered by AWS PrivateLink. For each subnet that you specify from your VPC, we create an endpoint network interface in the subnet and assign it a private IP address from the subnet address range. An endpoint network interface is a requester-managed network interface. You can view it in your AWS account but can’t manage it yourself. You are billed for hourly usage and data processing charges.

Using a Gateway Load Balancer with firewall appliances in multiple Availability Zones ensures fault tolerance and minimal failover time. The GWLB endpoint acts as an entry point for traffic from spoke VPCs, and the route table configuration ensures that all traffic from those VPCs is inspected before reaching the internet. It is also primarily designed to handle traffic to and from virtual appliances transparently, which aligns perfectly with the stated requirements. This setup fits the goal of creating a centralized inspection point that works across zones without introducing complexity or violating AWS high availability best practices.
Hence, the correct answer is: Place two firewall appliances in different Availability Zones in the shared services VPC. Set up a Gateway Load Balancer and link it to a target group containing both appliances. Then, deploy a Gateway Load Balancer endpoint and configure the shared services VPC route table to forward inter-VPC traffic to this endpoint as the next hop.
The option that says: Launch both firewall appliances in one Availability Zone within the shared services VPC. Configure a Gateway Load Balancer and associate it with a target group containing the appliances. Provision a Gateway Load Balancer endpoint and update the shared services VPC route table to use it as the next hop for incoming traffic from connected VPCs is incorrect. This option proposes correctly using the Gateway Load Balancer and the GWLB endpoint. Still, it fails the high availability requirement because it places both firewall appliances in the same Availability Zone. This setup introduces a single point of failure, which the scenario explicitly aims to avoid. Even though the components are set up correctly, the lack of cross-AZ deployment makes it non-compliant with uptime and regulatory demands. Just distributing appliances across zones would have made it a stronger candidate.
The option that says: Provision firewall appliances across two different Availability Zones in the shared services VPC. Set up a Network Load Balancer linked to a target group that includes the appliances. Deploy a VPC interface endpoint and configure the route table to direct incoming VPC traffic to this endpoint as the next hop is incorrect. This solution attempts to distribute appliances across two Availability Zones, which is good for availability. However, it uses a Network Load Balancer and a VPC interface endpoint, neither suitable for deploying or scaling third-party firewall appliances. NLBs are primarily meant for layer 4 traffic distribution and do not support the service chaining or transparent bump-in-the-wire behavior required for deep packet inspection. This architecture simply does not meet the inspection and scalability demands for inline traffic security appliances.
The option that says: Launch both firewall appliances in a single Availability Zone within the shared services VPC. Configure an Application Load Balancer and link it to a target group containing the appliances. Deploy a VPC interface endpoint and update the route table to forward traffic from connected VPCs to the endpoint as the next hop is incorrect. It proposes an Application Load Balancer, which operates at layer 7 and is designed primarily for HTTP/HTTPS traffic. It is entirely unsuitable for routing arbitrary traffic to firewall appliances for inspection. Additionally, the deployment keeps both firewall appliances in the same Availability Zone, so it just repeats the same availability issue found in the prior option. This setup would only handle web traffic and lacks the flexibility and reliability needed for centralized traffic inspection across VPCs.
 
References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html
https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-load-balancer-endpoints.html
 
Check out this AWS Elastic Load Balancing Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

---

## Question 21

**Category:** CSAP – Continuous Improvement for Existing Solutions

A web application is hosted on Amazon EC2 instances that are fronted by Application Load Balancer (ALB) configured with an Auto Scaling group (ASG). Enhanced security is provided to the ALB by AWS WAF web ACLs. As per the company's security policy, AWS CloudTrail is activated and logs are configured to be stored on Amazon S3 and CloudWatch Logs.

A holiday sales offer was run on the application for a week. The development team has noticed that a few of the instances have rebooted taking down the log files and all temporary data with them. Initial analysis has confirmed that the incident took place during off-peak hours. Even though the incident did not cause any sales or revenue loss, the CTO has asked the development team to fix the security error that has allowed the incident to go unnoticed and eventually untraceable.

Which of the following steps will you implement to permanently record all traffic coming into the application?

- A. Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking
- B. To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring
- C. Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting
- **D. Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking** ✅

### Explanation

Correct option:

Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking

The logging destinations that you can choose from for your AWS WAF logs are:


Amazon CloudWatch Logs
Amazon Simple Storage Service
Amazon Kinesis Data Firehose


To send logs to Amazon Kinesis Data Firehose, you send logs from your web ACL to an Amazon Kinesis Data Firehose with a configured storage destination. After you enable logging, AWS WAF delivers logs to your storage destination through the HTTPS endpoint of Kinesis Data Firehose.

One AWS WAF log is equivalent to one Kinesis Data Firehose record. If you typically receive 10,000 requests per second and you enable full logs, you should have 10,000 records per second setting in Kinesis Data Firehose.

Incorrect options:

Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking - As discussed above, the logging destinations that you can choose from for your AWS WAF logs are Amazon CloudWatch Logs, Amazon Simple Storage Service, and Amazon Kinesis Data Firehose. Amazon CloudTrail is not a valid destination for WAF ACL logs.

To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring - VPC Flow You should also note that VPC Flow Logs cannot capture all traffic coming into the application as these can only capture information about the IP traffic going to and from network interfaces in your VPC. In addition, VPC Flow Logs can be directly published only to the following destinations: Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose. So this option is incorrect.

Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting - Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. Elastic Load Balancing access logs are stored in Amazon S3 buckets and it is not possible to directly write the logs to Kinesis Data Firehose.

References:

https://aws.amazon.com/about-aws/whats-new/2021/12/awf-waf-cloudwatch-log-s3-bucket/

https://docs.aws.amazon.com/waf/latest/developerguide/logging-destinations.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

---

## Question 22


**Category:** CSAP – Design Solutions for Organizational Complexity

A global enterprise manages multiple AWS accounts under a single organization using AWS Organizations. The enterprise leverages AWS CloudFormation to automate infrastructure provisioning and centrally manages permissions and roles using AWS Identity and Access Management (IAM).
As part of a new chargeback model, the finance department requires each department to apply project tags selected from a predefined list of tag values to every newly created resource.
When analyzing spending using the AWS Cost and Usage Report in AWS Cost Explorer, the finance team identified non-compliant tag values that disrupted cost attribution.
To enforce compliance, the company needs a scalable way to validate and implement resource tagging based on these project values.
Which approach offers the easiest and most effective way to enforce this?

- A. Enable resource tagging enforcement using AWS Config rules. Integrate the rules with Organizations to evaluate tag compliance across accounts. Use automation documents to prevent cloudformation:CreateStack unless tags meet policy requirements.
- **B. In the organization’s management account, define a tag policy with valid project tag values. Then, create a Service Control Policy (SCP) to deny cloudformation:CreateStack except if the required project tag is included. Attach the created SCP to the root of the organization.** ✅
- C. Configure a tag policy in the Organizations management account to specify the approved project tag values. Then, implement an SCP that blocks the cloudformation:DetectStackResourceDrift operation unless a compliant project tag is part of the request. Apply this SCP at the organization’s root level.
- D. Use the AWS Tag Editor to audit and correct resource tags across all accounts. Schedule periodic reviews to identify non-compliant tags and update them to match the predefined project tag list

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		Defining a tag policy in the AWS Organizations management account ensures all accounts have standardized approved project tag values. Although tag policies alone cannot enforce tag usage, they enable visibility into tag compliance across the organization.
Enforcing tag compliance, on the other hand, is effectively handled using a Service Control Policy (SCP) that denies the cloudformation:CreateStack operation unless a required project tag is included.
AWS separates governance from enforcement to provide organizations with flexibility, gradual adoption, and control over how policies are introduced and applied across accounts. Regarding tag policies within AWS Organizations, governance tools are designed to define standards, guide behavior, and report compliance without immediately disrupting workflows. This allows organizations to monitor tagging hygiene, educate teams, and identify non-compliant patterns before applying hard restrictions. In contrast, Service Control Policies (SCPs) are enforcement mechanisms that strictly prevent specific actions, such as creating resources without required tags, regardless of IAM permissions. By separating these functions, AWS enables a phased approach: organizations can start with visibility and alignment through governance and then escalate to enforcement when ready, reducing the risk of unintended disruptions while improving long-term operational consistency.

A combination of Organization Tag Policy and SCPs uses a combined governance and enforcement approach that meets the question’s scalability, compliance, and effectiveness requirements.
Hence, the correct answer is: In the organization’s management account, define a tag policy with valid project tag values. Then, create a Service Control Policy (SCP) to deny cloudformation:CreateStack except if the required project tag is included. Attach the created SCP to the root of the organization.
The option that says: Enable resource tagging enforcement using AWS Config rules. Integrate the rules with Organizations to evaluate tag compliance across accounts. Use automation documents to prevent cloudformation:CreateStack unless tags meet policy requirements is incorrect. AWS Config rules operate after resource creation and do not natively prevent API actions like cloudformation:CreateStack. While integrating AWS Config with AWS Organizations enables centralized tag compliance checks, it only provides post-creation evaluation. Automation documents (SSM documents) can remediate or notify but cannot block the initial stack creation in real-time. As a result, non-compliant resources can still be launched, violating the requirement to enforce tagging at creation.
The option that says: Configure a tag policy in the Organizations management account to specify the approved project tag values. Then, implement an SCP that blocks the cloudformation:DetectStackResourceDrift operation unless a compliant project tag is part of the request. Apply this SCP at the organization’s root level is incorrect. It targets an API operation unrelated to resource creation where tag enforcement must occur. While defining a tag policy in the AWS Organizations management account helps establish governance, denying cloudformation:DetectStackResourceDrift is ineffective. This action is used for diagnostics and does not create, modify, or tag resources. Blocking it does nothing to prevent the deployment of resources with invalid or missing tags.
The option that says: Use the AWS Tag Editor to audit and correct resource tags across all accounts. Schedule periodic reviews to identify non-compliant tags and update them to match the predefined project tag list is incorrect. While AWS Tag Editor can be used to search and edit tags across multiple accounts and regions, it does not provide any mechanism for enforcement. It cannot block resource creation or validate tag values against a predefined list. It only allows administrators to inspect and modify tags manually after the fact. Also, relying on scheduled manual reviews introduces operational overhead, delays in enforcement, and a high risk of human error or oversight. Finally, although Tag Editor supports visibility, it offers no integration with AWS Organizations governance policies like tag policies or SCPs, and it does not prevent the use of non-compliant project tags during provisioning.
 
References:
https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html
 
Check out this AWS Organizations Cheat Sheet:
https://tutorialsdojo.com/aws-organizations/

---

## Question 23

**Category:** CSAP – Continuous Improvement for Existing Solutions

An e-commerce company has hired an AWS Certified Solutions Architect Professional to transform a standard three-tier web application architecture in AWS. Currently, the web and application tiers run on EC2 instances and the database tier runs on RDS MySQL. The company wants to redesign the web and application tiers to use API Gateway with Lambda Functions with the final goal of deploying the new application within 6 months. As an immediate short-term task, the Engineering Manager has mandated the Solutions Architect to reduce costs for the existing stack.

Which of the following options should the Solutions Architect recommend as the MOST cost-effective and reliable solution?

- A. Provision Reserved Instances for the web and application tiers and On-Demand Instances for the database tier
- B. Provision Reserved Instances for the web, application and database tiers
- C. Provision Spot Instances for the web and application tiers and Reserved Instances for the database tier
- **D. Provision On-Demand Instances for the web and application tiers and Reserved Instances for the database tier** ✅

### Explanation

Correct option:

Provision On-Demand Instances for the web and application tiers and Reserved Instances for the database tier

EC2 Instances support five different ways to pay for provisioning the servers: On-Demand, Savings Plans, Reserved Instances, Spot Instances and Dedicated Hosts.


via - https://aws.amazon.com/ec2/pricing/

An On-Demand Instance is an instance that you use on-demand. You have full control over its lifecycle — you decide when to launch, stop, hibernate, start, reboot, or terminate it. There is no long-term commitment required when you purchase On-Demand Instances. There is no upfront payment and you pay only for the seconds that your On-Demand Instances are running. The price per second for running an On-Demand Instance is fixed. On-demand instances cannot be interrupted. However, On-demand instances are not as cost-effective as Reserved instances.

A Spot Instance is an unused EC2 instance that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts (up to 90%), you can lower your Amazon EC2 costs significantly. Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks. These can be terminated at short notice, so these are not suitable for critical workloads that need to run at a specific point in time.

Reserved Instances provide you with significant savings (up to 75%) on your Amazon EC2 costs compared to On-Demand Instance pricing. Reserved Instances are not physical instances, but rather a billing discount applied to the use of On-Demand Instances in your account. You can purchase a Reserved Instance for a one-year or three-year commitment, with the three-year commitment offering a bigger discount. Reserved instances cannot be interrupted.

For the given use-case, only the web and application tiers would be re-engineered using API Gateway and Lambda within a duration of 6 months, so you cannot use Reserved Instances for these tiers as the minimum duration to purchase a Reserved Instance is 1 year. Additionally, using Spot Instances for these tiers is also ruled out because these can be terminated at short notice and would not be able to offer reliability for the web and application tiers. Therefore On-Demand is the best option for the web and application tiers. As the proposed transformation would not impact the database tier running on RDS MySQL, therefore you can purchase Reserved Instances for the database tier as the most cost-effective solution.

Incorrect options:

Provision Reserved Instances for the web, application and database tiers - As explained above, Reserved Instances are not a good fit for running the web and application tiers, so this option is not correct.

Provision Spot Instances for the web and application tiers and Reserved Instances for the database tier - As explained above, Spot Instances are not a good fit for running the web and application tiers, so this option is not correct.

Provision Reserved Instances for the web and application tiers and On-Demand Instances for the database tier - As explained above, Reserved Instances are not a good fit for running the web and application tiers, so this option is not correct. Also using On-Demand Instances for the database tier is not the most cost-effective option as you should use Reserved Instances for the database tier.

Reference:

https://aws.amazon.com/ec2/pricing/

---

## Question 24

**Category:** CSAP – Accelerate Workload Migration and Modernization

A Wall Street based trading firm is modernizing its message queuing system by migrating from self-managed message-oriented middleware systems to Amazon SQS. The firm is using SQS to migrate several trading applications to the cloud to ensure high availability and cost efficiency while simplifying administrative complexity and overhead. The development team at the firm expects a peak rate of about 2,400 messages per second to be processed via SQS. It is important that the messages are processed in the order they are received.

Which of the following options can be used to implement this system in the most cost-effective way?

- **A. Use Amazon SQS FIFO queue in batch mode of 8 messages per operation to process the messages at the peak rate** ✅
- B. Use Amazon SQS FIFO queue in batch mode of 12 messages per operation to process the messages at the peak rate
- C. Use Amazon SQS FIFO queue in batch mode of 4 messages per operation to process the messages at the peak rate
- D. Use Amazon SQS standard queue to process the messages

### Explanation

Correct option:

Use Amazon SQS FIFO queue in batch mode of 8 messages per operation to process the messages at the peak rate

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues - Standard queues vs FIFO queues.

For FIFO queues, the order in which messages are sent and received is strictly preserved (i.e. First-In-First-Out). On the other hand, the standard SQS queues offer best-effort ordering. This means that occasionally, messages might be delivered in an order different from which they were sent.

By default, FIFO queues support up to 300 messages (API calls) per second (300 send, receive, or delete operations per second). When you batch 10 messages per operation (maximum), FIFO queues can support up to 3,000 (300*10) messages per second. Therefore, you need to process 8 messages per operation so that the FIFO queue can support up to 2,400 (300*8) messages per second, which satisfies the peak rate constraint.

FIFO Queues Overview:

via - https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html

Incorrect options:

Use Amazon SQS standard queue to process the messages - As messages need to be processed in order, therefore standard queues are ruled out.

Use Amazon SQS FIFO queue in batch mode of 12 messages per operation to process the messages at the peak rate - This option has been added as a distractor, as SQS FIFO only supports a maximum of 10 messages per operation in batch mode.

Use Amazon SQS FIFO queue in batch mode of 4 messages per operation to process the messages at the peak rate - As mentioned earlier in the explanation, you need to use FIFO queues in batch mode and process 8 messages per operation, so that the FIFO queue can support up to 2,400 messages per second. With 4 messages per operation, you can only support up to 1,200 messages per second.

References:

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html

https://aws.amazon.com/sqs/

https://aws.amazon.com/sqs/features/

---

## Question 25

**Category:** CSAP – Design for New Solutions

A data analytics company uses Amazon S3 as the data lake to store the input data that is ingested from the IoT field devices on an hourly basis. The ingested data has attributes such as the device type, ID of the device, the status of the device, the timestamp of the event, the source IP address, etc. The data runs into millions of records per day and the company wants to run complex analytical queries on this data daily for product improvements for each device type.

Which is the most optimal way to save this data to get the best performance from the millions of data points processed daily?

- **A. Store the data in Apache ORC, partitioned by date and sorted by device type of the device** ✅
- B. Store the data in compressed .csv, partitioned by date and sorted by the status of the device
- C. Store the data in compressed .csv, partitioned by date and sorted by device type
- D. Store the data in Apache Parquet, partitioned by device type and sorted by date

### Explanation

Correct option:

Store the data in Apache ORC, partitioned by date and sorted by device type of the device - Apache Parquet and ORC are columnar storage formats that are optimized for fast retrieval of data and used in AWS analytical applications.

By partitioning your data, you can restrict the amount of data scanned by each query, thus improving performance and reducing cost. You can partition your data by any key. A common practice is to partition the data based on time, often leading to a multi-level partitioning scheme. For example, a customer who has data coming in every hour might decide to partition by year, month, date, and hour. Another customer, who has data coming from many different sources but that is loaded only once per day, might partition by a data source identifier and date.

For the given use case, as the company does daily analysis, so it only needs to look at the data generated for a given date. Hence partitioning by date offers significant performance and cost advantages. Since the company also wants to analyze product improvements for each device type, it is better to keep the data sorted by device type, so it allows for faster query execution.

Incorrect options:

Store the data in Apache Parquet, partitioned by device type and sorted by date -  Apache Parquet is a columnar storage format that is optimized for fast retrieval of data and used in AWS analytical applications. However, partitioning by device type is incorrect for this use case, and partitioning by date is optimal.

Store the data in compressed .csv, partitioned by date and sorted by the status of the device

Store the data in compressed .csv, partitioned by date and sorted by device type

Both the above options are not columnar storage formats, they are row-based formats that are not optimal for big data retrievals for complex analytical queries.

Reference:

https://docs.aws.amazon.com/athena/latest/ug/partitions.html

---

## Question 26


**Category:** CSAP – Design Solutions for Organizational Complexity

A North American-based tech startup plans to expand to Europe due to the unexpected, overwhelming success of its software-as-a-service (SaaS) solution, which uses AWS AppFabric for SaaS integration and security observability. A solutions architect consultant was hired to design and execute the expansion.
The company uses the us-east-1 Region for its North American infrastructure. The system uses Amazon S3, which is accessed through Amazon CloudFront, as its front-end component. It uses Amazon API Gateway for the API endpoints. AWS Lambda functions connected to an Amazon RDS for MySQL serve as its backend and persistence layer. Amazon Route 53 manages the domain via a simple routing policy pointing to the API Gateway.
In anticipation of the upcoming expansion, the engineering team proactively provisioned eu-west-1 Region infrastructure, including API Gateways and Lambda functions in the mentioned Region.
Initial measurements of the consultant suggest that around 95% of the database traffic is read-only.
What approach can the consultant take to expand on the existing eu-west-1 Region and ensure minimal latency for users in the Europe Region?

- **A. In Route 53, use latency-based routing. Set up a cross-Region read replica of the database in eu-west-1.** ✅
- B. Use latency-based routing in Route 53 to direct traffic to the appropriate API  endpoint. Configure an AWS Database Migration Service (AWS DMS) task with change data capture (CDC) for replication of the main database from the us-east-1 to eu-west-1 .
- C. Use failover routing in Route 53. Create a Multi-AZ replica of the primary database.
- D. Keep simple routing in Route 53 for minimal setup. Set up an AWS Database Migration Service (AWS DMS) task with full load combined with change data capture (CDC) to replicate the original database from us-east-1 to eu-west-1.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		To minimize latency for European users accessing a report-generation platform, the key objective is to bring data and computing closer to users in the European Region. The scenario highlights that over 95% of the database workload is read-only, indicating that read scalability through replication is a viable and preferred solution. Also, the infrastructure in eu-west-1 (API Gateway + Lambda) has already been deployed, so we only need to ensure data consistency and fast access in that region.
We can reduce latency by the following approach:
1. Cross-Region read replica ensures that read-only queries (which comprise 90% of the load) are offloaded from the primary us-east-1 database and served locally in eu-west-1, reducing cross-Region latency and data transfer.
2. Latency-based routing in Amazon Route 53 ensures that European users are routed to the fastest (often the nearest) API Gateway + Lambda stack in eu-west-1.

Since RDS cross-Region read replicas are designed for scaling reads globally, and Route 53 can route to the correct endpoint, this setup provides an efficient and scalable architecture.
Hence, the correct answer is: In Route 53, use latency-based routing. Set up a cross-Region read replica of the database in eu-west-1.
The option that says: Use latency-based routing in Route53 to direct traffic to the appropriate API endpoint. Configure an AWS Database Migration Service (AWS DMS) task with change data capture (CDC) for replication of the main database from the us-east-1 to eu-west-1 is incorrect. AWS DMS with CDC can replicate data across Regions, but it is not designed for real-time, low-latency read access in high-throughput applications. DMS is only meant for data migration, warehousing, or hybrid environments, not for scalable, low-latency read operations in production. Additionally, DMS adds complexity and operational overhead, including managing replication tasks and monitoring lag.
The option that says: Use failover routing in Route 53. Create a Multi-AZ replica of the primary database is incorrect. Failover routing in Route 53 is designed to improve availability during outages by routing traffic to a healthy endpoint if the primary fails. It does not facilitate latency-based traffic distribution between Regions. Additionally, Multi-AZ deployments are confined to a single Region. You cannot create a Multi-AZ read replica across Regions; they are designed to provide high availability within the same Region only.
The option that says: Keep simple routing in Route 53 for minimal setup. Set up an AWS Database Migration Service (AWS DMS) task with full load combined with change data capture (CDC) to replicate the original database from us-east-1 to eu-west-1 is incorrect. First, simple routing does not differentiate traffic based on Region or latency. All users are directed to a single endpoint, defeating the goal of optimizing for European users. Second, AWS DMS is not the right tool for real-time production read replicas, as with the first option. It introduces lag and does not scale efficiently for large volumes of read traffic.
 
References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html
 
Check out this Amazon Aurora Cheat Sheet:
https://tutorialsdojo.com/amazon-aurora/

---

## Question 27

**Category:** CSAP – Continuous Improvement for Existing Solutions

A web hosting company's CFO recently analyzed the company's monthly bill for the AWS account for the development environment and identified an opportunity to reduce the cost for AWS Elastic Beanstalk infrastructure in use. The CFO in consultation with the CTO has hired you as an AWS Certified Solutions Architect Professional to design a highly available solution that will provision an Elastic Beanstalk environment in the morning and terminate it at the end of the day. The solution should be designed with minimal operational overhead with a focus on minimizing costs. The solution should also facilitate the increased use of Elastic Beanstalk environments among different development teams and must provide a one-stop scheduler solution for all teams to keep the operational costs as low as possible.

Which of the following solution designs will you suggest to address these requirements?

- A. Provision an EC2 Micro instance. Configure an IAM role with the required Elastic Beanstalk environment permissions and attach it to the instance profile. Create scripts on the instance to provision and terminate the Elastic Beanstalk environment. Set up cron jobs on the instance to execute the scripts
- B. Leverage the activity task of an AWS Step Function to provision and terminate the Elastic Beanstalk environment. Create a role for the Step Function to allow it to provision and terminate the Elastic Beanstalk environment. Execute the Step Function daily and use the "wait state" to control the start and stop time
- C. Configure the Elastic Beanstalk environment to use custom commands in the EC2 instance user data. Leverage the scheduled action for an Auto Scaling group to scale-out EC2 instances in the morning and scale-in the instance count to 0 to terminate the EC2 instances at the end of the day
- **D. Set up separate Lambda functions to provision and terminate the Elastic Beanstalk environment. Configure a Lambda execution role granting the required Elastic Beanstalk environment permissions and assign the role to the Lambda functions. Configure cron expression based Amazon EventBridge events rules to trigger the Lambda functions** ✅

### Explanation

Correct option:

Set up separate Lambda functions to provision and terminate the Elastic Beanstalk environment. Configure a Lambda execution role granting the required Elastic Beanstalk environment permissions and assign the role to the Lambda functions. Configure cron expression based Amazon EventBridge events rules to trigger the Lambda functions

You can configure Lambda functions to make the Elastic Beanstalk API calls for provisioning and terminating the Elastic Beanstalk environment. To perform these API calls on a schedule, you can configure events in Amazon EventBridge events to trigger these Lambda functions at a specific time each day via cron expressions. Make sure that you attach the policy with the required Elastic Beanstalk environment permissions to the Lambda execution role.


via - https://aws.amazon.com/premiumsupport/knowledge-center/schedule-elastic-beanstalk-stop-restart/


via - https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html

Please review this excellent reference material for a deep-dive on how to stop and restart an Elastic Beanstalk environment on a schedule:

https://aws.amazon.com/premiumsupport/knowledge-center/schedule-elastic-beanstalk-stop-restart/

Incorrect options:

Leverage the activity task of an AWS Step Function to provision and terminate the Elastic Beanstalk environment. Create a role for the Step Function to allow it to provision and terminate the Elastic Beanstalk environment. Execute the Step Function daily and use the "wait state" to control the start and stop time - AWS Step Functions lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using Step Functions, you can design and run workflows that stitch together services such as AWS Lambda into feature-rich applications.


via - https://aws.amazon.com/step-functions/

This option involves cost components that are not needed. There is no need to keep the Step Function running in a "wait state" for the most part of the day just to control the provisioning and termination of Elastic Beanstalk environment. This is better handled via a "serverless cron" type of solution that can be invoked twice a day for provisioning and termination of Elastic Beanstalk environment.

Configure the Elastic Beanstalk environment to use custom commands in the EC2 instance user data. Leverage the scheduled action for an Auto Scaling group to scale-out EC2 instances in the morning and scale-in the instance count to 0 to terminate the EC2 instances at the end of the day - Scheduled action allows you to set your own scaling schedule for an Auto Scaling group. For example, let's say that every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can plan your scaling actions based on the predictable traffic patterns of your web application. Scaling actions are performed automatically as a function of time and date. A scheduled action sets the minimum, maximum, and desired sizes to what is specified by the scheduled action at the time specified by the scheduled action.

The issue with this option is that it's costly. Firstly, there is a cost element of running the EC2 instances for the day hours. Secondly, Elastic Beanstalk environment is provisioned via custom commands in the EC2 instance user data (it should also be emphasized that EC2 instance user data is not the best place to trigger the creation of an Elastic Beanstalk environment) however the environment itself is not terminated at the end of the day. So the costs for the resources created by Elastic Beanstalk keep accumulating. Hence this option is incorrect.

Provision an EC2 Micro instance. Configure an IAM role with the required Elastic Beanstalk environment permissions and attach it to the instance profile. Create scripts on the instance to provision and terminate the Elastic Beanstalk environment. Set up cron jobs on the instance to execute the scripts - This option involves cost components that are not needed. There is no need to provision an EC2 Micro instance and keep it running just to control the provisioning and termination of Elastic Beanstalk environment. This is better handled via a "serverless cron" type of solution that can be invoked twice a day for provisioning and termination of Elastic Beanstalk environment.

References:

https://aws.amazon.com/premiumsupport/knowledge-center/schedule-elastic-beanstalk-stop-restart/

https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html

https://aws.amazon.com/step-functions/

---

## Question 28

**Category:** CSAP – Continuous Improvement for Existing Solutions

The development team at a company has noticed issues with the Quality of Service (QoS) in the traffic to the EC2 instances hosting a VOIP program. The team needs to inspect the network packets to determine if it is a programming error or a networking error.

As an AWS Certified Solutions Architect Professional, which of the following options would you suggest for the given use case?

- **A. Configure traffic mirroring on the source EC2 instances hosting the VOIP program, set up a network monitoring program on a target EC2 instance and stream the logs to an S3 bucket for further analysis** ✅
- B. Use CloudWatch to inspect the network packets
- C. Provision another EC2 instance with an ENI added to act as a monitoring interface. Configure the port to promiscuous mode and sniff the traffic to analyze the packets. Direct the output of this single stream to an S3 bucket for further analysis
- D. Use VPC Flow Logs to inspect the network packets

### Explanation

Correct option:

Configure traffic mirroring on the source EC2 instances hosting the VOIP program, set up a network monitoring program on a target EC2 instance and stream the logs to an S3 bucket for further analysis

Quality of Service (QoS) is a set of technologies that enable a network to dependably run high-priority applications and traffic under limited network capacity. QoS technologies accomplish this by providing differentiated handling and capacity allocation to specific flows in network traffic. Bandwidth (throughput), latency (delay), jitter (variance in latency), and error rate are the metrics relevant to QoS. This implies that QoS is of particular importance to high-bandwidth, real-time traffic such as voice over IP (VoIP), video conferencing, and video-on-demand that have a high sensitivity to latency and jitter.

Generally, the promiscuous mode allows the user to bypass the normal operation mode by forwarding all traffic it receives to the CPU. However for AWS, even if you can turn your NIC to Promiscuous mode, the hypervisor will never pass traffic intended for another virtual machine to your EC2 instance. You need to use traffic mirroring as it allows you to copy traffic passing through an elastic network adaptor and send it toward another instance for further investigation. For the given use case, you need to set up traffic mirroring on the source EC2 instances hosting the VOIP program and then install a network monitoring program (such as Wireshark) on the traffic mirroring target EC2 instance. Finally, you can stream the logs from the target EC2 instance to an S3 bucket for further analysis.

Incorrect options:

Use CloudWatch to inspect the network packets - Amazon CloudWatch is a monitoring service for AWS cloud resources and the applications you run on AWS. You can use Amazon CloudWatch to collect and track metrics, collect and monitor log files, and set alarms. CloudWatch cannot be used to inspect the network packets.

Use VPC Flow Logs to inspect the network packets - VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored. VPC Flow Logs cannot be used to inspect the network packets.

Provision another EC2 instance with an ENI added to act as a monitoring interface. Configure the port to promiscuous mode and sniff the traffic to analyze the packets. Direct the output of this single stream to an S3 bucket for further analysis - Amazon EC2 instances running with an Amazon VPC have built-in protection against packet sniffing. It is not possible for a virtual instance running in promiscuous mode to receive or “sniff” traffic that is intended for a different virtual instance. While customers can place their interfaces into promiscuous mode, the hypervisor will not deliver any traffic to them that is not addressed to them. Even two virtual instances that are owned by the same customer located on the same physical host cannot listen to each other’s traffic. So this option is incorrect.

References:

https://d1.awsstatic.com/whitepapers/Security/Networking_Security_Whitepaper.pdf

https://medium.com/@macsat101/packet-sniffing-using-wireshark-on-aws-183b7983685d

https://www.paloaltonetworks.com/cyberpedia/what-is-quality-of-service-qos

---

## Question 29

**Category:** CSAP – Design for New Solutions

An e-commerce company manages its flagship applications on AWS. The Amazon EC2 instances running the applications are fronted by an Application Load Balancer (ALB). Amazon Route 53 provides public DNS services. Different URLs (mobile.ecomm.com, web.ecomm.com, api.ecomm.com) will serve the required content to the end-users.

As an AWS Certified Solutions Architect Professional, which combination of services would you use to serve the content to the end-users? (Select two)

- A. Use Path conditions in ALB listener to route *.ecomm.com to appropriate target groups
- **B. Use Host conditions in ALB listener to route *.ecomm.com to appropriate target groups** ✅
- C. Use Host conditions in ALB listener to route $$$$.ecomm.com to appropriate target groups
- **D. Use Host conditions in ALB listener to route ecomm.com to appropriate target groups** ✅
- E. Use Path component of Redirect actions in ALB listener configuration to route ecomm.com to appropriate target groups

### Explanation

Correct options:

Use Host conditions in ALB listener to route *.ecomm.com to appropriate target groups

Use Host conditions in ALB listener to route ecomm.com to appropriate target groups

You can use host conditions to define rules that route requests based on the hostname in the host header (also known as host-based routing). This enables you to support multiple subdomains and different top-level domains using a single load balancer.

A hostname is not case-sensitive, can be up to 128 characters in length, and can contain any of the following characters:
1. A–Z, a–z, 0–9
2. - .
3. * (matches 0 or more characters)
4. ? (matches exactly 1 character)

You must include at least one "." character. You can include only alphabetical characters after the final "." character.

Example hostnames: example.com, test.example.com, *.example.com

The rule *.example.com matches test.example.com but doesn't match example.com. Hence, we also need to include ecomm.com along with *.ecomm.com to include all the hosts serving the requests.

Incorrect options:

Use Path component of Redirect actions in ALB listener configuration to route ecomm.com to appropriate target groups - You can use redirect actions to redirect client requests from one URL to another. The path component has an absolute path, starting with the leading "/". A path is case-sensitive, can be up to 128 characters in length, and consists of alphanumeric characters, wildcards (* and ?), & (using &), and the following special characters: _-.$/~"'@:+. This option is not useful for the given scenario.

Use Host conditions in ALB listener to route $$$$.ecomm.com to appropriate target groups - As discussed above, - ., * or ? can be used. '$' is not a valid character.

Use Path conditions in ALB listener to route *.ecomm.com to appropriate target groups - The path component has an absolute path, starting with the leading "/". Example HTTP path patterns /img/*, /img/*/pics, etc. It does not help while dealing with hostnames, as required for the given scenario.

Reference:

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html

---

## Question 30


**Category:** CSAP – Design Solutions for Organizational Complexity

A financial institution is running multiple AWS Lambda functions. These functions are packaged as .zip archives and rely on a shared Lambda layer that contains common libraries.
Security compliance requires that the development team must:


Continuously monitor the Lambda functions and the shared Lambda layer for current common vulnerabilities and exposures (CVEs).


Perform additional automated code scans on a subset of Lambda functions to detect data leaks and injection flaws.


Ensure that not all Lambda functions are scanned for code issues, since some workloads handle non-sensitive test data.


The company wants a fully managed AWS-native solution to meet these requirements.


Which of the following will meet the given requirements? (Select THREE.)

- **A. Apply an Amazon Inspector exclusion tag with a key of InspectorCodeExclusion and a value of LambdaCodeScanning to Lambda functions that should not be code-scanned.** ✅
- **B. Enable Amazon Inspector Lambda code scanning to detect code-level vulnerabilities.** ✅
- C. Use AWS IAM policies to restrict Amazon Inspector from scanning specific Lambda functions.
- D. Use Amazon GuardDuty Lambda Protection to monitor for CVEs and data leaks.
- E. Enable AWS Config with a custom rule to check Lambda deployment packages for CVEs.
- **F. Enable Amazon Inspector and activate Lambda standard scanning for CVE detection.** ✅

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		Amazon Inspector is a vulnerability management service that automatically identifies workloads and continuously scans them for software vulnerabilities and unintended network exposure. It can discover and scan Amazon EC2 instances, container images in Amazon ECR, and Lambda functions. When Amazon Inspector detects a software vulnerability or unintended network exposure, it generates a finding—a detailed report that outlines the issue. You can manage these findings through the Amazon Inspector console or API.
Amazon Inspector supports security vulnerability assessments for AWS Lambda functions and layers, providing continuous automated scanning. It offers two types of scanning for Lambda functions:
– Amazon Inspector Lambda standard scanning – This scan type is the default Lambda scan type. It scans application dependencies in Lambda functions and layers for package vulnerabilities.
– Amazon Inspector Lambda code scanning – This scan type scans custom application code in your Lambda functions and layers for code vulnerabilities. You can activate Lambda standard scanning or Lambda standard scanning with Lambda code scanning.
If you want to activate Lambda code scanning, you must first enable standard scanning.

You can add tags to Lambda functions to exclude them from Amazon Inspector’s Lambda code scans. Excluding functions from scans can help prevent receiving unactionable alerts. To tag a function for exclusion, use the following key-value pair for the tag.
– Key – InspectorCodeExclusion
– Value – LambdaCodeScanning
Hence, the correct answers are:
– Enable Amazon Inspector and activate Lambda standard scanning for CVE detection. It enables continuous, automated scanning of Lambda function deployment packages and layers for known vulnerabilities (CVEs).
– Enable Amazon Inspector Lambda code scanning to detect code-level vulnerabilities. It allows Amazon Inspector to perform static code analysis on Lambda functions to detect issues like injection flaws and data leaks. This meets the requirement for automated code scans on a subset of functions handling sensitive data.
– Apply an Amazon Inspector exclusion tag with a key of InspectorCodeExclusion and a value of LambdaCodeScanning to Lambda functions that should not be code-scanned. It provides a native way to exclude specific Lambda functions from code scanning. This ensures that functions handling non-sensitive test data are not unnecessarily scanned, aligning with the compliance requirement.
The option that says: Enable AWS Config with a custom rule to check Lambda deployment packages for CVEs is incorrect because AWS Config does not primarily support vulnerability scanning. While it can track configuration changes and compliance, it cannot inspect Lambda packages for CVEs without external tooling or custom logic.
The option that says: Use Amazon GuardDuty Lambda Protection to monitor for CVEs and data leaks is incorrect because GuardDuty focuses on detecting runtime threats and anomalous behavior, not static vulnerabilities like CVEs or code-level flaws. It does not scan deployment packages or source code for vulnerabilities.
The option that says: Use AWS IAM policies to restrict Amazon Inspector from scanning specific Lambda functions is incorrect because Amazon Inspector does not use IAM policies to control scanning scope at the function level. Instead, it typically relies on tagging mechanisms for exclusions.
 
References:
https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html
https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html
https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_code_exclude_functions.html
 
Check out this Amazon Inspector Cheat Sheet:
https://tutorialsdojo.com/amazon-inspector/

---

## Question 31


**Category:** CSAP – Design for New Solutions

A genome research facility uses AWS Step Functions to orchestrate a nightly machine learning pipeline that retrains predictive models to discover potential cancer cures. The pipeline consists of multiple AWS Lambda tasks responsible for parsing genomic data, running simulations, and optimizing hyperparameters. Each step is time-sensitive and mission-critical.
Recently, the research team discovered that if even a single state within the Step Functions workflow encounters an error, whether during data processing, model training, or evaluation, the entire retraining sequence fails silently, and no alerts are sent. As a result, several nights of crucial model updates were missed without the team’s knowledge.
The solutions architect must implement a failure detection and notification system to avoid these unseen interruptions. This solution should immediately alert the team by email anytime a Task, Map, or Parallel state fails. The alert must include the original input arguments that triggered the failure, enabling rapid diagnosis and response.
Which action should the architect take to design this system?

- **A. Set up an Amazon SNS topic and configure an Email-type subscription that delivers messages to the group’s distribution address. Define a Task state called “Email” that sends the state’s input parameters to the SNS topic. For every Task, Map, and Parallel state, add a Catch clause that matches  "ErrorEquals": ["States.ALL"], and routes the flow to the “Email” state via the “Next” field.** ✅
- B. Enable AWS X-Ray on all Lambda functions in the workflow to trace failed invocations. Implement a Catch clause in all Task, Map, and Parallel states, setting "ErrorEquals": ["States.ALL"] to handle any failure type. Route execution to the “Email” state through the “Next” property whenever an error is intercepted.
- C. Provision an Amazon SNS topic and attach an Email-based subscription that routes notifications to the team’s group inbox. Introduce a Task state labeled “Email” that passes along the received input to the SNS topic. For each Task, Map, and Parallel state, include a Catch block configured with  "ErrorEquals": ["States.Runtime"] and direct control to the “Email” state using the “Next” parameter.
- D. Use Amazon EventBridge to monitor the execution history of the Step Functions. Add a Catch handler to every Task, Map, and Parallel state, specifying "ErrorEquals": ["States.Runtime"] to capture runtime-related issues. Use the “Next” field to transition the flow to the “Email” state upon encountering such errors.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		With AWS Step Functions, you can create workflows called State machines to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning pipelines.
Step Functions is based on state machines and tasks. In Step Functions, state machines are a series of event-driven steps. Each step in a workflow is called a state. For example, a Task state represents a unit of work that another AWS service performs, such as calling an AWS Lambda function or API. Instances of running workflows performing tasks are called executions in Step Functions.

By using "ErrorEquals": ["States.ALL"] in Step Functions, the solution ensures that all possible errors are caught, whether runtime, timeout, permissions, or others. It also incorporates Amazon SNS with an email subscription to notify the team instantly, and the “Email” Task is designed to pass along the input arguments, allowing the researchers to diagnose what caused the failure quickly. This approach is thorough and aligns directly with AWS best practices for robust error handling and alerting in mission-critical workflows.
Hence, the correct answer is: Set up an Amazon SNS topic and configure an Email-type subscription that delivers messages to the group’s distribution address. Define a Task state called “Email” that sends the state’s input parameters to the SNS topic. For every Task, Map, and Parallel state, add a Catch clause that matches  "ErrorEquals": ["States.ALL"], and routes the flow to the “Email” state via the “Next” field.
The option that says: Provision an Amazon SNS topic and attach an Email-based subscription that routes notifications to the team’s group inbox. Introduce a Task state labeled “Email” that passes along the received input to the SNS topic. For each Task, Map, and Parallel state, include a Catch block configured with  "ErrorEquals": ["States.Runtime"] and direct control to the “Email” state using the “Next” parameter is incorrect. This solution uses "ErrorEquals": ["States.Runtime"], which only captures a subset of errors, primarily those related to runtime execution, like timeouts or failures in the Lambda function itself. It does not catch other common failure types, such as permission errors or input validation issues. Using "States.ALL" is essential to ensure the system responds to any failure, not just a specific category.
The option that says: Use Amazon EventBridge to monitor the execution history of the Step Functions. Add a Catch handler to every Task, Map, and Parallel state, specifying "ErrorEquals": ["States.Runtime"] to capture runtime-related issues. Use the “Next” field to transition the flow to the “Email” state upon encountering such errors is incorrect. This option includes Amazon EventBridge, which is not needed in this context. Step Functions already has built-in support for error handling using Catch blocks, and the requirement is to alert on each state failure, not just monitor overall workflow executions. EventBridge primarily helps with state change events, but it simply does not offer granular control or direct access to the input arguments at the state level as Step Functions does natively.
The option that says: Enable AWS X-Ray on all Lambda functions in the workflow to trace failed invocations. Implement a Catch clause in all Task, Map, and Parallel states, setting "ErrorEquals": ["States.ALL"] to handle any failure type. Route execution to the “Email” state through the “Next” property whenever an error is intercepted is incorrect. AWS X-Ray is primarily a tracing tool that helps visualize service call paths and diagnose performance issues. While useful for debugging, it does not provide built-in mechanisms for capturing workflow errors or sending alerts. X-Ray does not integrate with Step Functions Catch logic, so it cannot be used to route control flow or trigger email notifications. Simply enabling tracing does not fulfill the requirement for real-time failure alerts.
 
References:
https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html
https://docs.aws.amazon.com/step-functions/latest/dg/connect-sns.html 
 
Check out this AWS Step Functions Cheat Sheet:
https://tutorialsdojo.com/aws-step-functions/

---

## Question 32


**Category:** CSAP – Accelerate Workload Migration and Modernization

A fast-rising technology company is preparing to migrate a portfolio of applications to AWS. The current on-premises environment includes a mix of physical and virtual machines. The founding CTO, who originally designed the infrastructure, has left the company and provided limited documentation about the architecture.
The company lacks complete visibility into its application estate and infrastructure layout.
One critical application scheduled for migration has several unmapped dependencies. Many of these dependencies use low-latency communication over a custom IP-based protocol bound to port 1000. To preserve operational integrity, the company must migrate the application and all tightly coupled systems in the same migration wave.
The company has used AWS Transform discovery and assessment capabilities to collect telemetry from its servers for several months. The new CTO must now identify the complete set of connected systems that should be grouped and migrated together.
What approach should the new CTO take to discover and group the correct dependencies for simultaneous migration?

- A. Export the collected discovery data to Amazon S3. Use AWS Glue to crawl the exported dataset and create a data catalog. Then run Amazon Athena queries to search for references to port 1000 or IP-based traffic. Create a migration wave based only on the query results and proceed with the migration.
- B. Use AWS Transform MGN to replicate the application servers and migrate them immediately. After cutover, rely on Amazon CloudWatch metrics to identify dependency-related issues. Then scan for any missing dependencies and migrate those systems later as needed.
- **C. Use AWS Transform discovery and assessment capabilities to analyze the application servers and their communication patterns. Review the dependency mapping and network flow data, and use Amazon Athena data exploration to identify systems communicating through the custom protocol on port 1000. Group the application and all tightly coupled dependent servers into the same migration wave for coordinated migration.** ✅
- D. Use Amazon VPC Network Access Analyzer to define a network access scope that matches traffic on port 1000. Analyze the resulting network paths to determine which systems communicate with the application. Then create a migration wave in AWS Transform based on the Network Access Analyzer results.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		AWS Transform helps organizations plan and accelerate migration and modernization work by analyzing existing infrastructure, applications, and code. For migration planning, it can help assess workloads, review discovered server groupings, and organize applications into migration waves. A migration wave is made up of one or more move groups, and a move group represents co-dependent applications or systems that should be moved together because of technical or business dependencies. This is important for complex environments where applications depend on shared databases, internal services, or low-latency communication paths.
In this scenario, the company must not simply migrate the main application server by itself. The critical requirement is to identify all tightly coupled systems that communicate with the application over the custom IP-based protocol on port 1000. AWS Transform discovery and assessment capabilities help the new CTO understand application relationships and communication patterns before the migration begins. This allows the team to build a more accurate move group and migration wave instead of relying only on incomplete documentation or post-migration troubleshooting. AWS documentation also describes dependency relationships as connections between systems, which can include technical dependencies that require systems to be moved together.

Amazon Athena data exploration further strengthens the analysis because it allows collected discovery data from on-premises servers to be queried in one place. When data exploration is enabled, discovered data can be stored in Amazon S3 and queried with Athena, including utilization details and network connection data. This helps the team validate which servers are communicating with the application and which dependencies are related to port 1000 traffic. In this case, the best approach is to use AWS Transform for dependency mapping and migration wave planning, then use Athena data exploration to inspect the underlying connection data when a more specific protocol or port-based analysis is needed.
AWS Transform MGN is related to the migration phase, but it primarily focuses on rehosting servers to AWS. It replicates physical, virtual, or cloud-based source servers and helps launch them in AWS with minimal changes. That capability is useful after the migration plan is ready, but it does not replace the need to identify dependencies before cutover. In this question, the issue is not only how to move the servers. The main issue is how to determine which systems must be moved together to preserve low-latency communication and avoid breaking the application during migration.
Hence, the correct answer is: Use AWS Transform discovery and assessment capabilities to analyze the application servers and their communication patterns. Review the dependency mapping and network flow data, and use Amazon Athena data exploration to identify systems communicating through the custom protocol on port 1000. Group the application and all tightly coupled dependent servers into the same migration wave for coordinated migration.
The option that says: Export the collected discovery data to Amazon S3. Use AWS Glue to crawl the exported dataset and create a data catalog. Then run Amazon Athena queries to search for references to port 1000 or IP-based traffic. Create a migration wave based only on the query results and proceed with the migration is incorrect because it only focuses on manual data querying. Amazon Athena can help inspect collected discovery data, but this option skips the broader migration-planning capabilities of AWS Transform, such as dependency review, move group creation, and migration wave organization. A query that simply looks for port 1000 traffic could miss business dependencies, application relationships, shared services, or indirect communication patterns that should also influence the move group.
The option that says: Use Amazon VPC Network Access Analyzer to define a network access scope that matches traffic on port 1000. Analyze the resulting network paths to determine which systems communicate with the application. Then create a migration wave in AWS Transform based on the Network Access Analyzer results is incorrect. Amazon VPC Network Access Analyzer is typically used to analyze network access paths within AWS networking resources. It is not designed to discover dependency relationships across an on-premises estate of physical and virtual machines. In this scenario, the required traffic analysis must come from discovered server telemetry and connection data, not just from AWS VPC path analysis.
The option that says: Use AWS Transform MGN to replicate the application servers and migrate them immediately. After cutover, rely on Amazon CloudWatch metrics to identify dependency-related issues. Then scan for any missing dependencies and migrate those systems later as needed  is incorrect because it simply moves the workload first and discovers problems afterward. This is risky for a critical application with unmapped low-latency dependencies. CloudWatch is useful for monitoring resources after migration, but it is not a substitute for pre-migration dependency analysis. Migrating the primary application before identifying its tightly coupled systems could cause connection failures, degraded performance, or an incomplete cutover.
 
References:
https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-review-groupings-and-waves.html
https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html
https://docs.aws.amazon.com/application-discovery/latest/userguide/explore-data.html
 
Check out this Migration Evaluator Cheat Sheet:
https://tutorialsdojo.com/migration-evaluator-cheat-sheet/

---

## Question 33

**Category:** CSAP – Design for New Solutions

An investment firm collects daily stock trading data from exchanges and stores it in a data warehouse. The development team at the firm needs a solution that streams data directly into the data repository but should also allow SQL-based data modifications when needed. The solution should facilitate complex analytical queries that execute in the fastest possible time. The solution should also offer a business intelligence dashboard that highlights any stock price anomalies.

Which of the following options represents the best solution for the given use case?

- A. Configure Amazon Kinesis Data Streams to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source
- B. Configure Amazon Kinesis Data Streams to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source
- C. Configure Amazon Kinesis Data Firehose to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source
- **D. Configure Amazon Kinesis Data Firehose to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source** ✅

### Explanation

Correct option:

Configure Amazon Kinesis Data Firehose to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source

Amazon Kinesis Data Firehose is an extract, transform, and load (ETL) service that reliably captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards.

Kinesis Data Firehose Overview:

via - https://aws.amazon.com/kinesis/data-firehose/

Amazon Kinesis Data Streams is a massively scalable, highly durable data ingestion and processing service optimized for streaming data. Amazon Kinesis Data Streams is integrated with a number of AWS services, including Amazon Kinesis Data Firehose for near real-time transformation.

Key Concepts for Kinesis Data Streams:



via - https://aws.amazon.com/kinesis/data-streams/getting-started/

For the given use case, you can use Kinesis Data Firehose to stream data to Amazon Redshift. For a Redshift destination, streaming data is delivered to an S3 bucket first. Kinesis Data Firehose then issues an Amazon Redshift COPY command to load data from your S3 bucket to your Amazon Redshift cluster. If data transformation is enabled, you can optionally back up source data to another Amazon S3 bucket. Once the data is in Redshift, you can use Quicksight to create a business intelligence dashboard that has Redshift as the data source.


via - https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html

Incorrect options:

Configure Amazon Kinesis Data Streams to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source

You cannot stream data from Kinesis Data Streams directly to Redshift. You need to use Kinesis Data Firehose to deliver streaming data to Redshift. So this option is incorrect.

Configure Amazon Kinesis Data Firehose to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source

Configure Amazon Kinesis Data Streams to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source

Storing the data in S3 and then querying the data via Athena would not facilitate the execution of complex queries in the fastest possible time since Redshift has much better performance than Athena for complex analytical queries. So both these options are incorrect.

References:

https://aws.amazon.com/kinesis/data-firehose/

https://aws.amazon.com/kinesis/data-streams/getting-started/

https://aws.amazon.com/premiumsupport/knowledge-center/quicksight-redshift-private-connection/

---

## Question 34

**Category:** CSAP – Design for New Solutions

A company provides a web-based business-management platform for IT service companies across the globe to manage help desk, customer service, sales and marketing, and other critical business functions. More than 50,000 people use the company's platform, so the company must respond quickly to any reported problems. However, the company has issues with not having enough visibility into its systems to discover any issues. Multiple logs and monitoring systems are needed to understand the root cause of problems thereby taking hours to resolve. Even as the company is slowly moving towards serverless architecture using AWS Lambda/Amazon API Gateway/Amazon Elastic Container Service (Amazon ECS), the company wants to monitor the microservices and gain deeper insights into its serverless resources.

Which of the following will you recommend to address the given requirements?

- A. Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing
- **B. Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon CloudWatch for monitoring containers, latency, web server requests, and incoming load-balancer requests and create CloudWatch alarms to send out notifications if system latency is increasing** ✅
- C. Configure Amazon CloudWatch to monitor and analyze all microservices through request tracing. Enable CloudTrail to log all user activity
- D. Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing. Use AWS Config to continually assesses, audit, and evaluate the configurations and relationships of your resources and trigger alarms when needed

### Explanation

Correct option:

Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon CloudWatch for monitoring containers, latency, web server requests, and incoming load-balancer requests and create CloudWatch alarms to send out notifications if system latency is increasing

AWS X-Ray helps developers analyze and debug production, and distributed applications, such as those built using a microservices architecture.

Analyze and debug using X-Ray:

via - https://aws.amazon.com/xray/

AWS X-Ray creates a map of services used by your application with trace data that you can use to drill into specific services or issues. This provides a view of connections between services in your application and aggregated data for each service, including average latency and failure rates.

X-Ray service map:

via - https://aws.amazon.com/xray/features/

X-Ray Traces:

via - https://aws.amazon.com/xray/features/

Amazon CloudWatch allows you to collect infrastructure metrics from more than 70 AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon DynamoDB, Amazon Simple Storage Service (Amazon S3), Amazon ECS, AWS Lambda, Amazon API Gateway, with no action on your part. For example, Amazon EC2 instances automatically publish CPU utilization, data transfer, and disk usage metrics to help you understand state changes. You can use built-in metrics for API Gateway to detect latency or use built-in metrics for AWS Lambda to detect errors or throttles. Likewise, Amazon CloudWatch also allows you to collect application metrics (such as user activity, error metrics or memory used) from your applications to monitor operational performance, troubleshoot issues, and spot trends.

Amazon CloudWatch for monitoring:

via - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html

Incorrect options:

Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing

Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing. Use AWS Config to continually assesses, audit, and evaluate the configurations and relationships of your resources and trigger alarms when needed

Amazon EventBridge is a serverless event bus service that uses the Amazon CloudWatch Events API, but also includes more functionality, like the ability to ingest events from SaaS apps. EventBridge is designed to extend the event model beyond AWS, bringing data from software-as-a-service (SaaS) providers into your AWS environment. This means you can consume events from popular providers such as Zendesk, PagerDuty, and Auth0. You can use these in your applications with the same ease as any AWS-generated event.

For the given use case, you can use Cloudwatch for monitoring containers, latency, web server requests, and incoming load-balancer requests and create CloudWatch alarms to send out notifications if system latency is increasing. Therefore, both these options are incorrect.

Configure Amazon CloudWatch to monitor and analyze all microservices through request tracing. Enable CloudTrail to log all user activity - X-Ray can be used to monitor and analyze AWS microservices through request tracing, so this option is incorrect.

References:

https://aws.amazon.com/cloudwatch/features/

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html

https://aws.amazon.com/solutions/case-studies/connectwise/

---

## Question 35

**Category:** CSAP – Continuous Improvement for Existing Solutions

The engineering team at a retail company has deployed a fleet of EC2 instances under an Auto Scaling group (ASG). The instances under the ASG span two Availability Zones (AZ) within the eu-west-1 region. All the incoming requests are handled by an Application Load Balancer (ALB) that routes the requests to the EC2 instances under the ASG. A planned migration went wrong last week when two instances (belonging to AZ 1) were manually terminated and desired capacity was reduced causing the Availability Zones to become unbalanced. Later that day, another instance (belonging to AZ 2) was detected as unhealthy by the Application Load Balancer's health check.

Which of the following options represent the correct outcomes for the aforesaid events? (Select two)

- **A. Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance** ✅
- B. Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously
- C. As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched
- D. Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it
- **E. As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application** ✅

### Explanation

Correct options:

As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application

Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. You create collections of EC2 instances, called Auto Scaling groups. You can specify the minimum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below this size.

Actions such as changing the Availability Zones for your group or explicitly terminating or detaching instances and decrement the desired capacity at the same time, it can lead to the Auto Scaling group becoming unbalanced between Availability Zones. Amazon EC2 Auto Scaling compensates by rebalancing the Availability Zones.

When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application. Therefore, this option is correct.

Availability Zone Rebalancing Overview:

via - https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html

Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance

However, the scaling activity of Auto Scaling works in a different sequence compared to the rebalancing activity. Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance.

Incorrect options:

Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it - This option contradicts the correct sequence of events outlined earlier for scaling activity created by EC2 Auto Scaling. Actually, Auto Scaling first terminates the unhealthy instance and then launches a new instance. Hence this is incorrect.

As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched - This option contradicts the correct sequence of events outlined earlier for rebalancing activity. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones. Hence this is incorrect.

Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously - This is a made-up option as both the terminate and launch activities can't happen simultaneously. This option has been added as a distractor.

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/common-scenarios-termination.html#common-scenarios-termination-rebalancing

https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-unhealthy-instance.html

---

## Question 36

**Category:** CSAP – Design for New Solutions

A company has its web application hosted on Amazon EC2 instances that are deployed in a single AWS Region. The company has now expanded its operations into new geographies and the company wants to offer low-latency access for the application to its customers. To comply with different financial regulations of each geography, the application needs to operate in silos and the underlying instances in one region should not interact with instances running in other regions.

Which of the following represents the most optimal solution to automate the application deployment to different AWS regions?

- **A. Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation stack set from an administrator account to launch stack instances that deploy the application to various other regions** ✅
- B. Create a shell script that uses the AWS CLI to query the current state in one region and output an AWS CloudFormation template. Create a CloudFormation stack from the template by using the AWS CLI, specifying the --region parameter to deploy the application to other regions
- C. Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation change set from an administrator account to launch stack instances that deploy the application to various other regions
- D. Create a CloudFormation template describing the application infrastructure in the Resources section. Create a CloudFormation stack from the template by using the AWS CLI, specify multiple regions using the --regions parameter to deploy the application

### Explanation

Correct option:

Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation stack set from an administrator account to launch stack instances that deploy the application to various other regions


via - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html

Here are the relevant CloudFormation concepts:

Template: A CloudFormation template is a JSON or YAML formatted text file. You can save these files with any extension, such as .json, .yaml, .template, or .txt. CloudFormation uses these templates as blueprints for building your AWS resources.

Stack: When you use CloudFormation, you manage related resources as a single unit called a stack. You create, update, and delete a collection of resources by creating, updating, and deleting stacks. All the resources in a stack are defined by the stack's CloudFormation template.

Change set: If you need to make changes to the running resources in a stack, you update the stack. Before making changes to your resources, you can generate a change set, which is a summary of your proposed changes. Change sets allow you to see how your changes might impact your running resources, especially for critical resources, before implementing them.

Stack set: A stack set lets you create stacks in AWS accounts across regions by using a single CloudFormation template. All the resources included in each stack are defined by the stack set's CloudFormation template. As you create the stack set, you specify the template to use, in addition to any parameters and capabilities that the template requires.

After you've defined a stack set, you can create, update, or delete stacks in the target accounts and AWS Regions you specify. When you create, update, or delete stacks, you can also specify operation preferences, such as the order of Regions in which you want the operation to be performed, the failure tolerance beyond which stack operations stop, and the number of accounts in which operations are performed on stacks concurrently. A stack set is a regional resource. If you create a stack set in one AWS Region, you can't see it or change it in other Regions.


via - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html

For the given use case, you need to create a stack set that includes the CloudFormation template that you want to use to create stacks and then identify the AWS Regions in which you want to deploy stacks in your target accounts. A stack set ensures consistent deployment of the same stack resources, with the same settings, to all specified target accounts within the Regions you choose.

Incorrect options:

Create a CloudFormation template describing the application infrastructure in the Resources section. Create a CloudFormation stack from the template by using the AWS CLI, specify multiple regions using the --regions parameter to deploy the application - You can create a stack using the AWS Management Console or using AWS CloudFormation commands in the AWS CLI. The aws cloudformation create-stack command supports only a region parameter for a single region and not regions parameter for multiple regions.


via - https://aws.amazon.com/blogs/infrastructure-and-automation/multiple-account-multiple-region-aws-cloudformation/

Create a shell script that uses the AWS CLI to query the current state in one region and output an AWS CloudFormation template. Create a CloudFormation stack from the template by using the AWS CLI, specifying the --region parameter to deploy the application to other regions - Creating a script is not an elegant solution to provision same infrastructure in multiple AWS regions since this functionality is directly offered by AWS in the form of stack sets.

Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation change set from an administrator account to launch stack instances that deploy the application to various other regions - When you need to update a stack, understanding how your changes will affect running resources before you implement them can help you update stacks with confidence. Change sets allow you to preview how proposed changes to a stack might impact your running resources, for example, whether your changes will delete or replace any critical resources, AWS CloudFormation makes the changes to your stack only when you decide to execute the change set, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another change set. You cannot use change sets to deploy an application to multiple AWS regions.

References:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

---

## Question 37

**Category:** CSAP – Continuous Improvement for Existing Solutions

A company has its flagship application fronted by an Application Load Balancer that is targeting several EC2 Linux instances running in an Auto Scaling group in a private subnet. AWS Systems Manager Agent is installed on all the EC2 instances. The company recently released a new version of the application, however, some of the EC2 instances are now being marked as unhealthy and are being terminated, thereby causing the application to run at reduced capacity. You have been tasked to ascertain the root cause by analyzing Amazon CloudWatch logs that are collected from the application, but you find that the logs are inconclusive.

Which of the following options would you propose to get access to an EC2 instance to troubleshoot the issue?

- A. Suspend the Auto Scaling group's Launch process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause
- **B. Suspend the Auto Scaling group's Terminate process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause** ✅
- C. Enable EC2 instance termination protection. Use Session Manager to log In to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause
- D. Suspend the Auto Scaling group's HealthCheck process. Use EC2 instance connect to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause

### Explanation

Correct option:

Suspend the Auto Scaling group's Terminate process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause

The Terminate process removes instances from the Auto Scaling group when the group scales in, or when Amazon EC2 Auto Scaling chooses to terminate instances for other reasons, such as when an instance is terminated for exceeding its maximum lifetime duration or failing a health check. You need to suspend the Terminate process which will allow you to get access to the instance without it being terminated even if it is marked as unhealthy. You should note that another way to prevent Amazon EC2 Auto Scaling from terminating unhealthy instances, is to suspend the ReplaceUnhealthy process. You can then leverage the Session Manager to log in to the instance that is marked as unhealthy and analyze the system logs to figure out the root cause.


via - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination


via - https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination

Incorrect options:

Suspend the Auto Scaling group's HealthCheck process. Use EC2 instance connect to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause - The HealthCheck process checks the health of the instances and marks an instance as unhealthy if Amazon EC2 or Elastic Load Balancing tells Amazon EC2 Auto Scaling that the instance is unhealthy. This process can override the health status of an instance that you set manually. If you suspend the HealthCheck process, then none of the instances would be marked as unhealthy. Therefore, you cannot suspend the HealthCheck process for the given use case, since you must identify the root cause behind some of the instances being marked as unhealthy.

Suspend the Auto Scaling group's Launch process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause - The Launch process adds instances to the Auto Scaling group when the group scales out, or when Amazon EC2 Auto Scaling chooses to launch instances for other reasons, such as when it adds instances to a warm pool. Suspending the Launch process will not help in identifying the root cause behind some instances being marked as unhealthy as those instances would still be terminated.

Enable EC2 instance termination protection. Use Session Manager to log In to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause - Enabling EC2 instance termination (DisableApiTermination attribute) does not prevent Amazon EC2 Auto Scaling from terminating an instance.

References:

https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html

---

## Question 38

**Category:** CSAP – Continuous Improvement for Existing Solutions

A leading internet television network company uses AWS Cloud for analytics, recommendation engines and video transcoding. To monitor and optimize this network, the engineering team at the company has developed a solution for ingesting, augmenting, and analyzing the multiple terabytes of data its network generates daily in the form of virtual private cloud (VPC) flow logs. This would enable the company to identify performance-improvement opportunities such as identifying apps that are communicating across regions and collocating them. The VPC flow logs data is funneled into Kinesis Data Streams which further acts as the source of a delivery stream for Kinesis Firehose. The engineering team has now configured a Kinesis Agent to send the VPC flow logs data from another set of network devices to the same Firehose delivery stream. They noticed that data is not reaching Firehose as expected.

As a Solutions Architect Professional, which of the following options would you identify as the MOST plausible root cause behind this issue?

- A. Kinesis Firehose delivery stream has reached its limit and needs to be scaled manually
- B. The data sent by Kinesis Agent is lost because of a configuration error
- **C. Kinesis Agent cannot write to a Kinesis Firehose for which the delivery stream source is already set as Kinesis Data Streams** ✅
- D. Kinesis Agent can only write to Kinesis Data Streams, not to Kinesis Firehose

### Explanation

Correct option:

Kinesis Agent cannot write to a Kinesis Firehose for which the delivery stream source is already set as Kinesis Data Streams

Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

When a Kinesis data stream is configured as the source of a Firehose delivery stream, Firehose’s PutRecord and PutRecordBatch operations are disabled and Kinesis Agent cannot write to Firehose delivery stream directly. Data needs to be added to the Kinesis data stream through the Kinesis Data Streams PutRecord and PutRecords operations instead. Therefore, this option is correct.

Incorrect options:

Kinesis Agent can only write to Kinesis Data Streams, not to Kinesis Firehose - Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Kinesis Data Streams or Kinesis Firehose. So this option is incorrect.

Kinesis Firehose delivery stream has reached its limit and needs to be scaled manually - Kinesis Firehose is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. Therefore this option is not correct.

How Kinesis Firehose works:

via - https://aws.amazon.com/kinesis/data-firehose/

The data sent by Kinesis Agent is lost because of a configuration error - This is a made-up option and has been added as a distractor.

References:

https://aws.amazon.com/kinesis/data-firehose/

https://aws.amazon.com/kinesis/data-firehose/faqs/

---

## Question 39


**Category:** CSAP – Design Solutions for Organizational Complexity

An edtech company is preparing to launch a new virtual learning environment (VLE) hosted on Amazon EC2 instances. To support students and educators around the globe, the platform must be deployed across three AWS Regions: us-east-1, eu-west-1, and ap-southeast-1. Key components of the system, such as student progress tracking, resource availability, and real-time collaboration events, must remain consistent and synchronized across all Regions.
To support real-time interactivity, the VLE uses more than just standard HTTP and HTTPS ports. WebSocket connections run on port 5000 for live quizzes, and the interactive whiteboard feature communicates over port 8080. To ensure optimal user experience, the platform must direct learners to the AWS Region with the lowest latency. Additionally, the architecture must be designed so that any single Region can dynamically scale to accommodate traffic from all others, should the need arise.
A solutions architect must define an infrastructure strategy that delivers global availability, seamless scalability, and low-latency access, all while keeping operational overhead to a minimum.
What solution best satisfies these needs while reducing operational management effort?

- A. Deploy EC2 instances within Auto Scaling groups across all AWS Regions, linking each group to its corresponding Application Load Balancer (ALB). Configure Amazon Route 53 to use latency-based routing policies, directing users to the Region with the fastest response time via the associated ALB. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions.
- B. Deploy EC2 Auto Scaling groups across all AWS Regions and link each group to its own Network Load Balancer (NLB). Enable EC2 Global View to centrally monitor and manage instance health, capacity, and scaling activity across Regions. Use Amazon Route 53 with latency-based routing to ensure users are directed to the Region delivering the lowest latency. Store platform metadata in Amazon RDS for PostgreSQL, deploying one instance per Region, and configure cross-Region read replicas to maintain synchronized data consistency on a global scale.
- **C. Provision of an EC2 Auto Scaling group in every AWS Region to manage computing resources dynamically. Associate each group with its respective Network Load Balancer (NLB). Configure Amazon Route 53 with latency-based routing policies that direct traffic to the NLB offering the fastest response times per Region. Store platform metadata within an Amazon DynamoDB global table to maintain data consistency across all Regions.** ✅
- D. Launch an EC2 Spot Fleet in every AWS Region and link each to its respective Network Load Balancer (NLB). Provision an AWS Global Accelerator IP address that targets the NLB to enable consistent global access. Configure Amazon Route 53 to apply latency-based routing, directing traffic to the Region with the fastest response time using the AWS Global Accelerator IP address. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		An Auto Scaling group is a logical set of EC2 instances managed by Amazon EC2 Auto Scaling, which automatically maintains instance count and handles health checks and scaling based on demand.
Application Load Balancers (ALBs) operate at the application layer, ideal for web apps and microservices with features like SSL termination and session stickiness. Network Load Balancers (NLBs) work at the transport layer, offering low latency and high throughput for performance-intensive workloads like gaming and IoT.
Amazon Route 53 with latency-based routing directs users to the Region with the lowest latency.
Amazon DynamoDB global tables provide multi-Region replication with strong or eventual consistency. Strong consistency ensures that applications can always read the latest data from any Region, enabling high availability and zero RPO.

EC2 Auto Scaling groups manage compute capacity across Regions, with each group linked to a Network Load Balancer, ideal for TCP traffic on non-standard ports like 5000 and 8080 used by the VLE. Amazon Route 53 with latency-based routing directs users to the Region with the lowest latency. DynamoDB global tables offer multi-Region, multi-active replication, enabling all Regions to read and write simultaneously. This setup ensures real-time consistency without complex replication logic or added operational overhead.
Hence, the correct answer is: Provision of an EC2 Auto Scaling group in every AWS Region to manage computing resources dynamically. Associate each group with its respective Network Load Balancer (NLB). Configure Amazon Route 53 with latency-based routing policies that direct traffic to the NLB offering the fastest response times per Region. Store platform metadata within an Amazon DynamoDB global table to maintain data consistency across all Regions.
The option that says: Deploy EC2 instances within Auto Scaling groups across all AWS Regions, linking each group to its corresponding Application Load Balancer (ALB). Configure Amazon Route 53 to use latency-based routing policies, directing users to the Region with the fastest response time via the associated ALB. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions is incorrect. This solution uses Application Load Balancers, which support only HTTP and HTTPS. Since the VLE uses WebSockets on port 5000 and custom traffic on port 8080, ALBs are incompatible without additional configuration. Despite the rest of the architecture aligning with requirements, using ALBs makes the solution technically unsuitable. One cannot simply replace an NLB with an ALB when the traffic types do not align.
The option that says: Launch an EC2 Spot Fleet in every AWS Region and link each to its respective Network Load Balancer (NLB). Provision an AWS Global Accelerator IP address that targets the NLB to enable consistent global access. Configure Amazon Route 53 to apply latency-based routing, directing traffic to the Region with the fastest response time using the AWS Global Accelerator IP address. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions is incorrect. This option adds unnecessary complexity by introducing EC2 Spot Fleets and AWS Global Accelerator. While Spot Fleets reduce cost, they can be interrupted without notice, making them unreliable for a real-time education platform. Global Accelerator provides advanced routing, but is redundant when Amazon Route 53’s latency-based routing already meets latency needs. These features add operational overhead without meaningful benefits for the platform’s reliability and availability.
The option that says:  Deploy EC2 Auto Scaling groups across all AWS Regions and link each group to its own Network Load Balancer (NLB). Enable EC2 Global View to centrally monitor and manage instance health, capacity, and scaling activity across Regions. Use Amazon Route 53 with latency-based routing to ensure users are directed to the Region delivering the lowest latency. Store platform metadata in Amazon RDS for PostgreSQL, deploying one instance per Region, and configure cross-Region read replicas to maintain synchronized data consistency on a global scale is incorrect. This option uses EC2 Global View and Amazon RDS for PostgreSQL with cross-Region replication. While EC2 Global View offers centralized monitoring across Regions, it does not handle traffic distribution or scaling. The main limitation is that RDS for PostgreSQL only supports cross-Region read replicas and does not offer multi-Region write capability out of the box. Supporting global writes would require extra tooling and coordination, increasing operational overhead.
 
References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html
https://aws.amazon.com/what-is/load-balancing/
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html
https://aws.amazon.com/dynamodb/global-tables/
 
Check out this AWS Elastic Load Balancing Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

---

## Question 40

**Category:** CSAP – Continuous Improvement for Existing Solutions

A company has built its serverless solution using Amazon API Gateway REST API and AWS Lambda across multiple AWS Regions configured into a single AWS account. During peak hours, customers began to receive 429 Too Many Requests errors from multiple API methods. While troubleshooting the issue, the team realized that AWS Lambda function(s) have not been invoked for these API methods. Also, the company wants to provide a separate quota for its premium customers to access the APIs.

Which solution will you offer to meet this requirement?

- A. The error is the outcome of the company reaching its API Gateway account limit for calls per second, set Lambda-level throttling targets in the API Gateway usage plan, and configure customers to use a particular API method when the client identifier is set
- B. The error is the outcome of the company reaching its API Gateway account per-method limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers
- **C. The error is the outcome of the company reaching its API Gateway account limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers** ✅
- D. The error is the outcome of the company reaching its API Gateway limits for the steady-state requests per second (RPS) across all APIs within an AWS account per Region. These limits can be overwritten by configuring the AWS Regional throttling parameters to a greater value. However, based on the AWS account type, a limit is set to the overwritten throttling values

### Explanation

Correct options:

The error is the outcome of the company reaching its API Gateway account limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers

After you create, test, and deploy your APIs, you can use API Gateway usage plans to make them available as product offerings for your customers. You can configure usage plans and API keys to allow customers to access selected APIs, and begin throttling requests to those APIs based on defined limits and quotas. These can be set at the API, or API method level.

Per-client throttling limits are applied to clients that use API keys associated with your usage plan as a client identifier. Note that these limits can't be higher than the per-account limits.

When request submissions exceed the steady-state request rate and burst limits, API Gateway begins to throttle requests. Clients may receive 429 Too Many Requests error responses at this point. Since the error is at API Gateway, the Lambda functions configured are not invoked at all.

How throttling limit settings are applied in API Gateway:

via - https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

Incorrect options:

"The error is the outcome of the company reaching its API Gateway account per-method limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers - You should note that a throttling limit sets the target point at which request throttling should start. This can be set at the API or API method level. The use case states that the 429 Too Many Requests errors were received from multiple API methods, so the API Gateway reached its limit at the API level since none of the methods invoked the downstream Lambda function. So this option is incorrect.

The error is the outcome of the company reaching its API Gateway account limit for calls per second, set Lambda-level throttling targets in the API Gateway usage plan, and configure customers to use a particular API method when the client identifier is set - This is incorrect. You cannot define Lambda-level throttling targets in the API Gateway usage plan.

The error is the outcome of the company reaching its API Gateway limits for the steady-state requests per second (RPS) across all APIs within an AWS account per Region. These limits can be overwritten by configuring the AWS Regional throttling parameters to a greater value. However, based on the AWS account type, a limit is set to the overwritten throttling values - Per-account limits are applied to all APIs in an account in a specified Region. The account-level rate limit can be increased upon request - higher limits are possible with APIs that have shorter timeouts and smaller payloads. To request an increase in account-level throttling limits per Region, contact the AWS Support Center. It cannot be done from the AWS account directly.

References:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

---

## Question 41

**Category:** CSAP – Design for New Solutions

A multi-national bank has recently migrated to AWS Cloud to utilize dedicated instances that are physically isolated at the host hardware level from instances that belong to other AWS accounts. The bank's flagship application is hosted on a fleet of EC2 instances which are part of an Auto Scaling group (ASG). The ASG uses a Launch Configuration (LC-A) with "dedicated" instance placement tenancy but the VPC (VPC-A) used by the Launch Configuration LC-A has the instance tenancy set to default. Later the engineering team creates a new Launch Configuration (LC-B) with "default" instance placement tenancy but the VPC (VPC-B) used by the Launch Configuration LC-B has the instance tenancy set to dedicated.

As a Solutions Architect Professional, which of the following options would you identify as correct regarding the instances launched via Launch Configuration LC-A and Launch Configuration LC-B?

- A. The instances launched by Launch Configuration LC-A will have dedicated instance tenancy while the instances launched by the Launch Configuration LC-B will have default instance tenancy
- B. The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have default instance tenancy
- **C. The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have dedicated instance tenancy** ✅
- D. The instances launched by Launch Configuration LC-A will have default instance tenancy while the instances launched by the Launch Configuration LC-B will have dedicated instance tenancy

### Explanation

Correct option:

The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have dedicated instance tenancy

A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances. When you create a launch configuration, you specify information for the instances. Include the ID of the Amazon Machine Image (AMI), the instance type, a key pair, one or more security groups, and a block device mapping. If you've launched an EC2 instance before, you specified the same information to launch the instance.

When you create a launch configuration, the default value for the instance placement tenancy is null and the instance tenancy is controlled by the tenancy attribute of the VPC.  If you set the Launch Configuration Tenancy to default and the VPC Tenancy is set to dedicated, then the instances have dedicated tenancy. If you set the Launch Configuration Tenancy to dedicated and the VPC Tenancy is set to default, then again the instances have dedicated tenancy.

Launch Configuration Tenancy vs VPC Tenancy

via - https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy

Incorrect options:

The instances launched by Launch Configuration LC-A will have dedicated instance tenancy while the instances launched by the Launch Configuration LC-B will have default instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

The instances launched by Launch Configuration LC-A will have default instance tenancy while the instances launched by the Launch Configuration LC-B will have dedicated instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have default instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy

---

## Question 42

**Category:** CSAP – Continuous Improvement for Existing Solutions

A retail company is deploying a critical application on multiple EC2 instances in a VPC. Per the company policy, any failed client connections to the EC2 instances must be logged.

Which of the following options would you recommend as the MOST cost-effective solution to address these requirements?

- A. Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to a Kinesis Data Firehose stream with the data delivery to an S3 bucket
- B. Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to Kinesis Data Streams with the data delivery to an S3 bucket
- **C. Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to CloudWatch Logs** ✅
- D. Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to Amazon CloudWatch Logs

### Explanation

Correct option:

Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to CloudWatch Logs

VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. After you've created a flow log, you can retrieve and view its data in the chosen destination.

You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.

Flow logs can help you with a number of tasks, such as:

Diagnosing overly restrictive security group rules

Monitoring the traffic that is reaching your instance

Determining the direction of the traffic to and from the network interfaces


via - https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

For the given use case, you can configure the VPC Flow Logs only for the elastic network interfaces associated with the instances and set the type of traffic to be captured as rejected traffic only. Lastly, you can publish the Flow Logs to Amazon CloudWatch Logs.

Incorrect options:

Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to Kinesis Data Streams with the data delivery to an S3 bucket - Flow Logs data can only be published to Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose. Kinesis Data Firehose is a streaming ETL solution. It is the easiest way to load streaming data into data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk. You cannot publish Flow Logs to Kinesis Data Streams, so this option is incorrect.

Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to Amazon CloudWatch Logs

Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to a Kinesis Data Firehose stream with the data delivery to an S3 bucket

Dedicated tenancy ensures all EC2 instances that are launched in a VPC run on hardware that's dedicated to a single customer. Dedicated Instances are Amazon EC2 instances that run in a VPC on hardware that's dedicated to a single customer. Your Dedicated instances are physically isolated at the host hardware level from instances that belong to other AWS accounts. Dedicated instances may share hardware with other instances from the same AWS account that are not Dedicated instances. You can also use Dedicated Hosts to launch Amazon EC2 instances on physical servers that are dedicated for your use. Dedicated Hosts give you additional visibility and control over how instances are placed on a physical server, and you can reliably use the same physical server over time.

Dedicated Instance pricing has two components: (1) an hourly per instance usage fee and (2) a dedicated per region fee (note that you pay this once per hour regardless of how many Dedicated Instances you're running). Therefore dedicated VPC turns out to be a costlier solution. So both these options are incorrect for the given use case.

References:

https://aws.amazon.com/about-aws/whats-new/2017/10/switch-the-tenancy-of-your-vpc-from-dedicated-to-default-instantly/

https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

---

## Question 43

**Category:** CSAP – Continuous Improvement for Existing Solutions

The DevOps team for a CRM SaaS company wants to implement a patching plan on AWS Cloud for a large mixed fleet of Windows and Linux servers. The patching plan has to be auditable and must be implemented securely to ensure compliance with the company's business requirements.

As a Solutions Architect Professional, which of the following options would you recommend to address these requirements with MINIMAL effort? (Select two)

- **A. Apply patch baselines using the AWS-RunPatchBaseline SSM document** ✅
- B. Apply patch baselines using the AWS-ApplyPatchBaseline SSM document
- C. Set up an OS-native patching service to manage the update frequency and release approval for all instances. Set up AWS Config to provide audit and compliance reporting
- **D. Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval** ✅
- E. Configure OpsWorks automatic patching support for all applications which will keep the OS up-to-date following the initial installation. Set up AWS Config to provide audit and compliance reporting

### Explanation

Correct options:

Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval

Apply patch baselines using the AWS-RunPatchBaseline SSM document

Systems Manager is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects. AWS Systems Manager Agent (SSM Agent) is Amazon software that can be installed and configured on an EC2 instance, an on-premises server, or a virtual machine (VM). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources.


via - https://aws.amazon.com/systems-manager/

You can use Patch Manager to apply patches for both operating systems and applications. (On Windows Server, application support is limited to updates for Microsoft applications). Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches individually or to large groups of instances by using Amazon EC2 tags.

For the given use-case, you can install patches on a regular basis by scheduling patching to run as a Systems Manager maintenance window task.

Systems Manager supports an SSM document for Patch Manager, AWS-RunPatchBaseline, which performs patching operations on instances for both security-related and other types of updates. When the document is run, it uses the patch baseline currently specified as the "default" for an operating system type.

The AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only and doesn't support Linux instances. For applying patch baselines to both Windows Server and Linux instances, the recommended SSM document is AWS-RunPatchBaseline.


via - https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html


via - https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-differences.html

Incorrect options:

Configure OpsWorks automatic patching support for all applications which will keep the OS up-to-date following the initial installation. Set up AWS Config to provide audit and compliance reporting - AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments. You cannot use OpsWorks for automatic patch management, so this option is incorrect.

The part about using AWS Config is a distraction. AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - “What did my AWS resource look like at xyz point in time?”.

Set up an OS-native patching service to manage the update frequency and release approval for all instances. Set up AWS Config to provide audit and compliance reporting - You could use an OS-native patching service to manage the update frequency and release approval for all instances but it would take considerable effort to set up and configure this solution. This violates the minimal effort requirement of the given use-case.

Apply patch baselines using the AWS-ApplyPatchBaseline SSM document - As mentioned in the explanation above, the AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only and doesn't support Linux instances. For applying patch baselines to both Windows Server and Linux instances, the recommended SSM document is AWS-RunPatchBaseline.

References:

https://aws.amazon.com/systems-manager/

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-differences.html

---

## Question 44

**Category:** CSAP – Design for New Solutions

A solutions architect at a retail company has set up a workflow to ingest the clickstream data into the raw zone of the S3 data lake. The architect wants to run some SQL-based data sanity checks on the raw zone of the data lake.

What AWS services would you suggest for this requirement such that the solution is cost-effective and easy to maintain?

- **A. Use Athena to run SQL based analytics against S3 data** ✅
- B. Load the incremental raw zone data into Redshift on an hourly basis and run the SQL based sanity checks
- C. Load the incremental raw zone data into RDS on an hourly basis and run the SQL based sanity checks
- D. Load the incremental raw zone data into an EMR based Spark Cluster on an hourly basis and use SparkSQL to run the SQL based sanity checks

### Explanation

Correct option:

Use Athena to run SQL based analytics against S3 data

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to set up or manage, and customers pay only for the queries they run. You can use Athena to process logs, perform ad-hoc analysis, and run interactive queries.

AWS Athena Benefits:

via - https://aws.amazon.com/athena/

Incorrect options:

Load the incremental raw zone data into Redshift on an hourly basis and run the SQL-based sanity checks - Amazon Redshift is a fully-managed petabyte-scale cloud-based data warehouse product designed for large-scale data set storage and analysis. As the development team would have to maintain and monitor the Redshift cluster size and would require significant development time to set up the processes to consume the data periodically, so this option is ruled out.

Load the incremental raw zone data into an EMR based Spark Cluster on an hourly basis and use SparkSQL to run the SQL based sanity checks - Amazon EMR is the industry-leading cloud big data platform for processing vast amounts of data using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto. Amazon EMR uses Hadoop, an open-source framework, to distribute your data and processing across a resizable cluster of Amazon EC2 instances. Using an EMR cluster would imply managing the underlying infrastructure so it’s ruled out because the correct solution for the given use case should require the least amount of development effort and ongoing maintenance.

Load the incremental raw zone data into RDS on an hourly basis and run the SQL-based sanity checks - Loading the incremental data into RDS implies data migration jobs will have to be written via a Lambda function or an EC2 based process. This goes against the requirement that the solution should involve the least amount of development effort and ongoing maintenance. Hence this option is not correct.

Reference:

https://aws.amazon.com/athena/

---

## Question 45


**Category:** CSAP – Design for New Solutions

An accounting company initiated a migration of its core workloads to the AWS Cloud to modernize its infrastructure, following a recent change in technical leadership. The company’s current setup includes Graviton‑based Amazon EC2 instances (ARM64 architecture) for compute resources, Amazon EFS for shared file storage, and Amazon RDS DB instances for managing relational databases.




To comply with regulatory mandates and uphold internal data governance standards, the new leadership has mandated the following backup procedures:


The solution must provide a centralized overview of backup status across the AWS environment.


Any backup failure must trigger immediate notifications to technical stakeholders.


Data backups must follow custom retention policies, with separate rules for daily, weekly, and monthly backups.


Backups must be automatically replicated to at least one additional AWS Region immediately after creation.


Which actions will meet these objectives while introducing the least operational overhead?

- A. Define individual snapshot lifecycle policies in Amazon Data Lifecycle Manager (Amazon DLM) to align with each retention requirement. Activate cross-Region snapshot replication within DLM to ensure backups are automatically copied to another AWS Region. Develop an AWS Lambda function that monitors for backup or restore events and triggers a notification when a job finishes with either RESTORE_JOB_SUCCESSFUL or BACKUP_JOB_FAILED status.
- B. Define an AWS Backup plan that includes individual backup rules aligned with each required retention schedule. Develop an AWS Lambda function to handle cross-Region backup replication and to dispatch notifications whenever a backup job results in BACKUP_JOB_FAILED or  RESTORE_JOB_SUCCESSFUL.
- **C. Establish an AWS Backup strategy incorporating individual backup rules corresponding to every retention specification. Set up a Backup strategy for cross-Region backup replication. Integrate an Amazon Simple Notification Service (Amazon SNS) topic into the backup strategy to dispatch alerts for completed operations, excluding those with the BACKUP_JOB_COMPLETED status.** ✅
- D. Develop and deploy a consolidated Python script on a single EC2 instance. Schedule the script to connect to each RDS DB instance, run pg_dump/mysqldump. Call the create_image() API to generate AMIs for selected instances. Mount the EFS file system to the EC2 instance and use rsync to copy data. Replicate the backup files to another Region using Amazon S3. Send emails using Amazon SES if anything fails.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		AWS Backup is a fully managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on-premises. Using this service, you can configure backup policies and monitor activity for your AWS resources in one place. It allows you to automate and consolidate backup tasks previously performed service-by-service, and removes the need to create custom scripts and manual processes. You can automate your data protection policies and schedules with a few clicks in the AWS Backup console.
AWS Backup provides many features and capabilities, including lifecycle management policies, cross-Region backup, and backup activity monitoring.

AWS Backup is purpose-built to manage backup operations across EC2, EFS, and RDS with centralized visibility. It allows you to define individual backup rules for each retention period, supports native cross-Region replication, and integrates directly with Amazon SNS to send alerts for specific backup job statuses. The requirement also states the necessity to trigger immediate notifications on failure. Since AWS Backup includes multiple possible failure statuses and transitional statuses, the configuration simply sends notifications for all job completions except the successful BACKUP_JOB_COMPLETED status, ensuring nothing slips through the cracks. This approach meets all the stated requirements without introducing custom scripting or external monitoring, and it introduces the least operational overhead by using built-in managed features.
Hence, the correct answer is: Establish an AWS Backup strategy incorporating individual backup rules corresponding to every retention specification. Set up a Backup strategy for cross-Region backup replication. Integrate an Amazon Simple Notification Service (Amazon SNS) topic into the backup strategy to dispatch alerts for completed operations, excluding those with the BACKUP_JOB_COMPLETED status.
The option that says: Develop and deploy a consolidated Python script on a single EC2 instance. Schedule the script to connect to each RDS DB instance, run pg_dump/mysqldump. Call the create_image() API to generate AMIs for selected instances. Mount the EFS file system to the EC2 instance and use rsync to copy data. Replicate the backup files to another Region using Amazon S3. Send emails using Amazon SES if anything fails is incorrect. It relies on a custom EC2-based script to manage backups, which requires ongoing maintenance and complex logic to handle failures, retention, and replication. It just does not provide centralized visibility or native integration with AWS services for status tracking and alerting. This method adds operational complexity instead of reducing it and primarily duplicates features that AWS Backup already offers.
The option that says: Define individual snapshot lifecycle policies in Amazon Data Lifecycle Manager (Amazon DLM) to align with each retention requirement. Activate cross-Region snapshot replication within DLM to ensure backups are automatically copied to another AWS Region. Develop an AWS Lambda function that monitors for backup or restore events and triggers a notification when a job finishes with either RESTORE_JOB_SUCCESSFUL or BACKUP_JOB_FAILED status is incorrect. Amazon DLM is primarily designed for EBS volume snapshots and does not support RDS or EFS. While it can automate retention and replication for EC2 volumes, it simply does not offer centralized backup visibility across all services or native notification mechanisms. Relying on Lambda for alerts adds overhead and does not replace the native features that AWS Backup provides.
The option that says:  Define an AWS Backup plan that includes individual backup rules aligned with each required retention schedule. Develop an AWS Lambda function to handle cross-Region backup replication and to dispatch notifications whenever a backup job results in BACKUP_JOB_FAILED or RESTORE_JOB_SUCCESSFUL is incorrect. This solution offloads replication and notifications to custom Lambda functions, even though AWS Backup already supports built-in replication and alert integration through SNS. This approach just adds unnecessary components, making the architecture more complex and challenging to manage. It primarily ignores the full capabilities of AWS Backup and increases operational burden without any real benefit.
 
References:
https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html
https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html
 
Check out this AWS Backup Cheat Sheet:
https://tutorialsdojo.com/aws-backup/

---

## Question 46

**Category:** CSAP – Continuous Improvement for Existing Solutions

A healthcare company has to maintain a log of all transactions for audit and compliance purposes. The company is planning stringent security measures for all of its CloudTrail log files.

Which of the following would you suggest as the LEAST effort options to secure the CloudTrail logs? (Select two)

- A. Integrate with Amazon CloudWatch alarms to generate an alarm whenever changes are made to CloudTrail log files
- B. To prevent access rights violation, use AWS root user account to manage CloudTrail logs
- **C. Use Amazon S3 MFA Delete on the S3 bucket that holds CloudTrail logs and digest files** ✅
- **D. Enable CloudTrail log file integrity validation** ✅
- E. Enable Amazon S3 encryption using AWS KMS keys on the S3 bucket that stores CloudTrail logs to prevent unauthorized modification of the log files

### Explanation

Correct options:

Enable CloudTrail log file integrity validation - Validated log files are invaluable in security and forensic investigations. For example, a validated log file enables you to assert positively that the log file itself has not changed, or that particular user credentials performed specific API activity. The CloudTrail log file integrity validation process also lets you know if a log file has been deleted or changed, or assert positively that no log files were delivered to your account during a given time.

When you enable log file integrity validation, CloudTrail creates a hash for every log file that it delivers. Every hour, CloudTrail also creates and delivers a file that references the log files for the last hour and contains a hash of each. This file is called a digest file. CloudTrail signs each digest file using the private key of a public and private key pair. After delivery, you can use the public key to validate the digest file. CloudTrail uses different key pairs for each AWS region.

Use Amazon S3 MFA Delete on the S3 bucket that holds CloudTrail logs and digest files - The digest files are delivered to the same Amazon S3 bucket associated with your trail as your CloudTrail log files. If your log files are delivered from all regions or from multiple accounts into a single Amazon S3 bucket, CloudTrail will deliver the digest files from those regions and accounts into the same bucket.

Configuring multi-factor authentication (MFA) ensures that any attempt to change the versioning state of your bucket or permanently delete an object version requires additional authentication. This helps prevent any operation that could compromise the integrity of your log files, even if a user acquires the password of an IAM user that has permission to permanently delete Amazon S3 objects.

Incorrect options:

Enable Amazon S3 encryption using AWS KMS keys on the S3 bucket that stores CloudTrail logs to prevent unauthorized modification of the log files - This option sounds correct because encryption is commonly associated with stronger security controls. However, S3 default encryption with AWS KMS only protects the confidentiality of data at rest, not its integrity or deletion. Even when logs are encrypted, any IAM principal with sufficient permissions can still delete objects, overwrite them, or change access policies.

Integrate with Amazon CloudWatch alarms to generate an alarm whenever changes are made to CloudTrail log files - CloudTrail and CloudWatch are closely integrated and it is possible to implement something like this. However, this requires additional effort compared to the correct options.

To prevent access rights violation, use AWS root user account to manage CloudTrail logs - Root user account should not be used for any operational use cases as a security best practice, so this option is incorrect.

References:

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html

---

## Question 47

**Category:** CSAP – Design for New Solutions

A leading hotel reviews website has a repository of more than one million high-quality digital images. When this massive volume of images became too cumbersome to handle in-house, the company decided to offload the content to a central repository on Amazon S3 as part of its hybrid cloud strategy. The company now wants to reprocess its entire collection of photographic images to change the watermarks. The company wants to use Amazon EC2 instances and Amazon SQS in an integrated workflow to generate the sizes they need for each photo. The team wants to process a few thousand photos each night, using Amazon EC2 Spot Instances. The team uses Amazon SQS to communicate the photos that need to be processed and the status of the jobs. To handle certain sensitive photos, the team wants to postpone the delivery of certain messages to the queue by one minute while all other messages need to be delivered immediately to the queue.

As a Solutions Architect Professional, which of the following solutions would you suggest to the company to handle the workflow for sensitive photos?

- A. Use visibility timeout to postpone the delivery of certain messages to the queue by one minute
- **B. Use message timers to postpone the delivery of certain messages to the queue by one minute** ✅
- C. Use delay queues to postpone the delivery of certain messages to the queue by one minute
- D. Use dead-letter queues to postpone the delivery of certain messages to the queue by one minute

### Explanation

Correct option:

Use message timers to postpone the delivery of certain messages to the queue by one minute

You can use message timers to set an initial invisibility period for a message added to a queue. So, if you send a message with a 60-second timer, the message isn't visible to consumers for its first 60 seconds in the queue. The default (minimum) delay for a message is 0 seconds. The maximum is 15 minutes. Therefore, you should use message timers to postpone the delivery of certain messages to the queue by one minute.

Incorrect options:

Use dead-letter queues to postpone the delivery of certain messages to the queue by one minute - Dead-letter queues can be used by other queues (source queues) as a target for messages that can't be processed (consumed) successfully. Dead-letter queues are useful for debugging your application or messaging system because they let you isolate problematic messages to determine why their processing doesn't succeed. You cannot use dead-letter queues to postpone the delivery of certain messages to the queue by one minute.

Use visibility timeout to postpone the delivery of certain messages to the queue by one minute - Visibility timeout is a period during which Amazon SQS prevents other consumers from receiving and processing a given message. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours. You cannot use visibility timeout to postpone the delivery of certain messages to the queue by one minute.

Use delay queues to postpone the delivery of certain messages to the queue by one minute - Delay queues let you postpone the delivery of all new messages to a queue for several seconds, for example, when your consumer application needs additional time to process messages. If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period. The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes. You cannot use delay queues to postpone the delivery of only certain messages to the queue by one minute.


via - https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html

References:

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html

---

## Question 48

**Category:** CSAP – Accelerate Workload Migration and Modernization

A social media company is transitioning its IT infrastructure from its on-premises data center to the AWS Cloud. The company wants to move its data artifacts, 200 TB in total size, to Amazon S3 on the AWS Cloud in the shortest possible time. The company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for this data migration. In terms of the networking infrastructure, the company has a 500 Mbps Direct Connect connection to the AWS Cloud as well as an IPSec based AWS VPN connection using the public internet that supports a bandwidth of 1 Gbps.

Which of the following solutions would you recommend to address the given use-case?

- A. Leverage the 500 Mbps Direct Connect connection to transfer the data to S3 over the dedicated connection
- B. Leverage the 1Gbps IPSec based AWS VPN connection to transfer the data to S3 over the public internet
- **C. Order three AWS Snowball Edge appliances, split and transfer the data to these three appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3** ✅
- D. Leverage S3 Transfer Acceleration to transfer the data to S3

### Explanation

Correct option:

Order three AWS Snowball Edge appliances, split and transfer the data to these three appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3

The AWS Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities. Each Snowball Edge device can transport data at speeds faster than the internet. This transport is done by shipping the data in the appliances through a Regional carrier. The appliances are rugged shipping containers, complete with E Ink shipping labels. Snowball Edge devices have three options for device configurations – storage optimized, compute optimized, and with GPU.

Snowball Edge is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. The AWS Snow Family is ideal for customers moving large batches of data at once. The AWS Snowball has a typical 5-7 days turnaround time. As each Snowball Edge device can handle 80TB of data, you can order 3 such devices to take care of the data transfer for the given use-case.

Incorrect options:

Leverage the 1Gbps IPSec based AWS VPN connection to transfer the data to S3 over the public internet

The given use-case requires transferring 200 TB of archived data within the shortest possible duration. Now, the IPSec based AWS VPN connection assures a speed of 1 Gbps (Gigabits per second). As 1 Byte = 8 bits, therefore you can transfer 0.125 GBps (Gigabytes per second).

So the hourly data transfer is 0.1256060 = 450 GB or approximately 0.45 TB.

So the approximate daily data transfer is 0.45 * 24 = ~ 10 TB

Therefore, the entire archived dataset of 200 TB can be transferred in 20 days. As explained above, using Snowball appliances, you can complete this data transfer in just 5-7 days. So this option is incorrect.

Leverage the 500 Mbps Direct Connect connection to transfer the data to S3 over the dedicated connection - We established above that a 1GBps connection would take 20 days to transfer the dataset, so the 500 Mbps Direct Connect connection would take 40 days to transfer the dataset. So this option is incorrect.

Exam Alert:

The exam would probe you on multiple scenarios around competing options to migrate data from on-premises data centers to AWS Cloud. You should remember that a 1Gbps connection at full utilization can transfer approximately 10 TB of data in a day. You will see questions that tweak the available connection bandwidth or change the available utilization, so you just need to factor these changes into the above-mentioned unit rate to identify the correct answer.

Leverage S3 Transfer Acceleration to transfer the data to S3 - S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and your Amazon S3 bucket. S3 Transfer Acceleration leverages Amazon CloudFront’s globally distributed AWS Edge Locations.

You should note that S3 Transfer Acceleration over a fully-utilized 1 Gbps line can only transfer up to 75 TBs in a week's duration. So this option is not correct for the given use-case.


via - https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration

References:

https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration

---

## Question 49

**Category:** CSAP – Design for New Solutions

A company is building an on-demand streaming application on AWS Cloud. The company has chosen Amazon S3 as its storage service and moved the existing videos to an Amazon S3 bucket. The application requires the video playback to start quickly, fast-forwarding should be more efficient and the overall user experience should be smoother without smothering the user's bandwidth.

Which AWS service(s) will help implement this solution effectively?

- A. Use AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery. Create a CloudFront distribution that points to the S3 bucket with videos uploaded. CloudFront will direct the request to the best edge location, based on the user’s location enhancing the overall user experience
- **B. Use AWS Elemental MediaConvert for file-based video processing and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest** ✅
- C. Use Amazon S3 for storage and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest
- D. Deploy the application on Amazon EC2 instances with access to the S3 bucket. Configure these with a Network Load Balancer (NLB). Deploy the application stack in multiple AWS Regions around the world and configure Global Accelerator to serve content to the user

### Explanation

Correct option:

Use AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest

A complete on-demand streaming solution typically makes use of Amazon S3 for storage, AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery.

Once videos are uploaded to the Amazon S3 bucket, you may need to convert your video into the size, resolution, or format needed by a particular television or connected device. AWS Elemental MediaConvert will take care of this for you. MediaConvert takes content from S3, transcodes it per your request, and stores the result back in S3. Transcoding processes video files, creating compressed versions of the original content to reduce its size, change its format, or increase playback device compatibility.

With your content safely stored and available in the formats required by your users, the next step is global delivery with Amazon CloudFront. The Amazon Content Delivery Network caches content at the edges for low latency and high throughput video delivery. Its scalability means that you can serve up as much or as little video as you want.

A family of video streaming protocols including Apple’s HTTP Live Streaming (HLS), Dynamic Adaptive Streaming over HTTP (DASH), Microsoft’s Smooth Streaming (MSS), and Adobe’s HTTP Dynamic Streaming (HDS) improves the user experience by delivering video as it is being watched, generally fetching content a few seconds ahead of when it will be needed. Playback starts more quickly, fast-forwarding is more efficient, and the overall user experience is smoother. With this option, you only pay for what the viewer watches, you don’t waste the user’s bandwidth, and users get to see the desired content more quickly.

You will need to do a little more work to implement the second option. First, you use MediaConvert to convert your video files to HLS format (the most widely supported streaming protocol). This will split the video into short segments and will also create a manifest file. Then, you point the CloudFront distribution at the manifest. Finally, to play the live stream, embed the manifest URL in the players that your users will play your live stream with. For example, to play a live stream for which the manifest file is myStream/playlist.m3u8 and the CloudFront distribution is d111111abcdef8.cloudfront.net, you embed the following URL in players: http://d111111abcdef8.cloudfront.net/myStream/playlist.m3u8

On-demand streaming of content stored in Amazon S3:

via - https://aws.amazon.com/cloudfront/streaming/

Incorrect options:

Use AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery. Create a CloudFront distribution that points to the S3 bucket with videos uploaded. CloudFront will direct the request to the best edge location, based on the user’s location enhancing the overall user experience - This option is very easy to implement and is supported by just about every mobile device and desktop. All you need to do is to put your content in an S3 bucket and create a CloudFront distribution that points to the bucket. Your user’s video player will use CloudFront URLs (accessible as part of the distribution) to request the video file. The request will be directed to the best edge location, based on the user’s location. The CDN will serve the video from its cache, fetching it from the S3 bucket if it is not already cached. This option has a couple of downsides. It makes inefficient use of your viewer’s bandwidth. If the user doesn’t bother to watch the entire video, content that would never be seen is still downloaded and you are paying for it.

Use Amazon S3 for storage and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest - For this case, AWS Elemental MediaConvert is required to convert your video into the size, resolution, or format needed by a particular television or connected device. Else this functionality will have to be custom-built.

Deploy the application on Amazon EC2 instances with access to the S3 bucket. Configure these with a Network Load Balancer (NLB). Deploy the application stack in multiple AWS Regions around the world and configure Global Accelerator to serve content to the user - AWS Elemental MediaConvert is required to convert your video into the size, resolution, or format needed by a particular television or connected device. Or this functionality will have to be custom-built. Video streaming protocols improve the user experience by delivering video as it is being watched, generally fetching content a few seconds ahead of when it will be needed. This will enhance the user experience by not hogging the network bandwidth of the user. The option lacks the video processing capabilities of AWS Elemental MediaConvert and the efficient delivery capabilities of CloudFront.

References:

https://aws.amazon.com/blogs/networking-and-content-delivery/how-flowplayer-improved-live-video-ingest-with-aws-global-accelerator/

https://aws.amazon.com/cloudfront/streaming/

---

## Question 50

**Category:** CSAP – Design for New Solutions

An e-commerce company has a three-tier web application with separate subnets for Web, Application and Database tiers. The CTO at the company wants to monitor any malicious activity targeting the web application running on EC2 instances. As a solutions architect, you have been tasked with developing a solution to notify the security team in case the network exposure of EC2 instances on specific ports violates the security policies of the company.

Which AWS Services would you use to build an automated notification system to meet these requirements with the least development effort? (Select two)

- A. AWS Shield
- B. VPC Flow Logs
- **C. Amazon SNS** ✅
- **D. Amazon Inspector** ✅
- E. Amazon CloudWatch

### Explanation

Correct options:

Amazon SNS

Amazon Inspector

Amazon Inspector is an automated security assessment service that helps you test the network accessibility of your Amazon EC2 instances and the security state of your applications running on the instances.

You can perform network security assessments via your own custom solutions, however, that entails significant time and effort. You might need to run network port-scanning tools to test routing and firewall configurations, then validate what processes are listening on your instance network ports, before finally mapping the IPs identified in the port scan back to the host’s owner.

To make this process simpler for its customers, AWS offers the Network Reachability rules package in Amazon Inspector, which is an automated security assessment service that enables you to understand and improve the security and compliance of applications deployed on AWS. The existing Amazon Inspector host assessment rules packages check the software and configurations on your Amazon Elastic Compute Cloud (Amazon EC2) instances for vulnerabilities and deviations from best practices.


via https://aws.amazon.com/blogs/security/amazon-inspector-assess-network-exposure-ec2-instances-aws-network-reachability-assessments/

You can use these rules packages to analyze the accessibility of critical ports, as well as all other network ports. For critical ports, Amazon Inspector will show the exposure of each and will offer findings per port. When critical, well-known ports (based on Amazon’s standard guidance) are reachable, findings will be created with higher severities.


via https://aws.amazon.com/blogs/security/amazon-inspector-assess-network-exposure-ec2-instances-aws-network-reachability-assessments/

The findings also have recommendations that include information about exactly which Security Group you can edit to remove the access. And like all Amazon Inspector findings, these can be published to an SNS topic for additional processing or you could use a Lambda to automatically remove ingress rules in the Security Group to address a network reachability finding. For the given use case, the network engineer can use the SNS topic to send the notifications to the team.

Incorrect options:

AWS Shield - AWS Shield is a managed service that protects against Distributed Denial of Service (DDoS) attacks for applications running on AWS. AWS Shield Standard is automatically enabled to all AWS customers at no additional cost. AWS Shield Advanced is an optional paid service. AWS Shield Advanced provides additional protections against more sophisticated and larger attacks for your applications running on Amazon EC2, Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator, and Route 53. AWS Shield cannot be used to assess network exposure of EC2 instances on specific ports.

Amazon CloudWatch - Amazon CloudWatch is a monitoring service for AWS cloud resources and the applications you run on AWS. You can use Amazon CloudWatch to collect and track metrics, collect and monitor log files, and set alarms. CloudWatch cannot be used to assess network exposure of EC2 instances on specific ports.

VPC Flow Logs - VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored. You can use VPC Flow Logs to assess network exposure of EC2 instances on specific ports but the solution would entail significant development effort to parse through the logs and identify the exposed ports. So this option is incorrect.

Reference:

https://aws.amazon.com/blogs/security/amazon-inspector-assess-network-exposure-ec2-instances-aws-network-reachability-assessments/

---

## Question 51

**Category:** CSAP – Accelerate Workload Migration and Modernization

An on-premises data center, set up a decade ago, hosts all the applications of a business. The business now wants to move to AWS Cloud. The documentation of these systems is outdated and complete knowledge of all existing workloads is absent. The data center hosts a mix of Windows and Linux virtual machines.

As a solutions architect, you need to provide a plan to migrate all the applications to the cloud. How will you gather the necessary data of the existing machines?

- A. Register the on-premises VMs with the AWS Migration Hub to collect configuration and utilization data
- B. Deploy the AWS Server Migration Service (AWS SMS) connector using the OVA image on the VMware cluster to collect configuration and utilization data from the VMs
- **C. Install the AWS Application Discovery Service on each of the VMs to collect the configuration and utilization data** ✅
- D. Use the AWS Migration Portfolio Assessment (MPA) tool to connect to each of the VMs to collect the configuration and utilization data

### Explanation

Correct option:

Install the AWS Application Discovery Service on each of the VMs to collect the configuration and utilization data - AWS Application Discovery Service helps enterprise customers plan migration projects by gathering information about their on-premises data centers. ADS will discover on-premises or other hosted infrastructure. This includes details such as server hostnames, IP and MAC addresses, resource allocation, and utilization details of key resources.

Planning data center migrations can involve thousands of workloads that are often deeply interdependent. Server utilization data and dependency mapping are important early first steps in the migration process. AWS Application Discovery Service collects and presents configuration, usage, and behavior data from your servers to help you better understand your workloads.

ADS will identify server dependencies by recording inbound and outbound network activity for each server. ADS will provide details on server performance. It captures performance information about applications and processes by measuring metrics such as host CPU, memory, and disk utilization. It also will allow you to search in Amazon Athena with predefined queries.

The collected data is retained in encrypted format in an AWS Application Discovery Service data store. In addition, this data is also available in AWS Migration Hub, where you can migrate the discovered servers and track their progress as they get migrated to AWS.

All about portfolio assessment and migration planning:

via - https://aws.amazon.com/blogs/architecture/accelerating-your-migration-to-aws/

Incorrect options:

Deploy the AWS Server Migration Service (AWS SMS) connector using the OVA image on the VMware cluster to collect configuration and utilization data from the VMs - AWS SMS combines data collection tools with automated server replication to speed the migration of on-premises servers to AWS. AWS SMS is an agentless service, which makes it easier and faster for you to migrate thousands of on-premises workloads to AWS.

As of March 31, 2022, AWS has discontinued AWS Server Migration Service (AWS SMS). Going forward, AWS recommends AWS Application Migration Service (AWS MGN) as the primary migration service for lift-and-shift migrations.

Use the AWS Migration Portfolio Assessment (MPA) tool to connect to each of the VMs to collect the configuration and utilization data - AWS MPA is a detailed portfolio assessment (server right-sizing, pricing, TCO comparisons, migration cost analysis), as well as migration planning (application data analysis and data collection, application grouping, migration prioritization, and wave planning), can be done online using Migration Portfolio Assessment. MPA offers extensive configuration support and enables experienced consultants to model customers’ scenarios and generate data for business case analysis and migration planning. MPA cannot collect and present configuration, usage, and behavior data from your servers to help you better understand your workloads.

Register the on-premises VMs with the AWS Migration Hub to collect configuration and utilization data - AWS Migration Hub provides a single location to track migration tasks across multiple AWS tools and partner solutions. With Migration Hub, you can choose the AWS and partner migration tools that best fit your needs while gaining visibility into the status of your migration projects. Migration Hub also provides key metrics and progress information for individual applications, regardless of which tools you use to migrate them. Migration Hub cannot collect and present configuration, usage, and behavior data from your servers to help you better understand your workloads.

Reference:

https://aws.amazon.com/blogs/architecture/accelerating-your-migration-to-aws/

---

## Question 52

**Category:** CSAP – Design for New Solutions

A weather monitoring agency stores and manages the global weather data for the last 50 years. The data has a velocity of 1GB per minute. You would like to store the data with only the most relevant attributes to build a predictive model for weather patterns.

Which of the following solutions would you use to build the most cost-effective solution with the LEAST amount of infrastructure maintenance?

- A. Capture the data in Kinesis Data Streams and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3
- B. Capture the data in a Spark Streaming Cluster on EMR use Spark Streaming transformations before writing to S3
- C. Capture the data in Kinesis Data Analytics and use SQL queries to filter and transform the data before writing to S3
- **D. Capture the data in Kinesis Data Firehose and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3** ✅

### Explanation

Correct option:

Capture the data in Kinesis Data Firehose and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3

Amazon Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

Kinesis Data Firehose Overview

via - https://aws.amazon.com/kinesis/data-firehose/

The correct option is to ingest the data in Kinesis Data Firehose and use a Lambda function to filter and transform the incoming data before the output is dumped on S3. This way you only need to store a sliced version of the data with only the relevant data attributes required for your model. Also, it should be noted that this solution is entirely serverless and requires no infrastructure maintenance.

Kinesis Data Firehose to S3:

via - https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html

Incorrect options:

Capture the data in Kinesis Data Analytics and use SQL queries to filter and transform the data before writing to S3 - Amazon Kinesis Data Analytics is the easiest way to analyze streaming data in real-time. Kinesis Data Analytics enables you to easily and quickly build queries and sophisticated streaming applications in three simple steps: set up your streaming data sources, write your queries or streaming applications and set up your destination for processed data. Kinesis Data Analytics cannot directly ingest data from the source as it ingests data either from Kinesis Data Streams or Kinesis Data Firehose, so this option is ruled out.

Capture the data in Kinesis Data Streams and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3 - Amazon Kinesis Data Streams (KDS) is a massively scalable, highly durable data ingestion and processing service optimized for streaming data. Amazon Kinesis Data Streams is integrated with many AWS services, including Amazon Kinesis Data Firehose for near real-time transformation.

Kinesis Data Streams cannot directly write the output to S3. In addition, KDS does not offer plug-and-play integration with an intermediary Lambda function as Firehose does. You will need to do a lot of custom coding to get the Lambda function to process the incoming stream and then reliably dump the transformed output to S3. So this option is incorrect.

Capture the data in a Spark Streaming Cluster on EMR use Spark Streaming transformations before writing to S3 - Amazon EMR is the industry-leading cloud big data platform for processing vast amounts of data using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto. Amazon EMR uses Hadoop, an open-source framework, to distribute your data and processing across a resizable cluster of Amazon EC2 instances.
Using an EMR cluster would imply managing the underlying infrastructure so it’s ruled out because the correct solution for the given use case should require the least amount of infrastructure maintenance.

References:

https://aws.amazon.com/kinesis/data-firehose/

https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html

---

## Question 53

**Category:** CSAP – Accelerate Workload Migration and Modernization

An e-commerce company is planning to migrate its IT infrastructure from the on-premises data center to AWS Cloud to ramp up its capabilities well in time for the upcoming Holiday Sale season. The company’s CTO has hired you as an AWS Certified Solutions Architect Professional to design a distributed, highly available and loosely coupled order processing application. The application is responsible for receiving and processing orders before storing them in a DynamoDB table. The application has seen sporadic traffic spikes in the past and the CTO wants the application to be able to scale during marketing campaigns to process the orders with minimal disruption.

Which of the following options would you recommend as the MOST reliable solution to address these requirements?

- **A. Ingest the orders in an SQS queue and trigger a Lambda function to process them** ✅
- B. Ingest the orders via a Step Function state machine and trigger an ECS container to process them
- C. Push the orders to an SNS topic and subscribe a Lambda function to process them
- D. Push the orders to Kinesis Data Streams and use Amazon EC2 instances to process them

### Explanation

Correct option:

Ingest the orders in an SQS queue and trigger a Lambda function to process them

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume. Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.

You can use an AWS Lambda function to process messages in an Amazon Simple Queue Service (Amazon SQS) queue. Lambda event source mappings support standard queues and first-in, first-out (FIFO) queues. With Amazon SQS, you can offload tasks from one component of your application by sending them to a queue and processing them asynchronously.


via - https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

AWS manages all ongoing operations and underlying infrastructure needed to provide a highly available and scalable message queuing service. With SQS, there is no upfront cost, no need to acquire, install, and configure messaging software, and no time-consuming build-out and maintenance of supporting infrastructure. SQS queues are dynamically created and scale automatically so you can build and grow applications quickly and efficiently.

Incorrect options:

Ingest the orders via a Step Function state machine and trigger an ECS container to process them - AWS Step Functions lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using Step Functions, you can design and run workflows that stitch together services such as AWS Lambda into feature-rich applications.


via - https://aws.amazon.com/step-functions/

You cannot use a Step Functions state machine to directly ingest incoming orders, so this option is incorrect.

Push the orders to Kinesis Data Streams and use Amazon EC2 instances to process them - You cannot use EC2 instances to process the orders because if the EC2 instances become unhealthy then the application would be unable to process the orders, thereby making the architecture unreliable.

Push the orders to an SNS topic and subscribe a Lambda function to process them - Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications. You cannot use SNS to facilitate reliable order processing workflow for the given use-case because once the Lambda function picks an order's message from the SNS topic, the order would remain unprocessed if the Lambda fails to process it successfully. In the case of SQS, the message will be available for re-processing after visibility timeout.

How SNS Works:

via - https://docs.aws.amazon.com/sns/latest/dg/welcome.html

References:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html

https://docs.aws.amazon.com/sns/latest/dg/welcome.html

---

## Question 54

**Category:** CSAP – Accelerate Workload Migration and Modernization

A gaming company runs its flagship application with an SLA of 99.99%. Global users access the application 24/7. The application is currently hosted on the on-premises data centers and it routinely fails to meet its SLA, especially when hundreds of thousands of users access the application concurrently. The engineering team has also received complaints from some users about high latency.

As a Solutions Architect Professional, how would you redesign this application for scalability and also allow for automatic failover at the lowest possible cost?

- A. Configure Route 53 geolocation-based routing to route to the nearest Region and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer
- B. Configure a combination of Route 53 failover routing with geolocation-based routing. Host the website behind an Application Load Balancer (ALB) with targets as EC2 instances that are automatically scaled via Auto-Scaling Group (ASG). Repeat this configuration of ALB with EC2 instances as targets that are scaled via ASG in multiple Regions. Use a Multi-AZ deployment with RDS MySQL as the data layer
- C. Configure Route 53 round-robin routing policy to distribute load evenly across all Regions and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer
- **D. Configure Route 53 latency-based routing to route to the nearest Region and activate the health checks. Host the website on S3 in each Region and use API Gateway with AWS Lambda for the application layer. Set up the data layer using DynamoDB global tables with DAX for caching** ✅

### Explanation

Correct option:

Configure Route 53 latency-based routing to route to the nearest Region and activate the health checks. Host the website on S3 in each Region and use API Gateway with AWS Lambda for the application layer. Set up the data layer using DynamoDB global tables with DAX for caching

You can use Route 53 routing policies for a hosted zone record to determine how Amazon Route 53 responds to queries.


via - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

You can use a combination of alias records (such as latency alias, weighted alias or failover alias) and non-alias records to build a decision tree that gives you greater control over how Route 53 responds to requests. For example, you might use latency alias records to select a Region close to a user and use weighted records for two or more resources within each Region to protect against the failure of a single endpoint or an Availability Zone.

The following schematic shows how you can use a combination of latency routing policy (that has health checks activated) with a weighted routing policy to manage a multi-Region routing infrastructure. In case a Region goes down, Route 53 would look for the latency alias record with the next-best latency and choose the record for the other Region.


via - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html

Therefore, for the given use-case, this solution allows for automatic failover while minimizing the latency. As the downstream components for this solution such as the API Gateway, Lambda functions and DynamoDB global tables (with DAX) are serverless, so it allows the solution to scale easily.

Incorrect options:

Configure Route 53 geolocation-based routing to route to the nearest Region and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer - You cannot use geolocation-based routing to route to the nearest Region as you need to use latency based routing to accomplish that.

Geolocation routing is used when you want to route traffic based on the location of your users. When you use geolocation routing, you can localize your content and present some or all of your website in the language of your users. You can also use geolocation routing to restrict the distribution of content to only the locations in which you have distribution rights. Other components mentioned in the stack are not a deal-breaker, but using geolocation-based routing makes this option incorrect.

Configure Route 53 round-robin routing policy to distribute load evenly across all Regions and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer - This option has been added as a distractor as there is no such thing as a Route 53 round-robin routing policy.

Configure a combination of Route 53 failover routing with geolocation-based routing. Host the website behind an Application Load Balancer (ALB) with targets as EC2 instances that are automatically scaled via Auto-Scaling Group (ASG). Repeat this configuration of ALB with EC2 instances as targets that are scaled via ASG in multiple Regions. Use a Multi-AZ deployment with RDS MySQL as the data layer - As mentioned earlier, you cannot use geolocation-based routing to route to the nearest Region as you need to use latency based routing to accomplish that. Failover routing could help with ensuring failover across AWS Regions, but using geolocation-based routing is a deal-breaker. Another red-flag is using Multi-AZ RDS MySQL as data layer, which can be deployed in just one AWS Region. You would need to develop and maintain custom data sync scripts/jobs to maintain data consistency across Regions.

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html

https://aws.amazon.com/premiumsupport/knowledge-center/route-53-dns-health-checks/

---

## Question 55

**Category:** CSAP – Design for New Solutions

A social gaming company is developing a mobile game that streams score updates to a backend processor and then publishes results on a leaderboard. The company has hired you to design a solution that can handle major traffic spikes, process the mobile game updates in the order of receipt, and store the processed updates in a highly available database. The company wants to minimize the management overhead required to maintain the solution.

Which of the following solutions will you recommend to meet these requirements?

- **A. Send score updates to Kinesis Data Streams which uses a Lambda function to process these updates and then store these processed updates in DynamoDB** ✅
- B. Send score updates to Kinesis Data Streams which uses a fleet of EC2 instances (with Auto Scaling) to process the updates in Kinesis Data Streams and then store these processed updates in DynamoDB
- C. Send score updates to an SQS queue which uses a fleet of EC2 instances (with Auto Scaling) to process these updates in the SQS queue and then store these processed updates in an RDS MySQL database
- D. Send score updates to an SNS topic, subscribe a Lambda function to this SNS topic to process the updates and then store these processed updates in a SQL database running on Amazon EC2

### Explanation

Correct option:

Send score updates to Kinesis Data Streams which uses a Lambda function to process these updates and then store these processed updates in DynamoDB

To help ingest real-time data or streaming data at large scale, you can use Amazon Kinesis Data Streams (KDS). KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources. The data collected is available in milliseconds, enabling real-time analytics. KDS provides ordering of records, as well as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications.

Lambda integrates natively with Kinesis Data Streams. The polling, checkpointing, and error handling complexities are abstracted when you use this native integration. The processed data can then be configured to be saved in DynamoDB.

Incorrect options:

Send score updates to an SQS queue which uses a fleet of EC2 instances (with Auto Scaling) to process these updates in the SQS queue and then store these processed updates in an RDS MySQL database

Send score updates to Kinesis Data Streams which uses a fleet of EC2 instances (with Auto Scaling) to process the updates in Kinesis Data Streams and then store these processed updates in DynamoDB

Send score updates to an SNS topic, subscribe a Lambda function to this SNS topic to process the updates, and then store these processed updates in a SQL database running on Amazon EC2

These three options use EC2 instances as part of the solution architecture. The use-case seeks to minimize the management overhead required to maintain the solution. However, EC2 instances involve several maintenance activities such as managing the guest operating system and software deployed to the guest operating system, including updates and security patches, etc. Hence these options are incorrect.

Reference:

https://aws.amazon.com/blogs/big-data/best-practices-for-consuming-amazon-kinesis-data-streams-using-aws-lambda/

---

## Question 56

**Category:** CSAP – Design for New Solutions

A mobile app based social media company is using Amazon CloudFront to deliver media-rich content to its audience across the world. The Content Delivery Network (CDN) offers a multi-tier cache by default, with regional edge caches that improve latency and lower the load on the origin servers when the object is not already cached at the edge. However, there are certain content types that bypass the regional edge cache and go directly to the origin.

Which of the following content types skip the regional edge cache? (Select two)

- A. Static content such as style sheets, JavaScript files
- **B. Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin** ✅
- **C. Dynamic content, as determined at request time (cache-behavior configured to forward all headers)** ✅
- D. E-commerce assets such as product photos
- E. User-generated videos

### Explanation

Correct options:

Dynamic content, as determined at request time (cache-behavior configured to forward all headers)

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.
CloudFront points of presence (POPs) (edge locations) make sure that popular content can be served quickly to your viewers. CloudFront also has regional edge caches that bring more of your content closer to your viewers, even when the content is not popular enough to stay at a POP, to help improve performance for that content.

Dynamic content, as determined at request time (cache-behavior configured to forward all headers), does not flow through regional edge caches, but goes directly to the origin. So this option is correct.

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin from the POPs and do not proxy through the regional edge caches. So this option is also correct.

How CloudFront works with regional edge caches:

via - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

Incorrect Options:

E-commerce assets such as product photos

User-generated videos

Static content such as style sheets, JavaScript files

The following type of content flows through the regional edge caches - user-generated content, such as video, photos, or artwork; e-commerce assets such as product photos and videos and static content such as style sheets, JavaScript files. Hence these three options are not correct.

Reference:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

---

## Question 57


**Category:** CSAP – Design for New Solutions

A cloud engineer at a fintech startup is preparing the infrastructure for a critical internal platform launch. The cloud engineer configures DNS resolution for a newly provisioned VPC in the ap-southeast-1 (Singapore) Region as part of the setup. This VPC uses the 13.232.18.0/24 CIDR block and has been integrated with Amazon Route 53 Resolver to manage DNS queries.
Initially, the team planned for basic DNS resolution, but the requirements have since changed to support more advanced functionality. Now, all domain name lookups must be routed through a Private hosted zone, and any Amazon EC2 instances with assigned Public IP addresses must automatically receive corresponding Public hostnames.
Which of the following should the cloud engineer do to satisfy the new requirements and ensure the domain names are resolved correctly and consistently within the VPC? (Select TWO.)

- **A. Set up a private DNS zone and link it to the VPC. Confirm that the VPC has both enableDnsSupport and enableDnsHostnames enabled.** ✅
- **B. Define a custom DHCP options set that specifies domain-name-servers=AmazonProvidedDNS, and attach this configuration to the VPC.** ✅
- C. Create a new DHCP options set that sets domain-name-servers=13.232.18.98, and apply this configuration to the VPC by associating it accordingly.
- D. Create a private hosted zone and associate it with the VPC. Ensure the VPC is configured with the appropriate instanceTenancy setting.
- E. Establish a private hosted zone and connect it to the designated VPC. Make sure that the enableNetworkAddressUsageMetrics feature is activated.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		One of the foundational networking components in the Virtual Private Cloud (VPC) is the Amazon DNS server, also known as the Route 53 Resolver. This DNS resolver service is natively integrated into each Availability Zone within the AWS Region, providing a reliable and scalable solution for domain name resolution within the VPC.
The VPC attributes enableDnsHostnames and enableDnsSupport determine the DNS support provided for your VPC. If both attributes are enabled, an instance launched into the VPC receives a public DNS hostname if assigned a public IPv4 address or an Elastic IP address at creation. If you enable both attributes for a VPC that didn’t previously have them enabled, instances already launched into that VPC receive public DNS hostnames if they have a public IPv4 address or an Elastic IP address.
On the other hand, a DHCP option set is a group of network settings used by resources in your VPC, such as EC2 instances, to communicate over your virtual network. If we create a DHCP option set that contains the setting domain-name-servers=AmazonProvidedDNS, we use the built-in Amazon DNS server. The Amazon DNS server in your VPC resolves the DNS domain names you specify in a private hosted zone in Route 53.

To summarize, enabling enableDnsSupport allows instances in the VPC to use a DNS resolver. Enabling enableDnsHostnames ensures that instances assigned public IP addresses receive corresponding public DNS hostnames. Defining a custom DHCP options set that specifies domain-name-servers=AmazonProvidedDNS ensures compatibility with Amazon Route 53 Resolver, including support for private hosted zones and automatic assignment of public hostnames to EC2 instances with public IPs.
Hence, the correct answers are:
– Set up a private DNS zone and link it to the VPC. Confirm that the VPC has both enableDnsSupport and enableDnsHostnames enabled
– Define a custom DHCP options set that specifies domain-name-servers=AmazonProvidedDNS, and attach this configuration to the VPC
The option that says: Create a private hosted zone and associate it with the VPC. Ensure the VPC is configured with the appropriate instanceTenancy setting is incorrect. The instanceTenancy option typically refers to whether instances in the VPC are launched on shared or dedicated hardware. This setting has no impact on DNS resolution or hostname assignment. It is unrelated to the functional requirements described in the scenario.
The option that says: Establish a private hosted zone and connect it to the designated VPC. Make sure that the enableNetworkAddressUsageMetrics feature is activated  is incorrect. The enableNetworkAddressUsageMetrics simply allows monitoring IP address usage through CloudWatch. While it may help track network resource consumption, it does not affect DNS functionality or contribute to resolving domain names or assigning hostnames.
The option that says: Create a new DHCP options set that sets domain-name-servers=13.232.18.98, and apply this configuration to the VPC by associating it accordingly is incorrect. Setting the domain-name-servers to a specific IP address, such as 13.232.18.98, overrides the default Amazon-provided DNS configuration. This setting could interfere with Route 53 Resolver features, such as support for private hosted zones and public DNS hostname assignment, which depend on the use of AmazonProvidedDNS. Therefore, this option does not meet the full requirements and could lead to inconsistent or incorrect DNS resolution within the VPC.
 
References:
https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html
https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSetConcepts.html
 
Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

---

## Question 58

**Category:** CSAP – Continuous Improvement for Existing Solutions

A company has an Elastic Load Balancer (ELB) that is configured with an Auto Scaling Group (ASG) having a minimum of 4, a maximum of 10, and the desired value of 4 instances. The ASG cooldown and the termination policies are configured to the default values. Monitoring reports indicate a general usage requirement of 4 instances, while any traffic spikes result in an additional 10 instances. Customers have been complaining of request timeouts and partially loaded pages.

As an AWS Certified Solutions Architect Professional, which of the following options will you suggest to fix this issue?

- A. Enable Sticky Sessions on ELB
- B. Configure termination policies on ASG to determine which instances it terminates first during scale-in events
- C. Add a lifecycle hook on scale-out event to your ASG, making sure that the instance is fully ready before it starts receiving traffic
- **D. Configure connection draining on ELB** ✅

### Explanation

Correct option:

Configure connection draining on ELB - To ensure that an ELB stops sending requests to instances that are de-registering or unhealthy while keeping the existing connections open, use connection draining. This enables the load balancer to complete in-flight requests made to instances that are de-registering or unhealthy.

When you enable connection draining, you can specify a maximum time for the load balancer to keep connections alive before reporting the instance as de-registered. The maximum timeout value can be set between 1 and 3,600 seconds (the default is 300 seconds). When the maximum time limit is reached, the load balancer forcibly closes connections to the de-registering instance.

When Connection Draining is enabled and configured, the process of deregistering an instance from an Elastic Load Balancer gains an additional step. For the duration of the configured timeout, the load balancer will allow existing, in-flight requests made to an instance to complete, but it will not send any new requests to the instance.

Incorrect options:

Configure termination policies on ASG to determine which instances it terminates first during scale-in events - Amazon EC2 Auto Scaling uses termination policies to determine which instances it terminates first during scale-in events. Termination policies define the termination criteria that is used by Amazon EC2 Auto Scaling when choosing which instances to terminate. However, termination policies are not relevant to the given use case.

Enable Sticky Sessions on ELB - Sticky session feature (also known as session affinity), enables the load balancer to bind a user's session to a specific instance. This ensures that all requests from the user during the session are sent to the same instance. The key to managing sticky sessions is to determine how long your load balancer should consistently route the user's request to the same instance. A sticky session is relevant for a use case that needs to maintain session functionality.

Add a lifecycle hook on scale-out event to your ASG, making sure that the instance is fully ready before it starts receiving traffic - Amazon EC2 Auto Scaling offers the ability to add lifecycle hooks to your Auto Scaling groups. These hooks enable an Auto Scaling group to be aware of events in the Auto Scaling instance lifecycle and then perform a custom action when the corresponding lifecycle event occurs. Adding a lifecycle hook on a scale-out event is not relevant for the given use case.

References:

https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html

https://aws.amazon.com/blogs/aws/elb-connection-draining-remove-instances-from-service-with-care/

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html

---

## Question 59


**Category:** CSAP – Design Solutions for Organizational Complexity

An international shipping company with a global fleet runs its cloud operations through a multi-account AWS environment managed by AWS Control Tower. Due to fluctuating fuel costs and rising logistics expenses, the company recently launched a company-wide cost-cutting initiative, including the tech department.
The company uses AWS Organizations for account-level boundaries, AWS Config to ensure compliance standards are met, and AWS Trusted Advisor to surface cost inefficiencies and potential security gaps.
As per the directive of the CTO, in line with company cost-cutting, only Amazon EC2 and Amazon RDS burstable instances should be allowed. All other services not directly supporting the company’s lean tech initiative must be blocked.
A solutions architect has been tasked with locking this down in a scalable, maintainable way aligned with AWS best practices.
What’s the most effective approach to enforce these service restrictions?

- A. Deploy Amazon GuardDuty to scan for unsupported AWS services and non-burstable EC2 or RDS instances. Use its findings to block non-compliant deployments automatically in the future.
- **B. Define a custom preventive guardrail within AWS Control Tower that enforces restrictions allowing only burstable instance types to be launched, while blocking access to any non-essential services. Assign this control to the target development OU to ensure policy compliance across applicable accounts.** ✅
- C. Enable AWS Trusted Advisor's cost optimization checks in each development account to enforce the usage of burstable instances and prevent launching non-approved services.
- D. Set up a custom detective guardrail in AWS Control Tower to monitor the environment for compliance, ensuring that only burstable instances are provisioned and that any usage of unauthorized services is flagged. Link this control to the corresponding OU to track adherence across associated accounts.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment, following prescriptive best practices. Its orchestration extends the capabilities of AWS Organizations. To help keep your organizations and accounts from drift, which is divergence from best practices, AWS Control Tower applies controls (sometimes called guardrails).
Preventive controls prevent actions from occurring. For example, the elective control called Disallow Changes to Bucket Policy for Amazon S3 Buckets (Previously called Disallow Policy Changes to Log Archive) prevents IAM policy changes within the log archive shared account. Any attempt to perform a prevented action is denied and logged in CloudTrail. The resource is also logged in AWS Config.
Detective controls detect specific events when they occur and log the action in CloudTrail. For example, the strongly recommended control called Detect Whether Encryption is Enabled for Amazon EBS Volumes Attached to Amazon EC2 Instances detects whether an unencrypted Amazon EBS volume is attached to an EC2 instance in your landing zone.

Custom preventive guardrails in the AWS Control Tower enforce policy before resource deployment. Preventive guardrails are backed by Service Control Policies (SCPs). They are designed to explicitly block actions that violate rules, such as launching non-burstable EC2 or RDS instances or accessing disallowed services. Assigning the control to the target OU ensures the restriction applies across all relevant accounts in a multi-account AWS environment, aligning with AWS best practices and the company’s cost-cutting directive.
Hence, the correct answer is: Define a custom preventive guardrail within AWS Control Tower that enforces restrictions allowing only burstable instance types to be launched, while blocking access to any non-essential services. Assign this control to the target development OU to ensure policy compliance across applicable accounts.
The option that says: Set up a custom detective guardrail in AWS Control Tower to monitor the environment for compliance, ensuring that only burstable instances are provisioned and that any usage of unauthorized services is flagged. Link this control to the corresponding OU to track adherence across associated accounts  is incorrect. Detective guardrails in AWS Control Tower do not block actions. They simply monitor and flag violations after they occur. While they are helpful for auditing and visibility, they cannot enforce restrictions in advance. This lack of enforcement capabilities means that non-burstable instances could still be launched, defeating the purpose of proactively managing costs and service usage.
The option that says: Deploy Amazon GuardDuty to scan for unsupported AWS services and non-burstable EC2 or RDS instances. Use its findings to block non-compliant deployments automatically in the future is incorrect. Amazon GuardDuty is primarily a threat detection service for identifying potential security risks like compromised resources or unusual API calls. It is not designed to enforce service usage policies or instance-type restrictions. One cannot rely on GuardDuty to block deployments, as it does not have preventive capabilities in this context.
The option that says: Enable AWS Trusted Advisor’s cost optimization checks in each development account to enforce the usage of burstable instances and prevent launching non-approved services is incorrect. AWS Trusted Advisor provides recommendations, not enforcement. It primarily offers insights into cost optimization and security best practices. It cannot enforce instance-type policies or prevent the use of non-approved services. Simply enabling Trusted Advisor checks will not restrict developers from launching non-compliant resources.
 
References:
https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
https://docs.aws.amazon.com/controltower/latest/userguide/how-controls-work.html
https://aws.amazon.com/blogs/aws/new-for-aws-control-tower-comprehensive-controls-management-preview/
 
Check out this AWS Control Tower Cheat Sheet:
https://tutorialsdojo.com/aws-control-tower/

---

## Question 60

**Category:** CSAP – Design Solutions for Organizational Complexity

An IT company wants to move all its clients belonging to the regulated and security-sensitive industries such as financial services and healthcare to the AWS Cloud as it wants to leverage the out-of-box security-specific capabilities offered by AWS. The Security team at the company is developing a framework to validate the adoption of AWS best practices and industry-recognized compliance standards. The AWS Management Console is the preferred method for the in-house teams wanting to provision resources. You have been hired as an AWS Certified Solutions Architect Professional to spearhead this strategic initiative.

Which of the following strategies would you adopt to address these business requirements for continuously assessing, auditing and monitoring the configurations of AWS resources? (Select two)

- A. Leverage CloudTrail integration with SNS to automatically notify unauthorized API activities. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services. Use Lambda functions to automatically revert non-authorized changes in AWS resources
- B. Leverage EventBridge events near-real-time capabilities to monitor system events patterns to trigger Lambda functions to automatically revert non-authorized changes in AWS resources. Send notifications via SNS topics to improve the incidence response time
- **C. Leverage Config rules to audit changes to AWS resources and monitor the compliance of the configuration by running the evaluations for the rule at a frequency that you choose. Develop AWS Config custom rules to establish a test-driven development approach by triggering the evaluation when any resource that matches the rule's scope changes in configuration** ✅
- **D. Enable trails and set up CloudTrail events to review and monitor management activities of all AWS accounts by logging these activities into CloudWatch Logs using a KMS key. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services** ✅
- E. Leverage CloudWatch Logs agent to collect all the AWS SDK logs. Search the log data using a pre-defined set of filter patterns that match mutating API calls. Use CloudWatch alarms to send notifications via SNS when unintended changes are performed. Archive log data by using a batch export to Amazon S3 and analyze via Athena

### Explanation

Correct options:

Leverage Config rules to audit changes to AWS resources and monitor the compliance of the configuration by running the evaluations for the rule at a frequency that you choose. Develop AWS Config custom rules to establish a test-driven development approach by triggering the evaluation when any resource that matches the rule's scope changes in configuration

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - “What did my AWS resource look like at xyz point in time?”.

How AWS Config Works:

via - https://aws.amazon.com/config/

For the given use-case, you can use AWS Config to evaluate the configuration settings of your AWS resources. You do this by creating AWS Config rules, which represent your ideal configuration settings. AWS Config provides customizable, predefined rules called managed rules to help you get started. You can also create your own custom rules. While AWS Config continuously tracks the configuration changes that occur among your resources, it checks whether these changes violate any of the conditions in your rules. If a resource violates a rule, AWS Config flags the resource and marks the rule as noncompliant.

There are two types of evaluation trigger types for Config rules:

Configuration changes – AWS Config triggers the evaluation when any resource that matches the rule's scope changes in configuration. The evaluation runs after AWS Config sends a configuration item change notification.

Periodic – AWS Config runs evaluations for the rule at a frequency that you choose (for example, every 24 hours).

Enable trails and set up CloudTrail events to review and monitor management activities of all AWS accounts by logging these activities into CloudWatch Logs using a KMS key. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services

CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. An event in CloudTrail is the record of activity in an AWS account. This activity can be an action taken by a user, role, or service that is monitorable by CloudTrail. CloudTrail events provide a history of both API and non-API account activity made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.

CloudTrail data events are disabled by default. You can enable logging at an additional cost. Data events are also known as data plane operations and are often high-volume activities. Data events aren't viewable in CloudTrail event history and are charged for all copies at a reduced rate compared to management events.

CloudTrail records management events for the last 90 days free of charge, and are viewable in the Event History with the CloudTrail console. For Amazon S3 delivery of CloudTrail events, the first copy delivered is free. Additional copies of management events are charged.


via - https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

Incorrect options:

Leverage CloudWatch Logs agent to collect all the AWS SDK logs. Search the log data using a pre-defined set of filter patterns that match mutating API calls. Use CloudWatch alarms to send notifications via SNS when unintended changes are performed. Archive log data by using a batch export to Amazon S3 and analyze via Athena - One of the key constraints for the given scenario is that the AWS Management Console is the preferred method for the in-house teams wanting to provision resources. Although this option is technically feasible, but it focuses on using CloudWatch Logs agent to collect all the AWS SDK logs. The given use-case has no specific requirements for AWS SDKs or AWS APIs because AWS Management Console is the preferred method to provision resources. So this option is not the best fit solution.

Leverage CloudTrail integration with SNS to automatically notify unauthorized API activities. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services. Use Lambda functions to automatically revert non-authorized changes in AWS resources - One of the key constraints for the given scenario is that the AWS Management Console is the preferred method for the in-house teams wanting to provision resources. Although this option is technically feasible, but it focuses on capturing unauthorized API activities. The given use-case has no specific requirements for AWS SDKs or AWS APIs because AWS Management Console is the preferred method to provision resources. In addition, the use-case just talks about assessing, auditing and monitoring the configurations of AWS resources. Reverting non-authorized changes in AWS resources is not part of the mandate. So this option is not correct.

Leverage EventBridge events near-real-time capabilities to monitor system events patterns to trigger Lambda functions to automatically revert non-authorized changes in AWS resources. Send notifications via SNS topics to improve the incidence response time - The use-case just talks about assessing, auditing and monitoring the configurations of AWS resources. Reverting non-authorized changes in AWS resources is not part of the mandate. So this option is not correct.

References:

https://aws.amazon.com/config/

https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_manage-rules.html

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

---

## Question 61

**Category:** CSAP – Design for New Solutions

A development team is designing a system on AWS that will leverage Amazon CloudFront for content caching and for protecting the underlying origin. The team has flagged a concern regarding a probable attack on the origin server IP addresses, despite it being served by CloudFront.

As an AWS Certified Solutions Architect Professional, which of the following would you recommend as the BEST solution for providing the strongest level of protection to the origin server?

- A. Configure an AWS Lambda@Edge function to validate that the traffic to the Application Load Balancer originates from CloudFront
- B. Configure private access to content by using special CloudFront signed URLs or signed cookies
- C. Configure Origin Access Identity(OAI) on the origin server, which will only allow requests originating from CloudFront
- **D. Configure CloudFront to use a custom header and configure an AWS WAF rule on the origin’s Application Load Balancer to accept only traffic that contains that header** ✅

### Explanation

Correct option:

Configure CloudFront to use a custom header and configure an AWS WAF rule on the origin’s Application Load Balancer to accept only traffic that contains that header - You can configure CloudFront to add custom headers to the requests that it sends to your origin. These custom headers enable you to send and gather information from your origin that you don’t get with typical viewer requests. These headers can even be customized for each origin. CloudFront supports custom headers for both custom and Amazon S3 origins.

You can use custom headers for a variety of things, such as the following:
1. Determining which requests come from a particular distribution - If you configure more than one CloudFront distribution to use the same origin, you can add different custom headers in each distribution. You can then use the logs from your origin to determine which requests came from which CloudFront distribution.
2. Enabling cross-origin resource sharing (CORS)
3. Controlling access to content

Incorrect options:

Configure Origin Access Identity(OAI) on the origin server, which will only allow requests originating from CloudFront - Using Origin Access Identity (OAI), access can be restricted to an Amazon S3 bucket, making it only accessible from CloudFront. OAI cannot be used for custom origins.

Configure an AWS Lambda@Edge function to validate that the traffic to the Application Load Balancer originates from CloudFront - Since AWS Lambda@Edge resides on the AWS backbone, it will not be able to validate traffic for the downstream application server such as for an EC2 instance or an Application Load Balancer.

Configure private access to content by using special CloudFront signed URLs or signed cookies - You can configure CloudFront to require that users access your files using either signed URLs or signed cookies. You then develop your application either to create and distribute signed URLs to authenticated users or to send Set-Cookie headers that set signed cookies for authenticated users. You cannot use signed URLs or signed cookies for the given use case.

Reference:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.html

---

## Question 62


**Category:** CSAP – Continuous Improvement for Existing Solutions

A game development startup runs a multiplayer gaming platform powered by Amazon EC2 instances and AWS Lambda functions. The EC2 fleet supports always-on services like matchmaking and leaderboards, which run under a consistent and stable workload. In contrast, Lambda functions are triggered by unpredictable, bursty events like player actions, achievements, or chat messages.
To keep gameplay smooth and responsive, the platform uses a high-performance caching layer backed by Amazon MemoryDB for Redis, with dedicated MemoryDB cache nodes storing session data and player stats.
An AWS solutions architect is tasked with designing a cost-optimized infrastructure that cuts down on monthly operating costs without sacrificing performance.
What is the most cost-effective strategy to meet these goals?

- **A. Use an EC2 instance Savings Plan to commit to the EC2 compute resources financially. Apply a Compute Savings Plan to offset the baseline utilization of Lambda functions. Allocate reserved nodes to provision capacity for the MemoryDB cache nodes.** ✅
- B. Leverage On-Demand pricing across all services to maintain flexibility. Use Lambda provisioned concurrency for better performance. Rely on auto-scaling EC2 instances instead of committing to Savings Plans.
- C. Use a Compute Savings Plan to cover EC2, Lambda, and MemoryDB usage in a single commitment. Configure Lambda reserved concurrency to manage unpredictable workloads. Provision MemoryDB cache nodes by acquiring reserved nodes to ensure dedicated capacity.
- D. Use EC2 Spot Instances to reduce compute costs for matchmaking and leaderboard services. Use On-Demand Lambda execution. Replace MemoryDB with Amazon ElastiCache.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		Savings Plans provide savings beyond On-Demand rates in exchange for a commitment to using a specified amount of compute power (measured per hour) for one or three years. Savings Plans offer a flexible pricing model that provides savings on AWS usage. You can save up to 72 percent on your AWS compute workloads.
EC2 Instance Savings Plans provide savings up to 72 percent off On-Demand, in exchange for a commitment to a specific instance family in a chosen AWS Region (for example, m5 in Virginia).
Compute Savings Plans provide the most flexibility and prices up to 66 percent off of On-Demand rates. These plans automatically apply to your EC2 instance usage, regardless of instance family (for example, m5, c5, etc.), instance size (for example, c5.large, c5.xlarge, etc.), Region (for example, us-east-1, us-east-2, etc.), operating system (for example, Windows, Linux, etc.), or tenancy (for example, Dedicated, default, Dedicated Host). They also apply to your Fargate and Lambda usage.
MemoryDB Reserved nodes, on the other hand, provide you with a significant discount compared to On-Demand node pricing. Reserved nodes are not physical nodes but a billing discount applied to using On-Demand nodes in your account. Discounts for reserved nodes are tied to node type and AWS Region.

Since the EC2 instances handle consistent and predictable workloads like matchmaking and leaderboards, committing to an EC2 instance Savings Plan is the most economical approach, as it offers the highest discount specifically for EC2 usage. The Lambda functions, which respond to bursty and inconsistent traffic patterns, should be covered using a Compute Savings Plan, but only up to the minimum baseline usage that can be forecasted. This configuration still allows cost savings without overcommitting. Finally, MemoryDB cache nodes, part of a caching layer with stable demand, are best supported through reserved nodes, ensuring provisioned capacity at a reduced cost compared to On-Demand.
This combination of service-specific purchase models aligns well with the application’s usage patterns, optimizing spending without compromising performance.
Hence, the correct answer is: Use an EC2 instance Savings Plan to commit to the EC2 compute resources financially. Apply a Compute Savings Plan to offset the baseline utilization of Lambda functions. Allocate reserved nodes to provision capacity for the MemoryDB cache nodes.
The option that says: Use a Compute Savings Plan to cover EC2, Lambda, and MemoryDB usage in a single commitment. Configure Lambda reserved concurrency to manage unpredictable workloads. Provision MemoryDB cache nodes by acquiring reserved nodes to ensure dedicated capacity is incorrect. This option is tempting at first glance because it offers a consolidated Compute Savings Plan, but this plan only gives moderate discounts. It does not take full advantage of workload predictability. EC2 instance Savings Plans offer deeper savings for EC2 workloads, so relying on Compute Savings Plans across all three services simply leaves potential savings on the table. Additionally, configuring Lambda reserved concurrency does not save money; it just reserves capacity. The answer also correctly suggests reserved nodes for MemoryDB, but this partial correctness isn’t enough to make it the best solution.
The option that says: Use EC2 Spot Instances to reduce compute costs for matchmaking and leaderboard services. Use On-Demand Lambda execution. Replace MemoryDB with Amazon ElastiCache is incorrect. This option makes several risky trade-offs in the name of savings, but they are inappropriate for the scenario. EC2 Spot Instances are not recommended for critical, always-on services like matchmaking or leaderboards because Spot capacity can be interrupted anytime. Using On-Demand Lambda means you’re just paying full price with no cost optimization, and replacing MemoryDB with ElastiCache is misleading. While ElastiCache is a Redis-compatible caching service, it lacks the high durability and multi-AZ replication features of MemoryDB, which are often essential in real-time gaming environments.
The option that says: Leverage On-Demand pricing across all services to maintain flexibility. Use Lambda provisioned concurrency for better performance. Rely on auto-scaling EC2 instances instead of committing to Savings Plans is incorrect. This option sacrifices cost savings entirely in the name of flexibility, which directly contradicts the goal of minimizing monthly expenses. Relying on On-Demand pricing across all services is simply the most expensive route. Using Lambda provisioned concurrency adds cost without addressing the variable, event-driven nature of Lambda workloads. Lastly, just depending on EC2 auto-scaling does not remove the need for committing to Savings Plans, especially when the EC2 usage is described as stable and predictable. This option misses the opportunity to optimize spend where it clearly could be.
 
References:
https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html
https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reservednodes.html
 
Check out this AWS Savings Plan Cheat Sheet:
https://tutorialsdojo.com/aws-savings-plan/

---

## Question 63

**Category:** CSAP – Continuous Improvement for Existing Solutions

An Internet-of-Things (IoT) company is using Kinesis Data Streams (KDS) to process IoT data from field devices. Multiple consumer applications are using the incoming data streams and the engineers have noticed a performance lag for the data delivery speed between producers and consumers of the data streams.

As a Solutions Architect Professional, which of the following would you recommend to improve the performance for the given use-case?

- A. Swap out Kinesis Data Streams with SQS FIFO queues to support the desired read throughput for the downstream applications
- B. Swap out Kinesis Data Streams with Kinesis Data Firehose to support the desired read throughput for the downstream applications
- C. Swap out Kinesis Data Streams with SQS Standard queues to support the desired read throughput for the downstream applications
- **D. Use Enhanced Fanout feature of Kinesis Data Streams to support the desired read throughput for the downstream applications** ✅

### Explanation

Correct option:

Use Enhanced Fanout feature of Kinesis Data Streams to support the desired read throughput for the downstream applications

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. By default, the 2MB/second/shard output is shared between all of the applications consuming data from the stream.

You should use enhanced fan-out if you have multiple consumers retrieving data from a stream in parallel. With enhanced fan-out developers can register stream consumers to use enhanced fan-out and receive their own 2MB/second pipe of read throughput per shard, and this throughput automatically scales with the number of shards in a stream.


via - https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/


via - https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

Incorrect options:

Swap out Kinesis Data Streams with Kinesis Data Firehose to support the desired read throughput for the downstream applications -  Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security. Kinesis Data Firehose can only write to S3, Redshift, Elasticsearch or Splunk. You can't have applications consuming data streams from Kinesis Data Firehose, that's the job of Kinesis Data Streams. Therefore this option is not correct.

Swap out Kinesis Data Streams with SQS Standard queues to support the desired read throughput for the downstream applications

Swap out Kinesis Data Streams with SQS FIFO queues to support the desired read throughput for the downstream applications

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent. As multiple applications are consuming the same stream concurrently, both SQS Standard and SQS FIFO are not the right fit for the given use-case.


via - https://aws.amazon.com/kinesis/data-streams/faqs/

References:

https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

https://aws.amazon.com/kinesis/data-streams/faqs/

---

## Question 64

**Category:** CSAP – Design for New Solutions

The product team at a global IoT technology company is looking to build features to facilitate better collaboration with the company's customers. As part of its research, the product team has figured out a market need to support both stateful and stateless client-server communications via the APIs developed using its platform.

You have been hired by the company as an AWS Certified Solutions Architect Professional to build a solution to fulfill this market need using AWS API Gateway. Which of the following would you recommend to the company?

- A. API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server
- B. API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server
- C. API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server
- **D. API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server** ✅

### Explanation

Correct option:
API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the front door for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications.

How API Gateway Works:

via - https://aws.amazon.com/api-gateway/

API Gateway creates RESTful APIs that:
Are HTTP-based.
Enable stateless client-server communication.
Implement standard HTTP methods such as GET, POST, PUT, PATCH, and DELETE.

API Gateway creates WebSocket APIs that:
Adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server.
Route incoming messages based on message content.

So API Gateway supports stateless RESTful APIs as well as stateful WebSocket APIs. Therefore this option is correct.

Incorrect options:
API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server

API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server

API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server

These three options contradict the earlier details provided in the explanation. To summarize, API Gateway supports stateless RESTful APIs and stateful WebSocket APIs. Hence these options are incorrect.


via - https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

Reference:

https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

---

## Question 65

**Category:** CSAP – Continuous Improvement for Existing Solutions

A supply-chain manufacturing company manages its AWS resources in an Elastic Beanstalk environment. For implementing a new security requirement, the company needs to assign a single static IP address to a load-balanced Elastic Beanstalk environment. Subsequently, this IP address will be used to uniquely identify traffic coming from the Elastic Beanstalk environment.

As a solutions architect, which of the following would you recommend as the BEST solution that requires minimal maintenance?

- A. Use a Bastion host to map multiple IP addresses into a single publicly exposed IP address
- B. Use a Network Address Translation (NAT) instance to map multiple IP addresses into a single publicly exposed IP address
- **C. Use a Network Address Translation (NAT) gateway to map multiple IP addresses into a single publicly exposed IP address** ✅
- D. Attach the same Elastic IP to all instances to obtain a single publicly exposed IP address

### Explanation

Correct option:

Use a Network Address Translation (NAT) gateway to map multiple IP addresses into a single publicly exposed IP address

Use a network address translation (NAT) gateway to map multiple IP addresses into a single publicly exposed IP address. When your Elastic Beanstalk environment uses a NAT gateway, the backend instances in your environment are launched in private subnets. Elastic Beanstalk routes outbound traffic through the NAT gateway. You can identify the source of the outbound traffic from the backend instances by the Elastic IP address. The Elastic IP address is a static IP address required by the NAT gateway.

The following steps are needed to implement this change. Elastic Beanstalk launches your Amazon Elastic Compute Cloud (Amazon EC2) instances into private subnets. These private subnets use a NAT gateway with an attached Elastic IP address as a default route. The load balancer is in public subnets. Elastic Beanstalk routes all external traffic to and from the load balancer through an internet gateway.

Incorrect options:

Attach the same Elastic IP to all instances to obtain a single publicly exposed IP address - This statement is incorrect. If an instance is in a private subnet then it not possible to attach an Elastic IP to it. Also, Elastic IP can only be used with one instance at a time.

Use a Network Address Translation (NAT) instance to map multiple IP addresses into a single publicly exposed IP address - You can use an Elastic IP address or a public IP address with a NAT instance. But, NAT instances have to be managed by the customers which do not meet the requirement of minimal maintenance, as mandated for the given use case.

Use a Bastion host to map multiple IP addresses into a single publicly exposed IP address - A bastion host is a server used to provide access to a private network from an external network, such as the Internet. The bastion host is not relevant for the given use case.

References:

https://aws.amazon.com/premiumsupport/knowledge-center/elastic-beanstalk-static-IP-address/

https://medium.com/awesome-cloud/aws-vpc-difference-between-internet-gateway-and-nat-gateway-c9177e710af6

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html

---

## Question 66

**Category:** CSAP – Accelerate Workload Migration and Modernization

A multi-national digital media company wants to exit out of the business of owning and maintaining its own IT infrastructure so it can redeploy resources toward innovation in Artificial Intelligence and related areas to create a better customer experience. As part of this digital transformation, the media company wants to archive about 9 PB of data in its on-premises data center to durable long term storage.

As a Solutions Architect Professional, what is your recommendation to migrate and store this data in the quickest and MOST cost-optimal way?

- A. Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data directly into AWS Glacier
- B. Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier
- **C. Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier** ✅
- D. Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data directly into AWS Glacier

### Explanation

Correct option:

Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier

Snowball Edge Storage Optimized is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. It provides up to 80 TB of usable HDD storage, 40 vCPUs, 1 TB of SATA SSD storage, and up to 40 Gb network connectivity to address large scale data transfer and pre-processing use cases.

The data stored on the Snowball Edge device can be copied into the S3 bucket and later transitioned into AWS Glacier via a lifecycle policy. You can't directly copy data from Snowball Edge devices into AWS Glacier.


via - https://docs.aws.amazon.com/whitepapers/latest/aws-overview/migration-services.html

Incorrect options:

Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier - AWS Snowmobile is an exabyte-scale data transfer service used to move extremely large amounts of data to AWS. You can transfer up to 100 PB per Snowmobile. Snowmobile makes it easy to move massive volumes of data to the cloud, including video libraries, image repositories, or even a complete data center migration.

AWS recommends that you should use Snowmobile to migrate large datasets of 10PB or more in a single location. For datasets less than 10PB or distributed in multiple locations, you should use Snowball. So, this option is not the best fit for the given use-case.


via - https://aws.amazon.com/snowmobile/faqs/

Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data directly into AWS Glacier - As mentioned above, AWS recommends that you should use Snowmobile to migrate large datasets of 10PB or more in a single location. For datasets less than 10PB or distributed in multiple locations, you should use Snowball. So, this option is not the best fit for the given use-case.

Although you should note that for Snowmobile, you can import your data directly into Glacier.

Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data directly into AWS Glacier - As mentioned earlier, you can't directly copy data from Snowball Edge devices into AWS Glacier. Hence, this option is incorrect.

References:

https://aws.amazon.com/snowball/

https://docs.aws.amazon.com/snowball/latest/ug/how-it-works.html

https://aws.amazon.com/snowmobile/faqs/

https://docs.aws.amazon.com/whitepapers/latest/aws-overview/migration-services.html

---

## Question 67

**Category:** CSAP – Continuous Improvement for Existing Solutions

A web application is hosted on a fleet of Amazon EC2 instances running behind an Application Load Balancer (ALB). A custom functionality has mandated the need for a static IP address for the ALB.

As a solutions architect, how will you implement this requirement while keeping the costs to a minimum?

- A. Configure Gateway Load Balancer in front of the Application Load Balancer to provide a static IP address for the ALB
- B. An Elastic IP can be registered to an Application Load Balancer only during the creation. Re-create the ALB with the new Elastic IP and switch the workload to the newly created ALB
- **C. Register the Application Load Balancer behind a Network Load Balancer that will provide the necessary static IP address to the ALB** ✅
- D. Configure Global Accelerator in front of the Application Load Balancer to provide a static IP address for the ALB

### Explanation

Correct option:

Register the Application Load Balancer behind a Network Load Balancer that will provide the necessary static IP address to the ALB - You can't assign a static IP address to an Application Load Balancer. If you need a static IP address for your Application Load Balancer, it's a best practice to register the Application Load Balancer behind a Network Load Balancer. The static IP address assigned to a Network Load Balancer doesn't change, providing a fixed entry point for your Application Load Balancer.

You can forward traffic from your Network Load Balancer, which provides support for PrivateLink and a static IP address per Availability Zone, to your Application Load Balancer. Create an Application Load Balancer-type target group, register your Application Load Balancer to it, and configure your Network Load Balancer to forward traffic to the Application Load Balancer-type target group.

Incorrect options:

An Elastic IP can be registered to an Application Load Balancer only during the creation. Re-create the ALB with the new Elastic IP and switch the workload to the newly created ALB - An Elastic IP address is a static public IPv4 address associated with your AWS account in a specific Region. Unlike an auto-assigned public IP address, an Elastic IP address is preserved after you stop and start your instance in a virtual private cloud (VPC). An ALB does not support an Elastic IP.

Configure Global Accelerator in front of the Application Load Balancer to provide a static IP address for the ALB - When you create an Application Load Balancer in the AWS Management Console, you can optionally add an accelerator at the same time. Elastic Load Balancing and Global Accelerator work together to transparently add the accelerator for you. The accelerator is created in your account, with the load balancer as an endpoint. Using an accelerator provides static IP addresses and improves the availability and performance of your applications. However, Global Accelerator will not be a cost-effective choice when compared to a Network Load Balancer.

Configure Gateway Load Balancer in front of the Application Load Balancer to provide a static IP address for the ALB - You should use Gateway Load Balancer when deploying inline virtual appliances where network traffic is not destined for the Gateway Load Balancer itself. Gateway Load Balancer transparently passes all Layer 3 traffic through third-party virtual appliances and is invisible to the source and destination of the traffic. This option has been added as a distractor.

References:

https://aws.amazon.com/premiumsupport/knowledge-center/on-premises-direct-connect-traffic/

https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/

https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.alb-accelerator.html

---

## Question 68

**Category:** CSAP – Continuous Improvement for Existing Solutions

An e-commerce company runs its flagship website on its on-premises Linux servers. Recently, the company suffered outages after announcing huge discounts on its website. The web tier of the application is fronted by Elastic Load Balancer while the database tier is built on RDS MYSQL database. The company is planning to run heavy discounts for the upcoming holiday sales season. The company is looking for a solution to avoid any similar outages as well as quickly ramp up the ability to handle huge traffic spikes.

As an AWS Certified Solutions Architect Professional, which of the following would you suggest as the most optimal solution that can enhance the application's capabilities to handle the sudden spikes in user traffic without significant development effort?

- **A. Create a CloudFront distribution and configure CloudFront to cache objects from a custom origin. This will offload some traffic from the on-premises servers. Customize CloudFront cache behavior by setting Time To Live (TTL) to suit your business requirement** ✅
- B. Change the application architecture to use Docker containers and redeploy on AWS with ECS
- C. Create an S3 bucket and configure it for website hosting. Migrate your DNS to Route53 and leverage Route53 DNS failover to failover to the S3 hosted website
- D. Lift and Shift the application using AWS Elastic Beanstalk to enhance the scalability of the application without any downtime on the existing one

### Explanation

Correct option:

Create a CloudFront distribution and configure CloudFront to cache objects from a custom origin. This will offload some traffic from the on-premises servers. Customize CloudFront cache behavior by setting Time To Live (TTL) to suit your business requirement

CloudFront distribution supports custom origin servers. You can control how long your files stay in a CloudFront cache before CloudFront forwards another request to your origin. Reducing the duration allows you to serve dynamic content. Increasing the duration means that your users get better performance because your files are more likely to be served directly from the edge cache. A longer duration also reduces the load on your origin.

Typically, CloudFront serves a file from an edge location until the cache duration that you specified passes—that is until the file expires. After it expires, the next time the edge location gets a user request for the file, CloudFront forwards the request to the origin server to verify that the cache contains the latest version of the file. To change the cache duration for all files that match the same path pattern, you can change the CloudFront settings for Minimum TTL, Maximum TTL, and Default TTL for a cache behavior.

The CloudFront cache will offload some traffic from the on-premises servers thereby improving the performance as well as scale the ability to handle any traffic spikes.

Incorrect options:

Change the application architecture to use Docker containers and redeploy on AWS with ECS - This requires writing custom code and hence is not a feasible solution for the given scenario as it involves significant development effort.

Lift and Shift the application using AWS Elastic Beanstalk to enhance the scalability of the application without any downtime on the existing one - The company is looking for an immediate solution that can handle the peak traffic for the upcoming holiday season, hence AWS Elastic Beanstalk is not the right choice here as it involves significant changes in the underlying architecture.

Create an S3 bucket and configure it for website hosting. Migrate your DNS to Route53 and leverage Route53 DNS failover to failover to the S3 hosted website - Amazon S3 can be used for hosting static websites only. Since the use case does not specifically mention the content being static, this option is ruled out.

Reference:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html

---

## Question 69


**Category:** CSAP – Design Solutions for Organizational Complexity

A cloud-native enterprise manages its environments using AWS Organizations within a multi-account structure. As part of the container-based architecture, the team packages workloads into Docker images and stores these in Amazon Elastic Container Registry (Amazon ECR).
These images must remain accessible only to accounts in the same AWS Organization. The images are pushed via a CI/CD process, which runs multiple times daily. The company wants to retain all tagged images while limiting untagged images to the five most recent ones to reduce storage costs.
The company prefers a solution that minimizes operational overhead, securely manages access, and ensures that only required ECR operations are permitted.
Which approach best meets the company’s goals with the LEAST operational burden?

- A. Provision a public repository in ECR and apply a permissions policy scoped to essential ECR operations. Use the aws:PrincipalOrgID condition key to enforce organization-wide access control. Design an AWS Step Functions workflow to retain all tagged images and remove older untagged ones, keeping just the latest five.
- B. Configure a public ECR repository with limited permissions via a policy that employs the aws:PrincipalIsAWSService condition key for organizational restrictions. Set up an Amazon ECS Scheduled Task that retains all tagged images and automatically purges untagged images, ensuring only the five most recent remain.
- **C. Create a private ECR repository and define a permissions policy that allows only the required ECR operations, with a condition using the aws:PrincipalOrgID key to restrict access to the organization. Apply a lifecycle rule to the repository to retain all tagged images and delete untagged images beyond the most recent five.** ✅
- D. Set up a private ECR repository and attach a permissions policy restricting access based on the aws:PrincipalIsAWSService condition key, allowing only the necessary ECR actions. Use an AWS Glue job to keep all tagged images while routinely cleaning up untagged ones, preserving only the five most recent ones.

### Explanation

Correct
																		
									
								
								
																			
									Incorrect								
																		Amazon ECR (Elastic Container Registry) supports lifecycle policies that allow you to automatically manage the images’ lifecycle in your repositories. These policies can be used to remove untagged images or keep only the most recent ones based on criteria such as imageTagStatus or countNumber, which makes them ideal for reducing storage costs without needing custom logic or additional computing resources. In this case, applying a lifecycle policy that retains all tagged images and deletes only the older untagged ones while keeping the five most recent is a built-in capability that aligns perfectly with the company’s requirements and minimizes operational overhead.
Regarding access control, Amazon ECR supports fine-grained repository permissions using resource-based policies. Using the aws:PrincipalOrgID condition key ensures that only principals (such as IAM users, roles, or services) within the same AWS Organization are granted access. This method is highly effective for organization-wide restrictions and is recommended for securely sharing resources across multiple accounts. This approach simplifies management because the policy doesn’t require managing individual account IDs.

Using a private ECR repository with a permissions policy scoped to required actions and restricted by aws:PrincipalOrgID, combined with lifecycle rules to retain tagged images and limit untagged ones to the five most recent, meets the requirements for secure access, minimal operational overhead, and precise control over ECR operations.
Hence, the correct answer is: Create a private ECR repository and define a permissions policy that allows only the required ECR operations, with a condition using the aws:PrincipalOrgID key to restrict access to the organization. Apply a lifecycle rule to the repository to retain all tagged images and delete untagged images beyond the most recent five.
The option that says: Set up a private ECR repository and attach a permissions policy restricting access based on the aws:PrincipalIsAWSService condition key, allowing only the necessary ECR actions. Use an AWS Glue job to keep all tagged images while routinely cleaning up untagged ones, preserving only the five most recent ones is incorrect. Although it uses a private ECR repository and restricts access with a condition key (aws:PrincipalIsAWSService), that specific key is designed for service principals (such as allowing access to AWS services) and not restricting access based on organization membership. The correct key for that purpose is aws:PrincipalOrgID. Additionally, using an AWS Glue job to clean up old untagged images introduces unnecessary operational complexity. Glue is intended only for ETL (extract, transform, load) workloads, not for lifecycle management of container images. Using Glue here requires additional scheduling and scripting logic that could be entirely avoided with a native ECR lifecycle policy.
The option that says: Provision a public repository in ECR and apply a permissions policy scoped to essential ECR operations. Use the aws:PrincipalOrgID condition key to enforce organization-wide access control. Design an AWS Step Functions workflow to retain all tagged images and remove older untagged ones, keeping just the latest five  is incorrect. It proposes using a public ECR repository, which contradicts the security requirement that the images be accessible only to accounts within the same organization. Public repositories are visible to all AWS accounts (and, optionally, anonymous users), which opens up unintended exposure. Even though it correctly applies the aws:PrincipalOrgID condition for access control, using a public repository is a security misstep. Furthermore, implementing image cleanup using AWS Step Functions adds complexity compared to lifecycle policies designed for this exact use case, with less overhead.
The option that says: Configure a public ECR repository with limited permissions via a policy that employs the aws:PrincipalIsAWSService condition key for organizational restrictions. Set up an Amazon ECS Scheduled Task that retains all tagged images and automatically purges untagged images, ensuring only the five most recent remain is incorrect. It suffers from both architectural and security issues. Like the previous option, it mistakenly recommends a public repository, which goes against the requirement of restricting image access within the AWS Organization. It also uses the aws:PrincipalIsAWSService condition key, which is inappropriate for controlling cross-account access within an organization. Finally, the image cleanup is managed using an ECS Scheduled Task, which introduces operational complexity that can be avoided using ECR’s native lifecycle policy feature.
 
References:
https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgid
https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html
 
Check out this Amazon Elastic Container Registry Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-container-registry-amazon-ecr/

---

## Question 70

**Category:** CSAP – Accelerate Workload Migration and Modernization

The DevOps team at a leading social media company uses Chef to automate the configurations of servers in the on-premises data center. The CTO at the company now wants to migrate the IT infrastructure to AWS Cloud with minimal changes to the server configuration workflows and at the same time account for less operational overhead post-migration to AWS. The company has hired you as an AWS Certified Solutions Architect Professional to recommend a solution for this migration.

Which of the following solutions would you recommend to address the given use-case?

- **A. Replatform the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS** ✅
- B. Replatform the IT infrastructure to AWS Cloud by leveraging AWS Config as a configuration management service to automate the configurations of servers on AWS
- C. Rehost the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS
- D. Rehost the IT infrastructure to AWS Cloud by leveraging AWS Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS

### Explanation

Correct option:

Replatform the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS

Replatforming is a migration strategy where you don't change the core architecture but leverage some cloud optimizations. Here are the six most common application migration strategies:


via - https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

For the given use-case, you can leverage AWS OpsWorks to automate the configurations of your servers. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments. Specifically, OpsWorks for Chef Automate provides a fully managed Chef server and suite of automation tools that give you workflow automation for continuous deployment, automated testing for compliance and security, and a user interface that gives you visibility into your nodes and their status.

The migration results in an optimized IT infrastructure as OpsWorks for Chef Automate provides a configuration management experience that is fully compatible with Chef, including all community scripts and tooling, but without the operational overhead of managing the underlying Chef server.

Incorrect options:

Replatform the IT infrastructure to AWS Cloud by leveraging AWS Config as a configuration management service to automate the configurations of servers on AWS - AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - "What did my AWS resource look like at xyz point in time?". You cannot use AWS Config as a configuration management service to automate the configurations of servers on AWS.

How Config Works:

via - https://aws.amazon.com/config/

Rehost the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS - This option is incorrect because the correct migration strategy used for this use-case is Replatforming, as described in the explanation above. Rehosting refers to a migration strategy where no cloud optimizations are done and the application is migrated as-is.

Rehost the IT infrastructure to AWS Cloud by leveraging AWS Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS - As explained above, Rehosting is not the correct migration strategy for the given use-case. Elastic Beanstalk makes it easier for developers to quickly deploy and manage applications in the AWS Cloud. Developers simply upload their application, and Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring. You cannot use Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS.

References:

https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

https://aws.amazon.com/opsworks/

https://aws.amazon.com/config/

https://aws.amazon.com/elasticbeanstalk/faqs/

---

## Question 71

**Category:** CSAP – Design for New Solutions

A media company has its users accessing the content from different platforms including mobile, tablet, and desktop. Each platform is customized to provide a different user experience based on various viewing modes. Path-based headers are used to serve the content for different platforms, hosted on different Amazon EC2 instances. An Auto Scaling group (ASG) has also been configured for the EC2 instances to ensure that the solution is highly scalable.

Which of the following combination of services can help minimize the cost while maximizing the performance? (Select two)

- A. Network Load Balancer
- B. Amazon Route 53 with traffic flow policies
- **C. Application Load Balancer** ✅
- D. Amazon S3 configured as a static website
- **E. Amazon CloudFront with Lambda@Edge** ✅

### Explanation

Correct options:

Amazon CloudFront with Lambda@Edge - Lambda@Edge is a feature of Amazon CloudFront that lets you run code closer to users of your application, which improves performance and reduces latency. Lambda@Edge runs your code in response to events generated by the Amazon CloudFront content delivery network (CDN). By combining Lambda@Edge with other AWS services, developers can build dynamic, powerful web applications at the edge that automatically scale up and down—with zero origin infrastructure and administrative effort required for automatic scaling, backups, or data center redundancy.

By using Lambda@Edge to dynamically route requests to different origins based on different viewer characteristics, you can balance the load on your origins, while improving the performance for your users. For example, you can route requests to origins within a home region, based on a viewer's location.

With Lambda@Edge, you don't have to provision or manage infrastructure in multiple locations around the world. You pay only for the compute time you consume - there is no charge when your code is not running.

Intelligently Route Across Origins and Data Centers:

via - https://aws.amazon.com/lambda/edge/

Application Load Balancer - An Application Load Balancer serves as the single point of contact for clients. The load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. This increases the availability of your application. You add one or more listeners to your load balancer. ALB offers support for Path conditions. You can configure rules for your listener that forward requests based on the URL in the request. This enables you to structure your application as smaller services, and route requests to the correct service based on the content of the URL.

Incorrect options:

Network Load Balancer - Application Load Balancer works at the Application Layer (Layer 7 of the OSI model, Request level). Network Load Balancer works at the Transport layer (Layer 4 of the OSI model). NLB just forwards requests whereas ALB examines the contents of the HTTP request header to determine where to route the request. So, the application load balancer can perform content-based routing while NLB cannot.

Amazon S3 configured as a static website - It is mentioned in the use case that the application is hosted on an Amazon EC2 instance and that a solution is needed for performance and cost-effectiveness. Hence, using Amazon S3 as a static website is not a correct option.

Amazon Route 53 with traffic flow policies - Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost-effective way to route end users to Internet applications by translating names like www.example.com into the numeric IP addresses like 192.0.2.1 that computers use to connect. Amazon Route 53 is fully compliant with IPv6 as well.

Traffic Flow policy allows an Amazon Web Services customer to define how end-user traffic is routed to application endpoints through a visual interface. Route 53 can route between domains and subdomains but is not useful for path-based traffic flows.

References:

https://aws.amazon.com/lambda/edge/

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html

https://aws.amazon.com/premiumsupport/knowledge-center/create-subdomain-route-53/

---

## Question 72

**Category:** CSAP – Design Solutions for Organizational Complexity

A financial services firm intends to migrate its IT operations to AWS. The security team is establishing a framework to ensure that AWS best practices are being followed. AWS management console is the only way used by the IT teams to provision AWS resources. As per the firm's compliance requirements, the AWS resources need to be maintained in a particular configuration and audited regularly for unauthorized changes.

As an AWS Certified Solutions Architect Professional, how will you implement this requirement? (Select two)

- A. Leverage Systems Manager to view and control your infrastructure on AWS, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS infrastructure. Use SNS topics to enable notifications and improve the response time of incident responses
- B. Leverage CloudWatch Logs agent to aggregate all the AWS SDK logs. Analyze the log data using a pre-defined set of filter patterns that match any changes in the API calls. Trigger notifications via Amazon CloudWatch alarms when unintended changes are performed
- **C. Leverage AWS Config rules for auditing changes to AWS resources periodically and monitor the compliance of the configuration. Set up AWS Config custom rules using AWS Lambda to create a test-driven development approach, and finally automate the evaluation of configuration changes against the required controls** ✅
- D. Leverage EventBridge events to monitor and evaluate system events patterns, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS resources. Use SNS topics to enable notifications and improve the response time of incident responses
- **E. Leverage AWS CloudTrail events to review management activities of all AWS accounts. Make sure that CloudTrail is enabled in all accounts for the available AWS services. Enable CloudTrail trails and encrypt CloudTrail event log files with an AWS KMS key and monitor the recorded events via CloudWatch Logs** ✅

### Explanation

Correct options:

Leverage AWS Config rules for auditing changes to AWS resources periodically and monitor the compliance of the configuration. Set up AWS Config custom rules using AWS Lambda to create a test-driven development approach, and finally automate the evaluation of configuration changes against the required controls - AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting. AWS Config service is tailor-made for this requirement.

Leverage AWS CloudTrail events to review management activities of all AWS accounts. Make sure that CloudTrail is enabled in all accounts for the available AWS services. Enable CloudTrail trails and encrypt CloudTrail event log files with an AWS KMS key and monitor the recorded events via CloudWatch Logs - AWS CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

Visibility into your AWS account activity is a key aspect of security and operational best practices. You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. You can identify who or what took which action, what resources were acted upon, when the event occurred, and other details to help you analyze and respond to activity in your AWS account. Optionally, you can enable AWS CloudTrail Insights on a trail to help you identify and respond to unusual activity.

You can integrate CloudTrail into applications using the API, automate trail creation for your organization, check the status of trails you create, and control how users view CloudTrail events.

CloudTrail security best practices suggested by AWS are:
1. Create a trail
2. Apply trails to all AWS Regions
3. Enable CloudTrail log file integrity
4. Integrate with Amazon CloudWatch Logs

These steps are all covered in this option and hence it's the right choice for the given requirement.

Incorrect options:

Leverage Systems Manager to view and control your infrastructure on AWS, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS infrastructure. Use SNS topics to enable notifications and improve the response time of incident responses - AWS Systems Manager (formerly known as SSM) is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed nodes and reporting on (or taking corrective action on) any policy violations it detects.

Systems Manager supports Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and virtual machines (VMs). Beyond these resources, Systems Manager cannot be used for managing other AWS resources, so this option is incorrect.

Leverage CloudWatch Logs agent to aggregate all the AWS SDK logs. Analyze the log data using a pre-defined set of filter patterns that match any changes in the API calls. Trigger notifications via Amazon CloudWatch alarms when unintended changes are performed - The CloudWatch Logs agent provides an automated way to send log data to CloudWatch Logs only from Amazon EC2 instances. It cannot aggregate all the AWS SDK logs, so this option is incorrect.

Leverage EventBridge events to monitor and evaluate system events patterns, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS resources. Use SNS topics to enable notifications and improve the response time of incident responses - EventBridge events can certainly be used to monitor and evaluate system events patterns, however, it would involve significant development effort to handle all configuration changes across the AWS services. Using AWS Config with automated resource configuration management via Lambda functions is a better choice.

References:

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html

https://aws.amazon.com/config/

---

## Question 73

**Category:** CSAP – Design for New Solutions

A leading Internet-of-Things (IoT) solutions company needs to develop a platform that would analyze real-time clickstream events from embedded sensors in consumer electronic devices. The company has hired you as an AWS Certified Solutions Architect Professional to consult the engineering team and develop a solution using the AWS Cloud. The company wants to use clickstream data to perform data science, develop algorithms, and create visualizations and dashboards to support the business stakeholders. Each of these groups would work independently and would need real-time access to this clickstream data for their applications.

Which of the following options would provide a highly available and fault-tolerant solution to capture the clickstream events from the source and also provide a simultaneous feed of the data stream to the downstream applications?

- A. Use AWS Kinesis Data Analytics to facilitate multiple applications consume and analyze same streaming data concurrently and independently
- B. Use AWS Kinesis Data Firehose to allow applications to consume the same streaming data concurrently and independently
- **C. Use AWS Kinesis Data Streams to facilitate multiple applications consume same streaming data concurrently and independently** ✅
- D. Use Amazon SQS to facilitate multiple applications process same streaming data concurrently and independently

### Explanation

Correct option:

Use AWS Kinesis Data Streams to facilitate multiple applications consume the same streaming data concurrently and independently

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.

Amazon Kinesis Data Streams enables real-time processing of streaming big data. It provides ordering of records, as well as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications. The Amazon Kinesis Client Library (KCL) delivers all records for a given partition key to the same record processor, making it easier to build multiple applications reading from the same Amazon Kinesis data stream (for example, to perform counting, aggregation, and filtering).

Amazon Kinesis Data Streams is recommended when you need the ability for multiple applications to consume the same stream concurrently. For example, you have one application that updates a real-time dashboard and another application that archives data to Amazon Redshift. You want both applications to consume data from the same stream concurrently and independently.

KDS provides the ability for multiple applications to consume the same stream concurrently

via - https://aws.amazon.com/kinesis/data-streams/faqs/

Incorrect options:

Use AWS Kinesis Data Firehose to allow applications to consume same streaming data concurrently and independently - Amazon Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security. As Kinesis Data Firehose is used to load streaming data into data stores, therefore this option is incorrect.

Use AWS Kinesis Data Analytics to facilitate multiple applications consume and analyze same streaming data concurrently and independently - Amazon Kinesis Data Analytics is the easiest way to analyze streaming data in real-time.  You can quickly build SQL queries and sophisticated Java applications using built-in templates and operators for common processing functions to organize, transform, aggregate, and analyze data at any scale. Kinesis Data Analytics enables you to easily and quickly build queries and sophisticated streaming applications in three simple steps: setup your streaming data sources, write your queries or streaming applications and set up your destination for processed data. As Kinesis Data Analytics is used to build SQL queries on streaming data, therefore this option is incorrect.

Use Amazon SQS to facilitate multiple applications process same streaming data concurrently and independently - Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent. For SQS, you cannot have the same message being consumed by multiple consumers at the same time, therefore this option is incorrect.

References:

https://aws.amazon.com/kinesis/data-streams/faqs/

https://aws.amazon.com/kinesis/data-firehose/faqs/

https://aws.amazon.com/kinesis/data-analytics/faqs/

---

## Question 74

**Category:** CSAP – Continuous Improvement for Existing Solutions

A web application is running on a fleet of Amazon EC2 instances that are configured to operate in an Auto Scaling group (ASG). The instances are fronted by an Elastic Load Balancer (ELB). To enhance the system performance, a new Amazon Machine Image (AMI) was created and the ASG was configured to use the new AMI. However, after the production deployment, users complained of aberrations in the expected application functionality. A cross-check on the ELB has confirmed that all the instances are healthy and running as expected.

As a solutions architect, which option would you suggest to rectify these issues and guarantee that later deployments are successful?

- A. Configure the ASG to use Elastic Load Balancing (ELB) health checks in place of EC2 status checks
- B. Configure the ASG to use multiple Availability Zones. When an instance becomes unhealthy, the ASG maintains the desired capacity by distributing instances across these Availability Zones. This configuration helps in better application availability and reduces errors cropping from network connectivity issues
- C. Configure the ASG to a maximum capacity of 3 times the actual needed size. With this configuration, the ASG will terminate unhealthy instances and launch new ones quickly to maintain an optimum number of instances to meet user requirements
- **D. Create a new ASG launch configuration that uses the newly created AMI. Double the size of the ASG and allow the new instances to become healthy and then reduce the ASG back to the original size. If the new instances do not work as expected, associate the ASG with the old launch configuration** ✅

### Explanation

Correct option:

Create a new ASG launch configuration that uses the newly created AMI. Double the size of the ASG and allow the new instances to become healthy and then reduce the ASG back to the original size. If the new instances do not work as expected, associate the ASG with the old launch configuration

A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances. When you create a launch configuration, you specify information for the instances. Include the ID of the Amazon Machine Image (AMI), the instance type, a key pair, one or more security groups, and a block device mapping. If you've launched an EC2 instance before, you specified the same information to launch the instance.

You can specify your launch configuration with multiple Auto Scaling groups. However, you can only specify one launch configuration for an Auto Scaling group at a time, and you can't modify a launch configuration after you've created it. To change the launch configuration for an Auto Scaling group, you must create a launch configuration and then update your Auto Scaling group with it.

An Auto Scaling group is associated with one launch configuration at a time, and you can't modify a launch configuration after you've created it. To change the launch configuration for an Auto Scaling group, use an existing launch configuration as the basis for a new launch configuration. Then, update the Auto Scaling group to use the new launch configuration.

After you change the launch configuration for an Auto Scaling group, any new instances are launched using the new configuration options, but existing instances are not affected. To update the existing instances, terminate them so that they are replaced by your Auto Scaling group, or allow auto-scaling to gradually replace older instances with newer instances based on your termination policies. If you did not assign a specific termination policy to the group, Amazon EC2 Auto Scaling uses the default termination policy. It terminates the instances that were launched from the oldest launch template or launch configuration.


via - https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html

Incorrect options:

Configure the ASG to use Elastic Load Balancing (ELB) health checks in place of EC2 status checks - The default health checks for an Auto Scaling group are EC2 status checks only. To ensure that your Auto Scaling group can determine instance health based on additional load balancer tests, configure the Auto Scaling group to use Elastic Load Balancing (ELB) health checks. However, this change will not address the underlying issues for the given use case.

Configure the ASG to a maximum capacity of 3 times the actual needed size. With this configuration, the ASG will terminate unhealthy instances and launch new ones quickly to maintain an optimum number of instances to meet user requirements - This is false and given only as a distractor.

Configure the ASG to use multiple Availability Zones. When an instance becomes unhealthy, the ASG maintains the desired capacity by distributing instances across these Availability Zones. This configuration helps in better application availability and reduces errors cropping from network connectivity issues - When instances are launched, if you specified multiple Availability Zones, the desired capacity is distributed across these Availability Zones. If a scaling action occurs, Amazon EC2 Auto Scaling automatically maintains balance across all of the Availability Zones that you specify. This option is a distractor and will not address the underlying issues for the given use case.

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/change-launch-config.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-group-replacing-instances.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-elb-healthcheck.html

---

## Question 75

**Category:** CSAP – Accelerate Workload Migration and Modernization

An e-commerce company manages its flagship application on a load-balanced EC2 instance fleet for web hosting, database API services, and business logic. This tightly coupled architecture makes it inflexible for new feature additions while also making the architecture less scalable.

Which of the following options can be used to decouple the architecture, improve scalability and provide the ability to track the failed orders?

- **A. Configure Amazon S3 for hosting the web application while using AWS AppSync for database access services. Use Amazon Simple Queue Service (Amazon SQS) for queuing orders and AWS Lambda for business logic. Use Amazon SQS dead-letter queue for tracking and re-processing failed orders** ✅
- B. Use AWS Elastic Beanstalk for hosting the web application and Amazon API Gateway for database API services. Use Kinesis Data Streams for queuing orders and AWS Lambda to build business logic. Configure an Amazon S3 bucket for retaining failed orders on an hourly basis
- C. Configure Amazon CloudFront for hosting the website and Amazon API Gateway for database API services. Use Amazon Simple Queue Service (Amazon SQS) for order queuing and AWS Lambda for business logic. Use Amazon SQS long polling for retaining failed orders
- D. Use Amazon Lightsail for web hosting with AWS AppSync for database API services. Use Simple Queue Service (Amazon SQS) for order queuing. Use Amazon Elastic Container Service (Amazon ECS) for business logic and use the visibility timeout parameter of Amazon SQS to retain the failed orders

### Explanation

Correct option:

Configure Amazon S3 for hosting the web application while using AWS AppSync for database access services. Use Amazon Simple Queue Service (Amazon SQS) for queuing orders and AWS Lambda for business logic. Use Amazon SQS dead-letter queue for tracking and re-processing failed orders

Amazon S3 can be configured to host a web application.

AWS AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint to securely query, update, or publish data. AWS AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint to securely query, update, or publish data.

How AWS AppSync works:

via - https://aws.amazon.com/appsync/

Amazon SQS supports dead-letter queues (DLQ), which other queues (source queues) can target for messages that can't be processed (consumed) successfully. Dead-letter queues are useful for debugging your application or messaging system because they let you isolate unconsumed messages to determine why their processing doesn't succeed.

SQS dead-letter queues:

via - https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html

Incorrect options:

Configure Amazon CloudFront for hosting the website and Amazon API Gateway for database API services. Use Amazon Simple Queue Service (Amazon SQS) for order queuing and AWS Lambda for business logic. Use Amazon SQS long polling for retaining failed orders - You cannot use Amazon CloudFront for hosting a website as the website is hosted on the Cloudfront distribution's underlying origin (such as S3 or an EC2 instance). You cannot use Amazon SQS long polling for retaining failed orders. When the wait time for the ReceiveMessage API action is greater than 0, long polling is in effect. Long polling helps reduce the cost of using Amazon SQS by eliminating the number of empty responses and false empty responses. Long polling is a configurable parameter of SQS queues and not a temporary storage space to hold failed orders.

Use Amazon Lightsail for web hosting with AWS AppSync for database API services. Use Simple Queue Service (Amazon SQS) for order queuing. Use Amazon Elastic Container Service (Amazon ECS) for business logic and use the visibility timeout parameter of Amazon SQS to retain the failed orders - You cannot use the visibility timeout parameter of Amazon SQS to retain the failed orders. Immediately after a message is received in an SQS queue, it remains in the queue. To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout, a period during which Amazon SQS prevents other consumers from receiving and processing the message. Visibility timeout is a configurable parameter of SQS queues and not a temporary storage space to hold failed orders.

Use AWS Elastic Beanstalk for hosting the web application and Amazon API Gateway for database API services. Use Kinesis Data Streams for queuing orders and AWS Lambda to build business logic. Configure an Amazon S3 bucket for retaining failed orders on an hourly basis - Amazon Kinesis Streams allows real-time processing of streaming big data and the ability to read and replay records to multiple Amazon Kinesis Applications. Amazon SQS offers a reliable, highly-scalable hosted queue for storing messages as they travel between applications or microservices. It moves data between distributed application components and helps you decouple these components.

You should not use S3 to retain failed orders on an hourly basis. This would result in too many small objects (1 object for each failed order) on S3 which need to be written and read multiple times. In addition, it would be cumbersome to keep track of the failed orders and do the root cause analysis. You could run SQL queries via Athena on this underlying data in S3. However, it would turn out to be costly and inefficient while querying small objects via Athena. Therefore, this use case is an anti-pattern for S3.

References:

https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html

https://aws.amazon.com/appsync/

https://aws.amazon.com/sqs/faqs/

https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/

https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html

---
