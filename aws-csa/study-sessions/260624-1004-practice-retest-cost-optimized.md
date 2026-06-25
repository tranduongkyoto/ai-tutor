# Practice Exam Re-Test — Design Cost-Optimized Architectures

**Date:** 2026-06-24 | **Questions:** 8 | **Source:** Udemy Practice Exams 1 & 2
**Status:** IN_PROGRESS | **Score:** _/8

---

## Q1/8 [Exam 1 - Q7]

**A media agency stores its re-creatable assets on Amazon Simple Storage Service (Amazon S3) buckets. The assets are accessed by a large number of users for the first few days and the frequency of access falls down drastically after a week. Although the assets would be accessed occasionally after the first week, but they must continue to be immediately accessible when required. The cost of maintaining all the assets on Amazon S3 storage is turning out to be very expensive and the agency is looking at reducing costs as much as possible. As an AWS Certified Solutions Architect – Associate, can you suggest a way to lower the storage costs while fulfilling the business requirements?**

A) Configure a lifecycle policy to transition the objects to Amazon S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days

B) Configure a lifecycle policy to transition the objects to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days

C) Configure a lifecycle policy to transition the objects to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) after 7 days

D) Configure a lifecycle policy to transition the objects to Amazon S3 Standard-Infrequent Access (S3 Standard-IA) after 7 days

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** B
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q2/8 [Exam 1 - Q35]

**A leading video streaming service delivers billions of hours of content from Amazon Simple Storage Service (Amazon S3) to customers around the world. Amazon S3 also serves as the data lake for its big data analytics solution. The data lake has a staging zone where intermediary query results are kept only for 24 hours. These results are also heavily referenced by other parts of the analytics pipeline. Which of the following is the MOST cost-effective strategy for storing this intermediary query data?**

A) Store the intermediary query results in Amazon S3 One Zone-Infrequent Access storage class

B) Store the intermediary query results in Amazon S3 Glacier Instant Retrieval storage class

C) Store the intermediary query results in Amazon S3 Standard storage class

D) Store the intermediary query results in Amazon S3 Standard-Infrequent Access storage class

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** C
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q3/8 [Exam 1 - Q50]

**A technology blogger wants to write a review on the comparative pricing for various storage types available on AWS Cloud. The blogger has created a test file of size 1 gigabytes with some random data. Next he copies this test file into AWS S3 Standard storage class, provisions an Amazon EBS volume (General Purpose SSD (gp2)) with 100 gigabytes of provisioned storage and copies the test file into the Amazon EBS volume, and lastly copies the test file into an Amazon EFS Standard Storage filesystem. At the end of the month, he analyses the bill for costs incurred on the respective storage types for the test file. What is the correct order of the storage charges incurred for the test file on these three storage types?**

A) Cost of test file storage on Amazon EFS &lt; Cost of test file storage on Amazon S3 Standard &lt; Cost of test file storage on Amazon EBS

B) Cost of test file storage on Amazon S3 Standard &lt; Cost of test file storage on Amazon EFS &lt; Cost of test file storage on Amazon EBS

C) Cost of test file storage on Amazon S3 Standard &lt; Cost of test file storage on Amazon EBS &lt; Cost of test file storage on Amazon EFS

D) Cost of test file storage on Amazon EBS &lt; Cost of test file storage on Amazon S3 Standard &lt; Cost of test file storage on Amazon EFS

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** B
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q4/8 [Exam 2 - Q27]

**You would like to use AWS Snowball to move on-premises backups into a long term archival tier on AWS. Which solution provides the MOST cost savings?**

A) Create a AWS Snowball job and target an Amazon S3 Glacier Deep Archive Vault

B) Create an AWS Snowball job and target a Amazon S3 Glacier Vault

C) Create an AWS Snowball job and target an Amazon S3 bucket. Create a lifecycle policy to transition this data to Amazon S3 Glacier on the same day

D) Create an AWS Snowball job and target an Amazon S3 bucket. Create a lifecycle policy to transition this data to Amazon S3 Glacier Deep Archive on the same day

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q5/8 [Exam 2 - Q35]

**You have multiple AWS accounts within a single AWS Region managed by AWS Organizations and you would like to ensure all Amazon EC2 instances in all these accounts can communicate privately. Which of the following solutions provides the capability at the CHEAPEST cost?**

A) Create a Private Link between all the Amazon EC2 instances

B) Create a VPC peering connection between all virtual private cloud (VPCs)

C) Create a virtual private cloud (VPC) in an account and share one or more of its subnets with the other accounts using Resource Access Manager

D) Create an AWS Transit Gateway and link all the virtual private cloud (VPCs) in all the accounts together

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** C
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q6/8 [Exam 2 - Q45]

**Amazon EC2 Auto Scaling needs to terminate an instance from Availability Zone (AZ) us-east-1a as it has the most number of instances amongst the Availability Zone (AZs) being used currently. There are 4 instances in the Availability Zone (AZ) us-east-1a like so: Instance A has the oldest launch template, Instance B has the oldest launch configuration, Instance C has the newest launch configuration and Instance D is closest to the next billing hour. Which of the following instances would be terminated per the default termination policy?**

A) Instance A

B) Instance D

C) Instance C

D) Instance B

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q7/8 [Exam 2 - Q46]

**An application is currently hosted on four Amazon EC2 instances (behind Application Load Balancer) deployed in a single Availability Zone (AZ). To maintain an acceptable level of end-user experience, the application needs at least 4 instances to be always available. As a solutions architect, which of the following would you recommend so that the application achieves high availability with MINIMUM cost?**

A) Deploy the instances in three Availability Zones (AZs). Launch two instances in each Availability Zone (AZ)

B) Deploy the instances in two Availability Zones (AZs). Launch two instances in each Availability Zone (AZ)

C) Deploy the instances in two Availability Zones (AZs). Launch four instances in each Availability Zone (AZ)

D) Deploy the instances in one Availability Zones. Launch two instances in the Availability Zone (AZ)

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Q8/8 [Exam 2 - Q47]

**Your company has a monthly big data workload, running for about 2 hours, which can be efficiently distributed across multiple servers of various sizes, with a variable number of CPUs. The solution for the workload should be able to withstand server failures. Which is the MOST cost-optimal solution for this workload?**

A) Run the workload on Reserved Instances (RI)

B) Run the workload on Spot Instances

C) Run the workload on Dedicated Hosts

D) Run the workload on a Spot Fleet

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** ____
**Result:** [ ] CORRECT  [ ] WRONG
**Explanation:**

---

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 8 |
| Correct | _ |
| Wrong | _ |
| Score | _% |
| Improvement | _ |