# Review Mode td6_isolated – AWS Certified Solutions Architect Professional (Tutorials Dojo)

**Kết quả:** 11/16 câu đúng (68.75%) — ❌ Chưa đạt

**Unseen only:** 11/16 (69%) · **Mode:** review, blocks of 25 · **Date:** 2026-10-13

## Điểm theo domain

| Domain | Tỉ lệ đúng |
|---|---|
| CSAP – Accelerate Workload Migration and Modernization | 100.00% |
| CSAP – Continuous Improvement for Existing Solutions | 40.00% |
| CSAP – Design Solutions for Organizational Complexity | 71.43% |
| CSAP – Design for New Solutions | 100.00% |

## Bảng tổng hợp

| Câu | TD Q | Kết quả | Bạn chọn | Đáp án đúng |
|---|---|---|---|---|
| 1 | Q11 | ❌ Sai | B | A |
| 2 | Q6 | ✅ Đúng | D | D |
| 3 | Q14 | ✅ Đúng | B | B |
| 4 | Q2 | ✅ Đúng | A | A |
| 5 | Q4 | ✅ Đúng | D | D |
| 6 | Q9 | ❌ Sai | A, B, C | A, B, F |
| 7 | Q8 | ✅ Đúng | A, B | A, B |
| 8 | Q7 | ✅ Đúng | C | C |
| 9 | Q1 | ✅ Đúng | C | C |
| 10 | Q10 | ✅ Đúng | A | A |
| 11 | Q3 | ❌ Sai | B | A |
| 12 | Q15 | ✅ Đúng | C | C |
| 13 | Q12 | ✅ Đúng | A | A |
| 14 | Q5 | ✅ Đúng | C | C |
| 15 | Q13 | ❌ Sai | A | B |
| 16 | Q16 | ❌ Sai | C | A |

---

## Câu 1 — ❌ SAI

### Câu hỏi

A research company specializing in agricultural innovation operates a fleet of IoT devices across experimental farms to automate and monitor water distribution, temperature regulation, and humidity control. The collected telemetry data is stored in Optimized Row Columnar (ORC) format within the Hadoop Distributed File System (HDFS), running on a persistent Amazon EMR cluster. The company’s data analytics team runs SQL queries using Apache Presto on the same always-on EMR environment. These queries scan large datasets, complete within 15 minutes, and are executed only between 6 PM and 2 AM as part of the company’s nightly analysis routine.
With cloud costs climbing, the research company’s leadership seeks a more cost-effective solution to support these recurring SQL-based data queries. A solutions architect must recommend the most economical approach while maintaining query performance and compatibility with the existing ORC data format.
What is the most cost-effective recommendation that the solutions architect can make?

### Các phương án

- **A.** Persist data in Amazon S3, and execute SQL-based analytics through Amazon Athena, using schema definitions stored in the AWS Glue Data Catalog. ✅
- **B.** Load your datasets into Amazon Redshift and perform analytics directly within the Redshift data warehouse environment. 👈 *(bạn chọn)*
- **C.** Use AWS Glue ETL jobs to ingest the ORC files into Amazon Aurora and enable SQL-based querying.
- **D.** Use AWS Lambda functions to convert the ORC files into JSON and store them in Amazon DynamoDB for querying.

> **Bạn chọn:** B  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds.
Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. Athena scales automatically, running queries in parallel, so results are fast, even with large datasets and complex queries.

Athena can read data directly from Amazon S3 in ORC format, making it highly compatible with the company’s existing dataset. The AWS Glue Data Catalog serves as the centralized metadata store, allowing Athena to interpret and query the structure of the ORC files. Since the research company only needs to run queries during a narrow time window each night, keeping a persistent EMR cluster active is simply wasteful. Athena is cost-effective because the company is billed just for the data scanned per query, and the infrastructure does not need to run continuously, reducing compute-related expenses.
Hence, the correct answer is: Persist data in Amazon S3, and execute SQL-based analytics through Amazon Athena, using schema definitions stored in the AWS Glue Data Catalog.
The option that says: Load your datasets into Amazon Redshift and perform analytics directly within the Redshift data warehouse environment is incorrect. Amazon Redshift is a provisioned data warehouse that incurs ongoing compute and storage costs, regardless of whether queries are being executed. It is primarily designed for high-throughput, continuous analytical workloads, not intermittent query patterns that only occur during a specific time window. Additionally, Redshift does not natively support querying ORC files stored in HDFS. The data must be loaded into Redshift tables, introducing unnecessary overhead.
The option that says: Use AWS Glue ETL jobs to ingest the ORC files into Amazon Aurora and enable SQL-based querying is incorrect. Amazon Aurora is a relational database optimized for transactional workloads, not for large-scale analytics on ORC-formatted files. Using AWS Glue ETL jobs to transform and load ORC data into Aurora introduces processing and storage costs that are simply unnecessary for the use case. Aurora does not support the high-volume data scanning common in big data SQL workloads, making this solution technically inappropriate and financially inefficient.
The option that says: Use AWS Lambda functions to convert the ORC files into JSON and store them in Amazon DynamoDB for querying is incorrect. Amazon DynamoDB is a NoSQL key-value and document database optimized primarily for low-latency, high-throughput transactional operations, not for complex SQL-based analytics across large datasets. Converting ORC files to JSON introduces unnecessary transformation overhead, and using Lambda for this task is simply unsuitable due to its memory and execution time limits, especially when handling large ORC files. Additionally, DynamoDB does not support SQL or efficient data scanning for analytical queries, making this solution technically invalid and economically impractical for the company’s use case.

References:
https://docs.aws.amazon.com/athena/latest/ug/what-is.html
https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html

Check out this Amazon Athena Cheat Sheet:
https://tutorialsdojo.com/amazon-athena/

---

## Câu 2 — ✅ ĐÚNG

### Câu hỏi

A tech company that performs large-scale analytics uses an Amazon Redshift cluster with reserved nodes to support its daily data workloads. A recently hired director has initiated a new requirement: generating a deep audit analysis report. This new reporting initiative has introduced complex read queries that are highly CPU-intensive, resulting in unexpected bursts of usage on the Redshift cluster.
The existing setup must continue to handle both read and write queries consistently, even during performance spikes. A solutions architect must propose the most cost-effective solution to address the rising CPU metrics while maintaining system responsiveness and minimizing operational cost.
What is the most economical approach to manage the increased workload introduced by this new reporting initiative?

### Các phương án

- **A.** Launch additional Amazon EC2 instances to scale horizontally Redshift for query parallelization.
- **B.** Export data from Redshift and import it into Amazon RDS PostgreSQL for deep audit analysis during periods of high load.
- **C.** Deploy an Amazon EMR cluster to offload high-load transformation jobs from the main analytics pipeline.
- **D.** Enable concurrency scaling in the Redshift setup to handle spikes in concurrent query loads without impacting performance. 👈 *(bạn chọn)* ✅

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

With Amazon Redshift’s Concurrency Scaling feature, you can support thousands of concurrent users and queries with consistently fast query performance. When you turn on concurrency scaling, Redshift automatically adds additional cluster capacity to process an increase in both read and write queries. Users see the most current data, whether the queries run on the main or concurrency-scaling clusters.
You’re charged for concurrency-scaling clusters only when they’re actively running queries.

Enabling concurrency scaling in Amazon Redshift is the most cost-efficient and operationally elegant solution to address CPU-intensive workload spikes, such as the deep audit analysis report. This feature is designed for situations where query demand temporarily exceeds cluster capacity. It works by automatically adding transient clusters to handle excess read workloads, ensuring that the main cluster can continue to service both read and write operations without latency or disruption. The beauty of this approach lies in its simplicity. This ensures the system remains responsive without permanently overprovisioning resources.
Hence, the correct answer is: Enable concurrency scaling in the Redshift setup to handle spikes in concurrent query loads without impacting performance.
The option that says: Deploy an Amazon EMR cluster to offload high-load transformation jobs from the main analytics pipeline is incorrect. Amazon EMR is robust for distributed data processing, but would only introduce unnecessary complexity in this case. The issue is not about transformation or ETL pipelines. It is about read query concurrency and CPU bottlenecks within the Redshift cluster itself. Offloading workloads to EMR simply doesn’t solve the immediate pressure on Redshift’s compute layer, nor is it primarily focused on short-term spikes. Additionally, EMR adds extra infrastructure to manage and incurs costs, making it neither the simplest nor the most cost-effective option.
The option that says: Launch additional Amazon EC2 instances to scale horizontally Redshift for query parallelization is incorrect. Scaling Amazon Redshift by launching EC2 instances fundamentally misunderstands how Redshift is designed to operate. Redshift is a managed data warehouse that cannot be scaled horizontally through EC2 the way traditional application servers might be. Redshift scaling is handled through built-in features like Elastic Resize or Concurrency Scaling, not EC2 fleets. Trying to scale Redshift with EC2 is not just incorrect; it’s not even technically possible. This option simply doesn’t apply to the way Redshift architecture works.
The option that says: Export data from Redshift and import it into Amazon RDS PostgreSQL for deep audit analysis during periods of high load is incorrect. Exporting Redshift data to Amazon RDS PostgreSQL during high-load periods may sound like an alternative strategy, but it’s a step in the wrong direction. RDS PostgreSQL is designed primarily for transactional workloads, not for handling CPU-heavy, complex analytical queries. Attempting to mirror Redshift’s analytical capabilities in RDS would result in performance degradation, additional data movement pipelines, and more operational overhead. This approach is not only technically mismatched but also simply adds more cost and complexity without addressing the core issues of query concurrency and CPU pressure within Redshift itself.

References:
https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html
https://docs.aws.amazon.com/redshift/latest/dg/welcome.html

Check out this Amazon Redshift Cheat Sheet:
https://tutorialsdojo.com/amazon-redshift/

---

## Câu 3 — ✅ ĐÚNG

### Câu hỏi

An international shipping company with a global fleet runs its cloud operations through a multi-account AWS environment managed by AWS Control Tower. Due to fluctuating fuel costs and rising logistics expenses, the company recently launched a company-wide cost-cutting initiative, including the tech department.
The company uses AWS Organizations for account-level boundaries, AWS Config to ensure compliance standards are met, and AWS Trusted Advisor to surface cost inefficiencies and potential security gaps.
As per the directive of the CTO, in line with company cost-cutting, only Amazon EC2 and Amazon RDS burstable instances should be allowed. All other services not directly supporting the company’s lean tech initiative must be blocked.
A solutions architect has been tasked with locking this down in a scalable, maintainable way aligned with AWS best practices.
What’s the most effective approach to enforce these service restrictions?

