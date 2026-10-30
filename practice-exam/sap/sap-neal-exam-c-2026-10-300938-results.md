# Neal Exam C — final check, 35 questions (2026-10-30 09:38)

**Kết quả:** 25/35 câu đúng (71.42%)

**Time used:** 1:34:17 · **Flagged:** 2, 3, 6, 8, 18, 20, 22, 27, 31

| Domain | Score |
|---|---|
| CSAP – Design Solutions for Organizational Complexity | 66.67% |
| CSAP – Design for New Solutions | 80% |
| CSAP – Continuous Improvement for Existing Solutions | 53.85% |
| CSAP – Accelerate Workload Migration and Modernization | 83.33% |

## ⏱ Timing

- Avg per question 2:41 · single 2:37 · multi 2:58 · right 2:37 · wrong 2:51
- Answered 25 at 60:19 · 50 at — · 35 at 85:54 (exam clock) · >3 min: 12 q · changed answer: 16 q (5 ended wrong)
- Slowest: Q18 5:18✓ · Q24 4:46✓ · Q31 3:51✗ · Q20 3:49✗ · Q1 3:45✓ · Q19 3:42✗ · Q3 3:37✓ · Q25 3:35✓ · Q13 3:18✗ · Q11 3:16✗
- First-answer order: 2 3 5 6 7 8 9 10 14 15 16 17 18 19 22 23 24 25 26 27 30 31 32 33 34 35 1 4 11 12 13 20 21 28 29

## Câu 1 — ✅ ĐÚNG

<!-- source: T3Q25 · domain: CI · time: 3:45 · first: 65:29 · visits: 2 · changes: 1 -->

### Câu hỏi

A security team uses a ticketing system to capture suspicious events that require investigation. The security team has created a system where events are captured using CloudTrail Logs and saved to Amazon S3. A scheduled AWS Lambda function then uses Amazon Athena to query the logs for any API actions performed by the root user. The results are then submitted to the ticketing system by the Lambda function.
The ticketing system has a monthly 4-hour maintenance window when the system is offline and cannot log new tickets and an audit revealed that several tickets were not created due to the ticketing system being unavailable.
Which combination of steps should a solutions architect take to ensure that the incidents are reported to the ticketing system even during planned maintenance? (Select TWO.)

### Các phương án

- **A.** Create an Amazon SNS topic to which Amazon CloudWatch alarms will be published. Configure a CloudWatch alarm to invoke the Lambda function.
- **B.** Create an Amazon SQS queue to which Amazon CloudWatch alarms will be published. Configure a CloudWatch alarm to publish to the SQS queue.
- **C.** Update the Lambda function to be triggered by messages published to an Amazon SNS topic. Update the existing application code to retry every 5 minutes if the ticketing system's API endpoint is unavailable.
- **D.** Update the Lambda function to poll the Amazon SQS queue for messages and to return successfully when the ticketing system API has processed the request.
- **E.** Create an Amazon EventBridge rule with a pattern that looks for AWS CloudTrail events where the API calls involve the root user account. Configure an Amazon SQS queue as a target for the rule.

> **Bạn chọn:** D, E
> **Đáp án đúng:** D, E

### Giải thích

The existing system can be modified to use Amazon EventBridge instead of using AWS CloudTrail with Amazon Athena. Eventbridge can be configured with a rule that checks all AWS API calls via CloudTrail. The rule can be configured to look for the usage or the root user account. Eventbridge can then be configured with an Amazon SQS queue as a target that puts a message in the queue waiting to be processed.
The Lambda function can then be configured to poll the queue for messages (event-source mapping), process the event synchronously and only return a successful result when the ticketing system has processed the request. The message will be deleted only if the result is successful, allowing for retries.
This system will ensure that the important events are not missed when the ticketing system is unavailable.
CORRECT:
"Create an Amazon EventBridge rule with a pattern that looks for AWS CloudTrail events where the API calls involve the root user account. Configure an Amazon SQS queue as a target for the rule" is a correct answer.
CORRECT:
"Update the Lambda function to poll the Amazon SQS queue for messages and to return successfully when the ticketing system API has processed the request" is also a correct answer.
INCORRECT:
"Update the Lambda function to be triggered by messages published to an Amazon SNS topic. Update the existing application code to retry every 5 minutes if the ticketing system's API endpoint is unavailable" is incorrect. SNS does not store messages so if the Lambda function is unable to successfully process the message it will be lost.
INCORRECT:
"Create an Amazon SNS topic to which Amazon CloudWatch alarms will be published. Configure a CloudWatch alarm to invoke the Lambda function" is incorrect. SQS should be used instead of SNS as SNS will not store messages for subsequent attempts at processing.
INCORRECT:
"Create an Amazon SQS queue to which Amazon CloudWatch alarms will be published. Configure a CloudWatch alarm to publish to the SQS queue" is incorrect. EventBridge rules should be used (CloudWatch Events) as they can look for patterns in events. CloudWatch alarms will alarm based on metrics.
References:
https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-application-integration-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 2 — ✅ ĐÚNG

<!-- source: T2Q24 · domain: CI · flagged · time: 2:58 · first: 2:07 · visits: 3 · changes: 0 -->

### Câu hỏi

An application runs on an Amazon EC2 instance with an attached Amazon EBS Provisioned IOPS (PIOPS) volume. The volume is configured at 200-GB in size and has 3,000 IOPS provisioned. The application requires low latency and random access to the data. A Solutions Architect has been asked to consider options for lowering the cost of the storage without impacting performance and durability.
What should the Solutions Architect recommend?

### Các phương án

- **A.** Change the PIOPS volume for a 1-TB EBS General Purpose SSD (gp2) volume.
- **B.** Change the PIOPS volume for a 1-TB Throughput Optimized HDD (st1) volume.
- **C.** Create an Amazon EFS file system with the performance mode set to Max I/O. Mount the EFS file system to the EC2 operating system.
- **D.** Create an Amazon EFS file system with the throughput mode set to Provisioned. Mount the EFS file system to the EC2 operating system.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

The most cost-effective solution is to use an Amazon EBS General Purpose SSD (gp2) volume. The volume should be configured with 1-TB as gp2 volumes provide 3 IOPS per GB, which will allow the full 3,000 IOPS to be achieved.
CORRECT:
"Change the PIOPS volume for a 1-TB EBS General Purpose SSD (gp2) volume" is the correct answer.
INCORRECT:
"Change the PIOPS volume for a 1-TB Throughput Optimized HDD (st1) volume" is incorrect. This volume type supports a maximum of 500 IOPS per volume.
INCORRECT:
"Create an Amazon EFS file system with the performance mode set to Max I/O. Mount the EFS file system to the EC2 operating system" is incorrect. EFS will be much more expensive than using a gp2 volume.
INCORRECT:
"Create an Amazon EFS file system with the throughput mode set to Provisioned. Mount the EFS file system to the EC2 operating system" is incorrect. EFS will be much more expensive than using a gp2 volume.
References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

## Câu 3 — ✅ ĐÚNG

<!-- source: T4Q14 · domain: NEW · flagged · time: 3:37 · first: 5:10 · visits: 2 · changes: 1 -->

### Câu hỏi

A company runs a two-tier application that uses EBS-backed Amazon EC2 instances in an Auto Scaling group and an Amazon Aurora PostgreSQL database. The company intends to use a pilot light approach for disaster recovery in a different AWS Region. The company has an RTO of 6 hours and an RPO of 24 hours.
Which solution would achieve the requirements with MINIMAL cost?

### Các phương án

- **A.** Use AWS Lambda to create daily EBS snapshots and copy them to the disaster recovery Region. Implement an Aurora Replica in the DR Region. Use Amazon Route 53 with an active-passive failover configuration. Use Amazon EC2 in an Auto Scaling group with the capacity set to 0 in the disaster recovery Region.
- **B.** Use EBS cross-region snapshot copy capability to create snapshots in the disaster recovery (DR) Region. Implement an Aurora Replica in the DR Region. Use Amazon Route 53 with an active-passive failover configuration. Use Amazon EC2 in an Auto Scaling group configured the same as the primary Region.
- **C.** Use EBS and RDS cross-Region snapshot copy capability to create snapshots in the disaster recovery (DR) Region. Use Amazon Route 53 with an active-active failover configuration. Use Amazon EC2 in an Auto Scaling group with the capacity set to 0 in the disaster recovery Region.
- **D.** Use AWS Lambda to create daily EBS and RDS snapshots and copy them to the disaster recovery Region. Use Amazon Route 53 with an active-active failover configuration. Use Amazon EC2 in an Auto Scaling group configured the same as the primary Region.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

> ⚠️ A cross-Region Aurora replica is not auto-promoted; promotion is manual (or use Global Database failover).

The correct answer must be the lowest cost option that delivers the RPO and RTO requirements and is in line with a pilot light strategy. Please note the AWS definition of a pilot light scenario:
“In this DR approach, you simply replicate part of your IT structure for a limited set of core services so that the AWS cloud environment seamlessly takes over in the event of a disaster. A small part of your infrastructure is always running simultaneously syncing mutable data (as databases or documents), while other parts of your infrastructure are switched off and used only during testing. Unlike a backup and recovery approach, you must ensure that your most critical core elements are already configured and running in AWS (the pilot light).”
The mutable data in this case is the Aurora database so this should be running in the DR Region. The best way to achieve that is to create an Aurora replica in the DR Region. This increases cost compared to replicating snapshots but is in line with the pilot light strategy.
For the EC2 instances AWS Lambda can be used to automate the replication of snapshots to the DR Region. These can be daily snapshots as the RPO is 24 hours. Auto Scaling can be configured with the capacity set to 0 and Route 53 failover records can be created in an active-passive configuration.
In the event of a disaster it would then be easy to create AMIs from the EC2 snapshots, add them to a launch config and then increase the capacity of the ASG. The Aurora Replica will automatically become a writable database and the entire configuration can be up and running well within the RTO.
CORRECT:
"Use AWS Lambda to create daily EBS snapshots and copy them to the disaster recovery Region. Implement an Aurora Replica in the DR Region. Use Amazon Route 53 with an active-passive failover configuration. Use Amazon EC2 in an Auto Scaling group with the capacity set to 0 in the disaster recovery Region" is the correct answer.
INCORRECT:
"Use EBS cross-region snapshot copy capability to create snapshots in the disaster recovery (DR) Region. Implement an Aurora Replica in the DR Region. Use Amazon Route 53 with an active-passive failover configuration. Use Amazon EC2 in an Auto Scaling group configured the same as the primary Region" is incorrect.
You cannot create snapshots of an instance in one Region directly into another Region as the wording suggests. You must create the snapshot in the same Region and then copy it across Regions. You would also not configure the ASG the same as in the primary Region as it would be more costly.
INCORRECT:
"Use EBS and RDS cross-Region snapshot copy capability to create snapshots in the disaster recovery (DR) Region. Use Amazon Route 53 with an active-active failover configuration. Use Amazon EC2 in an Auto Scaling group with the capacity set to 0 in the disaster recovery Region" is incorrect.
As above, you cannot create snapshots of an instance in one Region directly into another Region as the wording suggests. You must create the snapshot in the same Region and then copy it across Regions.
INCORRECT:
"Use AWS Lambda to create daily EBS and RDS snapshots and copy them to the disaster recovery Region. Use Amazon Route 53 with an active-active failover configuration. Use Amazon EC2 in an Auto Scaling group configured the same as the primary Region" is incorrect.
You would not configure the ASG the same as in the primary Region as it would be more costly.
References:
https://aws.amazon.com/blogs/publicsector/rapidly-recover-mission-critical-systems-in-a-disaster/
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 4 — ✅ ĐÚNG

<!-- source: T1Q7 · domain: ORG · time: 1:30 · first: 67:14 · visits: 3 · changes: 1 -->

### Câu hỏi

A company is using multiple AWS accounts. The company’s DNS records are stored in a private Amazon Route 53 hosted zone in the management account and their applications are running in a production account.
A Solutions Architect is attempting to deploy an application into the production account. The application must resolve a CNAME record set for an Amazon RDS endpoint. The CNAME record set was created in a private hosted zone in the management account.
The deployment failed to start and the Solutions Architect has discovered that the CNAME record is not resolvable on the application EC2 instance despite being correctly created in Route 53.
Which combination of steps should the Solutions Architect take to resolve this issue? (Select TWO.)

### Các phương án

- **A.** Deploy the database on a separate EC2 instance in the new VPC. Create a record set for the instance's private IP in the private hosted zone.
- **B.** Hardcode the DNS name and IP address of the RDS database instance into the /etc/resolv.conf file on the application server.
- **C.** Create an authorization to associate the private hosted zone in the management account with the new VPC in the production account.
- **D.** Create a private hosted zone for the record set in the production account. Configure Route 53 replication between AWS accounts.
- **E.** Associate a new VPC in the production account with a hosted zone in the management account. Delete the association authorization in the management account.

