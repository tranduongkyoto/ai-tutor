# TD Set 3 (timed) — Correct Answer Review (42 questions)

Source: `TutorialsDojo_SAP_Timed_Mode_Set_3.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/⚠️/🧠 are study notes. Wrong answers: `td_set_3_review.md`.

## Purpose

Confirm each correct answer was **knowledge, not a guess**. Answer again without looking; if you can't justify why every wrong option fails, tick **Guessed** and treat it as a wrong answer.

## ⚠️ Inconsistent concepts (right here, wrong elsewhere in this test)

| Right | Wrong | Concept |
|---|---|---|
| Q21, Q22, Q27 | Q24 | SQS as a write buffer in front of a slow/throttled DB |
| Q40 | Q30 | ElastiCache to cut DB load and latency |
| Q66 | Q61 | Systems Manager Patch Manager for OS patching |
| Q3 | Q14 | Storage Gateway type: tape backup → Tape Gateway; process the content → File Gateway |
| Q52 | Q17, Q6 | EC2 → S3 access via IAM role (temporary credentials) |
| Q73, Q74 | Q57 | Federation/third party → STS temporary credentials, never long-term keys |
| Q59 | Q75 | How SCPs behave (deny vs allow-list) |
| Q31 | Q7 | X-Ray for end-to-end tracing |
| Q54, Q56 | Q53 | Zero-downtime deployment (blue/green, immutable) |
| Q15, Q43 | Q16 | Cross-Region DR sized to the RTO |

These are partial knowledge — review each pair together.

## Tracker

| Group | Q | Guessed? | Pass 1 | Pass 2 |
|---|---|---|---|---|
| A | [Q21](#q21) | ☐ | ☐ | ☐ |
| A | [Q22](#q22) | ☐ | ☐ | ☐ |
| A | [Q27](#q27) | ☐ | ☐ | ☐ |
| A | [Q40](#q40) | ☐ | ☐ | ☐ |
| A | [Q44](#q44) | ☐ | ☐ | ☐ |
| A | [Q62](#q62) | ☐ | ☐ | ☐ |
| B | [Q9](#q9) | ☐ | ☐ | ☐ |
| B | [Q18](#q18) | ☐ | ☐ | ☐ |
| B | [Q35](#q35) | ☐ | ☐ | ☐ |
| B | [Q41](#q41) | ☐ | ☐ | ☐ |
| B | [Q52](#q52) | ☐ | ☐ | ☐ |
| B | [Q64](#q64) | ☐ | ☐ | ☐ |
| B | [Q73](#q73) | ☐ | ☐ | ☐ |
| B | [Q74](#q74) | ☐ | ☐ | ☐ |
| C | [Q34](#q34) | ☐ | ☐ | ☐ |
| C | [Q59](#q59) | ☐ | ☐ | ☐ |
| C | [Q66](#q66) | ☐ | ☐ | ☐ |
| C | [Q68](#q68) | ☐ | ☐ | ☐ |
| C | [Q69](#q69) | ☐ | ☐ | ☐ |
| C | [Q70](#q70) | ☐ | ☐ | ☐ |
| D | [Q15](#q15) | ☐ | ☐ | ☐ |
| D | [Q33](#q33) | ☐ | ☐ | ☐ |
| D | [Q38](#q38) | ☐ | ☐ | ☐ |
| D | [Q43](#q43) | ☐ | ☐ | ☐ |
| D | [Q51](#q51) | ☐ | ☐ | ☐ |
| D | [Q65](#q65) | ☐ | ☐ | ☐ |
| E | [Q31](#q31) | ☐ | ☐ | ☐ |
| E | [Q46](#q46) | ☐ | ☐ | ☐ |
| E | [Q54](#q54) | ☐ | ☐ | ☐ |
| E | [Q56](#q56) | ☐ | ☐ | ☐ |
| E | [Q67](#q67) | ☐ | ☐ | ☐ |
| F | [Q2](#q2) | ☐ | ☐ | ☐ |
| F | [Q3](#q3) | ☐ | ☐ | ☐ |
| F | [Q4](#q4) | ☐ | ☐ | ☐ |
| F | [Q5](#q5) | ☐ | ☐ | ☐ |
| F | [Q39](#q39) | ☐ | ☐ | ☐ |
| F | [Q47](#q47) | ☐ | ☐ | ☐ |
| G | [Q11](#q11) | ☐ | ☐ | ☐ |
| G | [Q12](#q12) | ☐ | ☐ | ☐ |
| G | [Q25](#q25) | ☐ | ☐ | ☐ |
| G | [Q36](#q36) | ☐ | ☐ | ☐ |
| G | [Q49](#q49) | ☐ | ☐ | ☐ |

---

# Group A — Decouple & cache (6)

<a id="q21"></a>

## Q21

A company has scheduled to launch a promotional sale on its e-commerce platform. The company’s web application is hosted on a fleet of Amazon EC2 instances in an Auto Scaling group. The database tier is hosted on an Amazon RDS for PostgreSQL DB instance. This is a large event so the management expects a sudden spike and unpredictable user traffic for the duration of the event. New users are also expected to register and participate in the event so there will be a lot of database writes during the event. The Solutions Architect has been tasked to create a solution that will ensure all submissions are committed to the database without changing the underlying data model.

Which of the following options is the recommended solution for this scenario?

- **A.** To minimize any changes on the application or the current infrastructure, manually scale the current DB instance to a significantly larger instance size before the event. Choose a larger instance size depending on the anticipated user traffic, and scale down after the event is completed.
- **B.** Decouple the application and database tier by creating an Amazon SQS queue between them. Create an AWS Lambda function that picks up the messages on the SQS queue and writes them into the database.
- **C.** Instead of using Amazon RDS, migrate the database to an Amazon DynamoDB table instead. Utilize the built-in automatic scaling in DynamoDB to scale the database based on user traffic.
- **D.** Create an Amazon ElastiCache for Memcached cluster between the application and database tier. The cache will temporarily store the user submissions until the database is able to commit those entries.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** bursty writes, no change to data model

⚠️ **Watch:** Same idea as Q24 (missed) — SQS buffers writes

🧠 **Rule:** Spiky writes to RDS → SQS + Lambda consumer

### TD explanation

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message oriented middleware and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.
Use Amazon SQS to transmit any volume of data, at any level of throughput, without losing messages or requiring other services to be available. SQS lets you decouple application components so that they run and fail independently, increasing the overall fault tolerance of the system. Multiple copies of every message are stored redundantly across multiple availability zones so that they are available whenever needed.
Amazon SQS leverages the AWS cloud to dynamically scale based on demand. SQS scales elastically with your application so you don’t have to worry about capacity planning and pre-provisioning. There is no limit to the number of messages per queue, and standard queues provide nearly unlimited throughput.
You can use Amazon Simple Queue Service (SQS) to trigger AWS Lambda functions. Lambda functions can act as message consumers. Message consumers are processes that make the ReceiveMessage API call on SQS. Messages from queues can be processed either in batch or as a single message at a time. Each approach has its advantages and disadvantages.
- Batch processing: This is where each message can be processed independently, and an error on a single message is not required to disrupt the entire batch. Batch processing provides the most throughput for processing, and also provides the most optimizations for resources involved in reading messages.
- Single message processing: Single message processing is commonly used in scenarios where each message may trigger multiple processes within the consumer. In case of errors, the retry is confined to the single message.

Therefore, the correct answer is: Decouple the application and database tier by creating an Amazon SQS queue between them. Create an AWS Lambda function that picks up the messages on the SQS queue and writes them into the database. This is an excellent scenario for which Amazon SQS is designed for. The SQS queue can scale reliably to hold user submissions to ensure they will be written to the database. The SQS queue is highly durable which ensures that you will not lose any submissions.
The option that says: To minimize any changes on the application or the current infrastructure, manually scale the current DB instance to a significantly larger instance size before the event. Choose a larger instance size depending on the anticipated user traffic, and scale down after the event is completed is incorrect. There is no mention in the question if the database is Multi-AZ configuration. If Multi-AZ is not enabled, this will result in a brief downtime as the database is being scaled up or down. Additionally, since the user traffic is unpredictable, there is no guarantee the larger instance can handle the user traffic.
The option that says: Instead of using Amazon RDS, migrate the database to an Amazon DynamoDB table instead. Utilize the built-in automatic scaling in DynamoDB to scale the database based on user traffic is incorrect. This is not recommended for the scenario as changing the database requires major changes in the application and database layers.
The option that says: Create an Amazon ElastiCache for Memcached cluster between the application and database tier. The cache will temporarily store the user submissions until the database is able to commit those entries is incorrect. Amazon ElastiCache is designed for caching frequent requests to the database and not for holding data that is waiting to be written to the database.

References:
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
https://aws.amazon.com/blogs/architecture/application-integration-using-queues-and-messages/
https://aws.amazon.com/sqs/faqs/

Check out the Amazon SQS Cheat Sheet:
https://tutorialsdojo.com/amazon-sqs/

</details>

<a id="q22"></a>

## Q22

A medical firm uses an image analysis application that extracts data from multiple images. The input stream analyzes a batch of images and for each file, it writes the result data to an output stream of files. The number of input files per day grows and peaks for a few hours in a day. The application is hosted on an Amazon EC2 instance with a large EBS volume that hosts the input data, but the results still take almost 20 hours per day to be processed.

Which of the following solutions can be implemented to reduce the processing time and improve the availability of the application?

- **A.** Store I/O files in an EBS Provisioned IOPS volume, and use SNS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the number of SNS notifications.
- **B.** Store I/O files in S3 instead and use SQS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the length of your SQS queue.
- **C.** Store I/O files in an EBS Provisioned IOPS volume, and use SNS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the length of your SQS queue.
- **D.** Store I/O files in S3 instead and use SQS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the number of SNS notifications.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** growing input files, availability, processing time

⚠️ **Watch:** Don't pick bigger instances; scale out on queue length

🧠 **Rule:** Batch file processing → S3 for I/O + SQS + ASG on queue depth

### TD explanation

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications. Building applications from individual components that each perform a discrete function improves scalability and reliability, and is best practice design for modern applications. SQS makes it simple and cost-effective to decouple and coordinate the components of a cloud application. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be always available.

Therefore, the correct answer is: Store I/O files in S3 instead and use SQS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the length of your SQS queue. It provides high availability and can store the massive amount of data. Auto-scaling of EC2 instances reduces the overall processing time and SQS helps in distributing the commands/tasks to the group of EC2 instances.
The option that says: Store I/O files in an EBS Provisioned IOPS volume, and use SNS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the number of SNS notifications is incorrect because EBS is for storage and SNS is only for notification, not for scaling.
The option that says: Store I/O files in an EBS Provisioned IOPS volume, and use SNS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the length of your SQS queue is incorrect because EBS is only for block storage and not for scaling.
The option that says: Store I/O files in S3 instead and use SQS to facilitate a group of hosts working in parallel. Include the hosts in an auto scaling group that scales accordingly to the number of SNS notifications is incorrect because SNS is only for notification and not for scaling.
References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html
https://aws.amazon.com/blogs/aws/auto-scaling-with-sqs/

Check out these AWS Auto Scaling and Amazon SQS Cheat Sheets:
https://tutorialsdojo.com/aws-auto-scaling/
https://tutorialsdojo.com/amazon-sqs/

</details>

<a id="q27"></a>

## Q27

A company recently developed a web application that processes customer behavioral data and stores the results in a DynamoDB table. The application is expected to receive a high usage load. To ensure that data is not lost when DynamoDB write requests are throttled, the solutions architect must reduce the load taken by the table.

Which of the following is the MOST cost-effective strategy for reducing the load on the DynamoDB table?

- **A.** Replicate the DynamoDB table to another AWS region using global tables.
- **B.** Provision higher write-capacity units (WCUs) to your DynamoDB table.
- **C.** Provision more DynamoDB tables to absorb the load.
- **D.** Use an SQS queue to decouple messages from the application and the database.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** DynamoDB throttled writes, data not lost, MOST cost-effective

⚠️ **Watch:** Raising WCU works but costs more

🧠 **Rule:** Throttled writes → SQS in front of DynamoDB

### TD explanation

Queuing is a commonly used solution for separating computation components in a distributed processing system. It is a form of the asynchronous communication system used in serverless and microservices architectures. Messages wait in a queue for processing, and leave the queue when received by a single consumer.
Amazon Simple Queue Service (Amazon SQS) is a scalable message queuing system that stores messages as they travel between various components of your application architecture. Amazon SQS enables web service applications to quickly and reliably queue messages that are generated by one component and consumed by another component. A queue is a temporary repository for messages that are awaiting processing.
In the below diagram, the goal is to smooth out the traffic from the application, so that the load process into DynamoDB is much more consistent. The key service used to achieve this is Amazon SQS, which holds all the items until a loader process stores the data in DynamoDB. The architecture looks like this:

Therefore, the correct answer is: Use an SQS queue to decouple messages from the application and the database. Data can be lost if the application fails to store it in DynamoDB due to throttling. Amazon SQS can reduce the load by temporarily holding the data until the DynamoDB throttling subsides. It is scalable as well as cost-efficient.
The option that says: Replicate the DynamoDB table to another AWS region using global tables is incorrect. The global table is a DynamoDB feature that is primarily used for applications requiring multi-region fault tolerance. It won't reduce the load on the existing DynamoDB table.
The option that says: Provision higher write-capacity units (WCUs) to your DynamoDB table is incorrect because increasing the write capacity is an expensive option.
The option that says: Provision more DynamoDB tables to absorb the load is incorrect. While it is possible to create another table for the application to use, it is an anti-pattern and will require a lot of development overhead to keep the data from the tables in sync, not to mention when joining queries. Remember that JOIN operations are not possible in DynamoDB so you need to implement this at the application level. Furthermore, this is not a cost-efficient solution.

References:
https://aws.amazon.com/sqs/
https://aws.amazon.com/blogs/compute/creating-a-scalable-serverless-import-process-for-amazon-dynamodb/
https://aws.amazon.com/blogs/database/implementing-priority-queueing-with-amazon-dynamodb/

Check out this Amazon SQS Cheat Sheet:
https://tutorialsdojo.com/amazon-sqs/

</details>

<a id="q40"></a>

## Q40

A company runs a live flight tracking service hosted on the AWS cloud. The application gets updated every 10 minutes with the latest flight information from every airline. The tracking website has a global audience and uses an Auto Scaling group behind an Elastic Load Balancer and an Amazon RDS database. A simple web interface is hosted as static content on an Amazon S3 bucket. The Auto Scaling group is set to trigger a scale-up event at 90% CPU utilization. The average load time of the web page is around 7 seconds but the management wants to bring it down to less than 3 seconds.

Which combination of options will make the page load time faster in the MOST cost-effective way? (Select TWO.)

- **A.** Add a caching layer using Amazon ElastiCache Service to be used for storing sessions and frequent DB queries.
- **B.** Scale more frequently by setting the scale up trigger of the Auto Scaling group to 30%.
- **C.** Have CloudFront enable caching of re-usable content from your website.
- **D.** Create a second installation in another region, and utilize Amazon Route 53's latency-based routing feature to direct requests to the appropriate region.
- **E.** Replace your existing Auto Scaling group with the AWS Systems Manager State Manager which provides a more effective way to manage and scale your EC2 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C (you answered correctly)

🔑 **Key words:** page load < 3 s, global audience, MOST cost-effective

⚠️ **Watch:** Same idea as Q30 (missed) — ElastiCache cuts DB latency

🧠 **Rule:** Slow pages → ElastiCache for sessions/queries + CloudFront for reusable content

### TD explanation

You can use a content delivery network (CDN) like Amazon CloudFront to improve the performance of your website by securely delivering data, videos, applications, and APIs to customers globally with low latency and high transfer speeds. To improve performance, you can simply configure your website’s traffic to be delivered over CloudFront’s globally distributed edge network by setting up a CloudFront distribution. In addition, CloudFront offers a variety of optimization options.
Amazon ElastiCache allows you to seamlessly set up, run, and scale popular open-source compatible in-memory data stores in the cloud. Build data-intensive apps or boost the performance of your existing databases by retrieving data from high throughput and low latency in-memory data stores. Both Redis and MemCached are in-memory, open-source data stores. Memcached, a high-performance distributed memory cache service, is designed for simplicity while Redis offers a rich set of features that make it effective for a wide range of use cases.
In this scenario, you can improve the page load times of your application by using a combination of Amazon ElastiCache, CloudFront, or alternatively, an upgraded RDS instance to increase the read capacity.

The option that says: Add a caching layer using Amazon ElastiCache Service to be used for storing sessions and frequent DB queries is correct. This uses ElastiCache for storing sessions as well as frequent DB queries hence, reducing the load on the database. This should help increase the read performance.
The option that says: Having CloudFront enable caching of re-usable content from your website is correct. This uses CloudFront which is a network of globally distributed edge-locations that caches the content and improves the user experience.
The option that says: Scale more frequently by setting the scale up trigger of the Auto Scaling group to 30% is incorrect. This will increase the number of web server instances but will not reduce the load on the database and hence, will not improve the read performance.
The option that says: Create a second installation in another region, and utilize Amazon Route 53's latency-based routing feature to direct requests to the appropriate region is incorrect. This will not improve read performance. In fact, this setup would add to the cost.
The option that says: Replace your existing Auto Scaling group with the AWS Systems Manager State Manager which provides a more effective way to manage and scale your EC2 instances is incorrect. The AWS Systems Manager State Manager is a secure and scalable service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define. It is not a suitable solution to improve the load times of your web application. This is primarily used to control the configuration detail of your instances in your VPC as well as your servers located in your on-premises data centers, such as server configurations, anti-virus definitions, firewall settings, and many others.

References:
https://aws.amazon.com/elasticache/
https://aws.amazon.com/cloudfront/dynamic-content/
https://aws.amazon.com/blogs/networking-and-content-delivery/improve-your-website-performance-with-amazon-cloudfront/

Check out these Amazon CloudFront, Amazon ElastiCache, and Amazon RDS Cheat Sheets:
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/amazon-elasticache/
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q44"></a>

## Q44

A company plans to release a public beta of its new video game. The release package is approximately 5GB in size. Based on previous releases and community feedback, millions of users from around the world are expected to download the new game. Currently, the company has a Linux-based website that lists the files which are hosted on its on-premises data center. Public Internet users are able to download the game via the website. However, the company wants a new solution that is cost-effective and will allow faster download performance for its users regardless of their location.

Which of the following options is the recommended solution to meet the company’s requirements?

- **A.** Host the service on an Auto Scaling group of Amazon EC2 instances. Save the game files on the mounted Amazon EBS volumes on each instance. Place the Auto Scaling group behind an Application Load Balancer. Create an Amazon Route 53 entry pointing to the ALB. Publish the Route 53 entry as the download URL to allow users to download the game package.
- **B.** Host the service on an Auto Scaling group of Amazon EC2 instances. Save the game files on the mounted Amazon EFS volume on each instance. Place the Auto Scaling group behind a Network Load Balancer. Create an Amazon Route 53 entry pointing to the NLB. Publish the Route 53 entry as the download URL to allow users to download the game package.
- **C.** Create an Amazon S3 bucket with website hosting enabled and upload the game package on it. Create an Amazon CloudFront distribution with the S3 bucket as the origin. Create an Amazon Route 53 entry pointing to the CloudFront distribution. Publish the Route 53 entry as the download URL to allow users to download the game package.
- **D.** Create an Amazon S3 bucket with website hosting enabled and upload the game package on it. To improve cost-effectiveness, enable the “Requestor Pays” option for the S3 bucket. Create an Amazon Route 53 entry pointing to the S3 bucket. Publish the Route 53 entry as the download URL to allow users to download the game package.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** 5 GB file, millions of global downloads

⚠️ **Watch:** Not EC2/EFS behind ALB

🧠 **Rule:** Large global downloads → S3 + CloudFront + Route 53

### TD explanation

You can use Amazon S3 to host a static website. Hosting a static website on Amazon S3 delivers a highly performant and scalable website at a fraction of the cost of a traditional web server. To host a static website on Amazon S3, configure an Amazon S3 bucket for website hosting and upload your website content. Using the AWS Management Console, you can configure your Amazon S3 bucket as a static website without writing any code. Depending on your website requirements, you can also use some optional configurations, including redirects, web traffic logging, and custom error documents.
When you configure a bucket as a static website, you must enable static website hosting, configure an index document, and set permissions.
You can use Amazon CloudFront to improve the performance of your Amazon S3 website. CloudFront makes your website files (such as HTML, images, and video) available from data centers around the world (known as edge locations). When a visitor requests a file from your website, CloudFront automatically redirects the request to a copy of the file at the nearest edge location. This results in faster download times than if the visitor had requested the content from a data center that is located farther away.
CloudFront caches content at edge locations for a period of time that you specify. If a visitor requests content that has been cached for longer than the expiration date, CloudFront checks the origin server to see if a newer version of the content is available. If a newer version is available, CloudFront copies the new version to the edge location. Changes that you make to the original content are replicated to edge locations as visitors request the content.

To serve a static website hosted on Amazon S3, you can deploy a CloudFront distribution using one of these configurations:
- Using a REST API endpoint as the origin, with access restricted by an origin access control (OAC)
- Using a website endpoint as the origin, with anonymous (public) access allowed. It allows public users to download files.
- Using a website endpoint as the origin, with access restricted by a Referer header
- Using AWS CloudFormation to deploy a REST API endpoint as the origin, with access restricted by an OAC and a custom domain pointing to CloudFront
Hence, the correct answer is: Create an Amazon S3 bucket with website hosting enabled and upload the game package on it. Create an Amazon CloudFront distribution with the S3 bucket as the origin. Create an Amazon Route 53 entry pointing to the CloudFront distribution. Publish the Route 53 entry as the download URL to allow users to download the game package. Storing the game package on an Amazon S3 bucket is very cost-effective. Using CloudFront will ensure that users will have a consistently high download performance regardless of their location.
The option that says: Host the service on an Auto Scaling group of Amazon EC2 instances. Save the game files on the mounted Amazon EBS volumes on each instance. Place the Auto Scaling group behind an Application Load Balancer. Create an Amazon Route 53 entry pointing to the ALB. Publish the Route 53 entry as the download URL to allow users to download the game package is incorrect. This is possible but very expensive as you have to attach EBS volumes to each instance. Additionally, this is limited to only one region. Other users from around the world may experience a slower download speed.
The option that says: Host the service on an Auto Scaling group of Amazon EC2 instances. Save the game files on the mounted Amazon EFS volume on each instance. Place the Auto Scaling group behind a Network Load Balancer. Create an Amazon Route 53 entry pointing to the NLB. Publish the Route 53 entry as the download URL to allow users to download the game package is incorrect. This is not recommended because using EFS is typically more expensive than using an S3 bucket. A Network Load Balancer is also very expensive.
The option that says: Create an Amazon S3 bucket with website hosting enabled and upload the game package on it. To improve cost-effectiveness, enable the “Requestor Pays” option for the S3 bucket. Create an Amazon Route 53 entry pointing to the S3 bucket. Publish the Route 53 entry as the download URL to allow users to download the game package is incorrect. This is not possible because the users will need their own AWS accounts in order to download an object from a bucket that has "Requestor Pays" enabled.

References:
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html
https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/

Check out these Amazon S3 and Amazon CloudFront Cheat Sheets:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q62"></a>

## Q62

A company has a multi-tier web application hosted in AWS. It leverages Amazon CloudFront to reliably scale and quickly serve requests from users around the world. After several months in operation, the company received user complaints of slow response time from the web application. The monitoring team reported that the CloudFront cache hit ratio metric is steadily dropping for the past months. This metric indicates that there are inconsistent query strings on user requests and queries that contain upper-case or mixed-case letters. These requests cause CloudFront to send unnecessary origin queries.

Which of the following actions will increase the cache hit ratio of the CloudFront distribution?

- **A.** Write a Lamda@Edge function that will normalize the query parameters by sorting them in alphabetical order and converting them into lower case. Deploy this function with the CloudFront distribution and set “viewer request” as the trigger to invoke the function.
- **B.** Reconfigure the CloudFront distribution to remove the caching behavior based on query string parameters. This will cache the requests regardless of the order or case of the query parameters.
- **C.** Launch a reverse proxy inside the application VPC to intercept the requests going to the origin instances. Process the query parameters to sort them by name and convert them to lowercase letters before forwarding them to the instances.
- **D.** Reconfigure the CloudFront distribution to ensure that the “case insensitive” option is enabled for processing query string parameters.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** query strings in different order/case, cache hit ratio

⚠️ **Watch:** Not more TTL or more origins

🧠 **Rule:** Normalize query strings with Lambda@Edge on viewer request

### TD explanation

For each query string parameter that your web application forwards to CloudFront, CloudFront forwards requests to your origin for every parameter value and caches a separate version of the object for every parameter value. This is true even if your origin always returns the same object regardless of the parameter value. For multiple parameters, the number of requests and the number of objects multiply. For example, if requests for an object include two parameters that each have three different values, CloudFront caches six versions of that object. AWS recommends that you configure CloudFront to cache based only on the query string parameters for which your origin returns different versions, and that you carefully consider the merits of caching based on each parameter.
If you configure CloudFront to cache based on query string parameters, you can improve caching if you do the following:
- Configure CloudFront to forward only the query string parameters for which your origin will return unique objects.
- Use the same case (uppercase or lowercase) for all instances of the same parameter. For example, if one request contains parameter1=A and another contains parameter1=a, CloudFront forwards separate requests to your origin when a request contains parameter1=A and when a request contains parameter1=a. CloudFront then separately caches the corresponding objects returned by your origin separately even if the objects are identical. If you use just A or a, CloudFront forwards fewer requests to your origin.
- List parameters in the same order. As with differences in case, if one request for an object contains the query string parameter1=a&parameter2=b and another request for the same object contains parameter2=b&parameter1=a, CloudFront forwards both requests to your origin and separately caches the corresponding objects even if they're identical. If you always use the same order for parameters, CloudFront forwards fewer requests to your origin.
Lambda@Edge is an extension of AWS Lambda, a compute service that lets you execute functions that customize the content that CloudFront delivers. You can author Node.js or Python functions in one Region, US-East-1 (N. Virginia), and then execute them in AWS locations globally that are closer to the viewer, without provisioning or managing servers. Lambda@Edge scales automatically, from a few requests per day to thousands per second. Processing requests at AWS locations closer to the viewer instead of on origin servers significantly reduces latency and improves the user experience.

With Lambda@Edge, you can improve your cache hit ratio by making the following changes to query strings before CloudFront forwards requests to your origin:
- Alphabetize key-value pairs by the name of the parameter.
- Change the case of key-value pairs to lowercase.
Therefore, the correct answer is: Write a Lamda@Edge function that will normalize the query parameters by sorting them in alphabetical order and converting them into lower case. Deploy this function with the CloudFront distribution and set “viewer request” as the trigger to invoke the function. With the "viewer request" set as the trigger, the Lambda@Edge function will normalize the query string before CloudFront processes it. CloudFront will then see the matching cache item for the normalized request, thus increasing the cache hit ratio.
The option that says: Reconfigure the CloudFront distribution to remove the caching behavior based on query string parameters. This will cache the requests regardless of the order or case of the query parameters is incorrect. This will ignore any query parameters and will cache all requests which will cause CloudFront to return incorrect cached items to users.
The option that says: Launch a reverse proxy inside the application VPC to intercept the requests going to the origin instances. Process the query parameters to sort them by name and convert them to lowercase letters before forwarding them to the instances is incorrect. This will not increase the cache hit ratio because CloudFront already forwarded the request to the origin as the proxy processes it which defeats the purpose of having a CloudFront cache.
The option that says: Reconfigure the CloudFront distribution to ensure that the “case insensitive” option is enabled for processing query string parameters is incorrect. CloudFront is case-sensitive when caching objects. There is no "case-insensitive" option in CloudFront. You will have to normalize your query parameters if you want all requests to be in lower-case.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-normalize-query-string-parameters
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html
https://docs.amazonaws.cn/en_us/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html
https://docs.amazonaws.cn/en_us/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html#cache-hit-ratio-query-string-parameters

Check out these Amazon CloudFront and AWS Lambda Cheat Sheets:
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/aws-lambda/

</details>

---

# Group B — Security & identity (8)

<a id="q9"></a>

## Q9

A leading commercial bank has a hybrid network architecture and is extensively using AWS for its day-to-day operations. The bank uses an Amazon S3 bucket to store sensitive bank records. It has versioning enabled and does not have any encryption. The new solutions architect for the company was asked to implement Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C) for the Amazon S3 bucket to ensure data inside it is secured both at rest and in transit.

Which of the following options should the solutions architect implement to achieve the company requirements? (Select TWO.)

- **A.** Use WSS (WebSocket Secure)
- **B.** For presigned URLs, specify the algorithm using the x-amz-server-side​-encryption​-customer-key-MD5 request header
- **C.** For Amazon S3 REST API calls, use the following HTTP Request Headers: x-amz-server-side​-encryption​-customer-algorithm x-amz-server-side​-encryption​-customer-key x-amz-server-side​-encryption​-customer-key-MD5
- **D.** Only use the S3 console to upload and update objects with SSE-C encryption.
- **E.** For presigned URLs, specify the algorithm using the x-amz-server-side​-encryption​-customer-algorithm request header

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E (you answered correctly)

🔑 **Key words:** encrypt at rest + in transit, customer-provided keys

⚠️ **Watch:** Watch SSE-C headers vs SSE-KMS headers

🧠 **Rule:** SSE-C → x-amz-server-side-encryption-customer-* headers (HTTPS required)

### TD explanation

Server-side encryption is about protecting data at rest. Using server-side encryption with customer-provided encryption keys (SSE-C) allows you to set your own encryption keys. With the encryption key you provide as part of your request, Amazon S3 manages both the encryption as it writes to disks, and decryption when you access your objects. Therefore, you don't need to maintain any code to perform data encryption and decryption. The only thing you do is manage the encryption keys you provide.
When you upload an object, Amazon S3 uses the encryption key you provide to apply AES-256 encryption to your data and removes the encryption key from memory. Amazon S3 will reject any requests made over HTTP when using SSE-C. For security reasons, it is recommended that you consider any key you send erroneously using HTTP to be compromised. You should discard the key and rotate as appropriate.
At the time of object creation—that is, when you are uploading a new object or making a copy of an existing object—you can specify if you want Amazon S3 to encrypt your data by adding the x-amz-server-side-encryption header to the request. Set the value of the header to the encryption algorithm AES256 that Amazon S3 supports. Amazon S3 confirms that your object is stored using server-side encryption by returning the response header x-amz-server-side-encryption.

Therefore, the following options are correct:
- For Amazon S3 REST API calls, you have to include the following HTTP Request Headers:
x-amz-server-side-encryption-customer-algorithm
x-amz-server-side-encryption-customer-key
x-amz-server-side-encryption-customer-key-MD5
- For presigned URLs, you should specify the algorithm using the x-amz-server-side-encryption-customer-algorithm request header.
The option that says: Using WSS (WebSocket Secure) is incorrect as you have to use HTTPS and not WSS.
The option that says: Specifying the algorithm using the x-amz-server-side​-encryption​-customer-key-MD5 request header for presigned URLs  is incorrect. You should use the x-amz-server-side-encryption-customer-algorithm request header instead.
The option that says: Only use the S3 console to upload and update objects with SSE-C encryption is incorrect because you should use S3 REST APIs instead of the S3 web console.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html
https://aws.amazon.com/blogs/security/how-to-use-the-rest-api-to-encrypt-s3-objects-by-using-aws-kms/
https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-encryption.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q18"></a>

## Q18

A company recently patched a vulnerability in its web application hosted on AWS. The solutions architect was tasked to improve the security of the company’s AWS resources as well as secure the web applications from common web vulnerabilities and cyber attacks. One example is a Distributed Denial of Service attack (DDoS) in which there is numerous incoming traffic coming from many different locations that simultaneously target the company web application and floods the network with bogus requests.

Which of the following options are recommended strategies for reducing DDoS attack surface and minimizing the blast radius in the cloud infrastructure? (Select TWO.)

- **A.** Add Elastic Load Balancing and Auto Scaling to your EC2 instances to improve availability and scalability. Use extra large EC2 instances to accommodate a surge of incoming traffic caused by a DDoS attack and utilize AWS Systems Manager Session Manager to filter all client-side web sessions to your instances.
- **B.** Always add a security group that only allows certain ports and authorized servers and protects your origin servers by putting it behind a CloudFront distribution. Enable AWS Shield Advanced which provides enhanced DDoS attack detection and monitoring for application-layer traffic to your AWS resources.
- **C.** Configure the Network Access Control Lists (ACLs) to only allow the required ports to your network. Identify and block common DDoS request patterns to effectively mitigate a DDoS attack by using AWS WAF.
- **D.** Allow versioning in your S3 bucket. Ensure that the OS of all of your EC2 instances are properly patched using Systems Manager Patch Manager.
- **E.** Strictly implement Multi-Factor Authentication (MFA) in AWS. Use a combination of Amazon Fraud Detector, AWS Config, and Trusted Advisor to fortify your AWS resources.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C (you answered correctly)

🔑 **Key words:** reduce DDoS attack surface, blast radius

⚠️ **Watch:** Shield Standard alone vs Advanced + WAF

🧠 **Rule:** DDoS: CloudFront + SG/NACL minimal ports + WAF rate rules + Shield Advanced

### TD explanation

Another important consideration when architecting on AWS is to limit the opportunities that an attacker may have to target your application. For example, if you do not expect an end-user to interact directly with certain resources, you will want to make sure that those resources are not accessible from the Internet. Similarly, if you do not expect end-users or external applications to communicate with your application on certain ports or protocols, you will want to make sure that traffic is not accepted. This concept is known as attack surface reduction. Resources that are not exposed to the Internet are more difficult to attack, which limits the options an attacker might have to target the availability of your application.

AWS Shield is a managed DDoS protection service that is available in two tiers: Standard and Advanced. AWS Shield Standard applies always-on detection and inline mitigation techniques, such as deterministic packet filtering and priority-based traffic shaping, to minimize application downtime and latency. AWS Shield Standard is included automatically and transparently to your Elastic Load Balancing load balancers, Amazon CloudFront distributions, and Amazon Route 53 resources at no additional cost. When you use these services that include AWS Shield Standard, you receive comprehensive availability protection against all known infrastructure layer attacks. Customers who have the technical expertise to manage their own monitoring and mitigation of application layer attacks can use AWS Shield together with AWS WAF rules to create a comprehensive DDoS attack mitigation strategy.
The following options are both correct as they are best practices for reducing the DDoS attack surface, which then limits the extent to which your application is exposed:
1. Always add a security group that only allows certain ports and authorized servers and protect your origin servers by putting it behind a CloudFront distribution. Enable AWS Shield Advanced which provides enhanced DDoS attack detection and monitoring for application-layer traffic to your AWS resources.
2. Configure the Network Access Control Lists (ACLs) to only allow the required ports to your network. Identify and block common DDoS request patterns to effectively mitigate a DDoS attack by using AWS WAF.
Using AWS Shield together with AWS WAF rules provide a comprehensive DDoS attack mitigation strategy.
The option that says: Add Elastic Load Balancing and Auto Scaling to your EC2 instances to improve availability and scalability. Use extra large EC2 instances to accommodate a surge of incoming traffic caused by a DDoS attack and utilize AWS Systems Manager Session Manager to filter all client-side web sessions to your instances is incorrect. Although it improves the scalability of your network in case of an ongoing DDoS attack, it simply absorbs the heavy application layer traffic and doesn't minimize the attack surface in your cloud architecture. In addition, AWS Systems Manager Session Manager is primarily used to provide secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys, but not to filter client-side web sessions.
The options that say: Allow versioning in your S3 bucket. Ensure that the OS of all of your EC2 instances are properly patched using Systems Manager Patch Manager and Strictly implement Multi-Factor Authentication (MFA) in AWS. Use a combination of Amazon Fraud Detector, AWS Config, and Trusted Advisor to fortify your AWS resources are incorrect because MFA, as well as the Versioning feature in S3, don't minimize the DDoS attack surface area. Although it is recommended that all of your instances are properly patched using the Systems Manager Patch Manager, it is still not enough to protect your cloud infrastructure against DDoS attacks. In addition, Amazon Fraud Detector is used in the detection of potentially fraudulent activities online. This service will not help you minimize the blast radius of a security attack.

References:
https://aws.amazon.com/answers/networking/aws-ddos-attack-mitigation/
https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf
https://d0.awsstatic.com/whitepapers/DDoS_White_Paper_June2015.pdf

Tutorials Dojo's AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q35"></a>

## Q35

A supermarket chain has a team that handles branded credit card transactions from major card schemes such as Mastercard, Visa, Discover, and AMEX. The company requested an external auditor to audit its AWS environment as part of the Payment Card Industry Data Security Standard (PCI DSS) security compliance. The auditor, operating from their own AWS account, has requested read-only access to the AWS resources across all the company's accounts in order to conduct the necessary checks.

Which of the following options is the recommended action to give the auditor the required access?

- **A.** Give the auditor each of your AWS users' username and password in your VPC and let the auditor use those credentials to login to a specific account and conduct the audit.
- **B.** Create an Active Directory account for the auditor and use identity federation for SSO to let the auditor log in to your AWS environment and conduct the audit.
- **C.** Create a new IAM User which has an access key ID and a secret access key for API calls that can be used by the auditor. Attach a read-only permissions to the IAM user.
- **D.** Create an IAM role in each AWS account that requires auditing, with a trust policy that lists the auditor's ARN as a principal. Assign this role read-only permissions to access necessary resources.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** external PCI auditor, multiple accounts

⚠️ **Watch:** Never create IAM users with access keys for outsiders

🧠 **Rule:** Auditor → read-only cross-account role in each account trusting the auditor

### TD explanation

In this scenario, it is recommended that you create an IAM Role that contains the required permissions needed by the auditor. This specific role can be revoked from the user once the compliance activities end.
An IAM role is similar to a user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials (password or access keys) associated with it. Instead, if a user assumes a role, temporary security credentials are created dynamically and provided to the user.

Therefore, the correct answer is: Create an IAM role in each AWS account that requires auditing, with a trust policy that lists the auditor's ARN as a principal. Assign this role read-only permissions to access necessary resources.
The options that says: Give the auditor each of your AWS users' username and password in your VPC and let the auditor use those credentials to login to a specific account and conduct the audit is incorrect. Providing the username and password is in itself a major security breach that will result in compliance failure.
The options that says: Create an Active Directory account for the auditor and use identity federation for SSO to let the auditor log in to your AWS environment and conduct the audit is incorrect. While using Active Directory and SSO is a secure approach, this method is typically used for integrating an organization's internal user management system with AWS, which is not necessary for an external auditor.
The options that says: Create a new IAM User which has an access key ID and a secret access key for API calls that can be used by the auditor. Attach a read-only permissions to the IAM user is incorrect. Creating a new IAM user for the auditor with read-only permissions is a valid approach, but it's not as secure and manageable as using roles. IAM users with long-term credentials can pose a security risk if those credentials are compromised.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q41"></a>

## Q41

A world-renowned logistics company runs its global enterprise e-commerce platform on the AWS cloud. The company has built a multi-tier web application running in a VPC that uses an Elastic Load Balancer in front of both the web tier and the app tier, with static assets served directly from an Amazon S3 bucket. It uses a combination of Amazon RDS and DynamoDB for the dynamic data and then archiving nightly into an Amazon S3 bucket for further processing with Amazon Elastic MapReduce. After a routine audit, the company found questionable log entries and suspected that someone is attempting to gain unauthorized access to the system. The solutions architect has been tasked to improve the security of the architecture from DDoS, SQL injection, and HTTP flood attacks as well as from bad bots (content scrapers).

Which of the following approach provides the MOST suitable and scalable solution to protect the infrastructure from these kinds of security attacks?

- **A.** Create an identical application stack that acts as a standby environment in another AWS region by using an AWS CloudFormation template. Use AWS CloudFormation StackSets to deploy the new stack and configure the security groups as well as network ACLs of the EC2 instances. Use Amazon Macie to protect the data stored in the Amazon S3 bucket. Create a Route 53 failover routing policy and configure an active-passive failover.
- **B.** Insert the identified suspect's source IP as an explicit inbound deny to the network ACL rules of the web tier's subnet. Set up AWS Config to periodically audit the network ACLs and ensure that the blacklisted IP addresses are always in place.
- **C.** Set up AWS WAF and AWS Shield Advanced on all web endpoints. Launch AWS WAF rules against SQL injection and other common web exploits.
- **D.** Establish an AWS Direct Connect (DX) connection to the VPC through a Direct Connect partner. Configure Internet connectivity to filter the traffic in hardware Web Application Firewall (WAF) and then reroute the traffic through the DX connection into the application. Use the company's wide area network (WAN) to send traffic over the DX connection.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** SQL injection, bots/scrapers, scalable

⚠️ **Watch:** NACLs/SGs can't inspect L7

🧠 **Rule:** L7 attacks → AWS WAF rules + Shield Advanced

### TD explanation

AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection.
AWS WAF is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web security rules. You can use AWS WAF to create custom rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that are designed for your specific application. New rules can be deployed within minutes, letting you respond quickly to changing traffic patterns. Also, AWS WAF includes a full-featured API that you can use to automate the creation, deployment, and maintenance of web security rules.

Hence, the correct answer is: Set up AWS WAF and AWS Shield Advanced on all web endpoints. Launch AWS WAF rules against SQL injection and other common web exploits.
The option that says: Create an identical application stack that acts as a standby environment in another AWS region by using an AWS CloudFormation template. Use AWS CloudFormation StackSets to deploy the new stack and configure the security groups as well as network ACLs of the EC2 instances. Use Amazon Macie to protect the data stored in the Amazon S3 bucket. Create a Route 53 failover routing policy and configure an active-passive failover is incorrect because this solution doesn't provide the necessary security protection against DDoS and other web vulnerability attacks. It only provides a disaster recovery plan in the event that your primary environment goes down. You have to set up AWS WAF and AWS Shield Advanced instead.
The option that says: Insert the identified suspect's source IP as an explicit inbound deny to the network ACL rules of the web tier's subnet. Set up AWS Config to periodically audit the network ACLs and ensure that the blacklisted IP addresses are always in place is incorrect. Even though blocking certain IPs will mitigate the risk, the attacker could maneuver the IP address and circumvent the IP check by NACL, and it does not prevent attacks from new sources of threat.
The option that says: Establish an AWS Direct Connect (DX) connection to the VPC through a Direct Connect partner. Configure Internet connectivity to filter the traffic in hardware Web Application Firewall (WAF) and then reroute the traffic through the DX connection into the application. Use the company's wide area network (WAN) to send traffic over the DX connection is incorrect. Although this option could work, the setup is very complex and it is not a cost-effective solution. Using the AWS Shield Advanced and AWS WAF combination is still the better solution.

References:
https://aws.amazon.com/waf/
https://www.slideshare.net/AmazonWebServices/aws-august-webinar-series-ddos-resiliency

Check out these AWS WAF and Shield Cheat Sheets:
https://tutorialsdojo.com/aws-waf/
https://tutorialsdojo.com/shield/

</details>

<a id="q52"></a>

## Q52

A startup currently runs a web application on an extra-large Amazon EC2 instance. The application allows users to upload and download various pdf files from a private Amazon S3 bucket using a pre-signed URL. The web application checks if the file being requested actually exists in the S3 bucket before generating the URL.

In this scenario, how should the solutions architect configure the web application to access the Amazon S3 bucket securely?

- **A.** 1. Store your access keys inside the EC2 instance. 2. Program your web application to retrieve the AWS credentials from the instance to interact with the objects in the S3 bucket.
- **B.** 1. Create an IAM user with the appropriate permissions allowing access and listing of all of the objects of the S3 bucket. Associate the EC2 instance with the IAM user. 2. Program your web application to retrieve the user credentials from the EC2 instance metadata.
- **C.** 1. Create an IAM role with a policy that allows listing of the objects in the S3 bucket. Launch the EC2 instance with the IAM role. 2. Program your web application to retrieve the temporary security credentials from the EC2 instance user data.
- **D.** 1. Create an IAM role with a policy that allows listing and uploading of the objects in the S3 bucket. Launch the EC2 instance with the IAM role. 2. Program your web application to retrieve the temporary security credentials from the EC2 instance metadata.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** EC2 app generates pre-signed URLs, access S3 securely

⚠️ **Watch:** Contrast Q6/Q17 — credentials on EC2 come from the instance role

🧠 **Rule:** EC2 → S3: IAM role, temporary credentials from instance metadata

### TD explanation

Applications that run on an EC2 instance must include AWS credentials in their AWS API requests. You could store AWS credentials directly within the EC2 instance and allow applications in that instance to use those credentials. But you would then have to manage the credentials and ensure that they securely pass the credentials to each instance and update each EC2 instance when it's time to rotate the credentials. That's a lot of additional work. Instead, you can and should use an IAM role to manage temporary credentials for applications that run on an EC2 instance. When you use a role, you don't have to distribute long-term credentials (such as a user name and password or access keys) to an EC2 instance.

Instead, the role supplies temporary permissions that applications can use when they make calls to other AWS resources. When you launch an EC2 instance, you specify an IAM role to associate with the instance. Applications that run on the instance can then use the role-supplied temporary credentials to sign API requests.
When the application runs, it obtains temporary security credentials from Amazon EC2 instance metadata. These are temporary security credentials that represent the role and are valid for a limited period of time to access various AWS resources. You can fetch the temporary security credentials from the instance by requesting it from this endpoint:
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access
In this particular scenario, you have to use a combination of IAM Role and EC2 instance metadata to provide the web application the required access it needs to access the S3 bucket. Hence, the correct answer is the following option:
1. Create an IAM role with a policy that allows listing and uploading of the objects in the S3 bucket. Launch the EC2 instance with the IAM role.
2. Program your web application to retrieve the temporary security credentials from the EC2 instance metadata.

The following option is incorrect because it is a security vulnerability to store the AWS credentials in your EC2 instances:
1. Store your access keys inside the EC2 instance.
2. Program your web application to retrieve the AWS credentials from the instance to interact with the objects in the S3 bucket.
Anyone who has access to that EC2 instance can find your AWS credentials and hence, this is not a recommended option.

The following option is incorrect because you should have used an IAM Role instead of an IAM User:
1. Create an IAM user with the appropriate permissions allowing access and listing of all of the objects of the S3 bucket. Associate the EC2 instance with the IAM user.
 2. Program your web application to retrieve the user credentials from the EC2 instance metadata.

The following option is incorrect because you should retrieve the IAM role's credentials from the EC2 instance metadata and not from the user data:
1. Create an IAM role with a policy that allows listing of the objects in the S3 bucket. Launch the EC2 instance with the IAM role.
2. Program your web application to retrieve the temporary security credentials from the EC2 instance user data.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html
 https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#instance-metadata-security-credentials

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q64"></a>

## Q64

A company has several financial applications hosted in AWS that uses Amazon S3 buckets to store static data. The Solutions Architect recently discovered that some employees store highly classified data into S3 buckets without proper approval. To mitigate any security risks, the Architect needs to determine all possible S3 objects that contain personally identifiable information (PII) and determine whether the data has been accessed. Due to the sheer volume of data, the Architect must implement an automated solution to accomplish this important task.

Which of the following should the solutions architect implement for this scenario?

- **A.** Detect personally identifiable information (PII) on the specific S3 buckets using Amazon Athena. Set up Amazon CloudWatch to determine if the objects with PII have been recently accessed by tracking the GET API calls that are used to download these objects.
- **B.** Enable Amazon Macie on the S3 buckets to automatically classify the data and detect any objects with personally identifiable information (PII). Determine if the objects with PII have been recently accessed by tracking the GET API calls in AWS CloudTrail.
- **C.** Use Amazon GuardDuty to detect personally identifiable information (PII) on the Amazon S3 buckets. Determine if the objects with PII have been recently accessed by tracking the GET API calls in AWS CloudTrail that are used to download these objects.
- **D.** Install the Amazon Inspector agent on the Amazon S3 buckets. Use AWS CloudTrail to determine if the objects with personally identifiable information (PII) have been recently accessed by tracking the GET API calls that are used to fetch these objects.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** classified data in S3, PII, automated

⚠️ **Watch:** GuardDuty/Inspector don't classify data

🧠 **Rule:** Find PII in S3 → Macie; who accessed it → CloudTrail data events

### TD explanation

Amazon Macie is an ML-powered security service that helps you prevent data loss by automatically discovering, classifying, and protecting sensitive data stored in Amazon S3. Amazon Macie uses machine learning to recognize sensitive data such as personally identifiable information (PII) or intellectual property, assigns a business value, and provides visibility into where this data is stored and how it is being used in your organization.
Amazon Macie continuously monitors data access activity for anomalies and delivers alerts when it detects the risk of unauthorized access or inadvertent data leaks. Amazon Macie has the ability to detect global access permissions inadvertently being set on sensitive data, detect uploading of API keys inside source code, and verify sensitive customer data is being stored and accessed in a manner that meets their compliance standards.

Hence, the correct answer is: Enable Amazon Macie on the S3 buckets to automatically classify the data and detect any objects with personally identifiable information (PII). Determine if the objects with PII have been recently accessed by tracking the GET API calls in AWS CloudTrail.
The option that says: Detect personally identifiable information (PII) on the specific S3 buckets using Amazon Athena. Set up Amazon CloudWatch to determine if the objects with PII have been recently accessed by tracking the GET API calls that are used to download these objects is incorrect because Amazon Athena is not capable of detecting personally identifiable information (PII) in an Amazon S3 bucket. You have to use Amazon Macie instead. In addition, you have to use AWS CloudTrail to track the GET API calls that are used to fetch the objects with PII.
The option that says: Use Amazon GuardDuty to detect personally identifiable information (PII) on the Amazon S3 buckets. Determine if the objects with PII have been recently accessed by tracking the GET API calls in AWS CloudTrail that are used to download these objects is incorrect because GuardDuty is just a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads. You have to use Amazon Macie instead.
The option that says: Install the Amazon Inspector agent on the Amazon S3 buckets. Use AWS CloudTrail to determine if the objects with personally identifiable information (PII) have been recently accessed by tracking the GET API calls that are used to fetch these objects is incorrect because you can only install the Amazon Inspector agent to EC2 instances and not to S3 buckets. Amazon Inspector is basically an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. You have to use Amazon Macie instead.

References:
https://docs.aws.amazon.com/macie/latest/userguide/what-is-macie.html
https://aws.amazon.com/macie/faq/
https://docs.aws.amazon.com/macie/index.html

Check out this Amazon Macie Cheat Sheet:
https://tutorialsdojo.com/amazon-macie/

</details>

<a id="q73"></a>

## Q73

A tech company is about to undergo a financial audit. It has been planned to use a third-party web application that needs to have certain AWS access to issue several API commands. It will discover Amazon EC2 resources running within the enterprise's account. The company has internal security policies that require any outside access to its environment to conform to the principles of least privilege. The solutions architect must ensure that the credentials used by the third-party vendor cannot be used by any other third party. The third-party vendor also has an AWS account where it runs its web application and it already provided a unique customer ID, including their AWS account number.

Which of the following options would allow the solutions architect to give permissions to the third-party vendor in compliance with the company requirements?

- **A.** Create a new IAM role for the 3rd-party vendor. Add a permission policy that only allows the actions required by the third party application. Also, add a trust policy with a Condition element for the ExternalId context key. The Condition must test the ExternalId context key to ensure that it matches the unique customer ID from the 3rd party vendor.
- **B.** Use Amazon Connect to allow the third-party application to access your AWS resources. In the AWS Connect configuration, input the ExternalId context key to ensure that it matches the unique customer ID of the 3rd party vendor.
- **C.** Provide your own access key and secret key to the third-party software.
- **D.** Create an IAM user in the enterprise account that has permissions allowing only the actions required by the third-party application. Also generate a new access key and secret key from the user to be given to the third-party provider.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** third-party vendor, discover EC2, confused deputy

⚠️ **Watch:** Fixed TD2 Q41 miss

🧠 **Rule:** Third party → cross-account role with ExternalId condition

### TD explanation

At times, you need to give third party access to your AWS resources (delegate access). One important aspect of this scenario is the External ID, optional information that you can use in an IAM role trust policy to designate who can assume the role.
To use an external ID, update a role trust policy with the external ID of your choice. Then, when someone uses the AWS CLI or AWS API to assume that role, they must provide the external ID.
For example, let's say that you decide to hire a third-party company called Boracay Corp to monitor your AWS account and help optimize costs. In order to track your daily spending, Boracay Corp needs to access your AWS resources. Boracay Corp also monitors many other AWS accounts for other customers.

Do not give Boracay Corp access to an IAM user and its long-term credentials in your AWS account. Instead, use an IAM role and its temporary security credentials. An IAM role provides a mechanism to allow a third party to access your AWS resources without needing to share long-term credentials (for example, an IAM user's access key).
You can use an IAM role to establish a trusted relationship between your AWS account and the Boracay Corp account. After this relationship is established, a member of the Boracay Corp account can call the AWS STS AssumeRole API to obtain temporary security credentials. The Boracay Corp members can then use the credentials to access AWS resources in your account.
When a user, a resource, an application, or any service needs to access any AWS service or resource, always opt to create an appropriate role that has the least privileged access or only the required access, rather than using any other credentials such as keys.
Therefore, the correct answer is: Create a new IAM role for the 3rd-party vendor. Add a permission policy that only allows the actions required by the third party application. Also, add a trust policy with a Condition element for the ExternalId context key. The Condition must test the ExternalId context key to ensure that it matches the unique customer ID from the 3rd party vendor.
The option that says: Use Amazon Connect to allow the third-party application to access your AWS resources. In the AWS Connect configuration, input the ExternalId context key to ensure that it matches the unique customer ID of the 3rd party vendor is incorrect because Amazon Connect is simply an easy to use omnichannel cloud contact center that helps companies provide superior customer service at a lower cost. You should use an IAM Role in this scenario instead of Amazon Connect.
The option that says: Provide your own access key and secret key to the third-party software is incorrect because you should never share your access and secret keys.
The option that says: Create an IAM user in the enterprise account that has permissions allowing only the actions required by the third-party application and generating a new access key and secret key from the user to be given to the third-party provider is incorrect because when a user is created, its security credentials are stored in the EC2 which can be compromised, and the creation of the appropriate role is always the better solution rather than creating a user.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q74"></a>

## Q74

A large software company has an on-premises LDAP server and has established an IPSec VPN connection between its on-premises network and its VPC in AWS. The company wants to enable employees to access AWS resources using the same corporate account used inside the company network.

Which of the following actions should the solutions architect implement to achieve the company’s requirements?

- **A.** Create an identity broker that authenticates against the on-premises LDAP server and then calls AWS STS to assume an IAM role, generating temporary AWS security credentials. The employees can use these credentials to access AWS resources.
- **B.** Set up a federation between the on-premises LDAP server and AWS IAM. When employees authenticate against the LDAP server, retrieve the name of an IAM role associated with the user. Use AWS STS to assume that IAM role and provide the employees with temporary credentials to access AWS resources.
- **C.** Create an identity broker that authenticates against the on-premises LDAP server and then calls AWS STS to get IAM federated user credentials. The employees can use these credentials to access AWS resources.
- **D.** Integrate the on-premises LDAP server with AWS IAM so the employees can log into IAM using their corporate LDAP credentials. Once authenticated, they can use the temporary credentials to access any AWS resource.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** on-prem LDAP, same corporate account, not SAML

⚠️ **Watch:** Fixed TD2 Q28 miss

🧠 **Rule:** LDAP (no SAML) → custom identity broker → STS AssumeRole

### TD explanation

If your identity store is not compatible with SAML 2.0, then you can build a custom identity broker application to perform a similar function. The broker application authenticates users, requests temporary credentials for users from AWS, and then provides them to the user to access AWS resources.
To enable corporate employees to access the company's AWS resources, you can develop a custom identity broker application. The application verifies that employees are signed into the company's existing identity and authentication system (which might use LDAP, Active Directory, or another system). The identity broker application then obtains temporary security credentials for the employees. To get temporary security credentials, the identity broker application calls either the AssumeRole or GetFederationToken actions in STS to obtain temporary security credentials.

Hence, the correct answer is: Create an identity broker that authenticates against the on-premises LDAP server and then calls AWS STS to assume an IAM role, generating temporary AWS security credentials. The employees can use these credentials to access AWS resources is correct because it involves creating an identity broker that authenticates against the on-premises LDAP server and then calls AWS STS to assume an IAM role, generating temporary AWS security credentials. This allows the employees to access AWS resources using their corporate account.
The option that says: Set up a federation between the on-premises LDAP server and AWS IAM. When employees authenticate against the LDAP server, retrieve the name of an IAM role associated with the user. Use AWS STS to assume that IAM role and provide the employees with temporary credentials to access AWS resources is incorrect because it primarily involves setting up a federation between the on-premises LDAP server and AWS IAM, which does not align with the company's requirement of enabling employees to access AWS resources using the same corporate account used inside the company network.
The option that says: Create an identity broker that authenticates against the on-premises LDAP server and then calls AWS STS to get IAM federated user credentials. The employees can use these credentials to access AWS resources is incorrect as the users need to be authenticated using LDAP first and not just via STS. In addition, the temporary credentials to log into AWS should be provided by STS and not the identity broker.
The option that says: Integrate the on-premises LDAP server with AWS IAM so the employees can log into IAM using their corporate LDAP credentials. Once authenticated, they can use the temporary credentials to access any AWS resource is incorrect because you cannot use the LDAP credentials to log into IAM. IAM supports identity federation, which allows you to manage access to your AWS resources centrally through your existing identity provider (IdP), but it does not directly integrate with LDAP for user authentication.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html
https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

---

# Group C — Governance & ops automation (6)

<a id="q34"></a>

## Q34

A cryptocurrency startup owns multiple AWS accounts which are all linked under AWS Organizations. Due to the financial nature of the business, the DevOps lead has been instructed by the CTO to prepare for IT auditing activities to meet industry compliance requirements.

Which of the following provides the most durable and secure logging solution that can be used to track changes made to all of the company’s AWS resources globally?

- **A.** 1. Launch a new CloudTrail trail using the AWS console with an existing S3 bucket to store the logs and with the "Apply trail to all regions" checkbox 2. Enable MFA Delete on the S3 bucket.
- **B.** 1. Launch a new CloudTrail trail using the AWS console with one new S3 bucket to store the logs and with the "Enable for all accounts in my organization" checkbox enabled. 2. Enable MFA Delete and Log Encryption on the S3 bucket.
- **C.** 1. Launch a new CloudTrail with one new S3 bucket to store the logs. 2. Configure SNS to send log file delivery notifications to your management system. 3. Enable MFA Delete and Log Encryption on the S3 bucket.
- **D.** 1. Launch three new CloudTrail trails using three new S3 buckets to store the logs for the AWS Management console, for AWS SDKs, and for the AWS CLI. 2. Enable MFA Delete and Log Encryption on the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** all accounts, durable + secure audit logs

⚠️ **Watch:** Per-account trails are more effort

🧠 **Rule:** Organization trail + one bucket with MFA Delete + encryption

### TD explanation

AWS CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

CloudTrail is enabled on your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. You can easily view recent events in the CloudTrail console by going to Event history. You can also enable the tracking of multi-region and global events. By default, the log files delivered by CloudTrail to your bucket are encrypted by Amazon server-side encryption with Amazon S3-managed encryption keys (SSE-S3). To provide a security layer that is directly manageable, you can instead use server-side encryption with AWS KMS keys (SSE-KMS) for your CloudTrail log files.
If you have created an organization in AWS Organizations, you can create a trail that will log all events for all AWS accounts in that organization. This is sometimes referred to as an organization trail. You can also choose to edit an existing trail in the management account and apply it to an organization, making it an organization trail. Organization trails log events for the management account, and all member accounts in the organization.
Organization trails are similar to regular trails in many ways. You can create multiple trails for your organization and choose whether to create an organization trail in all regions or a single region, and what kinds of events you want logged in your organization trail, just as in any other trail.
To create an organization trail, ensure that the "Enable for all accounts in my organization" option is checked when you create a new CloudTrail trail.

To protect your logs, you can encrypt the S3 bucket and add MFA Delete to protect your trail logs from accidental deletions. In this scenario, the following option is the best answer as it provides all of the things mentioned above:
1. Launch a new CloudTrail trail using the AWS console with one new S3 bucket to store the logs and with the "Enable for all accounts in my organization" checkbox enabled.
2. Enable MFA Delete and Log Encryption on the S3 bucket.
The following option is incorrect because although CloudTrail encrypts the data by default using SSE-S3, it is still more secure if you enabled log encryption and use SSE-KMS. Take note that the scenario asked for the most durable and secure logging solution:
1. Launch a new CloudTrail trail using the AWS console with an existing S3 bucket to store the logs and with the "Apply trail to all regions" checkbox
2. Enable MFA Delete on the S3 bucket.
The following option is incorrect because the multi-region option is not enabled which is needed to fetch all CloudTrail trail from all AWS regions:
1. Launch a new CloudTrail with one new S3 bucket to store the logs.
2. Configure SNS to send log file delivery notifications to your management system.
3. Enable MFA Delete and Log Encryption on the S3 bucket.
The following option is incorrect because this option creates too many S3 buckets that are unnecessary, whereas all of the events can be easily logged in just a single S3 bucket:
1. Launch three new CloudTrail trails using three new S3 buckets to store the logs for the AWS Management console, for AWS SDKs, and for the AWS CLI.
2. Enable MFA Delete and Log Encryption on the S3 bucket.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-encryption-cli.html
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html

Check out this AWS CloudTrail Cheat Sheet:
https://tutorialsdojo.com/aws-cloudtrail/

</details>

<a id="q59"></a>

## Q59

An enterprise has several development and production AWS accounts managed under its AWS Organization. Consolidated billing is enabled in the organization but the management wants more visibility on the AWS Billing and Cost Management. With the sudden increase in the Amazon RDS and Amazon DynamoDB costs, the management required all CloudFormation templates to enforce a consistent tagging with cost center numbers and project ID numbers on all resources that will be provisioned. The management also wants these tags to be enforced in all existing and future DynamoDB and RDS instances.

Which of the following options is the recommended strategy to meet the company requirements?

- **A.** Tag all existing resources in bulk using the Tag Editor. On the Billing and Cost Management page, create new cost allocation tags for the cost center and project ID. Wait for at least 24 hours to allow AWS to propagate the tags and gather cost reports.
- **B.** Create an AWS Config rule to check for any untagged resource and send a notification email to the finance team. Write a Lambda function that has a cross-account role to tag all RDS databases and DynamoDB resources on all accounts under the organization. Schedule this function to run every hour.
- **C.** Tag all existing resources in bulk using the Tag Editor. On the Billing and Cost Management page, create new cost allocation tags for the cost center and project ID. Apply an SCP on the organizational unit that denies users from creating resources that do not have the cost center and project ID tags.
- **D.** On the Billing and Cost Management page, create new cost allocation tags for the cost center and project ID. Wait for at least 24 hours to allow AWS to propagate the tags and gather cost reports. Update existing federated roles to deny users from creating resources that do not have the cost center and project ID tags.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** cost visibility, enforce tags on future DynamoDB/RDS

⚠️ **Watch:** Contrast Q75 — here the SCP denies untagged creates

🧠 **Rule:** Tag Editor + cost allocation tags + SCP deny create without tags

### TD explanation

Tags are words or phrases that act as metadata that you can use to identify and organize your AWS resources. A resource can have up to 50 user-applied tags. It can also have read-only system tags. Each tag consists of a key and one optional value.
You can add tags to resources when you create the resource. You can use the resource's service console or API to add, change, or remove those tags one resource at a time. To add tags to—or edit or delete tags of—multiple resources at once, use Tag Editor. With Tag Editor, you search for the resources that you want to tag, and then manage tags for the resources in your search results.
For each resource, each tag key must be unique, and each tag key can have only one value. You can use tags to organize your resources, and cost allocation tags to track your AWS costs on a detailed level. After you activate cost allocation tags, AWS uses the cost allocation tags to organize your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs. AWS provides two types of cost allocation tags, AWS generated tags and user-defined tags. AWS, or AWS Marketplace ISV defines, creates, and applies the AWS generated tags for you, and you define, create, and apply user-defined tags. You must activate both types of tags separately before they can appear in Cost Explorer or on a cost allocation report.

User-defined tags are tags that you define, create, and apply to resources. After you have created and applied the user-defined tags, you can activate them by using the Billing and Cost Management console for cost allocation tracking. Cost Allocation Tags appear on the console after you've enabled Cost Explorer, Budgets, AWS Cost and Usage Reports, or legacy reports. After you activate the AWS services, they appear on your cost allocation report. You can then use the tags on your cost allocation report to track your AWS costs. Tags are not applied to resources that were created before the tags were created.
Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. SCPs help you to ensure your accounts stay within your organization’s access control guidelines. SCPs are available only in an organization that has all features enabled. SCPs aren't available if your organization has enabled only the consolidated billing features.
Therefore, the correct answer is: Tag all existing resources in bulk using the Tag Editor. On the Billing and Cost Management page, create new cost allocation tags for the cost center and project ID. Apply an SCP on the organizational unit that denies users from creating resources that do not have the cost center and project ID tags. Tag Editor allows bulk tagging to easily tag your AWS resources. The SCP rules will enforce the company tagging policy by preventing users from creating resources that do not have the appropriate tags.
The option that says: Tag all existing resources in bulk using the Tag Editor. On the Billing and Cost Management page, create new cost allocation tags for the cost center and project ID. Wait for at least 24 hours to allow AWS to propagate the tags and gather cost reports is incorrect. This solution is incomplete. It does not prevent users from creating untagged resources in the future.
The option that says: Create an AWS Config rule to check for any untagged resource and send a notification email to the finance team. Write a Lambda function that has a cross-account role to tag all RDS databases and DynamoDB resources on all accounts under the organization. Schedule this function to run every hour is incorrect. This solution does not prevent users from creating untagged resources in the future and the AWS Config rule does not automatically tag non-compliant resources.
The option that says: On the Billing and Cost Management page, create new cost allocation tags for the cost center and project ID. Wait for at least 24 hours to allow AWS to propagate the tags and gather cost reports. Update existing federated roles to deny users from creating resources that do not have the cost center and project ID tags is incorrect. This may be possible but it will be cumbersome to edit all IAM policies across all the company AWS accounts. It is better to use an SCP applied at the organization unit level to enforce the tagging policy.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html#example-require-tag-on-create
https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html

Check out this AWS Billing and Cost Management Cheat Sheet:
https://tutorialsdojo.com/aws-billing-and-cost-management/

</details>

<a id="q66"></a>

## Q66

A company hosts its application on several Amazon EC2 instances inside a VPC. A known security vulnerability was discovered in the outdated Operating System of the company's EC2 fleet. The solutions architect is responsible for mitigating the vulnerability as soon as possible to safeguard your systems from various cybersecurity attacks. In addition, it is also required to record all of the changes to patches and association compliance statuses.

Which of the following options is the recommended way to meet the above requirements?

- **A.** Create a new AMI that automatically installs the OS security patches every week on the provided maintenance window. Roll out the new AMI to the Amazon EC2 instances fleet.
- **B.** Use AWS Systems Manager Patch Manager to deploy the OS security patches on the EC2 instances. Use AWS Config to manage, detect and record the security compliance of the EC2 instances.
- **C.** Set up Amazon Control Tower to deploy OS security updates to the Amazon EC2 instances. Create an Amazon Managed Grafana dashboard to visualize the security compliance of the EC2 instance fleet.
- **D.** Use AWS Systems Manager State Manager to ensure that OS security patches are installed on the Amazon EC2 instances. Use Amazon OpenSearch service to record, monitor, and visualize the patch statuses of the entire EC2 instance fleet.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** OS vulnerability, record patch compliance changes

⚠️ **Watch:** Contrast Q61 (missed) — Patch Manager again

🧠 **Rule:** Patch Manager for patches + AWS Config for compliance history

### TD explanation

AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

Since you are also required to record all of the changes to patch and association compliance statuses, you can use AWS Config to meet this requirement. AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations.
Therefore, the correct answer is: Use AWS Systems Manager Patch Manager to deploy the OS security patches on the EC2 instances. Use AWS Config to manage, detect and record the security compliance of the EC2 instances.
The option that says: Create a new AMI that automatically installs the OS security patches every week on the provided maintenance window. Roll out the new AMI to the Amazon EC2 instances fleet is incorrect. This approach is possible but is not recommended because you won't have control over each particular patch that needs to be installed. And it will be cumbersome to have a rollback operation in case a certain update broke the normal operations of your servers.
The option that says: Set up Amazon Control Tower to deploy OS security updates to the Amazon EC2 instances. Create an Amazon Managed Grafana dashboard to visualize the security compliance of the EC2 instance fleet is incorrect. Amazon Control Tower is used to automate the setup of your multi-account AWS environment, not install security patches.
The option that says: Use AWS Systems Manager State Manager to ensure that OS security patches are installed on the Amazon EC2 instances. Use Amazon OpenSearch service to record, monitor, and visualize the patch statuses of the entire EC2 instance fleet is incorrect. AWS Systems Manager State Manager is designed to be a  configuration management service that automates the process of keeping your managed nodes and other AWS resources in a state that you define. Although it may be possible to use it to install security patches, AWS SSM Patch Manager is the recommended service for installing OS updates to your EC2 instances.

References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html
https://aws.amazon.com/config/

Check out this AWS Systems Manager and AWS Config Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/
https://tutorialsdojo.com/aws-config/

</details>

<a id="q68"></a>

## Q68

A multinational manufacturing company has multiple AWS accounts in multiple AWS regions across North America, Europe, and Asia. The solutions architect has been tasked to set up AWS Organizations to centrally manage policies and have full administrative control across the multiple AWS accounts owned by the company.

Which of the following options is the recommended implementation to achieve this requirement with the LEAST effort?

- **A.** Set up AWS Organizations by establishing cross-account access from the master account to all member AWS accounts of the company. The master account will automatically have full administrative control across all member accounts.
- **B.** Set up AWS Organizations by sending an invitation to the master account of your organization from each of the member accounts of the company. Create an OrganizationAccountAccessRole IAM role in the member account and grant permission to the master account to assume the role.
- **C.** Use AWS Control Tower from the master account and enroll all the member AWS accounts of the company. AWS Control Tower will automatically provision the needed IAM permissions to have full administrative control across all member accounts.
- **D.** Set up AWS Organizations by sending an invitation to all member accounts of the company from the master account of your organization. Create an OrganizationAccountAccessRole IAM role in the member account and grant permission to the master account to assume the role.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** existing accounts into Organizations, full admin control, LEAST effort

⚠️ **Watch:** Invited accounts don't get OrganizationAccountAccessRole automatically

🧠 **Rule:** Invite accounts + create OrganizationAccountAccessRole in each

### TD explanation

After you create an Organization and verify that you own the email address associated with the master account, you can invite existing AWS accounts to join your organization. When you invite an account, AWS Organizations sends an invitation to the account owner, who decides whether to accept or decline the invitation. You can use the AWS Organizations console to initiate and manage invitations that you send to other accounts. You can send an invitation to another account only from the master account of your organization.
If you are the administrator of an AWS account, you also can accept or decline an invitation from an organization. If you accept, your account becomes a member of that organization. Your account can join only one organization, so if you receive multiple invitations to join, you can accept only one.

When an invited account joins your organization, you do not automatically have full administrator control over the account, unlike created accounts. If you want the master account to have full administrative control over an invited member account, you must create the  OrganizationAccountAccessRole IAM role in the member account and grant permission to the master account to assume the role.
Therefore, the correct answer is: Set up AWS Organizations by sending an invitation to all member accounts of the company from the master account of your organization. Create an OrganizationAccountAccessRole IAM role in the member account and grant permission to the master account to assume the role.
The option that says: Set up AWS Organizations by establishing cross-account access from the master account to all member AWS accounts of the company. The master account will automatically have full administrative control across all member accounts is incorrect. Cross-account access is primarily used for scenarios where you need to grant your IAM users permission to switch to roles within your AWS account or to roles defined in other AWS accounts that you own.
The option that says: Set up AWS Organizations by sending an invitation to the master account of your organization from each of the member accounts of the company. Create an OrganizationAccountAccessRole IAM role in the member account and grant permission to the master account to assume the role is incorrect. It entails a lot of effort to send an individual invitation to the master account from each of the member accounts of the company. It's stated in the scenario that you should achieve this requirement with the LEAST effort, and you can do this by sending an invitation to all member accounts of the company from the master account of your organization.
The option that says: Use AWS Control Tower from the master account and enroll all the member AWS accounts of the company. AWS Control Tower will automatically provision the needed IAM permissions to have full administrative control across all member accounts is incorrect. AWS Control Tower can be typically used to set up and manage multiple AWS accounts. However, it will not automatically provision IAM permissions for all member accounts.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html

Check out this AWS Organizations Cheat Sheet:
https://tutorialsdojo.com/aws-organizations/

</details>

<a id="q69"></a>

## Q69

A financial services company operates a multi-account AWS environment managed by AWS Control Tower. The security team must centralize the management of compliance and security findings across all accounts. The solution should implement preventive, detective, and responsive controls to align with AWS best practices for securing multi-account environments and ensuring compliance with organizational policies.

Which of the following options will meet the given requirements?

- **A.** Create a new member account in AWS Organizations. Enable AWS Security Hub and designate the account as the delegated administrator.
- **B.** Configure the AWS Control Tower management account to use an AWS CloudFormation StackSet with the automatic deployment option enabled to deploy Amazon Detective across all existing and newly created AWS accounts.
- **C.** Configure a delegated administrator account to create an AWS CloudTrail Lake data store that collects CloudTrail management events from all AWS accounts, and use the queried event data as the primary mechanism to centralize compliance and security findings.
- **D.** Set up Amazon GuardDuty in each account and export the findings to a central Amazon S3 bucket for aggregation and analysis.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** Control Tower, centralize compliance/security findings

⚠️ **Watch:** Not Config aggregator alone

🧠 **Rule:** Centralize findings → Security Hub with a delegated administrator account

### TD explanation

AWS Security Hub is a security service that provides a comprehensive view of an organization’s security posture. It collects and aggregates findings from multiple AWS services like Amazon GuardDuty, AWS Config, Amazon Inspector, and partner solutions. Security Hub enables centralization of findings, making it easier to monitor and manage security compliance across accounts.

AWS Organizations allows central management of multiple AWS accounts. It supports service delegation, enabling specific accounts to act as delegated administrators for various AWS services, including Security Hub. This helps streamline security operations by consolidating security management into a single account.
A delegated administrator account is a member account within an AWS Organization that has been assigned the authority to manage specific services on behalf of the management account. For AWS Security Hub, the delegated administrator can:

Enable Security Hub across all member accounts.
Aggregate findings from all accounts into the delegated administrator account.
Provide a unified security view, reducing the need for individual account management and aligning with AWS best practices.

Hence, the correct answer is: Create a new member account in AWS Organizations. Enable AWS Security Hub and designate the account as the delegated administrator. AWS Security Hub is the AWS-recommended service for centralizing compliance and security findings across multiple accounts. It integrates with GuardDuty, Inspector, Macie, IAM Access Analyzer, and AWS Config, providing preventive, detective, and responsive controls. Using a delegated administrator account aligns with AWS best practices for multi-account environments managed by AWS Control Tower.
The option that says: Configure the AWS Control Tower management account to use an AWS CloudFormation StackSet with the automatic deployment option enabled to deploy Amazon Detective across all existing and newly created AWS accounts is incorrect because Amazon Detective is primarily an investigation tool. It helps analyze and visualize findings, but does not centralize compliance/security findings or provide preventive and responsive controls. It’s useful after findings exist, not for managing compliance across accounts.
The option that says: Configure a delegated administrator account to create an AWS CloudTrail Lake data store that collects CloudTrail management events from all AWS accounts, and use the queried event data as the primary mechanism to centralize compliance and security findings is incorrect because CloudTrail Lake is typically used for event analysis and auditing. It helps with detective controls but does not provide preventive or responsive controls. It is not intended to be the central hub for compliance/security findings across accounts.
The option that says: Set up Amazon GuardDuty in each account and export the findings to a central Amazon S3 bucket for aggregation and analysis is incorrect because this approach would typically result in a significant amount of manual effort and administrative overhead. While Amazon GuardDuty can detect threats, manually exporting and aggregating findings is not efficient or scalable for a multi-account environment.

References:
https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html
https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html
https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html
https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/security-control-types.html

Check out these AWS Security Hub and AWS Organizations Cheat Sheets:
https://tutorialsdojo.com/aws-security-hub/
https://tutorialsdojo.com/aws-organizations/

</details>

<a id="q70"></a>

## Q70

A leading financial company owns multiple AWS accounts that are consolidated under one AWS Organization. To ensure that tags are always added when users create any resources across all accounts, the solutions architect should enforce the use of centralized resource provisioning tools and infrastructure-as-code templates that apply tags automatically upon resource creation across all account.

Which of the following options are the recommended actions to achieve the company requirements? (Select TWO.)

- **A.** Set up AWS Config to add the corresponding tags to your resources right from the very moment that they are created.
- **B.** Set up AWS Service Catalog to tag the provisioned resources with corresponding unique identifiers for portfolio, product, and users.
- **C.** Set up AWS generated tags by activating it in the Billing and Cost Management console of the member account.
- **D.** Set up the CloudFormation Resource Tags property to apply tags to certain resource types upon creation.
- **E.** Set up AWS Systems Manager Automation to automatically add tags to your provisioned resources.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D (you answered correctly)

🔑 **Key words:** enforce tags on resource creation across accounts

⚠️ **Watch:** Not Tag Editor (after the fact)

🧠 **Rule:** Tag on creation → Service Catalog TagOptions/auto-tags + CloudFormation resource tags

### TD explanation

AWS offers a variety of tools to help you implement proactive tag governance practices by ensuring that tags are consistently applied when resources are created.
AWS CloudFormation provides a common language for provisioning all the infrastructure resources in your cloud environment. CloudFormation templates are simple text files that create AWS resources in an automated and secure manner. When you create AWS resources using AWS CloudFormation templates, you can use the CloudFormation Resource Tags property to apply tags to certain resource types upon creation.
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application environments. AWS Service Catalog enables a self-service capability for users, allowing them to provision the services they need while also helping you to maintain consistent governance – including the application of required tags and tag values.
AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow or deny their access to AWS resources. When you create IAM policies, you can specify resource-level permissions, which include specific permissions for creating and deleting tags. In addition, you can include condition keys, such as aws:RequestTag and aws:TagKeys, which will prevent resources from being created if specific tags or tag values are not present.

With AWS Service Catalog, you can create products that represent the resources you want to provision, and you can define tagging policies for those products. When users provision resources through Service Catalog, the resources will be automatically tagged according to the defined tagging policies. This ensures that resources are consistently tagged with the required identifiers for portfolio, product, and users across all accounts.
AWS CloudFormation allows you to provision and manage AWS resources using infrastructure-as-code templates. The Resource Tags property in CloudFormation templates enables you to specify tags that should be applied to resources upon creation. This option aligns with the company's requirements for centralized resource provisioning and automatic tagging using infrastructure-as-code templates.
Therefore, the correct answers are:
- Set up AWS Service Catalog to tag the provisioned resources with corresponding unique identifiers for portfolio, product, and users.
- Set up the CloudFormation Resource Tags property to apply tags to certain resource types upon creation.
The option that says: Set up AWS config to add the corresponding tags to your resources right from the very moment that they are created is incorrect. AWS Config is a service that continuously monitors and records your AWS resource configurations, including resource metadata like tags. While AWS Config can help you identify resources that are not compliant with your tagging policies, it does not directly add tags to resources upon creation. Instead, AWS Config is typically used in combination with other services like AWS Lambda or AWS Systems Manager Automation to remediate non-compliant resources by adding missing tags. However, this approach is reactive, as it relies on first detecting resources without the required tags and then triggering a remediation action. Additionally, the requirement in this scenario is to proactively enforce tagging upon resource creation, which is why AWS Config alone is not the recommended solution.
The option that says: Set up AWS generated tags by activating it in the Billing and Cost Management console of the member account is incorrect. While enabling AWS generated tags can be beneficial for cost allocation and management purposes, it does not directly address the requirement of automatically adding tags upon resource creation across all accounts.
The option that says: Set up AWS Systems Manager Automation to automatically add tags to your provisioned resources is incorrect because AWS Systems Manager Automation is a service that allows you to automate common maintenance and deployment tasks across AWS resources. While Automation can be used to add tags to existing resources, it is not designed for automatically tagging resources upon creation. Automation is more suitable for managing and maintaining resources after they have been provisioned, not for the initial resource creation and tagging process. Additionally, it is not designed as a centralized resource provisioning tool or infrastructure-as-code solution, which are the recommended approaches for enforcing tagging upon resource creation in this scenario.

References:
https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html
https://aws.amazon.com/about-aws/whats-new/2018/03/aws-service-catalog-announces-autotags-for-automatic-tagging-of-provisioned-resources/

Check out this AWS Service Catalog Cheat Sheet:
https://tutorialsdojo.com/aws-service-catalog/

</details>

---

# Group D — DR, HA & multi-Region (6)

<a id="q15"></a>

## Q15

A company is running its main web service in a fleet of Amazon EC2 instances in the us-east-1 AWS Region. The EC2 instances are launched by an Auto Scaling group behind an Application Load Balancer (ALB). The EC2 instances are spread across multiple Availability Zones. The MySQL database is hosted on an Amazon EC2 instance in a private subnet. To improve the resiliency of the web service in case of a disaster, the Solutions Architect must design a data recovery strategy in another region using the available AWS services to lessen the operational overhead. The target RPO is less than a minute and the target RTO is less than 5 minutes. The Solutions Architect has started to provision the ALB and the Auto Scaling group on the us-west-2 region.

Which of the following steps should be implemented next to achieve the above requirements?

- **A.** Migrate the database from the Amazon EC2 instance to an Amazon RDS for MySQL instance. Set the us-east-1 region database as the master and configure a cross-Region read replica to the us-west-2 region. Configure Amazon Route 53 DNS entry with health checks and failover routing policy to the us-west-2 region.
- **B.** Migrate the database from the Amazon EC2 instance to an Amazon Aurora global database. Set the us-east-1 region as the primary database and the us-west-2 region as the secondary database. Configure Amazon Route 53 DNS entry with health checks and failover routing policy to the us-west-2 region.
- **C.** Migrate the database from the Amazon EC2 instance to an Amazon RDS for MySQL instance. Enable Multi-AZ deployment for this database. Configure Amazon Route 53 DNS entry with failover routing policy to the us-west-2 region.
- **D.** Create a snapshot of the current Amazon EC2 database instance and restore the snapshot to the us-west-2 region. Configure the new EC2 instance as MySQL standby database of the us-east-1 instance. Configure Amazon Route 53 DNS entry with failover routing policy to the us-west-2 region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** DB on EC2, second Region, failover

⚠️ **Watch:** Contrast Q16 — here the DB must go cross-Region

🧠 **Rule:** Cross-Region DR DB → Aurora Global Database + Route 53 failover

### TD explanation

Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions. It replicates your data with no impact on database performance, enables fast local reads with low latency in each region, and provides disaster recovery from region-wide outages.
Critical workloads with a global footprint, such as financial, travel, or gaming applications, have strict availability requirements and may need to tolerate a region-wide outage. Traditionally this required difficult tradeoffs between performance, availability, cost, and data integrity. Global Database uses storage-based replication with typical latency of less than 1 second, using dedicated infrastructure that leaves your database fully available to serve application workloads. In the unlikely event of a regional degradation or outage, one of the secondary regions can be promoted to read and write capabilities in less than 1 minute.

Aurora Global Database lets you easily scale database reads across the world and place your applications close to your users. Your applications enjoy quick data access regardless of the number and location of secondary regions, with typical cross-region replication latencies below 1 second. If your primary region suffers a performance degradation or outage, you can promote one of the secondary regions to take read/write responsibilities. An Aurora cluster can recover in less than 1 minute even in the event of a complete regional outage. This provides your application with an effective Recovery Point Objective (RPO) of 1 second and a Recovery Time Objective (RTO) of less than 1 minute, providing a strong foundation for a global business continuity plan.
Amazon Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources. If you have multiple resources that perform the same function, you can configure DNS failover so that Route 53 will route your traffic from an unhealthy resource to a healthy resource. Each health check that you create can monitor one of the following:
- The health of a specified resource, such as a web server
- The status of other health checks
- The status of an Amazon CloudWatch alarm
Therefore, the correct answer is: Migrate the database from the Amazon EC2 instance to an Amazon Aurora global database. Set the us-east-1 region as the primary database and the us-west-2 region as the secondary database. Configure Amazon Route 53 DNS entry with health checks and failover routing policy to the us-west-2 region.
The option that says: Migrate the database from the Amazon EC2 instance to an Amazon RDS for MySQL instance. Set the us-east-1 region database as the master and configure a cross-Region read replica to the us-west-2 region. Configure Amazon Route 53 DNS entry with health checks and failover routing policy to the us-west-2 region is incorrect. Although this is possible, there is no automatic way to promote the read replica on the backup region as the master database. You need to manually configure this, and when you do, the RDS instance will reboot. In this case, you might exceed the RPO of 1 minute and RTO of 5 minutes.
The option that says: Migrate the database from the Amazon EC2 instance to an Amazon RDS for MySQL instance. Enable Multi-AZ deployment for this database. Configure Amazon Route 53 DNS entry with failover routing policy to the us-west-2 region is incorrect. Multi-AZ deployment will protect you from outages on single AZ’s only. It will not protect your database from regional outages.
The option that says: Create a snapshot of the current Amazon EC2 database instance and restore the snapshot to the us-west-2 region. Configure the new EC2 instance as MySQL standby database of the us-east-1 instance. Configure Amazon Route 53 DNS entry with failover routing policy to the us-west-2 region is incorrect. Although this is a possible solution, the requirement is to use the available AWS services for lower operational overhead. This requires extra management effort to set up, configure and manage the database on the EC2 instance, instead of using a managed Amazon RDS database. Moreover, it won't be able to satisfy the requirement of providing a 1-minute RPO and 5-minute RTO.

References:
https://aws.amazon.com/rds/aurora/global-database/
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

Check out these Amazon Aurora Cheat Sheets:
https://tutorialsdojo.com/amazon-aurora/
https://tutorialsdojo.com/amazon-aurora-vs-amazon-rds/

</details>

<a id="q33"></a>

## Q33

A media company runs its new content management system (CMS) on a Windows-based Amazon EC2 instance. This is a test setup with a single instance. After a few weeks of testing, the application will be deployed on a production environment. For high availability, the application will be hosted on at least three Amazon EC2 instances across multiple Availability Zones. The current test EC2 instance has a 1 TB Amazon Elastic Block Store (EBS) volume as its root device. This is where all the static content is stored.

The solutions architect must ensure that all instances will have the same data at all times, for the application to work properly. The filesystem must also support Windows ACLs to control access to file contents. Additionally, all instances must be joined to the company’s Active Directory domain. The solution should have the least amount of management overhead.

Which of the following options should the Solutions Architect implement to meet the company's requirements?

- **A.** Create an Amazon Machine Image (AMI) of the test Amazon EC2 instance. Use the AMI for an Auto Scaling group with a minimum size of three instances that spans three Availability Zones (AZs). Create an Amazon Elastic Filesystem (Amazon EFS) volume. Write a user data script to join the instances on the AD domain and mount the EFS share upon boot-up.
- **B.** Create an Amazon Machine Image (AMI) of the test Amazon EC2 instance. Use the AMI for an Auto Scaling group with a minimum size of three instances that spans three Availability Zones (AZs). Create an Amazon FSx for Lustre filesystem that will be used for shared storage. Write a user data script to join the instances on the AD domain and mount the EFS share upon boot-up.
- **C.** Deploy a new Windows AMI for an Auto Scaling group with a minimum size of three instances and spans across three Availability Zones (AZs). Create an Amazon FSx for Windows File Server file system that will be used for shared storage. Write a user data script to install the CMS application, mount the FSx for Windows File Server file system and join the instances to the AD domain.
- **D.** Deploy a new Windows AMI for an Auto Scaling group with a minimum size of three instances and spans across three Availability Zones (AZs). Use an Amazon EBS volume with Multi-Attach enabled to allow multiple Amazon EC2 instances to share the volume. Write a user data script to install the CMS application and join the instances to the AD domain.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** Windows CMS, HA, shared storage, least overhead

⚠️ **Watch:** EFS is Linux-only (NFS)

🧠 **Rule:** Windows shared storage → FSx for Windows + ASG across 3 AZs

### TD explanation

Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system. FSx for Windows File Server has the features, performance, and compatibility to easily lift and shift enterprise applications to the AWS Cloud.
Amazon FSx supports a broad set of enterprise Windows workloads with fully managed file storage built on Microsoft Windows Server. Amazon FSx has native support for Windows file system features and for the industry-standard Server Message Block (SMB) protocol to access file storage over a network.
As a fully managed service, FSx for Windows File Server eliminates the administrative overhead of setting up and provisioning file servers and storage volumes. Additionally, Amazon FSx keeps Windows software up to date, detects and addresses hardware failures, and performs backups.

AWS recommends using a staging environment with the same configuration as your production environment. For example, use the same Active Directory (AD) and networking configurations, file system size and configuration, and Windows features, such as data deduplication and shadow copies. Running test workloads in a staging environment that simulates your desired production traffic helps the process run smoothly.
Therefore, the correct answer is: Deploy a new Windows AMI for an Auto Scaling group with a minimum size of three instances and spans across three Availability Zones (AZs). Create an Amazon FSx for Windows File Server file system that will be used for shared storage. Write a user data script to install the CMS application, mount the FSx for Windows File Server file system and join the instances to the AD domain. Amazon FSx for Windows File Server is a scalable file storage that is accessible over SMB protocol. Since it is built on Windows Server, it natively supports administrative features such as user quotas, end-user file restore, and Microsoft Active Directory integration.
The option that says: Create an Amazon Machine Image (AMI) of the test Amazon EC2 instance. Use the AMI for an Auto Scaling group with a minimum size of three instances that spans three Availability Zones (AZs). Create an Amazon Elastic Filesystem (Amazon EFS) volume. Write a user data script to join the instances on the AD domain and mount the EFS share upon boot-up is incorrect. Amazon EFS uses the NFS protocol which is primarily used by Linux AMIs. This filesystem does not support Windows ACLs.
The option that says: Create an Amazon Machine Image (AMI) of the test Amazon EC2 instance. Use the AMI for an Auto Scaling group with a minimum size of three instances that spans three Availability Zones (AZs). Create an Amazon FSx for Lustre filesystem that will be used for shared storage. Write a user data script to join the instances on the AD domain and mount the EFS share upon boot-up is incorrect. Amazon FSx for Lustre is POSIX-compliant file system that runs on Lustre. It can only be used by Linux-based instances.
The option that says: Deploy a new Windows AMI for an Auto Scaling group with a minimum size of three instances and spans across three Availability Zones (AZs). Use an Amazon EBS volume with Multi-Attach enabled to allow multiple Amazon EC2 instances to share the volume. Write a user data script to install the CMS application and join the instances to the AD domain is incorrect. This is not an ideal solution because Multi-Attach EBS volumes can only be attached on instances within the same Availability Zone.

References:
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html

Check out this Amazon FSx Cheat Sheet:
https://tutorialsdojo.com/amazon-fsx/

Check out this Amazon EFS, Amazon FSx for Windows and Amazon FSx for Lustre Comparison:
https://tutorialsdojo.com/amazon-efs-vs-amazon-fsx-for-windows-vs-amazon-fsx-for-lustre/

</details>

<a id="q38"></a>

## Q38

A company has a web service portal where users can perform read and write operations on its semi-structured data. The company wants to refactor the current application and leverage AWS-managed services for more scalability and higher availability. To ensure optimal user experience, the service is expected to respond to short but significant system load spikes. The service must be highly available and fault-tolerant in the event of a regional AWS failure.

Which of the following options is a suitable solution to meet the company's requirements?

- **A.** Use DocumentDB to store the semi-structured data. Create an edge-optimized Amazon API Gateway and AWS Lambda-based web service, and set it as the origin of a global Amazon CloudFront distribution. Add the company’s domain as an alternate name on the CloudFront distribution. Create an Amazon Route 53 Alias record pointed to the CloudFront distribution.
- **B.** Create a primary Amazon S3 bucket to store the semi-structured data. Enable S3 Cross-Region Replication to sync objects to the backup region. Create an Amazon API Gateway and AWS Lambda-based web service on each region, and set them as the origin for the two Amazon CloudFront distributions. Add the company’s domain as an alternate name on the CloudFront distributions. Create Amazon Route 53 Alias records pointed to each distribution using a failover routing policy.
- **C.** Create an Amazon DynamoDB global table to store the semi-structured data in two Regions. Use on-demand capacity mode to allow DynamoDB scaling. Run the web service on an Auto Scaling Amazon ECS Fargate cluster in each region. Place each Fargate cluster behind its own Application Load Balancer (ALB). Create Amazon Route 53 Alias records pointed to each ALB using a latency routing policy with health checks enabled.
- **D.** Create an Amazon Aurora global database to store the semi-structured data in two Regions. Configure Auto Scaling replicas on both regions. Run the web service on an Auto Scaling group of Amazon EC2 instances in both regions using the user data script to download the application code. Place each Auto Scaling group behind its own Application Load Balancer (ALB). Create a single Amazon Route 53 Alias record pointed to each ALB using a multi-value answer routing policy with health checks enabled.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** semi-structured data, Region failure, managed

⚠️ **Watch:** Not RDS cross-Region replica

🧠 **Rule:** Multi-Region active-active NoSQL → DynamoDB global tables + Fargate per Region

### TD explanation

Amazon DynamoDB is a fast, fully-managed NoSQL database service that makes it simple and cost effective to store and retrieve any amount of data, and serve any level of request traffic. DynamoDB helps offload the administrative burden of operating and scaling a highly-available distributed database cluster. This storage alternative meets the latency and throughput requirements of highly demanding applications by providing single-digit millisecond latency and predictable performance with seamless throughput and storage scalability.
DynamoDB stores structured data in tables, indexed by primary key, and allows low-latency read and write access to items ranging from 1 byte up to 400 KB. DynamoDB supports three data types (number, string, and binary), in both scalar and multi-valued sets. It supports document stores such as JSON, XML, or HTML in these data types. Tables do not have a fixed schema, so each data item can have a different number of attributes. The primary key can either be a single-attribute hash key or a composite hash-range key.
Global tables build on the global Amazon DynamoDB footprint to provide you with a fully managed, multi-region, and multi-active database that delivers fast, local, read and write performance for massively scaled, global applications. Global tables replicate your DynamoDB tables automatically across your choice of AWS Regions.

DynamoDB global tables are ideal for massively scaled applications with globally dispersed users. In such an environment, users expect very fast application performance. Global tables provide automatic multi-active replication to AWS Regions worldwide. They enable you to deliver low-latency data access to your users no matter where they are located.
AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design. Fargate allocates the right amount of compute, eliminating the need to choose instances and scale cluster capacity. Fargate runs each task or pod in its own kernel providing the tasks and pods their own isolated compute environment.
Therefore, the correct answer is: Create an Amazon DynamoDB global table to store the semi-structured data in two Regions. Use on-demand capacity mode to allow DynamoDB scaling. Run the web service on an Auto Scaling Amazon ECS Fargate cluster in each region. Place each Fargate cluster behind its own Application Load Balancer (ALB). Create Amazon Route 53 Alias records pointed to each ALB using a latency routing policy with health checks enabled. DynamoDB global table offers a multi-active database on multiple regions. AWS Fargate clusters scale up or down significantly faster than EC2 instances because they are only containers and can be provisioned quickly. Latency routing policy with health checks enabled ensures that users are sent to the fastest healthy region based on their location.
The option that says: Use DocumentDB to store the semi-structured data. Create an edge-optimized Amazon API Gateway and AWS Lambda-based web service, and set it as the origin of a global Amazon CloudFront distribution. Add the company's domain as an alternate name on the CloudFront distribution. Create an Amazon Route 53 Alias record pointed to the CloudFront distribution is incorrect because, while DocumentDB has a global clusters feature, only the primary cluster can perform write operations. In contrast, DynamoDB Global Tables provide multi-region, multi-active write capabilities with automatic failover, making it more suitable for this use case.
The option that says: Create a primary Amazon S3 bucket to store the semi-structured data. Enable S3 Cross-Region Replication to sync objects to the backup region. Create an Amazon API Gateway and AWS Lambda-based web service on each region, and set them as the origin for the two Amazon CloudFront distributions. Add the company’s domain as an alternate name on the CloudFront distributions. Create Amazon Route 53 Alias records pointed to each distribution using a failover routing policy is incorrect. Although you can primarily store structured and unstructured data, there is a delay of up to 15 minutes in Cross-Region Replication. In the event of a failover, some data might not have been replicated yet on the secondary region.
The option that says: Create an Amazon Aurora global database to store the semi-structured data in two Regions. Configure Auto Scaling replicas on both regions. Run the web service on an Auto Scaling group of Amazon EC2 instances in both regions using the user data script to download the application code. Place each Auto Scaling group behind its own Application Load Balancer (ALB). Create a single Amazon Route 53 Alias record pointed to each ALB using a multi-value answer routing policy with health checks enabled is incorrect. Scaling EC2 instances can take a few minutes because the EBS volumes need to be provisioned, and the OS needs to load along with the user script. This scaling time might not be quick enough for the expected short but significant spikes in the system load.

References:
https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/amazon-dynamodb.html
https://aws.amazon.com/dynamodb/global-tables/
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html
https://aws.amazon.com/fargate/

Check out these Amazon DynamoDB and AWS Fargate Cheat Sheets:
https://tutorialsdojo.com/amazon-dynamodb/
https://tutorialsdojo.com/aws-fargate/

</details>

<a id="q43"></a>

## Q43

A company runs its critical application in an Auto Scaling group of Amazon EC2 instances that uses ElastiCache with Append Only Files (AOF) enabled in multiple AWS regions. Recently, one of the regions experienced a power outage due to a storm which has affected the business revenue.

Assuming that only a short recovery downtime period is allowed, how should the solutions architect maintain site availability in case an event like this occurs again in the future?

- **A.** Set up a DNS active-active failover using latency based routing policy that resolves to an ELB. Configure the 'Evaluate Target Health' attribute to Yes.
- **B.** Consolidate all of your VPCs across multiple regions into a single Private Hosted Zone using Route 53.
- **C.** Enable Domain Name System Security Extensions (DNSSEC) in your domain. Configure Route 53 to automatically failover the traffic to a secondary group of healthy resources on standby. Configure the 'Evaluate Target Health' attribute to No.
- **D.** Create a dedicated Transit VPC to directly route multi-VPC traffic over a VPN connection across multiple regions.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** Region outage, short downtime allowed

⚠️ **Watch:** Failover vs latency routing

🧠 **Rule:** Active-active Regions → latency routing + Evaluate Target Health

### TD explanation

DNS active-active failover allows access to your unhealthy instances to be redirected to active instances. Together with latency-based routing, customers accessing your web servers will be balanced throughout available healthy instances based on latency.

Hence, the correct answer is: Set up a DNS active-active failover using latency based routing policy that resolves to an ELB. Configure the 'Evaluate Target Health' attribute to Yes.
The option that says: Console all of your VPCs across multiple regions into a single Private Hosted Zone using Route 53 is incorrect because private hosted zones are primarily used to specify how you want to route traffic in a single VPC or a group of VPCs, instead of going through the public Internet. This does not provide an active-active failover.
The option that says: Enable Domain Name System Security Extensions (DNSSEC) in your domain. Configure Route 53 to automatically failover the traffic to a secondary group of healthy resources on standby. Configure the 'Evaluate Target Health' attribute to No is incorrect because DNSSEC is primarily used to protect your domain from DNS spoofing or man-in-the-middle attacks. If you set Evaluate Target Health to No, Route 53 continues to route traffic to the records that an alias record refers to even if health checks for those records are failing. Thus, this configuration will lead to unavailability issues on the application.
The option that says: Create a dedicated Transit VPC to directly route multi-VPC traffic over a VPN connection across multiple regions is incorrect because a Transit VPC is not suitable in providing a failover routing for your resources. This set up is more suitable for scenarios where you are designing a Multiple-VPC VPN connection sharing.

References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html
 https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html
 https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html

Check out this Amazon Route 53 Cheat Sheet:
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q51"></a>

## Q51

A small telecommunications company has recently adopted a hybrid cloud architecture with AWS. They are storing static files of their on-premises web application on a 5 TB gateway-stored volume in AWS Storage Gateway, which is attached to the application server via an iSCSI interface. As part of their disaster recovery plan, they should be able to run the web application on AWS in case their on-premises network encountered any technical issues.

Which of the following options is the MOST suitable solution that you should implement?

- **A.** Restore the static content from an AWS Storage Gateway to an S3 bucket and link it to the EC2 instance where the app server is running.
- **B.** Restore the static content by attaching the AWS Storage Gateway to the EC2 instance that hosts the application server.
- **C.** For the static content, create an EFS file system from the AWS Storage Gateway service and mount it to the EC2 instance where the application server is hosted.
- **D.** Generate an EBS snapshot of the static content from the AWS Storage Gateway service.Afterward, restore it to an EBS volume that you can then attach to the EC2 instance where the application server is hosted.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** stored volume, make data available on AWS if on-prem fails

⚠️ **Watch:** Fixed TD2 Q45 miss

🧠 **Rule:** Storage Gateway volume → EBS snapshot → restore to EBS on EC2

### TD explanation

By using stored volumes, you can store your primary data locally, while asynchronously backing up that data to AWS. Stored volumes provide your on-premises applications with low-latency access to their entire datasets. At the same time, they provide durable, offsite backups. You can create storage volumes and mount them as iSCSI devices from your on-premises application servers. Data written to your stored volumes are stored on your on-premises storage hardware. This data is asynchronously backed up to Amazon S3 as Amazon Elastic Block Store (Amazon EBS) snapshots.

You can restore an Amazon EBS snapshot to an on-premises gateway storage volume if you need to recover a backup of your data. You can also use the snapshot as a starting point for a new Amazon EBS volume, which you can then attach to an Amazon EC2 instance.
Since this is using a Volume Storage Gateway, you have to generate an EBS snapshot and generate an EBS Volume to restore the data.
Therefore, the correct answer is: Generate an EBS snapshot of the static content from the AWS Storage Gateway service. Afterwards, restore it to an EBS volume that you can then attach to the EC2 instance where the application server is hosted.
The option that says: Restore the static content from an AWS Storage Gateway to an S3 bucket and linking it on the EC2 instance where the app server is running is incorrect because linking the S3 bucket to the EC2 instance is not a suitable option to restore data from AWS Storage Gateway. You should generate a snapshot first and generate an EBS Volume that you can attach to the instance.
The option that says: Restore the static content by attaching the AWS Storage Gateway to the EC2 instance that hosts the application server is incorrect because you cannot directly attach the AWS Storage Gateway to a running EC2 instance which runs your application server. Although you can deploy and activate a volume or tape gateway on EC2, this instance has a different AMI than your application server which runs on a different EC2 instance. You have to generate an EBS Volume first, based on the generated snapshot from AWS Storage Gateway.
The option that says: Create an EFS file system from the AWS Storage Gateway service and mounting it to the EC2 instance where the application server is hosted for the static content is incorrect because using EFS in this scenario is not appropriate. You should use EBS Volumes to restore your data from Storage Gateway.

References:
https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#storage-gateway-stored-volume-concepts
https://aws.amazon.com/storagegateway/faqs/

Check out this AWS Storage Gateway Cheat Sheet:
https://tutorialsdojo.com/aws-storage-gateway/

Tutorials Dojo's AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q65"></a>

## Q65

A major telecommunications company is planning to set up a disaster recovery solution for its Amazon Redshift cluster which is being used by its online data analytics application. Database encryption is enabled on their clusters using AWS KMS and it is required that the recovery site should be at least 500 miles from their primary cloud location.

Which of the following is the most suitable solution to meet these requirements and to make its architecture highly available?

- **A.** Create a new AWS CloudFormation stack that will deploy the cluster in another region and will regularly back up the data to an S3 bucket, configured with cross-region replication. In case of an outage in the primary region, just use the snapshot from the S3 bucket and then start the cluster.
- **B.** Set up a snapshot copy grant for a master key in the destination region and enable cross-region snapshots in your Redshift cluster to copy snapshots of the cluster to another region.
- **C.** Develop a scheduled job using AWS Lambda which will regularly take a snapshot of the Redshift cluster and copy it to another region.
- **D.** In your Redshift cluster, enable the cross-region snapshot copy feature to copy snapshots to another region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** Redshift + KMS encryption, DR in another Region

⚠️ **Watch:** Fixed repeat drill miss

🧠 **Rule:** Encrypted Redshift cross-Region → snapshot copy grant in destination Region

### TD explanation

Snapshots are point-in-time backups of a cluster. There are two types of snapshots: automated and manual. Amazon Redshift stores these snapshots internally in Amazon S3 by using an encrypted Secure Sockets Layer (SSL) connection. Amazon Redshift automatically takes incremental snapshots that track changes to the cluster since the previous automated snapshot.

Automated snapshots retain all of the data required to restore a cluster from a snapshot. You can take a manual snapshot any time. When you restore from a snapshot, Amazon Redshift creates a new cluster and makes the new cluster available before all of the data is loaded, so you can begin querying the new cluster immediately. The cluster streams data on demand from the snapshot in response to active queries, then loads the remaining data in the background.
When you launch an Amazon Redshift cluster, you can choose to encrypt it with a master key from the AWS Key Management Service (AWS KMS). AWS KMS keys are specific to a region. If you want to enable cross-region snapshot copy for an AWS KMS-encrypted cluster, you must configure a snapshot copy grant for a master key in the destination region so that Amazon Redshift can perform encryption operations in the destination region.
Therefore, the correct answer is: Set up a snapshot copy grant for a master key in the destination region and enable cross-region snapshots in your Redshift cluster to copy snapshots of the cluster to another region.
The option that says: Create a new AWS CloudFormation stack that will deploy the cluster in another region and will regularly back up the data to an S3 bucket, configured with cross-region replication. In case of an outage in the primary region, just use the snapshot from the S3 bucket and then start the cluster is incorrect. Using a combination of CloudFormation and a separate S3 bucket entails a lot of configuration and set up compared with just enabling cross-region snapshot copy in your Redshift cluster.
The option that says: Develop a scheduled job using AWS Lambda which will regularly take a snapshot of the Redshift cluster and copy it to another region is incorrect. It is not recommended to use AWS Lambda to copy data on your Redshift cluster to another region. You simply have to enable cross-region snapshot copy in your Redshift cluster in order to meet the requirement.
The option that says: In your Redshift cluster, enable the cross-region snapshot copy feature to copy snapshots to another region is incorrect. Although it is right to use the cross-region snapshot copy feature, you still have to configure a snapshot copy grant for a master key in the destination region so that Amazon Redshift can perform encryption operations in the destination region.

References:
https://docs.aws.amazon.com/redshift/latest/mgmt/managing-snapshots-console.html#snapshot-crossregioncopy-configure
https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html

Check out this Amazon Redshift Cheat Sheet:
https://tutorialsdojo.com/amazon-redshift/

Tutorials Dojo's AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

---

# Group E — Deployment & CI/CD (5)

<a id="q31"></a>

## Q31

A cryptocurrency trading platform uses a Lambda function which has recently been integrated with DynamoDB Streams as its event source. Whenever there is a new deployment, the incoming traffic to the function must be shifted in two increments using CodeDeploy. Ten percent of the incoming traffic should be shifted to the new version and then the remaining 90 percent should be deployed five minutes later. It is also required to trace the event source that invoked the Lambda function including the downstream calls that the function made.

Which of the following options should the solutions architect implement to satisfy this requirement?

- **A.** Configure an All-at-once deployment configuration for your Lambda function and use AWS Config to trace the event source and downstream calls.
- **B.** Configure a Canary deployment configuration for your Lambda function. Enable active tracing to integrate AWS X-Ray to your AWS Lambda function.
- **C.** Configure a Linear deployment configuration for your Lambda function and use AWS Config to trace the event source and downstream calls.
- **D.** Configure a Rolling with additional batch deployment configuration for your Lambda function and use X-Ray to trace the event source and downstream calls.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** Lambda traffic in two increments, trace downstream calls

⚠️ **Watch:** Linear = many steps; canary = two

🧠 **Rule:** Two-step Lambda shift → Canary; tracing → X-Ray active tracing

### TD explanation

CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services. CodeDeploy can deploy application content that runs on a server and is stored in Amazon S3 buckets, GitHub repositories, or Bitbucket repositories. CodeDeploy can also deploy a serverless Lambda function. You do not need to make changes to your existing code before you can use CodeDeploy.
When you deploy to an AWS Lambda compute platform, the deployment configuration specifies the way traffic is shifted to the new Lambda function versions in your application.

In a Canary deployment configuration, the traffic is shifted in two increments. You can choose from predefined canary options that specify the percentage of traffic shifted to your updated Lambda function version in the first increment and the interval, in minutes, before the remaining traffic is shifted in the second increment.
Therefore, the correct answer is: Configure a Canary deployment configuration for your Lambda function. Enable active tracing to integrate AWS X-Ray to your AWS Lambda function.
The option that says: Configure an All-at-once deployment configuration for your Lambda function and using AWS Config to trace the event source and downstream calls is incorrect. If you use this deployment configuration, the traffic is shifted from the original Lambda function to the updated Lambda function version all at once. In addition, you can't use AWS Config to trace the event source and downstream calls. You have to use X-Ray instead and this can be done by simply enabling active tracing.

The option that says: Configure a Linear deployment configuration for your Lambda function and using AWS Config to trace the event source and downstream calls is incorrect. A deployment configuration will cause the traffic to be shifted in equal increments with an equal number of minutes between each increment. You can choose from predefined linear options that specify the percentage of traffic shifted in each increment and the number of minutes between each increment.
The option that says: Configure a Rolling with additional batch deployment configuration for your Lambda function and using X-Ray to trace the event source and downstream calls is incorrect. Although X-Ray can be used to trace the event source and downstream calls,Rolling with additional batch is only applicable in Elastic Beanstalk and not for Lambda.

References:
https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html
https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html

Check out this AWS CodeDeploy Cheat Sheet:
https://tutorialsdojo.com/aws-codedeploy/

</details>

<a id="q46"></a>

## Q46

A company uses an AWS CloudFormation template to deploy its three-tier web application on the AWS Cloud. The CloudFormation template contains a custom AMI value used by the Auto Scaling group of Amazon EC2 instances. Every new version of the application corresponds to a new AMI that needs to be deployed. The company doesn’t want any downtime during the deployment process. The Solutions Architect has been tasked to implement a solution that will streamline its AMI deployment process by performing the following steps:

Update the CloudFormation template to refer to the new AMI.

Launch new EC2 instances from the new AMI by calling the UpdateStack API to replace the old EC2 instances.

Which of the following actions should the Solutions Architect take to achieve the above requirements?

- **A.** Create a new CloudFormation change set to view the changes in the new version of the template. Verify that the correct AMI is listed on the change before executing the change set.
- **B.** Update the CloudFormation template AWS::AutoScaling::LaunchConfiguration resource section and specify a DeletionPolicy attribute with MinSuccessfulInstancesPercent of 50.
- **C.** Update the CloudFormation template AWS::AutoScaling::AutoScalingGroup resource section and specify an UpdatePolicy attribute with an AutoScalingRollingUpdate policy.
- **D.** Copy the updated template and deploy it to a new CloudFormation stack. After its successful deployment, update the Amazon Route 53 records to point to the new stack and delete the old stack.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** new AMI per release via UpdateStack, replace instances

⚠️ **Watch:** Not CreationPolicy

🧠 **Rule:** ASG instance replacement in CloudFormation → UpdatePolicy AutoScalingRollingUpdate

### TD explanation

AWS CloudFormation gives you an easy way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles, by treating infrastructure as code. You can use a template to create, update, and delete an entire stack as a single unit, as often as you need to, instead of managing resources individually.
The AWS::AutoScaling::AutoScalingGroup resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

When you update the launch template for an Auto Scaling group, this update action does not deploy any change across the running Amazon EC2 instances in the Auto Scaling group. All new instances will get the updated configuration, but existing instances continue to run with the configuration that they were originally launched with. This works the same way as any other Auto Scaling group.
You can add an UpdatePolicy attribute to your stack to perform rolling updates (or replace the group) when a change has been made to the group. Alternatively, you can force a rolling update on your instances at any time after updating the stack by starting an instance refresh.
The UpdatePolicy on the AutoScalingGroup will automatically execute the rolling deployment of the new AMI instances when the Cloudformation template is updated.
To specify how AWS CloudFormation handles rolling updates for an Auto Scaling group, use the AutoScalingRollingUpdate policy. Rolling updates enable you to specify whether AWS CloudFormation updates instances that are in an Auto Scaling group in batches or all at once. For example, suppose you have updated the MaxBatchSize in your stack template's UpdatePolicy from 1 to 10. This allows you to perform updates without causing downtime to your currently running application.
Therefore, the correct answer is: Update the CloudFormation template AWS::AutoScaling::AutoScalingGroup resource section and specify an UpdatePolicy attribute with an AutoScalingRollingUpdate policy.
The option that says: Create a new CloudFormation change set to view the changes in the new version of the template. Verify that the correct AMI is listed on the change before executing the change set is incorrect. Although this is possible, the existing EC2 instances won't be replaced this way immediately. The change set will only update the Launch Template with the new AMI and will only be applied to the newly spawned instances, excluding the existing ones.
The option that says: Update the CloudFormation template AWS::AutoScaling::LaunchConfiguration resource section and specify a DeletionPolicy attribute with MinSuccessfulInstancesPercentof 50 is incorrect. This option should have used a CreationPolicy attribute instead of a DeletionPolicy attribute because there is no MinSuccessfulInstancesPercentof element in the DeletionPolicy attribute.
The option that says: Copy the updated template and deploy it to a new CloudFormation stack. After its successful deployment, update the Amazon Route 53 records to point to the new stack and delete the old stack is incorrect. Although this is possible, it typically involves an extra step that requires updating the Route 53 entry for every deployment. This does not satisfy the deployment requirement of calling the UpdateStack API to replace the instances.

References:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStack.html

Check out the Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q54"></a>

## Q54

A company recently adopted a modern design for its legacy application. The new application is now suitable for native cloud deployments so the CI/CD pipelines need to be updated as well. The following deployment requirements are needed to support the new application:

- The pipeline should support deployments of new versions several times every hour.

- The pipeline should be able to quickly rollback to the previous application version if any problems are encountered on the new version.

Which of the following options is the recommended solution to meet the company requirements?

- **A.** Package the newer application version on AMIs including the needed configurations. Reconfigure the CI/CD pipeline to deploy this AMI by replacing the current Amazon EC2 instances.
- **B.** Reconfigure the pipeline to create a Staging environment on AWS Elastic Beanstalk. Deploy the newer version on the Staging environment. Swap the Staging and Production environment URLs to shift traffic to the newer version.
- **C.** Use Amazon Lightsail to handle the deployment of new Amazon EC2 instances and the needed load balancers. Add an Amazon EC2 user data script to download the latest application artifact from an Amazon S3 bucket. Use a weighted routing policy on Amazon Route 53 to slowly shift traffic to the newer version.
- **D.** Package the newer application version on AMIs including the needed configurations. Update the Launch Template of the Auto Scaling group and trigger a scale-out to use this new AMI. Ensure that the configured termination policy is to delete the old instances using the previous AMI.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** staging, swap, roll back quickly

⚠️ **Watch:** Contrast Q53 (missed) — zero-downtime deploy patterns

🧠 **Rule:** Elastic Beanstalk blue/green → deploy to staging env + swap CNAMEs

### TD explanation

AWS Elastic Beanstalk provides several options for how deployments are processed, including deployment policies (All at once, Rolling, Rolling with additional batch, Immutable, and Traffic splitting) and options that let you configure the batch size and health check behavior during deployments. By default, your environment uses all-at-once deployments. If you created the environment with the EB CLI and it's a scalable environment, it uses rolling deployments.
You can use the AWS Elastic Beanstalk console to upload an updated source bundle and deploy it to your Elastic Beanstalk environment or redeploy a previously uploaded version. The following list provides summary information about the different deployment policies and adds related considerations.
All at once – The quickest deployment method. Suitable if you can accept a short loss of service and if quick deployments are important to you. With this method, Elastic Beanstalk deploys the new application version to each instance.
Rolling – Avoids downtime and minimizes reduced availability at a cost of a longer deployment time. Suitable if you can't accept any period of completely lost service. With this method, your application is deployed to your environment one batch of instances at a time.
Rolling with additional batch – Avoids any reduced availability at a cost of an even longer deployment time compared to the Rolling method. Suitable if you must maintain the same bandwidth throughout the deployment. With this method, Elastic Beanstalk launches an extra batch of instances, then performs a rolling deployment.
Immutable – A slower deployment method that ensures your new application version is always deployed to new instances instead of updating existing instances. It also has the additional advantage of a quick and safe rollback in case the deployment fails.
Traffic splitting – A canary testing deployment method. Suitable if you want to test the health of your new application version using a portion of incoming traffic while keeping the rest of the traffic served by the old application version.
For deployments that depend on resource configuration changes or a new version that can't run alongside the old version, you can launch a new environment with the new version and perform a CNAME swap for a blue/green deployment.
Because AWS Elastic Beanstalk performs an in-place update when you update your application versions, your application can become unavailable to users for a short period of time. You can avoid this downtime by performing a blue/green deployment, where you deploy the new version to a separate environment and then swap CNAMEs of the two environments to redirect traffic to the new version instantly. With this method, you can have two independent environments and you can quickly switch between the version by swapping the URLs.

Therefore, the correct answer is: Reconfigure the pipeline to create a Staging environment on AWS Elastic Beanstalk. Deploy the newer version on the Staging environment. Swap the Staging and Production environment URLs to shift traffic to the newer version. This is a blue/green deployment on Elastic Beanstalk. You can deploy a newer version without affecting the current version and quickly roll back by just swapping the URLs again.
The option that says: Package the newer application version on AMIs including the needed configurations. Reconfigure the CI/CD pipeline to deploy this AMI by replacing the current Amazon EC2 instances is incorrect. This is a possible deployment procedure, however, the rollback procedure will take too long because it will need to replace the current EC2 instances again.
The option that says: Use Amazon Lightsail to handle the deployment of new Amazon EC2 instances and the needed load balancers. Add an Amazon EC2 user data script to download the latest application artifact from an Amazon S3 bucket. Use a weighted routing policy on Amazon Route 53 to slowly shift traffic to the newer version is incorrect. This is possible, however, is designed to deploy simple web applications in Dev/Test environments, not for production, mission-critical workloads. The rollback for this procedure will take longer too, as there is a need to re-create newer instances again to run the EC2 user data script.
The options that says: Package the newer application version on AMIs including the needed configurations. Update the Launch Template of the Auto Scaling group and trigger a scale-out to use this new AMI. Ensure that the configured termination policy is to delete the old instances using the previous AMI is incorrect. This is also a possible deployment, however, it is not recommended for this scenario. With this solution, you will have to re-deploy the older AMI in case of a rollback which takes more time compared to just swapping the environment URLs.

References:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deploy-existing-version.html

Check out the AWS Elastic Beanstalk Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-beanstalk/

</details>

<a id="q56"></a>

## Q56

A company has a critical application running on an Auto Scaling group of Amazon EC2 instances. The application CI/CD pipelines are created on AWS CodePipeline and all of the relevant AWS resources are defined in AWS CloudFormation templates. During deployments, the Auto Scaling group spawns new instances and the user data script downloads the new artifact from a central Amazon S3 bucket. With several code updates during the development cycle, a recent update on the CloudFormation templates has caused a major application downtime.

Which of the following solutions should the Solutions Architect implement to reduce the chances of downtime during deployments?

- **A.** Update the CloudFormation templates to include cfn helper scripts. This will detect and report conditions during deployments to ensure that only healthy deployments are continued. Create test plans for the quality assurance team to ensure that changes are tested on a non-production environment before applying to production.
- **B.** Add an AWS CodeBuild stage on the deployment pipeline to automatically test on a non-production environment. Leverage change sets on AWS CloudFormation to preview changes before applying to production. Set up a blue/green deployment pattern on AWS CodeDeploy to deploy changes on a separate environment and to quickly rollback if needed.
- **C.** Check the CloudFormation templates for errors with the help of plugins on the integrated development environment (IDE). Ensure that the templates are valid using AWS CLI. Include cfn helper scripts on the deployment code to detect and report for errors. Deploy on a non-production environment and perform manual testing before applying changes to production.
- **D.** Set up a blue/green deployment pattern on AWS CodeDeploy using CloudFormation to update the user data deployment scripts. Manually login to the instances and perform tests to verify that the deployment is successful and the application is running as expected.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** deployments caused downtime, preview changes

⚠️ **Watch:** Not manual approvals alone

🧠 **Rule:** Test stage + CloudFormation change sets + CodeDeploy blue/green

### TD explanation

AWS CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers. It provides prepackaged build environments for popular programming languages and build tools such as Apache Maven, Gradle, and more. You can also customize build environments in CodeBuild to use your own build tools.
You can automate your release process by using AWS CodePipeline to test your code and run your builds with AWS CodeBuild. This involves two main steps:
- Create a continuous delivery (CD) pipeline with CodePipeline that automates builds with CodeBuild.
- Add test and build automation with CodeBuild to an existing pipeline in CodePipeline.
When you need to update a CloudFormation stack, understanding how your changes will affect running resources before you implement them can help you update stacks with confidence. Change sets allow you to preview how proposed changes to a stack might impact your running resources, for example, whether your changes will delete or replace any critical resources, AWS CloudFormation makes the changes to your stack only when you decide to execute the change set, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another change set.
AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers. AWS CodeDeploy makes it possible to automate the deployment of code to either Amazon EC2 or on-premises instances. AWS CodeDeploy supports blue/green deployments. AWS CodeDeploy offers two ways to perform blue/green deployments:
- In the first approach, AWS CodeDeploy makes a copy of an Auto Scaling group. It, in turn, provisions new Amazon EC2 instances, deploys the application to these new instances, and then redirects traffic to the newly deployed code.
- In the second approach, you use instance tags or an Auto Scaling group to select the instances that will be used for the green environment. AWS CodeDeploy then deploys the code to the tagged instances.
In the following figure, the release manager uses the workstation instance to push a new version of the application to AWS CodeDeploy and starts a blue-green deployment. AWS CodeDeploy creates a copy of the Auto Scaling group. It launches two new web server instances just like the original two. AWS CodeDeploy installs the new version of the application and then redirects the load balancer to the new instances.

Therefore, the correct answer is: Add an AWS CodeBuild stage on the deployment pipeline to automatically test on a non-production environment. Leverage change sets on AWS CloudFormation to preview changes before applying to production. Set up a blue/green deployment pattern on AWS CodeDeploy to deploy changes on a separate environment and to quickly rollback if needed. With AWS CodeBuild on your pipeline, you can add automated tests to verify that the artifact is working as expected. CloudFormation change sets allow you to preview proposed changes on templates before you apply them. AWS CodeDeploy can use a blue/green deployment strategy to have a separate deployment environment and easy rollback procedures.
The option that says: Update the CloudFormation templates to include cfn helper scripts. This will detect and report conditions during deployments to ensure that only healthy deployments are continued. Create test plans for the quality assurance team to ensure that changes are tested on a non-production environment before applying to production is incorrect. This may be possible, however, it will rely on another team to do the testing. It is better to set up AWS CodeBuild to automate this verification which also reduces any human intervention or errors.
The option that says: Check the CloudFormation templates for errors with the help of plugins on the integrated development environment (IDE). Ensure that the templates are valid using AWS CLI. Include cfn helper scripts on the deployment code to detect and report for errors. Deploy on a non-production environment and perform manual testing before applying changes to production is incorrect. Using plugins on IDEs only detects syntax errors on your CloudFormation codes. It won't prevent the user from creating logical errors on the template that may have drastic effects on the current environment.
The option that says: Set up a blue/green deployment pattern on AWS CodeDeploy using CloudFormation to update the user data deployment scripts. Manually login to the instances and perform tests to verify that the deployment is successful and the application is running as expected is incorrect. This is possible but not recommended since manual intervention is prone to human error. You should create automated testing instead to verify the application for every deployment.

References:
https://aws.amazon.com/blogs/devops/performing-bluegreen-deployments-with-aws-codedeploy-and-auto-scaling-groups/
https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html
https://aws.amazon.com/blogs/devops/automating-your-api-testing-with-aws-codebuild-aws-codepipeline-and-postman/

Check out these AWS CodeBuild, AWS CodeDeploy, and AWS CloudFormation Cheat Sheets:
https://tutorialsdojo.com/aws-codebuild/
https://tutorialsdojo.com/aws-codedeploy/
https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q67"></a>

## Q67

A leading financial company runs its application in an Amazon ECS Cluster. The application processes a large stream of intraday data and stores the generated result in a DynamoDB table. To comply with the financial regulatory policy, the solutions architect was tasked to design a system that detects new entries in the DynamoDB table and then automatically run tests to verify the results using a Lambda function.

Which of the following options can satisfy the company’s requirement with minimal configuration changes?

- **A.** Set up a DynamoDB stream to detect the new entries and automatically trigger the Lambda function.
- **B.** Run an AWS Lambda function using Amazon SNS as a trigger each time the ECS Cluster successfully processes financial data.
- **C.** Migrate the table to Amazon DocumentDB to take advantage of its integration with Amazon EventBridge which can invoke a Lambda function for specific database events.
- **D.** Detect the new entries in the DynamoDB table using Systems Manager Automation then automatically invoke the Lambda function for processing.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** verify results on new DynamoDB entries, minimal changes

⚠️ **Watch:** Not polling with a scheduled job

🧠 **Rule:** React to new DynamoDB items → DynamoDB Streams → Lambda

### TD explanation

Amazon DynamoDB is integrated with AWS Lambda so that you can create triggers—pieces of code that automatically respond to events in DynamoDB Streams. With triggers, you can build applications that react to data modifications in DynamoDB tables.
If you enable DynamoDB Streams on a table, you can associate the stream ARN with a Lambda function that you write. Immediately after an item in the table is modified, a new record appears in the table's stream. AWS Lambda polls the stream and invokes your Lambda function synchronously when it detects new stream records.

You can create a Lambda function which can perform a specific action that you specify, such as sending a notification or initiating a workflow. For instance, you can set up a Lambda function to simply copy each stream record to persistent storage, such as EFS or S3, to create a permanent audit trail of write activity in your table.
Suppose you have a mobile gaming app that writes to a TutorialsDojoCourses table. Whenever the TopCourse attribute of the TutorialsDojoScores table is updated, a corresponding stream record is written to the table's stream. This event could then trigger a Lambda function that posts a congratulatory message on a social media network. (The function would simply ignore any stream records that are not updates to TutorialsDojoCourses or that do not modify the TopCourse attribute.)
Therefore, the correct answer is: Set up a DynamoDB stream to detect the new entries and automatically trigger the Lambda function. In this way, the requirement can be met with a minimal configuration change. DynamoDB streams can be used as an event source to automatically trigger Lambda functions whenever there is a new entry.
The option that says: Run an AWS Lambda function using Amazon SNS as a trigger each time the ECS Cluster successfully processes financial data is incorrect. You don't need to create an SNS topic just to invoke Lambda functions. You can simply enable DynamoDB streams to meet the requirement with less configuration.
The option that says: Migrate the table to Amazon DocumentDB to take advantage of its integration with Amazon EventBridge which can invoke a Lambda function for specific database events is incorrect. The question requires minimal configuration changes so migrating the database to another service is not recommended as this will require a effort and changes on the application.
The option that says: Detect the new entries in the DynamoDB table using Systems Manager Automation then automatically invoking the Lambda function for processing is incorrect. The Systems Manager Automation service is primarily used to simplify common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. It does not have the capability to detect new entries in a DynamoDB table.

References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html

Check out this Amazon DynamoDB cheat sheet:
https://tutorialsdojo.com/amazon-dynamodb/

</details>

---

# Group F — Migration & hybrid (6)

<a id="q2"></a>

## Q2

A fashion company in France sells bags, clothes, and other luxury items in its online web store. The online store is currently hosted on the company’s on-premises data center. The company has recently decided to move all of its on-premises infrastructure to the AWS cloud. The main application is running on an NGINX web server and a database with an Oracle Real Application Clusters (RAC) One Node configuration.

Which of the following is the best way to migrate the application to AWS and set up an automated backup?

- **A.** Launch an EC2 instance and run an NGINX server to host the application. Deploy an RDS instance and enable automated backups on the RDS RAC cluster.
- **B.** Launch an On-Demand EC2 instance and run an NGINX server to host the application. Deploy an RDS instance with a Multi-AZ deployment configuration and enable automated backups on the RDS RAC cluster.
- **C.** Launch an EC2 instance for both the NGINX server as well as for the database. Attach EBS Volumes on the EC2 instance of the database and then write a shell script that runs the manual snapshot of the volumes.
- **D.** Launch an EC2 instance for both the NGINX server as well as for the database. Attach EBS volumes to the EC2 instance of the database and then use the Data Lifecycle Manager to automatically create scheduled snapshots against the EBS volumes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** Oracle RAC One Node, automated backup

⚠️ **Watch:** RDS doesn't support RAC

🧠 **Rule:** Oracle RAC → EC2 + EBS + Data Lifecycle Manager snapshots

### TD explanation

Oracle RAC is not supported by RDS. That is why you need to deploy the database in an EC2 instance and then either create a shell script to automate the backup or use the Data Lifecycle Manager to automate the process.
An Oracle Real Application Clusters (RAC) One Node option provides virtualized servers on a single machine. This provides an 'always on' availability for single-instance databases for a fraction of a cost.

Amazon Data Lifecycle Manager (DLM) for EBS Snapshots provides a simple, automated way to back up data stored on Amazon EBS volumes. You can define backup and retention schedules for EBS snapshots by creating lifecycle policies based on tags. With this feature, you no longer have to rely on custom scripts to create and manage your backups.
Hence, the correct answer is: Launch an EC2 instance for both the NGINX server as well as for the database. Attach EBS volumes to the EC2 instance of the database and then use the Data Lifecycle Manager to automatically create scheduled snapshots against the EBS volumes.
The option that says: Launch an EC2 instance for both the NGINX server as well as for the database. Attach EBS Volumes on the EC2 instance of the database and then write a shell script that runs the manual snapshot of the volumes is incorrect. Although this approach is valid, a more suitable option is to use the Data Lifecycle Manager (DLM) to automatically take the snapshot of the EC2 instance. The DLM can also reduce storage costs by deleting outdated backups.
The following options are incorrect as these two use Amazon RDS, which doesn't natively support Oracle RAC:
- Launch an EC2 instance and run an NGINX server to host the application. Deploy an RDS instance and enable automated backups on the RDS RAC cluster.
- Launch an On-Demand EC2 instance and run an NGINX server to host the application. Deploy an RDS instance with a Multi-AZ deployment configuration and enable automated backups on the RDS RAC cluster.

References:
https://aws.amazon.com/rds/oracle/faqs/
 https://aws.amazon.com/about-aws/whats-new/2015/11/self-managed-oracle-rac-on-ec2/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q3"></a>

## Q3

A global finance company has multiple data centers around the globe. Due to the ever-growing data that your company is storing, the solutions architect was instructed to set up a durable, cost-effective solution to archive sensitive data from the existing on-premises tape-based backup infrastructure to AWS Cloud.

Which of the following options is the recommended implementation to achieve the company requirements?

- **A.** Set up a Tape Gateway to back up your data in Amazon S3 and archive it in Amazon Glacier using your existing tape-based processes.
- **B.** Set up a Stored Volume Gateway to back up your data in Amazon S3 with point-in-time backups as EBS snapshots.
- **C.** Set up a Tape Gateway to back up your data in Amazon S3 with point-in-time backups as tapes which will be stored in the Virtual Tape Shelf.
- **D.** Set up a File Gateway to back up your data in Amazon S3 and archive in Amazon Glacier using your existing tape-based processes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** tape-based backup processes, archive

⚠️ **Watch:** Contrast Q14 (missed) — tape gateway is for backup, not processing

🧠 **Rule:** Keep tape backup workflow → Tape Gateway → S3/Glacier

### TD explanation

AWS Storage Gateway connects an on-premises software appliance with cloud-based storage to provide seamless integration with data security features between your on-premises IT environment and the AWS storage infrastructure. You can use the service to store data in the Amazon Web Services Cloud for scalable and cost-effective storage that helps maintain data security.
AWS Storage Gateway offers file-based file gateways (Amazon S3 File and Amazon FSx File), volume-based (Cached and Stored), and tape-based storage solutions.
Tape Gateway offers a durable, cost-effective solution to archive your data in the AWS Cloud. With its virtual tape library (VTL) interface, you use your existing tape-based backup infrastructure to store data on virtual tape cartridges that you create on your tape gateway. Each tape gateway is preconfigured with a media changer and tape drives. These are available to your existing client backup applications as iSCSI devices. You add tape cartridges as you need to archive your data.

Therefore, the correct answer is: Set up a Tape Gateway to back up your data in Amazon S3 and archive it in Amazon Glacier using your existing tape-based processes.
The option that says: Set up a Stored Volume Gateway to back up your data in Amazon S3 with point-in-time backups as EBS snapshots is incorrect. Stored Volume Gateway is not recommended for Tape archives, you should use Tape Gateway instead.
The option that says: Set up a Tape Gateway to back up your data in Amazon S3 with point-in-time backups as tapes which will be stored in the Virtual Tape Shelf is incorrect. The archival should be on Amazon Glacier for cost-effectiveness.
The option that says: Set up a File Gateway to back up your data in Amazon S3 and archive in Amazon Glacier using your existing tape-based processes is incorrect. A File Gateway is not recommended for Tape archives, you should use Tape Gateway instead.

References:
https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#storage-gateway-vtl-concepts
https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html
https://docs.aws.amazon.com/storagegateway/latest/userguide/create-tape-gateway.html

Check out this AWS Storage Gateway Cheat Sheet:
https://tutorialsdojo.com/aws-storage-gateway/

</details>

<a id="q4"></a>

## Q4

A company plans to migrate its on-premises workload to the AWS cloud. The solutions architect has been tasked to perform a Total Cost of Ownership (TCO) analysis and prepare a cost-optimized migration plan for the systems hosted in your on-premises network to AWS. It is required to collect detail about configuration, usage, and behavioral data from the on-premises servers to help better understand the current workloads before doing the migration.

Which of the following option is the recommended solution that should be implemented to meet the company requirements?

- **A.** Use the AWS SAM service to move your data to AWS which will also help you perform the TCO analysis.
- **B.** Use the AWS Migration Hub service to collect data from each server in your on-premises data center and perform the TCO analysis.
- **C.** Use the AWS Application Migration Service (MGN) to migrate VM servers to AWS and collect the data required to complete your TCO analysis.
- **D.** Use the AWS Application Discovery Service to gather data about your on-premises data center and perform the TCO analysis.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** TCO analysis before migration

⚠️ **Watch:** Not Migration Hub alone

🧠 **Rule:** Discover on-prem servers for TCO → Application Discovery Service

### TD explanation

AWS Application Discovery Service helps enterprise customers plan migration projects by gathering information about their on-premises data centers.
Planning data center migrations can involve thousands of workloads that are often deeply interdependent. Server utilization data and dependency mapping are important early first steps in the migration process. AWS Application Discovery Service collects and presents configuration, usage, and behavior data from your servers to help you better understand your workloads.

The collected data is retained in encrypted format in an AWS Application Discovery Service data store. You can export this data as a CSV file and use it to estimate the Total Cost of Ownership (TCO) of running on AWS and to plan your migration to AWS. In addition, this data is also available in AWS Migration Hub, where you can migrate the discovered servers and track their progress as they get migrated to AWS.
Therefore, the correct answer is: Use the AWS Application Discovery Service to gather data about your on-premises data center and perform the TCO analysis.
The option that says: Use the AWS SAM service to move your data to AWS which will also help you perform the TCO analysis is incorrect. The AWS Serverless Application Model (AWS SAM) service is just an open-source framework that you can use to build serverless applications on AWS. It is not a suitable migration service to be used for your on-premises systems.
The option that says: Use the AWS Migration Hub service to collect data from each server in your on-premises data center and performing the TCO analysis is incorrect. AWS Migration Hub simply provides a single location to track the progress of application migrations across multiple AWS and partner solutions. Using Migration Hub just allows you to choose the AWS and partner migration tools that best fits your needs while providing visibility into the status of migrations across your portfolio of applications. Although AWS Application Discovery Service can be integrated with AWS Migration Hub, this service alone is not enough to meet the requirement in this scenario.
The option that says: Use the AWS Application Migration Service (MGN) to migrate VM servers to AWS and collect the data required to complete your TCO analysis is incorrect. Although AWS Application Migration Service is a migration tool, it is used to replicate or mirror your on-premises VMs to the AWS cloud. It does not provide a helpful dashboard on applications running on each VM, unlike AWS Application Discovery Service.

References:
https://aws.amazon.com/application-discovery/
https://aws.amazon.com/server-migration-service/?nc=sn&loc=1
https://aws.amazon.com/cloud-migration/

Check out this AWS Application Migration (MGN) Service Cheat Sheet:
https://tutorialsdojo.com/aws-application-migration-service/

</details>

<a id="q5"></a>

## Q5

A company runs its legacy web application in its on-premises data center. The solutions architect has been tasked to move the legacy web application in a virtual machine running inside the data center to the Amazon VPC. However, this application requires a private and dedicated connection to a number of servers hosted on the on-premises network in order for it to work.

Which combination of options provides the most suitable way to configure the web application running inside the VPC to reach back and access its internal dependencies on the company’s on-premises network? (Select TWO.)

- **A.** An Internet Gateway to allow a VPN connection.
- **B.** A network device in your data center that supports Border Gateway Protocol (BGP) and BGP MD5 authentication.
- **C.** An AWS Direct Connect link between the VPC and the network housing the internal services.
- **D.** An Elastic IP address on the VPC instance.
- **E.** Set up a Transit VPC between your on-premises data center and your VPC.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C (you answered correctly)

🔑 **Key words:** VM needs on-prem dependencies, private connection

⚠️ **Watch:** DX needs BGP-capable device

🧠 **Rule:** Direct Connect requirements → BGP + MD5-capable router + DX link

### TD explanation

AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router.

With this connection, you can create virtual interfaces directly to public AWS services (for example, to Amazon S3) or to Amazon VPC, bypassing Internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the Region with which it is associated. You can use a single connection in a public Region or AWS GovCloud (US) to access public AWS services in all other public Regions.
The option that says: A network device in your data center that supports Border Gateway Protocol (BGP) and BGP MD5 authentication is correct as a network device that supports Border Gateway Protocol (BGP) and BGP MD5 authentication is needed to establish a Direct Connect link from your data center to your VPC.
The option that says: An AWS Direct Connect link between the VPC and the network housing the internal services is correct because Direct Connect sets up a dedicated connection between on-premises data center and Amazon VPC, and provides you with the ability to connect your on-premises servers with the instances in your VPC.
The option that says: An Internet Gateway to allow a VPN connection is incorrect as you normally create a VPN connection based on a customer gateway and a virtual private gateway (VPG) in AWS.
The option that says: An Elastic IP address on the VPC instance is incorrect because EIPs are not needed as the instances in the VPC can communicate with on-premises servers via their private IP address.
The option that says: Setting up a Transit VPC between your on-premises data center and your VPC is incorrect. Although a Transit VPC can establish a connection to your VPC and on-premises data center, this option is not suitable for this scenario. Remember that a Transit VPC just simplifies network management and minimizes the number of connections required to connect multiple VPCs and remote networks.

References:
https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html
https://docs.aws.amazon.com/directconnect/latest/UserGuide/getting_started.html#ConnectionRequest

Check out this AWS Direct Connect Cheat Sheet:
https://tutorialsdojo.com/aws-direct-connect/

</details>

<a id="q39"></a>

## Q39

A company has multiple database servers hosted on extra-large Reserved Amazon EC2 instances which are all deployed to a private subnet. A single NAT instance is in place to allow the servers to fetch data from the Internet. The solutions architect noticed that whenever there is a new database patch update, the processing takes a lot of time which results in request time-outs. As a workaround, the developers just manually re-run the database patch update on the servers that failed to complete the process the first time.

What could be the possible root cause of the issue and what steps should the solutions architect implement to solve it?

- **A.** The timeout behavior of a NAT instance is that, when there is a connection time out, it sends a FIN packet to resources behind the NAT instance to close the connection. It does not attempt to continue the connection which is why some database updates are failing. For better performance, use a NAT Gateway instead.
- **B.** There is no Internet Gateway (IGW) attached to the VPC. Simply add an IGW and the issue will be resolved.
- **C.** There is no Virtual Private Gateway attached to the VPC that links up to the Customer Gateway of the database provider. Simply add the missing gateway and the issue will be resolved
- **D.** The database servers are not in a Placement Group, which means that the inter-instance communications are not optimal. This is causing the timeout issue. Place all the database servers on either a Spread or a Cluster type Placement group to fix the problem.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** NAT instance, long-running DB update fails on timeout

⚠️ **Watch:** NAT gateway sends RST, NAT instance sends FIN

🧠 **Rule:** NAT instance timeout → FIN; replace with NAT gateway

### TD explanation

A NAT gateway is a Network Address Translation (NAT) service. You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.
The NAT gateway replaces the source IPv4 address of the instances with the private IP address of the NAT gateway. When sending response traffic to the instances, the NAT device translates the addresses back to the original source IPv4 addresses.

When you create a NAT gateway, you specify one of the following connectivity types:
Public – (Default) Instances in private subnets can connect to the internet through a public NAT gateway, but cannot receive unsolicited inbound connections from the internet. You create a public NAT gateway in a public subnet and must associate an elastic IP address with the NAT gateway at creation. You route traffic from the NAT gateway to the internet gateway for the VPC. Alternatively, you can use a public NAT gateway to connect to other VPCs or your on-premises network. In this case, you route traffic from the NAT gateway through a transit gateway or a virtual private gateway.
Private – Instances in private subnets can connect to other VPCs or your on-premises network through a private NAT gateway. You can route traffic from the NAT gateway through a transit gateway or a virtual private gateway. You cannot associate an elastic IP address with a private NAT gateway. You can attach an internet gateway to a VPC with a private NAT gateway, but if you route traffic from the private NAT gateway to the internet gateway, the internet gateway drops the traffic.

Take note of the following difference between a NAT Instance and a NAT Gateway when handling a timeout:
NAT Instance - When there is a connection time out, a NAT instance sends a FIN packet to resources behind the NAT instance to close the connection.
NAT Gateway - When there is a connection time out, a NAT gateway returns an RST packet to any resources behind the NAT gateway that attempt to continue the connection (it does not send a FIN packet).

Therefore, the correct answer is: The timeout behavior of a NAT instance is that, when there is a connection time out, it sends a FIN packet to resources behind the NAT instance to close the connection. It does not attempt to continue the connection which is why some database updates are failing. For better performance, use a NAT Gateway instead.
The option that says: There is no Internet Gateway (IGW) attached to the VPC. Simply add an IGW and the issue will be resolved is incorrect. If there is no Internet Gateway attached to the VPC, any communication to the outside internet will fail, which is not the case here.
The option that says: There is no Virtual Private Gateway attached to the VPC that links up to the Customer Gateway of the database provider. Simply add the missing gateway and the issue will be resolved is incorrect. A Virtual Private Gateway is used for VPN connections. This will not resolve the issue for this scenario.
The option that says: The database servers are not in a Placement Group, which means that the inter-instance communications are not optimal. This is causing the timeout issue. Place all the database servers on either a Spread or a Cluster type Placement group to fix the problem is incorrect. Placement groups are just allocation of servers to be as close together as possible. This does not improve the performance of the NAT instance.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

Tutorials Dojo's AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q47"></a>

## Q47

A company has recently finished developing a web application that will soon be put into production. Before it is transferred into the production environment, a final test run must be conducted. Only the employees can access the web app - either from the corporate network or from the Internet. The manager instructed the solutions architect to ensure that the EC2 instance hosting the application server will not be exposed to the Internet.

Which of the following options is the recommended implementation to fulfill the company requirements?

- **A.** 1. Use IPsec VPN that would allow your employees to access the network of your application servers. 2. Create a public subnet in your VPC and launch your application servers in it.
- **B.** 1. Use AWS Direct Connect to hook up your employee workstations to the VPC via a private interface. 2. Create a public subnet and place your application servers in it.
- **C.** 1. Configure SSL VPN on the public subnet of your VPC. 2. Install an SSL VPN client software on all employee workstations. 3. Create a private subnet in your VPC and place your application servers in it.
- **D.** 1. Launch an Elastic Load Balancer for your EC2 instances that terminates SSL to them. 2. Create a public subnet in your VPC and launch your application servers in it.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** employees only, from corporate network or home, not exposed

⚠️ **Watch:** Not public subnet + IP allow list

🧠 **Rule:** Remote employee access → SSL VPN in public subnet + app in private subnet

### TD explanation

In this scenario, you have a web application which is still under development but you want to enable access to it only for the employees via public Internet. In this scenario, you can implement an SSL VPN solution in which the employees can connect first and once they are authenticated, they will be granted access to the online portal. In this way, you can launch the web servers in the private subnet and still access it over the Internet via the VPN.

Therefore, the correct answer is:
1. Configure SSL VPN on the public subnet of your VPC.
2. Install an SSL VPN client software on all employee workstations.
3. Create a private subnet in your VPC and place your application servers in it.
The following option is incorrect. Even though an IPSec VPN may work, your application servers are still exposed since you launched them in a public subnet:
1. Use IPsec VPN that would allow your employees to access the network of your application servers.
2. Create a public subnet in your VPC and launch your application servers in it.
The following option is incorrect because you don't need to set up a DirectConnect connection in order to meet the requirement. Additionally, it is costly to maintain this connection considering that it is not required to have a high bandwidth connection between the customer and AWS:
1. Use AWS Direct Connect to hook up your employee workstations to the VPC via a private interface.
2. Create a public subnet and place your application servers in it.
The following option is incorrect because terminating the SSL on the EC2 instance does not meet the requirement.
1. Launch an Elastic Load Balancer for your EC2 instances that terminates SSL to them.
2. Create a public subnet in your VPC and launch your application servers in it.
The application servers are still exposed as it is deployed to a public subnet.

References:
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpn-connections.html
 https://aws.amazon.com/marketplace/pp/B00MI40CAE?qid=1532168886060&sr=0-1&ref_=srh_res_product_title

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

---

# Group G — Service fit & performance (5)

<a id="q11"></a>

## Q11

A company has recently migrated its core application to the AWS Cloud. The application allows users to upload scanned forms through a web application hosted on a fleet of Amazon EC2 instances. The application connects to a backend database hosted on Amazon RDS for PostgreSQL. The user metadata are stored on the database while the scanned forms are stored on an Amazon S3 bucket.

For each uploaded form, the application sends a notification to an Amazon SNS topic to which the team members are subscribed. Then, one of the team members will log in, validate the forms, and manually extracts relevant data from the scanned forms. This information is then submitted to another system using an API. The management wants to improve this process by automation to reduce human effort, increase efficiency and maintain high accuracy.

Which of the following options is the recommended solution to meet the company's requirements?

- **A.** Add another tier to the application by deploying an open-source optical character recognition (OCR) software on Amazon Elastic Kubernetes (Amazon EKS) to process the uploaded forms. Store the output in another Amazon S3 bucket. Parse the output and send it to an Amazon DynamoDB table. Update the application to get data from the DynamoDB table and send it to the other system via API call.
- **B.** Add another tier to the application by using AWS Step Functions and AWS Lambda to facilitate the different stages of processing. Implement an artificial intelligence and machine learning (AL/ML) service using Amazon Rekognition and Amazon Transcribe to parse information from the scanned forms. Store the output in Amazon DocumentDB. Update the application to parse data from the DocumentDB table and send it to the other system via API call.
- **C.** Add another tier to the application by deploying an artificial intelligence and machine learning (AL/ML) model trained using Amazon SageMaker service. Use this model to perform optical character recognition (OCR) on the uploaded forms. Store the output in another Amazon S3 bucket. Update the application to parse data from the Amazon S3 bucket and send it to the other system via API call.
- **D.** Add another tier to the application by using AWS Step Functions and AWS Lambda to facilitate the different stages of processing. Use a combination of Amazon Textract and Amazon Comprehend to perform optical character recognition (OCR) and parse data from the scanned forms. Store the output in another Amazon S3 bucket. Update the application to parse data from the Amazon S3 bucket and send it to the other system via API call.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** scanned forms, OCR, reduce human effort

⚠️ **Watch:** Rekognition is not document OCR

🧠 **Rule:** Forms OCR → Textract + Comprehend, orchestrated by Step Functions

### TD explanation

Amazon Textract is a fully managed machine learning service that automatically extracts printed text, handwriting, and other data from scanned documents that goes beyond simple optical character recognition (OCR) to identify, understand, and extract data from forms and tables.
Amazon Textract helps you add document text detection and analysis to your applications. Using Amazon Textract, you can do the following:
-Detect typed and handwritten text in a variety of documents, including financial reports, medical records, and tax forms.
-Extract text, forms, and tables from documents with structured data using the Amazon Textract Document Analysis API.
-Specify and extract information from documents using the Queries feature within the Amazon Textract Analyze Document API.
-Process invoices and receipts with the AnalyzeExpense API.
-Process ID documents, such as driver's licenses and passports issued by the U.S. government, using the AnalyzeID API.
-Upload and process mortgage loan packages through automatic routing of the document pages to the appropriate Amazon Textract analysis operations using the Analyze Lending workflow.
Amazon Comprehend uses natural language processing (NLP) to extract insights about the content of documents. It develops insights by recognizing the entities, key phrases, language, sentiments, and other common elements in a document. Use Amazon Comprehend to create new products based on understanding the structure of documents.
Amazon Comprehend uses machine learning to help you uncover the insights and relationships in your unstructured data. The service identifies the language of the text; extracts key phrases, places, people, brands, or events; understands how positive or negative the text is; analyzes text using tokenization and parts of speech; and automatically organizes a collection of text files by topic.

Therefore, the correct answer is: Add another tier to the application by using AWS Step Functions and AWS Lambda to facilitate the different stages of processing. Use a combination of Amazon Textract and Amazon Comprehend to perform optical character recognition (OCR) and parse data from the scanned forms. Store the output in another Amazon S3 bucket. Update the application to parse data from the Amazon S3 bucket and send it to the other system via API call.  Amazon Textract uses machine learning service that automatically extracts printed text, handwriting, and other data from scanned documents. Amazon Comprehend uses machine learning to find insights and relationships in text.
The option that says: Add another tier to the application by deploying an open-source optical character recognition (OCR) software on Amazon Elastic Kubernetes (Amazon EKS) to process the uploaded forms. Store the output in another Amazon S3 bucket. Parse the output and send it to an Amazon DynamoDB table. Update the application to get data from the DynamoDB table and send it to the other system via API call is incorrect. This may be possible but is not recommended as it will add operation overhead. The Amazon Textract and Comprehend services are better suited for this scenario.
The option that says: Add another tier to the application by using AWS Step Functions and AWS Lambda to facilitate the different stages of processing. Implement an artificial intelligence and machine learning (AL/ML) service using Amazon Rekognition and Amazon Transcribe to parse information from the scanned forms. Store the output in Amazon DocumentDB. Update the application to parse data from the DocumentDB table and send it to the other system via API call is incorrect. Amazon Rekognition is used for computer vision to extract information from images and videos, not for scanned text forms. Amazon Transcribe is used for automatic speech recognition or adding speech-to-text capabilities to applications.
The option that says: Add another tier to the application by deploying an artificial intelligence and machine learning (AL/ML) model trained using Amazon SageMaker service. Use this model to perform optical character recognition (OCR) on the uploaded forms. Store the output in another Amazon S3 bucket. Update the application to parse data from the Amazon S3 bucket and send it to the other system via API call is incorrect. This may be possible, however, this will require you to create and train a model for performing OCR. AWS already offers Textract and Comprehend services which are better suited for this scenario.

References:
https://docs.aws.amazon.com/textract/latest/dg/what-is.html
https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html
https://aws.amazon.com/blogs/machine-learning/building-an-nlp-powered-search-index-with-amazon-textract-and-amazon-comprehend/

Check out these AWS Textract and Amazon Comprehend Cheat Sheets:
https://tutorialsdojo.com/amazon-textract/
https://tutorialsdojo.com/amazon-comprehend/

</details>

<a id="q12"></a>

## Q12

A data analytics company is running simulations on a high-performance computing (HPC) cluster in AWS. The compute node and storage are tightly coupled to achieve the best performance possible. The running simulations on the cluster produce thousands of large files stored on an Amazon EFS share that is shared across 200 Amazon EC2 instances. Several more simulation jobs need to be run on the cluster so the number of nodes has been increased to 1000 instances. However, the bigger cluster performed below the expectations of the company. The Solutions Architect was tasked to implement a solution that will achieve maximum performance from the HPC cluster.

Which of the following options are the recommended actions to achieve this? (Select THREE.)

- **A.** Improve the performance by placing all the compute nodes as close to each other. Re-launch all the Amazon EC2 instances within a single Availability Zone in a cluster placement group.
- **B.** Improve the network performance of each node by attaching multiple network interfaces to the Amazon EC2 instances. This ensures that the network bandwidth is not a bottleneck.
- **C.** Improve the network performance of each node by using Amazon EC2 instances with an Elastic Fabric Adapter (EFA) network interface.
- **D.** Improve the performance and scalability of the HPC cluster by spreading the Amazon EC2 instances into multiple Availability Zones. Improve the storage performance by using Amazon EBS volumes configured on RAID 0 mode. This allows for much higher IOPS compared to Amazon EFS.
- **E.** Improve the storage performance by using Amazon EBS Throughput Optimized volumes configured on RAID 0 mode. This allows for much higher IOPS compared to Amazon EFS.
- **F.** Improve the storage performance by implementing Amazon FSx for Lustre instead of using Amazon EFS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, F (you answered correctly)

🔑 **Key words:** tightly coupled HPC, maximum performance

⚠️ **Watch:** EFS is not HPC scratch storage

🧠 **Rule:** HPC → cluster placement group + EFA + FSx for Lustre

### TD explanation

In this scenario, the shared Amazon EFS storage and the spreading of the compute nodes on multiple AZs cause sluggishness on both the storage and network performance of the HPC cluster. For a tightly-coupled HPC cluster, you want the Amazon EC2 instances to be launched on a single Availability Zone.

When you launch a new EC2 instance, the EC2 service attempts to place the instance in such a way that all of your instances are spread out across underlying hardware to minimize correlated failures. You can use placement groups to influence the placement of a group of interdependent instances to meet the needs of your workload. Depending on the type of workload, you can create a placement group using one of the following placement strategies:
Cluster – packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the low-latency network performance necessary for tightly-coupled node-to-node communication that is typical of HPC applications.
Partition – spreads your instances across logical partitions such that groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions. This strategy is typically used by large distributed and replicated workloads, such as Hadoop, Cassandra, and Kafka.
Spread – strictly places a small group of instances across distinct underlying hardware to reduce correlated failures.
Elastic Fabric Adapter (EFA) is a network interface for Amazon EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS. Its custom-built operating system (OS) bypass hardware interface enhances the performance of inter-instance communications, which is critical to scaling these applications. EFA’s unique OS bypass networking mechanism provides a low-latency, low-jitter channel for inter-instance communications. This enables your tightly-coupled HPC or distributed machine learning applications to scale to thousands of cores, making your applications run faster.

Amazon FSx for Lustre makes it easy and cost-effective to launch and run the popular, high-performance Lustre file system. You use Lustre for workloads where speed matters, such as machine learning, high-performance computing (HPC), video processing, and financial modeling. Amazon FSx file systems provide up to multiple GB/s of throughput and hundreds of thousands of IOPS. The specific amount of throughput and IOPS that your workload can drive on your file system depends on the throughput capacity and storage capacity configuration of your file system, along with the nature of your workload, including the size of the active working set.
The open-source Lustre file system is designed for applications that require fast storage—where you want your storage to keep up with your computing capacity. Lustre was built to solve the problem of quickly and cheaply processing the world's ever-growing datasets. It's a widely used file system designed for the fastest computers in the world. It provides submillisecond latencies, up to hundreds of Gbps of throughput, and up to millions of IOPS.
Therefore, the correct answers are:
- Improve the performance by placing all the compute nodes as close to each other. Re-launch all the Amazon EC2 instances within a single Availability Zone in a cluster placement group.
- Improve the network performance of each node by using Amazon EC2 instances with an Elastic Fabric Adapter (EFA) network interface.
- Improve the storage performance by implementing Amazon FSx for Lustre instead of using Amazon EFS.
The option that says: Improve the network performance of each node by attaching multiple network interfaces to the Amazon EC2 instances. This ensures that the network bandwidth is not a bottleneck is incorrect. Although this may increase the network performance of the individual compute node, the Amazon EFS could still be a bottleneck because there are too many instances accessing the EFS shared storage simultaneously. A better solution is to use Amazon FSx for Lustre which supports multiple GB/s of throughput and hundreds of thousands of IOPS.
The option that says: Improve the performance and scalability of the HPC cluster by spreading the Amazon EC2 instances into multiple Availability Zones is incorrect. The HPC cluster relies on tight communication between the compute nodes and the storage solution. Spreading the EC2 instances into multiple Availability Zones will lower the performance of the cluster because the underlying physical servers will have to communicate with each other over long distances.
The option that says: Improve the storage performance by using Amazon EBS Throughput Optimized volumes configured on RAID 0 mode. This allows for much higher IOPS compared to Amazon EFS is incorrect. The cluster relies on shared storage across all the compute nodes. A Throughput Optimized EBS volume cannot be shared between EC2 instances. The Amazon EBS Multi-Attach feature is only applicable for Provisioned IOPS SSD volumes.

References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html
https://aws.amazon.com/hpc/efa/
https://aws.amazon.com/fsx/lustre/
https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html

Check out the Amazon FSx Cheat Sheet:
https://tutorialsdojo.com/amazon-fsx/

</details>

<a id="q25"></a>

## Q25

A travel booking company runs its main web application on the AWS cloud. Its trip planner website provides timetables, travel alerts, and other public transportation information for trains, buses, ferries, and trams. The front-end tier is composed of an ALB in front of an Auto Scaling group of Amazon EC2 instances deployed across 3 Availability Zones and a Multi-AZ RDS for its database tier. When there are sporting events and popular concerts to be held in a city, the usage of the trip planner application spikes which causes the application servers to reach utilization of over 90%. The solutions architect must ensure that the website can quickly recover in the event that one of its Availability Zones failed during its peak usage.

Which of the following is the most cost-effective architectural design that should be implemented for this website to maintain high availability?

- **A.** Increase the capacity and scaling thresholds of the Auto Scaling group to allow the application servers to scale up across all Availability Zones, which will lower the aggregate utilization of the EC2 instances. Use Reserved Instances to handle the steady-state load and a combination of On-Demand and Spot Instances to process the peak load. When the peak usage is over, scale down the number of the On-Demand and Spot instances.
- **B.** Deploy six Reserved and Spot EC2 Instances in each of the 3 Availability Zones. In this way, the remaining two Availability Zones can handle the load left behind by the Availability Zone that went down.
- **C.** Deploy one On-Demand EC2 instance and two Spot EC2 Instances in each of the 3 Availability Zones. In case that one Availability Zone fails, the remaining two Availability Zones can handle the peak load.
- **D.** To have the most cost-effective architecture, replace all of the Reserved and On-Demand EC2 instances with Spot instances across all Availability Zones. Configure an Auto Scaling group in one of the AZs for scalability.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** steady-state + peaks, most cost-effective, HA

⚠️ **Watch:** Not all On-Demand

🧠 **Rule:** Steady state → Reserved; peaks → Auto Scaling

### TD explanation

Remember that Spot Instances are the most cost-effective type of instances that you can choose. However, this is not suitable for applications with steady state usage.
Amazon EC2 Spot instances allow you to request spare Amazon EC2 computing capacity for up to 90% off the On-Demand price. Spot instances are recommended for:
- Applications that have flexible start and end times
- Applications that are only feasible at very low compute prices
- Users with urgent computing needs for large amounts of additional capacity

On-Demand instances are recommended for:
- Users that prefer the low cost and flexibility of Amazon EC2 without any up-front payment or long-term commitment
- Applications with short-term, spiky, or unpredictable workloads that cannot be interrupted
- Applications being developed or tested on Amazon EC2 for the first time
Reserved Instances are recommended for:
- Applications with steady state usage
- Applications that may require reserved capacity
- Customers that can commit to using EC2 over a 1 or 3 year term to reduce their total computing costs
The option that says: Increase the capacity and scaling thresholds of the Auto Scaling group to allow the application servers to scale up across all Availability Zones, which will lower the aggregate utilization of the EC2 instances. Use Reserved Instances to handle the steady-state load and a combination of On-Demand and Spot Instances to process the peak load. When the peak usage is over, scale down the number of the On-Demand and Spot instances is correct because by using Auto Scaling, you allow the application servers to scale up across all Availability Zones and handle the additional load. The combination of On-Demand and Spot Instances to process the peak load is a cost-effective solution because when the peak usage is over, you can scale down the number of your instances to save costs.
The option that says: Deploy six Reserved and Spot EC2 Instances in each of the 3 Availability Zones. In this way, the remaining two Availability Zones can handle the load left behind by the Availability Zone that went down is incorrect because having 6 Reserved Instances are still costly even if you add a Spot instance on each Availability Zone. You should also use an Auto Scaling group in order to properly scale your compute resources in accordance with your incoming traffic.
The option that says: Deploy one On-Demand EC2 instance and two Spot EC2 Instances in each of the 3 Availability Zones. In case that one Availability Zone fails, the remaining two Availability Zones can handle the peak load is incorrect because although this is a cost-effective solution, it doesn't use Auto Scaling and hence, the availability of the website is at risk. If the On-Demand instance fails then the Availability Zone is only left with 2 Spot instances, which would not be able to handle the steady state usage.
The option that says: To have the most cost-effective architecture, replace all of the Reserved and On-Demand EC2 instances with Spot instances across all Availability Zones. Configure an Auto Scaling group in one of the AZs for scalability is incorrect because although this is the most cost-effective solution, it is also the most unstable one considering that a Spot instance can be interrupted and hence, the availability of the website is compromised.

References:
https://aws.amazon.com/ec2/pricing
https://aws.amazon.com/ec2/spot/

Check out this Amazon EC2 Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

</details>

<a id="q36"></a>

## Q36

A company is running a financial modeling application on the AWS cloud. The application tier runs on an Auto Scaling group of Amazon EC2 instances. A separate EC2 cluster with a fixed number of instances is hosting the 200 TB of financial data in a shared file system. The application reads and processes the data on the shared filesystem to generate an overall financial report, which takes about 72 hours to complete. This whole process only needs to run at the end of each month, but the storage tier instances are running continuously to retain all the data in the shared file system.

As the storage tier takes up a large percentage of operational costs, the management wants to reduce the cost of the storage tier while maintaining the high-performance access needed by the application during its 72-hour run.

Which of the following options should the solutions architect implement that will have the largest overall cost reduction?

- **A.** For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Intelligent-Tiering Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed.
- **B.** For the data tier, create an Amazon EFS filesystem and move the objects of the existing shared file system to it. Since the data will only be used once a month, use EFS Standard–Infrequent Access (IA) class to save costs. Mount this filesystem as shared storage for the application tier EC2 instance for the duration of the job.
- **C.** For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Glacier Instant Retrieval Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed.
- **D.** For the data tier, use Mountpoint for Amazon S3 to access the financial data directly from an S3 bucket. This will eliminate the need for a shared file system and reduce costs. Mount the S3 bucket on the application tier EC2 instances and run the job directly from it.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** 200 TB shared FS, 72-hour runs, largest cost reduction

⚠️ **Watch:** Not keeping the always-on EC2 file cluster

🧠 **Rule:** Data in S3 Intelligent-Tiering + lazy-loaded FSx for Lustre per run

### TD explanation

Amazon FSx for Lustre is a large-scale, distributed parallel file system powering the workloads of most of the largest supercomputers. It is popular among AWS customers for high-performance computing workloads, such as meteorology, life science, and engineering simulations. It is also used in media and entertainment, as well as the financial services industry. If your workloads require fast, POSIX-compliant file system access to your S3 buckets, then you can use FSx for Lustre to link your S3 buckets to a file system and keep data synchronized between the file system and S3 in both directions.
Amazon FSx for Lustre offers a choice of solid-state drive (SSD) and hard disk drive (HDD) storage types that are optimized for different data processing requirements.
FSx for Lustre integrates with Amazon S3, making it easier for you to process cloud datasets using the Lustre high-performance file system. When linked to an Amazon S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files. Amazon FSx imports listings of all existing files in your S3 bucket at file system creation. Amazon FSx can also import listings of files added to the data repository after the file system is created. You can set the import preferences to match your workflow needs. The file system also makes it possible for you to write file system data back to S3. Data repository tasks simplify the transfer of data and metadata between your FSx for Lustre file system and its durable data repository on Amazon S3.

Therefore, the correct answer is: For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Intelligent-Tiering Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed. The FSx for Lustre filesystem can temporarily load the data from S3 and share it among the application tier instances. This is cheaper as we can use S3 for long-term storage and FSx for Lustre for the temporary shared file system.
The option that says: For the data tier, create an Amazon EFS filesystem and move the objects of the existing shared file system to it. Since the data will only be used once a month, use EFS Standard–Infrequent Access (IA) class to save costs. Mount this filesystem as shared storage for the application tier EC2 instance for the duration of the job is incorrect. Amazon EFS Filesystem costs significantly more than standard Amazon S3 storage costs.
The option that says: For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Glacier Instant Retrieval Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed is incorrect. S3 Glacier is typically recommended for long-lived archive data accessed once a quarter. Also, S3 Glacier has additional charges for retrieving data from cold storage.
The option that says: For the data tier, use Mountpoint for Amazon S3 to access the financial data directly from an S3 bucket. This will eliminate the need for a shared file system and reduce costs. Mount the S3 bucket on the application tier EC2 instances and run the job directly from it is incorrect because Mountpoint for Amazon S3 is optimized for read-heavy workloads with sequential access patterns, but it does not offer the high-throughput, low-latency performance required for intensive data processing like financial modeling. It lacks POSIX compliance and does not support full file system semantics, which may cause compatibility issues with applications expecting traditional shared file systems. Additionally, it doesn’t primarily support parallel access with the same efficiency as FSx for Lustre.

References:
https://aws.amazon.com/blogs/storage/persistent-storage-for-high-performance-workloads-using-amazon-fsx-for-lustre/
https://aws.amazon.com/blogs/aws/enhanced-amazon-s3-integration-for-amazon-fsx-for-lustre/
https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html

Check out these Amazon S3 and Amazon FSx for Lustre Cheat Sheets:
https://tutorialsdojo.com/amazon-s3/
https://tutorialsdojo.com/amazon-efs-vs-amazon-fsx-for-windows-vs-amazon-fsx-for-lustre/

</details>

<a id="q49"></a>

## Q49

A national library is planning to store around 50 TB of data containing all books, articles, and other written materials in AWS. One of the requirements is to have a search feature to enable users to look for the collection on a dynamic website. The library also uses Amazon Pinpoint for user email notifications.

What is the most suitable solution to implement in AWS to satisfy the required functionality?

- **A.** Use AWS Elastic Beanstalk as the deployment service. Deploy the needed AWS resources, such as the Multi-AZ Amazon RDS for storage and an Amazon EC2 instance to host their website.
- **B.** Utilize AWS CloudFormation as the deployment service to deploy the needed AWS resources such as an Amazon S3 bucket for storage, OpenSearch to provide the needed search functionality, and an Amazon EC2 instance to host their website.
- **C.** Use AWS CodePipeline as the deployment service to deploy Amazon Kinesis as the storage service and an Amazon EC2 instance to serve their website.
- **D.** Use Amazon CodeDeploy as the deployment service to deploy two Amazon S3 buckets, in which the first one serves as the storage service and the second one for hosting their dynamic website. Use the native search functionality of S3 to satisfy the search feature requirement.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** 50 TB, search on a website

⚠️ **Watch:** Not RDS full-text search

🧠 **Rule:** Search feature → OpenSearch; storage → S3

### TD explanation

Amazon S3 offers a highly durable, scalable, and secure destination for backing up and archiving your critical data. You can use S3’s versioning capability to provide even further protection for your stored data. Whether you’re storing pharmaceutical or financial data, or multimedia files such as photos and videos, Amazon S3 can be used as your data lake for big data analytics.
Amazon OpenSearch Service is a fully managed service that enables interactive search, real-time analytics, and logging on large datasets. It is ideal for providing search functionality for applications like a dynamic website that needs to index and query vast amounts of data, such as books and articles in this case. OpenSearch supports full-text search, faceting, and filtering, making it a perfect match for the library’s requirement to search their collection.
Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic.

Amazon S3 is great for storage, but it lacks an effective search feature. Hence, it is better to use a service like Amazon OpenSearch Service to fulfill the requirements in the scenario.
Therefore, the correct answer is: Utilize AWS CloudFormation as the deployment service to deploy the needed AWS resources such as an Amazon S3 bucket for storage, OpenSearch to provide the needed search functionality, and an Amazon EC2 instance to host their website.
The option that says: Use AWS Elastic Beanstalk as the deployment service. Deploy the needed AWS resources, such as the Multi-AZ Amazon RDS for storage and an Amazon EC2 instance to host their website is incorrect. You can simply use RDS as your database for the application; however, this will be very expensive. It is recommended to use the Amazon OpenSearch service instead to have a cost-effective search solution for the website application.
The option that says: Use AWS CodePipeline as the deployment service to deploy Amazon Kinesis as the storage service and an Amazon EC2 instance to serve their website is incorrect. Although AWS CodePipeline is useful for automating release pipelines, it's not designed to handle the complexities of deploying and managing applications. Additionally, though Amazon Kinesis is typically great for real-time data streaming, it's not an ideal long-term storage service.
The option that says: Use Amazon CodeDeploy as the deployment service to deploy two Amazon S3 buckets, in which the first one serves as the storage service and the second one for hosting their dynamic website. Use the native search functionality of S3 to satisfy the search feature requirement is incorrect. You cannot host the dynamic application on Amazon S3, and there is no built-in search feature on Amazon S3 that will satisfy the application requirements.

References:
https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html
https://aws.amazon.com/what-is-cloud-object-storage/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html

Check out this Amazon OpenSearch Service Cheat Sheet:
https://tutorialsdojo.com/amazon-opensearch-service/

</details>
