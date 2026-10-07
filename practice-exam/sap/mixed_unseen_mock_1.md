# Mixed Unseen Mock #1 — SAP-C02 (Gate 1)

**75 questions · 210 minutes (ESL +30) · no notes · multi-select = all-or-nothing**

Answer sheet format (send back as text): `1:A, 2:BD, 3:C, …` — mark guesses with `?` (e.g. `7:B?`) and flagged ones with `!`.

---

## Q1

An analytics company wants to leverage ElastiCache for Redis in cluster mode to enhance the performance and scalability of its existing two-tier application architecture. The ElastiCache cluster is configured to listen on port 6379. The company has hired you as an AWS Certified Solutions Architect Professional to build a secure solution so that the cache data is secure and protected from unauthorized access.

Which of the following steps would address the given use-case? (Select three)

- **A.** Configure the security group for the ElastiCache cluster with the required rules to allow inbound traffic from the cluster itself as well as from the cluster's clients on port 6379
- **B.** Configure the ElastiCache cluster to have both in-transit as well as at-rest encryption
- **C.** Enable CloudTrail to monitor the API Calls for the ElastiCache cluster
- **D.** Enable CloudWatch Logs to monitor the security credentials for the ElastiCache cluster
- **E.** Configure the security group for the ElastiCache cluster with the required rules to allow outbound traffic to the cluster's clients on port 6379
- **F.** Create the cluster with auth-token parameter and make sure that the parameter is included in all subsequent commands to the cluster

---

## Q2

A research company specializing in agricultural innovation operates a fleet of IoT devices across experimental farms to automate and monitor water distribution, temperature regulation, and humidity control. The collected telemetry data is stored in Optimized Row Columnar (ORC) format within the Hadoop Distributed File System (HDFS), running on a persistent Amazon EMR cluster. The company’s data analytics team runs SQL queries using Apache Presto on the same always-on EMR environment. These queries scan large datasets, complete within 15 minutes, and are executed only between 6 PM and 2 AM as part of the company’s nightly analysis routine.
With cloud costs climbing, the research company’s leadership seeks a more cost-effective solution to support these recurring SQL-based data queries. A solutions architect must recommend the most economical approach while maintaining query performance and compatibility with the existing ORC data format.
What is the most cost-effective recommendation that the solutions architect can make?

- **A.** Persist data in Amazon S3, and execute SQL-based analytics through Amazon Athena, using schema definitions stored in the AWS Glue Data Catalog.
- **B.** Load your datasets into Amazon Redshift and perform analytics directly within the Redshift data warehouse environment.
- **C.** Use AWS Glue ETL jobs to ingest the ORC files into Amazon Aurora and enable SQL-based querying.
- **D.** Use AWS Lambda functions to convert the ORC files into JSON and store them in Amazon DynamoDB for querying.

---

## Q3

A legacy web application runs 24/7 and it is currently hosted on an on-premises server with an outdated version of the Operating System (OS). The OS support will end soon and the team wants to expedite migration to an Amazon EC2 instance with an updated version of the OS. The application also references 90 TB of static data in the form of images that need to be moved to AWS.

How should this be accomplished most cost-effectively?

- **A.** Use AWS Application Migration Service to migrate the application and all its data to Amazon EC2 instance
- **B.** Replatform the server to Amazon EC2 while choosing an AMI of your choice to cater to the OS requirements. Use AWS Snowball to transfer the image data to Amazon S3
- **C.** Set up the application on AWS Fargate for a serverless solution and use AWS Snowball to transfer the image data to Amazon S3
- **D.** Use AWS Direct Connect to establish a dedicated connection between on-premises systems and AWS. Transfer data to Amazon S3 using this link. Migrate the application to Amazon EC2 instance

---

## Q4

A social media company has a serverless application stack that consists of CloudFront, API Gateway and Lambda functions. The company has hired you as an AWS Certified Solutions Architect Professional to improve the current deployment process which creates a new version of the Lambda function and then runs an AWS CLI script for deployment. In case the new version errors out, then another CLI script is invoked to deploy the previous working version of the Lambda function. The company has mandated you to decrease the time to deploy new versions of the Lambda functions and also reduce the time to detect and rollback when errors are identified.

Which of the following solutions would you suggest for the given use-case?

- **A.** Set up and deploy a CloudFormation stack containing a new API Gateway endpoint that points to the new Lambda version. Test the updated CloudFront origin that points to this new API Gateway endpoint and in case errors are detected then revert the CloudFront origin to the previous working API Gateway endpoint
- **B.** Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. Use pre-traffic and post-traffic test functions of the change set to verify the deployment. Rollback in case CloudWatch alarms are triggered
- **C.** Use Serverless Application Model (SAM) and leverage the built-in traffic-shifting feature of SAM to deploy the new Lambda version via CodeDeploy and use pre-traffic and post-traffic test functions to verify code. Rollback in case CloudWatch alarms are triggered
- **D.** Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. In case the Lambda function errors out, rollback the CloudFormation change set to the previous version

---

## Q5

A retail company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for managing a serverless application that consists of multiple API gateways, Lambda functions, S3 buckets and DynamoDB tables. The company is getting reports from customers that some of the application components seem to be lagging while loading dynamic images and some are timing out with the "504 Gateway Timeout" error. As part of your investigations to identify the root cause behind this issue, you can confirm that DynamoDB monitoring metrics are at acceptable levels.

Which of the following steps would you recommend to address these application issues? (Select two)

- **A.** Process and analyze the VPC Flow Logs to determine if there is packet loss between the Lambda function and S3
- **B.** Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals
- **C.** Enable execution logging for the API Gateway. Process and analyze the execution logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **D.** Enable access logging for the API Gateway. Process and analyze the access logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **E.** Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors

---

## Q6

An e-commerce web application is hosted on Amazon EC2 instances that are fronted by Application Load Balancer (ALB) configured with an Auto Scaling group (ASG). Enhanced security is provided to the ALB by AWS WAF web ACLs. As per the company's security policy, AWS CloudTrail is activated and logs are configured to be stored on Amazon S3 and CloudWatch Logs.

A discount sales offer was run on the application for a week. The support team has noticed that a few of the instances have rebooted taking down the log files and all temporary data with them. Initial analysis has confirmed that the incident took place during off-peak hours. Even though the incident did not cause any sales or revenue loss, the CTO has asked the security team to fix the security error that has allowed the incident to go unnoticed and eventually untraceable.

What steps will you implement to permanently record all traffic coming into the application?

- **A.** To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring
- **B.** Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking
- **C.** Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking
- **D.** Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting

---

## Q7

A data analytics company needs to set up a data lake on Amazon S3 for a financial services client. The data lake is split in raw and curated zones. For compliance reasons, the source data needs to be kept for a minimum of 5 years. The source data arrives in the raw zone and is then processed via an AWS Glue based ETL job into the curated zone. The business analysts run ad-hoc queries only on the data in the curated zone using Athena. The team is concerned about the cost of data storage in both the raw and curated zones as the data is increasing at a rate of 2 TB daily in each zone.

Which of the following options would you implement together as the MOST cost-optimal solution?
(Select two)

- **A.** Setup a lifecycle policy to transition the raw zone data into Glacier Deep Archive after 1 day of object creation
- **B.** Create a Lambda function based job to delete the raw zone data after 1 day
- **C.** Setup a lifecycle policy to transition the curated zone data into Glacier Deep Archive after 1 day of object creation
- **D.** Use Glue ETL job to write the transformed data in the curated zone using CSV format
- **E.** Use Glue ETL job to write the transformed data in the curated zone using a compressed file format

---

## Q8

A digital media company wants to use AWS Cloudfront to manage its content. Firstly, it would like to allow only those new users who have paid the annual subscription fee the ability to download the application installation file. Secondly, only the subscribers should be able to view the files in the members' area.

As a Solutions Architect Professional, which of the following would you recommend as the MOST optimal solutions to deliver restricted content to the bona fide end users? (Select two)

- **A.** Use CloudFront signed cookies to restrict access to all the files in the members' area of the website
- **B.** Use CloudFront signed URLs to restrict access to the application installation file
- **C.** Require HTTPS for communication between CloudFront and your S3 origin
- **D.** Use CloudFront signed cookies to restrict access to the application installation file
- **E.** Use CloudFront signed URLs to restrict access to all the files in the members' area of the website

---

## Q9

A global enterprise oversees at least six hundred AWS accounts via AWS Organizations. Recently, the governance team granted product owners the ability to configure Amazon S3 Access Points within the assigned accounts. These access points must be accessible only from within VPCs (Virtual Private Clouds), and any access from the Internet must be restricted.
What is the most operationally scalable and manageable approach to enforce this control efficiently across the organization?

- **A.** At the root level of the organization, implement a Service Control Policy (SCP) that blocks s3:CreateAccessPoint except if the s3:AccessPointNetworkOrigin is equal to VPC
- **B.** Modify the bucket’s resource policy to block any attempt to perform the s3:CreateAccessPoint operation, except when the s3:ResourceAccount condition is explicitly matched to VPC
- **C.** Use AWS Config rules combined with AWS Lambda to detect and revert S3 Access Points that are not restricted to VPC-only access
- **D.** Use an S3 Object ACL to block the creation of access points unless the request originates from a VPC by checking the s3:AccessPointNetworkOrigin condition

---

## Q10

A payment service provider company has a legacy application built on high throughput and resilient queueing system to send messages to the customers. The implementation relied on a manually-managed RabbitMQ cluster and consumers. The system was able to process a large load of messages within a reasonable delivery time. The cluster and consumers were both deployed on Amazon Elastic Compute Cloud (Amazon EC2) instances. However, when the messages in the queue piled up due to network failures on the customer side, the latency of the overall flow was affected, resulting in a breach of the service level agreement (SLA). The development team had to manually scale the queues to resolve the issue. Also, while doing manual upgrades on RabbitMQ and the hosting operating system, the company faced downtimes.

