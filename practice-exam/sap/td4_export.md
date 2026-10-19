# TD Set 4 — Timed (Gate 2, 2026-10-19)

**Kết quả:** 50/75 câu đúng (66.67%) — Chưa đạt

| Domain | Score |
|---|---|
| CSAP – Accelerate Workload Migration and Modernization | 100% |
| CSAP – Continuous Improvement for Existing Solutions | 56.41% |
| CSAP – Design for New Solutions | 68% |
| CSAP – Design Solutions for Organizational Complexity | 100% |

## Câu 1 — ✅ ĐÚNG

### Câu hỏi

A technology company is developing an educational mobile app for students, with an exam feature that also allows them to submit their answers. The developers used React Native so the app can be deployed on both iOS and Android devices. They used AWS Lambda and Amazon API Gateway for the backend services and a DynamoDB table as the database service. After a month, the released app has been downloaded over 3 million times. However, there are a lot of users who complain about the slow processing of the app especially when they are submitting their answers in the multiple-choice exams. The diagrams and images on the exam also take a lot of time to load, which is not a good user experience.

Which of the following options provides the most cost-effective and scalable architecture for the application?

### Các phương án

- **A.** Enable Auto Scaling in DynamoDB with a Target Utilization of 100% and a maximum provisioned capacity of 1000 units. Use an S3 bucket to host the diagrams, images, and other static assets of the mobile app.
- **B.** Instead of DynamoDB, use RDS Multi-AZ configuration with Read Replicas. Use a web distribution in CloudFront and Amazon S3 to host the diagrams, images, and other static assets of the mobile app.
- **C.** Launch an SQS queue and develop a custom service which integrates with SQS to buffer the incoming requests. Use a web distribution in CloudFront and Amazon S3 to host the diagrams, images, and other static assets of the mobile app.
- **D.** Increase the write capacity in DynamoDB to 10,000 WCU. Use a web distribution in CloudFront with associated CloudFront Functions to host the diagrams, images and other static assets of the mobile app in real-time

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

In this scenario, the mobile app is both write and read-intensive. You can use SQS to buffer and scale the backend service to accommodate the large incoming traffic. CloudFront is the best choice to distribute the static assets of the mobile app to load it faster.

![image](https://media.tutorialsdojo.com/cloudfront_cdn_diagram.png)

SQS can help with the slowness experienced when submitting answers. You can modify your application to use SQS. For example, when the users submit their answers, instead of waiting for the complete submission and processing of all the answers you can save the submitted answers on the SQS Queue and then quickly return the user to a new page stating that the answers are successfully submitted. This improves the user experience as the user will not wait on a “loading submit” button until all the answers are processed completely. When the answers are buffered in the queue, the backend instances can now process the answers in the queue. You can then have another webpage that will show the results separately. This is a simple cost-effective design that improves user experience without increasing the capacity of your systems.

With CloudFront, the images on the S3 bucket will be cached on Edge locations close to users. This further improves the load times of the web page. Images are quickly accessed and loaded because they are physically closer (using CloudFront cache) to users around the world.

Therefor the correct answer is: **Launch an SQS queue and develop a custom service which integrates with SQS to buffer the incoming requests. Use a web distribution in CloudFront and Amazon S3 to host the diagrams, images, and other static assets of the mobile app.**

The option that says: **Enable Auto Scaling in DynamoDB with a Target Utilization of 100% and a maximum provisioned capacity of 1000 units. Use an S3 bucket to host the diagrams, images, and other static assets of the mobile app**  is incorrect because you can only set the auto scaling target utilization values between 20 and 90 percent for your read and write capacity, not 100%.

The option that says:**Increase the write capacity in DynamoDB to 10,000 WCU. Use a web distribution in CloudFront with associated CloudFront Functions to host the diagrams, images and other static assets of the mobile app in real-time**  is incorrect. Although using a CloudFront Function can reduce the latency of the processing, there are certain limitations on what it can do since this is just a JavaScript-based based feature that is commonly used to manipulate the requests and responses that flow through CloudFront, perform basic authentication and authorization, generate HTTP responses at the edge, and more. Increasing the write capacity (WCU) for the DynamoDB table may work but using a 10,000 WCU entails a significantly high cost.

The options that says: **Instead of DynamoDB, use RDS Multi-AZ configuration with Read Replicas. Use a web distribution in CloudFront and Amazon S3 to host the diagrams, images, and other static assets of the mobile app**  is incorrect because this will require changing the whole application to use an SQL database and moving from DynamoDB to RDS Multi-AZ is not cost-effective.

**References:**

[https://aws.amazon.com/sqs/](https://aws.amazon.com/sqs/)

[https://aws.amazon.com/blogs/aws/new-auto-scaling-for-amazon-dynamodb/](https://aws.amazon.com/blogs/aws/new-auto-scaling-for-amazon-dynamodb/)

**Check out this Amazon SQS Cheat Sheet:**

[https://tutorialsdojo.com/amazon-sqs/](https://tutorialsdojo.com/amazon-sqs/)

---

## Câu 2 — ✅ ĐÚNG

### Câu hỏi

A company is hosting its application and MySQL database in its on-premises data center. The database increases at about 10GB per day and is approximately 25TB in total size. The company wants to migrate the database workload to the AWS cloud. A 50Mbps VPN connection is currently in place to connect the corporate network to AWS. The company plans to complete the migration to AWS within 3 weeks with the LEAST downtime possible.

Which of the following solutions should be implemented to meet the company requirements?

### Các phương án

- **A.** Create a snapshot of the on-premises database server and use the VM Import/Export service to import the snapshot to AWS. Provision a new Amazon EC2 instance from the imported snapshot. Configure replication from the on-premises database server to the EC2 instance through the VPN connection. Wait until the replication is complete then update the database DNS entry to point to the EC2 instance. Stop the database replication.
- **B.** Create an AWS Database Migration Service (AWS DMS) instance and an Amazon Aurora MySQL DB instance. Define the on-premises database server details and the Aurora MySQL instance details on the DMS instance. Use the VPN connection to start the replication from the on-premises database server to AWS. Wait until the replication is complete then update the database DNS entry to point to the Aurora DB instance. Stop the database replication.
- **C.** Create a database export of the on-premises database server and bring it to an AWS Data Transfer Terminal facility. Once the data is imported to AWS, provision an Amazon Aurora MySQL DB instance and load the data. Using the VPN connection, configure replication from the on-premises database server to the Aurora DB instance. Wait until the replication is complete, then update the database DNS entry to point to the Aurora DB instance. Stop the database replication.
- **D.** Temporarily stop the on-premises application to stop any database I/O operations. Create a database export of the on-premises database server and bring it to an AWS Data Transfer Terminal facility. Once the data is imported to AWS, provision an Amazon Aurora MySQL DB instance and load the data. Update the database DNS entry to point to the Aurora DB instance. Start the application again to resume normal operations.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

The **AWS Data Transfer Terminal**  is a network-ready, physical facility where you can bring your data storage devices for quick transfers to and from AWS Cloud services. This service allows you to upload data collected remotely, making it easier to access that information.

![image](https://media.tutorialsdojo.com/public/Data%20Transfer%20Terminal-08JUN2026.png)

To use the Data Transfer Terminal, schedule a reservation at one of the facilities through the AWS Management Console. Arrive at your scheduled time and upload your data to your AWS Cloud services using your devices. Once your reservation is complete and you leave the facility, it will be re-secured and prepared for the next scheduled appointment.

Amazon Aurora MySQL integrates with other AWS services so that you can extend your Aurora MySQL DB cluster to use additional capabilities in the AWS Cloud. Your Aurora MySQL DB cluster can use AWS services to load data from text or XML files stored in an Amazon Simple Storage Service (Amazon S3) bucket into your DB cluster using the LOAD DATA FROM S3 or LOAD XML FROM S3 command.

Therefore, the correct answer is: **Create a database export of the on-premises database server and bring it to an AWS Data Transfer Terminal facility. Once the data is imported to AWS, provision an Amazon Aurora MySQL DB instance and load the data. Using the VPN connection, configure replication from the on-premises database server to the Aurora DB instance. Wait until the replication is complete, then update the database DNS entry to point to the Aurora DB instance. Stop the database replication.**  AWS Data Transfer Terminal can handle the bulk migration of 25TB efficiently. After the bulk load, AWS DMS can replicate ongoing changes over the VPN, ensuring minimal downtime. You can load the data to the Amazon Aurora DB instance and replicate the missing data from the on-premises database server. You can cut over to the Aurora database after replication.

The option that says: **Create a snapshot of the on-premises database server and use the VM Import/Export service to import the snapshot to AWS. Provision a new Amazon EC2 instance from the imported snapshot. Configure replication from the on-premises database server to the EC2 instance through the VPN connection. Wait until the replication is complete then update the database DNS entry to point to the EC2 instance. Stop the database replication**  is incorrect. You cannot import a 25 TB snapshot using VM Import/Export. This option does not specify whether it uses the company network to export the snapshot to AWS. If so, the 50Mbps won’t be enough to export the entire database within the 3-week window.

The option that says: **Create an AWS Database Migration Service (AWS DMS) instance and an Amazon Aurora MySQL DB instance. Define the on-premises database server details and the Aurora MySQL instance details on the DMS instance. Use the VPN connection to start the replication from the on-premises database server to AWS. Wait until the replication is complete then update the database DNS entry to point to the Aurora DB instance. Stop the database replication** is incorrect. Replicating an entire 25 TB database via the 50Mbps VPN connection will typically take several weeks for the replication to catch up. Not to mention that there will be an additional 10 GB of data to be replicated for each passing day.

The option that says: **Temporarily stop the on-premises application to stop any database I/O operations. Create a database export of the on-premises database server and bring it to an AWS Data Transfer Terminal facility. Once the data is imported to AWS, provision an Amazon Aurora MySQL DB instance and load the data. Update the database DNS entry to point to the Aurora DB instance. Start the application again to resume normal operations**  is incorrect because it requires stopping the application during migration, which causes significant downtime. The requirement is to primarily minimize downtime, so this option does not meet the company’s needs.

**References:**

[https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)

[https://docs.aws.amazon.com/datatransferterminal/latest/userguide/scheduling.html](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/scheduling.html)

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/replicate-amazon-rds-mysql-on-premises/](https://aws.amazon.com/premiumsupport/knowledge-center/replicate-amazon-rds-mysql-on-premises/)

**Check out this Amazon Aurora Cheat Sheet:**

[https://tutorialsdojo.com/amazon-aurora/](https://tutorialsdojo.com/amazon-aurora/)

---

## Câu 3 — ✅ ĐÚNG

### Câu hỏi

A leading e-commerce company plans to launch a donation website for all the victims of the recent super typhoon in South East Asia for its Corporate and Social Responsibility program. The company will advertise its program on TV and on social media, which is why they anticipate incoming traffic on their donation website. Donors can send their donations in cash, which can be transferred electronically, or they can simply post their home address where a team of volunteers can pick up their used clothes, canned goods, and other donations. Donors can optionally write a positive and encouraging message to the victims along with their donations. These features of the donation website will eventually result in a high number of write operations on their database tier considering that there are millions of generous donors around the globe who want to help.

Which of the following options is the best solution for this scenario?

### Các phương án

- **A.** Use DynamoDB as a database storage and a CloudFront web distribution for hosting static resources.
- **B.** Use an Oracle database hosted on an extra large Dedicated EC2 instance as your database tier and an SQS queue for buffering the write operations.
- **C.** Amazon DynamoDB with a provisioned write throughput. Use an SQS queue to buffer the large incoming traffic to your Auto Scaled EC2 instances, which processes and writes the data to DynamoDB.
- **D.** Use an Amazon RDS instance with Provisioned IOPS.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

In this scenario, the application is write-intensive which means that we have to implement a solution to buffer and scale out the services according to the incoming traffic. SQS can be used to handle the large incoming requests and you can use DynamoDB to store large amounts of data.

**Amazon Simple Queue Service (Amazon SQS)**  offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Amazon SQS offers common constructs such as dead-letter queues and cost allocation tags.

Amazon SQS queues can deliver very high throughput. Standard queues support a nearly unlimited number of transactions per second (TPS) per action. By default, FIFO queues support up to 3,000 messages per second with batching.

![image](https://media.tutorialsdojo.com/sap_sqs_dynamodb.png)

Therefore, the correct answer is: **Amazon DynamoDB with a provisioned write throughput. Use an SQS queue to buffer the large incoming traffic to your Auto Scaled EC2 instances, which processes and writes the data to DynamoDB.**  The SQS queue can act as a buffer to temporarily store all the requests while waiting for them to be processed and written to the DynamoDB table.

The option that says: **Use DynamoDB as a database storage and a CloudFront web distribution for hosting static resources**  is incorrect. CloudFront is used for caching static content, not for hosting the static website resources

The option that says: **Use an Oracle database hosted on an extra large Dedicated EC2 instance as your database tier and an SQS queue for buffering the write operations**  is incorrect. AWS does not recommend hosting a database on EC2 instances. RDS instances are designed for hosting databases.

The option that says: **Use an Amazon RDS instance with Provisioned IOPS**  is incorrect. This may be possible, however, this is significantly more expensive than using a DynamoDB table and adding an SQS queue.

**References:**

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-throughput-horizontal-scaling-and-batching.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-throughput-horizontal-scaling-and-batching.html)

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-client-side-buffering-request-batching.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-client-side-buffering-request-batching.html)

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

**Check out this Amazon SQS Cheat Sheet:**

[https://tutorialsdojo.com/amazon-sqs/](https://tutorialsdojo.com/amazon-sqs/)

---

## Câu 4 — ✅ ĐÚNG

### Câu hỏi

A multinational consumer goods company is currently using a VMWare vCenter Server to manage their virtual machines, multiple ESXi hosts, and all dependent components from a single centralized location. To save costs and to avail the benefits of cloud computing, the company decided to move its virtual machines to AWS. The Solutions Architect is required to generate new AMIs of the existing virtual machines which can then be launched as an EC2 instance in the company VPC.

Which combination of steps should the Solutions Architect do to properly execute the cloud migration? (Select TWO.)

### Các phương án

- **A.** Establish a Direct Connect connection between your data center and your VPC. Use AWS Service Catalog to centrally manage all your IT services and to quickly migrate virtual machines to your virtual private cloud.
- **B.** Create an AWS CloudFormation template that mirrors the on-premises virtualized environment. Deploy the stack to the AWS cloud.
- **C.** Use the AWS Application Migration Service to migrate your on-premises workloads to the AWS cloud.
- **D.** Install the AWS Replication Agent in your on-premises virtualization environment.
- **E.** Use Serverless Application Model (SAM) to migrate the virtual machines (VMs) to AWS and automatically launch an Amazon ECS Cluster to host the VMs.

> **Bạn chọn:** C, D
> **Đáp án đúng:** C, D

### Giải thích

**AWS Application Migration Service (MGN)**  is a highly automated lift-and-shift (rehost) solution that simplifies, expedites, and reduces the cost of migrating applications to AWS. It enables companies to lift and shift a large number of physical, virtual, or cloud servers without compatibility issues, performance disruption, or long cutover windows.

MGN replicates source servers into your AWS account. When you’re ready, it automatically converts and launches your servers on AWS so you can quickly benefit from the cost savings, productivity, resilience, and agility of the Cloud.

Once your applications are running on AWS, you can leverage AWS services and capabilities to quickly and easily re-platform or refactor those applications – which makes lift-and-shift a fast route to modernization.

![image](https://media.tutorialsdojo.com/sap_aws_mgn_overview.jpg)

Therefore, the correct answers are:

**– Use the AWS Application Migration Service to migrate your on-premises workloads to the AWS cloud.**

**– Install the AWS Replication Agent in your on-premises virtualization environment.**

The option that says: **Use Serverless Application Model (SAM) to migrate the virtual machine (VMs) to AWS and**  **automatically launch an Amazon ECS Cluster to host the VMs**  is incorrect because the Serverless Application Model (SAM) service is primarily used to build serverless applications on AWS, and not to migrate virtual machines from your on-premises data center.

The option that says:**Create an AWS CloudFormation template that mirrors the on-premises virtualized environment. Deploy the stack to the AWS cloud** is incorrect. This is possible; however, this will create new AMIs that are from AWS, not from the existing VMs. CloudFormation is ideal for creating and deploying new environments in the AWS Cloud.

The option that says: **Establish a Direct Connect connection between your data center and your VPC. Use AWS Service Catalog to centrally manage all your IT services and to quickly migrate virtual machines to your virtual private cloud**  is incorrect. The AWS Service Catalog is primarily used to allow organizations to create and manage catalogs of IT services that are approved for use on AWS. It enables you to centrally manage commonly deployed IT services and helps you achieve consistent governance and meet your compliance requirements while enabling users to quickly deploy only the approved IT services they need. However, this service is not suitable for migrating your virtual machines.

**References:**

[https://aws.amazon.com/application-migration-service/](https://aws.amazon.com/application-migration-service/)

[https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)

[https://docs.aws.amazon.com/mgn/latest/ug/quick-start-guide-gs.html](https://docs.aws.amazon.com/mgn/latest/ug/quick-start-guide-gs.html)

**Check out this AWS Application Migration Service Cheat Sheet:**

[https://tutorialsdojo.com/aws-application-migration-service/](https://tutorialsdojo.com/aws-application-migration-service/)

---

## Câu 5 — ❌ SAI

### Câu hỏi

A digital banking company runs its production workload on the AWS cloud. The company has enabled multi-region support on an AWS CloudTrail trail. As part of the company security policy, the creation of any IAM users must be approved by the security team. When an IAM user is created, all of the permissions from that user must be removed automatically. A notification must then be sent to the security team to approve the user creation.

Which of the following options should the solutions architect implement to meet the company requirements? (Select THREE.)

### Các phương án

- **A.** Create a rule in Amazon EventBridge that will check for patterns in AWS CloudTrail API calls with the CreateUser eventName.
- **B.** Use Amazon AWS Audit Manager to continually audit newly created users and send a notification to the security team.
- **C.** Use Amazon EventBridge to invoke an AWS Step Function state machine that will remove permissions on the newly created IAM user.
- **D.** Send a message to an Amazon Simple Notification Service (Amazon SNS) topic. Have the security team subscribe to the SNS topic.
- **E.** Configure an event filter in AWS CloudTrail for the CreateUser event and send a notification to an Amazon Simple Notification Service (Amazon SNS) topic.
- **F.** Use Amazon EventBridge to invoke an AWS Fargate tasks that will remove permissions on the newly created IAM user.

> **Bạn chọn:** D, E, F
> **Đáp án đúng:** A, C, D

### Giải thích

Using IAM, you can manage access to AWS services and resources securely. You can create and manage AWS users and groups and use permissions to allow and deny those users and groups access to AWS resources.

You can create an **Amazon EventBridge**  rule with an event pattern that matches a specific IAM API call or multiple IAM API calls. Then, associate the rule with an **Amazon Simple Notification Service (Amazon SNS)**  topic. When the rule runs, an SNS notification is sent to the corresponding subscriptions.

Amazon EventBridge works with **AWS CloudTrail** , a service that records actions from AWS services. CloudTrail captures API calls made by or on behalf of your AWS account from the EventBridge console and to EventBridge API operations.

Using the information collected by CloudTrail, you can determine what request was made to EventBridge, the IP address from which the request was made, who made the request, when it was made, and more. When an event occurs in EventBridge, CloudTrail records the event in Event history. You can view, search, and download recent events in your AWS account.

![image](https://media.tutorialsdojo.com/sap_cloudtrail_event_notification.png)

The option that says: **Use Amazon EventBridge to invoke an AWS Step Function state machine that will remove permissions on the newly created IAM user**  is correct. When Amazon EventBridge detects a pattern from the specified events, it can trigger an AWS Step Function that has specific actions.

The option that says: **Send a message to an Amazon Simple Notification Service (Amazon SNS) topic. Have the security team subscribe to the SNS topic**  is correct. If you create a pattern in Amazon EventBridge, it can then send a message to an SNS Topic once the event is detected.

The option that says: **Create a rule in Amazon EventBridge that will check for patterns in AWS CloudTrail API calls with the CreateUser eventName**  is correct. With Amazon EventBridge, you define patterns to scan events that happen in your AWS account, such as creating an IAM user.

The option that says: **Configure an event filter in AWS CloudTrail for the CreateUser event and send a notification to an Amazon Simple Notification Service (Amazon SNS) topic**  is incorrect. You can filter events on CloudTrail by searching for keywords, however, you can’t configure it to send notifications to Amazon SNS. You should use EventBridge for this scenario.

The option that says: **Use Amazon AWS Audit Manager to continually audit newly created users and send a notification to the security team**  is incorrect. AWS Audit Manager is used to map compliance requirements to AWS usage data with prebuilt and custom frameworks and automated evidence collection, not for scanning IAM user creation events.

The option that says: **Use Amazon EventBridge to invoke an AWS Fargate tasks that will remove permissions on the newly created IAM user**  is incorrect. Amazon EventBridge cannot directly invoke AWS Fargate tasks.

**References:**

[https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/iam-eventbridge-sns-rule/](https://aws.amazon.com/premiumsupport/knowledge-center/iam-eventbridge-sns-rule/)

[https://aws.amazon.com/premiumsupport/knowledge-center/sns-email-notifications-eventbridge/](https://aws.amazon.com/premiumsupport/knowledge-center/sns-email-notifications-eventbridge/)

**Check out these Amazon CloudWatch and AWS Simple Notification Service Cheat Sheets:**

[https://tutorialsdojo.com/amazon-cloudwatch/](https://tutorialsdojo.com/amazon-cloudwatch/)

[https://tutorialsdojo.com/amazon-sns/](https://tutorialsdojo.com/amazon-sns/)

---

## Câu 6 — ✅ ĐÚNG

### Câu hỏi

A FinTech startup has recently consolidated its multiple AWS accounts using AWS Organizations. It currently has two teams in its organization, a security team and a development team. The former is responsible for protecting their cloud infrastructure and making sure that all of their resources are compliant, while the latter is responsible for developing new applications that are deployed to EC2 instances. The security team is required to set up a system that will check if all of the running EC2 instances are using an approved AMI. However, the solution should not stop the development team from deploying an EC2 instance running on a non-approved AMI. The disruption is only allowed once the deployment has been completed**.**  In addition, they have to set up a notification system that sends the compliance state of the resources to determine whether they are compliant.

Which of the following options is the most suitable solution that the security team should implement?

### Các phương án

- **A.** Use the Amazon Inspector service to automatically check all of the AMIs that are being used by your EC2 instances. Set up an SNS topic that will send a notification to both the security and development teams if there is a non-compliant EC2 instance running in their VPCs.
- **B.** Create and assign an SCP and an IAM policy that restricts the AWS accounts and the development team from launching an EC2 instance using an unapproved AMI. Create a CloudWatch alarm that will automatically notify the security team if there are non-compliant EC2 instances running in their VPCs.
- **C.** Use an AWS Config Managed Rule and specify a list of approved AMI IDs. This rule will check whether running EC2 instances are using specified AMIs. Configure AWS Config to stream configuration changes and notifications to an Amazon SNS topic which will send a notification for non-compliant instances.
- **D.** Set up a Trusted Advisor check that will verify whether the running EC2 instances in your VPCs are using approved AMIs. Create a CloudWatch alarm and integrate it with the Trusted Advisor metrics that will check all of the AMIs being used by your EC2 instances and that will send a notification if there is a running instance which uses an unapproved AMI.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

When you run your applications on AWS, you usually use AWS resources, which you must create and manage collectively. As the demand for your application keeps growing, so does your need to keep track of your AWS resources. AWS Config is designed to help you oversee your application resources.

![image](https://media.tutorialsdojo.com/sap_config_how_it_works.png)

**AWS Config**  provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time. With AWS Config, you can do the following:

– Evaluate your AWS resource configurations for desired settings.

– Get a snapshot of the current configurations of the supported resources that are associated with your AWS account.

– Retrieve configurations of one or more resources that exist in your account.

– Retrieve historical configurations of one or more resources.

– Receive a notification whenever a resource is created, modified, or deleted.

– View relationships between resources. For example, you might want to find all resources that use a particular security group.

AWS Config provides *AWS managed rules* , which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices. In this scenario, you can use the `**approved-amis-by-id** ` AWS managed rule which checks whether running instances are using specified AMIs.

Therefore, the correct answer is: **Use an AWS Config Managed Rule and specify a list of approved AMI IDs. This rule will check whether running EC2 instances are using specified AMIs. Configure AWS Config to stream configuration changes and notifications to an Amazon SNS topic which will send a notification for non-compliant instances.**

The option that says: **Create and assign an SCP and an IAM policy that restricts the AWS accounts and the development team from launching an EC2 instance using an unapproved AMI. Create a CloudWatch alarm that will automatically notify the security team if there are non-compliant EC2 instances running in their VPCs**  is incorrect. Setting up an SCP and IAM Policy will totally restrict the development team from launching EC2 instances with unapproved AMIs. The scenario clearly says that the solution should not have this kind of restriction.

The option that says: **Use the Amazon Inspector service to automatically check all of the AMIs that are being used by your EC2 instances. Set up an SNS topic that will send a notification to both the security and development teams if there is a non-compliant EC2 instance running in their VPCs**  is incorrect. The Amazon Inspector service is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. It does not have the capability to detect EC2 instances that are using unapproved AMIs, unlike AWS Config.

The option that says: **Set up a Trusted Advisor check that will verify whether the running EC2 instances in your VPCs are using approved AMIs. Create a CloudWatch alarm and integrate it with the Trusted Advisor metrics that will check all of the AMIs being used by your EC2 instances and that will send a notification if there is a running instance which uses an unapproved AMI**  is incorrect. AWS Trusted Advisor is primarily used to check if your cloud infrastructure is in compliance with the best practices and recommendations across five categories: cost optimization, security, fault tolerance, performance, and service limits. Their security checks for EC2 do not cover the checking of individual AMIs that are being used by your EC2 instances.

**References:**

[https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-id.html](https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-id.html)

[https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html)

**Check out this AWS Config Cheat Sheet:**

[https://tutorialsdojo.com/aws-config/](https://tutorialsdojo.com/aws-config/)

---

## Câu 7 — ✅ ĐÚNG

### Câu hỏi

A company stores confidential financial documents as well as sensitive corporate information in an Amazon S3 bucket. There is a new security policy that prohibits any public S3 objects in the company’s S3 bucket. In the event that a public object was identified, the IT Compliance team must be notified immediately and the object’s permissions must be remediated automatically. The notification must be sent as soon as a public object was created in the bucket.

What is the MOST suitable solution that should be implemented by the Solutions Architect to comply with this data policy?

### Các phương án

- **A.** Set up a Systems Manager (SSM) Automation document that changes any public object in the bucket to private. Integrate Amazon EventBridge with AWS Lambda to create a scheduled process that checks the S3 bucket every hour. Configure the Lambda function to invoke the SSM Automation document when a public object is identified and to notify the IT Compliance team via email using Amazon SNS.
- **B.** Enable object-level logging in the S3 bucket to automatically track S3 actions using CloudTrail. Set up an Amazon EventBridge rule with an SNS Topic to notify the IT Compliance team when a `PutObject` API call with public-read permission is detected in the CloudTrail logs. Launch another CloudWatch Events rule that invokes an AWS Lambda function to turn the newly uploaded public object to private.
- **C.** Integrate Amazon Lex with Amazon GuardDuty to detect public objects in the S3 bucket and to automatically update the permission of a public object to private. Associate an SNS Topic to Amazon Lex to notify the IT Compliance team via email if a public object was identified.
- **D.** Automatically track S3 actions using the Trusted Advisor API and AWS Cloud Development Kit (CDK). Set up an Amazon EventBridge rule with an Amazon SNS Topic to notify the IT Compliance team when the Trusted Advisor detected a `PutObject` API call with public-read permission. Launch another CloudWatch Events rule that invokes an AWS Lambda function to turn the newly uploaded public object to private.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

**Amazon S3**  is integrated with **AWS CloudTrail** , a service that provides a record of actions taken by a user, role, or an AWS service in Amazon S3. CloudTrail captures a subset of API calls for Amazon S3 as events, including calls from the Amazon S3 console and from code calls to the Amazon S3 APIs. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon S3. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in the Event history. Using the information collected by CloudTrail, you can determine the request that was made to Amazon S3, the IP address from which the request was made, who made the request, when it was made, and additional details.

![image](https://media.tutorialsdojo.com/sap_cloudtrail_s3_lambda_sns.jpg)

You can also get CloudTrail logs for object-level Amazon S3 actions. To do this, specify the Amazon S3 object for your trail. When an object-level action occurs in your account, CloudTrail evaluates your trail settings. If the event matches the object that you specified in a trail, the event is logged.

**Amazon EventBridge**  is a serverless event bus service that you can use to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your applications, software as a service (SaaS) applications, and AWS services to targets such as AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts. A rule matches incoming events and sends them to targets for processing. A single rule can send an event to multiple targets, which then run in parallel. Rules are based either on an event pattern or a schedule. An event pattern defines the event structure and the fields that a rule matches. Rules that are based on a schedule perform an action at regular intervals.

Hence, the correct answer is: **Enable object-level logging in the S3 bucket to automatically track S3 actions using CloudTrail. Set up an Amazon EventBridge rule with an SNS Topic to notify the IT Compliance team when a `PutObject` API call with public-read permission is detected in the CloudTrail logs. Launch another CloudWatch Events rule that invokes an AWS Lambda function to turn the newly uploaded public object to private.**

The option that says: **Set up a Systems Manager (SSM) Automation document that changes any public object in the bucket to private. Integrate Amazon EventBridge with AWS Lambda to create a scheduled process that checks the S3 bucket every hour. Configure the Lambda function to invoke the SSM Automation document when a public object was identified and to notify the IT Compliance team via email using Amazon SNS**  is incorrect because the requirement says that the notification must be sent as soon as a public object was created in the bucket. Running the process to check for public objects ever hour will cause delays in detecting a public object in the S3 bucket.

The option that says: **Automatically track S3 actions using the Trusted Advisor API and AWS Cloud Development Kit (CDK). Set up an Amazon EventBridge rule with an Amazon SNS Topic to notify the IT Compliance team when the Trusted Advisor detected a `PutObject` API call with public-read permission. Launch another CloudWatch Events rule that invokes an AWS Lambda function to turn the newly uploaded public object to private**  is incorrect. Using the Trusted Advisor as a web service to track all S3 actions is not enough as it only provides high-level data about your S3 bucket, excluding the object-level permissions. A better solution is to enable the object-level logging in the S3 bucket.

The option that says: **Integrate Amazon Lex with Amazon GuardDuty to detect public objects in the S3 bucket and to automatically update the permission of a public object to private. Associate an SNS Topic to Amazon Lex to notify the IT Compliance team via email if a public object was identified**  is incorrect because Amazon Lex is simply a service for building conversational interfaces into any application using voice and text. In addition, Amazon GuardDuty is just a threat detection service that analyzes continuous streams of meta-data generated from your account and network activity found in AWS CloudTrail Events, Amazon VPC Flow Logs, and DNS Logs. These two services are not suitable in detecting public objects in your S3 bucket.

**References** :

[https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/log-s3-data-events.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/log-s3-data-events.html)

[https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudtrail-logging.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudtrail-logging.html)

[https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)

[https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)

**Check out this Amazon CloudWatch Cheat Sheet:**

[https://tutorialsdojo.com/amazon-cloudwatch/](https://tutorialsdojo.com/amazon-cloudwatch/)

---

## Câu 8 — ✅ ĐÚNG

### Câu hỏi

An enterprise is in the process of integrating the systems of the smaller companies it has acquired in the past few months. The company wants to create an AWS Landing Zone that will allow hundreds of new employees to use their corporate credentials to log in to the AWS Console. The company is using a Microsoft Active Directory (AD) service for user authentication and has an AWS Direct Connect connection to AWS. The newly acquired companies come from a wide range of engineering fields so it is required that the solution will be able to federate third-party services and providers as well as custom applications.

Which of the following implementations will meet the company requirements with the LEAST amount of management overhead?

### Các phương án

- **A.** Connect the company on-premises Active Directory using the AWS Directory Service AD connector to create a single sign-on experience for users. Configure IAM and service roles to enable federation support. Configure single sign-on integrations for connections with third-party applications.
- **B.** Create an IAM role that identifies your identity provider. Create an Active Directory Federation Services (AD FA) with SAML 2.0 to connect the company Active Directory to AWS. Configure the AD FS to use Regex with the AD naming convention for the security group. This will allow federation on all AWS accounts. Configure single sign-on integrations for third party applications by adding them to the AD FS server as a principal (trusted entity).
- **C.** Configure AWS IAM Identity Center with AWS Organizations to manage SSO access and permissions on AWS. Set up a two-way forest trust relationship between the AWS Directory service and the company Active Directory to allow users to use their corporate credentials when logging in to AWS. Leverage on the third-party integration support of AWS IAM Identity Center.
- **D.** Create an Active Directory Federation Services (AD FS) portal page with the company branding. Integrate third-party applications on this portal with SAML 2.0 support. Use single sign-on with the AD FS to connect the company Active Directory to AWS. Configure the Identity Provider (IdP) to use form-based authentication with the portal page.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

**AWS IAM Identity Center**  (successor to AWS Single Sign-On) expands the capabilities of AWS Identity and Access Management (IAM) to provide a central place that brings together administration of users and their access to AWS accounts and cloud applications. Although the service name AWS Single Sign-On has been retired, the term single sign-on is still used throughout this guide to describe the authentication scheme that allows users to sign in one time to access multiple applications and websites.

With IAM Identity Center, you can manage sign-in security for your workforce by creating or connecting your users and groups to AWS in one place. With multi-account permissions, you can assign your workforce identities access to AWS accounts. You can use application assignments to assign your users access to software as a service (SaaS) applications. With a single click, IAM Identity Center enabled application admins can assign access to your workforce users and can also use application assignments to assign your users access to the software as a service (SaaS) applications.

![image](https://media.tutorialsdojo.com/sap_aws_directory_service.png)

AWS IAM Identity Center has integration with Microsoft AD through the **AWS Directory Service** . This means your employees can sign in to your AWS access portal using their corporate Active Directory credentials. To grant Active Directory users access to accounts and applications, you simply add them to the appropriate Active Directory groups. For example, you can grant the DevOps group SSO access to your production AWS accounts. Users added to the DevOps group are then granted SSO access to these AWS accounts automatically. This automation makes it easy to onboard new users and gives existing users access to new accounts and applications quickly.

You can configure one and two-way external and forest trust relationships between your AWS Directory Service for Microsoft Active Directory and on-premises directories, as well as between multiple AWS Managed Microsoft AD directories in the AWS cloud. AWS Managed Microsoft AD supports all three trust relationship directions: Incoming, Outgoing, and Two-way (Bi-directional). AWS Managed Microsoft AD supports both external and forest trusts.

Users in your self-managed Active Directory (AD) can also have SSO access to AWS accounts and cloud applications in the AWS access portal. To do that, AWS Directory Service has the following two options available:

**Create a two-way trust relationship**  – When two-way trust relationships are created between AWS Managed Microsoft AD and a self-managed AD, users in your self-managed AD can sign in with their corporate credentials to various AWS services and business applications. One-way trusts do not work with AWS IAM Identity Center.

AWS IAM Identity Center (successor to AWS Single Sign-On) requires a two-way trust so that it has permission to read user and group information from your domain to synchronize user and group metadata. IAM Identity Center uses this metadata when assigning access to permission sets or applications. User and group metadata is also used by applications for collaboration, like when you share a dashboard with another user or group. The trust from AWS Directory Service for Microsoft Active Directory to your domain permits IAM Identity Center to trust your domain for authentication. The trust in the opposite direction grants AWS permissions to read user and group metadata.

**Create an AD Connector**  – AD Connector is a directory gateway that can redirect directory requests to your self-managed AD without caching any information in the cloud.

Therefore, the correct answer is: **Configure AWS IAM Identity Center with AWS Organizations to manage SSO access and permissions on AWS. Set up a two-way forest trust relationship between the AWS Directory service and the company Active Directory to allow users to use their corporate credentials when logging in to AWS. Leverage on the third-party integration support of AWS IAM Identity Center.**

The option that says: **Create an Active Directory Federation Services (AD FS) portal page with the company branding. Integrate third-party applications on this portal with SAML 2.0 support. Use single sign-on with the AD FS to connect the company Active Directory to AWS. Configure the Identity Provider (IdP) to use form-based authentication with the portal page**  is incorrect. This may be possible, but creating a form-based authentication defeats the purpose of a single sign-on. Also, this requires more additional management to create the AD FS portal page.

The option that says: **Connect the company on-premises Active Directory using the AWS Directory Service AD connector to create a single sign-on experience for users. Configure IAM and service roles to enable federation support. Configure single sign-on integrations for connections with third-party applications**  is incorrect. This does not address the third-party integrations because when using the AD connector for SSO, you cannot use both on-premises AD and third-party integrations at the same time.

The option that says: **Create an Active Directory Federation Services (AD FS) with SAML 2.0 to connect the company Active Directory to AWS. Configure the AD FS to use Regex with the AD naming convention for the security group. This will allow federation on all AWS accounts. Configure single sign-on integrations for third party applications by adding them to the AD FS server as a principal (trusted entity)**  is incorrect. This is possible but will require more management overhead compared to just using AWS IAM Identity Center service. Using Regex is favorable if you have established standard naming conventions, however, you may encounter some problems if other companies are not using your expected naming convention.

**References:**

[https://docs.aws.amazon.com/singlesignon/latest/userguide/connectonpremad.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/connectonpremad.html)

[https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_setup_trust.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_setup_trust.html)

[https://docs.microsoft.com/en-us/azure/active-directory-domain-services/concepts-forest-trust](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/concepts-forest-trust)

**Check out this AWS Directory Service Cheat Sheet:**

[https://tutorialsdojo.com/aws-directory-service/](https://tutorialsdojo.com/aws-directory-service/)

---

## Câu 9 — ✅ ĐÚNG

### Câu hỏi

A software development company based in New Jersey has tasked the solutions architect to design the network architecture for their new enterprise resource planning (ERP) system in AWS. The new system should allow access to business managers and analysts over the Internet, whether they are in their hotel rooms, cafes, or elsewhere. However, the ERP system should not be publicly accessible by anyone over the Internet but only by authorized personnel.

Which of the following network design meets the above requirements while minimizing deployment and operational costs?

### Các phương án

- **A.** Establish an SSL VPN solution in a public subnet of your VPC. Install and configure SSL VPN client software on all the workstations/laptops of the users who need access to the ERP system. Create a private subnet in your VPC and place your application servers behind it.
- **B.** Establish an AWS Direct Connect connection and create a private interface to your VPC. Create a public subnet and place your app servers in it.
- **C.** Establish an IPsec VPN connection and provide the users with the configuration details. Create a public subnet in your VPC, and place your application servers in it.
- **D.** Deploy the ERP system behind an Elastic Load Balancer with an SSL certificate to allow HTTPS connections.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

**Secure Sockets Layer (SSL) VPN**  is an emerging technology that provides remote-access VPN capability, using the SSL function that is already built into a modern web browser. SSL VPN allows users from any Internet-enabled location to launch a web browser to establish remote-access VPN connections, thus promising productivity enhancements and improved availability, as well as further IT cost reduction for VPN client software and support.

![image](https://media.tutorialsdojo.com/sap_aws_vpn.png)

Always keep in mind to install the SSL VPN software in your EC2 instances which are deployed in the public subnet. This will be where your users can connect to the Internet to be able to access the business applications, which is deployed in the private subnet of your VPC.

Therefore, the correct answer is: **Establish an SSL VPN solution in a public subnet of your VPC. Install and configure SSL VPN client software on all the workstations/laptops of the users who need access to the ERP system. Create a private subnet in your VPC and place your application servers behind it** . Configuring the SSL VPN solution is cost-effective and allows access only for business travelers and remote employees. And since the application servers are in the private subnet, the application is not accessible via the Internet.

The option that says: **Establish an AWS Direct Connect connection and create a private interface to your VPC. Create a public subnet and place your app servers in it**  is incorrect. AWS Direct Connect is not a cost-effective solution compared with a VPN solution.

The option that says: **Deploy the ERP system behind an Elastic Load Balancer with an SSL certificate to allow HTTPS connections**  is incorrect. It does not mention how the application would be accessible only for business travelers and remote employees, and not to the public.

The option that says: **Establish an IPsec VPN connection and provide the users with the configuration details. Create a public subnet in your VPC, and place your application servers in it**  is incorrect. If the application servers are put in the public subnet, they would be publicly accessible via the Internet.

**References:**

[https://aws.amazon.com/quickstart/architecture/aviatrix-user-vpn/](https://aws.amazon.com/quickstart/architecture/aviatrix-user-vpn/)

[https://aws.amazon.com/articles/connecting-multiple-vpcs-with-ec2-instances-ssl](https://aws.amazon.com/articles/connecting-multiple-vpcs-with-ec2-instances-ssl)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 10 — ✅ ĐÚNG

### Câu hỏi

A company has several applications written in TypeScript and Python hosted on the AWS cloud. The company uses an automated deployment solution for its applications using AWS CloudFormation templates and AWS CodePipeline. The company recently acquired a new business unit that uses Python scripts to deploy applications on AWS. The developers from the new business are having difficulty migrating their deployments to AWS CloudFormation because they need to learn a new domain-specific language and their old Python scripts require programming loops, which are not supported in CloudFormation.

Which of the following is the recommended solution to address the developers’ concerns and help them update their deployment procedures?

### Các phương án

- **A.** Write new CloudFormation templates for the deployments of the new business unit. Extract parts of the Python scripts to be added as EC2 user data. Deploy the CloudFormation templates using the AWS Cloud Development Kit (AWS CDK). Add a stage on AWS CodePipeline to integrate AWS CDK using the templates for the application deployment.
- **B.** Create a standard deployment process for the company and the new business unit by leveraging a third-party resource provisioning engine on AWS CodeBuild. Add a stage on AWS CodePipeline to integrate AWS CodeBuild on the application deployment.
- **C.** Write TypeScript or Python code that will define AWS resources. Convert these codes to AWS CloudFormation templates by using AWS Cloud Development Kit (AWS CDK). Create CloudFormation stacks using AWS CDK. Create an AWS CodeBuild job that includes AWS CDK and add this stage to AWS CodePipeline.
- **D.** Ask the developers to continue using Python scripts for deploying new resources. Once the resources are created, import them into a new CloudFormation stack.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

**AWS Cloud Development Kit (AWS CDK)**  is a software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.

**AWS CloudFormation**  enables you to:

– Create and provision AWS infrastructure deployments predictably and repeatedly.

– Leverage AWS products such as Amazon EC2, Amazon Elastic Block Store, Amazon SNS, Elastic Load Balancing, and Auto Scaling.

– Build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure.

– Use a template file to create and delete a collection of resources together as a single unit (a stack).

Use the AWS CDK to define your cloud resources in a familiar programming language. The AWS CDK supports TypeScript, JavaScript, Python, Java, and C#/.Net. Developers can use one of the supported programming languages to define reusable cloud components known as Constructs.

![image](https://media.tutorialsdojo.com/sap_aws_cdk_appstacks.png)

The **AWS Cloud Development Kit (AWS CDK)**  lets you define your cloud infrastructure as code in one of five supported programming languages. It is intended for moderately to highly experienced AWS users. An AWS CDK app is an application written in TypeScript, JavaScript, Python, Java, or C# that uses the AWS CDK to define AWS infrastructure. An app defines one or more stacks. Stacks (equivalent to AWS CloudFormation stacks) contain constructs, each of which defines one or more concrete AWS resources, such as Amazon S3 buckets, Lambda functions, Amazon DynamoDB tables, and so on.

Constructs (as well as stacks and apps) are represented as types in your programming language of choice. You instantiate constructs within a stack to declare them to AWS and connect them to each other using well-defined interfaces.

The AWS CDK lets you easily define applications in the AWS Cloud using your programming language of choice. To deploy your applications, you can use **AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline** . Together, they allow you to build what’s called a deployment pipeline for your application.

Therefore, the correct answer is: **Write TypeScript or Python code that will define AWS resources. Convert these codes to AWS CloudFormation templates by using AWS Cloud Development Kit (AWS CDK). Create CloudFormation stacks using AWS CDK. Create an AWS CodeBuild job that includes AWS CDK and add this stage to AWS CodePipeline.**  With this solution, the developers no longer need to learn the AWS CloudFormation specific language as they can continue writing TypeScript or Python scripts. The AWS CDK stacks can be converted to AWS CloudFormation templates which can be integrated into the company deployment process.

The option that says: **Write new CloudFormation templates for the deployments of the new business unit. Extract parts of the Python scripts to be added as EC2 user data. Deploy the CloudFormation templates using the AWS Cloud Development Kit (AWS CDK). Add a stage on AWS CodePipeline to integrate AWS CDK using the templates for the application deployment**  is incorrect. This is possible but you don’t have to write new CloudFormation templates. AWS CDK can convert the TypeScript and Python code to create AWS CDK stacks and convert them to CloudFormation templates.

The option that says: **Create a standard deployment process for the company and the new business unit by leveraging a third-party resource provisioning engine on AWS CodeBuild. Add a stage on AWS CodePipeline to integrate AWS CodeBuild on the application deployment**  is incorrect. You don’t have to rely on third-party resources to standardize the deployment process. AWS CDK already allows you to write CloudFormation templates in TypeScript or Python.

The option that says: **Ask the developers to continue using Python scripts for deploying new resources. Once the resources are created, import them into a new CloudFormation stack**  is incorrect. This approach requires a lot of work to make sure resources fit the CloudFormation template and could introduce errors and mismatches between manually made resources and their CloudFormation versions. You typically import existing resources into a CloudFormation stack to bring already-deployed AWS resources under CloudFormation’s management. Deliberately creating resources outside of CloudFormation only to import them later is inefficient and counterintuitive.

**References:**

[https://docs.aws.amazon.com/cdk/latest/guide/codepipeline_example.html](https://docs.aws.amazon.com/cdk/latest/guide/codepipeline_example.html)

[https://docs.aws.amazon.com/cdk/latest/guide/home.html](https://docs.aws.amazon.com/cdk/latest/guide/home.html)

[https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)

**Check out these AWS CloudFormation and AWS CodePipeline Cheat Sheets:**

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

[https://tutorialsdojo.com/aws-codepipeline/](https://tutorialsdojo.com/aws-codepipeline/)

---

## Câu 11 — ✅ ĐÚNG

### Câu hỏi

A retail company runs its customer support call system on its in-house data center. The Solutions Architect was tasked to migrate the call system to AWS and leverage the use of managed services to reduce management overhead. The solution must be able to handle the current tasks such as receiving calls and creating contact flows. It must be able to scale to handle more calls as the customer base grows. The company also wants to add deep learning capabilities to the call system to reduce the need to speak to an agent. It must be able to recognize the intent of the caller based on certain keywords and handle basic tasks, as well as provide information to the call center agents.

Which combination of actions should the Solutions Architect implement to meet the company’s requirements? (Select TWO.)

### Các phương án

- **A.** Use an Amazon Lex bot to recognize callers' intent.
- **B.** Leverage Amazon Rekognition to identify the caller and process the voice through Amazon Polly to determine the intent based on the customer’s voice.
- **C.** Use the Amazon Connect service to create an omnichannel cloud-based contact center for the agents.
- **D.** Send incoming customer calls to an Amazon Kinesis stream and process their voice through Amazon Comprehend to determine the customer’s intent.
- **E.** Build a conversational interface on Amazon Alexa for Business to have AI-based answers to customer queries, thereby reducing the need to speak to an agent.

> **Bạn chọn:** A, C
> **Đáp án đúng:** A, C

### Giải thích

**Amazon Connect**  is an easy-to-use omnichannel cloud contact center that helps companies provide superior customer service across voice, chat, and tasks at a lower cost than traditional contact center systems. You can set up a contact center in a few steps, add agents who are located anywhere, and start engaging with your customers.

You can create personalized experiences for your customers using omnichannel communications. For example, you can dynamically offer chat and voice contact based on such factors as customer preference and estimated wait times. Agents, meanwhile, conveniently handle all customers from just one interface. For example, they can chat with customers and create or respond to tasks as they are routed to them.

The following diagram shows these key characteristics of Amazon Connect.

![image](https://media.tutorialsdojo.com/sap_amazon_connect.png)

To help provide a better contact center, you can use Amazon Connect to integrate with several AWS services to provide Machine Learning (ML) and Artificial Intelligence (AI) capabilities.

Amazon Connect uses the following services for ML/AI:

**Amazon Lex** —Let you create a chatbot to use as an Interactive Voice Response (IVR).

**Amazon Polly** —Provides text-to-speech in all contact flows.

**Amazon Transcribe** —Grabs conversation recordings from Amazon S3 and transcribes them to text so you can review them.

**Amazon Comprehend** —Takes the transcription of recordings and applies speech analytics machine learning to the call to identify sentiment, keywords, adherence to company policies, and more.

**Amazon Lex**  is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text and natural language understanding (NLU) to recognize the intent of the text to enable you to build applications with highly engaging user experiences and lifelike conversational interactions.

By using an Amazon Lex chatbot in your call center, callers can perform tasks such as changing a password, requesting a balance on an account, or scheduling an appointment without needing to speak to an agent. These chatbots use automatic speech recognition and natural language understanding to ascertain a caller’s intent, maintain context and fluidly manage the conversation. Amazon Lex uses AWS Lambda functions to query your business applications, provide information back to callers, and make updates as requested.

The option that says: **Use the Amazon Connect service to create an omnichannel cloud-based contact center for the agents**  is correct. Amazon Connect is the AWS service you will want to use to build a cloud-based call center system.

The option that says: **Use an Amazon Lex bot to recognize callers’ intent** is correct. Amazon Lex provides the deep learning capabilities required to recognize the intent of a caller based on certain keywords and handle basic tasks autonomously. It integrates well with Amazon Connect, allowing the creation of conversational interfaces that can interact with users effectively.

The option that says: **Leverage Amazon Rekognition to identify the caller and process the voice through Amazon Polly to determine the intent based on the customer’s voice**  is incorrect. Amazon Rekognition is used to identify persons on photos or videos, not on voice calls. Amazon Polly is used for text-to-speech services. You should use Amazon Lex for this scenario.

The option that says: **Build a conversational interface on Amazon Alexa for Business to have AI-based answers to customer queries, thereby reducing the need to speak to an agent.**  is incorrect. Alexa for Business gives you the tools you need to manage Alexa devices, enroll your users, and assign skills at scale for your organization. For conversational interfaces such as chatbots, you can use Amazon Lex.

The option that says: **Send incoming customer calls to an Amazon Kinesis stream and process their voice through Amazon Comprehend to determine the customer’s intent**  is incorrect. Amazon Comprehend processes text and applies speech analysis. It can’t handle speech from audio sources. The scenario requires understanding the intent of the user based on their speech, so Amazon Lex is better suited for this.

**References:**

[https://aws.amazon.com/connect/](https://aws.amazon.com/connect/)

[https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)

[https://docs.aws.amazon.com/connect/latest/adminguide/related-services-amazon-connect.html](https://docs.aws.amazon.com/connect/latest/adminguide/related-services-amazon-connect.html)

[https://aws.amazon.com/blogs/machine-learning/delivering-natural-conversational-experiences-using-amazon-lex-streaming-apis/](https://aws.amazon.com/blogs/machine-learning/delivering-natural-conversational-experiences-using-amazon-lex-streaming-apis/)

**Check out the Amazon Lex Cheat Sheet:**

[https://tutorialsdojo.com/amazon-lex/](https://tutorialsdojo.com/amazon-lex/)

---

## Câu 12 — ✅ ĐÚNG

### Câu hỏi

A big fast-food chain in Asia is planning to implement a location-based alert on their existing mobile app. If a user is in proximity to one of its restaurants, an alert will be shown on the user’s mobile phone. The notification needs to happen in less than a minute while the user is still in the vicinity. Currently, the mobile app has 10 million users in the Philippines, China, Korea, and other Asian countries.

Which one of the following AWS architecture is the most suitable option for this scenario?

### Các phương án

- **A.** Set up an API that uses an Application Load Balancer and an Auto Scaling group of EC2 instances. The mobile app will send the user's location data to the API web service. Use DynamoDB to store and retrieve relevant offers on the nearest restaurant. Configure the EC2 instances to push alerts to the mobile app.
- **B.** The mobile app will send the real-time location data using Amazon Kinesis. Set up an API which uses an Application Load Balancer and an Auto Scaling group of EC2 instances to retrieve the relevant offers from a DynamoDB table. Use Amazon Lambda and SES to push the notification to the mobile app.
- **C.** Establish connectivity with mobile carriers using AWS Direct Connect. Set up an API on all EC2 instances to receive the location data from the mobile app via the carrier's GPS connection. Use RDS to store the data and fetch relevant offers from the restaurant. The EC2 instances will communicate with mobile carriers to send alerts to the mobile app.
- **D.** The mobile app will send device location to an SQS endpoint. Set up an API that utilizes an Application Load Balancer and an Auto Scaling group of EC2 instances, which will retrieve the relevant offers from DynamoDB. Use Amazon SNS to send offers to the mobile app.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

**Amazon Simple Queue Service (SQS)**  is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications. Additionally, SNS can be used to fan out notifications to end users using mobile push, SMS, and email.

With the **Mobile Push feature of Amazon SNS** , you have the ability to send push notification messages directly to apps on mobile devices. Push notification messages sent to a mobile endpoint can appear in the mobile app as message alerts, badge updates, or even sound alerts.

![image](https://media.tutorialsdojo.com/sap_sns_publisher.png)

You send push notification messages to both mobile devices and desktops using one of the following supported push notification services:

– Amazon Device Messaging (ADM)

– Apple Push Notification Service (APNS) for both iOS and Mac OS X

– Baidu Cloud Push (Baidu)

– Google Cloud Messaging for Android (GCM)

– Microsoft Push Notification Service for Windows Phone (MPNS)

– Windows Push Notification Services (WNS)

Therefore, the correct answer is: **The mobile app will send device location to an SQS endpoint** **. Set up an API that utilizes an Application Load Balancer and an Auto Scaling group of EC2 instances, which will retrieve the relevant offers from DynamoDB. Use Amazon SNS to send offers to the mobile app.**

The option that says: **Set up an API that uses an Application Load Balancer and an Auto Scaling group of EC2 instances. The mobile app will send the user’s location data to the API web service. Use DynamoDB to store and retrieve relevant offers on the nearest restaurant. Configure the EC2 instances to push alerts to the mobile app** is incorrect. Using EC2 instances to push alerts to the mobile app is not an appropriate solution. You have to use the AWS Mobile Push feature of SNS.

The option that says:**Establish connectivity with mobile carriers using AWS Direct Connect. Set up an API on all EC2 instances to receive the location data from the mobile app via the carrier’s GPS connection. Use RDS to store the data and fetch relevant offers from the restaurant. The EC2 instances will communicate with mobile carriers to send alerts to the mobile app** is incorrect. AWS Direct Connect is primarily used to establish a dedicated network connection from your premises to AWS.

The option that says: **The mobile app will send the real-time location data using Amazon Kinesis. Set up an API which uses an Application Load Balancer and an Auto Scaling group of EC2 instances to retrieve the relevant offers from a DynamoDB table. Use Amazon Lambda and SES to push the notification to the mobile app**  is incorrect. You can’t use SES to send push notifications to mobile phones. You have to use SNS instead.

**References:**

[https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html)

[https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send.html](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send.html)

**Check out this Amazon SNS Cheat Sheet:**

[https://tutorialsdojo.com/amazon-sns/](https://tutorialsdojo.com/amazon-sns/)

---

## Câu 13 — ❌ SAI

### Câu hỏi

An Internet-of-Things (IoT) company is building a portal that stores data coming from its 20,000 gas sensors. The gas sensors, which have unique IDs, are used to detect a gas leak or other emissions inside the oil facility. Every 15 minutes, the sensors will send a data point throughout the day containing its ID, current gas level data, as well as the timestamp. Each data point contains critical information coming from the gas sensors. The company would like to query the information coming from a particular gas sensor for the past week and would like to delete all data that are older than eight weeks. The application is using a NoSQL database which is why they are using the Amazon DynamoDB service.

How would you implement this in the most cost-effective way?

### Các phương án

- **A.** Use one table every week, with a composite primary key which is the sensor ID as the partition key and the timestamp as the sort key.
- **B.** Use one table with a primary key which is the concatenated value of the sensor ID and the timestamp.
- **C.** Use one table with a primary key which is the sensor ID. Use the timestamp as the hash key.
- **D.** Use one table every week, with a primary key which is the concatenated value of the sensor ID and the timestamp.

> **Bạn chọn:** C
> **Đáp án đúng:** A

### Giải thích

The gas sensors are generating a large amount of data every week. As mentioned in the question, there are 20,000 gas sensors that send data every 15 minutes. That translates to 1,920,000 records in a single day and with that large amount of data, there would be complexities in querying the DynamoDB database. In these scenarios, you can create new DynamoDB every week and then add a partition key and a sort key in the table.

When you create a table, in addition to the table name, you must specify the primary key of the table. The primary key uniquely identifies each item in the table, so that no two items can have the same key.

**Amazon DynamoDB**  supports two different kinds of primary keys:

**Partition key**  – A simple primary key, composed of one attribute known as the partition key. DynamoDB uses the partition key’s value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored.

**Partition key and sort key**  – Referred to as a composite primary key, this type of key is composed of two attributes. The first attribute is the partition key, and the second attribute is the sort key. DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored.

Take note that the partition key of an item is also known as its hash attribute. The term hash attribute derives from the use of an internal hash function in DynamoDB that evenly distributes data items across partitions, based on their partition key values.

Therefore, the correct answer is: **Use one table every week, with a composite primary key which is the sensor ID as the partition key and the timestamp as the sort key.**

The option that says: **Use one table with a primary key which is the sensor ID. Use the timestamp as the hash key**  is incorrect. If you only use one table, the table would be very enormous and the searching will take a very long time.

The option that says: **Use one table every week, with a primary key which is the concatenated value of the sensor ID and the timestamp**  is incorrect. You need a fixed value for the primary key so you shouldn’t concatenate the timestamp to the sensor ID.

The option that says: **Use one table with a primary key which is the concatenated value of the sensor ID and the timestamp is**  incorrect. If you only use one table, the table would be very enormous and the search will take a very long time.

**References:**

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html)

**Check out this Amazon DynamoDB Cheat Sheet:**

[https://tutorialsdojo.com/amazon-dynamodb/](https://tutorialsdojo.com/amazon-dynamodb/)

---

## Câu 14 — ❌ SAI

### Câu hỏi

A company has adopted cloud-native computing best practices for its infrastructure. The company started using AWS CloudFormation templates for defining its cloud resources, and the templates are hosted in its private GitHub repository. As the developers continuously update the templates, the company has encountered several downtimes caused by misconfigured templates, wrong executions, or the creation of unnecessary environments. The management wants to streamline the process of testing the CloudFormation templates to prevent these errors. The Solutions Architect has been tasked to create an automated solution.

Which of the following options should be implemented to meet the company’s requirements?

### Các phương án

- **A.** Write an AWS Lambda function that syncs the private GitHub repository to another Git provider like GitLab or Bitbucket. Using AWS CodeDeploy, create a change set and execute the AWS CloudFormation template. Add an AWS CodeBuild stage on the deployment to build and run test scripts to verify the new stack.
- **B.** Write an AWS Lambda function that builds any changes committed on the private GitHub repository. Store the generated artifacts on AWS CodeArtifact. Using AWS CodePipeline, create a change set with the new artifact and execute the AWS CloudFormation template. Add a CodeBuild action to run test scripts that verify the new stack.
- **C.** Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set from the CloudFormation template and execute it using AWS CodeDeploy. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack.
- **D.** Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set and execute the CloudFormation template. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack.

> **Bạn chọn:** C
> **Đáp án đúng:** D

### Giải thích

You can apply continuous delivery practices to your **AWS CloudFormation**  stacks using AWS CodePipeline. **AWS CodePipeline**  is a continuous delivery service for fast and reliable application and infrastructure updates. CodePipeline builds, tests, and deploys your code every time there is a code change based on the release process models you define.

With continuous delivery, you can automatically deploy CloudFormation template updates to your pipeline stages for testing and then promote them to production. For example, you could use CodePipeline to model an automated release process that provisions a test stack whenever an updated template is committed to a source repository (Git repositories managed by GitHub, GitLab, and Atlassian Bitbucket) or uploaded to an Amazon S3 bucket. You can inspect the test stack and then approve it for the production stage, after which CodePipeline can delete the test stack and create a change set for final approval. When the change set is approved, CodePipeline can execute the change set and deploy the change to production.

**AWS CodeBuild**  is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. AWS CodeBuild scales continuously and processes multiple builds concurrently, so your builds are not left waiting in a queue.

Here is an example of a Quick Start from AWS for CI/CD Pipeline for AWS CloudFormation templates:

![image](https://media.tutorialsdojo.com/sap_codebuild_workflow.png)

– A pipeline created by CodePipeline, which is triggered when a commit is made to the referenced branch of the GitHub repository used in the source stage.

– A build project in CodeBuild to run TaskCat and launch AWS CloudFormation templates for testing.

– An AWS Lambda function that merges the source branch of the GitHub repository with the release branch.

– AWS Identity and Access Management (IAM) roles for the Lambda function and the build project.

– An Amazon Simple Storage Service (Amazon S3) bucket to stash the build artifacts temporarily and to store the TaskCat report.

Therefore, the correct answer is: **Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set and execute the CloudFormation template. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack.**  With AWS CodePipeline, you can create change sets and automatically deploy CloudFormation template updates safely. You can have a CodeBuild stage for building artifacts and testing your new infra.

The option that says: **Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set from the CloudFormation template and execute it using AWS CodeDeploy. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack**  is incorrect. AWS CodeDeploy is only an unnecessary resource as you will not deploy the changes in your production environment. You need a pipeline to execute the CloudFormation change set and CodeBuild project to test your changes.

The option that says: **Write an AWS Lambda function that syncs the private GitHub repository to another Git provider like GitLab or Bitbucket. Using AWS CodeDeploy, create a change set and execute the AWS CloudFormation template. Add an AWS CodeBuild stage on the deployment to build and run test scripts to verify the new stack**  is incorrect. You don’t need a custom Lambda function as AWS CodePipiline supports executions from third-party Git sources.

The option that says: **Write an AWS Lambda function that builds any changes committed on the private GitHub repository. Store the generated artifacts on AWS CodeArtifact. Using AWS CodePipeline, create a change set with the new artifact and execute the AWS CloudFormation template. Add a CodeBuild action to run test scripts that verify the new stack**  is incorrect. Building artifacts may take longer than the 15-minute maximum execution time of Lambda functions. AWS CodeArtifact is primarily used to automatically fetch software packages and dependencies from public artifact repositories. AWS CodeBuild can be used to build and test artifacts before application deployments.

**References:**

[https://aws.amazon.com/about-aws/whats-new/2016/11/continuously-deliver-changes-to-aws-cloudformation-stacks-with-aws-codepipeline/](https://aws.amazon.com/about-aws/whats-new/2016/11/continuously-deliver-changes-to-aws-cloudformation-stacks-with-aws-codepipeline/)

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.html)

[https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-third-party-git-source-repositories-in-aws-codepipeline.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-third-party-git-source-repositories-in-aws-codepipeline.html)

[https://aws.amazon.com/quickstart/architecture/cicd-taskcat/](https://aws.amazon.com/quickstart/architecture/cicd-taskcat/)

**Check out these AWS CodePipeline and AWS CloudFormation Cheat Sheets:**

[https://tutorialsdojo.com/aws-codepipeline/](https://tutorialsdojo.com/aws-codepipeline/)

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

---

## Câu 15 — ❌ SAI

### Câu hỏi

A media company recently launched a web service that allows users to upload and share short videos. Currently, the web servers are hosted on an Auto Scaling group of Amazon EC2 instances in which the videos are processed and stored in the EBS volumes. Each uploaded video sends a message on the Amazon SQS queue, which is also processed by an Auto Scaling group of Amazon EC2 instances. The company relies on third-party software to analyze and categorize the videos. The website also contains static content that has variable user traffic. The company wants to re-architecture the application to reduce costs, reduce dependency on third-party software, and reduce management overhead by leveraging AWS-managed services.

Which of the following solutions will meet the company’s requirements?

### Các phương án

- **A.** Create an Amazon ECS Fargate cluster and use containers to host the web application. Create an Auto Scaling group of Amazon EC2 Spot instances to process the SQS queue. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets.
- **B.** Create an Amazon S3 bucket with website hosting enabled to host the web application. Store the videos and static content on a separate S3 bucket. Configure S3 event notification to send messages to an Amazon SQS queue for each video upload event. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos.
- **C.** Reduce operational overhead by using AWS Elastic Beanstalk to provision the Auto Scaling group of EC2 instances for the web servers and the Amazon SQS queue consumers. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets.
- **D.** Create an Amazon EFS volume to store the videos and static content. Mount the volume on all EC2 instances of the web application. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos.

> **Bạn chọn:** B
> **Đáp án đúng:** A

### Giải thích

**AWS Fargate**  is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. With AWS Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing. Fargate makes it easy for you to focus on building your applications.

When you run your tasks and services with the Fargate launch type, you package your application in containers, specify the CPU and memory requirements, define networking and IAM policies, and launch the application.

**Amazon Rekognition**  makes it easy to add image and video analysis to your applications. You just provide an image or video to the Amazon Rekognition API, and the service can identify objects, people, text, scenes, and activities. It can detect any inappropriate content as well. Amazon Rekognition also provides highly accurate facial analysis, face comparison, and face search capabilities. You can detect, analyze, and compare faces for a wide variety of use cases, including user verification, cataloging, people counting, and public safety.

Amazon Rekognition is based on the same proven, highly scalable, deep learning technology developed by Amazon’s computer vision scientists to analyze billions of images and videos daily. It requires no machine learning expertise to use. Amazon Rekognition includes a simple, easy-to-use API that can quickly analyze any image or video file that’s stored in Amazon S3.

![image](https://media.tutorialsdojo.com/sap_aws_rekognition_screen.png)

You can use **Amazon S3**  to host a static website. On a static website, individual webpages include static content. They might also contain client-side scripts. By contrast, a dynamic website relies on server-side processing, including server-side scripts such as PHP, JSP, or ASP.NET. Amazon S3 does not support server-side scripting, but AWS has other resources for hosting dynamic websites. This makes Amazon S3 suitable for hosting static website contents.

A **Spot Instance**  is an unused EC2 instance that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts, you can lower your Amazon EC2 costs significantly. The hourly price for a Spot Instance is called a Spot price. The Spot price of each instance type in each Availability Zone is set by Amazon EC2, and is adjusted gradually based on the long-term supply of and demand for Spot Instances. Your Spot Instance runs whenever capacity is available and the maximum price per hour for your request exceeds the Spot price.

Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted. For example, Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks.

Therefore, the correct answer is: **Create an Amazon ECS Fargate cluster and use containers to host the web application. Create an Auto Scaling group of Amazon EC2 Spot instances to process the SQS queue. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets.** Using an ECS Fargate cluster reduces the overhead of managing EC2 instances and using Spot instances to process the SQS queue significantly reduces the operating costs. Amazon Rekognition is designed to analyze videos which you can use to categorize them. Amazon S3 bucket serves as durable and cost-effective storage for the uploaded videos.

The option that says: **Create an Amazon EFS volume to store the videos and static content. Mount the volume on all EC2 instances of the web application. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos**  is incorrect. Amazon S3 is more cost-effective than using EFS. This also increases management overhead as you need to configure the EFS mount point on all your EC2 instances.

The option that says: **Create an Amazon S3 bucket with website hosting enabled to host the web application. Store the videos and static content on a separate S3 bucket. Configure S3 event notification to send messages to an Amazon SQS queue for each video upload event. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos**  is incorrect. The scenario states that the videos are processed and then stored in EBS volumes, suggesting that the service is dynamic in nature. Amazon S3’s static website hosting does not provide server-side processing, which is necessary for dynamic websites. Therefore, hosting a web application on an Amazon S3 bucket with website hosting enabled may not be a suitable option.

The option that says: **Reduce operational overhead by using AWS Elastic Beanstalk to provision the Auto Scaling group of EC2 instances for the web servers and the Amazon SQS queue consumers. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets**  is incorrect. Although Elastic Beanstalk can manage the EC2 instances for you, there is no mention to use Spot instances for processing the SQS queue which can further reduce the operating costs.

**References:**

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

[https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

**Check out these AWS Fargate and Amazon Rekognition Cheat Sheets:**

[https://tutorialsdojo.com/aws-fargate/](https://tutorialsdojo.com/aws-fargate/)

[https://tutorialsdojo.com/amazon-rekognition/](https://tutorialsdojo.com/amazon-rekognition/)

---

## Câu 16 — ✅ ĐÚNG

### Câu hỏi

A company develops cloud-native applications and uses AWS CloudFormation templates for deploying applications in AWS. The application artifacts and templates are stored in an Amazon S3 bucket with versioning enabled. The developers use Amazon EC2 instances that have integrated development (IDE) to download, modify, and re-upload the artifacts on the S3 bucket. The unit testing is done locally on the EC2 instances. The company wants to improve the existing deployment process with a CI/CD pipeline to help the developers be more productive. The following requirements need to be satisfied:

– Utilize GitHub as the code repository for application and CloudFormation templates.

– Have automated testing and security scanning for the generated artifacts.

– Receive a notification when unit testing fails.

– Ability to turn on/off application features and dynamically customize the deployment as part of CI/CD.

– The Lead Developer must approve changes before deploying applications to production.

Which of the following options should the solutions architect implement to meet the company’s requirements?

### Các phương án

- **A.** Use AWS CodeArtifact to store generated artifacts. AWS scans the artifacts for common vulnerabilities and allows custom actions to run the unit tests. Create an Amazon CloudWatch rule that will send Amazon SNS alerts when unit testing fails. Use different Docker images for choosing different application features. Add a manual approval stage on the pipeline for the Lead Developer’s approval prior to production deployment.
- **B.** Create an AWS CodeBuild job to run tests and security scans on the generated artifacts. Create an Amazon EventBridge rule that will send Amazon SNS alerts when unit testing fails. Create AWS Cloud Development Kit (AWS CDK) constructs with a manifest file to turn on/off features of the AWS CDK app. Add a manual approval stage on the pipeline for the Lead Developer’s approval prior to production deployment.
- **C.** Write an AWS Lambda function to run unit tests and security scans on the generated artifacts. Add another Lambda trigger on the next pipeline stage to notify the developers if the unit testing fails. Create AWS Amplify plugins to allow turning on/off of application features. Add an AWS SES action on the pipeline to send an approval message to the Lead Developer prior to production deployment.
- **D.** Create a Jenkins job to run tests and security scans on the generated artifacts. Create an Amazon EventBridge rule that will send Amazon SES alerts when unit testing fails. Use AWS CloudFormation with nested stacks to allow turning on/off of application features. Add an AWS Lambda function to the pipeline to allow approval from the Lead Developer prior to production deployment.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

**AWS CodeBuild**  is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers. It provides prepackaged build environments for popular programming languages and builds tools such as Apache Maven, Gradle, and more. You can also customize build environments in CodeBuild to use your own build tools. CodeBuild scales automatically to meet peak build requests. CodeBuild provides these benefits:

**Fully managed**  – CodeBuild eliminates the need to set up, patch, update, and manage your own build servers.

**On-demand**  – CodeBuild scales on demand to meet your build needs. You pay only for the number of build minutes you consume.

**Out of the box**  – CodeBuild provides preconfigured build environments for the most popular programming languages. All you need to do is point to your build script to start your first build.

![image](https://media.tutorialsdojo.com/sap_codepipeline_stages.png)

The **AWS Cloud Development Kit (AWS CDK)**  lets you easily define applications in the AWS Cloud using your programming language of choice. But creating an application is just the start of the journey. You also want to make changes to it and deploy them. You can do this through the Code suite of tools: GitHub, AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline. Together, they allow you to build what’s called a deployment pipeline for your application.

In **AWS CodePipeline** , you can add an approval action to a stage in a pipeline at the point where you want the pipeline execution to stop so that someone with the required AWS Identity and Access Management permissions can approve or reject the action.

If the action is approved, the pipeline execution resumes. If the action is rejected—or if no one approves or rejects the action within seven days of the pipeline reaching the action and stopping—the result is the same as an action failing, and the pipeline execution does not continue.

You might use manual approvals for these reasons:

– You want someone to perform a code review or change management review before a revision is allowed into the next stage of a pipeline.

– You want someone to perform manual quality assurance testing on the latest version of an application or to confirm the integrity of a build artifact before it is released.

– You want someone to review new or updated text that is published on a company website.

Therefore, the correct answer is: **Create an AWS CodeBuild job to run tests and security scans on the generated artifacts. Create an Amazon EventBridge rule that will send Amazon SNS alerts when unit testing fails. Create AWS Cloud Development Kit (AWS CDK) constructs with a manifest file to turn on/off features of the AWS CDK app. Add a manual approval stage on the pipeline for the Lead Developer’s approval prior to production deployment.** AWS CodeBuild allows automated build and testing of application artifacts. AWS CDK allows you to control application features using a manifest file, and adding an approval on AWS CodePipeline will allow the Lead Developer to approve deployments.

The option that says: **Write an AWS Lambda function to run unit tests and security scans on the generated artifacts. Add another Lambda trigger on the next pipeline stage to notify the developers if the unit testing fails. Create AWS Amplify plugins to allow turning on/off of application features. Add an AWS SES action on the pipeline to send an approval message to the Lead Developer prior to production deployment** is incorrect. Unit testing and security scanning may typically take longer than 15 minutes, so AWS Lambda is not recommended here. It would be easier and much simpler to just add an approval stage on the pipeline instead of using AWS SES to send an approval message to the Lead Developer.

The option that says: **Create a Jenkins job to run tests and security scans on the generated artifacts. Create an Amazon EventBridge rule that will send Amazon SES alerts when unit testing fails. Use AWS CloudFormation with nested stacks to allow turning on/off of application features. Add an AWS Lambda function to the pipeline to allow approval from the Lead Developer prior to production deployment**  is incorrect. Instead of creating a Jenkins job, you can use AWS CodeBuild to test your artifacts. CodeBuild is tightly integrated on AWS, so it is very easy to add it to your deployment pipeline.

The option that says:**Use AWS CodeArtifact to store generated artifacts. AWS scans the artifacts for common vulnerabilities and allows custom actions to run the unit tests. Create an Amazon CloudWatch rule that will send Amazon SNS alerts when unit testing fails. Use different Docker images for choosing different application features. Add a manual approval stage on the pipeline for the Lead Developer’s approval prior to production deployment** is incorrect. AWS CodeArtifact is a fully managed artifact repository service that primarily allows organizations to securely store, publish, and share software packages used in their software development process. It works with common package managers and builds tools like Maven, Gradle, npm, yarn, twine, and pip. It does not allow the user to configure custom actions or scripts to perform unit tests on artifacts. It is recommended to use AWS CodeBuild for this scenario.

**References:**

[https://docs.aws.amazon.com/cdk/latest/guide/codepipeline_example.html](https://docs.aws.amazon.com/cdk/latest/guide/codepipeline_example.html)

[https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)

[https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html)

**Check out these AWS CodeBuild and AWS CodePipeline Cheat Sheet:**

[https://tutorialsdojo.com/aws-codebuild/](https://tutorialsdojo.com/aws-codebuild/)

---

## Câu 17 — ❌ SAI

### Câu hỏi

A company hosts a serverless application on AWS using Amazon API Gateway and AWS Lambda with Amazon DynamoDB as the backend database. The application has a feature that allows users to create posts and reply to comments based on different topics. The API model currently uses the following methods:

– `GET /posts/[postid]` – used to get details about the post

– `GET /users/[userid]` – used to get details about a user

– `GET /comments/[commentid]` – used to get details of a comment

The application does not use API keys for request authorization. To increase user engagement on the web app, the company wants to reduce comment latency by making the comments appear in real-time.

Which of the following solution should be implemented to meet the requirements and improve user experience?

### Các phương án

- **A.** Update the application code to call the `GET /comments/[commentid]` API every 3 seconds to show comments in real-time without sacrificing performance.
- **B.** Lower the API response time of the Lambda functions by increasing the concurrency limit. This allows functions to run in parallel to deliver the comments in real-time.
- **C.** Create a distribution on Amazon CloudFront and use edge-optimized APIs. Cache API responses in CloudFront to improve comment latency.
- **D.** Leverage AWS AppSync by building GraphQL APIs and using Websockets to deliver comments in real-time.

> **Bạn chọn:** C
> **Đáp án đúng:** D

### Giải thích

**AWS AppSync**  is a fully managed service that makes it easy to develop GraphQL APIs by handling the heavy lifting of securely connecting to data sources like Amazon DynamoDB, Lambda, and more. Adding caches to improve performance, subscriptions to support real-time updates, and client-side data stores that keep offline clients in sync are just as easy. Once deployed, AWS AppSync automatically scales your GraphQL API execution engine up and down to meet API request volumes.

With managed GraphQL subscriptions, AWS AppSync can push real-time data updates over Websockets to millions of clients. For mobile and web applications, AppSync also provides local data access when devices go offline, and data synchronization with customizable conflict resolution, when they are back online.

AppSync supports real-time chat applications. You can build conversational mobile or web applications that support multiple private chat rooms, offer access to conversation history, and queue outbound messages, even when a device is offline.

![image](https://media.tutorialsdojo.com/sap_aws_appsync_overview.png)

AppSync can also be used for real-time collaboration. You can broadcast data from the backend to all connected clients (one-to-many) or between clients (many-to-many), such as in a second screen scenario where you broadcast the same data to all clients, who can then reply.

Therefore, the correct answer is: **Leverage AWS AppSync by building GraphQL APIs and using Websockets to deliver comments in real-time.**  AWS AppSync can push real-time data updates over Websockets. This can automatically scale to millions of client requests.

The option that says: **Create a distribution on Amazon CloudFront and use edge-optimized APIs. Cache API responses in CloudFront to improve comment latency**  is incorrect. Caching API responses can improve the loading of comments, however, this may not show the comments in real-time if the new comments are not yet on the cache.

The option that says: **Update the application code to call the `GET /comments/[commentid]` API every 3 seconds to show comments in real-time without sacrificing performance**  is incorrect. This is possible but will heavily put a burden on your Lambda function executions. Even if there are no new comments, the API will still be called. This will add unnecessary cost to function executions.

The option that says: **Lower the API response time of the Lambda functions by increasing the concurrency limit. This allows functions to run in parallel to deliver the comments in real-time**  is incorrect. Increasing the concurrency limit will not help in showing the comments in real-time. If you don’t reach the Lambda concurrency limit regularly, there is no apparent advantage for this option.

**References:**

[https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html)

[https://docs.aws.amazon.com/appsync/latest/devguide/real-time-websocket-client.html](https://docs.aws.amazon.com/appsync/latest/devguide/real-time-websocket-client.html)

[https://aws.amazon.com/about-aws/whats-new/2020/04/aws-appsync-enables-support-for-generic-websockets-clients-graphql-real-time-subscriptions/](https://aws.amazon.com/about-aws/whats-new/2020/04/aws-appsync-enables-support-for-generic-websockets-clients-graphql-real-time-subscriptions/)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 18 — ✅ ĐÚNG

### Câu hỏi

A cryptocurrency exchange company has recently signed up for a 3rd party online auditing system, which is also using AWS, to perform regulatory compliance audits on their cloud systems. The online auditing system needs to access certain AWS resources in your network to perform the audit.

In this scenario, which of the following approach is the most secure way of providing access to the 3rd party online auditing system?

### Các phương án

- **A.** Create a new IAM user and assign a user policy to the IAM user that allows only the actions required by the online audit system. Create a new access and secret key for the IAM user and provide these credentials to the 3rd party auditing company.
- **B.** Create a new IAM role for cross-account access which allows the online auditing system account to assume the role. Assign a policy that allows full and unrestricted access to all AWS resources.
- **C.** Create a new IAM user and assign a user policy to the IAM user that allows full and unrestricted access to all AWS resources. Create a new access and secret key for the IAM user and provide these credentials to the 3rd party auditing company.
- **D.** Create a new IAM role for cross-account access which allows the online auditing system account to assume the role. Assign it a policy that allows only the actions required for the compliance audit.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

An IAM *role*  is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.

You can use roles to delegate access to users, applications, or services that don’t normally have access to your AWS resources. For example, you might want to grant users in your AWS account access to resources they don’t usually have, or grant users in one AWS account access to resources in another account. Or you might want to allow a mobile app to use AWS resources, but not want to embed AWS keys within the app (where they can be difficult to rotate and where users can potentially extract them). Sometimes you want to give AWS access to users who already have identities defined outside of AWS, such as in your corporate directory. Or, you might want to grant access to your account to third parties so that they can perform an audit on your resources.

![image](https://media.tutorialsdojo.com/sap_iam_assume_role_cross_account.png)

To allow users from one AWS account to access resources in another AWS account, create a role that defines who can access it and what permissions it grants to users that switch to it. Use IAM roles to delegate access within or between AWS accounts. By setting up cross-account access, you don’t need to create individual IAM users in each account in order to provide access to different AWS accounts.

The option that says: **Create a new IAM role for cross-account access which allows the online auditing system account to assume the role. Assign it a policy that allows only the actions required for the compliance audit** is correct because it uses an IAM role and only provides the needed access, which adheres to the principle of least privilege.

The option that says:**Create a new IAM role for cross-account access which allows the online auditing system account to assume the role. Assign a policy that allows full and unrestricted access to all AWS resources**  is incorrect. Although you are right to use an IAM role, you should provide only the access needed by the 3rd party audit system and not a full, unrestricted access to all AWS resources.

The option that says: **Create a new IAM user and assign a user policy to the IAM user that allows only the actions required by the online audit system. Create a new access and secret key for the IAM user and provide these credentials to the 3rd party auditing company**  is incorrect as you need to use an IAM role instead of an IAM user.

The option that says: **Create a new IAM user and assign a user policy to the IAM user that allows full and unrestricted access to all AWS resources. Create a new access and secret key for the IAM user and provide these credentials to the 3rd party auditing company**  is incorrect as you need to use an IAM role instead of an IAM user. In addition, you should provide only the access needed by the 3rd party audit system and not a full, unrestricted access to all AWS resources.

**References:**

[https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

**Check out this AWS IAM Cheat Sheet:**

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 19 — ❌ SAI

### Câu hỏi

A research company hosts its internal applications inside AWS VPCs in multiple AWS Accounts. The internal applications are accessed securely from inside the company network using an AWS Site-to-Site VPN connection. VPC peering connections has been established from the company’s main AWS account to VPCs in other AWS Accounts. The company has recently announced that employees will be allowed to work remotely if they are connected using a VPN. The solutions architect has been tasked to create a scalable and reliable AWS Client VPN solution that employees can use when working remotely.

Which of the following options is the most cost-effective implementation to meet the company requirements with minimal changes to the current setup?

### Các phương án

- **A.** Install the AWS Client VPN on the company data center. Create AWS Transit Gateway to connect the main VPC and other VPCs into a single hub. Update the VPC route configurations to allow communication with the internal applications.
- **B.** Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in each of the AWS accounts. Update each VPC route configuration to allow communication with the internal applications.
- **C.** Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in the same VPC region in the main AWS account. Update the VPC route configurations to allow communication with the internal applications.
- **D.** Install the AWS Client VPN on the company data center. Configure connectivity between the existing AWS Site-to-Site VPN and client VPN endpoint.

> **Bạn chọn:** A
> **Đáp án đúng:** C

### Giải thích

**AWS Client VPN**  is a managed client-based VPN service that enables you to securely access your AWS resources and resources in your on-premises network. With Client VPN, you can access your resources from any location using an OpenVPN-based VPN client.

The **administrator**  is responsible for setting up and configuring the service. This involves creating the Client VPN endpoint, associating the target network, configuring the authorization rules, and setting up additional routes (if required).

The **client**  is the end user. This is the person who connects to the Client VPN endpoint to establish a VPN session. The client establishes the VPN session from their local computer or mobile device using an OpenVPN-based VPN client application.

The following are the key components for using AWS Client VPN.

**-Client VPN endpoint**  — Your Client VPN administrator creates and configures a Client VPN endpoint in AWS. Your administrator controls which networks and resources you can access when establishing a VPN connection.

**-VPN client application**  — The software application that you use to connect to the Client VPN endpoint and establish a secure VPN connection.

**-Client VPN endpoint configuration file**  — A configuration file that’s provided to you by your Client VPN administrator. The file includes information about the Client VPN endpoint and the certificates required to establish a VPN connection. You load this file into your chosen VPN client application.

The configuration for this scenario includes a target VPC (VPC A) that is peered with an additional VPC (VPC B). We recommend this configuration if you need to give clients access to the resources inside a target VPC and other VPCs that are peered with it (such as VPC B).

![image](https://media.tutorialsdojo.com/sap_aws_client_vpn.png)

Therefore, the correct answer is: **Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in the same VPC region in the main AWS account. Update the VPC route configurations to allow communication with the internal applications.**  This solution is cost-effective and requires minimal changes to the current network setup.

The option that says: **Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in each of the AWS accounts. Update each VPC route configuration to allow communication with the internal applications**  is incorrect. You only need to create a Client VPN endpoint on the main VPC account that has Site-to-Site VPN.

The option that says: **Install the AWS Client VPN on the company data center. Create AWS Transit Gateway to connect the main VPC and other VPCs into a single hub. Update the VPC route configurations to allow communication with the internal applications**  is incorrect. This may be possible, however, this will require reconfiguring the existing VPC peering between the main VPC and the other VPCs in other AWS accounts. Additionally, the AWS Client VPN should be installed on the employee workstations.

The option that says: **Install the AWS Client VPN on the company data center. Configure connectivity between the existing AWS Site-to-Site VPN and client VPN endpoint**  is incorrect. This configuration is impossible and the AWS Client VPN should be installed on the employee workstations and not in the company data center.

**References:**

[https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/scenario-peered.html](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/scenario-peered.html)

[https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

[https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations)

**Check out these Amazon VPC and VPC Peeing Cheat Sheets:**

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

[https://tutorialsdojo.com/vpc-peering/](https://tutorialsdojo.com/vpc-peering/)

---

## Câu 20 — ✅ ĐÚNG

### Câu hỏi

A computer hardware manufacturer has a supply chain application that is written in NodeJS. The application is deployed on an Amazon EC2 Reserved instance which has been provisioned with an IAM Role that provides access to data files stored in an S3 bucket.

In this architecture, which of the following IAM policies control access to the data files in S3? (Select TWO.)

### Các phương án

- **A.** An IAM trust policy that allows the NodeJS supply chain application running on the EC2 instance to access the data files stored in the S3 bucket.
- **B.** An IAM trust policy that allows the Amazon S3 service to assume an EC2 instance role.
- **C.** A bucket policy that allows the EC2 role to list objects in the S3 bucket.
- **D.** An IAM permissions policy that allows the EC2 role to access S3 objects.
- **E.** An IAM trust policy that allows the Amazon EC2 service to assume an EC2 instance role.

> **Bạn chọn:** D, E
> **Đáp án đúng:** D, E

### Giải thích

An **IAM role**  is an IAM identity that you can create in your account that has specific permissions. An IAM role has some similarities to an IAM user. Roles and users are both AWS identities with permissions policies that determine what the identity can and cannot do in AWS.

**Applications that run on an Amazon EC2 instance**  must include AWS credentials in the AWS API requests. You can and should use an**IAM role**  to manage temporary credentials for applications that run on an Amazon EC2 instance. When you use a role, you don’t have to distribute long-term credentials (such as sign-in credentials or access keys) to an Amazon EC2 instance. Instead, the role supplies temporary permissions that applications can use when they make calls to other AWS resources. When you launch an Amazon EC2 instance, you specify an IAM role to associate with the instance. Applications that run on the instance can then use the role-supplied temporary credentials to sign API requests.

![image](https://media.tutorialsdojo.com/sap_ec2_iam_role_s3_bucket.png)

**IAM trust policies**  for IAM roles specify which entities, like users, roles, or services, can assume a role and request temporary credentials, whether across multiple accounts or within a single one. They’re crucial for authorizing access to resources. Even within a single account, trust policies are necessary to define eligible principals, such as users, federated users, or AWS services. For instance, in an EC2 instance scenario, the trust policy ensures only EC2 instances can assume the role, enhancing security and access control.

**IAM permissions policies** , on the other hand, define the specific actions and resources that are allowed or denied for IAM entities (such as roles or users). These policies control what actions can be performed on which AWS resources. For instance, an IAM permissions policy attached to an EC2 role might grant permissions to read from or write to specific S3 buckets.

Hence, the correct answers are:

**– An IAM trust policy that allows the Amazon EC2 service to assume an EC2 instance role.**

**– An IAM permissions policy that allows the EC2 role to access S3 objects.**

The option that says: **An IAM trust policy that allows the NodeJS supply chain application running on the EC2 instance to access the data files stored in the S3 bucket**  is incorrect. IAM trust policies define which principals can assume a role; they do not directly grant permissions to access resources like S3 buckets. Thus, a trust policy wouldn’t be used to allow application access to S3 data.

The option that says: **A bucket policy that allows the EC2 role to list objects in the S3 bucket**  is incorrect because the question states the EC2 role needs access (i.e. download/read) the data files in S3. Therefore, a policy that only grants the role the ability to list objects does not fully meet the requirements stated in the question.

The option that says: **An IAM trust policy that allows the Amazon S3 service to assume an EC2 instance role**  is incorrect. To enable an EC2 instance assume a role, Amazon EC2 must be specified as the principal. S3, as a service, does not assume roles to perform operations on behalf of EC2 instances.

**References:**

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#term_trust-policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#term_trust-policy)

**Check out this AWS IAM Cheat Sheet:**

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 21 — ❌ SAI

### Câu hỏi

A startup is developing a health-related mobile app for iOS and Android. The co-founder developed a sleep-tracking app that collects the user’s biometric data and stores it in an Amazon DynamoDB table configured with on-demand provisioned throughput. Every day at nine in the morning, a scheduled task scans the DynamoDB table to extract and aggregate last night’s data for each user and stores the results in an Amazon S3 bucket. When the new data is available, the users are then notified via Amazon SNS mobile push notifications. Due to budget constraints, management wants to optimize the backend system’s architecture to reduce costs and increase overall revenue.

Which of the following options can the solutions architect implement to further lower the cost in AWS? (Select TWO.)

### Các phương án

- **A.** Use Amazon ElastiCache to cache reads and writes from the DynamoDB table.
- **B.** Launch an Amazon Redshift cluster to replace DynamoDB. Switch from a Standard S3 bucket to One Zone-Infrequent Access storage class.
- **C.** Avail a reserved capacity for provisioned throughput for DynamoDB.
- **D.** Use an Amazon RDS instance configured with Multi-AZ deployments and Read Replicas as a replacement to your DynamoDB.
- **E.** Set up a scheduled job to drop the DynamoDB table for the previous day that contains the biometric data after it is successfully stored in the S3 bucket. Create another DynamoDB table for the day and perform the deletion and creation process everyday.

> **Bạn chọn:** A, C
> **Đáp án đúng:** C, E

### Giải thích

You can purchase reserved capacity in advance to lower the costs of running your DynamoDB instance. With reserved capacity, you pay a one-time upfront fee and commit to a minimum usage level over a period of time. By reserving your read and write capacity units ahead of time, you realize significant cost savings compared to on-demand provisioned throughput settings. In addition, you can also drop the DynamoDB table, which contains the biometric data right after it is successfully stored in S3.

![image](https://media.tutorialsdojo.com/sap_dynamoDB_auto_scaling.png)

Hence, the correct answers are:

**– Avail a reserved capacity for provisioned throughput for DynamoDB** . If you can predict your need for Amazon DynamoDB read-and-write throughput, reserved capacity offers significant savings over the normal price of DynamoDB provisioned throughput capacity.

**– Set up a scheduled job to drop the DynamoDB table for the previous day that contains the biometric data after it is successfully stored in the S3 bucket. Create another DynamoDB table for the day and perform the deletion and creation process everyday** . This saves costs by not storing too much data on DynamoDB tables.

The option that says: **Use an Amazon RDS instance configured with Multi-AZ deployments and Read Replicas as a replacement to your DynamoDB**  is incorrect because using an RDS database with Multi-AZ deployments and Read Replicas will actually cost more than the current architecture. The scenario just wants to lower the cost, and it didn’t specify the need to shift to a NoSQL database.

The option that says: **Launch an Amazon Redshift cluster to replace DynamoDB. Switch from a Standard S3 bucket to One Zone-Infrequent Access storage class**  is incorrect because Redshift is primarily used for online analytical processing (OLAP) applications and not as a NoSQL database. This change also entails a significant amount of time and resources to execute.

The option that says: **Use Amazon ElastiCache to cache reads and writes from the DynamoDB table**  is incorrect. Although an ElastiCache cluster can lower the CPU utilization of your EC2 instances and improve application performance, it doesn’t provide significant cost reduction as compared to Options 3 and 5. Take note that this will also increase the cost since you have to pay for your ElastiCache cluster.

**References:**

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ProvisionedThroughput.html#HowItWorks.ProvisionedThroughput.ReservedCapacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ProvisionedThroughput.html#HowItWorks.ProvisionedThroughput.ReservedCapacity)

[https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/amazon-dynamodb-reservations.html](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/amazon-dynamodb-reservations.html)

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)

**Check out this Amazon DynamoDB Cheat Sheet:**

[https://tutorialsdojo.com/amazon-dynamodb/](https://tutorialsdojo.com/amazon-dynamodb/)

---

## Câu 22 — ✅ ĐÚNG

### Câu hỏi

A global data analytics firm has various data centers from different countries all over the world. The staff are regularly uploading analytics, financial, and regulatory files of each of their respective data centers to a web portal deployed in AWS, which uses an S3 bucket named `global-analytics-reports-bucket` to durably store the data. The staff download various reports from a CloudFront distribution which uses the `global-analytics-reports-bucket` S3 bucket as the origin. The security team noticed that the staff are using both the CloudFront link and the direct Amazon S3 URLs to download the reports. The security team sees this as a security risk and they recommended implementing a way to prevent anyone from bypassing CloudFront and using the direct Amazon S3 URLs.

Which of the following options should the solutions architect implement to meet the above requirement?

### Các phương án

- **A.** In your CloudFront distribution, use a custom SSL instead of the default SSL. 2. Remove anyone else’s permission to use Amazon S3 URLs to read the objects.
- **B.** Configure the distribution to use Signed URLs. 2. Create a special CloudFront user called an origin access control (OAC). 3. Give the origin access control permission to read the objects in your bucket.
- **C.** Create a special CloudFront user called an origin access control (OAC) and associate it with your CloudFront distribution. 2. Give the origin access control permission to read the objects in your bucket. 3. Remove anyone else’s permission to use Amazon S3 URLs to read the objects.
- **D.** Set up a field-level encryption configuration in the CloudFront distribution. 2. Remove anyone else’s permission to use Amazon S3 URLs to read the objects.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

You can optionally secure the content in your Amazon S3 bucket so that users can access it through CloudFront but cannot access it directly by using Amazon S3 URLs. This prevents someone from bypassing CloudFront and using the Amazon S3 URL to get content that you want to restrict access to. This step isn’t required to use signed URLs, but is recommended by AWS. Be aware that this option is only available if you have not set up your Amazon S3 bucket as a website endpoint.

To require that users access your content through CloudFront URLs, you do the following tasks:

– Create a special CloudFront user called an origin access control and associate it with your CloudFront distribution.

– Give the origin access control permission to read the files in your bucket.

– Remove permission for anyone else to use Amazon S3 URLs to read the files.

![image](https://media.tutorialsdojo.com/sap_cloudfront_oia.png)

**Origin Access Control (OAC)**  is a new feature that enables CloudFront customers to easily secure their S3 origins by permitting only designated CloudFront distributions to access their S3 buckets. Customers can now enable AWS Signature Version 4 (SigV4) on CloudFront requests to S3 buckets with the ability to set when and if CloudFront should sign requests. Additionally, customers can now use SSE-KMS when performing uploads and downloads through CloudFront.

In this scenario, the main objective is to prevent the staff from using the direct Amazon S3 URLs to download the reports. The best solution that you can choose here is to use an Origin Access Control (OAC) and remove anyone else’s permission to use the S3 URLs to read the objects. Hence, the correct answer is the following option:

**1. Create a special CloudFront user called an origin access control (OAC).**

**2. Give the origin access control permission to read the objects in your bucket.**

**3. Remove anyone else’s permission to use Amazon S3 URLs to read the objects.**

The following option is incorrect because SSL is not needed in this particular scenario:

**1. In your CloudFront distribution, use a custom SSL instead of the default SSL.**

**2. Remove anyone else’s permission to use Amazon S3 URLs to read the objects.**

What you need to implement is an OAC.

The following option is incorrect because the field-level encryption configuration is mainly used for safeguarding sensitive fields in your CloudFront, and not suitable for this scenario:

**1. Set up a field-level encryption configuration in the CloudFront distribution.**

**2. Remove anyone else’s permission to use Amazon S3 URLs to read the objects.**

The following option is incorrect because although it is recommended to use Signed URLs and OAC in CloudFront, this option is still missing the crucial step of removing anyone else’s permission to use the S3 URLs to read the objects:

**1. Configure the distribution to use Signed URLs.**

**2. Create a special CloudFront user called an origin access control (OAC).**

**3. Give the origin access control permission to read the objects in your bucket.**

**References:**

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#private-content-overview-s3](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#private-content-overview-s3)

[https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-cloudfront-origin-access-control/](https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-cloudfront-origin-access-control/)

**Check out this Amazon CloudFront Cheat Sheet:**

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

---

## Câu 23 — ✅ ĐÚNG

### Câu hỏi

A company manually runs its custom scripts when deploying a new version of its application that is hosted on a fleet of Amazon EC2 instances. This method is prone to human errors, such as accidentally running the wrong script or deploying the wrong artifact. The company wants to automate its deployment procedure.

If errors are encountered after the deployment, the company wants to be able to roll back to the older application version as fast as possible.

Which of the following options should the Solutions Architect implement to meet the requirements?

### Các phương án

- **A.** Create a new pipeline on AWS CodePipeline and add a stage that will deploy the application on the EC2 instances. Choose a “rolling update with an additional batch” deployment strategy, to allow a quick rollback to the older version in case of errors.
- **B.** Create two identical environments of the application on AWS Elastic Beanstalk. Use a blue/green deployment strategy by swapping the environment’s URL. Deploy the custom scripts using Elastic Beanstalk platform hooks.
- **C.** Create an AWS System Manager automation runbook to manage the deployment process. Set up the runbook to first deploy the new application version to a staging environment. Include automated tests and, upon successful completion, use the runbook to deploy the application to the production environment
- **D.** Utilize AWS CodeBuild and add a job with Chef recipes for the new application version. Use a “canary” deployment strategy to the new version on a new instance. Delete the canary instance if errors are found on the new version.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Blue/Green Deployment involves maintaining two separate, identical environments. The “Blue” environment is the current production version, while the “Green” is for the new version. . This Green environment is an exact replica of the Blue one but hosts the new version of your application. After deploying and thoroughly testing the new version in the Green environment, you simply switch the environment’s URL to redirect traffic from the Blue to the Green environment. This switch makes the new version live for users. If a rollback is needed due to any issues, it’s just a matter of switching the URL back to the original Blue environment and instantly reverting to the previous version of the application.

![image](https://media.tutorialsdojo.com/public/elasticbeanstalk-diagram013124-aws-blue-green.png)

In Elastic Beanstalk you can perform a blue/green deployment by swapping the CNAMEs of the two environments to redirect traffic to the new version instantly. If there are any custom scripts or executable files that you want to run automatically as part of your deployment process, you may use platform hooks.

To provide platform hooks that run during an application deployment, place the files under the `.platform/hooks` directory in your source bundle, in one of the following subdirectories:

`prebuild` – Files here run after the Elastic Beanstalk platform engine downloads and extracts the application source bundle, and before it sets up and configures the application and web server.

`predeploy` – Files here run after the Elastic Beanstalk platform engine sets up and configures the application and web server, and before it deploys them to their final runtime location.

`postdeploy` – Files here run after the Elastic Beanstalk platform engine deploys the application and proxy server.

Therefore, the correct answer is: **Create two identical environments of the application on AWS Elastic Beanstalk. Use a blue/green deployment strategy by swapping the environment’s URL. Deploy the custom scripts using Elastic Beanstalk platform hooks.**

The option that says: **Create an AWS System Manager automation runbook to manage the deployment process. Set up the runbook to first deploy the new application version to a staging environment. Include automated tests and, upon successful completion, use the runbook to deploy the application to the production environment** is incorrect. While this is technically possible, it does not offer the fastest rollback mechanism in case of immediate issues post-deployment, as the rollback would involve a separate process. Moreover, unlike AWS Elastic Beanstalk, which has built-in features for version tracking, using AWS System Manager for deployment requires a more manual approach to version control. You would need to maintain a system for tracking different application versions, ensuring that you have the correct version deployed in the right environment (staging vs. production). This adds complexity to the deployment process.

The option that says: **Create a new pipeline on AWS CodePipeline and add a stage that will deploy the application on the EC2 instances. Choose a “rolling update with an additional batch” deployment strategy, to allow a quick rollback to the older version in case of errors**  is incorrect. Although the pipeline can primarily deploy the new version on the EC2 instances, rollback for this strategy takes time. You will have to re-deploy the older version if you want to do a rollback.

The option that says: **Utilize AWS CodeBuild and add a job with Chef recipes for the new application version. Use a “canary” deployment strategy to the new version on a new instance. Delete the canary instance if errors are found on the new version** is incorrect. Although you can detect errors on a canary deployment, AWS CodeBuild cannot deploy the new application version on the EC2 instances. You typically have to use AWS CodeDeploy if you want to go this route.

**References:**

[https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html#using-features.platform.upgrade.bluegreen](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html#using-features.platform.upgrade.bluegreen)

[https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.html)

[https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html)

**Check out this AWS Elastic Beanstalk Cheat Sheet:**

[https://tutorialsdojo.com/aws-elastic-beanstalk/](https://tutorialsdojo.com/aws-elastic-beanstalk/)

---

## Câu 24 — ✅ ĐÚNG

### Câu hỏi

A company manages more than 50 AWS accounts under its AWS Organization. All AWS accounts deploy resources on a single AWS region only. To enable routing across all accounts, each VPC has a Transit Gateway Attachment to a centralized AWS Transit Gateway. Each VPC also has an internet gateway and NAT gateway to provide outbound internet connectivity for its resources. As a security requirement, the company must have a centrally managed rule-based filtering solution for outbound internet traffic on all AWS accounts under its organization. It is expected that peak outbound traffic for each Availability Zone will not exceed 25 Gbps.

Which of the following options should the solutions architect implement to fulfill the company requirements?

### Các phương án

- **A.** Provision an Auto Scaling group of Amazon EC2 instances with network-optimized instance type on each AWS account. Install an open-source internet proxy software for rule-based filtering. Configure the route tables on each VPC to point to the Auto Scaling group.
- **B.** Create a dedicated VPC for outbound internet traffic with a NAT gateway on it. Connect this VPC to the existing AWS Transit Gateway. Configure an AWS Network Firewall firewall for the rule-based filtering. Modify all the default routes in each account to point to the Network Firewall endpoint.
- **C.** Use AWS Network Firewall service to create firewall rule groups and firewall policies for rule-based filtering. Attach the firewall policy to a new Network Firewall firewall on each account. Modify all the default routes in each account to point to their corresponding Network Firewall firewall.
- **D.** Create a dedicated VPC for outbound internet traffic with a NAT gateway on it. Connect this VPC to the existing AWS Transit Gateway. On this VPC, create an Auto Scaling group of Amazon EC2 instances running with an open-source internet proxy software for rule-based filtering across all AZ in the region. Configure the route tables on each VPC to point to this Auto Scaling group.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

**AWS Network Firewall**  is a stateful, managed, network firewall and intrusion detection and prevention service for your virtual private cloud (VPC) that you created in Amazon Virtual Private Cloud (Amazon VPC). With Network Firewall, you can filter traffic at the perimeter of your VPC. This includes filtering traffic going to and coming from an internet gateway, NAT gateway, or over VPN or AWS Direct Connect.

Once AWS Network Firewall is deployed, you will see a firewall endpoint in each firewall subnet. Firewall endpoint is similar to interface endpoint and it shows up as vpce-id in your VPC route table target selection. You have multiple deployment models for Network Firewall.

For a centralized egress deployment model, an AWS Transit Gateway is a prerequisite. AWS Transit Gateway acts as a network hub and simplifies the connectivity between VPCs. For this model, we have a dedicated, central egress VPC which has a NAT gateway configured in a public subnet with access to IGW.

![image](https://media.tutorialsdojo.com/sap_network_firewall_central_egress.png)

Traffic originating from spoke VPCs is forwarded to inspection VPC for processing. It is then forwarded to central egress VPC using a default route in the Transit Gateway firewall route table. The default route is set to target central egress VPC Attachment (pointing to the AWS Network Firewall endpoint).

Therefore, the correct answer is: **Create a dedicated VPC for outbound internet traffic with a NAT gateway on it. Connect this VPC to the existing AWS Transit Gateway. Configure an AWS Network Firewall firewall for the rule-based filtering. Modify all the default routes in each account to point to the Network Firewall endpoint.** This solution provides a dedicated VPC for rule-based inspection and controlling of egress traffic. Please check the references section for more details.

The option that says: **Use AWS Network Firewall service to create firewall rule groups and firewall policies for rule-based filtering. Attach the firewall policy to a new Network Firewall firewall on each account. Modify all the default routes in each account to point to their corresponding Network Firewall firewall**  is incorrect. For centralized rule-based filtering with a Network Firewall, you will need an AWS Transit Gateway to act as a network hub and allow the connectivity between VPCs.

The option that says: **Provision an Auto Scaling group of Amazon EC2 instances with network-optimized instance type on each AWS account. Install an open-source internet proxy software for rule-based filtering. Configure the route tables on each VPC to point to the Auto Scaling group**  is incorrect. This will be difficult to manage since you will have a proxy cluster essentially on each AWS account.

The option that says: **Create a dedicated VPC for outbound internet traffic with a NAT gateway on it. Connect this VPC to the existing AWS Transit Gateway. On this VPC, create an Auto Scaling group of Amazon EC2 instances running with an open-source internet proxy software for rule-based filtering across all AZ in the region. Configure the route tables on each VPC to point to this Auto Scaling group**  is incorrect. This may be possible but is not recommended. AWS Network Firewall can offer centralized rule-based traffic filtering and inspection across your VPCs.

**References:**

[https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/)

[https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)

[https://docs.aws.amazon.com/network-firewall/latest/developerguide/how-it-works.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/how-it-works.html)

**Check out this AWS Transit Gateway Cheat Sheet:**

[https://tutorialsdojo.com/aws-transit-gateway/](https://tutorialsdojo.com/aws-transit-gateway/)

---

## Câu 25 — ✅ ĐÚNG

### Câu hỏi

A company is running its new web application on a test environment in its on-premises data center. The stateful application is running on a single web server and it connects to a MySQL database that is hosted on a separate server. In a few weeks, the web application is scheduled to be released to the general public and the company is worried about its scalability. The user traffic will be unpredictable so it has been decided to migrate the web application and database to AWS. The company wants to use the Amazon EC2 service for hosting the web application, Amazon Aurora for the database, and Elastic Load Balancing for load distribution.

Which of the following solutions will allow the web and database tier to scale along with user traffic?

### Các phương án

- **A.** Create an Amazon Aurora MySQL database instance. Create an Aurora Replica and enable Aurora Auto Scaling for the replica. Create an Auto Scaling group of Amazon EC2 instances placed behind an Application Load Balancer with the round-robin routing algorithm. Ensure that the sticky sessions feature is enabled for the ALB.
- **B.** Create an Amazon Aurora MySQL database instance and enable Aurora Auto Scaling for the master database. Create an Auto Scaling group of Amazon EC2 instances placed behind a Network Load Balancer with the least outstanding request (LOR) routing algorithm. Ensure that the sticky sessions feature is enabled for the NLB.
- **C.** Create an Amazon Aurora MySQL database instance. Create an Aurora Replica and enable Aurora Auto Scaling for the replica. Create an Auto Scaling group of Amazon EC2 instances placed behind a Network Load Balancer with the least outstanding request (LOR) routing algorithm. Ensure that the sticky sessions feature is enabled for the NLB.
- **D.** Create an Amazon Aurora MySQL database instance and enable Aurora Auto Scaling for the master database. Create an Auto Scaling group of Amazon EC2 instances placed behind an Application Load Balancer with the round-robin routing algorithm. Ensure that the sticky sessions feature is enabled for the ALB.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

**Amazon Aurora (Aurora)**  is a fully managed relational database engine that’s compatible with MySQL and PostgreSQL. Aurora includes a high-performance storage subsystem. Its MySQL- and PostgreSQL-compatible database engines are customized to take advantage of that fast distributed storage. To meet your connectivity and workload requirements, Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas provisioned for an Aurora DB cluster using single-master replication. Aurora Auto Scaling is available for both Aurora MySQL and Aurora PostgreSQL. Aurora Auto Scaling enables your Aurora DB cluster to handle sudden increases in connectivity or workload. When the connectivity or workload decreases, Aurora Auto Scaling removes unnecessary Aurora Replicas so that you don’t pay for unused provisioned DB instances.

You define and apply a scaling policy to an Aurora DB cluster. The scaling policy defines the minimum and maximum number of Aurora Replicas that Aurora Auto Scaling can manage. Based on the policy, Aurora Auto Scaling adjusts the number of Aurora Replicas up or down in response to actual workloads, determined by using Amazon CloudWatch metrics and target values. Before you can use Aurora Auto Scaling with an Aurora DB cluster, you must first create an Aurora DB cluster with a primary instance and at least one Aurora Replica.

![image](https://media.tutorialsdojo.com/sap_aurora_rds.jpg)

Aurora Auto Scaling uses a scaling policy to adjust the number of Aurora Replicas in an Aurora DB cluster. Aurora Auto Scaling has the following components:

**A service-linked role**  – a service role to allow scaling of the Aurora Replicas

**A target metric**  – a predefined or custom metric and a target value for the metric. Aurora Auto Scaling creates and manages CloudWatch alarms that trigger the scaling policy

**Minimum and maximum capacity**  – the minimum and maximum number of Aurora Replicas to be managed by Application Auto Scaling

**A cooldown period**  – blocks subsequent scale-in or scale-out requests until the specified period expires.

**Sticky sessions**  are a mechanism to route requests to the same target in a target group. This is useful for servers that maintain state information in order to provide a continuous experience to clients. To use sticky sessions, the clients must support cookies. Sticky sessions are helpful if your stateful application is having problems handling user sessions in an Auto Scaling environment.

There are two common routing algorithms for Application Load Balancers (ALB):

– Round Robin

– Least Outstanding Requests (LOR)

With the Least outstanding requests (LOR) algorithm, customers can route requests within a target group. As the new request comes in, the load balancer will send it to the target with the least number of outstanding requests. Targets processing long-standing requests or having lower processing capabilities are not burdened with more requests and the load is evenly spread across targets. This also helps the new targets to effectively take the load off of overloaded targets.

Therefore, the correct answer is: **Create an Amazon Aurora MySQL database instance. Create an Aurora Replica and enable Aurora Auto Scaling for the replica. Create an Auto Scaling group of Amazon EC2 instances placed behind an Application Load Balancer with the round-robin routing algorithm. Ensure that the sticky sessions feature is enabled for the ALB.**

The option that says: **Create an Amazon Aurora MySQL database instance. Create an Aurora Replica and enable Aurora Auto Scaling for the replica. Create an Auto Scaling group of Amazon EC2 instances placed behind a Network Load Balancer with the least outstanding request (LOR) routing algorithm. Ensure that the sticky sessions feature is enabled for the NLB**  is incorrect. A Network Load Balancer is only recommended if your application expects millions of requests per second. Since there is no mention of this strict requirement on the question, the Application Load Balancer is the recommended choice as it is less expensive and supports Layer 7 features that are suitable for web applications.

The option that says: **Create an Amazon Aurora MySQL database instance and enable Aurora Auto Scaling for the master database. Create an Auto Scaling group of Amazon EC2 instances placed behind an Application Load Balancer with the round-robin routing algorithm. Ensure that the sticky sessions feature is enabled for the ALB**  is incorrect. You cannot set Auto Scaling for the master database on Amazon Aurora. You can only manually resize the instance size of the master node.

The option that says: **Create an Amazon Aurora MySQL database instance and enable Aurora Auto Scaling for the master database. Create an Auto Scaling group of Amazon EC2 instances placed behind a Network Load Balancer with the least outstanding request (LOR) routing algorithm. Ensure that the sticky sessions feature is enabled for the NLB** is incorrect because it is not possible to set Auto Scaling for the master database on Amazon Aurora. You can only manually resize the instance size of the master node. Take note that a Network Load Balancer doesn’t fully support the least outstanding request (LOR) routing algorithm as this is commonly used in Application Load Balancers instead.

**References:**

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html)

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)

[https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html)

**Check out the Amazon Aurora and AWS Elastic Load Balancing Cheat Sheets:**

[https://tutorialsdojo.com/amazon-aurora/](https://tutorialsdojo.com/amazon-aurora/)

[https://tutorialsdojo.com/aws-elastic-load-balancing-elb/](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/)

---

## Câu 26 — ✅ ĐÚNG

### Câu hỏi

A call center company has recently adopted a hybrid architecture requiring predictable network performance and reduced bandwidth costs to connect its data center and AWS Cloud. Two AWS Direct Connect connections have been implemented between the data center and AWS to ensure stable and highly available network performance. After a recent IT financial audit, it was decided to review the current implementation and replace it with a more cost-effective option.

Which of the following connectivity setups would be recommended for this scenario?

### Các phương án

- **A.** Use AWS VPN CloudHub to connect your data center network to Amazon VPC
- **B.** A single AWS Direct Connect connection and enable the built-in failover feature
- **C.** A single AWS Direct Connect and an AWS managed VPN connection to connect your data center with Amazon VPC
- **D.** Setup a Hardware VPN on your datacenter and set it to use the Direct Connect for its connection

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

The scenario requires you to revise the current setup of using two Direct Connect connections being used by the company. Since Direct Connect does not provide any redundancy for its connection, it is recommended to set up at least two connections for high availability. However, this setup is expensive as you will be charged for the two Direct Connect connections. Usually, the second connection is used only when the main connection fails, which rarely happens.

To maintain high availability but reduce costs, you can use a single ***AWS Direct Connect***  to create a dedicated private connection from your data center network to your Amazon VPC and then combine this connection with an ***AWS-managed VPN connection***  to create an IPsec-encrypted connection as a backup connection. If the Direct Connect connection fails, you still have a managed VPN to connect to your Amazon VPC, albeit with a slower connection. This will suffice until your Direct Connect connection is restored.

![image](https://media.tutorialsdojo.com/sap_directconnect_vpn.jpg)

Therefore, the correct answer is: **A single AWS Direct Connect and an AWS managed VPN connection to connect your data center with Amazon VPC.**  The AWS Direct Connect connection will provide the high-speed bandwidth network required while having the VPN as the slower backup link in case the main Direct Connect link fails.

The option that says: **A single AWS Direct Connect connection and enable the built-in failover feature**  is incorrect. AWS Direct Connect does not primarily have a built-in failover feature.

The option that says: **Setup a Hardware VPN on your datacenter and set it to use the Direct Connect for its connection**  is incorrect. If you implement this, your VPN will typically fail if Direct Connect fails.

The option that says: **Use AWS VPN CloudHub to connect your data center network to Amazon VPC**  is incorrect. You still need a dedicated high-bandwidth network provided by Direct Connect.

**References:**

[https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html)

[https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-managed-vpn.html](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-managed-vpn.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/configure-vpn-backup-dx/](https://aws.amazon.com/premiumsupport/knowledge-center/configure-vpn-backup-dx/)

**Check out this Amazon VPC Cheat Sheet:**

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

**Comparison of AWS Services Cheat Sheets:**

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

---

## Câu 27 — ✅ ĐÚNG

### Câu hỏi

A government technology agency has recently hired a team to build a mobile tax app that allows users to upload their tax deductions and income records using their devices. The app would also allow users to view or download their uploaded files later on. These files are confidential, tax-related documents that need to be stored in a single, secure S3 bucket. The mobile app’s design is to allow the users to upload, view, and download their files directly from an Amazon S3 bucket via the mobile app. Since this app will be used by potentially hundreds of thousands of taxpayers in the country, the solutions architect must ensure that proper user authentication and security features are in place.

Which of the following options should the solutions architect implement in the infrastructure when a new user registers on the app?

### Các phương án

- **A.** Record the user's information in Amazon RDS and create a role in IAM with appropriate permissions. When the user uses his/her mobile app, create temporary credentials using the 'AssumeRole' function in STS. Store these credentials in the mobile app's memory and use them to access the S3 bucket. Generate new credentials the next time the user runs the mobile app.
- **B.** Use Amazon DynamoDB to record the user's information and when the user uses the mobile app, create access credentials using STS with appropriate permissions. Store these credentials in the mobile app's memory and use them to access the S3 bucket every time the user runs the app.
- **C.** Create a set of long-term credentials using AWS Security Token Service with appropriate permissions. Store these credentials in the mobile app and use them to access Amazon S3.
- **D.** Create an IAM user then assign appropriate permissions to the IAM user. Generate an access key and secret key for the IAM user, store them in the mobile app and use these credentials to access Amazon S3.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

This scenario requires the mobile application to have access to the S3 bucket. The mobile app might potentially have millions of tax-paying users that will upload their documents to S3. In this scenario where mobile applications need to access AWS Resources, always think about using STS actions such as **“AssumeRole”** , **“AssumeRoleWithSAML”** , and **“AssumeRoleWithWebIdentity”** .

You can use the AWS Security Token Service (AWS STS) to create and provide trusted users with temporary security credentials that can control access to your AWS resources. Temporary security credentials work almost identically to the long-term access key credentials that your IAM users can use, with the following differences:

-Temporary security credentials are *short-term* , as the name implies. They can be configured to last for anywhere from a few minutes to several hours. After the credentials expire, AWS no longer recognizes them or allows any kind of access from API requests made with them.

-Temporary security credentials are not stored with the user but are generated dynamically and provided to the user when requested. When (or even before) the temporary security credentials expire, the user can request new credentials, as long as the user requesting them still has permission to do so.

![image](https://media.tutorialsdojo.com/sap_assumeRole.png)

You can let users sign in using a well-known third-party identity provider such as Login with Amazon, Facebook, Google, or any OpenID Connect (OIDC) 2.0 compatible provider. You can exchange the credentials from that provider for temporary permissions to use resources in your AWS account. This is known as the web identity federation approach to temporary access. When you use web identity federation for your mobile or web application, you don’t need to create custom sign-in codes or manage your own user identities. Using web identity federation helps you keep your AWS account secure because you don’t have to distribute long-term security credentials, such as IAM user access keys, with your application.

The option that says: **Record the user’s information in Amazon RDS and create a role in IAM with appropriate permissions. When the user uses his/her mobile app, create temporary credentials using the ‘AssumeRole’ function in STS. Store these credentials in the mobile app’s memory and use them to access the S3 bucket. Generate new credentials the next time the user runs the mobile app**  is correct because it creates an IAM Role with the required permissions and generates temporary security credentials using STS “AssumeRole” function. Furthermore, it generates new credentials when the user runs the app the next time around.

The option that says: **Create a set of long-term credentials using AWS Security Token Service with appropriate permissions. Store these credentials in the mobile app and use them to access Amazon S3**  is incorrect because you should never store credentials inside a mobile app for security purposes to avoid the risk of exposing any access keys or passwords. You should instead grant temporary credentials for the mobile app. In addition, you cannot create long-term credentials using AWS STS, as this service can only generate temporary access tokens.

The option that says: **Use Amazon DynamoDB to record the user’s information and when the user uses the mobile app, create access credentials using STS with appropriate permissions. Store these credentials in the mobile app’s memory and use them to access the S3 bucket every time the user runs the app**  is incorrect. Even though the setup is similar to the previous option and uses DynamoDB, it is still wrong to store long-term credentials in a mobile app as it is a security risk. In addition, it does not create an IAM Role with proper permissions, which is an essential step.

The option that says:**Create an IAM user then assign appropriate permissions to the IAM user. Generate an access key and secret key for the IAM user, store them in the mobile app and use these credentials to access Amazon S3**  is incorrect because it creates an IAM User and not an IAM Role. You should create an IAM Role so that the app can access the AWS Resource via the “AssumeRole” action in STS.

**References:**

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

[https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)

**Check out this AWS IAM Cheat Sheet:**

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 28 — ❌ SAI

### Câu hỏi

A stock trading company is running its application on the AWS cloud. The mission-critical database is hosted on an Amazon RDS for MySQL instance deployed in a Multi-AZ configuration. An AWS Backup rule is in place to take automated snapshots hourly. The operations team recently performed an RDS database failover test and found that it caused an outage of approximately 40 seconds.

The management has asked the solutions architect to implement a solution that will reduce the outage to less than 20 seconds. Most connections should stay alive during failovers except for the ones that are in the middle of a transaction or SQL statement. New database connections should still be accepted, and the incoming write requests should be queued until the failover completes.

Which of the following options should the solutions architect implement to meet the company’s requirements? (Choose THREE.)

### Các phương án

- **A.** Enable the Amazon RDS Optimized Writes feature and create an Amazon ElastiCache for Memcached cluster in front of the database layer to cache any frequently requested queries.
- **B.** Set up an Amazon RDS Proxy in front of the database layer to automatically route traffic to healthy RDS instances.
- **C.** Migrate the Amazon RDS for MySQL cluster to an Amazon Aurora for MySQL cluster.
- **D.** Ensure that Multi-AZ is enabled on Amazon Aurora and create one or more Aurora Replicas.
- **E.** Enable the Amazon RDS Optimized Reads feature and launch an Amazon ElastiCache for Redis cluster in front of the database layer to temporarily serve database queries in case of RDS failure.
- **F.** Ensure that Multi-AZ is enabled on Amazon RDS for MySQL and create one or more read replicas to ensure quick failover.

> **Bạn chọn:** B, E, F
> **Đáp án đúng:** B, C, D

### Giải thích

**Amazon RDS Proxy**  is a fully managed, highly available database proxy for Amazon Relational Database Service (RDS) that makes applications more scalable, more resilient to database failures, and more. Amazon RDS Proxy sits between your application and your relational database to efficiently manage connections to the database and improve the scalability of the application. Amazon RDS Proxy can be enabled for most applications with no code changes.

Your Amazon RDS Proxy instance maintains a pool of established connections to your RDS database instances, reducing the stress on database compute and memory resources that typically occurs when new connections are established. RDS Proxy also shares infrequently used database connections so that fewer connections access the RDS database.

![image](https://media.tutorialsdojo.com/sap_rds_proxy_failover.png)

With RDS Proxy, you can build applications that can transparently tolerate database failures without needing to write complex failure-handling code. The proxy automatically routes traffic to a new database instance while preserving application connections. It also bypasses Domain Name System (DNS) caches to reduce failover times by up to 66% for Aurora Multi-AZ databases

Connecting through a proxy makes your application more resilient to database failovers. When the original DB instance becomes unavailable, RDS Proxy connects to the standby database without dropping idle application connections. Doing so helps to speed up and simplify the failover process. The result is faster failover that’s less disruptive to your application than a typical reboot or database problem.

Without RDS Proxy, a failover involves a brief outage. During the outage, you can’t perform write operations on that database. Any existing database connections are disrupted, and your application must reopen them. The database becomes available for new connections and write operations when a read-only DB instance is promoted in place of one that’s unavailable.

![image](https://media.tutorialsdojo.com/amazon-rds-proxy-DBS-C01.jpg)

For applications that maintain their own connection pool, going through RDS Proxy means that most connections stay alive during failovers or other disruptions. Only connections that are in the middle of a transaction or SQL statement are canceled. RDS Proxy immediately accepts new connections. When the database writer is unavailable, RDS Proxy queues up incoming requests.

For applications that don’t maintain their own connection pools, RDS Proxy offers faster connection rates and more open connections. It offloads the expensive overhead of frequent reconnects from the database. It does so by reusing database connections maintained in the RDS Proxy connection pool. This approach is particularly important for TLS connections, where setup costs are significant.

**Amazon Aurora**  is a modern relational database service offering performance and high availability at scale, fully open-source MySQL and PostgreSQL-compatible editions. Unlike other databases, after a database crash, Amazon Aurora does not need to replay the redo log from the last database checkpoint (typically five minutes) and confirm that all changes have been applied before making the database available for operations. Amazon Aurora moves the buffer cache out of the database process and makes it available immediately at restart time. This prevents you from having to throttle access until the cache is repopulated to avoid brownouts. This reduces database restart times to less than 60 seconds in most cases.

With properly configured Multi-AZ and Aurora replicas, Amazon Aurora can quickly recover from failures. Amazon Aurora does not need to replay the redo log from the last database checkpoint (typically five minutes) and confirm that all changes have been applied before making the database available for operations.

Thus, enabling RDS Proxy can further decrease the downtime of a failover to around 20 seconds (66% reduction from 60 seconds).

Therefore, the correct answers are:

**-Set up an Amazon RDS Proxy in front of the database layer to automatically route traffic to healthy RDS instances.**

**-Migrate the Amazon RDS for MySQL cluster to an Amazon Aurora for MySQL cluster.**

**-Ensure that Multi-AZ is enabled on Amazon Aurora and create one or more Aurora Replicas.**

The option that says: **Enable the Amazon RDS Optimized Writes feature and create an Amazon ElastiCache for Memcached cluster in front of the database layer to cache any frequently requested queries** is incorrect. Memcached is used for database caching only and not as a database proxy. Although it can respond to frequently queried data, it can’t queue any write request to the database while the failover process is in place. The Amazon RDS Optimized Writes feature is not useful in this scenario as it only provides you with up to 2x improvement in write transaction throughput on RDS for MySQL by writing only once while protecting you from data loss.

The option that says: **Enable the Amazon RDS Optimized Reads feature and launch an Amazon ElastiCache for Redis cluster in front of the database layer to temporarily serve database queries in case of RDS failure** is incorrect. Although Redis can store data to some extent similar to a database, it is still no substitute for a real database storage system. Moreover, the Amazon RDS Optimized Reads feature is commonly used to achieve faster query processing by placing temporary tables generated by MySQL on NVMe-based SSD block storage that is physically connected to the host server. This feature cannot make most DB connections stay alive during failovers.

The option that says: **Ensure that Multi-AZ is enabled on Amazon RDS for MySQL and create one or more read replicas to ensure quick failover**  is incorrect. This may be possible since the database is currently on RDS with Multi-AZ. However, RDS automatic database failover can take up to 60 seconds for one standby instance and up to [35 seconds](https://aws.amazon.com/rds/features/multi-az) for two readable standby instances. A better option is to use RDS Proxy to fulfill the aforementioned requirements.

**References:**

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html)

[https://aws.amazon.com/rds/aurora/faqs/](https://aws.amazon.com/rds/aurora/faqs/)

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Concepts.AuroraHighAvailability.Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Concepts.AuroraHighAvailability.Proxy)

**Check out these Amazon Aurora and Amazon RDS Cheat Sheets:**

[https://tutorialsdojo.com/amazon-aurora/](https://tutorialsdojo.com/amazon-aurora/)

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

**Check out this Amazon Aurora vs Amazon RDS comparison:**

[https://tutorialsdojo.com/amazon-aurora-vs-amazon-rds/](https://tutorialsdojo.com/amazon-aurora-vs-amazon-rds/)

---

## Câu 29 — ❌ SAI

### Câu hỏi

A company has data centers in Europe, Asia, and North America. Each data center has a 10Gbps AWS Direct Connect connection to AWS, and the company uses a custom VPN to encrypt traffic between its data center network and AWS. In total, the data centers have about five hundred physical servers that host a mix of Windows and Linux-based applications and database services. The company plans to decommission these data centers and migrate its entire infrastructure to the AWS cloud instead. Separate accounts for staging and launching VMs must be implemented, as well as the ability to do AWS Region-to-Region Amazon VPC stack creation.

Which of the following options is the recommended solution for this migration?

### Các phương án

- **A.** Leverage AWS Storage Gateway for the migration. Install the AWS Storage Gateway software appliance on their on-premises servers and use it to transfer their data to Amazon S3. Once the data is in S3, use Amazon EC2 to create virtual machines that replicate their on-premises infrastructure.
- **B.** Leverage VM Import/Export for the migration. Convert each physical Windows and Linux server into a virtual machine image, upload the images to Amazon S3, import them as AMIs, and manually launch Amazon EC2 instances in the target AWS Regions for testing and cutover.
- **C.** Leverage AWS Transform MGN for the migration. Install the AWS Replication agent on each physical machine to start the replication to the AWS Cloud. Once syncing is completed, launch test instances and initiate cutover to the AWS Cloud.
- **D.** Leverage AWS Outposts service for the migration of physical servers to AWS. Install the Outposts server agent on the data center to incrementally replicate the servers into Amazon Machine Images (AMIs). Deploy the AMIs into Amazon EC2 instances to initiate cutover.

> **Bạn chọn:** B
> **Đáp án đúng:** C

### Giải thích

**AWS Transform MGN**  is an automated lift-and-shift (rehost) solution designed to simplify, accelerate, and lower the cost of migrating applications to AWS. This service enables companies to efficiently lift and shift a large number of physical, virtual, or cloud servers without encountering compatibility issues, performance disruptions, or lengthy cutover periods.

MGN replicates your source servers into your AWS account. When you are ready, it automatically converts and launches these servers on AWS, allowing you to quickly take advantage of the cloud’s cost savings, increased productivity, enhanced resilience, and greater agility. Once your applications are running on AWS, you can utilize AWS services and capabilities to easily replatform or refactor those applications, making lift-and-shift an effective pathway to modernization.

![image](https://media.tutorialsdojo.com/public/AWS%20Transform%20MGN-08JUN2026.png)

AWS Transform MGN is specifically designed for large-scale lift-and-shift migrations of servers. It facilitates the migration of physical, virtual, and cloud servers to AWS. The AWS Replication Agent can be installed on compatible Windows and Linux source servers, enabling continuous block-level replication to AWS. After the replication process, you can launch test instances for validation. Once everything is confirmed, you can proceed with launching cutover instances when the migration is ready. This solution effectively meets the requirements for migrating approximately 500 physical servers, performing test launches, and completing the cutover to AWS.

Therefore, the correct answer is: **Leverage AWS Transform MGN for the migration. Install the AWS Replication agent on each physical machine to start the replication to the AWS Cloud. Once syncing is completed, launch test instances and initiate cutover to the AWS Cloud.**

The option that says: **Leverage AWS Storage Gateway for the migration. Install the Storage Gateway software appliance on their on-premises servers and use it to transfer their data to S3. Once the data is in Amazon S3, use Amazon EC2 to create virtual machines that replicate their on-premises infrastructure**  is incorrect because AWS Storage Gateway is primarily used for connecting an on-premises software appliance with cloud-based storage to provide seamless and secure integration between an organization’s on-premises IT environment and AWS’s storage infrastructure. It is not designed for migrating live applications and databases.

The option that says: **Leverage AWS Outposts service for the migration of physical servers to AWS. Install the Outposts server agent on the data center to incrementally replicate the servers into Amazon Machine Images (AMIs). Deploy the AMIs into Amazon EC2 instances to initiate cutover** is incorrect. AWS Outposts is a service that typically extends AWS infrastructure, services, APIs, and tools to customer premises. It allows customers to build and run applications on-premises using the same programming interfaces as in AWS Regions. It is not a migration service.

The option that says: **Leverage VM Import/Export for the migration. Convert each physical Windows and Linux server into a virtual machine image, upload the images to Amazon S3, import them as AMIs, and manually launch Amazon EC2 instances in the target AWS Regions for testing and cutover**  is incorrect because VM Import/Export is a manual process that is time‑consuming and not scalable for hundreds of servers. It lacks automation, testing workflows, and region‑to‑region stack creation capabilities. It is suitable for small, ad‑hoc migrations but not for large‑scale data center decommissioning.

**References:**

[https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html)

[https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html](https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html)

**Check out these AWS Cheat Sheets:**

[https://tutorialsdojo.com/aws-cheat-sheets/](https://tutorialsdojo.com/aws-cheat-sheets/)

---

## Câu 30 — ✅ ĐÚNG

### Câu hỏi

A multinational bank has recently set up AWS Organizations to manage its several AWS accounts from its various business units. The Senior Solutions Architect attached the SCP below to an Organizational Unit (OU) to define the services that its member accounts can use:

{
 “Version”:”2012-10-17″,
 “Statement”:[
 {
 “Effect”:”Allow”,
 “Action”:[“EC2:*”,”S3:*”],
 “Resource”:”*”
 }
 ]
 }

In one of the member accounts under that OU, an IAM user tried to create a new Amazon S3 bucket but was getting a permission denied error.

Which of the following options is the most likely cause of this issue?

### Các phương án

- **A.** The IAM user in the member account does not have IAM policies that explicitly grant Amazon EC2 or S3 service actions.
- **B.** All accounts within the OU do not automatically inherit the policy attached to them. You still have to manually attach the SCP to the individual AWS accounts of the OU.
- **C.** An IAM policy that allows the use of S3 and Amazon EC2 services should be the one attached to the OU instead of an SCP.
- **D.** Use the root user of the account to be able to create the new S3 bucket.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

A **service control policy (SCP)**  determines what services and actions can be delegated by administrators to the users and roles in the accounts that the SCP is applied to. An SCP ***does not***  grant any permissions. Instead, SCPs are JSON policies that specify the maximum permissions for an organization or organizational unit (OU). The SCP limits permissions for entities in member accounts, including each AWS account root user.

A **service control policy (SCP)**  determines what services and actions can be delegated by administrators to the users and roles in the accounts to which the SCP is applied. An SCP ***does not***  grant any permissions. Instead, SCPs are JSON policies that specify the maximum permissions for an organization or organizational unit (OU). The SCP limits permissions for entities in member accounts, including each AWS account root user.

If the SCP allows the actions for a service, the administrator of the account can grant permissions for those actions to the users and roles in that account, and the users and roles can perform the actions that the administrator granted them. If the SCP denies actions for a service, the administrators in that account can’t effectively grant permissions for those actions, and the users and roles in the account can’t perform the actions even if granted by an administrator.

![image](https://media.tutorialsdojo.com/sap_scp_org_attached.png)

By default, when SCPs are enabled in AWS Organizations, AWS attaches the managed `FullAWSAccess` policy to the root, OUs, and accounts, ensuring no restrictions unless explicitly modified. Since there is no indication in the given scenario that an SCP was modified at the account level, the account simply inherits the OU policy and the default `FullAWSAccess` policy.

Users and roles must still be granted permissions using IAM permission policies attached to them or to groups. The SCPs filter the permissions granted by such policies, and the user can’t perform any actions that the applicable SCPs don’t allow. Actions allowed by the SCPs can be used if they are granted to the user or role by one or more IAM permission policies. Take note that the IAM user being used by the administrator does not have IAM policies that explicitly grant EC2 or S3 service actions.

Hence, the correct answer is: **The IAM user in the member account does not have IAM policies that explicitly grant Amazon EC2 or S3 service actions** .

The option that says: **All accounts within the OU do not automatically inherit the policy attached to them. You still have to manually attach the SCP to the individual AWS accounts of the OU**  is incorrect because an SCP attached to an OU is automatically inherited by all accounts within that same OU. The main cause of this issue is just the missing IAM policy in the account, which explicitly grants EC2 or S3 service actions to the IAM user.

The option that says: **An IAM policy that allows the use of S3 and Amazon EC2 services should be the one attached to the OU instead of an SCP**  is incorrect because you cannot directly assign an IAM policy to an OU. In addition, there is no attached IAM policy that allows EC2 or S3 service actions for the IAM user.

The option that says: **Use the root user of the account to be able to create the new S3 bucket**  is incorrect because SCPs do affect the root user, along with all IAM users and standard IAM roles in any affected account. The issue lies only in the missing IAM policy of the account and not with the SCP, OU, or its AWS Organizations settings.

**References:**

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html)

[https://aws.amazon.com/organizations/faqs/](https://aws.amazon.com/organizations/faqs/)

**Check out these AWS Cheat Sheets:**

[https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/](https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/)

If the SCP allows the actions for a service, the administrator of the account can grant permissions for those actions to the users and roles in that account, and the users and roles can perform the actions of the administrators grant those permissions. If the SCP denies actions for a service, the administrators in that account can’t effectively grant permissions for those actions, and the users and roles in the account can’t perform the actions even if granted by an administrator.

![image](https://media.tutorialsdojo.com/sap_scp_org_attached.png)

Users and roles must still be granted permissions using IAM permission policies attached to them or to groups. The SCPs filter the permissions granted by such policies, and the user can’t perform any actions that the applicable SCPs don’t allow. Actions allowed by the SCPs can be used if they are granted to the user or role by one or more IAM permission policies. Take note that the IAM user being used by the administrator does not have IAM policies that explicitly grant EC2 or S3 service actions.

Hence, the correct answer is: **The IAM user in the member account does not have IAM policies that explicitly grant EC2 or S3 service actions** .

The option that says: **All accounts within the OU does not automatically inherit the policy attached to them. You still have to manually attach the SCP to the individual AWS accounts of the OU**  is incorrect because an SCP attached to an OU is automatically inherited by all accounts within that same OU. The main cause of this issue is the missing IAM policy in the account, which explicitly grants EC2 or S3 service actions to the IAM user.

The option that says: **An IAM policy that allows the use of S3 and EC2 services should be the one attached in the OU instead of an SCP**  is incorrect because you cannot directly assign an IAM policy to an OU. In addition, there is no attached IAM policy that allows EC2 or S3 service actions to the IAM user.

The option that says:**Using the root user of the account to be able to create the new S3 bucket**  is incorrect because SCPs **do**  affect the root user along with all IAM users and standard IAM roles in any affected account. The issue lies in the missing IAM policy of the account and not with the SCP, OU, or its AWS Organizations settings.

**References:**

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html)

[https://aws.amazon.com/organizations/faqs/](https://aws.amazon.com/organizations/faqs/)

**Check out these AWS Cheat Sheets:**

[https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/](https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/)

---

## Câu 31 — ✅ ĐÚNG

### Câu hỏi

A company requires regular processing of a massive amount of product catalogs that need to be handled per batch. The data needs to be processed regularly by on-demand workers. The company instructed its solutions architect to design a workflow orchestration system that will enable to reprocess failures and handle multiple concurrent operations.

What is the MOST suitable solution that the solutions architect should implement in order to manage the state of every workflow?

### Các phương án

- **A.** Use Amazon MQ to set up a batch process workflow that handles the processing for a single batch. Develop worker jobs using AWS Lambda functions.
- **B.** Set up a workflow using AWS Config and AWS Step Functions in order to orchestrate multiple concurrent workflows. Visualize the status of each workflow using the AWS Management Console. Store the historical data in an Amazon S3 bucket and visualize the data using Amazon QuickSight.
- **C.** Store workflow data in an Amazon RDS with AWS Lambda functions polling the RDS database instance for status changes. Set up worker Lambda functions to process the next workflow steps, then use Amazon QuickSight to visualize workflow states directly out of RDS.
- **D.** Implement Step Functions to orchestrate batch processing workflows. Use the AWS Management Console to monitor workflow status and manage failure reprocessing.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

AWS Step Functions lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using Step Functions, you can design and run workflows that stitch together services, such as AWS Lambda, AWS Fargate, and Amazon SageMaker AI, into feature-rich applications.

![image](https://media.tutorialsdojo.com/public/codepipeline_statemachine.png)

In this scenario, the company can leverage AWS Step Functions to design and manage the workflows required for processing massive amounts of product catalogs. Step Functions can orchestrate these workflows by defining them as a series of steps or states, where each state can represent a specific task in the process, such as data validation, transformation, or loading. Furthermore, AWS Step Functions offers built-in mechanisms for error handling and retry policies, which are essential for managing failures in any of the workflow steps. Through the AWS Management Console, you can actively monitor each workflow’s status, seeing real-time updates on successes, failures, and ongoing tasks. This setup makes it much easier for your solutions architect and operations team to quickly spot and troubleshoot any issues.

Hence, the correct answer is: **Implement Step Functions to orchestrate batch processing workflows. Use the AWS Management Console to monitor workflow status and manage failure reprocessing.**

The option that says: **Store workflow data in an Amazon RDS with AWS Lambda functions polling the RDS database instance for status changes. Set up worker Lambda functions to process the next workflow steps, then use Amazon QuickSight to visualize workflow states directly out of RDS** is incorrect. While this could work, it involves more overhead in managing database connections and polling mechanisms, making it less efficient for orchestrating complex workflows compared to using a dedicated service like AWS Step Functions.

The option that says: **Set up a workflow using AWS Config and AWS Step Functions in order to orchestrate multiple concurrent workflows. Visualize the status of each workflow using the AWS Management Console. Store the historical data in an Amazon S3 bucket and visualize the data using Amazon QuickSight** is incorrect. AWS Config is primarily a service for auditing and evaluating the configurations of your AWS resources, not for workflow orchestration.

The option that says: **Use Amazon MQ to set up a batch process workflow that handles the processing for a single batch. Develop worker jobs using AWS Lambda functions** is incorrect. Amazon MQ is simply a message broker service for messaging between software components but does not offer the same level of workflow orchestration or state management capabilities as AWS Step Functions. It’s more suited for decoupling applications and integrating different systems rather than managing complex workflows.

**References:**

[https://aws.amazon.com/step-functions/](https://aws.amazon.com/step-functions/)

[https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-state-machine-structure.html](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-state-machine-structure.html)

[https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html)

**Check out this AWS Step Functions Cheat Sheet:**

[https://tutorialsdojo.com/aws-step-functions/](https://tutorialsdojo.com/aws-step-functions/)

---

## Câu 32 — ✅ ĐÚNG

### Câu hỏi

A consumer goods company runs its e-commerce website entirely on its on-premises data center with high-resolution photos and videos. Due to the unprecedented growth of their popular product, they are expecting an increase in incoming traffic to their website across the globe in the coming days. The CTO requested to urgently do the necessary architectural changes to be able to handle the demand. The solutions architect suggested migrating the application to AWS, but the CTO decided that they need at least 3 months to implement a hybrid cloud architecture.

What could the solutions architect do with the current on-premises website to help offload some of the traffic and scale out to meet the demand in a cost-effective way?

### Các phương án

- **A.** Launch a CloudFront web distribution with the URL of the on-premises web application as the origin. Offload the DNS to AWS to handle CloudFront traffic.
- **B.** Rehost the website to an S3 bucket with website hosting enabled. Create a CloudFront distribution with the S3 endpoint as the origin. Set up Origin Shield and launch a CloudFront Function to offload the DNS to AWS to handle CloudFront traffic.
- **C.** Replicate the current web infrastructure of the on-premises website on AWS. Offload the DNS to Route 53 and configure weight-based DNS routing to send 50% of the traffic to AWS.
- **D.** Use AWS Transit Gateway to establish a dedicated connection with the on-premises website and to manage and configure the servers with AWS App Runner to meet the demand.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

**Amazon CloudFront**  is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay) so that content is delivered with the best possible performance.

![image](https://media.tutorialsdojo.com/sap_cloudfront.png)

– If the content is already in the edge location with the lowest latency, CloudFront delivers it immediately.

– If the content is not in that edge location, CloudFront retrieves it from an origin that you’ve defined—such as an Amazon S3 bucket, a MediaPackage channel, or an HTTP server (for example, a web server) that you have identified as the source for the definitive version of your content.

You can use CloudFront with the on-premises website as the origin. CloudFront is a highly available, scalable service that can cache frequently accessed files on the website and can significantly make the load times faster.

Therefore, the correct answer is: **Launch a CloudFront web distribution with the URL of the on-premises web application as the origin. Offload the DNS to AWS to handle CloudFront traffic.**

The option that says:**Use AWS Transit Gateway to establish a dedicated connection with the on-premises website and to manage and configure the servers with AWS App Runner to meet the demand**  is incorrect since you cannot create a hybrid dedicated connection to your on-premises network by using an AWS Transit Gateway alone. You have to use AWS Direct Connect for this to work. AWS App Runner is simply a fully managed container application service that lets you build, deploy, and run containerized web applications and API services. The scenario didn’t mention any container-based application; thus, AWS App Runner is irrelevant in this case.

The option that says: **Rehost the website to an S3 bucket with website hosting enabled. Create a CloudFront distribution with the S3 endpoint as the origin. Set up Origin Shield and launch a CloudFront Function to offload the DNS to AWS to handle CloudFront traffic** is incorrect. While S3 can be used for hosting websites, it’s only suitable for static websites and simple landing pages, not for full-blown web applications that require dynamic content processing and user interaction. Lastly, the CloudFront function is not capable of DNS offloading, which is typically handled by DNS management services like Route 53.

The option that says: **Replicate the current web infrastructure of the on-premises website on AWS. Offload the DNS to Route 53 and configure weight-based DNS routing to send 50% of the traffic to AWS**  is incorrect as this option is time-consuming and you don’t have enough time to replicate the entire architecture of the on-premises website.

**References:**

[https://aws.amazon.com/cloudfront/](https://aws.amazon.com/cloudfront/)

[https://aws.amazon.com/blogs/aws/amazon-cloudfront-support-for-custom-origins/](https://aws.amazon.com/blogs/aws/amazon-cloudfront-support-for-custom-origins/)

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

**Check out this Amazon CloudFront Cheat Sheet:**

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

---

## Câu 33 — ✅ ĐÚNG

### Câu hỏi

An analytics company hosts its data processing application on its on-premises data center. Data scientists upload input files through a web portal which then are then stored in the company NAS. For every uploaded file, the web server sends a message to the processing server over a message queue. It could take up to 30 minutes to process each file on the NAS. During business hours, the number of files awaiting processing is significantly higher and it could take a while for the processing servers to catch up. The number of files significantly declines after business hours. The company has tasked the solutions architect to migrate this workload to the AWS cloud.

Which of the following options is the recommended solution while being cost-effective?

### Các phương án

- **A.** Reconfigure the web application to publish messages to a new Amazon SQS queue. Create an auto-scaling group of Amazon EC2 instances based on the SQS queue length to pull messages from the queue and process the files. Store the processed files on an Amazon S3 bucket.
- **B.** Reconfigure the web application to publish messages to a new Amazon SQS queue. Write an AWS Lambda function to pull messages from the SQS queue and process the files. Trigger the Lambda function for every new message on the queue. Store the processed files on an Amazon S3 bucket.
- **C.** Reconfigure the web application to publish messages to a new Amazon MQ queue. Create an auto-scaling group of Amazon EC2 instances to pull messages from the queue and process the files. Store the processed files on an Amazon EFS volume. Power off the EC2 when there are no messages left on the queue
- **D.** Reconfigure the web application to publish messages to a new Amazon MQ queue. Write an AWS Lambda function to pull messages from the SQS queue and process the files. Trigger the Lambda function for every new message on the queue. Store the processed files in Amazon EFS.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

**Amazon Simple Queue Service (Amazon SQS)**  offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.

There are some scenarios where you might think about scaling in response to activity in an Amazon SQS queue. For example, suppose that you have a web app that lets users upload images and use them online. In this scenario, each image requires resizing and encoding before it can be published. The app runs on EC2 instances in an Auto Scaling group, and it’s configured to handle your typical upload rates. Unhealthy instances are terminated and replaced to maintain current instance levels at all times. The app places the raw bitmap data of the images in an SQS queue for processing. It processes the images and then publishes the processed images where they can be viewed by users. The architecture for this scenario works well if the number of image uploads doesn’t vary over time. But if the number of uploads changes over time, you might consider using dynamic scaling to scale the capacity of your Auto Scaling group.

There are three main parts to this configuration:

-An **Auto Scaling group to manage EC2**  instances for the purposes of processing messages from an SQS queue.

-A custom metric to send to Amazon CloudWatch that measures the number of messages in the queue per EC2 instance in the Auto Scaling group.

-A target tracking policy that configures your Auto Scaling group to scale based on the custom metric and a set target value. CloudWatch alarms invoke the scaling policy.

The following diagram illustrates the architecture of this configuration.

![image](https://media.tutorialsdojo.com/sap_sqs_auto_scaling.png)

Therefore, the correct answer is: **Reconfigure the web application to publish messages to a new Amazon SQS queue. Create an auto-scaling group of Amazon EC2 instances based on the SQS queue length to pull messages from the queue and process the files. Store the processed files on an Amazon S3 bucket.**  This is a cost-effective solution as the EC2 instances scale out depending on the length of the SQS queue, and Amazon S3 is cheaper compared to Amazon EFS.

The option that says: **Reconfigure the web application to publish messages to a new Amazon SQS queue. Write an AWS Lambda function to pull messages from the SQS queue and process the files. Trigger the Lambda function for every new message on the queue. Store the processed files on an Amazon S3 bucket**  is incorrect. The files may take up to 30 minutes to be processed. AWS Lambda has an execution limit of 15 minutes.

The option that says: **Reconfigure the web application to publish messages to a new Amazon MQ queue. Create an auto-scaling group of Amazon EC2 instances to pull messages from the queue and process the files. Store the processed files on an Amazon EFS volume. Power off the EC2 when there are no messages left on the queue**  is incorrect. This is possible but not the most cost-effective solution. Amazon EFS is significantly more expensive than Amazon S3.

The option that says: **Reconfigure the web application to publish messages to a new Amazon MQ queue. Write an AWS Lambda function to pull messages from the SQS queue and process the files. Trigger the Lambda function for every new message on the queue. Store the processed files in Amazon EFS**  is incorrect. The files may take up to 30 minutes to be processed. AWS Lambda has an execution limit of 15 minutes. Amazon EFS is significantly more expensive than Amazon S3.

**References:**

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html)

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

**Check out these Amazon EC2 and Amazon SQS Cheat Sheets:**

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

[https://tutorialsdojo.com/amazon-sqs/](https://tutorialsdojo.com/amazon-sqs/)

---

## Câu 34 — ❌ SAI

### Câu hỏi

A company plans to migrate its on-premises legacy application to AWS and develop a highly scalable application. Currently, all user requests are sent to the on-premises load balancer which forwards the requests to two Linux servers hosting the legacy application. The database is hosted on two servers in master-master configuration. Since this is an old application, the communication to the database servers is done through static IP addresses and not via DNS names. The license of the application is tied to the MAC address of the network adapter of the Linux server. If the application is to be installed on a new server, it will take about 15 hours for the software vendor to send the new license via email.

Which combination of actions must be done to meet the company requirements? (Select TWO.)

### Các phương án

- **A.** Create an AWS Lambda function to update the database IP addresses on the Systems Manager Parameter Store. Create an Amazon EC2 bootstrap script that will retrieve the database IP address from SSM Parameter Store. Update the local configuration files with the parameters.
- **B.** Install the application on an EC2 instance and configure the needed license file. Update the local configuration with the database IP addresses. Use this instance as the base AMI for all instances in the Auto Scaling group.
- **C.** Create an Amazon EC2 bootstrap script that will resolve the database DNS names into IP addresses. Update the local configuration files with the resolved values.
- **D.** Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files on an Amazon S3 bucket and use bootstrap scripts to retrieve an unused license file and attach corresponding ENI when provisioning EC2 instances.
- **E.** Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files inside an Amazon EC2 instance and create a base AMI from this EC2 instance. Use bootstrap scripts to configure license keys and attach the corresponding ENI when provisioning EC2 instances.

> **Bạn chọn:** B, D
> **Đáp án đúng:** A, D

### Giải thích

**AWS Systems Manager Parameter Store**  provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values as plain text or encrypted data. You can reference Systems Manager parameters in your scripts, commands, SSM documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter.

Parameter Store offers these benefits:

– You can use a secure, scalable, hosted secrets management service with no servers to manage.

– Improve your security posture by separating your data from your code.

– Store configuration data and encrypted strings in hierarchies and track versions.

– Control and audit access at granular levels.

Parameter Store provides support for three types of parameters: `String`, `StringList`, and `SecureString`.

![image](https://media.tutorialsdojo.com/public/Parameter-Store_29AUG2023.jpg)

An **elastic network interface (ENI)**  is a logical networking component in a VPC that represents a virtual network card. It can include the following attributes:

– A primary private IPv4 address from the IPv4 address range of your VPC

– One or more secondary private IPv4 addresses from the IPv4 address range of your VPC

– One Elastic IP address (IPv4) per private IPv4 address

– One public IPv4 address

– One or more IPv6 addresses

– One or more security groups

– A MAC address

– A source/destination check flag

– A description

You can create and configure network interfaces in your account and attach them to instances in your VPC. Your account might also have requester-managed network interfaces, which are created and managed by AWS services to enable you to use other resources and services.

You can create a network interface, attach it to an instance, detach it from an instance, and attach it to another instance. The attributes of a network interface follow it as it’s attached or detached from an instance and reattached to another instance. When you move a network interface from one instance to another, network traffic is redirected to the new instance.

Each instance has a default network interface, called the primary network interface. You cannot detach a primary network interface from an instance. You can create and attach additional network interfaces.

The option that says: **Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files on an Amazon S3 bucket and use bootstrap scripts to retrieve an unused license file and attach corresponding ENI when provisioning EC2 instances**  is correct. Having the license files on an Amazon S3 bucket reduces the management overhead for the EC2 instances, as you can easily add/remove more license keys if needed.

The option that says: **Create an AWS Lambda function to update the database IP addresses on the Systems Manager Parameter Store. Create an Amazon EC2 bootstrap script that will retrieve the database IP address from SSM Parameter Store. Update the local configuration files with the parameters**  is correct. Having the database IP addresses on Parameter Store ensures that all the EC2 instances will have a central location to retrieve the IP addresses. This also reduces the need to constantly update any script from inside the EC2 instance even if you add/remove more databases in the future.

The option that says: **Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files inside an Amazon EC2 instance and create a base AMI from this EC2 instance. Use bootstrap scripts to configure license keys and attach the corresponding ENI when provisioning EC2 instances**  is incorrect. Although this is possible, this is not an ideal solution. If you need more EC2 instances and more ENIs, you will have to manually update your base AMI to include all the new license files. This can be a lot of work if you scale your cluster on a regular basis.

The option that says: **Create an Amazon EC2 bootstrap script that will resolve the database DNS names into IP addresses. Update the local configuration files with the resolved values**  is incorrect. Although this is possible, this is not recommended. You will have to update the bootstrap script manually for the new DNS name every time you create a new database such as when you are scaling out your database instances.

The option that says: **Install the application on an EC2 instance and configure the needed license file. Update the local configuration with the database IP addresses. Use this instance as the base AMI for all instances in the Auto Scaling group**  is incorrect. This will not work because the application license is tied to the MAC address on which it was installed. When you provision a new EC2 instance, it will have a new IP address and a newly assigned MAC address for its network adapter.

**References:**

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)

[https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

[https://docs.aws.amazon.com/cdk/latest/guide/get_ssm_value.html](https://docs.aws.amazon.com/cdk/latest/guide/get_ssm_value.html)

**Check out these AWS SSM Parameter Store and Amazon EC2 Cheat Sheets:**

[https://tutorialsdojo.com/aws-secrets-manager-vs-systems-manager-parameter-store/](https://tutorialsdojo.com/aws-secrets-manager-vs-systems-manager-parameter-store/)

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

---

## Câu 35 — ✅ ĐÚNG

### Câu hỏi

A credit company deployed its online loan application system in an Auto Scaling group across multiple Availability Zones in the ap-southeast-2 region. As part of the company’s Disaster Recovery Plan, the target RTO must be less than 2 hours, and the target RPO must be 10 minutes. At 12:00 PM, a production incident occurred in the main database, and the operations team discovered that transactions made from 10:30 AM onwards cannot be recovered.

How can a solutions architect modify the current architecture to achieve the required RTO and RPO in the event of a similar system failure?

### Các phương án

- **A.** Create database backups every hour and store it to Glacier for archiving. Store the transaction logs in an Amazon S3 bucket every 5 minutes.
- **B.** Create database backups every hour and store it in an Amazon S3 bucket with Cross-Region Replication enabled. Store the transaction logs in the same S3 bucket every 5 minutes.
- **C.** Perform database backups every hour and store the result to Amazon EBS volumes. Backup the transaction logs every 5 minutes to an Amazon S3 bucket with Cross-Region Replication enabled.
- **D.** Improve data redundancy by implementing a synchronous database “source-replica” replication between two Availability Zones.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Businesses of all sizes are using AWS to enable faster disaster recovery of their critical IT systems without incurring the infrastructure expense of a second physical site. AWS supports many disaster recovery architectures, from those built for smaller workloads to enterprise solutions that enable rapid failover at scale. AWS provides a set of cloud-based disaster recovery services that enable fast recovery of your IT infrastructure and data.

**Recovery time objective (RTO)**  – The time it takes after a disruption to restore a business process to its service level, as defined by the operational level agreement (OLA). For example, if a disaster occurs at 12:00 PM (noon) and the RTO is eight hours, the DR process should restore the business process to the acceptable service level by 8:00 PM.

**Recovery point objective (RPO)**  – The acceptable amount of data loss measured in time. For example, if a disaster occurs at 12:00 PM (noon) and the RPO is one hour, the system should recover all data that was in the system before 11:00 AM. Data loss will span only one hour, between 11:00 AM and 12:00 PM (noon).

![image](https://media.tutorialsdojo.com/sap_s3_versioning_enable.png)

A company typically decides on an acceptable RTO and RPO based on the financial impact to the business when systems are unavailable. The company determines financial impact by considering many factors, such as the loss of business and damage to its reputation due to downtime and the lack of system availability. IT organizations then plan solutions to provide cost-effective system recovery based on the RPO within the timeline and the service level established by the RTO.

**Cross-region replication (CRR)**  enables automatic, asynchronous copying of objects across buckets in different AWS Regions. Buckets configured for cross-region replication can be owned by the same AWS account or by different accounts. This is also helpful to durably store your data and for disaster recovery in the event of a region-wide outage.

Therefore, the correct answer is: **Create database backups every hour and store it in an Amazon S3 bucket with Cross-Region Replication enabled. Store the transaction logs in the same S3 bucket every 5 minutes.**

The option that says: **Improve data redundancy by implementing a synchronous database “source-replica” replication between two Availability Zones**  is incorrect. Although this is a valid answer, it will not be able to provide the needed data redundancy in the event of a region-wide outage. If one Availability Zone goes down, then there is another Availability Zone that contains the data. However, if the whole AWS region is down, then the data will be totally unreachable. A better solution is to use S3 and enable Cross-Region Replication (CRR).

The option that says: **Perform database backups every hour and store the result to Amazon EBS volumes. Backup the transaction logs every 5 minutes to an Amazon S3 bucket with Cross-Region Replication enabled**  is incorrect because storing backups to EBS primarily keeps data in the same region, making recovery from a regional failure slower. Although transaction logs are stored in S3, the process of restoring from EBS and applying logs simply adds complexity and risks exceeding the <2-hour RTO.

The option that says: **Create database backups every hour and store it to Glacier for archiving. Store the transaction logs in an Amazon S3 bucket every 5 minutes**  is incorrect because Glacier is intended for long-term archival and simply cannot provide fast recovery. Even with transaction logs stored every 5 minutes, restoring data from Glacier would exceed the RTO. This option only ensures durability but does not support rapid disaster recovery.

**References:**

[https://aws.amazon.com/disaster-recovery/](https://aws.amazon.com/disaster-recovery/)

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

[https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html)

**Check out this Amazon S3 Cheat Sheet:**

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

---

## Câu 36 — ✅ ĐÚNG

### Câu hỏi

A company has released a new mobile game and its backend servers are hosted on the company’s on-premises data center. The game logic is exposed using REST APIs that have multiple functions depending on the user state. Access to the backend services is controlled with an API key, while any test traffic is distinguished by a different key. A central file server stores player session data. User traffic is variable throughout the day but the on-premises servers cannot handle traffic during peak hours. The game also has latency issues caused by the slow fetching of player session data. The management tasked the solutions architect to migrate this infrastructure to AWS in order to improve scalability and reduce the latency for data access while keeping the backend API model unchanged.

Which of the following is the recommended solution to meet the company requirements?

### Các phương án

- **A.** Create a fleet of Amazon EC2 instances to host the backend services. Expose the REST APIs by placing the instances behind a Network Load Balancer (NLB). Use Amazon Aurora Serverless to store the player session data.
- **B.** Use AWS Lambda functions to run the backend game logic. Expose the REST APIs by using Amazon API Gateway. Use Amazon DynamoDB with auto-scaling to store the player session data.
- **C.** Use AWS Lambda functions to run the backend game logic. Expose the REST APIs by using AWS AppSync. Use Amazon Aurora Serverless to store the player session data.
- **D.** Use AWS Lambda functions to run the backend game logic. Expose the REST APIs by placing the Lambda functions behind an Application Load Balancer (ALB). Use Amazon DynamoDB with auto-scaling to store the player session data.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

**AWS Lambda**  is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code is not running. With Lambda, you can run code for virtually any type of application or backend service, all with zero administration.

You can create a web API with an HTTP endpoint for your Lambda function by using **Amazon API Gateway** . API Gateway provides tools for creating and documenting web APIs that route HTTP requests to Lambda functions. You can secure access to your API with authentication and authorization controls. Your APIs can serve traffic over the Internet or can be accessible only within your VPC. Amazon API Gateway invokes your function synchronously with an event that contains a JSON representation of the HTTP request. For custom integration, the event is the body of the request. For a proxy integration, the event has a defined structure.

API Gateway allows you to throttle traffic and authorize API calls to ensure that backend operations withstand traffic spikes and backend systems are not unnecessarily called.

![image](https://media.tutorialsdojo.com/sap_lambda_api_function.png)

You can use **Amazon DynamoDB**  for storing player session data. Gaming companies use Amazon DynamoDB in all parts of game platforms, including game state, player data, session history, and leaderboards. The main benefits that these companies get from DynamoDB are its ability to scale reliably to millions of concurrent users and requests while ensuring consistently low latency—measured in single-digit milliseconds. In addition, as a fully managed service, DynamoDB has no operational overhead. Game developers can focus on developing their games instead of managing databases. Also, as game makers are looking to expand from a single AWS Region to multiple Regions, they can rely on DynamoDB global tables for multi-region, active-active data replication.

Therefore, the correct answer is: **Use AWS Lambda functions to run the backend game logic. Expose the REST APIs by using Amazon API Gateway. Use Amazon DynamoDB with auto-scaling to store the player session data.** API Gateway tightly integrates with AWS Lambda which enables you to quickly build REST compliant serverless applications. DynamoDB is well-suited for scalability to handle fast access to player session data.

The option that says: **Create a fleet of Amazon EC2 instances to host the backend services. Expose the REST APIs by placing the instances behind a Network Load Balancer (NLB). Use Amazon Aurora Serverless to store the player session data**  is incorrect. Aurora Serverless is an on-demand, auto-scaling configuration for Amazon Aurora. It is recommended to use Aurora Serverless for lightly-used applications, with peaks of 30 minutes to several hours a few times each day or several times per year, such as human resources, budgeting, or operational reporting application.

The option that says: **Use AWS Lambda functions to run the backend game logic. Expose the REST APIs by placing the Lambda functions behind an Application Load Balancer (ALB). Use Amazon DynamoDB with auto-scaling to store the player session data**  is incorrect. Although you can use an ALB with Lambda as the backend service, it is still recommended to use API Gateway to expose your APIs. You have a lot more options and flexibility on API Gateway including the ability to use API keys and add custom headers to each request.

The option that says: **Use AWS Lambda functions to run the backend game logic. Expose the REST APIs by using AWS AppSync. Use Amazon Aurora Serverless to store the player session data** is incorrect. AWS AppSync is recommended for applications that are written for GraphQL APIs, not REST APIs.

**References:**

[https://aws.amazon.com/blogs/database/amazon-dynamodb-gaming-use-cases-and-design-patterns/](https://aws.amazon.com/blogs/database/amazon-dynamodb-gaming-use-cases-and-design-patterns/)

[https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html)

[https://docs.aws.amazon.com/lambda/latest/dg/welcome.html](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

**Check out these Amazon API Gateway and Amazon DynamoDB Cheat Sheets:**

[https://tutorialsdojo.com/amazon-api-gateway/](https://tutorialsdojo.com/amazon-api-gateway/)

[https://tutorialsdojo.com/amazon-dynamodb/](https://tutorialsdojo.com/amazon-dynamodb/)

---

## Câu 37 — ✅ ĐÚNG

### Câu hỏi

A fintech startup has several resources provisioned on the AWS cloud. The majority of the company’s compute clusters are composed of an Application Load Balancer (ALB) in front of an Auto Scaling group of On-Demand Amazon EC2 instances. To lower down the overall cost, the management wants to have one EC2 instance terminated whenever the overall CPU utilization of the cluster is at 15% or lower.

Which of the following options should the solutions architect implement for a cost-effective and scalable architecture that satisfies the company requirement?

### Các phương án

- **A.** Use scheduled actions in the Auto Scaling configuration to automatically terminate EC2 instances when the CPU Utilization hits below 15%.
- **B.** Use AWS Lambda triggers to send a notification to the Auto Scaling group when the CPU utilization is less than 15% to kick off the scaling in policy to remove the EC2 instance.
- **C.** Use CloudWatch for the monitoring and configure the scaling in policy of the Auto Scaling group to terminate one EC2 instance when the CPU Utilization is 15% or below.
- **D.** Configure a monitoring script that sends out an email using SNS when the CPU utilization is less than 15% so the administrator can manually remove an EC2 instance.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

**Simple scaling policies**  enable you to take specific actions in response to CloudWatch alarms triggered by changes in metrics like CPU utilization. You can configure these policies to add or remove a specified number of instances when a metric crosses a defined threshold. **Amazon EC2 Auto Scaling**  is responsible for creating and managing the CloudWatch alarms that trigger the scaling policy and calculate the scaling adjustment based on the metric and the target value. The scaling policy adds or removes capacity as needed to maintain the metric at, or close to, the specified target value. In addition to keeping the metric close to the target value, a target tracking scaling policy adjusts to fluctuations in the metric due to a fluctuating load pattern and minimizes rapid fluctuations in the capacity of the Auto Scaling group.

![image](https://media.tutorialsdojo.com/sap_autoscaling_group.png)

For example, you could use simple scaling to:

Configure a simple scaling policy to add instances when your Auto Scaling group’s average CPU utilization exceeds 70% and remove instances when it falls below 30%.

Configure a simple scaling policy to scale up when the request count per target of your Elastic Load Balancing target group exceeds 1200 and scale down when it falls below 800.

Therefore, the correct answer is: **Use CloudWatch for the monitoring and configure the scaling in policy of the Auto Scaling group to terminate one EC2 instance when the CPU Utilization is 15% or below.**

The option that says: **Use scheduled actions in the Auto Scaling configuration to automatically terminate EC2 instances when the CPU Utilization hits below 15%**  is incorrect. You can’t use scheduled actions because the CPU usage of the instances can be unpredictable depending on the network traffic.

The option that says: **Configure a monitoring script that sends out an email using SNS when the CPU utilization is less than 15% so the administrator can manually remove an EC2 instance**  is incorrect. You don’t have to configure your own monitoring script. Amazon CloudWatch has integration with Amazon SNS to send scaling notifications to you.

The option that says: **Use AWS Lambda triggers to send a notification to the Auto Scaling group when the CPU utilization is less than 15% to kick off the scaling in policy to remove the EC2 instance**  is incorrect. This may be possible, but you don’t have to create your own Lambda triggers. The Auto Scaling group has built-in functionality to automatically remove an EC2 instance depending on your CPU threshold setting.

**References:**

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/autoscaling-policy-cloudwatch-alarm/](https://aws.amazon.com/premiumsupport/knowledge-center/autoscaling-policy-cloudwatch-alarm/)

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-monitoring-features.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-monitoring-features.html)

**Check out this AWS Auto Scaling Cheat Sheet:**

[https://tutorialsdojo.com/aws-auto-scaling/](https://tutorialsdojo.com/aws-auto-scaling/)

---

## Câu 38 — ❌ SAI

### Câu hỏi

A company wants to release a weather forecasting app for mobile users. The application servers generate a weather forecast every 15 minutes, and each forecast update overwrites the older forecast data. Each weather forecast outputs approximately 1 billion unique data points, where each point is about 20 bytes in size. This results in about 20GB of data for each forecast. Approximately 1,500 global users access the forecast data concurrently every second, and this traffic can spike up to 10 times more during weather events. The company wants users to have a good experience when using the weather forecast application so it requires that each user query must be processed in less than two seconds.

Which of the following solutions will meet the required application request rate and response time?

### Các phương án

- **A.** Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Configure a cache-control timeout of 15 minutes in the API caching section of the API Gateway stage.
- **B.** Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Write an Amazon Lambda@Edge function to cache the data points on edge locations for a 15-minute duration.
- **C.** Use an Amazon EFS volume to store the weather forecast data points. Mount this EFS volume on a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution.
- **D.** Create an Amazon S3 bucket to store the weather forecast data points as individual objects. Create a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer to query the objects on the S3 bucket. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution.

> **Bạn chọn:** A
> **Đáp án đúng:** C

### Giải thích

**Amazon Elastic File System (Amazon EFS)**  provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is built to scale on-demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth.

Amazon EFS can provide very low and consistent operational latency as well as a throughput scale of 10+GB per second.

Amazon EFS file systems are distributed across an unconstrained number of storage servers. This distributed data storage design enables file systems to grow elastically to petabyte scale and enables massively parallel access from Amazon EC2 instances to your data. The Amazon EFS-distributed design avoids the bottlenecks and constraints inherent to traditional file servers.

This distributed data storage design means that multithreaded applications and applications that concurrently access data from multiple Amazon EC2 instances can drive substantial levels of aggregate throughput and IOPS. Big data and analytics workloads, media processing workflows, content management, and web serving are examples of these applications. In addition, Amazon EFS data is distributed across multiple Availability Zones, providing a high level of durability and availability.

![image](https://media.tutorialsdojo.com/sap_efs_how_it_works.png)

**Amazon CloudFront**  is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. CloudFront can provide a reliable, low latency, and high throughput network connectivity for global users.

To deliver content to end-users with lower latency, Amazon CloudFront peers with thousands of Tier 1/2/3 telecom carriers globally is well connected with all major access networks for optimal performance and has hundreds of terabits of deployed capacity.

Therefore, the correct answer is: **Use an Amazon EFS volume to store the weather forecast data points. Mount this EFS volume on a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution.**

The option that says: **Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Configure a cache-control timeout of 15 minutes in the API caching section of the API Gateway stage**  is incorrect. This is a possible implementation, but the Lambda functions won’t be able to quickly scale and serve requests during peak traffic. By default, the burst concurrency for Lambda functions is between 500-3000 requests per second (depending on region).

The option that says: **Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Write an Amazon Lambda[@Edge](https://portal.tutorialsdojo.com/members/edge/) function to cache the data points on edge locations for a 15-minute duration**  is incorrect. While using Amazon OpenSearch and Lambda functions to query the data is a valid approach, the use of Lambda[@Edge](https://portal.tutorialsdojo.com/members/edge/) for caching the data points at the edge locations is not the most appropriate choice. Lambda[@Edge](https://portal.tutorialsdojo.com/members/edge/) is primarily used to customize the behavior of CloudFront distributions, not to serve as the core caching mechanism for large datasets.

The option that says: **Create an Amazon S3 bucket to store the weather forecast data points as individual objects. Create a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer to query the objects on the S3 bucket. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution**  is incorrect. This solution is not recommended. Access from the EC2 instances to the S3 bucket via HTTP calls will increase the total response time of the application. Access to EFS is faster compared to calling objects on S3 buckets. Although AWS S3 supports strong read-after-write consistency, billions of objects will be overwritten on the S3 bucket every 15 minutes which could take longer to write than using Amazon EFS.

**References:**

[https://aws.amazon.com/efs/](https://aws.amazon.com/efs/)

[https://aws.amazon.com/cloudfront/features/](https://aws.amazon.com/cloudfront/features/)

[https://docs.aws.amazon.com/efs/latest/ug/performance.html](https://docs.aws.amazon.com/efs/latest/ug/performance.html)

**Check out the Amazon EFS and comparison Cheat Sheets:**

[https://tutorialsdojo.com/amazon-efs/](https://tutorialsdojo.com/amazon-efs/)

[https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/](https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/)

---

## Câu 39 — ✅ ĐÚNG

### Câu hỏi

A law firm has decided to use Amazon S3 buckets for storage after an extensive Total Cost of ownership (TCO) analysis comparing S3 versus acquiring more storage for its on-premises hardware. The attorneys, paralegals, clerks, and other employees of the law firm will be using Amazon S3 buckets to store their legal documents and other media files. For a better user experience, the management wants to implement a single-sign-on system in which the user can just use their existing Active Directory login to access the S3 storage to avoid having to remember yet another password.

Which of the following options should the solutions architect implement for the above requirement and also provide a mechanism that restricts access for each user to a designated user folder in a bucket? (Select TWO.)

### Các phương án

- **A.** Configure an IAM Policy that restricts access only to the user-specific folders in the Amazon S3 Bucket.
- **B.** Set up a federation proxy or a custom identity provider and use AWS Security Token Service to generate temporary tokens. Use an IAM Role to enable access to AWS services.
- **C.** Set up a matching IAM user and IAM Policy for every user in your corporate directory that needs access to a folder in the bucket.
- **D.** Use Amazon Connect to integrate the on-premises Active Directory with Amazon S3 and AWS IAM.
- **E.** Configure an IAM user that provides access for the user and an IAM Policy that restricts access only to the user-specific folders in the S3 Bucket.

> **Bạn chọn:** A, B
> **Đáp án đúng:** A, B

### Giải thích

Federation enables you to manage access to your AWS Cloud resources centrally. With federation, you can use single sign-on (SSO) to access your AWS accounts using credentials from your corporate directory. Federation uses open standards, such as Security Assertion Markup Language 2.0 (SAML), to exchange identity and security information between an identity provider (IdP) and an application.

![image](https://media.tutorialsdojo.com/sap_sso_ldap_broker.png)

Your users might already have identities outside of AWS, such as in your corporate directory. If those users need to work with AWS resources (or work with applications that access those resources) then those users also need AWS security credentials. You can use an IAM role to specify permissions for users whose identity is federated from your organization or a third-party identity provider (IdP). Setting up an identity provider for federated access is required for integrating your on-premises Active Directory with AWS.

Therefore, the following options are the correct answers:

**– Set up a federation proxy or a custom identity provider and use AWS Security Token Service to generate temporary tokens. Use an IAM Role to enable access to AWS services.**

**– Configure an IAM Policy that restricts access only to the user-specific folders in the Amazon S3 Bucket.**

The option that says: **Using Amazon Connect to integrate the on-premises Active Directory with Amazon S3 and AWS IAM** is incorrect because Amazon Connect is simply an easy to use omnichannel cloud contact center that helps companies provide superior customer service at a lower cost.

The option that says: **Configure an IAM user that provides access for the user and an IAM Policy that restricts access only to the user-specific folders in the S3 Bucket**  is incorrect because you have to use an IAM Role, instead of an IAM user, to provide the access needed to your AWS Resources.

The option that says: **Set up a matching IAM user and IAM Policy for every user in your corporate directory that needs access to a folder in the bucket**  is incorrect because you should be creating IAM Roles rather than IAM Users.

**References** :

[https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket/](https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket/)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html)

**Check out this AWS Identity & Access Management (IAM) Cheat Sheet:**

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 40 — ❌ SAI

### Câu hỏi

A digital media publishing company hired a solutions architect to manage its online portal, which is deployed on a single Amazon EC2 instance. The architecture uses a combination of Reserved EC2 Instances to handle the steady-state load and On-Demand EC2 Instances to handle the peak load. Currently, the web servers operate at 90% utilization during peak load.

Which of the following is the most cost-effective option to enable the online portal to quickly recover in the event of a zone outage?

### Các phương án

- **A.** Launch a Spot Fleet of On-demand and Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet.
- **B.** Create an Auto Scaling group of Spot instances on multiple Availability Zones. Attach an Application Load Balancer to the group.
- **C.** Launch a Spot Fleet of Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet.
- **D.** Create an Auto Scaling group On-Demand instances on multiple Availability Zones. Attach an Application Load Balancer to the group.

> **Bạn chọn:** D
> **Đáp án đúng:** A

### Giải thích

A Spot Fleet is a set of Spot Instances and optionally On-Demand Instances that are launched based on criteria that you specify. The Spot Fleet selects the Spot capacity pools that meet your needs and launches Spot Instances to meet the target capacity for the fleet. By default, Spot Fleets are set to maintain target capacity by launching replacement instances after Spot Instances in the fleet are terminated. You can submit a Spot Fleet as a one-time request, which does not persist after the instances have been terminated. You can include On-Demand Instance requests in a Spot Fleet request.

![image](https://media.tutorialsdojo.com/sap_ec2_type_fleet_request.png)

To avoid interruption to your Spot instances, you can actually set up a diversified spot fleet allocation strategy in which you are using a range of different EC2 instance types such as c3.2xlarge, m3.xlarge, r3.xlarge et cetera instead of just one type. This will effectively increase the chances of providing a more stable compute capacity to your application. Therefore, in the event that there is a Spot interruption due to the high demand for a specific instance type, say c3.2xlarge, your application could still scale using another instance type, such as m3.xlarge or r3.xlarge.

In the scenario, using a mix of On-demand and Spot instances within a Spot Fleet across multiple Availability Zones strikes the right balance. The On-demand instances primarily handle the steady-state load, while additional Spot instances are launched to help with the increased load during peak times, keeping costs down. The fleet setup automatically adjusts to maintain service even if an Availability Zone goes down, ensuring that the system is both cost-effective and resilient.

Hence, the correct answer is: **Launch a Spot Fleet of On-demand and Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet.**

The option that says: **Create an Auto Scaling group of Spot instances on multiple Availability Zones. Attach an Application Load Balancer to the group**  is incorrect. While being highly cost-effective due to the use of Spot instances, it could lead to availability issues since Spot instances can be reclaimed by AWS when spot market prices exceed the bid price.

The option that says: **Create an Auto Scaling group On-Demand instances on multiple Availability Zones. Attach an Application Load Balancer to the group**  is incorrect. This approach ensures that the portal can handle peak loads without the risk of losing instances unexpectedly. However, the cost of On-Demand instances is significantly higher than Spot instances, making this option less cost-effective for managing fluctuating or unpredictable workloads.

The option that says: **Launch a Spot Fleet of Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet**  is incorrect. Like the other incorrect option, this solution fully relies on Spot instances and, while being cheaper, is more susceptible to service disruption due to Spot market fluctuations.

**References:**

[https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf#page=11](https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf#page=11)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html#spot-fleet-allocation-strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html#spot-fleet-allocation-strategy)

[https://aws.amazon.com/about-aws/whats-new/2019/08/new-capacity-optimized-allocation-strategy-for-provisioning-amazon-ec2-spot-instances/](https://aws.amazon.com/about-aws/whats-new/2019/08/new-capacity-optimized-allocation-strategy-for-provisioning-amazon-ec2-spot-instances/)

**Check out this Amazon EC2 Cheat Sheet:**

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

---

## Câu 41 — ❌ SAI

### Câu hỏi

A company recently switched to using Amazon CloudFront for its content delivery network. The development team already made the preparations necessary to optimize the application performance for global users. The company’s content management system (CMS) serves both dynamic and static content. The dynamic content is served from a fleet of Amazon EC2 instances behind an application load balancer (ALB) while the static assets are served from an Amazon S3 bucket. The ALB is configured as the default origin of the CloudFront distribution. An Origin Access Control (OAC) was created and applied to the S3 bucket policy to allow access only from the CloudFront distribution. Upon testing the CMS webpage, the static assets return an error 404 message.

Which of the following solutions must be implemented to solve this error? (Select TWO.)

### Các phương án

- **A.** Update the application load balancer listener and create a new path-based rule for the static assets so that it will forward requests to the Amazon S3 bucket.
- **B.** Update the CloudFront distribution and create a new behavior that will forward to the origin of the static assets based on path pattern.
- **C.** Edit the CloudFront distribution and create another origin for serving the static assets.
- **D.** Update the application load balancer listener to check for HEADER condition if the request is from CloudFront and forward it to the Amazon S3 bucket.
- **E.** Replace the CloudFront distribution with AWS Global Accelerator. Configure the AWS Global Accelerator with multiple endpoint groups that target endpoints on all AWS Regions. Use the accelerator’s static IP address to create a record in Amazon Route 53 for the apex domain.

> **Bạn chọn:** A, C
> **Đáp án đúng:** B, C

### Giải thích

**Amazon CloudFront**  is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay) so that content is delivered with the best possible performance.

You create a CloudFront distribution to tell CloudFront where you want the content to be delivered from and the details about how to track and manage content delivery. Then CloudFront uses computers—edge servers—that are close to your viewers to deliver that content quickly when someone wants to see it or use it.

![image](https://media.tutorialsdojo.com/sap_cloudfront_s3_http_steps.png)

In general, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you can either allow everyone to have access to the files there or you can restrict access. To restrict access to content that you serve from Amazon S3 buckets, follow these steps:

- Create a special CloudFront user called an **origin access control (OAC)**  and associate it with your distribution.

- Configure your S3 bucket permissions so that CloudFront can use the OAC to access the files in your bucket and serve them to your users. Make sure that users can’t use a direct URL to the S3 bucket to access a file there.

After you take these steps, users can only access your files through CloudFront, not directly from the S3 bucket.

You can configure a **single CloudFront web distribution**  to serve different types of requests from multiple origins. For example, if you are building a website that serves static content from an Amazon Simple Storage Service (Amazon S3) bucket and dynamic content from a load balancer, you can serve both types of content from a CloudFront web distribution.

Follow these steps to configure a CloudFront web distribution to serve static content from an S3 bucket and dynamic content from a load balancer:

- Open your web distribution from the CloudFront console.

- Choose the **Origins**  tab.

- Create **one origin**  for your S3 bucket and **another origin**  for your load balancer.  **Note:**  If you’re using a custom origin server or an S3 website endpoint, you must enter the origin’s domain name into the **Origin Domain Name**  field.

- From your distribution, choose the **Behaviors**  tab.

- Create a behavior that specifies a path pattern to route all static content requests to the S3 bucket. For example, you can set the “images/*.jpg” path pattern to route all requests for “.jpg” files in the images directory to the S3 bucket.

- Edit the **Default (*)** path pattern behavior and set its **Origin**  as your load balancer.

Therefore, the correct answers are:

**– Edit the CloudFront distribution and create another origin for serving the static assets.**

**– Update the CloudFront distribution and create a new behavior that will forward to the origin of the static assets based on path pattern.**

The option that says: **Update the application load balancer listener and create a new path-based rule for the static assets so that it will forward requests to the Amazon S3 bucket**  is incorrect. The OAC is used to allow only CloudFront to access the static assets on the S3 bucket. Using the load balancer to forward the requests will result in the access denied error.

The option that says: **Replace the CloudFront distribution with AWS Global Accelerator. Configure the AWS Global Accelerator with multiple endpoint groups that target endpoints on all AWS Regions. Use the accelerator’s static IP address to create a record in Amazon Route 53 for the apex domain** is incorrect. AWS Global Accelerator is a network layer service that improves the availability and performance of your applications used by a wide global audience. This service is not a substitute for a CDN service like Amazon CloudFront.

The option that says: **Update the application load balancer listener to check for HEADER condition if the request is from CloudFront and forward it to the Amazon S3 bucket**  is incorrect. Although an ALB can inspect the HTTP Header requests, using the load balancer to forward the requests will result in the access denied error because of the OAC on the S3 bucket policy.

**References:**

[https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html)

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

[https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/)

**Check out this Amazon CloudFront Cheat Sheet:**

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

---

## Câu 42 — ✅ ĐÚNG

### Câu hỏi

A top Internet of Things (IoT) company has developed a wrist-worn activity tracker for soldiers deployed in the field. The device acts as a sensor to monitor the health and vital statistics of the wearer. It is expected that there would be thousands of devices that will send data to the server every minute and after 5 years, the number will increase to tens of thousands. One of the requirements is that the application should be able to accept the incoming data, run it through ETL to store in a data warehouse, and archive the old data. The officers in the military headquarters should have a real-time dashboard to view the sensor data.

Which of the following options is the most suitable architecture to implement in this scenario?

### Các phương án

- **A.** Store the data directly to DynamoDB. Launch a data pipeline that starts an EMR cluster using data from DynamoDB and sends the data to S3 and Redshift.
- **B.** Send the raw data directly to Amazon Data Firehose for processing and output the data to an S3 bucket. For archiving, create a lifecycle policy from S3 to Glacier. Use Amazon EMR to process the data stored in S3 and load the processed data into Amazon Redshift.
- **C.** Leverage Amazon Athena to accept the incoming data and store them using DynamoDB. Setup a cron job that takes data from the DynamoDB table and sends it to an Amazon EMR cluster for ETL, then outputs the result to Amazon Redshift.
- **D.** Store the raw data directly in an Amazon S3 bucket with a lifecycle policy to store in Glacier after a month. Register the S3 bucket as a source on AWS Lake Formation. Launch an EMR cluster access the data lake, runs it through ETL, and then output that data to Amazon Redshift.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Whenever there is a requirement for real-time data collection or analysis, always consider Amazon Kinesis.

**Amazon Data Firehose**  is a fully managed service for delivering real-time streaming data to destinations such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon OpenSearch Service, Splunk, and any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, and Sumo Logic. Data Firehose is part of the Kinesis streaming data platform, along with Kinesis Data Streams and Kinesis Video Streams.

![image](https://media.tutorialsdojo.com/sap_kinesis_data_firehose_overview.png)

Therefore, the correct answer is: **Send the raw data directly to Amazon Data Firehose for processing and output the data to an S3 bucket. For archiving, create a lifecycle policy from S3 to Glacier. Use Amazon EMR to process the data stored in S3 and load the processed data into Amazon Redshift.**  Amazon Kinesis will ingest the data in real-time, transform it, and output it to an Amazon S3 bucket.

The option that says: **Store the data directly to DynamoDB. Launch a data pipeline that starts an EMR cluster using data from DynamoDB and sends the data to S3 and Redshift**  is incorrect. For the collection of real-time data, AWS recommends Amazon Kinesis for ingestion. After ingestion, you can output the data into several AWS services for further processing.

The option that says: **Store the raw data directly in an Amazon S3 bucket with a lifecycle policy to store in Glacier after a month. Register the S3 bucket as a source on AWS Lake Formation. Launch an EMR cluster access the data lake, runs it through ETL, and then output that data to Amazon Redshift**  is incorrect. Amazon S3 can only accept data using HTTP requests, and the data sent by IoT may be in a different format. For ingesting the data, Amazon Kinesis should be the first one to accept, process it, and store it in Amazon S3.

The option that says: **Leverage Amazon Athena to accept the incoming data and store them using DynamoDB. Setup a cron job that takes data from the DynamoDB table and sends it to an Amazon EMR cluster for ETL, then outputs the result to Amazon Redshift**  is incorrect. Amazon Athena is a query service to query data and analyze big data, and not suitable for ingesting real-time IoT data.

**References:**

[https://aws.amazon.com/kinesis/data-firehose/](https://aws.amazon.com/kinesis/data-firehose/)

[https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

[https://docs.aws.amazon.com/kinesisanalytics/latest/java/examples-s3.html](https://docs.aws.amazon.com/kinesisanalytics/latest/java/examples-s3.html)

**Check out this Amazon Kinesis Cheat Sheet:**

[https://tutorialsdojo.com/amazon-kinesis/](https://tutorialsdojo.com/amazon-kinesis/)

---

## Câu 43 — ✅ ĐÚNG

### Câu hỏi

A travel and tourism company has multiple AWS accounts that are assigned to various departments. The marketing department stores the images and media files that are used in its marketing campaigns on an encrypted Amazon S3 bucket in its AWS account. The marketing team wants to share this S3 bucket so that the management team can review the files.

The solutions architect created an IAM role named mgmt_reviewer in the Management AWS account as well as a custom AWS Key Management System (AWS KMS) key on the Marketing AWS account which is associated with the S3 bucket. However, when users from the Management account received an Access Denied error when they assume the IAM role and try to access the objects on the S3 bucket.

Which of the following options should the solutions architect implement to make sure that the users on the Management AWS account can access the Marketing team’s S3 bucket with the minimum required permissions? (Select THREE.)

### Các phương án

- **A.** Ensure that the mgmt_reviewer IAM role policy includes read permissions to the Amazon S3 bucket and a decrypt permission to the custom AWS KSM key.
- **B.** Add an Amazon S3 bucket policy that includes read permission. Ensure that the Principal is set to the Management team’s AWS account ID.
- **C.** Add an Amazon S3 bucket policy that includes read permission. Ensure that the Principal is set to the Marketing team’s AWS account ID.
- **D.** Update the custom AWS KMS key policy in the Marketing account to include decrypt permission for the Management team’s AWS account ID.
- **E.** Ensure that the mgmt_reviewer IAM role on the Management account has full permissions to access the S3 bucket. Add a decrypt permission for the custom KMS key on the IAM policy.
- **F.** Update the custom AWS KMS key policy in the Marketing account to include decrypt permission for the mgmt_reviewer IAM role.

> **Bạn chọn:** A, B, F
> **Đáp án đúng:** A, B, F

### Giải thích

An AWS account—for example, Account A—can grant another AWS account, Account B, permission to access its resources, such as buckets and objects. Account B can then delegate those permissions to users in its account. Account A can also directly grant a user in Account B permissions using a bucket policy. But the user will still need permission from the parent account, Account B, to which the user belongs, even if Account B does not have permission from Account A. As long as the user has permission from both the resource owner and the parent account, the user will be able to access the resource.

In **Amazon S3** , you can grant users in another AWS account (Account B) granular cross-account access to objects owned by your account (Account A).

Depending on the type of access that you want to provide, use one of the following solutions to grant cross-account access to objects:

**-AWS Identity and Access Management (IAM) policies and resource-based bucket policies**  for programmatic-only access to S3 bucket objects

**-IAM policies and resource-based Access Control Lists (ACLs)**  for programmatic-only access to S3 bucket objects

**-Cross-account IAM roles**  for programmatic and console access to S3 bucket objects

![image](https://media.tutorialsdojo.com/sap_s3_cross_account_access.png)

If the requester is an IAM principal, then the AWS account that owns the principal must grant the S3 permissions through an IAM policy. Based on your specific use case, the bucket owner must also grant permissions through a bucket policy or ACL. After access is granted, programmatic access of cross-account buckets is the same as accessing the same account buckets.

To grant access to an **AWS KMS-encrypted**  bucket in Account A to a user in Account B, you must have these permissions in place:

-The bucket policy in Account A must grant access to Account B.

-The AWS KMS key policy in Account A must grant access to the user in Account B.

-The AWS Identity and Access Management (IAM) policy in Account B must grant user access to the bucket and the AWS KMS key in Account A.

The option that says: **Add an Amazon S3 bucket policy that includes read permission. Ensure that the Principal is set to the Management team’s AWS account ID** is correct. The S3 bucket policy must allow read permission from the Management team. Thus, the Principal on the bucket policy should be set to the Management team’s account ID.

The option that says: **Update the custom AWS KMS key policy in the Marketing account to include decrypt permission for the mgmt_reviewer IAM role** is correct. The decrypt permission is needed by the mgmt_reviewer IAM role to use the KMS key to decrypt the objects on the S3 bucket.

The option that says: **Ensure that the mgmt_reviewer IAM role policy includes read permissions to the Amazon S3 bucket and a decrypt permission to the custom AWS KSM key** is correct. This is needed so that all users assuming this role will have access permission to access the S3 and use the KMS key to decrypt the S3 objects.

The option that says: **Ensure that the mgmt_reviewer IAM role on the Management account has full permissions to access the S3 bucket. Add a decrypt permission for the custom KMS key on the IAM policy**  is incorrect. The Management team only requires read permissions on the S3 bucket. Unless required, you should not grant full permission access to the S3 bucket.

The option that says: **Add an Amazon S3 bucket policy that includes read permission. Ensure that the Principal is set to the Marketing team’s AWS account ID**  is incorrect. The Marketing team already owns the S3 bucket. The bucket policy Principal should be set to the Management team’s account ID.

The option that says: **Update the custom AWS KMS key policy in the Marketing account to include decrypt permission for the Management team’s AWS account ID**  is incorrect. Policy on the KMS key should include the mgmt_reviewer IAM role ARN, not the Management team’s account ID.

**References:**

[https://repost.aws/knowledge-center/cross-account-access-denied-error-s3](https://repost.aws/knowledge-center/cross-account-access-denied-error-s3)

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.html)

[https://repost.aws/knowledge-center/cross-account-access-s3](https://repost.aws/knowledge-center/cross-account-access-s3)

**Check out these Amazon S3 and AWS Key Management Service Cheat Sheets:**

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

[https://tutorialsdojo.com/aws-key-management-service-aws-kms/](https://tutorialsdojo.com/aws-key-management-service-aws-kms/)

---

## Câu 44 — ❌ SAI

### Câu hỏi

A company runs its travel and tours website on AWS. The application only supports HTTP at the moment. To improve their SEO ranking and provide more security for their customers, they decided to enable SSL on their website. The company would also like to ensure the separation of roles between the Development team and the Security team in handling the sensitive SSL certificate. The Development team can log in to EC2 Instances but they should not have access to the SSL certificate, which only the Security team has exclusive control of. Currently, they are using an Application Load Balancer which provides loads of incoming traffic to an Auto Scaling group of On-Demand EC2 instances.

Which of the following options should the solutions architect implement to satisfy the above requirements?

### Các phương án

- **A.** In the web server, set the file owner of the SSL certificate to the Security team and set the file permissions to `700` which will deny all access to the Development team.
- **B.** Create a new private S3 bucket and then upload the SSL certificate owned by the Security team. Configure the EC2 instance to have exclusive access to the certificate and block any access from the Development team.
- **C.** Store the SSL certificate in IAM and authorize access only to the Security team using an IAM policy. Configure the Application Load Balancer to use the SSL certificate instead of the EC2 instances.
- **D.** Retrieve a read-only copy of the SSL certificate upon the boot of the EC2 instance from a CloudHSM, which is exclusively managed by the Security team.

> **Bạn chọn:** D
> **Đáp án đúng:** C

### Giải thích

In the ALB, you can create a listener that uses encrypted connections (also known as SSL offload). This feature enables traffic encryption between your load balancer and the clients that initiate SSL or TLS sessions. To use an HTTPS listener, you must deploy an SSL/TLS server certificate on your load balancer. The load balancer uses this certificate to terminate the connection and then decrypt requests from clients before sending them to the targets.

Although you can terminate the SSL in the EC2 instance, this setup is not recommended in this scenario. It is best to store the SSL certificate in IAM or in AWS Certificate Manager (ACM) where you can control which teams, either the Security or the Development team, can have access.

![image](https://media.tutorialsdojo.com/sap_alb_ssl_cert.png)

Therefore the correct answer is: **Store the SSL certificate in IAM and authorize access only to the Security team using an IAM policy. Configure the Application Load Balancer to use the SSL certificate instead of the EC2 instances.**

The option that says: **In the web server, set the file owner of the SSL certificate to the Security team and set the file permissions to `700` which will deny all access to the Development team**  is incorrect. You don’t have to store the SSL Cert on the EC2 instances. The SSL certificate should be at the Load Balancer since the EC2 instances are behind it and the application only supports HTTP.

The option that says: **Retrieve a read-only copy of the SSL certificate upon the boot of the EC2 instance from a CloudHSM, which is exclusively managed by the Security team**  is incorrect. The clients access the website through the Load Balancer and not the EC2 instances directly. Using CloudHSM to store your SSL certificate will just increase your costs without satisfying the requirement.

The option that says: **Create a new private S3 bucket and then upload the SSL certificate owned by the Security team. Configure the EC2 instance to have exclusive access to the certificate and block any access from the Development team**  is incorrect. The Developers can log in to the EC2, therefore, they will still be able to access the SSL certificate in the EC2 instances after they were downloaded from Amazon S3.

**References:**

[https://aws.amazon.com/premiumsupport/knowledge-center/elb-ssl-tls-certificate-https/](https://aws.amazon.com/premiumsupport/knowledge-center/elb-ssl-tls-certificate-https/)

[https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates)

**Check out this AWS Elastic Load Balancing (ELB) Cheat Sheet:**

[https://tutorialsdojo.com/aws-elastic-load-balancing-elb/](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/)

---

## Câu 45 — ✅ ĐÚNG

### Câu hỏi

A company recently launched its new e-commerce platform that is hosted on its on-premises data center. The web servers connect to a MySQL database. The e-commerce platform is quickly gaining popularity, and the management is worried that the on-premises servers won’t be able to keep up with user traffic in the coming months. They decided to migrate the entire application to AWS to take advantage of the scalability of the cloud. The following are required for this migration:

– Improve the security of the application.

– Increase the reliability and availability of the application.

– Reduce the latency between the users and the application.

– Reduce the maintenance overhead after the migration to the cloud.

Which combination of options should the Solutions Architect implement to meet the company’s requirements? (Select TWO.)

### Các phương án

- **A.** Create an Auto Scaling of Amazon EC2 instances spread in two Availability Zones to host the web servers and the highly available MySQL database cluster in a master and slave configuration.
- **B.** Create an Auto Scaling of Amazon EC2 instances spread in two Availability Zones to host the web servers. To reduce the latency when serving content, create an AWS Global Accelerator endpoint. Migrate the database to an Amazon RDS MySQL instance.
- **C.** Create an Amazon S3 bucket to store and host the static contents. To reduce the latency when serving content, set this bucket as the origin for an Amazon CloudFront distribution. Create AWS WAF rules to block common web exploits.
- **D.** Create an Auto Scaling of Amazon EC2 instances spread in two Availability Zones to host the web servers. Use an Amazon RDS for MySQL with Multi-AZ enabled as the database.
- **E.** Create an Amazon S3 bucket to store the static contents and enable website hosting. To reduce the latency when serving content, enable S3 Transfer Acceleration. Create AWS WAF rules to block common web exploits.

> **Bạn chọn:** C, D
> **Đáp án đúng:** C, D

### Giải thích

**Amazon RDS Multi-AZ**  deployments provide enhanced availability and durability for RDS database (DB) instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure and is engineered to be highly reliable.

Adding **Amazon EC2 Auto Scaling**  to your application architecture is one way to maximize the benefits of the AWS Cloud. When you use Amazon EC2 Auto Scaling, your applications gain the following benefits:

– Better fault tolerance. Amazon EC2 Auto Scaling can detect when an instance is unhealthy, terminate it, and launch an instance to replace it. You can also configure Amazon EC2 Auto Scaling to use multiple Availability Zones. If one Availability Zone becomes unavailable, Amazon EC2 Auto Scaling can launch instances in another one to compensate.

– Better availability. Amazon EC2 Auto Scaling helps ensure that your application always has the right amount of capacity to handle the current traffic demand.

– Better cost management. Amazon EC2 Auto Scaling can dynamically increase and decrease capacity as needed. Because you pay for the EC2 instances you use, you save money by launching instances when they are needed and terminating them when they aren’t.

**Amazon CloudFront**  works seamlessly with **Amazon Simple Storage Service (S3)**  to accelerate the delivery of your web content and reduce the load on your origin servers. The CloudFront edge locations will cache and deliver your content closer to your users to reduce latency and offload capacity from your origin. CloudFront will also restrict access to your S3 bucket to only CloudFront endpoints rendering your content and application more secure and performant.

![image](https://media.tutorialsdojo.com/sap_cloudfront_ssl.jpg)

**AWS WAF**  is a web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources. AWS WAF gives you control over how traffic reaches your applications by enabling you to create security rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that filter out specific traffic patterns you define.

Hence, the correct answers are:

The option that says: **Create an Auto Scaling of Amazon EC2 instances spread in two Availability Zones to host the web servers. Use an Amazon RDS for MySQL with Multi-AZ enabled as the database** is correct. The Auto Scaling group ensures there are enough web servers to answer user requests. Spreading the instances on at least two AZ and enabling Multi-AZ on the database ensure that your application is protected if one AZ in AWS goes down.

The option that says: **Create an Amazon S3 bucket to store and host the static contents. To reduce the latency when serving content, set this bucket as the origin for an Amazon CloudFront distribution. Create AWS WAF rules to block common web exploits**  is correct. Amazon S3 can serve static content and Amazon CloudFront can cache frequently requested content, which greatly improves latency. AWS WAF has default rules that you can enable to block common web exploits to improve your application security in AWS.

The option that says: **Create an Auto Scaling of Amazon EC2 instances spread in two Availability Zones to host the web servers and the highly available MySQL database cluster in a master and slave configuration**  is incorrect. Spreading EC2 instances across multiple AZs is generally good for availability; however, hosting the database on the EC2 instances requires significant management overhead. It is primarily recommended to use Amazon RDS for the database.

The option that says: **Create an Amazon S3 bucket to store the static contents and enable website hosting. To reduce the latency when serving content, enable S3 Transfer Acceleration. Create AWS WAF rules to block common web exploits**  is incorrect. Amazon S3 can typically serve static content, but S3 Transfer Acceleration is used for accelerating transfers going to and from the S3 bucket. Caching with CloudFront would typically be even faster, as it avoids repeated access to the S3 bucket for cached requests.

The option that says: **Create an Auto Scaling of Amazon EC2 instances spread in two Availability Zones to host the web servers. To reduce the latency when serving content, create an AWS Global Accelerator endpoint. Migrate the database to an Amazon RDS MySQL instance**  is incorrect. Without enabling Multi-AZ, your RDS is not protected in the event of a crash or failure. When you promote read-replicas to become master, a small downtime is required. This reduces the application availability.

**References:**

[https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html)

[https://aws.amazon.com/cloudfront/getting-started/S3/](https://aws.amazon.com/cloudfront/getting-started/S3/)

[https://aws.amazon.com/waf/](https://aws.amazon.com/waf/)

**Check out these Amazon RDS, Amazon S3, and Amazon CloudFront Cheat Sheets:**

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

---

## Câu 46 — ✅ ĐÚNG

### Câu hỏi

A logistics company is running its business application on Amazon EC2 instances. The web application is running on an Auto Scaling group of EC2 instances behind an Application Load Balancer. The self-managed MySQL database is also running on a large EC2 instance to handle the heavy I/O operations needed by the application. The application is able to handle the amount of traffic during normal hours. However, the performance slows down significantly during the last four days of the month as more users run their month-end reports simultaneously. The Solutions Architect was tasked to improve the performance of the application, especially during the peak days.

Which of the following should the Solutions Architect implement to improve the application performance with the LEAST impact on availability?

### Các phương án

- **A.** Take a snapshot of the EBS volumes with I/O heavy operations and replace them with Provisioned IOPS volumes during the end of the month. Revert to the old EBS volume type afterward to save on costs.
- **B.** Convert all EBS volumes of the EC2 instances to GP2 volumes to improve I/O performance. Scale up the EC2 instances into bigger instance types. Pre-warm the Application Load Balancer to handle sudden spikes in traffic.
- **C.** Migrate the Amazon EC2 database instance to Amazon RDS for MySQL. Add more read replicas to the database cluster during the end of the month to handle the spike in traffic.
- **D.** Create Amazon CloudWatch metrics based on EC2 instance CPU usage or response time on the ALB. Trigger an AWS Lambda function to change the instance size, type, and the allocated IOPS of the EBS volumes based on the breached threshold.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

**Amazon Relational Database Service (Amazon RDS)**  is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

Amazon RDS supports the most demanding database applications. You can choose between two SSD-backed storage options: one optimized for high-performance OLTP applications, and the other for cost-effective general-purpose use. You can scale your database’s compute and storage resources with only a few mouse clicks or an API call, often with no downtime.

**Amazon RDS Read Replicas**  provide enhanced performance and durability for RDS database (DB) instances. They make it easy to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads. You can create one or more replicas of a given source DB Instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput. Read replicas can also be promoted when needed to become standalone DB instances.

![image](https://media.tutorialsdojo.com/sap_RDSreadreplica_async.jpg)

You can reduce the load on your source DB instance by routing read queries from your applications to the read replica. Read replicas allow you to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads. Because read replicas can be promoted to master status, they are useful as part of a sharding implementation.

In this scenario, the Amazon EC2 instances are in an Auto Scaling group already which means that the database read operations is the possible bottleneck especially during the month-end wherein the reports are generated. This can be solved by creating RDS read replicas.

Therefore, the correct answer is: **Migrate the Amazon EC2 database instance to Amazon RDS for MySQL. Add more read replicas to the database cluster during the end of the month to handle the spike in traffic.**

The option that says: **Convert all EBS volumes of the EC2 instances to GP2 volumes to improve I/O performance. Scale up the EC2 instances into bigger instance types. Pre-warm the Application Load Balancer to handle sudden spikes in traffic**  is incorrect. The Amazon EC2 instances are in an Auto Scaling group already which means that the database read operations is the possible bottleneck so changing to bigger EC2 instances will just increase the costs unnecessarily.

The option that says: **Create Amazon CloudWatch metrics based on EC2 instance CPU usage or response time on the ALB. Trigger an AWS Lambda function to change the instances size, type, and the allocated IOPS of the EBS volumes based on the breached threshold**  is incorrect. This will cause a lot of interruption on the application when you change the EBS volumes and the instance type for the EC2 database instance. You will have to reboot the database instances when you change the instance type.

The option that says: **Take a snapshot of the EBS volumes with I/O heavy operations and replace them with Provisioned IOPS volumes during the end of the month. Revert to the old EBS volume type afterward to save on costs** is incorrect. Creating snapshots will cause the disk write operations to temporarily stop in which the database will stop responding to write requests. Changing the disk types every month is not ideal as this also causes downtime on the application during the switch. A better solution for heavy read operations is to provision an Amazon RDS database with Read Replicas.

**References:**

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

[https://aws.amazon.com/rds/features/read-replicas/](https://aws.amazon.com/rds/features/read-replicas/)

[https://aws.amazon.com/about-aws/whats-new/2018/01/amazon-rds-read-replicas-now-support-multi-az-deployments/](https://aws.amazon.com/about-aws/whats-new/2018/01/amazon-rds-read-replicas-now-support-multi-az-deployments/)

**Check out this Amazon RDS Cheat Sheet:**

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

---

## Câu 47 — ✅ ĐÚNG

### Câu hỏi

A company has deployed a multi-tier web application on AWS that uses Compute Optimized Instances for server-side processing and Storage Optimized EC2 Instances to store various media files. To ensure data durability, there is a scheduled job that replicates the files to each EC2 instance. The current architecture worked for a few months but it started to fail as the number of files grew, which is why the management decided to redesign the system.

Which of the following options should the solutions architect implement in order to launch a new architecture with improved data durability and cost-efficiency?

### Các phương án

- **A.** Migrate and host the entire web application to Amazon S3 for a more cost-effective web hosting. Enable cross-region replication to improve data durability. Use a combination of Consolidated Billing and AWS Trusted advisor checks to monitor the operating costs and identify potential savings.
- **B.** Migrate all media files to an Amazon S3 bucket and use this as the origin for the new CloudFront web distribution. Set up an Elastic Load Balancer with an Auto Scaling of EC2 instances to host the web servers. Use a combination of Cost Explorer and AWS Trusted advisor checks to monitor the operating costs and identify potential savings.
- **C.** Migrate all media files to Amazon EFS then attach this new drive as a mount point to a new set of Storage Optimized EC2 Instances. For the web servers, set up an Elastic Load Balancer with an Auto Scaling of EC2 instances and use this as the origin for a new Amazon CloudFront web distribution. Use a combination of Cost Explorer and AWS Trusted advisor checks to monitor the operating costs and identify potential savings.
- **D.** Migrate the web application to AWS Elastic Beanstalk and move all media files to Amazon EFS for a durable and scalable storage. Set up an Amazon CloudFront distribution with EFS as the origin. Use a combination of Consolidated Billing and AWS Trusted advisor checks to monitor the operating costs and identify potential savings.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Cloud storage is a cloud computing model that stores data on the Internet through a cloud computing provider who manages and operates data storage as a service. It’s delivered on demand with just-in-time capacity and costs, and eliminates buying and managing your own data storage infrastructure. This gives you agility, global scale and durability, with ‘anytime, anywhere’ data access.

**AWS Trusted Advisor**  is an online tool that provides you real-time guidance to help you provision your resources following AWS best practices. Whether establishing new workflows, developing applications, or as part of ongoing improvement, take advantage of the recommendations provided by Trusted Advisor on a regular basis to help keep your solutions provisioned optimally.

**AWS Cost Explorer**  has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. Get started quickly by creating custom reports that analyze cost and usage data, both at a high level and for highly-specific requests. Using AWS Cost Explorer, you can dive deeper into your cost and usage data to identify trends, pinpoint cost drivers, and detect anomalies.

![image](https://media.tutorialsdojo.com/sap_efs_s3_ebs_table.png)

In this scenario, you can use a combination of Cost Explorer and AWS Trusted advisor checks to monitor the operating costs and identify potential savings. For data storage, you can either use S3 or EFS to store the media files. However, S3 is cheaper than EFS and is more suitable to use in storing static media files.

Therefore, the correct answer is: **Migrate all media files to an Amazon S3 bucket and use this as the origin for the new CloudFront web distribution. Set up an Elastic Load Balancer with an Auto Scaling of EC2 instances to host the web servers. Use a combination of Cost Explorer and AWS Trusted advisor checks to monitor the operating costs and identify potential savings.**

The option that says: **Migrate and host the entire web application to Amazon S3 for a more cost-effective web hosting. Enable cross-region replication to improve data durability. Use a combination of Consolidated Billing and AWS Trusted advisor checks to monitor the operating costs and identify potential savings**  is incorrect. Amazon S3 is not capable to handle server-side processing as this can only be used for static websites. Moreover, you can only use Consolidated Billing if your account is configured to use AWS Organizations.

The option that says: **Migrate all media files to Amazon EFS then attach this new drive as a mount point to a new set of Storage Optimized EC2 Instances. For the web servers, set up an Elastic Load Balancer with an Auto Scaling of EC2 instances and use this as the origin for a new Amazon CloudFront web distribution. Use a combination of Cost Explorer and AWS Trusted advisor checks to monitor the operating costs and identify potential savings**  is incorrect. Although this new setup may work, it entails a higher cost to maintain a new set of Storage Optimized EC2 Instances along with EFS. There is also an added cost of maintaining your web-tier which is comprised of an Elastic Load Balancer with another set of Auto Scaling of EC2 instances. It is also better to use S3 instead of EFS since you are only storing media files and not documents which requires file locking or POSIX-compliant storage.

The option that says: **Migrate the web application to AWS Elastic Beanstalk and move all media files to Amazon EFS for a durable and scalable storage. Set up an Amazon CloudFront distribution with EFS as the origin. Use a combination of Consolidated Billing and AWS Trusted advisor checks to monitor the operating costs and identif** **y** **potential savings**  is incorrect. You cannot set EFS as the origin of your CloudFront web distribution. The scenario also doesn’t mention the use of AWS Organization, which is why Consolidated Billing is not applicable.

**References:**

[https://aws.amazon.com/efs/when-to-choose-efs/](https://aws.amazon.com/efs/when-to-choose-efs/)

[https://aws.amazon.com/what-is-cloud-storage/](https://aws.amazon.com/what-is-cloud-storage/)

**Check out this Amazon S3 Cheat Sheet:**

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

**Check out this Amazon S3, EBS, and EFS comparison:**

[https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/](https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/)

---

## Câu 48 — ✅ ĐÚNG

### Câu hỏi

A leading aerospace engineering company has over 1 TB of aeronautical data stored on the corporate file server of its on-premises network. This data is used by a lot of its in-house analytical and engineering applications. The aeronautical data consists of technical files that can have a file size of a few megabytes to multiple gigabytes. The data scientists typically modify an average of 10 percent of these files every day. Recently, the management decided to adopt a hybrid cloud architecture to serve its clients around the globe better. The management requested to migrate its applications to AWS over the weekend to minimize any business impact and system downtime. The on-premises data center has a 50-Mbps Internet connection, which can be used to transfer all of the 1 TB of data to AWS, but based on the calculations, it will take at least 48 hours to complete this task.

Which of the following options will allow the solutions architect to move all of the aeronautical data to AWS MOST cost-effectively?

### Các phương án

- **A.** Set up a Gateway-Stored volume gateway using the AWS Storage Gateway service. 2. Establish an iSCSI connection between your on-premise data center and your AWS Cloud then copy the data to the Storage Gateway volume. 3. After all of your data has been successfully copied, create an EBS snapshot of the volume. 4. Restore the snapshots as EBS volumes and attach them to your EC2 instances on Sunday.
- **B.** Make a reservation on the Data Transfer Terminal console on Thursday since all reservations must be made at least 24 hours in advance. 2. At the end of business hours on Friday, bring the storage devices containing the aeronautical data to the reserved AWS Data Transfer Terminal facility and upload the data to AWS using the facility’s high-bandwidth connection. 3. When the service has completely transferred your data to your AWS Cloud, copy all of the data to multiple EBS Volumes. 4. On Sunday afternoon, mount the generated EBS volume to your EC2 instances.
- **C.** Synchronize the on-premise data to an S3 bucket one week before the migration schedule using the AWS CLI’s S3 `sync` command. 2. Perform a final synchronization task on Friday after the end of business hours. 3. Set up your application hosted in a large EC2 instance in your VPC to use the S3 bucket.
- **D.** Synchronize the data from your on-premise data center to an S3 bucket using Multipart upload for large files from Saturday morning to Sunday evening. 2. Configure your application hosted in AWS to use the S3 bucket to serve the aeronautical data files.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

The most effective choice here is to use the S3 `sync` feature that is available in AWS CLI. In this way, you can comfortably synchronize the data in your on-premises server and in AWS a week before the migration. And on Friday, just do another sync to complete the task. Remember that the sync feature of S3 only uploads the “delta” or in other words, the “difference” in the subset. Therefore, it will only take just a fraction of the time to complete the data synchronization compared to the other methods.

![image](https://media.tutorialsdojo.com/sap_aws_s3_cli.png)

Therefore, the correct answer is:

**1. Synchronize the on-premises data to an S3 bucket one week before the migration schedule using the AWS CLI’s S3 `sync` command.**

**2. Perform a final synchronization task on Friday after the end of business hours.**

**3. Set up your application hosted in a large EC2 instance in your VPC to use the S3 bucket.**

The idea is to synchronize the data days before the migration weekend to avoid the risks and possible delays of transferring the data in such a short period of allowable time, i.e., 48 hours.

The option below is incorrect because although AWS Data Transfer Terminal can move very large datasets quickly, it is not the most cost‑effective solution for only 1 TB of data. Data Transfer Terminal is primarily designed for massive transfers (tens or hundreds of terabytes), where the cost of reserving ports and specialized infrastructure is justified. For smaller datasets, the expense outweighs the benefit compared to simply pre‑synchronizing with the AWS CLI.

**1. Make a reservation on the Data Transfer Terminal console on Thursday since all reservations must be made at least 24 hours in advance.**

**2. At the end of business hours on Friday, bring the storage devices containing the aeronautical data to the reserved AWS Data Transfer Terminal facility and upload the data to AWS using the facility’s high-bandwidth connection.**

**3. When the service has completely transferred your data to your AWS Cloud, copy all of the data to multiple EBS Volumes.**

**4. On Sunday afternoon, mount the generated EBS volume to your EC2 instances.**

The option below is incorrect because you have to create storage volumes in the AWS Cloud that your on-premises applications can access as Internet Small Computer System Interface (iSCSI) targets, which is not mentioned in the option. This is not a cost-effective solution, considering that you only have to migrate 1 TB of data, and the fact that you can just use the S3 `sync` command via AWS CLI.

**1. Set up a Gateway-Stored volume gateway using the AWS Storage Gateway service.**

**2. Establish an iSCSI connection between your on-premises data center and your AWS Cloud then copy the data to the Storage Gateway volume.**

**3. After all of your data has been successfully copied, create an EBS snapshot of the volume.**

**4. Restore the snapshots as EBS volumes and attach them to your EC2 instances on Sunday.**

The option below is incorrect because although using multi-part upload in S3 is faster than regular S3 upload, this method still carries a risk, considering that the company only has a 50 Mbps internet connection. It is still better to use S3 `sync` command via AWS CLI days before the actual migration to mitigate the risks.

**1. Synchronize the data from your on-premises data center to an S3 bucket using Multipart upload for large files from Saturday morning to Sunday evening.**

**2. Configure your application hosted in AWS to use the S3 bucket to serve the aeronautical data files.**

**References:**

[https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)

[https://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html](https://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html)

**Check out this Amazon S3 Cheat Sheet:**

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

---

## Câu 49 — ✅ ĐÚNG

### Câu hỏi

A supermarket chain is planning to launch an online shopping website to allow its loyal shoppers to buy their groceries online. Since there are a lot of online shoppers at any time of the day, the website should be highly available 24/7 and fault-tolerant.

Which of the following options provides the best architecture that meets the above requirement?

### Các phương án

- **A.** Deploy the website across 3 Availability Zones with Auto Scaled EC2 instances behind an Application Load Balancer and a RDS configured with Multi-AZ Deployments.
- **B.** Deploy the website across 3 Availability Zones with Auto Scaled EC2 instances behind an Application Load Balancer and one RDS instance deployed with Read Replicas in the two separate Availability Zones.
- **C.** Deploy the website across 2 Availability Zones with Auto Scaled EC2 instances behind an Application Load Balancer and an Amazon RDS database running in a single Reserved EC2 Instance.
- **D.** Deploy the website across 2 Availability Zones with Auto Scaled EC2 instances each and an RDS instance deployed with Read Replicas in two separate Availability Zones.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

For high availability, it is best to always choose an RDS instance configured with Multi-AZ deployments. You should also deploy your application across multiple Availability Zones to improve fault tolerance. AWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. Using AWS Auto Scaling, it’s easy to set up application scaling for multiple resources across multiple services in minutes.

![image](https://media.tutorialsdojo.com/sap_multiaz_multiregion_readreplica.png)

Amazon RDS Multi-AZ deployments provide enhanced availability and durability for RDS database (DB) instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different [Availability Zone](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones) (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of [Amazon Aurora](https://aws.amazon.com/rds/aurora/)), so that you can resume database operations as soon as the failover is complete. Since the endpoint for your DB Instance remains the same after a failover, your application can resume database operation without the need for manual administrative intervention.

Hence, the correct answer is the option that says: **Deploy the website across 3 Availability Zones with Auto Scaled EC2 instances behind an Application Load Balancer and an RDS configured with Multi-AZ Deployments.**

The option that says: **Deploy the website across 2 Availability Zones with Auto Scaled EC2 instances each and an RDS instance deployed with Read Replicas in two separate Availability Zones**  is incorrect because a Read Replica is primarily used to improve the scalability of the database. This architecture will neither be highly available 24/7 nor fault-tolerant in the event of an AZ outage.

The option that says: **Deploy the website across 3 Availability Zones with Auto Scaled EC2 instances behind an Application Load Balancer and one RDS instance deployed with Read Replicas in the two separate Availability Zones**  is incorrect. Although the EC2 instances are highly available, the database tier is not. You have to use an Amazon RDS database with Multi-AZ configuration.

The option that says: **Deploy the website across 2 Availability Zones with Auto Scaled EC2 instances behind an Application Load Balancer and an Amazon RDS database running in a single Reserved EC2 Instance**  is incorrect. With this architecture, the single Reserved Instance is only deployed in a single AZ. In the event of an AZ outage, the entire database will be unavailable.

**References:**

[https://aws.amazon.com/autoscaling/](https://aws.amazon.com/autoscaling/)

[https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

**Check out this AWS Auto Scaling Cheat Sheet:**

[https://tutorialsdojo.com/aws-auto-scaling/](https://tutorialsdojo.com/aws-auto-scaling/)

---

## Câu 50 — ✅ ĐÚNG

### Câu hỏi

A large company has multiple AWS accounts with multiple IAM Users that launch different types of Amazon EC2 instances and EBS volumes every day. As a result, most accounts quickly hit the service limit and IAM users can no longer create any new instances. When cleaning up the AWS accounts, the solutions architect noticed that the majority of the instances and volumes are untagged. Therefore, it is difficult to pinpoint the owner of these resources and verify if they are safe to terminate. Because of this, the management had issued a new protocol that requires adding a predefined set of tags before anyone can launch their EC2 instances.

Which of the following options is the simplest way to enforce this new requirement?

### Các phương án

- **A.** Apply an IAM policy to the individual member accounts of the OU that includes a `Condition` element in the policy containing the `ForAllValues` qualifier and the `aws:TagKeys` condition. This policy will require its principals to attach specific tags to their resources during creation.
- **B.** Configure AWS Organizations to group different accounts into separate Organizational Units (OU) depending on the business function. Create a rule in AWS Config requiring users to tag specific resources and raise an alert whenever the rule is violated. The Config Rule should allow a user to launch EC2 instances only if the user adds all the tags defined in the rule. If the user applies any other tag then the action is denied.
- **C.** Configure AWS Organizations to group different accounts into separate Organizational Units (OU) depending on the business function. Create a rule using AWS Systems Manager requiring users to tag specific resources and raise an alert whenever the rule is violated. This will allow a user to launch EC2 instances only if certain tags were defined. If the user applies any other tag then the action is denied.
- **D.** Configure AWS Organizations to group different accounts into separate Organizational Units (OU) depending on the business function. Create a Service Control Policy that restricts launching any AWS resources without a tag by including the `Condition` element in the policy which uses the `ForAllValues` qualifier and the `aws:TagKeys` condition. This policy will require its principals to tag resources during creation. Apply the SCP to the OU which will automatically cascade the policy to individual member accounts.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

You can specify tags for EC2 instances and EBS volumes as part of the API call that creates the resources. Using this principle, you can require users to tag specific resources by applying conditions to their IAM policy. Using AWS Organizations, you can consolidate all of your AWS accounts and group the business units into separate Organizational Units (OUs) with a custom service control policy (SCP).

![image](https://media.tutorialsdojo.com/sap_aws_organization_explanations.png)

You can configure your IAM policy to allow a user to launch an EC2 instance and create an EBS volume only if the user applies all the tags that are defined in the policy using the **`ForAllValues`** qualifier. If the user applies any tag that’s not included in the policy then the action is denied. To enforce case sensitivity, use the condition ***`aws:TagKeys`*** .

You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs.

Therefore, the correct answer is: **Configure AWS Organizations to group different accounts into separate Organizational Units (OU) depending on the business function. Create a Service Control Policy that restricts launching any AWS resources without a tag by including the `Condition` element in the policy which uses the `ForAllValues` qualifier and the `aws:TagKeys` condition. This policy will require its principals to tag resources during creation. Apply the SCP to the OU which will automatically cascade the policy to individual member accounts.**

The option that says: **Apply an IAM policy to the individual member accounts of the OU that includes a `Condition` element in the policy containing the `ForAllValues` qualifier and the `aws:TagKeys` condition. This policy will require its principals to attach specific tags to their resources during creation**  is incorrect as it requires a lot of effort to implement the policy in each and every AWS account of the organization. You should set up AWS Organizations, group different accounts into separate Organizational Units (OU), and use SCP instead.

The option that says: **Configure AWS Organizations to group different accounts into separate Organizational Units (OU) depending on the business function. Create a rule in AWS Config requiring users to tag specific resources and raise an alert whenever the rule is violated. The Config Rule should allow a user to launch EC2 instances only if the user adds all the tags defined in the rule. If the user applies any other tag then the action is denied**  is incorrect. AWS Config only audits and evaluates if your instance and volume configurations match the rules you have created. Unlike an IAM policy, it does not permit nor restrict users from performing certain actions.

The option that says: **Configure AWS Organizations to group different accounts into separate Organizational Units (OU) depending on the business function. Create a rule using AWS Systems Manager requiring users to tag specific resources and raise an alert whenever the rule is violated. This will allow a user to launch EC2 instances only if certain tags were defined. If the user applies any other tag then the action is denied**  is incorrect because you cannot create a rule using AWS Systems Manager requiring users to tag specific resources and raise an alert whenever the rule is violated. You have to use an IAM policy in order to do this.

**References:**

[https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-tags-restrict/](https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-tags-restrict/)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_multi-value-conditions.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_multi-value-conditions.html)

**Check out this AWS IAM Cheat Sheet:**

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

**Service Control Policies (SCP) vs IAM Policies:**

[https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/](https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/)

**Comparison of AWS Services Cheat Sheets:**

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

---

## Câu 51 — ❌ SAI

### Câu hỏi

A company runs a mission-critical application on a fixed set of Amazon EC2 instances behind an Application Load Balancer. The application responds to user requests by querying a 120GB dataset. The application requires high throughput and low latency storage so the dataset is stored on Provisioned IOPS (PIOPS) Amazon EBS volumes with 3000 IOPS provisioned. The EC2 launch template has been configured to allocate and attach this 120GB size PIOPS EBS volume for the fleet of EC2 instances. After a few months of operation, the company noticed the high cost of EBS volumes in the billing section. The Solutions Architect has been tasked to design a solution that will reduce the costs without a negative impact on the application performance and data durability.

Which of the following solutions will meet the company requirements?

### Các phương án

- **A.** Remove the PIOPS EBS volume allocation on the EC2 launch template. Attach a 120GB instance store volume on the EC2 instance to ensure that the application will have enough IOPS for its operation.
- **B.** Use the cheaper General Purpose SSD (gp2) EBS volumes instead of PIOPS EBS volumes. Allocating 1TB EBS volumes (gp2) will have a throughput of 3000 IOPS. Update the EC2 launch template to allocate this type of volume.
- **C.** Create an Amazon EFS volume and mount it across all the EC2 instances. Use the Provisioned Throughput mode on the EFS volume to ensure that the application can reach the required IOPS.
- **D.** Create an Amazon EFS volume and mount it across all the EC2 instances. Use Max I/O performance mode on the EFS volume to ensure the application can reach the required IOPS.

> **Bạn chọn:** B
> **Đáp án đúng:** C

### Giải thích

**Amazon Elastic File System (Amazon EFS)**  provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is built to scale on-demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth. Amazon EFS has a simple web services interface that allows you to create and configure file systems quickly and easily. The service manages all the file storage infrastructure for you, meaning that you can avoid the complexity of deploying, patching, and maintaining complex file system configurations.

![image](https://media.tutorialsdojo.com/sap_efs_how_it_works.png)

Amazon EFS is designed to provide the throughput, IOPS, and low latency needed for a broad range of workloads. With Amazon EFS, you can choose from two performance modes and two throughput modes:

– The default**General Purpose performance mode**  is ideal for latency-sensitive use cases, like web serving environments, content management systems, home directories, and general file serving. File systems in the **Max I/O mode**  can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for file metadata operations.

– Using the default **Bursting Throughput mode** , throughput scales as your file system grows. Using **Provisioned Throughput mode** , you can specify the throughput of your file system independent of the amount of data stored.

With Bursting Throughput mode, throughput on Amazon EFS scales as the size of your file system in the standard storage class grows. With Provisioned Throughput mode, you can instantly provision the throughput of your file system (in MiB/s) independent of the amount of data stored.

If your file system is in the Provisioned Throughput mode, you can increase the Provisioned Throughput of your file system as often as you want. You can decrease your file system throughput in Provisioned Throughput mode as long as it’s been more than 24 hours since the last decrease.

Hence, the correct answer is: **Create an Amazon EFS volume and mount it across all the EC2 instances. Use the Provisioned Throughput mode on the EFS volume to ensure that the application can reach the required IOPS.**

The option that says: **Create an Amazon EFS volume and mount it across all the EC2 instances. Use Max I/O performance mode on the EFS volume to ensure the application can reach the required IOPS**  is incorrect. File systems in the Max I/O mode can scale to higher levels of aggregate throughput and operations per second. However, this scaling is done with a tradeoff of slightly higher latencies for file metadata operations.

The option that says: **Use the cheaper General Purpose SSD (gp2) EBS volumes instead of PIOPS EBS volumes. Allocating 1TB EBS volumes (gp2) will have a throughput of 3000 IOPS. Update the EC2 launch template to allocate this type of volume**  is incorrect. Although this may look cheaper at first, creating several 1TB volumes for each EC2 instance entails higher costs. The Amazon EFS volume solution will be cheaper for sharing storage across all EC2 instances. Although you can use EBS Multi-Attach to attach EBS volumes to multiple EC2 instances, this is limited only to Provisioned IOPS SSD (io1 or io2 Block Express) volumes that are attached to Nitro-based EC2 instances in the same Availability Zone.

The option that says: **Remove the PIOPS EBS volume allocation on the EC2 launch template. Attach a 120GB instance store volume on the EC2 instance to ensure that the application will have enough IOPS for its operation**  is incorrect. Instance store volumes are ephemeral which means that you will typically lose all data in the volume when you stop/start the instance. This is not recommended for this mission-critical application.

**References:**

[https://docs.aws.amazon.com/efs/latest/ug/performance.html](https://docs.aws.amazon.com/efs/latest/ug/performance.html)

[https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)

**Check out these Amazon EFS and Comparison Cheat Sheets:**

[https://tutorialsdojo.com/amazon-efs/](https://tutorialsdojo.com/amazon-efs/)

[https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/](https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/)

---

## Câu 52 — ✅ ĐÚNG

### Câu hỏi

A leading media company in the country is building a voting system for a popular singing competition show on national TV. The viewers who watch the performances can visit the company’s dynamic website to vote for their favorite singer. After the show has finished, it is expected that the site will receive millions of visitors who would like to cast their votes. Web visitors should log in using their social media accounts and then submit their votes. The webpage will display the winner after the show, as well as the vote total for each singer. The solutions architect is tasked to build the voting site and ensure that it can handle the rapid influx of incoming traffic in the most cost-effective way possible.

Which of the following architecture should you use to meet the requirement?

### Các phương án

- **A.** Use a CloudFront web distribution and an Application Load Balancer in front of an Auto Scaling group of EC2 instances. Use Amazon Cognito for user authentication. The web servers will process the user's vote and pass the result in an SQS queue. Set up an IAM Role to grant the EC2 instances permissions to write to the SQS queue. A group of EC2 instances will then retrieve and process the items from the queue. Finally, store the results in a DynamoDB table.
- **B.** Use a CloudFront web distribution and an Application Load balancer in front of an Auto Scaling group of EC2 instances. The servers will first authenticate the user using IAM and then process the user's vote which will then be stored to RDS.
- **C.** Use a CloudFront web distribution and an Application Load Balancer in front of an Auto Scaling group of EC2 instances. Develop a custom authentication service using STS and AssumeRoleWithSAML API. The servers will process the user's vote and store the result in a DynamoDB table.
- **D.** Use a CloudFront web distribution and deploy the website using S3 hosting feature. Write a custom NodeJS application to authenticate the user using STS and AssumeRole API. Setup an IAM Role to grant permission to store the user's vote to a DynamoDB table.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

For User authentication, you can use **Amazon Cognito** . To host the static assets of the website, you can use CloudFront. Considering that there would be millions of voters and data to be stored, it is best to use DynamoDB which can automatically scale.

![image](https://media.tutorialsdojo.com/sap_cognito_identity_pool.png)

Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0.

Therefore, the correct answer is: **Use a CloudFront web distribution and an Application Load Balancer in front of an Auto Scaling group of EC2 instances. Use Amazon Cognito for user authentication. The web servers will process the user’s vote and pass the result in an SQS queue. Set up an IAM Role to grant the EC2 instances permissions to write to the SQS queue. A group of EC2 instances will then retrieve and process the items from the queue. Finally, store the results in a DynamoDB table.**

The option that says: **Use a CloudFront web distribution and an Application Load balancer in front of an Auto Scaling group of EC2 instances. The servers will first authenticate the user using IAM and then process the user’s vote which will then be stored to RDS**  is incorrect. By default, you can’t use IAM alone to set up social media account registration to your website. You have to use Amazon Cognito. It is also more suitable to use DynamoDB instead of an RDS database since this is only a simple voting application that doesn’t warrant a complex table relationship. DynamoDB is a fully managed database that automatically scales, unlike RDS. It can store and accommodate millions of data from the users who cast their votes more effectively than RDS.

The option that says:**Use a CloudFront web distribution and deploy the website using S3 hosting feature. Write a custom NodeJS application to authenticate the user using STS and AssumeRole API. Setup an IAM Role to grant permission to store the user’s vote to a DynamoDB table**  is incorrect. The `AssumeRole` API is not suitable for user authentication that uses a web identity provider such as Amazon Cognito, Login with Amazon, Facebook, Google, or any social media identity provider. You can use the AssumeRoleWithWebIdentity API or better yet, Amazon Cognito instead.

The option that says: **Use a CloudFront web distribution and an Application Load Balancer in front of an Auto Scaling group of EC2 instances. Develop a custom authentication service using STS and AssumeRoleWithSAML API. The servers will process the user’s vote and store the result in a DynamoDB table**  is incorrect. The `AssumeRoleWithSAML` API is primarily used for SAML 2.0-based federation and for social media user registration.

**References:**

[https://aws.amazon.com/cognito/](https://aws.amazon.com/cognito/)

[https://aws.amazon.com/cloudfront/](https://aws.amazon.com/cloudfront/)

[https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html)

**Check out these Amazon Cognito Cheat Sheets:**

[https://tutorialsdojo.com/amazon-cognito/](https://tutorialsdojo.com/amazon-cognito/)

[https://tutorialsdojo.com/amazon-cognito-user-pools-and-identity-pools-explained/](https://tutorialsdojo.com/amazon-cognito-user-pools-and-identity-pools-explained/)

---

## Câu 53 — ✅ ĐÚNG

### Câu hỏi

A retail company has an online shopping website that provides cheap bargains and discounts on various products. The company has recently moved its infrastructure from its previous hosting provider to AWS. The architecture uses an Application Load Balancer (ALB) in front of an Auto Scaling group of Spot and On-Demand EC2 instances. The solutions architect must set up a CloudFront web distribution that uses a custom domain name and the origin should point to the new ALB.

Which of the following options is the correct implementation of an end-to-end HTTPS connection from the origin to the CloudFront viewers?

### Các phương án

- **A.** Import a certificate that is signed by a trusted third-party certificate authority, store it to ACM then attach it in your ALB. Set the Viewer Protocol Policy to HTTPS Only in CloudFront and use an SSL/TLS certificate from a third-party certificate authority which was imported to either ACM or the IAM certificate store.
- **B.** Use a certificate that is signed by a trusted third-party certificate authority in the ALB, which is then imported into ACM. Set the Viewer Protocol Policy to HTTPS Only in CloudFront, then use an SSL/TLS certificate from a third-party certificate authority which was imported to S3.
- **C.** Upload a self-signed certificate in the ALB. Set the Viewer Protocol Policy to `HTTPS Only` in CloudFront and use an SSL/TLS certificate from a third-party certificate authority which was imported to either ACM or the IAM certificate store.
- **D.** Use a certificate that is signed by a trusted third-party certificate authority in the ALB, which is then imported into ACM. Set the Viewer Protocol Policy to Match Viewer to support both HTTP or HTTPS in CloudFront then use an SSL/TLS certificate from a third-party certificate authority which was imported to either ACM or the IAM certificate store.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Remember that there are rules on which type of SSL Certificate to use if you are using an EC2 or an ELB as your origin. This question is about setting up an end-to-end HTTPS connection between the Viewers, CloudFront, and your custom origin, which is an ALB instance.

The certificate issuer you must use depends on whether you want to require HTTPS between viewers and CloudFront or between CloudFront and your origin:

**HTTPS between viewers and CloudFront**

– You can use a certificate that was issued by a trusted certificate authority (CA) such as Comodo, DigiCert, Symantec or other third-party providers.

– You can use a certificate provided by AWS Certificate Manager (ACM)

**HTTPS between CloudFront and a custom origin**

– If the origin is not an ELB load balancer, such as Amazon EC2, the certificate must be issued by a trusted CA such as Comodo, DigiCert, Symantec or other third-party providers.

– If your origin is an ELB load balancer, you can also use a certificate provided by ACM.

![image](https://media.tutorialsdojo.com/sap_cloudfront_ssl.jpg)

If you’re using your own domain name, such as tutorialsdojo.com, you need to change several CloudFront settings. You also need to use an SSL/TLS certificate provided by AWS Certificate Manager (ACM), or import a certificate from a third-party certificate authority into ACM or the IAM certificate store. Lastly, you should set the Viewer Protocol Policy to HTTPS Only in CloudFront.

Hence, the option that says: **Import a certificate that is signed by a trusted third-party certificate authority, store it to ACM then attach it in your ALB. Set the Viewer Protocol Policy to HTTPS Only in CloudFront and use an SSL/TLS certificate from a third-party certificate authority which was imported to either ACM or the IAM certificate store**  is the correct answer in this scenario.

The option that says: **Upload a self-signed certificate in the ALB. Set the Viewer Protocol Policy to `HTTPS only` in CloudFront and use an SSL/TLS certificate from a third-party certificate authority which was imported to either ACM or the IAM certificate store**  is incorrect because you cannot directly upload a self-signed certificate in your ALB.

The option that says: **Use a certificate that is signed by a trusted third-party certificate authority in the ALB, which is then imported into ACM. Set the Viewer Protocol Policy to Match Viewer to support both HTTP or HTTPS in CloudFront then use an SSL/TLS certificate from a third-party certificate authority which was imported to either ACM or the IAM certificate store**  is incorrect because you have to set the Viewer Protocol Policy to `HTTPS Only`.

The option that says: **Use a certificate that is signed by a trusted third-party certificate authority in the ALB, which is then imported into ACM. Set the Viewer Protocol Policy to HTTPS Only in CloudFront, then use an SSL/TLS certificate from a third-party certificate authority which was imported to S3** is incorrect because you cannot use an SSL/TLS certificate from a third-party certificate authority which was imported to S3.

**References:**

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html)

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html)

**Check out this Amazon CloudFront Cheat Sheet:**

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

---

## Câu 54 — ❌ SAI

### Câu hỏi

A pharmaceutical company has a hybrid cloud architecture in AWS. It has three different accounts for its environments: DEV, UAT, and PROD, which are all part of the consolidated billing account. The PROD account has purchased 10 Amazon EC2 Reserved Instances in the us-west-2a Availability Zone using the `ec2:PurchaseReservedInstancesOffering` and `ec2:ModifyReservedInstances` API actions.

Currently, there are no running EC2 instances in the PROD account because the application is not live yet. However, in the DEV account, there are 5 EC2 instances running in the us-west-2a Availability Zone. In the UAT account, there are also 5 EC2 instances running in the us-west-1a Availability Zone. All the EC2 instances in the DEV and UAT accounts match the reserved instance type in the PROD account.

In this scenario, which account benefits the most from the Reserved Instance pricing?

### Các phương án

- **A.** None. Considering that the PROD account is the one that purchased the Reserved Instance and it does not have any running EC2 instance, there is currently no other member account that benefits from the Reserved Instance pricing.
- **B.** Currently, only the DEV account benefits from the Reserved Pricing.
- **C.** Currently, only the UAT account benefits from the Reserved Pricing.
- **D.** Since both DEV and UAT accounts are running an EC2 instance type that exactly matches the Reserved Instance type, then the Reserved instance pricing will be applied to all EC2 instances in those two member accounts.

> **Bạn chọn:** A
> **Đáp án đúng:** B

### Giải thích

In the question, DEV and UAT are running the same instance type, but the main difference is that the former is using us-west-2a Availability Zone while the latter uses us-west-1a. Remember that the PROD account has bought the Reserved Instance in the us-west-2a Availability Zone, which means that only the DEV account exactly matches the criteria.

As an **Amazon EC2 Reserved Instance** s example, suppose that Bob and Susan each have an account in an organization. Susan has five Reserved Instances of the same type, and Bob has none. During one particular hour, Susan uses three instances, and Bob uses six, for a total of nine instances on the organization’s consolidated bill. AWS bills five instances as Reserved Instances and the remaining four instances as regular instances.

![image](https://media.tutorialsdojo.com/sap_reserved_instances_basic.png)

Bob receives the cost-benefit from Susan’s Reserved Instances only if he launches his instances in the same Availability Zone where Susan purchased her Reserved Instances. For example, if Susan specifies us-west-2a when she purchases her Reserved Instances, Bob must specify us-west-2a when he launches his instances to get the cost-benefit on the organization’s consolidated bill. However, the actual locations of Availability Zones are independent from one account to another. For example, the us-west-2a Availability Zone for Bob’s account might be in a different location than the location for Susan’s account.

Therefore, the correct answer is: **Currently, only the DEV account benefits from the Reserved Pricing.**

The option that says: **Currently, only the UAT account benefits from the Reserved Pricing**  is incorrect. The UAT account can only benefit from the Reserved Instances of the PROD account if they were launched in the same Availability Zone where the PROD account purchased the Reserved Instances.

The option that says: **Since both DEV and UAT accounts are running an EC2 instance type which exactly matches the Reserved Instance type, then the Reserved instance pricing will be applied to all EC2 instances in those two member accounts**  is incorrect. The UAT account can only benefit from the Reserved Instances of the PROD account if they were launched in the same Availability Zone where the PROD account purchased the Reserved Instances.

The option that says: **None. Considering that the PROD account is the one that purchased the Reserved Instance and it does not have any running EC2 instance, there is currently no other member account that benefits from the Reserved Instance pricing**  is incorrect. The DEV account primarily benefits from the Reserved Instances pricing because the instances are launched on the same AZ where the PROD account purchased the Reserved Instances.

**References:**

[https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

[https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidatedbilling-other.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidatedbilling-other.html)

**Check out this AWS Billing and Cost Management Cheat Sheet:**

[https://tutorialsdojo.com/aws-billing-and-cost-management/](https://tutorialsdojo.com/aws-billing-and-cost-management/)

---

## Câu 55 — ✅ ĐÚNG

### Câu hỏi

A data analytics company has recently adopted a hybrid cloud infrastructure with AWS. They are in the business of collecting and processing vast amounts of data. Each data set generates up to several thousands of files which can range from 10 MB to 1 GB in size. The archived data is rarely restored and in case there is a request to retrieve it, the company has a maximum of 24 hours to send the files. The data sets can be searched using its file ID, set name, authors, tags, and other criteria.

Which of the following options provides the most cost-effective architecture to meet the above requirements?

### Các phương án

- **A.** For each completed data set, compress and concatenate all of the files into a single Glacier archive. 2. Store the associated archive ID for the compressed files along with other search metadata in a DynamoDB table. 3. For retrieving the data, query the DynamoDB table for files that match the search criteria and then restore the files from the retrieved archive ID.
- **B.** Store the files of the completed data sets into a single S3 bucket. 2. Store the S3 object key for the compressed files along with other search metadata in a DynamoDB table. 3. For retrieving the data, query the DynamoDB table for files that match the search criteria and then restore the files from the S3 bucket.
- **C.** Store individually compressed files to an S3 bucket. Also, store the search metadata and the S3 object key of the files in a separate S3 bucket. 2. Create a lifecycle rule to move the data from an S3 Standard class to Glacier after a certain month. 3. For retrieving the data, query the S3 bucket for files matching the search criteria and then retrieve the file from the other S3 bucket.
- **D.** Store individual files in Glacier using the filename as the archive name. 2. For retrieving the data, query the Glacier vault for files matching the search criteria.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

You can further lower the cost of storing data by compressing it into a zip or tar file. In addition, searching for archives in Glacier takes a long time, which is why it is advisable to store the search criteria and archive ID in a database for faster searching.

![image](https://media.tutorialsdojo.com/sap_dynamodb_s3_glacier.png)

Hence, the correct answer in this scenario is:

**1. For each completed data set, compress and concatenate all of the files into a single Glacier archive.**

**2. Store the associated archive ID for the compressed files along with other search metadata in a DynamoDB table.**

**3. For retrieving the data, query the DynamoDB table for files that match the search criteria and then restore the files from the retrieved archive ID.**

The following option is incorrect because storing the data in the S3 Standard class is costly. It is typically more cost-effective to use Amazon Glacier instead.

**1. Store the files of the completed data sets into a single S3 bucket.**
 **2. Store the S3 object key for the compressed files along with other search metadata in a DynamoDB table.**
 **3. For retrieving the data, query the DynamoDB table for files that match the search criteria and then restore the files from the S3 bucket.**

The following option is incorrect because initially storing the archive in the S3 Standard class for a month still entails additional cost. Since the company allows a maximum of 24 hours to retrieve the files, you can directly store the archives in Glacier instead:

**1. Store individual compressed files to an S3 bucket. Also store the search metadata and the S3 object key of the files in a separate S3 bucket.**
 **2. Create a lifecycle rule to move the data from an S3 Standard class to Glacier after a certain a month.**
 **3. For retrieving the data, query the S3 bucket for files matching the search criteria and then retrieve the file from the other S3 bucket.**

The following option is incorrect because Glacier doesn’t have a built-in search function to help you retrieve the data. You have to primarily store the archive ID in a database, such as DynamoDB, to help you effectively search the required data:

**1. Store individual files in Glacier using the filename as the archive name.**
 **2. For retrieving the data, query the Glacier vault for files matching the search criteria.**

**References:**

[https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)

[https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html)

**Check out this Amazon S3 Glacier Cheat Sheet:**

[https://tutorialsdojo.com/amazon-glacier/](https://tutorialsdojo.com/amazon-glacier/)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 56 — ❌ SAI

### Câu hỏi

A large media company based in Los Angeles, California, operates a MySQL RDS instance within an AWS VPC. The company has a custom analytics application running in its on-premises data center that requires read-only access to the database. The company aims to replicate the data from the MySQL RDS instance in AWS to a MySQL instance located on-premises to serve as the read-only endpoint for this analytics application.

Which of the following options is the most secure way of performing this replication?

### Các phương án

- **A.** RDS cannot replicate to an on-premises database server. Instead, configure the RDS instance to replicate to an EC2 instance with core MySQL and then configure replication over a secure VPN/VPG connection.
- **B.** Create a Data Pipeline that exports the MySQL data each night and securely downloads the data from an S3 HTTPS endpoint. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication.
- **C.** Configure the RDS instance as the master and enable replication over the open Internet using an SSL endpoint to the on-premises server. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication.
- **D.** Create an IPSec VPN connection using either OpenVPN or VPN/VGW through the Virtual Private Cloud service. Prepare an instance of MySQL running external to Amazon RDS. Configure the MySQL RDS instance to be the replication source. Use `mysqldump` to transfer the database from the Amazon RDS instance to the on-premises MySQL instance and start the replication from the Amazon RDS Read Replica.

> **Bạn chọn:** A
> **Đáp án đúng:** D

### Giải thích

Amazon supports **Internet Protocol security (IPsec) VPN**  connections. IPsec is a protocol suite for securing Internet Protocol (IP) communications by authenticating and encrypting each IP packet of a data stream. Data transferred between your VPC and datacenter routes over an encrypted VPN connection to help maintain the confidentiality and integrity of data in transit. An Internet gateway is not required to establish a hardware VPN connection.

You can set up replication between an **Amazon RDS MySQL**  (or MariaDB DB instance) that is running in AWS and a MySQL (or MariaDB instance) to your on-premises data center. A read replica is a read-only copy of a MySQL database instance that is kept synchronized with the source instance. Read replicas can be used to offload read traffic from the primary instance, improving performance and scalability.

![image](https://media.tutorialsdojo.com/public/td-RDS-replication-On-premise-05-Aug-2024.png)

To allow communication between RDS and to your on-premises network, you must first set up a VPN or an AWS *Direct Connect*  connection. Once that is done, just follow the below steps to perform the replication:

- Set up a MySQL database server in the on-premises environment, which will act as the read replica for the RDS instance.

- Configure the RDS MySQL instance as the replication source (master) for the on-premises MySQL instance.

- Use the **`mysqldump`**  utility to transfer the initial data from the Amazon RDS instance to the on-premises MySQL instance. This step is necessary to establish the initial replication state.

- After the initial data transfer, start the replication process from the on-premises MySQL instance, which will act as a read replica of the Amazon RDS instance.

By following this approach, the data replication traffic between the RDS instance and the on-premises MySQL server is securely transmitted over the IPSec VPN connection, ensuring the confidentiality and integrity of the data during transit, rather than exposing the RDS instance directly to the internet or using less secure methods for data transfer.

Hence, the correct answer is **Create an IPSec VPN connection using either OpenVPN or VPN/VGW through the Virtual Private Cloud service. Prepare an instance of MySQL running external to Amazon RDS. Configure the MySQL RDS instance to be the replication source. Use `mysqldump` to transfer the database from the Amazon RDS instance to the on-premises MySQL instance and start the replication from the Amazon RDS Read Replica** because it is feasible to set up the secure IPSec VPN connection between the on-premises server and AWS VPC using the VPN/Gateways.

The option that says: **Configure the RDS instance as the master and enable replication over the open Internet using an SSL endpoint to the on-premises server. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication**  is incorrect because SSL endpoint cannot be utilized here as it is only used to securely access the database.

The option that says: **RDS cannot replicate to an on-premises database server. Instead, configure the RDS instance to replicate to an EC2 instance with core MySQL and then configure replication over a secure VPN/VPG connection**  is incorrect because you do not need to establish a secure VPN/VPG connection in the first place as EC2 and RDS are both in AWS Cloud.

The option that says: **Create a Data Pipeline that exports the MySQL data each night and securely downloads the data from an S3 HTTPS endpoint. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication**  is incorrect because Data Pipeline is primarily for batch jobs and is not suitable for this scenario.

**References:**

[https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Exporting.NonRDSRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Exporting.NonRDSRepl.html)

**Check out these Amazon RDS and Amazon VPC Cheat Sheets:**

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 57 — ❌ SAI

### Câu hỏi

A company launched a high-performance computing (HPC) application inside the VPC of its AWS account. The application is composed of hundreds of private EC2 instances running in a cluster placement group, which allows the instances to communicate with each other at network speeds of up to 10 Gbps. There is also a custom cluster controller EC2 instance that closely controls and monitors the system performance of each instance. The cluster controller has the same instance type and AMI as the other instances. It is configured with a public IP address and runs outside the placement group. The Solutions Architect has been tasked to improve the network performance between the controller instance and the EC2 instances in the placement group.

Which option provides the MOST suitable solution that the Architect must implement to satisfy the requirement while maintaining low-latency network performance?

### Các phương án

- **A.** Terminate the custom cluster controller instance and re-launch it to the existing placement group. Attach an Elastic Network Adapter (ENA) to the cluster controller instance to increase its network performance. Change the placement strategy of the placement group to `Spread`.
- **B.** Terminate the custom cluster controller EC2 instance and stop all of the running instances in the existing placement group. Move the cluster controller instance to the existing placement group and restart all of the instances.
- **C.** Stop the custom cluster controller instance and move it to the existing placement group.
- **D.** Attach an Elastic IP address to the custom cluster controller instance to increase its network capability to 10 Gbps.

> **Bạn chọn:** B
> **Đáp án đúng:** C

### Giải thích

Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput, or both. They are also recommended when the majority of the network traffic is between the instances in the group. To provide the lowest latency and the highest packet-per-second network performance for your placement group, choose an instance type that supports enhanced networking.

![image](https://media.tutorialsdojo.com/sap_az1_placement_group.png)

A spread placement group is a group of instances that are each placed on distinct racks, with each rack having its own network and power source. Spread placement groups are recommended for applications that have a small number of critical instances that should be kept separate from each other. Launching instances in a spread placement group reduces the risk of simultaneous failures that might occur when instances share the same racks. Spread placement groups provide access to distinct racks, and are therefore suitable for mixing instance types or launching instances over time.

![image](https://media.tutorialsdojo.com/sap_az1_placement_group_instances.png)

You can change the placement group for an instance in any of the following ways:

- Move an existing instance to a placement group

- Move an instance from one placement group to another

- Remove an instance from a placement group

Before you move or remove the instance, the instance must be in the stopped state. You can move or remove an instance using the AWS CLI or an AWS SDK.

Hence, the correct answer is: **Stop the custom cluster controller instance and move it to the existing placement group.**

The option that says: **Terminate the custom cluster controller EC2 instance and stop all of the running instances in the existing placement group. Move the cluster controller instance to the existing placement group and restart all of the instances**  is incorrect because you don’t need to restart or terminate any instance to move a new EC2 instance to an existing placement group. You just have to stop the cluster controller instance, move it to the placement group, and restart it.

The option that says:**Attach an Elastic IP address to the custom cluster controller instance to increase its network capability to 10 Gbps**  is incorrect because an Elastic IP is simply a static IPv4 address designed for dynamic cloud computing. It doesn’t increase the network bandwidth of the instance to 10 Gbps either.

The option that says: **Terminate the custom cluster controller instance and re-launch it to the existing placement group. Attach an Elastic Network Adapter (ENA) to the cluster controller instance to increase its network performance. Change the placement strategy of the placement group to `Spread`**  is incorrect because using a Spread placement group will degrade the existing network performance of the architecture. The use of a Cluster placement group must be maintained. And while it is true that the Elastic Network Adapter (ENA) can increase the instance network performance, the described process of moving the custom cluster controller instance to the placement group is still incorrect. You can just stop the instance and directly include it to the placement group. There is no need to terminate the EC2 instance.

**References:**

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)

**Check out this Amazon EC2 Cheat Sheet:**

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

---

## Câu 58 — ❌ SAI

### Câu hỏi

A multinational investment bank has multiple cloud architectures across the globe. The company has a VPC in the US East region for their East Coast office and another VPC in the US West for their West Coast office. There is a requirement to establish a low latency, high-bandwidth connection between their on-premises data center in Texas and both of their VPCs in AWS.

Which of the following options should the solutions architect implement to achieve the requirement in a cost-effective manner?

### Các phương án

- **A.** Establish a Direct Connect connection between the VPC in US East region to the on-premise data center in Texas and then establish another Direct Connect connection between the VPC in US West region to the on-premises data center.
- **B.** Set up two separate VPC peering connections for the two VPCs and for the on-premises data center.
- **C.** Set up an AWS VPN managed connection between the VPC in US East region and the on-premises data center in Texas.
- **D.** Set up an AWS Direct Connect Gateway with two virtual private gateways.

> **Bạn chọn:** A
> **Đáp án đúng:** D

### Giải thích

You can use an **AWS Direct Connect gateway**  to connect your AWS Direct Connect connection over a private virtual interface to one or more VPCs in your account that are located in the same or different regions. You associate a Direct Connect gateway with the virtual private gateway for the VPC, and then create a private virtual interface for your AWS Direct Connect connection to the Direct Connect gateway. You can attach multiple private virtual interfaces to your Direct Connect gateway. A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any public region and access it from all other public regions.

![image](https://media.tutorialsdojo.com/sap_directconnect_gateway.png)

Hence, the correct answer is:**Set up an AWS Direct Connect Gateway with two virtual private gateways. Create the required Private Virtual Interfaces to the Direct Connect Gateway.**

The option that says: **Establish a Direct Connect connection between the VPC in US East region and the on-premises data center in Texas, and then establish another Direct Connect connection between the VPC in US West region and the on-premises data center**  is incorrect because establishing two separate Direct Connect connections is expensive and hence, not a cost-effective option. It is better to establish a Direct Connect gateway instead which uses one Direct Connect connection to integrate the 2 VPCs and the on-premises data center.

**Setting up an AWS VPN managed connection between the VPC in US East region and the on-premises data center in Texas**  is incorrect because a VPN Connection is a more suitable solution for low to modest bandwidth requirements which can tolerate the inherent variability in Internet-based connectivity.

**Setting up two separate VPC peering connections for the two VPCs and for the on-premises data center**  is incorrect because VPC Peering is used to connect 2 VPC’s together and not to connect your on-premises data center.

**References:**

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html)

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html)

**Check out this AWS Direct Connect Cheat Sheet:**

[https://tutorialsdojo.com/aws-direct-connect/](https://tutorialsdojo.com/aws-direct-connect/)

---

## Câu 59 — ✅ ĐÚNG

### Câu hỏi

A company has a suite of IBM products in its on-premises data centers, such as IBM WebSphere, IBM MQ, and IBM DB2 servers. The solutions architect has been tasked to migrate all of the current systems to the AWS Cloud in the most cost-effective way and improve the availability of the cloud infrastructure.

Which of the following options is the MOST suitable solution that the solutions architect should implement to meet the company’s requirements?

### Các phương án

- **A.** Use the AWS Application Migration Service to migrate your servers to AWS. Upload the IBM licenses to AWS License Manager and use the licenses when configuring Amazon EC2 instances to re-host your IBM WebSphere and IBM DB2 servers separately. Re-host and migrate the IBM MQ service to Amazon MQ.
- **B.** Use the AWS Application Migration Service to migrate your servers to AWS. Set up Amazon EC2 instances to re-host your IBM WebSphere and IBM DB2 servers separately. Re-host and migrate the IBM MQ service to Amazon SQS Standard Queue.
- **C.** Use the AWS Database Migration Service (DMS) and the AWS Schema Conversion Tool (SCT) to convert, re-architect, and migrate the IBM Db2 database to Amazon Aurora. Set up an Auto Scaling group of EC2 instances with an ELB in front to migrate and re-host your IBM WebSphere. Re-host and migrate the IBM MQ service to Amazon SQS FIFO Queue.
- **D.** Use the AWS Database Migration Service (DMS) and the AWS Schema Conversion Tool (SCT) to convert, migrate, and re-architect the IBM Db2 database to Amazon Aurora. Set up an Auto Scaling group of EC2 instances with an ELB in front to migrate and re-host your IBM WebSphere. Migrate and re-platform IBM MQ to Amazon MQ in a phased approach.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

On Amazon EC2, you can run many of the proven IBM technologies with which you’re already familiar. You may be eligible to bring many of your own IBM software and licenses (BYOSL) to run on Amazon EC2 instances.

![image](https://media.tutorialsdojo.com/sap_ibm_byol_infra.png)

**AWS Database Migration Service (DMS)**  and the **AWS Schema Conversion Tool (SCT)**  can allow you to convert and migrate IBM Db2 databases on Linux, UNIX, and Windows (Db2 LUW) to any DMS-supported target. This can accelerate your move to the cloud by allowing you to migrate more of your legacy databases. The new Db2 LUW source adds to the existing list of the relational database, NoSQL, and object store sources supported by DMS. If the database migration target is Amazon Aurora, Amazon Redshift, or Amazon DynamoDB, you can use DMS free for six months.

![image](https://media.tutorialsdojo.com/sap_ibmmq_infra.png)

**Amazon MQ**  is a managed message broker service from AWS that makes it easy to set up and operate message brokers in the cloud. To migrate and re-platform your on-premises IBM MQ to Amazon MQ, you can opt for a phased approach for the migration process. You can move the producers (senders) and consumers (receivers) in phases from your on-premises to the cloud. This process uses Amazon MQ as the message broker and decommissions IBM MQ once all producers/consumers have been successfully migrated.

Hence, the correct option is: **Use the AWS Database Migration Service (DMS) and the AWS Schema Conversion Tool (SCT) to convert, migrate and re-architect the IBM Db2 database to Amazon Aurora. Set up an Auto Scaling group of EC2 instances with an ELB in front to migrate and re-host your IBM WebSphere. Migrate and re-platform IBM MQ to Amazon MQ in phased approach.**

The option that says: **Use the AWS Application Migration Service to migrate your servers to AWS. Set up Amazon EC2 instances to re-host your IBM WebSphere and IBM DB2 servers separately. Re-host and migrate the IBM MQ service to Amazon SQS Standard Queue**  is incorrect because the AWS Application Migration Service simply automates the migration of your on-premises virtual machines to the AWS Cloud. Moreover, you can’t re-host and migrate your IBM MQ service to Amazon SQS. A better solution is to re-platform IBM MQ to Amazon MQ.

The option that says:**Use the AWS Application Migration Service to migrate your servers to AWS. Upload the IBM licenses to AWS License Manager and use the licenses when configuring Amazon EC2 instances to re-host your IBM WebSphere and IBM DB2 servers separately. Re-host and migrate the IBM MQ service to Amazon MQ** is incorrect because the AWS Application Migration Service simply automates the migration of your on-premises virtual machines to the AWS Cloud. AWS License Manager is used to create customized licensing rules that emulate the terms of their licensing agreements and then enforce these rules. It is not used for storing software licenses. This service is limited to migrating virtual machines (VMs) and in addition, you cannot directly re-host and migrate your IBM MQ to Amazon MQ since these are two completely different systems. Instead, you have to re-platform IBM MQ to Amazon MQ in a phased approach.

The option that says: **Use the AWS Database Migration Service (DMS) and the AWS Schema Conversion Tool (SCT) to convert, re-architect and migrate the IBM Db2 database to Amazon Aurora. Set up an Auto Scaling group of EC2 instances with an ELB in front to migrate and re-host your IBM WebSphere. Re-host and migrate the IBM MQ service to Amazon SQS FIFO Queue**  is incorrect. Although the use of AWS Database Migration Service (DMS) and the AWS Schema Conversion Tool (SCT) is correct, the migration process for your IBM MQ is wrong. Amazon Simple Queue Service (SQS) is just a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. There are a lot of features in IBM MQ that are not available in Amazon SQS, whether it is a Standard or a FIFO Queue. You have to re-platform IBM MQ to Amazon MQ instead.

**References:**

[https://aws.amazon.com/quickstart/architecture/ibm-websphere-liberty/](https://aws.amazon.com/quickstart/architecture/ibm-websphere-liberty/)

[https://aws.amazon.com/about-aws/whats-new/2018/04/aws-dms-supports-ibm-db2-as-a-source/](https://aws.amazon.com/about-aws/whats-new/2018/04/aws-dms-supports-ibm-db2-as-a-source/)

[https://aws.amazon.com/quickstart/architecture/ibm-mq/](https://aws.amazon.com/quickstart/architecture/ibm-mq/)

[https://developer.ibm.com/messaging/2018/09/26/ibm-mq-available-managed-service-aws/](https://developer.ibm.com/messaging/2018/09/26/ibm-mq-available-managed-service-aws/)

[https://aws.amazon.com/blogs/compute/migrating-from-ibm-mq-to-amazon-mq-using-a-phased-approach](https://aws.amazon.com/blogs/compute/migrating-from-ibm-mq-to-amazon-mq-using-a-phased-approach)

**Check out these cheat sheets on AWS Database Migration Service and AWS Application Migration Service:**

[https://tutorialsdojo.com/aws-database-migration-service/](https://tutorialsdojo.com/aws-database-migration-service/)

[https://tutorialsdojo.com/aws-application-migration-service/](https://tutorialsdojo.com/aws-application-migration-service/)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 60 — ✅ ĐÚNG

### Câu hỏi

An AWS Partner company hosts all its infrastructure on the AWS cloud. All resources are currently deployed in the us-east-1 region. The company plans to expand its business to include deployments in Europe and Asia. The solutions architect has been tasked to provision the needed resources on multiple regions across multiple AWS accounts under the company’s AWS Organization.

Which of the following options is the recommended solution to meet the company requirements?

### Các phương án

- **A.** Write infrastructure-as-code to maintain consistency. Create nested stacks with AWS CloudFormation templates and use global parameters to specify which target region and accounts to provision the needed resources.
- **B.** Write infrastructure-as-code to maintain consistency. Create AWS CloudFormation templates and create IAM policies to control multiple accounts. Use regional parameters when deploying CloudFormation templates across multiple regions to provision the needed resources.
- **C.** Use AWS Organizations to centrally manage the deployment of AWS CloudFormation template from the central account. Use AWS Control Tower as an orchestration layer deploying resources across multiple accounts and regions.
- **D.** Write infrastructure-as-code to maintain consistency. Use AWS Organizations to centrally orchestrate the deployment of AWS CloudFormation template from the central account. Use CloudFormation StackSets to simplify permissions and automatic provisioning of resources across multiple regions and accounts.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

**AWS CloudFormation StackSets**  allow you to roll out CloudFormation stacks over multiple AWS accounts and in multiple Regions with just a couple of clicks. With AWS Organizations, you can centrally manage multiple AWS accounts across diverse business needs including billing, access control, compliance, security and resource sharing.

Using **AWS Organizations**  you can centrally orchestrate any AWS CloudFormation enabled service across multiple AWS accounts and regions. For example, you can deploy your centralized AWS Identity and Access Management (IAM) roles, provision Amazon Elastic Compute Cloud (Amazon EC2) instances or AWS Lambda functions across AWS Regions and accounts in your organization. CloudFormation StackSets simplify the configuration of cross-accounts permissions and allow for automatic creation and deletion of resources when accounts are joining or are removed from your Organization.

You can get started by enabling data sharing between CloudFormation and Organizations from the StackSets console. Once done, you will be able to use StackSets in the Organizations master account to deploy stacks to all accounts in your organization or in specific organizational units (OUs).

![image](https://media.tutorialsdojo.com/sap_cloudformation_aws_organizations.png)

Therefore, the correct answer is: **Write infrastructure-as-code to maintain consistency. Use AWS Organizations to centrally orchestrate the deployment of AWS CloudFormation template from the central account. Use CloudFormation StackSets to simplify permissions and automatic provisioning of resources across multiple regions and accounts.**  With AWS Organizations, you can centrally orchestrate any AWS CloudFormation enabled service across multiple AWS accounts and regions.

The option that says: **Write infrastructure-as-code to maintain consistency. Create AWS CloudFormation templates and create IAM policies to control multiple accounts. Use regional parameters when deploying CloudFormation templates across multiple regions to provision the needed resources**  is incorrect. This is not recommended as it entails more operational overhead. It is recommended to use CloudFormation StackSets to deploy stack across multiple regions and accounts in a single operation.

The option that says: **Use AWS Organizations to centrally manage the deployment of AWS CloudFormation template from the central account. Use AWS Control Tower as an orchestration layer deploying resources across multiple accounts and regions**  is incorrect. It is possible to use AWS Control Tower as an orchestration layer for multi-account environments. However, for this solution to work, you still need to create CloudFormation StackSets for deployment on multiple regions.

The option that says: **Write infrastructure-as-code to maintain consistency. Create nested stacks with AWS CloudFormation templates and use global parameters to specify which target region and accounts to provision the needed resources**  is incorrect. This is not possible, if you want to deploy CloudFormation stacks on multiple regions and accounts in a single operation, you should use CloudFormation StackSets.

**References:**

[https://aws.amazon.com/blogs/aws/new-use-aws-cloudformation-stacksets-for-multiple-accounts-in-an-aws-organization/](https://aws.amazon.com/blogs/aws/new-use-aws-cloudformation-stacksets-for-multiple-accounts-in-an-aws-organization/)

[https://aws.amazon.com/blogs/aws/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/](https://aws.amazon.com/blogs/aws/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/)

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

**Check out these AWS Organizations and AWS CloudFormation Sheet:**

[https://tutorialsdojo.com/aws-organizations/](https://tutorialsdojo.com/aws-organizations/)

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

---

## Câu 61 — ✅ ĐÚNG

### Câu hỏi

A company has performed a security audit on its existing application. It was determined that the application retrieves the Amazon RDS for MySQL credentials from an encrypted file in an Amazon S3 bucket. To improve the security of the application the following should be implemented on the next application deployment:

- The database credentials must be randomly generated and stored in a secure AWS managed service.

- The credentials must be rotated every 90 days.

- Infrastructure-as-code provisioning of application resources using AWS CloudFormation.

- For the application deployment, the solutions architect will create a CloudFormation template.

Which of the following options should the solutions architect implement to meet the company’s requirement with the LEAST amount of operational overhead?

### Các phương án

- **A.** Use AWS Secrets Manager, create a secret resource and generate a secure database password. Use Secrets Manager’s managed rotation to automatically rotate the database password every 90 days. On AWS CloudFormation, specify the `AutomaticallyAfterDays` property in `RotationRules` to set the rotation schedule to 90 days.
- **B.** Using AWS Secrets Manager, create a secret resource and generate a secure database password. Write an AWS Lambda function to rotate the database password. Create a scheduled rule on Amazon EventBridge to trigger the Lambda function to rotate the database password every 90 days.
- **C.** On Systems Manager Parameter Store, create a SecureString parameter and generate a secure database password. On AWS CloudFormation, create an AWS KMS resource to rotate the database password every 90 days.
- **D.** On Systems Manager Parameter Store, create a SecureString parameter and generate a secure database password. Write an AWS Lambda function to rotate the database password. On AWS CloudFormation, specify a resource for Parameter Store `RotationSchedule` to rotate the password every 90 days.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

**AWS Secrets Manager**  enables you to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. This helps ensure the secret can’t be compromised by someone examining your code because the secret no longer exists in the code. Also, you can configure Secrets Manager to automatically rotate the secret for you according to a specified schedule. This enables you to replace long-term secrets with short-term ones, significantly reducing the risk of compromise.

The following diagram illustrates the most basic scenario. It shows that you can store credentials for a database in Secrets Manager and then use those credentials in an application to access the database.

![image](https://media.tutorialsdojo.com/sap_secrets_manager_how.png)

- The database administrator creates a set of credentials on the Personnel database for use by an application called MyCustomApp. The administrator also configures those credentials with the permissions required for the application to access the Personnel database.

- The database administrator stores the credentials as a secret in Secrets Manager named MyCustomAppCreds. Then, Secrets Manager encrypts and stores the credentials within the secret as the *protected secret text* .

- When MyCustomApp accesses the database, the application queries Secrets Manager for the secret named MyCustomAppCreds.

- Secrets Manager retrieves the secret, decrypts the protected secret text, and returns the secret to the client app over a secured (HTTPS with TLS) channel.

- The client application parses the credentials, connection string, and any other required information from the response and then uses the information to access the database server.

![image](https://media.tutorialsdojo.com/aws-cloudformation-aws-rotationschedule.jpg)

**Amazon RDS**  offers managed rotation through **AWS Secrets Manager** , which does not require writing a custom Lambda function. On **AWS CloudFormation**  template, the `**AWS::SecretsManager::RotationSchedule** ` can be used to set the rotation schedule for a secret.

In the given scenario, the correct property to use for setting the rotation schedule in AWS Secrets Manager is **`AutomaticallyAfterDays`** . This property specifies the number of days between automatically scheduled rotations of the secret, which aligns with the requirement to rotate the credentials every 90 days.

Hence, the correct answer is: **Use AWS Secrets Manager, create a secret resource and generate a secure database password. Use Secrets Manager’s managed rotation to automatically rotate the database password every 90 days. On AWS CloudFormation, specify the `AutomaticallyAfterDays` property in `RotationRules` to set the rotation schedule to 90 days.** This option leverages AWS Secrets Manager’s managed rotation, which simplifies the process and reduces operational overhead by not requiring a custom Lambda function for rotation.

The option that says: **On Systems Manager Parameter Store, create a SecureString parameter and generate a secure database password. Write an AWS Lambda function to rotate the database password. On AWS CloudFormation, specify a resource for Parameter Store `RotationSchedule` to rotate the password every 90 days**  is incorrect. There is no Systems Manager Parameter Store RotationSchedule resource on AWS CloudFormation.

The option that says: **Use AWS Secrets Manager, create a secret resource and generate a secure database password. Write an AWS Lambda function to rotate the database password. Create a scheduled rule on Amazon EventBridge to trigger the Lambda function to rotate the database password every 90 days**  is incorrect. This option may be possible. However, it does not use AWS CloudFormation in its solution. Additionally, for RDS services covered by Secrets Manager’s managed rotation, creating a scheduled rule on EventBridge to trigger a Lambda function is just unnecessary.

The option that says: **On Systems Manager Parameter Store, create a SecureString parameter and generate a secure database password. On AWS CloudFormation, create an AWS KMS resource to rotate the database password every 90 days**  is incorrect. AWS KMS can automatically rotate keys that are stored only on KMS, not parameters stored in the Systems Manager Parameter Store.

**References:**

[https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

[https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html)

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html#cfn-secretsmanager-rotationschedule-rotationrules-automaticallyafterdays](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html#cfn-secretsmanager-rotationschedule-rotationrules-automaticallyafterdays)

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html)

**Check out these AWS Secrets Manager and AWS CloudFormation Cheat Sheets:**

[https://tutorialsdojo.com/aws-secrets-manager/](https://tutorialsdojo.com/aws-secrets-manager/)

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

**AWS Secrets Manager and Systems Manager Parameter Store comparison:**

[https://tutorialsdojo.com/aws-secrets-manager-vs-systems-manager-parameter-store/](https://tutorialsdojo.com/aws-secrets-manager-vs-systems-manager-parameter-store/)

---

## Câu 62 — ❌ SAI

### Câu hỏi

A privately funded aerospace and sub-orbital spaceflight services company hosts its rapidly evolving applications in AWS. For its deployment process, the company is using CloudFormation templates which are regularly updated to map the latest AMI IDs for its Amazon EC2 instances clusters. It takes a lot of time to execute this on a regular basis which is why the solutions architect has been instructed to automate this process.

Which of the following options is the most suitable solution that can satisfy the above requirements?

### Các phương án

- **A.** Use CloudFormation with AWS Service Catalog to fetch the latest AMI IDs and automatically use them for succeeding deployments.
- **B.** Use a combination of AWS Service Catalog with AWS Config to automatically fetch the latest AMI and use it for succeeding deployments.
- **C.** Use CloudFormation with Systems Manager Parameter Store to retrieve the latest AMI IDs for your template. Whenever you decide to update the EC2 instances, call the update-stack API in CloudFormation in your CloudFormation template.
- **D.** Configure your Systems Manager State Manager to store the latest AMI IDs and integrate them with your CloudFormation template. Call the update-stack API in CloudFormation whenever you decide to update the EC2 instances in your CloudFormation template.

> **Bạn chọn:** A
> **Đáp án đúng:** C

### Giải thích

You can use the existing **Parameters**  section of your **CloudFormation template**  to define Systems Manager parameters, along with other parameters. Systems Manager parameters are a unique type that is different from existing parameters because they refer to actual values in the Parameter Store. The value for this type of parameter would be the Systems Manager (SSM) parameter key instead of a string or other value. CloudFormation will fetch values stored against these keys in Systems Manager in your account and use them for the current stack operation.

If the parameter being referenced in the template does not exist in Systems Manager, a synchronous validation error is thrown. Also, if you have defined any parameter value validations (AllowedValues, AllowedPattern, etc.) for Systems Manager parameters, they will be performed against SSM keys which are given as input values for template parameters, not actual values stored in Systems Manager.

![image](https://media.tutorialsdojo.com/sap_cloudformation_parameter_store.png)

Parameters stored in Systems Manager are mutable. Any time you use a template containing Systems Manager parameters to create/update your stacks, CloudFormation uses the values for these Systems Manager parameters at the time of the create/update operation. So, as parameters are updated in Systems Manager, you can have the new value of the parameter take effect by just executing a stack update operation. The [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html) section in the output for Describe API will show an additional ‘ResolvedValue’ field that contains the resolved value of the Systems Manager parameter that was used for the last stack operation.

Hence, the correct answer is the option that says: **Use CloudFormation with Systems Manager Parameter Store to retrieve the latest AMI IDs for your template. Whenever you decide to update the EC2 instances, call the update-stack API in CloudFormation in your CloudFormation template.**

The option that says: **Configure your Systems Manager State Manager to store the latest AMI IDs and integrate them with your CloudFormation template. Call the update-stack API in CloudFormation whenever you decide to update the EC2 instances in your CloudFormation template**  is incorrect because the Systems Manager State Manager service simply automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define. This can’t be used as a parameter store that refers to the latest AMI of your application.

The following options are incorrect because using AWS Service Catalog is not suitable in this scenario. This service just allows organizations to create and manage catalogs of IT services that are approved for use on AWS:

**– Use a combination of AWS Service Catalog with AWS Config to automatically fetch the latest AMI and use it for succeeding deployments.**

**– Use CloudFormation with AWS Service Catalog to fetch the latest AMI IDs and automatically use them for succeeding deployments.**

**References:**

[https://aws.amazon.com/blogs/mt/integrating-aws-cloudformation-with-aws-systems-manager-parameter-store/](https://aws.amazon.com/blogs/mt/integrating-aws-cloudformation-with-aws-systems-manager-parameter-store/)

[https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

**Check out this AWS Systems Manager Cheat Sheet:**

[https://tutorialsdojo.com/aws-systems-manager/](https://tutorialsdojo.com/aws-systems-manager/)

---

## Câu 63 — ❌ SAI

### Câu hỏi

A company has a large collection of user-submitted stock photos. An AWS Lambda function processes and extracts metadata from these photos to make a searchable catalog. The metadata is extracted depending on several rules and the output is sent to an Amazon ElastiCache for Redis cluster. The metadata extraction is done in several batches and the whole process takes about 45 minutes to complete. Whenever there is a change in the metadata extraction rules, the update process is triggered manually before the extraction process starts. As the stock photo submissions are steadily growing, the company wants to reduce the metadata extraction time for its catalog.

Which of the following options should the Solutions Architect implement to reduce the time for the metadata extraction process?

### Các phương án

- **A.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Create another workflow that will retrieve the list of photos for processing and execute the metadata extraction workflow for each photo.
- **B.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Configure all the Lambda extraction functions to subscribe to this SQS queue with higher batch size.
- **C.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Associate the Lambda functions to an AWS Batch compute environment. Write another Lambda function that will retrieve the list of photos for processing and send each item to the job queue in the AWS Batch compute environment.
- **D.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Set this SQS queue as the input for the Step Functions workflow.

> **Bạn chọn:** D
> **Đáp án đúng:** A

### Giải thích

**AWS Step Functions**  can be used to run a serverless workflow that coordinates multiple AWS Lambda functions. AWS Step Functions is a serverless function orchestrator that makes it easy to sequence AWS Lambda functions and multiple AWS services into business-critical applications. Through its visual interface, you can create and run a series of checkpointed and event-driven workflows that maintain the application state. The output of one step acts as an input to the next. Each step in your application executes in order, as defined by your business logic.

**AWS Lambda**  is a serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes. With Lambda, you can run code for virtually any type of application or backend service – all with zero administration. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic.

![image](https://media.tutorialsdojo.com/sap_step_function_lambda_function.JPG)

In this scenario, you can quickly make changes to the whole process depending on the extraction rules if you have dedicated Lambda functions for each type of metadata. Technically, you can create one Lambda function to call the other Lambda metadata extraction functions. However, it is quite challenging to orchestrate the data flow of the Lambda functions as the number of functions grow. Plus, any change in the flow of the application will require changes in multiple places, and you could end up writing the same code over and over again.

To solve this challenge, you can use AWS Step Functions. This is a serverless orchestration service that lets you easily coordinate multiple Lambda functions into flexible workflows that are easy to debug and easy to change. Step Functions will keep your Lambda functions free of additional logic by triggering and tracking each step of your application for you.

Therefore, the correct answer is: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Create another workflow that will retrieve the list of photos for processing and execute the metadata extraction workflow for each photo.**

The option that says: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Associate the Lambda functions to an AWS Batch compute environment. Write another Lambda function that will retrieve the list of photos for processing and send each item to the job queue in the AWS Batch compute environment**  is incorrect. AWS Batch only adds complexity to the solution. AWS Batch is designed to easily and efficiently run hundreds of thousands of batch computing jobs on AWS but not with Lambda functions.

The option that says: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Set this SQS queue as the input for the Step Functions workflow**  is incorrect. This might be possible if you have a Lambda Function that consumes the messages on the SQS and feeds them to the Step Function, which is not explicitly stated on this option. An SQS queue cannot be used as a direct input for an AWS Step Function workflow.

The option that says: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Configure all the Lambda extraction functions to subscribe to this SQS queue with higher batch size**  is incorrect. This may be possible but it will not work for this scenario. When a Lambda function processes the photo for a specific type of metadata, it will become invisible on the queue, and other Lambda functions will not be able to process the same photo. This defeats the purpose of multiple Lambda functions that are supposed to process the photo in parallel.

**References:**

[https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/](https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/)

[https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html](https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html)

[https://aws.amazon.com/blogs/aws/new-step-functions-support-for-dynamic-parallelism/](https://aws.amazon.com/blogs/aws/new-step-functions-support-for-dynamic-parallelism/)

[https://aws.amazon.com/step-functions/use-cases/](https://aws.amazon.com/step-functions/use-cases/)

**Check out the AWS Step Functions Cheat Sheet:**

[https://tutorialsdojo.com/aws-step-functions/](https://tutorialsdojo.com/aws-step-functions/)

---

## Câu 64 — ❌ SAI

### Câu hỏi

A data analytics company is running a Redshift data warehouse for one of its major clients. In compliance with the Business Continuity Program of the client, they need to provide a Recovery Point Objective of 24 hours and a Recovery Time Objective of 1 hour. The data warehouse should be available even in the event that the entire AWS Region is down.

Which of the following is the most suitable configuration for this scenario?

### Các phương án

- **A.** Configure Redshift to use Cross-Region Replication (CRR) and in case of system failure, failover to the backup region and manually copy the snapshot from the primary region to the secondary region.
- **B.** Configure Redshift to have automatic snapshots and do a cross-region snapshot copy to automatically replicate the current production cluster to the disaster recovery region.
- **C.** Enable Redshift replication from the cluster running in the primary region to the cluster running in the secondary region. Change the DNS endpoint to the secondary cluster's primary node in case of system failures in the primary region.
- **D.** No additional configuration needed. Redshift is configured with automatic snapshot by default.

> **Bạn chọn:** C
> **Đáp án đúng:** B

### Giải thích

When automated snapshots are enabled for a cluster, **Amazon Redshift**  periodically takes snapshots of that cluster, usually every eight hours or following every 5 GB per node of data changes, or whichever comes first. Automated snapshots are enabled by default when you create a cluster. These snapshots are deleted at the end of a retention period. The default retention period is one day, but you can modify it by using the Amazon Redshift console or programmatically by using the Amazon Redshift API.

When you enable Amazon Redshift to automatically copy snapshots to another region, you specify the destination region where you want snapshots to be copied. In the case of automated snapshots, you can also specify the retention period that they should be kept in the destination region. After an automated snapshot is copied to the destination region and it reaches the retention time period there, it is deleted from the destination region, keeping your snapshot usage low. You can change this retention period if you need to keep the automated snapshots for a shorter or longer period of time in the destination region.

![image](https://media.tutorialsdojo.com/sap_redshift_snapshot.png)

Therefore the correct answer is: **Configure Redshift to have automatic snapshots and do a cross-region snapshot copy to automatically replicate the current production cluster to the disaster recovery region.**  The automatic snapshots feature is automatically enabled by default. You can then configure Amazon Redshift to automatically copy snapshots (automated or manual) for a cluster to another AWS Region.

The option that says: **Configure Redshift to use Cross-Region Replication (CRR) and in case of system failure, failover to the backup region and manually copy the snapshot from the primary region to the secondary region**  is incorrect. Amazon Redshift only has cross-region backup feature (using snapshots), not Cross-Region Replication.

The option that says: **Enable Redshift replication from the cluster running in the primary region to the cluster running in the secondary region. Change the DNS endpoint to the secondary cluster’s primary node in case of system failures in the primary region**  is incorrect. Amazon Redshift only has cross-region backup feature (using snapshots); it can’t replicate directly to another cluster in another region.

The option that says: **No additional configuration needed. Redshift is configured with automatic snapshot by default**  is incorrect. Even though the automatic snapshots feature is enabled by default, cross-region snapshot copy is not.

**References:**

[https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html)

**Check out this Amazon Redshift Cheat Sheet:**

[https://tutorialsdojo.com/amazon-redshift/](https://tutorialsdojo.com/amazon-redshift/)

---

## Câu 65 — ❌ SAI

### Câu hỏi

A company has an on-premises data center that is hosting its gaming service. Its primary function is player-matching and is accessible from players around the world. The gaming service prioritizes network speed for the users so all traffic to the servers uses User Datagram Protocol (UDP). As more players join, the company is having difficulty scaling its infrastructure so it plans to migrate the service to the AWS cloud. The Solutions Architect has been tasked with the migration and AWS Shield Advanced has been enabled already to protect all public-facing resources.

Which of the following actions should the Solutions Architect implement to achieve the company requirements? (Select TWO.)

### Các phương án

- **A.** Place the Auto Scaling of Amazon EC2 instances behind an Internet-facing Application Load Balancer (ALB). For the domain name, create an Amazon Route 53 entry that is Aliased to the FQDN of the ALB.
- **B.** Set up network ACL rules on the VPC to deny all non-UDP traffic. Ensure that the NACL is associated with the load balancer subnets.
- **C.** Place the Auto Scaling of Amazon EC2 instances behind a Network Load Balancer (NLB). For the domain name, create an Amazon Route 53 entry that points to the Elastic IP address of the NLB.
- **D.** Create an AWS WAF rule that will explicitly block all non-UDP traffic. Ensure that the AWS WAF rule is associated with the load balancer of the EC2 instances.
- **E.** Create an Amazon CloudFront distribution and set the Load Balancer as the origin. Use only secure protocols on the distribution origin settings.

> **Bạn chọn:** C, E
> **Đáp án đúng:** B, C

### Giải thích

A**Network Load Balancer**  operates at the connection level (Layer 4), routing connections to targets (Amazon EC2 instances, microservices, and containers) within Amazon VPC based on IP protocol data. Ideal for load balancing of both TCP and UDP traffic, Network Load Balancer is capable of handling millions of requests per second while maintaining ultra-low latencies. Network Load Balancer is optimized to handle sudden and volatile traffic patterns while using a single static IP address per Availability Zone.

For UDP traffic, the load balancer selects a target using a flow hash algorithm based on the protocol, source IP address, source port, destination IP address, and destination port. A UDP flow has the same source and destination, so it is consistently routed to a single target throughout its lifetime. Different UDP flows have different source IP addresses and ports so that they can be routed to different targets.

![image](https://media.tutorialsdojo.com/sap_nlb_ec2_backend.png)

When you create **Network Access Control Lists (NACLs)** , you can specify both allow and deny rules. This is useful if you want to explicitly deny certain types of traffic to your application. For example, you can define IP addresses (as CIDR ranges), protocols, and destination ports that are denied access to the entire subnet. If your application is used only for TCP traffic, you can create a rule to deny all UDP traffic or vice versa. This option is useful when responding to DDoS attacks because it lets you create your own rules to mitigate the attack when you know the source IPs or other signatures.

![image](https://media.tutorialsdojo.com/sap_nacl_subnet.png)

If you are subscribed to AWS Shield Advanced, you can register Elastic IPs (EIPs) as Protected Resources. DDoS attacks against EIPs that have been registered as Protected Resources are detected more quickly, which can result in a faster time to mitigate.

The option that says: **Place the Auto Scaling of Amazon EC2 instances behind a Network Load Balancer (NLB). For the domain name, create an Amazon Route 53 entry that points to the Elastic IP address of the NLB**  is correct. The service uses UDP traffic and prioritizes network speed, so a Network Load Balancer is ideal for this scenario. You can create a Route 53 entry pointing to the NLB’s Elastic IP.

The option that says: **Set up network ACL rules on the VPC to deny all non-UDP traffic. Ensure that the NACL is associated with the load balancer subnets**  is correct. Since all traffic to the servers is UDP, you can set NACL to block all non-UDP traffic which can help block attacks such as traffic coming from TCP connections.

The option that says: **Place the Auto Scaling of Amazon EC2 instances behind an internet-facing Application Load Balancer (ALB). For the domain name, create an Amazon Route 53 entry that is Aliased to the FQDN of the ALB** is incorrect. UDP traffic operates at Layer 4 of the OSI model while an ALB operates at Layer 7. A Network Load Balancer is a better fit for this scenario.

The option that says: **Create an AWS WAF rule that will explicitly block all non-UDP traffic. Ensure that the AWS WAF rule is associated with the load balancer of the EC2 instances**  is incorrect. AWS WAF rules cannot protect a Network Load Balancer yet. It is better to use NACL rules to block the non-UDP traffic.

The option that says: **Create an Amazon CloudFront distribution and set the Load Balancer as the origin. Use only secure protocols on the distribution origin settings**  is incorrect. Although CloudFront does provide caching and security settings for the origin, it helps mitigate DDoS attacks to your instances or NLBs because AWS Shield Standard is enabled by default. For more advanced DDoS mitigation AWS Shield Advanced offers integration with NACLs that will block traffic at the edge of the AWS Network.

**References:**

[https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/security-groups-and-network-access-control-lists-nacls-bp5.html](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/security-groups-and-network-access-control-lists-nacls-bp5.html)

[https://aws.amazon.com/blogs/security/now-you-can-use-aws-shield-advanced-to-protect-your-amazon-ec2-instances-and-network-load-balancers/](https://aws.amazon.com/blogs/security/now-you-can-use-aws-shield-advanced-to-protect-your-amazon-ec2-instances-and-network-load-balancers/)

[https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)

**Check out these Application Load Balancer and AWS Shield Cheat Sheets:**

[https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-classic-load-balancer/](https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-classic-load-balancer/)

[https://tutorialsdojo.com/aws-shield/](https://tutorialsdojo.com/aws-shield/)

---

## Câu 66 — ❌ SAI

### Câu hỏi

A legal consulting firm is running a WordPress website on EC2 instances deployed across multiple Availability Zones with a Multi-AZ RDS MySQL database instance. Their website is designed to use an eventual consistency model and performs a high number of read and write operations. There is a growing number of people who are reporting that the website is slow and after checking, the root cause is due to the slow read processing in your database tier. The current DB instances are already optimized for the firm’s operational budget, with considerations for cost-effectiveness and resource utilization.

Which of the following options could solve this issue? (Select THREE.)

### Các phương án

- **A.** Add an RDS MySQL Read Replica in each Availability Zone.
- **B.** Deploy an Amazon ElastiCache Cluster with nodes running in each Availability Zone.
- **C.** Integrate Amazon CloudFront to the website to deliver the static media assets to the viewers faster. Consider using AWS Compute Optimizer to rightsize your fleet of Amazon EC2 instances.
- **D.** Implement sharding to distribute the incoming load to multiple RDS MySQL instances.
- **E.** Upgrade the instance type of the RDS MySQL database instance to a larger type.
- **F.** Upgrade the RDS MySQL instance to use provisioned IOPS.

> **Bạn chọn:** A, B, F
> **Đáp án đúng:** A, B, D

### Giải thích

To improve the read performance of the application, you can use RDS Read Replicas and ElastiCache.

**Amazon ElastiCache**  is a web service that makes it easy to deploy, operate, and scale an in-memory data store or cache in the cloud. The service improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory data stores instead of relying entirely on slower disk-based databases.

![image](https://media.tutorialsdojo.com/sap_rds_elasticache.JPG)

**Amazon RDS Read Replicas**  provide enhanced performance and durability for database (DB) instances. This replication feature makes it easy to elastically scale out beyond the capacity constraints of a single DB Instance for read-heavy database workloads. You can create one or more replicas of a given source DB Instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput.

**Database sharding**  is the process of storing a large database across multiple machines. A single machine, or database server, can store and process only a limited amount of data. Database sharding overcomes this limitation by splitting data into smaller chunks, called shards, and storing them across several database servers. All database servers usually have the same underlying technologies, and they work together to store and process large volumes of data.

The option that says: **Add an RDS MySQL Read Replica in each Availability Zone**  is correct. This improves the database retrieval time as there will be more nodes that can serve the database request. You won’t need to increase the master instance size to accommodate all the read loads.

The option that says: **Deploy an Amazon ElastiCache Cluster with nodes running in each Availability Zone**  is correct. Adding a cache will significantly reduce the retrieval time for frequent database queries. This also reduces the load significantly on the database tier.

The option that says: **Implement sharding to distribute the incoming load to multiple RDS MySQL instances**  is correct. You can use Amazon RDS as the building block a sharded architecture. Sharding allows you to split your current instances into smaller ones that could operate more efficiently. It would also provide horizontal scalability, which can be more cost-effective in the long term compared to simply upgrading to a larger DB instance.

The option that says: **Upgrade the RDS MySQL instance to use provisioned IOPS**  is incorrect. This provides an increase in IOPS for the database tier, however, this is also very expensive to implement since provisioned IOPS costs a lot more.

The option that says: **Integrate Amazon CloudFront to the website to deliver the static media assets to the viewers faster. Consider using AWS Compute Optimizer to rightsize your fleet of Amazon EC2 instances**  is incorrect. Amazon CloudFront simply caches content at the edge. It can be a complementary solution for overall performance improvement but would not directly impact the database layer where the bottleneck is occuring.

The option that says: **Upgrade the instance type of the RDS MySQL database instance to a larger type** is incorrect. While this may improve the overall performance of the database, it’s costly and may exceed the operational budget. This approach is an example of vertical scaling, which has limits and may not be as sustainable as horizontal scaling solutions in the long run.

**References:**

[https://aws.amazon.com/elasticache/](https://aws.amazon.com/elasticache/)

[https://aws.amazon.com/rds/details/read-replicas/](https://aws.amazon.com/rds/details/read-replicas/)

[https://aws.amazon.com/what-is/database-sharding/](https://aws.amazon.com/what-is/database-sharding/)

[https://aws.amazon.com/blogs/database/sharding-with-amazon-relational-database-service/](https://aws.amazon.com/blogs/database/sharding-with-amazon-relational-database-service/)

**Check out these Amazon Elasticache and Amazon RDS Cheat Sheet:**

[https://tutorialsdojo.com/amazon-elasticache/](https://tutorialsdojo.com/amazon-elasticache/)

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

---

## Câu 67 — ✅ ĐÚNG

### Câu hỏi

A company’s cloud governance team is tightening its AWS policies for an upcoming audit. During an initial review, the team found IAM policies attached to Lambda function execution roles, granting full access to S3 buckets and DynamoDB tables. As a best practice, the team recommends implementing the principle of least privilege access for compliance with the security audit.

What steps should be taken to determine the minimum access needed by each function with the LEAST amount of effort? (Select TWO.)

### Các phương án

- **A.** Create a trail in AWS CloudTrail and turn on CloudTrail logging to capture Amazon S3 and Amazon DynamoDB events.
- **B.** Enable CloudTrail logging in the AWS account and export the logs to S3. Use Amazon GuardDuty to analyze the data and monitor unauthorized access to Amazon S3 and Amazon DynamoDB. Restrict access in IAM.
- **C.** Set up AWS Audit Manager to continuously audit AWS usage. Review the findings and create IAM access policies to provide more restrictive permissions for the Lambda functions.
- **D.** Use IAM Access Analyzer to review AWS CloudTrail logs and generate a policy template with permissions required by the Lambda functions.
- **E.** Build an inventory of AWS API Calls by applying the CodeGuru Profiler function decorator to Lambda’s handler functions. Export this data to a CSV file. Create a generic access policy for each Lambda function and apply the update to the functions using a Python script.

> **Bạn chọn:** A, D
> **Đáp án đúng:** A, D

### Giải thích

AWS CloudTrail is an AWS service that helps enable operational and risk auditing, governance, and compliance of your AWS account. It provides three ways to record events: event history, CloudTrail Lake, and Trails. Trails capture a record of AWS activities and store them in an Amazon S3 bucket. These events can be integrated into security monitoring solutions for further analysis.

IAM Access Analyzer can analyze your CloudTrail events to identify actions and services used by an IAM entity (user or role). Based on that activity, you can generate an IAM policy. You can refine an entity’s permissions when you replace a broad permissions policy attached to the entity with the generated policy.

![image](https://media.tutorialsdojo.com/public/CloudTrailPolicy.jpg)

To start logging API activities for Amazon S3 and DynamoDB, you must first set up a CloudTrail trail. Once API activities are captured in the CloudTrail log, you can use the IAM Access Analyzer to generate IAM access policy templates for a specific date range from the events logged. After creating these policies, you can review the actions and services and customize them based on your needs.

Therefore, the correct answers are:

**– Create a trail in AWS CloudTrail and turn on CloudTrail logging to capture Amazon S3 and Amazon DynamoDB events.**

**– Use IAM Access Analyzer to review AWS CloudTrail logs and generate a policy template with permissions required by the Lambda functions.**

The option that says: **Enable CloudTrail logging in the AWS account and export the logs to S3. Use Amazon GuardDuty to analyze the data and monitor unauthorized access to Amazon S3 and Amazon DynamoDB. Restrict access in IAM**  is incorrect. While enabling the use of Amazon GuardDuty can help identify potential security threats, it does not directly help identify the minimum access needed by the Lambda functions. Amazon GuardDuty is more of a threat detection service.

The option that says: **Set up AWS Audit Manager to continuously audit AWS usage. Review the findings and create IAM access policies to provide more restrictive permissions for the Lambda functions**  is incorrect. AWS Audit Manager facilitates continuous AWS usage auditing to simplify risk management and ensure compliance with regulations and industry standards. While it can identify non-compliant resources, it does not provide insights into the minimum access needed by the Lambda functions. It aids more in overall compliance than granular access to AWS services.

The option that says: **Build an inventory of AWS API Calls by applying the CodeGuru Profiler function decorator to Lambda’s handler functions. Export this data to a CSV file. Create a generic access policy for each Lambda function and apply the update to the functions using a Python script** is incorrect. AWS CodeGuru Profiler can be integrated with AWS Lambda, but the insights that it provides is more on improving function performance and reducing costs by identifying expensive lines of code and anomalies. It won’t be helpful in determining the minimum access needed by the Lambda functions.

**References:**

[https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-genation.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)

[https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)

**Check out this AWS IAM Cheat Sheet:**

[https://tutorialsdojo.com/aws-identity-and-access-management-iam](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 68 — ✅ ĐÚNG

### Câu hỏi

A leading insurance company in South East Asia recently deployed a new web portal that enables your users to log in and manage their accounts, view their insurance plans, and pay their monthly premiums. After a few weeks, the solutions architect noticed that there is a significant amount of incoming traffic from a country in which the insurance company does not operate. Later on, it was determined that the same set of IP addresses coming from the unsupported country is sending out massive amounts of requests to your portal which has caused some performance issues on the application.

Which of the following options is the recommended solution to block the series of attacks coming from a set of determined IP ranges?

### Các phương án

- **A.** Create an inbound Network Access control list associated with explicit deny rules to block the attacking IP addresses.
- **B.** Launch the online portal on the private subnet.
- **C.** Launch a Security Group with explicit deny rules to block the attacking IP addresses.
- **D.** Create a custom route table associated with the web tier and block the attacking IP addresses from the Internet Gateway.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.

The following are the basic things that you need to know about network ACLs:

– Your VPC automatically comes with a modifiable default network ACL. By default, it allows all inbound and outbound IPv4 traffic and, if applicable, IPv6 traffic.

– You can create a custom network ACL and associate it with a subnet. By default, each custom network ACL denies all inbound and outbound traffic until you add rules.

– Each subnet in your VPC must be associated with a network ACL. If you don’t explicitly associate a subnet with a network ACL, the subnet is automatically associated with the default network ACL.

– You can associate a network ACL with multiple subnets. However, a subnet can be associated with only one network ACL at a time. When you associate a network ACL with a subnet, the previous association is removed.

– A network ACL contains a numbered list of rules. We evaluate the rules in order, starting with the lowest numbered rule, to determine whether traffic is allowed in or out of any subnet associated with the network ACL. The highest number that you can use for a rule is 32766. We recommend that you start by creating rules in increments (for example, increments of 10 or 100) so that you can insert new rules where you need to later on.

– A network ACL has separate inbound and outbound rules, and each rule can either allow or deny traffic.

– Network ACLs are stateless, which means that responses from allow inbound traffic are subject to the rules for outbound traffic (and vice versa).

The required task is to block all of the offending IP addresses from the unsupported country. In order to do this, you have to use Network Access Control List (NACL).

![image](https://media.tutorialsdojo.com/sap_nacls_subnet_example.png)

Therefore, the correct answer is: **Create an inbound Network Access control list associated with explicit deny rules to block the attacking IP addresses.**

The option that says: **Launch the online portal on the private subnet**  is incorrect because if you launch the online portal on the private subnet, then it will not be accessible to the users over the public Internet anymore.

The option that says: **Create a custom route table associated with the web tier and blocking the attacking IP addresses from the Internet Gateway**  is incorrect because you do not have to change the route table nor make any changes to the Internet Gateway (IGW).

The option that says: **Launch a Security Group with explicit deny rules to block the attacking IP addresses**  is incorrect because you cannot explicitly deny or block IP addresses using a security group.

**References:**

[https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html)

[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

**Check out this Amazon VPC Cheat Sheet:**

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

**Check out this security group and network access list comparison:**

[https://tutorialsdojo.com/security-group-vs-nacl/](https://tutorialsdojo.com/security-group-vs-nacl/)

---

## Câu 69 — ✅ ĐÚNG

### Câu hỏi

A company runs hundreds of Amazon EC2 instances inside an Amazon VPC. Whenever an EC2 error is encountered, the solutions architect performs manual steps in order to regain access to the impaired instance. The management wants to automatically recover impaired EC2 instances in the VPC. The goal is to automatically fix an instance that has become unreachable due to network misconfigurations, RDP issues, firewall settings, and many others to meet the compliance requirements.

Which of the following options is the most suitable solution that the solutions architect should implement to meet the above requirements?

### Các phương án

- **A.** Use the EC2Rescue tool to diagnose and troubleshoot problems on your Amazon EC2 Linux and Windows Server instances. Run the tool automatically by using AWS Lambda and a custom script.
- **B.** To meet the compliance requirements, use a combination of AWS Config and the AWS Systems Manager Session Manager to self-diagnose and troubleshoot problems on your EC2 Linux and Windows Server instances. Automate the recovery process by setting up a monitoring system using Amazon CloudWatch, AWS Lambda, and the AWS Systems Manager Run Command that will automatically monitor and recover impaired EC2 instances.
- **C.** To meet the compliance requirements, use a combination of AWS Config and the AWS Systems Manager State Manager to self-diagnose and troubleshoot problems on your Amazon EC2 Linux and Windows Server instances. Automate the recovery process by using AWS Systems Manager Maintenance Windows.
- **D.** Use the EC2Rescue tool to diagnose and troubleshoot problems on your EC2 Linux and Windows Server instances. Run the tool automatically by using the AWS Systems Manager Automation and the `AWSSupport-ExecuteEC2Rescue` document.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

**EC2Rescue**  can help you diagnose and troubleshoot problems on Amazon EC2 Linux and Windows Server instances. You can run the tool manually, or you can run the tool automatically by using Systems Manager Automation and the *AWSSupport-ExecuteEC2Rescue*  document. The *AWSSupport-ExecuteEC2Rescue* document is designed to perform a combination of Systems Manager actions, AWS CloudFormation actions, and Lambda functions that automate the steps normally required to use EC2Rescue.

**Systems Manager Automation**  simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. Automation enables you to do the following:

– Build Automation workflows to configure and manage instances and AWS resources.

– Create custom workflows or use pre-defined workflows maintained by AWS.

– Receive notifications about Automation tasks and workflows by using Amazon EventBridge.

– Monitor Automation progress and execution details by using the Amazon EC2 or the AWS Systems Manager console.

![image](https://media.tutorialsdojo.com/sap_aws_ssm_overview.png)

Therefore, the correct answer is: **Use the EC2Rescue tool to diagnose and troubleshoot problems on your EC2 Linux and Windows Server instances. Run the tool automatically by using the AWS Systems Manager Automation and the `AWSSupport-ExecuteEC2Rescue` document.**

The option that says: **To meet the compliance requirements, use a combination of AWS Config and the AWS Systems Manager State Manager to self-diagnose and troubleshoot problems on your EC2 Linux and Windows Server instances. Automate the recovery process by using AWS Systems Manager Maintenance Windows**  is incorrect. AWS Config is a service which is primarily used to assess, audit, and evaluate the configurations of your AWS resources but not to diagnose and troubleshoot problems in your EC2 instances. In addition, AWS Systems Manager State Manager is primarily used as a secure and scalable configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define but does not help you in troubleshooting your EC2 instances.

The option that says: **To meet the compliance requirements, use a combination of AWS Config and the AWS Systems Manager Session Manager to self-diagnose and troubleshoot problems on your EC2 Linux and Windows Server instances. Automate the recovery process by setting up a monitoring system using Amazon CloudWatch, AWS Lambda, and the AWS Systems Manager Run Command that will automatically monitor and recover impaired EC2 instances**  is incorrect. Just like the other option, AWS Config does not help you troubleshoot the problems in your EC2 instances. The AWS Systems Manager Sessions Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys for your EC2 instances, but it does not provide the capability of helping you diagnose and troubleshoot problems in your instance like what the EC2Rescue tool can do. In addition, setting up a CloudWatch, AWS Lambda, and the AWS Systems Manager Run Command that will automatically monitor and recover impaired EC2 instances is an operational overhead that can be easily done by using AWS Systems Manager Automation.

The option that says: **Use the EC2Rescue tool to diagnose and troubleshoot problems on your EC2 Linux and Windows Server instances. Run the tool automatically by using AWS Lambda and a custom script**  is incorrect because while it is technically possible to use AWS Lambda to automate the running of the EC2Rescue tool, this approach typically requires significant development effort to create and maintain the custom script. On the other hand, using the existing `AWSSupport-ExecuteEC2Rescue` automation document in AWS Systems Manager can be a more straightforward solution. This document, maintained by AWS, can be triggered automatically, reducing the need for custom scripting and the associated development and maintenance effort.

**References:**

[https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-ec2rescue.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-ec2rescue.html)

[https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)

**Check out this AWS Systems Manager Cheat Sheet:**

[https://tutorialsdojo.com/aws-systems-manager/](https://tutorialsdojo.com/aws-systems-manager/)

---

## Câu 70 — ✅ ĐÚNG

### Câu hỏi

An adventure company runs a PostgreSQL database that is used to store events from its monitoring application on its on-premises data center. The database is unable to scale enough to handle frequent write events that need to be ingested into the database. The management has tasked the solutions architect to create a hybrid solution that will utilize the existing company VPN connection to AWS. Additional requirements are as follows:

- Leverage AWS-managed services to minimize operation overhead

- Create a buffer that automatically scales to accommodate the events that need to be ingested

- A visualization tool to observe near real-time events and supports creating dashboards.

- Has support for dynamic schemas and semi-structured JSON data.

Which of the following options should the solutions architect implement to meet the company requirements? (Select TWO.)

### Các phương án

- **A.** Levering Amazon Neptune DB auto-scaling feature to reliably ingest the events. Use Neptune DB as the DB source for Amazon QuickSight to create near-real-time dashboards and visualizations.
- **B.** Ingest the events using Amazon Data Firehose. Write a Lambda function to process and transform the buffered events.
- **C.** Use Amazon Kinesis Data Stream to reliably ingest the events. Write a Lambda function to process and transform the buffered events.
- **D.** Provision an Amazon Aurora PostgreSQL DB cluster to reliably ingest the events. Use this DB as the source for Amazon QuickSight to create near-real-time dashboards and visualizations.
- **E.** Create an Amazon OpenSearch Service domain to reliably ingest the events. Leverage the OpenSearch Dashboards tool to create near-real-time dashboards and visualizations.

> **Bạn chọn:** B, E
> **Đáp án đúng:** B, E

### Giải thích

**Amazon Data Firehose**  is a fully managed service for delivering real-time streaming data to destinations such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, **Amazon OpenSearch Service** , Amazon OpenSearch Serverless, Splunk, and any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers. With Data Firehose, you don’t need to write applications or manage resources. You configure your data producers to send data to Data Firehose, and it automatically delivers the data to the destination that you specified. You can also configure Data Firehose to transform your data before delivering it.

**Amazon OpenSearch Service**  is a managed service that makes it easy to deploy, operate, and scale OpenSearch clusters in the AWS Cloud. Amazon OpenSearch Service supports OpenSearch and legacy Elasticsearch OSS (up to 7.10, the final open-source version of the software). When you create a cluster, you have the option of which search engine to use.

OpenSearch is a fully open-source search and analytics engine for use cases such as log analytics, real-time application monitoring, and clickstream analysis. **Amazon OpenSearch Service**  provisions all the resources for your cluster and launches it. It also automatically detects and replaces failed OpenSearch Service nodes, reducing the overhead associated with self-managed infrastructures.

![image](https://media.tutorialsdojo.com/sap_kinesis_elasticsearch.png)

**OpenSearch Dashboards**  is an open-source visualization tool designed to work with OpenSearch. Amazon OpenSearch Service provides an installation of OpenSearch Dashboards with every OpenSearch Service domain. You can find a link to Dashboards on your domain dashboard on the OpenSearch Service console.

Hence, the correct answers are:

**– Ingest the events using Amazon Data Firehose. Write a Lambda function to process and transform the buffered events.**

**– Create an Amazon OpenSearch Service domain to reliably ingest the events. Leverage the OpenSearch Dashboards tool to create near-real-time dashboards and visualizations.**

The option that says: **Levering Amazon Neptune DB auto-scaling feature to reliably ingest the events. Use Neptune DB as the DB source for Amazon QuickSight to create near-real-time dashboards and visualizations**  is incorrect. Neptune DB is designed for graph application and loading CSV formatted data. Amazon QuickSight can directly use Neptune DB as a source.

The option that says: **Provision an Amazon Aurora PostgreSQL DB cluster to reliably ingest the events. Use this DB as the source for Amazon QuickSight to create near-real-time dashboards and visualizations**  is incorrect. Amazon Aurora PostgreSQL may not be suited for ingesting semi-structured JSON or data with dynamic schemas. You will need to use a data transformer before ingesting to PostgreSQL database.

The option that says: **Use Amazon Kinesis Data Stream to reliably ingest the events. Write a Lambda function to process and transform the buffered events**  is incorrect. This may be possible, but since you are going to use Kinesis as a buffer, you don’t need the longer-term, durable storage offered by Kinesis Data Stream. Amazon Data Firehose has a feature to buffer data and supports data transformation in near-real-time.

**References:**

[https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)

[https://aws.amazon.com/blogs/big-data/ingest-streaming-data-into-amazon-elasticsearch-service-within-the-privacy-of-your-vpc-with-amazon-kinesis-data-firehose/](https://aws.amazon.com/blogs/big-data/ingest-streaming-data-into-amazon-elasticsearch-service-within-the-privacy-of-your-vpc-with-amazon-kinesis-data-firehose/)

[https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html)

**Check out these Amazon Kinesis and Amazon OpenSearch Cheat Sheets:**

[https://tutorialsdojo.com/amazon-kinesis/](https://tutorialsdojo.com/amazon-kinesis/)

[https://tutorialsdojo.com/amazon-opensearch-service/](https://tutorialsdojo.com/amazon-opensearch-service/)

---

## Câu 71 — ✅ ĐÚNG

### Câu hỏi

A digital advertising startup runs an ad-supported photo-sharing website that has users around the globe. The startup is using Amazon S3 to serve photos to website users. Several weeks later, the solutions architect found out that third-party sites have been linking to the photos on the company S3 bucket which is causing losses in overall financial ad revenue. Some users are also reporting that the photos are taking too much time to load.

Which of the following options is an effective method to mitigate this security flaw and to improve the performance of the photo-sharing website?

### Các phương án

- **A.** Use CloudFront to distribute static content and block the IP addresses of the other websites that are illegally linking the photos to their own websites.
- **B.** Remove public read access from the S3 bucket. Use CloudFront as the global content delivery network (CDN) service for the photos and use Signed URLs with expiry dates.
- **C.** Store photos on an EBS volume of the web server with data encryption enabled.
- **D.** Block the IPs of the offending websites in Security Groups and use S3 Cross-Region Replication (CRR).

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

**Amazon CloudFront**  is a global content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to your viewers with low latency and high transfer speeds. CloudFront is integrated with AWS – including physical locations that are directly connected to the AWS global infrastructure, as well as software that works seamlessly with services including AWS Shield for DDoS mitigation, Amazon S3, Elastic Load Balancing or Amazon EC2 as origins for your applications, and Lambda@Edge to run custom code close to your viewers.

![image](https://media.tutorialsdojo.com/sap_cloudfront_oia.png)

A signed URL includes additional information, for example, expiration date and time, that gives you more control over access to your content. These additional information appear in a policy statement, which is based on either a canned policy or a custom policy.

In this scenario, the main issue is that there are other websites that are illegally using the photos hosted from your S3 bucket. The secondary issue is the slow loading times of the photos. The use of CloudFront as a CDN with Signed URLs is the best solution for this situation.

Therefore, the correct answer is: **Remove public read access from the S3 bucket. Use CloudFront as the global content delivery network (CDN) service for the photos and use Signed URLs with expiry dates** .

The option that says: **Use CloudFront to distribute static content and block the IP addresses of the other websites that are illegally linking the photos to their own websites**  is incorrect. Although you can block the offending IP addresses of the websites that illegally use your photos, other attackers can still use a different IP address and use your photos without your permission.

The option that says: **Store photos on an EBS volume of the web server with data encryption enabled**  is incorrect. An EBS volume is not a scalable storage solution and is not suitable in hosting static assets for a public website.

The option that says: **Block the IPs of the offending websites in Security Groups and use S3 Cross-Region Replication (CRR)**  is incorrect. In a Security Group, you can specify and allow rules, but not deny rules. In addition, S3 Cross-Region Replication (CRR) will not provide the security needed in this case. Take note: although S3 Cross-Region Replication replicates the bucket to another region, it is still better to use CloudFront to cover all of the global regions.

**References:**

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html)

[https://aws.amazon.com/cloudfront/](https://aws.amazon.com/cloudfront/)

**Check out this Amazon CloudFront Cheat Sheet:**

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professiona](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 72 — ✅ ĐÚNG

### Câu hỏi

A leading electronics company is getting ready to make a major public announcement of its latest smartphone. The official website uses an Application Load Balancer in front of an Auto Scaling group of On-Demand Amazon EC2 instances, which are deployed across multiple Availability Zones with a Multi-AZ Amazon RDS MySQL database. In preparation for its new product launch, the solutions architect checked the performance of the company website and found that the database takes a lot of time to retrieve the data when there are over 100,000 simultaneous requests on the server. The static content, such as the images and videos, is promptly loaded as expected, but not the customer information that is fetched from the database.

Which of the following options could be done to solve this issue in a cost-effective way? (Select TWO.)

### Các phương án

- **A.** Implement a caching system using Amazon ElastiCache in-memory cache on each Availability Zone.
- **B.** Configure the database tier to use sharding, which will distribute the incoming load to multiple RDS MySQL instances.
- **C.** Add Read Replicas in RDS for each Availability Zone.
- **D.** Migrate the database to use Amazon Keyspaces (for Apache Cassandra), which natively supports sharding to distribute database queries to multiple nodes.
- **E.** Launch an Amazon CloudFront web distribution to solve the latency issue.

> **Bạn chọn:** A, C
> **Đáp án đúng:** A, C

### Giải thích

In-memory data caching can be one of the most effective strategies to improve your overall application performance and to **reduce**  your database costs. Caching can be applied to any type of database including relational databases such as Amazon RDS or NoSQL databases such as Amazon DynamoDB, MongoDB, and Apache Cassandra. The best part of caching is that it’s minimally invasive to implement and by doing so, your application performance regarding both scale and speed is dramatically improved.

![image](https://media.tutorialsdojo.com/sap_rds_caching.PNG)

In this scenario, the issue lies in the database tier of the architecture.

Hence, the correct answers are:

**– Implement a caching system using Amazon ElastiCache in-memory cache on each Availability Zone.**  Adding a cache will significantly reduce the retrieval time for frequent database queries. This also reduces the load significantly on the database tier.

**– Add Read Replicas in RDS for each Availability Zone.**  This improves the database retrieval time as there will be more nodes that can serve the database request. You won’t need to increase the master instance size to accommodate all the read loads.

The option that says: **Configure the database tier to use sharding, which will distribute the incoming load to multiple RDS MySQL instances** is incorrect because this solution is not cost-effective unlike the options mentioned above. It is quite expensive to implement load distribution on the RDS instances because you will need to use multiple sets of standby instances and read replicas. Since it will use more instances, this solution will cost more as opposed to using just Read Replicas.

The option that says: **Migrate the database to use Amazon Keyspaces (for Apache Cassandra), which natively supports sharding to distribute database queries to multiple nodes**  is incorrect. Amazon Keyspaces is primarily designed to be compatible with Apache Cassandra databases. Since the question uses MySQL compatible database, using Amazon Keyspaces is not recommended here.

The option that says: **Launch an Amazon CloudFront web distribution to solve the latency issu** ***e*** is incorrect. This option tries to improve the performance of the front-end tier. To solve the slow data retrieval times from RDS, it is typically best to implement caching and adding Read Replicas which are cheaper and simpler to do than upgrading the RDS database instance.

**References:**

[https://aws.amazon.com/caching/database-caching/](https://aws.amazon.com/caching/database-caching/)

[https://aws.amazon.com/blogs/database/sharding-with-amazon-relational-database-service/](https://aws.amazon.com/blogs/database/sharding-with-amazon-relational-database-service/)

**Check out this Amazon RDS Cheat Sheet:**

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

---

## Câu 73 — ✅ ĐÚNG

### Câu hỏi

A tech company uses AWS CloudFormation to deploy a three-tier web application that consists of a web tier, application tier, and database tier. The application will utilize an Amazon DynamoDB table for database storage. All resources will be created using a CloudFormation template.

Which of the following options would allow the application instances access to the DynamoDB tables without exposing the API credentials?

### Các phương án

- **A.** Launch an IAM user in the CloudFormation template that has permissions to read and write from the DynamoDB table. Use the GetAtt function to retrieve the Access and secret keys and pass them to the web application instance through the use of its instance user-data.
- **B.** Launch an IAM Role that has the required permissions to read and write from the required DynamoDB table. Associate the Role to the application instances by referencing it to the `AWS::IAM::InstanceRoleName` Property.
- **C.** In the CloudFormation template, use the Parameter section to have the user input the AWS Access and Secret Keys from an already created IAM user that has the permissions required to interact with the DynamoDB table.
- **D.** Launch an IAM Role that has the required permissions to read and write from the DynamoDB table. Reference the IAM Role as a property inside the `AWS::IAM::InstanceProfile` of the application instance.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

**Identity and Access Management**  is an AWS service that you can use to manage users and their permissions in AWS. You can use IAM with AWS CloudFormation to specify what AWS CloudFormation actions users can perform, such as viewing stack templates, creating stacks, or deleting stacks. Furthermore, anyone managing AWS CloudFormation stacks will require permissions to resources within those stacks. For example, if users want to use AWS CloudFormation to launch, update, or terminate Amazon EC2 instances, they must have permission to call the relevant Amazon EC2 actions.

Using roles to grant permissions to applications that run on EC2 instances requires a bit of extra configuration. An application running on an EC2 instance is abstracted from AWS by the virtualized operating system. Because of this extra separation, an additional step is needed to assign an AWS role and its associated permissions to an EC2 instance and make them available to its applications. This extra step is the creation of an [instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)[profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) that is attached to the instance.

![image](https://media.tutorialsdojo.com/sap_lambda_iam.png)

The instance profile contains the role and can provide the role’s temporary credentials to an application that runs on the instance. Those temporary credentials can then be used in the application’s API calls to access resources and to limit access to only those resources that the role specifies. Note that only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.

Using roles in this way has several benefits. Because role credentials are temporary and rotated automatically, you don’t have to manage credentials, and you don’t have to worry about long-term security risks. In addition, if you use a single role for multiple instances, you can make a change to that one role and the change is propagated automatically to all the instances.

An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts. If you use the AWS Management Console to create a role for Amazon EC2, the console automatically creates an instance profile and gives it the same name as the role.

Hence, the correct answer is: **Launch an IAM Role that has the required permissions to read and write from the DynamoDB table. Reference the IAM Role as a property inside the `AWS::IAM::InstanceProfile` of the application instance.**

The option that says: **Launch an IAM Role that has the required permissions to read and write from the required DynamoDB table. Associate the Role to the application instances by referencing it to the `AWS::IAM::InstanceRoleName` property**  is incorrect because you have to use the `InstanceProfile` property instead. Take note that there is no `InstanceRoleName` property in IAM.

The option that says: **In the CloudFormation template, use the Parameter section to have the user input the AWS Access and Secret Keys from an already created IAM user that has the permissions required to interact with the DynamoDB table**  is incorrect because it is a security risk to include the IAM access keys in a CloudFormation template. You have to use an IAM Role instead.

The option that says:**Launch an IAM user in the CloudFormation template that has permissions to read and write from the DynamoDB table. Use the GetAtt function to retrieve the Access and secret keys and pass them to the web application instance through the use of its instance user-data**  is incorrect because it is inappropriate to use an IAM User to provide an EC2 instance the required access to the DynamoDB table. Attaching an IAM Role to the EC2 instances is the most suitable solution in this scenario.

**References:**

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#use-iam-to-control-access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#use-iam-to-control-access)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html)

**Check out this AWS CloudFormation Cheat Sheet:**

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

---

## Câu 74 — ❌ SAI

### Câu hỏi

A company wants to have a secure content management solution that can be accessed by its external custom applications via API calls. The solutions architect has been instructed to create the infrastructure design. The solution should enable users to upload documents as well as download a specific version or the latest version of a document. There is also a requirement to enable customer administrators to simply submit an API call that can roll back changes to existing files sent to the system.

Which of the following options is the MOST secure and suitable solution that the solutions architect should implement?

### Các phương án

- **A.** Use S3 with Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Use client-side encryption to encrypt customer files then share the KMS Key ID and the client-side master key to all customers in order to access the CMS.
- **B.** Use Amazon WorkDocs for document storage and utilize its user access management, version control, and built-in encryption. Integrate the Amazon WorkDocs Content Manager to the external custom applications. Develop a rollback feature to replace the current document version with the previous version from Amazon WorkDocs.
- **C.** Use Amazon S3 with Versioning and Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Encrypt all documents using client-side encryption for enhanced data security. Share the encryption keys to all customers to unlock the documents. Develop a rollback feature to replace the current document version with the previous version from Amazon S3.
- **D.** Use Amazon EFS for object storage and enable data encryption in transit with TLS. Store unique customer managed keys in AWS KMS. Set up IAM roles and IAM access policies for EFS to specify separate encryption keys for each customer application. Utilize file locking and file versioning features in EFS to roll back changes to existing files stored in the CMS.

> **Bạn chọn:** C
> **Đáp án đúng:** B

### Giải thích

**Amazon WorkDocs**  is a fully managed, secure content creation, storage, and collaboration service. With Amazon WorkDocs, you can easily create, edit, and share content, and because it’s stored centrally on AWS, access it from anywhere on any device. Amazon WorkDocs makes it easy to collaborate with others, and lets you easily share content, provide rich feedback, and collaboratively edit documents. You can use Amazon WorkDocs to retire legacy file share infrastructure by moving file shares to the cloud. Amazon WorkDocs lets you integrate with your existing systems, and offers a rich API so that you can develop your own content-rich applications. Amazon WorkDocs is built on AWS, where your content is secured on the world’s largest cloud infrastructure.

![image](https://media.tutorialsdojo.com/sap_amazon_workdocs_overview.png)

Amazon WorkDocs Content Manager is a high-level utility tool that uploads content or downloads it from an Amazon WorkDocs site. It can be used for both administrative and user applications. For user applications, a developer must construct the Amazon WorkDocs Content Manager with anonymous AWS credentials and an authentication token. For administrative applications, the Amazon WorkDocs client must be initialized with AWS Identity and Access Management (IAM) credentials. In addition, the authentication token must be omitted in subsequent API calls.

Hence, the correct answer in this scenario is: **Use Amazon WorkDocs for document storage and utilize its user access management, version control, and built-in encryption. Integrate the Amazon WorkDocs Content Manager to the external custom applications. Develop a rollback feature to replace the current document version with the previous version from Amazon WorkDocs.**

The option that says: **Use Amazon S3 with Versioning and Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Encrypt all documents using client-side encryption for enhanced data security. Share the encryption keys to all customers to unlock the documents. Develop a rollback feature to replace the current document version with the previous version from Amazon S3**  is incorrect. Although you can use Amazon S3, sharing the encryption keys to all customers just to unlock the documents is a security risk.

The option that says: **Use S3 with Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Use client-side encryption to encrypt customer files then share the KMS Key ID and the client-side master key to all customers in order to access the CMS**  is incorrect because the S3 bucket being used has only enabled Server Access Logging and not Versioning. In addition, it is also a security risk to share the KMS Key ID and the client-side master key with all customers.

The option that says: **Use Amazon EFS for object storage and enable data encryption in transit with TLS. Store unique customer managed keys in AWS KMS. Set up IAM roles and IAM access policies for EFS to specify separate encryption keys for each customer application. Utilize file locking and file versioning features in EFS to roll back changes to existing files stored in the CMS**  is incorrect because EFS is primarily used as a file system and not for object storage. Although EFS has file locking capabilities, it does not have file versioning features.

**References:**

[https://aws.amazon.com/workdocs/](https://aws.amazon.com/workdocs/)

[https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_constructing.html](https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_constructing.html)

[https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_downloading.html](https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_downloading.html)

---

## Câu 75 — ✅ ĐÚNG

### Câu hỏi

A retail company runs its two-tier e-commerce website on its on-premises data center. The application runs on a LAMP stack behind a load balancing appliance. The operations team uses SSH to login to the application servers to deploy software updates and install patches on the system. The website has been a target of multiple cyber-attacks recently such as:

- Distributed Denial of Service (DDoS) attacks

- SQL Injection attacks

- Dictionary attacks to SSH accounts on the web servers

The solutions architect plans to migrate the whole system to AWS to improve its security and availability. The following approaches are laid out to address the company concerns:

- Fix SQL injection attacks by reviewing existing application code and logic.

- Use the latest Amazon Linux AMIs to ensure that initial security patches are installed.

- Install the AWS Systems Manager agent on the instances to manage OS patching.

Which of the following are additional recommended actions to address the identified attacks while maintaining high availability and security for the application?

### Các phương án

- **A.** Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Enable remote SSH login only on a bastion host with limited access from the company IP address. Migrate the on-premises MySQL server to an Amazon RDS Multi-AZ instance. Create a CloudFront distribution in front of the application servers and enable AWS Shield Standard for DDoS protection.
- **B.** Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Disable remote SSH login to the EC2 instances and use AWS SSM Session Manager instead. Migrate the on-premises MySQL server to an Amazon RDS Single-AZ instance. Create a CloudFront distribution in front of the application servers, and apply AWS WAF rules for the distribution.
- **C.** Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Disable remote SSH login to the EC2 instances and use AWS SSM Session Manager instead. Migrate the on-premises MySQL server to an Amazon RDS Multi-AZ instance. Create a CloudFront distribution in front of the application servers, and apply AWS WAF rules for the distribution. Enable AWS Shield Advanced for added protection.
- **D.** Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Enable remote SSH login on the EC2 instances but with limited access from the company IP address only. Migrate the on-premises MySQL server to an Amazon RDS Single-AZ instance. Enable AWS Shield Standard to protect the instances from DDoS attacks.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

**AWS Systems Manager Session Manager**  allows you to manage your Amazon Elastic Compute Cloud (Amazon EC2) instances, on-premises instances, and virtual machines (VMs) through an interactive one-click browser-based shell or through the AWS Command Line Interface (AWS CLI). Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.

A distributed denial of service (DDoS) attack is an attack in which multiple compromised systems attempt to flood a target, such as a network or web application, with traffic. A DDoS attack can prevent legitimate users from accessing a service and can cause the system to crash due to the overwhelming traffic volume.

AWS provides two levels of protection against DDoS attacks: **AWS Shield Standard**  and **AWS Shield Advanced** . All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. AWS Shield Standard defends against the most common, frequently occurring network and transport layer DDoS attacks that target your website or applications. For higher levels of protection against attacks, you can subscribe to AWS Shield Advanced. When you subscribe to AWS Shield Advanced and add specific resources to be protected, AWS Shield Advanced provides expanded DDoS attack protection for web applications running on the resources.

**AWS WAF**  is a web application firewall that helps protect your web applications or APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources. AWS WAF gives you control over how traffic reaches your applications by enabling you to create security rules that control bot traffic and block common attack patterns, such as SQL injection or cross-site scripting. You can also customize rules that filter out specific traffic patterns.

![image](https://media.tutorialsdojo.com/sap_well_architectured_security.png)

Therefore, the correct answer is: **Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Disable remote SSH login to the EC2 instances and use AWS SSM Session Manager instead. Migrate the on-premises MySQL server to an Amazon RDS Multi-AZ instance. Create a CloudFront distribution in front of the application servers, and apply AWS WAF rules for the distribution. Enable AWS Shield Advanced for added protection.**  AWS SSM Session manager allows secure remote access to your instances without using SSH login. AWS WAF rules can block common web exploits like SQL injection attacks and AWS Shield Advanced provides added protection for DDoS attacks.

The option that says: **Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Enable remote SSH login only on a bastion host with limited access from the company IP address. Migrate the on-premises MySQL server to an Amazon RDS Multi-AZ instance. Create a CloudFront distribution in front of the application servers and enable AWS Shield Standard for DDoS protection**  is incorrect. You don’t need to use a bastion host if you have AWS SSM agent installed on the instances. You can use SSM Session Manager to login to the servers. AWS Shield Standard is already enabled by default but you should enable AWS Shield Advanced for a higher level of protection.

The option that says: **Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Enable remote SSH login on the EC2 instances but with limited access from the company IP address only. Migrate the on-premises MySQL server to an Amazon RDS Single-AZ instance. Enable AWS Shield Standard to protect the instances from DDoS attacks**  is incorrect. You don’t need to use a bastion host if you have AWS SSM agent installed on the instances. Using a Single-AZ RDS instance is not recommended if you require a highly available database.

The option that says: **Use an Application Load Balancer to spread the load on a cluster of Amazon EC2 instances. Disable remote SSH login to the EC2 instances and use AWS SSM Session Manager instead. Migrate the on-premises MySQL server to an Amazon RDS Single-AZ instance. Create a CloudFront distribution in front of the application servers, and apply AWS WAF rules for the distribution**  is incorrect. AWS WAF may protect you from common web attacks, but you still need to enable AWS Shield Advanced for a higher level of protection against DDoS attacks. Using a Single-AZ RDS instance is not recommended if you require a highly available database.

**References:**

[https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

[https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)

[https://aws.amazon.com/waf/](https://aws.amazon.com/waf/)

**Check out these AWS Systems Manager and AWS WAF Cheat Sheets:**

[https://tutorialsdojo.com/aws-systems-manager/](https://tutorialsdojo.com/aws-systems-manager/)

[https://tutorialsdojo.com/aws-waf/](https://tutorialsdojo.com/aws-waf/)

---
