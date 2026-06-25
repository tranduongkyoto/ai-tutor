# Practice Exam Re-Test — Design Secure Architectures

**Date:** 2026-06-24 | **Questions:** 20 | **Source:** Udemy Practice Exams 1 & 2
**Status:** IN_PROGRESS | **Score:** 17/20 | **Correct:** 17 | **Wrong:** 3 | **Progress:** COMPLETE (85%)

---

## Q1/20 [Exam 1 - Q1]

**An enterprise runs a microservices-based application on Amazon EKS, deployed on EC2 worker nodes. The application includes a frontend UI service that interacts with Amazon DynamoDB and a data-processing service that stores and retrieves files from Amazon S3. The organization needs to strictly enforce least privilege access: the UI Pods must access only DynamoDB, and the data-processing Pods must access only S3. Which solution will best enforce these access controls within the EKS cluster?**

A) Create separate Kubernetes service accounts for the UI and data services. Use IAM Roles for Service Accounts (IRSA) to map each service account to an IAM role with only the required permissions. Assign DynamoDB access to the UI Pods and S3 access to the data Pods

B) Attach an IAM policy directly to each Pod using Kubernetes annotations. Assign the S3 policy to data-service Pods and the DynamoDB policy to UI Pods

C) Create IAM policies for DynamoDB and S3 access, and attach both to the EC2 instance profile used by the EKS nodes. Use Kubernetes role-based access control (RBAC) to control service-level permissions within the cluster

D) Create one Kubernetes service account shared across all Pods. Attach a single IAM role to this account with both AmazonS3FullAccess and AmazonDynamoDBFullAccess policies

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A
</details>

**Re-test answer:** B (IRSA)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** IRSA maps each K8s service account to a scoped IAM role via OIDC+STS. Pod-level least privilege without sharing instance profile. RBAC only controls K8s API, not AWS permissions. Separate node groups work but wasteful. Storing IAM keys in Secrets Manager is anti-pattern vs temp credentials.

---

## Q2/20 [Exam 1 - Q14]

**A financial services company operates a containerized microservices architecture using Kubernetes in its on-premises data center. Due to strict industry regulations and internal security policies, all application data and workloads must remain physically within the on-premises environment. The company’s infrastructure team wants to modernize its Kubernetes stack and take advantage of AWS-managed services and APIs, including automated Kubernetes upgrades, Amazon CloudWatch integration, and access to AWS IAM features — but without migrating any data or compute resources to the cloud. Which AWS solution will best meet the company’s requirements for modernization while ensuring that all data remains on premises?**

A) Deploy Amazon ECS with Fargate in a nearby AWS Local Zone. Use CloudWatch Logs to forward events to the primary region. Connect the Local Zone to the company’s data center over a VPN. Configure containers to pull data from on-premises storage through a mounted file share

B) Set up a dedicated AWS Direct Connect connection between the on-premises environment and an AWS Region. Deploy Amazon EKS in the cloud and connect it to the local Kubernetes cluster. Use IAM roles and API Gateway to integrate authentication and traffic flow for hybrid workloads

C) Use an AWS Snowball Edge Compute Optimized device to run EKS-compatible Docker containers on-site. Periodically export application logs and container snapshots to Amazon S3 using Snowball’s offline data transfer features. Use the Snowball console to orchestrate workloads in batches

D) Install an AWS Outposts rack in the company’s data center. Use Amazon EKS Anywhere on Outposts to run containerized workloads locally while integrating with AWS APIs

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** D
</details>

**Re-test answer:** D (Outposts + EKS Anywhere)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Outposts extends AWS infra into your DC — data stays on-prem. EKS Anywhere provides managed K8s + CloudWatch/IAM. Local Zones are AWS-operated (not your DC). Direct Connect+cloud EKS = data in cloud. Snowball is for offline/disconnected edge, no live AWS integration.

---

## Q3/20 [Exam 1 - Q17] (Select 2)

**A company uses Amazon S3 buckets for storing sensitive customer data. The company has defined different retention periods for different objects present in the Amazon S3 buckets, based on the compliance requirements. But, the retention rules do not seem to work as expected. Which of the following options represent a valid configuration for setting up retention periods for objects in Amazon S3 buckets? (Select two)**

