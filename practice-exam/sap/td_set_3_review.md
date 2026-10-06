# TD Set 3 (timed) — Wrong Answer Review (33 questions)

Source: `TutorialsDojo_SAP_Timed_Mode_Set_3.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td_set_3_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q16](#q16) | ☐ | ☐ | ☐ |
| A | [Q20](#q20) | ☐ | ☐ | ☐ |
| A | [Q24](#q24) | ☐ | ☐ | ☐ |
| A | [Q26](#q26) | ☐ | ☐ | ☐ |
| A | [Q29](#q29) | ☐ | ☐ | ☐ |
| A | [Q30](#q30) | ☐ | ☐ | ☐ |
| A | [Q42](#q42) | ☐ | ☐ | ☐ |
| A | [Q63](#q63) | ☐ | ☐ | ☐ |
| A | [Q72](#q72) | ☐ | ☐ | ☐ |
| B | [Q13](#q13) | ☐ | ☐ | ☐ |
| B | [Q17](#q17) | ☐ | ☐ | ☐ |
| B | [Q28](#q28) | ☐ | ☐ | ☐ |
| B | [Q37](#q37) | ☐ | ☐ | ☐ |
| B | [Q45](#q45) | ☐ | ☐ | ☐ |
| B | [Q55](#q55) | ☐ | ☐ | ☐ |
| C | [Q48](#q48) | ☐ | ☐ | ☐ |
| C | [Q60](#q60) | ☐ | ☐ | ☐ |
| C | [Q61](#q61) | ☐ | ☐ | ☐ |
| C | [Q71](#q71) | ☐ | ☐ | ☐ |
| C | [Q75](#q75) | ☐ | ☐ | ☐ |
| D | [Q7](#q7) | ☐ | ☐ | ☐ |
| D | [Q10](#q10) | ☐ | ☐ | ☐ |
| D | [Q23](#q23) | ☐ | ☐ | ☐ |
| D | [Q50](#q50) | ☐ | ☐ | ☐ |
| E | [Q1](#q1) | ☐ | ☐ | ☐ |
| E | [Q14](#q14) | ☐ | ☐ | ☐ |
| E | [Q19](#q19) | ☐ | ☐ | ☐ |
| E | [Q32](#q32) | ☐ | ☐ | ☐ |
| E | [Q53](#q53) | ☐ | ☐ | ☐ |
| E | [Q57](#q57) | ☐ | ☐ | ☐ |
| F | [Q6](#q6) | ☐ | ☐ | ☐ |
| F | [Q8](#q8) | ☐ | ☐ | ☐ |
| F | [Q58](#q58) | ☐ | ☐ | ☐ |

---

# Group A — Overbuilt — the simplest/cheapest fix wins (9)

<a id="q16"></a>

## Q16

A company is hosting its three-tier web application on the us-east-1 region of AWS. The web and application tiers are stateless and both are running on their own fleet of On-Demand Amazon EC2 instances, each with its respective Auto Scaling group. The database tier is running on an Amazon Aurora database with about 40 TB of data. As part of the business continuity strategy of the company, the Solutions Architect must design a disaster recovery plan in case the primary region fails. The application requires an RTO of 30 minutes and the data tier requires an RPO of 5 minutes.

Which of the following options should the Solution Architect implement to achieve the company requirements in a cost-effective manner? (Select TWO.)

- **A.** Schedule a daily snapshot of the Amazon EC2 instances for the web and application tier. Copy the snapshot to the backup region. Restore the backups in case of a disaster in the primary region.
- **B.** For a quick recovery time, set up a hot-standby of web and application tier on the backup region. Redirect the traffic to the backup region in case of a disaster in the primary region.
- **C.** Configure an automated snapshot of the Amazon Aurora database every 5 minutes. Quickly restore the database on the backup region in case of a disaster in the primary region.
- **D.** Set up a cross-Region read replica of the Amazon Aurora database to the backup region. Promote this read replica as the master database in case of a disaster in the primary region.
- **E.** Use AWS Backup to create a backup job that will copy the EC2 EBS volumes and RDS data to an Amazon S3 bucket in another region. Restore the backups in case of a disaster in the primary region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** B, D

🔑 **Key words:** RTO 30 min, RPO 5 min, cost-effective, stateless web/app tiers

🪤 **Your trap:** 🔁 Hot standby is not cost-effective when RTO is 30 min — restoring EC2 snapshots fits

🧠 **Rule:** Match the DR tier to the RTO: 30 min → backup/restore for stateless tiers + cross-Region read replica for the DB

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
us-east-1 (Primary)                    Backup Region
┌──────────────────────┐               ┌──────────────────────┐
│ Web tier   (stateless)│   daily EBS   │                      │
│ App tier   (stateless)│ ──snapshot──► │ Restore khi có disaster│
├──────────────────────┤               ├──────────────────────┤
│ Aurora 40 TB           │──cross-Region │ Read Replica          │
│                        │  async replica│ → promote thành master│
└──────────────────────┘               └──────────────────────┘

Yêu cầu: RTO 30 phút (app) | RPO 5 phút (data) | CHI PHÍ THẤP
```

Đáp án đúng: **A + D**. Anh chọn đúng D (cross-Region read replica cho Aurora) nhưng chọn sai **B** (hot-standby) cho tầng web/app — đáp án đúng là **A** (daily EC2 snapshot + copy sang backup region).

⚠️ **Lỗi lặp lại** — đây là dạng bài "DR cost-effective theo RTO/RPO" mà anh đã từng vấp trước đó trong đợt ôn này: xu hướng chọn giải pháp nặng/luôn chạy (hot-standby) dù đề đã cho RTO đủ rộng để dùng backup/restore rẻ hơn.

#### Vì sao A đúng — daily snapshot cho tầng stateless

Web và app tier là **stateless** → không có dữ liệu quan trọng nằm trên instance. Vì vậy chỉ cần:
- Snapshot EBS hằng ngày của các EC2 instance này
- Copy snapshot sang backup region
- Khi có disaster: restore snapshot thành EC2 instance mới, đưa vào Auto Scaling group

RTO 30 phút là **thừa thời gian** để spin up EC2 mới từ snapshot — không cần trả tiền cho hạ tầng chạy sẵn 24/7.

#### Vì sao D đúng — cross-Region read replica cho Aurora

RPO 5 phút nghĩa là mất dữ liệu tối đa 5 phút được chấp nhận. Aurora cross-Region read replica nhận **replication bất đồng bộ (asynchronous)** liên tục từ primary, nên dữ liệu trên replica luôn gần như cập nhật. Khi primary region sập:
- Promote read replica thành master → không cần đợi restore snapshot 40 TB (có thể mất hàng giờ, vượt RTO 30 phút)

#### Vì sao B (lựa chọn của anh) sai

B dùng **hot-standby** cho web/app tier ở backup region — nghĩa là hạ tầng chạy sẵn liên tục ở DR region. Điểm mấu chốt: hot-standby cho RTO nhanh gần như tức thì, nhưng ở đây RTO đã là 30 phút — dư thừa so với mức cần. Chạy EC2/ALB song song 24/7 ở backup region tạo ra chi phí liên tục không cần thiết → **không cost-effective**, vi phạm đúng yêu cầu đề bài ("cost-effective manner").

#### Các lựa chọn sai còn lại

- **C** — snapshot Aurora mỗi 5 phút: Automated backup của RDS/Aurora chỉ chạy theo backup window hằng ngày, **không thể cấu hình chạy mỗi 5 phút**. Hơn nữa restore 40 TB có thể vượt quá 30 phút RTO.
- **E** — AWS Backup copy EBS + RDS sang S3: tần suất backup cao nhất của AWS Backup là **mỗi 12 giờ**, chỉ cho RPO tối đa 12 giờ — không đạt RPO 5 phút yêu cầu.

#### Bảng so sánh

| Tier | Giải pháp đúng | Vì sao |
|---|---|---|
| Web/App (stateless) | A. Daily EBS snapshot → copy region → restore | RTO 30' đủ để restore, rẻ hơn hot-standby |
| Aurora (data) | D. Cross-Region read replica → promote | Đạt RPO 5', nhanh hơn restore snapshot |
| ~~Web/App~~ | ~~B. Hot-standby~~ | Luôn chạy → tốn phí không cần thiết |
| ~~Aurora~~ | ~~C. Snapshot mỗi 5'~~ | Không khả thi — backup window hằng ngày |
| ~~Cả hai~~ | ~~E. AWS Backup~~ | Max RPO 12 giờ, không đạt 5 phút |

#### Lưu ý thực tế

- "Hot-standby" trong DR = hạ tầng **luôn chạy** ở DR region, dùng khi cần RTO cực thấp (gần 0). Nếu đề cho RTO vài chục phút, đáp án gần như luôn là backup/restore rẻ hơn.
- Aurora cross-Region read replica khác snapshot: replica luôn "sống" và đồng bộ liên tục, nên promote nhanh hơn nhiều so với restore từ snapshot.

#### Quy tắc nhớ cho thi

- **Thấy "stateless tier" + RTO vài chục phút** → **snapshot/backup + restore**, không cần hot-standby
- **Thấy RPO vài phút cho DB** → **cross-Region read replica**, không phải snapshot định kỳ
- **Thấy "cost-effective" + DR** → loại ngay phương án có hạ tầng chạy liên tục song song
- **AWS Backup max RPO ≈ 12 giờ** — không dùng khi đề yêu cầu RPO phút

### TD explanation

Amazon EC2 EBS volumes are the primary persistent storage option for Amazon EC2. You can use this block storage for structured data, such as databases, or unstructured data, such as files in a file system on a volume. With Amazon EBS, you can create point-in-time snapshots of volumes, which we store for you in Amazon S3. After you create a snapshot and it has finished copying to Amazon S3, you can copy it from one AWS Region to another, or within the same Region.
Snapshots are useful if you want to back up your data and logs across different geographical locations at regular intervals. In case of disaster, you can restore your applications using point-in-time backups stored in the secondary Region. This minimizes data loss and recovery time.
You can create cross-region read replicas for Amazon Aurora. This allows you to serve read traffic from your users in different geographic regions and increases your application’s responsiveness. This feature also provides you with improved disaster recovery capabilities in case of regional disruptions. You can seamlessly migrate your database from one region to another by creating a cross-region read replica and promoting it to be the new primary database.

You can create an Amazon Aurora MySQL DB cluster as a read replica in a different AWS Region than the source DB cluster. You can promote an Aurora MySQL read replica to a standalone DB cluster. When you promote an Aurora MySQL read replica, its DB instances are rebooted before they become available. Typically, you promote an Aurora MySQL read replica to a standalone DB cluster as a data recovery scheme if the source DB cluster fails.
When restoring Amazon Aurora snapshots, or point-in-time restore, the restoration may take several minutes to hours. Long restore times are caused by long-running transactions in the source database at the time the backup was taken.
The option that says: Schedule a daily snapshot of the Amazon EC2 instances for the web and application tier. Copy the snapshot to the backup region. Restore the backups in case of a disaster in the primary region is correct. The web and application tiers are stateless, meaning they don’t have any important data stored on them. Therefore, copying the daily snapshot of the EC2 instance to the backup region will suffice. The RTO of 30 minutes is ample time to spawn new EC2 instances on the backup region.
The option that says: Set up a cross-Region read replica of the Amazon Aurora database to the backup region. Promote this read-replica as the master database in case of a disaster in the primary region is correct. Given that the RPO for the data tier is 5 minutes, it is better to create a cross-Region read-replica on the backup region. The primary DB instance will asynchronously replicate the data to the Read Replica. So in the event that the primary DB failed, the Read Replica contains the updated data. You can also quickly promote this as the master DB instance in case of a disaster in the primary region. You don’t have to wait for a long database snapshot restore time too, which might exceed the 30-minute RTO requirement.
The option that says: For a quick recovery time, set up a hot-standby of web and application tier on the backup region. Redirect the traffic to the backup region in case of a disaster in the primary region is incorrect. Although this is possible, this is not the most cost-effective solution as it entails a significant number of resources that are continuously running. With an RTO of 30 minutes, you can quickly restore backups of the EC2 snapshots of the web and application tier instead of running a hot-standby environment. Take note that in Disaster Recovery, a "hot-standby" means that the application runs in the DR region. Because it's always running, you will incur a significant amount of cost.
The option that says: Configure an automated snapshot of the Amazon Aurora database every 5 minutes. Quickly restore the database on the backup region in case of a disaster in the primary region is incorrect. Restoring 40 TB of data may not be possible if you have an RTO requirement of 30 minutes. Depending on how busy the database was during the time the snapshot was taken, the restoration process may take longer than 30 minutes to complete. Moreover, automated backups only occur once every day during the defined backup window. You can't configure it to run every 5 minutes.
The option that says: Use AWS Backup to create a backup job that will copy the EC2 EBS volumes and RDS data to an Amazon S3 bucket in another region. Restore the backups in case of a disaster in the primary region is incorrect. This may be possible, but the restoration time from the RDS backup may take more time than the required 30 minutes of RTO. The highest backup frequency in AWS Backup is every 12 hours only and not every 5-minutes. Thus, it can only provide a maximum RPO of 12 hours. A better solution is to use a Read Replica with a replication latency of only about a few minutes, providing a higher RPO.

References:
https://aws.amazon.com/premiumsupport/knowledge-center/aurora-mysql-slow-snapshot-restore/
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html
https://aws.amazon.com/about-aws/whats-new/2016/06/amazon-aurora-now-supports-cross-region-replication/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html

Check out these Amazon EBS and Amazon RDS Cheat Sheets:
https://tutorialsdojo.com/amazon-ebs/
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q20"></a>

## Q20

An analytics company provides big data services to various clients worldwide. For performance-testing activities, a Big Data Analytics application is using an Elastic MapReduce cluster which will only be run once. The cluster is designed to ingest 20 TB of data with a total of 30 EC2 instances and is expected to run for about 48 hours.

Which of the following options is the most cost-effective architecture to implement for this scenario without sacrificing data integrity?

- **A.** Use a combination of On-Demand instance and Spot Instance types for both the master and core nodes. Use On-Demand EC2 instances for the task nodes.
- **B.** Use On-Demand instances for the core nodes. Use Reserved EC2 instances for the master node and Spot EC2 instances for the task nodes.
- **C.** For both the master and core nodes, use On-Demand EC2 instances. For the task nodes, use Spot EC2 instances.
- **D.** For both the master and core nodes, use Reserved EC2 instances. For the task nodes, use Spot EC2 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** run once, 48 hours, without sacrificing data integrity

🪤 **Your trap:** Reserved Instances need a 1–3 year term — wrong for a one-off job

🧠 **Rule:** One-off EMR: On-Demand master + core (hold data), Spot only for task nodes

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EMR Cluster — chạy MỘT LẦN DUY NHẤT (one-off)
30 EC2 instances | 20 TB data | ~48 giờ

┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│ Master node  │   │ Core node(s) │   │ Task node(s) │
│ (coordinate) │   │ (lưu HDFS)   │   │ (chỉ compute)│
└─────────────┘   └─────────────┘   └─────────────┘
   On-Demand?         On-Demand?        Spot?
```

Yêu cầu: **most cost-effective**, **không hy sinh data integrity**. Đáp án đúng: **C** (On-Demand cho master + core, Spot cho task). Anh chọn **D** (Reserved cho master + core, Spot cho task).

⚠️ **Lỗi lặp lại** — đây là cùng một concept bị sai **2 lần trong đợt thi này** (xem Q29): cứ thấy "cost-effective" + chạy dài giờ là phản xạ chọn Reserved Instance, trong khi Reserved yêu cầu term tối thiểu 1 năm.

#### Vì sao C đúng

- **Master node**: tránh Spot vì Spot bị terminate thì **toàn bộ cluster chết**. On-Demand là lựa chọn an toàn, không cần ký cam kết dài hạn.
- **Core node**: lưu dữ liệu trên HDFS. Nếu Core chạy Spot và bị thu hồi, dữ liệu trên HDFS instance đó **mất** → vi phạm "data integrity". Nên core cũng phải On-Demand.
- **Task node**: không lưu dữ liệu trong HDFS, chỉ chạy task tính toán. Nếu bị Spot terminate, job có thể retry ở node khác mà không mất dữ liệu → an toàn để dùng **Spot**, tiết kiệm chi phí vì Spot rẻ hơn On-Demand.

Vì cluster chỉ chạy **một lần, 48 giờ**, không có lý do gì phải mua Reserved Instance.

#### Vì sao D (lựa chọn của anh) sai

Reserved Instance yêu cầu **cam kết tối thiểu 1 năm** (reserve capacity dài hạn). Cluster này chỉ chạy đúng 48 giờ rồi thôi — mua Reserved cho một job 48 giờ là lãng phí toàn bộ phần thời gian còn lại của term 1 năm, hoàn toàn ngược với "cost-effective".

#### Các lựa chọn sai còn lại

- **A** — On-Demand + Spot hỗn hợp cho master/core, nhưng On-Demand cho task node: sai vì **task node nên dùng Spot** để tiết kiệm; dùng On-Demand cho task là không tối ưu chi phí.
- **B** — Reserved cho master, On-Demand cho core, Spot cho task: vẫn mắc lỗi Reserved cho một job one-off.

#### Bảng so sánh

| Node | Vai trò | Lựa chọn đúng | Vì sao |
|---|---|---|---|
| Master | Điều phối cluster | On-Demand | Spot bị thu hồi → chết cả cluster |
| Core | Lưu HDFS | On-Demand | Spot bị thu hồi → mất data integrity |
| Task | Chỉ compute, không lưu data | Spot | Rẻ hơn, mất node không mất data |
| — | Reserved Instance | ❌ không dùng | Cam kết ≥ 1 năm, job chỉ 48 giờ |

#### Lưu ý thực tế

- Amazon EMR tự có cơ chế: application master process chỉ chạy trên **core node**, không chạy trên task node — nên mất task node (Spot) không làm job fail hoàn toàn.
- Reserved Instance trên EMR chỉ có lợi khi cluster chạy liên tục dài hạn (ví dụ cluster thường trực nhiều tháng/năm).

#### Quy tắc nhớ cho thi

- **Thấy "run once" / "one-time" + số giờ cụ thể (8h, 48h...)** → loại ngay Reserved Instance
- **EMR node pattern chuẩn**: Master = On-Demand, Core = On-Demand (vì giữ HDFS), Task = Spot
- **"Without sacrificing data integrity"** → không bao giờ đặt Spot vào node lưu dữ liệu (master/core)

### TD explanation

When you set up a cluster, you choose a purchasing option for EC2 instances. You can choose On-Demand Instances, Spot Instances, or both. With On-Demand Instances, you pay for compute capacity by the hour. Optionally, you can have these On-Demand Instances use Reserved Instance or Dedicated Instance purchasing options.
With Reserved Instances, you make a one-time payment for an instance to reserve capacity. Dedicated Instances are physically isolated at the host hardware level from instances that belong to other AWS accounts. After you purchase a Reserved Instance, if all of the following conditions are true, Amazon EMR uses the Reserved Instance when a cluster launches:
- An On-Demand Instance is specified in the cluster configuration that matches the Reserved Instance specification.
- The cluster is launched within the scope of the instance reservation (the Availability Zone or Region).
- The Reserved Instance capacity is still available.
Spot Instances in Amazon EMR provide an option for you to purchase Amazon EC2 instance capacity at a reduced cost as compared to On-Demand purchasing. The disadvantage of using Spot Instances is that instances may terminate unpredictably as prices fluctuate.

With the uniform instance group configuration, you can have up to a total of 48 task instance groups. The ability to add instance groups in this way allows you to mix EC2 instance types and pricing options, such as On-Demand Instances and Spot Instances. This gives you the flexibility to respond to workload requirements in a cost-effective way.
With the instance fleet configuration, the ability to mix instance types and purchasing options are built-in, so there is only one task instance fleet.
Because Spot Instances are often used to run task nodes, Amazon EMR has default functionality for scheduling YARN jobs so that running jobs do not fail when task nodes running on Spot Instances are terminated. Amazon EMR does this by allowing application master processes to run only on core nodes. The application master process controls running jobs and needs to stay alive for the life of the job.
On-Demand instances cost more than Spot instances, which is why it is better to use Spot Instances for the task nodes to save costs. However, using Spot Instances for the master and core nodes is not recommended since a Spot Instance can potentially become unavailable during the 48-hour process.
Hence, this option is the correct answer: For both the master and core nodes, use On-Demand EC2 instances. For the task nodes, use Spot EC2 instances.
Remember that in this scenario, the processing will only take 48 hours. That is why it is not suitable to use Reserved Instances since the minimum reservation for this instance purchasing option is 1 year.
Therefore, the following options are incorrect:
- Use On-Demand instances for the core nodes. Use Reserved EC2 instances for the master node and Spot EC2 instances for the task nodes.
- For both the master and core nodes, use Reserved EC2 instances. For the task nodes, use Spot EC2 instances.
The option that says: Use a combination of On-Demand instance and Spot Instance types for both the master and core nodes. Use On-Demand EC2 instances for the task nodes is incorrect because using On-Demand EC2 instances for the task nodes is not cost-efficient. A better setup is to use Spot Instances for the task nodes.

References:
https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf#page=11
https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-purchasing-options.html
https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html

Check out this Amazon EMR Cheat Sheet:
https://tutorialsdojo.com/amazon-emr/

</details>

<a id="q24"></a>

## Q24

A company runs an application in a fleet of Amazon EC2 instances in the us-east-2 region. A database server is hosted on the on-premises data center which complies with the BASE (Basically Available, Soft state, Eventual consistency) model rather than the ACID (Atomicity, Consistency, Isolation, Durability) consistency model. The on-premises network has a 10 GB AWS Direct Connect connection to the Amazon VPC in us-east-2. The application relies on this database for normal operations and must meet strict recovery point objectives. Whenever there are lots of database write requests, the application behavior becomes erratic.

Which of the following options should the solutions architect implement to improve the performance of the application in a cost-effective way?

- **A.** Create a Hadoop cluster using Amazon Elastic Map Reduce (Amazon EMR) and use the S3DistCp tool to synchronize data between the on-premises database and the Hadoop cluster.
- **B.** Create an Amazon SQS queue and develop a consumer process to flush the queue to the on-premises database server. Update the application to enable writing to the SQS queue.
- **C.** Create an Amazon RDS multi-AZ instance that will synchronize with the on-premises database server using Amazon EventBridge. Redirect the write operations of the application to the RDS endpoint via the Amazon Elastic Transcoder service.
- **D.** Update the application to write to an Amazon DynamoDB table. Feed the table to an Amazon EMR cluster and create a map function that will update the on-premises database for every table update.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** write spikes, erratic behavior, cost-effective, strict RPO

🪤 **Your trap:** DynamoDB with high WCU + EMR cluster = much more cost and overhead than a queue

🧠 **Rule:** Write bursts to a slow backend → SQS buffer + consumer that flushes to the DB

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 app (us-east-2) ──10GB Direct Connect──► On-prem DB (BASE model, eventual consistency)
                                               ↑
                                      write bursts → app erratic

Yêu cầu: cải thiện performance, cost-effective, strict RPO
```

Đáp án đúng: **B** (SQS queue + consumer flush vào on-prem DB). Anh chọn **D** (DynamoDB + EMR map function cập nhật on-prem DB).

#### Vì sao B đúng

Ứng dụng đang theo mô hình **BASE (eventual consistency)** — nghĩa là chấp nhận dữ liệu không cần nhất quán ngay lập tức. Điều này mở đường cho giải pháp đệm (buffer) ghi:

```
App ──write──► SQS queue ──consumer process──► On-prem DB
```

SQS tách rời (decouple) tốc độ ghi của app khỏi tốc độ xử lý của DB on-prem. Khi có spike ghi, message chỉ xếp hàng trong queue, consumer xử lý dần theo khả năng của DB — tránh app bị "erratic" vì DB quá tải. Đây cũng là giải pháp **rẻ nhất** trong 4 lựa chọn: chỉ thêm SQS + 1 consumer process, không cần đổi database engine hay dựng cluster mới.

#### Vì sao D (lựa chọn của anh) sai

D yêu cầu: app viết vào DynamoDB → feed vào EMR cluster → map function cập nhật on-prem DB cho **mỗi lần update**. Vấn đề:
- DynamoDB table cần **WCU cao** để chịu tải ghi tương tự → tốn tiền
- Thêm **EMR cluster** chạy liên tục để xử lý map function → tốn tiền và operational overhead lớn hơn nhiều so với một SQS queue đơn giản
- Về bản chất kỹ thuật vẫn khả thi, nhưng **không cost-effective** — đúng vào từ khóa đề bài yêu cầu.

#### Các lựa chọn sai còn lại

- **A** — EMR + S3DistCp: S3DistCp dùng để copy dữ liệu lớn từ S3 vào HDFS, **không phải** công cụ đồng bộ dữ liệu tới một database on-premises.
- **C** — RDS Multi-AZ đồng bộ qua EventBridge, ghi qua Elastic Transcoder: sai ở nhiều điểm — (1) ứng dụng dùng BASE model nên một DB SQL như RDS (ACID) có thể không tương thích với kiểu dữ liệu; (2) EventBridge không trực tiếp đồng bộ với DB on-prem; (3) Elastic Transcoder là dịch vụ **chuyển mã media**, không liên quan đến việc gửi write operations tới RDS endpoint.

#### Bảng so sánh

| Lựa chọn | Cơ chế | Chi phí/Ops | Vấn đề |
|---|---|---|---|
| **B. SQS + consumer** | Buffer ghi, flush dần vào DB | Thấp | — (đúng) |
| D. DynamoDB + EMR map | Ghi qua DynamoDB rồi đẩy sang on-prem qua EMR | Cao | WCU cao + EMR cluster tốn kém |
| A. EMR + S3DistCp | Sync dữ liệu S3↔HDFS | — | Sai mục đích công cụ |
| C. RDS + EventBridge + Elastic Transcoder | Đồng bộ RDS với on-prem | — | Sai service, không tương thích BASE |

#### Lưu ý thực tế

- SQS Standard queue cho phép message đến **nhiều lần và không theo thứ tự** — phù hợp vì ứng dụng đã chấp nhận eventual consistency (BASE), không cần đảm bảo order nghiêm ngặt.
- "Strict RPO" trong đề không mâu thuẫn với SQS: SQS lưu trữ bền (durable) message cho đến khi được consumer xử lý thành công, nên không mất dữ liệu ghi dù DB tạm thời quá tải.

#### Quy tắc nhớ cho thi

- **Thấy "BASE model" / "eventual consistency" + write spike vào backend chậm** → **SQS buffer + consumer**, không phải đổi hẳn sang NoSQL + big data pipeline
- **"Cost-effective" + đã có giải pháp đơn giản (queue)** → loại ngay phương án yêu cầu thêm cluster (EMR, Redshift…)
- **Elastic Transcoder** → chỉ dùng cho media, không liên quan database/replication

### TD explanation

Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Since the application relies on an eventual consistency model, there should be no problem on adding an SQS queue in front of the database.
Decoupling message queuing from the database improves database availability and enables greater message queue scalability. It also provides a more cost-effective use of the database, and mitigates backpressure created when database performance is constrained by message management.
You can use standard message queues in many scenarios, as long as your application can process messages that arrive more than once and out of order, for example:
- Decouple live user requests from intensive background work: Let users upload media while resizing or encoding it.
- Allocate tasks to multiple worker nodes: Process a high number of credit card validation requests.
- Batch messages for future processing: Schedule multiple entries to be added to a database.

Therefore, the correct answer is: Create an Amazon SQS queue and develop a consumer process to flush the queue to the on-premises database server. Update the application to enable writing to the SQS queue. Since the application follows the eventual consistency model, an SQS can be used to temporarily hold the write requests, while a worker process flushes the queue to the on-premises database.
The option that says: Create a Hadoop cluster using Amazon Elastic Map Reduce (Amazon EMR) and use the S3DistCp tool to synchronize data between the on-premises database and the Hadoop cluster is incorrect. S3DistCp tool is primarily used to copy large amounts of data from Amazon S3 into HDFS. It is not suitable for synchronizing data to an on-premises database.
The option that says: Create an Amazon RDS multi-AZ instance that will synchronize with the on-premises database server using Amazon EventBridge. Redirect the write operations of the application to the RDS endpoint via the Amazon Elastic Transcoder service is incorrect. The application is using the BASE consistency model so an SQL-based database, such as an Amazon RDS, may not be compatible with the data to be written by the application. Moreover, you cannot directly synchronize your on-premises database server using Amazon EventBridge. Amazon Elastic Transcoder is simply a media transcoding service in AWS; thus, it can't be used to send write operations to your Amazon RDS endpoint.
The option that says: Update the application to write to an Amazon DynamoDB table. Feed the table to an Amazon EMR cluster and create a map function that will update the on-premises database for every table update is incorrect. This may be possible but creating a DynamoDB table with a high WCU and an EMR cluster significantly increases operational costs compared to using an SQS queue.

References:
https://aws.amazon.com/blogs/architecture/modernized-database-queuing-using-amazon-sqs-and-aws-services/
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
https://aws.amazon.com/sqs/features/

Check out this Amazon SQS Cheat Sheet:
https://tutorialsdojo.com/amazon-sqs/

</details>

<a id="q26"></a>

## Q26

A tech company in the USA has sold millions of sensors that collect temperature information from different locations in a household. These sensors send data to the IoT application developed by the company which is hosted on the AWS cloud using the domain iot.tutorialsdojotest.com. The domain is registered using Amazon Route 53. The sensors use the MQTT protocol to connect to a custom MQTT broker which is hosted on a large Amazon EC2 instance. After processing the received IoT data, the application then sends the data to an Amazon DynamoDB table for storage.

In the past month, the MQTT broker crashed a few times because it was overloaded by the large amount of data being received. This outage caused sensor data to be lost. The management wants to improve the reliability of the IoT workflow to prevent this from happening again.

Which of the following options is the recommended solution to meet the company's requirements while being cost-effective?

- **A.** Create a new Data-ATS endpoint in AWS IoT Greengrass. Point the Route 53 DNS zone record to this new endpoint to allow IoT devices on the edge to send data using the MQTT protocol. Create an AWS IoT rule that will invoke a Lambda function to store the received data in the Amazon DynamoDB Table.
- **B.** Use AWS IoT Core with MQTT to create a new Data-ATS endpoint. Update the Route 53 DNS zone record to point to the new endpoint and allow the IoT devices to send data using the MQTT protocol. Create an AWS IoT rule to directly insert the data into the Amazon DynamoDB table.
- **C.** Create an Auto Scaling group of Amazon EC2 instances for the message broker. Put the Auto Scaling group behind a Network Load Balancer (NLB) since it supports TCP connection for the MQTT protocol. Update the Route 53 DNS zone record to point to the NLB with an Alias type record. Use Amazon EFS as shared storage for the Auto Scaling group to improve the durability of received data.
- **D.** Leverage AWS IoT Device Management to update the firmware of the IoT devices. Push a firmware update with a random timer on each device to prevent them from sending data all at once. Set up another Amazon EC2 instance for the MQTT broker in another US region. Create a grouping of devices from IoT Device Management to send the other groups' traffic to this new instance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** MQTT broker overloaded, sensor data lost, recommended

🪤 **Your trap:** Scaling your own broker (ASG + NLB + EFS) is DIY and costly

🧠 **Rule:** IoT devices over MQTT → AWS IoT Core endpoint + IoT rule straight to DynamoDB

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hàng triệu sensor (MQTT) ──► Custom MQTT broker (1 EC2 instance lớn) ──► xử lý ──► DynamoDB
                                      │
                             CRASH khi quá tải → MẤT DỮ LIỆU SENSOR
iot.tutorialsdojotest.com (Route 53)

Yêu cầu: cải thiện reliability, RECOMMENDED + cost-effective
```

Đáp án đúng: **B** (AWS IoT Core Data-ATS endpoint + IoT Rule insert thẳng vào DynamoDB). Anh chọn **C** (tự scale broker: ASG + NLB + EFS).

#### Vì sao B đúng

```
Sensors (MQTT) ──► AWS IoT Core (Data-ATS endpoint, managed)
                          │
                    AWS IoT Rule
                          │
                    insert thẳng ──► DynamoDB table
