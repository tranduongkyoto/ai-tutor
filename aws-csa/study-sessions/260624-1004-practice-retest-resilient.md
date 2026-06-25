# Practice Exam Re-Test — Design Resilient Architectures

**Date:** 2026-06-24 | **Questions:** 10 | **Source:** Udemy Practice Exams 1 & 2
**Status:** IN_PROGRESS | **Score:** _/10

---

## Q1/10 [Exam 1 - Q43] (Select 2)

**The DevOps team at an e-commerce company wants to perform some maintenance work on a specific Amazon EC2 instance that is part of an Auto Scaling group using a step scaling policy. The team is facing a maintenance challenge - every time the team deploys a maintenance patch, the instance health check status shows as out of service for a few minutes. This causes the Auto Scaling group to provision another replacement instance immediately. As a solutions architect, which are the MOST time/resource efficient steps that you would recommend so that the maintenance work can be completed at the earliest? (Select two)**

A) Delete the Auto Scaling group and apply the maintenance fix to the given instance. Create a new Auto Scaling group and add all the instances again using the manual scaling policy

B) Suspend the ScheduledActions process type for the Auto Scaling group and apply the maintenance patch to the instance. Once the instance is ready, you can you can manually set the instance's health status back to healthy and activate the ScheduledActions process type again

C) Put the instance into the Standby state and then update the instance by applying the maintenance patch. Once the instance is ready, you can exit the Standby state and then return the instance to service

D) Take a snapshot of the instance, create a new Amazon Machine Image (AMI) and then launch a new instance using this AMI. Apply the maintenance patch to this new instance and then add it back to the Auto Scaling Group by using the manual scaling policy. Terminate the earlier instance that had the maintenance issue

E) Suspend the ReplaceUnhealthy process type for the Auto Scaling group and apply the maintenance patch to the instance. Once the instance is ready, you can manually set the instance's health status back to healthy and activate the ReplaceUnhealthy process type again

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** C, E
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q2/10 [Exam 1 - Q48]

**A new DevOps engineer has just joined a development team and wants to understand the replication capabilities for Amazon RDS Multi-AZ deployment as well as Amazon RDS Read-replicas. Which of the following correctly summarizes these capabilities for the given database?**

A) Multi-AZ follows synchronous replication and spans at least two Availability Zones (AZs) within a single region. Read replicas follow asynchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region

B) Multi-AZ follows asynchronous replication and spans one Availability Zone (AZ) within a single region. Read replicas follow synchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region

C) Multi-AZ follows asynchronous replication and spans at least two Availability Zones (AZs) within a single region. Read replicas follow synchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region

D) Multi-AZ follows asynchronous replication and spans at least two Availability Zones (AZs) within a single region. Read replicas follow asynchronous replication and can be within an Availability Zone (AZ), Cross-AZ, or Cross-Region

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q3/10 [Exam 1 - Q55]

**A government agency is developing a online application to assist users in submitting permit requests through a web-based interface. The system architecture consists of a front-end web application tier and a background processing tier that handles the validation and submission of the forms. The application is expected to see high traffic and it must ensure that every submitted request is processed exactly once, with no loss of data. Which design choice best satisfies these requirements?**

A) Implement an Amazon SQS standard queue to reliably buffer and deliver form submissions from the web application layer to the processing tier

B) Leverage Amazon EventBridge to send events from the web application to the processing tier for asynchronous form handling

C) Implement an Amazon SQS FIFO queue to reliably buffer and deliver form submissions from the web application layer to the processing tier

D) Leverage Amazon API Gateway to pass the form submissions to AWS Lambda for processing in real time

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** C
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q4/10 [Exam 1 - Q60]

**An e-commerce company is looking for a solution with high availability, as it plans to migrate its flagship application to a fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances. The solution should allow for content-based routing as part of the architecture. As a Solutions Architect, which of the following will you suggest for the company?**

A) Use an Auto Scaling group for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure a Public IP address to mask any failure of an instance

B) Use an Auto Scaling group for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure an elastic IP address (EIP) to mask any failure of an instance

C) Use an Application Load Balancer for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure Auto Scaling group to mask any failure of an instance

D) Use a Network Load Balancer for distributing traffic to the Amazon EC2 instances spread across different Availability Zones (AZs). Configure a Private IP address to mask any failure of an instance

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** C
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q5/10 [Exam 1 - Q62]

**A biotech research company needs to perform data analytics on real-time lab results provided by a partner organization. The partner stores these lab results in an Amazon RDS for MySQL instance within the partner’s own AWS account. The research company has a private VPC that does not have internet access, Direct Connect, or a VPN connection. However, the company must establish secure and private connectivity to the RDS database in the partner’s VPC. The solution must allow the research company to connect from its VPC while minimizing complexity and complying with data security requirements. Which solution will meet these requirements?**

A) Set up VPC peering between the company’s VPC and the partner’s VPC. Use AWS Transit Gateway in the partner's account to route traffic from the company’s VPC to the database. Modify the RDS subnet route tables to allow access from the company’s CIDR block

B) Instruct the partner to create a Network Load Balancer (NLB) in front of the Amazon RDS for MySQL instance. Use AWS PrivateLink to expose the NLB as an interface VPC endpoint in the research company’s VPC