The company is growing and has to maintain a strict delivery time SLA. The company is now looking for a serverless solution for its messaging queues. The queue functions of handling concurrency, message delays and retries, maintaining message order, secure delivery, and scalability are needed in the proposed solution architecture.

Which of the following would you propose for a cost-effective solution for the requirement?

- **A.** Design a cost-effective, serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Classic
- **B.** Design the serverless architecture by use of Amazon Simple Queue Service (SQS) with Amazon ECS Fargate. To save costs, run the Amazon SQS FIFO queues and Amazon ECS Fargate tasks only when needed
- **C.** Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Fargate. To save costs, run the Amazon MQ for RabbitMQ queues and Amazon ECS Fargate tasks only when needed
- **D.** Design the serverless architecture by use of Amazon MQ for RabbitMQ with Amazon ECS Classic

---

## Q11

An international e-commerce company relies on Amazon CloudFront to deliver its multi-regional Amazon ECS-based web store with fast, scalable performance. Over recent months, customers around the globe have started reporting sluggish page load times, particularly during flash sales and heavy promotional events.
The performance reliability team has spotted a troubling pattern: CloudFront’s cache hit ratio has consistently decreased. Amazon CloudWatch metrics reveal the root cause: query strings in some request URLs are inconsistent. Parameter order shifts unpredictably, and values alternate between mixed-case and lowercase.
Which steps should be implemented to rapidly restore CloudFront’s cache hit/ratio with the least operational overhead and cost?

- **A.** Configure a CloudFront Function on the Viewer Request event that alphabetically sorts all query parameter keys and enforces lowercase for both parameter names and values
- **B.** Attach a Lambda@Edge handler to the CloudFront distribution’s Viewer Request event that alphabetically sorts each query string parameter and converts all names and values to lowercase to ensure consistent cache key generation
- **C.** Place a reverse proxy layer downstream of the load balancer to intercept incoming URLs and rewrite all query string characters to lowercase
- **D.** Modify the CloudFront distribution’s cache or origin-request policy to stop including query-string parameters in the cache key

---

## Q12

An e-commerce company is investigating user reports of its Java-based web application errors on the day of the Thanksgiving sale. The development team recovered the logs created by the EC2 instance-hosted web servers and reviewed Aurora DB cluster performance metrics. Some of the web servers were terminated before logs could be collected and the Aurora metrics were inadequate for query performance analysis.

Which of the following steps would you recommend to make the monitoring process more reliable to troubleshoot any future events due to traffic spikes? (Select three)

- **A.** Enable detailed monitoring for Amazon EC2 instances to send data points to CloudWatch every minute. Track the metric 'CPUUtilization' to know when the auto-scaling process can kick in
- **B.** Use CloudTrail and configure a trail to deliver Amazon Aurora query activity to an Amazon S3 bucket. Process and analyze these real-time log streams using Amazon Kinesis Data Streams
- **C.** Configure the Aurora MySQL DB cluster to publish slow query and error logs to Amazon CloudWatch Logs
- **D.** Enable Aurora lab mode which will then publish all logs and activity on Aurora DB to CloudWatch logs
- **E.** Set up the AWS X-Ray SDK to trace incoming HTTP requests on the EC2 instances as well as set up tracing of SQL queries with the X-Ray SDK for Java
- **F.** Install and configure an Amazon CloudWatch Logs agent on the EC2 instances to send the application logs to CloudWatch Logs

---

## Q13

A solutions architect at a retail company has configured a private hosted zone using Route 53. The architect needs to configure health checks for record sets within the private hosted zone that are associated with EC2 instances.

How can the architect build a solution to address the given use case?

- **A.** Configure a Route 53 health check that monitors an SNS topic which in turn notifies a CloudWatch alarm when the EC2 StatusCheckFailed metric fails
- **B.** Configure a Route 53 health check to a private IP associated with the instances inside the VPC to be checked
- **C.** Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric and then configure a health check that monitors the status of the metric
- **D.** Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric, add an alarm to the metric, and then configure a health check that monitors the state of the alarm

---

## Q14

An e-commerce company wants to rollout and test a blue-green deployment for its global application in the next couple of days. Most of the customers use mobile phones which are prone to DNS caching. The company has only two days left before the big sale will be launched.

As a Solutions Architect Professional, which of the following options would you suggest to test the deployment on as many users as possible in the given time frame?

- **A.** Use Route 53 weighted routing to spread traffic across different deployments
- **B.** Use AWS CodeDeploy deployment options to choose the right deployment
- **C.** Use Elastic Load Balancer to distribute traffic across deployments
- **D.** Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment

---

## Q15

A company wants to migrate its on-premises resources to AWS. The IT environment consists of 200 virtual machines (VMs) with a combined storage capacity of 50 TB. While the majority of VMs may be taken down for migration since they are only used during business hours, others are mission-critical, so the downtime must be minimized. The on-premises network engineer has allocated 10 Mbps of internet bandwidth for the migration. The capacity of the on-premises network has peaked and increasing it would be prohibitively expensive.

You have been hired as an AWS Certified Solutions Architect Professional to develop a migration strategy that can be implemented in the next three months. Which of the following would you recommend?

- **A.** Export the VMs locally, starting with the most mission-critical servers first. Configure a 1.25 Gbps AWS site-to-site VPN to securely upload each VM to Amazon S3 after they are exported. Use VM Import/Export to import the VMs into Amazon EC2
- **B.** Migrate mission-critical VMs using AWS Application Migration Service (MGN). Export the other VMs locally and transfer them to Amazon S3 using AWS Snowball Edge. Leverage VM Import/Export to import the VMs into Amazon EC2
- **C.** Leverage AWS Migration Hub to analyze each application for further refactoring and optimizations using AWS services or AWS Marketplace solutions
- **D.** Create a 10 Gbps AWS Direct Connect connection and then configure a private virtual interface. Leverage AWS Server Migration Service (SMS) to migrate the VMs into Amazon EC2

---

## Q16

A tech company that performs large-scale analytics uses an Amazon Redshift cluster with reserved nodes to support its daily data workloads. A recently hired director has initiated a new requirement: generating a deep audit analysis report. This new reporting initiative has introduced complex read queries that are highly CPU-intensive, resulting in unexpected bursts of usage on the Redshift cluster.
The existing setup must continue to handle both read and write queries consistently, even during performance spikes. A solutions architect must propose the most cost-effective solution to address the rising CPU metrics while maintaining system responsiveness and minimizing operational cost.
What is the most economical approach to manage the increased workload introduced by this new reporting initiative?

- **A.** Launch additional Amazon EC2 instances to scale horizontally Redshift for query parallelization.
- **B.** Export data from Redshift and import it into Amazon RDS PostgreSQL for deep audit analysis during periods of high load.
- **C.** Deploy an Amazon EMR cluster to offload high-load transformation jobs from the main analytics pipeline.
- **D.** Enable concurrency scaling in the Redshift setup to handle spikes in concurrent query loads without impacting performance.

---

## Q17

A web development studio runs hundreds of Proof-of-Concept (PoC) and demo applications on virtual machines running on an on-premises server. Many of the applications are simple PHP, JavaScript or Python web applications which are no longer actively developed and serve little traffic.

As a Solutions Architect Professional, which of the following approaches would you suggest to migrate these applications to AWS with the lowest infrastructure cost and least development effort?

- **A.** Leverage VM Import/Export to create AMIs for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image
- **B.** Leverage AWS Server Migration Service (SMS) to create AMIs for each virtual machine and run each application on a dedicated EC2 instance
- **C.** Dockerize each application and then deploy to an ECS cluster running behind an Application Load Balancer
- **D.** Migrate the application code to use a serverless stack comprising of Lambda functions and DynamoDB

---

## Q18

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

---

## Q19

A global multi-player gaming application runs on UDP protocol and it needs to add functionality where you can assign multiple players to a single session on a game server based on factors such as geographic location, player skill, and a few more configurable parameters. The application is accessed by players spread out across different regions of the world.

What is the BEST way to configure this requirement?

- **A.** Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC subnet endpoints
- **B.** Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC sharing
- **C.** Use custom routing accelerator of Global Accelerator in front of Network Load Balancer (NLB) to route traffic that can maintain session data
- **D.** Use Application Load Balancer (ALB) with sticky sessions enabled to maintain player session data. Configure Global Accelerator to front the ALB for cross-region elasticity

---

## Q20

A bank has received a security directive to harden its cloud infrastructure in response to a wave of cyberattacks targeting financial institutions. As part of this initiative, the bank is integrating third-party firewall appliances sourced from the AWS Marketplace to perform deep inspection and control of outbound internet traffic originating from all internal workloads.
The strategy involves centralizing these firewall appliances inside a shared services VPC, serving as a security chokepoint across the organization’s cloud infrastructure. The bank’s network team has already implemented VPC routing that funnels traffic from spoke VPCs into the shared services VPC.
The cloud security engineer must design a secure and highly available inspection architecture within a single AWS Region to satisfy security requirements and uptime guarantees.
Which of the following should the cloud engineer implement to meet these goals?

- **A.** Provision firewall appliances across two different Availability Zones in the shared services VPC. Set up a Network Load Balancer linked to a target group that includes the appliances. Deploy a VPC interface endpoint and configure the route table to direct incoming VPC traffic to this endpoint as the next hop.
- **B.** Launch both firewall appliances in a single Availability Zone within the shared services VPC. Configure an Application Load Balancer and link it to a target group containing the appliances. Deploy a VPC interface endpoint and update the route table to forward traffic from connected VPCs to the endpoint as the next hop.
- **C.** Launch both firewall appliances in one Availability Zone within the shared services VPC. Configure a Gateway Load Balancer and associate it with a target group containing the appliances. Provision a Gateway Load Balancer endpoint and update the shared services VPC route table to use it as the next hop for incoming traffic from connected VPCs.
- **D.** Place two firewall appliances in different Availability Zones in the shared services VPC. Set up a Gateway Load Balancer and link it to a target group containing both appliances. Then, deploy a Gateway Load Balancer endpoint and configure the shared services VPC route table to forward inter-VPC traffic to this endpoint as the next hop.

---

## Q21

