# Review Mode udemy2_unseen – AWS Certified Solutions Architect Professional (Tutorials Dojo)

**Kết quả:** 13/27 câu đúng (48.15%) — ❌ Chưa đạt

**Unseen only:** 13/27 (48%) · **Mode:** review, blocks of 25 · **Date:** 2026-10-08

## Điểm theo domain

| Domain | Tỉ lệ đúng |
|---|---|
| CSAP – Accelerate Workload Migration and Modernization | 71.43% |
| CSAP – Continuous Improvement for Existing Solutions | 45.45% |
| CSAP – Design Solutions for Organizational Complexity | 0.00% |
| CSAP – Design for New Solutions | 37.50% |

## Bảng tổng hợp

| Câu | TD Q | Kết quả | Bạn chọn | Đáp án đúng |
|---|---|---|---|---|
| 1 | Q23 | ❌ Sai | B | D |
| 2 | Q60 | ✅ Đúng | A | A |
| 3 | Q66 | ✅ Đúng | D | D |
| 4 | Q35 | ❌ Sai | B | C |
| 5 | Q15 | ✅ Đúng | C | C |
| 6 | Q74 | ❌ Sai | D | C |
| 7 | Q1 | ✅ Đúng | A | A |
| 8 | Q58 | ❌ Sai | D | C |
| 9 | Q43 | ❌ Sai | D, E | B, E |
| 10 | Q46 | ✅ Đúng | C | C |
| 11 | Q19 | ✅ Đúng | D | D |
| 12 | Q33 | ❌ Sai | C | B |
| 13 | Q62 | ❌ Sai | C | B |
| 14 | Q9 | ✅ Đúng | A, E | A, E |
| 15 | Q54 | ❌ Sai | B | C |
| 16 | Q22 | ✅ Đúng | D | D |
| 17 | Q16 | ✅ Đúng | A | A |
| 18 | Q20 | ✅ Đúng | C | C |
| 19 | Q71 | ✅ Đúng | D | D |
| 20 | Q45 | ❌ Sai | A | D |
| 21 | Q50 | ❌ Sai | A, D | B, C |
| 22 | Q59 | ❌ Sai | B, C | A, D |
| 23 | Q25 | ✅ Đúng | A, B, F | A, B, F |
| 24 | Q29 | ❌ Sai | B | C |
| 25 | Q3 | ✅ Đúng | A, B | A, B |
| 26 | Q40 | ❌ Sai | A, C | C, D |
| 27 | Q28 | ❌ Sai | B, E | A, E |

---

## Câu 1 — ❌ SAI

### Câu hỏi

An Internet-of-Things (IoT) company is using Kinesis Data Streams (KDS) to process IoT data from field devices. Multiple consumer applications are using the incoming data streams and the engineers have noticed a performance lag for the data delivery speed between producers and consumers of the data streams.

As a Solutions Architect Professional, which of the following would you recommend to improve the performance for the given use-case?

### Các phương án

- **A.** Swap out Kinesis Data Streams with SQS FIFO queues to support the desired read throughput for the downstream applications
- **B.** Swap out Kinesis Data Streams with Kinesis Data Firehose to support the desired read throughput for the downstream applications 👈 *(bạn chọn)*
- **C.** Swap out Kinesis Data Streams with SQS Standard queues to support the desired read throughput for the downstream applications
- **D.** Use Enhanced Fanout feature of Kinesis Data Streams to support the desired read throughput for the downstream applications ✅

> **Bạn chọn:** B  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Use Enhanced Fanout feature of Kinesis Data Streams to support the desired read throughput for the downstream applications

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. By default, the 2MB/second/shard output is shared between all of the applications consuming data from the stream.

You should use enhanced fan-out if you have multiple consumers retrieving data from a stream in parallel. With enhanced fan-out developers can register stream consumers to use enhanced fan-out and receive their own 2MB/second pipe of read throughput per shard, and this throughput automatically scales with the number of shards in a stream.

via - https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

via - https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

Incorrect options:

Swap out Kinesis Data Streams with Kinesis Data Firehose to support the desired read throughput for the downstream applications -  Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security. Kinesis Data Firehose can only write to S3, Redshift, Elasticsearch or Splunk. You can't have applications consuming data streams from Kinesis Data Firehose, that's the job of Kinesis Data Streams. Therefore this option is not correct.

Swap out Kinesis Data Streams with SQS Standard queues to support the desired read throughput for the downstream applications

Swap out Kinesis Data Streams with SQS FIFO queues to support the desired read throughput for the downstream applications

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent. As multiple applications are consuming the same stream concurrently, both SQS Standard and SQS FIFO are not the right fit for the given use-case.

via - https://aws.amazon.com/kinesis/data-streams/faqs/

References:

https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

https://aws.amazon.com/kinesis/data-streams/faqs/

---

## Câu 2 — ✅ ĐÚNG

### Câu hỏi

A Wall Street based trading firm is modernizing its message queuing system by migrating from self-managed message-oriented middleware systems to Amazon SQS. The firm is using SQS to migrate several trading applications to the cloud to ensure high availability and cost efficiency while simplifying administrative complexity and overhead. The development team at the firm expects a peak rate of about 2,400 messages per second to be processed via SQS. It is important that the messages are processed in the order they are received.

Which of the following options can be used to implement this system in the most cost-effective way?

### Các phương án

- **A.** Use Amazon SQS FIFO queue in batch mode of 8 messages per operation to process the messages at the peak rate 👈 *(bạn chọn)* ✅
- **B.** Use Amazon SQS FIFO queue in batch mode of 12 messages per operation to process the messages at the peak rate
- **C.** Use Amazon SQS FIFO queue in batch mode of 4 messages per operation to process the messages at the peak rate
- **D.** Use Amazon SQS standard queue to process the messages

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Use Amazon SQS FIFO queue in batch mode of 8 messages per operation to process the messages at the peak rate

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues - Standard queues vs FIFO queues.

For FIFO queues, the order in which messages are sent and received is strictly preserved (i.e. First-In-First-Out). On the other hand, the standard SQS queues offer best-effort ordering. This means that occasionally, messages might be delivered in an order different from which they were sent.

By default, FIFO queues support up to 300 messages (API calls) per second (300 send, receive, or delete operations per second). When you batch 10 messages per operation (maximum), FIFO queues can support up to 3,000 (300*10) messages per second. Therefore, you need to process 8 messages per operation so that the FIFO queue can support up to 2,400 (300*8) messages per second, which satisfies the peak rate constraint.

FIFO Queues Overview:

via - https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html

Incorrect options:

Use Amazon SQS standard queue to process the messages - As messages need to be processed in order, therefore standard queues are ruled out.

Use Amazon SQS FIFO queue in batch mode of 12 messages per operation to process the messages at the peak rate - This option has been added as a distractor, as SQS FIFO only supports a maximum of 10 messages per operation in batch mode.

Use Amazon SQS FIFO queue in batch mode of 4 messages per operation to process the messages at the peak rate - As mentioned earlier in the explanation, you need to use FIFO queues in batch mode and process 8 messages per operation, so that the FIFO queue can support up to 2,400 messages per second. With 4 messages per operation, you can only support up to 1,200 messages per second.

References:

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html

https://aws.amazon.com/sqs/

https://aws.amazon.com/sqs/features/

---

## Câu 3 — ✅ ĐÚNG

### Câu hỏi

A web hosting company's CFO recently analyzed the company's monthly bill for the AWS account for the development environment and identified an opportunity to reduce the cost for AWS Elastic Beanstalk infrastructure in use. The CFO in consultation with the CTO has hired you as an AWS Certified Solutions Architect Professional to design a highly available solution that will provision an Elastic Beanstalk environment in the morning and terminate it at the end of the day. The solution should be designed with minimal operational overhead with a focus on minimizing costs. The solution should also facilitate the increased use of Elastic Beanstalk environments among different development teams and must provide a one-stop scheduler solution for all teams to keep the operational costs as low as possible.

Which of the following solution designs will you suggest to address these requirements?

### Các phương án

- **A.** Provision an EC2 Micro instance. Configure an IAM role with the required Elastic Beanstalk environment permissions and attach it to the instance profile. Create scripts on the instance to provision and terminate the Elastic Beanstalk environment. Set up cron jobs on the instance to execute the scripts
- **B.** Leverage the activity task of an AWS Step Function to provision and terminate the Elastic Beanstalk environment. Create a role for the Step Function to allow it to provision and terminate the Elastic Beanstalk environment. Execute the Step Function daily and use the "wait state" to control the start and stop time
- **C.** Configure the Elastic Beanstalk environment to use custom commands in the EC2 instance user data. Leverage the scheduled action for an Auto Scaling group to scale-out EC2 instances in the morning and scale-in the instance count to 0 to terminate the EC2 instances at the end of the day
- **D.** Set up separate Lambda functions to provision and terminate the Elastic Beanstalk environment. Configure a Lambda execution role granting the required Elastic Beanstalk environment permissions and assign the role to the Lambda functions. Configure cron expression based Amazon EventBridge events rules to trigger the Lambda functions 👈 *(bạn chọn)* ✅

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Set up separate Lambda functions to provision and terminate the Elastic Beanstalk environment. Configure a Lambda execution role granting the required Elastic Beanstalk environment permissions and assign the role to the Lambda functions. Configure cron expression based Amazon EventBridge events rules to trigger the Lambda functions

You can configure Lambda functions to make the Elastic Beanstalk API calls for provisioning and terminating the Elastic Beanstalk environment. To perform these API calls on a schedule, you can configure events in Amazon EventBridge events to trigger these Lambda functions at a specific time each day via cron expressions. Make sure that you attach the policy with the required Elastic Beanstalk environment permissions to the Lambda execution role.

via - https://aws.amazon.com/premiumsupport/knowledge-center/schedule-elastic-beanstalk-stop-restart/

via - https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html

Please review this excellent reference material for a deep-dive on how to stop and restart an Elastic Beanstalk environment on a schedule:

https://aws.amazon.com/premiumsupport/knowledge-center/schedule-elastic-beanstalk-stop-restart/

Incorrect options:

Leverage the activity task of an AWS Step Function to provision and terminate the Elastic Beanstalk environment. Create a role for the Step Function to allow it to provision and terminate the Elastic Beanstalk environment. Execute the Step Function daily and use the "wait state" to control the start and stop time - AWS Step Functions lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using Step Functions, you can design and run workflows that stitch together services such as AWS Lambda into feature-rich applications.

via - https://aws.amazon.com/step-functions/

This option involves cost components that are not needed. There is no need to keep the Step Function running in a "wait state" for the most part of the day just to control the provisioning and termination of Elastic Beanstalk environment. This is better handled via a "serverless cron" type of solution that can be invoked twice a day for provisioning and termination of Elastic Beanstalk environment.

