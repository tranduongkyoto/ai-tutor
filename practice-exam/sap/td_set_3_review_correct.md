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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 ASG (web tier) ──► RDS PostgreSQL (DB tier)
         spike user traffic + bursty writes (sale event)
Yêu cầu: KHÔNG đổi data model, không mất submission nào
```

Đáp án đúng: **B** — chèn Amazon SQS queue giữa app và DB, dùng Lambda tiêu thụ queue và viết vào database. Anh chọn đúng B.

#### Vì sao B đúng

- SQS là message queue fully managed, lưu message bền (durable) trên nhiều AZ → **không mất submission** dù traffic tăng đột biến và không đoán trước được.
- SQS scale co giãn theo nhu cầu — không giới hạn số message/queue, standard queue throughput gần như không giới hạn → chịu được "sudden spike and unpredictable traffic".
- Lambda làm consumer, pull message theo tốc độ DB chịu được rồi ghi vào RDS PostgreSQL → **không cần đổi data model**, DB vẫn là PostgreSQL với schema như cũ.
- Về bản chất đây là decouple: tốc độ ghi của app tách khỏi tốc độ xử lý của DB, SQS đóng vai trò bộ đệm hấp thụ spike.

#### Vì sao từng đáp án sai bị loại

- **A sai**: scale DB instance lên size lớn hơn bằng tay — đề không nói RDS có Multi-AZ, nên quá trình scale có thể gây downtime ngắn; hơn nữa traffic không đoán trước được, không đảm bảo instance lớn hơn là đủ.
- **C sai**: migrate từ RDS sang DynamoDB đòi hỏi thay đổi lớn ở cả application layer và database layer — vi phạm trực tiếp yêu cầu "without changing the underlying data model".
- **D sai**: ElastiCache được thiết kế để cache các request đọc lặp lại (frequent reads), **không phải** để giữ data đang chờ ghi vào DB — dùng sai mục đích của cache layer.

#### Lưu ý thực tế

⚠️ **Dễ nhầm** — cùng dạng câu hỏi với Q24 (đã trả lời sai): Q24 cũng là "bursty writes vào một backend chậm, cần cost-effective" và đáp án đúng cũng là SQS buffer + consumer flush dữ liệu dần vào DB. Khi thấy "viết dữ liệu dồn ứ, backend không theo kịp, không đổi kiến trúc dữ liệu" → luôn nghĩ tới **SQS làm bộ đệm ghi**, không phải scale cứng DB, không phải đổi database engine, và tuyệt đối không dùng ElastiCache cho mục đích buffer ghi.

#### Quy tắc nhớ cho thi

- **"Bursty/unpredictable writes, không đổi data model"** → **SQS queue + Lambda/consumer ghi vào DB**
- **ElastiCache** → chỉ dùng để cache **đọc** (reads), không phải buffer **ghi** (writes)
- **Migrate database engine** → chỉ chọn khi đề thực sự cho phép thay đổi lớn ở cả app và data layer

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Input images ──► EC2 (1 host, EBS volume) ──► processed results
             số file input tăng dần, peak vài giờ/ngày
             xử lý tốn tới 20 giờ/ngày (gần hết thời gian)

Yêu cầu: giảm processing time + tăng availability
```

Đáp án đúng: **B** — lưu I/O file trên S3, dùng SQS để điều phối một nhóm host xử lý song song, đặt các host trong Auto Scaling group scale theo **độ dài hàng đợi SQS**. Anh chọn đúng B.

#### Vì sao B đúng

- **S3** thay cho EBS volume: S3 high availability, scale được dung lượng khổng lồ mà một EBS volume gắn trên 1 instance không làm được — đúng yêu cầu "improve the availability".
- **SQS** phân phối công việc (từng file/batch) cho **nhiều host xử lý song song** thay vì 1 instance đơn lẻ → giảm processing time đáng kể vì công việc được chia nhỏ, chạy đồng thời.
- **Auto Scaling group scale theo SQS queue length**: khi input file tăng (peak hours), queue dài ra → ASG thêm instance xử lý; khi queue ngắn lại → scale in. Đây là cơ chế scale đúng với bài toán "batch processing growing over time, peaks for a few hours".

#### Vì sao từng đáp án sai bị loại

- **A sai**: dùng EBS Provisioned IOPS (vẫn là block storage gắn 1 instance, không giúp nhiều host cùng truy cập file) + SNS để điều phối nhóm host — SNS là dịch vụ **notification**, không có khái niệm hàng đợi để cân bằng tải xử lý giữa các host, và cũng không dùng làm metric scale.
- **C sai**: vẫn dùng EBS (storage, không giúp parallel access nhiều host) dù scale theo SQS queue length — storage layer vẫn là điểm nghẽn.
- **D sai**: S3 đúng nhưng lại dùng SNS để điều phối song song và scale theo **số lượng SNS notification** — SNS chỉ push notification, không phải cơ chế hàng đợi công việc hay scaling metric phù hợp.

#### So sánh nhanh

| Đáp án | Storage | Điều phối song song | Scale theo |
|---|---|---|---|
| **B (đúng)** | S3 | SQS | SQS queue length |
| A | EBS PIOPS | SNS | số SNS notification |
| C | EBS PIOPS | SNS | SQS queue length |
| D | S3 | SQS | số SNS notification |

#### Lưu ý thực tế

⚠️ **Dễ nhầm** — cùng nhóm ý tưởng với Q21 và Q27 (và đối lập với Q24, đã trả lời sai): hễ đề có "nhiều worker/host cần chia việc, chịu tải biến động" thì **SQS luôn là cơ chế điều phối + scale**, còn **SNS chỉ để thông báo (fan-out), không bao giờ là scaling metric hay cơ chế hàng đợi**. Đừng nhầm hai dịch vụ này chỉ vì cả hai đều viết tắt "SxS" quen mắt.

#### Quy tắc nhớ cho thi

- **"Nhiều host xử lý song song, scale theo tải công việc"** → **SQS + ASG scale theo queue length**
- **SNS** → chỉ dùng cho pub/sub notification, không phải cơ chế điều phối việc hay metric để scale
- **"Giảm processing time + tăng availability cho file I/O"** → chuyển từ EBS (1 instance) sang **S3** (shared, scalable, highly available)

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
App (high usage load) ──write──► DynamoDB table
                                   │
                              bị throttled khi tải cao → mất dữ liệu

Yêu cầu: giảm tải lên table, KHÔNG mất data, MOST cost-effective
```

Đáp án đúng: **D** — dùng SQS queue để decouple message giữa application và database. Anh chọn đúng D.

#### Vì sao D đúng

- SQS hoạt động như một "bộ đệm" tạm giữ toàn bộ write request: khi DynamoDB bị throttle (do vượt WCU được provision), message vẫn nằm an toàn trong queue thay vì bị mất.
- Một loader process rút message ra khỏi queue và ghi vào DynamoDB theo tốc độ table chịu được → traffic ghi được "làm mượt" (smooth out), table không còn bị spike đột ngột.
- Đây là giải pháp **rẻ nhất** trong 4 lựa chọn: SQS tính phí theo số request, không cần tăng capacity cố định hay nhân bản tài nguyên — đúng với yêu cầu "MOST cost-effective".

#### Vì sao từng đáp án sai bị loại

- **A sai**: Global Tables dùng cho **multi-region fault tolerance**, không liên quan đến giảm tải ghi trên table hiện tại — sai mục đích sử dụng tính năng.
- **B sai**: tăng WCU provisioned là giải pháp **khả thi về kỹ thuật nhưng đắt** — tăng capacity là trả tiền trực tiếp cho throughput, không phải cách tối ưu chi phí mà đề yêu cầu.
- **C sai**: tạo thêm table để chia tải là anti-pattern — DynamoDB không hỗ trợ JOIN, nên phải tự đồng bộ dữ liệu giữa các table ở application layer, tốn nhiều effort phát triển và vẫn không rẻ hơn.

#### So sánh nhanh

| Đáp án | Cách giảm tải | Chi phí | Vấn đề |
|---|---|---|---|
| **D (đúng)** | SQS buffer trước DynamoDB | Thấp | Không |
| B | Tăng WCU | Cao | Trả tiền trực tiếp cho throughput |
| C | Thêm table | Trung-cao | Phải tự sync + không JOIN được |
| A | Global Tables | Cao | Sai mục đích (multi-region, không giảm tải) |

#### Lưu ý thực tế

⚠️ **Dễ nhầm** — cùng pattern với Q21 và Q22: bất cứ khi nào DynamoDB/RDS bị throttle do ghi dồn, phản xạ đúng luôn là **thêm SQS trước database** để làm bộ đệm, không phải tăng capacity cứng (WCU/instance size) hay tách bảng/engine. "MOST cost-effective" trong đề SAP-C02 gần như luôn loại các lựa chọn tăng tiền trực tiếp (WCU, nhiều table, nhiều region) để ưu tiên giải pháp decouple bằng queue.

#### Quy tắc nhớ cho thi

- **"DynamoDB throttled, không mất data, cost-effective"** → **SQS queue** trước table
- **Global Tables** → chỉ cho multi-region DR/latency, không giải quyết throttling
- **Tăng WCU / thêm table** → luôn là lựa chọn "khả thi nhưng đắt/anti-pattern", gần như luôn bị loại khi đề hỏi "MOST cost-effective"

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Global users ──► ALB ──► ASG EC2 (app) ──► RDS
                              │
                      S3 static web interface

Load time hiện tại ~7s, mục tiêu < 3s
Yêu cầu: MOST cost-effective, chọn ĐÚNG HAI giải pháp
```

Đáp án đúng: **A, C** — thêm caching layer bằng ElastiCache cho session + query thường xuyên, VÀ cho CloudFront cache nội dung tái sử dụng được. Anh chọn đúng A, C.

#### Vì sao A và C đúng — hai lớp cache bù trừ cho nhau

- **A — ElastiCache**: lưu session và các câu query DB lặp đi lặp lại → giảm tải lên RDS, tăng read performance. Việc này giải quyết phần "backend chậm vì DB phải xử lý nhiều".
- **C — CloudFront cache reusable content**: mạng edge location toàn cầu giúp người dùng khắp nơi (global audience) lấy nội dung tĩnh/tái sử dụng được gần họ hơn, giảm latency mạng. Việc này giải quyết phần "người dùng toàn cầu, xa origin".
- Hai giải pháp này **không chồng chéo**: một xử lý tầng database, một xử lý tầng network delivery toàn cầu — kết hợp lại vừa giảm tải backend vừa giảm khoảng cách vật lý, đúng yêu cầu "MOST cost-effective" vì không cần build thêm hạ tầng nặng (region mới, instance lớn hơn).

#### Vì sao từng đáp án sai bị loại

- **B sai**: hạ ngưỡng scale-up ASG xuống 30% CPU chỉ làm tăng **số lượng web server**, hoàn toàn không giảm tải lên database — không cải thiện read performance, vốn là nguyên nhân chính gây chậm.
- **D sai**: dựng thêm installation ở region khác + Route 53 latency-based routing — về mặt kỹ thuật có thể giảm latency, nhưng **không cải thiện read performance** của DB và **làm tăng chi phí** đáng kể (double infra) — vi phạm "MOST cost-effective".
- **E sai**: AWS Systems Manager State Manager dùng để **quản lý cấu hình** của EC2/on-premises server (patch, firewall, antivirus...), hoàn toàn không liên quan đến scale hay cải thiện tốc độ tải trang — sai mục đích dịch vụ.

#### Lưu ý thực tế

⚠️ **Dễ nhầm** — đối lập trực tiếp với Q30 (đã trả lời sai): Q30 cũng là bài toán "giảm latency nhanh và rẻ" và đáp án đúng cũng là **thêm ElastiCache trước database** — không phải migrate database sang engine khác, không phải build thêm region. Ở đây, Q40 mở rộng thêm lớp CloudFront vì có yêu cầu "global audience". Ghi nhớ: **ElastiCache luôn là lựa chọn nhanh/rẻ để giảm tải DB — không bao giờ là "nâng cấp/migrate database"**.

#### Quy tắc nhớ cho thi

- **"Giảm page load time, cost-effective"** → **ElastiCache** (giảm tải DB) + **CloudFront** (giảm khoảng cách mạng cho global users)
- **Hạ ngưỡng scale ASG** → chỉ thêm web server, không giúp DB bớt tải
- **Multi-region + Route 53 latency routing** → đắt, không giải quyết gốc vấn đề read performance
- **SSM State Manager** → config management, không liên quan tới scaling/performance tuning

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem Linux website ──► 5GB game package ──► triệu người dùng toàn cầu download

Hiện tại: data center on-premises
Yêu cầu: giải pháp mới, cost-effective + download nhanh BẤT KỂ vị trí người dùng
```

Đáp án đúng: **C** — tạo S3 bucket (website hosting) chứa file game, đặt CloudFront distribution với origin là S3 bucket, Route 53 trỏ vào CloudFront. Anh chọn đúng C.

#### Vì sao C đúng

- **S3** lưu file 5GB với chi phí lưu trữ rất thấp so với hạ tầng EC2/EBS/EFS, và scale tự động theo số lượng request mà không cần provision trước.
- **CloudFront** nhân bản nội dung ra các edge location toàn cầu — khi người dùng ở bất kỳ đâu request file, CloudFront phục vụ từ edge gần nhất, đảm bảo tốc độ download nhất quán "regardless of their location", đúng trọng tâm đề bài.
- **Route 53** chỉ đơn giản trỏ domain về CloudFront distribution — không có logic phụ, không tăng chi phí.
- Tổng thể: đây là kiến trúc **rẻ nhất và nhanh nhất** cho bài toán "large file, global mass download".

#### Vì sao từng đáp án sai bị loại

- **A sai**: EC2 ASG + EBS volume mỗi instance + ALB — khả thi nhưng **rất đắt** (phải gắn EBS cho từng instance) và **chỉ nằm trong 1 region**, người dùng xa region đó sẽ download chậm hơn.
- **B sai**: EC2 ASG + **EFS** (mount shared volume) + **Network Load Balancer** — EFS thường đắt hơn S3 cho use case này, và NLB cũng là dịch vụ chi phí cao; không hợp lý so với bài toán chỉ cần phân phối file tĩnh.
- **D sai**: S3 + "Requestor Pays" — tính năng này yêu cầu **người request phải có AWS account riêng** để trả phí download, hoàn toàn không phù hợp với việc public beta game cho triệu người dùng ẩn danh trên Internet tải miễn phí.

#### So sánh nhanh

| Đáp án | Lưu trữ | Phân phối | Vấn đề |
|---|---|---|---|
| **C (đúng)** | S3 | CloudFront (global edge) | Không |
| A | EBS/instance | ALB (1 region) | Đắt, chỉ 1 region |
| B | EFS | NLB (1 region) | EFS + NLB đắt hơn cần thiết |
| D | S3 + Requestor Pays | Trực tiếp S3 | Cần AWS account để download — sai use case |

#### Lưu ý thực tế

- "Requestor Pays" chỉ hợp lý khi người tải file **đã có AWS account** và chấp nhận trả phí data transfer (ví dụ dataset chia sẻ giữa các tổ chức), không áp dụng cho public, anonymous mass download như game release.
- CloudFront + S3 website endpoint là pattern chuẩn cho "static content, global distribution, high download volume" trong SAP-C02.

#### Quy tắc nhớ cho thi

- **"Large file, millions of global downloads, cost-effective"** → **S3 + CloudFront + Route 53**
- **EC2 + EBS/EFS + ALB/NLB** cho file tĩnh → luôn đắt hơn và kém global hơn S3+CloudFront, gần như luôn là bẫy
- **"Requestor Pays"** → chỉ dùng khi downloader có AWS account, không dùng cho public anonymous traffic

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users ──query string (thứ tự/chữ hoa-thường khác nhau)──► CloudFront ──miss──► Origin

parameter1=A&parameter2=b   và   parameter2=b&parameter1=a
     → CloudFront coi là 2 request KHÁC NHAU → cache hit ratio giảm dần
```

Đáp án đúng: **A** — viết Lambda@Edge function để sắp xếp query parameter theo alphabet và chuyển hết về chữ thường, deploy function với trigger "viewer request". Anh chọn đúng A.

#### Vì sao A đúng

- CloudFront cache theo **từng biến thể giá trị tham số** — nếu forward query string, nó coi `parameter1=A` và `parameter1=a` là 2 object khác nhau, tương tự thứ tự tham số khác nhau cũng tạo cache entry riêng. Đây chính là nguyên nhân cache hit ratio giảm trong đề.
- **Lambda@Edge** chạy code tùy biến tại edge location, gần viewer hơn origin → có thể "chuẩn hoá" (normalize) query string: sắp xếp alphabet theo tên tham số + đổi hết về lowercase, **trước khi** CloudFront xử lý cache key.
- Trigger **"viewer request"**: đây là thời điểm request vừa đến edge, trước khi CloudFront tra cache — normalize ở đây đảm bảo CloudFront nhìn thấy cùng một dạng query string cho các request về logic tương đương, từ đó match đúng cache entry đã có, tăng hit ratio.

#### Vì sao từng đáp án sai bị loại

- **B sai**: bỏ hẳn caching theo query string parameter → CloudFront sẽ cache mà **không phân biệt tham số**, nghĩa là có thể trả về **sai nội dung cached** cho các request có tham số khác nhau về mặt logic (không chỉ khác case/order) — giải quyết sai vấn đề, gây lỗi dữ liệu.
- **C sai**: đặt reverse proxy để normalize tham số **bên trong VPC gần origin** — nhưng tại thời điểm request đi tới proxy này, CloudFront **đã forward request tới origin rồi** (vì cache miss xảy ra trước khi proxy xử lý) → không hề cải thiện cache hit ratio, mất hết ý nghĩa của việc có CloudFront cache.
- **D sai**: không có tùy chọn "case insensitive" nào cho query string trong CloudFront — CloudFront luôn case-sensitive khi cache object; đáp án này dựa trên một tính năng không tồn tại.

#### Lưu ý thực tế

⚠️ **Watch** — đừng nhầm "tăng TTL" hay "thêm origin" với bài toán này: nguyên nhân cache miss ở đây là **sự không nhất quán của chính query string** (thứ tự + case), không phải do TTL ngắn hay origin chậm — nên giải pháp đúng luôn xoay quanh việc chuẩn hoá request *trước khi* CloudFront tra cache, cụ thể là ở bước "viewer request" của Lambda@Edge.

#### Quy tắc nhớ cho thi

- **"Query string khác thứ tự/case → cache hit ratio giảm"** → **Lambda@Edge normalize (sort + lowercase) tại trigger "viewer request"**
- **Bỏ cache theo query string hoàn toàn** → chỉ dùng khi origin luôn trả về cùng nội dung bất kể tham số, nếu không sẽ trả sai data
- **Không có "case insensitive" option** trong CloudFront cho query string — phải tự chuẩn hoá bằng code

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 bucket (versioning ON, chưa mã hóa)
        │
        ├── REST API calls ──────► cần header SSE-C đầy đủ
        └── Presigned URL ───────► cần đúng 1 header chỉ định algorithm
                                    (KHÔNG phải header chứa key)
Yêu cầu: SSE-C (Server-Side Encryption Customer-Provided Keys)
         → bảo vệ cả at-rest và in-transit