A web application is hosted on Amazon EC2 instances that are fronted by Application Load Balancer (ALB) configured with an Auto Scaling group (ASG). Enhanced security is provided to the ALB by AWS WAF web ACLs. As per the company's security policy, AWS CloudTrail is activated and logs are configured to be stored on Amazon S3 and CloudWatch Logs.

A holiday sales offer was run on the application for a week. The development team has noticed that a few of the instances have rebooted taking down the log files and all temporary data with them. Initial analysis has confirmed that the incident took place during off-peak hours. Even though the incident did not cause any sales or revenue loss, the CTO has asked the development team to fix the security error that has allowed the incident to go unnoticed and eventually untraceable.

Which of the following steps will you implement to permanently record all traffic coming into the application?

- **A.** Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking
- **B.** To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring
- **C.** Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting
- **D.** Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking

---

## Q22

A global enterprise manages multiple AWS accounts under a single organization using AWS Organizations. The enterprise leverages AWS CloudFormation to automate infrastructure provisioning and centrally manages permissions and roles using AWS Identity and Access Management (IAM).
As part of a new chargeback model, the finance department requires each department to apply project tags selected from a predefined list of tag values to every newly created resource.
When analyzing spending using the AWS Cost and Usage Report in AWS Cost Explorer, the finance team identified non-compliant tag values that disrupted cost attribution.
To enforce compliance, the company needs a scalable way to validate and implement resource tagging based on these project values.
Which approach offers the easiest and most effective way to enforce this?

- **A.** Enable resource tagging enforcement using AWS Config rules. Integrate the rules with Organizations to evaluate tag compliance across accounts. Use automation documents to prevent cloudformation:CreateStack unless tags meet policy requirements.
- **B.** In the organization’s management account, define a tag policy with valid project tag values. Then, create a Service Control Policy (SCP) to deny cloudformation:CreateStack except if the required project tag is included. Attach the created SCP to the root of the organization.
- **C.** Configure a tag policy in the Organizations management account to specify the approved project tag values. Then, implement an SCP that blocks the cloudformation:DetectStackResourceDrift operation unless a compliant project tag is part of the request. Apply this SCP at the organization’s root level.
- **D.** Use the AWS Tag Editor to audit and correct resource tags across all accounts. Schedule periodic reviews to identify non-compliant tags and update them to match the predefined project tag list

---

## Q23

An e-commerce company has hired an AWS Certified Solutions Architect Professional to transform a standard three-tier web application architecture in AWS. Currently, the web and application tiers run on EC2 instances and the database tier runs on RDS MySQL. The company wants to redesign the web and application tiers to use API Gateway with Lambda Functions with the final goal of deploying the new application within 6 months. As an immediate short-term task, the Engineering Manager has mandated the Solutions Architect to reduce costs for the existing stack.

Which of the following options should the Solutions Architect recommend as the MOST cost-effective and reliable solution?

- **A.** Provision Reserved Instances for the web and application tiers and On-Demand Instances for the database tier
- **B.** Provision Reserved Instances for the web, application and database tiers
- **C.** Provision Spot Instances for the web and application tiers and Reserved Instances for the database tier
- **D.** Provision On-Demand Instances for the web and application tiers and Reserved Instances for the database tier

---

## Q24

A Wall Street based trading firm is modernizing its message queuing system by migrating from self-managed message-oriented middleware systems to Amazon SQS. The firm is using SQS to migrate several trading applications to the cloud to ensure high availability and cost efficiency while simplifying administrative complexity and overhead. The development team at the firm expects a peak rate of about 2,400 messages per second to be processed via SQS. It is important that the messages are processed in the order they are received.

Which of the following options can be used to implement this system in the most cost-effective way?

- **A.** Use Amazon SQS FIFO queue in batch mode of 8 messages per operation to process the messages at the peak rate
- **B.** Use Amazon SQS FIFO queue in batch mode of 12 messages per operation to process the messages at the peak rate
- **C.** Use Amazon SQS FIFO queue in batch mode of 4 messages per operation to process the messages at the peak rate
- **D.** Use Amazon SQS standard queue to process the messages

---

## Q25

A data analytics company uses Amazon S3 as the data lake to store the input data that is ingested from the IoT field devices on an hourly basis. The ingested data has attributes such as the device type, ID of the device, the status of the device, the timestamp of the event, the source IP address, etc. The data runs into millions of records per day and the company wants to run complex analytical queries on this data daily for product improvements for each device type.

Which is the most optimal way to save this data to get the best performance from the millions of data points processed daily?

- **A.** Store the data in Apache ORC, partitioned by date and sorted by device type of the device
- **B.** Store the data in compressed .csv, partitioned by date and sorted by the status of the device
- **C.** Store the data in compressed .csv, partitioned by date and sorted by device type
- **D.** Store the data in Apache Parquet, partitioned by device type and sorted by date

---

## Q26

A North American-based tech startup plans to expand to Europe due to the unexpected, overwhelming success of its software-as-a-service (SaaS) solution, which uses AWS AppFabric for SaaS integration and security observability. A solutions architect consultant was hired to design and execute the expansion.
The company uses the us-east-1 Region for its North American infrastructure. The system uses Amazon S3, which is accessed through Amazon CloudFront, as its front-end component. It uses Amazon API Gateway for the API endpoints. AWS Lambda functions connected to an Amazon RDS for MySQL serve as its backend and persistence layer. Amazon Route 53 manages the domain via a simple routing policy pointing to the API Gateway.
In anticipation of the upcoming expansion, the engineering team proactively provisioned eu-west-1 Region infrastructure, including API Gateways and Lambda functions in the mentioned Region.
Initial measurements of the consultant suggest that around 95% of the database traffic is read-only.
What approach can the consultant take to expand on the existing eu-west-1 Region and ensure minimal latency for users in the Europe Region?

- **A.** In Route 53, use latency-based routing. Set up a cross-Region read replica of the database in eu-west-1.
- **B.** Use latency-based routing in Route 53 to direct traffic to the appropriate API  endpoint. Configure an AWS Database Migration Service (AWS DMS) task with change data capture (CDC) for replication of the main database from the us-east-1 to eu-west-1 .
- **C.** Use failover routing in Route 53. Create a Multi-AZ replica of the primary database.
- **D.** Keep simple routing in Route 53 for minimal setup. Set up an AWS Database Migration Service (AWS DMS) task with full load combined with change data capture (CDC) to replicate the original database from us-east-1 to eu-west-1.

---

## Q27

A web hosting company's CFO recently analyzed the company's monthly bill for the AWS account for the development environment and identified an opportunity to reduce the cost for AWS Elastic Beanstalk infrastructure in use. The CFO in consultation with the CTO has hired you as an AWS Certified Solutions Architect Professional to design a highly available solution that will provision an Elastic Beanstalk environment in the morning and terminate it at the end of the day. The solution should be designed with minimal operational overhead with a focus on minimizing costs. The solution should also facilitate the increased use of Elastic Beanstalk environments among different development teams and must provide a one-stop scheduler solution for all teams to keep the operational costs as low as possible.

Which of the following solution designs will you suggest to address these requirements?

- **A.** Provision an EC2 Micro instance. Configure an IAM role with the required Elastic Beanstalk environment permissions and attach it to the instance profile. Create scripts on the instance to provision and terminate the Elastic Beanstalk environment. Set up cron jobs on the instance to execute the scripts
- **B.** Leverage the activity task of an AWS Step Function to provision and terminate the Elastic Beanstalk environment. Create a role for the Step Function to allow it to provision and terminate the Elastic Beanstalk environment. Execute the Step Function daily and use the "wait state" to control the start and stop time
- **C.** Configure the Elastic Beanstalk environment to use custom commands in the EC2 instance user data. Leverage the scheduled action for an Auto Scaling group to scale-out EC2 instances in the morning and scale-in the instance count to 0 to terminate the EC2 instances at the end of the day
- **D.** Set up separate Lambda functions to provision and terminate the Elastic Beanstalk environment. Configure a Lambda execution role granting the required Elastic Beanstalk environment permissions and assign the role to the Lambda functions. Configure cron expression based Amazon EventBridge events rules to trigger the Lambda functions

---

## Q28

The development team at a company has noticed issues with the Quality of Service (QoS) in the traffic to the EC2 instances hosting a VOIP program. The team needs to inspect the network packets to determine if it is a programming error or a networking error.

As an AWS Certified Solutions Architect Professional, which of the following options would you suggest for the given use case?

- **A.** Configure traffic mirroring on the source EC2 instances hosting the VOIP program, set up a network monitoring program on a target EC2 instance and stream the logs to an S3 bucket for further analysis
- **B.** Use CloudWatch to inspect the network packets
- **C.** Provision another EC2 instance with an ENI added to act as a monitoring interface. Configure the port to promiscuous mode and sniff the traffic to analyze the packets. Direct the output of this single stream to an S3 bucket for further analysis
- **D.** Use VPC Flow Logs to inspect the network packets

---

## Q29

An e-commerce company manages its flagship applications on AWS. The Amazon EC2 instances running the applications are fronted by an Application Load Balancer (ALB). Amazon Route 53 provides public DNS services. Different URLs (mobile.ecomm.com, web.ecomm.com, api.ecomm.com) will serve the required content to the end-users.

As an AWS Certified Solutions Architect Professional, which combination of services would you use to serve the content to the end-users? (Select two)

- **A.** Use Path conditions in ALB listener to route *.ecomm.com to appropriate target groups
- **B.** Use Host conditions in ALB listener to route *.ecomm.com to appropriate target groups
- **C.** Use Host conditions in ALB listener to route $$$$.ecomm.com to appropriate target groups
- **D.** Use Host conditions in ALB listener to route ecomm.com to appropriate target groups
- **E.** Use Path component of Redirect actions in ALB listener configuration to route ecomm.com to appropriate target groups

---

## Q30

A financial institution is running multiple AWS Lambda functions. These functions are packaged as .zip archives and rely on a shared Lambda layer that contains common libraries.
Security compliance requires that the development team must:


