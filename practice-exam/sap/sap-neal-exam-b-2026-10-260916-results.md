# Neal Exam B — 75 questions (2026-10-26 09:16)

**Kết quả:** 55/75 câu đúng (73,33%)

**Time used:** 3:30:01 (time up) · **Flagged:** 28, 35, 69, 70, 71, 73, 74

| Domain | Score |
|---|---|
| CSAP – Design Solutions for Organizational Complexity | 57.14% |
| CSAP – Design for New Solutions | 71.43% |
| CSAP – Continuous Improvement for Existing Solutions | 74.07% |
| CSAP – Accelerate Workload Migration and Modernization | 76.92% |

## Câu 1 — ✅ ĐÚNG

<!-- source: T6Q35 · domain: ORG -->

### Câu hỏi

The security department of a large company with several AWS accounts wishes to centralize the management of identities and AWS permissions. The design should also synchronize authentication credentials with the company’s existing on-premises identity management provider (IdP).
Which solution will meet the security department’s requirements?

### Các phương án

- **A.** Create a SAML-based identity management provider in a central account and map IAM roles that provide the necessary permissions for users. Map users in the on-premises IdP groups to IAM roles. Use cross-account access to the other AWS accounts.
- **B.** Deploy the required IAM users, groups, roles, and policies in every AWS account. Create an AWS Organization and federate the on-premises identity management provider and the AWS accounts.
- **C.** Create an AWS Organization with a management account that defines the SCPs for member accounts. Create a SAML-based identity management provider in each account and map users in the on-premises IdP groups to IAM roles.
- **D.** Create a SAML-based identity management provider in a central account and map IAM roles that provide the necessary permissions for users. Create a centralized AWS Lambda function that replicates the identities in the on-premises IdP groups to the AWS accounts.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

A SAML-based IdP can be created that integrates with AWS IAM. In this configuration you map IAM roles that are assumed by authenticated identities. These IAM roles must have the correct permissions for users. The users can then assume roles in the other AWS accounts in order to perform there.
This solution centralizes the management of identities, federation, and permissions and allows the users to access each account as needed. The diagram below depicts how identity federation works between IAM and an on-premises IdP:
CORRECT:
"Create a SAML-based identity management provider in a central account and map IAM roles that provide the necessary permissions for users. Map users in the on-premises IdP groups to IAM roles. Use cross-account access to the other AWS accounts" is the correct answer.
INCORRECT:
"Deploy the required IAM users, groups, roles, and policies in every AWS account. Create an AWS Organization and federate the on-premises identity management provider and the AWS accounts" is incorrect. This does not centralize the management of permissions and identities.
INCORRECT:
"Create an AWS Organization with a management account that defines the SCPs for member accounts. Create a SAML-based identity management provider in each account and map users in the on-premises IdP groups to IAM roles" is incorrect. The SAML-based IdP should be mapped to the central account, not each individual account.
INCORRECT:
"Create a SAML-based identity management provider in a central account and map IAM roles that provide the necessary permissions for users. Create a centralized AWS Lambda function that replicates the identities in the on-premises IdP groups to the AWS accounts" is incorrect. This does not centralize the control of permissions and identities and there could be several security issues with using this method.
References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/
Generated on 10/21/2026

## Câu 2 — ✅ ĐÚNG

<!-- source: T1Q13 · domain: ORG -->

### Câu hỏi

A company has created several development accounts in an AWS Organizations organization. The company has defined a fixed budget for each development account and needs to ensure that developers cannot launch expensive services or exceed the fixed monthly budget.
Which combination of steps should a solutions architect take? (Select THREE.)

### Các phương án

- **A.** Create an SCP that defines a fixed monthly resource usage limit. Apply the SCP to an OU containing the development accounts.
- **B.** Use the AWS Budgets service to define a fixed monthly budget for each development account.
- **C.** Create an SCP that denies access to expensive services. Apply the SCP to an OU containing the development accounts.
- **D.** Create an IAM policy that denies access to expensive services. Apply the IAM policy to the development accounts.
- **E.** Create an AWS Budgets alert action to terminate services when the budgeted amount is reached. Configure the action to terminate all services.
- **F.** Create an AWS Budgets alert action to send an Amazon SNS notification when the budgeted amount is reached. Invoke an AWS Lambda function to terminate all services.

> **Bạn chọn:** B, C, F
> **Đáp án đúng:** B, C, F

### Giải thích

The solutions architect should use an SCP to deny access to expensive services as this will ensure that they cannot be launched in the first place. Then, an AWS Budget should be defined and configured with the fixed monthly cost allowance. The budget can trigger an SNS notification which in turn can invoke an AWS Lambda function to terminate the resources.
CORRECT:
"Use the AWS Budgets service to define a fixed monthly budget for each development account" is a correct answer (as explained above.)
CORRECT:
"Create an SCP that denies access to expensive services. Apply the SCP to an OU containing the development accounts" is also a correct answer (as explained above.)
CORRECT:
"Create an AWS Budgets alert action to send an Amazon SNS notification when the budgeted amount is reached. Invoke an AWS Lambda function to terminate all services" is also a correct answer (as explained above.)
INCORRECT:
"Create an SCP that defines a fixed monthly resource usage limit. Apply the SCP to an OU containing the development accounts" is incorrect. You cannot define resource limits in this manner using an SCP.
INCORRECT:
"Create an IAM policy that denies access to expensive services. Apply the IAM policy to the development accounts" is incorrect. You cannot attach an IAM policy to an account, they must be attached to users, groups, or roles.
INCORRECT:
"Create an AWS Budgets alert action to terminate services when the budgeted amount is reached. Configure the action to terminate all services" is incorrect. You cannot configure the alert action to terminate all services. You can stop EC2 and RDS instances or you can attach an IAM policy or SCP.
References:
https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-organizations/

## Câu 3 — ✅ ĐÚNG

<!-- source: T1Q10 · domain: MIG -->

### Câu hỏi

A company is migrating an order processing application to the AWS Cloud. The usage patterns vary significantly but the application must be available at all times. Orders must be processed immediately and in the order that they are received. Which actions should a Solutions Architect take to meet these requirements?

### Các phương án

- **A.** Use Amazon SNS with FIFO to send orders in the correct order. Use Spot Instances in multiple Availability Zones for processing.
- **B.** Use Amazon SNS with FIFO to send orders in the correct order. Use a single large Reserved Instance for processing.
- **C.** Use Amazon SQS with FIFO to queue messages in the correct order. Use Reserved Instances in multiple Availability Zones for processing.
- **D.** Use Amazon SQS with FIFO to queue messages in the correct order. Use Spot Instances in multiple Availability Zones for processing.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Amazon Simple Queue Service (SQS) with a first-in-first-out (FIFO) queue will ensure that messages are delivered to the processing layer in the correct order. An application component running on Amazon EC2 will then be configured to poll the queue and process the messages.
Reserved instances should be used for the processing layer as this is the best way to ensure that the application is available at all times at the best cost.
CORRECT:
"Use Amazon SQS with FIFO to queue messages in the correct order. Use Reserved Instances in multiple Availability Zones for processing" is the correct answer.
INCORRECT:
"Use Amazon SQS with FIFO to queue messages in the correct order. Use Spot Instances in multiple Availability Zones for processing" is incorrect. With Spot instances the application could become unavailable if the Spot price exceeds the default maximum price configured.
INCORRECT:
"Use Amazon SNS with FIFO to send orders in the correct order. Use Spot Instances in multiple Availability Zones for processing" is incorrect. SNS is used for sending notifications, it is not the best service to use for this use case.
INCORRECT:
"Use Amazon SNS with FIFO to send orders in the correct order. Use a single large Reserved Instance for processing" is incorrect. SNS is used for sending notifications, it is not the best service to use for this use case.
References:
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

## Câu 4 — ✅ ĐÚNG

<!-- source: T2Q30 · domain: NEW -->

### Câu hỏi

A company is planning to build a high-performance computing (HPC) solution in the AWS Cloud. The solution will include a 10-node cluster running Linux. High speed and low latency inter-instance connectivity is required to optimize the performance of the cluster.
Which combination of steps will meet these requirements? (Choose two.)

### Các phương án

- **A.** Deploy Amazon EC2 instances in a cluster placement group.
- **B.** Deploy instances across at least three Availability Zones.
- **C.** Deploy Amazon EC2 instances in a partition placement group.
- **D.** Use Amazon EC2 instance types and AMIs that support EFA.
- **E.** Use Amazon EC2 instances that support burstable performance.

> **Bạn chọn:** A, D
> **Đáp án đúng:** A, D

### Giải thích

A cluster placement group is a logical grouping of instances within a single Availability Zone. A cluster placement group can span peered VPCs in the same Region. Instances in the same cluster placement group enjoy a higher per-flow throughput limit for TCP/IP traffic and are placed in the same high-bisection bandwidth segment of the network.
Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput, or both. They are also recommended when the majority of the network traffic is between the instances in the group.
An Elastic Fabric Adapter (EFA) is a network device that you can attach to your Amazon EC2 instance to accelerate High Performance Computing (HPC) and machine learning applications. EFA enables you to achieve the application performance of an on-premises HPC cluster, with the scalability, flexibility, and elasticity provided by the AWS Cloud.
CORRECT:
"Deploy Amazon EC2 instances in a cluster placement group" is a correct answer.
CORRECT:
"Use Amazon EC2 instance types and AMIs that support EFA" is also a correct answer.
INCORRECT:
"Deploy instances across at least three Availability Zones" is incorrect. This will increase latency between instances which is bad for HPC applications.
INCORRECT:
"Deploy Amazon EC2 instances in a partition placement group" is incorrect. Partition placement groups are recommended for applications that are distributed and replicated. It does not provide the optimum latency and throughput required by an HPC application.
INCORRECT:
"Use Amazon EC2 instances that support burstable performance" is incorrect. This feature provides bursts of CPU performance but in this scenario low latency and high throughput is required between instances and burstable CPUs do not assist with this.
References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#placement-groups-cluster
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 5 — ✅ ĐÚNG

<!-- source: T2Q27 · domain: MIG -->

### Câu hỏi

A company is running a custom Java application on-premises and plans to migrate the application to the AWS Cloud. The application uses a MySQL database and the application servers maintain users’ sessions locally. Which combination of architecture changes will be required to create a highly available solution on AWS? (Select THREE.)

### Các phương án

- **A.** Configure the application to store the user's session in Amazon ElastiCache. Use Application Load Balancers to distribute the load between application instances.
- **B.** Migrate the database to Amazon EC2 instances in multiple Availability Zones. Configure Multi-AZ to synchronize the changes.
- **C.** Migrate the database to Amazon RDS for MySQL. Configure the RDS instance to use a Multi-AZ deployment.
- **D.** Move the Java content to an Amazon S3 bucket configured for static website hosting. Configure cross-Region replication for the S3 bucket contents.
- **E.** Put the application instances in an Amazon EC2 Auto Scaling group. Configure the Auto Scaling group to create new instances if an instance becomes unhealthy.
- **F.** Configure the application to run in multiple Regions. Use an Application Load Balancer to distribute the load between application instances.

> **Bạn chọn:** A, C, E
> **Đáp án đúng:** A, C, E

### Giải thích

To create a highly available application architecture on AWS the Solutions Architect can use Amazon EC2 Auto Scaling across multiple availability zones to ensure the application instances are available. The instances can be placed behind an ALB to distribute incoming connection requests between them.
For the database layer the MySQL database can be directly migrated to Amazon RDS with Multi-AZ which will provide fault tolerance. Additionally, Amazon ElastiCache can be used for storing session state data so the failure of an instance does not cause data to be lost.
CORRECT:
"Configure the application to store the user's session in Amazon ElastiCache. Use Application Load Balancers to distribute the load between application instances" is a correct answer.
CORRECT:
"Migrate the database to Amazon RDS for MySQL. Configure the RDS instance to use a Multi-AZ deployment" is also a correct answer.
CORRECT:
"Put the application instances in an Amazon EC2 Auto Scaling group. Configure the Auto Scaling group to create new instances if an instance becomes unhealthy" is also a correct answer.
INCORRECT:
"Migrate the database to Amazon EC2 instances in multiple Availability Zones. Configure Multi-AZ to synchronize the changes" is incorrect. You cannot configure Multi-AZ for databases running on EC2 instances as this is an RDS feature.
INCORRECT:
"Move the Java content to an Amazon S3 bucket configured for static website hosting. Configure cross-Region replication for the S3 bucket contents" is incorrect. Static website hosting cannot be used for dynamic content.
INCORRECT:
"Configure the application to run in multiple Regions. Use an Application Load Balancer to distribute the load between application instances" is incorrect. You cannot use an ELB to load balance between Regions, multiple AZs should be used instead.
References:
https://aws.amazon.com/getting-started/hands-on/building-fast-session-caching-with-amazon-elasticache-for-redis/
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 6 — ✅ ĐÚNG

<!-- source: T3Q23 · domain: NEW -->

### Câu hỏi

A Solutions Architect is helping to standardize a company’s method of deploying applications to AWS using AWS CodePipeline and AWS CloudFormation. A group of developers create applications using JavaScript and TypeScript and they are concerned about needing to learn new domain-specific languages. They are also reluctant to lose access to features of the existing languages such as looping.
How can the Solutions Architect address the developers concerns and quickly bring the applications up to deployment standards?

### Các phương án

- **A.** Create CloudFormation templates and re-use parts of the JavaScript and TypeScript code as Instance user data. Use the AWS Cloud Development Kit (AWS CDK) to deploy the application using these templates. Incorporate the AWS CDK into CodePipeline and deploy the application to AWS using these templates.
- **B.** Use AWS SAM and specify a serverless transform. Add the JavaScript and TypeScript code as metadata to the template file. Use AWS CodeBuild to build the code and output a CloudFormation template.
- **C.** Use a third-party resource provisioning engine inside AWS CodeBuild to standardize the deployment processes. Orchestrate the CodeBuild job using CodePipeline and use CloudFormation for deployment.
- **D.** Define the AWS resources using JavaScript or TypeScript. Use the AWS Cloud Development Kit (AWS CDK) to create CloudFormation templates from the developers' code and use the AWS CDK to create CloudFormation stacks. Incorporate the AWS CDK as a CodeBuild job in CodePipeline.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

The AWS CDK is a software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. You can use the AWS CDK to define your cloud resources in a familiar programming language. The AWS CDK supports TypeScript, JavaScript, Python, Java, and C#/.Net.
Developers can use one of the supported programming languages to define reusable cloud components known as
Constructs
. You compose these together into
Stacks
and
Apps
. The diagram below depicts how an AWS CDK application is constructed:
CORRECT:
"Define the AWS resources using JavaScript or TypeScript. Use the AWS Cloud Development Kit (AWS CDK) to create CloudFormation templates from the developers' code and use the AWS CDK to create CloudFormation stacks. Incorporate the AWS CDK as a CodeBuild job in CodePipeline" is the correct answer.
INCORRECT:
"Create CloudFormation templates and re-use parts of the JavaScript and TypeScript code as Instance user data. Use the AWS Cloud Development Kit (AWS CDK) to deploy the application using these templates. Incorporate the AWS CDK into CodePipeline and deploy the application to AWS using these templates" is incorrect. You cannot use instance user data to run JavaScript or TypeScript code. This is not a way to deploy one of these applications.
INCORRECT:
"Use AWS SAM and specify a serverless transform. Add the JavaScript and TypeScript code as metadata to the template file. Use AWS CodeBuild to build the code and output a CloudFormation template" is incorrect. AWS SAM is used for deploying serverless applications using CloudFormation. You cannot run code using metadata in an AWS SAM app. You also cannot use CodeBuild to create a CloudFormation template.
INCORRECT:
"Use a third-party resource provisioning engine inside AWS CodeBuild to standardize the deployment processes. Orchestrate the CodeBuild job using CodePipeline and use CloudFormation for deployment" is incorrect. CodeBuild does not do resources provisioning – CodeDeploy or CloudFormation does.
References:
https://docs.aws.amazon.com/cdk/latest/guide/home.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-developer-tools-sap/

## Câu 7 — ✅ ĐÚNG

<!-- source: T3Q34 · domain: MIG -->

### Câu hỏi

A company is planning to migrate on-premises resources to AWS. The resources include over 150 virtual machines (VMs) that use around 50 TB of storage. Most VMs can be taken offline outside of business hours, however, a few are mission critical and downtime must be minimized. The company’s internet bandwidth is fully utilized and cannot currently be increased. A Solutions Architect must design a migration strategy that can be completed within the next 3 months.
Which method would fulfill these requirements?

### Các phương án

- **A.** Set up a 1 Gbps AWS Direct Connect connection. Then, provision a private virtual interface, and use AWS Application Migration Service (MGN) to migrate the VMs into Amazon EC2.
- **B.** Use an AWS Storage Gateway file gateway. Mount the file gateway and synchronize the VM filesystems to cloud storage. Use the VM Import/Export to import from cloud storage to Amazon EC2.
- **C.** Export the VMs locally, beginning with the most mission-critical servers first. Use Amazon S3 Transfer Acceleration to quickly upload each VM to Amazon S3 after they are exported. Use VM Import/Export to import the VMs into Amazon EC2.
- **D.** Migrate mission-critical VMs with AWS Application Migration Service (MGN). Export the other VMs locally and transfer them to Amazon S3 using AWS Snowball. Use VM Import/Export to import the VMs into Amazon EC2.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

The best way to avoid downtime is to provision an AWS Direct Connect connection and use AWS Application Migration Service (MGN) to migrate the VMs into EC2. AWS Application Migration Service (MGN) simplifies and speeds up the migration of virtual machines (VMs) from on-premises environments to the AWS Cloud.
MGN offers an agentless replication approach, eliminating the need for additional software installations. Continuous data replication ensures near real-time synchronization between source and target VMs, enabling a smooth transition with minimal downtime. MGN includes automated testing and post-migration validation features, allowing for thorough verification of the migration process.
CORRECT:
"Set up a 1 Gbps AWS Direct Connect connection. Then, provision a private virtual interface, and use AWS Application Migration Service (MGN) to migrate the VMs into Amazon EC2" is the correct answer.
INCORRECT:
"Migrate mission-critical VMs with AWS Application Migration Service (MGN). Export the other VMs locally and transfer them to Amazon S3 using AWS Snowball. Use VM Import/Export to import the VMs into Amazon EC2" is incorrect. The VMs that are exported and transported using Snowball will be offline for several days in this scenario which is not acceptable.
INCORRECT:
"Use an AWS Storage Gateway file gateway. Mount the file gateway and synchronize the VM filesystems to cloud storage. Use the VM Import/Export to import from cloud storage to Amazon EC2" is incorrect. You cannot migrate VMs in this manner and you cannot mount block-based volumes and replicate the entire operating system volume using file-based storage systems.
INCORRECT:
"Export the VMs locally, beginning with the most mission-critical servers first. Use Amazon S3 Transfer Acceleration to quickly upload each VM to Amazon S3 after they are exported. Use VM Import/Export to import the VMs into Amazon EC2" is incorrect. S3 has an object limit of 5 TB which could be an issue for some VMs (maybe). The key problem here is that there is no bandwidth to quickly upload these images, even using Transfer Acceleration will not help if the bottleneck is the saturated internet link at the data center.
References:
https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-migration-sap/

## Câu 8 — ✅ ĐÚNG

<!-- source: T4Q18 · domain: CI -->

### Câu hỏi

An S3 endpoint has been created in an Amazon VPC. A staff member assumed an IAM role and attempted to download an object from a bucket using the endpoint. The staff member received the error message “403: Access Denied”. The bucket is encrypted using an AWS KMS key. A Solutions Architect has verified that the staff member assumed the correct IAM role and the role does allow the object to be downloaded. The bucket policy and NACL are also valid.
Which additional step should the Solutions Architect take to troubleshoot this issue?

### Các phương án

- **A.** Ensure that blocking all public access has not been enabled in the S3 bucket.
- **B.** Verify that the IAM role has permission to decrypt the referenced KMS key.
- **C.** Verify that the IAM role has the correct trust relationship configured.
- **D.** Check that local firewall rules are not preventing access to the S3 endpoint.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

If an IAM user can’t access an object that the user has full permissions to, then check if the object is encrypted by AWS KMS. You can use the Amazon S3 console to view the object’s properties, which include the object’s encryption information.
If the object is KMS encrypted, then make sure that the KMS key policy grants permissions to the IAM user for the following actions:
- "kms:Encrypt"
- "kms:Decrypt"
- "kms:ReEncrypt*"
- "kms:GenerateDataKey*"
- "kms:DescribeKey"
CORRECT:
"Verify that the IAM role has permission to decrypt the referenced KMS key" is the correct answer.
INCORRECT:
"Verify that the IAM role has the correct trust relationship configured" is incorrect. If the IAM role trust relationship was not configured correctly the user would not be able to assume the role and the question states that the user did assume the role.
INCORRECT:
"Ensure that blocking all public access has not been enabled in the S3 bucket" is incorrect. This is not a case of public access, the S3 bucket is being accessed using an IAM role with the permissions set correctly.
INCORRECT:
"Check that local firewall rules are not preventing access to the S3 endpoint" is incorrect. The NACL is valid and an access denied error is being generated by S3, it would not be generated by a firewall.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/s3-troubleshoot-403/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 9 — ✅ ĐÚNG

<!-- source: T4Q4 · domain: NEW -->

### Câu hỏi

A company needs to host a highly available and secure image processing application in AWS. Their VPC architecture consists of a public and a private subnet within an Amazon VPC traversing two Availability Zones.
The application is hosted on Amazon EC2 instances in the private subnet. The application needs to communicate with the internet via two NAT gateways and uses an Application Load Balancer in the public subnet. Images are stored in an Amazon S3 bucket which average around 1 TB in new objects per day.
A solutions architect must reduce the associated cost of the solution and reduce manual effort while maintaining security.
How can this be accomplished?

### Các phương án

- **A.** Use NAT instances in place of the NAT gateways. In the VPC route table, create a route from the private subnets to the NAT instances.
- **B.** Move the EC2 instances to the public subnets. Remove the NAT gateways.
- **C.** Set up an S3 gateway VPC endpoint in the VPC. Attach an endpoint policy to the endpoint to allow the required actions on the S3 bucket.
- **D.** Attach an Amazon Elastic File System (Amazon EFS) volume to the EC2 instances and host the images on this EFS volume.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

> ⚠️ Explanation says NAT gateways become unnecessary, but the scenario still needs internet access.

There are already two NAT gateways in place but Amazon S3 and DynamoDB come with the option to place gateway endpoints in the VPC which provide reliable connectivity to Amazon S3 without requiring an internet gateway or a NAT device for your VPC. There is no additional charge for using gateway endpoints and this is a secure method of connecting to these service endpoints without using public IP addresses. The cost of the solution can then be reduced as the NAT gateways would no longer be needed.
CORRECT:
"Set up an S3 gateway VPC endpoint in the VPC. Attach an endpoint policy to the endpoint to allow the required actions on the S3 bucket" is the correct answer (as explained above.)
INCORRECT:
" Use NAT instances in place of the NAT gateways. In the VPC route table, create a route from the private subnets to the NAT instances." is incorrect.
Including NAT instances would have negative impact as they require maintenance and cost is associated with them as well.
INCORRECT:
"Move the EC2 instances to the public subnets. Remove the NAT gateways" is incorrect.
Moving an instance to public subnet poses additional security threats and is not recommended. Instances should run in private subnets when possible.
INCORRECT:
"Attach an Amazon Elastic File System (Amazon EFS) volume to the EC2 instances and host the images on the EFS volume" is incorrect.
Since the question doesn’t mention file shares, but rather S3 (object storage), EFS can be eliminated.
References:
https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-vpc/

## Câu 10 — ❌ SAI

<!-- source: T6Q19 · domain: MIG -->

### Câu hỏi

A company needs to close a data center and must migrate data to AWS urgently. The data center has a 1 Gbps internet connection and a 500 Mbps AWS Direct Connect link. The company must transfer 25 TB of data from the data center to an Amazon S3 bucket.
What is the FASTEST method of transferring the data?

### Các phương án

- **A.** Use the AWS Direct Connect link to upload the data to S3.
- **B.** Upload the data to the S3 bucket using S3 Transfer Acceleration.
- **C.** Use AWS DataSync to migrate the data to S3.
- **D.** Copy the data to an 80 TB AWS Snowball device.

> **Bạn chọn:** D
> **Đáp án đúng:** B

### Giải thích

The fastest way to upload the data would be to use the higher speed internet connection and use Amazon S3 Transfer Acceleration.
Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.
CORRECT:
"Upload the data to the S3 bucket using S3 Transfer Acceleration" is the correct answer.
INCORRECT:
"Use the AWS Direct Connect link to upload the data to S3" is incorrect. The Direct Connect link is slower than the internet link, with transfer acceleration latency can be reduced as the data is sent to the nearest edge location and then routed over the AWS global network.
INCORRECT:
"Use AWS DataSync to migrate the data to S3" is incorrect. AWS DataSync will not improve the speed in this case whereas transfer acceleration will.
INCORRECT:
"Copy the data to an 80 TB AWS Snowball device" is incorrect. With the internet link running at 1 Gbps and 25TB of data, the data can be moved quickly to AWS. Shipping snowball devices both ways will likely take longer.
References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

## Câu 11 — ✅ ĐÚNG

<!-- source: T1Q35 · domain: CI -->

### Câu hỏi

A financial services company receives a data feed from a credit card service provider. The feed consists of approximately 2,500 records that are sent every 10 minutes in plaintext and delivered over HTTPS to an encrypted S3 bucket. The data includes credit card data that must be automatically masked before sending the data to another S3 bucket for additional internal processing. There is also a requirement to remove and merge specific fields, and then transform the record into JSON format.
Which solutions will meet these requirements?

