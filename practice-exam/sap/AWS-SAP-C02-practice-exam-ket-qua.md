# Kết quả AWS Certified Solutions Architect – Professional (SAP-C02) – Official Practice Exam

- **Điểm:** 783 (điểm đạt: 750) — **Đạt**
- **Lần thi:** 1
- **Số câu đúng / sai / bỏ qua:** 47 / 28 / 0
- **Tổng thời gian:** 3 giờ 15 phút 34 giây (trung bình 2 phút 36 giây/câu)

---

## Câu 1 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 43 seconds*

**Đề bài:**

A company's service for video game recommendations has just gone viral. The company has new users from all over the world. The website for the service is hosted on a set of Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer (ALB). The website consists of static content with different resources being loaded depending on the device type.

Users recently reported that the load time for the website has increased. Administrators are reporting high loads on the EC2 instances that host the service.

Which set actions should a solutions architect take to improve response times?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Move content to Amazon S3. Create an Amazon CloudFront distribution to serve content out of the S3 bucket. Use the User-Agent HTTP header to load different content.**

  *Giải thích:* You can use CloudFront to cache responses based on user-agent headers. However, this strategy is not ideal because the many possible values will cause CloudFront to send more requests to the origin.
  For more information about HTTP request headers with CloudFront, see HTTP Request Headers and CloudFront Behavior (Custom and Amazon S3 Origins) 
  .

- **B. Create separate Auto Scaling groups based on device types. Switch to a Network Load Balancer (NLB). Use the User-Agent HTTP header in the NLB to route to a different set of EC2 instances.**

  *Giải thích:* You cannot route traffic based on headers with an NLB.
  For more information about NLB listener configuration, see Listeners for Your Network Load Balancers 
  .

- **C. Move content to Amazon S3. Create an Amazon CloudFront distribution to serve content out of the S3 bucket. Use Lambda@Edge to load different resources based on the User-Agent HTTP header.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You can use Lambda@Edge to serve different content for different devices. Lambda@Edge also provides the benefit of edge location caching.
  For more information about how to use Lambda@Edge to personalize content based on headers, see Example: Serving Different Versions of an Object Based on the Device 
  .

- **D. Create a separate ALB for each device type. Create one Auto Scaling group behind each ALB. Use Amazon Route 53 to route to different ALBs depending on the User-Agent HTTP header.**

  *Giải thích:* Route 53 is a DNS service. Route 53 does not have a user-agent header routing policy.
  For more information about Route 53 routing options, see Choosing a Routing Policy 
  .

---

## Câu 2 — ✅ Đúng

*Multiple Choice · Thời gian làm: 4 minutes 18 seconds*

**Đề bài:**

A company has deployed multiple copies of a reporting application in separate AWS accounts to serve users from different departments. The applications run on Amazon EC2 instances that run in Auto Scaling groups.

When the EC2 instances in the Auto Scaling groups scale in, they leave behind objects in a central Amazon S3 bucket. These objects must be cleaned up within a few minutes. The S3 objects are prefixed with the instance ID. The team that manages these applications wants to minimize cost and must use Amazon EventBridge as part of the solution.

Which design will meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Create an EventBridge bus in a central account. Create an EventBridge rule in each of the AWS accounts. Configure the rule to push the events to the central account event bus from source "aws.autoscaling". Specify an Amazon ECS task as a target in the central account.**

  *Giải thích:* Although Amazon ECS can be the target in the central account, this is not the solution with least operational overhead.
  For more information about Amazon ECS, see Amazon Elastic Container Service (Amazon ECS). https://aws.amazon.com/ecs/

- **B. Create an EventBridge rule in each of the AWS accounts to handle events from source "aws.autoscaling". Configure AWS Lambda functions on each of the accounts to clean up the S3 folder and objects.**

  *Giải thích:* This solution would result in multiple pipeline configurations and duplication of code in Lambda functions. These drawbacks would make operations cumbersome.
  For more information about EventBridge rules, see Amazon EventBridge Rules. https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html

- **C. Create an EventBridge bus in a central account. Create an EventBridge rule in each of the AWS accounts. Configure the rule to push the events to the central account event bus from source "aws.autoscaling". Invoke an AWS Lambda function in the central account to clean up the S3 folder and objects.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You can centralize the event logging by using EventBridge. You can also use a single Lambda function to perform cleanup. A solution that updates only one Lambda function is operationally efficient.
  For more information about how to use an event bus, see Amazon EventBridge Event Buses. https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html

- **D. Create EventBridge rules in each of the AWS accounts to push events to an Amazon SQS queue in a central account. Configure Spot Instances to process the SQS messages and clean up the S3 folder and objects.**

  *Giải thích:* Although Amazon SQS can manage the message queue, a solution that uses Amazon SQS with EC2 Spot Instances would require more operational overhead than necessary.
  For more information about Spot Instances, see Amazon EC2 Spot Instances. https://aws.amazon.com/ec2/spot/

---

## Câu 3 — ✅ Đúng

*Multiple Choice · Thời gian làm: 3 minutes 43 seconds*

**Đề bài:**

A company is developing a new game app for mobile devices. The app has two user tiers: one tier for free-play users and another tier for premium users.

The company currently uses custom identity authentication across its apps. The company wants to continue to use custom authentication if possible. However, the company's custom identity provider (IdP) is not compatible with either the SAML or OpenID Connect (OIDC) standards. A solutions architect needs to design an authentication approach that makes it easy to transition free-play users to premium users.

Which design will meet these requirements with the LEAST development effort?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Create a single Amazon Cognito identity pool. Develop an authentication provider for the pool that calls the existing custom IdP. Implement two separate authentication flows in the mobile app: one for the free-play users and one for the premium users.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* The code for the authentication provider would be a wrapper that allows the company to use its existing identity authentication functionality. The company should design the mobile app with two authentication flows to support free-play users and premium users. The use of a single identity pool also supports an easy transition between the free-play tier and the premium tier.
  For more information about how to create a developer authenticated identity provider, see Developer Authenticated Identities (Identity Pools). https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html

- **B. Create an Amazon Cognito user pool for the premium users. Add a user pool sign-in through the custom IdP. Create a second Amazon Cognito user pool to provide guest access for the free-play users.**

  *Giải thích:* The company has a custom IdP that is not based on SAML or OIDC. The user pool sign-in features of Amazon Cognito would not support the company's custom IdP. Significant development effort would be necessary to build a new IdP that is compliant with SAML or OIDC.
  For more information about supported IdPs for Amazon Cognito user pools, see Amazon Cognito User Pools. https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html

- **C. Create two Amazon Cognito identity pools. Develop an authentication provider for the premium user identity pool that calls the existing custom IdP. For the second identity pool, configure an authentication flow for the free-play users.**

  *Giải thích:* The creation of two identity pools would potentially require double the development work. This design would also be difficult to implement on the mobile app side. The use of two pools would also make the transition between the free-play tier and the premium tier more difficult. Significant development effort would be necessary to create a new premium user in the respective identity pool and to remove the user from the free-play user identity pool.
  For more information about how to create a developer authenticated identity provider, see Developer Authenticated Identities (Identity Pools). https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html 
  For more information about how to add users to an identity pool, see Identity Pools (Federated Identities) Authentication Flow. https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html

- **D. Create a single Amazon Cognito user pool. Add a user pool sign-in through the custom IdP. Set up Amazon Cognito guest access in the same user pool for the free-play users.**

  *Giải thích:* The company has a custom IdP that is not based on SAML or OIDC. The user pool sign-in features in Amazon Cognito would not support the company's custom IdP. Significant development effort would be necessary to build a new IdP that is compliant with SAML or OIDC.
  For more information about supported IdPs for Amazon Cognito user pools, see Amazon Cognito User Pools. https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html

---

## Câu 4 — ✅ Đúng

*Multi-Select · Thời gian làm: 1 minutes 27 seconds*

**Đề bài:**

A company wants to replace its call center system with a solution built using AWS managed services. The company call center would like the solution to receive calls, create contact flows, and scale to handle growth projections. The call center would also like the solution to use deep learning capabilities to recognize the intent of the callers and handle basic tasks, reducing the need to speak to an agent. The solution should also be able to query business applications and provide relevant information back to callers as requested.

Which services should the solutions architect use to build this solution?

**Đáp án bạn chọn:** B, C, D  
**Đáp án đúng:** B, C, D

**Các lựa chọn và giải thích:**

- **A. Amazon Rekognition to identify who is calling**

  *Giải thích:* Amazon Rekognition gives you the ability to add image and video analysis to your applications. This scenario is not an appropriate use case for Amazon Rekognition.
  For more information about Amazon Rekognition, see Amazon Rekognition. https://aws.amazon.com/rekognition/

- **B. Amazon Lex to recognize the intent of the caller**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You can use Amazon Lex to build conversational interfaces that use voice and text into any application. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) to convert speech to text. Amazon Lex also provides natural language understanding (NLU) functionality to recognize conversational intent.
  For more information about Amazon Lex, see Amazon Lex. https://aws.amazon.com/lex/

- **C. Amazon Connect to create a cloud-based contact center**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You use Amazon Connect to create cloud-based contact centers, to design contact flows (similar to interactive voice response agents), and to onboard agents.
  For more information about Amazon Connect, see Category: Amazon Connect. https://aws.amazon.com/blogs/aws/category/amazon-connect/ 
  For more information about contact flows, see Create Amazon Connect Contact Flows. https://docs.aws.amazon.com/connect/latest/userguide/contactflow.html

- **D. AWS Lambda to integrate with internal systems**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Amazon Lex uses AWS Lambda functions to query business applications, provide information back to callers, and make updates to information as needed.
  For more information about Lambda integration with Amazon Lex, see Amazon Lex. https://aws.amazon.com/lex/#Call\_Center\_Bots

- **E. Amazon Alexa for Business to build conversational interfaces**

  *Giải thích:* Alexa for Business provides features to control Alexa-compatible devices, enroll users, and assign skills at scale within an organization. This scenario is not an appropriate use case for Alexa for Business.
  For more information about Alexa, see Alexa for Business. https://aws.amazon.com/alexaforbusiness/#Benefits

- **F. Amazon SQS to add incoming callers to a queue**

  *Giải thích:* Amazon SQS gives users the ability to decouple and scale microservices, distributed systems, and serverless applications. Amazon Connect manages a customer queue flow. You use Amazon SQS to send, store, and receive messages between software components. This scenario is not an appropriate use case for Amazon SQS.
  For more information about Amazon SQS, see Amazon SQS. https://aws.amazon.com/sqs/

---

## Câu 5 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 2 seconds*

**Đề bài:**

A company has multiple AWS accounts with resources in different AWS Regions. The company uses a combination of security services, such as Amazon GuardDuty, Amazon Macie, and AWS Identity and Access Management (IAM) Access Analyzer. A security team needs to provide regular audit reports on security findings and remediation efforts. The security team needs to see consolidated findings for all accounts.

Which solution will meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Activate AWS Security Hub in each AWS account. Designate an administrator account and add the other AWS accounts as member accounts. Create an aggregation Region in the administrator account. Use the aggregation Region in the administrator account to report on the consolidated findings.**

  *Giải thích:* Security Hub provides a comprehensive view of your security state on AWS and evaluates environments according to security industry standards and best practices. However, without Organizations, you would have to manually configure Security Hub in each new account. This solution would require unnecessary operational overhead.
  For more information about Security Hub, see What Is AWS Security Hub? https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html 
  For more information about Organizations, see Using AWS Organizations to Manage Accounts. https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-prereq-orgs.html

- **B. Create an organization in AWS Organizations and activate AWS Security Hub in the management account. Designate a Security Hub administrator account and add the other AWS accounts as member accounts in Security Hub. Use the administrator account to report on the consolidated findings.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Organizations gives you the ability to create new AWS accounts programmatically. Security Hub provides a comprehensive view of your security state on AWS and evaluates environments according to security industry standards and best practices. When Organizations is activated, Security Hub can automatically detect new accounts that the company adds to the organization. This is the solution with the least operational overhead.
  For more information about Security Hub, see What Is AWS Security Hub? https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html 
  For more information about Organizations, see Using AWS Organizations to Manage Accounts. https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-prereq-orgs.html

- **C. Activate AWS Audit Manager in each Region in each account where AWS resources are running. Create a custom framework that includes the controls and control sets. Share the custom framework with the other accounts. Run assessments and view assessments by using the framework.**

  *Giải thích:* Audit Manager continuously audits your AWS usage to assess risks and compliance with regulations and industry standards. However, you need Security Hub to consolidate findings from various AWS security services.
  For more information on Audit Manager, see What Is AWS Audit Manager? https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html 
  For more information about Security Hub, see What Is AWS Security Hub? https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html

- **D. Create an organization in AWS Organizations and add all the accounts to the organization. Designate an AWS Audit Manager administrator account in the organization. Activate Audit Manager in the management account. Use the administrator account to run assessments and to view assessment reports.**

  *Giải thích:* Audit Manager continuously audits your AWS usage to assess risks and compliance with regulations and industry standards. However, you need Security Hub to consolidate findings from various AWS security services.
  For more information on Audit Manager, see What Is AWS Audit Manager? https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html 
  For more information about Security Hub, see What Is AWS Security Hub? https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html

---

## Câu 6 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes*

**Đề bài:**

A company has two AWS accounts: AccountA and AccountB. An audit requirement exists to allow an IAM user named Auditor in AccountB to have read-only access to the Amazon EC2 resources in AccountA. A security administrator in AccountA has created an IAM role named EC2Audit with read-only access to EC2 resources. A security administrator in AccountB has created the IAM user named Auditor with an inline IAM policy that allows a call to sts:AssumeRole. The call specifies the resource as "arn:aws:iam::AccountA:role/EC2Audit". No other user in AccountB can have the ability to assume the role of EC2Audit.

When Auditor attempts to assume the EC2Audit role through the AWS Management Console, Auditor is not able to sign in to AccountA.

Which action will give Auditor in AccountB the ability to assume the EC2Audit role in AccountA?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. The security administrator in AccountB must change the inline IAM policy to be a managed IAM policy and attach the policy to Auditor.**

  *Giải thích:* An appropriate trust policy is needed to ensure that Auditor in AccountB can access the EC2Audit role in AccountA. If the inline IAM policy is changed to a managed IAM policy, Auditor will not be able to assume the role in AccountA.
  For more information about managed policies and inline policies, see Managed Policies and Inline Policies. https://docs.aws.amazon.com/IAM/latest/UserGuide/access\_policies\_managed-vs-inline.html 
  For more information about cross-account access, see Providing Access to an IAM User in Another AWS Account That You Own. https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_common-scenarios\_aws-accounts.html

- **B. The security administrator in AccountB must create an IAM role that includes read-only access to Amazon EC2 for the resource "arn.aws.ec2::AccountA/\*".**

  *Giải thích:* The addition of a role in AccountB would not have any effect on resources in AccountA. An appropriate trust policy is needed to ensure that Auditor in AccountB can assume the role in AccountA.
  For more information about cross-account access, see Providing Access to an IAM User in Another AWS Account That You Own. https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_common-scenarios\_aws-accounts.html

- **C. The security administrator in AccountA must add a trust policy to the EC2Audit role with the resource "arn:aws:iam::AccountB:user/\*".**

  *Giải thích:* This trust policy would allow all users in AccountB to assume the EC2Audit role in AccountA. This policy setting is incorrect because the requirement is that only Auditor should be able to assume the role in AccountA.
  For more information about cross-account access, see Providing Access to an IAM User in Another AWS Account That You Own. https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_common-scenarios\_aws-accounts.html

- **D. The security administrator in AccountA must add a trust policy to the EC2Audit role with the resource "arn:aws:iam::AccountB:user/Auditor".**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* This trust policy will allow only Auditor in AccountB to assume the EC2Audit role.
  For more information about cross-account access, see Providing Access to an IAM User in Another AWS Account That You Own. https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_common-scenarios\_aws-accounts.html 
  For more information about access to an IAM user in another account, see IAM Tutorial: Delegate Access Across AWS Accounts Using IAM Roles. https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial\_cross-account-with-roles.html

---

## Câu 7 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 47 seconds*

**Đề bài:**

A company runs a web application on Amazon EC2 instances behind an Application Load Balancer (ALB). The instances run in an Amazon EC2 Auto Scaling group. The company's customers use the DNS name of the ALB to reach the application.

The company has gained new customers in a new geographic area and hopes to expand further. The company has purchased a new domain and wants customers to use the apex domain name to access the application from anywhere. The company has deployed an identical configuration in a second AWS Region in the new area. The company wants to reconfigure its deployment to provide a highly available solution and a faster experience to its new global customers.

What should the company do to meet these requirements?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Create an Amazon Route 53 public hosted zone with a record for the apex domain name. Set up a DNS active-active failover configuration that uses latency-based routing. Set "Evaluate Target Health" to "Yes" for the set of alias resource records.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* A Route 53 hosted zone is a container for records. Records contain information that is needed to route traffic for a specific domain. You need a public hosted zone to route traffic from the internet. A latency-based routing policy would serve user requests from the Region that provides the lowest latency. You need a set of alias records to map to the apex domain name.
  For more information about public hosted zones, see Working with Public Hosted Zones. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html 
  For more information about how to route traffic based on latency, see Latency-Based Routing. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency 
  For more information about alias records, see Choosing between Alias and Non-alias Records. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html

- **B. Create an Amazon Route 53 private hosted zone with a record for the apex domain name. Set up a DNS active-active failover configuration that uses latency-based routing. Set "Evaluate Target Health" to "Yes" for the set of CNAME resource records.**

  *Giải thích:* A Route 53 hosted zone is a container for records. Records contain information that is needed to route traffic for a specific domain. A private hosted zone would route traffic in a VPC. A public hosted zone is required for internet traffic. Additionally, it is not possible to map a CNAME record to an apex domain name. An alias record is required.
  For more information about private hosted zones, see Working with Private Hosted Zones. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html 
  For more information about public hosted zones, see Working with Public Hosted Zones. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html 
  For more information about alias records, see Choosing between Alias and Non-alias Records. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html

- **C. Create an Amazon Route 53 private hosted zone with a record for the apex domain name. Set up a DNS active-active failover configuration that uses latency-based routing. Set "Evaluate Target Health" to "Yes" for the set of alias resource records.**

  *Giải thích:* A Route 53 hosted zone is a container for records. Records contain information that is needed to route traffic for a specific domain. A private hosted zone would route traffic in a VPC. A public hosted zone is required for internet traffic.
  For more information about private hosted zones, see Working with Private Hosted Zones. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html 
  For more information about public hosted zones, see Working with Public Hosted Zones. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html

- **D. Create an Amazon Route 53 public hosted zone with a record for the apex domain name. Set up a DNS active-active failover configuration that uses latency-based routing. Set "Evaluate Target Health" to "Yes" for the set of CNAME resource records.**

  *Giải thích:* A Route 53 hosted zone is a container for records. Records contain information that is needed to route traffic for a specific domain. You need a public hosted zone to route traffic from the internet. However, it is not possible to map a CNAME record to an apex domain name. An alias record is required.
  For more information about public hosted zones, see Working with Public Hosted Zones. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html 
  For more information about alias records, see Choosing between Alias and Non-alias Records. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html

---

## Câu 8 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 55 seconds*

**Đề bài:**

A company has deployed a Python application on an Amazon ECS cluster. The application includes a stateless frontend, an Amazon RDS Multi-AZ database, and a two-node Amazon ElastiCache (Memcached) cluster to offload the database read requests for frequently accessed data.

The number of read requests to the database is increasing. A solutions architect adds two more nodes to the ElastiCache cluster. However, performance does not appear to improve after the addition of the nodes, and the new Memcached instances seem idle.

How can the solutions architect resolve this issue with the LEAST code changes?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Replace the ElastiCache (Memcached) cluster with an ElastiCache (Redis OSS) cluster that has cluster mode disabled. Add four read replicas to the Redis cluster.**

  *Giải thích:* Additional Redis replicas would likely increase the read performance of the caching solution. However, if you replace the Memcached cluster with a Redis cluster, you would have to completely reconfigure the application to use Redis APIs. This reconfiguration would involve significant code changes.
  For more information about Redis cluster read replicas, see Understanding Valkey and Redis OSS replication 
  .

- **B. Replace the ElastiCache (Memcached) cluster with an ElastiCache (Redis OSS) cluster that has cluster mode enabled. Add four shards to the Redis cluster.**

  *Giải thích:* The addition of a Redis cluster with shards would likely increase the read and write performance of the caching solution. However, if you replace the Memcached cluster with a Redis cluster, you would have to completely reconfigure the application to use Redis APIs. This reconfiguration would involve significant code changes.
  For more information about how to enable Redis cluster mode and how to configure shards, see Replication: Valkey and Redis OSS Cluster Mode Disabled vs. Enabled 
  .

- **C. Use the AWS CLI to discover the newly added node endpoints. Configure the RDS database for reads and writes to all the endpoints.**

  *Giải thích:* You cannot configure the RDS database to perform any reads and writes against the Memcached cluster. The application reads and writes to the cache.
  For more information about database caches, see Types of Database Caching 
  .

- **D. Use the AWS CLI to discover the newly added node endpoints. Configure the application for reads and writes to all the endpoints.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* ElastiCache (Memcached) can support Auto Discovery for certain clients. Auto Discovery is not in use in this scenario because the newly added nodes are not being discovered. You need to add the new endpoints to the application code. Some code change would be necessary, but this process would not require a complete rewrite of the code that interacts with Memcached.
  For more information about how to discover connection endpoints for a newly added Memcached node, see Finding connection endpoints in ElastiCache 
  .
  For more information about how to connect to cache nodes manually, see Connecting to Memached Cache Nodes Manually 
  .

---

## Câu 9 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 49 seconds*

**Đề bài:**

A company stores a large amount of customer data in an Amazon S3 bucket that uses the S3 Standard storage class. The amount of data will continue to grow. The company needs to reduce the cost of the data storage. The company needs to access some customer data frequently within the first 6 months. However, the company rarely needs to access other customer data during that period. The company rarely needs to access data that is 180 days or older, but the company must have the ability to access this old data within 6 hours.

Which storage strategy will meet these requirements MOST cost-effectively?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Implement S3 Intelligent-Tiering on the existing S3 bucket. Activate the Archive Access tier. Set the days until transition to 180.**  
  _✔ Đáp án đúng_

  *Giải thích:* S3 Intelligent-Tiering automatically monitors access patterns and moves objects across multiple access tiers to optimize storage costs. Standard retrieval of objects in the S3 Intelligent-Tiering Archive Access tier occurs within 3–5 hours. This solution addresses both the unknown access patterns and the requirement to access the old data within 6 hours.
  For more information about S3 Intelligent-Tiering, see How S3 Intelligent-Tiering Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html 
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

- **B. Create a new S3 Lifecycle configuration for the existing S3 bucket. Configure the lifecycle rule for all objects to move data to S3 Glacier Deep Archive after 180 days.**

  *Giải thích:* Use of S3 Lifecycle configurations to move data to S3 Glacier Deep Archive would reduce the cost of storage after 180 days. However, S3 Glacier Deep Archive has a retrieval time of 12 hours. This time frame does not meet the requirement to access the old data within 6 hours. Additionally, this solution leaves all data in S3 Standard storage for the first 180 days, when many of the infrequently accessed objects could be stored at a much lower cost.
  For more information about S3 Lifecycle rules, see Transitioning Objects Using Amazon S3 Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html 
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

- **C. Implement S3 Intelligent-Tiering on the existing S3 bucket. Activate the Deep Archive Access tier. Set the days until transition to 180.**  
  _☑ Bạn đã chọn_

  *Giải thích:* S3 Intelligent-Tiering automatically monitors access patterns and moves objects across multiple access tiers to optimize storage costs. However, Standard retrieval of objects in the S3 Intelligent-Tiering Deep Access Archive tier occurs within 12 hours. This time frame does not meet the requirement to access the old data within 6 hours.
  For more information about S3 Intelligent-Tiering, see How S3 Intelligent-Tiering Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html 
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

- **D. Create a new S3 Lifecycle configuration for the existing S3 bucket. Configure the lifecycle rule for all objects to move data to S3 Glacier Flexible Retrieval after 180 days.**

  *Giải thích:* Use of S3 Lifecycle configurations to move data to S3 Glacier Flexible Retrieval would reduce the cost of storage after 180 days. S3 Glacier Flexible Retrieval can retrieve objects quickly. However, this solution leaves all data in S3 Standard for the first 180 days, when many of the infrequently accessed objects could be stored at a much lower cost. This solution does not optimize the storage classes based on unknown or changing access patterns. A better solution would use S3 Intelligent-Tiering.
  For more information about S3 Lifecycle rules, see Transitioning Objects Using Amazon S3 Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html 
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

---

## Câu 10 — ✅ Đúng

*Multiple Choice · Thời gian làm: 3 minutes 54 seconds*

**Đề bài:**

A company has multiple AWS accounts. A solutions architect has created an organization in AWS Organizations with two OUs: Dev and Prod. The company enforces the following rules:

The root user in all existing and future member accounts must not have the ability to make any AWS service API calls.
Existing and future Dev member accounts must be able to create resources only in the us-west-2 Region.
Existing and future Prod member accounts must be able to create resources in any Region.

The company creates the following SCPs:

SCP1, which denies all actions on all resources with the following condition: { "Condition": {"StringLike": { "aws:PrincipalArn": "arn:aws:iam::*:root" }}}
SCP2, which denies all actions on all resources with the following condition: { "Condition": {"StringNotEquals": {"aws:RequestedRegion": "us-west-2"}}}

How should the company implement the SCPs to meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Attach SCP1 and SCP2 to the organization's root.**

  *Giải thích:* If you attach SCP2 to the organization's root, you will enforce all the rules in SCP2 on all member accounts. The requirement is to enforce the rules in SCP2 only on member accounts in the Dev OU.
  For more information about inheritance for service control policies, see Inheritance for Service Control Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance\_auth.html

- **B. Attach SCP1 to all accounts. Attach SCP2 to each Dev account.**

  *Giải thích:* If you attach SCP1 to all accounts and attach SCP2 to each member account under the Dev OU, you will enforce the rules in both SCPs correctly. However, this solution would incur additional operational overhead that you would avoid by attaching the SCPs at the OU level.
  For more information about management of OUs, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html 
  For more information about inheritance for service control policies, see Inheritance for Service Control Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance\_auth.html