Configure the Elastic Beanstalk environment to use custom commands in the EC2 instance user data. Leverage the scheduled action for an Auto Scaling group to scale-out EC2 instances in the morning and scale-in the instance count to 0 to terminate the EC2 instances at the end of the day - Scheduled action allows you to set your own scaling schedule for an Auto Scaling group. For example, let's say that every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can plan your scaling actions based on the predictable traffic patterns of your web application. Scaling actions are performed automatically as a function of time and date. A scheduled action sets the minimum, maximum, and desired sizes to what is specified by the scheduled action at the time specified by the scheduled action.

The issue with this option is that it's costly. Firstly, there is a cost element of running the EC2 instances for the day hours. Secondly, Elastic Beanstalk environment is provisioned via custom commands in the EC2 instance user data (it should also be emphasized that EC2 instance user data is not the best place to trigger the creation of an Elastic Beanstalk environment) however the environment itself is not terminated at the end of the day. So the costs for the resources created by Elastic Beanstalk keep accumulating. Hence this option is incorrect.

Provision an EC2 Micro instance. Configure an IAM role with the required Elastic Beanstalk environment permissions and attach it to the instance profile. Create scripts on the instance to provision and terminate the Elastic Beanstalk environment. Set up cron jobs on the instance to execute the scripts - This option involves cost components that are not needed. There is no need to provision an EC2 Micro instance and keep it running just to control the provisioning and termination of Elastic Beanstalk environment. This is better handled via a "serverless cron" type of solution that can be invoked twice a day for provisioning and termination of Elastic Beanstalk environment.

References:

https://aws.amazon.com/premiumsupport/knowledge-center/schedule-elastic-beanstalk-stop-restart/

https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html

https://aws.amazon.com/step-functions/

---

## Câu 4 — ❌ SAI

### Câu hỏi

A multi-national digital media company wants to exit out of the business of owning and maintaining its own IT infrastructure so it can redeploy resources toward innovation in Artificial Intelligence and related areas to create a better customer experience. As part of this digital transformation, the media company wants to archive about 9 PB of data in its on-premises data center to durable long term storage.

As a Solutions Architect Professional, what is your recommendation to migrate and store this data in the quickest and MOST cost-optimal way?

### Các phương án

- **A.** Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data directly into AWS Glacier
- **B.** Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier 👈 *(bạn chọn)*
- **C.** Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier ✅
- **D.** Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data directly into AWS Glacier

> **Bạn chọn:** B  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier

Snowball Edge Storage Optimized is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. It provides up to 80 TB of usable HDD storage, 40 vCPUs, 1 TB of SATA SSD storage, and up to 40 Gb network connectivity to address large scale data transfer and pre-processing use cases.

The data stored on the Snowball Edge device can be copied into the S3 bucket and later transitioned into AWS Glacier via a lifecycle policy. You can't directly copy data from Snowball Edge devices into AWS Glacier.

via - https://docs.aws.amazon.com/whitepapers/latest/aws-overview/migration-services.html

Incorrect options:

Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier - AWS Snowmobile is an exabyte-scale data transfer service used to move extremely large amounts of data to AWS. You can transfer up to 100 PB per Snowmobile. Snowmobile makes it easy to move massive volumes of data to the cloud, including video libraries, image repositories, or even a complete data center migration.

AWS recommends that you should use Snowmobile to migrate large datasets of 10PB or more in a single location. For datasets less than 10PB or distributed in multiple locations, you should use Snowball. So, this option is not the best fit for the given use-case.

via - https://aws.amazon.com/snowmobile/faqs/

Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data directly into AWS Glacier - As mentioned above, AWS recommends that you should use Snowmobile to migrate large datasets of 10PB or more in a single location. For datasets less than 10PB or distributed in multiple locations, you should use Snowball. So, this option is not the best fit for the given use-case.

Although you should note that for Snowmobile, you can import your data directly into Glacier.

Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data directly into AWS Glacier - As mentioned earlier, you can't directly copy data from Snowball Edge devices into AWS Glacier. Hence, this option is incorrect.

References:

https://aws.amazon.com/snowball/

https://docs.aws.amazon.com/snowball/latest/ug/how-it-works.html

https://aws.amazon.com/snowmobile/faqs/

https://docs.aws.amazon.com/whitepapers/latest/aws-overview/migration-services.html

---

## Câu 5 — ✅ ĐÚNG

### Câu hỏi

A web development studio runs hundreds of Proof-of-Concept (PoC) and demo applications on virtual machines running on an on-premises server. Many of the applications are simple PHP, JavaScript or Python web applications which are no longer actively developed and serve little traffic.

As a Solutions Architect Professional, which of the following approaches would you suggest to migrate these applications to AWS with the lowest infrastructure cost and least development effort?

### Các phương án

- **A.** Leverage VM Import/Export to create AMIs for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image
- **B.** Leverage AWS Server Migration Service (SMS) to create AMIs for each virtual machine and run each application on a dedicated EC2 instance
- **C.** Dockerize each application and then deploy to an ECS cluster running behind an Application Load Balancer 👈 *(bạn chọn)* ✅
- **D.** Migrate the application code to use a serverless stack comprising of Lambda functions and DynamoDB

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Dockerize each application and then deploy to an ECS cluster running behind an Application Load Balancer

Amazon Elastic Container Service (ECS) is a highly scalable, high performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of Amazon EC2 instances.

How ECS Works:

via - https://aws.amazon.com/ecs/

Using an ECS cluster running behind an Application Load Balancer offers advantages such as Application Load Balancers allow containers to use dynamic host port mapping so that multiple tasks from the same service are allowed per container instance. This reduces the number of instances required for migration and therefore reduces the overall costs.

via - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html

Incorrect options:

Migrate the application code to use a serverless stack comprising of Lambda functions and DynamoDB - It would take significant development effort to migrate the existing applications to a serverless stack. In addition, some of the web applications, such as those built using PHP are not supported by Lambda functions (unless you use custom runtime). So, this option is incorrect.

Leverage AWS Server Migration Service (SMS) to create AMIs for each virtual machine and run each application on a separate EC2 instance - AWS Server Migration Service automates the migration of your on-premises VMware vSphere, Microsoft Hyper-V/SCVMM, and Azure virtual machines to the AWS Cloud. AWS SMS incrementally replicates your server VMs as cloud-hosted Amazon Machine Images (AMIs) ready for deployment on Amazon EC2. As this solution provisions a separate EC2 instance for each application, so it is a costly migration solution.

Leverage VM Import/Export to create AMIs for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image - VM Import/Export enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances. You can use Elastic Beanstalk to quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.

A single-instance environment doesn't have a load balancer, which can help you reduce costs compared to a load-balanced, scalable environment. Use a single-instance environment if you expect your production application to have low traffic or if you are doing remote development. For the given use-case, you will end up creating as many instances as the number of applications, which will turn out to be a really costly solution.

References:

https://aws.amazon.com/ecs/

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html

---

## Câu 6 — ❌ SAI

### Câu hỏi

A leading internet television network company uses AWS Cloud for analytics, recommendation engines and video transcoding. To monitor and optimize this network, the engineering team at the company has developed a solution for ingesting, augmenting, and analyzing the multiple terabytes of data its network generates daily in the form of virtual private cloud (VPC) flow logs. This would enable the company to identify performance-improvement opportunities such as identifying apps that are communicating across regions and collocating them. The VPC flow logs data is funneled into Kinesis Data Streams which further acts as the source of a delivery stream for Kinesis Firehose. The engineering team has now configured a Kinesis Agent to send the VPC flow logs data from another set of network devices to the same Firehose delivery stream. They noticed that data is not reaching Firehose as expected.

As a Solutions Architect Professional, which of the following options would you identify as the MOST plausible root cause behind this issue?

### Các phương án

- **A.** Kinesis Firehose delivery stream has reached its limit and needs to be scaled manually
- **B.** The data sent by Kinesis Agent is lost because of a configuration error
- **C.** Kinesis Agent cannot write to a Kinesis Firehose for which the delivery stream source is already set as Kinesis Data Streams ✅
- **D.** Kinesis Agent can only write to Kinesis Data Streams, not to Kinesis Firehose 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Kinesis Agent cannot write to a Kinesis Firehose for which the delivery stream source is already set as Kinesis Data Streams

Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

When a Kinesis data stream is configured as the source of a Firehose delivery stream, Firehose’s PutRecord and PutRecordBatch operations are disabled and Kinesis Agent cannot write to Firehose delivery stream directly. Data needs to be added to the Kinesis data stream through the Kinesis Data Streams PutRecord and PutRecords operations instead. Therefore, this option is correct.

Incorrect options:

Kinesis Agent can only write to Kinesis Data Streams, not to Kinesis Firehose - Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Kinesis Data Streams or Kinesis Firehose. So this option is incorrect.

Kinesis Firehose delivery stream has reached its limit and needs to be scaled manually - Kinesis Firehose is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. Therefore this option is not correct.

How Kinesis Firehose works:

via - https://aws.amazon.com/kinesis/data-firehose/

The data sent by Kinesis Agent is lost because of a configuration error - This is a made-up option and has been added as a distractor.

References:

https://aws.amazon.com/kinesis/data-firehose/

https://aws.amazon.com/kinesis/data-firehose/faqs/

---

## Câu 7 — ✅ ĐÚNG

### Câu hỏi

The DevOps team at a leading social media company uses Chef to automate the configurations of servers in the on-premises data center. The CTO at the company now wants to migrate the IT infrastructure to AWS Cloud with minimal changes to the server configuration workflows and at the same time account for less operational overhead post-migration to AWS. The company has hired you as an AWS Certified Solutions Architect Professional to recommend a solution for this migration.

Which of the following solutions would you recommend to address the given use-case?

### Các phương án

- **A.** Replatform the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS 👈 *(bạn chọn)* ✅
- **B.** Replatform the IT infrastructure to AWS Cloud by leveraging AWS Config as a configuration management service to automate the configurations of servers on AWS
- **C.** Rehost the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS
- **D.** Rehost the IT infrastructure to AWS Cloud by leveraging AWS Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Replatform the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS

Replatforming is a migration strategy where you don't change the core architecture but leverage some cloud optimizations. Here are the six most common application migration strategies:

via - https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

For the given use-case, you can leverage AWS OpsWorks to automate the configurations of your servers. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments. Specifically, OpsWorks for Chef Automate provides a fully managed Chef server and suite of automation tools that give you workflow automation for continuous deployment, automated testing for compliance and security, and a user interface that gives you visibility into your nodes and their status.