### Các phương án

- **A.** Deploy Amazon GuardDuty to scan for unsupported AWS services and non-burstable EC2 or RDS instances. Use its findings to block non-compliant deployments automatically in the future.
- **B.** Define a custom preventive guardrail within AWS Control Tower that enforces restrictions allowing only burstable instance types to be launched, while blocking access to any non-essential services. Assign this control to the target development OU to ensure policy compliance across applicable accounts. 👈 *(bạn chọn)* ✅
- **C.** Enable AWS Trusted Advisor's cost optimization checks in each development account to enforce the usage of burstable instances and prevent launching non-approved services.
- **D.** Set up a custom detective guardrail in AWS Control Tower to monitor the environment for compliance, ensuring that only burstable instances are provisioned and that any usage of unauthorized services is flagged. Link this control to the corresponding OU to track adherence across associated accounts.

> **Bạn chọn:** B  
> **Đáp án đúng:** B  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment, following prescriptive best practices. Its orchestration extends the capabilities of AWS Organizations. To help keep your organizations and accounts from drift, which is divergence from best practices, AWS Control Tower applies controls (sometimes called guardrails).
Preventive controls prevent actions from occurring. For example, the elective control called Disallow Changes to Bucket Policy for Amazon S3 Buckets (Previously called Disallow Policy Changes to Log Archive) prevents IAM policy changes within the log archive shared account. Any attempt to perform a prevented action is denied and logged in CloudTrail. The resource is also logged in AWS Config.
Detective controls detect specific events when they occur and log the action in CloudTrail. For example, the strongly recommended control called Detect Whether Encryption is Enabled for Amazon EBS Volumes Attached to Amazon EC2 Instances detects whether an unencrypted Amazon EBS volume is attached to an EC2 instance in your landing zone.

Custom preventive guardrails in the AWS Control Tower enforce policy before resource deployment. Preventive guardrails are backed by Service Control Policies (SCPs). They are designed to explicitly block actions that violate rules, such as launching non-burstable EC2 or RDS instances or accessing disallowed services. Assigning the control to the target OU ensures the restriction applies across all relevant accounts in a multi-account AWS environment, aligning with AWS best practices and the company’s cost-cutting directive.
Hence, the correct answer is: Define a custom preventive guardrail within AWS Control Tower that enforces restrictions allowing only burstable instance types to be launched, while blocking access to any non-essential services. Assign this control to the target development OU to ensure policy compliance across applicable accounts.
The option that says: Set up a custom detective guardrail in AWS Control Tower to monitor the environment for compliance, ensuring that only burstable instances are provisioned and that any usage of unauthorized services is flagged. Link this control to the corresponding OU to track adherence across associated accounts  is incorrect. Detective guardrails in AWS Control Tower do not block actions. They simply monitor and flag violations after they occur. While they are helpful for auditing and visibility, they cannot enforce restrictions in advance. This lack of enforcement capabilities means that non-burstable instances could still be launched, defeating the purpose of proactively managing costs and service usage.
The option that says: Deploy Amazon GuardDuty to scan for unsupported AWS services and non-burstable EC2 or RDS instances. Use its findings to block non-compliant deployments automatically in the future is incorrect. Amazon GuardDuty is primarily a threat detection service for identifying potential security risks like compromised resources or unusual API calls. It is not designed to enforce service usage policies or instance-type restrictions. One cannot rely on GuardDuty to block deployments, as it does not have preventive capabilities in this context.
The option that says: Enable AWS Trusted Advisor’s cost optimization checks in each development account to enforce the usage of burstable instances and prevent launching non-approved services is incorrect. AWS Trusted Advisor provides recommendations, not enforcement. It primarily offers insights into cost optimization and security best practices. It cannot enforce instance-type policies or prevent the use of non-approved services. Simply enabling Trusted Advisor checks will not restrict developers from launching non-compliant resources.

References:
https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
https://docs.aws.amazon.com/controltower/latest/userguide/how-controls-work.html
https://aws.amazon.com/blogs/aws/new-for-aws-control-tower-comprehensive-controls-management-preview/

Check out this AWS Control Tower Cheat Sheet:
https://tutorialsdojo.com/aws-control-tower/

---

## Câu 4 — ✅ ĐÚNG

### Câu hỏi

A genome research facility uses AWS Step Functions to orchestrate a nightly machine learning pipeline that retrains predictive models to discover potential cancer cures. The pipeline consists of multiple AWS Lambda tasks responsible for parsing genomic data, running simulations, and optimizing hyperparameters. Each step is time-sensitive and mission-critical.
Recently, the research team discovered that if even a single state within the Step Functions workflow encounters an error, whether during data processing, model training, or evaluation, the entire retraining sequence fails silently, and no alerts are sent. As a result, several nights of crucial model updates were missed without the team’s knowledge.
The solutions architect must implement a failure detection and notification system to avoid these unseen interruptions. This solution should immediately alert the team by email anytime a Task, Map, or Parallel state fails. The alert must include the original input arguments that triggered the failure, enabling rapid diagnosis and response.
Which action should the architect take to design this system?

### Các phương án

- **A.** Set up an Amazon SNS topic and configure an Email-type subscription that delivers messages to the group’s distribution address. Define a Task state called “Email” that sends the state’s input parameters to the SNS topic. For every Task, Map, and Parallel state, add a Catch clause that matches  "ErrorEquals": ["States.ALL"], and routes the flow to the “Email” state via the “Next” field. 👈 *(bạn chọn)* ✅
- **B.** Enable AWS X-Ray on all Lambda functions in the workflow to trace failed invocations. Implement a Catch clause in all Task, Map, and Parallel states, setting "ErrorEquals": ["States.ALL"] to handle any failure type. Route execution to the “Email” state through the “Next” property whenever an error is intercepted.
- **C.** Provision an Amazon SNS topic and attach an Email-based subscription that routes notifications to the team’s group inbox. Introduce a Task state labeled “Email” that passes along the received input to the SNS topic. For each Task, Map, and Parallel state, include a Catch block configured with  "ErrorEquals": ["States.Runtime"] and direct control to the “Email” state using the “Next” parameter.
- **D.** Use Amazon EventBridge to monitor the execution history of the Step Functions. Add a Catch handler to every Task, Map, and Parallel state, specifying "ErrorEquals": ["States.Runtime"] to capture runtime-related issues. Use the “Next” field to transition the flow to the “Email” state upon encountering such errors.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

With AWS Step Functions, you can create workflows called State machines to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning pipelines.
Step Functions is based on state machines and tasks. In Step Functions, state machines are a series of event-driven steps. Each step in a workflow is called a state. For example, a Task state represents a unit of work that another AWS service performs, such as calling an AWS Lambda function or API. Instances of running workflows performing tasks are called executions in Step Functions.

By using "ErrorEquals": ["States.ALL"] in Step Functions, the solution ensures that all possible errors are caught, whether runtime, timeout, permissions, or others. It also incorporates Amazon SNS with an email subscription to notify the team instantly, and the “Email” Task is designed to pass along the input arguments, allowing the researchers to diagnose what caused the failure quickly. This approach is thorough and aligns directly with AWS best practices for robust error handling and alerting in mission-critical workflows.
Hence, the correct answer is: Set up an Amazon SNS topic and configure an Email-type subscription that delivers messages to the group’s distribution address. Define a Task state called “Email” that sends the state’s input parameters to the SNS topic. For every Task, Map, and Parallel state, add a Catch clause that matches  "ErrorEquals": ["States.ALL"], and routes the flow to the “Email” state via the “Next” field.
The option that says: Provision an Amazon SNS topic and attach an Email-based subscription that routes notifications to the team’s group inbox. Introduce a Task state labeled “Email” that passes along the received input to the SNS topic. For each Task, Map, and Parallel state, include a Catch block configured with  "ErrorEquals": ["States.Runtime"] and direct control to the “Email” state using the “Next” parameter is incorrect. This solution uses "ErrorEquals": ["States.Runtime"], which only captures a subset of errors, primarily those related to runtime execution, like timeouts or failures in the Lambda function itself. It does not catch other common failure types, such as permission errors or input validation issues. Using "States.ALL" is essential to ensure the system responds to any failure, not just a specific category.
The option that says: Use Amazon EventBridge to monitor the execution history of the Step Functions. Add a Catch handler to every Task, Map, and Parallel state, specifying "ErrorEquals": ["States.Runtime"] to capture runtime-related issues. Use the “Next” field to transition the flow to the “Email” state upon encountering such errors is incorrect. This option includes Amazon EventBridge, which is not needed in this context. Step Functions already has built-in support for error handling using Catch blocks, and the requirement is to alert on each state failure, not just monitor overall workflow executions. EventBridge primarily helps with state change events, but it simply does not offer granular control or direct access to the input arguments at the state level as Step Functions does natively.
The option that says: Enable AWS X-Ray on all Lambda functions in the workflow to trace failed invocations. Implement a Catch clause in all Task, Map, and Parallel states, setting "ErrorEquals": ["States.ALL"] to handle any failure type. Route execution to the “Email” state through the “Next” property whenever an error is intercepted is incorrect. AWS X-Ray is primarily a tracing tool that helps visualize service call paths and diagnose performance issues. While useful for debugging, it does not provide built-in mechanisms for capturing workflow errors or sending alerts. X-Ray does not integrate with Step Functions Catch logic, so it cannot be used to route control flow or trigger email notifications. Simply enabling tracing does not fulfill the requirement for real-time failure alerts.

References:
https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html
https://docs.aws.amazon.com/step-functions/latest/dg/connect-sns.html

Check out this AWS Step Functions Cheat Sheet:
https://tutorialsdojo.com/aws-step-functions/

---

## Câu 5 — ✅ ĐÚNG

### Câu hỏi

A bank has received a security directive to harden its cloud infrastructure in response to a wave of cyberattacks targeting financial institutions. As part of this initiative, the bank is integrating third-party firewall appliances sourced from the AWS Marketplace to perform deep inspection and control of outbound internet traffic originating from all internal workloads.
The strategy involves centralizing these firewall appliances inside a shared services VPC, serving as a security chokepoint across the organization’s cloud infrastructure. The bank’s network team has already implemented VPC routing that funnels traffic from spoke VPCs into the shared services VPC.
The cloud security engineer must design a secure and highly available inspection architecture within a single AWS Region to satisfy security requirements and uptime guarantees.
Which of the following should the cloud engineer implement to meet these goals?