- **C. Attach SCP1 to the organization's root. Attach SCP2 to the Dev OU.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* If you attach SCP1 to the organization's root and attach SCP2 to the Dev OU, you will enforce the rules in the two SCPs correctly with the least operational overhead.
  For more information about management of OUs, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html 
  For more information about inheritance for service control policies, see Inheritance for Service Control Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance\_auth.html

- **D. Attach SCP1 to the Prod OU. Attach SCP2 to the Dev OU.**

  *Giải thích:* If you attach SCP1 to only the Prod OU, you will enforce the rules in SCP1 only on the accounts under the Prod OU. The requirement is to enforce the rules in SCP1 on all accounts.
  For more information about best practices for member accounts, see Best Practices for Member Accounts. https://docs.aws.amazon.com/organizations/latest/userguide/best-practices\_member-acct.html 
  For more information about inheritance for service control policies, see Inheritance for Service Control Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance\_auth.html

---

## Câu 11 — ❌ Sai

*Multiple Choice · Thời gian làm: 1 minutes 32 seconds*

**Đề bài:**

A company has a serverless application that is backed by an Amazon RDS database. The company's AWS Lambda functions share the same user account to access the database.

A database administrator updates the password in the database to comply with security policies. Shortly after the update, several Lambda functions fail. The user receives an error message for credentials that are not valid. After investigating the error, a solutions architect discovers that the affected Lambda functions use hardcoded credentials. The solutions architect needs to address the errors and improve the security of the credentials.

Which solution will meet these requirements with the LEAST development effort?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Store the credentials in AWS Systems Manager Parameter Store. Update the Lambda functions to retrieve the user name and password from Parameter Store. Configure an Amazon EventBridge rule that invokes a Lambda function to update Parameter Store whenever the password is changed in the RDS database.**  
  _☑ Bạn đã chọn_

  *Giải thích:* Parameter Store can securely store the credentials. However, the creation of an extra Lambda function to rotate the password involves significant code development. This solution also requires manual updates of the database.
  For more information about Parameter Store, see AWS Systems Manager Parameter Store. https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html

- **B. Store the user name and password in AWS Secrets Manager. Update the Lambda functions to retrieve the user name and password from Secrets Manager. Configure an alternating users automatic rotation of the credentials as required.**

  *Giải thích:* Secrets Manager replaces hardcoded credentials with API calls to retrieve secrets programmatically. You can configure Secrets Manager to automatically rotate RDS database passwords. An alternating users rotation updates credentials for two users in one secret. However, in this scenario, the database has only a single application user account.
  For more information about Secrets Manager, see What is AWS Secrets Manager? https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html 
  For more information about rotation strategies, see Rotation Strategies. https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets\_strategies.html

- **C. Create a Lambda function to update the credentials in the RDS database. Schedule the Lambda function to run as required. Configure an Amazon EventBridge rule that invokes a Lambda function to update the hardcoded passwords whenever the password is changed in the RDS database.**

  *Giải thích:* Significant code development would be required to create multiple Lambda functions to rotate the passwords both in the database and the applications.
  For more information about EventBridge notifications for Amazon RDS, see Creating a Rule that Triggers on an Amazon RDS Event. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-cloud-watch-events.html

- **D. Store the user name and password in AWS Secrets Manager. Update the Lambda functions to retrieve the user name and password from Secrets Manager. Configure a single user automatic rotation of the credentials as required.**  
  _✔ Đáp án đúng_

  *Giải thích:* Secrets Manager replaces hardcoded credentials with API calls to retrieve secrets programmatically. You can configure Secrets Manager to automatically rotate RDS database passwords. In this scenario, the database has a single application user account. For this reason, the single user rotation strategy would be appropriate. This solution requires no new Lambda functions, so it requires the least development effort.
  For more information about Secrets Manager, see What is AWS Secrets Manager? https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html 
  For more information about rotation strategies, see Rotation Strategies. https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets\_strategies.html

---

## Câu 12 — ✅ Đúng

*Multi-Select · Thời gian làm: 3 minutes 41 seconds*

**Đề bài:**

A company needs to migrate two individual applications from on premises to AWS:

The first application is a legacy custom application that is hosted on a physical Windows server. The application source code is no longer available. The application has little documentation, has hardcoded operating system configuration settings, and is used by an external third party.
The second application is an IBM Db2 database that is hosted on a single Linux VM that uses network-attached storage (NAS) to store the database data. The company uses this database internally for employee records.

The applications are hosted in a data center that the company plans to decommission in 90 days. Where possible, the company must use managed AWS services.

Which actions for migration should a solutions architect recommend to meet these requirements?

**Đáp án bạn chọn:** B, D  
**Đáp án đúng:** B, D

**Các lựa chọn và giải thích:**

- **A. Migrate the Windows server with the legacy application to Amazon EC2 by using AWS DataSync.**

  *Giải thích:* DataSync is an online data transfer service that simplifies, automates, and accelerates the movement of data between storage systems and services. You cannot use DataSync to migrate servers.
  For more information about DataSync, see What Is AWS DataSync?

- **B. Migrate the IBM Db2 database data to Amazon RDS for MySQL by using AWS DMS and the AWS SCT replication agent.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* This solution will replatform the existing database server to Amazon RDS. AWS DMS gives you the ability to convert from IBM Db2 to a supported RDS engine such as MySQL. You need AWS SCT to support the schema conversion to Amazon RDS.
  For more information about AWS DMS, see AWS Database Migration Service Supports IBM Db2 as a Source 
  .
  For more information about AWS SCT, see What Is the AWS Schema Conversion Tool?

- **C. Migrate the Linux VM with the IBM Db2 database service to an Amazon EC2 instance by using AWS Transform MGN (previously known as AWS Application Migration Service).**

  *Giải thích:* Although this solution is a possibility, the company wants to use a managed AWS service. Amazon EC2 is not the best option because it is not a managed service. The company can migrate the IBM Db2 database to a managed database service such as Amazon RDS for MySQL.
  For more information about AWS Transform MGN, see What Is AWS Transform MGN?

- **D. Migrate the Windows server with the legacy application to Amazon EC2 by using AWS Transform MGN (previously known as AWS Application Migration Service).**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* A rehost (lift and shift) method is the only viable option because of the application type and because the application is on a physical server. Because the application uses custom OS configurations, AWS Transform MGN is the best option. Although Amazon EC2 is not a managed service, it is the only option for this use case.
  For more information about AWS Transform MGN, see What Is AWS Transform MGN?

- **E. Migrate the IBM Db2 database data to Amazon RDS for MySQL by using AWS DataSync and the AWS SCT data extraction agent.**

  *Giải thích:* DataSync is an online data transfer service that simplifies, automates, and accelerates the movement of data between storage systems and services. You cannot use DataSync to migrate databases.
  For more information about DataSync, see What Is AWS DataSync?

---

## Câu 13 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 19 seconds*

**Đề bài:**

A company plans to set up multiple AWS accounts by using AWS Organizations. A company-wide policy requires teams to take a backup of Amazon EBS volumes each day. The company's Cloud Center of Excellence (CCoE) team wants to design a backup solution that it can enforce consistently across all the accounts.

Which solution will meet these requirements MOST reliably?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create an AWS Service Catalog product that creates an Amazon Data Lifecycle Manager (Amazon DLM) snapshot policy. Enable all account administrators to launch the product within each account.**

  *Giải thích:* Amazon DLM automates the creation, retention, and deletion of EBS snapshots. However, you cannot ensure reliability by creating an Amazon DLM snapshot policy as an AWS Service Catalog product. An individual account administrator might not launch the product or might accidentally delete the product.
  For more information about Amazon DLM, see Amazon Data Lifecycle Manager. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html 
  For more information about AWS Service Catalog, see Overview of AWS Service Catalog. https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is\_concepts.html

- **B. Create an AWS CloudFormation template to create a backup plan through AWS Backup. Use the template to deploy the backup plan to multiple accounts by using CloudFormation StackSets.**

  *Giải thích:* AWS Backup centralizes and automates data backups across AWS services, including Amazon EBS. CloudFormation StackSets can reliably launch the solution as stack instances across the accounts. However, it is possible to delete these stack instances internally within the account. This solution will not meet the requirement to consistently enforce the company's backup policy.
  For more information about how to detect changes in resources in stack sets, see Detecting Unmanaged Configuration Changes in Stack Sets. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html

- **C. Create an Organizations backup policy to back up resources by using Amazon Data Lifecycle Manager (Amazon DLM). Validate and attach the backup policy to the root of the organization.**  
  _☑ Bạn đã chọn_

  *Giải thích:* Amazon DLM automates the creation, retention, and deletion of EBS snapshots. However, you cannot create an Amazon DLM snapshot policy by using an Organizations backup policy.
  For more information about Amazon DLM, see Amazon Data Lifecycle Manager. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html

- **D. Create an Organizations backup policy to back up resources by using AWS Backup. Validate and attach the backup policy to the root of the organization.**  
  _✔ Đáp án đúng_

  *Giải thích:* AWS Backup centralizes and automates data backups across AWS services, including Amazon EBS. AWS Backup can implement a backup plan with the appropriate backup rule to meet the company's backup policy. Additionally, Organizations backup policies conveniently create these backup plans across multiple accounts. It is not possible to delete or edit these backup plans individually within the account. This solution will enforce the company's backup policy reliably and consistently.
  For more information about AWS Backup, see Creating a Backup Plan. https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html 
  For more information about Organizations backup policies, see Creating, Updating, and Deleting Backup Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_backup\_create.html

---

## Câu 14 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 4 seconds*

**Đề bài:**

A company uses AWS to host resources for developers to help the developers develop and test applications. The developers have created their own resources on AWS, which has led to cost fluctuations and a lack of enforcement of company standards. The company has decided to provide two standard configurations: one for development systems and one for test systems. The company wants a solution that will give the developers the ability to create the resources they need. However, the company wants to limit developers to the approved configurations only.

Which solution will meet these requirements?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Create Docker-based containers to use with Amazon ECS for each standard configuration. Create IAM policies to allow the developers to launch the containers.**

  *Giải thích:* Amazon ECS is a highly scalable, fast container-management service that provides tools to run, stop, and manage containers on a cluster. Use of containers would give the developers the ability to deploy only application components instead of the ability to deploy standard resource configurations.
  For more information about Amazon ECS, see What Is Amazon Elastic Container Service? https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html

- **B. Create identity-based IAM policies that allow the creation of only standard resources. Attach the policies to the developers. Allow the developers to create new resources.**

  *Giải thích:* IAM policies define permissions for an action regardless of the method that developers use to perform the operation. Identity-based IAM policies can restrict which resources the developers can create. However, developers would have the ability to deploy only partial resources instead of the full, approved resource configurations. Available resources on AWS change constantly, and the company would need to regularly review and update IAM policies.
  For more information about IAM policies, see Policies and Permissions in IAM. https://docs.aws.amazon.com/IAM/latest/UserGuide/access\_policies.html

- **C. Create products in AWS Service Catalog for development and testing. Attach an IAM role that has appropriate permissions to the products. Create IAM policies to allow the developers to launch the products.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* AWS Service Catalog provides a self-service option for users to create resources. Attachment of an IAM role to the products will allow developers to create the resources without the need to maintain direct privileges for resource creation on AWS.
  For more information about AWS Service Catalog, see What Is AWS Service Catalog? https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html

- **D. Create AWS CloudFormation templates for each standard configuration. Store the templates in an Amazon S3 bucket. Create IAM policies to allow the developers to use the templates to create stacks.**

  *Giải thích:* CloudFormation helps model and set up AWS resources so that developers can spend less time on the management of those resources and spend more time on the applications that run on AWS. To create resources by using CloudFormation templates, the developers would need direct privileges. This solution would not limit the developers to the approved configurations.
  For more information about CloudFormation, see What Is AWS CloudFormation? https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html

---

## Câu 15 — ✅ Đúng

*Multiple Choice · Thời gian làm: 4 minutes 30 seconds*

**Đề bài:**

A solutions architect is responsible for redesigning a legacy Java application to improve its availability, data durability, and scalability. Currently, the application runs on a single high-memory Amazon EC2 instance. It accepts HTTP requests from upstream clients, adds them to an in-memory queue, and responds with a 200 status. A separate application thread reads items from the queue, processes them, and persists the results to an Amazon RDS MySQL instance. The processing time for each item takes 90 seconds on average, most of which is spent waiting on external service calls, but the application is written to process multiple items in parallel.

Traffic to this service is unpredictable. During periods of high load, items may sit in the internal queue for over an hour while the application processes the backlog. In addition, the current system has issues with availability and data loss if the single application node fails.

Clients that access this service cannot be modified. They expect to receive a response to each HTTP request they send within 10 seconds before they will time out and retry the request.

Which approach would improve the availability and durability of the system while decreasing the processing latency and minimizing costs?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Modify the application to use Amazon DynamoDB instead of Amazon RDS. Configure Auto Scaling for the DynamoDB table. Deploy the application within an Auto Scaling group with a scaling policy based on CPU utilization. Back the in-memory queue with a memory-mapped file to an instance store volume and periodically write that file to Amazon S3.**

  *Giải thích:* You would not address the durability concerns by configuring auto scaling for DynamoDB. If an instance fails, you will lose messages.
  For more information about DynamoDB auto scaling, see Managing Throughput Capacity Automatically with DynamoDB Auto Scaling 
  .

- **B. Update the application to use a Redis task queue instead of the in-memory queue. Build a Docker container image for the application. Create an Amazon ECS task definition that includes the application container and a separate container to host Redis. Deploy the new task definition as an ECS service using AWS Fargate, and enable Auto Scaling.**

  *Giải thích:* This solution does not improve the durability. This solution is also not cost-effective because the frontend and backend are still coupled and must be scaled together.

- **C. Create an Amazon API Gateway REST API that uses Lambda proxy integration to pass requests to an AWS Lambda function. Migrate the core processing code to a Lambda function and write a wrapper class that provides a handler method that converts the proxy events to the internal application data model and invokes the processing module.**

  *Giải thích:* API Gateway REST API Lambda proxy integrations are inherently synchronous. The clients would time out before the request finishes. API Gateway has a limit of 29 seconds for backend response times.
  For more information about API Gateway with Lambda integration, see Build an API Gateway REST API with Lambda Integration 
  .

- **D. Create an Amazon API Gateway REST API that uses a service proxy to put items in an Amazon SQS queue. Extract the core processing code from the existing application and update it to pull items from Amazon SQS instead of an in-memory queue. Deploy the new processing application to smaller EC2 instances within an Auto Scaling group that scales dynamically based on the approximate number of messages in the Amazon SQS queue.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* This solution provides a managed, automatically scaled frontend to receive requests. This solution stores messages durably in Amazon SQS until the messages are successfully processed. The backend will scale horizontally when a surge of requests arrives.
  For more information about API Gateway integrations, see Setting Up REST API Integrations 
  .
  For more information about auto scaling based on Amazon SQS, see Scaling Based on Amazon SQS 
  .

---

## Câu 16 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 34 seconds*

**Đề bài:**

During migration to the AWS Cloud, a company modernized an application to use a microservices architecture. The company will deploy the application across multiple AWS Regions to meet latency and disaster recovery requirements. During both full and partial failures, the traffic must be automatically rerouted to the healthy deployments in other Regions. The company will route traffic to an Amazon API Gateway API by using a custom domain name that the company manages with Amazon Route 53. The company will monitor the infrastructure, including API Gateway endpoints, by using multiple Amazon CloudWatch metrics.

Which solution will route user requests to fully functional microservices?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Configure Route 53 Application Recovery Controller routing controls and health checks for each deployment. Create AWS Lambda functions that will be invoked based on each resource’s metric alarms. Use the Lambda functions to toggle routing controls to automate routing appropriately.**  
  _✔ Đáp án đúng_

  *Giải thích:* Route 53 Application Recovery Controller routing controls provide simple on/off switches that give you the ability to direct traffic from one replica to another. These routing controls are based on Route 53 health checks that you configure. The Route 53 health checks become healthy or unhealthy by toggling routing controls. Based on multiple metrics from various application components, you can automate the toggling of these routing controls with CloudWatch alarms and Lambda functions.
  For more information about Route 53 Application Recovery Controller routing controls, see Routing Control in Amazon Route 53 Application Recovery Controller. https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html 
  For more information about how to create Route 53 Application Recovery Controller routing controls, see Create Routing Control Structures in ARC. https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create.html

- **B. Configure Route 53 health checks for each Regional API Gateway endpoint to automate routing appropriately.**

  *Giải thích:* You would not detect any partial failures within the application by monitoring API Gateway endpoints with Route 53 health checks. This option will not meet the requirements.
  For more information about Route 53 health checks, see How Amazon Route 53 Determines Whether a Health Check Is Healthy. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html

- **C. Select the Route 53 Evaluate Target Health option for each record set to automate routing appropriately.**  
  _☑ Bạn đã chọn_

  *Giải thích:* You would not detect any partial failures within the application by monitoring API Gateway endpoints with the Route 53 Evaluate Target Health option. This option will not meet the requirements.
  For more information about the Route 53 Evaluate Target Health option, see How Amazon Route 53 Chooses Records when Health Checking Is Configured. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-how-route-53-chooses-records.html

- **D. Configure Route 53 Application Recovery Controller readiness checks for each resource type of the application. Create AWS Lambda functions that will be invoked based on readiness checks. Use the Lambda functions to update the Route 53 record sets to automate routing appropriately.**

  *Giải thích:* A Route 53 Application Recovery Controller readiness check continuously monitors AWS resource configurations, capacity, and network routing policies. These checks give you the ability to monitor for changes that would affect your ability to enact a recovery operation. These checks ensure that you have scaled and configured the recovery environment appropriately to take over when necessary. However, this is an assessment feature which, by itself, will not route traffic to the healthy Regions.
  For more information about Route 53 Application Recovery Controller readiness checks, see Amazon Route 53 Application Recovery Controller Components. https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-components.html

---

## Câu 17 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 37 seconds*

**Đề bài:**

A company is hosting an ecommerce application on two Amazon EC2 instances behind an Application Load Balancer (ALB) across two Availability Zones. The application is performing well during normal sales activity. However, customers experience slow response times during unexpected peak sales activity.

Recently, one of the instances was accidentally stopped, resulting in a significant performance decrease. A solutions architect investigates the slow response times but finds no correlation between the peaks and changes in Amazon CloudWatch metrics for the EC2 instances. The solutions architect is planning to use Amazon EC2 Auto Scaling to help resolve the issues.

How should the solutions architect configure the Auto Scaling group to resolve these issues?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create a scheduled scaling policy for the Auto Scaling group. Configure the scheduled actions to increase the number of EC2 instances during the peak sales periods.**  
  _☑ Bạn đã chọn_

  *Giải thích:* Scheduled scaling uses scheduled actions that are performed automatically as a function of date and time. A scheduled time would not address the unexpected peak activity.
  For more information about scheduled scaling, see Scheduled Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule\_time.html

- **B. Create a dynamic scaling policy for the Auto Scaling group. Configure a target tracking policy to increase the number of EC2 instances based on the average CPU utilization of the Auto Scaling group.**

  *Giải thích:* Dynamic scaling scales the capacity of an Auto Scaling group in response to changes in demand. Target tracking based on this metric would not scale the group at the appropriate times because the peaks in sales do not correlate with any CloudWatch metrics for EC2 instances, including CPU utilization.
  For more information about dynamic scaling, see Dynamic Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html 
  For more information about how to choose metrics for dynamic scaling, see Choosing Metrics. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#available-metrics

- **C. Create a predictive scaling policy for the Auto Scaling group to scale based on forecast. Configure the scaling metric to be the request count per target on the ALB target group.**

  *Giải thích:* Predictive scaling changes the number of EC2 instances in an Auto Scaling group in advance of daily and weekly patterns in traffic flows. Predictive scaling is not a good option because the peak sales activities happen at unexpected times.
  For more information about predictive scaling, see Predictive Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html

- **D. Create a dynamic scaling policy for the Auto Scaling group. Configure the scaling metric to be the request count per target on the ALB target group.**  
  _✔ Đáp án đúng_

  *Giải thích:* Dynamic scaling scales the capacity of an Auto Scaling group in response to changes in demand. The only performance differentiator in this scenario is the number of requests sent to each EC2 instance. A target tracking policy based on the number of requests from the ALB will appropriately scale the group.
  For more information about dynamic scaling, see Dynamic Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html 
  For more information about how to choose metrics for dynamic scaling, see Choosing Metrics. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#available-metrics

---

## Câu 18 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 14 seconds*

**Đề bài:**

A company has multiple on-premises data centers around the world. The company wants to migrate 150 VMs to AWS with minimal downtime. The company also needs to migrate 300 TB of data to a single AWS Region. With the company's current internet connection, the data migration would take 5 days.

Which combination of tools and services will provide the FASTEST migration to AWS?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Transfer the data by using AWS Snowball devices. Use AWS Transform MGN (previously known as AWS Application Migration Service) to migrate the VMs.**

  *Giải thích:* You would need approximately 7 days to transfer the data by using Snowball devices. AWS Transform MGN provides significant improvement over VM Import/Export. AWS Transform MGN provides automated, live, incremental server replication and AWS console support.
  For more information about Snowball, see Amazon Snowball FAQs. https://aws.amazon.com/snowball/faqs 
  For more information about migration tools and services, see AWS Transform MGN FAQs. https://aws.amazon.com/application-migration-service/faqs

- **B. Transfer the data by using Amazon S3 Transfer Acceleration. Use VM Import/Export to migrate the VMs.**

  *Giải thích:* You would need approximately 5 days to transfer the data by using S3 Transfer Acceleration. However, AWS Transform MGN provides significant improvement over VM Import/Export. AWS Transform MGN provides automated, live, incremental server replication and AWS console support.
  For more information about S3 Transfer Acceleration, see S3 Transfer Acceleration. https://aws.amazon.com/s3/transfer-acceleration 
  For more information about migration tools and services, see AWS Transform MGN FAQs. https://aws.amazon.com/application-migration-service/faqs

- **C. Transfer the data by using AWS Snowball devices. Use VM Import/Export to migrate the VMs.**

  *Giải thích:* You would need approximately 7 days to transfer the data by using Snowball devices. AWS Transform MGN provides significant improvement over VM Import/Export. AWS Transform MGN provides automated, live, incremental server replication and AWS console support.
  For more information about Snowball, see Amazon Snowball FAQs. https://aws.amazon.com/snowball/faqs 
  For more information about migration tools and services, see AWS Transform MGN FAQs. https://aws.amazon.com/application-migration-service/faqs

- **D. Transfer the data by using Amazon S3 Transfer Acceleration. Use AWS Transform MGN (previously known as AWS Application Migration Service) to migrate the VMs.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You would need approximately 5 days to transfer the data by using S3 Transfer Acceleration. AWS Transform MGN provides automated, live, incremental server replication and AWS console support. Incremental AWS Transform MGN replication minimizes the business impact that is associated with application downtime during the final cutover.
  For more information about S3 Transfer Acceleration, see S3 Transfer Acceleration. https://aws.amazon.com/s3/transfer-acceleration 
  For more information about migration tools and services, see AWS Transform MGN FAQs. https://aws.amazon.com/application-migration-service/faqs

---

## Câu 19 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 38 seconds*

**Đề bài:**

A solutions architect needs to create an infrastructure proposal for a web application. The application requires a resilient and highly available design across multiple Availability Zones. The solutions architect proposes the following:

A VPC with an internet gateway and a NAT gateway
One public subnet and one private subnet each in two different Availability Zones
An Amazon EC2 Auto Scaling group spread across multiple Availability Zones behind an internet-facing Application Load Balancer (ALB)
Amazon DynamoDB tables to store data

What should the solutions architect do to increase the resilience and availability of the proposed architecture?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create a second internet-facing ALB. Attach each ALB to a different subnet.**

  *Giải thích:* You do not need to create a second internet-facing ALB to achieve a resilient architecture across Availability Zones. By default, an ALB is a highly available and scalable resource that is managed by AWS.
  For more information about ALBs, see Application Load Balancers. https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html

- **B. Create a second internet gateway. Attach each internet gateway to a different subnet.**

  *Giải thích:* You do not need to create a second internet gateway to achieve a resilient architecture across Availability Zones. By default, an internet gateway is a highly available and scalable component that is managed by AWS.
  For more information about internet gateways, see Connect Subnets to the Internet Using an Internet Gateway. https://docs.aws.amazon.com/vpc/latest/userguide/VPC\_Internet\_Gateway.html

- **C. Create DynamoDB global tables with two replicated tables that are stored in different AWS Regions.**  
  _☑ Bạn đã chọn_

  *Giải thích:* DynamoDB global tables are not necessary for this solution. Data in DynamoDB tables is automatically replicated across multiple Availability Zones in the Region where the tables are created. You do not need to create a global DynamoDB table to achieve a resilient architecture across Availability Zones.
  For more information about DynamoDB high availability, see What Is Amazon DynamoDB? https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

- **D. Create a second NAT gateway. Update the route tables on each private subnet as needed.**  
  _✔ Đáp án đúng_

  *Giải thích:* You need to create a second NAT gateway in a separate Availability Zone to achieve a resilient architecture across Availability Zones. A NAT gateway is highly available only within the Availability Zone where it is deployed.
  For more information about the availability of NAT gateways, see NAT Gateway Basics. https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-basics

---

## Câu 20 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 37 seconds*

**Đề bài:**

A company has offices in several countries. Each office has its own AWS account. The company manages all accounts centrally by using AWS Organizations. While implementing a process to centralize security policies, system operators from multiple accounts simultaneously report an inability to access any Amazon S3 buckets.