The migration results in an optimized IT infrastructure as OpsWorks for Chef Automate provides a configuration management experience that is fully compatible with Chef, including all community scripts and tooling, but without the operational overhead of managing the underlying Chef server.

Incorrect options:

Replatform the IT infrastructure to AWS Cloud by leveraging AWS Config as a configuration management service to automate the configurations of servers on AWS - AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - "What did my AWS resource look like at xyz point in time?". You cannot use AWS Config as a configuration management service to automate the configurations of servers on AWS.

How Config Works:

via - https://aws.amazon.com/config/

Rehost the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS - This option is incorrect because the correct migration strategy used for this use-case is Replatforming, as described in the explanation above. Rehosting refers to a migration strategy where no cloud optimizations are done and the application is migrated as-is.

Rehost the IT infrastructure to AWS Cloud by leveraging AWS Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS - As explained above, Rehosting is not the correct migration strategy for the given use-case. Elastic Beanstalk makes it easier for developers to quickly deploy and manage applications in the AWS Cloud. Developers simply upload their application, and Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring. You cannot use Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS.

References:

https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

https://aws.amazon.com/opsworks/

https://aws.amazon.com/config/

https://aws.amazon.com/elasticbeanstalk/faqs/

---

## Câu 8 — ❌ SAI

### Câu hỏi

A leading Internet-of-Things (IoT) solutions company needs to develop a platform that would analyze real-time clickstream events from embedded sensors in consumer electronic devices. The company has hired you as an AWS Certified Solutions Architect Professional to consult the engineering team and develop a solution using the AWS Cloud. The company wants to use clickstream data to perform data science, develop algorithms, and create visualizations and dashboards to support the business stakeholders. Each of these groups would work independently and would need real-time access to this clickstream data for their applications.

Which of the following options would provide a highly available and fault-tolerant solution to capture the clickstream events from the source and also provide a simultaneous feed of the data stream to the downstream applications?

### Các phương án

- **A.** Use AWS Kinesis Data Analytics to facilitate multiple applications consume and analyze same streaming data concurrently and independently
- **B.** Use AWS Kinesis Data Firehose to allow applications to consume the same streaming data concurrently and independently
- **C.** Use AWS Kinesis Data Streams to facilitate multiple applications consume same streaming data concurrently and independently ✅
- **D.** Use Amazon SQS to facilitate multiple applications process same streaming data concurrently and independently 👈 *(bạn chọn)*

> **Bạn chọn:** D  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Use AWS Kinesis Data Streams to facilitate multiple applications consume the same streaming data concurrently and independently

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.

Amazon Kinesis Data Streams enables real-time processing of streaming big data. It provides ordering of records, as well as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications. The Amazon Kinesis Client Library (KCL) delivers all records for a given partition key to the same record processor, making it easier to build multiple applications reading from the same Amazon Kinesis data stream (for example, to perform counting, aggregation, and filtering).

Amazon Kinesis Data Streams is recommended when you need the ability for multiple applications to consume the same stream concurrently. For example, you have one application that updates a real-time dashboard and another application that archives data to Amazon Redshift. You want both applications to consume data from the same stream concurrently and independently.

KDS provides the ability for multiple applications to consume the same stream concurrently

via - https://aws.amazon.com/kinesis/data-streams/faqs/

Incorrect options:

Use AWS Kinesis Data Firehose to allow applications to consume same streaming data concurrently and independently - Amazon Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security. As Kinesis Data Firehose is used to load streaming data into data stores, therefore this option is incorrect.

Use AWS Kinesis Data Analytics to facilitate multiple applications consume and analyze same streaming data concurrently and independently - Amazon Kinesis Data Analytics is the easiest way to analyze streaming data in real-time.  You can quickly build SQL queries and sophisticated Java applications using built-in templates and operators for common processing functions to organize, transform, aggregate, and analyze data at any scale. Kinesis Data Analytics enables you to easily and quickly build queries and sophisticated streaming applications in three simple steps: setup your streaming data sources, write your queries or streaming applications and set up your destination for processed data. As Kinesis Data Analytics is used to build SQL queries on streaming data, therefore this option is incorrect.

Use Amazon SQS to facilitate multiple applications process same streaming data concurrently and independently - Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent. For SQS, you cannot have the same message being consumed by multiple consumers at the same time, therefore this option is incorrect.

References:

https://aws.amazon.com/kinesis/data-streams/faqs/

https://aws.amazon.com/kinesis/data-firehose/faqs/

https://aws.amazon.com/kinesis/data-analytics/faqs/

---

## Câu 9 — ❌ SAI

### Câu hỏi

A retail company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for managing a serverless application that consists of multiple API gateways, Lambda functions, S3 buckets and DynamoDB tables. The company is getting reports from customers that some of the application components seem to be lagging while loading dynamic images and some are timing out with the "504 Gateway Timeout" error. As part of your investigations to identify the root cause behind this issue, you can confirm that DynamoDB monitoring metrics are at acceptable levels.

Which of the following steps would you recommend to address these application issues? (Select two)

### Các phương án

- **A.** Process and analyze the VPC Flow Logs to determine if there is packet loss between the Lambda function and S3
- **B.** Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals ✅
- **C.** Enable execution logging for the API Gateway. Process and analyze the execution logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **D.** Enable access logging for the API Gateway. Process and analyze the access logs in the API Gateway for HTTP errors to determine the root cause of the errors 👈 *(bạn chọn)*
- **E.** Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors 👈 *(bạn chọn)* ✅

> **Bạn chọn:** D, E  
> **Đáp án đúng:** B, E  
> **Kết quả:** ❌ Sai

### Giải thích

Correct options:

Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals

To help you troubleshoot failures in a function, the Lambda service logs all requests handled by a Lambda function and also automatically stores logs generated by your code through Amazon CloudWatch Logs. You can insert logging statements into your code to determine processing times for requested images. These logs can then be processed at certain pre-configured intervals for further analysis.

via - https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html

Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors

You can use AWS X-Ray to visualize the components of your application, identify performance bottlenecks such as the one described in the use-case for processing images and troubleshoot those requests that resulted in an error. Your Lambda functions send trace data to X-Ray, and X-Ray processes the data to generate a service map and searchable trace summaries.

via - https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html

Incorrect options:

Enable execution logging for the API Gateway. Process and analyze the execution logs in the API Gateway for HTTP errors to determine the root cause of the errors

Enable access logging for the API Gateway. Process and analyze the access logs in the API Gateway for HTTP errors to determine the root cause of the errors

For an API Gateway, a "504 Gateway Timeout" error implies an "Endpoint Request Timed-out Exception".

via - https://docs.aws.amazon.com/apigateway/api-reference/handling-errors/

To troubleshoot an API Gateway REST API or WebSocket API that you're developing, enable execution logging and access logging to Amazon CloudWatch Logs. Execution logs contain helpful information that you can use to identify and fix most errors with your APIs. Access logs contain details about who accessed your API and how they accessed it, which you can also use for troubleshooting.

via - https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-cloudwatch-logs/

However, neither execution logs nor access logs at the API Gateway level will provide information to identify the root cause for the "504 Gateway Timeout" error as it needs to be analyzed at the source system level which is Lambda function for the given use-case, as that's where the images are being processing and the application is lagging or timing out for some of those images. Another thing to note is that only access logs are available for HTTP APIs, so you do not have access to execution logs for the given use-case.

Therefore, both of these options are incorrect.

Process and analyze the VPC Flow Logs to determine if there is packet loss between the Lambda function and S3

VPC Flow Logs allow you to capture information about the IP traffic going to and from network interfaces in your VPC. You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.

via - https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

This option has been added as a distractor as you cannot use VPC Flow Logs to determine packet loss. AWS has a built-in tool called AWSSupport-SetupIPMonitoringFromVPC that you can use to monitor metrics such as latency and the percentage of packet loss across a network path. It monitors the selected target IP addresses by continuously running ping, MTR, TCP traceroute, and tracepath network diagnostic tests.

References:

https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html

https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html

https://docs.aws.amazon.com/apigateway/api-reference/handling-errors/

https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-cloudwatch-logs/

https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/

https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

---

## Câu 10 — ✅ ĐÚNG

### Câu hỏi

A company has built its serverless solution using Amazon API Gateway REST API and AWS Lambda across multiple AWS Regions configured into a single AWS account. During peak hours, customers began to receive 429 Too Many Requests errors from multiple API methods. While troubleshooting the issue, the team realized that AWS Lambda function(s) have not been invoked for these API methods. Also, the company wants to provide a separate quota for its premium customers to access the APIs.

Which solution will you offer to meet this requirement?

### Các phương án

- **A.** The error is the outcome of the company reaching its API Gateway account limit for calls per second, set Lambda-level throttling targets in the API Gateway usage plan, and configure customers to use a particular API method when the client identifier is set
- **B.** The error is the outcome of the company reaching its API Gateway account per-method limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers
- **C.** The error is the outcome of the company reaching its API Gateway account limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers 👈 *(bạn chọn)* ✅
- **D.** The error is the outcome of the company reaching its API Gateway limits for the steady-state requests per second (RPS) across all APIs within an AWS account per Region. These limits can be overwritten by configuring the AWS Regional throttling parameters to a greater value. However, based on the AWS account type, a limit is set to the overwritten throttling values

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct options:

The error is the outcome of the company reaching its API Gateway account limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers

After you create, test, and deploy your APIs, you can use API Gateway usage plans to make them available as product offerings for your customers. You can configure usage plans and API keys to allow customers to access selected APIs, and begin throttling requests to those APIs based on defined limits and quotas. These can be set at the API, or API method level.

Per-client throttling limits are applied to clients that use API keys associated with your usage plan as a client identifier. Note that these limits can't be higher than the per-account limits.

When request submissions exceed the steady-state request rate and burst limits, API Gateway begins to throttle requests. Clients may receive 429 Too Many Requests error responses at this point. Since the error is at API Gateway, the Lambda functions configured are not invoked at all.

How throttling limit settings are applied in API Gateway:

via - https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

Incorrect options:

"The error is the outcome of the company reaching its API Gateway account per-method limit for calls per second, configure API keys as client identifiers using usage plans to define the per-client throttling limits for premium customers - You should note that a throttling limit sets the target point at which request throttling should start. This can be set at the API or API method level. The use case states that the 429 Too Many Requests errors were received from multiple API methods, so the API Gateway reached its limit at the API level since none of the methods invoked the downstream Lambda function. So this option is incorrect.

The error is the outcome of the company reaching its API Gateway account limit for calls per second, set Lambda-level throttling targets in the API Gateway usage plan, and configure customers to use a particular API method when the client identifier is set - This is incorrect. You cannot define Lambda-level throttling targets in the API Gateway usage plan.