A) You cannot place a retention period on an object version through a bucket default setting

B) Different versions of a single object can have different retention modes and periods

C) When you use bucket default settings, you specify a Retain Until Date for the object version

D) When you apply a retention period to an object version explicitly, you specify a Retain Until Date for the object version

E) The bucket default settings will override any explicit retention mode or period you request on an object version

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** B, D
</details>

**Re-test answer:** B + C (WRONG — correct is B + D)
**Result:** [ ] CORRECT  [x] WRONG
**Explanation:** B correct: versions independently lockable with different modes/periods. D correct: explicit retention uses a specific Retain Until Date. C wrong: bucket DEFAULTS use duration (e.g. 30 days), NOT a specific date — date is auto-calculated from upload time. E wrong: explicit overrides defaults. A wrong: you CAN set retention via bucket defaults.

---

## Q4/20 [Exam 1 - Q18]

**An organization wants to delegate access to a set of users from the development environment so that they can access some resources in the production environment which is managed under another AWS account. As a solutions architect, which of the following steps would you recommend?**

A) Create new IAM user credentials for the production environment and share these credentials with the set of users from the development environment

B) It is not possible to access cross-account resources

C) Both IAM roles and IAM users can be used interchangeably for cross-account access

D) Create a new IAM role with the required permissions to access the resources in the production environment. The users can then assume this IAM role while accessing the resources from the production environment

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** D
</details>

**Re-test answer:** B (IAM role in prod, assume via STS)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Cross-account: create role in target account + trust policy for source. Users call sts:AssumeRole for temp credentials. Roles/users NOT interchangeable (roles=temp, users=permanent). Sharing credentials = anti-pattern.

---

## Q5/20 [Exam 1 - Q27]

**A media company runs a photo-sharing web application that is accessed across three different countries. The application is deployed on several Amazon Elastic Compute Cloud (Amazon EC2) instances running behind an Application Load Balancer. With new government regulations, the company has been asked to block access from two countries and allow access only from the home country of the company. Which configuration should be used to meet this changed requirement?**

A) Configure the security group on the Application Load Balancer

B) Configure the security group for the Amazon EC2 instances

C) Use Geo Restriction feature of Amazon CloudFront in a Amazon Virtual Private Cloud (Amazon VPC)

D) Configure AWS Web Application Firewall (AWS WAF) on the Application Load Balancer in a Amazon Virtual Private Cloud (Amazon VPC)

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** D
</details>

**Re-test answer:** C (WAF on ALB with geo match)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** WAF supports geo match conditions, attaches directly to ALB. CloudFront Geo Restriction only works on CF distributions, not ALB. SGs filter by IP/CIDR, not country. Route 53 geolocation routes traffic but doesn't block access.

---

## Q6/20 [Exam 1 - Q32] (Select 2)

**A healthcare startup needs to enforce compliance and regulatory guidelines for objects stored in Amazon S3. One of the key requirements is to provide adequate protection against accidental deletion of objects. As a solutions architect, what are your recommendations to address these guidelines? (Select two) ?**

A) Create an event trigger on deleting any Amazon S3 object. The event invokes an Amazon Simple Notification Service (Amazon SNS) notification via email to the IT manager

B) Enable multi-factor authentication (MFA) delete on the Amazon S3 bucket

C) Enable versioning on the Amazon S3 bucket

D) Change the configuration on Amazon S3 console so that the user needs to provide additional confirmation while deleting any Amazon S3 object

E) Establish a process to get managerial approval for deleting Amazon S3 objects

<details>
<summary>Original Result</summary>

- **Your answer:** E
- **Correct answer:** B, C
</details>

**Re-test answer:** C + D (WRONG — correct is B + C)
**Result:** [ ] CORRECT  [x] WRONG
**Explanation:** B correct: MFA Delete requires MFA code to permanently delete versions. C correct: versioning makes "delete" just a delete marker, data recoverable. D wrong: no such S3 console confirmation feature — fabricated option. A wrong: SNS notifies but doesn't prevent. E wrong: manual process, not AWS control.

