# TD Set 2 — Timed retake (2026-10-16)

**Kết quả:** 67/75 câu đúng (89.33%)

## Câu 1 — ✅ ĐÚNG

### Câu hỏi

An electronics and communications company in Japan has several VPCs in the AWS cloud. It uses NAT instances to allow multiple EC2 instances from the private subnet to initiate connections to the Internet while also restricting any requests coming from the outside network. However, there are numerous incidents where the NAT instance is not available, which affects the batch processing of critical applications.



Which is the most suitable solution that provides better availability and bandwidth to the current infrastructure with minimal administrative effort?

### Các phương án

- **A.** Create a NAT gateway then specify its corresponding subnet and Elastic IP address. Update the route tables of the private subnet to point the Internet traffic to the NAT gateway.
- **B.** Launch a larger NAT instance with the enhanced networking feature enabled to improve the availability and performance of the NAT device.
- **C.** Launch two large NAT instances in two separate public subnets and add a route from the private subnet to each NAT instance to make it more fault-tolerant and highly available.
- **D.** Create an egress-only Internet gateway. Update the route tables of the private subnet to point the Internet traffic to the egress-only Internet gateway.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

You can use a **NAT**  device to enable instances in a private subnet to connect to the internet (for example, for software updates) or other AWS services, but prevent the internet from initiating connections with the instances. A NAT device forwards traffic from the instances in the private subnet to the internet or other AWS services, and then sends the response back to the instances. When traffic goes to the internet, the source IPv4 address is replaced with the NAT device’s address and similarly, when the response traffic goes to those instances, the NAT device translates the address back to those instances’ private IPv4 addresses.

 