The error is the outcome of the company reaching its API Gateway limits for the steady-state requests per second (RPS) across all APIs within an AWS account per Region. These limits can be overwritten by configuring the AWS Regional throttling parameters to a greater value. However, based on the AWS account type, a limit is set to the overwritten throttling values - Per-account limits are applied to all APIs in an account in a specified Region. The account-level rate limit can be increased upon request - higher limits are possible with APIs that have shorter timeouts and smaller payloads. To request an increase in account-level throttling limits per Region, contact the AWS Support Center. It cannot be done from the AWS account directly.

References:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

---

## Câu 11 — ✅ ĐÚNG

### Câu hỏi

An e-commerce company has hired an AWS Certified Solutions Architect Professional to transform a standard three-tier web application architecture in AWS. Currently, the web and application tiers run on EC2 instances and the database tier runs on RDS MySQL. The company wants to redesign the web and application tiers to use API Gateway with Lambda Functions with the final goal of deploying the new application within 6 months. As an immediate short-term task, the Engineering Manager has mandated the Solutions Architect to reduce costs for the existing stack.

Which of the following options should the Solutions Architect recommend as the MOST cost-effective and reliable solution?

### Các phương án

- **A.** Provision Reserved Instances for the web and application tiers and On-Demand Instances for the database tier
- **B.** Provision Reserved Instances for the web, application and database tiers
- **C.** Provision Spot Instances for the web and application tiers and Reserved Instances for the database tier
- **D.** Provision On-Demand Instances for the web and application tiers and Reserved Instances for the database tier 👈 *(bạn chọn)* ✅

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Provision On-Demand Instances for the web and application tiers and Reserved Instances for the database tier

EC2 Instances support five different ways to pay for provisioning the servers: On-Demand, Savings Plans, Reserved Instances, Spot Instances and Dedicated Hosts.

via - https://aws.amazon.com/ec2/pricing/

An On-Demand Instance is an instance that you use on-demand. You have full control over its lifecycle — you decide when to launch, stop, hibernate, start, reboot, or terminate it. There is no long-term commitment required when you purchase On-Demand Instances. There is no upfront payment and you pay only for the seconds that your On-Demand Instances are running. The price per second for running an On-Demand Instance is fixed. On-demand instances cannot be interrupted. However, On-demand instances are not as cost-effective as Reserved instances.

A Spot Instance is an unused EC2 instance that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts (up to 90%), you can lower your Amazon EC2 costs significantly. Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks. These can be terminated at short notice, so these are not suitable for critical workloads that need to run at a specific point in time.

Reserved Instances provide you with significant savings (up to 75%) on your Amazon EC2 costs compared to On-Demand Instance pricing. Reserved Instances are not physical instances, but rather a billing discount applied to the use of On-Demand Instances in your account. You can purchase a Reserved Instance for a one-year or three-year commitment, with the three-year commitment offering a bigger discount. Reserved instances cannot be interrupted.

For the given use-case, only the web and application tiers would be re-engineered using API Gateway and Lambda within a duration of 6 months, so you cannot use Reserved Instances for these tiers as the minimum duration to purchase a Reserved Instance is 1 year. Additionally, using Spot Instances for these tiers is also ruled out because these can be terminated at short notice and would not be able to offer reliability for the web and application tiers. Therefore On-Demand is the best option for the web and application tiers. As the proposed transformation would not impact the database tier running on RDS MySQL, therefore you can purchase Reserved Instances for the database tier as the most cost-effective solution.

Incorrect options:

Provision Reserved Instances for the web, application and database tiers - As explained above, Reserved Instances are not a good fit for running the web and application tiers, so this option is not correct.

Provision Spot Instances for the web and application tiers and Reserved Instances for the database tier - As explained above, Spot Instances are not a good fit for running the web and application tiers, so this option is not correct.

Provision Reserved Instances for the web and application tiers and On-Demand Instances for the database tier - As explained above, Reserved Instances are not a good fit for running the web and application tiers, so this option is not correct. Also using On-Demand Instances for the database tier is not the most cost-effective option as you should use Reserved Instances for the database tier.

Reference:

https://aws.amazon.com/ec2/pricing/

---

## Câu 12 — ❌ SAI

### Câu hỏi

A leading hotel reviews website has a repository of more than one million high-quality digital images. When this massive volume of images became too cumbersome to handle in-house, the company decided to offload the content to a central repository on Amazon S3 as part of its hybrid cloud strategy. The company now wants to reprocess its entire collection of photographic images to change the watermarks. The company wants to use Amazon EC2 instances and Amazon SQS in an integrated workflow to generate the sizes they need for each photo. The team wants to process a few thousand photos each night, using Amazon EC2 Spot Instances. The team uses Amazon SQS to communicate the photos that need to be processed and the status of the jobs. To handle certain sensitive photos, the team wants to postpone the delivery of certain messages to the queue by one minute while all other messages need to be delivered immediately to the queue.

As a Solutions Architect Professional, which of the following solutions would you suggest to the company to handle the workflow for sensitive photos?

### Các phương án

- **A.** Use visibility timeout to postpone the delivery of certain messages to the queue by one minute
- **B.** Use message timers to postpone the delivery of certain messages to the queue by one minute ✅
- **C.** Use delay queues to postpone the delivery of certain messages to the queue by one minute 👈 *(bạn chọn)*
- **D.** Use dead-letter queues to postpone the delivery of certain messages to the queue by one minute

> **Bạn chọn:** C  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Use message timers to postpone the delivery of certain messages to the queue by one minute

You can use message timers to set an initial invisibility period for a message added to a queue. So, if you send a message with a 60-second timer, the message isn't visible to consumers for its first 60 seconds in the queue. The default (minimum) delay for a message is 0 seconds. The maximum is 15 minutes. Therefore, you should use message timers to postpone the delivery of certain messages to the queue by one minute.

Incorrect options:

Use dead-letter queues to postpone the delivery of certain messages to the queue by one minute - Dead-letter queues can be used by other queues (source queues) as a target for messages that can't be processed (consumed) successfully. Dead-letter queues are useful for debugging your application or messaging system because they let you isolate problematic messages to determine why their processing doesn't succeed. You cannot use dead-letter queues to postpone the delivery of certain messages to the queue by one minute.

Use visibility timeout to postpone the delivery of certain messages to the queue by one minute - Visibility timeout is a period during which Amazon SQS prevents other consumers from receiving and processing a given message. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours. You cannot use visibility timeout to postpone the delivery of certain messages to the queue by one minute.

Use delay queues to postpone the delivery of certain messages to the queue by one minute - Delay queues let you postpone the delivery of all new messages to a queue for several seconds, for example, when your consumer application needs additional time to process messages. If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period. The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes. You cannot use delay queues to postpone the delivery of only certain messages to the queue by one minute.

via - https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html

References:

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html

---

## Câu 13 — ❌ SAI

### Câu hỏi

An e-commerce web application is hosted on Amazon EC2 instances that are fronted by Application Load Balancer (ALB) configured with an Auto Scaling group (ASG). Enhanced security is provided to the ALB by AWS WAF web ACLs. As per the company's security policy, AWS CloudTrail is activated and logs are configured to be stored on Amazon S3 and CloudWatch Logs.

A discount sales offer was run on the application for a week. The support team has noticed that a few of the instances have rebooted taking down the log files and all temporary data with them. Initial analysis has confirmed that the incident took place during off-peak hours. Even though the incident did not cause any sales or revenue loss, the CTO has asked the security team to fix the security error that has allowed the incident to go unnoticed and eventually untraceable.

What steps will you implement to permanently record all traffic coming into the application?

### Các phương án

- **A.** To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring
- **B.** Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking ✅
- **C.** Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking 👈 *(bạn chọn)*
- **D.** Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting

> **Bạn chọn:** C  
> **Đáp án đúng:** B  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking

The logging destinations that you can choose from for your AWS WAF logs are:

Amazon CloudWatch Logs
Amazon Simple Storage Service
Amazon Kinesis Data Firehose

To send logs to Amazon Kinesis Data Firehose, you send logs from your web ACL to an Amazon Kinesis Data Firehose with a configured storage destination. After you enable logging, AWS WAF delivers logs to your storage destination through the HTTPS endpoint of Kinesis Data Firehose.

One AWS WAF log is equivalent to one Kinesis Data Firehose record. If you typically receive 10,000 requests per second and you enable full logs, you should have 10,000 records per second setting in Kinesis Data Firehose.

Incorrect options:

Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking - As discussed above, the logging destinations that you can choose from for your AWS WAF logs are Amazon CloudWatch Logs, Amazon Simple Storage Service, and Amazon Kinesis Data Firehose. Amazon CloudTrail is not a valid destination for WAF ACL logs.

To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring - VPC Flow You should also note that VPC Flow Logs cannot capture all traffic coming into the application as these can only capture information about the IP traffic going to and from network interfaces in your VPC. In addition, VPC Flow Logs can be directly published only to the following destinations: Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose. So this option is incorrect.

Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting - Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. Elastic Load Balancing access logs are stored in Amazon S3 buckets and it is not possible to directly write the logs to Kinesis Data Firehose.

References:

https://aws.amazon.com/about-aws/whats-new/2021/12/awf-waf-cloudwatch-log-s3-bucket/

https://docs.aws.amazon.com/waf/latest/developerguide/logging-destinations.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

---

## Câu 14 — ✅ ĐÚNG

### Câu hỏi

A data analytics company needs to set up a data lake on Amazon S3 for a financial services client. The data lake is split in raw and curated zones. For compliance reasons, the source data needs to be kept for a minimum of 5 years. The source data arrives in the raw zone and is then processed via an AWS Glue based ETL job into the curated zone. The business analysts run ad-hoc queries only on the data in the curated zone using Athena. The team is concerned about the cost of data storage in both the raw and curated zones as the data is increasing at a rate of 2 TB daily in each zone.

Which of the following options would you implement together as the MOST cost-optimal solution?
(Select two)

### Các phương án

- **A.** Setup a lifecycle policy to transition the raw zone data into Glacier Deep Archive after 1 day of object creation 👈 *(bạn chọn)* ✅
- **B.** Create a Lambda function based job to delete the raw zone data after 1 day
- **C.** Setup a lifecycle policy to transition the curated zone data into Glacier Deep Archive after 1 day of object creation
- **D.** Use Glue ETL job to write the transformed data in the curated zone using CSV format
- **E.** Use Glue ETL job to write the transformed data in the curated zone using a compressed file format 👈 *(bạn chọn)* ✅

> **Bạn chọn:** A, E  
> **Đáp án đúng:** A, E  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct options:

Setup a lifecycle policy to transition the raw zone data into Glacier Deep Archive after 1 day of object creation