```

Đề hỏi chọn HAI đáp án đúng cho việc triển khai SSE-C. Anh chọn đúng **C** và **E**.

#### Vì sao C đúng

Khi gọi S3 REST API trực tiếp (không qua presigned URL), request phải mang đủ 3 header SSE-C:

```
x-amz-server-side-encryption-customer-algorithm   → AES256
x-amz-server-side-encryption-customer-key         → key do khách tự cung cấp
x-amz-server-side-encryption-customer-key-MD5     → checksum của key, S3 dùng để verify
```

S3 **chỉ lưu** encryption key trong lúc xử lý request, không bao giờ lưu lại — mất key là mất luôn dữ liệu (không ai, kể cả AWS, giải mã lại được).

#### Vì sao E đúng

Với **presigned URL**, do URL được tạo trước và key nhạy cảm không nên nhúng thẳng vào URL, S3 chỉ yêu cầu khai báo **algorithm** qua header `x-amz-server-side-encryption-customer-algorithm` — còn key thật sự được truyền riêng khi client thực hiện request bằng presigned URL đó.

#### Vì sao từng đáp án sai bị loại

- **A sai**: SSE-C bắt buộc dùng **HTTPS**, không phải WSS (WebSocket Secure) — S3 sẽ **reject mọi request qua HTTP** khi dùng SSE-C, không liên quan gì đến WebSocket.
- **B sai**: với presigned URL phải dùng header `...-customer-algorithm`, không phải `...-customer-key-MD5` (header MD5 dùng cho REST API trực tiếp, không phải cho việc khai báo algorithm trên presigned URL).
- **D sai**: SSE-C hoạt động qua REST API headers, không có cơ chế "chỉ dùng console" — S3 console không hỗ trợ đầy đủ việc nhập customer-provided key theo cách này; phải dùng REST API/SDK.

#### Lưu ý thực tế

- Nếu gửi SSE-C key qua **HTTP** (không phải HTTPS) dù vô tình, AWS khuyến cáo coi key đó là **đã bị lộ (compromised)** — phải discard và rotate key ngay, vì request có thể bị log/sniff ở giữa đường.
- SSE-C khác hoàn toàn SSE-KMS/SSE-S3: SSE-C đòi khách tự quản lý key (S3 không lưu key), còn SSE-KMS/SSE-S3 thì AWS quản lý key.

#### Quy tắc nhớ cho thi

- **REST API call với SSE-C** → cần đủ 3 header: `customer-algorithm`, `customer-key`, `customer-key-MD5`
- **Presigned URL với SSE-C** → chỉ cần header `customer-algorithm`
- **SSE-C encryption key gửi qua HTTP** → coi như lộ key, phải rotate
- **"Customer-provided key"** → luôn là SSE-C, không phải SSE-KMS/SSE-S3

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internet ──(DDoS: nhiều nguồn, flood request)──► Web App trên AWS
Yêu cầu: giảm "attack surface" + giảm "blast radius" khi bị DDoS
         (KHÔNG chỉ là chịu đựng traffic, mà là THU NHỎ diện tích bị tấn công)
```

Đề yêu cầu chọn HAI chiến lược. Anh chọn đúng **B** và **C**.

#### Vì sao B đúng

- **Security group chỉ mở port/server cần thiết** + đặt origin server **phía sau CloudFront** → ẩn origin thật, giảm diện tích có thể bị tấn công trực tiếp (CloudFront có AWS Shield Standard tự động, hấp thụ traffic ở edge trước khi chạm origin).
- **AWS Shield Advanced** bổ sung detect/monitor DDoS ở **application layer (L7)** — tầng mà Shield Standard không bảo vệ sâu.

#### Vì sao C đúng

- **Network ACL chỉ cho phép port cần thiết** → thu nhỏ bề mặt tấn công ở tầng network.
- **AWS WAF** nhận diện và block pattern request DDoS phổ biến ở tầng ứng dụng (ví dụ flood request kiểu HTTP GET/POST lặp lại).

Kết hợp Shield (hạ tầng) + WAF (ứng dụng) = chiến lược phòng chống DDoS toàn diện theo khuyến nghị AWS.

#### Vì sao từng đáp án sai bị loại

- **A sai**: thêm ELB/ASG + dùng instance cực lớn chỉ giúp **chịu đựng (absorb)** traffic tốt hơn, không **giảm attack surface**. Systems Manager Session Manager dùng để quản lý instance an toàn (không cần mở SSH/bastion), **không phải** để filter client-side web session.
- **D sai**: S3 versioning và patch OS qua Patch Manager là best practice bảo mật chung, nhưng **không liên quan đến DDoS surface/blast radius**.
- **E sai**: MFA, Fraud Detector, Config, Trusted Advisor giúp bảo mật tài khoản/phát hiện gian lận, nhưng **không thu nhỏ bề mặt tấn công DDoS**. Fraud Detector là dịch vụ phát hiện fraud online, không liên quan DDoS.

#### So sánh nhanh

| Đáp án | Giảm attack surface? | Giảm blast radius khi bị DDoS? | Lý do loại |
|---|---|---|---|
| **B (đúng)** | Có (SG + CloudFront) | Có (Shield Advanced L7) | — |
| **C (đúng)** | Có (NACL + WAF) | Có (block pattern DDoS) | — |
| A | Không | Chỉ absorb, không giảm | Chỉ scale, không thu nhỏ bề mặt |
| D | Không | Không | S3 versioning/patching không liên quan |
| E | Không | Không | MFA/Fraud Detector không chống DDoS |

#### Lưu ý thực tế

- **Shield Standard** tự động áp dụng miễn phí cho ELB, CloudFront, Route 53 — bảo vệ hạ tầng (L3/L4). **Shield Advanced** là tier trả phí, thêm detect/mitigate ở **application layer**, cần kết hợp với **AWS WAF** để có chiến lược đầy đủ.

#### Quy tắc nhớ cho thi

- **"Giảm attack surface + blast radius"** → SG/NACL chỉ mở port cần + CloudFront che origin + WAF + Shield Advanced
- **"Chỉ scale lên để chịu traffic"** → không phải chiến lược giảm attack surface
- **MFA, Fraud Detector, Config, Trusted Advisor** → tốt cho bảo mật chung, **không phải** công cụ chống DDoS

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Auditor (account riêng, AWS account khác)
        │  cần: read-only access vào NHIỀU account công ty
        │  để audit PCI DSS compliance
        ▼
Công ty có nhiều AWS account cần audit
```

Yêu cầu chốt: cấp quyền cho **bên ngoài (external auditor)** vào **nhiều account**, chỉ **read-only**, theo chuẩn bảo mật PCI DSS. Anh chọn đúng **D**.

#### Vì sao D đúng

- **IAM role** (không phải user) là cách chuẩn để cấp quyền cho một **identity bên ngoài**: role không có credential dài hạn (no password, no access key cố định) — ai assume role thì nhận **temporary security credentials**, hết hạn tự động.
- **Trust policy liệt kê ARN của auditor làm principal** → chỉ đúng auditor đó (hoặc account của họ) mới assume được role này, không ai khác.
- Tạo role này **ở từng account** cần audit → đúng yêu cầu "access across all company's accounts".
- Gắn **read-only permission** → đúng yêu cầu chỉ kiểm tra, không sửa đổi.
- Sau khi audit xong, công ty chỉ cần **xóa/revoke role** — không phải thu hồi credential nào đang trôi nổi bên ngoài.

#### Vì sao từng đáp án sai bị loại

- **A sai**: đưa username/password của user nội bộ cho người ngoài là **lộ credential trực tiếp** — tự nó đã là một vi phạm bảo mật nghiêm trọng, chắc chắn fail audit PCI DSS.
- **B sai**: Active Directory + SSO là giải pháp tốt cho **nhân viên nội bộ** cần truy cập AWS qua hệ thống identity có sẵn của công ty — không phù hợp và quá cồng kềnh cho một **auditor ngoài, truy cập tạm thời, ngắn hạn**.
- **C sai**: tạo IAM user + access key/secret key cho auditor là **credential dài hạn** — dù gắn read-only, vẫn kém an toàn hơn role vì access key có thể bị lưu trữ sai chỗ, không tự hết hạn, khó revoke tức thì so với việc đơn giản xóa role.

#### So sánh nhanh

| Đáp án | Loại credential | Thời hạn | Phù hợp external auditor? |
|---|---|---|---|
| **D (đúng)** | IAM role, temp credentials qua AssumeRole | Tự hết hạn | Có |
| A | Username/password thật | Vĩnh viễn | Không — lộ credential |
| B | AD + SSO | Vĩnh viễn (quản lý qua AD) | Không — dành cho nội bộ |
| C | IAM user access key | Vĩnh viễn (chỉ xóa bằng tay) | Kém hơn role |

#### Lưu ý thực tế

- Role cross-account kiểu này thường kết hợp thêm điều kiện **ExternalId** trong trust policy nếu muốn chống "confused deputy" (xem thêm Q73/Q74 về mô hình third-party access tương tự).
- "Mỗi account cần audit" → nghĩa là phải lặp lại việc tạo role này ở **từng account**, không chỉ một account trung tâm (trừ khi dùng AWS Organizations + cross-account role pattern tập trung hơn).

#### Quy tắc nhớ cho thi

- **"External auditor / third party cần quyền tạm vào nhiều account"** → **IAM role với trust policy chỉ định ARN của họ**, không bao giờ là IAM user với access key
- **Không bao giờ chia sẻ username/password hoặc access key dài hạn** cho người ngoài tổ chức
- **AD + SSO federation** → chỉ dùng khi tích hợp identity nội bộ của chính công ty, không phải cho bên thứ ba truy cập ngắn hạn

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Multi-tier e-commerce (ELB + web tier + app tier + S3 static assets + RDS/DynamoDB)
        │
Log bất thường → nghi ngờ bị tấn công: DDoS, SQL injection, HTTP flood, bad bots
Yêu cầu: giải pháp MOST suitable + scalable
```

Anh chọn đúng **C**: AWS WAF + AWS Shield Advanced trên tất cả web endpoint.

#### Vì sao C đúng

- **SQL injection, HTTP flood, bad bots** là các cuộc tấn công ở **tầng application (L7)** — NACL/Security Group (L3/L4) **không nhìn được nội dung HTTP request** nên không chặn được loại này.
- **AWS WAF**: định nghĩa rule chặn pattern SQL injection, XSS, request bất thường từ bot — rule mới có thể deploy "trong vài phút", phản ứng nhanh với traffic pattern thay đổi, có API để tự động hóa.
- **AWS Shield Advanced**: bổ sung detect/mitigate DDoS ở application layer, đi kèm hỗ trợ từ AWS DDoS Response Team khi cần.
- Giải pháp này **scalable** vì áp dụng ngay trên toàn bộ web endpoint, không cần triển khai hạ tầng mới.

#### Vì sao từng đáp án sai bị loại

- **A sai**: tạo standby stack ở region khác + CloudFormation StackSets + Route 53 failover là giải pháp **disaster recovery (failover khi primary down)**, không phải giải pháp **chống tấn công**. Amazon Macie chỉ phát hiện PII/dữ liệu nhạy cảm trong S3, không chống SQL injection hay DDoS.
- **B sai**: block IP cụ thể bằng NACL là biện pháp **thủ công, không scalable** — attacker dễ dàng đổi IP khác để vượt qua, và cách này **không phòng được các nguồn tấn công mới** chưa từng xuất hiện.
- **D sai**: xây dựng Direct Connect + hardware WAF riêng là giải pháp **quá phức tạp và tốn kém**, không cần thiết khi AWS đã có managed service (WAF + Shield Advanced) giải quyết đúng vấn đề với chi phí/độ phức tạp thấp hơn.

#### So sánh nhanh

| Đáp án | Giải quyết đúng vấn đề? | Scalable | Vấn đề chính |
|---|---|---|---|
| **C (đúng)** | Có — WAF (L7) + Shield Advanced | Có | — |
| A | Không — chỉ là DR, không chống tấn công | — | Sai mục tiêu |
| B | Một phần, dễ bị vượt qua | Không | Thủ công, không scale |
| D | Có thể, nhưng quá phức tạp | Thấp | Chi phí & độ phức tạp cao |

#### Lưu ý thực tế

- Network ACL/Security Group chỉ lọc theo IP/port/protocol (L3/L4) — **không bao giờ** là công cụ đúng khi đề nói đến SQL injection, XSS, hay bad bot content scraping (các tấn công ở L7).
- Amazon Macie và AWS WAF dễ bị nhầm vai trò trong đề thi: Macie = phát hiện dữ liệu nhạy cảm, WAF = chặn tấn công ứng dụng web.

#### Quy tắc nhớ cho thi

- **Thấy "SQL injection", "bad bots", "HTTP flood", "web exploit"** → **AWS WAF**
- **Thấy "DDoS" ở application layer, cần hỗ trợ chuyên sâu** → **AWS Shield Advanced**
- **NACL/Security Group** → chỉ xử lý được tấn công ở L3/L4, không xử lý được tấn công ở L7
- **Disaster recovery (failover, StackSets, Route 53 failover)** ≠ giải pháp chống tấn công bảo mật

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 instance (web app) ──cần──► Amazon S3 bucket (private)
   app phải: list + upload objects, tạo presigned URL
Yêu cầu: cách cấu hình AN TOÀN để EC2 app truy cập S3
```

Anh chọn đúng **D**: IAM role (list + upload) gắn vào EC2, lấy temporary credentials từ **instance metadata**.

#### Vì sao D đúng

```
EC2 instance
    │ launch với IAM role (policy: list + upload S3)
    ▼
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>
    │
    ▼
Temporary security credentials (tự xoay, có thời hạn)
    │
    ▼
App dùng credentials này gọi S3 API
```

- **IAM role** gắn trực tiếp vào EC2 instance khi launch → không cần lưu access key/secret key nào trong code hay trên disk.
- App lấy **temporary credentials** từ **instance metadata endpoint** (`169.254.169.254`) — AWS tự động tạo, xoay (rotate), và thu hồi credentials này gắn với role.
- Policy của role cho phép cả **list và upload** — đúng với nhu cầu: app cần list để kiểm tra file tồn tại trước khi tạo presigned URL, và cần upload để nhận file người dùng tải lên.

#### Vì sao từng đáp án sai bị loại

- **A sai**: lưu access key/secret key trực tiếp trong EC2 instance là **lỗ hổng bảo mật** — bất kỳ ai truy cập được instance (hoặc code) đều lấy được credential dài hạn này.
- **B sai**: tạo **IAM user** rồi "associate" với EC2 instance không phải cách AWS hoạt động — EC2 chỉ nhận **IAM role**, không gắn trực tiếp IAM user. Dùng user nghĩa là vẫn phải quản lý access key dài hạn.
- **C sai**: dùng đúng IAM role, nhưng lấy credentials từ **instance user data** là sai — user data chỉ là script khởi tạo lúc boot, **không chứa credentials động**; credentials thật sự phải lấy từ **instance metadata**. Ngoài ra policy ở C chỉ cho list, thiếu quyền upload mà app cần.

#### So sánh nhanh

| Đáp án | Nguồn credential | Loại credential | Quyền | Đúng/Sai |
|---|---|---|---|---|
| **D (đúng)** | Instance metadata | Temporary (role) | List + Upload | Đúng |
| A | Lưu cứng trong instance | Dài hạn | — | Sai — lộ key |
| B | IAM user "associate" EC2 | Dài hạn | List only | Sai — không có cơ chế này |
| C | Instance user data | Temporary nhưng sai nguồn lấy | List only | Sai — nguồn lấy sai + thiếu quyền |

#### Lưu ý thực tế ⚠️ Dễ nhầm

- ⚠️ **Dễ nhầm**: Q52 (đúng) vs Q17, Q6 (đã làm sai trước đây) — cùng mô-típ "EC2 cần truy cập S3". Quy tắc chung: **EC2 → S3 luôn dùng IAM role + temporary credentials lấy từ instance metadata**, không bao giờ là access key lưu cứng, không bao giờ là IAM user gắn vào instance, và credentials **không bao giờ** nằm trong user data.
- User data vs instance metadata là cặp khái niệm hay bị đánh lừa trong đề: user data = script khởi tạo (cấu hình ban đầu), instance metadata = thông tin runtime của instance bao gồm cả role credentials.

#### Quy tắc nhớ cho thi

- **"EC2 cần gọi S3/AWS service khác"** → **IAM role**, không phải access key, không phải IAM user
- **"Lấy credentials ở đâu trên EC2"** → luôn là **instance metadata** (`169.254.169.254`), không phải user data
- **Thấy "store access keys inside EC2"** → luôn là đáp án sai

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 buckets (lưu static data của financial app)
    │
    ├── Nghi ngờ: có PII (personally identifiable information) bị lưu không đúng chỗ
    │   → cần phát hiện TỰ ĐỘNG, khối lượng data lớn
    └── Cần biết: data có PII đó đã bị truy cập (GET) chưa
```

Anh chọn đúng **B**: Amazon Macie (phát hiện PII) + CloudTrail (track GET API calls).

#### Vì sao B đúng

- **Amazon Macie** là dịch vụ **ML-powered**, chuyên **tự động discover và classify sensitive data** (bao gồm PII) lưu trong S3 — đúng chính xác nhu cầu "tự động phát hiện PII trên khối lượng dữ liệu lớn".
- Macie còn giám sát liên tục hoạt động truy cập, cảnh báo khi có nguy cơ truy cập trái phép hoặc rò rỉ dữ liệu.
- **AWS CloudTrail** ghi lại **data events** bao gồm các lệnh gọi **GET** trên object S3 → dùng để xác định object chứa PII đã bị ai, khi nào truy cập.
- Kết hợp Macie (tìm PII) + CloudTrail (ai đã đọc nó) → giải quyết đủ cả hai yêu cầu của đề.

#### Vì sao từng đáp án sai bị loại

- **A sai**: **Amazon Athena** là dịch vụ query dữ liệu (SQL trên S3), **không có khả năng tự nhận diện/classify PII** — phải dùng Macie. Đồng thời phải dùng CloudTrail để track GET calls, không phải CloudWatch (CloudWatch theo dõi metrics/logs vận hành, không phải data events chi tiết kiểu này).
- **C sai**: **Amazon GuardDuty** là dịch vụ **threat detection** (phát hiện hoạt động độc hại/bất thường trong account), **không phải** công cụ phát hiện PII trong dữ liệu — vai trò hoàn toàn khác Macie.
- **D sai**: **Amazon Inspector** chỉ cài đặt agent được trên **EC2 instance**, **không áp dụng được cho S3 bucket** — S3 là object storage, không chạy agent được. Inspector dùng để security assessment cho ứng dụng/compute, không liên quan phát hiện PII.

#### So sánh nhanh

| Đáp án | Dịch vụ phát hiện PII | Đúng chức năng? | Dịch vụ track truy cập |
|---|---|---|---|
| **B (đúng)** | Amazon Macie | Đúng | CloudTrail |
| A | Amazon Athena | Sai — chỉ query, không classify | CloudWatch (sai, nên là CloudTrail) |
| C | Amazon GuardDuty | Sai — là threat detection | CloudTrail |
| D | Amazon Inspector | Sai — chỉ chạy trên EC2 | CloudTrail |

