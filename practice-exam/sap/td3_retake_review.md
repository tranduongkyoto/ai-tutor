# TD Set 3 — Timed retake (2026-10-21) — Wrong Answer Review (9 questions)

Source: `td3_retake_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td3_retake_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q1](#q1) | ✅ 10-21 | ☐ | ☐ |
| A | [Q40](#q40) | ✅ 10-21 | ☐ | ☐ |
| A | [Q41](#q41) | ✅ 10-21 | ☐ | ☐ |
| A | [Q56](#q56) | ✅ 10-21 | ☐ | ☐ |
| A | [Q62](#q62) | ✅ 10-21 | ☐ | ☐ |
| B | [Q34](#q34) | ✅ 10-21 | ☐ | ☐ |
| B | [Q47](#q47) | ✅ 10-21 | ☐ | ☐ |
| C | [Q38](#q38) | ✅ 10-21 | ☐ | ☐ |
| C | [Q68](#q68) | ✅ 10-21 | ☐ | ☐ |

---

# Group A — Repeat misses (missed before, again now) (5)

<a id="q1"></a>

## Q1

A business news portal is visited by thousands of readers each day to check on the latest hot topics in the world of business and technology. The news portal runs on a fleet of Spot Amazon EC2 instances behind an Application Load Balancer (ALB). Readers can also submit comments in every article. Currently, the system’s database is running on an on-premises data center, and the CTO is concerned that the content delivery time is not meeting company objectives. The portal’s page load time is of utmost importance for the company to maintain its daily visitors.

Which of the following options would allow the solutions architect to quickly and cost-effectively modify the current infrastructure to reduce latency for customers?

- **A.** Add an in-memory datastore using Amazon ElastiCache for Redis to reduce the burden on the database. Enable Redis replication to scale database reads and to have highly available clusters.
- **B.** Migrate your database on-premises to Amazon Aurora using the AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (SCT). Create Aurora Replicas across Availability Zones and reconfigure the web servers to query from the Aurora database instead.
- **C.** Create an Amazon CloudFront web distribution to speed up the delivery of data to their readers around the globe. Migrate the entire portal to an Amazon S3 bucket and then enable static web hosting. Set the S3 bucket as the origin of your CloudFront distribution.
- **D.** Replace the on-premises database of the news portal with a fast, scalable full-text search engine using Amazon OpenSearch Service by setting up an ELK stack (Elasticsearch, Logstash, and Kibana). Use an Amazon CloudFront web distribution to speed up the delivery of data to your users across the globe.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** on-premises database; page load latency; quickly and cost-effectively; Spot EC2 behind ALB; reduce latency

🪤 **Your trap:** 🔁 Picked B: Aurora migration via DMS/SCT is slow and costly, engine support not guaranteed. Question wants quick, cheap fix; ElastiCache in VPC cuts trips to on-prem DB.

🧠 **Rule:** DB latency plus quick and cost-effective: add ElastiCache cache in front of DB; do not migrate the database.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Readers ──► ALB ──► Spot EC2 (web, trong AWS VPC)
                        │
                        │  mỗi request đều đi qua link dài
                        ▼
                 Database ON-PREMISES  ◄── điểm nghẽn latency
```

Yêu cầu chốt: **giảm latency**, làm **nhanh** và **rẻ** (quickly + cost-effectively), trang vẫn **dynamic** (readers gửi comment). Đáp án đúng: **A (ElastiCache for Redis)**. Anh chọn B (migrate sang Aurora).

⚠️ Lỗi lặp lại: câu này sai ở cả lần 10-05 lẫn lần retake. Bẫy cố định: thấy "database chậm/ở xa" là phản xạ chọn "migrate DB". Đề lại hỏi **quick + cost-effective**.

#### Vì sao A đúng

- Vấn đề cốt lõi (theo TD): **latency tới backend database** ở on-premises.
- Đặt **in-memory cache trong VPC** cạnh web servers: dữ liệu hay đọc, ít đổi được cache lại → trả lời **sub-millisecond**, không phải gọi về data center mỗi request.
- Trả giá query một lần, các lần đọc sau lấy từ cache. Khoảng cách vật lý tới DB gốc gần như hết ảnh hưởng.
- Redis replication → scale đọc + cluster HA. Không phải đụng schema, engine hay dữ liệu.

#### Vì sao B (pick của anh) sai

Aurora nghe "nhanh hơn" nên trông hợp lý, nhưng:

- Migrate bằng **DMS + SCT** là dự án lớn, **không nhanh**.
- TD: **không đảm bảo** engine hiện tại được Aurora hỗ trợ.
- Chạy Aurora + replicas nhiều AZ → chi phí cao, ngược "cost-effective".
- Đổi sang Aurora không tự giải quyết "đọc lặp lại cùng dữ liệu"; cache làm việc đó rẻ hơn.

#### Các phương án còn lại

- **C sai:** portal có **comment từ readers** nên là website **dynamic**, không host tĩnh trên S3 được dù có CloudFront.
- **D sai:** OpenSearch dùng cho search/log analytics, **không phải database chính**. Có thể làm lớp phụ, không thay thế DB.

| Phương án | Giải quyết latency DB? | Nhanh/rẻ? | Vấn đề |
|---|---|---|---|
| **A. ElastiCache Redis** | Có (cache trong VPC) | Có | Không |
| B. Aurora + DMS/SCT | Có nhưng tốn công | Không | Engine support, chi phí, thời gian |
| C. S3 static + CloudFront | Không phù hợp | - | Site dynamic |
| D. OpenSearch | Không | - | Không phải DB |

#### Quy tắc nhớ cho thi

- **Thấy "latency tới DB" + "quickly/cost-effectively"** → **ElastiCache (cache)**, không phải migrate DB.
- **Thấy "readers submit comments / user input"** → site dynamic, loại **S3 static hosting**.
- **Thấy "OpenSearch"** → search/analytics, không bao giờ là DB chính.
- Mnemonic: **chậm vì đọc lặp → cache trước, migrate sau.**

### TD explanation

The success of the website and business is significantly affected by the speed at which you deliver content. Even the most optimized database query or remote API call is going to be noticeably slower than retrieving a flat key from an in-memory cache.

The primary purpose of an in-memory key-value store is to provide ultrafast (submillisecond latency) and inexpensive access to copies of data. Most data stores have areas of data that are frequently accessed but seldom updated. Additionally, querying a database is always slower and more expensive than locating a key in a key-value pair cache. By caching such query results, you pay the price of the query once and then are able to quickly retrieve the data multiple times without having to re-execute the query.

With the cache inside the VPC along with the web servers and application servers, the application doesn’t have to constantly go from AWS to the local data center. This change makes the physical distance between servers irrelevant. The new architecture should greatly improve the customer experience.

Therefore, the correct answer is: Add an in-memory datastore using Amazon ElastiCache for Redis to reduce the burden on the database. Enable Redis replication to scale database reads and to have highly available clusters. The main issue in this problem involves latency to the backend database. This solution dramatically reduces data retrieval latency. It also scales request volume considerably, because Amazon ElastiCache can deliver extremely high request rates, measured at over 20 million per second.

The option that says: Migrate your database on-premises to Amazon Aurora using the AWS Database Migration Service (AWS DMS) and AWS Schema Conversion Tool (SCT). Create Aurora Replicas across Availability Zones and reconfigure the web servers to query from the Aurora database instead is incorrect. There is no guarantee that the database engine currently being used by the news portal is supported by Amazon Aurora. It is also important to take note that the question asks for a quick and cost-effective solution. Migrating the database may typically take a long amount of time, and the number of requests being sent each day can rack up costs.

The option that says: Replace the on-premises database of the news portal with a fast, scalable full-text search engine using Amazon OpenSearch Service by setting up an ELK stack (Elasticsearch, Logstash, and Kibana). Use an Amazon CloudFront web distribution to speed up the delivery of data to your users across the globe is incorrect. OpenSearch is primarily used for log analytics, full-text search, security intelligence, business analytics, and operational intelligence use cases but not as a full-fledged database. A search engine could possibly be beneficial to the news portal as an additional layer but not as its sole data source. This solution might provide some advantages when they are both integrated together.

The option that says: Create an Amazon CloudFront web distribution to speed up the delivery of data to their readers around the globe. Migrate the entire portal to an Amazon S3 bucket and then enable static web hosting. Set the S3 bucket as the origin of your CloudFront distribution is incorrect. It is stated in the scenario that the readers can also submit their comments in every article, which means that the news portal is a dynamic website and not static. Hence, using S3 is not suitable for this scenario which is why this option is incorrect, even though it mentions the use of CloudFront web distribution.

 

References:

https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/elasticache-use-cases.html

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.Redis-RedisCluster.html

 

Check out this Amazon ElastiCache Cheat Sheet:

https://tutorialsdojo.com/amazon-elasticache/