You can manage your objects so that they are stored cost-effectively throughout their lifecycle by configuring their Amazon S3 Lifecycle. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. For example, you might choose to transition objects to the S3 Standard-IA storage class 30 days after you created them, or archive objects to the S3 Glacier storage class one year after creating them.

For the given use-case, the raw zone consists of the source data, so it cannot be deleted due to compliance reasons. Therefore, you should use a lifecycle policy to transition the raw zone data into Glacier Deep Archive after 1 day of object creation.

Please read more about S3 Object Lifecycle Management:

via - https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html

Use Glue ETL job to write the transformed data in the curated zone using a compressed file format

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics.

You cannot transition the curated zone data into Glacier Deep Archive because it is used by the business analysts for ad-hoc querying. Therefore, the best optimization is to have the curated zone data stored in a compressed format via the Glue job. The compressed data would reduce the storage cost incurred on the data in the curated zone.

Please see this example for a Glue ETL Pipeline:

via - https://aws.amazon.com/glue/

Incorrect options:

Create a Lambda function based job to delete the raw zone data after 1 day - As mentioned in the use-case, the source data needs to be kept for a minimum of 5 years for compliance reasons. Therefore the data in the raw zone cannot be deleted after 1 day.

Setup a lifecycle policy to transition the curated zone data into Glacier Deep Archive after 1 day of object creation - You cannot transition the curated zone data into Glacier Deep Archive because it is used by the business analysts for ad-hoc querying. Hence this option is incorrect.

Use Glue ETL job to write the transformed data in the curated zone using CSV format - It is cost-optimal to write the data in the curated zone using a compressed format instead of CSV format. The compressed data would reduce the storage cost incurred on the data in the curated zone. So, this option is incorrect.

References:

https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html

https://aws.amazon.com/glue/

---

## Câu 15 — ❌ SAI

### Câu hỏi

A social media company is transitioning its IT infrastructure from its on-premises data center to the AWS Cloud. The company wants to move its data artifacts, 200 TB in total size, to Amazon S3 on the AWS Cloud in the shortest possible time. The company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for this data migration. In terms of the networking infrastructure, the company has a 500 Mbps Direct Connect connection to the AWS Cloud as well as an IPSec based AWS VPN connection using the public internet that supports a bandwidth of 1 Gbps.

Which of the following solutions would you recommend to address the given use-case?

### Các phương án

- **A.** Leverage the 500 Mbps Direct Connect connection to transfer the data to S3 over the dedicated connection
- **B.** Leverage the 1Gbps IPSec based AWS VPN connection to transfer the data to S3 over the public internet 👈 *(bạn chọn)*
- **C.** Order three AWS Snowball Edge appliances, split and transfer the data to these three appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3 ✅
- **D.** Leverage S3 Transfer Acceleration to transfer the data to S3

> **Bạn chọn:** B  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Order three AWS Snowball Edge appliances, split and transfer the data to these three appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3

The AWS Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities. Each Snowball Edge device can transport data at speeds faster than the internet. This transport is done by shipping the data in the appliances through a Regional carrier. The appliances are rugged shipping containers, complete with E Ink shipping labels. Snowball Edge devices have three options for device configurations – storage optimized, compute optimized, and with GPU.

Snowball Edge is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. The AWS Snow Family is ideal for customers moving large batches of data at once. The AWS Snowball has a typical 5-7 days turnaround time. As each Snowball Edge device can handle 80TB of data, you can order 3 such devices to take care of the data transfer for the given use-case.

Incorrect options:

Leverage the 1Gbps IPSec based AWS VPN connection to transfer the data to S3 over the public internet

The given use-case requires transferring 200 TB of archived data within the shortest possible duration. Now, the IPSec based AWS VPN connection assures a speed of 1 Gbps (Gigabits per second). As 1 Byte = 8 bits, therefore you can transfer 0.125 GBps (Gigabytes per second).

So the hourly data transfer is 0.1256060 = 450 GB or approximately 0.45 TB.

So the approximate daily data transfer is 0.45 * 24 = ~ 10 TB

Therefore, the entire archived dataset of 200 TB can be transferred in 20 days. As explained above, using Snowball appliances, you can complete this data transfer in just 5-7 days. So this option is incorrect.

Leverage the 500 Mbps Direct Connect connection to transfer the data to S3 over the dedicated connection - We established above that a 1GBps connection would take 20 days to transfer the dataset, so the 500 Mbps Direct Connect connection would take 40 days to transfer the dataset. So this option is incorrect.

Exam Alert:

The exam would probe you on multiple scenarios around competing options to migrate data from on-premises data centers to AWS Cloud. You should remember that a 1Gbps connection at full utilization can transfer approximately 10 TB of data in a day. You will see questions that tweak the available connection bandwidth or change the available utilization, so you just need to factor these changes into the above-mentioned unit rate to identify the correct answer.

Leverage S3 Transfer Acceleration to transfer the data to S3 - S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and your Amazon S3 bucket. S3 Transfer Acceleration leverages Amazon CloudFront’s globally distributed AWS Edge Locations.

You should note that S3 Transfer Acceleration over a fully-utilized 1 Gbps line can only transfer up to 75 TBs in a week's duration. So this option is not correct for the given use-case.

via - https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration

References:

https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration

---

## Câu 16 — ✅ ĐÚNG

### Câu hỏi

The product team at a global IoT technology company is looking to build features to facilitate better collaboration with the company's customers. As part of its research, the product team has figured out a market need to support both stateful and stateless client-server communications via the APIs developed using its platform.

You have been hired by the company as an AWS Certified Solutions Architect Professional to build a solution to fulfill this market need using AWS API Gateway. Which of the following would you recommend to the company?

### Các phương án

- **A.** API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server
- **B.** API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server
- **C.** API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server
- **D.** API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server 👈 *(bạn chọn)* ✅

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:
API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the front door for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications.

How API Gateway Works:

via - https://aws.amazon.com/api-gateway/

API Gateway creates RESTful APIs that:
Are HTTP-based.
Enable stateless client-server communication.
Implement standard HTTP methods such as GET, POST, PUT, PATCH, and DELETE.

API Gateway creates WebSocket APIs that:
Adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server.
Route incoming messages based on message content.

So API Gateway supports stateless RESTful APIs as well as stateful WebSocket APIs. Therefore this option is correct.

Incorrect options:
API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server

API Gateway creates RESTful APIs that enable stateless client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server

API Gateway creates RESTful APIs that enable stateful client-server communication and API Gateway also creates WebSocket APIs that adhere to the WebSocket protocol, which enables stateless, full-duplex communication between client and server

These three options contradict the earlier details provided in the explanation. To summarize, API Gateway supports stateless RESTful APIs and stateful WebSocket APIs. Hence these options are incorrect.

via - https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

Reference:

https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

---

## Câu 17 — ✅ ĐÚNG

### Câu hỏi

An e-commerce company is planning to migrate its IT infrastructure from the on-premises data center to AWS Cloud to ramp up its capabilities well in time for the upcoming Holiday Sale season. The company’s CTO has hired you as an AWS Certified Solutions Architect Professional to design a distributed, highly available and loosely coupled order processing application. The application is responsible for receiving and processing orders before storing them in a DynamoDB table. The application has seen sporadic traffic spikes in the past and the CTO wants the application to be able to scale during marketing campaigns to process the orders with minimal disruption.

Which of the following options would you recommend as the MOST reliable solution to address these requirements?

### Các phương án

- **A.** Ingest the orders in an SQS queue and trigger a Lambda function to process them 👈 *(bạn chọn)* ✅
- **B.** Ingest the orders via a Step Function state machine and trigger an ECS container to process them
- **C.** Push the orders to an SNS topic and subscribe a Lambda function to process them
- **D.** Push the orders to Kinesis Data Streams and use Amazon EC2 instances to process them

> **Bạn chọn:** A  
> **Đáp án đúng:** A  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Ingest the orders in an SQS queue and trigger a Lambda function to process them

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume. Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.

You can use an AWS Lambda function to process messages in an Amazon Simple Queue Service (Amazon SQS) queue. Lambda event source mappings support standard queues and first-in, first-out (FIFO) queues. With Amazon SQS, you can offload tasks from one component of your application by sending them to a queue and processing them asynchronously.

via - https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

AWS manages all ongoing operations and underlying infrastructure needed to provide a highly available and scalable message queuing service. With SQS, there is no upfront cost, no need to acquire, install, and configure messaging software, and no time-consuming build-out and maintenance of supporting infrastructure. SQS queues are dynamically created and scale automatically so you can build and grow applications quickly and efficiently.

Incorrect options:

Ingest the orders via a Step Function state machine and trigger an ECS container to process them - AWS Step Functions lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using Step Functions, you can design and run workflows that stitch together services such as AWS Lambda into feature-rich applications.

via - https://aws.amazon.com/step-functions/

You cannot use a Step Functions state machine to directly ingest incoming orders, so this option is incorrect.

Push the orders to Kinesis Data Streams and use Amazon EC2 instances to process them - You cannot use EC2 instances to process the orders because if the EC2 instances become unhealthy then the application would be unable to process the orders, thereby making the architecture unreliable.

Push the orders to an SNS topic and subscribe a Lambda function to process them - Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications. You cannot use SNS to facilitate reliable order processing workflow for the given use-case because once the Lambda function picks an order's message from the SNS topic, the order would remain unprocessed if the Lambda fails to process it successfully. In the case of SQS, the message will be available for re-processing after visibility timeout.

How SNS Works:

via - https://docs.aws.amazon.com/sns/latest/dg/welcome.html

References:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html

https://docs.aws.amazon.com/sns/latest/dg/welcome.html

---

## Câu 18 — ✅ ĐÚNG

### Câu hỏi

A social media company has a serverless application stack that consists of CloudFront, API Gateway and Lambda functions. The company has hired you as an AWS Certified Solutions Architect Professional to improve the current deployment process which creates a new version of the Lambda function and then runs an AWS CLI script for deployment. In case the new version errors out, then another CLI script is invoked to deploy the previous working version of the Lambda function. The company has mandated you to decrease the time to deploy new versions of the Lambda functions and also reduce the time to detect and rollback when errors are identified.

Which of the following solutions would you suggest for the given use-case?

### Các phương án

- **A.** Set up and deploy a CloudFormation stack containing a new API Gateway endpoint that points to the new Lambda version. Test the updated CloudFront origin that points to this new API Gateway endpoint and in case errors are detected then revert the CloudFront origin to the previous working API Gateway endpoint
- **B.** Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. Use pre-traffic and post-traffic test functions of the change set to verify the deployment. Rollback in case CloudWatch alarms are triggered
- **C.** Use Serverless Application Model (SAM) and leverage the built-in traffic-shifting feature of SAM to deploy the new Lambda version via CodeDeploy and use pre-traffic and post-traffic test functions to verify code. Rollback in case CloudWatch alarms are triggered 👈 *(bạn chọn)* ✅
- **D.** Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. In case the Lambda function errors out, rollback the CloudFormation change set to the previous version