> **Bạn chọn:** C, E
> **Đáp án đúng:** C, E

### Giải thích

An application cannot resolve record sets created in the private hosted zone of another AWS account. The solution to this problem is to associate the Route 53 private hosted zone in the management account with the VPC in the production account.
To associate a Route 53 private hosted zone in one AWS account (Account A) with a virtual private cloud that belongs to another AWS account (Account B), follow these steps using the AWS CLI:
1. From an instance in Account A, authorize the association between the private hosted zone in Account A and the virtual private cloud in Account B.
2. From an instance in Account B, create the association between the private hosted zone in Account A and the virtual private cloud in Account B.
3. Delete the association authorization after the association is created.
CORRECT:
"Create an authorization to associate the private hosted zone in the management account with the new VPC in the production account" is a correct answer.
CORRECT:
"Associate a new VPC in the production account with a hosted zone in the management account. Delete the association authorization in the management account" is also a correct answer.
INCORRECT:
"Deploy the database on a separate EC2 instance in the new VPC. Create a record set for the instance's private IP in the private hosted zone" is incorrect. The record should be a CNAME record that points to the DNS endpoint of the RDS database, not to a private IP address.
INCORRECT:
"Hardcode the DNS name and IP address of the RDS database instance into the /etc/resolv.conf file on the application server" is incorrect. This is not a best practice as the IP address of the RDS instance should not be used, a CNAME pointing to its DNS endpoint is preferred.
INCORRECT:
"Create a private hosted zone for the record set in the production account. Configure Route 53 replication between AWS accounts" is incorrect. You cannot configure replication for hosted zones in Route 53.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/private-hosted-zone-different-account/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 5 — ❌ SAI

<!-- source: T4Q13 · domain: MIG · time: 2:49 · first: 8:02 · visits: 2 · changes: 1 -->

### Câu hỏi

A Solutions Architect has been tasked with migrating an application to AWS. The application includes a desktop client application and web application. The web application has an uptime SLA of 99.5%. The Solutions Architect must re-architect the application to meet or exceed this SLA.
The application contains a MySQL database running on a single virtual machine. The web application uses multiple virtual machines with a load balancer. Remote users complain about slow load times while using this latency-sensitive application.
The Solutions Architect must minimize changes to the application whilst improving the user experience, minimizing costs, and ensuring the availability requirements are met. Which solutions best meets these requirements?

### Các phương án

- **A.** Migrate the database to a MySQL database in Amazon EC2. Host the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Allocate an Amazon WorkSpaces WorkSpace for each end user to improve the user experience.
- **B.** Migrate the database to an Amazon RDS Aurora MySQL configuration. Host the web application on an Auto Scaling configuration of Amazon EC2 instances behind an Application Load Balancer. Use Amazon AppStream 2.0 to improve the user experience.
- **C.** Migrate the database to an Amazon EMR cluster with at least two nodes. Deploy the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Use Amazon CloudFront to improve the user experience.
- **D.** Migrate the database to an Amazon RDS MySQL Multi-AZ configuration. Host the web application on automatically scaled AWS Fargate containers behind a Network Load Balancer. Use Amazon ElastiCache to improve the user experience.

> **Bạn chọn:** D
> **Đáp án đúng:** B

### Giải thích

The uptime SLA for Amazon RDS is 99.5%. Therefore, it is not necessary to add a Multi-AZ configuration which will increase the solution cost. For the compute layer this could be containers or EC2 instances. To minimize changes to the application using EC2 instances may be slightly easier, but could work. To solve the user experience issues Amazon AppStream 2.0 should be used.
Amazon AppStream 2.0 is a fully managed non-persistent application and desktop streaming service. You centrally manage your desktop applications on AppStream 2.0 and securely deliver them to any computer. Each end user has a fluid and responsive experience because applications run on virtual machines optimized for specific use cases and each streaming sessions automatically adjust to network conditions.
CORRECT:
"Migrate the database to an Amazon RDS Aurora MySQL configuration. Host the web application on an Auto Scaling configuration of Amazon EC2 instances behind an Application Load Balancer. Use Amazon AppStream 2.0 to improve the user experience" is the correct answer.
INCORRECT:
"Migrate the database to a MySQL database in Amazon EC2. Host the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Allocate an Amazon WorkSpaces WorkSpace for each end user to improve the user experience" is incorrect. An RDS managed service would be better for the database and AppStream 2.0 is a better fit for an optimized desktop application.
INCORRECT:
"Migrate the database to an Amazon EMR cluster with at least two nodes. Deploy the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Use Amazon CloudFront to improve the user experience" is incorrect. EMR is a hosted Hadoop framework for running analytics on big data and is not suitable for this workload. CloudFront is not well suited to optimizing performance for desktop applications.
INCORRECT:
"Migrate the database to an Amazon RDS MySQL Multi-AZ configuration. Host the web application on automatically scaled AWS Fargate containers behind a Network Load Balancer. Use Amazon ElastiCache to improve the user experience" is incorrect. AppStream 2.0 is a better fit for the desktop application. ElastiCache will just improve database query performance.
References:
https://aws.amazon.com/rds/sla/
https://aws.amazon.com/appstream2/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-front-end-web-and-mobile-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 6 — ✅ ĐÚNG

<!-- source: T5Q18 · domain: NEW · flagged · time: 1:53 · first: 9:47 · visits: 2 · changes: 0 -->

### Câu hỏi

A Solutions Architect wants to make sure that only IAM users with appropriate permissions can access a new Amazon API Gateway endpoint. How can the Solutions Architect design the API Gateway access control to meet this requirement?

### Các phương án

- **A.** Set the authorization to AWS_IAM for the API Gateway method. Create a permissions policy that grants execute-api:Invoke permission on the REST API resource and attach it to a group containing the IAM user accounts.
- **B.** Create an AWS Lambda function as a custom authorizer and ask the API client to pass the key and secret when making the call, and then use Lambda to validate the key/secret pair against the IAM system.
- **C.** Set the authorization to AWS_IAM for the API Gateway method. Create a permissions policy that grants lambda:InvokeFunction permission on the REST API resource and attach it to a group containing the IAM user accounts.
- **D.** Create a client certificate for API Gateway. Distribute the certificate to the AWS users that need to access the endpoint. Enable the API caller to pass the client certificate when accessing the endpoint.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

To allow an API caller to invoke the API or refresh its caching, you must create IAM policies that permit a specified API caller to invoke the API method for which the IAM user authentication is enabled. The API developer sets the method's authorizationType property to AWS_IAM to require that the caller submit the IAM user's access keys to be authenticated. Then, you attach the policy to an IAM user representing the API caller, to an IAM group containing the user, or to an IAM role assumed by the user.
In this IAM permissions policy statement, the IAM Resource element contains a list of deployed API methods identified by given HTTP verbs and API Gateway resource paths. The IAM Action element contains the required API Gateway API executing actions. These actions include execute-api:Invoke or execute-api:InvalidateCache, where execute-api designates the underlying API execution component of API Gateway.
CORRECT:
"Set the authorization to AWS_IAM for the API Gateway method. Create a permissions policy that grants execute-api:Invoke permission on the REST API resource and attach it to a group containing the IAM user accounts" is the correct answer.
INCORRECT:
"Create an AWS Lambda function as a custom authorizer and ask the API client to pass the key and secret when making the call, and then use Lambda to validate the key/secret pair against the IAM system" is incorrect. This solution does is not a valid method of integrating the REST API with IAM.
INCORRECT:
"Set the authorization to AWS_IAM for the API Gateway method. Create a permissions policy that grants lambda:InvokeFunction permission on the REST API resource and attach it to a group containing the IAM user accounts" is incorrect. The permission that is being granted here is for invoking a Lambda function, not a REST API.
INCORRECT:
"Create a client certificate for API Gateway. Distribute the certificate to the AWS users that need to access the endpoint. Enable the API caller to pass the client certificate when accessing the endpoint" is incorrect. Client certificates are a different way to authenticate, this is not using IAM user accounts.
References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 7 — ❌ SAI

<!-- source: T3Q9 · domain: CI · time: 2:32 · first: 12:18 · visits: 1 · changes: 0 -->

### Câu hỏi

A company uses Amazon DynamoDB as the backend for the development environment of a new serverless application. While benchmarking the load, they have configured the RCU and WCU for DynamoDB based on the maximum anticipated load for peak usage.
Peak usage runs over several hours each weekend and is twice the usual load across the week. Within this duration, write operations are significant and take up most of the traffic.
The company must optimize the cost of running the application before releasing to production. Which solution will meet these requirements?

### Các phương án

- **A.** Purchase reserved RCU and WCU for the DynamoDB table and use AWS Application Auto scaling to match the increased load during the peak usage period.
- **B.** Configure on-demand capacity mode for the table to enable pay-per-request pricing for read and write requests.
- **C.** Reduce the provisioned read capacity to match the new peak load on the table and configure DynamoDB Accelerator (DAX) in front of the table.
- **D.** Configure on-demand capacity mode for the table and configure DynamoDB Accelerator (DAX) in front of the table.

> **Bạn chọn:** D
> **Đáp án đúng:** B

### Giải thích

With a manually set scaling policy, you can set the upper and low limits of the scaling. So, for example, you could set it at a minimum of 1 and a max of 20 read capacity. This would mean that no matter what you would always have at least 1 read capacity but never more than 20.
So now if you receive that same spike but have the max throughput to 20, DynamoDB will throttle those requests and prevent you from going over your max auto scaled threshold.
With On-Demand Scaling you don't need to think about provisioning throughput. Instead, your table will scale all behind the scenes automatically. Extreme spikes in load can occur and be handled seamlessly by AWS. This also brings a change in the cost structure for DynamoDB. With On-Demand Scaling, instead of paying for provisioned throughput, you pay per read or write request.
Remember for Provisioned with Auto-Scaling you are basically paying for throughput 24/7. Whereas for On-Demand Scaling you pay per request. This means for applications still in development or low traffic applications, it might be more economical to use On-Demand Scaling and not worry about provisioning throughput. However, at scale, this can quickly shift once you have a more consistent usage pattern.
CORRECT:
"Configure on-demand capacity mode for the table to enable pay-per-request pricing for read and write requests" is the correct answer (as explained above.)
INCORRECT:
"Purchase reserved RCU and WCU for the DynamoDB table and use AWS Application Auto scaling to match the increased load during the peak usage period" is incorrect.
This is a close option however extremely rapid spikes in load could still occur faster than the table could scale.
INCORRECT:
"Reduce the provisioned read capacity to match the new peak load on the table and configure DynamoDB Accelerator (DAX) in front of the table" is incorrect.
The question doesn’t ask about repeated load, hence caching isn’t appropriate in this case.
INCORRECT:
" Configure on-demand capacity mode for the table and configure DynamoDB Accelerator (DAX) in front of the table" is incorrect.
As mentioned above, since the application doesn’t have repeated load or hot data, caching isn’t appropriate in this case.
References:
https://aws.amazon.com/blogs/aws/amazon-dynamodb-on-demand-no-capacity-planning-and-pay-per-request-pricing/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-dynamodb/

## Câu 8 — ✅ ĐÚNG

<!-- source: T5Q16 · domain: CI · flagged · time: 2:21 · first: 14:29 · visits: 2 · changes: 0 -->

### Câu hỏi

A serverless application uses an AWS Lambda function behind and Amazon API Gateway REST API. During busy periods thousands of simultaneous invocations are required and requests fail multiple times before succeeding. The operations team has checked for AWS Lambda errors and did not find any. A Solutions Architect must investigate the root cause of the issue. What is the most likely cause of this problem?

### Các phương án

- **A.** The Lambda is configured with too little memory causing the function to fail at peak load.
- **B.** The Lambda function is set to use synchronous invocation and the REST API is calling the function using asynchronous invocation.
- **C.** The throttle limit on the REST API is configured too low. During busy periods some requests are being throttled and are not reaching the Lambda function.
- **D.** The API is using the non-proxy integration with Lambda when it should be using proxy integration.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Throttling can be configured for API Gateway at the stage or usage plan level. Amazon API Gateway provides two basic types of throttling-related settings:
•
Server-side throttling limits
are applied across all clients. These limit settings exist to prevent your API—and your account—from being overwhelmed by too many requests.
•
Per-client throttling limits
are applied to clients that use API keys associated with your usage policy as client identifier.
In this case it is likely that the server-side throttling limits are configured to a value that is too low for the periods of peak usage. This is causing requests to fail repeatedly before they finally make it through to the Lambda function.
This is the most likely cause of the issue as it is clear the requests are not reaching Lambda or there would be errors logged by the function.
CORRECT:
"The throttle limit on the REST API is configured too low. During busy periods some requests are being throttled and are not reaching the Lambda function" is the correct answer.
INCORRECT:
"The Lambda is configured with too little memory causing the function to fail at peak load" is incorrect. If this was the case we would see errors being logged by Lambda but there aren’t any.
INCORRECT:
"The Lambda function is set to use synchronous invocation and the REST API is calling the function using asynchronous invocation" is incorrect. API Gateway can be configured to invoke a Lambda function both synchronously and asynchronously.
INCORRECT:
"The API is using the non-proxy integration with Lambda when it should be using proxy integration" is incorrect. API Gateway can be configured to connect to Lambda using both proxy and non-proxy integrations.
References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 9 — ❌ SAI