#### Lưu ý thực tế

- Bốn dịch vụ Athena, GuardDuty, Inspector, Macie rất dễ gây nhầm lẫn vai trò trong đề thi vì đều nghe "liên quan security/data": chỉ **Macie** là dịch vụ **chuyên biệt phát hiện và phân loại dữ liệu nhạy cảm (PII)** trong S3.
- "Ai đã truy cập object nào" luôn gắn với **CloudTrail data events** (phải enable riêng, vì data events không bật sẵn mặc định như management events).

#### Quy tắc nhớ cho thi

- **"Tìm PII trong S3"** → **Amazon Macie**
- **"Ai đã truy cập/đọc object nào trong S3"** → **AWS CloudTrail (data events, GET API calls)**
- **GuardDuty** → threat detection chung, không classify data
- **Inspector** → chỉ chạy trên EC2, không chạy trên S3
- **Athena** → chỉ query dữ liệu, không tự nhận diện PII

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Third-party vendor (account riêng, có unique Customer/Account ID)
        │  cần: gọi API để discover EC2 resources trong account công ty
        ▼
Công ty cần: least privilege + credential KHÔNG dùng được bởi bên thứ ba khác
```

Anh chọn đúng **A**: IAM role + trust policy có Condition kiểm tra **ExternalId**.

#### Vì sao A đúng

```
Company account                         Vendor account
┌─────────────────────────┐            ┌─────────────────────────┐
│ IAM Role                │            │ Vendor app               │
│  - Permission policy:   │            │  sts:AssumeRole ──────►  │ gọi
│    chỉ action cần thiết │  ◄──────── │  kèm ExternalId          │
│  - Trust policy:        │            │  (unique customer ID)    │
│    Principal = vendor   │            └─────────────────────────┘
│    Condition: ExternalId│
└─────────────────────────┘
```

- **IAM role** không có credential dài hạn — vendor chỉ nhận **temporary security credentials** qua `sts:AssumeRole`, hết hạn tự động.
- **Permission policy** gắn vào role chỉ cho đúng các action vendor cần (ví dụ `ec2:Describe*`) → đúng nguyên tắc least privilege.
- **Trust policy với Condition trên ExternalId**: chống "confused deputy" — nếu vendor này cũng phục vụ nhiều khách hàng khác và vô tình (hoặc bị lừa) dùng role ARN của một khách để assume nhầm sang account công ty, ExternalId (do đề cho là unique customer ID) đảm bảo **chỉ đúng vendor biết đúng ExternalId mới assume được** — khớp yêu cầu "credentials không thể dùng bởi bên thứ ba khác".

#### Vì sao từng đáp án sai bị loại

- **B sai**: **Amazon Connect** là dịch vụ **contact center** (omnichannel customer service), hoàn toàn không liên quan đến việc cấp quyền AWS cho bên thứ ba — không có khái niệm "input ExternalId" trong Connect để cấp IAM access.
- **C sai**: đưa access key/secret key của chính mình cho third-party software là **tuyệt đối không nên** — chia sẻ credential cá nhân/root là rủi ro bảo mật nghiêm trọng, vi phạm ngay nguyên tắc least privilege và không kiểm soát được việc credential bị dùng lại.
- **D sai**: tạo **IAM user** + access key/secret key cho vendor là credential **dài hạn**, dễ bị lưu trữ sai chỗ hoặc rò rỉ, khó kiểm soát ai đang dùng — role luôn là lựa chọn an toàn hơn user khi cấp quyền cho bên ngoài.

#### So sánh nhanh

| Đáp án | Cơ chế | Credential | Chống dùng lại bởi bên khác? |
|---|---|---|---|
| **A (đúng)** | IAM role + ExternalId condition | Temporary | Có |
| B | Amazon Connect | — (không áp dụng) | Không áp dụng |
| C | Chia sẻ access key cá nhân | Dài hạn, của chính công ty | Không — rủi ro cực cao |
| D | IAM user riêng cho vendor | Dài hạn | Không — vẫn là key cố định |

#### Lưu ý thực tế ⚠️ Dễ nhầm

- ⚠️ **Dễ nhầm**: Q73 (đúng) cùng mô-típ với Q74 (đúng) — cả hai đều là "bên ngoài/đã có identity riêng cần truy cập AWS" → luôn giải qua **STS temporary credentials**, không bao giờ qua IAM user với access key dài hạn. Trước đây đã làm sai case tương tự ở TD2 Q41.
- **ExternalId** chỉ có ý nghĩa khi vendor/third-party cung cấp một giá trị unique cho từng khách hàng của họ — nó không phải "password" mà là điều kiện chống nhầm account trong kịch bản nhiều khách hàng dùng chung một vendor.

#### Quy tắc nhớ cho thi

- **"Third-party vendor cần truy cập AWS account của mình"** → **IAM role cross-account**, không bao giờ IAM user với access key
- **"Chống việc credential bị dùng bởi bên thứ ba khác / confused deputy"** → thêm **Condition ExternalId** vào trust policy
- **Không bao giờ** chia sẻ access key/secret key của chính mình cho bên ngoài

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises LDAP server ── IPSec VPN ──► VPC trên AWS
Yêu cầu: nhân viên dùng CHÍNH corporate account (LDAP) để truy cập AWS resources
         LDAP KHÔNG tương thích SAML 2.0 (không nói gì về SAML/AD FS)
```

Anh chọn đúng **A**: identity broker tự xây, authenticate LDAP → gọi STS **AssumeRole** lấy temporary credentials.

#### Vì sao A đúng

```
Employee ──auth──► LDAP server (on-prem)
                        │ xác thực OK
                        ▼
              Identity broker (app tự viết)
                        │ gọi STS:AssumeRole
                        ▼
              Temporary AWS security credentials
                        │
                        ▼
              Employee dùng credentials này truy cập AWS resources
```

- LDAP **không tương thích SAML 2.0** → không dùng được federation chuẩn qua AD FS/SAML. Giải pháp đúng là **custom identity broker**: một ứng dụng tự viết, xác thực user qua hệ thống hiện có (LDAP/AD…), sau đó gọi STS để lấy credentials tạm.
- Broker gọi **AssumeRole** (hoặc GetFederationToken) trong STS → trả về **temporary security credentials** cho user, đúng khuyến nghị AWS cho trường hợp identity store không hỗ trợ SAML.

#### Vì sao từng đáp án sai bị loại

- **B sai**: nói "set up federation between LDAP và AWS IAM" — LDAP không hỗ trợ SAML nên **không thể federation trực tiếp** theo kiểu này; đây không phải mô hình identity broker mà đề yêu cầu, không khớp với cách AWS triển khai thực tế cho LDAP thuần.
- **C sai**: dùng đúng mô hình identity broker, nhưng gọi STS để lấy **federated user credentials** (GetFederationToken cho IAM user tồn tại sẵn) — khác với yêu cầu đề là dùng chính **corporate account**; ngoài ra đáp án diễn đạt như thể chỉ cần STS mà bỏ qua việc phải xác thực LDAP trước, sai thứ tự/logic.
- **D sai**: không có cơ chế "integrate LDAP trực tiếp với IAM để login" — **IAM không hỗ trợ LDAP authentication trực tiếp**; IAM chỉ hỗ trợ identity federation qua các IdP tương thích (SAML, OIDC), LDAP thuần không thuộc nhóm này.

#### So sánh nhanh

| Đáp án | Cơ chế | Dùng đúng LDAP (không SAML)? | Kết quả |
|---|---|---|---|
| **A (đúng)** | Custom identity broker → STS AssumeRole | Có | Đúng |
| B | "Federation" trực tiếp LDAP-IAM | Không khả thi vì LDAP không SAML | Sai |
| C | Broker nhưng dùng GetFederationToken sai ngữ cảnh | Không khớp yêu cầu | Sai |
| D | "Integrate" LDAP trực tiếp vào IAM login | IAM không hỗ trợ kiểu này | Sai |

#### Lưu ý thực tế ⚠️ Dễ nhầm

- ⚠️ **Dễ nhầm**: Q74 (đúng) cùng mô-típ Q73 (đúng) — bất kỳ khi nào identity bên ngoài (LDAP, third party, federation) cần truy cập AWS, câu trả lời luôn xoay quanh **STS temporary credentials**, không bao giờ là long-term IAM user credentials hay "login trực tiếp vào IAM". Trước đây đã làm sai mô-típ tương tự ở TD2 Q28.
- Khi identity store **hỗ trợ SAML 2.0** (ví dụ Active Directory qua AD FS), AWS khuyến nghị dùng **SAML federation trực tiếp** thay vì tự viết identity broker — nhưng LDAP thuần (không SAML) buộc phải đi đường "custom identity broker".

#### Quy tắc nhớ cho thi

- **"LDAP không hỗ trợ SAML, cần dùng chính corporate account"** → **custom identity broker + STS AssumeRole**
- **Identity store hỗ trợ SAML 2.0** → ưu tiên **SAML federation** trực tiếp, không cần tự viết broker
- **IAM không bao giờ "tích hợp trực tiếp" với LDAP** để login — chỉ có federation qua IdP tương thích

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations (crypto startup, nhiều account)
            │
   Yêu cầu: logging giải pháp DURABLE + SECURE NHẤT
            track changes trên TẤT CẢ resource, TOÀN BỘ company, GLOBAL
```

Đáp án đúng: **B** — tạo 1 CloudTrail trail mới với 1 S3 bucket MỚI, bật "Enable for all accounts in my organization", rồi enable MFA Delete + Log Encryption trên bucket đó. Anh chọn đúng B.

#### Vì sao B đúng

- **"Enable for all accounts in my organization"** tạo ra một **organization trail**: trail này tự động log event của **management account + mọi member account**, đáp ứng "track changes... across all of the company's AWS resources globally" mà không cần set up trail riêng cho từng account.
- **MFA Delete** trên S3 bucket chứa log: ngăn việc xóa log file hoặc disable versioning một cách vô tình/ác ý nếu không có MFA — đây là yếu tố "secure" mà đề nhấn mạnh.
- **Log Encryption (SSE-KMS)**: CloudTrail mặc định đã mã hóa log bằng SSE-S3, nhưng đề hỏi **"most durable and secure"** — bật thêm Log Encryption với KMS cho một lớp bảo mật có thể quản lý trực tiếp (customer-manageable key), chặt hơn SSE-S3 mặc định.

#### Vì sao từng đáp án sai bị loại

- **A sai**: dùng "Apply trail to all regions" (đúng cho multi-region) nhưng **không** bật "Enable for all accounts in my organization" → chỉ log 1 account, không phải toàn công ty. Ngoài ra chỉ bật MFA Delete, **không** bật Log Encryption — kém "secure" hơn B.
- **C sai**: không hề bật multi-region, cũng không bật organization trail — chỉ 1 trail đơn account, đơn region; thêm SNS notification không giải quyết yêu cầu "tất cả resource của toàn công ty, global".
- **D sai**: tạo **3 trail riêng** cho Console/SDK/CLI là dư thừa không cần thiết — một trail duy nhất (org trail) vốn đã ghi lại tất cả activity (Console, SDK, CLI) trong 1 bucket, không cần chia tách theo nguồn gọi API.

#### So sánh nhanh

| Đáp án | Organization trail | Multi-region | MFA Delete | Log Encryption |
|---|---|---|---|---|
| **B (đúng)** | Có | Có (default) | Có | Có |
| A | Không | Có | Có | Không |
| C | Không | Không | Có | Có |
| D | Không | — (3 trail riêng) | Có | Có |

#### Lưu ý thực tế

- CloudTrail mặc định mã hóa log bằng SSE-S3 — nhưng khi đề nhấn "most secure", luôn ưu tiên bật thêm **SSE-KMS (Log Encryption)** cho khả năng quản lý key tốt hơn.
- Organization trail chỉ tạo được từ **management account**, và phải chọn "Enable for all accounts in my organization" khi tạo (hoặc sửa trail hiện có rồi apply cho organization).

#### Quy tắc nhớ cho thi

- **"Audit log cho TẤT CẢ account trong Organization"** → **organization trail** ("Enable for all accounts in my organization")
- **"Most durable and secure"** → 1 bucket, **MFA Delete + Log Encryption (KMS)**, không cần nhiều bucket/nhiều trail
- Nhiều trail cho từng loại nguồn gọi API (Console/SDK/CLI) → không cần thiết, CloudTrail đã ghi tất cả trong 1 trail

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organization (dev + prod accounts) ── Consolidated billing

RDS + DynamoDB cost tăng đột biến
Yêu cầu: enforce tag (cost center + project ID) trên
         - TẤT CẢ resource hiện có
         - TẤT CẢ resource trong TƯƠNG LAI (existing + future)
```

Đáp án đúng: **C** — Tag Editor để bulk-tag resource hiện có, tạo cost allocation tag trên Billing console, VÀ áp **SCP ở OU level deny việc tạo resource không có tag** cost center/project ID. Anh chọn đúng C.

#### Vì sao C đúng

- **Tag Editor**: công cụ bulk-tag nhiều resource cùng lúc trên nhiều region/account — giải quyết phần "existing resources" nhanh gọn.
- **Cost allocation tags** trên Billing and Cost Management: bật để các tag này xuất hiện trên cost report, phục vụ chính nhu cầu "more visibility on Billing and Cost Management" trong đề.
- **SCP deny tại OU**: đây là phần mấu chốt giải quyết "future resources" — SCP là guardrail áp dụng cho **toàn bộ account trong OU**, chặn hành động tạo resource (RDS, DynamoDB...) nếu thiếu tag bắt buộc, hiệu lực ngay tại thời điểm tạo, không phụ thuộc vào IAM policy riêng của từng account.

#### Vì sao từng đáp án sai bị loại

- **A sai**: chỉ tag resource hiện có + kích hoạt cost allocation tag rồi chờ 24h để có report — **không có cơ chế nào ngăn resource mới được tạo thiếu tag** trong tương lai. Giải pháp thiếu phần "enforce" mà đề yêu cầu.
- **B sai**: AWS Config rule chỉ **phát hiện (detect)** resource chưa tag rồi gửi email — không tự động gắn tag, và Lambda chạy mỗi giờ để tag lại là giải pháp **reactive, chạy sau khi đã tạo** chứ không ngăn chặn tại thời điểm tạo; tốn nhiều effort vận hành hơn một SCP.
- **D sai**: sửa IAM policy của federated role ở từng account để deny resource không tag — khả thi nhưng **cồng kềnh**: phải sửa policy lặp lại trên tất cả account trong công ty, trong khi SCP ở cấp OU chỉ cần áp 1 lần cho toàn bộ account dưới OU đó.

#### So sánh nhanh

| Đáp án | Tag resource cũ | Ngăn resource mới thiếu tag | Nơi enforce |
|---|---|---|---|
| **C (đúng)** | Tag Editor | Có | SCP tại OU (toàn org) |
| A | Tag Editor | Không | — |
| B | Không tự tag, chỉ cảnh báo | Không (reactive, theo giờ) | Lambda + Config |
| D | Không | Có, nhưng cồng kềnh | IAM policy mỗi account |

#### Lưu ý thực tế

⚠️ **Dễ nhầm** — đối lập trực tiếp với Q75 (đã trả lời sai): ở Q75, SCP dùng theo mô hình **allow-list**, nếu thiếu action nào trong SCP thì action đó **bị chặn hoàn toàn dù IAM cho phép** (SCP không cấp quyền, chỉ giới hạn trần quyền). Ở Q59, SCP lại đóng vai trò **deny có điều kiện** (deny create resource nếu thiếu tag cụ thể) — SCP vẫn luôn hoạt động theo nguyên tắc "giới hạn", nhưng cách viết statement (allow danh sách cố định vs. deny có condition trên tag) quyết định hành vi thực tế rất khác nhau. Đừng lẫn hai kiểu SCP này.

#### Quy tắc nhớ cho thi

- **"Enforce tag tại thời điểm tạo, toàn Organization"** → **SCP deny create-without-tag** ở cấp OU
- **Tag Editor** → chỉ xử lý resource **đã tồn tại** (bulk, không tự động cho tương lai)
- **AWS Config + Lambda remediation** → reactive (phát hiện rồi sửa), không ngăn chặn tại thời điểm tạo
- SCP allow-list thiếu action → chặn tuyệt đối; SCP deny-with-condition → chặn có điều kiện cụ thể (ví dụ thiếu tag)

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 fleet (OS outdated, có security vulnerability)
         │
Yêu cầu: vá lỗ hổng NHANH + ghi lại toàn bộ thay đổi patch
         và compliance status của association
```

Đáp án đúng: **B** — dùng AWS Systems Manager **Patch Manager** để deploy OS security patch, dùng **AWS Config** để quản lý/phát hiện/ghi lại security compliance của EC2. Anh chọn đúng B.

#### Vì sao B đúng

- **Patch Manager** tự động hóa việc patch managed instance theo OS type (Windows, Ubuntu, RHEL, SUSE, Amazon Linux...) — có thể chỉ scan để biết patch còn thiếu, hoặc scan + install luôn, giải quyết đúng yêu cầu "mitigate the vulnerability as soon as possible".
- **AWS Config**: liên tục monitor và **ghi lại (record)** resource configuration, đồng thời cho phép đánh giá tự động so với baseline mong muốn — đáp ứng chính xác yêu cầu phụ "record all of the changes to patches and association compliance statuses" mà đề nhấn mạnh.
- Hai dịch vụ này phối hợp: Patch Manager xử lý **hành động** patch, Config xử lý **lịch sử/compliance** — không dịch vụ nào tự làm được cả hai, nên kết hợp đúng cả hai là cần thiết.

#### Vì sao từng đáp án sai bị loại

- **A sai**: tạo AMI mới tự patch mỗi tuần theo maintenance window — cách này **không kiểm soát được từng patch cụ thể** nào được cài, và việc rollback khi một update làm hỏng hệ thống sẽ rất cồng kềnh (phải quay lại AMI cũ, re-launch...).
- **C sai**: Amazon Control Tower dùng để **tự động setup multi-account environment**, không có chức năng deploy OS security update — dùng sai mục đích dịch vụ hoàn toàn.
- **D sai**: AWS Systems Manager **State Manager** là dịch vụ configuration management tổng quát (giữ instance ở "state" định nghĩa trước) — có thể dùng để cài patch nhưng **không phải dịch vụ khuyến nghị cho patching OS** (đó là vai trò của Patch Manager); đồng thời Amazon OpenSearch không phải công cụ ghi/track compliance chuẩn cho patch của AWS (đó là vai trò của Config).

#### So sánh nhanh

| Đáp án | Patch OS | Record compliance |
|---|---|---|
| **B (đúng)** | Patch Manager | AWS Config |
| A | Tự build AMI theo tuần | Không có |
| C | Control Tower (sai mục đích) | Managed Grafana (visualize, không record compliance chuẩn) |
| D | State Manager (không chuyên patch) | OpenSearch (không phải service record compliance chuẩn) |

#### Lưu ý thực tế

⚠️ **Dễ nhầm** — cùng chủ đề Patch Manager với Q61 (đã trả lời sai): ở Q61, bẫy là chọn một dịch vụ **không host được server** (CloudShell) hay dùng sai dịch vụ làm bastion (AppStream); ở Q66, bẫy là chọn dịch vụ **đúng vai trò gần giống nhưng không phải chuyên trách** — State Manager thay Patch Manager, OpenSearch/Grafana thay Config. Quy tắc chung: khi đề nói "vá lỗ hổng OS trên EC2 fleet" → luôn là **Patch Manager**; khi đề nói "ghi lại/track compliance/configuration history" → luôn là **AWS Config**.

#### Quy tắc nhớ cho thi

- **"Patch OS cho EC2/on-prem fleet"** → **AWS Systems Manager Patch Manager**
- **"Record/track compliance history của resource"** → **AWS Config**
- **State Manager** → giữ instance ở configuration state định sẵn, không phải service chính để patch
- **Control Tower** → setup/governance multi-account, không deploy OS patch

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Multinational company ── nhiều account AWS ĐÃ TỒN TẠI sẵn (nhiều region)

Yêu cầu: set up AWS Organizations, management account có FULL ADMIN CONTROL
         trên tất cả member account, với LEAST EFFORT
```