### Các phương án

- **A.** Provision firewall appliances across two different Availability Zones in the shared services VPC. Set up a Network Load Balancer linked to a target group that includes the appliances. Deploy a VPC interface endpoint and configure the route table to direct incoming VPC traffic to this endpoint as the next hop.
- **B.** Launch both firewall appliances in a single Availability Zone within the shared services VPC. Configure an Application Load Balancer and link it to a target group containing the appliances. Deploy a VPC interface endpoint and update the route table to forward traffic from connected VPCs to the endpoint as the next hop.
- **C.** Launch both firewall appliances in one Availability Zone within the shared services VPC. Configure a Gateway Load Balancer and associate it with a target group containing the appliances. Provision a Gateway Load Balancer endpoint and update the shared services VPC route table to use it as the next hop for incoming traffic from connected VPCs.
- **D.** Place two firewall appliances in different Availability Zones in the shared services VPC. Set up a Gateway Load Balancer and link it to a target group containing both appliances. Then, deploy a Gateway Load Balancer endpoint and configure the shared services VPC route table to forward inter-VPC traffic to this endpoint as the next hop. 👈 *(bạn chọn)* ✅

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

Gateway Load Balancers (GWLB) enable you to deploy, scale, and manage virtual appliances like firewalls, intrusion detection and prevention systems, and deep packet inspection systems. It combines a transparent network gateway (a single entry and exit point for all traffic) and distributes traffic while scaling your virtual appliances with the demand.
A Gateway Load Balancer operates at the third layer of the Open Systems Interconnection (OSI) model, the network layer. It listens for all IP packets across all ports and forwards traffic to the target group specified in the listener rule.
You can create a Gateway Load Balancer endpoint to connect to endpoint services powered by AWS PrivateLink. For each subnet that you specify from your VPC, we create an endpoint network interface in the subnet and assign it a private IP address from the subnet address range. An endpoint network interface is a requester-managed network interface. You can view it in your AWS account but can’t manage it yourself. You are billed for hourly usage and data processing charges.

Using a Gateway Load Balancer with firewall appliances in multiple Availability Zones ensures fault tolerance and minimal failover time. The GWLB endpoint acts as an entry point for traffic from spoke VPCs, and the route table configuration ensures that all traffic from those VPCs is inspected before reaching the internet. It is also primarily designed to handle traffic to and from virtual appliances transparently, which aligns perfectly with the stated requirements. This setup fits the goal of creating a centralized inspection point that works across zones without introducing complexity or violating AWS high availability best practices.
Hence, the correct answer is: Place two firewall appliances in different Availability Zones in the shared services VPC. Set up a Gateway Load Balancer and link it to a target group containing both appliances. Then, deploy a Gateway Load Balancer endpoint and configure the shared services VPC route table to forward inter-VPC traffic to this endpoint as the next hop.
The option that says: Launch both firewall appliances in one Availability Zone within the shared services VPC. Configure a Gateway Load Balancer and associate it with a target group containing the appliances. Provision a Gateway Load Balancer endpoint and update the shared services VPC route table to use it as the next hop for incoming traffic from connected VPCs is incorrect. This option proposes correctly using the Gateway Load Balancer and the GWLB endpoint. Still, it fails the high availability requirement because it places both firewall appliances in the same Availability Zone. This setup introduces a single point of failure, which the scenario explicitly aims to avoid. Even though the components are set up correctly, the lack of cross-AZ deployment makes it non-compliant with uptime and regulatory demands. Just distributing appliances across zones would have made it a stronger candidate.
The option that says: Provision firewall appliances across two different Availability Zones in the shared services VPC. Set up a Network Load Balancer linked to a target group that includes the appliances. Deploy a VPC interface endpoint and configure the route table to direct incoming VPC traffic to this endpoint as the next hop is incorrect. This solution attempts to distribute appliances across two Availability Zones, which is good for availability. However, it uses a Network Load Balancer and a VPC interface endpoint, neither suitable for deploying or scaling third-party firewall appliances. NLBs are primarily meant for layer 4 traffic distribution and do not support the service chaining or transparent bump-in-the-wire behavior required for deep packet inspection. This architecture simply does not meet the inspection and scalability demands for inline traffic security appliances.
The option that says: Launch both firewall appliances in a single Availability Zone within the shared services VPC. Configure an Application Load Balancer and link it to a target group containing the appliances. Deploy a VPC interface endpoint and update the route table to forward traffic from connected VPCs to the endpoint as the next hop is incorrect. It proposes an Application Load Balancer, which operates at layer 7 and is designed primarily for HTTP/HTTPS traffic. It is entirely unsuitable for routing arbitrary traffic to firewall appliances for inspection. Additionally, the deployment keeps both firewall appliances in the same Availability Zone, so it just repeats the same availability issue found in the prior option. This setup would only handle web traffic and lacks the flexibility and reliability needed for centralized traffic inspection across VPCs.

References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html
https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-load-balancer-endpoints.html

Check out this AWS Elastic Load Balancing Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

---

## Câu 6 — ❌ SAI

### Câu hỏi

A financial institution is running multiple AWS Lambda functions. These functions are packaged as .zip archives and rely on a shared Lambda layer that contains common libraries.
Security compliance requires that the development team must:


Continuously monitor the Lambda functions and the shared Lambda layer for current common vulnerabilities and exposures (CVEs).


Perform additional automated code scans on a subset of Lambda functions to detect data leaks and injection flaws.


Ensure that not all Lambda functions are scanned for code issues, since some workloads handle non-sensitive test data.


The company wants a fully managed AWS-native solution to meet these requirements.


Which of the following will meet the given requirements? (Select THREE.)

### Các phương án

- **A.** Apply an Amazon Inspector exclusion tag with a key of InspectorCodeExclusion and a value of LambdaCodeScanning to Lambda functions that should not be code-scanned. 👈 *(bạn chọn)* ✅
- **B.** Enable Amazon Inspector Lambda code scanning to detect code-level vulnerabilities. 👈 *(bạn chọn)* ✅
- **C.** Use AWS IAM policies to restrict Amazon Inspector from scanning specific Lambda functions. 👈 *(bạn chọn)*
- **D.** Use Amazon GuardDuty Lambda Protection to monitor for CVEs and data leaks.
- **E.** Enable AWS Config with a custom rule to check Lambda deployment packages for CVEs.
- **F.** Enable Amazon Inspector and activate Lambda standard scanning for CVE detection. ✅

> **Bạn chọn:** A, B, C  
> **Đáp án đúng:** A, B, F  
> **Kết quả:** ❌ Sai

### Giải thích

Amazon Inspector is a vulnerability management service that automatically identifies workloads and continuously scans them for software vulnerabilities and unintended network exposure. It can discover and scan Amazon EC2 instances, container images in Amazon ECR, and Lambda functions. When Amazon Inspector detects a software vulnerability or unintended network exposure, it generates a finding—a detailed report that outlines the issue. You can manage these findings through the Amazon Inspector console or API.
Amazon Inspector supports security vulnerability assessments for AWS Lambda functions and layers, providing continuous automated scanning. It offers two types of scanning for Lambda functions:
– Amazon Inspector Lambda standard scanning – This scan type is the default Lambda scan type. It scans application dependencies in Lambda functions and layers for package vulnerabilities.
– Amazon Inspector Lambda code scanning – This scan type scans custom application code in your Lambda functions and layers for code vulnerabilities. You can activate Lambda standard scanning or Lambda standard scanning with Lambda code scanning.
If you want to activate Lambda code scanning, you must first enable standard scanning.

You can add tags to Lambda functions to exclude them from Amazon Inspector’s Lambda code scans. Excluding functions from scans can help prevent receiving unactionable alerts. To tag a function for exclusion, use the following key-value pair for the tag.
– Key – InspectorCodeExclusion
– Value – LambdaCodeScanning
Hence, the correct answers are:
– Enable Amazon Inspector and activate Lambda standard scanning for CVE detection. It enables continuous, automated scanning of Lambda function deployment packages and layers for known vulnerabilities (CVEs).
– Enable Amazon Inspector Lambda code scanning to detect code-level vulnerabilities. It allows Amazon Inspector to perform static code analysis on Lambda functions to detect issues like injection flaws and data leaks. This meets the requirement for automated code scans on a subset of functions handling sensitive data.
– Apply an Amazon Inspector exclusion tag with a key of InspectorCodeExclusion and a value of LambdaCodeScanning to Lambda functions that should not be code-scanned. It provides a native way to exclude specific Lambda functions from code scanning. This ensures that functions handling non-sensitive test data are not unnecessarily scanned, aligning with the compliance requirement.
The option that says: Enable AWS Config with a custom rule to check Lambda deployment packages for CVEs is incorrect because AWS Config does not primarily support vulnerability scanning. While it can track configuration changes and compliance, it cannot inspect Lambda packages for CVEs without external tooling or custom logic.
The option that says: Use Amazon GuardDuty Lambda Protection to monitor for CVEs and data leaks is incorrect because GuardDuty focuses on detecting runtime threats and anomalous behavior, not static vulnerabilities like CVEs or code-level flaws. It does not scan deployment packages or source code for vulnerabilities.
The option that says: Use AWS IAM policies to restrict Amazon Inspector from scanning specific Lambda functions is incorrect because Amazon Inspector does not use IAM policies to control scanning scope at the function level. Instead, it typically relies on tagging mechanisms for exclusions.

References:
https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html
https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html
https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_code_exclude_functions.html

Check out this Amazon Inspector Cheat Sheet:
https://tutorialsdojo.com/amazon-inspector/

---

## Câu 7 — ✅ ĐÚNG

### Câu hỏi

A cloud engineer at a fintech startup is preparing the infrastructure for a critical internal platform launch. The cloud engineer configures DNS resolution for a newly provisioned VPC in the ap-southeast-1 (Singapore) Region as part of the setup. This VPC uses the 13.232.18.0/24 CIDR block and has been integrated with Amazon Route 53 Resolver to manage DNS queries.
Initially, the team planned for basic DNS resolution, but the requirements have since changed to support more advanced functionality. Now, all domain name lookups must be routed through a Private hosted zone, and any Amazon EC2 instances with assigned Public IP addresses must automatically receive corresponding Public hostnames.
Which of the following should the cloud engineer do to satisfy the new requirements and ensure the domain names are resolved correctly and consistently within the VPC? (Select TWO.)

### Các phương án