<!-- source: T5Q1 · domain: CI · time: 2:09 · first: 15:50 · visits: 2 · changes: 0 -->

### Câu hỏi

A company has a security policy that requires that all internal application connectivity must use private IP addresses. A Solutions Architect has created interface endpoints in private subnets to connect to AWS public services. The Solutions Architect tested the configuration and the connectivity failed.
Which configuration change should the Solutions Architect make to resolve the issue?

### Các phương án

- **A.** Update the route table for the subnets with a route to the interface endpoint.
- **B.** Enable the private DNS option on the VPC attributes.
- **C.** Configure the security group on the interface endpoint to allow connectivity to the AWS services.
- **D.** Configure an Amazon Route 53 private hosted zone with a conditional forwarder for the internal application.

> **Bạn chọn:** A
> **Đáp án đúng:** C

### Giải thích

You must ensure that the security group that's associated with the endpoint network interface allows communication between the endpoint network interface and the resources in your VPC that communicate with the service.
When you create an interface endpoint, endpoint-specific DNS hostnames are generated. For AWS services and AWS Marketplace Partner services, the private DNS option (enabled by default) associates a private hosted zone with your VPC.
The hosted zone contains a record set for the default DNS name for the service (for example, ec2.us-east-1.amazonaws.com) that resolves to the private IP addresses of the endpoint network interfaces in your VPC. This enables you to make requests to the service using its default DNS hostname instead of the endpoint-specific DNS hostnames.
With Private DNS enabled on the endpoint, instances can send requests AWS services through the interface endpoint using either the default DNS hostname or the endpoint-specific DNS hostname.
CORRECT:
"Configure the security group on the interface endpoint to allow connectivity to the AWS services" is the correct answer.
INCORRECT:
"Enable the private DNS option on the VPC attributes" is incorrect. Private DNS is enabled by default for endpoints created for AWS services and AWS Marketplace Partner services.
INCORRECT:
"Update the route table for the subnets with a route to the interface endpoint" is incorrect. You do not need to update the route table for interface endpoints.
INCORRECT:
"Configure an Amazon Route 53 private hosted zone with a conditional forwarder for the internal application" is incorrect. This is unnecessary, a private hosted zone is a private hosted zone is associated with the VPC by default when the private DNS option is enabled (which is a default).
References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html
https://docs.aws.amazon.com/vpc/latest/userguide/verify-domains.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 10 — ✅ ĐÚNG

<!-- source: T3Q17 · domain: CI · time: 1:39 · first: 17:34 · visits: 1 · changes: 0 -->

### Câu hỏi

A financial services company is looking to enhance its web application deployment process to ensure rapid and safe updates. The application, which handles sensitive financial transactions, is hosted on a cluster of Amazon EC2 instances behind an Application Load Balancer (ALB). The source code is maintained in a Bitbucket repository, and they use AWS CodeBuild for building the application. The company plans to integrate AWS CodePipeline for automating the deployment process from Bitbucket commits.
The key requirements are to minimize downtime during updates and provide a mechanism for quick rollback in case the new version introduces bugs or security vulnerabilities.
Which CI/CD setup would best fulfill these requirements?

### Các phương án

- **A.** Configure CodePipeline with a deployment stage using AWS CodeDeploy for blue/green deployments. After deploying the new version, monitor its performance and security, and use CodeDeploy's rollback feature in case of any issues.
- **B.** Configure CodePipeline to deploy using AWS Elastic Beanstalk with rolling updates. Continuously monitor the application, and manually redeploy the previous version if problems are detected.
- **C.** Configure CodePipeline with a deployment stage that uses AWS CloudFormation to manage separate stacks for testing and production. Monitor the application post-deployment, and push updates if issues arise.
- **D.** Configure CodePipeline to deploy through AWS OpsWorks using rolling deployments. Keep an eye on the new deployment and revert to a previous stack configuration if necessary.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

AWS CodeDeploy's blue/green deployment method is ideal for this scenario. It allows the new version of the application to be deployed alongside the old version, ensuring minimal downtime. Traffic is gradually shifted from the old version to the new version, allowing for monitoring and quick rollback if needed.
This approach is particularly suitable for applications where reliability and quick recovery are crucial, such as financial services applications. CodeDeploy's built-in rollback capabilities provide an additional safety net, ensuring that the application can quickly revert to the previous stable version if the new deployment introduces any critical issues.
CORRECT:
"Configure CodePipeline with a deployment stage using AWS CodeDeploy for blue/green deployments. After deploying the new version, monitor its performance and security, and use CodeDeploy's rollback feature in case of any issues" is the correct answer (as explained above.)
INCORRECT:
"Configure CodePipeline to deploy using AWS Elastic Beanstalk with rolling updates. Continuously monitor the application, and manually redeploy the previous version if problems are detected" is incorrect.
While Elastic Beanstalk supports rolling updates, this method involves replacing instances with new versions, which can cause temporary downtime and does not provide as immediate a rollback mechanism as blue/green deployments.
INCORRECT:
"Configure CodePipeline with a deployment stage that uses AWS CloudFormation to manage separate stacks for testing and production. Monitor the application post-deployment, and push updates if issues arise" is incorrect.
Using CloudFormation for managing separate stacks is more about infrastructure management and does not inherently provide the rapid deployment and quick rollback capabilities of blue/green deployments.
INCORRECT:
"Configure CodePipeline to deploy through AWS OpsWorks using rolling deployments. Keep an eye on the new deployment and revert to a previous stack configuration if necessary" is incorrect.
OpsWorks offers more control over the configuration of the application stack but does not specialize in minimizing downtime or quick rollback in the same way as blue/green deployments in CodeDeploy.
References:
https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-developer-tools/

## Câu 11 — ❌ SAI

<!-- source: T6Q26 · domain: NEW · time: 3:16 · first: 68:55 · visits: 2 · changes: 0 -->

### Câu hỏi

A business is in the process of setting up an Amazon Elastic Kubernetes Service (Amazon EKS) cluster to manage a specific workload. This workload is expected to generate a highly variable number of stateless pods, with a significant number of these pods being launched in a brief timeframe due to automatic scaling of replicas.
What approach should be taken to optimize the resilience of the nodes in this scenario?

### Các phương án

- **A.** Implement a distinct launch template for deploying the EKS control plane in a secondary cluster, separate from the node groups that handle the workload.
- **B.** Modify the node groups for the workload by reducing the number of node groups but opting for larger instances within these groups.
- **C.** Set up the Kubernetes Cluster Autoscaler to maintain the compute capacity of the workload node groups at a consistently under provisioned level.
- **D.** Adjust the workload configuration to utilize topology spread constraints based on different Availability Zones.

> **Bạn chọn:** C
> **Đáp án đúng:** D

### Giải thích

Using topology spread constraints based on Availability Zones is a strategic approach to enhance node resilience in an Amazon EKS cluster.
This method ensures that the pods are evenly distributed across different Availability Zones.
By doing so, it reduces the risk of a significant impact on the workload if one Availability Zone experiences issues, thereby maximizing node resilience and ensuring better fault tolerance and high availability.
CORRECT:
"Adjust the workload configuration to utilize topology spread constraints based on different Availability Zones" is the correct answer (as explained above.)
INCORRECT:
"Implement a distinct launch template for deploying the EKS control plane in a secondary cluster, separate from the node groups that handle the workload" is incorrect.
Deploying a separate EKS control plane in a different cluster does not directly contribute to the resilience of the nodes within the workload node groups. The control plane's location and configuration are more about management and orchestration rather than node resilience.
INCORRECT:
"Modify the node groups for the workload by reducing the number of node groups but opting for larger instances within these groups" is incorrect.
Using fewer node groups with larger instances might improve performance but does not necessarily maximize node resilience. Larger instances can still be susceptible to zone-specific issues, and having fewer groups could reduce the distribution and fault tolerance capabilities.
INCORRECT:
"Set up the Kubernetes Cluster Autoscaler to maintain the compute capacity of the workload node groups at a consistently under provisioned level" is incorrect.
Keeping the compute capacity of the workload node groups under provisioned is counterproductive for maximizing node resilience. Under provisioning can lead to insufficient resources during peak demand, potentially causing performance issues or even service disruptions.
References:
https://aws.github.io/aws-eks-best-practices/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-ecs-and-eks/

## Câu 12 — ❌ SAI

<!-- source: T4Q5 · domain: NEW · time: 3:03 · first: 70:14 · visits: 2 · changes: 4 -->

### Câu hỏi

A media publishing company has created an online bookstore which gives users access to books and other reference material. These materials can be downloaded by users and new materials can also be uploaded on the portal. According to company requirements, all data must be encrypted in transit and at rest. A solutions architect is building the solution by using Amazon S3 and Amazon CloudFront.
Which combination of steps will meet the encryption requirements? (Select THREE.)

### Các phương án

- **A.** Turn on the S3 server-side encryption for the S3 bucket in use.
- **B.** For the read and write operations in the S3 ACLs, add condition "aws:SecureTransport": "true".
- **C.** Create a bucket policy that denies any unencrypted operations in the S3 bucket that the web application uses.
- **D.** Configure encryption at rest on CloudFront by using server-side encryption with AWS KMS keys (SSE-KMS).
- **E.** Configure redirection of HTTP requests to HTTPS requests in CloudFront.
- **F.** Use the RequireSSL option in the creation of presigned URLS for the S3 bucket that the web application uses

> **Bạn chọn:** A, B, E
> **Đáp án đúng:** A, C, E

### Giải thích

For object encryption at rest, you can set the default encryption behavior on an Amazon S3 bucket so that all objects are encrypted when they are stored in the bucket. The objects are encrypted using server-side encryption with either Amazon S3-managed keys (SSE-S3) or AWS Key Management Service (AWS KMS) keys.
To deny unencrypted objects, "s3:x-amz-server-side-encryption" can be added which allows only encrypted object upload and can restrict to a specific KMS key as well.
Amazon CloudFront can use 301 response code to redirect HTTP requests to HTTPS and allows only secured traffic.
CORRECT:
"Turn on S3 server-side encryption for the S3 bucket that the web application uses is a correct answer (as explained above.)
CORRECT:
"Create a bucket policy that denies any unencrypted operations in the S3 bucket that the web application uses" is also a correct answer (as explained above.)
CORRECT:
"Configure redirection of HTTP requests to HTTPS requests in CloudFront" is also a correct answer (as explained above.)
INCORRECT:
"For the read and write operations in the S3 ACLs , add condition "aws:SecureTransport": "true"" is incorrect.
To only allow HTTPS requests, set “true” for key "aws:SecureTransport". When this key is true, the request is sent through HTTPS. This option configures encryption in transit and does not enforce encryption at rest.
INCORRECT:
"Configure encryption at rest on CloudFront by using server-side encryption with AWS KMS keys (SSE-KMS)" is incorrect.
The data must be encrypted at rest in the Amazon S3 origin that is the source for the CloudFront distribution. This configuration does not ensure encryption at rest in the S3 bucket.
INCORRECT:
"Use the RequireSSL option in the creation of presigned URLs for the S3 bucket that the web application uses" is incorrect.
Pre-signed URLs are used to provide short-term access to a private object in your S3 bucket. They work by appending an AWS Access Key, expiration time, and Sigv4 signature as query parameters to the S3 object. Encryption cannot be configured through the pre-signed URL.
References:
https://aws.amazon.com/blogs/networking-and-content-delivery/serving-sse-kms-encrypted-content-from-s3-using-cloudfront/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/data-protection-summary.html
https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-s3-and-glacier/

## Câu 13 — ❌ SAI

<!-- source: T1Q12 · domain: CI · time: 3:18 · first: 73:42 · visits: 3 · changes: 1 -->

### Câu hỏi

A company has deployed an eCommerce application that is used by thousands of customers to place online orders. The application runs on Amazon ECS tasks behind an Application Load Balancer (ALB) and data is stored in an Amazon DynamoDB table.
The application has recently experienced attacks that caused application slowdowns and outages. The company must prevent attacks and ensure business continuity with minimal service interruptions.
Which combination of steps will meet these requirements MOST cost-effectively? (Select TWO.)

### Các phương án

- **A.** Create an Amazon CloudFront distribution with the ALB as the origin and configure a custom header and secret value. Configure the ALB to conditionally forward traffic only if the header and value match.
- **B.** Deploy the application in two AWS Regions. Configure Amazon Route 53 to route to both Regions with equal weight.
- **C.** Configure AWS Auto Scaling for Amazon ECS tasks. Create an Amazon DynamoDB Accelerator (DAX) cluster in front of the DynamoDB table.
- **D.** Configure AWS Auto Scaling for Amazon ECS tasks. Configure an Amazon ElastiCache cluster in front of the DynamoDB table.
- **E.** Deploy an AWS WAF web ACL that includes a rule group that blocks the attack traffic. Associate the web ACL with the Amazon CloudFront distribution.