Continuously monitor the Lambda functions and the shared Lambda layer for current common vulnerabilities and exposures (CVEs).


Perform additional automated code scans on a subset of Lambda functions to detect data leaks and injection flaws.


Ensure that not all Lambda functions are scanned for code issues, since some workloads handle non-sensitive test data.


The company wants a fully managed AWS-native solution to meet these requirements.


Which of the following will meet the given requirements? (Select THREE.)

- **A.** Apply an Amazon Inspector exclusion tag with a key of InspectorCodeExclusion and a value of LambdaCodeScanning to Lambda functions that should not be code-scanned.
- **B.** Enable Amazon Inspector Lambda code scanning to detect code-level vulnerabilities.
- **C.** Use AWS IAM policies to restrict Amazon Inspector from scanning specific Lambda functions.
- **D.** Use Amazon GuardDuty Lambda Protection to monitor for CVEs and data leaks.
- **E.** Enable AWS Config with a custom rule to check Lambda deployment packages for CVEs.
- **F.** Enable Amazon Inspector and activate Lambda standard scanning for CVE detection.

---

## Q31

A genome research facility uses AWS Step Functions to orchestrate a nightly machine learning pipeline that retrains predictive models to discover potential cancer cures. The pipeline consists of multiple AWS Lambda tasks responsible for parsing genomic data, running simulations, and optimizing hyperparameters. Each step is time-sensitive and mission-critical.
Recently, the research team discovered that if even a single state within the Step Functions workflow encounters an error, whether during data processing, model training, or evaluation, the entire retraining sequence fails silently, and no alerts are sent. As a result, several nights of crucial model updates were missed without the team’s knowledge.
The solutions architect must implement a failure detection and notification system to avoid these unseen interruptions. This solution should immediately alert the team by email anytime a Task, Map, or Parallel state fails. The alert must include the original input arguments that triggered the failure, enabling rapid diagnosis and response.
Which action should the architect take to design this system?

- **A.** Set up an Amazon SNS topic and configure an Email-type subscription that delivers messages to the group’s distribution address. Define a Task state called “Email” that sends the state’s input parameters to the SNS topic. For every Task, Map, and Parallel state, add a Catch clause that matches  "ErrorEquals": ["States.ALL"], and routes the flow to the “Email” state via the “Next” field.
- **B.** Enable AWS X-Ray on all Lambda functions in the workflow to trace failed invocations. Implement a Catch clause in all Task, Map, and Parallel states, setting "ErrorEquals": ["States.ALL"] to handle any failure type. Route execution to the “Email” state through the “Next” property whenever an error is intercepted.
- **C.** Provision an Amazon SNS topic and attach an Email-based subscription that routes notifications to the team’s group inbox. Introduce a Task state labeled “Email” that passes along the received input to the SNS topic. For each Task, Map, and Parallel state, include a Catch block configured with  "ErrorEquals": ["States.Runtime"] and direct control to the “Email” state using the “Next” parameter.
- **D.** Use Amazon EventBridge to monitor the execution history of the Step Functions. Add a Catch handler to every Task, Map, and Parallel state, specifying "ErrorEquals": ["States.Runtime"] to capture runtime-related issues. Use the “Next” field to transition the flow to the “Email” state upon encountering such errors.

---

## Q32

A fast-rising technology company is preparing to migrate a portfolio of applications to AWS. The current on-premises environment includes a mix of physical and virtual machines. The founding CTO, who originally designed the infrastructure, has left the company and provided limited documentation about the architecture.
The company lacks complete visibility into its application estate and infrastructure layout.
One critical application scheduled for migration has several unmapped dependencies. Many of these dependencies use low-latency communication over a custom IP-based protocol bound to port 1000. To preserve operational integrity, the company must migrate the application and all tightly coupled systems in the same migration wave.
The company has used AWS Transform discovery and assessment capabilities to collect telemetry from its servers for several months. The new CTO must now identify the complete set of connected systems that should be grouped and migrated together.
What approach should the new CTO take to discover and group the correct dependencies for simultaneous migration?

- **A.** Export the collected discovery data to Amazon S3. Use AWS Glue to crawl the exported dataset and create a data catalog. Then run Amazon Athena queries to search for references to port 1000 or IP-based traffic. Create a migration wave based only on the query results and proceed with the migration.
- **B.** Use AWS Transform MGN to replicate the application servers and migrate them immediately. After cutover, rely on Amazon CloudWatch metrics to identify dependency-related issues. Then scan for any missing dependencies and migrate those systems later as needed.
- **C.** Use AWS Transform discovery and assessment capabilities to analyze the application servers and their communication patterns. Review the dependency mapping and network flow data, and use Amazon Athena data exploration to identify systems communicating through the custom protocol on port 1000. Group the application and all tightly coupled dependent servers into the same migration wave for coordinated migration.
- **D.** Use Amazon VPC Network Access Analyzer to define a network access scope that matches traffic on port 1000. Analyze the resulting network paths to determine which systems communicate with the application. Then create a migration wave in AWS Transform based on the Network Access Analyzer results.

---

## Q33

An investment firm collects daily stock trading data from exchanges and stores it in a data warehouse. The development team at the firm needs a solution that streams data directly into the data repository but should also allow SQL-based data modifications when needed. The solution should facilitate complex analytical queries that execute in the fastest possible time. The solution should also offer a business intelligence dashboard that highlights any stock price anomalies.

Which of the following options represents the best solution for the given use case?

- **A.** Configure Amazon Kinesis Data Streams to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source
- **B.** Configure Amazon Kinesis Data Streams to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source
- **C.** Configure Amazon Kinesis Data Firehose to stream data to Amazon S3. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Athena as a data source
- **D.** Configure Amazon Kinesis Data Firehose to stream data to Amazon Redshift. Create a business intelligence dashboard by using Amazon QuickSight that has Amazon Redshift as a data source

---

## Q34

A company provides a web-based business-management platform for IT service companies across the globe to manage help desk, customer service, sales and marketing, and other critical business functions. More than 50,000 people use the company's platform, so the company must respond quickly to any reported problems. However, the company has issues with not having enough visibility into its systems to discover any issues. Multiple logs and monitoring systems are needed to understand the root cause of problems thereby taking hours to resolve. Even as the company is slowly moving towards serverless architecture using AWS Lambda/Amazon API Gateway/Amazon Elastic Container Service (Amazon ECS), the company wants to monitor the microservices and gain deeper insights into its serverless resources.

Which of the following will you recommend to address the given requirements?

- **A.** Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing
- **B.** Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon CloudWatch for monitoring containers, latency, web server requests, and incoming load-balancer requests and create CloudWatch alarms to send out notifications if system latency is increasing
- **C.** Configure Amazon CloudWatch to monitor and analyze all microservices through request tracing. Enable CloudTrail to log all user activity
- **D.** Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing. Use AWS Config to continually assesses, audit, and evaluate the configurations and relationships of your resources and trigger alarms when needed

---

## Q35

The engineering team at a retail company has deployed a fleet of EC2 instances under an Auto Scaling group (ASG). The instances under the ASG span two Availability Zones (AZ) within the eu-west-1 region. All the incoming requests are handled by an Application Load Balancer (ALB) that routes the requests to the EC2 instances under the ASG. A planned migration went wrong last week when two instances (belonging to AZ 1) were manually terminated and desired capacity was reduced causing the Availability Zones to become unbalanced. Later that day, another instance (belonging to AZ 2) was detected as unhealthy by the Application Load Balancer's health check.

Which of the following options represent the correct outcomes for the aforesaid events? (Select two)

- **A.** Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance
- **B.** Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously
- **C.** As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched
- **D.** Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it
- **E.** As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application

---

## Q36

A company has its web application hosted on Amazon EC2 instances that are deployed in a single AWS Region. The company has now expanded its operations into new geographies and the company wants to offer low-latency access for the application to its customers. To comply with different financial regulations of each geography, the application needs to operate in silos and the underlying instances in one region should not interact with instances running in other regions.

Which of the following represents the most optimal solution to automate the application deployment to different AWS regions?

- **A.** Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation stack set from an administrator account to launch stack instances that deploy the application to various other regions
- **B.** Create a shell script that uses the AWS CLI to query the current state in one region and output an AWS CloudFormation template. Create a CloudFormation stack from the template by using the AWS CLI, specifying the --region parameter to deploy the application to other regions
- **C.** Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation change set from an administrator account to launch stack instances that deploy the application to various other regions
- **D.** Create a CloudFormation template describing the application infrastructure in the Resources section. Create a CloudFormation stack from the template by using the AWS CLI, specify multiple regions using the --regions parameter to deploy the application

---

## Q37

A company has its flagship application fronted by an Application Load Balancer that is targeting several EC2 Linux instances running in an Auto Scaling group in a private subnet. AWS Systems Manager Agent is installed on all the EC2 instances. The company recently released a new version of the application, however, some of the EC2 instances are now being marked as unhealthy and are being terminated, thereby causing the application to run at reduced capacity. You have been tasked to ascertain the root cause by analyzing Amazon CloudWatch logs that are collected from the application, but you find that the logs are inconclusive.

Which of the following options would you propose to get access to an EC2 instance to troubleshoot the issue?

- **A.** Suspend the Auto Scaling group's Launch process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause
- **B.** Suspend the Auto Scaling group's Terminate process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause
- **C.** Enable EC2 instance termination protection. Use Session Manager to log In to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause
- **D.** Suspend the Auto Scaling group's HealthCheck process. Use EC2 instance connect to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause

---

## Q38

A leading internet television network company uses AWS Cloud for analytics, recommendation engines and video transcoding. To monitor and optimize this network, the engineering team at the company has developed a solution for ingesting, augmenting, and analyzing the multiple terabytes of data its network generates daily in the form of virtual private cloud (VPC) flow logs. This would enable the company to identify performance-improvement opportunities such as identifying apps that are communicating across regions and collocating them. The VPC flow logs data is funneled into Kinesis Data Streams which further acts as the source of a delivery stream for Kinesis Firehose. The engineering team has now configured a Kinesis Agent to send the VPC flow logs data from another set of network devices to the same Firehose delivery stream. They noticed that data is not reaching Firehose as expected.