```

- **AWS IoT Core** là managed service chuyên xử lý kết nối từ hàng loạt thiết bị IoT, hỗ trợ sẵn **MQTT** mà **không cần provision hay quản lý server nào** — giải quyết tận gốc vấn đề "broker tự host bị quá tải".
- Cập nhật Route 53 DNS record trỏ **iot.tutorialsdojotest.com** sang Data-ATS endpoint mới của IoT Core — sensor tiếp tục dùng domain quen thuộc, kết nối qua MQTT như trước.
- **AWS IoT Rule** cho phép định nghĩa action (ví dụ insert vào DynamoDB) chạy trực tiếp khi có message đến — bỏ qua hoàn toàn tầng xử lý trung gian, giảm điểm lỗi.
- Vì là managed service w/ auto-scale theo lượng thiết bị, đây là lựa chọn **vừa đáng tin cậy vừa rẻ hơn** so với việc vận hành broker riêng.

#### Vì sao C (lựa chọn của anh) sai

C đề xuất tự xây dựng high-availability cho broker hiện tại: Auto Scaling group của EC2 (message broker) + Network Load Balancer (hỗ trợ TCP cho MQTT) + Amazon EFS làm shared storage để tăng độ bền dữ liệu. Về lý thuyết khả thi, nhưng:
- Chi phí **cao hơn** vì phải chạy nhiều EC2 instance, NLB, và EFS liên tục.
- Tăng **operational overhead** — vẫn phải tự quản lý, patch, scale broker MQTT tự viết, trong khi AWS IoT Core đã làm sẵn việc này ở tầng managed.
→ Đây là giải pháp "DIY broker" nặng hơn mức cần thiết khi đã có dịch vụ managed chuyên biệt.

#### Các lựa chọn sai còn lại

- **A** — Dùng AWS IoT Greengrass tạo Data-ATS endpoint: **sai bản chất** — IoT Greengrass là phần mềm chạy trên **edge device**, cần client software trên thiết bị, không cải thiện được hiệu năng của broker trên AWS. Đồng thời dùng Lambda để insert vào DynamoDB là thừa khi IoT Rule có thể insert trực tiếp.
- **D** — Cập nhật firmware để random delay gửi dữ liệu + dựng thêm 1 EC2 broker ở region khác + chia nhóm thiết bị gửi theo region: tốn thêm chi phí cho instance mới, **không đề cập cách xử lý Route 53 record**, và giải pháp **không dễ scale** khi có thêm thiết bị trong tương lai.

#### Bảng so sánh

| Lựa chọn | Hạ tầng | Managed? | Vấn đề |
|---|---|---|---|
| **B. IoT Core + IoT Rule** | Data-ATS endpoint | Có (fully managed) | — (đúng) |
| C. ASG + NLB + EFS (anh chọn) | Tự host broker, scale thủ công | Không | Tốn kém, nhiều ops overhead |
| A. IoT Greengrass | Edge-based | — | Sai mục đích, cần client trên device |
| D. Firmware update + broker region khác | Thủ công, phân vùng thiết bị | Không | Tốn kém, không scale tốt, thiếu chi tiết DNS |

#### Lưu ý thực tế

- Data-ATS endpoint của AWS IoT Core gắn với từng **AWS account + Region** cụ thể, dùng để gửi/nhận dữ liệu qua message broker, Device Shadow, và Rules Engine.
- AWS IoT Rule có thể trực tiếp insert vào DynamoDB, viết vào S3, publish SNS, hoặc invoke Lambda — chọn action trực tiếp nhất (insert DynamoDB) khi không cần xử lý thêm logic.

#### Quy tắc nhớ cho thi

- **Thấy "custom MQTT broker" bị quá tải/crash** → **AWS IoT Core** luôn là câu trả lời managed chuẩn, không phải tự scale broker
- **"Recommended" + "cost-effective"** → loại ngay phương án ASG/NLB/EFS tự dựng khi có managed service tương đương
- **IoT Rule → DynamoDB trực tiếp** được, không cần Lambda trung gian nếu chỉ là insert đơn giản

### TD explanation

AWS IoT Core is a managed cloud service that enables connected devices to securely interact with cloud applications and other devices. AWS IoT Core can support many devices and messages and process and route those messages to AWS IoT endpoints and other devices. With AWS IoT Core, your applications can interact with all your devices even when disconnected. AWS IoT Core services connect IoT devices to AWS IoT services and other AWS services. AWS IoT Core includes the device gateway and the message broker, which connect and process messages between your IoT devices and the cloud.
AWS IoT lets you select the most appropriate and up-to-date technologies for your solution. To help you manage and support your IoT devices in the field, AWS IoT Core supports these protocols:
-MQTT (Message Queuing and Telemetry Transport)
-MQTT over WSS (WebSockets Secure)
-HTTPS (Hypertext Transfer Protocol - Secure)
-LoRaWAN (Long Range Wide Area Network)
The AWS IoT Core message broker supports devices and clients that use MQTT and MQTT over WSS protocols to publish and subscribe to messages. It also supports devices and clients that use the HTTPS protocol to publish messages.

The AWS IoT Core - data plane endpoints are specific to each AWS account and AWS Region. The Data-ATS endpoint sends and receives data to and from the message broker, Device Shadow, and Rules Engine components of AWS IoT.
You configure AWS IoT rules to route data from your connected things. A rule includes one or more actions that AWS IoT performs when enacting the rule. For example, you can insert data into a DynamoDB table, write data to an Amazon S3 bucket, publish to an Amazon SNS topic, or invoke a Lambda function.
Therefore, the correct answer is: Use AWS IoT Core with MQTT to create a new Data-ATS endpoint. Update the Route 53 DNS zone record to point to the new endpoint and allow the IoT devices to send data using the MQTT protocol. Create an AWS IoT rule to directly insert the data into the Amazon DynamoDB table. AWS IoT Core supports several protocols, including MQTT without the need to provision or manage servers. It can receive the data from IoT devices, and with an IoT rule, you can create an action to insert data into an Amazon DynamoDB table.
The option that says: Create a new Data-ATS endpoint in AWS IoT Greengrass. Point the Route 53 DNS zone record to this new endpoint to allow IoT devices on the edge to send data using the MQTT protocol. Create an AWS IoT rule that will invoke a Lambda function to store the received data in the Amazon DynamoDB Table is incorrect. AWS IoT Greengrass needs a client software that brings intelligence to edge devices. This setup will not improve the data broker's performance on AWS.
The option that says: Create an Auto Scaling group of Amazon EC2 instances for the message broker. Put the Auto Scaling group behind a Network Load Balancer (NLB) since it supports TCP connection for the MQTT protocol. Update the Route 53 DNS zone record to point to the NLB with an Alias type record. Use Amazon EFS as shared storage for the Auto Scaling group to improve the durability of received data is incorrect. This option may be possible; however, it may cost more for using Amazon EFS, the NLB, and multiple EC2 instances. It also increases the operational overhead for managing the instances.
The option that says: Leverage AWS IoT Device Management to update the firmware of the IoT devices. Push a firmware update with a random timer on each device to prevent them from sending data all at once. Set up another Amazon EC2 instance for the MQTT broker in another US region. Create a grouping of devices from IoT Device Management to send the other groups' traffic to this new instance is incorrect. This option may be possible; however, creating another instance in another US region will cost more. It does not mention how to handle the Route 53 record. Additionally, this solution is not easily scalable if more devices will be added in the future.

References:
https://docs.aws.amazon.com/general/latest/gr/iot-core.html
https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html
https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html

</details>

<a id="q29"></a>

## Q29

The European Organization for Nuclear Research, also known as CERN, is a research organization that operates the largest particle accelerator in the world and generates terabytes of experimental data every day. A group of data scientists is planning to use an Elastic MapReduce cluster for their data analysis, which will only be run once. The cluster is designed to ingest 300 TB of data with a total of 200 EC2 instances and is expected to run for about 8 hours. The resulting data set must be stored temporarily until it is permanently stored in their AWS Redshift database.

Which of the following options is the best and most cost-effective solution to satisfy the above requirements?

- **A.** Use On-Demand EC2 instances for both the master and core nodes and use Spot EC2 instances for the task nodes.
- **B.** Use Reserved EC2 instances for both the master and core nodes and use Spot EC2 instances for the task nodes.
- **C.** Use a combination of On-Demand instance and Spot instance types for both the master and core nodes. Use Spot EC2 instances for the task nodes.
- **D.** Use Reserved EC2 instances for the master node; On-Demand instances for the core nodes; and use Spot EC2 instances for the task nodes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** run only once, 8 hours, most cost-effective

🪤 **Your trap:** Same trap as Q20 in this test — Reserved for a one-off 8-hour job

🧠 **Rule:** One-off EMR: On-Demand master/core + Spot task nodes; never Reserved for short jobs

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EMR Cluster của CERN — chạy MỘT LẦN DUY NHẤT (one-off)
200 EC2 instances | 300 TB data | ~8 giờ
→ Kết quả lưu tạm rồi đẩy vào Redshift

┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│ Master node  │   │ Core node(s) │   │ Task node(s) │
└─────────────┘   └─────────────┘   └─────────────┘
```

Yêu cầu: **best and most cost-effective**. Đáp án đúng: **A** (On-Demand cho master + core, Spot cho task). Anh chọn **B** (Reserved cho master + core, Spot cho task).

⚠️ **Lỗi lặp lại** — Đây là **chính xác cùng concept với Q20** trong đợt thi này: EMR cluster chạy one-off → phải dùng On-Demand cho master/core, KHÔNG dùng Reserved Instance. Hai câu khác số liệu (20 TB/48h vs 300 TB/8h) nhưng cùng một cái trap: thấy chữ "cost-effective" là phản xạ nhảy vào Reserved.

#### Vì sao A đúng

- **Master node**: không đặt Spot — nếu bị terminate, **toàn bộ cluster sập**. Dùng On-Demand vì job chỉ chạy 8 giờ, không đáng để mua Reserved.
- **Core node**: lưu dữ liệu trên HDFS; nếu dùng Spot và bị thu hồi khi đang xử lý 300 TB thì mất dữ liệu đang ghi trên HDFS volume → rủi ro quá lớn với tập dữ liệu khoa học. Dùng On-Demand.
- **Task node**: không giữ dữ liệu HDFS, chỉ chạy compute phụ → dùng **Spot** để giảm chi phí, mất node này không ảnh hưởng đến tính toàn vẹn dữ liệu.

Vì job chỉ chạy **8 giờ, một lần duy nhất**, Reserved Instance (cam kết ≥ 1 năm) hoàn toàn không phù hợp — tiền trả cho Reserved sẽ lãng phí gần hết thời hạn cam kết.

#### Vì sao B (lựa chọn của anh) sai

Giống lỗi ở Q20: Reserved Instance đòi cam kết dài hạn (tối thiểu 1 năm), trong khi đây là dự án one-time 8 giờ. "Cost-effective" ở đây nghĩa là **trả đúng cho thời gian sử dụng** — không phải trả trước cho cả năm để chỉ dùng 8 giờ.

#### Các lựa chọn sai còn lại

- **C** — On-Demand + Spot hỗn hợp cho cả master và core, Spot cho task: sai vì đặt Spot vào core node (lưu HDFS) với khối lượng dữ liệu lớn (300 TB) có thể gây **mất dữ liệu hoặc gián đoạn xử lý** khi Spot bị thu hồi.
- **D** — Reserved cho master, On-Demand cho core, Spot cho task: vẫn mắc lỗi Reserved cho job one-off (dù chỉ áp cho master).

#### Bảng so sánh

| Node | Lựa chọn đúng | Vì sao |
|---|---|---|
| Master | On-Demand | Spot mất → sập cả cluster; job ngắn nên không cần Reserved |
| Core | On-Demand | Giữ HDFS; Spot mất → mất dữ liệu 300 TB đang xử lý |
| Task | Spot | Không giữ dữ liệu, mất node không ảnh hưởng integrity |
| Reserved IC | ❌ | Cam kết ≥ 1 năm, job one-off 8 giờ |

#### Lưu ý thực tế

- Số lượng instance lớn (200 instance) hay dữ liệu lớn (300 TB) **không** làm đổi logic chọn purchasing option — logic vẫn dựa trên: node có giữ data không (core/master) và job có phải one-off không, chứ không phải quy mô cluster.
- Khi dữ liệu càng lớn/nhạy cảm (ví dụ dữ liệu thí nghiệm khoa học CERN), việc giữ core node ổn định (On-Demand) càng quan trọng để tránh phải chạy lại toàn bộ job.

#### Quy tắc nhớ cho thi

- **Thấy "run once"/"one-time" bất kể số liệu to hay nhỏ** → luôn loại Reserved Instance
- **EMR node pattern chuẩn, học thuộc**: Master = On-Demand, Core = On-Demand, Task = Spot
- **Đây là lần 2 gặp đúng pattern này trong một bài thi** → khi thấy "EMR" + "run once/only once" trong đề, lập tức áp quy tắc trên, không suy diễn thêm

### TD explanation

In this scenario, the scientists are doing a one-time processing of their data in 8 hours. Hence, a Reserved instance is not a suitable type to use as this project is not for the long term.
Amazon EMR provides a managed Hadoop framework that makes it easy, fast, and cost-effective to process vast amounts of data using EC2 instances. When using Amazon EMR, you don’t need to worry about installing, upgrading, and maintaining Spark software (or any other tool from the Hadoop framework). You also don’t need to worry about installing and maintaining underlying hardware or operating systems. Instead, you can focus on your business applications and use Amazon EMR to remove the undifferentiated heavy lifting.
The central component of Amazon EMR is the cluster. A cluster is a collection of Amazon Elastic Compute Cloud (Amazon EC2) instances. Each instance in the cluster is called a node. Each node has a role within the cluster, referred to as the node type. Amazon EMR also installs different software components on each node type, giving each node a role in a distributed application like Apache Hadoop.
The node types in Amazon EMR are as follows:

Master node: A node that manages the cluster by running software components to coordinate the distribution of data and tasks among other nodes for processing. The master node tracks the status of tasks and monitors the health of the cluster. Every cluster has a master node, and it's possible to create a single-node cluster with only the master node.
Core node: A node with software components that run tasks and store data in the Hadoop Distributed File System (HDFS) on your cluster. Multi-node clusters have at least one core node.
Task node: A node with software components that only runs tasks and does not store data in HDFS. Task nodes are optional.
For optimizing costs and performance in choosing the instance types:

Master node: Unless your cluster is very short-lived and the runs are cost-driven, avoid running your Master node on a Spot Instance. We suggest this because a Spot interruption on the Master node terminates the entire cluster. Alternatively to On-Demand, you can set up the Master node on a Spot Block. You do so by setting the defined duration of the node and failing over to On-Demand if the Spot Block capacity is unavailable.
Core nodes: Avoid using Spot Instances for Core nodes if the jobs on the cluster use HDFS. That prevents a situation where Spot interruptions cause data loss for data that was written to the HDFS volumes on the instances.
Task nodes: Use Spot Instances for your task nodes by selecting up to five instance types that match your hardware requirement. Amazon EMR fulfills the most suitable capacity by price and capacity availability.

Therefore, the correct answer is: Use On-Demand EC2 instances for both the master and core nodes and use Spot EC2 instances for the task nodes.
The option that says: Use a combination of On-Demand instance and Spot instance types for both the master and core nodes. Use Spot EC2 instances for the task nodes is incorrect. It is not recommended to use a Spot instance for the Master node. Also, if dealing with a large amount of data shared on the cluster, you don't want to use spot instances for the Core nodes as it may cause data loss or interruption on your processing.
The option that says: Use Reserved EC2 instances for both the master and core nodes and use Spot EC2 instances for the task nodes is incorrect. The scenario is not a long-term project so a Reserved instance is not a suitable type to use in this case.

The option that says: Use Reserved EC2 instances for the master node; On-Demand instances for the core nodes; and use Spot EC2 instances for the task nodes is incorrect. The scenario is not a long-term project so a Reserved instance is not a suitable type to use in this case.

References:
https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html
https://aws.amazon.com/blogs/big-data/best-practices-for-running-apache-spark-applications-using-amazon-ec2-spot-instances-with-amazon-emr/
https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-fleet.html#emr-instance-fleet-allocation-strategy

Check out this Amazon EMR Cheat Sheet:
https://tutorialsdojo.com/amazon-emr/

</details>

<a id="q30"></a>

## Q30

A business news portal is visited by thousands of readers each day to check on the latest hot topics in the world of business and technology. The news portal runs on a fleet of Spot Amazon EC2 instances behind an Application Load Balancer (ALB). Readers can also submit comments in every article. Currently, the system's database is running on an on-premises data center, and the CTO is concerned that the content delivery time is not meeting company objectives. The portal's page load time is of utmost importance for the company to maintain its daily visitors.

Which of the following options would allow the solutions architect to quickly and cost-effectively modify the current infrastructure to reduce latency for customers?

- **A.** Migrate your database on-premises to Amazon Aurora using the AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (SCT). Create Aurora Replicas across Availability Zones and reconfigure the web servers to query from the Aurora database instead.
- **B.** Replace the on-premises database of the news portal with a fast, scalable full-text search engine using Amazon OpenSearch Service by setting up an ELK stack (Elasticsearch, Logstash, and Kibana). Use an Amazon CloudFront web distribution to speed up the delivery of data to your users across the globe.
- **C.** Add an in-memory datastore using Amazon ElastiCache for Redis to reduce the burden on the database. Enable Redis replication to scale database reads and to have highly available clusters.
- **D.** Create an Amazon CloudFront web distribution to speed up the delivery of data to their readers around the globe. Migrate the entire portal to an Amazon S3 bucket and then enable static web hosting. Set the S3 bucket as the origin of your CloudFront distribution.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** quickly and cost-effectively, reduce latency, database on-premises

🪤 **Your trap:** Migrating the DB to Aurora is slow and may not even be compatible — not 'quick'

🧠 **Rule:** 'Quick + cheap + reduce read latency' → add ElastiCache in front of the DB

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Readers ──► ALB ──► Spot EC2 fleet (news portal, dynamic — có comment)
                           │
                           ▼
                  On-premises database  ← latency cao, page load chậm

Yêu cầu: "quickly AND cost-effectively" giảm latency, giữ nguyên hạ tầng tối đa
```

Đáp án đúng: **C** (thêm ElastiCache for Redis trước DB). Anh chọn **A** (migrate database sang Aurora qua DMS/SCT).

⚠️ **Lỗi lặp lại** — liên quan đến một lỗi trước đó trong đợt ôn (RDS read scaling → ElastiCache): phản xạ "muốn giảm tải đọc DB thì nâng cấp/migrate hẳn database" trong khi đề yêu cầu **nhanh và rẻ**, và câu trả lời chuẩn luôn là thêm **cache layer** trước, không phải đổi engine DB.

#### Vì sao C đúng

Thêm **Amazon ElastiCache for Redis** ngay trước database on-premises:

```
Web/App servers ──► ElastiCache (Redis) ──cache miss──► On-prem DB
                         │
                    cache hit: trả dữ liệu
                    submillisecond latency
```

- Truy vấn cache nhanh hơn và rẻ hơn truy vấn DB nhiều lần cho cùng dữ liệu — trả giá cho query một lần, sau đó lấy lại từ cache nhiều lần.
- Vì cache nằm trong VPC cùng web/app server, khoảng cách vật lý tới data center on-prem **không còn quan trọng** với phần lớn request (những request cache-hit).
- Enable **Redis replication** giúp scale thêm cho các read request và tăng tính sẵn sàng (high availability) của cluster cache.
- Đây là thay đổi **nhỏ, nhanh triển khai**, không đụng vào kiến trúc database hiện tại → đúng yêu cầu "quickly and cost-effectively".

#### Vì sao A (lựa chọn của anh) sai

A đề xuất dùng AWS DMS + SCT để migrate toàn bộ database on-prem sang Amazon Aurora, tạo Aurora Replica across AZ. Vấn đề:
- Việc migrate database **không hề nhanh** — cần schema conversion, kiểm thử tương thích, cutover cẩn thận.
- Không có gì đảm bảo database engine hiện tại **tương thích** với Aurora.
- Chi phí hoạt động hàng ngày cho lượng request lớn cũng có thể tăng.
→ Đi ngược yêu cầu "quickly and cost-effectively" ngay từ đầu, dù về lâu dài có thể cải thiện hiệu năng.

#### Các lựa chọn sai còn lại

- **B** — Thay thế database on-prem bằng Amazon OpenSearch Service (ELK stack) + CloudFront: OpenSearch là công cụ cho full-text search/log analytics/operational intelligence, **không phải database chính**. Có thể bổ sung làm lớp phụ, nhưng không thay thế hoàn toàn được vai trò DB.
- **D** — CloudFront + migrate toàn bộ portal sang S3 static hosting: portal có phần **dynamic** (người đọc submit comment), S3 chỉ host **static website** → không phù hợp, dù có CloudFront.

#### Bảng so sánh

| Lựa chọn | Thay đổi | Nhanh? | Rẻ? | Vấn đề |
|---|---|---|---|---|
| **C. ElastiCache for Redis** | Thêm cache layer | Có | Có | — (đúng) |
| A. Migrate sang Aurora qua DMS | Đổi hẳn DB engine | Không | Không chắc | Migrate lâu, không đảm bảo compatible |
| B. OpenSearch + CloudFront | Thay DB bằng search engine | — | — | OpenSearch không phải DB chính |
| D. S3 static + CloudFront | Chuyển hẳn sang static site | — | — | Portal là dynamic (có comment) |

#### Lưu ý thực tế

- ElastiCache có thể đạt tốc độ phục vụ **hơn 20 triệu request/giây** — đủ đáp ứng site có lượng độc giả lớn mà không cần đổi database.
- "Quickly" trong đề luôn là tín hiệu loại các phương án "migrate database" hay "chuyển đổi toàn bộ kiến trúc" — những việc này tốn thời gian lập kế hoạch, kiểm thử, cutover.

#### Quy tắc nhớ cho thi

- **Thấy "quickly and cost-effectively" + giảm latency đọc DB** → **ElastiCache**, không phải migrate/nâng cấp DB engine
- **Thấy "dynamic content" (comment, form submit…)** → loại ngay phương án chuyển sang S3 static hosting
- **OpenSearch/ELK** → vai trò search/log analytics, không thay thế được database chính

### TD explanation

The success of the website and business is significantly affected by the speed at which you deliver content. Even the most optimized database query or remote API call is going to be noticeably slower than retrieving a flat key from an in-memory cache.
The primary purpose of an in-memory key-value store is to provide ultrafast (submillisecond latency) and inexpensive access to copies of data. Most data stores have areas of data that are frequently accessed but seldom updated. Additionally, querying a database is always slower and more expensive than locating a key in a key-value pair cache. By caching such query results, you pay the price of the query once and then are able to quickly retrieve the data multiple times without having to re-execute the query.

With the cache inside the VPC along with the web servers and application servers, the application doesn’t have to constantly go from AWS to the local data center. This change makes the physical distance between servers irrelevant. The new architecture should greatly improve the customer experience.

Therefore, the correct answer is: Add an in-memory datastore using Amazon ElastiCache for Redis to reduce the burden on the database. Enable Redis replication to scale database reads and to have highly available clusters. The main issue in this problem involves latency to the backend database. This solution dramatically reduces data retrieval latency. It also scales request volume considerably, because Amazon ElastiCache can deliver extremely high request rates, measured at over 20 million per second.
The option that says: Migrate your database on-premises to Amazon Aurora using the AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (SCT). Create Aurora Replicas across Availability Zones and reconfigure the web servers to query from the Aurora database instead is incorrect. There is no guarantee that the database engine currently being used by the news portal is supported by Amazon Aurora. It is also important to take note that the question asks for a quick and cost-effective solution. Migrating the database may typically take a long amount of time, and the number of requests being sent each day can rack up costs.
The option that says: Replace the on-premises database of the news portal with a fast, scalable full-text search engine using Amazon OpenSearch Service by setting up an ELK stack (Elasticsearch, Logstash, and Kibana). Use an Amazon CloudFront web distribution to speed up the delivery of data to your users across the globe is incorrect. OpenSearch is primarily used for log analytics, full-text search, security intelligence, business analytics, and operational intelligence use cases but not as a full-fledged database. A search engine could possibly be beneficial to the news portal as an additional layer but not as its sole data source. This solution might provide some advantages when they are both integrated together.
The option that says: Create an Amazon CloudFront web distribution to speed up the delivery of data to their readers around the globe. Migrate the entire portal to an Amazon S3 bucket and then enable static web hosting. Set the S3 bucket as the origin of your CloudFront distribution is incorrect. It is stated in the scenario that the readers can also submit their comments in every article, which means that the news portal is a dynamic website and not static. Hence, using S3 is not suitable for this scenario which is why this option is incorrect, even though it mentions the use of CloudFront web distribution.

References:
 https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/elasticache-use-cases.html
 https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.Redis-RedisCluster.html

Check out this Amazon ElastiCache Cheat Sheet:
https://tutorialsdojo.com/amazon-elasticache/

</details>

<a id="q42"></a>

## Q42

A company has a gaming store platform hosted in its on-premises data center for a whole variety of digital games. The application just experienced downtime last week due to a large burst in web traffic caused by a year-end sale on almost all of the games. Due to the success of the previous promotion, the CEO has planned to do the same in a few weeks, which will drive similar unpredictable bursts in web traffic. The solutions architects are looking to find ways to quickly improve the infrastructure's ability to handle unexpected increases in traffic. The web application is currently made up of a 2-tier web tier which consists of a load balancer and several web app servers, as well as a database tier that hosts an Oracle database.

Which of the following infrastructure changes should the team implement to avoid any further incidences of downtime considering that the new announcement will be done in a few weeks?

- **A.** Create an AMI that can be used to launch new EC2 web servers. Then create an Auto Scaling group which will use the AMI to scale the web tier. Finally, place an Application Load Balancer to distribute traffic between your on-premises servers and servers running in AWS.
- **B.** Migrate your environment to AWS by using AWS VM Import to quickly convert your web server into an AMI. Then set up an Auto Scaling group that uses the imported AMI. Also, create an RDS read replica and migrate the Oracle database to an RDS instance through replication.
- **C.** Set up an Amazon S3 bucket for website hosting. Migrate your DNS to Route 53 using zone import, and use DNS failover to failover to the hosted website in S3.
- **D.** Set up a CloudFront distribution to cache objects from a custom origin to offload traffic from your on-premises environment. Customize your object cache behavior, and choose a time-to-live that will determine how long objects will reside in the cache.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** in a few weeks, quickly improve, unpredictable bursts

🪤 **Your trap:** Full migration to AWS (VM Import + RDS) takes too long for a few weeks

🧠 **Rule:** Short deadline + traffic bursts on on-prem site → CloudFront with a custom origin to offload

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises data center
┌────────────────────────┐
│ Load Balancer           │
│ Web/App servers (2-tier)│
│ Oracle database          │
└────────────────────────┘
        ▲
        │ traffic burst sắp tới (vài TUẦN nữa) — y hệt lần trước gây downtime
        │
Yêu cầu: cải thiện khả năng chịu burst, TRIỂN KHAI NHANH (trong vài tuần)
```

Đáp án đúng: **D** (CloudFront với custom origin trỏ về on-prem). Anh chọn **B** (migrate toàn bộ sang AWS bằng VM Import + RDS read replica).

#### Vì sao D đúng

```
Readers ──► CloudFront (edge cache) ──origin──► Load balancer on-prem
                  │
          Cache hit: trả từ edge, KHÔNG chạm vào on-prem
```

- CloudFront chỉ cần đổi **origin** của distribution về load balancer on-prem hiện tại (gọi là "custom origin") — **không cần thay đổi kiến trúc hiện có**.
- Khi có burst traffic bất ngờ, phần lớn request được edge location của CloudFront trả lời từ cache (theo TTL cấu hình) → giảm tải trực tiếp lên hạ tầng on-prem.
- Đây là thay đổi **duy nhất cần làm** để tăng khả năng chịu tải trong thời gian ngắn còn lại trước đợt sale — khớp chính xác yêu cầu "trong vài tuần" và "quickly improve".

#### Vì sao B (lựa chọn của anh) sai

B đề xuất: dùng AWS VM Import để convert web server thành AMI, tạo Auto Scaling group, đồng thời tạo RDS read replica và **migrate Oracle database sang RDS** qua replication. Đây là một cuộc **di dời (migration) toàn bộ hạ tầng** sang AWS:
- Việc migrate database Oracle, kiểm thử tương thích, cutover **tốn thời gian hơn nhiều** so với vài tuần còn lại.
- So với việc chỉ cấu hình CloudFront (vài giờ/ngày), đây là phương án "nặng" không đáp ứng kịp deadline.
→ Vi phạm thẳng yêu cầu "quickly" của đề, dù về bản chất kỹ thuật là hướng đi hợp lý cho lâu dài.

#### Các lựa chọn sai còn lại

- **A** — Tạo AMI + Auto Scaling group tại AWS, đặt ALB phân phối traffic giữa on-prem và AWS: **ELB không thể load balance tới instance on-premises** nếu VPC chưa kết nối qua Direct Connect hoặc VPN — đề không nói có kết nối này.
- **C** — Host website trên S3 + Route 53 DNS failover: S3 **không host được dynamic website**; đây là gaming store platform cần xử lý logic động, không phù hợp với static hosting.

#### Bảng so sánh

| Lựa chọn | Thời gian triển khai | Thay đổi kiến trúc | Vấn đề |
|---|---|---|---|
| **D. CloudFront custom origin** | Nhanh (vài giờ–ngày) | Tối thiểu | — (đúng) |
| B. VM Import + RDS migration | Chậm (migration toàn bộ) | Lớn | Không kịp deadline vài tuần |
| A. ASG + ALB (AWS + on-prem) | — | — | ALB không load-balance tới on-prem nếu thiếu VPN/DX |
| C. S3 static + Route 53 failover | — | — | Không host được dynamic site |

#### Lưu ý thực tế

- CloudFront còn tích hợp sẵn **AWS Shield** cho DDoS mitigation — một lợi ích phụ khi traffic burst có thể trùng với traffic bất thường/tấn công.
- "Custom origin" trong CloudFront cho phép origin là bất kỳ HTTP server, không bắt buộc phải là S3 hay AWS resource — phù hợp để trỏ về load balancer on-prem hiện có.

#### Quy tắc nhớ cho thi

- **Thấy deadline ngắn ("in a few weeks") + traffic burst không đoán trước** → **CloudFront với custom origin**, không phải full migration sang AWS
- **"Minimal change" / thời gian gấp** → loại ngay các phương án có chữ "migrate database" hay "convert toàn bộ VM"
- **ALB/ELB chỉ load-balance tới on-prem nếu có Direct Connect/VPN** — không có thông tin này trong đề thì coi như không khả thi

### TD explanation

Amazon CloudFront is a global content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to your viewers with low latency and high transfer speeds. CloudFront is integrated with AWS – including physical locations that are directly connected to the AWS global infrastructure, as well as software that works seamlessly with services including AWS Shield for DDoS mitigation, Amazon S3, Elastic Load Balancing or Amazon EC2 as origins for your applications, and Lambda@Edge to run custom code close to your viewers. In this scenario, the major points of consideration are: your application may get unpredictable bursts of traffic, you need to improve the current infrastructure in the shortest period possible, and your web servers that are on-premises.
CloudFront caches content at edge locations for a period of time that you specify. If a visitor requests content that has been cached for longer than the expiration date, CloudFront checks the origin server to see if a newer version of the content is available. If a newer version is available, CloudFront copies the new version to the edge location. Changes that you make to the original content are replicated to edge locations as visitors request the content.
Since the time period at hand is short, instead of migrating the app to AWS, you need to consider different ways where the performance would improve without doing much modification to the existing infrastructure.

Therefore, the correct answer is: Set up a CloudFront distribution to cache objects from a custom origin to offload traffic from your on-premises environment. Customize your object cache behavior, and choose a time-to-live that will determine how long objects will reside in the cache. CloudFront is a highly scalable, highly available content delivery service, which can perform excellently even in case of sudden unpredictable burst of traffic. Plus, the only change you need to make is the on-premises load balancer as the custom origin of the CloudFront distribution.
The option that says: Create an AMI that can be used to launch new EC2 web servers. Then create an Auto Scaling group which will use the AMI to scale the web tier. Finally, place an Application Load Balancer to distribute traffic between your on-premises servers and servers running in AWS is incorrect. ELB cannot do load balancing to your on-premises instances if it is not connected to your VPC either through a DirectConnect connection or a VPN.
The option that says: Migrate your environment to AWS by using AWS VM Import to quickly convert your web server into an AMI. Then set up an Auto Scaling group that uses the imported AMI. Also, create an RDS read replica and migrate the Oracle database to an RDS instance through replication is incorrect. You are supposed to improve the current situation at the shortest time possible. Migrating to AWS would be more time consuming than simply setting up the CloudFront distribution.
The option that says: Set up an Amazon S3 bucket for website hosting. Migrate your DNS to Route 53 using zone import, and use DNS failover to failover to the hosted website in S3 is incorrect. You cannot host dynamic websites on S3 bucket. Also, this option provides insufficient infrastructure set up options.

References:
https://aws.amazon.com/cloudfront
https://aws.amazon.com/blogs/networking-and-content-delivery/improve-your-website-performance-with-amazon-cloudfront/
https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q63"></a>

## Q63

A leading telecommunications company is moving all of its mission-critical, multi-tier applications to AWS. At present, its architecture is composed of desktop client applications and several servers that are all located in its on-premises data center. The application-tier is using a MySQL database that is hosted on a single VM while both the presentation and business logic layers are distributed across multiple VMs. There has been a lot of reports that its users, who access the applications remotely, are experiencing increased connection latency and slow load times.

Which of the following is the MOST cost-effective solution to improve the uptime of the application with MINIMAL change and improve the overall user experience?

- **A.** Set up a new Amazon CloudFront web distribution to improve the overall user experience of your desktop applications. Migrate the MySQL database from your VM to an Amazon Redshift cluster. Host the application and presentation layers in Amazon ECS containers behind a Network Load Balancer.
- **B.** Use Amazon ElastiCache to improve the overall user experience of your desktop applications. Directly migrate the MySQL database from your VM to an Amazon DynamoDB database. Host the application and presentation layers in AWS Fargate containers behind an Application Load Balancer.
- **C.** Use Amazon WorkSpaces applications (formerly Amazon AppStream 2.0) to centrally manage your desktop applications and improve the overall user experience. Migrate the MySQL database from your VM to Amazon Aurora. Host the application and presentation layers in an Auto Scaling group on Amazon EC2 instances behind an Application Load Balancer.
- **D.** Using Amazon WorkSpaces, set up and allocate a workspace for each user to improve the overall user experience. Migrate the MySQL database from your VM to a self-hosted MySQL database in a large Amazon EC2 instance. Host the application and presentation layers in Amazon ECS containers behind an Application Load Balancer.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** desktop client applications, MINIMAL change, most cost-effective

🪤 **Your trap:** WorkSpaces = full virtual desktops per user (expensive); self-hosted MySQL on EC2 adds ops

🧠 **Rule:** Stream desktop apps → AppStream 2.0 (WorkSpaces applications); DB → Aurora; tiers → ASG + ALB

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises data center
┌─────────────────────────────────────┐
│ Desktop client apps (remote users)   │  ← latency cao, load chậm
│ Presentation + business logic (VMs)   │
│ MySQL DB (single VM)                  │
└─────────────────────────────────────┘

Yêu cầu: MOST cost-effective + MINIMAL change + cải thiện uptime & UX
```

Đáp án đúng: **C** (WorkSpaces applications/AppStream 2.0 cho desktop app + Aurora cho DB + ASG/EC2 + ALB cho app/presentation). Anh chọn **D** (WorkSpaces per-user + self-hosted MySQL trên EC2 lớn + ECS + ALB).

#### Vì sao C đúng

```
Users ──stream app──► WorkSpaces applications (AppStream 2.0)
Presentation+Logic ──► ASG trên EC2 ──behind──► ALB
MySQL (VM) ──migrate──► Amazon Aurora
```

- **WorkSpaces applications (AppStream 2.0)**: stream riêng **ứng dụng desktop**, không cấp cả một virtual desktop cho mỗi user. Đề chỉ nói "desktop client applications" chứ không yêu cầu toàn bộ desktop Windows/Linux cho user → dùng application streaming là đủ và **rẻ hơn** cấp WorkSpaces đầy đủ cho từng người.
- **Amazon Aurora**: MySQL tương thích trực tiếp với Aurora MySQL-compatible edition → migrate dễ, được quản lý hoàn toàn (managed), giảm vận hành so với tự host MySQL trên EC2.
- **Auto Scaling group + ALB**: scale tầng application/presentation theo tải, là pattern chuẩn, chi phí hợp lý, vận hành đơn giản hơn so với container orchestration không cần thiết.

#### Vì sao D (lựa chọn của anh) sai

D dùng **Amazon WorkSpaces** (không phải "applications" — là full virtual desktop) **cấp riêng cho mỗi user**. Đây là **Desktop-as-a-Service (DaaS)** đầy đủ — chi phí cao hơn nhiều vì mỗi user có một virtual desktop hoàn chỉnh, trong khi đề không hề nói user cần cả màn hình desktop Windows/Linux, chỉ cần chạy desktop *application*. Ngoài ra D còn migrate MySQL sang **self-hosted MySQL trên một EC2 instance lớn** — vẫn phải tự quản lý patching, backup, HA → không giảm được operational overhead, không phải "minimal change" theo đúng nghĩa managed service.

#### Các lựa chọn sai còn lại

- **A** — CloudFront cho desktop app (không hợp lý vì đây không phải nội dung web tĩnh để cache), migrate MySQL sang **Redshift** (Redshift là data warehouse cho OLAP, không phù hợp để làm database vận hành (OLTP) thay cho MySQL), dùng ECS + NLB.
- **B** — ElastiCache không đủ để cải thiện UX cho desktop *client* applications (ElastiCache chỉ là cache tầng dữ liệu); migrate trực tiếp MySQL (relational) sang DynamoDB (NoSQL) là **không khả thi trực tiếp** vì khác mô hình dữ liệu hoàn toàn; dùng Fargate + ALB.

#### Bảng so sánh

| Lựa chọn | Desktop app | Database | App/Presentation | Vấn đề |
|---|---|---|---|---|
| **C (đúng)** | AppStream 2.0 (chỉ app) | Aurora | ASG EC2 + ALB | — |
| D (anh chọn) | WorkSpaces full desktop | Self-hosted MySQL/EC2 | ECS + ALB | Chi phí cao hơn, vẫn tự quản lý DB |
| A | CloudFront | Redshift | ECS + NLB | Redshift không phải OLTP DB, CloudFront sai mục đích |
| B | ElastiCache | DynamoDB | Fargate + ALB | Không migrate trực tiếp relational→NoSQL |

#### Lưu ý thực tế

- 📝 **Ghi chú kỹ thuật:** "WorkSpaces applications" (AppStream 2.0) ≠ "Amazon WorkSpaces" — WorkSpaces applications chỉ stream **ứng dụng**, WorkSpaces (cổ điển) cấp **toàn bộ virtual desktop**. Đề thi SAP-C02 thường test chính xác sự khác biệt này.
- Aurora hỗ trợ MySQL-compatible và PostgreSQL-compatible — khi nguồn là MySQL, Aurora MySQL edition là lựa chọn migrate tự nhiên, ít thay đổi logic ứng dụng nhất.

#### Quy tắc nhớ cho thi

- **Thấy "desktop client applications" (không nói cần cả desktop OS)** → **AppStream 2.0 / WorkSpaces applications**, không phải WorkSpaces full desktop
- **Migrate MySQL, cần managed + minimal change** → **Aurora**, không phải self-hosted trên EC2, không phải Redshift/DynamoDB
- **"Most cost-effective + minimal change"** → luôn ưu tiên managed service thay thế đúng vai trò cũ, tránh giải pháp cấp phát tài nguyên riêng cho từng user

### TD explanation

Amazon WorkSpaces applications (formerly Amazon AppStream 2.0) is a fully managed application streaming service. You centrally manage your desktop applications on WorkSpaces applications and securely deliver them to any computer. You can easily scale to any number of users across the globe without acquiring, provisioning, and operating hardware or infrastructure. WorkSpaces applications is built on AWS, so you benefit from a data center and network architecture designed for the most security-sensitive organizations. Each user has a fluid and responsive experience with your applications, including GPU-intensive 3D design and engineering ones, because your applications run on virtual machines (VMs) optimized for specific use cases and each streaming session automatically adjusts to network conditions.

Enterprises can use WorkSpaces applications to simplify application delivery and complete their migration to the cloud. Educational institutions can provide every student access to the applications they need for class on any computer. Software vendors can use WorkSpaces applications to deliver trials, demos, and training for their applications with no downloads or installations. They can also develop a full software-as-a-service (SaaS) solution without rewriting their application.
Therefore, the correct answer is: Use Amazon WorkSpaces applications (formerly Amazon AppStream 2.0) to centrally manage your desktop applications and improve the overall user experience. Migrate the MySQL database from your VM to Amazon Aurora. Host the application and presentation layers in an Auto Scaling group on Amazon EC2 instances behind an Application Load Balancer.
The option that says: Set up a new Amazon CloudFront web distribution to improve the overall user experience of your desktop applications. Migrate the MySQL database from your VM to an Amazon Redshift cluster. Host the application and presentation layers in Amazon ECS containers behind a Network Load Balancer is incorrect. It is not suitable to migrate your MySQL database to a Redshift cluster.
The option that says: Use Amazon ElastiCache to improve the overall user experience of your desktop applications. Directly migrate the MySQL database from your VM to an Amazon DynamoDB database. Host the application and presentation layers in AWS Fargate containers behind an Application Load Balancer is incorrect. You cannot directly migrate your MySQL database, which is relational in type, to DynamoDB which is a NoSQL database or non-relational. The use of Amazon ElastiCache alone will not significantly improve the overall user experience since this service is primarily used for caching.
The option that says: Using Amazon WorkSpaces, set up and allocate a workspace for each user to improve the overall user experience. Migrate the MySQL database from your VM to a self-hosted MySQL database in a large Amazon EC2 instance. Host the application and presentation layers in Amazon ECS containers behind an Application Load Balancer is incorrect. Amazon WorkSpaces is primarily used as a managed, secure Desktop-as-a-Service (DaaS) solution and it costs a lot to implement. Take note that in the scenario, it was mentioned that they are using desktop applications but there was no mention about the need for Windows or Linux desktops which is why the use of Amazon WorkSpaces is incorrect.

References:
https://aws.amazon.com/appstream2/
https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q72"></a>

## Q72

A company uses Amazon WorkSpaces to improve the productivity and security of its remote workers. Hundreds of remote workers log in to the virtual desktop service using the Amazon WorkSpaces client application on a regular basis. Users have reported that they cannot log in to their virtual desktops even though they have the correct credentials.

Upon investigation, the Solutions Architect discovered that the filesystem storing the user profiles has reached its capacity, which is the reason why users cannot establish a new session in Amazon WorkSpaces. The environment is configured with a 10 TB Amazon FSx for Windows File Server file system to store the user profiles.

Which of the following options should the Solutions Architect implement to solve the issue and prevent it from happening again?

- **A.** Create a new Amazon FSx for Windows File Server file system with a larger capacity. Create a script to copy all user profiles to the new file system. Create an Amazon CloudWatch metric to monitor the FreeStorageCapacity of the filesystem and send a notification via Amazon SNS before it reaches capacity.
- **B.** Create an Amazon CloudWatch Alarm to monitor the FreeStorageCapacity metric of the file system. Write an AWS Lambda Function to increase the capacity of the Amazon FSx for Windows File Server file system using the update-file-system command. Utilize Amazon EventBridge to invoke this Lambda function when the metric threshold is reached.
- **C.** Create an Amazon CloudWatch Alarm using the FreeStorageCapacity metric to monitor the file system. Once triggered, use AWS Steps Functions as the target. Run the Steps Function to create a new Amazon FSx for Windows File Server file system and migrate the user profiles.
- **D.** From the Amazon FSx console, select the desired file system to edit its attributes. Enable the option Dynamically Allocate to allow the file system to scale depending on the size of the data stored. This will present a large capacity drive to Amazon WorkSpaces clients and will grow automatically as users add more data to their profiles.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** filesystem reached capacity, solve and prevent it from happening again

🪤 **Your trap:** Creating a new FSx + copying profiles is manual — FSx can grow in place

🧠 **Rule:** FSx for Windows: increase storage in place (update-file-system); automate with CloudWatch alarm → EventBridge → Lambda

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
WorkSpaces users ──► Amazon FSx for Windows File Server (10 TB, lưu user profiles)
                              │
                       ĐÃ ĐẦY → user không login được

Yêu cầu: giải quyết NGAY + tránh lặp lại trong tương lai (tự động)
```

