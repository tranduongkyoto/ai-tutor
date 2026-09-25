# TD Set 5 — Correct Answer Review (31 questions)

Source: `TD_SAP_Timed_Set5_Full.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/⚠️/🧠 are study notes. Wrong answers: `td_set_5_review.md`.

## Purpose

Confirm each correct answer was **knowledge, not a guess**. Answer again without looking; if you can't justify why every wrong option fails, tick **Guessed** and treat it as a wrong answer.

## ⚠️ Inconsistent concepts (right here, wrong elsewhere in Set 5)

| Right | Wrong | Concept |
|---|---|---|
| Q44 | Q16 | CUR in management account + QuickSight |
| Q60 | Q10 | AWS Transfer Family for SFTP |
| Q52 | Q33 | AWS Transform discovery |
| Q46 | Q4, Q32 | VM Import/Export + FSx for Windows + DataSync |
| Q40 | Q5, Q58 | RDS Proxy for Lambda connection pressure |
| Q11 | Q8 | Compute Optimizer |

These are partial knowledge — review each pair together.

## Tracker

| Group | Q | Guessed? | Pass 1 | Pass 2 |
|---|---|---|---|---|
| A | [Q11](#q11) | ☐ | ☐ | ☐ |
| A | [Q25](#q25) | ☐ | ☐ | ☐ |
| A | [Q39](#q39) | ☐ | ☐ | ☐ |
| A | [Q59](#q59) | ☐ | ☐ | ☐ |
| A | [Q60](#q60) | ☐ | ☐ | ☐ |
| A | [Q65](#q65) | ☐ | ☐ | ☐ |
| A | [Q66](#q66) | ☐ | ☐ | ☐ |
| B | [Q26](#q26) | ☐ | ☐ | ☐ |
| B | [Q41](#q41) | ☐ | ☐ | ☐ |
| B | [Q43](#q43) | ☐ | ☐ | ☐ |
| B | [Q44](#q44) | ☐ | ☐ | ☐ |
| B | [Q45](#q45) | ☐ | ☐ | ☐ |
| B | [Q70](#q70) | ☐ | ☐ | ☐ |
| B | [Q71](#q71) | ☐ | ☐ | ☐ |
| B | [Q75](#q75) | ☐ | ☐ | ☐ |
| C | [Q53](#q53) | ☐ | ☐ | ☐ |
| D | [Q2](#q2) | ☐ | ☐ | ☐ |
| D | [Q46](#q46) | ☐ | ☐ | ☐ |
| D | [Q47](#q47) | ☐ | ☐ | ☐ |
| D | [Q52](#q52) | ☐ | ☐ | ☐ |
| E | [Q34](#q34) | ☐ | ☐ | ☐ |
| E | [Q40](#q40) | ☐ | ☐ | ☐ |
| E | [Q50](#q50) | ☐ | ☐ | ☐ |
| E | [Q56](#q56) | ☐ | ☐ | ☐ |
| E | [Q64](#q64) | ☐ | ☐ | ☐ |
| F | [Q3](#q3) | ☐ | ☐ | ☐ |
| F | [Q6](#q6) | ☐ | ☐ | ☐ |
| F | [Q7](#q7) | ☐ | ☐ | ☐ |
| F | [Q17](#q17) | ☐ | ☐ | ☐ |
| F | [Q27](#q27) | ☐ | ☐ | ☐ |
| F | [Q37](#q37) | ☐ | ☐ | ☐ |

---

# Group A — Managed service / operations (7)

<a id="q11"></a>

## Q11

A large company has thousands of Amazon EC2 instances with Amazon Elastic Block Storage (EBS) in its AWS account. The instances are spread across different regions and multiple VPCs. Hundreds of these are very large, high-memory instances that host database clusters in active/passive configurations. The company wants to analyze how efficiently the business is using these resources and take appropriate actions based on the results. Currently, the company has no baseline pattern on how the applications utilize the databases.

Which of the following options is the recommended action to meet the company requirements in a cost-effective manner?

- **A.** Enable Amazon CloudWatch detailed monitoring for all Amazon EC2 instances to enable monitoring of its memory and EBS volumes. Create a new dashboard on Amazon CloudWatch to view metrics based on CPU, Memory, and Disk usage. Resize the EC2 instances based on the identified usage patterns and peak loads on the metrics.
- **B.** Create visualizations associated with Amazon CloudWatch metrics of the CPU, Memory, and EBS utilization of the Amazon EC2 instances. Set up a new monitoring dashboard using AWS Systems Manager OpsCenter. Review this dashboard to identify usage patterns and peak loads, then rightsize the EC2 instances accordingly.
- **C.** Ensure that the Amazon CloudWatch agent is installed on all Amazon EC2 instances. In the company AWS account, opt-in for the AWS Compute Optimizer and wait for at least 12 hours. Rightsize the EC2 instances based on the recommendations from the Compute Optimizer service.
- **D.** Enable the extended features of AWS Trusted Advisor and the AWS Systems Manager Incident Manager by signing up the company AWS account with the AWS Enterprise Support plan. Wait for at least 12 hours for Trusted Advisor to populate recommendations. Resize the EC2 instances based on its recommendations to save on cost.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** thousands of EC2 incl. high-memory; analyze efficiency; act on recommendations

⚠️ **Watch:** Memory metrics need CloudWatch agent — Compute Optimizer alone sees CPU only. ⚠️ Missed same service in Q8

🧠 **Rule:** Right-sizing → Compute Optimizer (opt-in, ≥12h data) + CloudWatch agent for memory.

### TD explanation

AWS Compute Optimizer helps you choose the optimal AWS Compute resources for your workloads. Compute Optimizer delivers intuitive and actionable recommendations to help you identify the optimal AWS Compute resources. When you access the AWS Compute Optimizer console for the first time, you are asked to opt-in, using the account that you’re signed in with, before you can use the service.

After you opt-in, Compute Optimizer starts to scan your AWS infrastructure and generates recommendations. It may take up to 12 hours for Compute Optimizer to deliver recommendations for all supported AWS Compute resources.

You can use the dashboard in the Compute Optimizer console to evaluate and prioritize the optimization opportunities for the supported resource types in your account. The findings section displays the findings classifications count and percentage for resource types in your account. Compute Optimizer classifies EC2 instances, Auto Scaling groups, and Lambda functions as under-provisioned, over-provisioned, or optimized. Amazon EBS volumes are classified as not optimized or optimized. You can improve your recommendation by installing the Amazon CloudWatch agent to enable memory metrics for your EC2 instances.

Therefore, the correct answer is: Ensure that the Amazon CloudWatch agent is installed on all Amazon EC2 instances. In the company AWS account, opt-in for the AWS Compute Optimizer and wait for at least 12 hours. Rightsize the EC2 instances based on the recommendations from the Compute Optimizer service. AWS Compute Optimizer can show recommendations for sizing your EC2 instances, Auto Scaling groups, Lambda functions, and EBS volumes.

The option that says: Create visualizations associated with Amazon CloudWatch metrics of the CPU, Memory, and EBS utilization of the Amazon EC2 instances. Set up a new monitoring dashboard using AWS Systems Manager OpsCenter. Review this dashboard to identify usage patterns and peak loads, then rightsize the EC2 instances accordingly is incorrect. The AWS Systems Manager OpsCenter service simply enables you to view, investigate, and resolve operational work items (OpsItems) related to AWS resources. It is not intended to be used for analyzing EC2 usage efficient patterns and it does not provide recommendations for EC2 sizing.

The option that says: Enable Amazon CloudWatch detailed monitoring for all Amazon EC2 instances to enable monitoring of its memory and EBS volumes. Create a new dashboard on Amazon CloudWatch to view metrics based on CPU, Memory, and Disk usage. Resize the EC2 instances based on the identified usage patterns and peak loads on the metrics is incorrect. This may be possible however you will have to manually review the dashboards and graphs for each instance. You don’t have automated recommendations with this approach.

The option that says: Enable the extended features of AWS Trusted Advisor and the AWS Systems Manager Incident Manager by signing up the company AWS account with the AWS Enterprise Support plan. Wait for at least 12 hours for Trusted Advisor to populate recommendations. Resize the EC2 instances based on its recommendations to save on cost is incorrect. Recommendations for rightsizing your EC2 instances is actually a feature of AWS Compute Optimizer, not AWS Trusted Advisor. In addition, the AWS Systems Manager Incident Manager service is totally separate from AWS Trusted Advisor so upgrading to the AWS Enterprise Support plan is not a prerequisite in order to use it.

 

References:

https://aws.amazon.com/compute-optimizer/getting-started/

https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html

https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/

 

Check out this Amazon EC2 Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

</details>

<a id="q25"></a>

## Q25

A healthcare insurance company plans to implement a blockchain-based system to store patient records using Amazon Managed Blockchain. The system must allow patient records to be exchanged among various private entities while ensuring that the data is securely stored, transparent, and immutable.

What solution would meet these requirements?

- **A.** Use AWS Lambda functions to store a hash of each PII data on an Amazon Managed Blockchain network. Store the PII data off-chain in an Amazon DynamoDB table.
- **B.** Store all patient data on an Amazon Managed Blockchain network. Use EC2 Arbitrum Nodes to encrypt and decrypt data before they are stored in the blockchain network. Use an Application Load Balancer (ALB) to access the EC2 nodes in an HTTPS endpoint.
- **C.** Store all patient data on an Amazon Managed Blockchain network.
- **D.** Store only the patient’s name and ID on an Amazon Managed Blockchain network. Store all other PII data off-chain in an Amazon DynamoDB table.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** Managed Blockchain; patient PII; transparent + immutable; private entities

⚠️ **Watch:** Never store raw PII on-chain (immutable = can't delete)

🧠 **Rule:** Blockchain + PII → hash on-chain, PII off-chain (DynamoDB).

### TD explanation

Amazon Managed Blockchain is a fully managed service that helps build and manage Web3 applications with blockchain frameworks. With Amazon Managed Blockchain, you can securely transact and share data on a distributed and immutable ledger.

You can deploy a REST API to provide a simple interface to read and write to the blockchain network. One implementation of building REST APIs is with a serverless architecture using AWS Lambda and Amazon API Gateway. Lambda has built-in fault tolerance and provides high availability for the service itself and the functions it operates, allowing developers to focus on developing the business logic. An API Gateway provides a layer of security to AWS Lambda, allowing for features such as authentication and rate-limiting.

In this scenario, sensitive patient data is processed in two main environments: on-chain and off-chain. The on-chain component involves storing a hashed version of the Personally Identifiable Information (PII), such as patient names, on Amazon Managed Blockchain. This ensures data integrity and immutability, as each hash is a unique representation of the data that cannot be altered.

For the off-chain component, the actual PII is stored in Amazon DynamoDB. This approach leverages DynamoDB’s scalability and fast access to secure and manage sensitive patient data. The reference to the on-chain hash ensures that any data retrieved can be verified against its immutable blockchain record.

AWS Lambda functions serve as the intermediary that processes the PII. First, they generate a hash of the data and store it on-chain in the blockchain. Second, Lambda functions encrypt the PII before storing it off-chain in DynamoDB. They manage the encryption process using secure algorithms and AWS Key Management Service (KMS) for key management, ensuring that the data is protected throughout its lifecycle.

Therefore, the correct answer is: Use AWS Lambda functions to store a hash of each PII data on an Amazon Managed Blockchain network. Store the PII data off-chain in an Amazon DynamoDB table.

The option that says: Store all patient data on an Amazon Managed Blockchain network is incorrect. This approach could lead to privacy concerns since blockchains are inherently transparent and could be accessible to all participants in the network. This approach may not comply with regulations such as HIPAA in the healthcare industry, which require strict privacy controls over patient information.

The option that says: Store only the patient’s name and ID on an Amazon Managed Blockchain network. Store all other PII data off-chain in an Amazon DynamoDB table is incorrect. Patient names and IDs are still considered personally identifiable information (PII) and are subject to data protection regulations. It is best practice not to store these in plaintext on blockchain.

The option that says: Store all patient data on an Amazon Managed Blockchain network. Use EC2 Arbitrum Nodes to encrypt and decrypt data before they are stored in the blockchain network. Use an Application Load Balancer (ALB) to access the EC2 nodes in an HTTPS endpoint is incorrect. Storing all patient data directly is not the best practice due to privacy and security regulations. Also, using Arbitrum is not appropriate in the context of Amazon Managed Blockchain, which already provides support for the underlying infrastructure that utilizes blockchain technology. Using an ALB with the EC2 nodes is also incorrect, as these do not provide any implementation of proper authentication and authorization for data access.

 

References:

https://aws.amazon.com/managed-blockchain/faqs

https://aws.amazon.com/blogs/database/building-a-serverless-blockchain-application-with-amazon-managed-blockchain/

</details>

<a id="q39"></a>

## Q39

A company is using a custom software framework to write its web application. The framework is needed as a dependency in order for the application to work. Currently, the framework is installed by an Amazon EC2 user data script and takes about 15-20 minutes to complete. This process has become a bottleneck in the application deployment process. The developers want to have a faster deployment time in order to deliver more frequent application updates.

Which of the following implementations can improve the deployment process?

- **A.** Compress the custom software framework installation files to make them smaller and store them in an Amazon S3 bucket. Update the user data script to pull the installation files from the S3 bucket.
- **B.** Create an AWS Elastic Beanstalk environment to deploy the application.
- **C.** Create an AWS Systems Manager Automation task and use the AWS-CreateImage document to build a custom AMI with the framework installed. Use this AMI as a baseline for application deployments.
- **D.** Create a pipeline in AWS CodePipeline to parallelize the installation of the software framework and the application during the deployment.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** framework install 15–20 min in user data; faster deployment

⚠️ **Watch:** Don't keep installing at boot

🧠 **Rule:** Slow boot bootstrap → golden AMI (SSM Automation AWS-CreateImage / Image Builder).

### TD explanation

AWS Systems Manager (formerly known as SSM) is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects.

A Systems Manager Automation runbook defines the automation (the actions that Systems Manager performs on your managed instances and AWS resources). Automation includes several pre-defined runbooks that you can use to perform common tasks like restarting one or more Amazon EC2 instances or creating an Amazon Machine Image (AMI). You can create your own runbooks as well. Runbooks use JavaScript Object Notation (JSON) or YAML, and they include steps and parameters that you specify.

Therefore, the correct answer is: Create an AWS Systems Manager Automation task and use the AWS-CreateImage document to build a custom AMI with the framework installed. Use this AMI as a baseline for application deployments. Creating a custom AMI with the software framework pre-installed will significantly speed up the application deployment process. 

The option that says: Compress the custom software framework installation files to make them smaller and store them in an Amazon S3 bucket. Update the user data script to pull the installation files from the S3 bucket is incorrect. Downloading the software framework may be faster from the S3 bucket but extracting the zip file and installation will still take a lot of time. 

The option that says: Create a pipeline in AWS CodePipeline to parallelize the installation of the software framework and the application during the deployment is incorrect. The software framework is a dependency of the application so the software framework needs to be installed first. 

The option that says: Create an AWS Elastic Beanstalk environment to deploy the application is incorrect because while Elastic Beanstalk does simplify the deployment process, it doesn’t address the issue of the time it takes to install the framework.

 

References:

https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-ami-automation/

https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html

 

Check out the AWS Systems Manager Cheat Sheet:

https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q59"></a>

## Q59

A company hosts a .NET REST API in AWS. Currently, the business logic of the API is deployed on three EC2 instances distributed across different Availability Zones. The application is monolithic in nature, and some functions tend to consume more resources than others during operation. Clients interact with the API by calling its domain name. This domain is registered with Route 53, which uses a multi-value answer policy to route each request to one of the available EC2 instances.

The application experiences non-constant traffic throughout the day and becomes unresponsive during periods of peak demand. A solutions architect is tasked with redesigning the architecture to be more cost-effective and to have the least amount of operational overhead.

Which solution will meet these requirements?

- **A.** Register the existing EC2 instances in an Auto Scaling group and use it as a target for an Application Load Balancer (ALB). Configure a dynamic scaling policy based on the ALB’s RequestCountPerTarget metric. Update Route 53 to direct traffic to the ALB’s endpoint.
- **B.** Create a custom routing accelerator in AWS Global Accelerator, targeting the subnets housing the EC2 instances. Place the EC2 instances into an Auto Scaling group with a policy that scales based on average CPU utilization. Update the Route 53 records to resolve to the IP address provided by the Global Accelerator.
- **C.** Move the API on an Amazon Elastic Kubernetes Service (EKS) cluster that uses EC2 Spot Instances. Configure a Kubernetes Ingress controller for request routing and create a corresponding ingress resource. Update Route 53 to point to the external IP provided by the Ingress controller.
- **D.** Split the API into multiple AWS Lambda functions to handle different components. Provision an Amazon API Gateway REST API to act as the interface for these Lambda functions. Configure a custom domain in API Gateway, then update the Route 53 record to map to this custom domain.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** .NET monolith; uneven resource use; domain in Route 53; scale per function

⚠️ **Watch:** Keep the domain — custom domain on API Gateway

🧠 **Rule:** Split monolith by function → Lambda per component + API Gateway + custom domain.

### TD explanation

AWS Lambda is a serverless compute service that lets you run your code without provisioning or managing servers. It executes your code only when needed and scales automatically, from a few requests per day to thousands per second. Amazon API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs at any scale. It acts as a “front door” for applications to access data, business logic, or functionality from your backend services, such as Lambda functions, web applications, or real-time communication services. In combination, Lambda and API Gateway provide a powerful, scalable, and cost-effective solution to build and expose APIs without the need for server management.

In the scenario, by transitioning from monolithic to microservices using multiple AWS Lambda functions managed through Amazon API Gateway, the architecture becomes serverless. This significantly reduces operational overhead and costs for fluctuating traffic as you pay only for what you use. Additionally, breaking down the monolithic API into Lambda functions allows for fine-grained scalability. Unlike in a monolithic architecture where the entire application must scale as a unit, individual Lambda functions can scale independently based on the demand for that specific function.

Hence, the correct answer in this scenario is: Split the API into multiple AWS Lambda functions to handle different components. Provision an Amazon API Gateway REST API to act as the interface for these Lambda functions. Configure a custom domain in API Gateway, then update the Route 53 record to map to this custom domain.

The option that says: Register the existing EC2 instances in an Auto Scaling group and use it as a target for an Application Load Balancer (ALB). Configure a dynamic scaling policy based on the ALB’s RequestCountPerTarget metric. Update Route 53 to direct traffic to the ALB’s endpoint is incorrect. The use of EC2 instances to host a monolithic application presents a limitation in that you cannot scale individual components independently. If a function within the application overwhelms the resources of one of the EC2 instances, you’re forced to scale the entire application by adding more EC2 instances. Thus, this approach is less cost-effective.

The option that says: Create a custom routing accelerator in AWS Global Accelerator, targeting the subnets housing the EC2 instances. Place the EC2 instances into an Auto Scaling group with a policy that scales based on average CPU utilization. Update the Route 53 records to resolve to the IP address provided by the Global Accelerator is incorrect. AWS Global Accelerator is primarily used for improving the availability and performance of applications with global users by routing user traffic through AWS’s network infrastructure. However, unless the application has a global user base that would benefit from such optimized routing, incorporating Global Accelerator could add unnecessary complexity and cost.

The option that says: Move the API on an Amazon Elastic Kubernetes Service (EKS) cluster that uses EC2 Spot Instances. Configure a Kubernetes Ingress controller for request routing and create a corresponding ingress resource. Update Route 53 to point to the external IP provided by the Ingress controller is incorrect. Deploying the API on an Amazon EKS cluster would introduce considerable operational complexity. Kubernetes is powerful but has a steep learning curve and high operational overhead, making it less aligned with the goal of minimizing operational tasks. Moreover, although using Spot Instances can be cost-effective, they’re not suitable for all types of workloads, especially for applications that cannot tolerate disruptions.

 

References:

https://aws.amazon.com/blogs/compute/migrating-a-monolithic-net-rest-api-to-aws-lambda/

https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html

 

Check out these AWS Lambda and Amazon API Gateway Cheat Sheets:

https://tutorialsdojo.com/aws-lambda/

https://tutorialsdojo.com/amazon-api-gateway/

</details>

<a id="q60"></a>

## Q60

An advertising company has terabytes of data on its Amazon S3 data lake. Its partner companies upload customer preference data over a custom SFTP server every night. The SFTP URL is reachable via the Amazon Route 53 domain name sftp.tutorialsdojo.com. It is hosted on an Amazon EC2 instance in a public subnet inside a VPC. There is a cron job script on the ec2 instance that sends the uploaded files from the SFTP server to the Amazon S3 data lake.

Which of the following implementations will improve the reliability and scalability of the SFTP server?

- **A.** Create a TCP listener on a Network Load Balancer (NLB) and place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the NLB domain name.
- **B.** Use AWS Transfer for SFTP service instead to serve as the SFTP server. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the server endpoint hostname.
- **C.** Create an HTTPS listener on an Application Load Balancer (ALB) and place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the ALB domain name.
- **D.** Migrate the SFTP server to an AWS Storage Gateway file gateway and expose its endpoint URL. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the storage gateway endpoint.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** custom SFTP on EC2 + cron to S3; reduce management

⚠️ **Watch:** ⚠️ Same service you missed in Q10 (VPC endpoint + EIP detail)

🧠 **Rule:** SFTP to S3 → AWS Transfer Family; point Route 53 record at server endpoint.

### TD explanation

AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services. AWS Transfer Family supports transferring data from or to the following AWS storage services – Amazon Simple Storage Service (Amazon S3) storage and Amazon Elastic File System (Amazon EFS) Network File System (NFS) file system.

AWS Transfer Family supports transferring data over the following protocols:

-Secure Shell (SSH) File Transfer Protocol (SFTP) (AWS Transfer for SFTP)

-File Transfer Protocol Secure (FTPS) (AWS Transfer for FTPS)

-File Transfer Protocol (FTP) (AWS Transfer for FTP)

Common use cases for Transfer Family with Amazon S3 are the following:

-Data lakes in AWS for uploads from third parties such as vendors and partners.

-Subscription-based data distribution with your customers.

-Internal transfers within your organization.

AWS Transfer Family supports up to 3 Availability Zones and is backed by an auto scaling, redundant fleet for your connection and transfer requests. With Transfer Family, you get access to a file transfer protocol-enabled server in AWS without the need to run any server infrastructure. You can use this service to migrate your file transfer-based workflows to AWS while maintaining your end users’ clients and configurations as is. You first associate your hostname with the server endpoint, then add your users and provision them with the right level of access. After you do this, your users’ transfer requests are serviced directly out of your Transfer Family server endpoint.

Therefore, the correct answer is: Use AWS Transfer for SFTP service instead to serve as the SFTP server. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the server endpoint hostname. This is a fully managed, highly scalable solution for hosting SFTP services in AWS. 

The option that says: Create a TCP listener on a Network Load Balancer (NLB), place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the NLB domain name is incorrect. This is possible to implement, however, it will require unnecessary work and configuration to set up correctly. Using the AWS Transfer for SFTP service is designed for these types of scenarios.

The option that says: Create an HTTPS listener on an Application Load Balancer (ALB), place an Auto Scaling group of Amazon EC2 instances behind it to host the SFTP service. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the ALB domain name is incorrect. The SFTP service uses the TCP protocol so an HTTPS listener on an ALB will not work in this scenario. 

The option that says: Migrate the SFTP server to an AWS Storage Gateway file gateway and expose its endpoint URL. Update the Amazon Route 53 record to point the sftp.tutorialsdojo.com URL to the storage gateway endpoint is incorrect. The AWS Storage Gateway file gateway is ideal for on-premises scenarios requiring data to be sent to AWS. There is no exposed SFTP endpoint for the file gateway. 

 

References:

https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html

https://docs.aws.amazon.com/transfer/latest/userguide/how-aws-transfer-works.html

https://docs.aws.amazon.com/transfer/latest/userguide/transfer-file.html

 

Check out this AWS Transfer Family Cheat Sheet:

https://tutorialsdojo.com/aws-transfer-family/

</details>

<a id="q65"></a>

## Q65

A startup develops a new web application that manages job listings for contractors and seasonal workers. The application source code is stored on a GitHub repository. For continuous integration, the developers trigger a pipeline on AWS CodePipeline. This pipeline includes a build stage that generates an artifact that is sent to an Amazon S3 bucket. The developers want to improve this process and have requested the solutions architect to create a strategy that meets the following requirements:

– Create a pipeline to accommodate Feature-Driven Development (FDD) process for the app

– Feature development must not affect the existing production application

– Must include a stage for continuous unit testing

– Create separate development and production artifacts

– Maintain the capability of integrating development and production code.

Which of the following options is the recommended solution to meet the company’s requirements?

- **A.** Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage for AWS CodeBuild to run unit testing and stage the generated artifacts in an S3 bucket in a separate testing AWS account.
- **B.** Create a new repository in GitHub for features development. Use Amazon CodeGuru to review and improve your code. Then, use the commits on this repo as triggers for AWS CodeBuild to build and test the artifacts. Use AWS CodeDeploy to stage the artifacts on a separate S3 bucket in the production AWS account.
- **C.** Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage that will trigger AWS Lambda functions to perform unit testing on the generated artifacts. Use AWS CodeDeploy to stage the artifacts on an S3 bucket in a separate testing AWS account.
- **D.** Create a new pipeline in Jenkins that is triggered by the “feature” tags from GitHub. Add a stage that will run unit testing on the generated artifacts. Send the artifacts to a staging S3 bucket in a separate AWS account using the AWS Well-Architected Tool.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** GitHub + CodePipeline; test feature branch separately

⚠️ **Watch:** Don't mix test artifacts with prod pipeline

🧠 **Rule:** Branch-based testing → separate pipeline per branch + CodeBuild tests + separate test account.

### TD explanation

AWS CodePipeline is a continuous delivery service that you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

AWS CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers.

You can automate your release process by using AWS CodePipeline to test your code and run your builds with AWS CodeBuild. You can use the AWS suite of CI/CD services to compile, build, and install a version-controlled Java application onto a set of Amazon Elastic Compute Cloud (Amazon EC2) Linux instances via a fully automated and secure pipeline. With these tools, you can promote a code commit or change to pass through various automated stage gates all the way from development to production environments across AWS accounts.

The following diagram illustrates the workflow:

– A change or commit to the code in the GitHub repository triggers CodePipeline through a webhook event.

– The pipeline downloads the code from the GitHub repository, initiates the Build and Test action using CodeBuild, and securely saves the built artifact on the S3 bucket.

– If the preceding step is successful, the pipeline triggers the Deploy in Dev action using CodeDeploy and deploys the app in the dev account.

– If successful, the pipeline triggers the Deploy in Prod action using CodeDeploy and deploys the app in the prod account.

Therefore, the correct answer is: Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage for AWS CodeBuild to run unit testing and stage the generated artifacts in an S3 bucket in a separate testing AWS account.

The option that says: Create a separate pipeline on CodePipeline that is triggered by the “feature” branch from GitHub. Add a stage that will trigger AWS Lambda functions to perform unit testing on the generated artifacts. Use AWS CodeDeploy to stage the artifacts on an S3 bucket in a separate testing AWS account is incorrect. This is possible; however, it is not necessary to write Lambda code for unit testing. You just need to include the tests on the CodeBuild stage, which will perform the unit testing.

The option that says: Create a new pipeline in Jenkins that is triggered by the “feature” tags from GitHub. Add a stage that will run unit testing on the generated artifacts. Send the artifacts to a staging S3 bucket in a separate AWS account using the AWS Well-Architected Tool is incorrect. Using a separate Jenkins instance to run your pipeline is not recommended. AWS CodePipeline is an AWS-managed service that can automate code builds, unit testing, and deployments on your behalf. Moreover, the AWS Well-Architected Tool simply allows you to monitor the status of multiple workloads across your organization and helps you understand potential risks. This is not meant to send artifacts to a staging S3 bucket located in a separate AWS account.

The option that says: Create a new repository in GitHub for features development. Use Amazon CodeGuru to review and improve your code. Then, use the commits on this repo as triggers for AWS CodeBuild to build and test the artifacts. Use AWS CodeDeploy to stage the artifacts on a separate S3 bucket in the production AWS account is incorrect. You don’t need to create a separate repository for your feature development. This will just duplicate your GitHub storage and can add complexity to your deployments. It is recommended to create a feature branch instead and use it to test and deploy new features. Moreover, while CodeGuru can help improve code quality, it’s not explicitly required to meet the stated requirements. The scenario doesn’t mention the need for code review or performance optimization, which are the primary functions of CodeGuru. Therefore, while CodeGuru could be beneficial in a general sense for improving code quality, it’s not strictly necessary based on the specific requirements given in the question.

 

References:

https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html

https://aws.amazon.com/about-aws/whats-new/2018/05/aws-codepipeline-supports-push-events-from-github-via-webhooks/

https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html

 

Check out these AWS CodePipeline and AWS CodeBuild Cheat Sheets:

https://tutorialsdojo.com/aws-codepipeline/

https://tutorialsdojo.com/aws-codebuild/

</details>

<a id="q66"></a>

## Q66

A company hosts an e-commerce application on an Auto Scaling group (ASG) of EC2 instances behind an Application Load Balancer (ALB). The ASG is set to maintain 10 EC2 instances at all times. It uses Elastic Load Balancing (ELB) health checks to detect and replace any unhealthy instances. Each EC2 instance has a CloudWatch agent installed that sends application logs to Amazon CloudWatch Logs at 5-minute intervals.

The operations team is unable to recover logs that were stored in terminated instances. This prevents them from conducting proper troubleshooting. For this reason, they require a solution that can automatically collect and back up relevant log data from instances that are about to be terminated.

Which solution would meet the requirements?

- **A.** Add a lifecycle hook to the Auto Scaling Group for the autoscaling:EC2_INSTANCE_TERMINATING event and set the default result to CONTINUE. Implement a script using an AWS Systems Manager Automation document to backup log data to an Amazon S3 bucket. Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating:Wait state. Configure the function to call the SendCommand API to run the automation document.
- **B.** Change the interval at which the CloudWatch Logs agent sends data to 1 minute. Increase the deregistration delay of the Application Load Balancer. SSH into the instance to run the script for backing up the log data to an S3 bucket.
- **C.** Use an AWS Systems Manager Automation document to create the script for backing up log data to an Amazon S3 bucket. Create an OpsItem for EC2 termination events in AWS Systems Manager OpsCenter. Configure a remediation runbook that calls the CompleteLifecycleAction Auto Scaling API with ABANDON to pause the termination of instance and SendCommand System Manager API to run the automation document.
- **D.** Create a shell script for backing up log data to an S3 bucket. Install the script to the EC2 instance’s user data. Run the script using a Lambda function via Remote Call Procedure (RPC). Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating state.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** ASG replaces unhealthy instances; logs sent every 5 min get lost

⚠️ **Watch:** Default result CONTINUE so termination isn't blocked

🧠 **Rule:** Save data before termination → lifecycle hook EC2_INSTANCE_TERMINATING + SSM Automation.

### TD explanation

The EC2 instances in an Auto Scaling group have a path, or lifecycle, that differs from that of other EC2 instances. The lifecycle starts when the Auto Scaling group launches an instance and puts it into service. The lifecycle ends when you terminate the instance, or the Auto Scaling group takes the instance out of service and terminates it.

You can add a lifecycle hook to your Auto Scaling group so that you can perform custom actions when instances launch or terminate.

When Amazon EC2 Auto Scaling responds to a scale out event, it launches one or more instances. These instances start in the Pending state. If you added an autoscaling:EC2_INSTANCE_LAUNCHING lifecycle hook to your Auto Scaling group, the instances move from the Pending state to the Pending:Wait state. After you complete the lifecycle action, the instances enter the Pending:Proceed state. When the instances are fully configured, they are attached to the Auto Scaling group and they enter the InService state.

When Amazon EC2 Auto Scaling responds to a scale in event, it terminates one or more instances. These instances are detached from the Auto Scaling group and enter the Terminating state. If you added an autoscaling:EC2_INSTANCE_TERMINATING lifecycle hook to your Auto Scaling group, the instances move from the Terminating state to the Terminating:Wait state. After you complete the lifecycle action, the instances enter the Terminating:Proceed state. When the instances are fully terminated, they enter the Terminated state.

In the scenario, we can use AWS Auto Scaling lifecycle hooks, specifically the autoscaling:EC2_INSTANCE_TERMINATING event, to intercept the instance before termination. During this intercepted state, AWS Systems Manager Automation can run a script to backup logs to an Amazon S3 bucket. To automate this process, an Amazon EventBridge rule can be set to trigger a Lambda function when the instance enters the Terminating:Wait state. This Lambda function can then call the SendCommand API to run the automation document, ensuring that the logs are backed up before termination.

Hence, the correct answer is: Add a lifecycle hook to the Auto Scaling Group for the autoscaling:EC2_INSTANCE_TERMINATING event and set the default result to CONTINUE. Implement a script using an AWS Systems Manager Automation document to backup log data to an Amazon S3 bucket. Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating:Wait state. Configure the function to call the SendCommand API to run the automation document.

The option that says: Create a shell script for backing up log data to an S3 bucket. Install the script to the EC2 instance’s user data. Run the script using a Lambda function via Remote Call Procedure (RPC). Create an Amazon EventBridge rule that invokes a Lambda function when an instance is in the Terminating state is incorrect. This approach does not guarantee the script to be executed before the instance is terminated. Termination can occur very quickly, and it’s very likely that the script won’t have time to run and back up the logs.

The option that says: Change the interval at which the CloudWatch Logs agent sends data to 1 minute. Increase the deregistration delay of the Application Load Balancer. SSH into the instance to run the script for backing up the log data to an S3 bucket is incorrect. Having to SSH into instances manually isn’t a scalable or reliable solution. If there are many instances, or if the instances are frequently scaled in or out, this method becomes unmanageable. Moreover, it doesn’t provide a solution for automatic collection and backup of logs.

The option that says: Use an AWS Systems Manager Automation document to create the script for backing up log data to an Amazon S3 bucket. Create an OpsItem for EC2 termination events in AWS Systems Manager OpsCenter. Configure a remediation runbook that calls the CompleteLifecycleAction Auto Scaling API with ABANDON to pause the termination of instance and SendCommand System Manager API to run the automation document is incorrect. In this solution, the runbook remediation is triggered upon instance termination events. This means that the termination may have already proceeded past a point where it could be halted so the backup script can be executed. Moreover, the use of Systems Manager OpsCenter adds unnecessary complexity to the solution. OpsCenter is more oriented towards incident management rather than an operational activity like capturing logs.

 

References:

https://aws.amazon.com/blogs/infrastructure-and-automation/run-code-before-terminating-an-ec2-auto-scaling-instance/

https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/cloud-watch-events.html#terminate-successful

https://aws.amazon.com/premiumsupport/knowledge-center/auto-scaling-delay-termination/

 

Check out this AWS Auto Scaling Cheat Sheet:

https://tutorialsdojo.com/aws-auto-scaling/

</details>

---

# Group B — Multi-account governance & identity (8)

<a id="q26"></a>

## Q26

A company has hundreds of AWS accounts and numerous S3 buckets scattered across multiple AWS Regions. The organization is struggling to understand its storage usage, and they’ve noticed a significant increase in S3 costs. They are interested in obtaining historical trends and comparing differences in storage usage and activity over the last 6 months.

Which solution can be used to accomplish this objective with the least amount of development overhead?

- **A.** Use Amazon S3 Storage Lens to create a customized dashboard that aggregates data from all the organization's AWS accounts and regions. Configure the dashboard to include advanced metrics
- **B.** Enable Storage Class Analysis on S3 buckets. Use the Amazon S3 console storage usage visualizations for trend analysis. Move objects between storage classes based on reports.
- **C.** Use IAM Access Analyzer for S3 to review bucket-level permissions and monitor for policy changes. Download the findings in CSV format and store them in an S3 bucket. Visualize the data using Amazon QuickSight.
- **D.** Enable Amazon S3 Inventory to generate object-level metadata reports. Follow AWS Trusted Advisor recommendations for cost optimization.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** hundreds of accounts, many Regions; S3 usage trends; 6 months history

⚠️ **Watch:** Free metrics keep only 14 days — need advanced metrics

🧠 **Rule:** Org-wide S3 usage/cost insight → S3 Storage Lens (org dashboard + advanced metrics).

### TD explanation

Amazon S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide visibility into object-storage usage and activity. You can use S3 Storage Lens metrics to generate summary insights, such as finding out how much storage you have across your entire organization or which are the fastest-growing buckets and prefixes.

You can also use S3 Storage Lens metrics to identify cost-optimization opportunities, implement data protection and security best practices, and improve the performance of application workloads. For example, you can identify buckets that don’t have S3 Lifecycle rules to expire incomplete multipart uploads that are more than 7 days old. You can also identify buckets that aren’t following data-protection best practices, such as using S3 Replication or S3 Versioning. S3 Storage Lens also analyzes metrics to deliver contextual recommendations that you can use to optimize storage costs and apply best practices for protecting your data.

In the scenario, the organization wants to understand its S3 storage spread over multiple accounts and regions for the past 6 months. S3 Storage Lens meets these needs effectively by aggregating data and providing a unified view with the ability to look back up to 15 months using the advanced metrics tier.

Therefore, the correct answer is: Use Amazon S3 Storage Lens to create a customized dashboard that aggregates data from all the organization’s AWS accounts and regions. Configure the dashboard to include advanced metrics

The option that says: Use IAM Access Analyzer for S3 to review bucket-level permissions and monitor for policy changes. Download the findings in CSV format and store them in an S3 bucket. Visualize the data using Amazon QuickSight is incorrect. IAM Access Analyzer for S3 simply focuses on reviewing bucket-level permissions. While it provides security insights, it does not offer detailed storage usage, historical trends, or comparisons over time.

The option that says: Enable Amazon S3 Inventory to generate object-level metadata reports. Follow AWS Trusted Advisor recommendations for cost optimization is incorrect. While you can use S3 Inventory to track storage to some extent and analyze object types, the complexity involved in aggregating and analyzing this data for hundreds of accounts makes this approach less suitable for the task.

The option that says: Enable Storage Class Analysis on S3 buckets. Use the Amazon S3 console storage usage visualizations for trend analysis. Move objects between storage classes based on reports is incorrect. Storage Class Analysis can help in optimizing storage costs by suggesting what objects to move between storage classes; however, it doesn’t offer a comprehensive view for understanding storage usage, historical trends, or comparisons over multiple AWS accounts and regions.

 

References:

https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html

https://aws.amazon.com/blogs/aws/s3-storage-lens/

 

Check out this Amazon S3 Cheat Sheet:

https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q41"></a>

## Q41

A large media company plans to migrate its infrastructure from its on-premises data center to AWS. The company wants to use different AWS accounts to separate resources for different business units and centrally manage them using AWS Organizations. Initially, the solutions architect will create three accounts. As other business units migrate, more accounts will be added.

A Solutions Architect needs to ensure that AWS CloudTrail is enabled in all existing and future AWS accounts.

Which of the following options is the MOST operationally efficient solution?

- **A.** Configure an organizational trail in the management account of AWS Organization.
- **B.** Create a custom script running on an Amazon EC2 instance that periodically checks for new AWS accounts and configures CloudTrail trails in each.
- **C.** Configure an Amazon EventBridge rule to trigger an AWS Lambda function. The function will periodically check and create a CloudTrail trail under the organization.
- **D.** Configure a CloudTrail trail in each business unit's AWS account manually when a new account is added and apply an SCP to enforce the logging.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** multiple accounts, more added later; log API activity everywhere

⚠️ **Watch:** Per-account trails miss new accounts

🧠 **Rule:** Org-wide auditing → organization trail in management account.

### TD explanation

AWS Organization is a useful feature of AWS that enables the consolidation of multiple AWS accounts into a single organizational unit for better management and billing. With this feature, you can create organizational units (OUs) that represent different departments or teams within your organization. Each OU can have its own AWS accounts, which can be subject to the same policies and settings, making it easier to manage and control access to resources.

AWS CloudTrail is a powerful service that allows you to record all API calls and CLI commands made in your AWS account. The service conveniently delivers log files to an S3 bucket, which means you can easily monitor and analyze your account activity. AWS CloudTrail captures all actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. You have the option to create two types of trails – single region trails, which log activity in one region only, or multi-region trails that log across all regions.

An organizational trail in AWS CloudTrail is a type of trail that logs and monitors activity across all AWS accounts within an AWS Organization. The management account or delegated admin can create an organization trail that automatically enables logging in all current and future member accounts of the organization.

The CloudTrail trail configuration includes settings like the S3 bucket for log delivery, log file encryption, event selectors to choose which API calls to log, etc. For organization trails, these settings apply uniformly to all member accounts.

Configuring an organizational trail in the management account is the most effective way to ensure CloudTrail is enabled in all existing and future AWS accounts while maintaining operational efficiency. An organizational trail applies CloudTrail configuration uniformly across all member accounts in the organization. Once created, it will automatically enable CloudTrail to log in new accounts as they are added to the organization without any manual steps. This provides a centralized way to monitor and audit activity in all accounts from a single location. The logs from all accounts will be delivered to the single S3 bucket specified for the organizational trail.

Hence, the correct answer is: Configure an organizational trail in the management account of AWS Organization.

The option that says: Configure an Amazon EventBridge rule to trigger an AWS Lambda function. The function will periodically check and create a CloudTrail trail under the organization is incorrect. While this option seems to automate the process of enabling CloudTrail, it is overly complex and potentially costly because it requires custom coding and continuous monitoring. It might not catch all new accounts immediately upon creation, depending on the periodic check interval.

The option that says: Configure a CloudTrail trail in each business unit’s AWS account manually when a new account is added and apply an SCP to enforce the logging is incorrect. This method is manual, error-prone, and inefficient. Relying on manual processes for each new account increases the risk of human error and inconsistencies in configuration. While using a Service Control Policy (SCP) to enforce logging is a good practice, it does not automate the creation of CloudTrail trails.

The option that says: Create a custom script running on an Amazon EC2 instance that periodically checks for new AWS accounts and configures CloudTrail trails in each is incorrect. Similar to the previous option, this approach involves custom scripting and maintaining an EC2 instance, leading to additional complexity and costs. It also does not guarantee immediate configuration of CloudTrail upon account creation, and continuous operation of an EC2 instance may be less efficient compared to using native AWS services.

 

References:

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html

https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html

 

Check out these AWS Organizations and AWS CloudTrail Cheat Sheets:

https://tutorialsdojo.com/aws-organizations/

https://tutorialsdojo.com/aws-cloudtrail/

</details>

<a id="q43"></a>

## Q43

A digital services provider manages many AWS accounts via AWS Organizations. The company’s policy mandates that only personnel in supervisory roles can execute IAM actions across all AWS accounts. The cloud management team wants to enforce this policy while ensuring that non-supervisory roles are restricted from executing IAM actions.

What would be the most effective approach to implement this policy with minimal administrative effort?

- **A.** Use AWS Identity and Access Management (IAM) to create a single IAM role with the necessary permissions and assign this role to all supervisory personnel across all AWS accounts.
- **B.** Use IAM permissions boundaries to restrict IAM actions to supervisory roles.
- **C.** Implement AWS Service Control Policies (SCPs) at the root Organizational Unit (OU) level that deny all non-supervisory roles from executing IAM actions.
- **D.** Assign AWS Service Control Policies (SCPs) directly to individual IAM users in each AWS account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** only supervisory roles run IAM actions across ALL accounts; minimal admin

⚠️ **Watch:** IAM policies per account = high admin

🧠 **Rule:** Org-wide guardrail → SCP at root OU denying IAM actions for non-supervisory principals.

### TD explanation

AWS Service Control Policies (SCPs) are a type of policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization, allowing you to ensure your accounts stay within your organization’s access control guidelines. By applying the SCP at the root OU level, it ensures that the policy is enforced across all accounts in the organization, which aligns with the company’s policy.

You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies account management. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization and OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another.

Hence, the correct answer is: Implement AWS Service Control Policies (SCPs) at the root Organizational Unit (OU) level that deny all non-supervisory roles from executing IAM actions.

The option that says: Use IAM permissions boundaries to restrict IAM actions to supervisory roles is incorrect because IAM permissions boundaries are only used to delegate permissions management to other users, but they do not inherently restrict IAM actions to specific roles.

The option that says: Assign AWS Service Control Policies (SCPs) directly to individual IAM users in each AWS account is incorrect because SCPs cannot be assigned directly to individual users. SCPs are simply designed to be applied at the organizational level, not at the user level, making this option technically invalid.

The option that says: Use AWS Identity and Access Management (IAM) to create a single IAM role with the necessary permissions and assign this role to all supervisory personnel across all AWS accounts is incorrect because while this could grant the necessary permissions to supervisory personnel, it does not inherently restrict all other non-supervisory roles from executing IAM actions. Therefore, this would not ensure that only supervisory roles can execute IAM actions.

 

References:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html

Check this Service Control Policies (SCP) vs IAM Policies Cheat Sheet:

https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

</details>

<a id="q44"></a>

## Q44

A global corporation manages numerous operation groups, each with unique IT requirements. The corporation uses AWS Organizations to assign individual groups to their respective Organizational Units (OUs). Each OU contains thousands of AWS accounts. A solutions architect is tasked with designing a solution that allows each OU to view and analyze a detailed breakdown of AWS usage and costs for its member accounts.

Which set of actions will satisfy the requirements?

- **A.** Use AWS Trusted Advisor in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard.
- **B.** Create an AWS Cost and Usage Report (CUR) in the management account. Store the CUR in a central Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard.
- **C.** Create a Lambda function in the management account. Configure the function to create an AWS Cost and Usage Report (CUR) in the member's account. Schedule the function using Amazon EventBridge.Store the CUR in a central Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard.
- **D.** Use AWS Systems Manager OpsCenter in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** each OU views detailed cost breakdown of member accounts

⚠️ **Watch:** ⚠️ Same concept you MISSED in Q16 (picked RAM there) — review both together

🧠 **Rule:** Org cost breakdown → CUR in management account → S3 → QuickSight dashboard.

### TD explanation

The AWS Cost and Usage Reports (AWS CUR) contains the most comprehensive set of cost and usage data available. You can use Cost and Usage Reports to publish your AWS billing reports to an Amazon Simple Storage Service (Amazon S3) bucket that you own. You can receive reports that break down your costs by the hour, day, or month, by product or product resource, or by tags that you define yourself. AWS updates the report in your bucket once a day in comma-separated value (CSV) format. You can view the reports using spreadsheet software such as Microsoft Excel or Apache OpenOffice Calc, or access them from an application using the Amazon S3 API.

The CUR tracks your AWS usage and provides estimated charges associated with your account. Each report contains line items for each unique combination of AWS products, usage type, and operations that you use in your AWS account. You can customize the AWS Cost and Usage Reports to aggregate the information either by hour, day, or month.

In the scenario, by generating a single CUR in the management account, the corporation can effectively simplify the process and ensure complete coverage of cost and usage data across all member accounts, thereby providing each OU with the ability to analyze their respective AWS usage and costs.

Hence, the correct answer is: Create an AWS Cost and Usage Report (CUR) in the management account. Store the CUR in a central Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard.

The option that says: Use AWS Systems Manager OpsCenter in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on an Amazon QuickSight dashboard is incorrect because AWS Systems Manager OpsCenter is primarily used for managing and resolving operational issues, not for generating CURs.

The option that says: Use AWS Trusted Advisor in the management account to generate an AWS Cost and Usage Report (CUR). Store the CUR in an Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard is incorrect. AWS Trusted Advisor is simply a service that gives guidance in provisioning resources that follows AWS best practices. It’s not capable of generating CURs.

The option that says: Create a Lambda function in the management account. Configure the function to create an AWS Cost and Usage Report (CUR) in the member’s account. Schedule the function using Amazon EventBridge. Store the CUR in a central Amazon S3 bucket and visualize it on a custom CloudWatch Dashboard is incorrect. This approach is unnecessarily complicated when you can generate a single CUR in the management account for all member accounts. Furthermore, Amazon QuickSight provides better visualization options for cost and usage data than a custom CloudWatch Dashboard. CloudWatch Dashboards might technically be feasible for simple visualizations, but they won’t offer the same level of detail, insight, and interactive analysis capability that Amazon QuickSight can.

 

References:

https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html

https://aws.amazon.com/blogs/enterprise-strategy/the-aws-cost-usage-report-the-next-step-on-your-cost-management-journey/

https://repost.aws/knowledge-center/quicksight-cost-usage-report

 

Check out this AWS Billing and Cost Management Cheat Sheet:

https://tutorialsdojo.com/aws-billing-and-cost-management/

</details>

<a id="q45"></a>

## Q45

A Solutions Architect is configuring a multi-account AWS environment using AWS CloudFormation. The setup requires deploying an IAM role in the primary account (Account A), which should be assumed by an EC2 instance in a secondary account (Account B). The EC2 instance uses an instance profile that incorporates the necessary IAM role.

After deploying the CloudFormation template in Account A, the EC2 instance in Account B encounters permissions issues when attempting to assume the specified IAM role.

The Solutions Architect needs to ensure the EC2 instance in Account B can successfully assume the role created in Account A.

Which actions should the Solutions Architect take?

- **A.** In the CloudFormation template, include both 'CAPABILITY_IAM' and 'CAPABILITY_NAMED_IAM' capabilities.
- **B.** In Account A, update the trust policy of the IAM role to include the ARN of the IAM role associated with the EC2 instance in Account B to allow the AssumeRole action.
- **C.** In Account A, modify the trust policy of the IAM role to allow the AssumeRole action from Account B’s root principal.
- **D.** In Account B, update the trust policy of the IAM role to include the primary Account A as a trusted entity and specify the EC2 instance as the principal.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** CFN role in Account A assumed by EC2 in Account B; access denied

⚠️ **Watch:** Fix is the TRUST policy in the role owner's account

🧠 **Rule:** Cross-account AssumeRole → role's trust policy in A names B's instance role ARN (+ B allows sts:AssumeRole).

### TD explanation

IAM Roles and Cross-Account Access: An IAM role is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumed by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.

You can use IAM Roles to delegate access to users, applications, or services that don’t normally have access to your AWS resources. For example, you might want to grant users in your AWS account access to resources they don’t usually have or grant users in one AWS account access to resources in another account.

An instance profile is a container that passes an AWS Identity and Access Management (IAM) role to an Amazon Elastic Compute Cloud (EC2) instance. It is used to securely provide temporary AWS credentials to the EC2 instance, allowing it to access other AWS services.

The issue in the given scenario is that the EC2 instance in Account B is unable to assume the IAM role in Account A due to insufficient permissions. This problem can be resolved by modifying the trust policy of the IAM role in Account A to grant the necessary permissions to Account B.

A trust policy is associated with an IAM role, which defines the principals (accounts, users, or services) that can assume the role. By default, a newly created role does not have any trust policy statements, which means that no principal can assume the role.

By adding the ARN of the IAM role associated with the EC2 instance in Account B as a trusted entity in the trust policy of the IAM role in Account A, the EC2 instance will be able to assume the role successfully.

Hence, the correct answer is: In Account A, update the trust policy of the IAM role to include the ARN of the IAM role associated with the EC2 instance in Account B to allow the AssumeRole action.

The option that says: In Account B, update the trust policy of the IAM role to include the primary Account A as a trusted entity and specify the EC2 instance as the principal is incorrect because the trust policy of an IAM role is managed in the account where the role is created, not in the account that assumes the role. In this case, the IAM role is created in Account A, so the trust policy should be updated in Account A, not in Account B.

The option that says: In Account A, modify the trust policy of the IAM role to allow the AssumeRole action from Account B’s root principal is incorrect because allowing the AssumeRole action from Account B’s root principal would allow any identities in Account B to assume the IAM role in Account A. Such strategy does not follow the principle of least privilege. It’s better to grant permissions to specific IAM roles or users.

The option that says: In the CloudFormation template, include both ‘CAPABILITY_IAM’ and ‘CAPABILITY_NAMED_IAM’ capabilities is incorrect. While these capabilities are required when creating or updating IAM resources using CloudFormation, they do not directly address the issue of cross-account role assumption. Including these capabilities ensures that the CloudFormation deployment succeeds, but it does not resolve the permissions issues encountered when the EC2 instance in Account B attempts to assume the role in Account A.

References:

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html

Check out this AWS IAM Cheat Sheet:

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q70"></a>

## Q70

A leading streaming service provider is utilizing GitHub Actions for the CI/CD pipeline, which orchestrates deployments across multiple AWS regions. The provider has been using an IAM user with an access key for authentication. An IAM role with the necessary permissions to manage Amazon S3 buckets is already in place.

Following a security audit, the provider’s security team requires the replacement of static IAM user keys with a dynamic, short-lived credential system. Additionally, the team wants to integrate GitHub Actions to automate the process of obtaining and using these dynamic credentials seamlessly. The solutions architect needs to comply with the new security policy and ensure the CI/CD pipeline remains functional and secure.

Which of the following options will meet the specified requirements while minimizing operational overhead?

- **A.** Configure AWS Security Token Service (STS) to issue temporary security credentials that the GitHub Actions CI/CD pipeline can use for deployments.
- **B.** Configure AWS IAM Identity Center and integrate it with GitHub. Create an IAM role with the required permissions and assign it to a user group in AWS IAM Identity Center. Update GitHub Actions to authenticate using AWS IAM Identity Center credentials before executing deployments.
- **C.** Configure an IAM OpenID Connect (OIDC) Identity Provider (IdP) in AWS IAM, associated with GitHub. Create an IAM role with a trust policy for the sts:AssumeRoleWithWebIdentity AWS STS API calls from the GitHub OIDC IdP. Modify the GitHub Actions CI/CD pipeline to use this IAM role for its deployment processes.
- **D.** Configure Amazon Cognito as an OpenID Connect (OIDC) Identity Provider and create a Cognito user pool. Create an IAM role with a trust policy that allows sts:AssumeRoleWithWebIdentity for authentication through Cognito. Modify the GitHub Actions CI/CD pipeline to authenticate via Cognito and assume the IAM role for deployments.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** GitHub Actions; replace static IAM user keys

⚠️ **Watch:** No long-lived access keys

🧠 **Rule:** CI/CD from GitHub → IAM OIDC identity provider + role trusting sts:AssumeRoleWithWebIdentity.

### TD explanation

IAM OIDC identity providers are entities in IAM that describe an external identity provider (IdP) service supporting the OpenID Connect (OIDC) standard. You would use an IAM OIDC identity provider when you want to establish trust between an OIDC-compatible IdP and your AWS account. This is useful when creating a mobile app or web application that requires access to AWS resources. In this case, the streaming service provider needs to establish trust between GitHub (which is acting as the IdP) and their AWS account. This is done by configuring an IAM OIDC IdP in AWS IAM and associating it with GitHub.

After creating an IAM OpenID Connect (OIDC) identity provider, the next step is to create an IAM role with the sts:AssumeRoleWithWebIdentity action and a trust policy that allows GitHub Actions to assume the role securely. The sts:AssumeRoleWithWebIdentity action is an AWS Security Token Service (STS) API operation that allows a web identity (OIDC or SAML-based identity provider) to assume an IAM role and receive temporary security credentials. This action is commonly used when applications, third-party services (e.g., GitHub Actions, Kubernetes, mobile apps), or federated identities need access to AWS resources without requiring long-lived IAM credentials. The IAM role is dynamically assigned to a federated user that is authenticated by the organization’s IdP. The policies assigned to the role determine what the federated users are allowed to do in AWS.

GitHub Actions is a platform for continuous integration and continuous delivery (CI/CD). It enables you to automate your build, test, and deployment processes. With GitHub Actions, you can create workflows to build and test every pull request to your repository and deploy merged pull requests to production. In this case, the streaming service provider is using GitHub Actions for their CI/CD pipeline. After creating the IAM role, the GitHub Actions CI/CD pipeline needs to be updated to assume this IAM role for deployments.

This approach not only adheres to the new security policy by replacing static IAM user keys with a dynamic credential system but also leverages existing AWS services, thereby minimizing operational overhead. It ensures secure and authenticated communication between GitHub and AWS services, facilitating reliable deployment workflows. This solution is in line with best practices for managing access keys and enhancing security in AWS environments.

Hence, the correct answer is: Configure an IAM OpenID Connect (OIDC) Identity Provider (IdP) in AWS IAM, associated with GitHub. Create an IAM role with a trust policy for the sts:AssumeRoleWithWebIdentity AWS STS API calls from the GitHub OIDC IdP. Modify the GitHub Actions CI/CD pipeline to use this IAM role for its deployment processes.

The option that says: Configure AWS IAM Identity Center and integrate it with GitHub. Create an IAM role with the required permissions and assign it to a user group in AWS IAM Identity Center. Update GitHub Actions to authenticate using AWS IAM Identity Center credentials before executing deployments is incorrect because AWS IAM Identity Center is primarily designed for human user authentication and does not natively support workload-to-workload authentication, such as GitHub Actions assuming a role. AWS IAM Identity Center requires interactive authentication via a web-based login, which is not feasible for an automated CI/CD pipeline. The correct approach is to use IAM OIDC with GitHub for seamless and automated authentication.

The option that says: Configure Amazon Cognito as an OpenID Connect (OIDC) Identity Provider and create a Cognito user pool. Create an IAM role with a trust policy that allows sts:AssumeRoleWithWebIdentity for authentication through Cognito. Modify the GitHub Actions CI/CD pipeline to authenticate via Cognito and assume the IAM role for deployments is incorrect because Amazon Cognito is primarily used for user authentication in applications, not for service-to-service authentication like GitHub Actions. Cognito user pools are designed for managing human users, and it does not provide a seamless way for GitHub Actions to assume an IAM role dynamically. This adds unnecessary complexity and does not align with AWS best practices for CI/CD authentication.

The option that says: Configure AWS Security Token Service (STS) to issue temporary security credentials that the GitHub Actions CI/CD pipeline can use for deployments is incorrect because while AWS STS does provide temporary security credentials, it does not specify how these credentials are associated with an IAM role. The CI/CD pipeline needs to assume an IAM role with the necessary permissions for deployments, and this option does not address that requirement.

 

References:

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html

https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html

https://aws.amazon.com/blogs/devops/integrating-with-github-actions-ci-cd-pipeline-to-deploy-a-web-app-to-amazon-ec2/

 

Check out this AWS Identity and Access Management Cheat Sheet:

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q71"></a>

## Q71

A company has integrated AWS Directory Service for Microsoft Active Directory with its on-premises Active Directory.

The company wants to grant employees access to internal applications hosted within its AWS Virtual Private Cloud (VPC) from any geographical location. The company’s security protocols mandate that access to these resources must be via a VPN, which requires multi-factor authentication (MFA).

Which solution in the following options should a solutions architect implement to comply with these requirements?

- **A.** Configure two or more AWS Site-to-Site VPN connections using AWS VPN CloudHub. Integrate AWS VPN CloudHub with AWS Directory Service for Microsoft Active Directory and utilize AWS Copilot to establish the VPN connections.
- **B.** Integrate AWS Site-to-Site VPN with AWS Directory Service for Microsoft Active Directory and use Amazon WorkSpaces with Multi-Factor Authentication enabled for the VPN connection.
- **C.** Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via AWS Direct Connect and enable Multi-Factor Authentication for the VPN connections.
- **D.** Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via the AD Connector for the VPN connection, and enable Multi-Factor Authentication for the AD Connector.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** Managed AD integrated with on-prem AD; VPN from anywhere; MFA

⚠️ **Watch:** Site-to-Site VPN ≠ remote user VPN

🧠 **Rule:** Remote users + AD + MFA → AWS Client VPN with AD Connector + MFA.

### TD explanation

AWS Directory Service is a managed service that makes it easy to set up and run Microsoft Active Directory (AD) in the AWS cloud or connect your AWS resources to an existing on-premises Microsoft AD.

AWS Directory Service supports several directory types:

– Simple AD allows you to easily launch a new Active Directory forest in the AWS cloud.

– Microsoft AD allows you to run an existing on-premises AD in the AWS cloud.

– AD Connector allows you to connect your AWS resources to an existing on-premises AD.

– Amazon Cognito is an AWS service that helps you manage user sign-up, authentication, and account management for your mobile and web applications.

It reduces the need for complex directory administration. The directories are automatically deployed across Availability Zones for high availability. AWS handles daily backups and software patching.

It allows you to integrate your directories with other AWS services, such as Amazon WorkSpaces, Amazon WorkMail, etc., for user management and access control. You can enable access to these services from the AWS Directory Service console.

The directories store information about users, groups, devices, etc., and administrators can use them to centrally manage access to information and resources across AWS accounts and services.

AWS Client VPN is a service that allows you to securely connect to your AWS resources and your on-premises network from any location. It is a client-based VPN service that uses an OpenVPN-based VPN client to enable easy access to your resources. With Client VPN, you can ensure your connection is always secure and reliable.

Using AWS Directory Service in conjunction with AD Connector allows for seamless single sign-on for users. The AWS Client VPN endpoint creates a secure IPsec VPN tunnel between the on-premises network and the VPC. Enabling Multi-Factor Authentication (MFA) on the Active Directory (AD) connector ensures that only authorized and authenticated users can access resources within the Virtual Private Cloud (VPC). These measures work together to provide a secure and hassle-free way for employees to access internal applications from anywhere while complying with the company’s security protocols for VPN access and MFA.

Hence, the correct answer is: Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via the AD Connector for the VPN connection, and enable Multi-Factor Authentication for the AD Connector.

The option that says: Integrate AWS Site-to-Site VPN with AWS Directory Service for Microsoft Active Directory and use Amazon WorkSpaces with Multi-Factor Authentication enabled for the VPN connection is incorrect because AWS Site-to-Site VPN is only designed for connecting entire networks to each other, rather than providing individual user access.

The option that says: Configure two or more AWS Site-to-Site VPN connections using AWS VPN CloudHub. Integrate AWS VPN CloudHub with AWS Directory Service for Microsoft Active Directory and utilize AWS Copilot to establish the VPN connections is incorrect because it overcomplicates the solution. AWS VPN CloudHub is generally used for multiple site-to-site connections and does not directly address the need for individual secure remote access with MFA.

The option that says: Configure an AWS Client VPN endpoint with AWS Directory Service for Microsoft Active Directory via AWS Direct Connect and enable Multi-Factor Authentication for the VPN connections is incorrect. While integrating AWS Client VPN with AWS Directory Service for Microsoft Active Directory is feasible, doing so through AWS Direct Connect is unconventional for this purpose, as Direct Connect is primarily used for establishing a dedicated network link, not for securing or managing VPN connections.

 

References:

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html

https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html

 

Check out this AWS Directory Service Cheat Sheet:

https://tutorialsdojo.com/aws-directory-service/

</details>

<a id="q75"></a>

## Q75

A company is using AWS Organizations to manage multiple AWS accounts, each belonging to a different department within the organization. As part of a new cloud spending strategy, the company wants to implement a billing reporting system with the following requirements:

Each department head must receive email notifications if their account’s spending exceeds a predefined threshold.

Each department head should receive a monthly billing report of their respective account.

The company is looking for a centralized, cost-effective solution.

Which of the following options achieves these requirements in the most cost-effective manner?

- **A.** In each department account, configure AWS Budgets to set spending thresholds and send SNS alerts to department leaders when limits are breached. Use AWS Cost Explorer within each department account to generate monthly billing reports
- **B.** In each department account, enable AWS Cost and Usage Reports (CUR) to capture detailed billing data. Use an AWS Lambda function in each department account to analyze CUR data and trigger Amazon SNS notifications to the department leaders when spending thresholds are breached
- **C.** Enable cost allocation tags in the management account and apply them to departmental resources. Use AWS Cost and Usage Reports (CUR) to filter expenses by tags. In each department account, set up AWS Lambda to analyze CUR data and trigger SNS alerts for cost overruns.
- **D.** In the management account, use AWS Budgets with budget filters to set spending thresholds for each member account. Configure these alerts to send email notifications to department heads. Use AWS Cost Explorer to generate monthly billing reports for each member account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** department heads: alert when spend exceeds threshold + monthly reports

⚠️ **Watch:** Alerts = Budgets, reporting = Cost Explorer

🧠 **Rule:** Per-account spend alerts → AWS Budgets (filters per account) in mgmt account + Cost Explorer reports.

### TD explanation

AWS Budgets allows you to set custom budgets to track your AWS spending, and it can alert you via email or SNS notifications if your costs exceed or are projected to exceed your budget. AWS Cost Explorer is a tool that provides detailed information about your AWS costs and usage, enabling you to visualize and understand your spending patterns.

In the scenario, using AWS Budgets in the management account offers a centralized way to manage and monitor spending across multiple departmental accounts. You can create budget alerts specifically for each member account using budget filters, fulfilling the requirement to notify department heads when spending exceeds predefined thresholds.

Alongside this, AWS Cost Explorer can be filtered by linked accounts to generate monthly billing reports, providing each department head with a detailed understanding of their respective account’s spending.

Hence, the correct answer in this scenario is: In the management account, use AWS Budgets with budget filters to set spending thresholds for each member account. Configure these alerts to send email notifications to department heads. Use AWS Cost Explorer to generate monthly billing reports for each member account.

The option that says: In each department account, enable AWS Cost and Usage Reports (CUR) to capture detailed billing data. Use an AWS Lambda function in each department account to analyze CUR data and trigger Amazon SNS notifications to the department leaders when spending thresholds are breached is incorrect because this is not a centralized approach. This is also more complicated to implement and incurs additional costs due to the use of Lambda functions to process billing data.

The option that says: Enable cost allocation tags in the management account and apply them to departmental resources. Use AWS Cost and Usage Reports (CUR) to filter expenses by tags. In each department account, set up AWS Lambda to analyze CUR data and trigger SNS alerts for cost overruns is incorrect. Cost allocation tags are particularly useful when you need granular visibility into your AWS spending. They allow you to attribute costs to specific projects, departments, or other categories within your organization. However, if the primary goal is simply to monitor overall spending at the account level, then cost allocation tags may introduce unnecessary complexity. Moreover, this approach would require ongoing maintenance to ensure that all new resources are correctly tagged for cost allocation.

The option that says: In each department account, configure AWS Budgets to set spending thresholds and send SNS alerts to department leaders when limits are breached. Use AWS Cost Explorer within each department account to generate monthly billing reports is incorrect. This is a viable solution but it uses a decentralized approach. This means that each department account would have to separately manage its own AWS Budgets and Cost Explorer settings.

 

References:

https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html

https://docs.aws.amazon.com/cost-management/latest/userguide/ce-access.html

https://aws.amazon.com/blogs/mt/manage-cost-overruns-part-1/

 

Check out this AWS Billing and Cost Management Cheat Sheet:

https://tutorialsdojo.com/aws-billing-and-cost-management/

</details>

---

# Group C — DR (1)

<a id="q53"></a>

## Q53

A financial company is migrating its banking application to the cloud. The application will be deployed on medium-sized Amazon EC2 instances with an Amazon Aurora for PostgreSQL database. The company aims to increase the resiliency of the application by creating a disaster recovery plan to failover across different AWS regions. As part of compliance, the recovery point objective (RPO) should be under one minute, while the recovery time objective (RTO) should be a maximum of 15 minutes only.

What solution will fulfill these requirements MOST cost-effectively?

- **A.** Deploy an identical infrastructure in multiple regions and keep the regions actively serving traffic. Use global load balancers to distribute requests between regions.
- **B.** Build the infrastructure using AWS CloudFormation templates to allow provisioning the resources in a DR region in the event of a disaster. Create an Aurora global database with the primary instance in the production region and a secondary (read-only) instance in the DR region. Configure AWS Elastic Disaster Recovery to continuously replicate the EC2 instances from the production region to the DR region, and setup an auto-scaling group in the DR region. Use Amazon Route 53 failover routing policy to direct traffic to DR in case of a disaster.
- **C.** Set up a scaled-down replica of the infrastructure in another AWS region. Keep the replica in a warm state by keeping at least one EC2 instance running and an Aurora for PostgreSQL instance active. Enable data replication from the primary database to the secondary database.
- **D.** Periodically take snapshots of the EC2 instances and Aurora for PostgreSQL database to serve as backups. In the event of a disaster, restore the system by launching EC2 instances from the snapshots and restoring the Aurora database from the database backup.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** Aurora PostgreSQL; cross-Region DR; RPO < 1 minute

⚠️ **Watch:** Snapshots/cross-Region replicas can't guarantee sub-minute RPO

🧠 **Rule:** RPO < 1 min cross-Region Aurora → Aurora Global Database (+ CFN to provision DR infra).

### TD explanation

By default, AWS CloudFormation operates within a specific AWS region, and resources managed by the CloudFormation stack must reside in the same region as the stack. To achieve cross-region deployments, AWS CloudFormation StackSets can be used to deploy stacks across multiple accounts and regions. CloudFormation templates can include cross-region resource references. Nested stacks can also be used to organize resources logically and reference outputs across regions. Elastic Disaster Recovery is an AWS service that allows for a fast and reliable recovery of resources, increasing resilience. It has a Point in Time (PIT) state schedule, as low as 10 minutes for the last hour.

Amazon Aurora global databases span multiple AWS Regions, enabling low latency global reads and providing fast recovery from the rare outage that might affect an entire AWS Region. An Aurora global database has a primary DB cluster in one Region and up to five secondary DB clusters in different Regions. An Aurora global database provides more business continuity and disaster recovery (BCDR) protection than the standard high availability provided by an Aurora DB cluster in a single AWS Region. By using an Aurora global database, you can plan for and recover from true Regional disasters or complete service-level outages quickly. Amazon Route 53 allows a routing policy called Failover routing which allows routing traffic to a healthy resource or a different resource when the first resource is detected to be unhealthy.

Hence, the correct answer is: Build the infrastructure using AWS CloudFormation templates to allow provisioning the resources in a DR region in the event of a disaster. Create an Aurora global database with the primary instance in the production region and a secondary (read-only) instance in the DR region. Configure AWS Elastic Disaster Recovery to continuously replicate the EC2 instances from the production region to the DR region, and setup an auto-scaling group in the DR region. Use Amazon Route 53 failover routing policy to direct traffic to DR in case of a disaster.

The option that says: Deploy an identical infrastructure in multiple regions and keep the regions actively serving traffic. Use global load balancers to distribute requests between regions is incorrect. While this approach primarily achieves zero downtime during failover, it is the most expensive option. Running a full-scale infrastructure in multiple regions incurs high costs.

The option that says: Set up a scaled-down replica of the infrastructure in another AWS region. Keep the replica in a warm state by keeping at least one EC2 instance running and an Aurora for PostgreSQL instance active. Enable data replication from the primary database to the secondary database is incorrect. Although this approach can typically achieve the specified objectives of recovery time and recovery point, there is no automatic failover in place, which can add to the recovery time of the infrastructure in the DR region.

The option that says: Periodically take snapshots of the EC2 instances and Aurora for PostgreSQL database to serve as backups. In the event of a disaster, restore the system by launching EC2 instances from the snapshots and restoring the Aurora database from the database backup is incorrect. While this approach is cost-effective, the recovery point objective (RPO) and recovery time objective (RTO) may not be met since restoring from snapshots takes more time.

 

References:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/disaster-recovery-resiliency.html

https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html

 

Check out this AWS Disaster Recovery Cheat Sheet:

https://tutorialsdojo.com/aws-well-architected-framework-disaster-recovery/

</details>

---

# Group D — Migration (4)

<a id="q2"></a>

## Q2

An e-commerce enterprise is in the process of migrating its flagship application from a local data center to the AWS cloud. The web application architecture includes a load balancer, operates on a Linux-based environment, and utilizes a PostgreSQL database for data storage. The application handles high traffic volumes, especially during peak shopping seasons, requiring the infrastructure to scale efficiently and seamlessly.

The application needs a robust NFS-compatible storage system for its digital assets, such as product images and user-generated content. The proposed cloud infrastructure needs to have the flexibility to scale from 3 to 50 Amazon EC2 instances to handle unexpected traffic surges, without allowing any modifications to the application. Additionally, it must ensure data integrity and availability, safeguarding against data loss.

Which of the following options would fulfill the given requirements?

- **A.** Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Transition the web application onto AWS Elastic Beanstalk, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage .ebextensions configuration files to mount the EFS onto the EC2 instances. Establish an Amazon Aurora database with PostgreSQL compatibility, separate from the Elastic Beanstalk setup.
- **B.** Use Amazon Elastic Block Store (EBS) with Multi-Attach capability. Transition the web application to AWS Elastic Beanstalk, incorporating a Network Load Balancer and an Auto Scaling group for adaptive scalability. Utilize .ebextensions scripts to mount the EBS volume to the EC2 instances. Within the Elastic Beanstalk environment, set up an Amazon RDS configured for PostgreSQL.
- **C.** Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Establish a launch template and an Auto Scaling group to initiate EC2 instances for the web application. Set up a Network Load Balancer for traffic management. Configure an Amazon Aurora database with PostgreSQL compatibility. Employ an EC2 Auto Scaling scale-in lifecycle hook to mount the EFS to the EC2 instances.
- **D.** Use Amazon S3 to serve as the file storage infrastructure. Transition the web application onto AWS Lambda, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage AWS SAM templates to mount the S3 bucket onto the Lambda functions. Establish an Amazon RDS database with PostgreSQL compatibility, separate from the Lambda setup.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** migrate web app + PostgreSQL; high traffic peaks; scale seamlessly; low overhead

⚠️ **Watch:** Shared file storage for web tier

🧠 **Rule:** Replatform web app → Elastic Beanstalk (ALB + ASG) + EFS for shared files + managed DB.

### TD explanation

Amazon Elastic File System (EFS) is a fully managed service that makes it easy to set up and scale file storage in the Amazon Cloud. It’s designed to provide massively parallel shared access to thousands of Amazon EC2 instances, enabling your applications to achieve high levels of aggregate throughput and IOPS with consistent low latencies. This makes it a suitable choice for a robust NFS-compatible storage system for the application’s digital assets.

AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. This service would allow the e-commerce enterprise to easily migrate their web application to the cloud.

An Application Load Balancer operates at the application layer, which is the topmost layer in the Open Systems Interconnection (OSI) model. When a request arrives, the load balancer checks its set of listener rules in the order of their priority to determine which rule to apply. Once the appropriate rule is identified, the load balancer then chooses a target from the corresponding target group to handle the request. This, in combination with an Auto Scaling group, provides the flexibility to scale from 3 to 50 Amazon EC2 instances to handle unexpected traffic surges.

The .ebextensions configuration files are used to customize the software that runs on the EC2 instances of your Elastic Beanstalk environment. You can use .ebextensions configuration files to mount the EFS onto the EC2 instances.

Amazon Aurora is a relational database compatible with MySQL and PostgreSQL. It is designed for the cloud and offers the performance and availability of traditional enterprise databases along with the simplicity and cost-effectiveness of open-source databases. This makes it an ideal choice for the PostgreSQL database needed for the application.

Hence, the correct answer is: Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Transition the web application onto AWS Elastic Beanstalk, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage .ebextensions configuration files to mount the EFS onto the EC2 instances. Establish an Amazon Aurora database with PostgreSQL compatibility, separate from the Elastic Beanstalk setup.

The option that says: Use Amazon Elastic Block Store (EBS) with Multi-Attach capability. Transition the web application to AWS Elastic Beanstalk, incorporating a Network Load Balancer and an Auto Scaling group for adaptive scalability. Utilize .ebextensions scripts to mount the EBS volume to the EC2 instances. Within the Elastic Beanstalk environment, set up an Amazon RDS configured for PostgreSQL is incorrect because EBS with Multi-Attach is not NFS-compatible, which is a requirement for the application’s digital assets.

The option that says: Use Amazon Elastic File System (EFS) to serve as the file storage infrastructure. Establish a launch template and an Auto Scaling group to initiate EC2 instances for the web application. Set up a Network Load Balancer for traffic management. Configure an Amazon Aurora database with PostgreSQL compatibility. Employ an EC2 Auto Scaling scale-in lifecycle hook to mount the EFS to the EC2 instances is incorrect because lifecycle hooks are not designed for mounting file systems, which is necessary for the application’s operation.

The option that says: Use Amazon S3 to serve as the file storage infrastructure. Transition the web application onto AWS Lambda, integrating an Application Load Balancer and an Auto Scaling group for dynamic adaptability. Leverage AWS SAM templates to mount the S3 bucket onto the Lambda functions. Establish an Amazon RDS database with PostgreSQL compatibility, separate from the Lambda setup is incorrect because Amazon S3 is not NFS-compatible and transitioning to AWS Lambda would require modifications to the application, which is against the requirements.

 

References:

https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/services-efs.html

 

Check out these Amazon EFS and AWS Elastic Beanstalk Cheat Sheets:

https://tutorialsdojo.com/amazon-efs/

</details>

<a id="q46"></a>

## Q46

A company has several legacy virtual machines running on VMware infrastructure in its on-premises data center. There is also a storage server with SMB shares that is used as a central logging and backup destination. The company wants to migrate its production workload to Amazon EC2 instances. For this migration, the solutions architect has been tasked to preserve the software and configuration settings of the servers.

Which of the following options should the solutions architect implement to meet the company requirements?

- **A.** Install the AWS Systems Manager agent on all on-premises servers. Utilize AWS SSM to create a managed-instance activation for hybrid environment and register all the virtual machines in Systems Manager. Configure AWS Backup to create an AMI backup of all the registered instances. Launch Amazon EC2 instances based on the created AMIs.
- **B.** Export all the virtual machines using the VMware vSphere client and save the images as Open Virtualization Format (OVF). Upload the VM images to an Amazon S3 bucket on the destination region. Create an IAM role that has permissions to use VM Import/Export. Use AWS CLI to import the VM images and launch them as EC2 instances.
- **C.** Create an Amazon FSx for Windows File Server. Set up the AWS DataSync agent in the on-premises data center to start replication to AWS. Create VM images and upload them to an Amazon S3 bucket in the destination region. Use AWS VM Import/Export to import the images and launch them as EC2 instances.
- **D.** Create an AWS Storage Gateway – File Gateway and configure a Common Internet File System (CIFS). Sync the SMB server files to this share. Create a snapshot of the virtual machines in VMware and copy them to the File Gateway. On the AWS Management Console, launch EC2 instances and select the snapshots as the AMI.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** VMware VMs; preserve software/config; SMB log/backup share

⚠️ **Watch:** ⚠️ Same services you missed in Q4 (VM Import) and Q32 (FSx+DataSync)

🧠 **Rule:** Lift VM as-is → VM Import/Export; SMB share → FSx for Windows + DataSync.

### TD explanation

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS Storage services, as well as between AWS Storage services. DataSync can copy data between Network File System (NFS) shares, Server Message Block (SMB) shares, self-managed object storage, AWS Snowcone, Amazon Simple Storage Service (Amazon S3) buckets, Amazon Elastic File System (Amazon EFS) file systems, and Amazon FSx for Windows File Server file systems.

These are some of the main use cases for AWS DataSync:

Data migration – Move active datasets rapidly over the network into Amazon S3, Amazon EFS, or FSx for Windows File Server.

Archiving cold data – Move cold data stored in on-premises storage directly to durable and secure long-term storage such as Amazon S3 Glacier or S3 Glacier Deep Archive.

Data protection – Move data into any Amazon S3 storage class, choosing the most cost-effective storage class for your needs.

Data movement for timely in-cloud processing – Move data into or out of AWS for processing when working with systems that generate data on-premises. This approach can speed up critical hybrid cloud workflows across many industries.

VM Import/Export enables you to import virtual machine (VM) images from your existing virtualization environment to Amazon EC2 and then export them back. This enables you to migrate applications and workloads to Amazon EC2, copy your VM image catalog to Amazon EC2, or create a repository of VM images for backup and disaster recovery.

Therefore, the correct answer is: Create an Amazon FSx for Windows File Server. Set up the AWS DataSync agent in the on-premises data center to start replication to AWS. Create VM images and upload them to an Amazon S3 bucket in the destination region. Use AWS VM Import/Export to import the images and launch them as EC2 instances. 

The option that says: Create an AWS Storage Gateway – File Gateway and configure a Common Internet File System (CIFS). Sync the SMB server files to this share. Create a snapshot of the virtual machines in VMware and copy them to the File Gateway. On the AWS Management Console, launch EC2 instances and select the snapshots as the AMI is incorrect. This may be possible; however, it is unnecessary to create a File Gateway on your on-premises data center if you want to sync an SMB to the AWS cloud. AWS DataSync offers a managed service that is designed for copying data from SMB shares to AWS.

The option that says: Export all the virtual machines using the VMware vSphere client and save the images as Open Virtualization Format (OVF). Upload the VM images to an Amazon S3 bucket on the destination region. Create an IAM role that has permissions to use VM Import/Export. Use AWS CLI to import the VM images and launch them as EC2 instances is incorrect. This may be possible; however, there is no mention of how to migrate the SMB share data. The data inside the SMB share can change while doing any snapshot so it is better to use AWS DataSync for the migration.

The option that says: Install the AWS Systems Manager agent on all on-premises servers. Utilize AWS SSM to create a managed-instance activation for hybrid environment and register all the virtual machines in Systems Manager. Configure AWS Backup to create an AMI backup of all the registered instances. Launch Amazon EC2 instances based on the created AMIs is incorrect. AWS Backup only supports backing up AWS services. It cannot create AMIs from on-premises virtual machines.

 

References:

https://aws.amazon.com/datasync/

https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

https://docs.aws.amazon.com/vm-import/latest/userguide/what-is-vmimport.html

 

Check out the AWS DataSync and Cheat Sheet:

https://tutorialsdojo.com/aws-datasync/

</details>

<a id="q47"></a>

## Q47

A large company runs its mission-critical Microsoft SQL Server Always On cluster on its on-premises data center servers. The management is planning to migrate its core applications, including the database servers, to the AWS cloud. The management specifically requested to use AWS managed services whenever possible to save on operational overhead costs. The Solutions Architect must create a heterogeneous database migration strategy to AWS.

Which of the following options is the recommended solution that will meet the above requirements?

- **A.** Utilize the native SQL Server backup utility to create a copy of the current database. Upload the created backup file to an Amazon S3 bucket. Create a new Amazon RDS for MySQL instance. Use AWS Glue to load S3 data into the RDS MySQL Table.
- **B.** Create a backup copy of the on-premises SQL Server. Use AWS DataSync to transfer the backup files directly to an Amazon S3 bucket. Create an Amazon RDS for MySQL instance. Use the SQL Server BULK INSERT feature to load data from the S3 bucket to the RDS instance.
- **C.** Install the AWS Schema Conversion Tool on the on-premises data center to convert the database schema from Microsoft SQL Server to MySQL. Create an Amazon RDS for MySQL instance. Migrate the on-premises database to the RDS instance using AWS Database Migration Service (AWS DMS).
- **D.** Establish a secure VPN connection from the on-premises network to Amazon VPC. Create a new Amazon RDS for MySQL instance. Use the AWS DataSync service to replicate the SQL server database to AWS. Promote the RDS instance as a master database once replication is completed.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** SQL Server Always On → heterogeneous migration; managed services

⚠️ **Watch:** Heterogeneous = schema conversion first

🧠 **Rule:** Heterogeneous DB migration → AWS SCT (schema) + DMS (data) to RDS.

### TD explanation

You can use the AWS Schema Conversion Tool (AWS SCT) to convert your existing database schema from one database engine to another. You can convert relational OLTP schema or data warehouse schema. Your converted schema is suitable for an Amazon Relational Database Service (Amazon RDS), MySQL, MariaDB, Oracle, SQL Server, PostgreSQL DB, an Amazon Aurora DB cluster, or an Amazon Redshift cluster. The converted schema can also be used with a database on an Amazon EC2 instance or stored as data on an Amazon S3 bucket.

AWS Database Migration Service (AWS DMS) is a cloud service that makes it easy to migrate relational databases, data warehouses, NoSQL databases, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud or between combinations of cloud and on-premises setups.

With AWS DMS, you can perform one-time migrations, and you can replicate ongoing changes to keep sources and targets in sync. If you want to migrate to a different database engine, you can use the AWS Schema Conversion Tool (AWS SCT) to translate your database schema to the new platform. You then use AWS DMS to migrate the data. Because AWS DMS is a part of the AWS Cloud, you get the cost efficiency, speed to market, security, and flexibility that AWS services offer. At a basic level, AWS DMS is a server in the AWS Cloud that runs replication software. You create a source and target connection to tell AWS DMS where to extract from and load into.

Therefore, the correct answer is: Install the AWS Schema Conversion Tool on the on-premises data center to convert the database schema from Microsoft SQL Server to MySQL. Create an Amazon RDS for MySQL instance. Migrate the on-premises database to the RDS instance using AWS Database Migration Service (AWS DMS). The AWS SCT can convert the database schema to MySQL, and the AWS DMS can be used to easily migrate the converted database to an RDS MySQL instance.

The option that says: Utilize the native SQL Server backup utility to create a copy of the current database. Upload the created backup file to an Amazon S3 bucket. Create a new Amazon RDS for MySQL instance. Use AWS Glue to load S3 data into the RDS MySQL Table is incorrect because AWS Glue is primarily designed for ETL (Extract, Transform, Load) jobs, which are better suited for data transformation rather than direct migration of SQL Server backups to an RDS MySQL database.

The option that says: Create a backup copy of the on-premises SQL Server. Use AWS DataSync to transfer the backup files directly to an Amazon S3 bucket. Create an Amazon RDS for MySQL instance. Use the SQL Server BULK INSERT feature to load data from the S3 bucket to the RDS instance is incorrect because DataSync is typically intended for file transfer and not database migration. The BULK INSERT feature only supports loading data from an S3 bucket to a SQL server instance, not an RDS MySQL instance.

The option that says: Establish a secure VPN connection from the on-premises network to Amazon VPC. Create a new Amazon RDS for MySQL instance. Use the AWS DataSync service to replicate the SQL server database to AWS. Promote the RDS instance as a master database once replication is completed is incorrect. AWS DataSync can facilitate the copying of data from on-premises data stores to the AWS cloud, but it can’t be used to replicate an on-premises database to AWS.

 

References:

https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html

https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.HighLevelView.html

 

Check out this AWS Database Migration Service Cheat Sheet:

https://tutorialsdojo.com/aws-database-migration-service/

</details>

<a id="q52"></a>

## Q52

A company has a suite of services hosted on its on-premises data center. These services run on a network of virtualized Ubuntu and Windows servers. To benefit from AWS’ scaling capabilities, the company decides to migrate its entire system to AWS.

The migration strategy aims to precisely understand the actual usage and deeply analyze application components and the dependencies within its on-premises workload. The company also wants to right-size its Amazon EC2 instances to avoid unnecessary expenses for underutilized resources.

Which set of actions will meet the requirements?

- **A.** Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves, and use AWS Transform migration assessments to generate EC2 right-sizing and cost recommendations.
- **B.** Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves. After the workloads are migrated to EC2, use AWS Compute Optimizer to generate EC2 right-sizing recommendations.
- **C.** Install the AWS Systems Manager Agent on both the physical servers and Virtual machines to perform an application-level assessment. Utilize Systems Manager Application Manager to logically separate servers into different applications. Input server size data into the AWS Pricing calculator and adhere to its recommendations.
- **D.** Use AWS Transform MGN to install replication agents on the source servers and immediately start continuous block-level replication to AWS. After the servers are launched on EC2, use AWS Compute Optimizer to recommend instance sizes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** virtualized Ubuntu + Windows; actual usage + dependencies

⚠️ **Watch:** ⚠️ Same service you missed in Q33 (AWS Transform discovery)

🧠 **Rule:** Discovery + dependency mapping → AWS Transform discovery tool + migration planning.

### TD explanation

AWS Transform is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.

With AWS Transform, you can:

– Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS

– Migrate VMware workloads to Amazon EC2

– Modernize .NET applications to Linux-ready cross-platform .NET

– Assess workloads for migration readiness

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.

The AWS Transform discovery tool automatically identifies server inventory within your organization to prepare for migration. The tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To use the discovery tool, you’ll configure one or more discovery sources, let the tool run, and then review the results in the Discovered Inventory pane.

Once you’ve set up a discovery source, the discovery tool begins collecting information. The time required for the tool to analyze your network completely depends on the size of your environment. For a directional migration business case, you can utilize the Migration Portfolio Assessment (MPA) files that the tool generates once server collection is complete.

The Migration Planning job step within AWS Transform for VMware provides a collaborative, chat-based experience designed for planning large migrations. AWS Transform agents utilize AWS Prescriptive Guidance to assist customers in transitioning from analyzing on-premises data to finalizing migration wave plans.

Once the Discover on-premises data job successfully completes, AWS Transform employs the discovery data to categorize applications into migration waves. The service guides you through the steps of analyzing and scoping your servers, grouping them into applications, creating move groups, and developing migration waves. During the analysis of your on-premises environment, you can ask questions to gain insights into how AWS Transform evaluated your installed software, including aspects such as server dependencies and network architecture.

AWS Transform assessments help you evaluate the cost, feasibility, and business value of migrating your on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinements through chat.

You can use migration assessments to:

– Obtain cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx

– Receive automated right-sizing recommendations

– Assess business value and sustainability impact

– Compare multiple migration scenarios side by side

– Refine assessments interactively through chat

– Generate executive presentations and detailed reports

Hence, the correct answer is: Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves, and use AWS Transform migration assessments to generate EC2 right-sizing and cost recommendations.

The option that says: Install the AWS Systems Manager Agent on both the physical servers and Virtual machines to perform an application-level assessment. Utilize Systems Manager Application Manager to logically separate servers into different applications. Input server size data into the AWS Pricing calculator and adhere to its recommendations is incorrect. The AWS Systems Manager agent does not provide a deep understanding of current resource usage and application dependencies as the AWS Application Discovery Agent. AWS Systems Manager Application Manager is primarily designed for application lifecycle management, not necessarily for grouping servers into applications as part of a migration strategy. Also, the AWS Pricing calculator gives cost estimates based on input parameters but does not provide sophisticated EC2 instance sizing recommendations that are based on actual performance and usage data.

The option that says: Use AWS Transform MGN to install replication agents on the source servers and immediately start continuous block-level replication to AWS. After the servers are launched on EC2, use AWS Compute Optimizer to recommend instance sizes is incorrect because AWS Transform MGN is typically a rehost migration service that replicates source servers to AWS using block-level replication. This option begins replication immediately and skips the required discovery, dependency analysis, application grouping, and migration wave planning. In addition, AWS Compute Optimizer analyzes CloudWatch metrics from running AWS resources, so it is better suited for optimization after workloads are already running in AWS, not for the required pre-migration assessment.

The option that says: Deploy the AWS Transform discovery tool in the on-premises environment to gather performance and usage information from physical servers and virtual machines. Use AWS Transform migration planning to group servers into applications and migration waves. After the workloads are migrated to EC2, use AWS Compute Optimizer to generate EC2 right-sizing recommendations is incorrect because it correctly uses AWS Transform discovery and migration planning, but it delays right-sizing until after the workloads have already been migrated to Amazon EC2. AWS Compute Optimizer provides recommendations for optimal AWS resource utilization based on historical usage data. In this case, the company has not yet migrated to AWS, so there’s no historical usage data for the Compute Optimizer to base its recommendations on.

 

References:

https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html

https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html

https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html

 

Check out this AWS Migration Services Cheat Sheet:

https://tutorialsdojo.com/aws-cheat-sheets-migration-services/

</details>

---

# Group E — Serverless + DB (5)

<a id="q34"></a>

## Q34

An e-commerce company experiences operational disruptions during peak shopping periods. The web application, serving a global customer base, is currently hosted on a single Amazon EC2 instance, which often becomes unresponsive under heavy load. The application makes read-intensive calls to an Amazon RDS for PostgreSQL database.

A Solutions Architect must enhance the application’s reliability with minimal development effort.

Which of the following solutions meets this requirement?

- **A.** Upgrade the EC2 instance type to a more powerful and larger instance type. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations.
- **B.** Deploy the application across multiple EC2 instances managed by an Auto Scaling group, with an Elastic Load Balancer to distribute traffic. Migrate the database to Amazon Aurora and utilize Aurora Replicas for handling read-intensive tasks.
- **C.** Set up an Auto Scaling group for the EC2 instances that host the application. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations.
- **D.** Upgrade the EC2 instance type to a more powerful and larger instance type. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. Migrate the database to Amazon Aurora and utilize Aurora Replicas to handle read-intensive tasks.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** single EC2 unresponsive at peak; read-heavy PostgreSQL; minimal dev effort

⚠️ **Watch:** Read-heavy → replicas, not bigger instance

🧠 **Rule:** Reliability → ASG + ELB; read scaling → Aurora + Aurora Replicas.

### TD explanation

Auto Scaling Groups: Auto Scaling groups help ensure that you have the correct number of Amazon EC2 instances available to handle your application’s load. You can create launch configurations that serve as templates for launching instances. The Auto Scaling group can automatically increase or decrease the number of instances based on user-defined policies, schedules, and health checks.

Elastic Load Balancing: Elastic Load Balancing automatically distributes incoming application traffic across multiple Amazon EC2 instances in one or more Availability Zones. It provides high availability by routing traffic to healthy instances and monitors the health of registered instances.

Amazon CloudFront: Amazon CloudFront is a content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds. It caches content at edge locations around the world, reducing the load on the origin servers.

Amazon RDS Multi-AZ Deployment: Amazon RDS Multi-AZ deployment provides enhanced availability and data durability for DB instances. It creates a primary database instance and synchronously replicates the data to a standby instance in a different Availability Zone.

Amazon Aurora: Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud. It combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open-source databases.

Amazon Aurora Replicas: Aurora Replicas are independent endpoints in an Aurora DB cluster, capable of driving read operations and offloading read workloads from the primary instance. They can help scale read operations and improve overall performance.

The solution, which combines Auto Scaling groups, Elastic Load Balancing, Amazon Aurora, and Aurora Replicas, provides the most comprehensive solution to meet the requirements of:

Enhancing reliability: By distributing the application across multiple EC2 instances managed by an Auto Scaling group, the solution ensures that the application can automatically scale resources based on demand, reducing the risk of operational disruptions during peak periods.

Improving performance and handling heavy loads: The Elastic Load Balancer distributes traffic across multiple instances, ensuring that the application can handle heavy loads without becoming unresponsive.

Addressing the performance bottleneck for read-intensive operations: By migrating the database to Amazon Aurora, the solution leverages a database service designed for better performance and scalability compared to traditional relational databases.

Utilizing Aurora Replicas: Aurora Replicas are used to handle read-intensive tasks, offloading the read workload from the primary instance and improving overall performance.

Minimal development effort: This solution leverages managed services and does not require significant code changes, minimizing the development effort required.

Hence, the correct answer is: Deploy the application across multiple EC2 instances managed by an Auto Scaling group, with an Elastic Load Balancer to distribute traffic. Migrate the database to Amazon Aurora and utilize Aurora Replicas for handling read-intensive tasks.

The option that says: Set up an Auto Scaling group for the EC2 instances that host the application. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations is incorrect. While this option addresses the scalability and high availability concerns for the web application and database, it does not fully resolve the read-intensive performance bottleneck. Using the standby instance of the Multi-AZ RDS deployment for read operations may provide some relief, but it is not as efficient as using dedicated read replicas like Aurora Replicas. Additionally, using CloudFront is not necessary for this use case, as it is primarily designed for content delivery and caching static assets. Lastly, you cannot directly use an Auto Scaling group (ASG) as the origin for an Amazon CloudFront distribution.

The option that says: Upgrade the EC2 instance type to a more powerful and larger instance type. Create an Amazon CloudFront distribution with the Auto Scaling group as the origin. Migrate the database to Amazon Aurora and utilize Aurora Replicas to handle read-intensive tasks is incorrect. This option addresses the read-intensive database performance bottleneck by using Aurora Replicas, which is a good solution. However, it suggests upgrading the EC2 instance type instead of using an Auto Scaling group and Elastic Load Balancer. Upgrading the instance type may provide temporary relief, but it does not address the scalability and high availability concerns for the web application. Additionally, just like the previous option, using CloudFront is not necessary for this use case.

The option that says: Upgrade the EC2 instance type to a more powerful and larger instance type. For the database, enable the Multi-AZ deployment of the Relational Database Service for PostgreSQL and use the standby instance for read operations is incorrect. While it addresses high availability for the database using Multi-AZ deployment, just like the previous option that uses Amazon RDS, it does not fully resolve the read-intensive performance bottleneck, and it is not as efficient as using dedicated read replicas like Aurora Replicas. Additionally, upgrading the EC2 instance type alone may not be sufficient to handle peak loads, and it does not provide the same level of flexibility and automatic scaling as an Auto Scaling group combined with an Elastic Load Balancer.

 

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Overview.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

</details>

<a id="q40"></a>

## Q40

An organization operates an application on AWS Environment. The backend consists of AWS Lambda functions triggered by Amazon API Gateway, with product data stored in an Amazon RDS for MySQL database.

During high-traffic events, the application receives an exponential increase in requests, causing slowdowns. The organization noticed high Lambda invocations, database connections, and CPU utilization on RDS through Amazon CloudWatch. A Solutions Architect must implement a solution to improve the performance of the application.

Which combination of steps in the following options would meet this requirement most efficiently? (Select TWO.)

- **A.** Enable Amazon RDS Multi-AZ deployments for higher availability and failover support.
- **B.** Modify the Lambda function to use an RDS Proxy endpoint for database queries.
- **C.** Cache frequently accessed data to the RDS database with an Amazon ElastiCache for Redis cluster.
- **D.** Adjust the Lambda function's timeout settings and increase concurrent execution limits.
- **E.** Adjust the memory allocation for Lambda functions and ensure database connections are closed after data retrieval.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C (you answered correctly)

🔑 **Key words:** API GW + Lambda + RDS MySQL; high invocations, connections, CPU

⚠️ **Watch:** ⚠️ Same fix you missed in Q5/Q58 (RDS Proxy)

🧠 **Rule:** Connection pressure → RDS Proxy; read load → ElastiCache for Redis.

### TD explanation

Amazon RDS Proxy is a service that allows applications to pool and share database connections, improving their ability to scale and making them more resilient to database failures. When an application connects to an RDS Proxy, the proxy maintains a pool of connections to the database and reuses these connections across requests.

RDS Proxy handles unpredictable spikes in database traffic and queue connections when the maximum limit is reached. This maintains predictable performance for the database. The proxy also enforces AWS Identity and Access Management (IAM) authentication for databases and securely stores credentials in AWS Secrets Manager.

To use RDS Proxy with Lambda functions, you first need to create a proxy and grant necessary permissions to the Lambda execution role. Then, modify the Lambda function code to connect to the proxy endpoint instead of the database endpoint. No other code changes are required. The proxy takes care of connection pooling and throttling traffic between the Lambda function and the database.

Amazon ElastiCache is a web service that makes it easy to set up, manage, and scale distributed in-memory caches.

Amazon ElastiCache for Redis: ElastiCache provides a managed service that handles tasks like provisioning, monitoring, and patching Redis nodes. You can either use serverless caching, which automatically scales a Redis cluster, or design your own clusters by choosing node types and configurations. Redis supports data persistence through replication and snapshots.

Two steps can be taken to improve application performance during high-traffic events. First, cache frequently accessed data in Amazon ElastiCache for Redis cluster to reduce the load on the database. Second, modify the Lambda function to use an RDS Proxy endpoint for database queries, which allows Lambda functions to reuse connections and prevents overloading the database.

Hence, the correct answers are:

– Cache frequently accessed data to the RDS database with an Amazon ElastiCache for Redis cluster.

– Modify the Lambda function to use an RDS Proxy endpoint for database queries.

The option that says: Adjust the memory allocation for Lambda functions and ensure database connections are closed after data retrieval is incorrect. While memory adjustments may enhance Lambda performance slightly, they don’t directly tackle scalability or connection management issues during peak loads. Similarly, closing database connections after retrieval is a good practice but doesn’t efficiently handle connection management in high-traffic scenarios. In contrast, ElastiCache’s data caching reduces database load by serving frequently accessed data from cache, while RDS Proxy optimizes connection management, addressing the specific challenges faced during high-traffic events more effectively. Therefore, opting for RDS Proxy and ElastiCache provides a more robust solution for improving application performance under heavy loads in an AWS Lambda and RDS environment.

The option that says: Adjust the Lambda function’s timeout settings and increase concurrent execution limits is incorrect. Adjusting timeout settings and concurrency might help to some extent but does not tackle the core issues of database load and efficient data retrieval during high traffic, thus not as effective as using RDS Proxy and ElastiCache.

The option that says: Enable Amazon RDS Multi-AZ deployments for higher availability and failover support is incorrect. While Multi-AZ deployments provide high availability and failover capabilities, they are not primarily aimed at improving performance under high load, which is the requirement in this scenario.

References:

https://docs.aws.amazon.com/lambda/latest/operatorguide/traffic-server-based.html

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-elasticache/

https://tutorialsdojo.com/aws-lambda/

</details>

<a id="q50"></a>

## Q50

A healthcare research institute is building a machine learning model for predicting disease outbreaks. A fleet of small Amazon EC2 instances fetches URLs of health-related articles and research papers from an Amazon SQS queue using a web-crawling process. After fetching the articles and research papers from the provided URLs, the instances analyze the documents, extract features, and store the results as .json files in an Amazon EFS volume, which is accessible to all instances within the fleet.

An automated system feeds the URLs of the health-related articles and research papers into the SQS queue based on real-time updates from various health organizations. Each instance processes the data within 5 minutes. However, there are periods when the instances are idle due to low volumes of health updates. A cloud engineer is tasked to restructure the system to reduce operational costs.

What actions should the cloud engineer take to ensure the most cost-effective solution? (Select TWO.)

- **A.** Use Amazon Neptune to store the .json files instead of Amazon EFS.
- **B.** Replace the EC2 instances with AWS Lambda functions to fetch and process data from the SQS queue.
- **C.** Use Amazon S3 to store the .json files instead of Amazon EFS.
- **D.** Employ Amazon EC2 Spot Instances for executing the web-crawling process.
- **E.** Use Amazon RDS to store the .json files instead of Amazon EFS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C (you answered correctly)

🔑 **Key words:** EC2 fleet polls SQS, stores .json on EFS; optimize cost

⚠️ **Watch:** EFS costlier than S3 for object output

🧠 **Rule:** SQS worker fleet → Lambda triggered by SQS; object output → S3 not EFS.

### TD explanation

AWS Lambda is a serverless compute service that lets you run your code without provisioning or managing servers. It automatically scales your application in response to the volume of incoming messages in the SQS queue. This would be more cost-effective during periods of low health update volumes.

Amazon S3 offers an easy-to-use web services interface for storing and accessing large amounts of data from anywhere on the internet at any time. It provides developers with access to Amazon’s highly scalable, reliable, and cost-effective data storage infrastructure, which powers its global network of websites. The service is designed to leverage the advantages of scale and make them available to developers.

Hence, the correct answers are:

– Replace the EC2 instances with AWS Lambda functions to fetch and process data from the SQS queue.

– Use Amazon S3 to store the .json files instead of Amazon EFS.

The option that says: Employ Amazon EC2 Spot Instances for executing the web-crawling process is incorrect because Spot Instances are subject to availability in the Spot pool and can be interrupted with two minutes of notification when EC2 needs the capacity back. This could disrupt the real-time updates needed for the system.

The option that says: Use Amazon Neptune to store the .json files instead of Amazon EFS is incorrect because Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. It’s not designed for storing .json files.

The option that says: Use Amazon RDS to store the .json files instead of Amazon EFS is incorrect because Amazon RDS is a relational database service and is not suitable for storing .json files. It would also likely be more expensive than using EFS or S3.

References:

https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html

https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html

 

Check out these AWS Lambda and Amazon S3 Cheat Sheets:

https://tutorialsdojo.com/aws-lambda/

https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q56"></a>

## Q56

A company is developing a serverless application that is deployed on AWS Lambda. The application consists of several Lambda functions that resize, watermark, and process images. The metadata generated from the functions is written in an Amazon DynamoDB table. The company deployed an Amazon Neptune DB cluster in three private subnets inside a VPC. A new feature was developed that requires the Lambda functions to access the Neptune DB cluster.

Which of the following options are possible solutions to allow the Lambda functions to access both the DynamoDB table and Neptune DB cluster? (Select TWO.)

- **A.** Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Create a DynamoDB VPC endpoint and update the route table for routing DynamoDB requests.
- **B.** Deploy the AWS Lambda functions into three new public subnets in the same VPC. Update the Amazon Neptune DB security group to allow connections from the Lambda security group. Route internet traffic to the Internet Gateway.
- **C.** Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Route the internet traffic of the Lambda functions through a NAT gateway.
- **D.** Keep the AWS Lambda functions outside the VPC. Create a VPC endpoint for the Amazon Neptune service. Update the Lambda functions to use this endpoint to send requests to the Neptune DB cluster.
- **E.** Keep the Lambda functions outside the VPC. Configure the Neptune DB security group to allow inbound access from the AWS Lambda IP range.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C (you answered correctly)

🔑 **Key words:** Lambda must reach Neptune in private subnets + DynamoDB

⚠️ **Watch:** Lambda in VPC loses internet → endpoint or NAT

🧠 **Rule:** Lambda to VPC resource → Lambda in private subnets + SG rule; DynamoDB via gateway endpoint or NAT.

### TD explanation

Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Neptune is a purpose-built, high-performance graph database engine. This engine is optimized for storing billions of relationships and querying the graph with milliseconds latency.

You can configure a Lambda function to connect to private subnets in a virtual private cloud (VPC) in your AWS account. Use Amazon Virtual Private Cloud (Amazon VPC) to create a private network for resources such as databases, cache instances, or internal services. Connect your function to the VPC to access private resources while the function is running.

When you connect a function to a VPC, Lambda assigns your function to a Hyperplane ENI (elastic network interface) for each subnet in your function’s VPC configuration. Lambda creates a Hyperplane ENI the first time a unique subnet and security group combination is defined for a VPC-enabled function in an account.

Internet access from a private subnet requires network address translation (NAT). To give internet access to an Amazon VPC-connected Lambda function, route its outbound traffic to a NAT gateway or NAT instance in a public subnet. Lambda functions do not, and cannot, have public IP addresses. You cannot send traffic to the internet, which happens via the VPC’s Internet Gateway, unless you have a public IP.

The option that says: Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Create a DynamoDB VPC endpoint and update the route table for routing DynamoDB requests is correct. In the private subnet, the Lambda functions can directly access the Neptune DB cluster, and the DynamoDB table via the DynamoDB VPC endpoint.

The option that says: Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Route the internet traffic of the Lambda functions through a NAT gateway is correct. Since DynamoDB is accessed via HTTPS API calls on the internet, you can use a NAT gateway to allow private resources, such as the Lambda functions, to route their traffic to the internet.

The option that says: Deploy the AWS Lambda functions into three new public subnets in the same VPC. Update the Amazon Neptune DB security group to allow connections from the Lambda security group. Route internet traffic to the Internet Gateway is incorrect. You can deploy Lambda functions on a public subnet. However, since Lambda functions typically do not have a public IP, they can’t directly access the internet even if you associate an internet gateway to the VPC.

The option that says: Keep the AWS Lambda functions outside the VPC. Create a VPC endpoint for the Amazon Neptune service. Update the Lambda functions to use this endpoint to send requests to the Neptune DB cluster is incorrect. Since the Neptune DB cluster is in a private subnet, it is not exposed to the outside world. A VPC endpoint is exposed only to resources inside a VPC, so Lamdba functions can’t connect to it either.

The option that says: Keep the Lambda functions outside the VPC. Configure the Neptune DB security group to allow inbound access from the AWS Lambda IP range is incorrect. Lambda functions by default are created outside a VPC and they can’t access any resources that are inside a VPC.

References:

https://docs.aws.amazon.com/neptune/latest/userguide/intro.html

https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html

https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/

Check out these Amazon VPC and AWS Lambda Cheat Sheets:

https://tutorialsdojo.com/amazon-vpc/

https://tutorialsdojo.com/aws-lambda/

</details>

<a id="q64"></a>

## Q64

A company is developing a containerized web application using the .NET Core framework which is packaged as a Docker container. This application will serve public traffic and the management wants to deploy it in AWS. The application requires a highly-available Microsoft SQL Server as its database backend. As a security best practice, the SQL Server connection string should not be saved inside the container to avoid exposing the database password.

Which of the following options should the Solutions Architect implement to deploy the application in AWS while satisfying the company requirements?

- **A.** Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the Fargate service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers.
- **B.** Deploy the SQL Server in an AWS Fargate cluster with Service Auto Scaling. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create another Fargate Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers.
- **C.** Deploy the SQL Server in an Auto Scaling group of Amazon EC2 instances. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers.
- **D.** Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create an Amazon EKS Distro cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an IAM role associated with the EKS service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s pod definition. Create an empty non-persistent volume attachment in the pod definition. This allows EKS to write the database credentials to the non-persistent volume when starting the containers.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** containerized .NET; HA SQL Server; connection string not in container

⚠️ **Watch:** Secrets never in image

🧠 **Rule:** HA SQL Server → RDS Multi-AZ; creds → Secrets Manager injected into Fargate task.

### TD explanation

Amazon RDS supports DB instances running several versions and editions of Microsoft SQL Server. Amazon RDS currently supports Multi-AZ deployments for SQL Server using SQL Server Database Mirroring (DBM) or Always On Availability Groups (AGs) as a high-availability, failover solution.

AWS Secrets Manager enables you to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. This helps ensure the secret can’t be compromised by someone examining your code because the secret no longer exists in the code. Also, you can configure Secrets Manager to automatically rotate the secret for you according to a specified schedule. This enables you to replace long-term secrets with short-term ones, significantly reducing the risk of compromise.

Amazon ECS enables you to inject sensitive data into your containers by storing your sensitive data in AWS Secrets Manager secrets and then referencing them in your container definition. Sensitive data stored in Secrets Manager secrets can be exposed to a container as environment variables or as part of the log configuration. In the Task Definition, you can instruct Fargate tasks to securely grab secrets from Secrets Manager so that these secrets are never exposed in the wild—not even in private configuration files. This frees you from the burden of having to implement the undifferentiated heavy lifting of securing these secrets.

When you inject a secret as an environment variable, you can specify the full contents of a secret, a specific JSON key within a secret, or a specific version of a secret to inject. This helps you control the sensitive data exposed to your container.

Therefore, the correct answer is: Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the Fargate service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers.

The option that says: Deploy the SQL Server in an AWS Fargate cluster with Service Auto Scaling. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create another Fargate Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers is incorrect. Deploying the SQL Server in a Fargate cluster is not recommended because you will need persistent and durable storage. You should use Amazon RDS for SQL Server instead.

The option that says: Deploy the SQL Server in an Auto Scaling group of Amazon EC2 instances. Create an encrypted parameter in AWS SSM Parameter Store to store the database credentials. Create a Fargate cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an ECS task execution role associated with the application service that allows fetching of parameters from SSM Parameter Store. Specify the ARN of the database parameter in the environment variable section of the application’s task definition. This allows Fargate to inject the database credentials as an environment variable when starting the containers is incorrect. This solution is feasible, but deploying the SQL Server in an Auto Scaling group of EC2 instances is not recommended. You should use Amazon RDS for SQL Server with Multi-AZ instead so that AWS can manage the replication and availability of the cluster.

The option that says: Deploy the SQL Server on Amazon RDS with Multi-AZ enabled. Create a secret in AWS Secrets Manager to store the database credentials. Create an Amazon EKS Distro cluster with Service Auto Scaling for the application tasks which are placed behind an Application Load Balancer with multiple Availability Zones. Create an IAM role associated with the EKS service that allows fetching of secrets from Secrets Manager. Specify the ARN of the database secret in the environment variable section of the application’s pod definition. Create an empty non-persistent volume attachment in the pod definition. This allows EKS to write the database credentials to the non-persistent volume when starting the containers is incorrect because using Amazon EKS Distro adds complexity as it’s not a managed service. Storing credentials in a non-persistent volume could lead to loss of data if the pod is terminated. It might be simpler to use a service more integrated with Docker, like Amazon ECS or AWS Fargate, given that your application is a Docker container.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html

https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html

https://docs.aws.amazon.com/AmazonECS/latest/userguide/specifying-sensitive-data-secrets.html

https://aws.amazon.com/blogs/compute/securing-credentials-using-aws-secrets-manager-with-aws-fargate/

 

Check out these AWS Fargate and AWS Secrets Manager Cheat Sheets:

https://tutorialsdojo.com/aws-fargate/

https://tutorialsdojo.com/aws-secrets-manager/

</details>

---

# Group F — Networking / S3 / perf (6)

<a id="q3"></a>

## Q3

A company has developed an Optical Character Recognition (OCR) application that allows users to upload PDF files to an Amazon S3 bucket. The user-facing website is hosted on S3, and its content is distributed by Amazon CloudFront. When a user initiates an OCR job, the application makes a call to a REST API in Amazon API Gateway (Regional), which in turn invokes an AWS Lambda function asynchronously to start the OCR process. The OCR output’s S3 path is then stored in an Amazon DynamoDB table

Currently, the application stack is deployed in the us-east-1 AWS region. The company wants to expand its user base to include users from Asia and the Middle East and aims to improve latency for these users.

Which combination of steps is the most cost-effective approach that would meet this requirement? (Select TWO.)

- **A.** Enable S3 Transfer Acceleration on the S3 bucket and update the application code to use the Transfer Acceleration endpoint.
- **B.** Upload the PDF files to an Amazon EBS-backed Amazon EC2 instance in the us-east-1 region. Create an AWS Global Accelerator for the EC2 instance. Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.
- **C.** Deploy additional Lambda functions and S3 buckets in Asia and Middle East regions. Set up cross-region S3 replication. Configure Route 53 Geolocation Routing to direct users to the closest regional resources.
- **D.** Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.
- **E.** Migrate the DynamoDB table to Amazon Aurora Serverless and use an Amazon RDS Proxy in front of the Lambda function.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D (you answered correctly)

🔑 **Key words:** global users upload PDFs to S3; Regional API GW; slow for distant users

⚠️ **Watch:** Transfer Acceleration = uploads to S3; edge-optimized = API latency

🧠 **Rule:** Global uploads → S3 Transfer Acceleration; global API callers → edge-optimized endpoint.

### TD explanation

Amazon S3 Transfer Acceleration can speed up content transfers to and from Amazon S3 by as much as 50% – 500% for long-distance transfer of larger objects. Customers who have either web or mobile applications with widespread users or applications hosted far away from their S3 bucket can experience long and variable upload and download speeds over the Internet.

S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrive at an edge location, they are routed to Amazon S3 over an optimized network path.

In the given scenario, since Amazon CloudFront is already in use for distributing content, the focus for reducing latency should be on the user’s interactions with the API and the S3 bucket where PDF files are uploaded. Enabling Amazon S3 Transfer Acceleration (S3TA) would speed up file uploads to the bucket, while switching the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint would enhance API call performance for users worldwide, including those in Asia and the Middle East

Hence, the correct answers are:

– Enable S3 Transfer Acceleration on the S3 bucket and update the application code to use the Transfer Acceleration endpoint.

– Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.

The option that says: Migrate the DynamoDB table to Amazon Aurora Serverless and use an Amazon RDS Proxy in front of the Lambda function is incorrect. Simply switching to a relational database would not address the latency concerns for users in Asia and the Middle East.

The option that says: Upload the PDF files to an Amazon EBS-backed Amazon EC2 instance in the us-east-1 region. Create an AWS Global Accelerator for the EC2 instance. Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint is incorrect. The use of an EC2 instance would not only introduce additional operational overhead but also incur higher costs. AWS Global Accelerator is unnecessary since CloudFront is already handling global content distribution and latency reduction for HTTP/HTTPS content.

The option that says: Deploy additional Lambda functions and S3 buckets in Asia and Middle East regions. Set up cross-region S3 replication. Configure Route 53 Geolocation Routing to direct users to the closest regional resources is incorrect. Cross-region replication in Amazon S3 is typically used for disaster recovery, data archiving, or data migration purposes. Having multiple copies of data in different regions would increase storage costs.

 

References:

https://aws.amazon.com/s3/transfer-acceleration/

https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html

 

Check out these Amazon S3 and Amazon API Gateway Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-api-gateway/

</details>

<a id="q6"></a>

## Q6

A digital marketing firm is planning to integrate its local servers with AWS for better scalability. The firm has chosen a 200 Mbps AWS Direct Connect connection for this integration. The proposed setup includes a transit gateway and a Direct Connect gateway to ensure smooth communication between several Amazon VPCs and the local servers.

The firm needs to make sure that its local servers can interact with the VPC resources through a transit virtual interface (VIF) using the Direct Connect connection.

Which two actions should the firm take to achieve these requirements? (Select TWO.)

- **A.** Use the same Connection Key Name (CKN) and Connectivity Association Key (CAK) for all Direct Connect connections.
- **B.** Upgrade the Direct Connect connection from 200 Mbps to 500 Mbps.
- **C.** Configure the Direct Connect connection by setting the MACsec encryption mode parameter to must_encrypt.
- **D.** Advertise the allowed prefixes to a range that is the same or wider than the VPC CIDR block on the Direct Connect gateway.
- **E.** Advertise the VPC prefixes list on the Direct Connect gateway for the transit gateway association.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D, E (you answered correctly)

🔑 **Key words:** DX + Transit Gateway + DX Gateway; on-prem reach VPCs

⚠️ **Watch:** Allowed prefixes must cover VPC CIDRs

🧠 **Rule:** DX Gateway ↔ TGW → advertise allowed prefixes = VPC CIDR (same or wider).

### TD explanation

The prefix list, which includes IPv4 and IPv6 addresses, is a filter that permits the same or a smaller range of CIDRs to be promoted to the Direct Connect gateway. When setting up a Direct Connect gateway, it’s important to set the allowed prefixes to a range that is the same or wider than the VPC CIDR block. This ensures that all IP addresses within the VPC can be reached from the local servers.

If you want to connect your AWS Direct Connect connection to the VPCs or VPNs that are attached to your transit gateway, you can use an AWS Direct Connect gateway. To do this, you need to associate a Direct Connect gateway with the transit gateway and create a transit virtual interface for your AWS Direct Connect connection to the Direct Connect gateway.

Provisioning the allowed prefixes list on the Direct Connect gateway is a necessary step. This list is used to route on-premises traffic to or from a Direct Connect gateway to the transit gateway, even when the VPCs attached to the transit gateway do not have assigned CIDRs. This setup ensures that the local servers can interact with the AWS VPC resources through the transit VIF.

Hence, the correct answers are:

– Advertise the allowed prefixes to a range that is the same or wider than the VPC CIDR block on the Direct Connect gateway.

– Advertise the VPC prefixes list on the Direct Connect gateway for the transit gateway association.

The option that says: Upgrade the Direct Connect connection from 200 Mbps to 500 Mbps is incorrect because while upgrading the connection speed typically improves performance, it is not necessary for the local servers to interact with the AWS VPC resources. The question does not indicate that the current speed is insufficient.

The option that says: Configure the Direct Connect connection by setting the MACsec encryption mode parameter to must_encrypt is incorrect because it is not necessary for the local servers to interact with the Amazon VPC resources through a transit virtual interface (VIF) using the Direct Connect connection. The encryption mode parameter does not affect the interaction between the servers and VPC resources.

The option that says: Use the same Connection Key Name (CKN) and Connectivity Association Key (CAK) for all Direct Connect connections is incorrect because the CKN and CAK are primarily used for MACsec encryption. Using the same keys for all connections would not be a good security practice, and it is not necessary for the local servers to interact with the AWS VPC resources.

 

References:

https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html

https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html

 

Check out this AWS Direct Connect Gateway Cheat Sheet:

https://tutorialsdojo.com/aws-direct-connect/

</details>

<a id="q7"></a>

## Q7

A company uses Amazon EC2 instances to host development and production workloads in the us-east-1 region. The instances are spread across multiple AWS accounts under the AWS Organization of the main company account. Every VPC on the us-east-1 region hosts either a development or production workload. All EC2 instances under the organization that have the same environment must be able to communicate with each other, while EC2 instances in different environments must not be able to communicate with each other. To accomplish this requirement, the company created a common network account and used the AWS Transit Gateway service. A transit gateway is created in the us-east-1 region and with the help of AWS Resource Access Manager, it is shared with the entire AWS Organization. Each VPC is then attached to the transit gateway to allow communication between the EC2 instances. However, this also allowed communication between the production and development EC2 instances.

Which of the following implementation would ensure that the development traffic is isolated from the production traffic?

- **A.** Create a network tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Configure the AWS Transit Gateway route table to allow production tagged attachments to communicate with other production tagged attachments. Set up the same configuration for development tagged attachments.
- **B.** Create an env tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Create policies to restrict traffic between the development and production VPCs based on the tag by using the AWS Transit Gateway Network Manager.
- **C.** Configure the attached security groups of the production Amazon EC2 instances to block traffic from the development EC2 instances. Configure the attached security groups of the development EC2 instances to block traffic from the production EC2 instances.
- **D.** Delete each account’s route propagation and association to the default route table of the AWS Transit Gateway. Create two separate transit gateway route tables for development and production environments. Attach each VPC to their respective route tables and enable route propagation for each attachment.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** multi-account VPCs via TGW; dev↔dev, prod↔prod, no dev↔prod

⚠️ **Watch:** Default TGW route table connects everything

🧠 **Rule:** Segmentation on TGW → separate route tables per environment, disable default association/propagation.

### TD explanation

A transit gateway enables you to attach VPCs and VPN connections in the same Region and route traffic between them. A transit gateway works across AWS accounts, and you can use AWS RAM to share your transit gateway with other accounts. After you share a transit gateway with another AWS account, the account owner can attach their VPCs to your transit gateway. A user from either account can delete the attachment at any time.

You can enable multicast on a transit gateway, and then create a transit gateway multicast domain that allows multicast traffic to be sent from your multicast source to multicast group members over VPC attachments that you associate with the domain.

Each VPC or VPN attachment is associated with a single route table. That route table decides the next hop for the traffic coming from that resource attachment. A route table inside the transit gateway allows for both IPv4 or IPv6 CIDRs and targets. The targets are VPCs and VPN connections. When you attach a VPC or create a VPN connection on a transit gateway, the attachment is associated with the default route table of the transit gateway.

You can create additional route tables inside the transit gateway, and change the VPC or VPN association to these route tables. This enables you to segment your network. For example, you can associate development VPCs with one route table and production VPCs with a different route table. This enables you to create isolated networks inside a transit gateway similar to virtual routing and forwarding (VRFs) in traditional networks.

Therefore, the correct answer is: Delete each account’s route propagation and association to the default route table of the AWS Transit Gateway. Create two separate transit gateway route tables for development and production environments. Attach each VPC to their respective route tables and enable route propagation for each attachment. This enables you to segment your network. With this method, you can associate development VPCs with one route table and production VPCs with a different route table.

The option that says: Create an env tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Create policies to restrict traffic between the development and production VPCs based on the tag by using the AWS Transit Gateway Network Manager is incorrect. AWS Transit Gateway Network Manager is used to monitor network activity into a single dashboard. It is not used for creating network policies.

The option that says: Configure the attached security groups of the production Amazon EC2 instances to block traffic from the development EC2 instances. Configure the attached security groups of the development EC2 instances to block traffic from the production EC2 instances is incorrect. Security groups can only allow traffic, not block traffic.

The option that says: Create a network tag for each VPC attachment and assign a value of development or production depending on the environment of that VPC. Configure the AWS Transit Gateway route table to allow production tagged attachments to communicate with other production tagged attachments. Set up the same configuration for development tagged attachments is incorrect. You can tag your VPC attachments to identify them on the AWS Console, however, this tag cannot be used as a basis for network routing. 

 

References:

https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html

https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html

https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html

 

Check out this AWS Transit Gateway Cheat Sheet:

https://tutorialsdojo.com/aws-transit-gateway/

</details>

<a id="q17"></a>

## Q17

A company has several Amazon FSx for Windows File Server deployments in multiple AWS accounts. The solutions architect is conducting a performance review on all Amazon for FSx file deployments to comply with the company policy that requires all file systems to be configured to be highly available in at least two Availability Zones. The solutions architect found some Amazon FSx file systems that use a deployment type of Single-AZ. These must be corrected while minimizing downtime that could affect other application components.

Which of the following option is the recommended action to meet the company requirements?

- **A.** Use AWS DataSync to copy data to a new Amazon FSx file system that uses a Multi-AZ deployment type. After copying, point the applications to use the new Amazon FSx share.
- **B.** Take a backup of the current Amazon FSx file system. Restore this backup to a new Amazon FSx file system with a deployment type of Multi-AZ. After restoration, point the applications to use the new Amazon FSx share.
- **C.** Use AWS DataSync to continuously sync data to a second Amazon FSx file system that uses a Single-AZ deployment type. In the event of failure, point the applications to use the second Amazon FSx share.
- **D.** On the AWS management console, update the Amazon FSx file system to use a Multi-AZ deployment type.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** FSx for Windows Single-AZ must become Multi-AZ

⚠️ **Watch:** Deployment type is immutable

🧠 **Rule:** FSx Single-AZ → Multi-AZ: new Multi-AZ file system + DataSync copy + repoint apps.

### TD explanation

Amazon FSx for Windows File Server offers two file system deployment types: Single-AZ and Multi-AZ.

With Single-AZ file systems, Amazon FSx automatically replicates your data within an Availability Zone (AZ) to protect it from component failure. It continuously monitors for hardware failures and automatically replaces infrastructure components in the event of a failure. Amazon FSx also uses the Windows Volume Shadow Copy Service to make highly durable backups of your file system daily and store them in Amazon S3.

Multi-AZ file systems support all the availability and durability features of Single-AZ file systems. In addition, they are designed to provide continuous availability to data, even when an Availability Zone is unavailable. In a Multi-AZ deployment, Amazon FSx automatically provisions and maintains a standby file server in a different Availability Zone. Any changes written to disk in your file system are synchronously replicated across Availability Zones to the standby. With Amazon FSx Multi-AZ deployments can enhance availability during planned system maintenance, and help protect your data against instance failure and Availability Zone disruption. If there is planned file system maintenance or unplanned service disruption, Amazon FSx automatically fails over to the secondary file server, allowing you to continue accessing your data without manual intervention.

Multi-AZ file systems are ideal for business-critical workloads that require high availability to shared Windows file data. Examples of these include business applications, web serving environments, and Microsoft SQL Server.

Therefore, the correct answer is: Use AWS DataSync to copy data to a new Amazon FSx file system that uses a Multi-AZ deployment type. After copying, point the applications to use the new Amazon FSx share. AWS DataSync will continuously replicate data between the FSx share until you are able to point the application to the new share.

The option that says: Take a backup of the current Amazon FSx file system. Restore this backup to a new Amazon FSx file system with a deployment type of Multi-AZ. After restoration, point the applications to use the new Amazon FSx share is incorrect. This is possible, however, after the data backup is complete, new data may have been written on the original FSx share. You should use AWS Data Sync to sync data between the shares.

The option that says: Use AWS DataSync to continuously sync data to a second Amazon FSx file system that uses a Single-AZ deployment type. In the event of failure, point the applications to use the second Amazon FSx share is incorrect. This is still non-compliant because the FSx file system is deployed on a Single-AZ. It will also introduce unnecessary downtime if you can’t detect the failure of the primary FSx share.

The option that says: On the AWS management console, update the Amazon FSx file system to use a Multi-AZ deployment type is incorrect. It is not possible to update the deployment type of the FSx file system once it is created. You will need to re-create the file system for this scenario.

 

References:

https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html

https://aws.amazon.com/blogs/aws/amazon-fsx-for-windows-file-server-update-new-enterprise-ready-features/

https://aws.amazon.com/fsx/windows/faqs/

 

Check out these Amazon FSx and AWS DataSync Cheat Sheets:

https://tutorialsdojo.com/amazon-fsx/

https://tutorialsdojo.com/aws-datasync/

</details>

<a id="q27"></a>

## Q27

A company runs an auction website using AWS Fargate fronted by an Application Load Balancer (ALB). The company manages an Amazon Route 53 hosted zone for its domain, which it presents to users. The domain is linked to a CloudFront distribution that points to the ALB as the origin.

Lately, there have been reports of intermittent HTTP 502 (Bad Gateway) errors. Initial investigation revealed that a misconfiguration in the Fargate task definition is causing the problem. This results in users seeing the ALB’s default error page.

To improve user experience, the company wants users to be redirected to a custom error page while they troubleshoot the issue. The solution must be achieved in the least amount of operational overhead.

Which solution would meet the requirements?

- **A.** Upload the error HTML page to an Amazon S3 bucket and enable static website hosting. Update the existing Route 53 record by adding a failover policy that routes traffic to the S3 website endpoint when health checks become unhealthy.
- **B.** Upload an error HTML page to an Amazon S3 bucket that is configured with static website hosting. Modify the CloudFront distribution by adding a new origin for the S3 bucket and enforcing Origin Access Control (OAC). Create a CloudFront custom error response that returns the error page when the application returns a 502 HTTP error code as an origin failover
- **C.** Create a Lambda function that adds a redirection rule to the path of the error page within the application. Configure a CloudWatch alarm to trigger this Lambda function when the Application Load Balancer (ALB) metric HTTPCode_Target_5XX_Count registers a value of one.
- **D.** Modify the Application Load Balancer’s rules by adding a condition for the path /*. Configure a fixed-response action that returns a 502 response code and a custom error message in the response body.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** CloudFront → ALB; intermittent 502; show custom error page

⚠️ **Watch:** Error page must live outside the failing origin

🧠 **Rule:** Custom error page → S3 origin (OAC) + CloudFront custom error response.

### TD explanation

Normally, when an object served through CloudFront is unavailable, the web server will return an HTTP status code to CloudFront to indicate the problem. For example, if a client requests an invalid URL, your web server would return an HTTP 404 (Not Found) status code to CloudFront, and CloudFront would relay that status code back to the client.

However, with CloudFront’s custom error response feature, you can configure CloudFront to return a custom error page to the viewer instead. This customization can be done by updating your CloudFront distribution to specify the custom error page.

You can specify an origin group for your CloudFront origin if, for example, you want to configure origin failover for scenarios when you need high availability. Use origin failover to designate a primary origin for CloudFront plus a second origin that CloudFront automatically switches to when the primary origin returns specific HTTP status code failure responses.

In the given scenario, the most straightforward approach to displaying a custom error page is by uploading the page to an Amazon S3 bucket, and then adding that bucket as an origin in the existing CloudFront distribution. Then, you configure a custom error response within CloudFront, pointing it to the path of the error page stored in the S3 bucket. This method has minimal operational overhead and does not require any coding.

Therefore, the correct answer is: Upload an error HTML page to an Amazon S3 bucket that is configured with static website hosting. Modify the CloudFront distribution by adding a new origin for the S3 bucket and enforcing Origin Access Control (OAC). Create a CloudFront custom error response that returns the error page when the application returns a 502 HTTP error code as an origin failover.

The option that says: Create a Lambda function that adds a redirection rule to the path of the error page within the application. Configure a CloudWatch alarm to trigger this Lambda function when the Application Load Balancer (ALB) metric HTTPCode_Target_5XX_Count registers a value of one is incorrect. This option presents unnecessary development overhead for the purpose of simply displaying a custom error page. This solution also doesn’t provide an instant response to users experiencing a 502 error, as there might be a delay between the error occurrence and the CloudWatch alarm triggering the Lambda function.

The option that says: Upload the error HTML page to an Amazon S3 bucket and enable static website hosting. Update the existing Route 53 record by adding a failover policy that routes traffic to the S3 website endpoint when health checks become unhealthy is incorrect. This approach is more suited for scenarios where there is a complete failure of the primary endpoint rather than intermittent errors. The health checks may not register a failure if the 502 errors are sporadic and the system is generally operational, thus the failover might not be triggered.

The option that says: Modify the Application Load Balancer’s rules by adding a condition for the path /*. Configure a fixed-response action that returns a 502 response code and a custom error message in the response body is incorrect. Although this could provide some level of customization, it does not fully meet the requirement of redirecting users to a custom error page. Instead, it just modifies the response body of the error. Moreover, using a fixed-response rule at the root path will return a 502 response for all requests, regardless of their paths, essentially blocking all requests.

 

References:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GeneratingCustomErrorResponses.html

https://aws.amazon.com/blogs/aws/custom-error-pages-and-responses-for-amazon-cloudfront/

 

Check out the Amazon CloudFront Cheat Sheet:

https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q37"></a>

## Q37

A global e-commerce company has a complex microservices architecture deployed on multiple AWS accounts. Each microservice has its own VPC, and all VPC flow logs are sent to a centralized Amazon S3 bucket in Text format. These logs are compressed using the gzip compression method and are kept indefinitely for compliance reasons.

A data analytics team frequently uses Amazon Redshift Spectrum to analyze and query these logs. However, as the number of logs increases, the performance of their data visualizations is decreasing. The company’s lead architect is tasked with improving the performance of the data visualizations and reducing the storage space used by the VPC flow logs.

Which solution will provide the MOST significant improvement in performance?

- **A.** Store the VPC flow logs in multiple S3 buckets instead of a single centralized bucket.
- **B.** Compress the VPC flow logs using a different compression method like bzip2 instead of gzip.
- **C.** Update the log configuration on the VPC Flow log to output in Parquet format and partition the data by hour.
- **D.** Implement AWS Glue to catalog the VPC flow logs.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** VPC flow logs gzip text in S3; Redshift Spectrum queries slow/costly

⚠️ **Watch:** Columnar + partitioned = less data scanned

🧠 **Rule:** Query-heavy logs → Parquet output + hourly partitions.

### TD explanation

VPC Flow Logs allow you to capture information about the IP traffic going to and from network interfaces in your VPC. This can be useful for a variety of reasons, such as understanding network traffic patterns, identifying potential security issues, auditing usage, and diagnosing network connectivity issues.

These logs are often sent directly to Amazon S3 for long-term storage. However, they are initially stored as raw text files in GZIP format. While this format is useful for certain use cases, it can add complexity and increase costs when it comes to analyzing the log data.

Apache Parquet is an open-source file format that is optimized for use with big data processing frameworks. It stores data in a columnar format, which means it organizes the data by columns rather than by rows. This can lead to significant performance improvements when executing analytical queries.

In addition, Parquet provides different encoding types and supports predicate filtering, which allows non-relevant data to be skipped during queries. This results in fewer reads on Amazon S3 and improved query performance. Furthermore, due to its efficient encoding and good compression ratios, storing VPC flow logs in Parquet format can also help reduce your Amazon S3 storage costs.

Hence, the correct answer is: Update the log configuration on the VPC Flow log to output in Parquet format and partition the data by hour.

The option that says: Compress the VPC flow logs using a different compression method like bzip2 instead of gzip is incorrect because while bzip2 might provide slightly better compression ratios than gzip, the difference is not significant enough to result in a substantial performance improvement. Also, the time taken to compress and decompress bzip2 files is generally more than gzip, which could offset any gains from the slightly better compression ratio.

The option that says: Store the VPC flow logs in multiple S3 buckets instead of a single centralized bucket is incorrect because storing VPC flow logs in multiple S3 buckets would not improve the performance of data visualizations. It might even complicate the data management process without providing any significant benefits.

The option that says: Implement AWS Glue to catalog the VPC flow logs is incorrect because while AWS Glue can be used to catalog data, it does not inherently improve the performance of data visualizations. AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load your data for analytics, but it does not optimize the data for these operations.

 

References:

https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/

https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

 

Check out this Amazon VPC Cheat Sheet:

https://tutorialsdojo.com/amazon-vpc/

</details>