As a Solutions Architect Professional, which of the following options would you identify as the MOST plausible root cause behind this issue?

- **A.** Kinesis Firehose delivery stream has reached its limit and needs to be scaled manually
- **B.** The data sent by Kinesis Agent is lost because of a configuration error
- **C.** Kinesis Agent cannot write to a Kinesis Firehose for which the delivery stream source is already set as Kinesis Data Streams
- **D.** Kinesis Agent can only write to Kinesis Data Streams, not to Kinesis Firehose

---

## Q39

An edtech company is preparing to launch a new virtual learning environment (VLE) hosted on Amazon EC2 instances. To support students and educators around the globe, the platform must be deployed across three AWS Regions: us-east-1, eu-west-1, and ap-southeast-1. Key components of the system, such as student progress tracking, resource availability, and real-time collaboration events, must remain consistent and synchronized across all Regions.
To support real-time interactivity, the VLE uses more than just standard HTTP and HTTPS ports. WebSocket connections run on port 5000 for live quizzes, and the interactive whiteboard feature communicates over port 8080. To ensure optimal user experience, the platform must direct learners to the AWS Region with the lowest latency. Additionally, the architecture must be designed so that any single Region can dynamically scale to accommodate traffic from all others, should the need arise.
A solutions architect must define an infrastructure strategy that delivers global availability, seamless scalability, and low-latency access, all while keeping operational overhead to a minimum.
What solution best satisfies these needs while reducing operational management effort?

- **A.** Deploy EC2 instances within Auto Scaling groups across all AWS Regions, linking each group to its corresponding Application Load Balancer (ALB). Configure Amazon Route 53 to use latency-based routing policies, directing users to the Region with the fastest response time via the associated ALB. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions.
- **B.** Deploy EC2 Auto Scaling groups across all AWS Regions and link each group to its own Network Load Balancer (NLB). Enable EC2 Global View to centrally monitor and manage instance health, capacity, and scaling activity across Regions. Use Amazon Route 53 with latency-based routing to ensure users are directed to the Region delivering the lowest latency. Store platform metadata in Amazon RDS for PostgreSQL, deploying one instance per Region, and configure cross-Region read replicas to maintain synchronized data consistency on a global scale.
- **C.** Provision of an EC2 Auto Scaling group in every AWS Region to manage computing resources dynamically. Associate each group with its respective Network Load Balancer (NLB). Configure Amazon Route 53 with latency-based routing policies that direct traffic to the NLB offering the fastest response times per Region. Store platform metadata within an Amazon DynamoDB global table to maintain data consistency across all Regions.
- **D.** Launch an EC2 Spot Fleet in every AWS Region and link each to its respective Network Load Balancer (NLB). Provision an AWS Global Accelerator IP address that targets the NLB to enable consistent global access. Configure Amazon Route 53 to apply latency-based routing, directing traffic to the Region with the fastest response time using the AWS Global Accelerator IP address. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions.

---

## Q40

A company has built its serverless solution using Amazon API Gateway REST API and AWS Lambda across multiple AWS Regions configured into a single AWS account. During peak hours, customers began to receive 429 Too Many Requests errors from multiple API methods. While troubleshooting the issue, the team realized that AWS Lambda function(s) have not been invoked for these API methods. Also, the company wants to provide a separate quota for its premium customers to access the APIs.

Which solution will you offer to meet this requirement?

- **A.** The error is the outcome of the company reaching its API Gateway account limit for calls per second, set Lambda-level throttling targets in the API Gateway usage plan, and configure customers to use a particular API method when the client identifier is set
- **B.** The error is the outcome of the company reaching its API Gateway account per-method limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers
- **C.** The error is the outcome of the company reaching its API Gateway account limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers
- **D.** The error is the outcome of the company reaching its API Gateway limits for the steady-state requests per second (RPS) across all APIs within an AWS account per Region. These limits can be overwritten by configuring the AWS Regional throttling parameters to a greater value. However, based on the AWS account type, a limit is set to the overwritten throttling values

---

## Q41

A multi-national bank has recently migrated to AWS Cloud to utilize dedicated instances that are physically isolated at the host hardware level from instances that belong to other AWS accounts. The bank's flagship application is hosted on a fleet of EC2 instances which are part of an Auto Scaling group (ASG). The ASG uses a Launch Configuration (LC-A) with "dedicated" instance placement tenancy but the VPC (VPC-A) used by the Launch Configuration LC-A has the instance tenancy set to default. Later the engineering team creates a new Launch Configuration (LC-B) with "default" instance placement tenancy but the VPC (VPC-B) used by the Launch Configuration LC-B has the instance tenancy set to dedicated.

As a Solutions Architect Professional, which of the following options would you identify as correct regarding the instances launched via Launch Configuration LC-A and Launch Configuration LC-B?

- **A.** The instances launched by Launch Configuration LC-A will have dedicated instance tenancy while the instances launched by the Launch Configuration LC-B will have default instance tenancy
- **B.** The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have default instance tenancy
- **C.** The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have dedicated instance tenancy
- **D.** The instances launched by Launch Configuration LC-A will have default instance tenancy while the instances launched by the Launch Configuration LC-B will have dedicated instance tenancy

---

## Q42

A retail company is deploying a critical application on multiple EC2 instances in a VPC. Per the company policy, any failed client connections to the EC2 instances must be logged.

Which of the following options would you recommend as the MOST cost-effective solution to address these requirements?

- **A.** Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to a Kinesis Data Firehose stream with the data delivery to an S3 bucket
- **B.** Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to Kinesis Data Streams with the data delivery to an S3 bucket
- **C.** Set up VPC Flow Logs for the elastic network interfaces associated with the instances and configure the VPC Flow Logs to be filtered for rejected traffic. Publish the Flow Logs to CloudWatch Logs
- **D.** Migrate the EC2 instances to a dedicated VPC. Configure VPC Flow Logs with a filter on the reject action. Publish the Flow Logs to Amazon CloudWatch Logs

---

## Q43

The DevOps team for a CRM SaaS company wants to implement a patching plan on AWS Cloud for a large mixed fleet of Windows and Linux servers. The patching plan has to be auditable and must be implemented securely to ensure compliance with the company's business requirements.

As a Solutions Architect Professional, which of the following options would you recommend to address these requirements with MINIMAL effort? (Select two)

- **A.** Apply patch baselines using the AWS-RunPatchBaseline SSM document
- **B.** Apply patch baselines using the AWS-ApplyPatchBaseline SSM document
- **C.** Set up an OS-native patching service to manage the update frequency and release approval for all instances. Set up AWS Config to provide audit and compliance reporting
- **D.** Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval
- **E.** Configure OpsWorks automatic patching support for all applications which will keep the OS up-to-date following the initial installation. Set up AWS Config to provide audit and compliance reporting

---

## Q44

A solutions architect at a retail company has set up a workflow to ingest the clickstream data into the raw zone of the S3 data lake. The architect wants to run some SQL-based data sanity checks on the raw zone of the data lake.

What AWS services would you suggest for this requirement such that the solution is cost-effective and easy to maintain?

- **A.** Use Athena to run SQL based analytics against S3 data
- **B.** Load the incremental raw zone data into Redshift on an hourly basis and run the SQL based sanity checks
- **C.** Load the incremental raw zone data into RDS on an hourly basis and run the SQL based sanity checks
- **D.** Load the incremental raw zone data into an EMR based Spark Cluster on an hourly basis and use SparkSQL to run the SQL based sanity checks

---

## Q45

An accounting company initiated a migration of its core workloads to the AWS Cloud to modernize its infrastructure, following a recent change in technical leadership. The company’s current setup includes Graviton‑based Amazon EC2 instances (ARM64 architecture) for compute resources, Amazon EFS for shared file storage, and Amazon RDS DB instances for managing relational databases.




To comply with regulatory mandates and uphold internal data governance standards, the new leadership has mandated the following backup procedures:


The solution must provide a centralized overview of backup status across the AWS environment.


Any backup failure must trigger immediate notifications to technical stakeholders.


Data backups must follow custom retention policies, with separate rules for daily, weekly, and monthly backups.


Backups must be automatically replicated to at least one additional AWS Region immediately after creation.


Which actions will meet these objectives while introducing the least operational overhead?

- **A.** Define individual snapshot lifecycle policies in Amazon Data Lifecycle Manager (Amazon DLM) to align with each retention requirement. Activate cross-Region snapshot replication within DLM to ensure backups are automatically copied to another AWS Region. Develop an AWS Lambda function that monitors for backup or restore events and triggers a notification when a job finishes with either RESTORE_JOB_SUCCESSFUL or BACKUP_JOB_FAILED status.
- **B.** Define an AWS Backup plan that includes individual backup rules aligned with each required retention schedule. Develop an AWS Lambda function to handle cross-Region backup replication and to dispatch notifications whenever a backup job results in BACKUP_JOB_FAILED or  RESTORE_JOB_SUCCESSFUL.
- **C.** Establish an AWS Backup strategy incorporating individual backup rules corresponding to every retention specification. Set up a Backup strategy for cross-Region backup replication. Integrate an Amazon Simple Notification Service (Amazon SNS) topic into the backup strategy to dispatch alerts for completed operations, excluding those with the BACKUP_JOB_COMPLETED status.
- **D.** Develop and deploy a consolidated Python script on a single EC2 instance. Schedule the script to connect to each RDS DB instance, run pg_dump/mysqldump. Call the create_image() API to generate AMIs for selected instances. Mount the EFS file system to the EC2 instance and use rsync to copy data. Replicate the backup files to another Region using Amazon S3. Send emails using Amazon SES if anything fails.

---

## Q46

A healthcare company has to maintain a log of all transactions for audit and compliance purposes. The company is planning stringent security measures for all of its CloudTrail log files.

Which of the following would you suggest as the LEAST effort options to secure the CloudTrail logs? (Select two)