---

## Q7/20 [Exam 1 - Q39] (Select 2)

**A company has moved its business critical data to Amazon Elastic File System (Amazon EFS) which will be accessed by multiple Amazon EC2 instances. As an AWS Certified Solutions Architect - Associate, which of the following would you recommend to exercise access control such that only the permitted Amazon EC2 instances can read from the Amazon EFS file system? (Select two)**

A) Use VPC security groups to control the network traffic to and from your file system

B) Use network access control list (network ACL) to control the network traffic to and from your Amazon EC2 instance

C) Use Amazon GuardDuty to curb unwanted access to Amazon EFS file system

D) Set up the IAM policy root credentials to control and configure the clients accessing the Amazon EFS file system

E) Use an IAM policy to control access for clients who can mount your file system with the required permissions

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** A, E
</details>

**Re-test answer:** A + B (WRONG — correct is A + E)
**Result:** [ ] CORRECT  [x] WRONG
**Explanation:** A correct: EFS mount targets have SGs — control network access per instance on port 2049. E correct: EFS IAM authorization controls who can mount + permissions. B wrong: NACLs are subnet-level, can't distinguish individual instances. C wrong: GuardDuty detects threats, doesn't control access. D wrong: root credentials = anti-pattern. EFS access = SG (network) + IAM (identity).

---

## Q8/20 [Exam 2 - Q2]

**An IT company has built a solution wherein an Amazon Redshift cluster writes data to an Amazon S3 bucket belonging to a different AWS account. However, it is found that the files created in the Amazon S3 bucket using the UNLOAD command from the Amazon Redshift cluster are not even accessible to the Amazon S3 bucket owner. What could be the reason for this denial of permission for the bucket owner?**

A) By default, an Amazon S3 object is owned by the AWS account that uploaded it. So the Amazon S3 bucket owner will not implicitly have access to the objects written by the Amazon Redshift cluster

B) When objects are uploaded to Amazon S3 bucket from a different AWS account, the S3 bucket owner will get implicit permissions to access these objects. This issue seems to be due to an upload error that can be fixed by providing manual access from AWS console

C) When two different AWS accounts are accessing an Amazon S3 bucket, both the accounts must share the bucket policies. An erroneous policy can lead to such permission failures

D) The owner of an Amazon S3 bucket has implicit access to all objects in his bucket. Permissions are set on objects after they are completely copied to the target location. Since the owner is unable to access the uploaded files, the write operation may be still in progress

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A
</details>

**Re-test answer:** A (Object owned by uploader)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** S3 objects owned by uploading account by default. Bucket owner has no implicit access to cross-account uploads. Fix: bucket-owner-full-control ACL or S3 Object Ownership setting. Not a policy sharing issue — it's ownership semantics.

---

## Q9/20 [Exam 2 - Q6]

**A financial services company has deployed its flagship application on Amazon EC2 instances. Since the application handles sensitive customer data, the security team at the company wants to ensure that any third-party Secure Sockets Layer certificate (SSL certificate) SSL/Transport Layer Security (TLS) certificates configured on Amazon EC2 instances via the AWS Certificate Manager (ACM) are renewed before their expiry date. The company has hired you as an AWS Certified Solutions Architect Associate to build a solution that notifies the security team 30 days before the certificate expiration. The solution should require the least amount of scripting and maintenance effort. What will you recommend?**

A) Monitor the days to expiry Amazon CloudWatch metric for certificates imported into ACM. Create a CloudWatch alarm to monitor such certificates based on the days to expiry metric and then trigger a custom action of notifying the security team

B) Monitor the days to expiry Amazon CloudWatch metric for certificates created via ACM. Create a CloudWatch alarm to monitor such certificates based on the days to expiry metric and then trigger a custom action of notifying the security team

C) Leverage AWS Config managed rule to check if any third-party SSL/TLS certificates imported into ACM are marked for expiration within 30 days. Configure the rule to trigger an Amazon SNS notification to the security team if any certificate expires within 30 days