- **A.** Set up a private DNS zone and link it to the VPC. Confirm that the VPC has both enableDnsSupport and enableDnsHostnames enabled. 👈 *(bạn chọn)* ✅
- **B.** Define a custom DHCP options set that specifies domain-name-servers=AmazonProvidedDNS, and attach this configuration to the VPC. 👈 *(bạn chọn)* ✅
- **C.** Create a new DHCP options set that sets domain-name-servers=13.232.18.98, and apply this configuration to the VPC by associating it accordingly.
- **D.** Create a private hosted zone and associate it with the VPC. Ensure the VPC is configured with the appropriate instanceTenancy setting.
- **E.** Establish a private hosted zone and connect it to the designated VPC. Make sure that the enableNetworkAddressUsageMetrics feature is activated.

> **Bạn chọn:** A, B  
> **Đáp án đúng:** A, B  
> **Kết quả:** ✅ Đúng

### Giải thích

One of the foundational networking components in the Virtual Private Cloud (VPC) is the Amazon DNS server, also known as the Route 53 Resolver. This DNS resolver service is natively integrated into each Availability Zone within the AWS Region, providing a reliable and scalable solution for domain name resolution within the VPC.
The VPC attributes enableDnsHostnames and enableDnsSupport determine the DNS support provided for your VPC. If both attributes are enabled, an instance launched into the VPC receives a public DNS hostname if assigned a public IPv4 address or an Elastic IP address at creation. If you enable both attributes for a VPC that didn’t previously have them enabled, instances already launched into that VPC receive public DNS hostnames if they have a public IPv4 address or an Elastic IP address.
On the other hand, a DHCP option set is a group of network settings used by resources in your VPC, such as EC2 instances, to communicate over your virtual network. If we create a DHCP option set that contains the setting domain-name-servers=AmazonProvidedDNS, we use the built-in Amazon DNS server. The Amazon DNS server in your VPC resolves the DNS domain names you specify in a private hosted zone in Route 53.

To summarize, enabling enableDnsSupport allows instances in the VPC to use a DNS resolver. Enabling enableDnsHostnames ensures that instances assigned public IP addresses receive corresponding public DNS hostnames. Defining a custom DHCP options set that specifies domain-name-servers=AmazonProvidedDNS ensures compatibility with Amazon Route 53 Resolver, including support for private hosted zones and automatic assignment of public hostnames to EC2 instances with public IPs.
Hence, the correct answers are:
– Set up a private DNS zone and link it to the VPC. Confirm that the VPC has both enableDnsSupport and enableDnsHostnames enabled
– Define a custom DHCP options set that specifies domain-name-servers=AmazonProvidedDNS, and attach this configuration to the VPC
The option that says: Create a private hosted zone and associate it with the VPC. Ensure the VPC is configured with the appropriate instanceTenancy setting is incorrect. The instanceTenancy option typically refers to whether instances in the VPC are launched on shared or dedicated hardware. This setting has no impact on DNS resolution or hostname assignment. It is unrelated to the functional requirements described in the scenario.
The option that says: Establish a private hosted zone and connect it to the designated VPC. Make sure that the enableNetworkAddressUsageMetrics feature is activated  is incorrect. The enableNetworkAddressUsageMetrics simply allows monitoring IP address usage through CloudWatch. While it may help track network resource consumption, it does not affect DNS functionality or contribute to resolving domain names or assigning hostnames.
The option that says: Create a new DHCP options set that sets domain-name-servers=13.232.18.98, and apply this configuration to the VPC by associating it accordingly is incorrect. Setting the domain-name-servers to a specific IP address, such as 13.232.18.98, overrides the default Amazon-provided DNS configuration. This setting could interfere with Route 53 Resolver features, such as support for private hosted zones and public DNS hostname assignment, which depend on the use of AmazonProvidedDNS. Therefore, this option does not meet the full requirements and could lead to inconsistent or incorrect DNS resolution within the VPC.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html
https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSetConcepts.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

---

## Câu 8 — ✅ ĐÚNG

### Câu hỏi

An edtech company is preparing to launch a new virtual learning environment (VLE) hosted on Amazon EC2 instances. To support students and educators around the globe, the platform must be deployed across three AWS Regions: us-east-1, eu-west-1, and ap-southeast-1. Key components of the system, such as student progress tracking, resource availability, and real-time collaboration events, must remain consistent and synchronized across all Regions.
To support real-time interactivity, the VLE uses more than just standard HTTP and HTTPS ports. WebSocket connections run on port 5000 for live quizzes, and the interactive whiteboard feature communicates over port 8080. To ensure optimal user experience, the platform must direct learners to the AWS Region with the lowest latency. Additionally, the architecture must be designed so that any single Region can dynamically scale to accommodate traffic from all others, should the need arise.
A solutions architect must define an infrastructure strategy that delivers global availability, seamless scalability, and low-latency access, all while keeping operational overhead to a minimum.
What solution best satisfies these needs while reducing operational management effort?

### Các phương án

- **A.** Deploy EC2 instances within Auto Scaling groups across all AWS Regions, linking each group to its corresponding Application Load Balancer (ALB). Configure Amazon Route 53 to use latency-based routing policies, directing users to the Region with the fastest response time via the associated ALB. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions.
- **B.** Deploy EC2 Auto Scaling groups across all AWS Regions and link each group to its own Network Load Balancer (NLB). Enable EC2 Global View to centrally monitor and manage instance health, capacity, and scaling activity across Regions. Use Amazon Route 53 with latency-based routing to ensure users are directed to the Region delivering the lowest latency. Store platform metadata in Amazon RDS for PostgreSQL, deploying one instance per Region, and configure cross-Region read replicas to maintain synchronized data consistency on a global scale.
- **C.** Provision of an EC2 Auto Scaling group in every AWS Region to manage computing resources dynamically. Associate each group with its respective Network Load Balancer (NLB). Configure Amazon Route 53 with latency-based routing policies that direct traffic to the NLB offering the fastest response times per Region. Store platform metadata within an Amazon DynamoDB global table to maintain data consistency across all Regions. 👈 *(bạn chọn)* ✅
- **D.** Launch an EC2 Spot Fleet in every AWS Region and link each to its respective Network Load Balancer (NLB). Provision an AWS Global Accelerator IP address that targets the NLB to enable consistent global access. Configure Amazon Route 53 to apply latency-based routing, directing traffic to the Region with the fastest response time using the AWS Global Accelerator IP address. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

An Auto Scaling group is a logical set of EC2 instances managed by Amazon EC2 Auto Scaling, which automatically maintains instance count and handles health checks and scaling based on demand.
Application Load Balancers (ALBs) operate at the application layer, ideal for web apps and microservices with features like SSL termination and session stickiness. Network Load Balancers (NLBs) work at the transport layer, offering low latency and high throughput for performance-intensive workloads like gaming and IoT.
Amazon Route 53 with latency-based routing directs users to the Region with the lowest latency.
Amazon DynamoDB global tables provide multi-Region replication with strong or eventual consistency. Strong consistency ensures that applications can always read the latest data from any Region, enabling high availability and zero RPO.

EC2 Auto Scaling groups manage compute capacity across Regions, with each group linked to a Network Load Balancer, ideal for TCP traffic on non-standard ports like 5000 and 8080 used by the VLE. Amazon Route 53 with latency-based routing directs users to the Region with the lowest latency. DynamoDB global tables offer multi-Region, multi-active replication, enabling all Regions to read and write simultaneously. This setup ensures real-time consistency without complex replication logic or added operational overhead.
Hence, the correct answer is: Provision of an EC2 Auto Scaling group in every AWS Region to manage computing resources dynamically. Associate each group with its respective Network Load Balancer (NLB). Configure Amazon Route 53 with latency-based routing policies that direct traffic to the NLB offering the fastest response times per Region. Store platform metadata within an Amazon DynamoDB global table to maintain data consistency across all Regions.
The option that says: Deploy EC2 instances within Auto Scaling groups across all AWS Regions, linking each group to its corresponding Application Load Balancer (ALB). Configure Amazon Route 53 to use latency-based routing policies, directing users to the Region with the fastest response time via the associated ALB. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions is incorrect. This solution uses Application Load Balancers, which support only HTTP and HTTPS. Since the VLE uses WebSockets on port 5000 and custom traffic on port 8080, ALBs are incompatible without additional configuration. Despite the rest of the architecture aligning with requirements, using ALBs makes the solution technically unsuitable. One cannot simply replace an NLB with an ALB when the traffic types do not align.
The option that says: Launch an EC2 Spot Fleet in every AWS Region and link each to its respective Network Load Balancer (NLB). Provision an AWS Global Accelerator IP address that targets the NLB to enable consistent global access. Configure Amazon Route 53 to apply latency-based routing, directing traffic to the Region with the fastest response time using the AWS Global Accelerator IP address. Persist game-related metadata in a globally distributed Amazon DynamoDB table to ensure consistent data availability across Regions is incorrect. This option adds unnecessary complexity by introducing EC2 Spot Fleets and AWS Global Accelerator. While Spot Fleets reduce cost, they can be interrupted without notice, making them unreliable for a real-time education platform. Global Accelerator provides advanced routing, but is redundant when Amazon Route 53’s latency-based routing already meets latency needs. These features add operational overhead without meaningful benefits for the platform’s reliability and availability.
The option that says:  Deploy EC2 Auto Scaling groups across all AWS Regions and link each group to its own Network Load Balancer (NLB). Enable EC2 Global View to centrally monitor and manage instance health, capacity, and scaling activity across Regions. Use Amazon Route 53 with latency-based routing to ensure users are directed to the Region delivering the lowest latency. Store platform metadata in Amazon RDS for PostgreSQL, deploying one instance per Region, and configure cross-Region read replicas to maintain synchronized data consistency on a global scale is incorrect. This option uses EC2 Global View and Amazon RDS for PostgreSQL with cross-Region replication. While EC2 Global View offers centralized monitoring across Regions, it does not handle traffic distribution or scaling. The main limitation is that RDS for PostgreSQL only supports cross-Region read replicas and does not offer multi-Region write capability out of the box. Supporting global writes would require extra tooling and coordination, increasing operational overhead.

References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html
https://aws.amazon.com/what-is/load-balancing/
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html
https://aws.amazon.com/dynamodb/global-tables/

Check out this AWS Elastic Load Balancing Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

---

## Câu 9 — ✅ ĐÚNG

### Câu hỏi