### Các phương án

- **A.** Trigger an AWS Lambda function on file delivery that extracts each record and writes it to an Amazon SQS queue. Trigger another Lambda function when new messages arrive in the SQS queue to process the records, writing the results to a temporary location in Amazon S3. Trigger a final Lambda function once the SQS queue is empty to transform the records into JSON format and send the results to another S3 bucket for internal processing.
- **B.** Trigger an AWS Lambda function on file delivery that extracts each record and writes it to an Amazon SQS queue. Configure an AWS Fargate container application to automatically scale to a single instance when the SQS queue contains messages. Have the application process each record and transform the record into JSON format. When the queue is empty, send the results to another S3 bucket for internal processing and scale down the AWS Fargate task.
- **C.** Create an AWS Glue crawler and custom classifier based on the data feed formats and build a table definition to match. Trigger an AWS Lambda function on file delivery to start an AWS Glue ETL job to transform the entire record according to the processing and transformation requirements. Define the output format as JSON. Once complete, have the ETL job send the results to another S3 bucket for internal processing.
- **D.** Create an AWS Glue crawler and custom classifier based upon the data feed formats and build a table definition to match. Perform an Amazon Athena query on file delivery to start an Amazon EMR ETL job to transform the entire record according to the processing and transformation requirements. Define the output format as JSON. Once complete, send the results to another S3 bucket for internal processing and scale down the EMR cluster.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

You can use a Glue crawler to populate the AWS Glue Data Catalog with tables. The Lambda function can be triggered using S3 event notifications when object create events occur. The Lambda function will then trigger the Glue ETL job to transform the records masking the sensitive data and modifying the output format to JSON. This solution meets all requirements.
CORRECT:
"Create an AWS Glue crawler and custom classifier based on the data feed formats and build a table definition to match. Trigger an AWS Lambda function on file delivery to start an AWS Glue ETL job to transform the entire record according to the processing and transformation requirements. Define the output format as JSON. Once complete, have the ETL job send the results to another S3 bucket for internal processing" is the correct answer.
INCORRECT:
"Trigger an AWS Lambda function on file delivery that extracts each record and writes it to an Amazon SQS queue. Trigger another Lambda function when new messages arrive in the SQS queue to process the records, writing the results to a temporary location in Amazon S3. Trigger a final Lambda function once the SQS queue is empty to transform the records into JSON format and send the results to another S3 bucket for internal processing" is incorrect. AWS Glue is an ETL service and is therefore a better fit for processing the records as part of an ETL job rather than using Lambda.
INCORRECT:
"Trigger an AWS Lambda function on file delivery that extracts each record and writes it to an Amazon SQS queue. Configure an AWS Fargate container application to automatically scale to a single instance when the SQS queue contains messages. Have the application process each record and transform the record into JSON format. When the queue is empty, send the results to another S3 bucket for internal processing and scale down the AWS Fargate task" is incorrect. AWS Glue is preferred for ETL work. Also, Lambda is more scalable and will be faster to respond than using a single Fargate task.
INCORRECT:
"Create an AWS Glue crawler and custom classifier based upon the data feed formats and build a table definition to match. Perform an Amazon Athena query on file delivery to start an Amazon EMR ETL job to transform the entire record according to the processing and transformation requirements. Define the output format as JSON. Once complete, send the results to another S3 bucket for internal processing and scale down the EMR cluster" is incorrect. AWS Glue is better suited to this ETL job than using Amazon EMR.
References:
https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html
https://docs.aws.amazon.com/glue/latest/dg/author-job.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

## Câu 12 — ✅ ĐÚNG

<!-- source: T6Q13 · domain: ORG -->

### Câu hỏi

A company has recently established 15 Amazon VPCs within the us-east-1 AWS Region. The company has also established an AWS Direct Connect to the Region from their on-premises data center. The company requires full transitive peering between the VPCs and the on-premises data center.
Which combination of actions is required to implement these requirements with the LEAST complexity? (Select TWO.)

### Các phương án

- **A.** Create an AWS transit gateway and add attachments for all of the VPCs. Configure the route tables in the VPCs to send traffic to the transit gateway.
- **B.** Create VPC peering connections between the VPCs in a fully meshed topology. Configure the route tables in the VPCs to route traffic across the peering connections.
- **C.** Create an AWS Direct Connect (DX) gateway and attach the DX gateway to a transit gateway. Enable route propagation with BGP.
- **D.** Create an AWS Direct Connect (DX) gateway and associate the DX gateway with a VGW in each VPC. Enable route propagation with BGP.
- **E.** Create IPSec VPN connections between the VPCs in a fully meshed topology. Configure the route tables in the VPCs to route traffic across the IPSec VPN connections.

> **Bạn chọn:** A, C
> **Đáp án đúng:** A, C

### Giải thích

The simplest solution here with the lowest complexity is to use a combination of an AWS transit gateway and a DX gateway. The transit gateway allows fully transitive connections between VPCs in a Region. The DX gateway can then connect the transit gateway to the DX connection. BGP is used to propagate routes from the on-premises data center into AWS and vice versa.
The diagram below depicts a similar configuration with transit gateway and DX gateway:
CORRECT:
"Create an AWS transit gateway and add attachments for all of the VPCs. Configure the route tables in the VPCs to send traffic to the transit gateway" is a correct answer.
CORRECT:
"Create an AWS Direct Connect (DX) gateway and attach the DX gateway to a transit gateway. Enable route propagation with BGP" is also a correct answer.
INCORRECT:
"Create VPC peering connections between the VPCs in a fully meshed topology. Configure the route tables in the VPCs to route traffic across the peering connections" is incorrect. This would be highly complex with many connections between VPCs and complex routing configurations. Transit gateway greatly simplifies this solution.
INCORRECT:
"Create an AWS Direct Connect (DX) gateway and associate the DX gateway with a VGW in each VPC. Enable route propagation with BGP" is incorrect. DX gateway is good for cross-Region and cross-Account scenarios. In this scenario with many VPCs in a Region it is better to use a transit gateway.
INCORRECT:
"Create IPSec VPN connections between the VPCs in a fully meshed topology. Configure the route tables in the VPCs to route traffic across the IPSec VPN connections" is incorrect. This is another example of a much more complex solution to the requirements.
References:
https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 13 — ✅ ĐÚNG

<!-- source: T3Q33 · domain: NEW -->

### Câu hỏi

An agricultural company is rolling out thousands of devices that will send environmental data to a data platform. The platform will process and analyze the data and provide information back to researchers. The devices will send 8 KB of data every second and the solution must support near real-time analytics, provide durability for the data, and deliver results to a data warehouse.
Which strategy should a solutions architect use to meet these requirements?

### Các phương án

- **A.** Use Amazon Kinesis Data Firehose to collect the inbound sensor data, analyze the data with Kinesis clients, and save the results to an Amazon RDS instance.
- **B.** Use Amazon Kinesis Data Streams to collect the inbound data, analyze the data with Kinesis clients, and save the results to an Amazon Redshift cluster using Amazon EMR.
- **C.** Use Amazon S3 to collect the inbound device data, analyze the data from Amazon SQS with Kinesis, and save the results to an Amazon Redshift cluster.
- **D.** Use an Amazon API Gateway to put requests into an Amazon SQS queue, analyze the data with an AWS Lambda function, and save the results to an Amazon Redshift cluster using Amazon EMR.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

The solution must support near real-time analytics. For this Amazon Kinesis data streams can be used with clients processing and analyzing the data using Amazon EMR. The solution must also deliver results to a data warehouse and Amazon RedShift is ideal for this purpose.
CORRECT:
"Use Amazon Kinesis Data Streams to collect the inbound data, analyze the data with Kinesis clients, and save the results to an Amazon Redshift cluster using Amazon EMR" is the correct answer.
INCORRECT:
"Use Amazon Kinesis Data Firehose to collect the inbound sensor data, analyze the data with Kinesis clients, and save the results to an Amazon RDS instance" is incorrect. Firehose does not use Kinesis clients; it loads data directly to a destination.
INCORRECT:
"Use Amazon S3 to collect the inbound device data, analyze the data from Amazon SQS with Kinesis, and save the results to an Amazon Redshift cluster" is incorrect. Amazon S3 should not be used for near real-time ingestion of streaming data on this scale. Amazon Kinesis a better fit for this use case. Analyzing with Kinesis from SQS does not make sense either.
INCORRECT:
"Use an Amazon API Gateway to put requests into an Amazon SQS queue, analyze the data with an AWS Lambda function, and save the results to an Amazon Redshift cluster using Amazon EMR" is incorrect. API Gateway should not be used for streaming data and cannot directly put data into an SQS queue.
References:
https://aws.amazon.com/kinesis/data-streams/getting-started/
https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html
https://aws.amazon.com/emr/
https://aws.amazon.com/redshift/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 14 — ❌ SAI

<!-- source: T5Q13 · domain: NEW -->

### Câu hỏi

An application runs on Amazon EC2 instances in a private subnet within an Amazon VPC. The application stores files in a specific Amazon S3 bucket. The files should not traverse the internet and only the application instances should be granted access to save files to the S3 bucket. A gateway endpoint has been created for Amazon S3 and connected to the Amazon VPC.
What additional steps should a Solutions Architect take to meet the stated requirements?

### Các phương án

- **A.** Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Attach a bucket policy to the S3 bucket that grants access only to the VPC endpoint.
- **B.** Attach a bucket policy to the S3 bucket that grants access to the EC2 instances only using the aws:SourceIp condition. Update the VPC route table so only the application EC2 instances can access the VPC endpoint.
- **C.** Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Assign an IAM role to the EC2 instances and attach a policy to the S3 bucket that grants access only to this role.
- **D.** Attach an endpoint policy to the gateway endpoint that restricts access to S3 in the current Region. Attach a bucket policy to the S3 bucket that grants access to ec2.amazonaws.com service only.

> **Bạn chọn:** A
> **Đáp án đúng:** C

### Giải thích

An endpoint policy can be attached to a gateway endpoint that will restrict access to the specific S3 bucket. This means the gateway endpoint can only be used to access that one particular bucket. To restrict access to the bucket to the EC2 instances only an IAM role can be assigned to the instances and then a bucket policy can be added to the bucket that restricts access only to the IAM role. This solution meets all requirements.
The diagram below depicts this configuration:
CORRECT:
"Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Assign an IAM role to the EC2 instances and attach a policy to the S3 bucket that grants access only to this role" is the correct answer.
INCORRECT:
"Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Attach a bucket policy to the S3 bucket that grants access only to the VPC endpoint" is incorrect. This does not restrict access to the specific EC2 instances running the application. This will allow any EC2 instances in the private subnet to access the S3 bucket (if they have S3 permissions).
INCORRECT:
"Attach a bucket policy to the S3 bucket that grants access to the EC2 instances only using the aws:SourceIp condition. Update the VPC route table so only the application EC2 instances can access the VPC endpoint" is incorrect. The aws:SourceIp condition is used for restricting access based on public IP addresses, not private IP addresses.
INCORRECT:
"Attach an endpoint policy to the gateway endpoint that restricts access to S3 in the current Region. Attach a bucket policy to the S3 bucket that grants access to ec2.amazonaws.com service only" is incorrect. This solution does not lock down the specific bucket or the specific application EC2 instances and fails to meet all requirements.
References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html#vpc-endpoint-policies
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 15 — ✅ ĐÚNG

<!-- source: T2Q17 · domain: CI -->

### Câu hỏi

A company operates a large-scale workload with numerous Amazon EC2 instances within a VPC, which includes both public and private subnets. The public subnets are currently configured with a route to an internet gateway for IPv4 traffic (0.0.0.0/0), while the private subnets route IPv4 traffic (0.0.0.0/0) to a NAT gateway. The company now plans to transition its EC2 instances to IPv6, ensuring that instances in private subnets remain inaccessible from the public internet.
To achieve this IPv6 migration while adhering to the specified network accessibility requirements, what actions should the solutions architect take?

### Các phương án

- **A.** Modify the existing VPC to include an Amazon-provided IPv6 CIDR block for the VPC and its subnets. For the public subnets, update the route tables to route IPv6 traffic (::/0) to the internet gateway. For the private subnets, update the route tables to route IPv6 traffic (::/0) to an egress-only internet gateway.
- **B.** Modify the VPC to include an Amazon-provided IPv6 CIDR block for both the VPC and its subnets. For the public and private subnets, adjust the route tables to direct IPv6 traffic (::/0) through the existing NAT gateway.
- **C.** Modify the current VPC configuration by adding a custom IPv6 CIDR block to the VPC and all its subnets. Establish an egress-only internet gateway and update the route tables of the public and private subnets to include a route for IPv6 traffic (::/0) to this gateway.
- **D.** Modify the current VPC configuration by adding a custom IPv6 CIDR block for the VPC and its subnets. Implement a new IPv6-enabled NAT gateway and update the route tables for the private subnets to route IPv6 traffic (::/0) through this new gateway.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Incorporating an Amazon-provided IPv6 CIDR block into the VPC and its subnets enables IPv6 support across the entire network infrastructure.
For public subnets, routing IPv6 traffic (::/0) to the internet gateway allows instances in these subnets to send and receive IPv6 traffic from the internet, maintaining their public accessibility.
For private subnets, using an egress-only internet gateway for IPv6 traffic ensures that instances can initiate outbound IPv6 connections while remaining inaccessible from the public internet.
This dual approach maintains the necessary security posture for private subnet instances and provides the required public internet connectivity for instances in public subnets, aligning with the IPv6 migration objectives.
CORRECT:
"Modify the existing VPC to include an Amazon-provided IPv6 CIDR block for the VPC and its subnets. For the public subnets, update the route tables to route IPv6 traffic (::/0) to the internet gateway. For the private subnets, update the route tables to route IPv6 traffic (::/0) to an egress-only internet gateway" is the correct answer (as explained above.)
INCORRECT:
"Modify the VPC to include an Amazon-provided IPv6 CIDR block for both the VPC and its subnets. For the public and private subnets, adjust the route tables to direct IPv6 traffic (::/0) through the existing NAT gateway" is incorrect.
NAT gateways in AWS do not support IPv6 traffic. Therefore, using the existing NAT gateway for IPv6 traffic is not a viable solution. Also, you cannot use NAT gateways for the instances in the public subnet, they should be directed via the internet gateway.
INCORRECT:
"Modify the current VPC configuration by adding a custom IPv6 CIDR block to the VPC and all its subnets. Establish an egress-only internet gateway and update the route tables of the public and private subnets to include a route for IPv6 traffic (::/0) to this gateway" is incorrect.
While using an egress-only internet gateway is correct, AWS does not allow the association of custom IPv6 CIDR blocks with a VPC. IPv6 CIDR blocks must be provided by Amazon.
INCORRECT:
"Modify the current VPC configuration by adding a custom IPv6 CIDR block for the VPC and its subnets. Implement a new IPv6-enabled NAT gateway and update the route tables for the private subnets to route IPv6 traffic (::/0) through this new gateway" is incorrect.
Currently, AWS NAT gateways do not support IPv6 traffic. Therefore, this option is not feasible for handling IPv6 traffic in AWS.
References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#vpc-ipv6
https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-vpc/

## Câu 16 — ✅ ĐÚNG

<!-- source: T2Q32 · domain: ORG -->

### Câu hỏi

A developer is attempting to access an Amazon S3 bucket in a member account in AWS Organizations. The developer is logged in to the account with user credentials and has received an access denied error with no bucket listed. The developer should have read-only access to all buckets in the account.
A Solutions Architect has reviewed the permissions and found that the developer's IAM user has been granted read-only access to all S3 buckets in the account.
Which additional steps should the Solutions Architect take to troubleshoot the issue? (Select TWO.)

### Các phương án

- **A.** Check the bucket policies for all S3 buckets.
- **B.** Check the ACLs for all S3 buckets.
- **C.** Check the SCPs set at the organizational units (OUs).
- **D.** Check for the permissions boundaries set for the IAM user.
- **E.** Check if an appropriate IAM role is attached to the IAM user.

> **Bạn chọn:** C, D
> **Đáp án đúng:** C, D

### Giải thích

A service control policy (SCP) may have been implemented that limits the API actions that are available for Amazon S3. This will apply to all users in the account regardless of the permissions they have assigned to their user account.
Another potential cause of the issue is that the permissions boundary for the user limits the S3 API actions available to the user. A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries.
CORRECT:
"Check the SCPs set at the organizational units (OUs)" is a correct answer.
CORRECT:
"Check for the permissions boundaries set for the IAM user" is also a correct answer.
INCORRECT:
"Check if an appropriate IAM role is attached to the IAM user" is incorrect. The question states that the user is logged in with a user account so is not assuming a role.
INCORRECT:
"Check the bucket policies for all S3 buckets" is incorrect. The user has not been granted access to any buckets, and the error does not list access denied to any specific bucket. Therefore, it is more likely that the user is not been granted the API action to list the buckets.
INCORRECT:
"Check the ACLs for all S3 buckets" is incorrect. With a bucket ACL the grantee is an AWS account or one of the predefined groups. With an ACL you can grant read/write at the bucket level but list is restricted to the object level so would not apply to the bucket itself. The user has been unable to list any buckets in this case so an ACL is unlikely to be the cause.
References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 17 — ❌ SAI

<!-- source: T5Q24 · domain: CI -->

### Câu hỏi

An application publishes data continuously to Amazon DynamoDB using an AWS Lambda function. The DynamoDB table has an auto scaling policy enabled with the target utilization set to 70%. There are short predictable periods in which a large volume of data is received and this can exceed the typical load by up to 300%. The AWS Lambda function writes
ProvisionedThroughputExceededException messages to Amazon CloudWatch Logs during these times, and some records are redirected to the dead letter queue.
What change should the company make to resolve this issue?

### Các phương án

- **A.** Use Amazon CloudWatch Events to monitor the dead letter queue and invoke a Lambda function to automatically retry failed records.
- **B.** Reduce the DynamoDB table auto scaling policy's target utilization to 50% to provide more resources for peak traffic periods.
- **C.** Use Application Auto Scaling to set a step scaling policy to scale out write capacity on the DynamoDB table when load spikes reach a defined threshold.
- **D.** Use Application Auto Scaling to scale out write capacity on the DynamoDB table based on a schedule.

> **Bạn chọn:** A
> **Đáp án đúng:** D

### Giải thích

The error message received will include the following statement:
You exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes.
This indicates that the table’s capacity is insufficient for the load. The best way to resolve this for a predictable spike in traffic is to configure Application Auto Scaling to scale based on a defined schedule.
Scaling based on a schedule allows you to set your own scaling schedule for predictable load changes. For example, every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can configure Application Auto Scaling to increase capacity on Wednesday and decrease capacity on Friday.
CORRECT:
"Use Application Auto Scaling to scale out write capacity on the DynamoDB table based on a schedule" is the correct answer.
INCORRECT:
"Use Application Auto Scaling to set a step scaling policy to scale out write capacity on the DynamoDB table when load spikes reach a defined threshold" is incorrect. Step scaling is a dynamic scaling type that will scale when the load increases and scales according to the size of the alarm breach. However, this method must respond to alarm breaches and therefore may still result in errors. Scheduled scaling is preferable as it ensures the additional capacity is enabled before the increase in load occurs.
INCORRECT:
"Use Amazon CloudWatch Events to monitor the dead letter queue and invoke a Lambda function to automatically retry failed records" is incorrect. This does not solve the original problem and the records may still fail to be written if the load has not decreased.
INCORRECT:
"Reduce the DynamoDB table auto scaling policy's target utilization to 50% to provide more resources for peak traffic periods" is incorrect. This will still result in an alarm breach if the utilization goes above 50% and is less cost-effective.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 18 — ✅ ĐÚNG

<!-- source: T2Q16 · domain: NEW -->

### Câu hỏi

A company operates a mobile application that enables users to upload images for processing. The app experiences a surge in usage, with thousands of uploads per minute, primarily between 8 AM and 5 PM on weekdays, and minimal activity at other times. Users receive notifications when their image processing is complete.
To effectively manage this variable load and ensure scalable image processing, which three steps should a solutions architect implement? (Select THREE.)

### Các phương án

- **A.** Configure the mobile app to send image uploads directly to Amazon S3. Configure S3 to trigger an Amazon Simple Queue Service (Amazon SQS) standard queue message upon each upload.
- **B.** Implement an AWS Lambda function that initiates image processing in response to messages in the SQS queue.
- **C.** Use Amazon Simple Notification Service (Amazon SNS) to send push notifications to the mobile app once the image processing is finished.
- **D.** Direct image uploads from the mobile app to Amazon S3 and use S3 event notifications to place messages in an Amazon MQ queue for subsequent processing.
- **E.** Activate an S3 Batch Operations job to handle image processing based on queue messages.
- **F.** Use Amazon Simple Email Service (Amazon SES) to send notifications to the mobile app after the completion of image processing tasks.

> **Bạn chọn:** A, B, C
> **Đáp án đúng:** A, B, C

### Giải thích

The combination of Amazon S3 for image uploads, Amazon SQS for queuing, and AWS Lambda for processing forms a highly scalable and efficient serverless architecture, ideal for handling variable workloads. By uploading images directly to Amazon S3, the mobile app leverages S3's robustness and scalability for data storage.
S3's event notification feature then plays a critical role, as it automatically posts messages to an Amazon SQS standard queue upon each image upload. This integration ensures that the image processing workload is queued efficiently, particularly important during peak usage times.
The use of a standard SQS queue is crucial here, as it can handle a high throughput of messages, maintaining the order of image uploads and ensuring that no messages are lost, even under heavy load.
The second part of the solution involves AWS Lambda, which is triggered by messages in the SQS queue to process the images. Lambda's serverless nature allows it to scale automatically with the number of upload requests, providing a cost-effective solution that matches the application's demand patterns.
This setup ensures that image processing starts promptly after each upload, handling the bursts of activity during peak hours without the need for manual scaling. Finally, Amazon SNS is used to notify users upon the completion of image processing.
SNS provides a reliable way to send real-time notifications to the mobile app, enhancing the user experience by promptly informing users when their images are ready.
This end-to-end solution effectively addresses the challenge of variable loads, ensuring that the system remains responsive and cost-efficient regardless of the number of uploads at any given time.
CORRECT:
"Configure the mobile app to send image uploads directly to Amazon S3. Configure S3 to trigger an Amazon Simple Queue Service (Amazon SQS) standard queue message upon each upload" is a correct answer (as explained above.)
CORRECT:
"Implement an AWS Lambda function that initiates image processing in response to messages in the SQS queue" is also a correct answer (as explained above.)
CORRECT:
"Use Amazon Simple Notification Service (Amazon SNS) to send push notifications to the mobile app once the image processing is finished" is also a correct answer (as explained above.)
INCORRECT:
"Direct image uploads from the mobile app to Amazon S3 and use S3 event notifications to place messages in an Amazon MQ queue for subsequent processing" is incorrect.
While Amazon MQ is a message broker service for Apache ActiveMQ and RabbitMQ, it's more complex and typically used for migrating existing message brokers to AWS. For new applications, especially those requiring high scalability, Amazon SQS is generally more appropriate.
INCORRECT:
"Activate an S3 Batch Operations job to handle image processing based on queue messages" is incorrect.
S3 Batch Operations is designed for performing large-scale batch operations on S3 objects, not for real-time, event-driven tasks like image processing. This approach would not provide the necessary responsiveness or scalability for the described use case.
INCORRECT:
"Use Amazon Simple Email Service (Amazon SES) to send notifications to the mobile app after the completion of image processing tasks" is incorrect.
Amazon SES is primarily an email service and would not be the best choice for sending real-time push notifications to a mobile app. Amazon SNS is more suited for this purpose, offering a broader range of notification options including push notifications.
References:
https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html
https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html

## Câu 19 — ✅ ĐÚNG

<!-- source: T4Q19 · domain: CI -->

### Câu hỏi

A company recently migrated a high-traffic eCommerce website to the AWS Cloud. The website is experiencing strong growth. Developers use a private GitHub repository to manage code and the DevOps team use Jenkins for builds and unit testing.
The Developers need to receive notifications when a build does not work and ensure there is no downtime during deployments. It is also required that any changes to production are seamless for users and can be easily rolled back if a significant issue occurs.
A Solutions Architect is finalizing the design for the environment and will use AWS CodePipeline to manage the build and deployment process. What other steps should be taken to meet the requirements?

### Các phương án

- **A.** Use GitHub websockets to trigger the CodePipeline pipeline. Use the Jenkins plugin for AWS CodeBuild to conduct unit testing. Send alerts to an Amazon SNS topic for any bad builds. Deploy in an in-place, all-at-once deployment configuration using AWS CodeDeploy.
- **B.** Use GitHub webhooks to trigger the CodePipeline pipeline. Use the Jenkins plugin for AWS CodeBuild to conduct unit testing. Send alerts to an Amazon SNS topic for any bad builds. Deploy in a blue/green deployment using AWS CodeDeploy.
- **C.** Use GitHub websockets to trigger the CodePipeline pipeline. Use AWS X-Ray for unit testing and static code analysis. Send alerts to an Amazon SNS topic for any bad builds. Deploy in a blue/green deployment using AWS CodeDeploy.
- **D.** Use GitHub webhooks to trigger the CodePipeline pipeline. Use AWS X-Ray for unit testing and static code analysis. Send alerts to an Amazon SNS topic for any bad builds. Deploy in an in-place, all-at-once deployment configuration using AWS CodeDeploy.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