- **A.** Integrate with Amazon CloudWatch alarms to generate an alarm whenever changes are made to CloudTrail log files
- **B.** To prevent access rights violation, use AWS root user account to manage CloudTrail logs
- **C.** Use Amazon S3 MFA Delete on the S3 bucket that holds CloudTrail logs and digest files
- **D.** Enable CloudTrail log file integrity validation
- **E.** Enable Amazon S3 encryption using AWS KMS keys on the S3 bucket that stores CloudTrail logs to prevent unauthorized modification of the log files

---

## Q47

A leading hotel reviews website has a repository of more than one million high-quality digital images. When this massive volume of images became too cumbersome to handle in-house, the company decided to offload the content to a central repository on Amazon S3 as part of its hybrid cloud strategy. The company now wants to reprocess its entire collection of photographic images to change the watermarks. The company wants to use Amazon EC2 instances and Amazon SQS in an integrated workflow to generate the sizes they need for each photo. The team wants to process a few thousand photos each night, using Amazon EC2 Spot Instances. The team uses Amazon SQS to communicate the photos that need to be processed and the status of the jobs. To handle certain sensitive photos, the team wants to postpone the delivery of certain messages to the queue by one minute while all other messages need to be delivered immediately to the queue.

As a Solutions Architect Professional, which of the following solutions would you suggest to the company to handle the workflow for sensitive photos?

- **A.** Use visibility timeout to postpone the delivery of certain messages to the queue by one minute
- **B.** Use message timers to postpone the delivery of certain messages to the queue by one minute
- **C.** Use delay queues to postpone the delivery of certain messages to the queue by one minute
- **D.** Use dead-letter queues to postpone the delivery of certain messages to the queue by one minute

---

## Q48

A social media company is transitioning its IT infrastructure from its on-premises data center to the AWS Cloud. The company wants to move its data artifacts, 200 TB in total size, to Amazon S3 on the AWS Cloud in the shortest possible time. The company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for this data migration. In terms of the networking infrastructure, the company has a 500 Mbps Direct Connect connection to the AWS Cloud as well as an IPSec based AWS VPN connection using the public internet that supports a bandwidth of 1 Gbps.

Which of the following solutions would you recommend to address the given use-case?

- **A.** Leverage the 500 Mbps Direct Connect connection to transfer the data to S3 over the dedicated connection
- **B.** Leverage the 1Gbps IPSec based AWS VPN connection to transfer the data to S3 over the public internet
- **C.** Order three AWS Snowball Edge appliances, split and transfer the data to these three appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3
- **D.** Leverage S3 Transfer Acceleration to transfer the data to S3

---

## Q49

A company is building an on-demand streaming application on AWS Cloud. The company has chosen Amazon S3 as its storage service and moved the existing videos to an Amazon S3 bucket. The application requires the video playback to start quickly, fast-forwarding should be more efficient and the overall user experience should be smoother without smothering the user's bandwidth.

Which AWS service(s) will help implement this solution effectively?

- **A.** Use AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery. Create a CloudFront distribution that points to the S3 bucket with videos uploaded. CloudFront will direct the request to the best edge location, based on the user’s location enhancing the overall user experience
- **B.** Use AWS Elemental MediaConvert for file-based video processing and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest
- **C.** Use Amazon S3 for storage and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest
- **D.** Deploy the application on Amazon EC2 instances with access to the S3 bucket. Configure these with a Network Load Balancer (NLB). Deploy the application stack in multiple AWS Regions around the world and configure Global Accelerator to serve content to the user

---

## Q50

An e-commerce company has a three-tier web application with separate subnets for Web, Application and Database tiers. The CTO at the company wants to monitor any malicious activity targeting the web application running on EC2 instances. As a solutions architect, you have been tasked with developing a solution to notify the security team in case the network exposure of EC2 instances on specific ports violates the security policies of the company.

Which AWS Services would you use to build an automated notification system to meet these requirements with the least development effort? (Select two)

- **A.** AWS Shield
- **B.** VPC Flow Logs
- **C.** Amazon SNS
- **D.** Amazon Inspector
- **E.** Amazon CloudWatch

---

## Q51

An on-premises data center, set up a decade ago, hosts all the applications of a business. The business now wants to move to AWS Cloud. The documentation of these systems is outdated and complete knowledge of all existing workloads is absent. The data center hosts a mix of Windows and Linux virtual machines.

As a solutions architect, you need to provide a plan to migrate all the applications to the cloud. How will you gather the necessary data of the existing machines?

- **A.** Register the on-premises VMs with the AWS Migration Hub to collect configuration and utilization data
- **B.** Deploy the AWS Server Migration Service (AWS SMS) connector using the OVA image on the VMware cluster to collect configuration and utilization data from the VMs
- **C.** Install the AWS Application Discovery Service on each of the VMs to collect the configuration and utilization data
- **D.** Use the AWS Migration Portfolio Assessment (MPA) tool to connect to each of the VMs to collect the configuration and utilization data

---

## Q52

A weather monitoring agency stores and manages the global weather data for the last 50 years. The data has a velocity of 1GB per minute. You would like to store the data with only the most relevant attributes to build a predictive model for weather patterns.

Which of the following solutions would you use to build the most cost-effective solution with the LEAST amount of infrastructure maintenance?

- **A.** Capture the data in Kinesis Data Streams and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3
- **B.** Capture the data in a Spark Streaming Cluster on EMR use Spark Streaming transformations before writing to S3
- **C.** Capture the data in Kinesis Data Analytics and use SQL queries to filter and transform the data before writing to S3
- **D.** Capture the data in Kinesis Data Firehose and use an intermediary Lambda function to filter and transform the incoming stream before the output is dumped on S3

---

## Q53

An e-commerce company is planning to migrate its IT infrastructure from the on-premises data center to AWS Cloud to ramp up its capabilities well in time for the upcoming Holiday Sale season. The company’s CTO has hired you as an AWS Certified Solutions Architect Professional to design a distributed, highly available and loosely coupled order processing application. The application is responsible for receiving and processing orders before storing them in a DynamoDB table. The application has seen sporadic traffic spikes in the past and the CTO wants the application to be able to scale during marketing campaigns to process the orders with minimal disruption.

Which of the following options would you recommend as the MOST reliable solution to address these requirements?

- **A.** Ingest the orders in an SQS queue and trigger a Lambda function to process them
- **B.** Ingest the orders via a Step Function state machine and trigger an ECS container to process them
- **C.** Push the orders to an SNS topic and subscribe a Lambda function to process them
- **D.** Push the orders to Kinesis Data Streams and use Amazon EC2 instances to process them

---

## Q54

A gaming company runs its flagship application with an SLA of 99.99%. Global users access the application 24/7. The application is currently hosted on the on-premises data centers and it routinely fails to meet its SLA, especially when hundreds of thousands of users access the application concurrently. The engineering team has also received complaints from some users about high latency.

As a Solutions Architect Professional, how would you redesign this application for scalability and also allow for automatic failover at the lowest possible cost?

- **A.** Configure Route 53 geolocation-based routing to route to the nearest Region and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer
- **B.** Configure a combination of Route 53 failover routing with geolocation-based routing. Host the website behind an Application Load Balancer (ALB) with targets as EC2 instances that are automatically scaled via Auto-Scaling Group (ASG). Repeat this configuration of ALB with EC2 instances as targets that are scaled via ASG in multiple Regions. Use a Multi-AZ deployment with RDS MySQL as the data layer
- **C.** Configure Route 53 round-robin routing policy to distribute load evenly across all Regions and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer
- **D.** Configure Route 53 latency-based routing to route to the nearest Region and activate the health checks. Host the website on S3 in each Region and use API Gateway with AWS Lambda for the application layer. Set up the data layer using DynamoDB global tables with DAX for caching

---

## Q55

A social gaming company is developing a mobile game that streams score updates to a backend processor and then publishes results on a leaderboard. The company has hired you to design a solution that can handle major traffic spikes, process the mobile game updates in the order of receipt, and store the processed updates in a highly available database. The company wants to minimize the management overhead required to maintain the solution.

Which of the following solutions will you recommend to meet these requirements?

- **A.** Send score updates to Kinesis Data Streams which uses a Lambda function to process these updates and then store these processed updates in DynamoDB
- **B.** Send score updates to Kinesis Data Streams which uses a fleet of EC2 instances (with Auto Scaling) to process the updates in Kinesis Data Streams and then store these processed updates in DynamoDB
- **C.** Send score updates to an SQS queue which uses a fleet of EC2 instances (with Auto Scaling) to process these updates in the SQS queue and then store these processed updates in an RDS MySQL database
- **D.** Send score updates to an SNS topic, subscribe a Lambda function to this SNS topic to process the updates and then store these processed updates in a SQL database running on Amazon EC2

---

## Q56

A mobile app based social media company is using Amazon CloudFront to deliver media-rich content to its audience across the world. The Content Delivery Network (CDN) offers a multi-tier cache by default, with regional edge caches that improve latency and lower the load on the origin servers when the object is not already cached at the edge. However, there are certain content types that bypass the regional edge cache and go directly to the origin.

Which of the following content types skip the regional edge cache? (Select two)

- **A.** Static content such as style sheets, JavaScript files
- **B.** Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin
- **C.** Dynamic content, as determined at request time (cache-behavior configured to forward all headers)
- **D.** E-commerce assets such as product photos
- **E.** User-generated videos

---

## Q57

A cloud engineer at a fintech startup is preparing the infrastructure for a critical internal platform launch. The cloud engineer configures DNS resolution for a newly provisioned VPC in the ap-southeast-1 (Singapore) Region as part of the setup. This VPC uses the 13.232.18.0/24 CIDR block and has been integrated with Amazon Route 53 Resolver to manage DNS queries.
Initially, the team planned for basic DNS resolution, but the requirements have since changed to support more advanced functionality. Now, all domain name lookups must be routed through a Private hosted zone, and any Amazon EC2 instances with assigned Public IP addresses must automatically receive corresponding Public hostnames.
Which of the following should the cloud engineer do to satisfy the new requirements and ensure the domain names are resolved correctly and consistently within the VPC? (Select TWO.)