A fast-rising technology company is preparing to migrate a portfolio of applications to AWS. The current on-premises environment includes a mix of physical and virtual machines. The founding CTO, who originally designed the infrastructure, has left the company and provided limited documentation about the architecture.
The company lacks complete visibility into its application estate and infrastructure layout.
One critical application scheduled for migration has several unmapped dependencies. Many of these dependencies use low-latency communication over a custom IP-based protocol bound to port 1000. To preserve operational integrity, the company must migrate the application and all tightly coupled systems in the same migration wave.
The company has used AWS Transform discovery and assessment capabilities to collect telemetry from its servers for several months. The new CTO must now identify the complete set of connected systems that should be grouped and migrated together.
What approach should the new CTO take to discover and group the correct dependencies for simultaneous migration?

### Các phương án

- **A.** Export the collected discovery data to Amazon S3. Use AWS Glue to crawl the exported dataset and create a data catalog. Then run Amazon Athena queries to search for references to port 1000 or IP-based traffic. Create a migration wave based only on the query results and proceed with the migration.
- **B.** Use AWS Transform MGN to replicate the application servers and migrate them immediately. After cutover, rely on Amazon CloudWatch metrics to identify dependency-related issues. Then scan for any missing dependencies and migrate those systems later as needed.
- **C.** Use AWS Transform discovery and assessment capabilities to analyze the application servers and their communication patterns. Review the dependency mapping and network flow data, and use Amazon Athena data exploration to identify systems communicating through the custom protocol on port 1000. Group the application and all tightly coupled dependent servers into the same migration wave for coordinated migration. 👈 *(bạn chọn)* ✅
- **D.** Use Amazon VPC Network Access Analyzer to define a network access scope that matches traffic on port 1000. Analyze the resulting network paths to determine which systems communicate with the application. Then create a migration wave in AWS Transform based on the Network Access Analyzer results.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Transform helps organizations plan and accelerate migration and modernization work by analyzing existing infrastructure, applications, and code. For migration planning, it can help assess workloads, review discovered server groupings, and organize applications into migration waves. A migration wave is made up of one or more move groups, and a move group represents co-dependent applications or systems that should be moved together because of technical or business dependencies. This is important for complex environments where applications depend on shared databases, internal services, or low-latency communication paths.
In this scenario, the company must not simply migrate the main application server by itself. The critical requirement is to identify all tightly coupled systems that communicate with the application over the custom IP-based protocol on port 1000. AWS Transform discovery and assessment capabilities help the new CTO understand application relationships and communication patterns before the migration begins. This allows the team to build a more accurate move group and migration wave instead of relying only on incomplete documentation or post-migration troubleshooting. AWS documentation also describes dependency relationships as connections between systems, which can include technical dependencies that require systems to be moved together.

Amazon Athena data exploration further strengthens the analysis because it allows collected discovery data from on-premises servers to be queried in one place. When data exploration is enabled, discovered data can be stored in Amazon S3 and queried with Athena, including utilization details and network connection data. This helps the team validate which servers are communicating with the application and which dependencies are related to port 1000 traffic. In this case, the best approach is to use AWS Transform for dependency mapping and migration wave planning, then use Athena data exploration to inspect the underlying connection data when a more specific protocol or port-based analysis is needed.
AWS Transform MGN is related to the migration phase, but it primarily focuses on rehosting servers to AWS. It replicates physical, virtual, or cloud-based source servers and helps launch them in AWS with minimal changes. That capability is useful after the migration plan is ready, but it does not replace the need to identify dependencies before cutover. In this question, the issue is not only how to move the servers. The main issue is how to determine which systems must be moved together to preserve low-latency communication and avoid breaking the application during migration.
Hence, the correct answer is: Use AWS Transform discovery and assessment capabilities to analyze the application servers and their communication patterns. Review the dependency mapping and network flow data, and use Amazon Athena data exploration to identify systems communicating through the custom protocol on port 1000. Group the application and all tightly coupled dependent servers into the same migration wave for coordinated migration.
The option that says: Export the collected discovery data to Amazon S3. Use AWS Glue to crawl the exported dataset and create a data catalog. Then run Amazon Athena queries to search for references to port 1000 or IP-based traffic. Create a migration wave based only on the query results and proceed with the migration is incorrect because it only focuses on manual data querying. Amazon Athena can help inspect collected discovery data, but this option skips the broader migration-planning capabilities of AWS Transform, such as dependency review, move group creation, and migration wave organization. A query that simply looks for port 1000 traffic could miss business dependencies, application relationships, shared services, or indirect communication patterns that should also influence the move group.
The option that says: Use Amazon VPC Network Access Analyzer to define a network access scope that matches traffic on port 1000. Analyze the resulting network paths to determine which systems communicate with the application. Then create a migration wave in AWS Transform based on the Network Access Analyzer results is incorrect. Amazon VPC Network Access Analyzer is typically used to analyze network access paths within AWS networking resources. It is not designed to discover dependency relationships across an on-premises estate of physical and virtual machines. In this scenario, the required traffic analysis must come from discovered server telemetry and connection data, not just from AWS VPC path analysis.
The option that says: Use AWS Transform MGN to replicate the application servers and migrate them immediately. After cutover, rely on Amazon CloudWatch metrics to identify dependency-related issues. Then scan for any missing dependencies and migrate those systems later as needed  is incorrect because it simply moves the workload first and discovers problems afterward. This is risky for a critical application with unmapped low-latency dependencies. CloudWatch is useful for monitoring resources after migration, but it is not a substitute for pre-migration dependency analysis. Migrating the primary application before identifying its tightly coupled systems could cause connection failures, degraded performance, or an incomplete cutover.

References:
https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-review-groupings-and-waves.html
https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html
https://docs.aws.amazon.com/application-discovery/latest/userguide/explore-data.html

Check out this Migration Evaluator Cheat Sheet:
https://tutorialsdojo.com/migration-evaluator-cheat-sheet/

---

## Câu 10 — ✅ ĐÚNG

### Câu hỏi

A North American-based tech startup plans to expand to Europe due to the unexpected, overwhelming success of its software-as-a-service (SaaS) solution, which uses AWS AppFabric for SaaS integration and security observability. A solutions architect consultant was hired to design and execute the expansion.
The company uses the us-east-1 Region for its North American infrastructure. The system uses Amazon S3, which is accessed through Amazon CloudFront, as its front-end component. It uses Amazon API Gateway for the API endpoints. AWS Lambda functions connected to an Amazon RDS for MySQL serve as its backend and persistence layer. Amazon Route 53 manages the domain via a simple routing policy pointing to the API Gateway.
In anticipation of the upcoming expansion, the engineering team proactively provisioned eu-west-1 Region infrastructure, including API Gateways and Lambda functions in the mentioned Region.
Initial measurements of the consultant suggest that around 95% of the database traffic is read-only.
What approach can the consultant take to expand on the existing eu-west-1 Region and ensure minimal latency for users in the Europe Region?

### Các phương án

- **A.** In Route 53, use latency-based routing. Set up a cross-Region read replica of the database in eu-west-1. 👈 *(bạn chọn)* ✅
- **B.** Use latency-based routing in Route 53 to direct traffic to the appropriate API  endpoint. Configure an AWS Database Migration Service (AWS DMS) task with change data capture (CDC) for replication of the main database from the us-east-1 to eu-west-1 .
- **C.** Use failover routing in Route 53. Create a Multi-AZ replica of the primary database.
- **D.** Keep simple routing in Route 53 for minimal setup. Set up an AWS Database Migration Service (AWS DMS) task with full load combined with change data capture (CDC) to replicate the original database from us-east-1 to eu-west-1.

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

To minimize latency for European users accessing a report-generation platform, the key objective is to bring data and computing closer to users in the European Region. The scenario highlights that over 95% of the database workload is read-only, indicating that read scalability through replication is a viable and preferred solution. Also, the infrastructure in eu-west-1 (API Gateway + Lambda) has already been deployed, so we only need to ensure data consistency and fast access in that region.
We can reduce latency by the following approach:
1. Cross-Region read replica ensures that read-only queries (which comprise 90% of the load) are offloaded from the primary us-east-1 database and served locally in eu-west-1, reducing cross-Region latency and data transfer.
2. Latency-based routing in Amazon Route 53 ensures that European users are routed to the fastest (often the nearest) API Gateway + Lambda stack in eu-west-1.

Since RDS cross-Region read replicas are designed for scaling reads globally, and Route 53 can route to the correct endpoint, this setup provides an efficient and scalable architecture.
Hence, the correct answer is: In Route 53, use latency-based routing. Set up a cross-Region read replica of the database in eu-west-1.
The option that says: Use latency-based routing in Route53 to direct traffic to the appropriate API endpoint. Configure an AWS Database Migration Service (AWS DMS) task with change data capture (CDC) for replication of the main database from the us-east-1 to eu-west-1 is incorrect. AWS DMS with CDC can replicate data across Regions, but it is not designed for real-time, low-latency read access in high-throughput applications. DMS is only meant for data migration, warehousing, or hybrid environments, not for scalable, low-latency read operations in production. Additionally, DMS adds complexity and operational overhead, including managing replication tasks and monitoring lag.
The option that says: Use failover routing in Route 53. Create a Multi-AZ replica of the primary database is incorrect. Failover routing in Route 53 is designed to improve availability during outages by routing traffic to a healthy endpoint if the primary fails. It does not facilitate latency-based traffic distribution between Regions. Additionally, Multi-AZ deployments are confined to a single Region. You cannot create a Multi-AZ read replica across Regions; they are designed to provide high availability within the same Region only.
The option that says: Keep simple routing in Route 53 for minimal setup. Set up an AWS Database Migration Service (AWS DMS) task with full load combined with change data capture (CDC) to replicate the original database from us-east-1 to eu-west-1 is incorrect. First, simple routing does not differentiate traffic based on Region or latency. All users are directed to a single endpoint, defeating the goal of optimizing for European users. Second, AWS DMS is not the right tool for real-time production read replicas, as with the first option. It introduces lag and does not scale efficiently for large volumes of read traffic.

References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html

Check out this Amazon Aurora Cheat Sheet:
https://tutorialsdojo.com/amazon-aurora/

---

## Câu 11 — ❌ SAI

### Câu hỏi

An international e-commerce company relies on Amazon CloudFront to deliver its multi-regional Amazon ECS-based web store with fast, scalable performance. Over recent months, customers around the globe have started reporting sluggish page load times, particularly during flash sales and heavy promotional events.
The performance reliability team has spotted a troubling pattern: CloudFront’s cache hit ratio has consistently decreased. Amazon CloudWatch metrics reveal the root cause: query strings in some request URLs are inconsistent. Parameter order shifts unpredictably, and values alternate between mixed-case and lowercase.
Which steps should be implemented to rapidly restore CloudFront’s cache hit/ratio with the least operational overhead and cost?