Đáp án đúng: **B** (CloudWatch Alarm → EventBridge → Lambda gọi `update-file-system` để tăng dung lượng). Anh chọn **A** (tạo file system mới lớn hơn, script copy dữ liệu, SNS cảnh báo).

#### Vì sao B đúng

```
FreeStorageCapacity metric ──CloudWatch Alarm──► EventBridge ──► Lambda
                                                                     │
                                                      gọi update-file-system
                                                      (tăng capacity NGAY TRÊN FILE SYSTEM HIỆN TẠI)
```

- Amazon FSx for Windows File Server hỗ trợ **tăng dung lượng ngay trên file system hiện có** qua console, API, hoặc CLI (`update-file-system`) — không cần tạo file system mới.
- Khi tăng dung lượng, FSx tự động thêm một bộ disk mới lớn hơn và **tự chạy quy trình optimization để di chuyển dữ liệu từ disk cũ sang disk mới trong background** — người dùng không phải tự viết script copy.
- Thiết lập **CloudWatch Alarm theo dõi FreeStorageCapacity**, khi đạt ngưỡng thì **EventBridge** kích hoạt **Lambda** tự động gọi `update-file-system` — giải quyết đồng thời cả 2 phần: xử lý ngay (khi chạy lần đầu) và tự động hóa để "prevent it from happening again".

#### Vì sao A (lựa chọn của anh) sai

A tạo **một file system FSx mới** dung lượng lớn hơn, rồi **viết script tự copy** toàn bộ user profile sang. Vấn đề: việc này hoàn toàn **thủ công và không cần thiết** — vì FSx đã có khả năng tăng dung lượng in-place và tự động migrate data ở background. Tạo mới + script copy là làm lại việc mà dịch vụ đã làm sẵn, phát sinh thêm thao tác và rủi ro vận hành.

#### Các lựa chọn sai còn lại

- **C** — CloudWatch Alarm → Step Functions → tạo file system mới + migrate profiles: cùng lỗi với A, chỉ khác là dùng Step Functions để tự động hóa việc **tạo mới + migrate** — vẫn thừa, vì FSx tự tăng dung lượng in-place và tự di chuyển dữ liệu nền.
- **D** — Bật tùy chọn "Dynamically Allocate" trên console FSx: **không có tùy chọn này tồn tại** trên Amazon FSx. Dung lượng chỉ có thể điều chỉnh thủ công/qua tự động hóa (console, API, CLI), không có auto-scale storage kiểu "dynamically allocate".

#### Bảng so sánh

| Lựa chọn | Cách tăng dung lượng | Tự động hóa | Vấn đề |
|---|---|---|---|
| **B. CloudWatch → EventBridge → Lambda → update-file-system** | Tăng in-place | Có | — (đúng) |
| A. Tạo file system mới + script copy | Tạo mới + copy thủ công | Một phần (chỉ cảnh báo SNS) | Thừa — FSx đã tự copy khi tăng dung lượng |
| C. CloudWatch → Step Functions → tạo mới + migrate | Tạo mới + migrate | Có | Thừa — không cần tạo mới |
| D. "Dynamically Allocate" | — | — | Tính năng không tồn tại |

#### Lưu ý thực tế (đề không hỏi nhưng dễ vấp)

- 📝 **Ghi chú kỹ thuật:** Amazon FSx **chỉ có thể tăng** dung lượng, **không thể giảm** sau khi đã tăng.
- Metric `FreeStorageCapacity` là metric chuẩn trên CloudWatch để theo dõi dung lượng còn trống của FSx file system — nên nhớ tên chính xác này khi gặp câu hỏi dạng alarm/threshold.

#### Quy tắc nhớ cho thi

- **FSx hết dung lượng** → tăng **in-place** bằng `update-file-system`, KHÔNG tạo file system mới + tự copy
- **"Prevent from happening again"** → luôn cần vòng tự động hóa: CloudWatch Alarm → EventBridge → Lambda
- **Không có "Dynamically Allocate" trên FSx** → nếu thấy option này trong đáp án, loại ngay

### TD explanation

Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system. With file storage on Amazon FSx, the code, applications, and tools that Windows developers and administrators use today can continue to work unchanged. Windows applications and workloads ideal for Amazon FSx include business applications, home directories, web serving, content management, data analytics, software build setups, and media processing workloads.
As you need additional storage, you can increase the storage capacity that is configured on your FSx for Windows File Server file system. You can do so using the Amazon FSx console, the Amazon FSx API, or the AWS Command Line Interface (AWS CLI).
You can only increase the amount of storage capacity for a file system; you cannot decrease storage capacity. When you increase the storage capacity of your Amazon FSx file system, behind the scenes, Amazon FSx adds a new, larger set of disks to your file system. Amazon FSx then runs a storage optimization process in the background to transparently migrate data from the old disks to the new disks.
The following illustration shows the four main steps of the process that Amazon FSx uses when increasing a file system's storage capacity.

EventBridge (CloudWatch Events) helps you to respond to state changes in your AWS resources. With EventBridge (CloudWatch Events), you can create rules that match selected events in the stream and route them to your AWS Lambda function to take action.
Using the update-file-system command, you can use AWS SDK or CLI to programmatically increase the size of the FSx file system. You can use Amazon CloudWatch to monitor the metrics of the file system and trigger the Lambda function to perform an action.
Therefore, the correct answer is: Create an Amazon CloudWatch Alarm to monitor the FreeStorageCapacity metric of the file system. Write an AWS Lambda Function to increase the capacity of the Amazon FSx for Windows File Server file system using the update-file-system command. Utilize Amazon EventBridge to invoke this Lambda function when the metric threshold is reached.
The option that says: Create a new Amazon FSx for Windows File Server file system with a larger capacity. Create a script to copy all user profiles to the new file system. Create an Amazon CloudWatch metric to monitor the FreeStorageCapacity of the filesystem and send a notification via Amazon SNS before it reaches capacity is incorrect. You don't have to manually copy all user data to a new volume. You can increase the file system and Amazon FSx automatically migrates the data to a larger volume in the background.
The option that says: Create an Amazon CloudWatch Alarm using the FreeStorageCapacity metric to monitor the file system. Once triggered, use AWS Steps Functions as the target. Run the Steps Function to create a new Amazon FSx for Windows File Server file system and migrate the user profiles is incorrect. You don't need to create the Step Function to migrate the user profiles. Amazon FSx automatically migrates the data in the background when you increase the file system size.
The option that says: From the Amazon FSx console, select the desired file system to edit its attributes. Enable the option Dynamically Allocate to allow the file system to scale depending on the size of the data stored. This will present a large capacity drive to Amazon WorkSpaces clients and will grow automatically as users add more data to their profiles is incorrect. There is no option to Dynamically Allocate the file system size. You can manually adjust the file system size using the Amazon FSx console, the Amazon FSx API, or the AWS CLI.

References:
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html
https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html

Check out this Amazon FSx Cheat Sheet and Amazon CloudWatch Cheat Sheets:
https://tutorialsdojo.com/amazon-fsx/
https://tutorialsdojo.com/amazon-cloudwatch/

</details>

---

# Group B — Data protection & network access (6)

<a id="q13"></a>

## Q13

A company wants to migrate its on-premises application to the AWS cloud. Due to limited manpower, the company wants to utilize fully managed AWS services as much as possible. This way, there will be less maintenance work after the migration. The application processes large files containing sensitive information so the company has the following requirements:

Data encryption at rest and in transit are both required on all files that will be processed by the application.

The storage solution must be highly durable and available.

The company must be able to use its own encryption key and then periodically rotated for improved security.

Amazon Redshift Spectrum will be used to analyze the migrated data.

Which of the following should the Solutions Architect implement to achieve these requirements?

- **A.** Provision an AWS Storage Gateway – File Gateway device in the on-premises data center. Enable encryption on the file share with AWS KMS. The data will be transferred securely to an Amazon S3 bucket with SSE-S3 encryption.
- **B.** Create an Amazon S3 bucket to store all data. Enable server-side encryption with AWS KMS (SSE-KMS). Apply a bucket policy that enforces HTTPS only connections to the S3 bucket.
- **C.** Store the data files on an Amazon DynamoDB table. Leverage on the default SSL connection settings of the DynamoDB table. Use AWS KMS to encrypt the table and enable automatic key rotation.
- **D.** Store the data files in an Amazon EC2 instance with an encrypted EBS volume. Use AWS KMS to encrypt the EBS volume and enable automatic key rotation.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** use its own encryption key, periodically rotated, fully managed, Redshift Spectrum

🪤 **Your trap:** SSE-S3 keys are AWS-managed, not the company's; File Gateway adds overhead

🧠 **Rule:** Own key + rotation on S3 → SSE-KMS; in-transit → bucket policy with aws:SecureTransport

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises files (chứa sensitive info)
        │
        ▼
  ┌─────────────────────────┐
  │ Lưu trữ + mã hóa ở đâu? │
  └─────────────────────────┘
Yêu cầu:
  - Mã hóa at rest + in transit
  - Durable + available cao
  - DÙNG CHÍNH KEY CỦA CÔNG TY, key phải ĐƯỢC XOAY (rotate) định kỳ
  - Sau đó Redshift Spectrum sẽ query trực tiếp lên data
  - Fully managed, ít overhead vận hành nhất có thể
```

Đáp án đúng: **B** (S3 + SSE-KMS + bucket policy HTTPS-only). Anh chọn **A** (Storage Gateway File Gateway + SSE-S3).

#### Vì sao B đúng

- **SSE-KMS** cho phép dùng **customer managed KMS key** — đây chính là "own encryption key" mà đề yêu cầu, và key này hỗ trợ **automatic key rotation** định kỳ.
- S3 tự đạt 11 số 9 durability, không cần quản lý hạ tầng gì thêm → đúng tinh thần "fully managed, ít overhead".
- Để ép mã hóa in-transit, thêm bucket policy deny khi `aws:SecureTransport = false`.
- Redshift Spectrum đọc trực tiếp dữ liệu nằm trên S3 — không cần thêm bước di chuyển dữ liệu.

#### Vì sao A (lựa chọn của anh) sai

**Trap:** Storage Gateway – File Gateway nghe có vẻ hợp lý để đẩy file on-premises lên cloud, nhưng:

- Đích đến cuối cùng trong option A là bucket dùng **SSE-S3** — SSE-S3 nghĩa là Amazon S3 tự quản lý key, công ty **không có quyền kiểm soát hay tự rotate key này**. Yêu cầu "use its own encryption key... periodically rotated" đòi hỏi SSE-KMS, không phải SSE-S3.
- File Gateway tạo thêm một thiết bị phải cấu hình, vận hành, bảo trì → tăng overhead, ngược với mục tiêu "fully managed, less maintenance".

#### Các lựa chọn sai khác

- **C (DynamoDB):** mỗi item DynamoDB giới hạn 400 KB — không phù hợp để lưu "large files".
- **D (EC2 + encrypted EBS):** phải tự provision và quản lý EC2 instance — tăng overhead vận hành; một EBS volume đơn lẻ cũng không durable bằng S3 (11 9's).

| Option | Key do ai quản lý | Rotate được? | Overhead vận hành |
|---|---|---|---|
| **B. S3 + SSE-KMS** | Customer managed KMS key | Có | Thấp nhất |
| A. File Gateway + SSE-S3 | AWS quản lý (SSE-S3) | Không (key không thuộc công ty) | Cao hơn (phải quản lý gateway) |
| C. DynamoDB | KMS | Có | Giới hạn item 400KB |
| D. EC2 + EBS | KMS | Có | Cao (tự quản EC2) |

#### Lưu ý thực tế

- SSE-S3, SSE-KMS, SSE-C khác nhau ở **ai quản lý key**: SSE-S3 → AWS toàn quyền; SSE-C → anh tự quản key; SSE-KMS → AWS quản data key nhưng anh quản **KMS key** (tạo, rotate, disable, audit).
- "Use own key" trên exam hầu như luôn trỏ tới **SSE-KMS với customer managed key**, không phải SSE-S3.

#### Quy tắc nhớ cho thi

- **Thấy "own key" + "rotation" trên S3** → **SSE-KMS (customer managed key)**
- **Thấy "in-transit enforce"** → bucket policy deny khi `aws:SecureTransport: false`
- **Thấy "fully managed, least maintenance"** → ưu tiên S3 trực tiếp, tránh thêm Storage Gateway/EC2 nếu không cần thiết
- **Thấy "large files"** → loại DynamoDB (giới hạn item 400KB)

### TD explanation

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers scalability, data availability, security, and performance. Amazon S3 is designed for 99.999999999% (11 9's) of durability, and stores data for millions of applications for companies all around the world.
Amazon S3 default encryption provides a way to set the default encryption behavior for an S3 bucket. You can set default encryption on a bucket so that all new objects are encrypted when they are stored in the bucket. The objects are encrypted using server-side encryption with either Amazon S3-managed keys (SSE-S3) or KMS keys stored in AWS Key Management Service (AWS KMS).
SSE-S3 requires that Amazon S3 manage the data and the encryption keys.
SSE-C requires that you manage the encryption key.
SSE-KMS requires that AWS manage the data key but you manage the KMS key in AWS KMS.
When you configure your bucket to use default encryption with SSE-KMS, you can also enable an S3 Bucket Key to decrease request traffic from Amazon S3 to AWS Key Management Service (AWS KMS) and reduce the cost of encryption. When you configure your bucket to use an S3 Bucket Key for SSE-KMS on new objects, AWS KMS generates a bucket-level key that is used to create a unique data key for objects in the bucket. This bucket key is used for a time-limited period within Amazon S3, reducing the need for Amazon S3 to make requests to AWS KMS to complete encryption operations.

By default, Amazon S3 allows both HTTP and HTTPS requests. To comply with the s3-bucket-ssl-requests-only rule (only accepting HTTPS connections), your bucket policy should explicitly deny access to HTTP requests. To determine HTTP or HTTPS requests in a bucket policy, use a condition that checks for the key "aws:SecureTransport". When this key is set to true, this means that the request is sent through HTTPS. To be sure to comply with the s3-bucket-ssl-requests-only rule, create a bucket policy that explicitly denies access when the request meets the condition "aws:SecureTransport": "false". This policy explicitly denies access to HTTP requests.
Therefore, the correct answer is: Create an Amazon S3 bucket to store all data. Enable server-side encryption with AWS KMS (SSE-KMS). Apply a bucket policy that enforces HTTPS only connections to the S3 bucket.
The option that says: Provision an AWS Storage Gateway – File Gateway device in the on-premises data center. Enable encryption on the file share with AWS KMS. The data will be transferred securely to an Amazon S3 bucket with SSE-S3 encryption is incorrect. Although this is possible, the encryption key on the S3 with SSE-S3 is managed by AWS and not the customer. This also entails more management overhead because you need to manage your file gateway. Less maintenance is needed if data is just sent directly to an encrypted S3 bucket.
The option that says: Store the data files on an Amazon DynamoDB table. Leverage on the default SSL connection settings of the DynamoDB table. Use AWS KMS to encrypt the table and enable automatic key rotation is incorrect. The application processes large documents that may not fit on an Amazon DynamoDB table in which each entry is limited to 400 KB only.
The option that says: Store the data files in an Amazon EC2 instance with an encrypted EBS volume. Use AWS KMS to encrypt the EBS volume and enable automatic key rotation is incorrect as this entails more management overhead as you need to provision your own EC2 instance. Amazon S3 is also more durable compared to a single Amazon EC2 instance with EBS volume.

References:
https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html
https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/

Check out these Amazon S3 and AWS KMS Cheat Sheets:
https://tutorialsdojo.com/amazon-s3/
https://tutorialsdojo.com/aws-kms-keys-policy-management-in-aws-kms/

</details>

<a id="q17"></a>

## Q17

A company hosts an internal web portal on a fleet of Amazon EC2 instances that allows access to confidential files stored in an encrypted Amazon S3 bucket. Because the files contain sensitive information, the company does not want any files to traverse the public Internet. Bucket access should be restricted to only allow the web portal’s EC2 instances. To comply with the requirements, the Solutions Architect created an Amazon S3 VPC endpoint and associated it with the web portal’s VPC.

Which of the following actions should the Solutions Architect take to fully comply with the company requirements?

- **A.** Create a VPC endpoint policy that restricts access to the specific Amazon S3 bucket. Apply an Amazon S3 bucket policy that only allows access from the VPC endpoint. Update the VPC’s Network Access Control List (NACL) to deny other EC2 instances from accessing the gateway prefix list.
- **B.** Apply an Amazon S3 bucket policy that includes the aws:SourceIp condition to deny all access except those coming from the application EC2 instances IP addresses. Update the route table for the VPC to ensure that the VPC endpoint is associated only with the application instances subnets.
- **C.** Create a VPC endpoint policy that restricts access to the specific Amazon S3 bucket. Create an IAM role that grants access to the S3 bucket and attach it to the application EC2 instances. Apply an Amazon S3 bucket policy that only allows access from the VPC endpoint and those using the IAM role.
- **D.** Create a VPC endpoint policy that restricts access to the specific Amazon S3 bucket on the current region. Apply an Amazon S3 bucket policy that only allows access from the VPC private subnets. Update the VPC’s Network Access Control List (NACL) to deny other EC2 instances from accessing the gateway prefix list.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** restrict to only the web portal's EC2 instances, not traverse the public Internet

🪤 **Your trap:** NACLs can't reference the gateway prefix list for this; the bucket policy must also check identity

🧠 **Rule:** S3 via gateway endpoint: endpoint policy (which bucket) + bucket policy (aws:sourceVpce + IAM role) + IAM role on EC2

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Web portal EC2 fleet (VPC)
        │  (S3 Gateway VPC Endpoint — không qua Internet)
        ▼
  Encrypted S3 bucket (confidential files)

Yêu cầu:
  - File KHÔNG đi qua public Internet
  - CHỈ web portal EC2 instances mới truy cập được bucket
```

Đáp án đúng: **C**. Anh chọn **A** — đây là `⚠️ Lỗi lặp lại`: cùng một cụm khái niệm "S3 gateway endpoint + endpoint policy + bucket policy + IAM role" đã từng bị bỏ sót trước đây (liên quan S3 access point/gateway endpoint).

#### Vì sao C đúng — ba lớp phải khớp nhau

```
VPC Endpoint Policy      → giới hạn endpoint chỉ cho phép tới ĐÚNG bucket
IAM Role (gắn vào EC2)   → cấp quyền s3:* cụ thể cho application
Bucket Policy            → chỉ allow nếu request đến từ (aws:sourceVpce = endpoint này)
                           VÀ principal dùng IAM role đó
```

Ba lớp này cộng lại mới ra đúng một giải pháp:
- **Endpoint policy** trả lời "endpoint này được gọi S3 action nào, trên bucket nào".
- **IAM role trên EC2** trả lời "instance nào (identity nào) được phép gọi".
- **Bucket policy với `aws:SourceVpce`** trả lời "request phải đi qua đúng VPC endpoint này" — chặn luôn mọi traffic không qua endpoint (tức không qua Internet).

Thiếu IAM role: endpoint + bucket policy chỉ chặn theo đường mạng, chưa chặn theo **danh tính** — bất kỳ ai dùng được endpoint đó cũng vào được bucket. TD explanation nói rõ: "you must explicitly allow the user-level permissions" bằng IAM policy hoặc statement khác trong bucket policy.

#### Vì sao A (lựa chọn của anh) sai

A có endpoint policy + bucket policy allow từ VPC endpoint — đúng hướng, nhưng phần cuối "update NACL để deny EC2 khác truy cập **gateway prefix list**" là sai kỹ thuật: **NACL không thể reference prefix list của gateway endpoint** theo cách này. TD explanation: "gateway prefix list ID should be added to the **route table**... not on the NACL." Gateway endpoint hoạt động qua route table (route tới prefix list `pl-xxxxxxxx` → target là endpoint), không qua NACL.

#### Các lựa chọn sai khác

- **B:** dùng `aws:SourceIp` trong bucket policy — nhưng điều kiện này **không áp dụng được** cho request đi qua VPC endpoint (SourceIp chỉ dùng cho IP công khai hoặc trong VPC, không nhận diện được traffic qua gateway endpoint).
- **D:** bucket policy "chỉ allow từ VPC private subnets" — S3 bucket policy **không nhận subnet ID** làm điều kiện; và vẫn mắc lỗi NACL/gateway prefix list giống A.

| Option | Endpoint policy | Bucket policy đúng cơ chế | IAM role trên EC2 | Lỗi |
|---|---|---|---|---|
| **C (đúng)** | Có | `aws:sourceVpce` + role | Có | — |
| A (anh chọn) | Có | `aws:sourceVpce` | Không | NACL không nhận prefix list |
| B | — | `aws:SourceIp` (sai context) | — | SourceIp không dùng được qua VPC endpoint |
| D | Có | Subnet ID (không hợp lệ) | — | Bucket policy không nhận subnet ID + lỗi NACL |

#### Lưu ý thực tế

- Gateway endpoint (S3, DynamoDB) gắn vào **route table**, không gắn vào NACL/SG.
- `aws:SourceVpce` chỉ dùng được trong bucket policy khi traffic đi qua chính VPC endpoint đó.
- Chỉ chặn theo mạng (network path) là chưa đủ "least privilege" — vẫn cần ràng buộc theo identity (IAM role/user).

#### Quy tắc nhớ cho thi

- **Thấy "restrict S3 chỉ cho EC2 cụ thể qua VPC endpoint"** → cần **cả 3**: endpoint policy + bucket policy (`aws:sourceVpce`) + IAM role trên EC2
- **Thấy "NACL + gateway prefix list"** → luôn là bẫy, gateway endpoint dùng **route table**, không dùng NACL
- **Thấy `aws:SourceIp` cho traffic qua VPC endpoint** → sai, SourceIp không áp dụng được ở đây

### TD explanation

When you create an interface or gateway endpoint, you can attach an endpoint policy to it that controls access to the service to which you are connecting. Endpoint policies must be written in JSON format. Not all services support endpoint policies.
A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when you create or modify the endpoint. If you do not attach a policy when you create an endpoint, we attach a default policy for you that allows full access to the service. If a service does not support endpoint policies, the endpoint allows full access to the service. An endpoint policy does not override or replace IAM user policies or service-specific policies (such as S3 bucket policies). It is a separate policy for controlling access from the endpoint to the specified service.
You cannot attach more than one policy to an endpoint. However, you can modify the policy at any time. If you do modify a policy, it can take a few minutes for the changes to take effect.
Your endpoint policy can be like any IAM policy; however, take note of the following:
- Your policy must contain a Principal element.
- The size of an endpoint policy cannot exceed 20,480 characters.
When you create or modify an endpoint, you specify the VPC route tables that are used to access the service via the endpoint. A route is automatically added to each of the route tables with a destination that specifies the AWS prefix list ID of the service (pl-xxxxxxxx), and a target with the endpoint ID (vpce-xxxxxxxx).
The following example bucket policy blocks traffic to the bucket unless the request is from specified VPC endpoints (aws:sourceVpce):

{
  "Id": "VPCe",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VPCe",
      "Action": "s3:*",
      "Effect": "Deny",
      "Resource": [
        "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
        "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpce": [
            "vpce-1111111",
            "vpce-2222222"
          ]
        }
      },
      "Principal": "*"
    }
  ]
}

- To use this policy with the aws:sourceVpce condition, you must attach a VPC endpoint for Amazon S3. The VPC endpoint must be attached to the route table of the EC2 instance's subnet, and in the same AWS Region as the bucket.
- To allow users to perform S3 actions on the bucket from the VPC endpoints or IP addresses, you must explicitly allow the user-level permissions. You can explicitly allow user-level permissions on either an AWS Identity and Access Management (IAM) policy or another statement in the bucket policy.
Therefore, the correct answer is: Create a VPC endpoint policy that restricts access to the specific Amazon S3 bucket. Create an IAM role that grants access to the S3 bucket and attach it to the application EC2 instances. Apply an Amazon S3 bucket policy that only allows access from the VPC endpoint and those using the IAM role. This ensures that traffic to the S3 bucket are all coming from the VPC endpoint and that the application EC2 instances are the only ones allowed to access it.
The option that says: Create a VPC endpoint policy that restricts access to the specific Amazon S3 bucket. Apply an Amazon S3 bucket policy that only allows access from the VPC endpoint. Update the VPC’s Network Access Control List (NACL) to deny other EC2 instances from accessing the gateway prefix list is incorrect. The gateway prefix list ID should be added to the route table in the VPC to allow access for the specific subnet, and not on the NACL.
The option that says: Apply an Amazon S3 bucket policy that includes the aws:SourceIp condition to deny all access except those coming from the application EC2 instances IP addresses. Update the route table for the VPC to ensure that the VPC endpoint is associated only with the application instances subnets is incorrect. The aws:SourceIp is used for specifying external IP addresses (from the public Internet or from within the VPC). You cannot use the aws:SourceIp condition in your bucket policies for Amazon S3 requests coming from a VPC endpoint. When you associate a VPC endpoint to your VPC, the route tables are automatically updated to include the AWS prefix list ID.
The option that says: Create a VPC endpoint policy that restricts access to the specific Amazon S3 bucket on the current region. Apply an Amazon S3 bucket policy that only allows access from the VPC private subnets. Update the VPC’s Network Access Control List (NACL) to deny other EC2 instances from accessing the gateway prefix list is incorrect. You cannot input subnet IDs as restrictions on the bucket policies. You should use VPC endpoint or source IPs instead.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html#vpc-endpoint-policies
https://aws.amazon.com/premiumsupport/knowledge-center/block-s3-traffic-vpc-ip/

Check out these Amazon VPC and Amazon S3 Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q28"></a>

## Q28

A financial services company uses hardware security modules (HSMs) to generate encryption master keys. Since the company application logs include personally identifiable information, encryption is required as part of regulatory compliance. The application logs are going to be stored on a central Amazon S3 bucket and should be encrypted at rest. The security team wants to use the company HSMs to generate the key material for encryption on the S3 bucket.

Which of the following options should the solutions architect implement to meet the company’s requirements?

- **A.** Create a new AWS CloudHSM cluster and set it as the key material source in AWS Key Management Service (KMS) when you generate a new KMS key. Set a 1-year duration for the KMS key automatic key rotation. Apply an Amazon S3 bucket policy on the central logging bucket to require AWS KMS as the encryption source and deny unencrypted object uploads.
- **B.** Request to provision an AWS Direct Connect connection from the on-premises data center to AWS VPC. Ensure that the network addresses do not overlap. Apply an Amazon S3 bucket policy on the central logging bucket to allow only encrypted object uploads. Configure the application to generate a unique KMS key for each logging event by querying the on-premises HSMs through the Direct Connection network.
- **C.** Using AWS CLI, create a new KMS key with no key material and use EXTERNAL as the origin of the key. Generate a key from the on-premises HSMs and import it as KMS key using the public key and import token from AWS. Apply an Amazon S3 bucket policy on the central logging bucket to require AWS KMS as the encryption source and deny unencrypted object uploads.
- **D.** Using AWS CLI, create a new KMS key with AWS-provided key material and use AWS_KMS as the origin of the key. Overwrite this KMS key with a generated key from the on-premises HSMs by using the public key and import token provided by AWS. Set a 1-year duration for the KMS key automatic key rotation. Apply an Amazon S3 bucket policy on the central logging bucket to require AWS KMS as the encryption source and deny unencrypted object uploads.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** use the company HSMs to generate the key material

🪤 **Your trap:** CloudHSM key store uses AWS CloudHSM, not the company's own on-prem HSMs

🧠 **Rule:** Key material from your own HSM → KMS key with Origin=EXTERNAL + import key material (BYOK)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises HSMs (công ty tự sở hữu)
        │ generate key material
        ▼
   AWS KMS key  ──────►  S3 bucket (logs chứa PII)
                          (server-side encryption, deny unencrypted upload)