AWS CodePipeline can receive a webhook from GitHub when a change is made to your GitHub repository. Webhooks can tell CodePipeline to initiate a pipeline execution.
You can use the Jenkins plugin for AWS CodeBuild to integrate CodeBuild with your Jenkins build jobs. Instead of sending your build jobs to Jenkins build nodes, you use the plugin to send your build jobs to CodeBuild. This eliminates the need for you to provision, configure, and manage Jenkins build nodes.
SNS is an obvious tool to use for sending notifications and CodeDeploy should use a blue/green deployment strategy. This strategy ensures that updates are seamless and can be easily rolled back if necessary.
CORRECT:
"Use GitHub webhooks to trigger the CodePipeline pipeline. Use the Jenkins plugin for AWS CodeBuild to conduct unit testing. Send alerts to an Amazon SNS topic for any bad builds. Deploy in a blue/green deployment using AWS CodeDeploy" is the correct answer.
INCORRECT:
"Use GitHub webhooks to trigger the CodePipeline pipeline. Use AWS X-Ray for unit testing and static code analysis. Send alerts to an Amazon SNS topic for any bad builds. Deploy in an in-place, all-at-once deployment configuration using AWS CodeDeploy" is incorrect. You cannot use X-Ray for unit testing, it is used for tracing. Also, an in-place, all-at-once deployment strategy makes it difficult to roll back.
INCORRECT:
"Use GitHub websockets to trigger the CodePipeline pipeline. Use the Jenkins plugin for AWS CodeBuild to conduct unit testing. Send alerts to an Amazon SNS topic for any bad builds. Deploy in an in-place, all-at-once deployment configuration using AWS CodeDeploy" is incorrect. You cannot use websockets to trigger CodePipeline, webhooks must be used.
INCORRECT:
"Use GitHub websockets to trigger the CodePipeline pipeline. Use AWS X-Ray for unit testing and static code analysis. Send alerts to an Amazon SNS topic for any bad builds. Deploy in a blue/green deployment using AWS CodeDeploy" is incorrect. You cannot use websockets to trigger CodePipeline, webhooks must be used.
References:
https://aws.amazon.com/about-aws/whats-new/2018/05/aws-codepipeline-supports-push-events-from-github-via-webhooks/
https://docs.aws.amazon.com/codebuild/latest/userguide/jenkins-plugin.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-developer-tools-sap/

## Câu 20 — ✅ ĐÚNG

<!-- source: T5Q17 · domain: MIG -->

### Câu hỏi

A company is planning to migrate a containerized application to Amazon ECS. The company wishes to reduce instance costs as much as possible whilst reducing the probability of service interruptions. How should a Solutions Architect configure the solution?

### Các phương án

- **A.** Use Amazon ECS Spot instances and configure Spot Instance Draining.
- **B.** Use Amazon ECS Cluster Auto Scaling (CAS) and configure a warm-up time.
- **C.** Use Amazon ECS Reserved instances and configure termination protection.
- **D.** Use Amazon ECS with Application Auto Scaling and suspend dynamic scaling.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Spot instances are the lowest cost option but can be terminated by AWS at any time if they need the capacity back or the maximum configured price is exceeded. This can lead to service interruptions as the underlying container instances are terminated.
Automated Spot Instance Draining will automatically place Spot instances in “DRAINING” state upon the receipt of two minute interruption notice. ECS tasks running on Spot instances will automatically be triggered for shutdown before the instance terminates and replacement tasks will be scheduled elsewhere on the cluster. No new ECS service tasks will be started on the instances once the termination process has begun.
ECS takes over the coordination of termination of tasks with the termination of the underlying EC2 instance using the inherent instance “DRAINING” functionality. The managed termination, scheduling of replacement tasks and graceful termination of the LB connections reduces the probability of service interruptions. This makes it easier for customers to use Spot instances as part of their ECS cluster.
CORRECT:
"Use Amazon ECS Spot instances and configure Spot Instance Draining" is the correct answer.
INCORRECT:
"Use Amazon ECS Cluster Auto Scaling (CAS) and configure a warm-up time" is incorrect. The warm-up time defines the number of seconds it takes for a newly launched instance to warm up and is not relevant here.
INCORRECT:
"Use Amazon ECS Reserved instances and configure termination protection" is incorrect. Termination protection with RIs will provide cost savings and protection from service interruptions but it is not the lowest cost option.
INCORRECT:
"Use Amazon ECS with Application Auto Scaling and suspend dynamic scaling" is incorrect. This answer does not provide a solution for lowering instance costs and suspension of dynamic scaling is going to prevent scale-in and scale-out events from occurring.
References:
https://aws.amazon.com/about-aws/whats-new/2019/09/amazon-ecs-supports-automated-draining-for-spot-instances-running-ecs-services/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 21 — ✅ ĐÚNG

<!-- source: T5Q2 · domain: MIG -->

### Câu hỏi

A company runs a high performance computing (HPC) application in an on-premises data center. The solution consists of a 10-node cluster running Linux with high-speed inter-node connectivity. The company is planning to migrate the application to the AWS Cloud. A Solutions Architect needs to design the solution architecture on AWS to ensure optimum performance for the HPC cluster.
Which combination of steps will meet these requirements? (Select TWO.)

### Các phương án

- **A.** Deploy instances across multiple Availability Zones.
- **B.** Deploy Amazon EC2 instances in a placement group.
- **C.** Use Amazon EC2 instances that support Elastic Fabric Adapter (EFA).
- **D.** Use Amazon EC2 instances that support burstable performance.
- **E.** Deploy Amazon EC2 instances in an Auto Scaling group.

> **Bạn chọn:** B, C
> **Đáp án đúng:** B, C

### Giải thích

High performance computing applications require that the nodes have very high-bandwidth, low-latency connections between the nodes in the cluster. AWS recommend that the instances are placed in a placement group.
A cluster placement group should be used as it packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the low-latency network performance necessary for tightly-coupled node-to-node communication that is typical of HPC applications.
Elastic Fabric Adapter (EFA) is a network interface for Amazon EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS. Its custom-built operating system (OS) bypass hardware interface enhances the performance of inter-instance communications, which is critical to scaling these applications.
CORRECT:
"Deploy Amazon EC2 instances in a placement group" is a correct answer.
CORRECT:
"Use Amazon EC2 instances that support Elastic Fabric Adapter (EFA)" is also a correct answer.
INCORRECT:
"Deploy instances across multiple Availability Zones" is incorrect. To ensure the best inter-node connectivity the instances should be deployed in a single AZ.
INCORRECT:
"Use Amazon EC2 instances that support burstable performance" is incorrect. This is not a recommended solution for optimum performance of HPC applications.
INCORRECT:
"Deploy Amazon EC2 instances in an Auto Scaling group" is incorrect. This does not enable better performance.
References:
https://aws.amazon.com/hpc/efa/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html
https://aws.amazon.com/hpc/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 22 — ❌ SAI

<!-- source: T6Q5 · domain: NEW -->

### Câu hỏi

A company is planning to launch a new web application on AWS using a fully serverless design. The website will be used by global customers and should be highly responsive and offer minimal latency. The design should be highly availably and include baseline DDoS protections against spikes in traffic. The users will login in to the web application using social IdPs such as Google, and Amazon.
How can the design requirements be met?

### Các phương án

- **A.** Build an API using Docker containers running on Amazon ECS behind an Amazon CloudFront distribution. Use AWS Secrets Manager to provide user management authentication functions.
- **B.** Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an Amazon CloudFront distribution with the S3 bucket as the origin. Use Amazon Cognito to provide user management authentication functions.
- **C.** Build an API using Docker containers running on AWS Fargate in multiple Regions behind Application Load Balancers. Use an Amazon Route 53 latency-based routing policy. Use Amazon Cognito to provide user management authentication functions.
- **D.** Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an AWS WAF Web ACL and attach it for DDoS attack mitigation. Use Amazon Cognito to provide user management authentication functions.

> **Bạn chọn:** D
> **Đáp án đúng:** B

### Giải thích

A serverless web application can be created using a REST API running on API Gateway, a Lambda function, and S3 to store static assets. CloudFront can then be used to cache the S3 assets for lower latency for the global user base. CloudFront also offers basic DDoS protections with AWS Shield standard offered for free for use with CloudFront. Amazon Cognito is ideal for implementing user authentication for this type of application and you can integrate with social IdPs.
CORRECT:
"Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an Amazon CloudFront distribution with the S3 bucket as the origin. Use Amazon Cognito to provide user management authentication functions" is the correct answer.
INCORRECT:
"Build an API using Docker containers running on Amazon ECS behind an Amazon CloudFront distribution. Use AWS Secrets Manager to provide user management authentication functions" is incorrect. You cannot put CloudFront directly in front of ECS, you must point it to a load balancer. Secrets Manager is not an authentication service, it is used for securely storing secrets such as passwords.
INCORRECT:
"Build an API using Docker containers running on AWS Fargate in multiple Regions behind Application Load Balancers. Use an Amazon Route 53 latency-based routing policy. Use Amazon Cognito to provide user management authentication functions" is incorrect. This is a serverless design but it is not the best design. Using Lambda functions and API gateway will likely be more cost-effective and scale more seamlessly. Also CloudFront is a better way to get assets such as media files closer to users and cheaper than hosting the solution in many Regions.
INCORRECT:
"Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an AWS WAF Web ACL and attach it for DDoS attack mitigation. Use Amazon Cognito to provide user management authentication functions" is incorrect. A WAF Web ACL will not provide DDoS attack mitigation, use AWS Shield instead or use CloudFront with WAF.
References:
https://aws.amazon.com/shield/
https://aws.amazon.com/serverless/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 23 — ❌ SAI

<!-- source: T3Q24 · domain: ORG -->

### Câu hỏi

A company is in the process of migrating applications to AWS using multiple accounts in AWS Organizations . The management account is at the root of the Organizations hierarchy. Business units each have different accounts and requirements for the services they need to use. The security team needs to implement controls across all accounts to prohibit many AWS services. In some cases a business unit may have a valid exception to these controls and this must be achievable.
Which solution will meet these requirements with minimal optional overhead?

### Các phương án

- **A.** Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level. For any specific exceptions for an OU, create a new SCP for that OU and add the required AWS services to the allow list.
- **B.** Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level and each OU. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions, modify the SCP attached to that OU, and add the required AWS services to the allow list.
- **C.** Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at each OU level. Leave the default AWS managed SCP attached to the root level and all OUs. For accounts that require specific exceptions, create an OU under root and attach an SCP the denies fewer services.
- **D.** Use an SCP in Organizations to implement an allow list of AWS services. Apply this SCP at the root level. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions for an OU, modify the SCP attached to that OU, and add the required AWS services to the allow list.

> **Bạn chọn:** D
> **Đáp án đúng:** C

### Giải thích

AWS Organizations Service Control Policies (SCPs) can be used to control the maximum available permissions in an AWS account. The permissions flow through a hierarchy from the root to all entities beneath. With a deny list strategy a default SCP allows all services and deny lists must be implemented for any specific services that must be restricted.
In this scenario using a deny list strategy will mean the AWS managed SCP at the root level and all OUs will allow all services for all business units. An SCP can then be defined that prohibits AWS services and this can be applied to all OUs.
When an exception is required, an OU must be created under root with an SCP that has fewer restrictions. This OU must be under root so it is not part of the hierarchy of OUs that have denies, as a deny at a higher level always overrides an allow.
The diagram below depicts a scenario with a deny list strategy and SCPs applied to multiple OUs/accounts:
CORRECT:
"Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at each OU level. Leave the default AWS managed SCP attached to the root level and all OUs. For accounts that require specific exceptions, create an OU under root and attach an SCP the denies fewer services" is the correct answer.
INCORRECT:
"Use an SCP in Organizations to implement an allow list of AWS services. Apply this SCP at the root level. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions for an OU, modify the SCP attached to that OU, and add the required AWS services to the allow list" is incorrect. You cannot modify an SCP that is applied to multiple OUs at one child OU. It must be edited in one place.
INCORRECT:
"Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level. For any specific exceptions for an OU, create a new SCP for that OU and add the required AWS services to the allow list" is incorrect. This will not work as there is an explicit deny at a higher level and this will override an allow at any level beneath.
INCORRECT:
"Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level and each OU. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions, modify the SCP attached to that OU, and add the required AWS services to the allow list" is incorrect. You cannot modify an SCP that is applied to multiple OUs at one child OU. It must be edited in one place. This will also not work as there is an explicit deny at a higher level and this will override an allow at any level beneath.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_auth.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 24 — ✅ ĐÚNG

<!-- source: T2Q14 · domain: NEW -->

### Câu hỏi

A financial services company is implementing AWS Lambda functions to connect to an Amazon Aurora MySQL database cluster. These Lambda functions will be utilized in both a development environment for testing and a live production environment.
The company's priority is to ensure that database credentials are not hardcoded within the Lambda functions and that there's a system in place for the automated rotation of passwords.
Which solution will fulfill these requirements?

### Các phương án

- **A.** Utilize AWS Systems Manager Parameter Store to manage database credentials for both the development and production environments. Encrypt these credentials using an AWS KMS key. Modify the Lambda functions' code to retrieve credentials from the Parameter Store using the AWS SDK for JavaScript. Assign appropriate IAM roles to the Lambda functions for accessing the Parameter Store.
- **B.** Configure AWS Secrets Manager for managing the database credentials, creating separate secret keys for the development and production environments. Enable automatic secret rotation. Pass the Secrets Manager secret ARNs to the Lambda functions through environment variables. Assign appropriate IAM roles to the Lambda functions for accessing the secrets.
- **C.** Save the database credentials in AWS KMS for both environments and enable automatic key rotation. Use environment variables in the Lambda functions to reference the stored AWS KMS credentials. Assign appropriate IAM roles to the Lambda functions for accessing AWS KMS.
- **D.** Establish distinct Amazon S3 buckets for development and production environments. Enable server-side encryption using AWS KMS keys (SSE-KMS) for both buckets. Implement a file naming convention that allows Lambda functions to dynamically fetch the appropriate credentials based on their environment. Ensure the execution roles of the Lambda functions have the necessary permissions to access the respective S3 buckets.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

AWS Secrets Manager is specifically designed to handle secrets like database credentials. It provides built-in support for rotating credentials safely and seamlessly, without the need for embedded credentials in the application code.
Using separate secrets for different environments (development and production) ensures that the credentials are environment-specific, enhancing security.
The use of environment variables to pass Secrets Manager ARNs to Lambda functions is a secure and efficient way to provide access to the required credentials without hardcoding them.
CORRECT:
"Configure AWS Secrets Manager for managing the database credentials, creating separate secret keys for the development and production environments. Enable automatic secret rotation. Pass the Secrets Manager secret ARNs to the Lambda functions through environment variables. Assign appropriate IAM roles to the Lambda functions for accessing the secrets" is the correct answer (as explained above.)
INCORRECT:
"Utilize AWS Systems Manager Parameter Store to manage database credentials for both the development and production environments. Encrypt these credentials using an AWS KMS key. Modify the Lambda functions' code to retrieve credentials from the Parameter Store using the AWS SDK for JavaScript. Assign appropriate IAM roles to the Lambda functions for accessing the Parameter Store" is incorrect.
While the AWS Systems Manager Parameter Store is a viable option for storing configuration data and secrets, it does not have the built-in automatic rotation feature for secrets, which is crucial in this scenario.
INCORRECT:
"Save the database credentials in AWS KMS for both environments and enable automatic key rotation. Use environment variables in the Lambda functions to reference the stored AWS KMS credentials. Assign appropriate IAM roles to the Lambda functions for accessing AWS KMS" is incorrect.
AWS KMS is primarily used for creating and managing cryptographic keys and is not suited for storing application-level secrets like database credentials. Additionally, KMS does not offer a feature to rotate database credentials.
INCORRECT:
"Establish distinct Amazon S3 buckets for development and production environments. Enable server-side encryption using AWS KMS keys (SSE-KMS) for both buckets. Implement a file naming convention that allows Lambda functions to dynamically fetch the appropriate credentials based on their environment. Ensure the execution roles of the Lambda functions have the necessary permissions to access the respective S3 buckets" is incorrect.
Using S3 buckets to store credentials is not a recommended practice. This approach can lead to security risks as S3 is primarily for object storage and does not have the built-in capability to manage secrets or rotate them securely. Furthermore, it complicates the management and retrieval of credentials, especially when compared to services like AWS Secrets Manager and Parameter Store.
References:
https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-secrets-manager/

## Câu 25 — ✅ ĐÚNG

<!-- source: T2Q8 · domain: NEW -->

### Câu hỏi

A serverless application is using AWS Lambda and Amazon DynamoDB and developers have finalized an update to the Lambda function code. AWS CodeDeploy will be used to deploy new versions of the function. Updates to the Lambda function should be delivered to a subset of users before deploying the changes to all users. The update process should also be easy to abort and rollback if necessary.
Which CodeDeploy configuration should the solutions architect use?

### Các phương án

- **A.** A blue/green deployment
- **B.** A linear deployment
- **C.** A canary deployment
- **D.** An all-at-once deployment

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

When using AWS CodeDeploy with AWS Lambda there are three ways traffic can be shifted during a deployment:
Canary: Traffic is shifted in two increments. You can choose from predefined canary options that specify the percentage of traffic shifted to your updated Amazon ECS task set / Lambda function in the first increment and the interval, in minutes, before the remaining traffic is shifted in the second increment.
Linear: Traffic is shifted in equal increments with an equal number of minutes between each increment. You can choose from predefined linear options that specify the percentage of traffic shifted in each increment and the number of minutes between each increment.
All-at-once: All traffic is shifted from the original Lambda function to the updated Lambda function all at once.
Blue/green: Traffic is shifted from one version of a Lambda function to a new version of the same Lambda function.
All AWS Lambda and deployments are blue/green, as a new version of the function is created and traffic is shifted using one of the available options. Canary is the best choice if you just want to shift a percentage of traffic across to a subset of users and then shift the remainder.
CORRECT:
"A canary deployment" is the correct answer.
INCORRECT:
"A blue/green deployment" is incorrect. All Lambda deployments are blue/green as you cannot do in-place upgrades.
INCORRECT:
"A linear deployment" is incorrect. Linear shifts in multiple increments using a percentage per interval. The scenario asks for a 2-step process.
INCORRECT:
"An all-at-once deployment" is incorrect. This simply shifts all traffic at once and does not deploy to a subset of users first.
References:
https://docs.aws.amazon.com/whitepapers/latest/modern-application-development-on-aws/canary-deployments-to-aws-lambda.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-developer-tools-sap/

## Câu 26 — ✅ ĐÚNG

<!-- source: T5Q5 · domain: CI -->

### Câu hỏi

A manufacturing company collects data from IoT devices in JSON format. The data is collected, transformed, and stored in a data warehouse for analysis using an analytics tool that uses ODBC. The performance of the current solution suffers under high loads due to insufficient compute capacity and incoming data is often lost.
The application will be migrated to AWS. The solution must support the current analytics tool, resolve the compute constraints, and be cost-effective.
Which solution meets these requirements?

### Các phương án

- **A.** Re-architect the application. Load the data into Amazon S3. Use AWS Lambda to transform the data. Create an Amazon DynamoDB global table across two Regions to store the data and use Amazon Elasticsearch to query the data.
- **B.** Replatform the application. Use Amazon API Gateway for data ingestion. Use AWS Lambda to transform the JSON data. Create an Amazon Aurora PostgreSQL DB cluster with an Aurora Replica in another Availability Zone. Use Amazon QuickSight to generate reports and visualize data.
- **C.** Re-architect the application. Load the data into Amazon S3. Use AWS Glue to transform the data. Store the table schema in an AWS Glue Data Catalog. Use Amazon Athena to query the data.
- **D.** Re-architect the application. Load the data into Amazon S3. Use Amazon Kinesis Data Analytics to transform the data. Create an external schema in an AWS Glue Data Catalog. Use Amazon Redshift Spectrum to query the data.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

There are multiple options that work here but we must select the most cost-effective and resilient solution that also resolves the performance constraints. Using a fully serverless architecture meets all of these goals.
The JSON data can be initially stored in Amazon S3 and then AWS Glue can be directed at the source bucket to run transformation on the data and store the results in another S3 bucket. The Glue Data Catalog is used to store metadata about the data in the S3 data lake.
Athena can be used to query the transformed data in the S3 bucket. The Amazon Athena ODBC driver can be used to connect to Athena from the existing analytics tool.
The architecture in the diagram below shows a similar solution using an AWS IoT Analytics channel. This also includes AWS Glue and Athena. Instead of using QuickSight to visualize data, the solution in the question scenario uses a third-party analytics tool connecting over ODBC.
CORRECT:
"Re-architect the application. Load the data into Amazon S3. Use AWS Glue to transform the data. Store the table schema in an AWS Glue Data Catalog. Use Amazon Athena to query the data" is the correct answer.
INCORRECT:
"Replatform the application. Use Amazon API Gateway for data ingestion. Use AWS Lambda to transform the JSON data. Create an Amazon Aurora PostgreSQL DB cluster with an Aurora Replica in another Availability Zone. Use Amazon QuickSight to generate reports and visualize data" is incorrect. This is a workable solution but is not as cost-effective as using a fully serverless architecture.
INCORRECT:
"Re-architect the application. Load the data into Amazon S3. Use AWS Lambda to transform the data. Create an Amazon DynamoDB global table across two Regions to store the data and use Amazon Elasticsearch to query the data" is incorrect. This is another workable solution and you can connect to Elasticsearch using ODBC. However, the DynamoDB global table introduces additional cost and is unnecessary in this solution.
INCORRECT:
"Re-architect the application. Load the data into Amazon S3. Use Amazon Kinesis Data Analytics to transform the data. Create an external schema in an AWS Glue Data Catalog. Use Amazon Redshift Spectrum to query the data" is incorrect. There is no mention of where the data would be output to, and this would not the most cost-effective solution.
References:
https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc.html
https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

## Câu 27 — ✅ ĐÚNG

<!-- source: T3Q31 · domain: CI -->

### Câu hỏi

A company has experienced issues updating an AWS Lambda function that is deployed using an AWS CloudFormation stack. The issues have resulted in outages that affected large numbers of customers. A Solutions Architect must adjust the deployment process to support a canary release strategy. Invocation traffic should be routed based on specified weights.
Which solution will meet these requirements?

### Các phương án

- **A.** Create an alias for new versions of the Lambda function. Use the AWS CLI update-alias command with the routing-config parameter to distribute the load.
- **B.** Deploy the application into a new CloudFormation stack. Use an Amazon Route 53 weighted routing policy to distribute the load.
- **C.** Create a version for every new update to the Lambda function code. Use the AWS CLI update-function-configuration command with the routing-config parameter to distribute the load.
- **D.** Use AWS CodeDeploy to deploy using the CodeDeployDefault.HalfAtATime deployment configuration to distribute the load.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

With the introduction of alias traffic shifting, it is now possible to trivially implement canary deployments of Lambda functions. By updating additional version weights on an alias, invocation traffic is routed to the new function versions based on the weight specified.
Detailed CloudWatch metrics for the alias and version can be analyzed during the deployment, or other health checks performed, to ensure that the new version is healthy before proceeding.
The following example AWS CLI command points an alias to a new version, weighted at 5% (original version at 95% of traffic):
aws lambda update-alias --function-name myfunction --name myalias --routing-config '{"AdditionalVersionWeights" : {"2" : 0.05} }'
CORRECT:
"Create an alias for new versions of the Lambda function. Use the AWS CLI update-alias command with the routing-config parameter to distribute the load" is the correct answer.
INCORRECT:
"Create a version for every new update to the Lambda function code. Use the AWS CLI update-function-configuration command with the routing-config parameter to distribute the load" is incorrect. A Lambda alias should be used to point to a new version. A Lambda alias is like a pointer to a specific function version. Users can access the function version using the alias Amazon Resource Name (ARN). The alias in the used in the CLI command. This method is used as you can change the version that is associated with the alias easily.
INCORRECT:
"Deploy the application into a new CloudFormation stack. Use an Amazon Route 53 weighted routing policy to distribute the load" is incorrect. Route 53 is not a method of doing a canary release, the solution should use Lambda aliases with the CLI.
INCORRECT:
"Use AWS CodeDeploy to deploy using the CodeDeployDefault.HalfAtATime deployment configuration to distribute the load" is incorrect. This CodeDeploy configuration is used for in-place and blue/green migrations but not for canary releases.
References:
https://aws.amazon.com/blogs/compute/implementing-canary-deployments-of-aws-lambda-functions-with-alias-traffic-shifting/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 28 — ❌ SAI

<!-- source: T4Q12 · domain: ORG · flagged -->

### Câu hỏi

A company is creating a multi-account structure using AWS Organizations. The accounts will include the Management account, Production account, and Development account. The company requires auditing for all API actions across accounts. A Solutions Architect is advising the company on how to configure the accounts. Which of the following recommendations should the Solutions Architect make? (Select TWO.)

### Các phương án

- **A.** Enable AWS CloudTrail and keep all CloudTrail trails and logs in the management account.
- **B.** Create user accounts in the Production and Development accounts.
- **C.** Enable AWS CloudTrail and keep all CloudTrail trails and logs within each account.
- **D.** Create user accounts in the Management account and use cross-account access to access resources.
- **E.** Create all resources in the Management account and grant access to the Production and Development accounts.

> **Bạn chọn:** A, E
> **Đáp án đúng:** A, B

### Giải thích