C) Configure a client VPN endpoint in the company’s account. Have researchers connect to the VPN from their local machines. Establish a Direct Connect gateway to the partner’s VPC and route RDS traffic via this connection

D) Instruct the partner to enable public access on the Amazon RDS instance and add a security group rule to allow inbound access from the company’s IP range. The company accesses the database over the public internet through a NAT Gateway configured in a private subnet

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** B
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q6/10 [Exam 1 - Q65] (Select 2)

**The DevOps team at an e-commerce company has deployed a fleet of Amazon EC2 instances under an Auto Scaling group (ASG). The instances under the ASG span two Availability Zones (AZ) within the us-east-1 region. All the incoming requests are handled by an Application Load Balancer (ALB) that routes the requests to the Amazon EC2 instances under the Auto Scaling Group. As part of a test run, two instances (instance 1 and 2, belonging to AZ A) were manually terminated by the DevOps team causing the Availability Zones (AZ) to have unbalanced resources. Later that day, another instance (belonging to AZ B) was detected as unhealthy by the Application Load Balancer's health check. Can you identify the correct outcomes for these events? (Select two)**

A) Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously

B) As the resources are unbalanced in the Availability Zones, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application

C) Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it

D) As the resources are unbalanced in the Availability Zones, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched

E) Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** B, E
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q7/10 [Exam 2 - Q10]

**A media company is migrating its flagship application from its on-premises data center to AWS for improving the application's read-scaling capability as well as its availability. The existing architecture leverages a Microsoft SQL Server database that sees a heavy read load. The engineering team does a full copy of the production database at the start of the business day to populate a dev database. During this period, application users face high latency leading to a bad user experience. The company is looking at alternate database options and migrating database engines if required. What would you suggest?**

A) Leverage Amazon RDS for MySQL with a Multi-AZ deployment and use the standby instance as the dev database

B) Leverage Amazon Aurora MySQL with Multi-AZ Aurora Replicas and create the dev database by restoring from the automated backups of Amazon Aurora

C) Leverage Amazon Aurora MySQL with Multi-AZ Aurora Replicas and restore the dev database via mysqldump

D) Leverage Amazon RDS for SQL server with a Multi-AZ deployment and read replicas. Use the read replica as the dev database

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** B
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q8/10 [Exam 2 - Q33]

**A company has recently launched a new mobile gaming application that the users are adopting rapidly. The company uses Amazon RDS MySQL as the database. The engineering team wants an urgent solution to this issue where the rapidly increasing workload might exceed the available database storage. As a solutions architect, which of the following solutions would you recommend so that it requires minimum development and systems administration effort to address this requirement?**

A) Create read replica for Amazon RDS MySQL

B) Migrate RDS MySQL database to Amazon Aurora which offers storage auto-scaling

C) Enable storage auto-scaling for Amazon RDS MySQL

D) Migrate Amazon RDS MySQL database to Amazon DynamoDB which automatically allocates storage space when required

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** C
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q9/10 [Exam 2 - Q34] (Select 3)

**The engineering team at a logistics company has noticed that the Auto Scaling group (ASG) is not terminating an unhealthy Amazon EC2 instance. As a Solutions Architect, which of the following options would you suggest to troubleshoot the issue? (Select three)**

A) The health check grace period for the instance has not expired

B) The instance maybe in Impaired status

C) A custom health check might have failed. The Auto Scaling group (ASG) does not terminate instances that are set unhealthy by custom checks

D) A user might have updated the configuration of the Auto Scaling group (ASG) and increased the minimum number of instances forcing ASG to keep all instances alive

E) The Amazon EC2 instance could be a spot instance type, which cannot be terminated by the Auto Scaling group (ASG)

F) The instance has failed the Elastic Load Balancing (ELB) health check status

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A, B, F
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q10/10 [Exam 2 - Q61]

**The DevOps team at a major financial services company uses Multi-Availability Zone (Multi-AZ) deployment for its MySQL Amazon RDS database in order to automate its database replication and augment data durability. The DevOps team has scheduled a maintenance window for a database engine level upgrade for the coming weekend. Which of the following is the correct outcome during the maintenance window?**

A) Any database engine level upgrade for an Amazon RDS database instance with Multi-AZ deployment triggers both the primary and standby database instances to be upgraded at the same time. This causes downtime until the upgrade is complete

B) Any database engine level upgrade for an Amazon RDS database instance with Multi-AZ deployment triggers the primary database instance to be upgraded which is then followed by the upgrade of the standby database instance. This does not cause any downtime for the duration of the upgrade

C) Any database engine level upgrade for an Amazon RDS database instance with Multi-AZ deployment triggers the standby database instance to be upgraded which is then followed by the upgrade of the primary database instance. This does not cause any downtime for the duration of the upgrade

D) Any database engine level upgrade for an Amazon RDS database instance with Multi-AZ deployment triggers both the primary and standby database instances to be upgraded at the same time. However, this does not cause any downtime until the upgrade is complete

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 10 |
| Correct | _ |
| Wrong | _ |
| Score | _% |
| Improvement | _ |