Yêu cầu bắt buộc: dùng CHÍNH key material từ HSM CỦA CÔNG TY (không phải HSM của AWS)
```

Đáp án đúng: **C** (KMS key Origin=EXTERNAL, import key material từ HSM on-prem). Anh chọn **A** (CloudHSM cluster làm custom key store).

#### Vì sao C đúng

```
1. Tạo KMS key với "no key material", Origin = EXTERNAL
2. AWS cấp public key + import token
3. Dùng public key đó để wrap key material được generate TỪ HSM ON-PREMISES
4. Import key material đã wrap vào KMS key (Origin=EXTERNAL)
5. Áp bucket policy: require AWS KMS encryption + deny unencrypted upload
```

Đây chính là cơ chế **BYOK (Bring Your Own Key)** — key material sinh ra hoàn toàn từ HSM của công ty, AWS KMS chỉ "chứa" và quản lý vòng đời sử dụng (policy, audit, tích hợp dịch vụ), còn nguồn gốc material vẫn đúng yêu cầu compliance.

#### Vì sao A (lựa chọn của anh) sai

**Trap:** CloudHSM custom key store nghe giống "dùng HSM để tạo key", nhưng **AWS CloudHSM cluster là HSM do AWS vận hành** (dù tenant riêng cho công ty), **không phải HSM on-premises đang có sẵn** của công ty. TD explanation: "it uses an AWS CloudHSM cluster instead of the company's existing on-premises HSMs to generate the key material." Yêu cầu đề là "the security team wants to use the **company HSMs**" — rõ ràng chỉ HSM vật lý tại chỗ, không phải dịch vụ CloudHSM trên AWS.

#### Các lựa chọn sai khác

- **B:** dựng Direct Connect rồi generate **một KMS key riêng cho mỗi logging event** bằng cách query HSM on-prem qua network — không scalable, tạo quá nhiều key phải quản lý, và vẫn không enforce encryption rõ ràng trên bucket.
- **D:** tạo KMS key với Origin=AWS_KMS (key material do AWS sinh), sau đó "overwrite" bằng key từ HSM on-prem — **overwrite key material đang tồn tại rất rủi ro**, có thể gây mất dữ liệu/security risk; đúng cách là tạo key mới với Origin=EXTERNAL ngay từ đầu (no key material), không phải tạo rồi ghi đè.

| Option | Nguồn key material | Cách thực hiện | Vấn đề |
|---|---|---|---|
| **C (đúng)** | HSM on-prem | KMS Origin=EXTERNAL, import | — |
| A (anh chọn) | AWS CloudHSM (AWS vận hành) | Custom key store | Không phải HSM của công ty |
| B | HSM on-prem (qua DX) | 1 key/event | Không scalable, nhiều key |
| D | AWS_KMS rồi ghi đè | Overwrite key material | Rủi ro mất dữ liệu/an toàn |

#### Lưu ý thực tế

- **CloudHSM key store** (custom key store cho KMS) phù hợp khi công ty muốn **toàn quyền kiểm soát HSM compute** (FIPS 140-2 Level 3) nhưng **chấp nhận AWS cung cấp phần cứng HSM** — khác với yêu cầu "dùng chính HSM công ty đang sở hữu".
- **Import key material (Origin=EXTERNAL)** không hỗ trợ automatic key rotation của AWS — phải rotate thủ công (reimport) nếu cần, khác với key do AWS sinh (Origin=AWS_KMS) có thể enable automatic rotation.

#### Quy tắc nhớ cho thi

- **Thấy "use company's own/existing on-premises HSM to generate key material"** → **KMS key Origin=EXTERNAL + import key material** (BYOK)
- **Thấy "CloudHSM cluster" / "custom key store"** → đó là HSM do AWS cung cấp, KHÔNG phải HSM vật lý của công ty
- **Thấy "overwrite existing key material"** → luôn là bẫy, rủi ro mất data; phải tạo key mới Origin=EXTERNAL

### TD explanation

You can protect data at rest in Amazon S3 by using different modes of server-side encryption:
- SSE-S3: All Amazon S3 buckets have encryption configured by default. The default option for server-side encryption is with Amazon S3 managed keys (SSE-S3). Each object is encrypted with a unique key. As an additional safeguard, SSE-S3 encrypts the key itself with a root key that it regularly rotates. SSE-S3 uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.
- SSE-C: With server-side encryption with customer-provided keys (SSE-C), you manage the encryption keys, and Amazon S3 manages the encryption as it writes to disks and the decryption when you access your objects
- SSE-KMS: Server-side encryption with AWS KMS keys (SSE-KMS) is provided through an integration of the AWS KMS service with Amazon S3. With AWS KMS, you have more control over your keys.
- DSSE-KMS: Dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) is similar to SSE-KMS, but DSSE-KMS applies two individual layers of object-level encryption instead of one layer. Because both layers of encryption are applied to an object on the server side, you can use a wide range of AWS services and tools to analyze data in S3 while using an encryption method that can satisfy your compliance requirements.
Server-side encryption is the encryption of data at its destination by the application or service that receives it. AWS Key Management Service (AWS KMS) is a service that combines secure, highly available hardware and software to provide a key management system scaled for the cloud. Amazon S3 uses server-side encryption with AWS KMS (SSE-KMS) to encrypt your S3 object data. Also, when SSE-KMS is requested for the object, the S3 checksum (as part of the object's metadata) is stored in encrypted form.
If you use KMS keys, you use AWS KMS via the AWS Management Console or AWS KMS APIs to centrally create KMS keys, define the policies that control how KMS keys can be used, and audit their usage to prove that they are being used correctly. You can use these KMS keys to protect your data in Amazon S3 buckets. When you use SSE-KMS encryption with an S3 bucket, the AWS KMS keys must be in the same Region as the bucket. If you want to use a customer managed key for SSE-KMS, create a symmetric encryption customer managed key before you configure SSE-KMS. Then, when you configure SSE-KMS for your bucket, specify the existing customer managed key.
Creating a customer managed key gives you more flexibility and control. For example, you can create, rotate, and disable customer managed keys. You can also define access controls and audit the customer managed key that you use to protect your data.

Using existing on-premises Hardware Security Modules (HSMs) to generate the encryption key materials is essential for regulatory compliance in the financial industry, where strict controls are mandated for handling sensitive data like personally identifiable information (PII) present in the application logs. By generating the key material from their trusted on-premises HSMs and importing it into AWS Key Management Service (KMS), the company can ensure that the encryption keys used to protect their data originate from a secure and compliant source. Furthermore, the capabilities of AWS KMS for key management, provides benefits such as key rotation, auditing, and integration with other AWS services. This allows the company to take advantage of the robust key management features offered by AWS while still maintaining control over the key material generation process. Lastly, by applying an S3 bucket policy that enforces encryption using the KMS key with the imported key material from the on-premises HSMs, the company can ensure that all objects uploaded to the central logging bucket are encrypted, protecting the PII data and meeting regulatory compliance requirements.
Therefore, the correct answer is: Using AWS CLI, create a new KMS key with no key material and use EXTERNAL as the origin of the key. Generate a key from the on-premises HSMs and import it as KMS key using the public key and import token from AWS. Apply an Amazon S3 bucket policy on the central logging bucket to require AWS KMS as the encryption source and deny unencrypted object uploads.
The option that says: Create a new AWS CloudHSM cluster and set it as the key material source in AWS Key Management Service (KMS) when you generate a new KMS key. Set a 1-year duration for the KMS key automatic key rotation. Apply an Amazon S3 bucket policy on the central logging bucket to require AWS KMS as the encryption source and deny unencrypted object uploads is incorrect because it uses an AWS CloudHSM cluster instead of the company's existing on-premises HSMs to generate the key material.
The option that says: Request to provision an AWS Direct Connect connection from the on-premises data center to AWS VPC. Ensure that the network addresses do not overlap. Apply an Amazon S3 bucket policy on the central logging bucket to allow only encrypted object uploads. Configure the application to generate a unique KMS key for each logging event by querying the on-premises HSMs through the Direct Connection network is incorrect because it involves setting up an AWS Direct Connect connection from the on-premises data center to AWS VPC, which may not be necessary if the on-premises HSMs can securely communicate with AWS over the internet. It also requires generating a unique KMS key for each logging event by querying the on-premises HSMs through the Direct Connect network. This approach is not scalable or efficient, as it would result in a large number of KMS keys being created and managed. Lastly, it does not explicitly enforce encryption on the central Amazon S3 bucket using the KMS key with the imported key material from the on-premises HSMs.
The option that says: Using AWS CLI, create a new KMS key with AWS-provided key material and use AWS_KMS as the origin of the key. Overwrite this KMS key with a generated key from the on-premises HSMs by using the public key and import token provided by AWS. Set a 1-year duration for the KMS key automatic key rotation. Apply an Amazon S3 bucket policy on the central logging bucket to require AWS KMS as the encryption source and deny unencrypted object uploads is incorrect because it creates a KMS key with AWS-provided key material (origin set to AWS_KMS) and then overwrites this key material with the key generated from the on-premises HSMs. This approach is not recommended, as overwriting an existing key material can lead to security risks and potential data loss if not handled correctly. It is better to create a new KMS key with no key material (origin set to EXTERNAL) and import the key material from the on-premises HSMs.

References:
https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html
https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html

Check out these AWS KMS and Amazon S3 Cheat Sheets:
https://tutorialsdojo.com/aws-key-management-service-aws-kms/
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q37"></a>

## Q37

A company stores confidential files on an Amazon S3 bucket. There was a recent production incident in the company in which the files that are stored in an S3 bucket were accidentally made public. This has caused data leakage that affected the company revenue. The management has instructed the solutions architect to come up with a solution to safeguard the S3 bucket. The solution should only allow private files to be uploaded to the S3 bucket and no file should have a public read or public write access.

Which of the following options should the solutions architect implement to meet the above requirements with MINIMAL effort?

- **A.** Set up a policy that restricts all s3:PutObject actions of the user to have a private canned ACL only which prohibits any public access to the uploaded objects.
- **B.** Use the s3-bucket-public-read-prohibited and s3-bucket-public-write-prohibited managed rules in AWS Config to restrict all users from uploading publicly accessible and writable files to the S3 bucket.
- **C.** Set up AWS Organizations and create a new Service Control Policy (SCP) that will deny public objects from being uploaded to the Amazon S3 bucket. Attach the SCP to the AWS account.
- **D.** Enable Amazon S3 Block Public Access in the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** only private files, no public read/write, MINIMAL effort

🪤 **Your trap:** An SCP works but is far more effort (and SCPs don't target one bucket)

🧠 **Rule:** Stop public S3 objects with minimal effort → S3 Block Public Access

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 bucket chứa confidential files
   │
   ▼ (đã từng bị set public nhầm → data leak)

Yêu cầu: KHÔNG file nào được public read/write
Điều kiện ràng buộc: MINIMAL EFFORT
```

Đáp án đúng: **D** (S3 Block Public Access). Anh chọn **C** (SCP deny public upload) — `⚠️ Lỗi lặp lại`: đây là nhóm ý "chọn control đơn giản nhất" từng bị sai trước đó; lần này vẫn chọn một giải pháp đúng-về-mặt-kỹ-thuật nhưng SAI vì không phải MINIMAL EFFORT.

#### Vì sao D đúng

**S3 Block Public Access** là một bộ 4 setting độc lập, bật trực tiếp trên bucket (hoặc cả account) trong vài click/một API call:
- Nó **override mọi bucket policy hoặc ACL khác** cho phép public access — bất kể ai set, bất kể cách nào tạo ra permission đó.
- Không cần viết policy JSON, không cần dựng thêm hạ tầng tổ chức nào → đúng nghĩa "minimal effort".

#### Vì sao C (lựa chọn của anh) sai

**Trap:** SCP **có thể** chặn được việc upload public object — về mặt khả năng nó đúng hướng. Nhưng:
- Phải **set up AWS Organizations** (nếu chưa có) + viết SCP + attach vào account — nhiều bước hơn hẳn so với việc chỉ bật 1 setting có sẵn trên S3.
- TD explanation nói rõ: "it still entails a lot of effort to implement... SCP is primarily used to determine what services and actions can be delegated... in the accounts that the SCP is applied to" — SCP là công cụ cấp **account/OU**, không phải công cụ tối ưu cho một bucket cụ thể.
- Đề hỏi **MINIMAL effort** — đây là từ khóa quyết định, không phải "đúng hay sai về mặt kỹ thuật".

#### Các lựa chọn sai khác

- **A:** viết IAM policy ép `s3:PutObject` phải dùng private canned ACL — khả thi nhưng tốn công viết/maintain policy, không đơn giản bằng 1 toggle.
- **B:** AWS Config managed rules (`s3-bucket-public-read-prohibited`, `s3-bucket-public-write-prohibited`) chỉ **phát hiện và báo cáo (notify)**, hoàn toàn **không ngăn chặn (restrict)** việc upload — sai bản chất yêu cầu.

| Option | Ngăn được public access? | Effort | Vấn đề |
|---|---|---|---|
| **D. Block Public Access (đúng)** | Có, override tất cả | Thấp nhất | — |
| A. IAM policy private ACL | Có | Trung bình-cao | Phải viết & duy trì policy |
| B. AWS Config rules | **Không** — chỉ cảnh báo | Thấp | Không restrict được |
| C. SCP (anh chọn) | Có | Cao (cần Organizations) | Không phải minimal effort |

#### Lưu ý thực tế

- Block Public Access có 4 flag độc lập: `BlockPublicAcls`, `IgnorePublicAcls`, `BlockPublicPolicy`, `RestrictPublicBuckets` — có thể set ở cấp bucket hoặc cấp account; nếu account và bucket khác nhau, S3 áp dụng **tổ hợp khắt khe nhất**.
- SCP không tự sai về bản chất — nó chỉ sai *trong ngữ cảnh đề hỏi "minimal effort"*. Nếu đề không có từ khóa effort, SCP vẫn có thể là một lựa chọn hợp lệ ở cấp tổ chức.

#### Quy tắc nhớ cho thi

- **Thấy "MINIMAL effort" + "no public S3 object"** → luôn là **S3 Block Public Access**, không phải SCP/IAM policy/Config rule
- **Thấy AWS Config managed rule cho compliance** → chỉ để **detect/notify**, không bao giờ **restrict/prevent**
- **Thấy SCP cho một bucket cụ thể** → thường là bẫy "đúng nhưng không phải cách đơn giản nhất" (⚠️ lỗi đã lặp lại — luôn soát lại từ khóa effort trước khi chọn SCP)

### TD explanation

Amazon S3 provides Block Public Access settings for buckets and accounts to help you manage public access to Amazon S3 resources. By default, new buckets and objects don't allow public access, but users can modify bucket policies or object permissions to allow public access. Amazon S3 Block Public Access provides settings that override these policies and permissions so that you can limit public access to these resources.
With Amazon S3 Block Public Access, account administrators and bucket owners can easily set up centralized controls to limit public access to their Amazon S3 resources that are enforced regardless of how the resources are created.

Therefore, the correct answer is: Enable Amazon S3 Block Public Access in the S3 bucket. It provides a way to meet the requirements with minimal effort.
When Amazon S3 receives a request to access a bucket or an object, it determines whether the bucket or the bucket owner's account has a Block Public Access setting. If there is an existing Block Public Access setting that prohibits the requested access, then Amazon S3 rejects the request. Amazon S3 Block Public Access provides four settings. These settings are independent and can be used in any combination, and each setting can be applied to a bucket or to an entire AWS account.
If a bucket has Block Public Access settings that are different from its owner's account, Amazon S3 applies the most restrictive combination of the bucket-level and account-level settings. Thus, when Amazon S3 evaluates whether an operation is prohibited by a Block Public Access setting, it rejects any request that would violate either a bucket-level or an account-level setting.
The option that says: Set up a policy that restricts all s3:PutObject actions of the user to have a private canned ACL only which prohibits any public access to the uploaded objects is incorrect. Although this solution is possible, it entails a lot of effort to set up an IAM policy that restricts the user from uploading public objects. Using the Amazon Block Public Access is a more suitable solution for this scenario.
The option that says: Use the s3-bucket-public-read-prohibited and s3-bucket-public-write-prohibited managed rules in AWS Config to restrict all users from uploading publicly accessible and writable files to the S3 bucket is incorrect. This solution with AWS Config will only notify you and your team of public objects in the S3 bucket. It would not be able to restrict any user from uploading public objects.
The option that says: Set up AWS Organizations and create a new Service Control Policy (SCP) that will deny public objects from being uploaded to the Amazon S3 bucket, then attaching the SCP to the AWS account is incorrect. Although you can satisfy the requirement using a service control policy (SCP), it still entails a lot of effort to implement. Remember that the scenario asks you to meet the requirements with minimal effort. Enabling the Amazon S3 Block Public Access in the S3 bucket is still the easiest one to implement. An SCP is primarily used to determine what services and actions can be delegated by administrators to the users and roles in the accounts that the SCP is applied to.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q45"></a>

## Q45

A company runs a finance-related application on a fleet of Amazon EC2 instances inside a private subnet of a VPC in AWS. To access the application, the instances are behind an internet-facing Application Load Balancer (ALB). As part of security compliance, the company is required to have a solution that allows it to inspect network payloads that are being sent to the application. Analyzing the network payloads will help in reverse-engineering sophisticated network attacks that the application may experience.

Which of the following options should the solutions architect implement to meet the company requirements?

- **A.** Go to the Amazon VPC console and create a VPC flow log. Set the destination of flow log data to an Amazon S3 bucket for analysis.
- **B.** Go to the Amazon EC2 console and enable “Access logs” for the ALB. Send the ALB access logs to Amazon AppFlow for payload inspection and to an Amazon S3 bucket for long-term storage.
- **C.** Configure Traffic Mirroring on the elastic network interface of the EC2 instances. Send the mirrored traffic to a monitoring appliance for storage and inspection.
- **D.** Create a new AWS web ACL with blank rules and a default “Allow” action. Associate the ALB to this web ACL. Enable logging on web ACL and send them to Amazon CloudWatch Logs for analysis.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** inspect network payloads, reverse-engineer attacks

🪤 **Your trap:** VPC Flow Logs capture metadata (L3/L4), never packet payloads

🧠 **Rule:** Need packet contents → VPC Traffic Mirroring on the ENIs to a monitoring appliance

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internet ──► ALB (internet-facing) ──► EC2 fleet (private subnet)
                                           │
                                   cần INSPECT PAYLOAD
                                 (nội dung gói tin, không chỉ metadata)
                                 để reverse-engineer attack
```

Đáp án đúng: **C** (VPC Traffic Mirroring → monitoring appliance). Anh chọn **A** (VPC Flow Logs → S3).

#### Vì sao C đúng

```
ENI của EC2 instance
      │  Traffic Mirroring (copy inbound + outbound)
      ▼
Monitoring appliance (EC2 khác, hoặc fleet sau NLB với UDP listener)
      │
      ▼
Content inspection / Threat monitoring / Troubleshooting
```

**Traffic Mirroring copy toàn bộ network traffic** — bao gồm **payload thật** — từ ENI của EC2 sang một appliance giám sát. Đây là cơ chế duy nhất trong 4 lựa chọn thực sự "nhìn thấy" nội dung gói tin, hỗ trợ filter + packet truncation để chỉ lấy traffic cần.

#### Vì sao A (lựa chọn của anh) sai

**Trap:** VPC Flow Logs nghe có vẻ là "log network traffic" nên dễ nhầm là đáp án. Nhưng:
- Flow Logs chỉ chứa thông tin ở **OSI Layer 4 (Transport)** — tức metadata (source/dest IP, port, protocol, bytes, action ACCEPT/REJECT...), **hoàn toàn không có payload**.
- Flow log cấp VPC sẽ log traffic của **toàn bộ VPC**, không riêng cluster EC2 cần giám sát — không đáp ứng đúng phạm vi yêu cầu.

#### Các lựa chọn sai khác

- **B:** ALB access logs chỉ chứa request path + một số header, không có payload; đồng thời Amazon AppFlow dùng để chuyển dữ liệu giữa các ứng dụng SaaS, **không phải tool inspection payload**.
- **D:** AWS WAF web ACL logging gửi CloudWatch Logs chỉ cho thấy chi tiết **request packet** (header, rule match...), không chứa payload gốc; CloudWatch Logs vốn để search/query log, không phải công cụ phân tích payload sâu.

| Option | Có capture payload? | Phạm vi | Vấn đề |
|---|---|---|---|
| **C. Traffic Mirroring (đúng)** | Có — toàn bộ gói tin | Theo ENI chỉ định | — |
| A. VPC Flow Logs | Không — chỉ L4 metadata | Toàn VPC | Thiếu payload, sai phạm vi |
| B. ALB access logs + AppFlow | Không | Request path/headers | AppFlow không dùng để inspect payload |
| D. WAF logging → CloudWatch | Không | Request detail | CloudWatch chỉ để query log, không phải payload |

#### Lưu ý thực tế

- Traffic Mirroring target có thể là EC2 khác hoặc **NLB với UDP listener**; traffic mirror source và target có thể khác VPC nếu nối qua **intra-Region VPC peering hoặc Transit Gateway** (không hỗ trợ cross-region).
- Phân biệt rõ 3 tầng log hay bị nhầm trên exam: Flow Logs (L3/L4 metadata) vs ALB/WAF logs (request detail, không payload) vs Traffic Mirroring (full payload).

#### Quy tắc nhớ cho thi

- **Thấy "inspect network payload" / "reverse-engineer attack content"** → **VPC Traffic Mirroring**, không phải Flow Logs/WAF logs/ALB access logs
- **Thấy "VPC Flow Logs"** → luôn chỉ là metadata L3/L4, không bao giờ có payload
- **Thấy "AppFlow" trong security/monitoring context** → sai, AppFlow là data integration giữa SaaS apps

### TD explanation

Traffic Mirroring is an Amazon VPC feature that you can use to copy network traffic from an elastic network interface of Amazon EC2 instances. You can then send the traffic to out-of-band security and monitoring appliances for:
-Content inspection
-Threat monitoring
-Troubleshooting
The security and monitoring appliances can be deployed as individual instances or as a fleet of instances behind a Network Load Balancer with a UDP listener. Traffic Mirroring supports filters and packet truncation so that you only extract the traffic of interest to monitor by using monitoring tools of your choice.

Traffic Mirroring copies inbound and outbound traffic from the network interfaces that are attached to your Amazon EC2 instances. You can send the mirrored traffic to the network interface of another EC2 instance or a Network Load Balancer that has a UDP listener. The traffic mirror source and the traffic mirror target (monitoring appliance) can be in the same VPC. Or they can be in different VPCs that are connected through intra-Region VPC peering or a transit gateway.
Therefore, the correct answer is: Configure Traffic Mirroring on the elastic network interface of the EC2 instances. Send the mirrored traffic to a monitoring appliance for storage and inspection. Traffic Mirroring can copy network traffic from an elastic network interface and send it to a monitoring appliance for inspection.
The option that says: Go to the Amazon VPC console and create a VPC flow log. Set the destination of flow log data to an Amazon S3 bucket for analysis is incorrect. This will log network data on all resources on the VPC, not just the EC2 cluster in question. Additionally, VPC flow log data only contain OSI Layer 4 (Transport) information. This does not include payload contents.
The option that says: Go to the Amazon EC2 console and enable “Access logs” for the ALB. Send the ALB access logs to Amazon AppFlow for payload inspection and to an Amazon S3 bucket for long-term storage is incorrect. Amazon AppFlow is used for transferring data between Software-as-a-Service (SaaS) applications, not for payload inspection. ALB access logs have similar content to HTTP/HTTPS logs, however, it only contains the request path and some headers on the logs. The payload itself is not recorded.
The option that says: Create a new AWS web ACL with blank rules and a default “Allow” action. Associate the ALB to this web ACL. Enable logging on web ACL and send them to Amazon CloudWatch Logs for analysis is incorrect. You can capture information about the web requests that are evaluated by AWS WAF and send them to AWS CloudWatch Logs. However, CloudWatch Logs is designed for searching and querying logs. You will only see the details of the request packet and not the payload itself. If you need a more sophisticated analysis and inspection of the request payload, it would be better to use a dedicated monitoring appliance.

References:
https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html
https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html
https://docs.aws.amazon.com/vpc/latest/mirroring/tm-example-inbound-tcp.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

<a id="q55"></a>

## Q55

An Amazon partner company plans to host its application on a fleet of Amazon EC2 instances in an Auto Scaling group on a public subnet inside a VPC. A single security group is associated with all the EC2 instances. On a private subnet in the same region, an Amazon Aurora MySQL DB Cluster is created to be accessed by the application. A different security group is associated with the DB Cluster. The solutions architect has been tasked to provide access from the application to the DB Cluster.

Which of the following options is the recommended implementation to meet the application requirements while providing the least-privilege permissions? (Select TWO.)

- **A.** On the Amazon EC2 instances’ security group, create an inbound rule with the source as the DB cluster’s security group using the default Aurora port 3306.
- **B.** On the Amazon EC2 instances’ security group, create an outbound rule with the destination as the DB cluster’s security group using the default Aurora port 3306.
- **C.** On the Amazon Aurora cluster’s security group, create an inbound rule with the source as the Amazon EC2 instances’ security group using the default Aurora port 3306.
- **D.** On the Amazon Aurora cluster’s security group, create an outbound rule with the destination as the Amazon EC2 instances’ security group using the default Aurora port 3306.
- **E.** To restrict communication in a different subnet, update the outbound Network Access Control List (NACL) of the public subnet to allow access to the private subnet CIDR with the default Aurora port 3306.
- **F.** To restrict communication in a different subnet, update the inbound Network Access Control List (NACL) of the private subnet to allow access from the public subnet CIDR with default Aurora port 3306.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C · **You picked:** B, F

🔑 **Key words:** least-privilege, security group per tier, Aurora port 3306

🪤 **Your trap:** A NACL with the public subnet CIDR opens access to every instance in that subnet

🧠 **Rule:** App → DB access: SG-to-SG references (EC2 SG outbound to DB SG; DB SG inbound from EC2 SG)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Public subnet                         Private subnet
┌─────────────────────┐               ┌─────────────────────┐
│ EC2 Auto Scaling     │   kết nối    │ Aurora MySQL         │
│ SG: app-sg           │ ───────────► │ DB Cluster           │
│ (app chủ động mở     │  port 3306   │ SG: db-sg            │
│  connection tới DB)  │               │                      │
└─────────────────────┘               └─────────────────────┘

Yêu cầu: least-privilege, (Select TWO)
```

Đáp án đúng: **B, C**. Anh chọn **B, F** — đúng B nhưng F sai; thiếu C.

#### Hai đáp án đúng ghép thành MỘT giải pháp

```
EC2 (app-sg)  --outbound rule (B): destination = db-sg, port 3306-->  Aurora (db-sg)
                                                                          │
Aurora (db-sg) --inbound rule (C): source = app-sg, port 3306 <---------┘
```

- **B — outbound trên app-sg:** app chủ động mở kết nối (initiate connection) tới DB, nên **app-sg cần outbound rule**, destination là chính **db-sg** (SG-to-SG reference, không phải CIDR).
- **C — inbound trên db-sg:** DB nhận kết nối từ app, nên **db-sg cần inbound rule**, source là **app-sg**.

Hai rule này là **hai mặt của một luồng kết nối duy nhất**: app-sg nói "tôi được phép gửi đi tới db-sg", db-sg nói "tôi chấp nhận request từ app-sg". Thiếu một trong hai, traffic không thông — nhưng vì Security Group là **stateful**, chỉ cần đúng 2 rule này (không cần thêm outbound trên db-sg) là đủ cho cả chiều đi và chiều response.

#### Vì sao F (lựa chọn của anh) sai

**Trap:** F dùng NACL để "restrict communication in a different subnet" — nghe hợp lý vì public/private subnet khác nhau. Nhưng:
- NACL ở đây dùng **source/destination là CIDR của subnet** — tức là **mở quyền truy cập cho TẤT CẢ instance khác trong subnet đó**, không riêng gì các EC2 instance của application. Điều này **vi phạm nguyên tắc least-privilege**.
- TD explanation nhấn mạnh: "you should not use CIDR as this will open the communication from other EC2 instances on the subnet as well. It is recommended to use **security group IDs** for this scenario."
- Đề bài không yêu cầu điều chỉnh NACL — NACL ở trạng thái mặc định (allow all) đã đủ để traffic đi qua, vấn đề cần giải là **giới hạn theo danh tính (SG)**, không phải theo subnet.

#### Các lựa chọn sai khác

- **A:** inbound trên app-sg với source = db-sg — sai chiều; app là bên *initiate* nên cần outbound, không phải inbound.
- **D:** outbound trên db-sg — không cần, vì DB không chủ động kết nối tới app; SG stateful tự cho phép response đi ra theo inbound rule đã match.
- **E:** cùng lỗi như F — dùng CIDR trên NACL, mở rộng quyền ngoài ý muốn cho cả subnet.

| Option | Đúng/Sai | Lý do |
|---|---|---|
| **B (đúng)** | Đúng | Outbound app-sg → db-sg, chiều app initiate |
| **C (đúng)** | Đúng | Inbound db-sg ← app-sg, chiều DB nhận request |
| A | Sai | Sai chiều (inbound thay vì outbound trên app-sg) |
| D | Sai | DB không cần outbound, SG đã stateful |
| E | Sai | NACL + CIDR mở quyền cho cả subnet |
| F (anh chọn) | Sai | NACL + CIDR mở quyền cho cả subnet (cùng lỗi với E) |

#### Lưu ý thực tế

- **SG-to-SG reference** (dùng security group ID làm source/destination) là cách chuẩn để giới hạn theo **tầng ứng dụng** (chỉ đúng nhóm instance), bất kể instance đó đổi IP hay scale thêm.
- NACL hoạt động ở mức **subnet** và chỉ nhận CIDR — không reference được SG ID — nên luôn kém "chính xác" hơn SG khi cần phân quyền theo nhóm tài nguyên cụ thể.

#### Quy tắc nhớ cho thi

- **Thấy "app → DB, least privilege, Select TWO"** → luôn là cặp **SG-to-SG**: outbound trên SG nguồn (app) + inbound trên SG đích (DB)
- **Thấy "NACL + CIDR of subnet" để giới hạn theo nhóm instance cụ thể** → luôn là bẫy, vì mở quyền cho cả subnet
- **Thấy DB cluster SG cần outbound rule** → hầu như luôn sai, vì DB không initiate connection và SG là stateful

### TD explanation

A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.
When you create a VPC, it comes with a default security group. You can create additional security groups for each VPC. You can associate a security group only with resources in the VPC for which it is created. For each security group, you add rules that control the traffic based on protocols and port numbers. There are separate sets of rules for inbound traffic and outbound traffic.
The rules of a security group control the inbound traffic that's allowed to reach the resources that are associated with the security group. The rules also control the outbound traffic that's allowed to leave them.
You can add or remove rules for a security group (also referred to as authorizing or revoking inbound or outbound access). A rule applies either to inbound traffic (ingress) or outbound traffic (egress). You can grant access to a specific source or destination.
Security groups are stateful. For example, if you send a request from an instance, the response traffic for that request is allowed to reach the instance regardless of the inbound security group rules. Responses to allowed inbound traffic are allowed to leave the instance, regardless of the outbound rules.

The option that says: On the Amazon EC2 instances’ security group, create an outbound rule with the destination as the DB cluster’s security group using the default Aurora port 3306 is correct. The application on the EC2 instance will initiate the connection to the DB cluster, thus, an outbound rule is needed on the instances security group with the destination set as the DB cluster security group.
The option that says: On the Amazon Aurora cluster’s security group, create an inbound rule with the source as the Amazon EC2 instances’ security group using the default Aurora port 3306 is correct. The DB cluster will be receiving requests from the EC2 instances, thus, an inbound rule is needed, and the source is the EC2 instances security group.
The option that says: On the Amazon EC2 instances’ security group, create an inbound rule with the source as the DB cluster’s security group using the default Aurora port 3306 is incorrect. The application on the EC2 instance will initiate the connection to the DB cluster, thus, an outbound rule is needed on the instances security group.
The option that says: On the Amazon Aurora cluster’s security group, create an outbound rule with the destination as the Amazon EC2 instances’ security group using the default Aurora port 3306 is incorrect. You don't need to add an outbound rule on the DB security because the DB clusters do not initiate connections. Any request received with the inbound rule will be automatically allowed to reply to the source.
The option that says: To restrict communication in a different subnet, update the outbound Network Access Control List (NACL) of the public subnet to allow access to the private subnet CIDR with the default Aurora port 3306 is incorrect. This may be possible, however, you should not use CIDR as this will open the communication from other EC2 instances on the subnet as well. It is recommended to use security group IDs for this scenario.
The option that says: To restrict communication in a different subnet, update the inbound Network Access Control List (NACL) of the private subnet to allow access from the public subnet CIDR with default Aurora port 3306 is incorrect. This may be possible, however, you should not use CIDR as this will open the communication from other EC2 instances on the subnet as well. It is recommended to use security group IDs for this scenario.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

Check out this Security Group vs. NACL comparison:
https://tutorialsdojo.com/security-group-vs-nacl/

</details>

---

# Group C — Governance, compliance & IAM (5)

<a id="q48"></a>

## Q48

A company is running hundreds of Linux-based Amazon EC2 instances launched with custom AMIs that are dedicated to specific products and services. As part of the security compliance requirements, vulnerability scanning must be done on all EC2 instances wherein each instance must be scanned and pass a Common Vulnerabilities and Exposures (CVE) assessment. Since the development team relies heavily on the custom AMIs for their deployments, the company wants to have an automated process to run the security assessment on any new AMIs and properly tag them before they can be used by the developers. To ensure continuous compliance, the security-approved AMIs must also be scanned every 30 days to check for new vulnerabilities and apply the necessary patches.

Which of the following steps should the Solutions Architect implement to achieve the security requirements? (Select TWO.)

- **A.** Install the AWS Systems Manager (SSM) agent on all EC2 instances. With the agent running, run a detailed CVE assessment scan on the EC2 instances launched from the AMIs that need scanning.
- **B.** Develop a Lambda function that will create automatic approval rules. Create a parameter on AWS SSM Parameter Store to save the list of all security-approved AMI. Set up a 30-day interval cron rule on Amazon EventBridge to trigger an AWS SSM Automation document run on all EC2 instances.
- **C.** Create an Assessment template on Amazon Inspector to target the EC2 instances. Run a detailed CVE assessment scan on all running Amazon EC2 instances launched from the AMIs that need scanning.
- **D.** Write a Lambda function that will create automatic approval rules. Create a parameter on AWS SSM Parameter Store to save the list of all security-approved AMI. Set up a managed rule on AWS Config to continuously scan all running EC2 instances. For any detected vulnerability, run the designated SSM Automation document.
- **E.** Check AWS CloudTrail logs to determine the Amazon EC2 instance IDs that were launched from the AMIs that need scanning. Use AWS Config managed rule to run CVE assessment and remediation on the instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C · **You picked:** C, D

🔑 **Key words:** CVE assessment, new AMIs, rescan every 30 days

🪤 **Your trap:** AWS Config can't scan the OS for CVEs and the requirement is every 30 days, not continuous

🧠 **Rule:** CVE scans → Amazon Inspector; periodic re-checks → EventBridge schedule → SSM Automation

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Custom AMI (Linux) ──► EC2 instances (hàng trăm)
        │
        ├─ Yêu cầu 1: AMI mới ra ──► phải scan CVE + tag trước khi dev dùng
        └─ Yêu cầu 2: AMI đã approved ──► rescan mỗi 30 NGÀY (không phải liên tục)
                                          + tự patch nếu có lỗ hổng mới
```

Đề chọn 2 đáp án. Đúng: **B (Lambda approval + SSM Parameter Store + EventBridge 30-day cron → SSM Automation)** và **C (Amazon Inspector chạy assessment CVE)**. Anh chọn đúng C, sai ở **D (AWS Config quét liên tục)**.

#### C đúng — Amazon Inspector lo phần "quét CVE"

Amazon Inspector có agent cài trong OS, dùng rules package để kiểm tra instance có dính CVE công khai không. Đây là **dịch vụ duy nhất trong danh sách thực sự scan được lỗ hổng ở tầng OS/package** — đúng với "detailed CVE assessment".

#### B đúng — SSM Automation + EventBridge lo phần "rescan mỗi 30 ngày + vá lỗi"

```
EventBridge (cron rate(30 days))
        │
        ▼
SSM Automation document ──► chạy trên EC2 ──► apply patch ──► đóng gói lại AMI
        │
        ▼