D) Leverage AWS Config managed rule to check if any SSL/TLS certificates created via ACM are marked for expiration within 30 days. Configure the rule to trigger an Amazon SNS notification to the security team if any certificate expires within 30 days

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** C
</details>

**Re-test answer:** C (Config rule for imported certs + SNS)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Third-party = imported certs (no auto-renew). Config managed rule `acm-certificate-expiration-check` is out-of-box, least effort. ACM-issued certs auto-renew, no monitoring needed. CloudWatch works but more config effort than Config rule.

---

## Q10/20 [Exam 2 - Q12]

**A security consultant is designing a solution for a company that wants to provide developers with individual AWS accounts through AWS Organizations, while also maintaining standard security controls. Since the individual developers will have AWS account root user-level access to their own accounts, the consultant wants to ensure that the mandatory AWS CloudTrail configuration that is applied to new developer accounts is not modified. Which of the following actions meets the given requirements?**

A) Set up an IAM policy that prohibits changes to AWS CloudTrail and attach it to the root user

B) Set up a service control policy (SCP) that prohibits changes to AWS CloudTrail, and attach it to the developer accounts

C) Configure a new trail in AWS CloudTrail from within the developer accounts with the organization trails option enabled

D) Set up a service-linked role for AWS CloudTrail with a policy condition that allows changes only from an Amazon Resource Name (ARN) in the master account

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** B
</details>

**Re-test answer:** B (SCP on developer accounts)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** SCP overrides even root permissions in member accounts. IAM on root can be self-removed. Organization Trails don't prevent modification. Service-linked roles don't restrict CloudTrail changes.

---

## Q11/20 [Exam 2 - Q16]

**A financial services company wants to store confidential data in Amazon S3 and it needs to meet the following data security and compliance norms: Which is the MOST operationally efficient solution?**

A) Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) with manual key rotation

B) Server-side encryption with customer-provided keys (SSE-C) with automatic key rotation

C) Server-side encryption (SSE-S3) with automatic key rotation

D) Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) with automatic key rotation

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** D (SSE-KMS with automatic rotation)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** SSE-KMS = audit trail via CloudTrail + customer key control. Automatic rotation = zero ops effort. Manual = more work. SSE-C = you manage everything. SSE-S3 = no audit trail, no key control for compliance.

---

## Q12/20 [Exam 2 - Q18]

**You have a team of developers in your company, and you would like to ensure they can quickly experiment with AWS Managed Policies by attaching them to their accounts, but you would like to prevent them from doing an escalation of privileges, by granting themselves the AdministratorAccess managed policy. How should you proceed?**

A) For each developer, define an IAM permission boundary that will restrict the managed policies they can attach to themselves

B) Attach an IAM policy to your developers, that prevents them from attaching the AdministratorAccess policy

C) Create a Service Control Policy (SCP) on your AWS account that restricts developers from attaching themselves the AdministratorAccess policy

D) Put the developers into an IAM group, and then define an IAM permission boundary on the group that will restrict the managed policies they can attach to themselves

<details>
<summary>Original Result</summary>

- **Your answer:** C
- **Correct answer:** A
</details>

**Re-test answer:** A (Permission boundary per developer)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Permission boundary = max permissions cap per user/role. Effective = Policy ∩ Boundary. SCP needs Organizations (not mentioned). Boundaries can't attach to groups — only users/roles. Deny policy can be self-removed by developer.

---

## Q13/20 [Exam 2 - Q19]

**A social media application is hosted on an Amazon EC2 fleet running behind an Application Load Balancer. The application traffic is fronted by an Amazon CloudFront distribution. The engineering team wants to decouple the user authentication process for the application, so that the application servers can just focus on the business logic. As a Solutions Architect, which of the following solutions would you recommend to the development team so that it requires minimal development effort?**

A) Use Amazon Cognito Authentication via Cognito Identity Pools for your Application Load Balancer

B) Use Amazon Cognito Authentication via Cognito User Pools for your Amazon CloudFront distribution

C) Use Amazon Cognito Authentication via Cognito User Pools for your Application Load Balancer

D) Use Amazon Cognito Authentication via Cognito Identity Pools for your Amazon CloudFront distribution

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** C
</details>