- **A.** Set up a private DNS zone and link it to the VPC. Confirm that the VPC has both enableDnsSupport and enableDnsHostnames enabled.
- **B.** Define a custom DHCP options set that specifies domain-name-servers=AmazonProvidedDNS, and attach this configuration to the VPC.
- **C.** Create a new DHCP options set that sets domain-name-servers=13.232.18.98, and apply this configuration to the VPC by associating it accordingly.
- **D.** Create a private hosted zone and associate it with the VPC. Ensure the VPC is configured with the appropriate instanceTenancy setting.
- **E.** Establish a private hosted zone and connect it to the designated VPC. Make sure that the enableNetworkAddressUsageMetrics feature is activated.

---

## Q58

A company has an Elastic Load Balancer (ELB) that is configured with an Auto Scaling Group (ASG) having a minimum of 4, a maximum of 10, and the desired value of 4 instances. The ASG cooldown and the termination policies are configured to the default values. Monitoring reports indicate a general usage requirement of 4 instances, while any traffic spikes result in an additional 10 instances. Customers have been complaining of request timeouts and partially loaded pages.

As an AWS Certified Solutions Architect Professional, which of the following options will you suggest to fix this issue?

- **A.** Enable Sticky Sessions on ELB
- **B.** Configure termination policies on ASG to determine which instances it terminates first during scale-in events
- **C.** Add a lifecycle hook on scale-out event to your ASG, making sure that the instance is fully ready before it starts receiving traffic
- **D.** Configure connection draining on ELB

---

## Q59

An international shipping company with a global fleet runs its cloud operations through a multi-account AWS environment managed by AWS Control Tower. Due to fluctuating fuel costs and rising logistics expenses, the company recently launched a company-wide cost-cutting initiative, including the tech department.
The company uses AWS Organizations for account-level boundaries, AWS Config to ensure compliance standards are met, and AWS Trusted Advisor to surface cost inefficiencies and potential security gaps.
As per the directive of the CTO, in line with company cost-cutting, only Amazon EC2 and Amazon RDS burstable instances should be allowed. All other services not directly supporting the company’s lean tech initiative must be blocked.
A solutions architect has been tasked with locking this down in a scalable, maintainable way aligned with AWS best practices.
What’s the most effective approach to enforce these service restrictions?

- **A.** Deploy Amazon GuardDuty to scan for unsupported AWS services and non-burstable EC2 or RDS instances. Use its findings to block non-compliant deployments automatically in the future.
- **B.** Define a custom preventive guardrail within AWS Control Tower that enforces restrictions allowing only burstable instance types to be launched, while blocking access to any non-essential services. Assign this control to the target development OU to ensure policy compliance across applicable accounts.
- **C.** Enable AWS Trusted Advisor's cost optimization checks in each development account to enforce the usage of burstable instances and prevent launching non-approved services.
- **D.** Set up a custom detective guardrail in AWS Control Tower to monitor the environment for compliance, ensuring that only burstable instances are provisioned and that any usage of unauthorized services is flagged. Link this control to the corresponding OU to track adherence across associated accounts.

---

## Q60

An IT company wants to move all its clients belonging to the regulated and security-sensitive industries such as financial services and healthcare to the AWS Cloud as it wants to leverage the out-of-box security-specific capabilities offered by AWS. The Security team at the company is developing a framework to validate the adoption of AWS best practices and industry-recognized compliance standards. The AWS Management Console is the preferred method for the in-house teams wanting to provision resources. You have been hired as an AWS Certified Solutions Architect Professional to spearhead this strategic initiative.

Which of the following strategies would you adopt to address these business requirements for continuously assessing, auditing and monitoring the configurations of AWS resources? (Select two)

- **A.** Leverage CloudTrail integration with SNS to automatically notify unauthorized API activities. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services. Use Lambda functions to automatically revert non-authorized changes in AWS resources
- **B.** Leverage EventBridge events near-real-time capabilities to monitor system events patterns to trigger Lambda functions to automatically revert non-authorized changes in AWS resources. Send notifications via SNS topics to improve the incidence response time
- **C.** Leverage Config rules to audit changes to AWS resources and monitor the compliance of the configuration by running the evaluations for the rule at a frequency that you choose. Develop AWS Config custom rules to establish a test-driven development approach by triggering the evaluation when any resource that matches the rule's scope changes in configuration
- **D.** Enable trails and set up CloudTrail events to review and monitor management activities of all AWS accounts by logging these activities into CloudWatch Logs using a KMS key. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services
- **E.** Leverage CloudWatch Logs agent to collect all the AWS SDK logs. Search the log data using a pre-defined set of filter patterns that match mutating API calls. Use CloudWatch alarms to send notifications via SNS when unintended changes are performed. Archive log data by using a batch export to Amazon S3 and analyze via Athena

---

## Q61

A development team is designing a system on AWS that will leverage Amazon CloudFront for content caching and for protecting the underlying origin. The team has flagged a concern regarding a probable attack on the origin server IP addresses, despite it being served by CloudFront.

As an AWS Certified Solutions Architect Professional, which of the following would you recommend as the BEST solution for providing the strongest level of protection to the origin server?

- **A.** Configure an AWS Lambda@Edge function to validate that the traffic to the Application Load Balancer originates from CloudFront
- **B.** Configure private access to content by using special CloudFront signed URLs or signed cookies
- **C.** Configure Origin Access Identity(OAI) on the origin server, which will only allow requests originating from CloudFront
- **D.** Configure CloudFront to use a custom header and configure an AWS WAF rule on the origin’s Application Load Balancer to accept only traffic that contains that header

---

## Q62

A game development startup runs a multiplayer gaming platform powered by Amazon EC2 instances and AWS Lambda functions. The EC2 fleet supports always-on services like matchmaking and leaderboards, which run under a consistent and stable workload. In contrast, Lambda functions are triggered by unpredictable, bursty events like player actions, achievements, or chat messages.
To keep gameplay smooth and responsive, the platform uses a high-performance caching layer backed by Amazon MemoryDB for Redis, with dedicated MemoryDB cache nodes storing session data and player stats.
An AWS solutions architect is tasked with designing a cost-optimized infrastructure that cuts down on monthly operating costs without sacrificing performance.
What is the most cost-effective strategy to meet these goals?

- **A.** Use an EC2 instance Savings Plan to commit to the EC2 compute resources financially. Apply a Compute Savings Plan to offset the baseline utilization of Lambda functions. Allocate reserved nodes to provision capacity for the MemoryDB cache nodes.
- **B.** Leverage On-Demand pricing across all services to maintain flexibility. Use Lambda provisioned concurrency for better performance. Rely on auto-scaling EC2 instances instead of committing to Savings Plans.
- **C.** Use a Compute Savings Plan to cover EC2, Lambda, and MemoryDB usage in a single commitment. Configure Lambda reserved concurrency to manage unpredictable workloads. Provision MemoryDB cache nodes by acquiring reserved nodes to ensure dedicated capacity.
- **D.** Use EC2 Spot Instances to reduce compute costs for matchmaking and leaderboard services. Use On-Demand Lambda execution. Replace MemoryDB with Amazon ElastiCache.

---

## Q63

An Internet-of-Things (IoT) company is using Kinesis Data Streams (KDS) to process IoT data from field devices. Multiple consumer applications are using the incoming data streams and the engineers have noticed a performance lag for the data delivery speed between producers and consumers of the data streams.

As a Solutions Architect Professional, which of the following would you recommend to improve the performance for the given use-case?

- **A.** Swap out Kinesis Data Streams with SQS FIFO queues to support the desired read throughput for the downstream applications
- **B.** Swap out Kinesis Data Streams with Kinesis Data Firehose to support the desired read throughput for the downstream applications
- **C.** Swap out Kinesis Data Streams with SQS Standard queues to support the desired read throughput for the downstream applications
- **D.** Use Enhanced Fanout feature of Kinesis Data Streams to support the desired read throughput for the downstream applications

---

## Q64

The product team at a global IoT technology company is looking to build features to facilitate better collaboration with the company's customers. As part of its research, the product team has figured out a market need to support both stateful and stateless client-server communications via the APIs developed using its platform.

You have been hired by the company as an AWS Certified Solutions Architect Professional to build a solution to fulfill this market need using AWS API Gateway. Which of the following would you recommend to the company?

- **A.** API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server
- **B.** API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server
- **C.** API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server
- **D.** API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server

---

## Q65

A supply-chain manufacturing company manages its AWS resources in an Elastic Beanstalk environment. For implementing a new security requirement, the company needs to assign a single static IP address to a load-balanced Elastic Beanstalk environment. Subsequently, this IP address will be used to uniquely identify traffic coming from the Elastic Beanstalk environment.

As a solutions architect, which of the following would you recommend as the BEST solution that requires minimal maintenance?

- **A.** Use a Bastion host to map multiple IP addresses into a single publicly exposed IP address
- **B.** Use a Network Address Translation (NAT) instance to map multiple IP addresses into a single publicly exposed IP address
- **C.** Use a Network Address Translation (NAT) gateway to map multiple IP addresses into a single publicly exposed IP address
- **D.** Attach the same Elastic IP to all instances to obtain a single publicly exposed IP address

---

## Q66

A multi-national digital media company wants to exit out of the business of owning and maintaining its own IT infrastructure so it can redeploy resources toward innovation in Artificial Intelligence and related areas to create a better customer experience. As part of this digital transformation, the media company wants to archive about 9 PB of data in its on-premises data center to durable long term storage.

As a Solutions Architect Professional, what is your recommendation to migrate and store this data in the quickest and MOST cost-optimal way?

- **A.** Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data directly into AWS Glacier
- **B.** Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier
- **C.** Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier
- **D.** Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data directly into AWS Glacier

---

## Q67

A web application is hosted on a fleet of Amazon EC2 instances running behind an Application Load Balancer (ALB). A custom functionality has mandated the need for a static IP address for the ALB.