![image](https://media.tutorialsdojo.com/sap_nat_gateway.png)

 

AWS offers two kinds of NAT devices—a ***NAT gateway***  or a ***NAT instance*** . It is recommended to use NAT gateways, as they provide better availability and bandwidth over NAT instances. The NAT Gateway service is also a managed service that does not require your administration efforts.

 

A NAT instance is launched from a NAT AMI and you can choose to use a NAT instance for special purposes. However, this type of NAT device is limited and is not highly available compared with a NAT Gateway.

 

Therefore, the correct answer is: **Create a NAT gateway then specify its corresponding subnet and Elastic IP address. Update the route tables of the private subnet to point the Internet traffic to the NAT gateway.**

 

The option that says: **Launch a larger NAT instance with the enhanced networking feature enabled to improve the availability and performance of the NAT device**  is incorrect. Even if you upgrade your NAT device to a larger instance, it would still be a single component. This means that if your NAT instance goes down, there would be no other instance to handle the requests, which means that your architecture is not highly available. It is better to use a NAT Gateway to provide better availability and bandwidth for your infrastructure.

 

The option that says: **Launch two large NAT instances in two separate public subnets and add a route from the private subnet to each NAT instance to make it more fault-tolerant and highly available**  is incorrect. Although this solution is indeed highly available and fault-tolerant, this entails a lot of administrative effort to manage those two NAT instances. Hence, it is still better to use the NAT Gateway service since it is a managed service that does not require administrative effort.

 

The option that says: **Create an egress-only Internet gateway. Update the route tables of the private subnet to point the Internet traffic to the egress-only Internet gateway** is incorrect because an egress-only Internet gateway is primarily used to handle IPv6 traffic, which is not mentioned in this scenario.

 

**References** :

 

[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html)

 

[https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat.html](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat.html)

 

 

**Check out this Amazon VPC Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

---

## Câu 2 — ✅ ĐÚNG

### Câu hỏi

A company has launched a web service in the cloud that analyzes tweets filtered by keywords. This service is hosted on a fleet of on-demand Amazon EC2 instances running in multiple Availability Zones with Auto Scaling, and is load-balanced by an application load balancer. After checking the load balancer logs, the solutions architect noticed that on-demand EC2 instances in one of the AZ’s are not receiving requests.



Which of the following options is the most likely cause of this issue?

### Các phương án

- **A.** EC2 Auto Scaling does not span multiple availability zones.
- **B.** You have to manually add instances in each AZ for them to receive traffic.
- **C.** The availability zone that is not receiving traffic was not associated with the application load balancer.
- **D.** Multi-AZ autoscaling only works in the North Virginia region.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

A load balancer accepts incoming traffic from clients and routes requests to its registered targets (such as EC2 instances) in one or more Availability Zones. The load balancer also monitors the health of its registered targets and routes traffic only to healthy targets. When the load balancer detects an unhealthy target, it stops routing traffic to that target. It then resumes routing traffic to that target when it detects that the target is healthy again.

 

You can enable or disable the Availability Zones for your load balancer at any time. After you enable an Availability Zone, the load balancer starts routing requests to the registered targets in that Availability Zone. Application Load Balancers have cross-zone load balancing on by default, resulting in requests being routed to all registered targets across all Availability Zones. When cross-zone load balancing is off, the load balancer only routes requests to targets in the same Availability Zone.

 

![image](https://media.tutorialsdojo.com/sap_cross_zone_load_balancing_disabled.png)

 

When you enable an Availability Zone for your load balancer, Elastic Load Balancing creates a load balancer node in the Availability Zone. If you register targets in an Availability Zone but do not enable the Availability Zone, these registered targets do not receive traffic. Your load balancer is most effective when each enabled Availability Zone has at least one registered target.

 

Therefore, the correct answer is: **The availability zone that is not receiving traffic was not associated with the application load balancer.**  Most likely, the reason is that the specific AZ is not added to the ELB.

 

The option that says:**EC2 Auto Scaling does not span multiple availability zones**  is incorrect because autoscaling can primarily work with multiple AZs.

 

The option that says:**Multi-AZ autoscaling only works in the North Virginia region**  is incorrect because autoscaling can be enabled for multi-AZ in any single region, not just N. Virginia.

 

The option that says:**You have to manually add instances in each AZ for them to receive traffic**  is incorrect because Auto Scaling automatically registers instances with the ALB target group. Manual addition is not required as long as the AZ is enabled on the ALB.

 

 

**References:**

 

[https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)

 

[https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html)

 

[https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html)

 

 

**Check out this AWS Elastic Load Balancing Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-elastic-load-balancing-elb/](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/)

---

## Câu 3 — ✅ ĐÚNG

### Câu hỏi

A shipping firm runs its web applications on its on-premises data center. The servers have a dependency on non-x86 hardware and the management plans to use AWS to scale its on-premises data storage. However, the backup application is only able to write to POSIX-compatible block-based storage. There is a total of 1,000 TB of data files that need to be mounted to a single folder on the file server. Existing users must also be able to access portions of this data while the backups are taking place.



Which of the following backup solutions would be most appropriate to meet the above requirements?

### Các phương án

- **A.** Use Amazon S3 as the target for your data backups.
- **B.** Provision Gateway Cached Volumes from AWS Storage Gateway.
- **C.** Use Amazon Glacier as the target for your data backups.
- **D.** Provision Gateway Stored Volumes from AWS Storage Gateway.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**AWS Storage Gateway**  connects an on-premises software appliance with cloud-based storage to provide seamless integration with data security features between your on-premises IT environment and the AWS storage infrastructure. You can use the service to store data in the AWS Cloud for scalable and cost-effective storage that helps maintain data security. Gateway-Cached volumes can support volumes of 1,024TB in size, whereas Gateway-stored volume supports volumes of 512 TB size.

 

![image](https://media.tutorialsdojo.com/sap_storage_gateway_stored.png)

 

Therefore, the correct answer is: **Provision Gateway Cached Volumes from AWS Storage Gateway**  is correct because it supports volumes of up to 1,024 TB in size, and the frequently accessed data is stored on the on-premises server while the entire data is backed up over AWS.

 

The option that says: **Use Amazon Glacier as the target for your data backups**  is incorrect. The data stored in Amazon Glacier is not available immediately. Retrieval jobs typically require 3-5 hours to complete.

 

The option that says: **Provision Gateway Stored Volumes from AWS Storage Gateway**  is incorrect. Gateway stored volumes can only store up to 512 TB worth of data.

 

The option that says: **Use Amazon S3 as the target for your data backups**  is incorrect. Amazon S3 is designed for object storage and not ideal for POSIX compliant data.

 

**References** :

 

[https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html)

 

[https://docs.aws.amazon.com/storagegateway/latest/vgw/StorageGatewayConcepts.html#storage-gateway-stored-volume-concepts](https://docs.aws.amazon.com/storagegateway/latest/vgw/StorageGatewayConcepts.html#storage-gateway-stored-volume-concepts)

 

 

**Check out this AWS Storage Gateway Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-storage-gateway/](https://tutorialsdojo.com/aws-storage-gateway/)

 

 

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

 

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 4 — ✅ ĐÚNG

### Câu hỏi

A car parts manufacturing company installed IP cameras along an assembly line. These cameras are part of the quality inspection process, capturing images of each car part and detecting defects by comparing images with baseline references. To improve detection accuracy, the company used Amazon SageMaker AI to train a machine learning (ML) model containing baseline images and common defects.



Upon detection, workers must receive feedback from a Linux server in an on-premises data center that hosts an API for the IP cameras. The company requires the solution to remain operational even when factory internet connectivity is unavailable.



Which of the following options is the recommended solution for deploying the ML model that meets these requirements?

### Các phương án

- **A.** Deploy an AWS Outposts server in the local data center to create an AWS private cloud. Deploy SageMaker AI on this server for ML training, and leverage Amazon Rekognition's computer vision capabilities to detect defects in manufactured car parts.
- **B.** Use SageMaker Ground Truth to label defect images, then deploy the trained model directly to the IP cameras for real-time inference and feedback via the Linux server API.
- **C.** Use SageMaker Edge Manager to deploy and manage the ML model directly on IP cameras, enabling defect detection and transmitting results to the Linux server API.
- **D.** Deploy the AWS IoT Greengrass client software to another local server. Run ML inference on the Greengrass server from the ML model trained from SageMaker AI. Use Greengrass components to interact with the Linux server API whenever a defect is detected.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**AWS IoT Greengrass**  is an open-source Internet of Things (IoT) edge runtime and cloud service that helps you build, deploy and manage IoT applications on your devices. You can use AWS IoT Greengrass to build software that enables your devices to act locally on the data that they generate, run predictions based on machine learning models, and filter and aggregate device data. AWS IoT Greengrass enables your devices to collect and analyze data closer to where that data is generated, react autonomously to local events, and communicate securely with other devices on the local network.

 

**AWS IoT Greengrass**  components are software modules that you deploy to Greengrass core devices. Components can represent applications, runtime installers, libraries, or any code that you would run on a device. You can define components that depend on other components. For example, you might define a component that installs Python and then define that component as a dependency of your components that run Python applications.

 

![image](https://media.tutorialsdojo.com/sap_iot_greengrass_overview.png)

 

With **AWS IoT Greengrass** , you can perform **machine learning (ML)**  inference on your edge devices on locally generated data using cloud-trained models. You benefit from the low latency and cost savings of running local inference yet still take advantage of cloud computing power for training models and complex processing.

 

AWS IoT Greengrass makes the steps required to perform inference more efficient. You can train your inference models anywhere and deploy them locally as machine learning components. For example, you can build and train deep-learning models in **Amazon SageMaker AI**  or computer vision models in Amazon Lookout for Vision.

 

Therefore, the correct answer is: **Deploy the AWS IoT Greengrass client software to another local server. Run ML inference on the Greengrass server from the ML model trained from SageMaker AI. Use Greengrass components to interact with the Linux server API whenever a defect is detected.** AWS IoT Greengrass makes it easy to perform machine learning inference locally on devices, using models that are created, trained, and optimized in the cloud. AWS IoT Greengrass provides prebuilt components for common use cases which includes interacting with external APIs.

 

The option that says: **Deploy an AWS Outposts server in the local data center to create an AWS private cloud. Deploy SageMaker AI on this server for ML training, and leverage Amazon Rekognition’s computer vision capabilities to detect defects in manufactured car parts**  is incorrect. Although AWS Outposts support running some AWS services such as ECS, IoT Greengrass, and SageMaker Edge, it does not support running Amazon Rekognition locally.

 

The option that says: **Use SageMaker Ground Truth to label defect images, then deploy the trained model directly to the IP cameras for real-time inference and feedback via the Linux server API**  is incorrect. Amazon SageMaker Ground Truth is only used for labeling training datasets, not for deploying or running ML models. It only prepares data for training and does not support real-time inference or integration with local systems, such as the Linux server API.

 

The option that says: **Use SageMaker Edge Manager to deploy and manage the ML model directly on IP cameras, enabling defect detection and transmitting results to the Linux server API**  is incorrect because this service is primarily designed for managing models on edge devices, but it does not provide the necessary infrastructure for real-time local ML inference on a server. Deploying ML models directly on IP cameras is impractical for complex ML workloads due to hardware limitations.

 

 

**References:**

 

[https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-components.html](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-components.html)

 

[https://docs.aws.amazon.com/greengrass/v2/developerguide/perform-machine-learning-inference.html](https://docs.aws.amazon.com/greengrass/v2/developerguide/perform-machine-learning-inference.html)

 

[https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)

 

 

**Check out this Amazon SageMaker AI Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-sagemaker/](https://tutorialsdojo.com/amazon-sagemaker/)

---

## Câu 5 — ✅ ĐÚNG

### Câu hỏi

A multinational software provider in the US hosts both of its development and test environments in the AWS cloud. The CTO decided to use separate AWS accounts in hosting each environment. The solutions architect has enabled Consolidated Billing to link each of the accounts’ bill to a Master AWS account. To make sure that each account is kept within the budget, the administrators in the master account must have the power to stop, delete, and/or terminate resources in both development and test environment AWS accounts.



Which of the following options is the recommended action to meet the requirements for this scenario?

### Các phương án

- **A.** First, create IAM users in the master account. Then in the Dev and Test accounts, generate cross-account roles that have full admin permissions while granting access for the master account.
- **B.** By linking all accounts under Consolidated Billing, you will be able to provide IAM users in the master account access to Dev and Test account resources.
- **C.** IAM users with full admin permissions will be created in the master account. In both Dev and Test accounts, generate cross-account roles that would grant the master account access to Dev and Test account resources through permissions inherited from the master account.
- **D.** In the master account, you are to create IAM users and a cross-account role that has full admin permissions to the Dev and Test accounts.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

You share resources in one account with users in a different account. By setting up cross-account access in this way, you don’t need to create individual IAM users in each account. In addition, users don’t have to sign out of one account and sign into another in order to access resources that are in different AWS accounts.

 

![image](https://media.tutorialsdojo.com/sap_assumeRole.png)

 

Therefore, the correct answer is:**First, create IAM users in the master account. Then in the Dev and Test accounts, generate cross-account roles that have full admin permissions while granting access for the master account.** The cross-account role is created in Dev and Test accounts, and the users are created in the Master account that are given that role.

 

The option that says:**In the master account, you are to create IAM users and a cross-account role that has full admin permissions to the Dev and Test accounts**  is incorrect. A cross-account role should be created in Dev and Test accounts, not Master account.

 

The option that says:**IAM users with full admin permissions will be created in the master account. In both Dev and Test accounts, generate cross-account roles that would grant the master account access to Dev and Test account resources through permissions inherited from the master account**  is incorrect. The permissions cannot be inherited from one AWS account to another.

 

The option that says: **By linking all accounts under Consolidated Billing, you will be able to provide IAM users in the master account access to Dev and Test account resources**  is incorrect. Consolidated billing does not give access to resources in this fashion.

 

 

**References** :

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html)

 

 

**Check out this AWS IAM Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 6 — ✅ ĐÚNG

### Câu hỏi

A company wants to improve data protection for the sensitive information stored on its AWS account – both in transit and at rest. Data protection in transit simply means that the data should be secured while it travels to and from Amazon S3. Data protection at rest means that the stored data on disk must be secured in S3 data centers. The data can be protected in transit by using SSL or by using client-side encryption. To secure data at rest, there are a variety of available Server-Side Encryption that can be used in S3. The company currently uses Mountpoint for Amazon S3 to provide high-performance file access to its S3 buckets, and its now evaluating server‑side encryption options to protect its data at rest.



Which of the following best describes how the S3-Managed Keys (SSE-S3) encryption method works?

### Các phương án

- **A.** SSE-S3 provides strong multi-factor encryption in which each object is encrypted with a unique key. It also encrypts the key itself with a master key that it rotates regularly.
- **B.** In SSE-S3, a randomly generated data encryption key is returned which is used by the client to encrypt the object data.
- **C.** In SSE-S3, you will be able to manage the AWS KMS keys and S3 manages the encryption for reading and writing objects in your S3 bucket.
- **D.** SSE-S3 provides separate permissions to use an API key that provides added protection against unauthorized access of your objects in S3.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

With **Amazon S3**  default encryption, you can set the default encryption behavior for an S3 bucket so that all new objects are encrypted when they are stored in the bucket. The objects are encrypted using server-side encryption with either Amazon S3-managed keys (SSE-S3) or AWS KMS keys stored in AWS Key Management Service (SSE-KMS).

 

When you configure your bucket to use default encryption with SSE-KMS, you can also enable S3 Bucket Keys to decrease request traffic from Amazon S3 to AWS Key Management Service (AWS KMS) and reduce the cost of encryption. When you use server-side encryption, Amazon S3 encrypts an object before saving it to disk and decrypts it when you download the object.

 

**Server-side encryption**  with Amazon S3-managed encryption keys (SSE-S3) uses strong multi-factor encryption. Amazon S3 encrypts each object with a unique key. As an additional safeguard, it encrypts the key itself with a master key that it rotates regularly. Amazon S3 server-side encryption uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.

 

![image](https://media.tutorialsdojo.com/sap_s3_sse_encryption.png)

 

Therefore, the correct answer is: **SSE-S3 provides strong multi-factor encryption in which each object is encrypted with a unique key. It also encrypts the key itself with a master key that it rotates regularly.**

 

The option that says: **SSE-S3 provides separate permissions to use an API key that provides added protection against unauthorized access of your objects in S3**  is incorrect. SSE-S3 does not simply use API keys but rather encryption keys.

 

The option that says: **In SSE-S3, you will be able to manage the AWS KMS keys and S3 manages the encryption for reading and writing objects in your S3 bucket** is incorrect. KMS keys are being used in SSE-KMS and not in SSE-S3.

 

The option that says:**In SSE-S3, a randomly generated data encryption key is returned which is used by the client to encrypt the object data**  is incorrect. SSE-S3 does not just use a randomly generated data encryption key.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html)

 

 

**Check out this Amazon S3 Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

---

## Câu 7 — ✅ ĐÚNG

### Câu hỏi

A startup is running a data processing application on AWS. The application is hosted on 25 Amazon EC2 On-Demand Instances, distributed across three Availability Zones, and registered with a target group for a Network Load Balancer (NLB).



Reports indicate a sharp decline in performance during high-demand periods, with CPU utilization spiking to 90%-100%. During normal operations, utilization averages only 20%. The application is stateless and needs to ensure consistent response times even during peak traffic. The company is also considering scheduled scaling to handle anticipated traffic increases during planned events.



The company wants to improve application performance while optimizing costs over the next three years.



Which solution is the most cost-effective for addressing this issue?

### Các phương án

- **A.** Replace the On-Demand Instances with a Spot Fleet request type of `request`. Configure the `InstanceInterruptionBehavior` to `stop` and `TotalTargetCapacity` parameter to 30. Attach the Spot Fleet to the NLB.
- **B.** Configure an Auto Scaling group and attach it to the NLB. Set the minimum capacity to 5 instances and the maximum capacity to 30. Purchase Reserved Instances for 5 instances.
- **C.** Configure an ASG (Auto Scaling Group) and attach it to the Network Load Balancer. Set the capacity to a minimum of 15 instances and a maximum of 25. Purchase Reserved Instances for 15 instances.
- **D.** Replace the On-Demand Instances with a Spot Fleet request type of `request` and with EBS-optimized enabled. Set the `TotalTargetCapacity` parameter to 25 and `DefaultTargetCapacityType` parameter to Spot. Attach the Spot Fleet to the NLB.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

An**Auto Scaling Group**  is a feature of Amazon EC2 that automatically manages a collection of EC2 instances, adjusting the number of running instances based on defined conditions. It helps maintain application availability and allows you to automatically increase the number of instances during demand spikes to preserve performance, and decrease capacity during lulls to reduce costs.

 

A **Network Load Balancer (NLB)**  is a high-performance load-balancing service that operates at the transport layer (Layer 4) of the OSI model and is designed to handle millions of requests per second while maintaining ultra-low latencies. It’s capable of processing TCP, UDP, and TLS traffic, and is ideal for applications requiring extreme performance, such as gaming, IoT, and streaming services, while also providing static IP addresses for each Availability Zone.

 

![image](https://media.tutorialsdojo.com/public/td-ASG-min-max-capacity-setup-in-console-12-20-24.png)

 

The combination of Auto Scaling Groups and Network Load Balancer provides a robust and flexible infrastructure that can adapt to varying workloads while maintaining cost-efficiency. The Auto Scaling Group ensures that the application always has enough resources to handle incoming traffic, scaling up during high-demand periods and down during quieter times. This dynamic scaling addresses the reported performance issues during peak times when CPU utilization spikes to 90-100%.

 

The Network Load Balancer, meanwhile, efficiently distributes the incoming traffic across the available instances, ensuring that no single instance becomes overwhelmed. This is particularly important for maintaining consistent response times, which is a key requirement for the application.

 

The minimum capacity of 5 instances aligns well with the average 20% CPU utilization during normal operations. This baseline ensures that the application can handle typical loads without over-provisioning resources. The maximum capacity of 30 instances allows for significant scaling during high-demand periods, exceeding the current setup of 25 instances and providing room for future growth.

 

Purchasing Reserved Instances for a minimum of five instances is a strategic cost-saving measure. Reserved Instances offer substantial discounts compared to On-Demand pricing, especially over three years. This approach locks in lower prices for the baseline capacity while still allowing for flexible scaling with On-Demand instances when needed.

 

Hence, the correct answer is: **Configure an Auto Scaling group and attach it to the NLB. Set the minimum capacity to 5 instances and the maximum capacity to 30. Purchase Reserved Instances for 5 instances.**

 

The option that says: **Replace the On-Demand Instances with a Spot Fleet request type of `request` and with EBS-optimized enabled. Set the `TotalTargetCapacity` parameter to 25 and `DefaultTargetCapacityType` parameter to Spot. Attach the Spot Fleet to the NLB**  is incorrect. While Spot Instances can offer cost savings, they are unsuitable for applications requiring consistent performance. Spot Instances are primarily used for flexible workloads that can tolerate interruptions. They are ideal for batch processing jobs, big data analytics, and high-performance computing tasks that don’t require continuous availability.

 

The option that says: **Replace the On-Demand Instances with a Spot Fleet request type of `request`. Configure the `InstanceInterruptionBehavior` to `stop` and `TotalTargetCapacity` parameter to 30. Attach the Spot Fleet to the NLB** is incorrect because, similar to the previous option, this solution relies entirely on Spot Instances, which are not suitable for applications requiring consistent performance. Additionally, the `stop` behavior doesn’t prevent interruptions, and it only changes how instances are handled when interrupted.

 

The option that says: **Configure an ASG (Auto Scaling Group) and attach it to the Network Load Balancer. Set the capacity to a minimum of 15 instances and a maximum of 25. Purchase Reserved Instances for 15 instances** is incorrect. While this option uses Auto Scaling and Reserved Instances, which are good practices, it doesn’t allow scaling beyond the current maximum of 25 instances, which may not address the performance issues during peak demand.

 

 

**References:**

 

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

 

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html)

 

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)

 

 

**Check out these AWS Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

 

[https://tutorialsdojo.com/aws-auto-scaling/](https://tutorialsdojo.com/aws-auto-scaling/)

---

## Câu 8 — ✅ ĐÚNG

### Câu hỏi

A global enterprise web application is using a private S3 bucket, named MANILATECH-CONFIG, which has Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3) to store its configuration files for different regions in North America, Latin America, Europe, and Asia. There has been a lot of database changes and feature toggle switching for the past few weeks. Your CTO assigned you the task of enabling versioning on this bucket to track any changes made to the configuration files and have the ability to use the old settings if needed. In the coming days ahead, a new region in Oceania will be supported by the web application and thus, a new configuration file will be added soon. Currently, there are already four files in the bucket, namely: MNL-NA.config, MNL-LA.config, MNL-EUR.config, and MNL-ASIA.config which are updated regularly. As instructed, you enabled the versioning in the bucket and after a few days, the new MNL-O.config configuration file for the Oceania region has been uploaded. A week after, a configuration has been done on MNL-NA.config, MNL-LA.config, and MNL-O.config files.



In this scenario, which of the following is correct about files inside the MANILATECH-CONFIG S3 bucket? (Select TWO.)

### Các phương án

- **A.** The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of null.
- **B.** The first Version ID of MNL-NA.config and MNL-LA.config has a value of 1.
- **C.** The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of 1.
- **D.** The latest Version ID of MNL-NA.config and MNL-LA.config has a value of null.
- **E.** There would be two available versions for each of the MNL-NA.config, MNL-LA.config, and MNL-O.config files. The first Version ID of MNL-NA.config and MNL-LA.config has a value of null.

> **Bạn chọn:** A, E
> **Đáp án đúng:** A, E

### Giải thích

Correct 

**Versioning**  is a means of keeping multiple variants of an object in the same bucket. You can use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket. With versioning, you can easily recover from both unintended user actions and application failures.

 

In this scenario, we have an initial 4 files in the MANILATECH-CONFIG bucket: MNL-NA.config, MNL-LA.config, MNL-EUR.config, and MNL-ASIA.config. Then, the Versioning feature was enabled which caused all of the 4 existing files to have a Version ID of null. This new configuration will enable the new files that will be added to have an alphanumeric VERSION ID, as well as any new updates for the first 4 files. Hence, when a new MNL-O.config configuration file was added, its Version ID was an alphanumeric key since this file was uploaded after the Versioning feature was enabled.

 

A week after, a new update has been done on the 3 configuration files only (MNL-NA.config, MNL-LA.config, and MNL-O.config files). Take note that at this point, there are NO changes made on the MNL-EUR.config and MNL-ASIA.config files, which is why their first (and latest) version ID will still remain as *null*  since there were no new updates made yet.

 

However, for MNL-NA.config and MNL-LA.config, it has the first Version ID of null and then the second Version ID would be an alphanumeric key. For the MNL-O.config file, the first Version ID is already an alphanumeric key since this file was created after the Versioning was enabled.

 

Therefore, the correct answers are:

 

**– There would be two available versions for each of the MNL-NA.config, MNL-LA.config, and MNL-O.config files. The first Version ID of MNL-NA.config and MNL-LA.config has a value of null.**

 

**– The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of null**

 

![image](https://media.tutorialsdojo.com/sap_s3_versioning.png)

 

The option that says: **The first Version ID of MNL-NA.config and MNL-LA.config has a value of 1**  is incorrect. The first VERSION ID of these files would be null since they were already existing when the S3 Versioning was enabled.

 

The option that says: **The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of 1**  is incorrect because the Version ID for these files is null.

 

The option that says: **The latest Version ID of MNL-NA.config and MNL-LA.config has a value of null**  is incorrect because the latest VERSION ID value for these 2 files would be an alphanumeric value and not null.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectVersioning.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectVersioning.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html)

 

 

**Check out this Amazon S3 Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

---

## Câu 9 — ✅ ĐÚNG

### Câu hỏi

An online gambling site is hosted in two Elastic Compute Cloud (EC2) instances inside a Virtual Private Cloud (VPC) in the same Availability Zone (AZ) but in different subnets. The first EC2 instance is running a database and the other EC2 instance is a web application that fetches data from the database. You are required to ensure that the two EC2 instances can connect with each other in order for your application to work properly. You also need to track historical changes to the security configurations associated to your instances.



Which of the following options below can meet this requirement? (Select TWO.)

### Các phương án

- **A.** Use Route 53 to ensure that there is proper routing between the two subnets.
- **B.** Ensure that the default route is set to a NAT instance or Internet Gateway (IGW).
- **C.** Use AWS Config to track historical changes to the security configurations associated to your instances.
- **D.** Use AWS Systems Manager to track historical changes to the security configurations associated to your instances.
- **E.** Check and configure the network ACL to allow communication between the two subnets. Ensure that the security groups allow the application host to talk to the database on the right port and protocol.

> **Bạn chọn:** C, E
> **Đáp án đúng:** C, E

### Giải thích

Correct 

AWS provides two features that you can use to increase security in your VPC: security groups and network ACLs. **Security groups**  control inbound and outbound traffic for your instances, and **network ACLs**  control inbound and outbound traffic for your subnets. In most cases, security groups can meet your needs; however, you can also use network ACLs if you want an additional layer of security for your VPC.

 

![image](https://media.tutorialsdojo.com/sap_config_how_it_works.png)

 

**AWS Config**  is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting.

 

The option that says: **Check and configure the network ACL to allow communication between the two subnets. Ensure that the security groups allow the application host to talk to the database on the right port and protocol**  is correct. NACLs and security groups act like firewalls for communication within your instances and subnets.

 

The option that says: **Use AWS Config to track historical changes to the security configurations associated to your instances**  is correct. AWS Config can help you maintain compliance with your security setting by monitoring and detecting violations on your security groups depending on the rules you have specified.

 

The option that says: **Use Route 53 to ensure that there is proper routing between the two subnets** is incorrect. Route 53 can’t be used to connect two subnets. You should use Network ACLs and Security Groups instead.

 

The option that says: **Ensure that the default route is set to NAT instance or Internet Gateway (IGW)**  is incorrect. Neither a NAT instance nor an Internet gateway is needed for the two EC2 instances to communicate.

 

The option that says: **Use AWS Systems Manager to track historical changes to the security configurations associated to your instances**  is incorrect. Using AWS Systems Manager is not suitable to track historical changes to the security configurations associated to your instances. You have to use AWS Config instead.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html)

 

[https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html)

 

 

**Check out these Amazon VPC and AWS Config Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

 

[https://tutorialsdojo.com/aws-config/](https://tutorialsdojo.com/aws-config/)

 

 

**Learn more about AWS Config in this 19-minute video:**

---

## Câu 10 — ✅ ĐÚNG

### Câu hỏi

A company implements best practices and mandates that all of the cloud-related deployments should not be done manually but through the use of CloudFormation. All of the CloudFormation templates should be treated as code and hence, all of them are committed in a private GIT repository. A senior solutions architect has recently left the team. One of the tasks of the junior solutions architect is to handle a distributed system in AWS, in which the architecture is declared in a CloudFormation template. The distributed system needs to be migrated to another VPC and the junior solutions architect tried to read the template to understand the AWS resources that the template will generate. While analyzing the CloudFormation template, he stumbled upon the code below.



What does this code snippet do in CloudFormation?



`
 "SNSTopic" : {
 "Type" : "AWS::SNS::Topic",
 "Properties" : {
 "Subscription" : [{
 "Protocol" : "sqs",
 "Endpoint" : { "Fn::GetAtt" : [ "TutorialsDojoQueue", "Arn" ] }
 }]
 }
 `

### Các phương án

- **A.** Creates an SNS topic which allows SQS subscription endpoints.
- **B.** Creates an SNS topic and then adds a subscription using the ARN attribute name for the SQS resource, which is created under the logical name TutorialsDojoQueue.
- **C.** Creates an SNS topic which allows SQS subscription endpoints to be added as a parameter on the template.
- **D.** Creates an SNS topic and then invokes the call to create an SQS queue with a logical resource name of TutorialsDojoQueue.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**AWS CloudFormation**  provides several built-in functions that help you manage your stacks which are called “intrinsic functions”. Use intrinsic functions in your templates to assign values to properties that are not available until runtime.

 

You can use intrinsic functions only in specific parts of a template. Currently, you can use intrinsic functions in resource properties, outputs, metadata attributes, and update policy attributes. You can also use intrinsic functions to conditionally create stack resources.

 

The **`Fn::GetAtt`**  intrinsic function returns the value of an attribute from a resource in the template. It has 2 parameters: the **`logicalNameOfResource`** and the **`attributeName`** . The logical name (also called logical ID) of the resource contains the attribute that you want to use. The **`attributeName`** is the name of the resource-specific attribute whose value you want to utilize.

 

![image](https://media.tutorialsdojo.com/sap_cloudformation_steps.png)

 

Therefore, the correct answer is: **Create an SNS topic and then add a subscription using the ARN attribute name for the SQS resource, which is created under the logical name TutorialsDojoQueue.**  The code snippet creates an SNS topic and then adds a subscription using the ARN attribute name for the SQS resource, which is created under the logical name “TutorialsDojoQueue” using the GetAtt intrinsic function.

 

The following options are all incorrect because these options incorrectly described what the code snippet does:

 

**– Creates an SNS topic which allows SQS subscription endpoints to be added as a parameter on the template.**

 

**– Creates an SNS topic which allows SQS subscription endpoints.**

 

**– Creates an SNS topic and then invokes the call to create an SQS queue with a logical resource name of TutorialsDojoQueue.**

 

 

**References:**

 

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html)

 

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html)

 

 

**Check out this AWS CloudFormation Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

---

## Câu 11 — ✅ ĐÚNG

### Câu hỏi

A company located on the west coast of North America plans to release a new online service for its customers. The company already created a new VPC in the us-west-1 region where they will launch the Amazon EC2 instances that will host the web application. The application must be highly-available and must dynamically scale based on user traffic. In addition, the company wants to have a disaster recovery site in the us-east-1 region that will act as a passive backup of the running application.



Which of the following options should the Solutions Architect implement in order to achieve the requirements?

### Các phương án

- **A.** Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) that spans multiple Availability Zones (AZs) on both VPCs. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB. Create an Alias record entry in Amazon Route 53 that points to the DNS name of the ALB.
- **B.** Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB.
- **C.** Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create separate record entries for each region’s ALB on Amazon Route 53 and enable health checks to ensure high-availability for both regions.
- **D.** Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create record entries in Amazon Route 53 pointing to the ALBs with health check enabled and a failover routing policy.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

On **Amazon Route 53** , after you create a hosted zone for your domain, such as tutorialsdojo.com, you create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain. You can create a record that points to the DNS name of your Application Load Balancer on AWS.

 

When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:

 

- **Simple routing policy**  – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.
- **Failover routing policy**  – Use when you want to configure active-passive failover.
- **Geolocation routing policy**  – Use when you want to route traffic based on the location of your users.
- **Geoproximity routing policy**  – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
- **Latency routing policy**  – Use when you have resources in multiple AWS Regions, and you want to route traffic to the region that provides the best latency.
- **Multivalue answer routing policy**  – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
- **Weighted routing policy**  – Use to route traffic to multiple resources in proportions that you specify.

 

You can use **Route 53 health checks**  to configure active-active and active-passive failover configurations. You configure active-active failover using any routing policy (or combination of routing policies) other than failover, and you configure active-passive failover using the failover routing policy.

 

![image](https://media.tutorialsdojo.com/route53-failover.png )

 

Use an **active-passive failover configuration**  when you want a primary resource or group of resources to be available the majority of the time, and you want a secondary resource or group of resources to be on standby in case all the primary resources become unavailable. When responding to queries, Route 53 includes only the “healthy primary” resources. If all the primary resources are unhealthy, Route 53 begins to include only the healthy secondary resources in response to DNS queries.

 

This way, you can create a failover routing policy that will direct traffic to the backup region when your primary region fails.

 

Amazon EC2 Auto Scaling integrates with Elastic Load Balancing to enable you to insert one or more Application Load Balancer, Network Load Balancer, or Gateway Load Balancer with multiple target groups in front of your Auto Scaling group.

 

Creating an Application Load Balancer on each region with an Auto Scaling group that spans multiple Availability Zones ensures that your application will be highly available and will scale based on the user traffic.

 

Therefore, the correct answer is: **Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create record entries in Amazon Route 53 pointing to the ALBs with health check enabled and a failover routing policy.**

 

The option that says: **Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB**  is incorrect because an Auto Scaling group cannot span AZs on multiple regions, and the Application Load Balancer cannot serve traffic to EC2 instances on a different region even with Inter-Region VPC peering.

 

The option that says: **Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) that spans multiple Availability Zones (AZs) on both VPCs. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB. Create an Alias record entry in Amazon Route 53 that points to the DNS name of the ALB**  is incorrect because an Application Load Balancer cannot span to multiple regions, only multiple AZs on the same region. An Auto Scaling group also cannot span multiple regions as it can only deploy EC2 instances in one region.

 

The option that says: **Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create separate record entries for each region’s ALB on Amazon Route 53 and enable health checks to ensure high-availability for both regions**  is incorrect. Although this setup is possible, it does not mention the routing policy to be used on Amazon Route 53. The question requires that the second region acts as a passive backup, which means only the main region receives all the traffic so you need to specifically use a failover routing policy in Amazon Route 53.

 

 

**References:**

 

[https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)

 

[https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html)

 

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html)

 

 

**Check out the Amazon Route 53 Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-route-53/](https://tutorialsdojo.com/amazon-route-53/)

---

## Câu 12 — ✅ ĐÚNG

### Câu hỏi

A technology company runs an industrial chain orchestration software on the AWS cloud. It consists of a web application tier that is currently deployed on a fixed fleet of Amazon EC2 instances. The database tier is deployed on Amazon RDS. The web and database tiers are deployed in the public and private subnet of the VPC respectively. The company wants to improve the service to make it more cost-effective, scalable, highly available and should require minimal human intervention.



Which of the following actions should the solutions architect implement to improve the availability and load balancing of this cloud architecture? (Select TWO.)

### Các phương án

- **A.** Launch a load balancer in front of all the web servers then create a Non-Alias Record in Route 53 which maps to the DNS name of the load balancer.
- **B.** Set up a NAT instance in your VPC. Update your route table by creating a default route via the NAT instance with all subnets associated with it. Configure a DNS A Record in Route 53 pointing to the NAT instance's public IP address.
- **C.** Create a Non-Alias Record in Route 53 with a Multivalue Answer Routing configuration and add all the IP addresses for your web servers.
- **D.** Create a CloudFront distribution whose origin points to the private IP addresses of your web servers. Also set up a CNAME record in Route 53 mapped to your CloudFront distribution.
- **E.** Place an Application Load Balancer in front of all the web servers. Create a new Alias Record in Route 53 which maps to the DNS name of the load balancer.

> **Bạn chọn:** C, E
> **Đáp án đúng:** C, E

### Giải thích

Correct 

**Amazon Route 53 *alias records***  provide a Route 53–specific extension to DNS functionality. Alias records let you route traffic to selected AWS resources, such as CloudFront distributions and Amazon S3 buckets. They also let you route traffic from one record in a hosted zone to another record.

 

Unlike a CNAME record, you can create an alias record at the top node of a DNS namespace, also known as the *zone apex* . For example, if you register the DNS name `tutorialsdojo.com`, the zone apex is `tutorialsdojo.com`. You can’t create a CNAME record for `tutorialsdojo.com`, but you can create an alias record for `tutorialsdojo.com` that routes traffic to `**www** .tutorialsdojo.com `(take note of the **www**  subdomain).

 

You can also type the domain name for the resource. For example:

 

– CloudFront distribution domain name: dtut0rial5d0j0.cloudfront.net
 – Elastic Beanstalk environment CNAME: tutorialsdojo.elasticbeanstalk.com
 – ELB load balancer DNS name:tutorialsdojo-1.us-east-2.elb.amazonaws.com
 – S3 website endpoint: s3-website.us-east-2.amazonaws.com
 – Resource record set in this hosted zone: www.tutorialsdojo.com
 – VPC endpoint: tutorialsdojo.us-east-2.vpce.amazonaws.com
 – API Gateway custom regional API: d-tut5d0j0c0m.execute-api.us-west-2.amazonaws.com

 

![image](https://media.tutorialsdojo.com/sap_route53_alias.png)

 

Multivalue answer routing lets you configure Amazon Route 53 to return multiple values, such as IP addresses for your web servers, in response to DNS queries. You can specify multiple values for almost any record, but multivalue answer routing also lets you check the health of each resource, so Route 53 returns only value for healthy resources. It’s not a substitute for a load balancer, but the ability to return multiple health-checkable IP addresses is a way to use DNS to improve availability and load balancing.

 

The option that says:**Place an Application Load Balancer in front of all the web servers. Create a new Alias Record in Route 53 which maps to the DNS name of the load balancer** is correct because if the web servers are behind an ELB, the load on the web servers will be uniformly distributed which means that if any of the web servers go offline, the web traffic would be routed to other web servers. In this way, there would be no unnecessary downtime. You can also use Route 53 to set the ALIAS record that points to the ELB endpoint.

 

The option that says: **Create a Non-Alias Record in Route 53 with a Multivalue Answer Routing configuration and add all the IP addresses for your web servers**  is correct. Although a Multivalue answer routing is not a substitute for a load balancer, its ability to return multiple health-checkable IP addresses can still improve the availability and load balancing of your system.

 

The option that says: **Create a CloudFront distribution whose origin points to the private IP addresses of your web servers. Also set up a CNAME record in Route 53 mapped to your CloudFront distribution**  is incorrect as it is using Amazon CloudFront, which is directly pointing to the web server as its origin. You should use a Public IP address, not a Private IP address when using an EC2 origin. In addition, if the EC2 instances go down, the entire website would also become unavailable in this scenario.

 

The option that says: **Set**  **up a NAT instance in your VPC. Update your route table by creating a default route via the NAT instance with all subnets associated with it. Configure a DNS A Record in Route 53 pointing to the NAT instance’s public IP address**  is incorrect as a NAT instance is mainly used to allow an EC2 instance launched on a private subnet to access the Internet via a public subnet. In addition, the issue is mainly on the web servers which are hosted on the public subnet and not on the private subnet.

 

The option that says: **Launch a load balancer in front of all the web servers then create a Non-Alias Record in Route 53 which maps to the DNS name of the load balancer**  is incorrect. Although it is recommended to use a load balancer in front of your EC2 instances, you need to use an *Alias*  Record in Route 53 and not a Non-Alias Record.

 

 

**References** :

 

[https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-alias.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-alias.html)

 

[https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

 

 

**Check out this Amazon Route 53 Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-route-53/](https://tutorialsdojo.com/amazon-route-53/)

---

## Câu 13 — ✅ ĐÚNG

### Câu hỏi

A company wants to create a new service that will complement the launch of its new product. The site must be highly available and scalable to handle the unpredictable workload, and should also be stateless and REST compliant. The solution needs to have multiple persistent storage layers for service object metadata and durable storage for static content. All requests to the service should be authenticated and securely processed. The company also wants to keep the costs at a minimum. The team considered using an AWS Lambda authorizer for custom authentication logic but wants to minimize operational overhead.



Which of the following is the recommended solution that will meet the company requirements?

### Các phương án

- **A.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **B.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service.
- **C.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **D.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

**Amazon API Gateway Lambda proxy**  **integration**  is a simple, powerful, and nimble mechanism to build an API with a setup of a single API method. The Lambda proxy integration allows the client to call a single Lambda function in the backend. The function accesses many resources or features of other AWS services, including calling other Lambda functions.

 

In Lambda proxy integration, when a client submits an API request, API Gateway passes to the integrated Lambda function the raw request as-is, except that the order of the request parameters is not preserved. This request data includes the request headers, query string parameters, URL path variables, payload, and API configuration data. The configuration data can include current deployment stage name, stage variables, user identity, or authorization context (if any).

 

A user pool is a user directory in **Amazon Cognito** . With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers. Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).

 

![image](https://media.tutorialsdojo.com/sap_cognito_user_pool.png)

 

User pools provide:

 

– Sign-up and sign-in services.

 

– A built-in, customizable web UI to sign in users.

 

– Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple, as well as sign-in with SAML identity providers from your user pool.

 

– User directory management and user profiles.

 

– Security features such as multi-factor authentication (MFA), checks for compromised credentials, account takeover protection, and phone and email verification.

 

– Customized workflows and user migration through AWS Lambda triggers.

 

**Amazon S3**  is a simple key-based object store whose scalability and low cost make it ideal for storing large datasets or objects. When finding objects based on attributes or other metadata, a common solution is to build an external index such as a DynamoDB Table that maps queryable attributes to the S3 object key. DynamoDB is a NoSQL data store that can be used for storing the index itself.

 

One way of securing objects that are shared on S3 buckets is by using presigned URLs. When you create a presigned URL for your object, you must provide your security credentials, specify a bucket name, an object key, specify the HTTP method (GET to download the object), and expiration date and time. The presigned URLs are valid only for the specified duration.

 

Anyone who receives the presigned URL can then access the object. For example, if you have a video in your bucket and both the bucket and the object are private, you can share the video with others by generating a presigned URL.

 

Hence, the correct answer is:**Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.**

 

The option that says: **Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service** is incorrect. Although running Docker-based containers on Amazon Fargate is possible, this solution does not just offer the lowest possible cost to satisfy the given scenario. AWS Lambda is suited for creating serverless/stateless APIs and costs cheaper than AWS Fargate.

 

The option that says: **Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket** is incorrect. Running a Fargate cluster continuously is more expensive than running Lambda functions which only runs on-demand.

 

The option that says: **Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket**  is incorrect because it is recommended to use Amazon Cognito user pools for user access controls compared to an API Gateway custom authorizer. It is more robust and offers more features because it is designed to handle user access.

 

 

**References:**

 

[https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)

 

[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)

 

[https://aws.amazon.com/blogs/big-data/building-and-maintaining-an-amazon-s3-metadata-index-without-servers/](https://aws.amazon.com/blogs/big-data/building-and-maintaining-an-amazon-s3-metadata-index-without-servers/)

 

 

**Check out these AWS Comparison Cheat Sheets:**

 

[https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai/](https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai/)

 

[https://tutorialsdojo.com/ec2-container-service-ecs-vs-lambda/](https://tutorialsdojo.com/ec2-container-service-ecs-vs-lambda/)

---

## Câu 14 — ✅ ĐÚNG

### Câu hỏi

An international humanitarian aid organization has a requirement to store 20 TB worth of scanned files for the relief operations, which can grow to a total of 50 TB of data. There is also a requirement to have a website with a search feature in place that can be used to easily find a certain item through the thousands of scanned files. The new system is expected to run for more than three years.



Which of the following is the most cost-effective option for implementing the search feature in the system?

### Các phương án

- **A.** Design the new system using a CloudFormation template. Use an EC2 instance running an NGINX web server and an open-source search application. Launch multiple standard EBS volumes with RAID configuration to store the scanned files with a search index.
- **B.** Use Amazon EFS to store and serve the scanned files. Install a 3rd-party search software on an Auto Scaling group of On-Demand EC2 Instances and an Elastic Load Balancer.
- **C.** Use S3 for both storing and searching the scanned files by utilizing the native search capabilities of S3.
- **D.** Set up a new S3 bucket with standard storage to store and serve the scanned files. Use Amazon OpenSearch Service for query processing and use Elastic Beanstalk to host the website across multiple availability zones.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**Amazon Simple Storage Service (S3)**  is an excellent object-based storage that is highly durable and scalable. However, its native search capability is not effective. Hence, you need to have a separate service to handle the search feature.

 

**Amazon OpenSearch Service**  simplifies the deployment, operation, and scaling of OpenSearch, a widely-used open-source search and analytics engine. It provides robust security features, ensures high availability and data durability, and offers direct access to the OpenSearch API.

 

![image](https://media.tutorialsdojo.com/public/s3-opensearch-093024.png)

 

Amazon S3 offers scalable and cost-effective storage, making it ideal for handling large datasets. It ensures durability and easy access to the scanned files.

 

Amazon OpenSearch Service is optimized for efficient search and analytics, making it perfect for querying extensive datasets.

 

Elastic Beanstalk simplifies the deployment and management of the website, significantly reducing operational overhead.

 

By hosting the website across multiple availability zones, the system ensures high reliability and availability, which is crucial for humanitarian operations.

 

Hence, the correct answer is: **Set up a new S3 bucket with standard storage to store and serve the scanned files. Use Amazon OpenSearch Service for query processing and use Elastic Beanstalk to host the website across multiple availability zones.**

 

The option that says: **Use Amazon EFS to store and serve the scanned files. Install a 3rd-party search software on an Auto Scaling group of On-Demand EC2 Instances and an Elastic Load Balancer**  is incorrect. It is stated in the scenario that the new system is expected to run for more than 3 years which means that using Reserved EC2 instances would typically be a more cost-effective choice than using On-Demand instances. In addition, purchasing and installing a 3rd-party search software might be more expensive than just using Amazon OpenSearch Service.

 

The option that says: **Design the new system using a CloudFormation template. Use an EC2 instance running an NGINX web server and an open-source search application. Launch multiple standard EBS volumes with RAID configuration to store the scanned files with a search index** is incorrect because a system composed of RAID configuration of EBS volumes is not a durable and scalable solution compared to S3.

 

The option that says: **Use S3 for both storing and searching the scanned files by utilizing the native search capabilities of S3**  is incorrect as the native search capability of S3 is not effective. It is better to use Amazon OpenSearch Service or another service primarily providing search functionality.

 

 

**References:**

 

[https://aws.amazon.com/s3/](https://aws.amazon.com/s3/)

 

[https://docs.aws.amazon.com/opensearch-service/](https://docs.aws.amazon.com/opensearch-service/)

 

[https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hawordpress-tutorial.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hawordpress-tutorial.html)

 

 

**Check out this Amazon OpenSearch Service Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-opensearch-service/](https://tutorialsdojo.com/amazon-opensearch-service/)

---

## Câu 15 — ❌ SAI

### Câu hỏi

A global real estate startup is looking for an option to add a cost-effective location-based alert to iOS and Android mobile apps. Users will receive push notifications on mobile devices regarding real estate offers in proximity to current locations, with delivery expected in under a minute. The existing mobile app has an initial 2 million users worldwide and is rapidly growing. The team considered using AWS Wavelength for edge processing of location data but chose a simpler queuing approach to reduce costs.



What is the most suitable architecture to use in this scenario?

### Các phương án

- **A.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app.
- **B.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use Amazon SNS Mobile Push to send out the offers to the mobile app.
- **C.** Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app.
- **D.** Set up an architecture where the mobile app sends each user's location to an Amazon SQS queue, and AWS Lambda functions process the queued messages and retrieve nearby offers from an Amazon Aurora Serverless database. After processing, publish the offers to Amazon SNS topics configured with SMS delivery for registered mobile numbers.

> **Bạn chọn:** D
> **Đáp án đúng:** B

### Giải thích

Incorrect  

With **Amazon SNS Mobile Push Notifications** , you have the ability to send push notification messages directly to apps on mobile devices. Push notification messages sent to a mobile endpoint can appear in the mobile app as message alerts, badge updates, or even sound alerts.

 

![image](https://media.tutorialsdojo.com/public/Amazon SNS Mobile push notifications-24SEP2026.png)

 

Hence, the correct answer is: **Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use Amazon SNS Mobile Push to send out the offers to the mobile app.**  SQS is a highly scalable, cost-effective solution for carrying out utility tasks such as holding the location of millions of users. In addition, it uses a highly scalable DynamoDB table and a cost-effective AWS SNS Mobile Push service to send push notification messages directly to the mobile apps.

 

The option that says: **Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app**  is incorrect. Although a combination of On-Demand EC2 instances and API Gateway can typically provide a scalable computing system, it is wrong to use AWS AppSync for push notifications to mobile devices. You should use Amazon SNS Mobile Push service instead.

 

The option that says: **Set up an architecture where the mobile app sends each user’s location to an Amazon SQS queue, and AWS Lambda functions process the queued messages and retrieve nearby offers from an Amazon Aurora Serverless database. After processing, publish the offers to Amazon SNS topics configured with SMS delivery for registered mobile numbers**  is incorrect because SNS SMS delivery is not the right mechanism for mobile app push notifications. Amazon SNS SMS delivers text messages to phone numbers instead of push notifications to the mobile application. Although Amazon SQS and AWS Lambda provide a scalable and cost-effective processing architecture, the SMS delivery method does not satisfy the requirement to send native push notifications to the iOS and Android apps.

 

The option that says: **Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app**  is incorrect because AWS Device Farm is an app testing service and is not used to push notifications to various mobile devices. It only lets you test and interact with your Android, iOS, and web apps on many devices at once, or reproduce issues on a device in real time.

 

**References:**

 

[https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html)

 

[https://docs.aws.amazon.com/sns/latest/dg/mobile-push-pseudo.html](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-pseudo.html)

 

[https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html)

 

 

**Check out this Amazon SNS Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-sns/](https://tutorialsdojo.com/amazon-sns/)

---

## Câu 16 — ✅ ĐÚNG

### Câu hỏi

An insurance company collects contributions from its clients and invests in the stock market. Using the on-premises data center, the company ingests raw data feeds from the stock market, transforms it, and sends it to the internal Apache Kafka cluster for processing. The management wants to send the cluster’s output to Amazon Web Services by building a scalable and near-real-time solution that will provide the stock market data to its web application. The application is a critical production component, so the solution needs to have a consistent high-performance network.



Which of the following actions should the solutions architect implement to fulfill the requirements? (Select THREE.)

### Các phương án

- **A.** Fetch the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Consumer Library. Use Kinesis Data Analytics to process and transform the streaming data before delivering it to downstream consumers.
- **B.** To have a consistent performance while being cost-effective, configure a Site-to-Site VPN from the on-premises data center to the AWS VPC.
- **C.** Pull the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Producer Library.
- **D.** To have consistent performance, request for an AWS Direct Connect connection from the on-premises data center to the AWS VPC.
- **E.** Write an AWS Lambda function to process the Amazon Kinesis data stream and write a GraphQL API in AWS AppSync to invoke the function. Send the callback messages to connected clients by using the `@connections` command for the API.
- **F.** Write an AWS Lambda function to process the Amazon Kinesis data stream and create a WebSocket API in Amazon API Gateway to invoke the function. Send the callback messages to connected clients by using the `@connections` command for the API.

> **Bạn chọn:** C, D, F
> **Đáp án đúng:** C, D, F

### Giải thích

Correct 

**AWS Direct Connect**  makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs in the same region. Using private VIF on AWS Direct Connect, you can establish private connectivity between AWS and your data center, office, or colocation environment, as shown in the following figure. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.

 

![image](https://media.tutorialsdojo.com/sap_awsDirectConnect.jpg)

 

A producer puts data records into Amazon Kinesis data streams. For example, a web server sending log data to a Kinesis data stream is a producer. A consumer processes the data records from a stream. To put data into the stream, you must specify the name of the stream, a partition key, and the data blob to be added to the stream. The partition key is used to determine which shard in the stream the data record is added to. All the data in the shard is sent to the same worker that is processing the shard.

 

A **WebSocket API**  in API Gateway is a collection of WebSocket routes that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can use API Gateway features to help you with all aspects of the API lifecycle, from creation through monitoring your production APIs.

 

![image](https://media.tutorialsdojo.com/sap_webSockets.jpg)

 

API Gateway WebSocket APIs are bidirectional. A client can send messages to a specific service, and services can independently send messages to clients. This bidirectional behavior enables richer client/service interactions because services can push data to clients without requiring clients to make an explicit request. WebSocket APIs are often used in real-time applications such as chat applications, collaboration platforms, multiplayer games, and financial trading platforms.

 

You can use the `@connections` API from your backend service to send a callback message to a connected client, get connection information or disconnect from the client.

 

Hence, the correct answers are:

 

**– To have consistent performance, request for an AWS Direct Connect connection from the on-premises data center to the AWS VPC.**

 

**– Pull the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Producer Library.**

 

**– Write an AWS Lambda function to process the Amazon Kinesis data stream and create a WebSocket API in Amazon API Gateway to invoke the function. Send the callback messages to connected clients by using the `@connections` command for the API.**

 

The option that says: **Fetch the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Consumer Library. Use Kinesis Data Analytics to process and transform the streaming data before delivering it to downstream consumers**  is incorrect because you should typically use Amazon Kinesis Producer Library, not Consumer Library.

 

The option that says: **Write an AWS Lambda function to process the Amazon Kinesis data stream and write a GraphQL API in AWS AppSync to invoke the function. Send the callback messages to connected clients by using the `@connections` command for the API**  is incorrect because using `@connections` to have the backend service connect back to the clients is not primarily a feature of the GraphQL API when using AWS AppSync.

 

The option that says: **To have a consistent performance while being cost-effective, configure a Site-to-Site VPN from the on-premises data center to the AWS VPC**  is incorrect because a Site-to-Site VPN does not provide a reliable and high-performance network connection between the on-premises data center and Amazon VPC.

 

 

**References:**

 

[https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html)

 

[https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-producers.html](https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-producers.html)

 

[https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html](https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html)

 

 

**Check out these AWS Direct Connect and Amazon Kinesis Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-direct-connect/](https://tutorialsdojo.com/aws-direct-connect/)

 

[https://tutorialsdojo.com/amazon-kinesis/](https://tutorialsdojo.com/amazon-kinesis/)

---

## Câu 17 — ❌ SAI

### Câu hỏi

A company is using AWS Managed Active Directory Service to host the company AD in the AWS Cloud with a custom AD domain name private.tutorialsdojo.com. A pair of domain controllers are launched with the default configuration inside the VPC. A VPC interface endpoint was also created for the Amazon Kinesis using AWS Private Link to allow instances to connect to Kinesis service endpoints from inside the VPC. The solutions architect launched several EC2 instances in the VPC, however, the instances were not able to resolve the company’s custom AD domain name.



Which of the following steps should the Solutions Architect implement to allow the instances to resolve both AWS VPC endpoints and the AWS Managed Microsoft AD domain’s FQDN? (Select TWO.)

### Các phương án

- **A.** Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.
- **B.** Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.
- **C.** Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries.
- **D.** Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.
- **E.** Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.

> **Bạn chọn:** A, B
> **Đáp án đúng:** A, D

### Giải thích

Incorrect  

When you create a VPC using Amazon VPC, **Route 53 Resolver**  automatically answers DNS queries for local VPC domain names for EC2 instances (ec2-192-0-2-44.compute-1.amazonaws.com) and records in private hosted zones (private.tutorialsdojo.com). For all other domain names, Resolver performs recursive lookups against public name servers.

 

You also can integrate DNS resolution between Resolver and DNS resolvers on your network by configuring forwarding rules. Your network can include any network that is reachable from your VPC, such as the following:

 

- The VPC itself
- Another peered VPC
- An on-premises network that is connected to AWS with AWS Direct Connect, a VPN, or a network address translation (NAT) gateway.

 

A Route 53 Resolver Endpoint is a customer-managed resolver consisting of one or more Elastic Network Interfaces (ENIs) deployed on your VPC. Resolver Endpoints are classified into two types:

 

- **Inbound Endpoint –**  provides DNS resolution of AWS resources, such as EC2 instances, for your corporate network.
- **Outbound Endpoint**  – provides resolution of specific DNS names that you configure using forwarding rules to your VPC.

 

Outbound Resolver Endpoints host Forwarding Rules that forward queries for specified domain names to specific IP addresses. You create forwarding rules when you want to forward DNS queries for specified domain names to DNS resolvers on your network.

 

To forward selected queries, you create Resolver rules that specify the domain names for the DNS queries that you want to forward (such as example.com), and the IP addresses of the DNS resolvers on your network that you want to forward the queries to. If a query matches multiple rules (tutorialsdojo.com, portal.tutorialsdojo.com), the Resolver chooses the rule with the most specific match (portal.tutorialsdojo.com) and forwards the query to the IP addresses that you specified in that rule.

 

![image](https://media.tutorialsdojo.com/sap_outbound_resolver.png)

 

When **Outbound Endpoint**  and **Forwarding Rule**  are created, any resource in the VPC that queries the AmazonProvidedDNS as its DNS resolver is able to seamlessly resolve for AWS Managed Microsoft AD domain’s FQDN, as well as any AWS resources on the VPC such as (interface) VPC Endpoints.

 

The option that says: **Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC**  is correct. You need an outbound endpoint to forward and resolve custom domain names inside your VPC.

 

The option that says: **Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers**  is correct. The forwarding rules will handle queries for a given DNS domain and forward them to the AD server to resolve them.

 

The option that says: **Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC**  is incorrect. An inbound endpoint is used for DNS resolution of AWS services. You need an outbound endpoint for this scenario.

 

The option that says: **Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries**  is incorrect. It is not recommended to manually configure resources to split DNS queries. This entails a lot of management overhead. You just need to set the Active Directory servers as the DNS servers and the requests will be forwarded to the VPC resolver accordingly.

 

The option that says: **Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers**  is incorrect. A conditional forwarder is configured inside the AD servers, not on the Route 53 resolver endpoint.

 

**References:**

 

[https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-configuring](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-configuring)

 

[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html)

 

[https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/)

 

 

**Check out these Amazon VPC and Amazon Route 53 Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

 

[https://tutorialsdojo.com/amazon-route-53/](https://tutorialsdojo.com/amazon-route-53/)

---

## Câu 18 — ✅ ĐÚNG

### Câu hỏi

A manufacturing company is developing a system to monitor and analyze equipment performance using IoT devices. They plan to use AWS IoT Core to collect data from 500 sensors across their production lines.



The collected data must be enriched with additional context before being stored in an Amazon S3 data lake. Sensor data is collected every 10 seconds. The enriched data should be available in the data lake within 20 minutes of collection.



Which approach would best fulfill these requirements in the MOST cost-effective and scalable manner?

### Các phương án

- **A.** Use AWS IoT Core to send data to an Amazon Timestream table for temporary storage. Deploy an AWS Lambda function to query Timestream, enrich the data, and upload it to Amazon S3.
- **B.** Use AWS IoT Core Basic Ingest for data collection. Configure an AWS IoT rule action to send data to Amazon Data Firehose. Set up Data Firehose with an AWS Lambda function for data enrichment and a buffer interval of 300 seconds.
- **C.** Use AWS IoT Core Basic Ingest to forward sensor data to Amazon Kinesis Data Streams. Deploy an Auto Scaling group of EC2 instances to enrich and process the data, and use the S3 `PutObject` API to upload the processed data in Amazon S3.
- **D.** Ingest data over MQTT protocol using AWS IoT Core. Use an IoT rule action to trigger an AWS Step Functions workflow that enriches data using an AWS Lambda function and delivers results to Amazon S3.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**AWS IoT**  is a managed cloud platform that allows connected devices to securely and easily interact with cloud applications and other devices. It provides secure communication, data processing, and device management for Internet of Things (IoT) solutions. AWS IoT Core, which is mentioned in the question, is the central component of AWS IoT that provides the communication infrastructure for connecting IoT devices to the AWS cloud.

 

**Amazon Data Firehose**  is a fully managed service for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and Splunk. It can automatically scale to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

 

**AWS Lambda**  is a serverless compute service that allows you to run code without managing servers. You can create Lambda functions to perform specific tasks, which can be triggered by various AWS services or called directly. Lambda automatically scales based on workload size. In data processing, it can be used to transform, enrich, or analyze data flowing through services like Amazon Data Firehose.

 

![image](https://media.tutorialsdojo.com/public/td-Iot-Devices-DataFiehose-Diagram-12-20-24.png)

 

To efficiently manage data collection from a network of 500 sensors, it is recommended that AWS IoT Core Basic Ingest be used. This method is specifically designed for high-volume data ingestion, allowing devices to publish messages directly to the AWS IoT Rules Engine without maintaining a persistent connection, which helps reduce overhead.

 

Configuring an AWS IoT rule action allows data to be routed to Amazon Data Firehose, a fully managed service that streams real-time data to destinations like Amazon S3. Data Firehose automatically scales to meet throughput demands and requires no ongoing administration while also supporting data transformation through AWS Lambda which could be use to the enrich data before storing to Amazon S3.

 

Setting a buffer interval of 300 seconds (5 minutes) is a good choice for processing data in batches, making it cost-effective for delivery to Amazon S3 within the required 20-minute window. Each buffered batch are processed by a Lambda function and sent back to Firehose. Firehose then sends the data to Amazon S3 once the specified buffering size or buffering interval is reached, whichever comes first.

 

Hence, the correct answer is: **Use AWS IoT Core Basic Ingest for data collection. Configure an AWS IoT rule action to send data to Amazon Data Firehose. Set up Data Firehose with an AWS Lambda function for data enrichment and a buffer interval of 900 seconds.**

 

The option that says: **Ingest data over MQTT protocol using AWS IoT Core. Use an IoT rule action to trigger an AWS Step Functions workflow that enriches data using an AWS Lambda function and delivers results to Amazon S3** is incorrect. While Step Functions and Lambda would work, it introduces more complexity and adds unncessary overhead. Moreover, triggering a Step Functions workflow for every data point that comes in (every 10 seconds) would be expensive and potentially slow. Step Functions are primarily used for complex, long-running workflows rather than high-frequency, simple data processing.

 

The option that says: **Use AWS IoT Core to send data to an Amazon Timestream table for temporary storage. Deploy an AWS Lambda function to query Timestream, enrich the data, and upload it to Amazon S3** is incorrect because Amazon Timestream is more suited for time-series data querying rather than real-time processing and enrichment of IoT data. Also, you’d need to manage the logic for both querying Timestream and handling the S3 upload in a Lambda function, which has more overhead than using Amazon Data Firehose.

 

The option that says: **Use AWS IoT Core Basic Ingest to forward sensor data to Amazon Kinesis Data Streams. Deploy an Auto Scaling group of EC2 instances to enrich and process the data, and use the S3 `PutObject` API to upload the processed data in Amazon S3** is incorrect. Using EC2 instances for data processing only introduces unnecessary operational overhead. While Kinesis Data Streams could handle the data ingestion, managing an Auto Scaling group of EC2 instances would be more complex to setup than using managed services like AWS Lambda and Amazon Data Firehose.

 

 

**References:**

 

[https://aws.amazon.com/blogs/iot/ingesting-enriched-iot-data-into-amazon-s3-using-amazon-kinesis-data-firehose/](https://aws.amazon.com/blogs/iot/ingesting-enriched-iot-data-into-amazon-s3-using-amazon-kinesis-data-firehose/)

 

[https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)

 

[https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

 

[https://docs.aws.amazon.com/lambda/latest/dg/welcome.html](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

 

 

**Check out these AWS Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-lambda/](https://tutorialsdojo.com/aws-lambda/)

 

[https://tutorialsdojo.com/amazon-kinesis/](https://tutorialsdojo.com/amazon-kinesis/)

 

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

 

[https://tutorialsdojo.com/aws-iot-core/](https://tutorialsdojo.com/aws-iot-core/)

---

## Câu 19 — ✅ ĐÚNG

### Câu hỏi

A company has recently released a new mobile game. With the boost in marketing, the mobile game suddenly became viral. The registration webpage is bombarded with user registrations from around the world. The registration website is hosted on a fleet of Amazon EC2 instances created as an Auto Scaling group. This cluster is behind an Application Load Balancer to balance the user traffic. The website contains static content that is loaded differently depending on the user’s device type. With the sudden increase in user traffic, the fleet of Amazon EC2 instances experienced high CPU usage and users are reporting sluggishness on the website.



Which of the following options should the Solutions Architect implement to improve the website response time?

### Các phương án

- **A.** Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Configure CloudFront to deliver different contents depending on the user’s `User-Agent HTTP` header.
- **B.** Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Write a Lambda@Edge function to parse the `User-Agent HTTP` header and serve the appropriate contents based on the user’s device type.
- **C.** Use a Network Load Balancer (NLB) instead of an ALB to distribute the user traffic. Create a dedicated Auto Scaling group for the different device types. Configure the NLB to parse the `User-Agent HTTP` header to route the users to the appropriate EC2 Auto Scaling groups.
- **D.** Create a dedicated Auto Scaling group for the different device types and create separate Application Load Balancers (ALB) for each group. Create an Amazon Route 53 entry to route the users to the appropriate ALB depending on their `User-Agent HTTP` header.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**Lambda@Edge**  is an extension of AWS Lambda, a compute service that lets you execute functions that customize the content that CloudFront delivers. You can author Node.js or Python functions in one Region, US-East-1 (N. Virginia), and then execute them in AWS locations globally that are closer to the viewer, without provisioning or managing servers. Lambda@Edge scales automatically, from a few requests per day to thousands per second. Processing requests at AWS locations closer to the viewer instead of on origin servers significantly reduces latency and improves the user experience.

 

![image](https://media.tutorialsdojo.com/sap_lambda_workflow.png)

 

When you associate a **CloudFront distribution**  with a **Lambda@Edge function** , CloudFront intercepts requests and responses at CloudFront edge locations. You can execute Lambda functions when the following CloudFront events occur:

 

– When CloudFront receives a request from a viewer (viewer request)

 

– Before CloudFront forwards a request to the origin (origin request)

 

– When CloudFront receives a response from the origin (origin response)

 

– Before CloudFront returns the response to the viewer (viewer response)

 

There are many uses for Lambda@Edge processing. For example:

 

– A Lambda function can inspect cookies and rewrite URLs so that users see different versions of a site for A/B testing.

 

– CloudFront can return different objects to viewers based on the device they’re using by checking the User-Agent header, which includes information about the devices. For example, CloudFront can return different images based on the screen size of their device. Similarly, the function could consider the value of the Referer header and cause CloudFront to return the images to bots that have the lowest available resolution.

 

– Or you could check cookies for other criteria. For example, on a retail website that sells clothing, if you use cookies to indicate which color a user chose for a jacket, a Lambda function can change the request so that CloudFront returns the image of a jacket in the selected color.

 

– A Lambda function can generate HTTP responses when CloudFront viewer request or origin request events occur.

 

– A function can inspect headers or authorization tokens, and insert a header to control access to your content before CloudFront forwards the request to your origin.

 

– A Lambda function can also make network calls to external resources to confirm user credentials, or fetch additional content to customize a response.

 

You can configure CloudFront to cache objects based on values in the User-Agent header, but AWS doesn’t recommend it. The User-Agent header has many possible values, and caching based on those values would cause CloudFront to forward significantly more requests to your origin. If you do not configure CloudFront to cache objects based on values in the `User-Agent` header, CloudFront adds a `User-Agent` header with the following value before it forwards a request to your origin: `User-Agent = Amazon CloudFront`.

 

Therefore, the correct answer is: **Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Write a Lambda@Edge function to parse the `User-Agent HTTP` header and serve the appropriate contents based on the user’s device type.**  CloudFront will run the Lamda@Edge function for every request to serve the appropriate content to the user. This will lessen the load on the EC2 instances of the Auto Scaling group.

 

The option that says: **Use a Network Load Balancer (NLB) instead of an ALB to distribute the user traffic. Create a dedicated Auto Scaling group for the different device types. Configure the NLB to parse the `User-Agent HTTP` header to route the users to the appropriate EC2 Auto Scaling groups**  is incorrect. An NLB operates at Layer 4 of the OSI network model so it can’t read the `User-Agent HTTP` header which is present at Layer 7.

 

The option that says: **Create a dedicated Auto Scaling group for the different device types and create separate Application Load Balancers (ALB) for each group. Create an Amazon Route 53 entry to route the users to the appropriate ALB depending on their `User-Agent HTTP` header**  is incorrect. This is not possible because Amazon Route 53 does not have a way to direct users based on HTTP headers.

 

The option that says: **Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Configure CloudFront to deliver different contents depending on the user’s `User-Agent HTTP` header**  is incorrect. This may be possible as you can configure CloudFront to cache objects based on values in the Date and User-Agent headers, but AWS doesn’t recommend it. These headers have many possible values, and caching based on their values would cause CloudFront to forward significantly more requests to your origin.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works.html)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-user-agent-header](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-user-agent-header)

 

 

**Check out these AWS Lambda and Amazon CloudFront Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-lambda/](https://tutorialsdojo.com/aws-lambda/)

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

---

## Câu 20 — ✅ ĐÚNG

### Câu hỏi

A leading commercial bank has multiple AWS accounts that are consolidated using AWS Organizations. The bank uses AWS Firewall Manager to centrally manage firewall rules across all its AWS accounts. The cybersecurity team already centrally manages Firewall Policies for web applications via Firewall Manager. The bank is building an online portal for foreclosed real estate properties that it owns. The online portal is designed to use SSL for better security. The bank would like to implement a separation of responsibilities between the DevOps team and its cybersecurity team. The DevOps team is entitled to manage and log in to the Amazon EC2 instances, while the cybersecurity team has exclusive access to the application’s X.509 certificate, which contains the private key and is stored in AWS Certificate Manager (ACM).



Which of the following options would satisfy the company requirements?

### Các phương án

- **A.** Set up a Service Control Policy (SCP) that authorizes access to the certificate store only for the cybersecurity team and then add a configuration to terminate the SSL on the ELB.
- **B.** Use the AWS Config service to configure the EC2 instances to retrieve the X.509 certificate upon boot from an AWS CloudHSM that is managed by the cybersecurity team.
- **C.** Configure an IAM policy that authorizes access to the certificate store only for the cybersecurity team and then add a configuration to terminate the SSL on the ELB.
- **D.** Upload the X.509 certificate to an Amazon S3 bucket owned by the cybersecurity team and accessible only by the IAM role of the EC2 instances. Use the AWS Systems Manager Session Manager as the HTTPS session manager for the application.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

In this scenario, the best solution is to set the appropriate IAM policy to both the DevOps and cybersecurity teams and then add a configuration to terminate the SSL on the ELB.

 

Take note that you can either terminate the SSL on the ELB side or on the EC2 instance. If you choose the former, the X.509 certificate will only be present in the ELB and if you choose the latter, the X.509 certificate will be stored inside the EC2 instance.

 

Since we don’t want the DevOps team to have access to the certificate, it is best to terminate the SSL on the ELB level rather than the EC2.

 

![image](https://media.tutorialsdojo.com/sap_alb_ssl_cert.png)

 

Therefore, the correct answer is: **Configure an IAM policy that authorizes access to the certificate store only for the cybersecurity team and then add a configuration to terminate the SSL on the ELB.**

 

The option that says: **Use the AWS Config service to configure the EC2 instances to retrieve the X.509 certificate upon boot from an AWS CloudHSM that is managed by the cybersecurity team**  is incorrect. The AWS Config service simply enables you to assess, audit, and evaluate the configurations of your AWS resources. It does not grant any permission or access. In addition, CloudHSM is a managed hardware security module (HSM) in the AWS Cloud that handles encryption keys and not SSL certificates.

 

The option that says: **Upload the X.509 certificate to an Amazon S3 bucket owned by the cybersecurity team and accessible only by the IAM role of the EC2 instances. Use the AWS Systems Manager Session Manager as the HTTPS session manager for the application**  is incorrect because the Systems Manager Session Manager service simply provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys. This service does not handle SSL connections. It is also a security risk to store X.509 certificates in an S3 bucket. It should be stored in the AWS Certificate Manager.

 

The option that says: **Set up a Service Control Policy (SCP) that authorizes access to the certificate store only for the cybersecurity team and then adding a configuration to terminate the SSL on the ELB**  is incorrect. A service control policy (SCP) simply determines what services and actions can be delegated by administrators to the users and roles in the accounts to which the SCP is applied. It does not grant any permissions, unlike an IAM Policy.

 

 

**References:**

 

[https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadServerCertificate.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadServerCertificate.html )

 

[https://aws.amazon.com/blogs/aws/elastic-load-balancer-support-for-ssl-termination/](https://aws.amazon.com/blogs/aws/elastic-load-balancer-support-for-ssl-termination/)

 

 

**Check out these AWS Elastic Load Balancing (ELB) and IAM Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-elastic-load-balancing-elb/](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/)

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

 

 

**Service Control Policies (SCP) vs IAM Policies:**

 

[https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/](https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/)

---

## Câu 21 — ✅ ĐÚNG

### Câu hỏi

An organization is migrating its on-premises web application to AWS. The application comprises a Java-based backend and a NoSQL MongoDB database. Due to constraints, the application cannot be modified during the migration process, and the migrated solution must maintain an architecture similar to the on-premises setup. Additionally, the application requires high availability for both the backend and the database to ensure continuous operation.



Which solution will meet these requirements while adhering to the constraints?

### Các phương án

- **A.** Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Use Amazon DocumentDB (with MongoDB compatibility) in a single Availability Zone deployment to host the MongoDB database.
- **B.** Use AWS Elastic Beanstalk to deploy the Java application and migrate the MongoDB database to Amazon Aurora with multiple read replicas across different Availability Zones.
- **C.** Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Migrate the MongoDB database to Amazon DocumentDB (with MongoDB compatibility) across multiple Availability Zones.
- **D.** Containerize the Java application using AWS App2Container and deploy it on Amazon Elastic Kubernetes Service (EKS). Use Amazon DynamoDB for the database layer to achieve high availability.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**Amazon DocumentDB (with MongoDB Compatibility)**  is a managed NoSQL database service designed to seamlessly support MongoDB workloads. It allows the organization to migrate its existing MongoDB database without requiring application changes, as it is compatible with MongoDB’s JSON-like storage format, query language, and drivers. This service ensures high availability by deploying data across three Availability Zones by default, providing fault tolerance and durability. If a primary instance fails, Amazon DocumentDB automatically promotes a replica to primary, ensuring continuous operations without manual intervention. This makes it an ideal choice for the organization’s needs, as it adheres to the requirement of high availability for the database layer and maintains architectural compatibility.

 

![image](https://media.tutorialsdojo.com/public/amazon-document-db-06Jan2025.png)

 

**Amazon EC2 instances:**  EC2 (Elastic Compute Cloud) provides scalable computing capacity in the AWS cloud. By deploying the Java application on EC2 instances, you retain the flexibility to run custom configurations and setups that closely match your on-premises environment.

 

An **Auto Scaling group**  manages the fleet of Amazon EC2 instances hosting the Java-based backend application. It ensures that the correct number of instances are always running to handle varying levels of application traffic. By dynamically scaling up during peak traffic and scaling down during lower demand, Auto Scaling optimizes costs while maintaining performance. Moreover, it replaces unhealthy instances automatically, ensuring that the backend application remains operational even in the event of instance failures. This makes Auto Scaling crucial for providing the required scalability and fault tolerance for the application.

 

![image](https://media.tutorialsdojo.com/public/auto-scaling-group-06Jan2025.png)

 

**Multiple Availability Zones**  are leveraged to ensure high availability and fault tolerance for both the backend and database. Resources are deployed across at least two physically separate zones within the AWS Region. This setup ensures that the application and database remain operational even if one Availability Zone experiences an outage. The distribution of resources across zones also improves resiliency and fault tolerance while enhancing overall application availability. By deploying in multiple zones, the organization can maintain a highly available architecture similar to the on-premises setup, with the added benefit of AWS’s robust infrastructure.

 

Hence, the correct answer is: **Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Migrate the MongoDB database to Amazon DocumentDB (with MongoDB compatibility) across multiple Availability Zones.**

 

The option that says: **Containerize the Java application using AWS App2Container and deploy it on Amazon Elastic Kubernetes Service (EKS). Use Amazon DynamoDB for the database layer to achieve high availability**  is incorrect because it primarily involves significant changes to the application’s architecture, particularly replacing MongoDB with DynamoDB, which is a different type of database.

 

The option that says: **Use AWS Elastic Beanstalk to deploy the Java application and migrate the MongoDB database to Amazon Aurora with multiple read replicas across different Availability Zones**  is incorrect because it changes the database from MongoDB to Amazon Aurora, which is a relational database service. This would not maintain the same architecture as the on-premises setup.

 

The option that says: **Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Use Amazon DocumentDB (with MongoDB compatibility) in a single Availability Zone deployment to host the MongoDB database** is incorrect because while it uses Amazon DocumentDB, it only deploys it in a single Availability Zone, which does not meet the high availability requirement for the database.

 

 

**References:**

 

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)

 

[https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)

 

 

**Check out this Amazon DocumentDB Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-documentdb/](https://tutorialsdojo.com/amazon-documentdb/)

---

## Câu 22 — ✅ ĐÚNG

### Câu hỏi

A pharmaceutical firm must securely store confidential experimental data. The company manages user authentication through AWS IAM Identity Center and has assigned its R&D scientists to a dedicated group.



The firm wants to consolidate all research documents into a shared Amazon S3 bucket while ensuring that each scientist can only access files they own. In addition, the company wants monthly audit reports detailing which users accessed which documents.



What combination of steps will satisfy these requirements? (Select TWO.)

### Các phương án

- **A.** Create a custom IAM Identity Center role with a permission set granting access to the S3 bucket. Use an identity-based policy restricting data access to prefixes identified by each user’s tag, such as the `${aws:PrincipalTag/userNameID}/*`condition.
- **B.** Use S3 Object Lock in Governance mode to prevent unauthorized research data modification. Use AWS Config rules to monitor and report on S3 object access patterns every week.
- **C.** Enable AWS CloudTrail data event logging for the S3 bucket and store these logs in a separate bucket. Use Amazon Athena (with an Amazon Athena connector) to query the CloudTrail logs monthly and generate comprehensive user access reports.
- **D.** Create an S3 Access Point for each scientist with a resource policy restricting access to objects with matching prefixes. Enable S3 Server Access Logging and use Amazon QuickSight to visualize access patterns.
- **E.** Turn on S3 server access logging and store the logs in an EMRFS (EMR File System ). Use Amazon Athena to query the EMRFS logs directly for monthly usage reporting.

> **Bạn chọn:** A, C
> **Đáp án đúng:** A, C

### Giải thích

Correct 

**AWS IAM Identity Center**  centralizes access management for various AWS accounts and applications. It provides single sign-on (SSO) access, enabling users to manage all their assigned accounts from a single location. Users can synchronize with an existing identity provider or create new users and groups directly within the service.

 

IAM Identity Center utilizes permission sets—collections of IAM policies—to manage user access across AWS Organizations. It includes a user-friendly AWS Access Portal for easy access to applications and supports deployment for both organization and account instances. Designed for high availability across multiple availability zones, the service ensures secure access through AWS Identity and Access Management (IAM) roles and policies.

 

![image](https://media.tutorialsdojo.com/public/td-aws-iam-identity-center-tag-condition-role-example-12-17-24.png)

 

**CloudTrail data events**  are detailed records of resource operations in AWS services. They provide visibility into specific actions performed on or within a resource, such as Amazon S3 object-level API activity, Lambda function executions, or DynamoDB table operations.

 

![image](https://media.tutorialsdojo.com/public/td-cloudtrail-data-events-s3-12-17-24.png)

 

**Amazon Athena**  is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. It’s serverless, so there’s no infrastructure to manage, and you pay only for the queries you run.

 

Hence, the correct answers are:

 

**– Create a custom IAM Identity Center role with a permission set granting access to the S3 bucket. Use an identity-based policy restricting data access to prefixes identified by each user’s tag, such as the `${aws:PrincipalTag/userNameID}/*`condition.** This approach uses the IAM Identity Center for authentication and leverages identity-based policies with user tags to restrict access to specific prefixes in the S3 bucket. This meets the requirement of ensuring each scientist can only access their own files.

 

**– Enable AWS CloudTrail data event logging for the S3 bucket and store these logs in a separate bucket. Use Amazon Athena (with an Amazon Athena connector) to query the CloudTrail logs monthly and generate comprehensive user access reports.** CloudTrail can log all data events (object-level API activity) in the S3 bucket, and Athena can be used to query these logs and generate detailed reports on user access patterns.

 

The option that says: **Use S3 Object Lock in Governance mode to prevent unauthorized research data modification. Use AWS Config rules to monitor and report on S3 object access patterns every week** is incorrect. While S3 Object Lock can typically prevent modifications, it doesn’t address the access control requirements. Additionally, AWS Config rules don’t provide detailed access reports as required.

 

The option that says: **Create an S3 Access Point for each scientist with a resource policy restricting access to objects with matching prefixes. Enable S3 Server Access Logging and use Amazon QuickSight to visualize access patterns** is incorrect. This option could only work for access control, it doesn’t provide the detailed monthly audit reports required. QuickSight is more suited for business intelligence than detailed access auditing.

 

The option that says: **Turn on S3 server access logging and store the logs in an EMRFS (EMR File System ). Use Amazon Athena to query the EMRFS logs directly for monthly usage reporting** is incorrect. While S3 server access logging can provide detailed logs, storing them in EMRFS is unnecessary and complicates the solution. Athena can query S3 logs directly without EMRFS.

 

 

**References:**

 

[https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging-console.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging-console.html)

 

[https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

 

[https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html)

 

 

**Check out the following Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

 

[https://tutorialsdojo.com/amazon-athena/](https://tutorialsdojo.com/amazon-athena/)

 

[https://tutorialsdojo.com/aws-cloudtrail/](https://tutorialsdojo.com/aws-cloudtrail/)

---

## Câu 23 — ✅ ĐÚNG

### Câu hỏi

An analytics company plans to create a self-service solution that will provide a safe and cost-effective way for data scientists to access Amazon SageMaker AI on the company’s AWS accounts. The data scientists have limited knowledge of the AWS cloud, so the complex setup requirements for its ML models should not be exposed. The company wants the data scientists to be able to launch a Jupyter notebook instance if needed. The data at rest on the storage volume of the notebook instance must be encrypted with a preconfigured AWS KMS key.



Which of the following solutions will meet the company requirements with the LEAST amount of operational overhead?

### Các phương án

- **A.** Write an AWS CloudFormation template that contains the `AWS::SageMaker::NotebookInstance` resource type to launch a Jupyter notebook instance with a preconfigured KMS key. On the Outputs section of the CloudFormation template, reference the URL of the notebook instance. Rename this template to be more user-friendly and upload it to a shared Amazon S3 bucket for distribution to the data scientists.
- **B.** Create an Amazon S3 bucket with website hosting enabled. Create a simple form as a front-end website hosted on the S3 bucket that allows the data scientist to input their request for Jupyter notebook creation. Send the request to an Amazon API Gateway that will invoke an AWS Lambda function with an IAM role permission to create the Jupyter notebook instance with a preconfigured KMS key. Have the Lambda function reply the URL of the notebook instance for display on the front-end website.
- **C.** Write an AWS CloudFormation template that contains the `AWS::SageMaker::NotebookInstance` resource type to launch a Jupyter notebook instance with a preconfigured KMS key. Create Mappings on the CloudFormation to map simpler parameter names for instance sizes such as Small, Medium, Large. Reference the URL of the notebook instance on the Outputs section of the template. Create a portfolio in AWS Service Catalog and upload the template to be shared with the IAM role of the data scientists.
- **D.** Create an AWS CloudFormation template that provisions a SageMaker AI notebook instance with a preconfigured KMS key. Use AWS Control Tower Account Factory to create a dedicated AWS account for each data scientist and automatically deploy the notebook template through CloudFormation StackSets. Allow the data scientists to access their assigned notebook instances through the SageMaker AI console.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**AWS Service Catalog**  allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage deployed IT services and your applications, resources, and metadata.

 

With AWS Service Catalog, you define your own catalog of AWS services and AWS Marketplace software and make them available for your organization. Then, end users can quickly discover and deploy IT services using a self-service portal.

 

**Amazon SageMaker AI**  is a fully managed machine learning service. With SageMaker AI, data scientists and developers can quickly and easily build and train machine learning models and then directly deploy them into a production-ready hosted environment. It provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don’t have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. With native support for bring-your-own algorithms and frameworks, SageMaker AI offers flexible distributed training options that adjust to your specific workflows.

 

You can easily create a self-service, secured data science using Amazon SageMaker AI, AWS Service Catalog, and AWS Key Management Service (KMS). Using AWS Service Catalog, you can use a pre-configured AWS KMS key to encrypt data at rest on the machine learning (ML) storage volume that is attached to your notebook instance without ever exposing the complex, unnecessary details to data scientists. ML storage volume encryption is enforced by an AWS Service Catalog product that is pre-configured by centralized security and/or infrastructure teams.

 

![image](https://media.tutorialsdojo.com/sap_service_catalog.png)

 

Hence, the correct answer is: **Write an AWS CloudFormation template that contains the `AWS::SageMaker::NotebookInstance` resource type to launch a Jupyter notebook instance with a preconfigured KMS key. Create Mappings on the CloudFormation to map simpler parameter names for instance sizes such as Small, Medium, Large. Reference the URL of the notebook instance on the Outputs section of the template. Create a portfolio in AWS Service Catalog and upload the template to be shared with the IAM role of the data scientists.**

 

The option that says: **Create an Amazon S3 bucket with website hosting enabled. Create a simple form as a front-end website hosted on the S3 bucket that allows the data scientist to input their request for Jupyter notebook creation. Send the request to an Amazon API Gateway that will invoke an AWS Lambda function with an IAM role permission to create the Jupyter notebook instance with a preconfigured KMS key. Have the Lambda function reply the URL of the notebook instance for display on the front-end website**  is incorrect. Although this is possible, this requires a lot of operational overhead as you need to write a custom website and write a proper Lambda function that has the appropriate code to create the needed resources. Additionally, as the company has several accounts, you will need to create the Lambda function for each AWS account.

 

The option that says: **Write an AWS CloudFormation template that contains the `AWS::SageMaker::NotebookInstance` resource type to launch a Jupyter notebook instance with a preconfigured KMS key. On the Outputs section of the CloudFormation template, reference the URL of the notebook instance. Rename this template to be more user-friendly and upload it to a shared Amazon S3 bucket for distribution to the data scientists**  is incorrect. This is possible; however, it is not very user-friendly, as users need to download the appropriate CloudFormation template from Amazon S3 and then upload it to CloudFormation. They just need to input the needed parameters for the creation of their Jupyter notebook instance.

 

The option that says: **Create an AWS CloudFormation template that provisions a SageMaker AI notebook instance with a preconfigured KMS key. Use AWS Control Tower Account Factory to create a dedicated AWS account for each data scientist and automatically deploy the notebook template through CloudFormation StackSets. Allow the data scientists to access their assigned notebook instances through the SageMaker AI console**  is incorrect because it is overly complex and costly. Provisioning a dedicated AWS account for each data scientist is unnecessary for this use case. Control Tower and StackSets are typically intended for large-scale multi-account governance, not lightweight notebook provisioning. This adds significant operational overhead compared to Service Catalog.

 

 

**References:**

 

[https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/](https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/)

 

[https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

 

[https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)

 

 

**Check out these Amazon SageMaker AI and AWS Service Catalog Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-sagemaker/](https://tutorialsdojo.com/amazon-sagemaker/)

 

[https://tutorialsdojo.com/aws-service-catalog/](https://tutorialsdojo.com/aws-service-catalog/)

---

## Câu 24 — ✅ ĐÚNG

### Câu hỏi

An e-commerce company is running a three-tier application on AWS. The application includes a web tier as frontend, an application tier as backend, and the database tier that stores the transactions and users’ data. The database is currently hosted on an extra-large instance with 128 GB of memory. The company is also considering using Amazon Managed Grafana to monitor the performance of its application infrastructure.



For the company’s business continuity and disaster recovery plan, the Solutions Architect must ensure a Recovery Time Objective (RTO) of 5 minutes and a Recovery Point Objective (RPO) of 1 hour on the backup site in the event that the application goes down. There is also a requirement for the backup site to be at least 250 miles away from the primary site.



Which of the following solutions must the Solutions Architect implement to meet the company’s disaster recovery requirements while keeping the cost at a minimum?

### Các phương án

- **A.** Use a pilot light strategy for the backup region. Configure the primary database to replicate data to a large standby instance in the backup region. In case of a disaster, vertically resize the database instance to meet the full demand. Create an AWS CloudFormation template to quickly provision the same web servers, application servers, and load balancers on the backup region. Update the Amazon Route 53 records to point to the backup region.
- **B.** On the backup region, create a scaled-down version of the fully functional environment with one Amazon EC2 instance of the web server and application server in their own Auto Scaling groups behind Application Load Balancers. Create a standby database instance that replicates data from the primary database. In case of disaster, scale the instances to meet the demand and update the Amazon Route 53 record to point to the backup region.
- **C.** Create a frequently scheduled backup of the application and database that will be stored on an Amazon S3 bucket. Configure S3 Cross-Region Replication (CRR) on the bucket to copy the backups to another region. In case of disaster, use an AWS CloudFormation template to quickly replicate the same resources to the backup region and restore the data from the S3 bucket.
- **D.** Use a multi-region strategy for the backup region to comply with the tight RTO and RPO requirements. Create a fully functional web, application, and database tier on the backup region with the same capacity as the primary region. Set the database on the backup region on standby mode. In case of disaster, update the Amazon Route 53 record to point to the backup region.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

Having backups and redundant workload components in place is the start of your DR strategy. RTO and RPO are your objectives for the restoration of your workload. Set these based on business needs.

 

**Recovery Time Objective (RTO)**  is defined by the organization. RTO is the maximum acceptable delay between the interruption of service and restoration of service. This determines what is considered an acceptable time window when service is unavailable.

 

**Recovery Point Objective (RPO)**  is defined by the organization. RPO is the maximum acceptable amount of time since the last data recovery point. This determines what is considered an acceptable loss of data between the last recovery point and the interruption of service.

 

When architecting a multi-region disaster recovery strategy for your workload, you should choose one of the following multi-region strategies. They are listed in increasing order of complexity, and decreasing order of RTO and RPO. DR Region refers to an AWS Region other than the one primarily used for your workload (or any AWS Region if your workload is on-premises).

 

![image](https://media.tutorialsdojo.com/sap_dr_rto_rpo.png)

 

**– Backup and restore (RPO in hours, RTO in 24 hours or less)** : Back up your data and applications using point-in-time backups into the DR Region. Restore this data when necessary to recover from a disaster.

 

**– Pilot light (RPO in minutes, RTO in hours)** : Replicate your data from one region to another and provision a copy of your core workload infrastructure. Resources required to support data replication and backup such as databases and object storage are always on. Other elements such as application servers are loaded with application code and configurations, but are switched off and are only used during testing or when Disaster Recovery failover is invoked.

 

**– Warm standby (RPO in seconds, RTO in minutes)** : Maintain a scaled-down but fully functional version of your workload always running in the DR Region. Business-critical systems are fully duplicated and are always on, but with a scaled down fleet. When the time comes for recovery, the system is scaled up quickly to handle the production load.

 

**– Multi-region (multi-site) active-active (RPO near zero, RTO potentially zero)** : Your workload is deployed to, and actively serving traffic from, multiple AWS Regions. This strategy requires you to synchronize data across Regions.

 

The difference between **Pilot Light**  and **Warm Standby**  can sometimes be difficult to understand. Both include an environment in your DR Region with copies of your primary region assets. The distinction is that Pilot Light cannot process requests without additional action taken first, while Warm Standby can handle traffic (at reduced capacity levels) immediately. Pilot Light will require you to turn on servers, possibly deploy additional (non-core) infrastructure and then scale up. In Warm Standby, it only requires you to scale up your resources since all the necessary components are already deployed and running). You can choose between these two disaster recovery strategies based on your RTO and RPO needs.

 

Therefore, the correct answer is:**On the backup region, create a scaled-down version of the fully functional environment with one Amazon EC2 instance of the web server and application server in their own Auto Scaling groups behind Application Load Balancers. Create a standby database instance that replicates data from the primary database. In case of disaster, scale the instances to meet the demand and update the Amazon Route 53 record to point to the backup region.**

 

The option that says: **Create a frequently scheduled backup of the application and database that will be stored on an Amazon S3 bucket. Configure S3 Cross-Region Replication (CRR) on the bucket to copy the backups to another region. In case of disaster, use an AWS CloudFormation template to quickly replicate the same resources to the backup region and restore the data from the S3 bucket**  is incorrect. Basically, this is just a backup and restore strategy that has RPO in hours and RTO in 24 hours or less. Even with using CloudFormation, provisioning resources and restoring the backups from an Amazon S3 bucket may take a long time. Take note that the required RTO is only 5 minutes.

 

The option that says: **Use a pilot light strategy for the backup region. Configure the primary database to replicate data to a large standby instance in the backup region. In case of a disaster, vertically resize the database instance to meet the full demand. Create an AWS CloudFormation template to quickly provision the same web servers, application servers, and load balancers on the backup region. Update the Amazon Route 53 records to point to the backup region**  is incorrect. Although this reduces the recovery time because the database instance is already replicated, you may still miss the 5 minute RTO because provisioning the needed servers and load balancers may take several minutes.

 

The option that says: **Use a multi-region strategy for the backup region to comply with the tight RTO and RPO requirements. Create a fully functional web, application, and database tier on the backup region with the same capacity as the primary region. Set the database on the backup region on standby mode. In case of disaster, update the Amazon Route 53 record to point to the backup region**  is incorrect. Although this meets the RTO and RPO requirements, keeping a multi-region strategy is very expensive. With the given cost-effectiveness requirement, using the warm standby strategy is the most suitable one to use in this scenario.

 

 

**References:**

 

[https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html)

 

[https://aws.amazon.com/blogs/aws/new-whitepaper-use-aws-for-disaster-recovery/](https://aws.amazon.com/blogs/aws/new-whitepaper-use-aws-for-disaster-recovery/)

 

[https://d1.awsstatic.com/whitepapers/Storage/Backup_and_Recovery_Approaches_Using_AWS.pdf](https://d1.awsstatic.com/whitepapers/Storage/Backup_and_Recovery_Approaches_Using_AWS.pdf)

 

 

**Backup and Restore vs Pilot Light vs Warm Standby vs Multi-Site:**

 

[https://tutorialsdojo.com/backup-and-restore-vs-pilot-light-vs-warm-standby-vs-multi-site/](https://tutorialsdojo.com/backup-and-restore-vs-pilot-light-vs-warm-standby-vs-multi-site/)

 

 

**Check out this AWS Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-cheat-sheets/](https://tutorialsdojo.com/aws-cheat-sheets/)

---

## Câu 25 — ✅ ĐÚNG

### Câu hỏi

An e-commerce company is having its annual sale event, where buyers will be able to purchase goods at a large discount on its e-commerce website. The e-commerce site will receive millions of visitors in a short period of time when the sale begins. The visitors will first log in to the site using either a Facebook or Google account and add items to the cart. After purchasing, a page will display the cart items along with the discounted prices. The company is also considering using Amazon Translate to support multiple languages for its international visitors. The company needs to build a checkout system that can handle the sudden surge of incoming traffic. The team evaluated Amazon Managed Streaming for Apache Kafka but opted for a simpler message queue for decoupling.



Which of the following is the MOST scalable solution that the company should use?

### Các phương án

- **A.** Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Lex, then process the user's purchases and store the cart into a Multi-AZ Amazon RDS database.
- **B.** Combine an Elastic Load balancer in front of multiple web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito. The web servers will process the user's purchases and store them in an Amazon DynamoDB table. Use an IAM Role to gain permissions to the DynamoDB table.
- **C.** Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito, then process the user's purchases and store them into an Amazon SQS queue using IAM Roles for Amazon EC2 Instances to gain permissions to the queue. Finally, the items from the queue are retrieved by a set of application servers and stored into an Amazon DynamoDB table.
- **D.** Use the static website hosting feature of Amazon S3 with the Javascript SDK to authenticate the user login with Amazon Cognito. Set up AWS Global Accelerator to deliver the static content stored in the S3 bucket. Store user purchases in an Amazon DynamoDB table and use an IAM Role for managing permissions.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**Amazon Simple Queue Service (SQS)**  is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message oriented middleware, and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

 

![image](https://media.tutorialsdojo.com/public/td-sqs_dynamodb_workflow-22-April2026.png)

 

In this scenario, the best solution is to use a combination of CloudFront, Elastic Load Balancer and SQS to provide a highly scalable architecture.

 

Hence, the correct answer is: **Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito, then process the user’s purchases and store them into an Amazon SQS queue using IAM Roles for Amazon EC2 Instances to gain permissions to the queue. Finally, the items from the queue are retrieved by a set of application servers and stored into an Amazon DynamoDB table.** This is a highly scalable solution and creates an appropriate IAM Role to access the DynamoDB database. In addition, it uses SQS which decouples the application architecture. This will allow the application servers to process the requests.

 

The option that says: **Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Lex, then process the user’s purchases and store the cart into a Multi-AZ Amazon RDS database**  is incorrect because multi-AZ RDS is a more expensive solution when compared to DynamoDB. In addition, Amazon Lex is just a service for building conversational interfaces into any application using voice and text. This is not utilized for user authentication, unlike Amazon Cognito.

 

The option that says:**Use the static website hosting feature of Amazon S3 with the Javascript SDK to authenticate the user login with Amazon Cognito. Set up AWS Global Accelerator to deliver the static content. Store user purchases in an Amazon DynamoDB table and use an IAM Role for managing permissions**  is incorrect. Although this would work, it is not scalable, and storing all the data directly in DynamoDB would consume read and write capacity and increase the cost. Moreover, you cannot use AWS Global Accelerator to deliver the static content stored in the S3 bucket. You have to use Amazon CloudFront instead.

 

The option that says:**Combine an Elastic Load balancer in front of multiple web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito. The web servers will process the user’s purchases and store them in an Amazon DynamoDB table. Use an IAM Role to gain permissions to the DynamoDB table**  is incorrect because it is not scalable and storing all the data directly in DynamoDB would simply consume read and write capacity and increase the cost. Moreover, the web servers are not placed in an Auto Scaling group, which means that this solution is not scalable.

 

 

**References:**

 

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/authentication-and-access-control.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/authentication-and-access-control.html)

 

[https://aws.amazon.com/blogs/database/dynamodb-streams-use-cases-and-design-patterns/](https://aws.amazon.com/blogs/database/dynamodb-streams-use-cases-and-design-patterns/)

 

 

**Check out this Amazon DynamoDB Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-dynamodb/](https://tutorialsdojo.com/amazon-dynamodb/)

---

## Câu 26 — ❌ SAI

### Câu hỏi

A company has several resources in its production environment that is shared among various business units of the company. A single business unit may have one or more AWS accounts that have resources in the production environment. There were a lot of incidents in which the developers from a specific business unit accidentally terminated the Amazon EC2 instances, Amazon EKS clusters, and Amazon Aurora Serverless databases which are owned by another business unit. The solutions architect has been tasked to come up with a solution to only allow a specific business unit that owns the EC2 instances, and other AWS resources, to terminate their own resources.



Which of the following is the most suitable multi-account strategy implementation to meet the company requirements?

### Các phương án

- **A.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to individual Organization Units (OU). Create an IAM Role in the production account, which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the IAM policy to every member account of the OU.
- **B.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the SCP to the OUs, which will then be automatically inherited by its member accounts.
- **C.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Provide the cross-account access and the SCP to the individual member accounts to tightly control who can terminate the EC2 instances.
- **D.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create an IAM Role in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Create an `AWSServiceRoleForOrganizations` service-linked role for the individual member accounts of the OU to enable **trusted access** .

> **Bạn chọn:** B
> **Đáp án đúng:** A

### Giải thích

Incorrect  

**AWS Organizations**  is an account management service that enables you to consolidate multiple AWS accounts into an *organization*  that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.

 

![image](https://media.tutorialsdojo.com/sap_scp_organization.jpg)

 

You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.

 

Resource-level permissions refer to the ability to specify which resources users are allowed to perform actions on. Amazon EC2 has partial support for resource-level permissions. This means that for certain Amazon EC2 actions, you can control when users are allowed to use those actions based on conditions that have to be fulfilled, or specific resources that users are allowed to use. For example, you can grant users permissions to launch instances, but only of a specific type, and only using a specific AMI.

 

The scenario on this question has a lot of AWS Accounts that need to be managed. AWS Organization solves this problem and provides you with control by assigning the different business units as individual Organization Units (OU). Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. However, SCPs alone are not sufficient for allowing access to the accounts in your organization. Attaching an SCP to an AWS Organizations entity just defines a guardrail for what actions the principals can perform. You still need to attach identity-based or resource-based policies to principals or resources in your organization’s accounts to actually grant permission to them.

 

Since SCPs only allow or deny the use of an AWS service, you don’t want to block OUs from completely using the EC2 service. Thus, you will need to provide cross-account access and the IAM policy to every member accounts of the OU.

 

Hence, the correct answer is: **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to individual Organization Units (OU). Create an IAM Role in the production account, which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the IAM policy to every member account of the OU.**

 

The option that says: **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create an IAM Role in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns.** **Create an `AWSServiceRoleForOrganizations` service-linked role for the individual member accounts of the OU to enable` trusted access`**  is incorrect because **AWSServiceRoleForOrganizations**  service-linked role is primarily used to only allow AWS Organizations to create service-linked roles for other AWS services. This service-linked role is present in all organizations and not just in a specific OU.

 

The following options are incorrect because an SCP policy simply specifies the services and actions that users and roles can use in the accounts:

 

**–** **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns.** **Provide the cross-account access and the SCP to the individual member accounts to tightly control who can terminate the EC2 instances.**

 

**–** **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit.** **Provide the cross-account access and the SCP to the OUs, which will then be automatically inherited by its member accounts.**

 

SCPs are similar to IAM permission policies except that they don’t grant any permissions.

 

 

**References:**

 

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html)

 

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

 

 

**Check out these AWS Organizations and** **Comparison of AWS Services Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-organizations/](https://tutorialsdojo.com/aws-organizations/)

 

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

 

 

**Service Control Policies (SCP) vs IAM Policies:**

 

[https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/](https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/)

---

## Câu 27 — ✅ ĐÚNG

### Câu hỏi

A logistics company is developing a new application that will be used for all its departments. All of the company’s AWS accounts are under OrganizationA in its AWS Organizations. A certain feature of the application must allow AWS resource access from a third-party account that is under AWS Organizations named OrganizationB. The company wants to follow security best practices and grant “least privilege” access using an API or CLI to the third-party account. After access is configured, the security team will use Amazon Detective to investigate unusual activity involving the third-party account.



Which of the following options is the recommended way to securely allow OrganizationB to access AWS resources on OrganizationA?

### Các phương án

- **A.** The logistics company must create an IAM user with an IAM policy allowing only the required access. The logistics company should then send the AWS credentials to the third-party account to allow login and perform only specific tasks.
- **B.** The third-party account should create an External ID that will be given to OrganizationA. The logistics company should then create an IAM role with the required access and put the External ID in the IAM role’s trust policy. The third-party account should use the IAM role’s ARN and External ID when requesting access to OrganizationA’s AWS resources.
- **C.** The logistics company should create an IAM role and attach an IAM policy allowing only the required access. The third-party account should then use AWS STS to assume the IAM role’s Amazon Resource Name (ARN) when requesting access to OrganizationA’s AWS resources.
- **D.** The third-party AWS Organization must integrate with the AWS Identity Center of the logistics company. Then create custom IAM policies for the third-party account to only access specific resources under OrganizationA.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

At times, you need to give third-party access to your AWS resources (delegate access). One important aspect of this scenario is the **External ID** , optional information that you can use in an IAM role trust policy to designate who can assume the role. The external ID allows the user who is assuming the role to assert the circumstances in which they are operating. It also provides a way for the account owner to permit the role to be assumed only under specific circumstances.

 

In a multi-tenant environment where you support multiple customers with different AWS accounts, AWS recommends using one external ID per AWS account. This ID should be a random string generated by the third party.

 

To require that the third party provide an external ID when assuming a role, update the role’s trust policy with the external ID of your choice. To provide an external ID when you assume a role, use the AWS CLI or AWS API to assume that role.

 

For example, let’s say that you decide to hire a third-party company called Example Corp to monitor your AWS account and help optimize costs. In order to track your daily spending, Example Corp needs to access your AWS resources. Example Corp also monitors many other AWS accounts for other customers.

 

![image](https://media.tutorialsdojo.com/sap_external_ID_IAM.png)

 

Do not give Example Corp access to an IAM user and its long-term credentials in your AWS account. Instead, use an IAM role and its temporary security credentials. An IAM role provides a mechanism to allow a third party to access your AWS resources without needing to share long-term credentials.

 

Therefore, the correct answer is: **The third-party account should create an External ID that will be given to OrganizationA. The logistics company should then create an IAM role with the required access and put the External ID in the IAM role’s trust policy. The third-party account should use the IAM role’s ARN and External ID when requesting access to OrganizationA’s AWS resources.** An External ID in an IAM role’s trust policy is a recommended best practice to ensure that the external party can assume your role only when it is acting on your behalf.

 

The option that says: **The third-party AWS Organization must integrate with the AWS Identity Center of the logistics company. Then create custom IAM policies for the third-party account to only access specific resources under OrganizationA**  is incorrect. This is not recommended as this will add unnecessary complexity, and there is a possibility for OrganizationB users to log in and view the accounts on OrganizationA.

 

The option that says: **The logistics company must create an IAM user with an IAM policy allowing only the required access. The logistics company should then send the AWS credentials to the third-party account to allow login and perform only specific tasks**  is incorrect. This is possible but not recommended because AWS credentials may get leaked or exposed. It is recommended to use STS to generate a temporary token when requesting access to AWS resources.

 

The option that says: **The logistics company should create an IAM role and attach an IAM policy allowing only the required access. The third-party account should then use AWS STS to assume the IAM role’s Amazon Resource Name (ARN) when requesting access to OrganizationA’s AWS resources**  is incorrect. This is possible but not the most secure way among the options. Without the External ID on the IAM role’s trust policy, it is possible that other AWS accounts can assume that IAM role.

 

 

**References:**

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html)

 

[https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/](https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/)

 

 

**Check out these AWS Organizations and AWS IAM Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-organizations/](https://tutorialsdojo.com/aws-organizations/)

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 28 — ✅ ĐÚNG

### Câu hỏi

A company has a hybrid cloud architecture where their on-premises data center and VPC are connected via multiple AWS Direct Connect ports in a single Link Aggregation Group (LAG). They have an on-premises patch management system that automatically applies the patches to the operating systems of their servers and file systems. You were given a task to synchronize the patch baselines being used on-premises to all of the EC2 instances in your VPC, as well as to automate the patching schedule.



Which of the following methods should you implement to meet the above requirement with the LEAST amount of effort?

### Các phương án

- **A.** Use AWS Systems Manager Session Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by using the AWS Systems Manager Maintenance Windows.
- **B.** Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by setting up scheduled jobs using AWS Lambda and AWS Systems Manager Run Command.
- **C.** Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Install the SSM Agent to all of your instances and automate the patching schedule by using AWS Systems Manager Maintenance Windows.
- **D.** Use the AWS Systems Manager State Manager to automate the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define, which includes the OS patches that should be applied in each EC2 instance. Automate the patching schedule by using AWS Systems Manager Distributor, to package and distribute the required patches to your instances.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**AWS Systems Manager Patch Manager** automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

 

![image](https://media.tutorialsdojo.com/sap_ssm_patch_manager.jpg)

 

**AWS Systems Manager Maintenance Windows**  let you define a schedule for when to perform potentially disruptive actions on your instances such as patching an operating system, updating drivers, or installing software or patches. Each Maintenance Window has a schedule, a maximum duration, a set of registered targets (the instances that are acted upon), and a set of registered tasks. You can also specify dates that a Maintenance Window should not run before or after, and you can specify the international time zone on which to base the Maintenance Window schedule.

 

Therefore, the correct answer is: **Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Install the SSM Agent to all of your instances and automate the patching schedule by using AWS Systems Manager Maintenance Windows.**

 

The option that says: **Use AWS Systems Manager Session Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by using the AWS Systems Manager Maintenance Windows**  is incorrect because the Session Manager is primarily used to comply with corporate policies that require controlled access to instances, strict security practices, and fully auditable logs with instance access details, but not for applying OS patches. Using the AWS Systems Manager Patch Manager is a more appropriate solution to implement.

 

The option that says: **Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by setting up scheduled jobs using AWS Lambda and AWS Systems Manager Run Command**  is incorrect. Although it properly uses AWS Systems Manager Patch Manager, it is still better to use AWS Systems Manager Maintenance Windows instead of manually creating scheduled jobs using AWS Lambda and AWS Systems Manager Run Command. Take note that the scenario specifies that you have to meet the requirement with the LEAST amount of effort, which can be met by using the AWS Systems Manager Maintenance Windows feature. In addition, installing the SSM Agent to all of your instances is also required when using the AWS Systems Manager Patch Manager, which is not mentioned in this option.

 

The option that says: **Use the AWS Systems Manager State Manager to automate the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define, which includes the OS patches that should be applied in each EC2 instance. Automate the patching schedule by using AWS Systems Manager Distributor, to package and distribute the required patches to your instances**  is incorrect because the AWS Systems Manager State Manager is primarily used as a secure and scalable configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define. This does not handle patch management, unlike AWS Systems Manager Patch Manager. With the State Manager, you can configure your instances to boot with a specific software at start-up; download and update agents on a defined schedule; configure network settings and many others, but not the patching of your EC2 instances.

 

 

**References:**

 

[https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

 

[https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)

 

 

**Check out this AWS Systems Manager Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-systems-manager/](https://tutorialsdojo.com/aws-systems-manager/)

---

## Câu 29 — ✅ ĐÚNG

### Câu hỏi

As part of the Corporate Social Responsibility of the tech company, the development team created an online learning system for a public university. The application architecture uses an Application Load Balancer in front of two On-Demand EC2 instances located in two Availability Zones. The only remaining requirement is to secure the new website with an HTTPS connection.



Which of the following option is the most cost-effective and easiest way to complete the online learning system?

### Các phương án

- **A.** Generate a Private Certificate in ACM. Configure the two EC2 instances to use the Private Certificate to handle HTTPS requests.
- **B.** Generate a Public Certificate in ACM. Configure the Application Load Balancer to use the Public Certificate to handle HTTPS requests.
- **C.** Generate a Private Certificate in ACM. Configure the Application Load Balancer to use the Private Certificate to handle HTTPS requests.
- **D.** Generate a Public Certificate in ACM. Configure the two EC2 instances to use the Public Certificate to handle HTTPS requests.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

With **AWS Certificate Manager** , you can generate public or private SSL/TLS certificates that you can use to secure your site. Public SSL/TLS certificates provisioned through AWS Certificate Manager are free. You pay only for the AWS resources that you create to run your application. For private certificates, the ACM Private Certificate Authority (CA) is priced along two dimensions: (1) You pay a monthly fee for the operation of each private CA until you delete it and (2) you pay for the private certificates you issue each month.

 

![image](https://media.tutorialsdojo.com/sap_aws_acm_certs.png)

 

Public certificates generated from ACM can be used on Amazon CloudFront, Elastic Load Balancing, or Amazon API Gateway but not directly on EC2 instances, unlike private certificates.

 

Hence, **generating a Public Certificate in ACM and configuring the Application Load Balancer to use the Public Certificate to handle HTTPS requests**  is correct in this scenario as a public certificate does not cost anything and you can configure this certificate with the Application Load Balancer.

 

The option that says: **Generate a Private Certificate in ACM. Configure the Application Load Balancer to use the Private Certificate to handle HTTPS requests**  is incorrect because this solution entails an additional cost. Remember that you have to pay a monthly fee for the operation of each private CA until you delete it. A more cost-effective solution is to use a public certificate instead since this is free of charge.

 

The option that says: **Generate a Public Certificate in ACM. Configure the two EC2 instances to use the Public Certificate to handle HTTPS requests**  is incorrect because you cannot export public certificates from ACM and use them with your EC2 instances. You can only use the public certificate from ACM in Amazon CloudFront, Elastic Load Balancing, and Amazon API Gateway.

 

The option that says: **Generate a Private Certificate in ACM. Configure the two EC2 instances to use the Private Certificate to handle HTTPS requests**  is incorrect. Although you can export private certificates from ACM and use them with EC2 instances, using this type of certificate still costs more than a public certificate.

 

 

**References:**

 

[https://aws.amazon.com/certificate-manager/pricing/](https://aws.amazon.com/certificate-manager/pricing/)

 

[https://aws.amazon.com/certificate-manager/faqs/](https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf#page=11)

 

 

**Check out this AWS Billing and Cost Management Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-billing-and-cost-management/](https://tutorialsdojo.com/aws-billing-and-cost-management/)

 

 

**How can I add certificates for websites to the ELB using Amazon Certificate Manager?**

 

[https://youtu.be/pTQrAZbHmRU](https://youtu.be/pTQrAZbHmRU)

---

## Câu 30 — ✅ ĐÚNG

### Câu hỏi

There was a major incident that occurred in your company wherein the web application that you are supporting unexpectedly went down in the production environment. Upon investigation, it was found that a junior DevOps engineer terminated the EC2 instance in production which caused the disruption of service. Only the Solutions Architects should be allowed to stop or terminate instances in the production environment. You also found out that there are a lot of developers who have full access to your production AWS account.



Which of the following options will fix this security vulnerability in your cloud architecture and prevent this kind of failure from happening again? (Select TWO.)

### Các phương án

- **A.** Modify the associated IAM Role assigned to the developers by removing the policy that allows them to terminate EC2 instances in production.
- **B.** Modify the IAM policy of the developers to require MFA before deleting EC2 instances.
- **C.** Replace the Security Group of all of the EC2 instances in Production to prevent developers from accessing it.
- **D.** Attach a `PowerUserAccess` AWS managed policy to the developers.
- **E.** Add tags to the EC2 instances in the production environment and assign the developers a role with a policy that denies terminating the instance based on the tag.

> **Bạn chọn:** A, E
> **Đáp án đúng:** A, E

### Giải thích

Correct 

To help you manage your instances, images, and other Amazon EC2 resources, you can optionally assign your own metadata to each resource in the form of tags. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags you’ve assigned to it. For example, you could define a set of tags for your account’s Amazon EC2 instances that help you track each instance’s owner and stack level.

 

![image](https://media.tutorialsdojo.com/sap_iam_identity_vs_resource_policy.png)

 

Take note that MFA is just an additional layer of security but it won’t totally prevent the users from terminating the EC2 instances.

 

**Adding tags to the EC2 instances in the production environment and assign the developers a role with a policy that denies terminating the instance based on the tag**  is correct because it leverages resource tags for identification and IAM roles/policies for access control, following the principle of least privilege and providing a scalable, secure approach to prevent unauthorized termination of production instances while adhering to AWS best practices.

 

**Modifying the associated IAM Role assigned to the developers by removing the policy that allows them to terminate EC2 instances in production**  is correct because changing the IAM Role assigned to the developers to revoke their privilege of terminating EC2 instances will certainly prevent the issue from happening again.

 

**Modifying the IAM policy of the developers to require MFA before deleting EC2 instances**  is incorrect because MFA is just an additional layer of security given to the users when logging into AWS and accessing the resources. However, an MFA alone cannot prevent the users from performing resource level actions, such as terminating the instance.

 

**Replacing the Security Group of all of the EC2 instances in Production to prevent developers from accessing it**  is incorrect because a security group is mainly used to secure and control the traffic coming in and out of the EC2 instances. In this scenario, it is best to modify the IAM policy of all of the developers and add tags to the instances in the production environment.

 

**Attaching a `PowerUserAccess` AWS managed policy to the developers**  is incorrect because it will only provide more permissive access to terminate EC2 instances.

 

 

**References:**

 

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)

 

[https://aws.amazon.com/iam/details/mfa/](https://aws.amazon.com/iam/details/mfa/)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 

 

**Check out these Amazon EC2 and AWS IAM Cheat Sheets:**

 

**[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 31 — ✅ ĐÚNG

### Câu hỏi

A leading fast-food chain has recently adopted a hybrid cloud infrastructure that extends its data centers into AWS Cloud. The solutions architect has been tasked to allow on-premises users, who are already signed in using their corporate accounts, to manage AWS resources without creating separate IAM users for each of them. This is to avoid having two separate login accounts and memorizing multiple credentials.



Which of the following is the best way to handle user authentication in this hybrid architecture?

### Các phương án

- **A.** Authenticate using your on-premises SAML 2.0-compliant identity provider (IDP), retrieve temporary credentials using STS, and grant federated access to the AWS console via the AWS IAM Identity Center.
- **B.** Retrieve AWS temporary security credentials with Web Identity Federation using STS and AssumeRoleWithWebIdentity to enable users to log in to the AWS console.
- **C.** Integrate the company’s authentication process with Amazon AppFlow and allow Amazon STS to retrieve temporary AWS credentials using OAuth 2.0 to enable your members to log in to the AWS Console.
- **D.** Authenticate through your on-premises SAML 2.0-compliant identity provider (IDP) using STS and AssumeRoleWithWebIdentity to retrieve temporary security credentials, which enables your users to log in to the AWS console using a browser.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

In this scenario, you need to provide temporary access to AWS resources to the existing users, but you should not create new IAM users for them to avoid having to maintain two login accounts. This means that you need to set up a single-sign on authentication for your users so they only need to sign-in once in their on-premises network and can also access the AWS cloud at the same time.

 

![image](https://media.tutorialsdojo.com/public/iam-identity-center-1018-1353.png)

 

You can use a role to configure your SAML 2.0-compliant identity provider (IdP) and AWS to permit your federated users to access the AWS Management Console. The role grants the user permission to carry out tasks in the console.

 

Therefore, the correct answer is: **Authenticate using your on-premises SAML 2.0-compliant identity provider (IDP), retrieving temporary credentials using STS, and granting federated access to the AWS console via the AWS IAM Identity center.** It gives federated access to the users to AWS resources by using SAML 2.0 identity provider and it uses on-premises single sign-on (SSO) endpoint to authenticate users, which gives them access tokens prior to providing the federated access.

 

The option that says:**Integrate the company’s authentication process with Amazon AppFlow and allow Amazon STS to retrieve temporary AWS credentials using OAuth 2.0 to enable your members to log in to the AWS Console** is incorrect. Amazon AppFlow is used to securely transfer data between Software-as-a-Service (SaaS) applications like Salesforce, SAP, Zendesk, Slack, and ServiceNow, and AWS services. It is not used for authentication. Additionally, OAuth 2.0 is not applicable in this scenario. We are not using Web Identity Federation as it is used with public identity providers such as Facebook, Google, etc.

 

The option that says:**Authenticate through your on-premises SAML 2.0-compliant identity provider (IDP) using STS and AssumeRoleWithWebIdentity to retrieve temporary security credentials, which enables your users to log in to the AWS console using a browser**  is incorrect. The use of AssumeRoleWithWebIdentity is wrong which is only for Web Identity Federation (Facebook, Google, and other social logins). Even though it uses SAML 2.0 identity provider, the requirement is to provide a single sign-on to users, which means that the users should not sign in to the AWS console using any security credentials but through their corporate identity provider.

 

The option that says:**Retrieve AWS temporary security credentials with Web Identity Federation using STS and AssumeRoleWithWebIdentity to enable users to log in to the AWS console**  is incorrect. We are not using Web Identity Federation as it is used with public identity providers such as Facebook, Google, etc.

 

 

**References:**

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html )

 

[https://aws.amazon.com/identity/federation/](https://aws.amazon.com/identity/federation/ )

 

[https://aws.amazon.com/blogs/security/how-to-establish-federated-access-to-your-aws-resources-by-using-active-directory-user-attributes/](https://aws.amazon.com/blogs/security/how-to-establish-federated-access-to-your-aws-resources-by-using-active-directory-user-attributes/)

 

 

**Check out this AWS IAM Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 32 — ✅ ĐÚNG

### Câu hỏi

A financial startup offers flexible short-term loans of up to $5,000 to its users. Their online portal is hosted in AWS which uses S3 for scalable storage, DynamoDB as a NoSQL database, and a fleet of EC2 instances to host their web servers. To meet the financial regulation, the company is required to undergo a compliance audit.



In this scenario, how will you provide the auditor access to the logs of your AWS resources?

### Các phương án

- **A.** 1. Contact AWS and inform them of the upcoming audit activities. 2. AWS will grant required access to the third-party auditor to see the logs.
- **B.** 1. Enable CloudTrail logging to required AWS resources. 2. Create an IAM user with read-only permissions to the required AWS resources. 3. Provide the access credential to the auditor.
- **C.** 1. Create an IAM role that has the required permissions for the auditor. 2. Attach the roles to the EC2, S3, and DynamoDB.
- **D.** 1. Create an SNS Topic. 2. Configure the SNS to send out an email with the attached CloudTrail log files to the auditor’s email every time the CloudTrail delivers the logs to S3.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**AWS CloudTrail**  is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain events related to API calls across your AWS infrastructure. CloudTrail provides a history of AWS API calls for your account, including API calls made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This history simplifies security analysis, resource change tracking, and troubleshooting.

 

![image](https://media.tutorialsdojo.com/sap_cloudtrail_works.jpg)

 

Therefore the correct answer is:

 

**1. Enable CloudTrail logging to required AWS resources.**

 

**2. Create an IAM user with read-only permissions to the required AWS resources.**

 

**3. Provide the access credential to the auditor.**

 

The following option is incorrect because you do not need to contact AWS for any audit activities since you can just use CloudTrail:

 

**1. Contact AWS and inform them of the upcoming audit activities.**

 

**2. AWS will grant required access to the third-party auditor to see the logs.**

 

You can contact AWS in case you will perform penetration testing to or originating from any of your AWS resources as part of the shared responsibility model, but for audit activities like this, an authorization is not required.

 

The following option is incorrect because it is a security risk to send the CloudTrail logs via email:

 

**1. Create an SNS Topic.**

 

**2. Configure the SNS to send out an email with the attached CloudTrail log files to the auditor’s email every time the CloudTrail delivers the logs to S3.**

 

It is best to keep them stored inside an S3 bucket and just provide read access to the bucket to the auditor.

 

The following option is incorrect because an IAM role should be attached to the IAM user of the auditor but the most preferred way to do this is still to use CloudTrail:

 

**1. Create an IAM role that has the required permissions for the auditor.**

 

**2. Attach the roles to the EC2, S3, and DynamoDB.**

 

 

**References:**

 

[https://aws.amazon.com/cloudtrail/](https://aws.amazon.com/cloudtrail/)

 

[https://aws.amazon.com/blogs/security/how-to-audit-cross-account-roles-using-aws-cloudtrail-and-amazon-cloudwatch-events/](https://aws.amazon.com/blogs/security/how-to-audit-cross-account-roles-using-aws-cloudtrail-and-amazon-cloudwatch-events/)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html)

 

 

**Check out this AWS CloudTrail Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-cloudtrail/](https://tutorialsdojo.com/aws-cloudtrail/)

---

## Câu 33 — ✅ ĐÚNG

### Câu hỏi

An enterprise plans to create a new cloud deployment that will be used by several project teams. The network must be designed so that it allows autonomy for the administrators of the individual AWS accounts to modify their route tables freely. However, the company wants to monitor outbound traffic so it is required to have a centralized and controlled egress Internet connection for all accounts. As more teams are expected to join this deployment, the organization is expected to grow into thousands of AWS accounts.



Which of the following options should the Solutions Architect implement to meet the company requirements?

### Các phương án

- **A.** Create a centralized transit VPC. Have the VPCs on each AWS account connect to the transit VPC using a VPN connection. Control the outbound Internet traffic using firewall appliances.
- **B.** Create a centralized shared VPC. On this VPC, create a subnet that will be associated with each AWS account. Use a fleet of proxy servers to control the outbound Internet traffic.
- **C.** Create a shared transit gateway. Have each spoke VPC connect to the transit gateway. In a central VPC, deploy a Gateway Load Balancer (GWLB) that fronts a fleet of firewall appliances with routing to the public internet.
- **D.** Create a shared services VPC. On this VPC, host the central assets which include a fleet of firewalls that have a route to the public Internet. Have each spoke VPC connect to the central VPC using VPC peering.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**AWS Transit Gateway**  is a highly available and scalable service used to consolidate the AWS VPC routing configuration for a region with a hub-and-spoke architecture. Each spoke VPC only needs to connect to the Transit Gateway to gain access to other connected VPCs. Transit Gateway across different regions can peer with each other to enable VPC communications across regions. With a large number of VPCs, Transit Gateway provides simpler VPC-to-VPC communication management over VPC Peering.

 

**Transit Gateway**  enables customers to connect thousands of VPCs. You can attach all your hybrid connectivity (VPN and Direct Connect connections) to a single Transit Gateway— consolidating and controlling your organization’s entire AWS routing configuration in one place. Transit Gateway controls how traffic is routed among all the connected spoke networks using route tables. This hub and spoke model simplifies management and reduces operational costs because VPCs only connect to the Transit Gateway to gain access to the connected networks.

 

Deploying a Gateway Load Balancer (GWLB) in a central VPC provides a scalable, easy-to-manage layer that fronts a fleet of firewall appliances. The GWLB simplifies the deployment of third-party virtual appliances in AWS, providing a single entry and exit point for traffic and thus facilitating the centralized inspection and control of outbound Internet traffic as required by the scenario.

 

If resources in private subnets need access to the Internet, introducing a NAT Gateway is a common solution. The NAT Gateway allows instances in a private subnet to connect to the Internet or other AWS services while preventing the Internet from initiating a connection with those instances.

 

![image](https://media.tutorialsdojo.com/public/aws-centralized-egress-gwlb.png)

 

Alternatively, if your firewall appliance supports two-arm mode, you may eliminate the need for a NAT Gateway. In two-arm mode, the appliance can perform both inspection and NAT with two network interfaces: one connected to a public subnet and the other to a private subnet.

 

Therefore, the correct answer is: **Create a shared transit gateway. Have each spoke VPC connect to the transit gateway. In a central VPC, deploy a Gateway Load Balancer (GWLB) that fronts a fleet of firewall appliances with routing to the public internet.**

 

The option that says: **Create a centralized transit VPC. Have the VPCs on each AWS account connect to the transit VPC using a VPN connection. Control the outbound Internet traffic using firewall appliances**  is incorrect. Using a VPN connection for connecting within Amazon VPCs or with the transit is not needed. You can use the AWS network backbone which is much faster than setting up a VPN connection.

 

The option that says: **Create a centralized shared VPC. On this VPC, create a subnet that will be associated with each AWS account. Use a fleet of proxy servers to control the outbound Internet traffic**  is incorrect. The default limit for shared VPC subnets is 100. Additionally, on this setup, the participants on the shared subnets will not be able to modify their own route tables.

 

The option that says: **Create a shared services VPC. On this VPC, host the central assets which include a fleet of firewalls that have a route to the public Internet. Have each spoke VPC connect to the central VPC using VPC peering**  is incorrect. There is a default limit of 50 VPC peering for each VPC. This is not enough to handle peering for thousands of AWS accounts.

 

 

**References:**

 

[https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html)

 

[https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html)

 

[https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway.html](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway.html)

 

 

**Check out these AWS Transit Gateway and Amazon VPC Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-transit-gateway/](https://tutorialsdojo.com/aws-transit-gateway/)

 

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

---

## Câu 34 — ✅ ĐÚNG

### Câu hỏi

A weather forecasting agency established a network of IoT devices in the ocean to help predict incoming typhoons. The IoT devices monitor the sea surface temperature and atmospheric pressure and send the data as messages to AWS IoT Core, which updates an Amazon DynamoDB table. On the weekly monitoring report, a system administrator notices that no new database updates are happening. The agency already uses AWS IoT Device Defender to audit device security policies and detect abnormal behavior, but this does not help diagnose connectivity interruptions.



What should the administrator do to troubleshoot the issue?

### Các phương án

- **A.** Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core.
- **B.** Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity.
- **C.** Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click.
- **D.** Register the IoT devices to AWS IoT Device Management and monitor the devices' health and ensure the devices are connected to AWS IoT Core.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

AWS IoT Device Management is a service that makes it easy to securely register, organize, monitor, and remotely manage IoT devices at scale throughout their lifecycle. You can use IoT Device Management to upload and view device information and configuration, organize your device inventory, monitor your fleet of devices, troubleshoot individual devices, and remotely manage devices deployed across many locations, including updating device software over-the-air (OTA).

 

By registering the IoT devices to AWS IoT Device Management, the system administrator can monitor the health of the devices and ensure connectivity to AWS IoT Core. This will help identify if there are connectivity issues that might be causing the lack of updates in the DynamoDB table.

 

![image](https://media.tutorialsdojo.com/public/AWSIoTDeviceManagementConsole.jpg)

 

AWS IoT Device Management has a feature that allows you to group your device fleet based on function, security requirements, or other categories. This makes it easier to manage IoT devices at scale. The groupings allow policy management, viewing metrics, or performing actions on the entire group.

 

Therefore, the correct answer is: **Register the IoT devices to AWS IoT Device Management and monitor the devices’ health and ensure the devices are connected to AWS IoT Core.**

 

The option that says: **Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity**  is incorrect. AWS IoT Defender is primarily used for security audit, alerting, and mitigation of IoT resources and does not directly manage Certificate Authority in AWS IoT Core. It is also not used for establishing connectivity between the devices and AWS IoT Core.

 

The option that says: **Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core** is incorrect. AWS IoT SiteWise is simply used for collecting and gaining insights to equipment data for industrial operations management. It is not used for collecting data from IoT devices.

 

The option that says: **Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click**  is incorrect. Triggering a Lambda function does not address the potential connectivity issue between the IoT devices and AWS IoT Core. Using it to directly update the DynamoDB table will bypass AWS IoT Core and is not the solution to the question.

 

**References:**

 

[https://aws.amazon.com/iot-device-management/faq/](https://aws.amazon.com/iot-device-management/faq/)

 

[https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html)

 

 

**Check out this AWS IoT Core Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-iot-core/](https://tutorialsdojo.com/aws-iot-core/)

---

## Câu 35 — ✅ ĐÚNG

### Câu hỏi

A company has an Oracle Real Application Clusters (RAC) database on their on-premises data center which they want to migrate to AWS. The Chief Information Security Officer (CISO) instructed the solutions architects to automate the patch management process of the operating system in which the database runs, as well as to set up scheduled backups to comply with the company’s disaster recovery plan.



Which of the following should the solutions architect implement to meet the company requirements with the least amount of effort?

### Các phương án

- **A.** Launch a Lambda function that would automate the creation of snapshots of the database in the EC2 instance. Use the CodeDeploy and CodePipeline service to automate the patch management process of the database.
- **B.** Migrate the database to Amazon RDS which provides a multi-AZ failover feature for your RAC cluster. This will also reduce the RPO and RTO in the event of system failure since RDS offers features such as patch management and maintenance of the underlying host.
- **C.** Migrate the database to a cluster of EBS-backed Amazon EC2 instances across multiple AZs. Automate the creation of EBS snapshots from EBS volumes of the EC2 instance by using Amazon Data Lifecycle Manager. Install the SSM Agent to the EC2 instance and automate the patch management process using AWS Systems Manager Patch Manager.
- **D.** Migrate the database to Amazon Aurora and enable automated backups for your Aurora RAC cluster. Patching is automatically handled in Aurora during the system maintenance window.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

Amazon RDS does not support certain features in Oracle such as Multitenant Database, Real Application Clusters (RAC), Unified Auditing, Database Vault, and many more.

 

**AWS Systems Manager Patch Manager**  automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows Server, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), CentOS, Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

 

![image](https://media.tutorialsdojo.com/sap_ssm_maintenance_window.png)

 

Hence, the option that says: **Migrate the database to a cluster of EBS-backed Amazon EC2 instances across multiple AZs. Automate the creation of EBS snapshots from EBS volumes of the EC2 instance by using Amazon Data Lifecycle Manager. Install the SSM Agent to the EC2 instance and automate the patch management process using AWS Systems Manager Patch Manager** is correct. Oracle RAC is supported via the deployment using Amazon EC2. AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates.

 

The following options are both incorrect because an Amazon RDS database does not support Oracle RAC:

 

**1. Migrate the database to Amazon RDS which provides a multi-AZ failover feature for your RAC cluster. This will also reduce the RPO and RTO in the event of system failure since RDS offers features such as patch management and maintenance of the underlying host.**

 

**2. Migrate the database to Amazon Aurora and enable automated backups for your Aurora RAC cluster. Patching is automatically handled in Aurora during the system maintenance window**

 

The option that says: **Launch a Lambda function that would automate the creation of snapshots of the database in the EC2 instance. Use the CodeDeploy and CodePipeline service to automate the patch management process of the database**  is incorrect because CodeDeploy and CodePipeline are CI/CD services and are not suitable for patch management. You should use AWS Systems Manager Patch Manager instead.

 

 

**References:**

 

[https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)

 

[https://aws.amazon.com/rds/oracle/faqs/](https://aws.amazon.com/rds/oracle/faqs/)

 

 

**Check out this Amazon RDS Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

---

## Câu 36 — ✅ ĐÚNG

### Câu hỏi

A company is migrating a legacy Oracle database from its on-premises data center to AWS. It will be deployed in an existing Amazon EBS backed Amazon EC2 instance with multiple EBS volumes attached. For the migration, a new volume must be created for the Oracle database and then attached to the instance. This will be used by a financial web application and will primarily store historical financial data that are infrequently accessed. The company is also considering using Amazon GuardDuty to monitor its AWS environment for security threats.



Which of the following is the MOST cost-effective and throughput-oriented solution that the Solutions Architect should implement?

### Các phương án

- **A.** Migrate the database using the AWS Transform MGN and use a General Purpose (gp2) EBS Volume.
- **B.** Migrate the database using the AWS Database Migration Service and use a Provisioned IOPS (io1) EBS volume.
- **C.** Migrate the database using the AWS Transform MGN and use a Throughput Optimized (st1) EBS volume.
- **D.** Migrate the database using the AWS Database Migration Service and use a Cold HDD (sc1) EBS volume.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**AWS Database Migration Service**  helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database.

 

The **AWS Database Migration Service**  can migrate your data to and from the most widely used commercial and open-source databases. AWS Database Migration Service supports homogeneous migrations such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle or Microsoft SQL Server to Amazon Aurora. With AWS Database Migration Service, you can continuously replicate your data with high availability and consolidate databases into a petabyte-scale data warehouse by streaming data to Amazon Redshift and Amazon S3.

 

![image](https://media.tutorialsdojo.com/sap_dms_prep.png)

 

Cold HDD volumes provide low-cost magnetic storage that defines performance in terms of throughput rather than IOPS. With a lower throughput limit than Throughput Optimized HDD, this is a good fit ideal for large, sequential cold-data workloads. If you require infrequent access to your data and are looking to save costs, Cold HDD provides inexpensive block storage. Take note that bootable Cold HDD volumes are not supported.

 

Cold HDD provides the lowest cost HDD volume and is designed for less frequently accessed workloads. Therefore, the correct answer is: **Migrate the database using the AWS Database Migration Service and use a Cold HDD (sc1) EBS volume.**

 

The option that says: **Migrate the database using the AWS Database Migration Service and use a Provisioned IOPS (io1) EBS volume**  is incorrect because it costs more than the Cold HDD and thus, not cost-effective for this scenario. It provides the highest performance SSD volume for mission-critical low-latency or high-throughput workloads, which is not needed in the scenario.

 

The option that says: **Migrate the database using the AWS Transform MGN and use a Throughput Optimized (st1) EBS volume** is incorrect. Although it is cheaper than SSD, it is primarily designed and used for frequently accessed throughput-intensive workloads. Cold HDD perfectly fits the description as it is used for their infrequently accessed data and provides the lowest cost, unlike Throughput Optimized HDD. In addition, the AWS Transform MGN is primarily used to migrate on-premises virtual machines from VMware vSphere, Windows Hyper-V, or Microsoft Azure only. You have to use the AWS Database Migration Service instead in this situation.

 

The option that says: **Migrate the database using the AWS Transform MGN and use a General Purpose (gp2) EBS Volume** is incorrect because a General purpose SSD volume costs more and it is mainly used for a wide variety of workloads. It is recommended to be used as system boot volumes, virtual desktops, low-latency interactive apps, and many more. Moreover, you have to use the AWS Database Migration Service instead in this scenario and not AWS Transform MGN.

 

 

**References:**

 

[https://aws.amazon.com/ebs/details/](https://aws.amazon.com/ebs/details/)

 

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)

 

[https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html)

 

 

**Check out this Amazon EBS Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-ebs/](https://tutorialsdojo.com/amazon-ebs/)

---

## Câu 37 — ✅ ĐÚNG

### Câu hỏi

A company has a team of data analysts that uploads generated data points to an Amazon S3 bucket. The data points are used by other departments, so the objects in this primary S3 bucket need to be replicated to other S3 buckets on several AWS Accounts owned by the company. The company enforces data governance across all its AWS accounts using AWS Audit Manager. The Solutions Architect created an AWS Lambda function that is triggered by S3 PUT events on the primary bucket.



This Lambda function will replicate the newly uploaded object to other destination buckets. Since there will be thousands of object uploads on the primary bucket every day, the company is concerned that this Lambda function may affect other critical Lambda functions because of the regional concurrency limit in Lambda. The replication of the objects does not need to happen in real-time. The team initially considered using provisioned concurrency to guarantee execution capacity, but realized that it was not necessary given the non‑urgent nature of the replication. The company needs to ensure that this Lambda function will not affect the execution of other critical Lambda functions.



Which of the following options will meet the requirements in the LEAST amount of development effort?

### Các phương án

- **A.** Decouple the S3 event notifications and send the events to an Amazon SQS queue in a separate AWS account. Create the new Lambda function on this account, too. Invoke the Lambda function whenever an event message is received in the SQS queue.
- **B.** Implement an exponential backoff algorithm in the new Lambda function to ensure that it will not run if the concurrency limit is reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached.
- **C.** Set the execution timeout of the new Lambda function to 5 minutes. This will allow it to wait for other Lambda function executions to finish in case the concurrency limit is reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached.
- **D.** Configure a reserved concurrency limit for the new function to ensure that its executions will not exceed this limit. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to ensure that the concurrency limit is not being reached.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**Concurrency**  is the number of requests that your function is serving at any given time. When your function is invoked, Lambda allocates an instance of it to process the event. When the function code finishes running, it can handle another request. If the function is invoked again while a request is still being processed, another instance is allocated, which increases the function’s concurrency. Concurrency is subject to a Regional quota that is shared by all functions in a Region.

 

There are two types of concurrency available:

 

**Reserved concurrency**  – Reserved concurrency creates a pool of requests that can only be used by its function, and also prevents its function from using unreserved concurrency.

 

**Provisioned concurrency**  – Provisioned concurrency initializes a requested number of execution environments so that they are prepared to respond to your function’s invocations.

 

In a single account with the default concurrency limit of 1000 concurrent executions, when other services invoke Lambda function concurrently, there is the possibility for two issues to pop up:

 

– One or more of these services could invoke enough functions to consume a majority of the available concurrency capacity. This could cause others to be starved for it, causing failed invocations.

 

– A service could consume too much concurrent capacity and cause a downstream service or database to be overwhelmed, which could cause failed executions.

 

For Lambda functions that are launched in a VPC, you have the potential to consume the available IP addresses in a subnet or the maximum number of elastic network interfaces to which your account has access. One way to solve both of these problems is by applying a concurrency limit to the Lambda functions in an account.

 

You can set a concurrency limit on individual Lambda functions in an account. The concurrency limit that you set reserves a portion of your account-level concurrency for a given function. All of your functions’ concurrent executions count against this account-level limit by default.

 

If you set a concurrency limit for a specific function, then that function’s concurrency limit allocation is deducted from the shared pool and assigned to that specific function. AWS also reserves 100 units of concurrency for all functions that don’t have a specified concurrency limit set. This helps to make sure that future functions have the capacity to be consumed.

 

![image](https://media.tutorialsdojo.com/sap_lambda_concurrency.png)

 

Therefore, the correct answer is: **Configure a reserved concurrency limit for the new function to ensure that its executions will not exceed this limit. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to ensure that the concurrency limit is not being reached.**

 

The option that says: **Set the execution timeout of the new Lambda function to 5 minutes. This will allow it to wait for other Lambda function executions to finish in case the concurrency limit is reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached**  is incorrect. This will still invoke the new Lambda function and cause more problems because, during the wait time, the slice for the Lambda function is still being consumed. Other Lambda functions won’t be able to execute if all slices are consumed.

 

The option that says: **Decouple the S3 event notifications and send the events to an Amazon SQS queue in a separate AWS account. Create the new Lambda function on this account, too. Invoke the Lambda function whenever an event message is received in the SQS queue**  is incorrect. This is possible, and you will have the concurrency limit on the separate AWS account for the new Lambda function. However, this only requires more work and the creation of another AWS account. Setting a concurrency limit is recommended, as it can limit the number of executions of a particular function.

 

The option that says: **Implement an exponential backoff algorithm in the new Lambda function to ensure that it will not run if the concurrency limit is being reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached** is incorrect. This will simply require you to write a backoff algorithm to check the concurrency limit. The function needs to execute in order to run the backoff algorithm, which defeats the purpose of limiting concurrency.

 

 

**References:**

 

[https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)

 

[https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)

 

[https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html)

 

[https://aws.amazon.com/blogs/compute/managing-aws-lambda-function-concurrency/](https://aws.amazon.com/blogs/compute/managing-aws-lambda-function-concurrency/)

 

 

**Check out the AWS Lambda Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-lambda/](https://tutorialsdojo.com/aws-lambda/)

---

## Câu 38 — ✅ ĐÚNG

### Câu hỏi

A call center company uses its custom application to process and store call recordings in its on-premises data center. The recordings are stored on an NFS share. An offshore team is contracted to transcribe about 2% of the call recordings to be used for quality assurance purposes. It could take up to 3 days before the recordings are completely transcribed. The application that processes the calls and manages the transcription queue is hosted on Linux servers. A web portal is available for the quality assurance team to review the call recordings. After 90 days, the recordings are sent to an offsite location for long-term storage. The company plans to migrate the system to the AWS cloud to reduce storage costs and automate the transcription of the recordings.



Which of the following options is the recommended solution to meet the company’s requirements?

### Các phương án

- **A.** Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group. Store all recordings in an Amazon EFS share that is mounted on all instances. After 90 days, archive all call recordings using AWS Backup and use Amazon Transcribe to transcribe the recordings.
- **B.** Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using AWS IQ. Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group.
- **C.** Store all recordings in an Amazon S3 bucket and send the object key to an Amazon SQS queue. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an Auto Scaling group of Amazon EC2 instances to push the recordings to Amazon Translate for transcription. Set the Auto Scaling policy based on the number of objects on the SQS queue. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda.
- **D.** Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using Amazon Transcribe. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**Amazon Transcribe**  is an AWS service that makes it easy for customers to convert speech to text. Using Automatic Speech Recognition (ASR) technology, customers can choose to use Amazon Transcribe for a variety of business applications, including transcription of voice-based customer service calls, generation of subtitles on audio/video content, and conduct (text-based) content analysis on audio/video content.

 

**Amazon Transcribe**  analyzes audio files that contain speech and uses advanced machine-learning techniques to transcribe the voice data into text. You can then use the transcription as you would any text document.

 

Amazon Transcribe uses a deep learning process called automatic speech recognition (ASR) to convert speech to text quickly and accurately. Amazon Transcribe can be used to transcribe customer service calls, automate subtitling, and generate metadata for media assets to create a fully searchable archive. Amazon Transcribe automatically adds speaker diarization, punctuation, and formatting so that the output closely matches the quality of manual transcription at a fraction of the time and expense. Speech-to-text processing can be applied to live audio streams or batch audio content for transcription.

 

To transcribe an audio file, Amazon Transcribe uses three operations:

 

**`StartTranscriptionJob`**  – Starts a batch job to transcribe the speech in an audio file to text.

 

`**ListTranscriptionJobs** ` – Returns a list of transcription jobs that have been started. You can specify the status of the jobs that you want the operation to return. For example, you can get a list of all pending jobs or a list of completed jobs.

 

**`GetTranscriptionJob`**  – Returns the result of a transcription job. The response contains a link to a JSON file containing the results.

 

To manage your objects so that they are stored cost-effectively throughout their lifecycle, configure their Amazon S3 Lifecycle. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. There are two types of actions:

 

**Transition actions** —Define when objects transition to another Using Amazon S3 storage classes. For example, you might choose to transition objects to the S3 Standard-IA storage class 30 days after you created them or archive objects to the S3 Glacier storage class one year after creating them.

 

**Expiration actions** —Define when objects expire. Amazon S3 deletes expired objects on your behalf. The lifecycle expiration costs depend on when you choose to expire objects.

 

![image](https://media.tutorialsdojo.com/sap_step_function_amazon_transcribe.jpg)

 

Therefore, the correct answer is: **Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using Amazon Transcribe. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda.**  Amazon S3 and Glacier offer very cheap object storage for recordings. Amazon Transcribe offers speech-to-text services that can quickly transcribe recordings. Amazon S3, API Gateway, and Lambda are cheap and scalable ways to host the web portal.

 

The option that says: **Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using AWS IQ. Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group**  is incorrect because this AWS IQ is just a freelancing platform that provides hands-on help from AWS experts, and it does not have a feature to automate a transcription job. The correct answer is Amazon Transcribe, where in itis faster in the transcription process, which is a requirement by the company.

 

The option that says: **Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group. Store all recordings in an Amazon EFS share that is mounted on all instances. After 90 days, archive all call recordings using AWS Backup and use Amazon Transcribe to transcribe the recordings** is incorrect because Amazon Transcribe is primarily used to trancribe your recordings and stored on Amazon S3, not on Amazon EFS. Storing the call recordings to Amazon S3 is cheaper compared to Amazon EFS.

 

The option that says: **Store all recordings in an Amazon S3 bucket and send the object key to an Amazon SQS queue. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an Auto Scaling group of Amazon EC2 instances to push the recordings to Amazon Translate for transcription. Set the Auto Scaling policy based on the number of objects on the SQS queue. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda**  is incorrect because Amazon Translate is only a text translation service that uses advanced machine learning technologies to provide high-quality translation on demand. It is not used for transcribing voice messages to text.

 

 

**References:**

 

[https://aws.amazon.com/transcribe/faqs/](https://aws.amazon.com/transcribe/faqs/)

 

[https://docs.aws.amazon.com/transcribe/latest/dg/API_StartTranscriptionJob.html](https://docs.aws.amazon.com/transcribe/latest/dg/API_StartTranscriptionJob.html)

 

[https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html](https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

 

 

**Check out the Amazon Transcribe and Amazon S3 Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-transcribe/](https://tutorialsdojo.com/amazon-transcribe/)

 

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

---

## Câu 39 — ✅ ĐÚNG

### Câu hỏi

A health insurance company has recently adopted a hybrid cloud architecture which connects their on-premises network and their cloud infrastructure in AWS. They have an ELB which has a set of EC2 instances behind them. As the cloud engineer of the company, your manager instructed you to ensure that the SSL key used to encrypt data is always kept secure at all times. In addition, the application logs should only be decrypted by a handful of key users.



In this scenario, which of the following meets all of the requirements?

### Các phương án

- **A.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot. 3. Persist your application server logs to a private S3 bucket using SSE.
- **B.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic. 3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
- **C.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to a private S3 bucket using SSE.
- **D.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**AWS CloudHSM**  is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. With CloudHSM, you can manage your own encryption keys using FIPS 140-2 Level 3 validated HSMs. CloudHSM offers you the flexibility to integrate with your applications using industry-standard APIs, such as PKCS#11, Java Cryptography Extensions (JCE), and Microsoft CryptoNG (CNG) libraries.

 

You can use **AWS CloudHSM to offload SSL/TLS**  processing for your web servers. Using CloudHSM for this processing reduces the burden on your web server and provides extra security by storing your web server’s private key in CloudHSM. Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are used to confirm the identity of web servers and establish secure HTTPS connections over the Internet.

 

![image](https://media.tutorialsdojo.com/sap_hsm_ssl_offload.png)

 

AWS CloudHSM automates time-consuming HSM administrative tasks for you, such as hardware provisioning, software patching, high availability, and backups. You can scale your HSM capacity quickly by adding and removing HSMs from your cluster on-demand. AWS CloudHSM automatically load balances requests and securely duplicates keys stored in any HSM to all of the other HSMs in the cluster.

 

CloudHSM provides a better and more secure way of offloading the SSL processing for the web servers and ensures the application logs are durably and securely stored.

 

In this scenario, the following option is the best choice because it uses CloudHSM and the application server logs are persisted in an S3 bucket with a Server Side Encryption (SSE):

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Configure the ELB to perform TCP load balancing.** 
  **3. Use an AWS CloudHSM instance to perform the SSL transactions.** 
  **4. Persist your application server logs to a private S3 bucket using SSE.**

 

The following sets of options are incorrect because the ephemeral volume is just temporary storage and hence, not a suitable option for durable storage:

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic.** 
  **3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.**

 

as well as this option:

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Configure the ELB to perform TCP load balancing.** 
  **3. Use an AWS CloudHSM instance to perform the SSL transactions.** 
  **4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.**

 

The following option is incorrect because you should never store sensitive private keys in S3:

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot.** 
  **3. Persist your application server logs to a private S3 bucket using SSE.**

 

 

**References:**

 

[https://aws.amazon.com/cloudhsm/](https://aws.amazon.com/cloudhsm/)

 

[https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-overview.html](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-overview.html)

---

## Câu 40 — ✅ ĐÚNG

### Câu hỏi

A company is running 150 virtual machines (VMs) using 40 TB of storage on its on-premises data center. The company wants to migrate its whole environment to AWS within the next three months. The VMs are mainly used during business hours only, so these can be taken offline, but some are mission-critical, which means that the downtime needs to be minimized. Since upgrading the Internet connection is quite costly for the company, the on-premises network administrator provisioned only a 12 Mbps Internet bandwidth for the migration. The Solutions Architect must design a cost-effective plan to complete the migration within the target time frame. The migration team has already installed the AWS Application Discovery Agent on its on‑premises servers to collect performance and dependency data.



Which of the following options should the Solutions Architect implement to fulfill the requirements?

### Các phương án

- **A.** Request a 1 Gbps AWS Direct Connect connection from the on-premises data center to AWS. Create a private virtual interface on Direct Connect. Migrate the virtual machines to AWS using the AWS Transform MGN.
- **B.** Use AWS Transform MGN to migrate the mission‑critical virtual machines to AWS. For the non‑mission‑critical VMs, export them and schedule a reservation with AWS Data Transfer Terminal to upload the data at the facility. Once the VMs are on Amazon S3, import the VMs into Amazon EC2 instances using the VM Import/Export service.
- **C.** Create an export of your virtual machines during out of office hours. Use the AWS Transfer service to securely upload the VMs to Amazon S3 using the SFTP protocol. Import the VMs into Amazon EC2 instances using the VM Import/Export service.
- **D.** Deploy the AWS Agentless Discovery connector on the company VMware vCenter to assess each application. With the information gathered, refactor each application to run on AWS services or using AWS Marketplace solutions.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**AWS Transform MGN (MGN)**  is an automated lift-and-shift solution that simplifies and speeds up the migration of applications to AWS, reducing costs. It enables businesses to move physical, virtual, or cloud servers without compatibility issues or performance disruptions. MGN replicates source servers to AWS and automatically launches them, allowing immediate benefits from cloud agility and cost savings. After migration, companies can easily replatform or refactor their applications using AWS services for faster modernization.

 

![image](https://media.tutorialsdojo.com/public/AWS Transform MGN-08JUN2026.png)

 

The **AWS Data Transfer Terminal**  is a network-ready, physical facility where you can bring your data storage devices for quick transfers to and from AWS Cloud services. This service allows you to upload data collected remotely, making it easier to access that information.

 

![image](https://media.tutorialsdojo.com/public/Data Transfer Terminal-08JUN2026.png)

 

To use the Data Transfer Terminal, schedule a reservation at one of the facilities through the AWS Management Console. Arrive at your scheduled time and upload your data to your AWS Cloud services using your devices. Once your reservation is complete and you leave the facility, it will be re-secured and prepared for the next scheduled appointment.

 

AWS**VM Import/Export**  enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances and export them back to your on-premises environment. VM Import/Export is available at no additional charge beyond standard usage charges for Amazon EC2 and Amazon S3. As part of the import process, VM Import will convert your VM into an Amazon EC2 AMI, which you can use to run Amazon EC2 instances.

 

Therefore, the correct answer is: **Use AWS Transform MGN to migrate the mission‑critical virtual machines to AWS. For the non‑mission‑critical VMs, export them and schedule a reservation with AWS Data Transfer Terminal to upload the data at the facility. Once the VMs are on Amazon S3, import the VMs into Amazon EC2 instances using the VM Import/Export service.**  AWS Transform MGN minimizes downtime for mission‑critical workloads, while AWS Data Transfer Terminal provides a cost‑effective offline transfer solution for the bulk 40 TB dataset. This offline transfer is necessary to meet the requirement since the available Internet bandwidth is only 12 Mbps, which would otherwise make the migration impossible within the three‑month timeframe. This hybrid approach meets the deadline and balances both cost and downtime requirements.

 

The option that says: **Request a 1 Gbps AWS Direct Connect connection from the on-premises data center to AWS. Create a private virtual interface on Direct Connect. Migrate the virtual machines to AWS using the AWS Transform MGN**  is incorrect. Although this is a fast solution that can typically finish the migration within the required time frame, it is not the most cost-effective solution. As stated in the question, upgrading the Internet connection (and probably requesting a new connection) is costly for the company. Moreover, the requirement is to migrate to virtual machines and not to establish a fast, dedicated network connection from the on-premises network to AWS.

 

The option that says: **Deploy the AWS Agentless Discovery connector on the company VMware vCenter to assess each application. With the information gathered, refactor each application to run on AWS services or using AWS Marketplace solutions**  is incorrect. This requires a lot of effort for planning since you will have to match each application to the AWS service. This will just require changes in the application and can cause possible interruptions during the migration.

 

The option that says:**Create an export of your virtual machines during out of office hours. Use the AWS Transfer service to securely upload the VMs to Amazon S3 using the SFTP protocol. Import the VMs into Amazon EC2 instances using the VM Import/Export service**  is incorrect. Although this is possible, with the 12 Mbps Internet connection, it will take more than three months to upload all the 40 TB worth of VM storage to an Amazon S3 bucket.

 

 

**References:**

 

[https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html)

 

[https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)

 

[https://aws.amazon.com/ec2/vm-import/](https://aws.amazon.com/ec2/vm-import/)

 

 

**Check out these AWS Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-cheat-sheets/](https://tutorialsdojo.com/aws-cheat-sheets/)

---

## Câu 41 — ✅ ĐÚNG

### Câu hỏi

A company is planning to launch a mobile app for the Department of Transportation that allows government staff to upload the latest photos of ongoing construction works such as bridges, roads culverts, and dams all over the country. The mobile app should send the photos to a web server hosted on an EC2 instance which then adds a watermark to each photo that contains the project details and the date it was taken. The solutions architect must design a solution in which the photos generated by the server will be uploaded to an S3 bucket for durable storage.



Which of the following solutions is a secure architecture and allows the EC2 instance to upload photos to S3?

### Các phương án

- **A.** Set up an IAM user with permissions to list and write objects to the S3 bucket. Launch the instance as the IAM user which will enable the EC2 instance to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket.
- **B.** Set up a service control policy (SCP) with permissions to list and write objects to the S3 bucket. Attach the SCP to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket.
- **C.** Set up an IAM service role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket.
- **D.** Set up an IAM role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

This question tests your understanding of IAM, specifically on when to use an IAM Role over an SCP. Since the server is running on an EC2 instance and the application makes requests to S3 to store the photos, the more suitable option to use here is an IAM Role.

 

![image](https://media.tutorialsdojo.com/sap_scp_organization.jpg)

 

In addition, don’t create an IAM user and pass the user’s credentials to the application or embed the credentials in the application. That will create a security risk because if an attacker had unauthorized access to that EC2 instance then the user credentials can easily be acquired and exploited. The better way is to create an IAM role that you can attach to the EC2 instance to give applications running on the instance temporary security credentials which can be used to access other AWS resources such as an S3 bucket. The credentials have the permissions specified in the policies attached to the role.

 

The option that says: **Set up an IAM role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket**  is correct as it uses an IAM Role and fetches the temporary security credentials from the instance metadata.

 

The option that says: **Set up a service control policy (SCP) with permissions to list and write objects to the S3 bucket. Attach the SCP to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket**  is incorrect as SCPs simply enable you to restrict, at the account level of granularity, what services and actions the users, groups, and roles in those accounts can do. SCPs don’t grant permissions to any user or role because this is handled through IAM policies.

 

The option that says: **Set up an IAM user with permissions to list and write objects to the S3 bucket. Launch the instance as the IAM user which will enable the EC2 instance to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket**  is incorrect as an IAM Role is a better option to use instead of an IAM User. Plus, you should always retrieve the temporary security credentials from the instance metadata and not from the user data.

 

The option that says: **Set up an IAM service role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket**  is incorrect because although it uses an IAM Role, the temporary security credentials should be retrieved from the instance metadata and not from the user data.

 

 

**References:**

 

[https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-service-control-policy/](https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-service-control-policy/)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-roles)

 

 

**Check out this AWS IAM Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

 

 

**Here is a deep dive on IAM Policies:**

 

[https://youtu.be/YQsK4MtsELU](https://youtu.be/YQsK4MtsELU)

---

## Câu 42 — ❌ SAI

### Câu hỏi

A company is using Microsoft Active Directory to manage all employee accounts and devices. The IT department instructed the solutions architect to implement a single sign-on feature to allow the employees to use their existing Windows account password to connect and use the various AWS resources.



Which of the following options is the recommended way to extend the current Active Directory domain to AWS?

### Các phương án

- **A.** Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.
- **B.** Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts.
- **C.** Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps' backend resources in AWS.
- **D.** Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account.

> **Bạn chọn:** B
> **Đáp án đúng:** A

### Giải thích

Incorrect  

Because the company is using Microsoft Active Directory already, you can use **AWS Directory Service for Microsoft AD**  to create secure Windows trusts between your on-premises Microsoft Active Directory domains and your AWS Microsoft AD domain in the AWS Cloud. By setting up a trust relationship, you can integrate SSO to the AWS Management Console and the AWS Command Line Interface (CLI), as well as your Windows-based workloads.

 

![image](https://media.tutorialsdojo.com/sap_aws_directory_service.png)

 

**AWS Directory Service**  helps you to set up and run a standalone AWS Managed Microsoft AD directory hosted in the AWS Cloud. You can also use AWS Directory Service to connect your AWS resources with an existing on-premises Microsoft Active Directory. To configure AWS Directory Service to work with your on-premises Active Directory, you must first set up trust relationships to extend authentication from on-premises to the cloud.

 

Therefore, the correct answer is: **Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.**

 

The option that says: **Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps’ backend resources in AWS**  is incorrect because Cognito is primarily used for federation to your web and mobile apps running on AWS. It allows you to authenticate users through social identity providers. But since the company is already using Microsoft AD, AWS Directory Service is the better choice here.

 

The option that says: **Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts**  is incorrect because using the AWS IAM Identity Center service alone is not enough to meet the requirement. Although it can help you manage SSO access and user permissions across all your AWS accounts in AWS Organizations, you still have to use the AWS Directory Service to integrate your on-premises Microsoft AD. AWS IAM Identity Center integrates with Microsoft AD using AWS Directory Service so there is no need to create users and groups.

 

The option that says: **Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account**  is incorrect because setting up cross-account access allows you to share resources in one AWS account with users in a different AWS account. Since the company is already using Microsoft AD then, the better choice to use here is the AWS Directory Service.

 

 

**References:**

 

[https://aws.amazon.com/directoryservice/](https://aws.amazon.com/directoryservice/ )

 

[https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-directory-connected.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-directory-connected.html)

 

 

**Check out this AWS Directory Service Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-directory-service/](https://tutorialsdojo.com/aws-directory-service/)

---

## Câu 43 — ✅ ĐÚNG

### Câu hỏi

A leading media company is building a collaborative news website that is expected to have over 5 million readers per month globally. Each article contains a cover image and has at least 200 words. Based on the trend of their other websites, the new articles are highly browsed in the first 2 months and the authors tend to frequently update the articles on the first month after its publication. The readership is also expected to drop on the 3rd month and the articles are usually rarely accessed after a year. The readers are also leaving a lot of comments within the first 3 months of publishing.



In this scenario, which of the following items can you use to build a durable, highly available, and scalable architecture for the news website? (Select TWO.)

### Các phương án

- **A.** Use Amazon RDS Multi-AZ deployments with Read Replicas. Use S3 to store the static data such as the cover images and other media.
- **B.** Use CloudFront as a Content Delivery Network to load the articles much faster anywhere in the globe.
- **C.** Launch an RDS Oracle Real Application Clusters (RAC) with Read Replicas.
- **D.** Use Lambda with Auto-Healing enabled.
- **E.** Use EBS Volumes in RAID 0 configuration to store the static data such as the cover images and other media.

> **Bạn chọn:** A, B
> **Đáp án đúng:** A, B

### Giải thích

Correct 

In this scenario, the main objective is to provide a durable, highly-available and scalable architecture for the website. You can use CloudFront as a CDN, then Amazon RDS with Multi-AZ deployments and Read Replicas to provide scalability and high-availability for the millions of incoming traffic every month. Lastly, you can use an S3 bucket to durably store the images and other static media content of the website.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_ssl.jpg)

 

Therefore, the correct answer is: **Use CloudFront as a Content Delivery Network to load the articles much faster anywhere in the globe** and **Use Amazon RDS Multi-AZ deployments with Read Replicas. Use S3 to store the static data such as the cover images and other media** .

 

The option that says: **Launch an RDS Oracle Real Application Clusters (RAC) with Read Replicas**  is incorrect because Oracle RAC is not supported in RDS.

 

The option that says: **Use Lambda with Auto-Healing enabled** is incorrect. AWS Lambda is serverless and it does not have Auto-Healing option since functions are event-driven.

 

The option that says: **Use EBS Volumes in RAID 0 configuration to store the static data such as the cover images and other media** is incorrect because EBS Volumes are not as durable and not as scalable compared with S3, even with a RAID 1 (mirroring) configuration.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html )

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

 

[https://aws.amazon.com/s3/](https://aws.amazon.com/s3/)

 

 

**Check out these Amazon RDS and Amazon S3 Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

 

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

---

## Câu 44 — ✅ ĐÚNG

### Câu hỏi

A telecommunications company has several Amazon EC2 instances inside an AWS VPC. To improve data leak protection, the company wants to restrict the internet connectivity of its EC2 instances. The EC2 instances that are launched on a public subnet should be able to access product updates and patches from the Internet. The packages are accessible through the third-party provider via their URLs. The company wants to explicitly deny any other outbound connections from the VPC instances to hosts on the Internet.



Which of the following options would the solutions architect consider implementing to meet the company requirements?

### Các phương án

- **A.** You can use a forward web proxy server in your VPC and manage outbound access using URL-based rules. Default routes are also removed.
- **B.** Use network ACL rules that allow network access to your specific package destinations. Add an implicit deny for all other cases.
- **C.** Create security groups with the appropriate outbound access rules that will let you retrieve software packages from the Internet.
- **D.** Move all instances from the public subnets to the private subnets. Additionally, remove the default routes from your routing tables and replace them instead with routes that specify your package locations.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

A forward proxy server acts as an intermediary for requests from internal users and servers, often caching content to speed up subsequent requests. Companies usually implement proxy solutions to provide URL and web content filtering, IDS/IPS, data loss prevention, monitoring, and advanced threat protection. AWS customers often use a VPN or AWS Direct Connect connection to leverage existing corporate proxy server infrastructure, or build a forward proxy farm on AWS using software such as Squid proxy servers with internal Elastic Load Balancing (ELB).

 

You can limit outbound web connections from your VPC to the internet, using a web proxy (such as a squid server) with custom domain whitelists or DNS content filtering services. The solution is scalable, highly available, and deploys in a fully automated way.

 

![image](https://media.tutorialsdojo.com/sap_squid_proxy.jpg)

 

Therefore, the correct answer is: **You can use a forward web proxy server in your VPC and manage outbound access using URL-based rules. Default routes are also removed.**  A proxy server filters requests from the client, and allows only those that are related to the product updates, and in this case helps filter all other requests except the ones for the product updates.

 

The option that says: **Move all instances from the public subnets to the private subnets. Additionally, remove the default routes from your routing tables and replace them instead with routes that specify your package locations**  is incorrect. Even though moving the instances in a private subnet is a good idea, the routing table does not have the filtering logic. It only connects the subnets with Internet gateway.

 

The option that says: **Using network ACL rules that allow network access to your specific package destinations then adding an implicit deny for all other cases**  is incorrect. NACLs cannot filter requests based on URLs.

 

The option that says: **Creating security groups with the appropriate outbound access rules that will let you retrieve software packages from the Internet**  is incorrect. A security group cannot filter requests based on URLs.

 

 

**References** :

 

[https://docs.aws.amazon.com/cli/latest/userguide/cli-http-proxy.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-http-proxy.html)

 

[https://aws.amazon.com/blogs/security/how-to-set-up-an-outbound-vpc-proxy-with-domain-whitelisting-and-content-filtering/](https://aws.amazon.com/blogs/security/how-to-set-up-an-outbound-vpc-proxy-with-domain-whitelisting-and-content-filtering/)

 

 

**Check out this Amazon VPC Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

---

## Câu 45 — ❌ SAI

### Câu hỏi

A software development company implements cloud best practices on its AWS infrastructure. The solutions architect has been instructed to manage its AWS cloud Infrastructure as code (IAC) to automate its software build, test, and deploy process. The company follows a continuous integration and continuous delivery (CI/CD) practice to streamline its software development lifecycle. The company already uses AWS CodeArtifact to store and version its private software packages.



The company would like to have the ability to easily deploy exact copies of different versions of its cloud infrastructure, stage changes into different environments, revert back to previous versions, and identify the specific versions running in the VPC. Plus, all new public-facing applications should also have a global content delivery network (CDN) service.



Which of the following options is the recommended action to meet the company requirement?

### Các phương án

- **A.** Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.
- **B.** Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.
- **C.** Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.
- **D.** Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture.

> **Bạn chọn:** C
> **Đáp án đúng:** B

### Giải thích

Incorrect  

**AWS CloudFormation**  provides a common language for you to describe and provision all the infrastructure resources in your cloud environment. CloudFormation allows you to use a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This file serves as the single source of truth for your cloud environment.

 

![image](https://media.tutorialsdojo.com/public/td-aws-cloudformation-diagram-1April2026.png)

 

**Amazon CloudFront**  is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the user is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

 

Therefore, the correct answer is: **Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.**

 

The option that says: **Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture**  is incorrect. CloudWatch is typically not a CDN service.

 

The option that says: **Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture**  is incorrect. As with the case above, CloudWatch is not a CDN service.

 

The option that says: **Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture**  is incorrect. Even though Elastic Beanstalk enables you to quickly deploy and manage applications in the AWS Cloud, you still can’t manage the cloud infrastructure as application code with it. The best option is simply to use CloudFormation.

 

 

**References:**

 

[https://aws.amazon.com/cloudformation/](https://aws.amazon.com/cloudformation/ )

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

 

 

**Check out this AWS CloudFormation Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

 

 

**Elastic Beanstalk vs CloudFormation vs OpsWorks vs CodeDeploy:**

 

[https://tutorialsdojo.com/elastic-beanstalk-vs-cloudformation-vs-opsworks-vs-codedeploy/](https://tutorialsdojo.com/elastic-beanstalk-vs-cloudformation-vs-opsworks-vs-codedeploy/)

 

 

**Comparison of AWS Services Cheat Sheets:**

 

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

---

## Câu 46 — ✅ ĐÚNG

### Câu hỏi

An advertising company plans to release a new photo-sharing app that will be hosted on the AWS Cloud. The app will store all pictures directly uploaded by users in a single Amazon S3 bucket, and users will also be able to view and download uploaded pictures directly from the S3 bucket. The company uses Amazon Fraud Detector to identify and prevent fraudulent account registrations and suspicious user activities at scale. The development team also uses AWS Device Farm to test the application on a wide range of real mobile devices before launch.



The solutions architect must ensure the security of the application, and it should be able to handle potentially millions of users in the most secure manner.



How should the solutions architect set up the user registration flow in AWS for this mobile app?

### Các phương án

- **A.** Create an IAM user, assign appropriate permissions to it, and generate an access key and a secret key that will be stored in the mobile app and used to access S3.
- **B.** Create an IAM user and generate an access key and a secret key to be stored in the mobile app for the IAM user. After applying the appropriate permissions to the S3 bucket policy, use the generated credentials to access S3.
- **C.** Generate long-term credentials using AWS STS and apply the appropriate permissions. Store the credentials in the mobile app, and use them to access S3.
- **D.** Store user information in Amazon RDS and create an IAM Role with appropriate permissions. Generate new temporary credentials using the AWS Security Token Service `AssumeRole` function each time the user opens the mobile app. These credentials will be stored in the mobile app’s memory and will be used to access S3.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

In this scenario, the best solution is to use a combination of an IAM Role and STS for authentication. The STS `AssumeRole` returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use AssumeRole for cross-account access or federation.

 

![image](https://media.tutorialsdojo.com/public/td-sts-token-diagram-1April2026.png)

 

Therefore, the correct answer is: **Store user information in Amazon RDS and create an IAM Role with appropriate permissions. Generate new temporary credentials using the AWS Security Token Service `AssumeRole` function each time the user opens the mobile app. These credentials will be stored in the mobile app’s memory and will be used to access S3.**  It creates an IAM Role with appropriate permissions and then generates temporary security credentials using STS `AssumeRole`. Then, it generates new credentials when the user runs the app the next time.

 

The option that says: **Create an IAM user and generate an access key and a secret key to be stored in the mobile app for the IAM user. After applying the appropriate permissions to the S3 bucket policy, use the generated credentials to access S3**  is incorrect. It simply suggests creating an IAM User, not the IAM Role, which is not a good solution. You should create an IAM Role so that the app can access the AWS Resource using STS AssumeRole.

 

The option that says: **Generate long-term credentials using AWS STS and apply the appropriate permissions. Store the credentials in the mobile app, and use them to access S3**  is incorrect. You should always grant short-term or temporary credentials for the mobile application. This option recommends creating long-term credentials.

 

The option that says: **Create an IAM user, assign appropriate permissions to it, and generate an access key and a secret key that will be stored in the mobile app and used to access S3**  is incorrect. It typically does not create the required IAM Role, but instead, an IAM user.

 

 

**References:**

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

 

[https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

 

 

**Check out this AWS IAM Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 47 — ✅ ĐÚNG

### Câu hỏi

A company is planning to migrate its workload to the AWS cloud. The solutions architect is looking to reduce the amount of time spent managing database instances from the on-premises data center by migrating to a managed relational database service in AWS such as Amazon Relational Database Service (RDS). In addition, the solutions architect plans to move the application hosted in the on-premises data center to a fully managed platform such as AWS Elastic Beanstalk.



Which of the following is the most cost-effective migration strategy that should be implemented to meet the above requirement?

### Các phương án

- **A.** Rehost
- **B.** Replatform
- **C.** Refactor / Re-architect
- **D.** Repurchase

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**Organizations**  usually begin to think about how they will migrate an application during Phase 2 (*Portfolio Discovery and Planning* ) of the migration process. This is when you determine what is in your environment and the migration strategy for each application. The six approaches detailed below are common migration strategies employed and build upon “The 5 R’s” that Gartner Inc, a global research and advisory firm, outlined in 2011.

 

You should gain a thorough understanding of which migration strategy will be best suited for certain portions of your portfolio. It is also important to consider that while one of the six strategies may be best for migrating certain applications in a given portfolio, another strategy might work better for moving different applications in the same portfolio.

 

![image](https://media.tutorialsdojo.com/sap_migration_paths.png)

 

**1. Rehost (“lift and shift”)**  – In a large legacy migration scenario where the organization is looking to quickly implement its migration and scale to meet a business case, we find that the majority of applications are rehosted.

 

**2. Replatform (“lift, tinker and shift”)** – This entails making a few cloud optimizations in order to achieve some tangible benefit without changing the core architecture of the application.

 

**3. Repurchase (“drop and shop”)** – This is a decision to move to a different product and likely means your organization is willing to change the existing licensing model you have been using. For workloads that can easily be upgraded to newer versions, this strategy might allow a feature set upgrade and smoother implementation.

 

**4. Refactor / Re-architect** – Typically, this is driven by a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment.

 

**5. Retire** – Identifying IT assets that are no longer useful and can be turned off will help boost your business case and direct your attention towards maintaining the resources that are widely used.

 

**6. Retain**  – You may want to retain portions of your IT portfolio because there are some applications that you are not ready to migrate and feel more comfortable keeping them on-premises, or you are not ready to prioritize an application that was recently upgraded and then make changes to it again.

 

Therefore, the correct answer is: **Replatform.** This strategy is done by making a few cloud optimizations on your existing systems before migrating them to AWS, which is what will happen if you move your existing database and web applications to AWS. This strategy is more suitable when you want to reduce the amount of time you spend managing database instances by migrating to a managed relational database service such as Amazon Relational Database Service (RDS), or migrating your application to a fully managed platform like AWS Elastic Beanstalk.

 

**Rehost**  is incorrect. Rehost (“lift and shift”) strategy is more suitable for quickly migrating the systems to AWS to meet a certain business case without no additional configuration involved. Take note that if you migrate your systems to either Elastic Beanstalk or RDS, you will still need to set up, configure, and test your systems, which takes additional time and effort.

 

**Repurchase**  is incorrect. This strategy entails a decision to move to a different product and likely means your organization is willing to change the existing licensing model you have been using. Hence, this is not a suitable migration strategy for this scenario.

 

**Refactor / Re-architect**  is incorrect. This strategy is suitable if there is a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment. This type of migration strategy also entails additional cost, compared with the Replatform strategy, since you are allocating time, effort, and budget to optimize your systems.

 

 

**References:**

 

[https://aws.amazon.com/cloud-migration/](https://aws.amazon.com/cloud-migration/)

 

[https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/)

 

[https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/planning-phase.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/planning-phase.html)

 

 

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

 

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 48 — ✅ ĐÚNG

### Câu hỏi

A company that manages hundreds of AWS client accounts has created a central logging service running on an Auto Scaling group of Amazon EC2 instances. The logging service receives logs from the client AWS accounts through the connectivity provided by AWS PrivateLink. The interface endpoint for this is available on each of the client AWS accounts. The EC2 instances hosting the logging service are spread on multiple subnets with a Network Load Balancer in front to spread the incoming load. Upon testing, the clients are unable to submit logs through the VPC endpoint.



Which of the following solutions will most likely resolve the issue? (Select TWO.)

### Các phương án

- **A.** Ensure that the NACL associated with the logging service subnet allows communication to and from the NLB subnets. Ensure that the NACL associated with the NLB subnets allows communication to and from the EC2 instances subnets running the logging service.
- **B.** Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the IP address block of the clients.
- **C.** Ensure that the Auto Scaling group is associated with a launch template that includes the latest Amazon Machine Image (AMI) and that the EC2 instances are using instance types that are optimized for log processing.
- **D.** Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the NLB’s security group. Also, ensure that the security group attached to the NLB allows inbound traffic from the interface endpoint subnet.
- **E.** Ensure that the NACL associated with the logging service subnets allows communication to and from the interface endpoint. Ensure that the NACL associated with the interface endpoint subnet allows communication to and from the EC2 instances running the logging service.

> **Bạn chọn:** A, D
> **Đáp án đúng:** A, D

### Giải thích

Correct 

When you create an Amazon VPC endpoint interface with **AWS PrivateLink** , an Elastic Network Interface is created inside of the subnet that you specify. This interface VPC endpoint (interface endpoint) inherits the network ACL of the associated subnet. You must associate a security group with the interface endpoint to protect incoming and outgoing requests.

 

![image](https://media.tutorialsdojo.com/sap_privatelink_vpc_endpoint.png)

 

When you associate a Network Load Balancer with an endpoint service, the Network Load Balancer forwards requests to the registered target as if the target was registered by IP address. In this case, the source IP addresses are the private IP addresses of the load balancer nodes. If you have access to the Amazon VPC endpoint service, you must verify that the security group rules and the rules within the network ACL associated with the Network Load Balancer’s targets:

 

– Allow communication from the private IP address of the Network Load Balancer.

 

– Don’t allow communication from the IP address of the client or the interface endpoint.

 

To allow communication between clients and the Amazon VPC endpoint, you must create rules within the network ACL associated with the client’s subnet and the subnet associated with the interface endpoint. Be aware of this limit:

 

– You cannot use the security groups for clients as a source in the security groups for the targets. Instead, use the client CIDR blocks as sources in the target security groups.

 

If you register targets by IP address and do not want to grant access to the entire VPC CIDR, you can grant access to the private IP addresses used by the load balancer nodes. There is one IP address per load balancer subnet.

 

Therefore, the correct answer are:

 

**– Ensure that the NACL associated with the logging service subnet allows communication to and from the NLB subnets. Ensure that the NACL associated with the NLB subnets allows communication to and from the EC2 instances subnets running the logging service.**

 

**– Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the NLB’s security group. Also, ensure that the security group attached to the NLB allows inbound traffic from the interface endpoint subnet.**

 

The option that says: **Ensure that the NACL associated with the logging service subnets allows communication to and from the interface endpoint. Ensure that the NACL associated with the interface endpoint subnet allows communication to and from the EC2 instances running the logging service**  is incorrect because the rules within the network ACL associated with the Network Load Balancer’s targets should not allow direct communication from the IP address of the client or the interface endpoint. A better approach is to ensure that the NACL associated with the NLB subnets allows communication to and from the EC2 instances subnets running the logging service.

 

The option that says: **Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the IP address block of the clients**  is incorrect because the security group attached to the EC2 instances must permit the inbound traffic from the NLB subnet IPs and not the IP address block of the clients. The security group rules associated with the Network Load Balancer’s targets should not allow direct access from the IP address of the client or the interface endpoint.

 

The option that says: **Ensure that the Auto Scaling group is associated with a launch template that includes the latest Amazon Machine Image (AMI) and that the EC2 instances are using instance types that are optimized for log processing**  is incorrect because the issue described in the scenario is more likely related to connectivity, not the configuration of the EC2 instances. Therefore, while it’s generally good practice to use the latest AMI and appropriate instance types, this may not resolve the specific issue in the scenario. The most likely solutions involve checking the security groups of the interface endpoints and ensuring the Network Load Balancer is correctly configured.

 

 

**References:**

 

[https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-troubleshooting.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-troubleshooting.html)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/security-network-acl-vpc-endpoint/](https://aws.amazon.com/premiumsupport/knowledge-center/security-network-acl-vpc-endpoint/)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/security-group-load-balancer/](https://aws.amazon.com/premiumsupport/knowledge-center/security-group-load-balancer/)

 

[https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html#target-security-groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html#target-security-groups)

 

 

**Application Load Balancer vs Network Load Balancer vs Classic Load Balancer:**

 

[https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-classic-load-balancer/](https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-classic-load-balancer/)

---

## Câu 49 — ✅ ĐÚNG

### Câu hỏi

A leading call center company has its headquarters in Seattle. Its corporate web portal is deployed to AWS. The AWS cloud resources are linked to its corporate data center via a link aggregation group (LAG), which terminates at the same AWS Direct Connect endpoint and is connected on a private virtual interface (VIF) in your VPC. The portal must authenticate against their on-premises LDAP server. Each Amazon S3 bucket can only be accessed by a logged-in user if it belongs to that user.



Which of the following options should the solutions architect implement in AWS to meet the company requirements? (Select TWO.)

### Các phương án

- **A.** Create an identity broker that assumes an IAM role, and retrieve temporary AWS security credentials via IAM Security Token Service (STS). The application gets the AWS temporary security credentials from the identity broker to gain access to the appropriate S3 bucket.
- **B.** Use a Direct Connect Gateway instead of a single Direct Connect connection. Set up a Transit VPC which will authenticate against their on-premises LDAP server.
- **C.** The application first authenticates against LDAP to retrieve the name of an IAM role associated with the user. It then assumes that role via a call to IAM Security Token Service (STS). Afterward, the application can now use the temporary credentials from the role to access the appropriate S3 bucket.
- **D.** The application first authenticates against LDAP, and then uses the LDAP credentials to log in to IAM service. Finally, it can now use the IAM temporary credentials to access the appropriate S3 bucket.
- **E.** Authenticate against LDAP using an identity broker you created, and have it call IAM Security Token Service (STS) to retrieve IAM federated user credentials. The application then gets the IAM federated user credentials from the identity broker to access the appropriate S3 bucket.

> **Bạn chọn:** C, E
> **Đáp án đúng:** C, E

### Giải thích

Correct 

**Lightweight Directory Access Protocol (LDAP)**  is a standard communications protocol used to read and write data to and from Active Directory. You can manage your user identities in an external system outside of AWS and grant users who sign in from those systems access to perform AWS tasks and access your AWS resources. The distinction is where the external system resides—in your data center or an external third party on the web.

 

For enterprise **identity federation** , you can authenticate users in your organization’s network, and then provide those users access to AWS without creating new AWS identities for them and requiring them to sign in with a separate user name and password. This is known as the single sign-on (SSO) approach to temporary access. AWS STS supports open standards like Security Assertion Markup Language (SAML) 2.0, with which you can use Microsoft AD FS to leverage your Microsoft Active Directory.

 

![image](https://media.tutorialsdojo.com/sap_sso_ldap_broker.png)

 

This scenario has the following attributes:

 

– The identity broker application has permissions to access IAM’s token service (STS) API to create temporary security credentials.

 

– The identity broker application is able to verify that employees are authenticated within the existing authentication system.

 

– Users are able to get a temporary URL that gives them access to the AWS Management Console (which is referred to as single sign-on).

 

The option that says: **Authenticate against LDAP using an identity broker you created, and have it call IAM Security Token Service (STS) to retrieve IAM federated user credentials. The application then gets the IAM federated user credentials from the identity broker to access the appropriate S3 bucket**  is correct because it follows the correct sequence. It develops an identity broker that authenticates users against LDAP, gets the security token from STS, and then accesses the S3 bucket using the IAM federated user credentials.

 

Likewise, the option that says:**The application first authenticates against LDAP to retrieve the name of an IAM role associated with the user. It then assumes that role via call to IAM Security Token Service (STS). Afterwards, the application can now use the temporary credentials from the role to access the appropriate S3 bucket**  is correct because it follows the correct sequence. It authenticates users using LDAP, gets the security token from STS, and then accesses the S3 bucket using the temporary credentials.

 

The option that says: **Create an identity broker that assumes an IAM role, and retrieve temporary AWS security credentials via IAM Security Token Service (STS). The application gets the AWS temporary security credentials from the identity broker to gain access to the appropriate S3 bucket**  is incorrect because the users need to be authenticated using LDAP first, not STS. Also, the temporary credentials to log into AWS are provided by STS, not identity broker.

 

The option that says: **The application first authenticates against LDAP, and then uses the LDAP credentials to log in to IAM service. Finally, it can now use the IAM temporary credentials to access the appropriate S3 bucket**  is incorrect because you cannot use the LDAP credentials to log into IAM.

 

The option that says: **Use a Direct Connect Gateway instead of a single Direct Connect connection. Set up a Transit VPC which will authenticate against their on-premises LDAP server**  is incorrect because using a Direct Connect Gateway will only improve the availability of your on-premises network connection and using a transit VPC is just a common strategy for connecting multiple, geographically disperse VPCs and remote networks in order to create a global network transit center. These two things will not meet the requirement.

 

 

**References** :

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html)

 

 

**Check out this AWS IAM Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 50 — ✅ ĐÚNG

### Câu hỏi

A company has three AWS accounts each with its own VPCs. There is a requirement for communication between the AWS resources across the accounts, so VPC peering needs to be configured. Please refer to the figure below for details of each VPC:



![image](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20419'%3E%3C/svg%3E)



VPC-B and VPC-C have matching CIDR blocks. For a short-term requirement, VPC-A needs to communicate only with the database instance in VPC-B with an IP address of `10.0.0.77/32` while being able to communicate with all the resources in VPC-C. The Solutions Architect already created the necessary VPC peering links but VPC-A cannot effectively communicate to the VPC-B instance. The Solutions Architect suspects that the routes on each VPC still need proper configuration.



Which of the following solutions will allow VPC-A to communicate with the database instance in VPC-B while being able to communicate with all resources on VPC-C?

### Các phương án

- **A.** Enable dynamic route propagation in VPC-A with the peering targets `pcx-aaaabbbb` and `pcx-aaaacccc` respectively. On VPC-B, enable dynamic route propagation with peering target `pcx-aaaabbbb` and add a network acces control list (NACL) that allows only connections to IP address `10.0.0.77/32` from `pcx-aaaabbbb`. On VPC-C, enable dynamic route propagation with the peering target `pcx-aaaacccc`.
- **B.** On VPC-A, add a static route for VPC-B CIDR (`10.0.0.0/24`) with the target `pcx-aaaabbbb` and another static route for VPC-C CIDR (`10.0.0.0/16`) with the target `pcx-aaaacccc`. On VPC-B, add a static route for VPC-A CIDR (`172.16.0.0/24`) with the target `pcx-aaaabbbb`. On VPC-C, add a static route for VPC-A CIDR (`172.16.0.0/24`) with the target `pcx-aaaacccc`.
- **C.** On VPC-A, add a static route for VPC-B CIDR (`10.0.0.77/32`) with the target `pcx-aaaabbbb` and another static route for VPC-C CIDR (`10.0.0.0/16`) with the target` pcx-aaaacccc`. On VPC-B, add a static route for VPC-A CIDR (`172.16.0.0/16`) with the target `pcx-aaaabbbb`. On VPC-C, add a static route for VPC-A CIDR (`172.16.0.0/16`) with the target `pcx-aaaacccc`.
- **D.** On VPC-A, add a static route for VPC-B CIDR (`10.0.0.0/24`) with the target `pcx-aaaabbbb` and another static route for VPC-C CIDR (`10.0.0.0/24`) with the target `pcx-aaaacccc`. Add a network access control list (NACL) on VPC-A to deny all connections to VPC-B except for the IP address `10.0.0.77/32`. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target `pcx-aaaabbbb`. On VPC-C, add a static route for VPC-A CIDR (`172.16.0.0/24`) with the target `pcx-aaaacccc`.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

You can configure **VPC peering connections**  to provide access to part of the CIDR block, a specific CIDR block (if the VPC has multiple CIDR blocks), or a specific instance within the peer VPC. In this scenario, a central VPC is peered to two or more VPCs that have overlapping CIDR blocks.

 

You have a central VPC (VPC A) with one subnet, and you have a VPC peering connection between VPC A and VPC B (`pcx-aaaabbbb`), and between VPC A and VPC C (`pcx-aaaacccc`). VPC B and VPC C have matching CIDR blocks. You want to use a VPC peering connection `pcx-aaaabbbb` to route traffic between VPC A and a specific instance in VPC B. All other traffic destined for the `10.0.0.0/16` IP address range is routed through `pcx-aaaacccc` between VPC A and VPC C.

 

VPC route tables use the longest prefix match to select the most specific route across the intended VPC peering connection. All other traffic is routed through the next matching route, in this case, across the VPC peering connection `pcx-aaaacccc`.

 

![image](https://media.tutorialsdojo.com/sap_vpc_peering_cidr_example.png)

 

If you have a VPC peered with multiple VPCs that have overlapping or matching CIDR blocks, ensure that your route tables are configured to avoid sending response traffic from your VPC to the incorrect VPC. AWS currently does not support unicast reverse path forwarding in VPC peering connections that check the source IP of packets and route reply packets back to the source. You still need to configure static routes on VPC-B and VPC-C going to VPC-A, respectively.

 

Therefore, the correct answer is: **On VPC-A, add a static route for VPC-B CIDR (`10.0.0.77/32`) with the target `pcx-aaaabbbb` and another static route for VPC-C CIDR (`10.0.0.0/16`) with the target` pcx-aaaacccc`. On VPC-B, add a static route for VPC-A CIDR (`172.16.0.0/16`) with the target `pcx-aaaabbbb`. On VPC-C, add a static route for VPC-A CIDR (`172.16.0.0/16`) with the target `pcx-aaaacccc`.**  The standard VPC peering configuration will be done for VPC-A and VPC-C. As for VPC-B, only the static route to the specific should be configured on VPC-A. AWS will handle the longest prefix match to route the traffic.

 

The option that says:**On VPC-A, add a static route for VPC-B CIDR (`10.0.0.0/24`) with the target `pcx-aaaabbbb` and another static route for VPC-C CIDR (`10.0.0.0/24`) with the target `pcx-aaaacccc`. Add a network access control list (NACL) on VPC-A to deny all connections to VPC-B except for the IP address `10.0.0.77/32`. On VPC-B, add a static route for VPC-A CIDR (`172.16.0.0/24`) with the target `pcx-aaaabbbb`. On VPC-C, add a static route for VPC-A CIDR (`172.16.0.0/24`) with the target `pcx-aaaacccc`**  is incorrect. This will only result in a conflict on the routing configuration on VPC-A. Network ACLs can block connections going out of your VPC, however, they can’t redirect connections out to specific targets.

 

The option that says: **Enable dynamic route propagation in VPC-A with the peering targets `pcx-aaaabbbb` and `pcx-aaaacccc` respectively. On VPC-B, enable dynamic route propagation with peering target `pcx-aaaabbbb` and add a network acces control list (NACL) that allows only connections to IP address `10.0.0.77/32` from `pcx-aaaabbbb`. On VPC-C, enable dynamic route propagation with the peering target `pcx-aaaacccc`**  is incorrect. Dynamic route propagation is primarily used for Direct Connection connections or Site-to-Site VPNs. In this scenario, you want to force a specific route to a specific instance on a specific peering target, thus, you need to configure static routes.

 

The option that says: **On VPC-A, add a static route for VPC-B CIDR (`10.0.0.0/24`) with the target `pcx-aaaabbbb` and another static route for VPC-C CIDR (`10.0.0.0/16`) with the target `pcx-aaaacccc`. On VPC-B, add a static route for VPC-A CIDR (`172.16.0.0/24`) with the target `pcx-aaaabbbb`. On VPC-C, add a static route for VPC-A CIDR (`172.16.0.0/24`) with the target `pcx-aaaacccc`**  is incorrect. Route configuration for VPC-A and VPC-C is correct here, however, the route configuration of VPC-A and VPC-B is not. This will make traffic to other instances in the CIDR (`10.0.0.0/24`), which is under VPC-C, to be routed to VPC-B.

 

 

**References:**

 

[https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html#one-to-two-vpcs-lpm](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html#one-to-two-vpcs-lpm)

 

[https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html)

 

[https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html)

 

 

**Check out this Amazon VPC Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

---

## Câu 51 — ✅ ĐÚNG

### Câu hỏi

A company is building a new cryptocurrency trading platform that will be hosted on the AWS cloud. The solutions architect needs to set up the designed architecture in a single VPC. The solution should mitigate distributed denial-of-service (DDoS) attacks to secure the company’s applications and systems. The solution should also include a notification for incoming Layer 3 or Layer 4 attacks such as SYN floods and UDP reflection attacks. The system should also be protected against SQL injection, cross-site scripting, and other Layer 7 attacks.



Which of the following solutions should the solutions architect implement together to meet the above requirement? (Select TWO.)

### Các phương án

- **A.** Use AWS WAF to define customizable web security rules that control which traffic can access your web applications.
- **B.** Place your servers behind a CloudFront web distribution and improve your cache hit ratio.
- **C.** Use AWS Shield Advanced which provides enhanced DDoS attack detection and monitoring for application-layer traffic to your AWS resources.
- **D.** Set up rule-based filtering using the AWS Network Firewall service.
- **E.** Send network logs to Amazon Fraud Detector to detect DDoS attacks and send notifications to security teams.

> **Bạn chọn:** A, C
> **Đáp án đúng:** A, C

### Giải thích

Correct 

A **Distributed Denial of Service (DDoS)**  attack is a malicious attempt to make a targeted system, such as a website or application, unavailable to end users. To achieve this, attackers use a variety of techniques that consume network or other resources, interrupting access for legitimate end-users.

 

![image](https://media.tutorialsdojo.com/sap_aws_shield.png)

 

AWS provides flexible infrastructure and services that help customers implement strong DDoS mitigations and create highly available application architectures that follow AWS Best Practices for DDoS Resiliency. These include services such as Amazon Route 53, Amazon CloudFront, Elastic Load Balancing, and AWS WAF to control and absorb traffic and deflect unwanted requests. These services integrate with **AWS Shield** , a managed DDoS protection service that provides always-on detection and automatic inline mitigations to safeguard web applications running on AWS.

 

**AWS WAF**  is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web security rules. You can use AWS WAF to create custom rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that are designed for your specific application. New rules can be deployed within minutes, letting you respond quickly to changing traffic patterns. Also, AWS WAF includes a full-featured API that you can use to automate the creation, deployment, and maintenance of web security rules.

 

In this scenario, AWS Shield Advanced and AWS WAF are the two services that can provide optimal DDoS attack mitigation and protection against Layer 7 security risks to your cloud infrastructure.

 

Therefore the correct answers are:

 

**– Use AWS Shield Advanced which provides enhanced DDoS attack detection and monitoring for application-layer traffic to your AWS resources.**

 

**– Use AWS WAF to define customizable web security rules that control which traffic can access your web applications** .

 

The option that says: **Send network logs to Amazon Fraud Detector to detect DDoS attacks and send notifications to security teams**  is incorrect. Amazon Fraud Detector uses machine learning that automates the detection of potentially fraudulent activities online. It is designed to predict fraudulent transactions based on previous data sets that were used to create a model. It is not designed to detect and mitigate DDoS attacks. AWS Shield is a more suitable service for this scenario.

 

The option that says: **Place your servers behind a CloudFront web distribution and improve your cache hit ratio**  is incorrect. Although CloudFront can help mitigate DDoS attacks, improving the cache hit ratio of your CloudFront distribution is still not enough to totally protect your infrastructure. This option also fails to mention the geoblocking and HTTPS protocol support features of CloudFront. Using AWS Shield Advanced and AWS WAF will provide more effective protection against DDoS.

 

The option that says:**Set up rule-based filtering using the AWS Network Firewall service**  is incorrect. AWS Network Firewall is primarily used to manage multiple firewall rules across hundreds of Amazon VPCs and AWS Accounts that are usually under a single AWS Organization. It is explicitly mentioned in the scenario that the company is using its sole AWS account, and the solution is only running on a single Amazon VPC. Hence, using the AWS Network Firewall service is not suitable for this case.

 

 

**References** :

 

[https://aws.amazon.com/answers/networking/aws-ddos-attack-mitigation/](https://aws.amazon.com/answers/networking/aws-ddos-attack-mitigation/)

 

[https://d0.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf](https://d0.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf)

 

[https://aws.amazon.com/network-firewall](https://aws.amazon.com/network-firewall)

 

 

**Check out these AWS WAF and AWS Shield Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-waf/](https://tutorialsdojo.com/aws-waf/)

 

[https://tutorialsdojo.com/aws-shield/](https://tutorialsdojo.com/aws-shield/)

---

## Câu 52 — ✅ ĐÚNG

### Câu hỏi

An electric utility company deploys smart meters for its customers to easily track electricity usage. Each smart meter sends data every five minutes to an Amazon API Gateway, which is then processed by several AWS Lambda functions before being stored in an Amazon DynamoDB table. The Lambda functions take about 5 to 10 seconds to process the data based on the initial deployment testing. As the company’s customer base grew, the solutions architect noticed that the Lambda functions were now taking 60 to 90 seconds to complete the processing. New metrics are also collected from the smart meters, which further increases the processing time. Errors began showing when running the Lambda function, such as `TooManyRequestsException` and `ProvisionedThroughputExceededException` error when performing a PUT operation on the DynamoDB table.



Which combination of the following actions will resolve these issues? (Select TWO.)

### Các phương án

- **A.** The new metrics being collected requires more processing power from the Lambda functions. Adjust the memory allocation for the Lambda function to accommodate the surge.
- **B.** As more customers are sending data, adjust the Write Capacity Unit (WCU) of the DynamoDB table to be able to accommodate all the write requests being processed by the Lambda functions.
- **C.** Modify the Amazon API Gateway throttling limits and quotas at the stage level to allow a higher request rate and burst capacity so that incoming smart meter data is not throttled before being sent to Lambda.
- **D.** Process the data in batches to avoid reaching the write limits to the DynamoDB table. Group the requests from API Gateway by streaming the data into an Amazon Kinesis data stream.
- **E.** Since the Lambda functions are being overwhelmed with too many requests, increase the payload size from the meters but send the data less frequently to avoid reaching the concurrency limit.

> **Bạn chọn:** B, D
> **Đáp án đúng:** B, D

### Giải thích

Correct 

In **Amazon DynamoDB** , the `ProvisionedThroughputExceededException` error means that you exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes. This means that your request rate is too high. The AWS SDKs for DynamoDB automatically retries requests that receive this exception. Your request is eventually successful unless your retry queue is too large to finish.

 

To solve this, you can increase the write capacity unit (WCU) of your DynamoDB table. Every PutItem request consumes a write capacity unit. A write capacity unit represents one write per second, for an item up to 1 KB in size. For example, suppose that you create a table with 10 write capacity units. This allows you to perform 10 writes per second for items up to 1 KB in size.

 

![image](https://media.tutorialsdojo.com/public/DynamoDB Auto scaling-03FEB2026.png)

 

In **AWS Lambda,**  the first time you invoke your function, AWS Lambda creates an instance of the function and runs its handler method to process the event. When the function returns a response, it stays active and waits to process additional events. If you invoke the function again while the first event is being processed, Lambda initializes another instance, and the function processes the two events concurrently. Your functions’ concurrency is the number of instances that serve requests at a given time. For an initial burst of traffic, your functions’ cumulative concurrency in a Region can reach an initial level of between 500 and 3000, which varies per Region.

 

When seeing the `TooManyRequestsException` in AWS Lambda, it is possible that the throttles that you’re seeing aren’t on your Lambda function. Throttles can also occur on API calls during your function’s invocation or on concurrency limits.

 

With **API Gateway** , you can send the stream to an Amazon Kinesis data stream on which you can group requests in batches, so there will be a decrease in requests in Lambda.

 

Hence, the correct answers are:

 

**– As more customers are sending data, adjust the Write Capacity Unit (WCU) of the DynamoDB table to be able to accommodate all the write requests being processed by the Lambda functions.**

 

**– Process the data in batches to avoid reaching the write limits to the DynamoDB table. Group the requests from API Gateway by streaming the data into an Amazon Kinesis data stream.**

 

The option that says: **The new metrics being collected requires more processing power from the Lambda functions. Adjust the memory allocation for the Lambda function to accommodate the surge**  is incorrect. While increasing memory allocation can improve the Lambda function’s execution speed, it can only do so to a certain extent. This improvement may alleviate some occurrences of the `TooManyRequestsException` error, especially at lower memory configurations. However, as you approach the upper memory limits, the performance gains tend to plateau, making it less effective than solutions such as batching. Moreover, the cost in running the function will also increase significanly.

 

The option that says: **Since the Lambda functions are being overwhelmed with too many requests, increase the payload size from the meters but send the data less frequently to avoid reaching the concurrency limit**  is incorrect. Although this will solve the `TooManyRequestsException` for the Lambda function, you may reach the 10MB payload limit on the API gateway if you aggregate too much data before sending it to the API Gateway.

 

The option that says: **Modify the Amazon API Gateway throttling limits and quotas at the stage level to allow a higher request rate and burst capacity so that incoming smart meter data is not throttled before being sent to Lambda**  is incorrect because the errors observed (`TooManyRequestsException` and `ProvisionedThroughputExceededException`) are typically caused by Lambda concurrency limits and DynamoDB throughput, not API Gateway throttling. API Gateway quotas are much higher than the described workload, so increasing them would not resolve the actual bottlenecks.

 

 

**References:**

 

[https://aws.amazon.com/premiumsupport/knowledge-center/lambda-troubleshoot-throttling/](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-troubleshoot-throttling/)

 

[https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html#concurrent-execution-safety-limit](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html#concurrent-execution-safety-limit)

 

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html)

 

[https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html)

 

 

**Check out these AWS Lambda and Amazon DynamoDB Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-lambda/](https://tutorialsdojo.com/aws-lambda/)

 

[https://tutorialsdojo.com/amazon-dynamodb/](https://tutorialsdojo.com/amazon-dynamodb/)

---

## Câu 53 — ❌ SAI

### Câu hỏi

A company hosts its main web application on the AWS cloud which is composed of web servers and database servers. To ensure high availability, the web servers are deployed on an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones with an Application Load Balancer in front. For the database, it is deployed on a Multi-Availability Zone configuration in Amazon RDS. During the RDS maintenance window, the operating system of the primary DB instance undergoes software patching that triggers the failover process.



What would happen to the database during failover?

### Các phương án

- **A.** A new DB instance will be created and immediately replace the primary database.
- **B.** The canonical name record (CNAME) is changed from the primary database to standby database.
- **C.** The RDS DB instance will automatically reboot.
- **D.** The IP address of the primary DB instance is switched to the standby DB instance.

> **Bạn chọn:** D
> **Đáp án đúng:** B

### Giải thích

Incorrect  

**Amazon RDS Multi-AZ**  deployments provide enhanced availability and durability for Database (DB) Instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of Amazon Aurora), so that you can resume database operations as soon as the failover is complete.

 

![image](https://media.tutorialsdojo.com/sap_rds_multiaz.png)

 

When automatic failover occurs, your application can remain unaware of what’s happening behind the scenes. The CNAME record for your DB instance will be altered to point to the newly promoted standby.

 

Therefore, the correct answer is: **The canonical name record (CNAME) is changed from the primary database to standby database.**

 

The option that says: **The** **IP address of the primary DB instance is switched to the standby DB instance**  is incorrect because the Canonical Name Record (CNAME) will be changed and not the IP address.

 

The option that says: **The RDS DB instance will automatically reboot**  is incorrect because the RDS instance will not automatically reboot.

 

The option that says:**A new DB instance will be created and immediately replace the primary database**  is incorrect because there is no new DB instance that will be created.

 

 

**References:**

 

[https://aws.amazon.com/rds/details/multi-az/](https://aws.amazon.com/rds/details/multi-az/)

 

[https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-deployment/](https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-deployment/)

 

 

**Check out this Amazon RDS Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

---

## Câu 54 — ✅ ĐÚNG

### Câu hỏi

A company runs a popular photo-sharing site hosted on the AWS cloud. There are user complaints about the frequent downtime of the site considering the hefty price for using their service. The company is using a MySQL RDS instance to record user details and other data analytics. A standard S3 storage class bucket is used to store the photos and user metadata, which are frequently accessed only in the first month. The website is also capable of immediately retrieving the images no matter how long they were stored. The RDS instance is always affected and sometimes goes down when there is a problem in the Availability Zone. The solutions architect was tasked to analyze the current architecture and to solve the user complaints about the website. In addition, the solutions architect should also implement a system that automatically discovers, classifies, and protects personally identifiable information (PII) data in the Amazon S3 bucket.



Which of the following options offers the BEST solution for this scenario?

### Các phương án

- **A.** Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 bucket with EBS Volumes and use Redshift instead of RDS.
- **B.** Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Amazon S3 Glacier Deep Archive after a month. Re-configure the existing database to use RDS Multi-AZ Deployments.
- **C.** Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 Standard bucket with an Infrequent Access storage class. Re-configure the existing database to use RDS Read Replicas.
- **D.** Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Infrequent Access storage class after a month. Re-configure the existing database to use RDS Multi-AZ Deployments.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**Amazon Macie**  is a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. Amazon Macie recognizes sensitive data such as personally identifiable information (PII) or intellectual property and provides you with dashboards and alerts that give visibility into how this data is being accessed or moved. The fully managed service continuously monitors data access activity for anomalies and generates detailed alerts when it detects the risk of unauthorized access or inadvertent data leaks. Today, Amazon Macie is available to protect data stored in Amazon S3, with support for additional AWS data stores soon.

 

![image](https://media.tutorialsdojo.com/sap_macie_dashboard.jpg)

 

In this scenario, the best way to solve the issue is to: **Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Infrequent Access storage class after a month. Re-configure the existing database to use RDS Multi-AZ Deployments** . Keep in mind that the website should be able to immediately retrieve the images no matter how long they were stored. This means that you should not archive the images.

 

The option that says: **Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 bucket with EBS Volumes and use Redshift instead of RDS**  is incorrect because EBS Volumes are not as scalable as S3 and Redshift is not a suitable storage option as it is mainly used as a petabyte-scale data warehouse service.

 

The option that says: **Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Amazon S3 Glacier Deep Archive after a month. Re-configure the existing database to use RDS Multi-AZ Deployments**  is incorrect because although it is right to use Amazon RDS Multi-AZ deployments configuration, the use of Glacier Deep Archive is not preferred for this scenario. Take note that Glacier is primarily used for archiving and the retrieval times are much slower compared to S3. Implementing this solution means that the users will have to wait a long time to retrieve their photos. In addition, Amazon Inspector is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS, especially in Amazon EC2 instances. You have to use Amazon Macie instead.

 

The option that says: **Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 Standard bucket with an Infrequent Access storage class. Re-configure the existing database to use RDS Read Replicas**  is incorrect because although it is right to use Infrequent Access storage class, the use of Read Replica is not suitable for this scenario. Although it may improve availability, you are only limited to use read operations when you use Read Replicas. This means when the primary database is down, the Read Replica would not be available to register new users since read operations are only allowed. Moreover, you have to use Amazon Macie and not Amazon Inspector, since this is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS.

 

 

**References:**

 

[https://aws.amazon.com/s3/storage-classes/](https://aws.amazon.com/s3/storage-classes/)

 

[https://aws.amazon.com/macie/](https://aws.amazon.com/macie/)

 

[https://aws.amazon.com/macie/details/](https://aws.amazon.com/macie/details/)

 

 

**Check out this Amazon S3 Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

 

 

**Check out this Amazon Macie Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-macie/](https://tutorialsdojo.com/amazon-macie/)

---

## Câu 55 — ✅ ĐÚNG

### Câu hỏi

A company has an on-premises identity provider (IdP) used for authenticating employees. The Solutions Architect has created a SAML 2.0 based federated identity solution that integrates with the company IdP. This solution is used to authenticate users’ access to the AWS environment. Upon initial testing, the Solutions Architect has been successfully granted access to the AWS environment through the federated identity web portal. However, other test users who tried to authenticate through the federated identity web portal are not given access to the AWS environment.



Which of the following options must be checked to ensure the proper configuration of identity federation? (Select THREE.)

### Các phương án

- **A.** Ensure that the ARN of the SAML provider, the ARN of the created IAM role, and SAML assertion from the IdP are all included when the federated identity web portal calls the AWS STS `AssumeRoleWithSAML` API.
- **B.** Ensure that the IAM policy for that user has “Allow” permissions to use SAML federation.
- **C.** Ensure that the appropriate IAM roles are mapped to company users and groups in the IdP’s SAML assertions.
- **D.** Ensure that the trust policy of the IAM roles created for the federated users or groups has set the SAML provider as principal.
- **E.** Ensure that the resources on the AWS environment Amazon VPC can reach the on-premises IdP using its DNS hostname.
- **F.** Check the company’s IdP to ensure that the users are all part of the default `AWSFederatedUser` IAM group which is readily available in AWS.

> **Bạn chọn:** A, C, D
> **Đáp án đúng:** A, C, D

### Giải thích

Correct 

AWS supports identity federation with SAML 2.0 (Security Assertion Markup Language 2.0), an open standard that many identity providers (IdPs) use. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without having to create an IAM user for everyone in your organization. By using SAML, you can simplify the process of configuring federation with AWS because you can use the IdP’s service instead of writing custom identity proxy code.

 

IAM federation supports these use cases:

 

– Federated access allows a user or application in your organization to call AWS API operations. You use a SAML assertion (as part of the authentication response) that is generated in your organization to get temporary security credentials.

 

– Web-based single sign-on (SSO) to the AWS Management Console from your organization. Users can sign in to a portal in your organization hosted by a SAML 2.0–compatible IdP, select an option to go to AWS, and be redirected to the console without having to provide additional sign-in information. You can use a third-party SAML IdP to establish SSO access to the console or you can create a custom IdP to enable console access for your external users.

 

![image](https://media.tutorialsdojo.com/public/iam-identity-center-ldap-25Feb2025.png)

 

The diagram illustrates the following steps:

 

1. The user browses to your organization’s portal and selects the option to go to the AWS Management Console. In your organization, the portal is typically a function of your IdP that handles the exchange of trust between your organization and AWS.
2. The portal verifies the user’s identity in your organization.
3. The portal generates a SAML authentication response that includes assertions that identify the user and include attributes about the user. The portal sends this response to the client browser.
4. The client browser is redirected to the AWS IAM Identity Center endpoint and posts the SAML assertion.
5. The endpoint requests temporary security credentials on behalf of the user and creates a console sign-in URL that uses those credentials.
6. AWS sends the sign-in URL back to the client as a redirect.
7. The client browser is redirected to the AWS Management Console. If the SAML authentication response includes attributes that map to multiple IAM roles, the user is first prompted to select the role for accessing the console.

 

Before you can use SAML 2.0-based federation, you must configure your organization’s IdP and your AWS account to trust each other. Inside your organization, you must have an IdP that supports SAML 2.0, like Microsoft Active Directory Federation Service (AD FS, part of Windows Server), Shibboleth, or another compatible SAML 2.0 provider. In your organization’s IdP, you define assertions that map users or groups in your organization to the IAM roles. Note that different users and groups in your organization might map to different IAM roles. The exact steps for performing the mapping depend on what IdP you’re using.

 

The role or roles that you create in IAM define what federated users from your organization are allowed to do in AWS. When you create the trust policy for the role, you specify the SAML provider that you created earlier as the `Principal`. You can additionally scope the trust policy with a `Condition` element to allow only users that match certain SAML attributes to access the role.

 

Hence, the correct answers are:

 

**– Ensure that the trust policy of the IAM roles created for the federated users or groups has set the SAML provider as principal** . In IAM, you create one or more IAM roles for the federated users. In the role’s trust policy, you need to set the SAML provider as the principal, which establishes a trust relationship between your organization and AWS.

 

– **Ensure that the ARN of the SAML provider, the ARN of the created IAM role, and SAML assertion from the IdP are all included when the federated identity web portal calls the AWS STS `AssumeRoleWithSAML` API** . These items should all be passed by the client calling the AWS STS `AssumeRoleWithSAML` API.

 

**–** **Ensure that the appropriate IAM roles are mapped to company users and groups in the IdP’s SAML assertions** . In your organization’s IdP, you should define assertions that map users or groups in your organization to the IAM roles.

 

The option that says: **Ensure that the IAM policy for that user has “Allow” permissions to use SAML federation** is incorrect because the test user’s permissions are mapped to IAM roles, so we need to take a look at the IAM role policies and not the individual user IAM permission policies.

 

The option that says: **Check the company’s IdP to ensure that the users are all part of the default `AWSFederatedUser` IAM group which is readily available in AWS**  is incorrect because there is no such thing as a default `AWSFederatedUser` IAM group. You only need to define assertions in your organization’s IdP that map users or groups in your organization to the IAM roles.

 

The option that says: **Ensure that the resources on the AWS environment Amazon VPC can reach the on-premises IdP using its DNS hostname**  is incorrect as this is not primarily a requirement for the identity federation to work.

 

 

**References:**

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html)

 

[https://aws.amazon.com/blogs/security/how-to-set-up-federated-single-sign-on-to-aws-using-google-workspace/](https://aws.amazon.com/blogs/security/how-to-set-up-federated-single-sign-on-to-aws-using-google-workspace/)

 

 

**Check out these AWS Security and Identity Services Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-cheat-sheets-security-identity-services/](https://tutorialsdojo.com/aws-cheat-sheets-security-identity-services/)

---

## Câu 56 — ✅ ĐÚNG

### Câu hỏi

An international insurance company has clients all across the globe. The company has financial files that are stored in an Amazon S3 bucket which is behind CloudFront. At present, their clients can access their data by directly using an S3 URL or using their CloudFront distribution. The company wants to deliver their content to a specific client in California and they need to make sure that only that client can access the data.



Which of the following options is a valid solution that meets the above requirements? (Select TWO.)

### Các phương án

- **A.** Use CloudFront Signed Cookies to ensure that only their client can access the files. Enable HTTPS in your CloudFront distribution.
- **B.** Create a new S3 bucket in US West (N. California) region and upload the files. Set up an origin access control (OAC) and give it permission to read the files in the bucket. Enable HTTPS in your CloudFront distribution.
- **C.** Use CloudFront signed URLs to ensure that only their client can access the files. Enable field-level encryption in your CloudFront distribution.
- **D.** Create a new S3 bucket in US West (N. California) region and upload the files. Use S3 pre-signed URLs to ensure that only their client can access the files. Remove permission to use Amazon S3 URLs to read the files for anyone else.
- **E.** Use CloudFront signed URLs to ensure that only their client can access the files. Create an origin access control (OAC) and give it permission to read the files in the bucket. Remove permission to use Amazon S3 URLs to read the files for anyone else.

> **Bạn chọn:** D, E
> **Đáp án đúng:** D, E

### Giải thích

Correct 

Many companies that distribute content over the internet want to restrict access to documents, business data, media streams, or content that is intended for selected users, for example, users who have paid a fee. To securely serve this private content by using CloudFront, you can do the following:

 

– Require that your users access your private content by using special CloudFront signed URLs or signed cookies.

 

– Require that your users access your Amazon S3 content by using CloudFront URLs, not Amazon S3 URLs. Requiring CloudFront URLs isn’t necessary, but it is recommended to prevent users from bypassing the restrictions that you specify in signed URLs or signed cookies.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_oia.png)

 

All objects and buckets by default are private. The presigned URLs are useful if you want your user/customer to be able to upload a specific object to your bucket, but you don’t require them to have AWS security credentials or permissions. You can generate a presigned URL programmatically using the AWS SDK for Java or the AWS SDK for .NET. If you are using Microsoft Visual Studio, you can also use AWS Explorer to generate a presigned object URL without writing any code. Anyone who receives a valid presigned URL can then programmatically upload an object.

 

Therefore, the correct answer is: **Create a new S3 bucket in US West (N. California) region and upload the files. Use S3 pre-signed URLs to ensure that only their client can access the files. Remove permission to use Amazon S3 URLs to read the files for anyone else**  and **Use CloudFront signed URLs to ensure that only their client can access the files. Create an origin access control (OAC) and give it permission to read the files in the bucket. Remove permission to use Amazon S3 URLs to read the files for anyone else.**  Using a presigned URL to your S3 bucket will prevent other users from getting your private data which is intended to a certain client. A combination of Signed URL and OAC is also a valid solution that meets the requirement.

 

The option that says: **Use CloudFront Signed Cookies to ensure that only their client can access the files. Enable HTTPS in your CloudFront distribution**  is incorrect. The signed cookies feature is primarily used if you want to provide access to multiple restricted files, for example, all of the files for a video in HLS format or all of the files in the subscribers’ area of website. In addition, this solution is not complete since the users can bypass the restrictions by simply using the direct S3 URLs.

 

The option that says: **Use CloudFront signed URLs to ensure that only their client can access the files. Enable field-level encryption in your CloudFront distribution**  is incorrect. Although this solution is valid, the users can still bypass the restrictions in CloudFront by simply connecting to the direct S3 URLs.

 

The option that says: **Create a new S3 bucket in US West (N. California) region and upload the files. Set up an origin access control (OAC) and give it permission to read the files in the bucket. Enable HTTPS in your CloudFront distribution**  is incorrect. An Origin Access Control (OAC) will only require your client to only access the files by using the CloudFront URL and not through a direct S3 URL. This can be a possible solution if it mentions the use of Signed URL or Signed Cookies.

 

 

**References** :

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html)

 

 

**Check out this Amazon CloudFront Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

 

 

**S3 Pre-signed URLs vs CloudFront Signed URLs vs Origin Access Control (OAC)**

 

[https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/](https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/)

 

 

**Comparison of AWS Services Cheat Sheets:**

 

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

---

## Câu 57 — ✅ ĐÚNG

### Câu hỏi

An enterprise software company has just recently started using AWS as its cloud infrastructure. The company is building an enterprise proprietary issue tracking system which would be accessed by its customers worldwide. Hence, the CTO carefully instructed the team to ensure that the architecture of the issue tracking system is both scalable and highly available to avoid any complaints from the clients. It is expected that the application will have steady-state usage, and the database would be used for online transaction processing (OLTP). The team recently used the AWS Well-Architected Tool to review its architecture, which highlighted the need for a highly available and fault-tolerant design.



Which of the following would be the best architecture setup to satisfy the above requirement?

### Các phương án

- **A.** Use multiple On-Demand Amazon EC2 instances to host the application and a highly scalable Amazon DynamoDB for the database. Use Amazon ElastiCache for in-memory data caching for your database to improve performance.
- **B.** Use an AWS CloudFormation template to launch an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones, which are all connected via an ELB to handle the load balancing. Leverage Amazon CloudFront for distributing your static content and an Amazon RDS instance with a Multi-AZ deployment configuration.
- **C.** Use a Dedicated Amazon EC2 instance as the application server and Amazon Redshift as a petabyte-scale data warehouse service. Use Amazon ElastiCache for in-memory data caching for your database to improve performance.
- **D.** Launch an Auto Scaling group of Spot Amazon EC2 instances with an ELB in front to handle the load balancing. Leverage on Amazon CloudFront in distributing your static content and an Amazon RDS instance with Read Replicas.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

It is recommended to use a **CloudFormation**  template to launch your architecture in AWS. An Auto Scaling group of EC2 instances across multiple Availability Zones with an ELB in front is a highly available and scalable architecture. In addition, leveraging on CloudFront in distributing your static content improves the load times of the system. Finally, an RDS instance with Multi-AZ deployments configuration can ensure the availability of your database in case one instance goes down.

 

![image](https://media.tutorialsdojo.com/sap_cloudformation_steps.png)

 

Therefore, the correct answer is: **Use an AWS CloudFormation template to launch an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones, which are all connected via an ELB to handle the load balancing. Leverage Amazon CloudFront for distributing your static content and an Amazon RDS instance with a Multi-AZ deployment configuration** . This offers high availability and scalability for the application.

 

The option that says: **Use a Dedicated Amazon EC2 instance as the application server and Amazon Redshift as a petabyte-scale data warehouse service. Use Amazon ElastiCache for in-memory data caching for your database to improve performance**  is incorrect. Using Dedicated EC2 instances without Auto Scaling is not a scalable nor a highly available architecture. In addition, RedShift is not applicable to OLTP but rather with OLAP.

 

The option that says: **Launch an Auto Scaling group of Spot Amazon EC2 instances with an ELB in front to handle the load balancing. Leverage on Amazon CloudFront in distributing your static content and an Amazon RDS instance with Read Replicas**  is incorrect. Spot EC2 instances are just not suitable for steady state usage and Read Replicas only provide limited availability compared to Multi-AZ Deployments.

 

The option that says: **Use multiple On-Demand Amazon EC2 instances to host the application and a highly scalable Amazon DynamoDB for the database. Use Amazon ElastiCache for in-memory data caching for your database to improve performance**  is incorrect. This does not use Auto Scaling and is not deployed across multiple Availability Zones.

 

 

**References:**

 

[https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf)

 

[https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-best-practices.html](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-best-practices.html)

 

[https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/architecting-for-high-availability.html](https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/architecting-for-high-availability.html)

 

 

**Check out this Amazon EC2 Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

 

 

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

 

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

---

## Câu 58 — ❌ SAI

### Câu hỏi

A finance company plans to launch a new website to let users view tutorials promoting proper use of the mobile app. The website contains static media files stored in a private Amazon S3 bucket, while dynamic content is hosted on an AWS Fargate cluster. The Fargate tasks are accepting traffic behind an Application Load Balancer (ALB). To improve the user experience, static and dynamic content are served via an Amazon CloudFront distribution. An Amazon Route 53 Alias record has already been created to point the website URL to the CloudFront distribution. The company wants to ensure that access to both static and dynamic content is handled exclusively through CloudFront.



Which of the following options should the Solutions Architect implement to meet this requirement? (Select TWO.)

### Các phương án

- **A.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer.
- **B.** Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets.
- **C.** Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC.
- **D.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution.
- **E.** Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution.

> **Bạn chọn:** B, C
> **Đáp án đúng:** A, C

### Giải thích

Incorrect  

**AWS WAF**  is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the values of query strings or the IP addresses that requests originate from, CloudFront responds to requests either with the requested content or with an HTTP status code `403(Forbidden)`. You can also configure CloudFront to return a custom error page when a request is blocked.

 

After you create an **AWS WAF web access control list (web ACL)** , create or update a web distribution to associate the distribution with the web ACL. You can associate as many CloudFront distributions as you want with the same web ACL or with different web ACLs.

 

On **Amazon CloudFront** , you can control user access to your private content in two ways:

 

1. Restrict access to files in CloudFront caches.
2. Restrict access to files in your origin by doing one of the following:

 

– Set up an origin access control (OAC) for your Amazon S3 bucket.

 

– Configure custom headers for a private HTTP server (a custom origin).

 

CloudFront provides two ways to send authenticated requests to an Amazon S3 origin: origin access control (OAC) and origin access identity (OAI). OAC helps you secure your origins, such as Amazon S3.

 

AWS recommends that you use OAC instead because it supports the following features:

 

- All Amazon S3 buckets in all AWS Regions, including opt-in Regions launched after December 2022
- Amazon S3 server-side encryption with AWS KMS (SSE-KMS)
- Dynamic requests (`PUT` and `DELETE`) to Amazon S3

 

Origin Access Identity (OAI) is considered a legacy, not-recommended mechanism due to its functional limitations.

 

You can secure the content in your Amazon S3 bucket so that users can access it through CloudFront, but cannot access it directly by using Amazon S3 URLs. This prevents someone from bypassing CloudFront and using the Amazon S3 URL to get content that you want to restrict access to. To require that users access your content through CloudFront URLs, you do the following tasks:

 

1. Create an origin access control and associate it with your CloudFront distribution.
2. Give the origin access control permission to read the files in your bucket.
3. Remove permission for anyone else to use Amazon S3 URLs to read the files.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_oia.png)

 

If you use a custom origin, you can optionally set up custom headers to restrict access. For CloudFront to get your files from a custom origin, the files must be accessible by CloudFront using a standard HTTP (or HTTPS) request. But by using custom headers, you can further restrict access to your content so that users can access it only through CloudFront, not directly. This step isn’t required to use signed URLs, but it is recommended. To require that users access content through CloudFront, change the following settings in your CloudFront distributions:

 

**Origin Custom Headers**  – Configure CloudFront to forward custom headers to your origin.

 

**Viewer Protocol Policy**  – Configure your distribution to require viewers to use HTTPS to access CloudFront.

 

**Origin Protocol Policy**  – Configure your distribution to require CloudFront to use the same protocol as viewers to forward requests to the origin.

 

Hence, the correct answers are:

 

**– Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer.**  After you create an AWS WAF web access control list (web ACL), create or update a web distribution to associate the distribution with the ALB. Associating the Web ACL with the ALB ensures that only requests from CloudFront will reach the ALB. Any request going to the ALB without the custom header will be denied by WAF.

 

**–**  **Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC.**  OAC enables CloudFront to use SigV4-signed requests to access private S3 content, and the S3 bucket policy can explicitly allow access only from CloudFront via that OAC. This prevents users from retrieving objects directly from S3 and forces access through CloudFront.

 

The option that says: **Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution**  is incorrect. If any new requests are going to CloudFront, they won’t have the custom header initially, so AWS WAF may block the request immediately. This could deny any new connections to CloudFront. Therefore, you need to associate the web ACL to the ALB, which is after CloudFront adds the custom header.

 

The option that says: **Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets**  is incorrect. This will limit all resources inside the ALB subnets to accept only traffic from the CloudFront distribution. However, there are no fixed IP addresses for Amazon CloudFront, and if you manually add AWS IP addresses, you will have to update the NACL as AWS updates its IP pool.

 

The option that says: **Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution**  is incorrect. You can’t directly configure a bucket ACL to allow access only from Amazon CloudFront. You typically need an origin access control (OAC) for this setup.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#forward-custom-headers-restrict-access](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#forward-custom-headers-restrict-access)

 

 

**Check out these Amazon CloudFront and AWS WAF Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

 

[https://tutorialsdojo.com/aws-waf/](https://tutorialsdojo.com/aws-waf/)

---

## Câu 59 — ✅ ĐÚNG

### Câu hỏi

A company uses a CloudFormation script to deploy an online voting application. The app is used for a Nature Photography Contest that accepts high-resolution images, stores them in an S3 bucket, and records a 100-character summary about the image in RDS. The Solutions Architect must ensure that the same online voting application can be deployed once again using the same CloudFormation template for succeeding contests in the future. The photography contest will run for just a month and once it has been concluded, there would be nobody using the online voting application anymore until the next contest. As preparation for the upcoming events next year, the 100-character summaries should be kept and the S3 bucket, which contains the high-resolution photos, should remain.



Which of the following options is the recommended action to meet the above requirement?

### Các phương án

- **A.** 1. Enable Cross-Region Replication (CRR) in the S3 bucket to maintain a copy of all the S3 objects. 2. Set the DeletionPolicy for the RDS instance to `Snapshot`.
- **B.** 1. Set the DeletionPolicy on the S3 resource declaration in the CloudFormation template to `Retain`. 2. Set the RDS resource declaration DeletionPolicy to `Snapshot`.
- **C.** For both the RDS and S3 resource types on the CloudFormation template, set the DeletionPolicy to `Retain`.
- **D.** 1. Set the DeletionPolicy on the S3 resource to `Snapshot`. 2. Set the DeletionPolicy on the RDS resource to `Snapshot`.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

With the **DeletionPolicy attribute** , you can preserve or (in some cases) back up a resource when its stack is deleted. You specify a DeletionPolicy attribute for each resource that you want to control. If a resource has no DeletionPolicy attribute, AWS CloudFormation deletes the resource by default.

 

![image](https://media.tutorialsdojo.com/sap_cloudformation_deletionpolicy-2.JPG)

 

Note that this capability also applies to stack update operations that lead to resources being deleted from stacks, for example, if you remove the resource from the stack template and then update the stack with the template. This capability does not apply to resources whose physical instance is replaced during stack update operations. For example, if you edit a resource’s properties such that AWS CloudFormation replaces that resource during a stack update.

 

In this scenario, you need to keep the data on your S3 bucket and RDS which can be achieved by **setting the DeletionPolicy of S3 to `Retain` and for RDS to use** **`Snapshot`** .

 

**Setting the DeletionPolicy on the S3 resource to `Snapshot` and for RDS resource to use** **`Snapshot`** ***``***  is incorrect because S3 does not support snapshots. It should be set to `Retain`.

 

**For both the RDS and S3 resource types on the CloudFormation template, setting the DeletionPolicy to** **`Retain`** ***``***  is incorrect. Although you can set `Retain` on both the DeletionPolicy of the S3 bucket and the RDS database, this entails an unnecessary operating cost since the RDS database will still be running even if it is not used. Take note that the application is meant to run for just a month and once it has been concluded, nobody would be using it until the next contest next year. The RDS should be set to `Snapshot`.

 

**Enabling Cross-Region Replication (CRR) in the S3 bucket to maintain a copy of all the S3 objects and setting the DeletionPolicy for the RDS instance to `Snapshot`** is incorrect because even though your data will still be available in the other region because of the CRR, the current S3 bucket will still be deleted.

 

 

**References:**

 

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/delete-cf-stack-retain-resources/](https://aws.amazon.com/premiumsupport/knowledge-center/delete-cf-stack-retain-resources/)

 

 

**Check out this AWS CloudFormation Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

---

## Câu 60 — ✅ ĐÚNG

### Câu hỏi

A media company in South Korea offers high-quality wildlife photos to its clients. Its photographers upload a large number of photographs to the company’s Amazon S3 bucket. Currently, the company is using a dedicated group of on-premises servers to process the photos and uses an open-source messaging system to deliver job information to the servers. After processing, the data would go to a tape library and be stored for long-term archival. The company decided to shift everything to AWS Cloud, and the solutions architect was tasked to implement the same existing infrastructure design and leverage AWS tools such as storage and messaging services to minimize cost.



Which of the following options is the recommended solution that will meet the requirement?

### Các phương án

- **A.** Create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon Glacier.
- **B.** SQS will handle the job messages, while CloudWatch alarms will terminate any idle EC2 worker instances. After the data has been processed, change the storage class of your S3 objects to S3 IA-Standard.
- **C.** Initially change the storage class of the S3 objects to S3 IA-Standard. Then create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon S3-IA.
- **D.** SNS will handle the passing of job messages, while CloudWatch alarms will terminate any idle spot worker instances. After the data has been processed, transfer your S3 objects to Amazon Glacier.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

There are some scenarios where you might think about scaling in response to activity in an **Amazon SQS queue** . For example, suppose that you have a web app that lets users upload images and use them online. In this scenario, each image requires resizing and encoding before it can be published. The app runs on EC2 instances in an Auto Scaling group, and it’s configured to handle your typical upload rates. Unhealthy instances are terminated and replaced to maintain current instance levels at all times. The app places the raw bitmap data of the images in an SQS queue for processing. It processes the images and then publishes the processed images where they can be viewed by users. The architecture for this scenario works well if the number of image uploads doesn’t vary over time. But if the number of uploads changes over time, you might consider using dynamic scaling to scale the capacity of your Auto Scaling group.

 

![image](https://media.tutorialsdojo.com/sap_sqs_cloudwatch_metric.png)

 

In this scenario, the best option is the combination of SQS and Glacier as a storage option.

 

Therefore, the correct answer is: **Create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon Glacier.** It uses SQS to process the messages, and it uses Glacier as the archival storage solution which is the cheapest storage option.

 

The option that says: **SQS will handle the job messages, while CloudWatch alarms will terminate any idle EC2 worker instances. After the data has been processed, change the storage class of your S3 objects to S3 IA-Standard**  is incorrect. S3 IA is not an archival storage option, and since auto scaling is not mentioned, you cannot use CloudWatch alarms to terminate the idle EC2 instances.

 

The option that says: **Initially change the storage class of the S3 objects to S3 IA-Standard. Then create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon S3-IA**  is incorrect. S3 IA is not an archival storage option.

 

The option that says: **SNS will handle the passing of job messages, while CloudWatch alarms will terminate any idle spot worker instances. After the data has been processed, transfer your S3 objects to Amazon Glacier**  is incorrect. Amazon Simple Notification Service cannot be used to process the messages.

 

**References** :

 

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

 

[https://aws.amazon.com/glacier](https://aws.amazon.com/glacier)

 

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html)

 

 

**Check out these Amazon SQS and Amazon S3 Glacier Cheat Sheets:**

 

**[https://tutorialsdojo.com/amazon-sqs/](https://tutorialsdojo.com/amazon-sqs/)**

 

**[https://tutorialsdojo.com/amazon-glacier/](https://tutorialsdojo.com/amazon-glacier/)**

---

## Câu 61 — ✅ ĐÚNG

### Câu hỏi

A company hosts a stateful licensing application on an Amazon EC2 instance.



The application is tied to the instance’s existing network configuration, and client systems must continue connecting to the same IP address after recovery. The company wants the instance to recover automatically when the underlying AWS hardware fails.



Which solution will meet the given requirements?

### Các phương án

- **A.** Configure an Amazon CloudWatch alarm that monitors the `StatusCheckFailed_System` metric and triggers the EC2 instance recovery action.
- **B.** Use AWS Systems Manager Automation to patch the EC2 instance when the system status check fails.
- **C.** Associate an Elastic IP address with the EC2 instance and configure an Amazon CloudWatch alarm to stop and start the instance after a system status check failure.
- **D.** Configure an Amazon CloudWatch alarm to invoke an AWS Lambda function that runs the aws `ec2 reboot-instances` command whenever the EC2 instance reports a system status check failure.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

If AWS detects that an instance is unavailable due to an underlying hardware or software issue, CloudWatch action-based recovery can automatically restore the instance’s availability by migrating it from the affected host to a different host.

 

![image](https://media.tutorialsdojo.com/public/EC2 Action - Recover this instance-29JUN2026.png)

 

You can configure CloudWatch action-based recovery to add recovery actions to Amazon CloudWatch alarms. CloudWatch action-based recovery works with the `StatusCheckFailed_System` metric. CloudWatch action-based recovery provides to-the-minute recovery response time granularity and Amazon Simple Notification Service (Amazon SNS) notifications of recovery actions and outcomes.

 

![image](https://media.tutorialsdojo.com/public/StatusCheckFailed_System-29JUN2026.png)

 

These configuration options enable quicker recovery attempts and provide more precise control over how the system responds to status check failures, compared to simplified automatic recovery.

 

Hence, the correct answer is: **Configure an Amazon CloudWatch alarm that monitors the `StatusCheckFailed_System` metric and triggers the EC2 instance recovery action.**  The recovery action automatically moves the instance to healthy hardware while preserving the instance ID, private IP, and Elastic IP. This ensures the licensing application continues to use the same network configuration, and client systems can reconnect seamlessly.

 

The option that says: **Associate an Elastic IP address with the EC2 instance and configure an Amazon CloudWatch alarm to stop and start the instance after a system status check failure**  is incorrect because stopping and starting the instance will launch it on new hardware, but this disrupts the ephemeral state and is not the intended automatic recovery mechanism. While the Elastic IP ensures the same public IP, this approach is manual and less reliable compared to the native recovery action.

 

The option that says: **Use AWS Systems Manager Automation to patch the EC2 instance when the system status check fails**  is incorrect because patching typically addresses software or OS-level issues, not hardware failures. A system status check failure indicates underlying AWS hardware problems, which patching cannot resolve.

 

The option that says: **Configure an Amazon CloudWatch alarm to invoke an AWS Lambda function that runs the aws `ec2 reboot-instances` command whenever the EC2 instance reports a system status check failure**  is incorrect because rebooting the instance only restarts it on the same faulty hardware. This does not resolve system-level failures and does not guarantee recovery.

 

 

**References:**

 

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cloudwatch-recovery.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cloudwatch-recovery.html)

 

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html)

 

 

**Check out these Amazon EC2 and Amazon CloudWatch Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

 

[https://tutorialsdojo.com/amazon-cloudwatch/](https://tutorialsdojo.com/amazon-cloudwatch/)

---

## Câu 62 — ❌ SAI

### Câu hỏi

A hospital chain in London uses an online central hub for its doctors and nurses. The application interacts with millions of requests per day to fetch various medical data of their patients. The system is composed of a web tier, an application tier, and a database tier that receives large and unpredictable traffic demands. The Solutions Architect must ensure that this infrastructure is highly-available and scalable enough to handle web traffic fluctuations automatically.



Which of the following options should the solutions architect implement to meet the above requirements?

### Các phương án

- **A.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **B.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **C.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas.
- **D.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled.

> **Bạn chọn:** A
> **Đáp án đúng:** D

### Giải thích

Incorrect  

When users or services interact with an application, they will often perform a series of interactions that form a session. A session is unique data for users that persists between requests while they use the application. A stateless application is an application that does not need knowledge of previous interactions and does not store session information.

 

![image](https://media.tutorialsdojo.com/sap_spot_stateless_session.png)

 

For example, an application that, given the same input, provides the same response to any end user, is a stateless application. Stateless applications can scale horizontally because any of the available compute resources (such as EC2 instances and AWS Lambda functions) can service any request. Without stored session data, you can simply add more compute resources as needed. When that capacity is no longer required, you can safely terminate those individual resources, after running tasks have been drained. Those resources do not need to be aware of the presence of their peers—all that is required is a way to distribute the workload to them.

 

In this scenario, the best option is to use a combination of **Amazon**  **ElastiCache Serverless** , **Cloudwatch** , and **RDS Read Replica** .

 

Therefore, the correct answer is: **Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled.**  It uses stateless instances. The web server uses ElastiCache Serverless for read operations and relies on CloudWatch for monitoring traffic fluctuations. When variations in traffic occur, CloudWatch notifies the autoscaling group to perform scale-in or scale-out actions accordingly. ElastiCache Serverless is a robust cache solution that ensures high availability by automatically replicating data across multiple Availability Zones. Furthermore, it leverages read replicas for RDS to efficiently handle read-heavy workloads and utilizes Multi-AZ configurations to ensure high availability.

 

The option that says: **Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled**  is incorrect because it uses stateful instances. It also does not use any caching mechanism for web and application tiers, and multi-AZ RDS does not improve read performance.

 

The option that says: **Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas**  is incorrect because it uses stateful instances and it does not use any caching mechanism for web and application tiers.

 

The option that says: **Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.**  is incorrect because multi-AZ RDS only improves Availability, not read performance.

 

 

**References** :

 

[https://aws.amazon.com/elasticache/](https://aws.amazon.com/elasticache/ )

 

[https://aws.amazon.com/rds/details/read-replicas/](https://aws.amazon.com/rds/details/read-replicas/)

 

[https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf)

 

 

**Check out these AWS Cheat Sheets:**

 

**[https://tutorialsdojo.com/amazon-elasticache/](https://tutorialsdojo.com/amazon-elasticache/)**

 

**[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)**

---

## Câu 63 — ✅ ĐÚNG

### Câu hỏi

An online stock trading application is deployed to multiple Availability Zones in the us-east-1 region (N. Virginia) and uses RDS to host the database. Considering the massive financial transactions that the trading application handles, the company has hired you to be a consultant to make sure that the system is scalable, highly-available, and disaster resilient. In the event of failure, the Recovery Time Objective (RTO) must be less than 2 hours and the Recovery Point Objective (RPO) must be 10 minutes to meet the compliance requirements set by the regulators.



In this scenario, which Disaster Recovery strategy can be used to achieve the RTO and RPO requirements in the event of system failure? (Select TWO.)

### Các phương án

- **A.** Store hourly database backups to an EC2 instance store volume with transaction logs stored in an S3 bucket every 5 minutes.
- **B.** Take 15-minute database backups stored in Glacier with transaction logs stored in S3 every 5 minutes.
- **C.** Take hourly database backups and export to an S3 bucket with transaction logs stored in S3 every 5 minutes. Set up a Cross-Region Replication (CRR) to another AWS Region.
- **D.** Configure your database to use synchronous “source-replica” replication between multiple Availability Zones.
- **E.** Set up an AWS Backup plan for the Amazon RDS database with the continuous backups for point-in-time recovery (PITR) option enabled

> **Bạn chọn:** C, E
> **Đáp án đúng:** C, E

### Giải thích

Correct 

**Point-in-time recovery (PITR)**  is the process of restoring a database to the state it was in at a specified date and time.

 

When automated backups are turned on for your DB instance, Amazon RDS automatically performs a full daily snapshot of your data. The snapshot occurs during your preferred backup window. It also captures transaction logs to Amazon S3 every 5 minutes (as updates to your DB instance are made). Archiving the transaction logs is an important part of your DR process and PITR. When you initiate a point-in-time recovery, transactional logs are applied to the most appropriate daily backup in order to restore your DB instance to the specific requested time.

 

![image](https://media.tutorialsdojo.com/sap_s3_replication.jpg)

 

With S3 Cross-Region Replication (CRR), you can replicate objects (and their respective metadata and object tags) into other AWS Regions for reduced latency, compliance, security, disaster recovery, and other use cases. S3 CRR is configured to a source S3 bucket and replicates objects into a destination bucket in another AWS Region.

 

Amazon S3 CRR automatically replicates data between buckets across different AWS Regions. With CRR, you can set up replication at a bucket level, a shared prefix level, or an object level using S3 object tags. You can use CRR to provide lower-latency data access in different geographic regions. CRR can also help if you have a compliance requirement to store copies of data hundreds of miles apart. You can use CRR to change account ownership for the replicated objects to protect data from accidental deletion.

 

**AWS Backup**  is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud and on-premises. Using this service, you can configure backup policies and monitor activity for your AWS resources in one place. It allows you to automate and consolidate backup tasks that were previously performed service-by-service and remove the need to create custom scripts and manual processes. With a few clicks in the AWS Backup console, you can automate your data protection policies and schedules.

 

AWS Backup supports continuous backups and point-in-time recovery (PITR) in addition to snapshot backups.

 

With **continuous backups** , you can restore your AWS Backup-supported resource by rewinding it back to a specific time that you choose within 1 second of precision (going back a maximum of 35 days). Continuous backup works by first creating a full backup of your resource and then constantly backing up your resource’s transaction logs. PITR restore works by accessing your full backup and replaying the transaction log to the time that you tell AWS Backup to recover.

 

![image](https://media.tutorialsdojo.com/public/aws_backup_rds_continuous_backup.png)

 

In this scenario, you have to use durable storage, database backups, and continuous backups for point-in-time recovery (PITR) to satisfy the RTO and RPO requirements. Hence,

 

The option that says: **Take hourly database backups and export to an S3 bucket with transaction logs stored in S3 every 5 minutes. Set up a Cross-Region Replication (CRR) to another AWS Region**  is correct as this solution meets the 2-hour RTO as well as the 10-minute RPO requirement.

 

The option that says: **Set up an AWS Backup plan for the Amazon RDS database with the continuous backups for point-in-time recovery (PITR) option enabled**  is correct as AWS Backup has a native feature that you can enable to satisfy the point-in-time recovery (PITR) requirement.

 

The option that says: **Store hourly database backups to an EC2 instance store volume with transaction logs stored in an S3 bucket every 5 minutes**  is incorrect because an instance store volume is ephemeral and it is not suitable to store the database backups.

 

The option that says: **Take 15-minute database backups stored in Glacier with transaction logs stored in S3 every 5 minutes**  is incorrect because the RTO is at least 3 hours, which means that Amazon Glacier is not the ideal solution to use. Note that the standard retrieval time for Glacier is 3 to 5 hours and with that time, you will surely miss your RTO.

 

The option that says: **Configure your database to use synchronous “source-replica” replication between multiple Availability Zones**  is incorrect because it provides a highly available architecture but it doesn’t provide any durable storage nor DB snapshots.

 

 

**References:**

 

[https://www.slideshare.net/AmazonWebServices/disaster-recovery-options-with-aws](https://www.slideshare.net/AmazonWebServices/disaster-recovery-options-with-aws)

 

[https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/](https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/)

 

[https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html)

 

 

**Check out this AWS Well-Architected Framework Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-well-architected-framework-disaster-recovery/](https://tutorialsdojo.com/aws-well-architected-framework-disaster-recovery/)

 

 

**RPO and RTO Explained:**

---

## Câu 64 — ✅ ĐÚNG

### Câu hỏi

A company runs its internal tool on AWS. It is used for logistics and shipment tracking for the company’s warehouse. With the current system process, the application receives an order and it sends an email to the employees with the information needed for the package shipment. After the employees prepare the order and ship the package, a reply is sent to the email so that the application can mark the order as shipped. The company wants to migrate to a serverless application model to stop relying on emails and minimize the operational overhead for the application.



Which of the following options should the Solutions Architect implement to meet the company requirements?

### Các phương án

- **A.** Create AWS Batch jobs corresponding to different tasks needed to ship a package. Write an AWS Lambda function with AWS Batch as the trigger to create and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger another Lambda function to move the AWS Batch job to the next stage of the shipping process.
- **B.** Use an Amazon EFS volume to store the new order information. Configure an instance to pull the order information from the EFS share and print the shipping label for the package. Once the package is scanned and leaves the warehouse, remove the order information on the EFS share by using an Amazon API Gateway call to the instances.
- **C.** Store order information on an Amazon SQS queue when a new order is created. Schedule an AWS Lambda function to poll the queue every 5 minutes and start processing if any orders are found. Use another Lambda function to print the shipping labels for the package. Once the package is scanned and leaves the warehouse, use Amazon SNS to send a notification to customers regarding the status of their order.
- **D.** Store the order information on an Amazon DynamoDB table. Create an AWS Step Functions workflow that will be triggered for every new order. Have the workflow mark the order as “in progress” and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger an AWS Lambda function to mark the order as “shipped” and complete the Step Functions workflow.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**AWS Step Functions**  is a serverless orchestration service that lets you combine AWS Lambda functions and other AWS services to build business-critical applications. Orchestration centrally manages a workflow by breaking it into multiple steps, adding flow logic, and tracking the inputs and outputs between the steps. As your applications execute, Step Functions maintains the application state, tracking exactly which workflow step your application is in and storing an event log of data that is passed between application components.

 

Step Functions is based on state machines and tasks. A state machine is a workflow. A task is a state in a workflow that represents a single unit of work that another AWS service performs. Each step in a workflow is a state.

 

With Step Functions’ built-in controls, you examine the state of each step in your workflow to make sure that your application runs in order and as expected. Depending on your use case, you can have Step Functions call AWS services, such as **AWS Lambda** , to perform tasks.

 

Step Functions is ideal for coordinating session-based applications. You can use Step Functions to coordinate all of the steps of a checkout process on an e-commerce site, for example. Step Functions can read and write from **Amazon DynamoDB**  as needed to manage inventory records.

 

![image](https://media.tutorialsdojo.com/public/AWS Step Functions-12OCT2026.png)

 

You can use Step Functions to make decisions about how best to process data, for example, to do post-processing of groups of satellite images to determine the amount of trees per acre of land. Depending on the size and resolution of the image, this Step Functions workflow will determine whether to use AWS Lambda or AWS Fargate to complete the post-processing of each file in order to optimize runtime and costs.

 

![image](https://media.tutorialsdojo.com/sap_step_function_amazon_s3.JPG)

 

Using AWS Step Functions, you define your workflows as state machines, which transform complex code into easy-to-understand statements and diagrams. Building apps and confirming that they are implementing your desired functionality is quicker and easier.

 

Therefore, the correct answer is: **Store the order information on an Amazon DynamoDB table. Create an AWS Step Functions workflow that will be triggered for every new order. Have the workflow mark the order as “in progress” and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger an AWS Lambda function to mark the order as “shipped” and complete the Step Functions workflow.**  Step Functions is suitable to orchestrate this workflow to update a DynamoDB table for the order progress as well trigger AWS Lambda functions for various actions.

 

The option that says: **Create AWS Batch jobs corresponding to different tasks needed to ship a package. Write an AWS Lambda function with AWS Batch as the trigger to create and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger another Lambda function to move the AWS Batch job to the next stage of the shipping process**  is incorrect. AWS Batch is not designed to orchestrate a workflow. AWS Batch is used to run batch jobs such as transaction reporting or analysis reporting, which usually run as stand-alone jobs.

 

The option that says: **Store order information on an Amazon SQS queue when a new order is created. Schedule an AWS Lambda function to poll the queue every 5 minutes and start processing if any orders are found. Use another Lambda function to print the shipping labels for the package. Once the package is scanned and leaves the warehouse, use Amazon SNS to send a notification to customers regarding the status of their order**  is incorrect. This may be possible; however, polling the SQS every 5 minutes is not efficient compared to writing to the DynamoDB table. If there are no orders for the past 5 minutes, the Lambda function will still run.

 

The option that says: **Use an Amazon EFS volume to store the new order information. Configure an instance to pull the order information from the EFS share and print the shipping label for the package. Once the package is scanned and leaves the warehouse, remove the order information on the EFS share by using an Amazon API Gateway call to the instances**  is incorrect. Using an EFS share will require EC2 instances and will increase the operational overhead needed to manage the infrastructure. This is not a serverless solution.

 

 

**References:**

 

[https://aws.amazon.com/step-functions/use-cases/](https://aws.amazon.com/step-functions/use-cases/)

 

[https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

 

[https://aws.amazon.com/step-functions/features/](https://aws.amazon.com/step-functions/features/)

 

[https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/](https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/)

 

 

**Check out the AWS Step Functions Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-step-functions/](https://tutorialsdojo.com/aws-step-functions/)

---

## Câu 65 — ✅ ĐÚNG

### Câu hỏi

A multinational healthcare company plans to launch a new MedTech information website. The solutions architect decided to use Amazon CloudFormation to deploy a three-tier web application that consists of a web tier, an application tier, and a database tier that will utilize Amazon DynamoDB for storage. The solutions architect must secure any credentials that are used to access the database tier. The company already uses AWS CloudTrail Lake data store to audit API activity and track credential usage across its AWS accounts.



Which of the following options will allow the application instances access to the DynamoDB tables without exposing API credentials?

### Các phương án

- **A.** Create an IAM User in the CloudFormation template and assign permissions to read and write from the DynamoDB table. Then retrieve the values of the access and secret keys using CloudFormation's GetAtt function, and pass them to the application instance through user-data.
- **B.** Create an IAM Role and assign the required permissions to read and write from the DynamoDB table. Have the instance profile property of the application instance reference the role.
- **C.** Create an IAM Role that grants access to the DynamoDB table. Use the `AWS::SSM::Parameter` resource that creates an SSM parameter in AWS Systems Manager Parameter Store containing the Amazon Resource Name of the IAM role. Have the instance profile property of the application instance reference the role.
- **D.** Have the user enter the access and secret keys of an existing IAM User that has permissions to read and write from the DynamoDB table instead of using the Parameter section in the CloudFormation template.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

Applications that run on an EC2 instance must include AWS credentials in their AWS API requests. You could have your developers store AWS credentials directly within the EC2 instance and allow applications in that instance to use those credentials. But developers would then have to manage the credentials and ensure that they securely pass the credentials to each instance and update each EC2 instance when it’s time to rotate the credentials. That’s a lot of additional work.

 

Instead, you can and should use an **IAM role**  to manage *temporary*  credentials for applications that run on an EC2 instance. When you use a role, you don’t have to distribute long-term credentials (such as a user name and password or access keys) to an EC2 instance. Instead, the role supplies temporary permissions that applications can use when they make calls to other AWS resources. When you launch an EC2 instance, you specify an IAM role to associate with the instance. Applications that run on the instance can then use the role-supplied temporary credentials to sign API requests.

 

An **IAM role**  is similar to a user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials (password or access keys) associated with it. Instead, if a user assumes a role, temporary security credentials are created dynamically and provided to the user. The scenario requires the instance to have access to DynamoDB tables without having to use the API credentials. In such scenarios, always think of creating IAM Roles rather than IAM Users.

 

![image](https://media.tutorialsdojo.com/sap_ec2_iam_role.png)

 

Therefore, the correct answer is: **Create an IAM Role and assign the required permissions to read and write from the DynamoDB table. Have the instance profile property of the application instance reference the role.**  It uses an IAM Role with the appropriate permissions to access the resource, and it references that Role in the instance profile property of the application instance.

 

The option that says: **Create an IAM User in the CloudFormation template and assign permissions to read and write from the DynamoDB table. Then retrieve the values of the access and secret keys using CloudFormation’s GetAtt function, and pass them to the application instance through user-data**  is incorrect because you should never expose the Access and Secret Keys while accessing AWS resources, and using an IAM Role is a simply more secure way of accessing the resources than using IAM Users with security credentials.

 

The option that says: **Create an IAM Role that grants access to the DynamoDB table. Use the `AWS::SSM::Parameter` resource that creates an SSM parameter in AWS Systems Manager Parameter Store containing the Amazon Resource Name of the IAM role. Have the instance profile property of the application instance reference the role**  is incorrect because storing the ARN of the IAM Role in the AWS Systems Manager Parameter Store is not the proper way to attach the role to the application instance. You have to use the instance profile property (`AWS::IAM::InstanceProfile`) instead.

 

The option that says: **Have the user enter the access and secret keys of an existing IAM User that has permissions to read and write from the DynamoDB table instead of using the Parameter section in the CloudFormation template**  is incorrect because you should never just expose the Access and Secret Keys while accessing the AWS resources, and using IAM Role is a more secure way of accessing the resources than using IAM Users with security credentials.
 **References:**

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)

 

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)

 

 

**Check out this AWS IAM Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

---

## Câu 66 — ✅ ĐÚNG

### Câu hỏi

A BPO company uses a multitiered, java-based content management system (CMS) hosted on an on-premises data center. The CMS has a JBoss Application server present in the application tier. The database tier consists of an Oracle database which is regularly backed up to S3 using the Oracle RMAN backup utility. The application’s static files and content are kept on a 512 GB Storage Gateway volume which is attached to the application server via an iSCSI interface. The solutions architect was tasked to create a disaster recovery solution for the application and its data.



Which AWS-based disaster recovery strategy will give you the best RTO?

### Các phương án

- **A.** Use RDS for your Oracle database and EC2 for the JBoss application server. Restore the RMAN Oracle backups from Amazon Glacier, and provision an EBS volume containing static content obtained from Storage Gateway. The volume will be attached to the JBoss EC2 server.
- **B.** Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Use an AWS Storage Gateway-VTL running on Amazon EC2 as your source for restoring static content.
- **C.** Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Also provision an EBS volume containing static content obtained from Storage Gateway, and attach the volume to the JBoss EC2 server.
- **D.** Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Attach an AWS Storage Gateway running on Amazon EC2 as an iSCSI volume to the JBoss EC2 server to access the static content.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**Recovery Manager (RMAN)**  is an Oracle Database client that performs backup and recovery tasks on your databases and automates the administration of your backup strategies. It greatly simplifies backing up, restoring, and recovering database files.

 

By using stored volumes, you can store your primary data locally, while asynchronously backing up that data to AWS. Stored volumes provide your on-premises applications with low-latency access to their entire datasets. At the same time, they provide durable, offsite backups. You can create storage volumes and mount them as iSCSI devices from your on-premises application servers. Data written to your stored volumes is stored on your on-premises storage hardware. This data is asynchronously backed up to Amazon S3 as Amazon Elastic Block Store (Amazon EBS) snapshots.

 

If you are restoring an **AWS Storage Gateway volume snapshot** , you can choose to restore the snapshot as an AWS Storage Gateway volume or as an Amazon EBS volume. AWS Backup integrates with both services, and any AWS Storage Gateway snapshot can be restored to either an AWS Storage Gateway volume or an Amazon EBS volume.

 

![image](https://media.tutorialsdojo.com/sap_rman_oracle.png)

 

The option that says: **Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Also provision an EBS volume containing static content obtained from Storage Gateway, and attach the volume to the JBoss EC2 server**  is correct because it deploys the Oracle database on an EC2 instance by restoring the backups from S3 which can provide a faster recovery time, and it generates the EBS volume of static content from Storage Gateway.

 

The option that says: **Use RDS for your Oracle database and EC2 for the JBoss application server. Restore the RMAN Oracle backups from Amazon Glacier, and provision an EBS volume containing static content obtained from Storage Gateway. The volume will be attached to the JBoss EC2 server**  is incorrect because restoring the backups from Amazon Glacier will be slower than S3 and will not meet the RTO.

 

The option that says: **Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Attach an AWS Storage Gateway running on Amazon EC2 as an iSCSI volume to the JBoss EC2 server to access the static content**  is incorrect because there is no need to attach the Storage Gateway as an iSCSI volume; you can just easily and quickly create an EBS volume from the Storage Gateway. Then, you can generate snapshots from the EBS volumes for better recovery time.

 

The option that says: **Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Use an AWS Storage Gateway-VTL running on Amazon EC2 as your source for restoring static content**  is incorrect as restoring the content from Virtual Tape Library will not fit into the RTO.

 

 

**References:**

 

[https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html)

 

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RMAN.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RMAN.html)

 

[https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-storage-gateway.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-storage-gateway.html)

 

 

**Check out this AWS Storage Gateway Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-storage-gateway/](https://tutorialsdojo.com/aws-storage-gateway/)

---

## Câu 67 — ✅ ĐÚNG

### Câu hỏi

A company is implementing cloud best practices for its infrastructure. The Solutions Architect is using AWS CloudFormation templates for infrastructure-as-code of its two-tier web application. The application frontend is hosted on an Auto Scaling group of Amazon EC2 instances while the database is an Amazon RDS for MySQL instance. For security purposes, the database password must be rotated every 60 days.



Which of the following solutions is the MOST secure way to store and retrieve the database password for the web application?

### Các phương án

- **A.** On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Add a `UserData` property to reference the secret resource in the initialization script of the Auto Scaling group’s launch template using the `Ref` intrinsic function. Use the `Ref` intrinsic function to reference the secret resource as the value of the `MasterUserPassword` property in the `AWS::RDS::DBInstance` resource.
- **B.** On the CloudFormation template, create an encrypted parameter using AWS Systems Manager Parameter Store for the database password. Add a `UserData` property to reference the encrypted parameter in the initialization script of the Auto Scaling group’s launch template. Use the `Fn::GetAtt` intrinsic function to reference the encrypted parameter as the value of the `MasterUserPassword` property in the `AWS::RDS::DBInstance` resource.
- **C.** On the CloudFormation template, create a database password parameter. Add a `UserData` property to reference the password parameter in the initialization script of the Auto Scaling group’s launch template using the `Ref` intrinsic function. Save the password inside the EC2 instance upon its launch. Use the `Ref` intrinsic function to reference the parameter as the value of the `MasterUserPassword` property in the `AWS::RDS::DBInstance` resource.
- **D.** On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Modify the application to retrieve the database password from Secrets Manager when it launches. Use a dynamic reference for the secret resource to be placed as the value of the `MasterUserPassword` property of the `AWS::RDS::DBInstance` resource.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**AWS Secrets Manager**  integrates with **AWS CloudFormation**  so you can create and retrieve secrets securely using CloudFormation. This integration makes it easier to automate provisioning your AWS infrastructure. For example, without any code changes, you can generate unique secrets for your resources with every execution of your CloudFormation template. This also improves the security of your infrastructure by storing secrets securely, encrypting automatically, and enabling rotation more easily. Secrets Manager helps you protect the secrets needed to access your applications, services, and IT resources.

 

**CloudFormation**  helps you model your AWS resources as templates and execute these templates to provision AWS resources at scale. Some AWS resources require secrets as part of the provisioning process. For example, to provision a MySQL database, you must provide the credentials for the database superuser. You can use Secrets Manager, the AWS dedicated secrets management service, to create and manage such secrets.

 

**Secrets Manager**  makes it easier to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. You can reference Secrets Manager in your CloudFormation templates to create unique secrets with every invocation of your template. By default, Secrets Manager encrypts these secrets with encryption keys that you own and control. Secrets Manager ensures the secret isn’t logged or persisted by CloudFormation by using a dynamic reference to the secret. You can configure Secrets Manager to rotate your secrets automatically without disrupting your applications. Secrets Manager offers built-in integrations for rotating credentials for all Amazon RDS databases and supports extensibility with AWS Lambda so you can meet your custom rotation requirements.

 

![image](https://media.tutorialsdojo.com/sap_secrets_manager_cloudformation.png)

 

**Dynamic references**  provide a compact, powerful way for you to specify external values that are stored and managed in other services, such as the Systems Manager Parameter Store, in your stack templates. When you use a dynamic reference, CloudFormation retrieves the value of the specified reference when necessary during stack and change set operations.

 

Secrets Manager resource types supported in CloudFormation:

 

`AWS::SecretsManager::Secret` — Create a secret and store it in Secrets Manager.

 

`AWS::SecretsManager::ResourcePolicy` — Create a resource-based policy and attach it to a secret. Resource-based policies enable you to control access to secrets.

 

`AWS::SecretsManager::SecretTargetAttachment` — Configure Secrets Manager to rotate the secret automatically.

 

`AWS::SecretsManager::RotationSchedule` — Define the Lambda function that will be used to rotate the secret.

 

Therefore, the correct answer is: **On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Modify the application to retrieve the database password from Secrets Manager when it launches. Use a dynamic reference for the secret resource to be placed as the value of the `MasterUserPassword` property of the `AWS::RDS::DBInstance` resource.** You can use dynamic references in CloudFormation to specify external values that are stored and managed in other services, such as AWS SSM Parameter Store or AWS Secrets Manager. Your application can then retrieve the database password resource on AWS Secrets Manager when it needs to.

 

The option that says: **On the CloudFormation template, create a database password parameter. Add a `UserData` property to reference the password parameter in the initialization script of the Auto Scaling group’s launch template using the `Ref` intrinsic function. Save the password inside the EC2 instance upon its launch. Use the `Ref` intrinsic function to reference the parameter as the value of the `MasterUserPassword` property in the `AWS::RDS::DBInstance` resource**  is incorrect. Using a normal parameter in CloudFormation is not secure. This will require you to either store the password on the template itself or input it on the AWS web console.

 

The option that says: **On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Add a `UserData` property to reference the secret resource in the initialization script of the Auto Scaling group’s launch template using the `Ref` intrinsic function. Use the `Ref` intrinsic function to reference the secret resource as the value of the `MasterUserPassword` property in the `AWS::RDS::DBInstance` resource**  is incorrect. Using the user data scripts to retrieve the database password may expose the password to the environment of the operating system of the EC2 instance. It is more secure to configure the application to retrieve the secret resource when the application launches so it is not exposed to anything outside the application.

 

The option that says: **On the CloudFormation template, create an encrypted parameter using AWS Systems Manager Parameter Store for the database password. Add a `UserData` property to reference the encrypted parameter in the initialization script of the Auto Scaling group’s launch template. Use the `Fn::GetAtt` intrinsic function to reference the encrypted parameter as the value of the `MasterUserPassword` property in the `AWS::RDS::DBInstance` resource**  is incorrect. AWS Systems Manager Parameter can store an encrypted password, however, it cannot generate a password that can be referenced in AWS CloudFormation. It also doesn’t support automatic rotation of the parameter.

 

 

**References:**

 

[https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_cloudformation.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_cloudformation.html)

 

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html)

 

[https://aws.amazon.com/blogs/security/how-to-create-and-retrieve-secrets-managed-in-aws-secrets-manager-using-aws-cloudformation-template/](https://aws.amazon.com/blogs/security/how-to-create-and-retrieve-secrets-managed-in-aws-secrets-manager-using-aws-cloudformation-template/)

 

 

**Check out these AWS Secrets Manager and AWS CloudFormation Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-secrets-manager/](https://tutorialsdojo.com/aws-secrets-manager/)

---

## Câu 68 — ✅ ĐÚNG

### Câu hỏi

A company is running thousands of virtualized Linux and Microsoft Windows servers on its on-premises data center. The virtual servers host a range of Java and PHP applications that use MySQL and Oracle databases. There are also several department services hosted on an external data center. The company uses SAN storage to provide iSCSI disks to its physical servers. The company wants to migrate its data center to the AWS Cloud, but the technical documentation of the systems is incomplete and outdated. The Solutions Architect was tasked to analyze the current environment and estimate the cost of migrating the resources to the cloud.



Which of the following should the Solutions Architect do to effectively plan the cloud migration? (Select THREE.)

### Các phương án

- **A.** Use the AWS Transform discovery tool to gather information about the running virtual machines and running applications inside the servers.
- **B.** Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket.
- **C.** Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.
- **D.** Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration.
- **E.** Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud.
- **F.** Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.

> **Bạn chọn:** A, C, F
> **Đáp án đúng:** A, C, F

### Giải thích

Correct 

The scenario requires tools of services that will help to effectively plan the cloud migration, so the answers should be focused on planning.

 

**AWS Transform**  is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.

 

With AWS Transform, you can:

 

– Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS

 

– Migrate VMware workloads to Amazon EC2

 

– Modernize .NET applications to Linux-ready cross-platform .NET

 

– Assess workloads for migration readiness

 

![image](https://media.tutorialsdojo.com/public/AWS Transform-16JUN2026.png)

 

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.

 

**The AWS Transform discovery tool**  assists you in automatically discovering the server inventory within your organization in preparation for migration. This tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To utilize the discovery tool, you need to configure one or more discovery sources, allow the tool to run, and then review the results displayed in the Discovered Inventory pane.

 

Once you configure a discovery source, the tool will begin collecting information. The time required for the discovery tool to completely analyze your network depends on the size of your environment. For businesses utilizing a directional migration approach, you can leverage the Migration Portfolio Assessment (MPA) files generated by the tool after the server collection is completed.

 

The **AWS Cloud Adoption Readiness Tool (CART)**  helps organizations of all sizes develop efficient and effective plans for cloud adoption and enterprise cloud migrations. This 16-question online survey and assessment report detail your cloud migration readiness across six perspectives, including business, people, process, platform, operations, and security. Once you complete a CART survey, you can provide your contact details to download a customized cloud migration assessment that charts your readiness and what you can do to improve it. This tool is designed to help organizations assess their progress with cloud adoption and identify gaps in organizational skills and processes.

 

**AWS Transform assessments**  evaluate the cost, feasibility, and business value of migrating on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinement through chat.

 

You can apply migration assessments for several objectives:

 

– Get cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx

 

– Receive automated right-sizing recommendations

 

– Assess business value and sustainability impact

 

– Compare multiple migration scenarios side by side

 

– Refine assessments interactively through chat

 

– Generate executive presentations and detailed reports

 

Therefore, the correct answers are:

 

**– Use the AWS Transform Discovery Tool to gather information about the running virtual machines and running applications inside the servers.**

 

**– Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.**

 

**– Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.**

 

The option that says: **Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud**  is incorrect because MGN is primarily used for the actual migration of your on-premises virtual machines to the AWS Cloud and not for planning. Take note that in the scenario, the Solutions Architect was tasked to analyze the existing on-premises architecture first before doing the actual migration to AWS.

 

The option that says: **Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration**  is incorrect because AWS X-Ray is typically used to debug production and distributed applications, such as those built using a microservices architecture. This is not helpful for planning the migration.

 

The option that says: **Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket**  is incorrect because Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. This is not helpful for assessing the applications on the on-premises data center.

 

 

**References:**

 

[https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html)

 

[https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)

 

[https://docs.aws.amazon.com/transform/latest/launchguide/resources.html](https://docs.aws.amazon.com/transform/latest/launchguide/resources.html)

 

[https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html)

 

 

**Check out this AWS Migration Strategies Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-migration-strategies-the-7-rs/](https://tutorialsdojo.com/aws-migration-strategies-the-7-rs/)

---

## Câu 69 — ✅ ĐÚNG

### Câu hỏi

A company has built an application that allows painters to upload photos of original creations. The app allows users from North America and European regions to browse the galleries and order chosen artworks. The application is hosted on a fixed set of Amazon EC2 instances in the us-east-1 region. Using mobile phones, the artists can scan and upload large, high-resolution images, which are stored in a centralized Amazon S3 bucket also in the same region. After the initial week of operation, the European artists are reporting slow performance when uploading images.



Which of the following is the best solution to improve the image upload process?

### Các phương án

- **A.** Set the centralized S3 bucket as the custom origin on an Amazon CloudFront distribution. This will use CloudFront’s global edge network to improve the upload speed.
- **B.** Increase the upload capacity by creating an AWS Global Accelerator endpoint in front of the EC2 instances. Create an Auto Scaling Group that can scale automatically based on the users' traffic.
- **C.** Enable multipart upload on S3 and redeploy the application to support it. This allows the transmission of separate parts of the image in parallel.
- **D.** Enable S3 Transfer Acceleration on the central S3 bucket. Use the s3-accelerate endpoint to upload the images.

> **Bạn chọn:** D
> **Đáp án đúng:** D

### Giải thích

Correct 

**Amazon S3 Transfer Acceleration**  enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.

 

***![image](https://media.tutorialsdojo.com/s3-transfer-acceleration.png )***

 

You might want to use Transfer Acceleration on a bucket for various reasons, including the following:

 

– You have customers that upload to a centralized bucket from all over the world.

 

– You transfer gigabytes to terabytes of data on a regular basis across continents.

 

– You are unable to utilize all of your available bandwidth over the Internet when uploading to Amazon S3.

 

You can enable Transfer Acceleration on a bucket in any of the following ways:

 

– Use the Amazon S3 console.

 

– Use the REST API PUT Bucket accelerate operation.

 

– Use the AWS CLI and AWS SDKs.

 

You can transfer data to and from the acceleration-enabled bucket by using one of the following s3-accelerate endpoint domain names:

 

`- s3-accelerate.amazonaws.com` – to access an acceleration-enabled bucket.

 

`- s3-accelerate.dualstack.amazonaws.com` – to access an acceleration-enabled bucket over IPv6. Amazon S3 dual-stack endpoints support requests to S3 buckets over IPv6 and IPv4.

 

You can point your Amazon S3 PUT object and GET object requests to the s3-accelerate endpoint domain name after you enable Transfer Acceleration. After Transfer Acceleration is enabled, it can take up to 20 minutes for you to realize the performance benefit. However, the accelerate endpoint will be available as soon as you enable Transfer Acceleration.

 

Therefore, the correct answer is: **Enable S3 Transfer Acceleration on the central S3 bucket. Use the s3-accelerate endpoint to upload the images.**

 

The option that says: **Enable multipart upload on S3 and redeploy the application to support it. This allows the transmission of separate parts of the image in parallel**  is incorrect. Although multipart upload can improve the upload throughput to an S3 bucket, the European users are still limited on their Internet connection to the S3 bucket in the US region. S3 Transfer acceleration uses the AWS backbone network, which can optimize the transfer from far away regions.

 

The option that says: **Set the centralized S3 bucket as the custom origin on an Amazon CloudFront distribution. This will use CloudFront’s global edge network to improve the upload speed**  is incorrect. CloudFront distribution is primarily designed for optimizing content delivery and content caching. Although CloudFront supports content uploads via POST, PUT, and other HTTP Methods, there is a limited connection timeout to the origin (60 seconds). If uploads take several minutes, the connection might get terminated. If you want to optimize performance when uploading large files to Amazon S3, it is recommended to use Amazon S3 Transfer Acceleration which can provide fast and secure transfers over long distances. Transfer Acceleration uses Amazon CloudFront’s globally distributed edge locations.

 

The option that says:**Increase the upload capacity by creating an AWS Global Accelerator endpoint in front of the EC2 instances. Create an Auto Scaling Group that can scale automatically based on the users’ traffic** is incorrect. Although AWS Global Accelerator can typically help increase network availability and performance, it won’t have an effect on this scenario because the images are directly uploaded to the S3 bucket. Increasing the number of EC2 instances does not necessarily improve the S3 upload speeds. Even if the application is configured to use the EC2 instance as a temporary storage for the images, the upload experience of the users will not improve because they are uploading from a different continent.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration-examples.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration-examples.html)

 

[https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/s3-upload-large-files/](https://aws.amazon.com/premiumsupport/knowledge-center/s3-upload-large-files/)

 

 

**Check out this Amazon S3 Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

---

## Câu 70 — ✅ ĐÚNG

### Câu hỏi

A popular news website that uses an Oracle database is currently deployed in the company’s on-premises network. Due to its growing number of readers, the company decided to move its infrastructure to AWS, where it can further improve the performance of the website. The company is also considering using AWS License Manager to track and manage its Oracle database licenses on AWS.



The company earns from the advertisements placed on the website, so the Solutions Architect was instructed to ensure that the website remains available in case of database server failures. The company’s team of content writers constantly uploads new articles every day, including the wee hours of the morning, to cover breaking news.



How can the Solutions Architect implement a highly available architecture to meet the requirements?

### Các phương án

- **A.** Create an Oracle Real Application Clusters (RAC) in Amazon RDS which provides a shared cache architecture that overcomes the limitations of traditional shared-nothing and shared-disk approaches to provide highly scalable and available database solutions for the news website.
- **B.** Create an Oracle database in Amazon RDS with Multi-AZ deployments.
- **C.** Create an Oracle database in Amazon RDS with Read Replicas.
- **D.** Create an Oracle database instance in Amazon RDS with Recovery Manager (RMAN) which performs backup and recovery tasks on your database and automates the administration of your backup strategies.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

**Amazon RDS Multi-AZ**  deployments provide enhanced availability and durability for Database (DB) Instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable.

 

In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of Amazon Aurora), so that you can resume database operations as soon as the failover is complete. Since the endpoint for your DB Instance remains the same after a failover, your application can resume database operations without the need for manual administrative intervention.

 

![image](https://media.tutorialsdojo.com/sap_rds_multiaz.png)

 

Therefore, the correct answer is: **Create an Oracle database in Amazon RDS with Multi-AZ deployments.**  This ensures high availability even if the primary database instance goes down.

 

The option that says: **Create an Oracle database in Amazon RDS with Read Replicas** is incorrect because the content writers won’t be able to upload their articles to the Read Replicas in the event that the primary database goes down.

 

The following options are incorrect because Oracle RMAN and RAC are not supported in RDS:

 

**– Create an Oracle database instance in Amazon RDS with Recovery Manager (RMAN) which performs backup and recovery tasks on your database and automates the administration of your backup strategies**

 

– **Create an Oracle Real Application Clusters (RAC) in Amazon RDS which provides a shared cache architecture that overcomes the limitations of traditional shared-nothing and shared-disk approaches to provide highly scalable and available database solutions for the news website** .

 

 

**References:**

 

[https://aws.amazon.com/rds/details/multi-az/](https://aws.amazon.com/rds/details/multi-az/)

 

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

 

 

**Check out this Amazon RDS Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

---

## Câu 71 — ✅ ĐÚNG

### Câu hỏi

A leading online media company runs a popular sports news website. The solutions architect has been tasked to analyze each web visitor’s clickstream data on the website to populate user analytics, which gives insights about the sequence of pages and advertisements the visitor has clicked. The data will be processed in real-time which will then transform the page layout as the visitors click through the web portal to increase user engagement and consequently, increase the revenue for the company.



Which of the following options should the solutions architect implement to meet the above requirements?

### Các phương án

- **A.** Publish web clicks by session to an Amazon SQS queue and periodically drain these events to Amazon RDS then analyze with SQL.
- **B.** Publish the web clicks to Amazon Timestream. Run custom analysis, SQL queries and apply machine learning to generate relevant reports regarding user behavior.
- **C.** Push web clicks by session to Amazon Kinesis and analyze behavior using Amazon Kinesis workers.
- **D.** Log clicks in weblogs by URL and store it in Amazon S3, and then analyze with Elastic MapReduce.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

**Amazon Kinesis**  makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information. Amazon Kinesis offers key capabilities to cost-effectively process streaming data at any scale, along with the flexibility to choose the tools that best suit the requirements of your application. With Amazon Kinesis, you can ingest real-time data such as video, audio, application logs, website clickstreams, and IoT telemetry data for machine learning, analytics, and other applications. Amazon Kinesis enables you to process and analyze data as it arrives and responds instantly instead of having to wait until all your data is collected before the processing can begin.

 

In this example, a simple HTML page simulates the content of a blog page. As the reader scrolls the simulated blog post, the browser script uses the SDK for JavaScript to record the scroll distance down the page and send that data to Kinesis using the **`putRecords`** method of the Kinesis client class. The streaming data captured by Amazon Kinesis Data Streams can then be processed by Amazon EC2 instances and stored in any of several data stores including Amazon DynamoDB and Amazon Redshift.

 

![image](https://media.tutorialsdojo.com/sap_kinesis_arch.JPG)

 

Therefore, the correct answer is: **Push web clicks by session to Amazon Kinesis and analyzing behavior using Amazon Kinesis workers.**

 

The following options are incorrect as SQS, EC2, EMR, and Timestream services do not have the capacity to analyze real-time streaming data:

 

**– Log clicks in weblogs by URL and store it in Amazon S3, and then analyze with Elastic MapReduce.**

 

**–** **Publish the web clicks to Amazon Timestream. Run custom analysis, SQL queries and apply machine learning to generate relevant reports regarding user behavior.**

 

**– Publish web clicks by session to an Amazon SQS queue and periodically drain these events to Amazon RDS then analyze with SQL.**

 

**References** :

 

[https://docs.aws.amazon.com/streams/latest/dev/introduction.html](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

 

[https://aws.amazon.com/kinesis/data-streams/](https://aws.amazon.com/kinesis/data-streams/)

 

[https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/kinesis-examples-capturing-page-scrolling.html](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/kinesis-examples-capturing-page-scrolling.html)

 

 

**Check out this Amazon Kinesis Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-kinesis/](https://tutorialsdojo.com/amazon-kinesis/)

---

## Câu 72 — ✅ ĐÚNG

### Câu hỏi

A company stores several terabytes of data on an Amazon S3 bucket. The data will be made available to respective partner companies, however, the management doesn’t want the partner companies to access the files directly from Amazon S3 URLs. The solutions architect has been asked to ensure that all confidential files shared via Amazon S3 should only be accessible through CloudFront.



Which of the following options could satisfy this requirement?

### Các phương án

- **A.** Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission.
- **B.** Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access.
- **C.** Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN).
- **D.** Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront.

> **Bạn chọn:** A
> **Đáp án đúng:** A

### Giải thích

Correct 

To restrict access to content that you serve from **Amazon S3**  buckets, you create **CloudFront signed URLs**  or **signed cookies**  to limit access to files in your Amazon S3 bucket, and then you create a special CloudFront user called an origin access control (OAC) and associate it with your distribution. Then you configure permissions so that CloudFront can use the OAC to access and serve files to your users, but users can’t use a direct URL to the S3 bucket to access a file there. Taking these steps helps you maintain secure access to the files that you serve through CloudFront.

 

In general, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you can either allow everyone to have access to the files there, or you can restrict access. If you limit access by using, for example, CloudFront signed URLs or signed cookies, you also won’t want people to be able to view files by simply using the direct URL for the file. Instead, you want them to only access the files by using the CloudFront URL, so your protections work.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_oia.png)

 

Typically, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you grant everyone permission to read the objects in your bucket. This allows anyone to access your objects either through CloudFront or using the Amazon S3 URL. CloudFront doesn’t expose Amazon S3 URLs, but your users might have those URLs if your application serves any objects directly from Amazon S3 or if anyone gives out direct links to specific objects in Amazon S3.

 

Therefore, the correct answer is: **Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission.**  It gives CloudFront exclusive access to the S3 bucket and prevents other users from accessing the public content of S3 directly via S3 URL.

 

The option that says: **Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN)**  is incorrect. Creating a bucket policy is unnecessary and it does not prevent other users from accessing the public content of S3 directly via S3 URL.

 

The option that says: **Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront**  is incorrect. This does not give CloudFront exclusive access to the S3 bucket.

 

The option that says: **Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access**  is incorrect. You do not need to create any individual policies for each bucket.

 

 

**References** :

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amazon-s3/](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amazon-s3/)

 

 

**Check out this Amazon CloudFront Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

 

 

**S3 Pre-signed URLs vs CloudFront Signed URLs vs Origin Access Control (OAC)**

 

[https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/](https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/)

 

 

**Comparison of AWS Services Cheat Sheets:**

 

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

---

## Câu 73 — ✅ ĐÚNG

### Câu hỏi

A company runs a popular blogging platform that is hosted on AWS. Bloggers from all around the world upload millions of entries per month, and the average blog entry size is 300 KB. The access rate to blog entries drops to a negligible level six months after publishing and after a year, bloggers rarely access a blog. The blog entries have a high update rate during the first 3 months after the blogger has published it and this drops to no updates after 6 months. The company wants to use CloudFront to improve the load times of the blogging platform.



Which of the following is an ideal cloud implementation for this scenario?

### Các phương án

- **A.** Create two different CloudFront distributions: one with US-Europe price class for your US/Europe users and another one with all edge locations included for your remaining users.
- **B.** You can use one S3 source bucket that is partitioned according to the month a blog entry was submitted, and store the entry in that partition. Create a CloudFront distribution with access permissions to S3 and is restricted only to it.
- **C.** Store two copies of each entry in two different S3 buckets, and let each bucket have its own CloudFront distribution where S3 access is permitted to that CloudFront identity only.
- **D.** Create a CloudFront distribution and set the Restrict Viewer Access Forward Query string to true with a minimum TTL of 0.

> **Bạn chọn:** B
> **Đáp án đúng:** B

### Giải thích

Correct 

You can control how long your objects stay in a **CloudFront**  cache before CloudFront forwards another request to your origin. Reducing the duration allows you to serve dynamic content. Increasing the duration means your users get better performance because your objects are more likely to be served directly from the edge cache. A longer duration also reduces the load on your origin.

 

Typically, **CloudFront**  serves an object from an edge location until the cache duration that you specified passes—that is, until the object expires. After it expires, the next time the edge location gets a user request for the object, CloudFront forwards the request to the origin server to verify that the cache contains the latest version of the object.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_partitions.png)

 

Therefore, the correct answer is: **You can use one S3 source bucket that is partitioned according to the month a blog entry was submitted, and store the entry in that partition. Create a CloudFront distribution with access permissions to S3 and is restricted only to it.**  The content is only accessed by CloudFront, and if the content is partitioned at the origin based on the month it was uploaded, you can control the cache behavior accordingly and keep only the latest updated content in the CloudFront cache so that it can be accessed with fast load-time, hence, improving the performance.

 

The option that says: **Store two copies of each entry in two different S3 buckets, and letting each bucket have its own CloudFront distribution where S3 access is permitted to that CloudFront identity only**  is incorrect. Maintaining two separate buckets is not going to improve the load time for the users.

 

The option that says: **Create a CloudFront distribution and setting the Restrict Viewer Access Forward Query string to true with a minimum TTL of 0**  is incorrect. Setting minimum TTL of 0 will enforce loading of the content from origin every time, even if it has not been updated over 6 months.

 

The option that says: **Create two different CloudFront distributions: one with US-Europe price class for your US/Europe users and another one with all edge locations included for your remaining users**  is incorrect. The location-wise distribution is not going to improve the load time for the users.

 

 

**References** :

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)

 

 

**Check out this Amazon CloudFront Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

---

## Câu 74 — ✅ ĐÚNG

### Câu hỏi

A company runs a cryptocurrency analytics website and uses a CloudFront distribution with a custom domain name ([tutorialsdojo.com](http://tutorialsdojo.com/)) to speed up the loading time of the site. Since the data being distributed are quite confidential, the management instructed the solutions architect to require HTTPS communication between the viewers (web visitors) and the CloudFront distribution. Additionally, it is required to improve the performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers.



Which of the following are the recommended actions to accomplish the above requirement? (Select TWO.)

### Các phương án

- **A.** Use an SSL/TLS certificate provided by AWS Certificate Manager (ACM).
- **B.** Import an SSL/TLS certificate from a third-party certificate authority into a private S3 bucket with versioning and MFA enabled.
- **C.** Configure the CloudFront origin to add a `Cache-Control max-age directive` to your objects and specify the longest practical value for `max-age`.
- **D.** Associate your CloudFront web distribution with Lambda@Edge which provides automatic scalability from a few requests per day to thousands of requests per second.
- **E.** Integrate your CloudFront web distribution with Amazon OpenSearch to cache recent requests and improve the performance of your origin servers. Use Kibana to visualize the cache hit-ratio graph in real time.

> **Bạn chọn:** A, C
> **Đáp án đúng:** A, C

### Giải thích

Correct 

You can configure one or more cache behaviors in your **CloudFront**  distribution to require HTTPS for communication between viewers and CloudFront. You also can configure one or more cache behaviors to allow both HTTP and HTTPS so that CloudFront requires HTTPS for some objects but not for others. The configuration steps depend on which domain name you’re using in object URLs:

 

– If you’re using the domain name that CloudFront assigned to your distribution, such as d111111abcdef8.cloudfront.net, you change the Viewer Protocol Policy setting for one or more cache behaviors to require HTTPS communication. In that configuration, CloudFront provides the SSL/TLS certificate.

 

– If you’re using your own domain name, such as tutorialsdojo.com, you need to change several CloudFront settings. You also need to use an SSL/TLS certificate provided by AWS Certificate Manager (ACM), or import a certificate from a third-party certificate authority into ACM or the IAM certificate store.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_ssl.jpg)

 

You can improve performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers for content; that is, by improving the cache hit ratio for your distribution. To increase your cache hit ratio, you can configure your origin to add a **`Cache-Control max-age`** directive to your objects and specify the longest practical value for `**max-age** `. The shorter the cache duration, the more frequently CloudFront forwards another request to your origin to determine whether the object has changed and, if so, to get the latest version.

 

Therefore, the correct answers are:

 

**-Use an SSL/TLS certificate provided by AWS Certificate Manager (ACM)**

 

**-Configure the CloudFront origin to add a `Cache-Control max-age directive` to your objects and specifying the longest practical value for `max-age.`**

 

The option that says: **Associate your CloudFront web distribution with Lambda@Edge which provides automatic scalability from a few requests per day to thousands of requests per second**  is incorrect because Lambda@Edge is an extension of AWS Lambda which lets you execute functions that customize the content that CloudFront delivers. This feature does not improve the cache hit ratio of your CloudFront distribution.

 

The option that says: **Integrate your CloudFront web distribution with Amazon OpenSearch to cache recent requests and improve the performance of your origin servers. Use Kibana to visualize the cache hit-ratio graph in real time** is incorrect. Amazon OpenSearch service is used to perform interactive log analytics, real-time application monitoring, and more. This service will not improve the cache hit ratio of your CloudFront distribution. The built-in Kibana support only provides a way to get faster and better insights into your data and thus, not relevant to this scenario.

 

The option that says: **Import an SSL/TLS certificate from a third-party certificate authority into a private S3 bucket with versioning and MFA enabled**  is incorrect. For an SSL certificate, whether it is public or private, is not recommended to store it on an Amazon S3 bucket.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html)

 

 

**Check out this Amazon CloudFront Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

 

[https://tutorialsdojo.com/aws-certificate-manager/](https://tutorialsdojo.com/aws-certificate-manager/)

---

## Câu 75 — ✅ ĐÚNG

### Câu hỏi

A leading commercial bank has a hybrid cloud architecture and is using a Volume Gateway under the AWS Storage Gateway service to store their data via the Internet Small Computer Systems Interface (ISCSI). The security team has detected a series of replay attacks to your network, which is basically a form of network attack in which a valid data transmission is maliciously or fraudulently repeated or delayed. After their investigation, they detected that the originator of the attack is trying to intercept the data with an intention to re-transmit it, which is possibly part of a masquerade attack by IP packet substitution.



As a Solutions Architect of the bank, how can you secure your AWS Storage Gateway from these types of attacks?

### Các phương án

- **A.** Replace the current ISCSI Block Interface with an ISCSI Virtual Tape Library Interface.
- **B.** Replace ISCSI with more secure protocols like Common Internet File System (CIFS) Protocol or Server Message Block (SMB).
- **C.** Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSI and initiator connections.
- **D.** Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate NFS connections and safeguard your network from replay attacks.

> **Bạn chọn:** C
> **Đáp án đúng:** C

### Giải thích

Correct 

In **AWS Storage Gatewa** y, your iSCSI initiators connect to your volumes as iSCSI targets. Storage Gateway uses Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSI and initiator connections. CHAP provides protection against playback attacks by requiring authentication to access storage volume targets. For each volume target, you can define one or more CHAP credentials. You can view and edit these credentials for the different initiators in the Configure CHAP credentials dialog box.

 

![image](https://media.tutorialsdojo.com/sap_storage_gateway_stored.png)

 

Therefore the correct answer is: **Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSl and initiator connections** .

 

The option that says: **Replace lSCSl with more secure protocols like Common Internet File System (CIFS) Protocol or Server Message Block (SMB)**  is incorrect. Replacing ISCSI with CIFS and SMB would be irrelevant since these two do not provide the required security mechanism in the scenario. It is best to use Challenge-Handshake Authentication Protocol (CHAP) instead.

 

The option that says: **Replace the current lSCSl Block Interface with an lSCSl Virtual Tape Library Interface** is incorrect. ISCSI Virtual Tape Library Interface is primarily used for Tape Gateways and not for Volume Gateways. It is better to use Challenge-Handshake Authentication Protocol (CHAP) instead.

 

The option that says: **Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate NFS connections and safeguard your network from replay attacks** is incorrect. CHAP is primarily used to authenticate iSCSI and not NFS.

 

 

**References:**

 

[https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedConfigureChap.html](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedConfigureChap.html)

 

[https://docs.aws.amazon.com/storagegateway/latest/vgw/initiator-connection-common.html](https://docs.aws.amazon.com/storagegateway/latest/vgw/initiator-connection-common.html)

 

 

**Check out this AWS Storage Gateway Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-storage-gateway/](https://tutorialsdojo.com/aws-storage-gateway/)

---