Lambda (approval rule) ──► ghi danh sách AMI đã approved vào SSM Parameter Store
```

B khớp đúng tần suất đề cho ("every 30 days") bằng cơ chế lập lịch rõ ràng (EventBridge cron), và SSM Automation document còn làm được việc **patch + tạo lại golden AMI** — khớp "apply the necessary patches".

#### D sai — vì sao giống B nhưng không đúng

D cũng dùng Lambda + Parameter Store (giống B) nhưng thay EventBridge 30-day cron bằng **AWS Config managed rule scan liên tục (continuously)**. Hai vấn đề:

1. **AWS Config không có khả năng scan OS tìm CVE** — Config chỉ theo dõi *cấu hình* resource (AMI ID nào được dùng, tag gì...), không chạy assessment vào bên trong hệ điều hành.
2. Đề yêu cầu rescan **mỗi 30 ngày**, không phải continuous — dùng Config ở đây là sai cả cơ chế lẫn tần suất.

#### Các đáp án khác

| Đáp án | Vấn đề |
|---|---|
| A | SSM Agent chỉ là agent quản lý, **không tự chạy CVE scan** — phải dùng Inspector |
| D | AWS Config không scan OS; yêu cầu là 30-day, không phải continuous |
| E | CloudTrail chỉ ghi log API calls, không giúp xác định CVE; AWS Config vẫn không scan được OS |

#### Lưu ý thực tế

- Amazon Inspector chỉ tạo **assessment template + chạy scan** — không tự động hoá vòng lặp "rescan định kỳ + remediate". Việc lập lịch lại là của **EventBridge + SSM Automation**, nên hai dịch vụ này thường đi cùng nhau trong câu hỏi dạng pipeline bảo trì AMI.
- AWS Config managed rule như `approved-amis-by-id` chỉ kiểm tra **AMI ID instance đang chạy có nằm trong whitelist không**, không liên quan gì đến việc tìm CVE trong AMI đó.

#### Quy tắc nhớ cho thi

- **Thấy "CVE assessment / vulnerability scan"** → **Amazon Inspector** (không phải Config, không phải SSM Agent)
- **Thấy "rescan every N days" / "scheduled"** → **EventBridge cron/rate expression**
- **Thấy "apply patch tự động + đóng gói lại AMI"** → **SSM Automation document**
- **AWS Config** chỉ hợp khi câu hỏi nói về **compliance của config/resource** (ví dụ AMI ID được dùng có hợp lệ không), KHÔNG hợp khi câu hỏi cần soi vào OS tìm lỗ hổng.

### TD explanation

AWS Systems Manager Automation simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. Automation enables you to do the following:
- Build automations to configure and manage instances and AWS resources.
- Create custom runbooks or use pre-defined runbooks maintained by AWS.
- Receive notifications about Automation tasks and runbooks by using Amazon EventBridge.
- Monitor Automation progress and details by using the AWS Systems Manager console.
SSM Automation offers one-click automation for simplifying complex tasks such as creating golden Amazon Machines Images (AMIs) and recovering unreachable EC2 instances. For example, you can use Use the  AWS-UpdateLinuxAmi and  AWS-UpdateWindowsAmi runbooks to create golden AMIs from a source AMI. You can run custom scripts before and after updates are applied. You can also include or exclude specific packages from being installed.

With AWS EventBridge, you can create rules that self-trigger on an automated schedule in EventBridge using cron or rate expressions. Rate expressions are simpler to define but don't offer the fine-grained schedule control that cron expressions support. For example, with a cron expression, you can define a rule that triggers at a specified time on a certain day of each week or month. With this, you can schedule running AWS SSM Automation documents to remediate the vulnerable AMIs.
You can use Amazon Inspector to conduct a detailed scan for CVE in your fleet of EC2 instances. Amazon Inspector offers predefined software called an agent that you can optionally install in the operating system of the EC2 instances that you want to assess. Amazon Inspector also has rules packages that help verify whether the EC2 instances in your assessment targets are exposed to common vulnerabilities and exposures (CVEs). Attacks can exploit unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of your service or data. The CVE system provides a reference method for publicly known information security vulnerabilities and exposures.
The option that says: Develop a Lambda function that will create automatic approval rules. Create a parameter on AWS SSM Parameter Store to save the list of all security-approved AMI. Set up a 30-day interval cron rule on Amazon EventBridge to trigger an AWS SSM Automation document run on all EC2 instances is correct because it satisfies the requirement for updating the security-approved AMI, along with scheduled patches every 30-days using SSM Automation document. AWS SSM Automation can automatically pack AMIs after patches are applied.
The option that says: Create an Assessment template on Amazon Inspector to target the EC2 instances. Run a detailed CVE assessment scan on all running Amazon EC2 instances launched from the AMIs that need scanning is correct because Amazon Inspector can run assessments on target EC2 instances to check if they are exposed to common vulnerabilities and exposures (CVEs).
The option that says: Install the AWS Systems Manager (SSM) agent on all EC2 instances. With the agent running, run a detailed CVE assessment scan on the EC2 instances launched from the AMIs that need scanning is incorrect because the SSM agent cannot run a detailed CVE assessment scan on EC2 instances. You have to use Amazon Inspector to satisfy the given requirement.
The option that says: Write a Lambda function that will create automatic approval rules. Create a parameter on AWS SSM Parameter Store to save the list of all security-approved AMI. Set up a managed rule on AWS Config to continuously scan all running EC2 instances. For any detected vulnerability, run the designated SSM Automation document is incorrect because AWS Config cannot automatically run checks on the operating system of your Amazon EC2 instances. The requirement is to run the assessment every 30-days only and not continuously.
The option that says: Check AWS CloudTrail logs to determine the Amazon EC2 instance IDs that were launched from the AMIs that need scanning. Use AWS Config managed rule to run CVE assessment and remediation on the instances is incorrect. Although it is possible to parse the EC2 instance IDs from CloudTrail and determine the vulnerable instances, you still cannot run the CVE assessment in AWS Config for your Amazon EC2 instances. Using Amazon Inspector is the most suitable service to use in running the CVE assessment.

References:
https://docs.aws.amazon.com/inspector/latest/userguide/inspector_walkthrough.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html
https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduled-events.html

Check out the AWS Systems Manager and AWS Inspector Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/
https://tutorialsdojo.com/amazon-inspector/

</details>

<a id="q60"></a>

## Q60

A company wants to improve the security of its cloud resources by ensuring that all running EC2 instances were launched from pre-approved AMIs only, which are set by the Security team. Their Development team has an agile CI/CD process which should not be stalled by the new automated solution that they’ll implement. Any new application release must be deployed first before the solution could analyze if it is using a pre-approved AMI or not.

Which of the following options enforces the required controls with the LEAST impact on the development process? (Select TWO.)

- **A.** Set up the required policies, roles, and permissions to a centralized IT Operations team, which will manually process the security approval steps to ensure that EC2 instances are only launched from pre-approved AMIs.
- **B.** Set up AWS Config rules to determine any launches of EC2 instances based on non-approved AMIs and then trigger an AWS Lambda function to automatically terminate the instance. Afterward, publish a message to an SNS topic to inform the Security team about the occurrence.
- **C.** Set up a scheduled Lambda function to search through the list of running EC2 instances within your VPC and determine if any of these are based on unauthorized AMIs. Afterward, publish a new message to an SNS topic to inform the Security team that this occurred and then terminate the EC2 instance.
- **D.** Set up IAM policies to restrict the ability of users to launch EC2 instances based on a specific set of pre-approved AMIs which were tagged by the Security team.
- **E.** Set up Amazon Inspector to do regular scans using a custom assessment template to determine if the EC2 instance is based upon a pre-approved AMI. Terminate the instances and inform the Security team by email about the security breach.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C · **You picked:** B, D

🔑 **Key words:** 🔁 should not be stalled, deployed first before analysis, LEAST impact on development

🪤 **Your trap:** 🔁 IAM restriction blocks developers before launch — the stem asks to detect after deployment

🧠 **Rule:** 'Don't block developers' → detect and remediate after launch (Config rule / scheduled Lambda + terminate + SNS)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Security team: "EC2 chỉ được launch từ pre-approved AMI"
Dev team: CI/CD agile, KHÔNG muốn bị chặn (stall)
                │
                ▼
Yêu cầu: app release phải được DEPLOY TRƯỚC, rồi solution mới phân tích
         AMI có approved hay không  →  DETECT SAU KHI ĐÃ LAUNCH, không phải NGĂN TRƯỚC
```

Đề chọn 2 đáp án. Đúng: **B (AWS Config rule + Lambda auto-terminate + SNS)** và **C (scheduled Lambda scan + SNS + terminate)**. Anh chọn đúng B, sai ở **D (IAM policy restrict launch)**.

#### ⚠️ Lỗi lặp lại

Đây là lần thứ 2 anh vấp đúng kiểu bẫy này — **TD Set 1 Q12** cũng là tình huống "không được impede/stall developers" và đáp án đúng cũng là detect + remediate SAU KHI deploy, không phải chặn quyền trước (IAM restriction). Não đang có phản xạ "muốn chặn AMI sai → sửa IAM policy", nhưng đề luôn nói rõ **"should not stall / impede the development process"** — đó là cờ báo hiệu loại bỏ ngay các đáp án mang tính **preventive/blocking** (IAM deny, SCP, bắt buộc review trước khi launch).

**Mnemonic:** *"Deploy first, judge later"* — câu nào có cụm **"deployed first before… analyze"** hoặc **"should not stall CI/CD"** → luôn tìm đáp án dạng **detect-after-launch + auto-remediate**, không bao giờ là IAM/SCP chặn quyền launch.

#### B và C đúng — cùng là "detect sau, remediate sau"

```
B: EC2 launch ──► AWS Config rule (approved-amis-by-id) phát hiện vi phạm
                        │
                        ▼
                Lambda tự terminate instance ──► SNS báo Security team

C: Lambda chạy theo schedule ──► quét toàn bộ EC2 đang chạy trong VPC
                        │
                        ▼
                Tìm AMI không approved ──► SNS báo + terminate
```

Cả hai đều để instance **launch được bình thường** (không chặn CI/CD), rồi mới phát hiện + xử lý — đúng với "LEAST impact on development process".

#### D sai — vì sao đúng hướng (approved AMI) nhưng sai thời điểm

D dùng IAM policy để **chặn user launch instance từ AMI không được approve ngay từ đầu**. Về bảo mật nghe hợp lý, nhưng đề đã nói rõ: *"should not stall... any new application release must be deployed first before the solution could analyze"*. Nghĩa là kiểm tra phải xảy ra **sau** khi đã deploy, không phải **trước**. IAM restriction chặn ngay tại bước launch → vi phạm đúng yêu cầu "LEAST impact on development process" vì nó tạo thêm gate chặn CI/CD.

#### Các đáp án khác

| Đáp án | Vấn đề |
|---|---|
| A | Approval thủ công (manual) bởi IT Ops → chậm, ảnh hưởng CI/CD nhiều hơn cả IAM |
| D | IAM policy chặn trước khi launch → đúng bẫy "stall development" |
| E | Amazon Inspector không có khả năng kiểm tra AMI gốc của instance — chỉ là Config mới làm được (`approved-amis-by-id`) |

#### Lưu ý thực tế

- AWS Config managed rule thật sự dùng cho use case này là **`approved-amis-by-id`** (hoặc by-tag) — chuyên để kiểm tra instance đang chạy có dùng AMI nằm trong whitelist không.
- Amazon Inspector **không** có rules package nào kiểm tra "AMI nguồn gốc" của instance — dễ nhầm vì Inspector cũng hay xuất hiện trong câu hỏi về AMI (như Q48), nhưng ở đó là CVE scan, khác hẳn mục đích ở Q60.

#### Quy tắc nhớ cho thi

- **Thấy "should not stall/impede CI-CD" / "deploy first, analyze after"** → loại ngay IAM/SCP restriction, chọn **detect-after-launch + auto-remediate**
- **"EC2 instance đang chạy dùng AMI không approved"** → **AWS Config rule `approved-amis-by-id`** hoặc **scheduled Lambda scan**
- **IAM policy / SCP** chỉ đúng khi đề **muốn chặn ngay từ đầu** và KHÔNG có yêu cầu giữ tốc độ CI/CD

### TD explanation

When you run your applications on AWS, you usually use AWS resources, which you must create and manage collectively. As the demand for your application keeps growing, so does your need to keep track of your AWS resources. AWS Config is designed to help you oversee your application resources.

AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time. With AWS Config, you can do the following:

 - Evaluate your AWS resource configurations for desired settings.
- Get a snapshot of the current configurations of the supported resources that are associated with your AWS account.
- Retrieve configurations of one or more resources that exist in your account.
- Retrieve historical configurations of one or more resources.
- Receive a notification whenever a resource is created, modified, or deleted.
- View relationships between resources. For example, you might want to find all resources that use a particular security group.

AWS Config provides AWS managed rules, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices. In this scenario, you can use the approved-amis-by-id AWS manage rule which checks whether running instances are using specified AMIs. You can also use a Lambda function which is scheduled to run regularly to scan all of the running EC2 instances in your VPC and check if there is an instance that was launched using an unauthorized AMI. Hence, the following options are the correct answers:
- Set up AWS Config rules to determine any launches of EC2 instances based on non-approved AMIs and then trigger an AWS Lambda function to automatically terminate the instance. Afterward, publish a message to an SNS topic to inform the Security team about the occurrence.
- Set up a scheduled Lambda function to search through the list of running EC2 instances within your VPC and determine if any of these are based on unauthorized AMIs. Afterward, publish a new message to an SNS topic to inform the Security team that this occurred and then terminate the EC2 instance.
The option that says: Set up the required policies, roles, and permissions to a centralized IT Operations team, which will manually process the security approval steps to ensure that EC2 instances are only launched from pre-approved AMIs is incorrect because having manual information security approval will impact the development process. A better solution is to implement an automated process using AWS Config and a scheduled AWS Lambda function.
The option that says: Set up IAM policies to restrict the ability of users to launch EC2 instances based on a specific set of pre-approved AMIs which were tagged by the Security team is incorrect because setting up an IAM Policy will totally restrict the development team from launching EC2 instances with unapproved AMIs which could impact their CI/CD process. The scenario clearly says that the solution should not have any interruption in the company's development process.
The option that says: Set up Amazon Inspector to do regular scans using a custom assessment template to determine if the EC2 instance is based upon a pre-approved AMI. Terminate the instances and inform the Security team by email about the security breach is incorrect because the Amazon Inspector service is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. It does not have the capability to detect EC2 instances that are using unapproved AMIs, unlike AWS Config.

References:
https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-id.html
https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html

Check out this AWS Config Cheat Sheet:
https://tutorialsdojo.com/aws-config/

</details>

<a id="q61"></a>

## Q61

A company has a large Microsoft Windows Server running on a public subnet. There are EC2 instances hosted on a private subnet that allows Remote Desktop Protocol (RDP) connections to the Windows Server via port 3389. These instances enable the Microsoft Administrators to connect to the public servers and troubleshoot any server failures.

The server must always have the latest operating system upgrades to improve security and it must be accessible at any given point in time. The administrators are tasked to refactor the existing solution and manage the server patching activities effectively, even outside the regular maintenance window.

Which of the following provides the LEAST amount of administrative overhead in managing the server?

- **A.** Launch an AWS AppSync environment with a single EC2 instance that runs the Windows Server. Set up the environment with a custom AMI to utilize a hardened machine image that can be downloaded from AWS Marketplace. Configure the AWS Systems Manager Patch Manager to automatically apply the OS updates.
- **B.** Launch the Windows Server on EC2 instances. Use AWS Systems Manager Patch Manager to manage the patching process for the server. Configure it to automatically apply patches as they become available, ensuring that the server is always up-to-date with the latest operating system upgrades.
- **C.** Launch a hardened machine image from the AWS Marketplace and host the server using AWS CloudShell. Set up the AWS Systems Manager Patch Manager to automatically apply system updates. Use Amazon WorkSpaces applications (formerly Amazon AppStream 2.0) to act as a bastion host.
- **D.** Launch the server in Amazon Lightsail with the recommended Amazon AMI. Set up a combination of Amazon EventBridge and AWS Lambda scheduled event to call the Upgrade Operating System API in Lightsail to apply system updates.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** latest OS patches, accessible at any time, LEAST administrative overhead

🪤 **Your trap:** CloudShell is a browser CLI, not a server host; AppStream as bastion adds complexity

🧠 **Rule:** Keep a Windows server patched with low overhead → EC2 + Systems Manager Patch Manager

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Windows Server (public subnet) ◄── RDP (port 3389) ── EC2 private subnet (admin bastion)
        │
        ▼
Yêu cầu: luôn có OS update mới nhất + accessible mọi lúc
         patch phải chạy được NGOÀI maintenance window thông thường
         → tìm giải pháp LEAST administrative overhead
```

Đáp án đúng: **B (EC2 + AWS Systems Manager Patch Manager)**. Anh chọn **C (CloudShell + AppStream làm bastion)**.

#### B đúng — EC2 + Patch Manager là tổ hợp chuẩn cho patching ít overhead

Patch Manager dùng **patch baseline** (auto-approve patch theo số ngày sau khi release, kèm danh sách approved/rejected) và **patch group** để gom instance theo môi trường (dev/test/prod). Việc patch có thể chạy như một **Maintenance Window task**, nên vẫn patch được **ngoài giờ maintenance thông thường** khi cần. Toàn bộ quá trình tự động hoá, không cần can thiệp tay → đúng "LEAST administrative overhead".

#### C sai — vì sao nghe có vẻ hợp lý nhưng không đúng

**AWS CloudShell** chỉ là **shell CLI chạy trên trình duyệt** để tương tác với AWS — nó **không phải dịch vụ host server**, không thể "launch a hardened machine image" lên CloudShell được. Đây là lỗi nhận diện dịch vụ: CloudShell ≠ nơi chạy Windows Server.

Thêm vào đó, dùng **Amazon AppStream 2.0 (Amazon WorkSpaces applications)** làm bastion host là **thừa và phức tạp hơn mức cần thiết** — AppStream là dịch vụ stream ứng dụng/desktop cho end-user, không phải thiết kế để làm bastion. Overhead quản lý cao hơn so với chỉ dùng EC2 + Patch Manager trực tiếp.

#### Các đáp án khác

| Đáp án | Vấn đề |
|---|---|
| A | AWS AppSync là dịch vụ GraphQL API, không liên quan đến việc host EC2/Windows Server |
| C | CloudShell không host được server; AppStream làm bastion là overkill |
| D | Lightsail + tự ghép EventBridge/Lambda gọi Upgrade OS API → nhiều cấu hình tay hơn Patch Manager (vốn đã tự động hoá sẵn) |

#### Lưu ý thực tế

- Patch Manager dùng được cho cả **Linux và Windows** managed node (qua SSM Agent) — không giới hạn OS.
- "Patch ngoài maintenance window thông thường" không có nghĩa là bỏ maintenance window — Patch Manager vẫn có thể **chạy on-demand** hoặc theo baseline auto-approve, không bị khoá cứng vào một khung giờ cố định.
- Điểm học được từ việc từng ôn **patch groups**: patch group chỉ là cách *tổ chức* instance để áp baseline khác nhau theo môi trường — không phải lý do chọn đáp án, lý do chính vẫn là "EC2 + Patch Manager = overhead thấp nhất".

#### Quy tắc nhớ cho thi

- **Thấy "patch Windows/Linux server, overhead thấp nhất"** → **EC2 + Systems Manager Patch Manager** (patch baseline + maintenance window task)
- **CloudShell** → chỉ là CLI trình duyệt, không bao giờ là nơi "host" server
- **AppStream / WorkSpaces applications** → dịch vụ app/desktop streaming cho end-user, không dùng làm bastion host
- **Lightsail + Lambda/EventBridge tự gọi API patch** → luôn nhiều overhead hơn Patch Manager có sẵn trên EC2

### TD explanation

Amazon EC2 is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.
AWS Systems Manager Patch Manager can automate the process of patching managed instances, including both security-related updates and other types of updates. It uses the appropriate built-in mechanism for an operating system type to install updates on a managed node.
Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as optional lists of approved and rejected patches. This ensures that the server is always up-to-date with the latest operating system upgrades.

You can also leverage patch groups to organize instances for patching, such as different environments/tagged instances like development, test, and production.
Furthermore, you can schedule patching to run as a Maintenance Windows task, ensuring that patching activities are managed effectively even outside the regular maintenance window.
This solution would provide the least amount of administrative overhead as it automates the patching process, reducing the need for manual intervention.
Hence, the correct answer is: Launch the Windows Server on EC2 instances. Use AWS Systems Manager Patch Manager to manage the patching process for the server. Configure it to automatically apply patches as they become available, ensuring that the server is always up-to-date with the latest operating system upgrades.
The option that says: Launch an AWS AppSync environment with a single EC2 instance that runs the Windows Server. Set up the environment with a custom AMI to utilize a hardened machine image that can be downloaded from AWS Marketplace. Configure the AWS Systems Manager Patch Manager to automatically apply the OS updates is incorrect because the AWS AppSync service is simply a fully managed service for developing GraphQL APIs, and not for creating an environment with a single Window Server instance.
The option that says: Launch a hardened machine image from the AWS Marketplace and host the server using AWS CloudShell. Set up the AWS Systems Manager Patch Manager to automatically apply system updates. Use Amazon WorkSpaces applications (formerly Amazon AppStream 2.0) to act as a bastion host is incorrect. AWS CloudShell is just a browser-based command-line tool intended for interacting with AWS resources through the CLI. It’s not suitable for hosting a production Windows Server. Additionally, using Amazon AppStream 2.0 as a bastion host adds unnecessary complexity and overhead to the solution. This approach has more administrative overhead compared to using AWS Systems Manager directly on an EC2 instance.
The option that says:  Launch the server in Amazon Lightsail with the recommended Amazon AMI. Set up a combination of Amazon EventBridge and AWS Lambda scheduled event to call the Upgrade Operating System API in Lightsail to apply system updates is incorrect because although Amazon Lightsail is a simplified offering, setting up EventBridge and Lambda to manage operating system updates introduces additional manual configuration and complexity. AWS Systems Manager Patch Manager on EC2 offers a more streamlined and automated solution for patch management, making it a better fit for this requirement.

References:
https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html
https://aws.amazon.com/blogs/mt/patching-your-windows-ec2-instances-using-aws-systems-manager-patch-manager/

Check out this AWS Systems Manager Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q71"></a>

## Q71

A leading insurance firm operates across the AWS Global Infrastructure and has several new members in its development team. The solutions architect was instructed to provision access to certain IAM users who perform application development tasks in the VPC. The access should allow the users to create and configure various AWS resources such as deploying Windows Amazon EC2 servers. In addition, the users should be able to see the permissions in AWS Organizations to view information about the user's organization, including the master account email and organization limitations.

Which of the following should the solutions architect implement to follow the standard security advice of granting the least privilege?

- **A.** Attach the PowerUserAccess AWS managed policy to the IAM users.
- **B.** Attach the AdministratorAccess AWS managed policy to the IAM users.
- **C.** Create a new IAM role and attach the SystemAdministrator AWS managed policy to it. Assign the IAM Role to the IAM users.
- **D.** Create a new IAM role and attach the AdministratorAccess AWS managed policy to it. Assign the IAM Role to the IAM users.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** create/configure resources, view Organizations info, least privilege

🪤 **Your trap:** AdministratorAccess includes IAM and full Organizations control — far beyond least privilege

🧠 **Rule:** Developers who need everything except IAM/user management → PowerUserAccess (also allows organizations:Describe*)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IAM users (dev team mới) cần:
  1. Create/configure AWS resources (deploy Windows EC2...)
  2. Xem thông tin AWS Organizations (master account email, org limitations)
                │
                ▼
        Yêu cầu: LEAST PRIVILEGE
```

Đáp án đúng: **A (attach PowerUserAccess managed policy)**. Anh chọn **D (tạo IAM Role, attach AdministratorAccess)**.

#### A đúng — PowerUserAccess khớp chính xác cả 2 yêu cầu

PowerUserAccess dùng **`NotAction`** để allow **mọi action, mọi resource NGOẠI TRỪ IAM và Organizations** (statement 1), cộng thêm statement 2 cho phép cụ thể:
- tạo **service-linked role** (cần cho một số service truy cập resource ở service khác, ví dụ S3)
- quyền Organizations để **xem** thông tin org (master account email, organization limitations)

```
PowerUserAccess
  Statement 1: NotAction [iam:*, organizations:*] → Allow tất cả còn lại
  Statement 2: Allow iam:CreateServiceLinkedRole + organizations:Describe*
```

Vừa đủ cho "create/configure resources (deploy EC2...)" + "view Organizations info" — không thừa quyền IAM user management hay Organizations full control → đúng nghĩa least privilege.

#### D sai — vì sao "có vẻ cũng làm được" nhưng không least privilege

AdministratorAccess cho **toàn quyền trên mọi service và resource** — bao gồm cả IAM (tạo/sửa/xoá user, role, policy) và toàn quyền Organizations (tạo/xoá account, thay đổi SCP...). Việc gán qua IAM Role hay trực tiếp vào IAM User không làm thay đổi bản chất: đây vẫn là **vượt xa mức cần thiết**. Đề yêu cầu rõ "standard security advice of granting the least privilege" — AdministratorAccess luôn là đáp án sai khi có lựa chọn PowerUserAccess đủ dùng.

#### Các đáp án khác

| Đáp án | Vấn đề |
|---|---|
| B | AdministratorAccess trực tiếp — thừa quyền giống D |
| C | SystemAdministrator managed policy **không có quyền Organizations** để xem master account email/limitations → thiếu một phần yêu cầu |
| D | AdministratorAccess qua Role — thừa quyền, dù gán qua role không bù được việc policy quá rộng |

#### Lưu ý thực tế

- Managed policy **có thể attach trực tiếp vào IAM User** — không bắt buộc phải qua Role. Đề không yêu cầu cross-account hay assume-role, nên việc D "bọc" AdministratorAccess vào một Role mới chỉ làm phức tạp thêm, không giải quyết vấn đề thừa quyền.
- `organizations:Describe*` nằm sẵn trong PowerUserAccess — đây là điểm dễ bị bỏ qua vì tên "Developer Power User" khiến nhiều người nghĩ nó chỉ liên quan application development, không ngờ có luôn quyền xem thông tin Organizations.

#### Quy tắc nhớ cho thi

- **Thấy "create/configure resources" + "least privilege"** → **PowerUserAccess** (not Administrator)
- **PowerUserAccess** = full access trừ **IAM** và **Organizations full control**, nhưng vẫn có **Organizations:Describe*** (view-only) + **iam:CreateServiceLinkedRole**
- **AdministratorAccess** → chỉ chọn khi đề thực sự cần toàn quyền, không có ràng buộc least privilege
- **SystemAdministrator** → không có quyền xem Organizations info

### TD explanation

AWS managed policies for job functions are designed to closely align to common job functions in the IT industry. You can use these policies to easily grant the permissions needed to carry out the tasks expected of someone in a specific job function. These policies consolidate permissions for many services into a single policy that's easier to work with than having permissions scattered across many policies.

There are a lot of available AWS Managed Policies that you can directly attach to your IAM Users, such as Administrator, Billing, Database Administrator, Data Scientist, Developer Power User, Network Administrator, Security Auditor, System Administrator and many others.
For Administrators, you can use the AWS managed policy name: AdministratorAccess if you want to provision full access to a specific IAM User. This will enable the user to delegate permissions to every service and resource in AWS as this policy grants all actions for all AWS services and for all resources in the account.
For Developer Power Users, you can use the AWS managed policy name: PowerUserAccess if you have users who perform application development tasks. This policy will enable them to create and configure resources and services that support AWS aware application development. The first statement of this policy uses the NotAction element to allow all actions for all AWS services and for all resources except AWS Identity and Access Management and AWS Organizations. The second statement grants IAM permissions to create a service-linked role. This is required by some services that must access resources in another service, such as an Amazon S3 bucket. It also grants Organizations permissions to view information about the user's organization, including the master account email and organization limitations.
Therefore, the correct answer is: Attach the PowerUserAccess AWS managed policy to the IAM users.
The options that say: Attach the AdministratorAccess AWS managed policy to the IAM users and Create a new IAM role and attach the AdministratorAccess AWS managed policy to it. Assign the IAM Role to the IAM users are incorrect. Although an AdministratorAccess policy can meet the requirement, it is simply more suitable to attach a PowerUserAccess to the IAM users since this policy can provide the required access. Take note that you have to follow the standard security best practice of granting the least privilege. In addition, a managed policy can be directly attached to your IAM Users, which is one of the reasons why the latter option is incorrect.
The option that says: Create a new IAM role and attach the SystemAdministrator AWS managed policy to it. Assign the IAM Role to the IAM users is incorrect because the SystemAdministrator managed policy typically does not have AWS Organizations permissions to view information about the user's organization, such as the master account email or the organization limitations. In this scenario, you have to use PowerUserAccess instead.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html?shortFooter=true#access_policies_job-functions_create-policies

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q75"></a>

## Q75

A multinational corporation has recently acquired a smaller company. The solutions architect was instructed to consolidate the multiple AWS accounts of both entities using AWS Organizations. The solutions architect has set up the required service control policies (SCPs) to simplify the process of controlling access permissions for each individual account and Organizational Units (OUs). However, one account is having trouble creating a new S3 bucket, and it is required to investigate the cause of this issue. The account has the following SCP attached:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudtrail:*",
      "Resource": "*"
    },
   {
      "Effect": "Allow",
      "Action": "iam:*",
      "Resource": "*"
    }
  ]
}

Each IAM user of the account has the following IAM policy attached:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::*"
             ]
        },
        {
            "Effect": "Deny",
            "NotAction": "s3:*",
            "NotResource": [
                "arn:aws:s3:::*"
            ]
        }
    ]
}

Based on the provided SCP and IAM policy, which of the following options could be the possible root cause of this problem?

- **A.** The SCP is the root cause since it does not explicitly allow the required action that would enable the account to create an S3 bucket.
- **B.** The SCP is the root cause because it does not support whitelisting actions of the AWS resources.
- **C.** The IAM policy is the root cause because you have denied user permissions to execute any S3-related actions.
- **D.** Both the IAM policy and the SCP are the problem. The SCP should explicitly allow S3 bucket creation in its policy and the IAM policy should exactly match the permissions of the SCP.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** SCP allows only cloudtrail:* and iam:*, IAM policy allows s3:*

🪤 **Your trap:** The IAM policy's NotAction Deny doesn't affect S3; the SCP allow list is the blocker

🧠 **Rule:** SCPs never grant: an allow-list SCP must include every action; missing s3:* blocks CreateBucket even if IAM allows it

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
    │
    ▼
Account bị lỗi khi "create S3 bucket"
    │
    ├─ SCP attached vào account:
    │     Allow cloudtrail:*
    │     Allow iam:*
    │     (KHÔNG có s3:* nào trong SCP)
    │
    └─ IAM policy của mọi user trong account:
          Allow s3:*  trên arn:aws:s3:::*
          Deny  NotAction s3:*  trên NotResource arn:aws:s3:::*
```

Đáp án đúng: **A (SCP là root cause vì không explicitly allow S3)**. Anh chọn **C (đổ lỗi cho IAM policy deny S3)**.

#### A đúng — SCP là allow-list, thiếu action nào là mất action đó

Mặc định mỗi root/OU/account có SCP `FullAWSAccess` cho phép tất cả. Khi SA đã **thay SCP này bằng một SCP tuỳ chỉnh** chỉ liệt kê `cloudtrail:*` và `iam:*`, SCP đó trở thành **whitelist**: bất kỳ action nào không nằm trong danh sách — kể cả `s3:CreateBucket` — sẽ bị **implicit deny** ở tầng Organizations, **trước khi** IAM policy của user được xét tới.

```
Request: s3:CreateBucket
    │
    ▼
SCP checkpoint: Action có trong {cloudtrail:*, iam:*}? → KHÔNG → DENY (implicit)
    │
    ▼ (không bao giờ tới đây)
IAM policy checkpoint: Allow s3:*  →  (vô nghĩa, SCP đã chặn từ trước)
```

**Nguyên tắc cốt lõi:** SCP **không bao giờ cấp quyền (grant)** — nó chỉ set **giới hạn trần (maximum permissions)**. Một hành động phải được **cả SCP và IAM policy cùng allow** mới thực thi được. SCP ở đây không chặn S3 một cách chủ động — nó chỉ đơn giản là **không nhắc đến S3**, nên S3 rơi vào vùng implicit deny.

#### C sai — đọc kỹ IAM policy để thấy Deny không đụng tới S3

IAM policy có 2 statement:

1. **Allow `s3:*`** trên `arn:aws:s3:::*` — cho phép mọi action S3.
2. **Deny** với **`NotAction: s3:*`** trên **`NotResource: arn:aws:s3:::*`**.

`NotAction`/`NotResource` là phần tử nâng cao, nghĩa là **"match mọi thứ NGOẠI TRỪ cái được liệt kê"**. Vậy statement 2 đọc là: *Deny mọi action KHÔNG PHẢI s3:\*, trên mọi resource KHÔNG PHẢI s3 bucket/object*. Nói cách khác, statement này chặn **các action không phải S3 trên các resource không phải S3** — nó **không hề đụng đến quyền S3** nào cả. Vì vậy IAM policy tự nó **cho phép đầy đủ** `s3:CreateBucket` — IAM không phải là vấn đề.

#### Các đáp án khác

| Đáp án | Vấn đề |
|---|---|
| B | Sai về bản chất SCP — SCP **hoàn toàn hỗ trợ** whitelist action (đây chính là cách hoạt động mặc định khi thay FullAWSAccess) |
| C | Đọc nhầm `NotAction`/`NotResource`: Deny đó không chạm vào S3 |
| D | Sai ở phần "IAM policy phải match chính xác SCP" — SCP chỉ là giới hạn trần, IAM policy không cần khớp 1:1 với SCP, chỉ cần nằm trong phạm vi SCP cho phép |

#### ⚠️ Lỗi lặp lại

Đây là lần thứ 3 anh vấp bẫy "SCP vs IAM policy" (đã từng sai 2 lần ở **TD Set 2**). Mẫu số chung: khi đề cho **cả SCP và IAM policy cùng lúc**, phản xạ hay đổ lỗi cho statement "Deny" trong IAM policy vì nó *nhìn* giống nguyên nhân rõ ràng nhất — nhưng thực chất cần kiểm tra **SCP trước tiên** vì SCP là **rào chắn ngoài cùng**: thiếu allow ở SCP thì IAM allow cũng vô dụng.

**Mnemonic:** *"SCP = cổng ngoài, IAM = cổng trong — cổng ngoài đóng thì cổng trong mở cũng vô ích."* Mỗi khi thấy SCP dạng allow-list (không có `FullAWSAccess`), việc đầu tiên là **check SCP có list đủ action cần dùng chưa**, rồi mới soi tới IAM policy.

#### Lưu ý thực tế

- SCP không áp dụng cho **management account** của Organization — chỉ áp dụng cho **member account**.
- Hiệu lực cuối cùng = **giao (intersection)** giữa SCP (mọi cấp: root → OU → account) và IAM policy — không phải hợp (union). Thiếu allow ở bất kỳ cấp nào trong chuỗi SCP là đủ để chặn.

#### Quy tắc nhớ cho thi

- **Thấy SCP dạng allow-list (đã thay FullAWSAccess)** → kiểm tra SCP có đủ action cần dùng không, **trước khi** nghi ngờ IAM policy
- **SCP không bao giờ grant** — chỉ set permission boundary; quyền thật phải đến từ IAM policy
- **`NotAction` / `NotResource`** → đọc kỹ là "match mọi thứ TRỪ cái liệt kê", đừng vội kết luận nó chặn đúng cái đang bị hỏi
- **IAM policy không cần khớp 1:1 với SCP** — chỉ cần nằm trong giới hạn SCP cho phép

### TD explanation

A service control policy (SCP) is a policy that specifies the services and actions that users and roles can use in the specified AWS accounts. SCPs are similar to IAM permission policies except that they don't grant any permissions. Instead, SCPs specify the maximum permissions for an organization, organizational unit (OU), or account. When you attach an SCP to your organization root or an OU, the SCP limits permissions for entities in member accounts. Even if a user is granted full administrator permissions with an IAM permission policy, any access that is not explicitly allowed or that is explicitly denied by the SCPs affecting that account is blocked.
For example, if you assign an SCP that allows only database service access to your "database" account, then any user, group, or role in that account is denied access to any other service's operations. SCPs are available only when you enable all features in your organization.

By default, an SCP named FullAWSAccess is attached to every root, OU, and account. This default SCP allows all actions and all services. So in a new organization, until you start creating or manipulating the SCPs, all of your existing IAM permissions continue to operate as they did. As soon as you apply a new or modified SCP to a root or OU that contains an account, the permissions that your users have in that account become filtered by the SCP. Permissions that used to work might now be denied if they're not allowed by the SCP at every level of the hierarchy down to the specified account.
Therefore, the correct answer is: The SCP is the root cause since it does not explicitly allow the required action that would enable the account to create an S3 bucket. The default service policy was changed which means that you would need to explicitly allow your account access to S3 to be able to create buckets. By removing the default FullAWSAccess SCP, all actions for all services are now implicitly denied. To use SCPs as a whitelist, you must replace the AWS-managed FullAWSAccess SCP with an SCP that explicitly permits only those services and actions that you want to allow. Your custom SCP then overrides the implicit Deny with an explicit Allow for only those actions that you want to permit.
The option that says: The SCP is the root cause because it does not support whitelisting actions of the AWS resources is incorrect. The SCP format is correct, and it definitely does support the whitelisting feature.
The option that says: The IAM policy is the root cause because you have denied user permissions to execute any S3-related actions is incorrect. The IAM policy allows the user to perform all actions under Amazon S3. The included Deny policy only affects actions on AWS resources that are not of S3, and therefore, should not hinder you from creating S3 buckets. Take note that the NotAction/NotResource is an advanced policy element that explicitly matches everything except the list of action/resources that you specified.
The option that says: Both the IAM policy and the SCP are the problem. The SCP should explicitly allow S3 bucket creation in its policy and the IAM policy should exactly match the permissions of the SCP is incorrect. The IAM policy does not necessarily need to match the service control policy. Although it is true that you would have to explicitly allow S3 bucket creation on the SCP, an SCP does not grant any permissions. Users and roles must still be granted permissions with appropriate IAM permission policies. A user without any IAM permission policies has no access at all, even if the applicable SCPs allow all services and all actions.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_deny-except-bucket.html

Service Control Policies (SCP) vs IAM Policies:
https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

</details>

---

# Group D — Edge, TLS & API auth (4)

<a id="q7"></a>

## Q7

A company is running a serverless backend API service on AWS. It has several AWS Lambda functions written in Python and an Amazon API Gateway that is configured to invoke the functions. The company wants to secure the API endpoint by ensuring that only authorized IAM users or roles can access the Amazon API Gateway endpoint. The Solutions Architect was also tasked to provide the ability to inspect each request end-to-end to check the latency of the request and to generate service maps.

Which of the following implementation will fulfill the above company requirements?

- **A.** Configure authorization to use AWS_IAM for the API Gateway method. Create the IAM users or roles that have the execute-api:Invoke permission to the ARN of the API resource. Enable request signing with AWS Signature for every call to the API endpoint. Trace and analyze each user request on API Gateway by using AWS X-Ray.
- **B.** Ensure that the API Gateway resource is secured by only returning the company’s domain in Access-Control-Allow-Origin headers and enabling Cross-origin resource sharing (CORS). Create the IAM users or roles that have the execute-api:Invoke permission to the ARN of the API resource. Trace and analyze each user request on API Gateway using Amazon CloudWatch Logs.
- **C.** Write a separate AWS Lambda function that will act as a custom authorizer. For every call to the API gateway, require the client to pass the access key and secret key. Use the Lambda function to validate the key/secret pair against a valid IAM user. Trace and analyze each user request on API Gateway by using AWS X-Ray.
- **D.** Generate a new client certificate on Amazon API Gateway. Distribute this certificate to all AWS users or roles that require access to the API endpoint. Ensure that each user will pass the client certification for every request made to the API endpoint. Trace and analyze each user request on API Gateway using Amazon CloudWatch Logs.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** only authorized IAM users or roles, inspect each request end-to-end, service maps

🪤 **Your trap:** CORS is a browser rule, not authentication; CloudWatch Logs don't give end-to-end traces

🧠 **Rule:** API Gateway + IAM principals → AWS_IAM authorization (SigV4); latency + service map → X-Ray

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client (IAM user/role)              API Gateway              Lambda (Python)
      │  SigV4-signed request            │                         │
      └──────────────────────────────────►                         │
                                          │  invoke                 │
                                          └─────────────────────────►
Yêu cầu:
  1) Chỉ IAM user/role được phép mới gọi được API
  2) Inspect request END-TO-END: đo latency + vẽ service map
```

