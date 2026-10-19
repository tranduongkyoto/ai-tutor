# TD Set 4 — Timed (Gate 2, 2026-10-19) — Wrong Answer Review (25 questions)

Source: `td4_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td4_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q5](#q5) | ☐ | ☐ | ☐ |
| A | [Q28](#q28) | ☐ | ☐ | ☐ |
| A | [Q57](#q57) | ☐ | ☐ | ☐ |
| A | [Q58](#q58) | ☐ | ☐ | ☐ |
| A | [Q62](#q62) | ☐ | ☐ | ☐ |
| A | [Q64](#q64) | ☐ | ☐ | ☐ |
| B | [Q13](#q13) | ☐ | ☐ | ☐ |
| B | [Q38](#q38) | ☐ | ☐ | ☐ |
| B | [Q51](#q51) | ☐ | ☐ | ☐ |
| B | [Q66](#q66) | ☐ | ☐ | ☐ |
| C | [Q15](#q15) | ☐ | ☐ | ☐ |
| C | [Q21](#q21) | ☐ | ☐ | ☐ |
| C | [Q40](#q40) | ☐ | ☐ | ☐ |
| C | [Q54](#q54) | ☐ | ☐ | ☐ |
| D | [Q14](#q14) | ☐ | ☐ | ☐ |
| D | [Q41](#q41) | ☐ | ☐ | ☐ |
| D | [Q63](#q63) | ☐ | ☐ | ☐ |
| E | [Q17](#q17) | ☐ | ☐ | ☐ |
| E | [Q19](#q19) | ☐ | ☐ | ☐ |
| E | [Q29](#q29) | ☐ | ☐ | ☐ |
| E | [Q34](#q34) | ☐ | ☐ | ☐ |
| E | [Q44](#q44) | ☐ | ☐ | ☐ |
| E | [Q56](#q56) | ☐ | ☐ | ☐ |
| E | [Q65](#q65) | ☐ | ☐ | ☐ |
| E | [Q74](#q74) | ☐ | ☐ | ☐ |

---

# Group A — Known rule, new wording (EventBridge, RDS Proxy/Aurora, DX gateway, Redshift snapshot copy, placement group, SSM parameters) (6)

<a id="q5"></a>

## Q5

A digital banking company runs its production workload on the AWS cloud. The company has enabled multi-region support on an AWS CloudTrail trail. As part of the company security policy, the creation of any IAM users must be approved by the security team. When an IAM user is created, all of the permissions from that user must be removed automatically. A notification must then be sent to the security team to approve the user creation.

Which of the following options should the solutions architect implement to meet the company requirements? (Select THREE.)

- **A.** Create a rule in Amazon EventBridge that will check for patterns in AWS CloudTrail API calls with the CreateUser eventName.
- **B.** Use Amazon AWS Audit Manager to continually audit newly created users and send a notification to the security team.
- **C.** Use Amazon EventBridge to invoke an AWS Step Function state machine that will remove permissions on the newly created IAM user.
- **D.** Send a message to an Amazon Simple Notification Service (Amazon SNS) topic. Have the security team subscribe to the SNS topic.
- **E.** Configure an event filter in AWS CloudTrail for the CreateUser event and send a notification to an Amazon Simple Notification Service (Amazon SNS) topic.
- **F.** Use Amazon EventBridge to invoke an AWS Fargate tasks that will remove permissions on the newly created IAM user.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, D · **You picked:** D, E, F

🔑 **Key words:** CreateUser, auto remove permissions, notify security team; select three

🪤 **Your trap:** 🔁 Picked E (CloudTrail cannot send SNS notifications) and F (EventBridge cannot invoke Fargate tasks directly); missed the EventBridge CreateUser rule (A) and Step Functions (C).

🧠 **Rule:** CloudTrail API event -> EventBridge rule -> Step Functions (remediate) + SNS (notify). CloudTrail alone does not notify.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IAM CreateUser ──► CloudTrail (multi-region) ──► EventBridge rule (pattern: eventName = CreateUser)
                                                    ├──► target 1: Step Functions ──► gỡ toàn bộ permission của user
                                                    └──► target 2: SNS topic ──► security team (subscribe) duyệt
```

Yêu cầu chốt: **tự động** gỡ quyền + **thông báo** security team. Đáp án đúng: **A + C + D** (một pipeline duy nhất trên EventBridge). Anh chọn D, E, F: đúng D, sai E và F, thiếu A và C.

⚠️ Lỗi lặp lại: Anh đã học rule "event-driven phản ứng với API call = **CloudTrail + EventBridge**", nhưng đề đổi cách diễn đạt (E dùng "event filter in CloudTrail") nên bị nhầm. CloudTrail chỉ **ghi** sự kiện; EventBridge mới là nơi **match pattern và gọi target**.

#### Ba đáp án đúng ghép thành một giải pháp

- **A** - rule EventBridge match pattern CloudTrail API call có `eventName = CreateUser`. Đây là "cái bắt sự kiện", thiếu nó thì C và D không có gì kích hoạt.
- **C** - EventBridge target là **Step Functions** state machine, thực hiện chuỗi hành động gỡ permission (detach policy, xóa inline policy, gỡ khỏi group...). Step Functions điều phối được nhiều bước, có retry.
- **D** - SNS topic, security team subscribe. EventBridge gửi message vào topic khi rule khớp.

#### Vì sao E sai (Anh chọn)

E trông hợp lý vì CloudTrail "thấy" CreateUser. Nhưng theo TD: CloudTrail có thể **tìm kiếm/lọc** event để xem, **không** cấu hình để gửi thông báo SNS theo từng event. Muốn phản ứng với event phải qua EventBridge.

#### Vì sao F sai (Anh chọn)

F thay Step Functions bằng Fargate task. TD loại F vì "EventBridge cannot directly invoke Fargate tasks".

📝 Ghi chú kỹ thuật: thực tế EventBridge có hỗ trợ target là **ECS task** (kể cả launch type Fargate), nên câu giải thích của TD không hoàn toàn khớp thực tế. Trong đề vẫn giữ đáp án **C** (Step Functions) là đúng; F cũng chạy kiểu "tự dựng container + code" nặng hơn cần thiết so với state machine.

#### Các đáp án sai còn lại

- **B** (Audit Manager): dùng map compliance framework và thu thập evidence, không phải công cụ phản ứng realtime với `CreateUser`, không gỡ quyền.

| Thành phần | Vai trò | Đáp án |
|---|---|---|
| CloudTrail | Ghi API call (nguồn sự kiện) | không phải chỗ cấu hình notify |
| EventBridge rule | Match pattern, route tới target | A |
| Step Functions | Gỡ permission tự động | C |
| SNS | Báo security team | D |

#### Quy tắc nhớ cho thi

- **Thấy "khi API call X xảy ra thì tự động làm Y + báo team"** → **CloudTrail → EventBridge rule → target (Step Functions/Lambda) + SNS**
- **"CloudTrail event filter gửi SNS"** → bẫy, CloudTrail không làm việc này; luôn qua **EventBridge**
- **"Audit Manager"** → compliance evidence, không phải remediation
- **Multi-select** → chọn đủ bộ ba: **bắt sự kiện (A) + hành động (C) + thông báo (D)**

### TD explanation

Using IAM, you can manage access to AWS services and resources securely. You can create and manage AWS users and groups and use permissions to allow and deny those users and groups access to AWS resources.

You can create an **Amazon EventBridge**  rule with an event pattern that matches a specific IAM API call or multiple IAM API calls. Then, associate the rule with an **Amazon Simple Notification Service (Amazon SNS)**  topic. When the rule runs, an SNS notification is sent to the corresponding subscriptions.

Amazon EventBridge works with **AWS CloudTrail** , a service that records actions from AWS services. CloudTrail captures API calls made by or on behalf of your AWS account from the EventBridge console and to EventBridge API operations.

Using the information collected by CloudTrail, you can determine what request was made to EventBridge, the IP address from which the request was made, who made the request, when it was made, and more. When an event occurs in EventBridge, CloudTrail records the event in Event history. You can view, search, and download recent events in your AWS account.