Đáp án đúng: **D** — gửi invitation từ master account tới **tất cả member account**, rồi tạo **OrganizationAccountAccessRole** IAM role trong mỗi member account và cho phép master account assume role đó. Anh chọn đúng D.

#### Vì sao D đúng

- Account đã tồn tại từ trước (không phải tạo mới trong Organizations) → cách duy nhất để đưa vào Organization là **invite**, và chiều gửi invitation đúng là **từ master account tới member account** — đây là chiều duy nhất AWS Organizations hỗ trợ.
- Khi account được **invite** (khác với account được **create** trong Organizations), master account **không tự động** có full admin control — phải chủ động tạo **OrganizationAccountAccessRole** trong account đó và cấp quyền cho master assume role này.
- Gửi invitation 1 lần từ master tới toàn bộ member account cùng lúc là cách **ít effort nhất** trong các lựa chọn.

#### Vì sao từng đáp án sai bị loại

- **A sai**: "cross-account access" từ master tới member không tự động cấp full admin control — cross-account access (qua IAM role switch) là cơ chế **được cấu hình thủ công theo từng use case**, không phải cơ chế tự động của Organizations.
- **B sai**: gửi invitation theo chiều ngược — **từ member account tới master account** — hoàn toàn sai chiều kỹ thuật (Organizations chỉ cho invite từ master), và nếu làm được thì cũng tốn effort gửi riêng lẻ từng account, trái với "LEAST effort".
- **C sai**: Control Tower giúp setup và quản lý multi-account, nhưng **không tự động provision IAM permission** đầy đủ cho master kiểm soát toàn bộ member account — vẫn cần bước cấu hình quyền tương ứng.

#### So sánh nhanh

| Đáp án | Chiều invite | Role cấp quyền admin | Effort |
|---|---|---|---|
| **D (đúng)** | Master → tất cả member (1 lượt) | OrganizationAccountAccessRole | Thấp nhất |
| B | Member → master (sai chiều, từng cái) | OrganizationAccountAccessRole | Cao |
| A | Không dùng invite, chỉ "cross-account access" | Không tự có | Không chính xác |
| C | Control Tower enroll | Không tự provision đủ | Vẫn cần cấu hình thêm |

#### Lưu ý thực tế

- Account **tạo mới** trực tiếp trong Organizations tự động có OrganizationAccountAccessRole sẵn, cho phép master full control ngay; chỉ account **được invite vào** (account đã tồn tại từ trước) mới cần tạo role này thủ công — đây là điểm phân biệt quan trọng hay bị hỏi trong đề thi.

#### Quy tắc nhớ cho thi

- **"Đưa account đã tồn tại vào Organization, full control, LEAST effort"** → master gửi **invitation tới toàn bộ member account** + tạo **OrganizationAccountAccessRole** trong mỗi member
- Invitation luôn đi theo chiều **master → member**, không bao giờ ngược lại
- Account **created** trong Organizations ≠ account **invited** vào Organizations — chỉ account created mới tự động có full admin control sẵn

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Financial company ── Multi-account, quản lý bởi AWS Control Tower

Yêu cầu: centralize compliance + security findings
         implement preventive + detective + responsive controls
```

Đáp án đúng: **A** — tạo member account mới trong Organizations, enable AWS Security Hub và chỉ định account đó làm **delegated administrator**. Anh chọn đúng A.

#### Vì sao A đúng

- **Security Hub** là service được AWS khuyến nghị chuyên để **centralize** compliance/security findings — nó tổng hợp (aggregate) finding từ GuardDuty, Config, Inspector, Macie, IAM Access Analyzer và cả partner solutions vào một chỗ.
- Vì tích hợp nhiều nguồn như vậy, Security Hub phủ được cả 3 loại control mà đề yêu cầu: **preventive** (qua Config rules/IAM Access Analyzer), **detective** (GuardDuty, Inspector phát hiện threat), **responsive** (finding kích hoạt remediation workflow) — không service đơn lẻ nào khác trong 4 lựa chọn phủ đủ cả 3.
- **Delegated administrator account**: đây là pattern chuẩn cho multi-account quản lý bởi AWS Organizations/Control Tower — một member account được giao quyền quản lý Security Hub cho **toàn bộ account khác**, tập trung view bảo mật về một nơi, giảm việc quản lý riêng lẻ từng account, đúng best practice.

#### Vì sao từng đáp án sai bị loại

- **B sai**: Amazon Detective là tool **investigation** (phân tích/visualize finding đã có sẵn) — nó hữu ích **sau khi** đã có finding, không phải service để centralize compliance/security finding hay cung cấp preventive/responsive control.
- **C sai**: CloudTrail Lake dùng cho **event analysis và auditing** (query log sự kiện quản trị) — đây là một phần của detective control, nhưng không cung cấp preventive hay responsive control, và không phải service chính để "centralize compliance and security findings" như đề yêu cầu.
- **D sai**: GuardDuty tự thân có thể detect threat tốt, nhưng cách làm trong D — "export finding ra S3 bucket trung tâm" — là giải pháp **thủ công, tốn effort vận hành**, không scale tốt cho multi-account, và cũng không mang theo cơ chế preventive/responsive như Security Hub.

#### So sánh nhanh

| Đáp án | Vai trò chính | Preventive | Detective | Responsive | Centralize finding |
|---|---|---|---|---|---|
| **A (đúng)** | Security Hub + delegated admin | Có | Có | Có | Có |
| B | Detective (StackSet deploy) | Không | Có (investigate) | Không | Không |
| C | CloudTrail Lake | Không | Có (audit) | Không | Không (chỉ event data) |
| D | GuardDuty + export S3 tay | Không | Có | Không | Thủ công, không scale |

#### Lưu ý thực tế

- Delegated administrator cho Security Hub giúp một account quản lý Security Hub **thay cho** management account, tuân theo nguyên tắc không dùng management account cho công việc vận hành hàng ngày — một best practice hay bị hỏi riêng trong đề AWS Organizations/Control Tower.

#### Quy tắc nhớ cho thi

- **"Centralize compliance + security findings, multi-account"** → **AWS Security Hub với delegated administrator account**
- **Amazon Detective** → investigation sau khi có finding, không phải nơi tập trung finding
- **CloudTrail Lake** → audit/event analysis, không cung cấp preventive/responsive control
- **GuardDuty tự export tay** → không scale, không có preventive/responsive — chỉ nên dùng khi không có nhu cầu tích hợp đa dịch vụ

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organization (financial company, nhiều account)

Yêu cầu: tags LUÔN được add khi tạo resource bất kỳ, trên MỌI account
         → dùng "centralized resource provisioning tools" +
           "infrastructure-as-code templates" apply tag NGAY LÚC TẠO
Chọn HAI đáp án
```

Đáp án đúng: **B, D** — Service Catalog tag resource với unique identifier cho portfolio/product/user, VÀ CloudFormation Resource Tags property apply tag lúc tạo resource. Anh chọn đúng B, D.

#### Vì sao B và D đúng — hai kênh provisioning khác nhau, cùng tự động tag lúc tạo

- **D — CloudFormation Resource Tags property**: đúng nghĩa đen với "infrastructure-as-code templates" trong đề — khi resource được tạo qua CloudFormation template, Resource Tags property gắn tag ngay tại thời điểm resource được provision, không cần bước phụ nào sau đó.
- **B — AWS Service Catalog**: đúng nghĩa với "centralized resource provisioning tools" — Service Catalog cho phép tổ chức catalog các product đã được chuẩn hoá (self-service cho user), và tự động gắn tag (portfolio, product, user identifier) khi user provision resource qua catalog — enforce tagging policy mà không phụ thuộc user có tự tag đúng hay không.
- Hai lựa chọn này bổ sung cho nhau: D phù hợp khi team dùng IaC trực tiếp, B phù hợp khi tổ chức muốn chuẩn hoá self-service qua catalog — cả hai đều **proactive, tag ngay lúc tạo**, đúng trọng tâm câu hỏi.

#### Vì sao từng đáp án sai bị loại

- **A sai**: AWS Config chỉ **monitor và record** configuration (bao gồm tag), nó giúp **phát hiện** resource không tuân thủ tagging policy, nhưng **không tự add tag lúc resource được tạo** — đây là cơ chế reactive (detect rồi mới remediate qua Lambda/SSM Automation), không phải proactive tag-on-create.
- **C sai**: AWS generated tags kích hoạt trong Billing and Cost Management console chỉ phục vụ **cost allocation/tracking**, hoàn toàn không liên quan tới việc tự động gắn tag khi resource được tạo.
- **E sai**: Systems Manager Automation dùng để tự động hoá các task maintenance/deployment cho resource **đã tồn tại** — nó không phải công cụ provisioning tập trung hay IaC, và không được thiết kế để tag resource ngay lúc tạo mới.

#### So sánh nhanh

| Đáp án | Loại công cụ | Tag lúc tạo? | Vai trò thực |
|---|---|---|---|
| **B (đúng)** | Service Catalog | Có | Centralized self-service provisioning |
| **D (đúng)** | CloudFormation Resource Tags | Có | Infrastructure-as-code |
| A | AWS Config | Không (reactive) | Detect/record configuration |
| C | Billing console AWS generated tags | Không | Cost allocation only |
| E | SSM Automation | Không | Maintenance task cho resource đã có |

#### Lưu ý thực tế

- AWS Config có thể **kết hợp** với Lambda/SSM Automation để remediate resource thiếu tag — nhưng đó luôn là bước xử lý **sau khi phát hiện**, không phải cơ chế tag-on-create mà đề hỏi trực tiếp.

#### Quy tắc nhớ cho thi

- **"Tag tự động NGAY LÚC TẠO, qua provisioning tool / IaC"** → **Service Catalog (self-service, TagOptions)** + **CloudFormation Resource Tags property**
- **AWS Config** → chỉ detect/record, cần thêm remediation action để fix retroactively, không proactive
- **Billing console AWS generated tags** → chỉ phục vụ cost allocation, không liên quan tới việc enforce tag khi tạo resource

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
us-east-1 (Primary)                      us-west-2 (DR)
┌─────────────────────┐                 ┌─────────────────────┐
│ ALB + ASG (đã có)    │                 │ ALB + ASG (đã có)    │
│ MySQL trên EC2       │  ───phải di cư──►│ ?                    │
│ (private subnet)     │                 │                      │
└─────────────────────┘                 └─────────────────────┘

Yêu cầu: RPO < 1 phút | RTO < 5 phút | "lessen operational overhead"
```

Database đang nằm trên EC2 (tự quản lý), cần một giải pháp DR **xuyên Region** đạt RPO/RTO cực chặt mà vẫn ít overhead. Đáp án đúng: **B** — migrate sang Aurora Global Database (primary ở us-east-1, secondary ở us-west-2) + Route 53 failover routing với health checks.

#### Vì sao B đúng

- **Aurora Global Database** dùng storage-based replication, latency thường **< 1 giây** giữa các Region — tự động đáp ứng RPO < 1 phút mà không cần tự dựng replication.
- Khi primary Region gặp sự cố, secondary Region có thể được **promote lên read/write trong chưa đầy 1 phút** — nằm trong RTO < 5 phút.
- Đây là dịch vụ **managed hoàn toàn**, không cần tự cấu hình replication, không cần script promote phức tạp → đúng yêu cầu "lessen operational overhead".
- **Route 53 failover routing + health checks**: khi ALB ở us-east-1 "unhealthy", Route 53 tự chuyển traffic sang ALB ở us-west-2 — khớp với phần ASG/ALB solutions architect đã dựng sẵn.

#### Vì sao từng đáp án sai bị loại

- **A sai** — RDS for MySQL cross-Region read replica **không tự động promote**. Phải promote thủ công, và khi promote thì instance phải **reboot**, dễ vượt quá RTO 5 phút và RPO 1 phút.
- **C sai** — Multi-AZ chỉ bảo vệ khỏi sự cố ở **một AZ**, hoàn toàn không bảo vệ khỏi sự cố **toàn Region** — đề yêu cầu DR xuyên Region.
- **D sai** — tạo snapshot EC2 rồi restore sang us-west-2, tự cấu hình "MySQL standby" bằng tay: vừa tốn operational overhead (tự quản lý replication/failover trên EC2), vừa không đạt được RPO 1 phút/RTO 5 phút như snapshot thủ công thường mất.

#### So sánh nhanh

| Đáp án | Giải pháp DB | Promote tự động? | Đạt RPO<1p/RTO<5p? |
|---|---|---|---|
| **B (đúng)** | Aurora Global Database | Có (<1 phút) | Có |
| A | RDS MySQL cross-Region read replica | Không (manual + reboot) | Không chắc |
| C | RDS MySQL Multi-AZ | Chỉ chống AZ failure, không chống Region failure | Không áp dụng |
| D | EC2 snapshot + standby tự quản | Không, tự tay | Không |

#### Lưu ý thực tế

⚠️ **Dễ nhầm** với Q16: Q16 cho RTO rộng (30 phút) và yêu cầu "cost-effective" cho **tier stateless (web/app)** → ở đó đáp án đúng lại là **daily EC2 snapshot + restore**, không cần hot/managed DB replication liên tục cho tầng không giữ state. Ở Q15 thì ngược lại: RTO/RPO siết rất chặt (< 5 phút / < 1 phút) và **database chính là tầng có state quan trọng nhất** → bắt buộc dùng giải pháp replication liên tục, gần-real-time (Aurora Global Database), snapshot/backup định kỳ không đủ nhanh. Quy tắc chung: **chọn giải pháp DR theo đúng độ gắt của RTO/RPO và theo tầng nào giữ state** — đừng áp dụng cùng một công thức "backup/restore rẻ" cho mọi tình huống DR.

#### Quy tắc nhớ cho thi

- **"RPO/RTO siết rất chặt (phút hoặc giây) cho database"** → **Aurora Global Database** (hoặc replication storage-based tương đương), không dùng snapshot/restore thủ công.
- **"Multi-AZ"** → chỉ chống AZ failure, **không** phải giải pháp DR cross-Region.
- **RDS cross-Region read replica** → luôn cần **promote thủ công + reboot**, không phải lựa chọn "ít operational overhead nhất" khi RTO rất gắt.
- **"lessen operational overhead"** → ưu tiên dịch vụ managed (Aurora Global DB) hơn tự dựng standby trên EC2.

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Test: 1 EC2 Windows instance, EBS root volume, static content lưu trên EBS
                 │
                 ▼ Production: ≥3 EC2 across multiple AZ (ASG)
                 │
     Cần: cùng dữ liệu mọi lúc + hỗ trợ Windows ACL + join AD domain
     Yêu cầu: LEAST management overhead
```

Yêu cầu chốt: filesystem dùng chung cho nhiều Windows instance, phải hỗ trợ **Windows ACL** và **AD domain join**, overhead thấp nhất. Đáp án đúng: **C** — FSx for Windows File Server + ASG 3 AZ + user data join AD và mount FSx.

#### Vì sao C đúng

- **Amazon FSx for Windows File Server** là filesystem Windows **native**, dùng protocol **SMB**, hỗ trợ đầy đủ **Windows ACL** — đúng yêu cầu kiểm soát quyền truy cập theo kiểu Windows.
- FSx for Windows tích hợp sẵn với **Microsoft Active Directory** — các instance join AD domain vẫn truy cập share bình thường với đúng permission.
- Là dịch vụ **managed hoàn toàn**: AWS tự patch Windows software bên dưới, tự backup, tự xử lý hardware failure → đúng "least management overhead", không cần tự dựng file server Windows.

#### Vì sao từng đáp án sai bị loại

- **A sai** — **Amazon EFS dùng protocol NFS**, chủ yếu dành cho Linux, **không hỗ trợ Windows ACL**. Dùng cho CMS Windows là sai công cụ ngay từ đầu.
- **B sai** — **FSx for Lustre** là filesystem POSIX-compliant, chỉ dùng được với **Linux-based instance**, không tương thích Windows.
- **D sai** — EBS **Multi-Attach** chỉ cho phép nhiều EC2 cùng gắn một volume khi các instance **nằm trong cùng một Availability Zone**. Đề yêu cầu HA trải 3 AZ → Multi-Attach không đáp ứng được.

#### So sánh nhanh

| Đáp án | Filesystem | Hỗ trợ Windows ACL? | Chạy được đa AZ? |
|---|---|---|---|
| **C (đúng)** | FSx for Windows File Server | Có | Có |
| A | EFS (NFS) | Không | Có (nhưng sai protocol) |
| B | FSx for Lustre | Không (Linux only) | Có (nhưng sai OS) |
| D | EBS Multi-Attach | N/A | **Không** — cùng AZ only |

#### Lưu ý thực tế

- Lựa chọn filesystem chia sẻ luôn phải khớp **hệ điều hành** trước khi xét đến khả năng chịu lỗi: EFS/Lustre = Linux, FSx for Windows = Windows.
- EBS Multi-Attach là tính năng cho volume **io1/io2** dùng trong cluster ứng dụng đặc biệt (ví dụ clustered database trên Linux), không phải giải pháp shared storage đa AZ.

#### Quy tắc nhớ cho thi

- **"Windows + shared storage + ACL + AD domain"** → **FSx for Windows File Server**
- **"EFS"** → chỉ dùng cho Linux (protocol NFS), không hỗ trợ Windows ACL
- **"FSx for Lustre"** → chỉ dùng cho Linux, chủ yếu cho HPC/machine learning workload cần throughput cao
- **"EBS Multi-Attach"** → giới hạn trong **cùng một AZ**, không phải lựa chọn cho kiến trúc đa AZ

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users ──► Web service (semi-structured data, read/write)
             │
Yêu cầu: scale nhanh với spike ngắn nhưng mạnh
             +
         chịu được outage TOÀN REGION
             +
         ưu tiên AWS-managed service