AWS recommends that you use the management account and its users and roles only for tasks that can be performed only by that account. Store all of your AWS resources in
other
AWS accounts in the organization and keep them out of the management account. The one exception is that AWS does recommend that you enable AWS CloudTrail and keep relevant CloudTrail trails and logs in the management account.
One important reason to keep your resources in other accounts is because Organizations service control policies (SCPs) do not work to restrict any users or roles in the management account.
Separating your resources from your management account also help you to understand the charges on your invoices.
CORRECT:
"Enable AWS CloudTrail and keep all CloudTrail trails and logs in the management account" is a correct answer.
CORRECT:
"Create user accounts in the Production and Development accounts" is also a correct answer.
INCORRECT:
"Enable AWS CloudTrail and keep all CloudTrail trails and logs within each account" is incorrect. AWS recommends that you centralize this data to the management account.
INCORRECT:
"Create user accounts in the Management account and use cross-account access to access resources" is incorrect. Because user accounts in the management account are not restricted by SCPs, this is not a best practice.
INCORRECT:
"Create all resources in the Management account and grant access to the Production and Development accounts" is incorrect. Resources should be created in the relevant accounts (Production/Development), you cannot just grant access and have them in the management account.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 29 — ✅ ĐÚNG

<!-- source: T5Q20 · domain: CI -->

### Câu hỏi

A company stores highly confidential information in an Amazon S3 bucket. The security team have evaluated the security of the configuration and have come up with some new requirements that must be met. The security team now requires the ability to identify the IP addresses that make requests to the bucket to be able to identify malicious actors. They additionally require that any changes to the bucket policy are automatically remediated and alerts of these changes are sent to their team members.
Which strategies should a Solutions Architect use to meet these requirements?

### Các phương án

- **A.** Use Amazon CloudWatch Logs with the Amazon Athena connector to identify the IP addresses in Amazon S3 requests. Use CloudWatch Events rules with AWS Lambda to automatically remediate S3 bucket policy changes. Configure alerting with Amazon SNS.
- **B.** Use Amazon Macie with to identify the IP addresses in Amazon S3 requests. Use AWS Lambda with Macie to automatically remediate S3 bucket policy changes. Use Macie automatic alerting capabilities for alerts.
- **C.** Create an AWS CloudTrail trail and log management events. Use CloudWatch Events rules with AWS Lambda to automatically remediate S3 bucket policy changes. Configure alerting with Amazon SNS.
- **D.** Identify the IP addresses in Amazon S3 requests with Amazon S3 access logs and Amazon Athena. Use AWS Config with Auto Remediation to remediate any changes to S3 bucket policies. Configure alerting with AWS Config and Amazon SNS.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Amazon S3 server access logging provides detailed records for the requests that are made to a bucket. This includes the IP addresses that issued the requests. S3 stores server access logs as objects in an S3 bucket. Athena can then be used to query Amazon S3 access logs using SQL queries.
The AWS Config Auto Remediation feature automatically remediates non-compliant resources evaluated by AWS Config rules. You can associate remediation actions with AWS Config rules and choose to execute them automatically to address non-compliant resources without manual intervention. An AWS Config rule can be applied to identify and remediate any unauthorized changes to the policy associated with the S3 bucket. Amazon SNS can be integrated as a destination for alerts.
CORRECT:
"Identify the IP addresses in Amazon S3 requests with Amazon S3 access logs and Amazon Athena. Use AWS Config with Auto Remediation to remediate any changes to S3 bucket policies. Configure alerting with AWS Config and Amazon SNS" is the correct answer.
INCORRECT:
"Use Amazon CloudWatch Logs with the Amazon Athena connector to identify the IP addresses in Amazon S3 requests. Use CloudWatch Events rules with AWS Lambda to automatically remediate S3 bucket policy changes. Configure alerting with Amazon SNS" is incorrect. CloudWatch Logs will not contain information about the IP addresses that issued requests to Amazon S3, AWS CloudTrail should be used instead.
INCORRECT:
"Use Amazon Macie with to identify the IP addresses in Amazon S3 requests. Use AWS Lambda with Macie to automatically remediate S3 bucket policy changes. Use Macie automatic alerting capabilities for alerts" is incorrect. Macie is used to identify personally identifiable information rather than IP addresses.
INCORRECT:
"Create an AWS CloudTrail trail and log management events. Use CloudWatch Events rules with AWS Lambda to automatically remediate S3 bucket policy changes. Configure alerting with Amazon SNS" is incorrect. CloudTrail can be used to identify object-level actions but you must enable object-level events, not management events.
References:
https://aws.amazon.com/blogs/mt/aws-config-auto-remediation-s3-compliance/
https://docs.aws.amazon.com/AmazonS3/latest/dev/using-s3-access-logs-to-identify-requests.html#querying-s3-access-logs-for-requests
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 30 — ✅ ĐÚNG

<!-- source: T1Q30 · domain: CI -->

### Câu hỏi

A company has deployed an application that uses an Amazon DynamoDB table and the user base has increased significantly. Users have reported poor response times during busy periods but no error pages have been generated. The application uses Amazon DynamoDB in read-only mode. The operations team has determined that the issue relates to ProvisionedThroughputExceeded exceptions in the application logs when doing Scan and read operations.
A Solutions Architect has been tasked with improving application performance. Which solutions will meet these requirements whilst MINIMIZING changes to the application? (Select TWO.)

### Các phương án

- **A.** Enable adaptive capacity for the DynamoDB table to minimize throttling due to throughput exceptions.
- **B.** Enable DynamoDB Auto Scaling to manage the throughput capacity as table traffic increases. Set the upper and lower limits to control costs and set a target utilization based on the peak usage.
- **C.** Provision an Amazon ElastiCache for Redis cluster. The cluster should be provisioned with enough shards to handle the peak application load.
- **D.** Provision a DynamoDB Accelerator (DAX) cluster with the correct number and type of nodes. Tune the item and query cache configuration for an optimal user experience.
- **E.** Include error retries and exponential backoffs in the application code to handle throttling errors and reduce load during periods of high requests.

> **Bạn chọn:** B, D
> **Đáp án đúng:** B, D

### Giải thích

When a ProvisionedThroughputExceeded error is generated it means that insufficient throughput has been enabled on the table. In this case that would be insufficient read capacity units (RCUs). Enabling DynamoDB Auto Scaling will ensure that the RCUs are adjusted based on load.
You configure Auto Scaling by specifying the minimum and maximum capacity units and the target utilization as you can see in the image below:
Another great addition to the solution is to create an Amazon DynamoDB Accelerator (DAX) cluster. DAX is a caching solution for DynamoDB that can be placed in front of the database. This will provide much improved read performance without any application changes.
CORRECT:
"Enable DynamoDB Auto Scaling to manage the throughput capacity as table traffic increases. Set the upper and lower limits to control costs and set a target utilization based on the peak usage" is a correct answer.
CORRECT:
"Provision a DynamoDB Accelerator (DAX) cluster with the correct number and type of nodes. Tune the item and query cache configuration for an optimal user experience" is also a correct answer.
INCORRECT:
"Enable adaptive capacity for the DynamoDB table to minimize throttling due to throughput exceptions" is incorrect. Adaptive capacity is enabled automatically for every DynamoDB table, at no additional cost. You don't need to explicitly enable or disable it.
INCORRECT:
"Provision an Amazon ElastiCache for Redis cluster. The cluster should be provisioned with enough shards to handle the peak application load" is incorrect. DAX is a better solution for a DynamoDB table as it works without any code changes which is preferred in this scenario.
INCORRECT:
"Include error retries and exponential backoffs in the application code to handle throttling errors and reduce load during periods of high requests" is incorrect. This option also requires application code changes so should be avoided in this scenario.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 31 — ✅ ĐÚNG

<!-- source: T3Q2 · domain: MIG -->

### Câu hỏi

A Solutions Architect is working on refactoring a monolithic application into a modern application design that will be deployed in the AWS Cloud. A CI/CD pipeline should be used that supports the modern design and allows for multiple releases every hour. The pipeline should also ensure that changes can be quickly rolled back if required.
Which design will meet these requirements?

### Các phương án

- **A.** Deploy a CI/CD pipeline that incorporates AMIs to contain the application and their configurations. Deploy the application by replacing Amazon EC2 instances.
- **B.** Use AWS Elastic Beanstalk and create a secondary environment configured as a deployment target for the CI/CD pipeline. To deploy, swap the staging and production environment URLs.
- **C.** Use AWS CloudFormation StackSets to create production and staging stacks. Update the staging stack and use Amazon Route 53 weighted routing to point to the StackSet endpoint address.
- **D.** Package updates into an Amazon EC2 AMI and update the Auto Scaling group to use the new AMI. Terminate existing instances in staged approach to cause launches using the new AMI.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

With AWS Elastic Beanstalk you can perform a blue/green deployment, where you deploy the new version to a separate environment, and then swap CNAMEs of the two environments to redirect traffic to the new version instantly.
This approach meets all requirements as it is possible to make multiple updates each hour and it’s easy to swap the CNAMEs (URLs) back again in the case of issues occurring.
The image below shows the management console view where you can swap the environment URLs:
CORRECT:
"Use AWS Elastic Beanstalk and create a secondary environment configured as a deployment target for the CI/CD pipeline. To deploy, swap the staging and production environment URLs" is the correct answer.
INCORRECT:
"Use AWS CloudFormation StackSets to create production and staging stacks. Update the staging stack and use Amazon Route 53 weighted routing to point to the StackSet endpoint address" is incorrect. StackSets are used for deploying a stack to different accounts or Regions. There is no StackSet address that you can point users to.
INCORRECT:
"Package updates into an Amazon EC2 AMI and update the Auto Scaling group to use the new AMI. Terminate existing instances in staged approach to cause launches using the new AMI" is incorrect. This is not an approach you can take without a lot of manual effort and it will also cause disruption and potential downtime. This approach also makes it hard to roll back.
INCORRECT:
"Deploy a CI/CD pipeline that incorporates AMIs to contain the application and their configurations. Deploy the application by replacing Amazon EC2 instances" is incorrect. This approach also does not allow an easy method of rolling back as EC2 instances have been replaced.
References:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 32 — ✅ ĐÚNG

<!-- source: T3Q13 · domain: ORG -->

### Câu hỏi

A media advertising company currently has resources hosted in two AWS accounts: Management and Production. DNS records are stored in a private hosted zone using Amazon Route 53 in the Management account. The Production account is used for applications and databases.
The company has deployed a two-tier application in a new VPC. To simplify the configuration, the database.company.com CNAME record set for the Amazon RDS endpoint was created in a private hosted zone for Amazon Route 53.
While deploying, the application failed to start. Troubleshooting revealed that database.company.com is not resolvable within the Amazon EC2 instance. The solutions architect confirmed that the record set was created correctly in Route 53.
Which combination of steps should the solutions architect take to resolve this issue? (Select TWO.)

### Các phương án

- **A.** Deploy the database on a separate EC2 instance in the new VPC. Create a record set for the instance's private IP in the private hosted zone.
- **B.** Use SSH to connect to the application tier EC2 instance. Add an RDS endpoint IP address to the /etc/resolv.conf file.
- **C.** Create an authorization to associate the private hosted zone in the Management account with the new VPC in the Production account.
- **D.** Create a private hosted zone for the example.com domain in the Production account. Configure Route 53 replication between AWS accounts.
- **E.** Associate a new VPC in the Production account with a hosted zone in the Management account. Delete the association authorization in the Management account.

> **Bạn chọn:** C, E
> **Đáp án đúng:** C, E

### Giải thích

Below is the sequence of steps for achieving this:
- Connect to an Amazon Elastic Compute Cloud (Amazon EC2) instance in the Management account.
- Run the following commands:
- pip3 install awscli --upgrade –user
- aws route53 list-hosted-zones (to find the hosted zone to be linked)
- aws route53 create-vpc-association-authorization --hosted-zone-id <hosted-zone-id> --vpc VPCRegion=<region>,VPCId=<vpc-id> --region <Region>
-
Connect to an Amazon EC2 instance in target account
CORRECT:
"Create an authorization to associate the private hosted zone in the Management account with the new VPC in the Production account" is a correct answer (as explained above.)
CORRECT:
"Associate a new VPC in the Production account with a hosted zone in the Management account. Delete the association authorization in the Management account" is also a correct answer (as explained above.)
INCORRECT:
"Deploy the database on a separate EC2 instance in the new VPC. Create a record set for the instance's private IP in the private hosted zone" is incorrect.
Deploying the database on a separate EC2 instance might be cost inefficient and might not be possible due to architectural constraints. Since associating these accounts is possible by VPC association, that is a better option.
INCORRECT:
"Use SSH to connect to the application tier EC2 instance. Add an RDS endpoint IP address to the /etc/resolv.conf file" is incorrect.
Using SSH to login into instance would mean maintaining private keys for the instance which can lead to security issues hence this option is not correct.
INCORRECT:
"Create a private hosted zone for the example.com domain in the Production account. Configure Route 53 replication between AWS accounts" is incorrect.
You cannot replicate the records on an ongoing basis between accounts / zones. This is not a native Route 53 feature.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/route53-private-hosted-zone/
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-route-53/

## Câu 33 — ✅ ĐÚNG

<!-- source: T3Q19 · domain: CI -->

### Câu hỏi

A company runs Docker containers on Amazon ECS. A containerized application uses a custom tool that must be manually updated each time the container code is updated. The updated container image can then be used for new tasks. A Solutions Architect has been tasked with automating this process to eliminate the manual work and ensure a new container image is generated each time the tool code is updated.
Which combination of actions should the Solutions Architect take to meet these requirements? (Select THREE.)

### Các phương án

- **A.** Create an Amazon ECR repository for the image. Create an AWS CodeCommit repository containing code for the tool being deployed to the container image in Amazon ECR.
- **B.** Create an AWS CodeDeploy application that pulls the latest container image from Amazon ECR, updates the container with code from the source AWS CodeCommit repository, and pushes the updated container image to Amazon ECR.
- **C.** Create an AWS CodeBuild project that pulls the latest container image from Amazon ECR, updates the container with code from the source AWS CodeCommit repository, and pushes the updated container image to Amazon ECR.
- **D.** Create an AWS CodePipeline pipeline that sources the tool code from the AWS CodeCommit repository and initiates an AWS CodeDeploy application update.
- **E.** Create an Amazon EventBridge rule that triggers on commits to the AWS CodeCommit repository for the image. Configure the event to trigger an update to the image in Amazon ECR. Push the updated container image to Amazon ECR.
- **F.** Create an AWS CodePipeline pipeline that sources the tool code from the AWS CodeCommit repository and initiates an AWS CodeBuild build.

> **Bạn chọn:** A, C, F
> **Đáp án đúng:** A, C, F

### Giải thích

> ⚠️ CodeCommit availability for new customers changed in 2024–2025; the design pattern is still valid.

Choosing the correct combination of answers relies on understanding which tool to use for which piece of the job. The basic steps and tools to use are as follows:
1) Store a container image in a repository – Amazon ECR can be used.
2) Store the tool code in the repository – AWS CodeCommit can be used.
3) Update the container image with the code and save back to repository – AWS CodeBuild can be used.
4) Automate the whole process – AWS CodePipeline can be used to create an automated CI/CD pipeline.
The diagram below depicts the AWS tools (and comparable popular third-party tools) and where they are used in the CI/CD pipeline:
CORRECT:
"Create an Amazon ECR repository for the image. Create an AWS CodeCommit repository containing code for the tool being deployed to the container image in Amazon ECR" is a correct answer.
CORRECT:
"Create an AWS CodeBuild project that pulls the latest container image from Amazon ECR, updates the container with code from the source AWS CodeCommit repository, and pushes the updated container image to Amazon ECR" is also a correct answer.
CORRECT:
"Create an AWS CodePipeline pipeline that sources the tool code from the AWS CodeCommit repository and initiates an AWS CodeBuild build" is also a correct answer.
INCORRECT:
"Create an AWS CodeDeploy application that pulls the latest container image from Amazon ECR, updates the container with code from the source AWS CodeCommit repository, and pushes the updated container image to Amazon ECR" is incorrect. CodeDeploy is the wrong tool for this job, use CodeBuild instead.
INCORRECT:
"Create an AWS CodePipeline pipeline that sources the tool code from the AWS CodeCommit repository and initiates an AWS CodeDeploy application update" is incorrect. CodeDeploy will deploy the container, but the application must first be updated into the image using CodeBuild.
INCORRECT:
"Create an Amazon EventBridge rule that triggers on commits to the AWS CodeCommit repository for the image. Configure the event to trigger an update to the image in Amazon ECR. Push the updated container image to Amazon ECR" is incorrect. CodePipeline should be used rather than EventBridge.
References:
https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html
https://aws.amazon.com/ecr/getting-started/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-developer-tools-sap/

## Câu 34 — ❌ SAI

<!-- source: T6Q16 · domain: NEW -->

### Câu hỏi

An eCommerce application offers a membership program. Members of the program need to be able to download all files in a secured Amazon S3 bucket. The access should be restricted to members of the program and not available to anyone else. An Amazon CloudFront distribution has been created to deliver the content to users around the world.
What is the most efficient method a Solutions Architect should use to securely enable access to the files in the S3 bucket?

### Các phương án

- **A.** Configure the application to generate a signed URL for authenticated users that provides time-limited access to the files.
- **B.** Configure the application to send Set-Cookie headers to the viewer and control access to the files using signed cookies.
- **C.** Use an Origin Access Identity (OAI) to control access to the S3 bucket to users of the CloudFront distribution only.
- **D.** Configure a behavior in CloudFront that forwards requests for the files to the S3 bucket based on a path pattern.

> **Bạn chọn:** A
> **Đáp án đúng:** B

### Giải thích

CloudFront signed cookies allow you to control who can access your content when you don't want to change your current URLs or when you want to provide access to multiple restricted files, for example, all of the files in the subscribers' area of a website.
When using signed cookies the application sends three Set-Cookie headers to the viewer and the viewer stores the name-value pairs and adds them to the requests using a Cookie header. Access is then controlled in CloudFront based on the cookies.
CORRECT:
"Configure the application to send Set-Cookie headers to the viewer and control access to the files using signed cookies" is the correct answer.
INCORRECT:
"Configure the application to generate a signed URL for authenticated users that provides time-limited access to the files" is incorrect. A signed URL is for access to an individual file, for multiple files a signed URL would be required for each file. In this case the signed cookies approach is more efficient.
INCORRECT:
"Use an Origin Access Identity (OAI) to control access to the S3 bucket to users of the CloudFront distribution only" is incorrect. An OAI limits direct access to S3 to the CloudFront distribution only. In this case we also need a method to ensure that only the correct users of CloudFront are allowed access.
INCORRECT:
"Configure a behavior in CloudFront that forwards requests for the files to the S3 bucket based on a path pattern" is incorrect. A path pattern controls where to send requests based on path or file type. This doesn’t really assist here as it doesn’t secure based on the user requesting access.
References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-choosing-signed-urls-cookies.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 35 — ❌ SAI

<!-- source: T3Q15 · domain: NEW · flagged -->

### Câu hỏi

A corporation needs to quickly enable 350 staff members to work remotely in the event of an emergency. Their current setup includes a mix of Windows and Linux desktops with various applications installed, such as office suites and communication tools.
The solution must integrate with the company's existing on-premises Active Directory, allowing staff to use their current login credentials. Additionally, it should support multifactor authentication (MFA) and closely replicate the user interface of their existing desktop environments.
Which AWS solution would best meet these criteria?

### Các phương án

- **A.** Use Amazon WorkSpaces as the cloud-based desktop service. Establish a VPN connection to the on-premises network, set up an AD Connector to integrate with the on-premises Active Directory, and configure MFA for Amazon WorkSpaces via the AWS Management Console.
- **B.** Use Amazon AppStream 2.0 for streaming applications. Configure it with a desktop-like interface for employees. Establish a VPN connection to the on-premises network and use Active Directory Federation Services (AD FS) for integration. Connect the VPC to AD FS through the VPN.
- **C.** Use Amazon WorkSpaces for providing cloud desktops. Connect it to the on-premises network via VPN, integrate with the on-premises Active Directory using an AD Connector, and set up a RADIUS server to enable MFA.
- **D.** Use Amazon AppStream 2.0 for application streaming services. Integrate it with on-premises Active Directory Federation Services for identity management and configure MFA to control access on AppStream 2.0.

> **Bạn chọn:** D
> **Đáp án đúng:** C

### Giải thích

Amazon WorkSpaces is a managed, secure Desktop-as-a-Service (DaaS) solution that can easily scale to accommodate the needs of 350 employees. It supports both Windows and Linux desktops, ensuring a seamless transition for users.
The integration with on-premises Active Directory via an AD Connector allows employees to use their existing credentials. The use of a RADIUS server for MFA adds an extra layer of security, ensuring that the remote desktop experience is both secure and familiar to the users.
CORRECT:
"Use Amazon WorkSpaces for providing cloud desktops. Connect it to the on-premises network via VPN, integrate with the on-premises Active Directory using an AD Connector, and set up a RADIUS server to enable MFA" is the correct answer (as explained above.)
INCORRECT:
"Use Amazon WorkSpaces as the cloud-based desktop service. Establish a VPN connection to the on-premises network, set up an AD Connector to integrate with the on-premises Active Directory, and configure MFA for Amazon WorkSpaces via the AWS Management Console" is incorrect.
While Amazon WorkSpaces is a suitable solution, enabling MFA via an on-premises Active Directory is achieved by way of a RADIUS server rather than through enabling it directly in the AWS Management Console.
INCORRECT:
"Use Amazon AppStream 2.0 for streaming applications. Configure it with a desktop-like interface for employees. Establish a VPN connection to the on-premises network and use Active Directory Federation Services (AD FS) for integration. Connect the VPC to AD FS through the VPN" is incorrect.
Amazon AppStream 2.0 is more focused on application streaming rather than providing a full desktop experience. While it can be configured for a desktop-like interface, it might not fully replicate the existing desktop environment for all users.
INCORRECT:
"Use Amazon AppStream 2.0 for application streaming services. Integrate it with on-premises Active Directory Federation Services for identity management and configure MFA to control access on AppStream 2.0" is incorrect.
Choosing Amazon AppStream 2.0 primarily focuses on application streaming and may not provide the complete desktop experience that users are accustomed to. While it can integrate with AD FS for identity management, it might not offer the full desktop interface required in this scenario.
References:
https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-directory-services/

## Câu 36 — ✅ ĐÚNG

<!-- source: T4Q27 · domain: CI -->

### Câu hỏi

A company uses AWS CodePipeline to manage an application that runs on Amazon EC2 instances in an Auto Scaling group. All AWS resources are defined in CloudFormation templates. Application code is stored in an Amazon S3 bucket and installed at launch time using lifecycle hooks with EventBridge and AWS Lambda. Recent changes in the CloudFormation templates have resulted in issues that have caused outages and management require a solution to ensure this situation is not repeated.
What should a Solutions Architect do to reduce the likelihood that future changes in the templates will cause downtime?

### Các phương án

- **A.** Use AWS CodeBuild to detect and report CloudFormation error conditions when performing deployments. Deploy updates to a separate stack in a test account and use manual test plans to validate the changes.
- **B.** Use AWS CodeBuild for automated testing. Use CloudFormation changes sets to evaluate changes ahead of deployment. Use AWS CodeDeploy to leverage blue/green deployment patterns.
- **C.** Move the application code to AWS CodeCommit. Use CodeBuild to validate the application code and automate testing. Use CloudFormation StackSets to deploy updates to different environments to leverage a blue/green deployment pattern.
- **D.** Use AWS CodeDeploy and a blue/green deployment pattern with CloudFormation to replace the lifecycle hooks. Gather feedback from users to identify and issues that may require a rollback.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

AWS CodeBuild can be used to provide automated testing of application code. With CodeBuild you can use Amazon S3 as a source provider. CloudFormation change sets can be used to test updates to the templates before the infrastructure is updated.
Change sets allow you to preview how proposed changes to a stack might impact your running resources, for example, whether your changes will delete or replace any critical resources, AWS CloudFormation makes the changes to your stack only when you decide to execute the change set, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another change set.
Blue/green deployments mean that the updates are made to a separate application stack and validated before the user traffic is switched across. This provides an easy rollback path if there are any issues identified in the updated application.
CORRECT:
"Use AWS CodeBuild for automated testing. Use CloudFormation changes sets to evaluate changes ahead of deployment. Use AWS CodeDeploy to leverage blue/green deployment patterns" is the correct answer.
INCORRECT:
"Use AWS CodeBuild to detect and report CloudFormation error conditions when performing deployments. Deploy updates to a separate stack in a test account and use manual test plans to validate the changes" is incorrect. CodeBuild does not detect CloudFormation error conditions, it is used to build and test application code.
INCORRECT:
"Move the application code to AWS CodeCommit. Use CodeBuild to validate the application code and automate testing. Use CloudFormation StackSets to deploy updates to different environments to leverage a blue/green deployment pattern" is incorrect. CloudFormation StackSets are used for deploying stacks into different Regions or accounts. Change sets should be used instead for this use case.
INCORRECT:
"Use AWS CodeDeploy and a blue/green deployment pattern with CloudFormation to replace the lifecycle hooks. Gather feedback from users to identify and issues that may require a rollback" is incorrect. This doesn’t offer a way of validating issues ahead of users being directed to the updated application. Testing should be automated and issues should be identified before users access the application as much as possible.
References:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 37 — ❌ SAI

<!-- source: T6Q28 · domain: CI -->

### Câu hỏi

An automotive company is using AWS CodeBuild for CI/CD pipelines where each CodeBuild project is directly mapped to an individual application. Many of these applications use large sets of marketing data which is hosted inside an Amazon S3 bucket.
This data is provided by files which are owned by another third-party agency. A few of these projects need the entire set of data while a few of them require just a subset of more relevant data.
As the number of CodeBuild projects grows, the company notices a significant increase in the time required for the pipeline to finish running. The company wants to optimize the pipeline and reduce the amount of time that the pipeline requires to finish running.
Which solution will meet these requirements?

