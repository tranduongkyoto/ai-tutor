# Neal Exam B — 75 questions (2026-10-26) — Wrong Answer Review (20 questions)

Source: `sap-neal-exam-b-2026-10-260916-results.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `neal_b_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q10](#q10) | ❌ 10-27 | ☐ | ☐ |
| A | [Q61](#q61) | ✅ 10-27 | ☐ | ☐ |
| A | [Q63](#q63) | ✅ 10-27 | ☐ | ☐ |
| A | [Q71](#q71) | ✅ 10-27 | ☐ | ☐ |
| B | [Q14](#q14) | ✅ 10-27 | ☐ | ☐ |
| B | [Q23](#q23) | ✅ 10-27 | ☐ | ☐ |
| B | [Q28](#q28) | ✅ 10-27 | ☐ | ☐ |
| B | [Q51](#q51) | ✅ 10-27 | ☐ | ☐ |
| B | [Q56](#q56) | ✅ 10-27 | ☐ | ☐ |
| B | [Q59](#q59) | ✅ 10-27 | ☐ | ☐ |
| C | [Q17](#q17) | ✅ 10-27 | ☐ | ☐ |
| C | [Q22](#q22) | ✅ 10-27 | ☐ | ☐ |
| C | [Q34](#q34) | ✅ 10-27 | ☐ | ☐ |
| C | [Q35](#q35) | ✅ 10-27 | ☐ | ☐ |
| C | [Q37](#q37) | ✅ 10-27 | ☐ | ☐ |
| C | [Q45](#q45) | ✅ 10-27 | ☐ | ☐ |
| D | [Q41](#q41) | ✅ 10-27 | ☐ | ☐ |
| D | [Q68](#q68) | ✅ 10-27 | ☐ | ☐ |
| D | [Q70](#q70) | ✅ 10-27 | ☐ | ☐ |
| D | [Q74](#q74) | ✅ 10-27 | ☐ | ☐ |

---

# Group A — Over-built or DIY pick where a simpler managed fit existed (4)

<a id="q10"></a>

## Q10

<!-- source: T6Q19 · domain: MIG -->



A company needs to close a data center and must migrate data to AWS urgently. The data center has a 1 Gbps internet connection and a 500 Mbps AWS Direct Connect link. The company must transfer 25 TB of data from the data center to an Amazon S3 bucket.
What is the FASTEST method of transferring the data?

- **A.** Use the AWS Direct Connect link to upload the data to S3.
- **B.** Upload the data to the S3 bucket using S3 Transfer Acceleration.
- **C.** Use AWS DataSync to migrate the data to S3.
- **D.** Copy the data to an 80 TB AWS Snowball device.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** 25 TB, 1 Gbps internet, 500 Mbps Direct Connect, fastest, Snowball vs Transfer Acceleration

🪤 **Your trap:** 🔁 Chose Snowball; 25 TB at 1 Gbps takes ~2-3 days, shipping both ways is slower. Transfer Acceleration uses the faster internet link; Direct Connect is slower.

🧠 **Rule:** Do the transfer math first: 1 Gbps is about 10 TB/day; Snowball only pays off past ~1 week. Fastest link wins.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Data center ──1 Gbps internet──────────► S3
     │
     └──500 Mbps Direct Connect────────► S3
Dữ liệu: 25 TB     Yêu cầu: NHANH NHẤT, đóng DC gấp
```

Đáp án đúng: **B (S3 Transfer Acceleration)**. Anh chọn D (Snowball 80 TB).

#### Vì sao B đúng

Hai đường truyền: internet 1 Gbps và Direct Connect 500 Mbps. Muốn nhanh nhất thì dùng đường **băng thông lớn hơn** (internet 1 Gbps) và tối ưu đường đi bằng **Transfer Acceleration**: dữ liệu vào **CloudFront edge location** gần nhất rồi đi qua mạng nội bộ AWS tới S3.

Ước lượng thô: 25 TB = 200.000 Gb; ở 1 Gbps lý thuyết khoảng 200.000 giây, tức khoảng 2,3 ngày. Ở 500 Mbps thì gấp đôi, khoảng 4,6 ngày.

#### Vì sao D (Snowball) sai

Anh nghĩ "25 TB nhiều thì dùng Snowball". Nhưng Snowball có chu kỳ: đặt thiết bị, chờ giao, copy, **gửi trả**, rồi AWS import vào S3. Giải thích của đề: với internet 1 Gbps, 25 TB đẩy lên được nhanh, còn vận chuyển hai chiều "likely take longer".

#### Các phương án còn lại

- **A. Direct Connect 500 Mbps:** chậm hơn internet 1 Gbps, bằng một nửa băng thông.
- **C. DataSync:** là công cụ tự động hóa, có thể dùng cả đường mạng sẵn có, nhưng đề nói nó không cải thiện tốc độ so với Transfer Acceleration trong trường hợp này.

| Cách | Băng thông / đường đi | Nhận xét |
|---|---|---|
| **B. Transfer Acceleration** | Internet 1 Gbps + edge location | Nhanh nhất |
| A. Direct Connect | 500 Mbps | Hẹp hơn một nửa |
| C. DataSync | Dùng đường mạng sẵn | Không tăng tốc thêm |
| D. Snowball | Vận chuyển vật lý 2 chiều | Chậm vì shipping |

📝 **Ghi chú kỹ thuật:** Transfer Acceleration không làm đường truyền rộng hơn 1 Gbps; nó giúp khi khoảng cách tới Region xa hoặc đường internet không ổn định. Đề dùng nó làm đáp án vì là lựa chọn duy nhất tận dụng được đường 1 Gbps. Giữ nguyên đáp án B theo đề.

#### Lưu ý thực tế

- Quy tắc kinh nghiệm: tính **thời gian truyền = dung lượng / băng thông**. Nếu vài ngày thì mạng đủ, Snowball thường chỉ hợp khi mất hàng tuần hoặc băng thông rất thấp.
- Transfer Acceleration phải được bật trên bucket và dùng endpoint riêng của accelerate.

#### Quy tắc nhớ cho thi

- **Thấy "FASTEST" + có đường internet băng thông lớn hơn Direct Connect** → **S3 Transfer Acceleration**
- **Thấy dữ liệu lớn, nhưng mạng đủ nhanh để xong trong vài ngày** → đừng vội chọn **Snowball**
- **Luôn so sánh băng thông các link** trong đề trước khi chọn
- **Snowball** → mạng chậm / không ổn định / mất hàng tuần

### TD explanation

The fastest way to upload the data would be to use the higher speed internet connection and use Amazon S3 Transfer Acceleration.
Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.
CORRECT:
"Upload the data to the S3 bucket using S3 Transfer Acceleration" is the correct answer.
INCORRECT:
"Use the AWS Direct Connect link to upload the data to S3" is incorrect. The Direct Connect link is slower than the internet link, with transfer acceleration latency can be reduced as the data is sent to the nearest edge location and then routed over the AWS global network.
INCORRECT:
"Use AWS DataSync to migrate the data to S3" is incorrect. AWS DataSync will not improve the speed in this case whereas transfer acceleration will.
INCORRECT:
"Copy the data to an 80 TB AWS Snowball device" is incorrect. With the internet link running at 1 Gbps and 25TB of data, the data can be moved quickly to AWS. Shipping snowball devices both ways will likely take longer.
References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

</details>

<a id="q61"></a>

## Q61

<!-- source: T4Q26 · domain: MIG -->



A company runs a web application in an on-premises data center in Paris. The application includes stateless web servers behind a load balancer, shared files in a NAS device, and a MySQL database server. The company plans to migrate the solution to AWS and has the following requirements:
· Provide optimum performance for customers.
· Implement elastic scalability for the web tier.
· Optimize the database server performance for read-heavy workloads.
· Reduce latency for users across Europe and the US.
· Design the new architecture with a 99.9% availability SLA.
Which solution should a Solutions Architect propose to meet these requirements while optimizing operational efficiency?

- **A.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon ElastiCache cluster in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe.
- **B.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and two Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe. Configure EFS cross-Region replication.
- **C.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon DocumentDB table in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes all global locations.
- **D.** Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and three Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon FSx with cross-Region synchronization. Configure Amazon CloudFront with the ALB as the origin and a price class that includes the US and Europe.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** Paris data center migration, 99.9% SLA, Europe and US users, ElastiCache, Aurora, EFS, CloudFront price class

🪤 **Your trap:** 🔁 Chose two Regions with global Aurora and FSx. A single Region over three AZs already meets 99.9%; CloudFront covers US/Europe latency, so multi-Region is overbuilt.

🧠 **Rule:** Match design to stated SLA: 99.9% needs Multi-AZ in one Region. CloudFront handles global latency; skip multi-Region.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem Paris:  web (stateless) + LB  |  NAS  |  MySQL
                         │
                 migrate lên AWS
                         ▼
Yêu cầu: elastic web tier, read-heavy DB, giảm latency EU + US,
         SLA 99.9%, vận hành ĐƠN GIẢN
```

Đáp án đúng: **A** (một Region, 3 AZ). Anh chọn D (hai Region).

#### Vì sao A đúng, từng yêu cầu một

| Yêu cầu | Thành phần trong A |
|---|---|
| Elastic web tier | ALB + Auto Scaling group, 3 AZ |
| Read-heavy DB | **ElastiCache** trước **Aurora MySQL Multi-AZ** |
| Shared files (NAS) | **Amazon EFS** (NFS, nhiều AZ) |
| Latency EU + US | **CloudFront**, ALB làm origin, price class gồm US + Europe |
| 99.9% | Multi-AZ trong **một Region** là đủ |
| Tiết kiệm | Price class giới hạn US/Europe → rẻ hơn "all locations" |

#### Anh chọn D - vì sao trượt

D thêm **hai Region + Aurora Global + FSx cross-Region**: quá mức cần thiết.

- 99.9% đạt được bằng multi-AZ một Region; thêm Region chỉ tăng độ phức tạp và chi phí, trái "optimizing operational efficiency."
- **Không có cơ chế điều hướng traffic giữa hai Region** (không thấy Route 53/Global Accelerator). Đề không nói cách user vào Region nào.
- Aurora Global Database: Region phụ chỉ **đọc**, ghi phải qua primary hoặc write forwarding - lại thêm phức tạp.

📝 **Ghi chú kỹ thuật:** Neal nói FSx "không có cross-Region synchronization". Thực tế **FSx hỗ trợ sao chép cross-Region** (backup copy; một số loại như FSx for NetApp ONTAP còn có replication). Vì vậy **đừng** loại D vì lý do này; D sai vì thừa kiến trúc multi-Region và thiếu routing.

#### Các phương án còn lại

- **B**: Hai Region, 2 AZ mỗi Region, EFS cross-Region replication. Cũng thừa multi-Region, và vẫn không có cơ chế định tuyến.
- **C**: **Amazon DocumentDB "table"** làm cache cho Aurora - DocumentDB là database tương thích MongoDB, **không phải cache**. Và price class "all global locations" đắt hơn cần thiết.

#### Lưu ý thực tế

- Latency user toàn cầu thường giải bằng **CloudFront (cache edge)**, không nhất thiết đưa compute sang nhiều Region.
- Price class: bớt edge location để giảm chi phí; user ngoài vùng vẫn truy cập được nhưng có thể chậm hơn.
- Multi-Region đáng cân nhắc khi đề nói **DR / RTO-RPO thấp / chủ quyền dữ liệu / ghi ở nhiều Region**.

#### Quy tắc nhớ cho thi

- **Thấy "99.9% SLA"** → multi-AZ một Region là đủ
- **Thấy "giảm latency user nhiều châu lục" + web** → **CloudFront**, không tự động là multi-Region
- **Thấy "read-heavy DB"** → read replica hoặc **ElastiCache**
- **ElastiCache = cache; DocumentDB = DB**, đừng lẫn
- **Thấy "shared files NAS Linux"** → **EFS**
- **Multi-Region mà không có Route 53/Global Accelerator** → nghi ngờ

### TD explanation

> ⚠️ FSx supports cross-Region backup copies/replication, contrary to the explanation.

To meet the 99.9% availability SLA a solution in a single Region with Auto Scaling and Load Balancing across multiple AZs is sufficient. To optimize the DB for read-heavy workloads, Amazon ElastiCache can be placed in front of an Aurora MySQL DB. The shared files can be easily moved to an Amazon EFS file system. CloudFront can be used to reduce latency for users in different geographies. In this case US and Europe price classes can be selected in CloudFront and this will cache the content in those locations only which reduces cost.
CORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon ElastiCache cluster in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe" is the correct answer.
INCORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and two Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes the US and Europe. Configure EFS cross-Region replication" is incorrect.
There’s no need to have a cross-Region solution to meet a 99.9% availability SLA and there’s no mechanism mentioned for directing traffic between Regions.
INCORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in one AWS Region and three Availability Zones. Configure an Amazon DocumentDB table in front of a Multi-AZ Amazon Aurora MySQL DB cluster. Move the shared files to Amazon EFS. Configure Amazon CloudFront with the ALB as the origin and select a price class that includes all global locations" is incorrect.
DocumentDB is not a caching engine and cannot be used in front of an Aurora DB. CloudFront should not use a price class the includes all global locations as this will be more costly and is not required in the solution.
INCORRECT:
"Use an Application Load Balancer (ALB) in front of an Auto Scaling group of Amazon EC2 instances in two AWS Regions and three Availability Zones in each Region. Configure an Amazon ElastiCache cluster in front of a global Amazon Aurora MySQL database. Move the shared files to Amazon FSx with cross-Region synchronization. Configure Amazon CloudFront with the ALB as the origin and a price class that includes the US and Europe" is incorrect.
Amazon FSx also does not have a feature for cross-Region synchronization. There’s also no need to have a cross-Region solution to meet a 99.9% availability SLA and there’s no mechanism mentioned for directing traffic between Regions.
References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q63"></a>

## Q63

<!-- source: T4Q15 · domain: MIG -->



A company is running a two-tier web-based application in an on-premises data center. The application layer consists of a single server running a stateless application. The application connects to a PostgreSQL database running on a separate server. A Solutions Architect is planning a migration to AWS. The company requires that the application and database layer must be highly available across three availability zones.
Which solution will meet the company’s requirements?

- **A.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ and add Aurora Replicas in two more AZs.
- **B.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind a Network Load Balancer. Create an Amazon RDS Multi-AZ PostgreSQL database across two AZs and add a Read Replica in a third AZ.
- **C.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora Global database.
- **D.** Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind a Network Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ with storage auto scaling enabled.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** two-tier app, PostgreSQL, highly available across three AZs, Aurora replicas, Aurora Global

🪤 **Your trap:** 🔁 Aurora Global database spans Regions, overbuilt for three-AZ availability. Aurora writer plus replicas in two other AZs gives automatic failover; Multi-AZ is not DR across Regions.

🧠 **Rule:** Three AZs in one Region: Aurora cluster with replicas in different AZs. Global database is for cross-Region DR and RPO.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users ─► LB ─► ASG (3 AZ)  ── stateless app
                  │
                  ▼
             PostgreSQL  ── phải HA qua 3 AZ
```

Từ khóa quyết định: **database layer highly available across THREE AZs**. Đáp án đúng: **A**. Anh chọn C.

#### Vì sao A đúng

```
AZ-a: Aurora writer
AZ-b: Aurora Replica  ─┐ tự động promote khi writer lỗi
AZ-c: Aurora Replica  ─┘
        └── chung một cluster volume (6 bản copy / 3 AZ)
```

- Aurora: 1 writer + tới 15 **Aurora Replica**; replica là read-only nhưng **tự được promote** làm writer khi failover.
- Đặt writer + 2 replica ở 3 AZ khác nhau → **compute** cũng HA qua 3 AZ, không chỉ storage.
- Lớp web: ASG 3 AZ sau **ALB** (hợp web app; NLB cũng dùng được, nên đây không phải điểm phân biệt).

#### Anh chọn C - vì sao trượt

C: **Aurora Global database**.

- Global Database dành cho **cross-Region** (DR, đọc gần user ở Region khác). Đề không yêu cầu nhiều Region → thừa.
- Option **không nói** đặt instance ở những AZ nào. Global Database không tự bảo đảm "3 AZ compute HA" nếu không tạo thêm replica; yêu cầu 3 AZ là thứ phải **chỉ rõ**, mà A chỉ rõ còn C thì không.
- Chi phí và độ phức tạp cao hơn cho nhu cầu không có.

Aurora storage luôn trải 3 AZ, nhưng nếu chỉ có **một instance** thì AZ đó chết là phải dựng lại instance - **compute** vẫn là điểm lỗi.

#### Thắc mắc: "Global Database cũng trải ≥ 3 AZ mà?"

**Đúng một nửa.** Storage của Global Database trải 3 AZ ở mỗi Region, nhưng đó là đặc điểm của **mọi** Aurora cluster (kể cả D chỉ có 1 instance), nên **không phải điểm phân biệt**.

```
Aurora STORAGE: luôn 6 bản copy / 3 AZ   ← A, C, D đều có
Aurora COMPUTE (instance):                ← đây mới quyết định HA
  - 1 instance → AZ chết = mất writer, phải dựng lại (vài phút+)
  - writer + replica ở AZ khác → tự promote ~30 giây
```

| | A. Aurora + replica 3 AZ | C. Aurora Global Database |
|---|---|---|
| Storage 3 AZ | Có | Có (mỗi Region) |
| **Compute HA qua 3 AZ** | **Có, nêu rõ** (writer + 2 replica) | **Không nêu**: Region chính chỉ có 1 writer nếu không thêm replica |
| Failover | Tự động trong Region, ~30 giây | Sang **Region phụ (read-only)** = failover **cross-Region**, mất vài phút, đổi endpoint |
| Phạm vi đề yêu cầu | Đúng: 3 AZ, 1 Region | Thừa: thêm Region không được yêu cầu |

→ Đề hỏi **HA qua AZ** chứ không hỏi **sống sót khi mất cả Region**, nên chọn A.

**Quy tắc:** "HA qua **AZ**" → **replica ở AZ khác** (Aurora replica hoặc RDS Multi-AZ DB cluster). "Sống sót khi **mất Region** / RPO < 1 giây cross-Region" → **Aurora Global Database**. Storage 3 AZ có sẵn ở mọi Aurora, **không bao giờ là yếu tố quyết định**.

#### Các phương án còn lại

- **B**: NLB + **RDS Multi-AZ** (2 AZ) + **Read Replica** ở AZ thứ ba. Kiểu Multi-AZ **instance** (như option mô tả) chỉ dùng **2 AZ**; Read Replica phải **promote thủ công**, không phải đích failover tự động. Không đạt "HA qua 3 AZ".
- **D**: Aurora **một AZ** + storage auto scaling. Neal: storage auto scaling vốn bật sẵn cho mọi Aurora và chỉ là **scale dung lượng**, không phải HA.

| Phương án | HA compute qua 3 AZ | Ghi chú |
|---|---|---|
| **A. Aurora writer + 2 replica ở 3 AZ** | **Có** | Failover tự động |
| B. RDS Multi-AZ + read replica | Không | 2 AZ + replica không auto-failover |
| C. Aurora Global | Không nêu | Cross-Region, thừa |
| D. Aurora 1 instance | Không | Chỉ scale storage |

#### Lưu ý thực tế

- Aurora cluster endpoint luôn trỏ writer hiện tại; reader endpoint cân bằng giữa các replica.
- Đặt replica ở AZ khác writer là cách chuẩn để vừa HA vừa giảm tải đọc.

#### Quy tắc nhớ cho thi

- **Thấy "HA qua 3 AZ" + DB** → **Aurora với replica ở 3 AZ**
- **RDS Multi-AZ DB instance** = 2 AZ (primary + standby không đọc được); **Aurora** trải 3 AZ qua replica
- 📝 **Ghi chú kiểm định (10-26):** từ 2022 RDS MySQL/PostgreSQL còn có **Multi-AZ DB cluster** (1 writer + 2 standby **đọc được** ở 3 AZ, failover ~35 giây). Nếu đề có lựa chọn này thì nó cũng đạt "HA qua 3 AZ". Câu này không có, nên đáp án A vẫn đúng.
- **Thấy "Global database"** → chỉ khi đề nói **multi-Region**
- **"Storage auto scaling"** = tăng dung lượng, không phải HA

### TD explanation

All answers include an ASG with Auto Scaling across three AZs. An Application Load Balancer is better suited to this particular use case but a Network Load Balancer could also be used. The key to answering correctly is to choose a storage solution that meets the requirement of high availability across three Availability Zones (AZs).
With Amazon Aurora you can have one writer instance and up to 15 Aurora Replicas. Aurora Replicas are read-only but are automatically promoted to be writer instances in the event of a failure. Therefore, for this solution we can have a single Aurora writer instance and two Aurora Replicas, each in separate AZs.
CORRECT:
"Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ and add Aurora Replicas in two more AZs" is the correct answer.
INCORRECT:
"Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind an Application Load Balancer. Create an Amazon Aurora Global database" is incorrect. Global database is used for cross-Region databases which is not required in this scenario.
INCORRECT:
"Create an Auto Scaling group of Amazon EC2 instances across three availability zones behind a Network Load Balancer. Create an Amazon Aurora PostgreSQL database in one AZ with storage auto scaling enabled" is incorrect. Storage auto scaling is enabled for all Aurora databases and does not provide high availability for the database, it provides scaling for the storage.
References:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

</details>

<a id="q71"></a>

## Q71

<!-- source: T3Q6 · domain: ORG · flagged -->



A large financial services company with multiple business units plans to migrate workloads to AWS. The company wants to implement a multi-account strategy to separate workloads, ensure strong security boundaries, and delegate limited administrative control to individual business units.
Key requirements include:
· Centralized governance and visibility across all AWS accounts
· Enforced compliance through guardrails and service control policies (SCPs)
· Integration with the corporate Microsoft Active Directory for authentication
· Role-based access to AWS accounts and resources for employees
· Minimal custom development and operational overhead
Which solution will BEST meet these requirements?

- **A.** Use AWS Organizations and manually create accounts. Configure IAM federation in each account using SAML with Microsoft AD. Apply SCPs and manage access permissions using IAM roles.
- **B.** Deploy AWS Control Tower to set up a landing zone. Use Account Factory for account provisioning. Integrate IAM Identity Center with Microsoft Active Directory and manage access centrally using permission sets and SCPs.
- **C.** Use AWS Single Sign-On (SSO) integrated with Active Directory. Manually create accounts in AWS Organizations and configure permissions in each account using IAM groups and roles.
- **D.** Create a single AWS account. Use IAM Identity Center integrated with Microsoft AD to manage access to resources. Apply IAM policies for role-based access control.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** multi-account, delegated admin, SCP guardrails, Microsoft AD, minimal overhead, Control Tower, Identity Center

🪤 **Your trap:** 🔁 Picked manual accounts with per-account SAML; high overhead. Control Tower landing zone with Account Factory and Identity Center gives guardrails and AD access with minimal setup.

🧠 **Rule:** Multi-account governance with minimal overhead: Control Tower plus Account Factory plus Identity Center. Manual per-account federation is the DIY trap.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhiều business unit ──► multi-account
   + governance tập trung (guardrails/SCP)
   + đăng nhập bằng Microsoft AD
   + role-based access
   + ÍT custom, ÍT vận hành
```

Đáp án đúng: **B (Control Tower + Account Factory + IAM Identity Center + AD)**. Anh chọn A. Câu này làm gấp, nên dễ bỏ qua cụm "minimal overhead".

#### Vì sao B đúng

| Yêu cầu | Thành phần |
|---|---|
| Multi-account, tách workload | **Control Tower landing zone** trên Organizations |
| Tạo account nhất quán | **Account Factory** |
| Guardrails / SCP | **Controls** của Control Tower (SCP + AWS Config) |
| Visibility tập trung | Log archive / audit account, dashboard Control Tower |
| Đăng nhập AD, role-based | **IAM Identity Center** + AD + **permission sets** |
| Ít vận hành | Tự động hóa dựng sẵn |

Control Tower tự dựng nền tảng (SCP, logging, baseline) thay vì anh tự làm từng bước.

#### Anh chọn A - vì sao trượt

A dùng Organizations + **tạo account thủ công** + **SAML federation ở từng account** + IAM roles.

- Đúng công cụ (SCP, SAML) nhưng **cấu hình rời rạc từng account** → vận hành nặng, không có điểm quản lý quyền tập trung. Neal: "no centralized access management, violates the minimal effort requirement."
- Thiếu cơ chế baseline/guardrail tự động cho account mới.

#### Các phương án còn lại

- **C**: Có Identity Center + AD, nhưng **tạo account thủ công** và **IAM groups/roles trong từng account** → thiếu tự động hóa, governance phân tán.
- **D**: **Một account duy nhất** → vi phạm multi-account strategy, không có ranh giới bảo mật giữa business unit.

| Phương án | Multi-account | Tự động hóa/guardrail | Access tập trung (AD) |
|---|---|---|---|
| A. Orgs thủ công + SAML mỗi account | Có | Không | Không |
| **B. Control Tower + Identity Center** | **Có** | **Có** | **Có** |
| C. Identity Center + account thủ công | Có | Không | Một phần |
| D. Một account | Không | - | Có |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** Trong đáp án B, "permission sets and SCPs" nói gộp. Thực tế **permission set** quản lý quyền người dùng (qua Identity Center), còn **SCP** là guardrail ở cấp Organizations; hai thứ khác lớp nhau. Đáp án B vẫn đúng.

- "AWS SSO" trong C là tên cũ của **IAM Identity Center**.
- Identity Center kết nối AD qua **AWS Managed Microsoft AD / AD Connector** hoặc IdP bên ngoài.
- Control Tower **không thay** Organizations; nó chạy trên đó.

#### Quy tắc nhớ cho thi

- **Thấy "multi-account + governance + minimal overhead"** → **Control Tower** (+ Account Factory)
- **Thấy "AD + role-based cho nhiều account"** → **IAM Identity Center + permission sets**
- **Thấy "manually create accounts"** → thường là đáp án sai
- **Thấy "single account"** khi đề cần tách business unit → loại

### TD explanation

This question tests your knowledge of governance, identity management, and automation in a multi-account AWS environment.
CORRECT:
"Deploy AWS Control Tower to set up a landing zone. Use Account Factory for account provisioning. Integrate IAM Identity Center with Microsoft Active Directory and manage access centrally using permission sets and SCPs."
is the correct answer.
AWS Control Tower automates the setup of a secure multi-account environment, including SCPs and governance baselines. It integrates natively with AWS Organizations and IAM Identity Center (formerly AWS SSO), which supports directory integration and centralized permission management. This solution minimizes custom coding and meets all technical requirements efficiently.
INCORRECT:
"Use AWS Organizations and manually create accounts. Configure IAM federation in each account using SAML with Microsoft AD. Apply SCPs and manage access permissions using IAM roles."
is incorrect.
While AWS Organizations and SCPs provide governance, manually managing accounts and setting up SAML-based federation in each account adds significant operational overhead. There's no centralized access management, which violates the minimal effort requirement.
INCORRECT:
"Use AWS Single Sign-On (SSO) integrated with Active Directory. Manually create accounts in AWS Organizations and configure permissions in each account using IAM groups and roles."
is incorrect.
This approach lacks automation and governance. Although AWS SSO (now IAM Identity Center) can integrate with AD, the manual account creation and distributed IAM role setup in each account increases complexity and undermines centralized control.
INCORRECT:
"Create a single AWS account. Use IAM Identity Center integrated with Microsoft AD to manage access to resources. Apply IAM policies for role-based access control."
is incorrect.
This violates the requirement for a multi-account strategy and strong workload isolation. Using one account for multiple business units leads to governance, security, and billing challenges, making it unsuitable for large enterprise structures.
References:
https://docs.aws.amazon.com/controltower/
https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

</details>

---

# Group B — Identity/org scope: wrong account, level, principal or SCP mode (6)

<a id="q14"></a>

## Q14

<!-- source: T5Q13 · domain: NEW -->



An application runs on Amazon EC2 instances in a private subnet within an Amazon VPC. The application stores files in a specific Amazon S3 bucket. The files should not traverse the internet and only the application instances should be granted access to save files to the S3 bucket. A gateway endpoint has been created for Amazon S3 and connected to the Amazon VPC.
What additional steps should a Solutions Architect take to meet the stated requirements?

- **A.** Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Attach a bucket policy to the S3 bucket that grants access only to the VPC endpoint.
- **B.** Attach a bucket policy to the S3 bucket that grants access to the EC2 instances only using the aws:SourceIp condition. Update the VPC route table so only the application EC2 instances can access the VPC endpoint.
- **C.** Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Assign an IAM role to the EC2 instances and attach a policy to the S3 bucket that grants access only to this role.
- **D.** Attach an endpoint policy to the gateway endpoint that restricts access to S3 in the current Region. Attach a bucket policy to the S3 bucket that grants access to ec2.amazonaws.com service only.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** S3 gateway endpoint, only app instances may write, endpoint policy, bucket policy, IAM role

🪤 **Your trap:** Bucket policy limited to the VPC endpoint lets any instance in the subnet with S3 permissions write; it does not isolate the application instances.

🧠 **Rule:** Restrict who via IAM role plus bucket policy naming that role; endpoint policy restricts which bucket. VPC endpoint condition alone is network, not identity.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC
 └─ Private subnet: EC2 (app) ──► Gateway Endpoint ──► S3 bucket X
                                  (đã tạo)
Yêu cầu 1: không đi qua internet        -> gateway endpoint lo
Yêu cầu 2: CHỈ bucket X                 -> endpoint policy
Yêu cầu 3: CHỈ các instance của app     -> ???
```

Đáp án đúng: **C**. Anh chọn A.

#### Vì sao C đúng

Ba lớp kiểm soát, mỗi lớp giải một yêu cầu:

```
Endpoint policy : endpoint chỉ cho đi tới bucket X
IAM role        : gắn vào EC2 của app (danh tính của app)
Bucket policy   : Allow chỉ principal = role đó
```

Yêu cầu "chỉ application instances" là yêu cầu về **danh tính (identity)**, nên phải dùng **IAM role + bucket policy theo principal**.

#### Vì sao A (anh chọn) sai

A có endpoint policy giới hạn bucket (đúng) và bucket policy "chỉ cho phép từ VPC endpoint" (kiểu `aws:SourceVpce`). Nghe an toàn, nhưng điều kiện này kiểm soát **đường đi (network path)**, không phân biệt instance nào. Mọi EC2 khác trong private subnet cũng đi qua endpoint đó, nên bucket vẫn mở cho chúng (nếu chúng có quyền S3). Đề: "only the application instances".

#### Các phương án còn lại

- **B:** `aws:SourceIp` chỉ dùng cho **public IP**. Request qua gateway endpoint không mang IP public để so khớp theo cách này. Route table cũng không kiểm soát được "instance nào" dùng endpoint, chỉ kiểm soát subnet.
- **D:** endpoint policy cho cả S3 trong Region (quá rộng) và `ec2.amazonaws.com` là service principal, không khóa bucket cũng không khóa đúng instance.

| Phương án | Giới hạn bucket | Giới hạn đúng app |
|---|---|---|
| **C** | Endpoint policy | IAM role + bucket policy |
| A | Endpoint policy | Chỉ giới hạn theo endpoint, không theo instance |
| B | Không | SourceIp sai ngữ cảnh |
| D | Chỉ mức Region | Service principal, không khóa instance |

#### Lưu ý thực tế

- Gateway endpoint thêm route tới prefix list của S3 vào route table của subnet; không có ENI/IP riêng.
- Bucket policy dùng `aws:SourceVpce` / `aws:SourceVpc` hợp lệ khi muốn khóa theo mạng, nhưng nó không thay thế cho kiểm soát theo danh tính.

#### Quy tắc nhớ cho thi

- **"Only these instances / this application"** → **IAM role + policy theo role** (identity)
- **"Not traverse the internet"** → **VPC endpoint**
- **"Only this bucket via endpoint"** → **endpoint policy**
- **VPC endpoint condition** = khóa theo **mạng**, không khóa theo **instance**
- **aws:SourceIp + private IP** → sai

### TD explanation

An endpoint policy can be attached to a gateway endpoint that will restrict access to the specific S3 bucket. This means the gateway endpoint can only be used to access that one particular bucket. To restrict access to the bucket to the EC2 instances only an IAM role can be assigned to the instances and then a bucket policy can be added to the bucket that restricts access only to the IAM role. This solution meets all requirements.
The diagram below depicts this configuration:
CORRECT:
"Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Assign an IAM role to the EC2 instances and attach a policy to the S3 bucket that grants access only to this role" is the correct answer.
INCORRECT:
"Attach an endpoint policy to the gateway endpoint that restricts access to the specific S3 bucket. Attach a bucket policy to the S3 bucket that grants access only to the VPC endpoint" is incorrect. This does not restrict access to the specific EC2 instances running the application. This will allow any EC2 instances in the private subnet to access the S3 bucket (if they have S3 permissions).
INCORRECT:
"Attach a bucket policy to the S3 bucket that grants access to the EC2 instances only using the aws:SourceIp condition. Update the VPC route table so only the application EC2 instances can access the VPC endpoint" is incorrect. The aws:SourceIp condition is used for restricting access based on public IP addresses, not private IP addresses.
INCORRECT:
"Attach an endpoint policy to the gateway endpoint that restricts access to S3 in the current Region. Attach a bucket policy to the S3 bucket that grants access to ec2.amazonaws.com service only" is incorrect. This solution does not lock down the specific bucket or the specific application EC2 instances and fails to meet all requirements.
References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html#vpc-endpoint-policies
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q23"></a>

## Q23

<!-- source: T3Q24 · domain: ORG -->



A company is in the process of migrating applications to AWS using multiple accounts in AWS Organizations . The management account is at the root of the Organizations hierarchy. Business units each have different accounts and requirements for the services they need to use. The security team needs to implement controls across all accounts to prohibit many AWS services. In some cases a business unit may have a valid exception to these controls and this must be achievable.
Which solution will meet these requirements with minimal optional overhead?

- **A.** Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level. For any specific exceptions for an OU, create a new SCP for that OU and add the required AWS services to the allow list.
- **B.** Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level and each OU. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions, modify the SCP attached to that OU, and add the required AWS services to the allow list.
- **C.** Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at each OU level. Leave the default AWS managed SCP attached to the root level and all OUs. For accounts that require specific exceptions, create an OU under root and attach an SCP the denies fewer services.
- **D.** Use an SCP in Organizations to implement an allow list of AWS services. Apply this SCP at the root level. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions for an OU, modify the SCP attached to that OU, and add the required AWS services to the allow list.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** Organizations SCP deny list, exceptions per OU, minimal overhead, default FullAWSAccess, allow list

🪤 **Your trap:** 🔁 Chose allow-list SCP, which needs every permitted action listed and removal of FullAWSAccess; high overhead. Deny list keeps FullAWSAccess; exception OU sits under root with fewer denies.

🧠 **Rule:** Many services blocked plus exceptions: deny list, keep FullAWSAccess, exceptions via a separate OU. Allow list needs every action listed.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Root (mgmt account)
 ├─ OU-A  ┐
 ├─ OU-B  ├─ cần CHẶN nhiều service
 ├─ OU-C  ┘
 └─ OU-Exception (nằm ngay dưới Root) ← ngoại lệ, chặn ít hơn
Yêu cầu: chặn nhiều service, cho phép ngoại lệ, overhead THẤP NHẤT
```

Đáp án đúng: **C (deny list áp ở từng OU + OU ngoại lệ dưới Root)**. Anh chọn D (allow list).

#### Hai chiến lược SCP

```
Deny list : giữ FullAWSAccess (Allow *) ở mọi cấp + gắn SCP Deny service cấm
Allow list: gỡ FullAWSAccess, phải Allow tường minh ở MỌI cấp
```

Với SCP, quyền hiệu lực là **giao** của các cấp: Root, OU, account đều phải cho phép. **Explicit Deny ở cấp trên luôn thắng Allow ở cấp dưới.**

#### Vì sao C đúng

- Giữ `FullAWSAccess` mặc định ở Root và mọi OU, nên không phải liệt kê hết các service cần dùng.
- Gắn SCP deny list ở **từng OU** (không gắn ở Root).
- Account cần ngoại lệ: đặt vào **OU riêng nằm dưới Root**, không nằm trong nhánh OU bị deny, gắn SCP deny ít service hơn. Vì deny ở trên không bị ghi đè bởi allow ở dưới, ngoại lệ chỉ làm được bằng cách đưa account ra khỏi nhánh bị deny.

#### Vì sao D (anh chọn) sai

D là allow list gắn ở Root, gỡ `FullAWSAccess`, rồi "sửa SCP của OU để thêm service". Theo đề: một SCP gắn ở nhiều cấp không thể sửa riêng tại một OU con, chỉ sửa ở một nơi nên mọi OU đều đổi theo. Ngoài ra allow list cần liệt kê toàn bộ service được dùng và phải có Allow ở mọi cấp, nên overhead cao, trái "minimal operational overhead".

#### Các phương án còn lại

- **A:** deny ở Root rồi tạo SCP allow riêng cho OU. Không được: **Deny ở cấp trên đè Allow ở cấp dưới**.
- **B:** deny ở Root và từng OU, gỡ `FullAWSAccess`, sửa SCP để thêm allow. Cùng lỗi "không sửa riêng ở một OU con" và deny cấp trên vẫn đè allow.

| Phương án | Chiến lược | Ngoại lệ làm được? | Lỗi chính |
|---|---|---|---|
| **C** | Deny list ở OU | Có, OU riêng dưới Root | Không |
| A | Deny ở Root | Không | Deny trên đè Allow dưới |
| B | Deny ở Root+OU | Không | Deny đè; sửa SCP dùng chung |
| D | Allow list ở Root | Khó | SCP dùng chung; overhead cao |

#### Lưu ý thực tế

- SCP **không áp** lên management account; nó chỉ giới hạn quyền tối đa, không cấp quyền.
- Gỡ `FullAWSAccess` mà chưa có Allow thay thế sẽ chặn sạch mọi thứ.

#### Quy tắc nhớ cho thi

- **"Chặn một số service, vẫn cần ngoại lệ"** → **deny list** + **OU riêng dưới Root** cho ngoại lệ
- **Explicit Deny cấp trên** → luôn thắng, không allow nào ở dưới cứu được
- **Allow list** = overhead cao, phải Allow ở mọi cấp
- **Muốn nới cho một account** → **di chuyển nó** sang nhánh khác, đừng cố "allow" trong nhánh bị deny

### TD explanation

AWS Organizations Service Control Policies (SCPs) can be used to control the maximum available permissions in an AWS account. The permissions flow through a hierarchy from the root to all entities beneath. With a deny list strategy a default SCP allows all services and deny lists must be implemented for any specific services that must be restricted.
In this scenario using a deny list strategy will mean the AWS managed SCP at the root level and all OUs will allow all services for all business units. An SCP can then be defined that prohibits AWS services and this can be applied to all OUs.
When an exception is required, an OU must be created under root with an SCP that has fewer restrictions. This OU must be under root so it is not part of the hierarchy of OUs that have denies, as a deny at a higher level always overrides an allow.
The diagram below depicts a scenario with a deny list strategy and SCPs applied to multiple OUs/accounts:
CORRECT:
"Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at each OU level. Leave the default AWS managed SCP attached to the root level and all OUs. For accounts that require specific exceptions, create an OU under root and attach an SCP the denies fewer services" is the correct answer.
INCORRECT:
"Use an SCP in Organizations to implement an allow list of AWS services. Apply this SCP at the root level. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions for an OU, modify the SCP attached to that OU, and add the required AWS services to the allow list" is incorrect. You cannot modify an SCP that is applied to multiple OUs at one child OU. It must be edited in one place.
INCORRECT:
"Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level. For any specific exceptions for an OU, create a new SCP for that OU and add the required AWS services to the allow list" is incorrect. This will not work as there is an explicit deny at a higher level and this will override an allow at any level beneath.
INCORRECT:
"Use an SCP in Organizations to implement a deny list of AWS services. Apply this SCP at the root level and each OU. Remove the default AWS managed SCP from the root level and all OU levels. For any specific exceptions, modify the SCP attached to that OU, and add the required AWS services to the allow list" is incorrect. You cannot modify an SCP that is applied to multiple OUs at one child OU. It must be edited in one place. This will also not work as there is an explicit deny at a higher level and this will override an allow at any level beneath.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_auth.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

</details>

<a id="q28"></a>

## Q28

<!-- source: T4Q12 · domain: ORG · flagged -->



A company is creating a multi-account structure using AWS Organizations. The accounts will include the Management account, Production account, and Development account. The company requires auditing for all API actions across accounts. A Solutions Architect is advising the company on how to configure the accounts. Which of the following recommendations should the Solutions Architect make? (Select TWO.)

- **A.** Enable AWS CloudTrail and keep all CloudTrail trails and logs in the management account.
- **B.** Create user accounts in the Production and Development accounts.
- **C.** Enable AWS CloudTrail and keep all CloudTrail trails and logs within each account.
- **D.** Create user accounts in the Management account and use cross-account access to access resources.
- **E.** Create all resources in the Management account and grant access to the Production and Development accounts.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B · **You picked:** A, E

🔑 **Key words:** Organizations multi-account, CloudTrail centralised in management account, users in member accounts (select two)

🪤 **Your trap:** 🔁 Picked A correctly but also E, putting resources in the management account. SCPs do not restrict management account, so keep resources and users in member accounts.

🧠 **Rule:** Management account holds only org-level tasks and CloudTrail. Users and resources live in member accounts; SCPs never cover management.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
 ├─ Management account  ← SCP KHÔNG giới hạn được user/role ở đây
 ├─ Production account
 └─ Development account
Yêu cầu: audit mọi API action trên các account. Chọn 2.
```

Đáp án đúng: **A + B**. Anh chọn **A + E**: A đúng, E sai. Anh đánh dấu "không chắc", đúng là chỗ dễ nhầm.

#### Hai đáp án đúng ghép thành một thiết kế

- **A. CloudTrail, trail và log giữ ở management account:** gom log về một chỗ để audit tập trung. Đây là ngoại lệ AWS khuyến nghị: nên bật CloudTrail và giữ trail/log liên quan ở management account.
- **B. Tạo user ở Production và Development account:** workload và người dùng nằm ở member account, nên SCP áp được lên họ.

Nguyên tắc chung: dùng management account chỉ cho việc **chỉ nó mới làm được**; để mọi resource ở account khác.

#### Vì sao E (anh chọn) sai

E: tạo hết resource ở management account rồi cấp quyền cho Prod/Dev. Lỗi:
- **SCP không hạn chế được user/role trong management account**, nên đặt resource ở đó là mất lớp kiểm soát.
- Tách resource khỏi management account còn giúp đọc hóa đơn rõ theo account.
- Đề: resource phải tạo ở đúng account (Production/Development), không "tập trung rồi cấp quyền".

#### Các phương án còn lại

- **C:** để trail/log trong từng account: AWS khuyến nghị tập trung về management account, không phân tán.
- **D:** tạo user ở management account và dùng cross-account access: user ở management account không bị SCP giới hạn nên không phải best practice.

| Phương án | Ý chính | Đánh giá |
|---|---|---|
| **A** | CloudTrail tập trung ở mgmt | Đúng |
| **B** | User ở Prod/Dev | Đúng |
| C | CloudTrail rải từng account | Sai, không tập trung |
| D | User ở mgmt + cross-account | Sai, SCP không phủ mgmt |
| E | Resource ở mgmt | Sai, SCP không phủ mgmt |

📝 **Ghi chú kỹ thuật:** Trong thực tế, mô hình mạnh hơn là tạo **organization trail** (từ management account, áp cho mọi member account) và gửi log về S3 ở một log archive account riêng. Nhưng theo wording của đề, A là đáp án vì AWS nói giữ trail/log ở management account.

#### Quy tắc nhớ cho thi

- **"Multi-account + audit mọi API"** → **CloudTrail tập trung** (A)
- **Management account** → chỉ làm việc bắt buộc; **không đặt workload, không đặt user thường**
- **SCP không chạm management account** → mọi lựa chọn dựa vào mgmt account để kiểm soát đều sai
- **Multi-select** → mỗi lựa chọn phải thuộc cùng một thiết kế: log tập trung (A) + identity ở member account (B)

#### 📝 Ghi chú kiểm định (10-26)
- Đáp án A + B là **tốt nhất trong 5 lựa chọn**, nhưng cách diễn đạt **đã cũ**. Best practice hiện nay: **organization trail** ghi log về một **Log Archive account** riêng (không "giữ trong management account"); người dùng quản lý tập trung qua **IAM Identity Center** (không tạo IAM user từng account).
- Nguyên tắc cần nhớ: **management account chỉ làm việc cấp tổ chức** (SCP không áp dụng lên nó) → workload và người dùng ở **member account**. Lựa chọn E (đặt mọi tài nguyên ở management account) **sai rõ ràng**.

### TD explanation

AWS recommends that you use the management account and its users and roles only for tasks that can be performed only by that account. Store all of your AWS resources in
other
AWS accounts in the organization and keep them out of the management account. The one exception is that AWS does recommend that you enable AWS CloudTrail and keep relevant CloudTrail trails and logs in the management account.
One important reason to keep your resources in other accounts is because Organizations service control policies (SCPs) do not work to restrict any users or roles in the management account.
Separating your resources from your management account also help you to understand the charges on your invoices.
CORRECT:
"Enable AWS CloudTrail and keep all CloudTrail trails and logs in the management account" is a correct answer.
CORRECT:
"Create user accounts in the Production and Development accounts" is also a correct answer.
INCORRECT:
"Enable AWS CloudTrail and keep all CloudTrail trails and logs within each account" is incorrect. AWS recommends that you centralize this data to the management account.
INCORRECT:
"Create user accounts in the Management account and use cross-account access to access resources" is incorrect. Because user accounts in the management account are not restricted by SCPs, this is not a best practice.
INCORRECT:
"Create all resources in the Management account and grant access to the Production and Development accounts" is incorrect. Resources should be created in the relevant accounts (Production/Development), you cannot just grant access and have them in the management account.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

</details>

<a id="q51"></a>

## Q51

<!-- source: T3Q27 · domain: NEW -->



A company requires federated access to AWS for users of a mobile application. The security team has mandated that the application must use a custom-built solution for authenticating users and use IAM roles for authorization.
Which of the following actions would enable authentication and authorization and satisfy the requirements? (Select TWO.)

- **A.** Use a custom-built SAML-compatible solution for authentication and use AWS SSO for authorization.
- **B.** Create a custom-built LDAP connector using Amazon API Gateway and AWS Lambda for authentication. Use a token-based Lambda authorizer that uses JWT.
- **C.** Use a custom-built OpenID Connect-compatible solution with AWS SSO for authentication and authorization.
- **D.** Use a custom-built SAML-compatible solution that uses LDAP for authentication and uses a SAML assertion to perform authorization to the IAM identity provider.
- **E.** Use a custom-built OpenID Connect-compatible solution for authentication and use Amazon Cognito for authorization.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D, E · **You picked:** B, D

🔑 **Key words:** mobile app, custom authentication, IAM roles authorization, OIDC with Cognito, SAML with LDAP (select two)

🪤 **Your trap:** Picked B (LDAP connector with Lambda authorizer JWT); that only authorizes API calls and gives no IAM role credentials. Needed OIDC plus Cognito, or SAML assertion to IAM IdP.

🧠 **Rule:** Custom IdP to IAM roles: OIDC provider plus Cognito identity pool, or SAML assertion via IAM IdP. API Gateway authorizers do not issue AWS credentials.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile app ──► Custom IdP (tự xây) ──► token / assertion
                                           │
                                           ▼
                     AWS: đổi token lấy credential tạm của IAM role
```

Yêu cầu: **authentication bằng giải pháp custom**, **authorization bằng IAM roles**. Chọn 2 đáp án, mỗi đáp án là **một giải pháp trọn vẹn riêng**. Đáp án đúng: **D + E**. Anh chọn B + D: đúng D, sai B (thiếu E).

#### Hai cách hợp lệ (mỗi cách đứng độc lập)

**E - OIDC custom + Amazon Cognito (identity pool):**

```
App ─► custom OIDC IdP ─► ID token ─► Cognito identity pool ─► STS ─► credential tạm (IAM role)
```

Identity pool nhận token từ OIDC provider (đăng ký OIDC provider trong IAM / identity pool), cấp **temporary AWS credentials** gắn IAM role. Đây là mẫu chuẩn cho **mobile app**.

**D - SAML custom (LDAP phía sau) + SAML assertion:**

```
User ─► custom SAML IdP (xác thực LDAP) ─► SAML assertion ─► sts:AssumeRoleWithSAML ─► IAM role
```

IAM SAML identity provider tin IdP; assertion map user/group sang IAM role. Authorization = role được assume.

#### Anh chọn B - vì sao trượt

B: LDAP connector bằng API Gateway + Lambda, rồi **Lambda authorizer (JWT)**.

- Lambda authorizer chỉ **cho phép/từ chối lời gọi API Gateway** của chính anh. Nó **không** cấp IAM role hay credential AWS cho app.
- Đề yêu cầu "IAM roles for authorization" → B không có bước đổi sang IAM role. Neal: "not a complete solution, API Gateway not required."

#### Các phương án còn lại (đều dính AWS SSO)

- **A** (SAML + AWS SSO) và **C** (OIDC + AWS SSO): **AWS SSO = IAM Identity Center** là SSO cho **workforce** (nhân viên vào console/app tổ chức), không phải cho user cuối của mobile app. Neal: "cannot be used for mobile applications."

| Phương án | Có IdP custom | Kết thúc ở IAM role | Kết luận |
|---|---|---|---|
| A. SAML + AWS SSO | Có | Qua Identity Center | Sai kênh |
| B. LDAP + Lambda authorizer | Có | Không | Thiếu bước chính |
| C. OIDC + AWS SSO | Có | Qua Identity Center | Sai kênh |
| **D. SAML + LDAP + assertion** | Có | AssumeRoleWithSAML | Đúng |
| **E. OIDC + Cognito** | Có | Identity pool | Đúng |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** "AWS SSO" trong đề nay đã đổi tên thành **IAM Identity Center**; đáp án vẫn giữ nguyên vì Identity Center phục vụ workforce, không phải end-user mobile.

- Cognito có hai thứ: **user pool** (đăng ký/đăng nhập, phát token) và **identity pool** (đổi token lấy AWS credential). Câu này dùng identity pool vì IdP là custom.
- Với SAML cho mobile thực tế ít dùng hơn OIDC, nhưng đề chấp nhận cả hai.

#### Quy tắc nhớ cho thi

- **Thấy "mobile app + AWS credential/IAM role"** → **Cognito identity pool**
- **Thấy "custom OIDC IdP"** → OIDC provider + Cognito
- **Thấy "custom SAML IdP"** → IAM SAML provider + `AssumeRoleWithSAML`
- **Thấy "AWS SSO / Identity Center"** → workforce, loại khi đề nói mobile/customer app
- **Thấy "Lambda authorizer"** → bảo vệ API, không cấp IAM role

### TD explanation

> ⚠️ 'AWS SSO' is now IAM Identity Center.

There are two possible solutions for this scenario:
· An OpenID Connect provider can be added in IAM to enable federated authentication. An Amazon Cognito identity pool can then be used for authorization. Amazon Cognito identity pools provide temporary AWS credentials for users who are guests (unauthenticated) and for users who have been authenticated and received a token.
· AWS supports identity federation with SAML 2.0. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without you having to create an IAM user for everyone in your organization. In your organization's IdP, you define assertions that map users or groups in your organization to the IAM roles.
The diagram below shows how the authentication and authorization process works when assuming a role using SAML:
CORRECT:
"Use a custom-built OpenID Connect-compatible solution for authentication and use Amazon Cognito for authorization" is a correct answer.
CORRECT:
"Use a custom-built SAML-compatible solution that uses LDAP for authentication and uses a SAML assertion to perform authorization to the IAM identity provider" is also a correct answer.
INCORRECT:
"Use a custom-built SAML-compatible solution for authentication and use AWS SSO for authorization" is incorrect. AWS SSO cannot be used for mobile applications.
INCORRECT:
"Create a custom-built LDAP connector using Amazon API Gateway and AWS Lambda for authentication. Use a token-based Lambda authorizer that uses JWT" is incorrect. This is not a complete solution and API Gateway is not required for this solution.
INCORRECT:
"Use a custom-built OpenID Connect-compatible solution with AWS SSO for authentication and authorization" is incorrect. AWS SSO cannot be used for mobile applications.
References:
https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

</details>

<a id="q56"></a>

## Q56

<!-- source: T6Q2 · domain: ORG -->



A company is creating an account structure on AWS. There will be separate accounts for the production and testing environments. The Solutions Architect wishes to implement centralized control of security identities and permissions to access the environments.
Which solution is most appropriate for these requirements?

- **A.** Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the production and testing accounts. Add the identity account to the trust policies for the roles.
- **B.** Create an AWS Organization that includes the production and testing accounts. Create IAM user accounts in the production and testing accounts and implement service control policies (SCPs) to centrally control permissions.
- **C.** Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the identity account and delegate access to the production and testing accounts.
- **D.** Create all user accounts in the production account. Create roles for access in the production account and testing accounts. Grant cross-account access from the production account to the testing account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** separate identity account, IAM users, roles in prod/test with trust policy, central security identities

🪤 **Your trap:** 🔁 Picked IAM users per account with SCPs; SCPs only restrict, never grant, and users stay scattered. Central identities need an identity account trusted by roles in each target account.

🧠 **Rule:** Central identities: users in one identity account, roles in target accounts whose trust policy names the identity account. SCPs never grant.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
        ┌──────────────────┐
        │ Identity account │  IAM users nằm ĐÂY (tập trung)
        └───────┬──────────┘
      AssumeRole│(trust policy)
      ┌─────────┴─────────┐
      ▼                   ▼
┌───────────┐       ┌───────────┐
│ Prod acct │       │ Test acct │  roles + permissions nằm ĐÂY
└───────────┘       └───────────┘
```

Yêu cầu khóa: **centralized control of security identities** (danh tính) và permissions. Đáp án đúng: **A**. Anh chọn B.

#### Vì sao A đúng

Mẫu **identity account (hub) + cross-account role (spoke)**:

- User chỉ tạo **một nơi** (identity account) → quản lý danh tính tập trung.
- Trong từng account tài nguyên (prod/test) tạo **role** với quyền phù hợp; **trust policy** của role tin identity account.
- User ở identity account gọi `sts:AssumeRole` vào role của account đích (cần thêm quyền AssumeRole phía identity account).

#### Anh chọn B - vì sao trượt

B: Organizations + **tạo IAM user ngay trong prod và test** + SCP.

- IAM user luôn thuộc **một account cụ thể**. Tạo ở từng account = danh tính **phân tán**, Organizations không gom được. Đúng như Neal: "identities are always created within individual accounts."
- **SCP không cấp quyền**, chỉ đặt **trần quyền tối đa** (guardrail). Không thay cho việc gán IAM policy cho user. Nên B không "control permissions" theo nghĩa cấp quyền.
- Organizations/SCP vẫn có ích, nhưng là lớp bổ sung, không giải quyết yêu cầu về danh tính.

#### Các phương án còn lại

- **C**: Tạo role trong **identity account** rồi "delegate access to prod/test". Sai chiều: role phải nằm ở **account có tài nguyên** (account đích), vì role là thứ chứa quyền truy cập tài nguyên account đó.
- **D**: Gom user vào **prod account**. Trộn danh tính với workload production, không có account riêng cho identity; và prod phải cấp quyền ngược sang test - vi phạm tách biệt.

| Phương án | Danh tính tập trung | Role đặt đúng chỗ |
|---|---|---|
| **A** | Có (identity account) | Có (prod, test) |
| B | Không (user mỗi account) | Không có cross-account role |
| C | Có | Không (role ở identity account) |
| D | Không đúng nghĩa (nằm trong prod) | Lộn xộn |

#### Lưu ý thực tế

- Role cross-account cần **hai nửa**: trust policy ở account đích **và** identity policy cho phép `sts:AssumeRole` ở account nguồn.
- Thực tế hiện nay AWS khuyến nghị **IAM Identity Center** cho workforce thay vì IAM user; nhưng nguyên lý hub-and-spoke của đề vẫn là đáp án thi.

#### Quy tắc nhớ cho thi

- **Thấy "centralized identities, nhiều account"** → **identity account + cross-account roles**
- **Role nằm ở account có tài nguyên**, trust trỏ về identity account
- **SCP** = trần quyền, **không cấp quyền**, không quản lý danh tính
- **IAM user là per-account** → Organizations không gom user

### TD explanation

The AWS best practice for this situation is to use an identity account to store all user and service accounts. You then create roles in the accounts you want to access and delegate permissions for the identity account users (or the whole account) to be able to assume the role. This provides centralized control of security identities.
The configuration for cross-account access between two accounts is depicted below. In this diagram the user in account B (the identity account) is able to assume a role in account A (the resource account) and access an S3 bucket.
CORRECT:
"Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the production and testing accounts. Add the identity account to the trust policies for the roles" is the correct answer.
INCORRECT:
"Create an AWS Organization that includes the production and testing accounts. Create IAM user accounts in the production and testing accounts and implement service control policies (SCPs) to centrally control permissions" is incorrect. The identities should be created in a separate identity account as Organizations does not provide centralized control of identities as they are always created within individual accounts. SCPs control the maximum available permissions but to not actually control the IAM permissions assigned to users.
INCORRECT:
"Create a separate AWS account for identities where IAM user accounts can be created. Create roles with appropriate permissions in the identity account and delegate access to the production and testing accounts" is incorrect. The roles should be created in the production and testing accounts, not in the identity account.
INCORRECT:
"Create all user accounts in the production account. Create roles for access in the production account and testing accounts. Grant cross-account access from the production account to the testing account" is incorrect. A separate account should be created for identities.
References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

</details>

<a id="q59"></a>

## Q59

<!-- source: T1Q5 · domain: ORG -->



A company requires that only the master account in AWS Organizations is able to purchase Amazon EC2 Reserved Instances. Current and future member accounts should be blocked from purchasing Reserved Instances.
Which solution will meet these requirements?

- **A.** Create an Amazon CloudWatch Events rule that triggers a Lambda function to terminate any Reserved Instances launched by member accounts.
- **B.** Create an OU for the master account and each member account. Move the accounts into their respective OUs. Apply an SCP to the master accounts’ OU with the Allow effect for the ec2:PurchaseReservedInstancesOffering.
- **C.** Move all current member accounts to a new OU. Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the new OU.
- **D.** Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the root of the organization.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** Organizations, only management account may buy Reserved Instances, SCP Deny at root, current and future members

🪤 **Your trap:** SCP on a new OU covers only current moved accounts, missing future ones. SCP never affects the management account, so Deny at root blocks all members and spares management.

🧠 **Rule:** Block for every present and future member: Deny SCP at root. Management account is exempt from SCPs anyway.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Root
 ├── Management account   (SCP KHÔNG áp dụng)
 └── OU(s)
      ├── Member account hiện tại
      └── Member account TƯƠNG LAI  (sẽ được tạo / mời vào)
```

Yêu cầu: chỉ management (master) account mua được Reserved Instances; member **hiện tại và tương lai** bị chặn. Đáp án đúng: **D**. Anh chọn C.

#### Vì sao D đúng

- **SCP Deny** `ec2:PurchaseReservedInstancesOffering` gắn ở **root** của organization.
- Mọi OU và account đều **kế thừa** policy gắn ở root, kể cả account **mới** thêm sau này (account mới mặc định nằm dưới root rồi mới di chuyển).
- **SCP chỉ ảnh hưởng member account**, không tác động user/role trong management account → management vẫn mua được. Chính đặc tính này làm giải pháp gọn: không cần loại trừ management.

#### Anh chọn C - vì sao trượt

C: gom **member hiện tại** vào OU mới, gắn SCP Deny cho OU đó.

- Chỉ phủ account **đã có** lúc đó. Account tạo/mời sau này nếu không được nhớ chuyển vào OU kia thì **không bị chặn**.
- Đề nói rõ "current **and future**" → cần gắn ở mức **root** để kế thừa tự động.
- Thêm việc di chuyển account = công sức không cần thiết.

#### Các phương án còn lại

- **B**: Dùng **Allow** cho OU của management. SCP Allow **không cấp quyền** (chỉ là danh sách cho phép tối đa) và không **chặn** member. Cấu trúc mỗi account một OU thì phức tạp vô ích.
- **A**: EventBridge + Lambda "terminate Reserved Instances". RI là **hợp đồng giảm giá thanh toán**, không phải instance để terminate; phản ứng sau khi đã mua; Neal còn nói CloudWatch Events không trigger theo hành động mua RI.

| Cách | Phủ account tương lai | Chặn thật (preventive) |
|---|---|---|
| A. Lambda terminate | Không rõ | Không (sau sự việc) |
| B. Allow ở OU management | Không | Không |
| C. Deny ở OU mới | **Không** | Có |
| **D. Deny ở root** | **Có** | **Có** |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** Phần giải thích A của Neal ("CloudWatch Events không trigger được") không đáng tin để học; lý do vững hơn là RI không phải thứ để terminate và cách này là **detective**, không phải **preventive**. Đáp án D không đổi.

- SCP **không bao giờ** ảnh hưởng management account, nên không dùng SCP để bảo vệ chính management account.
- Cần có `FullAWSAccess` (hoặc allow-list) song song; Deny ở root chỉ cắt một action cụ thể.

#### Quy tắc nhớ cho thi

- **Thấy "current and future accounts"** → **gắn SCP ở root**
- **Thấy "chặn một action"** → SCP **Deny**, không phải Allow
- **Thấy "management account được phép"** → SCP vốn không áp dụng cho nó, khỏi loại trừ
- **SCP Allow** ≠ cấp quyền, chỉ là trần

### TD explanation

The only solution that works for both existing and future member accounts is to apply a Deny policy to the root of the organization. When you attach a policy to the organization root, all OUs and accounts in the organization inherit that policy which ensures that any new accounts that are added will inherit the policy automatically.
SCPs affect only
member
accounts in the organization. They have no effect on users or roles in the management account (also known as the master account). Therefore, the users in the management account are able to purchase reserved instances.
Note the following behavior in relation to policy inheritance:
You can attach policies to organization entities (organization root, organizational unit (OU), or account) in your organization:
When you attach a policy to the organization root, all OUs and accounts in the organization inherit that policy.
When you attach a policy to a specific OU, accounts that are directly under that OU or any child OU inherit the policy.
When you attach a policy to a specific account, it affects only that account.
CORRECT:
"Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the root of the organization" is the correct answer.
INCORRECT:
"Move all current member accounts to a new OU. Create an SCP with the Deny effect on the ec2:PurchaseReservedInstancesOffering action. Attach the SCP to the new OU" is incorrect. This will work for existing accounts but if new accounts are added and are not added to the same OU they will not inherit the policy.
INCORRECT:
"Create an Amazon CloudWatch Events rule that triggers a Lambda function to terminate any Reserved Instances launched by member accounts" is incorrect. CloudWatch Events is not able to trigger based on EC2 Reserved Instance purchase actions.
INCORRECT:
"Create an OU for the master account and each member account. Move the accounts into their respective OUs. Apply an SCP to the master accounts’ OU with the Allow effect for the ec2:PurchaseReservedInstancesOffering" is incorrect. This is a complex setup and does not deny the relevant API actions from the member accounts.
References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance.html
https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseReservedInstancesOffering.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

</details>

---

# Group C — Right service family, wrong feature variant for the stated need (6)

<a id="q17"></a>

## Q17

<!-- source: T5Q24 · domain: CI -->



An application publishes data continuously to Amazon DynamoDB using an AWS Lambda function. The DynamoDB table has an auto scaling policy enabled with the target utilization set to 70%. There are short predictable periods in which a large volume of data is received and this can exceed the typical load by up to 300%. The AWS Lambda function writes
ProvisionedThroughputExceededException messages to Amazon CloudWatch Logs during these times, and some records are redirected to the dead letter queue.
What change should the company make to resolve this issue?

- **A.** Use Amazon CloudWatch Events to monitor the dead letter queue and invoke a Lambda function to automatically retry failed records.
- **B.** Reduce the DynamoDB table auto scaling policy's target utilization to 50% to provide more resources for peak traffic periods.
- **C.** Use Application Auto Scaling to set a step scaling policy to scale out write capacity on the DynamoDB table when load spikes reach a defined threshold.
- **D.** Use Application Auto Scaling to scale out write capacity on the DynamoDB table based on a schedule.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** DynamoDB auto scaling 70% target, predictable spike up to 300%, ProvisionedThroughputExceeded, scheduled scaling

🪤 **Your trap:** Retrying the DLQ later does not stop throttling; and reactive target tracking or step scaling lags a sudden spike. Predictable spike needs capacity ready beforehand.

🧠 **Rule:** Predictable spike: Application Auto Scaling scheduled action scales ahead. Target tracking and step scaling react after the breach.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Lambda ──write──► DynamoDB (auto scaling, target 70%)
                    │
 Spike định kỳ, DỰ ĐOÁN ĐƯỢC, vượt tải thường tới 300%
 -> ProvisionedThroughputExceededException
 -> record rơi vào DLQ
```

Đáp án đúng: **D (scheduled scaling)**. Anh chọn A (retry DLQ bằng Lambda).

#### Vì sao D đúng

Nguyên nhân gốc: capacity ghi (WCU) **không đủ** khi spike. Từ khóa "short predictable periods" nghĩa là biết trước giờ spike, nên dùng **Application Auto Scaling scheduled action** để nâng capacity **trước** spike, hạ xuống sau đó. Đề giải thích: scheduled scaling bảo đảm capacity có sẵn trước khi tải tăng.

#### Vì sao A (anh chọn) sai

A là xử lý hậu quả (retry record trong DLQ), không xử lý nguyên nhân. Nếu tải chưa giảm, retry vẫn bị throttle lần nữa. Đề: "does not solve the original problem".

#### Các phương án còn lại

- **B. Giảm target utilization còn 50%:** auto scaling theo target tracking vẫn **phản ứng sau** khi metric vượt ngưỡng, nên spike nhanh vẫn có thể bị throttle trước khi scale xong. Còn tốn kém hơn vì luôn giữ dư capacity.
- **C. Step scaling:** vẫn là scaling **động**, chỉ chạy sau khi CloudWatch alarm breach, nên vẫn có thể lỗi trong lúc chờ.

| Cách | Thời điểm thêm capacity | Hợp với spike dự đoán được |
|---|---|---|
| **D. Scheduled** | **Trước** spike | Có |
| C. Step scaling | Sau alarm breach | Không, bị trễ |
| B. Target 50% | Sau khi vượt 50% | Không chắc, tốn hơn |
| A. Retry DLQ | Không đổi capacity | Không |

#### Lưu ý thực tế

- Lag của dynamic scaling đến từ việc phải có metric vượt ngưỡng và alarm; spike ngắn và dốc có thể xong trước khi kịp scale.
- On-demand capacity mode cũng là hướng khác cho tải khó đoán, nhưng đề đã cố định provisioned + auto scaling.

#### Quy tắc nhớ cho thi

- **Thấy "predictable" / "scheduled" / "every week..."** → **scheduled scaling**
- **Thấy "unpredictable"** → **target tracking / dynamic**
- **ProvisionedThroughputExceededException** → thiếu capacity, sửa **capacity**, không sửa client retry
- **Dynamic scaling** luôn có độ trễ; **scheduled** thì chủ động

### TD explanation

The error message received will include the following statement:
You exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes.
This indicates that the table’s capacity is insufficient for the load. The best way to resolve this for a predictable spike in traffic is to configure Application Auto Scaling to scale based on a defined schedule.
Scaling based on a schedule allows you to set your own scaling schedule for predictable load changes. For example, every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can configure Application Auto Scaling to increase capacity on Wednesday and decrease capacity on Friday.
CORRECT:
"Use Application Auto Scaling to scale out write capacity on the DynamoDB table based on a schedule" is the correct answer.
INCORRECT:
"Use Application Auto Scaling to set a step scaling policy to scale out write capacity on the DynamoDB table when load spikes reach a defined threshold" is incorrect. Step scaling is a dynamic scaling type that will scale when the load increases and scales according to the size of the alarm breach. However, this method must respond to alarm breaches and therefore may still result in errors. Scheduled scaling is preferable as it ensures the additional capacity is enabled before the increase in load occurs.
INCORRECT:
"Use Amazon CloudWatch Events to monitor the dead letter queue and invoke a Lambda function to automatically retry failed records" is incorrect. This does not solve the original problem and the records may still fail to be written if the load has not decreased.
INCORRECT:
"Reduce the DynamoDB table auto scaling policy's target utilization to 50% to provide more resources for peak traffic periods" is incorrect. This will still result in an alarm breach if the utilization goes above 50% and is less cost-effective.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

</details>

<a id="q22"></a>

## Q22

<!-- source: T6Q5 · domain: NEW -->



A company is planning to launch a new web application on AWS using a fully serverless design. The website will be used by global customers and should be highly responsive and offer minimal latency. The design should be highly availably and include baseline DDoS protections against spikes in traffic. The users will login in to the web application using social IdPs such as Google, and Amazon.
How can the design requirements be met?

- **A.** Build an API using Docker containers running on Amazon ECS behind an Amazon CloudFront distribution. Use AWS Secrets Manager to provide user management authentication functions.
- **B.** Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an Amazon CloudFront distribution with the S3 bucket as the origin. Use Amazon Cognito to provide user management authentication functions.
- **C.** Build an API using Docker containers running on AWS Fargate in multiple Regions behind Application Load Balancers. Use an Amazon Route 53 latency-based routing policy. Use Amazon Cognito to provide user management authentication functions.
- **D.** Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an AWS WAF Web ACL and attach it for DDoS attack mitigation. Use Amazon Cognito to provide user management authentication functions.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** serverless, global users, low latency, baseline DDoS, social IdP login, CloudFront S3 origin, Cognito

🪤 **Your trap:** 🔁 Picked WAF Web ACL for DDoS. WAF filters L7 rules; baseline DDoS comes free with CloudFront through Shield Standard, which also cuts latency by caching S3.

🧠 **Rule:** Global low latency plus baseline DDoS means CloudFront (Shield Standard included). WAF is for SQLi/XSS. Social IdP means Cognito.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users toàn cầu (login Google/Amazon)
   │
   ▼
CloudFront ──► S3 (static)
   │
   └──► API Gateway ──► Lambda
Auth: Cognito (social IdP)
Yêu cầu: serverless hoàn toàn, latency thấp, HA, baseline DDoS
```

Đáp án đúng: **B**. Anh chọn D.

#### Vì sao B đúng

- **API Gateway + Lambda + S3** → serverless, HA.
- **CloudFront** trước S3 → cache ở edge cho người dùng toàn cầu, giảm latency.
- **CloudFront đi kèm AWS Shield Standard** (miễn phí) → baseline DDoS protection.
- **Amazon Cognito** → user pool, liên kết social IdP (Google, Amazon...).

#### Vì sao D (anh chọn) sai

D đúng phần serverless và Cognito, nhưng bỏ CloudFront và dùng **AWS WAF Web ACL "for DDoS attack mitigation"**. Đề chỉ ra: WAF Web ACL không phải công cụ giảm thiểu DDoS baseline; dùng **AWS Shield**, hoặc CloudFront kết hợp WAF. Ngoài ra D thiếu CDN nên không giải quyết latency toàn cầu.

📝 **Ghi chú kỹ thuật:** Thực tế WAF có rate-based rule giúp chống một phần tấn công tầng 7, nên không hoàn toàn vô dụng. Nhưng trong đề, "baseline DDoS protections" = Shield Standard, đi sẵn với CloudFront. Giữ đáp án B.

#### Các phương án còn lại

- **A:** CloudFront không đặt trực tiếp trước ECS được, phải trỏ tới load balancer (theo đề). **Secrets Manager** lưu secret, không phải dịch vụ xác thực người dùng.
- **C:** Fargate nhiều Region + ALB + Route 53 latency routing là serverless nhưng kém tối ưu: tốn kém hơn, kém co giãn mượt hơn Lambda/API Gateway, và CloudFront rẻ hơn nhiều so với chạy nhiều Region.

| Phương án | Serverless | Edge/latency | DDoS baseline | Auth đúng |
|---|---|---|---|---|
| **B** | Có | CloudFront | Shield Standard | Cognito |
| D | Có | Không có CDN | WAF (sai mục đích) | Cognito |
| C | Có (Fargate) | Multi-Region đắt | Không nêu | Cognito |
| A | Không rõ | CloudFront nhưng sai origin | Có | Secrets Manager sai |

#### Quy tắc nhớ cho thi

- **"Baseline DDoS"** → **Shield Standard** (tự có với CloudFront, Route 53)
- **"Global + static content + low latency"** → **CloudFront + S3**
- **"Social IdP login"** → **Amazon Cognito**
- **Secrets Manager** = lưu secret, không phải auth người dùng
- **WAF** = lọc request (SQLi, XSS, rate), không phải đáp án cho DDoS baseline

#### 📝 Ghi chú kiểm định (10-26)
- Đáp án **B đúng**. Yếu tố quyết định là **độ trễ thấp toàn cầu** → cần **CloudFront** (đi kèm Shield Standard miễn phí). D không có CDN nên không đạt yêu cầu latency.
- Lời giải Neal nói "WAF không giúp chống DDoS" là **nói quá**: WAF rate-based rule vẫn giảm thiểu được flood tầng 7. D sai vì **thiếu CloudFront**, không phải vì WAF.

### TD explanation

A serverless web application can be created using a REST API running on API Gateway, a Lambda function, and S3 to store static assets. CloudFront can then be used to cache the S3 assets for lower latency for the global user base. CloudFront also offers basic DDoS protections with AWS Shield standard offered for free for use with CloudFront. Amazon Cognito is ideal for implementing user authentication for this type of application and you can integrate with social IdPs.
CORRECT:
"Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an Amazon CloudFront distribution with the S3 bucket as the origin. Use Amazon Cognito to provide user management authentication functions" is the correct answer.
INCORRECT:
"Build an API using Docker containers running on Amazon ECS behind an Amazon CloudFront distribution. Use AWS Secrets Manager to provide user management authentication functions" is incorrect. You cannot put CloudFront directly in front of ECS, you must point it to a load balancer. Secrets Manager is not an authentication service, it is used for securely storing secrets such as passwords.
INCORRECT:
"Build an API using Docker containers running on AWS Fargate in multiple Regions behind Application Load Balancers. Use an Amazon Route 53 latency-based routing policy. Use Amazon Cognito to provide user management authentication functions" is incorrect. This is a serverless design but it is not the best design. Using Lambda functions and API gateway will likely be more cost-effective and scale more seamlessly. Also CloudFront is a better way to get assets such as media files closer to users and cheaper than hosting the solution in many Regions.
INCORRECT:
"Build an API with API Gateway and AWS Lambda, use Amazon S3 for hosting static web resources and create an AWS WAF Web ACL and attach it for DDoS attack mitigation. Use Amazon Cognito to provide user management authentication functions" is incorrect. A WAF Web ACL will not provide DDoS attack mitigation, use AWS Shield instead or use CloudFront with WAF.
References:
https://aws.amazon.com/shield/
https://aws.amazon.com/serverless/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

</details>

<a id="q34"></a>

## Q34

<!-- source: T6Q16 · domain: NEW -->



An eCommerce application offers a membership program. Members of the program need to be able to download all files in a secured Amazon S3 bucket. The access should be restricted to members of the program and not available to anyone else. An Amazon CloudFront distribution has been created to deliver the content to users around the world.
What is the most efficient method a Solutions Architect should use to securely enable access to the files in the S3 bucket?

- **A.** Configure the application to generate a signed URL for authenticated users that provides time-limited access to the files.
- **B.** Configure the application to send Set-Cookie headers to the viewer and control access to the files using signed cookies.
- **C.** Use an Origin Access Identity (OAI) to control access to the S3 bucket to users of the CloudFront distribution only.
- **D.** Configure a behavior in CloudFront that forwards requests for the files to the S3 bucket based on a path pattern.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** membership, download all files in secured S3 bucket, CloudFront signed cookies vs signed URL

🪤 **Your trap:** Signed URL grants one file at a time; many files would need many URLs. Signed cookies cover multiple files without changing URLs.

🧠 **Rule:** One file or non-cookie clients: signed URL. Many restricted files, keep URLs: signed cookies. OAI/OAC only locks S3 to CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Thành viên ──► CloudFront ──► S3 (private)
                  ▲
          Ai được vào? -> chỉ member
Yêu cầu: tải TẤT CẢ file trong khu vực member, hiệu quả nhất
```

Đáp án đúng: **B (signed cookies)**. Anh chọn A (signed URL).

#### Vì sao B đúng

**Signed cookies** hợp khi:
- Muốn kiểm soát truy cập **nhiều file** (ví dụ cả khu subscribers).
- Không muốn đổi URL hiện có.

Cơ chế: app gửi ba header `Set-Cookie`; trình duyệt lưu và tự gắn vào mọi request sau; CloudFront kiểm tra cookie để cho vào. Một lần cấp, truy cập mọi file.

#### Vì sao A (anh chọn) sai

Signed URL vẫn bảo mật đúng, nhưng chỉ cấp quyền cho **một file / một URL**. Với "all files", phải sinh một signed URL cho từng file, kém hiệu quả. Đề hỏi "most efficient", nên signed cookies thắng.

#### Các phương án còn lại

- **C. OAI:** chỉ chặn truy cập trực tiếp vào S3, bắt buộc đi qua CloudFront. Nhưng không phân biệt **ai** trong người dùng CloudFront được vào, nên chưa đáp ứng "chỉ member".
- **D. Cache behavior theo path pattern:** chỉ định hướng request tới origin theo đường dẫn; không xác thực user.

| Phương án | Kiểm soát theo user? | Phạm vi |
|---|---|---|
| **B. Signed cookies** | Có | Nhiều file, giữ nguyên URL |
| A. Signed URL | Có | Từng file một |
| C. OAI | Không | Bucket chỉ cho CloudFront |
| D. Path pattern | Không | Chỉ định tuyến |

#### Lưu ý thực tế

- Trong thiết kế thật thường **kết hợp**: OAI (hoặc OAC) khóa S3 + signed cookies/URL khóa quyền người dùng.
- Signed URL vẫn đúng khi: client không hỗ trợ cookie (ví dụ RTMP trong tài liệu cũ), hoặc chia sẻ một file riêng lẻ.

#### Quy tắc nhớ cho thi

- **"Nhiều file / cả khu vực / giữ URL"** → **signed cookies**
- **"Một file riêng lẻ / client không hỗ trợ cookie"** → **signed URL**
- **OAI/OAC** = khóa S3 chỉ cho CloudFront, **không** xác thực người dùng
- **Path pattern** = định tuyến, không phải bảo mật

### TD explanation

CloudFront signed cookies allow you to control who can access your content when you don't want to change your current URLs or when you want to provide access to multiple restricted files, for example, all of the files in the subscribers' area of a website.
When using signed cookies the application sends three Set-Cookie headers to the viewer and the viewer stores the name-value pairs and adds them to the requests using a Cookie header. Access is then controlled in CloudFront based on the cookies.
CORRECT:
"Configure the application to send Set-Cookie headers to the viewer and control access to the files using signed cookies" is the correct answer.
INCORRECT:
"Configure the application to generate a signed URL for authenticated users that provides time-limited access to the files" is incorrect. A signed URL is for access to an individual file, for multiple files a signed URL would be required for each file. In this case the signed cookies approach is more efficient.
INCORRECT:
"Use an Origin Access Identity (OAI) to control access to the S3 bucket to users of the CloudFront distribution only" is incorrect. An OAI limits direct access to S3 to the CloudFront distribution only. In this case we also need a method to ensure that only the correct users of CloudFront are allowed access.
INCORRECT:
"Configure a behavior in CloudFront that forwards requests for the files to the S3 bucket based on a path pattern" is incorrect. A path pattern controls where to send requests based on path or file type. This doesn’t really assist here as it doesn’t secure based on the user requesting access.
References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-choosing-signed-urls-cookies.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q35"></a>

## Q35

<!-- source: T3Q15 · domain: NEW · flagged -->



A corporation needs to quickly enable 350 staff members to work remotely in the event of an emergency. Their current setup includes a mix of Windows and Linux desktops with various applications installed, such as office suites and communication tools.
The solution must integrate with the company's existing on-premises Active Directory, allowing staff to use their current login credentials. Additionally, it should support multifactor authentication (MFA) and closely replicate the user interface of their existing desktop environments.
Which AWS solution would best meet these criteria?

- **A.** Use Amazon WorkSpaces as the cloud-based desktop service. Establish a VPN connection to the on-premises network, set up an AD Connector to integrate with the on-premises Active Directory, and configure MFA for Amazon WorkSpaces via the AWS Management Console.
- **B.** Use Amazon AppStream 2.0 for streaming applications. Configure it with a desktop-like interface for employees. Establish a VPN connection to the on-premises network and use Active Directory Federation Services (AD FS) for integration. Connect the VPC to AD FS through the VPN.
- **C.** Use Amazon WorkSpaces for providing cloud desktops. Connect it to the on-premises network via VPN, integrate with the on-premises Active Directory using an AD Connector, and set up a RADIUS server to enable MFA.
- **D.** Use Amazon AppStream 2.0 for application streaming services. Integrate it with on-premises Active Directory Federation Services for identity management and configure MFA to control access on AppStream 2.0.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** 350 staff remote, Windows and Linux desktops, on-premises AD, MFA, WorkSpaces AD Connector RADIUS

🪤 **Your trap:** AppStream 2.0 streams applications, not full desktops that replicate the existing environment. WorkSpaces gives desktops; MFA with AD Connector needs RADIUS, not console toggle.

🧠 **Rule:** Full remote desktop plus on-prem AD: WorkSpaces + AD Connector + RADIUS MFA. AppStream 2.0 is app streaming only.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
350 nhân viên, khẩn cấp, làm việc từ xa
 Cần: desktop đầy đủ (Win/Linux), giống môi trường cũ
      dùng AD on-prem, hỗ trợ MFA
On-prem AD ──VPN──► VPC ──► Amazon WorkSpaces ?
```

Đáp án đúng: **C**. Anh chọn D (AppStream 2.0 + AD FS). Anh đánh dấu "không chắc".

#### Hai quyết định cần tách riêng

**1. WorkSpaces hay AppStream 2.0?** Đề cần "closely replicate the user interface of their existing desktop environments", tức **desktop đầy đủ**. **WorkSpaces** là DaaS cho desktop Windows/Linux. **AppStream 2.0** chuyên **stream ứng dụng**, nên đề cho là không tái tạo đầy đủ trải nghiệm desktop.

**2. MFA cho AD on-prem qua cách nào?** Với WorkSpaces dùng **AD Connector**, MFA bật bằng **RADIUS server** tích hợp vào AD Connector (kiểu MFA tương thích RADIUS), không bật thẳng trong console.

#### Vì sao C đúng

WorkSpaces + VPN + **AD Connector** (dùng credential AD hiện có) + **RADIUS** cho MFA. Đủ ba yêu cầu: desktop đầy đủ, AD on-prem, MFA.

#### Vì sao D (anh chọn) sai

D chọn AppStream 2.0 (đề cho là thiên về streaming ứng dụng) nên lệch yêu cầu desktop. Phần AD FS thì là cách federation hợp lệ cho AppStream, nhưng không cứu được lựa chọn dịch vụ.

#### Các phương án còn lại

- **A:** WorkSpaces + AD Connector đúng, nhưng "cấu hình MFA trong console" sai: MFA với AD on-prem đi qua **RADIUS**.
- **B:** AppStream 2.0 dạng desktop-like + AD FS qua VPN: vẫn là streaming ứng dụng.

| Phương án | Dịch vụ | MFA | Kết quả |
|---|---|---|---|
| **C** | WorkSpaces | RADIUS | Đúng |
| A | WorkSpaces | Console | Sai ở cơ chế MFA |
| B | AppStream 2.0 | AD FS | Sai dịch vụ |
| D | AppStream 2.0 | AD FS | Sai dịch vụ |

📝 **Ghi chú kỹ thuật:** AppStream 2.0 thật ra cũng có chế độ streaming desktop, nên lập luận "không thể tái tạo desktop" của đề hơi mạnh tay. Trong đề này, từ khóa "full desktop experience" và "Windows và Linux desktops" kéo về WorkSpaces. Giữ đáp án C. Chi tiết "RADIUS cho MFA" bám đúng giải thích của đề.

#### Quy tắc nhớ cho thi

- **"Full desktop / thay thế desktop vật lý"** → **WorkSpaces**
- **"Stream một vài ứng dụng"** → **AppStream 2.0**
- **WorkSpaces + AD on-prem + MFA** → **AD Connector + RADIUS**
- Thấy "bật MFA trong console" cho AD on-prem → nghi ngờ, thường là bẫy

### TD explanation

Amazon WorkSpaces is a managed, secure Desktop-as-a-Service (DaaS) solution that can easily scale to accommodate the needs of 350 employees. It supports both Windows and Linux desktops, ensuring a seamless transition for users.
The integration with on-premises Active Directory via an AD Connector allows employees to use their existing credentials. The use of a RADIUS server for MFA adds an extra layer of security, ensuring that the remote desktop experience is both secure and familiar to the users.
CORRECT:
"Use Amazon WorkSpaces for providing cloud desktops. Connect it to the on-premises network via VPN, integrate with the on-premises Active Directory using an AD Connector, and set up a RADIUS server to enable MFA" is the correct answer (as explained above.)
INCORRECT:
"Use Amazon WorkSpaces as the cloud-based desktop service. Establish a VPN connection to the on-premises network, set up an AD Connector to integrate with the on-premises Active Directory, and configure MFA for Amazon WorkSpaces via the AWS Management Console" is incorrect.
While Amazon WorkSpaces is a suitable solution, enabling MFA via an on-premises Active Directory is achieved by way of a RADIUS server rather than through enabling it directly in the AWS Management Console.
INCORRECT:
"Use Amazon AppStream 2.0 for streaming applications. Configure it with a desktop-like interface for employees. Establish a VPN connection to the on-premises network and use Active Directory Federation Services (AD FS) for integration. Connect the VPC to AD FS through the VPN" is incorrect.
Amazon AppStream 2.0 is more focused on application streaming rather than providing a full desktop experience. While it can be configured for a desktop-like interface, it might not fully replicate the existing desktop environment for all users.
INCORRECT:
"Use Amazon AppStream 2.0 for application streaming services. Integrate it with on-premises Active Directory Federation Services for identity management and configure MFA to control access on AppStream 2.0" is incorrect.
Choosing Amazon AppStream 2.0 primarily focuses on application streaming and may not provide the complete desktop experience that users are accustomed to. While it can integrate with AD FS for identity management, it might not offer the full desktop interface required in this scenario.
References:
https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-directory-services/

</details>

<a id="q37"></a>

## Q37

<!-- source: T6Q28 · domain: CI -->



An automotive company is using AWS CodeBuild for CI/CD pipelines where each CodeBuild project is directly mapped to an individual application. Many of these applications use large sets of marketing data which is hosted inside an Amazon S3 bucket.
This data is provided by files which are owned by another third-party agency. A few of these projects need the entire set of data while a few of them require just a subset of more relevant data.
As the number of CodeBuild projects grows, the company notices a significant increase in the time required for the pipeline to finish running. The company wants to optimize the pipeline and reduce the amount of time that the pipeline requires to finish running.
Which solution will meet these requirements?

- **A.** Create an S3 bucket for the pipeline. Configure S3 caching for the CodeBuild projects that are in the pipeline. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition.
- **B.** Create an S3 bucket for the pipeline. Configure the S3 bucket as a secondary source location for the CodeBuild projects. Update the build specifications of the CodeBuild projects. Add the S3 bucket and data file directory to the cache definition.
- **C.** Configure the cache of the CodeBuild projects as LOCAL_SOURCE_CACHE. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition.
- **D.** Create a new VPC for the CodeBuild projects. Create an Amazon Elastic File System (Amazon EFS) file system in the VPC. Configure the CodeBuild projects to run in the VPC. Mount the EFS file system at the location of the data file directory.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** CodeBuild many projects slow, large S3 dataset, S3 cache in buildspec, EFS in VPC

🪤 **Your trap:** Moving data to EFS in a new VPC is heavy rework. Vendor explanation is muddled (flagged); the intended fix is the lighter S3 cache of the data directory in buildspec.

🧠 **Rule:** CodeBuild slowed by repeated dependency or data downloads: add S3 cache to buildspec. Reach for EFS and VPC only for shared mounts.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhiều CodeBuild project ──► mỗi build tải lại bộ dữ liệu lớn từ S3
                                  (file thuộc agency bên thứ ba)
Số project tăng ──► pipeline chạy lâu
Yêu cầu: giảm thời gian pipeline
```

Đáp án đúng: **A (S3 caching, thêm thư mục data vào cache definition)**. Anh chọn D (EFS trong VPC mới).

> ⚠️ Giải thích gốc của đề mâu thuẫn (khen local cache nhưng chọn S3 cache). Giữ đáp án A, hiểu theo logic bên dưới.

#### Vì sao A đúng

**CodeBuild cache kiểu Amazon S3** lưu các thư mục khai báo trong `buildspec` (mục `cache: paths`) vào S3 bucket. Các build sau khôi phục cache thay vì tải lại. Cache S3 dùng chung giữa các build host khác nhau, hợp khi nhiều project/build chạy trên host khác nhau và cần dùng cùng bộ dữ liệu lớn.

#### Vì sao D (anh chọn) sai

EFS là file system dùng chung, mount được vào build. Nhưng chỉ đáng khi có nhu cầu **chia sẻ file system giữa nhiều instance** (đề: không nhắc). Phải dựng VPC mới, EFS và cấu hình CodeBuild chạy trong VPC, tốn công và không phải cách tối ưu build theo chủ đích của đề.

#### Các phương án còn lại

- **B:** thêm S3 làm **secondary source** là hợp khi source code và file ở nhiều nơi khác nhau; ở đây file cùng một nơi, nên không cần. Cũng không nên đưa "S3 bucket" vào cache definition.
- **C. LOCAL_SOURCE_CACHE:** chỉ cache **metadata Git** của source chính/phụ; build sau chỉ kéo phần thay đổi giữa các commit. Nếu project không dùng Git repo (GitHub, GitHub Enterprise, Bitbucket) thì tùy chọn này bị bỏ qua. Không cache file dữ liệu trong S3.

| Phương án | Cache cái gì | Phù hợp bộ data S3? |
|---|---|---|
| **A. S3 cache** | Thư mục khai báo trong buildspec | Có |
| C. LOCAL_SOURCE_CACHE | Git metadata | Không |
| B. Secondary source | Thêm nguồn | Không cần |
| D. EFS + VPC | File system dùng chung | Quá nặng, không cần |

📝 **Ghi chú kỹ thuật:** Mô tả "Local caching" ở đầu phần giải thích của đề không phải lý do chọn A. Local cache chỉ tồn tại trên build host trong thời gian giới hạn và hợp cho artifact trung gian lớn. Trong thực tế, local cache có 3 mode (source, Docker layer, custom). Phần dữ liệu từ S3 ở đây hợp với cache S3 vì đề muốn tái sử dụng giữa các project.

#### Quy tắc nhớ cho thi

- **"Giảm thời gian build do tải lại dữ liệu/dependency"** → **cache** trong buildspec (`cache: paths`)
- **Cache dùng chung giữa host/project** → **S3 cache**
- **LOCAL_SOURCE_CACHE** = chỉ Git metadata
- **Secondary source** = khi source nằm ở nhiều nơi
- **EFS** = chỉ khi cần file system chia sẻ giữa instance

### TD explanation

> ⚠️ Expl praises LOCAL cache then selects S3 cache; reasoning inconsistent, 'pipeline for the bucket' meaningless.

Local caching stores a cache on a build host. The cache is available to that build host only for a limited time and until another build is complete. For example, when you are dealing with large Java projects, compilation might take a long time. You can speed up subsequent builds by using local caching. This is a good option for large intermediate build artifacts because the cache is immediately available on the build host.
Since files are available in S3, it makes sense to create a pipeline for the bucket and then enable caching to reduce CodeBuild execution time.
CORRECT:
"Create an S3 bucket for the pipeline. Configure S3 caching for the CodeBuild projects that are in the pipeline. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition" is the correct answer (as explained above.)
INCORRECT:
"Create an S3 bucket for the pipeline. Configure the S3 bucket as a secondary source location for the CodeBuild projects. Update the build specifications of the CodeBuild projects. Add the S3 bucket and data file directory to the cache definition" is incorrect.
Since the question mentions that files are in the same location, there is no need to configure a secondary source location, this would have been correct if the source code and other files were at different locations.
INCORRECT:
"Configure the cache of the CodeBuild projects as LOCAL_SOURCE_CACHE. Update the build specifications of the CodeBuild projects. Add the data file directory to the cache definition" is incorrect.
As per the definition, LOCAL_SOURCE_CACHE caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored hence this is incorrect.
INCORRECT:
"Create a new VPC for the CodeBuild projects. Create an Amazon Elastic File System (Amazon EFS) file system in the VPC. Configure the CodeBuild projects to run in the VPC. Mount the EFS file system at the location of the data file directory" is incorrect.
The question doesn’t mention about file sharing across instances and hence this is not a correct use case for ECS.
References:
https://aws.amazon.com/blogs/devops/improve-build-performance-and-save-time-using-local-caching-in-aws-codebuild/
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-developer-tools/

</details>

<a id="q45"></a>

## Q45

<!-- source: T5Q14 · domain: CI -->



A fleet of EC2 instances generate a large quantity of data and store the data on an Amazon EFS file system. The EC2 instances also backup the data by uploading to an Amazon S3 bucket in another Region on a daily basis. Some S3 uploads have been failing and the storage costs have significantly increased.
The operations team has removed the failed uploads. How can a Solutions Architect configure the backup jobs to efficiently backup data to S3 while reducing storage costs?

- **A.** Use S3 Transfer Acceleration for the backup jobs. Use the Multi-Object Delete operation to remove the old uploads on a daily basis.
- **B.** Use multipart upload for the backup jobs. Create a lifecycle policy that archives data to Amazon S3 Glacier on a daily basis.
- **C.** Use S3 Transfer Acceleration for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating.
- **D.** Use multipart upload for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** EFS backups to S3 other Region, failed uploads cost, multipart upload, lifecycle abort incomplete

🪤 **Your trap:** Archiving to Glacier does not remove incomplete multipart parts, which still bill. Lifecycle rule to abort incomplete multipart uploads cleans them and stops new ones.

🧠 **Rule:** Growing S3 cost from failed large uploads: multipart upload plus lifecycle rule aborting incomplete multipart uploads. Archiving cannot clear hidden parts.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 ──(daily backup, Region A -> Region B)──► S3 bucket
         │
         └─ upload lớn bị fail giữa chừng
              └─ các PART đã upload vẫn nằm lại trong bucket
                   (không thấy khi list, nhưng VẪN tính phí storage)
```

Hai yêu cầu: (1) upload **hiệu quả** file lớn, (2) **giảm chi phí** do phần dở dang tích tụ. Đáp án đúng: **D (multipart upload + lifecycle rule cho incomplete multipart uploads)**. Anh chọn B.

#### Vì sao D đúng

- **Multipart upload**: chia object lớn thành nhiều part, upload song song, part nào lỗi thì chỉ retry part đó. Hợp file backup lớn.
- Nếu initiate mà không complete/abort, các part đã upload **ở lại và bị tính phí**, đồng thời **không hiện** khi list bucket. Đây chính là nguồn chi phí tăng.
- **Lifecycle rule "Delete incomplete multipart uploads"** (action `AbortIncompleteMultipartUpload`, đặt số ngày kể từ lúc initiate) tự dọn, chạy tự động, không cần người.

#### Anh chọn B - vì sao trượt

B đúng nửa đầu (multipart) nhưng sai nửa sau: **"archive sang Glacier mỗi ngày"**.

- Lifecycle transition chỉ áp dụng cho **object đã hoàn tất**. Part dở dang chưa phải object nên không được archive; nó vẫn tiếp tục tính phí.
- Archive nghĩa là **giữ** dữ liệu (trả phí Glacier), còn đề cần **xóa** phần hỏng. Neal: "failed uploads should not be archived, they should be deleted."
- Còn làm tăng phí: Glacier có thời gian lưu tối thiểu và chi phí retrieve.

#### Các phương án còn lại

- **A**: Transfer Acceleration chỉ tăng tốc đường truyền (edge location), không giải quyết phần dở dang. **Multi-Object Delete** là lệnh gọi thủ công, không tự động, và part dở dang không hiện trong list nên khó xóa đúng.
- **C**: Có lifecycle đúng nhưng dùng **Transfer Acceleration thay multipart**. TA không chia song song/retry theo part cho file lớn; không có multipart thì cũng không tạo ra "incomplete multipart upload" để dọn - nên cặp này không ăn khớp.

| Phương án | Upload hiệu quả | Dọn phần hỏng tự động |
|---|---|---|
| A. TA + Multi-Object Delete | Chỉ tăng tốc mạng | Không (thủ công) |
| B. Multipart + Glacier | Có | Không (archive, không xóa) |
| C. TA + lifecycle abort | Không chia part | Có |
| **D. Multipart + lifecycle abort** | **Có** | **Có** |

#### Lưu ý thực tế

- Multipart là **bắt buộc** với object > 5 GB (một PUT đơn tối đa 5 GB); AWS khuyến nghị dùng từ khoảng 100 MB trở lên.
- Lifecycle rule có thể lọc theo prefix/tag; rule abort này độc lập với rule transition/expiration của object hoàn tất.
- Có thể xem part dở dang bằng `ListMultipartUploads` hoặc S3 Storage Lens, vì list bucket thường không thấy.

#### Quy tắc nhớ cho thi

- **Thấy "storage cost tăng sau upload fail"** → **lifecycle: AbortIncompleteMultipartUpload**
- **Thấy "upload file lớn, song song, retry part"** → **multipart upload**
- **Thấy "failed/incomplete"** → **xóa**, không bao giờ archive
- **Thấy "Transfer Acceleration"** → chỉ là tăng tốc đường truyền tới S3 từ xa, không liên quan chi phí

### TD explanation

S3’s multipart upload feature accelerates the uploading of large objects by allowing you to split them up into logical parts that can be uploaded in parallel. If you initiate a multipart upload but never finish it, the in-progress upload occupies some storage space and will incur storage charges.
However, these uploads are not visible when you list the contents of a bucket. You can use a lifecycle rule to clean up incomplete multipart uploads which will reduce storage space.
The rule configuration can be seen in the image below:
CORRECT:
"Use multipart upload for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating" is the correct answer.
INCORRECT:
"Use S3 Transfer Acceleration for the backup jobs. Use the Multi-Object Delete operation to remove the old uploads on a daily basis" is incorrect. S3 transfer acceleration is for optimizing the speed of uploads, multipart upload is a better solution for running uploads of parts of objects in parallel. Using multi-object delete is not an automated process, it will be much better to use a lifecycle rule for efficiency.
INCORRECT:
"Use multipart upload for the backup jobs. Create a lifecycle policy that archives data to Amazon S3 Glacier on a daily basis" is incorrect. The failed uploads should not be archived, they should be deleted.
INCORRECT:
"Use S3 Transfer Acceleration for the backup jobs. Create a lifecycle policy for the incomplete multipart uploads on the S3 bucket to prevent new failed uploads from accumulating" is incorrect. As explained above for S3 transfer acceleration.
References:
https://aws.amazon.com/blogs/aws/s3-lifecycle-management-update-support-for-multipart-uploads-and-delete-markers/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-storage-sap/

</details>

---

# Group D — Misread stem or rushed (Q41, Q68-74): symptom or constraint overlooked (4)

<a id="q41"></a>

## Q41

<!-- source: T5Q23 · domain: CI -->



An application runs on a fleet of Amazon ECS instances and stores data in an Amazon S3 bucket. Until recently the application had been working well and then started to fail to upload objects to the S3 bucket. Server access logging has been enabled and 403 errors have been identified since the time of the fault. The ECS cluster has been setup according to best practices and no changes have been made to the S3 bucket policy or IAM roles used to access the bucket.
What is the most LIKELY cause of the failure?

- **A.** The ECS service in inaccessible.
- **B.** The ECS container instance IAM role was modified.
- **C.** The ECS tasks have insufficient memory assigned.
- **D.** The ECS task IAM role was modified.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** ECS app stopped uploading to S3, 403 errors, no policy changes, task role vs container instance role

🪤 **Your trap:** Picked insufficient memory; memory causes OOM or throttling, not 403. A 403 is authorization; best practice puts S3 permissions in the task role, so it was modified.

🧠 **Rule:** 403 means access denied: check the role the code runs under. On ECS that is the task role, not the instance role.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ECS tasks ──PutObject──► S3 bucket
  ► trước đó chạy tốt, giờ lỗi
  ► Server access log: HTTP 403
  ► bucket policy + IAM role: "không đổi"
  ► cluster theo best practice
```

Đáp án đúng: **D (ECS task IAM role bị sửa)**. Anh chọn C (thiếu memory).

#### Cách suy luận từ mã lỗi

**403 = Access Denied**, lỗi **authorization**. Khi thấy 403, loại ngay mọi nguyên nhân về tài nguyên (memory, CPU, service unavailable) và tìm nguyên nhân về quyền.

#### Vì sao D đúng

Theo best practice, quyền cho container nằm ở **task IAM role** (không phải role của container instance). Task role bị sửa (mất quyền S3) thì request lên S3 bị 403.

#### Vì sao C (anh chọn) sai

Thiếu memory làm task bị kill (OOM) hoặc không chạy, tức lỗi ở phía ECS/ứng dụng. Nó không tạo ra phản hồi **403 từ S3**. Log S3 ghi 403 nghĩa là request đã **tới được** S3 và bị từ chối.

📝 **Ghi chú kỹ thuật:** Đề nói "no changes made to ... IAM roles used to access the bucket" nhưng đáp án lại là task role bị sửa. Hai câu mâu thuẫn nhẹ; cách hiểu để làm bài: role gắn ở bucket/phía S3 không đổi, còn role gắn cho task bị đổi. Giữ đáp án D.

#### Các phương án còn lại

- **A. ECS service inaccessible:** không gây lỗi access denied từ S3.
- **B. Container instance role bị sửa:** best practice là quyền S3 nằm ở **task role**, không ở instance role, nên đổi instance role không ảnh hưởng quyền S3 của task.

| Phương án | Gây 403 từ S3? | Lý do |
|---|---|---|
| **D. Task role sửa** | Có | Task mất quyền S3 |
| B. Instance role sửa | Không | Quyền S3 không đặt ở đây (best practice) |
| C. Thiếu memory | Không | Lỗi tài nguyên, không phải authorization |
| A. Service không truy cập được | Không | Không liên quan authorization |

#### Lưu ý thực tế

- Task role (`taskRoleArn`) khác **task execution role** (kéo image, đẩy log); app gọi S3 dùng task role.
- Điều tra 403 trên S3: kiểm tra IAM policy, bucket policy, explicit Deny, SCP, mã hóa KMS.

#### Quy tắc nhớ cho thi

- **403 / Access Denied** → **IAM / policy**, không phải memory/network
- **ECS container gọi AWS service** → **task IAM role**
- **Instance role** ở ECS cho agent/EC2; không đặt quyền ứng dụng ở đó
- **Memory/CPU** → task bị kill hoặc pending, không phải 403

#### 📝 Ghi chú kiểm định (10-26)
- **Đề tự mâu thuẫn**: đề nói "không thay đổi IAM role dùng để truy cập bucket" nhưng đáp án lại là "ECS task role bị sửa". Kiểm định độc lập cũng đánh dấu câu này.
- Bài học vẫn đúng: **403 = lỗi phân quyền (authorization)**, không bao giờ do thiếu bộ nhớ. Theo best practice, quyền S3 của container nằm ở **ECS task role**, nên đây là chỗ cần kiểm tra đầu tiên.

### TD explanation

A 403 error is an access denied error. Therefore, there must be an issue relating to authorization to access the S3 bucket. In this scenario the bucket policy and IAM roles have not been modified. The next thing to check is that the IAM role is correctly assigned to the ECS tasks.
The most likely cause of this issue is that the ECS task role has been changed and the tasks no longer have the permissions to access S3.
CORRECT:
"The ECS task IAM role was modified" is the correct answer.
INCORRECT:
"The ECS container instance IAM role was modified" is incorrect. According to best practice the permissions that containers (tasks) require should be specified in task IAM roles not in container instance IAM roles. As the cluster has been setup according to best practice the permissions to S3 should not be specified in the container instance IAM role.
INCORRECT:
"The ECS service in inaccessible" is incorrect. This would not result in an access denied error.
INCORRECT:
"The ECS tasks have insufficient memory assigned" is incorrect. This would not result in an access denied error.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/s3-troubleshoot-403/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/

</details>

<a id="q68"></a>

## Q68

<!-- source: T5Q11 · domain: CI -->



A security team has discovered that developers have been storing IAM secret access keys in AWS CodeCommit repositories. The security team requires that measures are put in place to automatically find and remediate all instances of this vulnerability on an ongoing basis.
Which solution meets these requirements?

- **A.** Create an Amazon Macie job that scans AWS CodeCommit repositories for credentials. If any credentials are found an AWS Lambda function should be triggered that disables the credentials.
- **B.** Use AWS Trusted Advisor to check for unsecured AWS credentials. If any unsecured credentials are found, use AWS Secrets Manager to rotate the credentials.
- **C.** Run a cron job on an Amazon EC2 instance to check the CodeCommit repositories for unsecured credentials. If any unsecured credentials are found, generate new credentials and store them in AWS KMS.
- **D.** Configure a CodeCommit trigger to invoke an AWS Lambda function to scan new code submissions for credentials. If any credentials are found, disable them and notify the user.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** IAM secret keys in CodeCommit, find and remediate ongoing, CodeCommit trigger Lambda

🪤 **Your trap:** Trusted Advisor and Secrets Manager do not scan repository contents; Macie scans S3, not CodeCommit. Pick needed an event-driven scan of pushes. Vendor notes it covers only new pushes.

🧠 **Rule:** Scan code on commit: CodeCommit trigger to Lambda. Macie is S3-only, Trusted Advisor does not read repos, rotation does not find keys.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Developer ──git push──► CodeCommit repo ──► (trigger) ──► Lambda scan
                                                              │
                                      tìm thấy access key ──► disable key + notify user
```

Yêu cầu: **tự động** tìm và xử lý **liên tục** việc lộ IAM secret access key trong CodeCommit. Đáp án đúng: **D**. Anh chọn B.

#### Vì sao D đúng

- CodeCommit hỗ trợ **trigger** (tối đa 10 trigger mỗi repo) gọi **Lambda** hoặc SNS khi có push/sự kiện.
- Lambda quét code mới (pattern access key), nếu có thì **disable key** (IAM `UpdateAccessKey` Inactive) và **thông báo** người đẩy code.
- Chạy theo sự kiện, serverless, không tốn chi phí khi không có push → đúng "automatically, on an ongoing basis".

#### Anh chọn B - vì sao trượt

B: **Trusted Advisor** phát hiện, **Secrets Manager** rotate.

- Check "Exposed Access Keys" của Trusted Advisor quét các **kho công khai** (như repo public) và log hoạt động bất thường, **không đọc repo private CodeCommit** của anh.
- Secrets Manager dùng để **lưu và rotate secret** có sẵn kiểu (database...). Với IAM user access key, không có rotation tích hợp sẵn; muốn làm phải tự viết Lambda. Neal: "Secrets Manager cannot be used for rotating secret access keys." Quan trọng hơn, rotate khác với **phản ứng khi bị lộ** trong repo.

#### Các phương án còn lại

- **A**: **Macie** quét dữ liệu trong **S3**. Bucket của CodeCommit do AWS quản lý, anh không trỏ Macie vào được.
- **C**: Cron trên **EC2** - tốn công vận hành (máy chủ chạy 24/7), trái "automatic, least overhead"; và **KMS lưu khóa mã hóa**, không lưu secret access key.

| Phương án | Nhìn thấy repo CodeCommit | Phản ứng tự động | Vận hành |
|---|---|---|---|
| A. Macie | Không (chỉ S3) | Có | Thấp |
| B. Trusted Advisor + Secrets Manager | Không (repo public) | Không | Thấp |
| C. EC2 cron | Có | Tự viết | Cao |
| **D. CodeCommit trigger + Lambda** | **Có** | **Có** | **Thấp** |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật (audit):** Đáp án D chỉ quét **push mới**, không quét lịch sử/key **đã có** trong repo. Thực tế cần thêm bước quét lại toàn bộ repo một lần. Ngoài ra CodeCommit từng ngừng nhận khách hàng mới (2024) và được nói là mở lại cuối 2025 - cần kiểm chứng trước khi dựa vào nó; trên đề thi vẫn chọn D.

- Phòng ngừa tốt hơn là chặn từ phía developer (công cụ như `git-secrets` dùng làm pre-commit hook).
- Key đã lộ thì phải coi là **đã bị lộ**: disable/rotate và xem CloudTrail xem có bị dùng chưa.

#### Quy tắc nhớ cho thi

- **Thấy "CodeCommit + phản ứng khi push"** → **trigger → Lambda**
- **Macie** = dữ liệu nhạy cảm trong **S3**
- **Trusted Advisor exposed keys** = repo công khai, không phải CodeCommit
- **KMS** = khóa mã hóa; **Secrets Manager** = secret; đừng lẫn với IAM access key

### TD explanation

> ⚠️ Relies on CodeCommit (closed to new customers 2024; reportedly reopened late 2025, verify); trigger only scans new pushes, not existing keys.

You can configure a CodeCommit repository so that code pushes or other events trigger actions, such as sending a notification from Amazon Simple Notification Service (Amazon SNS) or invoking a function in AWS Lambda. You can create up to 10 triggers for each CodeCommit repository. In this case you can trigger AWS Lambda to scan the code for access keys
CORRECT:
"Configure a CodeCommit trigger to invoke an AWS Lambda function to scan new code submissions for credentials. If any credentials are found, disable them and notify the user" is correct.
INCORRECT:
"Create an Amazon Macie job that scans AWS CodeCommit repositories for credentials. If any credentials are found an AWS Lambda function should be triggered that disables the credentials" is incorrect. Macie scans Amazon S3 buckets but you cannot see the S3 bucket assigned to CodeCommit as it’s an AWS managed service bucket.
INCORRECT:
"Use AWS Trusted Advisor to check for unsecured AWS credentials. If any unsecured credentials are found, use AWS Secrets Manager to rotate the credentials" is incorrect. Secrets Manager cannot be used for rotating secret access keys.
INCORRECT:
"Run a cron job on an Amazon EC2 instance to check the CodeCommit repositories for unsecured credentials. If any unsecured credentials are found, generate new credentials and store them in AWS KMS" is incorrect. EC2 is not a very cost-effective option for running this task and KMS is used for storing encryption keys, not secret access keys.
References:
https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

</details>

<a id="q70"></a>

## Q70

<!-- source: T6Q27 · domain: CI · flagged -->



A company hosts a business-critical monolithic application on an Amazon EC2 instance which is installed on an instance launched from an Amazon Linux 2 AMI. The company requires that the data on the attached EBS volumes must be backed up to a specific Amazon S3 bucket managed by the company.
The security team has mandated against owning any SSH keys for instances, so the operations team are unable to SSH into the instance.
Which solution will meet these requirements with the least impact on the critical application?

- **A.** Attach an IAM role to the instance with permissions to write to Amazon S3. Use the AWS Systems Manager Session Manager to gain access to the instance and run commands to copy data into Amazon S3.
- **B.** Create an image of the instance with the reboot option turned on. Launch a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3.
- **C.** Take a snapshot of the EBS volume by using Amazon Data Lifecycle Manager (Amazon DLM). Use the EBS direct APIs to copy the data from the snapshot to Amazon S3.
- **D.** Create a new AMI image from the current EC2 instance and spin up a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** EC2 critical app, EBS backup to S3, no SSH keys, least impact, DLM snapshot, EBS direct APIs

🪤 **Your trap:** Session Manager copying data from the live instance loads the critical app. Snapshot plus EBS direct APIs reads data off-instance with least impact.

🧠 **Rule:** Least impact on the running instance: snapshot then read via EBS direct APIs. Avoid copying from the live host.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 (AL2, app business-critical)
  └─ EBS volume(s)  ──► backup vào S3 bucket CỦA CÔNG TY
Ràng buộc: không SSH key
Câu hỏi:   ÍT ẢNH HƯỞNG NHẤT lên ứng dụng
```

Đáp án đúng: **C** (DLM snapshot + EBS direct APIs). Anh chọn A (Session Manager rồi copy). Câu này làm trong những phút cuối nên dễ chọn "cách quen thuộc".

#### Vì sao C đúng

- **Data Lifecycle Manager (DLM)** tạo EBS snapshot theo policy, **không cần đăng nhập** vào instance, không dừng app.
- Snapshot thực chất nằm trong S3 do AWS quản lý, anh **không** chỉ định bucket riêng được. Muốn dữ liệu vào **bucket của công ty** thì dùng **EBS direct APIs** (`ListSnapshotBlocks`, `GetSnapshotBlock`, `ListChangedBlocks`) đọc block từ snapshot rồi ghi vào S3.
- Phần đọc/ghi chạy **ngoài** instance gốc (ở máy/Lambda khác) → instance production không bị tải thêm.

#### Anh chọn A - vì sao trượt

A nhìn có vẻ hợp lệ: Session Manager **không cần SSH key**, đáp ứng ràng buộc bảo mật. Nhưng trượt ở "ít ảnh hưởng nhất":

- Lệnh copy chạy **trên chính instance production** → tốn CPU, I/O đĩa, băng thông của app business-critical.
- Copy file từ filesystem đang ghi có thể không nhất quán (không point-in-time như snapshot).
- Là thao tác **thủ công** trên máy quan trọng. Neal: "Running manual commands on a business-critical instance isn't recommended."

#### Các phương án còn lại

- **B**: Tạo image **với reboot** → app bị reboot, mất availability. Đây là điểm loại rõ nhất.
- **D**: Tạo AMI rồi dựng instance mới chỉ để copy dữ liệu: nhiều bước thừa; DLM + snapshot đã làm gọn hơn. Lưu ý AMI mặc định cũng có thể reboot instance nếu không đặt `NoReboot`.

| Phương án | Chạm instance production | Ghi vào bucket công ty | Nhận xét |
|---|---|---|---|
| A. Session Manager + copy | Có (tải I/O) | Có | Thủ công, ảnh hưởng |
| B. Image có reboot | Có (reboot) | Qua instance mới | Mất availability |
| **C. DLM + EBS direct APIs** | **Không** | **Có** | **Ít ảnh hưởng** |
| D. AMI + instance mới | Có thể (reboot mặc định) | Qua instance mới | Thừa bước |

#### Lưu ý thực tế

- EBS snapshot **incremental** và nhất quán ở mức crash-consistent; app cần nhất quán ứng dụng thì cân nhắc quiesce, nhưng không thuộc phạm vi đề.
- Direct APIs hữu ích khi cần đọc dữ liệu snapshot mà **không gắn volume**.

#### Quy tắc nhớ cho thi

- **Thấy "least impact on critical app"** → làm việc **ngoài** instance (snapshot), không chạy lệnh trên nó
- **Thấy "backup EBS vào bucket S3 riêng"** → **snapshot + EBS direct APIs**
- **Thấy "automate snapshot"** → **DLM**
- **Thấy "no SSH"** → Session Manager vẫn được, nhưng không tự động là đáp án nếu có điều kiện khác (ảnh hưởng, tự động)
- **Create image mặc định có thể reboot** → loại khi đề cấm downtime

### TD explanation

Amazon Data Lifecycle Manager provides an automated, policy-based lifecycle management solution for Amazon Elastic Block Store (EBS) Snapshots and EBS-backed Amazon Machine Images (AMIs). Automate the creation of point-in-time copy of your block storage data with user-defined policies that you can customize based on data protection needs. Amazon Data Lifecycle Manager requires no scripting or special training.
You can use the Amazon Elastic Block Store (Amazon EBS) direct APIs to create EBS snapshots, write data directly to your snapshots, read data on your snapshots, and identify the differences or changes between two snapshots. These APIs can be used to read the data from the snapshot and copy the data to Amazon S3.
CORRECT:
"Take a snapshot of the EBS volume by using Amazon Data Lifecycle Manager (Amazon DLM). Use the EBS direct APIs to copy the data from the snapshot to Amazon S3" is the correct answer (as explained above).
INCORRECT:
"Attach an IAM role to the instance with permissions to write to Amazon S3. Use the AWS Systems Manager Session Manager to gain access to the instance and run commands to copy data into Amazon S3" is incorrect.
Running manual commands on a business-critical instance isn't recommended and DLM can safely take the snapshot without needing to log in to the instance in any way.
INCORRECT:
"Create an image of the instance with the reboot option turned on. Launch a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3" is incorrect.
The reboot option will cause the business-critical application to be rebooted which has an impact on availability.
INCORRECT:
"Create a new AMI image from the current EC2 instance and spin up a new EC2 instance from the image. Attach a role to the new instance with permission to write to Amazon S3. Run a command to copy data into Amazon S3" is incorrect.
This is unnecessary as DLM can safely take a backup of the EBS volume using a snapshot.
References:
https://aws.amazon.com/blogs/storage/automating-amazon-ebs-snapshots-management-using-data-lifecycle-manager/
https://aws.amazon.com/ebs/data-lifecycle-manager/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-ebs/

</details>

<a id="q74"></a>

## Q74

<!-- source: T5Q10 · domain: CI · flagged -->



A company uses an AWS account with resources deployed in multiple Regions globally. Operations teams deploy and manage resources within each Region. Some Region-specific service quotas have been reached causing an inability for the local operations teams to deploy resources. A centralized cloud team is responsible for monitoring and updating service quotas. The cloud team needs to create an automated and operationally efficient solution to proactively monitor service quotas. Monitoring should occur every 15 minutes and send alerts when a team exceeds 80% utilization.
Which solution will meet these requirements?

- **A.** Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the GetServiceQuota API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team.
- **B.** Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the ListServiceQuotas API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team.
- **C.** Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, use AWS Budgets to send an alert to the cloud team.
- **D.** Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** service quotas every 15 minutes, 80% utilization alert, Trusted Advisor, Lambda, SNS

🪤 **Your trap:** 🔁 Chose Budgets for the alert; Budgets tracks cost and usage spend, not quota utilization. Alert should publish to SNS. Vendor flags native Usage alarms as modern route.

🧠 **Rule:** Quota alerts: SNS notification (or CloudWatch alarm on AWS/Usage with SERVICE_QUOTA()). Budgets cost-tracks, never quotas.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhiều Region ─► service quota bị chạm ─► ops team không deploy được
Cloud team cần: tự động, mỗi 15 phút, cảnh báo khi dùng > 80%
```

Đáp án đúng: **D** (EventBridge schedule → Lambda → Trusted Advisor → **SNS**). Anh chọn C. Câu này làm gấp, hai phương án cuối khác nhau ở **một cụm cuối câu**.

#### Vì sao D đúng

```
EventBridge rule (rate 15 phút)
      └─► Lambda ─► Trusted Advisor (check Service Limits: usage vs quota)
                         └─ nếu > 80% ─► publish SNS ─► cloud team
```

- **EventBridge** chạy theo lịch (mỗi 15 phút).
- **Trusted Advisor** có check về service limits, trả về **mức sử dụng so với quota**.
- **SNS** là dịch vụ **gửi thông báo** (email/SMS/HTTP...).

#### Anh chọn C - vì sao trượt

C giống D hoàn toàn, chỉ khác bước cuối: **AWS Budgets** để gửi alert.

- **Budgets** theo dõi **chi phí/usage mức dùng của hóa đơn**, không phải kênh nhắn tin để Lambda đẩy cảnh báo về quota. Neal: "not a messaging service for alerting."
- Alert của Budgets gắn vào ngưỡng ngân sách đã tạo, không "publish một message" tùy ý từ Lambda.

#### Các phương án còn lại (A, B)

- **A** `GetServiceQuota` và **B** `ListServiceQuotas`: các API này trả về **giá trị quota** (hạn mức), **không trả mức đã dùng**. Không tính được 80% utilization.
- Dùng **scheduled AWS Config rule** cũng là công cụ không đúng việc: Config đánh giá cấu hình tài nguyên, không phải bộ lập lịch quota.

| Phương án | Lấy được "utilization" | Gửi alert đúng kênh |
|---|---|---|
| A. Config + GetServiceQuota | Không (chỉ quota) | SNS |
| B. Config + ListServiceQuotas | Không (chỉ quota) | SNS |
| C. EventBridge + TA + Budgets | Có | **Sai (Budgets)** |
| **D. EventBridge + TA + SNS** | **Có** | **SNS** |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** Cách của đề là lối cũ. Hiện nay **Service Quotas** tích hợp **CloudWatch**: bật usage metric (namespace `AWS/Usage`) và đặt **CloudWatch alarm** khi dùng vượt ngưỡng (ví dụ 80%), có thể đặt per-Region và gửi qua SNS - đơn giản hơn tự viết Lambda. Trong đề này D vẫn là đáp án tốt nhất trong các lựa chọn.

- Trusted Advisor đầy đủ check (và dùng được qua API) cần gói **Business/Enterprise Support**.
- Quota là **per-Region**, nên cần giám sát từng Region đang dùng.

#### Quy tắc nhớ cho thi

- **Thấy "service quota utilization > x%"** → **Trusted Advisor** (đề cũ) hoặc **Service Quotas + CloudWatch alarm** (hiện đại)
- **`GetServiceQuota` / `ListServiceQuotas`** → chỉ cho **hạn mức**, không cho mức đã dùng
- **Cảnh báo/ thông báo** → **SNS**; **Budgets** chỉ cho chi phí
- **Hai option giống nhau** → so cụm khác biệt cuối câu

#### 📝 Ghi chú kiểm định (10-26)
- Đáp án **D là tốt nhất trong các lựa chọn**, nhưng cách hiện đại là **Service Quotas + CloudWatch alarm trên metric `AWS/Usage`** (không có trong đáp án).
- Loại A/B: **AWS Config periodic rule chạy tối thiểu 1 giờ** (không đạt 15 phút), và GetServiceQuota/ListServiceQuotas chỉ trả về **giới hạn**, không trả **mức sử dụng**. Loại C: **Budgets theo dõi chi phí, không theo dõi quota**.
- Lưu ý: Trusted Advisor API cần gói Business/Enterprise Support.

### TD explanation

> ⚠️ Dated approach; now Service Quotas native CloudWatch usage alarms. Answer D still best of options.

Amazon EventBridge (formerly Amazon CloudWatch Events) can be used to run a function on a schedule. The function can retrieve the most current utilization and service limit data. The function can then trigger an SNS topic if the utilization is above 80%. This solution meets all requirements.
CORRECT:
"Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team" is the correct answer.
INCORRECT:
"Create an Amazon EventBridge rule that triggers an AWS Lambda function to use AWS Trusted Advisor to retrieve the most current utilization and service limit data. If the current utilization is above 80%, use AWS Budgets to send an alert to the cloud team" is incorrect.
AWS Budgets is used for tracking and alerting on spend on your AWS account, it is not a messaging service for alerting.
INCORRECT:
"Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the GetServiceQuota API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team" is incorrect.
The GetServiceQuota API will simply list the current quota, it does not return data showing how much of that quota has been utilized.
INCORRECT:
"Create a scheduled AWS Config rule to trigger an AWS Lambda function to call the ListServiceQuotas API. If any service utilization is above 80%, publish a message to an Amazon SNS topic to alert the cloud team" is incorrect.
The ListServiceQuotas API lists the service quota applied to a specific service. It also does not return data showing how much of that quota has been utilized.
References:
https://docs.aws.amazon.com/awssupport/latest/user/trustedadvisor.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

</details>
