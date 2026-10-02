# TD Set 2 — Correct Answer Review (43 questions)

Source: `TD_SAP_Review_Set2_Full.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/⚠️/🧠 are study notes. Wrong answers: `td_set_2_review.md`.

## Purpose

Confirm each correct answer was **knowledge, not a guess**. Answer again without looking; if you can't justify why every wrong option fails, tick **Guessed** and treat it as a wrong answer.

## ⚠️ Inconsistent concepts (right here, wrong elsewhere in this test)

| Right | Wrong | Concept |
|---|---|---|
| Q72, Q55 | Q15 | EC2/app access via IAM role / STS temporary credentials |
| Q57 | Q31 | SAML federation → AssumeRoleWithSAML |
| Q69, Q53 | Q44 | OAC vs signed URLs (path vs specific client) |
| Q65 | Q1 | ACM public certificates |
| Q11, Q13, Q46 | Q68, Q14 | Multi-AZ = HA, not DR / not RMAN |
| Q19 | Q75, Q66 | IAM policies with conditions grant access; SCPs don't |
| Q58, Q70 | Q24 | Streaming ingestion (Kinesis / Firehose) |

These are partial knowledge — review each pair together.

## Tracker

| Group | Q | Guessed? | Pass 1 | Pass 2 |
|---|---|---|---|---|
| A | [Q5](#q5) | ☐ | ☐ | ☐ |
| A | [Q19](#q19) | ☐ | ☐ | ☐ |
| A | [Q22](#q22) | ☐ | ☐ | ☐ |
| A | [Q35](#q35) | ☐ | ☐ | ☐ |
| A | [Q55](#q55) | ☐ | ☐ | ☐ |
| A | [Q57](#q57) | ☐ | ☐ | ☐ |
| A | [Q72](#q72) | ☐ | ☐ | ☐ |
| B | [Q6](#q6) | ☐ | ☐ | ☐ |
| B | [Q42](#q42) | ☐ | ☐ | ☐ |
| B | [Q53](#q53) | ☐ | ☐ | ☐ |
| B | [Q54](#q54) | ☐ | ☐ | ☐ |
| B | [Q65](#q65) | ☐ | ☐ | ☐ |
| B | [Q69](#q69) | ☐ | ☐ | ☐ |
| C | [Q10](#q10) | ☐ | ☐ | ☐ |
| C | [Q11](#q11) | ☐ | ☐ | ☐ |
| C | [Q13](#q13) | ☐ | ☐ | ☐ |
| C | [Q29](#q29) | ☐ | ☐ | ☐ |
| C | [Q46](#q46) | ☐ | ☐ | ☐ |
| C | [Q48](#q48) | ☐ | ☐ | ☐ |
| C | [Q63](#q63) | ☐ | ☐ | ☐ |
| D | [Q39](#q39) | ☐ | ☐ | ☐ |
| D | [Q51](#q51) | ☐ | ☐ | ☐ |
| D | [Q52](#q52) | ☐ | ☐ | ☐ |
| D | [Q61](#q61) | ☐ | ☐ | ☐ |
| D | [Q71](#q71) | ☐ | ☐ | ☐ |
| E | [Q8](#q8) | ☐ | ☐ | ☐ |
| E | [Q12](#q12) | ☐ | ☐ | ☐ |
| E | [Q20](#q20) | ☐ | ☐ | ☐ |
| E | [Q21](#q21) | ☐ | ☐ | ☐ |
| E | [Q30](#q30) | ☐ | ☐ | ☐ |
| E | [Q40](#q40) | ☐ | ☐ | ☐ |
| E | [Q47](#q47) | ☐ | ☐ | ☐ |
| E | [Q58](#q58) | ☐ | ☐ | ☐ |
| E | [Q64](#q64) | ☐ | ☐ | ☐ |
| E | [Q70](#q70) | ☐ | ☐ | ☐ |
| E | [Q73](#q73) | ☐ | ☐ | ☐ |
| E | [Q74](#q74) | ☐ | ☐ | ☐ |
| F | [Q4](#q4) | ☐ | ☐ | ☐ |
| F | [Q16](#q16) | ☐ | ☐ | ☐ |
| F | [Q25](#q25) | ☐ | ☐ | ☐ |
| F | [Q33](#q33) | ☐ | ☐ | ☐ |
| F | [Q36](#q36) | ☐ | ☐ | ☐ |
| F | [Q60](#q60) | ☐ | ☐ | ☐ |

---

# Group A — Identity, access & federation (7)

<a id="q5"></a>

## Q5

An analytics company plans to create a self-service solution that will provide a safe and cost-effective way for data scientists to access Amazon SageMaker AI on the company’s AWS accounts. The data scientists have limited knowledge of the AWS cloud, so the complex setup requirements for its ML models should not be exposed. The company wants the data scientists to be able to launch a Jupyter notebook instance if needed. The data at rest on the storage volume of the notebook instance must be encrypted with a preconfigured AWS KMS key.
Which of the following solutions will meet the company requirements with the LEAST amount of operational overhead?

- **A.** Create a self-service portal using AWS Proton and upload standardized service templates to Amazon S3. Add IAM permissions to the data scientist IAM group to use Proton. Write a custom AWS CLI script that will take input parameters from the data scientist for the requested Jupyter notebook instance with the pre-configured KMS key. Have the data scientists execute the script locally on their computers.
- **B.** Create an Amazon S3 bucket with website hosting enabled. Create a simple form as a front-end website hosted on the S3 bucket that allows the data scientist to input their request for Jupyter notebook creation. Send the request to an Amazon API Gateway that will invoke an AWS Lambda function with an IAM role permission to create the Jupyter notebook instance with a preconfigured KMS key. Have the Lambda function reply the URL of the notebook instance for display on the front-end website.
- **C.** Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. On the Outputs section of the CloudFormation template, reference the URL of the notebook instance. Rename this template to be more user-friendly and upload it to a shared Amazon S3 bucket for distribution to the data scientists.
- **D.** Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. Create Mappings on the CloudFormation to map simpler parameter names for instance sizes such as Small, Medium, Large. Reference the URL of the notebook instance on the Outputs section of the template. Create a portfolio in AWS Service Catalog and upload the template to be shared with the IAM role of the data scientists.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** self-service SageMaker notebooks; hide complexity; preconfigured KMS key

⚠️ **Watch:** Proton is for platform templates, not end-user self-service

🧠 **Rule:** Governed self-service launch → Service Catalog portfolio of CloudFormation products.

### TD explanation

AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage deployed IT services and your applications, resources, and metadata.
With AWS Service Catalog, you define your own catalog of AWS services and AWS Marketplace software and make them available for your organization. Then, end users can quickly discover and deploy IT services using a self-service portal.
Amazon SageMaker AI is a fully managed machine learning service. With SageMaker AI, data scientists and developers can quickly and easily build and train machine learning models and then directly deploy them into a production-ready hosted environment. It provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don’t have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. With native support for bring-your-own algorithms and frameworks, SageMaker AI offers flexible distributed training options that adjust to your specific workflows.
You can easily create a self-service, secured data science using Amazon SageMaker AI, AWS Service Catalog, and AWS Key Management Service (KMS). Using AWS Service Catalog, you can use a pre-configured AWS KMS key to encrypt data at rest on the machine learning (ML) storage volume that is attached to your notebook instance without ever exposing the complex, unnecessary details to data scientists. ML storage volume encryption is enforced by an AWS Service Catalog product that is pre-configured by centralized security and/or infrastructure teams.

Hence, the correct answer is: Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. Create Mappings on the CloudFormation to map simpler parameter names for instance sizes such as Small, Medium, Large. Reference the URL of the notebook instance on the Outputs section of the template. Create a portfolio in AWS Service Catalog and upload the template to be shared with the IAM role of the data scientists.
The option that says: Create an Amazon S3 bucket with website hosting enabled. Create a simple form as a front-end website hosted on the S3 bucket that allows the data scientist to input their request for Jupyter notebook creation. Send the request to an Amazon API Gateway that will invoke an AWS Lambda function with an IAM role permission to create the Jupyter notebook instance with a preconfigured KMS key. Have the Lambda function reply the URL of the notebook instance for display on the front-end website is incorrect. Although this is possible, this requires a lot of operational overhead as you need to write a custom website and write a proper Lambda function that has the appropriate code to create the needed resources. Additionally, as the company has several accounts, you will need to create the Lambda function for each AWS account.
The option that says: Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. On the Outputs section of the CloudFormation template, reference the URL of the notebook instance. Rename this template to be more user-friendly and upload it to a shared Amazon S3 bucket for distribution to the data scientists is incorrect. This is possible, however, it is not very user-friendly as the users need to download the appropriate CloudFormation template from Amazon S3 and then upload it to CloudFormation. They just need to input the needed parameters for the creation of their Jupyter notebook instance.
The option that says: Create a self-service portal using AWS Proton and upload standardized service templates to Amazon S3. Add IAM permissions to the data scientist IAM group to use Proton. Write a custom AWS CLI script that will take input parameters from the data scientist for the requested Jupyter notebook instance with the pre-configured KMS key. Have the data scientists execute the script locally on their computers is incorrect. You don’t have to write a custom AWS CLI script to take input parameters and run the script on the local machines. It is only possible to create a self-service portal using AWS Proton. You can use it to speed up the software development lifecycle with pre-approved templates for infrastructure.

References:
https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/
https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html

Check out these Amazon SageMaker AI and AWS Service Catalog Cheat Sheets:
https://tutorialsdojo.com/amazon-sagemaker/
https://tutorialsdojo.com/aws-service-catalog/

</details>

<a id="q19"></a>

## Q19

A pharmaceutical firm must securely store confidential experimental data. The company manages user authentication through AWS IAM Identity Center and has assigned its R&D scientists to a dedicated group.
The firm wants to consolidate all research documents into a shared Amazon S3 bucket while ensuring that each scientist can only access files they own. In addition, the company wants monthly audit reports detailing which users accessed which documents.
What combination of steps will satisfy these requirements? (Select TWO.)

- **A.** Create a custom IAM Identity Center role with a permission set granting access to the S3 bucket. Use an identity-based policy restricting data access to prefixes identified by each user’s tag, such as the ${aws:PrincipalTag/userNameID}/*condition.
- **B.** Use S3 Object Lock in Governance mode to prevent unauthorized research data modification. Use AWS Config rules to monitor and report on S3 object access patterns every week.
- **C.** Create an S3 Access Point for each scientist with a resource policy restricting access to objects with matching prefixes. Enable S3 Server Access Logging and use Amazon QuickSight to visualize access patterns.
- **D.** Turn on S3 server access logging and store the logs in an EMRFS (EMR File System ). Use Amazon Athena to query the EMRFS logs directly for monthly usage reporting.
- **E.** Enable AWS CloudTrail data event logging for the S3 bucket and store these logs in a separate bucket. Use Amazon Athena (with an Amazon Athena connector) to query the CloudTrail logs monthly and generate comprehensive user access reports.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E (you answered correctly)

🔑 **Key words:** Identity Center group; each scientist only own files; monthly access reports (Select TWO)

⚠️ **Watch:** Server access logs lack IAM identity detail; ⚠️ resource-level IAM conditions also decide Q75

🧠 **Rule:** Per-user prefix → ${aws:PrincipalTag/...} policy; who accessed what → CloudTrail data events + Athena.

### TD explanation

AWS IAM Identity Center centralizes access management for various AWS accounts and applications. It provides single sign-on (SSO) access, enabling users to manage all their assigned accounts from a single location. Users can synchronize with an existing identity provider or create new users and groups directly within the service.
IAM Identity Center utilizes permission sets—collections of IAM policies—to manage user access across AWS Organizations. It includes a user-friendly AWS Access Portal for easy access to applications and supports deployment for both organization and account instances. Designed for high availability across multiple availability zones, the service ensures secure access through AWS Identity and Access Management (IAM) roles and policies.

CloudTrail data events are detailed records of resource operations in AWS services. They provide visibility into specific actions performed on or within a resource, such as Amazon S3 object-level API activity, Lambda function executions, or DynamoDB table operations.

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. It’s serverless, so there’s no infrastructure to manage, and you pay only for the queries you run.
Hence, the correct answers are:
– Create a custom IAM Identity Center role with a permission set granting access to the S3 bucket. Use an identity-based policy restricting data access to prefixes identified by each user’s tag, such as the ${aws:PrincipalTag/userNameID}/*condition. This approach uses the IAM Identity Center for authentication and leverages identity-based policies with user tags to restrict access to specific prefixes in the S3 bucket. This meets the requirement of ensuring each scientist can only access their own files.
– Enable AWS CloudTrail data event logging for the S3 bucket and store these logs in a separate bucket. Use Amazon Athena (with an Amazon Athena connector) to query the CloudTrail logs monthly and generate comprehensive user access reports. CloudTrail can log all data events (object-level API activity) in the S3 bucket, and Athena can be used to query these logs and generate detailed reports on user access patterns.
The option that says: Use S3 Object Lock in Governance mode to prevent unauthorized research data modification. Use AWS Config rules to monitor and report on S3 object access patterns every week is incorrect. While S3 Object Lock can typically prevent modifications, it doesn’t address the access control requirements. Additionally, AWS Config rules don’t provide detailed access reports as required.
The option that says: Create an S3 Access Point for each scientist with a resource policy restricting access to objects with matching prefixes. Enable S3 Server Access Logging and use Amazon QuickSight to visualize access patterns is incorrect. This option could only work for access control, it doesn’t provide the detailed monthly audit reports required. QuickSight is more suited for business intelligence than detailed access auditing.
The option that says: Turn on S3 server access logging and store the logs in an EMRFS (EMR File System ). Use Amazon Athena to query the EMRFS logs directly for monthly usage reporting is incorrect. While S3 server access logging can provide detailed logs, storing them in EMRFS is unnecessary and complicates the solution. Athena can query S3 logs directly without EMRFS.

References:
https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging-console.html
https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html

Check out the following Cheat Sheets:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/
https://tutorialsdojo.com/amazon-athena/
https://tutorialsdojo.com/aws-cloudtrail/

</details>

<a id="q22"></a>

## Q22

A company is using Microsoft Active Directory to manage all employee accounts and devices. The IT department instructed the solutions architect to implement a single sign-on feature to allow the employees to use their existing Windows account password to connect and use the various AWS resources. 
Which of the following options is the recommended way to extend the current Active Directory domain to AWS?

- **A.** Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.
- **B.** Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps' backend resources in AWS.
- **C.** Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account.
- **D.** Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** existing Windows AD passwords for AWS SSO

⚠️ **Watch:** Cognito is for customer-facing apps

🧠 **Rule:** Extend on-prem AD → AWS Managed Microsoft AD with trust relationship.

### TD explanation

Because the company is using Microsoft Active Directory already, you can use AWS Directory Service for Microsoft AD to create secure Windows trusts between your on-premises Microsoft Active Directory domains and your AWS Microsoft AD domain in the AWS Cloud. By setting up a trust relationship, you can integrate SSO to the AWS Management Console and the AWS Command Line Interface (CLI), as well as your Windows-based workloads.

AWS Directory Service helps you to set up and run a standalone AWS Managed Microsoft AD directory hosted in the AWS Cloud. You can also use AWS Directory Service to connect your AWS resources with an existing on-premises Microsoft Active Directory. To configure AWS Directory Service to work with your on-premises Active Directory, you must first set up trust relationships to extend authentication from on-premises to the cloud.
Therefore, the correct answer is: Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.
The option that says: Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps’ backend resources in AWS is incorrect because Cognito is primarily used for federation to your web and mobile apps running on AWS. It allows you to authenticate users through social identity providers. But since the company is already using Microsoft AD, AWS Directory Service is the better choice here.
The option that says: Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts is incorrect because using the AWS IAM Identity Center service alone is not enough to meet the requirement. Although it can help you manage SSO access and user permissions across all your AWS accounts in AWS Organizations, you still have to use the AWS Directory Service to integrate your on-premises Microsoft AD. AWS IAM Identity Center integrates with Microsoft AD using AWS Directory Service so there is no need to create users and groups.
The option that says: Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account is incorrect because setting up cross-account access allows you to share resources in one AWS account with users in a different AWS account. Since the company is already using Microsoft AD then, the better choice to use here is the AWS Directory Service.

References:
https://aws.amazon.com/directoryservice/
https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-directory-connected.html

Check out this AWS Directory Service Cheat Sheet:
https://tutorialsdojo.com/aws-directory-service/

</details>

<a id="q35"></a>

## Q35

A financial startup offers flexible short-term loans of up to $5,000 to its users. Their online portal is hosted in AWS which uses S3 for scalable storage, DynamoDB as a NoSQL database, and a fleet of EC2 instances to host their web servers. To meet the financial regulation, the company is required to undergo a compliance audit. 
In this scenario, how will you provide the auditor access to the logs of your AWS resources?

- **A.** 1. Create an SNS Topic. 2. Configure the SNS to send out an email with the attached CloudTrail log files to the auditor’s email every time the CloudTrail delivers the logs to S3.
- **B.** 1. Enable CloudTrail logging to required AWS resources. 2. Create an IAM user with read-only permissions to the required AWS resources. 3. Provide the access credential to the auditor.
- **C.** 1. Contact AWS and inform them of the upcoming audit activities. 2. AWS will grant required access to the third-party auditor to see the logs.
- **D.** 1. Create an IAM role that has the required permissions for the auditor. 2. Attach the roles to the EC2, S3, and DynamoDB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** auditor needs log access

⚠️ **Watch:** Never call AWS to grant access

🧠 **Rule:** CloudTrail + least-privilege read-only IAM identity for the auditor.

### TD explanation

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain events related to API calls across your AWS infrastructure. CloudTrail provides a history of AWS API calls for your account, including API calls made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This history simplifies security analysis, resource change tracking, and troubleshooting.

Therefore the correct answer is:
1. Enable CloudTrail logging to required AWS resources.
2. Create an IAM user with read-only permissions to the required AWS resources.
3. Provide the access credential to the auditor.
The following option is incorrect because you do not need to contact AWS for any audit activities since you can just use CloudTrail:
1. Contact AWS and inform them of the upcoming audit activities.
2. AWS will grant required access to the third-party auditor to see the logs.
You can contact AWS in case you will perform penetration testing to or originating from any of your AWS resources as part of the shared responsibility model, but for audit activities like this, an authorization is not required.
The following option is incorrect because it is a security risk to send the CloudTrail logs via email:
1. Create an SNS Topic.
2. Configure the SNS to send out an email with the attached CloudTrail log files to the auditor’s email every time the CloudTrail delivers the logs to S3.
It is best to keep them stored inside an S3 bucket and just provide read access to the bucket to the auditor.
The following option is incorrect because an IAM role should be attached to the IAM user of the auditor but the most preferred way to do this is still to use CloudTrail:
1. Create an IAM role that has the required permissions for the auditor.
2. Attach the roles to the EC2, S3, and DynamoDB.

References:
https://aws.amazon.com/cloudtrail/
https://aws.amazon.com/blogs/security/how-to-audit-cross-account-roles-using-aws-cloudtrail-and-amazon-cloudwatch-events/
https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html

Check out this AWS CloudTrail Cheat Sheet:
https://tutorialsdojo.com/aws-cloudtrail/

</details>

<a id="q55"></a>

## Q55

An advertising company plans to release a new photo-sharing app that will be hosted on the AWS Cloud. The app will store all pictures directly uploaded by users in a single Amazon S3 bucket, and users will also be able to view and download uploaded pictures directly from the S3 bucket. The company uses Amazon Fraud Detector to identify and prevent fraudulent account registrations and suspicious user activities at scale. The development team also uses AWS Device Farm to test the application on a wide range of real mobile devices before launch.
The solutions architect must ensure the security of the application, and it should be able to handle potentially millions of users in the most secure manner.
How should the solutions architect set up the user registration flow in AWS for this mobile app?

- **A.** Generate long-term credentials using AWS STS and apply the appropriate permissions. Store the credentials in the mobile app, and use them to access S3.
- **B.** Store user information in Amazon RDS and create an IAM Role with appropriate permissions. Generate new temporary credentials using the AWS Security Token Service AssumeRole function each time the user opens the mobile app. These credentials will be stored in the mobile app’s memory and will be used to access S3.
- **C.** Create an IAM user, assign appropriate permissions to it, and generate an access key and a secret key that will be stored in the mobile app and used to access S3.
- **D.** Create an IAM user and generate an access key and a secret key to be stored in the mobile app for the IAM user. After applying the appropriate permissions to the S3 bucket policy, use the generated credentials to access S3.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** millions of mobile users; most secure S3 access

⚠️ **Watch:** Never embed long-term access keys in an app

🧠 **Rule:** Mobile clients → temporary STS credentials (AssumeRole / Cognito).

### TD explanation

In this scenario, the best solution is to use a combination of an IAM Role and STS for authentication. The STS AssumeRole returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use AssumeRole for cross-account access or federation.

Therefore, the correct answer is: Store user information in Amazon RDS and create an IAM Role with appropriate permissions. Generate new temporary credentials using the AWS Security Token Service AssumeRole function each time the user opens the mobile app. These credentials will be stored in the mobile app’s memory and will be used to access S3. It creates an IAM Role with appropriate permissions and then generates temporary security credentials using STS AssumeRole. Then, it generates new credentials when the user runs the app the next time.
The option that says: Create an IAM user and generate an access key and a secret key to be stored in the mobile app for the IAM user. After applying the appropriate permissions to the S3 bucket policy, use the generated credentials to access S3 is incorrect. It simply suggests creating an IAM User, not the IAM Role, which is not a good solution. You should create an IAM Role so that the app can access the AWS Resource using STS AssumeRole.
The option that says: Generate long-term credentials using AWS STS and apply the appropriate permissions. Store the credentials in the mobile app, and use them to access S3 is incorrect. You should always grant short-term or temporary credentials for the mobile application. This option recommends creating long-term credentials.
The option that says: Create an IAM user, assign appropriate permissions to it, and generate an access key and a secret key that will be stored in the mobile app and used to access S3 is incorrect. It typically does not create the required IAM Role, but instead, an IAM user.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html
https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q57"></a>

## Q57

A company has an on-premises identity provider (IdP) used for authenticating employees. The Solutions Architect has created a SAML 2.0 based federated identity solution that integrates with the company IdP. This solution is used to authenticate users’ access to the AWS environment. Upon initial testing, the Solutions Architect has been successfully granted access to the AWS environment through the federated identity web portal. However, other test users who tried to authenticate through the federated identity web portal are not given access to the AWS environment.
Which of the following options must be checked to ensure the proper configuration of identity federation? (Select THREE.)

- **A.** Ensure that the ARN of the SAML provider, the ARN of the created IAM role, and SAML assertion from the IdP are all included when the federated identity web portal calls the AWS STS AssumeRoleWithSAML API.
- **B.** Ensure that the IAM policy for that user has “Allow” permissions to use SAML federation.
- **C.** Ensure that the trust policy of the IAM roles created for the federated users or groups has set the SAML provider as principal.
- **D.** Check the company’s IdP to ensure that the users are all part of the default AWSFederatedUser IAM group which is readily available in AWS.
- **E.** Ensure that the appropriate IAM roles are mapped to company users and groups in the IdP’s SAML assertions.
- **F.** Ensure that the resources on the AWS environment Amazon VPC can reach the on-premises IdP using its DNS hostname.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, E (you answered correctly)

🔑 **Key words:** SAML federation works for admin but not other users (Select THREE)

⚠️ **Watch:** ⚠️ Same SAML family you missed in Q31 — AssumeRoleWithSAML, not WebIdentity

🧠 **Rule:** Check AssumeRoleWithSAML params, role trust policy principal = SAML provider, role mapping in assertions.

### TD explanation

AWS supports identity federation with SAML 2.0 (Security Assertion Markup Language 2.0), an open standard that many identity providers (IdPs) use. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without having to create an IAM user for everyone in your organization. By using SAML, you can simplify the process of configuring federation with AWS because you can use the IdP’s service instead of writing custom identity proxy code.
IAM federation supports these use cases:
– Federated access allows a user or application in your organization to call AWS API operations. You use a SAML assertion (as part of the authentication response) that is generated in your organization to get temporary security credentials.
– Web-based single sign-on (SSO) to the AWS Management Console from your organization. Users can sign in to a portal in your organization hosted by a SAML 2.0–compatible IdP, select an option to go to AWS, and be redirected to the console without having to provide additional sign-in information. You can use a third-party SAML IdP to establish SSO access to the console or you can create a custom IdP to enable console access for your external users.

The diagram illustrates the following steps:

The user browses to your organization’s portal and selects the option to go to the AWS Management Console. In your organization, the portal is typically a function of your IdP that handles the exchange of trust between your organization and AWS.
The portal verifies the user’s identity in your organization.
The portal generates a SAML authentication response that includes assertions that identify the user and include attributes about the user. The portal sends this response to the client browser.
The client browser is redirected to the AWS IAM Identity Center endpoint and posts the SAML assertion.
The endpoint requests temporary security credentials on behalf of the user and creates a console sign-in URL that uses those credentials.
AWS sends the sign-in URL back to the client as a redirect.
The client browser is redirected to the AWS Management Console. If the SAML authentication response includes attributes that map to multiple IAM roles, the user is first prompted to select the role for accessing the console.

Before you can use SAML 2.0-based federation, you must configure your organization’s IdP and your AWS account to trust each other. Inside your organization, you must have an IdP that supports SAML 2.0, like Microsoft Active Directory Federation Service (AD FS, part of Windows Server), Shibboleth, or another compatible SAML 2.0 provider. In your organization’s IdP, you define assertions that map users or groups in your organization to the IAM roles. Note that different users and groups in your organization might map to different IAM roles. The exact steps for performing the mapping depend on what IdP you’re using.
The role or roles that you create in IAM define what federated users from your organization are allowed to do in AWS. When you create the trust policy for the role, you specify the SAML provider that you created earlier as the Principal. You can additionally scope the trust policy with a Condition element to allow only users that match certain SAML attributes to access the role.
Hence, the correct answers are:
– Ensure that the trust policy of the IAM roles created for the federated users or groups has set the SAML provider as principal. In IAM, you create one or more IAM roles for the federated users. In the role’s trust policy, you need to set the SAML provider as the principal, which establishes a trust relationship between your organization and AWS.
– Ensure that the ARN of the SAML provider, the ARN of the created IAM role, and SAML assertion from the IdP are all included when the federated identity web portal calls the AWS STS AssumeRoleWithSAML API. These items should all be passed by the client calling the AWS STS AssumeRoleWithSAML API.
– Ensure that the appropriate IAM roles are mapped to company users and groups in the IdP’s SAML assertions. In your organization’s IdP, you should define assertions that map users or groups in your organization to the IAM roles.
The option that says: Ensure that the IAM policy for that user has “Allow” permissions to use SAML federation is incorrect because the test user’s permissions are mapped to IAM roles, so we need to take a look at the IAM role policies and not the individual user IAM permission policies.
The option that says: Check the company’s IdP to ensure that the users are all part of the default AWSFederatedUser IAM group which is readily available in AWS is incorrect because there is no such thing as a default AWSFederatedUser IAM group. You only need to define assertions in your organization’s IdP that map users or groups in your organization to the IAM roles.
The option that says: Ensure that the resources on the AWS environment Amazon VPC can reach the on-premises IdP using its DNS hostname is incorrect as this is not primarily a requirement for the identity federation to work.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html
https://aws.amazon.com/blogs/security/how-to-set-up-federated-single-sign-on-to-aws-using-google-workspace/

Check out these AWS Security and Identity Services Cheat Sheet:
https://tutorialsdojo.com/aws-cheat-sheets-security-identity-services/

</details>

<a id="q72"></a>

## Q72

A company is planning to launch a mobile app for the Department of Transportation that allows government staff to upload the latest photos of ongoing construction works such as bridges, roads culverts, and dams all over the country. The mobile app should send the photos to a web server hosted on an EC2 instance which then adds a watermark to each photo that contains the project details and the date it was taken. The solutions architect must design a solution in which the photos generated by the server will be uploaded to an S3 bucket for durable storage. 
Which of the following solutions is a secure architecture and allows the EC2 instance to upload photos to S3?

- **A.** Set up a service control policy (SCP) with permissions to list and write objects to the S3 bucket. Attach the SCP to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket.
- **B.** Set up an IAM role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket.
- **C.** Set up an IAM user with permissions to list and write objects to the S3 bucket. Launch the instance as the IAM user which will enable the EC2 instance to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket.
- **D.** Set up an IAM service role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** EC2 watermarks photos then uploads to S3 securely

⚠️ **Watch:** ⚠️ Q15: the instance profile alone is enough

🧠 **Rule:** EC2 → S3 access = IAM role; credentials from instance metadata (not userdata).

### TD explanation

This question tests your understanding of IAM, specifically on when to use an IAM Role over an SCP. Since the server is running on an EC2 instance and the application makes requests to S3 to store the photos, the more suitable option to use here is an IAM Role.

In addition, don’t create an IAM user and pass the user’s credentials to the application or embed the credentials in the application. That will create a security risk because if an attacker had unauthorized access to that EC2 instance then the user credentials can easily be acquired and exploited. The better way is to create an IAM role that you can attach to the EC2 instance to give applications running on the instance temporary security credentials which can be used to access other AWS resources such as an S3 bucket. The credentials have the permissions specified in the policies attached to the role.
The option that says: Set up an IAM role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket is correct as it uses an IAM Role and fetches the temporary security credentials from the instance metadata.
The option that says: Set up a service control policy (SCP) with permissions to list and write objects to the S3 bucket. Attach the SCP to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket is incorrect as SCPs simply enable you to restrict, at the account level of granularity, what services and actions the users, groups, and roles in those accounts can do. SCPs don’t grant permissions to any user or role because this is handled through IAM policies.
The option that says: Set up an IAM user with permissions to list and write objects to the S3 bucket. Launch the instance as the IAM user which will enable the EC2 instance to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket is incorrect as an IAM Role is a better option to use instead of an IAM User. Plus, you should always retrieve the temporary security credentials from the instance metadata and not from the user data.
The option that says: Set up an IAM service role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket is incorrect because although it uses an IAM Role, the temporary security credentials should be retrieved from the instance metadata and not from the user data.

References:
https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-service-control-policy/
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-roles

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

Here is a deep dive on IAM Policies:
https://youtu.be/YQsK4MtsELU

</details>

---

# Group B — Edge & data protection (6)

<a id="q6"></a>

## Q6

A company has recently released a new mobile game. With the boost in marketing, the mobile game suddenly became viral. The registration webpage is bombarded with user registrations from around the world. The registration website is hosted on a fleet of Amazon EC2 instances created as an Auto Scaling group. This cluster is behind an Application Load Balancer to balance the user traffic. The website contains static content that is loaded differently depending on the user’s device type. With the sudden increase in user traffic, the fleet of Amazon EC2 instances experienced high CPU usage and users are reporting sluggishness on the website.
Which of the following options should the Solutions Architect implement to improve the website response time?

- **A.** Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Write a Lambda@Edge function to parse the User-Agent HTTP header and serve the appropriate contents based on the user’s device type.
- **B.** Use a Network Load Balancer (NLB) instead of an ALB to distribute the user traffic. Create a dedicated Auto Scaling group for the different device types. Configure the NLB to parse the User-Agent HTTP header to route the users to the appropriate EC2 Auto Scaling groups.
- **C.** Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Configure CloudFront to deliver different contents depending on the user’s User-Agent HTTP header.
- **D.** Create a dedicated Auto Scaling group for the different device types and create separate Application Load Balancers (ALB) for each group. Create an Amazon Route 53 entry to route the users to the appropriate ALB depending on their User-Agent HTTP header.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** viral signups; static content by device type; EC2 CPU high

⚠️ **Watch:** CloudFront can't natively route on full User-Agent logic

🧠 **Rule:** Offload static to S3 + CloudFront; Lambda@Edge to vary content by device.

### TD explanation

Lambda@Edge is an extension of AWS Lambda, a compute service that lets you execute functions that customize the content that CloudFront delivers. You can author Node.js or Python functions in one Region, US-East-1 (N. Virginia), and then execute them in AWS locations globally that are closer to the viewer, without provisioning or managing servers. Lambda@Edge scales automatically, from a few requests per day to thousands per second. Processing requests at AWS locations closer to the viewer instead of on origin servers significantly reduces latency and improves the user experience.

When you associate a CloudFront distribution with a Lambda@Edge function, CloudFront intercepts requests and responses at CloudFront edge locations. You can execute Lambda functions when the following CloudFront events occur:
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
You can configure CloudFront to cache objects based on values in the User-Agent header, but AWS doesn’t recommend it. The User-Agent header has many possible values, and caching based on those values would cause CloudFront to forward significantly more requests to your origin. If you do not configure CloudFront to cache objects based on values in the User-Agent header, CloudFront adds a User-Agent header with the following value before it forwards a request to your origin: User-Agent = Amazon CloudFront.
Therefore, the correct answer is: Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Write a Lambda@Edge function to parse the User-Agent HTTP header and serve the appropriate contents based on the user’s device type. CloudFront will run the Lamda@Edge function for every request to serve the appropriate content to the user. This will lessen the load on the EC2 instances of the Auto Scaling group.
The option that says: Use a Network Load Balancer (NLB) instead of an ALB to distribute the user traffic. Create a dedicated Auto Scaling group for the different device types. Configure the NLB to parse the User-Agent HTTP header to route the users to the appropriate EC2 Auto Scaling groups is incorrect. An NLB operates at Layer 4 of the OSI network model so it can’t read the User-Agent HTTP header which is present at Layer 7.
The option that says: Create a dedicated Auto Scaling group for the different device types and create separate Application Load Balancers (ALB) for each group. Create an Amazon Route 53 entry to route the users to the appropriate ALB depending on their User-Agent HTTP header is incorrect. This is not possible because Amazon Route 53 does not have a way to direct users based on HTTP headers.
The option that says: Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Configure CloudFront to deliver different contents depending on the user’s User-Agent HTTP header is incorrect. This may be possible as you can configure CloudFront to cache objects based on values in the Date and User-Agent headers, but AWS doesn’t recommend it. These headers have many possible values, and caching based on their values would cause CloudFront to forward significantly more requests to your origin.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-user-agent-header

Check out these AWS Lambda and Amazon CloudFront Cheat Sheets:
https://tutorialsdojo.com/aws-lambda/
https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q42"></a>

## Q42

A leading commercial bank has a hybrid cloud architecture and is using a Volume Gateway under the AWS Storage Gateway service to store their data via the Internet Small Computer Systems Interface (ISCSI). The security team has detected a series of replay attacks to your network, which is basically a form of network attack in which a valid data transmission is maliciously or fraudulently repeated or delayed. After their investigation, they detected that the originator of the attack is trying to intercept the data with an intention to re-transmit it, which is possibly part of a masquerade attack by IP packet substitution. 
As a Solutions Architect of the bank, how can you secure your AWS Storage Gateway from these types of attacks?

- **A.** Replace ISCSI with more secure protocols like Common Internet File System (CIFS) Protocol or Server Message Block (SMB).
- **B.** Replace the current ISCSI Block Interface with an ISCSI Virtual Tape Library Interface.
- **C.** Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate NFS connections and safeguard your network from replay attacks.
- **D.** Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSI and initiator connections.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** replay attacks on Volume Gateway iSCSI

⚠️ **Watch:** CHAP for NFS is wrong — CHAP applies to iSCSI

🧠 **Rule:** Secure iSCSI targets → CHAP authentication.

### TD explanation

In AWS Storage Gateway, your iSCSI initiators connect to your volumes as iSCSI targets. Storage Gateway uses Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSI and initiator connections. CHAP provides protection against playback attacks by requiring authentication to access storage volume targets. For each volume target, you can define one or more CHAP credentials. You can view and edit these credentials for the different initiators in the Configure CHAP credentials dialog box.

Therefore the correct answer is: Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSl and initiator connections.
The option that says: Replace lSCSl with more secure protocols like Common Internet File System (CIFS) Protocol or Server Message Block (SMB) is incorrect. Replacing ISCSI with CIFS and SMB would be irrelevant since these two do not provide the required security mechanism in the scenario. It is best to use Challenge-Handshake Authentication Protocol (CHAP) instead.
The option that says: Replace the current lSCSl Block Interface with an lSCSl Virtual Tape Library Interface is incorrect. ISCSI Virtual Tape Library Interface is primarily used for Tape Gateways and not for Volume Gateways. It is better to use Challenge-Handshake Authentication Protocol (CHAP) instead.
The option that says: Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate NFS connections and safeguard your network from replay attacks is incorrect. CHAP is primarily used to authenticate iSCSI and not NFS.

References:
https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedConfigureChap.html
https://docs.aws.amazon.com/storagegateway/latest/vgw/initiator-connection-common.html

Check out this AWS Storage Gateway Cheat Sheet:
https://tutorialsdojo.com/aws-storage-gateway/

</details>

<a id="q53"></a>

## Q53

A finance company plans to launch a new website to let users view tutorials promoting proper use of the mobile app. The website contains static media files stored in a private Amazon S3 bucket, while dynamic content is hosted on an AWS Fargate cluster. The Fargate tasks are accepting traffic behind an Application Load Balancer (ALB). To improve the user experience, static and dynamic content are served via an Amazon CloudFront distribution. An Amazon Route 53 Alias record has already been created to point the website URL to the CloudFront distribution. The company wants to ensure that access to both static and dynamic content is handled exclusively through CloudFront.
Which of the following options should the Solutions Architect implement to meet this requirement? (Select TWO.)

- **A.** Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution.
- **B.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer.
- **C.** Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC.
- **D.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution.
- **E.** Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C (you answered correctly)

🔑 **Key words:** static (S3) + dynamic (ALB) only via CloudFront (Select TWO)

⚠️ **Watch:** ⚠️ Q44: OAC enforces the CloudFront path, not a specific client

🧠 **Rule:** S3 origin → OAC; ALB origin → CloudFront custom header checked by WAF on the ALB.

### TD explanation

AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the values of query strings or the IP addresses that requests originate from, CloudFront responds to requests either with the requested content or with an HTTP status code 403(Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked.
After you create an AWS WAF web access control list (web ACL), create or update a web distribution to associate the distribution with the web ACL. You can associate as many CloudFront distributions as you want with the same web ACL or with different web ACLs.
On Amazon CloudFront, you can control user access to your private content in two ways:

Restrict access to files in CloudFront caches.
Restrict access to files in your origin by doing one of the following:

– Set up an origin access control (OAC) for your Amazon S3 bucket.
– Configure custom headers for a private HTTP server (a custom origin).
CloudFront provides two ways to send authenticated requests to an Amazon S3 origin: origin access control (OAC) and origin access identity (OAI). OAC helps you secure your origins, such as Amazon S3.
AWS recommends that you use OAC instead because it supports the following features:

All Amazon S3 buckets in all AWS Regions, including opt-in Regions launched after December 2022
Amazon S3 server-side encryption with AWS KMS (SSE-KMS)
Dynamic requests (PUT and DELETE) to Amazon S3

Origin Access Identity (OAI) is considered a legacy, not-recommended mechanism due to its functional limitations.
You can secure the content in your Amazon S3 bucket so that users can access it through CloudFront, but cannot access it directly by using Amazon S3 URLs. This prevents someone from bypassing CloudFront and using the Amazon S3 URL to get content that you want to restrict access to. To require that users access your content through CloudFront URLs, you do the following tasks:

Create an origin access control and associate it with your CloudFront distribution.
Give the origin access control permission to read the files in your bucket.
Remove permission for anyone else to use Amazon S3 URLs to read the files.

If you use a custom origin, you can optionally set up custom headers to restrict access. For CloudFront to get your files from a custom origin, the files must be accessible by CloudFront using a standard HTTP (or HTTPS) request. But by using custom headers, you can further restrict access to your content so that users can access it only through CloudFront, not directly. This step isn’t required to use signed URLs, but it is recommended. To require that users access content through CloudFront, change the following settings in your CloudFront distributions:
Origin Custom Headers – Configure CloudFront to forward custom headers to your origin.
Viewer Protocol Policy – Configure your distribution to require viewers to use HTTPS to access CloudFront.
Origin Protocol Policy – Configure your distribution to require CloudFront to use the same protocol as viewers to forward requests to the origin.
Hence, the correct answers are:
– Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer. After you create an AWS WAF web access control list (web ACL), create or update a web distribution to associate the distribution with the ALB. Associating the Web ACL with the ALB ensures that only requests from CloudFront will reach the ALB. Any request going to the ALB without the custom header will be denied by WAF.
– Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC. OAC enables CloudFront to use SigV4-signed requests to access private S3 content, and the S3 bucket policy can explicitly allow access only from CloudFront via that OAC. This prevents users from retrieving objects directly from S3 and forces access through CloudFront.
The option that says: Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution is incorrect. If any new requests are going to CloudFront, they won’t have the custom header initially, so AWS WAF may block the request immediately. This could deny any new connections to CloudFront. Therefore, you need to associate the web ACL to the ALB, which is after CloudFront adds the custom header.
The option that says: Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets is incorrect. This will limit all resources inside the ALB subnets to accept only traffic from the CloudFront distribution. However, there are no fixed IP addresses for Amazon CloudFront, and if you manually add AWS IP addresses, you will have to update the NACL as AWS updates its IP pool.
The option that says: Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution is incorrect. You can’t directly configure a bucket ACL to allow access only from Amazon CloudFront. You typically need an origin access control (OAC) for this setup.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html
https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#forward-custom-headers-restrict-access

Check out these Amazon CloudFront and AWS WAF Cheat Sheets:
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/aws-waf/

</details>

<a id="q54"></a>

## Q54

A health insurance company has recently adopted a hybrid cloud architecture which connects their on-premises network and their cloud infrastructure in AWS. They have an ELB which has a set of EC2 instances behind them. As the cloud engineer of the company, your manager instructed you to ensure that the SSL key used to encrypt data is always kept secure at all times. In addition, the application logs should only be decrypted by a handful of key users.
In this scenario, which of the following meets all of the requirements?

- **A.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
- **B.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic. 3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
- **C.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot. 3. Persist your application server logs to a private S3 bucket using SSE.
- **D.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to a private S3 bucket using SSE.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** SSL key always secure; logs decrypted by few users

⚠️ **Watch:** Ephemeral volumes lose logs

🧠 **Rule:** Key never leaves → CloudHSM with TCP LB; logs → private S3 with SSE.

### TD explanation

AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. With CloudHSM, you can manage your own encryption keys using FIPS 140-2 Level 3 validated HSMs. CloudHSM offers you the flexibility to integrate with your applications using industry-standard APIs, such as PKCS#11, Java Cryptography Extensions (JCE), and Microsoft CryptoNG (CNG) libraries.
You can use AWS CloudHSM to offload SSL/TLS processing for your web servers. Using CloudHSM for this processing reduces the burden on your web server and provides extra security by storing your web server’s private key in CloudHSM. Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are used to confirm the identity of web servers and establish secure HTTPS connections over the Internet.

AWS CloudHSM automates time-consuming HSM administrative tasks for you, such as hardware provisioning, software patching, high availability, and backups. You can scale your HSM capacity quickly by adding and removing HSMs from your cluster on-demand. AWS CloudHSM automatically load balances requests and securely duplicates keys stored in any HSM to all of the other HSMs in the cluster.
CloudHSM provides a better and more secure way of offloading the SSL processing for the web servers and ensures the application logs are durably and securely stored.
In this scenario, the following option is the best choice because it uses CloudHSM and the application server logs are persisted in an S3 bucket with a Server Side Encryption (SSE):
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Configure the ELB to perform TCP load balancing.
3. Use an AWS CloudHSM instance to perform the SSL transactions.
4. Persist your application server logs to a private S3 bucket using SSE.
The following sets of options are incorrect because the ephemeral volume is just temporary storage and hence, not a suitable option for durable storage:
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic.
3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
as well as this option:
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Configure the ELB to perform TCP load balancing.
3. Use an AWS CloudHSM instance to perform the SSL transactions.
4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
The following option is incorrect because you should never store sensitive private keys in S3:
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot.
3. Persist your application server logs to a private S3 bucket using SSE.

References:
https://aws.amazon.com/cloudhsm/
https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-overview.html

</details>

<a id="q65"></a>

## Q65

A company runs a cryptocurrency analytics website and uses a CloudFront distribution with a custom domain name (tutorialsdojo.com) to speed up the loading time of the site. Since the data being distributed are quite confidential, the management instructed the solutions architect to require HTTPS communication between the viewers (web visitors) and the CloudFront distribution. Additionally, it is required to improve the performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers. 
Which of the following are the recommended actions to accomplish the above requirement? (Select TWO.)

- **A.** Configure the CloudFront origin to add a Cache-Control max-age directive to your objects and specify the longest practical value for max-age.
- **B.** Use an SSL/TLS certificate provided by AWS Certificate Manager (ACM).
- **C.** Import an SSL/TLS certificate from a third-party certificate authority into a private S3 bucket with versioning and MFA enabled.
- **D.** Associate your CloudFront web distribution with Lambda@Edge which provides automatic scalability from a few requests per day to thousands of requests per second.
- **E.** Integrate your CloudFront web distribution with Amazon OpenSearch to cache recent requests and improve the performance of your origin servers. Use Kibana to visualize the cache hit-ratio graph in real time.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B (you answered correctly)

🔑 **Key words:** HTTPS viewer↔CloudFront with custom domain; higher cache hit ratio (Select TWO)

⚠️ **Watch:** ⚠️ Q1: public ACM certs are free; import third-party certs into ACM, not S3

🧠 **Rule:** ACM certificate + long Cache-Control max-age.

### TD explanation

You can configure one or more cache behaviors in your CloudFront distribution to require HTTPS for communication between viewers and CloudFront. You also can configure one or more cache behaviors to allow both HTTP and HTTPS so that CloudFront requires HTTPS for some objects but not for others. The configuration steps depend on which domain name you’re using in object URLs:
– If you’re using the domain name that CloudFront assigned to your distribution, such as d111111abcdef8.cloudfront.net, you change the Viewer Protocol Policy setting for one or more cache behaviors to require HTTPS communication. In that configuration, CloudFront provides the SSL/TLS certificate.
– If you’re using your own domain name, such as tutorialsdojo.com, you need to change several CloudFront settings. You also need to use an SSL/TLS certificate provided by AWS Certificate Manager (ACM), or import a certificate from a third-party certificate authority into ACM or the IAM certificate store.

You can improve performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers for content; that is, by improving the cache hit ratio for your distribution. To increase your cache hit ratio, you can configure your origin to add a Cache-Control max-age directive to your objects and specify the longest practical value for max-age. The shorter the cache duration, the more frequently CloudFront forwards another request to your origin to determine whether the object has changed and, if so, to get the latest version.
Therefore, the correct answers are:
-Use an SSL/TLS certificate provided by AWS Certificate Manager (ACM)
-Configure the CloudFront origin to add a Cache-Control max-age directive to your objects and specifying the longest practical value for max-age.
The option that says: Associate your CloudFront web distribution with Lambda@Edge which provides automatic scalability from a few requests per day to thousands of requests per second is incorrect because Lambda@Edge is an extension of AWS Lambda which lets you execute functions that customize the content that CloudFront delivers. This feature does not improve the cache hit ratio of your CloudFront distribution.
The option that says: Integrate your CloudFront web distribution with Amazon OpenSearch to cache recent requests and improve the performance of your origin servers. Use Kibana to visualize the cache hit-ratio graph in real time is incorrect. Amazon OpenSearch service is used to perform interactive log analytics, real-time application monitoring, and more. This service will not improve the cache hit ratio of your CloudFront distribution. The built-in Kibana support only provides a way to get faster and better insights into your data and thus, not relevant to this scenario.
The option that says: Import an SSL/TLS certificate from a third-party certificate authority into a private S3 bucket with versioning and MFA enabled is incorrect. For an SSL certificate, whether it is public or private, is not recommended to store it on an Amazon S3 bucket.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/aws-certificate-manager/

</details>

<a id="q69"></a>

## Q69

A company stores several terabytes of data on an Amazon S3 bucket. The data will be made available to respective partner companies, however, the management doesn’t want the partner companies to access the files directly from Amazon S3 URLs. The solutions architect has been asked to ensure that all confidential files shared via Amazon S3 should only be accessible through CloudFront. 
Which of the following options could satisfy this requirement?

- **A.** Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission.
- **B.** Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access.
- **C.** Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront.
- **D.** Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN).

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** files only accessible through CloudFront

⚠️ **Watch:** Distribution ID is not a valid S3 principal

🧠 **Rule:** S3 origin locked to CloudFront → Origin Access Control + bucket policy.

### TD explanation

To restrict access to content that you serve from Amazon S3 buckets, you create CloudFront signed URLs or signed cookies to limit access to files in your Amazon S3 bucket, and then you create a special CloudFront user called an origin access control (OAC) and associate it with your distribution. Then you configure permissions so that CloudFront can use the OAC to access and serve files to your users, but users can’t use a direct URL to the S3 bucket to access a file there. Taking these steps helps you maintain secure access to the files that you serve through CloudFront.
In general, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you can either allow everyone to have access to the files there, or you can restrict access. If you limit access by using, for example, CloudFront signed URLs or signed cookies, you also won’t want people to be able to view files by simply using the direct URL for the file. Instead, you want them to only access the files by using the CloudFront URL, so your protections work.

Typically, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you grant everyone permission to read the objects in your bucket. This allows anyone to access your objects either through CloudFront or using the Amazon S3 URL. CloudFront doesn’t expose Amazon S3 URLs, but your users might have those URLs if your application serves any objects directly from Amazon S3 or if anyone gives out direct links to specific objects in Amazon S3.
Therefore, the correct answer is: Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission. It gives CloudFront exclusive access to the S3 bucket and prevents other users from accessing the public content of S3 directly via S3 URL.
The option that says: Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN) is incorrect. Creating a bucket policy is unnecessary and it does not prevent other users from accessing the public content of S3 directly via S3 URL.
The option that says: Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront is incorrect. This does not give CloudFront exclusive access to the S3 bucket.
The option that says: Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access is incorrect. You do not need to create any individual policies for each bucket.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amazon-s3/

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

S3 Pre-signed URLs vs CloudFront Signed URLs vs Origin Access Control (OAC)
https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services/

</details>

---

# Group C — DR / HA / database resilience (7)

<a id="q10"></a>

## Q10

A leading media company is building a collaborative news website that is expected to have over 5 million readers per month globally. Each article contains a cover image and has at least 200 words. Based on the trend of their other websites, the new articles are highly browsed in the first 2 months and the authors tend to frequently update the articles on the first month after its publication. The readership is also expected to drop on the 3rd month and the articles are usually rarely accessed after a year. The readers are also leaving a lot of comments within the first 3 months of publishing. 
In this scenario, which of the following items can you use to build a durable, highly available, and scalable architecture for the news website? (Select TWO.)

- **A.** Use Lambda with Auto-Healing enabled.
- **B.** Use Amazon RDS Multi-AZ deployments with Read Replicas. Use S3 to store the static data such as the cover images and other media.
- **C.** Launch an RDS Oracle Real Application Clusters (RAC) with Read Replicas.
- **D.** Use CloudFront as a Content Delivery Network to load the articles much faster anywhere in the globe.
- **E.** Use EBS Volumes in RAID 0 configuration to store the static data such as the cover images and other media.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D (you answered correctly)

🔑 **Key words:** 5M readers; durable, HA, scalable news site (Select TWO)

⚠️ **Watch:** RAID 0 has no redundancy

🧠 **Rule:** RDS Multi-AZ + read replicas, S3 for media, CloudFront.

### TD explanation

In this scenario, the main objective is to provide a durable, highly-available and scalable architecture for the website. You can use CloudFront as a CDN, then Amazon RDS with Multi-AZ deployments and Read Replicas to provide scalability and high-availability for the millions of incoming traffic every month. Lastly, you can use an S3 bucket to durably store the images and other static media content of the website.

Therefore, the correct answer is: Use CloudFront as a Content Delivery Network to load the articles much faster anywhere in the globe and Use Amazon RDS Multi-AZ deployments with Read Replicas. Use S3 to store the static data such as the cover images and other media.
The option that says: Launch an RDS Oracle Real Application Clusters (RAC) with Read Replicas is incorrect because Oracle RAC is not supported in RDS.
The option that says: Use Lambda with Auto-Healing enabled is incorrect. AWS Lambda is serverless and it does not have Auto-Healing option since functions are event-driven.
The option that says: Use EBS Volumes in RAID 0 configuration to store the static data such as the cover images and other media is incorrect because EBS Volumes are not as durable and not as scalable compared with S3, even with a RAID 1 (mirroring) configuration.

References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
https://aws.amazon.com/s3/

Check out these Amazon RDS and Amazon S3 Cheat Sheets:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q11"></a>

## Q11

A company hosts its main web application on the AWS cloud which is composed of web servers and database servers. To ensure high availability, the web servers are deployed on an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones with an Application Load Balancer in front. For the database, it is deployed on a Multi-Availability Zone configuration in Amazon RDS. During the RDS maintenance window, the operating system of the primary DB instance undergoes software patching that triggers the failover process.
What would happen to the database during failover?

- **A.** A new DB instance will be created and immediately replace the primary database.
- **B.** The RDS DB instance will automatically reboot.
- **C.** The IP address of the primary DB instance is switched to the standby DB instance.
- **D.** The canonical name record (CNAME) is changed from the primary database to standby database.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** what happens during RDS Multi-AZ failover

⚠️ **Watch:** IP address does not move

🧠 **Rule:** Multi-AZ failover flips the DB endpoint CNAME to the standby.

### TD explanation

Amazon RDS Multi-AZ deployments provide enhanced availability and durability for Database (DB) Instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of Amazon Aurora), so that you can resume database operations as soon as the failover is complete.

When automatic failover occurs, your application can remain unaware of what’s happening behind the scenes. The CNAME record for your DB instance will be altered to point to the newly promoted standby.
Therefore, the correct answer is: The canonical name record (CNAME) is changed from the primary database to standby database.
The option that says: The IP address of the primary DB instance is switched to the standby DB instance is incorrect because the Canonical Name Record (CNAME) will be changed and not the IP address.
The option that says: The RDS DB instance will automatically reboot is incorrect because the RDS instance will not automatically reboot.
The option that says: A new DB instance will be created and immediately replace the primary database is incorrect because there is no new DB instance that will be created.

References:
https://aws.amazon.com/rds/details/multi-az/
https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-deployment/

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q13"></a>

## Q13

An enterprise software company has just recently started using AWS as its cloud infrastructure. The company is building an enterprise proprietary issue tracking system which would be accessed by its customers worldwide. Hence, the CTO carefully instructed the team to ensure that the architecture of the issue tracking system is both scalable and highly available to avoid any complaints from the clients. It is expected that the application will have steady-state usage, and the database would be used for online transaction processing (OLTP). The team recently used the AWS Well-Architected Tool to review its architecture, which highlighted the need for a highly available and fault-tolerant design.
Which of the following would be the best architecture setup to satisfy the above requirement?

- **A.** Launch an Auto Scaling group of Spot Amazon EC2 instances with an ELB in front to handle the load balancing. Leverage on Amazon CloudFront in distributing your static content and an Amazon RDS instance with Read Replicas.
- **B.** Use an AWS CloudFormation template to launch an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones, which are all connected via an ELB to handle the load balancing. Leverage Amazon CloudFront for distributing your static content and an Amazon RDS instance with a Multi-AZ deployment configuration.
- **C.** Use a Dedicated Amazon EC2 instance as the application server and Amazon Redshift as a petabyte-scale data warehouse service. Use Amazon ElastiCache for in-memory data caching for your database to improve performance.
- **D.** Use multiple On-Demand Amazon EC2 instances to host the application and a highly scalable Amazon DynamoDB for the database. Use Amazon ElastiCache for in-memory data caching for your database to improve performance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** issue tracker; steady state; OLTP; HA + fault tolerant

⚠️ **Watch:** Spot for a steady-state HA tier is risky

🧠 **Rule:** Multi-AZ ASG + ELB + CloudFront + RDS Multi-AZ.

### TD explanation

It is recommended to use a CloudFormation template to launch your architecture in AWS. An Auto Scaling group of EC2 instances across multiple Availability Zones with an ELB in front is a highly available and scalable architecture. In addition, leveraging on CloudFront in distributing your static content improves the load times of the system. Finally, an RDS instance with Multi-AZ deployments configuration can ensure the availability of your database in case one instance goes down.

Therefore, the correct answer is: Use an AWS CloudFormation template to launch an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones, which are all connected via an ELB to handle the load balancing. Leverage Amazon CloudFront for distributing your static content and an Amazon RDS instance with a Multi-AZ deployment configuration. This offers high availability and scalability for the application.
The option that says: Use a Dedicated Amazon EC2 instance as the application server and Amazon Redshift as a petabyte-scale data warehouse service. Use Amazon ElastiCache for in-memory data caching for your database to improve performance is incorrect. Using Dedicated EC2 instances without Auto Scaling is not a scalable nor a highly available architecture. In addition, RedShift is not applicable to OLTP but rather with OLAP.
The option that says: Launch an Auto Scaling group of Spot Amazon EC2 instances with an ELB in front to handle the load balancing. Leverage on Amazon CloudFront in distributing your static content and an Amazon RDS instance with Read Replicas is incorrect. Spot EC2 instances are just not suitable for steady state usage and Read Replicas only provide limited availability compared to Multi-AZ Deployments.
The option that says: Use multiple On-Demand Amazon EC2 instances to host the application and a highly scalable Amazon DynamoDB for the database. Use Amazon ElastiCache for in-memory data caching for your database to improve performance is incorrect. This does not use Auto Scaling and is not deployed across multiple Availability Zones.

References:
https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf
https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-best-practices.html
https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/architecting-for-high-availability.html

Check out this Amazon EC2 Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q29"></a>

## Q29

A company runs a popular photo-sharing site hosted on the AWS cloud. There are user complaints about the frequent downtime of the site considering the hefty price for using their service. The company is using a MySQL RDS instance to record user details and other data analytics. A standard S3 storage class bucket is used to store the photos and user metadata, which are frequently accessed only in the first month. The website is also capable of immediately retrieving the images no matter how long they were stored. The RDS instance is always affected and sometimes goes down when there is a problem in the Availability Zone. The solutions architect was tasked to analyze the current architecture and to solve the user complaints about the website. In addition, the solutions architect should also implement a system that automatically discovers, classifies, and protects personally identifiable information (PII) data in the Amazon S3 bucket. 
Which of the following options offers the BEST solution for this scenario?

- **A.** Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Amazon S3 Glacier Deep Archive after a month. Re-configure the existing database to use RDS Multi-AZ Deployments.
- **B.** Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket.  Replace the S3 Standard bucket with an Infrequent Access storage class. Re-configure the existing database to use RDS Read Replicas.
- **C.** Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Infrequent Access storage class after a month. Re-configure the existing database to use RDS Multi-AZ Deployments.
- **D.** Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 bucket with EBS Volumes and use Redshift instead of RDS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** RDS down on AZ issue; photos retrievable immediately; PII discovery

⚠️ **Watch:** Inspector ≠ PII; Glacier Deep Archive isn't immediate

🧠 **Rule:** Macie for PII; S3 IA after 1 month; RDS Multi-AZ for AZ failure.

### TD explanation

Amazon Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. Amazon Macie recognizes sensitive data such as personally identifiable information (PII) or intellectual property and provides you with dashboards and alerts that give visibility into how this data is being accessed or moved. The fully managed service continuously monitors data access activity for anomalies and generates detailed alerts when it detects the risk of unauthorized access or inadvertent data leaks. Today, Amazon Macie is available to protect data stored in Amazon S3, with support for additional AWS data stores soon.

In this scenario, the best way to solve the issue is to: Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Infrequent Access storage class after a month. Re-configure the existing database to use RDS Multi-AZ Deployments. Keep in mind that the website should be able to immediately retrieve the images no matter how long they were stored. This means that you should not archive the images.
The option that says: Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 bucket with EBS Volumes and use Redshift instead of RDS is incorrect because EBS Volumes are not as scalable as S3 and Redshift is not a suitable storage option as it is mainly used as a petabyte-scale data warehouse service.
The option that says: Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Amazon S3 Glacier Deep Archive after a month. Re-configure the existing database to use RDS Multi-AZ Deployments is incorrect because although it is right to use Amazon RDS Multi-AZ deployments configuration, the use of Glacier Deep Archive is not preferred for this scenario. Take note that Glacier is primarily used for archiving and the retrieval times are much slower compared to S3. Implementing this solution means that the users will have to wait a long time to retrieve their photos. In addition, Amazon Inspector is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS, especially in Amazon EC2 instances. You have to use Amazon Macie instead.
The option that says: Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 Standard bucket with an Infrequent Access storage class. Re-configure the existing database to use RDS Read Replicas is incorrect because although it is right to use Infrequent Access storage class, the use of Read Replica is not suitable for this scenario. Although it may improve availability, you are only limited to use read operations when you use Read Replicas. This means when the primary database is down, the Read Replica would not be available to register new users since read operations are only allowed. Moreover, you have to use Amazon Macie and not Amazon Inspector, since this is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS.

References:
https://aws.amazon.com/s3/storage-classes/
https://aws.amazon.com/macie/
https://aws.amazon.com/macie/details/

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

Check out this Amazon Macie Cheat Sheet:
https://tutorialsdojo.com/amazon-macie/

</details>

<a id="q46"></a>

## Q46

A company located on the west coast of North America plans to release a new online service for its customers. The company already created a new VPC in the us-west-1 region where they will launch the Amazon EC2 instances that will host the web application. The application must be highly-available and must dynamically scale based on user traffic. In addition, the company wants to have a disaster recovery site in the us-east-1 region that will act as a passive backup of the running application.
Which of the following options should the Solutions Architect implement in order to achieve the requirements?

- **A.** Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB.
- **B.** Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create separate record entries for each region’s ALB on Amazon Route 53 and enable health checks to ensure high-availability for both regions.
- **C.** Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create record entries in Amazon Route 53 pointing to the ALBs with health check enabled and a failover routing policy.
- **D.** Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) that spans multiple Availability Zones (AZs) on both VPCs. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB. Create an Alias record entry in Amazon Route 53 that points to the DNS name of the ALB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** us-east-1 passive DR site

⚠️ **Watch:** An ALB can't span Regions

🧠 **Rule:** Separate ALB+ASG per Region + Route 53 failover routing.

### TD explanation

On Amazon Route 53, after you create a hosted zone for your domain, such as tutorialsdojo.com, you create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain. You can create a record that points to the DNS name of your Application Load Balancer on AWS.
When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:

Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.
Failover routing policy – Use when you want to configure active-passive failover.
Geolocation routing policy – Use when you want to route traffic based on the location of your users.
Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
Latency routing policy – Use when you have resources in multiple AWS Regions, and you want to route traffic to the region that provides the best latency.
Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify.

You can use Route 53 health checks to configure active-active and active-passive failover configurations. You configure active-active failover using any routing policy (or combination of routing policies) other than failover, and you configure active-passive failover using the failover routing policy.

Use an active-passive failover configuration when you want a primary resource or group of resources to be available the majority of the time, and you want a secondary resource or group of resources to be on standby in case all the primary resources become unavailable. When responding to queries, Route 53 includes only the “healthy primary” resources. If all the primary resources are unhealthy, Route 53 begins to include only the healthy secondary resources in response to DNS queries.
This way, you can create a failover routing policy that will direct traffic to the backup region when your primary region fails.
Amazon EC2 Auto Scaling integrates with Elastic Load Balancing to enable you to insert one or more Application Load Balancer, Network Load Balancer, or Gateway Load Balancer with multiple target groups in front of your Auto Scaling group.
Creating an Application Load Balancer on each region with an Auto Scaling group that spans multiple Availability Zones ensures that your application will be highly available and will scale based on the user traffic.
Therefore, the correct answer is: Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create record entries in Amazon Route 53 pointing to the ALBs with health check enabled and a failover routing policy.
The option that says: Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB is incorrect because an Auto Scaling group cannot span AZs on multiple regions, and the Application Load Balancer cannot serve traffic to EC2 instances on a different region even with Inter-Region VPC peering.
The option that says: Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) that spans multiple Availability Zones (AZs) on both VPCs. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB. Create an Alias record entry in Amazon Route 53 that points to the DNS name of the ALB is incorrect because an Application Load Balancer cannot span to multiple regions, only multiple AZs on the same region. An Auto Scaling group also cannot span multiple regions as it can only deploy EC2 instances in one region.
The option that says: Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create separate record entries for each region’s ALB on Amazon Route 53 and enable health checks to ensure high-availability for both regions is incorrect. Although this setup is possible, it does not mention the routing policy to be used on Amazon Route 53. The question requires that the second region acts as a passive backup, which means only the main region receives all the traffic so you need to specifically use a failover routing policy in Amazon Route 53.

References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html

Check out the Amazon Route 53 Cheat Sheet:
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q48"></a>

## Q48

A hospital chain in London uses an online central hub for its doctors and nurses. The application interacts with millions of requests per day to fetch various medical data of their patients. The system is composed of a web tier, an application tier, and a database tier that receives large and unpredictable traffic demands. The Solutions Architect must ensure that this infrastructure is highly-available and scalable enough to handle web traffic fluctuations automatically. 
Which of the following options should the solutions architect implement to meet the above requirements?

- **A.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas.
- **B.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **C.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **D.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** unpredictable traffic; HA and auto scaling all tiers

⚠️ **Watch:** Stateful instances break scaling

🧠 **Rule:** Stateless tiers + ElastiCache for state + RDS Multi-AZ with read replicas.

### TD explanation

When users or services interact with an application, they will often perform a series of interactions that form a session. A session is unique data for users that persists between requests while they use the application. A stateless application is an application that does not need knowledge of previous interactions and does not store session information.

For example, an application that, given the same input, provides the same response to any end user, is a stateless application. Stateless applications can scale horizontally because any of the available compute resources (such as EC2 instances and AWS Lambda functions) can service any request. Without stored session data, you can simply add more compute resources as needed. When that capacity is no longer required, you can safely terminate those individual resources, after running tasks have been drained. Those resources do not need to be aware of the presence of their peers—all that is required is a way to distribute the workload to them.
In this scenario, the best option is to use a combination of Amazon ElastiCache Serverless, Cloudwatch, and RDS Read Replica.
Therefore, the correct answer is: Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled. It uses stateless instances. The web server uses ElastiCache Serverless for read operations and relies on CloudWatch for monitoring traffic fluctuations. When variations in traffic occur, CloudWatch notifies the autoscaling group to perform scale-in or scale-out actions accordingly. ElastiCache Serverless is a robust cache solution that ensures high availability by automatically replicating data across multiple Availability Zones. Furthermore, it leverages read replicas for RDS to efficiently handle read-heavy workloads and utilizes Multi-AZ configurations to ensure high availability.
The option that says: Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled is incorrect because it uses stateful instances. It also does not use any caching mechanism for web and application tiers, and multi-AZ RDS does not improve read performance.
The option that says: Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas is incorrect because it uses stateful instances and it does not use any caching mechanism for web and application tiers.
The option that says: Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled. is incorrect because multi-AZ RDS only improves Availability, not read performance.

References:
https://aws.amazon.com/elasticache/
https://aws.amazon.com/rds/details/read-replicas/
https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/amazon-elasticache/
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q63"></a>

## Q63

A company hosts a stateful licensing application on an Amazon EC2 instance.
The application is tied to the instance’s existing network configuration, and client systems must continue connecting to the same IP address after recovery. The company wants the instance to recover automatically when the underlying AWS hardware fails.
Which solution will meet the given requirements?

- **A.** Configure an Amazon CloudWatch alarm to invoke an AWS Lambda function that runs the aws ec2 reboot-instances command whenever the EC2 instance reports a system status check failure.
- **B.** Associate an Elastic IP address with the EC2 instance and configure an Amazon CloudWatch alarm to stop and start the instance after a system status check failure.
- **C.** Configure an Amazon CloudWatch alarm that monitors the StatusCheckFailed_System metric and triggers the EC2 instance recovery action.
- **D.** Use AWS Systems Manager Automation to patch the EC2 instance when the system status check fails.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** keep same IP after hardware failure; auto recovery

⚠️ **Watch:** Stop/start may change host and private IP behavior; reboot doesn't move hosts

🧠 **Rule:** StatusCheckFailed_System alarm → EC2 recover action (keeps IPs, metadata).

### TD explanation

If AWS detects that an instance is unavailable due to an underlying hardware or software issue, CloudWatch action-based recovery can automatically restore the instance’s availability by migrating it from the affected host to a different host.

You can configure CloudWatch action-based recovery to add recovery actions to Amazon CloudWatch alarms. CloudWatch action-based recovery works with the StatusCheckFailed_System metric. CloudWatch action-based recovery provides to-the-minute recovery response time granularity and Amazon Simple Notification Service (Amazon SNS) notifications of recovery actions and outcomes.

These configuration options enable quicker recovery attempts and provide more precise control over how the system responds to status check failures, compared to simplified automatic recovery.
Hence, the correct answer is: Configure an Amazon CloudWatch alarm that monitors the StatusCheckFailed_System metric and triggers the EC2 instance recovery action. The recovery action automatically moves the instance to healthy hardware while preserving the instance ID, private IP, and Elastic IP. This ensures the licensing application continues to use the same network configuration, and client systems can reconnect seamlessly.
The option that says: Associate an Elastic IP address with the EC2 instance and configure an Amazon CloudWatch alarm to stop and start the instance after a system status check failure is incorrect because stopping and starting the instance will launch it on new hardware, but this disrupts the ephemeral state and is not the intended automatic recovery mechanism. While the Elastic IP ensures the same public IP, this approach is manual and less reliable compared to the native recovery action.
The option that says: Use AWS Systems Manager Automation to patch the EC2 instance when the system status check fails is incorrect because patching typically addresses software or OS-level issues, not hardware failures. A system status check failure indicates underlying AWS hardware problems, which patching cannot resolve.
The option that says: Configure an Amazon CloudWatch alarm to invoke an AWS Lambda function that runs the aws ec2 reboot-instances command whenever the EC2 instance reports a system status check failure is incorrect because rebooting the instance only restarts it on the same faulty hardware. This does not resolve system-level failures and does not guarantee recovery.

References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cloudwatch-recovery.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html

Check out these Amazon EC2 and Amazon CloudWatch Cheat Sheets:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/
https://tutorialsdojo.com/amazon-cloudwatch/

</details>

---

# Group D — Networking (5)

<a id="q39"></a>

## Q39

A company is using AWS Managed Active Directory Service to host the company AD in the AWS Cloud with a custom AD domain name private.tutorialsdojo.com. A pair of domain controllers are launched with the default configuration inside the VPC. A VPC interface endpoint was also created for the Amazon Kinesis using AWS Private Link to allow instances to connect to Kinesis service endpoints from inside the VPC. The solutions architect launched several EC2 instances in the VPC, however, the instances were not able to resolve the company’s custom AD domain name.
Which of the following steps should the Solutions Architect implement to allow the instances to resolve both AWS VPC endpoints and the AWS Managed Microsoft AD domain’s FQDN? (Select TWO.)

- **A.** Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.
- **B.** Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.
- **C.** Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries.
- **D.** Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.
- **E.** Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D (you answered correctly)

🔑 **Key words:** resolve both VPC endpoints and AD domain FQDN (Select TWO)

⚠️ **Watch:** Inbound endpoint is for on-prem → AWS queries

🧠 **Rule:** Route 53 Resolver outbound endpoint + forwarding rule to AD DNS; keep AmazonProvidedDNS.

### TD explanation

When you create a VPC using Amazon VPC, Route 53 Resolver automatically answers DNS queries for local VPC domain names for EC2 instances (ec2-192-0-2-44.compute-1.amazonaws.com) and records in private hosted zones (private.tutorialsdojo.com). For all other domain names, Resolver performs recursive lookups against public name servers.
You also can integrate DNS resolution between Resolver and DNS resolvers on your network by configuring forwarding rules. Your network can include any network that is reachable from your VPC, such as the following:

The VPC itself
Another peered VPC
An on-premises network that is connected to AWS with AWS Direct Connect, a VPN, or a network address translation (NAT) gateway.

A Route 53 Resolver Endpoint is a customer-managed resolver consisting of one or more Elastic Network Interfaces (ENIs) deployed on your VPC. Resolver Endpoints are classified into two types:

Inbound Endpoint – provides DNS resolution of AWS resources, such as EC2 instances, for your corporate network.
Outbound Endpoint – provides resolution of specific DNS names that you configure using forwarding rules to your VPC.

Outbound Resolver Endpoints host Forwarding Rules that forward queries for specified domain names to specific IP addresses. You create forwarding rules when you want to forward DNS queries for specified domain names to DNS resolvers on your network.
To forward selected queries, you create Resolver rules that specify the domain names for the DNS queries that you want to forward (such as example.com), and the IP addresses of the DNS resolvers on your network that you want to forward the queries to. If a query matches multiple rules (tutorialsdojo.com, portal.tutorialsdojo.com), the Resolver chooses the rule with the most specific match (portal.tutorialsdojo.com) and forwards the query to the IP addresses that you specified in that rule.

When Outbound Endpoint and Forwarding Rule are created, any resource in the VPC that queries the AmazonProvidedDNS as its DNS resolver is able to seamlessly resolve for AWS Managed Microsoft AD domain’s FQDN, as well as any AWS resources on the VPC such as (interface) VPC Endpoints.
The option that says: Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC is correct. You need an outbound endpoint to forward and resolve custom domain names inside your VPC.
The option that says: Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers is correct. The forwarding rules will handle queries for a given DNS domain and forward them to the AD server to resolve them.
The option that says: Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC is incorrect. An inbound endpoint is used for DNS resolution of AWS services. You need an outbound endpoint for this scenario.
The option that says: Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries is incorrect. It is not recommended to manually configure resources to split DNS queries. This entails a lot of management overhead. You just need to set the Active Directory servers as the DNS servers and the requests will be forwarded to the VPC resolver accordingly.
The option that says: Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers is incorrect. A conditional forwarder is configured inside the AD servers, not on the Route 53 resolver endpoint.
References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-configuring
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html
https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/

Check out these Amazon VPC and Amazon Route 53 Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q51"></a>

## Q51

An online gambling site is hosted in two Elastic Compute Cloud (EC2) instances inside a Virtual Private Cloud (VPC) in the same Availability Zone (AZ) but in different subnets. The first EC2 instance is running a database and the other EC2 instance is a web application that fetches data from the database. You are required to ensure that the two EC2 instances can connect with each other in order for your application to work properly. You also need to track historical changes to the security configurations associated to your instances.
Which of the following options below can meet this requirement? (Select TWO.)

- **A.** Check and configure the network ACL to allow communication between the two subnets. Ensure that the security groups allow the application host to talk to the database on the right port and protocol.
- **B.** Use AWS Config to track historical changes to the security configurations associated to your instances.
- **C.** Use Route 53 to ensure that there is proper routing between the two subnets.
- **D.** Use AWS Systems Manager to track historical changes to the security configurations associated to your instances.
- **E.** Ensure that the default route is set to a NAT instance or Internet Gateway (IGW).

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B (you answered correctly)

🔑 **Key words:** two subnets can't talk; track SG changes (Select TWO)

⚠️ **Watch:** Route 53 doesn't route between subnets

🧠 **Rule:** Fix NACL + SG; AWS Config for configuration history.

### TD explanation

AWS provides two features that you can use to increase security in your VPC: security groups and network ACLs. Security groups control inbound and outbound traffic for your instances, and network ACLs control inbound and outbound traffic for your subnets. In most cases, security groups can meet your needs; however, you can also use network ACLs if you want an additional layer of security for your VPC.

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting.
The option that says: Check and configure the network ACL to allow communication between the two subnets. Ensure that the security groups allow the application host to talk to the database on the right port and protocol is correct. NACLs and security groups act like firewalls for communication within your instances and subnets.
The option that says: Use AWS Config to track historical changes to the security configurations associated to your instances is correct. AWS Config can help you maintain compliance with your security setting by monitoring and detecting violations on your security groups depending on the rules you have specified.
The option that says: Use Route 53 to ensure that there is proper routing between the two subnets is incorrect. Route 53 can’t be used to connect two subnets. You should use Network ACLs and Security Groups instead.
The option that says: Ensure that the default route is set to NAT instance or Internet Gateway (IGW) is incorrect. Neither a NAT instance nor an Internet gateway is needed for the two EC2 instances to communicate.
The option that says: Use AWS Systems Manager to track historical changes to the security configurations associated to your instances is incorrect. Using AWS Systems Manager is not suitable to track historical changes to the security configurations associated to your instances. You have to use AWS Config instead.

References:
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html

Check out these Amazon VPC and AWS Config Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/aws-config/

Learn more about AWS Config in this 19-minute video:

</details>

<a id="q52"></a>

## Q52

A company has three AWS accounts each with its own VPCs. There is a requirement for communication between the AWS resources across the accounts, so VPC peering needs to be configured. Please refer to the figure below for details of each VPC:

VPC-B and VPC-C have matching CIDR blocks. For a short-term requirement, VPC-A needs to communicate only with the database instance in VPC-B with an IP address of 10.0.0.77/32 while being able to communicate with all the resources in VPC-C. The Solutions Architect already created the necessary VPC peering links but VPC-A cannot effectively communicate to the VPC-B instance. The Solutions Architect suspects that the routes on each VPC still need proper configuration.
Which of the following solutions will allow VPC-A to communicate with the database instance in VPC-B while being able to communicate with all resources on VPC-C?

- **A.** On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/24) with the target pcx-aaaacccc. Add a network access control list (NACL) on VPC-A to deny all connections to VPC-B except for the IP address 10.0.0.77/32. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc.
- **B.** On VPC-A, add a static route for VPC-B CIDR (10.0.0.77/32) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaacccc.
- **C.** On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc.
- **D.** Enable dynamic route propagation in VPC-A with the peering targets pcx-aaaabbbb and pcx-aaaacccc respectively. On VPC-B, enable dynamic route propagation with peering target pcx-aaaabbbb and add a network acces control list (NACL) that allows only connections to IP address 10.0.0.77/32 from pcx-aaaabbbb. On VPC-C, enable dynamic route propagation with the peering target pcx-aaaacccc.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** VPC-B and VPC-C overlap; VPC-A needs one host in B

⚠️ **Watch:** Overlapping CIDRs need a more specific route

🧠 **Rule:** Longest-prefix match: /32 route to VPC-B host, /16 to VPC-C.

### TD explanation

You can configure VPC peering connections to provide access to part of the CIDR block, a specific CIDR block (if the VPC has multiple CIDR blocks), or a specific instance within the peer VPC. In this scenario, a central VPC is peered to two or more VPCs that have overlapping CIDR blocks.
You have a central VPC (VPC A) with one subnet, and you have a VPC peering connection between VPC A and VPC B (pcx-aaaabbbb), and between VPC A and VPC C (pcx-aaaacccc). VPC B and VPC C have matching CIDR blocks. You want to use a VPC peering connection pcx-aaaabbbb to route traffic between VPC A and a specific instance in VPC B. All other traffic destined for the 10.0.0.0/16 IP address range is routed through pcx-aaaacccc between VPC A and VPC C.
VPC route tables use the longest prefix match to select the most specific route across the intended VPC peering connection. All other traffic is routed through the next matching route, in this case, across the VPC peering connection pcx-aaaacccc.

If you have a VPC peered with multiple VPCs that have overlapping or matching CIDR blocks, ensure that your route tables are configured to avoid sending response traffic from your VPC to the incorrect VPC. AWS currently does not support unicast reverse path forwarding in VPC peering connections that check the source IP of packets and route reply packets back to the source. You still need to configure static routes on VPC-B and VPC-C going to VPC-A, respectively.
Therefore, the correct answer is: On VPC-A, add a static route for VPC-B CIDR (10.0.0.77/32) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaacccc. The standard VPC peering configuration will be done for VPC-A and VPC-C. As for VPC-B, only the static route to the specific should be configured on VPC-A. AWS will handle the longest prefix match to route the traffic.
The option that says: On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/24) with the target pcx-aaaacccc. Add a network access control list (NACL) on VPC-A to deny all connections to VPC-B except for the IP address 10.0.0.77/32. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc is incorrect. This will only result in a conflict on the routing configuration on VPC-A. Network ACLs can block connections going out of your VPC, however, they can’t redirect connections out to specific targets.
The option that says: Enable dynamic route propagation in VPC-A with the peering targets pcx-aaaabbbb and pcx-aaaacccc respectively. On VPC-B, enable dynamic route propagation with peering target pcx-aaaabbbb and add a network acces control list (NACL) that allows only connections to IP address 10.0.0.77/32 from pcx-aaaabbbb. On VPC-C, enable dynamic route propagation with the peering target pcx-aaaacccc is incorrect. Dynamic route propagation is primarily used for Direct Connection connections or Site-to-Site VPNs. In this scenario, you want to force a specific route to a specific instance on a specific peering target, thus, you need to configure static routes.
The option that says: On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc is incorrect. Route configuration for VPC-A and VPC-C is correct here, however, the route configuration of VPC-A and VPC-B is not. This will make traffic to other instances in the CIDR (10.0.0.0/24), which is under VPC-C, to be routed to VPC-B.

References:
https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html#one-to-two-vpcs-lpm
https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html
https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

<a id="q61"></a>

## Q61

A company has launched a web service in the cloud that analyzes tweets filtered by keywords. This service is hosted on a fleet of on-demand EC2 instances running in multiple Availability Zones with Auto Scaling, and are load-balanced by an application load balancer. After checking the load balancer logs, the solutions architect noticed that on-demand EC2 instances in one of the AZ’s are not receiving requests. 
Which of the following option is the most likely cause of this issue?

- **A.** Multi-AZ autoscaling only works in the North Virginia region.
- **B.** You have to manually add instances in each AZ for them to receive traffic.
- **C.** The availability zone that is not receiving traffic was not associated with the application load balancer.
- **D.** Amazon EC2 Auto scaling does not span multiple availability zones.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** instances in one AZ get no traffic

⚠️ **Watch:** ASG spans AZs fine

🧠 **Rule:** ALB must have that AZ (subnet) enabled.

### TD explanation

You can set up your load balancer in EC2-Classic to distribute incoming requests across EC2 instances in a single Availability Zone or multiple Availability Zones. First, launch EC2 instances in all the Availability Zones that you plan to use. Next, register these instances with your load balancer. Finally, add the Availability Zones to your load balancer. After you add an Availability Zone, the load balancer starts routing requests to the registered instances in that Availability Zone. Note that you can modify the Availability Zones for your load balancer at any time. By default, the load balancer routes requests evenly across its Availability Zones. To route requests evenly across the registered instances in the Availability Zones, enable cross-zone load balancing.
If cross-zone load balancing is disabled:

– Each of the two targets in Availability Zone A receives 25% of the traffic.
– Each of the eight targets in Availability Zone B receives 6.25% of the traffic.

This is because each load balancer node can route 50% of its client traffic only to targets in its Availability Zone.

If cross-zone load balancing is enabled, each of the 10 targets receives 10% of the traffic. This is because each load balancer node can route 50% of its client traffic to all 10 targets.
Therefore, the correct answer is: The availability zone that is not receiving traffic was not associated with the application load balancer. Most likely, the reason is that the specific AZ is not added to the ELB.
The option that says: Amazon EC2 Auto Scaling does not span multiple availability zones is incorrect because autoscaling can work with multiple AZs.
The option that says: Multi-AZ autoscaling only works in the North Virginia region is incorrect because autoscaling can be enabled for multi AZ in any single region, not just N. Virginia.
The option that says: You have to manually add instances in each AZ for them to receive traffic is incorrect because instances need not be added manually to AZ.
References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html/
https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html

Check out this AWS Elastic Load Balancing Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

</details>

<a id="q71"></a>

## Q71

An electronics and communications company in Japan has several VPCs in the AWS cloud. It uses NAT instances to allow multiple EC2 instances from the private subnet to initiate connections to the Internet while also restricting any requests coming from the outside network. However, there are numerous incidents where the NAT instance is not available, which affects the batch processing of critical applications. 
Which is the most suitable solution that provides better availability and bandwidth to the current infrastructure with minimal administrative effort?

- **A.** Create a NAT gateway then specify its corresponding subnet and Elastic IP address. Update the route tables of the private subnet to point the Internet traffic to the NAT gateway.
- **B.** Launch two large NAT instances in two separate public subnets and add a route from the private subnet to each NAT instance to make it more fault-tolerant and highly available.
- **C.** Launch a larger NAT instance with the enhanced networking feature enabled to improve the availability and performance of the NAT device.
- **D.** Create an egress-only Internet gateway. Update the route tables of the private subnet to point the Internet traffic to the egress-only Internet gateway.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** NAT instance keeps failing; least effort

⚠️ **Watch:** Egress-only IGW is for IPv6

🧠 **Rule:** Replace NAT instances with NAT Gateway (per AZ).

### TD explanation

You can use a NAT device to enable instances in a private subnet to connect to the internet (for example, for software updates) or other AWS services, but prevent the internet from initiating connections with the instances. A NAT device forwards traffic from the instances in the private subnet to the internet or other AWS services, and then sends the response back to the instances. When traffic goes to the internet, the source IPv4 address is replaced with the NAT device’s address and similarly, when the response traffic goes to those instances, the NAT device translates the address back to those instances’ private IPv4 addresses.

AWS offers two kinds of NAT devices—a NAT gateway or a NAT instance. It is recommended to use NAT gateways, as they provide better availability and bandwidth over NAT instances. The NAT Gateway service is also a managed service that does not require your administration efforts.
A NAT instance is launched from a NAT AMI and you can choose to use a NAT instance for special purposes. However, this type of NAT device is limited and is not highly available compared with a NAT Gateway.
Therefore, the correct answer is: Create a NAT gateway then specify its corresponding subnet and Elastic IP address. Update the route tables of the private subnet to point the Internet traffic to the NAT gateway.
The option that says: Launch a larger NAT instance with the enhanced networking feature enabled to improve the availability and performance of the NAT device is incorrect. Even if you upgrade your NAT device to a larger instance, it would still be a single component. This means that if your NAT instance goes down, there would be no other instance to handle the requests, which means that your architecture is not highly available. It is better to use a NAT Gateway to provide better availability and bandwidth for your infrastructure.
The option that says: Launch two large NAT instances in two separate public subnets and add a route from the private subnet to each NAT instance to make it more fault-tolerant and highly available is incorrect. Although this solution is indeed highly available and fault-tolerant, this entails a lot of administrative effort to manage those two NAT instances. Hence, it is still better to use the NAT Gateway service since it is a managed service that does not require administrative effort.
The option that says: Create an egress-only Internet gateway. Update the route tables of the private subnet to point the Internet traffic to the egress-only Internet gateway is incorrect because an egress-only Internet gateway is primarily used to handle IPv6 traffic, which is not mentioned in this scenario.
References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

---

# Group E — Service fit (serverless, data, app design) (12)

<a id="q8"></a>

## Q8

A software development company implements cloud best practices on its AWS infrastructure. The solutions architect has been instructed to manage its AWS cloud Infrastructure as code (IAC) to automate its software build, test, and deploy process. The company follows a continuous integration and continuous delivery (CI/CD) practice to streamline its software development lifecycle. The company already uses AWS CodeArtifact to store and version its private software packages.
The company would like to have the ability to easily deploy exact copies of different versions of its cloud infrastructure, stage changes into different environments, revert back to previous versions, and identify the specific versions running in the VPC. Plus, all new public-facing applications should also have a global content delivery network (CDN) service.
Which of the following options is the recommended action to meet the company requirement?

- **A.** Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.
- **B.** Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture.
- **C.** Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.
- **D.** Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** IaC versions, stage, revert; global CDN

⚠️ **Watch:** CloudWatch is not a CDN

🧠 **Rule:** CloudFormation + CloudFront.

### TD explanation

AWS CloudFormation provides a common language for you to describe and provision all the infrastructure resources in your cloud environment. CloudFormation allows you to use a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This file serves as the single source of truth for your cloud environment.

Amazon CloudFront is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the user is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.
Therefore, the correct answer is: Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.
The option that says: Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture is incorrect. CloudWatch is typically not a CDN service.
The option that says: Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture is incorrect. As with the case above, CloudWatch is not a CDN service.
The option that says: Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture is incorrect. Even though Elastic Beanstalk enables you to quickly deploy and manage applications in the AWS Cloud, you still can’t manage the cloud infrastructure as application code with it. The best option is simply to use CloudFormation.

References:
https://aws.amazon.com/cloudformation/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

Check out this AWS CloudFormation Cheat Sheet:
https://tutorialsdojo.com/aws-cloudformation/

Elastic Beanstalk vs CloudFormation vs  OpsWorks vs CodeDeploy:
https://tutorialsdojo.com/elastic-beanstalk-vs-cloudformation-vs-opsworks-vs-codedeploy/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services/

</details>

<a id="q12"></a>

## Q12

An e-commerce company is having its annual sale event, where buyers will be able to purchase goods at a large discount on its e-commerce website. The e-commerce site will receive millions of visitors in a short period of time when the sale begins. The visitors will first log in to the site using either a Facebook or Google account and add items to the cart. After purchasing, a page will display the cart items along with the discounted prices. The company is also considering using Amazon Translate to support multiple languages for its international visitors. The company needs to build a checkout system that can handle the sudden surge of incoming traffic. The team evaluated Amazon Managed Streaming for Apache Kafka but opted for a simpler message queue for decoupling.
Which of the following is the MOST scalable solution that the company should use?

- **A.** Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito, then process the user's purchases and store them into an Amazon SQS queue using IAM Roles for Amazon EC2 Instances to gain permissions to the queue. Finally, the items from the queue are retrieved by a set of application servers and stored into an Amazon DynamoDB table.
- **B.** Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Lex, then process the user's purchases and store the cart into a Multi-AZ Amazon RDS database.
- **C.** Use the static website hosting feature of Amazon S3 with the Javascript SDK to authenticate the user login with Amazon Cognito. Set up AWS Global Accelerator to deliver the static content stored in the S3 bucket. Store user purchases in an Amazon DynamoDB table and use an IAM Role for managing permissions.
- **D.** Combine an Elastic Load balancer in front of multiple web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito. The web servers will process the user's purchases and store them in an Amazon DynamoDB table. Use an IAM Role to gain permissions to the DynamoDB table.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** sale surge; social login; simple queue for checkout

⚠️ **Watch:** Lex is a chatbot, not auth

🧠 **Rule:** Cognito + SQS buffer + DynamoDB behind ELB/CloudFront.

### TD explanation

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message oriented middleware, and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

In this scenario, the best solution is to use a combination of CloudFront, Elastic Load Balancer and SQS to provide a highly scalable architecture.
Hence, the correct answer is: Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito, then process the user’s purchases and store them into an Amazon SQS queue using IAM Roles for Amazon EC2 Instances to gain permissions to the queue. Finally, the items from the queue are retrieved by a set of application servers and stored into an Amazon DynamoDB table. This is a highly scalable solution and creates an appropriate IAM Role to access the DynamoDB database. In addition, it uses SQS which decouples the application architecture. This will allow the application servers to process the requests.
The option that says: Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Lex, then process the user’s purchases and store the cart into a Multi-AZ Amazon RDS database is incorrect because multi-AZ RDS is a more expensive solution when compared to DynamoDB. In addition, Amazon Lex is just a service for building conversational interfaces into any application using voice and text. This is not utilized for user authentication, unlike Amazon Cognito.
The option that says: Use the static website hosting feature of Amazon S3 with the Javascript SDK to authenticate the user login with Amazon Cognito. Set up AWS Global Accelerator to deliver the static content. Store user purchases in an Amazon DynamoDB table and use an IAM Role for managing permissions is incorrect. Although this would work, it is not scalable, and storing all the data directly in DynamoDB would consume read and write capacity and increase the cost. Moreover, you cannot use AWS Global Accelerator to deliver the static content stored in the S3 bucket. You have to use Amazon CloudFront instead.
The option that says: Combine an Elastic Load balancer in front of multiple web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito. The web servers will process the user’s purchases and store them in an Amazon DynamoDB table. Use an IAM Role to gain permissions to the DynamoDB table is incorrect because it is not scalable and storing all the data directly in DynamoDB would simply consume read and write capacity and increase the cost. Moreover, the web servers are not placed in an Auto Scaling group, which means that this solution is not scalable.

References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/authentication-and-access-control.html
https://aws.amazon.com/blogs/database/dynamodb-streams-use-cases-and-design-patterns/

Check out this Amazon DynamoDB Cheat Sheet:
https://tutorialsdojo.com/amazon-dynamodb/

</details>

<a id="q20"></a>

## Q20

A media company in South Korea offers high-quality wildlife photos to its clients. Its photographers upload a large number of photographs to the company’s Amazon S3 bucket. Currently, the company is using a dedicated group of on-premises servers to process the photos and uses an open-source messaging system to deliver job information to the servers. After processing, the data would go to a tape library and be stored for long-term archival. The company decided to shift everything to AWS Cloud, and the solutions architect was tasked to implement the same existing infrastructure design and leverage AWS tools such as storage and messaging services to minimize cost. 
Which of the following options is the recommended solution that will meet the requirement?

- **A.** SQS will handle the job messages, while CloudWatch alarms will terminate any idle EC2 worker instances. After the data has been processed, change the storage class of your S3 objects to S3 IA-Standard.
- **B.** SNS will handle the passing of job messages, while CloudWatch alarms will terminate any idle spot worker instances. After the data has been processed, transfer your S3 objects to Amazon Glacier.
- **C.** Create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon Glacier.
- **D.** Initially change the storage class of the S3 objects to S3 IA-Standard. Then create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon S3-IA.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** photo processing jobs; minimize cost; archive

⚠️ **Watch:** SNS isn't a work queue

🧠 **Rule:** SQS depth-scaled Spot ASG workers + Glacier for archive.

### TD explanation

There are some scenarios where you might think about scaling in response to activity in an Amazon SQS queue. For example, suppose that you have a web app that lets users upload images and use them online. In this scenario, each image requires resizing and encoding before it can be published. The app runs on EC2 instances in an Auto Scaling group, and it’s configured to handle your typical upload rates. Unhealthy instances are terminated and replaced to maintain current instance levels at all times. The app places the raw bitmap data of the images in an SQS queue for processing. It processes the images and then publishes the processed images where they can be viewed by users. The architecture for this scenario works well if the number of image uploads doesn’t vary over time. But if the number of uploads changes over time, you might consider using dynamic scaling to scale the capacity of your Auto Scaling group.

In this scenario, the best option is the combination of SQS and Glacier as a storage option.
Therefore, the correct answer is: Create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon Glacier. It uses SQS to process the messages, and it uses Glacier as the archival storage solution which is the cheapest storage option.
The option that says: SQS will handle the job messages, while CloudWatch alarms will terminate any idle EC2 worker instances. After the data has been processed, change the storage class of your S3 objects to S3 IA-Standard is incorrect. S3 IA is not an archival storage option, and since auto scaling is not mentioned, you cannot use CloudWatch alarms to terminate the idle EC2 instances.
The option that says: Initially change the storage class of the S3 objects to S3 IA-Standard. Then create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon S3-IA is incorrect. S3 IA is not an archival storage option.
The option that says: SNS will handle the passing of job messages, while CloudWatch alarms will terminate any idle spot worker instances. After the data has been processed, transfer your S3 objects to Amazon Glacier is incorrect. Amazon Simple Notification Service cannot be used to process the messages.
References:
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
https://aws.amazon.com/glacier
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html

Check out these Amazon SQS and Amazon S3 Glacier Cheat Sheets:
https://tutorialsdojo.com/amazon-sqs/
https://tutorialsdojo.com/amazon-glacier/

</details>

<a id="q21"></a>

## Q21

A company implements best practices and mandates that all of the cloud-related deployments should not be done manually but through the use of CloudFormation. All of the CloudFormation templates should be treated as code and hence, all of them are committed in a private GIT repository. A senior solutions architect has recently left the team. One of the tasks of the junior solutions architect is to handle a distributed system in AWS, in which the architecture is declared in a CloudFormation template. The distributed system needs to be migrated to another VPC and the junior solutions architect tried to read the template to understand the AWS resources that the template will generate. While analyzing the CloudFormation template, he stumbled upon the code below.
What does this code snippet do in CloudFormation?

"SNSTopic" : {
"Type" : "AWS::SNS::Topic",
"Properties" : {
"Subscription" : [{
"Protocol" : "sqs",
"Endpoint" : { "Fn::GetAtt" : [ "TutorialsDojoQueue", "Arn" ] }
}]
}

- **A.** Creates an SNS topic and then adds a subscription using the ARN attribute name for the SQS resource, which is created under the logical name TutorialsDojoQueue.
- **B.** Creates an SNS topic and then invokes the call to create an SQS queue with a logical resource name of TutorialsDojoQueue.
- **C.** Creates an SNS topic which allows SQS subscription endpoints to be added as a parameter on the template.
- **D.** Creates an SNS topic which allows SQS subscription endpoints.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** read a CFN SNS subscription snippet

⚠️ **Watch:** GetAtt references an existing logical resource

🧠 **Rule:** Fn::GetAtt Queue.Arn subscribes the SQS queue to the SNS topic.

### TD explanation

AWS CloudFormation provides several built-in functions that help you manage your stacks which are called “intrinsic functions”. Use intrinsic functions in your templates to assign values to properties that are not available until runtime.
You can use intrinsic functions only in specific parts of a template. Currently, you can use intrinsic functions in resource properties, outputs, metadata attributes, and update policy attributes. You can also use intrinsic functions to conditionally create stack resources.
The Fn::GetAtt intrinsic function returns the value of an attribute from a resource in the template. It has 2 parameters: the logicalNameOfResource and the attributeName. The logical name (also called logical ID) of the resource contains the attribute that you want to use. The attributeName is the name of the resource-specific attribute whose value you want to utilize.

Therefore, the correct answer is: Create an SNS topic and then add a subscription using the ARN attribute name for the SQS resource, which is created under the logical name TutorialsDojoQueue. The code snippet creates an SNS topic and then adds a subscription using the ARN attribute name for the SQS resource, which is created under the logical name “TutorialsDojoQueue” using the GetAtt intrinsic function.
The following options are all incorrect because these options incorrectly described what the code snippet does:
– Creates an SNS topic which allows SQS subscription endpoints to be added as a parameter on the template.

– Creates an SNS topic which allows SQS subscription endpoints.
– Creates an SNS topic and then invokes the call to create an SQS queue with a logical resource name of TutorialsDojoQueue.

References:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html

Check out this AWS CloudFormation Cheat Sheet:
https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q30"></a>

## Q30

A startup is running a data processing application on AWS. The application is hosted on 25 Amazon EC2 On-Demand Instances, distributed across three Availability Zones, and registered with a target group for a Network Load Balancer (NLB). 
Reports indicate a sharp decline in performance during high-demand periods, with CPU utilization spiking to 90%-100%. During normal operations, utilization averages only 20%. The application is stateless and needs to ensure consistent response times even during peak traffic. The company is also considering scheduled scaling to handle anticipated traffic increases during planned events.
 The company wants to improve application performance while optimizing costs over the next three years. 
Which solution is the most cost-effective for addressing this issue?

- **A.** Replace the On-Demand Instances with a Spot Fleet request type of request and with EBS-optimized enabled. Set the TotalTargetCapacity parameter to 25 and DefaultTargetCapacityType parameter to Spot. Attach the Spot Fleet to the NLB.
- **B.** Replace the On-Demand Instances with a Spot Fleet request type of request. Configure the InstanceInterruptionBehavior to stop and TotalTargetCapacity parameter to 30. Attach the Spot Fleet to the NLB.
- **C.** Configure an Auto Scaling group and attach it to the NLB. Set the minimum capacity to 5 instances and the maximum capacity to 30. Purchase Reserved Instances for 5 instances.
- **D.** Configure an ASG (Auto Scaling Group) and attach it to the Network Load Balancer. Set the capacity to a minimum of 15 instances and a maximum of 25. Purchase Reserved Instances for 15 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** stateless app; CPU spikes; cost over 3 years

⚠️ **Watch:** All-Spot for consistent response time is risky

🧠 **Rule:** ASG min 5/max 30 + Reserved Instances for the baseline.

### TD explanation

An Auto Scaling Group is a feature of Amazon EC2 that automatically manages a collection of EC2 instances, adjusting the number of running instances based on defined conditions. It helps maintain application availability and allows you to automatically increase the number of instances during demand spikes to preserve performance, and decrease capacity during lulls to reduce costs.
A Network Load Balancer (NLB) is a high-performance load-balancing service that operates at the transport layer (Layer 4) of the OSI model and is designed to handle millions of requests per second while maintaining ultra-low latencies. It’s capable of processing TCP, UDP, and TLS traffic, and is ideal for applications requiring extreme performance, such as gaming, IoT, and streaming services, while also providing static IP addresses for each Availability Zone.

The combination of Auto Scaling Groups and Network Load Balancer provides a robust and flexible infrastructure that can adapt to varying workloads while maintaining cost-efficiency. The Auto Scaling Group ensures that the application always has enough resources to handle incoming traffic, scaling up during high-demand periods and down during quieter times. This dynamic scaling addresses the reported performance issues during peak times when CPU utilization spikes to 90-100%.
The Network Load Balancer, meanwhile, efficiently distributes the incoming traffic across the available instances, ensuring that no single instance becomes overwhelmed. This is particularly important for maintaining consistent response times, which is a key requirement for the application.
The minimum capacity of 5 instances aligns well with the average 20% CPU utilization during normal operations. This baseline ensures that the application can handle typical loads without over-provisioning resources. The maximum capacity of 30 instances allows for significant scaling during high-demand periods, exceeding the current setup of 25 instances and providing room for future growth.
Purchasing Reserved Instances for a minimum of five instances is a strategic cost-saving measure. Reserved Instances offer substantial discounts compared to On-Demand pricing, especially over three years. This approach locks in lower prices for the baseline capacity while still allowing for flexible scaling with On-Demand instances when needed.
Hence, the correct answer is: Configure an Auto Scaling group and attach it to the NLB. Set the minimum capacity to 5 instances and the maximum capacity to 30. Purchase Reserved Instances for 5 instances.
The option that says: Replace the On-Demand Instances with a Spot Fleet request type of request and with EBS-optimized enabled. Set the TotalTargetCapacity parameter to 25 and DefaultTargetCapacityType parameter to Spot. Attach the Spot Fleet to the NLB is incorrect. While Spot Instances can offer cost savings, they are unsuitable for applications requiring consistent performance. Spot Instances are primarily used for flexible workloads that can tolerate interruptions. They are ideal for batch processing jobs, big data analytics, and high-performance computing tasks that don’t require continuous availability.
The option that says: Replace the On-Demand Instances with a Spot Fleet request type of request. Configure the InstanceInterruptionBehavior to stop and TotalTargetCapacity parameter to 30. Attach the Spot Fleet to the NLB is incorrect because, similar to the previous option, this solution relies entirely on Spot Instances, which are not suitable for applications requiring consistent performance. Additionally, the stop behavior doesn’t prevent interruptions, and it only changes how instances are handled when interrupted.
The option that says: Configure an ASG (Auto Scaling Group) and attach it to the Network Load Balancer. Set the capacity to a minimum of 15 instances and a maximum of 25. Purchase Reserved Instances for 15 instances is incorrect. While this option uses Auto Scaling and Reserved Instances, which are good practices, it doesn’t allow scaling beyond the current maximum of 25 instances, which may not address the performance issues during peak demand.

References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/
https://tutorialsdojo.com/aws-auto-scaling/

</details>

<a id="q40"></a>

## Q40

An international humanitarian aid organization has a requirement to store 20 TB worth of scanned files for the relief operations, which can grow to a total of 50 TB of data. There is also a requirement to have a website with a search feature in place that can be used to easily find a certain item through the thousands of scanned files. The new system is expected to run for more than three years. 
Which of the following is the most cost-effective option for implementing the search feature in the system?

- **A.** Use S3 for both storing and searching the scanned files by utilizing the native search capabilities of S3.
- **B.** Design the new system using a CloudFormation template. Use an EC2 instance running an NGINX web server and an open-source search application. Launch multiple standard EBS volumes with RAID configuration to store the scanned files with a search index.
- **C.** Use Amazon EFS to store and serve the scanned files. Install a 3rd-party search software on an Auto Scaling group of On-Demand EC2 Instances and an Elastic Load Balancer.
- **D.** Set up a new S3 bucket with standard storage to store and serve the scanned files. Use Amazon OpenSearch Service for query processing and use Elastic Beanstalk to host the website across multiple availability zones.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** 50 TB scanned files + search; >3 years; cost-effective

⚠️ **Watch:** S3 has no native full-text search

🧠 **Rule:** S3 storage + OpenSearch Service + Beanstalk.

### TD explanation

Amazon Simple Storage Service (S3) is an excellent object-based storage that is highly durable and scalable. However, its native search capability is not effective. Hence, you need to have a separate service to handle the search feature.
Amazon OpenSearch Service simplifies the deployment, operation, and scaling of OpenSearch, a widely-used open-source search and analytics engine. It provides robust security features, ensures high availability and data durability, and offers direct access to the OpenSearch API.

Amazon S3 offers scalable and cost-effective storage, making it ideal for handling large datasets. It ensures durability and easy access to the scanned files.
Amazon OpenSearch Service is optimized for efficient search and analytics, making it perfect for querying extensive datasets.
Elastic Beanstalk simplifies the deployment and management of the website, significantly reducing operational overhead.
By hosting the website across multiple availability zones, the system ensures high reliability and availability, which is crucial for humanitarian operations.
Hence, the correct answer is: Set up a new S3 bucket with standard storage to store and serve the scanned files. Use Amazon OpenSearch Service for query processing and use Elastic Beanstalk to host the website across multiple availability zones.
The option that says: Use Amazon EFS to store and serve the scanned files. Install a 3rd-party search software on an Auto Scaling group of On-Demand EC2 Instances and an Elastic Load Balancer is incorrect. It is stated in the scenario that the new system is expected to run for more than 3 years which means that using Reserved EC2 instances would typically be a more cost-effective choice than using On-Demand instances. In addition, purchasing and installing a 3rd-party search software might be more expensive than just using Amazon OpenSearch Service.
The option that says: Design the new system using a CloudFormation template. Use an EC2 instance running an NGINX web server and an open-source search application. Launch multiple standard EBS volumes with RAID configuration to store the scanned files with a search index is incorrect because a system composed of RAID configuration of EBS volumes is not a durable and scalable solution compared to S3.
The option that says: Use S3 for both storing and searching the scanned files by utilizing the native search capabilities of S3 is incorrect as the native search capability of S3 is not effective. It is better to use Amazon OpenSearch Service or another service primarily providing search functionality.

References:
https://aws.amazon.com/s3/
https://docs.aws.amazon.com/opensearch-service/
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hawordpress-tutorial.html

Check out this Amazon OpenSearch Service Cheat Sheet:
https://tutorialsdojo.com/amazon-opensearch-service/

</details>

<a id="q47"></a>

## Q47

An insurance company collects contributions from its clients and invests in the stock market. Using the on-premises data center, the company ingests raw data feeds from the stock market, transforms it, and sends it to the internal Apache Kafka cluster for processing. The management wants to send the cluster’s output to Amazon Web Services by building a scalable and near-real-time solution that will provide the stock market data to its web application. The application is a critical production component, so the solution needs to have a consistent high-performance network.
Which of the following actions should the solutions architect implement to fulfill the requirements? (Select THREE.)

- **A.** Fetch the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Consumer Library. Use Kinesis Data Analytics to process and transform the streaming data before delivering it to downstream consumers.
- **B.** Write an AWS Lambda function to process the Amazon Kinesis data stream and create a WebSocket API in Amazon API Gateway to invoke the function. Send the callback messages to connected clients by using the @connections command for the API.
- **C.** To have consistent performance, request for an AWS Direct Connect connection from the on-premises data center to the AWS VPC.
- **D.** Write an AWS Lambda function to process the Amazon Kinesis data stream and write a GraphQL API in AWS AppSync to invoke the function. Send the callback messages to connected clients by using the @connections command for the API.
- **E.** To have a consistent performance while being cost-effective, configure a Site-to-Site VPN from the on-premises data center to the AWS VPC.
- **F.** Pull the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Producer Library.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C, F (you answered correctly)

🔑 **Key words:** on-prem Kafka → near-real-time web app; consistent network (Select THREE)

⚠️ **Watch:** KCL consumes; KPL produces

🧠 **Rule:** EC2 KPL into Kinesis + Direct Connect + Lambda + WebSocket API @connections.

### TD explanation

AWS Direct Connect makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs in the same region. Using private VIF on AWS Direct Connect, you can establish private connectivity between AWS and your data center, office, or colocation environment, as shown in the following figure. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.

A producer puts data records into Amazon Kinesis data streams. For example, a web server sending log data to a Kinesis data stream is a producer. A consumer processes the data records from a stream. To put data into the stream, you must specify the name of the stream, a partition key, and the data blob to be added to the stream. The partition key is used to determine which shard in the stream the data record is added to. All the data in the shard is sent to the same worker that is processing the shard.
A WebSocket API in API Gateway is a collection of WebSocket routes that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can use API Gateway features to help you with all aspects of the API lifecycle, from creation through monitoring your production APIs.

API Gateway WebSocket APIs are bidirectional. A client can send messages to a specific service, and services can independently send messages to clients. This bidirectional behavior enables richer client/service interactions because services can push data to clients without requiring clients to make an explicit request. WebSocket APIs are often used in real-time applications such as chat applications, collaboration platforms, multiplayer games, and financial trading platforms.
You can use the @connections API from your backend service to send a callback message to a connected client, get connection information or disconnect from the client.
Hence, the correct answers are:
– To have consistent performance, request for an AWS Direct Connect connection from the on-premises data center to the AWS VPC.
– Pull the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Producer Library.
– Write an AWS Lambda function to process the Amazon Kinesis data stream and create a WebSocket API in Amazon API Gateway to invoke the function. Send the callback messages to connected clients by using the @connections command for the API.
The option that says: Fetch the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Consumer Library. Use Kinesis Data Analytics to process and transform the streaming data before delivering it to downstream consumers is incorrect because you should typically use Amazon Kinesis Producer Library, not Consumer Library.
The option that says: Write an AWS Lambda function to process the Amazon Kinesis data stream and write a GraphQL API in AWS AppSync to invoke the function. Send the callback messages to connected clients by using the @connections command for the API is incorrect because using @connections to have the backend service connect back to the clients is not primarily a feature of the GraphQL API when using AWS AppSync.
The option that says: To have a consistent performance while being cost-effective, configure a Site-to-Site VPN from the on-premises data center to the AWS VPC is incorrect because a Site-to-Site VPN does not provide a reliable and high-performance network connection between the on-premises data center and Amazon VPC.

References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html
https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-producers.html
https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html

Check out these AWS Direct Connect and Amazon Kinesis Cheat Sheets:
https://tutorialsdojo.com/aws-direct-connect/
https://tutorialsdojo.com/amazon-kinesis/

</details>

<a id="q58"></a>

## Q58

An electric utility company deploys smart meters for its customers to easily track electricity usage. Each smart meter sends data every five minutes to an Amazon API Gateway, which is then processed by several AWS Lambda functions before being stored in an Amazon DynamoDB table. The Lambda functions take about 5 to 10 seconds to process the data based on the initial deployment testing. As the company’s customer base grew, the solutions architect noticed that the Lambda functions were now taking 60 to 90 seconds to complete the processing. New metrics are also collected from the smart meters, which further increases the processing time. Errors began showing when running the Lambda function, such as TooManyRequestsException and ProvisionedThroughputExceededException error when performing a PUT operation on the DynamoDB table.
Which combination of the following actions will resolve these issues? (Select TWO.)

- **A.** The new metrics being collected requires more processing power from the Lambda functions. Adjust the memory allocation for the Lambda function to accommodate the surge.
- **B.** Process the data in batches to avoid reaching the write limits to the DynamoDB table. Group the requests from API Gateway by streaming the data into an Amazon Kinesis data stream.
- **C.** Modify the Amazon API Gateway throttling limits and quotas at the stage level to allow a higher request rate and burst capacity so that incoming smart meter data is not throttled before being sent to Lambda.
- **D.** As more customers are sending data, adjust the Write Capacity Unit (WCU) of the DynamoDB table to be able to accommodate all the write requests being processed by the Lambda functions.
- **E.** Since the Lambda functions are being overwhelmed with too many requests, increase the payload size from the meters but send the data less frequently to avoid reaching the concurrency limit.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D (you answered correctly)

🔑 **Key words:** TooManyRequests + ProvisionedThroughputExceeded (Select TWO)

⚠️ **Watch:** ⚠️ Q24: stream ingestion → Kinesis/Firehose batching

🧠 **Rule:** Batch via Kinesis + raise DynamoDB WCU.

### TD explanation

In Amazon DynamoDB, the ProvisionedThroughputExceededException error means that you exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes. This means that your request rate is too high. The AWS SDKs for DynamoDB automatically retries requests that receive this exception. Your request is eventually successful unless your retry queue is too large to finish.
To solve this, you can increase the write capacity unit (WCU) of your DynamoDB table. Every PutItem request consumes a write capacity unit. A write capacity unit represents one write per second, for an item up to 1 KB in size. For example, suppose that you create a table with 10 write capacity units. This allows you to perform 10 writes per second for items up to 1 KB in size.

In AWS Lambda, the first time you invoke your function, AWS Lambda creates an instance of the function and runs its handler method to process the event. When the function returns a response, it stays active and waits to process additional events. If you invoke the function again while the first event is being processed, Lambda initializes another instance, and the function processes the two events concurrently. Your functions’ concurrency is the number of instances that serve requests at a given time. For an initial burst of traffic, your functions’ cumulative concurrency in a Region can reach an initial level of between 500 and 3000, which varies per Region.
When seeing the TooManyRequestsException in AWS Lambda, it is possible that the throttles that you’re seeing aren’t on your Lambda function. Throttles can also occur on API calls during your function’s invocation or on concurrency limits.
With API Gateway, you can send the stream to an Amazon Kinesis data stream on which you can group requests in batches, so there will be a decrease in requests in Lambda.
Hence, the correct answers are:
– As more customers are sending data, adjust the Write Capacity Unit (WCU) of the DynamoDB table to be able to accommodate all the write requests being processed by the Lambda functions.
– Process the data in batches to avoid reaching the write limits to the DynamoDB table. Group the requests from API Gateway by streaming the data into an Amazon Kinesis data stream.
The option that says: The new metrics being collected requires more processing power from the Lambda functions. Adjust the memory allocation for the Lambda function to accommodate the surge is incorrect. While increasing memory allocation can improve the Lambda function’s execution speed, it can only do so to a certain extent. This improvement may alleviate some occurrences of the TooManyRequestsException error, especially at lower memory configurations. However, as you approach the upper memory limits, the performance gains tend to plateau, making it less effective than solutions such as batching. Moreover, the cost in running the function will also increase significanly.
The option that says: Since the Lambda functions are being overwhelmed with too many requests, increase the payload size from the meters but send the data less frequently to avoid reaching the concurrency limit is incorrect. Although this will solve the TooManyRequestsException for the Lambda function, you may reach the 10MB payload limit on the API gateway if you aggregate too much data before sending it to the API Gateway.
The option that says: Modify the Amazon API Gateway throttling limits and quotas at the stage level to allow a higher request rate and burst capacity so that incoming smart meter data is not throttled before being sent to Lambda is incorrect because the errors observed (TooManyRequestsException and ProvisionedThroughputExceededException) are typically caused by Lambda concurrency limits and DynamoDB throughput, not API Gateway throttling. API Gateway quotas are much higher than the described workload, so increasing them would not resolve the actual bottlenecks.

References:
https://aws.amazon.com/premiumsupport/knowledge-center/lambda-troubleshoot-throttling/
https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html#concurrent-execution-safety-limit
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html

Check out these AWS Lambda and Amazon DynamoDB Cheat Sheets:
https://tutorialsdojo.com/aws-lambda/
https://tutorialsdojo.com/amazon-dynamodb/

</details>

<a id="q64"></a>

## Q64

A company wants to create a new service that will complement the launch of its new product. The site must be highly available and scalable to handle the unpredictable workload, and should also be stateless and REST compliant. The solution needs to have multiple persistent storage layers for service object metadata and durable storage for static content. All requests to the service should be authenticated and securely processed. The company also wants to keep the costs at a minimum. The team considered using an AWS Lambda authorizer for custom authentication logic but wants to minimize operational overhead.
Which of the following is the recommended solution that will meet the company requirements?

- **A.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **B.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **C.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service.
- **D.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** stateless REST, authenticated, lowest cost

⚠️ **Watch:** ElastiCache isn't a durable metadata store

🧠 **Rule:** API Gateway + Lambda + Cognito + DynamoDB + S3 presigned URLs.

### TD explanation

Amazon API Gateway Lambda proxy integration is a simple, powerful, and nimble mechanism to build an API with a setup of a single API method. The Lambda proxy integration allows the client to call a single Lambda function in the backend. The function accesses many resources or features of other AWS services, including calling other Lambda functions.
In Lambda proxy integration, when a client submits an API request, API Gateway passes to the integrated Lambda function the raw request as-is, except that the order of the request parameters is not preserved. This request data includes the request headers, query string parameters, URL path variables, payload, and API configuration data. The configuration data can include current deployment stage name, stage variables, user identity, or authorization context (if any).
A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers. Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).

User pools provide:
– Sign-up and sign-in services.
– A built-in, customizable web UI to sign in users.
– Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple, as well as sign-in with SAML identity providers from your user pool.
– User directory management and user profiles.
– Security features such as multi-factor authentication (MFA), checks for compromised credentials, account takeover protection, and phone and email verification.
– Customized workflows and user migration through AWS Lambda triggers.
Amazon S3 is a simple key-based object store whose scalability and low cost make it ideal for storing large datasets or objects. When finding objects based on attributes or other metadata, a common solution is to build an external index such as a DynamoDB Table that maps queryable attributes to the S3 object key. DynamoDB is a NoSQL data store that can be used for storing the index itself.
One way of securing objects that are shared on S3 buckets is by using presigned URLs. When you create a presigned URL for your object, you must provide your security credentials, specify a bucket name, an object key, specify the HTTP method (GET to download the object), and expiration date and time. The presigned URLs are valid only for the specified duration.
Anyone who receives the presigned URL can then access the object. For example, if you have a video in your bucket and both the bucket and the object are private, you can share the video with others by generating a presigned URL.
Hence, the correct answer is: Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
The option that says: Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service is incorrect. Although running Docker-based containers on Amazon Fargate is possible, this solution does not just offer the lowest possible cost to satisfy the given scenario. AWS Lambda is suited for creating serverless/stateless APIs and costs cheaper than AWS Fargate.
The option that says: Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket is incorrect. Running a Fargate cluster continuously is more expensive than running Lambda functions which only runs on-demand.
The option that says: Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket is incorrect because it is recommended to use Amazon Cognito user pools for user access controls compared to an API Gateway custom authorizer. It is more robust and offers more features because it is designed to handle user access.

References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
https://aws.amazon.com/blogs/big-data/building-and-maintaining-an-amazon-s3-metadata-index-without-servers/

Check out these AWS Comparison Cheat Sheets:
https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai/
https://tutorialsdojo.com/ec2-container-service-ecs-vs-lambda/

</details>

<a id="q70"></a>

## Q70

A leading online media company runs a popular sports news website. The solutions architect has been tasked to analyze each web visitor’s clickstream data on the website to populate user analytics, which gives insights about the sequence of pages and advertisements the visitor has clicked. The data will be processed in real-time which will then transform the page layout as the visitors click through the web portal to increase user engagement and consequently, increase the revenue for the company. 
Which of the following options should the solutions architect implement to meet the above requirements?

- **A.** Publish web clicks by session to an Amazon SQS queue and periodically drain these events to Amazon RDS then analyze with SQL.
- **B.** Log clicks in weblogs by URL and store it in Amazon S3, and then analyze with Elastic MapReduce.
- **C.** Push web clicks by session to Amazon Kinesis and analyze behavior using Amazon Kinesis workers.
- **D.** Publish the web clicks to Amazon Timestream. Run custom analysis, SQL queries and apply machine learning to generate relevant reports regarding user behavior.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** clickstream real-time layout changes

⚠️ **Watch:** SQS/EMR are not real time

🧠 **Rule:** Kinesis + Kinesis consumers.

### TD explanation

Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information. Amazon Kinesis offers key capabilities to cost-effectively process streaming data at any scale, along with the flexibility to choose the tools that best suit the requirements of your application. With Amazon Kinesis, you can ingest real-time data such as video, audio, application logs, website clickstreams, and IoT telemetry data for machine learning, analytics, and other applications. Amazon Kinesis enables you to process and analyze data as it arrives and responds instantly instead of having to wait until all your data is collected before the processing can begin.
In this example, a simple HTML page simulates the content of a blog page. As the reader scrolls the simulated blog post, the browser script uses the SDK for JavaScript to record the scroll distance down the page and send that data to Kinesis using the putRecords method of the Kinesis client class. The streaming data captured by Amazon Kinesis Data Streams can then be processed by Amazon EC2 instances and stored in any of several data stores including Amazon DynamoDB and Amazon Redshift.

Therefore, the correct answer is: Push web clicks by session to Amazon Kinesis and analyzing behavior using Amazon Kinesis workers.
The following options are incorrect as SQS, EC2, EMR, and Timestream services do not have the capacity to analyze real-time streaming data:
– Log clicks in weblogs by URL and store it in Amazon S3, and then analyze with Elastic MapReduce.
– Publish the web clicks to Amazon Timestream. Run custom analysis, SQL queries and apply machine learning to generate relevant reports regarding user behavior.
– Publish web clicks by session to an Amazon SQS queue and periodically drain these events to Amazon RDS then analyze with SQL.
References:
https://docs.aws.amazon.com/streams/latest/dev/introduction.html
https://aws.amazon.com/kinesis/data-streams/
https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/kinesis-examples-capturing-page-scrolling.html

Check out this Amazon Kinesis Cheat Sheet:
https://tutorialsdojo.com/amazon-kinesis/

</details>

<a id="q73"></a>

## Q73

A global real estate startup is looking for an option of adding a cost-effective location-based alert to iOS and Android mobile apps. Users will receive push notifications on mobile devices regarding real estate offers in proximity to current locations, with delivery expected in under a minute. The existing mobile app has an initial 2 million users worldwide and is rapidly growing. The team considered using AWS Wavelength for edge processing of location data but chose a simpler queuing approach to reduce costs.
What is the most suitable architecture to use in this scenario?

- **A.** Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app.
- **B.** Set up an architecture where the mobile app will send the user's location to an Amazon API Gateway with AWS Lambda functions that process and retrieve the relevant offers from an Amazon RDS database. Once the data has been processed, use Amazon Pinpoint to send out the offers to the mobile app.
- **C.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use AWS SNS Mobile Push to send out the offers to the mobile app.
- **D.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** location-based push to millions; <1 min; cheap

⚠️ **Watch:** Device Farm is a testing service

🧠 **Rule:** SQS + workers + DynamoDB + SNS Mobile Push.

### TD explanation

With Amazon SNS Mobile Push Notifications, you have the ability to send push notification messages directly to apps on mobile devices. Push notification messages sent to a mobile endpoint can appear in the mobile app as message alerts, badge updates, or even sound alerts.

Hence, the correct answer is: Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use AWS SNS Mobile Push to send out the offers to the mobile app because SQS is a highly scalable, cost-effective solution for carrying out utility tasks such as holding the location of millions of users. In addition, it uses a highly scalable DynamoDB table and a cost-effective AWS SNS Mobile Push service to send push notification messages directly to the mobile apps.
The option that says: Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app is incorrect. Although a combination of On-Demand EC2 instances and API Gateway can provide a scalable computing system, it is wrong to use AWS AppSync for push notification to mobile devices. You should use AWS SNS Mobile Push service instead.
The option that says: Set up an architecture where the mobile app will send the user’s location to an Amazon API Gateway with AWS Lambda functions that process and retrieve the relevant offers from an Amazon RDS database. Once the data has been processed, use Amazon Pinpoint to send out the offers to the mobile app is incorrect. Although it is correct to use Amazon Pinpoint to send push notifications, RDS is not a suitable database for the mobile app because it is not as scalable enough when processing data from various users around the globe, compared with DynamoDB. Usually, mobile applications do not have complicated table relationships hence, it is recommended to use a NoSQL database like DynamoDB.
The option that says: Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app is incorrect because AWS Device Farm is an app testing service and is not simply used to push notifications to various mobile devices. It only lets you test and interact with your Android, iOS, and web apps on many devices at once, or reproduce issues on a device in real-time.
References:
https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html
https://docs.aws.amazon.com/sns/latest/dg/mobile-push-pseudo.html
https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html

Check out this Amazon SNS Cheat Sheet:
https://tutorialsdojo.com/amazon-sns/

</details>

<a id="q74"></a>

## Q74

A weather forecasting agency established a network of IoT devices in the ocean to help predict incoming typhoons. The IoT devices monitor the sea surface temperature and atmospheric pressure and send the data as messages to AWS IoT Core, which updates an Amazon DynamoDB table. On the weekly monitoring report, a system administrator notices that no new database updates are happening. The agency already uses AWS IoT Device Defender to audit device security policies and detect abnormal behavior, but this does not help diagnose connectivity interruptions.
What should the administrator do to troubleshoot the issue?

- **A.** Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core.
- **B.** Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click.
- **C.** Register the IoT devices to AWS IoT Device Management and monitor the devices' health and ensure the devices are connected to AWS IoT Core.
- **D.** Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** IoT devices stopped updating DynamoDB

⚠️ **Watch:** Device Defender is security auditing

🧠 **Rule:** Device health/connectivity → IoT Device Management.

### TD explanation

AWS IoT Device Management is a service that makes it easy to securely register, organize, monitor, and remotely manage IoT devices at scale throughout their lifecycle. You can use IoT Device Management to upload and view device information and configuration, organize your device inventory, monitor your fleet of devices, troubleshoot individual devices, and remotely manage devices deployed across many locations, including updating device software over-the-air (OTA).
By registering the IoT devices to AWS IoT Device Management, the system administrator can monitor the health of the devices and ensure connectivity to AWS IoT Core. This will help identify if there are connectivity issues that might be causing the lack of updates in the DynamoDB table.

AWS IoT Device Management has a feature that allows you to group your device fleet based on function, security requirements, or other categories. This makes it easier to manage IoT devices at scale. The groupings allow policy management, viewing metrics, or performing actions on the entire group.
Therefore, the correct answer is: Register the IoT devices to AWS IoT Device Management and monitor the devices’ health and ensure the devices are connected to AWS IoT Core.
The option that says: Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity is incorrect. AWS IoT Defender is primarily used for security audit, alerting, and mitigation of IoT resources and does not directly manage Certificate Authority in AWS IoT Core. It is also not used for establishing connectivity between the devices and AWS IoT Core.
The option that says: Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core is incorrect. AWS IoT SiteWise is simply used for collecting and gaining insights to equipment data for industrial operations management. It is not used for collecting data from IoT devices.
The option that says: Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click is incorrect. Triggering a Lambda function does not address the potential connectivity issue between the IoT devices and AWS IoT Core. Using it to directly update the DynamoDB table will bypass AWS IoT Core and is not the solution to the question.
References:
https://aws.amazon.com/iot-device-management/faq/
https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html

Check out this AWS IoT Core Cheat Sheet:
https://tutorialsdojo.com/aws-iot-core/

</details>

---

# Group F — Storage, migration & ops (6)

<a id="q4"></a>

## Q4

A company is running 150 virtual machines (VMs) using 40 TB of storage on its on-premises data center. The company wants to migrate its whole environment to AWS within the next three months. The VMs are mainly used during business hours only, so these can be taken offline, but some are mission-critical, which means that the downtime needs to be minimized. Since upgrading the Internet connection is quite costly for the company, the on-premises network administrator provisioned only a 12 Mbps Internet bandwidth for the migration. The Solutions Architect must design a cost-effective plan to complete the migration within the target time frame. The migration team has already installed the AWS Application Discovery Agent on its on‑premises servers to collect performance and dependency data.
Which of the following options should the Solutions Architect implement to fulfill the requirements?

- **A.** Deploy the AWS Agentless Discovery connector on the company VMware vCenter to assess each application. With the information gathered, refactor each application to run on AWS services or using AWS Marketplace solutions.
- **B.** Request a 1 Gbps AWS Direct Connect connection from the on-premises data center to AWS. Create a private virtual interface on Direct Connect. Migrate the virtual machines to AWS using the AWS Transform MGN.
- **C.** Create an export of your virtual machines during out of office hours. Use the AWS Transfer service to securely upload the VMs to Amazon S3 using the SFTP protocol. Import the VMs into Amazon EC2 instances using the VM Import/Export service.
- **D.** Use AWS Transform MGN to migrate the mission‑critical virtual machines to AWS. For the non‑mission‑critical VMs, export them and schedule a reservation with AWS Data Transfer Terminal to upload the data at the facility. Once the VMs are on Amazon S3, import the VMs into Amazon EC2 instances using the VM Import/Export service.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** 150 VMs, 40 TB, 12 Mbps, 3 months; some mission-critical

⚠️ **Watch:** DX takes weeks and costs more

🧠 **Rule:** MGN for critical VMs + offline bulk transfer + VM Import for the rest.

### TD explanation

AWS Transform MGN (MGN) is an automated lift-and-shift solution that simplifies and speeds up the migration of applications to AWS, reducing costs. It enables businesses to move physical, virtual, or cloud servers without compatibility issues or performance disruptions. MGN replicates source servers to AWS and automatically launches them, allowing immediate benefits from cloud agility and cost savings. After migration, companies can easily replatform or refactor their applications using AWS services for faster modernization.

The AWS Data Transfer Terminal is a network-ready, physical facility where you can bring your data storage devices for quick transfers to and from AWS Cloud services. This service allows you to upload data collected remotely, making it easier to access that information.

To use the Data Transfer Terminal, schedule a reservation at one of the facilities through the AWS Management Console. Arrive at your scheduled time and upload your data to your AWS Cloud services using your devices. Once your reservation is complete and you leave the facility, it will be re-secured and prepared for the next scheduled appointment.
AWS VM Import/Export enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances and export them back to your on-premises environment. VM Import/Export is available at no additional charge beyond standard usage charges for Amazon EC2 and Amazon S3. As part of the import process, VM Import will convert your VM into an Amazon EC2 AMI, which you can use to run Amazon EC2 instances.
Therefore, the correct answer is: Use AWS Transform MGN to migrate the mission‑critical virtual machines to AWS. For the non‑mission‑critical VMs, export them and schedule a reservation with AWS Data Transfer Terminal to upload the data at the facility. Once the VMs are on Amazon S3, import the VMs into Amazon EC2 instances using the VM Import/Export service. AWS Transform MGN minimizes downtime for mission‑critical workloads, while AWS Data Transfer Terminal provides a cost‑effective offline transfer solution for the bulk 40 TB dataset. This offline transfer is necessary to meet the requirement since the available Internet bandwidth is only 12 Mbps, which would otherwise make the migration impossible within the three‑month timeframe. This hybrid approach meets the deadline and balances both cost and downtime requirements.
The option that says: Request a 1 Gbps AWS Direct Connect connection from the on-premises data center to AWS. Create a private virtual interface on Direct Connect. Migrate the virtual machines to AWS using the AWS Transform MGN is incorrect. Although this is a fast solution that can typically finish the migration within the required time frame, it is not the most cost-effective solution. As stated in the question, upgrading the Internet connection (and probably requesting a new connection) is costly for the company. Moreover, the requirement is to migrate to virtual machines and not to establish a fast, dedicated network connection from the on-premises network to AWS.
The option that says: Deploy the AWS Agentless Discovery connector on the company VMware vCenter to assess each application. With the information gathered, refactor each application to run on AWS services or using AWS Marketplace solutions is incorrect. This requires a lot of effort for planning since you will have to match each application to the AWS service. This will just require changes in the application and can cause possible interruptions during the migration.
The option that says: Create an export of your virtual machines during out of office hours. Use the AWS Transfer service to securely upload the VMs to Amazon S3 using the SFTP protocol. Import the VMs into Amazon EC2 instances using the VM Import/Export service is incorrect. Although this is possible, with the 12 Mbps Internet connection, it will take more than three months to upload all the 40 TB worth of VM storage to an Amazon S3 bucket.

References:
https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html
https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html
https://aws.amazon.com/ec2/vm-import/

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/aws-cheat-sheets/

</details>

<a id="q16"></a>

## Q16

A company uses a CloudFormation script to deploy an online voting application. The app is used for a Nature Photography Contest that accepts high-resolution images, stores them in an S3 bucket, and records a 100-character summary about the image in RDS. The Solutions Architect must ensure that the same online voting application can be deployed once again using the same CloudFormation template for succeeding contests in the future. The photography contest will run for just a month and once it has been concluded, there would be nobody using the online voting application anymore until the next contest. As preparation for the upcoming events next year, the 100-character summaries should be kept and the S3 bucket, which contains the high-resolution photos, should remain. 
Which of the following options is the recommended action to meet the above requirement?

- **A.** 1. Enable Cross-Region Replication (CRR) in the S3 bucket to maintain a copy of all the S3 objects. 2. Set the DeletionPolicy for the RDS instance to Snapshot.
- **B.** 1. Set the DeletionPolicy on the S3 resource declaration in the CloudFormation template to Retain. 2. Set the RDS resource declaration DeletionPolicy to Snapshot.
- **C.** For both the RDS and S3 resource types on the CloudFormation template, set the DeletionPolicy to Retain.
- **D.** 1. Set the DeletionPolicy on the S3 resource to Snapshot. 2. Set the DeletionPolicy on the RDS resource to Snapshot.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** keep S3 photos and RDS summaries after stack delete

⚠️ **Watch:** S3 has no Snapshot policy

🧠 **Rule:** DeletionPolicy: Retain for S3, Snapshot for RDS.

### TD explanation

With the DeletionPolicy attribute, you can preserve or (in some cases) back up a resource when its stack is deleted. You specify a DeletionPolicy attribute for each resource that you want to control. If a resource has no DeletionPolicy attribute, AWS CloudFormation deletes the resource by default.

Note that this capability also applies to stack update operations that lead to resources being deleted from stacks, for example, if you remove the resource from the stack template and then update the stack with the template. This capability does not apply to resources whose physical instance is replaced during stack update operations. For example, if you edit a resource’s properties such that AWS CloudFormation replaces that resource during a stack update.
In this scenario, you need to keep the data on your S3 bucket and RDS which can be achieved by setting the DeletionPolicy of S3 to Retain and for RDS to use Snapshot.
Setting the DeletionPolicy on the S3 resource to Snapshot and for RDS resource to use Snapshot is incorrect because S3 does not support snapshots. It should be set to Retain.
For both the RDS and S3 resource types on the CloudFormation template, setting the DeletionPolicy to Retain is incorrect. Although you can set Retain on both the DeletionPolicy of the S3 bucket and the RDS database, this entails an unnecessary operating cost since the RDS database will still be running even if it is not used. Take note that the application is meant to run for just a month and once it has been concluded, nobody would be using it until the next contest next year. The RDS should be set to Snapshot.
Enabling Cross-Region Replication (CRR) in the S3 bucket to maintain a copy of all the S3 objects and setting the DeletionPolicy for the RDS instance to Snapshot is incorrect because even though your data will still be available in the other region because of the CRR, the current S3 bucket will still be deleted.

References:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html
https://aws.amazon.com/premiumsupport/knowledge-center/delete-cf-stack-retain-resources/

Check out this AWS CloudFormation Cheat Sheet:
https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q25"></a>

## Q25

A company has a hybrid cloud architecture where their on-premises data center and VPC are connected via multiple AWS Direct Connect ports in a single Link Aggregation Group (LAG). They have an on-premises patch management system that automatically applies the patches to the operating systems of their servers and file systems. You were given a task to synchronize the patch baselines being used on-premises to all of the EC2 instances in your VPC, as well as to automate the patching schedule.
Which of the following methods should you implement to meet the above requirement with the LEAST amount of effort?

- **A.** Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by setting up scheduled jobs using AWS Lambda and AWS Systems Manager Run Command.
- **B.** Use AWS Systems Manager Session Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by using the AWS Systems Manager Maintenance Windows.
- **C.** Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Install the SSM Agent to all of your instances and automate the patching schedule by using AWS Systems Manager Maintenance Windows.
- **D.** Use the AWS Systems Manager State Manager to automate the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define, which includes the OS patches that should be applied in each EC2 instance. Automate the patching schedule by using AWS Systems Manager Distributor, to package and distribute the required patches to your instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** sync on-prem patch baselines to EC2; schedule; least effort

⚠️ **Watch:** Session Manager isn't patching

🧠 **Rule:** Patch Manager + SSM Agent + Maintenance Windows.

### TD explanation

AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

AWS Systems Manager Maintenance Windows let you define a schedule for when to perform potentially disruptive actions on your instances such as patching an operating system, updating drivers, or installing software or patches. Each Maintenance Window has a schedule, a maximum duration, a set of registered targets (the instances that are acted upon), and a set of registered tasks. You can also specify dates that a Maintenance Window should not run before or after, and you can specify the international time zone on which to base the Maintenance Window schedule.
Therefore, the correct answer is: Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Install the SSM Agent to all of your instances and automate the patching schedule by using AWS Systems Manager Maintenance Windows.
The option that says: Use AWS Systems Manager Session Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by using the AWS Systems Manager Maintenance Windows is incorrect because the Session Manager is primarily used to comply with corporate policies that require controlled access to instances, strict security practices, and fully auditable logs with instance access details, but not for applying OS patches. Using the AWS Systems Manager Patch Manager is a more appropriate solution to implement.
The option that says: Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by setting up scheduled jobs using AWS Lambda and AWS Systems Manager Run Command is incorrect. Although it properly uses AWS Systems Manager Patch Manager, it is still better to use AWS Systems Manager Maintenance Windows instead of manually creating scheduled jobs using AWS Lambda and AWS Systems Manager Run Command. Take note that the scenario specifies that you have to meet the requirement with the LEAST amount of effort, which can be met by using the AWS Systems Manager Maintenance Windows feature. In addition, installing the SSM Agent to all of your instances is also required when using the AWS Systems Manager Patch Manager, which is not mentioned in this option.
The option that says: Use the AWS Systems Manager State Manager to automate the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define, which includes the OS patches that should be applied in each EC2 instance. Automate the patching schedule by using AWS Systems Manager Distributor, to package and distribute the required patches to your instances is incorrect because the AWS Systems Manager State Manager is primarily used as a secure and scalable configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define. This does not handle patch management, unlike AWS Systems Manager Patch Manager. With the State Manager, you can configure your instances to boot with a specific software at start-up; download and update agents on a defined schedule; configure network settings and many others, but not the patching of your EC2 instances.

References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

Check out this AWS Systems Manager Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q33"></a>

## Q33

A company has built an application that allows painters to upload photos of original creations. The app allows users from North America and European regions to browse the galleries and order chosen artworks. The application is hosted on a fixed set of Amazon EC2 instances in the us-east-1 region. Using mobile phones, the artists can scan and upload large, high-resolution images, which are stored in a centralized Amazon S3 bucket also in the same region. After the initial week of operation, the European artists are reporting slow performance when uploading images.
Which of the following is the best solution to improve the image upload process?

- **A.** Enable S3 Transfer Acceleration on the central S3 bucket. Use the s3-accelerate endpoint to upload the images.
- **B.** Increase the upload capacity by creating an AWS Global Accelerator endpoint in front of the EC2 instances. Create an Auto Scaling Group that can scale automatically based on the users' traffic.
- **C.** Enable multipart upload on S3 and redeploy the application to support it. This allows the transmission of separate parts of the image in parallel.
- **D.** Set the centralized S3 bucket as the custom origin on an Amazon CloudFront distribution. This will use CloudFront’s global edge network to improve the upload speed.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** European artists slow uploading to us-east-1 bucket

⚠️ **Watch:** CloudFront isn't an upload accelerator for S3 here

🧠 **Rule:** Long-distance uploads → S3 Transfer Acceleration.

### TD explanation

Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.

You might want to use Transfer Acceleration on a bucket for various reasons, including the following:
– You have customers that upload to a centralized bucket from all over the world.
– You transfer gigabytes to terabytes of data on a regular basis across continents.
– You are unable to utilize all of your available bandwidth over the Internet when uploading to Amazon S3.
You can enable Transfer Acceleration on a bucket in any of the following ways:
– Use the Amazon S3 console.
– Use the REST API PUT Bucket accelerate operation.
– Use the AWS CLI and AWS SDKs.
You can transfer data to and from the acceleration-enabled bucket by using one of the following s3-accelerate endpoint domain names:
- s3-accelerate.amazonaws.com – to access an acceleration-enabled bucket.
- s3-accelerate.dualstack.amazonaws.com – to access an acceleration-enabled bucket over IPv6. Amazon S3 dual-stack endpoints support requests to S3 buckets over IPv6 and IPv4.
You can point your Amazon S3 PUT object and GET object requests to the s3-accelerate endpoint domain name after you enable Transfer Acceleration. After Transfer Acceleration is enabled, it can take up to 20 minutes for you to realize the performance benefit. However, the accelerate endpoint will be available as soon as you enable Transfer Acceleration.
Therefore, the correct answer is: Enable S3 Transfer Acceleration on the central S3 bucket. Use the s3-accelerate endpoint to upload the images.
The option that says: Enable multipart upload on S3 and redeploy the application to support it. This allows the transmission of separate parts of the image in parallel is incorrect. Although multipart upload can improve the upload throughput to an S3 bucket, the European users are still limited on their Internet connection to the S3 bucket in the US region. S3 Transfer acceleration uses the AWS backbone network, which can optimize the transfer from far away regions.
The option that says: Set the centralized S3 bucket as the custom origin on an Amazon CloudFront distribution. This will use CloudFront’s global edge network to improve the upload speed is incorrect. CloudFront distribution is primarily designed for optimizing content delivery and content caching. Although CloudFront supports content uploads via POST, PUT, and other HTTP Methods, there is a limited connection timeout to the origin (60 seconds). If uploads take several minutes, the connection might get terminated. If you want to optimize performance when uploading large files to Amazon S3, it is recommended to use Amazon S3 Transfer Acceleration which can provide fast and secure transfers over long distances. Transfer Acceleration uses Amazon CloudFront’s globally distributed edge locations.
The option that says: Increase the upload capacity by creating an AWS Global Accelerator endpoint in front of the EC2 instances. Create an Auto Scaling Group that can scale automatically based on the users’ traffic is incorrect. Although AWS Global Accelerator can typically help increase network availability and performance, it won’t have an effect on this scenario because the images are directly uploaded to the S3 bucket. Increasing the number of EC2 instances does not necessarily improve the S3 upload speeds. Even if the application is configured to use the EC2 instance as a temporary storage for the images, the upload experience of the users will not improve because they are uploading from a different continent.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration-examples.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html
https://aws.amazon.com/premiumsupport/knowledge-center/s3-upload-large-files/

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q36"></a>

## Q36

A company is running thousands of virtualized Linux and Microsoft Windows servers on its on-premises data center. The virtual servers host a range of Java and PHP applications that use MySQL and Oracle databases. There are also several department services hosted on an external data center. The company uses SAN storage to provide iSCSI disks to its physical servers. The company wants to migrate its data center to the AWS Cloud, but the technical documentation of the systems is incomplete and outdated. The Solutions Architect was tasked to analyze the current environment and estimate the cost of migrating the resources to the cloud.
Which of the following should the Solutions Architect do to effectively plan the cloud migration? (Select THREE.)

- **A.** Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket.
- **B.** Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.
- **C.** Use the AWS Transform discovery tool to gather information about the running virtual machines and running applications inside the servers.
- **D.** Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.
- **E.** Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud.
- **F.** Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C, D (you answered correctly)

🔑 **Key words:** thousands of servers; outdated docs; estimate migration cost (Select THREE)

⚠️ **Watch:** Inspector/X-Ray aren't discovery tools

🧠 **Rule:** Transform discovery + assessment jobs + CART readiness.

### TD explanation

The scenario requires tools of services that will help to effectively plan the cloud migration, so the answers should be focused on planning.
AWS Transform is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.
With AWS Transform, you can:
– Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS
– Migrate VMware workloads to Amazon EC2
– Modernize .NET applications to Linux-ready cross-platform .NET
– Assess workloads for migration readiness

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.
The AWS Transform discovery tool assists you in automatically discovering the server inventory within your organization in preparation for migration. This tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To utilize the discovery tool, you need to configure one or more discovery sources, allow the tool to run, and then review the results displayed in the Discovered Inventory pane.
Once you configure a discovery source, the tool will begin collecting information. The time required for the discovery tool to completely analyze your network depends on the size of your environment. For businesses utilizing a directional migration approach, you can leverage the Migration Portfolio Assessment (MPA) files generated by the tool after the server collection is completed.
The AWS Cloud Adoption Readiness Tool (CART) helps organizations of all sizes develop efficient and effective plans for cloud adoption and enterprise cloud migrations. This 16-question online survey and assessment report detail your cloud migration readiness across six perspectives, including business, people, process, platform, operations, and security. Once you complete a CART survey, you can provide your contact details to download a customized cloud migration assessment that charts your readiness and what you can do to improve it. This tool is designed to help organizations assess their progress with cloud adoption and identify gaps in organizational skills and processes.
AWS Transform assessments evaluate the cost, feasibility, and business value of migrating on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinement through chat.
You can apply migration assessments for several objectives:
– Get cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx
– Receive automated right-sizing recommendations
– Assess business value and sustainability impact
– Compare multiple migration scenarios side by side
– Refine assessments interactively through chat
– Generate executive presentations and detailed reports
Therefore, the correct answers are:
– Use the AWS Transform Discovery Tool to gather information about the running virtual machines and running applications inside the servers.
– Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.
– Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.
The option that says: Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud is incorrect because MGN is primarily used for the actual migration of your on-premises virtual machines to the AWS Cloud and not for planning. Take note that in the scenario, the Solutions Architect was tasked to analyze the existing on-premises architecture first before doing the actual migration to AWS.
The option that says: Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration is incorrect because AWS X-Ray is typically used to debug production and distributed applications, such as those built using a microservices architecture. This is not helpful for planning the migration.
The option that says: Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket is incorrect because Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. This is not helpful for assessing the applications on the on-premises data center.

References:
https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html
https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html
https://docs.aws.amazon.com/transform/latest/launchguide/resources.html
https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html

Check out this AWS Migration Strategies Cheat Sheet:
https://tutorialsdojo.com/aws-migration-strategies-the-7-rs/

</details>

<a id="q60"></a>

## Q60

An organization is migrating its on-premises web application to AWS. The application comprises a Java-based backend and a NoSQL MongoDB database. Due to constraints, the application cannot be modified during the migration process, and the migrated solution must maintain an architecture similar to the on-premises setup. Additionally, the application requires high availability for both the backend and the database to ensure continuous operation.
Which solution will meet these requirements while adhering to the constraints?

- **A.** Containerize the Java application using AWS App2Container and deploy it on Amazon Elastic Kubernetes Service (EKS). Use Amazon DynamoDB for the database layer to achieve high availability.
- **B.** Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Use Amazon DocumentDB (with MongoDB compatibility) in a single Availability Zone deployment to host the MongoDB database.
- **C.** Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Migrate the MongoDB database to Amazon DocumentDB (with MongoDB compatibility) across multiple Availability Zones.
- **D.** Use AWS Elastic Beanstalk to deploy the Java application and migrate the MongoDB database to Amazon Aurora with multiple read replicas across different Availability Zones.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** Java + MongoDB; no code change; HA

⚠️ **Watch:** DynamoDB/Aurora require code changes

🧠 **Rule:** Multi-AZ EC2 ASG + DocumentDB across AZs.

### TD explanation

Amazon DocumentDB (with MongoDB Compatibility) is a managed NoSQL database service designed to seamlessly support MongoDB workloads. It allows the organization to migrate its existing MongoDB database without requiring application changes, as it is compatible with MongoDB’s JSON-like storage format, query language, and drivers. This service ensures high availability by deploying data across three Availability Zones by default, providing fault tolerance and durability. If a primary instance fails, Amazon DocumentDB automatically promotes a replica to primary, ensuring continuous operations without manual intervention. This makes it an ideal choice for the organization’s needs, as it adheres to the requirement of high availability for the database layer and maintains architectural compatibility.

Amazon EC2 instances: EC2 (Elastic Compute Cloud) provides scalable computing capacity in the AWS cloud. By deploying the Java application on EC2 instances, you retain the flexibility to run custom configurations and setups that closely match your on-premises environment.
An Auto Scaling group manages the fleet of Amazon EC2 instances hosting the Java-based backend application. It ensures that the correct number of instances are always running to handle varying levels of application traffic. By dynamically scaling up during peak traffic and scaling down during lower demand, Auto Scaling optimizes costs while maintaining performance. Moreover, it replaces unhealthy instances automatically, ensuring that the backend application remains operational even in the event of instance failures. This makes Auto Scaling crucial for providing the required scalability and fault tolerance for the application.

Multiple Availability Zones are leveraged to ensure high availability and fault tolerance for both the backend and database. Resources are deployed across at least two physically separate zones within the AWS Region. This setup ensures that the application and database remain operational even if one Availability Zone experiences an outage. The distribution of resources across zones also improves resiliency and fault tolerance while enhancing overall application availability. By deploying in multiple zones, the organization can maintain a highly available architecture similar to the on-premises setup, with the added benefit of AWS’s robust infrastructure.
Hence, the correct answer is: Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Migrate the MongoDB database to Amazon DocumentDB (with MongoDB compatibility) across multiple Availability Zones.
The option that says: Containerize the Java application using AWS App2Container and deploy it on Amazon Elastic Kubernetes Service (EKS). Use Amazon DynamoDB for the database layer to achieve high availability is incorrect because it primarily involves significant changes to the application’s architecture, particularly replacing MongoDB with DynamoDB, which is a different type of database.
The option that says: Use AWS Elastic Beanstalk to deploy the Java application and migrate the MongoDB database to Amazon Aurora with multiple read replicas across different Availability Zones is incorrect because it changes the database from MongoDB to Amazon Aurora, which is a relational database service. This would not maintain the same architecture as the on-premises setup.
The option that says: Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Use Amazon DocumentDB (with MongoDB compatibility) in a single Availability Zone deployment to host the MongoDB database is incorrect because while it uses Amazon DocumentDB, it only deploys it in a single Availability Zone, which does not meet the high availability requirement for the database.

References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html
https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html

Check out this Amazon DocumentDB Cheat Sheet:
https://tutorialsdojo.com/amazon-documentdb/

</details>