As a solutions architect, how will you implement this requirement while keeping the costs to a minimum?

- **A.** Configure Gateway Load Balancer in front of the Application Load Balancer to provide a static IP address for the ALB
- **B.** An Elastic IP can be registered to an Application Load Balancer only during the creation. Re-create the ALB with the new Elastic IP and switch the workload to the newly created ALB
- **C.** Register the Application Load Balancer behind a Network Load Balancer that will provide the necessary static IP address to the ALB
- **D.** Configure Global Accelerator in front of the Application Load Balancer to provide a static IP address for the ALB

---

## Q68

An e-commerce company runs its flagship website on its on-premises Linux servers. Recently, the company suffered outages after announcing huge discounts on its website. The web tier of the application is fronted by Elastic Load Balancer while the database tier is built on RDS MYSQL database. The company is planning to run heavy discounts for the upcoming holiday sales season. The company is looking for a solution to avoid any similar outages as well as quickly ramp up the ability to handle huge traffic spikes.

As an AWS Certified Solutions Architect Professional, which of the following would you suggest as the most optimal solution that can enhance the application's capabilities to handle the sudden spikes in user traffic without significant development effort?

- **A.** Create a CloudFront distribution and configure CloudFront to cache objects from a custom origin. This will offload some traffic from the on-premises servers. Customize CloudFront cache behavior by setting Time To Live (TTL) to suit your business requirement
- **B.** Change the application architecture to use Docker containers and redeploy on AWS with ECS
- **C.** Create an S3 bucket and configure it for website hosting. Migrate your DNS to Route53 and leverage Route53 DNS failover to failover to the S3 hosted website
- **D.** Lift and Shift the application using AWS Elastic Beanstalk to enhance the scalability of the application without any downtime on the existing one

---

## Q69

A cloud-native enterprise manages its environments using AWS Organizations within a multi-account structure. As part of the container-based architecture, the team packages workloads into Docker images and stores these in Amazon Elastic Container Registry (Amazon ECR).
These images must remain accessible only to accounts in the same AWS Organization. The images are pushed via a CI/CD process, which runs multiple times daily. The company wants to retain all tagged images while limiting untagged images to the five most recent ones to reduce storage costs.
The company prefers a solution that minimizes operational overhead, securely manages access, and ensures that only required ECR operations are permitted.
Which approach best meets the company’s goals with the LEAST operational burden?

- **A.** Provision a public repository in ECR and apply a permissions policy scoped to essential ECR operations. Use the aws:PrincipalOrgID condition key to enforce organization-wide access control. Design an AWS Step Functions workflow to retain all tagged images and remove older untagged ones, keeping just the latest five.
- **B.** Configure a public ECR repository with limited permissions via a policy that employs the aws:PrincipalIsAWSService condition key for organizational restrictions. Set up an Amazon ECS Scheduled Task that retains all tagged images and automatically purges untagged images, ensuring only the five most recent remain.
- **C.** Create a private ECR repository and define a permissions policy that allows only the required ECR operations, with a condition using the aws:PrincipalOrgID key to restrict access to the organization. Apply a lifecycle rule to the repository to retain all tagged images and delete untagged images beyond the most recent five.
- **D.** Set up a private ECR repository and attach a permissions policy restricting access based on the aws:PrincipalIsAWSService condition key, allowing only the necessary ECR actions. Use an AWS Glue job to keep all tagged images while routinely cleaning up untagged ones, preserving only the five most recent ones.

---

## Q70

The DevOps team at a leading social media company uses Chef to automate the configurations of servers in the on-premises data center. The CTO at the company now wants to migrate the IT infrastructure to AWS Cloud with minimal changes to the server configuration workflows and at the same time account for less operational overhead post-migration to AWS. The company has hired you as an AWS Certified Solutions Architect Professional to recommend a solution for this migration.

Which of the following solutions would you recommend to address the given use-case?

- **A.** Replatform the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS
- **B.** Replatform the IT infrastructure to AWS Cloud by leveraging AWS Config as a configuration management service to automate the configurations of servers on AWS
- **C.** Rehost the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS
- **D.** Rehost the IT infrastructure to AWS Cloud by leveraging AWS Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS

---

## Q71

A media company has its users accessing the content from different platforms including mobile, tablet, and desktop. Each platform is customized to provide a different user experience based on various viewing modes. Path-based headers are used to serve the content for different platforms, hosted on different Amazon EC2 instances. An Auto Scaling group (ASG) has also been configured for the EC2 instances to ensure that the solution is highly scalable.

Which of the following combination of services can help minimize the cost while maximizing the performance? (Select two)

- **A.** Network Load Balancer
- **B.** Amazon Route 53 with traffic flow policies
- **C.** Application Load Balancer
- **D.** Amazon S3 configured as a static website
- **E.** Amazon CloudFront with Lambda@Edge

---

## Q72

A financial services firm intends to migrate its IT operations to AWS. The security team is establishing a framework to ensure that AWS best practices are being followed. AWS management console is the only way used by the IT teams to provision AWS resources. As per the firm's compliance requirements, the AWS resources need to be maintained in a particular configuration and audited regularly for unauthorized changes.

As an AWS Certified Solutions Architect Professional, how will you implement this requirement? (Select two)

- **A.** Leverage Systems Manager to view and control your infrastructure on AWS, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS infrastructure. Use SNS topics to enable notifications and improve the response time of incident responses
- **B.** Leverage CloudWatch Logs agent to aggregate all the AWS SDK logs. Analyze the log data using a pre-defined set of filter patterns that match any changes in the API calls. Trigger notifications via Amazon CloudWatch alarms when unintended changes are performed
- **C.** Leverage AWS Config rules for auditing changes to AWS resources periodically and monitor the compliance of the configuration. Set up AWS Config custom rules using AWS Lambda to create a test-driven development approach, and finally automate the evaluation of configuration changes against the required controls
- **D.** Leverage EventBridge events to monitor and evaluate system events patterns, and trigger AWS Lambda functions to automatically revert non-authorized changes in AWS resources. Use SNS topics to enable notifications and improve the response time of incident responses
- **E.** Leverage AWS CloudTrail events to review management activities of all AWS accounts. Make sure that CloudTrail is enabled in all accounts for the available AWS services. Enable CloudTrail trails and encrypt CloudTrail event log files with an AWS KMS key and monitor the recorded events via CloudWatch Logs

---

## Q73

A leading Internet-of-Things (IoT) solutions company needs to develop a platform that would analyze real-time clickstream events from embedded sensors in consumer electronic devices. The company has hired you as an AWS Certified Solutions Architect Professional to consult the engineering team and develop a solution using the AWS Cloud. The company wants to use clickstream data to perform data science, develop algorithms, and create visualizations and dashboards to support the business stakeholders. Each of these groups would work independently and would need real-time access to this clickstream data for their applications.

Which of the following options would provide a highly available and fault-tolerant solution to capture the clickstream events from the source and also provide a simultaneous feed of the data stream to the downstream applications?

- **A.** Use AWS Kinesis Data Analytics to facilitate multiple applications consume and analyze same streaming data concurrently and independently
- **B.** Use AWS Kinesis Data Firehose to allow applications to consume the same streaming data concurrently and independently
- **C.** Use AWS Kinesis Data Streams to facilitate multiple applications consume same streaming data concurrently and independently
- **D.** Use Amazon SQS to facilitate multiple applications process same streaming data concurrently and independently

---

## Q74

A web application is running on a fleet of Amazon EC2 instances that are configured to operate in an Auto Scaling group (ASG). The instances are fronted by an Elastic Load Balancer (ELB). To enhance the system performance, a new Amazon Machine Image (AMI) was created and the ASG was configured to use the new AMI. However, after the production deployment, users complained of aberrations in the expected application functionality. A cross-check on the ELB has confirmed that all the instances are healthy and running as expected.

As a solutions architect, which option would you suggest to rectify these issues and guarantee that later deployments are successful?

- **A.** Configure the ASG to use Elastic Load Balancing (ELB) health checks in place of EC2 status checks
- **B.** Configure the ASG to use multiple Availability Zones. When an instance becomes unhealthy, the ASG maintains the desired capacity by distributing instances across these Availability Zones. This configuration helps in better application availability and reduces errors cropping from network connectivity issues
- **C.** Configure the ASG to a maximum capacity of 3 times the actual needed size. With this configuration, the ASG will terminate unhealthy instances and launch new ones quickly to maintain an optimum number of instances to meet user requirements
- **D.** Create a new ASG launch configuration that uses the newly created AMI. Double the size of the ASG and allow the new instances to become healthy and then reduce the ASG back to the original size. If the new instances do not work as expected, associate the ASG with the old launch configuration

---

## Q75

An e-commerce company manages its flagship application on a load-balanced EC2 instance fleet for web hosting, database API services, and business logic. This tightly coupled architecture makes it inflexible for new feature additions while also making the architecture less scalable.

Which of the following options can be used to decouple the architecture, improve scalability and provide the ability to track the failed orders?

- **A.** Configure Amazon S3 for hosting the web application while using AWS AppSync for database access services. Use Amazon Simple Queue Service (Amazon SQS) for queuing orders and AWS Lambda for business logic. Use Amazon SQS dead-letter queue for tracking and re-processing failed orders
- **B.** Use AWS Elastic Beanstalk for hosting the web application and Amazon API Gateway for database API services. Use Kinesis Data Streams for queuing orders and AWS Lambda to build business logic. Configure an Amazon S3 bucket for retaining failed orders on an hourly basis
- **C.** Configure Amazon CloudFront for hosting the website and Amazon API Gateway for database API services. Use Amazon Simple Queue Service (Amazon SQS) for order queuing and AWS Lambda for business logic. Use Amazon SQS long polling for retaining failed orders
- **D.** Use Amazon Lightsail for web hosting with AWS AppSync for database API services. Use Simple Queue Service (Amazon SQS) for order queuing. Use Amazon Elastic Container Service (Amazon ECS) for business logic and use the visibility timeout parameter of Amazon SQS to retain the failed orders

---
