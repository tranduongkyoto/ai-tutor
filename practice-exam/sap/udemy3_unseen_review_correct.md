# Udemy Test #3 — unseen questions (Gate 1) — Correct Answer Review (19 questions)

Source: `udemy3_unseen_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/⚠️/🧠 are study notes. Wrong answers: `udemy3_unseen_review.md`.

## Purpose

Confirm each correct answer was **knowledge, not a guess**. Answer again without looking; if you can't justify why every wrong option fails, tick **Guessed** and treat it as a wrong answer.

## ⚠️ Inconsistent concepts (right here, wrong elsewhere in this test)

| Right | Wrong | Concept |
|---|---|---|
| Q13 | Q14 | Flow Logs fit metadata (rejects) but not packet inspection → Traffic Mirroring |
| Q22 | Q26 | Global Accelerator: knew NLB-for-static-IP, missed custom routing accelerator |
| Q17 | Q21 | Edge/DNS mechanics: custom-header origin protection right, private-zone health checks missed |

These are partial knowledge — review each pair together.

## Tracker

| Group | Q | Guessed? | Pass 1 | Pass 2 |
|---|---|---|---|---|
| A | [Q4](#q4) | ☐ | ☐ | ☐ |
| A | [Q6](#q6) | ☐ | ☐ | ☐ |
| A | [Q10](#q10) | ☐ | ☐ | ☐ |
| A | [Q15](#q15) | ☐ | ☐ | ☐ |
| A | [Q27](#q27) | ☐ | ☐ | ☐ |
| B | [Q1](#q1) | ☐ | ☐ | ☐ |
| B | [Q2](#q2) | ☐ | ☐ | ☐ |
| B | [Q12](#q12) | ☐ | ☐ | ☐ |
| B | [Q13](#q13) | ☐ | ☐ | ☐ |
| B | [Q24](#q24) | ☐ | ☐ | ☐ |
| C | [Q5](#q5) | ☐ | ☐ | ☐ |
| C | [Q8](#q8) | ☐ | ☐ | ☐ |
| C | [Q19](#q19) | ☐ | ☐ | ☐ |
| D | [Q7](#q7) | ☐ | ☐ | ☐ |
| D | [Q17](#q17) | ☐ | ☐ | ☐ |
| D | [Q18](#q18) | ☐ | ☐ | ☐ |
| D | [Q20](#q20) | ☐ | ☐ | ☐ |
| D | [Q22](#q22) | ☐ | ☐ | ☐ |
| D | [Q23](#q23) | ☐ | ☐ | ☐ |

---

# Group A — Integration & streaming (5)

<a id="q4"></a>

## Q4

A solutions architect at a retail company has set up a workflow to ingest the clickstream data into the raw zone of the S3 data lake. The architect wants to run some SQL-based data sanity checks on the raw zone of the data lake.

What AWS services would you suggest for this requirement such that the solution is cost-effective and easy to maintain?

- **A.** Use Athena to run SQL based analytics against S3 data
- **B.** Load the incremental raw zone data into Redshift on an hourly basis and run the SQL based sanity checks
- **C.** Load the incremental raw zone data into RDS on an hourly basis and run the SQL based sanity checks
- **D.** Load the incremental raw zone data into an EMR based Spark Cluster on an hourly basis and use SparkSQL to run the SQL based sanity checks

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** SQL sanity checks on S3 raw zone, cheap

⚠️ **Watch:** loading into Redshift/EMR = overbuilt

🧠 **Rule:** Ad-hoc SQL on S3 → Athena

### TD explanation

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

</details>

<a id="q6"></a>

## Q6

A social gaming company is developing a mobile game that streams score updates to a backend processor and then publishes results on a leaderboard. The company has hired you to design a solution that can handle major traffic spikes, process the mobile game updates in the order of receipt, and store the processed updates in a highly available database. The company wants to minimize the management overhead required to maintain the solution.

Which of the following solutions will you recommend to meet these requirements?

- **A.** Send score updates to Kinesis Data Streams which uses a Lambda function to process these updates and then store these processed updates in DynamoDB
- **B.** Send score updates to Kinesis Data Streams which uses a fleet of EC2 instances (with Auto Scaling) to process the updates in Kinesis Data Streams and then store these processed updates in DynamoDB
- **C.** Send score updates to an SQS queue which uses a fleet of EC2 instances (with Auto Scaling) to process these updates in the SQS queue and then store these processed updates in an RDS MySQL database
- **D.** Send score updates to an SNS topic, subscribe a Lambda function to this SNS topic to process the updates and then store these processed updates in a SQL database running on Amazon EC2

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** ordered, spikes, minimal ops

⚠️ **Watch:** EC2 consumers = more ops

🧠 **Rule:** Ordered stream + serverless → KDS + Lambda + DynamoDB

### TD explanation

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

</details>

<a id="q10"></a>

## Q10

A weather monitoring agency stores and manages the global weather data for the last 50 years. The data has a velocity of 1GB per minute. You would like to store the data with only the most relevant attributes to build a predictive model for weather patterns.

Which of the following solutions would you use to build the most cost-effective solution with the LEAST amount of infrastructure maintenance?

- **A.** Capture the data in Kinesis Data Streams and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3
- **B.** Capture the data in a Spark Streaming Cluster on EMR use Spark Streaming transformations before writing to S3
- **C.** Capture the data in Kinesis Data Analytics and use SQL queries to filter and transform the data before writing to S3
- **D.** Capture the data in Kinesis Data Firehose and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** 1 GB/min, filter attributes, least maintenance

⚠️ **Watch:** KDS needs shard mgmt

🧠 **Rule:** Transform-and-land → Firehose + Lambda transform → S3

### TD explanation

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

</details>

<a id="q15"></a>

## Q15

A payment service provider company has a legacy application built on high throughput and resilient queueing system to send messages to the customers. The implementation relied on a manually-managed RabbitMQ cluster and consumers. The system was able to process a large load of messages within a reasonable delivery time. The cluster and consumers were both deployed on Amazon Elastic Compute Cloud (Amazon EC2) instances. However, when the messages in the queue piled up due to network failures on the customer side, the latency of the overall flow was affected, resulting in a breach of the service level agreement (SLA). The development team had to manually scale the queues to resolve the issue. Also, while doing manual upgrades on RabbitMQ and the hosting operating system, the company faced downtimes.

The company is growing and has to maintain a strict delivery time SLA. The company is now looking for a serverless solution for its messaging queues. The queue functions of handling concurrency, message delays and retries, maintaining message order, secure delivery, and scalability are needed in the proposed solution architecture.

Which of the following would you propose for a cost-effective solution for the requirement?

- **A.** Design a cost-effective, serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Classic
- **B.** Design the serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Fargate. To save costs, run the Amazon SQS FIFO queues and Amazon ECS Fargate tasks only when needed
- **C.** Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Fargate. To save costs, run the Amazon MQ for RabbitMQ queues and Amazon ECS Fargate tasks only when needed
- **D.** Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Classic

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** serverless queue, ordering, retries

⚠️ **Watch:** Amazon MQ isn't serverless

🧠 **Rule:** Serverless ordered queue → SQS FIFO + Fargate

### TD explanation

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

</details>

<a id="q27"></a>

## Q27

An investment firm collects daily stock trading data from exchanges and stores it in a data warehouse. The development team at the firm needs a solution that streams data directly into the data repository but should also allow SQL-based data modifications when needed. The solution should facilitate complex analytical queries that execute in the fastest possible time. The solution should also offer a business intelligence dashboard that highlights any stock price anomalies.

Which of the following options represents the best solution for the given use case?

- **A.** Configure Amazon Kinesis Data Streams to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source
- **B.** Configure Amazon Kinesis Data Streams to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source
- **C.** Configure Amazon Kinesis Data Firehose to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source
- **D.** Configure Amazon Kinesis Data Firehose to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** stream into DW, SQL modify, fast analytics, BI

⚠️ **Watch:** KDS can't deliver directly to Redshift

🧠 **Rule:** Firehose → Redshift → QuickSight

### TD explanation

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

</details>

---

# Group B — Ops, security & monitoring (5)

<a id="q1"></a>

## Q1

A web application is running on a fleet of Amazon EC2 instances that are configured to operate in an Auto Scaling group (ASG). The instances are fronted by an Elastic Load Balancer (ELB). To enhance the system performance, a new Amazon Machine Image (AMI) was created and the ASG was configured to use the new AMI. However, after the production deployment, users complained of aberrations in the expected application functionality. A cross-check on the ELB has confirmed that all the instances are healthy and running as expected.

As a solutions architect, which option would you suggest to rectify these issues and guarantee that later deployments are successful?

- **A.** Configure the ASG to use Elastic Load Balancing (ELB) health checks in place of EC2 status checks
- **B.** Configure the ASG to use multiple Availability Zones. When an instance becomes unhealthy, the ASG maintains the desired capacity by distributing instances across these Availability Zones. This configuration helps in better application availability and reduces errors cropping from network connectivity issues
- **C.** Configure the ASG to a maximum capacity of 3 times the actual needed size. With this configuration, the ASG will terminate unhealthy instances and launch new ones quickly to maintain an optimum number of instances to meet user requirements
- **D.** Create a new ASG launch configuration that uses the newly created AMI. Double the size of the ASG and allow the new instances to become healthy and then reduce the ASG back to the original size. If the new instances do not work as expected, associate the ASG with the old launch configuration

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** new AMI broke app, ELB says healthy

⚠️ **Watch:** ELB health checks wouldn't catch functional bugs

🧠 **Rule:** Safe AMI rollout → new launch config, double ASG, roll back to old config if bad

### TD explanation

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

</details>

<a id="q2"></a>

## Q2

An e-commerce company has a three-tier web application with separate subnets for Web, Application and Database tiers. The CTO at the company wants to monitor any malicious activity targeting the web application running on EC2 instances. As a solutions architect, you have been tasked with developing a solution to notify the security team in case the network exposure of EC2 instances on specific ports violates the security policies of the company.

Which AWS Services would you use to build an automated notification system to meet these requirements with the least development effort? (Select two)

- **A.** AWS Shield
- **B.** VPC Flow Logs
- **C.** Amazon SNS
- **D.** Amazon Inspector
- **E.** Amazon CloudWatch

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D (you answered correctly)

🔑 **Key words:** network exposure on ports violates policy → notify

⚠️ **Watch:** Shield/Flow Logs don't assess exposure

🧠 **Rule:** Network reachability findings → Inspector + SNS

### TD explanation

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

</details>

<a id="q12"></a>

## Q12

A web application is hosted on Amazon EC2 instances that are fronted by Application Load Balancer (ALB) configured with an Auto Scaling group (ASG). Enhanced security is provided to the ALB by AWS WAF web ACLs. As per the company's security policy, AWS CloudTrail is activated and logs are configured to be stored on Amazon S3 and CloudWatch Logs.

A holiday sales offer was run on the application for a week. The development team has noticed that a few of the instances have rebooted taking down the log files and all temporary data with them. Initial analysis has confirmed that the incident took place during off-peak hours. Even though the incident did not cause any sales or revenue loss, the CTO has asked the development team to fix the security error that has allowed the incident to go unnoticed and eventually untraceable.

Which of the following steps will you implement to permanently record all traffic coming into the application?

- **A.** Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking
- **B.** To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring
- **C.** Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting
- **D.** Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** record all traffic into WAF-fronted ALB

⚠️ **Watch:** CloudTrail isn't a WAF destination

🧠 **Rule:** WAF logs → Firehose → S3 → Athena

### TD explanation

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

</details>

<a id="q13"></a>

## Q13

A retail company is deploying a critical application on multiple EC2 instances in a VPC. Per the company policy, any failed client connections to the EC2 instances must be logged.

Which of the following options would you recommend as the MOST cost-effective solution to address these requirements?

- **A.** Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to a Kinesis Data Firehose stream with the data delivery to an S3 bucket
- **B.** Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to Kinesis Data Streams with the data delivery to an S3 bucket
- **C.** Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to CloudWatch Logs
- **D.** Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to Amazon CloudWatch Logs

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** log failed connections, cheapest

⚠️ **Watch:** Kinesis/new VPC = overbuilt

🧠 **Rule:** Rejected traffic → ENI Flow Logs (REJECT filter) → CloudWatch Logs

### TD explanation

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

</details>

<a id="q24"></a>

## Q24

A financial services firm intends to migrate its IT operations to AWS. The security team is establishing a framework to ensure that AWS best practices are being followed. AWS management console is the only way used by the IT teams to provision AWS resources. As per the firm's compliance requirements, the AWS resources need to be maintained in a particular configuration and audited regularly for unauthorized changes.

As an AWS Certified Solutions Architect Professional, how will you implement this requirement? (Select two)

- **A.** Leverage Systems Manager to view and control your infrastructure on AWS, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS infrastructure. Use SNS topics to enable notifications and improve the response time of incident responses
- **B.** Leverage CloudWatch Logs agent to aggregate all the AWS SDK logs. Analyze the log data using a pre-defined set of filter patterns that match any changes in the API calls. Trigger notifications via Amazon CloudWatch alarms when unintended changes are performed
- **C.** Leverage AWS Config rules for auditing changes to AWS resources periodically and monitor the compliance of the configuration. Set up AWS Config custom rules using AWS Lambda to create a test-driven development approach, and finally automate the evaluation of configuration changes against the required controls
- **D.** Leverage EventBridge events to monitor and evaluate system events patterns, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS resources. Use SNS topics to enable notifications and improve the response time of incident responses
- **E.** Leverage AWS CloudTrail events to review management activities of all AWS accounts. Make sure that CloudTrail is enabled in all accounts for the available AWS services. Enable CloudTrail trails and encrypt CloudTrail event log files with an AWS KMS key and monitor the recorded events via CloudWatch Logs

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E (you answered correctly)

🔑 **Key words:** configs audited for unauthorized change

⚠️ **Watch:** auto-revert via SSM/EventBridge not required

🧠 **Rule:** Config rules + CloudTrail→CloudWatch Logs (KMS)

### TD explanation

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

</details>

---

# Group C — Migration & cost (3)

<a id="q5"></a>

## Q5

A company wants to migrate its on-premises resources to AWS. The IT environment consists of 200 virtual machines (VMs) with a combined storage capacity of 50 TB. While the majority of VMs may be taken down for migration since they are only used during business hours, others are mission-critical, so the downtime must be minimized. The on-premises network engineer has allocated 10 Mbps of internet bandwidth for the migration. The capacity of the on-premises network has peaked and increasing it would be prohibitively expensive.

You have been hired as an AWS Certified Solutions Architect Professional to develop a migration strategy that can be implemented in the next three months. Which of the following would you recommend?

- **A.** Export the VMs locally, starting with the most mission-critical servers first. Configure a 1.25 Gbps AWS site-to-site VPN to securely upload each VM to Amazon S3 after they are exported. Use VM Import/Export to import the VMs into Amazon EC2
- **B.** Migrate mission-critical VMs using AWS Application Migration Service (MGN). Export the other VMs locally and transfer them to Amazon S3 using AWS Snowball Edge. Leverage VM Import/Export to import the VMs into Amazon EC2
- **C.** Leverage AWS Migration Hub to analyze each application for further refactoring and optimizations using AWS services or AWS Marketplace solutions
- **D.** Create a 10 Gbps AWS Direct Connect connection and then configure a private virtual interface. Leverage AWS Server Migration Service (SMS) to migrate the VMs into Amazon EC2

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** 50 TB, 10 Mbps, some VMs mission-critical

⚠️ **Watch:** network too slow for bulk

🧠 **Rule:** Critical VMs → MGN; bulk → Snowball + VM Import

### TD explanation

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

</details>

<a id="q8"></a>

## Q8

An on-premises data center, set up a decade ago, hosts all the applications of a business. The business now wants to move to AWS Cloud. The documentation of these systems is outdated and complete knowledge of all existing workloads is absent. The data center hosts a mix of Windows and Linux virtual machines.

As a solutions architect, you need to provide a plan to migrate all the applications to the cloud. How will you gather the necessary data of the existing machines?

- **A.** Register the on-premises VMs with the AWS Migration Hub to collect configuration and utilization data
- **B.** Deploy the AWS Server Migration Service (AWS SMS) connector using the OVA image on the VMware cluster to collect configuration and utilization data from the VMs
- **C.** Install the AWS Application Discovery Service on each of the VMs to collect the configuration and utilization data
- **D.** Use the AWS Migration Portfolio Assessment (MPA) tool to connect to each of the VMs to collect the configuration and utilization data

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** unknown estate, Windows+Linux VMs

⚠️ **Watch:** SMS/MPA don't discover

🧠 **Rule:** Discovery → Application Discovery Service agents

### TD explanation

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

</details>

<a id="q19"></a>

## Q19

A company has hired you as an AWS Certified Solutions Architect Professional to develop a deployment plan for its flagship application deployed on EC2 instances across multiple Availability Zones in the us-east-1 Region. Your solution must meet these constraints:

1) A 300 GB static dataset must be available to the application before it can be started

2) The application layer must scale on-demand with the least amount of starting time possible

3) The development team must be able to change the code multiple times in a day

4) Any patches for critical operating systems (OS) must be applied within 24 hours of release

Which of the following represents the best solution for this requirement?

- **A.** Leverage an Amazon-provided AMI for the OS and set up an Auto Scaling group to scale with traffic. Replace existing instances after each updated Amazon-provided AMI release. Use AWS CodeDeploy to push the application code to the instances. Configure an Amazon EC2 user data script to download the static dataset from Amazon S3
- **B.** Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Configure an Amazon EC2 user data script to download the static dataset from Amazon S3
- **C.** Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Store and access the static dataset using Amazon EFS
- **D.** Leverage AWS Systems Manager to create and maintain a new AMI with the OS patches updated on an ongoing basis. Configure the Auto Scaling group to use the patched AMI and replace existing unpatched instances. Use AWS CodeDeploy to push the application code to the instances. Store and access the static dataset using Amazon EBS

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** 300 GB dataset ready before start, fast scale

⚠️ **Watch:** S3 download in user data = slow start

🧠 **Rule:** Shared static dataset across ASG → EFS; patched AMI via SSM

### TD explanation

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

</details>

---

# Group D — Edge & networking (6)

<a id="q7"></a>

## Q7

A supply-chain manufacturing company manages its AWS resources in an Elastic Beanstalk environment. For implementing a new security requirement, the company needs to assign a single static IP address to a load-balanced Elastic Beanstalk environment. Subsequently, this IP address will be used to uniquely identify traffic coming from the Elastic Beanstalk environment.

As a solutions architect, which of the following would you recommend as the BEST solution that requires minimal maintenance?

- **A.** Use a Bastion host to map multiple IP addresses into a single publicly exposed IP address
- **B.** Use a Network Address Translation (NAT) instance to map multiple IP addresses into a single publicly exposed IP address
- **C.** Use a Network Address Translation (NAT) gateway to map multiple IP addresses into a single publicly exposed IP address
- **D.** Attach the same Elastic IP to all instances to obtain a single publicly exposed IP address

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** single static outbound IP for Beanstalk

⚠️ **Watch:** NAT instance = maintenance

🧠 **Rule:** Static egress IP → NAT Gateway with EIP

### TD explanation

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

</details>

<a id="q17"></a>

## Q17

A development team is designing a system on AWS that will leverage Amazon CloudFront for content caching and for protecting the underlying origin. The team has flagged a concern regarding a probable attack on the origin server IP addresses, despite it being served by CloudFront.

As an AWS Certified Solutions Architect Professional, which of the following would you recommend as the BEST solution for providing the strongest level of protection to the origin server?

- **A.** Configure an AWS Lambda@Edge function to validate that the traffic to the Application Load Balancer originates from CloudFront
- **B.** Configure private access to content by using special CloudFront signed URLs or signed cookies
- **C.** Configure Origin Access Identity(OAI) on the origin server, which will only allow requests originating from CloudFront
- **D.** Configure CloudFront to use a custom header and configure an AWS WAF rule on the origin’s Application Load Balancer to accept only traffic that contains that header

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** protect ALB origin behind CloudFront

⚠️ **Watch:** OAI only for S3 origins

🧠 **Rule:** Custom origin protection → CloudFront custom header + WAF rule on ALB

### TD explanation

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

</details>

<a id="q18"></a>

## Q18

A company has an Elastic Load Balancer (ELB) that is configured with an Auto Scaling Group (ASG) having a minimum of 4, a maximum of 10, and the desired value of 4 instances. The ASG cooldown and the termination policies are configured to the default values. Monitoring reports indicate a general usage requirement of 4 instances, while any traffic spikes result in an additional 10 instances. Customers have been complaining of request timeouts and partially loaded pages.

As an AWS Certified Solutions Architect Professional, which of the following options will you suggest to fix this issue?

- **A.** Enable Sticky Sessions on ELB
- **B.** Configure termination policies on ASG to determine which instances it terminates first during scale-in events
- **C.** Add a lifecycle hook on scale-out event to your ASG, making sure that the instance is fully ready before it starts receiving traffic
- **D.** Configure connection draining on ELB

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** timeouts, partial pages on scale-in

⚠️ **Watch:** lifecycle hook is for scale-out readiness

🧠 **Rule:** In-flight requests on scale-in → connection draining (deregistration delay)

### TD explanation

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

</details>

<a id="q20"></a>

## Q20

An e-commerce company runs its flagship website on its on-premises Linux servers. Recently, the company suffered outages after announcing huge discounts on its website. The web tier of the application is fronted by Elastic Load Balancer while the database tier is built on RDS MYSQL database. The company is planning to run heavy discounts for the upcoming holiday sales season. The company is looking for a solution to avoid any similar outages as well as quickly ramp up the ability to handle huge traffic spikes.

As an AWS Certified Solutions Architect Professional, which of the following would you suggest as the most optimal solution that can enhance the application's capabilities to handle the sudden spikes in user traffic without significant development effort?

- **A.** Create a CloudFront distribution and configure CloudFront to cache objects from a custom origin. This will offload some traffic from the on-premises servers. Customize CloudFront cache behavior by setting Time To Live (TTL) to suit your business requirement
- **B.** Change the application architecture to use Docker containers and redeploy on AWS with ECS
- **C.** Create an S3 bucket and configure it for website hosting. Migrate your DNS to Route53 and leverage Route53 DNS failover to failover to the S3 hosted website
- **D.** Lift and Shift the application using AWS Elastic Beanstalk to enhance the scalability of the application without any downtime on the existing one

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** on-prem spikes, little dev effort

⚠️ **Watch:** re-platforming = effort

🧠 **Rule:** Offload on-prem spikes quickly → CloudFront custom origin

### TD explanation

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

</details>

<a id="q22"></a>

## Q22

A web application is hosted on a fleet of Amazon EC2 instances running behind an Application Load Balancer (ALB). A custom functionality has mandated the need for a static IP address for the ALB.

As a solutions architect, how will you implement this requirement while keeping the costs to a minimum?

- **A.** Configure Gateway Load Balancer in front of the Application Load Balancer to provide a static IP address for the ALB
- **B.** An Elastic IP can be registered to an Application Load Balancer only during the creation. Re-create the ALB with the new Elastic IP and switch the workload to the newly created ALB
- **C.** Register the Application Load Balancer behind a Network Load Balancer that will provide the necessary static IP address to the ALB
- **D.** Configure Global Accelerator in front of the Application Load Balancer to provide a static IP address for the ALB

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** static IP for ALB, cheapest

⚠️ **Watch:** Global Accelerator costs more

🧠 **Rule:** Static IP for ALB → NLB in front (ALB-type target)

### TD explanation

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

</details>

<a id="q23"></a>

## Q23

A media company has its users accessing the content from different platforms including mobile, tablet, and desktop. Each platform is customized to provide a different user experience based on various viewing modes. Path-based headers are used to serve the content for different platforms, hosted on different Amazon EC2 instances. An Auto Scaling group (ASG) has also been configured for the EC2 instances to ensure that the solution is highly scalable.

Which of the following combination of services can help minimize the cost while maximizing the performance? (Select two)

- **A.** Network Load Balancer
- **B.** Amazon Route 53 with traffic flow policies
- **C.** Application Load Balancer
- **D.** Amazon S3 configured as a static website
- **E.** Amazon CloudFront with Lambda@Edge

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E (you answered correctly)

🔑 **Key words:** per-device content via path headers, cost + performance

⚠️ **Watch:** NLB has no L7 routing

🧠 **Rule:** Device-aware edge + L7 routing → CloudFront + Lambda@Edge + ALB

### TD explanation

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

</details>