> **Bạn chọn:** C  
> **Đáp án đúng:** C  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Use Serverless Application Model (SAM) and leverage the built-in traffic-shifting feature of SAM to deploy the new Lambda version via CodeDeploy and use pre-traffic and post-traffic test functions to verify code. Rollback in case CloudWatch alarms are triggered

The AWS Serverless Application Model (SAM) is an open source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. You define the application you want with just a few lines per resource and model it using YAML. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax. Then, CloudFormation provisions your resources with reliable deployment capabilities.

To address the given use-case, you can use the traffic shifting feature of SAM to easily test the new version of the Lambda function without having to manually move 100% of the traffic to the new version in one shot.

You can use CodeDeploy to create a deployment process that publishes the new Lambda version but does not send any traffic to it. Then it executes a PreTraffic test to ensure that your new function works as expected. After the test succeeds, CodeDeploy automatically shifts traffic gradually to the new version of the Lambda function. This workflow address one of the key requirements of reducing the time to detect errors. You can roll back to the previous version in case the new version errors out.

via - https://aws.amazon.com/blogs/compute/implementing-safe-aws-lambda-deployments-with-aws-codedeploy/

Incorrect options:

Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. In case the Lambda function errors out, rollback the CloudFormation change set to the previous version - You can use CloudFormation change sets to preview how proposed changes to a stack might impact your running resources, for example, whether your changes will delete or replace any critical resources, AWS CloudFormation makes the changes to your stack only when you decide to execute the change set, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another change set.

This option does not help in reducing the time to detect any potential deployment errors as you would not know about any potential failures until you actually deploy the stack.

via - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

Instead, you should use SAM to create your serverless application as it comes built-in with CodeDeploy to provide gradual Lambda deployments. Also, you can define pre-traffic and post-traffic test functions to verify that the newly deployed code is configured correctly and your application operates as expected. You can roll back the deployment if CloudWatch alarms are triggered.

Set up and deploy a CloudFormation stack containing a new API Gateway endpoint that points to the new Lambda version. Test the updated CloudFront origin that points to this new API Gateway endpoint and in case errors are detected then revert the CloudFront origin to the previous working API Gateway endpoint - This option does not help in reducing the time to detect any potential deployment errors as you would not know about any potential failures until you actually deploy the stack and point to the new endpoint.

Instead, you should use SAM to create your serverless application as it comes built-in with CodeDeploy to provide gradual Lambda deployments. Also, you can define pre-traffic and post-traffic test functions to verify that the newly deployed code is configured correctly and your application operates as expected. You can roll back the deployment if CloudWatch alarms are triggered.

Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. Use pre-traffic and post-traffic test functions of the change set to verify the deployment. Rollback in case CloudWatch alarms are triggered - This option has been added as a distractor, since CloudFormation change sets do not have pre-traffic and post-traffic test functions. Therefore this option is incorrect.

References:

https://aws.amazon.com/blogs/compute/implementing-safe-aws-lambda-deployments-with-aws-codedeploy/

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html

---

## Câu 19 — ✅ ĐÚNG

### Câu hỏi

A gaming company runs its flagship application with an SLA of 99.99%. Global users access the application 24/7. The application is currently hosted on the on-premises data centers and it routinely fails to meet its SLA, especially when hundreds of thousands of users access the application concurrently. The engineering team has also received complaints from some users about high latency.

As a Solutions Architect Professional, how would you redesign this application for scalability and also allow for automatic failover at the lowest possible cost?

### Các phương án

- **A.** Configure Route 53 geolocation-based routing to route to the nearest Region and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer
- **B.** Configure a combination of Route 53 failover routing with geolocation-based routing. Host the website behind an Application Load Balancer (ALB) with targets as EC2 instances that are automatically scaled via Auto-Scaling Group (ASG). Repeat this configuration of ALB with EC2 instances as targets that are scaled via ASG in multiple Regions. Use a Multi-AZ deployment with RDS MySQL as the data layer
- **C.** Configure Route 53 round-robin routing policy to distribute load evenly across all Regions and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer
- **D.** Configure Route 53 latency-based routing to route to the nearest Region and activate the health checks. Host the website on S3 in each Region and use API Gateway with AWS Lambda for the application layer. Set up the data layer using DynamoDB global tables with DAX for caching 👈 *(bạn chọn)* ✅

> **Bạn chọn:** D  
> **Đáp án đúng:** D  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct option:

Configure Route 53 latency-based routing to route to the nearest Region and activate the health checks. Host the website on S3 in each Region and use API Gateway with AWS Lambda for the application layer. Set up the data layer using DynamoDB global tables with DAX for caching

You can use Route 53 routing policies for a hosted zone record to determine how Amazon Route 53 responds to queries.

via - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

You can use a combination of alias records (such as latency alias, weighted alias or failover alias) and non-alias records to build a decision tree that gives you greater control over how Route 53 responds to requests. For example, you might use latency alias records to select a Region close to a user and use weighted records for two or more resources within each Region to protect against the failure of a single endpoint or an Availability Zone.

The following schematic shows how you can use a combination of latency routing policy (that has health checks activated) with a weighted routing policy to manage a multi-Region routing infrastructure. In case a Region goes down, Route 53 would look for the latency alias record with the next-best latency and choose the record for the other Region.

via - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html

Therefore, for the given use-case, this solution allows for automatic failover while minimizing the latency. As the downstream components for this solution such as the API Gateway, Lambda functions and DynamoDB global tables (with DAX) are serverless, so it allows the solution to scale easily.

Incorrect options:

Configure Route 53 geolocation-based routing to route to the nearest Region and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer - You cannot use geolocation-based routing to route to the nearest Region as you need to use latency based routing to accomplish that.

Geolocation routing is used when you want to route traffic based on the location of your users. When you use geolocation routing, you can localize your content and present some or all of your website in the language of your users. You can also use geolocation routing to restrict the distribution of content to only the locations in which you have distribution rights. Other components mentioned in the stack are not a deal-breaker, but using geolocation-based routing makes this option incorrect.

Configure Route 53 round-robin routing policy to distribute load evenly across all Regions and activate the health checks. Host the website behind a Network Load Balancer (NLB) with targets as ECS containers using Fargate. Repeat this configuration of NLB with ECS containers using Fargate in multiple Regions. Use Aurora Global database as the data layer - This option has been added as a distractor as there is no such thing as a Route 53 round-robin routing policy.

Configure a combination of Route 53 failover routing with geolocation-based routing. Host the website behind an Application Load Balancer (ALB) with targets as EC2 instances that are automatically scaled via Auto-Scaling Group (ASG). Repeat this configuration of ALB with EC2 instances as targets that are scaled via ASG in multiple Regions. Use a Multi-AZ deployment with RDS MySQL as the data layer - As mentioned earlier, you cannot use geolocation-based routing to route to the nearest Region as you need to use latency based routing to accomplish that. Failover routing could help with ensuring failover across AWS Regions, but using geolocation-based routing is a deal-breaker. Another red-flag is using Multi-AZ RDS MySQL as data layer, which can be deployed in just one AWS Region. You would need to develop and maintain custom data sync scripts/jobs to maintain data consistency across Regions.

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html

https://aws.amazon.com/premiumsupport/knowledge-center/route-53-dns-health-checks/

---

## Câu 20 — ❌ SAI

### Câu hỏi

An e-commerce company wants to rollout and test a blue-green deployment for its global application in the next couple of days. Most of the customers use mobile phones which are prone to DNS caching. The company has only two days left before the big sale will be launched.

As a Solutions Architect Professional, which of the following options would you suggest to test the deployment on as many users as possible in the given time frame?

### Các phương án

- **A.** Use Route 53 weighted routing to spread traffic across different deployments 👈 *(bạn chọn)*
- **B.** Use AWS CodeDeploy deployment options to choose the right deployment
- **C.** Use Elastic Load Balancer to distribute traffic across deployments
- **D.** Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment ✅

> **Bạn chọn:** A  
> **Đáp án đúng:** D  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

Blue/green deployment is a technique for releasing applications by shifting traffic between two identical environments running different versions of the application: "Blue" is the currently running version and "green" the new version. This type of deployment allows you to test features in the green environment without impacting the currently running version of your application. When you’re satisfied that the green version is working properly, you can gradually reroute the traffic from the old blue environment to the new green environment. Blue/green deployments can mitigate common risks associated with deploying software, such as downtime and rollback capability.

Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment - AWS Global Accelerator is a network layer service that directs traffic to optimal endpoints over the AWS global network, this improves the availability and performance of your internet applications. It provides two static anycast IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, such as your Application Load Balancers, Network Load Balancers, Elastic IP addresses or Amazon EC2 instances, in a single or in multiple AWS regions.

AWS Global Accelerator uses endpoint weights to determine the proportion of traffic that is directed to endpoints in an endpoint group, and traffic dials to control the percentage of traffic that is directed to an endpoint group (an AWS region where your application is deployed).

While relying on the DNS service is a great option for blue/green deployments, it may not fit use-cases that require a fast and controlled transition of the traffic. Some client devices and internet resolvers cache DNS answers for long periods; this DNS feature improves the efficiency of the DNS service as it reduces the DNS traffic across the Internet, and serves as a resiliency technique by preventing authoritative name-server overloads. The downside of this in blue/green deployments is that you don’t know how long it will take before all of your users receive updated IP addresses when you update a record, change your routing preference or when there is an application failure.

With AWS Global Accelerator, you can shift traffic gradually or all at once between the blue and the green environment and vice-versa without being subject to DNS caching on client devices and internet resolvers, traffic dials and endpoint weights changes are effective within seconds.

Incorrect options:

Use Route 53 weighted routing to spread traffic across different deployments - Weighted routing lets you associate multiple resources with a single domain name (example.com) or subdomain name (acme.example.com) and choose how much traffic is routed to each resource. This can be useful for a variety of purposes, including load balancing and testing new versions of the software. As discussed earlier, DNS caching is a negative behavior for this use case and hence Route 53 is not a good option.

Use Elastic Load Balancer to distribute traffic across deployments - An ELB can distribute traffic across healthy instances. You can also use the ALB weighted target groups feature for blue/green deployments as it does not rely on the DNS service. In addition you don’t need to create new ALBs for the green environment. As the use-case refers to a global application, so this option cannot be used for a multi-Region solution which is needed for the given requirement.