> **Bạn chọn:** A, C
> **Đáp án đúng:** A, E

### Giải thích

Amazon CloudFront comes with AWS Shield standard by default which will provide some protection against DDoS attacks. For malicious web attacks an AWS WAF ACL should be associated with the distribution so that it can protect against the attacks using an appropriate rule group.
In this configuration it is important to ensure that the attacks cannot circumvent CloudFront and connect directly to the public ALB. For this, we can create a custom header and secret value in CloudFront. This will be forwarded in requests that originate from CloudFront. The ALB can conditionally forward only if this HTTP header information is present in the request.
CORRECT:
"Create an Amazon CloudFront distribution with the ALB as the origin and configure a custom header and secret value. Configure the ALB to conditionally forward traffic only if the header and value match" is a correct answer (as explained above.)
CORRECT:
"Deploy an AWS WAF web ACL that includes a rule group that blocks the attack traffic. Associate the web ACL with the Amazon CloudFront distribution" is also a correct answer (as explained above.)
INCORRECT:
"Deploy the application in two AWS Regions. Configure Amazon Route 53 to route to both Regions with equal weight" is incorrect. This is not the most cost-effective option as the entire application stack is deployed in two Regions.
INCORRECT:
"Configure AWS Auto Scaling for Amazon ECS tasks. Create an Amazon DynamoDB Accelerator (DAX) cluster in front of the DynamoDB table" is incorrect. DAX may assist with performance when caching requests but doesn’t help with preventing web attacks from reaching the ALB or application servers.
INCORRECT:
"Configure AWS Auto Scaling for Amazon ECS tasks. Configure an Amazon ElastiCache cluster in front of the DynamoDB table" is incorrect. As with the previous answer this solution does not assist with mitigating the impact of the attacks.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/elb-route-traffic-custom-http-header/
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-waf-shield/

## Câu 14 — ✅ ĐÚNG

<!-- source: T4Q16 · domain: MIG · time: 2:22 · first: 21:11 · visits: 1 · changes: 2 -->

### Câu hỏi

A company plans to migrate physical servers and VMs from an on-premises data center to the AWS Cloud using AWS Migration Hub. The VMs run on a combination of VMware and Hyper-V hypervisors. A Solutions Architect must determine the best services for data collection and discovery. The company has also requested the ability to generate reports from the collected data.
Which solution meets these requirements?

### Các phương án

- **A.** Use the AWS Agentless Discovery Connector for data collection on physical servers and all VMs. Store the collected data in Amazon S3. Query the data with S3 Select. Generate reports by using Kibana hosted on Amazon EC2.
- **B.** Use the AWS Application Discovery Service agent for data collection on physical servers and Hyper-V. Use the AWS Agentless Discovery Connector for data collection on VMware. Store the collected data in Amazon S3. Query the data with Amazon Athena. Generate reports by using Amazon QuickSight.
- **C.** Use the AWS Application Discovery Service agent for data collection on physical servers and all VMs. Store the collected data in Amazon Elastic File System (Amazon EFS). Query the data and generate reports with Amazon Athena.
- **D.** Use the AWS Systems Manager agent for data collection on physical servers. Use the AWS Agentless Discovery Connector for data collection on all VMs. Store, query, and generate reports from the collected data by using Amazon Redshift.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

> ⚠️ Discovery Connector is superseded by the Agentless Collector; Migration Hub availability changed in 2025.

AWS Application Discovery Service helps you plan your migration to the AWS cloud by collecting usage and configuration data about your on-premises servers. Application Discovery Service is integrated with AWS Migration Hub, which simplifies your migration tracking as it aggregates your migration status information into a single console.
Application Discovery Service offers two ways of performing discovery and collecting data about your on-premises servers:
•
Agentless discovery
– Identifies VMs running on VMware.
•
Agent-based discovery
– Used for physical servers and VMs running on Hyper-V.
For reporting the data can be saved to Amazon S3 and queried using Amazon Athena and Amazon QuickSight.
Migration Hub can then be used to manage the migration process using AWS DMS.
CORRECT:
"Use the AWS Application Discovery Service agent for data collection on physical servers and Hyper-V. Use the AWS Agentless Discovery Connector for data collection on VMware. Store the collected data in Amazon S3. Query the data with Amazon Athena. Generate reports by using Amazon QuickSight" is the correct answer.
INCORRECT:
"Use the AWS Agentless Discovery Connector for data collection on physical servers and all VMs. Store the collected data in Amazon S3. Query the data with S3 Select. Generate reports by using Kibana hosted on Amazon EC2" is incorrect. You cannot use the agentless connector on physical servers or Hyper-V VMs.
INCORRECT:
"Use the AWS Application Discovery Service agent for data collection on physical servers and all VMs. Store the collected data in Amazon Elastic File System (Amazon EFS). Query the data and generate reports with Amazon Athena" is incorrect. It is more efficient to use the agentless connector on VMware VMs. Athena cannot query data in EFS.
INCORRECT:
"Use the AWS Systems Manager agent for data collection on physical servers. Use the AWS Agentless Discovery Connector for data collection on all VMs. Store, query, and generate reports from the collected data by using Amazon Redshift" is incorrect. You cannot use the agentless discovery connector on Hyper-V VMs. RedShift will be an expensive solution and requires application components to read/write data.
References:
https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html
https://aws.amazon.com/quicksight/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-migration-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

## Câu 15 — ✅ ĐÚNG

<!-- source: T2Q12 · domain: MIG · time: 2:31 · first: 22:54 · visits: 2 · changes: 2 -->

### Câu hỏi

A company runs applications on Microsoft Windows servers in an on-premises data center. The servers access a file system shared from one of the Windows servers. Several gigabytes of new data are produced daily. The company is migrating to the cloud and requires the data to be accessible on a file system in the AWS cloud.
Which data migration strategy should the company use?

### Các phương án

- **A.** Use an AWS Storage Gateway file gateway and point the existing on-premises application servers to the new file gateway.
- **B.** Use AWS DataPipeline to schedule a daily task to replicate data between the on-premises file share and Amazon EFS.
- **C.** Use AWS DataSync to schedule a daily task that replicates data between the on-premises file share and Amazon FSX.
- **D.** Use an AWS Storage Gateway volume gateway and point the existing on-premises application servers to the new volume gateway.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

AWS recommends using AWS DataSync to transfer data between FSx for Windows File Server file systems. DataSync is a data transfer service that simplifies, automates, and accelerates moving and replicating data between on-premises storage systems and other AWS storage services over the internet or AWS Direct Connect. DataSync can transfer your file system data and metadata, such as ownership, timestamps, and access permissions.
DataSync supports copying NTFS access control lists (ACLs), and also supports copying file audit control information, also known as NTFS system access control lists (SACLs), which are used by administrators to control audit logging of user attempts to access files.
CORRECT:
"Use AWS DataSync to schedule a daily task that replicates data between the on-premises file share and Amazon FSX" is the correct answer (as explained above.)
INCORRECT:
"Use an AWS Storage Gateway file gateway and point the existing on-premises application servers to the new file gateway" is incorrect. When using a file gateway the data is accessible via SMB locally in the on-premises data and is synchronized to Amazon S3. Therefore, there the data is not accessible in the AWS cloud on a file system.
INCORRECT:
"Use AWS DataPipeline to schedule a daily task to replicate data between the on-premises file share and Amazon EFS" is incorrect. AWS DataSync is designed for this use case whereas DataPipeline is more suitable to ETL use cases.
INCORRECT:
"Use an AWS Storage Gateway volume gateway and point the existing on-premises application servers to the new volume gateway" is incorrect. A volume gateway is used for block-based storage not file-based storage. You access a volume gateway over iSCSI rather than SMB.
References:
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-to-fsx-datasync.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-migration-services/

## Câu 16 — ✅ ĐÚNG

<!-- source: T4Q17 · domain: CI · time: 2:18 · first: 25:08 · visits: 1 · changes: 1 -->

### Câu hỏi

A company runs an eCommerce web application on a pair of Amazon EC2 instances behind an Application Load Balancer. The application stores data in an Amazon DynamoDB table. Traffic has been increasing with some major sales events and read and write traffic has slowed down considerably over the busiest periods.
Which option provides a scalable application architecture to handle peak traffic loads with the LEAST development effort?

### Các phương án

- **A.** Use AWS Lambda for the web application. Increase the read and write capacity of DynamoDB.
- **B.** Use AWS Lambda for the web application. Configure DynamoDB to use global tables.
- **C.** Use Auto Scaling groups for the web application and use DynamoDB auto scaling.
- **D.** Use Auto Scaling groups for the web application and use Amazon Simple Queue Service (Amazon SQS) and an AWS Lambda function to write to DynamoDB.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

This is a simple case of needing to add elasticity to the application. The question specifically states that the chosen option must incur the least development effort. Therefore, the best option is to simply use Amazon EC2 Auto Scaling for the web application and enable auto scaling for DynamoDB.
This solution provides a simple way to enable elasticity and does not require any refactoring of the application or updates to code.
CORRECT:
"Use Auto Scaling groups for the web application and use DynamoDB auto scaling" is the correct answer.
INCORRECT:
"Use Auto Scaling groups for the web application and use Amazon Simple Queue Service (Amazon SQS) and an AWS Lambda function to write to DynamoDB" is incorrect. In this scenario it would be simpler and require less development effort to use Auto Scaling for both layers.
INCORRECT:
"Use AWS Lambda for the web application. Increase the read and write capacity of DynamoDB" is incorrect. This requires major updates to the application code which is more development effort.
INCORRECT:
"Use AWS Lambda for the web application. Configure DynamoDB to use global tables" is incorrect. This requires major updates to the application code which is more development effort.
References:
https://aws.amazon.com/ec2/autoscaling/
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 17 — ✅ ĐÚNG

<!-- source: T2Q1 · domain: CI · time: 2:05 · first: 27:51 · visits: 2 · changes: 0 -->

### Câu hỏi

A company is updating their operating system patching processes. The company manages both on-premises servers and Amazon EC2 instances using multiple toolsets. A solutions architect wants to utilize a single tool for all servers and instances that can deploy patches and report on patch status.
Which set of actions should the solutions architect take to meet these requirements?

### Các phương án

- **A.** Use AWS Systems Manager Patch Manager to deploy patches on the on-premises servers and EC2 instances. Use Systems Manager to generate patch compliance reports.
- **B.** Use an Amazon EventBridge rule to apply patches by scheduling an AWS Systems Manager patch remediation job. Use Amazon Inspector to generate patch compliance reports.
- **C.** Use AWS OpsWorks to deploy patches on the on-premises servers and EC2 instances. Use Amazon Athena to generate patch compliance reports.
- **D.** Use AWS Systems Manager Patch Manager to deploy patches on the EC2 instances and use Run Command for the on-premises servers. Use Systems Manager to generate patch compliance reports.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

AWS Systems Manager Patch Manager can be used for both on-premises servers and EC2 instances. Systems Manager can be configured for hybrid environments that include on-premises servers, edge devices, and virtual machines (VMs) that are configured for AWS Systems Manager, including VMs in other cloud environments.
There are several steps that must be taken to configure your on-premises nodes to be managed by AWS Systems Manager. Please refer to the link in the references below to learn more.
CORRECT:
"Use AWS Systems Manager Patch Manager to deploy patches on the on-premises servers and EC2 instances. Use Systems Manager to generate patch compliance reports" is the correct answer (as explained above.)
INCORRECT:
"Use AWS Systems Manager Patch Manager to deploy patches on the EC2 instances and use Run Command for the on-premises servers. Use Systems Manager to generate patch compliance reports" is incorrect. The patch manager capability of systems manager can be used for the on-premises servers and the EC2 instances, there is no need to use Run Command.
INCORRECT:
"Use an Amazon EventBridge rule to apply patches by scheduling an AWS Systems Manager patch remediation job. Use Amazon Inspector to generate patch compliance reports" is incorrect. EventBridge is not needed as Systems Manager has its own capabilities for Patch Management. Systems Manager also has its own reporting, so Inspector is not needed here.
INCORRECT:
"Use AWS OpsWorks to deploy patches on the on-premises servers and EC2 instances. Use Amazon Athena to generate patch compliance reports" is incorrect. OpsWorks is not the tool to use for deploying patches across servers and instances. Also, Athena runs queries against S3 buckets so the patch compliance data would need to be stored in S3 somehow.
References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-systems-manager/

## Câu 18 — ✅ ĐÚNG

<!-- source: T2Q21 · domain: NEW · flagged · time: 5:18 · first: 30:51 · visits: 2 · changes: 2 -->

### Câu hỏi