Đáp án đúng: **A** (AWS_IAM authorization + SigV4 + X-Ray). Anh chọn **B** (CORS + CloudWatch Logs) — sai cả hai phần: CORS không xác thực ai, CloudWatch Logs không vẽ được service map.

#### A đúng — vì sao khớp đúng 2 yêu cầu

**Phần xác thực (IAM user/role):** API Gateway hỗ trợ nhiều cơ chế auth (resource policy, AWS_IAM, Lambda authorizer, Cognito user pools). Khi yêu cầu là "chỉ IAM principal được invoke", cơ chế đúng là **AWS_IAM authorization**:

```
Settings > Authorization > AWS_IAM
    → tạo IAM policy cho phép action "execute-api:Invoke"
      trên ARN của API resource
    → attach policy vào IAM user/role cần quyền
    → mỗi request phải ký bằng AWS Signature Version 4 (SigV4)
```

SigV4 chính là cơ chế API Gateway dùng để xác minh request thực sự đến từ IAM principal được cấp quyền — không cần code custom nào.

**Phần end-to-end trace + service map:** đây đúng là định nghĩa của **AWS X-Ray** — "provides an end-to-end view of requests as they travel through your application, and shows a map of your application's underlying components."

#### Vì sao B (lựa chọn của Anh) sai

- **CORS không phải authentication.** CORS chỉ là rule của browser kiểm soát domain nào được gọi fetch/XHR tới API — không xác minh IAM identity, ai cũng gọi được nếu có đúng origin header. Phần "IAM users/roles có execute-api:Invoke" trong B tự mâu thuẫn: B không nói cách nào để *bắt buộc* request phải được ký bằng IAM, nên policy đó vô nghĩa nếu không có AWS_IAM authorizer.
- **CloudWatch Logs chỉ là execution log**, dùng để monitoring/debug — không có khái niệm trace xuyên suốt nhiều service hay service map. Để có latency breakdown + map, phải dùng X-Ray.

#### Các lựa chọn sai khác

- **C — Lambda custom authorizer với access key/secret key:** vừa tốn công hơn AWS_IAM, vừa gửi access/secret key qua mỗi HTTPS call là **rủi ro bảo mật** (credential tĩnh đi trên wire). Không cần thiết khi AWS_IAM authorizer đã có sẵn.
- **D — client certificate + CloudWatch Logs:** client cert xác thực kết nối TLS mutual, không liên quan IAM identity; và vẫn vướng vấn đề CloudWatch Logs không end-to-end trace.

| Lựa chọn | Auth đúng loại? | End-to-end trace đúng loại? |
|---|---|---|
| **A. AWS_IAM + SigV4 + X-Ray** | Đúng | Đúng |
| B. CORS + CloudWatch Logs | Sai (CORS ≠ auth) | Sai (logs ≠ trace) |
| C. Custom authorizer + key/secret + X-Ray | Thừa + lộ key | Đúng |
| D. Client cert + CloudWatch Logs | Sai loại auth | Sai |

#### Lưu ý thực tế

- AWS_IAM authorization yêu cầu request phải **ký SigV4** — SDK AWS tự làm việc này khi gọi API Gateway bằng IAM credentials; nếu gọi bằng curl thô phải tự ký.
- Resource policy, Lambda authorizer, Cognito user pools là các lựa chọn auth khác của API Gateway nhưng không khớp "IAM users or roles" trực tiếp như AWS_IAM.

#### Quy tắc nhớ cho thi

- **Thấy "chỉ IAM user/role được invoke API Gateway"** → **AWS_IAM authorization + SigV4**
- **Thấy "end-to-end trace / latency / service map"** → **AWS X-Ray**, không phải CloudWatch Logs
- **Thấy "CORS"** → chỉ là browser same-origin rule, **không bao giờ** là authentication
- **Thấy "gửi access key/secret key qua request"** → luôn là trap bảo mật, loại ngay

### TD explanation

API Gateway supports multiple mechanisms for controlling and managing access to your API.
You can use the following mechanisms for authentication and authorization:

Resource policies let you create resource-based policies to allow or deny access to your APIs and methods from specified source IP addresses or VPC endpoints.
Standard AWS IAM roles and policies offer flexible and robust access controls that can be applied to an entire API or individual methods. IAM roles and policies can be used for controlling who can create and manage your APIs, as well as who can invoke them.
IAM tags can be used together with IAM policies to control access.
Endpoint policies for interface VPC endpoints allow you to attach IAM resource policies to interface VPC endpoints to improve the security of your private APIs.
Lambda authorizers are Lambda functions that control access to REST API methods using bearer token authentication—as well as information described by headers, paths, query strings, stage variables, or context variables request parameters. Lambda authorizers are used to control who can invoke REST API methods.
Amazon Cognito user pools let you create customizable authentication and authorization solutions for your REST APIs. Amazon Cognito user pools are used to control who can invoke REST API methods.

You can enable IAM authentication for an API method in the API Gateway console. Then, you can use IAM policies and resource policies to designate permissions for your API's users. Here are the general steps to implement this:

In the API Gateway console, enable IAM authentication for your API method by going to Settings > Authorization, and choosing AWS_IAM.
Deploy the API to ensure the changes are applied.
Grant API authorization to a group of IAM users by creating an IAM policy document with the required permissions.
For the IAM policy, ensure that it allows the execute-api:Invoke action and the resource is set to the ARN of the API gateway method.
Attach this policy to the required IAM users or IAM roles.

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. AWS X-Ray provides an end-to-end view of requests as they travel through your application, and shows a map of your application’s underlying components. You can use X-Ray to analyze both applications in development and in production, from simple three-tier applications to complex microservices applications consisting of thousands of services.
Therefore, the correct answer is: Configure authorization to use AWS_IAM for the API Gateway method. Create the IAM users or roles that have the execute-api:Invoke permission to the ARN of the API resource. Enable request signing with AWS Signature for every call to the API endpoint. Trace and analyze each user request on API Gateway by using AWS X-Ray.
The option that says: Ensure that the API Gateway resource is secured by only returning the company’s domain in Access-Control-Allow-Origin headers and enabling Cross-origin resource sharing (CORS). Create the IAM users or roles that have the execute-api:Invoke permission to the ARN of the API resource. Trace and analyze each user request on API Gateway using Amazon CloudWatch Logs is incorrect because CORS does not provide any IAM authentication capability. Although API Gateway can send execution logs to CloudWatch Logs, you can only view the logs with it for monitoring purposes. It does not provide end-to-end tracing or inspection for the request.
The option that says: Write a separate AWS Lambda function that will act as a custom authorizer. For every call to the API gateway, require the client to pass the access key and secret key. Use the Lambda function to validate the key/secret pair against a valid IAM user. Trace and analyze each user request on API Gateway by using AWS X-Ray is incorrect. Creating a custom Lambda authorizer will require more work compared to just using the AWS_IAM authorizer. Sending AWS access and secret key as part of each HTTPS call is not recommended from a security standpoint since these are sensitive security credentials.
The option that says: Generate a new client certificate on Amazon API Gateway. Distribute this certificate to all AWS users or roles that require access to the API endpoint. Ensure that each user will pass the client certification for every request made to the API endpoint. Trace and analyze each user request on API Gateway using Amazon CloudWatch Logs is incorrect. Using client certificates for authentication does not provide any IAM authentication capability and although API Gateway can send execution logs to CloudWatch Logs, the logs do not provide end-to-end tracing or inspection for request.

References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-iam-policy-examples-for-api-execution.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html
https://aws.amazon.com/premiumsupport/knowledge-center/iam-authentication-api-gateway/

Check out the AWS X-Ray and Amazon API Gateway Cheat Sheets:
https://tutorialsdojo.com/amazon-api-gateway/
https://tutorialsdojo.com/aws-x-ray/

</details>

<a id="q10"></a>

## Q10

A company runs a suite of web applications in AWS. The application is hosted in an Auto Scaling group of On-Demand Amazon EC2 instances behind an Application Load Balancer that handles traffic from multiple web domains. The solutions architect is responsible for securing the system by allowing multiple domains to serve SSL traffic without the need to re-authenticate and re-provision a new certificate whenever a new domain name is added. This change of architecture from HTTP to HTTPS will help improve the SEO and Google search ranking of the web application.

Which of the following options are valid solutions to meet the above requirements? (Select TWO.)

- **A.** Use a wildcard certificate to handle multiple sub-domains and different domains.
- **B.** Add a Subject Alternative Name (SAN) for each additional domain to your certificate.
- **C.** Create a new CloudFront web distribution and configure it to serve HTTPS requests using dedicated IP addresses in order to associate your alternate domain names with a dedicated IP address in each CloudFront edge location.
- **D.** Upload all SSL certificates of the domains in the ALB using the console and bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client using Server Name Indication (SNI).
- **E.** Use a Gateway Load Balancer instead of an Application Load Balancer. Upload all SSL certificates of the domains and use Server Name Indication (SNI).

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D · **You picked:** A, D

🔑 **Key words:** multiple domains, no re-provisioning when a new domain is added

🪤 **Your trap:** A wildcard cert covers sub-domains of one domain, not different domains

🧠 **Rule:** Many domains on one ALB → multiple certs on one listener (SNI); or CloudFront with dedicated-IP custom SSL

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ALB phục vụ nhiều domain khác nhau (không phải sub-domain của 1 domain)
                 │
   HTTP ──► phải chuyển HTTPS, KHÔNG được re-provision cert
            mỗi khi thêm domain mới
```

Yêu cầu multi-select (2 đáp án). Đáp án đúng: **C, D** (CloudFront dedicated-IP custom SSL + ALB multi-cert qua SNI). Anh chọn **A, D** — đúng D, sai A (wildcard cert).

#### D đúng — SNI trên ALB

```
ALB secure listener (443)
   ├── Cert 1: domain-a.com
   ├── Cert 2: domain-b.com
   └── Cert 3: domain-c.com
        (tất cả bind vào CÙNG MỘT listener)

Lúc client connect: gửi SNI extension chứa hostname
   → ALB tự chọn cert phù hợp, miễn phí, không cần cấu hình thêm
```

Mỗi khi thêm domain mới: chỉ **upload thêm 1 cert vào listener đó**, không cần làm lại/re-provision các cert cũ — đúng yêu cầu "no re-authenticate, no re-provision khi thêm domain".

#### C đúng — CloudFront dedicated-IP custom SSL

TD explanation: "If you configure CloudFront to serve HTTPS requests using SNI, CloudFront associates your alternate domain name with an IP address for each edge location." CloudFront hỗ trợ gắn **nhiều alternate domain name**, mỗi domain có cert riêng, phục vụ cùng cơ chế SNI tại edge location — tương tự ALB nhưng ở tầng CDN.

#### A (Anh chọn) sai — vì sao trông hợp lý nhưng thực ra không

Wildcard certificate (ví dụ `*.example.com`) nghe có vẻ "linh hoạt cho nhiều domain", nhưng **wildcard chỉ bao phủ các sub-domain của MỘT domain gốc** (`a.example.com`, `b.example.com`), **không** bao phủ domain hoàn toàn khác tên (`example.com` vs `another-site.com`). Đề bài nói "multiple web domains" — tức các domain khác nhau, không phải sub-domain — nên wildcard không giải quyết được bài toán.

#### B và E sai

- **B — SAN (Subject Alternative Name) cho mỗi domain mới:** kỹ thuật đúng là có thể gộp nhiều domain vào 1 cert qua SAN, nhưng **mỗi lần thêm domain mới vẫn phải re-issue lại cert đó** → vi phạm đúng yêu cầu "không cần re-authenticate/re-provision".
- **E — Gateway Load Balancer + SNI:** GWLB là loại load balancer cho network appliance (firewall, IDS/IPS), **không hỗ trợ SNI** hay TLS termination kiểu ALB.

| Lựa chọn | Nhiều domain khác nhau? | Không cần re-provision khi thêm domain? |
|---|---|---|
| **C. CloudFront dedicated-IP SNI** | Có | Có |
| **D. ALB multi-cert qua SNI** | Có | Có |
| A. Wildcard cert | Không (chỉ sub-domain) | — |
| B. SAN | Có | Không (phải re-issue) |
| E. GWLB + SNI | — | GWLB không hỗ trợ SNI |

#### Lưu ý thực tế

- SNI trên ALB và CloudFront đều **miễn phí**, không phụ thuộc số lượng cert gắn vào.
- Phân biệt: **SNI Custom SSL** (CloudFront, nhiều domain chia sẻ IP theo edge) vs **Dedicated IP Custom SSL** (1 domain/1 IP riêng, dùng khi client cũ không hỗ trợ SNI) — đề bài này match với cơ chế SNI dùng IP theo edge location.

#### Quy tắc nhớ cho thi

- **Thấy "wildcard certificate"** → chỉ dùng cho sub-domain CÙNG domain gốc, **không** dùng cho domain khác tên
- **Thấy "nhiều domain + không re-provision khi thêm domain mới"** → **SNI** (multi-cert trên 1 listener/edge), không phải SAN
- **Thấy "SAN"** → đúng về mặt kỹ thuật nhưng vẫn phải re-issue cert mỗi lần thêm domain → sai nếu đề cấm re-provision
- **Thấy "Gateway Load Balancer"** → không hỗ trợ SNI/TLS termination kiểu ALB, dùng cho network appliance

### TD explanation

SNI Custom SSL relies on the SNI extension of the Transport Layer Security protocol, which allows multiple domains to serve SSL traffic over the same IP address by including the hostname to which the viewers are trying to connect.
You can host multiple TLS-secured applications, each with its own TLS certificate, behind a single load balancer. In order to use SNI, all you need to do is bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client. These features are provided at no additional charge.

You can use your own SSL certificates with Amazon CloudFront at no additional charge with Server Name Indication (SNI) Custom SSL. Most modern browsers support SNI and provide an efficient way to deliver content over HTTPS using your own domain and SSL certificate. Amazon CloudFront delivers your content from each edge location and offers the same security as the Dedicated IP Custom SSL feature.
The option that says: Upload all SSL certificates of the domains in the ALB using the console and bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client using Server Name Indication (SNI) is correct. You can upload all SSL certificates of the domains in the ALB using the console and bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client using Server Name Indication (SNI).
The option that says: Create a new CloudFront web distribution and configure it to serve HTTPS requests using dedicated IP addresses in order to associate your alternate domain names with a dedicated IP address in each CloudFront edge location is correct. You can configure Amazon CloudFront to require viewers to interact with your content over an HTTPS connection using the HTTP to HTTPS Redirect feature. If you configure CloudFront to serve HTTPS requests using SNI, CloudFront associates your alternate domain name with an IP address for each edge location. The IP address to your domain name is determined during the SSL/TLS handshake negotiation and isn’t dedicated to your distribution.

The option that says: Use a wildcard certificate to handle multiple sub-domains and different domains is incorrect. A wildcard certificate can only handle multiple sub-domains but not different domain names.
The option that says: Add a Subject Alternative Name (SAN) for each additional domain to your certificate is incorrect. Although using Subject Alternative Name (SAN) is correct, you will still have to reauthenticate and reprovision your certificate every time you add a new domain. One of the requirements in the scenario is that you should not have to reauthenticate and reprovision your certificate; hence, this solution is incorrect.
The option that says: Use a Gateway Load Balancer instead of an Application Load Balancer. Upload all SSL certificates of the domains and use Server Name Indication (SNI) is incorrect because a Gateway Load Balancer does not support SNI.

References:
https://aws.amazon.com/blogs/aws/new-application-load-balancer-sni/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-https-dedicated-ip-or-sni.html#cnames-https-dedicated-ip
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

SNI Custom SSL vs Dedicated IP Custom SSL:
https://tutorialsdojo.com/sni-custom-ssl-vs-dedicated-ip-custom-ssl/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services/

</details>

<a id="q23"></a>

## Q23

The www.tutorialsdojonews.com website is using the WordPress platform that runs on a fleet of Amazon EC2 instances behind an application load balancer to deliver news around the globe. There are a lot of customers complaining about the slow loading time of the website. The solutions architect has created a CloudFront distribution and set the ALB as the origin to improve the read performance. After several days, the IT Security team reported that the setup is not secure and it should enable end-to-end HTTPS connections from the user's browser to the origin via CloudFront.

Which of the following options should the solutions architect implement to satisfy the above requirements?

- **A.** Use third-party CA certificate on both the origin and CloudFront.
- **B.** Use a self-signed certificate in both the origin and CloudFront.
- **C.** Configure the CloudFront distribution to redirect HTTP to HTTPS protocol. Generate a new SSL certificate on AWS Certificate Manager and use it as the CloudFront distribution and origin certificate.
- **D.** Configure CloudFront to use its default certificate. Configure the CloudFront distribution to redirect HTTP to HTTPS protocol. For the origin, generate a new SSL certificate on AWS Certificate Manager.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** custom domain, end-to-end HTTPS from browser to origin

🪤 **Your trap:** The CloudFront default certificate only works for *.cloudfront.net, not a custom domain

🧠 **Rule:** Custom domain on CloudFront → ACM cert on CloudFront (us-east-1) + HTTPS to the origin with a matching cert

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Browser ──HTTPS──► CloudFront ──HTTPS──► ALB (EC2 WordPress)
                 www.tutorialsdojonews.com   (custom origin)
         ↑ custom domain, KHÔNG phải *.cloudfront.net
Yêu cầu: end-to-end HTTPS, bảo mật đúng chuẩn
```

Đáp án đúng: **C** (ACM cert dùng chung cho cả CloudFront distribution và origin). Anh chọn **D** (dùng default CloudFront certificate) — sai vì distribution này gắn **custom domain**.

#### C đúng — vì sao ACM cert khớp cả hai chặng

TD explanation chia rõ 2 chặng HTTPS độc lập của CloudFront:

```
Chặng 1: Viewer ──HTTPS──► CloudFront
    → cert: ACM, hoặc third-party CA

Chặng 2: CloudFront ──HTTPS──► Origin (ALB)
    → nếu origin LÀ ELB load balancer: ACM cũng dùng được
    → nếu origin là EC2 trần (không qua ELB): phải dùng cert third-party CA
```

Ở đây origin là **ALB** (một loại ELB) → ACM cert hợp lệ cho cả hai chặng. Vì vậy "generate một ACM cert, dùng chung cho CloudFront distribution và origin" vừa đúng kỹ thuật vừa tiết kiệm (ACM miễn phí + auto-renew), đồng thời phải **redirect HTTP → HTTPS** trên CloudFront để đảm bảo toàn bộ traffic viewer đi qua HTTPS.

#### D (Anh chọn) sai — điểm quyết định: custom domain vs *.cloudfront.net

**Đây là điểm mấu chốt phân biệt với Q50 (trông có vẻ mâu thuẫn nhưng không phải):**

```
Q23: domain = www.tutorialsdojonews.com   → CUSTOM domain
Q50: domain = dtut0r1al5doj0.cloudfront.net → domain MẶC ĐỊNH của CloudFront
```

CloudFront's default certificate **chỉ valid cho chính domain `*.cloudfront.net`** mà CloudFront tự cấp cho distribution — nó không bao giờ bao phủ một custom domain như `www.tutorialsdojonews.com`. TD explanation nói rõ: *"you cannot use the default certificate in CloudFront since the website is using a custom domain."* Vì đề bài gắn custom domain, default cert là vô hiệu — bắt buộc phải có ACM cert phát hành (hoặc import) riêng cho domain đó.

#### Các lựa chọn sai khác

- **A — third-party CA cho cả hai chặng:** về mặt kỹ thuật khả thi (origin là ALB vẫn chấp nhận third-party cert), nhưng **không tối ưu** vì ACM miễn phí và tự renew — "incorrect" ở đây mang nghĩa "không phải lựa chọn tốt nhất", không phải sai hoàn toàn về bảo mật.
- **B — self-signed certificate cả hai chặng:** sai vì origin yêu cầu cert từ CA được tin cậy (trusted CA); self-signed không đáp ứng.

| Lựa chọn | Domain loại gì phù hợp | Vấn đề |
|---|---|---|
| **C. ACM cert cho cả CloudFront + origin** | Custom domain | Đúng — tận dụng ALB = ELB, ACM free + auto-renew |
| A. Third-party CA cả hai chặng | Custom domain | Khả thi nhưng tốn phí, không tự renew |
| B. Self-signed cả hai chặng | — | Sai luôn, self-signed không trusted |
| D. Default CloudFront cert + ACM cho origin | Chỉ *.cloudfront.net | Sai vì domain ở đây là custom domain |

#### Lưu ý thực tế

- Nếu origin **không** là ELB (ví dụ S3 website endpoint hoặc EC2 public IP không qua load balancer), ACM **không** dùng được cho chặng CloudFront→origin, buộc phải import cert third-party vào ACM/IAM certificate store.
- ACM cert cho CloudFront luôn phải được tạo ở **us-east-1**, bất kể CloudFront là dịch vụ global.

#### Quy tắc nhớ cho thi

- **Thấy custom domain trên CloudFront** (`www.something.com`) → bắt buộc **ACM cert hoặc third-party CA**, default cert KHÔNG dùng được
- **Thấy domain mặc định** (`*.cloudfront.net`) → **default CloudFront certificate** là đủ, không cần ACM
- **Thấy origin = ELB/ALB** → ACM cert hợp lệ cho cả 2 chặng; origin = EC2 trần → chặng origin cần third-party CA
- **Phân biệt Q23 vs Q50**: cùng chủ đề CloudFront SSL nhưng khác domain → khác đáp án về cert

### TD explanation

The certificate issuer you must use depends on whether you want to require HTTPS between viewers and CloudFront or between CloudFront and your origin:
HTTPS between viewers and CloudFront
- You can use a certificate that was issued by a trusted certificate authority (CA) such as Comodo, DigiCert, Symantec or other third-party providers.
- You can use a certificate provided by AWS Certificate Manager (ACM)
HTTPS between CloudFront and a custom origin
- If the origin is not an ELB load balancer, such as Amazon EC2, the certificate must be issued by a trusted CA such as Comodo, DigiCert, Symantec or other third-party providers.
- If your origin is an ELB load balancer, you can also use a certificate provided by ACM.

If you're using your own domain name, such as tutorialsdojo.com, you need to change several CloudFront settings. You also need to use an SSL/TLS certificate provided by AWS Certificate Manager (ACM), or import a certificate from a third-party certificate authority into ACM or the IAM certificate store.
Therefore, the correct answer is: Configure the CloudFront distribution to redirect HTTP to HTTPS protocol. Generate a new SSL certificate on AWS Certificate Manager and use it as the CloudFront distribution and origin certificate. You can use ACM to generate a valid SSL certificate for your ALB and CloudFront distribution.
The option that says: Use a third-party CA certificate on both the origin and CloudFront is incorrect. You can use a third-party CA certificate on both the custom origin and CloudFront, however, it is cost-effective to just use an ACM-generated SSL as it also supports automatic renewal.
The options that says: Use a self-signed certificate in both the origin and CloudFront is incorrect. The website is hosted in Amazon EC2 and the certificate must be issued by a trusted CA such as Comodo, DigiCert, Symantec, or other third-party providers.
The option that says: Configure CloudFront to use its default certificate. Configure the CloudFront distribution to redirect HTTP to HTTPS protocol. For the origin, generate a new SSL certificate on AWS Certificate Manager is incorrect. You cannot use the default certificate in CloudFront since the website is using a custom domain (www.tutorialsdojonews.com). You can generate a valid SSL certificate for your domain on AWS Certificate Manager.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q50"></a>

## Q50

A photo-sharing website uses a CloudFront distribution with a default name (dtut0r1al5doj0.cloudfront.net) to distribute its static contents. It uses an ELB in front of an Auto Scaling group of Spot EC2 instances deployed across two Availability Zones. The website has a poor search ranking in Google as it doesn't use a secure HTTPS/SSL on its site.

Which of the following are valid options in order to require HTTPS for communication between the viewers and CloudFront? (Select TWO.)

- **A.** Set the Viewer Protocol Policy to use Redirect HTTP to HTTPS or HTTPS Only.
- **B.** Use a self-signed SSL/TLS certificate in the ELB which is stored in a private S3 bucket.
- **C.** Configure CloudFront to use its default SSL/TLS certificate by changing the Viewer Protocol Policy setting for one or more cache behaviors to require HTTPS communication.
- **D.** Use a self-signed certificate in the ELB.
- **E.** Configure the ELB to use its default SSL/TLS certificate.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C · **You picked:** A, D

🔑 **Key words:** default CloudFront domain name, HTTPS between viewers and CloudFront

🪤 **Your trap:** A cert on the ELB covers CloudFront→origin, not viewer→CloudFront; self-signed is never for public sites

🧠 **Rule:** *.cloudfront.net + viewer HTTPS → Viewer Protocol Policy (redirect/HTTPS only) + default CloudFront cert

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Browser ──HTTPS?──► CloudFront (dtut0r1al5doj0.cloudfront.net) ──► ELB ──► ASG Spot EC2
                     ↑ domain MẶC ĐỊNH của CloudFront, KHÔNG phải custom domain
Yêu cầu: chỉ cần HTTPS giữa VIEWER và CloudFront (chưa đả động tới origin)
```

Multi-select (2 đáp án). Đáp án đúng: **A, C** (Viewer Protocol Policy + default CloudFront certificate). Anh chọn **A, D** — đúng A, sai D (cert trên ELB).

#### A và C đúng — khớp đúng domain mặc định + đúng chặng cần bảo mật

```
CloudFront cache behavior
   → Viewer Protocol Policy = Redirect HTTP to HTTPS (hoặc HTTPS Only)
   → vì domain là *.cloudfront.net (mặc định) → CloudFront tự cấp
     DEFAULT SSL/TLS certificate, không cần ACM, không cần làm gì thêm
```

TD explanation: *"If you're using the domain name that CloudFront assigned to your distribution... you can change the Viewer Protocol Policy... CloudFront provides its default SSL/TLS certificate."* Vì website dùng chính domain CloudFront cấp (không có custom domain), default cert là đủ — không cần ACM, không cần cert ở origin, vì yêu cầu chỉ là HTTPS **viewer ↔ CloudFront**.

#### D (Anh chọn) sai — điểm quyết định: viewer↔CloudFront vs CloudFront↔origin

**Đây chính là điểm phân biệt với Q23 (không mâu thuẫn, khác câu hỏi khác phạm vi):**

```
Q23: yêu cầu HTTPS END-TO-END (viewer→CloudFront VÀ CloudFront→origin)
     + domain là CUSTOM domain → cần ACM cert, default cert KHÔNG áp dụng được
Q50: yêu cầu HTTPS CHỈ viewer→CloudFront
     + domain là *.cloudfront.net (mặc định) → default cert ĐỦ, không cần cert ở ELB
```

Cert đặt trên **ELB (origin)** chỉ ảnh hưởng tới chặng **CloudFront → origin**, hoàn toàn không liên quan tới việc viewer có kết nối HTTPS tới CloudFront hay không. TD explanation nói rõ: *"you don't need to add an SSL certificate if you only require HTTPS for communication between the viewers and CloudFront. You should only do this if you require HTTPS between your origin and CloudFront."* Đề bài Q50 chỉ yêu cầu chặng viewer↔CloudFront, nên việc cấu hình cert ở ELB là **thừa và không giải quyết đúng yêu cầu** — thêm vào đó self-signed cert không hợp lệ cho mục đích public-facing.

#### Các lựa chọn sai khác

- **B — self-signed cert trên ELB, lưu trong private S3 bucket:** sai gộp 2 lỗi — (1) không cần cert ở ELB cho yêu cầu này, (2) self-signed cert không dùng được cho HTTPS CloudFront↔origin dù lưu ở đâu.
- **E — ELB dùng "default SSL/TLS certificate":** sai vì **ELB không có khái niệm default certificate** như CloudFront — ELB chỉ dùng cert do bạn upload/qua ACM. TD explanation: *"There is no default SSL certificate in ELB, unlike what we have in CloudFront (*.cloudfront.net)."*

| Lựa chọn | Đúng chặng cần bảo mật? | Đúng loại cert cho domain mặc định? |
|---|---|---|
| **A. Viewer Protocol Policy** | Đúng (viewer↔CloudFront) | — |
| **C. Default CloudFront cert** | Đúng | Đúng, domain là *.cloudfront.net |
| B. Self-signed trên ELB | Sai chặng | Self-signed không hợp lệ |
| D. Self-signed trên ELB | Sai chặng (ảnh hưởng origin, không phải viewer) | — |
| E. "Default cert" trên ELB | Sai chặng | ELB không có default cert |

#### Lưu ý thực tế

- Default CloudFront certificate chỉ work khi **không gắn alternate domain name (CNAME)** vào distribution — ngay khi thêm custom domain, phải chuyển sang ACM/third-party cert (xem Q23).
- "Redirect HTTP to HTTPS" và "HTTPS Only" đều thỏa yêu cầu "require HTTPS communication"; khác nhau ở việc có cho phép fallback HTTP ban đầu hay chặn hoàn toàn.

#### Quy tắc nhớ cho thi

- **Thấy domain mặc định `*.cloudfront.net`** → **default CloudFront certificate** đủ dùng, không cần ACM/cert ở origin
- **Thấy yêu cầu chỉ "viewer ↔ CloudFront"** → chỉnh **Viewer Protocol Policy**, KHÔNG cần đụng tới cert ở origin/ELB
- **Thấy "self-signed certificate"** cho public site → luôn là trap, loại ngay
- **Thấy "ELB default certificate"** → không tồn tại, chỉ CloudFront mới có cert mặc định
- **Phân biệt Q23 vs Q50**: custom domain + end-to-end HTTPS → cần ACM; domain mặc định + chỉ cần HTTPS tới viewer → default cert đủ

### TD explanation

If you're using the domain name that CloudFront assigned to your distribution, such as dtut0ria1sd0jo.cloudfront.net, you can change the Viewer Protocol Policy setting for one or more cache behaviors to require HTTPS communication by setting it as either Redirect HTTP to HTTPS or HTTPS Only. In that configuration, CloudFront provides its default SSL/TLS certificate.

If your origin is an Elastic Load Balancing load balancer, you can use a certificate provided by AWS Certificate Manager (ACM). You can also use a certificate that is signed by a trusted third-party certificate authority and imported into ACM. Note that you can't use a self-signed certificate for HTTPS communication between CloudFront and your origin.
Therefore, the following options are correct:
- Set the Viewer Protocol Policy to use Redirect HTTP to HTTPS or HTTPS Only.
- Configure CloudFront to use its default SSL/TLS certificate by changing the Viewer Protocol Policy setting for one or more cache behaviors to require HTTPS communication.
The option that says: Use a self-assigned SSL/TLS certificate in the ELB which is stored in a private S3 bucket is incorrect because you don't need to add an SSL certificate if you only require HTTPS for communication between the viewers and CloudFront. You should only do this if you require HTTPS between your origin and CloudFront. In addition, you can't use a self-signed certificate in this scenario even though it is stored in a private S3 bucket. You need to use either a certificate from ACM or a third-party certificate.
The option that says: Use a self-signed certificate in the ELB is incorrect. As explained in the previous paragraph, adding an SSL certificate in the ELB is not required. Additionally, using a self-signed certificate for public websites is not recommended.
The option that says: Configure the ELB to use its default SSL/TLS certificate is incorrect. There is no default SSL certificate in ELB, unlike what we have in CloudFront (*.cloudfront.net). As previously explained, adding an SSL certificate in the ELB is not required.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html#using-https-cloudfront-to-origin-certificate
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

</details>

---

# Group E — Service fit & service limits (6)

<a id="q1"></a>

## Q1

A company offers a service that allows users to upload media files through a web portal. The web servers accept the media files and are directly uploaded to the on-premises Network Attached Storage (NAS server). For each uploaded media file, a corresponding message is sent to the message queue. A processing server picks up each message and processes each media file, which can take up to 30 minutes to process. The company noticed that the number of media files waiting in the processing queue is significantly higher during business hours, but the processing server quickly catches up after business hours. To save costs, the company hired a Solutions Architect to improve the media processing by migrating the workload to AWS Cloud.

Which of the following options is the most cost-effective solution?

- **A.** Reconfigure the existing web servers to publish messages to a standard queue on Amazon SQS. Create an AWS Lambda function that will pull requests from the SQS queue and process the media files. Invoke the Lambda function every time a new message is sent to the queue. Send the processed media files to an Amazon S3 bucket.
- **B.** Reconfigure the existing web servers to publish messages to a queue in Amazon MQ. Create an Auto Scaling group of Amazon EC2 instances that will pull requests from the queue and process the media files. Configure the Auto Scaling group to scale based on the length of the Amazon SQS queue. Send the processed media files to an Amazon EFS mount point and shut down the EC2 instances after processing is complete.
- **C.** Reconfigure the existing web servers to publish messages to a queue in Amazon MQ. Create an AWS Lambda function that will pull requests from the Amazon SQS queue and process the media files. Invoke the Lambda function every time a new message is sent to the queue. Send the processed media files to an Amazon EFS volume.
- **D.** Reconfigure the existing web servers to publish messages to a standard queue on Amazon SQS. Create an Auto Scaling group of Amazon EC2 instances that will pull requests from the queue and process the media files. Configure the Auto Scaling group to scale based on the length of the SQS queue. Send the processed media files to an Amazon S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** processing can take up to 30 minutes, most cost-effective

🪤 **Your trap:** Lambda max timeout is 15 minutes — can't process a 30-minute job

🧠 **Rule:** Job > 15 min → EC2 ASG scaled on SQS queue depth (not Lambda); SQS over Amazon MQ unless JMS/AMQP needed

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Web server ──upload──► NAS on-prem
     │
     └──message──► Queue ──► Processing server (tới 30 phút/file)
                              ▲
                    Giờ hành chính: queue dồn lại
                    Ngoài giờ: xử lý kịp
Yêu cầu: migrate lên AWS, GIẢI PHÁP RẺ NHẤT
```

Đáp án đúng: **D** (SQS standard queue + EC2 ASG scale theo queue depth + S3). Anh chọn **A** (SQS + Lambda + S3) — đúng phần queue và storage, sai ở compute.

#### Vì sao D đúng, A sai — chỉ khác nhau một chữ: thời gian xử lý

Đề nói rõ: **"can take up to 30 minutes to process"**. AWS Lambda có **giới hạn cứng 15 phút/invocation**. Dù A rẻ hơn về lý thuyết (Lambda = pay-per-use, không tốn tiền khi idle), nó **không thể chạy được** job 30 phút — bị timeout giữa đường, không phải vấn đề chi phí mà là vấn đề khả thi.

```
Lambda timeout:  |----15 phút MAX----| ✗ KILLED
Job cần:         |----------30 phút----------|
```

→ D dùng **EC2 Auto Scaling Group**, không giới hạn thời gian chạy, và scale theo **SQS queue length** (target tracking trên custom CloudWatch metric `ApproximateNumberOfMessagesVisible`) — khớp pattern "tải cao giờ hành chính, thấp ngoài giờ" trong đề.

#### Hai lựa chọn còn lại — sai vì dùng nhầm MQ hoặc EFS

| Option | Vấn đề |
|---|---|
| B | Dùng Amazon MQ (không cần vì không có yêu cầu JMS/AMQP/MQTT/STOMP) + lưu kết quả vào **EFS** (đắt hơn S3) |
| C | Amazon MQ + Lambda (vừa sai MQ, vừa sai Lambda 15 phút) + EFS |

