# Udemy Practice Test #2 — full timed, 75 questions (2026-10-28) — Wrong Answer Review (14 questions)

Source: `sap-udemy2-full-2026-10-281130-results.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `udemy2_full_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q11](#q11) | ✅ 10-29 | ☐ | ☐ |
| A | [Q33](#q33) | ✅ 10-29 | ☐ | ☐ |
| A | [Q45](#q45) | ✅ 10-29 | ☐ | ☐ |
| A | [Q54](#q54) | ✅ 10-29 | ☐ | ☐ |
| B | [Q13](#q13) | ✅ 10-29 | ☐ | ☐ |
| B | [Q24](#q24) | ✅ 10-29 | ☐ | ☐ |
| B | [Q25](#q25) | ✅ 10-29 | ☐ | ☐ |
| B | [Q46](#q46) | ✅ 10-29 | ☐ | ☐ |
| B | [Q59](#q59) | ✅ 10-29 | ☐ | ☐ |
| B | [Q63](#q63) | ✅ 10-29 | ☐ | ☐ |
| C | [Q19](#q19) | ✅ 10-29 | ☐ | ☐ |
| C | [Q65](#q65) | ✅ 10-29 | ☐ | ☐ |
| C | [Q67](#q67) | ✅ 10-29 | ☐ | ☐ |
| C | [Q68](#q68) | ✅ 10-29 | ☐ | ☐ |

---

# Group A — Service fact or limit not known cold (IOPS math, KMS Region scope, Firehose targets, DB engine facts) (4)

<a id="q11"></a>

## Q11

<!-- source: U2Q68 · domain: CI · flagged · time: 4:06 · first: 4:26 · visits: 2 · changes: 1 -->



The engineering team at a data analytics company is currently optimizing a production workload on AWS that is I/O intensive with frequent read/write/update operations and it's currently constrained on the IOPS. This workload consists of a single-tier with 15 r6g.8xlarge instances, each with 3 TB gp2 volume. The number of processing jobs has increased recently, resulting in an increase in latency as well. The team has concluded that they need to increase the IOPS by 3,000 for each of the instances for the application to perform efficiently.

As an AWS Certified Solutions Architect Professional, which of the following solutions will you suggest to meet the performance goal in the MOST cost-efficient way?

- **A.** Provision a new EFS file system and migrate all the data to this new file system. Mount this file system on all 15 instances
- **B.** Modify the size of the gp2 volume for each instance from 3 TB to 4 TB
- **C.** Set up a new Amazon S3 bucket and migrate all the data to this new bucket. Configure each instance to access this S3 bucket and use it for storage
- **D.** Modify the type of Amazon EBS volume on each instance from gp2 to io1 and set provisioned IOPS to 12,000

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** gp2 3 TB, need +3,000 IOPS per instance, MOST cost-efficient, EBS vs EFS vs io1

🪤 **Your trap:** Changed the right answer (grow gp2) to EFS during review. EFS is shared network storage, slower per op for random I/O and costs more per GB; it adds no IOPS guarantee. Review change had no new evidence.

🧠 **Rule:** gp2 baseline = 3 IOPS per GiB (max 16,000). +1 TB = +3,000 IOPS; growing gp2 (or moving to gp3) beats io1 on cost.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
15 x r6g.8xlarge  ──►  mỗi máy 1 volume gp2 3 TB
                        Workload I/O nặng, thiếu IOPS
                        Cần: +3,000 IOPS / instance
                        Ràng buộc: MOST cost-efficient
```

Đáp án đúng: **B (tăng gp2 từ 3 TB lên 4 TB)**. Anh chọn A (EFS). Ban đầu Anh đã chọn đúng B, rồi đổi sang A trong lúc review cờ flag.

#### Vì sao B đúng

gp2 có baseline IOPS **tỷ lệ tuyến tính với dung lượng**: **3 IOPS mỗi GiB**, tối thiểu 100 IOPS, tối đa 16,000 IOPS (đạt ở 5,334 GiB trở lên).

```
Thêm 1 TB (~1,000 GiB) x 3 IOPS/GiB = +3,000 IOPS
3 TB -> 4 TB  =>  đúng mục tiêu +3,000 IOPS
Không đổi loại volume, không đổi kiến trúc, không migrate data
```

Elastic Volumes cho phép tăng size volume đang gắn, không cần detach. Sau khi tăng, cần mở rộng file system trong OS. Chi phí chỉ là thêm 1 TB gp2 cho mỗi máy.

#### Phương án Anh chọn (A, EFS) sai ở đâu

A trông "hiện đại" vì EFS là storage dùng chung, mount được cho cả 15 máy. Nhưng:

- EFS là **network file system (NFS)**, không phải block storage. Workload cần read/write/update ngẫu nhiên, độ trễ thấp, nên hợp với EBS hơn.
- Theo Udemy, EFS đắt khoảng **3 lần** gp2 tính theo GB-tháng.
- Phải migrate toàn bộ data, đổi cách mount, đổi kiến trúc. Rủi ro cao mà không giải quyết đúng yêu cầu "thêm 3,000 IOPS".

#### Các phương án còn lại

- **C (S3):** S3 là object storage, không hỗ trợ read/write/update ngẫu nhiên kiểu block. Không phù hợp workload IOPS cao.
- **D (io1, 12,000 IOPS):** đạt được hiệu năng (gp2 4 TB cũng ra khoảng 12,000 IOPS) nhưng io1 đắt hơn: giá GB cao hơn gp2 ít nhất 25% (theo Udemy) và còn tính thêm tiền cho IOPS đã provision. Vì đề hỏi MOST cost-efficient nên loại.

| Phương án | Đạt +3,000 IOPS | Chi phí | Công sức thay đổi |
|---|---|---|---|
| **B. gp2 +1 TB** | Có (3 IOPS/GiB) | Thấp nhất | Rất ít (Elastic Volumes) |
| D. io1 12,000 IOPS | Có | Cao hơn (GB + IOPS) | Đổi loại volume |
| A. EFS | Không đảm bảo | Cao (~3x gp2/GB) | Migrate toàn bộ |
| C. S3 | Không | Rẻ nhưng sai loại | Viết lại ứng dụng |

#### Bài học về review

Anh có đáp án đúng ngay từ đầu rồi tự đổi mà **không có thông tin mới**. Khi review câu đã flag, chỉ đổi đáp án nếu:

- Anh tìm ra một **từ khóa/ràng buộc đã bỏ sót** trong đề, hoặc
- Anh nhớ ra một **fact cụ thể** chứng minh đáp án cũ sai.

Nếu chỉ là cảm giác "phương án kia nghe xịn hơn" thì giữ nguyên đáp án đầu. Ở đây không có bằng chứng nào cho thấy EFS đáp ứng đề tốt hơn.

#### Lưu ý thực tế

- **gp3** (không có trong các lựa chọn) có baseline 3,000 IOPS không phụ thuộc dung lượng, có thể provision tới 16,000 IOPS, giá GB thấp hơn gp2. Ngoài đời đây thường là hướng tối ưu, nhưng khi đề chỉ cho gp2/io1 thì chọn "tăng size gp2".
- Sau khi modify volume, phải đợi trạng thái `optimizing`/`completed` mới sửa tiếp, và có giới hạn thời gian giữa hai lần sửa cùng một volume.

#### Quy tắc nhớ cho thi

- **Thấy** "gp2 + cần thêm IOPS + cost-efficient" → **tăng size gp2** (3 IOPS/GiB), tính số GiB cần thêm.
- **Thấy** "EFS / S3" cho workload IOPS ngẫu nhiên cao → **loại**.
- **Thấy** io1/io2 mà đề nói MOST cost-efficient → thường **không phải** đáp án nếu gp2/gp3 đáp ứng được.
- **Review flag** → chỉ đổi đáp án khi có bằng chứng mới, không đổi theo cảm giác.

### TD explanation

Correct option:

Modify the size of the gp2 volume for each instance from 3 TB to 4 TB

EBS provides block-level storage volumes for use with EC2 instances. EBS is well suited to both database-style applications that rely on random reads and writes, and to throughput-intensive applications that perform long, continuous reads and writes. EBS provides the following volume types: General Purpose SSD (gp2), Provisioned IOPS SSD (io1 and io2), Throughput Optimized HDD (st1), and Cold HDD (sc1).


via - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

gp2 volumes deliver single-digit millisecond latencies and the ability to burst to 3,000 IOPS for extended periods of time. Between a minimum of 100 IOPS (at 33.33 GiB and below) and a maximum of 16,000 IOPS (at 5,334 GiB and above), baseline performance scales linearly at 3 IOPS per GiB of volume size. Therefore, for the given use-case, the engineering team can address the shortfall of 3,000 IOPS by increasing the EBS volume size by 1 TB which will add 3,000 IOPS (3 IOPS per GB * 1000 GB) to the EBS volume on each instance.


via - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

Incorrect options:

Modify the type of Amazon EBS volume on each instance from gp2 to io1 and set provisioned IOPS to 12,000 - Provisioned IOPS SSD (io1 and io2) volumes are designed to meet the needs of I/O-intensive workloads, particularly database workloads, that are sensitive to storage performance and consistency. You can provision from 100 IOPS up to 64,000 IOPS per volume on Instances built on the Nitro System and up to 32,000 on other instances. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1 for io1 volumes, and 500:1 for io2 volumes.


via - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

For the given use-case, io1 does not represent the most cost-optimal solution as it is at least 25% more expensive compared to gp2 for per GB-month of provisioned storage. As identified above, a better solution is to just increase the existing gp2 EBS volume size by 1 TB to account for the additional 3,000 IOPS required for the production workload.


via - https://aws.amazon.com/ebs/pricing/

Provision a new EFS file system and migrate all the data to this new file system. Mount this file system on all 15 instances - For the given use-case, EFS does not represent the most cost-optimal solution as it is 3 times more expensive compared to gp2 on the basis of per GB storage cost. As identified above, a better solution is to just increase the existing gp2 EBS volume size by 1 TB to account for the additional 3,000 IOPS required for the production workload.


via - https://aws.amazon.com/efs/pricing/

Set up a new Amazon S3 bucket and migrate all the data to this new bucket. Configure each instance to access this S3 bucket and use it for storage - Although S3 provides cheap object-based storage, you cannot use S3 for the given high IOPS use-case as the instances need to be able to perform frequent read/write/update operations which cannot be supported out-of-the-box in S3.


via - https://aws.amazon.com/s3/pricing/

References:

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

https://aws.amazon.com/ebs/pricing/

https://aws.amazon.com/efs/pricing/

https://aws.amazon.com/s3/pricing/

</details>

<a id="q33"></a>

## Q33

<!-- source: U2Q18 · domain: NEW · flagged · time: 2:49 · first: 31:16 · visits: 3 · changes: 0 -->



The engineering team at a healthcare company is working on the Disaster Recovery (DR) plans for its Redshift cluster deployed in the eu-west-1 Region. The existing cluster is encrypted via AWS KMS and the team wants to copy the Redshift snapshots to another Region to meet the DR requirements.

As a Solutions Architect Professional, which of the following solutions would you suggest to address the given use-case?

- **A.** Create a snapshot copy grant in the source Region for a KMS key in the source Region. Configure Redshift cross-Region snapshots in the destination Region
- **B.** Create a snapshot copy grant in the destination Region for a KMS key in the destination Region. Configure Redshift cross-Region snapshots in the source Region
- **C.** Create an IAM role in destination Region with access to the KMS key in the source Region. Create a snapshot copy grant in the destination Region for this KMS key in the source Region. Configure Redshift cross-Region snapshots in the source Region
- **D.** Create a snapshot copy grant in the destination Region for a KMS key in the destination Region. Configure Redshift cross-Region replication in the source Region

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** Redshift KMS-encrypted, copy snapshots to another Region for DR, snapshot copy grant

🪤 **Your trap:** 🔁 Put the copy grant in the source Region with a source key. KMS keys are Regional, so the grant must be for a key in the destination Region; copy is enabled from the source cluster.

🧠 **Rule:** Redshift cross-Region snapshot of KMS cluster: snapshot copy grant in DESTINATION Region (destination key), enable copy in SOURCE Region.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
eu-west-1 (nguồn)                       Region đích (DR)
┌──────────────────────────┐            ┌──────────────────────────┐
│ Redshift cluster         │  snapshot  │ Snapshot đã copy         │
│ mã hóa bằng KMS key (R1) │ ─────────► │ cần mã hóa bằng KMS key  │
└──────────────────────────┘            │ của Region ĐÍCH (R2)     │
                                        └──────────────────────────┘
Yêu cầu: copy snapshot của cluster đã mã hóa KMS sang Region khác
```

Đáp án đúng: **B**. Anh chọn A.

#### Vì sao B đúng

**KMS key là tài nguyên theo Region.** Key ở Region nguồn không dùng được để mã hóa snapshot ở Region đích. Vì vậy Redshift cần:

1. Ở **Region đích**: tạo **snapshot copy grant**, trỏ tới một KMS key **nằm ở Region đích**. Grant này cho phép Redshift dùng key đó.
2. Ở **Region nguồn**: bật cross-Region snapshot copy trên cluster và chọn grant vừa tạo.

```
Region đích:  create snapshot copy grant (key của Region đích)
Region nguồn: enable cross-Region snapshot copy cho cluster, chọn grant
```

#### ⚠️ Lỗi lặp lại

Anh đã sai dạng này trước đó: đặt grant ở **Region nguồn** với key nguồn (đáp án A). Cách nhớ: snapshot sẽ được **ghi vào Region đích**, nên key mã hóa nó phải thuộc **Region đích**. Còn thao tác bật copy là thao tác trên **cluster nguồn**.

#### Phương án Anh chọn (A) sai ở đâu

A đảo ngược cả hai vế:

- Grant ở Region nguồn với key nguồn: sai, key nguồn không dùng được ở đích.
- Cấu hình copy ở Region đích: sai, cluster và setting copy nằm ở Region nguồn.

#### Các phương án còn lại

- **C:** tạo grant ở đích nhưng cho key ở Region nguồn. Không thể làm vậy vì key là theo Region. IAM role cross-Region cũng không giải quyết được điều này. Đây là distractor.
- **D:** grant đúng, nhưng nói "cross-Region **replication**" cho Redshift. Redshift không có khái niệm đó, đúng thuật ngữ là cross-Region **snapshot copy**. CRR là khái niệm của S3.

| Phương án | Vị trí grant | Key | Bật copy ở | Kết luận |
|---|---|---|---|---|
| A | Nguồn | Nguồn | Đích | Sai cả ba |
| **B** | **Đích** | **Đích** | **Nguồn** | **Đúng** |
| C | Đích | Nguồn | Nguồn | Key sai Region |
| D | Đích | Đích | "Replication" | Thuật ngữ sai |

#### Lưu ý thực tế

- Cluster không mã hóa thì không cần snapshot copy grant, chỉ cần bật cross-Region snapshot copy.
- Snapshot copy grant là một resource riêng, đặt tên được và tái sử dụng khi cấu hình copy.

#### Quy tắc nhớ cho thi

- **Thấy** "Redshift + KMS + copy snapshot sang Region khác" → **snapshot copy grant ở Region đích, key ở Region đích, bật copy ở cluster nguồn**.
- **Thấy** "key nguồn dùng ở Region đích" → **sai**, KMS key là theo Region.
- **Thấy** "Redshift cross-Region replication" → **sai thuật ngữ**, đúng là cross-Region snapshot copy.
- Mnemonic: **"Grant đi theo snapshot đến đích, công tắc copy ở lại nguồn"**.

### TD explanation

Correct option:

Create a snapshot copy grant in the destination Region for a KMS key in the destination Region. Configure Redshift cross-Region snapshots in the source Region

To copy snapshots for AWS KMS–encrypted clusters to another AWS Region, you need to create a grant for Redshift to use a KMS customer master key (CMK) in the destination AWS Region. Then choose that grant when you enable copying of snapshots in the source AWS Region. You cannot use a KMS key from the source Region as AWS KMS keys are specific to an AWS Region.


via - https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#configure-snapshot-copy-grant

Incorrect options:

Create a snapshot copy grant in the source Region for a KMS key in the source Region. Configure Redshift cross-Region snapshots in the destination Region - As described above, you need to configure the Redshift cross-Region snapshot in the source Region and not the destination Region. Also, the snapshot copy grant must be set up in the destination Region for a KMS key in the destination Region.

Create an IAM role in destination Region with access to the KMS key in the source Region. Create a snapshot copy grant in the destination Region for this KMS key in the source Region. Configure Redshift cross-Region snapshots in the source Region - This has been added as a distractor as AWS KMS keys are specific to an AWS Region. You cannot create a snapshot copy grant in the destination Region for a KMS key in the source Region.

Create a snapshot copy grant in the destination Region for a KMS key in the destination Region. Configure Redshift cross-Region replication in the source Region - This has been added as a distractor as there is no such thing as cross-Region replication for Redshift. The concept of cross-Region replication (CRR) applies to Amazon S3.

Reference:

https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#configure-snapshot-copy-grant

</details>

<a id="q45"></a>

## Q45

<!-- source: U2Q10 · domain: NEW · flagged · time: 2:38 · first: 161:45 · visits: 5 · changes: 2 -->



The engineering team at a company is evaluating the Multi-AZ and Read Replica capabilities of RDS MySQL vs Aurora MySQL before they implement the solution in their production environment. The company has hired you as an AWS Certified Solutions Architect Professional to provide a detailed report on this technical requirement.

Which of the following would you identify as correct regarding the given use-case? (Select three)

- **A.** Read Replicas can be manually promoted to a standalone database instance for Aurora MySQL whereas Read Replicas for RDS MySQL can be promoted to the primary instance
- **B.** Database engine version upgrades happen on primary for Aurora MySQL whereas all instances are updated together for RDS MySQL
- **C.** Multi-AZ deployments for both RDS MySQL and Aurora MySQL follow synchronous replication
- **D.** Multi-AZ deployments for Aurora MySQL follow synchronous replication whereas Multi-AZ deployments for RDS MySQL follow asynchronous replication
- **E.** The primary and standby DB instances are upgraded at the same time for RDS MySQL Multi-AZ. All instances are upgraded at the same time for Aurora MySQL
- **F.** Read Replicas can be manually promoted to a standalone database instance for RDS MySQL whereas Read Replicas for Aurora MySQL can be promoted to the primary instance

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E, F · **You picked:** A, C, E

🔑 **Key words:** RDS MySQL vs Aurora MySQL, Multi-AZ, read replica promotion, engine upgrade, Select THREE

🪤 **Your trap:** Swapped the promotion facts: Aurora replicas are failover targets that can become the primary; RDS MySQL read replicas are promoted to a separate standalone instance. Udemy's 'Aurora Multi-AZ is synchronous' is simplified wording (Aurora replicates storage across 3 AZs).

🧠 **Rule:** RDS read replica → promote = standalone DB (breaks replication). Aurora replica → failover = new primary of the same cluster.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
RDS MySQL                               Aurora MySQL
┌─────────┐  sync   ┌─────────┐         ┌──────────────────────────────┐
│ Primary │ ──────► │ Standby │         │ Primary + tối đa 15 Aurora   │
└─────────┘ (Multi-AZ)└───────┘         │ Replicas dùng CHUNG 1 cluster│
     │ async                            │ volume (6 bản / 3 AZ)        │
     ▼                                  └──────────────────────────────┘
 Read Replica
```

Select three. Đáp án đúng: **C, E, F**. Anh chọn **A, C, E**: đúng C và E, sai A, bỏ sót F.

#### Ba đáp án đúng

**C - Multi-AZ đều đồng bộ (synchronous).** RDS Multi-AZ: primary replicate đồng bộ sang standby ở AZ khác. Aurora: khi ghi, dữ liệu được ghi đồng bộ vào các storage node ở nhiều AZ.

**E - Cách nâng cấp engine version.** RDS MySQL Multi-AZ: primary và standby được nâng cấp cùng lúc. Aurora MySQL: tất cả instance nâng cấp cùng lúc.

**F - Promote read replica.**

- **RDS MySQL:** read replica được promote thành **standalone DB instance** (tách khỏi source, không còn replication).
- **Aurora MySQL:** Aurora Replica là **failover target**, khi primary lỗi thì replica được promote thành **primary** của cùng cluster.

#### Phương án Anh chọn (A) sai ở đâu

A đảo ngược F: nói Aurora replica thành standalone còn RDS replica thành primary. Hai cơ chế khác bản chất:

```
RDS MySQL read replica:  promote -> DB độc lập, mất replication với source
Aurora replica:          failover -> thành primary mới của CÙNG cluster
                         (vì dùng chung cluster volume với primary)
```

Mẹo nhớ: Aurora replica **không có storage riêng** nên không thể "đứng riêng", nó chỉ có thể thay primary.

#### Các phương án sai còn lại

- **B:** nói Aurora chỉ nâng cấp primary. Sai, Aurora MySQL nâng cấp tất cả instance cùng lúc.
- **D:** nói RDS MySQL Multi-AZ là asynchronous. Sai, RDS Multi-AZ là synchronous. Asynchronous là của **read replica**.

| Tiêu chí | RDS MySQL | Aurora MySQL |
|---|---|---|
| Multi-AZ replication | Đồng bộ (primary -> standby) | Ghi đồng bộ vào storage nhiều AZ |
| Read replica | Async, promote = standalone | Dùng chung volume, promote = primary |
| Upgrade engine (Multi-AZ) | Primary + standby cùng lúc | Tất cả instance cùng lúc |

#### 📝 Ghi chú kỹ thuật

Câu "Aurora Multi-AZ synchronous replication" của Udemy là cách nói **đơn giản hóa**. Thực tế Aurora không có "standby replica" kiểu RDS Multi-AZ. Cơ chế thật:

- Cluster volume lưu **6 bản copy dữ liệu trên 3 AZ** (mỗi AZ 2 bản), trong một Region.
- Ghi dùng **quorum**: cần 4/6 bản xác nhận mới coi là ghi thành công; đọc dùng quorum 3/6.
- Tính chịu lỗi: mất 1 AZ (2 bản) vẫn ghi được; mất 1 AZ cộng thêm 1 bản vẫn đọc được.
- Các Aurora Replica đọc từ cùng volume này, không phải nhận dữ liệu qua replication riêng như RDS read replica (độ trễ replica thường rất nhỏ).

Khi thi, giữ đáp án theo đề (C đúng), nhưng hiểu bản chất là **storage nhân bản đồng bộ theo quorum** chứ không phải cặp primary-standby.

Một chi tiết ngoài đề: Aurora MySQL còn có cross-Region read replica cluster, cái này promote được thành cluster độc lập. Đề này nói về Aurora Replica trong cùng cluster nên áp dụng quy tắc failover.

#### Quy tắc nhớ cho thi

- **Thấy** "RDS read replica promote" → **standalone DB**, replication đứt.
- **Thấy** "Aurora replica promote" → **thành primary** (failover target, dùng chung cluster volume).
- **Thấy** "RDS Multi-AZ" → **synchronous** standby; **read replica** mới là asynchronous.
- **Thấy** "Aurora storage" → **6 bản / 3 AZ**, quorum ghi 4/6, đọc 3/6.
- **Thấy** "upgrade engine Multi-AZ" → RDS: primary + standby cùng lúc; Aurora: tất cả cùng lúc.

### TD explanation

Correct options:

Multi-AZ deployments for both RDS MySQL and Aurora MySQL follow synchronous replication

Read Replicas can be manually promoted to a standalone database instance for RDS MySQL whereas Read Replicas for Aurora MySQL can be promoted to the primary instance

The primary and standby DB instances are upgraded at the same time for RDS MySQL Multi-AZ. All instances are upgraded at the same time for Aurora MySQL

RDS Read replicas are a special type of DB instances that make use of the built-in replication functionality for RDS. The source DB instance becomes the primary DB instance. Updates made to the primary DB instance are asynchronously copied to the read replica. When you create a read replica, you first specify an existing DB instance as the source. Then Amazon RDS takes a snapshot of the source instance and creates a read-only instance from the snapshot. Amazon RDS then uses the asynchronous replication method for the DB engine to update the read replica whenever there is a change to the primary DB instance.

Aurora Replicas are independent endpoints in an Aurora DB cluster, best used for scaling read operations and increasing availability. Up to 15 Aurora Replicas can be distributed across the Availability Zones that a DB cluster spans within an AWS Region. The DB cluster volume is made up of multiple copies of the data for the DB cluster. However, the data in the cluster volume is represented as a single, logical volume to the primary instance and to Aurora Replicas in the DB cluster.

In a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. The primary DB instance is synchronously replicated across Availability Zones to a standby replica to provide data redundancy, eliminate I/O freezes, and minimize latency spikes during system backups. Aurora stores copies of the data in a DB cluster across multiple Availability Zones in a single AWS Region. When data is written to the primary DB instance, Aurora synchronously replicates the data across Availability Zones to six storage nodes associated with your cluster volume.

To increase availability, you can use Aurora Replicas as failover targets. That is, if the primary instance fails, an Aurora Replica is promoted to the primary instance. There is a brief interruption during which read and write requests made to the primary instance fail with an exception, and the Aurora Replicas are rebooted.

For RDS MySQL in Multi-AZ configuration, database engine version upgrades happen on both the primary and standby DB instances at the same time. For Aurora MySQL, all instances are upgraded at the same time.


via - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.html

Incorrect options:

Database engine version upgrades happen on primary for Aurora MySQL whereas all instances are updated together for RDS MySQL

Read Replicas can be manually promoted to a standalone database instance for Aurora MySQL whereas Read Replicas for RDS MySQL can be promoted to the primary instance

Multi-AZ deployments for Aurora MySQL follow synchronous replication whereas Multi-AZ deployments for RDS MySQL follow asynchronous replication

These three options contradict the explanation provided above, so these are incorrect.

References:

https://aws.amazon.com/rds/features/read-replicas/

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html

</details>

<a id="q54"></a>

## Q54

<!-- source: U2Q21 · domain: NEW · flagged · time: 3:09 · first: 60:38 · visits: 3 · changes: 1 -->



A leading mobility company wants to use AWS for its connected cab application that would collect sensor data from its electric cab fleet to give drivers dynamically updated map information. The company would like to build its new sensor service by leveraging fully serverless components that are provisioned and managed automatically by AWS. The development team at the company does not want an option that requires the capacity to be manually provisioned, as it does not want to respond manually to changing volumes of sensor data. The company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for this strategic initiative.

Given these constraints, which of the following solutions would you suggest as the BEST fit to develop this service?

- **A.** Ingest the sensor data in Kinesis Data Firehose, which directly writes the data into an auto-scaled DynamoDB table for downstream processing
- **B.** Ingest the sensor data in an Amazon SQS standard queue, which is polled by an application running on an EC2 instance and the data is written into an auto-scaled DynamoDB table for downstream processing
- **C.** Ingest the sensor data in an Amazon SQS standard queue, which is polled by a Lambda function in batches and the data is written into an auto-scaled DynamoDB table for downstream processing
- **D.** Ingest the sensor data in a Kinesis Data Stream, which is polled by an application running on an EC2 instance and the data is written into an auto-scaled DynamoDB table for downstream processing

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** fully serverless, no manual capacity, sensor data, DynamoDB auto scaling

🪤 **Your trap:** 🔁 Picked Firehose writing directly to DynamoDB; DynamoDB is not a Firehose destination. Kinesis Data Streams needs shard capacity planning; EC2 pollers are not serverless.

🧠 **Rule:** Firehose targets: S3, Redshift, OpenSearch, Splunk, HTTP endpoints, Snowflake/Iceberg — not DynamoDB. Serverless + no capacity planning = SQS + Lambda.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Xe taxi điện ──► [Ingest] ──► [Xử lý] ──► DynamoDB (auto scaling)
(sensor data)

Yêu cầu: FULLY serverless, AWS tự quản lý,
         KHÔNG muốn provision capacity thủ công
```

Đáp án đúng: **C (SQS standard + Lambda poll theo batch + DynamoDB)**. Anh chọn A (Kinesis Data Firehose ghi thẳng vào DynamoDB).

#### Vì sao C đúng

```
Sensor ──► SQS standard queue ──► Lambda (event source mapping, batch) ──► DynamoDB auto scaling
          (tự scale, không cần          (không server)                      (không đặt tay capacity)
           provision)
```

- **SQS** là fully managed, queue tự scale, không cần provision throughput.
- **Lambda** poll SQS qua event source mapping, xử lý theo batch, không có server để quản lý.
- **DynamoDB auto scaling** điều chỉnh capacity theo tải.
- Cả chuỗi không có thành phần nào cần Anh đặt capacity bằng tay, đúng yêu cầu đề.

#### ⚠️ Lỗi lặp lại

Anh đã sai đúng chỗ này: nghĩ Firehose có thể ghi trực tiếp vào DynamoDB. **Firehose không có đích DynamoDB.** Đích của Firehose gồm: S3, Redshift, OpenSearch Service, Splunk, HTTP endpoint (kể cả đối tác như Datadog, Dynatrace, MongoDB, New Relic, Sumo Logic...), ngoài ra còn Snowflake và Apache Iceberg tables. Không có DynamoDB.

Muốn đưa data vào DynamoDB thì cần một lớp compute ở giữa (Lambda), hoặc dùng service khác.

#### Các phương án sai

- **A (Firehose -> DynamoDB):** Firehose không ghi thẳng DynamoDB được.
- **B (SQS + EC2 poller):** EC2 là server phải quản lý, trái với "fully serverless".
- **D (Kinesis Data Streams + EC2 poller):** cũng dùng EC2, loại ngay. Ngoài ra Kinesis Data Streams ở chế độ provisioned còn phải tính số shard, trái ý "không provision capacity".

| Phương án | Ingest | Xử lý | Serverless | Lỗi chính |
|---|---|---|---|---|
| A | Firehose | (ghi thẳng) | Có | Firehose không có đích DynamoDB |
| B | SQS | EC2 | Không | EC2 |
| **C** | **SQS** | **Lambda** | **Có** | **Đúng** |
| D | KDS | EC2 | Không | EC2 + shard |

#### Lưu ý thực tế

- Lambda cũng đọc được từ Kinesis Data Streams, nhưng đề này không có phương án KDS + Lambda, nên đáp án là SQS + Lambda.
- SQS standard: at-least-once, thứ tự best-effort. Nếu cần thứ tự nghiêm ngặt hoặc exactly-once thì mới nghĩ đến FIFO.

#### Quy tắc nhớ cho thi

- **Thấy** "fully serverless + không provision thủ công" → loại mọi phương án có **EC2**.
- **Thấy** "Firehose" → đích là **S3 / Redshift / OpenSearch / Splunk / HTTP endpoint / Snowflake / Iceberg**, **không** phải DynamoDB.
- **Thấy** "ingest rồi ghi DynamoDB, serverless" → **SQS + Lambda**.
- **Thấy** "Kinesis Data Streams" (provisioned) → phải tính **shard**, không phải "no capacity planning".

### TD explanation

Correct option:
Ingest the sensor data in an Amazon SQS standard queue, which is polled by a Lambda function in batches and the data is written into an auto-scaled DynamoDB table for downstream processing

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume. Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.

You can use an AWS Lambda function to process messages in an Amazon Simple Queue Service (Amazon SQS) queue. Lambda event source mappings support standard queues and first-in, first-out (FIFO) queues. With Amazon SQS, you can offload tasks from one component of your application by sending them to a queue and processing them asynchronously.


via - https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

AWS manages all ongoing operations and underlying infrastructure needed to provide a highly available and scalable message queuing service. With SQS, there is no upfront cost, no need to acquire, install, and configure messaging software, and no time-consuming build-out and maintenance of supporting infrastructure. SQS queues are dynamically created and scale automatically so you can build and grow applications quickly and efficiently.
As there is no need to manually provision the capacity, so this is the correct option.

Incorrect options:

Ingest the sensor data in Kinesis Data Firehose, which directly writes the data into an auto-scaled DynamoDB table for downstream processing

Amazon Kinesis Data Firehose is a fully managed service for delivering real-time streaming data to destinations such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon OpenSearch Service, Splunk, and any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, and Sumo Logic.

Firehose cannot directly write into a DynamoDB table, so this option is incorrect.

Ingest the sensor data in an Amazon SQS standard queue, which is polled by an application running on an EC2 instance and the data is written into an auto-scaled DynamoDB table for downstream processing

Ingest the sensor data in a Kinesis Data Stream, which is polled by an application running on an EC2 instance and the data is written into an auto-scaled DynamoDB table for downstream processing

Using an application on an EC2 instance is ruled out as the company wants to use fully serverless components. So both these options are incorrect.

References:
https://aws.amazon.com/sqs/

https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html

https://aws.amazon.com/kinesis/data-streams/faqs/

</details>

---

# Group B — Multi-select half right: one pick from a sibling feature that does not do the job (6)

<a id="q13"></a>

## Q13

<!-- source: U2Q27 · domain: CI · flagged · time: 2:23 · first: 110:32 · visits: 4 · changes: 1 -->



A company has built a serverless electronic document management system for users to upload their documents. The system also has a web application that connects to an Amazon API Gateway with Regional endpoints which in turn invokes AWS Lambda functions. The Lambda functions write the metadata of the documents to the Amazon Aurora Serverless database before uploading the actual documents to the Amazon S3 bucket. While the serverless architecture has been tested in the US East (N. Virginia) Region, the solution should be scalable for other AWS Regions too.

As an AWS Certified Solutions Architect Professional, which options would you recommend to make the architecture scalable while offering low latency service to customers of any AWS region? (Select two)

- **A.** Configure AWS Global Accelerator to front the CloudFront distribution for providing low latency access to customers of all AWS regions
- **B.** Change the API Gateway Regional endpoints to private API endpoints
- **C.** Enable S3 Transfer Acceleration on the S3 bucket and configure the web application to use the Transfer Acceleration endpoints
- **D.** Change the API Gateway Regional endpoints to edge-optimized endpoints
- **E.** Configure CloudFront to use signed URLs for providing low latency access to customers of all AWS regions

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D · **You picked:** A, D

🔑 **Key words:** serverless upload app, multi-Region users, low latency, API Gateway Regional, S3 uploads

🪤 **Your trap:** 🔁 Picked Global Accelerator in front of CloudFront; GA fronts ALB/NLB/EC2/Elastic IP, never CloudFront or S3. Low-latency upload to S3 is S3 Transfer Acceleration.

🧠 **Rule:** Global users → API Gateway edge-optimized endpoint + S3 Transfer Acceleration for uploads. GA cannot front CloudFront or S3.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Người dùng toàn cầu
      │
      ▼
API Gateway (Regional, us-east-1) ──► Lambda ──► Aurora Serverless (metadata)
                                          │
                                          └────► S3 bucket (file tài liệu)

Yêu cầu: scalable cho nhiều Region + LOW LATENCY cho user ở mọi nơi
```

Select two. Đáp án đúng: **C, D**. Anh chọn **A, D**: đúng D, sai A, bỏ sót C.

#### Hai đáp án đúng, mỗi cái xử lý một chặng

**D - API Gateway edge-optimized endpoint.** Endpoint Regional phục vụ tốt cho client cùng Region. Edge-optimized định tuyến request tới **CloudFront Point of Presence gần nhất**, sau đó đi vào API qua backbone AWS. Hợp với client phân tán toàn cầu.

**C - S3 Transfer Acceleration.** Người dùng upload tài liệu lên S3 từ xa. Transfer Acceleration đưa traffic vào edge location gần nhất rồi đi qua backbone AWS tới bucket. Ứng dụng phải dùng endpoint `bucketname.s3-accelerate.amazonaws.com`.

```
Chặng API:    user ──► CloudFront POP ──► API Gateway   (edge-optimized)
Chặng upload: user ──► edge location ──► S3             (Transfer Acceleration)
```

#### ⚠️ Lỗi lặp lại

Anh đã sai: chọn **Global Accelerator đứng trước CloudFront**. Endpoint hợp lệ của Global Accelerator chỉ gồm **Application Load Balancer, Network Load Balancer, EC2 instance, Elastic IP**. Không có CloudFront, không có S3. Cách nhớ: Global Accelerator tăng tốc tới **hạ tầng có IP/LB**, còn upload S3 tầm xa dùng **S3 Transfer Acceleration**.

#### Các phương án sai

- **A (Global Accelerator trước CloudFront):** endpoint không hợp lệ như trên. Trong đề cũng không có distribution CloudFront nào.
- **B (private API endpoint):** private API chỉ truy cập được từ VPC qua interface VPC endpoint. Ngược với nhu cầu phục vụ user internet toàn cầu.
- **E (CloudFront signed URL):** signed URL là cơ chế **kiểm soát truy cập** (hết hạn, ủy quyền private content), không cải thiện latency.

| Công cụ | Dùng để | Không dùng để |
|---|---|---|
| **API GW edge-optimized** | User xa gọi API qua CloudFront POP | Client chỉ trong cùng Region (Regional đủ) |
| **S3 Transfer Acceleration** | Upload/download S3 tầm xa | Kiểm soát quyền truy cập |
| Global Accelerator | Tăng tốc tới ALB/NLB/EC2/EIP | Đứng trước CloudFront hoặc S3 |
| Signed URL | Giới hạn truy cập private content | Giảm latency |
| Private API endpoint | API chỉ nội bộ VPC | User internet |

#### Lưu ý thực tế

- Tên bucket dùng Transfer Acceleration phải DNS-compliant và không chứa dấu chấm.
- Edge-optimized là mặc định của API Gateway REST API. CloudFront đứng sau do API Gateway quản lý, không hiển thị trong tài khoản của Anh.
- Transfer Acceleration có phụ phí; nếu client gần bucket thì có thể không nhanh hơn.

#### Quy tắc nhớ cho thi

- **Thấy** "user toàn cầu gọi API Gateway Regional" → đổi sang **edge-optimized**.
- **Thấy** "upload S3 từ xa, low latency" → **S3 Transfer Acceleration**.
- **Thấy** "Global Accelerator" → endpoint chỉ **ALB / NLB / EC2 / Elastic IP**, không CloudFront, không S3.
- **Thấy** "signed URL" → **kiểm soát truy cập**, không phải hiệu năng.

### TD explanation

Correct options:

Enable S3 Transfer Acceleration on the S3 bucket and configure the web application to use the Transfer Acceleration endpoints

Amazon S3 Transfer Acceleration can speed up content transfers to and from Amazon S3 by as much as 50-500% for long-distance transfer of larger objects. Customers who have either web or mobile applications with widespread users or applications hosted far away from their S3 bucket can experience long and variable upload and download speeds over the Internet. S3 Transfer Acceleration (S3TA) reduces the variability in Internet routing, congestion, and speeds that can affect transfers, and logically shortens the distance to S3 for remote applications. S3TA improves transfer performance by routing traffic through Amazon CloudFront’s globally distributed Edge Locations and over AWS backbone networks, and by using network protocol optimizations.

To access the bucket that is enabled for Transfer Acceleration, you must use the endpoint bucketname.s3-accelerate.amazonaws.com.

Change the API Gateway Regional endpoints to edge-optimized endpoints

An API endpoint type refers to the hostname of the API. The API endpoint type can be edge-optimized, regional, or private, depending on where the majority of your API traffic originates from.

A regional API endpoint is intended for clients in the same region. An edge-optimized API endpoint is best for geographically distributed clients. API requests are routed to the nearest CloudFront Point of Presence (POP). This is the default endpoint type for API Gateway REST APIs.

Incorrect options:

Configure AWS Global Accelerator to direct traffic to the CloudFront distribution for providing low latency access to customers of all AWS regions - AWS Global Accelerator has the following types of endpoints only - Network Load Balancers, Application Load Balancers, Amazon EC2 instances, or Elastic IP addresses. Hence, this option is incorrect.

Global Accelerator Types:

via - https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-components.html

Global Accelerator vs CloudFront:

via - https://aws.amazon.com/global-accelerator/faqs/

Configure CloudFront to use signed URLs for providing low latency access to customers of all AWS regions - A signed URL includes additional information, for example, expiration date and time, that gives you more control over access to your content. You can distribute private content using a signed URL. However, latency issues cannot be fixed by using signed URLs.

Change the API Gateway Regional endpoints to private API endpoints - A private API endpoint is an API endpoint that can only be accessed from your Amazon Virtual Private Cloud (VPC) using an interface VPC endpoint, which is an endpoint network interface (ENI) that you create in your VPC. This option is incorrect for the given use case.

References:

https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html

https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-components.html

https://aws.amazon.com/global-accelerator/faqs/

</details>

<a id="q24"></a>

## Q24

<!-- source: U2Q43 · domain: CI · flagged · time: 3:22 · first: 113:17 · visits: 5 · changes: 1 -->



A retail company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for managing a serverless application that consists of multiple API gateways, Lambda functions, S3 buckets and DynamoDB tables. The company is getting reports from customers that some of the application components seem to be lagging while loading dynamic images and some are timing out with the "504 Gateway Timeout" error. As part of your investigations to identify the root cause behind this issue, you can confirm that DynamoDB monitoring metrics are at acceptable levels.

Which of the following steps would you recommend to address these application issues? (Select two)

- **A.** Process and analyze the VPC Flow Logs to determine if there is packet loss between the Lambda function and S3
- **B.** Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals
- **C.** Enable execution logging for the API Gateway. Process and analyze the execution logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **D.** Enable access logging for the API Gateway. Process and analyze the access logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **E.** Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** B, C

🔑 **Key words:** serverless API, slow image loads, 504 Gateway Timeout, DynamoDB fine, find root cause

🪤 **Your trap:** 🔁 (missed on 10-08 too) Picked API Gateway execution logging; it shows the 504 but not where the time goes. X-Ray traces each hop; Lambda CloudWatch Logs show processing time.

🧠 **Rule:** Latency / timeout root cause across API Gateway → Lambda → S3 = X-Ray + Lambda CloudWatch Logs. Gateway logs only confirm the error.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──► API Gateway ──► Lambda (xử lý ảnh) ──► S3 / DynamoDB
               │
               └─ trả về "504 Gateway Timeout"
                  (Endpoint Request Timed-out Exception)

DynamoDB metrics bình thường -> nghi ngờ nằm ở Lambda / xử lý ảnh
Yêu cầu: tìm ROOT CAUSE của chậm / timeout
```

Select two. Đáp án đúng: **B, E**. Anh chọn **B, C**: đúng B, sai C, bỏ sót E.

#### Hai đáp án đúng

**B - CloudWatch Logs của Lambda.** Lambda tự ghi log vào CloudWatch Logs. Thêm logging trong code để đo thời gian xử lý từng ảnh, rồi phân tích định kỳ. Cho biết ảnh nào chậm và chậm bao lâu.

**E - AWS X-Ray traces.** X-Ray vẽ service map và trace từng request qua các thành phần, giúp thấy **thời gian nằm ở chặng nào** (API Gateway, Lambda, gọi S3...) và trace nào bị lỗi.

```
Gateway log:  "request này 504"                 -> biết CÓ lỗi
X-Ray:        thời gian mỗi chặng trong request -> biết LỖI Ở ĐÂU
Lambda log:   thời gian xử lý từng ảnh          -> biết VÌ SAO chậm
```

#### ⚠️ Lỗi lặp lại

Câu này Anh cũng đã sai ngày 10-08, cùng một kiểu: chọn log ở **API Gateway**. Execution logging và access logging của API Gateway chỉ xác nhận có lỗi HTTP (ở đây 504 = Endpoint Request Timed-out). Chúng **không cho biết nguyên nhân** vì thời gian bị tiêu ở phía backend (Lambda xử lý ảnh). Muốn tìm root cause của latency phải nhìn **vào trong từng chặng**: X-Ray + log của Lambda.

#### Phương án Anh chọn (C) và các phương án sai

- **C (execution logging):** có ích để debug cấu hình API, nhưng không xác định nguyên nhân backend chậm. Lưu ý thêm: HTTP API chỉ có access logs, không có execution logs.
- **D (access logging):** ghi ai gọi và gọi thế nào, thấy mã 504 nhưng không chỉ ra Lambda chậm ở đâu.
- **A (VPC Flow Logs):** Flow Logs ghi metadata luồng traffic IP (accepted/rejected) trên network interface, không đo được packet loss. Đo packet loss/latency mạng dùng công cụ như `AWSSupport-SetupIPMonitoringFromVPC`. Đây là distractor.

| Công cụ | Trả lời câu hỏi | Dùng cho root cause latency? |
|---|---|---|
| **X-Ray** | Thời gian mỗi chặng, trace lỗi | Có |
| **Lambda CloudWatch Logs** | Thời gian xử lý trong function | Có |
| API GW execution log | Request/response, lỗi cấu hình API | Không (chỉ thấy lỗi) |
| API GW access log | Ai gọi, status code | Không |
| VPC Flow Logs | Traffic IP accepted/rejected | Không |

#### Lưu ý thực tế

- Để X-Ray thấy chặng API Gateway, cần bật tracing trên stage API Gateway; với Lambda cần bật active tracing.
- API Gateway có giới hạn thời gian chờ tích hợp mặc định 29 giây, nên xử lý ảnh quá lâu sẽ ra 504 dù Lambda vẫn còn chạy.

#### Quy tắc nhớ cho thi

- **Thấy** "504 Gateway Timeout + serverless + tìm root cause" → **X-Ray + CloudWatch Logs của Lambda**.
- **Thấy** "API Gateway logs" → chỉ **xác nhận lỗi**, không chỉ ra nguyên nhân backend.
- **Thấy** "VPC Flow Logs + packet loss" → **sai**, Flow Logs không đo packet loss.
- Mnemonic: **"Gateway cho biết CÓ lỗi, X-Ray cho biết Ở ĐÂU, Lambda log cho biết VÌ SAO"**.

### TD explanation

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

</details>

<a id="q25"></a>

## Q25

<!-- source: U2Q32 · domain: CI · time: 4:05 · first: 156:28 · visits: 5 · changes: 2 -->



An automobile company helps more than 20 million web and mobile users browse automobile dealer inventory, read vehicle reviews, and consume other automobile-related content by leveraging its library of 50 million vehicle photos uploaded by auto dealers. The company is planning a key update with even better image quality and faster load times on the company's website as well as mobile apps but the existing image-handling solution based on Cloudera MapReduce clusters is not the right tool for the job. The company now wants to switch to a serverless solution on AWS Cloud. As part of this process, the engineering team has been studying various best practices for serverless solutions. They intend to use AWS Lambda extensively and are looking at the salient features to consider when using Lambda as the backbone for the serverless architecture.

As a Solutions Architect Professional, which of the following would you identify as key considerations for a serverless architecture? (Select three)

- **A.** If you intend to reuse code in more than one Lambda function, you should consider creating a Lambda Layer for the reusable code
- **B.** The bigger your deployment package, the slower your Lambda function will cold-start. Hence, AWS suggests packaging dependencies as a separate package from the actual Lambda package
- **C.** Lambda allocates compute power in proportion to the memory you allocate to your function. AWS, thus recommends to over provision your function time out settings for the proper performance of Lambda functions
- **D.** Serverless databases and Lambda complement each other and you should install databases on the Lambda functions
- **E.** By default, Lambda functions always operate from an AWS-owned VPC and hence have access to any public internet address or public AWS APIs. Once a Lambda function is VPC-enabled, it will need a route through a NAT gateway in a public subnet to access public resources
- **F.** Since Lambda functions can scale extremely quickly, it's a good idea to deploy a CloudWatch Alarm that notifies your team when function metrics such as ConcurrentExecutions or Invocations exceeds the expected threshold

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E, F · **You picked:** A, C, F

🔑 **Key words:** Lambda best practices, Select THREE, layers, VPC-enabled needs NAT, concurrency alarm

🪤 **Your trap:** Picked 'over-provision the timeout' — AWS advises right-sizing memory and setting timeouts to realistic values, not over-provisioning. Missed that VPC-enabled Lambda needs a NAT gateway for public access.

🧠 **Rule:** Lambda: layers for shared code; memory drives CPU; VPC Lambda reaches the internet only via NAT; alarm on ConcurrentExecutions.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Web/mobile users (20M) ──► Lambda (xử lý ảnh) ──► S3 / DB
                              │
        Chọn 3 phát biểu ĐÚNG về best practice của Lambda
```

Đề là dạng "chọn các phát biểu đúng", nên **mỗi lựa chọn phải đúng độc lập**. Không có chuyện "C sai nhưng ghép với A, F thì vẫn ổn". Đáp án đúng: **A + E + F**. Anh chọn A, C, F: đúng A và F, sai C và bỏ sót E.

#### Các phát biểu đúng (A, E, F)

**A đúng - Lambda Layer cho code dùng chung.** Layer là file ZIP chứa library, custom runtime hoặc dependency. Function kéo layer vào mà không cần nhét vào deployment package, giúp package nhỏ gọn. Một function dùng được tối đa 5 layer; tổng dung lượng unzipped của function + mọi layer không vượt 250 MB.

**E đúng - Lambda và VPC.** Mặc định Lambda chạy trong VPC do AWS sở hữu, nên gọi được internet và public AWS API. Khi **VPC-enabled**, mọi traffic tuân theo route table của subnet:

```
Lambda mặc định:        Lambda ──► Internet / public AWS API  (OK)

Lambda VPC-enabled:     Lambda (private subnet)
                           └─► NAT Gateway (public subnet) ──► IGW ──► Internet
                           (không có NAT = mất đường ra public)
```

Chỉ gắn Lambda vào VPC khi cần chạm resource private (ví dụ RDS).

**F đúng - Giám sát concurrency.** Lambda scale rất nhanh, nên đặt CloudWatch Alarm trên `ConcurrentExecutions` hoặc `Invocations` để biết khi có spike. Nên thêm AWS Budgets để theo dõi chi phí.

#### Lựa chọn của anh: C sai ở đâu

C ghép hai ý trong một câu:

- Vế 1 "compute power tỉ lệ với memory" là **đúng**. Đây là lý do C trông hợp lý.
- Vế 2 "AWS khuyên **over-provision timeout**" là **sai**. AWS khuyên làm ngược lại: hiểu hiệu năng code rồi đặt timeout sát thực tế. Timeout quá dài khiến function chạy lâu hơn dự kiến (ví dụ khi bị treo chờ dependency) và phát sinh chi phí ngoài ý muốn.

Một vế sai là cả phát biểu sai. Thứ nên over-provision (nếu có lợi) là **memory** để chạy nhanh hơn, không phải timeout.

#### Các lựa chọn sai còn lại

- **B sai:** "tách dependency thành package riêng để cold-start nhanh hơn" là distractor. TD ghi rõ có thể gói mọi dependency trong một deployment package mà không ảnh hưởng hiệu năng theo cách phát biểu này nói.
- **D sai:** Lambda không hỗ trợ cài database lên function. Dùng serverless database (DynamoDB, Aurora Serverless...) như một dịch vụ riêng.

| Option | Vế đầu | Vế sau | Kết luận |
|---|---|---|---|
| A | Layer cho code dùng chung | - | Đúng |
| C | Memory quyết định CPU (đúng) | Over-provision timeout (sai) | **Sai** |
| E | Mặc định ra internet được | VPC-enabled cần NAT | Đúng |
| F | Scale nhanh | Alarm ConcurrentExecutions | Đúng |

#### Lưu ý thực tế

- Lambda trong VPC gọi dịch vụ AWS (S3, DynamoDB) có thể dùng **VPC endpoint** thay cho NAT. Nhưng theo cách diễn đạt của đề, phát biểu E vẫn là đáp án đúng.
- Public subnet cho NAT Gateway; Lambda đặt ở **private subnet**. Gắn Lambda vào public subnet không cho nó public IP nên không ra internet được.

#### Quy tắc nhớ cho thi

- **Câu "chọn các phát biểu đúng"** → kiểm từng vế, một vế sai là loại cả option.
- **Thấy "over-provision timeout"** → sai; **memory** mới là thứ tăng CPU.
- **Thấy "share code giữa nhiều Lambda"** → **Lambda Layer**.
- **Thấy "VPC-enabled Lambda ra internet"** → **NAT Gateway** ở public subnet.
- **Thấy "Lambda scale nhanh, kiểm soát"** → CloudWatch Alarm trên `ConcurrentExecutions` + Budgets.

### TD explanation

Correct options:

By default, Lambda functions always operate from an AWS-owned VPC and hence have access to any public internet address or public AWS APIs. Once a Lambda function is VPC-enabled, it will need a route through a NAT gateway in a public subnet to access public resources - Lambda functions always operate from an AWS-owned VPC. By default, your function has full ability to make network requests to any public internet address — this includes access to any of the public AWS APIs. For example, your function can interact with AWS DynamoDB APIs to PutItem or Query for records. You should only enable your functions for VPC access when you need to interact with a private resource located in a private subnet. An RDS instance is a good example.

Once your function is VPC-enabled, all network traffic from your function is subject to the routing rules of your VPC/Subnet. If your function needs to interact with a public resource, you will need a route through a NAT gateway in a public subnet.

When to VPC-Enable a Lambda Function:

via - https://aws.amazon.com/blogs/architecture/best-practices-for-developing-on-aws-lambda/

Since Lambda functions can scale extremely quickly, it's a good idea to deploy a CloudWatch Alarm that notifies your team when function metrics such as ConcurrentExecutions or Invocations exceeds the expected threshold - Since Lambda functions can scale extremely quickly, this means you should have controls in place to notify you when you have a spike in concurrency. A good idea is to deploy a CloudWatch Alarm that notifies your team when function metrics such as ConcurrentExecutions or Invocations exceeds your threshold. You should create an AWS Budget so you can monitor costs on a daily basis.

If you intend to reuse code in more than one Lambda function, you should consider creating a Lambda Layer for the reusable code - You can configure your Lambda function to pull in additional code and content in the form of layers. A layer is a ZIP archive that contains libraries, a custom runtime, or other dependencies. With layers, you can use libraries in your function without needing to include them in your deployment package. Layers let you keep your deployment package small, which makes development easier. A function can use up to 5 layers at a time.

You can create layers, or use layers published by AWS and other AWS customers. Layers support resource-based policies for granting layer usage permissions to specific AWS accounts, AWS Organizations, or all accounts. The total unzipped size of the function and all layers can't exceed the unzipped deployment package size limit of 250 MB.

Incorrect options:

Lambda allocates compute power in proportion to the memory you allocate to your function. AWS, thus recommends to over provision your function time out settings for the proper performance of Lambda functions - Lambda allocates compute power in proportion to the memory you allocate to your function. This means you can over-provision memory to run your functions faster and potentially reduce your costs. However, AWS recommends that you should not over-provision your function time out settings. Always understand your code performance and set a function time out accordingly. Over-provisioning function timeout often results in Lambda functions running longer than expected and unexpected costs.

The bigger your deployment package, the slower your Lambda function will cold-start. Hence, AWS suggests packaging dependencies as a separate package from the actual Lambda package - This statement is added as a distractor. All the dependencies can be packaged into the single Lambda deployment package without any performance impact.

Serverless databases and Lambda complement each other and you should install databases on the Lambda functions - This statement is incorrect. AWS Lambda does not support installation of databases.

References:

https://aws.amazon.com/blogs/architecture/best-practices-for-developing-on-aws-lambda/

https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

</details>

<a id="q46"></a>

## Q46

<!-- source: U2Q34 · domain: CI · time: 1:51 · first: 124:54 · visits: 2 · changes: 1 -->



After a recent DDoS assault, the IT security team of a media company has asked the Security Engineer to revamp the security of the application to prevent future attacks. The website is hosted on an Amazon EC2 instance and data is maintained on Amazon RDS. A large part of the application data is static and this data is in the form of images.

Which of the following steps can be combined to constitute the revamped security model? (Select two)

- **A.** Use Global Accelerator to distribute traffic
- **B.** Configure the Amazon EC2 instance with an Auto Scaling Group (ASG) to scale in case of a DDoS assault. Front the ASG with AWS Web Application Firewall (AWS WAF) for another layer of security
- **C.** Use Amazon Route 53 to distribute traffic
- **D.** Configure Amazon Inspector with AWS Security Hub to mitigate DDoS attacks by continual scanning that delivers near real-time vulnerability findings
- **E.** Move the static content to Amazon S3, and front this with an Amazon CloudFront distribution. Configure another layer of protection by adding AWS Web Application Firewall (AWS WAF) to the CloudFront distribution

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E · **You picked:** B, E

🔑 **Key words:** after DDoS, EC2 + RDS, static images, revamp security, Select TWO

🪤 **Your trap:** Picked ASG + WAF in front of the ASG; WAF cannot attach to an ASG or EC2 directly (only CloudFront, ALB, API Gateway, AppSync, Cognito). Route 53 adds Shield Standard DNS-layer protection.

🧠 **Rule:** DDoS revamp = Route 53 + CloudFront (static on S3) + WAF on CloudFront/ALB; Shield Standard is built in. WAF never attaches to EC2/ASG.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users ──► ??? ──► EC2 (website) ──► RDS
                   │
                   └── phần lớn là ảnh tĩnh

Sau DDoS: thiết kế lại bảo mật. Chọn 2 bước KẾT HỢP thành một mô hình.
```

Đáp án đúng: **C (Route 53) + E (S3 + CloudFront + WAF)**. Anh chọn B + E: đúng E, sai B.

#### Hai lựa chọn đúng tạo thành một giải pháp

```
DNS query ──► Route 53 (Shield Standard, anycast + shuffle sharding)
                 │
                 ▼
Ảnh tĩnh ──► CloudFront + AWS WAF (rule chạy tại Edge Location) ──► S3
```

- **C - Route 53:** được thiết kế chịu DNS query flood; có sẵn giám sát liên tục và giảm thiểu tấn công hạ tầng (SYN/ACK flood, UDP flood, reflection). Dùng cùng **AWS Shield Standard** (miễn phí cho mọi khách hàng).
- **E - S3 + CloudFront + WAF:** đẩy ảnh tĩnh ra S3 để EC2 không phải phục vụ ảnh; CloudFront hấp thụ traffic tại edge, WAF chặn request xấu **trước khi** chạm web server. Shield Standard + CloudFront + Route 53 cho bảo vệ trước các tấn công hạ tầng layer 3/4.

Hai bước bổ sung nhau: Route 53 bảo vệ lớp DNS, CloudFront + WAF bảo vệ lớp phân phối nội dung.

#### Lựa chọn của anh: B sai ở đâu

B gồm hai nửa:

- "ASG scale khi bị DDoS" nghe hợp lý, nhưng chỉ dùng tiền để nuốt traffic xấu, không chặn nó.
- "Đặt **WAF trước ASG**" mới là chỗ sai cứng. WAF **không gắn trực tiếp** vào EC2 hay ASG.

**WAF chỉ gắn được vào các resource được hỗ trợ:**

```
CloudFront
Application Load Balancer (ALB)
API Gateway (REST)
AWS AppSync
Cognito user pool
App Runner
AWS Verified Access
```

Không có EC2, không có ASG. Muốn dùng WAF cho EC2 trong ASG phải thêm **ALB** phía trước rồi gắn WAF vào ALB. Option B không nhắc ALB nên sai.

Vì sao B trông đúng: ASG + WAF là hai thứ quen thuộc trong bảo mật. Nhưng với loại câu "kết hợp thành một mô hình", mỗi bước phải khả thi; B tự nó không thực hiện được.

#### Các lựa chọn sai còn lại

- **A - Global Accelerator:** tối ưu đường đi và phân phối traffic qua nhiều Region, không phải công cụ giảm thiểu DDoS trong ngữ cảnh đề này.
- **D - Inspector + Security Hub:** Inspector là dịch vụ quét lỗ hổng phần mềm và network exposure của EC2/container. Nó **phát hiện lỗ hổng**, không **giảm thiểu DDoS**.

| Option | Vai trò thật | Giảm thiểu DDoS? |
|---|---|---|
| C. Route 53 | DNS, chịu query flood, Shield Standard | Có |
| E. CloudFront + WAF + S3 | Edge cache, lọc request layer 7 | Có |
| B. ASG + WAF | WAF không gắn được vào ASG | Không khả thi |
| A. Global Accelerator | Điều hướng traffic | Không phải mục tiêu |
| D. Inspector | Quét lỗ hổng | Không |

#### Lưu ý thực tế

- Shield Standard tự động bật cho mọi khách hàng, không cần cấu hình.
- Cần bảo vệ nâng cao (đội DRT, cost protection) thì mới tính đến **Shield Advanced**; đề này không yêu cầu.
- Giữ origin (EC2/ALB) chỉ nhận traffic từ CloudFront thì lớp edge mới thật sự có tác dụng.

#### Quy tắc nhớ cho thi

- **Thấy "DDoS + static content"** → **S3 + CloudFront (+ WAF) + Route 53**.
- **Thấy "WAF" + EC2/ASG** → sai; WAF chỉ gắn **CloudFront, ALB, API Gateway, AppSync, Cognito user pool, App Runner, Verified Access**.
- **Thấy "Inspector" + DDoS** → sai; Inspector quét lỗ hổng.
- **Multi-select "kết hợp"** → mọi pick phải khả thi và cùng góp vào một giải pháp.

### TD explanation

Correct options:

Use Amazon Route 53 to distribute traffic

Move the static content to Amazon S3, and front this with an Amazon CloudFront distribution. Configure another layer of protection by adding AWS Web Application Firewall (AWS WAF) to the CloudFront distribution

AWS WAF is a web application firewall that helps protect web applications from attacks by allowing you to configure rules that allow, block, or monitor (count) web requests based on conditions that you define. These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection, and cross-site scripting.

AWS WAF is tightly integrated with Amazon CloudFront, the Application Load Balancer (ALB), Amazon API Gateway, and AWS AppSync – services that AWS customers commonly use to deliver content for their websites and applications. When you use AWS WAF on Amazon CloudFront, your rules run in all AWS Edge Locations, located around the world close to your end users. Blocked requests are stopped before they reach your web servers.

Route 53 DNS requests and subsequent application traffic routed through CloudFront are inspected inline. Always-on monitoring, anomaly detection, and mitigation against common infrastructure DDoS attacks such as SYN/ACK floods, UDP floods, and reflection attacks are built into both Route 53 and CloudFront.

Route 53 is also designed to withstand DNS query floods, which are real DNS requests that can continue for hours and attempt to exhaust DNS server resources. Route 53 uses shuffle sharding and anycast striping to spread DNS traffic across edge locations and help protect the availability of the service.

When used with Amazon CloudFront distribution, AWS Shield adds security against DDoS attacks.

AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection.

All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. AWS Shield Standard defends against the most common, frequently occurring network and transport layer DDoS attacks that target your website or applications. When you use AWS Shield Standard with Amazon CloudFront and Amazon Route 53, you receive comprehensive availability protection against all known infrastructure (Layer 3 and 4) attacks.

Incorrect options:

Configure the Amazon EC2 instance with an Auto Scaling Group (ASG) to scale in case of a DDoS assault. Front the ASG with AWS Web Application Firewall (AWS WAF) for another layer of security - AWS WAF is tightly integrated with Amazon CloudFront, the Application Load Balancer (ALB), Amazon API Gateway, and AWS AppSync – services that AWS customers commonly use to deliver content for their websites and applications. WAF cannot be directly configured in front of an ASG, so this option is incorrect.

Use Global Accelerator to distribute traffic - Global Accelerator is effective in traffic distribution across AWS Regions. However, the given use case needs services that can help mitigate DDoS attacks.

Configure Amazon Inspector with AWS Security Hub to mitigate DDoS attacks by continual scanning that delivers near real-time vulnerability findings - Amazon Inspector is an automated vulnerability management service that continually scans Amazon Elastic Compute Cloud (EC2) and container workloads for software vulnerabilities and unintended network exposure. It cannot be used to mitigate DDoS attacks.

References:

https://aws.amazon.com/shield/

https://aws.amazon.com/blogs/security/how-to-protect-dynamic-web-applications-against-ddos-attacks-by-using-amazon-cloudfront-and-amazon-route-53/

https://aws.amazon.com/waf/faqs/

</details>

<a id="q59"></a>

## Q59

<!-- source: U2Q37 · domain: MIG · flagged · time: 3:01 · first: 138:35 · visits: 4 · changes: 1 -->



A leading gaming company runs multiple game platforms that need to store game state, player data, session history, and leaderboards. The company is looking to move to AWS Cloud to scale reliably to millions of concurrent users and requests while ensuring consistently low latency measured in single-digit milliseconds. The engineering team at the company is evaluating multiple in-memory data stores with the ability to power its on-demand, live leaderboard. The company's leaderboard requires high availability, low latency, and real-time processing to deliver customizable user data for the community of its users.

As an AWS Certified Solutions Architect Professional, which of the following solutions would you recommend? (Select two)

- **A.** Develop the leaderboard using AWS Neptune as it meets the in-memory, high availability, low latency requirements
- **B.** Develop the leaderboard using DynamoDB with DynamoDB Accelerator (DAX) as it meets the in-memory, high availability, low latency requirements
- **C.** Develop the leaderboard using RDS Aurora as it meets the in-memory, high availability, low latency requirements
- **D.** Develop the leaderboard using DynamoDB as it meets the in-memory, high availability, low latency requirements
- **E.** Develop the leaderboard using ElastiCache Redis as it meets the in-memory, high availability, low latency requirements

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** B, D

🔑 **Key words:** gaming leaderboard, in-memory, single-digit ms, high availability, Select TWO

🪤 **Your trap:** Picked plain DynamoDB; it is disk-based (single-digit ms) but not in-memory. In-memory options are DAX and ElastiCache Redis (sorted sets for leaderboards).

🧠 **Rule:** 'In-memory' in the stem = ElastiCache (Redis sorted sets for leaderboards) or DynamoDB + DAX, not DynamoDB alone.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Game platform ──► Leaderboard (live, real-time)
                   │
   Yêu cầu: IN-MEMORY, high availability, single-digit ms, millions of users
```

Từ khóa quyết định: **"in-memory data stores"**. Đáp án đúng: **B (DynamoDB + DAX) + E (ElastiCache for Redis)**. Anh chọn B + D: đúng B, sai D.

#### Hai lựa chọn đúng

**E - ElastiCache for Redis** là in-memory data store, độ trễ dưới mili giây, dùng đúng cho gaming leaderboard, session store, real-time analytics. Redis có **sorted set**, rất hợp để xếp hạng người chơi theo điểm.

**B - DynamoDB + DAX.** DAX là cache in-memory tương thích DynamoDB, ngồi trước bảng để đọc nhanh hơn. DynamoDB lo tính bền vững và khả dụng cao, DAX đem lại phần "in-memory".

```
Cách 1:  App ──► ElastiCache Redis (sorted set = bảng xếp hạng)

Cách 2:  App ──► DAX (in-memory cache) ──► DynamoDB
```

Mỗi cách đều là một giải pháp in-memory hoàn chỉnh; đề cho chọn hai cách khả thi.

#### Lựa chọn của anh: D sai ở đâu

D nói "DynamoDB meets the in-memory requirement". Phát biểu này **sai**: DynamoDB là database dùng storage bền vững, cho độ trễ single-digit millisecond nhưng **không phải in-memory**. Đề đòi in-memory (và đã nêu ngay trong chính text của option), nên D tự mâu thuẫn.

Vì sao D hấp dẫn: anh nhớ đúng "DynamoDB = single-digit ms", khớp vế độ trễ. Nhưng đề có ba vế (in-memory, HA, low latency) và mọi vế trong option phải đúng. Vế "in-memory" đã làm D rớt.

Quan hệ B và D: B = D + DAX. Chỉ có phần DAX mới thêm "in-memory". Do đó chọn B thì không nên chọn D: D là phiên bản thiếu DAX.

#### Các lựa chọn sai còn lại

- **A - Neptune:** graph database, không phải in-memory.
- **C - Aurora:** relational database (MySQL/PostgreSQL compatible), không phải in-memory.

| Dịch vụ | Loại | In-memory? | Dùng cho leaderboard? |
|---|---|---|---|
| ElastiCache Redis | In-memory store | Có | Có (sorted set) |
| DynamoDB + DAX | NoSQL + in-memory cache | Có (qua DAX) | Có |
| DynamoDB | NoSQL | Không | Không đạt yêu cầu in-memory |
| Aurora | Relational | Không | Không |
| Neptune | Graph | Không | Không |

#### Lưu ý thực tế

- DAX tối ưu cho tải **đọc nhiều**; ghi vẫn đi qua tới DynamoDB.
- Với Redis, bảng xếp hạng thường dùng lệnh `ZADD` / `ZREVRANGE` trên sorted set.

#### Quy tắc nhớ cho thi

- **Thấy "in-memory"** → **ElastiCache** hoặc **DynamoDB + DAX**.
- **Thấy "leaderboard"** → **Redis sorted set**.
- **DynamoDB đứng một mình** → "single-digit ms" nhưng **không** in-memory.
- **Multi-select** → mỗi option phải thỏa MỌI vế của đề, không chỉ vế độ trễ.

### TD explanation

Correct options:

Develop the leaderboard using ElastiCache Redis as it meets the in-memory, high availability, low latency requirements

Amazon ElastiCache for Redis is a blazing fast in-memory data store that provides sub-millisecond latency to power internet-scale real-time applications. Amazon ElastiCache for Redis is a great choice for real-time transactional and analytical processing use cases such as caching, chat/messaging, gaming leaderboards, geospatial, machine learning, media streaming, queues, real-time analytics, and session store.
ElastiCache for Redis can be used to power the live leaderboard, so this option is correct.

ElastiCache for Redis Overview:


Develop the leaderboard using DynamoDB with DynamoDB Accelerator (DAX) as it meets the in-memory, high availability, low latency requirements

Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multi-Region, multi-master, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications.

DAX is a DynamoDB-compatible caching service that enables you to benefit from fast in-memory performance for demanding applications. So DynamoDB with DAX can be used to power the live leaderboard.

DAX Overview:

via - https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.html

Incorrect options:

Develop the leaderboard using AWS Neptune as it meets the in-memory, high availability, low latency requirements - Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. Neptune is not an in-memory database, so this option is not correct.

Develop the leaderboard using DynamoDB as it meets the in-memory, high availability, low latency requirements - DynamoDB is not an in-memory database, so this option is not correct.

Develop the leaderboard using RDS Aurora as it meets the in-memory, high availability, low latency requirements - Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. Amazon Aurora features a distributed, fault-tolerant, self-healing storage system that auto-scales up to 64TB per database instance. Aurora is not an in-memory database, so this option is not correct.

References:

https://aws.amazon.com/elasticache/

https://aws.amazon.com/elasticache/redis/

https://aws.amazon.com/dynamodb/dax/

</details>

<a id="q63"></a>

## Q63

<!-- source: U2Q56 · domain: ORG · flagged · time: 3:52 · first: 144:05 · visits: 7 · changes: 1 -->



A healthcare technology solutions company recently faced a security event resulting in an S3 bucket with sensitive data containing Personally Identifiable Information (PII) for patients being made public. The company policy mandates never to have public S3 objects so the Governance and Compliance team must be notified immediately as soon as any public objects are identified. The company has hired you as an AWS Certified Solutions Architect Professional to help build a solution that detects the presence of a public S3 object, which in turn sets off an alarm to trigger notifications and then automatically remediates the said object.

Which of the following solutions would you implement in tandem to meet the requirements of the given use-case? (Select two)

- **A.** Enable object-level logging for S3. When a PutObject API call is made with a public-read permission, use S3 event notifications to trigger a Lambda that sends a notification via SNS
- **B.** Leverage AWS Trusted Advisor to check for S3 bucket public-read permissions and invoke a Lambda function to send a notification via SNS as soon as a public object is uploaded
- **C.** Configure a Lambda function as one of the SNS topic subscribers, which is invoked to secure the objects in the S3 bucket
- **D.** Leverage AWS Access Analyzer to check for S3 bucket public-read permissions and invoke a Lambda function to send a notification via SNS as soon as a public object is uploaded
- **E.** Enable object-level logging for S3. Set up a EventBridge event pattern when a PutObject API call with public-read permission is detected in the AWS CloudTrail logs and set the target as an SNS topic for downstream notifications

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E · **You picked:** A, C

🔑 **Key words:** detect public S3 object, alarm, notify, auto-remediate, Select TWO

🪤 **Your trap:** 🔁 Picked S3 event notifications; they fire on object creation but cannot filter by ACL (public-read). CloudTrail data events + EventBridge pattern on PutObject with public-read can.

🧠 **Rule:** Detect an API parameter (ACL, encryption flag) = CloudTrail data events + EventBridge rule → SNS → Lambda remediates. S3 event notifications only know event type and key prefix/suffix.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Upload object ──► S3 bucket
                    │  (PutObject với ACL public-read?)
                    ▼
        PHÁT HIỆN ──► CẢNH BÁO ──► TỰ ĐỘNG SỬA
```

Ba yêu cầu: **detect** object public, **notify** ngay, **auto-remediate**. Đáp án đúng: **E + C**. Anh chọn A + C: đúng C, sai A.

#### Hai lựa chọn đúng tạo thành MỘT pipeline

```
S3 PutObject (public-read)
   │  CloudTrail data events (object-level logging)
   ▼
EventBridge rule (pattern: PutObject + public-read)
   ▼
SNS topic ──┬──► Email / SMS  (báo Governance & Compliance)
            └──► Lambda subscriber (sửa object, bỏ public)
```

- **E** làm phần **detect + notify**: bật object-level logging để CloudTrail ghi data events (mặc định trail không ghi data events), rồi EventBridge rule khớp API call `PutObject` có public-read, target là SNS.
- **C** làm phần **remediate**: Lambda là subscriber của SNS topic, chạy code để bảo mật lại object.

Hai option phụ thuộc nhau: C một mình không có gì kích hoạt SNS; E một mình chỉ báo, không sửa. Cần cả hai mới đủ ba yêu cầu.

#### Lựa chọn của anh: A sai ở đâu

A: bật object-level logging, rồi dùng **S3 event notifications** trigger Lambda khi `PutObject` có public-read.

S3 event notification chỉ cho chọn **loại sự kiện** (ví dụ `s3:ObjectCreated:Put` hoặc `s3:ObjectCreated:*`) và lọc theo prefix/suffix. Nó **không kiểm tra được ACL** của lần upload. Nên không thể tách "upload public" khỏi "upload bình thường".

Chi tiết dễ nhầm: câu "bật object-level logging" trong A không cứu được. Logging đẩy sang CloudTrail, còn S3 event notification là cơ chế riêng, không đọc CloudTrail. Option ghép hai thứ rời nhau.

⚠️ Lỗi lặp lại

Đây là lỗi anh đã gặp trước đó: chọn S3 event notifications cho yêu cầu phải nhìn vào **tham số của API call** (ACL, cờ mã hóa). Quy luật cần khắc cốt:

```
Cần biết GÌ ĐƯỢC TRUYỀN trong API call (ACL, encryption...)
        → CloudTrail + EventBridge
Chỉ cần biết CÓ object mới / bị xóa / theo prefix
        → S3 event notification
```

#### Các lựa chọn sai còn lại

- **B - Trusted Advisor:** chỉ kiểm tra bucket có open access, thông báo bằng email **hàng tuần** khi opt-in. Không phải near real-time, không báo ngay khi có object public.
- **D - Access Analyzer:** cho finding về bucket được chia sẻ/public, nhưng không near real-time cho object mới upload, và không invoke Lambda trực tiếp; finding xem trong console hoặc tải CSV.

| Cách | Near real-time? | Thấy được ACL public-read? | Auto-remediate? |
|---|---|---|---|
| **E. CloudTrail + EventBridge + SNS** | Có | Có | Qua subscriber |
| **C. Lambda subscribe SNS** | Có | - | Có |
| A. S3 event notification | Có | Không | - |
| B. Trusted Advisor | Không (hàng tuần) | Mức bucket | Không |
| D. Access Analyzer | Không | Mức bucket/finding | Không trực tiếp |

#### Lưu ý thực tế

📝 Ghi chú kỹ thuật: ngoài đời, cách phòng ngừa tốt hơn là **S3 Block Public Access** (chặn từ gốc), và bucket mới mặc định đã tắt ACL (Object Ownership = bucket owner enforced). Nhưng đề hỏi pipeline phát hiện + sửa tự động, nên giữ đáp án E + C.

- Data events của CloudTrail **tính phí riêng** và mặc định tắt; muốn dùng EventBridge cho object-level phải bật trước.

#### Quy tắc nhớ cho thi

- **Thấy "detect API call có tham số X" (public-read, encryption)** → **CloudTrail data events + EventBridge**.
- **S3 event notification** → chỉ biết loại event + prefix/suffix, **không** biết ACL.
- **"Notify + auto-remediate"** → **SNS** có cả email/SMS lẫn **Lambda subscriber**.
- **Trusted Advisor / Access Analyzer** → không near real-time, không phải bộ kích hoạt tự động.
- **Multi-select** → các pick phải ghép thành một chuỗi detect → notify → fix; sai một mắt xích là sai cả.

### TD explanation

Correct options:

Configure a Lambda function as one of the SNS topic subscribers, which is invoked to secure the objects in the S3 bucket

Enable object-level logging for S3. Set up a EventBridge event pattern when a PutObject API call with public-read permission is detected in the AWS CloudTrail logs and set the target as an SNS topic for downstream notifications

You can enable object-level logging for an S3 bucket to send logs to CloudTrail for object-level API operations such as GetObject, DeleteObject, and PutObject. These events are called data events. By default, CloudTrail trails don't log data events, but you can configure trails to log data events for S3 buckets that you specify, or to log data events for all the Amazon S3 buckets in your AWS account.


via - https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-cloudtrail-events.html

You need to further configure a EventBridge event-pattern based rule to analyze the CloudTrail logs for S3 PutObject API call with public-read permissions. The target for this rule can be set as an SNS topic. The SNS would send the notification via an email or SMS as soon as a public object is detected. Moreover, the SNS topic is also subscribed by a Lambda function which runs custom code to secure the objects in the S3 bucket.


via - https://docs.aws.amazon.com/sns/latest/dg/welcome.html

Incorrect options:

Enable object-level logging for S3. When a PutObject API call is made with a public-read permission, use S3 event notifications to trigger a Lambda that sends a notification via SNS - S3 event notification allows you to receive notifications when certain events happen in your bucket. To enable notifications, you must first add a notification configuration that identifies the events you want Amazon S3 to publish and the destinations where you want Amazon S3 to send the notifications. S3 can publish notifications for the new object create events.

You can request notification when only a specific API is used (for example, s3:ObjectCreated:Put), or you can use a wildcard (for example, s3:ObjectCreated:*), however, you cannot check if the API call was made with a public-read permission. So, this option is incorrect.


via - https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html

Leverage AWS Trusted Advisor to check for S3 bucket public-read permissions and invoke a Lambda function to send a notification via SNS as soon as a public object is uploaded - Trusted Advisor is an application that inspects your AWS environment and makes recommendations for saving money, improving system performance, or closing security gaps. The Trusted Advisor notification feature helps you stay up-to-date with your AWS resource deployment. However, you will only be notified by weekly email when you opt-in for this service, so this does not meet the key requirement for the use-case wherein the notification should be sent as soon as a public object is uploaded. Also, Trusted Advisor just checks buckets in Amazon Simple Storage Service (Amazon S3) that have open access permissions. It cannot be used for near real-time detection of a new public object uploaded on S3.


via - https://aws.amazon.com/premiumsupport/faqs/

Leverage AWS Access Analyzer to check for S3 bucket public-read permissions and invoke a Lambda function to send a notification via SNS as soon as a public object is uploaded - You can use AWS Access Analyzer to receive findings into the source and level of public or shared access for each public or shared bucket. For example, Access Analyzer for S3 might show that a bucket has read or write access provided through a bucket access control list (ACL), a bucket policy, or an access point policy. It cannot be used for near real-time detection of a new public object uploaded on S3. Additionally, you cannot invoke a Lambda function from Access Analyzer. The findings for Access Analyzer are available within the AWS Console or they can be downloaded in a CSV report.


via - https://docs.aws.amazon.com/AmazonS3/latest/user-guide/access-analyzer.html

References:

https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-cloudtrail-events.html

https://docs.aws.amazon.com/sns/latest/dg/welcome.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html

https://aws.amazon.com/premiumsupport/faqs/

https://docs.aws.amazon.com/AmazonS3/latest/user-guide/access-analyzer.html

</details>

---

# Group C — Hybrid / migration path: wrong connectivity or migration strategy for the constraint (4)

<a id="q19"></a>

## Q19

<!-- source: U2Q1 · domain: MIG · flagged · time: 2:29 · first: 16:54 · visits: 2 · changes: 0 -->



The DevOps team at a leading social media company uses Chef to automate the configurations of servers in the on-premises data center. The CTO at the company now wants to migrate the IT infrastructure to AWS Cloud with minimal changes to the server configuration workflows and at the same time account for less operational overhead post-migration to AWS. The company has hired you as an AWS Certified Solutions Architect Professional to recommend a solution for this migration.

Which of the following solutions would you recommend to address the given use-case?

- **A.** Replatform the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS
- **B.** Replatform the IT infrastructure to AWS Cloud by leveraging AWS Config as a configuration management service to automate the configurations of servers on AWS
- **C.** Rehost the IT infrastructure to AWS Cloud by leveraging AWS OpsWorks as a configuration management service to automate the configurations of servers on AWS
- **D.** Rehost the IT infrastructure to AWS Cloud by leveraging AWS Elastic Beanstalk as a configuration management service to automate the configurations of servers on AWS

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** on-prem Chef, minimal change to config workflow, less operational overhead, replatform

🪤 **Your trap:** AWS Config audits configuration; it does not run Chef recipes. Dated question: OpsWorks reached end of life in 2024.

🧠 **Rule:** Keep Chef/Puppet with managed server = OpsWorks (legacy answer). Today: Systems Manager State Manager or self-managed Chef. Config = compliance audit, not config management.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises DC                          AWS Cloud
┌────────────────────────┐              ┌────────────────────────┐
│ Server + Chef recipes  │   ──────►    │ EC2 + cấu hình bằng ?  │
│ (tự vận hành Chef      │              │ (giữ workflow Chef,    │
│  server)               │              │  ít vận hành hơn)      │
└────────────────────────┘              └────────────────────────┘
 Yêu cầu: ÍT thay đổi workflow cấu hình + ÍT operational overhead
```

Hai chữ khóa quyết định: **"minimal changes to the server configuration workflows"** (giữ Chef) và **"less operational overhead"** (dịch vụ managed, không tự chạy Chef server). Đáp án đúng: **A (Replatform + AWS OpsWorks)**. Anh chọn B (AWS Config).

#### Đáp án A đúng - Replatform + OpsWorks

**Replatform** = không đổi kiến trúc cốt lõi nhưng tận dụng một vài tối ưu của cloud (ở đây: thay Chef server tự vận hành bằng dịch vụ managed). **Rehost** = lift-and-shift y nguyên, không tối ưu gì.

**OpsWorks** cho phép dùng Chef/Puppet để tự động hóa cấu hình, deploy, quản lý server trên EC2 hoặc on-premises. Với Chef, **OpsWorks for Chef Automate** là Chef server managed hoàn toàn, tương thích đầy đủ với Chef (cookbook/recipe, community tooling) nên team giữ nguyên workflow, nhưng không phải vận hành Chef server.

```
Chef recipes cũ ──► OpsWorks for Chef Automate (managed) ──► EC2 nodes
   (giữ nguyên)         (hết việc patch/backup/HA Chef server)
```

#### Phương án anh chọn - B (AWS Config)

Nhìn thấy chữ "configuration" nên dễ nghĩ AWS Config quản lý cấu hình server. Thực tế **AWS Config chỉ đánh giá, audit, ghi lại lịch sử cấu hình của resource AWS** (trả lời câu "resource này trông thế nào lúc xyz?", kiểm tra compliance theo rule). Nó **không chạy recipe, không cấu hình bên trong server**. Config = "camera giám sát", không phải "thợ cài đặt".

#### Các phương án còn lại

- **C (Rehost + OpsWorks):** sai chiến lược. Có dùng dịch vụ managed thay Chef server là đã có tối ưu cloud nên là Replatform, không phải Rehost (as-is).
- **D (Rehost + Elastic Beanstalk):** sai cả chiến lược lẫn công cụ. Beanstalk deploy và quản lý **ứng dụng** (capacity, load balancing, auto scaling, health), không phải công cụ configuration management chạy Chef recipes.

| Phương án | Chiến lược | Công cụ | Vấn đề |
|---|---|---|---|
| **A** | Replatform | OpsWorks (Chef managed) | Đúng |
| B | Replatform | AWS Config | Config chỉ audit, không tự động hóa cấu hình |
| C | Rehost | OpsWorks | Sai chiến lược |
| D | Rehost | Elastic Beanstalk | Sai chiến lược và sai công cụ |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** câu hỏi này đã lỗi thời. **AWS OpsWorks đã hết vòng đời** (OpsWorks for Chef Automate và Puppet Enterprise ngừng từ 2023, OpsWorks Stacks ngừng năm 2024), nên hiện nay không còn dựng mới được như đáp án A mô tả. Tương đương ngày nay:

- **AWS Systems Manager** (State Manager, Run Command, Automation) để áp cấu hình lên EC2 và cả server on-premises. Systems Manager có document để chạy Chef recipe (ví dụ `AWS-ApplyChefRecipes`), nên có thể giữ cookbook cũ.
- **Chef tự quản (self-managed)**: chạy Chef Infra Server trên EC2 hoặc dùng Chef SaaS của hãng. Giữ nguyên workflow nhưng quay lại gánh vận hành server Chef.

Trong bài thi vẫn giữ **đáp án A**, vì đề phản ánh thời điểm OpsWorks còn hoạt động. Phần lý luận Replatform vs Rehost vẫn đúng.

#### Quy tắc nhớ cho thi

- **Thấy "Chef/Puppet hiện có, giữ workflow, ít vận hành"** → **OpsWorks** (đáp án cũ); thực tế ngày nay: Systems Manager hoặc Chef tự quản
- **Thấy "AWS Config"** → **audit/compliance/lịch sử cấu hình resource**, không bao giờ là công cụ cấu hình server
- **Thấy "Elastic Beanstalk"** → deploy ứng dụng, không phải configuration management
- **Rehost** = as-is; **Replatform** = đổi vài thành phần sang managed service mà không đổi kiến trúc

### TD explanation

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

</details>

<a id="q65"></a>

## Q65

<!-- source: U2Q15 · domain: MIG · flagged · time: 2:29 · first: 75:28 · visits: 2 · changes: 0 -->



A web development studio runs hundreds of Proof-of-Concept (PoC) and demo applications on virtual machines running on an on-premises server. Many of the applications are simple PHP, JavaScript or Python web applications which are no longer actively developed and serve little traffic.

As a Solutions Architect Professional, which of the following approaches would you suggest to migrate these applications to AWS with the lowest infrastructure cost and least development effort?

- **A.** Leverage VM Import/Export to create AMIs for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image
- **B.** Leverage AWS Server Migration Service (SMS) to create AMIs for each virtual machine and run each application on a dedicated EC2 instance
- **C.** Dockerize each application and then deploy to an ECS cluster running behind an Application Load Balancer
- **D.** Migrate the application code to use a serverless stack comprising of Lambda functions and DynamoDB

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** hundreds of PoC PHP/JS/Python apps, little traffic, lowest infra cost, least development effort

🪤 **Your trap:** Picked rewrite to Lambda + DynamoDB; that is a refactor with large dev effort (PHP not native in Lambda). One EC2/Beanstalk per app wastes cost.

🧠 **Rule:** Many small idle apps, cheap + little effort = containerize and bin-pack on ECS behind one ALB (dynamic port mapping).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem server (VM)                         AWS
┌──────────────────────────┐                ┌──────────────────────────┐
│ VM1: PHP demo   (ít tải) │                │                          │
│ VM2: JS demo    (ít tải) │   ───────►     │   ??? chạy hàng trăm app │
│ VM3: Python PoC (ít tải) │                │                          │
│ ... hàng trăm app        │                └──────────────────────────┘
└──────────────────────────┘
 Yêu cầu: chi phí hạ tầng THẤP NHẤT + công sức dev ÍT NHẤT
```

Hai ràng buộc kéo ngược nhau: **rẻ** (không dùng một máy cho mỗi app) và **ít sửa code** (không viết lại). Đáp án đúng: **C (Dockerize + ECS sau ALB)**. Anh chọn D (viết lại sang Lambda + DynamoDB).

#### Đáp án C đúng - Docker + ECS + ALB

Mỗi app đóng gói thành Docker image (hầu như không sửa code) rồi **bin-pack** nhiều container lên ít EC2 instance:

```
                ┌─────────────── ECS cluster (vài EC2) ───────────────┐
Users ─► ALB ─► │ EC2 #1: [app1:32768] [app2:32769] [app3:32770] ...  │
                │ EC2 #2: [app4:32768] [app5:32769] ...               │
                └──────────────────────────────────────────────────────┘
```

Mấu chốt là **dynamic host port mapping** của ALB: nhiều task của cùng một service chạy trên một container instance, mỗi task một port host ngẫu nhiên, ALB route theo target group/rule. Kết quả: **số EC2 cần dùng giảm mạnh**, nên chi phí giảm. App ít traffic nên dồn chung rất hợp, và một ALB phục vụ nhiều app qua listener rule.

#### Phương án anh chọn - D (Lambda + DynamoDB)

Trông "serverless nên rẻ khi ít traffic", nhưng sai ở vế **least development effort**:

- Phải **viết lại** từng app sang kiến trúc hàm + DynamoDB. Đây là Refactor, tốn công sức lớn cho hàng trăm app.
- Một số app (PHP) **không có runtime native trên Lambda**, chỉ chạy được qua custom runtime.
- DB hiện tại có thể là quan hệ, đổi sang DynamoDB kéo theo thiết kế lại dữ liệu.

#### Các phương án còn lại

- **A (VM Import/Export + Elastic Beanstalk single-instance):** single-instance không có load balancer nên rẻ hơn mức tải cân bằng, nhưng vẫn là **một EC2 cho mỗi app**. Hàng trăm app = hàng trăm instance, tốn kém.
- **B (SMS tạo AMI + một EC2 riêng cho mỗi app):** cùng vấn đề, một instance mỗi app. SMS chỉ lo việc replicate VM thành AMI.

| Phương án | Số EC2 | Công sức dev | Kết luận |
|---|---|---|---|
| A. Beanstalk single-instance | Một per app | Thấp | Đắt |
| B. SMS + EC2 per app | Một per app | Thấp | Đắt |
| **C. ECS + ALB** | **Rất ít (bin-pack)** | **Thấp (Dockerize)** | **Rẻ và ít việc** |
| D. Lambda + DynamoDB | Không có | Rất cao (viết lại) | Vi phạm "least effort" |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** **AWS Server Migration Service (SMS) đã ngừng hoạt động**, được thay bằng **AWS Application Migration Service (MGN)**. Với đề thi cũ, SMS vẫn xuất hiện như phương án "lift-and-shift VM".

- Bin-pack chạy bằng ECS trên EC2 dùng được dynamic port mapping với ALB. Nếu muốn bỏ luôn việc quản lý instance, Fargate là hướng khác nhưng tính tiền theo task, không còn lợi thế dồn chung instance.
- Dồn nhiều app lên cùng instance nghĩa là cần đặt CPU/memory reservation hợp lý cho từng task.

#### Quy tắc nhớ cho thi

- **Thấy "hàng trăm app nhỏ, ít traffic, rẻ nhất, ít công sức"** → **Dockerize + ECS + ALB** (nhiều container trên ít instance, dynamic port mapping)
- **Thấy "mỗi app một EC2 / một Beanstalk env"** → đắt, loại
- **Thấy "viết lại sang Lambda/DynamoDB"** khi đề nhấn **least development effort** → loại (refactor)
- **PHP + Lambda** → không native, cần custom runtime

### TD explanation

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

</details>

<a id="q67"></a>

## Q67

<!-- source: U2Q4 · domain: ORG · flagged · time: 3:48 · first: 80:28 · visits: 3 · changes: 1 -->



The CTO at a multi-national retail company is pursuing an IT re-engineering effort to set up a hybrid network architecture that would facilitate the company's envisaged long-term data center migration from multiple on-premises data centers to the AWS Cloud. The current on-premises data centers are in different locations and are inter-linked via a private fiber. Due to the unique constraints of the existing legacy applications, using NAT is not an option. During the migration period, many critical applications will need access to other applications deployed in both the on-premises data centers and AWS Cloud.

As a Solutions Architect Professional, which of the following options would you suggest to set up a hybrid network architecture that is highly available and supports high bandwidth for a multi-Region deployment post-migration?

- **A.** Set up multiple hardware VPN connections between AWS cloud and the on-premises data centers. Configure each subnet's traffic through different VPN connections for redundancy. Make sure that no VPC CIDR blocks overlap one another or the on-premises network
- **B.** Set up a Direct Connect as primary connection for all on-premises data centers with another VPN as backup. Configure both connections to use the same virtual private gateway and BGP. Make sure that no VPC CIDR blocks overlap one another or the on-premises network
- **C.** Set up multiple software VPN connections between AWS cloud and the on-premises data centers. Configure each subnet's traffic through different VPN connections for redundancy. Make sure that no VPC CIDR blocks overlap one another or the on-premises network
- **D.** Set up a Direct Connect to each on-premises data center from different service providers and configure routing to failover to the other on-premises data center's Direct Connect in case one connection fails. Make sure that no VPC CIDR blocks overlap one another or the on-premises network

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** multiple on-prem DCs linked by private fiber, no NAT, HA, high bandwidth, multi-Region

🪤 **Your trap:** Changed the right answer (Direct Connect at each DC from different providers) to DX + VPN backup during review. VPN backup is low bandwidth and the single-VGW design is not multi-Region.

🧠 **Rule:** HA + high bandwidth hybrid = redundant Direct Connect (diverse providers/locations) with failover across DCs. VPN backup only when cost beats bandwidth.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
DC A ══ private fiber ══ DC B ══ private fiber ══ DC C
 │                        │                        │
 │ DX (provider 1)        │ DX (provider 2)        │ DX (provider 3)
 ▼                        ▼                        ▼
┌──────────────────── AWS (multi-Region) ─────────────────────┐
│   VPC CIDR không trùng nhau, không trùng on-prem (không NAT)│
└─────────────────────────────────────────────────────────────┘
 Yêu cầu: HA + băng thông CAO + multi-Region, không dùng NAT
```

Đáp án đúng: **D (Direct Connect riêng cho từng data center, khác provider, failover sang DX của DC khác)**. Anh chọn B (DX chính + VPN dự phòng). Ban đầu anh đã chọn đúng D, rồi đổi sang B trong lúc review cờ.

#### Đáp án D đúng

- **Direct Connect** cho băng thông cao, ổn định, không qua internet công cộng (dedicated 1/10 Gbps, hosted từ 50 Mbps đến 10 Gbps).
- **Mỗi data center một DX, qua nhà cung cấp khác nhau**: tránh single point of failure ở provider hay ở thiết bị. Đây là mô hình **maximum resiliency** (kết nối riêng, nhà cung cấp khác nhau, kết thúc trên thiết bị tách biệt, ở nhiều location).
- Các DC nối với nhau bằng **private fiber** sẵn có, nên khi DX của DC này hỏng, traffic có thể đi vòng qua fiber sang DC khác và ra bằng DX của DC đó (failover bằng routing).
- "Không NAT" nghĩa là các dải địa chỉ phải **không chồng lấn** nhau, nên đáp án nào cũng kèm câu "no overlapping CIDR".

```
DX hỏng ở DC A:  A ──fiber──► B ──DX(provider 2)──► AWS
```

#### Phương án anh chọn - B (một DX + VPN backup)

Nhìn như thiết kế HA kinh điển, nhưng sai hai điểm theo TD:

1. **Không thể dùng một DX duy nhất cho nhiều data center ở các địa điểm khác nhau.** Mỗi DC cần đường kết nối vật lý riêng đến một DX location.
2. **VPN backup không đáp ứng "high bandwidth"**: VPN đi qua internet công cộng, băng thông hạn chế và không ổn định. Khi DX sập, chất lượng tụt hẳn so với yêu cầu.

Thêm nữa, dùng một VGW duy nhất không thể hiện được yêu cầu multi-Region.

#### Các phương án còn lại

- **A (nhiều hardware VPN):** VPN chạy trên internet, không hỗ trợ băng thông cao. Chỉ hợp khi cần nhanh và nhu cầu băng thông thấp đến vừa.
- **C (nhiều software VPN trên EC2):** cùng hạn chế như A, lại thêm gánh vận hành appliance.

| Phương án | Băng thông | HA | Vấn đề |
|---|---|---|---|
| A. Hardware VPN | Thấp | Có | Qua internet |
| B. 1 DX + VPN | Cao rồi tụt khi failover | Một phần | 1 DX cho nhiều DC, backup yếu |
| C. Software VPN | Thấp | Có | Qua internet + vận hành appliance |
| **D. DX mỗi DC, khác provider** | **Cao** | **Cao** | Đúng yêu cầu |

#### Bài học khi review câu đã flag

⚠️ Anh đã có câu trả lời đúng ngay lần đầu, rồi đổi sang sai mà **không có bằng chứng mới**. Phần lớn lần đổi đáp án vì "có vẻ an toàn hơn" (ở đây: DX + VPN backup quen thuộc) chỉ là cảm giác, không phải lý do.

- Khi review, chỉ đổi đáp án nếu tìm ra **một từ khóa cụ thể trong đề** mà lựa chọn ban đầu vi phạm, hoặc nhớ ra một **fact cụ thể** (ví dụ "một DX không phục vụ được nhiều location").
- Nếu không chỉ ra được lý do đó bằng một câu, giữ nguyên đáp án ban đầu.
- Trước khi đổi, hãy tự hỏi: "Từ khóa nào trong đề bác bỏ đáp án đầu của mình?"

#### Lưu ý thực tế

- Đề nói **multi-Region**: trong thực tế, một DX có thể tiếp cận VPC ở nhiều Region thông qua **Direct Connect gateway**, thay vì chỉ gắn một VGW cho một VPC.
- Mô hình DX + VPN backup là thiết kế **hợp lệ** khi ưu tiên chi phí hơn băng thông. Đề này nhấn HA và high bandwidth nên không dùng.

#### Quy tắc nhớ cho thi

- **Thấy "HA + high bandwidth + hybrid"** → **nhiều Direct Connect dự phòng** (khác provider, khác location), không phải VPN
- **Thấy "VPN"** khi đề cần bandwidth cao → loại (internet công cộng)
- **Thấy "không NAT"** → CIDR không được trùng nhau
- **Thấy "DX + VPN backup"** → chỉ đúng khi đề nhấn **cost**, không phải high bandwidth
- **Review flag:** đổi đáp án chỉ khi có **từ khóa/fact mới**, không đổi theo cảm giác

### TD explanation

Correct option:

Set up a Direct Connect to each on-premises data center from different service providers and configure routing to failover to the other on-premises data center's Direct Connect in case one connection fails. Make sure that no VPC CIDR blocks overlap one another or the on-premises network

AWS Direct Connect links your on-premises data center to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. With this connection, you can create virtual interfaces directly to public AWS services (for example, to Amazon S3) or to Amazon VPC, bypassing internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the Region with which it is associated.

There are two types of Direct Connect connections:

Dedicated Connection: A physical Ethernet connection associated with a single customer. Customers can request a dedicated connection through the AWS Direct Connect console, the CLI, or the API. This supports speed of 1Gbps and 10Gbps.

Hosted Connection: A physical Ethernet connection that an AWS Direct Connect Partner provisions on behalf of a customer. Customers request a hosted connection by contacting a partner in the AWS Direct Connect Partner Program, who provisions the connection. This supports speed of 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps.


via - https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

As the use-case requires a hybrid network architecture that is highly available and supports high bandwidth, therefore you should configure the Direct Connect based hybrid network to achieve maximum resiliency for critical workloads by using separate connections from different service providers that terminate on separate devices in more than one location.


via - https://docs.aws.amazon.com/directconnect/latest/UserGuide/maximum_resiliency.html


via - https://docs.aws.amazon.com/directconnect/latest/UserGuide/high_resiliency.html

Incorrect options:

Set up multiple hardware VPN connections between AWS cloud and the on-premises data centers. Configure each subnet's traffic through different VPN connections for redundancy. Make sure that no VPC CIDR blocks overlap one another or the on-premises network

Set up multiple software VPN connections between AWS cloud and the on-premises data centers. Configure each subnet's traffic through different VPN connections for redundancy. Make sure that no VPC CIDR blocks overlap one another or the on-premises network

A VPN connection refers to the connection between your VPC and your own on-premises network. Site-to-Site VPN supports Internet Protocol security (IPsec) VPN connections. VPNs on AWS come in three flavours: hardware only, software only and a mix of hardware/software. The hardware only VPN uses a hardware VPN device to connect the virtual private gateway on the AWS end to a customer VPN gateway on the customers end, via IPsec VPN tunnels.

Hardware only VPNs include both the AWS managed AWS Site-to-Site VPN solution and the AWS VPN CloudHub.

You can also create a VPN connection to your remote network by using an Amazon EC2 instance in your VPC that's running a third party software VPN appliance.

The limitation with both options is that VPNs do not support high bandwidth data transfer as these operate over the public internet infrastructure. VPN Connections are a good solution if you have an immediate need, and have low to modest bandwidth requirements.


via - https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html

Set up a Direct Connect as primary connection for all on-premises data centers with another VPN as backup. Configure both connections to use the same virtual private gateway and BGP. Make sure that no VPC CIDR blocks overlap one another or the on-premises network - This option has been added as a distractor as you cannot have just one Direct Connect connection for multiple on-premises data centers that are in different locations. Also having a VPN as a backup does not provide a high-bandwidth and high-availability fallback option.

References:

https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

https://docs.aws.amazon.com/directconnect/latest/UserGuide/maximum_resiliency.html

https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html

https://medium.com/@datapath_io/aws-direct-connect-vs-vpn-vs-direct-connect-gateway-97900cdf7d04

</details>

<a id="q68"></a>

## Q68

<!-- source: U2Q72 · domain: MIG · flagged · time: 3:14 · first: 83:16 · visits: 3 · changes: 0 -->



An e-commerce company runs a data archival workflow once a month for its on-premises data center which is connected to the AWS Cloud over a minimally used 10-Gbps Direct Connect connection using a private virtual interface to its virtual private cloud (VPC). The company internet connection is 200 Mbps, and the usual archive size is around 140 TB that is created on the first Friday of a month. The archive must be transferred and available in Amazon S3 by the next Monday morning.

As a Solutions Architect Professional, which of the following options would you recommend as the LEAST expensive way to address the given use-case?

- **A.** Configure a public virtual interface on the 10-Gbps Direct Connect connection and then copy the data to S3 over the connection
- **B.** Configure a private virtual interface on the 10-Gbps Direct Connect connection and then copy the data securely to S3 over the connection
- **C.** Order multiple AWS Snowball Edge appliances, transfer the data in parallel to these appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3
- **D.** Configure a VPC endpoint for S3 and then leverage the Direct Connect connection for data transfer with VPC endpoint as the target

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** 140 TB monthly, 10 Gbps DX with private VIF, 200 Mbps internet, by Monday, LEAST expensive, S3

🪤 **Your trap:** 🔁 Picked an S3 VPC endpoint over the private VIF; a gateway endpoint is not reachable from on-premises. S3 public endpoints need a public VIF on the same DX (no extra hardware).

🧠 **Rule:** On-prem → S3 over Direct Connect = public VIF (cheapest, uses existing DX). Private VIF reaches only VPC resources (or an S3 interface endpoint, newer option).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem DC                                      AWS
┌─────────────┐   10 Gbps Direct Connect        ┌───────────┐
│ Archive     │ ═══ (private VIF hiện có) ════► │ VPC       │
│ 140 TB      │                                 └───────────┘
│ (thứ Sáu)   │ ─── Internet 200 Mbps ────────► Amazon S3  <── đích
└─────────────┘
 Yêu cầu: có trên S3 trước sáng thứ Hai, chi phí THẤP NHẤT
```

Đáp án đúng: **A (tạo public VIF trên DX 10 Gbps sẵn có, copy thẳng lên S3)**. Anh chọn D (S3 VPC endpoint qua DX).

#### Bài toán băng thông - chọn đường truyền nào?

Đổi đơn vị: 140 TB = 1.120.000 Gb (1 byte = 8 bit).

| Đường truyền | Công thức | Thời gian |
|---|---|---|
| **DX 10 Gbps** | 1.120.000 Gb / 10 Gbps = 112.000 giây | **khoảng 31 giờ** |
| Internet 200 Mbps | 1.120.000 Gb / 0,2 Gbps = 5.600.000 giây | **khoảng 65 ngày** |

TD tính thận trọng hơn: 10 Gbps xấp xỉ 1 GB/s, tức 3,6 TB/giờ, khoảng 86 TB/ngày, nên 140 TB mất khoảng 39 giờ, vẫn dưới 48 giờ. Dù tính cách nào, cửa sổ từ chiều thứ Sáu đến sáng thứ Hai **đủ** cho DX 10 Gbps (đang "minimally used"), còn internet 200 Mbps thì **không thể**.

Kết luận: phải dùng **DX sẵn có** (không phát sinh phần cứng), vấn đề còn lại là loại VIF nào đưa data tới S3.

#### Đáp án A đúng - public VIF

- **Public VIF** kết nối tới các dịch vụ AWS có địa chỉ IP công khai (như **S3 endpoint công khai**) qua DX, không đi qua ISP.
- Dùng ngay port 10 Gbps đã trả tiền, chỉ thêm một VIF nên **rẻ nhất**.

```
On-prem ══ DX ══ public VIF ══► S3 public endpoint
```

#### Phương án anh chọn - D (VPC endpoint cho S3) ⚠️ Lỗi lặp lại

⚠️ **Lỗi lặp lại:** đây là lần nữa anh nhầm giữa **private VIF/VPC endpoint** và **public VIF** khi đưa data on-prem lên S3.

Cơ chế sai: **gateway VPC endpoint** của S3 là một mục trong **route table của VPC** (qua prefix list), chỉ phục vụ traffic xuất phát **từ trong VPC**. Traffic từ on-premises tới DX không dùng được gateway endpoint này, nên "dùng DX với VPC endpoint làm đích" không thành hiện thực. Đó là lý do TD gọi D là distractor.

#### Các phương án còn lại

- **B (private VIF):** private VIF chỉ truy cập resource **trong VPC** bằng IP private. S3 bucket (endpoint công khai) không nằm trong đó. Cần public VIF.
- **C (Snowball Edge):** theo TD, truyền khoảng 80 TB với Snowball Edge mất khoảng một tuần kể cả vận chuyển và xử lý, không kịp sáng thứ Hai. Cũng tốn thêm phí thiết bị và ship, không "least expensive" khi DX nhàn rỗi.

| Phương án | Tới S3 được? | Kịp thứ Hai? | Chi phí |
|---|---|---|---|
| **A. Public VIF** | Có | Có (khoảng 31-39 giờ) | **Thấp nhất** |
| B. Private VIF | Không (chỉ vào VPC) | Không xác định | Không áp dụng |
| C. Snowball Edge | Có | Không (khoảng một tuần) | Cao |
| D. Gateway endpoint qua DX | Không (on-prem không tới được) | Không xác định | Không áp dụng |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** kiến thức đã thay đổi so với lúc đề ra:

- **S3 interface endpoint (AWS PrivateLink) hiện truy cập được từ on-premises** qua DX private VIF hoặc VPN. Nhờ đó có thể đi đường private tới S3 mà không cần public VIF.
- **Gateway endpoint S3 thì KHÔNG** truy cập được từ on-premises. Đây chính là điểm mà phương án D trong đề dính.
- Interface endpoint tốn thêm phí theo giờ và phí xử lý dữ liệu theo GB, nên với yêu cầu **rẻ nhất** thì **public VIF vẫn là đáp án thi**.

Lưu ý khác: public VIF không mã hóa sẵn; S3 API qua HTTPS đã mã hóa ở tầng ứng dụng.

#### Quy tắc nhớ cho thi

- **Thấy "on-prem → S3 qua Direct Connect"** → **public VIF** (rẻ nhất, dùng DX sẵn có)
- **Private VIF** → chỉ vào **resource trong VPC**; **gateway endpoint** → chỉ dùng được từ trong VPC
- **Thấy "VPC endpoint" trong đáp án cho on-prem** → nghi ngờ distractor (ngoại lệ: S3 interface endpoint, nhưng đắt hơn)
- **Tính nhanh:** 140 TB qua 10 Gbps khoảng 31 giờ; qua 200 Mbps khoảng 65 ngày; Snowball khoảng một tuần
- Mnemonic: **"S3 là public service → public VIF"**

### TD explanation

Correct option:

Configure a public virtual interface on the 10-Gbps Direct Connect connection and then copy the data to S3 over the connection

AWS Direct Connect links your on-premises data center to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. With this connection, you can create virtual interfaces directly to public AWS services (for example, to Amazon S3) or to Amazon VPC, bypassing internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the Region with which it is associated.

There are two types of Direct Connect connections:

Dedicated Connection: A physical Ethernet connection associated with a single customer. Customers can request a dedicated connection through the AWS Direct Connect console, the CLI, or the API. This supports speed of 1Gbps and 10Gbps.

Hosted Connection: A physical Ethernet connection that an AWS Direct Connect Partner provisions on behalf of a customer. Customers request a hosted connection by contacting a partner in the AWS Direct Connect Partner Program, who provisions the connection. This supports speed of 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps.


via - https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

The given use-case requires transferring 140 TB of archived data within a duration of approximately two days (48 hours). Now, the Direct Connect connection assures a speed of 10Gbps (Gigabits per second) as it is minimally used. As 1 Byte = 8 bits, therefore you can transfer approximately 1GBps (Gigabytes per second).

So the hourly data transfer is 1 * 60 * 60 = 3,600 GB or approximately 3.6 TB.

So the approximate daily data transfer is 3.6 * 24 = ~ 86 TB

Therefore, the entire archived dataset of 140 TB can be transferred in less than two days (48 hours)

Additionally, you should configure a public virtual interface from the Direct Connect connection to connect to AWS resources that are reachable by a public IP address (such as an S3 bucket).


via - https://aws.amazon.com/premiumsupport/knowledge-center/public-private-interface-dx/

Incorrect options:

Configure a private virtual interface on the 10-Gbps Direct Connect connection and then copy the data securely to S3 over the connection - You can only use a private virtual interface to connect to your resources hosted in an Amazon Virtual Private Cloud (Amazon VPC) using their private IP addresses. You must use a public virtual interface from the Direct Connect connection to connect to an S3 bucket.

Configure a VPC endpoint for S3 and then leverage the Direct Connect connection for data transfer with VPC endpoint as the target - This option has been added as a distractor. A VPC endpoint is only meant to be used from within a VPC to connect to an S3 bucket, like so:


via - https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html

Order multiple AWS Snowball Edge appliances, transfer the data in parallel to these appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3 - The end-to-end time to transfer up to 80 TB of data into AWS with Snowball Edge is approximately one week, including the usual shipping and handling time in AWS data centers. Therefore this option is ruled out.

References:

https://aws.amazon.com/premiumsupport/knowledge-center/public-private-interface-dx/

https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html

https://aws.amazon.com/snowball/faqs/

</details>

---

# 🔁 Đổi đáp án khi review (5 câu)

Câu đã đổi đáp án sau lượt đầu (snapshot `exam_runs/udemy2-pre-review-snapshot-261028.json` → kết quả cuối). Q11 và Q67 nằm ở phần câu sai phía trên; Q43, Q52, Q55 đổi sang đúng và có đầy đủ đề + giải thích bên dưới.

| Q | Lượt đầu | Cuối | Đáp án | Kết quả đổi |
|---|---|---|---|---|
| [Q11](#q11) | B | A | B | 🔴 đúng → sai |
| [Q67](#q67) | D | B | D | 🔴 đúng → sai |
| [Q43](#q43) | B | C | C | 🟢 sai → đúng |
| [Q52](#q52) | D | B | B | 🟢 sai → đúng |
| [Q55](#q55) | A, C, D | A, D, E | A, D, E | 🟢 sai → đúng |

**Bài học:** 3 lần đổi đúng đều có lý do cụ thể (tìm ra yêu cầu bị bỏ sót, hoặc câu chọn 3 thiếu một bước). 2 lần đổi sai đều là câu 1 đáp án, đổi theo cảm giác. → Chỉ đổi khi chỉ ra được **từ khóa/dữ kiện mới** trong đề.

<a id="q43"></a>

## Q43 · đổi đáp án khi review (sai → đúng)

<!-- source: U2Q20 · domain: CI · flagged · time: 4:22 · first: 43:09 · visits: 2 · changes: 1 -->

A social media company has a serverless application stack that consists of CloudFront, API Gateway and Lambda functions. The company has hired you as an AWS Certified Solutions Architect Professional to improve the current deployment process which creates a new version of the Lambda function and then runs an AWS CLI script for deployment. In case the new version errors out, then another CLI script is invoked to deploy the previous working version of the Lambda function. The company has mandated you to decrease the time to deploy new versions of the Lambda functions and also reduce the time to detect and rollback when errors are identified.

Which of the following solutions would you suggest for the given use-case?

- **A.** Set up and deploy a CloudFormation stack containing a new API Gateway endpoint that points to the new Lambda version. Test the updated CloudFront origin that points to this new API Gateway endpoint and in case errors are detected then revert the CloudFront origin to the previous working API Gateway endpoint
- **B.** Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. Use pre-traffic and post-traffic test functions of the change set to verify the deployment. Rollback in case CloudWatch alarms are triggered
- **C.** Use Serverless Application Model (SAM) and leverage the built-in traffic-shifting feature of SAM to deploy the new Lambda version via CodeDeploy and use pre-traffic and post-traffic test functions to verify code. Rollback in case CloudWatch alarms are triggered
- **D.** Set up and deploy nested CloudFormation stacks with the CloudFront distribution as well as the API Gateway in the parent stack. Create and deploy a child stack containing the Lambda functions. To address any changes in a Lambda function, create a CloudFormation change set and deploy. In case the Lambda function errors out, rollback the CloudFormation change set to the previous version

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **Pass 1:** B → **Final:** C

🔑 **Key words:** Lambda new version via CLI scripts, reduce time to deploy, detect errors and roll back faster, CloudFront + API Gateway

🪤 **Pass-1 trap:** First pass picked B (nested CloudFormation + change set). Change sets have no pre/post-traffic hooks and no gradual traffic shift; those belong to CodeDeploy. Review caught that B borrowed CodeDeploy wording onto CloudFormation.

🧠 **Rule:** Faster, safer Lambda releases = SAM `DeploymentPreference` → CodeDeploy canary/linear + PreTraffic/PostTraffic hooks + CloudWatch alarms for auto-rollback.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CloudFront ──► API Gateway ──► Lambda (version mới)
                                  ▲
        Hiện tại: tạo version + chạy AWS CLI script deploy
                  lỗi -> chạy CLI script khác để deploy lại version cũ

Yêu cầu: (1) deploy NHANH hơn   (2) phát hiện lỗi + rollback NHANH hơn
```

Đáp án đúng: **C (SAM + CodeDeploy traffic shifting, PreTraffic/PostTraffic hooks, rollback bằng CloudWatch alarms)**. Lượt 1 anh chọn B, trong lúc review anh đổi sang C và đổi đúng.

#### Đáp án C đúng

SAM là framework viết serverless bằng cú pháp rút gọn; khi deploy, SAM được transform thành CloudFormation. Điểm mấu chốt: SAM tích hợp sẵn **CodeDeploy** cho Lambda thông qua `AutoPublishAlias` + `DeploymentPreference`.

```
Publish version mới (chưa nhận traffic)
    │
    ▼
PreTraffic hook (một Lambda test) ── fail ──► rollback, alias giữ version cũ
    │ pass
    ▼
Alias dịch traffic dần: Canary / Linear (hoặc AllAtOnce)
    │   CloudWatch alarms theo dõi trong lúc dịch traffic
    │   alarm kêu ──► CodeDeploy tự rollback về version cũ
    ▼
PostTraffic hook (Lambda test) ── fail ──► rollback
    │ pass
    ▼
100% traffic sang version mới
```

Khớp từng yêu cầu của đề:

- **Deploy nhanh hơn:** thay hai CLI script thủ công bằng một cơ chế khai báo trong template, không phải tự dịch 100% traffic một lần.
- **Phát hiện lỗi sớm:** PreTraffic test chạy khi version mới chưa nhận traffic thật; canary/linear chỉ cho một phần nhỏ user dính lỗi.
- **Rollback nhanh:** alarm kêu thì CodeDeploy tự đưa alias về version cũ, không cần script thứ hai.

#### Phương án anh chọn lượt 1 - B

B nhìn rất giống C: có nested stack, change set, và cả câu "pre-traffic and post-traffic test functions", "rollback in case CloudWatch alarms are triggered". Chính phần từ khóa này làm anh tin B đúng.

Nhưng **CloudFormation change set không có pre-traffic / post-traffic test function** (TD ghi rõ B là distractor). Change set chỉ để **xem trước** tác động lên stack (resource nào bị thay thế/xóa) rồi quyết định execute hay không. Nó không publish version rồi test, không dịch traffic dần. Hook PreTraffic/PostTraffic và canary/linear là tính năng của **CodeDeploy**. B đã "mượn" từ vựng của CodeDeploy gắn vào CloudFormation.

📝 Ghi chú kỹ thuật: CloudFormation có cơ chế rollback riêng khi stack update lỗi và có thể cấu hình rollback trigger bằng CloudWatch alarm. Nhưng đó là rollback cả stack update, không phải dịch traffic từng phần và không có hook test trước/sau traffic như B mô tả. Với đề này, giữ đáp án C.

#### Các phương án còn lại

- **D (nested stack + change set, rollback change set):** thiếu mọi thứ đề cần. Không biết lỗi cho tới khi deploy xong; không giúp "giảm thời gian phát hiện lỗi" (TD: không biết lỗi cho tới khi thực sự deploy stack).
- **A (API Gateway endpoint mới trỏ Lambda version mới, đổi CloudFront origin):** phải dựng endpoint mới, test thủ công, rồi đổi/đổi lại origin. Chậm và nhiều thao tác tay, không phát hiện lỗi sớm hơn; thực chất là blue/green tự chế.

| Cách | Test trước traffic | Dịch traffic dần | Rollback tự động |
|---|---|---|---|
| **C. SAM + CodeDeploy** | Có (PreTraffic hook) | Có (Canary/Linear) | Có (CloudWatch alarm) |
| B. Change set (hook là bịa) | Không | Không | Không như mô tả |
| D. Change set + rollback tay | Không | Không | Thủ công |
| A. Endpoint mới + đổi origin | Test tay | Không | Đổi origin tay |

#### Vì sao đổi đáp án lần này là đúng

Anh không đổi theo cảm giác, mà dựa vào **một dữ kiện cụ thể có thể kiểm chứng**: cụm "pre-traffic and post-traffic test functions" trong B. Khi hỏi "công cụ nào có hook pre/post-traffic cho Lambda?" thì câu trả lời là CodeDeploy (qua SAM), không phải CloudFormation change set. Đề còn có hai chữ khóa trực tiếp: **"giảm thời gian deploy"** và **"giảm thời gian phát hiện và rollback"**; chỉ C vừa có traffic shifting vừa có test hook vừa có alarm rollback.

So sánh với Q11 và Q67 (đổi từ đúng sang sai): hai lần đó anh đổi mà không chỉ ra được từ khóa mới nào trong đề. Lần này có bằng chứng cụ thể (một tính năng gắn sai service). Đó là ranh giới giữa đổi có cơ sở và đổi theo cảm giác.

#### Quy tắc nhớ cho thi

- **Thấy** "Lambda deployment an toàn / canary / linear / traffic shifting" → **SAM `DeploymentPreference` + CodeDeploy**.
- **Thấy** "PreTraffic / PostTraffic hook" → **CodeDeploy** (hook là Lambda function), không bao giờ là change set.
- **Thấy** "rollback tự động khi lỗi" cho Lambda → **CloudWatch alarms gắn vào CodeDeploy deployment**.
- **Thấy** "change set" → chỉ là **preview** thay đổi stack, không phải công cụ release an toàn.
- Khi hai đáp án gần giống nhau, hãy hỏi: "tính năng này có thật thuộc service này không?"

### TD explanation

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

</details>

<a id="q52"></a>

## Q52 · đổi đáp án khi review (sai → đúng)

<!-- source: U2Q49 · domain: MIG · flagged · time: 2:17 · first: 56:39 · visits: 2 · changes: 2 -->

A company wants to migrate its on-premises Oracle database to Aurora MySQL. The company has hired an AWS Certified Solutions Architect Professional to carry out the migration with minimal downtime using AWS DMS. The company has mandated that the migration must have minimal impact on the performance of the source database and the Solutions Architect must validate that the data was migrated accurately from the source to the target before the cutover.

Which of the following solutions will MOST effectively address this use-case?

- **A.** Configure DMS premigration assessment on the migration task so the assessment can compare the source and target data and report any mismatches
- **B.** Configure DMS data validation on the migration task so it can compare the source and target data for the DMS task and report any mismatches
- **C.** Use the table metrics of the DMS task to verify the statistics for tables being migrated including the DDL statements completed
- **D.** Use AWS Schema Conversion Tool for the migration task so it can compare the source and target data and report any mismatches

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **Pass 1:** D → **Final:** B

🔑 **Key words:** Oracle → Aurora MySQL with DMS, minimal impact on source, validate data migrated accurately

🪤 **Pass-1 trap:** First pass picked D (SCT). SCT converts schema and code; it does not compare migrated rows. Row-by-row comparison is DMS data validation, enabled on the task.

🧠 **Rule:** Validate migrated data = DMS data validation (compares rows, also CDC changes). Premigration assessment checks readiness before the run; SCT converts schema; table metrics only count rows/DDL.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises Oracle ──► AWS DMS (full load + CDC) ──► Aurora MySQL
                          │
                          └─ Yêu cầu:
                             1. Downtime tối thiểu           -> DMS với CDC
                             2. Ít ảnh hưởng source DB
                             3. KIỂM CHỨNG dữ liệu đã migrate đúng, TRƯỚC cutover
```

Đáp án đúng: **B (bật DMS data validation trên migration task)**. Lượt 1 anh chọn D (SCT), trong lúc review anh đổi sang B và đổi đúng.

#### Đáp án B đúng

**DMS data validation** là tính năng bật trên task (task setting `EnableValidation`) để so sánh dữ liệu giữa source và target:

- Với từng bảng, DMS **so sánh từng row** ở source với row tương ứng ở target, xác nhận hai bên chứa cùng dữ liệu, rồi báo mismatch.
- Với task có **CDC**, DMS còn so sánh cả các thay đổi tăng dần (incremental changes). Khớp với yêu cầu "minimal downtime" vì task đang chạy full load + CDC.
- Kết quả xem được theo bảng (validation state) để anh chốt trước khi cutover.

```
Source row ──┐
             ├─► DMS so sánh nội dung ──► khớp: Validated
Target row ──┘                            lệch: Mismatched records -> báo cáo
```

Từ khóa quyết định trong đề: **"validate that the data was migrated accurately from the source to the target"**. Chỉ có data validation làm đúng việc đó.

📝 Ghi chú kỹ thuật: validation chạy các truy vấn đọc bổ sung trên cả source lẫn target và dùng thêm network, tức có tốn tài nguyên (đúng như TD ghi). Cụm "minimal impact" của đề vẫn dẫn tới B vì không phương án nào còn lại thực sự so sánh dữ liệu. Ngoài đời, với source nhạy cảm, anh cân nhắc thời điểm chạy và đo tải.

#### Phương án anh chọn lượt 1 - D (SCT)

SCT trông hợp lý vì đề là migration Oracle sang Aurora MySQL (khác engine, thường đi kèm SCT). Nhưng vai trò của SCT là **chuyển đổi schema và code object** (table, view, stored procedure, function) sang engine đích, và báo cáo phần nào chưa convert tự động được. SCT **không so sánh dữ liệu đã migrate** giữa source và target của một DMS task. Nói cách khác, SCT trả lời "schema đích đã đúng chưa", không trả lời "từng row đã sang đúng chưa".

⚠️ Lỗi lặp lại: dễ gắn SCT vào mọi câu migration khác engine. Hãy tách rõ: SCT lo **schema**, DMS lo **data**, và validation là của **DMS**.

#### Các phương án còn lại

- **A (premigration assessment):** chạy **trước** khi task chạy, đánh giá task để tìm vấn đề có thể khiến migration không chạy như mong đợi (ví dụ cấu hình, hỗ trợ kiểu dữ liệu), để sửa trước. Nó không so sánh dữ liệu source với target. Từ khóa phân biệt: "before you run the task".
- **C (table metrics / table statistics):** chỉ thống kê số insert, update, delete, DDL đã áp dụng cho từng bảng. Đếm hoạt động, không đối chiếu nội dung từng row, nên không phát hiện sai lệch dữ liệu.

| Công cụ | Làm gì | Có so sánh dữ liệu? |
|---|---|---|
| **B. Data validation** | So từng row source vs target (cả CDC) | Có |
| A. Premigration assessment | Đánh giá task trước khi chạy | Không |
| C. Table metrics | Thống kê insert/update/delete/DDL | Không |
| D. SCT | Convert schema và code | Không |

#### Vì sao đổi đáp án lần này là đúng

Dữ kiện cụ thể trong đề là động từ của yêu cầu: **"validate that the data was migrated accurately"** (kiểm tra *dữ liệu*, *sau/trong khi* migrate). Khi gạch chân đúng chữ này, SCT bị loại ngay vì nó làm việc trên *schema*, không phải *data*. Anh đổi vì tìm ra tiêu chí đối chiếu rõ ràng, không phải vì "nghĩ lại thấy B hợp hơn".

Đối chiếu Q11 và Q67: hai câu đó anh đổi từ đúng sang sai mà không có từ khóa mới nào. Q52 đổi đúng vì phân biệt được vai trò của từng công cụ (SCT = schema, DMS validation = data) và nối với một cụm từ cụ thể trong đề.

#### Lưu ý thực tế

- Validation chạy sau khi các row đã được migrate (full load xong hoặc theo CDC), nên báo "pending" cho các row đang thay đổi liên tục; cutover nên đợi trạng thái validation ổn định.
- Có thể kết hợp **premigration assessment** (trước khi chạy) và **data validation** (trong/sau khi chạy). Hai thứ bổ sung nhau, nhưng chỉ validation trả lời được câu hỏi của đề.

#### Quy tắc nhớ cho thi

- **Thấy** "verify/validate data migrated accurately, compare source and target" → **DMS data validation**.
- **Thấy** "identify problems before running the task" → **premigration assessment**.
- **Thấy** "convert schema / stored procedure / heterogeneous migration" → **SCT**.
- **Thấy** "table statistics / inserts, updates, deletes, DDL counts" → **table metrics** (chỉ đếm).
- Mnemonic: **SCT = Schema, DMS = Data, Validation = so Từng row**.

### TD explanation

Correct option:

Configure DMS data validation on the migration task so it can compare the source and target data for the DMS task and report any mismatches

You can use AWS DMS data validation to ensure that your data has migrated accurately from the source to the target. DMS compares the source and target records and then reports any mismatches. In addition, for a CDC-enabled task, AWS DMS compares the incremental changes and reports any mismatches. As part of data validation, DMS compares each row in the source with its corresponding row at the target and verifies that those rows contain the same data. For this comparison, DMS issues appropriate queries to retrieve the data. These queries consume additional resources at the source and the target as well as additional network resources.

DMS data validation overview:

via - https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html

Incorrect options:

Use the table metrics of the DMS task to verify the statistics for tables being migrated including the DDL statements completed - You can use table metrics to capture statistics such as insert, update, delete, and DDL statements completed for the tables being migrated. This option will not help you compare the source and target data for the DMS task and report any mismatches.


via - https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.Metrics

Configure DMS premigration assessment on the migration task so the assessment can compare the source and target data and report any mismatches - A premigration assessment evaluates specified components of a database migration task to help identify any problems that might prevent a migration task from running as expected. This assessment gives you a chance to identify issues before you run a new or modified task. You can then fix problems before they occur while running the migration task itself. This can avoid delays in completing a given database migration needed to repair data and your database environment. This option will not help you compare the source and target data for the DMS task and report any mismatches.

Use AWS Schema Conversion Tool for the migration task so it can compare the source and target data and report any mismatches - You can use the AWS Schema Conversion Tool (AWS SCT) to convert your existing database schema from one database engine to another. You can convert relational OLTP schema or data warehouse schema. Your converted schema is suitable for an Amazon Relational Database Service (Amazon RDS) MySQL, MariaDB, Oracle, SQL Server, PostgreSQL DB, an Amazon Aurora DB cluster, or an Amazon Redshift cluster. This option will not help you compare the source and target data for the DMS task and report any mismatches.

References:

https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html

https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.Metrics

</details>

<a id="q55"></a>

## Q55 · đổi đáp án khi review (sai → đúng)

<!-- source: U2Q7 · domain: CI · flagged · time: 8:40 · first: 165:25 · visits: 6 · changes: 4 -->

A multi-national company uses Amazon S3 as its data lake to store the data that flows into its business. This data is both structured and semi-structured and is organized under different buckets in the company's AWS account in the same Region. Hundreds of applications in the company's AWS account use structured data for running data analytics, event monitoring, report generation, event creation, and many more. While the semi-structured data runs through several transformations and is sent to downstream applications for further processing. While the company's security policy restricts S3 bucket access over the internet, the internal security team has requested tighter access rules for the applications using the S3 data lake.

Which combination of steps will you undertake to implement this requirement in the most efficient way? (Select three)

- **A.** Create a gateway endpoint for Amazon S3 in the data lake VPC. Attach an endpoint policy to allow access to the S3 bucket only via the access points. Specify the route table that is used to access the bucket
- **B.** From each application VPC, create a gateway endpoint for Amazon S3. Configure the endpoint policy to allow access to an S3 access point. Specify the route table that is used to access the access point
- **C.** Create an S3 access point for each application from each AWS account and attach the access points to the S3 bucket. Configure each access point to be accessible only from the application's VPC. Update the bucket policy to require access from an access point
- **D.** Add a bucket policy on the buckets to deny access from applications outside the data lake VPC
- **E.** In the AWS account that owns the S3 buckets, create an S3 access point for each bucket that the applications must use to access the data. Set up all applications in a single data lake VPC
- **F.** Create an interface endpoint for Amazon S3 in each application's VPC. Configure the endpoint policy to allow access to an S3 access point. Create a VPC gateway attachment for the S3 endpoint

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D, E · **Pass 1:** A, C, D → **Final:** A, D, E

🔑 **Key words:** S3 data lake, hundreds of apps, tighter access rules, most efficient, Select THREE, access points + VPC

🪤 **Pass-1 trap:** First pass picked C (an access point per application from each account) — hundreds of access points across accounts is not 'most efficient' and conflicts with the single data-lake VPC design of A and D. Review swapped C for E (access point per bucket in the owning account, apps in one VPC).

🧠 **Rule:** Shared S3 data lake access = VPC-only access points (per bucket) + gateway endpoint policy allowing only those access points + bucket policy denying outside the VPC. Every pick must fit the same design.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Một AWS account, cùng Region
┌───────────────────────────────────────────────────────────┐
│ S3 data lake (nhiều bucket: structured + semi-structured) │
│        ▲                                                  │
│        │ chỉ cho truy cập qua access point, qua VPC       │
│  Hàng trăm ứng dụng (analytics, monitoring, reports...)   │
└───────────────────────────────────────────────────────────┘
Yêu cầu: không truy cập S3 qua internet, luật truy cập CHẶT hơn,
         cách HIỆU QUẢ nhất, chọn 3
```

Đáp án đúng: **A + D + E**. Lượt 1 anh chọn A, C, D. Anh đã đúng A và D, sau đó trong review đổi **C thành E** và thành đúng cả 3.

#### Ba lựa chọn đúng ghép thành MỘT thiết kế

```
E. Access point cho từng bucket (tạo ở account sở hữu bucket)
        │   + toàn bộ app đặt trong MỘT data lake VPC
        ▼
A. Gateway endpoint S3 trong data lake VPC
   endpoint policy: chỉ cho đi qua access point
   (điều kiện s3:DataAccessPointArn), gắn vào route table
        │
        ▼
D. Bucket policy: deny truy cập từ ngoài data lake VPC
```

- **E:** S3 access point là hostname riêng với IAM resource policy riêng và có thể cấu hình **chỉ nhận request từ một VPC** (VPC-only). Mỗi bucket một access point, và đặt các app vào một data lake VPC thì chỉ cần quản lý một điểm vào.
- **A:** gateway endpoint cho S3 trong VPC, thêm vào route table nên traffic đi vào S3 qua mạng AWS, không qua internet. Endpoint policy dùng condition kiểu `ArnNotLikeIfExists` với `s3:DataAccessPointArn` để deny mọi thứ không đi qua access point. Bucket mới chỉ cần tạo access point là tự được phép, khỏi sửa endpoint policy.
- **D:** bucket policy từ chối request đến từ ngoài VPC, đóng cửa các đường vòng (ví dụ truy cập thẳng bucket, không qua access point/VPC).

Đủ ba lớp: định danh điểm vào (access point), kiểm soát đường đi mạng (gateway endpoint + policy), khóa phía bucket (bucket policy).

#### Phương án anh chọn lượt 1 - C (và vì sao thay bằng E)

C: "tạo access point cho **từng ứng dụng** từ **từng account**, gắn vào bucket, mỗi access point chỉ truy cập được từ VPC của app, cập nhật bucket policy yêu cầu đi qua access point". Nghe giống hướng "tighter access rules", nhưng sai theo ba cách:

1. **Không hiệu quả:** có hàng trăm ứng dụng, tạo một access point cho mỗi app là hàng trăm đối tượng phải quản lý. Đề hỏi "most efficient".
2. **Sai mô hình sở hữu:** theo TD, access point chỉ tạo từ account sở hữu bucket, mà đề nói dữ liệu và ứng dụng đều nằm trong *cùng một account của công ty*, nên "from each AWS account" không có cơ sở.
3. **Mâu thuẫn với A và D:** A và D giả định một data lake VPC và một gateway endpoint chung. C lại chia mỗi app một VPC riêng. Ba lựa chọn trong câu chọn nhiều đáp án phải khớp thành cùng một thiết kế.

E thì khớp: access point **theo bucket**, tạo ở account sở hữu bucket, các app dùng chung một VPC.

📝 Ghi chú kỹ thuật: TD của đề viết rằng access point chỉ tạo được từ account sở hữu bucket. Ngoài đời S3 còn hỗ trợ tạo access point cho bucket của account khác (bucket owner phải cấp quyền trong bucket policy). Với đề thi, bám theo TD và quan trọng hơn là nhận ra C không hiệu quả và lệch thiết kế.

#### Các phương án còn lại

- **B (gateway endpoint ở từng VPC của app):** TD: không cần VPC riêng cho từng app. Một data lake VPC với một gateway endpoint (policy dùng điều kiện cho mọi access point của data lake) là đủ. Nhiều endpoint thì tốn công quản lý, không "efficient".
- **F (interface endpoint trong từng VPC + "VPC gateway attachment"):** sai hai chỗ theo TD: đề muốn gateway endpoint, và "gateway attachment" là khái niệm của Transit Gateway/gateway gắn VPC, không đi cùng S3 endpoint.

| Lựa chọn | Hiệu quả (1 VPC, 1 endpoint) | Khớp với A và D |
|---|---|---|
| **E. Access point mỗi bucket, 1 data lake VPC** | Có | Có |
| C. Access point mỗi app, nhiều account | Không (hàng trăm) | Không |
| B. Endpoint ở từng app VPC | Không | Không |
| F. Interface endpoint + gateway attachment | Không | Không |

#### Vì sao đổi đáp án lần này là đúng

Dữ kiện cụ thể trong đề khiến C sụp đổ:

- **"Hundreds of applications ... in the company's AWS account"**: một account, hàng trăm app. C ("from each AWS account", một access point mỗi app) vừa không có nhiều account, vừa nhân lên hàng trăm đối tượng.
- **"Most efficient way"**: ép chọn mô hình gom (một data lake VPC, một gateway endpoint, access point theo bucket).
- **A và D đã chắc đúng**: nên lựa chọn thứ ba phải cùng thiết kế "một data lake VPC", tức là E, không phải C.

Đó là bằng chứng mới trong đề (cụm từ + ràng buộc nhất quán giữa ba đáp án), khác với Q11 và Q67 mà anh đổi đáp án 1 lựa chọn theo cảm giác và làm hỏng bài. Với câu chọn 3, cách kiểm tra tốt là ghép ba đáp án thành một sơ đồ; nếu một đáp án không nằm trong sơ đồ đó thì nên nghi ngờ nó.

#### Quy tắc nhớ cho thi

- **Thấy** "S3 data lake, nhiều app, tighter access, chỉ trong VPC" → **VPC-only access point + gateway endpoint policy + bucket policy**.
- **Thấy** "Select THREE" → ghép các đáp án thành **một** kiến trúc nhất quán, loại đáp án lệch mô hình.
- **Thấy** "most efficient" với hàng trăm app → **gom một VPC/một endpoint**, tránh "mỗi app một cái".
- **Thấy** "gateway endpoint" → S3 và DynamoDB, thêm vào **route table**; "gateway attachment" thuộc Transit Gateway/VGW, không phải S3.
- Chỉ đổi đáp án khi chỉ ra được **từ khóa mới** trong đề, như đã đúng ở Q43, Q52, Q55 và đã sai ở Q11, Q67.

### TD explanation

Correct options:

In the AWS account that owns the S3 buckets, create an S3 access point for each bucket that the applications must use to access the data. Set up all applications in a single data lake VPC

Here is the approach that uses S3 Access Points in combination with VPC endpoint policies to make it easy to manage access to shared datasets on Amazon S3. The idea is to create an Amazon S3 VPC-Only Access Point, and then use it in the VPC endpoint policy to control access to the S3 bucket. You also have the option to use bucket policies to firewall S3 bucket access to VPCs only.

S3 Access Points are unique hostnames that you can create to enforce distinct permissions and network controls for any request made through the Access Point.

Some key features of S3 Access Points:
1. Access Points contain a hostname, an AWS ARN, and an AWS IAM resource policy.
2. Access Points by default have a specific setting to Block Public Access.
3. Access Points are unique to an account and Region.
4. Access Points can have custom IAM permissions for a user or application.
5. Access Points can have custom IAM permissions to specific objects in a bucket via a prefix to precisely control access.
6. Access Points can be configured to accept requests only from a virtual private cloud (VPC) to restrict Amazon S3 data access to a private network.

Use S3 Access Points to manage access to shared datasets on Amazon S3:

via - https://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/

How to set up S3 Access Points for an Amazon S3 bucket and use it with VPC endpoint:

via - https://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/

Create a gateway endpoint for Amazon S3 in the data lake VPC. Attach an endpoint policy to allow access to the S3 bucket only via the access points. Specify the route table that is used to access the bucket

You can access Amazon S3 from your VPC using gateway VPC endpoints. After you create the gateway endpoint, you can add it as a target in your route table for traffic destined from your VPC to Amazon S3. Leverage the following condition with a deny effect in the gateway endpoint policy:

"Condition": {
                "ArnNotLikeIfExists": {
                    "s3:DataAccessPointArn": "arn:aws:s3:us-east-1:<Account ID>:accesspoint/*"
                }


When a new Amazon S3 bucket is created, to allow access from the VPC, you can create an S3 Access Point on the S3 bucket. The preceding condition in the VPC endpoint policy would automatically allow access to this new S3 bucket via the Access Point, without having to edit the VPC endpoint policy.

Add a bucket policy on the buckets to deny access from applications outside the data lake VPC

Broadly, the steps involved are:
1. Create a VPC-only Access Point for the Amazon S3 bucket. This makes sure that this Access Point can only be accessed by resources in a specific VPC.


Create Amazon S3 gateway endpoint in the VPC and add a VPC endpoint policy. This VPC endpoint policy will have a statement that allows S3 access only via access points owned by the organization. We take advantage of the account ID in the Access Point ARN to make this possible.
Add a bucket policy on the bucket to allow access only from the VPC: This prevents any access from outside the VPC.


Incorrect options:

Create an interface endpoint for Amazon S3 in each application's VPC. Configure the endpoint policy to allow access to an S3 access point. Create a VPC gateway attachment for the S3 endpoint - You need to create an S3 access point for Amazon S3 in each application's VPC and not an interface endpoint. Gateway attachments are used with Transit Gateways and not with S3 endpoints.

Create an S3 access point for each application from each AWS account and attach the access points to the S3 bucket. Configure each access point to be accessible only from the application's VPC. Update the bucket policy to require access from an access point - This statement is incorrect. Amazon S3 access point can only be created from the AWS account that owns the S3 bucket.

From each application VPC, create a gateway endpoint for Amazon S3. Configure the endpoint policy to allow access to an S3 access point. Specify the route table that is used to access the access point - There is no need to create separate VPCs for each application, as just a single data lake VPC can house all applications, which allows you to configure a single S3 gateway endpoint having a policy with a condition to limit access via a common prefix for the access points of all the S3 buckets for the data lake. So this option is not the best fit.

References:

https://aws.amazon.com/s3/features/access-points/

https://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/

</details>