### Các phương án

- **A.** Create an S3 bucket for the pipeline. Configure S3 caching for the CodeBuild projects that are in the pipeline. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition.
- **B.** Create an S3 bucket for the pipeline. Configure the S3 bucket as a secondary source location for the CodeBuild projects. Update the build specifications of the CodeBuild projects. Add the S3 bucket and data file directory to the cache definition.
- **C.** Configure the cache of the CodeBuild projects as LOCAL_SOURCE_CACHE. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition.
- **D.** Create a new VPC for the CodeBuild projects. Create an Amazon Elastic File System (Amazon EFS) file system in the VPC. Configure the CodeBuild projects to run in the VPC. Mount the EFS file system at the location of the data file directory.

> **Bạn chọn:** D
> **Đáp án đúng:** A

### Giải thích

> ⚠️ Expl praises LOCAL cache then selects S3 cache; reasoning inconsistent, 'pipeline for the bucket' meaningless.

Local caching stores a cache on a build host. The cache is available to that build host only for a limited time and until another build is complete. For example, when you are dealing with large Java projects, compilation might take a long time. You can speed up subsequent builds by using local caching. This is a good option for large intermediate build artifacts because the cache is immediately available on the build host.
Since files are available in S3, it makes sense to create a pipeline for the bucket and then enable caching to reduce CodeBuild execution time.
CORRECT:
"Create an S3 bucket for the pipeline. Configure S3 caching for the CodeBuild projects that are in the pipeline. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition" is the correct answer (as explained above.)
INCORRECT:
"Create an S3 bucket for the pipeline. Configure the S3 bucket as a secondary source location for the CodeBuild projects. Update the build specifications of the CodeBuild projects. Add the S3 bucket and data file directory to the cache definition" is incorrect.
Since the question mentions that files are in the same location, there is no need to configure a secondary source location, this would have been correct if the source code and other files were at different locations.
INCORRECT:
"Configure the cache of the CodeBuild projects as LOCAL_SOURCE_CACHE. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition" is incorrect.
As per the definition, LOCAL_SOURCE_CACHE caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored hence this is incorrect.
INCORRECT:
"Create a new VPC for the CodeBuild projects. Create an Amazon Elastic File System (Amazon EFS) file system in the VPC. Configure the CodeBuild projects to run in the VPC. Mount the EFS file system at the location of the data file directory" is incorrect.
The question doesn’t mention about file sharing across instances and hence this is not a correct use case for ECS.
References:
https://aws.amazon.com/blogs/devops/improve-build-performance-and-save-time-using-local-caching-in-aws-codebuild/
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-developer-tools/

## Câu 38 — ✅ ĐÚNG

<!-- source: T5Q27 · domain: CI -->

### Câu hỏi

A media company runs an application that uses a static website configured in an Amazon S3 bucket and an Amazon CloudFront distribution. The website calls an Amazon API Gateway REST API, and an AWS Lambda function backs each API method.
The company wants to generate a CSV report every 2 weeks that records the following for each Lambda function:
· Recommended configured memory.
· Recommended cost.
· Price difference between current configurations and the recommendations.
Which solution will meet these requirements with the LEAST development time?

### Các phương án

- **A.** Create an additional Lambda function that extracts metrics data from Amazon CloudWatch Logs for each application Lambda function. Collate the data into tabular format. Store the data as a .csv file in an S3 bucket. Create an Amazon EventBridge rule to schedule the Lambda function to run every 2 weeks.
- **B.** Use AWS Compute Optimizer. Call the “ExportLambdaFunctionRecommendations” operation for the Lambda functions. Export the .csv file to an S3 bucket. Create an Amazon EventBridge rule to schedule the Lambda function to run every 2 weeks.
- **C.** Use AWS Compute Optimizer. Set up enhanced infrastructure metrics. Within the Compute Optimizer console, schedule a job to export the Lambda recommendations to a .csv file. Store the file in an S3 bucket every 2 weeks.
- **D.** Purchase the AWS Business Support plan for the production account. Opt into AWS Compute Optimizer for AWS Trusted Advisor checks. In the Trusted Advisor console, schedule a job to export the cost optimization checks to a .csv file. Store the file in an S3 bucket every 2 weeks.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

> ⚠️ Option B schedules a Lambda that was never created; wording sloppy but intent clear.

Explanation:
You can export your recommendations to record them over time and share the data with others. Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify.
Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see
Exporting Recommendations
in the Compute Optimizer User Guide.
CORRECT:
"Use AWS Compute Optimizer. Call the “ExportLambdaFunctionRecommendations” operation for the Lambda functions. Export the .csv file to an S3 bucket. Create an Amazon EventBridge rule to schedule the Lambda function to run every 2 weeks" is the correct answer (as explained above.)
INCORRECT:
"Create an additional Lambda function that extracts metrics data from Amazon CloudWatch Logs for each application Lambda function. Collate the data into tabular format. Store the data as a .csv file in an S3 bucket. Create an Amazon EventBridge rule to schedule the Lambda function to run every 2 weeks" is incorrect.
This option involves a lot of manual steps and additional effort for building the Lambda function, this would also add the cost of function invocation and so is not a suitable option.
INCORRECT:
"Use AWS Compute Optimizer. Set up enhanced infrastructure metrics. Within the Compute Optimizer console, schedule a job to export the Lambda recommendations to a .csv file. Store the file in an S3 bucket every 2 weeks" is incorrect.
The question ask specifically about the Lambda function's recommended configured memory, recommended cost, and the price difference between current configurations and the recommendations. Therefore, this is not the most suitable solution.
INCORRECT:
"Purchase the AWS Business Support plan for the production account. Opt into AWS Compute Optimizer for AWS Trusted Advisor checks. In the Trusted Advisor console, schedule a job to export the cost optimization checks to a .csv file. Store the file in an S3 bucket every 2 weeks" is incorrect.
AWS Compute Optimizer provides many inbuilt checks, and it is not necessary to have an AWS Business support plan. Also implementing the steps mentioned in this option would involve lot of steps initially and trusted advisor wouldn’t be able to deliver exact data in the format required.
References:
https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportLambdaFunctionRecommendations.html
https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-lambda/

## Câu 39 — ✅ ĐÚNG

<!-- source: T3Q32 · domain: NEW -->

### Câu hỏi

A Solutions Architect has been asked to implement a disaster recovery (DR) site for an eCommerce platform that is growing at an increasing rate. The platform runs on Amazon EC2 web servers behind Elastic Load Balancers, images stored in Amazon S3 and Amazon DynamoDB tables that store product and customer data. The DR site should be located in a separate AWS Region.
Which combinations of actions should the Solutions Architect take to implement the DR site? (Select THREE.)

### Các phương án

- **A.** Enable Amazon Route 53 health checks to determine if the primary site is down, and route traffic to the disaster recovery site if there is an issue.
- **B.** Enable DynamoDB Streams and use an event-source mapping to a Lambda function which populates a table in the second Region.
- **C.** Enable Amazon S3 cross-Region replication on the buckets that contain images.
- **D.** Enable multi-Region targets on the Elastic Load Balancer and target Amazon EC2 instances in both Regions.
- **E.** Enable versioning on the Amazon S3 buckets and enable cross-Region snapshots.
- **F.** Enable DynamoDB global tables to achieve multi-Region table replication.

> **Bạn chọn:** A, C, F
> **Đáp án đúng:** A, C, F

### Giải thích

To enable disaster recovery for this solution the Solutions Architect can create Amazon EC2 instances behind an ELB in a second Region and use DynamoDB Global Tables to create a multiregion, multi-active database. The failover can then be initiated by Amazon Route 53 using a failover routing policy configured for active-passive failover. This solutions meets all requirements.
A DynamoDB global table supports reads and writes in multiple Regions as can be seen in the diagram below:
CORRECT:
"Enable Amazon Route 53 health checks to determine if the primary site is down, and route traffic to the disaster recovery site if there is an issue" is a correct answer.
CORRECT:
"Enable Amazon S3 cross-Region replication on the buckets that contain images" is also a correct answer.
CORRECT:
"Enable DynamoDB global tables to achieve multi-Region table replication" is also a correct answer.
INCORRECT:
"Enable DynamoDB Streams and use an event-source mapping to a Lambda function which populates a table in the second Region" is incorrect. This is not a good method of synchronizing the data. DynamoDB global tables should be used instead.
INCORRECT:
"Enable multi-Region targets on the Elastic Load Balancer and target Amazon EC2 instances in both Regions" is incorrect. You cannot have multi-Region targets with an ELB.
INCORRECT:
"Enable versioning on the Amazon S3 buckets and enable cross-Region snapshots" is incorrect. There is no such thing as cross-Region snapshots with Amazon S3, snapshots are not an S3 feature.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 40 — ✅ ĐÚNG

<!-- source: T3Q1 · domain: NEW -->

### Câu hỏi

A data hosting company has developed a new application which works on a custom TCP port. The service must use fixed address assignments so other companies can whitelist the addresses in their firewalls. The application will be hosted on the publicly accessible DNS domain name cloud.myservice.com. The solution must offer high availability and redundancy across Availability Zones in a single AWS Region.
Which solution will meet these requirements?

### Các phương án

- **A.** Create Amazon EC2 instances with an Elastic IP address for each instance. Create a Network Load Balancer (NLB) and expose the static TCP port. Register EC2 instances with the NLB. Create a new name server record set named cloud.myservice.com and assign the Elastic IP addresses of the EC2 instances to the record set. Provide the Elastic IP addresses of the EC2 instances to the other companies to add to their allow lists.
- **B.** Create an Amazon ECS cluster and a service definition for the application. Create and assign public IP addresses for the ECS cluster. Create a Network Load Balancer (NLB) and expose the TCP port. Create a target group and assign the ECS cluster name to the NLB. Create a new A record set named cloud.myservice.com and assign the public IP addresses of the ECS cluster to the record set. Provide the public IP addresses of the ECS cluster to the other companies to add to their allow lists.
- **C.** Create Amazon EC2 instances for the service. Create one Elastic IP address for each Availability Zone. Create a Network Load Balancer (NLB) and expose the assigned TCP port. Assign the Elastic IP addresses to the NLB for each Availability Zone. Create a target group and register the EC2 instances with the NLB. Create a new A (alias) record set named cloud.myservice.com and assign the NLB DNS name to the record set.
- **D.** Create an Amazon ECS cluster and a service definition for the application. Create and assign public IP address for each host in the cluster. Create an Application Load Balancer (ALB) and expose the static TCP port. Create a target group and assign the ECS service definition name to the ALB. Create a new CNAME record set and associate the public IP addresses to the record set. Provide the Elastic IP addresses of the Amazon EC2 instances to the other companies to add to their allow lists.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Below is the sequence of steps to achieve the above:
- Create Amazon EC2 instances for the service.
- Create one Elastic IP address for each Availability Zone.
- Create a Network Load Balancer (NLB) and expose the assigned TCP port.
- Assign the Elastic IP addresses to the NLB for each Availability Zone.
- Create a target group and register the EC2 instances with the NLB.
- Create a new A (alias) record set named cloud.myservice.com and assign the NLB DNS name to the record set.
This solution exposes static public IP addresses that can be whitelisted in the firewalls of the clients. The solution also offers high availability across AZs within an AWS Region.
CORRECT:
"Create Amazon EC2 instances for the service. Create one Elastic IP address for each Availability Zone. Create a Network Load Balancer (NLB) and expose the assigned TCP port. Assign the Elastic IP addresses to the NLB for each Availability Zone. Create a target group and register the EC2 instances with the NLB. Create a new A (alias) record set named cloud.myservice.com and assign the NLB DNS name to the record set" is the correct answer (as explained above.)
INCORRECT:
"Create Amazon EC2 instances with an Elastic IP address for each instance. Create a Network Load Balancer (NLB) and expose the static TCP port. Register EC2 instances with the NLB. Create a new name server record set named cloud.myservice.com and assign the Elastic IP addresses of the EC2 instances to the record set. Provide the Elastic IP addresses of the EC2 instances to the other companies to add to their allow lists" is incorrect.
When creating NLB, you need to pick the available Elastic IP address which was initially allocated as mentioned in the question above. This can be one of three options:
- Amazon's pool of IPv4 addresses—If you want an IPv4 address to be allocated from Amazon's pool of IPv4 addresses.
- Public IPv4 address that you bring to your AWS account—If you want to allocate an IPv4 address from an IP address pool that you have brought to your AWS account. This option is disabled if you do not have any IP address pools.
- Customer owned pool of IPv4 addresses—If you want to allocate an IPv4 address from a pool created from your on-premises network for use with an AWS Outpost. This option is disabled if you do not have an AWS Outpost.
INCORRECT:
"Create an Amazon ECS cluster and a service definition for the application. Create and assign public IP addresses for the ECS cluster. Create a Network Load Balancer (NLB) and expose the TCP port. Create a target group and assign the ECS cluster name to the NLB. Create a new A record set named my.service.com and assign the public IP addresses of the ECS cluster to the record set. Provide the public IP addresses of the ECS cluster to the other companies to add to their allow list" is incorrect.
To have an ECS cluster behind NLB as a target group, ECS has dynamic port mapping which binds instances dynamically. Binding a cluster name directly behind NLB is not an option.
INCORRECT:
"Create an Amazon ECS cluster and a service definition for the application. Create and assign public IP address for each host in the cluster. Create an Application Load Balancer (ALB) and expose the static TCP port. Create a target group and assign the ECS service definition name to the ALB. Create a new CNAME record set and associate the public IP addresses to the record set. Provide the Elastic IP addresses of the Amazon EC2 instances to the other companies to add to their allow lists" is incorrect.
An ALB cannot be used as it only supports HTTP and HTTPS protocols and you cannot configure a listener with a custom TCP port.
References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html
https://aws.amazon.com/premiumsupport/knowledge-center/elb-attach-elastic-ip-to-public-nlb
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-elastic-load-balancing-aws-elb/
https://digitalcloud.training/amazon-route-53/

## Câu 41 — ❌ SAI

<!-- source: T5Q23 · domain: CI -->

### Câu hỏi

An application runs on a fleet of Amazon ECS instances and stores data in an Amazon S3 bucket. Until recently the application had been working well and then started to fail to upload objects to the S3 bucket. Server access logging has been enabled and 403 errors have been identified since the time of the fault. The ECS cluster has been setup according to best practices and no changes have been made to the S3 bucket policy or IAM roles used to access the bucket.
What is the most LIKELY cause of the failure?

### Các phương án

- **A.** The ECS service in inaccessible.
- **B.** The ECS container instance IAM role was modified.
- **C.** The ECS tasks have insufficient memory assigned.
- **D.** The ECS task IAM role was modified.

> **Bạn chọn:** C
> **Đáp án đúng:** D

### Giải thích

A 403 error is an access denied error. Therefore, there must be an issue relating to authorization to access the S3 bucket. In this scenario the bucket policy and IAM roles have not been modified. The next thing to check is that the IAM role is correctly assigned to the ECS tasks.
The most likely cause of this issue is that the ECS task role has been changed and the tasks no longer have the permissions to access S3.
CORRECT:
"The ECS task IAM role was modified" is the correct answer.
INCORRECT:
"The ECS container instance IAM role was modified" is incorrect. According to best practice the permissions that containers (tasks) require should be specified in task IAM roles not in container instance IAM roles. As the cluster has been setup according to best practice the permissions to S3 should not be specified in the container instance IAM role.
INCORRECT:
"The ECS service in inaccessible" is incorrect. This would not result in an access denied error.
INCORRECT:
"The ECS tasks have insufficient memory assigned" is incorrect. This would not result in an access denied error.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/s3-troubleshoot-403/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 42 — ✅ ĐÚNG

<!-- source: T4Q24 · domain: ORG -->

### Câu hỏi

A company runs several IT services in an on-premises data center that is connected to AWS using an AWS Direct Connect (DX) connection. The service data is sensitive and the company uses an IPSec VPN over the DX connection to encrypt data. Security requirements mandate that the data cannot traverse the internet. The company wants to offer the IT services to other companies who use AWS.
Which solution will meet these requirements?

### Các phương án

- **A.** Create a VPC Endpoint Service that accepts TCP traffic and host it behind a Network Load Balancer. Enable access to the IT services over the DX connection.
- **B.** Configure a mesh of AWS VPN CloudHub IPsec VPN connections between the customer AWS accounts and the service provider AWS account.
- **C.** Create a VPC Endpoint Service that accepts HTTP or HTTPS traffic and host it behind an Application Load Balancer. Enable access to the IT services over the DX connection.
- **D.** Attach an internet gateway to the VPC and ensure that network access control and security group rules allow the relevant inbound and outbound traffic.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

The solution is to use VPC endpoint services in a service provider model. In this model a network load balancer must be created in the service provider VPC in front of the application services. Remember that NLBs can use on-premises targets. A VPC endpoint is then created that uses the NLB.
A service consumer that has been granted permissions then creates an interface endpoint to your service, optionally in each Availability Zone in which you configured your service. This is depicted in the image below:
CORRECT:
"Create a VPC Endpoint Service that accepts TCP traffic and host it behind a Network Load Balancer. Enable access to the IT services over the DX connection" is the correct answer.
INCORRECT:
"Create a VPC Endpoint Service that accepts HTTP or HTTPS traffic and host it behind an Application Load Balancer. Enable access to the IT services over the DX connection" is incorrect. A NLB should be used for a VPC endpoint service.
INCORRECT:
"Configure a mesh of AWS VPN CloudHub IPsec VPN connections between the customer AWS accounts and the service provider AWS account" is incorrect. VPNs use the internet and the internet must be avoided. Note that the VPN used by the company runs over DX, not over the internet, so the connection can be encrypted.
INCORRECT:
"Attach an internet gateway to the VPC and ensure that network access control and security group rules allow the relevant inbound and outbound traffic" is incorrect. An internet gateway is used for internet-based connectivity which should be avoided. It is not needed for a VPC endpoint service.
References:
https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service-overview.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 43 — ✅ ĐÚNG

<!-- source: T4Q20 · domain: CI -->

### Câu hỏi

A company has created a fitness tracking mobile app the uses a serverless REST API. The app consists of an Amazon API Gateway API with a Regional endpoint, AWS Lambda functions and an Amazon Aurora MySQL database cluster. The company recently secured a deal with a sports company to promote the new app which resulted in a significant increase in the number of requests received.
Unfortunately, the increase in traffic resulted in sporadic database memory errors and performance degradation. The traffic included significant numbers of HTTP requests querying the same data in short bursts of traffic during weekends and holidays.
The company needs to improve its ability to support the additional usage while minimizing the increase in costs associated with the solution.
Which strategy meets these requirements?

### Các phương án

- **A.** Convert the API Gateway Regional endpoint to an edge-optimized endpoint. Enable caching in the production stage.
- **B.** Implement an Amazon ElastiCache for Redis cache to store the results of the database calls. Modify the Lambda functions to use the cache.
- **C.** Modify the instance type of the Aurora database cluster to use an instance with more memory.
- **D.** Create usage plans in API Gateway and distribute API keys to clients. Configure metered access to the production stage.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

An
edge-optimized API endpoint
is best for geographically distributed clients. API requests are routed to the nearest CloudFront Point of Presence (POP). For mobile clients this is a good use case for this type of endpoint. The Regional endpoint is best suited to traffic coming from within the Region only.
You can enable API caching in Amazon API Gateway to cache your endpoint's responses. With caching, you can reduce the number of calls made to your endpoint and also improve the latency of requests to your API.
CORRECT:
"Convert the API Gateway Regional endpoint to an edge-optimized endpoint. Enable caching in the production stage" is the correct answer.
INCORRECT:
"Create usage plans in API Gateway and distribute API keys to clients. Configure metered access to the production stage" is incorrect. This does not support the additional usage; it limits additional usage.
INCORRECT:
"Implement an Amazon ElastiCache for Redis cache to store the results of the database calls. Modify the Lambda functions to use the cache" is incorrect. This will increase costs associated with the solution as the ElastiCache cluster could be expensive.
INCORRECT:
"Modify the instance type of the Aurora database cluster to use an instance with more memory" is incorrect. This would mean the database cluster cost more at all times, not just when the traffic increases.
References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 44 — ✅ ĐÚNG

<!-- source: T1Q24 · domain: ORG -->

### Câu hỏi

A company includes several business units that each use a separate AWS account and a parent company AWS account. The company requires a single AWS bill across all AWS accounts with costs broken out for each business unit. The company also requires that services and features be restricted in the business unit accounts and this must be governed centrally.
Which combination of steps should a Solutions Architect take to meet these requirements? (Select TWO.)

### Các phương án

- **A.** Use AWS Organizations to create a separate organization for each AWS account with all features enabled. Then, create trust relationships between the AWS organizations.
- **B.** Use AWS Organizations to create a single organization in the parent account with all features enabled. Then, invite each business unit’s AWS account to join the organization.
- **C.** Use permissions boundaries applied to each business unit’s AWS account to define the maximum permissions available for services and features.
- **D.** Create an SCP that allows only approved services and features, then apply the policy to the business unit AWS accounts.
- **E.** Enable consolidated billing in the parent account's billing console and link the business unit AWS accounts.

> **Bạn chọn:** B, D
> **Đáp án đúng:** B, D

### Giải thích

To enable the required features you simply need to setup a single AWS organization in the parent account with all features enabled. The existing business unit AWS accounts can then be invited to join the organization.
This setup will automatically enable consolidated billing which will ensure a single AWS bill is received in the parent account which has costs broken out by each AWS account.
Service Control Policies (SCPs) can then be used to restrict the maximum available permissions to services and features that the parent company wishes to apply to the member accounts. Once applied, all users will be affected in the member accounts.
CORRECT:
"Use AWS Organizations to create a single organization in the parent account with all features enabled. Then, invite each business unit’s AWS account to join the organization" is a correct answer.
CORRECT:
"Create an SCP that allows only approved services and features, then apply the policy to the business unit AWS accounts" is also a correct answer.
INCORRECT:
"Use AWS Organizations to create a separate organization for each AWS account with all features enabled. Then, create trust relationships between the AWS organizations" is incorrect. A single organization should be created; trust relationships are not a concept associated with AWS Organizations.
INCORRECT:
"Use permissions boundaries applied to each business unit’s AWS account to define the maximum permissions available for services and features" is incorrect. Permissions boundaries are applied to IAM entities (users or roles), not to AWS accounts.
INCORRECT:
"Enable consolidated billing in the parent account's billing console and link the business unit AWS accounts" is incorrect. Consolidated billing is a feature of AWS Organizations, you must create an organization, invite the relevant accounts, and then a single bill will be generated in the management (parent) account.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 45 — ❌ SAI

<!-- source: T5Q14 · domain: CI -->

### Câu hỏi

A fleet of EC2 instances generate a large quantity of data and store the data on an Amazon EFS file system. The EC2 instances also backup the data by uploading to an Amazon S3 bucket in another Region on a daily basis. Some S3 uploads have been failing and the storage costs have significantly increased.
The operations team has removed the failed uploads. How can a Solutions Architect configure the backup jobs to efficiently backup data to S3 while reducing storage costs?

### Các phương án

- **A.** Use S3 Transfer Acceleration for the backup jobs. Use the Multi-Object Delete operation to remove the old uploads on a daily basis.
- **B.** Use multipart upload for the backup jobs. Create a lifecycle policy that archives data to Amazon S3 Glacier on a daily basis.
- **C.** Use S3 Transfer Acceleration for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating.
- **D.** Use multipart upload for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating.

> **Bạn chọn:** B
> **Đáp án đúng:** D

### Giải thích

S3’s multipart upload feature accelerates the uploading of large objects by allowing you to split them up into logical parts that can be uploaded in parallel. If you initiate a multipart upload but never finish it, the in-progress upload occupies some storage space and will incur storage charges.
However, these uploads are not visible when you list the contents of a bucket. You can use a lifecycle rule to clean up incomplete multipart uploads which will reduce storage space.
The rule configuration can be seen in the image below:
CORRECT:
"Use multipart upload for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating" is the correct answer.
INCORRECT:
"Use S3 Transfer Acceleration for the backup jobs. Use the Multi-Object Delete operation to remove the old uploads on a daily basis" is incorrect. S3 transfer acceleration is for optimizing the speed of uploads, multipart upload is a better solution for running uploads of parts of objects in parallel. Using multi-object delete is not an automated process, it will be much better to use a lifecycle rule for efficiency.
INCORRECT:
"Use multipart upload for the backup jobs. Create a lifecycle policy that archives data to Amazon S3 Glacier on a daily basis" is incorrect. The failed uploads should not be archived, they should be deleted.
INCORRECT:
"Use S3 Transfer Acceleration for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating" is incorrect. As explained above for S3 transfer acceleration.
References:
https://aws.amazon.com/blogs/aws/s3-lifecycle-management-update-support-for-multipart-uploads-and-delete-markers/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

## Câu 46 — ✅ ĐÚNG

<!-- source: T3Q21 · domain: ORG -->

### Câu hỏi

A financial company processes transactions using on-premises application servers which save output to an Amazon DynamoDB table. The company’s data center is connected to AWS using an AWS Direct Connect (DX) connection. Company managed has mandated that the solution should be available across multiple Regions. Consistent network performance must be maintained at all times.
What changes should the company make to meet these requirements?

### Các phương án