### Các phương án

- **A.** Configure a CloudFront Function on the Viewer Request event that alphabetically sorts all query parameter keys and enforces lowercase for both parameter names and values ✅
- **B.** Attach a Lambda@Edge handler to the CloudFront distribution’s Viewer Request event that alphabetically sorts each query string parameter and converts all names and values to lowercase to ensure consistent cache key generation 👈 *(bạn chọn)*
- **C.** Place a reverse proxy layer downstream of the load balancer to intercept incoming URLs and rewrite all query string characters to lowercase
- **D.** Modify the CloudFront distribution’s cache or origin-request policy to stop including query-string parameters in the cache key

> **Bạn chọn:** B  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

With CloudFront Functions, you can write lightweight functions in JavaScript for high-scale, latency-sensitive CDN customizations. Your functions can manipulate the requests and responses that flow through CloudFront, perform basic authentication and authorization, generate HTTP responses at the edge, and more. The CloudFront Functions runtime environment offers submillisecond startup times, scales immediately to handle millions of requests per second, and is highly secure. CloudFront Functions is a native feature of CloudFront, which means you can build, test, and deploy your code entirely within CloudFront.
When you associate a CloudFront function with a CloudFront distribution, CloudFront intercepts requests and responses at CloudFront edge locations and passes them to your function. You can invoke CloudFront Functions when the following events occur:
When CloudFront receives a request from a viewer (viewer request)
Before CloudFront returns the response to the viewer (viewer response)

Using a CloudFront Function at the Viewer Request event to alphabetically sort and lowercase query parameters is the optimal solution for this specific problem. CloudFront Functions are lightweight, execute in sub-millisecond time, and cost-efficient (~$0.10 per million requests). This option delivers the fastest remediation with minimal complexity or overhead.
Hence, the correct answer is: Configure a CloudFront Function on the Viewer Request event that alphabetically sorts all query parameter keys and enforces lowercase for both parameter names and values.
The option that says: Attach a Lambda@Edge handler to the CloudFront distribution’s Viewer Request event that alphabetically sorts each query string parameter and converts all names and values to lowercase to ensure consistent cache key generation is incorrect. Using Lambda@Edge is actually a technically sound approach: CloudFront calculates the cache key at that viewer-level stage, so normalizing the query string there ensures identical URLs map to the same cache key, reducing cache fragmentation and improving the cache hit ratio. However, this option is suboptimal compared to CloudFront Function. Deploying a CloudFront Function at the Viewer Request event achieves the same normalization (sorting and lowercasing query strings) but is far more lightweight, faster, and cost-effective. A CloudFront Function runs in sub-millisecond time at every edge location, whereas Lambda@Edge incurs a 1 to 2-millisecond cold-start latency and costs around 6 times. For a task as simple as query-string normalization, relying on Lambda@Edge introduces unnecessary latency and overhead compared to the more efficient CloudFront Function alternative.
The option that says: Modify the CloudFront distribution’s cache or origin-request policy to stop including query-string parameters in the cache key is incorrect. Disabling query-string–based caching can lead to wrong content being served, not just performance issues. When CloudFront excludes query strings from the cache key, every request, regardless of its unique query data, receives the same cached response. If one user’s request carries specific parameters (e.g., ?user=alice), CloudFront might cache that particular version and then serve it to another user requesting the same path without those parameters. In effect, CloudFront treats what could be distinct content as identical.
The option that says: Place a reverse proxy layer downstream of the load balancer to intercept incoming URLs and rewrite all query string characters to lowercase is incorrect. Placing a reverse proxy layer downstream of the load balancer to normalize URLs won’t improve cache hit ratios because CloudFront computes its cache key before forwarding requests to any backend. As a result, any normalization done later in the request pipeline simply does not affect caching at all. Without normalization at the edge, cache fragmentation persists. This approach is ineffective.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

---

## Câu 12 — ✅ ĐÚNG

### Câu hỏi

An accounting company initiated a migration of its core workloads to the AWS Cloud to modernize its infrastructure, following a recent change in technical leadership. The company’s current setup includes Graviton‑based Amazon EC2 instances (ARM64 architecture) for compute resources, Amazon EFS for shared file storage, and Amazon RDS DB instances for managing relational databases.




To comply with regulatory mandates and uphold internal data governance standards, the new leadership has mandated the following backup procedures:


The solution must provide a centralized overview of backup status across the AWS environment.


Any backup failure must trigger immediate notifications to technical stakeholders.


Data backups must follow custom retention policies, with separate rules for daily, weekly, and monthly backups.


Backups must be automatically replicated to at least one additional AWS Region immediately after creation.


Which actions will meet these objectives while introducing the least operational overhead?

### Các phương án

- **A.** Define individual snapshot lifecycle policies in Amazon Data Lifecycle Manager (Amazon DLM) to align with each retention requirement. Activate cross-Region snapshot replication within DLM to ensure backups are automatically copied to another AWS Region. Develop an AWS Lambda function that monitors for backup or restore events and triggers a notification when a job finishes with either RESTORE_JOB_SUCCESSFUL or BACKUP_JOB_FAILED status.
- **B.** Define an AWS Backup plan that includes individual backup rules aligned with each required retention schedule. Develop an AWS Lambda function to handle cross-Region backup replication and to dispatch notifications whenever a backup job results in BACKUP_JOB_FAILED or  RESTORE_JOB_SUCCESSFUL.
- **C.** Establish an AWS Backup strategy incorporating individual backup rules corresponding to every retention specification. Set up a Backup strategy for cross-Region backup replication. Integrate an Amazon Simple Notification Service (Amazon SNS) topic into the backup strategy to dispatch alerts for completed operations, excluding those with the BACKUP_JOB_COMPLETED status. 👈 *(bạn chọn)* ✅
- **D.** Develop and deploy a consolidated Python script on a single EC2 instance. Schedule the script to connect to each RDS DB instance, run pg_dump/mysqldump. Call the create_image() API to generate AMIs for selected instances. Mount the EFS file system to the EC2 instance and use rsync to copy data. Replicate the backup files to another Region using Amazon S3. Send emails using Amazon SES if anything fails.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

AWS Backup is a fully managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on-premises. Using this service, you can configure backup policies and monitor activity for your AWS resources in one place. It allows you to automate and consolidate backup tasks previously performed service-by-service, and removes the need to create custom scripts and manual processes. You can automate your data protection policies and schedules with a few clicks in the AWS Backup console.
AWS Backup provides many features and capabilities, including lifecycle management policies, cross-Region backup, and backup activity monitoring.

AWS Backup is purpose-built to manage backup operations across EC2, EFS, and RDS with centralized visibility. It allows you to define individual backup rules for each retention period, supports native cross-Region replication, and integrates directly with Amazon SNS to send alerts for specific backup job statuses. The requirement also states the necessity to trigger immediate notifications on failure. Since AWS Backup includes multiple possible failure statuses and transitional statuses, the configuration simply sends notifications for all job completions except the successful BACKUP_JOB_COMPLETED status, ensuring nothing slips through the cracks. This approach meets all the stated requirements without introducing custom scripting or external monitoring, and it introduces the least operational overhead by using built-in managed features.
Hence, the correct answer is: Establish an AWS Backup strategy incorporating individual backup rules corresponding to every retention specification. Set up a Backup strategy for cross-Region backup replication. Integrate an Amazon Simple Notification Service (Amazon SNS) topic into the backup strategy to dispatch alerts for completed operations, excluding those with the BACKUP_JOB_COMPLETED status.
The option that says: Develop and deploy a consolidated Python script on a single EC2 instance. Schedule the script to connect to each RDS DB instance, run pg_dump/mysqldump. Call the create_image() API to generate AMIs for selected instances. Mount the EFS file system to the EC2 instance and use rsync to copy data. Replicate the backup files to another Region using Amazon S3. Send emails using Amazon SES if anything fails is incorrect. It relies on a custom EC2-based script to manage backups, which requires ongoing maintenance and complex logic to handle failures, retention, and replication. It just does not provide centralized visibility or native integration with AWS services for status tracking and alerting. This method adds operational complexity instead of reducing it and primarily duplicates features that AWS Backup already offers.
The option that says: Define individual snapshot lifecycle policies in Amazon Data Lifecycle Manager (Amazon DLM) to align with each retention requirement. Activate cross-Region snapshot replication within DLM to ensure backups are automatically copied to another AWS Region. Develop an AWS Lambda function that monitors for backup or restore events and triggers a notification when a job finishes with either RESTORE_JOB_SUCCESSFUL or BACKUP_JOB_FAILED status is incorrect. Amazon DLM is primarily designed for EBS volume snapshots and does not support RDS or EFS. While it can automate retention and replication for EC2 volumes, it simply does not offer centralized backup visibility across all services or native notification mechanisms. Relying on Lambda for alerts adds overhead and does not replace the native features that AWS Backup provides.
The option that says:  Define an AWS Backup plan that includes individual backup rules aligned with each required retention schedule. Develop an AWS Lambda function to handle cross-Region backup replication and to dispatch notifications whenever a backup job results in BACKUP_JOB_FAILED or RESTORE_JOB_SUCCESSFUL is incorrect. This solution offloads replication and notifications to custom Lambda functions, even though AWS Backup already supports built-in replication and alert integration through SNS. This approach just adds unnecessary components, making the architecture more complex and challenging to manage. It primarily ignores the full capabilities of AWS Backup and increases operational burden without any real benefit.

References:
https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html
https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html

Check out this AWS Backup Cheat Sheet:
https://tutorialsdojo.com/aws-backup/

---

## Câu 13 — ✅ ĐÚNG

### Câu hỏi

A global enterprise oversees at least six hundred AWS accounts via AWS Organizations. Recently, the governance team granted product owners the ability to configure Amazon S3 Access Points within the assigned accounts. These access points must be accessible only from within VPCs (Virtual Private Clouds), and any access from the Internet must be restricted.
What is the most operationally scalable and manageable approach to enforce this control efficiently across the organization?

### Các phương án