#### So sánh SQS vs Amazon MQ

| | Amazon SQS | Amazon MQ |
|---|---|---|
| Khi nào dùng | App mới, cần scale vô hạn, API đơn giản | Migrate app cũ đang phụ thuộc JMS/AMQP/MQTT/STOMP |
| Setup | Serverless, không cần quản lý broker | Cần quản lý broker (managed nhưng vẫn là broker thật) |
| Đề bài này | Không nhắc protocol cụ thể → SQS là lựa chọn mặc định/rẻ hơn | — |

#### Lưu ý thực tế

- **S3 luôn rẻ hơn EFS** cho lưu file kết quả đơn giản (không cần shared POSIX filesystem) — đây là chi tiết TD hay chèn vào để loại bớt option.
- ASG scaling theo SQS **không có metric built-in** để scale trực tiếp — phải tạo **custom CloudWatch metric** (ví dụ `BacklogPerInstance`) rồi gắn target tracking policy.

#### Quy tắc nhớ cho thi

- **Job xử lý > 15 phút** → loại ngay Lambda, dùng **EC2 (ASG)** hoặc Fargate với timeout dài hơn.
- **ASG scale theo queue depth** → SQS + target tracking trên custom metric.
- **Lưu file đơn giản, không cần POSIX** → **S3**, không phải EFS (EFS đắt hơn, dùng khi cần shared file system thật).
- **Không có yêu cầu JMS/AMQP/MQTT** → mặc định chọn **SQS**, không phải Amazon MQ.

### TD explanation

Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Amazon SQS offers "standard" as the default queue type. Standard queues support at-least-once message delivery.

You can use standard message queues in many scenarios, as long as your application can process messages that arrive more than once and out of order, for example:

- Decouple live user requests from intensive background work – Let users upload media while resizing or encoding it.

- Allocate tasks to multiple worker nodes – Process a high number of credit card validation requests.

- Batch messages for future processing – Schedule multiple entries to be added to a database.

You can scale-in/scale-out your Amazon EC2 Auto Scaling group in response to changes in system load in an Amazon Simple Queue Service (Amazon SQS) queue. For example, suppose that you have a web app that lets users upload images and use them online. In this scenario, each image requires resizing and encoding before it can be published. The app runs on EC2 instances in an Auto Scaling group, and it's configured to handle your typical upload rates. Unhealthy instances are terminated and replaced to maintain current instance levels at all times.

The app places the raw bitmap data of the images in an SQS queue for processing. It processes the images and then publishes the processed images where they can be viewed by users. The architecture for this scenario works well if the number of image uploads doesn't vary over time. But if the number of uploads changes over time, you might consider using dynamic scaling to scale the capacity of your Auto Scaling group. If you use a target tracking scaling policy based on a custom Amazon SQS queue metric, dynamic scaling can adjust to the demand curve of your application more effectively.

Amazon SQS is a queue service that is highly scalable, simple to use, and doesn't require you to set up message brokers. AWS recommends this service for new applications that can benefit from nearly unlimited scalability and simple APIs.

Amazon MQ is a managed message broker service that provides compatibility with many popular message brokers. AWS recommends Amazon MQ for migrating applications from existing message brokers that rely on compatibility with APIs such as JMS or protocols such as AMQP, MQTT, OpenWire, and STOMP.

Hence, the correct answer is: Reconfigure the existing web servers to publish messages to a standard queue on Amazon SQS. Create an Auto Scaling group of Amazon EC2 instances that will pull requests from the queue and process the media files. Configure the Auto Scaling group to scale based on the length of the SQS queue. Send the processed media files to an Amazon S3 bucket.

The option that says: Reconfigure the existing web servers to publish messages to a standard queue on Amazon SQS. Create an AWS Lambda function that will pull requests from the SQS queue and process the media files. Invoke the Lambda function every time a new message is sent to the queue. Send the processed media files to an Amazon S3 bucket is incorrect. Although this answer is the most cost-effective, AWS Lambda only allows functions to run up to 15 minutes. Remember that the media files can take up to 30 minutes to process.

The option that says: Reconfigure the existing web servers to publish messages to a queue in Amazon MQ. Create an Auto Scaling group of Amazon EC2 instances that will pull requests from the queue and process the media files. Configure the Auto Scaling group to scale based on the length of the Amazon SQS queue. Send the processed media files to an Amazon EFS mount point and shut down the EC2 instances after processing is complete is incorrect. It is recommended to use Amazon SQS for this because it is not stated in the scenario to have compatibility with JMS or other protocols like MQTT AMQP, etc. Also, storing media files on Amazon EFS is more expensive than using Amazon S3.

The option that says: Reconfigure the existing web servers to publish messages to a queue in Amazon MQ. Create an AWS Lambda function that will pull requests from the Amazon SQS queue and process the media files. Invoke the Lambda function every time a new message is sent to the queue. Send the processed media files to an Amazon EFS volume is incorrect. Lambda functions cannot run for more than 15 minutes, while in the scenario, the processing time is 30 minutes. Moreover, storing media files on Amazon EFS is typically expensive than using Amazon S3.

References:

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html

Check out these Amazon SQS and Amazon MQ Cheat Sheets:

https://tutorialsdojo.com/amazon-sqs/

https://tutorialsdojo.com/amazon-mq/

</details>

<a id="q14"></a>

## Q14

A visual effects studio has over 40-TB worth of video files stored in the company's on-premises tape library. The tape drives are managed by a Media Asset Management (MAM) solution. The video files contain a variety of footage which includes faces, objects, sceneries, cars, and many others. The company wants to automatically build a metadata library for the video files based on these objects. This will then be used as a catalog for the search feature of the MAM solution. The company already has a catalog of people’s photos and names that appeared on the video footage. The company wants to migrate all the video files of the MAM solution to AWS so a Direct Connect connection was provisioned from the on-premises data center to AWS to facilitate this.

Which of the following is the MOST suitable implementation that will meet the company's requirements?

- **A.** Provision an AWS Storage Gateway – file gateway appliance on the on-premises data center. Configure the MAM solution to extract the video files from the current tape archives and move them to the file gateway share which is then synced to Amazon S3. Use Amazon Rekognition to build a collection based on the videos by using the catalog of people’s faces and names. Create an AWS Lambda function that will invoke Rekognition to pull the video files from the S3 bucket, retrieve the generated metadata and then push it to the MAM solution search catalog.
- **B.** Configure the MAM solution to extract the video files from the current tape archives and move them to an Amazon S3 bucket using AWS DataSync. Use an Amazon SageMaker Jupyter notebook instance to build a collection based on the videos by using the catalog of people’s faces and names. Create an AWS Lambda function that will invoke Amazon SageMaker to pull the video files from the S3 bucket, retrieve the generated metadata, and then push it to the MAM solution search catalog.
- **C.** Create a stream in Amazon Kinesis Video Streams that will ingest the videos from the MAM system and store the videos to an Amazon S3 bucket. Configure the MAM solution to stream the videos into Kinesis Video Streams. Use Amazon Rekognition to build a collection based on the videos by using the catalog of people’s faces and names. Set up a stream consumer that will retrieve the generated metadata and then push it to the MAM solution search catalog.
- **D.** Securely upload the files to an Amazon S3 bucket using AWS Transfer for SFTP. Create an Amazon EC2 instance that will run GluonCV libraries to generate metadata information from the video files in the S3 bucket. Store the catalog of people’s faces and names in the Amazon EBS volume to be used by GluonCV. After processing the videos, push the generated metadata to the MAM solution search catalog.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** 🔁 tape library, MAM, catalog of faces, metadata for videos

🪤 **Your trap:** 🔁 Third miss on this pattern. SageMaker notebooks don't do recognition; Rekognition does

🧠 **Rule:** Tape archive + video face/object tagging → File Gateway to S3 + Rekognition (face collection) + Lambda → MAM

### 🇻🇳 Phân tích chi tiết

#### ⚠️ Lỗi lặp lại — lần thứ BA trúng pattern này

```
On-prem tape library (40TB video) ──?──► AWS
     │
     video có: face, object, scenery, car...
     đã có catalog ảnh + tên người
Yêu cầu: tự động build metadata library cho MAM search
```

Đáp án đúng: **A** (File Gateway → S3 + Rekognition + Lambda). Anh chọn **B** (DataSync + SageMaker notebook).

Đây là **lần thứ 3** Anh dính đúng cụm "tape library + video face/object tagging":
- TD Set 1 Q57 (lần 1): chọn sai Tape Gateway thay vì File Gateway.
- TD Set 1 Q57 (redo): chọn sai lần nữa.
- TD Set 3 Q14 (lần này): chọn đúng phần storage nhưng sai phần AI — chọn SageMaker notebook thay vì Rekognition.

Pattern lỗi đang dịch chuyển: trước đây sai ở **loại Storage Gateway**, giờ sai ở **dịch vụ AI nào làm nhận diện**. Gốc vấn đề vẫn là chưa nắm chắc "ai làm gì" trong chuỗi tape → S3 → AI → MAM.

#### Vì sao A đúng

**Storage Gateway — File Gateway, không phải Tape Gateway:**
Đề nói nguồn dữ liệu đang nằm trong **tape library**, nhưng việc cần làm là "extract video files ra khỏi tape và đẩy vào S3" — tức **xử lý nội dung** (lấy ra, phân tích), không phải "sao lưu/archive y nguyên dạng tape". Đây là file thật (video) cần máy tính đọc được → phải qua **File Gateway** (NFS/SMB share → sync lên S3) rồi mới xử lý tiếp.

**Rekognition — không phải SageMaker:**
Yêu cầu là "build metadata dựa trên object + catalog khuôn mặt có sẵn" = nhận diện khuôn mặt + object detection có sẵn, dùng ngay. **Amazon Rekognition** có API `IndexFaces`/collection để làm chính xác việc này, không cần tự train model.

```
Tape library → File Gateway (NFS/SMB) → S3
                                          │
                        Lambda gọi Rekognition
                        (build face collection từ catalog có sẵn)
                                          │
                              Metadata → MAM search catalog
```

#### Vì sao B (lựa chọn của Anh) sai

**DataSync** về cơ bản hợp lý để di chuyển dữ liệu (dù TD không chọn vì không khớp "tape" bằng File Gateway), nhưng điểm chết là **SageMaker Jupyter notebook**:
> "Jupyter notebooks are primarily used to prepare your data and write code to train models" — **không tự làm nhận diện ảnh/video**. Đó chỉ là compute instance chạy Jupyter, Anh phải tự viết + train model nhận diện, trong khi đề đã có sẵn catalog và cần giải pháp managed, nhanh.

#### Các option sai khác

| Option | Vấn đề |
|---|---|
| C | Kinesis Video Streams dùng cho **streaming trực tiếp**, không hợp khi dữ liệu đang nằm tĩnh trong tape; MAM không chắc hỗ trợ stream vào KVS → cần custom producer, không cost-effective |
| D | AWS Transfer for SFTP khi không yêu cầu SFTP (S3 upload qua HTTPS đã đủ an toàn); tự chạy GluonCV trên EC2 = overhead vận hành cao, không bằng managed Rekognition |

#### Lưu ý thực tế

- **S3 upload mặc định đã mã hóa qua HTTPS** → không cần AWS Transfer Family trừ khi có yêu cầu SFTP rõ ràng.
- Đừng để chữ "tape" trong đề đánh lừa thành Tape Gateway — phải đọc tiếp xem **mục đích là archive nguyên trạng hay xử lý nội dung**.

#### Quy tắc nhớ cho thi

- **"Tape library" + "process/extract/build metadata"** → **File Gateway**, KHÔNG phải Tape Gateway (Tape Gateway chỉ dùng khi mục đích là backup/archive giữ nguyên định dạng tape, giống TD Set 3 Q3 — công ty archive dữ liệu tape-based, giữ nguyên tape-based process → **Tape Gateway** đúng ở đó vì không ai "xử lý nội dung", chỉ archive).
- **"Nhận diện khuôn mặt/object trong ảnh/video"** → **Amazon Rekognition**, không phải SageMaker notebook (SageMaker notebook = nơi viết code train model, không phải dịch vụ nhận diện có sẵn).
- Mnemonic: **"Tape mà có FACE thì dùng FILE"** — còn tape mà chỉ archive nguyên khối thì mới giữ Tape Gateway.

### TD explanation

AWS Storage Gateway connects an on-premises software appliance with cloud-based storage to provide seamless integration with data security features between your on-premises IT environment and the AWS storage infrastructure. You can use the service to store data in the AWS Cloud for scalable and cost-effective storage that helps maintain data security.
AWS Storage Gateway offers file-based, volume-based, and tape-based storage solutions. A file gateway supports a file interface into Amazon Simple Storage Service (Amazon S3) and combines a service and a virtual software appliance. By using this combination, you can store and retrieve objects in Amazon S3 using industry-standard file protocols such as Network File System (NFS) and Server Message Block (SMB). A file gateway simplifies file storage in Amazon S3, integrates with existing applications through industry-standard file system protocols, and provides a cost-effective alternative to on-premises storage. It also provides low-latency access to data through transparent local caching.

Amazon Rekognition makes it easy to add image and video analysis to your applications using proven, highly scalable, deep learning technology that requires no machine learning expertise to use. With Amazon Rekognition, you can identify objects, people, text, scenes, and activities in images and videos, as well as detect any inappropriate content.
Amazon Rekognition also provides highly accurate facial analysis and facial search capabilities that you can use to detect, analyze, and compare faces for a wide variety of user verification, people counting, and public safety use cases.
Therefore, the correct answer is: Provision an AWS Storage Gateway – file gateway appliance on the on-premises data center. Configure the MAM solution to extract the video files from the current tape archives and move them to the file gateway share which is then synced to Amazon S3. Use Amazon Rekognition to build a collection based on the videos by using the catalog of people’s faces and names. Create an AWS Lambda function that will invoke Rekognition to pull the video files from the S3 bucket, retrieve the generated metadata and then push it to the MAM solution search catalog.
The option that says: Configure the MAM solution to extract the video files from the current tape archives and move them to an Amazon S3 bucket using AWS DataSync. Use an Amazon SageMaker Jupyter notebook instance to build a collection based on the videos by using the catalog of people’s faces and names. Create an AWS Lambda function that will invoke Amazon SageMaker to pull the video files from the S3 bucket, retrieve the generated metadata and then push it to the MAM solution search catalog is incorrect. An Amazon SageMaker notebook instance is simply a machine learning (ML) compute instance running the Jupyter Notebook App. It is not capable of doing image detection or recognition. Jupyter notebooks are primarily used to prepare your data and write code to train models. A better solution for this is to use Amazon Rekognition.
The option that says: Create a stream in Amazon Kinesis Video Streams that will ingest the videos from the MAM system and store the videos to an Amazon S3 bucket. Configure the MAM solution to stream the videos into Kinesis Video Streams. Use Amazon Rekognition to build a collection based on the videos by using the catalog of people’s faces and names. Set up a stream consumer that will retrieve the generated metadata and then push it to the MAM solution search catalog is incorrect. This is not cost-effective and will require more changes to the existing MAM solution. In addition, it is not stated in the scenario that the MAM solution supports video streaming directly to Kinesis Video Stream. Most of the time, you need to set up a custom Kinesis Video Streams Producer client in order to send data to a Kinesis Video Stream.
The option that says: Securely upload the files to an Amazon S3 bucket using AWS Transfer for SFTP. Create an Amazon EC2 instance that will run GluonCV libraries to generate metadata information from the video files in the S3 bucket. Store the catalog of people’s faces and names in the Amazon EBS volume to be used by GluonCV. After processing the videos, push the generated metadata to the MAM solution search catalog is incorrect. Uploading files to Amazon S3 is secured by default because it is using HTTPS. Unless there is a requirement for using the SFTP protocol, AWS Transfer for SFTP is not recommended for this scenario. This is not cost-effective and will require more management overhead in maintaining and configuring the GluonCV libraries on the EC2 instance.

References:
https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html
https://aws.amazon.com/rekognition/
https://aws.amazon.com/rekognition/media-analysis/

Check out these Amazon Rekognition and Storage Gateway Cheat Sheets:
https://tutorialsdojo.com/amazon-rekognition/
https://tutorialsdojo.com/aws-storage-gateway/

</details>

<a id="q19"></a>

## Q19

A company has a CRM application that uses a MySQL database hosted in Amazon RDS, and a central data warehouse that runs on Amazon Redshift. There is a batch analytics process that runs every day and reads data from RDS. During the execution of the batch analytics, the RDS utilization spikes up, which results in the CRM application becoming unresponsive. The top management dashboard must also be updated with new data right after the batch analytics processing completes. However, the dashboard is on another system running on-premises and cannot be modified directly. The only way to update the dashboard is to send an email with the new data to the dashboard system via SMTP, which will then be parsed and processed to update the dashboard with the latest data.

How would the solutions architect optimize this scenario to solve performance issues and automate the process as much as possible?

- **A.** Add read replicas for the RDS database to speed up batch analytics and use Amazon SNS to notify the on-premises system to update the dashboard.
- **B.** Consider using Amazon Redshift as the main OLTP transactional database instead of RDS for the batch analytics and use Redshift Spectrum to run SQL queries directly against Exabytes of structured or unstructured data in S3 without the need for unnecessary data movement. Utilize Amazon SNS to notify the on-premises system to update the dashboard.
- **C.** Consider using Amazon Redshift instead of Amazon RDS as the database for the CRM application. Use Amazon SQS to notify the on-premises system to update the dashboard.
- **D.** Add read replicas for the RDS database to speed up batch analytics and use Amazon SQS to notify the on-premises system to update the dashboard.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** dashboard only accepts email via SMTP, automate

🪤 **Your trap:** SQS can't send email; something must poll it

🧠 **Rule:** Notify by email → SNS (email subscription); offload batch reads → RDS read replica

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CRM app ──MySQL──► Amazon RDS ◄── batch analytics (chạy mỗi ngày, đọc RDS)
                      │
              RDS spike khi batch chạy → CRM app bị unresponsive

Sau khi batch xong ──?──► Dashboard on-prem (chỉ nhận update qua EMAIL/SMTP)
```

Đáp án đúng: **A** (RDS Read Replica + Amazon SNS). Anh chọn **D** (RDS Read Replica + Amazon SQS) — đúng phần database, sai phần notify.

#### Vì sao A đúng

**Read Replica** giải quyết đúng vấn đề performance: batch analytics đọc trên **replica** thay vì đọc trực tiếp trên primary → CRM app không còn bị tranh tài nguyên khi batch chạy.

**Amazon SNS** giải quyết đúng vấn đề tự động hóa: SNS hỗ trợ **email subscription** — khi publish message vào topic, SNS tự gửi email đến endpoint đã subscribe, không cần code gì thêm ở phía gửi.

```
Batch analytics xong
      │
      ▼
   SNS topic ──(email subscription)──► SMTP ──► Dashboard on-prem
```

#### Vì sao D (lựa chọn của Anh) sai

**SQS không gửi được email.** SQS chỉ là hàng đợi message — cần có một bên **chủ động poll** queue rồi tự viết code gửi email qua SMTP. Đề yêu cầu **"automate the process as much as possible"**, và dashboard "cannot be modified directly", chỉ nhận qua SMTP — nghĩa là cần cơ chế **push trực tiếp ra email**, đúng việc SNS làm sẵn, SQS thì không.

```
SQS: message nằm trong queue, cần consumer tự poll + tự code gửi email
SNS: publish → tự động fan-out → email subscriber nhận ngay, không cần code thêm
```

#### Hai option còn lại — sai vì đổi nhầm vai trò RDS/Redshift

| Option | Vấn đề |
|---|---|
| B | Biến Redshift thành **OLTP chính** cho CRM — sai bản chất: Redshift là OLAP (data warehouse), RDS mới là OLTP |
| C | Thay RDS bằng Redshift cho CRM app — cùng lỗi OLAP/OLTP, thêm SQS cũng sai notify |

#### So sánh nhanh

| Nhu cầu | Dịch vụ đúng |
|---|---|
| Giảm tải đọc cho OLTP (RDS) | **Read Replica** |
| OLTP transactional (CRM) | **RDS** |
| OLAP / data warehouse | **Redshift** |
| Tự động gửi thông báo qua email/SMS mà không cần code poll | **SNS** |
| Hàng đợi để decouple, cần consumer chủ động xử lý | **SQS** |

#### Lưu ý thực tế

- SNS + SQS có thể **kết hợp** (fan-out pattern: SNS topic → nhiều SQS queue) nhưng ở đây yêu cầu chỉ là gửi email → SNS một mình đã đủ, không cần SQS.
- Đừng nhầm "notify" luôn cần SQS vì SQS là message queue quen thuộc — SQS không có concept "subscriber nhận email", đó là việc của SNS.

#### Quy tắc nhớ cho thi

- **Gửi thông báo tự động qua email/SMS/HTTP endpoint** → **SNS**, không phải SQS.
- **SQS** chỉ dùng khi cần một **consumer chủ động** poll và xử lý message.
- **Offload read-heavy batch khỏi OLTP** → **RDS Read Replica**.
- **CRM/OLTP transactional** → luôn giữ RDS; **Redshift chỉ cho OLAP/warehouse**, không thay thế RDS làm app database chính.

### TD explanation

In this scenario, the use of Amazon RDS Read Replicas is the best option. It provides enhanced performance and durability for database (DB) instances. This feature makes it easy to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads. You can create one or more replicas of a given source DB Instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput. Read replicas can also be promoted when needed to become standalone DB instances. Read replicas are available in Amazon RDS for MySQL, MariaDB, Oracle, and PostgreSQL as well as Amazon Aurora.

Therefore, the correct answer is: Adding read replicas for the RDS database to speed up batch analytics and using Amazon SNS to notify the on-premises system to update the dashboard. It uses Read Replicas which improves the read performance, and it uses SNS which automates the process of notifying the on-premises system to update the dashboard.
The option that says: Consider using Amazon Redshift as the main OLTP transactional database instead of RDS for the batch analytics and use Redshift Spectrum to run SQL queries directly against Exabytes of structured or unstructured data in S3 without the need for unnecessary data movement. Utilize Amazon SNS to notify the on-premises system to update the dashboard is incorrect because Redshift is primarily used for OLAP scenarios whereas RDS is used for OLTP scenarios. Hence, replacing RDS with Redshift is not a valid solution. Although using Redshift Spectrum to run SQL queries is valid, it is still incorrect to replace RDS with Redshift as your main OLTP database.
The option that says: Consider using Amazon Redshift instead of Amazon RDS as the database for the CRM application. Use Amazon SQS to notify the on-premises system to update the dashboard is incorrect because Redshift is used for OLAP scenarios whereas RDS is used for OLTP scenarios. Hence, replacing RDS with Redshift is not a solution.
The option that says: Adding read replicas for the RDS database to speed up batch analytics and using Amazon SQS to notify the on-premises system to update the dashboard is incorrect because SQS is not a service to be used for sending the notification.

References:
https://aws.amazon.com/rds/details/read-replicas/
https://aws.amazon.com/big-data/datalakes-and-analytics/

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q32"></a>

## Q32

A company is developing an application that will allow biologists from around the world to submit plant genomic information and share it with other biologists. The application will expect several submissions every minute and will push about 8KB of genomic data every second to the data platform. This data needs to be processed and analyzed to provide meaningful information back to the biologists. The following are the requirements for the data platform:

-The inbound genomic data must be processed near-real-time and provide analytics.

-The received data must be stored in a flexible, parallel, and durable manner.

-After processing the data, the resulting output must be delivered to a data warehouse.

Which of the following options should the Solutions Architect implement to meet the company's requirements?

- **A.** Create an Amazon Data Firehose stream to deliver the inbound data to an Amazon S3 bucket. Use a Kinesis client to analyze the stored data. For data warehousing, register the S3 bucket on AWS Lake Formation as a data lake. Use Amazon Quicksight to query the data lake.
- **B.** Create a stream in Amazon Kinesis Data Streams to collect the inbound data. Use a Kinesis client to analyze the genomic data. After processing, use Amazon EMR to save the results to an Amazon Redshift cluster.
- **C.** Store all inbound data files directly to an Amazon S3 bucket. Use Amazon Kinesis with Amazon SQS to analyze the data stored in the S3 bucket. After processing, send the results to an Amazon Redshift cluster.
- **D.** Leverage Amazon API Gateway to accept the inbound data and send it to an Amazon SQS queue. Write an AWS Lambda function that will process the messages on the SQS queue. After processing, use Amazon EMR to save the results to an Amazon Redshift cluster.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** near-real-time, durable parallel storage, deliver to a data warehouse

🪤 **Your trap:** S3 first + SQS is batch-ish and needs custom code — not near-real-time

🧠 **Rule:** Near-real-time ingest + analytics → Kinesis Data Streams + consumers; results → Redshift

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Biologists (toàn cầu) ──8KB/giây──► Data platform
Yêu cầu:
  1. Xử lý NEAR-REAL-TIME + analytics
  2. Lưu trữ flexible, parallel, durable
  3. Kết quả cuối phải đẩy vào DATA WAREHOUSE
```

Đáp án đúng: **B** (Kinesis Data Streams + Kinesis client + EMR → Redshift). Anh chọn **C** (S3 trước, rồi Kinesis + SQS phân tích).

#### Vì sao B đúng

**Kinesis Data Streams (KDS)** được thiết kế đúng cho use-case này: ingest liên tục dữ liệu tốc độ cao, dữ liệu sẵn sàng cho consumer **trong vòng ~70ms**, lưu trữ nhân bản đồng bộ trên 3 AZ (durable). Đây khớp cả 2 yêu cầu đầu: near-real-time + lưu trữ durable/parallel.

```
Biologists → KDS stream → Kinesis Client (KCL) → xử lý/phân tích
                                                        │
                                              EMR → Amazon Redshift (data warehouse)
```

Sau khi KDS xử lý, dùng **EMR để đẩy kết quả vào Redshift** — đúng yêu cầu thứ 3 (data warehouse).

#### Vì sao C (lựa chọn của Anh) sai

C đưa dữ liệu vào **S3 trước**, rồi mới "dùng Kinesis với SQS để phân tích dữ liệu trong S3" — việc ghi file vào S3 rồi mới xử lý **mất thời gian** (không phải pipeline streaming liên tục), không đáp ứng **near-real-time**. TD note thẳng: "Storing files to S3 first and then sending a message to an SQS queue takes some time... You will also have to write your own Lambda function which increases operational overhead."

```
C: Data → S3 (ghi file) → SQS message → tự code xử lý → chậm, nhiều thao tác thủ công
B: Data → KDS (buffer trong bộ nhớ/stream) → consumer xử lý ngay → nhanh, managed
```

#### Hai option còn lại

| Option | Vấn đề |
|---|---|
| A | Dùng Firehose → S3 → Lake Formation → **QuickSight không query được Lake Formation data lake trực tiếp** theo cách này; AWS khuyến nghị Redshift làm warehouse, không phải Lake Formation + QuickSight ở đây |
| D | API Gateway → SQS → Lambda → EMR → Redshift: SQS **không đảm bảo thứ tự** (standard queue) phù hợp cho near-real-time analysis theo trình tự |

#### Lưu ý thực tế

- **S3 + SQS không sai về nguyên tắc**, nhưng khi đề nhấn **"near-real-time"**, bất kỳ bước ghi-file-trước-rồi-mới-xử-lý nào đều bị loại — đây là từ khóa quyết định, không phải vấn đề cost.
- Kinesis Data Streams khác Kinesis Data Firehose: **KDS** = custom consumer, low-latency, cần tự quản lý shard; **Firehose** = managed delivery tới S3/Redshift/OpenSearch nhưng có buffer delay (không phải near-real-time thực sự ở mức ms).

#### Quy tắc nhớ cho thi

- **"Near-real-time" + "ingest liên tục, tốc độ cao"** → **Kinesis Data Streams**, không phải S3-first hay SQS-first.
- **"Lưu trữ durable, parallel"** cho streaming data → đặc tính sẵn có của KDS (replicate 3 AZ).
- **Kết quả cuối → "data warehouse"** → đích luôn là **Amazon Redshift**, không phải Lake Formation/QuickSight (đó là data lake pattern, không phải warehouse).
- Thấy **"ghi vào S3 rồi mới phân tích"** trong câu có từ khóa near-real-time → nghi ngờ ngay, đó thường là bẫy.

### TD explanation

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources, such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.
You can make your streaming data available to multiple real-time analytics applications, to Amazon S3, or to AWS Lambda within 70 milliseconds of the data being collected. KDS is highly durable as it performs synchronous replication of your streaming data across three Availability Zones in an AWS Region and stores that data for up to 365 days to provide multiple layers of protection from data loss.
You can have your Kinesis Applications run real-time analytics on high-frequency event data, such as sensor data collected by Kinesis Data Streams, which enables you to gain insights from your data at a frequency of minutes instead of hours or days.

One of the methods of developing custom consumer applications that can process data from KDS data streams is to use the Kinesis Client Library (KCL). KCL helps you consume and process data from a Kinesis data stream by taking care of many of the complex tasks associated with distributed computing. These include load balancing across multiple consumer application instances, responding to consumer application instance failures, checkpointing processed records, and reacting to resharding.
Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. An Amazon Redshift data warehouse is a collection of computing resources called nodes, which are organized into a group called a cluster. Each cluster runs an Amazon Redshift engine and contains one or more databases. With Redshift, you can query and combine exabytes of structured and semi-structured data across your data warehouse, operational database, and data lake using standard SQL.
Therefore, the correct answer is: Create a stream in Amazon Kinesis Data Streams to collect the inbound data. Use a Kinesis client to analyze the genomic data. After processing, use Amazon EMR to save the results to an Amazon Redshift cluster. Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. Your data can be made available to real-time analytics applications and then saved to Amazon Redshift for data warehousing.
The option that says: Create an Amazon Data Firehose stream to deliver the inbound data to an Amazon S3 bucket. Use a Kinesis client to analyze the stored data. For data warehousing, register the S3 bucket on AWS Lake Formation as a data lake. Use Amazon Quicksight to query the data lake is incorrect. You can't use Amazon Quicksight to query data lakes from AWS Lake Formation. AWS recommends Amazon Reshift as a data warehouse solution.
The option that says: Store all inbound data files directly to an Amazon S3 bucket. Use Amazon Kinesis with Amazon SQS to analyze the data stored in the S3 bucket. After processing, send the results to an Amazon Redshift cluster is incorrect. Storing files to S3 first and then sending a message to an SQS queue takes some time. This solution may not meet the near-real-time requirement. You will also have to write your own Lambda function which increases operational overhead.
The option that says: Leverage Amazon API Gateway to accept the inbound data and send it to an Amazon SQS queue. Write an AWS Lambda function that will process the messages on the SQS queue. After processing, use Amazon EMR to save the results to an Amazon Redshift cluster is incorrect. It is possible to integrate API Gateway with Amazon SQS. However, the messages will not be processed in an orderly manner required for near-real-time analysis.

References:
https://aws.amazon.com/kinesis/data-streams/
https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html
https://docs.aws.amazon.com/redshift/latest/dg/welcome.html

Check out these Amazon Kinesis and Amazon Redshift Cheat Sheets:
https://tutorialsdojo.com/amazon-redshift/
https://tutorialsdojo.com/amazon-kinesis/

</details>

<a id="q53"></a>

## Q53

A company is running its enterprise resource planning application in AWS that handles supply chain, order management, and delivery tracking. The architecture has a set of RESTful web services that enable third-party companies to search for data that will be consumed by their respective applications. The public web services consist of several AWS Lambda functions. DynamoDB is used for its database tier and is integrated with an Amazon OpenSearch domain, which stores the indexes and supports the search feature. A Solutions Architect has been instructed to ensure that in the event of a failed deployment, there should be no downtime, and a system should be in place to prevent subsequent deployments. The service must strictly maintain full capacity during API deployment without any reduced compute capacity to avoid degradation of the service.

Among the options below, which can the Architect use to meet the requirements in the MOST efficient way?

- **A.** Do a blue/green deployment on all upcoming changes using AWS CodeDeploy. Using AWS SAM, launch the DynamoDB tables, Lambda functions, and Amazon OpenSearch domain in your AWS VPC. Host the web application in AWS Elastic Beanstalk and set the deployment policy to All at Once.
- **B.** Do an in-place deployment on all upcoming changes using AWS CodeDeploy. Using AWS SAM, launch the Amazon DynamoDB tables, Lambda functions, and Amazon OpenSearch domain in your AWS VPC. Host the web application in AWS Elastic Beanstalk and set the deployment policy to Rolling.
- **C.** Do a blue/green deployment on all upcoming changes using AWS CodeDeploy. Using AWS CloudFormation, launch the Amazon DynamoDB tables, AWS Lambda functions, and Amazon OpenSearch domain in your AWS VPC. Host the web application in AWS Elastic Beanstalk and set the deployment policy to Immutable.
- **D.** Do a blue/green deployment on all upcoming changes using Amazon Lightsail. Let Amazon Lightsail handle the provisioning of database instances, EC2 instances, and load balancers needed by the web application. Use CloudFormation to deploy the AWS Lambda functions, provision DynamoDB tables, and create an Amazon OpenSearch domain in your VPC.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** no downtime, maintain full capacity during deployment, stop subsequent deployments on failure

🪤 **Your trap:** All-at-once takes instances out of service — reduces capacity

🧠 **Rule:** Full capacity during deploy → Elastic Beanstalk Immutable (or blue/green); never All at once / Rolling

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ERP app: RESTful web services (Lambda) + DynamoDB + OpenSearch (search index)
Yêu cầu khi deploy:
  1. Deployment fail → KHÔNG downtime
  2. Có cơ chế chặn deploy tiếp theo khi fail
  3. Full capacity suốt quá trình deploy — KHÔNG giảm compute
```

Đáp án đúng: **C** (blue/green qua CodeDeploy + CloudFormation + Elastic Beanstalk **Immutable**). Anh chọn **A** (blue/green + AWS SAM + Elastic Beanstalk **All at Once**).

#### Vì sao C đúng — Immutable giữ đúng full capacity

**Immutable deployment**: EB dựng **toàn bộ instance mới** (full set) trong **Auto Scaling Group riêng**, chạy song song với bản cũ. Nếu health check fail, EB **terminate instance mới**, instance cũ **không bị động tới** → zero downtime, full capacity luôn được giữ (bản cũ vẫn chạy đủ công suất suốt quá trình).

```
Deploy Immutable:
  ASG cũ (đang chạy, full capacity)  ──────────────► vẫn phục vụ request
  ASG mới (full set instance mới)    → health check
                                          │
                              Pass → swap traffic, xóa ASG cũ
                              Fail → terminate ASG mới, ASG cũ không đổi
```

**CloudFormation vs SAM:** đề không có yêu cầu đặc biệt về serverless framework; CloudFormation là lựa chọn TD chọn làm IaC chuẩn ở đây — không phải điểm quyết định chính, nhưng option đúng dùng CloudFormation.

#### Vì sao A (lựa chọn của Anh) sai — All at Once lấy instance ra khỏi service

**All at Once** deploy phiên bản mới cho **toàn bộ instance cùng lúc** → trong lúc deploy, các instance đó **tạm ngưng phục vụ** (out of service for a short time) → vi phạm trực tiếp yêu cầu "maintain full capacity... without any reduced compute capacity".

```
All at Once:  [instance1][instance2][instance3]
              tất cả đồng thời OUT OF SERVICE để update
              → capacity giảm xuống 0 trong lúc deploy