A company is deploying a web service that will provide read and write access to structured data. The company expects there to be variable usage patterns with some short but significant spikes. The service must dynamically scale and must be fault tolerant across multiple AWS Regions.
Which actions should a Solutions Architect take to meet these requirements?

### Các phương án

- **A.** Store the data in Amazon DocumentDB in two Regions. Use AWS DMS to synchronize data between databases. Run the web service on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer in each Region. In Amazon Route 53, configure an alias record and a failover routing policy.
- **B.** Store the data in Amazon S3 buckets in two Regions and configure cross-Region replication. Create an Amazon CloudFront distribution that points to multiple origins. Use Amazon API Gateway and AWS Lambda for the web frontend and configure Amazon Route 53 with an alias record pointing to the REST API.
- **C.** Store the data in an Amazon DynamoDB global table in two Regions using on-demand capacity mode. Run the web service in both Regions as Amazon ECS Fargate tasks in an Auto Scaling ECS service behind an Application Load Balancer (ALB). In Amazon Route 53, configure an alias record and a latency-based routing policy with health checks to distribute traffic between the two ALBs.
- **D.** Store the data in Amazon Aurora Multi-Master databases. Add Auto Scaling replicas to both Regions. Run the web service on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer in each Region. In Amazon Route 53, configure an alias record and a multi-value routing policy.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

The DynamoDB global tables solution is the only database solution that will allow writes in both AWS Regions. Using Amazon ECS Fargate tasks with Auto Scaling will ensure the compute layer scales appropriately and an ALB will distribute connections across multiple tasks.
This solution is active-active and so a latency-based routing policy will direct users to the closest Region to improve performance. Health checks are enabled which means that if a Region outage occurs, traffic will be directed to the second Region.
CORRECT:
"Store the data in an Amazon DynamoDB global table in two Regions using on-demand capacity mode. Run the web service in both Regions as Amazon ECS Fargate tasks in an Auto Scaling ECS service behind an Application Load Balancer (ALB). In Amazon Route 53, configure an alias record and a latency-based routing policy with health checks to distribute traffic between the two ALBs" is correct.
INCORRECT:
"Store the data in Amazon Aurora Multi-Master databases. Add Auto Scaling replicas to both Regions. Run the web service on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer in each Region. In Amazon Route 53, configure an alias record and a multi-value routing policy" is incorrect. Aurora Multi-Master works within a Region only, it cannot be used to synchronize writes across Regions.
INCORRECT:
"Store the data in Amazon DocumentDB in two Regions. Use AWS DMS to synchronize data between databases. Run the web service on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer in each Region. In Amazon Route 53, configure an alias record and a failover routing policy" is incorrect. DocumentDB is used for storing JSON data not structured data so is not suitable.
INCORRECT:
"Store the data in Amazon S3 buckets in two Regions and configure cross-Region replication. Create an Amazon CloudFront distribution that points to multiple origins. Use Amazon API Gateway and AWS Lambda for the web frontend and configure Amazon Route 53 with an alias record pointing to the REST API" is incorrect. When using CloudFront with multiple origins, behaviors must be configured to direct traffic to a specific origin, this would not work when the content is the same – it does not function as a load balancer or provide automatic failover.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 19 — ❌ SAI

<!-- source: T5Q28 · domain: CI · time: 3:42 · first: 34:24 · visits: 2 · changes: 0 -->

### Câu hỏi

A financial company stores personally identifiable information (PII) in an Amazon S3 bucket which currently does not have versioning enabled. The current configuration has server-side encryption with S3 managed encryption keys (SSE-S3) enabled to encrypt the objects. According to a new requirement, all current and future objects in the S3 bucket must be encrypted by keys that the company's security team manages.
Which solution will meet these requirements?

### Các phương án

- **A.** Change the default encryption to SSE-S3 with a customer managed key. Use the AWS CLI to re-upload all objects in the S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests.
- **B.** Change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS) in S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests. Use the AWS CLI to re-upload all objects in the S3 bucket.
- **C.** In the S3 bucket properties, change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS). Set an S3 bucket policy to automatically encrypt objects on GetObject and PutObject requests.
- **D.** Change the default encryption to AES-256 with a customer managed key. Attach a policy to deny unencrypted PutObject requests to any entities that access the S3 bucket. Use the AWS CLI to re-upload all objects in the S3 bucket.

> **Bạn chọn:** A
> **Đáp án đúng:** B

### Giải thích

You can configure your bucket to use an S3 Bucket Key for SSE-KMS on new objects by using the Amazon S3 console, REST API, Amazon SDK, Amazon CLI, or Amazon CloudFormation. If you want to enable or disable an S3 Bucket Key for existing objects, you can use a COPY operation.
Switching to AWS KMS from AWS SSE-S3 can provide some additional benefits, including protection from policies that may be overly permissive. For example, adding a bucket policy allowing overly broad access to the data instead of individual users or roles. By implementing encryption using KMS keys, the accessor of the resources would need Amazon S3 policy access and access to a KMS key to decrypt data.
The KMS key is managed by the company. To encrypt existing objects with this key they would need to be uploaded again and this operation can be performed using the AWS CLI.
CORRECT:
"Change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS) in S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests. Use the AWS CLI to re-upload all objects in the S3 bucket" is the correct answer (as explained above.)
INCORRECT:
"In the S3 bucket properties, change the default encryption to SSE-S3 with a customer managed key. Use the AWS CLI to re-upload all objects in the S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests" is incorrect.
You cannot manage your own encryption key with SSE-S3.
INCORRECT:
"Change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS) in S3 bucket. Set an S3 bucket policy to automatically encrypt objects on GetObject and PutObject requests" is incorrect.
You cannot encrypt using GetObject requests as this is downloading objects and they are first decrypted. The bucket policy should be setup to enforce encryption for PutObject requests only.
INCORRECT:
"Change the default encryption to AES-256 with a customer managed key. Attach a policy to deny unencrypted PutObject requests to any entities that access the S3 bucket. Use the AWS CLI to re-upload all objects in the S3 bucket" is incorrect.
Server-Side Encryption in S3 is always AES256, whether you are using SSE-S3 or SSE-KMS.
When changing the encryption type, we choose among AWS/ S3 managed or customer managed but the algorithm remains the same hence this is also incorrect.
References:
https://docs.amazonaws.cn/en_us/AmazonS3/latest/userguide/replication-config-for-kms-objects.html
https://aws.amazon.com/blogs/storage/changing-your-amazon-s3-encryption-from-s3-managed-encryption-sse-s3-to-aws-key-management-service-sse-kms/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-s3-and-glacier/

## Câu 20 — ❌ SAI

<!-- source: T2Q29 · domain: ORG · flagged · time: 3:49 · first: 77:02 · visits: 3 · changes: 1 -->

### Câu hỏi

A company uses multiple AWS accounts. There are separate accounts for development, staging, and production environments. Some new requirements have been issued to control costs and improve the overall governance of the AWS accounts. The company must be able to calculate costs associated with each project and each environment. Commonly deployed IT services must be centrally managed and business units should be restricted to deploying pre-approved IT services only.
Which combination of actions should be taken to meet these requirements? (Select TWO.)

### Các phương án

- **A.** Apply environment, cost center, and application name tags to all resources that accept tags.
- **B.** Configure custom budgets and define thresholds using AWS Cost Explorer.
- **C.** Use AWS Savings Plans to configure budget thresholds and send alerts to management.
- **D.** Create an AWS Service Catalog portfolio for each business unit and add products to the portfolios using AWS CloudFormation templates.
- **E.** Use Amazon CloudWatch to create a billing alarm that notifies managers when a billing threshold is reached or exceeded.

> **Bạn chọn:** B, D
> **Đáp án đúng:** A, D

### Giải thích

AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures.
AWS Service Catalog allows organizations to centrally manage commonly deployed IT services, and helps organizations achieve consistent governance and meet compliance requirements. End users can quickly deploy only the approved IT services they need, following the constraints set by the organization.
To track the costs associated with projects and environments cost allocation tags should be applied to the relevant resources. Cost allocation tags are used to track AWS costs on a detailed level. After you activate cost allocation tags, AWS uses the cost allocation tags to organize your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs.
CORRECT:
"Apply environment, cost center, and application name tags to all resources that accept tags" is a correct answer.
CORRECT:
"Create an AWS Service Catalog portfolio for each business unit and add products to the portfolios using AWS CloudFormation templates" is also a correct answer.
INCORRECT:
"Configure custom budgets and define thresholds using AWS Cost Explorer" is incorrect. Cost Explorer is used for viewing cost related information but not for creating budgets.
INCORRECT:
"Use AWS Savings Plans to configure budget thresholds and send alerts to management" is incorrect as this is not a service but a pricing model and cannot be used for sending alerts.
INCORRECT:
"Use Amazon CloudWatch to create a billing alarm that notifies managers when a billing threshold is reached or exceeded" is incorrect. There is no requirement to create billing alarms specified in the scenario.
References:
https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 21 — ✅ ĐÚNG

<!-- source: T2Q15 · domain: NEW · time: 2:46 · first: 80:53 · visits: 2 · changes: 0 -->

### Câu hỏi

A company utilizing Amazon Connect for their contact center is encountering a surge in automated calls, affecting both operational costs and agent productivity. They need a system where agents can easily mark a call as spam, subsequently preventing such numbers from being routed to agents in the future.
What is the most effective and operationally efficient solution for this scenario?

### Các phương án

- **A.** Implement a machine learning model within Amazon Connect to automatically detect and flag spam calls. Store these numbers in an Amazon DynamoDB table and configure contact flows to use an AWS Lambda function for consulting this table to block future spam calls.
- **B.** Add a custom 'flag as spam' button to the Contact Control Panel (CCP) in Amazon Connect. This button triggers an AWS Lambda function to update call attributes and log the number in an Amazon DynamoDB table. Adapt the contact flows to reference these attributes and interact with the DynamoDB table for future call filtering.
- **C.** Develop a special feature in the Amazon Connect CCP that allows agents to transfer spam calls to a designated queue. This queue triggers an AWS Lambda function to add the caller's number to a spam list in Amazon DynamoDB, with contact flows adjusted to check this list for incoming calls.
- **D.** Introduce a voice command feature in the Amazon Connect CCP for agents to verbally mark calls as spam. This command activates an AWS Lambda function to record the number in an Amazon DynamoDB table, and the contact flow is modified to use this table for blocking subsequent calls from these numbers.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

This solution is operationally efficient as it integrates directly into the existing Amazon Connect CCP, allowing agents to mark calls as spam with a simple button click.
The use of AWS Lambda ensures automated processing, and Amazon DynamoDB provides a scalable way to store and retrieve spam numbers.
By modifying the contact flows to reference the updated attributes and DynamoDB table, the system can effectively prevent future calls from flagged numbers, enhancing productivity and reducing costs.
CORRECT:
"Add a custom 'flag as spam' button to the Contact Control Panel (CCP) in Amazon Connect. This button triggers an AWS Lambda function to update call attributes and log the number in an Amazon DynamoDB table. Adapt the contact flows to reference these attributes and interact with the DynamoDB table for future call filtering" is the correct answer (as explained above.)
INCORRECT:
"Implement a machine learning model within Amazon Connect to automatically detect and flag spam calls. Store these numbers in an Amazon DynamoDB table and configure contact flows to use an AWS Lambda function for consulting this table to block future spam calls" is incorrect.
While a machine learning model could potentially automate the detection of spam calls, implementing and maintaining such a system requires significant resources and expertise. It may not be as operationally efficient compared to a simpler, direct solution like a custom button in the CCP.
INCORRECT:
"Develop a special feature in the Amazon Connect CCP that allows agents to transfer spam calls to a designated queue. This queue triggers an AWS Lambda function to add the caller's number to a spam list in Amazon DynamoDB, with contact flows adjusted to check this list for incoming calls" is incorrect.
Creating a special feature for transferring spam calls to a designated queue adds additional steps to the agent's workflow and may not be as immediate or straightforward as directly flagging a call as spam. This could lead to inefficiencies in handling calls.
INCORRECT:
"Introduce a voice command feature in the Amazon Connect CCP for agents to verbally mark calls as spam. This command activates an AWS Lambda function to record the number in an Amazon DynamoDB table, and the contact flow is modified to use this table for blocking subsequent calls from these numbers" is incorrect.
Introducing a voice command feature for marking spam calls is an innovative approach but may face challenges in terms of accuracy and ease of use, especially in a noisy call center environment. This might not be as reliable or efficient as a more traditional interface-based solution.
References:
https://aws.amazon.com/connect/features/

## Câu 22 — ✅ ĐÚNG

<!-- source: T5Q7 · domain: CI · flagged · time: 1:21 · first: 35:45 · visits: 2 · changes: 0 -->

### Câu hỏi

A company runs a Java application on Amazon EC2 instances. The DevOps team uses a combination of Amazon CloudFormation and AWS OpsWorks to update the infrastructure and application stacks respectively. During recent updates the DevOps team reported service disruption issues that affected the Java application running on the Amazon EC2 instances.
Which solution will increase the reliability of application updates?