Use AWS CodeDeploy deployment options to choose the right deployment - In CodeDeploy, a deployment is the process, and the components involved in the process, of installing content on one or more instances. This content can consist of code, web and configuration files, executables, packages, scripts, and so on. CodeDeploy deploys content that is stored in a source repository, according to the configuration rules you specify. Blue/Green deployment is one of the deployment types that CodeDeploy supports. AWS CodeDeploy performs deployments with AWS resources located in the same region, so this option is ruled out.

References:

https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-global-accelerator-to-achieve-blue-green-deployments

https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted

---

## Câu 21 — ❌ SAI

### Câu hỏi

A mobile app based social media company is using Amazon CloudFront to deliver media-rich content to its audience across the world. The Content Delivery Network (CDN) offers a multi-tier cache by default, with regional edge caches that improve latency and lower the load on the origin servers when the object is not already cached at the edge. However, there are certain content types that bypass the regional edge cache and go directly to the origin.

Which of the following content types skip the regional edge cache? (Select two)

### Các phương án

- **A.** Static content such as style sheets, JavaScript files 👈 *(bạn chọn)*
- **B.** Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin ✅
- **C.** Dynamic content, as determined at request time (cache-behavior configured to forward all headers) ✅
- **D.** E-commerce assets such as product photos 👈 *(bạn chọn)*
- **E.** User-generated videos

> **Bạn chọn:** A, D  
> **Đáp án đúng:** B, C  
> **Kết quả:** ❌ Sai

### Giải thích

Correct options:

Dynamic content, as determined at request time (cache-behavior configured to forward all headers)

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.
CloudFront points of presence (POPs) (edge locations) make sure that popular content can be served quickly to your viewers. CloudFront also has regional edge caches that bring more of your content closer to your viewers, even when the content is not popular enough to stay at a POP, to help improve performance for that content.

Dynamic content, as determined at request time (cache-behavior configured to forward all headers), does not flow through regional edge caches, but goes directly to the origin. So this option is correct.

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin from the POPs and do not proxy through the regional edge caches. So this option is also correct.

How CloudFront works with regional edge caches:

via - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

Incorrect Options:

E-commerce assets such as product photos

User-generated videos

Static content such as style sheets, JavaScript files

The following type of content flows through the regional edge caches - user-generated content, such as video, photos, or artwork; e-commerce assets such as product photos and videos and static content such as style sheets, JavaScript files. Hence these three options are not correct.

Reference:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

---

## Câu 22 — ❌ SAI

### Câu hỏi

The DevOps team for a CRM SaaS company wants to implement a patching plan on AWS Cloud for a large mixed fleet of Windows and Linux servers. The patching plan has to be auditable and must be implemented securely to ensure compliance with the company's business requirements.

As a Solutions Architect Professional, which of the following options would you recommend to address these requirements with MINIMAL effort? (Select two)

### Các phương án

- **A.** Apply patch baselines using the AWS-RunPatchBaseline SSM document ✅
- **B.** Apply patch baselines using the AWS-ApplyPatchBaseline SSM document 👈 *(bạn chọn)*
- **C.** Set up an OS-native patching service to manage the update frequency and release approval for all instances. Set up AWS Config to provide audit and compliance reporting 👈 *(bạn chọn)*
- **D.** Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval ✅
- **E.** Configure OpsWorks automatic patching support for all applications which will keep the OS up-to-date following the initial installation. Set up AWS Config to provide audit and compliance reporting

> **Bạn chọn:** B, C  
> **Đáp án đúng:** A, D  
> **Kết quả:** ❌ Sai

### Giải thích

Correct options:

Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval

Apply patch baselines using the AWS-RunPatchBaseline SSM document

Systems Manager is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects. AWS Systems Manager Agent (SSM Agent) is Amazon software that can be installed and configured on an EC2 instance, an on-premises server, or a virtual machine (VM). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources.

via - https://aws.amazon.com/systems-manager/

You can use Patch Manager to apply patches for both operating systems and applications. (On Windows Server, application support is limited to updates for Microsoft applications). Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches individually or to large groups of instances by using Amazon EC2 tags.

For the given use-case, you can install patches on a regular basis by scheduling patching to run as a Systems Manager maintenance window task.

Systems Manager supports an SSM document for Patch Manager, AWS-RunPatchBaseline, which performs patching operations on instances for both security-related and other types of updates. When the document is run, it uses the patch baseline currently specified as the "default" for an operating system type.

The AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only and doesn't support Linux instances. For applying patch baselines to both Windows Server and Linux instances, the recommended SSM document is AWS-RunPatchBaseline.

via - https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

via - https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-differences.html

Incorrect options:

Configure OpsWorks automatic patching support for all applications which will keep the OS up-to-date following the initial installation. Set up AWS Config to provide audit and compliance reporting - AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments. You cannot use OpsWorks for automatic patch management, so this option is incorrect.

The part about using AWS Config is a distraction. AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - “What did my AWS resource look like at xyz point in time?”.

Set up an OS-native patching service to manage the update frequency and release approval for all instances. Set up AWS Config to provide audit and compliance reporting - You could use an OS-native patching service to manage the update frequency and release approval for all instances but it would take considerable effort to set up and configure this solution. This violates the minimal effort requirement of the given use-case.

Apply patch baselines using the AWS-ApplyPatchBaseline SSM document - As mentioned in the explanation above, the AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only and doesn't support Linux instances. For applying patch baselines to both Windows Server and Linux instances, the recommended SSM document is AWS-RunPatchBaseline.

References:

https://aws.amazon.com/systems-manager/

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-differences.html

---

## Câu 23 — ✅ ĐÚNG

### Câu hỏi

An analytics company wants to leverage ElastiCache for Redis in cluster mode to enhance the performance and scalability of its existing two-tier application architecture. The ElastiCache cluster is configured to listen on port 6379. The company has hired you as an AWS Certified Solutions Architect Professional to build a secure solution so that the cache data is secure and protected from unauthorized access.

Which of the following steps would address the given use-case? (Select three)

### Các phương án

- **A.** Configure the security group for the ElastiCache cluster with the required rules to allow inbound traffic from the cluster itself as well as from the cluster's clients on port 6379 👈 *(bạn chọn)* ✅
- **B.** Configure the ElastiCache cluster to have both in-transit as well as at-rest encryption 👈 *(bạn chọn)* ✅
- **C.** Enable CloudTrail to monitor the API Calls for the ElastiCache cluster
- **D.** Enable CloudWatch Logs to monitor the security credentials for the ElastiCache cluster
- **E.** Configure the security group for the ElastiCache cluster with the required rules to allow outbound traffic to the cluster's clients on port 6379
- **F.** Create the cluster with auth-token parameter and make sure that the parameter is included in all subsequent commands to the cluster 👈 *(bạn chọn)* ✅

> **Bạn chọn:** A, B, F  
> **Đáp án đúng:** A, B, F  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct options:

Configure the ElastiCache cluster to have both in-transit as well as at-rest encryption

You can use both in-transit as well as at-rest encryption to guard against unauthorized access of your data on the server. In-transit encryption encrypts your data whenever it is moving from one place to another, such as between nodes in your cluster or between your cluster and your application. At-rest encryption encrypts your on-disk data during sync and backup operations.

via - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/encryption.html

Create the cluster with auth-token parameter and make sure that the parameter is included in all subsequent commands to the cluster

Redis authentication tokens enable Redis to require a token (password) before allowing clients to run commands, thereby improving data security. You can require that users enter a token on a token-protected Redis server. You also need to include it in all subsequent commands to the replication group or cluster.

via - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html

Configure the security group for the ElastiCache cluster with the required rules to allow inbound traffic from the cluster itself as well as from the cluster's clients on port 6379

You can create a VPC security group to restrict access to the cluster instances. Configure rules that only allow inbound traffic from the cluster itself as well as from the cluster's clients on port 6379. Typically the ElastiCache cluster is accessed from the web servers running on EC2 instances. You can configure the security groups like so:

via - https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-vpc-accessing.html

Incorrect options:

Configure the security group for the ElastiCache cluster with the required rules to allow outbound traffic to the cluster's clients on port 6379 - As mentioned in the explanation above, you need to create a security group that allows inbound traffic from the cluster itself as well as from the cluster's clients on port 6379. Creating a security group rule that allows outbound traffic from the cluster on port 6379 is not relevant to the use-case.

Enable CloudWatch Logs to monitor the security credentials for the ElastiCache cluster

Enable CloudTrail to monitor the API Calls for the ElastiCache cluster

Both these options are added as distractors since both CloudWatch Logs and CloudTrail can be used for post-facto analysis to ascertain the series of access events relevant to the cluster. These options will not prevent unauthorized access.

References:

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/encryption.html

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-vpc-accessing.html

---

## Câu 24 — ❌ SAI

### Câu hỏi

A multi-national bank has recently migrated to AWS Cloud to utilize dedicated instances that are physically isolated at the host hardware level from instances that belong to other AWS accounts. The bank's flagship application is hosted on a fleet of EC2 instances which are part of an Auto Scaling group (ASG). The ASG uses a Launch Configuration (LC-A) with "dedicated" instance placement tenancy but the VPC (VPC-A) used by the Launch Configuration LC-A has the instance tenancy set to default. Later the engineering team creates a new Launch Configuration (LC-B) with "default" instance placement tenancy but the VPC (VPC-B) used by the Launch Configuration LC-B has the instance tenancy set to dedicated.

As a Solutions Architect Professional, which of the following options would you identify as correct regarding the instances launched via Launch Configuration LC-A and Launch Configuration LC-B?

### Các phương án

- **A.** The instances launched by Launch Configuration LC-A will have dedicated instance tenancy while the instances launched by the Launch Configuration LC-B will have default instance tenancy
- **B.** The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have default instance tenancy 👈 *(bạn chọn)*
- **C.** The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have dedicated instance tenancy ✅
- **D.** The instances launched by Launch Configuration LC-A will have default instance tenancy while the instances launched by the Launch Configuration LC-B will have dedicated instance tenancy

> **Bạn chọn:** B  
> **Đáp án đúng:** C  
> **Kết quả:** ❌ Sai

### Giải thích

Correct option:

The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have dedicated instance tenancy

A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances. When you create a launch configuration, you specify information for the instances. Include the ID of the Amazon Machine Image (AMI), the instance type, a key pair, one or more security groups, and a block device mapping. If you've launched an EC2 instance before, you specified the same information to launch the instance.

When you create a launch configuration, the default value for the instance placement tenancy is null and the instance tenancy is controlled by the tenancy attribute of the VPC.  If you set the Launch Configuration Tenancy to default and the VPC Tenancy is set to dedicated, then the instances have dedicated tenancy. If you set the Launch Configuration Tenancy to dedicated and the VPC Tenancy is set to default, then again the instances have dedicated tenancy.