- **A.** Create a DX connection to a second AWS Region. Use DynamoDB global tables to replicate data to the second Region. Modify the application to fail over to the second Region.
- **B.** Use an AWS managed VPN to connect to a second AWS Region. Create a copy of the DynamoDB table in the second Region. Enable DynamoDB streams in the primary Region and use AWS Lambda to synchronize data to the copied table.
- **C.** Create a DX connection to a second AWS Region. Create an identical DynamoDB table in the second Region. Enable DynamoDB auto scaling to manage throughput capacity. Modify the application to write to the second Region.
- **D.** Use an AWS managed VPN to connect to a second AWS Region. Create a copy of the DynamoDB table in the second Region. Enable DynamoDB streams in the primary Region and use AWS DMS to synchronize data to the copied table.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

To ensure consistent network performance and AWS Direct Connect connection must be used as AWS Managed VPN relies on the public internet which cannot offer consistent performance.
Amazon DynamoDB Global Tables is a fully managed, multi-region, multi-active database. This means you can read and write to multiple Regions. In the event of the failure of a Region the application logic must be set to fail to an endpoint in another Region where a replica table is running.
The diagram below depicts how DynamoDB replicates data between Regions and accepts reads and writes:
CORRECT:
"Create a DX connection to a second AWS Region. Use DynamoDB global tables to replicate data to the second Region. Modify the application to fail over to the second Region" is the correct answer.
INCORRECT:
"Use an AWS managed VPN to connect to a second AWS Region. Create a copy of the DynamoDB table in the second Region. Enable DynamoDB streams in the primary Region and use AWS Lambda to synchronize data to the copied table" is incorrect. A VPN does not offer consistent performance and DynamoDB global tables should be used for a multi-active database.
INCORRECT:
"Create a DX connection to a second AWS Region. Create an identical DynamoDB table in the second Region. Enable DynamoDB auto scaling to manage throughput capacity. Modify the application to write to the second Region" is incorrect. This does not offer any solution for creating a synchronized copy of the database in a second Region.
INCORRECT:
"Use an AWS managed VPN to connect to a second AWS Region. Create a copy of the DynamoDB table in the second Region. Enable DynamoDB streams in the primary Region and use AWS DMS to synchronize data to the copied table" is incorrect. A VPN does not offer consistent performance and AWS DMS should be replaced with DynamoDB global tables.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 47 — ✅ ĐÚNG

<!-- source: T1Q11 · domain: NEW -->

### Câu hỏi

A company requires multi-Region availability for an application that runs on Amazon EC2 instances with an Amazon RDS for MySQL database. The solution must offer the highest availability.
Which solution should a solutions architect recommend?

### Các phương án

- **A.** Enable automated backups for the RDS database instance. In the case of an outage, promote the automated backup to be a standalone DB instance. Point applications to the new DB endpoint and create a read replica to maintain high availability.
- **B.** Enable global tables for the RDS database instance across multiple Regions. Store the DB endpoint in AWS Secrets Manager. In the case of an outage, update the DB endpoint in Secrets Manager to the cross-Region table endpoint.
- **C.** Enable a multi-master cluster configuration across multiple Regions. Store the DB endpoint in AWS Secrets Manager. In the case of an outage, use AWS Lambda to update the endpoint address used by the applications.
- **D.** Enable a cross-Region read replica for the RDS database. In the case of an outage, promote the replica to be a standalone DB instance. Point applications to the new DB endpoint and create a read replica to maintain high availability.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

You can promote a read replica to a standalone instance as a disaster recovery solution if the primary DB instance fails. This is a fairly quick and easy process. Applications will then need to be redirected to point to the endpoint of the newly promoted DB instance. To maintain availability a new read replica can then be created.
CORRECT:
"Enable a cross-Region read replica for the RDS database. In the case of an outage, promote the replica to be a standalone DB instance. Point applications to the new DB endpoint and create a read replica to maintain high availability" is the correct answer (as explained above.)
INCORRECT:
"Enable automated backups for the RDS database instance. In the case of an outage, promote the automated backup to be a standalone DB instance. Point applications to the new DB endpoint and create a read replica to maintain high availability" is incorrect.
You cannot promote automated backups. You can use them to restore databases to a specific point in time or create a new DB instance. This will not be useful if a regional outage occurs as the automated backup is stored within the same Region by default.
INCORRECT:
"Enable global tables for the RDS database instance across multiple Regions. Store the DB endpoint in AWS Secrets Manager. In the case of an outage, update the DB endpoint in Secrets Manager to the cross-Region table endpoint" is incorrect.
Global tables is a feature of Amazon DynamoDB and is not available for Amazon RDS.
INCORRECT:
"Enable a multi-master cluster configuration across multiple Regions. Store the DB endpoint in AWS Secrets Manager. In the case of an outage, use AWS Lambda to update the endpoint address used by the applications" is incorrect.
Multi-master configurations are only available for Amazon Aurora and only within a Region.
References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-rds/

## Câu 48 — ✅ ĐÚNG

<!-- source: T1Q22 · domain: MIG -->

### Câu hỏi

A company is migrating its on-premises systems to AWS. The computers consist of a combination of Windows and Linux virtual machines on VMware and physical servers.
The company wants to be able to identify dependencies between on-premises systems and group systems together into applications to build migration plans. The company also needs to understand the performance requirements for systems so they can be right-sized.
How can these requirements be met?

### Các phương án

- **A.** Extract system information from an on-premises configuration management database (CMDB). Import the data directly into the Application Discovery Service.
- **B.** Install the AWS Application Discovery Service Discovery Agent on each of the on-premises systems. Allow the Discovery Agent to collect data for a period of time.
- **C.** Install the AWS Application Discovery Service Discovery Connector in VMware vCenter. Allow the Discovery Connector to collect data for one week.
- **D.** Install the AWS Application Discovery Service Discovery Connector in VMware vCenter. Install the AWS Application Discovery Service Discovery Agent on the physical on-premises servers. Allow the Discovery Agent to collect data for a period of time.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

> ⚠️ Discovery Connector is superseded by the Agentless Collector (same ADS concept).

The AWS Discovery Agent is AWS software that you install on on-premises servers and VMs targeted for discovery and migration. Agents capture system configuration, system performance, running processes and details of the network connections between systems. Agents support most Linux and Windows operating systems, and you can deploy them on physical on-premises servers, Amazon EC2 instances, and virtual machines.
Though you can use the agent on virtual machines, as described above, it is more efficient to use the Agentless Discovery connector for VMware virtual machines. This connector can be installed in VMware vCenter.
The AWS Discovery Connector is a VMware appliance that can collect information only about VMware virtual machines (VMs). You install the Discovery Connector as a VM in your VMware vCenter Server environment using an Open Virtualization Archive (OVA) file. Because the Discovery Connector relies on VMware metadata to gather server information regardless of operating system, it minimizes the time required for initial on-premises infrastructure assessment.
CORRECT:
"Install the AWS Application Discovery Service Discovery Connector in VMware vCenter. Install the AWS Application Discovery Service Discovery Agent on the physical on-premises servers. Allow the Discovery Agent to collect data for a period of time" is the correct answer.
INCORRECT:
"Extract system information from an on-premises configuration management database (CMDB). Import the data directly into the Application Discovery Service" is incorrect. It is possible to upload data to the Migration Hub but you must use a specially formatted CSV file. It is unlikely the CMDB export would be directly importable into Migration Hub so some work is likely required to format the data. Also, the CMDB will hold configuration data but not performance data so this solution does not satisfy all requirements.
INCORRECT:
"Install the AWS Application Discovery Service Discovery Agent on each of the on-premises systems. Allow the Discovery Agent to collect data for a period of time" is incorrect. This is not the most efficient method of collecting data from the VMware virtual machines as the connector for vCenter is a better choice.
INCORRECT:
"Install the AWS Application Discovery Service Discovery Connector in VMware vCenter. Allow the Discovery Connector to collect data for one week" is incorrect. This will only retrieve information about the virtual machines, not the physical servers.
References:
https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html
https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-connector.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-migration-sap/

## Câu 49 — ✅ ĐÚNG

<!-- source: T1Q31 · domain: NEW -->

### Câu hỏi

A solution is required for updating user metadata and will be initiated by a fleet of front-end web servers. The solution must be capable of scaling rapidly from hundreds to tens of thousands of jobs in less than a minute. The solution must be asynchronous and minimize costs.
Which solution should a Solutions Architect use to meet these requirements?

### Các phương án

- **A.** Create an AWS CloudFormation stack that is updated by an AWS Lambda function. Configure the Lambda function to update the metadata.
- **B.** Create an AWS Lambda function that will update user metadata. Create an Amazon SQS queue and configure it as an event source for the Lambda function. Update the web application to send jobs to the queue.
- **C.** Create an AWS Lambda function that will update user metadata. Create AWS Step Functions that will trigger the Lambda function. Update the web application to initiate Step Functions for every job.
- **D.** Create an Amazon EC2 Auto Scaling group of EC2 instances that pull messages from an Amazon SQS queue and process the user metadata updates. Configure the web application to send jobs to the queue.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

The most cost-effective solution to this requirement will be to use a fully serverless and decoupled architecture. With Amazon SQS the web application can asynchronously place jobs in the queue. The queue can be configured as an event source for AWS Lambda which means the Lambda function will be triggered each time a job is placed in the queue. Lambda processes the messages synchronously.
CORRECT:
"Create an AWS Lambda function that will update user metadata. Create an Amazon SQS queue and configure it as an event source for the Lambda function. Update the web application to send jobs to the queue" is the correct answer.
INCORRECT:
"Create an AWS Lambda function that will update user metadata. Create AWS Step Functions that will trigger the Lambda function. Update the web application to initiate Step Functions for every job" is incorrect. Step Functions is used to coordinate multiple serverless functions in a workflow and is not necessary for this use case.
INCORRECT:
"Create an AWS CloudFormation stack that is updated by an AWS Lambda function. Configure the Lambda function to update the metadata" is incorrect. This solution doesn’t make much sense. CloudFormation is used for deploying infrastructure and there is no mention of what is triggering Lambda.
INCORRECT:
"Create an Amazon EC2 Auto Scaling group of EC2 instances that pull messages from an Amazon SQS queue and process the user metadata updates. Configure the web application to send jobs to the queue" is incorrect. This would work but would be less cost-effective compared to using AWS Lambda.
References:
https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-application-integration-sap/

## Câu 50 — ✅ ĐÚNG

<!-- source: T2Q2 · domain: MIG -->

### Câu hỏi

A Solutions Architect is migrating an application to AWS Fargate. The task runs in a private subnet and does not have direct connectivity to the internet. When the Fargate task is launched, it fails with the following error:
CannotPullContainerError: API error (500): Get https://111122223333.dkr.ecr.us-east-1.amazonaws.com/v2/: net/http: request canceled while waiting for connection"
What should the Solutions Architect do to correct the error?

### Các phương án

- **A.** Specify DISABLED for Auto-assign public IP when launching the task and configure a NAT gateway in a public subnet to route requests to the internet.
- **B.** Specify ENABLED for Auto-assign public IP when launching the task.
- **C.** Specify DISABLED for Auto-assign public IP when launching the task and configure a NAT gateway in a private subnet to route requests to the internet.
- **D.** Enable dual-stack in the Amazon ECS account settings and configure the network for the task to use awsvpc.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

When a Fargate task is launched, its elastic network interface requires a route to the internet to pull container images. If you receive an error similar to the following when launching a task, it is because a route to the internet does not exist:
CannotPullContainerError: API error (500): Get https://111122223333.dkr.ecr.us-east-1.amazonaws.com/v2/: net/http: request canceled while waiting for connection"
To resolve this issue, you can:
- For tasks in public subnets, specify
ENABLED
for
Auto-assign public IP
when launching the task.
- For tasks in private subnets, specify
DISABLED
for
Auto-assign public IP
when launching the task, and configure a NAT gateway in your VPC to route requests to the internet.
CORRECT:
"Specify
DISABLED
for
Auto-assign public IP
when launching the task and configure a NAT gateway in a public subnet to route requests to the internet" is the correct answer.
INCORRECT:
"Specify
DISABLED
for
Auto-assign public IP
when launching the task and configure a NAT gateway in a private subnet to route requests to the internet" is incorrect. The NAT Gateway should be in a public subnet.
INCORRECT:
"Specify
ENABLED
for
Auto-assign public IP
when launching the task" is incorrect. This will not work as the task is running in a private subnet and will not pick up a public IP.
INCORRECT:
"Enable dual-stack in the Amazon ECS account settings and configure the network for the task to use awsvpc" is incorrect. This is used to enable IPv6 for a task but that is not required in this situation.
References:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_cannot_pull_image.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

## Câu 51 — ❌ SAI

<!-- source: T3Q27 · domain: NEW -->

### Câu hỏi

A company requires federated access to AWS for users of a mobile application. The security team has mandated that the application must use a custom-built solution for authenticating users and use IAM roles for authorization.
Which of the following actions would enable authentication and authorization and satisfy the requirements? (Select TWO.)

### Các phương án

- **A.** Use a custom-built SAML-compatible solution for authentication and use AWS SSO for authorization.
- **B.** Create a custom-built LDAP connector using Amazon API Gateway and AWS Lambda for authentication. Use a token-based Lambda authorizer that uses JWT.
- **C.** Use a custom-built OpenID Connect-compatible solution with AWS SSO for authentication and authorization.
- **D.** Use a custom-built SAML-compatible solution that uses LDAP for authentication and uses a SAML assertion to perform authorization to the IAM identity provider.
- **E.** Use a custom-built OpenID Connect-compatible solution for authentication and use Amazon Cognito for authorization.

> **Bạn chọn:** B, D
> **Đáp án đúng:** D, E

### Giải thích

> ⚠️ 'AWS SSO' is now IAM Identity Center.

There are two possible solutions for this scenario:
· An OpenID Connect provider can be added in IAM to enable federated authentication. An Amazon Cognito identity pool can then be used for authorization. Amazon Cognito identity pools provide temporary AWS credentials for users who are guests (unauthenticated) and for users who have been authenticated and received a token.
· AWS supports identity federation with SAML 2.0. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without you having to create an IAM user for everyone in your organization. In your organization's IdP, you define assertions that map users or groups in your organization to the IAM roles.
The diagram below shows how the authentication and authorization process works when assuming a role using SAML:
CORRECT:
"Use a custom-built OpenID Connect-compatible solution for authentication and use Amazon Cognito for authorization" is a correct answer.
CORRECT:
"Use a custom-built SAML-compatible solution that uses LDAP for authentication and uses a SAML assertion to perform authorization to the IAM identity provider" is also a correct answer.
INCORRECT:
"Use a custom-built SAML-compatible solution for authentication and use AWS SSO for authorization" is incorrect. AWS SSO cannot be used for mobile applications.
INCORRECT:
"Create a custom-built LDAP connector using Amazon API Gateway and AWS Lambda for authentication. Use a token-based Lambda authorizer that uses JWT" is incorrect. This is not a complete solution and API Gateway is not required for this solution.
INCORRECT:
"Use a custom-built OpenID Connect-compatible solution with AWS SSO for authentication and authorization" is incorrect. AWS SSO cannot be used for mobile applications.
References:
https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 52 — ✅ ĐÚNG

<!-- source: T2Q33 · domain: ORG -->

### Câu hỏi

A company recently noticed an increase in costs associated with Amazon EC2 instances and Amazon RDS databases. The company needs to be able to track the costs. The company uses AWS Organizations for all of their accounts. AWS CloudFormation is used for deploying infrastructure and all resources are tagged. The management team has requested that cost center numbers and project ID numbers are added to all future EC2 instances and RDS databases.
What is the MOST efficient strategy a Solutions Architect should follow to meet these requirements?

### Các phương án

- **A.** Use an AWS Config rule to check for untagged resources. Create a centralized AWS Lambda based solution to tag untagged EC2 instances and RDS databases every hour using a cross-account role.
- **B.** Use Tag Editor to tag existing resources. Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to activate.
- **C.** Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to activate. Use permissions boundaries to restrict the creation of resources that do not have the cost center and project ID tags specified.
- **D.** Use Tag Editor to tag existing resources. Create cost allocation tags to define the cost center and project ID. Use SCPs to restrict the creation of resources that do not have the cost center and project ID tags specified.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

You can use tags to organize your resources, and cost allocation tags to track your AWS costs on a detailed level. After you activate cost allocation tags, AWS uses the cost allocation tags to organize your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs.
By adding tags to all new resources, the management team will be better able to track costs and allocate costs to specific cost centers and projects.
Service Control Policies (SCPs) can be used to limit the maximum available permissions in an account in AWS Organizations. SCPs are policies and conditional statements can be added. In this case an SCP can be created with a conditional statement that only allows resources to be created if they have a tag specified.
CORRECT:
"Use Tag Editor to tag existing resources. Create cost allocation tags to define the cost center and project ID. Use SCPs to restrict the creation of resources that do not have the cost center and project ID tags specified" is the correct answer.
INCORRECT:
"Use an AWS Config rule to check for untagged resources. Create a centralized AWS Lambda based solution to tag untagged EC2 instances and RDS databases every hour using a cross-account role" is incorrect. AWS Config can be used for compliance but a better solution would be to enforce tags at creation time. Using Lambda to tag the resources would be complex in terms of identifying which tags to add to which resources.
INCORRECT:
"Use Tag Editor to tag existing resources. Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to activate" is incorrect. There is no mechanism here to enforce application of tags.
INCORRECT:
"Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to activate. Use permissions boundaries to restrict the creation of resources that do not have the cost center and project ID tags specified" is incorrect. Permissions boundaries apply to user accounts but SCPs apply to entire AWS accounts and will be easier to enforce for all users.
References:
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 53 — ✅ ĐÚNG

<!-- source: T6Q7 · domain: NEW -->

### Câu hỏi

A Solutions Architect is designing a highly available infrastructure for a popular mobile application that offers games and videos for mobile phone users. The application runs on Amazon EC2 instances behind an Application Load Balancer. The database layer consist of an Amazon RDS MySQL Multi-AZ instance. The entire application stack is deployed across us-east-2 and us-west-1. Amazon Route 53 is configured to route traffic to the two deployments using a latency-based routing policy.
A testing team blocked access to the Amazon RDS DB instance in us-east-2 to verify that users who are typically directed to that deployment would be directed to us-west-1. This did not occur and users close to us-east-2 were directed there and the application failed.
Which changes to the infrastructure should a Solutions Architect make to resolve this issue? (Select TWO.)

### Các phương án

- **A.** Change to a failover routing policy in Amazon Route 53 and configure active-active failover. Write a custom health check the verifies successful access to the Application Load Balancers in each Region.
- **B.** Write a custom health check that queries the AWS Service Dashboard API to verify the Amazon RDS service is healthy in each Region.
- **C.** Set the value of Evaluate Target Health to Yes on the failover alias resources for both us-east-2 and us-west-1.
- **D.** Write a custom health check that verifies successful access to the database endpoints in each Region. Add the health check within the latency-based routing policy in Amazon Route 53.
- **E.** Set the value of Evaluate Target Health to Yes on the latency alias resources for both us-east-2 and us-west-1.

> **Bạn chọn:** D, E
> **Đáp án đúng:** D, E

### Giải thích

The problem that is occurring is the database layer has failed (simulated) but the health checks (if there are any) are not checking access to the database. This can be resolved by creating a custom health check that connects to the RDS database endpoints in each Region and verifies that they are accessible. If a health check fails, Route 53 will no longer send any traffic to the deployment in that Region.
CORRECT:
"Write a custom health check that verifies successful access to the database endpoints in each Region. Add the health check within the latency-based routing policy in Amazon Route 53" is a correct answer.
CORRECT:
"Set the value of Evaluate Target Health to Yes on the latency alias resources for both us-east-2 and us-west-1" is also a correct answer.
INCORRECT:
"Change to a failover routing policy in Amazon Route 53 and configure active-active failover. Write a custom health check the verifies successful access to the Application Load Balancers in each Region" is incorrect. Checking that the ALBs are accessible does not ensure that the database layer is accessible which is the problem in this scenario.
INCORRECT:
"Write a custom health check that queries the AWS Service Dashboard API to verify the Amazon RDS service is healthy in each Region" is incorrect. This could return a result that shows that the RDS service is available but the specific endpoint might not be.
INCORRECT:
"Set the value of Evaluate Target Health to Yes on the failover alias resources for both us-east-2 and us-west-1" is incorrect. There is no need to change to failover routing and this configuration would lose some of the performance benefits of latency-based routing.
References:
https://aws.amazon.com/blogs/aws/domain-name-health-checks-for-route-53/
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-latency.html#rrsets-values-latency-associate-with-health-check
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 54 — ✅ ĐÚNG

<!-- source: T1Q32 · domain: CI -->

### Câu hỏi

A database for an eCommerce website was deployed on an Amazon RDS for MySQL DB instance with 100GB of General Purpose SSD storage. The database was running performantly for several weeks until a peak shopping period when customers experienced slow performance and timeouts. Amazon CloudWatch metrics indicate that reads and writes to the DB instance were experiencing long response times. Metrics show that CPU utilization is <50%, plenty of available memory, and sufficient free storage space. There is no evidence of database connectivity issues in the application server logs.
What could be the root cause of database performance issues?

### Các phương án

- **A.** The increased load caused the data in the tables to change frequently, requiring indexes to be rebuilt to optimize queries.
- **B.** The increased load resulted in the maximum number of allowed connections to the database instance.
- **C.** A large number of reads and writes exhausted the I/O credit balance due to provisioning low disk storage during the setup phase.
- **D.** A large number of reads and writes exhausted the network bandwidth available to the RDS for MySQL DB instance.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

> ⚠️ Relies on gp2 burst I/O credits; RDS default now gp3 without credits.

Baseline I/O performance for General Purpose SSD storage is 3 IOPS for each GiB, with a minimum of 100 IOPS. This relationship means that larger volumes have better performance. In this case the volume is only 100 GB so it will only have 300 IOPS performance.
When using General Purpose SSD storage, a DB instance receives an initial I/O credit balance of 5.4 million I/O credits. This initial credit balance is enough to sustain a burst performance of 3,000 IOPS for 30 minutes. This balance is designed to provide a fast initial boot cycle for boot volumes and to provide a good bootstrapping experience for other applications.
Volumes earn I/O credits at the baseline performance rate of 3 IOPS for each GiB of volume size. For example, a 100-GiB SSD volume has a baseline performance of 300 IOPS.
It is clear that in this scenario the increased load has caused the I/O credit balance to become exhausted before the end of the peak shopping period. This means that performance will be limited until there is sufficient I/O credit.
CORRECT:
"A large number of reads and writes exhausted the I/O credit balance due to provisioning low disk storage during the setup phase" is the correct answer.
INCORRECT:
"The increased load caused the data in the tables to change frequently, requiring indexes to be rebuilt to optimize queries" is incorrect. Reading and writing items to the table should not result in indexes being rebuilt.
INCORRECT:
"The increased load resulted in the maximum number of allowed connections to the database instance" is incorrect. MySQL on RDS can have up to 100,000 client connections. In this case the application servers are the clients and it is unlikely there are that many app servers.
INCORRECT:
"A large number of reads and writes exhausted the network bandwidth available to the RDS for MySQL DB instance" is incorrect. Based on the storage configuration presented it is far more likely that storage performance is the issue as in this setup it will be exhausted long before the network bandwidth.
References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

## Câu 55 — ✅ ĐÚNG

<!-- source: T5Q26 · domain: CI -->

### Câu hỏi

A start-up company has created a new serverless application which includes an AWS Lambda function which sits behind an Amazon API gateway and an Amazon CloudFront CDN. The development team is currently using AWS CLI scripts to update the versions of Lambda functions. In case an error is detected, a different CLI script is used to roll back the version to the previous stable one.
A solutions architect needs to optimize this process and reduce the time taken to switch versions and detect the error in Lambda functions.
How can this be accomplished?

### Các phương án

- **A.** Add the AWS CloudFront distribution and API Gateway in the parent stack and AWS Lambda in a child stack. Within these nested stacks, when changes are to be introduced to AWS Lambda create an AWS CloudFormation change set and deploy. Revert the AWS CloudFormation change set to the previous version in case of failure.
- **B.** Use AWS SAM and built-in AWS CodeDeploy to deploy the new Lambda version, gradually shift traffic to the new version, and use pre-traffic and post-traffic test functions to verify code. Rollback in case Amazon CloudWatch alarms is triggered.
- **C.** Merge the AWS CLI scripts into a single script that deploys the new Lambda version. Execute these scripts when deployment is completed. If errors are detected, revert to the previous Lambda version.
- **D.** Create an AWS CloudFormation stack with API Gateway endpoint resource that references the new Lambda version. Change the CloudFront origin to the new API Gateway endpoint in case of success, else rollback to the previous version.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Explanation:
AWS CodeDeploy leverages Lambda’s traffic shifting capabilities to automate the gradual rollout of new function versions. It can also help you use deployment best practices, such as testing a new change on a small portion of traffic before deploying it to all customers. For example, CodeDeploy lets you automate pre-deployment tests that a function must pass before it begins taking traffic. You can also set alarms that automatically trigger rollbacks in the event of errors.
CORRECT:
"Use AWS SAM and built-in AWS CodeDeploy to deploy the new Lambda version, gradually shift traffic to the new version, and use pre-traffic and post-traffic test functions to verify code. Rollback in case Amazon CloudWatch alarms is triggered" is the correct answer (as explained above.)
INCORRECT:
"Add the AWS CloudFront distribution and API Gateway in the parent stack and AWS Lambda in a child stack. Within these nested stacks, when changes are to be introduced to AWS Lambda create an AWS CloudFormation change set and deploy. Revert the AWS CloudFormation change set to the previous version in case of failure" is incorrect.
Change sets don’t indicate whether AWS CloudFormation will successfully update a stack. It needs manual intervention to check the error and provide a resolution hence this is not a correct option.
INCORRECT:
"Merge the AWS CLI scripts into a single script that deploys the new Lambda version. Execute these scripts when deployment is completed. If errors are detected, revert to the previous Lambda version" is incorrect.
Even though CLI provides finer grain control to the AWS resources, this is more suitable for a development environment since debugging is tougher and needs manual effort. Therefore, the CLI does not reduce the amount of effort and is not a preferable option.
INCORRECT:
"Create an AWS CloudFormation stack with API Gateway endpoint resource that references the new Lambda version. Change the CloudFront origin to the new API Gateway endpoint in case of success, else rollback to the previous version" is incorrect.
While this is feasible, to detect the error, the CloudFormation output needs to be checked, lambda logs need to be checked and then CloudFront origin needs to be changed. Since the question is asking about reducing the time, this is also not a correct option.
References:
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-developer-tools/