### Các phương án

- **A.** Implement a blue/green deployment strategy.
- **B.** Implement the canary release strategy.
- **C.** Implement CloudFormation change sets.
- **D.** Implement CloudFormation Stack sets.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

> ⚠️ Relies on OpsWorks, end of life 2024; blue/green still best choice.

AWS OpsWorks is performing the updates to the application. There is no report of the infrastructure stack having any errors and therefore CloudFormation is not relevant.
AWS OpsWorks supports a blue-green deployment strategy. It does not support a canary deployment strategy.
A
blue-green
deployment strategy is a common way to efficiently use separate stacks to deploy an application update to production.
• The blue environment is the production stack, which hosts the current application.
• The green environment is the staging stack, which hosts the updated application.
When you are ready to deploy the updated app to production, you switch user traffic from the blue stack to the green stack, which becomes the new production stack. You then retire the old blue stack.
This deployment strategy offers the ability to perform testing on the green environment before fully cutting over and this can improve reliability for updates.
CORRECT:
"Implement a blue/green deployment strategy" is the correct answer.
INCORRECT:
"Implement the canary release strategy" is incorrect. OpsWorks does not support a canary release methodology.
INCORRECT:
"Implement CloudFormation change sets" is incorrect. CloudFormation is used to deploy the underlying infrastructure stack (e.g. Amazon EC2 and related infrastructure), OpsWorks is being used to deploy the application updates.
INCORRECT:
"Implement CloudFormation Stack sets" is incorrect. As above.
References:
https://docs.aws.amazon.com/opsworks/latest/userguide/best-deploy.html#best-deploy-environments-blue-green
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 23 — ✅ ĐÚNG

<!-- source: T1Q15 · domain: NEW · time: 1:05 · first: 37:03 · visits: 1 · changes: 0 -->

### Câu hỏi

An application stores user comment data in multiple Amazon DynamoDB tables. A solutions architect must use a serverless architecture to make the data accessible publicly through a simple and cost-effective API over HTTPS. The solution must scale automatically in response to demand.
Which solutions meet these requirements?

### Các phương án

- **A.** Create an Amazon API Gateway REST API. Configure this API with direct integrations to DynamoDB by using API Gateway's AWS Service integration type.
- **B.** Create an Amazon API Gateway HTTP API. Configure this API with direct integrations to DynamoDB by using API Gateway's AWS Service integration type.
- **C.** Create an Amazon API Gateway REST API. Configure this API with integrations to AWS Lambda functions that return data from the DynamoDB tables.
- **D.** Create an Amazon API Gateway HTTP API. Configure this API with integrations to AWS Lambda functions that return data from the DynamoDB tables.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

A REST API must be used to provide a direct AWS Service integration to Amazon DynamoDB. An AWS Lambda function is not needed in that case as direct integration is possible and API Gateway will scale seamlessly.
However, in this case the requirement is for a simple and cost-effective API. This is therefore a good use case for an HTTP API which is lower cost. With an HTTP API direct integration to DynamoDB is not possible but you can connect to multiple Lambda functions and configure methods and paths. This solution meets all requirements.
CORRECT:
"Create an Amazon API Gateway HTTP API. Configure this API with integrations to AWS Lambda functions that return data from the DynamoDB tables" is the correct answer (as explained above.)
INCORRECT:
"Create an Amazon API Gateway HTTP API. Configure this API with direct integrations to DynamoDB by using API Gateway's AWS Service integration type" is incorrect.
You cannot create a direct integration to DynamoDB when using an HTTP API.
INCORRECT:
"Create an Amazon API Gateway REST API. Configure this API with integrations to AWS Lambda functions that return data from the DynamoDB tables" is incorrect.
This is a less cost-effective solution as explained above.
INCORRECT:
"Create an Amazon API Gateway REST API. Configure this API with direct integrations to DynamoDB by using API Gateway's AWS Service integration type" is incorrect.
This is a less cost-effective solution as explained above.
References:
https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-as-a-proxy-for-dynamodb/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-api-gateway/

## Câu 24 — ✅ ĐÚNG

<!-- source: T3Q11 · domain: ORG · time: 4:46 · first: 41:11 · visits: 2 · changes: 0 -->

### Câu hỏi

A pharmaceutical company has deployed an application on their private Amazon VPC. They need to use a third-party software-as-a-service (SaaS) application which is hosted in another AWS account inside an Amazon VPC.
They need to connect applications to the third-party SaaS from private subnets in the company VPC. The company’s security team has mandated policies that private network needs to be used without internet propagation. No resources that run in the company VPC are allowed to be accessed from outside the company's VPC. All permissions must conform to the principles of least privilege.
Which solution meets these requirements?

### Các phương án

- **A.** Create an AWS PrivateLink interface VPC endpoint. Connect this endpoint to the endpoint service that the third-party SaaS application provides. Create a security group to limit the access to the endpoint and associate the security group with the endpoint.
- **B.** Create an AWS Site-to-Site VPN connection between the third-party SaaS application and the company VPC. Configure network ACLs to limit access across the VPN tunnels.
- **C.** Create a VPC peering connection between the third-party SaaS application and the company VPC. Update route tables by adding the required routes for the peering connection.
- **D.** Create an AWS PrivateLink endpoint service. Ask the third-party SaaS provider to create an interface VPC endpoint for this endpoint service. Grant permissions for the endpoint service to the specific account of the third-party SaaS provider.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

AWS PrivateLink provides you option to connect to SaaS products privately, as if it is running on customer’s VPC itself.
A service consumer creates a
VPC endpoint
to connect their VPC to an endpoint service. A service consumer must specify the service name of the endpoint service when creating a VPC endpoint. There are multiple types of VPC endpoints. You must create the type of VPC endpoint that's required by the endpoint service.
-
Interface
- Create an
interface endpoint
to send traffic to endpoint services that use a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS.
-
GatewayLoadBalancer
- Create a
Gateway Load Balancer endpoint
to send traffic to a fleet of virtual appliances using private IP addresses. You route traffic from your VPC to the Gateway Load Balancer endpoint using route tables. The Gateway Load Balancer distributes traffic to the virtual appliances and can scale with demand.
-
Gateway
- Create a
gateway endpoint
to send traffic to Amazon S3 or DynamoDB using private IP addresses. You route traffic from your VPC to the gateway endpoint using route tables. Gateway endpoints do not enable AWS PrivateLink.
In this case the AWS PrivateLink service must already be published by the service provider. The company then acts as the service consumer by creating an interface endpoint to connect to the service provider’s service.
CORRECT:
"Create an AWS PrivateLink interface VPC endpoint. Connect this endpoint to the endpoint service that the third-party SaaS application provides. Create a security group to limit the access to the endpoint. Associate the security group with the endpoint" is the correct answer (as explained above.)
INCORRECT:
"Create an AWS Site-to-Site VPN connection between the third-party SaaS application and the company VPC. Configure network ACLs to limit access across the VPN tunnels" is incorrect.
You cannot create S2S VPNs between VPCs or applications using AWS services. This would need to be configured using 3rd party software.
INCORRECT:
"Create a VPC peering connection between the third-party SaaS application and the company VPC. Update route tables by adding the required routes for the peering connection" is incorrect.
While VPC peering enables you to privately connect VPCs, AWS PrivateLink enables you to configure applications or services in VPCs as endpoints that your VPC peering connections can connect to. This is a more secure solution as there is less trust required.
INCORRECT:
"Create an AWS PrivateLink endpoint service. Ask the third-party SaaS provider to create an interface VPC endpoint for this endpoint service. Grant permissions for the endpoint service to the specific account of the third-party SaaS provider" is incorrect.
The AWS PrivateLink endpoint service is published by the service provider which in this case is the third-party SaaS provider. The company is then acting as the service consumer and needs to create a VPC interface endpoint.
References:
https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-saas.html
https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-vpc/

## Câu 25 — ✅ ĐÚNG

<!-- source: T1Q6 · domain: CI · time: 3:35 · first: 44:50 · visits: 1 · changes: 0 -->

### Câu hỏi

A media company streams live events and records viewership metrics in real-time. The data is ingested through Amazon Kinesis Data Streams and then stored in Amazon S3. The company uses Amazon Athena to analyze viewership trends from the stored data. Initially, the Athena queries performed well, but as the data volume has grown over several months, query performance has degraded.
The solutions architect needs to optimize the query performance while keeping operational overhead low.
Which solution will effectively address the performance issue?

### Các phương án

- **A.** Create an AWS Glue job to aggregate daily viewership data into summary tables and modify the Athena queries to use these summary tables.
- **B.** Configure the Kinesis Data Streams to categorize data into different S3 buckets based on the event type. Update the Athena queries to scan data from specific buckets based on the query requirements.
- **C.** Configure the Kinesis Data Firehose delivery stream to partition the data in Amazon S3 by date and event type. Redefine the Athena table to include these partitions and modify the queries to specifically target relevant partitions.
- **D.** Create an Amazon Redshift cluster and use Redshift Spectrum to query the S3 data. Modify the Athena queries to run against the Redshift Spectrum layer for improved performance.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Partitioning the data by date and event type using Kinesis Data Firehose and then updating the Athena table definitions to reflect these partitions can significantly improve query performance.
By doing so, Athena queries can be tailored to scan only the relevant partitions instead of the entire dataset, reducing the amount of data scanned and thus improving query efficiency.
This approach is operationally efficient as it leverages existing AWS services and structures without the need for extensive data processing or additional infrastructure management.
CORRECT:
"Configure the Kinesis Data Firehose delivery stream to partition the data in Amazon S3 by date and event type. Redefine the Athena table to include these partitions and modify the queries to specifically target relevant partitions" is the correct answer (as explained above.)
INCORRECT:
"Create an AWS Glue job to aggregate daily viewership data into summary tables and modify the Athena queries to use these summary tables" is incorrect.
While creating summary tables can improve performance, it introduces additional complexity and operational overhead in maintaining these tables.
INCORRECT:
"Configure the Kinesis Data Streams to categorize data into different S3 buckets based on the event type. Update the Athena queries to scan data from specific buckets based on the query requirements" is incorrect.
Distributing data across multiple buckets can complicate data management and may not significantly improve query performance compared to partitioning.
INCORRECT:
"Create an Amazon Redshift cluster and use Redshift Spectrum to query the S3 data. Modify the Athena queries to run against the Redshift Spectrum layer for improved performance" is incorrect.
While Redshift Spectrum can enhance performance for certain workloads, setting up and maintaining a Redshift cluster introduces more operational complexity and cost, which may not align with the goal of minimizing operational overhead.
References:
https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-format
https://docs.aws.amazon.com/athena/latest/ug/partitions.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-kinesis/

## Câu 26 — ✅ ĐÚNG

<!-- source: T1Q8 · domain: MIG · time: 1:33 · first: 46:24 · visits: 1 · changes: 0 -->

### Câu hỏi

A company runs a data processing application on-premises and plans to move it to the AWS Cloud. Files are uploaded by users to a web application which then stores the files on an NFS-based storage system and places a message on a queue. The files are then processed from the queue and the results are returned to the user (and stored in long-term storage). This process can take up to 30 minutes. The processing times vary significantly and can be much higher during business hours.
What is the MOST cost-effective migration recommendation?

### Các phương án

- **A.** Create a queue using Amazon SQS. Run the web application on Amazon EC2 and configure it to publish to the new queue. Use an AWS Lambda function to poll the queue, pull requests, and process the files. Store the processed files in an Amazon S3 bucket.
- **B.** Create a queue using Amazon MQ. Run the web application on Amazon EC2 and configure it to publish to the new queue. Launch an Amazon EC2 instance from a preconfigured AMI to poll the queue, pull requests, and process the files. Store the processed files in Amazon EFS. Terminate the EC2 instance after the task is complete.
- **C.** Create a queue using Amazon SQS. Run the web application on Amazon EC2 and configure it to publish to the new queue. Use Amazon EC2 instances in an EC2 Auto Scaling group to pull requests from the queue and process the files. Scale the EC2 instances based on the SQS queue length. Store the processed files in an Amazon S3 bucket.
- **D.** Create a queue using Amazon MQ. Run the web application on Amazon EC2 and configure it to publish to the new queue. Use an AWS Lambda function to poll the queue, pull requests, and process the files. Store the processed files in Amazon EFS.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