```

Đề cần một kiến trúc **active-active đa Region**, database phải ghi được ở cả 2 Region, compute phải scale cực nhanh để đối phó spike ngắn. Đáp án đúng: **C** — DynamoDB global table (on-demand) + ECS Fargate (ASG) mỗi Region, ALB riêng mỗi Region, Route 53 latency routing + health checks.

#### Vì sao C đúng

- **DynamoDB global table** là multi-Region, **multi-active** — cả hai Region đều ghi/đọc được, không có khái niệm "chỉ primary mới ghi" như một số dịch vụ khác. Khớp hoàn toàn yêu cầu "read and write operations" trên semi-structured data.
- **On-demand capacity mode** cho DynamoDB tự scale theo traffic, không cần provision trước → phù hợp "short but significant load spikes".
- **Fargate** là serverless container — scale container mới **nhanh hơn EC2 nhiều** vì không cần provision EBS, boot OS, chạy user data script → đáp ứng spike ngắn tốt hơn ASG EC2.
- **Route 53 latency routing + health checks**: điều hướng user tới Region khỏe mạnh có latency thấp nhất — đúng kiểu active-active.

#### Vì sao từng đáp án sai bị loại

- **A sai** — DocumentDB **global clusters** chỉ cho **primary cluster ghi được**, secondary chỉ đọc. Vậy không đáp ứng yêu cầu "perform read and write operations" ở cả hai Region khi Region primary gặp sự cố ngay lập tức.
- **B sai** — S3 Cross-Region Replication có **delay lên tới 15 phút**. Khi failover xảy ra, dữ liệu mới nhất ở Region chính có thể **chưa kịp replicate** sang Region phụ — mất dữ liệu, không đáp ứng yêu cầu HA/fault-tolerant.
- **D sai** — Auto Scaling EC2 group cần vài phút để provision EBS, boot OS, chạy user data script → **không đủ nhanh** cho spike ngắn nhưng mạnh như đề yêu cầu.

#### So sánh nhanh

| Đáp án | Database | Compute | Ghi được ở cả 2 Region? | Scale đủ nhanh cho spike? |
|---|---|---|---|---|
| **C (đúng)** | DynamoDB global table | ECS Fargate | Có | Có (container, không cần boot OS) |
| A | DocumentDB global cluster | Lambda + API Gateway | Không — chỉ primary ghi | Có (serverless) nhưng DB fail ghi |
| B | S3 + CRR | Lambda + API Gateway | Có delay ≤15 phút | Có nhưng dữ liệu lệch |
| D | Aurora global database | EC2 ASG | Chỉ primary ghi | Chậm — EC2 cần vài phút |

#### Lưu ý thực tế

⚠️ **Watch** (ghi chú gốc trong đề): không phải "RDS cross-Region replica" — bất kỳ dịch vụ nào có mô hình "chỉ 1 Region được ghi, Region khác chỉ đọc" (Aurora Global Database, DocumentDB global cluster, RDS cross-Region replica) **đều không đáp ứng** yêu cầu "read and write" active-active ở nhiều Region. Chỉ DynamoDB global table thật sự multi-active ghi ở mọi Region.

#### Quy tắc nhớ cho thi

- **"semi-structured data" + "read/write ở nhiều Region" + "chịu Region outage"** → **DynamoDB global table** (multi-active)
- **"spike ngắn nhưng mạnh, cần scale rất nhanh"** → **Fargate** thắng EC2 ASG vì không cần boot OS
- **Aurora/DocumentDB global database/cluster** → chỉ **primary Region ghi được**, không phải lựa chọn khi cần ghi ở nhiều Region đồng thời
- **S3 Cross-Region Replication** → có delay (tới ~15 phút), không phù hợp khi cần zero data loss lúc failover

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
us-east-1 (Region A)          us-east-?/us-west-? (Region B)
┌─────────────────────┐       ┌─────────────────────┐
│ ASG EC2 + ElastiCache│       │ ASG EC2 + ElastiCache│
│ (AOF enabled)        │       │ (AOF enabled)        │
└─────────────────────┘       └─────────────────────┘
      Region A bị MẤT ĐIỆN do storm → ảnh hưởng doanh thu

Yêu cầu: khi Region sập lại, downtime recovery CHỈ ĐƯỢC NGẮN
```

Hệ thống đã chạy **đa Region song song** (multi-Region), vấn đề là cơ chế failover DNS cần đảm bảo traffic chuyển ngay sang Region còn sống. Đáp án đúng: **A** — DNS active-active failover dùng latency-based routing trỏ tới ELB, "Evaluate Target Health" = Yes.

#### Vì sao A đúng

- Hệ thống đã chạy **song song ở nhiều Region** (active-active) — không phải kiểu "một Region chính, một Region đứng chờ" — nên cơ chế DNS phù hợp là **latency-based routing**: định tuyến user tới Region có latency thấp nhất trong số các Region còn khỏe.
- **Evaluate Target Health = Yes**: bắt buộc để Route 53 **tự động loại bỏ** Region/ELB đang unhealthy khỏi vòng chọn route. Nếu không bật cái này, Route 53 vẫn gửi traffic tới resource dù nó đã chết.
- Kết hợp cả hai: khi Region A mất điện, health check fail → Route 53 tự loại ELB của Region A, 100% traffic dồn về Region B gần ngay lập tức → downtime recovery ngắn.

#### Vì sao từng đáp án sai bị loại

- **B sai** — hợp nhất các VPC thành một **private hosted zone** chỉ giải quyết vấn đề DNS resolution **nội bộ VPC**, không cung cấp cơ chế active-active failover cho traffic Internet.
- **C sai** — DNSSEC chỉ chống **DNS spoofing/man-in-the-middle**, không liên quan gì tới failover. Quan trọng hơn: set **Evaluate Target Health = No** nghĩa là Route 53 **vẫn tiếp tục route traffic** tới resource dù health check đang fail → gây mất khả dụng đúng lúc cần failover nhất.
- **D sai** — Transit VPC dùng để đơn giản hóa kết nối **VPN giữa nhiều VPC**, không phải giải pháp DNS/traffic failover.

#### So sánh nhanh

| Đáp án | Cơ chế | Evaluate Target Health | Phù hợp active-active? |
|---|---|---|---|
| **A (đúng)** | Route 53 latency routing | **Yes** | Có |
| B | Private hosted zone hợp nhất VPC | — | Không — chỉ DNS nội bộ VPC |
| C | DNSSEC + failover routing | **No** (sai) | Không — vẫn route tới resource chết |
| D | Transit VPC qua VPN | — | Không — không liên quan DNS failover |

#### Lưu ý thực tế

⚠️ **Watch**: phân biệt rõ hai thuộc tính dễ gây nhầm trong Route 53 — **routing policy** (latency vs failover: latency dùng cho active-active nhiều Region đều đang phục vụ; failover dùng cho primary-standby) và **Evaluate Target Health** (phải luôn là **Yes** nếu muốn Route 53 tự loại resource unhealthy — set "No" là một cái trap thường gặp trong đề thi, nghe tưởng vô hại nhưng vô hiệu hóa toàn bộ cơ chế health-check failover).

⚠️ **Dễ nhầm** với Q16: cả hai bài đều là "DR cho outage toàn Region", nhưng độ gắt RTO ("chỉ cho phép downtime recovery NGẮN") quyết định kiến trúc hoàn toàn khác nhau. Q16 cho RTO rộng (30 phút) cho tầng stateless → đáp án đúng là backup/restore rẻ (daily EC2 snapshot). Q43 chỉ cho downtime ngắn → bắt buộc kiến trúc **active-active đã chạy sẵn ở nhiều Region** (ASG + ElastiCache AOF đang live ở cả hai Region) với DNS latency-routing + health check, **không có bước "restore" nào cả** vì mọi thứ đã online từ trước. Quy tắc: RTO/downtime cho phép **càng ngắn**, kiến trúc DR **càng phải "ấm/nóng" sẵn** (active-active hoặc hot-standby), không còn chỗ cho backup/restore.

#### Quy tắc nhớ cho thi

- **"Active-active đa Region, cần chuyển traffic nhanh khi 1 Region chết"** → **latency routing policy** + **Evaluate Target Health = Yes**
- **"Evaluate Target Health = No"** → luôn là trap, route 53 vẫn gửi traffic tới resource unhealthy
- **DNSSEC** → chỉ chống giả mạo DNS, không liên quan failover/HA
- **Private hosted zone** → DNS nội bộ VPC, không phải cơ chế failover cho user Internet

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem app server ──iSCSI──► AWS Storage Gateway
                                  (Gateway-STORED volume, 5TB)
                                        │
                              Data lưu local on-prem
                              + async backup → S3 dạng EBS snapshot

Disaster: on-prem network hỏng → cần chạy app trên AWS
```

Đây là **Stored Volume Gateway**: dữ liệu chính nằm on-prem, S3 chỉ giữ **EBS snapshot** làm bản backup bất đồng bộ. Đáp án đúng: **D** — tạo EBS snapshot từ Storage Gateway, restore thành EBS volume, attach vào EC2.

#### Vì sao D đúng

- Với **Stored Volume Gateway**, dữ liệu ghi vào volume được backup bất đồng bộ lên S3 **dưới dạng EBS snapshot** — đây là format dữ liệu "sẵn có" trong S3, không phải file thô.
- Muốn dùng lại dữ liệu đó trên AWS, chỉ có một đường: **restore EBS snapshot → tạo EBS volume mới → attach vào EC2** đang chạy application server.
- Đây đúng là quy trình chuẩn Storage Gateway khuyến nghị: snapshot có thể dùng để restore lại volume trên gateway on-prem, **hoặc** dùng làm điểm khởi tạo cho EBS volume mới gắn vào EC2 — chính là tình huống DR trong đề.

#### Vì sao từng đáp án sai bị loại

- **A sai** — dữ liệu Stored Volume Gateway không nằm trong S3 dưới dạng object thông thường để "link" trực tiếp vào EC2; nó là **EBS snapshot**, phải restore thành volume trước.
- **B sai** — **không thể attach trực tiếp AWS Storage Gateway vào một EC2 instance đang chạy app server khác**. Gateway chạy trên AMI riêng của chính nó; muốn dùng dữ liệu phải đi qua bước snapshot → EBS volume.
- **C sai** — tạo **EFS filesystem** từ Storage Gateway **không phải tính năng có thật** của dịch vụ này cho loại Stored Volume Gateway; đây không phải cách để restore dữ liệu — phải dùng EBS Volume.

#### So sánh nhanh

| Đáp án | Cách lấy dữ liệu ra | Đúng với Stored Volume Gateway? |
|---|---|---|
| **D (đúng)** | EBS snapshot → EBS volume → attach EC2 | Đúng — đây là cơ chế thật |
| A | Link S3 bucket vào EC2 | Sai — dữ liệu là snapshot, không phải object S3 |
| B | Attach trực tiếp Storage Gateway vào EC2 app server | Sai — không thể attach như vậy |
| C | Tạo EFS từ Storage Gateway | Sai — không có cơ chế này |

#### Lưu ý thực tế

⚠️ **Lỗi lặp lại**: đây là bài đã từng vấp ở TD Set 2 Q45 trước đây, giờ đã sửa đúng. Ghi chú: **Stored Volume** khác với **Cached Volume** — Stored Volume giữ **toàn bộ dữ liệu local on-prem** (S3 chỉ là bản backup), còn Cached Volume giữ **toàn bộ dữ liệu trên S3**, chỉ cache phần hay dùng ở local. Việc restore dữ liệu ra AWS luôn đi qua **EBS snapshot**, bất kể loại volume.

#### Quy tắc nhớ cho thi

- **"Gateway-stored volume cần dùng lại dữ liệu trên AWS"** → **EBS snapshot → EBS volume → attach EC2**
- Storage Gateway (loại Volume) **không attach trực tiếp** vào EC2 instance khác đang chạy ứng dụng
- **EFS** không phải cơ chế restore cho Volume Gateway — chỉ liên quan tới File Gateway
- Phân biệt: **Stored volume** = data chính ở on-prem, S3 là backup; **Cached volume** = data chính ở S3, on-prem chỉ cache

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Primary Region                         DR Region (≥ 500 miles)
┌─────────────────────┐               ┌─────────────────────┐
│ Redshift cluster      │  cross-region │ Redshift cluster     │
│ Encrypted bằng KMS CMK│──snapshot────►│ (restore từ snapshot) │
└─────────────────────┘    copy         └─────────────────────┘

Yêu cầu: HA + DR ≥500 miles + cluster đang encrypt bằng AWS KMS
```

Mấu chốt của bài: cluster **đã mã hóa bằng KMS**, và KMS key **gắn với một Region cụ thể** — không tự mang sang Region khác được. Đáp án đúng: **B** — tạo snapshot copy grant cho master key ở Region đích, rồi enable cross-region snapshot copy.

#### Vì sao B đúng

- KMS key **chỉ hoạt động trong đúng Region nó được tạo**. Muốn copy snapshot của cluster mã hóa sang Region khác, Redshift cần **quyền thực hiện encryption operation ở Region đích** — đó chính là vai trò của **snapshot copy grant**: cấp cho Redshift quyền dùng một master key ở Region đích để mã hóa lại snapshot khi copy tới đó.
- Sau khi có grant, việc **enable cross-region snapshot copy** trên cluster sẽ tự động copy snapshot (tăng dần, cả automated và manual) sang Region đích một cách managed, không cần tự viết job.
- Đây là cách làm được AWS khuyến nghị chính thức cho cluster có mã hóa KMS cần DR xuyên Region.

#### Vì sao từng đáp án sai bị loại

- **A sai** — dùng CloudFormation deploy cluster ở Region khác + tự backup S3 với CRR: **quá nhiều bước cấu hình thủ công** so với chỉ cần bật cross-region snapshot copy có sẵn trong Redshift — không phải giải pháp "most suitable" khi có tính năng built-in.
- **C sai** — tự viết Lambda job định kỳ chụp snapshot rồi copy sang Region khác: Redshift **đã có tính năng cross-region snapshot copy tích hợp sẵn**, không cần tự động hóa bằng Lambda.
- **D sai** — chỉ enable cross-region snapshot copy **mà thiếu bước snapshot copy grant** cho encryption key ở Region đích → Redshift sẽ **không thể** thực hiện encryption operation ở đó, copy sẽ thất bại vì cluster đang mã hóa bằng KMS.

#### So sánh nhanh

| Đáp án | Snapshot copy grant cho key ở Region đích? | Dùng tính năng built-in Redshift? |
|---|---|---|
| **B (đúng)** | Có | Có |
| A | Không áp dụng (dùng CloudFormation + S3 CRR riêng) | Không |
| C | Không | Không — tự viết Lambda |
| D | **Thiếu** | Có nhưng thiếu bước bắt buộc |

#### Lưu ý thực tế

⚠️ **Lỗi lặp lại** (đã sửa đúng drill lần trước): điểm dễ bỏ sót nhất ở bài này là quên rằng **KMS key là tài nguyên theo Region**. Bất cứ khi nào đề có "cluster/database mã hóa bằng KMS" + "cần copy/replicate sang Region khác", luôn phải nghĩ tới bước cấp quyền cho key ở Region đích trước — nếu không có bước đó, mọi thao tác enable feature cross-region sẽ thất bại vì thiếu quyền mã hóa ở nơi đến.

#### Quy tắc nhớ cho thi

- **"Redshift mã hóa KMS + DR cross-Region"** → **snapshot copy grant** ở Region đích + **enable cross-region snapshot copy**
- **KMS key luôn gắn với 1 Region** — không tự "theo" snapshot khi copy sang Region khác
- Khi thấy tính năng **built-in** của dịch vụ (ví dụ cross-region snapshot copy có sẵn trong Redshift) → ưu tiên hơn giải pháp tự viết Lambda/CloudFormation
- Thiếu bước cấp quyền key ở Region đích = đáp án **luôn sai** dù các bước khác đúng

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Lambda (event source: DynamoDB Streams)
    │
    ▼  deploy version mới qua CodeDeploy
Traffic shift: 10% ngay ──► 90% còn lại sau 5 phút  (ĐÚNG HAI bước)
    │
Yêu cầu thêm: trace event source + downstream calls của Lambda
```

Anh chọn đúng **B**: Canary deployment configuration + enable active tracing (X-Ray).

#### Vì sao B đúng

- **Canary deployment** trên CodeDeploy cho Lambda shift traffic theo **đúng hai increment**: một % traffic đầu tiên ngay, phần còn lại sau một khoảng thời gian định trước — khớp chính xác "10% ngay, 90% sau 5 phút".
- **Active tracing** (enable trên Lambda) tích hợp **AWS X-Ray** → trace được cả **event source** (DynamoDB Streams) kích hoạt Lambda và các **downstream call** mà function thực hiện — đúng yêu cầu thứ hai của đề.

#### Vì sao từng đáp án sai bị loại

- **A sai**: "All-at-once" shift 100% traffic ngay lập tức, không có khái niệm hai increment. Đồng thời **AWS Config không dùng để trace event source/downstream calls** — Config theo dõi cấu hình resource, không phải tracing request.
- **C sai**: "Linear" chia traffic thành **nhiều bước đều nhau**, cách nhau số phút cố định (nhiều increment, không phải đúng hai bước như đề). Và cũng sai công cụ tracing — vẫn là AWS Config, phải là X-Ray.
- **D sai**: "Rolling with additional batch" là deployment configuration **chỉ áp dụng cho Elastic Beanstalk**, **không tồn tại cho Lambda** — dù phần tracing (X-Ray) trong lựa chọn này đúng, phần deployment configuration sai hoàn toàn nền tảng.

#### So sánh nhanh

| Đáp án | Deployment config | Số increment | Công cụ tracing |
|---|---|---|---|
| **B (đúng)** | Canary | 2 (đúng yêu cầu) | X-Ray active tracing |
| A | All-at-once | 1 (100% ngay) | AWS Config (sai) |
| C | Linear | Nhiều, đều nhau | AWS Config (sai) |
| D | Rolling with additional batch | Không áp dụng cho Lambda | X-Ray (đúng nhưng deployment sai) |

#### Lưu ý thực tế ⚠️ Dễ nhầm

- ⚠️ **Dễ nhầm**: Q31 (đúng) vs Q7 (đã làm sai trước) — cùng chủ đề "trace Lambda event source + downstream calls". Quy tắc chắc chắn: tracing cho Lambda **luôn là AWS X-Ray** (bật qua **active tracing**), **không bao giờ** là AWS Config — Config chỉ ghi nhận thay đổi cấu hình resource theo thời gian, hoàn toàn không có khả năng trace lời gọi/request runtime.
- "Rolling with additional batch" là cái tên dễ đánh lừa vì nghe giống một kiểu traffic-shifting hợp lý, nhưng thực chất chỉ tồn tại trong Elastic Beanstalk, không có trong CodeDeploy-for-Lambda.

#### Quy tắc nhớ cho thi

- **"Traffic shift đúng HAI bước (ví dụ X% rồi phần còn lại sau N phút)"** → **Canary**
- **"Traffic shift NHIỀU bước, đều, cách N phút"** → **Linear**
- **"Trace event source + downstream calls"** → **AWS X-Ray (active tracing)**, không bao giờ là AWS Config
- **"Rolling with additional batch"** → chỉ có ở **Elastic Beanstalk**, không có ở Lambda/CodeDeploy

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CloudFormation stack (3-tier app, ASG dùng custom AMI)
    │
Mỗi version mới app = 1 AMI mới
Luồng: update template (AMI mới) ──► gọi UpdateStack API ──► EC2 cũ cần được THAY (replace)
Yêu cầu: KHÔNG downtime
```