- **A.** At the root level of the organization, implement a Service Control Policy (SCP) that blocks s3:CreateAccessPoint except if the s3:AccessPointNetworkOrigin is equal to VPC 👈 *(bạn chọn)* ✅
- **B.** Modify the bucket’s resource policy to block any attempt to perform the s3:CreateAccessPoint operation, except when the s3:ResourceAccount condition is explicitly matched to VPC
- **C.** Use AWS Config rules combined with AWS Lambda to detect and revert S3 Access Points that are not restricted to VPC-only access
- **D.** Use an S3 Object ACL to block the creation of access points unless the request originates from a VPC by checking the s3:AccessPointNetworkOrigin condition

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for the IAM users and IAM roles in your organization. SCPs help ensure your accounts stay within your organization’s access control guidelines.
SCPs do not grant permissions to your organization’s IAM users and IAM roles. An SCP defines a permission guardrail or limits the actions your organization’s IAM users and IAM roles can perform.

By applying this SCP at the root level, the enterprise ensures that no user or role in any account, regardless of their IAM policies, can create an S3 Access Point unless it is explicitly configured to be VPC-only. This method is highly scalable and manageable because it requires a single policy update at the organizational root to enforce the rule across hundreds of accounts. It also aligns perfectly with the requirement to restrict access to S3 Access Points from the internet, thereby ensuring compliance and reducing the risk of misconfiguration by individual product teams.
Hence, the correct answer is: At the root level of the organization, implement a Service Control Policy (SCP) that blocks s3:CreateAccessPoint except if the s3:AccessPointNetworkOrigin is equal to VPC.
The option that says: Modify the bucket’s resource policy to block any attempt to perform the s3:CreateAccessPoint operation, except when the s3:ResourceAccount condition is explicitly matched to VPC is incorrect. First, S3 bucket policies only control access to bucket-level and object-level operations (such as s3:GetObject, s3:PutObject, or s3:ListBucket). They do not govern actions related to creating or managing S3 Access Points, such as s3:CreateAccessPoint. That action is handled at the account level, not the bucket level, so attempting to restrict it through a bucket policy is fundamentally ineffective. Second, using the s3:ResourceAccount condition key is also inappropriate. s3:ResourceAccount refers to the AWS account that owns the resource, not the network origin or access type. The correct condition key for enforcing network-based restrictions during access point creation is s3:AccessPointNetworkOrigin, not s3:ResourceAccount. Therefore, this option fails on both policy scope and condition logic levels, making it an invalid approach for enforcing VPC-only access point creation across an organization.
The option that says: Use AWS Config rules combined with AWS Lambda to detect and revert S3 Access Points that are not restricted to VPC-only access is incorrect. While this method is technically feasible and can enforce compliance after the fact, it is only reactive and not preventive. AWS Config rules monitor resource configurations and can trigger AWS Lambda functions for remediation, but they do not block the creation of non-compliant access points in real-time. This means an S3 Access Point that allows internet access could exist, even briefly, before being detected and corrected, which introduces operational and security risks. Additionally, deploying and maintaining AWS Config rules and remediating Lambda functions across hundreds of accounts requires significant effort. It involves ensuring that Config is enabled and configured correctly in each account, managing the lifecycle of custom remediation functions, handling errors or exceptions, and maintaining consistency. Compared to a centralized and proactive mechanism like a Service Control Policy (SCP), this method introduces more moving parts, complexity, and operational overhead. Therefore, while it may serve as a supplementary compliance check, it is not the most efficient or scalable approach to enforce VPC-only S3 Access Point creation across an enterprise-wide AWS Organizations structure.
The option that says: Use an S3 Object ACL to block the creation of access points unless the request originates from a VPC by checking the s3:AccessPointNetworkOrigin condition is incorrect. This approach reflects a misunderstanding of both S3 Object ACLs and the mechanics of S3 Access Point creation. S3 Object ACLs manage access control at the object level, allowing or denying access to specific users or AWS accounts for actions such as s3:GetObject or s3:PutObject. They cannot control IAM-level operations like s3:CreateAccessPoint, an account-level API call not associated with individual objects or even directly with the bucket. Furthermore, ACLs do not support conditional logic based on context keys like s3:AccessPointNetworkOrigin. That condition key applies only to IAM policies, SCPs, or resource-based policies on access points, not to ACLs. Therefore, this option is incorrect in its proposed enforcement mechanism and invalid in how it misuses a condition key in a context where it cannot be applied. It would not work at all to restrict access point creation, regardless of network origin, making it entirely ineffective for meeting the stated requirement.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html
https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html

Check out this AWS Organizations Cheat Sheet:
https://tutorialsdojo.com/aws-organizations/

---

## Câu 14 — ✅ ĐÚNG

### Câu hỏi

A cloud-native enterprise manages its environments using AWS Organizations within a multi-account structure. As part of the container-based architecture, the team packages workloads into Docker images and stores these in Amazon Elastic Container Registry (Amazon ECR).
These images must remain accessible only to accounts in the same AWS Organization. The images are pushed via a CI/CD process, which runs multiple times daily. The company wants to retain all tagged images while limiting untagged images to the five most recent ones to reduce storage costs.
The company prefers a solution that minimizes operational overhead, securely manages access, and ensures that only required ECR operations are permitted.
Which approach best meets the company’s goals with the LEAST operational burden?

### Các phương án

- **A.** Provision a public repository in ECR and apply a permissions policy scoped to essential ECR operations. Use the aws:PrincipalOrgID condition key to enforce organization-wide access control. Design an AWS Step Functions workflow to retain all tagged images and remove older untagged ones, keeping just the latest five.
- **B.** Configure a public ECR repository with limited permissions via a policy that employs the aws:PrincipalIsAWSService condition key for organizational restrictions. Set up an Amazon ECS Scheduled Task that retains all tagged images and automatically purges untagged images, ensuring only the five most recent remain.
- **C.** Create a private ECR repository and define a permissions policy that allows only the required ECR operations, with a condition using the aws:PrincipalOrgID key to restrict access to the organization. Apply a lifecycle rule to the repository to retain all tagged images and delete untagged images beyond the most recent five. 👈 *(bạn chọn)* ✅
- **D.** Set up a private ECR repository and attach a permissions policy restricting access based on the aws:PrincipalIsAWSService condition key, allowing only the necessary ECR actions. Use an AWS Glue job to keep all tagged images while routinely cleaning up untagged ones, preserving only the five most recent ones.

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

Amazon ECR (Elastic Container Registry) supports lifecycle policies that allow you to automatically manage the images’ lifecycle in your repositories. These policies can be used to remove untagged images or keep only the most recent ones based on criteria such as imageTagStatus or countNumber, which makes them ideal for reducing storage costs without needing custom logic or additional computing resources. In this case, applying a lifecycle policy that retains all tagged images and deletes only the older untagged ones while keeping the five most recent is a built-in capability that aligns perfectly with the company’s requirements and minimizes operational overhead.
Regarding access control, Amazon ECR supports fine-grained repository permissions using resource-based policies. Using the aws:PrincipalOrgID condition key ensures that only principals (such as IAM users, roles, or services) within the same AWS Organization are granted access. This method is highly effective for organization-wide restrictions and is recommended for securely sharing resources across multiple accounts. This approach simplifies management because the policy doesn’t require managing individual account IDs.

Using a private ECR repository with a permissions policy scoped to required actions and restricted by aws:PrincipalOrgID, combined with lifecycle rules to retain tagged images and limit untagged ones to the five most recent, meets the requirements for secure access, minimal operational overhead, and precise control over ECR operations.
Hence, the correct answer is: Create a private ECR repository and define a permissions policy that allows only the required ECR operations, with a condition using the aws:PrincipalOrgID key to restrict access to the organization. Apply a lifecycle rule to the repository to retain all tagged images and delete untagged images beyond the most recent five.
The option that says: Set up a private ECR repository and attach a permissions policy restricting access based on the aws:PrincipalIsAWSService condition key, allowing only the necessary ECR actions. Use an AWS Glue job to keep all tagged images while routinely cleaning up untagged ones, preserving only the five most recent ones is incorrect. Although it uses a private ECR repository and restricts access with a condition key (aws:PrincipalIsAWSService), that specific key is designed for service principals (such as allowing access to AWS services) and not restricting access based on organization membership. The correct key for that purpose is aws:PrincipalOrgID. Additionally, using an AWS Glue job to clean up old untagged images introduces unnecessary operational complexity. Glue is intended only for ETL (extract, transform, load) workloads, not for lifecycle management of container images. Using Glue here requires additional scheduling and scripting logic that could be entirely avoided with a native ECR lifecycle policy.
The option that says: Provision a public repository in ECR and apply a permissions policy scoped to essential ECR operations. Use the aws:PrincipalOrgID condition key to enforce organization-wide access control. Design an AWS Step Functions workflow to retain all tagged images and remove older untagged ones, keeping just the latest five  is incorrect. It proposes using a public ECR repository, which contradicts the security requirement that the images be accessible only to accounts within the same organization. Public repositories are visible to all AWS accounts (and, optionally, anonymous users), which opens up unintended exposure. Even though it correctly applies the aws:PrincipalOrgID condition for access control, using a public repository is a security misstep. Furthermore, implementing image cleanup using AWS Step Functions adds complexity compared to lifecycle policies designed for this exact use case, with less overhead.
The option that says: Configure a public ECR repository with limited permissions via a policy that employs the aws:PrincipalIsAWSService condition key for organizational restrictions. Set up an Amazon ECS Scheduled Task that retains all tagged images and automatically purges untagged images, ensuring only the five most recent remain is incorrect. It suffers from both architectural and security issues. Like the previous option, it mistakenly recommends a public repository, which goes against the requirement of restricting image access within the AWS Organization. It also uses the aws:PrincipalIsAWSService condition key, which is inappropriate for controlling cross-account access within an organization. Finally, the image cleanup is managed using an ECS Scheduled Task, which introduces operational complexity that can be avoided using ECR’s native lifecycle policy feature.

References:
https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgid
https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html

Check out this Amazon Elastic Container Registry Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-container-registry-amazon-ecr/

---

## Câu 15 — ❌ SAI

### Câu hỏi

A global enterprise manages multiple AWS accounts under a single organization using AWS Organizations. The enterprise leverages AWS CloudFormation to automate infrastructure provisioning and centrally manages permissions and roles using AWS Identity and Access Management (IAM).
As part of a new chargeback model, the finance department requires each department to apply project tags selected from a predefined list of tag values to every newly created resource.
When analyzing spending using the AWS Cost and Usage Report in AWS Cost Explorer, the finance team identified non-compliant tag values that disrupted cost attribution.
To enforce compliance, the company needs a scalable way to validate and implement resource tagging based on these project values.
Which approach offers the easiest and most effective way to enforce this?