Launch Configuration Tenancy vs VPC Tenancy

via - https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy

Incorrect options:

The instances launched by Launch Configuration LC-A will have dedicated instance tenancy while the instances launched by the Launch Configuration LC-B will have default instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

The instances launched by Launch Configuration LC-A will have default instance tenancy while the instances launched by the Launch Configuration LC-B will have dedicated instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have default instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy

---

## Câu 25 — ✅ ĐÚNG

### Câu hỏi

A digital media company wants to use AWS Cloudfront to manage its content. Firstly, it would like to allow only those new users who have paid the annual subscription fee the ability to download the application installation file. Secondly, only the subscribers should be able to view the files in the members' area.

As a Solutions Architect Professional, which of the following would you recommend as the MOST optimal solutions to deliver restricted content to the bona fide end users? (Select two)

### Các phương án

- **A.** Use CloudFront signed cookies to restrict access to all the files in the members' area of the website 👈 *(bạn chọn)* ✅
- **B.** Use CloudFront signed URLs to restrict access to the application installation file 👈 *(bạn chọn)* ✅
- **C.** Require HTTPS for communication between CloudFront and your S3 origin
- **D.** Use CloudFront signed cookies to restrict access to the application installation file
- **E.** Use CloudFront signed URLs to restrict access to all the files in the members' area of the website

> **Bạn chọn:** A, B  
> **Đáp án đúng:** A, B  
> **Kết quả:** ✅ Đúng

### Giải thích

Correct options:

Use CloudFront signed URLs to restrict access to the application installation file

Use CloudFront signed cookies to restrict access to all the files in the members' area of the website

Many companies that distribute content over the internet want to restrict access to documents, business data, media streams, or content that is intended for selected users, for example, users who have paid a fee.

To securely serve this private content by using CloudFront, you can do the following:

Require that your users access your private content by using special CloudFront signed URLs or signed cookies.

You should use a signed URL if you want to restrict access to individual files, for example, an installation download for your application. A signed URL includes additional information, for example, expiration date and time, that gives you more control over access to your content.

On the other hand, CloudFront signed cookies allow you to control who can access your content when you don't want to change your current URLs or when you want to provide access to multiple restricted files, for example, all of the files in the members' area of a website.

via - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-choosing-signed-urls-cookies.html

Incorrect options:

Use CloudFront signed cookies to restrict access to the application installation file

Use CloudFront signed URLs to restrict access to all the files in the members' area of the website

These two options contradict the description provided in the explanation above, so these options are incorrect.

Require HTTPS for communication between CloudFront and your S3 origin

Requiring HTTPS for communication between CloudFront and your custom origin (or S3 origin) only enables secure access to the underlying content. You cannot use HTTPS to restrict access to your private content. So this option is incorrect.

References:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-choosing-signed-urls-cookies.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.html

---

## Câu 26 — ❌ SAI

### Câu hỏi

An IT company wants to move all its clients belonging to the regulated and security-sensitive industries such as financial services and healthcare to the AWS Cloud as it wants to leverage the out-of-box security-specific capabilities offered by AWS. The Security team at the company is developing a framework to validate the adoption of AWS best practices and industry-recognized compliance standards. The AWS Management Console is the preferred method for the in-house teams wanting to provision resources. You have been hired as an AWS Certified Solutions Architect Professional to spearhead this strategic initiative.

Which of the following strategies would you adopt to address these business requirements for continuously assessing, auditing and monitoring the configurations of AWS resources? (Select two)

### Các phương án

- **A.** Leverage CloudTrail integration with SNS to automatically notify unauthorized API activities. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services. Use Lambda functions to automatically revert non-authorized changes in AWS resources 👈 *(bạn chọn)*
- **B.** Leverage EventBridge events near-real-time capabilities to monitor system events patterns to trigger Lambda functions to automatically revert non-authorized changes in AWS resources. Send notifications via SNS topics to improve the incidence response time
- **C.** Leverage Config rules to audit changes to AWS resources and monitor the compliance of the configuration by running the evaluations for the rule at a frequency that you choose. Develop AWS Config custom rules to establish a test-driven development approach by triggering the evaluation when any resource that matches the rule's scope changes in configuration 👈 *(bạn chọn)* ✅
- **D.** Enable trails and set up CloudTrail events to review and monitor management activities of all AWS accounts by logging these activities into CloudWatch Logs using a KMS key. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services ✅
- **E.** Leverage CloudWatch Logs agent to collect all the AWS SDK logs. Search the log data using a pre-defined set of filter patterns that match mutating API calls. Use CloudWatch alarms to send notifications via SNS when unintended changes are performed. Archive log data by using a batch export to Amazon S3 and analyze via Athena

> **Bạn chọn:** A, C  
> **Đáp án đúng:** C, D  
> **Kết quả:** ❌ Sai

### Giải thích

Correct options:

Leverage Config rules to audit changes to AWS resources and monitor the compliance of the configuration by running the evaluations for the rule at a frequency that you choose. Develop AWS Config custom rules to establish a test-driven development approach by triggering the evaluation when any resource that matches the rule's scope changes in configuration

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - “What did my AWS resource look like at xyz point in time?”.

How AWS Config Works:

via - https://aws.amazon.com/config/

For the given use-case, you can use AWS Config to evaluate the configuration settings of your AWS resources. You do this by creating AWS Config rules, which represent your ideal configuration settings. AWS Config provides customizable, predefined rules called managed rules to help you get started. You can also create your own custom rules. While AWS Config continuously tracks the configuration changes that occur among your resources, it checks whether these changes violate any of the conditions in your rules. If a resource violates a rule, AWS Config flags the resource and marks the rule as noncompliant.

There are two types of evaluation trigger types for Config rules:

Configuration changes – AWS Config triggers the evaluation when any resource that matches the rule's scope changes in configuration. The evaluation runs after AWS Config sends a configuration item change notification.

Periodic – AWS Config runs evaluations for the rule at a frequency that you choose (for example, every 24 hours).

Enable trails and set up CloudTrail events to review and monitor management activities of all AWS accounts by logging these activities into CloudWatch Logs using a KMS key. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services

CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. An event in CloudTrail is the record of activity in an AWS account. This activity can be an action taken by a user, role, or service that is monitorable by CloudTrail. CloudTrail events provide a history of both API and non-API account activity made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.

CloudTrail data events are disabled by default. You can enable logging at an additional cost. Data events are also known as data plane operations and are often high-volume activities. Data events aren't viewable in CloudTrail event history and are charged for all copies at a reduced rate compared to management events.

CloudTrail records management events for the last 90 days free of charge, and are viewable in the Event History with the CloudTrail console. For Amazon S3 delivery of CloudTrail events, the first copy delivered is free. Additional copies of management events are charged.

via - https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

Incorrect options:

Leverage CloudWatch Logs agent to collect all the AWS SDK logs. Search the log data using a pre-defined set of filter patterns that match mutating API calls. Use CloudWatch alarms to send notifications via SNS when unintended changes are performed. Archive log data by using a batch export to Amazon S3 and analyze via Athena - One of the key constraints for the given scenario is that the AWS Management Console is the preferred method for the in-house teams wanting to provision resources. Although this option is technically feasible, but it focuses on using CloudWatch Logs agent to collect all the AWS SDK logs. The given use-case has no specific requirements for AWS SDKs or AWS APIs because AWS Management Console is the preferred method to provision resources. So this option is not the best fit solution.

Leverage CloudTrail integration with SNS to automatically notify unauthorized API activities. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services. Use Lambda functions to automatically revert non-authorized changes in AWS resources - One of the key constraints for the given scenario is that the AWS Management Console is the preferred method for the in-house teams wanting to provision resources. Although this option is technically feasible, but it focuses on capturing unauthorized API activities. The given use-case has no specific requirements for AWS SDKs or AWS APIs because AWS Management Console is the preferred method to provision resources. In addition, the use-case just talks about assessing, auditing and monitoring the configurations of AWS resources. Reverting non-authorized changes in AWS resources is not part of the mandate. So this option is not correct.

Leverage EventBridge events near-real-time capabilities to monitor system events patterns to trigger Lambda functions to automatically revert non-authorized changes in AWS resources. Send notifications via SNS topics to improve the incidence response time - The use-case just talks about assessing, auditing and monitoring the configurations of AWS resources. Reverting non-authorized changes in AWS resources is not part of the mandate. So this option is not correct.

References:

https://aws.amazon.com/config/

https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_manage-rules.html

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

---

## Câu 27 — ❌ SAI

### Câu hỏi

The engineering team at a retail company has deployed a fleet of EC2 instances under an Auto Scaling group (ASG). The instances under the ASG span two Availability Zones (AZ) within the eu-west-1 region. All the incoming requests are handled by an Application Load Balancer (ALB) that routes the requests to the EC2 instances under the ASG. A planned migration went wrong last week when two instances (belonging to AZ 1) were manually terminated and desired capacity was reduced causing the Availability Zones to become unbalanced. Later that day, another instance (belonging to AZ 2) was detected as unhealthy by the Application Load Balancer's health check.

Which of the following options represent the correct outcomes for the aforesaid events? (Select two)

### Các phương án

- **A.** Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance ✅
- **B.** Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously 👈 *(bạn chọn)*
- **C.** As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched
- **D.** Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it
- **E.** As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application 👈 *(bạn chọn)* ✅

> **Bạn chọn:** B, E  
> **Đáp án đúng:** A, E  
> **Kết quả:** ❌ Sai

### Giải thích

Correct options:

As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application

Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. You create collections of EC2 instances, called Auto Scaling groups. You can specify the minimum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below this size.

Actions such as changing the Availability Zones for your group or explicitly terminating or detaching instances and decrement the desired capacity at the same time, it can lead to the Auto Scaling group becoming unbalanced between Availability Zones. Amazon EC2 Auto Scaling compensates by rebalancing the Availability Zones.

When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application. Therefore, this option is correct.

Availability Zone Rebalancing Overview:

via - https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html

Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance

However, the scaling activity of Auto Scaling works in a different sequence compared to the rebalancing activity. Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance.

Incorrect options:

Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it - This option contradicts the correct sequence of events outlined earlier for scaling activity created by EC2 Auto Scaling. Actually, Auto Scaling first terminates the unhealthy instance and then launches a new instance. Hence this is incorrect.

As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched - This option contradicts the correct sequence of events outlined earlier for rebalancing activity. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones. Hence this is incorrect.

Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously - This is a made-up option as both the terminate and launch activities can't happen simultaneously. This option has been added as a distractor.

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/common-scenarios-termination.html#common-scenarios-termination-rebalancing

https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-unhealthy-instance.html

---