Anh chọn đúng **C**: thêm `UpdatePolicy` với `AutoScalingRollingUpdate` trên resource `AWS::AutoScaling::AutoScalingGroup`.

#### Vì sao C đúng

```
CloudFormation template
  AWS::AutoScaling::AutoScalingGroup
    UpdatePolicy:
      AutoScalingRollingUpdate:
        MinSuccessfulInstancesPercent / MaxBatchSize ...
```

- Mặc định, khi update Launch Template/AMI trong CloudFormation, **chỉ instance MỚI tạo sau này** nhận AMI mới — các instance đang chạy **không tự được thay**.
- `UpdatePolicy` với `AutoScalingRollingUpdate` khiến CloudFormation **tự động thực hiện rolling update**: thay instance cũ bằng instance mới theo từng batch khi phát hiện thay đổi trên ASG (ví dụ AMI mới) — vừa đáp ứng "launch new EC2 instances to replace the old ones qua UpdateStack", vừa đảm bảo **không downtime** vì luôn giữ đủ instance đang chạy trong lúc thay dần theo batch.

#### Vì sao từng đáp án sai bị loại

- **A sai**: **Change set** chỉ giúp **xem trước** thay đổi (ví dụ verify đúng AMI mới) trước khi execute — nó **không tự thay thế instance đang chạy**; các instance cũ vẫn nguyên, chỉ instance launch mới sau đó mới nhận AMI mới.
- **B sai**: nhầm attribute — phải dùng **CreationPolicy** (không phải **DeletionPolicy**) nếu muốn có `MinSuccessfulInstancesPercent`; `DeletionPolicy` không có thuộc tính này, và dù đúng attribute thì CreationPolicy/DeletionPolicy cũng không phải cơ chế rolling replace instance khi update AMI.
- **D sai**: tạo **stack mới hoàn toàn** rồi swap Route 53 record là một hình thức blue/green ở tầng CloudFormation, nhưng **không thỏa yêu cầu đề** là phải dùng **UpdateStack API để replace instance trong stack hiện tại** — cách này tạo thêm bước thủ công cập nhật Route 53 mỗi lần deploy.

#### So sánh nhanh

| Đáp án | Cơ chế | Tự thay instance cũ khi UpdateStack? | Zero-downtime? |
|---|---|---|---|
| **C (đúng)** | UpdatePolicy AutoScalingRollingUpdate | Có | Có |
| A | Change set (chỉ preview) | Không | — |
| B | DeletionPolicy (sai attribute) | Không áp dụng | — |
| D | Stack mới + swap Route 53 | Có (nhưng sai stack, thêm bước thủ công) | Có, nhưng không đúng cách đề yêu cầu |

#### Lưu ý thực tế

- Đừng nhầm `CreationPolicy` (chờ signal khi tạo resource mới, có `MinSuccessfulInstancesPercent`) với `DeletionPolicy` (chỉ quyết định resource bị xóa/giữ/snapshot khi stack bị update/delete) — hai attribute này không thay thế nhau được, và `DeletionPolicy` không có `MinSuccessfulInstancesPercent`.
- Thay Launch Template/AMI không tự động trigger instance refresh trừ khi có `UpdatePolicy` hoặc chủ động chạy **instance refresh** riêng.

#### Quy tắc nhớ cho thi

- **"Thay EC2 instance tự động khi update AMI qua CloudFormation, không downtime"** → `UpdatePolicy: AutoScalingRollingUpdate` trên `AWS::AutoScaling::AutoScalingGroup`
- **Change set** → chỉ preview, không tự replace instance đang chạy
- **CreationPolicy** (có MinSuccessfulInstancesPercent) ≠ **DeletionPolicy** (không có thuộc tính này)

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Legacy app → modernized, deploy "cloud native"
Yêu cầu pipeline:
  - Deploy nhiều lần MỖI GIỜ (vài lần/giờ)
  - Rollback NHANH nếu có vấn đề
```

Anh chọn đúng **B**: tạo Staging environment trên Elastic Beanstalk, deploy version mới lên Staging, rồi **swap URL** giữa Staging và Production.

#### Vì sao B đúng

```
Production env (URL: app-prod.elasticbeanstalk.com)   ← traffic hiện tại
Staging env    (URL: app-staging.elasticbeanstalk.com) ← deploy version mới ở đây

Khi version mới OK:
   SWAP CNAME ──► traffic chuyển ngay sang Staging (giờ thành Production)
Khi có vấn đề:
   SWAP CNAME lại ──► rollback NGAY LẬP TỨC
```

- Đây là mô hình **blue/green deployment** trên Elastic Beanstalk: deploy version mới lên một **environment riêng (Staging)** hoàn toàn độc lập với Production, rồi **swap CNAME** để chuyển traffic.
- **Zero-downtime khi deploy**: vì Production vẫn chạy bình thường trong lúc Staging được chuẩn bị, CNAME swap diễn ra tức thì.
- **Rollback nhanh**: chỉ cần swap CNAME lại lần nữa (không phải re-deploy, không phải tái tạo instance) — đúng yêu cầu "quickly rollback".
- Hỗ trợ tốt nhu cầu deploy "nhiều lần mỗi giờ" vì mỗi lần chỉ là một cú swap, không tốn thời gian chuẩn bị lại hạ tầng.

#### Vì sao từng đáp án sai bị loại

- **A sai**: deploy qua AMI mới + replace EC2 instance hiện tại — khả thi, nhưng **rollback chậm** vì phải replace lại instance với AMI cũ, mất nhiều thời gian hơn so với chỉ swap URL.
- **C sai**: Lightsail được thiết kế cho ứng dụng đơn giản, môi trường **dev/test**, không phù hợp production/mission-critical. Việc dùng weighted routing Route 53 để shift traffic "từ từ" cũng khiến rollback chậm hơn (phải tạo lại instance mới + chạy lại user data script).
- **D sai**: dù dùng đúng "AMI + Launch Template + scale-out", việc **rollback vẫn phải deploy lại AMI cũ và scale-out lần nữa** — chậm hơn nhiều so với đơn giản swap URL giữa hai environment.

#### So sánh nhanh

| Đáp án | Cơ chế deploy | Rollback | Phù hợp production? |
|---|---|---|---|
| **B (đúng)** | Blue/green Elastic Beanstalk, swap CNAME | Ngay lập tức (swap lại) | Có |
| A | Replace EC2 bằng AMI mới | Chậm — phải replace lại | Có, nhưng chậm |
| C | Lightsail + weighted routing | Chậm — phải tạo lại instance | Không — chỉ dev/test |
| D | Update Launch Template + scale-out | Chậm — phải deploy lại AMI cũ | Có, nhưng chậm |

#### Lưu ý thực tế ⚠️ Dễ nhầm

- ⚠️ **Dễ nhầm**: Q54 (đúng) đối lập với Q53 (đã làm sai) — cả hai đều về chủ đề "zero-downtime deployment". Quy tắc chung cần nhớ: khi đề cần **deploy nhanh + rollback nhanh**, ưu tiên các pattern **blue/green hoặc immutable** (môi trường mới tách biệt hoàn toàn, chỉ cần swap/switch để chuyển đổi) — tránh các giải pháp cần **replace/redeploy lại instance hiện tại** vì luôn chậm hơn khi rollback.
- Elastic Beanstalk mặc định là "all-at-once" (nhanh nhưng mất dịch vụ tạm thời); muốn tránh downtime hoàn toàn và rollback nhanh, cách chuẩn là blue/green qua CNAME swap.

#### Quy tắc nhớ cho thi

- **"Deploy nhiều lần/giờ + rollback nhanh"** → **blue/green** (deploy ở environment riêng, swap để chuyển traffic và rollback)
- **"Rollback = phải tạo lại/redeploy instance"** → luôn là dấu hiệu đáp án **chậm, không nên chọn**
- **Lightsail** → không dùng cho production mission-critical trong các câu hỏi dạng này

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ASG (EC2) + CodePipeline + CloudFormation templates
    │
Update CloudFormation gần đây ──► gây DOWNTIME lớn cho production
Yêu cầu: giảm khả năng downtime khi deploy LẦN SAU
```

Anh chọn đúng **B**: thêm stage CodeBuild test trên non-prod + dùng CloudFormation change sets để preview + blue/green trên CodeDeploy.

#### Vì sao B đúng

```
Pipeline mới:
  Source → CodeBuild (test tự động trên non-prod)
         → CloudFormation change set (preview thay đổi trước khi apply)
         → CodeDeploy blue/green (deploy, rollback nhanh nếu lỗi)
```

- **CodeBuild stage**: tự động chạy test trên môi trường non-production **trước khi** chạm production — phát hiện lỗi sớm, không phụ thuộc con người kiểm tra thủ công.
- **CloudFormation change sets**: cho phép **xem trước (preview)** chính xác resource nào sẽ bị thay đổi/xóa/thay thế trước khi thực sự apply — giúp phát hiện các thay đổi logic nguy hiểm (chính là nguyên nhân gây downtime lần trước) trước khi chúng xảy ra thật.
- **Blue/green trên CodeDeploy**: deploy lên **environment/instance tách biệt** rồi chuyển traffic, cho phép **rollback nhanh** nếu deployment mới có vấn đề — giảm thời gian ảnh hưởng downtime nếu sự cố vẫn xảy ra.

#### Vì sao từng đáp án sai bị loại

- **A sai**: cfn helper scripts chỉ giúp detect/report điều kiện **trong lúc** deploy, còn việc test trước khi lên production lại giao cho **QA team làm thủ công** — phụ thuộc con người, không tự động hóa như CodeBuild, dễ bỏ sót lỗi.
- **C sai**: plugin IDE + `aws cloudformation validate-template` chỉ bắt được **lỗi cú pháp (syntax)**, **không bắt được lỗi logic** (ví dụ thay đổi có thể làm downtime) — mà chính lỗi logic kiểu này mới là nguyên nhân downtime trong tình huống đề nêu. Testing thủ công ở bước cuối cũng là điểm yếu giống A.
- **D sai**: blue/green đúng hướng, nhưng bước xác minh lại là **manual login vào instance để test** — dễ sai sót do con người, không tự động hóa, không có bước preview thay đổi CloudFormation (change set) trước khi apply.

#### So sánh nhanh

| Đáp án | Test tự động? | Preview thay đổi CloudFormation? | Rollback nhanh (blue/green)? |
|---|---|---|---|
| **B (đúng)** | Có (CodeBuild) | Có (change sets) | Có (CodeDeploy) |
| A | Không (QA thủ công) | Không | Không |
| C | Không (manual testing) | Chỉ check syntax, không phải change set | Không |
| D | Không (manual login + test) | Không | Có, nhưng thiếu test tự động + preview |

#### Lưu ý thực tế ⚠️ Dễ nhầm

- ⚠️ **Dễ nhầm**: Q56 (đúng) cùng chủ đề "zero-downtime deployment" với Q54 (đúng) và đối lập Q53 (đã làm sai). Mẫu số chung cần nhớ: giải pháp đúng luôn kết hợp **test tự động (CodeBuild)** + **preview thay đổi an toàn (change sets)** + **cơ chế rollback nhanh (blue/green)** — bất kỳ đáp án nào dựa vào **manual testing/manual login** đều là dấu hiệu sai trong các câu về giảm downtime CI/CD.
- Change set khác hẳn "validate template": validate chỉ kiểm tra cú pháp JSON/YAML hợp lệ, change set thực sự mô phỏng **impact** của thay đổi lên resource đang chạy (ví dụ sẽ replace hay chỉ update).

#### Quy tắc nhớ cho thi

- **"Giảm downtime khi deploy CI/CD với CloudFormation"** → kết hợp **CodeBuild test tự động** + **CloudFormation change sets** + **CodeDeploy blue/green**
- **"Manual testing / manual login để verify"** → luôn là dấu hiệu đáp án sai (prone to human error)
- **Validate template (IDE plugin/CLI)** → chỉ bắt lỗi cú pháp, không bắt lỗi logic gây downtime

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ECS Cluster ──xử lý intraday data──► ghi kết quả vào DynamoDB table
                                          │
                              Mỗi entry MỚI ──► cần tự động trigger Lambda để verify
Yêu cầu: giải pháp với THAY ĐỔI CẤU HÌNH TỐI THIỂU (minimal configuration changes)
```

Anh chọn đúng **A**: enable DynamoDB Streams để detect entry mới và tự động trigger Lambda.

#### Vì sao A đúng

```
DynamoDB table ──(enable Streams)──► Stream ARN
                                          │
                                 associate với Lambda function
                                          │
                              Item mới được ghi vào table
                                          │
                        AWS Lambda tự poll stream → invoke function
```

- **DynamoDB Streams** là tính năng **có sẵn** của DynamoDB — chỉ cần **enable** trên table hiện tại, không cần thêm service mới, không cần sửa logic ứng dụng ECS đang chạy.
- Khi item mới xuất hiện trong table, một stream record được ghi vào stream ngay lập tức; Lambda **tự động polling** và **invoke function synchronously** khi phát hiện record mới — đúng nghĩa "detect new entries... automatically run tests".
- Đây là thay đổi **tối thiểu**: chỉ bật 1 setting trên DynamoDB table + associate Lambda, không cần migrate dữ liệu, không cần thêm hạ tầng.

#### Vì sao từng đáp án sai bị loại

- **B sai**: dùng **SNS** làm trigger "mỗi khi ECS xử lý xong" là cách gián tiếp và **thêm hẳn một service mới (SNS topic)** cùng logic publish message từ ECS — tốn nhiều configuration hơn so với chỉ enable DynamoDB Streams có sẵn.
- **C sai**: yêu cầu **migrate toàn bộ table sang Amazon DocumentDB** để lấy tích hợp EventBridge — đây là thay đổi **lớn nhất có thể**, động đến cả application logic và dữ liệu, hoàn toàn ngược lại yêu cầu "minimal configuration changes".
- **D sai**: **Systems Manager Automation** được thiết kế để tự động hóa các tác vụ vận hành/bảo trì trên EC2 và resource AWS khác, **không có khả năng detect thay đổi dữ liệu trong DynamoDB table** — sai công cụ hoàn toàn.

#### So sánh nhanh

| Đáp án | Cơ chế detect entry mới | Mức độ thay đổi cấu hình | Phù hợp yêu cầu? |
|---|---|---|---|
| **A (đúng)** | DynamoDB Streams (built-in) | Tối thiểu — chỉ enable + associate | Có |
| B | SNS publish từ ECS mỗi lần xử lý | Thêm service mới, sửa logic ECS | Không — thừa |
| C | Migrate sang DocumentDB + EventBridge | Rất lớn — migrate dữ liệu + app | Không — ngược yêu cầu |
| D | Systems Manager Automation | Không khả thi | Không — sai công cụ |

#### Lưu ý thực tế

- DynamoDB Streams + Lambda trigger là pattern chuẩn cho mọi bài toán "react to data modification trong DynamoDB table" (insert/update/delete) — luôn là lựa chọn "minimal configuration" khi so với các service khác cần thêm hạ tầng hoặc migrate dữ liệu.
- Systems Manager Automation dễ gây nhầm vì tên có "Automation", nhưng phạm vi của nó chỉ là tác vụ quản trị/vận hành (patching, runbook…), không phải data-change detection.

#### Quy tắc nhớ cho thi

- **"Phát hiện entry mới trong DynamoDB table, kích hoạt Lambda, ít thay đổi cấu hình nhất"** → **DynamoDB Streams**
- **"Migrate database sang service khác chỉ để lấy 1 tính năng"** → thường là đáp án sai khi đề yêu cầu "minimal changes"
- **Systems Manager Automation** → không dùng để detect thay đổi dữ liệu trong DynamoDB

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem: NGINX web server + Oracle RAC One Node database
                 │
          migrate sang AWS + cần automated backup

Oracle RAC One Node = cấu hình "always-on" ảo hóa trên 1 máy
```

Mấu chốt bài này: **Oracle RAC không được RDS hỗ trợ** — dù là RAC đầy đủ hay RAC One Node. Đáp án đúng: **D** — chạy cả NGINX và database trên EC2, gắn EBS volume, dùng **Data Lifecycle Manager (DLM)** để tự động snapshot theo lịch.

#### Vì sao D đúng

- Vì **RDS không hỗ trợ Oracle RAC**, database buộc phải chạy trên **EC2 tự quản lý**, gắn EBS volume để lưu data.
- Yêu cầu "automated backup" → **Amazon Data Lifecycle Manager (DLM)** cho EBS snapshot chính là tính năng được xây ra để tự động hóa việc này: định nghĩa lifecycle policy theo tag, tự tạo và tự xóa snapshot theo retention schedule — không cần viết và duy trì script tự chế.
- DLM còn giúp **giảm chi phí lưu trữ** bằng cách tự xóa snapshot cũ hết hạn.

#### Vì sao từng đáp án sai bị loại

- **A sai** và **B sai** (cùng lý do) — cả hai đều chọn deploy database lên **RDS**. RDS **không hỗ trợ Oracle RAC** (kể cả RAC One Node), nên "RDS RAC cluster" trong đề là một khái niệm không khả thi — hai option này sai ngay từ tiền đề.
- **C sai** — chạy đúng cả NGINX và database trên EC2 (đúng hướng), nhưng dùng **shell script tự viết để chạy manual snapshot** — không sai về mặt kỹ thuật, nhưng DLM là giải pháp "tự động hóa" tốt hơn, ít overhead hơn, và còn tự dọn snapshot cũ — khớp hơn với từ khóa "automated backup" trong đề.

#### So sánh nhanh

| Đáp án | Database chạy ở đâu? | Cơ chế backup | RAC hỗ trợ? |
|---|---|---|---|
| **D (đúng)** | EC2 + EBS | **Data Lifecycle Manager** (tự động) | Có (EC2 tự quản lý) |
| C | EC2 + EBS | Shell script tự viết (manual) | Có nhưng backup kém tự động hơn |
| A | RDS | RDS automated backup | **Không** — RDS không hỗ trợ RAC |
| B | RDS Multi-AZ | RDS automated backup | **Không** — RDS không hỗ trợ RAC |

#### Lưu ý thực tế

- Đây là một trường hợp đặc biệt cần nhớ: Amazon RDS **managed database** rất tiện nhưng có giới hạn — **Oracle RAC (bao gồm RAC One Node)** là một trong những feature engine mà RDS **không** hỗ trợ, buộc phải tự host trên EC2.
- Khi phải tự host database trên EC2, luôn ưu tiên **DLM** cho backup tự động hơn là viết shell script + cron — đúng tinh thần "giảm operational overhead" mà AWS luôn khuyến khích.

#### Quy tắc nhớ cho thi

- **"Oracle RAC / RAC One Node"** → RDS **không hỗ trợ** → phải tự host trên EC2 + EBS
- **"automated backup cho EBS"** → **Data Lifecycle Manager (DLM)**, không phải script tự viết
- Thấy đáp án nào dùng **"RDS" + "RAC cluster"** cùng nhau → sai ngay, vì khái niệm này không tồn tại trên RDS

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem tape-based backup infrastructure (nhiều data center)
     │
     Yêu cầu: ARCHIVE dữ liệu nhạy cảm sang AWS
     Giữ nguyên QUY TRÌNH TAPE hiện có, durable + cost-effective
     │
     ▼
   AWS Storage Gateway — loại nào?
