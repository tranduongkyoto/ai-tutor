# Udemy Practice Test #1 — unseen questions — source (TD layout)

## Question 13

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

## Question 23

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

## Question 4

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

## Question 5

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

## Question 19

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