### Các phương án

- **A.** Enable resource tagging enforcement using AWS Config rules. Integrate the rules with Organizations to evaluate tag compliance across accounts. Use automation documents to prevent cloudformation:CreateStack unless tags meet policy requirements. 👈 *(bạn chọn)*
- **B.** In the organization’s management account, define a tag policy with valid project tag values. Then, create a Service Control Policy (SCP) to deny cloudformation:CreateStack except if the required project tag is included. Attach the created SCP to the root of the organization. ✅
- **C.** Configure a tag policy in the Organizations management account to specify the approved project tag values. Then, implement an SCP that blocks the cloudformation:DetectStackResourceDrift operation unless a compliant project tag is part of the request. Apply this SCP at the organization’s root level.
- **D.** Use the AWS Tag Editor to audit and correct resource tags across all accounts. Schedule periodic reviews to identify non-compliant tags and update them to match the predefined project tag list

> **Bạn chọn:** A  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

Defining a tag policy in the AWS Organizations management account ensures all accounts have standardized approved project tag values. Although tag policies alone cannot enforce tag usage, they enable visibility into tag compliance across the organization.
Enforcing tag compliance, on the other hand, is effectively handled using a Service Control Policy (SCP) that denies the cloudformation:CreateStack operation unless a required project tag is included.
AWS separates governance from enforcement to provide organizations with flexibility, gradual adoption, and control over how policies are introduced and applied across accounts. Regarding tag policies within AWS Organizations, governance tools are designed to define standards, guide behavior, and report compliance without immediately disrupting workflows. This allows organizations to monitor tagging hygiene, educate teams, and identify non-compliant patterns before applying hard restrictions. In contrast, Service Control Policies (SCPs) are enforcement mechanisms that strictly prevent specific actions, such as creating resources without required tags, regardless of IAM permissions. By separating these functions, AWS enables a phased approach: organizations can start with visibility and alignment through governance and then escalate to enforcement when ready, reducing the risk of unintended disruptions while improving long-term operational consistency.

A combination of Organization Tag Policy and SCPs uses a combined governance and enforcement approach that meets the question’s scalability, compliance, and effectiveness requirements.
Hence, the correct answer is: In the organization’s management account, define a tag policy with valid project tag values. Then, create a Service Control Policy (SCP) to deny cloudformation:CreateStack except if the required project tag is included. Attach the created SCP to the root of the organization.
The option that says: Enable resource tagging enforcement using AWS Config rules. Integrate the rules with Organizations to evaluate tag compliance across accounts. Use automation documents to prevent cloudformation:CreateStack unless tags meet policy requirements is incorrect. AWS Config rules operate after resource creation and do not natively prevent API actions like cloudformation:CreateStack. While integrating AWS Config with AWS Organizations enables centralized tag compliance checks, it only provides post-creation evaluation. Automation documents (SSM documents) can remediate or notify but cannot block the initial stack creation in real-time. As a result, non-compliant resources can still be launched, violating the requirement to enforce tagging at creation.
The option that says: Configure a tag policy in the Organizations management account to specify the approved project tag values. Then, implement an SCP that blocks the cloudformation:DetectStackResourceDrift operation unless a compliant project tag is part of the request. Apply this SCP at the organization’s root level is incorrect. It targets an API operation unrelated to resource creation where tag enforcement must occur. While defining a tag policy in the AWS Organizations management account helps establish governance, denying cloudformation:DetectStackResourceDrift is ineffective. This action is used for diagnostics and does not create, modify, or tag resources. Blocking it does nothing to prevent the deployment of resources with invalid or missing tags.
The option that says: Use the AWS Tag Editor to audit and correct resource tags across all accounts. Schedule periodic reviews to identify non-compliant tags and update them to match the predefined project tag list is incorrect. While AWS Tag Editor can be used to search and edit tags across multiple accounts and regions, it does not provide any mechanism for enforcement. It cannot block resource creation or validate tag values against a predefined list. It only allows administrators to inspect and modify tags manually after the fact. Also, relying on scheduled manual reviews introduces operational overhead, delays in enforcement, and a high risk of human error or oversight. Finally, although Tag Editor supports visibility, it offers no integration with AWS Organizations governance policies like tag policies or SCPs, and it does not prevent the use of non-compliant project tags during provisioning.

References:
https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html

Check out this AWS Organizations Cheat Sheet:
https://tutorialsdojo.com/aws-organizations/

---

## Câu 16 — ❌ SAI

### Câu hỏi

A game development startup runs a multiplayer gaming platform powered by Amazon EC2 instances and AWS Lambda functions. The EC2 fleet supports always-on services like matchmaking and leaderboards, which run under a consistent and stable workload. In contrast, Lambda functions are triggered by unpredictable, bursty events like player actions, achievements, or chat messages.
To keep gameplay smooth and responsive, the platform uses a high-performance caching layer backed by Amazon MemoryDB for Redis, with dedicated MemoryDB cache nodes storing session data and player stats.
An AWS solutions architect is tasked with designing a cost-optimized infrastructure that cuts down on monthly operating costs without sacrificing performance.
What is the most cost-effective strategy to meet these goals?

### Các phương án

- **A.** Use an EC2 instance Savings Plan to commit to the EC2 compute resources financially. Apply a Compute Savings Plan to offset the baseline utilization of Lambda functions. Allocate reserved nodes to provision capacity for the MemoryDB cache nodes. ✅
- **B.** Leverage On-Demand pricing across all services to maintain flexibility. Use Lambda provisioned concurrency for better performance. Rely on auto-scaling EC2 instances instead of committing to Savings Plans.
- **C.** Use a Compute Savings Plan to cover EC2, Lambda, and MemoryDB usage in a single commitment. Configure Lambda reserved concurrency to manage unpredictable workloads. Provision MemoryDB cache nodes by acquiring reserved nodes to ensure dedicated capacity. 👈 *(bạn chọn)*
- **D.** Use EC2 Spot Instances to reduce compute costs for matchmaking and leaderboard services. Use On-Demand Lambda execution. Replace MemoryDB with Amazon ElastiCache.

> **Bạn chọn:** C  
> **Đáp án đúng:** A  
> **Kết quả:** ❌ Sai

### Giải thích

Savings Plans provide savings beyond On-Demand rates in exchange for a commitment to using a specified amount of compute power (measured per hour) for one or three years. Savings Plans offer a flexible pricing model that provides savings on AWS usage. You can save up to 72 percent on your AWS compute workloads.
EC2 Instance Savings Plans provide savings up to 72 percent off On-Demand, in exchange for a commitment to a specific instance family in a chosen AWS Region (for example, m5 in Virginia).
Compute Savings Plans provide the most flexibility and prices up to 66 percent off of On-Demand rates. These plans automatically apply to your EC2 instance usage, regardless of instance family (for example, m5, c5, etc.), instance size (for example, c5.large, c5.xlarge, etc.), Region (for example, us-east-1, us-east-2, etc.), operating system (for example, Windows, Linux, etc.), or tenancy (for example, Dedicated, default, Dedicated Host). They also apply to your Fargate and Lambda usage.
MemoryDB Reserved nodes, on the other hand, provide you with a significant discount compared to On-Demand node pricing. Reserved nodes are not physical nodes but a billing discount applied to using On-Demand nodes in your account. Discounts for reserved nodes are tied to node type and AWS Region.

Since the EC2 instances handle consistent and predictable workloads like matchmaking and leaderboards, committing to an EC2 instance Savings Plan is the most economical approach, as it offers the highest discount specifically for EC2 usage. The Lambda functions, which respond to bursty and inconsistent traffic patterns, should be covered using a Compute Savings Plan, but only up to the minimum baseline usage that can be forecasted. This configuration still allows cost savings without overcommitting. Finally, MemoryDB cache nodes, part of a caching layer with stable demand, are best supported through reserved nodes, ensuring provisioned capacity at a reduced cost compared to On-Demand.
This combination of service-specific purchase models aligns well with the application’s usage patterns, optimizing spending without compromising performance.
Hence, the correct answer is: Use an EC2 instance Savings Plan to commit to the EC2 compute resources financially. Apply a Compute Savings Plan to offset the baseline utilization of Lambda functions. Allocate reserved nodes to provision capacity for the MemoryDB cache nodes.
The option that says: Use a Compute Savings Plan to cover EC2, Lambda, and MemoryDB usage in a single commitment. Configure Lambda reserved concurrency to manage unpredictable workloads. Provision MemoryDB cache nodes by acquiring reserved nodes to ensure dedicated capacity is incorrect. This option is tempting at first glance because it offers a consolidated Compute Savings Plan, but this plan only gives moderate discounts. It does not take full advantage of workload predictability. EC2 instance Savings Plans offer deeper savings for EC2 workloads, so relying on Compute Savings Plans across all three services simply leaves potential savings on the table. Additionally, configuring Lambda reserved concurrency does not save money; it just reserves capacity. The answer also correctly suggests reserved nodes for MemoryDB, but this partial correctness isn’t enough to make it the best solution.
The option that says: Use EC2 Spot Instances to reduce compute costs for matchmaking and leaderboard services. Use On-Demand Lambda execution. Replace MemoryDB with Amazon ElastiCache is incorrect. This option makes several risky trade-offs in the name of savings, but they are inappropriate for the scenario. EC2 Spot Instances are not recommended for critical, always-on services like matchmaking or leaderboards because Spot capacity can be interrupted anytime. Using On-Demand Lambda means you’re just paying full price with no cost optimization, and replacing MemoryDB with ElastiCache is misleading. While ElastiCache is a Redis-compatible caching service, it lacks the high durability and multi-AZ replication features of MemoryDB, which are often essential in real-time gaming environments.
The option that says: Leverage On-Demand pricing across all services to maintain flexibility. Use Lambda provisioned concurrency for better performance. Rely on auto-scaling EC2 instances instead of committing to Savings Plans is incorrect. This option sacrifices cost savings entirely in the name of flexibility, which directly contradicts the goal of minimizing monthly expenses. Relying on On-Demand pricing across all services is simply the most expensive route. Using Lambda provisioned concurrency adds cost without addressing the variable, event-driven nature of Lambda workloads. Lastly, just depending on EC2 auto-scaling does not remove the need for committing to Savings Plans, especially when the EC2 usage is described as stable and predictable. This option misses the opportunity to optimize spend where it clearly could be.

References:
https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html
https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reservednodes.html

Check out this AWS Savings Plan Cheat Sheet:
https://tutorialsdojo.com/aws-savings-plan/

---