```

Đề nói rõ: **"archive sensitive data from the existing on-premises tape-based backup infrastructure"** — tức công ty muốn **giữ nguyên quy trình backup bằng tape** đang dùng, chỉ đổi đích lưu trữ cuối thành AWS. Đáp án đúng: **A** — Tape Gateway, backup lên S3 và archive vào Glacier, dùng đúng quy trình tape-based hiện tại.

#### Vì sao A đúng

- **Tape Gateway** cung cấp giao diện **Virtual Tape Library (VTL)** qua iSCSI — các phần mềm backup hiện tại (đã quen làm việc với tape) coi gateway này như một **tape drive/media changer thật**, không cần thay đổi quy trình backup đang chạy.
- Dữ liệu được lưu dưới dạng **virtual tape cartridge**, backup lên S3, rồi archive xuống **Glacier** để tối ưu chi phí lưu trữ dài hạn — đúng "durable, cost-effective".
- Đây chính là use case Tape Gateway được thiết kế ra để giải quyết: **thay thế physical tape bằng virtual tape trên cloud, giữ nguyên tooling/backup software hiện có.**

#### Vì sao từng đáp án sai bị loại

- **B sai** — **Stored Volume Gateway** không dành cho tape archive; nó phục vụ việc lưu volume iSCSI với backup dạng EBS snapshot, không tương thích với "existing tape-based processes" của đề.
- **C sai** — vẫn dùng Tape Gateway (đúng loại), nhưng chọn lưu tape ở **Virtual Tape Shelf (VTS)** — sai điểm đến. Đề yêu cầu cost-effective archive cho dữ liệu nhạy cảm → nên vào **Glacier**, VTS trong trường hợp này không tối ưu chi phí như Glacier.
- **D sai** — **File Gateway** không phải công cụ cho tape archive; nó dùng để chia sẻ file qua NFS/SMB, không có khái niệm "tape cartridge" hay tương thích với backup software tape hiện tại.

#### So sánh nhanh

| Đáp án | Loại Gateway | Giữ được quy trình tape hiện tại? | Lưu trữ đích |
|---|---|---|---|
| **A (đúng)** | Tape Gateway | Có — VTL giả làm tape thật | S3 → Glacier |
| B | Stored Volume Gateway | Không — là volume iSCSI, không phải tape | S3 (EBS snapshot) |
| C | Tape Gateway | Có | Virtual Tape Shelf (kém cost-effective hơn) |
| D | File Gateway | Không — là file share, không phải tape | S3 → Glacier |

#### Lưu ý thực tế

⚠️ **Dễ nhầm** với Q14 — đây là cặp đối lập quan trọng Anh đã nhầm **3 lần** ở chiều ngược lại, nên cần nắm chắc tiêu chí phân biệt:

```
Q3  (bài này): "archive dữ liệu từ tape infra, GIỮ QUY TRÌNH TAPE"
      → chỉ cần CHUYỂN NGUYÊN DẠNG tape sang cloud, không xử lý nội dung
      → Tape Gateway (VTL giả làm tape thật cho backup software hiện có)

Q14 (đã nhầm): "video trong tape, cần TRÍCH XUẤT metadata/nhận diện mặt"
      → phải LẤY VIDEO RA khỏi tape, đọc được nội dung, rồi đưa qua AI xử lý
      → File Gateway (NFS/SMB share → S3, file đọc được bình thường)
      → sau đó Amazon Rekognition (không phải SageMaker) để nhận diện mặt/vật thể
```

**Câu hỏi tự kiểm tra**: đề có cần MÁY/AI **đọc được nội dung file** bên trong tape để xử lý tiếp (nhận diện, phân tích, transcode...) không?
- **Không, chỉ cần backup/archive y nguyên** → **Tape Gateway**
- **Có, cần trích xuất/xử lý nội dung** → **File Gateway** (file thật, đọc được) rồi mới đưa qua dịch vụ xử lý phù hợp (Rekognition cho ảnh/video, không phải SageMaker notebook tự train)

#### Quy tắc nhớ cho thi

- **"Tape-based backup, giữ quy trình hiện có, chỉ đổi đích lưu"** → **Tape Gateway** → S3 → Glacier
- **"Cần trích xuất/đọc nội dung file từ tape để xử lý tiếp (AI, metadata...)"** → **File Gateway**, không phải Tape Gateway
- **"Nhận diện mặt/vật thể có sẵn catalog"** → **Amazon Rekognition**, không phải SageMaker (SageMaker dùng khi cần tự train model mới)
- **Virtual Tape Shelf** = lưu trữ tape "lạnh" trong Tape Gateway, nhưng **Glacier** thường cost-effective hơn cho archive dài hạn khi đề nhấn "cost-effective"

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem servers (chưa biết rõ workload)
        │
        cần: thu thập config, usage, behavioral data
        để làm TCO analysis TRƯỚC KHI migrate
```

Trọng tâm bài: đây là bước **discovery/thu thập dữ liệu** để lập kế hoạch migration — chưa phải bước migrate thật. Đáp án đúng: **D** — AWS Application Discovery Service.

#### Vì sao D đúng

- **AWS Application Discovery Service** được thiết kế đúng cho giai đoạn **lập kế hoạch migration**: nó thu thập **configuration, usage, và behavior data** từ các server on-prem — chính xác những gì đề yêu cầu.
- Dữ liệu thu thập được lưu dạng encrypted, có thể **export ra CSV** để dùng tính **Total Cost of Ownership (TCO)** và lập kế hoạch migration — khớp 100% với "requirement" của đề.
- Dữ liệu này còn có thể tích hợp với Migration Hub để theo dõi tiến độ migrate sau này, nhưng việc **thu thập dữ liệu + TCO** là do Application Discovery Service thực hiện.

#### Vì sao từng đáp án sai bị loại

- **A sai** — **AWS SAM (Serverless Application Model)** là framework **build serverless application**, hoàn toàn không liên quan tới di chuyển dữ liệu on-prem hay TCO analysis.
- **B sai** — **AWS Migration Hub** chỉ là **nơi theo dõi tiến độ** migration tập trung từ nhiều công cụ AWS/partner khác nhau — nó **không tự thu thập** configuration/usage/behavior data. Application Discovery Service mới là nguồn dữ liệu, Migration Hub chỉ hiển thị.
- **C sai** — **AWS Application Migration Service (MGN)** dùng để **replicate/mirror VM** sang AWS trong lúc migrate thật, không cung cấp dashboard phân tích workload hay hỗ trợ TCO như Application Discovery Service.

#### So sánh nhanh

| Đáp án | Dịch vụ | Vai trò chính | Có tự thu thập config/usage/behavior? |
|---|---|---|---|
| **D (đúng)** | Application Discovery Service | Discovery + TCO | Có |
| B | Migration Hub | Theo dõi tiến độ migration (tổng hợp) | Không — chỉ hiển thị dữ liệu đã có |
| C | Application Migration Service (MGN) | Replicate VM để migrate thật | Không |
| A | SAM | Framework build serverless app | Không liên quan |

#### Lưu ý thực tế

⚠️ **Watch**: Migration Hub và Application Discovery Service **hay bị gộp nhầm** vì chúng tích hợp với nhau — Discovery Service **thu thập** dữ liệu, Migration Hub chỉ là **bảng điều khiển trung tâm** để theo dõi migration dùng data đó (và nhiều công cụ khác). Khi đề hỏi "collect data... TCO analysis" → luôn là Application Discovery Service, không phải Migration Hub.

#### Quy tắc nhớ cho thi

- **"Thu thập config/usage/behavior data trước khi migrate, phục vụ TCO"** → **AWS Application Discovery Service**
- **Migration Hub** → chỉ là dashboard theo dõi tiến độ, không tự thu thập dữ liệu discovery
- **Application Migration Service (MGN)** → dùng để replicate VM lúc **migrate thật**, không phải bước discovery
- **AWS SAM** → framework serverless, không liên quan migration on-prem

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem data center                     Amazon VPC
┌──────────────────────┐               ┌──────────────────────┐
│ VM chạy legacy app     │   cần kết nối │ VM (sau khi move vào  │
│ + nhiều server internal│──PRIVATE &────►│ VPC) phải "reach back" │
│   dependencies         │   DEDICATED   │ tới server nội bộ      │
└──────────────────────┘               └──────────────────────┘

Yêu cầu: kết nối private + dedicated, chọn ĐÚNG 2 trong 5 lựa chọn
```

Yêu cầu chốt: kết nối phải **private** (không qua Internet công khai) và **dedicated** (đường riêng, không chia sẻ) — đây chính là đặc điểm của **AWS Direct Connect**. Đáp án đúng: **B, C** — một network device hỗ trợ BGP/BGP MD5 authentication ở phía data center, cộng với một link Direct Connect.

#### Vì sao B và C đúng — hai lựa chọn tạo thành MỘT giải pháp

- **C — Direct Connect link**: thiết lập kết nối **dedicated qua cáp fiber-optic** giữa router on-prem và router Direct Connect của AWS, cho phép VM trong VPC giao tiếp với server on-prem qua đường riêng, không qua Internet — đúng "private and dedicated".
- **B — network device hỗ trợ BGP + BGP MD5 authentication**: Direct Connect **bắt buộc** phải dùng BGP để trao đổi route giữa hai mạng, và cần thiết bị hỗ trợ BGP MD5 để xác thực kết nối này. Thiếu thiết bị này thì **không thể dựng được Direct Connect link** — nên B là điều kiện cần đi kèm C, không phải là lựa chọn độc lập.
- Hai đáp án này **không đứng riêng lẻ** — phải chọn cả hai mới tạo thành một giải pháp Direct Connect hoàn chỉnh.

#### Vì sao từng đáp án sai bị loại

- **A sai** — Internet Gateway dùng để cho phép truy cập **Internet công khai**, không dùng cho VPN. VPN connection thông thường dựa trên **Virtual Private Gateway (VGW)** + **Customer Gateway**, không phải Internet Gateway.
- **D sai** — Elastic IP là **địa chỉ public**, không cần thiết ở đây vì các instance trong VPC có thể giao tiếp với server on-prem qua **private IP address** thông qua Direct Connect — không cần public IP.
- **E sai** — **Transit VPC** chỉ giúp **đơn giản hóa và giảm số lượng kết nối** khi có nhiều VPC/remote network cần kết nối với nhau, không phải giải pháp cho yêu cầu đơn giản "một VPC cần một kết nối private/dedicated tới on-prem".

#### So sánh nhanh

| Đáp án | Vai trò | Cần cho Direct Connect? |
|---|---|---|
| **B (đúng)** | Network device hỗ trợ BGP + MD5 | Có — bắt buộc |
| **C (đúng)** | Direct Connect link | Có — chính là kết nối cần dựng |
| A | Internet Gateway | Không — IGW dùng cho Internet, VPN cần VGW |
| D | Elastic IP | Không — instance dùng private IP qua DX |
| E | Transit VPC | Không — chỉ cần khi có nhiều VPC/remote network |

#### Lưu ý thực tế

⚠️ **Watch**: Direct Connect luôn đi kèm **BGP** để trao đổi routing table động giữa hai mạng — không giống như VPN (có thể dùng static route). Khi đề nhắc "Direct Connect" mà thiếu nhắc tới BGP/router hỗ trợ BGP, cần tự nhớ rằng thiết bị phía khách hàng **phải** support BGP (và thường kèm MD5 authentication) để Direct Connect hoạt động.

#### Quy tắc nhớ cho thi

- **"Private + dedicated connection tới on-prem"** → **AWS Direct Connect**
- Direct Connect luôn cần **network device hỗ trợ BGP + BGP MD5 authentication** ở phía on-prem
- **VPN** dùng Virtual Private Gateway + Customer Gateway, **không dùng Internet Gateway**
- **Transit VPC** chỉ hữu ích khi có **nhiều** VPC/remote network cần đơn giản hóa kết nối, không phải cho một kết nối đơn giản

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Private subnet                         NAT instance
┌───────────────────┐                 ┌───────────────┐
│ DB servers (xlarge)│ ──traffic ra────►│ Single NAT     │──► Internet
│                    │   Internet       │ instance       │
└───────────────────┘                 └───────────────┘

Patch update DB chạy LÂU → time-out → phải chạy lại thủ công
```

Mấu chốt bài: lỗi không nằm ở network routing (IGW/VGW) hay placement group, mà nằm ở **hành vi xử lý connection timeout khác nhau giữa NAT instance và NAT gateway**. Đáp án đúng: **A** — NAT instance gửi FIN packet khi timeout, khiến connection bị đóng giữa đường; giải pháp là đổi sang NAT Gateway.

#### Vì sao A đúng

- Khi một connection đi qua NAT instance bị **idle quá lâu** (ví dụ patch update chạy nhiều giờ, ít traffic trao đổi), NAT instance sẽ gửi **FIN packet** cho resource phía sau nó để **đóng hẳn connection**, không cố duy trì.
- Việc patch update chạy lâu dẫn đến idle timeout trên NAT instance → connection bị đóng giữa quá trình → patch update "fail" → phải chạy lại thủ công — khớp đúng mô tả hiện tượng trong đề.
- Giải pháp: chuyển sang **NAT Gateway**. NAT Gateway khi timeout sẽ gửi **RST packet** (không phải FIN) cho bên cố duy trì connection — về hành vi mạng khác nhau, và NAT Gateway nói chung có **hiệu năng và khả năng chịu lỗi tốt hơn** NAT instance tự quản lý.

#### Vì sao từng đáp án sai bị loại

- **B sai** — nếu thiếu Internet Gateway, **toàn bộ** giao tiếp ra Internet sẽ fail hoàn toàn, không phải chỉ riêng việc patch update bị timeout không liên tục như mô tả.
- **C sai** — Virtual Private Gateway dùng cho **VPN connection**, không liên quan tới NAT hay patch update timeout trong tình huống này.
- **D sai** — Placement Group chỉ ảnh hưởng tới **khoảng cách vật lý giữa instance** để tối ưu network performance giữa chúng, không liên quan gì tới việc NAT xử lý timeout của traffic đi ra Internet.

#### So sánh nhanh

| Đáp án | Nguyên nhân nêu ra | Đúng bản chất lỗi? |
|---|---|---|
| **A (đúng)** | NAT instance gửi FIN khi timeout | ✅ — đúng, giải pháp là NAT Gateway |
| B | Thiếu Internet Gateway | ❌ — sẽ fail toàn bộ, không phải timeout riêng lẻ |
| C | Thiếu Virtual Private Gateway | ❌ — VGW dùng cho VPN, không liên quan |
| D | Thiếu Placement Group | ❌ — không ảnh hưởng tới NAT timeout |

#### Lưu ý thực tế

⚠️ **Watch**: ghi nhớ chính xác chiều ngược của hành vi — **NAT instance → gửi FIN** khi timeout (đóng hẳn), **NAT Gateway → gửi RST** cho bất kỳ resource nào cố duy trì connection sau khi đã timeout. Đây là điểm kỹ thuật rất dễ bị hỏi đảo chiều (ai gửi FIN, ai gửi RST) trong đề thi thực tế.

#### Quy tắc nhớ cho thi

- **"NAT instance + connection timeout + long-running task fail"** → nguyên nhân là **FIN packet** từ NAT instance → giải pháp **đổi sang NAT Gateway**
- **NAT instance** → gửi **FIN** khi timeout; **NAT Gateway** → gửi **RST** khi timeout
- Đừng nhầm NAT issue với thiếu **Internet Gateway** (sẽ fail toàn bộ, không phải timeout có chọn lọc) hay **Placement Group** (không liên quan traffic ra Internet)

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhân viên công ty ──Internet / corporate network──► ???
                                                         │
                                            EC2 app server (test run)
                                            TUYỆT ĐỐI không bị expose Internet
```

Yêu cầu: chỉ **nhân viên** truy cập được (từ trong lẫn ngoài công ty qua Internet), nhưng EC2 app server **không được** nằm ở nơi có thể bị truy cập trực tiếp từ Internet. Đáp án đúng: **C** — SSL VPN đặt ở public subnet, cài client cho nhân viên, app server đặt ở private subnet.

#### Vì sao C đúng

- **SSL VPN** đặt ở **public subnet** đóng vai trò là "cổng vào" duy nhất mà nhân viên kết nối tới từ Internet — sau khi xác thực thành công qua VPN client, họ mới được cấp quyền truy cập tiếp vào mạng nội bộ.
- **App server đặt ở private subnet**: vì không có route trực tiếp ra Internet Gateway, app server **hoàn toàn không bị expose** ra Internet công khai — chỉ nhân viên đã qua xác thực VPN mới "nhìn thấy" được nó.
- Mô hình này giải quyết đúng cả hai nửa yêu cầu: nhân viên truy cập được từ bất kỳ đâu (qua VPN) + app server không public.

#### Vì sao từng đáp án sai bị loại

- **A sai** — dù dùng IPsec VPN để nhân viên kết nối, nhưng app server lại được đặt ở **public subnet** → vẫn bị expose ra Internet, vi phạm trực tiếp yêu cầu "not be exposed to the Internet".
- **B sai** — Direct Connect là kết nối **dedicated, băng thông cao**, tốn kém và không cần thiết chỉ để phục vụ test run tạm thời của nhân viên; hơn nữa, app server trong đáp án này cũng vẫn nằm ở **public subnet** → vẫn bị lộ.
- **D sai** — dùng ELB terminate SSL cho EC2 instance **không giải quyết được yêu cầu kiểm soát truy cập chỉ cho nhân viên**; quan trọng hơn, app server vẫn đặt ở **public subnet** → vẫn exposed ra Internet.

#### So sánh nhanh

| Đáp án | App server ở subnet nào? | Có bị expose Internet? | Cơ chế truy cập cho nhân viên |
|---|---|---|---|
| **C (đúng)** | Private | **Không** | SSL VPN (public subnet) + client |
| A | Public | Có | IPsec VPN |
| B | Public | Có | Direct Connect (tốn kém, không cần thiết) |
| D | Public | Có | ELB terminate SSL (không kiểm soát truy cập nhân viên) |

#### Lưu ý thực tế

⚠️ **Watch**: điểm chung của cả 3 đáp án sai là **app server luôn ở public subnet**, dù cơ chế kết nối phía trước (IPsec VPN, Direct Connect, ELB) có khác nhau. Chỉ cần thấy "app server đặt ở public subnet" trong một đề yêu cầu "not exposed to Internet" là loại ngay, bất kể lớp bảo vệ phía trước nghe có vẻ chắc chắn đến đâu.

#### Quy tắc nhớ cho thi

- **"Chỉ nhân viên truy cập, app server không được exposed ra Internet"** → **SSL VPN ở public subnet** (cổng vào) + **app server ở private subnet**
- App server ở **public subnet** = luôn bị loại khi đề yêu cầu "not exposed to Internet", bất kể có VPN/ELB/Direct Connect phía trước
- **Direct Connect** không phải lựa chọn cho nhu cầu truy cập tạm thời/thông thường của nhân viên — overkill về chi phí và băng thông

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Scanned forms → S3                 User metadata → RDS PostgreSQL
       │
   SNS notify team
       │
   Nhân viên LOG IN → đọc form → MANUAL extract data → gọi API hệ thống khác
       │
   Yêu cầu: TỰ ĐỘNG hoá, giảm công sức con người, tăng độ chính xác
```