![image](https://media.tutorialsdojo.com/sap_cloudtrail_event_notification.png)

The option that says: **Use Amazon EventBridge to invoke an AWS Step Function state machine that will remove permissions on the newly created IAM user**  is correct. When Amazon EventBridge detects a pattern from the specified events, it can trigger an AWS Step Function that has specific actions.

The option that says: **Send a message to an Amazon Simple Notification Service (Amazon SNS) topic. Have the security team subscribe to the SNS topic**  is correct. If you create a pattern in Amazon EventBridge, it can then send a message to an SNS Topic once the event is detected.

The option that says: **Create a rule in Amazon EventBridge that will check for patterns in AWS CloudTrail API calls with the CreateUser eventName**  is correct. With Amazon EventBridge, you define patterns to scan events that happen in your AWS account, such as creating an IAM user.

The option that says: **Configure an event filter in AWS CloudTrail for the CreateUser event and send a notification to an Amazon Simple Notification Service (Amazon SNS) topic**  is incorrect. You can filter events on CloudTrail by searching for keywords, however, you can’t configure it to send notifications to Amazon SNS. You should use EventBridge for this scenario.

The option that says: **Use Amazon AWS Audit Manager to continually audit newly created users and send a notification to the security team**  is incorrect. AWS Audit Manager is used to map compliance requirements to AWS usage data with prebuilt and custom frameworks and automated evidence collection, not for scanning IAM user creation events.

The option that says: **Use Amazon EventBridge to invoke an AWS Fargate tasks that will remove permissions on the newly created IAM user**  is incorrect. Amazon EventBridge cannot directly invoke AWS Fargate tasks.

**References:**

[https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/iam-eventbridge-sns-rule/](https://aws.amazon.com/premiumsupport/knowledge-center/iam-eventbridge-sns-rule/)

[https://aws.amazon.com/premiumsupport/knowledge-center/sns-email-notifications-eventbridge/](https://aws.amazon.com/premiumsupport/knowledge-center/sns-email-notifications-eventbridge/)

**Check out these Amazon CloudWatch and AWS Simple Notification Service Cheat Sheets:**

[https://tutorialsdojo.com/amazon-cloudwatch/](https://tutorialsdojo.com/amazon-cloudwatch/)

[https://tutorialsdojo.com/amazon-sns/](https://tutorialsdojo.com/amazon-sns/)

</details>

<a id="q28"></a>

## Q28

A stock trading company is running its application on the AWS cloud. The mission-critical database is hosted on an Amazon RDS for MySQL instance deployed in a Multi-AZ configuration. An AWS Backup rule is in place to take automated snapshots hourly. The operations team recently performed an RDS database failover test and found that it caused an outage of approximately 40 seconds.

The management has asked the solutions architect to implement a solution that will reduce the outage to less than 20 seconds. Most connections should stay alive during failovers except for the ones that are in the middle of a transaction or SQL statement. New database connections should still be accepted, and the incoming write requests should be queued until the failover completes.

Which of the following options should the solutions architect implement to meet the company’s requirements? (Choose THREE.)

- **A.** Enable the Amazon RDS Optimized Writes feature and create an Amazon ElastiCache for Memcached cluster in front of the database layer to cache any frequently requested queries.
- **B.** Set up an Amazon RDS Proxy in front of the database layer to automatically route traffic to healthy RDS instances.
- **C.** Migrate the Amazon RDS for MySQL cluster to an Amazon Aurora for MySQL cluster.
- **D.** Ensure that Multi-AZ is enabled on Amazon Aurora and create one or more Aurora Replicas.
- **E.** Enable the Amazon RDS Optimized Reads feature and launch an Amazon ElastiCache for Redis cluster in front of the database layer to temporarily serve database queries in case of RDS failure.
- **F.** Ensure that Multi-AZ is enabled on Amazon RDS for MySQL and create one or more read replicas to ensure quick failover.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C, D · **You picked:** B, E, F

🔑 **Key words:** cut RDS Multi-AZ failover from 40s to under 20s, keep connections alive, queue writes; choose three

🪤 **Your trap:** 🔁 Picked E (Redis cache) and F (read replicas on RDS MySQL); caches cannot queue writes and RDS replicas don't give fast failover. Need RDS Proxy + Aurora Multi-AZ replicas.

🧠 **Rule:** Faster failover, preserved connections, queued writes = RDS Proxy + Aurora with Aurora Replicas. Caches do not queue writes.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
RDS for MySQL Multi-AZ ── failover test ──► outage ~40 giây
Mục tiêu: < 20 giây
  - hầu hết connection còn sống qua failover (trừ transaction/statement đang chạy dở)
  - connection mới vẫn được nhận
  - write request được xếp hàng chờ failover xong
```

Đáp án đúng: **B + C + D** (RDS Proxy + migrate sang Aurora MySQL + Aurora Multi-AZ/replicas). Anh chọn B, E, F: đúng B, sai E và F, thiếu C và D.

⚠️ Lỗi lặp lại: Anh đã học rule "giữ connection sống + queue request khi failover" → **RDS Proxy**, và "failover nhanh" → **Aurora**. Lần này Anh chọn đúng Proxy nhưng thiếu Aurora vì đề thêm các option nhiễu về cache (E, A). Cache **không** thay thế được DB trong failover.

#### Ba đáp án đúng ghép thành một giải pháp

- **B - RDS Proxy**: nằm giữa app và DB, giữ pool connection; khi failover, hầu hết connection còn sống, chỉ các connection đang giữa transaction/statement bị hủy; nhận connection mới ngay và **queue** request khi writer chưa sẵn sàng. TD: bỏ qua DNS cache, giảm thời gian failover tới 66% cho Aurora Multi-AZ.
- **C - Migrate sang Aurora MySQL**: Aurora không cần replay redo log từ checkpoint, buffer cache nằm ngoài DB process nên restart nhanh (theo TD, dưới 60 giây trong đa số trường hợp).
- **D - Aurora Multi-AZ + Aurora Replicas**: có replica sẵn để promote khi lỗi.

Tính theo TD: ~60 giây giảm 66% nhờ Proxy còn khoảng 20 giây, đạt yêu cầu.

#### Vì sao F sai (Anh chọn)

F giữ nguyên RDS for MySQL Multi-AZ và thêm read replica. TD: failover RDS có thể mất đến 60 giây với một standby, và khoảng 35 giây với hai readable standby, nên không đảm bảo dưới 20 giây. Read replica cũng không phải proxy giữ connection hay queue write.

#### Vì sao E sai (Anh chọn)

- **Optimized Reads** chỉ đặt temporary table của MySQL lên NVMe SSD để query nhanh hơn; không giúp connection sống qua failover.
- **ElastiCache for Redis** không thay thế database thật và không queue write request khi DB chết.

#### Đáp án sai còn lại

- **A**: Optimized Writes chỉ tăng throughput ghi (tới 2x theo TD) mà không liên quan failover; **Memcached** chỉ cache đọc, không queue write.

| Đáp án | Giữ connection | Queue write | Giảm thời gian failover |
|---|---|---|---|
| **B. RDS Proxy** | Có | Có | Có (bỏ DNS cache) |
| **C. Aurora** | Không | Không | Có (không replay redo log) |
| **D. Aurora replicas** | Không | Không | Có (promote replica) |
| A, E (cache + Optimized) | Không | Không | Không |
| F (RDS replica) | Không | Không | Không đủ (35 đến 60 giây) |

#### Quy tắc nhớ cho thi

- **Thấy "connection còn sống qua failover + queue request"** → **RDS Proxy**
- **Thấy "failover < 20-30 giây"** → **Aurora (Multi-AZ + replicas) + RDS Proxy** (đủ cả hai)
- **ElastiCache / Optimized Reads / Optimized Writes** → tăng hiệu năng, **không** giải quyết failover
- Mnemonic: **Proxy giữ connection, Aurora làm failover nhanh, cache không phải DB**

### TD explanation

**Amazon RDS Proxy**  is a fully managed, highly available database proxy for Amazon Relational Database Service (RDS) that makes applications more scalable, more resilient to database failures, and more. Amazon RDS Proxy sits between your application and your relational database to efficiently manage connections to the database and improve the scalability of the application. Amazon RDS Proxy can be enabled for most applications with no code changes.

Your Amazon RDS Proxy instance maintains a pool of established connections to your RDS database instances, reducing the stress on database compute and memory resources that typically occurs when new connections are established. RDS Proxy also shares infrequently used database connections so that fewer connections access the RDS database.

![image](https://media.tutorialsdojo.com/sap_rds_proxy_failover.png)

With RDS Proxy, you can build applications that can transparently tolerate database failures without needing to write complex failure-handling code. The proxy automatically routes traffic to a new database instance while preserving application connections. It also bypasses Domain Name System (DNS) caches to reduce failover times by up to 66% for Aurora Multi-AZ databases

Connecting through a proxy makes your application more resilient to database failovers. When the original DB instance becomes unavailable, RDS Proxy connects to the standby database without dropping idle application connections. Doing so helps to speed up and simplify the failover process. The result is faster failover that’s less disruptive to your application than a typical reboot or database problem.

Without RDS Proxy, a failover involves a brief outage. During the outage, you can’t perform write operations on that database. Any existing database connections are disrupted, and your application must reopen them. The database becomes available for new connections and write operations when a read-only DB instance is promoted in place of one that’s unavailable.

![image](https://media.tutorialsdojo.com/amazon-rds-proxy-DBS-C01.jpg)

For applications that maintain their own connection pool, going through RDS Proxy means that most connections stay alive during failovers or other disruptions. Only connections that are in the middle of a transaction or SQL statement are canceled. RDS Proxy immediately accepts new connections. When the database writer is unavailable, RDS Proxy queues up incoming requests.

For applications that don’t maintain their own connection pools, RDS Proxy offers faster connection rates and more open connections. It offloads the expensive overhead of frequent reconnects from the database. It does so by reusing database connections maintained in the RDS Proxy connection pool. This approach is particularly important for TLS connections, where setup costs are significant.

**Amazon Aurora**  is a modern relational database service offering performance and high availability at scale, fully open-source MySQL and PostgreSQL-compatible editions. Unlike other databases, after a database crash, Amazon Aurora does not need to replay the redo log from the last database checkpoint (typically five minutes) and confirm that all changes have been applied before making the database available for operations. Amazon Aurora moves the buffer cache out of the database process and makes it available immediately at restart time. This prevents you from having to throttle access until the cache is repopulated to avoid brownouts. This reduces database restart times to less than 60 seconds in most cases.

With properly configured Multi-AZ and Aurora replicas, Amazon Aurora can quickly recover from failures. Amazon Aurora does not need to replay the redo log from the last database checkpoint (typically five minutes) and confirm that all changes have been applied before making the database available for operations.

Thus, enabling RDS Proxy can further decrease the downtime of a failover to around 20 seconds (66% reduction from 60 seconds).

Therefore, the correct answers are:

**-Set up an Amazon RDS Proxy in front of the database layer to automatically route traffic to healthy RDS instances.**

**-Migrate the Amazon RDS for MySQL cluster to an Amazon Aurora for MySQL cluster.**

**-Ensure that Multi-AZ is enabled on Amazon Aurora and create one or more Aurora Replicas.**

The option that says: **Enable the Amazon RDS Optimized Writes feature and create an Amazon ElastiCache for Memcached cluster in front of the database layer to cache any frequently requested queries** is incorrect. Memcached is used for database caching only and not as a database proxy. Although it can respond to frequently queried data, it can’t queue any write request to the database while the failover process is in place. The Amazon RDS Optimized Writes feature is not useful in this scenario as it only provides you with up to 2x improvement in write transaction throughput on RDS for MySQL by writing only once while protecting you from data loss.

The option that says: **Enable the Amazon RDS Optimized Reads feature and launch an Amazon ElastiCache for Redis cluster in front of the database layer to temporarily serve database queries in case of RDS failure** is incorrect. Although Redis can store data to some extent similar to a database, it is still no substitute for a real database storage system. Moreover, the Amazon RDS Optimized Reads feature is commonly used to achieve faster query processing by placing temporary tables generated by MySQL on NVMe-based SSD block storage that is physically connected to the host server. This feature cannot make most DB connections stay alive during failovers.

The option that says: **Ensure that Multi-AZ is enabled on Amazon RDS for MySQL and create one or more read replicas to ensure quick failover**  is incorrect. This may be possible since the database is currently on RDS with Multi-AZ. However, RDS automatic database failover can take up to 60 seconds for one standby instance and up to [35 seconds](https://aws.amazon.com/rds/features/multi-az) for two readable standby instances. A better option is to use RDS Proxy to fulfill the aforementioned requirements.

**References:**

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html)

[https://aws.amazon.com/rds/aurora/faqs/](https://aws.amazon.com/rds/aurora/faqs/)

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Concepts.AuroraHighAvailability.Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Concepts.AuroraHighAvailability.Proxy)

**Check out these Amazon Aurora and Amazon RDS Cheat Sheets:**

[https://tutorialsdojo.com/amazon-aurora/](https://tutorialsdojo.com/amazon-aurora/)

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

**Check out this Amazon Aurora vs Amazon RDS comparison:**

[https://tutorialsdojo.com/amazon-aurora-vs-amazon-rds/](https://tutorialsdojo.com/amazon-aurora-vs-amazon-rds/)

</details>

<a id="q57"></a>

## Q57

A company launched a high-performance computing (HPC) application inside the VPC of its AWS account. The application is composed of hundreds of private EC2 instances running in a cluster placement group, which allows the instances to communicate with each other at network speeds of up to 10 Gbps. There is also a custom cluster controller EC2 instance that closely controls and monitors the system performance of each instance. The cluster controller has the same instance type and AMI as the other instances. It is configured with a public IP address and runs outside the placement group. The Solutions Architect has been tasked to improve the network performance between the controller instance and the EC2 instances in the placement group.

Which option provides the MOST suitable solution that the Architect must implement to satisfy the requirement while maintaining low-latency network performance?

- **A.** Terminate the custom cluster controller instance and re-launch it to the existing placement group. Attach an Elastic Network Adapter (ENA) to the cluster controller instance to increase its network performance. Change the placement strategy of the placement group to `Spread`.
- **B.** Terminate the custom cluster controller EC2 instance and stop all of the running instances in the existing placement group. Move the cluster controller instance to the existing placement group and restart all of the instances.
- **C.** Stop the custom cluster controller instance and move it to the existing placement group.
- **D.** Attach an Elastic IP address to the custom cluster controller instance to increase its network capability to 10 Gbps.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** cluster controller outside placement group, improve network between it and HPC instances, keep low latency

🪤 **Your trap:** Picked terminating and stopping everything; you only stop the controller, move it into the existing placement group, and restart it. No need to touch others.

🧠 **Rule:** Move an existing instance into a placement group: stop it, modify placement group, start. No terminate, no ENA/EIP effect on bandwidth.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
┌─────── Cluster Placement Group (10 Gbps giữa các node) ───────┐
│  EC2 EC2 EC2 EC2 ... (hàng trăm instance, private)            │
└───────────────────────────────────────────────────────────────┘
                 ▲
                 │ mạng chậm hơn (ngoài group)
        ┌────────┴───────┐
        │ Cluster        │  cùng instance type + AMI,
        │ controller     │  public IP, NẰM NGOÀI placement group
        └────────────────┘
Yêu cầu: tăng network performance controller <-> các node, vẫn LOW LATENCY
```

Đáp án đúng: **C**. Anh chọn **B** (đúng hướng "đưa vào group" nhưng làm thừa).

#### Vì sao C đúng

Muốn controller có băng thông/latency như các node thì phải **đưa nó vào cùng cluster placement group**. TD nêu: instance muốn move vào placement group (hoặc chuyển/gỡ) thì phải ở trạng thái **stopped**, dùng AWS CLI hoặc SDK. Quy trình:

```
Stop controller -> modify placement group = group hiện có -> Start lại
```

Không cần terminate, không cần đụng tới các instance khác.

#### Vì sao B (Anh chọn) sai

B đúng ý "đưa controller vào group" nhưng thêm hai bước thừa và phá hoại:
- **Terminate** controller: không cần, chỉ cần stop.
- **Stop và restart toàn bộ instance trong group**: hàng trăm node bị gián đoạn vô ích. TD: không cần restart hay terminate gì để thêm instance mới vào placement group có sẵn.

Đề hỏi "MOST suitable" nên phương án ít tác động nhất (C) thắng.

#### Các option còn lại

- **A** - Đổi strategy sang **Spread**: spread đặt instance lên các rack riêng để giảm lỗi đồng thời, làm **giảm** hiệu năng mạng so với cluster. ENA có tăng network performance nhưng terminate là thừa.
- **D** - **Elastic IP** chỉ là địa chỉ IPv4 tĩnh, không tăng băng thông lên 10 Gbps.

| Option | Thay đổi | Vấn đề |
|---|---|---|
| **C** | Stop -> move -> start controller | Tối thiểu, đúng |
| B | Terminate controller + restart cả group | Gián đoạn không cần thiết |
| A | Relaunch + đổi sang Spread | Phá low latency |
| D | Gắn Elastic IP | Không liên quan băng thông |

#### Lưu ý thực tế

- Cluster placement group nên dùng instance type hỗ trợ **enhanced networking** để có latency thấp và packet-per-second cao nhất (theo TD).

#### Quy tắc nhớ cho thi

- **Thấy "instance nằm ngoài placement group, cần network tốt hơn"** -> **Stop -> move vào group -> start**
- **Thấy "low latency, high throughput giữa các node"** -> **Cluster** placement group; **Spread** là để tách rack/chịu lỗi
- **Thấy "Elastic IP tăng bandwidth"** -> sai, EIP chỉ là địa chỉ tĩnh

### TD explanation

Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput, or both. They are also recommended when the majority of the network traffic is between the instances in the group. To provide the lowest latency and the highest packet-per-second network performance for your placement group, choose an instance type that supports enhanced networking.

![image](https://media.tutorialsdojo.com/sap_az1_placement_group.png)

A spread placement group is a group of instances that are each placed on distinct racks, with each rack having its own network and power source. Spread placement groups are recommended for applications that have a small number of critical instances that should be kept separate from each other. Launching instances in a spread placement group reduces the risk of simultaneous failures that might occur when instances share the same racks. Spread placement groups provide access to distinct racks, and are therefore suitable for mixing instance types or launching instances over time.

![image](https://media.tutorialsdojo.com/sap_az1_placement_group_instances.png)

You can change the placement group for an instance in any of the following ways:

- Move an existing instance to a placement group

- Move an instance from one placement group to another

- Remove an instance from a placement group

Before you move or remove the instance, the instance must be in the stopped state. You can move or remove an instance using the AWS CLI or an AWS SDK.

Hence, the correct answer is: **Stop the custom cluster controller instance and move it to the existing placement group.**

The option that says: **Terminate the custom cluster controller EC2 instance and stop all of the running instances in the existing placement group. Move the cluster controller instance to the existing placement group and restart all of the instances**  is incorrect because you don’t need to restart or terminate any instance to move a new EC2 instance to an existing placement group. You just have to stop the cluster controller instance, move it to the placement group, and restart it.

The option that says:**Attach an Elastic IP address to the custom cluster controller instance to increase its network capability to 10 Gbps**  is incorrect because an Elastic IP is simply a static IPv4 address designed for dynamic cloud computing. It doesn’t increase the network bandwidth of the instance to 10 Gbps either.

The option that says: **Terminate the custom cluster controller instance and re-launch it to the existing placement group. Attach an Elastic Network Adapter (ENA) to the cluster controller instance to increase its network performance. Change the placement strategy of the placement group to `Spread`**  is incorrect because using a Spread placement group will degrade the existing network performance of the architecture. The use of a Cluster placement group must be maintained. And while it is true that the Elastic Network Adapter (ENA) can increase the instance network performance, the described process of moving the custom cluster controller instance to the placement group is still incorrect. You can just stop the instance and directly include it to the placement group. There is no need to terminate the EC2 instance.

**References:**

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)

**Check out this Amazon EC2 Cheat Sheet:**

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

</details>

<a id="q58"></a>

## Q58

A multinational investment bank has multiple cloud architectures across the globe. The company has a VPC in the US East region for their East Coast office and another VPC in the US West for their West Coast office. There is a requirement to establish a low latency, high-bandwidth connection between their on-premises data center in Texas and both of their VPCs in AWS.

Which of the following options should the solutions architect implement to achieve the requirement in a cost-effective manner?

- **A.** Establish a Direct Connect connection between the VPC in US East region to the on-premise data center in Texas and then establish another Direct Connect connection between the VPC in US West region to the on-premises data center.
- **B.** Set up two separate VPC peering connections for the two VPCs and for the on-premises data center.
- **C.** Set up an AWS VPN managed connection between the VPC in US East region and the on-premises data center in Texas.
- **D.** Set up an AWS Direct Connect Gateway with two virtual private gateways.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** low latency high bandwidth link from Texas data center to VPCs in US East and US West

🪤 **Your trap:** 🔁 Picked two separate Direct Connect connections (one per VPC), costly; one Direct Connect connection plus a Direct Connect gateway with two VGWs reaches both Regions.

🧠 **Rule:** One DX connection to multiple VPCs/Regions = Direct Connect gateway with a VGW per VPC and private virtual interfaces.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                       ┌─ VGW ── VPC US East
On-prem (Texas) ══ 1 DX ══ Private VIF ══ Direct Connect Gateway ─┤
                                                               └─ VGW ── VPC US West
Yêu cầu: low latency + high bandwidth tới CẢ HAI VPC, COST-EFFECTIVE
```

Đáp án đúng: **D (Direct Connect Gateway + 2 VGW)**. Anh chọn **A** (hai kết nối Direct Connect riêng).

⚠️ **Lỗi lặp lại:** Anh đã học quy tắc "nhiều VPC / nhiều Region + một Direct Connect -> Direct Connect Gateway" nhưng lần này đề đổi cách diễn đạt nên chọn lại cách "mỗi VPC một kết nối". Gặp "cost-effective" + nhiều VPC khác Region + DX thì nghĩ ngay tới **DX Gateway**.

#### Vì sao D đúng

Theo TD: **Direct Connect gateway** cho phép dùng **một** kết nối Direct Connect (qua private virtual interface) để tới nhiều VPC trong cùng hoặc khác Region. Cách làm:

1. Tạo Direct Connect gateway (resource toàn cầu, tạo ở bất kỳ public Region nào, truy cập từ mọi Region).
2. Associate gateway với **virtual private gateway** của từng VPC.
3. Tạo **private VIF** từ kết nối DX tới DX gateway.

Một đường DX, hai VPC, một data center: băng thông cao, latency thấp, chi phí thấp.

#### Vì sao A (Anh chọn) sai

A cũng đạt low latency và high bandwidth, nhưng dùng **hai kết nối Direct Connect riêng** -> đắt. Đề có từ khóa "cost-effective" nên A bị loại. Một kết nối + DX gateway đạt cùng kết quả với chi phí thấp hơn.

#### Các option còn lại

- **B** - VPC peering chỉ nối **VPC với VPC**, không nối được data center on-premises.
- **C** - AWS VPN chỉ nối US East, bỏ sót US West; ngoài ra VPN hợp với nhu cầu băng thông thấp-vừa, chấp nhận được độ biến động của Internet, không đạt "low latency, high-bandwidth".

| Option | Nối đủ 2 VPC? | Low latency/high BW | Chi phí |
|---|---|---|---|
| **D. DX Gateway** | Có | Có | 1 kết nối |
| A. 2 DX riêng | Có | Có | 2 kết nối (đắt) |
| C. VPN 1 VPC | Không | Không | - |
| B. VPC peering | Không (không nối on-prem) | - | - |

#### Quy tắc nhớ cho thi

- **Thấy "on-premises + nhiều VPC / nhiều Region + Direct Connect"** -> **Direct Connect Gateway + private VIF + VGW mỗi VPC**
- **Thấy "cost-effective" cạnh "2 Direct Connect"** -> hầu như luôn sai
- **Thấy "VPC peering" để nối on-premises** -> sai, peering chỉ VPC-VPC
- **Thấy "VPN" + "low latency, high bandwidth"** -> VPN không đáp ứng, cần DX

### TD explanation

You can use an **AWS Direct Connect gateway**  to connect your AWS Direct Connect connection over a private virtual interface to one or more VPCs in your account that are located in the same or different regions. You associate a Direct Connect gateway with the virtual private gateway for the VPC, and then create a private virtual interface for your AWS Direct Connect connection to the Direct Connect gateway. You can attach multiple private virtual interfaces to your Direct Connect gateway. A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any public region and access it from all other public regions.

![image](https://media.tutorialsdojo.com/sap_directconnect_gateway.png)

Hence, the correct answer is:**Set up an AWS Direct Connect Gateway with two virtual private gateways. Create the required Private Virtual Interfaces to the Direct Connect Gateway.**

The option that says: **Establish a Direct Connect connection between the VPC in US East region and the on-premises data center in Texas, and then establish another Direct Connect connection between the VPC in US West region and the on-premises data center**  is incorrect because establishing two separate Direct Connect connections is expensive and hence, not a cost-effective option. It is better to establish a Direct Connect gateway instead which uses one Direct Connect connection to integrate the 2 VPCs and the on-premises data center.

**Setting up an AWS VPN managed connection between the VPC in US East region and the on-premises data center in Texas**  is incorrect because a VPN Connection is a more suitable solution for low to modest bandwidth requirements which can tolerate the inherent variability in Internet-based connectivity.

**Setting up two separate VPC peering connections for the two VPCs and for the on-premises data center**  is incorrect because VPC Peering is used to connect 2 VPC’s together and not to connect your on-premises data center.

**References:**

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html)

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html)

**Check out this AWS Direct Connect Cheat Sheet:**

[https://tutorialsdojo.com/aws-direct-connect/](https://tutorialsdojo.com/aws-direct-connect/)

</details>

<a id="q62"></a>

## Q62

A privately funded aerospace and sub-orbital spaceflight services company hosts its rapidly evolving applications in AWS. For its deployment process, the company is using CloudFormation templates which are regularly updated to map the latest AMI IDs for its Amazon EC2 instances clusters. It takes a lot of time to execute this on a regular basis which is why the solutions architect has been instructed to automate this process.

Which of the following options is the most suitable solution that can satisfy the above requirements?

- **A.** Use CloudFormation with AWS Service Catalog to fetch the latest AMI IDs and automatically use them for succeeding deployments.
- **B.** Use a combination of AWS Service Catalog with AWS Config to automatically fetch the latest AMI and use it for succeeding deployments.
- **C.** Use CloudFormation with Systems Manager Parameter Store to retrieve the latest AMI IDs for your template. Whenever you decide to update the EC2 instances, call the update-stack API in CloudFormation in your CloudFormation template.
- **D.** Configure your Systems Manager State Manager to store the latest AMI IDs and integrate them with your CloudFormation template. Call the update-stack API in CloudFormation whenever you decide to update the EC2 instances in your CloudFormation template.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** automate mapping latest AMI IDs in CloudFormation templates

🪤 **Your trap:** Picked CloudFormation with Service Catalog; Service Catalog only manages approved product catalogs and doesn't fetch the latest AMI. Parameter Store parameters resolve AMI IDs.

🧠 **Rule:** Latest AMI in CloudFormation = SSM Parameter Store parameter type, then update-stack. Not Service Catalog, Config, or State Manager.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:  người sửa tay AMI ID trong template -> update stack  (tốn thời gian)

Cần:       template tự lấy AMI ID mới nhất
           ┌─────────────────────┐   tham chiếu key   ┌────────────────┐
           │ SSM Parameter Store │ ◄───────────────── │ CloudFormation │
           │ (lưu AMI ID)        │ ──── ResolvedValue ►│ template       │
           └─────────────────────┘                     └────────────────┘
```

Đáp án đúng: **C**. Anh chọn **A** (Service Catalog).

#### Vì sao C đúng

Section **Parameters** của template có kiểu parameter đặc biệt cho **Systems Manager Parameter Store**. Giá trị truyền vào là **SSM parameter key**, CloudFormation sẽ lấy giá trị thật lưu dưới key đó ở thời điểm tạo/cập nhật stack. Hệ quả:

- Parameter trong SSM là mutable: khi AMI ID mới được ghi vào key, chỉ cần chạy **update-stack** là template dùng giá trị mới, không phải sửa template.
- Nếu key không tồn tại thì có lỗi validation đồng bộ.
- `Describe` API trả thêm field **ResolvedValue** cho biết giá trị đã resolve.

#### Vì sao A (Anh chọn) sai

**AWS Service Catalog** cho tổ chức tạo và quản lý catalog các sản phẩm IT đã được duyệt. Nó là công cụ quản trị/provisioning, **không phải nơi lưu và tra cứu AMI ID mới nhất** cho template. Kết hợp CloudFormation + Service Catalog không tự fetch AMI.

#### Các option còn lại

- **B** - Service Catalog + AWS Config: cùng lỗi Service Catalog; AWS Config theo dõi cấu hình, không cấp AMI ID cho deployment.
- **D** - **SSM State Manager** chỉ duy trì trạng thái cấu hình của EC2/hybrid theo định nghĩa; không phải parameter store lưu AMI mới nhất. Chữ "SSM" gây nhầm: đúng service là **Parameter Store**, không phải State Manager.

| Option | Service chính | Có làm được "lấy AMI ID mới"? |
|---|---|---|
| **C** | SSM Parameter Store | Có |
| D | SSM State Manager | Không (giữ trạng thái instance) |
| A, B | Service Catalog | Không (catalog sản phẩm) |

#### Lưu ý thực tế

- Validation như `AllowedValues`/`AllowedPattern` trên parameter kiểu SSM được áp dụng lên **SSM key** nhập vào, không phải giá trị thật lưu trong Parameter Store.

#### Quy tắc nhớ cho thi

- **Thấy "CloudFormation tự lấy AMI ID mới nhất"** -> **SSM Parameter Store parameter type** + update-stack
- **Thấy "Service Catalog"** -> catalog/governance sản phẩm, không phải nguồn giá trị động
- **Thấy "State Manager"** -> duy trì trạng thái cấu hình, không phải kho giá trị

### TD explanation

You can use the existing **Parameters**  section of your **CloudFormation template**  to define Systems Manager parameters, along with other parameters. Systems Manager parameters are a unique type that is different from existing parameters because they refer to actual values in the Parameter Store. The value for this type of parameter would be the Systems Manager (SSM) parameter key instead of a string or other value. CloudFormation will fetch values stored against these keys in Systems Manager in your account and use them for the current stack operation.

If the parameter being referenced in the template does not exist in Systems Manager, a synchronous validation error is thrown. Also, if you have defined any parameter value validations (AllowedValues, AllowedPattern, etc.) for Systems Manager parameters, they will be performed against SSM keys which are given as input values for template parameters, not actual values stored in Systems Manager.

![image](https://media.tutorialsdojo.com/sap_cloudformation_parameter_store.png)

Parameters stored in Systems Manager are mutable. Any time you use a template containing Systems Manager parameters to create/update your stacks, CloudFormation uses the values for these Systems Manager parameters at the time of the create/update operation. So, as parameters are updated in Systems Manager, you can have the new value of the parameter take effect by just executing a stack update operation. The [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html) section in the output for Describe API will show an additional ‘ResolvedValue’ field that contains the resolved value of the Systems Manager parameter that was used for the last stack operation.

Hence, the correct answer is the option that says: **Use CloudFormation with Systems Manager Parameter Store to retrieve the latest AMI IDs for your template. Whenever you decide to update the EC2 instances, call the update-stack API in CloudFormation in your CloudFormation template.**

The option that says: **Configure your Systems Manager State Manager to store the latest AMI IDs and integrate them with your CloudFormation template. Call the update-stack API in CloudFormation whenever you decide to update the EC2 instances in your CloudFormation template**  is incorrect because the Systems Manager State Manager service simply automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define. This can’t be used as a parameter store that refers to the latest AMI of your application.

The following options are incorrect because using AWS Service Catalog is not suitable in this scenario. This service just allows organizations to create and manage catalogs of IT services that are approved for use on AWS:

**– Use a combination of AWS Service Catalog with AWS Config to automatically fetch the latest AMI and use it for succeeding deployments.**

**– Use CloudFormation with AWS Service Catalog to fetch the latest AMI IDs and automatically use them for succeeding deployments.**

**References:**

[https://aws.amazon.com/blogs/mt/integrating-aws-cloudformation-with-aws-systems-manager-parameter-store/](https://aws.amazon.com/blogs/mt/integrating-aws-cloudformation-with-aws-systems-manager-parameter-store/)

[https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

**Check out this AWS Systems Manager Cheat Sheet:**

[https://tutorialsdojo.com/aws-systems-manager/](https://tutorialsdojo.com/aws-systems-manager/)

</details>

<a id="q64"></a>

## Q64

A data analytics company is running a Redshift data warehouse for one of its major clients. In compliance with the Business Continuity Program of the client, they need to provide a Recovery Point Objective of 24 hours and a Recovery Time Objective of 1 hour. The data warehouse should be available even in the event that the entire AWS Region is down.

Which of the following is the most suitable configuration for this scenario?

- **A.** Configure Redshift to use Cross-Region Replication (CRR) and in case of system failure, failover to the backup region and manually copy the snapshot from the primary region to the secondary region.
- **B.** Configure Redshift to have automatic snapshots and do a cross-region snapshot copy to automatically replicate the current production cluster to the disaster recovery region.
- **C.** Enable Redshift replication from the cluster running in the primary region to the cluster running in the secondary region. Change the DNS endpoint to the secondary cluster's primary node in case of system failures in the primary region.
- **D.** No additional configuration needed. Redshift is configured with automatic snapshot by default.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** Redshift RPO 24 hours, RTO 1 hour, survive a Regional outage

🪤 **Your trap:** 🔁 Picked Redshift replication to a secondary-Region cluster with DNS switch; Redshift has no direct replication, only snapshots. Cross-Region snapshot copy is not enabled by default.

🧠 **Rule:** Redshift DR across Regions = automated snapshots with cross-Region snapshot copy enabled (no cross-Region replication).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Primary Region                         DR Region
┌───────────────┐   cross-Region       ┌──────────────────────┐
│ Redshift      │   snapshot copy      │ Snapshot (bản sao)   │
│ cluster       │ ───────────────────► │ -> restore khi DR    │
└───────────────┘   (tự động)          └──────────────────────┘
Yêu cầu: RPO 24h, RTO 1h, sống sót khi CẢ Region down
```

Đáp án đúng: **B**. Anh chọn **C** (replication cluster-to-cluster).

⚠️ **Lỗi lặp lại:** Anh đã học "Redshift chỉ có cross-Region **snapshot copy**, không có replication" nhưng lần này gặp cách diễn đạt khác (replicate + đổi DNS) nên vẫn chọn replication. Gặp Redshift + DR giữa các Region thì nghĩ **snapshot copy**.

#### Vì sao B đúng

- **Automated snapshots** bật mặc định: Redshift chụp snapshot định kỳ, thường mỗi 8 giờ hoặc sau mỗi 5 GB thay đổi dữ liệu mỗi node, tùy cái nào đến trước. Retention mặc định 1 ngày.
- Bật **cross-Region snapshot copy** để tự động copy snapshot (automated hoặc manual) sang Region đích; có thể đặt retention riêng ở Region đích.
- Khi Region chính hỏng, restore từ snapshot đã copy sang cluster mới ở Region DR.

Cách này khớp RPO 24h (snapshot thường xuyên) và có dữ liệu ở Region khác.

#### Vì sao C (Anh chọn) sai

C giả định có thể "enable Redshift replication" từ cluster sang cluster ở Region khác rồi chỉ đổi DNS. TD: Redshift chỉ có tính năng **cross-Region backup bằng snapshot**, không replicate trực tiếp sang cluster ở Region khác. Cũng không có DNS "primary node" để chuyển như vậy.

#### Các option còn lại

- **A** - "Cross-Region Replication (CRR)" không tồn tại cho Redshift (CRR là khái niệm của S3); lại còn copy snapshot thủ công khi sự cố.
- **D** - Automated snapshot mặc định có bật, nhưng nằm trong cùng Region; **cross-Region copy không bật mặc định**, nên Region down là mất.

| Option | Cơ chế | Sống sót Region down? |
|---|---|---|
| **B** | Automated snapshot + cross-Region snapshot copy | Có |
| C | "Replication" cluster-cluster | Không tồn tại |
| A | "CRR" | Không tồn tại |
| D | Chỉ snapshot mặc định | Không (chưa copy sang Region khác) |

#### Quy tắc nhớ cho thi

- **Thấy "Redshift + DR/Region down"** -> **cross-Region snapshot copy** (bật thủ công)
- **Thấy "Redshift replication / CRR / đổi DNS sang cluster Region khác"** -> sai
- **Thấy "mặc định đã có snapshot"** -> chỉ cùng Region, chưa đủ cho DR
- Mnemonic: **S3 có CRR, Redshift có snapshot copy**

### TD explanation

When automated snapshots are enabled for a cluster, **Amazon Redshift**  periodically takes snapshots of that cluster, usually every eight hours or following every 5 GB per node of data changes, or whichever comes first. Automated snapshots are enabled by default when you create a cluster. These snapshots are deleted at the end of a retention period. The default retention period is one day, but you can modify it by using the Amazon Redshift console or programmatically by using the Amazon Redshift API.

When you enable Amazon Redshift to automatically copy snapshots to another region, you specify the destination region where you want snapshots to be copied. In the case of automated snapshots, you can also specify the retention period that they should be kept in the destination region. After an automated snapshot is copied to the destination region and it reaches the retention time period there, it is deleted from the destination region, keeping your snapshot usage low. You can change this retention period if you need to keep the automated snapshots for a shorter or longer period of time in the destination region.

![image](https://media.tutorialsdojo.com/sap_redshift_snapshot.png)

Therefore the correct answer is: **Configure Redshift to have automatic snapshots and do a cross-region snapshot copy to automatically replicate the current production cluster to the disaster recovery region.**  The automatic snapshots feature is automatically enabled by default. You can then configure Amazon Redshift to automatically copy snapshots (automated or manual) for a cluster to another AWS Region.

The option that says: **Configure Redshift to use Cross-Region Replication (CRR) and in case of system failure, failover to the backup region and manually copy the snapshot from the primary region to the secondary region**  is incorrect. Amazon Redshift only has cross-region backup feature (using snapshots), not Cross-Region Replication.

The option that says: **Enable Redshift replication from the cluster running in the primary region to the cluster running in the secondary region. Change the DNS endpoint to the secondary cluster’s primary node in case of system failures in the primary region**  is incorrect. Amazon Redshift only has cross-region backup feature (using snapshots); it can’t replicate directly to another cluster in another region.

The option that says: **No additional configuration needed. Redshift is configured with automatic snapshot by default**  is incorrect. Even though the automatic snapshots feature is enabled by default, cross-region snapshot copy is not.

**References:**

[https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html)

**Check out this Amazon Redshift Cheat Sheet:**

[https://tutorialsdojo.com/amazon-redshift/](https://tutorialsdojo.com/amazon-redshift/)

</details>

---

# Group B — Storage & performance fit (DynamoDB key/table design, EFS vs Lambda/OpenSearch, sharding/cache vs IOPS) (4)

<a id="q13"></a>

## Q13

An Internet-of-Things (IoT) company is building a portal that stores data coming from its 20,000 gas sensors. The gas sensors, which have unique IDs, are used to detect a gas leak or other emissions inside the oil facility. Every 15 minutes, the sensors will send a data point throughout the day containing its ID, current gas level data, as well as the timestamp. Each data point contains critical information coming from the gas sensors. The company would like to query the information coming from a particular gas sensor for the past week and would like to delete all data that are older than eight weeks. The application is using a NoSQL database which is why they are using the Amazon DynamoDB service.

How would you implement this in the most cost-effective way?

- **A.** Use one table every week, with a composite primary key which is the sensor ID as the partition key and the timestamp as the sort key.
- **B.** Use one table with a primary key which is the concatenated value of the sensor ID and the timestamp.
- **C.** Use one table with a primary key which is the sensor ID. Use the timestamp as the hash key.
- **D.** Use one table every week, with a primary key which is the concatenated value of the sensor ID and the timestamp.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** 20,000 sensors every 15 min, query one sensor past week, delete older than 8 weeks, cost-effective DynamoDB

🪤 **Your trap:** One table forever grows enormous and slows search; deleting old data needs table-per-period. Option C lacks the week split.

🧠 **Rule:** Time-series DynamoDB: one table per period (drop old whole) with sensor ID partition key + timestamp sort key; never concatenate timestamp into key.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
20.000 sensor ──(mỗi 15 phút: ID + gas level + timestamp)──► DynamoDB
Truy vấn: 1 sensor cụ thể, 1 tuần gần nhất
Xóa: dữ liệu cũ hơn 8 tuần       Tiêu chí: tiết kiệm chi phí nhất
```

Đáp án đúng: **A** (một table mỗi tuần, partition key = sensor ID, sort key = timestamp). Anh chọn C.

#### Vì sao A đúng

```
Table tuần 1: PK = sensorId, SK = timestamp
Table tuần 2: PK = sensorId, SK = timestamp
...
Query tuần này: Query(PK = sensor-123, SK between ...)  ──► chỉ 1 table nhỏ
Xóa dữ liệu > 8 tuần: DROP cả table tuần cũ
```

- **Composite key (PK + SK)**: mọi data point của một sensor nằm chung partition key, sắp xếp theo timestamp, nên truy vấn "sensor X trong khoảng thời gian" là một `Query` hiệu quả.
- **Mỗi tuần một table**: dữ liệu mỗi table nhỏ (theo TD, 20.000 sensor x 4 lần/giờ = 1.920.000 record/ngày), query chỉ đụng table của tuần cần xem, xóa dữ liệu cũ bằng cách bỏ cả table thay vì xóa từng item.

#### Vì sao C sai (Anh chọn)

C có hai lỗi:

1. **Khóa không hợp lệ về logic**: "primary key là sensor ID, timestamp là hash key" tự mâu thuẫn. Nếu khóa chỉ là sensor ID thì mỗi sensor chỉ có đúng 1 item, các data point sau sẽ ghi đè data point trước. Phải có **sort key = timestamp** để lưu nhiều bản ghi cho mỗi sensor.
2. **Một table duy nhất**: theo TD, table sẽ rất lớn và tìm kiếm chậm; muốn xóa dữ liệu > 8 tuần phải xóa từng item.

#### Các đáp án sai còn lại

- **B** (một table, key = ID + timestamp nối chuỗi): vẫn một table khổng lồ; nối timestamp vào key khiến không còn "một key cố định cho mỗi sensor" để query theo range.
- **D** (table mỗi tuần nhưng key nối chuỗi): TD: "cần một giá trị cố định cho primary key, không nối timestamp vào sensor ID". Không query được range theo sensor.

| Đáp án | Số table | Dạng key | Query theo sensor + range | Xóa dữ liệu cũ |
|---|---|---|---|---|
| **A** | Mỗi tuần 1 table | PK sensorId + SK timestamp | Có | Drop table |
| B | 1 table | Key nối chuỗi | Không | Xóa từng item |
| C | 1 table | Chỉ sensorId (ghi đè) | Không | Xóa từng item |
| D | Mỗi tuần 1 table | Key nối chuỗi | Không | Drop table |

#### Lưu ý thực tế (đề không hỏi nhưng dễ vấp)

📝 Ghi chú kỹ thuật: DynamoDB còn có **TTL** để tự xóa item hết hạn, thực tế cũng là cách hợp lý để xóa dữ liệu cũ. Đề không đưa TTL vào đáp án nên vẫn chọn A theo pattern "table theo chu kỳ thời gian".

#### Quy tắc nhớ cho thi

- **Thấy "query theo ID + khoảng thời gian"** → **partition key = ID, sort key = timestamp**
- **Thấy "xóa dữ liệu cũ rẻ nhất, dữ liệu theo thời gian"** → **table theo chu kỳ (tuần/tháng), drop table cũ**
- **Nối ID + timestamp thành một key** → hầu như luôn sai

### TD explanation

The gas sensors are generating a large amount of data every week. As mentioned in the question, there are 20,000 gas sensors that send data every 15 minutes. That translates to 1,920,000 records in a single day and with that large amount of data, there would be complexities in querying the DynamoDB database. In these scenarios, you can create new DynamoDB every week and then add a partition key and a sort key in the table.

When you create a table, in addition to the table name, you must specify the primary key of the table. The primary key uniquely identifies each item in the table, so that no two items can have the same key.

**Amazon DynamoDB**  supports two different kinds of primary keys:

**Partition key**  – A simple primary key, composed of one attribute known as the partition key. DynamoDB uses the partition key’s value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored.

**Partition key and sort key**  – Referred to as a composite primary key, this type of key is composed of two attributes. The first attribute is the partition key, and the second attribute is the sort key. DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored.

Take note that the partition key of an item is also known as its hash attribute. The term hash attribute derives from the use of an internal hash function in DynamoDB that evenly distributes data items across partitions, based on their partition key values.

Therefore, the correct answer is: **Use one table every week, with a composite primary key which is the sensor ID as the partition key and the timestamp as the sort key.**

The option that says: **Use one table with a primary key which is the sensor ID. Use the timestamp as the hash key**  is incorrect. If you only use one table, the table would be very enormous and the searching will take a very long time.

The option that says: **Use one table every week, with a primary key which is the concatenated value of the sensor ID and the timestamp**  is incorrect. You need a fixed value for the primary key so you shouldn’t concatenate the timestamp to the sensor ID.

The option that says: **Use one table with a primary key which is the concatenated value of the sensor ID and the timestamp is**  incorrect. If you only use one table, the table would be very enormous and the search will take a very long time.

**References:**

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html)

**Check out this Amazon DynamoDB Cheat Sheet:**

[https://tutorialsdojo.com/amazon-dynamodb/](https://tutorialsdojo.com/amazon-dynamodb/)

</details>

<a id="q38"></a>

## Q38

A company wants to release a weather forecasting app for mobile users. The application servers generate a weather forecast every 15 minutes, and each forecast update overwrites the older forecast data. Each weather forecast outputs approximately 1 billion unique data points, where each point is about 20 bytes in size. This results in about 20GB of data for each forecast. Approximately 1,500 global users access the forecast data concurrently every second, and this traffic can spike up to 10 times more during weather events. The company wants users to have a good experience when using the weather forecast application so it requires that each user query must be processed in less than two seconds.

Which of the following solutions will meet the required application request rate and response time?

- **A.** Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Configure a cache-control timeout of 15 minutes in the API caching section of the API Gateway stage.
- **B.** Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Write an Amazon Lambda@Edge function to cache the data points on edge locations for a 15-minute duration.
- **C.** Use an Amazon EFS volume to store the weather forecast data points. Mount this EFS volume on a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution.
- **D.** Create an Amazon S3 bucket to store the weather forecast data points as individual objects. Create a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer to query the objects on the S3 bucket. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** 20GB forecast overwritten every 15 min, 1,500 users/s spiking 10x, under 2 seconds

🪤 **Your trap:** Picked OpenSearch + API Gateway + Lambda; Lambda burst concurrency cannot scale fast enough for peak. EFS on Auto Scaling EC2 behind CloudFront with 15-minute cache fits.

🧠 **Rule:** Spiky high request rate with periodically overwritten data: EFS + Auto Scaling EC2 + ELB + CloudFront cache matching refresh interval; Lambda burst limits.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Forecast mới mỗi 15 phút (ghi đè bản cũ)
  ~1 tỷ data point x ~20 byte = ~20GB / lần
Người dùng: ~1,500 req/giây, spike gấp 10 lần
Yêu cầu: mỗi query < 2 giây
```

Deciding words: **spike x10**, **ghi đè mỗi 15 phút**, **< 2 giây**. Đáp án đúng: **C (EFS + EC2 ASG + ELB + CloudFront cache 15 phút)**. Anh chọn A (OpenSearch + Lambda + API Gateway).

#### Vì sao C đúng

```
User ► CloudFront (cache 15 phút) ► ELB ► EC2 Auto Scaling ► EFS (20GB forecast)
```

- **CloudFront cache 15 phút** khớp chu kỳ cập nhật forecast: phần lớn request được trả từ edge, origin chỉ chịu số cache miss.
- **EC2 Auto Scaling + ELB** scale theo tải, không bị trần burst như Lambda.
- **EFS** là file system dùng chung cho cả fleet, độ trễ thấp và ổn định, throughput lớn. Khi forecast mới được ghi, mọi instance thấy ngay dữ liệu mới.

#### Vì sao A (anh chọn) sai

A có CloudFront và API Gateway cache 15 phút, nên trông đã tối ưu. Điểm yếu theo TD: **Lambda không scale đủ nhanh khi spike**. Burst concurrency mặc định của Lambda chỉ khoảng 500-3000 request/giây tùy Region, trong khi tải có thể lên gấp 10 lần mức 1,500 req/giây. Cache giúp giảm tải nhưng khi cache miss hàng loạt (ví dụ ngay lúc forecast mới), backend vẫn phải chịu được.

#### Các phương án sai khác

- **B:** dùng Lambda@Edge để cache data point. Lambda@Edge dùng để **tùy biến hành vi CloudFront**, không phải cơ chế cache chính cho dataset lớn. Cache là việc của CloudFront cache behavior.
- **D:** S3 chứa hàng tỷ object nhỏ rồi EC2 gọi qua HTTP. Mỗi request thêm một hop tới S3 làm tăng thời gian đáp ứng, và ghi đè hàng tỷ object mỗi 15 phút mất nhiều thời gian hơn ghi vào EFS (theo TD).

| Phương án | Lưu trữ | Compute | Điểm nghẽn |
|---|---|---|---|
| **C** | EFS | EC2 ASG | Không đáng kể |
| A | OpenSearch | Lambda | Lambda burst limit khi spike |
| B | OpenSearch | Lambda | Lambda burst + Lambda@Edge dùng sai mục đích |
| D | S3 (tỷ object) | EC2 ASG | Latency S3 + ghi đè tỷ object |

#### Quy tắc nhớ cho thi

- **Thấy "spike gấp nhiều lần, cần scale nhanh"** → cẩn thận **Lambda burst limit**; EC2 ASG + cache ở CloudFront an toàn hơn
- **Thấy "dữ liệu thay đổi mỗi N phút"** → **CloudFront cache TTL = N phút**
- **Thấy "dataset dùng chung cho nhiều EC2, độ trễ thấp"** → **EFS**
- **Thấy "Lambda@Edge để cache"** → sai mục đích, Lambda@Edge để customize request/response

### TD explanation

**Amazon Elastic File System (Amazon EFS)**  provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is built to scale on-demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth.

Amazon EFS can provide very low and consistent operational latency as well as a throughput scale of 10+GB per second.

Amazon EFS file systems are distributed across an unconstrained number of storage servers. This distributed data storage design enables file systems to grow elastically to petabyte scale and enables massively parallel access from Amazon EC2 instances to your data. The Amazon EFS-distributed design avoids the bottlenecks and constraints inherent to traditional file servers.

This distributed data storage design means that multithreaded applications and applications that concurrently access data from multiple Amazon EC2 instances can drive substantial levels of aggregate throughput and IOPS. Big data and analytics workloads, media processing workflows, content management, and web serving are examples of these applications. In addition, Amazon EFS data is distributed across multiple Availability Zones, providing a high level of durability and availability.

![image](https://media.tutorialsdojo.com/sap_efs_how_it_works.png)

**Amazon CloudFront**  is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. CloudFront can provide a reliable, low latency, and high throughput network connectivity for global users.

To deliver content to end-users with lower latency, Amazon CloudFront peers with thousands of Tier 1/2/3 telecom carriers globally is well connected with all major access networks for optimal performance and has hundreds of terabits of deployed capacity.

Therefore, the correct answer is: **Use an Amazon EFS volume to store the weather forecast data points. Mount this EFS volume on a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution.**

The option that says: **Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Configure a cache-control timeout of 15 minutes in the API caching section of the API Gateway stage**  is incorrect. This is a possible implementation, but the Lambda functions won’t be able to quickly scale and serve requests during peak traffic. By default, the burst concurrency for Lambda functions is between 500-3000 requests per second (depending on region).

The option that says: **Create an Amazon OpenSearch cluster to store the weather forecast data points. Write AWS Lambda functions to query the ES cluster. Create an Amazon CloudFront distribution and point the origin to an Amazon API Gateway endpoint that invokes the Lambda functions. Write an Amazon Lambda[@Edge](https://portal.tutorialsdojo.com/members/edge/) function to cache the data points on edge locations for a 15-minute duration**  is incorrect. While using Amazon OpenSearch and Lambda functions to query the data is a valid approach, the use of Lambda[@Edge](https://portal.tutorialsdojo.com/members/edge/) for caching the data points at the edge locations is not the most appropriate choice. Lambda[@Edge](https://portal.tutorialsdojo.com/members/edge/) is primarily used to customize the behavior of CloudFront distributions, not to serve as the core caching mechanism for large datasets.

The option that says: **Create an Amazon S3 bucket to store the weather forecast data points as individual objects. Create a fleet of Auto Scaling Amazon EC2 instances behind an Elastic Load Balancer to query the objects on the S3 bucket. Create an Amazon CloudFront distribution and point the origin to the ELB. Configure a 15-minute cache-control timeout for the CloudFront distribution**  is incorrect. This solution is not recommended. Access from the EC2 instances to the S3 bucket via HTTP calls will increase the total response time of the application. Access to EFS is faster compared to calling objects on S3 buckets. Although AWS S3 supports strong read-after-write consistency, billions of objects will be overwritten on the S3 bucket every 15 minutes which could take longer to write than using Amazon EFS.

**References:**

[https://aws.amazon.com/efs/](https://aws.amazon.com/efs/)

[https://aws.amazon.com/cloudfront/features/](https://aws.amazon.com/cloudfront/features/)

[https://docs.aws.amazon.com/efs/latest/ug/performance.html](https://docs.aws.amazon.com/efs/latest/ug/performance.html)

**Check out the Amazon EFS and comparison Cheat Sheets:**

[https://tutorialsdojo.com/amazon-efs/](https://tutorialsdojo.com/amazon-efs/)

[https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/](https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/)

</details>

<a id="q51"></a>

## Q51

A company runs a mission-critical application on a fixed set of Amazon EC2 instances behind an Application Load Balancer. The application responds to user requests by querying a 120GB dataset. The application requires high throughput and low latency storage so the dataset is stored on Provisioned IOPS (PIOPS) Amazon EBS volumes with 3000 IOPS provisioned. The EC2 launch template has been configured to allocate and attach this 120GB size PIOPS EBS volume for the fleet of EC2 instances. After a few months of operation, the company noticed the high cost of EBS volumes in the billing section. The Solutions Architect has been tasked to design a solution that will reduce the costs without a negative impact on the application performance and data durability.

Which of the following solutions will meet the company requirements?

- **A.** Remove the PIOPS EBS volume allocation on the EC2 launch template. Attach a 120GB instance store volume on the EC2 instance to ensure that the application will have enough IOPS for its operation.
- **B.** Use the cheaper General Purpose SSD (gp2) EBS volumes instead of PIOPS EBS volumes. Allocating 1TB EBS volumes (gp2) will have a throughput of 3000 IOPS. Update the EC2 launch template to allocate this type of volume.
- **C.** Create an Amazon EFS volume and mount it across all the EC2 instances. Use the Provisioned Throughput mode on the EFS volume to ensure that the application can reach the required IOPS.
- **D.** Create an Amazon EFS volume and mount it across all the EC2 instances. Use Max I/O performance mode on the EFS volume to ensure the application can reach the required IOPS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** 120GB dataset on PIOPS EBS 3000 IOPS per instance, cut cost without hurting performance or durability

🪤 **Your trap:** Picked 1TB gp2 per instance to reach 3000 IOPS; many 1TB volumes cost more. Shared EFS with Provisioned Throughput is cheaper; Max I/O adds latency.

🧠 **Rule:** Same dataset duplicated on per-instance EBS: use one shared EFS with Provisioned Throughput mode, not Max I/O (higher latency).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Fixed fleet EC2 sau ALB ──► mỗi instance có 1 volume PIOPS 120GB, 3000 IOPS
Dataset 120GB, cần throughput cao + latency thấp
Vấn đề: chi phí EBS cao
Yêu cầu: GIẢM CHI PHÍ, không giảm performance và durability
```

Đáp án đúng: **C (EFS dùng chung, Provisioned Throughput)**. Anh chọn B (gp2 1TB).

#### Vì sao C đúng

```
Trước:  N instance  x  N volume PIOPS 120GB (cùng một dataset, lặp N lần)
Sau:    N instance  ──mount──►  1 EFS dùng chung
```

- Dataset giống nhau cho mọi instance, nên chỉ cần **một bản chia sẻ** thay vì N volume.
- EFS có độ bền cao (dữ liệu lưu trên nhiều AZ).
- **Provisioned Throughput mode** cho đặt throughput độc lập với dung lượng lưu trữ, nên 120GB dữ liệu vẫn đạt throughput cần thiết.

#### Vì sao B (anh chọn) sai

B dựa vào quy tắc gp2 ở thời điểm đó: 3 IOPS mỗi GB, nên 1TB cho khoảng 3000 IOPS. Rẻ hơn PIOPS trên từng GB, nhưng:

- Mỗi instance phải có **volume 1TB riêng** để đạt 3000 IOPS, trong khi dữ liệu chỉ 120GB. Nhân lên cho cả fleet thì tổng chi phí vẫn cao hơn một EFS dùng chung (theo TD).
- Vẫn là N bản dữ liệu giống nhau, không giải quyết gốc vấn đề (lặp storage).

📝 Ghi chú kỹ thuật: gp3 hiện nay có baseline 3000 IOPS không phụ thuộc dung lượng, nên 120GB gp3 đã đạt 3000 IOPS mà không cần 1TB. Đề dùng gp2 nên cách lập luận dựa vào "1TB mới đủ IOPS". Với đề này vẫn chọn C theo TD.

#### Các phương án sai khác

- **A:** instance store là **ephemeral**; mất dữ liệu khi stop/start. Không phù hợp ứng dụng mission-critical và vi phạm yêu cầu durability.
- **D:** EFS Max I/O performance mode. Max I/O scale lên aggregate throughput/ops cao hơn nhưng đổi lại **latency metadata hơi cao hơn**; đề cần latency thấp. Hơn nữa bài toán là throughput nhất quán, không phải scale song song cực lớn.

| Phương án | Chi phí | Durability | Latency/Throughput |
|---|---|---|---|
| **C. EFS + Provisioned Throughput** | Một bản chia sẻ | Cao | Đặt throughput độc lập với dung lượng |
| B. gp2 1TB / instance | N volume lớn | Tốt | Đạt 3000 IOPS nhưng tốn |
| D. EFS Max I/O | Một bản chia sẻ | Cao | Latency metadata cao hơn |
| A. Instance store | Rẻ | Mất khi stop | Nhanh nhưng ephemeral |

#### Lưu ý thực tế

- **EBS Multi-Attach** chia sẻ volume cho nhiều instance, nhưng chỉ cho io1/io2 trên Nitro-based instance và trong **cùng một AZ**. Không phải lời giải rẻ ở đây.

#### Quy tắc nhớ cho thi

- **Thấy "cùng một dataset lặp trên mỗi EC2 + giảm chi phí"** → **EFS dùng chung**
- **Thấy "EFS cần throughput độc lập với dung lượng"** → **Provisioned Throughput**
- **Thấy "Max I/O"** → scale lớn, đổi lại latency cao hơn; không hợp bài toán latency thấp
- **Thấy "instance store" cho dữ liệu quan trọng** → loại (ephemeral)

### TD explanation

**Amazon Elastic File System (Amazon EFS)**  provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is built to scale on-demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth. Amazon EFS has a simple web services interface that allows you to create and configure file systems quickly and easily. The service manages all the file storage infrastructure for you, meaning that you can avoid the complexity of deploying, patching, and maintaining complex file system configurations.

![image](https://media.tutorialsdojo.com/sap_efs_how_it_works.png)

Amazon EFS is designed to provide the throughput, IOPS, and low latency needed for a broad range of workloads. With Amazon EFS, you can choose from two performance modes and two throughput modes:

– The default**General Purpose performance mode**  is ideal for latency-sensitive use cases, like web serving environments, content management systems, home directories, and general file serving. File systems in the **Max I/O mode**  can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for file metadata operations.

– Using the default **Bursting Throughput mode** , throughput scales as your file system grows. Using **Provisioned Throughput mode** , you can specify the throughput of your file system independent of the amount of data stored.

With Bursting Throughput mode, throughput on Amazon EFS scales as the size of your file system in the standard storage class grows. With Provisioned Throughput mode, you can instantly provision the throughput of your file system (in MiB/s) independent of the amount of data stored.

If your file system is in the Provisioned Throughput mode, you can increase the Provisioned Throughput of your file system as often as you want. You can decrease your file system throughput in Provisioned Throughput mode as long as it’s been more than 24 hours since the last decrease.

Hence, the correct answer is: **Create an Amazon EFS volume and mount it across all the EC2 instances. Use the Provisioned Throughput mode on the EFS volume to ensure that the application can reach the required IOPS.**

The option that says: **Create an Amazon EFS volume and mount it across all the EC2 instances. Use Max I/O performance mode on the EFS volume to ensure the application can reach the required IOPS**  is incorrect. File systems in the Max I/O mode can scale to higher levels of aggregate throughput and operations per second. However, this scaling is done with a tradeoff of slightly higher latencies for file metadata operations.

The option that says: **Use the cheaper General Purpose SSD (gp2) EBS volumes instead of PIOPS EBS volumes. Allocating 1TB EBS volumes (gp2) will have a throughput of 3000 IOPS. Update the EC2 launch template to allocate this type of volume**  is incorrect. Although this may look cheaper at first, creating several 1TB volumes for each EC2 instance entails higher costs. The Amazon EFS volume solution will be cheaper for sharing storage across all EC2 instances. Although you can use EBS Multi-Attach to attach EBS volumes to multiple EC2 instances, this is limited only to Provisioned IOPS SSD (io1 or io2 Block Express) volumes that are attached to Nitro-based EC2 instances in the same Availability Zone.

The option that says: **Remove the PIOPS EBS volume allocation on the EC2 launch template. Attach a 120GB instance store volume on the EC2 instance to ensure that the application will have enough IOPS for its operation**  is incorrect. Instance store volumes are ephemeral which means that you will typically lose all data in the volume when you stop/start the instance. This is not recommended for this mission-critical application.

**References:**

[https://docs.aws.amazon.com/efs/latest/ug/performance.html](https://docs.aws.amazon.com/efs/latest/ug/performance.html)

[https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)

**Check out these Amazon EFS and Comparison Cheat Sheets:**

[https://tutorialsdojo.com/amazon-efs/](https://tutorialsdojo.com/amazon-efs/)

[https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/](https://tutorialsdojo.com/amazon-s3-vs-ebs-vs-efs/)

</details>

<a id="q66"></a>

## Q66

A legal consulting firm is running a WordPress website on EC2 instances deployed across multiple Availability Zones with a Multi-AZ RDS MySQL database instance. Their website is designed to use an eventual consistency model and performs a high number of read and write operations. There is a growing number of people who are reporting that the website is slow and after checking, the root cause is due to the slow read processing in your database tier. The current DB instances are already optimized for the firm’s operational budget, with considerations for cost-effectiveness and resource utilization.

Which of the following options could solve this issue? (Select THREE.)

- **A.** Add an RDS MySQL Read Replica in each Availability Zone.
- **B.** Deploy an Amazon ElastiCache Cluster with nodes running in each Availability Zone.
- **C.** Integrate Amazon CloudFront to the website to deliver the static media assets to the viewers faster. Consider using AWS Compute Optimizer to rightsize your fleet of Amazon EC2 instances.
- **D.** Implement sharding to distribute the incoming load to multiple RDS MySQL instances.
- **E.** Upgrade the instance type of the RDS MySQL database instance to a larger type.
- **F.** Upgrade the RDS MySQL instance to use provisioned IOPS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B, D · **You picked:** A, B, F

🔑 **Key words:** slow reads on Multi-AZ RDS MySQL, eventual consistency, budget-optimized instances; select three

🪤 **Your trap:** Picked F (provisioned IOPS): increases IOPS but very expensive. Sharding scales horizontally and is cheaper than upsizing or paying for IOPS.

🧠 **Rule:** Read-heavy RDS bottleneck on a budget: read replicas + ElastiCache + sharding; avoid costly vertical or Provisioned IOPS upgrades.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 (nhiều AZ) -> RDS MySQL Multi-AZ  <- nút thắt: ĐỌC chậm
Ràng buộc: eventual consistency OK, nhiều read lẫn write,
           DB đã tối ưu theo NGÂN SÁCH vận hành (cost-effective)
```

Đáp án đúng: **A + B + D**. Anh chọn **A, B, F**: A và B đúng, F sai, thiếu D.

#### Ba đáp án đúng: ba hướng giảm tải đọc

- **A - Read Replica mỗi AZ**: thêm node phục vụ read, tăng aggregate read throughput, không cần phóng to master. Chấp nhận được vì website dùng eventual consistency.
- **B - ElastiCache**: cache query hay dùng trong bộ nhớ, giảm thời gian truy xuất và tải lên DB.
- **D - Sharding**: chia dữ liệu ra nhiều RDS MySQL instance nhỏ hơn -> scale ngang, hiệu quả chi phí lâu dài hơn nâng instance lên to. Vì có cả read lẫn write nhiều nên sharding phân tán được cả hai.

#### Vì sao F (Anh chọn) sai

**Provisioned IOPS** tăng IOPS cho tầng DB nhưng **rất đắt**, đề đã nói DB "optimized for operational budget". Nó cũng không giảm tải đọc bằng cách thêm node hay cache, nên không bằng A/B/D về chi phí-hiệu quả.

#### Các option còn lại

- **C** - CloudFront chỉ cache content ở edge cho media tĩnh, không tác động tầng DB là nơi nghẽn; Compute Optimizer rightsize EC2, không liên quan.
- **E** - Nâng instance type: scale dọc, tốn kém, có thể vượt ngân sách và bị giới hạn.

| Option | Hướng | Đánh giá |
|---|---|---|
| **A. Read Replica** | Scale ngang cho read | Đúng |
| **B. ElastiCache** | Cache | Đúng |
| **D. Sharding** | Scale ngang cho cả read/write | Đúng |
| F. Provisioned IOPS | Tăng IOPS | Đắt |
| E. Instance lớn hơn | Scale dọc | Đắt, có trần |
| C. CloudFront + Compute Optimizer | Ngoài tầng DB | Không đúng chỗ |

#### Quy tắc nhớ cho thi

- **Thấy "slow read, DB đã tối ưu ngân sách"** -> **Read Replica + ElastiCache + sharding** (scale ngang / cache)
- **Thấy "Provisioned IOPS" hoặc "larger instance"** -> đắt, đề có từ "cost" thì loại
- **Thấy "CloudFront" khi nghẽn ở DB** -> sai tầng
- **Thấy "eventual consistency chấp nhận"** -> Read Replica là hợp lệ

### TD explanation

To improve the read performance of the application, you can use RDS Read Replicas and ElastiCache.

**Amazon ElastiCache**  is a web service that makes it easy to deploy, operate, and scale an in-memory data store or cache in the cloud. The service improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory data stores instead of relying entirely on slower disk-based databases.

![image](https://media.tutorialsdojo.com/sap_rds_elasticache.JPG)

**Amazon RDS Read Replicas**  provide enhanced performance and durability for database (DB) instances. This replication feature makes it easy to elastically scale out beyond the capacity constraints of a single DB Instance for read-heavy database workloads. You can create one or more replicas of a given source DB Instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput.

**Database sharding**  is the process of storing a large database across multiple machines. A single machine, or database server, can store and process only a limited amount of data. Database sharding overcomes this limitation by splitting data into smaller chunks, called shards, and storing them across several database servers. All database servers usually have the same underlying technologies, and they work together to store and process large volumes of data.

The option that says: **Add an RDS MySQL Read Replica in each Availability Zone**  is correct. This improves the database retrieval time as there will be more nodes that can serve the database request. You won’t need to increase the master instance size to accommodate all the read loads.

The option that says: **Deploy an Amazon ElastiCache Cluster with nodes running in each Availability Zone**  is correct. Adding a cache will significantly reduce the retrieval time for frequent database queries. This also reduces the load significantly on the database tier.

The option that says: **Implement sharding to distribute the incoming load to multiple RDS MySQL instances**  is correct. You can use Amazon RDS as the building block a sharded architecture. Sharding allows you to split your current instances into smaller ones that could operate more efficiently. It would also provide horizontal scalability, which can be more cost-effective in the long term compared to simply upgrading to a larger DB instance.

The option that says: **Upgrade the RDS MySQL instance to use provisioned IOPS**  is incorrect. This provides an increase in IOPS for the database tier, however, this is also very expensive to implement since provisioned IOPS costs a lot more.

The option that says: **Integrate Amazon CloudFront to the website to deliver the static media assets to the viewers faster. Consider using AWS Compute Optimizer to rightsize your fleet of Amazon EC2 instances**  is incorrect. Amazon CloudFront simply caches content at the edge. It can be a complementary solution for overall performance improvement but would not directly impact the database layer where the bottleneck is occuring.

The option that says: **Upgrade the instance type of the RDS MySQL database instance to a larger type** is incorrect. While this may improve the overall performance of the database, it’s costly and may exceed the operational budget. This approach is an example of vertical scaling, which has limits and may not be as sustainable as horizontal scaling solutions in the long run.

**References:**

[https://aws.amazon.com/elasticache/](https://aws.amazon.com/elasticache/)

[https://aws.amazon.com/rds/details/read-replicas/](https://aws.amazon.com/rds/details/read-replicas/)

[https://aws.amazon.com/what-is/database-sharding/](https://aws.amazon.com/what-is/database-sharding/)

[https://aws.amazon.com/blogs/database/sharding-with-amazon-relational-database-service/](https://aws.amazon.com/blogs/database/sharding-with-amazon-relational-database-service/)

**Check out these Amazon Elasticache and Amazon RDS Cheat Sheet:**

[https://tutorialsdojo.com/amazon-elasticache/](https://tutorialsdojo.com/amazon-elasticache/)

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

</details>

---

# Group C — Cost choice (reserved capacity, Spot Fleet mix, RI sharing by AZ, Fargate+Spot) (4)

<a id="q15"></a>

## Q15

A media company recently launched a web service that allows users to upload and share short videos. Currently, the web servers are hosted on an Auto Scaling group of Amazon EC2 instances in which the videos are processed and stored in the EBS volumes. Each uploaded video sends a message on the Amazon SQS queue, which is also processed by an Auto Scaling group of Amazon EC2 instances. The company relies on third-party software to analyze and categorize the videos. The website also contains static content that has variable user traffic. The company wants to re-architecture the application to reduce costs, reduce dependency on third-party software, and reduce management overhead by leveraging AWS-managed services.

Which of the following solutions will meet the company’s requirements?

- **A.** Create an Amazon ECS Fargate cluster and use containers to host the web application. Create an Auto Scaling group of Amazon EC2 Spot instances to process the SQS queue. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets.
- **B.** Create an Amazon S3 bucket with website hosting enabled to host the web application. Store the videos and static content on a separate S3 bucket. Configure S3 event notification to send messages to an Amazon SQS queue for each video upload event. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos.
- **C.** Reduce operational overhead by using AWS Elastic Beanstalk to provision the Auto Scaling group of EC2 instances for the web servers and the Amazon SQS queue consumers. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets.
- **D.** Create an Amazon EFS volume to store the videos and static content. Mount the volume on all EC2 instances of the web application. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** re-architect: reduce cost, drop third-party analysis, less management, dynamic web app, SQS workers

🪤 **Your trap:** Picked S3 static website hosting for the web app; S3 has no server-side processing, but the app is dynamic. Fargate web + Spot workers + Rekognition fits.

🧠 **Rule:** Dynamic web app cannot run on S3 website hosting. Fargate for web, Spot for queue workers, Rekognition for video analysis, S3 for storage.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại: EC2 ASG (web + xử lý video, lưu EBS) ─► SQS ─► EC2 ASG (consumer + phần mềm 3rd party)
Mục tiêu: giảm CHI PHÍ + bỏ phần mềm bên thứ ba + giảm công quản lý (managed services)
Web có phần dynamic (xử lý video) + static content traffic thay đổi
```

Đáp án đúng: **A** (ECS Fargate cho web + EC2 Spot ASG xử lý SQS + Rekognition + S3). Anh chọn B.

#### Vì sao A đúng

- **Fargate**: chạy container không phải quản lý EC2 (giảm management overhead).
- **Spot instances** cho consumer SQS: xử lý nền, chịu được gián đoạn, nên rẻ hơn (giảm cost).
- **Rekognition** thay phần mềm bên thứ ba phân tích/phân loại video.
- **S3** lưu video và static content: bền, rẻ.

#### Vì sao B sai (Anh chọn)

B trông rất "serverless" và rẻ: S3 + SQS + Lambda + Rekognition. Điểm sai: **host web application trên S3 website hosting**. Đề nói web servers đang xử lý video rồi lưu EBS, nghĩa là ứng dụng **dynamic**; S3 static hosting không có xử lý server-side, nên không thay thế được web tier.

#### Các đáp án sai còn lại

- **C** (Elastic Beanstalk): vẫn dựa trên EC2 ASG, và không dùng Spot cho consumer nên không giảm cost nhiều như A.
- **D** (EFS): EFS đắt hơn S3 và phải cấu hình mount trên mọi EC2, tăng overhead; trái yêu cầu giảm cost và quản lý.

| Đáp án | Web tier | Lưu trữ | Vấn đề |
|---|---|---|---|
| **A** | Fargate | S3 | Phù hợp |
| B | S3 website hosting | S3 | Không chạy được logic dynamic |
| C | Beanstalk (EC2) | S3 | Không tối ưu cost |
| D | EC2 | EFS | Đắt hơn S3, thêm overhead |

#### Quy tắc nhớ cho thi

- **Thấy "web app có xử lý server-side"** → **không** dùng S3 static hosting
- **"Giảm cost + giảm quản lý"** → **Fargate** cho compute, **Spot** cho xử lý nền, **S3** cho lưu trữ
- **"Phân tích video/ảnh, bỏ phần mềm 3rd party"** → **Rekognition**
- **EFS vs S3** để lưu video/file tĩnh → S3 rẻ hơn

### TD explanation

**AWS Fargate**  is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. With AWS Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing. Fargate makes it easy for you to focus on building your applications.

When you run your tasks and services with the Fargate launch type, you package your application in containers, specify the CPU and memory requirements, define networking and IAM policies, and launch the application.

**Amazon Rekognition**  makes it easy to add image and video analysis to your applications. You just provide an image or video to the Amazon Rekognition API, and the service can identify objects, people, text, scenes, and activities. It can detect any inappropriate content as well. Amazon Rekognition also provides highly accurate facial analysis, face comparison, and face search capabilities. You can detect, analyze, and compare faces for a wide variety of use cases, including user verification, cataloging, people counting, and public safety.

Amazon Rekognition is based on the same proven, highly scalable, deep learning technology developed by Amazon’s computer vision scientists to analyze billions of images and videos daily. It requires no machine learning expertise to use. Amazon Rekognition includes a simple, easy-to-use API that can quickly analyze any image or video file that’s stored in Amazon S3.

![image](https://media.tutorialsdojo.com/sap_aws_rekognition_screen.png)

You can use **Amazon S3**  to host a static website. On a static website, individual webpages include static content. They might also contain client-side scripts. By contrast, a dynamic website relies on server-side processing, including server-side scripts such as PHP, JSP, or ASP.NET. Amazon S3 does not support server-side scripting, but AWS has other resources for hosting dynamic websites. This makes Amazon S3 suitable for hosting static website contents.

A **Spot Instance**  is an unused EC2 instance that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts, you can lower your Amazon EC2 costs significantly. The hourly price for a Spot Instance is called a Spot price. The Spot price of each instance type in each Availability Zone is set by Amazon EC2, and is adjusted gradually based on the long-term supply of and demand for Spot Instances. Your Spot Instance runs whenever capacity is available and the maximum price per hour for your request exceeds the Spot price.

Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted. For example, Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks.

Therefore, the correct answer is: **Create an Amazon ECS Fargate cluster and use containers to host the web application. Create an Auto Scaling group of Amazon EC2 Spot instances to process the SQS queue. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets.** Using an ECS Fargate cluster reduces the overhead of managing EC2 instances and using Spot instances to process the SQS queue significantly reduces the operating costs. Amazon Rekognition is designed to analyze videos which you can use to categorize them. Amazon S3 bucket serves as durable and cost-effective storage for the uploaded videos.

The option that says: **Create an Amazon EFS volume to store the videos and static content. Mount the volume on all EC2 instances of the web application. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos**  is incorrect. Amazon S3 is more cost-effective than using EFS. This also increases management overhead as you need to configure the EFS mount point on all your EC2 instances.

The option that says: **Create an Amazon S3 bucket with website hosting enabled to host the web application. Store the videos and static content on a separate S3 bucket. Configure S3 event notification to send messages to an Amazon SQS queue for each video upload event. Have AWS Lambda poll the Amazon SQS queue for messages and invoke a Lambda function that calls the Amazon Rekognition API to analyze and categorize the videos**  is incorrect. The scenario states that the videos are processed and then stored in EBS volumes, suggesting that the service is dynamic in nature. Amazon S3’s static website hosting does not provide server-side processing, which is necessary for dynamic websites. Therefore, hosting a web application on an Amazon S3 bucket with website hosting enabled may not be a suitable option.

The option that says: **Reduce operational overhead by using AWS Elastic Beanstalk to provision the Auto Scaling group of EC2 instances for the web servers and the Amazon SQS queue consumers. Use Amazon Rekognition to analyze and categorize the videos instead of the third-party software. Store the videos and static contents on Amazon S3 buckets**  is incorrect. Although Elastic Beanstalk can manage the EC2 instances for you, there is no mention to use Spot instances for processing the SQS queue which can further reduce the operating costs.

**References:**

[https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

[https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

**Check out these AWS Fargate and Amazon Rekognition Cheat Sheets:**

[https://tutorialsdojo.com/aws-fargate/](https://tutorialsdojo.com/aws-fargate/)

[https://tutorialsdojo.com/amazon-rekognition/](https://tutorialsdojo.com/amazon-rekognition/)

</details>

<a id="q21"></a>

## Q21

A startup is developing a health-related mobile app for iOS and Android. The co-founder developed a sleep-tracking app that collects the user’s biometric data and stores it in an Amazon DynamoDB table configured with on-demand provisioned throughput. Every day at nine in the morning, a scheduled task scans the DynamoDB table to extract and aggregate last night’s data for each user and stores the results in an Amazon S3 bucket. When the new data is available, the users are then notified via Amazon SNS mobile push notifications. Due to budget constraints, management wants to optimize the backend system’s architecture to reduce costs and increase overall revenue.

Which of the following options can the solutions architect implement to further lower the cost in AWS? (Select TWO.)

- **A.** Use Amazon ElastiCache to cache reads and writes from the DynamoDB table.
- **B.** Launch an Amazon Redshift cluster to replace DynamoDB. Switch from a Standard S3 bucket to One Zone-Infrequent Access storage class.
- **C.** Avail a reserved capacity for provisioned throughput for DynamoDB.
- **D.** Use an Amazon RDS instance configured with Multi-AZ deployments and Read Replicas as a replacement to your DynamoDB.
- **E.** Set up a scheduled job to drop the DynamoDB table for the previous day that contains the biometric data after it is successfully stored in the S3 bucket. Create another DynamoDB table for the day and perform the deletion and creation process everyday.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E · **You picked:** A, C

🔑 **Key words:** lower DynamoDB cost, predictable daily batch, select two

🪤 **Your trap:** Picked ElastiCache (A) instead of dropping the daily table after the S3 export; reserved capacity plus dropping the old table cut cost, not caching.

🧠 **Rule:** Predictable DynamoDB throughput: reserved capacity; also drop or expire data already exported to S3 to cut storage cost.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile app ─► DynamoDB (on-demand) ─ mỗi 9h sáng: scan + aggregate ─► S3 ─► SNS push
Mục tiêu: GIẢM CHI PHÍ (chọn 2)
```

Đáp án đúng: **C + E**. Anh chọn A + C: đúng C, sai A.

#### Hai đáp án đúng

- **C - Reserved capacity cho provisioned throughput**: cam kết trả trước mức đọc/ghi tối thiểu trong một khoảng thời gian, rẻ hơn đáng kể so với giá thường/on-demand nếu dự đoán được workload (ở đây tác vụ chạy đều hàng ngày).
- **E - Drop table của ngày trước sau khi đã lưu sang S3, tạo table mới mỗi ngày**: dữ liệu đã nằm ở S3 nên không phải trả tiền lưu trữ DynamoDB cho dữ liệu cũ; scan chỉ trên table nhỏ.

#### Vì sao A sai (Anh chọn)

ElastiCache cache đọc/ghi cho DynamoDB giúp tăng hiệu năng, nhưng ở đây workload chỉ là **một lần scan mỗi ngày**, cache ít tác dụng. TD: nó không giảm chi phí đáng kể mà còn **thêm chi phí** vì phải trả tiền cluster ElastiCache.

#### Các đáp án sai còn lại

- **B** (Redshift thay DynamoDB + S3 One Zone-IA): Redshift là OLAP, không phải NoSQL thay thế; chuyển đổi tốn thời gian và công sức.
- **D** (RDS Multi-AZ + Read Replicas): đắt hơn kiến trúc hiện tại; đề chỉ cần giảm chi phí, không yêu cầu chuyển khỏi NoSQL.

| Đáp án | Tác động chi phí | Lý do |
|---|---|---|
| **C** | Giảm | Reserved capacity rẻ hơn giá thường |
| **E** | Giảm | Không lưu dữ liệu cũ trong DynamoDB |
| A | Tăng | Trả thêm cluster cache, ít lợi ích |
| B | Tăng/rủi ro | Đổi công nghệ, sai loại workload |
| D | Tăng | Multi-AZ + replicas đắt |

#### Quy tắc nhớ cho thi

- **"Giảm cost DynamoDB, workload dự đoán được"** → **Reserved capacity**
- **"Dữ liệu đã export sang S3"** → bỏ dữ liệu cũ khỏi DynamoDB (drop table)
- **Thêm cache/replica/chuyển DB** khi đề chỉ hỏi "lower cost" → thường làm **tăng** chi phí
- **Multi-select** → chọn các cách thật sự giảm tiền, loại các cách "tăng hiệu năng"

### TD explanation

You can purchase reserved capacity in advance to lower the costs of running your DynamoDB instance. With reserved capacity, you pay a one-time upfront fee and commit to a minimum usage level over a period of time. By reserving your read and write capacity units ahead of time, you realize significant cost savings compared to on-demand provisioned throughput settings. In addition, you can also drop the DynamoDB table, which contains the biometric data right after it is successfully stored in S3.

![image](https://media.tutorialsdojo.com/sap_dynamoDB_auto_scaling.png)

Hence, the correct answers are:

**– Avail a reserved capacity for provisioned throughput for DynamoDB** . If you can predict your need for Amazon DynamoDB read-and-write throughput, reserved capacity offers significant savings over the normal price of DynamoDB provisioned throughput capacity.

**– Set up a scheduled job to drop the DynamoDB table for the previous day that contains the biometric data after it is successfully stored in the S3 bucket. Create another DynamoDB table for the day and perform the deletion and creation process everyday** . This saves costs by not storing too much data on DynamoDB tables.

The option that says: **Use an Amazon RDS instance configured with Multi-AZ deployments and Read Replicas as a replacement to your DynamoDB**  is incorrect because using an RDS database with Multi-AZ deployments and Read Replicas will actually cost more than the current architecture. The scenario just wants to lower the cost, and it didn’t specify the need to shift to a NoSQL database.

The option that says: **Launch an Amazon Redshift cluster to replace DynamoDB. Switch from a Standard S3 bucket to One Zone-Infrequent Access storage class**  is incorrect because Redshift is primarily used for online analytical processing (OLAP) applications and not as a NoSQL database. This change also entails a significant amount of time and resources to execute.

The option that says: **Use Amazon ElastiCache to cache reads and writes from the DynamoDB table**  is incorrect. Although an ElastiCache cluster can lower the CPU utilization of your EC2 instances and improve application performance, it doesn’t provide significant cost reduction as compared to Options 3 and 5. Take note that this will also increase the cost since you have to pay for your ElastiCache cluster.

**References:**

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ProvisionedThroughput.html#HowItWorks.ProvisionedThroughput.ReservedCapacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ProvisionedThroughput.html#HowItWorks.ProvisionedThroughput.ReservedCapacity)

[https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/amazon-dynamodb-reservations.html](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/amazon-dynamodb-reservations.html)

[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)

**Check out this Amazon DynamoDB Cheat Sheet:**

[https://tutorialsdojo.com/amazon-dynamodb/](https://tutorialsdojo.com/amazon-dynamodb/)

</details>

<a id="q40"></a>

## Q40

A digital media publishing company hired a solutions architect to manage its online portal, which is deployed on a single Amazon EC2 instance. The architecture uses a combination of Reserved EC2 Instances to handle the steady-state load and On-Demand EC2 Instances to handle the peak load. Currently, the web servers operate at 90% utilization during peak load.

Which of the following is the most cost-effective option to enable the online portal to quickly recover in the event of a zone outage?

- **A.** Launch a Spot Fleet of On-demand and Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet.
- **B.** Create an Auto Scaling group of Spot instances on multiple Availability Zones. Attach an Application Load Balancer to the group.
- **C.** Launch a Spot Fleet of Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet.
- **D.** Create an Auto Scaling group On-Demand instances on multiple Availability Zones. Attach an Application Load Balancer to the group.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** Reserved + On-Demand EC2 on one instance, recover from zone outage, most cost-effective

🪤 **Your trap:** Picked all On-Demand ASG: resilient but costs more. Spot Fleet mixing On-Demand and Spot across AZs is cheaper while staying available; all-Spot risks interruption.

🧠 **Rule:** Cheapest multi-AZ resilience = Spot Fleet mixing On-Demand (baseline) and Spot across AZs behind ALB; all-Spot risks interruption.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại: 1 EC2 instance (Reserved cho steady-state + On-Demand cho peak)
Peak: web server chạy 90% utilization
Mục tiêu: phục hồi NHANH khi một AZ sập  +  RẺ NHẤT
```

Hai ràng buộc cùng lúc: **multi-AZ (zone outage)** và **most cost-effective**. Đáp án đúng: **A (Spot Fleet gồm On-Demand + Spot, multi-AZ, có ALB)**. Anh chọn D (Auto Scaling group On-Demand, multi-AZ, có ALB).

#### Bốn phương án giống nhau, chỉ khác một cụm

| | Cơ chế | Loại instance | Chênh lệch then chốt |
|---|---|---|---|
| **A** | Spot Fleet | **On-Demand + Spot** | Phần nền On-Demand (ổn định) + phần peak Spot (rẻ) |
| B | Auto Scaling group | Chỉ Spot | Toàn Spot, có thể bị thu hồi |
| C | Spot Fleet | Chỉ Spot | Toàn Spot, có thể bị thu hồi |
| D | Auto Scaling group | Chỉ On-Demand | Ổn định nhưng giá cao nhất |

Cả bốn đều multi-AZ + ALB, nên **chống zone outage đều đạt**. Cái phân biệt là **chi phí** và **độ ổn định**.

#### Vì sao A đúng

Theo TD: On-Demand lo tải nền, Spot được thêm vào khi tăng tải lúc peak để giảm chi phí; fleet tự duy trì target capacity, kể cả khi một AZ mất. Vừa rẻ vừa không đặt cược toàn bộ vào Spot.

#### Vì sao D (anh chọn) sai

D đạt yêu cầu về độ sẵn sàng (multi-AZ + ALB), nên nhìn vào là "an toàn". Nhưng câu hỏi hỏi **cost-effective nhất**: D chạy toàn On-Demand, đắt hơn so với việc dùng Spot cho phần peak. Đề đã cho gợi ý: Reserved cho steady-state, On-Demand cho peak, nên bước tối ưu chi phí tiếp theo là thay phần peak bằng Spot.

#### B và C sai vì sao

Toàn Spot rất rẻ nhưng Spot có thể bị AWS thu hồi, dễ gây gián đoạn cho cổng web trực tuyến. TD không chọn vì rủi ro mất dịch vụ.

📝 Ghi chú kỹ thuật: TD nhắc "bid price" là cách nói cũ; hiện nay Spot không còn cơ chế đặt giá bid, instance bị thu hồi khi AWS cần lại capacity. Ngoài ra, thực tế ASG cũng có thể dùng mixed instances policy (On-Demand + Spot); đề chỉ dùng chữ "Spot Fleet" để phân biệt đáp án. Trong bài, hãy bám cụm **"On-demand and Spot"**.

#### Quy tắc nhớ cho thi

- **Thấy "most cost-effective" + "recover from zone outage"** → **multi-AZ + trộn On-Demand và Spot**
- **Thấy "chỉ Spot" cho web/portal quan trọng** → loại (có thể bị thu hồi)
- **Thấy "chỉ On-Demand" khi hỏi cost-effective** → loại
- **Khi 4 đáp án gần giống nhau** → lập bảng, tìm cụm khác nhau (ở đây: loại instance)

### TD explanation

A Spot Fleet is a set of Spot Instances and optionally On-Demand Instances that are launched based on criteria that you specify. The Spot Fleet selects the Spot capacity pools that meet your needs and launches Spot Instances to meet the target capacity for the fleet. By default, Spot Fleets are set to maintain target capacity by launching replacement instances after Spot Instances in the fleet are terminated. You can submit a Spot Fleet as a one-time request, which does not persist after the instances have been terminated. You can include On-Demand Instance requests in a Spot Fleet request.

![image](https://media.tutorialsdojo.com/sap_ec2_type_fleet_request.png)

To avoid interruption to your Spot instances, you can actually set up a diversified spot fleet allocation strategy in which you are using a range of different EC2 instance types such as c3.2xlarge, m3.xlarge, r3.xlarge et cetera instead of just one type. This will effectively increase the chances of providing a more stable compute capacity to your application. Therefore, in the event that there is a Spot interruption due to the high demand for a specific instance type, say c3.2xlarge, your application could still scale using another instance type, such as m3.xlarge or r3.xlarge.

In the scenario, using a mix of On-demand and Spot instances within a Spot Fleet across multiple Availability Zones strikes the right balance. The On-demand instances primarily handle the steady-state load, while additional Spot instances are launched to help with the increased load during peak times, keeping costs down. The fleet setup automatically adjusts to maintain service even if an Availability Zone goes down, ensuring that the system is both cost-effective and resilient.

Hence, the correct answer is: **Launch a Spot Fleet of On-demand and Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet.**

The option that says: **Create an Auto Scaling group of Spot instances on multiple Availability Zones. Attach an Application Load Balancer to the group**  is incorrect. While being highly cost-effective due to the use of Spot instances, it could lead to availability issues since Spot instances can be reclaimed by AWS when spot market prices exceed the bid price.

The option that says: **Create an Auto Scaling group On-Demand instances on multiple Availability Zones. Attach an Application Load Balancer to the group**  is incorrect. This approach ensures that the portal can handle peak loads without the risk of losing instances unexpectedly. However, the cost of On-Demand instances is significantly higher than Spot instances, making this option less cost-effective for managing fluctuating or unpredictable workloads.

The option that says: **Launch a Spot Fleet of Spot instances across multiple Availability Zones. Attach an Application Load Balancer to the fleet**  is incorrect. Like the other incorrect option, this solution fully relies on Spot instances and, while being cheaper, is more susceptible to service disruption due to Spot market fluctuations.

**References:**

[https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf#page=11](https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf#page=11)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html#spot-fleet-allocation-strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html#spot-fleet-allocation-strategy)

[https://aws.amazon.com/about-aws/whats-new/2019/08/new-capacity-optimized-allocation-strategy-for-provisioning-amazon-ec2-spot-instances/](https://aws.amazon.com/about-aws/whats-new/2019/08/new-capacity-optimized-allocation-strategy-for-provisioning-amazon-ec2-spot-instances/)

**Check out this Amazon EC2 Cheat Sheet:**

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

</details>

<a id="q54"></a>

## Q54

A pharmaceutical company has a hybrid cloud architecture in AWS. It has three different accounts for its environments: DEV, UAT, and PROD, which are all part of the consolidated billing account. The PROD account has purchased 10 Amazon EC2 Reserved Instances in the us-west-2a Availability Zone using the `ec2:PurchaseReservedInstancesOffering` and `ec2:ModifyReservedInstances` API actions.

Currently, there are no running EC2 instances in the PROD account because the application is not live yet. However, in the DEV account, there are 5 EC2 instances running in the us-west-2a Availability Zone. In the UAT account, there are also 5 EC2 instances running in the us-west-1a Availability Zone. All the EC2 instances in the DEV and UAT accounts match the reserved instance type in the PROD account.

In this scenario, which account benefits the most from the Reserved Instance pricing?

- **A.** None. Considering that the PROD account is the one that purchased the Reserved Instance and it does not have any running EC2 instance, there is currently no other member account that benefits from the Reserved Instance pricing.
- **B.** Currently, only the DEV account benefits from the Reserved Pricing.
- **C.** Currently, only the UAT account benefits from the Reserved Pricing.
- **D.** Since both DEV and UAT accounts are running an EC2 instance type that exactly matches the Reserved Instance type, then the Reserved instance pricing will be applied to all EC2 instances in those two member accounts.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** consolidated billing, PROD bought 10 RIs in us-west-2a, DEV runs in us-west-2a, UAT in us-west-1a, who benefits

🪤 **Your trap:** Picked none since PROD has no instances. RI discount applies to other member accounts in the same AZ; only DEV runs in us-west-2a.

🧠 **Rule:** In consolidated billing, zonal RIs discount matching instances in any member account only if in the same AZ and type.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Consolidated billing (cùng một Organization)
PROD: mua 10 Reserved Instances ở us-west-2a, đang KHÔNG chạy instance nào
DEV : 5 EC2 (cùng loại) ở us-west-2a   ◄── khớp AZ của RI
UAT : 5 EC2 (cùng loại) ở us-west-1a    ◄── khác AZ (và khác Region)
```

Đáp án đúng: **B (chỉ DEV được hưởng giá Reserved)**. Anh chọn A (không ai được hưởng vì PROD không chạy instance nào).

#### Cách RI chia sẻ dưới consolidated billing

RI mua ở một account **được chia sẻ cho các account khác** trong consolidated bill; không cần chính account mua phải chạy instance.

```
Billing gộp: RI của PROD (us-west-2a) trừ cho instance KHỚP tiêu chí ở bất kỳ account nào
   DEV  us-west-2a  ──► khớp  ──► được giảm giá (5 trong 10 RI)
   UAT  us-west-1a  ──► lệch  ──► KHÔNG được giảm giá
```

Ví dụ TD: Susan mua 5 RI nhưng chỉ dùng 3, Bob dùng 6; hóa đơn gộp tính 5 instance giá Reserved, phần còn lại giá thường. Bob chỉ được lợi nếu chạy ở **cùng AZ** mà Susan đã mua RI.

#### Vì sao A (anh chọn) sai

A nhầm "người mua phải là người dùng". Thực tế RI là lợi ích ở mức **consolidated bill**: PROD không chạy gì thì phần RI chưa dùng được áp cho instance khớp ở account khác. Vì DEV chạy đúng loại và đúng AZ nên **DEV hưởng lợi** (theo TD).

#### Vì sao UAT và D sai

- **C (chỉ UAT):** UAT ở us-west-1a, lệch với us-west-2a của RI. us-west-1 còn là Region khác với us-west-2, nên RI theo AZ (zonal) không áp dụng.
- **D (cả DEV và UAT):** đúng loại instance nhưng thiếu điều kiện **cùng AZ** nên UAT không được. "Match loại instance" chưa đủ.

| Account | Loại instance | AZ | Hưởng RI? |
|---|---|---|---|
| PROD | Không chạy | us-west-2a (nơi mua) | Là chủ RI |
| **DEV** | Khớp | **us-west-2a** | **Có** |
| UAT | Khớp | us-west-1a | Không |

#### Lưu ý thực tế

- Tên AZ (us-west-2a) ở mỗi account có thể ứng với vị trí vật lý khác nhau (TD nêu rõ điều này). Đề thi thường bỏ qua và coi như cùng tên là cùng AZ.
- RI mua theo **Region** (regional) khác zonal: áp dụng linh hoạt giữa các AZ trong Region nhưng không đảm bảo capacity. Đề này mua theo AZ nên đòi hỏi trùng AZ.

#### Quy tắc nhớ cho thi

- **Thấy "consolidated billing + RI"** → RI chia sẻ giữa các account, chủ RI không cần chạy instance
- **Thấy "RI mua theo AZ cụ thể"** → instance của account khác phải **cùng AZ + cùng loại** mới được hưởng
- **Thấy "khác Region"** → chắc chắn không dùng chung RI zonal

### TD explanation

In the question, DEV and UAT are running the same instance type, but the main difference is that the former is using us-west-2a Availability Zone while the latter uses us-west-1a. Remember that the PROD account has bought the Reserved Instance in the us-west-2a Availability Zone, which means that only the DEV account exactly matches the criteria.

As an **Amazon EC2 Reserved Instance** s example, suppose that Bob and Susan each have an account in an organization. Susan has five Reserved Instances of the same type, and Bob has none. During one particular hour, Susan uses three instances, and Bob uses six, for a total of nine instances on the organization’s consolidated bill. AWS bills five instances as Reserved Instances and the remaining four instances as regular instances.

![image](https://media.tutorialsdojo.com/sap_reserved_instances_basic.png)

Bob receives the cost-benefit from Susan’s Reserved Instances only if he launches his instances in the same Availability Zone where Susan purchased her Reserved Instances. For example, if Susan specifies us-west-2a when she purchases her Reserved Instances, Bob must specify us-west-2a when he launches his instances to get the cost-benefit on the organization’s consolidated bill. However, the actual locations of Availability Zones are independent from one account to another. For example, the us-west-2a Availability Zone for Bob’s account might be in a different location than the location for Susan’s account.

Therefore, the correct answer is: **Currently, only the DEV account benefits from the Reserved Pricing.**

The option that says: **Currently, only the UAT account benefits from the Reserved Pricing**  is incorrect. The UAT account can only benefit from the Reserved Instances of the PROD account if they were launched in the same Availability Zone where the PROD account purchased the Reserved Instances.

The option that says: **Since both DEV and UAT accounts are running an EC2 instance type which exactly matches the Reserved Instance type, then the Reserved instance pricing will be applied to all EC2 instances in those two member accounts**  is incorrect. The UAT account can only benefit from the Reserved Instances of the PROD account if they were launched in the same Availability Zone where the PROD account purchased the Reserved Instances.

The option that says: **None. Considering that the PROD account is the one that purchased the Reserved Instance and it does not have any running EC2 instance, there is currently no other member account that benefits from the Reserved Instance pricing**  is incorrect. The DEV account primarily benefits from the Reserved Instances pricing because the instances are launched on the same AZ where the PROD account purchased the Reserved Instances.

**References:**

[https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

[https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidatedbilling-other.html](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidatedbilling-other.html)

**Check out this AWS Billing and Cost Management Cheat Sheet:**

[https://tutorialsdojo.com/aws-billing-and-cost-management/](https://tutorialsdojo.com/aws-billing-and-cost-management/)

</details>

---

# Group D — Near-identical options - one phrase decides (CodeDeploy extra, Lambda/SQS vs Step Functions, behavior vs ALB rule) (3)

<a id="q14"></a>

## Q14

A company has adopted cloud-native computing best practices for its infrastructure. The company started using AWS CloudFormation templates for defining its cloud resources, and the templates are hosted in its private GitHub repository. As the developers continuously update the templates, the company has encountered several downtimes caused by misconfigured templates, wrong executions, or the creation of unnecessary environments. The management wants to streamline the process of testing the CloudFormation templates to prevent these errors. The Solutions Architect has been tasked to create an automated solution.

Which of the following options should be implemented to meet the company’s requirements?

- **A.** Write an AWS Lambda function that syncs the private GitHub repository to another Git provider like GitLab or Bitbucket. Using AWS CodeDeploy, create a change set and execute the AWS CloudFormation template. Add an AWS CodeBuild stage on the deployment to build and run test scripts to verify the new stack.
- **B.** Write an AWS Lambda function that builds any changes committed on the private GitHub repository. Store the generated artifacts on AWS CodeArtifact. Using AWS CodePipeline, create a change set with the new artifact and execute the AWS CloudFormation template. Add a CodeBuild action to run test scripts that verify the new stack.
- **C.** Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set from the CloudFormation template and execute it using AWS CodeDeploy. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack.
- **D.** Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set and execute the CloudFormation template. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** automate testing of CloudFormation templates from private GitHub, prevent bad executions

🪤 **Your trap:** Picked the twin that executes the change set via CodeDeploy, an unneeded service; CodePipeline itself executes the change set and CodeBuild tests.

🧠 **Rule:** CFN CI/CD = CodePipeline (GitHub source) + change set + CodeBuild tests. CodeDeploy is not for CloudFormation deployment.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
GitHub (private repo, template CFN)
        │ commit
        ▼
CodePipeline ──► tạo change set ──► execute CFN ──► CodeBuild chạy test script
Yêu cầu: tự động test template, tránh lỗi misconfig / chạy nhầm
```

Đáp án đúng: **D**. Anh chọn C. Hai đáp án gần như giống hệt nhau, chỉ khác **một cụm từ**.

#### Khác biệt duy nhất giữa C và D

| | C (Anh chọn) | D (đúng) |
|---|---|---|
| Nguồn + trigger | CodePipeline tự trigger khi commit GitHub | Giống |
| Tạo change set | Có | Có |
| Cụm quyết định | "execute it **using AWS CodeDeploy**" | "execute the CloudFormation template" (qua pipeline) |
| Test | Stage CodeBuild | Stage CodeBuild |

Cụm **"using AWS CodeDeploy"** là chỗ sai. CodeDeploy dùng để deploy ứng dụng lên EC2/on-premises/Lambda/ECS, không phải công cụ thực thi CloudFormation change set. Theo TD, CodeDeploy là tài nguyên thừa; CodePipeline có sẵn action của CloudFormation để tạo và execute change set.

#### Vì sao D đúng

CodePipeline hỗ trợ source từ GitHub, action CloudFormation (create/execute change set) và action CodeBuild để chạy test (ví dụ TaskCat theo Quick Start trong TD). Change set cho xem trước thay đổi trước khi áp dụng nên giảm lỗi misconfig.

#### Các đáp án sai còn lại

- **A**: Lambda sync repo sang GitLab/Bitbucket là thừa vì CodePipeline đã hỗ trợ nguồn Git bên thứ ba; lại dùng CodeDeploy để chạy change set (cùng lỗi như C).
- **B**: Lambda build artifact có giới hạn 15 phút, build có thể lâu hơn; CodeArtifact là kho package/dependency, không phải nơi lưu build output của pipeline. Build nên dùng CodeBuild.

#### Quy tắc nhớ cho thi

- **Thấy "test/deploy CloudFormation template tự động"** → **CodePipeline (source Git) + CFN change set action + CodeBuild test**
- **CodeDeploy** → deploy app (EC2/Lambda/ECS), **không** execute CloudFormation
- **Hai option giống nhau** → gạch chân từng cụm khác nhau, một tên service sai là loại
- **Lambda tự build/sync repo** → gần như luôn là bước thừa (nhớ giới hạn 15 phút)

### TD explanation

You can apply continuous delivery practices to your **AWS CloudFormation**  stacks using AWS CodePipeline. **AWS CodePipeline**  is a continuous delivery service for fast and reliable application and infrastructure updates. CodePipeline builds, tests, and deploys your code every time there is a code change based on the release process models you define.

With continuous delivery, you can automatically deploy CloudFormation template updates to your pipeline stages for testing and then promote them to production. For example, you could use CodePipeline to model an automated release process that provisions a test stack whenever an updated template is committed to a source repository (Git repositories managed by GitHub, GitLab, and Atlassian Bitbucket) or uploaded to an Amazon S3 bucket. You can inspect the test stack and then approve it for the production stage, after which CodePipeline can delete the test stack and create a change set for final approval. When the change set is approved, CodePipeline can execute the change set and deploy the change to production.

**AWS CodeBuild**  is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. AWS CodeBuild scales continuously and processes multiple builds concurrently, so your builds are not left waiting in a queue.

Here is an example of a Quick Start from AWS for CI/CD Pipeline for AWS CloudFormation templates:

![image](https://media.tutorialsdojo.com/sap_codebuild_workflow.png)

– A pipeline created by CodePipeline, which is triggered when a commit is made to the referenced branch of the GitHub repository used in the source stage.

– A build project in CodeBuild to run TaskCat and launch AWS CloudFormation templates for testing.

– An AWS Lambda function that merges the source branch of the GitHub repository with the release branch.

– AWS Identity and Access Management (IAM) roles for the Lambda function and the build project.

– An Amazon Simple Storage Service (Amazon S3) bucket to stash the build artifacts temporarily and to store the TaskCat report.

Therefore, the correct answer is: **Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set and execute the CloudFormation template. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack.**  With AWS CodePipeline, you can create change sets and automatically deploy CloudFormation template updates safely. You can have a CodeBuild stage for building artifacts and testing your new infra.

The option that says: **Create a pipeline in AWS CodePipeline that is triggered automatically for commits on the private GitHub repository. Have the pipeline create a change set from the CloudFormation template and execute it using AWS CodeDeploy. Add an AWS CodeBuild stage on the pipeline to build and run test scripts to verify the new stack**  is incorrect. AWS CodeDeploy is only an unnecessary resource as you will not deploy the changes in your production environment. You need a pipeline to execute the CloudFormation change set and CodeBuild project to test your changes.

The option that says: **Write an AWS Lambda function that syncs the private GitHub repository to another Git provider like GitLab or Bitbucket. Using AWS CodeDeploy, create a change set and execute the AWS CloudFormation template. Add an AWS CodeBuild stage on the deployment to build and run test scripts to verify the new stack**  is incorrect. You don’t need a custom Lambda function as AWS CodePipiline supports executions from third-party Git sources.

The option that says: **Write an AWS Lambda function that builds any changes committed on the private GitHub repository. Store the generated artifacts on AWS CodeArtifact. Using AWS CodePipeline, create a change set with the new artifact and execute the AWS CloudFormation template. Add a CodeBuild action to run test scripts that verify the new stack**  is incorrect. Building artifacts may take longer than the 15-minute maximum execution time of Lambda functions. AWS CodeArtifact is primarily used to automatically fetch software packages and dependencies from public artifact repositories. AWS CodeBuild can be used to build and test artifacts before application deployments.

**References:**

[https://aws.amazon.com/about-aws/whats-new/2016/11/continuously-deliver-changes-to-aws-cloudformation-stacks-with-aws-codepipeline/](https://aws.amazon.com/about-aws/whats-new/2016/11/continuously-deliver-changes-to-aws-cloudformation-stacks-with-aws-codepipeline/)

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.html)

[https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-third-party-git-source-repositories-in-aws-codepipeline.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-third-party-git-source-repositories-in-aws-codepipeline.html)

[https://aws.amazon.com/quickstart/architecture/cicd-taskcat/](https://aws.amazon.com/quickstart/architecture/cicd-taskcat/)

**Check out these AWS CodePipeline and AWS CloudFormation Cheat Sheets:**

[https://tutorialsdojo.com/aws-codepipeline/](https://tutorialsdojo.com/aws-codepipeline/)

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

</details>

<a id="q41"></a>

## Q41

A company recently switched to using Amazon CloudFront for its content delivery network. The development team already made the preparations necessary to optimize the application performance for global users. The company’s content management system (CMS) serves both dynamic and static content. The dynamic content is served from a fleet of Amazon EC2 instances behind an application load balancer (ALB) while the static assets are served from an Amazon S3 bucket. The ALB is configured as the default origin of the CloudFront distribution. An Origin Access Control (OAC) was created and applied to the S3 bucket policy to allow access only from the CloudFront distribution. Upon testing the CMS webpage, the static assets return an error 404 message.

Which of the following solutions must be implemented to solve this error? (Select TWO.)

- **A.** Update the application load balancer listener and create a new path-based rule for the static assets so that it will forward requests to the Amazon S3 bucket.
- **B.** Update the CloudFront distribution and create a new behavior that will forward to the origin of the static assets based on path pattern.
- **C.** Edit the CloudFront distribution and create another origin for serving the static assets.
- **D.** Update the application load balancer listener to check for HEADER condition if the request is from CloudFront and forward it to the Amazon S3 bucket.
- **E.** Replace the CloudFront distribution with AWS Global Accelerator. Configure the AWS Global Accelerator with multiple endpoint groups that target endpoints on all AWS Regions. Use the accelerator’s static IP address to create a record in Amazon Route 53 for the apex domain.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C · **You picked:** A, C

🔑 **Key words:** CloudFront with ALB default origin, S3 static assets with OAC return 404, select two

🪤 **Your trap:** Picked A (ALB path rule to S3); OAC only allows CloudFront to read S3, so ALB cannot serve S3. Fix is in CloudFront: add S3 origin and a path-pattern behavior.

🧠 **Rule:** OAC-protected S3 content must be reached from CloudFront: add an S3 origin and a path-pattern behavior. ALB cannot forward to S3.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CloudFront distribution
   Default origin = ALB  ──► EC2 (dynamic content)   OK
   Static assets /... ──► đi vào ALB ──► 404
S3 bucket (static) có OAC: chỉ cho CloudFront truy cập
```

Lỗi 404 vì request của static assets đi vào **default origin là ALB**, mà ALB/EC2 không có các file đó. Đáp án đúng: **B + C**. Anh chọn A + C: C đúng, A sai.

#### Hai lựa chọn đúng ghép thành một giải pháp

Một distribution phục vụ được nhiều origin, tách theo path:

```
CloudFront
  Origin 1: ALB      ◄── Default (*) behavior
  Origin 2: S3 (OAC) ◄── Behavior theo path pattern (vd: /static/*, images/*.jpg)
```

- **C:** tạo **thêm origin** cho S3 bucket (kèm OAC).
- **B:** tạo **behavior** theo path pattern, trỏ tới origin S3; Default (*) giữ nguyên là ALB.

Thiếu một trong hai là không chạy: có origin nhưng không có behavior thì không có request nào tới nó; có behavior mà chưa có origin thì không có đích để trỏ.

#### Vì sao A (anh chọn) sai

A cho ALB listener thêm path-based rule chuyển request tới S3. Sai vì:

- ALB không phải đường chính thức tới S3; target của ALB là instance/IP/Lambda, không phải S3 bucket.
- Bucket đã giới hạn bằng **OAC** chỉ cho CloudFront; request đi qua ALB sẽ bị **access denied** (theo TD).
- Đặt sai chỗ: việc chia traffic theo path phải làm ở CloudFront, không phải ở ALB.

#### Các phương án sai khác

- **D:** ALB kiểm tra HEADER xem request có từ CloudFront rồi chuyển sang S3. Cùng lỗi như A: đi qua ALB thì bị OAC từ chối.
- **E:** thay CloudFront bằng Global Accelerator. Global Accelerator là dịch vụ tầng network cải thiện availability/performance, không thay thế CDN và không giải quyết routing static/dynamic content.

| Phương án | Làm ở đâu | Kết quả |
|---|---|---|
| **B** | CloudFront behavior | Đúng |
| **C** | CloudFront origin | Đúng |
| A | ALB listener | Access denied (OAC) |
| D | ALB header rule | Access denied (OAC) |
| E | Đổi sang Global Accelerator | Không thay thế CDN |

#### Quy tắc nhớ cho thi

- **Thấy "static trên S3 + dynamic trên ALB, cùng một domain"** → **CloudFront: 2 origin + behavior theo path pattern**
- **Thấy "OAC trên S3"** → chỉ CloudFront truy cập được; mọi đường khác (ALB...) là access denied
- **Thấy "Global Accelerator thay CloudFront"** → sai, không phải CDN

### TD explanation

**Amazon CloudFront**  is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay) so that content is delivered with the best possible performance.

You create a CloudFront distribution to tell CloudFront where you want the content to be delivered from and the details about how to track and manage content delivery. Then CloudFront uses computers—edge servers—that are close to your viewers to deliver that content quickly when someone wants to see it or use it.

![image](https://media.tutorialsdojo.com/sap_cloudfront_s3_http_steps.png)

In general, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you can either allow everyone to have access to the files there or you can restrict access. To restrict access to content that you serve from Amazon S3 buckets, follow these steps:

- Create a special CloudFront user called an **origin access control (OAC)**  and associate it with your distribution.

- Configure your S3 bucket permissions so that CloudFront can use the OAC to access the files in your bucket and serve them to your users. Make sure that users can’t use a direct URL to the S3 bucket to access a file there.

After you take these steps, users can only access your files through CloudFront, not directly from the S3 bucket.

You can configure a **single CloudFront web distribution**  to serve different types of requests from multiple origins. For example, if you are building a website that serves static content from an Amazon Simple Storage Service (Amazon S3) bucket and dynamic content from a load balancer, you can serve both types of content from a CloudFront web distribution.

Follow these steps to configure a CloudFront web distribution to serve static content from an S3 bucket and dynamic content from a load balancer:

- Open your web distribution from the CloudFront console.

- Choose the **Origins**  tab.

- Create **one origin**  for your S3 bucket and **another origin**  for your load balancer.  **Note:**  If you’re using a custom origin server or an S3 website endpoint, you must enter the origin’s domain name into the **Origin Domain Name**  field.

- From your distribution, choose the **Behaviors**  tab.

- Create a behavior that specifies a path pattern to route all static content requests to the S3 bucket. For example, you can set the “images/*.jpg” path pattern to route all requests for “.jpg” files in the images directory to the S3 bucket.

- Edit the **Default (*)** path pattern behavior and set its **Origin**  as your load balancer.

Therefore, the correct answers are:

**– Edit the CloudFront distribution and create another origin for serving the static assets.**

**– Update the CloudFront distribution and create a new behavior that will forward to the origin of the static assets based on path pattern.**

The option that says: **Update the application load balancer listener and create a new path-based rule for the static assets so that it will forward requests to the Amazon S3 bucket**  is incorrect. The OAC is used to allow only CloudFront to access the static assets on the S3 bucket. Using the load balancer to forward the requests will result in the access denied error.

The option that says: **Replace the CloudFront distribution with AWS Global Accelerator. Configure the AWS Global Accelerator with multiple endpoint groups that target endpoints on all AWS Regions. Use the accelerator’s static IP address to create a record in Amazon Route 53 for the apex domain** is incorrect. AWS Global Accelerator is a network layer service that improves the availability and performance of your applications used by a wide global audience. This service is not a substitute for a CDN service like Amazon CloudFront.

The option that says: **Update the application load balancer listener to check for HEADER condition if the request is from CloudFront and forward it to the Amazon S3 bucket**  is incorrect. Although an ALB can inspect the HTTP Header requests, using the load balancer to forward the requests will result in the access denied error because of the OAC on the S3 bucket policy.

**References:**

[https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html)

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

[https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/)

**Check out this Amazon CloudFront Cheat Sheet:**

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

</details>

<a id="q63"></a>

## Q63

A company has a large collection of user-submitted stock photos. An AWS Lambda function processes and extracts metadata from these photos to make a searchable catalog. The metadata is extracted depending on several rules and the output is sent to an Amazon ElastiCache for Redis cluster. The metadata extraction is done in several batches and the whole process takes about 45 minutes to complete. Whenever there is a change in the metadata extraction rules, the update process is triggered manually before the extraction process starts. As the stock photo submissions are steadily growing, the company wants to reduce the metadata extraction time for its catalog.

Which of the following options should the Solutions Architect implement to reduce the time for the metadata extraction process?

- **A.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Create another workflow that will retrieve the list of photos for processing and execute the metadata extraction workflow for each photo.
- **B.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Configure all the Lambda extraction functions to subscribe to this SQS queue with higher batch size.
- **C.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Associate the Lambda functions to an AWS Batch compute environment. Write another Lambda function that will retrieve the list of photos for processing and send each item to the job queue in the AWS Batch compute environment.
- **D.** Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Set this SQS queue as the input for the Step Functions workflow.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** Lambda metadata extraction takes 45 min, split by metadata type, reduce extraction time

🪤 **Your trap:** Picked Lambda feeding SQS as Step Functions input; an SQS queue cannot directly invoke a Step Functions workflow. Use a workflow that runs the extraction workflow per photo.

🧠 **Rule:** SQS cannot be a direct Step Functions input. Parallel state for per-type functions, plus an orchestration workflow iterating over photos.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Ảnh -> [1 Lambda làm mọi loại metadata, tuần tự] -> ElastiCache Redis   (45 phút)

Mục tiêu: GIẢM thời gian -> tách theo loại metadata, chạy SONG SONG, dễ đổi rule
```

Đáp án đúng: **A**. Anh chọn **D**. Hai option gần giống nhau: cùng tách Lambda, cùng dùng Step Functions parallel; khác ở **cách ảnh đi vào workflow**.

#### Cụm từ khác biệt A vs D

| | A (đúng) | D (Anh chọn) |
|---|---|---|
| Tách Lambda theo loại metadata | Có | Có |
| Step Functions chạy Lambda song song | Có | Có |
| Cách đưa ảnh vào | **Workflow thứ 2 lấy danh sách ảnh và execute workflow trích xuất cho từng ảnh** | **Lambda gửi từng ảnh vào SQS, đặt SQS làm input của Step Functions** |

#### Vì sao A đúng

Step Functions là serverless orchestrator, phối hợp nhiều Lambda trong workflow dễ debug, dễ đổi; giữ Lambda sạch logic điều phối. Workflow thứ 2 lấy danh sách ảnh rồi khởi chạy workflow trích xuất cho từng ảnh, mỗi ảnh chạy các Lambda loại metadata song song. Tách riêng giúp đổi rule từng loại mà không đụng chỗ khác.

#### Vì sao D (Anh chọn) sai

D nghe hợp lý nhưng "set this SQS queue as the input for the Step Functions workflow" là **không làm được trực tiếp**: theo TD, SQS không thể là input trực tiếp của Step Functions. Chỉ khả thi nếu có thêm một Lambda đọc SQS rồi gọi Step Functions, mà option **không nói tới** Lambda đó. Anh đã đọc lướt đoạn khác biệt này.

#### Các option còn lại

- **B** - Nhiều Lambda cùng subscribe một SQS queue: khi một Lambda xử lý một ảnh thì message bị ẩn (invisible) với Lambda khác, nên các loại metadata **không chạy song song trên cùng ảnh**. Phá mục đích tách function.
- **C** - **AWS Batch** thêm độ phức tạp; Batch chạy batch job quy mô lớn, không dùng với Lambda function.

#### Quy tắc nhớ cho thi

- **Thấy "điều phối nhiều Lambda song song"** -> **Step Functions** (Parallel state)
- **Thấy "SQS làm input trực tiếp của Step Functions"** -> không có; cần Lambda trung gian
- **Thấy "nhiều consumer cùng queue, mỗi consumer cần cùng message"** -> sai (SQS giao mỗi message cho một consumer); cần fan-out kiểu khác
- **Thấy "Batch + Lambda"** -> loại
- Option giống nhau: **so từng cụm khác biệt**, đừng chốt theo phần giống

### TD explanation

**AWS Step Functions**  can be used to run a serverless workflow that coordinates multiple AWS Lambda functions. AWS Step Functions is a serverless function orchestrator that makes it easy to sequence AWS Lambda functions and multiple AWS services into business-critical applications. Through its visual interface, you can create and run a series of checkpointed and event-driven workflows that maintain the application state. The output of one step acts as an input to the next. Each step in your application executes in order, as defined by your business logic.

**AWS Lambda**  is a serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes. With Lambda, you can run code for virtually any type of application or backend service – all with zero administration. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic.

![image](https://media.tutorialsdojo.com/sap_step_function_lambda_function.JPG)

In this scenario, you can quickly make changes to the whole process depending on the extraction rules if you have dedicated Lambda functions for each type of metadata. Technically, you can create one Lambda function to call the other Lambda metadata extraction functions. However, it is quite challenging to orchestrate the data flow of the Lambda functions as the number of functions grow. Plus, any change in the flow of the application will require changes in multiple places, and you could end up writing the same code over and over again.

To solve this challenge, you can use AWS Step Functions. This is a serverless orchestration service that lets you easily coordinate multiple Lambda functions into flexible workflows that are easy to debug and easy to change. Step Functions will keep your Lambda functions free of additional logic by triggering and tracking each step of your application for you.

Therefore, the correct answer is: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Create another workflow that will retrieve the list of photos for processing and execute the metadata extraction workflow for each photo.**

The option that says: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Associate the Lambda functions to an AWS Batch compute environment. Write another Lambda function that will retrieve the list of photos for processing and send each item to the job queue in the AWS Batch compute environment**  is incorrect. AWS Batch only adds complexity to the solution. AWS Batch is designed to easily and efficiently run hundreds of thousands of batch computing jobs on AWS but not with Lambda functions.

The option that says: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Create a workflow on AWS Step Functions that will run multiple Lambda functions in parallel. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Set this SQS queue as the input for the Step Functions workflow**  is incorrect. This might be possible if you have a Lambda Function that consumes the messages on the SQS and feeds them to the Step Function, which is not explicitly stated on this option. An SQS queue cannot be used as a direct input for an AWS Step Function workflow.

The option that says: **Split the single Lambda function that processes the photos into several functions dedicated for each type of metadata. Write another Lambda function that will retrieve the list of photos for processing and send each item to an Amazon SQS queue. Configure all the Lambda extraction functions to subscribe to this SQS queue with higher batch size**  is incorrect. This may be possible but it will not work for this scenario. When a Lambda function processes the photo for a specific type of metadata, it will become invisible on the queue, and other Lambda functions will not be able to process the same photo. This defeats the purpose of multiple Lambda functions that are supposed to process the photo in parallel.

**References:**

[https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/](https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/)

[https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html](https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html)

[https://aws.amazon.com/blogs/aws/new-step-functions-support-for-dynamic-parallelism/](https://aws.amazon.com/blogs/aws/new-step-functions-support-for-dynamic-parallelism/)

[https://aws.amazon.com/step-functions/use-cases/](https://aws.amazon.com/step-functions/use-cases/)

**Check out the AWS Step Functions Cheat Sheet:**

[https://tutorialsdojo.com/aws-step-functions/](https://tutorialsdojo.com/aws-step-functions/)

</details>

---

# Group E — Service fit / app design (AppSync, Client VPN, MGN, ENI licenses, cert at ALB, WorkDocs, NLB+NACL, DB replication) (8)

<a id="q17"></a>

## Q17

A company hosts a serverless application on AWS using Amazon API Gateway and AWS Lambda with Amazon DynamoDB as the backend database. The application has a feature that allows users to create posts and reply to comments based on different topics. The API model currently uses the following methods:

– `GET /posts/[postid]` – used to get details about the post

– `GET /users/[userid]` – used to get details about a user

– `GET /comments/[commentid]` – used to get details of a comment

The application does not use API keys for request authorization. To increase user engagement on the web app, the company wants to reduce comment latency by making the comments appear in real-time.

Which of the following solution should be implemented to meet the requirements and improve user experience?

- **A.** Update the application code to call the `GET /comments/[commentid]` API every 3 seconds to show comments in real-time without sacrificing performance.
- **B.** Lower the API response time of the Lambda functions by increasing the concurrency limit. This allows functions to run in parallel to deliver the comments in real-time.
- **C.** Create a distribution on Amazon CloudFront and use edge-optimized APIs. Cache API responses in CloudFront to improve comment latency.
- **D.** Leverage AWS AppSync by building GraphQL APIs and using Websockets to deliver comments in real-time.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** real-time comments, serverless API Gateway Lambda DynamoDB, reduce comment latency

🪤 **Your trap:** Picked CloudFront caching of API responses; cached comments may not be new, so not real-time. Real-time push needs WebSocket subscriptions.

🧠 **Rule:** Real-time updates pushed to clients = AWS AppSync GraphQL subscriptions over WebSockets, not caching or polling.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──► API Gateway (REST: GET /posts, /users, /comments) ──► Lambda ──► DynamoDB
Mục tiêu: comment xuất hiện REAL-TIME (giảm độ trễ comment)
```

Từ khóa quyết định: **real-time**, tức server phải **đẩy** dữ liệu mới xuống client. Đáp án đúng: **D** (AppSync GraphQL + WebSockets). Anh chọn C.

#### Vì sao D đúng

**AWS AppSync** là dịch vụ managed GraphQL, kết nối DynamoDB/Lambda và có **subscriptions** để push cập nhật realtime qua WebSockets cho số lượng client lớn. Nó cũng tự scale và hỗ trợ ví dụ như chat, collaboration.

```
Client A gửi comment ──► AppSync mutation ──► DynamoDB
                                      └──► subscription push (WebSocket) ──► mọi client đang xem
```

#### Vì sao C sai (Anh chọn)

CloudFront + edge-optimized API + cache giúp **tải nhanh hơn** (giảm latency từng request), nhưng không đẩy dữ liệu mới. Theo TD: cache có thể chưa chứa comment mới nên người dùng không thấy ngay. Cache làm "đọc nhanh", không phải "realtime".

#### Các đáp án sai còn lại

- **A** (poll mỗi 3 giây): gần giống realtime nhưng gọi API liên tục dù không có comment mới, tốn Lambda execution và chi phí.
- **B** (tăng Lambda concurrency): không giúp hiển thị realtime; nếu chưa chạm giới hạn concurrency thì không có lợi ích.

| Cách | Cơ chế | Realtime thật? | Chi phí/Hạn chế |
|---|---|---|---|
| **D. AppSync subscription** | Server push (WebSocket) | Có | Thấp, managed |
| A. Polling 3s | Client kéo | Gần | Gọi thừa, tốn Lambda |
| C. CloudFront cache | Cache phản hồi | Không | Có thể trả dữ liệu cũ |
| B. Concurrency | Chạy song song | Không | Không liên quan |

#### Quy tắc nhớ cho thi

- **Thấy "real-time updates / push tới client / chat / collaboration"** → **AppSync (GraphQL subscriptions, WebSockets)**
- **Cache/CloudFront** → giảm latency đọc, **không** đảm bảo dữ liệu mới nhất
- **Polling** → chạy được nhưng đề thường coi là tốn kém

### TD explanation

**AWS AppSync**  is a fully managed service that makes it easy to develop GraphQL APIs by handling the heavy lifting of securely connecting to data sources like Amazon DynamoDB, Lambda, and more. Adding caches to improve performance, subscriptions to support real-time updates, and client-side data stores that keep offline clients in sync are just as easy. Once deployed, AWS AppSync automatically scales your GraphQL API execution engine up and down to meet API request volumes.

With managed GraphQL subscriptions, AWS AppSync can push real-time data updates over Websockets to millions of clients. For mobile and web applications, AppSync also provides local data access when devices go offline, and data synchronization with customizable conflict resolution, when they are back online.

AppSync supports real-time chat applications. You can build conversational mobile or web applications that support multiple private chat rooms, offer access to conversation history, and queue outbound messages, even when a device is offline.

![image](https://media.tutorialsdojo.com/sap_aws_appsync_overview.png)

AppSync can also be used for real-time collaboration. You can broadcast data from the backend to all connected clients (one-to-many) or between clients (many-to-many), such as in a second screen scenario where you broadcast the same data to all clients, who can then reply.

Therefore, the correct answer is: **Leverage AWS AppSync by building GraphQL APIs and using Websockets to deliver comments in real-time.**  AWS AppSync can push real-time data updates over Websockets. This can automatically scale to millions of client requests.

The option that says: **Create a distribution on Amazon CloudFront and use edge-optimized APIs. Cache API responses in CloudFront to improve comment latency**  is incorrect. Caching API responses can improve the loading of comments, however, this may not show the comments in real-time if the new comments are not yet on the cache.

The option that says: **Update the application code to call the `GET /comments/[commentid]` API every 3 seconds to show comments in real-time without sacrificing performance**  is incorrect. This is possible but will heavily put a burden on your Lambda function executions. Even if there are no new comments, the API will still be called. This will add unnecessary cost to function executions.

The option that says: **Lower the API response time of the Lambda functions by increasing the concurrency limit. This allows functions to run in parallel to deliver the comments in real-time**  is incorrect. Increasing the concurrency limit will not help in showing the comments in real-time. If you don’t reach the Lambda concurrency limit regularly, there is no apparent advantage for this option.

**References:**

[https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html)

[https://docs.aws.amazon.com/appsync/latest/devguide/real-time-websocket-client.html](https://docs.aws.amazon.com/appsync/latest/devguide/real-time-websocket-client.html)

[https://aws.amazon.com/about-aws/whats-new/2020/04/aws-appsync-enables-support-for-generic-websockets-clients-graphql-real-time-subscriptions/](https://aws.amazon.com/about-aws/whats-new/2020/04/aws-appsync-enables-support-for-generic-websockets-clients-graphql-real-time-subscriptions/)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

</details>

<a id="q19"></a>

## Q19

A research company hosts its internal applications inside AWS VPCs in multiple AWS Accounts. The internal applications are accessed securely from inside the company network using an AWS Site-to-Site VPN connection. VPC peering connections has been established from the company’s main AWS account to VPCs in other AWS Accounts. The company has recently announced that employees will be allowed to work remotely if they are connected using a VPN. The solutions architect has been tasked to create a scalable and reliable AWS Client VPN solution that employees can use when working remotely.

Which of the following options is the most cost-effective implementation to meet the company requirements with minimal changes to the current setup?

- **A.** Install the AWS Client VPN on the company data center. Create AWS Transit Gateway to connect the main VPC and other VPCs into a single hub. Update the VPC route configurations to allow communication with the internal applications.
- **B.** Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in each of the AWS accounts. Update each VPC route configuration to allow communication with the internal applications.
- **C.** Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in the same VPC region in the main AWS account. Update the VPC route configurations to allow communication with the internal applications.
- **D.** Install the AWS Client VPN on the company data center. Configure connectivity between the existing AWS Site-to-Site VPN and client VPN endpoint.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** Client VPN for remote employees, existing Site-to-Site VPN and VPC peering, most cost-effective, minimal change

🪤 **Your trap:** Picked installing Client VPN at the data center with Transit Gateway, which reconfigures peering. Client software goes on employee workstations; one endpoint in main account.

🧠 **Rule:** Client VPN: client on workstations, ONE endpoint in the main account reaching peered VPCs; no Transit Gateway rework needed.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhân viên remote ──(AWS Client VPN)──► Client VPN endpoint ──► Main VPC (có Site-to-Site VPN về on-prem)
                                                               ├── peering ──► VPC account B
                                                               └── peering ──► VPC account C
Yêu cầu: scalable + reliable, RẺ NHẤT, THAY ĐỔI TỐI THIỂU
```

Đáp án đúng: **C**. Anh chọn A.

#### Vì sao C đúng

- Cài **VPN client trên máy từng nhân viên** (Client VPN là client-based, dùng OpenVPN client).
- Tạo **một Client VPN endpoint** trong **VPC chính** (cùng Region), đã peering sẵn tới các VPC khác. Cấu hình này đúng với kịch bản AWS khuyến nghị: clients truy cập target VPC và các VPC peered với nó.
- Chỉ cần cập nhật route và authorization rule. Không thay đổi kiến trúc mạng hiện có.

#### Vì sao A sai (Anh chọn)

A có hai lỗi:

1. **"Install AWS Client VPN on the company data center"** sai chỗ: Client VPN cài trên **thiết bị nhân viên**, không cài ở data center.
2. **Thêm Transit Gateway** để thay peering: có thể chạy nhưng phải cấu hình lại peering đang có, nên trái "minimal changes" và tốn thêm chi phí.

#### Các đáp án sai còn lại

- **B**: tạo Client VPN endpoint ở **mỗi account** là thừa; chỉ cần ở account chính (đã có Site-to-Site VPN và peering), tốn chi phí endpoint gấp nhiều lần.
- **D**: nối Site-to-Site VPN với client VPN endpoint rồi cài Client VPN ở data center: TD ghi "impossible"; client phải ở máy nhân viên.

| Đáp án | Client cài ở | Số endpoint | Đổi mạng hiện có |
|---|---|---|---|
| **C** | Máy nhân viên | 1 (main account) | Không |
| A | Data center (sai) | - | Thay peering bằng TGW |
| B | Máy nhân viên | 1 mỗi account | Nhiều route |
| D | Data center (sai) | - | Không khả thi |

#### Quy tắc nhớ cho thi

- **Thấy "Client VPN"** → client cài trên **máy người dùng**; **một endpoint** ở VPC có đường tới các VPC khác
- **"Minimal changes" + đã có VPC peering** → **không** đổi sang Transit Gateway
- **Client VPN endpoint** không nhân bản theo từng account nếu đã có peering

### TD explanation

**AWS Client VPN**  is a managed client-based VPN service that enables you to securely access your AWS resources and resources in your on-premises network. With Client VPN, you can access your resources from any location using an OpenVPN-based VPN client.

The **administrator**  is responsible for setting up and configuring the service. This involves creating the Client VPN endpoint, associating the target network, configuring the authorization rules, and setting up additional routes (if required).

The **client**  is the end user. This is the person who connects to the Client VPN endpoint to establish a VPN session. The client establishes the VPN session from their local computer or mobile device using an OpenVPN-based VPN client application.

The following are the key components for using AWS Client VPN.

**-Client VPN endpoint**  — Your Client VPN administrator creates and configures a Client VPN endpoint in AWS. Your administrator controls which networks and resources you can access when establishing a VPN connection.

**-VPN client application**  — The software application that you use to connect to the Client VPN endpoint and establish a secure VPN connection.

**-Client VPN endpoint configuration file**  — A configuration file that’s provided to you by your Client VPN administrator. The file includes information about the Client VPN endpoint and the certificates required to establish a VPN connection. You load this file into your chosen VPN client application.

The configuration for this scenario includes a target VPC (VPC A) that is peered with an additional VPC (VPC B). We recommend this configuration if you need to give clients access to the resources inside a target VPC and other VPCs that are peered with it (such as VPC B).

![image](https://media.tutorialsdojo.com/sap_aws_client_vpn.png)

Therefore, the correct answer is: **Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in the same VPC region in the main AWS account. Update the VPC route configurations to allow communication with the internal applications.**  This solution is cost-effective and requires minimal changes to the current network setup.

The option that says: **Install the AWS Client VPN on each employee workstation. Create a Client VPN endpoint in each of the AWS accounts. Update each VPC route configuration to allow communication with the internal applications**  is incorrect. You only need to create a Client VPN endpoint on the main VPC account that has Site-to-Site VPN.

The option that says: **Install the AWS Client VPN on the company data center. Create AWS Transit Gateway to connect the main VPC and other VPCs into a single hub. Update the VPC route configurations to allow communication with the internal applications**  is incorrect. This may be possible, however, this will require reconfiguring the existing VPC peering between the main VPC and the other VPCs in other AWS accounts. Additionally, the AWS Client VPN should be installed on the employee workstations.

The option that says: **Install the AWS Client VPN on the company data center. Configure connectivity between the existing AWS Site-to-Site VPN and client VPN endpoint**  is incorrect. This configuration is impossible and the AWS Client VPN should be installed on the employee workstations and not in the company data center.

**References:**

[https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/scenario-peered.html](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/scenario-peered.html)

[https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

[https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations)

**Check out these Amazon VPC and VPC Peeing Cheat Sheets:**

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

[https://tutorialsdojo.com/vpc-peering/](https://tutorialsdojo.com/vpc-peering/)

</details>

<a id="q29"></a>

## Q29

A company has data centers in Europe, Asia, and North America. Each data center has a 10Gbps AWS Direct Connect connection to AWS, and the company uses a custom VPN to encrypt traffic between its data center network and AWS. In total, the data centers have about five hundred physical servers that host a mix of Windows and Linux-based applications and database services. The company plans to decommission these data centers and migrate its entire infrastructure to the AWS cloud instead. Separate accounts for staging and launching VMs must be implemented, as well as the ability to do AWS Region-to-Region Amazon VPC stack creation.

Which of the following options is the recommended solution for this migration?

- **A.** Leverage AWS Storage Gateway for the migration. Install the AWS Storage Gateway software appliance on their on-premises servers and use it to transfer their data to Amazon S3. Once the data is in S3, use Amazon EC2 to create virtual machines that replicate their on-premises infrastructure.
- **B.** Leverage VM Import/Export for the migration. Convert each physical Windows and Linux server into a virtual machine image, upload the images to Amazon S3, import them as AMIs, and manually launch Amazon EC2 instances in the target AWS Regions for testing and cutover.
- **C.** Leverage AWS Transform MGN for the migration. Install the AWS Replication agent on each physical machine to start the replication to the AWS Cloud. Once syncing is completed, launch test instances and initiate cutover to the AWS Cloud.
- **D.** Leverage AWS Outposts service for the migration of physical servers to AWS. Install the Outposts server agent on the data center to incrementally replicate the servers into Amazon Machine Images (AMIs). Deploy the AMIs into Amazon EC2 instances to initiate cutover.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** 500 physical servers, Windows and Linux, separate staging/launch accounts, migrate off data centers

🪤 **Your trap:** Picked VM Import/Export, which is manual per-server image conversion; MGN replicates physical servers continuously with agent, test launch and cutover.

🧠 **Rule:** Large-scale physical or virtual server rehost = AWS Application Migration Service (MGN) with replication agent.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
3 Data center (EU / Asia / NA)  ~500 physical servers (Windows + Linux)
   │  10Gbps Direct Connect + custom VPN
   ▼
AWS: staging account + launching account, tạo VPC stack Region-to-Region
Yêu cầu: lift-and-shift SỐ LƯỢNG LỚN, có test launch rồi cutover
```

Từ khóa quyết định: **physical servers**, **~500 máy**, **staging/launch**, **test rồi cutover**. Đáp án đúng: **C (AWS Transform MGN)**. Anh chọn B (VM Import/Export).

#### Vì sao C đúng

MGN (Application Migration Service) là dịch vụ **rehost tự động**:

```
Cài AWS Replication Agent trên từng server (Windows/Linux, kể cả physical)
    → replicate liên tục ở mức block vào staging area trong AWS
    → launch TEST instance để kiểm tra
    → OK thì launch CUTOVER instance
```

Replication liên tục nên cutover ngắn, không phải dừng server lâu để export image. Mô hình staging account / launch account là cách MGN tổ chức sẵn.

#### Vì sao B (anh chọn) sai

B trông hợp lý vì "VM Import/Export" là cách đưa máy vào AWS dưới dạng AMI. Nhưng:

- Quy trình **thủ công**: convert từng physical server thành VM image, upload S3, import AMI, launch tay. 500 máy thì không scale.
- Là bản chụp một thời điểm, **không replicate liên tục** nên downtime cutover dài.
- Không có workflow test/cutover và không hỗ trợ tạo stack VPC giữa các Region như đề yêu cầu (theo giải thích của TD).
- Phù hợp migrate nhỏ, lẻ, ad-hoc.

#### Các phương án còn lại

- **A (Storage Gateway):** để kết nối on-prem với storage trên cloud (S3/EBS...), không phải công cụ migrate server đang chạy ứng dụng và database.
- **D (Outposts):** mở rộng hạ tầng AWS về data center của khách, chạy workload ngay tại chỗ. Không phải migration service; "Outposts server agent" không phải cơ chế replicate server.

| Phương án | Bản chất | Tự động cho 500 server | Replicate liên tục |
|---|---|---|---|
| **C. MGN** | Rehost chuyên dụng | Có | Có |
| B. VM Import/Export | Import image thủ công | Không | Không |
| A. Storage Gateway | Hybrid storage | Không liên quan | Không |
| D. Outposts | Hạ tầng AWS tại chỗ | Không liên quan | Không |

📝 Ghi chú kỹ thuật: đề dùng tên "AWS Transform MGN"; trước đây dịch vụ này có tên AWS Application Migration Service (MGN). Cùng một dịch vụ, nên đọc đề thì nhận ra qua chữ **Replication agent**.

#### Quy tắc nhớ cho thi

- **Thấy "physical/virtual servers, hàng trăm máy, lift-and-shift"** → **MGN**
- **Thấy "Replication agent, test launch, cutover"** → **MGN**
- **Thấy "VM Import/Export"** → thủ công, quy mô nhỏ, hiếm khi là đáp án cho migrate lớn
- **Thấy "Storage Gateway"** → hybrid storage, không phải migrate server
- **Thấy "Outposts"** → chạy AWS on-prem, không phải migration

### TD explanation

**AWS Transform MGN**  is an automated lift-and-shift (rehost) solution designed to simplify, accelerate, and lower the cost of migrating applications to AWS. This service enables companies to efficiently lift and shift a large number of physical, virtual, or cloud servers without encountering compatibility issues, performance disruptions, or lengthy cutover periods.

MGN replicates your source servers into your AWS account. When you are ready, it automatically converts and launches these servers on AWS, allowing you to quickly take advantage of the cloud’s cost savings, increased productivity, enhanced resilience, and greater agility. Once your applications are running on AWS, you can utilize AWS services and capabilities to easily replatform or refactor those applications, making lift-and-shift an effective pathway to modernization.

![image](https://media.tutorialsdojo.com/public/AWS%20Transform%20MGN-08JUN2026.png)

AWS Transform MGN is specifically designed for large-scale lift-and-shift migrations of servers. It facilitates the migration of physical, virtual, and cloud servers to AWS. The AWS Replication Agent can be installed on compatible Windows and Linux source servers, enabling continuous block-level replication to AWS. After the replication process, you can launch test instances for validation. Once everything is confirmed, you can proceed with launching cutover instances when the migration is ready. This solution effectively meets the requirements for migrating approximately 500 physical servers, performing test launches, and completing the cutover to AWS.

Therefore, the correct answer is: **Leverage AWS Transform MGN for the migration. Install the AWS Replication agent on each physical machine to start the replication to the AWS Cloud. Once syncing is completed, launch test instances and initiate cutover to the AWS Cloud.**

The option that says: **Leverage AWS Storage Gateway for the migration. Install the Storage Gateway software appliance on their on-premises servers and use it to transfer their data to S3. Once the data is in Amazon S3, use Amazon EC2 to create virtual machines that replicate their on-premises infrastructure**  is incorrect because AWS Storage Gateway is primarily used for connecting an on-premises software appliance with cloud-based storage to provide seamless and secure integration between an organization’s on-premises IT environment and AWS’s storage infrastructure. It is not designed for migrating live applications and databases.

The option that says: **Leverage AWS Outposts service for the migration of physical servers to AWS. Install the Outposts server agent on the data center to incrementally replicate the servers into Amazon Machine Images (AMIs). Deploy the AMIs into Amazon EC2 instances to initiate cutover** is incorrect. AWS Outposts is a service that typically extends AWS infrastructure, services, APIs, and tools to customer premises. It allows customers to build and run applications on-premises using the same programming interfaces as in AWS Regions. It is not a migration service.

The option that says: **Leverage VM Import/Export for the migration. Convert each physical Windows and Linux server into a virtual machine image, upload the images to Amazon S3, import them as AMIs, and manually launch Amazon EC2 instances in the target AWS Regions for testing and cutover**  is incorrect because VM Import/Export is a manual process that is time‑consuming and not scalable for hundreds of servers. It lacks automation, testing workflows, and region‑to‑region stack creation capabilities. It is suitable for small, ad‑hoc migrations but not for large‑scale data center decommissioning.

**References:**

[https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html)

[https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html](https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html)

**Check out these AWS Cheat Sheets:**

[https://tutorialsdojo.com/aws-cheat-sheets/](https://tutorialsdojo.com/aws-cheat-sheets/)

</details>

<a id="q34"></a>

## Q34

A company plans to migrate its on-premises legacy application to AWS and develop a highly scalable application. Currently, all user requests are sent to the on-premises load balancer which forwards the requests to two Linux servers hosting the legacy application. The database is hosted on two servers in master-master configuration. Since this is an old application, the communication to the database servers is done through static IP addresses and not via DNS names. The license of the application is tied to the MAC address of the network adapter of the Linux server. If the application is to be installed on a new server, it will take about 15 hours for the software vendor to send the new license via email.

Which combination of actions must be done to meet the company requirements? (Select TWO.)

- **A.** Create an AWS Lambda function to update the database IP addresses on the Systems Manager Parameter Store. Create an Amazon EC2 bootstrap script that will retrieve the database IP address from SSM Parameter Store. Update the local configuration files with the parameters.
- **B.** Install the application on an EC2 instance and configure the needed license file. Update the local configuration with the database IP addresses. Use this instance as the base AMI for all instances in the Auto Scaling group.
- **C.** Create an Amazon EC2 bootstrap script that will resolve the database DNS names into IP addresses. Update the local configuration files with the resolved values.
- **D.** Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files on an Amazon S3 bucket and use bootstrap scripts to retrieve an unused license file and attach corresponding ENI when provisioning EC2 instances.
- **E.** Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files inside an Amazon EC2 instance and create a base AMI from this EC2 instance. Use bootstrap scripts to configure license keys and attach the corresponding ENI when provisioning EC2 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** B, D

🔑 **Key words:** legacy app, license tied to MAC address, static DB IPs, new license takes 15 hours

🪤 **Your trap:** Picked B (license baked into one AMI); each instance needs its own MAC-bound license. Need a pool of licensed ENIs (licenses in S3) and DB IPs in Parameter Store.

🧠 **Rule:** MAC-bound license: pre-license a pool of ENIs, keep license files in S3, attach via bootstrap; config values (DB IPs) in SSM Parameter Store.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Legacy app (Linux)  ──license gắn với MAC address──►  xin license mới ~15 GIỜ
        │
        └── kết nối DB master-master bằng STATIC IP (không dùng DNS)

Mục tiêu: Auto Scaling, scale được mà KHÔNG chờ license mới
```

Hai vấn đề độc lập, cần **hai** hành động: (1) giải bài toán **license/MAC**, (2) giải bài toán **IP của DB**. Đáp án đúng: **A + D**. Anh chọn B + D: D đúng, B sai.

#### Hai lựa chọn đúng ghép thành một giải pháp

**D, giải license/MAC:** MAC address đi theo **ENI**. Tạo trước một pool ENI, xin vendor license cho từng ENI, để license file trên S3. Khi EC2 khởi động, bootstrap script lấy license chưa dùng và attach ENI tương ứng. Instance mới không cần chờ 15 giờ vì license đã có sẵn theo ENI.

```
Pool ENI (MAC cố định) ◄──► license file trên S3
EC2 mới → bootstrap: lấy license chưa dùng → attach ENI đúng cặp
```

Lưu license trên S3 giúp thêm/bớt license dễ dàng, không phải sửa AMI.

**A, giải static IP của DB:** Lambda cập nhật IP của DB vào **SSM Parameter Store**; bootstrap script đọc từ Parameter Store rồi ghi vào config. Một chỗ lưu tập trung, thêm/bớt DB không phải sửa script trên từng instance.

#### Vì sao B (anh chọn) sai

B tạo base AMI từ một instance đã cài và gắn license. B trông tiện vì "AMI = nhân bản nhanh". Nhưng license **gắn với MAC address**; instance mới từ AMI sẽ có MAC mới nên license không còn hợp lệ. Muốn xin lại thì mất 15 giờ, trái hẳn yêu cầu scale.

#### Các phương án sai khác

- **C:** script resolve DNS name thành IP trong bootstrap. Làm được nhưng không khuyến nghị: mỗi lần thêm DB mới phải sửa script thủ công. A thì tập trung hơn.
- **E:** cũng dùng pool ENI nhưng nhét license vào trong AMI. Làm được nhưng không lý tưởng: thêm ENI/license mới thì phải cập nhật lại base AMI, tốn công nếu scale thường xuyên. D (S3) tốt hơn.

| Vấn đề | Đúng | Sai (vì sao) |
|---|---|---|
| License/MAC | **D** (S3 + ENI pool) | B (MAC đổi), E (license trong AMI) |
| Static IP DB | **A** (Parameter Store) | C (script phải sửa tay) |

#### Quy tắc nhớ cho thi

- **Thấy "license gắn MAC address"** → **pool ENI**, license đặt ở nơi tập trung (S3), không bake vào AMI
- **Thấy "cấu hình IP/config dùng chung cho nhiều instance"** → **SSM Parameter Store** thay vì hard-code trong script/AMI
- **Câu "Select TWO"** → tách ra từng vấn đề, mỗi đáp án giải một vấn đề

### TD explanation

**AWS Systems Manager Parameter Store**  provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values as plain text or encrypted data. You can reference Systems Manager parameters in your scripts, commands, SSM documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter.

Parameter Store offers these benefits:

– You can use a secure, scalable, hosted secrets management service with no servers to manage.

– Improve your security posture by separating your data from your code.

– Store configuration data and encrypted strings in hierarchies and track versions.

– Control and audit access at granular levels.

Parameter Store provides support for three types of parameters: `String`, `StringList`, and `SecureString`.

![image](https://media.tutorialsdojo.com/public/Parameter-Store_29AUG2023.jpg)

An **elastic network interface (ENI)**  is a logical networking component in a VPC that represents a virtual network card. It can include the following attributes:

– A primary private IPv4 address from the IPv4 address range of your VPC

– One or more secondary private IPv4 addresses from the IPv4 address range of your VPC

– One Elastic IP address (IPv4) per private IPv4 address

– One public IPv4 address

– One or more IPv6 addresses

– One or more security groups

– A MAC address

– A source/destination check flag

– A description

You can create and configure network interfaces in your account and attach them to instances in your VPC. Your account might also have requester-managed network interfaces, which are created and managed by AWS services to enable you to use other resources and services.

You can create a network interface, attach it to an instance, detach it from an instance, and attach it to another instance. The attributes of a network interface follow it as it’s attached or detached from an instance and reattached to another instance. When you move a network interface from one instance to another, network traffic is redirected to the new instance.

Each instance has a default network interface, called the primary network interface. You cannot detach a primary network interface from an instance. You can create and attach additional network interfaces.

The option that says: **Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files on an Amazon S3 bucket and use bootstrap scripts to retrieve an unused license file and attach corresponding ENI when provisioning EC2 instances**  is correct. Having the license files on an Amazon S3 bucket reduces the management overhead for the EC2 instances, as you can easily add/remove more license keys if needed.

The option that says: **Create an AWS Lambda function to update the database IP addresses on the Systems Manager Parameter Store. Create an Amazon EC2 bootstrap script that will retrieve the database IP address from SSM Parameter Store. Update the local configuration files with the parameters**  is correct. Having the database IP addresses on Parameter Store ensures that all the EC2 instances will have a central location to retrieve the IP addresses. This also reduces the need to constantly update any script from inside the EC2 instance even if you add/remove more databases in the future.

The option that says: **Provision a pool of Elastic Network Interfaces (ENIs). Request a license file for each ENI from the software vendor. Store the license files inside an Amazon EC2 instance and create a base AMI from this EC2 instance. Use bootstrap scripts to configure license keys and attach the corresponding ENI when provisioning EC2 instances**  is incorrect. Although this is possible, this is not an ideal solution. If you need more EC2 instances and more ENIs, you will have to manually update your base AMI to include all the new license files. This can be a lot of work if you scale your cluster on a regular basis.

The option that says: **Create an Amazon EC2 bootstrap script that will resolve the database DNS names into IP addresses. Update the local configuration files with the resolved values**  is incorrect. Although this is possible, this is not recommended. You will have to update the bootstrap script manually for the new DNS name every time you create a new database such as when you are scaling out your database instances.

The option that says: **Install the application on an EC2 instance and configure the needed license file. Update the local configuration with the database IP addresses. Use this instance as the base AMI for all instances in the Auto Scaling group**  is incorrect. This will not work because the application license is tied to the MAC address on which it was installed. When you provision a new EC2 instance, it will have a new IP address and a newly assigned MAC address for its network adapter.

**References:**

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)

[https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

[https://docs.aws.amazon.com/cdk/latest/guide/get_ssm_value.html](https://docs.aws.amazon.com/cdk/latest/guide/get_ssm_value.html)

**Check out these AWS SSM Parameter Store and Amazon EC2 Cheat Sheets:**

[https://tutorialsdojo.com/aws-secrets-manager-vs-systems-manager-parameter-store/](https://tutorialsdojo.com/aws-secrets-manager-vs-systems-manager-parameter-store/)

[https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)

</details>

<a id="q44"></a>

## Q44

A company runs its travel and tours website on AWS. The application only supports HTTP at the moment. To improve their SEO ranking and provide more security for their customers, they decided to enable SSL on their website. The company would also like to ensure the separation of roles between the Development team and the Security team in handling the sensitive SSL certificate. The Development team can log in to EC2 Instances but they should not have access to the SSL certificate, which only the Security team has exclusive control of. Currently, they are using an Application Load Balancer which provides loads of incoming traffic to an Auto Scaling group of On-Demand EC2 instances.

Which of the following options should the solutions architect implement to satisfy the above requirements?

- **A.** In the web server, set the file owner of the SSL certificate to the Security team and set the file permissions to `700` which will deny all access to the Development team.
- **B.** Create a new private S3 bucket and then upload the SSL certificate owned by the Security team. Configure the EC2 instance to have exclusive access to the certificate and block any access from the Development team.
- **C.** Store the SSL certificate in IAM and authorize access only to the Security team using an IAM policy. Configure the Application Load Balancer to use the SSL certificate instead of the EC2 instances.
- **D.** Retrieve a read-only copy of the SSL certificate upon the boot of the EC2 instance from a CloudHSM, which is exclusively managed by the Security team.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** enable SSL on HTTP-only site, separate Development and Security team roles for the certificate

🪤 **Your trap:** Picked CloudHSM on the EC2 instances; clients hit the load balancer, not instances, and CloudHSM adds cost. Store cert in IAM, restrict by policy, terminate SSL at ALB.

🧠 **Rule:** Separation of duties for SSL cert: store cert in IAM/ACM with IAM policy for Security team and attach it to the ALB, not EC2.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──HTTPS?──► ALB ──HTTP──► Auto Scaling EC2 (Dev login được)
Yêu cầu: Dev team KHÔNG được thấy SSL certificate; chỉ Security team quản lý
```

Từ khóa: **Dev có thể login vào EC2** → bất kỳ nơi nào cert nằm trên EC2 đều là rủi ro. Đáp án đúng: **C (cert lưu ở IAM, ALB dùng cert, IAM policy chỉ cho Security team)**. Anh chọn D (CloudHSM).

#### Vì sao C đúng

```
Security team ──IAM policy──► SSL cert trong IAM (hoặc ACM)
ALB HTTPS listener dùng cert này để terminate SSL
EC2 chỉ nói HTTP, KHÔNG có cert
```

- Ứng dụng chỉ hỗ trợ HTTP, và client đi qua ALB, nên **terminate SSL tại ALB** là hợp lý.
- Cert không bao giờ nằm trên EC2 nên Dev có login cũng không lấy được.
- Quyền truy cập cert kiểm soát bằng IAM policy, tách rõ vai trò Security và Dev.

#### Vì sao D (anh chọn) sai

D trông "an toàn" vì CloudHSM là nơi lưu khóa bảo mật cao. Nhưng:

- Client truy cập qua **Load Balancer**, không trực tiếp tới EC2, nên cert cần nằm ở ALB.
- D vẫn lấy một bản copy cert về EC2 lúc boot, nên Dev login vào EC2 vẫn có thể thấy bản copy đó. Không đạt yêu cầu tách vai trò.
- CloudHSM tăng chi phí mà không giải được yêu cầu (theo TD).

#### Các phương án sai khác

- **A:** đổi owner file cert sang Security và chmod 700 trên web server. Không cần để cert trên EC2; user có quyền cao trên instance vẫn có thể vượt qua phân quyền file, và SSL đáng ra đặt ở ALB.
- **B:** cert trong S3 private rồi cho EC2 tải về. Sau khi tải, cert nằm trên EC2, Dev login vào là thấy.

| Phương án | Cert nằm ở đâu | Dev tiếp cận được? |
|---|---|---|
| **C** | IAM/ACM + ALB | Không |
| A | File trên EC2 | Có thể |
| B | S3 rồi tải về EC2 | Có (sau khi tải) |
| D | CloudHSM rồi copy về EC2 | Có (bản copy) + tốn tiền |

#### Quy tắc nhớ cho thi

- **Thấy "tách quyền Dev/Security với SSL cert"** → **cert ở ALB (ACM/IAM)**, không đặt trên EC2
- **Thấy "app chỉ HTTP + muốn HTTPS"** → **HTTPS listener ở ALB (SSL offload)**
- **Thấy "CloudHSM" mà đề không đòi key phần cứng/compliance** → thường chỉ làm tăng chi phí

### TD explanation

In the ALB, you can create a listener that uses encrypted connections (also known as SSL offload). This feature enables traffic encryption between your load balancer and the clients that initiate SSL or TLS sessions. To use an HTTPS listener, you must deploy an SSL/TLS server certificate on your load balancer. The load balancer uses this certificate to terminate the connection and then decrypt requests from clients before sending them to the targets.

Although you can terminate the SSL in the EC2 instance, this setup is not recommended in this scenario. It is best to store the SSL certificate in IAM or in AWS Certificate Manager (ACM) where you can control which teams, either the Security or the Development team, can have access.

![image](https://media.tutorialsdojo.com/sap_alb_ssl_cert.png)

Therefore the correct answer is: **Store the SSL certificate in IAM and authorize access only to the Security team using an IAM policy. Configure the Application Load Balancer to use the SSL certificate instead of the EC2 instances.**

The option that says: **In the web server, set the file owner of the SSL certificate to the Security team and set the file permissions to `700` which will deny all access to the Development team**  is incorrect. You don’t have to store the SSL Cert on the EC2 instances. The SSL certificate should be at the Load Balancer since the EC2 instances are behind it and the application only supports HTTP.

The option that says: **Retrieve a read-only copy of the SSL certificate upon the boot of the EC2 instance from a CloudHSM, which is exclusively managed by the Security team**  is incorrect. The clients access the website through the Load Balancer and not the EC2 instances directly. Using CloudHSM to store your SSL certificate will just increase your costs without satisfying the requirement.

The option that says: **Create a new private S3 bucket and then upload the SSL certificate owned by the Security team. Configure the EC2 instance to have exclusive access to the certificate and block any access from the Development team**  is incorrect. The Developers can log in to the EC2, therefore, they will still be able to access the SSL certificate in the EC2 instances after they were downloaded from Amazon S3.

**References:**

[https://aws.amazon.com/premiumsupport/knowledge-center/elb-ssl-tls-certificate-https/](https://aws.amazon.com/premiumsupport/knowledge-center/elb-ssl-tls-certificate-https/)

[https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates)

**Check out this AWS Elastic Load Balancing (ELB) Cheat Sheet:**

[https://tutorialsdojo.com/aws-elastic-load-balancing-elb/](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/)

</details>

<a id="q56"></a>

## Q56

A large media company based in Los Angeles, California, operates a MySQL RDS instance within an AWS VPC. The company has a custom analytics application running in its on-premises data center that requires read-only access to the database. The company aims to replicate the data from the MySQL RDS instance in AWS to a MySQL instance located on-premises to serve as the read-only endpoint for this analytics application.

Which of the following options is the most secure way of performing this replication?

- **A.** RDS cannot replicate to an on-premises database server. Instead, configure the RDS instance to replicate to an EC2 instance with core MySQL and then configure replication over a secure VPN/VPG connection.
- **B.** Create a Data Pipeline that exports the MySQL data each night and securely downloads the data from an S3 HTTPS endpoint. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication.
- **C.** Configure the RDS instance as the master and enable replication over the open Internet using an SSL endpoint to the on-premises server. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication.
- **D.** Create an IPSec VPN connection using either OpenVPN or VPN/VGW through the Virtual Private Cloud service. Prepare an instance of MySQL running external to Amazon RDS. Configure the MySQL RDS instance to be the replication source. Use `mysqldump` to transfer the database from the Amazon RDS instance to the on-premises MySQL instance and start the replication from the Amazon RDS Read Replica.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** replicate RDS MySQL to on-premises MySQL for read-only analytics, most secure

🪤 **Your trap:** Picked A (replicate to an EC2 MySQL first), claiming RDS cannot replicate on-premises; a secure IPSec VPN to the VPC makes direct replication to on-premises MySQL feasible.

🧠 **Rule:** RDS MySQL to on-premises replication: IPSec VPN or VGW, external MySQL as replica, mysqldump seed, start replication. SSL endpoint alone is not it.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS VPC                                   On-premises (LA)
┌──────────────────┐   IPsec VPN / DX     ┌──────────────────┐
│ RDS MySQL        │ ═══════════════════► │ MySQL (tự dựng)  │
│ (replication     │   mã hóa đường truyền│ read-only cho    │
│  source)         │                      │ analytics app    │
└──────────────────┘                      └──────────────────┘
        Yêu cầu: replicate RDS -> on-premises, "most SECURE"
```

Đáp án đúng: **D**. Anh chọn **A** (replicate sang EC2 rồi mới VPN).

#### Vì sao D đúng

RDS MySQL/MariaDB **có thể** làm replication source cho một MySQL ở on-premises. Các bước theo TD:

1. Dựng kết nối riêng giữa VPC và data center: **IPsec VPN (VGW)** hoặc **Direct Connect**.
2. Dựng MySQL on-premises, chạy vai trò replica.
3. Cấu hình RDS MySQL là replication source (master).
4. Dùng `mysqldump` chép dữ liệu ban đầu, rồi start replication.

Traffic replication đi trong tunnel IPsec: được **authenticate + encrypt từng packet** nên giữ được confidentiality và integrity, không lộ ra Internet.

#### Vì sao A (Anh chọn) sai

A mở đầu bằng câu "RDS cannot replicate to an on-premises database server" - đây là **tiền đề sai**. Ngoài ra A replicate sang EC2: EC2 và RDS đều đã nằm trong AWS nên không cần VPN cho đoạn đó, và analytics app on-premises vẫn không có read-only endpoint nào ở on-premises. Không giải quyết yêu cầu.

#### Các option còn lại

- **B** - Data Pipeline export hàng đêm: đây là batch job, không phải replication liên tục; không tạo được replica đồng bộ.
- **C** - Replication qua Internet mở bằng "SSL endpoint": SSL endpoint chỉ dùng để truy cập DB an toàn, không phải kênh bảo vệ replication; đi Internet mở kém an toàn hơn VPN. Ngoài ra chép dữ liệu "từ S3" là không khớp.

| Option | Kênh truyền | Có replica on-prem? | Secure? |
|---|---|---|---|
| **D** | IPsec VPN / VGW | Có | Cao nhất |
| A | VPN (không cần thiết) | Không | Tiền đề sai |
| B | S3 HTTPS, theo đêm | Không (chỉ batch) | Không phải replication |
| C | Internet mở + SSL | Có | Thấp hơn VPN |

#### Lưu ý thực tế

- Trước khi replicate cần có đường mạng riêng (VPN hoặc **AWS Direct Connect**) - đây là điều kiện tiên quyết theo TD.
- `mysqldump` chỉ để seed dữ liệu ban đầu, replication chạy tiếp sau đó.

#### Quy tắc nhớ cho thi

- **Thấy "replicate RDS MySQL về on-premises, most secure"** -> **IPsec VPN/DX + RDS làm source + mysqldump seed**
- **Thấy "RDS cannot replicate to on-premises"** -> câu khẳng định sai, loại ngay
- **Thấy "SSL endpoint" cho replication** -> SSL chỉ bảo vệ kết nối truy cập, không thay thế VPN
- **Thấy "Data Pipeline / nightly export"** -> batch, không phải replication

### TD explanation

Amazon supports **Internet Protocol security (IPsec) VPN**  connections. IPsec is a protocol suite for securing Internet Protocol (IP) communications by authenticating and encrypting each IP packet of a data stream. Data transferred between your VPC and datacenter routes over an encrypted VPN connection to help maintain the confidentiality and integrity of data in transit. An Internet gateway is not required to establish a hardware VPN connection.

You can set up replication between an **Amazon RDS MySQL**  (or MariaDB DB instance) that is running in AWS and a MySQL (or MariaDB instance) to your on-premises data center. A read replica is a read-only copy of a MySQL database instance that is kept synchronized with the source instance. Read replicas can be used to offload read traffic from the primary instance, improving performance and scalability.

![image](https://media.tutorialsdojo.com/public/td-RDS-replication-On-premise-05-Aug-2024.png)

To allow communication between RDS and to your on-premises network, you must first set up a VPN or an AWS *Direct Connect*  connection. Once that is done, just follow the below steps to perform the replication:

- Set up a MySQL database server in the on-premises environment, which will act as the read replica for the RDS instance.

- Configure the RDS MySQL instance as the replication source (master) for the on-premises MySQL instance.

- Use the **`mysqldump`**  utility to transfer the initial data from the Amazon RDS instance to the on-premises MySQL instance. This step is necessary to establish the initial replication state.

- After the initial data transfer, start the replication process from the on-premises MySQL instance, which will act as a read replica of the Amazon RDS instance.

By following this approach, the data replication traffic between the RDS instance and the on-premises MySQL server is securely transmitted over the IPSec VPN connection, ensuring the confidentiality and integrity of the data during transit, rather than exposing the RDS instance directly to the internet or using less secure methods for data transfer.

Hence, the correct answer is **Create an IPSec VPN connection using either OpenVPN or VPN/VGW through the Virtual Private Cloud service. Prepare an instance of MySQL running external to Amazon RDS. Configure the MySQL RDS instance to be the replication source. Use `mysqldump` to transfer the database from the Amazon RDS instance to the on-premises MySQL instance and start the replication from the Amazon RDS Read Replica** because it is feasible to set up the secure IPSec VPN connection between the on-premises server and AWS VPC using the VPN/Gateways.

The option that says: **Configure the RDS instance as the master and enable replication over the open Internet using an SSL endpoint to the on-premises server. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication**  is incorrect because SSL endpoint cannot be utilized here as it is only used to securely access the database.

The option that says: **RDS cannot replicate to an on-premises database server. Instead, configure the RDS instance to replicate to an EC2 instance with core MySQL and then configure replication over a secure VPN/VPG connection**  is incorrect because you do not need to establish a secure VPN/VPG connection in the first place as EC2 and RDS are both in AWS Cloud.

The option that says: **Create a Data Pipeline that exports the MySQL data each night and securely downloads the data from an S3 HTTPS endpoint. Use `mysqldump` to transfer the database from the Amazon S3 to the on-premises MySQL instance and start the replication**  is incorrect because Data Pipeline is primarily for batch jobs and is not suitable for this scenario.

**References:**

[https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)

[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Exporting.NonRDSRepl.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Exporting.NonRDSRepl.html)

**Check out these Amazon RDS and Amazon VPC Cheat Sheets:**

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

**Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:**

[https://tutorialsdojo.com/aws-certified-solutions-architect-professional/](https://tutorialsdojo.com/aws-certified-solutions-architect-professional/)

</details>

<a id="q65"></a>

## Q65

A company has an on-premises data center that is hosting its gaming service. Its primary function is player-matching and is accessible from players around the world. The gaming service prioritizes network speed for the users so all traffic to the servers uses User Datagram Protocol (UDP). As more players join, the company is having difficulty scaling its infrastructure so it plans to migrate the service to the AWS cloud. The Solutions Architect has been tasked with the migration and AWS Shield Advanced has been enabled already to protect all public-facing resources.

Which of the following actions should the Solutions Architect implement to achieve the company requirements? (Select TWO.)

- **A.** Place the Auto Scaling of Amazon EC2 instances behind an Internet-facing Application Load Balancer (ALB). For the domain name, create an Amazon Route 53 entry that is Aliased to the FQDN of the ALB.
- **B.** Set up network ACL rules on the VPC to deny all non-UDP traffic. Ensure that the NACL is associated with the load balancer subnets.
- **C.** Place the Auto Scaling of Amazon EC2 instances behind a Network Load Balancer (NLB). For the domain name, create an Amazon Route 53 entry that points to the Elastic IP address of the NLB.
- **D.** Create an AWS WAF rule that will explicitly block all non-UDP traffic. Ensure that the AWS WAF rule is associated with the load balancer of the EC2 instances.
- **E.** Create an Amazon CloudFront distribution and set the Load Balancer as the origin. Use only secure protocols on the distribution origin settings.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C · **You picked:** C, E

🔑 **Key words:** UDP gaming service, Shield Advanced enabled, migrate to AWS, select two

🪤 **Your trap:** Picked CloudFront (E), which does not fit a UDP service; WAF can't protect NLB either. Use NLB for UDP and NACL to deny non-UDP.

🧠 **Rule:** UDP traffic = Network Load Balancer (Layer 4). Block non-UDP with NACLs; WAF and ALB are Layer 7 and don't apply.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Người chơi toàn cầu --UDP--> [Route 53] -> [NLB (EIP)] -> Auto Scaling EC2
                                   ▲
                      NACL: deny non-UDP ở subnet của LB
                      Shield Advanced bảo vệ resource (EIP/NLB)
Yêu cầu: UDP, ưu tiên tốc độ mạng, chống DDoS
```

Đáp án đúng: **B + C**. Anh chọn **C, E**: C đúng, E sai, thiếu B.

#### Hai đáp án đúng ghép thành một giải pháp

- **C - NLB**: hoạt động ở Layer 4, xử lý cả TCP và UDP, hàng triệu request/giây với latency cực thấp, có một static IP (Elastic IP) mỗi AZ. Với UDP, NLB chọn target bằng flow hash (protocol, source IP/port, destination IP/port). Route 53 trỏ tới EIP của NLB. Với Shield Advanced, EIP đăng ký làm protected resource thì DDoS được phát hiện nhanh hơn.
- **B - NACL** deny non-UDP: vì toàn bộ traffic tới server là UDP nên chặn mọi giao thức khác ở subnet của LB để giảm bề mặt tấn công (ví dụ TCP flood). NACL hỗ trợ cả allow lẫn deny rule và Shield Advanced còn tích hợp NACL để chặn ở edge.

#### Vì sao E (Anh chọn) sai

Đặt **CloudFront** trước LB không phù hợp: workload là UDP gaming, ưu tiên tốc độ mạng. TD nêu CloudFront vốn đã được Shield Standard bảo vệ mặc định, nhưng không thay thế giải pháp cần: chặn non-UDP bằng NACL và dùng NLB. Việc "chỉ dùng secure protocols ở origin" cũng không giải quyết yêu cầu UDP. Anh chọn E vì nghĩ "CloudFront = chống DDoS", nhưng không khớp yêu cầu.

#### Các option còn lại

- **A** - ALB ở Layer 7 (HTTP/HTTPS), không nhận UDP.
- **D** - AWS WAF không bảo vệ NLB (theo TD), và WAF lọc HTTP chứ không lọc theo "non-UDP"; dùng NACL.

| Option | Lý do |
|---|---|
| **C. NLB + Route 53 tới EIP** | L4, UDP, latency thấp |
| **B. NACL deny non-UDP** | Giảm tấn công ngoài UDP |
| A. ALB | L7, không UDP |
| D. WAF | Không áp dụng cho NLB |
| E. CloudFront | Không phù hợp UDP/yêu cầu |

#### Quy tắc nhớ cho thi

- **Thấy "UDP / TCP, low latency, static IP"** -> **NLB**; **ALB** chỉ HTTP/HTTPS
- **Thấy "chặn giao thức/IP cụ thể ở subnet, DDoS"** -> **NACL** (có deny rule)
- **Thấy "WAF" + NLB** -> WAF không đi với NLB
- **Shield Advanced** + **EIP/NLB** = protected resource, phát hiện nhanh hơn

### TD explanation

A**Network Load Balancer**  operates at the connection level (Layer 4), routing connections to targets (Amazon EC2 instances, microservices, and containers) within Amazon VPC based on IP protocol data. Ideal for load balancing of both TCP and UDP traffic, Network Load Balancer is capable of handling millions of requests per second while maintaining ultra-low latencies. Network Load Balancer is optimized to handle sudden and volatile traffic patterns while using a single static IP address per Availability Zone.

For UDP traffic, the load balancer selects a target using a flow hash algorithm based on the protocol, source IP address, source port, destination IP address, and destination port. A UDP flow has the same source and destination, so it is consistently routed to a single target throughout its lifetime. Different UDP flows have different source IP addresses and ports so that they can be routed to different targets.

![image](https://media.tutorialsdojo.com/sap_nlb_ec2_backend.png)

When you create **Network Access Control Lists (NACLs)** , you can specify both allow and deny rules. This is useful if you want to explicitly deny certain types of traffic to your application. For example, you can define IP addresses (as CIDR ranges), protocols, and destination ports that are denied access to the entire subnet. If your application is used only for TCP traffic, you can create a rule to deny all UDP traffic or vice versa. This option is useful when responding to DDoS attacks because it lets you create your own rules to mitigate the attack when you know the source IPs or other signatures.

![image](https://media.tutorialsdojo.com/sap_nacl_subnet.png)

If you are subscribed to AWS Shield Advanced, you can register Elastic IPs (EIPs) as Protected Resources. DDoS attacks against EIPs that have been registered as Protected Resources are detected more quickly, which can result in a faster time to mitigate.

The option that says: **Place the Auto Scaling of Amazon EC2 instances behind a Network Load Balancer (NLB). For the domain name, create an Amazon Route 53 entry that points to the Elastic IP address of the NLB**  is correct. The service uses UDP traffic and prioritizes network speed, so a Network Load Balancer is ideal for this scenario. You can create a Route 53 entry pointing to the NLB’s Elastic IP.

The option that says: **Set up network ACL rules on the VPC to deny all non-UDP traffic. Ensure that the NACL is associated with the load balancer subnets**  is correct. Since all traffic to the servers is UDP, you can set NACL to block all non-UDP traffic which can help block attacks such as traffic coming from TCP connections.

The option that says: **Place the Auto Scaling of Amazon EC2 instances behind an internet-facing Application Load Balancer (ALB). For the domain name, create an Amazon Route 53 entry that is Aliased to the FQDN of the ALB** is incorrect. UDP traffic operates at Layer 4 of the OSI model while an ALB operates at Layer 7. A Network Load Balancer is a better fit for this scenario.

The option that says: **Create an AWS WAF rule that will explicitly block all non-UDP traffic. Ensure that the AWS WAF rule is associated with the load balancer of the EC2 instances**  is incorrect. AWS WAF rules cannot protect a Network Load Balancer yet. It is better to use NACL rules to block the non-UDP traffic.

The option that says: **Create an Amazon CloudFront distribution and set the Load Balancer as the origin. Use only secure protocols on the distribution origin settings**  is incorrect. Although CloudFront does provide caching and security settings for the origin, it helps mitigate DDoS attacks to your instances or NLBs because AWS Shield Standard is enabled by default. For more advanced DDoS mitigation AWS Shield Advanced offers integration with NACLs that will block traffic at the edge of the AWS Network.

**References:**

[https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/security-groups-and-network-access-control-lists-nacls-bp5.html](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/security-groups-and-network-access-control-lists-nacls-bp5.html)

[https://aws.amazon.com/blogs/security/now-you-can-use-aws-shield-advanced-to-protect-your-amazon-ec2-instances-and-network-load-balancers/](https://aws.amazon.com/blogs/security/now-you-can-use-aws-shield-advanced-to-protect-your-amazon-ec2-instances-and-network-load-balancers/)

[https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)

**Check out these Application Load Balancer and AWS Shield Cheat Sheets:**

[https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-classic-load-balancer/](https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-classic-load-balancer/)

[https://tutorialsdojo.com/aws-shield/](https://tutorialsdojo.com/aws-shield/)

</details>

<a id="q74"></a>

## Q74

A company wants to have a secure content management solution that can be accessed by its external custom applications via API calls. The solutions architect has been instructed to create the infrastructure design. The solution should enable users to upload documents as well as download a specific version or the latest version of a document. There is also a requirement to enable customer administrators to simply submit an API call that can roll back changes to existing files sent to the system.

Which of the following options is the MOST secure and suitable solution that the solutions architect should implement?

- **A.** Use S3 with Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Use client-side encryption to encrypt customer files then share the KMS Key ID and the client-side master key to all customers in order to access the CMS.
- **B.** Use Amazon WorkDocs for document storage and utilize its user access management, version control, and built-in encryption. Integrate the Amazon WorkDocs Content Manager to the external custom applications. Develop a rollback feature to replace the current document version with the previous version from Amazon WorkDocs.
- **C.** Use Amazon S3 with Versioning and Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Encrypt all documents using client-side encryption for enhanced data security. Share the encryption keys to all customers to unlock the documents. Develop a rollback feature to replace the current document version with the previous version from Amazon S3.
- **D.** Use Amazon EFS for object storage and enable data encryption in transit with TLS. Store unique customer managed keys in AWS KMS. Set up IAM roles and IAM access policies for EFS to specify separate encryption keys for each customer application. Utilize file locking and file versioning features in EFS to roll back changes to existing files stored in the CMS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** secure content management via API, version download, API rollback, external custom apps

🪤 **Your trap:** Picked S3 with client-side encryption and shared keys, a security risk and custom rollback; WorkDocs gives access management, versioning and encryption built in.

🧠 **Rule:** Document management with versioning, user access control and encryption, API access = Amazon WorkDocs. Never share encryption keys with customers.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
External custom apps --API--> [CMS: lưu tài liệu]
   Cần: upload, download bản cụ thể hoặc mới nhất, admin gọi API để ROLLBACK
   Điều kiện: MOST secure và suitable
```

Đáp án đúng: **B (Amazon WorkDocs)**. Anh chọn **C** (S3 + Versioning + client-side encryption).

#### Vì sao B đúng

**Amazon WorkDocs** là dịch vụ quản lý nội dung được quản lý hoàn toàn, có sẵn **user access management, version control, built-in encryption** và API phong phú. **WorkDocs Content Manager** là tiện ích cấp cao để upload/download nội dung, dùng được cho cả ứng dụng người dùng (anonymous AWS credentials + authentication token) và ứng dụng admin (khởi tạo client bằng IAM credentials). Rollback: đọc phiên bản trước rồi thay phiên bản hiện tại.

Mọi yêu cầu (upload, tải theo version, rollback qua API, bảo mật) đều có sẵn, không phải tự xây.

📝 **Ghi chú kỹ thuật:** AWS đã **ngừng (retire) Amazon WorkDocs vào năm 2025**, nhưng đây vẫn là đáp án mong đợi của bộ đề này. Khi thi/luyện đề này, chọn WorkDocs; trong thực tế mới thì dùng S3 versioning hoặc giải pháp khác.

#### Vì sao C (Anh chọn) sai

C có Versioning và rollback bằng S3 nên về chức năng ổn, nhưng điểm chết là "**Share the encryption keys to all customers**": chia sẻ key mã hóa cho mọi khách hàng là rủi ro bảo mật, trái với "MOST secure". Anh bị cuốn vào phần S3 versioning mà bỏ qua câu key sharing.

#### Các option còn lại

- **A** - S3 chỉ bật Server Access Logging, **không bật Versioning** nên không có version/rollback; lại chia sẻ KMS Key ID và client-side master key cho khách hàng.
- **D** - **EFS** là file system, không phải object storage; có file locking nhưng **không có file versioning**, nên không rollback được như đề yêu cầu.

| Option | Versioning/rollback | Quản lý key | Kết luận |
|---|---|---|---|
| **B. WorkDocs** | Có | Built-in encryption | Đúng |
| C. S3 + Versioning | Có | Share key cho khách | Rủi ro bảo mật |
| A. S3 logging | Không | Share key + master key | Sai |
| D. EFS | Không có versioning | KMS | Sai |

#### Quy tắc nhớ cho thi

- **Thấy "content management + versioning + API + secure"** -> **Amazon WorkDocs** (trong bộ đề này)
- **Thấy "chia sẻ encryption key / master key cho khách hàng"** -> luôn là rủi ro, loại
- **Thấy "EFS versioning"** -> EFS không có file versioning
- **Server Access Logging** không phải Versioning

### TD explanation

**Amazon WorkDocs**  is a fully managed, secure content creation, storage, and collaboration service. With Amazon WorkDocs, you can easily create, edit, and share content, and because it’s stored centrally on AWS, access it from anywhere on any device. Amazon WorkDocs makes it easy to collaborate with others, and lets you easily share content, provide rich feedback, and collaboratively edit documents. You can use Amazon WorkDocs to retire legacy file share infrastructure by moving file shares to the cloud. Amazon WorkDocs lets you integrate with your existing systems, and offers a rich API so that you can develop your own content-rich applications. Amazon WorkDocs is built on AWS, where your content is secured on the world’s largest cloud infrastructure.

![image](https://media.tutorialsdojo.com/sap_amazon_workdocs_overview.png)

Amazon WorkDocs Content Manager is a high-level utility tool that uploads content or downloads it from an Amazon WorkDocs site. It can be used for both administrative and user applications. For user applications, a developer must construct the Amazon WorkDocs Content Manager with anonymous AWS credentials and an authentication token. For administrative applications, the Amazon WorkDocs client must be initialized with AWS Identity and Access Management (IAM) credentials. In addition, the authentication token must be omitted in subsequent API calls.

Hence, the correct answer in this scenario is: **Use Amazon WorkDocs for document storage and utilize its user access management, version control, and built-in encryption. Integrate the Amazon WorkDocs Content Manager to the external custom applications. Develop a rollback feature to replace the current document version with the previous version from Amazon WorkDocs.**

The option that says: **Use Amazon S3 with Versioning and Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Encrypt all documents using client-side encryption for enhanced data security. Share the encryption keys to all customers to unlock the documents. Develop a rollback feature to replace the current document version with the previous version from Amazon S3**  is incorrect. Although you can use Amazon S3, sharing the encryption keys to all customers just to unlock the documents is a security risk.

The option that says: **Use S3 with Server Access Logging enabled. Set up an IAM role and access policy for each customer application. Use client-side encryption to encrypt customer files then share the KMS Key ID and the client-side master key to all customers in order to access the CMS**  is incorrect because the S3 bucket being used has only enabled Server Access Logging and not Versioning. In addition, it is also a security risk to share the KMS Key ID and the client-side master key with all customers.

The option that says: **Use Amazon EFS for object storage and enable data encryption in transit with TLS. Store unique customer managed keys in AWS KMS. Set up IAM roles and IAM access policies for EFS to specify separate encryption keys for each customer application. Utilize file locking and file versioning features in EFS to roll back changes to existing files stored in the CMS**  is incorrect because EFS is primarily used as a file system and not for object storage. Although EFS has file locking capabilities, it does not have file versioning features.

**References:**

[https://aws.amazon.com/workdocs/](https://aws.amazon.com/workdocs/)

[https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_constructing.html](https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_constructing.html)

[https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_downloading.html](https://docs.aws.amazon.com/workdocs/latest/developerguide/content_manager_downloading.html)

</details>