```

#### Option còn lại bị loại

| Option | Vấn đề |
|---|---|
| B | In-place deployment + **Rolling**: deploy theo batch, mỗi batch bị lấy ra khỏi service tạm thời → vẫn giảm capacity theo số instance trong batch |
| D | Blue/green qua **Amazon Lightsail** — Lightsail dành cho app đơn giản/dev-test, AWS không khuyến nghị cho enterprise mission-critical workload |

#### So sánh các deployment policy của Elastic Beanstalk

| Policy | Capacity trong lúc deploy | Rủi ro |
|---|---|---|
| All at once | Giảm về 0 tạm thời | Downtime |
| Rolling | Giảm theo batch size | Giảm capacity một phần |
| Rolling + additional batch | Giữ full (thêm batch trước khi rút) | Tốn thêm instance tạm |
| **Immutable** | **Giữ full suốt** (ASG mới song song) | Tốn gấp đôi instance tạm thời, nhưng an toàn nhất |

#### Lưu ý thực tế

- Immutable cũng tự động **ngăn deploy tiếp** nếu bản mới fail health check (vì ASG mới bị terminate, không có gì để tiếp tục) — khớp luôn yêu cầu "prevent subsequent deployments" trong đề.
- Blue/green ở cấp CodeDeploy (ngoài Elastic Beanstalk) và Immutable ở cấp Elastic Beanstalk là hai lớp khác nhau nhưng cùng mục đích zero-downtime — đề bài kết hợp cả hai.

#### Quy tắc nhớ cho thi

- **"Full capacity" + "no reduced capacity" trong lúc deploy** → **Elastic Beanstalk Immutable** (hoặc Rolling with additional batch nếu không có Immutable trong option).
- **All at once** và **Rolling** → luôn làm giảm capacity tạm thời, loại ngay khi đề nhấn "full capacity".
- **Lightsail** → chỉ cho dev/test, không cho enterprise/mission-critical.
- CloudFormation/SAM không phải điểm quyết định chính của câu này — đừng để bẫy vào chi tiết phụ, tập trung vào **deployment policy**.

### TD explanation

AWS Elastic Beanstalk provides several options for how deployments are processed, including deployment policies (All at once, Rolling, Rolling with additional batch, and Immutable) and options that let you configure the batch size and health check behavior during deployments. By default, your environment uses all-at-once deployments. If you created the environment with the EB CLI and it's an automatically scaling environment (you didn't specify the --single option), it uses rolling deployments.
With rolling deployments, Elastic Beanstalk splits the environment's EC2 instances into batches and deploys the new version of the application to one batch at a time, leaving the rest of the instances in the environment running the old version of the application. During a rolling deployment, some instances serve requests with the old version of the application, while instances in completed batches serve other requests with the new version.

To maintain full capacity during deployments, you can configure your environment to launch a new batch of instances before taking any instances out of service. This option is known as a rolling deployment with an additional batch. When the deployment completes, Elastic Beanstalk terminates the additional batch of instances.''
Immutable deployments perform an immutable update to launch a full set of new instances running the new version of the application in a separate Auto Scaling group alongside the instances running the old version. Immutable deployments can prevent issues caused by partially completed rolling deployments. If the new instances don't pass health checks, Elastic Beanstalk terminates them, leaving the original instances untouched.
Therefore, the correct answer is: Do a blue/green deployment on all upcoming changes using AWS CodeDeploy. Using AWS CloudFormation, launch the Amazon DynamoDB tables, AWS Lambda functions, and Amazon OpenSearch domain in your AWS VPC. Host the web application in AWS Elastic Beanstalk and set the deployment policy to Immutable.

The option that says: Do a blue/green deployment on all upcoming changes using AWS CodeDeploy. Using AWS SAM, launch the DynamoDB tables, Lambda functions, and Amazon OpenSearch domain in your AWS VPC. Host the web application in AWS Elastic Beanstalk and set the deployment policy to All at Once is incorrect. This policy deploys the new version to all instances simultaneously which means that the instances in your environment are out of service for a short time while the deployment occurs.
The option that says: Do an in-place deployment on all upcoming changes using AWS CodeDeploy. Using AWS SAM, launch the Amazon DynamoDB tables, Lambda functions, and Amazon OpenSearch domain in your AWS VPC. Host the web application in AWS Elastic Beanstalk and set the deployment policy to Rolling is incorrect. This policy will deploy the new version in batches where each batch is taken out of service during the deployment phase, reducing your environment's capacity by the number of instances in a batch.
The option that says: Do a blue/green deployment on all upcoming changes using Amazon Lightsail. Let Amazon Lightsail handle the provisioning of database instances, EC2 instances, and load balancers needed by the web application. Use CloudFormation to deploy the AWS Lambda functions, provision DynamoDB tables, and create an Amazon OpenSearch domain in your VPC is incorrect. Amazon Lightsail is a cost-effective solution for deploying simple web applications. AWS recommends it for DEV/Test environments, not for enterprise-ready, mission-critical workloads.

References:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html
https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html#welcome-deployment-overview
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environmentmgmt-updates-immutable.html

Check out this AWS Elastic Beanstalk Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-beanstalk/

</details>

<a id="q57"></a>

## Q57

A startup is building a mobile app and a custom GraphQL API backend that lets people post photos and videos of road potholes, faulty street lights, bridge damages, and other issues in the public infrastructure with 100-character summaries. The data gathered by the system will be used by the department of public works to facilitate fast resolution. The developers used a javascript-based React Native mobile framework so that it would run on various mobile and tablet devices. The app will be connecting to a custom GraphQL API that will be responsible for storing the photos and videos in an Amazon S3 bucket and will also access a DynamoDB table to store the summaries. The developers have recently deployed the mobile app prototype but it was found that there is an availability issue with the custom GraphQL API. To proceed with the project, the team decided to remove the API and instead, re-model the mobile app so that it will directly connect to both DynamoDB and S3 as well as handle user authentication.

Which of the following options provides the most cost-effective and scalable architecture for this project?

- **A.** 1. Set up a web identity federation using the AssumeRoleWithWebIdentity API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP. 2. Create an IAM role for that provider and set up permissions for the IAM role to allow access to S3 and DynamoDB. 3. The mobile app will use the AWS temporary security credentials to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.
- **B.** 1. Set up a web identity federation using the AssumeRole API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP. 2. Create an IAM user for that provider and set up permissions for the IAM user to allow access to S3 and DynamoDB. 3. The mobile app will use the AWS access and secret keys to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.
- **C.** 1. Set up a web identity federation using the AssumeRoleWithSAML API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP. 2. Create an IAM role for that provider and set up permissions for the IAM role to allow access to S3 and DynamoDB. 3. The mobile app will use the AWS temporary security credentials to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.
- **D.** 1. Set up a web identity federation using the AssumeRoleWithWebIdentity API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP. 2. Create an IAM role for that provider and set up permissions for the IAM role to allow access to S3 and DynamoDB. 3. The mobile app will use the AWS access and secret keys to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.
- **E.** 1. Set up a web identity federation using Cognito and social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP. 2. Configure the IAM role in Cognito to allow access to S3 and DynamoDB. 3. The mobile app will use the AWS access and secret keys to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** E

🔑 **Key words:** 🔁 mobile app, social IdPs, store to S3 and DynamoDB directly

🪤 **Your trap:** 🔁 The option uses long-term access keys — apps must use temporary STS credentials

🧠 **Rule:** Mobile/web app + social login → web identity federation (AssumeRoleWithWebIdentity / Cognito) with temporary credentials

### 🇻🇳 Phân tích chi tiết

#### ⚠️ Lỗi lặp lại — cùng concept đã làm đúng ở TD Set 1 redo, giờ chọn sai

```
Mobile app (React Native) ──social login (Amazon/Google/Facebook/OIDC)──► ???
        │
        └──► lưu photo/video vào S3
        └──► lưu summary vào DynamoDB
Yêu cầu: cost-effective + scalable, KHÔNG qua custom API backend
```

Đáp án đúng: **A** (web identity federation qua **AssumeRoleWithWebIdentity** + IAM role + **temporary STS credentials**). Anh chọn **E** (Cognito + social IdP nhưng dùng **AWS access/secret keys** trong mobile app).

Anh đã làm đúng concept "web identity federation cho mobile app dùng social login" ở lần redo TD Set 1. Lần này vẫn chọn đúng **cơ chế liên kết IdP** (Cognito/social login), nhưng lại chọn nhánh sai ở **bước cuối cùng** — loại credential mà app dùng để gọi AWS. Đây là lỗi lặp lại về cùng nguyên tắc cốt lõi: **mobile app không bao giờ được giữ access/secret key**.

#### Vì sao A đúng

Web identity federation hoạt động theo luồng:
```
User login qua Amazon/Google/Facebook/OIDC IdP
        │
        ▼
   Nhận authentication token từ IdP
        │
        ▼
AssumeRoleWithWebIdentity (STS) ──► đổi token thành TEMPORARY credentials
        │                           (access key + secret key + session token,
        │                            có thời hạn, tự hết hạn)
        ▼
   IAM role (quyền hạn chế: chỉ S3 + DynamoDB)
        │
        ▼
   App dùng temp credentials gọi S3/DynamoDB trực tiếp
```
Không cần custom backend, không cần tự quản lý user identity, và vì dùng **IAM role + temporary credentials**, app không bao giờ lưu trữ secret lâu dài.

#### Vì sao E (lựa chọn của Anh) sai — đúng cơ chế, sai loại credential

E dùng đúng **Cognito + social IdP** (một cách hợp lệ khác để làm web identity federation), nhưng bước 3 ghi: *"mobile app will use the AWS access and secret keys"* — đây là **long-term credentials**, nhúng trực tiếp vào app. TD giải thích thẳng: *"it is wrong to store and use the AWS access and secret keys from the mobile app itself. This is a security risk and you should use the temporary security credentials instead."*

```
E:  App ──giữ mãi──► access key + secret key  → nếu app bị decompile/leak, key KHÔNG hết hạn
A:  App ──giữ tạm──► temporary STS credentials → tự expire, giảm thiệt hại khi leak
```

#### Các option sai khác

| Option | Vấn đề |
|---|---|
| B | Dùng **AssumeRole** (không phải AssumeRoleWithWebIdentity) + tạo **IAM user** — sai API và sai loại principal cho social login |
| C | Dùng **AssumeRoleWithSAML** — API này dành cho SAML 2.0 (enterprise IdP), không phải social/OIDC IdP |
| D | Đúng AssumeRoleWithWebIdentity + IAM role, nhưng vẫn sai ở bước cuối — dùng access/secret keys thay vì temporary credentials (cùng lỗi như E) |

#### Lưu ý thực tế

- **AssumeRoleWithWebIdentity** = social/OIDC IdP (Google, Facebook, Amazon, Apple…). **AssumeRoleWithSAML** = enterprise SAML IdP (Active Directory Federation Services…). Hai API khác mục đích, không dùng lẫn.
- Dù dùng Cognito hay STS trực tiếp, nguyên tắc **không bao giờ nhúng long-term access/secret key vào client app** (mobile/web) là bất biến — bất kể IdP nào.

#### Quy tắc nhớ cho thi

- **Mobile/web app + social login (Google/Facebook/Amazon/OIDC)** → **AssumeRoleWithWebIdentity**, không phải AssumeRole hay AssumeRoleWithSAML.
- **SAML IdP (enterprise)** → **AssumeRoleWithSAML**.
- **Bất kỳ câu nào có "mobile app ... access and secret keys"** → **LUÔN SAI**, dù phần IdP/Cognito đúng. Mobile/web app chỉ được dùng **temporary STS credentials**.
- Mnemonic: **"App cầm chìa khóa vĩnh viễn = toang"** — chỉ cầm chìa khóa có hẹn giờ (temporary credentials).

### TD explanation

With web identity federation, you don't need to create custom sign-in code or manage your own user identities. Instead, users of your app can sign in using a well-known external identity provider (IdP), such as Login with Amazon, Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP. They can receive an authentication token, and then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions to use the resources in your AWS account. Using an IdP helps you keep your AWS account secure, because you don't have to embed and distribute long-term security credentials with your application.
In this scenario, you have a mobile app that needs to have access to the DynamoDB and S3 bucket. You can achieve this by using Web Identity Federation with AssumeRoleWithWebIdentity API which provides temporary security credentials and an IAM role.

Thus, the correct answer here is the following option:
1. Set up a web identity federation using the AssumeRoleWithWebIdentity API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP.
2. Create an IAM role for that provider and set up permissions for the IAM role to allow access to S3 and DynamoDB.
3. The mobile app will use the AWS temporary security credentials to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.

The following option is incorrect because you cannot use AssumeRole API and an IAM user in this scenario:
1. Set up a web identity federation using the AssumeRole API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP.
2. Create an IAM user for that provider and set up permissions for the IAM user to allow access to S3 and DynamoDB.
3. The mobile app will use the AWS access and secret keys to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.

The following option is incorrect because you should have used AssumRoleWithWebIdentity instead of AssumeRoleWithSAML API:
1. Set up a web identity federation using the AssumeRoleWithSAML API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP.
2. Create an IAM role for that provider and set up permissions for the IAM role to allow access to S3 and DynamoDB.
3. The mobile app will use the AWS temporary security credentials to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.

The following option is incorrect because it is a security risk to store and use the AWS access and secret keys from the mobile app itself:
1. Set up a web identity federation using the AssumeRoleWithWebIdentity API of STS and register with social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP.
2. Create an IAM role for that provider and set up permissions for the IAM role to allow access to S3 and DynamoDB.
3. The mobile app will use the AWS access and secret keys to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.

The following option is incorrect. Even though the use of Cognito is valid, it is wrong to store and use the AWS access and secret keys from the mobile app itself. This is a security risk and you should use the temporary security credentials instead:
1. Set up a web identity federation using Cognito and social identity providers like Amazon, Google, Facebook or any other OpenID Connect (OIDC)-compatible IdP.
2. Configure the IAM role in Cognito to allow access to S3 and DynamoDB.
3. The mobile app will use the AWS access and secret keys to store the photos and videos to an S3 bucket and persist the summaries to the DynamoDB database.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

---

# Group F — HA, hybrid & troubleshooting (3)

<a id="q6"></a>

## Q6

A financial company is building a new online document portal system that allows its employees and developers to upload yearly and bi-annual corporate earnings report files to a private Amazon S3 bucket in which other confidential corporate files will also be stored. A Solutions Architect was instructed to create the private S3 bucket as well as the IAM users for the application developers to begin development. The required policies in IAM were assigned to the developers, granting read and write access to the S3 bucket. After a few weeks, the new online portal was completed and hosted on a fleet of Amazon EC2 Spot instances.

One of the application developers created a pre-signed URL that points to the correct S3 bucket, and after a few tests, the developer successfully uploaded the files from a laptop using the generated URL. The developer then made the necessary code change to the online portal to generate the pre-signed URL to upload the files to S3. However, after a few days, the development team complained that uploading files using the online portal was no longer possible.

Which of the following options are valid reasons for this behavior? (Select TWO.)

- **A.** There was a recent change in the S3 bucket that allows object versioning which invalidates all presigned URLs.
- **B.** The application developers do not have access to either read or upload objects to the S3 bucket.
- **C.** The expiration date of the pre-signed URL is incorrectly set to expire too quickly and thus, may have already expired when they used it.
- **D.** The ACL of the S3 bucket blocks the online portal and prevents the developers from uploading any files.
- **E.** The required AWS credentials in the ~/.aws/credentials configuration file located on the EC2 instances of the online portal were misconfigured

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E · **You picked:** A, C

🔑 **Key words:** pre-signed URL works from laptop, fails from EC2 Spot portal

🪤 **Your trap:** Enabling versioning does not invalidate pre-signed URLs

🧠 **Rule:** Pre-signed URL failures → expired URL or the signer's credentials (EC2 should use an IAM role, not ~/.aws/credentials)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Developer laptop ──presigned URL──► S3 bucket    ✅ upload thành công
EC2 Spot (online portal) ──presigned URL──► S3 bucket   ❌ upload thất bại
                     ↑ không có IAM Role / ~/.aws/credentials bị sai
```

Multi-select (2 đáp án). Đáp án đúng: **C, E** (URL hết hạn + credentials trên EC2 bị sai cấu hình). Anh chọn **A, C** — đúng C, sai A (versioning).

#### C và E đúng — hai nguyên nhân thực tế hợp lý nhất

**C — pre-signed URL hết hạn:** pre-signed URL luôn có thời hạn (expiration) được set lúc generate. Nếu portal set thời gian quá ngắn hoặc có delay giữa lúc generate và lúc client thực sự dùng, URL sẽ hết hạn → upload fail. Đây khớp với việc **developer test trên laptop thành công** (dùng ngay, chưa hết hạn) nhưng **portal** (có thể độ trễ pipeline khác) lại fail.

**E — credentials trên EC2 bị misconfigured:** TD explanation nhấn mạnh: đề bài không hề nói portal có **IAM Role** gắn vào EC2, cũng không nói có credentials hợp lệ trong `~/.aws/credentials`. Pre-signed URL được ký bằng credentials của principal tạo nó — nếu EC2 không có credentials đúng (hoặc role không đủ quyền), việc generate presigned URL trên server sẽ dùng sai/không có credentials → URL sinh ra không hợp lệ.

```
Khuyến nghị thực tế (theo TD explanation):
EC2 instance ──attach──► IAM Role (instance profile)
    → nhận credentials tạm thời, tự động rotate qua IMDS
    → không cần quản lý static access key trong ~/.aws/credentials
    → đặc biệt quan trọng với EC2 SPOT vì instance có thể bị interrupt/replace bất kỳ lúc nào
```

#### A (Anh chọn) sai — vì sao trông hợp lý nhưng không đúng

Bật **object versioning** không có bất kỳ liên hệ nào với cơ chế pre-signed URL. Pre-signed URL chỉ ký (sign) một request S3 API call với thời hạn cụ thể; versioning chỉ ảnh hưởng đến việc S3 giữ lại nhiều phiên bản của object, không "invalidate" các URL đã ký trước đó. TD explanation nói thẳng: *"Enabling object versioning in S3 will simply not hinder uploads that are done via a pre-signed URL."*

#### Các lựa chọn sai khác

- **B — developers không có quyền đọc/ghi:** sai vì đề bài đã nói rõ IAM policy cấp quyền read/write cho developers, và thực tế một developer đã upload thành công — chứng minh quyền đã đủ.
- **D — ACL của bucket chặn portal:** sai vì cùng bucket, cùng ACL, một người (developer trên laptop) đã upload thành công — nếu ACL chặn thì phải chặn tất cả, không riêng gì portal.

| Lựa chọn | Có giải thích được "laptop OK, portal fail" không? |
|---|---|
| **C. URL expired** | Có — portal có thể có delay khiến URL hết hạn trước khi dùng |
| **E. EC2 credentials misconfigured** | Có — portal (EC2) thiếu role/credentials đúng để sign URL |
| A. Versioning | Không — versioning không ảnh hưởng presigned URL |
| B. Developers thiếu quyền | Không — policy đã cấp, và đã upload thành công 1 lần |
| D. ACL chặn | Không — cùng bucket, 1 lần upload đã thành công |

#### Lưu ý thực tế

- Pre-signed URL thừa hưởng **đúng permission của principal ký nó** — nếu credentials ký URL không đủ quyền hoặc hết hạn (với temporary credentials từ role), URL dù chưa tới expiration time đã đặt vẫn có thể fail.
- Với **Spot EC2**, instance bị interrupt/replace thường xuyên — nếu dùng static credentials file thay vì IAM role, dễ bị "mất" credentials khi instance mới launch mà quên cấu hình lại.

#### Quy tắc nhớ cho thi

- **Thấy "pre-signed URL work từ máy A, fail từ máy B"** → nghi ngay **credentials dùng để ký URL** ở máy B, hoặc **thời hạn URL**
- **Thấy "object versioning"** trong context presigned URL → luôn là distractor, không liên quan
- **Thấy EC2 cần gọi AWS API** → luôn ưu tiên **IAM Role/instance profile**, tránh static credentials trong `~/.aws/credentials`
- **Thấy "1 user đã thành công" nhưng "user khác fail"** → loại bỏ nguyên nhân chung (bucket policy/ACL), tìm nguyên nhân riêng (credentials/expiration của phía fail)

### TD explanation

In this scenario, the main issue is that the online portal cannot upload files to the S3 bucket, but the application developers can successfully upload files on their laptops. Take note that in this scenario, the online portal is deployed to a group of EC2 instances, and it was not mentioned that you attached an IAM Role to these instances, nor added security credentials in the ~/.aws/credentials configuration file.
With all of this data in mind, we can deduce that the online portal is generating pre-signed URLs that are set to have an overly tight expiration date, which causes the issue. In addition, there might be no security credentials added in the EC2 instances that host the online portal, considering that it is not mentioned in the scenario. Remember that this is required to properly generate the pre-signed URLs.

When deploying applications on EC2 instances that interact with AWS services such as Amazon S3, the recommended approach is to attach an IAM Role to the EC2 instances via an instance profile rather than storing long-lived IAM credentials in the ~/.aws/credentials configuration file.
An instance profile allows EC2 instances to automatically receive temporary, rotating credentials through the EC2 Instance Metadata Service (IMDS), removing the need to manually manage or rotate static access keys. This is particularly important when using Spot EC2 instances, which can be interrupted and replaced at any time, making static credential files both a security risk and an operational burden.
While the absence or misconfiguration of credentials in the ~/.aws/credentials.The file is a valid root cause of the failure in this scenario; the proper remediation is to assign the appropriate IAM Role to the EC2 instances so that the online portal can securely and reliably generate pre-signed URLs on behalf of the application.
Therefore, the correct answers are:
- The expiration date of the pre-signed URL is incorrectly set to expire too quickly and thus, may have already expired when they used it.
- The required AWS credentials in the ~/.aws/credentials configuration file located on the EC2 instances of the online portal were misconfigured.
The option that says: There was a recent change in the S3 bucket that allows object versioning which invalidates all presigned URLs is incorrect. Enabling object versioning in S3 will simply not hinder uploads that are done via a pre-signed URL.
The options that says: The application developers do not have access to either read or upload objects to the S3 bucket is incorrect. You have already assigned the required IAM policies to the developers' IAM users that grant them read and write access to the S3 bucket.
The option that says: The ACL of the S3 bucket blocks the online portal and prevents the developers from uploading any files is incorrect because this is primarily not an issue; one developer has already successfully uploaded a file to the S3 bucket, which confirms that the bucket ACL is not the root cause of the problem.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html
https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-presigned-urls.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q8"></a>

## Q8

A leading aerospace engineering company is experiencing high growth and demand on their highly available and fault-tolerant cloud services platform that is hosted in AWS. The technical lead of your team has asked you to virtually extend two existing on-premises data centers into AWS cloud to support an online flight-tracking service that is used by a lot of airline companies. The online service heavily depends on existing, on-premises resources located in multiple data centers and static content that is served from an S3 bucket. To meet the requirement, you launched a dual-tunnel VPN connection between your CGW and VGW.

In this scenario, which component of your cloud architecture represents a potential single point of failure, which you should consider changing to make the solution more highly available?

- **A.** Create another Customer Gateway in a different data center and set up another dual-tunnel VPN connection.
- **B.** Set up a NAT Gateway in a different data center and set up another dual-tunnel VPN connection.
- **C.** Create another Virtual Gateway in a different AZ and create another dual-tunnel VPN connection.
- **D.** Create a second Virtual Gateway in a different AZ and a Customer Gateway in a different data center. Create another dual-tunnel connection to ensure high-availability and fault-tolerance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** single point of failure, dual-tunnel VPN between CGW and VGW

🪤 **Your trap:** A VPC can attach only one VGW — a 'second VGW' is impossible

🧠 **Rule:** VPN HA: VGW is already redundant (2 tunnels); add a second CGW in another data center

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises DC            VPC
┌──────────┐  dual-tunnel  ┌─────────┐
│   CGW    │◄─────VPN─────►│   VGW   │
└──────────┘   (2 tunnels)  └─────────┘
      ↑ single point of failure nằm ở đâu?
```

Đáp án đúng: **A** (tạo thêm 1 CGW ở data center khác + 1 kết nối dual-tunnel mới). Anh chọn **D** (thêm VGW + CGW) — sai vì VGW không thể tạo thêm.

#### A đúng — vì sao CGW là điểm cần nhân bản

TD explanation nêu rõ:

```
Site-to-Site VPN = 2 tunnel GIỮA 1 VGW (phía AWS) và 1 CGW (phía on-prem)
    → VGW: ĐÃ redundant sẵn (2 tunnel, AWS quản lý, không phải single point)
    → CGW: đại diện cho 1 thiết bị VPN tại 1 data center cụ thể
           → NẾU data center đó mất kết nối/down, toàn bộ VPN chết
           → đây chính là single point of failure
```

Giải pháp: **tạo thêm một CGW thứ hai đặt ở data center khác** (độc lập về vị trí vật lý) và thiết lập thêm một kết nối dual-tunnel VPN mới từ CGW đó tới VGW hiện có. Lúc này nếu một data center gặp sự cố, data center còn lại vẫn duy trì kết nối.

#### D (Anh chọn) sai — giới hạn nền tảng bị bỏ qua

**Chỉ một VGW có thể attach vào một VPC tại một thời điểm.** Đây là limit cứng của VPC, không phải vấn đề thiết kế. TD explanation nhắc hai lần: *"There can only be one VGW attached to a VPC at a given time."* Vì vậy "tạo thêm VGW" (dù kèm AZ khác hay CGW khác) là **không thể thực hiện được về mặt kỹ thuật** — không phải là chưa tối ưu mà là invalid.

#### Các lựa chọn sai khác

- **C — thêm VGW ở AZ khác:** cùng lý do trên, VGW là tài nguyên gắn 1-1 với VPC, không nhân bản theo AZ được.
- **B — thêm NAT Gateway ở data center khác:** NAT Gateway không liên quan gì đến kết nối Site-to-Site VPN; NAT chỉ dùng để instance trong private subnet ra Internet mà không bị truy cập ngược từ ngoài vào. Hoàn toàn sai bản chất vấn đề.

| Lựa chọn | Có khả thi về kỹ thuật? | Giải quyết đúng SPOF? |
|---|---|---|
| **A. Thêm CGW ở DC khác + dual-tunnel mới** | Có | Có — đúng điểm SPOF là CGW |
| B. Thêm NAT Gateway | Có (nhưng vô nghĩa ở đây) | Không liên quan |
| C. Thêm VGW ở AZ khác | **Không** — vi phạm 1 VGW/VPC | — |
| D. Thêm VGW + CGW | **Không** — vi phạm 1 VGW/VPC | — |

#### Lưu ý thực tế

- VGW đã tự redundant ở tầng AWS (2 tunnel endpoint khác nhau) — đề thi SAP hay đưa ra bẫy "thêm VGW" vì nghe có vẻ hợp lý với tư duy HA kiểu ALB/multi-AZ, nhưng VGW không hoạt động theo mô hình đó.
- Muốn HA hơn nữa (nhiều site, nhiều VPC), AWS thực tế khuyến nghị **Transit Gateway** thay cho VGW riêng lẻ — nhưng câu hỏi này giữ nguyên scope VGW/CGW cơ bản.

#### Quy tắc nhớ cho thi

- **Thấy "VGW" + "thêm một VGW nữa"** → luôn sai, chỉ **1 VGW/VPC**
- **Thấy "Site-to-Site VPN single point of failure"** → điểm yếu nằm ở **CGW** (thiết bị on-prem), không phải VGW
- **Thấy "thêm CGW ở data center khác"** → đúng hướng tăng HA cho VPN hybrid
- **Thấy "NAT Gateway"** trong câu hỏi về VPN connectivity → distractor, NAT không liên quan Site-to-Site VPN

### TD explanation

In this question, you will easily get confused if you do not know the basics of VPC and other AWS fundamentals. You can eliminate the obviously wrong answers and then just choose between the remaining options.
Remember that only one virtual private gateway (VGW) can be attached to a VPC at a time.
A Site-to-Site VPN connection offers two VPN tunnels between a virtual private gateway or a transit gateway on the AWS side, and a customer gateway (which represents a VPN device) on the remote (on-premises) side. A virtual private gateway is the VPN concentrator on the Amazon side of the Site-to-Site VPN connection. You create a virtual private gateway and attach it to the VPC from which you want to create the Site-to-Site VPN connection.

The correct answer is: Create another Customer Gateway in a different data center and setting up another dual-tunnel VPN connection. This will ensure high availability for your online flight-tracking service.
The option that says: Create another Virtual Gateway in a different AZ and create another dual-tunnel VPN connection is incorrect. There can only be one VGW attached to a VPC at a given time.
The option that says: Create a second Virtual Gateway in a different AZ and a Customer Gateway in a different data center. Create another dual-tunnel connection to ensure high-availability and fault-tolerance is incorrect. There can only be one VGW attached to a VPC at a given time.
The option that says: Setting up a NAT Gateway in a different data center and setting up another dual-tunnel VPN connection is incorrect. You don't need to use a NAT gateway in this situation. NAT is basically used to enable EC2 instances launched in the private subnet to access the Internet while blocking incoming public requests to the VPC.

References:
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html
https://docs.aws.amazon.com/AmazonVPC/latest/NetworkAdminGuide/Introduction.html
https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

<a id="q58"></a>

## Q58

A company is building an innovative AI-powered traffic monitoring portal and uses the AWS Global Infrastructure to host its cloud infrastructure. The application should track key performance indicators (KPIs) such as traffic flow, congestion levels, and incident response times across the city.

For the initial deployment, the application would be used by an entire city. The application must meet strict recovery point objectives and recovery time objectives to ensure it remains highly available and fault-tolerant to avoid unnecessary downtime.

Which of the following options is the MOST suitable architecture to implement?

- **A.** Launch an AWS Auto Scaling group of Amazon EC2 instances on two Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration. Use Amazon Route 53 and create an A record that points to the ELB.
- **B.** Launch an AWS Auto Scaling group of Amazon EC2 instances on three Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Amazon Aurora with Aurora Replicas as the database tier. Use Amazon Route 53 and create an Alias record that points to the ELB.
- **C.** Use Amazon ElastiCache for the database caching of the portal. Launch an AWS Auto Scaling group of Amazon EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration and Read Replicas. Use Amazon Route 53 and create a CNAME that points to the ELB.
- **D.** Use Amazon DynamoDB as the database of the portal. Launch an AWS Auto Scaling group of Amazon EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Amazon Route 53 and create an A record that points to the ELB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** strict RPO/RTO, highly available, fault-tolerant, single city

🪤 **Your trap:** DynamoDB + an A record (not alias) to the ELB — an ELB has no fixed IP

🧠 **Rule:** HA web tier → ASG across 3 AZs + ALB + Aurora Replicas; Route 53 Alias record to the ELB

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                    Route 53 (?)
                        │
                       ALB
                        │
         ASG EC2 (bao nhiêu AZ?)
                        │
                  DB tier (loại gì?)
Yêu cầu: strict RPO/RTO, HA + fault-tolerant, 1 thành phố
```

Đáp án đúng: **B** (ASG 3 AZ + ALB + Aurora Replicas + Route 53 **Alias**). Anh chọn **D** (DynamoDB + Route 53 **A record**) — sai chủ yếu ở loại record Route 53.

#### B đúng — điểm phân biệt duy nhất là Route 53 record type

TD explanation nói thẳng: *"In this scenario, all of the options are highly available architectures. The main difference here is how they use Route 53."* Tức là ASG nhiều AZ, ALB, các loại DB (Aurora/RDS/DynamoDB) ở 4 lựa chọn đều đủ HA — **điểm quyết định nằm ở loại DNS record trỏ vào ELB**:

```
ELB (ALB/CLB) KHÔNG có địa chỉ IP cố định
   → IP có thể đổi theo thời gian (scale, AZ failover...)
   → Route 53 A record trỏ vào 1 IP tĩnh  → SAI, sẽ lỗi khi IP đổi
   → Route 53 Alias record trỏ vào DNS name của ELB → ĐÚNG,
     tự động theo dõi IP thay đổi, miễn phí (không tính query),
     hỗ trợ health check tích hợp
```

Lựa chọn B dùng đúng Alias record → là lựa chọn hợp lệ duy nhất về mặt DNS pointing tới ELB.

#### D (Anh chọn) sai — vì sao trông hợp lý nhưng vi phạm nguyên tắc DNS-ELB

D có vẻ hấp dẫn vì DynamoDB serverless + 4 AZ (nhiều hơn B's 3 AZ) nghe "HA hơn", nhưng TD explanation chỉ rõ: *"To route domain traffic to an ELB load balancer, use Amazon Route 53 to create an alias resource record set that points to your load balancer."* Dùng **A record trỏ vào ELB bằng IP là sai về nguyên tắc** — ELB không có IP cố định để A record tham chiếu bền vững; lưu ý số lượng AZ hay loại DB tier không phải là tiêu chí phân biệt chính ở câu này.

#### Các lựa chọn sai khác

- **A — 2 AZ + MySQL RDS Multi-AZ + Route 53 A record:** sai vì A record (không phải vì 2 AZ — TD explanation không chê điểm AZ, chỉ chê record type).
- **C — 4 AZ + ElastiCache + MySQL RDS Multi-AZ/Read Replicas + Route 53 CNAME:** sai vì **CNAME** cũng không phải loại record đúng để trỏ domain gốc (apex) vào ELB; TD explanation: *"You have to use an Alias record to route to the ELB and not a CNAME record."*

| Lựa chọn | Route 53 record | Đúng/Sai |
|---|---|---|
| **B. Aurora Replicas, 3 AZ** | **Alias** | Đúng |
| A. RDS Multi-AZ, 2 AZ | A record | Sai |
| C. RDS Multi-AZ + Read Replica, 4 AZ | CNAME | Sai |
| D. DynamoDB, 4 AZ | A record | Sai |

#### Lưu ý thực tế

- **CNAME record không được phép trỏ domain apex** (ví dụ `example.com`, không phải `www.example.com`) theo chuẩn DNS; Alias record của Route 53 giải quyết đúng hạn chế này và miễn phí.
- Nhiều AZ hơn (4 so với 3) hay DB serverless (DynamoDB) không tự động thắng — đề thi SAP thường gài "nhiều AZ hơn trông HA hơn" làm trap để đánh lạc hướng khỏi điểm khác biệt thật (ở đây là DNS record type).

#### Quy tắc nhớ cho thi

- **Thấy "Route 53 record trỏ vào ELB/ALB/CLB"** → luôn phải là **Alias record**, không bao giờ là A record hay CNAME
- **Thấy nhiều lựa chọn "đều có vẻ HA"** → tìm điểm khác biệt thật theo đúng câu TD hay dùng: so sánh từng trục (AZ count, DB type, DNS record) riêng biệt
- **Thấy "số AZ nhiều hơn" hoặc "DB serverless"** → không tự động là tín hiệu đúng nếu điểm khác biệt chính của câu nằm ở chỗ khác

### TD explanation

Suppose that you start out running your app or website on a single EC2 instance, and over time, traffic increases to the point that you require more than one instance to meet the demand. You can launch multiple EC2 instances from your AMI and then use Elastic Load Balancing to distribute incoming traffic for your application across these EC2 instances. This increases the availability of your application. Placing your instances in multiple Availability Zones also improves the fault tolerance in your application. If one Availability Zone experiences an outage, traffic is routed to the other Availability Zone.

You can use Amazon EC2 Auto Scaling to maintain a minimum number of running instances for your application at all times. Amazon EC2 Auto Scaling can detect when your instance or application is unhealthy and replace it automatically to maintain the availability of your application. You can also use Amazon EC2 Auto Scaling to scale your Amazon EC2 capacity up or down automatically based on demand, using criteria that you specify.
In this scenario, all of the options are highly available architectures. The main difference here is how they use Route 53.
The correct answer is the option that says: Launch an Auto Scaling group of EC2 instances on three Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Amazon Aurora with Aurora Replicas as the database tier. Use Route 53 and create an Alias record that points to the ELB. It uses the correct type of record in Route 53, which is an alias record, to point to the ELB.
The option that says: Launch an Auto Scaling group of EC2 instances on two Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration. Use Route 53 and create an A record that points to the ELB is incorrect. You need to create an Alias record with the DNS name and not a normal A-record that points to an IP address.
The option that says: Use DynamoDB as the database of the portal. Launch an Auto Scaling group of EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Route 53 and create an A record that points to the ELB is incorrect. To route domain traffic to an ELB load balancer, use Amazon Route 53 to create an alias resource record set that points to your load balancer.
The option that says: Use ElastiCache for the database caching of the portal. Launch an Auto Scaling group of EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration and Read Replicas. Use Route 53 and create a CNAME that point to the ELB is incorrect. You have to use an Alias record to route to the ELB and not a CNAME record.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html

Check out this Amazon Route 53 Cheat Sheet:
https://tutorialsdojo.com/amazon-route-53/

Tutorials Dojo's AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>