Đề cần một dịch vụ **OCR chuyên biệt cho forms** (không chỉ đọc chữ, mà hiểu cấu trúc form/table), cộng với NLP để trích xuất insight, orchestrate bằng serverless workflow. Đáp án đúng: **D** — Step Functions + Lambda, dùng **Amazon Textract + Amazon Comprehend**. Anh chọn đúng D.

#### Vì sao D đúng

- **Amazon Textract**: không chỉ là OCR thường — nó **hiểu cấu trúc form và table**, trích xuất được key-value pairs từ scanned document, đúng chính xác loại dữ liệu trong bài ("scanned forms").
- **Amazon Comprehend**: dùng NLP để phân tích thêm insight (entity, key phrase…) từ text đã extract, giúp "parse data" sâu hơn.
- **Step Functions + Lambda**: orchestrate pipeline nhiều bước (upload → trigger Textract → Comprehend → lưu S3 → gọi API) mà không cần quản lý server — đúng mô hình serverless tự động hoá hoàn toàn, loại bỏ hoàn toàn bước "nhân viên login & manually extract".

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng **OCR mã nguồn mở tự host trên EKS** — TD nhận định đây "có thể chạy được" nhưng **thêm operational overhead** không cần thiết, khi AWS đã có Textract/Comprehend managed sẵn, tốt hơn hẳn.
- **B sai** vì dùng **Amazon Rekognition** và **Amazon Transcribe** — hai dịch vụ này **sai mục đích hoàn toàn**: Rekognition dùng cho computer vision (ảnh/video, không phải text form), Transcribe dùng cho speech-to-text (âm thanh), không liên quan gì tới OCR trên scanned forms.
- **C sai** vì phải **tự train model SageMaker để làm OCR** — tốn công, tốn thời gian, trong khi AWS đã cung cấp sẵn Textract/Comprehend là managed service chuyên biệt cho đúng use case này.

#### So sánh nhanh

| Đáp án | Dịch vụ OCR/NLP | Vấn đề |
|---|---|---|
| **D (đúng)** | Textract + Comprehend | Không có — đúng chuẩn cho scanned forms |
| A | OCR open-source trên EKS | Overhead vận hành cao, không cần thiết |
| B | Rekognition + Transcribe | Sai mục đích — vision & speech, không phải document OCR |
| C | SageMaker tự train | Tốn công train model trong khi có sẵn managed service |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** Amazon Rekognition **chỉ xử lý ảnh/video** (nhận diện object, face, scene) — nó **không phải dịch vụ OCR cho document/form**. Khi đề nói "scanned forms", "extract data from documents" → luôn nghĩ tới **Textract**, không phải Rekognition. Transcribe chỉ liên quan tới âm thanh, hoàn toàn không xuất hiện trong bài toán document.

#### Quy tắc nhớ cho thi

- **"Scanned forms / document OCR / key-value từ table"** → **Amazon Textract**
- **"Trích insight từ text (entity, sentiment, key phrase)"** → **Amazon Comprehend**
- **"Ảnh/video nhận diện object/face"** → Amazon Rekognition (không liên quan OCR document)
- **"Speech-to-text"** → Amazon Transcribe (không liên quan OCR document)
- **"Tự động hoá nhiều bước serverless"** → Step Functions + Lambda

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
HPC cluster — tightly-coupled compute + storage
200 nodes → tăng lên 1000 nodes → performance TỆ HƠN
Storage: Amazon EFS share chung
Yêu cầu: đạt maximum performance (Select THREE)
```

Đề cho 6 lựa chọn pha trộn giữa network, placement, và storage. Đáp án đúng: **A, C, F** — cluster placement group trong 1 AZ, EFA network interface, và FSx for Lustre thay EFS. Anh chọn đúng cả ba.

#### Vì sao A, C, F đúng

- **A — Cluster placement group, 1 Availability Zone**: HPC tightly-coupled cần **low-latency node-to-node communication**; cluster placement group gói các instance lại gần nhau trên cùng hạ tầng vật lý trong 1 AZ, giảm độ trễ network giữa node.
- **C — Elastic Fabric Adapter (EFA)**: network interface chuyên biệt cho HPC, dùng **OS bypass** để giảm latency/jitter khi giao tiếp liên-node ở quy mô lớn — cần thiết khi scale lên hàng nghìn core.
- **F — Amazon FSx for Lustre thay EFS**: Lustre cung cấp throughput multiple GB/s và hàng trăm nghìn IOPS, đúng cho workload HPC cần storage theo kịp tốc độ compute — còn EFS không thiết kế cho mức tải 1000 instance truy cập đồng thời.

#### Vì sao từng đáp án sai bị loại

- **B sai** vì gắn **nhiều network interface** chỉ tăng performance của *từng node riêng lẻ*, nhưng **Amazon EFS vẫn là bottleneck chung** khi quá nhiều instance truy cập đồng thời — giải pháp đúng là đổi hẳn sang FSx for Lustre, không phải vá thêm network interface.
- **D sai** vì **trải EC2 instance ra nhiều Availability Zone** đi ngược lại hoàn toàn nguyên tắc HPC tightly-coupled — khoảng cách vật lý giữa các AZ làm tăng latency giao tiếp giữa node, hạ performance thêm (đúng như triệu chứng "bigger cluster performed below expectations").
- **E sai** vì **EBS Throughput Optimized volumes không share được giữa nhiều instance** ở quy mô này — chỉ Provisioned IOPS SSD mới hỗ trợ Multi-Attach, và dù vậy cũng không phải thiết kế cho cluster HPC chia sẻ storage như EFS/Lustre.

#### So sánh nhanh

| Đáp án | Vấn đề giải quyết | Đúng/Sai |
|---|---|---|
| **A** | Latency network giữa node (placement) | ✅ |
| **C** | Latency network giữa node (interface) | ✅ |
| **F** | Bottleneck storage (EFS → Lustre) | ✅ |
| B | Network per-node, không fix shared storage | ❌ |
| D | Trải AZ → tăng latency, phá tightly-coupled | ❌ |
| E | EBS không share được ở quy mô lớn | ❌ |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** Amazon EFS là shared file system tốt cho nhiều use case general-purpose, nhưng **không phải scratch storage cho HPC** — nó không đạt throughput/IOPS cần thiết khi hàng nghìn node truy cập đồng thời tập tin lớn. Thấy "tightly-coupled HPC" + "shared file system chậm" → nghĩ ngay tới **FSx for Lustre**, không phải cố gắng tối ưu EFS hay EBS.

#### Quy tắc nhớ cho thi

- **"Tightly-coupled HPC, cần low latency giữa node"** → **Cluster placement group** (1 AZ) + **EFA**
- **"Shared storage cho HPC, cần throughput/IOPS cao"** → **Amazon FSx for Lustre**, không phải EFS hoặc EBS
- **"Trải nhiều AZ"** → tăng latency, **ngược** với mục tiêu HPC tightly-coupled
- **EBS Multi-Attach** → chỉ hỗ trợ Provisioned IOPS SSD, không hỗ trợ Throughput Optimized

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Trip planner: ALB ── ASG (3 AZ) ── Multi-AZ RDS
Bình thường: steady-state load
Sự kiện lớn (concert, thể thao): spike → utilization >90%
Yêu cầu: recover nhanh khi 1 AZ fail lúc peak, PHẢI cost-effective nhất
```

Đề yêu cầu cân bằng giữa 2 mục tiêu: **cost-effective** và **high availability khi AZ fail lúc đang peak**. Đáp án đúng: **A** — tăng threshold ASG để scale across AZ, Reserved cho steady-state, kết hợp On-Demand + Spot cho phần peak, scale down sau peak. Anh chọn đúng A.

#### Vì sao A đúng

- **Reserved Instances cho steady-state**: vì baseline traffic ổn định, dùng Reserved giảm chi phí dài hạn — đúng nguyên tắc "Reserved Instances recommended for applications with steady state usage".
- **On-Demand + Spot cho peak**: khi traffic spike (concert, sự kiện), scale thêm bằng On-Demand (ổn định, không bị gián đoạn) kết hợp Spot (rẻ) để xử lý phần tải tạm thời — sau đó **scale down khi hết peak** để tiết kiệm, đúng tinh thần elastic/cost-effective.
- **Tăng capacity + scaling threshold của ASG để scale lên tất cả AZ**: khi 1 AZ fail, ASG vẫn còn khả năng scale thêm ở 2 AZ còn lại để bù tải — đáp ứng đúng yêu cầu "quickly recover khi 1 AZ fail lúc peak".

#### Vì sao từng đáp án sai bị loại

- **B sai** vì **6 Reserved + Spot instance mỗi AZ** là cấu hình **quá tốn kém** (18 Reserved instance cố định) dù có Spot bổ sung, và **thiếu Auto Scaling** để điều chỉnh theo traffic thực tế — không linh hoạt, lãng phí khi traffic thấp.
- **C sai** vì tuy "cost-effective" (chỉ 1 On-Demand + 2 Spot mỗi AZ) nhưng **không dùng Auto Scaling**, khiến availability bị đe dọa: nếu On-Demand instance (duy nhất) fail, AZ đó chỉ còn lại 2 Spot — mà Spot instance **có thể bị interrupt bất kỳ lúc nào**, không đủ ổn định để gánh steady-state load.
- **D sai** vì thay **toàn bộ** Reserved/On-Demand bằng Spot — đây là lựa chọn rẻ nhất nhưng **bất ổn nhất**, vì Spot instance có thể bị AWS thu hồi (interrupt) bất cứ lúc nào, đe doạ trực tiếp đến tính khả dụng của website đúng lúc cần HA nhất.

#### So sánh nhanh

| Đáp án | Steady-state | Peak | Auto Scaling | Rủi ro |
|---|---|---|---|---|
| **A (đúng)** | Reserved | On-Demand + Spot | ✅ | Thấp — có ASG linh hoạt |
| B | 6 Reserved+Spot/AZ (cố định) | — | ❌ | Tốn kém, không linh hoạt |
| C | 1 On-Demand/AZ | 2 Spot/AZ | ❌ | Spot interrupt → mất HA |
| D | Toàn Spot | Toàn Spot | Chỉ 1 AZ | Rẻ nhất nhưng bất ổn nhất |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** "Cost-effective nhất" **không đồng nghĩa với "rẻ nhất tuyệt đối"** — đề luôn gài một lựa chọn toàn Spot (D) trông có vẻ rẻ nhất, nhưng phá vỡ yêu cầu HA. Phải đọc kỹ: bài toán cần **cân bằng** giữa chi phí và độ ổn định — Reserved cho phần tải chắc chắn sẽ dùng (steady-state), chỉ dùng On-Demand/Spot cho phần tải không chắc chắn (peak).

#### Quy tắc nhớ cho thi

- **"Steady-state usage"** → **Reserved Instances** để tối ưu chi phí dài hạn
- **"Traffic spike tạm thời, không chắc chắn"** → **On-Demand + Spot**, scale down sau peak
- **"Cần HA khi peak"** → phải có **Auto Scaling** phân bổ qua nhiều AZ, không cấu hình tĩnh (fixed count)
- **Toàn bộ Spot** → rẻ nhất nhưng rủi ro gián đoạn cao nhất, không phù hợp khi cần đảm bảo HA

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
200 TB shared file system (EC2 cluster chạy 24/7 chỉ để giữ data)
        │
Mỗi cuối tháng: chạy job 72 giờ cần high-performance shared storage
        │
Yêu cầu: giảm tối đa chi phí storage tier, vẫn giữ performance lúc chạy job
```

Mấu chốt: dữ liệu chỉ cần **high-performance access trong 72 giờ/tháng**, còn lại 99% thời gian **không cần** cluster EC2 chạy liên tục để giữ file. Đáp án đúng: **A** — S3 Intelligent-Tiering làm nơi lưu lâu dài + FSx for Lustre **lazy-loading** tạo tạm trong lúc job chạy, xoá sau khi xong. Anh chọn đúng A.

#### Vì sao A đúng

- **S3 Intelligent-Tiering cho 200TB lưu trữ dài hạn**: tự động di chuyển dữ liệu giữa các tier truy cập để tối ưu chi phí mà không cần quản lý thủ công, phù hợp khi pattern truy cập không đều (chỉ dùng 72h/tháng).
- **FSx for Lustre + lazy-loading từ S3**: Lustre trình diện S3 objects như file hệ thống POSIX-compliant, tốc độ cao — "lazy-loading" nghĩa là chỉ load dữ liệu khi thực sự cần đọc, không phải copy toàn bộ 200TB trước.
- **Tạo FSx khi cần job, xoá sau khi xong**: đây là điểm quyết định tiết kiệm chi phí lớn nhất — **không cần cluster EC2/storage chạy 24/7**, chỉ trả tiền cho storage tier (S3) liên tục + FSx trong đúng 72 giờ mỗi tháng.

#### Vì sao từng đáp án sai bị loại

- **B sai** vì **Amazon EFS tốn chi phí cao hơn đáng kể so với S3** cho cùng khối lượng lưu trữ — ngay cả với EFS Standard-IA, chi phí vẫn cao hơn việc dùng S3 + FSx tạm thời.
- **C sai** vì **S3 Glacier Instant Retrieval** được thiết kế cho dữ liệu **truy cập khoảng 1 lần/quý** (archive lâu dài), không phù hợp với pattern "mỗi tháng 1 lần" — ngoài ra Glacier còn tính **phụ phí retrieval** khi lấy dữ liệu ra khỏi cold storage, làm tăng chi phí thực tế so với Intelligent-Tiering.
- **D sai** vì **Mountpoint for Amazon S3** được tối ưu cho workload **đọc tuần tự, read-heavy**, không đạt được throughput/latency cần cho financial modeling cường độ cao; nó cũng **không POSIX-compliant đầy đủ** và không hỗ trợ parallel access hiệu quả như FSx for Lustre.

#### So sánh nhanh

| Đáp án | Storage lâu dài | Compute storage lúc job | Vấn đề |
|---|---|---|---|
| **A (đúng)** | S3 Intelligent-Tiering | FSx for Lustre (lazy-load, tạm) | Không có |
| B | EFS Standard-IA | — (dùng trực tiếp EFS) | EFS đắt hơn S3 nhiều |
| C | S3 Glacier Instant Retrieval | FSx for Lustre (lazy-load, tạm) | Glacier dành cho truy cập ~1 lần/quý + phụ phí retrieval |
| D | S3 (Mountpoint) | — (mount trực tiếp) | Không đủ throughput/POSIX cho workload intensive |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** "Giảm chi phí tối đa" dễ khiến chọn nhầm sang **Glacier** (nghe có vẻ rẻ nhất) — nhưng Glacier chỉ tối ưu khi truy cập **cực kỳ hiếm** (hàng quý) và có phụ phí retrieval; còn ở đây dữ liệu được dùng **mỗi tháng**, nên Intelligent-Tiering là lựa chọn đúng cân bằng giữa giá và tốc độ truy cập.

#### Quy tắc nhớ cho thi

- **"Shared storage chỉ cần performance cao trong khoảng thời gian ngắn, định kỳ"** → **S3 (lưu lâu dài) + FSx for Lustre lazy-loading (tạm, theo nhu cầu)**
- **"Truy cập dữ liệu mỗi tháng"** → S3 Intelligent-Tiering hoặc Standard-IA, **không** dùng Glacier (dành cho quý/năm)
- **EFS** → thường **đắt hơn** S3 cho cùng dung lượng lưu trữ lớn
- **Mountpoint for S3** → chỉ tốt cho read-heavy tuần tự, không thay được FSx for Lustre cho workload HPC/financial modeling

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

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
National library — 50 TB books/articles/written materials
         │
Dynamic website cần: SEARCH feature cho collection
Đã dùng: Amazon Pinpoint (email notification)
         │
Yêu cầu: giải pháp phù hợp nhất cho storage + search + hosting
```

Bài toán có 3 cấu phần: nơi lưu 50TB dữ liệu, dịch vụ tìm kiếm, và nơi host website. Đáp án đúng: **B** — CloudFormation deploy S3 (storage) + OpenSearch (search) + EC2 (host website). Anh chọn đúng B.

#### Vì sao B đúng

- **S3 cho 50TB lưu trữ**: S3 là giải pháp lưu trữ durable, scalable, chi phí thấp cho khối lượng dữ liệu lớn như sách/tài liệu viết — đúng vai trò "data lake" cho big data use case này.
- **OpenSearch cho search feature**: đây là dịch vụ **chuyên biệt cho full-text search, faceting, filtering** trên dataset lớn — đúng chính xác yêu cầu "search feature để người dùng tìm trong collection" trên dynamic website.
- **EC2 host dynamic website**: vì ứng dụng là **dynamic website** (không phải static), cần compute để chạy logic — EC2 đáp ứng đúng, S3 bản thân không host được dynamic content.
- **CloudFormation**: triển khai các resource này dưới dạng Infrastructure as Code, phù hợp để quản lý một kiến trúc nhiều thành phần.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng **Multi-AZ RDS làm storage chính cho 50TB dữ liệu + search** — TD chỉ ra: dùng RDS cho việc này **khả thi về kỹ thuật nhưng rất đắt**; RDS không được thiết kế tối ưu cho full-text search ở quy mô này, nên không phải lựa chọn cost-effective và phù hợp.
- **C sai** vì **Amazon Kinesis** là dịch vụ **streaming dữ liệu thời gian thực**, không phải giải pháp **lưu trữ lâu dài**; dùng Kinesis để "lưu" 50TB sách/tài liệu là sai hoàn toàn mục đích thiết kế của dịch vụ.
- **D sai** vì S3 **không host được dynamic website** (S3 chỉ host static website), và S3 **không có tính năng search built-in** đủ mạnh để đáp ứng yêu cầu tìm kiếm trên collection sách/tài liệu.

#### So sánh nhanh

| Đáp án | Storage | Search | Host website |
|---|---|---|---|
| **B (đúng)** | S3 | OpenSearch | EC2 |
| A | RDS Multi-AZ | (RDS, không tối ưu, đắt) | EC2 |
| C | Kinesis (sai mục đích) | — | EC2 |
| D | S3 + S3 | "Native search" (không tồn tại) | S3 (không host dynamic) |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** S3 là lựa chọn lưu trữ cực tốt nhưng **không có search engine tích hợp** — đề hay gài lựa chọn "dùng tính năng search sẵn có của S3" (như D) như một cái bẫy, vì **S3 hoàn toàn không có tính năng full-text search** cho nội dung lưu trữ. Khi cần search thật, luôn phải thêm **OpenSearch** (hoặc CloudSearch) vào kiến trúc.

#### Quy tắc nhớ cho thi

- **"Lưu trữ lớn (chục/trăm TB), không cần transaction phức tạp"** → **Amazon S3**
- **"Cần full-text search/filter trên dataset lớn"** → **Amazon OpenSearch Service**
- **"Dynamic website"** → cần compute (EC2/container/Lambda), **S3 không host được**
- **Amazon Kinesis** → chỉ dùng cho streaming dữ liệu real-time, không phải long-term storage

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