![](https://media.tutorialsdojo.com/sap_elasticache_how_it_works.png)

![](https://media.tutorialsdojo.com/sap_aws_reduce_latency.jpg)

</details>

<a id="q40"></a>

## Q40

A company is building an innovative AI-powered traffic monitoring portal and uses the AWS Global Infrastructure to host its cloud infrastructure. The application should track key performance indicators (KPIs) such as traffic flow, congestion levels, and incident response times across the city.

For the initial deployment, the application would be used by an entire city. The application must meet strict recovery point objectives and recovery time objectives to ensure it remains highly available and fault-tolerant to avoid unnecessary downtime.

Which of the following options is the MOST suitable architecture to implement?

- **A.** Launch an AWS Auto Scaling group of Amazon EC2 instances on two Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration. Use Amazon Route 53 and create an A record that points to the ELB.
- **B.** Use Amazon ElastiCache for the database caching of the portal. Launch an AWS Auto Scaling group of Amazon EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration and Read Replicas. Use Amazon Route 53 and create a CNAME that points to the ELB.
- **C.** Use Amazon DynamoDB as the database of the portal. Launch an AWS Auto Scaling group of Amazon EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Amazon Route 53 and create an A record that points to the ELB.
- **D.** Launch an AWS Auto Scaling group of Amazon EC2 instances on three Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Amazon Aurora with Aurora Replicas as the database tier. Use Amazon Route 53 and create an Alias record that points to the ELB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** strict RPO/RTO; highly available fault-tolerant; Route 53 record type pointing to ELB; Aurora Replicas

🪤 **Your trap:** 🔁 Picked B: CNAME to ELB is wrong. Route 53 must use an Alias record for ELB; ElastiCache and four AZs do not fix the record type.

🧠 **Rule:** All options look highly available: the Route 53 record decides. Point to ELB with Alias, not A record or CNAME.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
User ──► Route 53 ──?──► ALB ──► ASG EC2 (nhiều AZ) ──► Database HA
                  ▲
         loại record nào trỏ tới ELB?
```

Đề nói thẳng: mọi phương án đều HA/fault-tolerant; điểm khác nhau nằm ở cách dùng **Route 53**. Đáp án đúng: **D (Alias record)**. Anh chọn B (CNAME).

⚠️ Lỗi lặp lại: câu này sai ở cả lần 10-05 lẫn retake. Anh cứ bị hút vào các chi tiết HA (ElastiCache, Read Replicas, 4 AZ) mà bỏ qua chi tiết **loại DNS record**.

#### Vì sao D đúng

- Trỏ domain tới ELB phải dùng **Alias record** của Route 53 (TD).
- Alias trỏ thẳng tới DNS name của ELB, Route 53 tự theo dõi thay đổi IP phía sau ELB.
- Phần còn lại cũng đủ: ASG 3 AZ + ALB + **Aurora với Aurora Replicas** (storage nhân bản 6 bản qua 3 AZ, failover nhanh) cho RTO/RPO chặt.

#### Vì sao B (pick của anh) sai

B trông "mạnh nhất" (ElastiCache + Multi-AZ + Read Replicas + 4 AZ), nhưng dùng **CNAME** để trỏ ELB. TD: phải dùng **Alias record**, không phải CNAME.

#### Các phương án còn lại

- **A sai:** dùng **A record** bình thường. Alias cần DNS name của ELB, còn A record thường trỏ IP, mà IP của ELB thay đổi.
- **C sai:** cũng **A record** trỏ ELB, dù DynamoDB + 4 AZ thì HA tốt.

| Phương án | Record trỏ ELB | Đúng? |
|---|---|---|
| A (RDS Multi-AZ, 2 AZ) | A record | Sai record |
| B (ElastiCache + RR, 4 AZ) | CNAME | Sai record |
| C (DynamoDB, 4 AZ) | A record | Sai record |
| **D (Aurora, 3 AZ)** | **Alias** | **Đúng** |

📝 Ghi chú kỹ thuật: trong thực tế, CNAME vẫn có thể trỏ một subdomain tới tên DNS của ELB, nhưng **không dùng được ở zone apex** (ví dụ `example.com`), và Alias thì miễn phí truy vấn tới AWS resource. Với đề thi, hễ trỏ domain tới ELB thì chọn **Alias**.

#### Quy tắc nhớ cho thi

- **Thấy "Route 53 → ELB/CloudFront/S3 website"** → **Alias record**.
- **Khi mọi phương án đều HA** → nhìn chi tiết nhỏ: loại record DNS.
- **A record / CNAME trỏ ELB** → loại.
- Mnemonic: **ELB không có IP cố định, nên không dùng A; apex không CNAME được, nên Alias.**

### TD explanation

Suppose that you start out running your app or website on a single EC2 instance, and over time, traffic increases to the point that you require more than one instance to meet the demand. You can launch multiple EC2 instances from your AMI and then use Elastic Load Balancing to distribute incoming traffic for your application across these EC2 instances. This increases the availability of your application. Placing your instances in multiple Availability Zones also improves the fault tolerance in your application. If one Availability Zone experiences an outage, traffic is routed to the other Availability Zone.

You can use Amazon EC2 Auto Scaling to maintain a minimum number of running instances for your application at all times. Amazon EC2 Auto Scaling can detect when your instance or application is unhealthy and replace it automatically to maintain the availability of your application. You can also use Amazon EC2 Auto Scaling to scale your Amazon EC2 capacity up or down automatically based on demand, using criteria that you specify.

In this scenario, all of the options are highly available architectures. The main difference here is how they use Route 53.

The correct answer is the option that says: Launch an Auto Scaling group of EC2 instances on three Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Amazon Aurora with Aurora Replicas as the database tier. Use Route 53 and create an Alias record that points to the ELB. It uses the correct type of record in Route 53, which is an alias record, to point to the ELB.

The option that says: Launch an Auto Scaling group of EC2 instances on two Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration. Use Route 53 and create an A record that points to the ELB is incorrect. You need to create an Alias record with the DNS name and not a normal A-record that points to an IP address.

The option that says: Use DynamoDB as the database of the portal. Launch an Auto Scaling group of EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use Route 53 and create an A record that points to the ELB is incorrect. To route domain traffic to an ELB load balancer, use Amazon Route 53 to create an alias resource record set that points to your load balancer.

The option that says: Use ElastiCache for the database caching of the portal. Launch an Auto Scaling group of EC2 instances on four Availability Zones. Attach an application load balancer to the Auto Scaling Group. Use a MySQL RDS instance with Multi-AZ deployments configuration and Read Replicas. Use Route 53 and create a CNAME that point to the ELB is incorrect. You have to use an Alias record to route to the ELB and not a CNAME record.

 

References:

https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html

 

Check out this Amazon Route 53 Cheat Sheet:

https://tutorialsdojo.com/amazon-route-53/

 

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:

https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

![](https://media.tutorialsdojo.com/sap_alb_cross_zone.PNG)

</details>

<a id="q41"></a>

## Q41

A company is hosting its three-tier web application on the us-east-1 region of AWS. The web and application tiers are stateless and both are running on their own fleet of On-Demand Amazon EC2 instances, each with its respective Auto Scaling group. The database tier is running on an Amazon Aurora database with about 40 TB of data. As part of the business continuity strategy of the company, the Solutions Architect must design a disaster recovery plan in case the primary region fails. The application requires an RTO of 30 minutes and the data tier requires an RPO of 5 minutes.

Which of the following options should the Solution Architect implement to achieve the company requirements in a cost-effective manner? (Select TWO.)

- **A.** For a quick recovery time, set up a hot-standby of web and application tier on the backup region. Redirect the traffic to the backup region in case of a disaster in the primary region.
- **B.** Schedule a daily snapshot of the Amazon EC2 instances for the web and application tier. Copy the snapshot to the backup region. Restore the backups in case of a disaster in the primary region.
- **C.** Configure an automated snapshot of the Amazon Aurora database every 5 minutes. Quickly restore the database on the backup region in case of a disaster in the primary region.
- **D.** Set up a cross-Region read replica of the Amazon Aurora database to the backup region. Promote this read replica as the master database in case of a disaster in the primary region.
- **E.** Use AWS Backup to create a backup job that will copy the EC2 EBS volumes and RDS data to an Amazon S3 bucket in another region. Restore the backups in case of a disaster in the primary region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** A, D

🔑 **Key words:** Aurora 40 TB; RTO 30 minutes; RPO 5 minutes; stateless web/app tiers; cost-effective; Select TWO

🪤 **Your trap:** 🔁 Picked A and D: D right, but hot-standby web/app tier is not cost-effective. Stateless tiers only need daily EBS snapshot copied cross-Region; 30-minute RTO is enough.

🧠 **Rule:** Stateless tiers: cheap cross-Region snapshot copy. Aurora data tier: cross-Region read replica for RPO, promote on disaster.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
us-east-1 (primary)                    Backup region
┌──────────────────────┐               ┌──────────────────────────┐
│ Web/App (stateless)  │ snapshot copy │ AMI/snapshot sẵn, dựng   │
│ Aurora 40 TB         │ ────────────► │ lại khi disaster (B)     │
│                      │ async replica │ Cross-Region read replica│
└──────────────────────┘ ────────────► │ -> promote khi cần (D)   │
                                       └──────────────────────────┘
RTO 30 phút, RPO data tier 5 phút, phải COST-EFFECTIVE
```

Đáp án đúng: **B + D**. Anh chọn A + D. D đúng, A sai, thiếu B.

⚠️ Lỗi lặp lại: câu này sai ở cả lần 10-05 lẫn retake, cùng một bẫy "hot-standby cho nhanh". Đề nhấn **cost-effective**, và web/app tier là **stateless**.

#### Hai đáp án đúng ghép thành một giải pháp

- **D (Aurora cross-Region read replica):** replicate **asynchronous** sang region backup, nên khi primary chết replica có dữ liệu gần nhất, đáp ứng **RPO 5 phút**. **Promote** nhanh, không chờ restore snapshot 40 TB có thể vượt RTO 30 phút.
- **B (snapshot EC2 hàng ngày, copy sang backup region):** web/app tier **stateless**, không có dữ liệu quan trọng, nên snapshot cũ cũng đủ. **30 phút** là dư thời gian để dựng instance mới. Rẻ vì không chạy gì khi bình thường.

#### Vì sao A (pick của anh) sai

A là hot-standby: web/app chạy liên tục ở DR region. Về kỹ thuật làm được, nhưng theo TD **không cost-effective** vì phải trả tiền cho tài nguyên chạy 24/7, trong khi RTO 30 phút đủ để restore từ snapshot.

#### Các phương án còn lại

- **C sai:** TD: restore 40 TB có thể không kịp 30 phút; automated snapshot theo đề chỉ chạy **một lần/ngày** trong backup window, không đặt được mỗi 5 phút.
- **E sai:** TD: restore RDS từ AWS Backup có thể quá 30 phút RTO; tần suất backup cao nhất là **12 giờ**, nghĩa là RPO tối đa 12 giờ, không đạt 5 phút.

| Tầng | Chọn | Lý do | Cách bị loại |
|---|---|---|---|
| Web/App | **B** snapshot copy | Stateless + rẻ | A: hot-standby tốn tiền |
| Database | **D** cross-Region replica | RPO phút, promote nhanh | C, E: snapshot/backup quá chậm, RPO lỏng |

📝 Ghi chú kỹ thuật: các giới hạn tần suất snapshot/AWS Backup nêu trên là theo giải thích của TD; hãy giữ nguyên chúng cho đề thi.

#### Quy tắc nhớ cho thi

- **Thấy "RPO vài phút" + Aurora + cross-region** → **cross-Region read replica (promote)**.
- **Thấy "stateless tier + RTO 30 phút + cost-effective"** → **snapshot/AMI copy**, không hot-standby.
- **Thấy "restore snapshot DB lớn"** → coi là chậm, khó đạt RTO ngắn.
- Mnemonic: **data thì replica, compute stateless thì snapshot.**

### TD explanation

Amazon EC2 EBS volumes are the primary persistent storage option for Amazon EC2. You can use this block storage for structured data, such as databases, or unstructured data, such as files in a file system on a volume. With Amazon EBS, you can create point-in-time snapshots of volumes, which we store for you in Amazon S3. After you create a snapshot and it has finished copying to Amazon S3, you can copy it from one AWS Region to another, or within the same Region.

Snapshots are useful if you want to back up your data and logs across different geographical locations at regular intervals. In case of disaster, you can restore your applications using point-in-time backups stored in the secondary Region. This minimizes data loss and recovery time.

You can create cross-region read replicas for Amazon Aurora. This allows you to serve read traffic from your users in different geographic regions and increases your application’s responsiveness. This feature also provides you with improved disaster recovery capabilities in case of regional disruptions. You can seamlessly migrate your database from one region to another by creating a cross-region read replica and promoting it to be the new primary database.

You can create an Amazon Aurora MySQL DB cluster as a read replica in a different AWS Region than the source DB cluster. You can promote an Aurora MySQL read replica to a standalone DB cluster. When you promote an Aurora MySQL read replica, its DB instances are rebooted before they become available. Typically, you promote an Aurora MySQL read replica to a standalone DB cluster as a data recovery scheme if the source DB cluster fails.

When restoring Amazon Aurora snapshots, or point-in-time restore, the restoration may take several minutes to hours. Long restore times are caused by long-running transactions in the source database at the time the backup was taken.

The option that says: Schedule a daily snapshot of the Amazon EC2 instances for the web and application tier. Copy the snapshot to the backup region. Restore the backups in case of a disaster in the primary region is correct. The web and application tiers are stateless, meaning they don’t have any important data stored on them. Therefore, copying the daily snapshot of the EC2 instance to the backup region will suffice. The RTO of 30 minutes is ample time to spawn new EC2 instances on the backup region.

The option that says: Set up a cross-Region read replica of the Amazon Aurora database to the backup region. Promote this read-replica as the master database in case of a disaster in the primary region is correct. Given that the RPO for the data tier is 5 minutes, it is better to create a cross-Region read-replica on the backup region. The primary DB instance will asynchronously replicate the data to the Read Replica. So in the event that the primary DB failed, the Read Replica contains the updated data. You can also quickly promote this as the master DB instance in case of a disaster in the primary region. You don’t have to wait for a long database snapshot restore time too, which might exceed the 30-minute RTO requirement.

The option that says: For a quick recovery time, set up a hot-standby of web and application tier on the backup region. Redirect the traffic to the backup region in case of a disaster in the primary region is incorrect. Although this is possible, this is not the most cost-effective solution as it entails a significant number of resources that are continuously running. With an RTO of 30 minutes, you can quickly restore backups of the EC2 snapshots of the web and application tier instead of running a hot-standby environment. Take note that in Disaster Recovery, a “hot-standby” means that the application runs in the DR region. Because it’s always running, you will incur a significant amount of cost.

The option that says: Configure an automated snapshot of the Amazon Aurora database every 5 minutes. Quickly restore the database on the backup region in case of a disaster in the primary region is incorrect. Restoring 40 TB of data may not be possible if you have an RTO requirement of 30 minutes. Depending on how busy the database was during the time the snapshot was taken, the restoration process may take longer than 30 minutes to complete. Moreover, automated backups only occur once every day during the defined backup window. You can’t configure it to run every 5 minutes.

The option that says: Use AWS Backup to create a backup job that will copy the EC2 EBS volumes and RDS data to an Amazon S3 bucket in another region. Restore the backups in case of a disaster in the primary region is incorrect. This may be possible, but the restoration time from the RDS backup may take more time than the required 30 minutes of RTO. The highest backup frequency in AWS Backup is every 12 hours only and not every 5-minutes. Thus, it can only provide a maximum RPO of 12 hours. A better solution is to use a Read Replica with a replication latency of only about a few minutes, providing a higher RPO.

 

References:

https://aws.amazon.com/premiumsupport/knowledge-center/aurora-mysql-slow-snapshot-restore/

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html

https://aws.amazon.com/about-aws/whats-new/2016/06/amazon-aurora-now-supports-cross-region-replication/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html

 

Check out these Amazon EBS and Amazon RDS Cheat Sheets:

https://tutorialsdojo.com/amazon-ebs/

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

![](https://media.tutorialsdojo.com/sap_rds_cross_region_replica.png)

</details>

<a id="q56"></a>

## Q56

A company wants to migrate its on-premises application to the AWS cloud. Due to limited manpower, the company wants to utilize fully managed AWS services as much as possible. This way, there will be less maintenance work after the migration. The application processes large files containing sensitive information so the company has the following requirements:

Data encryption at rest and in transit are both required on all files that will be processed by the application.

The storage solution must be highly durable and available.

The company must be able to use its own encryption key and then periodically rotated for improved security.

Amazon Redshift Spectrum will be used to analyze the migrated data.

Which of the following should the Solutions Architect implement to achieve these requirements?

- **A.** Create an Amazon S3 bucket to store all data. Enable server-side encryption with AWS KMS (SSE-KMS). Apply a bucket policy that enforces HTTPS only connections to the S3 bucket.
- **B.** Provision an AWS Storage Gateway – File Gateway device in the on-premises data center. Enable encryption on the file share with AWS KMS. The data will be transferred securely to an Amazon S3 bucket with SSE-S3 encryption.
- **C.** Store the data files in an Amazon EC2 instance with an encrypted EBS volume. Use AWS KMS to encrypt the EBS volume and enable automatic key rotation.
- **D.** Store the data files on an Amazon DynamoDB table. Leverage on the default SSL connection settings of the DynamoDB table. Use AWS KMS to encrypt the table and enable automatic key rotation.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** fully managed; encryption at rest and in transit; own key rotated; highly durable; Redshift Spectrum

🪤 **Your trap:** 🔁 Picked B: File Gateway adds management overhead, and SSE-S3 keys are AWS-managed not customer-controlled. Direct S3 with SSE-KMS plus HTTPS-only policy fits better.

🧠 **Rule:** Fully managed, customer key, durable: S3 with SSE-KMS and bucket policy denying aws:SecureTransport false.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem app ──► Lưu trữ ? ──► Redshift Spectrum phân tích

Yêu cầu:
  1. Fully managed, ít maintenance
  2. Encrypt at rest + in transit
  3. Durable + available cao
  4. Dùng KEY CỦA MÌNH + rotate định kỳ
  5. Redshift Spectrum đọc được dữ liệu
```

Đáp án đúng: **A (S3 + SSE-KMS + bucket policy chỉ cho HTTPS)**. Anh chọn B (File Gateway + SSE-S3).

⚠️ **Lỗi lặp lại**: câu này anh đã sai cả lần thi 10-05 lẫn lần retake hôm nay. Điểm vấp lặp lại: **SSE-S3 không phải "key của mình"** và **thêm thiết bị on-prem là thêm việc quản lý**.

#### Vì sao A đúng

- **S3**: 11 nines durability, fully managed, và là nguồn dữ liệu mà **Redshift Spectrum** đọc trực tiếp.
- **SSE-KMS**: S3 xin data key từ KMS; anh quản lý **KMS key** (key policy, rotation). Khớp "own encryption key + rotated".
- **At rest** = SSE-KMS; **in transit** = bucket policy `Deny` khi `aws:SecureTransport` là `false` (ép HTTPS).

#### Phương án anh chọn: B sai

B nghe có vẻ "an toàn" vì có chữ KMS, nhưng KMS chỉ mã hóa ở **file share** của gateway. Đến S3 thì object dùng **SSE-S3**: key do **S3 tự quản lý**, anh không kiểm soát và không tự rotate. Vi phạm yêu cầu 4. Thêm nữa, File Gateway là thiết bị anh phải triển khai và vận hành tại on-prem, ngược yêu cầu "ít maintenance". Gửi thẳng vào S3 đã mã hóa thì nhẹ hơn.

#### Các phương án còn lại

- **C. EC2 + EBS mã hóa**: tự quản lý EC2, durability thấp hơn S3 (một instance/volume), và Spectrum không đọc từ EBS.
- **D. DynamoDB**: item tối đa **400 KB**, đề nói file lớn. Spectrum cũng không đọc từ DynamoDB.

| Cơ chế S3 | Ai giữ key | Hợp đề? |
|---|---|---|
| SSE-S3 | S3 quản lý toàn bộ | Không (không phải key của mình) |
| **SSE-KMS** | Anh quản lý KMS key | **Có** |
| SSE-C | Anh tự cung cấp key mỗi request | Không hợp "fully managed" |

#### Lưu ý thực tế

- **Bucket Key** cho SSE-KMS giảm số request tới KMS, giảm chi phí.
- Rotation tự động bật được trên **customer managed key**; key do AWS managed thì AWS tự rotate nhưng anh không điều khiển.

#### Quy tắc nhớ cho thi

- **Thấy "own encryption key + rotate"** → **SSE-KMS** (customer managed key), **không phải SSE-S3**
- **Thấy "encrypt in transit" với S3** → bucket policy `aws:SecureTransport = false` → Deny
- **Thấy "Redshift Spectrum"** → dữ liệu phải ở **S3**
- **Thấy "limited manpower / fully managed"** → loại EC2, loại thiết bị gateway on-prem
- Mẹo: **"S3 trực tiếp > có thêm hộp ở giữa"** khi đề nhấn ít maintenance

### TD explanation

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers scalability, data availability, security, and performance. Amazon S3 is designed for 99.999999999% (11 9’s) of durability, and stores data for millions of applications for companies all around the world.

Amazon S3 default encryption provides a way to set the default encryption behavior for an S3 bucket. You can set default encryption on a bucket so that all new objects are encrypted when they are stored in the bucket. The objects are encrypted using server-side encryption with either Amazon S3-managed keys (SSE-S3) or KMS keys stored in AWS Key Management Service (AWS KMS).

SSE-S3 requires that Amazon S3 manage the data and the encryption keys.

SSE-C requires that you manage the encryption key.

SSE-KMS requires that AWS manage the data key but you manage the KMS key in AWS KMS.

When you configure your bucket to use default encryption with SSE-KMS, you can also enable an S3 Bucket Key to decrease request traffic from Amazon S3 to AWS Key Management Service (AWS KMS) and reduce the cost of encryption. When you configure your bucket to use an S3 Bucket Key for SSE-KMS on new objects, AWS KMS generates a bucket-level key that is used to create a unique data key for objects in the bucket. This bucket key is used for a time-limited period within Amazon S3, reducing the need for Amazon S3 to make requests to AWS KMS to complete encryption operations.

By default, Amazon S3 allows both HTTP and HTTPS requests. To comply with the s3-bucket-ssl-requests-only rule (only accepting HTTPS connections), your bucket policy should explicitly deny access to HTTP requests. To determine HTTP or HTTPS requests in a bucket policy, use a condition that checks for the key "aws:SecureTransport". When this key is set to true, this means that the request is sent through HTTPS. To be sure to comply with the s3-bucket-ssl-requests-only rule, create a bucket policy that explicitly denies access when the request meets the condition "aws:SecureTransport": "false". This policy explicitly denies access to HTTP requests.

Therefore, the correct answer is: Create an Amazon S3 bucket to store all data. Enable server-side encryption with AWS KMS (SSE-KMS). Apply a bucket policy that enforces HTTPS only connections to the S3 bucket.

The option that says: Provision an AWS Storage Gateway – File Gateway device in the on-premises data center. Enable encryption on the file share with AWS KMS. The data will be transferred securely to an Amazon S3 bucket with SSE-S3 encryption is incorrect. Although this is possible, the encryption key on the S3 with SSE-S3 is managed by AWS and not the customer. This also entails more management overhead because you need to manage your file gateway. Less maintenance is needed if data is just sent directly to an encrypted S3 bucket.

The option that says: Store the data files on an Amazon DynamoDB table. Leverage on the default SSL connection settings of the DynamoDB table. Use AWS KMS to encrypt the table and enable automatic key rotation is incorrect. The application processes large documents that may not fit on an Amazon DynamoDB table in which each entry is limited to 400 KB only.

The option that says: Store the data files in an Amazon EC2 instance with an encrypted EBS volume. Use AWS KMS to encrypt the EBS volume and enable automatic key rotation is incorrect as this entails more management overhead as you need to provision your own EC2 instance. Amazon S3 is also more durable compared to a single Amazon EC2 instance with EBS volume.

 

References:

https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html

https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/

 

Check out these Amazon S3 and AWS KMS Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/aws-kms-keys-policy-management-in-aws-kms/

![](https://media.tutorialsdojo.com/sap_redshift_on_premises.PNG)

</details>

<a id="q62"></a>

## Q62

A major telecommunications company is planning to set up a disaster recovery solution for its Amazon Redshift cluster which is being used by its online data analytics application. Database encryption is enabled on their clusters using AWS KMS and it is required that the recovery site should be at least 500 miles from their primary cloud location.

Which of the following is the most suitable solution to meet these requirements and to make its architecture highly available?

- **A.** In your Redshift cluster, enable the cross-region snapshot copy feature to copy snapshots to another region.
- **B.** Create a new AWS CloudFormation stack that will deploy the cluster in another region and will regularly back up the data to an S3 bucket, configured with cross-region replication. In case of an outage in the primary region, just use the snapshot from the S3 bucket and then start the cluster.
- **C.** Set up a snapshot copy grant for a master key in the destination region and enable cross-region snapshots in your Redshift cluster to copy snapshots of the cluster to another region.
- **D.** Develop a scheduled job using AWS Lambda which will regularly take a snapshot of the Redshift cluster and copy it to another region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** Redshift DR; KMS-encrypted cluster; recovery site 500 miles away; cross-region snapshot; snapshot copy grant

🪤 **Your trap:** 🔁 Picked B: custom CloudFormation plus S3 replication is not the Redshift-native way. KMS keys are Region-specific, so encrypted cross-Region copy needs a snapshot copy grant.

🧠 **Rule:** KMS-encrypted Redshift cross-Region snapshot copy: create snapshot copy grant for destination-Region key first.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Primary Region                         DR Region (>= 500 miles)
┌──────────────────────┐   snapshots   ┌──────────────────────┐
│ Redshift (KMS encrypt)│ ───────────► │ Snapshot đã copy     │
│ KMS key (theo Region) │              │ KMS key RIÊNG của    │
└──────────────────────┘              │ Region này           │
                                      └──────────────────────┘
```

Từ khóa: **cluster mã hóa KMS** + **recovery site ở Region khác** + "most suitable". Đáp án đúng: **C (snapshot copy grant + cross-region snapshot copy)**. Anh chọn B.

⚠️ **Lỗi lặp lại**: anh cũng đã sai Redshift cross-Region snapshot copy ở TD4 Q64. Gốc rễ: chưa nhớ rằng **cluster mã hóa thì cross-region copy bắt buộc có snapshot copy grant**.

#### Vì sao C đúng

KMS key là tài nguyên **theo Region**; key ở Region nguồn không dùng được ở Region đích. Với cluster mã hóa, muốn bật cross-region snapshot copy phải:

```
1. Ở Region ĐÍCH: tạo snapshot copy grant cho 1 KMS key của Region đích
   (cho phép Redshift thực hiện encrypt/decrypt tại đó)
2. Ở cluster nguồn: bật cross-region snapshot copy, chỉ định Region đích + grant
```

Sau đó Redshift tự copy snapshot (tự động, theo dõi thay đổi tăng dần) sang Region đích; khi sự cố thì restore ra cluster mới.

#### Phương án anh chọn: B sai

B (CloudFormation + backup dữ liệu vào S3 có CRR + dựng lại cluster) làm được về lý thuyết nhưng quá nhiều bước tự dựng: phải tự xuất dữ liệu ra S3, cấu hình replication, tự lo mã hóa, tự restore. Redshift đã có tính năng native thay thế toàn bộ. Đề hỏi "most suitable" nên chọn tính năng managed.

#### Phương án còn lại

- **A. Bật cross-region copy nhưng không có grant**: hướng đúng nhưng **thiếu bước then chốt**. Cluster mã hóa KMS mà không có snapshot copy grant thì Redshift không có key để mã hóa bản copy ở Region đích. TD loại A vì thiếu grant.
- **D. Lambda scheduled job**: tự chế lại thứ Redshift đã có sẵn, tăng việc vận hành, không khuyến nghị.

| Phương án | Native? | Xử lý KMS Region đích | Kết quả |
|---|---|---|---|
| A | Có | Thiếu grant | Chưa đủ |
| **C** | **Có** | **Có grant** | **Đúng** |
| B | Không (tự dựng) | Tự lo | Quá phức tạp |
| D | Không (Lambda) | Tự lo | Không khuyến nghị |

#### Lưu ý thực tế

- Cluster **không mã hóa** thì bật cross-region copy là đủ, không cần grant. Đề này cố tình có "encryption enabled" để dẫn tới grant.
- Grant tạo ở **Region đích**, trỏ tới KMS key của Region đích.

#### Quy tắc nhớ cho thi

- **Thấy "Redshift + DR + khác Region"** → **cross-region snapshot copy**
- **Thấy "Redshift + KMS encrypted + cross-region"** → thêm **snapshot copy grant** (key ở Region đích)
- **Thấy đáp án chỉ "enable cross-region copy" mà đề có KMS** → bẫy, thiếu grant
- Mnemonic: **"Mã hóa KMS + sang Region khác = cần GRANT"**

### TD explanation

Snapshots are point-in-time backups of a cluster. There are two types of snapshots: automated and manual. Amazon Redshift stores these snapshots internally in Amazon S3 by using an encrypted Secure Sockets Layer (SSL) connection. Amazon Redshift automatically takes incremental snapshots that track changes to the cluster since the previous automated snapshot.

Automated snapshots retain all of the data required to restore a cluster from a snapshot. You can take a manual snapshot any time. When you restore from a snapshot, Amazon Redshift creates a new cluster and makes the new cluster available before all of the data is loaded, so you can begin querying the new cluster immediately. The cluster streams data on demand from the snapshot in response to active queries, then loads the remaining data in the background.

When you launch an Amazon Redshift cluster, you can choose to encrypt it with a master key from the AWS Key Management Service (AWS KMS). AWS KMS keys are specific to a region. If you want to enable cross-region snapshot copy for an AWS KMS-encrypted cluster, you must configure a snapshot copy grant for a master key in the destination region so that Amazon Redshift can perform encryption operations in the destination region.

Therefore, the correct answer is: Set up a snapshot copy grant for a master key in the destination region and enable cross-region snapshots in your Redshift cluster to copy snapshots of the cluster to another region.

The option that says: Create a new AWS CloudFormation stack that will deploy the cluster in another region and will regularly back up the data to an S3 bucket, configured with cross-region replication. In case of an outage in the primary region, just use the snapshot from the S3 bucket and then start the cluster is incorrect. Using a combination of CloudFormation and a separate S3 bucket entails a lot of configuration and set up compared with just enabling cross-region snapshot copy in your Redshift cluster.

The option that says: Develop a scheduled job using AWS Lambda which will regularly take a snapshot of the Redshift cluster and copy it to another region is incorrect. It is not recommended to use AWS Lambda to copy data on your Redshift cluster to another region. You simply have to enable cross-region snapshot copy in your Redshift cluster in order to meet the requirement.

The option that says: In your Redshift cluster, enable the cross-region snapshot copy feature to copy snapshots to another region is incorrect. Although it is right to use the cross-region snapshot copy feature, you still have to configure a snapshot copy grant for a master key in the destination region so that Amazon Redshift can perform encryption operations in the destination region.

 

References:

https://docs.aws.amazon.com/redshift/latest/mgmt/managing-snapshots-console.html#snapshot-crossregioncopy-configure

https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html

 

Check out this Amazon Redshift Cheat Sheet:

https://tutorialsdojo.com/amazon-redshift/

 

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:

https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

![](https://media.tutorialsdojo.com/sap_redshift_cross_region_snapshot.png)

</details>

---

# Group B — Regressions - half-right multi-select (one pick correct, second wrong) (2)

<a id="q34"></a>

## Q34

A leading commercial bank has a hybrid network architecture and is extensively using AWS for its day-to-day operations. The bank uses an Amazon S3 bucket to store sensitive bank records. It has versioning enabled and does not have any encryption. The new solutions architect for the company was asked to implement Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C) for the Amazon S3 bucket to ensure data inside it is secured both at rest and in transit.

Which of the following options should the solutions architect implement to achieve the company requirements? (Select TWO.)

- **A.** For Amazon S3 REST API calls, use the following HTTP Request Headers: x-amz-server-side​-encryption​-customer-algorithm x-amz-server-side​-encryption​-customer-key x-amz-server-side​-encryption​-customer-key-MD5
- **B.** For presigned URLs, specify the algorithm using the x-amz-server-side​-encryption​-customer-algorithm request header
- **C.** Use WSS (WebSocket Secure)
- **D.** Only use the S3 console to upload and update objects with SSE-C encryption.
- **E.** For presigned URLs, specify the algorithm using the x-amz-server-side​-encryption​-customer-key-MD5 request header

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B · **You picked:** A, E

🔑 **Key words:** SSE-C; Select TWO; presigned URLs; REST API headers; data in transit

🪤 **Your trap:** Picked A and E: A right, but for presigned URLs the algorithm header is x-amz-server-side-encryption-customer-algorithm, not the key-MD5 header. B was the correct second pick.

🧠 **Rule:** SSE-C: REST calls need algorithm, key, key-MD5 headers; presigned URLs specify the customer-algorithm header. HTTPS required.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──HTTPS──► S3 bucket (versioning, chưa mã hóa)
        │
        └─ gửi KEY của mình theo từng request  (SSE-C)
           S3 mã hóa AES-256 khi ghi, RỒI BỎ KEY khỏi memory
```

Yêu cầu: **SSE-C** (at rest) và **in transit** an toàn. Chọn 2. Đáp án đúng: **A + B**. Anh chọn A (đúng) + E (sai). Câu này trước đây anh làm đúng, lần này lệch ở cặp B/E, hãy nhớ nó chỉ khác nhau một header.

#### Hai đáp án đúng ghép thành một giải pháp

- **A (REST API headers):** mỗi request SSE-C phải kèm 3 header:
  `x-amz-server-side-encryption-customer-algorithm`, `...-customer-key`, `...-customer-key-MD5`.
- **B (presigned URL):** với presigned URL thì chỉ **khai báo algorithm** bằng header `x-amz-server-side-encryption-customer-algorithm`.
- Ghép lại: REST API gọi trực tiếp thì đủ 3 header; presigned URL thì algorithm đi theo header đúng tên.

#### Vì sao E (pick của anh) sai

E có đúng cấu trúc của B, chỉ **đổi tên header** thành `...-customer-key-MD5`:

| | Header dùng để khai báo algorithm trong presigned URL |
|---|---|
| **B (đúng)** | `x-amz-server-side-encryption-customer-algorithm` |
| E (sai) | `x-amz-server-side-encryption-customer-key-MD5` |

`customer-key-MD5` là checksum để S3 kiểm tra key không bị hỏng khi truyền, **không phải** nơi khai báo algorithm. Anh đã chọn A đúng nên chỉ thiếu B vì bị E "đánh lừa".

#### Các phương án còn lại

- **C sai:** in transit phải dùng **HTTPS**, không phải WSS. TD: S3 **từ chối mọi request SSE-C qua HTTP**; key lỡ gửi qua HTTP coi như bị lộ, phải rotate.
- **D sai:** không giới hạn S3 console; phải dùng **S3 REST API** (hoặc SDK/CLI bọc REST API) để cung cấp key cho SSE-C.

#### Lưu ý thực tế

- SSE-C: AWS **không lưu key**. Mất key = mất object, nên bắt buộc tự quản lý key.
- Mỗi lần GET cũng phải gửi lại đúng key.

#### Quy tắc nhớ cho thi

- **Thấy "SSE-C"** → key đi trong **request header**, qua **HTTPS**.
- **"REST API"** → 3 header: `algorithm`, `key`, `key-MD5`.
- **"Presigned URL"** → khai báo bằng `...-customer-algorithm` (không phải `key-MD5`).
- **"console only" / "WSS"** → loại.

### TD explanation

Server-side encryption is about protecting data at rest. Using server-side encryption with customer-provided encryption keys (SSE-C) allows you to set your own encryption keys. With the encryption key you provide as part of your request, Amazon S3 manages both the encryption as it writes to disks, and decryption when you access your objects. Therefore, you don’t need to maintain any code to perform data encryption and decryption. The only thing you do is manage the encryption keys you provide.

When you upload an object, Amazon S3 uses the encryption key you provide to apply AES-256 encryption to your data and removes the encryption key from memory. Amazon S3 will reject any requests made over HTTP when using SSE-C. For security reasons, it is recommended that you consider any key you send erroneously using HTTP to be compromised. You should discard the key and rotate as appropriate.

At the time of object creation—that is, when you are uploading a new object or making a copy of an existing object—you can specify if you want Amazon S3 to encrypt your data by adding the x-amz-server-side-encryption header to the request. Set the value of the header to the encryption algorithm AES256 that Amazon S3 supports. Amazon S3 confirms that your object is stored using server-side encryption by returning the response header x-amz-server-side-encryption.

Therefore, the following options are correct:

– For Amazon S3 REST API calls, you have to include the following HTTP Request Headers:

x-amz-server-side-encryption-customer-algorithm

x-amz-server-side-encryption-customer-key

x-amz-server-side-encryption-customer-key-MD5 

– For presigned URLs, you should specify the algorithm using the x-amz-server-side-encryption-customer-algorithm request header.

The option that says: Using WSS (WebSocket Secure) is incorrect as you have to use HTTPS and not WSS.

The option that says: Specifying the algorithm using the x-amz-server-side​-encryption​-customer-key-MD5 request header for presigned URLs is incorrect. You should use the x-amz-server-side-encryption-customer-algorithm request header instead.

The option that says: Only use the S3 console to upload and update objects with SSE-C encryption is incorrect because you should use S3 REST APIs instead of the S3 web console.

 

References:

https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html

https://aws.amazon.com/blogs/security/how-to-use-the-rest-api-to-encrypt-s3-objects-by-using-aws-kms/

https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-encryption.html

 

Check out this Amazon S3 Cheat Sheet:

https://tutorialsdojo.com/amazon-s3/

![](https://media.tutorialsdojo.com/sap_s3_sse_encryption.png)

</details>

<a id="q47"></a>

## Q47

A leading financial company owns multiple AWS accounts that are consolidated under one AWS Organization. To ensure that tags are always added when users create any resources across all accounts, the solutions architect should enforce the use of centralized resource provisioning tools and infrastructure-as-code templates that apply tags automatically upon resource creation across all account.

Which of the following options are the recommended actions to achieve the company requirements? (Select TWO.)

- **A.** Set up AWS Service Catalog to tag the provisioned resources with corresponding unique identifiers for portfolio, product, and users.
- **B.** Set up AWS Systems Manager Automation to automatically add tags to your provisioned resources.
- **C.** Set up the CloudFormation Resource Tags property to apply tags to certain resource types upon creation.
- **D.** Set up AWS Config to add the corresponding tags to your resources right from the very moment that they are created.
- **E.** Set up AWS generated tags by activating it in the Billing and Cost Management console of the member account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C · **You picked:** C, E

🔑 **Key words:** tags always added at creation; centralized provisioning tools; infrastructure-as-code templates; AWS Organization; Select TWO

🪤 **Your trap:** Picked C and E: C right, but AWS-generated cost allocation tags in Billing are not proactive tagging at creation. Service Catalog tags provisioned resources automatically, so A was needed.

🧠 **Rule:** Proactive tag-on-create: CloudFormation Resource Tags plus Service Catalog. Config only detects; Billing tags do not enforce.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhiều account trong 1 Organization
        │
        ▼
User tạo resource ──► [Công cụ provisioning tập trung] ──► Resource ĐÃ có tag ngay lúc tạo
                       (Service Catalog / CloudFormation)
```

Từ khóa quyết định: **centralized resource provisioning tools + infrastructure-as-code templates** + tag **tự động ngay khi tạo (proactive)**. Đáp án đúng: **A + C**. Anh chọn C (đúng) và E (sai); thiếu A.

#### Hai đáp án đúng tạo thành MỘT giải pháp

- **C. CloudFormation Resource Tags property**: template khai báo `Tags` cho từng resource, stack tạo resource là tag được gắn luôn. Đây là phần "IaC template".
- **A. Service Catalog**: phần "centralized provisioning tool". User tự phục vụ qua product đã duyệt; Service Catalog **tự gắn tag** (portfolio, product, user) lên resource được provision (tính năng AutoTags). Với phương án A, anh không cần tin user tự nhớ gắn tag.

Cả hai đều chặn từ gốc: resource sinh ra từ công cụ là đã có tag.

#### Phương án anh chọn: E sai

E (AWS generated tags, bật ở Billing and Cost Management) trông liên quan "tag" nhưng chỉ phục vụ **cost allocation**: tag do AWS sinh (vd `aws:createdBy`) để lọc báo cáo chi phí. Nó **không ép** tag nghiệp vụ nào, không thay đổi cách user tạo resource, và bật ở member account thì không giải quyết yêu cầu "mọi resource ở mọi account". Thiếu A nghĩa là chỉ mới có IaC, chưa có công cụ provisioning tập trung cho user tự tạo.

#### Các phương án còn lại

- **B. Systems Manager Automation**: dùng để tự động hóa tác vụ vận hành, gắn tag lên resource **đã tồn tại** (sau khi tạo). Không phải provisioning tool hay IaC.
- **D. AWS Config**: chỉ ghi nhận và đánh giá compliance, phát hiện resource thiếu tag. Muốn sửa phải kèm remediation (Lambda/SSM Automation). Đây là **reactive**, đề cần **proactive**.

| Công cụ | Thời điểm | Vai trò |
|---|---|---|
| **Service Catalog (A)** | Lúc provision | Tự gắn tag cho product |
| **CloudFormation Tags (C)** | Lúc tạo stack | Tag khai báo trong template |
| SSM Automation (B) | Sau khi tạo | Remediation |
| AWS Config (D) | Sau khi tạo | Phát hiện, đánh giá |
| Billing generated tags (E) | Báo cáo chi phí | Không ép tag |

#### Lưu ý thực tế

- Muốn **chặn cứng** tạo resource thiếu tag: IAM/SCP với condition key `aws:RequestTag` và `aws:TagKeys` (TD có nhắc). Tag policy của Organizations chuẩn hóa giá trị tag, không tự gắn tag.

#### Quy tắc nhớ cho thi

- **Thấy "tag ngay lúc tạo / proactive"** → **Service Catalog + CloudFormation Tags** (hoặc IAM `aws:RequestTag` để chặn)
- **Thấy "phát hiện / compliance / remediation"** → **AWS Config** (reactive)
- **Thấy "AWS generated tags / Billing console"** → chỉ **cost allocation**, loại khỏi bài governance
- Multi-select: mỗi đáp án phải khớp một cụm trong đề ("provisioning tool" → A, "IaC template" → C)

### TD explanation

AWS offers a variety of tools to help you implement proactive tag governance practices by ensuring that tags are consistently applied when resources are created.

AWS CloudFormation provides a common language for provisioning all the infrastructure resources in your cloud environment. CloudFormation templates are simple text files that create AWS resources in an automated and secure manner. When you create AWS resources using AWS CloudFormation templates, you can use the CloudFormation Resource Tags property to apply tags to certain resource types upon creation.

AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application environments. AWS Service Catalog enables a self-service capability for users, allowing them to provision the services they need while also helping you to maintain consistent governance – including the application of required tags and tag values.

AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow or deny their access to AWS resources. When you create IAM policies, you can specify resource-level permissions, which include specific permissions for creating and deleting tags. In addition, you can include condition keys, such as aws:RequestTag and aws:TagKeys, which will prevent resources from being created if specific tags or tag values are not present.

With AWS Service Catalog, you can create products that represent the resources you want to provision, and you can define tagging policies for those products. When users provision resources through Service Catalog, the resources will be automatically tagged according to the defined tagging policies. This ensures that resources are consistently tagged with the required identifiers for portfolio, product, and users across all accounts.

AWS CloudFormation allows you to provision and manage AWS resources using infrastructure-as-code templates. The Resource Tags property in CloudFormation templates enables you to specify tags that should be applied to resources upon creation. This option aligns with the company’s requirements for centralized resource provisioning and automatic tagging using infrastructure-as-code templates.

Therefore, the correct answers are:

– Set up AWS Service Catalog to tag the provisioned resources with corresponding unique identifiers for portfolio, product, and users.

– Set up the CloudFormation Resource Tags property to apply tags to certain resource types upon creation.

The option that says: Set up AWS config to add the corresponding tags to your resources right from the very moment that they are created is incorrect. AWS Config is a service that continuously monitors and records your AWS resource configurations, including resource metadata like tags. While AWS Config can help you identify resources that are not compliant with your tagging policies, it does not directly add tags to resources upon creation. Instead, AWS Config is typically used in combination with other services like AWS Lambda or AWS Systems Manager Automation to remediate non-compliant resources by adding missing tags. However, this approach is reactive, as it relies on first detecting resources without the required tags and then triggering a remediation action. Additionally, the requirement in this scenario is to proactively enforce tagging upon resource creation, which is why AWS Config alone is not the recommended solution.

The option that says: Set up AWS generated tags by activating it in the Billing and Cost Management console of the member account is incorrect. While enabling AWS generated tags can be beneficial for cost allocation and management purposes, it does not directly address the requirement of automatically adding tags upon resource creation across all accounts.

The option that says: Set up AWS Systems Manager Automation to automatically add tags to your provisioned resources is incorrect because AWS Systems Manager Automation is a service that allows you to automate common maintenance and deployment tasks across AWS resources. While Automation can be used to add tags to existing resources, it is not designed for automatically tagging resources upon creation. Automation is more suitable for managing and maintaining resources after they have been provisioned, not for the initial resource creation and tagging process. Additionally, it is not designed as a centralized resource provisioning tool or infrastructure-as-code solution, which are the recommended approaches for enforcing tagging upon resource creation in this scenario.

 

References:

https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html

https://aws.amazon.com/about-aws/whats-new/2018/03/aws-service-catalog-announces-autotags-for-automatic-tagging-of-provisioned-resources/

 

Check out this AWS Service Catalog Cheat Sheet:

https://tutorialsdojo.com/aws-service-catalog/

![](https://media.tutorialsdojo.com/sap_ec2_tags.png)

</details>

---

# Group C — Regressions - one detail decides (storage class, update mechanism) (2)

<a id="q38"></a>

## Q38

A company is running a financial modeling application on the AWS cloud. The application tier runs on an Auto Scaling group of Amazon EC2 instances. A separate EC2 cluster with a fixed number of instances is hosting the 200 TB of financial data in a shared file system. The application reads and processes the data on the shared filesystem to generate an overall financial report, which takes about 72 hours to complete. This whole process only needs to run at the end of each month, but the storage tier instances are running continuously to retain all the data in the shared file system.

As the storage tier takes up a large percentage of operational costs, the management wants to reduce the cost of the storage tier while maintaining the high-performance access needed by the application during its 72-hour run.

Which of the following options should the solutions architect implement that will have the largest overall cost reduction?

- **A.** For the data tier, use Mountpoint for Amazon S3 to access the financial data directly from an S3 bucket. This will eliminate the need for a shared file system and reduce costs. Mount the S3 bucket on the application tier EC2 instances and run the job directly from it.
- **B.** For the data tier, create an Amazon EFS filesystem and move the objects of the existing shared file system to it. Since the data will only be used once a month, use EFS Standard–Infrequent Access (IA) class to save costs. Mount this filesystem as shared storage for the application tier EC2 instance for the duration of the job.
- **C.** For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Glacier Instant Retrieval Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed.
- **D.** For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Intelligent-Tiering Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** 200 TB shared file system; monthly 72-hour job; reduce storage cost; S3 plus FSx for Lustre lazy-loading

🪤 **Your trap:** Picked C: S3 Glacier Instant Retrieval suits archive data accessed about once a quarter, not monthly processing. S3 Intelligent-Tiering plus temporary FSx for Lustre was right.

🧠 **Rule:** Monthly batch on huge data: S3 Intelligent-Tiering for storage, temporary FSx for Lustre linked to S3, delete after the job.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:  App tier (ASG) ──► Storage cluster EC2 (200 TB, chạy 24/7)  ◄── tốn tiền
Job chỉ chạy 72 giờ / tháng nhưng storage bật liên tục

Đích:      S3 (lưu dài hạn, rẻ)  ──lazy-load──►  FSx for Lustre (tạm, chỉ 72h)
```

Yêu cầu: **giảm chi phí lớn nhất** + vẫn **high-performance** trong 72 giờ chạy. Đáp án đúng: **D**. Anh chọn C. Câu này lần trước anh đúng, lần này nhầm chi tiết storage class.

#### Vì sao D đúng

- **Tách lưu trữ và hiệu năng:** dữ liệu nằm lâu dài trên **S3** (rẻ hơn EFS/EC2 cluster), còn **FSx for Lustre** chỉ dựng khi chạy job.
- **FSx for Lustre link với S3**: S3 object hiện thành file POSIX; **lazy-loading** nạp dữ liệu từ S3 khi cần. Song song, phân tán, hợp HPC/financial modeling.
- Xong job → **xóa file system**, không trả tiền cho phần hiệu năng khi nhàn rỗi.
- **S3 Intelligent-Tiering** hợp với dữ liệu truy cập không đoán trước: tự chuyển tầng, **không phí retrieval** kiểu archive.

#### Vì sao C (pick của anh) sai

C giống D gần hết, chỉ khác storage class: **S3 Glacier Instant Retrieval**. Theo TD:

- Glacier dành cho dữ liệu lưu lâu, truy cập khoảng **một lần mỗi quý**; ở đây là mỗi tháng.
- Có **phí retrieval** mỗi lần lấy dữ liệu, mà mỗi kỳ job đọc cả 200 TB, nên có thể ăn mất phần tiết kiệm.

#### Các phương án còn lại

- **B (EFS Standard-IA):** TD: EFS đắt hơn nhiều so với S3 Standard; dù có IA vẫn không rẻ bằng S3 + FSx tạm.
- **A (Mountpoint for S3):** tối ưu cho đọc tuần tự, **không đủ throughput/latency** cho xử lý nặng, **không đầy đủ POSIX semantics**, kém khi truy cập song song so với Lustre.

| Phương án | Lưu dài hạn | Hiệu năng 72h | Điểm trừ |
|---|---|---|---|
| **D. S3 Int-Tiering + FSx Lustre** | Rẻ, không phí retrieval | Cao | Không |
| C. S3 Glacier IR + FSx Lustre | Rẻ nhưng... | Cao | Phí retrieval, sai tần suất (tháng vs quý) |
| B. EFS Standard-IA | Đắt hơn S3 | Khá | Chi phí |
| A. Mountpoint S3 | Rẻ | Thấp | Thiếu POSIX/perf |

#### Quy tắc nhớ cho thi

- **Thấy "HPC / shared file system hiệu năng cao, chạy theo đợt"** → **S3 + FSx for Lustre (lazy-load), xóa sau job**.
- **Thấy "truy cập mỗi tháng, không đoán trước"** → **Intelligent-Tiering**; Glacier là cho "mỗi quý trở lên".
- **Thấy "Mountpoint for S3"** + workload nặng/POSIX → loại.

### TD explanation

Amazon FSx for Lustre is a large-scale, distributed parallel file system powering the workloads of most of the largest supercomputers. It is popular among AWS customers for high-performance computing workloads, such as meteorology, life science, and engineering simulations. It is also used in media and entertainment, as well as the financial services industry. If your workloads require fast, POSIX-compliant file system access to your S3 buckets, then you can use FSx for Lustre to link your S3 buckets to a file system and keep data synchronized between the file system and S3 in both directions.

Amazon FSx for Lustre offers a choice of solid-state drive (SSD) and hard disk drive (HDD) storage types that are optimized for different data processing requirements.

FSx for Lustre integrates with Amazon S3, making it easier for you to process cloud datasets using the Lustre high-performance file system. When linked to an Amazon S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files. Amazon FSx imports listings of all existing files in your S3 bucket at file system creation. Amazon FSx can also import listings of files added to the data repository after the file system is created. You can set the import preferences to match your workflow needs. The file system also makes it possible for you to write file system data back to S3. Data repository tasks simplify the transfer of data and metadata between your FSx for Lustre file system and its durable data repository on Amazon S3.

Therefore, the correct answer is: For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Intelligent-Tiering Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed. The FSx for Lustre filesystem can temporarily load the data from S3 and share it among the application tier instances. This is cheaper as we can use S3 for long-term storage and FSx for Lustre for the temporary shared file system.

The option that says: For the data tier, create an Amazon EFS filesystem and move the objects of the existing shared file system to it. Since the data will only be used once a month, use EFS Standard–Infrequent Access (IA) class to save costs. Mount this filesystem as shared storage for the application tier EC2 instance for the duration of the job is incorrect. Amazon EFS Filesystem costs significantly more than standard Amazon S3 storage costs.

The option that says: For the data tier, create an Amazon S3 bucket and move the objects of the existing shared file system to it. Use S3 Glacier Instant Retrieval Storage class to save costs. Use lazy-loading on an Amazon FSx for Lustre filesystem to import the contents of the S3 bucket. Use this filesystem as shared storage for the application tier EC2 instances for the duration of the job and delete it once the job is completed is incorrect. S3 Glacier is typically recommended for long-lived archive data accessed once a quarter. Also, S3 Glacier has additional charges for retrieving data from cold storage.

The option that says: For the data tier, use Mountpoint for Amazon S3 to access the financial data directly from an S3 bucket. This will eliminate the need for a shared file system and reduce costs. Mount the S3 bucket on the application tier EC2 instances and run the job directly from it is incorrect because Mountpoint for Amazon S3 is optimized for read-heavy workloads with sequential access patterns, but it does not offer the high-throughput, low-latency performance required for intensive data processing like financial modeling. It lacks POSIX compliance and does not support full file system semantics, which may cause compatibility issues with applications expecting traditional shared file systems. Additionally, it doesn’t primarily support parallel access with the same efficiency as FSx for Lustre.

 

References:

https://aws.amazon.com/blogs/storage/persistent-storage-for-high-performance-workloads-using-amazon-fsx-for-lustre/

https://aws.amazon.com/blogs/aws/enhanced-amazon-s3-integration-for-amazon-fsx-for-lustre/

https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html

 

Check out these Amazon S3 and Amazon FSx for Lustre Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-efs-vs-amazon-fsx-for-windows-vs-amazon-fsx-for-lustre/

![](https://media.tutorialsdojo.com/sap_fsx_s3_source.png)

</details>

<a id="q68"></a>

## Q68

A company uses an AWS CloudFormation template to deploy its three-tier web application on the AWS Cloud. The CloudFormation template contains a custom AMI value used by the Auto Scaling group of Amazon EC2 instances. Every new version of the application corresponds to a new AMI that needs to be deployed. The company doesn’t want any downtime during the deployment process. The Solutions Architect has been tasked to implement a solution that will streamline its AMI deployment process by performing the following steps:

Update the CloudFormation template to refer to the new AMI.

Launch new EC2 instances from the new AMI by calling the UpdateStack API to replace the old EC2 instances.

Which of the following actions should the Solutions Architect take to achieve the above requirements?

- **A.** Update the CloudFormation template AWS::AutoScaling::LaunchConfiguration resource section and specify a DeletionPolicy attribute with MinSuccessfulInstancesPercent of 50.
- **B.** Create a new CloudFormation change set to view the changes in the new version of the template. Verify that the correct AMI is listed on the change before executing the change set.
- **C.** Update the CloudFormation template AWS::AutoScaling::AutoScalingGroup resource section and specify an UpdatePolicy attribute with an AutoScalingRollingUpdate policy.
- **D.** Copy the updated template and deploy it to a new CloudFormation stack. After its successful deployment, update the Amazon Route 53 records to point to the new stack and delete the old stack.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** CloudFormation AMI update; no downtime; UpdateStack replaces instances; AutoScalingGroup UpdatePolicy

🪤 **Your trap:** Picked B: change set only previews changes and does not deploy instances. Zero-downtime AMI rollout needs an UpdatePolicy with AutoScalingRollingUpdate on the AutoScalingGroup.

🧠 **Rule:** Replace ASG instances with new AMI without downtime: UpdatePolicy AutoScalingRollingUpdate on AutoScalingGroup, not change set or new stack.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Template CloudFormation ──UpdateStack──► Auto Scaling group (AMI mới)
                                          │
              Instance cũ vẫn chạy AMI cũ ┘  (chỉ instance MỚI dùng AMI mới)

Yêu cầu: thay instance cũ bằng AMI mới, KHÔNG downtime,
         và đúng quy trình "sửa template + gọi UpdateStack"
```

Đáp án đúng: **C (UpdatePolicy với AutoScalingRollingUpdate trên AutoScalingGroup)**. Anh chọn B.

#### Vì sao C đúng

Đổi AMI trong launch template/configuration **không** tự thay các instance đang chạy; instance cũ giữ cấu hình cũ. Gắn **UpdatePolicy** vào resource `AWS::AutoScaling::AutoScalingGroup` thì khi `UpdateStack` thay đổi, CloudFormation tự **rolling update** theo batch (vd `MaxBatchSize`, `MinInstancesInService`), thay dần instance cũ, nên vẫn còn instance phục vụ, không downtime.

#### Phương án anh chọn: B sai

Change set chỉ để **xem trước** thay đổi và xác nhận AMI đúng. Đó là bước kiểm soát, không phải cơ chế triển khai. Execute change set xong, launch template có AMI mới nhưng **instance hiện tại không bị thay**, chỉ instance sinh mới mới dùng AMI mới. Thiếu UpdatePolicy thì không có rolling replacement.

#### Các phương án còn lại

- **A. DeletionPolicy với MinSuccessfulInstancesPercent**: sai thuộc tính. `MinSuccessfulInstancesPercent` thuộc **CreationPolicy** (ResourceSignal), không có trong DeletionPolicy. DeletionPolicy chỉ quyết định giữ/xóa resource khi xóa stack.
- **D. Stack mới + đổi Route 53 + xóa stack cũ**: blue/green làm được, nhưng mỗi lần deploy phải sửa Route 53 và không đúng yêu cầu thay instance bằng **UpdateStack** trên stack hiện có.

| Cơ chế | Thay instance cũ? | Downtime? | Đúng quy trình UpdateStack? |
|---|---|---|---|
| **C. UpdatePolicy rolling** | Có | Không | Có |
| B. Change set | Không | Không đổi gì | Chỉ preview |
| A. DeletionPolicy | Không liên quan | Không liên quan | Sai thuộc tính |
| D. Stack mới + Route 53 | Có (stack khác) | Không | Không |

#### Lưu ý thực tế

- Có thể ép rolling update bất cứ lúc nào bằng **instance refresh** của Auto Scaling.

📝 **Ghi chú kỹ thuật**: đề nhắc `AWS::AutoScaling::LaunchConfiguration` ở phương án A. Launch configuration là cơ chế cũ; hiện nay AWS khuyến nghị **launch template**. Đáp án C vẫn đúng với cả hai vì UpdatePolicy gắn ở AutoScalingGroup.

#### Quy tắc nhớ cho thi

- **Thấy "CloudFormation + ASG + đổi AMI + không downtime"** → **UpdatePolicy: AutoScalingRollingUpdate** trên ASG
- **Thấy "change set"** → chỉ **preview**, không triển khai
- **Thấy "MinSuccessfulInstancesPercent"** → thuộc **CreationPolicy**, không phải DeletionPolicy
- **Thấy "UpdateStack API" được yêu cầu giữ nguyên** → loại phương án tạo stack mới

### TD explanation

AWS CloudFormation gives you an easy way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles, by treating infrastructure as code. You can use a template to create, update, and delete an entire stack as a single unit, as often as you need to, instead of managing resources individually.

The AWS::AutoScaling::AutoScalingGroup resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

When you update the launch template for an Auto Scaling group, this update action does not deploy any change across the running Amazon EC2 instances in the Auto Scaling group. All new instances will get the updated configuration, but existing instances continue to run with the configuration that they were originally launched with. This works the same way as any other Auto Scaling group.

You can add an UpdatePolicy attribute to your stack to perform rolling updates (or replace the group) when a change has been made to the group. Alternatively, you can force a rolling update on your instances at any time after updating the stack by starting an instance refresh.

The UpdatePolicy on the AutoScalingGroup will automatically execute the rolling deployment of the new AMI instances when the Cloudformation template is updated.

To specify how AWS CloudFormation handles rolling updates for an Auto Scaling group, use the AutoScalingRollingUpdate policy. Rolling updates enable you to specify whether AWS CloudFormation updates instances that are in an Auto Scaling group in batches or all at once. For example, suppose you have updated the MaxBatchSize in your stack template’s UpdatePolicy from 1 to 10. This allows you to perform updates without causing downtime to your currently running application.

Therefore, the correct answer is: Update the CloudFormation template AWS::AutoScaling::AutoScalingGroup resource section and specify an UpdatePolicy attribute with an AutoScalingRollingUpdate policy.

The option that says: Create a new CloudFormation change set to view the changes in the new version of the template. Verify that the correct AMI is listed on the change before executing the change set is incorrect. Although this is possible, the existing EC2 instances won’t be replaced this way immediately. The change set will only update the Launch Template with the new AMI and will only be applied to the newly spawned instances, excluding the existing ones.

The option that says: Update the CloudFormation template AWS::AutoScaling::LaunchConfiguration resource section and specify a DeletionPolicy attribute with MinSuccessfulInstancesPercentof 50 is incorrect. This option should have used a CreationPolicy attribute instead of a DeletionPolicy attribute because there is no MinSuccessfulInstancesPercentof element in the DeletionPolicy attribute.

The option that says: Copy the updated template and deploy it to a new CloudFormation stack. After its successful deployment, update the Amazon Route 53 records to point to the new stack and delete the old stack is incorrect. Although this is possible, it typically involves an extra step that requires updating the Route 53 entry for every deployment. This does not satisfy the deployment requirement of calling the UpdateStack API to replace the instances.

 

References:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStack.html

 

Check out the Amazon CloudFront Cheat Sheet:

https://tutorialsdojo.com/amazon-cloudfront/

![](https://media.tutorialsdojo.com/sap_cloudformation_overview.png)

</details>