## Câu 56 — ❌ SAI

<!-- source: T6Q2 · domain: ORG -->

### Câu hỏi

A company is creating an account structure on AWS. There will be separate accounts for the production and testing environments. The Solutions Architect wishes to implement centralized control of security identities and permissions to access the environments.
Which solution is most appropriate for these requirements?

### Các phương án

- **A.** Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the production and testing accounts. Add the identity account to the trust policies for the roles.
- **B.** Create an AWS Organization that includes the production and testing accounts. Create IAM user accounts in the production and testing accounts and implement service control policies (SCPs) to centrally control permissions.
- **C.** Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the identity account and delegate access to the production and testing accounts.
- **D.** Create all user accounts in the production account. Create roles for access in the production account and testing accounts. Grant cross-account access from the production account to the testing account.

> **Bạn chọn:** B
> **Đáp án đúng:** A

### Giải thích

The AWS best practice for this situation is to use an identity account to store all user and service accounts. You then create roles in the accounts you want to access and delegate permissions for the identity account users (or the whole account) to be able to assume the role. This provides centralized control of security identities.
The configuration for cross-account access between two accounts is depicted below. In this diagram the user in account B (the identity account) is able to assume a role in account A (the resource account) and access an S3 bucket.
CORRECT:
"Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the production and testing accounts. Add the identity account to the trust policies for the roles" is the correct answer.
INCORRECT:
"Create an AWS Organization that includes the production and testing accounts. Create IAM user accounts in the production and testing accounts and implement service control policies (SCPs) to centrally control permissions" is incorrect. The identities should be created in a separate identity account as Organizations does not provide centralized control of identities as they are always created within individual accounts. SCPs control the maximum available permissions but to not actually control the IAM permissions assigned to users.
INCORRECT:
"Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the identity account and delegate access to the production and testing accounts" is incorrect. The roles should be created in the production and testing accounts, not in the identity account.
INCORRECT:
"Create all user accounts in the production account. Create roles for access in the production account and testing accounts. Grant cross-account access from the production account to the testing account" is incorrect. A separate account should be created for identities.
References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 57 — ✅ ĐÚNG

<!-- source: T3Q28 · domain: CI -->

### Câu hỏi

A company offers a photo sharing application to its users through a social networking app. To ensure images can be displayed with consistency, a single Amazon EC2 instance running JavaScript code processes the photos and stores the processed images in an Amazon S3 bucket. A front-end application runs from a static website in another S3 bucket and loads the processed images for display in the app.
The company has asked a Solutions Architect to make some recommendations for a cost-effective solution that offers massive scalability for a global user base.
Which combination of changes should the Solutions Architect recommend? (Select TWO.)

### Các phương án

- **A.** Place the image processing EC2 instance into an Auto Scaling group.
- **B.** Replace the EC2 instance with AWS Lambda to run the image processing tasks.
- **C.** Replace the EC2 instance with Amazon Rekognition for image processing.
- **D.** Create an Amazon CloudFront distribution in front of the processed images bucket.
- **E.** Deploy the applications in an Amazon ECS cluster and apply Service Auto Scaling.

> **Bạn chọn:** B, D
> **Đáp án đúng:** B, D

### Giải thích

Though it is not clearly documented the image processing task is likely to take less than the maximum execution time for a Lambda function (15 minutes). Therefore, Lambda could be more cost-effective and will be highly scalable.
Amazon CloudFront can be used with an origin configured as the S3 bucket with the processed images. This will provide a better user experience as users of the app in multiple geographies can retrieve images cached at edge locations with great performance.
CORRECT:
"Replace the EC2 instance with AWS Lambda to run the image processing tasks" is a correct answer.
CORRECT:
"Create an Amazon CloudFront distribution in front of the processed images bucket" is also a correct answer.
INCORRECT:
"Place the image processing EC2 instance into an Auto Scaling group" is incorrect. This will provide some improvements but it does not represent as much of an improvement as Lambda. Lambda is likely to be cheaper will scale very well for this application.
INCORRECT:
"Replace the EC2 instance with Amazon Rekognition for image processing" is incorrect. The question states that the images are being processed for “consistency”. Though this is vague, it is unlikely to mean identifying objects or performing the type of analysis Rekognition performs.
INCORRECT:
"Deploy the applications in an Amazon ECS cluster and apply Service Auto Scaling" is incorrect. This is also a valid solution for the image processing but less cost-effective than Lambda.
References:
https://aws.amazon.com/lambda/features/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 58 — ✅ ĐÚNG

<!-- source: T4Q29 · domain: MIG -->

### Câu hỏi

A company leases data center space in a co-location facility and needs to move out before the end of the financial year in 90 days. The company currently runs 150 virtual machines and a NAS device that holds over 50 TB of data. Access patterns for the data are infrequent but when access is required it must be immediate. The VM configurations are highly customized. The company has a 1 Gbps internet connection which is mostly idle and almost completely unused outside of business hours.
Which combination of steps should a Solutions Architect take to migrate the VMs to AWS with minimal downtime and operational impact? (Select TWO.)

### Các phương án

- **A.** Launch new Amazon EC2 instances and reinstall all applications.
- **B.** Migrate the virtual machines with AWS Application Migration Service.
- **C.** Migrate the NAS data to AWS using AWS Storage Gateway.
- **D.** Migrate the NAS data to AWS using AWS Snowball.
- **E.** Copy infrequently accessed data from the NAS using AWS SMS.

> **Bạn chọn:** B, C
> **Đáp án đúng:** B, C

### Giải thích

AWS Application Migration Service (AWS MGN) simplifies the migration of virtual machines to AWS. It allows for minimal downtime because it uses continuous block-level replication, ensuring that the source machines are synchronized with the target AWS environment up until the cutover is executed.
This service is ideal for the company's needs because it can handle highly customized VM configurations, ensuring that all the unique settings and data are preserved during the migration. It operates in the background, which aligns with the requirement for minimal operational impact.
AWS Storage Gateway is a hybrid cloud storage service that allows on-premises environments to seamlessly use AWS cloud storage. For the company's NAS device holding over 50 TB of data with infrequent access patterns but requiring immediate access when needed, the File Gateway configuration of AWS Storage Gateway is a suitable solution.
File Gateway provides a set of NFS and SMB file shares, making it easy to integrate with existing file-based applications and workflows. It caches frequently accessed data on-premises for low-latency access, while storing data in Amazon S3 for cost-effective, durable storage.
This approach meets the company's access pattern requirements without the need for significant changes to their applications.
CORRECT:
"Migrate the virtual machines with AWS Application Migration Service" is a correct answer.
CORRECT:
"Migrate the NAS data to AWS using AWS Storage Gateway" is also a correct answer.
INCORRECT:
"Launch new Amazon EC2 instances and reinstall all applications" is incorrect. The VMs are individually customized so there would too many configuration updates to make this a viable solution.
INCORRECT:
"Migrate the NAS data to AWS using AWS Snowball" is incorrect. This would mean the data is offline for many days which is not ideal. It is also unnecessary as the data can be easily migrated across the existing internet connection within acceptable timeframes.
INCORRECT:
"Copy infrequently accessed data from the NAS using AWS SMS" is incorrect. SMS is used for migrating servers not data from a NAS device.
References:
https://aws.amazon.com/storagegateway/file/
https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-migration-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

## Câu 59 — ❌ SAI

<!-- source: T1Q5 · domain: ORG -->

### Câu hỏi

A company requires that only the master account in AWS Organizations is able to purchase Amazon EC2 Reserved Instances. Current and future member accounts should be blocked from purchasing Reserved Instances.
Which solution will meet these requirements?

### Các phương án

- **A.** Create an Amazon CloudWatch Events rule that triggers a Lambda function to terminate any Reserved Instances launched by member accounts.
- **B.** Create an OU for the master account and each member account. Move the accounts into their respective OUs. Apply an SCP to the master accounts’ OU with the Allow effect for the ec2:PurchaseReservedInstancesOffering.
- **C.** Move all current member accounts to a new OU. Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the new OU.
- **D.** Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the root of the organization.

> **Bạn chọn:** C
> **Đáp án đúng:** D

### Giải thích

The only solution that works for both existing and future member accounts is to apply a Deny policy to the root of the organization. When you attach a policy to the organization root, all OUs and accounts in the organization inherit that policy which ensures that any new accounts that are added will inherit the policy automatically.
SCPs affect only
member
accounts in the organization. They have no effect on users or roles in the management account (also known as the master account). Therefore, the users in the management account are able to purchase reserved instances.
Note the following behavior in relation to policy inheritance:
You can attach policies to organization entities (organization root, organizational unit (OU), or account) in your organization:
When you attach a policy to the organization root, all OUs and accounts in the organization inherit that policy.
When you attach a policy to a specific OU, accounts that are directly under that OU or any child OU inherit the policy.
When you attach a policy to a specific account, it affects only that account.
CORRECT:
"Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the root of the organization" is the correct answer.
INCORRECT:
"Move all current member accounts to a new OU. Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the new OU" is incorrect. This will work for existing accounts but if new accounts are added and are not added to the same OU they will not inherit the policy.
INCORRECT:
"Create an Amazon CloudWatch Events rule that triggers a Lambda function to terminate any Reserved Instances launched by member accounts" is incorrect. CloudWatch Events is not able to trigger based on EC2 Reserved Instance purchase actions.
INCORRECT:
"Create an OU for the master account and each member account. Move the accounts into their respective OUs. Apply an SCP to the master accounts’ OU with the Allow effect for the ec2:PurchaseReservedInstancesOffering" is incorrect. This is a complex setup and does not deny the relevant API actions from the member accounts.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance.html
https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseReservedInstancesOffering.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 60 — ✅ ĐÚNG

<!-- source: T3Q10 · domain: MIG -->

### Câu hỏi

A financial services company runs an application that allows traders to perform online simulations of market conditions. The backend runs on a fleet of virtual machines in an on-premises data center and the business logic is exposed using a REST API with multiple functions. The trader’s session data is stored in a NAS file system in the on-premises data center. During busy periods of the day the server capacity is insufficient and latency issues have occurred when fetching the session data for a simulation.
A Solutions Architect must create a design for moving the application to AWS. The design must use the same API model but should be capable of scaling for the variable load and ensure access to session data is provided with low-latency.
Which solutions meets these requirements?

### Các phương án

- **A.** Implement the REST API using a Network Load Balancer (NLB). Run the business logic on an Amazon EC2 instance behind the NLB. Store trader session data in Amazon Aurora Serverless.
- **B.** Implement the REST API using an Application Load Balancer (ALB). Run the business logic in AWS Lambda. Store trader session data in Amazon DynamoDB with on-demand capacity.
- **C.** Implement the REST API using AWS AppSync. Run the business logic in AWS Lambda. Store trader session data in Amazon Aurora Serverless.
- **D.** Implement the REST API using Amazon API Gateway. Run the business logic in AWS Lambda. Store trader session data in Amazon DynamoDB with on-demand capacity.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Amazon API Gateway can be used to preserve the API model used in the current application while moving to a serverless technology. The business logic should be moved to AWS Lambda. This will ensure scalability for periods of high demand. Amazon DynamoDB is often used for storing session data. It is a low-latency NoSQL database that is well suited for this use case. This solution meets all of the stated requirements.
CORRECT:
"Implement the REST API using Amazon API Gateway. Run the business logic in AWS Lambda. Store trader session data in Amazon DynamoDB with on-demand capacity" is the correct answer.
INCORRECT:
"Implement the REST API using a Network Load Balancer (NLB). Run the business logic on an Amazon EC2 instance behind the NLB. Store trader session data in Amazon Aurora Serverless" is incorrect. NLBs do not provide REST APIs so you could not use an NLB to process API requests and forward them to the business logic instances.
INCORRECT:
"Implement the REST API using an Application Load Balancer (ALB). Run the business logic in AWS Lambda. Store trader session data in Amazon DynamoDB with on-demand capacity" is incorrect. ALBs do not provide REST APIs so you could not use an ALB to process API requests and forward them to the business logic function.
INCORRECT:
"Implement the REST API using AWS AppSync. Run the business logic in AWS Lambda. Store trader session data in Amazon Aurora Serverless" is incorrect. AppSync is a GraphQL service that is useful for use cases where real-time updates over WebSockets are required. API Gateway is a better fit for this use case to preserve the API model.
References:
https://docs.aws.amazon.com/aws-sdk-php/v2/guide/feature-dynamodb-session-handler.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 61 — ❌ SAI

<!-- source: T4Q26 · domain: MIG -->

### Câu hỏi

A company runs a web application in an on-premises data center in Paris. The application includes stateless web servers behind a load balancer, shared files in a NAS device, and a MySQL database server. The company plans to migrate the solution to AWS and has the following requirements:
· Provide optimum performance for customers.
· Implement elastic scalability for the web tier.
· Optimize the database server performance for read-heavy workloads.
· Reduce latency for users across Europe and the US.
· Design the new architecture with a 99.9% availability SLA.
Which solution should a Solutions Architect propose to meet these requirements while optimizing operational efficiency?

### Các phương án

- **A.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon ElastiCache cluster in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe.
- **B.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and two Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe. Configure EFS cross-Region replication.
- **C.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon DocumentDB table in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes all global locations.
- **D.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and three Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon FSx with cross-Region synchronization. Configure Amazon CloudFront with the ALB as the origin and a price class that includes the US and Europe.

> **Bạn chọn:** D
> **Đáp án đúng:** A

### Giải thích

> ⚠️ FSx supports cross-Region backup copies/replication, contrary to the explanation.

To meet the 99.9% availability SLA a solution in a single Region with Auto Scaling and Load Balancing across multiple AZs is sufficient. To optimize the DB for read-heavy workloads, Amazon ElastiCache can be placed in front of an Aurora MySQL DB. The shared files can be easily moved to an Amazon EFS file system. CloudFront can be used to reduce latency for users in different geographies. In this case US and Europe price classes can be selected in CloudFront and this will cache the content in those locations only which reduces cost.
CORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon ElastiCache cluster in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe" is the correct answer.
INCORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and two Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe. Configure EFS cross-Region replication" is incorrect.
There’s no need to have a cross-Region solution to meet a 99.9% availability SLA and there’s no mechanism mentioned for directing traffic between Regions.
INCORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon DocumentDB table in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes all global locations" is incorrect.
DocumentDB is not a caching engine and cannot be used in front of an Aurora DB. CloudFront should not use a price class the includes all global locations as this will be more costly and is not required in the solution.
INCORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and three Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon FSx with cross-Region synchronization. Configure Amazon CloudFront with the ALB as the origin and a price class that includes the US and Europe" is incorrect.
Amazon FSx also does not have a feature for cross-Region synchronization. There’s also no need to have a cross-Region solution to meet a 99.9% availability SLA and there’s no mechanism mentioned for directing traffic between Regions.
References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 62 — ✅ ĐÚNG

<!-- source: T3Q30 · domain: CI -->

### Câu hỏi

A company has deployed a web application in an Amazon VPC. A CloudFront distribution is used for both scalability and performance. The operations team has noticed that the cache hit ratio has been dropping over time leading to a gradual degradation of the performance for the web application.
The cache metrics report indicates that query strings on some URLs are inconsistently ordered and are specified in a mixture of mixed-case letters.
Which actions can a Solutions Architect take to increase the cache hit ratio and resolve the performance issues on the web application?

### Các phương án

- **A.** Create a Lambda@Edge function to sort parameters by name and force them to be lowercase. Select the CloudFront viewer request trigger to invoke the function.
- **B.** Update the CloudFront distribution to disable caching based on query string parameters.
- **C.** Use AWS WAF to create a WebACL and filter based on the case of the query strings in the URL. Configure WAF to trigger an AWS Lambda function that rewrites the URLs to lowercase.
- **D.** Create a path pattern in the CloudFront distribution that forwards all requests to the origin with case-sensitivity turned off.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Lambda@Edge lets you run Node.js and Python Lambda functions to customize content that CloudFront delivers, executing the functions in AWS locations closer to the viewer. The functions run in response to CloudFront events, without provisioning or managing servers. You can use Lambda functions to change CloudFront requests and responses at the following points:
• After CloudFront receives a request from a viewer (viewer request)
• Before CloudFront forwards the request to the origin (origin request)
• After CloudFront receives the response from the origin (origin response)
• Before CloudFront forwards the response to the viewer (viewer response)
In this scenario the Lambda@Edge function can be written to modify the parameters and rewrite them in lowercase. The function should invoke at the viewer request so that the rewritten query strings can be used to match objects in the cache.
CORRECT:
"Create a Lambda@Edge function to sort parameters by name and force them to be lowercase. Select the CloudFront viewer request trigger to invoke the function" is the correct answer.
INCORRECT:
"Update the CloudFront distribution to disable caching based on query string parameters" is incorrect. This would not help as it would force all of these requests to the web application and reduce performance further.
INCORRECT:
"Use AWS WAF to create a WebACL and filter based on the case of the query strings in the URL. Configure WAF to trigger an AWS Lambda function that rewrites the URLs to lowercase" is incorrect. WAF cannot be configured to directly trigger a Lambda function.
INCORRECT:
"Create a path pattern in the CloudFront distribution that forwards all requests to the origin with case-sensitivity turned off" is incorrect. Path patterns are always case-sensitive and this cannot be turned off.
References:
https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html
https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-not-following-cache-behavior/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

## Câu 63 — ❌ SAI

<!-- source: T4Q15 · domain: MIG -->

### Câu hỏi

A company is running a two-tier web-based application in an on-premises data center. The application layer consists of a single server running a stateless application. The application connects to a PostgreSQL database running on a separate server. A Solutions Architect is planning a migration to AWS. The company requires that the application and database layer must be highly available across three availability zones.
Which solution will meet the company’s requirements?

### Các phương án

- **A.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ and add Aurora Replicas in two more AZs.
- **B.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind a Network Load Balancer. Create an Amazon RDS Multi-AZ PostgreSQL database across two AZs and add a Read Replica in a third AZ.
- **C.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora Global database.
- **D.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind a Network Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ with storage auto scaling enabled.

> **Bạn chọn:** C
> **Đáp án đúng:** A

### Giải thích

All answers include an ASG with Auto Scaling across three AZs. An Application Load Balancer is better suited to this particular use case but a Network Load Balancer could also be used. The key to answering correctly is to choose a storage solution that meets the requirement of high availability across three Availability Zones (AZs).
With Amazon Aurora you can have one writer instance and up to 15 Aurora Replicas. Aurora Replicas are read-only but are automatically promoted to be writer instances in the event of a failure. Therefore, for this solution we can have a single Aurora writer instance and two Aurora Replicas, each in separate AZs.
CORRECT:
"Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ and add Aurora Replicas in two more AZs" is the correct answer.
INCORRECT:
"Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora Global database" is incorrect. Global database is used for cross-Region databases which is not required in this scenario.
INCORRECT:
"Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind a Network Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ with storage auto scaling enabled" is incorrect. Storage auto scaling is enabled for all Aurora databases and does not provide high availability for the database, it provides scaling for the storage.
References:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

## Câu 64 — ✅ ĐÚNG

<!-- source: T3Q8 · domain: CI -->

### Câu hỏi

An application uses Amazon EC2 instances in an Auto Scaling group and an Amazon RDS MySQL database. The web application has occasional spikes of traffic during the day. The operations team have determined the most appropriate instances sizes for both the EC2 instances and the DB instance. All instances use On-Demand pricing.
What of the following steps can be taken to gain the most cost savings without impacting the reliability of the application?

### Các phương án

- **A.** Use Spot instance pricing for the RDS database and the EC2 instances in the Auto Scaling group.
- **B.** Reserve capacity for the RDS database and the minimum number of EC2 instances that are constantly running.
- **C.** Use On-Demand pricing for the RDS database and use Spot pricing for the EC2 instances in the Auto Scaling group
- **D.** Reserve capacity for all EC2 instances and leverage Spot Instance pricing for the RDS database.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

The best cost saving measure is to reserve capacity for the RDS database as it should be adequately sized to handle any small bursts of traffic (RDS must have vertical capacity, or you must offload reads).
For Amazon EC2 instance, a combination of reserved instances and on-demand is the best option. The reserved instances should be used for the steady state usage requirement, and on-demand can be used to handle additional instances launched during busy periods.
CORRECT:
"Reserve capacity for the RDS database and the minimum number of EC2 instances that are constantly running" is the correct answer.
INCORRECT:
"Use Spot instance pricing for the RDS database and the EC2 instances in the Auto Scaling group" is incorrect. Spot instances can be terminated when AWS need the capacity back, this could impact the reliability of the application.
INCORRECT:
"Use On-Demand pricing for the RDS database and use Spot pricing for the EC2 instances in the Auto Scaling group" is incorrect. This is not the most cost-effective choice and leaves the web application vulnerable to instance termination.
INCORRECT:
"Reserve capacity for all EC2 instances and leverage Spot Instance pricing for the RDS database" is incorrect. This option does not cater for the spikes in load and leaves the DB vulnerable to instance termination.
References:
https://aws.amazon.com/ec2/pricing/reserved-instances/
https://aws.amazon.com/ec2/spot/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 65 — ✅ ĐÚNG

<!-- source: T5Q6 · domain: CI -->

### Câu hỏi

A Solutions Architect is designing a publicly accessible web application that runs from an Amazon S3 website endpoint. The S3 website is the origin for an Amazon CloudFront distribution. After deploying the solution the operations team ran some tests and received an “Error 403: Access Denied message” when attempting to connect.
What should the Solutions Architect check to determine the root cause of the issue? (Select TWO.)

### Các phương án

- **A.** Check if the S3 block public access option is enabled on the S3 bucket.
- **B.** Check if object lock is enabled for the objects in the S3 bucket.
- **C.** Check if the storage class for objects in the S3 Standard.
- **D.** Check the object versioning status of the objects in the S3 bucket.
- **E.** Check if the S3 bucket is encrypted using AWS KMS.

> **Bạn chọn:** A, E
> **Đáp án đúng:** A, E

### Giải thích

If your CloudFront distribution is using a website endpoint, verify the following requirements to avoid Access Denied errors:
• Objects in the bucket must be publicly accessible.
• Objects in the bucket can't be encrypted by AWS Key Management Service (AWS KMS).
• The bucket policy must allow access to s3:GetObject.
• If the bucket policy grants public read access, then the AWS account that owns the bucket must also own the object.
• The requested objects must exist in the bucket.
• Amazon S3 Block Public Access must be disabled on the bucket.
• If Requester Pays is enabled, then the request must include the request-payer parameter.
• If you're using a Referer header to restrict access from CloudFront to your S3 origin, then review the custom header.
From this list of potential causes for Access Denied errors we can ascertain that the Solutions Architect should verify if the S3 block public access option is enabled, and whether KMS encryption is enabled on the bucket.
CORRECT:
"Check if the S3 block public access option is enabled on the S3 bucket" is a correct answer.
CORRECT:
"Check if the S3 bucket is encrypted using AWS KMS" is also a correct answer.
INCORRECT:
"Check if object lock is enabled for the objects in the S3 bucket" is incorrect. Object Lock helps prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. This is not a potential cause of an Access Denied error when trying to connect to the website endpoint.
INCORRECT:
"Check if the storage class for objects in the S3 Standard" is incorrect. The storage class does not need to be S3 Standard. There are other storage classes that would work with this solution.
INCORRECT:
"Check the object versioning status of the objects in the S3 bucket" is incorrect. The versioning status is not relevant here.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/s3-website-cloudfront-error-403/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

## Câu 66 — ✅ ĐÚNG

<!-- source: T6Q18 · domain: CI -->

### Câu hỏi

A company has launched a web application on Amazon EC2 instances. The instances have been launched in a private subnet. An Application Load Balancer (ALB) is configured in front of the instances. The instances are assigned to a security group named WebAppSG and the ALB is assigned to a security group named ALB-SG. The security team requires that the security group rules are locked down according to best practice.
What rules should be configured in the security groups? (Select TWO.)

### Các phương án

- **A.** An inbound rule in WebAppSG allowing port 80 from source ALB-SG.
- **B.** An inbound rule in ALB-SG allowing port 80 from WebAppSG.
- **C.** An outbound rule in WebAppSG allowing ports 1024-65535 to destination ALB-SG.
- **D.** An inbound rule in ALB-SG allowing port 80 from source 0.0.0.0/0.
- **E.** An outbound rule in ALB-SG allowing ports 1024-65535 to destination 0.0.0.0/0.

> **Bạn chọn:** A, D
> **Đáp án đúng:** A, D

### Giải thích