The best solution is to use Amazon SQS for the message queue, Amazon EC2 Auto Scaling for the processing layer, and Amazon S3 for the storage layer. This solution meets all requirements and is the lowest cost option available.
The ASG should also be configured to scale based on the ApproximateNumberOfMessages queue attribute. This is used in combination with an acceptable backlog per instance metric which defines the number of messages in the queue to use as scaling criteria.
The following diagram illustrates the architecture of this configuration.
CORRECT:
"Create a queue using Amazon SQS. Run the web application on Amazon EC2 and configure it to publish to the new queue. Use Amazon EC2 instances in an EC2 Auto Scaling group to pull requests from the queue and process the files. Scale the EC2 instances based on the SQS queue length. Store the processed files in an Amazon S3 bucket" is the correct answer.
INCORRECT:
"Create a queue using Amazon SQS. Run the web application on Amazon EC2 and configure it to publish to the new queue. Use an AWS Lambda function to poll the queue, pull requests, and process the files. Store the processed files in an Amazon S3 bucket" is incorrect. Lambda cannot process files for 30 minutes; it has a maximum execution time of 15 minutes.
INCORRECT:
"Create a queue using Amazon MQ. Run the web application on Amazon EC2 and configure it to publish to the new queue. Launch an Amazon EC2 instance from a preconfigured AMI to poll the queue, pull requests, and process the files. Store the processed files in Amazon EFS. Terminate the EC2 instance after the task is complete" is incorrect. If the instance is terminated each time then how can it poll the queue? This is not a workable solution.
INCORRECT:
"Create a queue using Amazon MQ. Run the web application on Amazon EC2 and configure it to publish to the new queue. Use an AWS Lambda function to poll the queue, pull requests, and process the files. Store the processed files in Amazon EFS" is incorrect. Lambda cannot be used as mentioned previously (max execution limit).
References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-application-integration-sap/

## Câu 27 — ✅ ĐÚNG

<!-- source: T4Q35 · domain: ORG · flagged · time: 2:54 · first: 49:08 · visits: 2 · changes: 0 -->

### Câu hỏi

A multinational corporation with offices in different regions has several AWS accounts, each managed by local IT teams. The corporation's central IT department, based in their headquarters, needs to gain oversight, and implement standardized security policies across all these regional AWS accounts.
A solutions architect is tasked with enabling the central IT department to efficiently manage security policies and monitor compliance across all regional AWS accounts. After setting up AWS Organizations and inviting all regional accounts to join, what should be the next step to meet these requirements?

### Các phương án

- **A.** In each regional account, set up a dedicated IAM user for the central IT department with administrative privileges.
- **B.** In each regional account, create a SecurityAudit IAM policy and apply it to the respective regional administrators.
- **C.** In each regional account, establish the SecurityAudit IAM role and grant permission to the central account to assume this role.
- **D.** In the central account, develop a custom AWS Lambda function that automatically applies security policies to all regional accounts.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

By establishing a SecurityAudit IAM role (or a similarly purposed role) in each regional account and granting permissions to the central account to assume this role, the central IT department can efficiently manage and monitor security policies across all accounts.
This approach is aligned with AWS best practices for centralized management and governance in a multi-account environment.
CORRECT:
"In each regional account, establish the SecurityAudit IAM role and grant permission to the central account to assume this role" is the correct answer (as explained above.)
INCORRECT:
"In each regional account, set up a dedicated IAM user for the central IT department with administrative privileges" is incorrect.
Setting up individual IAM users in each regional account for the central IT department is not efficient and does not leverage the centralized management capabilities of AWS Organizations.
INCORRECT:
"In each regional account, create a SecurityAudit IAM policy and apply it to the respective regional administrators" is incorrect.
Creating a SecurityAudit IAM policy and applying it to regional administrators does not provide the central IT department with the ability to directly enforce and monitor security policies across accounts.
INCORRECT:
"In the central account, develop a custom AWS Lambda function that automatically applies security policies to all regional accounts" is incorrect.
Developing a custom AWS Lambda function for policy application is unnecessary when AWS Organizations and IAM roles can be used to accomplish this task more effectively and with less complexity.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-organizations/

## Câu 28 — ✅ ĐÚNG

<!-- source: T3Q7 · domain: MIG · time: 3:00 · first: 83:43 · visits: 2 · changes: 1 -->

### Câu hỏi

A company plans to migrate a content management system (CMS) to AWS. The CMS will use Amazon CloudFront to ensure optimum performance for users from around the world. The CMS includes both static and dynamic content and has been placed behind an Application Load Balancer (ALB) which is the default origin for the CloudFront distribution. The static assets are served from an Amazon S3 bucket.
When users attempt to access the static assets HTTP status code 404 errors are generated. Which actions should a Solutions Architect take to resolve the issue? (Select TWO.)

### Các phương án

- **A.** Add another origin to the CloudFront distribution for the static assets.
- **B.** Add a rule to the distribution to forward GET method requests to Amazon S3.
- **C.** Add a CachePolicyConfig to allow HTTP headers to be included in requests to the origin.
- **D.** Add a behavior to the CloudFront distribution for the path pattern and the origin of the static assets.
- **E.** Add a host header condition to the ALB listener and forward the header from CloudFront to add traffic to the allow list.

> **Bạn chọn:** A, D
> **Đáp án đúng:** A, D

### Giải thích