**Re-test answer:** C (User Pools on ALB)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** ALB natively integrates with Cognito User Pools — built-in auth on listener rule. User Pools = authentication (JWT). Identity Pools = AWS credential vending. CloudFront has no native User Pools integration.

---

## Q14/20 [Exam 2 - Q22]

**An e-commerce company operates multiple AWS accounts and has interconnected these accounts in a hub-and-spoke style using the AWS Transit Gateway. Amazon Virtual Private Cloud (Amazon VPCs) have been provisioned across these AWS accounts to facilitate network isolation. Which of the following solutions would reduce both the administrative overhead and the costs while providing shared access to services required by workloads in each of the VPCs?**

A) Build a shared services Amazon Virtual Private Cloud (Amazon VPC)

B) Use Fully meshed VPC Peering connection

C) Use VPCs connected with AWS Direct Connect

D) Use Transit VPC to reduce cost and share the resources across Amazon Virtual Private Cloud (Amazon VPCs)

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** A
</details>

**Re-test answer:** A (Shared services VPC)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Shared services VPC centralizes common resources, spoke VPCs access via existing TGW. Meshed peering doesn't scale. Direct Connect is on-prem↔AWS. Transit VPC is legacy, replaced by TGW.

---

## Q15/20 [Exam 2 - Q23]

**A retail company wants to share sensitive accounting data that is stored in an Amazon RDS database instance with an external auditor. The auditor has its own AWS account and needs its own copy of the database. Which of the following would you recommend to securely share the database with the auditor?**

A) Export the database contents to text files, store the files in Amazon S3, and create a new IAM user for the auditor with access to that bucket

B) Create a snapshot of the database in Amazon S3 and assign an IAM role to the auditor to grant access to the object in that bucket

C) Create an encrypted snapshot of the database, share the snapshot, and allow access to the AWS Key Management Service (AWS KMS) encryption key

D) Set up a read replica of the database and configure IAM standard database authentication to grant the auditor access

<details>
<summary>Original Result</summary>

- **Your answer:** D
- **Correct answer:** C
</details>

**Re-test answer:** C (Encrypted snapshot + share KMS key)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** RDS snapshots shared cross-account = own copy. KMS key access needed to decrypt. Export to text isn't a DB copy. Snapshots aren't in S3. Read replica gives live access, not independent copy — security risk for external auditor.

---

## Q16/20 [Exam 2 - Q31]

**Consider the following policy associated with an IAM group containing several users: { "Version":"2012-10-17", "Id":"EC2TerminationPolicy", "Statement":[ { "Effect":"Deny", "Action":"ec2:*", "Resource":"*", "Condition":{ "StringNotEquals":{ "ec2:Region":"us-west-1" } } }, { "Effect":"Allow", "Action":"ec2:TerminateInstances", "Resource":"*", "Condition":{ "IpAddress":{ "aws:SourceIp":"10.200.200.0/24" } } } ] } Which of the following options is correct?**

A) Users belonging to the IAM user group can terminate an Amazon EC2 instance in the us-west-1 region when the EC2 instance's IP address is 10.200.200.200

B) Users belonging to the IAM user group cannot terminate an Amazon EC2 instance in the us-west-1 region when the user's source IP is 10.200.200.200

C) Users belonging to the IAM user group can terminate an Amazon EC2 instance belonging to any region except the us-west-1 region when the user's source IP is 10.200.200.200

D) Users belonging to the IAM user group can terminate an Amazon EC2 instance in the us-west-1 region when the user's source IP is 10.200.200.200

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** D (Terminate in us-west-1, user source IP match)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Deny with StringNotEquals us-west-1 = deny everywhere except us-west-1. Allow TerminateInstances from aws:SourceIp 10.200.200.0/24. Combined: can terminate in us-west-1 from that IP range. aws:SourceIp = caller's IP, not instance IP.

---

## Q17/20 [Exam 2 - Q37]

**A health-care solutions company wants to run their applications on single-tenant hardware to meet regulatory guidelines. Which of the following is the MOST cost-effective way of isolating their Amazon Elastic Compute Cloud (Amazon EC2)instances to a single tenant?**