The most secure configuration that will allow the required traffic is as follows:
ALB-SG:
· Inbound rule to allow port 80 from 0.0.0.0/0.
· Outbound rule to allow port 80 to WebAppSG (and the health check port if different).
WebAppSG:
· Inbound rule to allow port 80 from the security group ID for ALB-SG.
· Outbound rules are not necessary as the response traffic to the ALB is allowed by default (may require rules for security updates etc.)
CORRECT:
"An inbound rule in WebAppSG allowing port 80 from source ALB-SG" is a correct answer.
CORRECT:
"An inbound rule in ALB-SG allowing port 80 from source 0.0.0.0/0" is also a correct answer.
INCORRECT:
"An inbound rule in ALB-SG allowing port 80 from WebAppSG" is incorrect. The ALB does not receive traffic from the WebAppSG on port 80. The NLB receives incoming traffic from the internet clients on port 80 and response traffic from the EC2 instances on a high numbered port between 1024 and 65535.
INCORRECT:
"An outbound rule in WebAppSG allowing ports 1024-65535 to destination ALB-SG" is incorrect. This is not required with a security group as they are stateful and response traffic is automatically allowed.
INCORRECT:
"An outbound rule in ALB-SG allowing ports 1024-65535 to destination 0.0.0.0/0" is incorrect. As above, this is not required as security groups are stateful.
References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 67 — ✅ ĐÚNG

<!-- source: T6Q24 · domain: NEW -->

### Câu hỏi

A company is in the planning stages for an application projected to hold around 15 TB of data. They require a Recovery Point Objective (RPO) of less than 5 minutes and a Recovery Time Objective (RTO) of less than 15 minutes. The team is seeking a database solution that not only meets these recovery objectives but also allows for cost-effective failover to a backup AWS Region.
Which database solution aligns best with these requirements while minimizing costs?

### Các phương án

- **A.** Deploy an Amazon Aurora DB cluster, schedule snapshots every 5 minutes, and regularly copy these snapshots to a backup Region. In case of a primary Region failure, use these snapshots to restore the database in the secondary Region.
- **B.** Configure an Amazon RDS instance with a cross-Region read replica in an alternative Region. Should the primary Region fail, promote the read replica to become the new primary database.
- **C.** Create an Amazon Aurora DB cluster in the main Region and a separate Aurora cluster in a secondary Region. Utilize AWS Database Migration Service (DMS) to continuously replicate data between the two clusters.
- **D.** Configure an Amazon RDS instance with a read replica within the same Region. In the event of a failure, promote the read replica to serve as the primary database.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Using Amazon RDS with a cross-Region read replica is a cost-effective solution that meets the specified RPO and RTO. The read replica in the secondary Region ensures that the data is continuously replicated, meeting the 5-minute RPO.
In the event of a primary Region failure, the read replica can be quickly promoted to a primary instance, aligning with the 15-minute RTO. This approach provides a balance between cost, data availability, and recovery speed, making it suitable for the company's requirements.
CORRECT:
"Configure an Amazon RDS instance with a cross-Region read replica in an alternative Region. Should the primary Region fail, promote the read replica to become the new primary database" is the correct answer (as explained above.)
INCORRECT:
"Deploy an Amazon Aurora DB cluster, schedule snapshots every 5 minutes, and regularly copy these snapshots to a backup Region. In case of a primary Region failure, use these snapshots to restore the database in the secondary Region" is incorrect.
While Aurora is a powerful database solution, taking and copying snapshots every 5 minutes could be resource-intensive and may not provide the most cost-effective solution.
INCORRECT:
"Create an Amazon Aurora DB cluster in the main Region and a separate Aurora cluster in a secondary Region. Utilize AWS Database Migration Service (DMS) to continuously replicate data between the two clusters" is incorrect.
Using AWS DMS for continuous replication between two Aurora clusters in different Regions can be more expensive and complex than necessary, especially for maintaining a 5-minute RPO.
INCORRECT:
"Configure an Amazon RDS instance with a read replica within the same Region. In the event of a failure, promote the read replica to serve as the primary database" is incorrect.
This setup does not provide failover to a secondary Region, which is a key requirement in the scenario. It's more suited for high availability within the same Region rather than for cross-Region disaster recovery.
References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.XRgn
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-rds/

## Câu 68 — ❌ SAI

<!-- source: T5Q11 · domain: CI -->

### Câu hỏi

A security team has discovered that developers have been storing IAM secret access keys in AWS CodeCommit repositories. The security team requires that measures are put in place to automatically find and remediate all instances of this vulnerability on an ongoing basis.
Which solution meets these requirements?

### Các phương án

- **A.** Create an Amazon Macie job that scans AWS CodeCommit repositories for credentials. If any credentials are found an AWS Lambda function should be triggered that disables the credentials.
- **B.** Use AWS Trusted Advisor to check for unsecured AWS credentials. If any unsecured credentials are found, use AWS Secrets Manager to rotate the credentials.
- **C.** Run a cron job on an Amazon EC2 instance to check the CodeCommit repositories for unsecured credentials. If any unsecured credentials are found, generate new credentials and store them in AWS KMS.
- **D.** Configure a CodeCommit trigger to invoke an AWS Lambda function to scan new code submissions for credentials. If any credentials are found, disable them and notify the user.

> **Bạn chọn:** B
> **Đáp án đúng:** D

### Giải thích

> ⚠️ Relies on CodeCommit (closed to new customers 2024; reportedly reopened late 2025, verify); trigger only scans new pushes, not existing keys.

You can configure a CodeCommit repository so that code pushes or other events trigger actions, such as sending a notification from Amazon Simple Notification Service (Amazon SNS) or invoking a function in AWS Lambda. You can create up to 10 triggers for each CodeCommit repository. In this case you can trigger AWS Lambda to scan the code for access keys
CORRECT:
"Configure a CodeCommit trigger to invoke an AWS Lambda function to scan new code submissions for credentials. If any credentials are found, disable them and notify the user" is correct.
INCORRECT:
"Create an Amazon Macie job that scans AWS CodeCommit repositories for credentials. If any credentials are found an AWS Lambda function should be triggered that disables the credentials" is incorrect. Macie scans Amazon S3 buckets but you cannot see the S3 bucket assigned to CodeCommit as it’s an AWS managed service bucket.
INCORRECT:
"Use AWS Trusted Advisor to check for unsecured AWS credentials. If any unsecured credentials are found, use AWS Secrets Manager to rotate the credentials" is incorrect. Secrets Manager cannot be used for rotating secret access keys.
INCORRECT:
"Run a cron job on an Amazon EC2 instance to check the CodeCommit repositories for unsecured credentials. If any unsecured credentials are found, generate new credentials and store them in AWS KMS" is incorrect. EC2 is not a very cost-effective option for running this task and KMS is used for storing encryption keys, not secret access keys.
References:
https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

## Câu 69 — ✅ ĐÚNG

<!-- source: T5Q31 · domain: NEW · flagged -->

### Câu hỏi

A corporation is seeking to develop a disaster recovery (DR) plan for its web application, which is currently operational in a single AWS Region. This application utilizes a microservices architecture with services running on AWS Fargate within Amazon Elastic Container Service (ECS). The data layer is handled by an Amazon RDS for MySQL database, and DNS management is conducted through Amazon Route 53. An Amazon CloudWatch alarm is configured to trigger an Amazon EventBridge rule in the event of an application failure.
The task is to design a DR strategy that enables quick restoration of the application in a different AWS Region following a failure.
Which approach would best meet these requirements?

### Các phương án

- **A.** Create a new ECS cluster and service on Fargate in an alternate Region. Create an AWS Lambda function to snapshot the RDS database, replicate the snapshot to the new Region, start a new RDS instance from this snapshot, and reconfigure Route 53 to point to the new ECS cluster. Update the EventBridge rule to trigger this Lambda function.
- **B.** Create an AWS Lambda function to automate the deployment of a backup ECS cluster and service in a second Region. This function should: initiate a backup of the RDS database, transfer this backup to the alternate Region, establish a new RDS instance from the backup, and update Route 53 to redirect traffic to the backup ECS cluster. Modify the EventBridge rule to activate this Lambda function.
- **C.** Set up a standby ECS cluster and service on Fargate in a different Region. Create a cross-Region RDS read replica in this new Region. Design an AWS Lambda function to promote the read replica to a primary database and reconfigure Route 53 to reroute traffic to the standby ECS cluster. Adjust the EventBridge rule to include this Lambda function as a target.
- **D.** Create a redundant ECS cluster and service on Fargate in another Region. Regularly back up the RDS database and store these backups in the secondary Region. Create an AWS Lambda function to initiate a new RDS instance from the latest backup and update Route 53 to direct traffic to the redundant ECS cluster when needed. Revise the EventBridge rule to call this Lambda function.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

This solution is efficient for minimizing recovery time in a disaster scenario. By having a standby ECS cluster and service in a different Region and a cross-Region RDS read replica, the application can quickly switch to the standby environment.
The AWS Lambda function plays a crucial role in automating the promotion of the read replica to a primary database and updating Route 53 to ensure traffic is directed to the standby cluster. This approach ensures a rapid transition with minimal downtime.
CORRECT:
"Set up a standby ECS cluster and service on Fargate in a different Region. Create a cross-Region RDS read replica in this new Region. Design an AWS Lambda function to promote the read replica to a primary database and reconfigure Route 53 to reroute traffic to the standby ECS cluster. Adjust the EventBridge rule to include this Lambda function as a target" is the correct answer (as explained above.)
INCORRECT:
"Create a new ECS cluster and service on Fargate in an alternate Region. Create an AWS Lambda function to snapshot the RDS database, replicate the snapshot to the new Region, start a new RDS instance from this snapshot, and reconfigure Route 53 to point to the new ECS cluster. Update the EventBridge rule to trigger this Lambda function" is incorrect.
While creating a new ECS cluster and using a Lambda function to handle snapshots and Route 53 updates is a viable strategy, it may not be as efficient as using a read replica, especially in terms of data synchronization and recovery time.
INCORRECT:
"Create an AWS Lambda function to automate the deployment of a backup ECS cluster and service in a second Region. This function should: initiate a backup of the RDS database, transfer this backup to the alternate Region, establish a new RDS instance from the backup, and update Route 53 to redirect traffic to the backup ECS cluster. Modify the EventBridge rule to activate this Lambda function" is incorrect.
Automating the deployment of a backup ECS cluster through a Lambda function is a good approach, but the process of initiating a backup and establishing a new RDS instance from it could be more time-consuming compared to using a read replica.
INCORRECT:
"Create a redundant ECS cluster and service on Fargate in another Region. Regularly back up the RDS database and store these backups in the secondary Region. Create an AWS Lambda function to initiate a new RDS instance from the latest backup and update Route 53 to direct traffic to the redundant ECS cluster when needed. Revise the EventBridge rule to call this Lambda function" is incorrect.
Establishing a redundant ECS cluster and storing regular RDS backups in another Region is a valid strategy, but it might lead to longer recovery times due to the need to initiate a new RDS instance from backups during a disaster event.
References:
https://aws.amazon.com/disaster-recovery/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-ecs-and-eks/

## Câu 70 — ❌ SAI

<!-- source: T6Q27 · domain: CI · flagged -->

### Câu hỏi

A company hosts a business-critical monolithic application on an Amazon EC2 instance which is installed on an instance launched from an Amazon Linux 2 AMI. The company requires that the data on the attached EBS volumes must be backed up to a specific Amazon S3 bucket managed by the company.
The security team has mandated against owning any SSH keys for instances, so the operations team are unable to SSH into the instance.
Which solution will meet these requirements with the least impact on the critical application?

### Các phương án

- **A.** Attach an IAM role to the instance with permissions to write to Amazon S3. Use the AWS Systems Manager Session Manager to gain access to the instance and run commands to copy data into Amazon S3.
- **B.** Create an image of the instance with the reboot option turned on. Launch a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3.
- **C.** Take a snapshot of the EBS volume by using Amazon Data Lifecycle Manager (Amazon DLM). Use the EBS direct APIs to copy the data from the snapshot to Amazon S3.
- **D.** Create a new AMI image from the current EC2 instance and spin up a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3.

> **Bạn chọn:** A
> **Đáp án đúng:** C

### Giải thích

Amazon Data Lifecycle Manager provides an automated, policy-based lifecycle management solution for Amazon Elastic Block Store (EBS) Snapshots and EBS-backed Amazon Machine Images (AMIs). Automate the creation of point-in-time copy of your block storage data with user-defined policies that you can customize based on data protection needs. Amazon Data Lifecycle Manager requires no scripting or special training.
You can use the Amazon Elastic Block Store (Amazon EBS) direct APIs to create EBS snapshots, write data directly to your snapshots, read data on your snapshots, and identify the differences or changes between two snapshots. These APIs can be used to read the data from the snapshot and copy the data to Amazon S3.
CORRECT:
"Take a snapshot of the EBS volume by using Amazon Data Lifecycle Manager (Amazon DLM). Use the EBS direct APIs to copy the data from the snapshot to Amazon S3" is the correct answer (as explained above).
INCORRECT:
"Attach an IAM role to the instance with permissions to write to Amazon S3. Use the AWS Systems Manager Session Manager to gain access to the instance and run commands to copy data into Amazon S3" is incorrect.
Running manual commands on a business-critical instance isn't recommended and DLM can safely take the snapshot without needing to log in to the instance in any way.
INCORRECT:
"Create an image of the instance with the reboot option turned on. Launch a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3" is incorrect.
The reboot option will cause the business-critical application to be rebooted which has an impact on availability.
INCORRECT:
"Create a new AMI image from the current EC2 instance and spin up a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3" is incorrect.
This is unnecessary as DLM can safely take a backup of the EBS volume using a snapshot.
References:
https://aws.amazon.com/blogs/storage/automating-amazon-ebs-snapshots-management-using-data-lifecycle-manager/
https://aws.amazon.com/ebs/data-lifecycle-manager/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-ebs/

## Câu 71 — ❌ SAI

<!-- source: T3Q6 · domain: ORG · flagged -->

### Câu hỏi

A large financial services company with multiple business units plans to migrate workloads to AWS. The company wants to implement a multi-account strategy to separate workloads, ensure strong security boundaries, and delegate limited administrative control to individual business units.
Key requirements include:
· Centralized governance and visibility across all AWS accounts
· Enforced compliance through guardrails and service control policies (SCPs)
· Integration with the corporate Microsoft Active Directory for authentication
· Role-based access to AWS accounts and resources for employees
· Minimal custom development and operational overhead
Which solution will BEST meet these requirements?

### Các phương án

- **A.** Use AWS Organizations and manually create accounts. Configure IAM federation in each account using SAML with Microsoft AD. Apply SCPs and manage access permissions using IAM roles.
- **B.** Deploy AWS Control Tower to set up a landing zone. Use Account Factory for account provisioning. Integrate IAM Identity Center with Microsoft Active Directory and manage access centrally using permission sets and SCPs.
- **C.** Use AWS Single Sign-On (SSO) integrated with Active Directory. Manually create accounts in AWS Organizations and configure permissions in each account using IAM groups and roles.
- **D.** Create a single AWS account. Use IAM Identity Center integrated with Microsoft AD to manage access to resources. Apply IAM policies for role-based access control.

> **Bạn chọn:** A
> **Đáp án đúng:** B

### Giải thích

This question tests your knowledge of governance, identity management, and automation in a multi-account AWS environment.
CORRECT:
"Deploy AWS Control Tower to set up a landing zone. Use Account Factory for account provisioning. Integrate IAM Identity Center with Microsoft Active Directory and manage access centrally using permission sets and SCPs."
is the correct answer.
AWS Control Tower automates the setup of a secure multi-account environment, including SCPs and governance baselines. It integrates natively with AWS Organizations and IAM Identity Center (formerly AWS SSO), which supports directory integration and centralized permission management. This solution minimizes custom coding and meets all technical requirements efficiently.
INCORRECT:
"Use AWS Organizations and manually create accounts. Configure IAM federation in each account using SAML with Microsoft AD. Apply SCPs and manage access permissions using IAM roles."
is incorrect.
While AWS Organizations and SCPs provide governance, manually managing accounts and setting up SAML-based federation in each account adds significant operational overhead. There's no centralized access management, which violates the minimal effort requirement.
INCORRECT:
"Use AWS Single Sign-On (SSO) integrated with Active Directory. Manually create accounts in AWS Organizations and configure permissions in each account using IAM groups and roles."
is incorrect.
This approach lacks automation and governance. Although AWS SSO (now IAM Identity Center) can integrate with AD, the manual account creation and distributed IAM role setup in each account increases complexity and undermines centralized control.
INCORRECT:
"Create a single AWS account. Use IAM Identity Center integrated with Microsoft AD to manage access to resources. Apply IAM policies for role-based access control."
is incorrect.
This violates the requirement for a multi-account strategy and strong workload isolation. Using one account for multiple business units leads to governance, security, and billing challenges, making it unsuitable for large enterprise structures.
References:
https://docs.aws.amazon.com/controltower/
https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

## Câu 72 — ✅ ĐÚNG

<!-- source: T4Q1 · domain: NEW -->

### Câu hỏi

A company captures financial transactions in Amazon DynamoDB tables. The security team is concerned about identifying fraudulent behavior and has requested that all changes to items stored in DynamoDB tables must be logged within 30 minutes.
How can a Solutions Architect meet this requirement?

### Các phương án

- **A.** Copy the DynamoDB tables into Apache Hive tables on Amazon EMR every hour and analyze them for anomalous behaviors. Send Amazon SNS notifications when anomalous behaviors are detected.
- **B.** Use AWS CloudTrail to capture all the APIs that change the DynamoDB tables. Send SNS notifications when anomalous behaviors are detected using CloudTrail event filtering.
- **C.** Use Amazon DynamoDB Streams to capture and send updates to AWS Lambda. Create a Lambda function to output records to Amazon Kinesis Data Streams. Analyze any anomalies with Amazon Kinesis Data Analytics. Send SNS notifications when anomalous behaviors are detected.
- **D.** Use event patterns in Amazon CloudWatch Events to capture DynamoDB API call events with an AWS Lambda function as a target to analyze behavior. Send SNS notifications when anomalous behaviors are detected.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

> ⚠️ Kinesis Data Analytics is now Managed Service for Apache Flink.

DynamoDB Streams captures a time-ordered sequence of item-level modifications in a DynamoDB table. DynamoDB is integrated with AWS Lambda so that you can create
triggers
—pieces of code that automatically respond to events in DynamoDB Streams.
With triggers, you can build applications that react to data modifications in DynamoDB tables. In this case the Lambda function can process the data and place it in a Kinesis Data Stream where Data Analytics can analyze the data and send an SNS notification if any fraudulent behavior is detected.
The diagram below depicts how data is updated in the table (1), the modification is added to the stream (2), and then AWS Lambda processes the record (3). The record of the update can then be analyzed using Kinesis (not shown).
CORRECT:
"Use Amazon DynamoDB Streams to capture and send updates to AWS Lambda. Create a Lambda function to output records to Amazon Kinesis Data Streams. Analyze any anomalies with Amazon Kinesis Data Analytics. Send SNS notifications when anomalous behaviors are detected" is the correct answer.
INCORRECT:
"Use event patterns in Amazon CloudWatch Events to capture DynamoDB API call events with an AWS Lambda function as a target to analyze behavior. Send SNS notifications when anomalous behaviors are detected" is incorrect. To capture item-level modification DynamoDB streams should be used, capturing API calls will not help.
INCORRECT:
"Copy the DynamoDB tables into Apache Hive tables on Amazon EMR every hour and analyze them for anomalous behaviors. Send Amazon SNS notifications when anomalous behaviors are detected" is incorrect. This solution uses the wrong features and tools for the job and is not as automated as the correct answer.
INCORRECT:
"Use AWS CloudTrail to capture all the APIs that change the DynamoDB tables. Send SNS notifications when anomalous behaviors are detected using CloudTrail event filtering" is incorrect. Capturing API calls does not give you the information you need at an item-level. To capture the changes to the items you must use DynamoDB streams.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

## Câu 73 — ✅ ĐÚNG

<!-- source: T1Q9 · domain: NEW · flagged -->

### Câu hỏi

A company is testing an application that collects data from sensors fitted to vehicles. The application collects usage statistics data every 4 minutes. The data is sent to Amazon API Gateway, it is then processed by an AWS Lambda function and the results are stored in an Amazon DynamoDB table.
As the sensors have been fitted to more vehicles, and as more metrics have been configured for collection, the Lambda function execution time has increased from a few seconds to over 2 minutes. There are also many TooManyRequestsException errors being generated by Lambda.
Which combination of changes will resolve these issues? (Select TWO.)

### Các phương án

- **A.** Use Amazon EC2 instead of Lambda to process the data.
- **B.** Increase the CPU units assigned to the Lambda functions.
- **C.** Increase the memory available to the Lambda functions.
- **D.** Collect data in an Amazon SQS FIFO queue, which triggers a Lambda function to process each message.
- **E.** Stream the data into an Amazon Kinesis data stream from API Gateway and process the data in batches.

> **Bạn chọn:** C, E
> **Đáp án đúng:** C, E

### Giải thích

To optimize the function execution time, the memory assigned to the Lambda functions can be increased. This will proportionally increase the amount of CPU assigned to each function execution.
The TooManyRequestsException error from Lambda can be resolved by configuring API Gateway to place incoming data into a Kinesis data stream. AWS Lambda can then process the data in batches which is more efficient.
CORRECT:
"Increase the memory available to the Lambda functions" is the correct answer.
CORRECT:
"Stream the data into an Amazon Kinesis data stream from API Gateway and process the data in batches" is also a correct answer.
INCORRECT:
"Use Amazon EC2 instead of Lambda to process the data" is incorrect. There is no reason to use EC2 in place of Lambda. This would not be more cost-effective and does not offer any advantages to this solution.
INCORRECT:
"Increase the CPU units assigned to the Lambda functions" is incorrect. You do not directly increase the CPU assigned to Lambda functions, you increase the memory assigned and that automatically adjust the amount of CPU assigned.
INCORRECT:
"Collect data in an Amazon SQS FIFO queue, which triggers a Lambda function to process each message" is incorrect. This is less efficient in terms of the number of function executions as it does not include batching.
References:
https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html
https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

## Câu 74 — ❌ SAI

<!-- source: T5Q10 · domain: CI · flagged -->

### Câu hỏi

A company uses an AWS account with resources deployed in multiple Regions globally. Operations teams deploy and manage resources within each Region. Some Region-specific service quotas have been reached causing an inability for the local operations teams to deploy resources. A centralized cloud team is responsible for monitoring and updating service quotas. The cloud team needs to create an automated and operationally efficient solution to proactively monitor service quotas. Monitoring should occur every 15 minutes and send alerts when a team exceeds 80% utilization.
Which solution will meet these requirements?

### Các phương án

- **A.** Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the GetServiceQuota API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team.
- **B.** Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the ListServiceQuotas API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team.
- **C.** Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, use AWS Budgets to send an alert to the cloud team.
- **D.** Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team.

> **Bạn chọn:** C
> **Đáp án đúng:** D

### Giải thích

> ⚠️ Dated approach; now Service Quotas native CloudWatch usage alarms. Answer D still best of options.

Amazon EventBridge (formerly Amazon CloudWatch Events) can be used to run a function on a schedule. The function can retrieve the most current utilization and service limit data. The function can then trigger an SNS topic if the utilization is above 80%. This solution meets all requirements.
CORRECT:
"Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team" is the correct answer.
INCORRECT:
"Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, use AWS Budgets to send an alert to the cloud team" is incorrect.
AWS Budgets is used for tracking and alerting on spend on your AWS account, it is not a messaging service for alerting.
INCORRECT:
"Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the GetServiceQuota API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team" is incorrect.
The GetServiceQuota API will simply list the current quota, it does not return data showing how much of that quota has been utilized.
INCORRECT:
"Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the ListServiceQuotas API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team" is incorrect.
The ListServiceQuotas API lists the service quota applied to a specific service. It also does not return data showing how much of that quota has been utilized.
References:
https://docs.aws.amazon.com/awssupport/latest/user/trustedadvisor.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

## Câu 75 — ✅ ĐÚNG

<!-- source: T2Q6 · domain: CI -->

### Câu hỏi

A company provides a service that allows users to upload high-resolution product images using an app on their phones for a price matching service. The service currently uses Amazon S3 in the us-west-1 Region. The company has expanded to Europe and users in European countries are experiencing significant delays when uploading images.
Which combination of changes can a Solutions Architect make to improve the upload times for the images? (Select TWO.)

### Các phương án

- **A.** Redeploy the application to use Amazon S3 multipart upload.
- **B.** Create an Amazon CloudFront distribution with the S3 bucket as an origin.
- **C.** Configure the client application to use byte-range fetches.
- **D.** Configure the S3 bucket to use S3 Transfer Acceleration.
- **E.** Modify the Amazon S3 bucket to use Intelligent Tiering.

> **Bạn chọn:** A, D
> **Đáp án đúng:** A, D

### Giải thích

Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between a client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.
Transfer Acceleration is a good solution for the following use cases:
- You have customers that upload to a centralized bucket from all over the world.
- You transfer gigabytes to terabytes of data on a regular basis across continents.
- You are unable to utilize all of your available bandwidth over the Internet when uploading to Amazon S3.
Multipart upload transfers parts of the file in parallel and can speed up performance. This should definitely be built into the application code. Multipart upload also handles the failure of any parts gracefully, allowing for those parts to be retransmitted.
Transfer Acceleration in combination with multipart upload will offer significant speed improvements when uploading data.
CORRECT:
"Configure the S3 bucket to use S3 Transfer Acceleration" is the correct answer.
CORRECT:
"Redeploy the application to use Amazon S3 multipart upload" is correct.
INCORRECT:
"Create an Amazon CloudFront distribution with the S3 bucket as an origin" is incorrect. CloudFront can offer performance improvements for downloading data but to improve upload transfer times, Transfer Acceleration should be used.
INCORRECT:
"Configure the client application to use byte-range fetches" is incorrect. This is a technique that is used when reading (not writing) data to fetch only the parts of the file that are required.
References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-migration-sap/