The configuration of Amazon CloudFront is such that all requests are being directed to the default origin, which in this case is the ALB. As the static assets do not exist on the ALB (more specifically, on its targets), the requests fail with a 404. A 404 HTTP status code indicates that the object has not been found.
The resolution to this issue is to add an additional origin that points to the S3 bucket and then use a path pattern behavior to direct requests for these URLs to the S3 origin. The pattern (for example, images/*.jpg) specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution. This will resolve the 404 Not Found error messages.
CORRECT:
"Add another origin to the CloudFront distribution for the static assets" is a correct answer.
CORRECT:
"Add a behavior to the CloudFront distribution for the path pattern and the origin of the static assets" is a correct answer.
INCORRECT:
"Add a rule to the distribution to forward GET method requests to Amazon S3" is incorrect. GET method requests also need to be directed to the ALB, and you cannot configure rules to direct methods to different origins. You can configure the AllowedMethods parameter which controls which methods are available.
INCORRECT:
"Add a CachePolicyConfig to allow HTTP headers to be included in requests to the origin" is incorrect. This parameter specifies the values that CloudFront includes in the cache key. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer. This cannot be used to ensure that requests for the static assets will be directed to S3.
INCORRECT:
"Add a host header condition to the ALB listener and forward the header from CloudFront to add traffic to the allow list" is incorrect. This will not resolve the 404 Not Found errors. The only way to resolve these errors is to direct traffic to the correct origin.
References:
https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CacheBehavior.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 29 — ✅ ĐÚNG

<!-- source: T3Q35 · domain: MIG · time: 2:24 · first: 85:54 · visits: 2 · changes: 2 -->

### Câu hỏi

An eCommerce company runs a successful website with a growing base of customers. The website is becoming popular internationally and demand is increasing quickly. The website is currently hosted in an on-premises data center with web servers and a MySQL database. The company plans to migrate the workloads to AWS. A Solutions Architect has been asked to create a solution that:
- Improves security
- Improves reliability
- Improves availability
- Reduces latency
- Reduces maintenance
Which combination of steps should the Solutions Architect take to meet these requirements? (Select THREE.)

### Các phương án

- **A.** Create an Auto Scaling group of Amazon EC2 instances in two Availability Zones and attach an Application Load Balancer.
- **B.** Launch Amazon EC2 instances in two Availability Zones to host a highly available MySQL database cluster.
- **C.** Migrate the database to an Amazon Aurora MySQL DB cluster configured for Multi-AZ.
- **D.** Host static website content in Amazon S3. Use Amazon CloudFront to reduce latency while serving webpages. Use AWS WAF to improve website security.
- **E.** Host static website content in Amazon S3. Use S3 Transfer Acceleration to reduce latency while serving webpages. Use AWS WAF to improve website security.
- **F.** Migrate the database to a single-AZ Amazon RDS for MySQL DB instance.

> **Bạn chọn:** A, C, D
> **Đáp án đúng:** A, C, D

### Giải thích

This is a simple migration to cloud that requires a standard set of security, performance, and reliability requirements. To meet these requirements an ASG should be created across multiple AZs for the web layer. This should be behind an ALB for distributing incoming connections.
For the database layer an Aurora MySQL DB cluster with an Aurora Replica in another AZ will provide Multi-AZ failover. This ensures the DB layer is highly available, and reduces maintenance.
Another way to improve performance for global users is to host static content in Amazon S3 and use the Amazon CloudFront CDN to cache the content in Edge Locations around the world. Adding AWS WAF adds additional security.
CORRECT:
"Create an Auto Scaling group of Amazon EC2 instances in two Availability Zones and attach an Application Load Balancer" is a correct answer.
CORRECT:
"Migrate the database to an Amazon Aurora MySQL DB cluster configured for Multi-AZ" is a correct answer.
CORRECT:
"Host static website content in Amazon S3. Use Amazon CloudFront to reduce latency while serving webpages. Use AWS WAF to improve website security" is a correct answer.
INCORRECT:
"Launch Amazon EC2 instances in two Availability Zones to host a highly available MySQL database cluster" is incorrect. This requires more maintenance to maintain so is not the best solution.
INCORRECT:
"Host static website content in Amazon S3. Use S3 Transfer Acceleration to reduce latency while serving webpages. Use AWS WAF to improve website security" is incorrect. Transfer Acceleration is for uploading data using the CloudFront Edge network. For serving static assets use a CloudFront distribution.
INCORRECT:
"Migrate the database to a single-AZ Amazon RDS for MySQL DB instance" is incorrect. This does not provide the availability required, deploying an Aurora Replica in another AZ provides high availability.
References:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 30 — ❌ SAI

<!-- source: T2Q10 · domain: CI · time: 1:31 · first: 50:24 · visits: 1 · changes: 1 -->

### Câu hỏi

A Solutions Architect has deployed an application on Amazon EC2 instances in a private subnet behind a Network Load Balancer (NLB) in a public subnet. Customers have attempted to connect from their office location and are unable to access the application. The targets were registered by instance-id and are all healthy in the associated target group.
What step should the Solutions Architect take to resolve the issue and enable access for the customers?

### Các phương án

- **A.** Check the security group for the EC2 instances to ensure it allows ingress from the NLB subnets.
- **B.** Check the security group for the EC2 instances to ensure it allows ingress from the customer office.
- **C.** Check the security group for the NLB to ensure it allows ingress from the EC2 instances’ security group.
- **D.** Check the security group for the NLB to ensure it allows ingress from the NLB elastic IP addresses.

> **Bạn chọn:** A
> **Đáp án đúng:** B

### Giải thích

> ⚠️ Says NLBs have no security groups; NLB supports SGs since 2023. Key B still correct.

The Solutions Architect should check that the security group of the EC2 instances is allowing inbound connections from the customer office IP ranges. Note that NLBs do not have security groups configured and pass connections straight to EC2 instances with the source IP of the client preserved (when registered by instance-id).
With NLBs, when you register EC2 instances as targets, you must ensure that the security groups for these instances allow traffic on both the listener port and the health check port. We know that the health check port is already configured correctly as the targets are all healthy.
CORRECT:
"Check the security group for the EC2 instances to ensure it allows ingress from the customer office" is the correct answer.
INCORRECT:
"Check the security group for the EC2 instances to ensure it allows ingress from the NLB subnets" is incorrect. This is not necessary as the source IPs of clients are preserved.
INCORRECT:
"Check the security group for the NLB to ensure it allows ingress from the EC2 instances’ security group" is incorrect. The NLB security group does not receive incoming traffic from EC2, the traffic would come from the client.
INCORRECT:
"Check the security group for the NLB to ensure it allows ingress from the NLB elastic IP addresses. There is no security group associated with an NLB. If using EIPs, these are associated with the nodes in the AZ but the NLB security group would not need to receive incoming traffic from the nodes.
References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html#target-security-groups
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 31 — ❌ SAI

<!-- source: T1Q14 · domain: ORG · flagged · time: 3:51 · first: 53:56 · visits: 2 · changes: 0 -->

### Câu hỏi

A company has established a 10 Gbps AWS Direct Connect (DX) connection to a single VPC in an AWS Region. A single private VIF has been created for the existing DX connection. The company requires redundancy for the existing DX connection and needs to connect to an additional VPC in a second Region.
Which solution meets these requirements?

### Các phương án

- **A.** Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region.
- **B.** Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a transit gateway in the VPCs in each Region.
- **C.** Create a new DX connection to the second Region. Create a new private VIF across the new DX connection to a virtual private gateway in the VPC in the second Region.
- **D.** Create a new DX connection to the second Region. Provision a transit gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region.

> **Bạn chọn:** C
> **Đáp án đúng:** A

### Giải thích

Use AWS Direct Connect gateway to connect your VPCs. You associate an AWS Direct Connect gateway with either of the following gateways:
A transit gateway when you have multiple VPCs in the same Region
A virtual private gateway
A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any Region and access it from all other Regions.
In this case the architecture should include a second DX connection from the on-premises network to the same Region as the existing DX connection to add redundancy. A DX GW can be provisioned and private VIFs can be created to virtual private gateways (VGWs) in the two AWS Regions the company wants to access.
CORRECT:
"Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region" is the correct answer (as explained above.)
INCORRECT:
"Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a transit gateway in the VPCs in each Region" is incorrect.
The transit gateway is not required in this scenario as the company only has a single VPC they need to connect to in each Region.
INCORRECT:
"Create a new DX connection to the second Region. Create a new private VIF across the new DX connection to a virtual private gateway in the VPC in the second Region" is incorrect.
This does not provide the DX redundancy the company requires for the existing DX connection as the connection goes to a different Region and VPC.
INCORRECT:
"Create a new DX connection to the second Region. Provision a transit gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region" is incorrect.
The company requires redundancy for the existing DX connection in the same Region and will then need ta DX gateway to connect across Regions.
References:
https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-direct-connect/

## Câu 32 — ✅ ĐÚNG

<!-- source: T6Q4 · domain: NEW · time: 1:27 · first: 55:11 · visits: 1 · changes: 1 -->

### Câu hỏi

A company uses AWS CodeCommit for source control and AWS CodePipeline for continuous integration. The pipeline has a build stage which uses an Amazon S3 bucket for artifacts. The company requires a new development pipeline for testing new features. The new pipeline should be isolated from the production pipeline and incorporate continuous testing for unit tests.
How can a Solutions Architect meet these requirements?

### Các phương án

- **A.** Create a separate pipeline in CodePipeline and trigger execution using CodeCommit branches. Use AWS CodeBuild for running unit tests and stage the artifacts in an S3 bucket in a separate testing account.
- **B.** Create a separate pipeline in CodePipeline and trigger execution using CodeCommit branches. Use AWS Lambda for running unit tests. Use AWS CodeDeploy to stage the artifacts within an S3 bucket in a separate testing account.
- **C.** Create a separate pipeline in CodePipeline and trigger execution using CodeCommit tags. Use Jenkins for running unit tests. Create a stage in the pipeline with S3 as the target for staging the artifacts with an S3 bucket in a separate testing account.
- **D.** Create a separate CodeCommit repository for feature development and use it to trigger the pipeline. Use AWS Lambda for running unit tests. Use AWS CodeBuild to stage the artifacts within different S3 buckets in the same production account.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

> ⚠️ Relies on CodeCommit availability (see T5Q11 note).

Branches are pointers or references to a commit. In development, they're a convenient way to organize your work. You can use branches to separate work on a new or different version of files without affecting work in other branches. In this case a branch can trigger a separate pipeline and CodeBuild can be used for running unit tests in that pipeline. The artifacts can be stored in a separate account for isolation from the production environment.
CORRECT:
"Create a separate pipeline in CodePipeline and trigger execution using CodeCommit branches. Use AWS CodeBuild for running unit tests and stage the artifacts in an S3 bucket in a separate testing account" is the correct answer.
INCORRECT:
"Create a separate pipeline in CodePipeline and trigger execution using CodeCommit branches. Use AWS Lambda for running unit tests. Use AWS CodeDeploy to stage the artifacts within an S3 bucket in a separate testing account" is incorrect. CodeBuild should be used for running the units tests instead of Lambda.
INCORRECT:
"Create a separate pipeline in CodePipeline and trigger execution using CodeCommit tags. Use Jenkins for running unit tests. Create a stage in the pipeline with S3 as the target for staging the artifacts with an S3 bucket in a separate testing account" is incorrect. CodeCommit branches rather than tags should be used to trigger the pipeline and CodeBuild should be used for running the units tests instead of Jenkins.
INCORRECT:
"Create a separate CodeCommit repository for feature development and use it to trigger the pipeline. Use AWS Lambda for running unit tests. Use AWS CodeBuild to stage the artifacts within different S3 buckets in the same production account" is incorrect. Branches can be used instead of a separate CodeCommit repository, CodeBuild should run unit tests and a separate account should be used for storing artifacts.
References:
https://docs.aws.amazon.com/codecommit/latest/userguide/branches.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-developer-tools-sap/

## Câu 33 — ✅ ĐÚNG

<!-- source: T6Q22 · domain: NEW · time: 2:44 · first: 57:44 · visits: 1 · changes: 1 -->

### Câu hỏi

A healthcare company has developed a series of microservices for processing patient data, hosted on AWS. These microservices are accessed through REST APIs managed by Amazon API Gateway. To comply with healthcare regulations, the company needs to ensure that these APIs are only accessible from their internal application, which runs on an Amazon EC2 instance within their AWS VPC. The application must securely access these APIs without exposing them to the public internet.
Which step should a solutions architect take to ensure that the REST APIs are securely accessible by the internal application, while complying with the healthcare regulations?

### Các phương án

- **A.** Set up an Elastic Load Balancer (ELB) in front of the API Gateway and restrict access to the ELB from the EC2 instance's security group.
- **B.** Create an interface VPC endpoint for API Gateway in the VPC. Enable private DNS naming for the VPC endpoint and configure an API resource policy that allows access from the VPC endpoint. Use the API endpoint's DNS names to access the API from the EC2 instance.
- **C.** Configure the API Gateway with a resource policy that restricts access to the IP range of the VPC in which the EC2 instance is running. Ensure the EC2 instance accesses the API Gateway using its public DNS name.
- **D.** Deploy a reverse proxy server in the VPC and configure it to forward requests to the API Gateway. Restrict access to the proxy server from the EC2 instance only.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Creating an interface VPC endpoint for API Gateway enables the internal application on the EC2 instance to access the REST APIs directly through the AWS private network.
Enabling private DNS naming for the VPC endpoint ensures the internal application can resolve the API Gateway endpoint within the VPC.
The API resource policy that allows access from the VPC endpoint ensures that the APIs are not accessible from the public internet, adhering to the healthcare regulations.
CORRECT:
"Create an interface VPC endpoint for API Gateway in the VPC. Enable private DNS naming for the VPC endpoint and configure an API resource policy that allows access from the VPC endpoint. Use the API endpoint's DNS names to access the API from the EC2 instance" is the correct answer (as explained above.)
INCORRECT:
"Set up an Elastic Load Balancer (ELB) in front of the API Gateway and restrict access to the ELB from the EC2 instance's security group" is incorrect.
An Elastic Load Balancer is typically used for balancing incoming internet or internal traffic and does not provide the necessary restriction for API Gateway access within a VPC.
INCORRECT:
"Configure the API Gateway with a resource policy that restricts access to the IP range of the VPC in which the EC2 instance is running. Ensure the EC2 instance accesses the API Gateway using its public DNS name" is incorrect.
Restricting access based on IP range does not prevent the possibility of exposing the API to the public internet, and using the public DNS name for API access contradicts the requirement for internal-only access.
INCORRECT:
"Deploy a reverse proxy server in the VPC and configure it to forward requests to the API Gateway. Restrict access to the proxy server from the EC2 instance only" is incorrect.
Deploying a reverse proxy server adds unnecessary complexity and does not leverage AWS's built-in capabilities for securing API Gateway access within a VPC.
References:
https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-vpc/

## Câu 34 — ✅ ĐÚNG

<!-- source: T1Q26 · domain: ORG · time: 2:15 · first: 60:19 · visits: 1 · changes: 0 -->

### Câu hỏi

A company uses AWS Organizations. The company recently acquired a new business unit and invited the new unit’s existing account to the company’s organization. The organization uses a deny list SCP in the root of the organization and all accounts are members of a single OU named Production.
The administrators of the new business unit discovered that they are unable to access AWS Database Migration Service (DMS) to complete an in-progress migration.
Which option will temporarily allow administrators to access AWS DMS and complete the migration project?

### Các phương án

- **A.** Remove the organization's root SCPs that limit access to AWS DMS. Create an SCP that allows AWS DMS actions and apply the SCP to the Production OU.
- **B.** Create a temporary OU named Staging for the new account. Apply an SCP to the Staging OU to allow AWS DMS actions. Move the new account to the Production OU when the migration project is complete.
- **C.** Convert the organization's root SCPs from deny list SCPs to allow list SCPs to allow the required services only. Temporarily apply an SCP to the organization's root that allows AWS DMS actions for principals only in the new account.
- **D.** Create a temporary OU named Staging for the new account. Apply an SCP to the Staging OU to allow AWS DMS actions. Move the organization's deny list SCP to the Production OU. Move the new account to the Production OU when adjustments to AWS DMS are complete.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

A deny list strategy uses an implicit deny and has an SCP named AWSFullAccess applied at the root level (by default) which allows all actions. In this case the company has applied a deny list SCP at the root level which denies access to specific services.
In AWS Organizations any account has only those permissions permitted by
every
parent above it. If a permission is blocked at any level above the account, either implicitly (by not being included in an Allow policy statement) or explicitly (by being included in a Deny policy statement), a user or role in the affected account can't use that permission.
Therefore, it will not be possible to allow services in an OU that have been denied at the root level. The only solution is to move the deny list from the root level to the Production OU (which means it is still effective for all other accounts) and then create a temporary OU with an SCP that allows AWS DMS (the AWSFullAccess would do this if it has not been removed).
The diagram below depicts the temporary configuration after the DenyList SCP has been moved to the Production OU:
CORRECT:
"Create a temporary OU named Staging for the new account. Apply an SCP to the Staging OU to allow AWS DMS actions. Move the organization's deny list SCP to the Production OU. Move the new account to the Production OU when adjustments to AWS DMS are complete" is the correct answer.
INCORRECT:
"Remove the organization's root SCPs that limit access to AWS DMS. Create an SCP that allows AWS DMS actions and apply the SCP to the Production OU" is incorrect. This would enabled AWS DMS for all member accounts which is more permissions than is required so this is not the best option.
INCORRECT:
"Create a temporary OU named Staging for the new account. Apply an SCP to the Staging OU to allow AWS DMS actions. Move the new account to the Production OU when the migration project is complete" is incorrect. The deny list SCP at the root level will not allow the restricted actions to be allowed at any level beneath so this will not work.
INCORRECT:
"Convert the organization's root SCPs from deny list SCPs to allow list SCPs to allow the required services only. Temporarily apply an SCP to the organization's root that allows AWS DMS actions for principals only in the new account" is incorrect. There is considerably more work involved with converting the SCPs, it would be much simpler to move the deny list SCP from the root to the Production OU to remove restrictions from higher in the hierarchy.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 35 — ✅ ĐÚNG

<!-- source: T1Q19 · domain: NEW · time: 1:52 · first: 62:27 · visits: 1 · changes: 0 -->

### Câu hỏi

A company is building a web application hosted on Amazon EC2 instances within an Auto Scaling group, fronted by a public-facing Application Load Balancer (ALB). The application should be accessible only to users from a designated country, and the company wants to log any access attempts that are blocked. The desired solution should be low maintenance.
What approach should be taken to meet these requirements?

### Các phương án

- **A.** Create an IPSet with IP ranges specific to the target country. Set up an AWS WAF web ACL with a rule to deny requests not originating from these IP ranges. Link this rule to the web ACL and associate the web ACL with the ALB.
- **B.** Create an AWS WAF web ACL with a geo-match rule to block requests from outside the specified country. Associate this rule with the web ACL, and then attach the web ACL to the ALB.
- **C.** Implement AWS Shield with a configuration to reject requests not coming from the specified country. Integrate AWS Shield with the ALB.
- **D.** Create a security group for the ALB that only permits traffic on ports 80 and 443 from IP ranges within the specified country.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

AWS WAF (Web Application Firewall) provides the functionality to create custom web access control lists (ACLs) with specific rules. Using a geo-match rule in AWS WAF, the company can easily restrict access to users from a specific country.
This approach is not only effective but also low maintenance, as it doesn't require the manual upkeep of IP ranges. AWS WAF also offers logging capabilities, allowing the company to monitor and log any blocked access attempts. Associating this web ACL with the ALB ensures that the traffic filtering is applied directly to the incoming web traffic.
CORRECT:
"Create an AWS WAF web ACL with a geo-match rule to block requests from outside the specified country. Associate this rule with the web ACL, and then attach the web ACL to the ALB" is the correct answer (as explained above.)
INCORRECT:
"Create an IPSet with IP ranges specific to the target country. Set up an AWS WAF web ACL with a rule to deny requests not originating from these IP ranges. Link this rule to the web ACL and associate the web ACL with the ALB" is incorrect.
While creating an IPSet and associating it with a web ACL can work, maintaining an up-to-date list of IP ranges for a specific country can be cumbersome and high maintenance.
INCORRECT:
"Implement AWS Shield with a configuration to reject requests not coming from the specified country. Integrate AWS Shield with the ALB" is incorrect.
AWS Shield is primarily used for protection against DDoS attacks and does not offer the granular country-based traffic filtering required in this scenario.
INCORRECT:
"Create a security group for the ALB that only permits traffic on ports 80 and 443 from IP ranges within the specified country" is incorrect.
Security groups are not designed for complex filtering based on geographic location. Maintaining a list of IP ranges for a specific country in a security group would be labor-intensive and not practical for this use case.
References:
https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html
https://docs.aws.amazon.com/waf/latest/developerguide/logging.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-waf-shield/