A) Dedicated Instances

B) Dedicated Hosts

C) On-Demand Instances

D) Spot Instances

<details>
<summary>Original Result</summary>

- **Your answer:** B
- **Correct answer:** A
</details>

**Re-test answer:** A (Dedicated Instances)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Dedicated Instances = single-tenant, lower cost than Hosts. Hosts add BYOL/socket visibility but overkill for just isolation. On-Demand/Spot = multi-tenant.

---

## Q18/20 [Exam 2 - Q41]

**An enterprise is building a secure business intelligence API using Amazon API Gateway to serve internal users with confidential analytics data. The API must be accessible only from a set of trusted IP addresses that are part of the organization's internal network ranges. No external IP traffic should be able to invoke the API. A solutions architect must design this access control mechanism with the least operational complexity. What should the architect do to meet these requirements?**

A) Deploy the API Gateway as a regional API in a public subnet and associate the subnet with a security group that permits inbound traffic only from trusted IP ranges

B) Modify the security group that is attached to API Gateway to allow only traffic from specific IP addresses

C) Deploy the API Gateway resource to an on-premises server using AWS Outposts. Apply host-based firewall rules to filter allowed IPs

D) Create a resource policy for the API Gateway API that explicitly denies access to all IP addresses except those listed in an allow list

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** D
</details>

**Re-test answer:** D (Resource policy with IP allow list)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** API GW resource policies support native IP-based access control. API GW is managed service — no subnets, no security groups. Can't deploy on Outposts.

---

## Q19/20 [Exam 2 - Q54]

**An enterprise uses a centralized Amazon S3 bucket to store logs and reports generated by multiple analytics services. Each service writes to and reads from a dedicated prefix (folder path) in the bucket. The company wants to enforce fine-grained access control so that each service can access only its own prefix, without being able to see or modify other services' data. The solution must support scalable and maintainable permissions management with minimal operational overhead. Which approach will best meet these requirements?**

A) Create a single S3 bucket policy that lists all object ARNs under each prefix and grants permissions accordingly. Use resource-level permissions to restrict access to individual services

B) Configure individual S3 access points for each analytics service. Attach access point policies that restrict access to only the relevant prefix in the S3 bucket

C) Create separate IAM users for each service. Manually assign inline IAM policies to grant read/write permissions to the S3 bucket. Reference specific object names in the policy for each user

D) Deploy Amazon Macie to classify the objects in the bucket by prefix and apply automated object-level access policies to each object based on service tags

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** B
</details>

**Re-test answer:** B (S3 access points per service)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** Access points = per-service policy scoped to prefix. Scalable, maintainable. Single bucket policy = unmanageable at scale. Inline IAM = no reuse. Macie = classification, not access control.

---

## Q20/20 [Exam 2 - Q65]

**Which of the following IAM policies provides read-only access to the Amazon S3 bucket mybucket and its content?**

A) "Version":"2012-10-17",

B) "Version":"2012-10-17",

C) "Version":"2012-10-17",

D) { "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "s3:ListBucket" ], "Resource":"arn:aws:s3:::mybucket/*" }, { "Effect":"Allow", "Action":[ "s3:GetObject" ], "Resource":"arn:aws:s3:::mybucket" } ] } Giải thích tổng thể Correct option:

<details>
<summary>Original Result</summary>

- **Your answer:** A
- **Correct answer:** C
</details>

**Re-test answer:** A (ListBucket on mybucket + GetObject on mybucket/*)
**Result:** [x] CORRECT  [ ] WRONG
**Explanation:** ListBucket = bucket-level op → arn:aws:s3:::mybucket. GetObject = object-level → arn:aws:s3:::mybucket/*. Different actions need different resource scopes. Swapping or using same ARN for both fails.

---

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 20 |
| Correct | 17 |
| Wrong | 3 |
| Score | 85% |
| Original Score | 0/20 (all were wrong) |
| Improvement | +85% |
| Still Weak | S3 retention (bucket default=duration vs explicit=date), S3 deletion protection (MFA delete+versioning), EFS access (SG+IAM, not NACLs) |