What should the system operators do to restore access to the S3 buckets?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Sign in to the management account as an IAM user with appropriate permissions. Open Organizations. Correct any SCP that is blocking access to Amazon S3.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* The fact that multiple accounts are affected simultaneously indicates that SCPs are a cause. The management account allows access to manage SCPs because the management account is unaffected by SCPs.
  For more information about Organizations management accounts, see Best Practices for the Management Account. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_best-practices\_mgmt-acct.html 
  For more information about SCPs, see Service Control Policies (SCPs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_scps.html

- **B. Sign in to each of the member accounts as the account root user. Open Organizations. Correct any SCP that is blocking access to Amazon S3.**

  *Giải thích:* The fact that the outages occurred at the same time indicates that the problem might be related to SCPs at a higher level of the organization. The member accounts of an organization are not able to inspect or change the SCPs that have been applied at any level in the organization's hierarchy.
  For more information about SCPs, see Service Control Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_scps.html 
  For more information about Organizations management accounts, see Best Practices for the Management Account. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_best-practices\_mgmt-acct.html

- **C. Sign in to the management account as an IAM user with appropriate permissions. Open IAM. Correct any IAM policy that is blocking access to Amazon S3.**

  *Giải thích:* An administrator can define permissions within a single AWS account by using IAM policies. However, the presence of errors in multiple accounts at the same time indicates that an SCP might be the problem.
  For more information about IAM, see Overview of Access Management: Permissions and Policies. https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction\_access-management.html 
  For more information about SCPs, see Service Control Policies (SCPs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_scps.html

- **D. Sign in to each of the member accounts as the account root user. Open IAM. Correct any IAM policy that is blocking access to Amazon S3.**

  *Giải thích:* An administrator can define permissions within a single AWS account by using IAM policies. However, the presence of errors in multiple accounts at the same time indicates that an SCP might be the problem.
  For more information about IAM, see Overview of Access/Management: Permissions and Policies. https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction\_access-management.html 
  For more information about SCPs, see Service Control Policies (SCPs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_scps.html

---

## Câu 21 — ❌ Sai

*Multi-Select · Thời gian làm: 1 minutes 50 seconds*

**Đề bài:**

A company runs an HPC cluster in an AWS Region. The cluster consists of a group of Linux instances that run a tightly coupled workload. The company is not satisfied with the current key performance indicators. The company needs to increase network throughput and reduce the network latency between the Amazon EC2 instances that make up the cluster.

Which combination of actions will meet these requirements?

**Đáp án bạn chọn:** A, C, E  
**Đáp án đúng:** A, C, F

**Các lựa chọn và giải thích:**

- **A. Select an EC2 instance type that supports the use of an Elastic Fabric Adapter (EFA).**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* An EFA is a network device that you can attach to an EC2 instance to accelerate HPC and machine learning applications. With an EFA, HPC applications can scale to thousands of CPUs or GPUs which results in the same application performance as on-premises HPC clusters with the additional benefit of the on-demand elasticity and flexibility of the AWS Cloud.
  For more information about EFAs, see Elastic Fabric Adapter. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html

- **B. Use EC2 instances with burstable performance.**

  *Giải thích:* The T instance family provides a baseline CPU performance with the ability to burst above the baseline at any time for as long as required. However, burstable performance instances would not typically improve network performance in an HPC cluster.
  For more information about burstable performance instances, see Burstable Performance Instances. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html

- **C. Run the HPC cluster within a single Availability Zone.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* If an HPC cluster runs within a single Availability Zone, workloads can achieve the low-latency network performance that is necessary for the tightly coupled node-to-node communication that is typical for HPC applications.
  For more information about network latency, see Architecture Guidelines and Decisions. https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-guidelines-and-decisions.html

- **D. Deploy the EC2 instances in a partition placement group.**

  *Giải thích:* Partition placement groups help reduce the likelihood of correlated hardware failures for an application. Deployment of EC2 instances in a partition placement group spreads EC2 instances across logical partitions and ensures that instances in different partitions do not share the same underlying hardware. A partition placement group would increase network latency, not reduce it.
  For more information about partition placement groups, see Partition Placement Groups. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#placement-groups-partition

- **E. Ensure that the EC2 instances run an AMI that supports paravirtual (PV).**  
  _☑ Bạn đã chọn_

  *Giải thích:* Linux AMIs use one of two types of virtualization: PV or hardware virtual machine (HVM). Linux PV AMIs would not improve the performance of the cluster because they cannot take advantage of special hardware extensions, such as enhanced networking or GPU processing, to ensure that the EC2 instances are running.
  For more information about Linux AMI virtualization types, see Linux AMI Virtualization Types. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization\_types.html

- **F. Disable CPU hyperthreading on the EC2 instances.**  
  _✔ Đáp án đúng_

  *Giải thích:* Intel Hyper-Threading Technology makes a single physical processor appear as multiple logical processors. Most HPC applications will benefit from disabling hyperthreading.
  For more information about Intel Hyper-Threading Technology, see Compute. https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute.html

---

## Câu 22 — ✅ Đúng

*Multi-Select · Thời gian làm: 1 minutes 20 seconds*

**Đề bài:**

A company is launching a web-based application in multiple Regions around the world. The application consists of both static content that the company stores in a private Amazon S3 bucket and dynamic content that the company hosts in Amazon ECS containers behind an Application Load Balancer (ALB). The company requires that the static and dynamic application content be accessible through Amazon CloudFront only.

Which combination of steps should a solutions architect recommend to restrict direct content access to CloudFront?

**Đáp án bạn chọn:** B, D, E  
**Đáp án đúng:** B, D, E

**Các lựa chọn và giải thích:**

- **A. Create a web ACL in AWS WAF with a rule to validate the presence of a custom header and associate the web ACL with the CloudFront distribution.**

  *Giải thích:* CloudFront adds the custom header. A web ACL in front of the CloudFront distribution would block any through traffic.
  For more information about how to add custom headers, see Adding Custom Headers to Origin Requests 
  .
  For more information about web ACLs, see Web Access Control Lists (Web ACLs) 
  .

- **B. Configure CloudFront to add a custom header to origin requests.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* CloudFront can add a custom header to a request.
  For more information about how to add customer headers, see Adding Custom Headers to Origin Requests 
  .

- **C. Configure the ALB to add a custom header to HTTP requests.**

  *Giải thích:* ALBs have HTTP(S) listeners. ALBs do not create new headers.
  For more information about ALBs, see What Is an Application Load Balancer?

- **D. Create a web ACL in AWS WAF with a rule to validate the presence of a custom header and associate the web ACL with the ALB.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You can use AWS WAF to validate custom headers. You can associate an AWS WAF web ACL with the ALB.
  For more information about how to add custom headers, see Adding Custom Headers to Origin Requests 
  .
  For more information about web ACLs, see Web Access Control Lists (Web ACLs) 
  .

- **E. Create a CloudFront Origin Access Control (OAC) and add it to the CloudFront distribution. Update the S3 bucket policy to allow access to the OAC only.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You can use an OAC to restrict access to an S3 bucket to viewers who make requests through CloudFront.
  For more information about CloudFront OACs and Amazon S3, see Restricting Access to an Amazon S3 Origin 
  .

- **F. Update the S3 bucket ACL to allow access from the CloudFront distribution only.**

  *Giải thích:* Amazon S3 ACLs define which AWS accounts or groups have access.
  For more information about Amazon S3 ACLs, see Access Control List (ACL) Overview 
  .

---

## Câu 23 — ✅ Đúng

*Multiple Choice · Thời gian làm: 3 minutes 42 seconds*

**Đề bài:**

A company has released a new line of appliances. The appliances use AWS IoT Core sensors that write data to an Amazon S3 bucket several times each day. The company configured the bucket with the S3 Standard storage class. The company accesses data from the most recent 6 months frequently to report usage patterns. The company must store the data indefinitely to meet compliance requirements. A solutions architect needs to reduce costs that are associated with storing the growing dataset in the S3 bucket.

Which storage solution will meet these requirements MOST cost-effectively?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Move the data to a new S3 bucket and set the storage class to S3 Standard-Infrequent Access (S3 Standard-IA). Implement S3 Intelligent-Tiering and set automatic data archiving to begin at 180 days.**

  *Giải thích:* It would cost more to move the data into an S3 Standard-IA bucket than to leave the data in S3 Standard because the company accesses the data frequently during the first 6 months. S3 Standard-IA costs more for each retrieval than S3 Standard costs for each retrieval.
  After 6 months, when the data is no longer frequently accessed, the data should be moved to a less expensive storage class. You can automate the change of storage class with an S3 Lifecycle rule because the access patterns in this scenario are well known and do not change. S3 Intelligent-Tiering is well suited to situations with unknown usage patterns or when access patterns frequently change. S3 Intelligent-Tiering would take time to recognize the change in access patterns and would keep the data in a more expensive storage class longer than necessary.
  For more information about S3 Standard-IA, see Storage Classes for Infrequently Accessed Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-infreq-data-access 
  For more information about S3 Intelligent-Tiering, see Storage Class for Automatically Optimizing Data with Changing or Unknown Access Patterns. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-dynamic-data-access 
  For more information about S3 Lifecycle rules, see Transitioning Objects Using Amazon S3 Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html

- **B. Create a new S3 Intelligent-Tiering configuration for the existing S3 bucket. Set automatic data archiving to begin at 180 days.**

  *Giải thích:* After 6 months, when the data is no longer frequently accessed, the data should be moved to a less expensive storage class. You can automate the change of storage class with an S3 Lifecycle rule because the access patterns in this scenario are well known and do not change. S3 Intelligent-Tiering is well suited to situations with unknown usage patterns or when access patterns frequently change. S3 Intelligent-Tiering would take time to recognize the change in access patterns and would keep the data in a more expensive storage class longer than necessary.
  For more information about S3 Intelligent-Tiering, see Storage Class for Automatically Optimizing Data with Changing or Unknown Access Patterns. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-dynamic-data-access 
  For more information about S3 Lifecycle rules, see Transitioning Objects Using Amazon S3 Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html

- **C. Move the data to a new S3 bucket and set the storage class to S3 Standard-Infrequent Access (S3 Standard-IA). Create an S3 Lifecycle rule to transfer data older than 180 days into S3 Glacier Flexible Retrieval.**

  *Giải thích:* It would cost more to move the data into an S3 Standard-IA bucket than to leave the data in a bucket that uses S3 Standard because the company accesses the data frequently during the first 6 months. S3 Standard-IA costs more for each retrieval than S3 Standard costs for each retrieval.
  For more information about S3 Standard-IA, see Storage Classes for Infrequently Accessed Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-infreq-data-access

- **D. Create a new S3 Lifecycle rule for the existing S3 bucket. Configure the rule with bucket-wide object-tiering settings that will move data into S3 Glacier Deep Archive after 180 days.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* S3 Glacier Deep Archive is suitable when you do not need immediate access to data. S3 Glacier Deep Archive is less expensive than any immediate-access tier, including S3 Standard and S3 Standard-IA. S3 Lifecycle rules are the correct choice to move data for this company because usage patterns do not change.
  For more information about S3 Glacier Deep Archive, see Storage Classes for Archiving Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-glacier 
  For more information about S3 Lifecycle rules, see Transitioning Objects Using Amazon S3 Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html

---

## Câu 24 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 34 seconds*

**Đề bài:**

A company has a multi-tier web application that runs on a fleet of Amazon EC2 instances behind an Application Load Balancer (ALB). The instances are in an Auto Scaling group. The ALB and the Auto Scaling group are replicated in a backup AWS Region. The minimum value and the maximum value for the Auto Scaling group are set to zero. An Amazon RDS Multi-AZ DB instance stores the application's data. The DB instance has a read replica in the backup Region. The application presents an endpoint to end users by using an Amazon Route 53 record.

The company needs to reduce its RTO to less than 15 minutes by giving the application the ability to automatically fail over to the backup Region. The company does not have a large enough budget for an active-active strategy.

Which solution will meet these requirements?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Reconfigure the application's Route 53 record with a latency-based routing policy that load balances traffic between the two ALBs. Create an AWS Lambda function in the backup Region to promote the read replica and modify the Auto Scaling group values. Create an Amazon CloudWatch alarm that is based on the HTTPCode\_Target\_5XX\_Count metric for the ALB in the primary Region. Configure the CloudWatch alarm to invoke the Lambda function.**

  *Giải thích:* Route 53 is a DNS service that translates domain names to IP addresses. Route 53 provides traffic routing, health checking, and domain registration capabilities. This solution is not functional because the Route 53 record will attempt to send traffic to the backup site while the site is still inactive. A failover routing policy would be more suitable for this scenario.
  Learn more about Route 53 routing policies. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

- **B. Create an AWS Lambda function in the backup Region to promote the read replica and modify the Auto Scaling group values. Configure Route 53 with a health check that monitors the web application and raises an Amazon CloudWatch alarm that sends an Amazon SNS notification to the Lambda function when the health check status is unhealthy. Update the application's Route 53 record with a failover policy that routes traffic to the ALB in the backup Region when a health check failure occurs.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Route 53 is a DNS service that translates domain names to IP addresses. Route 53 provides traffic routing, health checking, and domain registration capabilities. A Route 53 health check provides a global scope. This solution can automatically invoke the failover action when in an unhealthy state.
  Learn more about how to monitor Route 53 health checks by using CloudWatch. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-checks.html#monitoring-sns-notification-procedure 
  Learn more about Lambda. https://docs.aws.amazon.com/sns/latest/dg/lambda-console.html

- **C. Configure the Auto Scaling group in the backup Region to have the same values as the Auto Scaling group in the primary Region. Reconfigure the application's Route 53 record with a latency-based routing policy that load balances traffic between the two ALBs. Remove the read replica. Replace the read replica with a standalone RDS DB instance. Configure Cross-Region Replication between the RDS DB instances by using snapshots and Amazon S3.**

  *Giải thích:* Route 53 is a DNS service that translates domain names to IP addresses. Route 53 provides traffic routing, health checking, and domain registration capabilities. This solution is not functional. This solution attempts an active-active disaster recovery. Therefore, this solution violates the budget requirements.
  Learn more about Route 53 routing policies. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

- **D. Configure an endpoint in AWS Global Accelerator with the two ALBs as equal weighted targets. Create an AWS Lambda function in the backup Region to promote the read replica and modify the Auto Scaling group values. Create an Amazon CloudWatch alarm that is based on the HTTPCode\_Target\_5XX\_Count metric for the ALB in the primary Region. Configure the CloudWatch alarm to invoke the Lambda function.**

  *Giải thích:* Global Accelerator provides static IP addresses as fixed entry points for applications. Global Accelerator routes traffic through the AWS global network to the most suitable endpoint based on health, geography, and routing policies. Global Accelerator with equal weighted targets would route about half of the traffic to the backup Region. However, instances in the backup Region are not running because of auto scaling group minimum and maximum values being set to zero.
  Learn more about Global Accelerator. https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html

---

## Câu 25 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 48 seconds*

**Đề bài:**

A company uses several services to store important data within a single AWS Region. These services include Amazon S3, Amazon EBS, Amazon EFS, Amazon RDS, and on-premises storage servers. The company wants a backup and data protection solution that would offer Regional protection for all the company's existing data. The solution must automate the processes on AWS as much as possible. The company has configured AWS Storage Gateway Volume Gateway for the on-premises data.

Which solution will meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Create an AWS Backup backup vault in another Region. Create a cross-Region backup plan in AWS Backup by using the vault that includes data that is in S3 buckets, EBS volumes, EFS file systems, RDS databases, and the Storage Gateway volumes.**  
  _✔ Đáp án đúng_

  *Giải thích:* AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. A cross-Region backup plan would offer the required Regional protection for the data. This solution would incur the least operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html 
  For more information about cross-Region replication for Amazon S3, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario

- **B. Create a read replica of the RDS databases in another Region. Create a cross-Region backup plan in AWS Backup that includes the data that is in S3 buckets, EBS volumes, EFS file systems, and the Storage Gateway volumes.**  
  _☑ Bạn đã chọn_

  *Giải thích:* AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. RDS read replicas are not a backup solution. Read replicas of the RDS databases would not address the requirements but would add unnecessary operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html 
  For more information about RDS read replicas, see Working with Read Replicas. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_ReadRepl.html

- **C. Create EBS snapshots and copy the EBS snapshots to a different Region. Create a cross-Region backup plan in AWS Backup that includes data that is in S3 buckets, EFS file systems, RDS databases, and the Storage Gateway volumes.**

  *Giải thích:* AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. However, it is not necessary to use DataSync to replicate the EBS volumes because AWS Backup can back up EBS volumes. Cross-Region replication would automatically protect the data that is in S3 buckets with less operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html 
  For more information about cross-Region replication for Amazon S3, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario 
  For more information about how to copy EBS snapshots, see Copy an Amazon EBS Snapshot. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html

- **D. Configure AWS DataSync to replicate the data that is in EFS file systems to another Region. Create a cross-Region backup plan in AWS Backup that includes data that is in S3 buckets, EBS volumes, RDS databases, and the Storage Gateway volumes.**

  *Giải thích:* AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. Replicas of the EFS file systems are not necessary and would incur unnecessary operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html 
  For more information about DataSync, see What Is AWS DataSync? https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

---

## Câu 26 — ❌ Sai

*Multi-Select · Thời gian làm: 3 minutes 6 seconds*

**Đề bài:**

A company manages multiple AWS accounts by using AWS Organizations. The company uses AWS Config to continuously audit and evaluate its AWS resources. The company needs to deploy a set of AWS Config rules across almost all accounts, including the management account, while excluding a few accounts. An AWS CloudFormation template already defines the required AWS Config rules. The company wants to ensure consistent application of the rules and wants to prevent any unauthorized modifications.

Which combination of steps will meet these requirements?

**Đáp án bạn chọn:** A, B  
**Đáp án đúng:** B, E

**Các lựa chọn và giải thích:**

- **A. Use AWS CloudFormation StackSets to deploy stacks across all applicable accounts. Perform drift detection frequently to ensure consistency.**  
  _☑ Bạn đã chọn_

  *Giải thích:* CloudFormation StackSets gives you the ability to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation. Drift detection does not prevent unauthorized modifications.
  For more information about CloudFormation StackSets drift detection, see Detecting Unmanaged Configuration Changes in Stack Sets. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html 
  For more information about how to create a stack set, see Create a Stack Set with Service-Managed Permissions. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html#stacksets-orgs-associate-stackset-with-org

- **B. Activate trusted access in Organizations for the relevant service. Register a delegated administrator account to implement the relevant solution.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Organizations is an account-management service in which trusted access allows supported AWS services such as AWS Config to perform tasks across accounts in the organization. AWS Config also supports a delegated administrator that can implement conformance packs across multiple accounts and achieve consistent compliance without any unauthorized modifications.
  For more information about trusted access in Organizations, see AWS Services That You Can Use with AWS Organizations. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_integrate\_services\_list.html

- **C. Deactivate trusted access in Organizations for the relevant service. Activate each individual account administrator to implement the relevant solution.**

  *Giải thích:* Organizations is an account-management service in which trusted access allows supported AWS services such as AWS Config and CloudFormation to perform tasks across accounts in the organization. Performance of these tasks requires trusted access. Individual account administrators are not able to perform these tasks.
  For more information about trusted access in AWS Organizations, see AWS Services That You Can Use with AWS Organizations. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_integrate\_services\_list.html

- **D. Use a CloudFormation template and AWS Service Catalog to launch a product across all applicable accounts. Use CloudFormation to perform drift detection frequently to ensure consistency.**

  *Giải thích:* AWS Service Catalog creates and manages catalogs of IT services and solutions. This service helps achieve compliance with organizational business policies. Drift detection does not prevent unauthorized modifications.
  For more information about CloudFormation drift detection, see Detecting Unmanaged Configuration Changes to Stacks and Resources. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html

- **E. Use AWS Config to deploy an organization conformance pack that uses a CloudFormation template across all the accounts. Include a list of accounts to exclude.**  
  _✔ Đáp án đúng_

  *Giải thích:* AWS Config gives you the ability to continuously asses, audit, and evaluate the configurations of your AWS resources. AWS Config can deploy rules in a conformance pack across all AWS accounts within an organization. AWS Config can include the management account of Organizations and exclude other accounts by using the exclusion list. Only the delegated administrator account can modify the rules deployed by AWS Config. This limit ensures consistent compliance and prevents unauthorized modifications.
  For more information about application of AWS Config rules across accounts in an organization, see Enabling AWS Config Rules Across All Accounts in Your Organization. https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html 
  For more information about management of conformance packs within an organization, see Managing Conformance Packs Across All Accounts in Your Organization. https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-organization-apis.html

---

## Câu 27 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 15 seconds*

**Đề bài:**

A company deploys a serverless application to AWS. A solutions architect needs to develop a reliable and durable solution that logs changes that are made to the application infrastructure. The solution must identify the logs of actions in AWS SDKs and the AWS Management Console. The solution must detect any alterations to log files.

Which solution meets these requirements?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create an AWS CloudTrail trail to record the actions on the application's serverless components. Create a new private S3 bucket to store the logs. Configure S3 server-side file encryption on the S3 bucket that stores the logs.**

  *Giải thích:* CloudTrail records API calls to the AWS infrastructure. Events include actions that are taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs. CloudTrail can deliver events to Amazon S3. Server-side file encryption would not detect alterations to the log files.
  For more information about CloudTrail, see What Is AWS CloudTrail? https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html 
  For more information about server-side encryption, see Protecting Data Using Server-Side Encryption. https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html

- **B. Create two AWS CloudTrail trails: one trail for the AWS SDK actions and one trail for the AWS Management Console actions. Create two private S3 buckets for the logs. Select the server access logging option for the S3 buckets that store the logs.**

  *Giải thích:* CloudTrail records API calls to the AWS infrastructure. Events include actions that are taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs. Two CloudTrail logs would deliver a duplicated stream of logs to Amazon S3. Duplication would make this configuration unnecessary. Use of server access logs would not detect alterations to the log files.
  For more information about CloudTrail, see What Is AWS CloudTrail? https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html 
  For more information about server access logs, see Logging Requests Using Server Access Logging. https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html

- **C. Create two AWS CloudTrail trails: one trail for the AWS SDK actions and one trail for the AWS Management Console actions. Create two private S3 buckets for the logs. Run an Amazon Macie discovery job on the S3 buckets that store the logs.**

  *Giải thích:* CloudTrail records API calls to the AWS infrastructure. Events include actions that are taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs. Two CloudTrail logs would deliver a duplicated stream of logs to Amazon S3. The duplication makes this configuration unnecessary. Macie automates the discovery of sensitive data in Amazon S3. A Macie discovery job would not detect alterations to the log files.
  For more information about CloudTrail, see What Is AWS CloudTrail? https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html 
  For more information about Macie, see What Is Amazon Macie? https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html

- **D. Create an AWS CloudTrail trail to record the actions on the application's serverless components. Create a new private S3 bucket to store the logs. Configure validation of log file integrity on the CloudTrail trail.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* CloudTrail records API calls to the AWS infrastructure. Events include actions that are taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs. CloudTrail can deliver events to Amazon S3. Validation of log file integrity could identify alterations to a log file.
  For more information about CloudTrail, see What Is AWS CloudTrail? https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html 
  For more information about integrity validation, see Validating CloudTrail Log File Integrity. https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html

---

## Câu 28 — ✅ Đúng

*Multiple Choice · Thời gian làm: 3 minutes 3 seconds*

**Đề bài:**

A company currently hosts a popular gaming application with an associated on-premises Redis database. The database stores player and leaderboard data. The company wants to migrate both the application and the Redis database to the AWS Cloud. The company will migrate the application to run on a fleet of Amazon EC2 instances across multiple Availability Zones. The company requires the new database to be durable and to serve traffic with microsecond read latency. The company does not want to manage the database servers after the migration.

Which solution will meet these requirements and store the data in the MOST durable way?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Migrate the on-premises application and the database to separate fleets of EC2 instances by using AWS Transform MGN (previously known as AWS Application Migration Service). Turn on Redis replication with replicas in different Availability Zones.**

  *Giải thích:* Significant server management effort would be necessary to run the database on EC2 instances. The company does not want to manage the database servers.

- **B. Deploy an Amazon MemoryDB cluster to host the database. Configure at least one read replica for the MemoryDB cluster with Multi-AZ activated. Migrate the on-premises application servers by using AWS Transform MGN (previously known as AWS Application Migration Service). Take a snapshot of the existing Redis cluster and upload it to an Amazon S3 bucket. Seed the MemoryDB cluster with the Redis backup data.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* AWS Transform MGN helps make the migration of on-premises servers to EC2 instances seamless. MemoryDB is a durable, in-memory managed database for workloads that require an ultra-fast, primary database. MemoryDB stores successful write operations durably in a distributed Multi-AZ transaction log. You can seed a MemoryDB cluster with a snapshot from an existing Redis cluster. You could access the existing snapshot by uploading the snapshot to an S3 bucket.
  For more information about AWS Transform MGN, see What Is AWS Transform MGN? 
  For more information about MemoryDB, see What Is MemoryDB? 
  For more information about durability and consistency in MemoryDB, see Consistency 
  .
  For more information about how to seed MemoryDB with a Redis snapshot, see Seeding a New Cluster with an Externally Created Snapshot 
  .

- **C. Deploy an Amazon ElastiCache (Redis OSS) cluster to host the database. Configure a Redis replication group with Multi-AZ activated. Migrate the on-premises application servers by using AWS Transform MGN (previously known as AWS Application Migration Service). Take a snapshot of the existing Redis cluster and upload it to an Amazon S3 bucket. Seed the ElastiCache cluster with the Redis backup data.**

  *Giải thích:* Although ElastiCache (Redis OSS) does support Multi-AZ deployment and has backup and recovery features, this service is not the most durable option to store Redis data on AWS because of the potential for data loss. Amazon MemoryDB is better suited for a workload that requires a durable database that provides ultra-fast performance.
  For more information about resilience in ElastiCache (Redis OSS), see Resilience in Amazon ElastiCache 
  .
  For more information about how to choose between MemoryDB and ElastiCache, see Related Services 
  .
  For more information about durability and consistency in MemoryDB, see Consistency 
  .

- **D. Deploy an Amazon MemoryDB cluster to host the database. Configure at least one read replica for the MemoryDB cluster with Multi-AZ activated. Migrate both the on-premises application and the database by using AWS Transform MGN (previously known as AWS Application Migration Service).**

  *Giải thích:* AWS Transform MGN helps make the migration of on-premises servers to EC2 instances seamless. Although AWS Transform MGN can migrate the application to EC2 instances, this service does not support managed databases such as MemoryDB.
  For more information about AWS Transform MGN, see What Is AWS Transform MGN?

---

## Câu 29 — ✅ Đúng

*Multiple Choice · Thời gian làm: 4 minutes 17 seconds*

**Đề bài:**

A company is running an application on Amazon EC2 instances in an Amazon EC2 Auto Scaling group. The Auto Scaling group extends across multiple Availability Zones in a single AWS Region. A new requirement states that the architecture must support a multi-Region, active-active disaster recovery strategy.

The company clones the same architecture to the second Region. The company needs to provide two static IP addresses to customers so that customers can connect to the application without a need for the company to change the configuration. The new architecture must serve requests with the lowest possible latency.

Which solution meets these requirements with the LOWEST latency?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Use Network Load Balancers (NLBs). Create a Route 53 geolocation routing policy that resolves to the two NLBs.**

  *Giải thích:* A Route 53 geolocation routing policy serves traffic based on the geographic location. This solution does not provide the lowest latency because requests would travel across the regular internet instead of the low-latency AWS global network.
  For more information about Route 53 geolocation routing, see Geolocation Routing 
  .

- **B. Use Network Load Balancers (NLBs). Create a Route 53 failover routing record that points to the two NLBs.**

  *Giải thích:* Route 53 failover routing does not dispatch requests with the lowest possible latency. Requests would travel across the regular internet instead of the low-latency AWS global network.
  For more information about Route 53 routing options, see Choosing a Routing Policy 
  .

- **C. Use Application Load Balancers (ALBs). Create a Route 53 latency routing record that points to the two ALBs.**

  *Giải thích:* ALBs do not support static IP addresses. The company needs to provide static IP addresses.
  For more information about Elastic Load Balancing types, see Elastic Load Balancing Types 
  .

- **D. Use Network Load Balancers (NLBs). Configure AWS Global Accelerator to point to the two NLBs.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Global Accelerator simplifies global traffic management by providing two static anycast IP addresses that you would need to configure only once. With Global Accelerator, traffic will remain within the low-latency AWS global network, and the static IP addresses will allow customer applications to connect without the need for reconfiguration.
  For more information about Global Accelerator, see How AWS Global Accelerator Works 
  .
  For more information about how Global Accelerator provides static IP addresses, see Using static IP addresses in AWS Global Accelerator 
  .
  For more information about how Global Accelerator can provide failover capabilities, see Understanding AWS Global Accelerator use cases 
  .

---

## Câu 30 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 47 seconds*

**Đề bài:**

A company is migrating its marketing website and content management system from an on-premises data center to AWS. The company wants the AWS application to be deployed in a VPC with Amazon EC2 instances used for the web servers and an Amazon RDS instance for the database.

The company has a runbook document that describes the installation process of the on-premises system. The company would like to base the AWS system on the processes referenced in the runbook document. The runbook document describes the installation and configuration of the operating systems, network settings, the website, and content management system software on the servers. After the migration is complete, the company wants to be able to make changes quickly to take advantage of other AWS features.

How can the application and environment be deployed and automated in AWS with the LEAST operational overhead, while allowing for future changes?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Write an AWS CloudFormation template that creates the VPC, the EC2 instances, and the RDS instance for the application. Ensure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration.**  
  _☑ Bạn đã chọn_

  *Giải thích:* The CloudFormation template will help you build an automated solution. However, the installation and configuration of the software is still manual.

- **B. Write a Python script that uses the AWS API to create the VPC, the EC2 instances, and the RDS instance for the application. Write shell scripts that implement the rest of the steps in the runbook. Have the Python script copy and run the shell scripts on the newly created instances to complete the installation.**

  *Giải thích:* This solution includes some automation, but a Python script is not the best choice. Significant effort would be necessary to build the script. A Python script will require more operational overhead to handle future updates to the environment than a CloudFormation template will.

- **C. Update the runbook to describe how to create the VPC, the EC2 instances, and the RDS instance for the application by using the AWS Console. Make sure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration.**

  *Giải thích:* This solution does not include significant automation. It would be difficult to change the environment to use other services if necessary.

- **D. Write an AWS CloudFormation template that creates the VPC, the EC2 instances, and the RDS instance for the application. Include EC2 user data in the AWS CloudFormation template to install and configure the software.**  
  _✔ Đáp án đúng_

  *Giải thích:* CloudFormation and Amazon EC2 user data scripts are the best option. You can use stack updates to deploy multiple versions of the template to change the environment in the future.
  For more information about CloudFormation, see AWS CloudFormation Stack Updates 
  .

---

## Câu 31 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 57 seconds*

**Đề bài:**

A company has 10 VPCs in the same AWS Region. The VPCs have CIDR ranges that do not overlap. Based on an initial requirement to separate communications between VPCs, a solutions architect creates two transit gateways. Transit Gateway A (TGW-A) has six VPCs attached: VPC-1 through VPC-6. Transit Gateway B (TGW-B) has four VPCs attached: VPC-7 through VPC-10.

The solutions architect finds out that the networking requirements have changed. The company now requires full communication among all 10 VPCs.

How should the solutions architect change the network configuration to meet this requirement?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Create a gateway VPC endpoint in VPC-7 through VPC-10. Create attachments for the interface VPC endpoints to TGW-A. Create static route table entries for the newly added attachments. Delete TGW-B.**

  *Giải thích:* Gateway VPC endpoints are used to connect Amazon S3 and Amazon DynamoDB by using private IP addresses. Transit gateway connections are called attachments.
  For more information about gateway endpoints, see Gateway Endpoints 
  .

- **B. In another Region, create a new transit gateway. Attach VPC-7 through VPC-10 to the new transit gateway. Create and accept a peering attachment with TGW-A. Create a static route table entry to the new transit gateway.**

  *Giải thích:* For VPCs to be attached to a transit gateway, the VPCs must be in the same Region as the transit gateway.
  For more information about transit gateways, see Transit Gateways 
  .

- **C. Delete the attachments for VPC-7 through VPC-10 from TGW-B. Create attachments for VPC-7 through VPC-10 on TGW-A. Create static route table entries for the newly added attachments. Delete TGW-B.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* The attachment of all the VPCs to one transit gateway will provide full communication among all the VPCs. You must remove the attachments from TGW-B before you delete TGW-B.
  For more information about transit gateways, see Transit Gateways 
  .
  For more information about how to delete transit gateways, see Delete a Transit Gateway 
  .

- **D. Create an interface VPC endpoint in VPC-7 through VPC-10. Create attachments for the interface VPC endpoints to TGW-A. Create static route table entries for the newly added attachments. Delete TGW-B.**

  *Giải thích:* Interface VPC endpoints are used to connect supported services by using private IP addresses. Transit gateway connections are called attachments.
  For more information about interface VPC endpoints, see Interface VPC Endpoints (AWS PrivateLink) 
  .

---

## Câu 32 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 16 seconds*

**Đề bài:**

A company wants to provide desktop as a service (DaaS) to a number of employees using Amazon WorkSpaces. WorkSpaces will need to access files and services hosted on premises with authorization based on the company's Active Directory. Network connectivity will be provided through an existing AWS Direct Connect connection.

The solution has the following requirements:

Credentials from Active Directory should be used to access on-premises files and services.
Credentials from Active Directory should not be stored outside the company.
End users should have single sign-on (SSO) to on-premises files and services once connected to WorkSpaces.

Which strategy should the solutions architect use for end user authentication?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Create a service account in the on-premises Active Directory with the required permissions. Create an AD Connector in AWS Directory Service to be deployed on premises using the service account to communicate with the on-premises Active Directory. Ensure the required TCP ports are open from the WorkSpaces VPC to the on-premises AD Connector. Use the AD Connector as the directory for WorkSpaces.**

  *Giải thích:* You cannot deploy AD Connector on premises.
  For more information about the requirements for AD Connector, see AD Connector Prerequisites. https://docs.aws.amazon.com/directoryservice/latest/admin-guide/prereq\_connector.html

- **B. Create an AWS Managed Microsoft AD directory in the AWS Directory Service within the WorkSpaces VPC. Set up a one-way trust allowing users from the on-premises Active Directory to access resources in the AWS Managed Microsoft AD. Use AWS Managed Microsoft AD as the directory for WorkSpaces. Create an identity provider with IAM from an on-premises ADFS server. Allow users from this identity provider to assume a role with a policy allowing them to run WorkSpaces.**  
  _☑ Bạn đã chọn_

  *Giải thích:* To set up AWS IAM Identity Center with Amazon WorkSpaces Web, you would also need to set up AWS Organizations.
  For more information about how to set up IAM Identity Center for WorkSpaces, see Set Up IAM Identity Center as Your IdP. https://docs.aws.amazon.com/workspaces-web/latest/adminguide/sso-idp.html

- **C. Create a service account in the on-premises Active Directory with the required permissions. Create an AD Connector in AWS Directory Service within the WorkSpaces VPC using the service account to communicate with the on-premises Active Directory. Use the AD Connector as the directory for WorkSpaces.**  
  _✔ Đáp án đúng_

  *Giải thích:* AD Connector is a directory gateway that you can use to redirect directory requests to your on-premises Active Directory without the need to cache any information in the cloud. This solution will authenticate the Active Directory credentials of the end users. The WorkSpaces will be members of the Active Directory that provide SSO to on-premises resources.
  For more information about AD Connector, see Active Directory Connector. https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory\_ad\_connector.html

- **D. Create an AWS Managed Microsoft AD directory within the WorkSpaces VPC. Use the Active Directory Migration Tool (ADMT) with the Password Export Server to copy users from the on-premises Active Directory to AWS Managed Microsoft AD. Set up a one-way trust allowing users from AWS Managed Microsoft AD to access resources in the on-premises Active Directory. Use AWS Managed Microsoft AD as the directory for WorkSpaces.**

  *Giải thích:* This solution copies the users to AWS Managed Microsoft AD. However, the company requires a solution that does not store credentials from Active Directory outside the company.
  For more information about AWS Managed Microsoft AD, see AWS Managed Microsoft AD. https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory\_microsoft\_ad.html

---

## Câu 33 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 29 seconds*

**Đề bài:**

A company has several legacy on-premises C++ applications. The applications are highly integrated and dependent on one another. The servers and operating systems that support the applications are highly customized and fine-tuned. Currently, the company cannot modernize the applications. The company wants to move the applications to AWS. The company requires a highly available and scalable solution.

Which solution will meet these requirements with the LEAST migration effort?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Package the C++ code and create application source bundles. Deploy the bundles to multiple AWS Elastic Beanstalk environments.**

  *Giải thích:* You can use Elastic Beanstalk to quickly deploy and manage applications in the AWS Cloud without the need to learn about the infrastructure that runs the applications. However, the applications are written in C++, which would require the creation of a custom runtime. Additionally, it would take considerable effort to modify the servers that are deployed by Elastic Beanstalk to match the high amount of operating system customization that is needed to support the applications.
  For more information about Elastic Beanstalk, see What Is AWS Elastic Beanstalk? https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html

- **B. Use AWS Transform MGN (previously known as AWS Application Migration Service) to rehost the applications to run on instances in an Amazon EC2 Auto Scaling group.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* A solution that rehosts the existing applications to instances in an Auto Scaling group would provide the high availability and scalability that the company requires. AWS Transform MGN is a highly automated lift-and-shift solution to migrate servers, databases, and applications to the AWS Cloud. This solution would require the least migration effort.
  For more information about AWS Transform MGN, see What Is AWS Transform MGN? https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html?trkcampaign=tw-webinar-series 
  For more information about Auto Scaling groups, see Auto Scaling Groups. https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html

- **C. Containerize the applications. Create Docker-based images and deploy the images to Amazon ECS by using the EC2 launch type.**

  *Giải thích:* Amazon ECS is a scalable and fast container-management service. However, the existing servers have been highly customized to support the applications. Containerization of the applications and their operating systems might require significant migration effort. A better solution would run the applications directly on EC2 instances that the company can manage.
  For more information about Amazon ECS, see What Is Amazon Elastic Container Service? https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html

- **D. Containerize the applications. Create Docker-based images and deploy the images by using Amazon ECS by using the Fargate launch type.**

  *Giải thích:* Fargate runs containers without the need to manage servers or clusters of Amazon EC2 instances. However, the existing servers have been highly customized to support the applications. Containerization of the applications and their operating systems might require significant migration effort. A better solution would run the applications directly on EC2 instances that the company can manage.
  For more information about Fargate, see Amazon ECS on AWS Fargate. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS\_Fargate.html

---

## Câu 34 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 18 seconds*

**Đề bài:**

A company recently deployed a prototype application on an Amazon EC2 instance that runs Linux. The EC2 instance uses a Provisioned IOPS SSD Amazon EBS volume. The prototype application was successful, and the company plans to deploy the application to production.

The application has one step that produces an output file for subsequent steps to read and update. The company plans to run two copies of the application. It is possible to process the individual steps on different servers. A solutions architect needs to update the architecture to be highly available for both the files and the application.

Which solution will meet these requirements?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Deploy a second EC2 instance in another Availability Zone with an identical EBS volume. Configure AWS DataSync to synchronize data between the two EBS volumes.**

  *Giải thích:* DataSync can move data between some AWS storage services. However, DataSync does not work with EBS volumes.
  For more information about DataSync, see What Is AWS DataSync? https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

- **B. Deploy a second EC2 instance in another AWS Region. Create an Amazon EFS file system that uses EFS Standard storage. Configure both EC2 instances with shared access to the EFS file system.**

  *Giải thích:* Shared access is needed because steps can be processed on different servers. An EFS file system with EFS Standard storage would provide both EC2 instances with shared access to the data. However, EC2 instances can access an EFS shared file system only if the EFS file system is in the same Region as the EC2 instances.
  For more information about Amazon EFS, see What Is Amazon Elastic File System? https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html

- **C. Deploy a second EC2 instance in another Availability Zone. Configure EBS Multi-Attach to share access to the files from both EC2 instances.**

  *Giải thích:* Shared access is needed because steps can be processed on different servers. With EBS Multi-Attach, multiple instances could access the EBS volume. However, the instances must be in the same Availability Zone. Additionally, EBS Multi-Attach would not provide high availability protection for the data.
  For more information about EBS Multi-Attach, see Attach a Volume to Multiple Instances with Amazon EBS Multi-Attach. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html

- **D. Deploy a second EC2 instance in another Availability Zone. Create an Amazon EFS file system that uses EFS Standard storage. Configure both EC2 instances with shared access to the EFS file system.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Deployment of a second EC2 instance in another Availability Zone would improve the availability of the application. Shared access is needed because steps can be processed on different servers. An EFS file system with EFS Standard storage would provide both EC2 instances with shared access to the data. Additionally, the EFS file system would automatically provide high availability for the data.
  For more information about Amazon EFS, see What is Amazon Elastic File System? https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html

---

## Câu 35 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 55 seconds*

**Đề bài:**

A company has created an Amazon CloudFront distribution with two Amazon S3 buckets as origins. The company discovers that objects in both S3 buckets are publicly accessible. The desired state for the first S3 bucket is to allow access through CloudFront and other AWS resources with appropriate permissions. Objects in the second S3 bucket should be accessible only through CloudFront for all users except for the S3 bucket owner.

How should a solutions architect configure access to the buckets to meet these requirements?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Create a separate S3 bucket policy for each S3 bucket. Configure the policy for the first S3 bucket to allow read access to appropriate AWS resources and the CloudFront distribution as principals. Configure the policy for the second S3 bucket to allow only read access for the CloudFront distribution as the principal.**

  *Giải thích:* You can use an S3 bucket policy to restrict access to the objects. However, you cannot list a CloudFront distribution as a principal. An OAC must represent the CloudFront distribution for both bucket policies.

- **B. Create a separate origin access control (OAC) for the CloudFront distribution for each S3 bucket. Create an S3 bucket policy for the first S3 bucket that allows access to the appropriate AWS resources and the OAC as principals. Create an S3 bucket policy for the second S3 bucket that allows access to the appropriate OAC as the principal.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* An OAC is a special CloudFront user that is associated with S3 origins to secure all or some S3 content. You can use an S3 bucket policy to restrict access to the objects. You can list an OAC as a principal in a resource policy.
  For more information about how to use an OAC to restrict access to S3 content, see Restricting Access to an Amazon S3 Origin 
  .
  For more information about resource-based policies, see Identity-Based Policies and Resource-Based Policies 
  .

- **C. Create a separate origin access control (OAC) for the CloudFront distribution for each S3 bucket. Configure the first OAC to include access for the other AWS resources. Configure the second OAC to include only CloudFront. Update the S3 bucket policies to restrict access to the correct OACs.**

  *Giải thích:* An OAC is a special CloudFront user that is associated with S3 origins to secure all or some of the S3 content. However, an OAC cannot include principal information from AWS resources other than CloudFront.

- **D. Create an IAM policy and an IAM role that allow access to the first S3 bucket. Assign the role to the CloudFront distribution and the other resources that need access to the first S3 bucket. Create an origin access control (OAC) for the CloudFront distribution. Create an S3 bucket policy for the second S3 bucket that allows access only with the OAC as the principal.**

  *Giải thích:* You can assign an IAM role to certain AWS resources. However, you cannot assign an IAM role to a CloudFront distribution.

---

## Câu 36 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 51 seconds*

**Đề bài:**

A company must migrate some on-premises Linux applications to the AWS Cloud. The applications are independent, complex, and backed by MySQL databases. The company wants to eliminate the Linux administration work that is necessary to support these applications. Time constraints require a solution with minimal application redesign and coding.

Which solution will meet these requirements with the LEAST operational effort?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Implement the applications by using AWS Lambda. Use AWS Step Functions to coordinate the logical flow of the functions. Migrate the databases to run on Amazon RDS for MySQL.**

  *Giải thích:* A solution that refactors each complex application by using Lambda and Step Functions would require a high level of operational effort. Containerization of the applications should be straightforward because the applications are independent. A solution that containerizes the applications would require less operational effort.
  For more information about Lambda, see Getting Started with Lambda. https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html 
  For more information about how to use Docker to launch containers, see Docker Basics for Amazon ECS. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html

- **B. Containerize the applications. Manage the applications as tasks in Amazon ECS with the Fargate launch type. Migrate the databases to run on Amazon RDS for MySQL.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Containerization of the applications should be straightforward because the applications are independent. You can use Amazon ECS to run, stop, and manage containers on a cluster. The Fargate launch type removes the need to manage the underlying hosts and eliminates the Linux administration work. This solution also eliminates the need to manage the operating system at the backend by migrating the databases to Amazon RDS.
  For more information about how to use Docker to launch containers, see Docker Basics for Amazon ECS. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html 
  For more information about Amazon ECS on Fargate, see Amazon ECS on AWS Fargate. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS\_Fargate.html 
  For more information about Amazon RDS, see What Is Amazon Relational Database Service (Amazon RDS)? https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html

- **C. Implement the applications by using AWS Lambda. Use AWS Step Functions to coordinate the logical flow of the functions. Migrate the databases to run on Amazon DynamoDB.**

  *Giải thích:* A solution that refactors each complex application by using Lambda and Step Functions would require a high level of operational effort. Containerization of the applications should be straightforward because the applications are independent. A solution that containerizes the applications would require less operational effort. Migration of the relational MySQL databases to DynamoDB would also require significant effort.
  For more information about Lambda, see Getting Started with Lambda. https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html 
  For more information about how to use Docker to launch containers, see Docker Basics for Amazon ECS. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html 
  For more information about the differences between relational databases and NoSQL databases such as DynamoDB, see From SQL to NoSQL. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html

- **D. Containerize the applications. Manage the applications as tasks in Amazon ECS with the EC2 launch type. Migrate the databases to run on Amazon RDS for MySQL.**

  *Giải thích:* ECS clusters that use the EC2 launch type require ongoing operating system management. This solution fails to eliminate the Linux administration that is necessary to support these applications. A better solution would be serverless.
  For more information about ECS clusters, see Amazon ECS Clusters. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html

---

## Câu 37 — ✅ Đúng

*Multiple Choice · Thời gian làm: 5 minutes 5 seconds*

**Đề bài:**

A company has a website that enables users to upload videos. Company policy states the uploaded videos must be analyzed for restricted content. An uploaded video is placed in Amazon S3, and a message is pushed to an Amazon SQS queue with the video's location. A backend application pulls this location from Amazon SQS and analyzes the video.

The video analysis is compute-intensive and occurs sporadically during the day. The website scales with demand. The video analysis application runs on a fixed number of instances. Peak demand occurs during the holidays, so the company must add instances to the application during this time. All instances used are currently on-demand Amazon EC2 T2 instances. The company wants to reduce the cost of the current solution.

Which of the following solutions is MOST cost-effective?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Keep the website on T2 instances. Determine the minimum number of website instances required during off-peak times and use Spot Instances to cover them while using Reserved Instances to cover peak demand. Use Amazon EC2 R4 and Amazon EC2 R5 Reserved Instances in an Auto Scaling group for the video analysis application.**

  *Giải thích:* The memory-focused R family is not the best use case for compute-intensive video analysis. If you use Spot Instances to cover the minimum off-peak website demand, you may not achieve the total target capacity. Reserved Instances are cost-effective when there is a predictable pattern of usage. However, the video analysis task is sporadic.

- **B. Keep the website on T2 instances. Determine the minimum number of website instances required during off-peak times and use Reserved Instances to cover them while using On-Demand Instances to cover peak demand. Use Spot Fleet for the video analysis application comprised of Amazon EC2 C4 and Amazon EC2 C5 Spot Instances.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* It is cost-effective to use Reserved Instances to cover predictable website traffic off-peak. On-Demand instances are cost-effective for unpredictable holiday peak traffic. A fleet of Spot Instances for a sporadic video analysis application is cost-effective. C4 and C5 Spot Instances are the best fit for the video analysis application because this application is compute intensive.
  For more information about cost optimization with Spot Instances, see When to Use Spot Instances 
  .
  For more information about EC2 instance use cases, see Amazon EC2 Instance Types 
  .
  For more information about how to choose the correct EC2 instance type, see How Do I Choose the Appropriate EC2 Instance Type for My Workload? 
  For more information about EC2 Reserved Instances, see Amazon EC2 Reserved Instances 
  .

- **C. Migrate the website to AWS Elastic Beanstalk and Amazon EC2 C4 instances. Determine the minimum number of website instances required during off-peak times and use On-Demand Instances to cover them while using Spot capacity to cover peak demand. Use Spot Fleet for the video analysis application comprised of C4 and Amazon EC2 C5 instances.**

  *Giải thích:* Compute-optimized C4 instances are not as cost-effective for web servers as T2 instances. On-Demand instances are not the most cost-effective option for the predictable off-peak traffic.
  For more information about Amazon EC2 Reserved Instances, see Amazon EC2 Reserved Instances. https://aws.amazon.com/ec2/pricing/reserved-instances/

- **D. Migrate the website to AWS Elastic Beanstalk and Amazon EC2 R4 instances. Determine the minimum number of website instances required during off-peak times and use Reserved Instances to cover them while using On-Demand Instances to cover peak demand. Use Spot Fleet for the video analysis application comprised of R4 and Amazon EC2 R5 instances.**

  *Giải thích:* R4 instances are memory optimized and are not as cost-effective for web servers as T2 instances. Additionally, the memory-focused R family is not the best use case for compute-intensive video analysis.

---

## Câu 38 — ❌ Sai

*Multiple Choice · Thời gian làm: 5 minutes 1 seconds*

**Đề bài:**

A company has developed a single-page web application in JavaScript. The source code is stored in a single Amazon S3 bucket in the us-east-1 Region. The company serves the web application to a global user base through Amazon CloudFront.

The company wants to experiment with two versions of the website without informing application users. Each version of the website will reside in its own S3 bucket. The company wants to determine which version is most successful in marketing a new product.

The solution must send application users that are based in Europe to the new website design. The solution must send application users that are based in the United States to the current website design. However, some exceptions exist. The company needs to be able to redirect specific users to the new website design, regardless of the users' location.

Which solution meets these requirements?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Configure two CloudFront distributions. Configure a geolocation routing policy in Amazon Route 53 to route traffic to the appropriate CloudFront endpoint based on the location of clients.**

  *Giải thích:* A geolocation policy routes traffic based on the location of client. However, the company requires some exceptions to the forwarding rules. Rule exceptions are available through Route 53.
  For more information about how to use Route 53 to route traffic based on user geographic location, see Geolocation Routing. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html 
  For more information about Route 53 routing options, see Choosing a Routing Policy. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

- **B. Configure a single CloudFront distribution. Configure an alternate domain name on the distribution. Configure two behaviors to route users to the different S3 origins based on the domain name that the client uses in the HTTP request.**

  *Giải thích:* This solution allows users to route themselves by the HTTP request the users submit. However, the company requires a solution that routes users based on user location. The different domain names would inform the users of the two different website versions.
  For more information about how to configure CloudFront for multiple origins and behaviors, see Can I Use a Single CloudFront Web Distribution to Serve Content from Multiple Origins Using Multiple Behaviors? https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-distribution-serve-content/

- **C. Configure a single CloudFront distribution with Lambda@Edge. Use Lambda@Edge to send user requests to different origins based on request attributes.**  
  _✔ Đáp án đúng_

  *Giải thích:* You can use Lambda@Edge to dynamically route users to any origin from a CloudFront distribution based on request attributes such as headers. You can use this strategy to serve different versions of pages for A/B testing.
  For more information about how to use Lambda@Edge for A/B testing, see Example: A/B Testing. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-a-b-testing 
  For more information about how to use Lambda@Edge for custom responses based on user location, see Example: Redirecting Viewer Requests to a Country-Specific URL. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirect-based-on-country 
  For more information about how to initiate a Lambda function before CloudFront forwards a request, see Customizing at the Edge with Lambda@Edge. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html

- **D. Configure a single CloudFront distribution. Create a behavior with different paths for each version of the site. Configure Lambda@Edge on the default path to generate redirects and send the client to the correct version of the website.**  
  _☑ Bạn đã chọn_

  *Giải thích:* This solution would inform the user of the different versions by the different paths. You would associate Lambda@Edge with a CloudFront distribution, not a path.
  For more information about how to attach Lambda@Edge to a CloudFront distribution, see Get Started Creating and Using Lambda@Edge Functions. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works.html

---

## Câu 39 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 32 seconds*

**Đề bài:**

A company is migrating its on-premises file transfer solution to AWS Transfer Family. The on-premises host includes an SFTP server to receive files, an application that performs a transformation of the files, and a messaging server. The transformations run every 5 minutes. When a transformation is complete, the application sends a message to a queue on the messaging server.

The company needs to simplify the solution and reduce the management of the components.

Which solution will meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Configure Transfer Family to use Amazon S3 storage. Use Amazon EMR Serverless to perform the transformations. Configure Amazon EMR to send a message to an Amazon SNS topic when a file has been transformed.**

  *Giải thích:* Amazon EMR Serverless requires Spark and Hive expertise. Amazon EMR Serverless requires understanding of distributed computing concepts and management of job submission and orchestration. Therefore, this approach adds significant operational overhead. Amazon EMR is designed for big data processing workloads, not for simple file transformations. Therefore, Amazon EMR is unnecessarily complex for this use case.
  Learn more about Amazon EMR Serverless. https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html

- **B. Configure Transfer Family to use Amazon EFS storage. Create an AWS Glue time-based job to run every 5 minutes to initiate an AWS Glue transformation. Configure AWS Glue to send a message to an Amazon SQS queue when a file has been transformed.**

  *Giải thích:* Using time-based jobs that run every 5 minutes is less efficient than event-driven processing. Additionally, EFS storage with Transfer Family requires managing file system access. For an AWS Glue ETL job to place a message in SQS queue, you must write code. Therefore, this approach requires additional operational overhead.
  Learn more about Transfer Family. https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html

- **C. Configure Transfer Family to use Amazon EFS storage. Use a cron job on Amazon EC2 instances to perform the transformations. Configure the cron job to publish a message to an Amazon SNS topic when a file has been transformed.**

  *Giải thích:* Managing EC2 instances increases operational overhead. This approach does not simplify the solution.
  Learn more about Amazon EC2. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html 
  Learn more about Amazon EFS. https://docs.aws.amazon.com/transfer/latest/userguide/requirements-efs.html

- **D. Configure Transfer Family to use Amazon S3 storage. Configure an Amazon EventBridge rule to invoke an AWS Glue ETL job that performs the transformations after data is uploaded to Amazon S3. Configure an EventBridge rule to send a message to an Amazon SQS queue when the AWS Glue ETL job completes the data transformation.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Transfer Family with S3 storage provides serverless file storage. An EventBridge rule can trigger AWS Glue ETL jobs automatically when files arrive. This approach eliminates the need for scheduled polling. AWS Glue is a fully managed ETL service that can perform transformations. You can use another EventBridge rule to place a message in SQS queue when the AWS Glue ETL job finishes. This solution requires the least operational overhead.
  Learn more about Transfer Family. https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html 
   
  Learn more about AWS Glue. https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html 
  Learn more about EventBridge. https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html

---

## Câu 40 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 39 seconds*

**Đề bài:**

A multi-node application runs on Amazon EC2 instances that run in several subnets within the same VPC. Instance A (172.31.16.139) initiates communication to Instance B (10.10.128.14) on port 5001. Communication between the instances is not successful. A solutions architect analyzes VPC flow logs to identify the problem and discovers the following log entries:

2 123456789010 eni‑1235b8ca123456789 172.31.16.139 10.10.128.14 20641 5001 6 20 4249 1418530010 1418530070 ACCEPT OK

2 123456789010 eni‑1235b8ca123456789 10.10.128.14 172.31.16.139 5001 20641 6 20 4249 1418530192 1418530265 REJECT OK

Which solution will resolve this problem?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Modify any host-based firewalls on Instance B to allow inbound communications on TCP port 20641.**

  *Giải thích:* VPC flow logs represent metadata about network packets that flow through the VPC. VPC flow logs do not contain information that indicates what the operating system of an instance will accept or reject.
  For more information about VPC flow logs and what they capture, see Flow Logs Basics. https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-basics

- **B. Modify the inbound rules for the security group on eni-1235b8ca123456789 to allow port 20641.**

  *Giải thích:* VPC flow logs represent metadata about network packets that flow through the VPC. Network traffic appears to be allowed to exit the network interface. However, the response is not allowed. Security groups are stateful and would automatically allow return traffic.
  For more information about VPC flow logs and what they capture, see Flow Logs Basics. https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-basics 
  For more information about security groups and network ACL interpretation within the VPC Flow Logs, see Security Group and Network ACL Rules. https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html#flow-log-example-security-groups

- **C. Modify the main route table in the VPC to allow inbound and outbound traffic to both instances.**

  *Giải thích:* VPC flow logs represent metadata about network packets that flow through the VPC. This is not a routing problem because the logs indicate that the traffic has been rejected at the network interface.
  For more information about VPC flow logs and what they capture, see Flow Logs Basics. https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-basics 
  For more information about the local route, see Routes. https://docs.aws.amazon.com/vpc/latest/userguide/VPC\_Route\_Tables.html#route-table-routes

- **D. Modify the network ACL in the Instance B subnet to allow outbound communications on port 20641.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* VPC flow logs represent metadata about network packets that flow through the VPC. Network traffic appears to be allowed to exit the network interface. However, the response is not allowed. The problem must be with the network ACL because security groups are stateful and would automatically allow return traffic. Reconfiguration of the network ACL to allow traffic to return on the appropriate ports is the correct solution.
  For more information about VPC flow logs and what they capture, see Flow Logs Basics. https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-basics 
  For more information about security groups and network ACL interpretation within the VPC flow logs, see Security Group and Network ACL Rules. https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html#flow-log-example-security-groups

---

## Câu 41 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 26 seconds*

**Đề bài:**

An ecommerce company wants to migrate its order processing system to AWS. The order processing system is a Java-based application with a backend Oracle database. Most order processing occurs in less than 1 minute. The company will update its frontend website to accommodate a cloud-based solution. The company does not want to manage servers on AWS. The company has extensive Oracle database expertise and wants to use this expertise as part of the solution.

Which solution will meet these requirements?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Use Amazon EC2 instances in an Amazon EC2 Auto Scaling group to host the Java-based order processing application. Use an Amazon RDS for Oracle DB instance with a Multi-AZ deployment as the backend database.**

  *Giải thích:* This solution proposes to host the Java-based order processing application on EC2 instances. This solution does not meet the requirements because the company does not want to manage servers on AWS.
  For more information about serverless computing options on AWS, see Serverless Computing. https://aws.amazon.com/serverless/?nc=sn&loc=0 
  For more information about Amazon EC2, see Amazon Elastic Compute Cloud Documentation. https://docs.aws.amazon.com/ec2/index.html

- **B. Use Amazon SQS to hold the orders. Use AWS Lambda functions to capture and process the orders. Use an Amazon RDS for Oracle DB instance with a Multi-AZ deployment as the backend database.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* The use of Amazon SQS, Lambda, and Amazon RDS will eliminate the need to manage servers on AWS. This solution meets all the company's requirements.
  For more information about Oracle on Amazon RDS, see Oracle on Amazon RDS. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP\_Oracle.html 
  For more information about Amazon SQS, see What Is Amazon Simple Queue Service? https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html 
  For more information about Lambda, see What Is AWS Lambda? https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

- **C. Use Amazon Kinesis Data Streams to hold the orders. Use AWS Lambda functions to capture and process the orders. Convert the backend database to Amazon DynamoDB.**

  *Giải thích:* To use DynamoDB as the database, you would need to convert the Oracle database to DynamoDB. This solution does not meet the requirements because the company wants to continue to use its current Oracle database expertise.
  For more information about serverless computing options on AWS, see Serverless Computing. https://aws.amazon.com/serverless/?nc=sn&loc=0 
  For more information about DynamoDB, see What Is Amazon DynamoDB? https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

- **D. Use Amazon SQS to hold the orders. Use AWS Lambda functions to capture and process the orders. Convert the backend database to Amazon Aurora.**

  *Giải thích:* To use Aurora as the backend database, you would need to convert the Oracle database to Aurora. This solution does not meet the requirements because the company wants to continue to use its current Oracle database expertise.
  For more information about serverless computing options on AWS, see Serverless Computing. https://aws.amazon.com/serverless/?nc=sn&loc=0 
  For more information about Aurora, see What Is Amazon Aurora? https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP\_AuroraOverview.html

---

## Câu 42 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 40 seconds*

**Đề bài:**

A company runs a group of Amazon EC2 instances in private subnets. The EC2 instances store a small amount of infrequently updated data in an Amazon S3 bucket that is in the same AWS Region. A solutions architect creates a gateway VPC endpoint to allow the EC2 instances to access the S3 bucket. The company has a second group of EC2 instances in private subnets in a second Region. The second group of EC2 instances use the S3 bucket's public endpoint for read-only activity.

The company is experiencing higher data-transfer costs because of increased repetitive read activity by the second group of EC2 instances. The company needs a lower-cost solution that will give the second group of EC2 instances read access to the data.

Which solution will meet these requirements MOST cost-effectively?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Create an interface VPC endpoint for the S3 bucket in the VPC in the first Region by using AWS PrivateLink. Peer the VPCs and establish routing between the VPCs. Configure access to the S3 bucket from the EC2 instances in the second Region.**

  *Giải thích:* Interface VPC endpoints allow instances that run in a VPC to connect to other AWS services privately through an elastic network interface. However, interface VPC endpoints incur a cost. The additional cost to read the data frequently from a second Region would increase the data-transfer cost. Replication of a small amount of data to an S3 bucket in a different Region would be more cost-effective.
  For more information about interface endpoints for Amazon S3, see AWS PrivateLink for Amazon S3. https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html

- **B. Create an Amazon EFS file system in each Region. Transfer all the data from the S3 bucket to one of the EFS file systems. Use AWS DataSync to synchronize the EFS file systems. Create mount points in each subnet for EC2 access.**

  *Giải thích:* Amazon EFS provides simple and scalable file storage for use with EC2 instances. DataSync is an online data-transfer service that simplifies, automates, and accelerates data transfer between AWS storage services. CRR would be a more cost-effective solution.
  For more information about Amazon EFS, see What Is Amazon Elastic File System? https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html 
  For more information about DataSync, see What Is AWS DataSync? https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html 
  For more information about CRR, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario

- **C. Create a second S3 bucket in the second Region. Create a gateway VPC endpoint for the second S3 bucket. Allow the EC2 instances in the second Region to communicate with the second S3 bucket. Configure S3 Cross-Region Replication (CRR) between the two S3 buckets.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Gateway VPC endpoints allow resources in AWS to access an S3 bucket without crossing the internet. S3 CRR replicates objects between the two S3 buckets in different Regions. This solution would meet the requirements because the cost of S3 storage is low for a small amount of data. There is no cost for gateway VPC endpoints, and there would be charges only for data transfer between Regions when infrequent changes are made. When the new instances in the second Region repetitively read the data in the S3 bucket, there would be no data-transfer charges.
  For more information about gateway VPC endpoints, see Gateway VPC Endpoints. https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html 
  For more information about when to use CRR, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario

- **D. Create a second S3 bucket in the second Region. Create a gateway VPC endpoint for the second S3 bucket. Allow the EC2 instances in the second Region to communicate with the second S3 bucket. Use an AWS Lambda function to copy objects between the two S3 buckets.**

  *Giải thích:* This solution would not meet the requirements because it adds the costs associated with the use of Lambda to replicate the objects. CRR would provide the same functionality with no additional cost beyond the basic data-transfer cost.
  For more information about Lambda, see What Is AWS Lambda? https://docs.aws.amazon.com/lambda/latest/dg/welcome.html 
  For more information about CRR, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario

---

## Câu 43 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 15 seconds*

**Đề bài:**

A company has an Amazon S3 bucket that contains millions of unencrypted objects. To comply with a recent security audit, a solutions architect needs to ensure that all objects are encrypted and needs to compile a list of objects that contain sensitive data. Many applications access objects in the S3 bucket, and the development team has limited resources.

Which solution will meet these requirements with the LEAST development effort?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Run an Amazon Inspector report against the S3 bucket to identify sensitive data. Modify the S3 bucket to enable default encryption. Use an Amazon S3 Inventory report and Amazon S3 Batch Operations to encrypt the existing unencrypted objects in the same S3 bucket.**

  *Giải thích:* Amazon Inspector is an automated service that continually scans AWS workloads for software vulnerabilities and unintended network exposure. However, Amazon Inspector does not examine S3 buckets for sensitive data.
  For more information about Amazon Inspector, see What is Amazon Inspector? https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html

- **B. Run an Amazon Macie report on the S3 bucket to identify sensitive data. Modify the S3 bucket to enable default encryption. Use an S3 Inventory report and S3 Batch Operations to encrypt the existing unencrypted objects in the same S3 bucket.**  
  _✔ Đáp án đúng_

  *Giải thích:* Macie is a service that can identify sensitive data in Amazon S3. You can use an S3 Inventory report to create a list of objects that need to be encrypted. You can use that list as the manifest for S3 Batch Operations to encrypt existing data. No code changes are necessary for the applications that access the S3 objects.
  For more information about Macie, see What is Amazon Macie? https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html 
  For more information about S3 encryption, see Encrypting Existing Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html

- **C. Run an Amazon Macie report on the S3 bucket to identify sensitive data. Create a new S3 bucket with default encryption enabled. Transfer the unencrypted objects to the new S3 bucket. Update the applications to access the new S3 bucket.**  
  _☑ Bạn đã chọn_

  *Giải thích:* Macie is a service that can identify sensitive data in Amazon S3. However, additional development effort would be required to move the objects to a new S3 bucket and to update all the applications. You would have to inspect the code of each application for usage of the old S3 bucket names, update the code, and test the code.
  For more information about Macie, see What is Amazon Macie? https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html 
  For more information about S3 encryption, see Encrypting Existing Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html

- **D. Run an Amazon Inspector report on the S3 bucket to identify sensitive data. Create a new S3 bucket with default encryption enabled. Transfer the unencrypted objects to the new S3 bucket. Update the applications to access the new S3 bucket.**

  *Giải thích:* Amazon Inspector is an automated service that continually scans AWS workloads for software vulnerabilities and unintended network exposure. However, Amazon Inspector does not examine S3 buckets for sensitive data.
  For more information about Amazon Inspector, see What is Amazon Inspector? https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html

---

## Câu 44 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 36 seconds*

**Đề bài:**

A company has multiple AWS accounts as part of an organization created with AWS Organizations. Each account has a VPC in the us-east-2 Region and is used for either production or development workloads. Amazon EC2 instances across production accounts need to communicate with each other, and EC2 instances across development accounts need to communicate with each other, but production and development instances should not be able to communicate with each other.

To facilitate connectivity, the company created a common network account. The company used AWS Transit Gateway to create a transit gateway in the us-east-2 Region in the network account and shared the transit gateway with the entire organization by using AWS Resource Access Manager. Network administrators then attached VPCs in each account to the transit gateway, after which the EC2 instances were able to communicate across accounts. However, production and development accounts were also able to communicate with one another.

Which set of steps should a solutions architect take to ensure production traffic and development traffic are completely isolated?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Create a tag on each VPC attachment with a value of either production or development, according to the type of account being attached. Using the Network Manager feature of AWS Transit Gateway, create policies that restrict traffic between VPCs based on the value of this tag.**

  *Giải thích:* You use Transit Gateway Network Manager to monitor your global network, both on AWS and on premises. Transit Gateway Network Manager cannot create policies to restrict traffic based on tags.
  For more information about Transit Gateway Network Manager, see AWS Transit Gateway Network Manager 
  .

- **B. Create separate route tables for production and development traffic. Delete each account's association and route propagation to the default AWS Transit Gateway route table. Attach development VPCs to the development AWS Transit Gateway route table and production VPCs to the production route table, and enable automatic route propagation on each attachment.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Divide the network by creating multiple route tables in Transit Gateway and associate VPCs and VPNs to the route tables. Then you can create isolated networks inside a transit gateway similar to virtual routing and forwarding (VRFs) in traditional networks. The transit gateway will have a default route table.
  For more information about Transit Gateway, see AWS Transit Gateway FAQs 
  For more information about how transit gateways work, see How Transit Gateways Work 
  .

- **C. Create a tag on each VPC attachment with a value of either production or development, according to the type of account being attached. Modify the AWS Transit Gateway routing table to route production tagged attachments to one another and development tagged attachments to one another.**

  *Giải thích:* You use Transit Gateway route tables to configure routing for your transit gateway attachments. Transit Gateway route tables route traffic based on CIDRs, not tags.
  For more information about route tables, see Work with Route Tables 
  .
  For more information about how transit gateways work, see How Transit Gateways Work 
  .

- **D. Modify the security groups assigned to development EC2 instances to block traffic from production EC2 instances. Modify the security groups assigned to production EC2 instances to block traffic from development EC2 instances.**

  *Giải thích:* Security groups control the traffic that can reach and leave resources. Security groups implicitly deny traffic. You can create allow rules but not deny rules. When you first create a security group, it has no inbound rules. Therefore, no inbound traffic is allowed until you add inbound rules to the security group.
  For more information about how to use security groups to control traffic, see Control Traffic to Resources Using Security Groups 
  .

---

## Câu 45 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 40 seconds*

**Đề bài:**

A company plans to deploy a web application that will serve a global audience. The company will deploy the application by using Amazon EC2 instances across two AWS Regions. The company will create an Amazon Aurora global database, with a primary Aurora DB cluster in the first Region and a secondary Aurora DB cluster in the second Region. The company needs to minimize latency and ensure read-after-write consistency for the application’s database operations. The company also wants to regularly test its disaster recovery (DR) procedures to minimize data loss and maximize recovery speed across the two Regions.

Which solution will meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Use the secondary Aurora DB cluster endpoint to perform read and write operations. Configure write forwarding to forward write operations to the primary Aurora DB cluster endpoint. Test the DR procedure by using managed planned failover.**  
  _✔ Đáp án đúng_

  *Giải thích:* An Aurora global database replicates data with minimal replication lag to a secondary Aurora DB cluster in another Region. This process optimizes read operations for the company's global audience. Write forwarding will allow the secondary DB cluster to accept write operations and will forward write operations to the primary DB cluster. Aurora handles networking across Regions. Aurora also provides multiple consistency modes for the strongest read-after-write consistency, including global consistency. Finally, managed planned failover automatically handles demotion, promotion, and all synchronization across the clusters with no data loss and faster recovery.
  For more information about write forwarding in an Aurora global database, see Using Write Forwarding in an Amazon Aurora Global Database. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding.html 
  For more information about planned failover, see Using failover in an Amazon Aurora Global Database. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover

- **B. Use the secondary Aurora DB cluster endpoint to perform read and write operations. Configure write forwarding to forward write operations to the primary Aurora DB cluster endpoint. Test the DR procedure by using manual unplanned failover.**

  *Giải thích:* A manual unplanned failover process requires the manual performance of a series of tasks. You must detach and promote a secondary DB cluster. These steps are not suitable for the company's plan to test on a regular and frequent basis. A better solution would use managed planned failover, which would eliminate the manual steps and require less operational overhead.
  For more information about recovery from unplanned outages, see Recovering an Amazon Aurora Global Database from an Unplanned Outage. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover

- **C. Use the secondary Aurora DB cluster endpoint to perform read operations. Use the primary Aurora DB cluster endpoint to perform write operations. Test the DR procedure by using manual unplanned failover.**  
  _☑ Bạn đã chọn_

  *Giải thích:* An Aurora global database replicates data with minimal replication lag to a secondary Aurora DB cluster in another Region. This process optimizes read operations for the company's global audience. However, these read operations could provide stale information. This process will not achieve the required read-after-write consistency.
  For more information about Aurora global databases, see Using Amazon Aurora Global Databases. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html

- **D. Use the secondary Aurora DB cluster endpoint to perform read operations. Use the primary Aurora DB cluster endpoint to perform write operations. Test the DR procedure by using managed planned failover.**

  *Giải thích:* An Aurora global database replicates data with minimal replication lag to a secondary Aurora DB cluster in another Region. This process optimizes read operations for the company's global audience. However, these read operations could provide stale information. This process will not achieve the required read-after-write consistency.
  For more information about Aurora global databases, see Using Amazon Aurora Global Databases. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html

---

## Câu 46 — ✅ Đúng

*Multiple Choice · Thời gian làm: 4 minutes 14 seconds*

**Đề bài:**

A company has an online event-booking system that consists of a web application that is deployed in a five-instance fleet of Amazon EC2 instances. The EC2 instances run Amazon Linux 2 with identical unencrypted root volumes. A solutions architect has created an Amazon Machine Image (AMI) from the existing configuration.

Sometimes there is a gap of up to a month from when one event-booking window ends to when the next booking window begins. The company wants to shut off resources between event-booking windows. Currently, an administrator stops the instances after each event. However, the boot process is slow, and the long boot time is unacceptable when the company suddenly notifies the administrator that the next event-booking window is open. The company needs to find a solution that will stop and start the system quickly.

Which solution will meet these requirements?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Create a launch template by using the existing AMI. Create an EC2 Auto Scaling group that uses the new launch template. Configure the minimum and desired number of instances to one. Configure the maximum number of instances to five. Terminate the existing instances.**

  *Giải thích:* An EC2 Auto Scaling group with a minimum of one would leave one instance running even if the instance is not in use. The company wants to turn off all instances between booking windows. Additionally, this solution would not reduce the boot time for newly launched instances.
  For more information about EC2 Auto Scaling, see Auto Scaling Groups. https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html

- **B. Create an encrypted snapshot of a root volume. Create a new AMI from the encrypted snapshot. Terminate the existing instances. Launch new instances by using the new AMI with hibernation turned on. Hibernate the instances when they are not in use.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* A solution that hibernates instances will have the same cost implications as a solution that stops instances. It can be faster to restart hibernated instances than to restart stopped instances that take a long time to bootstrap. To use hibernation for supported EC2 instance types, you must configure hibernation when you first launch the EC2 instance. You can provide the required root volume encryption by creating an AMI from an encrypted snapshot of the existing volume. This solution would properly configure hibernation.
  For more information about EC2 instance hibernation, see Hibernate Your On-Demand or Reserved Linux Instance. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html 
  For more information about requirements for hibernation, see Enable Hibernation for an Instance. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enabling-hibernation.html 
  For more information about how to encrypt root volumes, see Encrypt Unencrypted Resources. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html

- **C. Create an encrypted snapshot of a root volume. Create a new root volume from the snapshot and attach it to the EC2 instances. Modify the EC2 instance options to turn on hibernation. Hibernate the instances when they are not in use.**

  *Giải thích:* A solution that hibernates instances will have the same cost implications as a solution that stops instances. It can be faster to restart hibernated instances than to restart stopped instances that take a long time to bootstrap. However, to use hibernation for supported EC2 instance types, you must configure hibernation when you first launch the EC2 instance.
  For more information about EC2 hibernation, see Hibernate Your On-Demand or Reserved Linux Instance. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html 
  For more information about requirements for hibernation, see Enable Hibernation for an Instance. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enabling-hibernation.html

- **D. Create a launch template by using the existing AMI. Create an EC2 Auto Scaling group that uses the new launch template. Configure the minimum and desired number of instances to zero. Configure the maximum number of instances to five. Terminate the existing instances.**

  *Giải thích:* An EC2 Auto Scaling group with a minimum of zero would terminate all instances that are running if they are not in use. This solution would require the instances to start fresh the for the next event-booking window. This solution would not reduce the boot time for newly launched instances.
  For more information about EC2 Auto Scaling, see Auto Scaling Groups. https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html

---

## Câu 47 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 18 seconds*

**Đề bài:**

A company has migrated most of its on-premises infrastructure to the AWS Cloud. The company is planning to complete the migration soon. After the migration, the company will retire its on-premises infrastructure. The company currently uses Active Directory to manage and authenticate its users. The company wants an AWS solution to manage users on AWS. The company has hundreds of users and needs only basic LDAP functionality. The company wants to implement multi-factor authentication (MFA) as part of the solution.

Which solution will meet these requirements with the LEAST operational effort?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Configure an Active Directory Connector directory in AWS Directory Service. Connect the Active Directory Connector directory to the on-premises Active Directory.**

  *Giải thích:* Active Directory Connector is a directory gateway that can redirect directory requests to an on-premises Active Directory without the need to cache any information in the cloud. However, the company plans to retire its on-premises infrastructure.
  For more information about Active Directory Connector, see Active Directory Connector 
  .

- **B. Configure a directory with AWS Managed Microsoft AD. Use the Active Directory Migration Toolkit to migrate the users from the on-premises Active Directory to AWS.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, runs Active Directory as a managed service. The Active Directory Migration Toolkit can migrate users from an on-premises Active Directory to AWS Managed Microsoft AD. This solution also supports MFA.
  For more information about AWS Managed Microsoft AD, see AWS Managed Microsoft AD 
  .
  For more information about user migration, see Migrating Active Directory users to AWS Managed Microsoft AD 
  .

- **C. Configure a Simple Active Directory directory in AWS Directory Service. Use the Comma Separated Value Directory Exchange (CSVDE) utility to migrate the users from the on-premises Active Directory to AWS.**

  *Giải thích:* Simple Active Directory is a standalone managed directory that is powered by a Samba 4 Active Directory Compatible Server. Simple Active Directory provides a subset of the features that AWS Managed Microsoft AD offers. However, Simple Active Directory does not support MFA, which is one of the requirements.
  For more information about Simple Active Directory, see Simple Active Directory 
  .

- **D. Configure an AWS IAM Identity Center identity store to manage the users in AWS. Provision users, groups, and entitlements in IAM Identity Center.**

  *Giải thích:* You configure an identity store when you configure IAM Identity Center. However, migration from Active Directory to the identity store used by IAM Identity Center would require recreation of the users, groups, and assignments (entitlements). This solution requires more operational effort than necessary.
  For more information about how to configure an identity store, see Manage Identities in IAM Identity Center 
  .
  For more information about how to change identity stores from Active Directory to IAM Identity Center, see Considerations for Changing Your Identity Source 
  .

---

## Câu 48 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 21 seconds*

**Đề bài:**

A company wants to store thousands of objects in Amazon S3. Object key names can have the following prefixes:

mk (marketing)
sa (sales)
ex (executive)

Access should be based on the following rules:

Marketing managers must have access only to objects with the mk prefix.
Sales managers must have access only to objects with the sa prefix.
Sales and marketing directors must have access to objects with both the mk and sa prefixes.
The finance administrator needs access to all objects with any prefix.

The company needs an access solution that provides the ability to add more prefixes in the future.

Which solution will meet these requirements with the LEAST ongoing administrative effort?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Create one S3 bucket. Place all the objects in the S3 bucket. Create multiple appropriate IAM policies based on the three prefixes. Attach the correct IAM policy to each object in the S3 bucket based on the object name. Give the single URL for the S3 bucket to all employees.**

  *Giải thích:* A policy defines the permissions for the identities or resources with which the policy is associated. You cannot attach IAM policies directly to objects. You must attach IAM resource-based policies to the S3 buckets.
  For more information about IAM resource-based policies, see Resource-Based Policies. https://docs.aws.amazon.com/IAM/latest/UserGuide/access\_policies.html#policies\_resource-based

- **B. Create one S3 bucket. Place all the objects in the S3 bucket. Create three S3 access points that are based on the object prefixes for mk, sa, and both. Attach the appropriate IAM resource-based policies to the S3 access points and the S3 bucket. Give the appropriate S3 access point aliases to the managers and directors. Give the URL for the S3 bucket to the finance administrator.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* S3 access points simplify data access for any AWS service or customer application that stores data in Amazon S3. You can attach IAM policies directly to the S3 access points. Employees would have a single URL to access their objects. This solution also gives the company a flexible way to add S3 access points for future prefixes.
  For more information about S3 access points, see Managing Data Access with Amazon S3 Access Points. https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html 
  For more information about IAM resource-based policies, see Resource-Based Policies. https://docs.aws.amazon.com/IAM/latest/UserGuide/access\_policies.html#policies\_resource-based

- **C. Create four S3 buckets. Separate the mk, sa, and ex objects into three separate S3 buckets. Replicate the mk and sa objects into the fourth S3 bucket and the ex S3 bucket. Define the appropriate IAM resource-based policy for each S3 bucket to control access. Give the correct URL for each S3 bucket to each employee.**

  *Giải thích:* This solution would separate access and would provide a single URL for each employee. However, if you add a new prefix later, you would have to create a new S3 bucket and replicate the new bucket to the ex bucket. This solution does not require the least ongoing administrative effort.
  For more information about S3 replication, see Replicating Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html

- **D. Create one S3 bucket. Create a folder with subfolders for the mk and sa objects. Attach the appropriate IAM resource-based policies to the folders. Create a separate folder for the ex objects. Define the appropriate IAM resource-based policy on the S3 bucket for the finance administrator. Give the folder URLs to the managers and directors. Give the S3 bucket URL to the finance administrator.**

  *Giải thích:* A policy defines the permissions for the identities or resources with which the policy is associated. You cannot attach IAM policies directly to folders in an S3 bucket. You must attach IAM resource-based policies to the S3 buckets.
  For more information about IAM resource-based policies, see Resource-Based Policies. https://docs.aws.amazon.com/IAM/latest/UserGuide/access\_policies.html#policies\_resource-based

---

## Câu 49 — ✅ Đúng

*Multiple Choice · Thời gian làm: 3 minutes 4 seconds*

**Đề bài:**

A company deploys a new internal application on two Amazon EC2 instances behind an Application Load Balancer (ALB). The ALB and the EC2 instances operate across two Availability Zones. The company's employees depend on the application to perform their work.

When workloads are high, employees report slow response times and reliability issues with the application. Some incoming requests can generate significant compute activity on the EC2 instances. The workload can increase by 2 to 10 times the typical load in a matter of minutes. A solutions architect needs to change the configuration so that the application will scale in response to multiple workload changes in the least amount of time possible.

How should the solutions architect configure Amazon EC2 Auto Scaling to meet these requirements?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Configure a simple scaling policy that scales EC2 instances based on the CPUUtilization metric.**

  *Giải thích:* EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. CPU utilization is the correct policy basis because requests can generate different amounts of activity on the instances. However, an Auto Scaling group with a simple scaling policy must wait for scaling activity to finish running, followed by a cooldown period, before the Auto Scaling group can respond to additional workload changes. The requirement is that the solution must respond to multiple workload changes in the least amount of time possible. A step scaling policy would respond faster to workload changes.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html 
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

- **B. Configure a simple scaling policy that scales EC2 instances based on the RequestCountPerTarget metric from the ALB.**

  *Giải thích:* EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. However, an Auto Scaling group with a simple scaling policy must wait for scaling activity to finish running, followed by a cooldown period, before the Auto Scaling group can respond to additional alarms. The requirement is that the solution must respond to multiple workload changes in the least amount of time possible. A step scaling policy would respond faster to workload changes. Additionally, different requests can generate different levels of activity on the instances, so a few requests could generate a lot of activity. A policy that is based on the RequestCountPerTarget metric would not be as effective as a policy that is based on CPU utilization.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html 
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

- **C. Configure a step scaling policy that scales EC2 instances based on the CPUUtilization metric.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. An Auto Scaling group with a step scaling policy would quickly respond to multiple workload changes, even while another scale-out activity is in progress. CPU utilization is the correct policy basis because requests can generate different amounts of activity on the instances.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html 
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

- **D. Configure a step scaling policy that scales EC2 instances based on the RequestCountPerTarget metric from the ALB.**

  *Giải thích:* EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. An Auto Scaling group with a step scaling policy would quickly respond to multiple workload changes, even while another scale-out activity is in progress. However, different requests can generate different levels of activity on the instances, and a few requests could generate a lot of activity. A policy that is based on the RequestCountPerTarget metric would not be as effective as a policy that is based on CPU utilization.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html 
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

---

## Câu 50 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 31 seconds*

**Đề bài:**

A company wants to migrate a three-tiered web application from an on-premises data center to AWS. The company developed the UI by using server-side JavaScript libraries. The business logic and API tier use a Python-based web framework. The data tier runs on a MySQL database.

The company custom built the application to meet business requirements. The company does not want to re-architect the application. The company needs a solution to replatform the application to AWS with the least possible amount of development. The solution needs to be highly available and must reduce operational overhead.

Which solution will meet these requirements?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Build the UI and business logic in Docker images. Store the images in Amazon ECR. Use Amazon ECS with the Fargate launch type to host the UI and business logic applications with an Application Load Balancer in front. Migrate the database to an Amazon RDS for MySQL Multi-AZ DB instance.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You can containerize both UI and business logic to provide replatforming without re-architecting the application. ECS with Fargate provides a fully managed and highly available container orchestration and hosting solution. This solution reduces operational overhead. RDS for MySQL Multi-AZ provides high availability for the database tier and maintains MySQL compatibility.
  Learn more about the ECS with AWS Fargate launch type. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS\_Fargate.html 
  Learn more about Amazon RDS for MySQL. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP\_MySQL.html 
  Learn more about Multi-AZ deployment in Amazon RDS. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html

- **B. Build the UI and business logic in Docker images. Store the images in Amazon ECR. Use Amazon EKS with Fargate profiles to host the UI and business logic. Use AWS DMS to migrate the data layer to Amazon DynamoDB.**

  *Giải thích:* You can migrate from MySQL to DynamoDB. However, this solution requires re-architecting the application and data access patterns because DynamoDB is a NoSQL database. This solution does not meet the requirement to avoid re-architecting.
  Learn more about DynamoDB. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

- **C. Deploy the UI to a static website on Amazon S3. Use Amazon CloudFront to deliver the website. Build the business logic in a Docker image. Store the image in Amazon ECR. Use Amazon ECS with the Fargate launch type to host the website with an Application Load Balancer in front. Deploy the data layer to an Amazon Aurora MySQL DB cluster.**

  *Giải thích:* The UI uses server-side JavaScript libraries. Therefore, you need server-side processing. You cannot deploy this solution as a static website on Amazon S3. S3 static websites support only client-side JavaScript execution.
  Learn more about static website hosting on Amazon S3. https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html

- **D. Deploy the UI to a static website on Amazon S3. Use Amazon CloudFront to deliver the website. Convert the business logic to AWS Lambda functions. Integrate the functions with Amazon API Gateway. Deploy the data layer to an Amazon Aurora MySQL DB cluster.**

  *Giải thích:* You can convert the Python-based web framework to Lambda functions. However, this solution requires significant re-architecting of the application. This solution does not meet the requirement to avoid re-architecting. This solution requires substantial development effort.
  Learn more about Lambda. https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

---

## Câu 51 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 22 seconds*

**Đề bài:**

A global company uses multiple accounts. Each account runs resources in three AWS Regions. The company needs identical Amazon EC2 instances as test systems in the different accounts. A solutions architect creates a custom AMI and an AWS CloudFormation template to provision the test systems in the company's main development account. The solutions architect shares the AMI across accounts and copies the AMI to each Region. The solutions architect shares the CloudFormation template to the various accounts and edits the template to refer to the appropriate AMI ID for each Region. The solutions architect needs to reduce the manual work that is necessary to create each new custom AMI.

Which solution will meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create AWS Systems Manager Parameter Store parameters that have identical names in each Region for each account. Include the appropriate AMI IDs for that Region in the parameters. Configure the CloudFormation template to retrieve the AMI ID from the parameters. Use the single CloudFormation template in the main development account to provision the test systems in all the accounts. Update the parameters as required when the company creates and shares a new AMI.**

  *Giải thích:* A CloudFormation template can create resources only in the account where the template resides. This solution would not give the solutions architect the ability to provision test systems in the other accounts.
  For more information about CloudFormation, see What Is AWS CloudFormation? https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html

- **B. Create a mapping section in the CloudFormation template to hold the AMI IDs for each Region. Update the template to retrieve the correct AMI ID from the mapping. Import the CloudFormation template into each account. Use the template to create the required resources. Update the mapping as required when the company creates and shares a new AMI.**

  *Giải thích:* A solution that uses mappings in a CloudFormation template requires less operational overhead than a solution that hardcodes the AMI IDs. Maintenance of multiple CloudFormation templates would require more operational overhead than usage of CloudFormation StackSets.
  For more information about CloudFormation, see What Is AWS CloudFormation? https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html 
  For more information about mappings, see Mappings. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html 
  For more information about StackSets, see Working with AWS CloudFormation StackSets. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html

- **C. Create AWS Systems Manager Parameter Store parameters that have identical names in each Region for each account. Include the appropriate AMI IDs for that Region. Configure the CloudFormation template to retrieve the AMI ID from the parameters. Copy the CloudFormation template to each account and Region. Use the template to create the required resources. Update the parameters as required when the company creates and shares a new AMI.**

  *Giải thích:* Parameter Store provides storage for configuration data, including passwords, database strings, and AMI IDs. Less operational overhead is required to store the AMI ID in Parameter Store than to hardcode the AMI IDs in the CloudFormation templates. A solution that relies on maintenance of parameters in each account and of multiple CloudFormation templates will require more operational overhead than a solution that uses CloudFormation StackSets and mappings.
  For more information about Parameter Store, see AWS Systems Manager Parameter Store. https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html 
  For more information about mappings, see Mappings. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html 
  For more information about StackSets, see Working with AWS CloudFormation StackSets. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html

- **D. Create a mapping section in the CloudFormation template to hold the AMI IDs for each Region. Update the template to retrieve the correct AMI ID from the mapping. Use CloudFormation StackSets to create a stack set in the main development account. Use the stack set to deploy stack instances in each account as needed. Update the mapping as required when the company creates and shares a new AMI.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* StackSets extends the functionality of CloudFormation stacks by giving users tools to manage stacks across multiple accounts and Regions. A solution that uses mappings in a CloudFormation template and creates a single stack set to deploy multiple stack instances to the multiple accounts and Regions would require less operational overhead than a solution that requires maintenance of multiple CloudFormation templates.
  For more information about StackSets, see Working with AWS CloudFormation StackSets. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html 
  For more information about mappings, see Mappings. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html

---

## Câu 52 — ✅ Đúng

*Multiple Choice · Thời gian làm: 53 seconds*

**Đề bài:**

A company is running a critical application on AWS. The application runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The instances run in an Amazon EC2 Auto Scaling group. The application uses an Amazon RDS for MySQL DB instance as the backend in a Multi-AZ deployment. All the services that the application supplies are currently in a single AWS Region.

A new disaster recovery (DR) regulation requires the company to have a multi-Region configuration. The failover deployment in the second Region must handle a full-capacity workload as quickly as possible. To prepare a DR configuration, a solutions architect has created an ALB and an EC2 Auto Scaling group in a second Region.

Which solution will meet these requirements with the FASTEST recovery time?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Use AWS Backup to back up the DB instance to a backup vault in the second Region. Use the backup to create a new RDS DB instance in the second Region if needed. Configure Amazon Route 53 with a failover routing policy.**

  *Giải thích:* The creation of a new database from backups is part of a backup and restore DR strategy, which takes a long time. A pilot light strategy would result in faster recovery time. The promotion of a read replica of the primary database would be an example of a pilot light strategy.
  For more information about restoration from a DB snapshot, see Restoring from a DB Snapshot. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_RestoreFromSnapshot.html 
  For more information about DR strategies, see Disaster Recovery Options in the Cloud. https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html

- **B. Use AWS Backup to back up the DB instance to a backup vault in the second Region. Use the backup to create a new RDS DB instance in the second Region if needed. Configure Amazon Route 53 with a weighted routing policy.**

  *Giải thích:* The creation of a new database from backups is part of a backup and restore DR strategy, which takes a long time. A pilot light strategy would result in faster recovery time. The promotion of a read replica of the primary database would be an example of a pilot light strategy.
  For more information about restoration from a DB snapshot, see Restoring from a DB Snapshot. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_RestoreFromSnapshot.html 
  For more information about DR strategies, see Disaster Recovery Options in the Cloud. https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html

- **C. Create a read replica of the DB instance in the second Region. Promote the read replica to be the primary DB instance if needed. Configure Amazon Route 53 with a weighted routing policy.**

  *Giải thích:* The promotion of a read replica would be a faster option than the creation of a database from backups. However, configuration of a weighted routing policy for Route 53 would not automatically route traffic to the second Region. This solution would require a manual intervention. This solution would not have the fastest recovery time.
  For more information about the promotion of read replicas, see Working with Read Replicas. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_ReadRepl.html 
  For more information about routing policies, see Choosing a Routing Policy. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

- **D. Create a read replica of the DB instance in the second Region. Promote the read replica to be the primary DB instance if needed. Configure Amazon Route 53 with a failover routing policy.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* The promotion of a read replica would be a faster option than the creation of a database from backups. The configuration of a failover routing policy for Route 53 would automatically move the incoming workload to the second deployment. This solution would have the fastest recovery time.
  For more information about how to create a read replica for Amazon RDS in a different Region, see Creating a Read Replica in a Different AWS Region. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_ReadRepl.XRgn.html 
  For more information about the promotion of read replicas, see Working with Read Replicas. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_ReadRepl.html 
  For more information about routing policies, see Choosing a Routing Policy. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

---

## Câu 53 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 59 seconds*

**Đề bài:**

A company recently deployed a new application that runs on a group of Amazon EC2 Linux instances in a VPC. In a peered VPC, the company launched an EC2 Linux instance that serves as a bastion host. The security group of the application instances allows access only on TCP port 22 from the private IP of the bastion host. The security group of the bastion host allows access to TCP port 22 from 0.0.0.0/0 so that system administrators can use SSH to remotely log in to the application instances from several branch offices.

While looking through operating system logs on the bastion host, a cloud engineer notices thousands of failed SSH logins to the bastion host from locations around the world. The cloud engineer wants to change how remote access is granted to the application instances and wants to meet the following requirements:

Eliminate brute-force SSH login attempts.
Retain a log of commands run during an SSH session.
Retain the ability to forward ports.

Which solution meets these requirements for remote access to the application instances?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Configure the application instances to communicate with AWS Systems Manager. Grant access to the system administrators to use Session Manager to establish a session with the application instances. Terminate the bastion host.**  
  _✔ Đáp án đúng_

  *Giải thích:* Session Manager helps you improve your security posture by giving you the ability to close inbound SSH ports. With Session Manager, you do not need to manage SSH keys and certificates, bastion hosts, or jump boxes. Session Manager offers the benefit of port forwarding. Session Manager also logs and audits session activity.
  For more information about Session Manager, see AWS Systems Manager Session Manager 
  .

- **B. Configure the application instances to communicate with AWS Systems Manager. Grant access to the system administrators to issue commands to the application instances by using Systems Manager Run Command. Terminate the bastion host.**

  *Giải thích:* Run Command gives you the ability to automate common administrative tasks and to perform one-time configuration changes at scale. However, Run Command cannot forward ports.
  For more information about Run Command, see AWS Systems Manager Run Command 
  .

- **C. Configure an AWS Client VPN endpoint and provision each system administrator with a certificate to establish a VPN connection to the application VPC. Update the security group of the application instances to allow traffic from only the Client VPN IPv4 CIDR. Terminate the bastion host.**  
  _☑ Bạn đã chọn_

  *Giải thích:* A Client VPN connection can guarantee encryption. However, this connection would not be able to retain a log of commands that a user ran during an SSH session.
  For more information about Client VPN, see What Is AWS Client VPN? 
  For more information about how to use Session Manager to log session activity, see Logging Session Activity 
  .

- **D. Update the security group of the bastion host to allow traffic from only the public IP addresses of the branch offices.**

  *Giải thích:* http:// 
  Incorrect. An update to the security group of the bastion host would not eliminate brute-force SSH attempts because the public IP addresses of the branch offices are open. Additionally, you can configure Session Manager to log session activity. This solution does not address the requirement to log commands.
  For more information about how to use security groups to control traffic, see Control Traffic to Resources Using Security Groups 
  .
  For more information about how use Session Manager to log session activity, see Logging Session Activity 
  .

---

## Câu 54 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 18 seconds*

**Đề bài:**

A company recently migrated a large, restartable batch computing workload from on-premises servers to AWS Batch. The batch job runs monthly in an Amazon EC2 compute environment that requires a custom AMI. The company wants to reduce the overhead that is associated with the management of the compute environment. The company also wants to reduce the cost to run the AWS Batch workload.

Which solution will meet these requirements?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Modify the AWS Batch job to run in a managed EC2 compute environment that uses the AMI. Select Spot as the provisioning model.**  
  _✔ Đáp án đúng_

  *Giải thích:* With AWS Batch, you need an EC2 compute environment in order to use the custom AMI. A managed compute environment would help reduce the overhead that is associated with the management of the compute environment. Also, the Spot provisioning model would have a lower cost for a restartable, monthly workload. This solution meets the requirements.
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html 
  For more information about how Spot Instances help reduce costs, see Spot Instances. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html

- **B. Modify the AWS Batch job to run in an AWS Fargate compute environment. Select Fargate as the provisioning model.**

  *Giải thích:* Fargate would reduce the overhead that is associated with management of the compute environment. However, you need a managed EC2 compute environment in order to use the custom AMI.
  For more information about AWS Batch on Fargate, see AWS Batch on AWS Fargate. https://docs.aws.amazon.com/batch/latest/userguide/fargate.html 
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html

- **C. Modify the AWS Batch job to run in an AWS Fargate compute environment. Select Fargate Spot as the provisioning model.**  
  _☑ Bạn đã chọn_

  *Giải thích:* Fargate would reduce the overhead that is associated with management of the compute environment. However, you need an EC2 compute environment in order to use the custom AMI.
  For more information about AWS Batch on Fargate, see AWS Batch on AWS Fargate. https://docs.aws.amazon.com/batch/latest/userguide/fargate.html 
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html

- **D. Modify the AWS Batch job to run in a managed EC2 compute environment that uses the AMI. Select On-Demand as the provisioning model.**

  *Giải thích:* With AWS Batch, you need a managed EC2 compute environment in order to use the custom AMI. However, because the AWS Batch job is restartable and runs monthly, Spot provisioning would be a lower-cost option than On-Demand.
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html

---

## Câu 55 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 43 seconds*

**Đề bài:**

A company's solutions architect is designing a disaster recovery (DR) solution for an application that runs on AWS. The application uses PostgreSQL 11.7 as its database. The company has an RPO of 30 seconds. The solutions architect must design a DR solution with the primary database in the us-east-1 Region and the failover database in the us-west-2 Region.

What should the solutions architect do to meet these requirements with minimum application change?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Migrate the database to Amazon RDS for PostgreSQL in us-east-1. Set up a standby replica in an Availability Zone in us-west-2. Set the managed RPO for the RDS database to 30 seconds.**

  *Giải thích:* Managed RPO is not a feature of Amazon RDS.
  For more information about Amazon RDS backups, see Enabling Automated Backups.
  https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_WorkingWithAutomatedBackups.html#USER\_WorkingWithAutomatedBackups.Enabling

- **B. Migrate the database to Amazon DynamoDB in us-east-1. Set up global tables with replica tables that are created in us-west-2.**

  *Giải thích:* DynamoDB is not a relational database. This solution would require significant changes to the application.
  For more information about DynamoDB, see What Is Amazon DynamoDB? https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

- **C. Migrate the database to an Amazon Aurora PostgreSQL global database with the primary Region as us-east-1 and the secondary Region as us-west-2. Set the managed RPO for the Aurora database to 30 seconds.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Aurora global databases provide managed RPO. Users can set RPO as low as 20 seconds.
  For more information about RPO parameters, see Managing RPOs for Aurora PostgreSQL–Based Global Databases. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-manage-recovery

- **D. Migrate the database to Amazon RDS for PostgreSQL in us-east-1. Set up a read replica in us-west-2. Set the managed RPO for the RDS database to 30 seconds.**

  *Giải thích:* Managed RPO is not a feature of Amazon RDS.
  For more information about Amazon RDS backups, see Enabling Automated Backups.
  https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_WorkingWithAutomatedBackups.html#USER\_WorkingWithAutomatedBackups.Enabling

---

## Câu 56 — ✅ Đúng

*Multi-Select · Thời gian làm: 2 minutes 11 seconds*

**Đề bài:**

A company wants to migrate its on-premises order entry system to a highly available solution on AWS. The existing order entry system is a PHP web application that accepts orders and publishes them to Apache ActiveMQ by using its own proprietary protocol. A processing application polls the queued orders and stores them in JSON format in a document database.

Which migration strategies would require the LEAST migration effort?

**Đáp án bạn chọn:** D, E, F  
**Đáp án đúng:** D, E, F

**Các lựa chọn và giải thích:**

- **A. Rehost the web application to an Amazon S3 bucket. Rehost the processing application on Amazon EC2 instances that use Amazon EC2 Auto Scaling.**

  *Giải thích:* An S3 bucket can host a static website. A solution that rehosts the web application to an S3 bucket would not meet the requirements because Amazon S3 does not support server-side scripting. AWS provides other resources to host dynamic websites.
  For more information about Amazon S3 as a host for static websites, see Hosting a Static Website Using Amazon S3 
  .

- **B. Refactor the database server into a Multi-AZ Amazon RDS DB instance. Modify the processing application to write to Amazon RDS.**

  *Giải thích:* Amazon RDS helps to set up, operate, and scale a relational database in the cloud. Because the application uses JSON documents, a solution that refactors the application to use DynamoDB would require less work than a solution that refactors the application to use a relational database.
  For more information about Amazon RDS, see What Is Amazon Relational Database Service (Amazon RDS)?

- **C. Replatform the message queue to Amazon SQS. Configure both applications to use this queue.**

  *Giải thích:* Amazon SQS offers a secure, durable, and available hosted queue that integrates and decouples distributed software systems and components. However, Amazon SQS supports only the HTTP and HTTPS protocols, and the requirement is to use the ActiveMQ protocol.
  For more information about Amazon SQS, see What Is Amazon Simple Queue Service?

- **D. Rehost both applications to Amazon EC2 instances that use Amazon EC2 Auto Scaling. Use an Application Load Balancer in front of the web application.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* A solution that rehosts the applications on EC2 instances that use EC2 Auto Scaling would be scalable and highly available. An Application Load Balancer automatically distributes incoming traffic across multiple targets in one or more Availability Zones.
  For more information about Amazon EC2, see What Is Amazon EC2? 
  For more information about EC2 Auto Scaling, see What Is Amazon EC2 Auto Scaling? 
  For more information about Elastic Load Balancing (ELB), see What Is Elastic Load Balancing?

- **E. Refactor the database server into Amazon DynamoDB tables. Modify the processing application to write to DynamoDB.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. You can use DynamoDB for document storage. A solution that refactors the application to use DynamoDB would require less work than a solution that refactors the application to use a relational database.
  For more information about DynamoDB, see What Is Amazon DynamoDB? 
  For more information about storage of JSON documents in DynamoDB, see Document Interfaces 
  .

- **F. Replatform the message queue to Amazon MQ. Configure both applications to use this queue.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Amazon MQ is a managed message broker service for ActiveMQ. This solution requires minimal code changes because the existing application uses ActiveMQ.
  For more information about Amazon MQ, see What Is Amazon MQ?

---

## Câu 57 — ❌ Sai

*Multi-Select · Thời gian làm: 3 minutes 27 seconds*

**Đề bài:**

A company plans to migrate 500 workloads to the AWS Cloud. The company creates separate accounts for different workloads by using AWS Organizations. The company has teams that focus solely on security and infrastructure. Most workloads fall into well-defined environments such as production, development, or testing. There are a few unique workloads that require specific security policies. The company is not sure how to organize the workloads and teams. A solutions architect needs to design an account structure.

Which combination of steps should the solutions architect take to set up the correct account structure?

**Đáp án bạn chọn:** A, B, D  
**Đáp án đúng:** A, C, D

**Các lựa chọn và giải thích:**

- **A. Create OUs for each environment. Add workload accounts to the appropriate environment OUs. Apply appropriate SCPs at the OU level.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Organizations provides centralized account management in a hierarchical fashion through OUs and policies. A solution that creates OUs based on functional roles would give you the ability to apply common SCPs across the accounts with the same functional role.
  For more information about the design of AWS accounts within Organizations, see Design Principles for Organizing Your AWS Accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-organizing-your-aws-accounts.html

- **B. Set up a centralized security account for logging, tooling, and audit-related activities.**  
  _☑ Bạn đã chọn_

  *Giải thích:* Organizations provides centralized account management in a hierarchical fashion through OUs and policies. You cannot achieve workload isolation, minimal blast radius, and simpler access management by creating a single account for all logging, tooling, and audit activities.
  For more information about security account structure, see Security OU and accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/security-ou-and-accounts.html

- **C. Set up separate security accounts for logging, tooling, and audit-related activities.**  
  _✔ Đáp án đúng_

  *Giải thích:* Organizations provides centralized account management in a hierarchical fashion through OUs and policies. You should create separate security accounts for logging, security tooling, read-only access, and emergency access (break-glass access), especially for advanced organizations.
  For more information about security account structure, see Security OU and accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/security-ou-and-accounts.html

- **D. Create accounts for unique workloads in a separate OU that is named "Exceptions." Apply appropriate SCPs at the account level.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Organizations provides centralized account management in a hierarchical fashion through OUs and policies. The creation of a separate OU for any exception accounts would reduce the effort necessary for you to apply SCPs to the relevant accounts as needed.
  For more information about accounts that have unique requirements, see Exceptions OU. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/exceptions-ou.html

- **E. Create accounts for unique workloads in the same OUs as the regular workloads. Apply appropriate SCPs at the account level.**

  *Giải thích:* Organizations provides centralized account management in a hierarchical fashion through OUs and policies. A solution that creates accounts for unique exception workloads in the same OU as the regular workloads would require you to apply common and unique SCPs directly to the accounts. This solution would complicate policy management.
  For more information about the design of AWS accounts within AWS Organizations, see Design Principles for Organizing Your AWS Accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-organizing-your-aws-accounts.html

- **F. Create one OU for each workload. Add each workload account into each workload OU. Apply appropriate SCPs at the OU level.**

  *Giải thích:* Organizations provides centralized account management in a hierarchical fashion through OUs and policies. A solution that creates OUs based on workloads would require you to apply common production and testing SCPs at the account level. This solution would complicate policy management.
  For more information about the design of AWS accounts within Organizations, see Design Principles for Organizing Your AWS Accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-organizing-your-aws-accounts.html

---

## Câu 58 — ❌ Sai

*Multiple Choice · Thời gian làm: 1 minutes 38 seconds*

**Đề bài:**

A company runs a grid computing application on eight Amazon EC2 instances. The instances are fully patched and updated. The application frequently fails because of network timeout errors. A solutions architect creates an AMI that is based on the existing EC2 instances. The solutions architect uses the AMI to add two additional EC2 instances. However, this change does not resolve the timeout errors.

Which solution will resolve the timeout errors with the LEAST operational effort?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Use the existing AMI to create new EC2 instances in a cluster placement group. Terminate the old instances.**  
  _✔ Đáp án đúng_

  *Giải thích:* A cluster placement group packs instances close together inside an Availability Zone. This solution will reduce the network latency between the EC2 instances. Reduction of network latency can resolve the timeout errors. Because an AMI already exists, the creation of a cluster placement group requires less operational effort than other network enhancements require.
  For more information about cluster placement groups, see Placement Groups. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html

- **B. Configure Elastic Network Adapters (ENAs) for all the instances.**  
  _☑ Bạn đã chọn_

  *Giải thích:* ENAs provide enhanced networking capabilities to EC2 instances. However, ENA configuration would require significant operational effort.
  For more information about ENAs see, Enable Enhanced Networking with the Elastic Network Adapter (ENA) on Linux Instances. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html

- **C. Configure Elastic Fabric Adapters (EFAs) for all the instances.**

  *Giải thích:* An EFA is a network device that attaches to EC2 instances to accelerate high performance computing (HPC) and machine learning applications. However, EFA configuration would require significant operational effort.
  For more information about EFAs, see Elastic Fabric Adapter. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html

- **D. Use the existing AMI to create new EC2 instances in an EC2 Fleet. Terminate the old instances.**

  *Giải thích:* An EC2 Fleet creates multiple EC2 instances in a single API call. In this scenario, there does not appear to be an issue with the number of EC2 instances. The problem is more likely to be related to network latency. For this reason, the creation of an EC2 Fleet is not likely to address timeout errors.
  For more information about EC2 Fleets, see EC2 Fleet. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html

---

## Câu 59 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 28 seconds*

**Đề bài:**

A company has resources in on-premises networks and in multiple VPCs on AWS. The company needs a networking solution that will give the on-premises resources the ability to communicate with the VPC resources. The VPC resources also must be able to communicate with each other.

The company has configured a customer gateway device on premises and has attached virtual private gateways to each VPC. The company wants a scalable solution so that the company can easily add more VPCs in the future.

How should a solutions architect configure the network connectivity to meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Set up a connection through AWS Direct Connect. Create VIFs to provide access to the virtual private gateways. Configure VPC peering connections between all the VPCs.**

  *Giải thích:* Direct Connect can connect on-premises networks to AWS. This solution would require the configuration and management of a Direct Connect connection and multiple VPC peering connections, significantly increasing operational overhead.
  For more information about Direct Connect, see What is AWS Direct Connect? https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

- **B. Create a transit VPC. Create VPN connections from the transit VPC to each virtual private gateway. Create AWS Site-to-Site VPN connections between the customer gateway device and the transit VPC.**

  *Giải thích:* A transit VPC is a common way to connect geographically dispersed VPCs and remote networks to create a global network transit center. However, a transit VPC requires additional configuration and operational overhead because you must manage Amazon EC2 instances. With a transit gateway, there are no EC2 instances to manage.
  For more information about transit VPCs, see Transit VPC Solution. https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-vpc-solution.html

- **C. Create an individual AWS Site-to-Site VPN connection between the customer gateway device and each of the virtual private gateways. Configure VPC peering connections between all the VPCs.**

  *Giải thích:* Site-to-Site VPN is a fully managed service that creates a secure connection between on-premises resources and AWS resources by using IPsec tunnels. A VPC peering connection is a network connection between two VPCs that gives you the ability to route traffic between the VPCs by using private addresses. A significant amount of operational overhead would result from the creation and management of multiple VPN connections and VPC peering connections.
  For more information about Site-to-Site VPN, see What is AWS Site-to-Site VPN? https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC\_VPN.html 
  For more information about how to peer VPCs, see What is VPC Peering? https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html

- **D. Create a transit gateway. Create an AWS Site-to-Site VPN attachment between the customer gateway device and the transit gateway. Attach the VPCs to the transit gateway. Remove the virtual private gateways.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* A transit gateway is a network transit hub that you can use to interconnect VPCs and on-premises networks. All the necessary connections can occur through a single transit gateway, minimizing operational overhead.
  For more information about transit gateways, see What is a Transit Gateway? https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html

---

## Câu 60 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 3 seconds*

**Đề bài:**

A company runs a three-tier architecture on AWS. The web tier and application tier run in Amazon EC2 Auto Scaling groups with a database as the backend. Scaling is based on CPU utilization of the application tier. The company creates an Amazon SQS standard queue to decouple the web tier and the application tier. However, tests reveal that duplicate transactions occur and that the EC2 instances are not scaling. The lack of scaling sometimes delays application processing. A solutions architect needs to eliminate the duplicate transactions and correct the scaling delay.

Which solution will meet these requirements in the MOST scalable way?

**Đáp án bạn chọn:** A  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create an SQS FIFO queue. Configure content-based deduplication. Update the application to use the new queue. Change the application tier scaling to use the ApproximateNumberOfMessagesVisible metric.**  
  _☑ Bạn đã chọn_

  *Giải thích:* FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. However, the ApproximateNumberOfMessagesVisible metric will not change in proportion to the size of the Auto Scaling group that processes messages. A better solution is to use a custom metric based on an acceptable backlog per instance. A custom metric would scale better as the Auto Scaling group grows.
  For more information about scaling in response to activity in SQS queues, see Scaling Based on Amazon SQS. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html 
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html 
  For more information about high throughput for FIFO queues, see High Throughput for FIFO Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html

- **B. Change the existing SQS standard queue to an SQS FIFO queue. Configure content-based deduplication for the queue. Change the application tier scaling to use the ApproximateNumberOfMessagesVisible metric.**

  *Giải thích:* FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. However, you cannot change an SQS standard queue to a FIFO queue.
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html 
  For more information about how to configure a FIFO queue, see Moving from a Standard Queue to a FIFO Queue. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-moving.html

- **C. Change the existing SQS standard queue to an SQS FIFO queue. Configure content-based deduplication for the queue. Create an Amazon CloudWatch custom metric to calculate the backlog per instance that is acceptable to the company. Use a target tracking scaling policy based on the custom metric.**

  *Giải thích:* FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. However, you cannot change an SQS standard queue to a FIFO queue.
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html 
  For more information about how to configure a FIFO queue, see Moving from a Standard Queue to a FIFO Queue. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-moving.html

- **D. Create an SQS FIFO queue. Configure content-based deduplication. Update the application to use the new queue. Create an Amazon CloudWatch custom metric to calculate the backlog per instance that is acceptable to the company. Use a target tracking scaling policy based on the custom metric.**  
  _✔ Đáp án đúng_

  *Giải thích:* FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. A custom metric to scale based on an acceptable backlog per instance would base the scaling on the system load in the SQS queue. The custom metric is calculated based on the approximate number of messages, processing latency, and the number of running EC2 instances. This solution provides more accurate scaling.
  For more information about scaling in response to activity in SQS queues, see Scaling Based on Amazon SQS. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html 
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html 
  For more information about high throughput for FIFO queues, see High Throughput for FIFO Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html

---

## Câu 61 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 49 seconds*

**Đề bài:**

A company stores many static files on premises. Users add a small number of new files each day. The company is refactoring and migrating some of its existing applications to AWS. The company expects this process to take 6 months. After the company completes the migration, each application will access the files directly from Amazon S3. During the migration, the files must remain accessible to the applications that the company is still running on premises. The on-premises applications run on multiple servers. The company does not want to maintain multiple copies of the static files.

How should the company manage the daily migration and the on-premises access to the files?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Create an AWS DataSync task to transfer the new files to the S3 bucket at the end of each day. Maintain the files on premises until the company completes the refactoring.**

  *Giải thích:* DataSync is an online data-transfer service that simplifies, automates, and accelerates the movement of data between on-premises storage systems and AWS storage services. DataSync would not provide access to the on-premises applications. The company would have to maintain a copy on premises.
  For more information about DataSync, see What Is AWS DataSync? https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

- **B. Create an S3 sync script and configure a recurring job to run the script at the end of each day. Maintain the files on premises until the company completes the refactoring and migration.**

  *Giải thích:* The S3 sync command synchronizes the contents of an S3 bucket and a local directory or the contents of two buckets. You could use this command to synchronize the data that is on premises to an S3 bucket. DataSync would not provide access to the on-premises applications. The company would have to maintain a copy on premises.
  For more information about the S3 sync command, see Sync Objects. https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-sync

- **C. Configure an AWS Storage Gateway Amazon S3 File Gateway and connect the S3 File Gateway to the S3 bucket. Create an on-premises NFS file share for the existing on-premises directory to establish access to the files.**  
  _✔ Đáp án đúng_

  *Giải thích:* S3 File Gateway supports a file interface with Amazon S3 and combines a service and a virtual software appliance. This combination can store and retrieve objects from Amazon S3 by using industry-standard file protocols, including NFS and SMB. NFS is a shared file system that can share data for multiple client connections. This solution will also provide access to the files for the on-premises applications.
  For more information about S3 File Gateway, see Amazon S3 File Gateways. https://docs.aws.amazon.com/filegateway/latest/files3/StorageGatewayConcepts.html#file-gateway-concepts

- **D. Configure an AWS Storage Gateway Volume Gateway and connect the Volume Gateway to the S3 bucket. Create an on-premises iSCSI volume share for the existing on-premises directory to establish access to the files.**  
  _☑ Bạn đã chọn_

  *Giải thích:* A Volume Gateway provides cloud-backed storage volumes that you can mount as iSCSI devices from on-premises application servers. However, you cannot connect multiple hosts to a Volume Gateway without additional configuration.
  For more information about how to use volumes, see Using Your Volume. https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStarted-use-volumes.html 
  For more information about how to configure a Volume Gateway, see Creating a Volume Gateway. https://docs.aws.amazon.com/storagegateway/latest/vgw/create-volume-gateway-volume.html

---

## Câu 62 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 11 seconds*

**Đề bài:**

A company uses AWS Organizations to manage multiple AWS accounts. The accounts share an Amazon SQS queue. The SQS queue is also shared with other AWS accounts outside the organization. All internal and external accounts have access to send and receive messages according to a permissions policy that is attached to the SQS queue. The company wants to identify any external principals that have access to the SQS queue.

How should a solutions architect meet this requirement?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Set up an AWS CloudTrail trail that logs management events. Use CloudTrail logs to track Amazon SQS API activities by any external principals.**

  *Giải thích:* CloudTrail records account activity and service events from most AWS services. A trail that logs management events does not capture data events such as SendMessage and ReceiveMessage activities.
  For more information about CloudTrail management events, see CloudTrail Concepts. https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

- **B. Use AWS Identity and Access Management Access Analyzer to create an analyzer with the current account as a zone of trust. Filter by external findings on the SQS queue.**

  *Giải thích:* IAM Access Analyzer helps identify the resources that are shared with an external entity. An analyzer with a specific account as the zone of trust will generate findings for other internal accounts along with external accounts. This solution does not meet the company's requirements.
  For more information about IAM Access Analyzer, see Using AWS IAM Access Analyzer. https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html

- **C. Set up an AWS CloudTrail trail that logs data events. Use CloudTrail logs to track Amazon SQS API activities by any external principals.**  
  _☑ Bạn đã chọn_

  *Giải thích:* CloudTrail records account activity and service events from most AWS services. A trail that logs data events does not capture data events from Amazon SQS such as SendMessage and ReceiveMessage activities.
  For more information about CloudTrail data events, see CloudTrail Concepts.
  https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-data-events

- **D. Use AWS Identity and Access Management Access Analyzer to create an analyzer with the current organization as a zone of trust. Filter by external findings on the SQS queue.**  
  _✔ Đáp án đúng_

  *Giải thích:* IAM Access Analyzer helps identify the resources that are shared with an external entity. An analyzer with the organization as the zone of trust will generate findings only for external accounts. It will not include the findings of the internal accounts within the organization.
  For more information about IAM Access Analyzer, see Using AWS IAM Access Analyzer. https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html 
  For more information about IAM Access Analyzer resource types, see Access Analyzer Resource Types. https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html 
  For more information about filtering IAM Access Analyzer findings, see Filtering Findings. https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-filter.html

---

## Câu 63 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 28 seconds*

**Đề bài:**

A company uses AWS KMS to manage a small number of AWS KMS customer-managed keys. Recently, one of the keys was accidentally deleted. The company did not discover the error within the mandatory waiting period for deleting AWS KMS keys, so the company lost a small amount of infrequently accessed data.

The company has configured AWS CloudTrail to deliver logs to Amazon CloudWatch Logs and Amazon S3 buckets. The company wants its systems administrator to receive notification about AWS KMS key deletions in a timely manner so that the company can avoid accidental key deletions in the future.

Which solution will meet these requirements with the LEAST operational effort?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create an Amazon Athena query to check the CloudTrail entries in the S3 bucket for AWS KMS key deletion requests. Run the query regularly. Configure the query to deliver the results to the systems administrator. Cancel deletion requests if necessary.**

  *Giải thích:* Athena is an interactive query service that helps users analyze data directly in Amazon S3 by using standard SQL. This solution requires more operational effort than the correct answer.
  For more information about how to use Athena to query CloudTrail logs, see Querying AWS CloudTrail Logs. https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html

- **B. Create an Amazon EventBridge rule to produce an alert when an AWS KMS key deletion request is performed. Configure the rule to invoke an AWS Lambda function as the target. Configure the Lambda function to cancel the deletion request.**

  *Giải thích:* EventBridge has prebuilt rules to produce alerts for AWS KMS key deletion requests. However, the use of a Lambda function to cancel the delete request is not appropriate if the request is not an accident. The system administrator needs to review the request to determine if the request was made in error.
  For more information about EventBridge events, see Events from AWS Services. https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html 
  For more information about Lambda, see What is AWS Lambda? https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

- **C. Create and schedule a daily Amazon Athena query to check the CloudTrail entries in the S3 bucket for AWS KMS key deletion requests. Configure the query to deliver the results to the systems administrator. Cancel deletion requests if necessary.**

  *Giải thích:* Athena is an interactive query service that helps users analyze data directly in Amazon S3 by using standard SQL. This solution requires more operational effort than the correct answer.
  For more information about how to use Athena to query CloudTrail logs, see Querying AWS CloudTrail Logs. https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html

- **D. Create an Amazon EventBridge rule to produce an alert when an AWS KMS key deletion request is performed. Configure the rule to send an Amazon SNS message to the systems administrator. Cancel the deletion request if necessary.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* EventBridge has prebuilt rules to produce alerts for AWS KMS key deletion requests. Amazon SNS is a managed service that provides message delivery from publishers to subscribers. This solution requires the least operational effort to provide the notification to the systems administrator.
  For more information about EventBridge events, see Events from AWS Services. https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html 
  For more information about Amazon SNS, see What is Amazon SNS? https://docs.aws.amazon.com/sns/latest/dg/welcome.html

---

## Câu 64 — ❌ Sai

*Multiple Choice · Thời gian làm: 29 seconds*

**Đề bài:**

A company manages 50 AWS accounts through AWS Organizations. Different workloads in these accounts require different security groups with appropriate rules. The company's security team wants to allow SSH access only from trusted IP CIDR blocks in all AWS accounts. The security team wants to ensure that this implementation remains compliant and cannot be modified by other accounts.

How can a solutions architect meet these requirements?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** C

**Các lựa chọn và giải thích:**

- **A. Create a common security group policy in AWS Firewall Manager. Add a primary security group with an SSH rule that allows access from trusted IP CIDR blocks. Provide the option to identify resources that do not comply with the policy rules. Select all accounts for this policy.**

  *Giải thích:* Firewall Manager does not restrict SSH access from any other sources. Additionally, Firewall Manager does not automatically remediate such broad SSH access. For these reasons, this solution does not meet the requirements.
  For more information about common security group policies, see Common Security Group Policies. https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies.html#security-group-policies-common

- **B. Create a content audit security group policy in AWS Firewall Manager. Configure custom policy rules to deny SSH traffic from 0.0.0.0/0. Use an audit security group to allow SSH traffic from trusted IP CIDR blocks. Enable automatic remediation for any noncompliant resources. Select all accounts for this policy.**

  *Giải thích:* A content audit security group policy in Firewall Manager is used to audit security groups across multiple accounts and to recognize any noncompliant rules. Policy rules can either allow or deny rules defined in the audit security group, but not both. With this setting, other security groups across accounts are evaluated. In this scenario, the policy rule allows SSH traffic from trusted IP CIDR blocks and denies SSH traffic from 0.0.0.0/0. This denial is not possible. Additionally, other security groups across accounts must be within the scope of the audit security group. Any out-of-scope rules will make these security groups noncompliant. Automatic remediation will occur, and Firewall Manager will remove any additional rules. Such actions will disrupt multiple workloads across all accounts.
  For more information about content audit security group policies, see Content Audit Security Group Policies. https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies.html#security-group-policies-audit 
  For more information about content audit security group policy remediation actions, see Security Group Content Audit Policy Findings. https://docs.aws.amazon.com/waf/latest/developerguide/security-group-content-audit-policy-findings.html

- **C. Create a firewall policy for AWS Network Firewall in AWS Firewall Manager. Add a stateless rule group to allow SSH access from trusted IP CIDR blocks with the lowest order priority. Restrict SSH access from 0.0.0.0/0. Select all accounts for this policy.**  
  _✔ Đáp án đúng_

  *Giải thích:* A firewall policy with a stateless group will allow or restrict traffic based on the rules within the group. In a stateless group, rules are processed starting from the lowest numbered priority setting. A rule that restricts SSH access from trusted sources will be processed and allowed first. The rest of the SSH traffic (0.0.0.0/0) will be restricted. These network firewalls and rule groups cannot be modified by the member accounts of an organization on AWS Organizations. This solution fulfills all the requirements.
  For more information about Network Firewall policies in Firewall Manager, see AWS Network Firewall Policies. https://docs.aws.amazon.com/waf/latest/developerguide/network-firewall-policies.html 
  For more information about stateless rule groups, see Stateless Rule Groups in AWS Network Firewall. https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-rule-groups-5-tuple.html

- **D. Create a firewall policy for AWS Network Firewall in AWS Firewall Manager. Add a stateful rule group with a strict evaluation order to allow SSH access from trusted IP CIDR blocks with the highest order priority. Restrict SSH access from 0.0.0.0/0. Select all accounts for this policy.**  
  _☑ Bạn đã chọn_

  *Giải thích:* A stateful rule group with a strict evaluation order will evaluate the rules by order of priority, starting from the lowest number. In this scenario, a rule that restricts SSH access from 0.0.0.0/0 will be evaluated first and will restrict all traffic, including SSH access from the trusted sources. This solution does not meet the requirements.
  For more information about stateful rule groups with strict evaluation order, see Strict Evaluation Order. https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order 
  For more information about standard stateful rule groups, see Standard Stateful Rule Groups in AWS Network Firewall. https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-basic.html

---

## Câu 65 — ❌ Sai

*Multiple Choice · Thời gian làm: 3 minutes 58 seconds*

**Đề bài:**

A company uses AWS Organizations with OUs in a single organization. The OUs are Finance, HR, IT, and Recruiting. Each OU contains several accounts. All the OUs have different SCPs attached to them. The HR and Recruiting OUs share some common policy requirements. However, the Recruiting OU has some additional required restrictions. When the company needs to create new common SCP restrictions for the HR and Recruiting OUs, the company wants to avoid duplicating effort to update both SCPs.

Which solution will meet these requirements with the LEAST operational effort?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Rename the Recruiting OU to Recruiting\_Old. Create a new OU named Recruiting as a child OU under the HR OU. Move the accounts that are under Recruiting\_Old to the new Recruiting OU. Remove the duplicate rules from the SCP for the Recruiting\_Old OU. Attach the updated SCP to the new Recruiting OU. Remove the Recruiting\_Old OU from the organization.**  
  _✔ Đáp án đúng_

  *Giải thích:* Organizations gives you the ability to create new OUs and to move accounts between OUs. Because the SCP for Recruiting has more restrictions than the SCP for HR, Recruiting should be the child OU with the more restrictive SCP attached. This solution requires minimal operational overhead.
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html 
  For more information about SCP policy inheritance, see Understanding Policy Inheritance. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance.html

- **B. Rename the HR OU to HR\_Old. Create a new OU named HR as a child OU under the Recruiting OU. Move the accounts that are under HR\_Old to the new HR OU. Remove the duplicate rules from the SCP for the HR\_Old OU. Attach the updated SCP to the new HR OU. Remove the HR\_Old OU from the organization.**

  *Giải thích:* Organizations gives you the ability to create new OUs and to move accounts between OUs. However, because the SCP for Recruiting has more restrictions than the SCP for HR, the Recruiting OU should be the child with the more restrictive SCP attached.
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html 
  For more information about SCP policy inheritance, see Understanding Policy Inheritance. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance.html

- **C. Move the accounts that are under the HR OU out of the organization. Remove the HR OU. Recreate the HR OU as a child OU under the Recruiting OU. Add the accounts back into the new HR OU. Remove the duplicate rules from the SCP for the HR OU. Attach the updated SCP to the new HR OU.**

  *Giải thích:* If you move an account out of an organization, you need to issue new invitations to add the account back to the organization. This solution requires more operational effort than a solution that moves accounts between OUs.
  For more information about how to invite an AWS account to join an organization, see Inviting an AWS Account to Join Your Organization. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_accounts\_invites.html 
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html

- **D. Move the accounts that are under the Recruiting OU out of the organization. Remove the Recruiting OU. Recreate the Recruiting OU as a child OU under the HR OU. Add the accounts back into the new Recruiting OU. Remove the duplicate rules from the SCP for the Recruiting OU. Attach the updated SCP to the new Recruiting OU.**  
  _☑ Bạn đã chọn_

  *Giải thích:* If you move an account out of an organization, you need to issue new invitations to add the account back to the organization. This solution requires more operational effort than a solution that moves accounts between OUs.
  For more information about how to invite an AWS account to join your organization, see Inviting an AWS Account to Join Your Organization. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_accounts\_invites.html 
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html

---

## Câu 66 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 34 seconds*

**Đề bài:**

A company's chief financial officer (CFO) wants advanced notification if projections show that the costs for Amazon EC2 instances will exceed 75% of the company's monthly AWS budget. To reduce costs, the CFO wants specific EC2 instances to stop when the CFO receives the advanced notification. A solutions architect plans to use an AWS Budgets alert as part of the solution.

Which solution will meet the CFO's requirements with the LOWEST risk of future overspending?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Create an alert based on projected costs of 75% of the monthly budget, filtered on instance type. Add an AWS Budgets action to stop the specified EC2 instances.**  
  _✔ Đáp án đúng_

  *Giải thích:* This AWS Budgets alert would activate when the projected expenditure reaches the threshold. An automatic AWS Budgets action is the best way to stop the EC2 instances. This automatic stop would prevent future overspending.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

- **B. Create an alert based on actual costs of 75% of the monthly budget, filtered on instance type. Send an alert to a systems operator to stop the specified EC2 instances.**

  *Giải thích:* This AWS Budgets alert would activate when the actual expenditure reaches the threshold. The requirements are based on projected spending. An alert based on actual spending would be too late.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

- **C. Create an alert based on actual costs of 75% of the monthly budget, filtered on instance type. Add an AWS Budgets action to stop the specified EC2 instances.**

  *Giải thích:* This AWS Budgets alert would activate when the actual expenditure reaches the threshold. The requirements are based on projected spending. An alert based on actual spending would be too late.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

- **D. Create an alert based on projected costs of 75% of the monthly budget, filtered on instance type. Send an alert to a systems operator to stop the specified EC2 instances.**  
  _☑ Bạn đã chọn_

  *Giải thích:* This AWS Budgets alert could partially meet the requirements because it would activate an alert based on projected expenditure. However, the manual step that requires the systems operator to stop the specified EC2 instances could result in overspending if the systems operator does not stop the EC2 instances quickly. An automatic AWS Budgets action is the best way to stop the EC2 instances. The automatic stop would prevent future overspending.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

---

## Câu 67 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 30 seconds*

**Đề bài:**

A media company has a system that transcodes a set of original video files and stores the newly formatted files in Amazon S3. These video files can be recreated. The company will access the stored files once per day for the first 60 days. After day 60, the company will access the files infrequently for the next 6 months. After that 6-month period, the company will very rarely access the files. However, company policy dictates that the files must be accessible within 5 hours.

Which S3 Lifecycle configuration will meet these requirements MOST cost-effectively?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Use S3 Intelligent-Tiering for the first 60 days. Use S3 One Zone-Infrequent Access (S3 One Zone-IA) for day 60 through the next 6 months. Use S3 Glacier Deep Archive after that 6-month period.**

  *Giải thích:* S3 Intelligent-Tiering is ideal when you want to optimize storage costs for data that has unknown or variable access patterns. However, in this scenario, the access patterns are well known. S3 Glacier Deep Archive is a low-cost option for data storage, but retrieval can take up to 12 hours.
  For more information about the cost of S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

- **B. Use S3 Standard for the first 60 days. Use S3 Standard-Infrequent Access (S3 Standard-IA) for day 60 through the next 6 months. Use S3 Glacier Deep Archive after that 6-month period.**

  *Giải thích:* In a scenario where data can be recreated, you can use S3 One Zone-IA. S3 One Zone-IA has a lower storage cost than S3 Standard-IA. S3 Glacier Deep Archive is a low-cost option for data storage, but retrieval can take up to 12 hours.
  For more information about the cost of S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

- **C. Use S3 Intelligent-Tiering for the first 60 days. Continue to use S3 Intelligent-Tiering for the next 6 months. Use S3 Glacier Flexible Retrieval after that 6-month period.**

  *Giải thích:* S3 Intelligent-Tiering is ideal when you want to optimize storage costs for data that has unknown or variable access patterns. However, in this scenario, the access patterns are well known.
  For more information about the cost of S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

- **D. Use S3 Standard for the first 60 days. Use S3 One Zone-Infrequent Access (S3 One Zone-IA) for day 60 through the next 6 months. Use S3 Glacier Flexible Retrieval after that 6-month period.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* For frequently accessed data, S3 Standard provides the lowest cost option for the first 60 days because there are no additional retrieval fees. S3 One Zone-IA is a low-cost option for infrequently accessed data that can be recreated. The company can use S3 One Zone-IA for object access during the next 6 months because the company does not need the higher availability. When the company needs to access the data very rarely, S3 Glacier Flexible Retrieval is the lowest cost object storage that allows retrieval in less than 5 hours.
  For more information about S3 Lifecycle configurations, see Managing Your Storage Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html 
  For more information about the cost of S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

---

## Câu 68 — ❌ Sai

*Multiple Choice · Thời gian làm: 1 minutes 54 seconds*

**Đề bài:**

A financial services company loaded millions of historical stock trades into an Amazon DynamoDB table. The table uses on-demand capacity mode. Once each day at midnight, a few million new records are loaded into the table. Application read activity against the table happens in bursts throughout the day. A limited set of keys are repeatedly looked up. The company needs to reduce costs associated with DynamoDB.

Which solution will meet these requirements with the LEAST operational overhead?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Use provisioned capacity mode. Purchase Savings Plans in AWS Cost Explorer.**

  *Giải thích:* Provisioned capacity mode with reserved capacity can reduce costs for predictable workloads. However, this solution does not address the repeated lookups of a limited key set. Savings Plans are not available for DynamoDB. You cannot purchase Savings Plans through Cost Explorer.
  Learn more about DynamoDB capacity modes. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html

- **B. Deploy DynamoDB Accelerator (DAX). Use provisioned capacity mode. Configure DynamoDB auto scaling.**  
  _✔ Đáp án đúng_

  *Giải thích:* DAX provides in-memory caching for frequently accessed keys. This solution can reduce read costs significantly. DAX is purpose-built for DynamoDB tables. Therefore, this solution minimizes operational overhead. Provisioned capacity mode with auto scaling handles predictable daily load patterns more cost-effectively than on-demand mode for this workload pattern.
  Learn more about DAX. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html 
  Learn more about DynamoDB auto scaling. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html

- **C. Deploy an Amazon ElastiCache cluster in front of the DynamoDB table.**

  *Giải thích:* ElastiCache can cache frequently accessed data. However, this solution requires additional infrastructure management and integration code changes. DAX is purpose-built for DynamoDB caching and provides better integration with lower operational overhead.
  Learn more about DAX. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html 
  Learn more about ElastiCache. https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html

- **D. Deploy DynamoDB Accelerator (DAX). Configure DynamoDB auto scaling. Purchase Savings Plans in AWS Cost Explorer.**  
  _☑ Bạn đã chọn_

  *Giải thích:* DynamoDB auto scaling is not compatible with on-demand capacity mode. Savings Plans are not available for DynamoDB. You cannot purchase Savings Plans through Cost Explorer. This combination of services cannot be implemented together.
  Learn more about DynamoDB auto scaling. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html 
  Learn more about Cost Explorer. https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html

---

## Câu 69 — ✅ Đúng

*Multi-Select · Thời gian làm: 2 minutes 37 seconds*

**Đề bài:**

A company deploys a new application on AWS. The application runs on two Amazon EC2 instances in two different Availability Zones behind an internet-facing Application Load Balancer (ALB). The application accesses an Amazon RDS Multi-AZ DB instance.

Within the first week, customers report that the application is having performance issues. Investigations identify two potential reasons for the performance issues: slow read responses from the RDS database and periodic high CPU utilization on the two EC2 instances. A solutions architect needs to implement changes to improve performance and to improve repetitive read responses for the new infrastructure. The solution must be fault-tolerant and must support native automated failover across Availability Zones.

Which combination of configuration changes will meet these requirements?

**Đáp án bạn chọn:** A, B  
**Đáp án đúng:** A, B

**Các lựa chọn và giải thích:**

- **A. Create an Amazon ElastiCache (Redis OSS) cluster to cache responses from the RDS database.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* ElastiCache gives you the ability to set up, manage, and scale a distributed in-memory data store or cache environment in the cloud. An ElastiCache cluster to cache the RDS database responses can improve repetitive read response times. ElastiCache (Redis OSS) natively supports automatic Multi-AZ failover.
  For more information about ElastiCache, see What Is Amazon ElastiCache?

- **B. Create an Amazon EC2 Auto Scaling group across Availability Zones. Configure the EC2 Auto Scaling group to be the target for the ALB.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* An Auto Scaling group would give the application the ability to scale out when CPU utilization increases. A solution that spreads the EC2 instances across multiple Availability Zones meets the requirement for high availability.
  For more information about Auto Scaling groups, see Auto Scaling Groups 
  .
  For more information about how to attach an ALB to an Auto Scaling group, see Attaching a Load Balancer to Your Auto Scaling Group 
  .

- **C. Create an Amazon ElastiCache (Memcached) cluster to cache responses from the RDS database.**

  *Giải thích:* ElastiCache gives you the ability to set up, manage, and scale a distributed in-memory data store or cache environment in the cloud. However, ElastiCache (Memcached) does not natively support automatic Multi-AZ failover. ElastiCache (Redis OSS) does meet this requirement.
  For more information about ElastiCache, see What Is Amazon ElastiCache? 
  For more information about the differences between ElastiCache (Memcached) and ElastiCache (Redis OSS), see Comparing Valkey, Memcached, and Redis OSS self-designed caches 
  .

- **D. Increase the instance size of the EC2 instances to meet CPU capacity requirements.**

  *Giải thích:* A change in the instance size could address the issues with high CPU utilization. However, without an Auto Scaling group to automatically replace failed instances, this solution would only partially meet the requirement for fault tolerance.
  For more information about how to change an EC2 instance size, see Change the Instance Type 
  .
  For more information about Auto Scaling groups, see Auto Scaling Groups 
  .

- **E. Add two more EC2 instances to host the application. Register the instances with the ALB.**

  *Giải thích:* The addition of EC2 instances could address the CPU utilization issue. However, more than two additional instances might be necessary. Additionally, this solution would not meet the requirement for high availability because there is no automatic Multi-AZ failover response. An Auto Scaling group would be a better solution for scaling and high availability.
  For more information about Auto Scaling groups, see Auto Scaling Groups 
  .

---

## Câu 70 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 8 seconds*

**Đề bài:**

To be FIPS 140-2 Level 3 compliant, a company needs to store encryption keys. The keys need to be available between the hours of 8:00 AM and 6:00 PM US Eastern Time, Monday through Friday. The keys must not be available outside of these hours. The company needs a highly available solution to store the encryption keys.

Which solution will meet these requirements MOST cost-effectively?

**Đáp án bạn chọn:** C  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create an AWS CloudHSM cluster with instances in multiple Availability Zones. Create an Amazon DynamoDB table. Store the CloudHSM metadata in the DynamoDB table. Create and schedule AWS Lambda functions to delete and recreate the CloudHSM cluster from a cluster backup. Configure the Lambda functions to retrieve the necessary metadata from the DynamoDB table.**

  *Giải thích:* CloudHSM provides dedicated hardware security modules in the AWS Cloud that are FIPS 140-2 Level 3 compliant. DynamoDB is a fully managed NoSQL database service. It is cost-effective to delete the CloudHSM cluster when the cluster is not needed. However, data storage in DynamoDB would incur unnecessary costs.
  For more information about CloudHSM, see What Is AWS CloudHSM? https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html 
  For more information about DynamoDB, see What Is Amazon DynamoDB? https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

- **B. Store the encryption keys in AWS KMS. Create and schedule AWS Lambda functions to remove and add key access policies as necessary.**

  *Giải thích:* AWS KMS is a managed service that gives you the ability to create and control the cryptographic keys that are used to protect data. However, AWS KMS is FIPS 140-2 Level 2 compliant. The company needs to be FIPS 140-2 Level 3 compliant.
  For more information about AWS KMS, see AWS Key Management Service. https://docs.aws.amazon.com/kms/latest/developerguide/overview.html

- **C. Store the encryption keys in AWS KMS. Create and schedule AWS Lambda functions to disable and enable the stored encryption keys as necessary.**  
  _☑ Bạn đã chọn_

  *Giải thích:* AWS KMS is a managed service that gives you the ability to create and control the cryptographic keys that are used to protect data. However, AWS KMS is FIPS 140-2 Level 2 compliant. The company needs to be FIPS 140-2 Level 3 compliant.
  For more information about AWS KMS, see AWS Key Management Service. https://docs.aws.amazon.com/kms/latest/developerguide/overview.html

- **D. Create an AWS CloudHSM cluster with instances in multiple Availability Zones. Store the CloudHSM metadata as standard parameters in AWS Systems Manager Parameter Store. Create and schedule AWS Lambda functions to delete and recreate the CloudHSM cluster from a cluster backup. Configure the Lambda functions to retrieve the necessary metadata from Parameter Store.**  
  _✔ Đáp án đúng_

  *Giải thích:* CloudHSM provides dedicated hardware security modules in the AWS Cloud that are FIPS 140-2 Level 3 compliant. Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. Storage of standard parameters in Parameter Store is free. A solution that deletes the CloudHSM cluster when the cluster is not needed and that stores secrets in Parameter Store is the most cost-effective option.
  For more information about how to reduce the cost of CloudHSM by limiting operating hours, see How to Lower Costs by Automatically Deleting and Recreating HSMs. https://aws.amazon.com/blogs/security/how-to-lower-costs-by-automatically-deleting-and-recreating-hsms 
  For more information about CloudHSM, see What Is AWS CloudHSM? https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html 
  For more information about Parameter Store, see AWS Systems Manager Parameter Store. https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html

---

## Câu 71 — ✅ Đúng

*Multiple Choice · Thời gian làm: 2 minutes 15 seconds*

**Đề bài:**

A company uses AWS Organizations with all features turned on to manage multiple AWS accounts. The tag names and values that are applied to the resources across accounts are inconsistent. The company wants to generate cost allocation reports based on a standardized set of tag names and values. The company needs to identify and correct noncompliant tags. After these corrections, the company will enforce the use of the standardized tags.

How can a solutions architect correct the noncompliant tags and enforce the use of only compliant tags in the future?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create tag policies in Organizations for the required tags. Select the option to prevent noncompliant operations for this tag to enforce use of the tags. Attach the tag policies to the organization entities as required. Use AWS Resource Groups to find noncompliant tags. Correct the tags by using the AWS service that created the resources.**

  *Giải thích:* Tag policies help standardize tags across resources in an organization's accounts. You can use Resource Groups to detect noncompliant resources and generate a report so that you can make corrections. However, the option to prevent noncompliant operations for this tag would not have any effect on resources that are created with no tags. An SCP is required to enforce the addition of the tags.
  For more information about tag policies in Organizations, see Tag Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_tag-policies.html 
  For more information about tag policy enforcement, see Understanding Enforcement. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_tag-policies-enforcement.html 
  For more information about how to use Resource Groups to manage compliance, see What Are Resource Groups? https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html

- **B. Create an Amazon EventBridge rule to monitor the addition of noncompliant tags to an AWS resource. Configure the rule to send a message to Amazon SQS. Configure the SQS queue to invoke an AWS Lambda function to apply an appropriate tag to the AWS resource.**

  *Giải thích:* EventBridge event-based rules can detect and automatically correct noncompliant resources in AWS. However, EventBridge cannot enforce the use of compliant tags in the future.
  For more information about EventBridge rules based on events, see Creating Amazon EventBridge Rules That React to Events. https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html

- **C. Use AWS Config to create managed rules in each account. Use the required-tags rule to apply specific tags to the AWS resources. Activate AWS Config for the organization. Create a custom AWS Systems Manager Automation runbook to automatically apply the appropriate tag to the AWS resource.**

  *Giải thích:* AWS Config managed rules can detect and automatically correct noncompliant resources in AWS. However, you cannot use AWS Config to enforce the use of compliant tags in the future.
  For more information about AWS Config managed rules, see AWS Config Managed Rules. https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config\_use-managed-rules.html 
  For more information about the AWS Config required-tags rule, see Required-Tags. https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html

- **D. Create tag policies in Organizations for the required tags. Attach the tag policies to the organization entities as required. Use AWS Resource Groups to find noncompliant tags. Correct the tags by using the AWS service that created the resources. Use SCPs to enforce the use of the tags across the organization.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* Tag policies help standardize tags across resources in an organization's accounts. You can use Resource Groups to detect noncompliant resources and generate a report so that you can make corrections. You can use SCPs to enforce the use of tags within the organization.
  For more information about tag policies in Organizations, see Tag Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_tag-policies.html 
  For more information about SCPs, see Service Control Policies (SCPs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_scps.html 
  For more information about how to use Resource Groups to manage compliance, see What Are Resource Groups? https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html

---

## Câu 72 — ✅ Đúng

*Multiple Choice · Thời gian làm: 3 minutes*

**Đề bài:**

A company runs a group of Amazon EC2 instances in a private subnet. The subnet is in a VPC in the us-east-1 Region. The EC2 instances store a large amount of sensitive data in an Amazon S3 bucket. Data that transfers between the EC2 instances and the S3 bucket must not travel across the internet. A solutions architect creates a gateway VPC endpoint to allow the EC2 instances to access the S3 bucket.

The solutions architect creates a second group of EC2 instances in a private subnet of a VPC in the eu-west-2 Region. The second group of EC2 instances requires infrequent access to the same data that is stored in the existing S3 bucket. The amount of data that will travel between the S3 bucket in us-east-1 and the EC2 instances in eu-west-2 will be low. The company needs to grant the second group of EC2 instances access to the data in the S3 bucket.

Which solution will meet these requirements MOST cost-effectively?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create an Amazon EFS file system in us-east-1. Create mount targets in each subnet where the EC2 instances are running to provide access to the file system. Transfer all the data from the S3 bucket to the file system.**

  *Giải thích:* Amazon EFS provides a shared NFS for use with multiple AWS services within a Region. However, with standard access patterns, S3 storage has a lower cost per GB than Amazon EFS. In a scenario where the amount of data that is stored is high but the amount of data that is transferred is low, the storage cost is the biggest factor. S3 storage is a more cost-effective solution.
  For more information about Amazon EFS, see What Is Amazon Elastic File System? https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html

- **B. Create a second S3 bucket in eu-west-2. Create a gateway VPC endpoint for the second S3 bucket. Allow the EC2 instances in eu-west-2 to communicate with the second S3 bucket. Copy the existing data and configure S3 Cross-Region Replication (CRR) between the two S3 buckets.**

  *Giải thích:* A solution that uses CRR between the two S3 buckets would double the cost of the S3 storage and would add the cost of the replication of the complete dataset. The volume of data that is stored is large, but the volume of data that is transferred is low. Therefore, a solution that duplicates all the data would not be as cost-effective as a solution that stores the data once and allows access when the data is needed across the network.
  For more information about CRR, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario 
  For more information about gateway VPC endpoints, see Gateway VPC Endpoints. https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html

- **C. Create a second S3 bucket in eu-west-2. Create a gateway VPC endpoint for the second S3 bucket. Allow the EC2 instances in eu-west-2 to communicate with the second S3 bucket. Copy the existing data and use an AWS Lambda function to copy new objects between the two S3 buckets.**

  *Giải thích:* You can use Lambda to replicate objects to multiple destination S3 buckets in the same Region or different Regions. However, this solution adds costs for data transfer and the use of Lambda. This solution also increases S3 storage costs. The volume of data that is stored is large, but the volume of data that is transferred is low. Therefore, a solution that duplicates all the data would not be as cost-effective as a solution that stores the data once and allows access when the data is needed across the network.
  For more information about Lambda, see What Is AWS Lambda? https://docs.aws.amazon.com/lambda/latest/dg/welcome.html 
  For more information about gateway VPC endpoints, see Gateway VPC Endpoints. https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html

- **D. Create an interface VPC endpoint for the S3 bucket in the VPC in us-east-1 by using AWS PrivateLink. Peer the VPCs and configure routing between the VPCs. Configure access to the S3 bucket in us-east-1 from the EC2 instances in eu-west-2 by using the endpoint.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* An interface VPC endpoint allows instances that are running in a VPC to connect to other AWS services privately through an elastic network interface. Use of a single S3 bucket along with an interface VPC endpoint is the most cost-effective solution because the volume of data that is stored is large and the volume of data that is transferred is low.
  For more information about interface endpoints for Amazon S3, see AWS PrivateLink for Amazon S3. https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html

---

## Câu 73 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 18 seconds*

**Đề bài:**

A company needs to create a web application on AWS to manage registrations for a conference. A database will store the registration information. Additionally, the web application will use several static files. The company's PHP web developer is familiar with the use of LAMP stack applications but does not have much AWS expertise. The company does not expect large changes in traffic on the web application and wants predictable pricing to facilitate budgeting for the conference.

Which solution will meet these requirements with the LEAST time required to learn new technologies?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** D

**Các lựa chọn và giải thích:**

- **A. Create and package the web application as a Docker container. Deploy the container by using AWS Fargate. Configure Amazon DynamoDB for the database. Configure Amazon S3 for the static files.**

  *Giải thích:* You can use Fargate to run containers without the need to manage servers or clusters of Amazon EC2 instances. However, you would need to develop some expertise to build and create Docker containers. Use of DynamoDB would also require additional time to learn.
  For more information about Fargate, see What is AWS Fargate? https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html 
  For more information about DynamoDB, see From SQL to NoSQL. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html

- **B. Create and package the web application as a .zip file. Deploy the web application by using AWS Elastic Beanstalk. Configure Amazon DynamoDB for the database. Configure Amazon S3 for the static files.**  
  _☑ Bạn đã chọn_

  *Giải thích:* You can use Elastic Beanstalk to quickly deploy and manage applications in the AWS Cloud without the need to learn about the underlying infrastructure. However, the price model is based on the resources that the application consumes. This solution would not meet the requirement for predictable pricing. Use of DynamoDB would also require additional time to learn.
  For more information about Elastic Beanstalk, see What is AWS Elastic Beanstalk? https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html 
  For more information about DynamoDB, see From SQL to NoSQL. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html

- **C. Create the web application by using AWS Lambda functions. Deploy the web application by using Amazon API Gateway. Configure Amazon RDS for the database. Configure Amazon S3 for the static files.**

  *Giải thích:* API Gateway is an AWS service you can use to create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale. API developers can create APIs that access AWS services, other web services, and data that is stored in the AWS Cloud. However, you would need to have significant AWS expertise to build the required APIs.
  For more information about API Gateway, see What is Amazon API Gateway? https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome 
  For more information about the configuration of Lambda functions, see Configuring AWS Lambda Functions. https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html

- **D. Create and package the web application by using Amazon Lightsail. Create a Lightsail instance by using an appropriate preconfigured template. Use Lightsail object storage to store the static files.**  
  _✔ Đáp án đúng_

  *Giải thích:* Lightsail provides developers with compute, storage, and network capacity tools. Lightsail also provides the ability to deploy and manage websites and web applications in the cloud. Lightsail offers affordable and predictable monthly payment plans.
  For more information about Lightsail, see Amazon Lightsail Documentation. https://docs.aws.amazon.com/lightsail 
  For more information about Lightsail object storage, see Object Storage in Amazon Lightsail. https://lightsail.aws.amazon.com/ls/docs/en\_us/articles/buckets-in-amazon-lightsail 
  For more information about deployment of LAMP (PHP) applications with Lightsail, see Tutorial: Launch and Configure a LAMP Instance in Amazon Lightsail. https://lightsail.aws.amazon.com/ls/docs/en\_us/articles/amazon-lightsail-tutorial-launching-and-configuring-lamp

---

## Câu 74 — ❌ Sai

*Multiple Choice · Thời gian làm: 2 minutes 1 seconds*

**Đề bài:**

A company is designing a new application that stores data in Amazon S3. The company creates an S3 bucket with default settings. According to company regulations, no user can delete objects or write over objects in the S3 bucket for a minimum of 5 years after the initial storage of the objects.

Which solution will meet these requirements?

**Đáp án bạn chọn:** D  
**Đáp án đúng:** A

**Các lựa chọn và giải thích:**

- **A. Create a new S3 bucket with S3 Versioning and S3 Object Lock turned on. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to compliance mode. Move the existing objects to the new S3 bucket.**  
  _✔ Đáp án đúng_

  *Giải thích:* Object Lock with a 5-year retention period would lock the objects and prevent the objects from being overwritten or deleted. In compliance mode, objects cannot be overwritten or deleted by any user, including the root user of the account, for the duration of the retention period. Because you can configure Object Lock only when you first create a bucket, you would need a new bucket.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html 
  For more information about Object Lock retention modes, see Retention Modes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes

- **B. Create a new S3 bucket with S3 Versioning and S3 Object Lock turned on. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to governance mode. Move the existing objects to the new S3 bucket.**

  *Giải thích:* Object Lock with a 5-year retention period would lock the objects and prevent the objects from being overwritten or deleted. However, in governance mode, a user that has appropriate permissions could remove the lock and delete the objects.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html 
  For more information about Object Lock retention modes, see Retention Modes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes

- **C. Modify the existing S3 bucket by turning on S3 Versioning and S3 Object Lock. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to governance mode.**

  *Giải thích:* You can configure S3 Versioning for an existing S3 bucket, but you can configure Object Lock only when you first create a bucket. You cannot configure Object Lock for a bucket that already exists. In governance mode, a user that has appropriate permissions could remove the lock and delete the objects.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html 
  For more information about Object Lock retention modes, see Retention Modes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes

- **D. Modify the existing S3 bucket by turning on S3 Versioning and S3 Object Lock. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to compliance mode.**  
  _☑ Bạn đã chọn_

  *Giải thích:* You can configure S3 Versioning for an existing S3 bucket, but you can configure Object Lock only when you first create a bucket. You cannot configure Object Lock for a bucket that already exists.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html

---

## Câu 75 — ✅ Đúng

*Multiple Choice · Thời gian làm: 1 minutes 6 seconds*

**Đề bài:**

A company that designs multiplayer online games wants to expand its user base outside of Europe. The company transfers a significant amount of UDP traffic to keep all the live and interactive sessions of the games. The company has plans for rapid expansion and wants to build its architecture to provide an optimized online experience to its users.

Which architecture will meet these requirements with the LOWEST latency for users?

**Đáp án bạn chọn:** B  
**Đáp án đúng:** B

**Các lựa chọn và giải thích:**

- **A. Set up a Multi-AZ environment in a single AWS Region. Use Amazon CloudFront to cache user sessions.**

  *Giải thích:* CloudFront delivers HTML, CSS, JS, and image files, not UDP traffic.
  For more information about CloudFront, see What Is Amazon CloudFront? https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

- **B. Set up environments in multiple AWS Regions. Create an accelerator in AWS Global Accelerator, and add endpoints from different Regions to it.**  
  _✔ Đáp án đúng · ☑ Bạn đã chọn_

  *Giải thích:* You can reduce latency by setting up the access perimeter in multiple Regions. Global Accelerator is well suited for UDP (and gaming) services, among other use cases.
  For more information about Global Accelerator, see AWS Global Accelerator FAQs. https://aws.amazon.com/global-accelerator/faqs/

- **C. Set up environments in multiple AWS Regions. Use Amazon Route 53, and select latency-based routing.**

  *Giải thích:* Latency-based routing will route over the public internet instead of AWS's global network. Latency-based routing will not provide the same level of performance as Global Accelerator.

- **D. Set up a Multi-AZ environment in a single AWS Region. Use AWS Lambda@Edge to update sessions closer to the users.**

  *Giải thích:* In this solution, all customers will interact with a single Region. This solution can add to latency or performance issues.

---

