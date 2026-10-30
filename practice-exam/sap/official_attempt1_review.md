# AWS Official Practice Exam SAP-C02 — attempt 1 (2026-10-29, scaled 783) — Wrong Answer Review (28 questions)

Source: `official_attempt1_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `official_attempt1_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q9](#q9) | ✅ 10-30 | ☐ | ☐ |
| A | [Q13](#q13) | ✅ 10-30 | ☐ | ☐ |
| A | [Q30](#q30) | ✅ 10-30 | ☐ | ☐ |
| A | [Q38](#q38) | ✅ 10-30 | ☐ | ☐ |
| A | [Q43](#q43) | ✅ 10-30 | ☐ | ☐ |
| A | [Q45](#q45) | ✅ 10-30 | ☐ | ☐ |
| A | [Q54](#q54) | ✅ 10-30 | ☐ | ☐ |
| A | [Q60](#q60) | ✅ 10-30 | ☐ | ☐ |
| A | [Q61](#q61) | ✅ 10-30 | ☐ | ☐ |
| A | [Q64](#q64) | ✅ 10-30 | ☐ | ☐ |
| A | [Q65](#q65) | ✅ 10-30 | ☐ | ☐ |
| A | [Q66](#q66) | ✅ 10-30 | ☐ | ☐ |
| A | [Q68](#q68) | ✅ 10-30 | ☐ | ☐ |
| A | [Q74](#q74) | ✅ 10-30 | ☐ | ☐ |
| B | [Q11](#q11) | ✅ 10-30 | ☐ | ☐ |
| B | [Q16](#q16) | ✅ 10-30 | ☐ | ☐ |
| B | [Q17](#q17) | ✅ 10-30 | ☐ | ☐ |
| B | [Q19](#q19) | ✅ 10-30 | ☐ | ☐ |
| B | [Q21](#q21) | ✅ 10-30 | ☐ | ☐ |
| B | [Q25](#q25) | ✅ 10-30 | ☐ | ☐ |
| B | [Q32](#q32) | ✅ 10-30 | ☐ | ☐ |
| B | [Q53](#q53) | ✅ 10-30 | ☐ | ☐ |
| B | [Q58](#q58) | ✅ 10-30 | ☐ | ☐ |
| B | [Q70](#q70) | ✅ 10-30 | ☐ | ☐ |
| B | [Q73](#q73) | ✅ 10-30 | ☐ | ☐ |
| C | [Q26](#q26) | ✅ 10-30 | ☐ | ☐ |
| C | [Q57](#q57) | ✅ 10-30 | ☐ | ☐ |
| C | [Q62](#q62) | ✅ 10-30 | ☐ | ☐ |

---

# Group A — Twin options: both look right, the one differing phrase decides (14)

<a id="q9"></a>

## Q9

<!-- source: OFF1Q9 · Multiple Choice · 3 minutes 49 seconds -->



A company stores a large amount of customer data in an Amazon S3 bucket that uses the S3 Standard storage class. The amount of data will continue to grow. The company needs to reduce the cost of the data storage. The company needs to access some customer data frequently within the first 6 months. However, the company rarely needs to access other customer data during that period. The company rarely needs to access data that is 180 days or older, but the company must have the ability to access this old data within 6 hours.

Which storage strategy will meet these requirements MOST cost-effectively?

- **A.** Implement S3 Intelligent-Tiering on the existing S3 bucket. Activate the Archive Access tier. Set the days until transition to 180.
- **B.** Create a new S3 Lifecycle configuration for the existing S3 bucket. Configure the lifecycle rule for all objects to move data to S3 Glacier Deep Archive after 180 days.
- **C.** Implement S3 Intelligent-Tiering on the existing S3 bucket. Activate the Deep Archive Access tier. Set the days until transition to 180.
- **D.** Create a new S3 Lifecycle configuration for the existing S3 bucket. Configure the lifecycle rule for all objects to move data to S3 Glacier Flexible Retrieval after 180 days.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** rarely accessed after 180 days, must retrieve within 6 hours, MOST cost-effective, Intelligent-Tiering

🪤 **Your trap:** Picked Deep Archive Access tier; its retrieval can take up to 12 hours, breaking the 6-hour SLA. Archive Access restores within minutes to ~5 hours.

🧠 **Rule:** Intelligent-Tiering: Archive Access (≤ ~5 h) vs Deep Archive Access (≤ 12 h). Match the retrieval SLA first, then pick the cheapest tier that meets it.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Ngày 0                     Ngày 180                  Sau đó
┌──────────────┐           ┌──────────────────┐
│ S3 Standard  │ ───────►  │ Dữ liệu cũ: hiếm │  Phải lấy lại trong ≤ 6 giờ
│ (đắt)        │           │ khi truy cập     │
└──────────────┘           └──────────────────┘
 6 tháng đầu: có object truy cập thường xuyên, có object hiếm khi
 Yêu cầu: giảm cost, MOST cost-effective, truy xuất cũ ≤ 6 giờ
```

Đáp án đúng: **A (Intelligent-Tiering + Archive Access tier, 180 ngày)**. Anh chọn **C** (Intelligent-Tiering + Deep Archive Access tier).

#### Cụm khác biệt quyết định

A và C giống hệt nhau, chỉ khác đúng một cụm:

- Đáp án đúng A: "Activate the **Archive Access** tier"
- Anh chọn C: "Activate the **Deep Archive Access** tier"

Đề nói "must have the ability to access this old data **within 6 hours**". Theo giải thích AWS:

- Archive Access tier: standard retrieval trong khoảng **3-5 giờ** -> đáp ứng 6 giờ.
- Deep Archive Access tier: standard retrieval trong **12 giờ** -> vượt 6 giờ.

Chọn tier nào = so SLA truy xuất với con số 6 giờ. Deep Archive Access rẻ hơn nhưng vi phạm SLA, nên bị loại.

#### Đáp án đúng A - vì sao hợp

S3 Intelligent-Tiering tự theo dõi access pattern và chuyển object giữa các tier để tối ưu chi phí. Đề có hai nhóm dữ liệu trong 6 tháng đầu (truy cập thường xuyên vs hiếm) -> access pattern không đồng nhất, không đoán trước được -> Intelligent-Tiering phù hợp hơn lifecycle chuyển cứng theo ngày. Bật Archive Access với 180 ngày thì dữ liệu cũ vào archive nhưng vẫn lấy lại trong 3-5 giờ.

#### Anh chọn C - vì sao trông đúng và vì sao sai

Trông đúng vì cùng là Intelligent-Tiering, và Deep Archive là tier "rẻ nhất" - phản xạ "MOST cost-effective" kéo anh về phía đó. Nhưng cost chỉ được tối ưu **sau khi** đã thỏa ràng buộc cứng (6 giờ). Deep Archive Access lấy lại trong 12 giờ nên không đạt.

⚠️ Lỗi lặp lại: chọn tầng lưu trữ rẻ nhất mà bỏ qua SLA truy xuất. Luôn lọc theo retrieval time trước.

#### Các đáp án còn lại

- **B (Lifecycle -> Glacier Deep Archive sau 180 ngày):** Deep Archive retrieval 12 giờ, không đạt 6 giờ. Thêm nữa, toàn bộ data nằm ở S3 Standard suốt 180 ngày đầu, trong khi nhiều object hiếm truy cập có thể để ở tầng rẻ hơn nhiều.
- **D (Lifecycle -> Glacier Flexible Retrieval sau 180 ngày):** Flexible Retrieval lấy lại nhanh nên đạt SLA, nhưng vẫn để mọi thứ ở S3 Standard 180 ngày đầu và không tối ưu theo access pattern không biết trước. AWS nói giải pháp tốt hơn là Intelligent-Tiering.

#### Bảng so sánh

| Phương án | Cơ chế | Truy xuất data cũ | Tối ưu 180 ngày đầu |
|---|---|---|---|
| **A. INT + Archive Access** | Tự động theo access | ~3-5 giờ (đạt) | Có |
| B. Lifecycle -> Deep Archive | Cố định theo ngày | 12 giờ (trượt) | Không |
| C. INT + Deep Archive Access | Tự động theo access | 12 giờ (trượt) | Có |
| D. Lifecycle -> Glacier Flexible | Cố định theo ngày | Nhanh (đạt) | Không |

#### Quy tắc nhớ cho thi

- **Thấy "access pattern không đoán trước / một phần hiếm dùng"** -> **S3 Intelligent-Tiering**
- **Thấy "truy xuất trong 6 giờ"** -> **Archive Access** (3-5 giờ), **không phải** Deep Archive Access (12 giờ)
- **Hai đáp án chỉ khác tên tier** -> so retrieval time với SLA trong đề trước, rồi mới xét giá
- **Lifecycle cứng theo ngày** -> để data ở Standard cho đến ngày chuyển, thường kém Intelligent-Tiering khi pattern không rõ

### TD explanation

A ✔. S3 Intelligent-Tiering automatically monitors access patterns and moves objects across multiple access tiers to optimize storage costs. Standard retrieval of objects in the S3 Intelligent-Tiering Archive Access tier occurs within 3–5 hours. This solution addresses both the unknown access patterns and the requirement to access the old data within 6 hours.
  For more information about S3 Intelligent-Tiering, see How S3 Intelligent-Tiering Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

B. Use of S3 Lifecycle configurations to move data to S3 Glacier Deep Archive would reduce the cost of storage after 180 days. However, S3 Glacier Deep Archive has a retrieval time of 12 hours. This time frame does not meet the requirement to access the old data within 6 hours. Additionally, this solution leaves all data in S3 Standard storage for the first 180 days, when many of the infrequently accessed objects could be stored at a much lower cost.
  For more information about S3 Lifecycle rules, see Transitioning Objects Using Amazon S3 Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

C. S3 Intelligent-Tiering automatically monitors access patterns and moves objects across multiple access tiers to optimize storage costs. However, Standard retrieval of objects in the S3 Intelligent-Tiering Deep Access Archive tier occurs within 12 hours. This time frame does not meet the requirement to access the old data within 6 hours.
  For more information about S3 Intelligent-Tiering, see How S3 Intelligent-Tiering Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

D. Use of S3 Lifecycle configurations to move data to S3 Glacier Flexible Retrieval would reduce the cost of storage after 180 days. S3 Glacier Flexible Retrieval can retrieve objects quickly. However, this solution leaves all data in S3 Standard for the first 180 days, when many of the infrequently accessed objects could be stored at a much lower cost. This solution does not optimize the storage classes based on unknown or changing access patterns. A better solution would use S3 Intelligent-Tiering.
  For more information about S3 Lifecycle rules, see Transitioning Objects Using Amazon S3 Lifecycle. https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html
  For more information about S3 storage classes, see Using Amazon S3 Storage Classes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html

</details>

<a id="q13"></a>

## Q13

<!-- source: OFF1Q13 · Multiple Choice · 2 minutes 19 seconds -->



A company plans to set up multiple AWS accounts by using AWS Organizations. A company-wide policy requires teams to take a backup of Amazon EBS volumes each day. The company's Cloud Center of Excellence (CCoE) team wants to design a backup solution that it can enforce consistently across all the accounts.

Which solution will meet these requirements MOST reliably?

- **A.** Create an AWS Service Catalog product that creates an Amazon Data Lifecycle Manager (Amazon DLM) snapshot policy. Enable all account administrators to launch the product within each account.
- **B.** Create an AWS CloudFormation template to create a backup plan through AWS Backup. Use the template to deploy the backup plan to multiple accounts by using CloudFormation StackSets.
- **C.** Create an Organizations backup policy to back up resources by using Amazon Data Lifecycle Manager (Amazon DLM). Validate and attach the backup policy to the root of the organization.
- **D.** Create an Organizations backup policy to back up resources by using AWS Backup. Validate and attach the backup policy to the root of the organization.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** Organizations, daily EBS backups, CCoE enforce consistently across accounts, MOST reliable

🪤 **Your trap:** Picked a backup policy using Data Lifecycle Manager; Organizations backup policies are an AWS Backup feature, not DLM.

🧠 **Rule:** Org-wide enforced backups = Organizations backup policy → AWS Backup plans in every account. DLM is per-account EBS/AMI lifecycle.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
┌──────────────────────────────────────────────┐
│ Root  ◄── Backup policy (gắn ở đây)          │
│  ├─ OU / Account 1: EBS volumes              │
│  ├─ OU / Account 2: EBS volumes              │
│  └─ OU / Account N: EBS volumes              │
└──────────────────────────────────────────────┘
 Yêu cầu: backup EBS hằng ngày, CCoE ÉP BUỘC nhất quán,
 MOST reliably
```

Đáp án đúng: **D (Organizations backup policy dùng AWS Backup)**. Anh chọn **C** (Organizations backup policy dùng Amazon DLM).

#### Cụm khác biệt quyết định

C và D giống nhau (Organizations backup policy, validate, attach vào root), chỉ khác một cụm:

- Đáp án đúng D: "back up resources by using **AWS Backup**"
- Anh chọn C: "back up resources by using **Amazon Data Lifecycle Manager (Amazon DLM)**"

Theo AWS: **không thể tạo một DLM snapshot policy bằng Organizations backup policy**. Organizations backup policy là tính năng tạo **backup plan của AWS Backup** ở mọi account. Đề yêu cầu "enforce consistently across all the accounts" nên cần cơ chế Organizations ép xuống account, và cơ chế đó chỉ đi cùng AWS Backup. C nghe hợp lý nhưng là tổ hợp không tồn tại.

#### Đáp án đúng D - vì sao hợp

AWS Backup tập trung hóa và tự động hóa backup nhiều dịch vụ, gồm EBS. Backup plan với backup rule phù hợp đáp ứng chính sách hằng ngày. Organizations backup policy tạo các backup plan này trên nhiều account. Theo AWS, **không thể xóa hay sửa các backup plan này riêng lẻ trong account** -> chính sách được ép thực thi đáng tin cậy và nhất quán.

#### Anh chọn C - vì sao trông đúng và vì sao sai

Trông đúng vì DLM đúng là công cụ tự động tạo, giữ và xóa EBS snapshot, và C có cả "Organizations backup policy" lẫn "root". Nhưng hai thứ này không ghép được với nhau: policy của Organizations không sinh ra DLM policy.

⚠️ Lỗi lặp lại: ghép một tính năng đúng chủ đề với một cơ chế quản trị không hỗ trợ nó. Hãy kiểm tra "tính năng X có được cơ chế Y triển khai không".

#### Các đáp án còn lại

- **A (Service Catalog product tạo DLM policy):** Không đảm bảo độ tin cậy, vì admin từng account có thể không launch product hoặc lỡ xóa nó.
- **B (CloudFormation tạo AWS Backup plan + StackSets):** StackSets triển khai được nhiều account, nhưng stack instance có thể bị xóa từ bên trong account -> không đảm bảo ép buộc nhất quán.

#### Bảng so sánh

| Phương án | Công cụ backup | Cách phân phối | Có thể bị gỡ tại account? |
|---|---|---|---|
| A | DLM | Service Catalog | Có (không launch / xóa) |
| B | AWS Backup | StackSets | Có (xóa stack instance) |
| C | DLM | Org backup policy | Không tồn tại tổ hợp này |
| **D** | **AWS Backup** | **Org backup policy** | **Không sửa/xóa riêng lẻ được** |

#### Quy tắc nhớ cho thi

- **Thấy "Organizations + backup policy"** -> **AWS Backup** (không bao giờ DLM)
- **Thấy "enforce consistently across accounts, MOST reliably"** -> cơ chế **không bị account xóa/sửa** (Org policy), không phải Service Catalog hay StackSets
- **DLM** = quản lý vòng đời EBS snapshot/AMI trong từng account, không phải công cụ org-wide

### TD explanation

A. Amazon DLM automates the creation, retention, and deletion of EBS snapshots. However, you cannot ensure reliability by creating an Amazon DLM snapshot policy as an AWS Service Catalog product. An individual account administrator might not launch the product or might accidentally delete the product.
  For more information about Amazon DLM, see Amazon Data Lifecycle Manager. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html
  For more information about AWS Service Catalog, see Overview of AWS Service Catalog. https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is\_concepts.html

B. AWS Backup centralizes and automates data backups across AWS services, including Amazon EBS. CloudFormation StackSets can reliably launch the solution as stack instances across the accounts. However, it is possible to delete these stack instances internally within the account. This solution will not meet the requirement to consistently enforce the company's backup policy.
  For more information about how to detect changes in resources in stack sets, see Detecting Unmanaged Configuration Changes in Stack Sets. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html

C. Amazon DLM automates the creation, retention, and deletion of EBS snapshots. However, you cannot create an Amazon DLM snapshot policy by using an Organizations backup policy.
  For more information about Amazon DLM, see Amazon Data Lifecycle Manager. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html

D ✔. AWS Backup centralizes and automates data backups across AWS services, including Amazon EBS. AWS Backup can implement a backup plan with the appropriate backup rule to meet the company's backup policy. Additionally, Organizations backup policies conveniently create these backup plans across multiple accounts. It is not possible to delete or edit these backup plans individually within the account. This solution will enforce the company's backup policy reliably and consistently.
  For more information about AWS Backup, see Creating a Backup Plan. https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html
  For more information about Organizations backup policies, see Creating, Updating, and Deleting Backup Policies. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_backup\_create.html

</details>

<a id="q30"></a>

## Q30

<!-- source: OFF1Q30 · Multiple Choice · 3 minutes 47 seconds -->



A company is migrating its marketing website and content management system from an on-premises data center to AWS. The company wants the AWS application to be deployed in a VPC with Amazon EC2 instances used for the web servers and an Amazon RDS instance for the database.

The company has a runbook document that describes the installation process of the on-premises system. The company would like to base the AWS system on the processes referenced in the runbook document. The runbook document describes the installation and configuration of the operating systems, network settings, the website, and content management system software on the servers. After the migration is complete, the company wants to be able to make changes quickly to take advantage of other AWS features.

How can the application and environment be deployed and automated in AWS with the LEAST operational overhead, while allowing for future changes?

- **A.** Write an AWS CloudFormation template that creates the VPC, the EC2 instances, and the RDS instance for the application. Ensure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration.
- **B.** Write a Python script that uses the AWS API to create the VPC, the EC2 instances, and the RDS instance for the application. Write shell scripts that implement the rest of the steps in the runbook. Have the Python script copy and run the shell scripts on the newly created instances to complete the installation.
- **C.** Update the runbook to describe how to create the VPC, the EC2 instances, and the RDS instance for the application by using the AWS Console. Make sure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration.
- **D.** Write an AWS CloudFormation template that creates the VPC, the EC2 instances, and the RDS instance for the application. Include EC2 user data in the AWS CloudFormation template to install and configure the software.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** runbook describes install and config, LEAST operational overhead, allow future changes

🪤 **Your trap:** Picked CloudFormation for infrastructure but kept the manual runbook steps for software install.

🧠 **Rule:** Automate the whole runbook: CloudFormation for infra + EC2 user data (or cfn-init) for install/config; change via stack updates.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Runbook on-prem:  [cài OS] -> [cấu hình mạng] -> [cài website] -> [cài CMS]
                                  │
                                  ▼
AWS: VPC + EC2 (web) + RDS    ... và các bước cài đặt phần mềm?

Yêu cầu: LEAST operational overhead + thay đổi nhanh về sau
```

Đáp án đúng: **D (CloudFormation + EC2 user data trong template)**. Anh chọn **A** (CloudFormation cho hạ tầng, còn các bước runbook khác vẫn làm tay).

#### Cụm khác biệt quyết định

A và D đều là CloudFormation tạo VPC, EC2, RDS. Khác nhau ở vế sau:

- Anh chọn A: "Ensure that the rest of the steps in the runbook are **updated to reflect any changes**" -> các bước cài đặt/cấu hình phần mềm **vẫn là thủ công**
- Đáp án đúng D: "Include **EC2 user data** in the AWS CloudFormation template to **install and configure the software**" -> cài đặt **tự động trong template**

Đề nhấn mạnh runbook mô tả cả cài OS, mạng, website, CMS, và yêu cầu **LEAST operational overhead**. Phần mềm vẫn cài tay (A) nghĩa là overhead còn nguyên. D tự động hóa toàn bộ runbook.

#### Đáp án đúng D - vì sao hợp

CloudFormation dựng hạ tầng, user data trên EC2 chạy script cài đặt và cấu hình phần mềm theo đúng các bước runbook. Muốn đổi sau này, dùng **stack update** để triển khai phiên bản template mới -> đáp ứng "thay đổi nhanh để tận dụng tính năng AWS khác".

#### Anh chọn A - vì sao trông đúng và vì sao sai

Trông đúng vì CloudFormation là hướng IaC chuẩn. Nhưng theo AWS, A chỉ tự động một nửa: "the installation and configuration of the software is still manual". Phần còn lại vẫn cần người làm theo runbook, nên không đạt LEAST overhead.

⚠️ Lỗi lặp lại: dừng ở "đã dùng IaC" mà không kiểm tra IaC có phủ hết quy trình trong đề hay chưa.

#### Các đáp án còn lại

- **B (Python script + AWS API + shell script):** Có tự động hóa nhưng phải tốn nhiều công xây script, và cập nhật môi trường về sau tốn overhead hơn CloudFormation.
- **C (cập nhật runbook, làm bằng Console):** Gần như không tự động hóa, khó đổi môi trường sang dịch vụ khác khi cần.

#### Quy tắc nhớ cho thi

- **Thấy "runbook mô tả cài đặt + LEAST overhead"** -> **tự động hóa trọn vẹn**: CloudFormation (hạ tầng) + **user data** (cài/cấu hình)
- **Hai đáp án cùng CloudFormation** -> xem đáp án nào còn bước thủ công
- **"Thay đổi về sau"** -> **stack update**, không phải script tự viết

### TD explanation

A. The CloudFormation template will help you build an automated solution. However, the installation and configuration of the software is still manual.

B. This solution includes some automation, but a Python script is not the best choice. Significant effort would be necessary to build the script. A Python script will require more operational overhead to handle future updates to the environment than a CloudFormation template will.

C. This solution does not include significant automation. It would be difficult to change the environment to use other services if necessary.

D ✔. CloudFormation and Amazon EC2 user data scripts are the best option. You can use stack updates to deploy multiple versions of the template to change the environment in the future.
  For more information about CloudFormation, see AWS CloudFormation Stack Updates
  .

</details>

<a id="q38"></a>

## Q38

<!-- source: OFF1Q38 · Multiple Choice · 5 minutes 1 seconds -->



A company has developed a single-page web application in JavaScript. The source code is stored in a single Amazon S3 bucket in the us-east-1 Region. The company serves the web application to a global user base through Amazon CloudFront.

The company wants to experiment with two versions of the website without informing application users. Each version of the website will reside in its own S3 bucket. The company wants to determine which version is most successful in marketing a new product.

The solution must send application users that are based in Europe to the new website design. The solution must send application users that are based in the United States to the current website design. However, some exceptions exist. The company needs to be able to redirect specific users to the new website design, regardless of the users' location.

Which solution meets these requirements?

- **A.** Configure two CloudFront distributions. Configure a geolocation routing policy in Amazon Route 53 to route traffic to the appropriate CloudFront endpoint based on the location of clients.
- **B.** Configure a single CloudFront distribution. Configure an alternate domain name on the distribution. Configure two behaviors to route users to the different S3 origins based on the domain name that the client uses in the HTTP request.
- **C.** Configure a single CloudFront distribution with Lambda@Edge. Use Lambda@Edge to send user requests to different origins based on request attributes.
- **D.** Configure a single CloudFront distribution. Create a behavior with different paths for each version of the site. Configure Lambda@Edge on the default path to generate redirects and send the client to the correct version of the website.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** A/B test two site versions in two S3 buckets, CloudFront, users must not notice

🪤 **Your trap:** Picked path-based behaviors + redirects; different paths and redirects are visible to users.

🧠 **Rule:** Invisible A/B routing between origins = Lambda@Edge (origin request) choosing the origin by request attributes or cookie.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Người dùng ──► CloudFront ──► ? S3 bucket (site hiện tại)
                         └──► ? S3 bucket (site mới)

Europe  -> site mới       US -> site hiện tại
Ngoại lệ: một số user cụ thể -> site mới, bất kể vị trí
Người dùng KHÔNG được biết đang A/B test
```

Đáp án đúng: **C (một CloudFront distribution + Lambda@Edge chọn origin theo request attributes)**. Anh chọn **D** (behavior theo path + Lambda@Edge tạo redirect).

#### Cụm khác biệt quyết định

C và D đều dùng một distribution và Lambda@Edge. Khác nhau ở cách đưa user tới bản site:

- Anh chọn D: "Create a behavior with **different paths** for each version ... Lambda@Edge ... **generate redirects** and send the client to the correct version"
- Đáp án đúng C: "Use Lambda@Edge to **send user requests to different origins** based on **request attributes**"

Đề yêu cầu thử nghiệm "without informing application users". Theo AWS, D "would inform the user of the different versions by the different paths" - path/redirect lộ ra phía người dùng. C chọn origin ở phía server (CloudFront), URL không đổi. Ngoài ra, request attributes (header, cookie) cho phép xử lý cả luật theo vị trí lẫn ngoại lệ theo user cụ thể.

Thêm một lỗi kỹ thuật của D: Lambda@Edge được gắn vào CloudFront distribution (cache behavior), không phải gắn "vào một path" như D mô tả.

#### Đáp án đúng C - vì sao hợp

Lambda@Edge có thể định tuyến động tới bất kỳ origin nào của distribution dựa trên request attributes như header. AWS có ví dụ chính thức cho A/B testing và cho xử lý theo quốc gia. Logic có thể viết: có header/cookie ngoại lệ -> site mới; nước Europe -> site mới; US -> site hiện tại.

#### Anh chọn D - vì sao trông đúng và vì sao sai

Trông đúng vì có Lambda@Edge và đủ ý "chuyển user tới đúng phiên bản". Sai ở chỗ dùng path khác nhau và redirect, làm người dùng thấy sự khác biệt, đi ngược yêu cầu "without informing".

⚠️ Lỗi lặp lại: thấy Lambda@Edge là chọn, mà không kiểm tra cách nó được dùng (rewrite origin ẩn vs redirect hiện).

#### Các đáp án còn lại

- **A (2 distribution + Route 53 geolocation):** Geolocation routing định tuyến theo vị trí, nhưng đề cần ngoại lệ theo từng user bất kể vị trí; cơ chế này không phù hợp với yêu cầu đó theo giải thích của AWS.
- **B (một distribution, behavior theo domain name):** Người dùng tự "định tuyến" bằng tên miền họ gõ; không dựa trên vị trí, và tên miền khác nhau cho người dùng biết có hai phiên bản.

#### Quy tắc nhớ cho thi

- **Thấy "A/B test, hai S3 origin, user không biết"** -> **Lambda@Edge chọn origin theo request attributes** (header/cookie/country)
- **Redirect hoặc path riêng cho từng bản** -> lộ ra phía user, loại
- **Thấy "ngoại lệ theo user bất kể vị trí"** -> cần logic theo request attribute, không chỉ geo routing
- **Lambda@Edge gắn vào distribution/cache behavior**, không gắn "vào path"

### TD explanation

A. A geolocation policy routes traffic based on the location of client. However, the company requires some exceptions to the forwarding rules. Rule exceptions are available through Route 53.
  For more information about how to use Route 53 to route traffic based on user geographic location, see Geolocation Routing. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html
  For more information about Route 53 routing options, see Choosing a Routing Policy. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

B. This solution allows users to route themselves by the HTTP request the users submit. However, the company requires a solution that routes users based on user location. The different domain names would inform the users of the two different website versions.
  For more information about how to configure CloudFront for multiple origins and behaviors, see Can I Use a Single CloudFront Web Distribution to Serve Content from Multiple Origins Using Multiple Behaviors? https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-distribution-serve-content/

C ✔. You can use Lambda@Edge to dynamically route users to any origin from a CloudFront distribution based on request attributes such as headers. You can use this strategy to serve different versions of pages for A/B testing.
  For more information about how to use Lambda@Edge for A/B testing, see Example: A/B Testing. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-a-b-testing
  For more information about how to use Lambda@Edge for custom responses based on user location, see Example: Redirecting Viewer Requests to a Country-Specific URL. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirect-based-on-country
  For more information about how to initiate a Lambda function before CloudFront forwards a request, see Customizing at the Edge with Lambda@Edge. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html

D. This solution would inform the user of the different versions by the different paths. You would associate Lambda@Edge with a CloudFront distribution, not a path.
  For more information about how to attach Lambda@Edge to a CloudFront distribution, see Get Started Creating and Using Lambda@Edge Functions. https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works.html

</details>

<a id="q43"></a>

## Q43

<!-- source: OFF1Q43 · Multiple Choice · 2 minutes 15 seconds -->



A company has an Amazon S3 bucket that contains millions of unencrypted objects. To comply with a recent security audit, a solutions architect needs to ensure that all objects are encrypted and needs to compile a list of objects that contain sensitive data. Many applications access objects in the S3 bucket, and the development team has limited resources.

Which solution will meet these requirements with the LEAST development effort?

- **A.** Run an Amazon Inspector report against the S3 bucket to identify sensitive data. Modify the S3 bucket to enable default encryption. Use an Amazon S3 Inventory report and Amazon S3 Batch Operations to encrypt the existing unencrypted objects in the same S3 bucket.
- **B.** Run an Amazon Macie report on the S3 bucket to identify sensitive data. Modify the S3 bucket to enable default encryption. Use an S3 Inventory report and S3 Batch Operations to encrypt the existing unencrypted objects in the same S3 bucket.
- **C.** Run an Amazon Macie report on the S3 bucket to identify sensitive data. Create a new S3 bucket with default encryption enabled. Transfer the unencrypted objects to the new S3 bucket. Update the applications to access the new S3 bucket.
- **D.** Run an Amazon Inspector report on the S3 bucket to identify sensitive data. Create a new S3 bucket with default encryption enabled. Transfer the unencrypted objects to the new S3 bucket. Update the applications to access the new S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** millions of unencrypted objects, find sensitive data, many apps use the bucket, LEAST development effort

🪤 **Your trap:** Picked copying to a new encrypted bucket; every application would have to change bucket names.

🧠 **Rule:** Encrypt existing objects in place = default encryption + S3 Inventory + S3 Batch Operations (copy-in-place). Macie finds PII.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 bucket (hàng triệu object, CHƯA mã hóa)
    ▲  ▲  ▲   Nhiều ứng dụng đang truy cập (tên bucket cố định)
    │  │  │
 App1 App2 AppN        Team dev ít nguồn lực

Cần: (1) mã hóa mọi object   (2) lập danh sách object chứa dữ liệu nhạy cảm
Ràng buộc: LEAST development effort
```

Đáp án đúng: **B (Macie + default encryption + S3 Inventory + S3 Batch Operations, cùng bucket)**. Anh chọn **C** (Macie, nhưng tạo bucket mới và chuyển object sang).

#### Cụm khác biệt quyết định

B và C cùng dùng Macie. Khác nhau ở cách mã hóa object hiện có:

- Đáp án đúng B: "Use an S3 Inventory report and S3 Batch Operations to encrypt the existing unencrypted objects **in the same S3 bucket**"
- Anh chọn C: "Create a **new** S3 bucket ... Transfer the unencrypted objects ... **Update the applications** to access the new S3 bucket"

Đề nói "Many applications access objects in the S3 bucket" và "development team has limited resources", cộng "LEAST development effort". Với C, phải rà soát code từng ứng dụng tìm tên bucket cũ, sửa và test. Với B, **không cần đổi code ứng dụng** vì bucket vẫn là bucket cũ.

#### Đáp án đúng B - vì sao hợp

- **Macie** nhận diện dữ liệu nhạy cảm trong S3.
- Bật **default encryption** để object mới tự được mã hóa.
- **S3 Inventory report** tạo danh sách object cần mã hóa, dùng làm manifest cho **S3 Batch Operations** để mã hóa dữ liệu hiện có tại chỗ.

#### Anh chọn C - vì sao trông đúng và vì sao sai

Phần Macie đúng, và bucket mới có default encryption nghe gọn. Nhưng chi phí thật là sửa/test mọi ứng dụng khi đổi tên bucket, vượt xa việc chạy Batch Operations.

#### Các đáp án còn lại

- **A:** Amazon Inspector quét lỗ hổng phần mềm và network exposure của workload, **không** quét S3 tìm dữ liệu nhạy cảm.
- **D:** Cũng dùng Inspector (sai công cụ) và còn bắt đổi bucket + sửa ứng dụng.

#### Bảng so sánh

| Phương án | Tìm dữ liệu nhạy cảm | Mã hóa object cũ | Sửa ứng dụng? |
|---|---|---|---|
| A | Inspector (sai) | Inventory + Batch Ops | Không |
| **B** | **Macie** | **Inventory + Batch Ops, cùng bucket** | **Không** |
| C | Macie | Chuyển sang bucket mới | Có |
| D | Inspector (sai) | Chuyển sang bucket mới | Có |

#### Quy tắc nhớ cho thi

- **Thấy "tìm dữ liệu nhạy cảm/PII trong S3"** -> **Macie** (không phải Inspector)
- **Thấy "mã hóa object S3 đã có, ít effort"** -> **default encryption + S3 Inventory + S3 Batch Operations**
- **Thấy "nhiều app dùng bucket"** -> tránh đáp án đổi bucket/sửa code

### TD explanation

A. Amazon Inspector is an automated service that continually scans AWS workloads for software vulnerabilities and unintended network exposure. However, Amazon Inspector does not examine S3 buckets for sensitive data.
  For more information about Amazon Inspector, see What is Amazon Inspector? https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html

B ✔. Macie is a service that can identify sensitive data in Amazon S3. You can use an S3 Inventory report to create a list of objects that need to be encrypted. You can use that list as the manifest for S3 Batch Operations to encrypt existing data. No code changes are necessary for the applications that access the S3 objects.
  For more information about Macie, see What is Amazon Macie? https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html
  For more information about S3 encryption, see Encrypting Existing Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html

C. Macie is a service that can identify sensitive data in Amazon S3. However, additional development effort would be required to move the objects to a new S3 bucket and to update all the applications. You would have to inspect the code of each application for usage of the old S3 bucket names, update the code, and test the code.
  For more information about Macie, see What is Amazon Macie? https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html
  For more information about S3 encryption, see Encrypting Existing Objects. https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html

D. Amazon Inspector is an automated service that continually scans AWS workloads for software vulnerabilities and unintended network exposure. However, Amazon Inspector does not examine S3 buckets for sensitive data.
  For more information about Amazon Inspector, see What is Amazon Inspector? https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html

</details>

<a id="q45"></a>

## Q45

<!-- source: OFF1Q45 · Multiple Choice · 3 minutes 40 seconds -->



A company plans to deploy a web application that will serve a global audience. The company will deploy the application by using Amazon EC2 instances across two AWS Regions. The company will create an Amazon Aurora global database, with a primary Aurora DB cluster in the first Region and a secondary Aurora DB cluster in the second Region. The company needs to minimize latency and ensure read-after-write consistency for the application’s database operations. The company also wants to regularly test its disaster recovery (DR) procedures to minimize data loss and maximize recovery speed across the two Regions.

Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use the secondary Aurora DB cluster endpoint to perform read and write operations. Configure write forwarding to forward write operations to the primary Aurora DB cluster endpoint. Test the DR procedure by using managed planned failover.
- **B.** Use the secondary Aurora DB cluster endpoint to perform read and write operations. Configure write forwarding to forward write operations to the primary Aurora DB cluster endpoint. Test the DR procedure by using manual unplanned failover.
- **C.** Use the secondary Aurora DB cluster endpoint to perform read operations. Use the primary Aurora DB cluster endpoint to perform write operations. Test the DR procedure by using manual unplanned failover.
- **D.** Use the secondary Aurora DB cluster endpoint to perform read operations. Use the primary Aurora DB cluster endpoint to perform write operations. Test the DR procedure by using managed planned failover.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** Aurora global database, minimize latency, read-after-write consistency, test DR

🪤 **Your trap:** Picked reads from secondary + writes to primary; reads from the secondary may be stale, breaking read-after-write.

🧠 **Rule:** Aurora Global DB local reads + writes with read-after-write = write forwarding on the secondary; test DR with managed (planned) failover.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Region 1                         Region 2
┌──────────────────┐ replicate ┌──────────────────────┐
│ Aurora PRIMARY   │ ────────► │ Aurora SECONDARY     │
│ cluster          │           │ cluster              │
└──────────────────┘           └──────────────────────┘
   EC2 app                        EC2 app

Yêu cầu: minimize latency + read-after-write consistency
         + test DR thường xuyên, ít mất dữ liệu, phục hồi nhanh
         + LEAST operational overhead
```

Đáp án đúng: **A (write forwarding ở secondary + managed planned failover)**. Anh chọn **C** (đọc từ secondary, ghi vào primary, manual unplanned failover).

#### Cụm khác biệt quyết định

Có hai cụm quyết định, mỗi cụm loại đi một nửa đáp án.

Cụm 1, cách đọc/ghi:
- Đáp án đúng (A, B): "perform read and write operations [on secondary] ... Configure **write forwarding**"
- Anh chọn (C, D): "secondary for **read** ... **primary endpoint for write**"

Đề cần "read-after-write consistency". Theo AWS, đọc từ secondary mà ghi ở primary thì đọc có thể trả dữ liệu **stale** (C, D). Write forwarding cho secondary nhận ghi và chuyển về primary, cùng các consistency mode mạnh (có global consistency) -> đạt read-after-write.

Cụm 2, cách test DR:
- Đáp án đúng (A, D): "**managed planned failover**"
- (B, C): "**manual unplanned failover**"

Đề muốn test DR "regularly", "minimize data loss and maximize recovery speed", LEAST overhead. Unplanned failover phải làm tay (detach và promote secondary), không phù hợp test thường xuyên. Managed planned failover tự xử lý demotion, promotion, đồng bộ -> không mất dữ liệu, nhanh hơn.

Chỉ **A** đúng ở cả hai cụm.

#### Đáp án đúng A - vì sao hợp

Aurora global database replicate với lag rất thấp, tối ưu đọc ở gần người dùng. Write forwarding giúp ứng dụng ở Region phụ ghi qua endpoint của secondary, Aurora lo phần mạng giữa các Region. Managed planned failover xử lý tự động toàn bộ thao tác khi chuyển vai trò.

#### Anh chọn C - vì sao trông đúng và vì sao sai

Trông đúng vì "đọc local, ghi primary" là mô hình quen thuộc và hợp lý về latency đọc. Nhưng AWS chỉ ra đọc ở secondary có thể stale, không bảo đảm read-after-write. Thêm nữa C test DR bằng manual unplanned failover, tốn nhiều bước thủ công.

⚠️ Lỗi lặp lại: chọn theo mô hình quen thuộc mà không đối chiếu từ khóa "read-after-write".

#### Các đáp án còn lại

- **B:** Đúng write forwarding nhưng test DR bằng manual unplanned failover: phải detach và promote thủ công, không hợp test thường xuyên, overhead cao.
- **D:** Planned failover đúng, nhưng đọc từ secondary / ghi primary có thể stale, không đạt read-after-write.

#### Bảng so sánh

| Phương án | Đọc/ghi | Read-after-write | Test DR | Overhead |
|---|---|---|---|---|
| **A** | **Write forwarding** | **Đạt** | **Managed planned** | **Thấp** |
| B | Write forwarding | Đạt | Manual unplanned | Cao |
| C | Đọc secondary, ghi primary | Trượt (stale) | Manual unplanned | Cao |
| D | Đọc secondary, ghi primary | Trượt (stale) | Managed planned | Thấp |

#### Quy tắc nhớ cho thi

- **Thấy "Aurora Global DB + read-after-write + ghi từ Region phụ"** -> **write forwarding** ở secondary
- **Thấy "test DR thường xuyên, ít mất dữ liệu, ít overhead"** -> **managed planned failover**
- **Manual unplanned failover** = cho sự cố thật, phải detach và promote tay
- **Bốn đáp án ghép hai cụm** -> kiểm tra từng cụm riêng, chỉ một đáp án đúng cả hai

### TD explanation

A ✔. An Aurora global database replicates data with minimal replication lag to a secondary Aurora DB cluster in another Region. This process optimizes read operations for the company's global audience. Write forwarding will allow the secondary DB cluster to accept write operations and will forward write operations to the primary DB cluster. Aurora handles networking across Regions. Aurora also provides multiple consistency modes for the strongest read-after-write consistency, including global consistency. Finally, managed planned failover automatically handles demotion, promotion, and all synchronization across the clusters with no data loss and faster recovery.
  For more information about write forwarding in an Aurora global database, see Using Write Forwarding in an Amazon Aurora Global Database. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding.html
  For more information about planned failover, see Using failover in an Amazon Aurora Global Database. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover

B. A manual unplanned failover process requires the manual performance of a series of tasks. You must detach and promote a secondary DB cluster. These steps are not suitable for the company's plan to test on a regular and frequent basis. A better solution would use managed planned failover, which would eliminate the manual steps and require less operational overhead.
  For more information about recovery from unplanned outages, see Recovering an Amazon Aurora Global Database from an Unplanned Outage. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover

C. An Aurora global database replicates data with minimal replication lag to a secondary Aurora DB cluster in another Region. This process optimizes read operations for the company's global audience. However, these read operations could provide stale information. This process will not achieve the required read-after-write consistency.
  For more information about Aurora global databases, see Using Amazon Aurora Global Databases. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html

D. An Aurora global database replicates data with minimal replication lag to a secondary Aurora DB cluster in another Region. This process optimizes read operations for the company's global audience. However, these read operations could provide stale information. This process will not achieve the required read-after-write consistency.
  For more information about Aurora global databases, see Using Amazon Aurora Global Databases. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html

</details>

<a id="q54"></a>

## Q54

<!-- source: OFF1Q54 · Multiple Choice · 3 minutes 18 seconds -->



A company recently migrated a large, restartable batch computing workload from on-premises servers to AWS Batch. The batch job runs monthly in an Amazon EC2 compute environment that requires a custom AMI. The company wants to reduce the overhead that is associated with the management of the compute environment. The company also wants to reduce the cost to run the AWS Batch workload.

Which solution will meet these requirements?

- **A.** Modify the AWS Batch job to run in a managed EC2 compute environment that uses the AMI. Select Spot as the provisioning model.
- **B.** Modify the AWS Batch job to run in an AWS Fargate compute environment. Select Fargate as the provisioning model.
- **C.** Modify the AWS Batch job to run in an AWS Fargate compute environment. Select Fargate Spot as the provisioning model.
- **D.** Modify the AWS Batch job to run in a managed EC2 compute environment that uses the AMI. Select On-Demand as the provisioning model.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** AWS Batch, custom AMI, restartable jobs, reduce management overhead and cost

🪤 **Your trap:** Picked Fargate Spot; Fargate cannot use a custom AMI.

🧠 **Rule:** Restartable batch + custom AMI + cheaper = managed EC2 compute environment with Spot. Fargate only when no custom AMI/GPU needs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Batch job (chạy hằng tháng, restartable)
        │
        ▼
Compute environment ?
  ├─ EC2 managed (dùng custom AMI)  ─► On-Demand / Spot
  └─ Fargate                        ─► Fargate / Fargate Spot

Ràng buộc: cần CUSTOM AMI, giảm overhead quản lý, giảm cost
```

Đáp án đúng: **A (managed EC2 compute environment + custom AMI + Spot)**. Anh chọn **C** (Fargate + Fargate Spot).

#### Cụm khác biệt quyết định

Hai chiều khác nhau: loại compute environment và provisioning model.

- Đáp án đúng A: "**managed EC2 compute environment that uses the AMI** ... **Spot**"
- Anh chọn C: "**AWS Fargate** compute environment ... **Fargate Spot**"

Đề nói rõ "requires a custom AMI". Theo AWS: để dùng custom AMI với AWS Batch cần compute environment **EC2**; Fargate không dùng được AMI riêng. Vì thế mọi đáp án Fargate (B, C) bị loại, dù Fargate giảm overhead. Còn A và D cùng EC2 managed, khác ở provisioning model: job "restartable" và chạy hằng tháng -> **Spot** rẻ hơn On-Demand và chịu được bị thu hồi vì job khởi động lại được.

#### Đáp án đúng A - vì sao hợp

- **Managed** compute environment: AWS Batch tự quản lý capacity -> giảm overhead quản lý.
- EC2 + AMI riêng: thỏa yêu cầu custom AMI.
- **Spot**: giảm chi phí cho workload restartable, chạy hằng tháng.

#### Anh chọn C - vì sao trông đúng và vì sao sai

Trông đúng vì Fargate gần như không phải quản lý hạ tầng và Fargate Spot rẻ hơn. Vấn đề là C đáp ứng "giảm overhead" và "giảm cost" nhưng vi phạm ràng buộc cứng custom AMI.

⚠️ Lỗi lặp lại: tối ưu hai mục tiêu mềm (overhead, cost) mà bỏ qua ràng buộc cứng (custom AMI). Gạch ràng buộc cứng trước.

#### Các đáp án còn lại

- **B (Fargate):** Giảm overhead nhưng cần EC2 compute environment để dùng custom AMI.
- **D (managed EC2 + On-Demand):** Đúng loại compute environment, nhưng job restartable và chạy hằng tháng nên Spot rẻ hơn On-Demand -> không tối ưu cost.

#### Bảng so sánh

| Phương án | Compute | Custom AMI | Cost |
|---|---|---|---|
| **A** | **Managed EC2 + Spot** | **Đạt** | **Thấp nhất** |
| B | Fargate | Trượt | - |
| C | Fargate Spot | Trượt | - |
| D | Managed EC2 + On-Demand | Đạt | Cao hơn Spot |

#### Quy tắc nhớ cho thi

- **Thấy "AWS Batch + custom AMI"** -> **EC2 compute environment** (managed), không phải Fargate
- **Thấy "restartable / fault-tolerant" + giảm cost** -> **Spot**
- **Hai ràng buộc cứng trước, mục tiêu mềm sau**: custom AMI loại Fargate, rồi mới chọn Spot vs On-Demand

### TD explanation

A ✔. With AWS Batch, you need an EC2 compute environment in order to use the custom AMI. A managed compute environment would help reduce the overhead that is associated with the management of the compute environment. Also, the Spot provisioning model would have a lower cost for a restartable, monthly workload. This solution meets the requirements.
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html
  For more information about how Spot Instances help reduce costs, see Spot Instances. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html

B. Fargate would reduce the overhead that is associated with management of the compute environment. However, you need a managed EC2 compute environment in order to use the custom AMI.
  For more information about AWS Batch on Fargate, see AWS Batch on AWS Fargate. https://docs.aws.amazon.com/batch/latest/userguide/fargate.html
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html

C. Fargate would reduce the overhead that is associated with management of the compute environment. However, you need an EC2 compute environment in order to use the custom AMI.
  For more information about AWS Batch on Fargate, see AWS Batch on AWS Fargate. https://docs.aws.amazon.com/batch/latest/userguide/fargate.html
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html

D. With AWS Batch, you need a managed EC2 compute environment in order to use the custom AMI. However, because the AWS Batch job is restartable and runs monthly, Spot provisioning would be a lower-cost option than On-Demand.
  For more information about the compute environment options for AWS Batch, see Compute Environment. https://docs.aws.amazon.com/batch/latest/userguide/compute\_environments.html

</details>

<a id="q60"></a>

## Q60

<!-- source: OFF1Q60 · Multiple Choice · 2 minutes 3 seconds -->



A company runs a three-tier architecture on AWS. The web tier and application tier run in Amazon EC2 Auto Scaling groups with a database as the backend. Scaling is based on CPU utilization of the application tier. The company creates an Amazon SQS standard queue to decouple the web tier and the application tier. However, tests reveal that duplicate transactions occur and that the EC2 instances are not scaling. The lack of scaling sometimes delays application processing. A solutions architect needs to eliminate the duplicate transactions and correct the scaling delay.

Which solution will meet these requirements in the MOST scalable way?

- **A.** Create an SQS FIFO queue. Configure content-based deduplication. Update the application to use the new queue. Change the application tier scaling to use the ApproximateNumberOfMessagesVisible metric.
- **B.** Change the existing SQS standard queue to an SQS FIFO queue. Configure content-based deduplication for the queue. Change the application tier scaling to use the ApproximateNumberOfMessagesVisible metric.
- **C.** Change the existing SQS standard queue to an SQS FIFO queue. Configure content-based deduplication for the queue. Create an Amazon CloudWatch custom metric to calculate the backlog per instance that is acceptable to the company. Use a target tracking scaling policy based on the custom metric.
- **D.** Create an SQS FIFO queue. Configure content-based deduplication. Update the application to use the new queue. Create an Amazon CloudWatch custom metric to calculate the backlog per instance that is acceptable to the company. Use a target tracking scaling policy based on the custom metric.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** SQS standard duplicates, instances not scaling, MOST scalable

🪤 **Your trap:** Picked scaling on ApproximateNumberOfMessagesVisible; queue depth does not change in proportion to fleet size.

🧠 **Rule:** SQS worker scaling = target tracking on backlog per instance (custom metric: messages ÷ in-service instances). FIFO + dedup removes duplicates.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Web tier ──► SQS Standard ──► App tier (EC2 Auto Scaling group) ──► DB
               │                    ▲
               │ at-least-once      │ scale theo CPU -> không scale kịp
               ▼                    │
        duplicate transactions      backlog tăng, xử lý bị trễ
```

Hai lỗi cần sửa cùng lúc: (1) **duplicate** do Standard queue chỉ đảm bảo at-least-once, (2) **scaling chậm** do scale theo CPU. Yêu cầu quyết định: **MOST scalable**.

Đáp án đúng: **D**. Anh chọn A (đúng nửa đầu, sai nửa sau về metric scaling).

#### Cụm khác biệt quyết định

Bốn đáp án ghép từ hai cặp lựa chọn:

| Cặp | Phương án 1 | Phương án 2 |
|---|---|---|
| Queue | "**Create** an SQS FIFO queue" (tạo mới) | "**Change** the existing standard queue to FIFO" (đổi loại) |
| Scaling | "ApproximateNumberOfMessagesVisible metric" | "custom metric **backlog per instance** + target tracking" |

- Anh chọn A: "Change the application tier scaling to use the **ApproximateNumberOfMessagesVisible** metric".
- Đáp án D: "Create an Amazon CloudWatch custom metric to calculate the **backlog per instance** ... Use a **target tracking scaling policy**".

Vì sao stem chọn D: yêu cầu "MOST scalable" và "correct the scaling delay". ApproximateNumberOfMessagesVisible là số message trong queue, **không đổi tỷ lệ theo kích thước fleet**. Fleet 2 hay 20 instance thì số message vẫn như nhau nên không biết đã đủ capacity chưa. Backlog per instance = số message ÷ số instance đang chạy, so với mức backlog chấp nhận được, nên scale đúng theo tải và vẫn đúng khi fleet lớn dần.

#### Phần queue: vì sao phải "Create", không phải "Change"

**B và C sai vì không thể đổi Standard queue thành FIFO.** Loại queue được cố định lúc tạo. Phải tạo FIFO queue mới (tên kết thúc bằng `.fifo`), sau đó cập nhật application trỏ sang queue mới. Vì vậy chỉ còn A và D.

FIFO + content-based deduplication giải quyết duplicate: message trùng nội dung trong cửa sổ deduplication (5 phút) bị bỏ.

#### Anh chọn A: vì sao trông đúng và sai ở đâu

A đúng ở phần queue (tạo FIFO mới, bật dedup), nên duplicate được xử lý. Sai ở metric: scale theo queue depth thô sẽ không tương xứng với số instance, nên không tối ưu về scalability. AWS: "a custom metric would scale better as the Auto Scaling group grows".

#### Các đáp án còn lại

- **B**: sai hai tầng, không đổi được loại queue, và vẫn dùng metric queue depth thô.
- **C**: đúng metric nhưng sai ở "Change the existing queue" nên không thực hiện được.

#### Quy tắc nhớ cho thi

- **Thấy "SQS standard bị duplicate"** → **FIFO + deduplication** (và phải tạo queue mới, không đổi tại chỗ).
- **Thấy "scale EC2 theo SQS"** → **custom metric backlog per instance + target tracking**, không dùng ApproximateNumberOfMessagesVisible thô.
- **Thấy "Change the existing standard queue to FIFO"** → loại ngay.

### TD explanation

A. FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. However, the ApproximateNumberOfMessagesVisible metric will not change in proportion to the size of the Auto Scaling group that processes messages. A better solution is to use a custom metric based on an acceptable backlog per instance. A custom metric would scale better as the Auto Scaling group grows.
  For more information about scaling in response to activity in SQS queues, see Scaling Based on Amazon SQS. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html
  For more information about high throughput for FIFO queues, see High Throughput for FIFO Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html

B. FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. However, you cannot change an SQS standard queue to a FIFO queue.
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html
  For more information about how to configure a FIFO queue, see Moving from a Standard Queue to a FIFO Queue. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-moving.html

C. FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. However, you cannot change an SQS standard queue to a FIFO queue.
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html
  For more information about how to configure a FIFO queue, see Moving from a Standard Queue to a FIFO Queue. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-moving.html

D ✔. FIFO queues can enhance message transmission between applications when the order of operations and events is critical or when duplicates are not acceptable. A custom metric to scale based on an acceptable backlog per instance would base the scaling on the system load in the SQS queue. The custom metric is calculated based on the approximate number of messages, processing latency, and the number of running EC2 instances. This solution provides more accurate scaling.
  For more information about scaling in response to activity in SQS queues, see Scaling Based on Amazon SQS. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html
  For more information about FIFO queues, see Amazon SQS FIFO (First-In-First-Out) Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html
  For more information about high throughput for FIFO queues, see High Throughput for FIFO Queues. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html

</details>

<a id="q61"></a>

## Q61

<!-- source: OFF1Q61 · Multiple Choice · 3 minutes 49 seconds -->



A company stores many static files on premises. Users add a small number of new files each day. The company is refactoring and migrating some of its existing applications to AWS. The company expects this process to take 6 months. After the company completes the migration, each application will access the files directly from Amazon S3. During the migration, the files must remain accessible to the applications that the company is still running on premises. The on-premises applications run on multiple servers. The company does not want to maintain multiple copies of the static files.

How should the company manage the daily migration and the on-premises access to the files?

- **A.** Create an AWS DataSync task to transfer the new files to the S3 bucket at the end of each day. Maintain the files on premises until the company completes the refactoring.
- **B.** Create an S3 sync script and configure a recurring job to run the script at the end of each day. Maintain the files on premises until the company completes the refactoring and migration.
- **C.** Configure an AWS Storage Gateway Amazon S3 File Gateway and connect the S3 File Gateway to the S3 bucket. Create an on-premises NFS file share for the existing on-premises directory to establish access to the files.
- **D.** Configure an AWS Storage Gateway Volume Gateway and connect the Volume Gateway to the S3 bucket. Create an on-premises iSCSI volume share for the existing on-premises directory to establish access to the files.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** static files on-prem, apps on multiple servers, NFS directory, one copy, migrate to S3

🪤 **Your trap:** Picked Volume Gateway (iSCSI block); it stores volumes, not S3 objects, and cannot be shared by several servers like NFS.

🧠 **Rule:** On-prem NFS/SMB access to S3 objects = S3 File Gateway. Volume Gateway = iSCSI block volumes; Tape Gateway = VTL.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem: nhiều server ứng dụng ──(đọc file qua thư mục dùng chung)──► ?
                                                                      │
                                                                      ▼
                                                          S3 bucket (đích sau 6 tháng)
Yêu cầu: file vẫn truy cập được từ on-prem trong lúc migrate
         KHÔNG giữ nhiều bản copy
```

Đáp án đúng: **C (S3 File Gateway + NFS)**. Anh chọn D (Volume Gateway + iSCSI).

#### Cụm khác biệt quyết định

Hai đáp án Gateway giống hệt cấu trúc, chỉ khác loại gateway và giao thức:

- Anh chọn D: "**Volume Gateway** ... on-premises **iSCSI volume** share".
- Đáp án C: "**S3 File Gateway** ... on-premises **NFS file share**".

Vì sao stem chọn C:
- Ứng dụng chạy trên **nhiều server** và cần đọc **cùng một thư mục** có sẵn: cần giao thức file chia sẻ (NFS/SMB). NFS cho nhiều client cùng truy cập.
- Sau migration, "each application will access the files directly from **Amazon S3**": file phải nằm dưới dạng **S3 object**. File Gateway lưu mỗi file là một object trong S3.
- Volume Gateway là **block storage** (iSCSI). Dữ liệu nằm trong volume do gateway quản lý (lưu trên S3 dạng block/snapshot), ứng dụng AWS không đọc được thành object S3 thông thường. Một iSCSI volume cũng không gắn đồng thời cho nhiều host nếu không cấu hình thêm (cluster file system).

#### Anh chọn D: vì sao trông đúng và sai ở đâu

D trông đúng vì cũng là Storage Gateway và cũng "connect to the S3 bucket". Nhưng iSCSI volume là block device, không phải thư mục dùng chung, và dữ liệu không ở dạng object để ứng dụng đã refactor đọc thẳng từ S3. AWS: "you cannot connect multiple hosts to a Volume Gateway without additional configuration".

#### Các đáp án còn lại

- **A (DataSync cuối ngày)**: chỉ chuyển dữ liệu, không cung cấp truy cập cho ứng dụng on-prem, phải giữ bản copy on-prem, vi phạm "không muốn nhiều bản copy".
- **B (S3 sync script)**: cùng vấn đề như A, còn tự vận hành script.

| Giải pháp | Giao thức on-prem | Dữ liệu trong S3 | Nhiều server | Một bản copy |
|---|---|---|---|---|
| **C. S3 File Gateway** | NFS/SMB | Object | Có | Có |
| D. Volume Gateway | iSCSI | Block volume | Cần cấu hình thêm | Có |
| A/B. DataSync/sync | Không | Object | Không áp dụng | Không (2 bản) |

#### Quy tắc nhớ cho thi

- **Thấy "NFS/SMB on-prem truy cập S3"** → **S3 File Gateway**.
- **Thấy "iSCSI"** → Volume Gateway (block), **Tape Gateway** → VTL/backup tape.
- **Thấy "không duy trì nhiều bản copy" + "vẫn truy cập on-prem"** → loại DataSync/sync script.

### TD explanation

A. DataSync is an online data-transfer service that simplifies, automates, and accelerates the movement of data between on-premises storage systems and AWS storage services. DataSync would not provide access to the on-premises applications. The company would have to maintain a copy on premises.
  For more information about DataSync, see What Is AWS DataSync? https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

B. The S3 sync command synchronizes the contents of an S3 bucket and a local directory or the contents of two buckets. You could use this command to synchronize the data that is on premises to an S3 bucket. DataSync would not provide access to the on-premises applications. The company would have to maintain a copy on premises.
  For more information about the S3 sync command, see Sync Objects. https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-sync

C ✔. S3 File Gateway supports a file interface with Amazon S3 and combines a service and a virtual software appliance. This combination can store and retrieve objects from Amazon S3 by using industry-standard file protocols, including NFS and SMB. NFS is a shared file system that can share data for multiple client connections. This solution will also provide access to the files for the on-premises applications.
  For more information about S3 File Gateway, see Amazon S3 File Gateways. https://docs.aws.amazon.com/filegateway/latest/files3/StorageGatewayConcepts.html#file-gateway-concepts

D. A Volume Gateway provides cloud-backed storage volumes that you can mount as iSCSI devices from on-premises application servers. However, you cannot connect multiple hosts to a Volume Gateway without additional configuration.
  For more information about how to use volumes, see Using Your Volume. https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStarted-use-volumes.html
  For more information about how to configure a Volume Gateway, see Creating a Volume Gateway. https://docs.aws.amazon.com/storagegateway/latest/vgw/create-volume-gateway-volume.html

</details>

<a id="q64"></a>

## Q64

<!-- source: OFF1Q64 · Multiple Choice · 29 seconds -->



A company manages 50 AWS accounts through AWS Organizations. Different workloads in these accounts require different security groups with appropriate rules. The company's security team wants to allow SSH access only from trusted IP CIDR blocks in all AWS accounts. The security team wants to ensure that this implementation remains compliant and cannot be modified by other accounts.

How can a solutions architect meet these requirements?

- **A.** Create a common security group policy in AWS Firewall Manager. Add a primary security group with an SSH rule that allows access from trusted IP CIDR blocks. Provide the option to identify resources that do not comply with the policy rules. Select all accounts for this policy.
- **B.** Create a content audit security group policy in AWS Firewall Manager. Configure custom policy rules to deny SSH traffic from 0.0.0.0/0. Use an audit security group to allow SSH traffic from trusted IP CIDR blocks. Enable automatic remediation for any noncompliant resources. Select all accounts for this policy.
- **C.** Create a firewall policy for AWS Network Firewall in AWS Firewall Manager. Add a stateless rule group to allow SSH access from trusted IP CIDR blocks with the lowest order priority. Restrict SSH access from 0.0.0.0/0. Select all accounts for this policy.
- **D.** Create a firewall policy for AWS Network Firewall in AWS Firewall Manager. Add a stateful rule group with a strict evaluation order to allow SSH access from trusted IP CIDR blocks with the highest order priority. Restrict SSH access from 0.0.0.0/0. Select all accounts for this policy.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** 50 accounts, SSH only from trusted CIDRs, compliant, cannot be modified by accounts, Firewall Manager

🪤 **Your trap:** Picked a stateful strict-order group with the allow rule given the highest order number; the deny 0.0.0.0/0 rule is evaluated first and blocks trusted SSH too.

🧠 **Rule:** Firewall Manager + Network Firewall: rules evaluate from the lowest priority number — put the trusted-CIDR allow first, deny-all after.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations (50 accounts)
        │
   AWS Firewall Manager (policy tập trung)
        │
   Network Firewall policy ──► áp vào mọi account, member account KHÔNG sửa được
        │
   Rule group: SSH từ trusted CIDR = ALLOW, 0.0.0.0/0 = DENY
```

Yêu cầu: chỉ cho SSH từ trusted CIDR, giữ compliant, account khác không sửa được. Đáp án đúng: **C**. Anh chọn D.

#### Cụm khác biệt quyết định

C và D đều dùng Network Firewall policy, đều "Restrict SSH access from 0.0.0.0/0". Khác nhau ở loại rule group và quy ước thứ tự:

- Anh chọn D: "**stateful** rule group with a **strict evaluation order** ... allow SSH ... with the **highest order priority**".
- Đáp án C: "**stateless** rule group ... allow SSH ... with the **lowest order priority**".

Vì sao stem chọn C: rule được xử lý **từ số priority nhỏ nhất đến lớn nhất**. Muốn rule allow trusted CIDR chạy trước rule deny 0.0.0.0/0, allow phải có số priority **thấp nhất**. Ở D, allow gán "highest order priority" (số lớn nhất) nên rule deny 0.0.0.0/0 chạy trước và chặn luôn cả trusted SSH. Lưu ý: trong stateful strict order, rule cũng xử lý từ số nhỏ nhất, nên chính phần "highest" làm D sai.

#### Anh chọn D: vì sao trông đúng và sai ở đâu

D nghe "mạnh" hơn (stateful, strict order) và dùng từ "highest priority" dễ hiểu nhầm là ưu tiên cao nhất. Nhưng với Network Firewall, số priority thấp mới được đánh giá trước. Kết quả D: deny-all đứng trước allow, trusted CIDR cũng bị chặn, không đạt yêu cầu.

#### Các đáp án còn lại

- **A (common security group policy)**: AWS Firewall Manager không giới hạn SSH từ nguồn khác và không tự remediate việc mở SSH rộng.
- **B (content audit security group policy)**: policy rule chỉ allow hoặc deny, không cả hai, nên "deny 0.0.0.0/0 + allow trusted" không thực hiện được. Rule ngoài phạm vi audit security group bị coi non-compliant, auto remediation gỡ rule dư và làm gián đoạn nhiều workload ở mọi account.

| Đáp án | Cơ chế | Kết quả |
|---|---|---|
| **C** | Stateless, allow ở priority thấp nhất | Allow trusted chạy trước, còn lại bị chặn |
| D | Stateful strict, allow ở priority cao nhất | Deny chạy trước, chặn luôn trusted |
| A | Common SG policy | Không chặn SSH từ nguồn khác |
| B | Content audit SG | Không allow + deny cùng lúc, remediation gây gián đoạn |

#### Quy tắc nhớ cho thi

- **Thấy "Network Firewall rule priority"** → **số nhỏ chạy trước**; allow cụ thể phải số nhỏ hơn deny tổng quát.
- **Thấy "cannot be modified by member accounts" + nhiều account** → **Firewall Manager** policy.
- **Thấy "highest order priority" cho rule allow** → bẫy, thường làm allow chạy sau deny.

### TD explanation

A. Firewall Manager does not restrict SSH access from any other sources. Additionally, Firewall Manager does not automatically remediate such broad SSH access. For these reasons, this solution does not meet the requirements.
  For more information about common security group policies, see Common Security Group Policies. https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies.html#security-group-policies-common

B. A content audit security group policy in Firewall Manager is used to audit security groups across multiple accounts and to recognize any noncompliant rules. Policy rules can either allow or deny rules defined in the audit security group, but not both. With this setting, other security groups across accounts are evaluated. In this scenario, the policy rule allows SSH traffic from trusted IP CIDR blocks and denies SSH traffic from 0.0.0.0/0. This denial is not possible. Additionally, other security groups across accounts must be within the scope of the audit security group. Any out-of-scope rules will make these security groups noncompliant. Automatic remediation will occur, and Firewall Manager will remove any additional rules. Such actions will disrupt multiple workloads across all accounts.
  For more information about content audit security group policies, see Content Audit Security Group Policies. https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies.html#security-group-policies-audit
  For more information about content audit security group policy remediation actions, see Security Group Content Audit Policy Findings. https://docs.aws.amazon.com/waf/latest/developerguide/security-group-content-audit-policy-findings.html

C ✔. A firewall policy with a stateless group will allow or restrict traffic based on the rules within the group. In a stateless group, rules are processed starting from the lowest numbered priority setting. A rule that restricts SSH access from trusted sources will be processed and allowed first. The rest of the SSH traffic (0.0.0.0/0) will be restricted. These network firewalls and rule groups cannot be modified by the member accounts of an organization on AWS Organizations. This solution fulfills all the requirements.
  For more information about Network Firewall policies in Firewall Manager, see AWS Network Firewall Policies. https://docs.aws.amazon.com/waf/latest/developerguide/network-firewall-policies.html
  For more information about stateless rule groups, see Stateless Rule Groups in AWS Network Firewall. https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-rule-groups-5-tuple.html

D. A stateful rule group with a strict evaluation order will evaluate the rules by order of priority, starting from the lowest number. In this scenario, a rule that restricts SSH access from 0.0.0.0/0 will be evaluated first and will restrict all traffic, including SSH access from the trusted sources. This solution does not meet the requirements.
  For more information about stateful rule groups with strict evaluation order, see Strict Evaluation Order. https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order
  For more information about standard stateful rule groups, see Standard Stateful Rule Groups in AWS Network Firewall. https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-basic.html

</details>

<a id="q65"></a>

## Q65

<!-- source: OFF1Q65 · Multiple Choice · 3 minutes 58 seconds -->



A company uses AWS Organizations with OUs in a single organization. The OUs are Finance, HR, IT, and Recruiting. Each OU contains several accounts. All the OUs have different SCPs attached to them. The HR and Recruiting OUs share some common policy requirements. However, the Recruiting OU has some additional required restrictions. When the company needs to create new common SCP restrictions for the HR and Recruiting OUs, the company wants to avoid duplicating effort to update both SCPs.

Which solution will meet these requirements with the LEAST operational effort?

- **A.** Rename the Recruiting OU to Recruiting\_Old. Create a new OU named Recruiting as a child OU under the HR OU. Move the accounts that are under Recruiting\_Old to the new Recruiting OU. Remove the duplicate rules from the SCP for the Recruiting\_Old OU. Attach the updated SCP to the new Recruiting OU. Remove the Recruiting\_Old OU from the organization.
- **B.** Rename the HR OU to HR\_Old. Create a new OU named HR as a child OU under the Recruiting OU. Move the accounts that are under HR\_Old to the new HR OU. Remove the duplicate rules from the SCP for the HR\_Old OU. Attach the updated SCP to the new HR OU. Remove the HR\_Old OU from the organization.
- **C.** Move the accounts that are under the HR OU out of the organization. Remove the HR OU. Recreate the HR OU as a child OU under the Recruiting OU. Add the accounts back into the new HR OU. Remove the duplicate rules from the SCP for the HR OU. Attach the updated SCP to the new HR OU.
- **D.** Move the accounts that are under the Recruiting OU out of the organization. Remove the Recruiting OU. Recreate the Recruiting OU as a child OU under the HR OU. Add the accounts back into the new Recruiting OU. Remove the duplicate rules from the SCP for the Recruiting OU. Attach the updated SCP to the new Recruiting OU.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** HR and Recruiting share SCP requirements, Recruiting stricter, avoid duplicate effort, LEAST effort

🪤 **Your trap:** Picked removing accounts from the organization and re-inviting them — far more effort than moving accounts between OUs.

🧠 **Rule:** Shared + extra restrictions = nest the stricter OU under the shared one (SCPs inherit); move accounts between OUs, never out of the org.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Trước:   Root ── Finance
              ├─ HR          (SCP chung + ...)
              ├─ IT
              └─ Recruiting  (SCP chung + THÊM restriction)

Sau:     Root ── HR  (SCP chung)
                  └─ Recruiting (chỉ SCP phần THÊM, kế thừa SCP của HR)
```

Mục tiêu: sửa rule chung một lần, **LEAST operational effort**. Đáp án đúng: **A**. Anh chọn D.

#### Cụm khác biệt quyết định

Bốn đáp án khác nhau ở hai chỗ: **OU nào làm con** và **cách di chuyển account**.

- Anh chọn D: "Move the accounts ... **out of the organization**. Remove the Recruiting OU. Recreate ... **Add the accounts back**".
- Đáp án A: "Rename the Recruiting OU to Recruiting_Old. Create a new OU ... **Move the accounts** that are under Recruiting_Old to the new Recruiting OU".

Vì sao stem chọn A:
- "LEAST operational effort": di chuyển account **giữa các OU** là thao tác đơn giản. Đưa account **ra khỏi organization** rồi mời lại cần gửi invitation mới, nhiều việc hơn nhiều.
- SCP **kế thừa** từ OU cha xuống OU con. Recruiting có thêm restriction nên là **con** của HR; SCP chung đặt ở HR, SCP của Recruiting chỉ giữ phần bổ sung.

#### Anh chọn D: vì sao trông đúng và sai ở đâu

D chọn đúng hướng lồng (Recruiting làm con của HR) nên cấu trúc cuối cùng đúng. Sai ở cách thực hiện: rút account khỏi organization rồi thêm lại. AWS: moving an account out of the organization requires new invitations, so it takes more operational effort than moving accounts between OUs.

#### Các đáp án còn lại

- **B**: lồng ngược. HR làm con của Recruiting nghĩa là HR bị kế thừa các restriction thêm của Recruiting. Đúng ra Recruiting (nhiều restriction hơn) phải là con. Cách di chuyển (move giữa OU) thì ổn.
- **C**: vừa lồng ngược, vừa rút account khỏi organization.

| Đáp án | Hướng lồng | Cách di chuyển account |
|---|---|---|
| **A** | Recruiting con của HR (đúng) | Move giữa OU (nhẹ) |
| B | HR con của Recruiting (sai) | Move giữa OU |
| C | HR con của Recruiting (sai) | Ra khỏi org, mời lại (nặng) |
| D | Recruiting con của HR (đúng) | Ra khỏi org, mời lại (nặng) |

Cách đọc nhanh: chọn đáp án có **hướng đúng** trước (A, D), sau đó loại đáp án dùng "out of the organization".

#### Lưu ý thực tế

- SCP là hàng rào cho phép tối đa: quyền hiệu lực của account là giao của SCP ở mọi cấp từ root xuống OU chứa nó.

#### Quy tắc nhớ cho thi

- **Thấy "chung + thêm restriction"** → OU **có thêm restriction làm con**, SCP chung đặt ở OU cha.
- **Thấy "move accounts out of the organization"** → gần như luôn sai nếu đề hỏi LEAST effort.
- Di chuyển account giữa OU: `move-account`, không cần invitation.

### TD explanation

A ✔. Organizations gives you the ability to create new OUs and to move accounts between OUs. Because the SCP for Recruiting has more restrictions than the SCP for HR, Recruiting should be the child OU with the more restrictive SCP attached. This solution requires minimal operational overhead.
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html
  For more information about SCP policy inheritance, see Understanding Policy Inheritance. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance.html

B. Organizations gives you the ability to create new OUs and to move accounts between OUs. However, because the SCP for Recruiting has more restrictions than the SCP for HR, the Recruiting OU should be the child with the more restrictive SCP attached.
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html
  For more information about SCP policy inheritance, see Understanding Policy Inheritance. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_policies\_inheritance.html

C. If you move an account out of an organization, you need to issue new invitations to add the account back to the organization. This solution requires more operational effort than a solution that moves accounts between OUs.
  For more information about how to invite an AWS account to join an organization, see Inviting an AWS Account to Join Your Organization. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_accounts\_invites.html
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html

D. If you move an account out of an organization, you need to issue new invitations to add the account back to the organization. This solution requires more operational effort than a solution that moves accounts between OUs.
  For more information about how to invite an AWS account to join your organization, see Inviting an AWS Account to Join Your Organization. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_accounts\_invites.html
  For more information about OU management, see Managing Organizational Units (OUs). https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_manage\_ous.html

</details>

<a id="q66"></a>

## Q66

<!-- source: OFF1Q66 · Multiple Choice · 2 minutes 34 seconds -->



A company's chief financial officer (CFO) wants advanced notification if projections show that the costs for Amazon EC2 instances will exceed 75% of the company's monthly AWS budget. To reduce costs, the CFO wants specific EC2 instances to stop when the CFO receives the advanced notification. A solutions architect plans to use an AWS Budgets alert as part of the solution.

Which solution will meet the CFO's requirements with the LOWEST risk of future overspending?

- **A.** Create an alert based on projected costs of 75% of the monthly budget, filtered on instance type. Add an AWS Budgets action to stop the specified EC2 instances.
- **B.** Create an alert based on actual costs of 75% of the monthly budget, filtered on instance type. Send an alert to a systems operator to stop the specified EC2 instances.
- **C.** Create an alert based on actual costs of 75% of the monthly budget, filtered on instance type. Add an AWS Budgets action to stop the specified EC2 instances.
- **D.** Create an alert based on projected costs of 75% of the monthly budget, filtered on instance type. Send an alert to a systems operator to stop the specified EC2 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** projected EC2 costs, notify CFO, stop instances, LOWEST risk of overspending

🪤 **Your trap:** Picked sending the alert to an operator to stop instances manually; human delay leaves the overspend risk.

🧠 **Rule:** Budgets alert on forecasted cost + Budgets action (stop EC2/RDS, apply IAM/SCP) = automatic guardrail.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Forecast chi phí EC2 ──► chạm 75% budget tháng
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
    Gửi alert cho operator          AWS Budgets action
    (người dừng EC2 bằng tay)       (tự động stop EC2)
```

Yêu cầu: báo trước (advanced notification), dừng EC2 chỉ định, **LOWEST risk of future overspending**. Đáp án đúng: **A**. Anh chọn D.

#### Cụm khác biệt quyết định

Hai cặp khác biệt: **projected vs actual** và **action vs operator**.

- Anh chọn D: "alert based on **projected** costs ... **Send an alert to a systems operator** to stop the specified EC2 instances".
- Đáp án A: "alert based on **projected** costs ... **Add an AWS Budgets action** to stop the specified EC2 instances".

Vì sao stem chọn A:
- "Advanced notification if **projections** show..." nên phải dùng **forecasted/projected**; alert theo actual thì đã quá muộn (loại B, C).
- "LOWEST risk of future overspending": cần dừng **ngay và tự động**. Phụ thuộc operator có độ trễ và rủi ro quên, nên overspending vẫn có thể xảy ra. Budgets action chạy tự động khi vượt ngưỡng.

#### Anh chọn D: vì sao trông đúng và sai ở đâu

D chọn đúng "projected" nên đáp ứng phần thông báo trước. Sai ở bước dừng instance thủ công. AWS: manual step "could result in overspending if the systems operator does not stop the EC2 instances quickly".

#### Các đáp án còn lại

- **B**: actual cost thì muộn, lại còn thủ công.
- **C**: dừng tự động nhưng theo actual nên chỉ kích hoạt sau khi đã chi.

| Đáp án | Điều kiện | Cách dừng EC2 | Đánh giá |
|---|---|---|---|
| **A** | Projected | Budgets action (tự động) | Đáp ứng đủ |
| D | Projected | Operator (thủ công) | Trễ, rủi ro còn |
| C | Actual | Budgets action | Quá muộn |
| B | Actual | Operator | Muộn và thủ công |

#### Quy tắc nhớ cho thi

- **Thấy "projected/forecasted ... advance notice"** → alert dựa trên **forecast**.
- **Thấy "LOWEST risk of overspending" / "automatically stop"** → **AWS Budgets action** (stop EC2/RDS, hoặc áp IAM/SCP policy), không dựa vào người.
- Loại ngay đáp án "send alert to operator to stop" khi đề nhấn mạnh rủi ro.

### TD explanation

A ✔. This AWS Budgets alert would activate when the projected expenditure reaches the threshold. An automatic AWS Budgets action is the best way to stop the EC2 instances. This automatic stop would prevent future overspending.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

B. This AWS Budgets alert would activate when the actual expenditure reaches the threshold. The requirements are based on projected spending. An alert based on actual spending would be too late.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

C. This AWS Budgets alert would activate when the actual expenditure reaches the threshold. The requirements are based on projected spending. An alert based on actual spending would be too late.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

D. This AWS Budgets alert could partially meet the requirements because it would activate an alert based on projected expenditure. However, the manual step that requires the systems operator to stop the specified EC2 instances could result in overspending if the systems operator does not stop the EC2 instances quickly. An automatic AWS Budgets action is the best way to stop the EC2 instances. The automatic stop would prevent future overspending.
  For more information about AWS Budgets, see Managing Your Costs with AWS Budgets. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html

</details>

<a id="q68"></a>

## Q68

<!-- source: OFF1Q68 · Multiple Choice · 1 minutes 54 seconds -->



A financial services company loaded millions of historical stock trades into an Amazon DynamoDB table. The table uses on-demand capacity mode. Once each day at midnight, a few million new records are loaded into the table. Application read activity against the table happens in bursts throughout the day. A limited set of keys are repeatedly looked up. The company needs to reduce costs associated with DynamoDB.

Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use provisioned capacity mode. Purchase Savings Plans in AWS Cost Explorer.
- **B.** Deploy DynamoDB Accelerator (DAX). Use provisioned capacity mode. Configure DynamoDB auto scaling.
- **C.** Deploy an Amazon ElastiCache cluster in front of the DynamoDB table.
- **D.** Deploy DynamoDB Accelerator (DAX). Configure DynamoDB auto scaling. Purchase Savings Plans in AWS Cost Explorer.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** DynamoDB on-demand, bursts, few hot keys repeatedly read, reduce cost, LEAST overhead

🪤 **Your trap:** Picked DAX + Savings Plans; Savings Plans do not cover DynamoDB.

🧠 **Rule:** Hot keys → DAX; predictable load → provisioned capacity + auto scaling (or reserved capacity). Savings Plans = EC2/Fargate/Lambda/SageMaker only.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Ứng dụng ──(đọc dồn theo đợt, ít key lặp lại)──► DynamoDB (on-demand)
Mỗi ngày 00:00: nạp vài triệu record mới (có lịch, dự đoán được)
Mục tiêu: giảm chi phí, LEAST operational overhead
```

Hai yếu tố: (1) **key nóng đọc lặp lại** → cache; (2) tải **dự đoán được** → provisioned thay vì on-demand. Đáp án đúng: **B (DAX + provisioned + auto scaling)**. Anh chọn D.

#### Cụm khác biệt quyết định

B và D cùng có DAX và auto scaling. Khác nhau đúng một cụm:

- Anh chọn D: "Configure DynamoDB auto scaling. **Purchase Savings Plans in AWS Cost Explorer**" (và không nêu chuyển sang provisioned).
- Đáp án B: "**Use provisioned capacity mode**. Configure DynamoDB auto scaling."

Vì sao stem chọn B:
- **Auto scaling của DynamoDB chỉ hoạt động với provisioned mode**, không dùng được với on-demand. Bảng đang on-demand, D không chuyển mode nên auto scaling không áp dụng được.
- **Savings Plans không áp dụng cho DynamoDB** (Savings Plans chỉ cho compute như EC2, Fargate, Lambda, SageMaker). DynamoDB có **reserved capacity** riêng, và cũng không mua Savings Plans qua Cost Explorer theo cách D mô tả.

#### Anh chọn D: vì sao trông đúng và sai ở đâu

D trông đúng vì gom ba công cụ giảm chi phí: DAX cho key nóng, auto scaling cho burst, Savings Plans cho giảm giá cam kết. Nhưng hai thành phần sau không dùng được trong bối cảnh này (auto scaling cần provisioned; Savings Plans không có cho DynamoDB). AWS: "This combination of services cannot be implemented together."

#### Các đáp án còn lại

- **A**: provisioned capacity là đúng hướng cho tải dự đoán được, nhưng không giải quyết việc đọc lặp lại ít key (không có cache), lại dùng Savings Plans (không áp dụng DynamoDB).
- **C (ElastiCache)**: cache được, nhưng phải tự quản hạ tầng và sửa code tích hợp. DAX được thiết kế riêng cho DynamoDB, tương thích API, overhead thấp hơn.

| Đáp án | Cache hot key | Tối ưu capacity | Vấn đề |
|---|---|---|---|
| **B** | DAX | Provisioned + auto scaling | Không |
| D | DAX | Auto scaling + Savings Plans | Auto scaling không dùng với on-demand; Savings Plans không có cho DynamoDB |
| A | Không | Provisioned + Savings Plans | Không cache; Savings Plans sai |
| C | ElastiCache | Không | Overhead cao hơn DAX |

#### Lưu ý thực tế

- Giảm giá cam kết cho DynamoDB: dùng **reserved capacity** (provisioned mode). Savings Plans không áp dụng cho DynamoDB.
- Với tải nạp theo lịch cố định mỗi ngày, provisioned + auto scaling (hoặc scheduled scaling) rẻ hơn on-demand.

#### Quy tắc nhớ cho thi

- **Thấy "key lặp lại / hot keys / read-heavy DynamoDB"** → **DAX**.
- **Thấy "tải dự đoán được, đang on-demand, giảm chi phí"** → chuyển **provisioned + auto scaling**.
- **Thấy "Savings Plans" + DynamoDB** → sai; DynamoDB dùng **reserved capacity**.
- **Auto scaling DynamoDB** chỉ đi với provisioned mode.

### TD explanation

A. Provisioned capacity mode with reserved capacity can reduce costs for predictable workloads. However, this solution does not address the repeated lookups of a limited key set. Savings Plans are not available for DynamoDB. You cannot purchase Savings Plans through Cost Explorer.
  Learn more about DynamoDB capacity modes. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html

B ✔. DAX provides in-memory caching for frequently accessed keys. This solution can reduce read costs significantly. DAX is purpose-built for DynamoDB tables. Therefore, this solution minimizes operational overhead. Provisioned capacity mode with auto scaling handles predictable daily load patterns more cost-effectively than on-demand mode for this workload pattern.
  Learn more about DAX. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html
  Learn more about DynamoDB auto scaling. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html

C. ElastiCache can cache frequently accessed data. However, this solution requires additional infrastructure management and integration code changes. DAX is purpose-built for DynamoDB caching and provides better integration with lower operational overhead.
  Learn more about DAX. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html
  Learn more about ElastiCache. https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html

D. DynamoDB auto scaling is not compatible with on-demand capacity mode. Savings Plans are not available for DynamoDB. You cannot purchase Savings Plans through Cost Explorer. This combination of services cannot be implemented together.
  Learn more about DynamoDB auto scaling. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html
  Learn more about Cost Explorer. https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html

</details>

<a id="q74"></a>

## Q74

<!-- source: OFF1Q74 · Multiple Choice · 2 minutes 1 seconds -->



A company is designing a new application that stores data in Amazon S3. The company creates an S3 bucket with default settings. According to company regulations, no user can delete objects or write over objects in the S3 bucket for a minimum of 5 years after the initial storage of the objects.

Which solution will meet these requirements?

- **A.** Create a new S3 bucket with S3 Versioning and S3 Object Lock turned on. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to compliance mode. Move the existing objects to the new S3 bucket.
- **B.** Create a new S3 bucket with S3 Versioning and S3 Object Lock turned on. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to governance mode. Move the existing objects to the new S3 bucket.
- **C.** Modify the existing S3 bucket by turning on S3 Versioning and S3 Object Lock. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to governance mode.
- **D.** Modify the existing S3 bucket by turning on S3 Versioning and S3 Object Lock. Configure Object Lock with a retention period of 5 years. Set the Object Lock retention to compliance mode.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** existing bucket default settings, no delete or overwrite for 5 years, Object Lock compliance mode

🪤 **Your trap:** Picked enabling Object Lock on the existing bucket; the exam key assumes Object Lock only on new buckets. (Real AWS: Object Lock can be enabled on existing versioned buckets since late 2023.)

🧠 **Rule:** WORM for N years = Versioning + Object Lock compliance mode with default retention. Exam key: create a new bucket and move objects.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Bucket hiện tại (default settings, đã có object)
        │
        ├─ Cách 1: tạo bucket MỚI bật Versioning + Object Lock, di chuyển object sang   (A, B)
        └─ Cách 2: sửa bucket HIỆN CÓ để bật Object Lock                                 (C, D)

Yêu cầu: không ai xóa hoặc ghi đè trong tối thiểu 5 năm
```

Đáp án đúng theo đề: **A**. Anh chọn D.

#### Cụm khác biệt quyết định

Hai cặp khác biệt: **bucket mới vs bucket hiện có** và **compliance vs governance**.

- Anh chọn D: "**Modify the existing** S3 bucket by turning on S3 Versioning and S3 Object Lock ... **compliance mode**".
- Đáp án A: "**Create a new S3 bucket** with S3 Versioning and S3 Object Lock turned on ... **compliance mode**. Move the existing objects to the new S3 bucket."

Vì sao stem chọn A:
- Theo giải thích của đề: "you can configure Object Lock only when you first create a bucket", nên bucket hiện có (default settings) không bật được, phải tạo bucket mới rồi chuyển object.
- "no user can delete ... or write over": phải là **compliance mode**. Trong compliance mode không ai kể cả root user xóa hoặc ghi đè được trong thời gian retention. Governance mode vẫn cho user có quyền phù hợp gỡ lock rồi xóa (loại B, C).

#### Anh chọn D: vì sao trông đúng và sai ở đâu

D chọn đúng **compliance mode** và 5 năm, nên chỉ sai theo đề ở chỗ "modify the existing bucket". Đây là câu "twin options": A và D giống hệt nhau về mode, chỉ khác tạo mới hay sửa bucket cũ, và đề coi sửa bucket cũ là không khả thi.

#### Các đáp án còn lại

- **B**: bucket mới đúng, nhưng **governance mode** cho phép user có quyền (ví dụ `s3:BypassGovernanceRetention`) gỡ lock và xóa, không đạt "no user".
- **C**: vừa sửa bucket cũ (theo đề là không được), vừa governance mode.

| Đáp án | Bucket | Mode | Kết quả theo đề |
|---|---|---|---|
| **A** | Mới + chuyển object | Compliance | Đúng |
| B | Mới | Governance | Sai: vẫn có người gỡ lock được |
| C | Hiện có | Governance | Sai hai chỗ |
| D | Hiện có | Compliance | Sai: theo đề không bật Object Lock trên bucket cũ |

#### Lưu ý thực tế

📝 Ghi chú kỹ thuật: từ cuối năm 2023, S3 Object Lock có thể bật trên **bucket hiện có** (bucket phải bật Versioning). Vì vậy trên AWS thật, lựa chọn D của anh hoạt động được. Đáp án thi (A) dựa trên quy tắc cũ "Object Lock chỉ bật khi tạo bucket" nên đã lỗi thời. Khi thi vẫn giữ đáp án **A** theo key của đề.


#### Quy tắc nhớ cho thi

- **Thấy "no user including root can delete/overwrite for N years"** → **Object Lock compliance mode**.
- **Thấy governance mode** → người có quyền bypass được, không đáp ứng "no user".
- **Thấy "existing bucket default settings" + Object Lock** → theo key thi: **tạo bucket mới và chuyển object** (dù thực tế đã bật được trên bucket cũ).

### TD explanation

A ✔. Object Lock with a 5-year retention period would lock the objects and prevent the objects from being overwritten or deleted. In compliance mode, objects cannot be overwritten or deleted by any user, including the root user of the account, for the duration of the retention period. Because you can configure Object Lock only when you first create a bucket, you would need a new bucket.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html
  For more information about Object Lock retention modes, see Retention Modes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes

B. Object Lock with a 5-year retention period would lock the objects and prevent the objects from being overwritten or deleted. However, in governance mode, a user that has appropriate permissions could remove the lock and delete the objects.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html
  For more information about Object Lock retention modes, see Retention Modes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes

C. You can configure S3 Versioning for an existing S3 bucket, but you can configure Object Lock only when you first create a bucket. You cannot configure Object Lock for a bucket that already exists. In governance mode, a user that has appropriate permissions could remove the lock and delete the objects.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html
  For more information about Object Lock retention modes, see Retention Modes. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes

D. You can configure S3 Versioning for an existing S3 bucket, but you can configure Object Lock only when you first create a bucket. You cannot configure Object Lock for a bucket that already exists.
  For more information about Object Lock, see How S3 Object Lock Works. https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html

</details>

---

# Group B — Working but wrong fit: the decisive requirement was overlooked (rotation, partial failure, unexpected peak, AZ scope, FIPS level, predictable price) (11)

<a id="q11"></a>

## Q11

<!-- source: OFF1Q11 · Multiple Choice · 1 minutes 32 seconds -->



A company has a serverless application that is backed by an Amazon RDS database. The company's AWS Lambda functions share the same user account to access the database.

A database administrator updates the password in the database to comply with security policies. Shortly after the update, several Lambda functions fail. The user receives an error message for credentials that are not valid. After investigating the error, a solutions architect discovers that the affected Lambda functions use hardcoded credentials. The solutions architect needs to address the errors and improve the security of the credentials.

Which solution will meet these requirements with the LEAST development effort?

- **A.** Store the credentials in AWS Systems Manager Parameter Store. Update the Lambda functions to retrieve the user name and password from Parameter Store. Configure an Amazon EventBridge rule that invokes a Lambda function to update Parameter Store whenever the password is changed in the RDS database.
- **B.** Store the user name and password in AWS Secrets Manager. Update the Lambda functions to retrieve the user name and password from Secrets Manager. Configure an alternating users automatic rotation of the credentials as required.
- **C.** Create a Lambda function to update the credentials in the RDS database. Schedule the Lambda function to run as required. Configure an Amazon EventBridge rule that invokes a Lambda function to update the hardcoded passwords whenever the password is changed in the RDS database.
- **D.** Store the user name and password in AWS Secrets Manager. Update the Lambda functions to retrieve the user name and password from Secrets Manager. Configure a single user automatic rotation of the credentials as required.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** Lambda shares RDS credentials, hardcoded, errors on password change, improve security, LEAST development effort

🪤 **Your trap:** Picked Parameter Store + EventBridge-driven custom rotation; Parameter Store has no native RDS rotation, so you build it yourself.

🧠 **Rule:** DB credentials + rotation with least effort = Secrets Manager managed rotation (single-user/alternating). Parameter Store = config/secrets without built-in rotation.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Lambda functions ──(hardcoded user/password)──► Amazon RDS
                                                   ▲
DBA đổi password ──────────────────────────────────┘
        → Lambda lỗi "credentials not valid"

Yêu cầu: bỏ hardcode + tăng bảo mật + LEAST development effort
```

Đáp án đúng: **D (Secrets Manager + single user rotation)**. Anh chọn **A (Parameter Store + EventBridge + Lambda tự viết)**.

#### Yêu cầu quyết định bị bỏ sót

Cụm từ quyết định là **"LEAST development effort"** kèm **"improve the security of the credentials"** (credential của DB bị đổi password). A có lưu credential an toàn được, nên "chạy được một phần", nhưng phần xoay (rotate) và đồng bộ password phải tự code. Đề hỏi giải pháp ít code nhất, tức là dịch vụ có **managed rotation** sẵn.

#### Vì sao D đúng

- **Secrets Manager** thay hardcode bằng API call lấy secret lúc chạy.
- Secrets Manager **tự rotate password của RDS** (rotation function do AWS cung cấp), không cần viết Lambda mới.
- Database chỉ có **một application user** dùng chung, nên chiến lược phù hợp là **single user rotation**. TD nói rõ: giải pháp này không cần Lambda mới nên ít development effort nhất.

#### Vì sao A (đáp án Anh chọn) không đạt

Parameter Store lưu được credential an toàn, nhưng **không có native rotation cho RDS**. Anh phải tự viết:

```
RDS password đổi → EventBridge rule → Lambda tự viết → cập nhật Parameter Store
```

TD: cần phát triển code đáng kể, và vẫn phải cập nhật database thủ công. Đây là đúng thứ đề muốn tránh.

#### Các đáp án còn lại

- **B sai:** cũng dùng Secrets Manager nhưng chọn **alternating users rotation** (xoay luân phiên hai user trong một secret). Kịch bản chỉ có **một application user**, nên single user mới khớp.
- **C sai:** tự viết nhiều Lambda để đổi password ở cả database lẫn ứng dụng, tốn code nhất và vẫn dính hardcode.

#### Bảng so sánh

| Cách | Lưu an toàn | Rotation RDS | Code phải viết |
|---|---|---|---|
| A. Parameter Store + EventBridge | Có | Không có sẵn | Lambda cập nhật Parameter Store |
| B. Secrets Manager, alternating users | Có | Có | Không, nhưng sai mô hình (1 user) |
| C. Lambda tự đổi password | Không | Tự làm | Nhiều Lambda |
| **D. Secrets Manager, single user** | Có | Có | **Không** |

#### Lưu ý thực tế

- **Alternating users** thường dùng khi cần **gần như không gián đoạn** (một user luôn hợp lệ khi user kia đang đổi password). Nó cần hai user trong DB. Đề này chỉ có một user nên single user là đáp án.
- Lambda cần quyền IAM đọc secret (`secretsmanager:GetSecretValue`) và nên cache secret để giảm số call.

#### Quy tắc nhớ cho thi

- **Thấy "credentials + rotation + RDS + least effort"** → **Secrets Manager managed rotation**.
- **Thấy "Parameter Store"** → lưu config/secret đơn giản, **không có rotation DB native**.
- **Thấy "một user duy nhất"** → **single user rotation**; **"hai user, tránh gián đoạn"** → **alternating users**.
- **Thấy "tự viết Lambda để rotate"** khi đề hỏi LEAST effort → loại.

### TD explanation

A. Parameter Store can securely store the credentials. However, the creation of an extra Lambda function to rotate the password involves significant code development. This solution also requires manual updates of the database.
  For more information about Parameter Store, see AWS Systems Manager Parameter Store. https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html

B. Secrets Manager replaces hardcoded credentials with API calls to retrieve secrets programmatically. You can configure Secrets Manager to automatically rotate RDS database passwords. An alternating users rotation updates credentials for two users in one secret. However, in this scenario, the database has only a single application user account.
  For more information about Secrets Manager, see What is AWS Secrets Manager? https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
  For more information about rotation strategies, see Rotation Strategies. https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets\_strategies.html

C. Significant code development would be required to create multiple Lambda functions to rotate the passwords both in the database and the applications.
  For more information about EventBridge notifications for Amazon RDS, see Creating a Rule that Triggers on an Amazon RDS Event. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-cloud-watch-events.html

D ✔. Secrets Manager replaces hardcoded credentials with API calls to retrieve secrets programmatically. You can configure Secrets Manager to automatically rotate RDS database passwords. In this scenario, the database has a single application user account. For this reason, the single user rotation strategy would be appropriate. This solution requires no new Lambda functions, so it requires the least development effort.
  For more information about Secrets Manager, see What is AWS Secrets Manager? https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
  For more information about rotation strategies, see Rotation Strategies. https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets\_strategies.html

</details>

<a id="q16"></a>

## Q16

<!-- source: OFF1Q16 · Multiple Choice · 3 minutes 34 seconds -->



During migration to the AWS Cloud, a company modernized an application to use a microservices architecture. The company will deploy the application across multiple AWS Regions to meet latency and disaster recovery requirements. During both full and partial failures, the traffic must be automatically rerouted to the healthy deployments in other Regions. The company will route traffic to an Amazon API Gateway API by using a custom domain name that the company manages with Amazon Route 53. The company will monitor the infrastructure, including API Gateway endpoints, by using multiple Amazon CloudWatch metrics.

Which solution will route user requests to fully functional microservices?

- **A.** Configure Route 53 Application Recovery Controller routing controls and health checks for each deployment. Create AWS Lambda functions that will be invoked based on each resource’s metric alarms. Use the Lambda functions to toggle routing controls to automate routing appropriately.
- **B.** Configure Route 53 health checks for each Regional API Gateway endpoint to automate routing appropriately.
- **C.** Select the Route 53 Evaluate Target Health option for each record set to automate routing appropriately.
- **D.** Configure Route 53 Application Recovery Controller readiness checks for each resource type of the application. Create AWS Lambda functions that will be invoked based on readiness checks. Use the Lambda functions to update the Route 53 record sets to automate routing appropriately.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** multi-Region API Gateway, full AND partial failures, reroute automatically, CloudWatch metrics

🪤 **Your trap:** Picked Route 53 Evaluate Target Health; it only sees the endpoint record, not partial failures inside the microservices.

🧠 **Rule:** Route on application health from many metrics, incl. partial failures = Route 53 Application Recovery Controller routing controls driven by alarms + Lambda.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users ─► Route 53 (custom domain) ─┬─► Region 1: API Gateway + microservices
                                   └─► Region 2: API Gateway + microservices

Giám sát: nhiều CloudWatch metrics (cả API Gateway endpoint lẫn các thành phần khác)
Yêu cầu: full VÀ partial failures → tự động chuyển sang deployment khỏe
```

Đáp án đúng: **A (ARC routing controls + health checks + CloudWatch alarm + Lambda)**. Anh chọn **C (Evaluate Target Health)**.

#### Yêu cầu quyết định bị bỏ sót

Cụm từ quyết định: **"full and partial failures"** cùng **"multiple Amazon CloudWatch metrics"**. Evaluate Target Health chỉ nhìn tình trạng của endpoint (API Gateway) mà record trỏ tới. Nếu API Gateway vẫn sống nhưng một microservice phía sau hỏng (partial failure) thì Route 53 vẫn thấy "healthy" và tiếp tục gửi traffic vào Region lỗi.

#### Vì sao A đúng

```
CloudWatch metrics (nhiều thành phần) → Alarm → Lambda
        → bật/tắt ARC routing control
        → Route 53 health check (gắn với routing control) healthy/unhealthy
        → DNS chuyển traffic sang Region khỏe
```

- **Routing controls** là công tắc on/off để chuyển traffic giữa các replica, dựa trên Route 53 health checks.
- Alarm + Lambda cho phép tự động hóa dựa trên **nhiều metric từ nhiều thành phần**, nên bắt được cả partial failure.

#### Vì sao C (đáp án Anh chọn) không đạt

Evaluate Target Health hoạt động ở mức endpoint. TD: không phát hiện được partial failure trong ứng dụng bằng cách giám sát API Gateway endpoint, nên không đáp ứng yêu cầu.

#### Các đáp án còn lại

- **B sai:** Route 53 health check cho từng Regional API Gateway endpoint, cùng lỗi như C: chỉ thấy endpoint, không thấy partial failure bên trong ứng dụng.
- **D sai:** **readiness checks** của ARC là tính năng **đánh giá** (cấu hình, capacity, network routing policy của môi trường recovery có sẵn sàng tiếp quản chưa). Bản thân nó không định tuyến traffic, và không phải tín hiệu sức khỏe runtime để failover.

#### Bảng so sánh

| Cách | Thấy partial failure | Tự chuyển traffic |
|---|---|---|
| **A. Routing controls + alarms + Lambda** | Có (nhiều metric) | Có |
| B. Health check trên API Gateway | Không | Có |
| C. Evaluate Target Health | Không | Có |
| D. Readiness checks | Không (chỉ đánh giá sẵn sàng) | Không |

#### Lưu ý thực tế

- **Readiness check** trả lời "Region dự phòng đã đủ sẵn sàng chưa?", còn **routing control** trả lời "bây giờ gửi traffic đi đâu?". Hai việc khác nhau, thường gặp ở đề DR.

#### Quy tắc nhớ cho thi

- **Thấy "partial failures" + "nhiều metrics"** → **ARC routing controls** điều khiển bởi alarm + Lambda.
- **Thấy "Evaluate Target Health" / health check endpoint** → chỉ cho full failure của endpoint.
- **Thấy "readiness check"** → đánh giá, không route traffic.

### TD explanation

A ✔. Route 53 Application Recovery Controller routing controls provide simple on/off switches that give you the ability to direct traffic from one replica to another. These routing controls are based on Route 53 health checks that you configure. The Route 53 health checks become healthy or unhealthy by toggling routing controls. Based on multiple metrics from various application components, you can automate the toggling of these routing controls with CloudWatch alarms and Lambda functions.
  For more information about Route 53 Application Recovery Controller routing controls, see Routing Control in Amazon Route 53 Application Recovery Controller. https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html
  For more information about how to create Route 53 Application Recovery Controller routing controls, see Create Routing Control Structures in ARC. https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create.html

B. You would not detect any partial failures within the application by monitoring API Gateway endpoints with Route 53 health checks. This option will not meet the requirements.
  For more information about Route 53 health checks, see How Amazon Route 53 Determines Whether a Health Check Is Healthy. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html

C. You would not detect any partial failures within the application by monitoring API Gateway endpoints with the Route 53 Evaluate Target Health option. This option will not meet the requirements.
  For more information about the Route 53 Evaluate Target Health option, see How Amazon Route 53 Chooses Records when Health Checking Is Configured. https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-how-route-53-chooses-records.html

D. A Route 53 Application Recovery Controller readiness check continuously monitors AWS resource configurations, capacity, and network routing policies. These checks give you the ability to monitor for changes that would affect your ability to enact a recovery operation. These checks ensure that you have scaled and configured the recovery environment appropriately to take over when necessary. However, this is an assessment feature which, by itself, will not route traffic to the healthy Regions.
  For more information about Route 53 Application Recovery Controller readiness checks, see Amazon Route 53 Application Recovery Controller Components. https://docs.aws.amazon.com/r53recovery/latest/dg/introduction-components.html

</details>

<a id="q17"></a>

## Q17

<!-- source: OFF1Q17 · Multiple Choice · 3 minutes 37 seconds -->



A company is hosting an ecommerce application on two Amazon EC2 instances behind an Application Load Balancer (ALB) across two Availability Zones. The application is performing well during normal sales activity. However, customers experience slow response times during unexpected peak sales activity.

Recently, one of the instances was accidentally stopped, resulting in a significant performance decrease. A solutions architect investigates the slow response times but finds no correlation between the peaks and changes in Amazon CloudWatch metrics for the EC2 instances. The solutions architect is planning to use Amazon EC2 Auto Scaling to help resolve the issues.

How should the solutions architect configure the Auto Scaling group to resolve these issues?

- **A.** Create a scheduled scaling policy for the Auto Scaling group. Configure the scheduled actions to increase the number of EC2 instances during the peak sales periods.
- **B.** Create a dynamic scaling policy for the Auto Scaling group. Configure a target tracking policy to increase the number of EC2 instances based on the average CPU utilization of the Auto Scaling group.
- **C.** Create a predictive scaling policy for the Auto Scaling group to scale based on forecast. Configure the scaling metric to be the request count per target on the ALB target group.
- **D.** Create a dynamic scaling policy for the Auto Scaling group. Configure the scaling metric to be the request count per target on the ALB target group.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** unexpected peak sales, slow responses, no correlation with time, two EC2 behind ALB

🪤 **Your trap:** Picked scheduled scaling; scheduled actions only fit predictable peaks.

🧠 **Rule:** Unpredictable load on ALB targets = dynamic target tracking on ALBRequestCountPerTarget. Scheduled scaling only for known calendars.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users ─► ALB ─┬─► EC2 (AZ-a)
              └─► EC2 (AZ-b)

Vấn đề: chậm khi có peak bán hàng BẤT NGỜ (unexpected)
        CloudWatch metric EC2 không tương quan với peak
Dự định: dùng EC2 Auto Scaling
```

Đáp án đúng: **D (dynamic scaling, target tracking theo request count per target của ALB)**. Anh chọn **A (scheduled scaling)**.

#### Yêu cầu quyết định bị bỏ sót

Cụm từ quyết định: **"unexpected peak sales activity"**. Scheduled scaling chạy theo ngày giờ đã đặt trước, nên chỉ hợp khi biết trước peak. Peak không báo trước thì lịch không bắt được. Thêm vào đó, đề nói metric EC2 (CPU...) **không tương quan** với peak, nên phải chọn metric phản ánh tải thật là số request.

#### Vì sao D đúng

- **Dynamic scaling** phản ứng theo nhu cầu thực tế, không cần biết trước thời điểm.
- TD: chỉ số khác biệt về hiệu năng trong kịch bản này là **số request gửi tới mỗi EC2 instance**. Target tracking theo **request count per target** của ALB target group sẽ scale đúng lúc.

```
Request tăng ─► RequestCountPerTarget vượt target
             ─► ASG thêm instance ─► tải mỗi instance giảm
```

#### Vì sao A (đáp án Anh chọn) không đạt

Scheduled scaling thực hiện scheduled actions theo ngày giờ. TD: lịch không xử lý được peak bất ngờ. Nó chạy được nếu đoán đúng giờ, nhưng chỉ phủ phần peak đã biết.

#### Các đáp án còn lại

- **B sai:** dynamic target tracking nhưng theo **average CPU**. Peak không tương quan với metric EC2 (gồm CPU), nên scale sai thời điểm.
- **C sai:** **predictive scaling** dự báo theo mẫu theo ngày/tuần. Peak xảy ra ở thời điểm bất ngờ nên không có mẫu để dự báo.

#### Bảng so sánh

| Cách | Cần peak dự đoán được | Metric dùng |
|---|---|---|
| A. Scheduled | Có (lịch cố định) | Không (theo giờ) |
| B. Target tracking CPU | Không | CPU, không tương quan |
| C. Predictive | Có (mẫu lặp lại) | Dự báo |
| **D. Target tracking request count** | **Không** | **ALBRequestCountPerTarget** |

#### Lưu ý thực tế

- Sự cố "một instance bị stop làm hiệu năng tụt" cũng là lý do cần ASG: đặt min capacity và health check để tự thay instance.
- Metric `ALBRequestCountPerTarget` là metric được hỗ trợ sẵn cho target tracking với ALB.

#### Quy tắc nhớ cho thi

- **Thấy "unexpected / unpredictable peak"** → **dynamic scaling**, không scheduled, không predictive.
- **Thấy "ALB + CPU không tương quan"** → target tracking theo **request count per target**.
- **Thấy "known calendar / sale cố định giờ"** → scheduled; **"mẫu lặp theo ngày/tuần"** → predictive.

### TD explanation

A. Scheduled scaling uses scheduled actions that are performed automatically as a function of date and time. A scheduled time would not address the unexpected peak activity.
  For more information about scheduled scaling, see Scheduled Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule\_time.html

B. Dynamic scaling scales the capacity of an Auto Scaling group in response to changes in demand. Target tracking based on this metric would not scale the group at the appropriate times because the peaks in sales do not correlate with any CloudWatch metrics for EC2 instances, including CPU utilization.
  For more information about dynamic scaling, see Dynamic Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html
  For more information about how to choose metrics for dynamic scaling, see Choosing Metrics. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#available-metrics

C. Predictive scaling changes the number of EC2 instances in an Auto Scaling group in advance of daily and weekly patterns in traffic flows. Predictive scaling is not a good option because the peak sales activities happen at unexpected times.
  For more information about predictive scaling, see Predictive Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html

D ✔. Dynamic scaling scales the capacity of an Auto Scaling group in response to changes in demand. The only performance differentiator in this scenario is the number of requests sent to each EC2 instance. A target tracking policy based on the number of requests from the ALB will appropriately scale the group.
  For more information about dynamic scaling, see Dynamic Scaling for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html
  For more information about how to choose metrics for dynamic scaling, see Choosing Metrics. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html#available-metrics

</details>

<a id="q19"></a>

## Q19

<!-- source: OFF1Q19 · Multiple Choice · 2 minutes 38 seconds -->



A solutions architect needs to create an infrastructure proposal for a web application. The application requires a resilient and highly available design across multiple Availability Zones. The solutions architect proposes the following:

A VPC with an internet gateway and a NAT gateway
One public subnet and one private subnet each in two different Availability Zones
An Amazon EC2 Auto Scaling group spread across multiple Availability Zones behind an internet-facing Application Load Balancer (ALB)
Amazon DynamoDB tables to store data

What should the solutions architect do to increase the resilience and availability of the proposed architecture?

- **A.** Create a second internet-facing ALB. Attach each ALB to a different subnet.
- **B.** Create a second internet gateway. Attach each internet gateway to a different subnet.
- **C.** Create DynamoDB global tables with two replicated tables that are stored in different AWS Regions.
- **D.** Create a second NAT gateway. Update the route tables on each private subnet as needed.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** resilient across multiple AZs, one NAT gateway, DynamoDB tables, increase resilience

🪤 **Your trap:** Picked DynamoDB global tables (multi-Region); DynamoDB is already multi-AZ. The single NAT gateway is the AZ-level single point of failure.

🧠 **Rule:** Multi-AZ HA review: find the one zonal resource — NAT gateway is per AZ, deploy one per AZ. Don't escalate to multi-Region when the ask is multi-AZ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC
├─ AZ-a: public subnet (ALB, NAT-GW)   private subnet (EC2 ASG)
└─ AZ-b: public subnet (ALB)           private subnet (EC2 ASG)
Internet Gateway (1) · NAT Gateway (chỉ 1) · DynamoDB

Yêu cầu: tăng resilience và availability ở mức multi-AZ
```

Đáp án đúng: **D (thêm NAT gateway thứ hai ở AZ khác, cập nhật route table)**. Anh chọn **C (DynamoDB global tables, multi-Region)**.

#### Yêu cầu quyết định bị bỏ sót

Cụm từ quyết định: **"resilient and highly available design across multiple Availability Zones"**. Đề hỏi **multi-AZ**, không phải multi-Region. Việc cần làm là tìm thành phần **gắn với một AZ** trong thiết kế. Chỉ có **NAT gateway** là zonal (một cái duy nhất đặt trong một AZ). Nếu AZ đó hỏng, instance ở private subnet của AZ còn lại mất đường ra internet.

⚠️ Lỗi lặp lại: Anh có xu hướng over-building, leo lên multi-Region khi đề chỉ yêu cầu multi-AZ. Trước khi chọn, hãy hỏi: "đề yêu cầu mức nào, AZ hay Region?"

#### Vì sao D đúng

TD: NAT gateway chỉ highly available **bên trong AZ nơi nó được deploy**. Cần một NAT gateway ở mỗi AZ:

```
private subnet AZ-a ─► NAT-GW AZ-a
private subnet AZ-b ─► NAT-GW AZ-b   (route table riêng cho từng private subnet)
```

#### Vì sao C (đáp án Anh chọn) không đạt

DynamoDB đã tự động nhân bản dữ liệu qua **nhiều AZ trong Region**. Global tables (nhân bản qua Region) giải bài toán khác, và không sửa điểm lỗi đơn (single point of failure) thật sự là NAT gateway. Tốn thêm chi phí và độ phức tạp mà không đáp ứng yêu cầu.

#### Các đáp án còn lại

- **A sai:** ALB vốn đã là dịch vụ highly available, scalable do AWS quản lý, không cần ALB thứ hai.
- **B sai:** internet gateway cũng highly available và scalable mặc định, hơn nữa một VPC dùng một IGW, không gắn "mỗi subnet một IGW".

#### Bảng: thành phần nào là zonal hay regional

| Thành phần | Phạm vi | Cần nhân bản? |
|---|---|---|
| ALB | Multi-AZ, AWS quản lý | Không |
| Internet gateway | HA, AWS quản lý | Không |
| DynamoDB | Multi-AZ trong Region | Không (với multi-AZ) |
| **NAT gateway** | **Một AZ** | **Có, mỗi AZ một cái** |

#### Quy tắc nhớ cho thi

- **Thấy "multi-AZ HA review"** → tìm thành phần zonal: **NAT gateway** (một cái mỗi AZ).
- **Thấy "across multiple AZs"** → đừng leo lên **multi-Region** (global tables, cross-Region).
- **ALB, IGW, DynamoDB, S3** → đã HA sẵn trong Region, không cần nhân đôi.

### TD explanation

A. You do not need to create a second internet-facing ALB to achieve a resilient architecture across Availability Zones. By default, an ALB is a highly available and scalable resource that is managed by AWS.
  For more information about ALBs, see Application Load Balancers. https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html

B. You do not need to create a second internet gateway to achieve a resilient architecture across Availability Zones. By default, an internet gateway is a highly available and scalable component that is managed by AWS.
  For more information about internet gateways, see Connect Subnets to the Internet Using an Internet Gateway. https://docs.aws.amazon.com/vpc/latest/userguide/VPC\_Internet\_Gateway.html

C. DynamoDB global tables are not necessary for this solution. Data in DynamoDB tables is automatically replicated across multiple Availability Zones in the Region where the tables are created. You do not need to create a global DynamoDB table to achieve a resilient architecture across Availability Zones.
  For more information about DynamoDB high availability, see What Is Amazon DynamoDB? https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

D ✔. You need to create a second NAT gateway in a separate Availability Zone to achieve a resilient architecture across Availability Zones. A NAT gateway is highly available only within the Availability Zone where it is deployed.
  For more information about the availability of NAT gateways, see NAT Gateway Basics. https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-basics

</details>

<a id="q21"></a>

## Q21

<!-- source: OFF1Q21 · Multi-Select · 1 minutes 50 seconds -->



A company runs an HPC cluster in an AWS Region. The cluster consists of a group of Linux instances that run a tightly coupled workload. The company is not satisfied with the current key performance indicators. The company needs to increase network throughput and reduce the network latency between the Amazon EC2 instances that make up the cluster.

Which combination of actions will meet these requirements?

- **A.** Select an EC2 instance type that supports the use of an Elastic Fabric Adapter (EFA).
- **B.** Use EC2 instances with burstable performance.
- **C.** Run the HPC cluster within a single Availability Zone.
- **D.** Deploy the EC2 instances in a partition placement group.
- **E.** Ensure that the EC2 instances run an AMI that supports paravirtual (PV).
- **F.** Disable CPU hyperthreading on the EC2 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, F · **You picked:** A, C, E

🔑 **Key words:** tightly coupled HPC, increase network throughput, reduce latency, Select THREE

🪤 **Your trap:** Picked a paravirtual (PV) AMI; PV is legacy and slower. Missed disabling hyperthreading, which helps tightly coupled HPC.

🧠 **Rule:** Tightly coupled HPC = EFA-capable instances + cluster placement / single AZ + disable hyperthreading (HVM AMIs, never PV).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
HPC cluster (Linux EC2) - tightly coupled workload
┌────┐ ◄──► ┌────┐ ◄──► ┌────┐   giao tiếp node-to-node liên tục
└────┘      └────┘      └────┘

Yêu cầu: tăng network throughput + giảm network latency
```

Đáp án đúng: **A, C, F**. Anh chọn **A, C, E**: đúng A và C, sai E (thiếu F).

#### Yêu cầu quyết định bị bỏ sót

Cụm từ quyết định: **"tightly coupled workload"** (HPC). Với HPC, các node cần băng thông cao, latency thấp, và tận dụng hết lõi tính toán thật. Phần còn thiếu là **tắt hyperthreading** (F), còn E (PV AMI) là lựa chọn lỗi thời, đi ngược hướng.

#### Ba đáp án đúng tạo thành một giải pháp

- **A. EFA-capable instance:** EFA là network device giúp tăng tốc HPC và machine learning, cho phép ứng dụng HPC scale tới hàng nghìn CPU/GPU với hiệu năng tương đương cluster on-premises.
- **C. Chạy trong một AZ:** các node ở cùng AZ cho latency thấp cần cho giao tiếp node-to-node.
- **F. Tắt hyperthreading:** Hyper-Threading làm một lõi vật lý hiện thành nhiều lõi logic. TD: hầu hết ứng dụng HPC được lợi khi tắt.

#### Vì sao E (đáp án Anh chọn) sai

Linux AMI có hai kiểu ảo hóa: **PV** và **HVM**. PV không tận dụng được các phần mở rộng phần cứng như **enhanced networking** hay GPU, nên không cải thiện hiệu năng cluster. Muốn hiệu năng cao phải dùng **HVM**.

#### Các đáp án còn lại

- **B sai:** burstable (họ T) cho CPU baseline và burst, nhưng không cải thiện network cho HPC.
- **D sai:** **partition placement group** trải instance ra các partition để giảm lỗi phần cứng tương quan. Nó **tăng** latency, ngược với mục tiêu. HPC cần cluster placement (gần nhau).

#### Bảng so sánh

| Lựa chọn | Tác động lên network | Kết luận |
|---|---|---|
| A. EFA | Throughput lên, latency xuống | Chọn |
| B. Burstable | Không đổi network | Loại |
| C. Single AZ | Latency thấp | Chọn |
| D. Partition PG | Latency tăng (ưu tiên chịu lỗi) | Loại |
| E. PV AMI | Không dùng được enhanced networking | Loại |
| F. Tắt hyperthreading | Hợp tải HPC | Chọn |

#### Quy tắc nhớ cho thi

- **Thấy "tightly coupled HPC"** → **EFA + cùng AZ (cluster placement) + tắt hyperthreading**.
- **Thấy "PV AMI"** → lỗi thời, luôn là **HVM**.
- **Thấy "partition placement group"** → chịu lỗi cho hệ phân tán lớn (Kafka, Hadoop), không phải HPC latency thấp.

### TD explanation

A ✔. An EFA is a network device that you can attach to an EC2 instance to accelerate HPC and machine learning applications. With an EFA, HPC applications can scale to thousands of CPUs or GPUs which results in the same application performance as on-premises HPC clusters with the additional benefit of the on-demand elasticity and flexibility of the AWS Cloud.
  For more information about EFAs, see Elastic Fabric Adapter. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html

B. The T instance family provides a baseline CPU performance with the ability to burst above the baseline at any time for as long as required. However, burstable performance instances would not typically improve network performance in an HPC cluster.
  For more information about burstable performance instances, see Burstable Performance Instances. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html

C ✔. If an HPC cluster runs within a single Availability Zone, workloads can achieve the low-latency network performance that is necessary for the tightly coupled node-to-node communication that is typical for HPC applications.
  For more information about network latency, see Architecture Guidelines and Decisions. https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-guidelines-and-decisions.html

D. Partition placement groups help reduce the likelihood of correlated hardware failures for an application. Deployment of EC2 instances in a partition placement group spreads EC2 instances across logical partitions and ensures that instances in different partitions do not share the same underlying hardware. A partition placement group would increase network latency, not reduce it.
  For more information about partition placement groups, see Partition Placement Groups. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#placement-groups-partition

E. Linux AMIs use one of two types of virtualization: PV or hardware virtual machine (HVM). Linux PV AMIs would not improve the performance of the cluster because they cannot take advantage of special hardware extensions, such as enhanced networking or GPU processing, to ensure that the EC2 instances are running.
  For more information about Linux AMI virtualization types, see Linux AMI Virtualization Types. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization\_types.html

F ✔. Intel Hyper-Threading Technology makes a single physical processor appear as multiple logical processors. Most HPC applications will benefit from disabling hyperthreading.
  For more information about Intel Hyper-Threading Technology, see Compute. https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute.html

</details>

<a id="q25"></a>

## Q25

<!-- source: OFF1Q25 · Multiple Choice · 3 minutes 48 seconds -->



A company uses several services to store important data within a single AWS Region. These services include Amazon S3, Amazon EBS, Amazon EFS, Amazon RDS, and on-premises storage servers. The company wants a backup and data protection solution that would offer Regional protection for all the company's existing data. The solution must automate the processes on AWS as much as possible. The company has configured AWS Storage Gateway Volume Gateway for the on-premises data.

Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Create an AWS Backup backup vault in another Region. Create a cross-Region backup plan in AWS Backup by using the vault that includes data that is in S3 buckets, EBS volumes, EFS file systems, RDS databases, and the Storage Gateway volumes.
- **B.** Create a read replica of the RDS databases in another Region. Create a cross-Region backup plan in AWS Backup that includes the data that is in S3 buckets, EBS volumes, EFS file systems, and the Storage Gateway volumes.
- **C.** Create EBS snapshots and copy the EBS snapshots to a different Region. Create a cross-Region backup plan in AWS Backup that includes data that is in S3 buckets, EFS file systems, RDS databases, and the Storage Gateway volumes.
- **D.** Configure AWS DataSync to replicate the data that is in EFS file systems to another Region. Create a cross-Region backup plan in AWS Backup that includes data that is in S3 buckets, EBS volumes, RDS databases, and the Storage Gateway volumes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** S3, EBS, EFS, RDS, Volume Gateway, Regional protection, automate, LEAST operational overhead

🪤 **Your trap:** Added RDS cross-Region read replicas on top of AWS Backup; replicas are not backups and add overhead. AWS Backup already covers RDS.

🧠 **Rule:** One service for S3/EBS/EFS/RDS/Storage Gateway backups with cross-Region copy = AWS Backup plan + vault in another Region.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Dữ liệu trong một Region:
S3 · EBS · EFS · RDS · on-premises (Storage Gateway Volume Gateway)
        │
        ▼
Cần: Regional protection (bản sao ở Region khác), tự động hóa tối đa
Yêu cầu: LEAST operational overhead
```

Đáp án đúng: **A (AWS Backup vault ở Region khác + cross-Region backup plan cho tất cả)**. Anh chọn **B (thêm RDS read replica cross-Region rồi mới dùng AWS Backup cho phần còn lại)**.

#### Yêu cầu quyết định bị bỏ sót

Cụm từ quyết định: **"LEAST operational overhead"** cùng **"automate the processes on AWS as much as possible"**. AWS Backup đã hỗ trợ cả năm nguồn (S3, EBS, EFS, RDS, Storage Gateway volumes) trong **một** plan. Mỗi dịch vụ phụ thêm là thêm việc vận hành.

#### Vì sao A đúng

```
AWS Backup plan (1 chỗ)
  ├─ S3 buckets
  ├─ EBS volumes
  ├─ EFS file systems
  ├─ RDS databases
  └─ Storage Gateway volumes
        │ cross-Region copy
        ▼
   Backup vault ở Region khác
```

Một dịch vụ, một policy, copy sang vault Region khác: Regional protection cho mọi dữ liệu với ít thao tác nhất.

#### Vì sao B (đáp án Anh chọn) không đạt

TD: **read replica không phải giải pháp backup**. Replica nhân bản cả thao tác xóa/hỏng dữ liệu, không có điểm khôi phục theo thời gian. Mà AWS Backup đã bao gồm RDS, nên replica chỉ thêm việc vận hành, không thêm giá trị đáp ứng yêu cầu.

#### Các đáp án còn lại

- **C sai:** tự tạo và copy EBS snapshot cross-Region, trong khi AWS Backup đã làm được cho EBS. Thêm bước thủ công không cần thiết.
- **D sai:** dùng **DataSync** nhân bản EFS sang Region khác, trong khi AWS Backup đã sao lưu EFS. Replica EFS không cần thiết và tăng overhead.

#### Bảng so sánh

| Cách | Dịch vụ phụ ngoài AWS Backup | Overhead |
|---|---|---|
| **A. AWS Backup cho tất cả** | Không | Thấp nhất |
| B. + RDS read replica | RDS replica | Cao hơn, replica không phải backup |
| C. + EBS snapshot copy tay | Snapshot copy | Cao hơn |
| D. + DataSync cho EFS | DataSync | Cao hơn |

#### Lưu ý thực tế

- Backup vault đích ở Region khác là phần tạo ra **Regional protection**; cross-Region copy cấu hình ngay trong backup plan.
- Read replica dùng cho scale đọc hoặc DR (promote khi sự cố), không thay cho backup có điểm khôi phục.

#### Quy tắc nhớ cho thi

- **Thấy "S3 + EBS + EFS + RDS + Storage Gateway + backup"** → **AWS Backup** một plan.
- **Thấy "Regional protection"** → **vault + cross-Region copy** trong plan.
- **Thấy "LEAST operational overhead"** → bỏ mọi dịch vụ phụ (DataSync, snapshot tay, replica).
- **Read replica** → không phải backup.

### TD explanation

A ✔. AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. A cross-Region backup plan would offer the required Regional protection for the data. This solution would incur the least operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
  For more information about cross-Region replication for Amazon S3, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario

B. AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. RDS read replicas are not a backup solution. Read replicas of the RDS databases would not address the requirements but would add unnecessary operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
  For more information about RDS read replicas, see Working with Read Replicas. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER\_ReadRepl.html

C. AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. However, it is not necessary to use DataSync to replicate the EBS volumes because AWS Backup can back up EBS volumes. Cross-Region replication would automatically protect the data that is in S3 buckets with less operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
  For more information about cross-Region replication for Amazon S3, see When to Use Cross-Region Replication. https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario
  For more information about how to copy EBS snapshots, see Copy an Amazon EBS Snapshot. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html

D. AWS Backup can automatically back up data that is in S3 buckets, Storage Gateway volumes, EBS volumes, EFS file systems, and RDS databases. Replicas of the EFS file systems are not necessary and would incur unnecessary operational overhead.
  For more information about AWS Backup, see What Is AWS Backup? https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
  For more information about DataSync, see What Is AWS DataSync? https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

</details>

<a id="q32"></a>

## Q32

<!-- source: OFF1Q32 · Multiple Choice · 3 minutes 16 seconds -->



A company wants to provide desktop as a service (DaaS) to a number of employees using Amazon WorkSpaces. WorkSpaces will need to access files and services hosted on premises with authorization based on the company's Active Directory. Network connectivity will be provided through an existing AWS Direct Connect connection.

The solution has the following requirements:

Credentials from Active Directory should be used to access on-premises files and services.
Credentials from Active Directory should not be stored outside the company.
End users should have single sign-on (SSO) to on-premises files and services once connected to WorkSpaces.

Which strategy should the solutions architect use for end user authentication?

- **A.** Create a service account in the on-premises Active Directory with the required permissions. Create an AD Connector in AWS Directory Service to be deployed on premises using the service account to communicate with the on-premises Active Directory. Ensure the required TCP ports are open from the WorkSpaces VPC to the on-premises AD Connector. Use the AD Connector as the directory for WorkSpaces.
- **B.** Create an AWS Managed Microsoft AD directory in the AWS Directory Service within the WorkSpaces VPC. Set up a one-way trust allowing users from the on-premises Active Directory to access resources in the AWS Managed Microsoft AD. Use AWS Managed Microsoft AD as the directory for WorkSpaces. Create an identity provider with IAM from an on-premises ADFS server. Allow users from this identity provider to assume a role with a policy allowing them to run WorkSpaces.
- **C.** Create a service account in the on-premises Active Directory with the required permissions. Create an AD Connector in AWS Directory Service within the WorkSpaces VPC using the service account to communicate with the on-premises Active Directory. Use the AD Connector as the directory for WorkSpaces.
- **D.** Create an AWS Managed Microsoft AD directory within the WorkSpaces VPC. Use the Active Directory Migration Tool (ADMT) with the Password Export Server to copy users from the on-premises Active Directory to AWS Managed Microsoft AD. Set up a one-way trust allowing users from AWS Managed Microsoft AD to access resources in the on-premises Active Directory. Use AWS Managed Microsoft AD as the directory for WorkSpaces.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** WorkSpaces, on-prem AD credentials, must not be stored outside the company, SSO to on-prem files

🪤 **Your trap:** Picked AWS Managed Microsoft AD with a trust; that creates a directory (and credentials) in AWS.

🧠 **Rule:** Use on-prem AD without storing anything in AWS = AD Connector (proxy, no caching). Managed AD = a real directory in AWS.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
WorkSpaces (VPC)  ──Direct Connect──►  On-premises Active Directory
      │                                   (files, services)
      └─ cần: login bằng AD credentials + SSO tới file/service on-prem
         Ràng buộc: credentials AD KHÔNG được lưu ngoài công ty
```

Đáp án đúng: **C (AD Connector trong WorkSpaces VPC)**. Anh chọn B (AWS Managed Microsoft AD + one-way trust + ADFS).

#### Yêu cầu quyết định bị bỏ sót

Câu hỏi có 3 yêu cầu, nhưng yêu cầu loại đáp án là câu **"credentials không được lưu ngoài công ty"**. Anh đọc "dùng AD" và nghĩ ngay tới Managed AD. Nhưng:

- **AD Connector** = directory gateway, chỉ **proxy** yêu cầu xác thực về AD on-prem, **không cache** gì trên cloud.
- **AWS Managed Microsoft AD** = một directory thật chạy trong AWS, có user/credential/object của riêng nó.

#### Đáp án đúng: C

AD Connector được đặt trong WorkSpaces VPC, dùng service account để nói chuyện với AD on-prem qua Direct Connect. User đăng nhập WorkSpaces bằng AD credentials, WorkSpaces là member của AD nên có SSO tới file/service on-prem. Không có credential nào nằm ở AWS.

#### Vì sao B không đạt

B tạo Managed AD trong AWS rồi dùng trust. Trust cho phép user on-prem vào Managed AD, nhưng bản thân Managed AD vẫn là directory lưu trữ trên AWS và WorkSpaces thuộc directory đó. Phần ADFS + IAM identity provider để chạy WorkSpaces làm phức tạp thêm mà không giải quyết ràng buộc "không lưu ngoài công ty". AWS còn chỉ ra phần Identity Center/Organizations không phù hợp ngữ cảnh này.

#### Các đáp án còn lại

- **A sai:** AD Connector **không thể deploy on-premises**. Nó chạy trong AWS (VPC của WorkSpaces). Chi tiết "deploy on premises" là bẫy.
- **D sai:** dùng ADMT + Password Export Server **copy user (và password) sang Managed AD** nên credentials nằm ngoài công ty, vi phạm yêu cầu trực tiếp. Trust one-way còn đặt hướng ngược với nhu cầu.

| Giải pháp | Credential lưu ở AWS? | Dùng AD on-prem làm nguồn xác thực |
|---|---|---|
| **AD Connector (C)** | Không (proxy, no cache) | Có |
| Managed AD + trust (B) | Có directory trong AWS | Gián tiếp |
| Managed AD + ADMT (D) | Có, copy cả user | Không (đã copy) |

#### Lưu ý thực tế

- AD Connector cần network tới AD on-prem (Direct Connect/VPN) và các port AD mở; cần service account có quyền delegate tối thiểu.
- Nếu on-prem AD mất kết nối, AD Connector không xác thực được (vì không cache). Đây là đánh đổi của "không lưu gì trên cloud".

#### Quy tắc nhớ cho thi

- **Thấy "dùng AD on-prem, không lưu credential trên AWS"** → **AD Connector**
- **Thấy "cần directory riêng trên AWS / chạy workload cần AD thật"** → **AWS Managed Microsoft AD**
- **Thấy "AD Connector on premises"** → sai, AD Connector chạy trong AWS
- **Thấy "copy user / ADMT"** → credentials rời công ty

### TD explanation

A. You cannot deploy AD Connector on premises.
  For more information about the requirements for AD Connector, see AD Connector Prerequisites. https://docs.aws.amazon.com/directoryservice/latest/admin-guide/prereq\_connector.html

B. To set up AWS IAM Identity Center with Amazon WorkSpaces Web, you would also need to set up AWS Organizations.
  For more information about how to set up IAM Identity Center for WorkSpaces, see Set Up IAM Identity Center as Your IdP. https://docs.aws.amazon.com/workspaces-web/latest/adminguide/sso-idp.html

C ✔. AD Connector is a directory gateway that you can use to redirect directory requests to your on-premises Active Directory without the need to cache any information in the cloud. This solution will authenticate the Active Directory credentials of the end users. The WorkSpaces will be members of the Active Directory that provide SSO to on-premises resources.
  For more information about AD Connector, see Active Directory Connector. https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory\_ad\_connector.html

D. This solution copies the users to AWS Managed Microsoft AD. However, the company requires a solution that does not store credentials from Active Directory outside the company.
  For more information about AWS Managed Microsoft AD, see AWS Managed Microsoft AD. https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory\_microsoft\_ad.html

</details>

<a id="q53"></a>

## Q53

<!-- source: OFF1Q53 · Multiple Choice · 3 minutes 59 seconds -->



A company recently deployed a new application that runs on a group of Amazon EC2 Linux instances in a VPC. In a peered VPC, the company launched an EC2 Linux instance that serves as a bastion host. The security group of the application instances allows access only on TCP port 22 from the private IP of the bastion host. The security group of the bastion host allows access to TCP port 22 from 0.0.0.0/0 so that system administrators can use SSH to remotely log in to the application instances from several branch offices.

While looking through operating system logs on the bastion host, a cloud engineer notices thousands of failed SSH logins to the bastion host from locations around the world. The cloud engineer wants to change how remote access is granted to the application instances and wants to meet the following requirements:

Eliminate brute-force SSH login attempts.
Retain a log of commands run during an SSH session.
Retain the ability to forward ports.

Which solution meets these requirements for remote access to the application instances?

- **A.** Configure the application instances to communicate with AWS Systems Manager. Grant access to the system administrators to use Session Manager to establish a session with the application instances. Terminate the bastion host.
- **B.** Configure the application instances to communicate with AWS Systems Manager. Grant access to the system administrators to issue commands to the application instances by using Systems Manager Run Command. Terminate the bastion host.
- **C.** Configure an AWS Client VPN endpoint and provision each system administrator with a certificate to establish a VPN connection to the application VPC. Update the security group of the application instances to allow traffic from only the Client VPN IPv4 CIDR. Terminate the bastion host.
- **D.** Update the security group of the bastion host to allow traffic from only the public IP addresses of the branch offices.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** eliminate brute-force SSH, log commands per session, keep port forwarding

🪤 **Your trap:** Picked Client VPN; SSH stays open behind the VPN and session commands are not logged.

🧠 **Rule:** No open SSH + session logs + port forwarding = Systems Manager Session Manager (close port 22, log to S3/CloudWatch).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Admin (nhiều branch) ──SSH:22 từ 0.0.0.0/0──► Bastion (peered VPC) ──SSH:22──► App instances
                                                  ▲
                                          hàng nghìn brute-force

Yêu cầu: (1) hết brute-force SSH  (2) log lệnh trong phiên  (3) vẫn forward port
```

Đáp án đúng: **A (Systems Manager Session Manager, bỏ bastion)**. Anh chọn C (Client VPN).

#### Yêu cầu quyết định bị bỏ sót

Anh đáp ứng được yêu cầu 1 (bỏ bastion, SSH không public), nhưng bỏ sót yêu cầu **"retain a log of commands run during an SSH session"**. Client VPN chỉ là đường hầm mã hóa: sau khi vào VPC, admin vẫn SSH bình thường và **không có bản ghi lệnh** nào do AWS lưu. Khi một lựa chọn "chạy được" thì phải đối chiếu từng gạch đầu dòng, thiếu một cái là loại.

#### Đáp án đúng: A

Session Manager:

- Không cần mở inbound port 22, không cần SSH key, không cần bastion/jump box, nên **hết brute-force**.
- **Ghi log phiên** (audit) ra S3 hoặc CloudWatch Logs, đáp ứng yêu cầu log lệnh.
- Hỗ trợ **port forwarding**.
- Instance chỉ cần SSM Agent + IAM instance profile và đường tới endpoint Systems Manager.

#### Các đáp án còn lại

- **B sai:** Run Command chạy lệnh từ xa quy mô lớn, nhưng **không forward port** được và không phải phiên tương tác.
- **C sai (anh chọn):** Client VPN mã hóa kết nối, nhưng không giữ log lệnh trong phiên SSH. Còn thêm gánh nặng cấp certificate cho từng admin.
- **D sai:** giới hạn IP branch vẫn để cổng 22 mở ra Internet, brute-force từ IP hợp lệ vẫn có thể xảy ra; và vẫn chưa có log lệnh.

| Giải pháp | Hết brute-force | Log lệnh | Port forwarding |
|---|---|---|---|
| **Session Manager (A)** | Có | Có | Có |
| Run Command (B) | Có | Có log lệnh chạy | Không |
| Client VPN (C) | Có | Không | Có |
| Giới hạn IP bastion (D) | Không | Không | Có |

#### Lưu ý thực tế

- Session logging không tự bật: phải cấu hình đích log (S3/CloudWatch Logs) trong Session Manager preferences.
- Instance trong private subnet cần VPC endpoint (ssm, ssmmessages, ec2messages) hoặc NAT để agent liên lạc.

#### Quy tắc nhớ cho thi

- **Thấy "đóng port 22 + log phiên + port forwarding"** → **Session Manager**
- **Thấy "bastion bị brute-force"** → thay bằng Session Manager, đừng chỉ siết security group
- **Thấy "VPN"** trong câu có yêu cầu **log lệnh** → VPN không cung cấp
- **Run Command** = chạy lệnh hàng loạt, không phải phiên/port forward

### TD explanation

A ✔. Session Manager helps you improve your security posture by giving you the ability to close inbound SSH ports. With Session Manager, you do not need to manage SSH keys and certificates, bastion hosts, or jump boxes. Session Manager offers the benefit of port forwarding. Session Manager also logs and audits session activity.
  For more information about Session Manager, see AWS Systems Manager Session Manager
  .

B. Run Command gives you the ability to automate common administrative tasks and to perform one-time configuration changes at scale. However, Run Command cannot forward ports.
  For more information about Run Command, see AWS Systems Manager Run Command
  .

C. A Client VPN connection can guarantee encryption. However, this connection would not be able to retain a log of commands that a user ran during an SSH session.
  For more information about Client VPN, see What Is AWS Client VPN?
  For more information about how to use Session Manager to log session activity, see Logging Session Activity
  .

D. http://
  Incorrect. An update to the security group of the bastion host would not eliminate brute-force SSH attempts because the public IP addresses of the branch offices are open. Additionally, you can configure Session Manager to log session activity. This solution does not address the requirement to log commands.
  For more information about how to use security groups to control traffic, see Control Traffic to Resources Using Security Groups
  .
  For more information about how use Session Manager to log session activity, see Logging Session Activity
  .

</details>

<a id="q58"></a>

## Q58

<!-- source: OFF1Q58 · Multiple Choice · 1 minutes 38 seconds -->



A company runs a grid computing application on eight Amazon EC2 instances. The instances are fully patched and updated. The application frequently fails because of network timeout errors. A solutions architect creates an AMI that is based on the existing EC2 instances. The solutions architect uses the AMI to add two additional EC2 instances. However, this change does not resolve the timeout errors.

Which solution will resolve the timeout errors with the LEAST operational effort?

- **A.** Use the existing AMI to create new EC2 instances in a cluster placement group. Terminate the old instances.
- **B.** Configure Elastic Network Adapters (ENAs) for all the instances.
- **C.** Configure Elastic Fabric Adapters (EFAs) for all the instances.
- **D.** Use the existing AMI to create new EC2 instances in an EC2 Fleet. Terminate the old instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** grid computing, timeouts between instances, adding instances did not help, LEAST effort

🪤 **Your trap:** Picked enabling ENA; current instances already use ENA. The issue is inter-node latency.

🧠 **Rule:** Low-latency node-to-node traffic = cluster placement group (relaunch from the AMI).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Grid computing: 8 EC2 (đã patch) ──network timeout thường xuyên──
Thêm 2 instance từ AMI → vẫn timeout (không phải vấn đề số lượng)
Yêu cầu: giải quyết timeout, LEAST operational effort
```

Đáp án đúng: **A (relaunch từ AMI trong cluster placement group)**. Anh chọn B (cấu hình ENA).

#### Yêu cầu quyết định bị bỏ sót

Hai manh mối: (1) thêm instance **không** giúp, nên không phải thiếu capacity; (2) grid computing = nhiều node nói chuyện với nhau, timeout là do **latency giữa các node**. Cộng thêm "LEAST operational effort" và đã có sẵn AMI, nghĩa là chọn cách đổi vị trí vật lý của instance, không phải đổi cấu hình network từng máy.

#### Đáp án đúng: A

**Cluster placement group** gom instance sát nhau trong một AZ, cho độ trễ thấp và băng thông cao giữa các node. Đã có AMI, chỉ cần launch bản sao vào placement group rồi terminate instance cũ. Ít việc nhất.

#### Vì sao B (anh chọn) không đúng

Anh nghĩ "network chậm thì bật enhanced networking". ENA thực tế đã có trên hầu hết instance type hiện đại, và theo AWS việc cấu hình ENA cho tất cả instance cần nhiều công sức. Quan trọng hơn: ENA tăng hiệu năng NIC nhưng không rút ngắn khoảng cách vật lý giữa các instance.

#### Các đáp án còn lại

- **C sai:** EFA tăng tốc HPC/ML, nhưng cần cấu hình thêm trên từng instance (và thường đi kèm cluster placement group), nên tốn nhiều effort hơn A.
- **D sai:** EC2 Fleet chỉ tạo nhiều instance trong một API call. Vấn đề không phải số lượng instance mà là latency.

| Giải pháp | Đánh vào latency node-to-node | Effort |
|---|---|---|
| **Cluster placement group (A)** | Có | Thấp (có AMI sẵn) |
| ENA (B) | Không rút ngắn khoảng cách | Cao |
| EFA (C) | Có (HPC) | Cao |
| EC2 Fleet (D) | Không | Trung bình |

#### Lưu ý thực tế

- Cluster placement group nằm trong **một AZ**, nên đánh đổi là khả năng chịu lỗi AZ thấp hơn.
- Nên launch cả nhóm cùng lúc và dùng cùng instance type để giảm lỗi thiếu capacity.

#### Quy tắc nhớ cho thi

- **Thấy "grid/HPC, latency giữa node, timeout"** → **cluster placement group**
- **Thấy "LEAST effort + đã có AMI"** → relaunch từ AMI, đừng cấu hình lại từng máy
- **Thêm instance không hết lỗi** → vấn đề không phải capacity
- **EFA** chỉ khi đề nhấn mạnh MPI/HPC/ML cần OS-bypass

### TD explanation

A ✔. A cluster placement group packs instances close together inside an Availability Zone. This solution will reduce the network latency between the EC2 instances. Reduction of network latency can resolve the timeout errors. Because an AMI already exists, the creation of a cluster placement group requires less operational effort than other network enhancements require.
  For more information about cluster placement groups, see Placement Groups. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html

B. ENAs provide enhanced networking capabilities to EC2 instances. However, ENA configuration would require significant operational effort.
  For more information about ENAs see, Enable Enhanced Networking with the Elastic Network Adapter (ENA) on Linux Instances. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html

C. An EFA is a network device that attaches to EC2 instances to accelerate high performance computing (HPC) and machine learning applications. However, EFA configuration would require significant operational effort.
  For more information about EFAs, see Elastic Fabric Adapter. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html

D. An EC2 Fleet creates multiple EC2 instances in a single API call. In this scenario, there does not appear to be an issue with the number of EC2 instances. The problem is more likely to be related to network latency. For this reason, the creation of an EC2 Fleet is not likely to address timeout errors.
  For more information about EC2 Fleets, see EC2 Fleet. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html

</details>

<a id="q70"></a>

## Q70

<!-- source: OFF1Q70 · Multiple Choice · 2 minutes 8 seconds -->



To be FIPS 140-2 Level 3 compliant, a company needs to store encryption keys. The keys need to be available between the hours of 8:00 AM and 6:00 PM US Eastern Time, Monday through Friday. The keys must not be available outside of these hours. The company needs a highly available solution to store the encryption keys.

Which solution will meet these requirements MOST cost-effectively?

- **A.** Create an AWS CloudHSM cluster with instances in multiple Availability Zones. Create an Amazon DynamoDB table. Store the CloudHSM metadata in the DynamoDB table. Create and schedule AWS Lambda functions to delete and recreate the CloudHSM cluster from a cluster backup. Configure the Lambda functions to retrieve the necessary metadata from the DynamoDB table.
- **B.** Store the encryption keys in AWS KMS. Create and schedule AWS Lambda functions to remove and add key access policies as necessary.
- **C.** Store the encryption keys in AWS KMS. Create and schedule AWS Lambda functions to disable and enable the stored encryption keys as necessary.
- **D.** Create an AWS CloudHSM cluster with instances in multiple Availability Zones. Store the CloudHSM metadata as standard parameters in AWS Systems Manager Parameter Store. Create and schedule AWS Lambda functions to delete and recreate the CloudHSM cluster from a cluster backup. Configure the Lambda functions to retrieve the necessary metadata from Parameter Store.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** FIPS 140-2 Level 3, keys available only business hours, highly available, MOST cost-effective

🪤 **Your trap:** Picked KMS with scheduled disable/enable; the exam treats KMS as Level 2. (Real AWS: KMS HSMs gained Level 3 validation in 2023.)

🧠 **Rule:** Exam rule: FIPS 140-2 Level 3 / dedicated HSM = CloudHSM (multi-AZ cluster). Cost trick: delete/restore the cluster from backup outside hours.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Yêu cầu: lưu encryption keys, FIPS 140-2 Level 3
         keys chỉ khả dụng 8:00-18:00 ET, Thứ 2-Thứ 6
         highly available, MOST cost-effective

Ngoài giờ: xóa CloudHSM cluster  ─┐
Đầu giờ  : restore từ backup    ─┘ metadata lưu ở Parameter Store (free)
```

Đáp án đúng: **D (CloudHSM multi-AZ + Parameter Store + Lambda xóa/tạo lại cluster)**. Anh chọn C (KMS + Lambda disable/enable key).

#### Yêu cầu quyết định bị bỏ sót

Yêu cầu loại đáp án là cụm **"FIPS 140-2 Level 3"**. Theo đề thi, AWS KMS là **Level 2**, còn **CloudHSM** (dedicated HSM) là **Level 3**. C và B đều dùng KMS nên bị loại ngay, dù cơ chế disable/enable theo lịch nghe hợp lý.

#### Đáp án đúng: D

- **CloudHSM cluster nhiều AZ** đáp ứng Level 3 và high availability.
- Ngoài giờ làm việc, Lambda theo lịch **xóa cluster** (HSM tính tiền theo giờ, xóa là hết tính), khóa cũng không còn khả dụng. Đầu giờ, Lambda **restore cluster từ backup**.
- Cần nhớ metadata để tạo lại cluster: lưu ở **Parameter Store standard parameters**, miễn phí.

#### Vì sao A kém hơn D

A có cùng ý tưởng với D nhưng lưu metadata trong **DynamoDB**, phát sinh chi phí lưu trữ không cần thiết. Đề hỏi MOST cost-effective nên D thắng.

#### Vì sao B, C sai

Cả hai dùng KMS (Level 2 theo đề). Disable/enable key hay sửa key policy chỉ là kiểm soát truy cập, không đổi mức chứng nhận.

| Giải pháp | FIPS 140-2 Level 3 | Chi phí |
|---|---|---|
| A. CloudHSM + DynamoDB | Có | Cao hơn (DynamoDB) |
| **D. CloudHSM + Parameter Store** | Có | Thấp nhất |
| B/C. KMS + Lambda | Không (Level 2 theo đề) | Không áp dụng |

📝 Ghi chú kỹ thuật: thực tế AWS KMS HSMs đã nhận chứng nhận **FIPS 140-2 Level 3** vào năm 2023, nên khẳng định "KMS = Level 2" trong đề đã lỗi thời. Với bài thi, vẫn giữ quy tắc: FIPS 140-2 Level 3 / dedicated HSM → **CloudHSM**.

#### Lưu ý thực tế

- Restore cluster từ backup cần Lambda tạo lại HSM trong các AZ và có thể mất thời gian, vì vậy lịch chạy nên đặt sớm hơn 8:00 AM.
- Cluster cũng có thể bị xóa kèm các HSM; backup được giữ nên dữ liệu khóa không mất.

#### Quy tắc nhớ cho thi

- **Thấy "FIPS 140-2 Level 3" / dedicated HSM** → **CloudHSM**
- **Thấy "chỉ khả dụng theo giờ + MOST cost-effective"** → xóa cluster ngoài giờ, restore từ backup
- **Lưu metadata** → **Parameter Store standard** (free), không phải DynamoDB
- **KMS** trong câu có yêu cầu Level 3 → loại theo logic đề

### TD explanation

A. CloudHSM provides dedicated hardware security modules in the AWS Cloud that are FIPS 140-2 Level 3 compliant. DynamoDB is a fully managed NoSQL database service. It is cost-effective to delete the CloudHSM cluster when the cluster is not needed. However, data storage in DynamoDB would incur unnecessary costs.
  For more information about CloudHSM, see What Is AWS CloudHSM? https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html
  For more information about DynamoDB, see What Is Amazon DynamoDB? https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

B. AWS KMS is a managed service that gives you the ability to create and control the cryptographic keys that are used to protect data. However, AWS KMS is FIPS 140-2 Level 2 compliant. The company needs to be FIPS 140-2 Level 3 compliant.
  For more information about AWS KMS, see AWS Key Management Service. https://docs.aws.amazon.com/kms/latest/developerguide/overview.html

C. AWS KMS is a managed service that gives you the ability to create and control the cryptographic keys that are used to protect data. However, AWS KMS is FIPS 140-2 Level 2 compliant. The company needs to be FIPS 140-2 Level 3 compliant.
  For more information about AWS KMS, see AWS Key Management Service. https://docs.aws.amazon.com/kms/latest/developerguide/overview.html

D ✔. CloudHSM provides dedicated hardware security modules in the AWS Cloud that are FIPS 140-2 Level 3 compliant. Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. Storage of standard parameters in Parameter Store is free. A solution that deletes the CloudHSM cluster when the cluster is not needed and that stores secrets in Parameter Store is the most cost-effective option.
  For more information about how to reduce the cost of CloudHSM by limiting operating hours, see How to Lower Costs by Automatically Deleting and Recreating HSMs. https://aws.amazon.com/blogs/security/how-to-lower-costs-by-automatically-deleting-and-recreating-hsms
  For more information about CloudHSM, see What Is AWS CloudHSM? https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html
  For more information about Parameter Store, see AWS Systems Manager Parameter Store. https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html

</details>

<a id="q73"></a>

## Q73

<!-- source: OFF1Q73 · Multiple Choice · 2 minutes 18 seconds -->



A company needs to create a web application on AWS to manage registrations for a conference. A database will store the registration information. Additionally, the web application will use several static files. The company's PHP web developer is familiar with the use of LAMP stack applications but does not have much AWS expertise. The company does not expect large changes in traffic on the web application and wants predictable pricing to facilitate budgeting for the conference.

Which solution will meet these requirements with the LEAST time required to learn new technologies?

- **A.** Create and package the web application as a Docker container. Deploy the container by using AWS Fargate. Configure Amazon DynamoDB for the database. Configure Amazon S3 for the static files.
- **B.** Create and package the web application as a .zip file. Deploy the web application by using AWS Elastic Beanstalk. Configure Amazon DynamoDB for the database. Configure Amazon S3 for the static files.
- **C.** Create the web application by using AWS Lambda functions. Deploy the web application by using Amazon API Gateway. Configure Amazon RDS for the database. Configure Amazon S3 for the static files.
- **D.** Create and package the web application by using Amazon Lightsail. Create a Lightsail instance by using an appropriate preconfigured template. Use Lightsail object storage to store the static files.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** PHP LAMP developer, little AWS expertise, stable traffic, predictable pricing, least time to learn

🪤 **Your trap:** Picked Elastic Beanstalk + DynamoDB; pay-per-resource pricing and a new NoSQL database both break the asks.

🧠 **Rule:** Simple LAMP app + fixed monthly price + minimal AWS learning = Amazon Lightsail.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Dev PHP/LAMP, ít kinh nghiệm AWS
Web app đăng ký hội nghị + DB + static files
Traffic ổn định, cần GIÁ DỰ ĐOÁN ĐƯỢC
Yêu cầu: LEAST time to learn new technologies
```

Đáp án đúng: **D (Amazon Lightsail, template LAMP + Lightsail object storage)**. Anh chọn B (Elastic Beanstalk + DynamoDB).

#### Yêu cầu quyết định bị bỏ sót

Hai yêu cầu mà B không đạt:

1. **Predictable pricing**: Beanstalk tính tiền theo tài nguyên thực dùng (EC2, ELB, v.v.), không có gói cố định hàng tháng.
2. **Least time to learn**: dev quen LAMP (MySQL), nhưng B dùng **DynamoDB** (NoSQL), cần học mô hình dữ liệu mới.

Beanstalk tự nó khá dễ, nhưng phần DynamoDB và mô hình giá làm B hỏng hai điều đề nhấn mạnh.

#### Đáp án đúng: D

Lightsail cung cấp compute, storage và networking đơn giản, có sẵn blueprint **LAMP** để chạy gần như y nguyên app PHP hiện có (DB MySQL ngay trên instance hoặc managed). Giá theo **gói tháng cố định**, hợp với việc lập ngân sách cho sự kiện. Static file dùng Lightsail object storage.

#### Các đáp án còn lại

- **A sai:** Fargate cần đóng gói Docker và hiểu container, cộng DynamoDB, nên phải học nhiều thứ mới.
- **B sai (anh chọn):** giá không cố định; DynamoDB đòi chuyển tư duy từ SQL sang NoSQL.
- **C sai:** Lambda + API Gateway cần kiến thức AWS đáng kể để dựng API; viết lại app LAMP thành serverless là rất tốn công.

| Giải pháp | Giá cố định | Giữ được mô hình LAMP/SQL | Độ học thêm |
|---|---|---|---|
| **Lightsail (D)** | Có | Có | Thấp nhất |
| Beanstalk + DynamoDB (B) | Không | Không | Trung bình-cao |
| Fargate + DynamoDB (A) | Không | Không | Cao |
| Lambda + API GW (C) | Không | Một phần | Cao |

#### Lưu ý thực tế

- Lightsail phù hợp app nhỏ, traffic ổn định; nếu sau này cần scale lớn thì phải chuyển sang các dịch vụ AWS đầy đủ.
- Giá cố định chỉ có ở gói Lightsail; data transfer vượt gói có thể phát sinh thêm.

#### Quy tắc nhớ cho thi

- **Thấy "LAMP, ít kinh nghiệm AWS, giá dự đoán được"** → **Amazon Lightsail**
- **Thấy "least time to learn"** → tránh dịch vụ mới (DynamoDB, container, serverless)
- **Predictable monthly price** → Lightsail, loại các dịch vụ pay-per-use
- Câu hỏi "đúng kỹ thuật" nhưng sai ràng buộc người dùng → vẫn sai

### TD explanation

A. You can use Fargate to run containers without the need to manage servers or clusters of Amazon EC2 instances. However, you would need to develop some expertise to build and create Docker containers. Use of DynamoDB would also require additional time to learn.
  For more information about Fargate, see What is AWS Fargate? https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
  For more information about DynamoDB, see From SQL to NoSQL. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html

B. You can use Elastic Beanstalk to quickly deploy and manage applications in the AWS Cloud without the need to learn about the underlying infrastructure. However, the price model is based on the resources that the application consumes. This solution would not meet the requirement for predictable pricing. Use of DynamoDB would also require additional time to learn.
  For more information about Elastic Beanstalk, see What is AWS Elastic Beanstalk? https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
  For more information about DynamoDB, see From SQL to NoSQL. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html

C. API Gateway is an AWS service you can use to create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale. API developers can create APIs that access AWS services, other web services, and data that is stored in the AWS Cloud. However, you would need to have significant AWS expertise to build the required APIs.
  For more information about API Gateway, see What is Amazon API Gateway? https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome
  For more information about the configuration of Lambda functions, see Configuring AWS Lambda Functions. https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html

D ✔. Lightsail provides developers with compute, storage, and network capacity tools. Lightsail also provides the ability to deploy and manage websites and web applications in the cloud. Lightsail offers affordable and predictable monthly payment plans.
  For more information about Lightsail, see Amazon Lightsail Documentation. https://docs.aws.amazon.com/lightsail
  For more information about Lightsail object storage, see Object Storage in Amazon Lightsail. https://lightsail.aws.amazon.com/ls/docs/en\_us/articles/buckets-in-amazon-lightsail
  For more information about deployment of LAMP (PHP) applications with Lightsail, see Tutorial: Launch and Configure a LAMP Instance in Amazon Lightsail. https://lightsail.aws.amazon.com/ls/docs/en\_us/articles/amazon-lightsail-tutorial-launching-and-configuring-lamp

</details>

---

# Group C — Organizations governance tooling: conformance packs, security account layout, Access Analyzer (3)

<a id="q26"></a>

## Q26

<!-- source: OFF1Q26 · Multi-Select · 3 minutes 6 seconds -->



A company manages multiple AWS accounts by using AWS Organizations. The company uses AWS Config to continuously audit and evaluate its AWS resources. The company needs to deploy a set of AWS Config rules across almost all accounts, including the management account, while excluding a few accounts. An AWS CloudFormation template already defines the required AWS Config rules. The company wants to ensure consistent application of the rules and wants to prevent any unauthorized modifications.

Which combination of steps will meet these requirements?

- **A.** Use AWS CloudFormation StackSets to deploy stacks across all applicable accounts. Perform drift detection frequently to ensure consistency.
- **B.** Activate trusted access in Organizations for the relevant service. Register a delegated administrator account to implement the relevant solution.
- **C.** Deactivate trusted access in Organizations for the relevant service. Activate each individual account administrator to implement the relevant solution.
- **D.** Use a CloudFormation template and AWS Service Catalog to launch a product across all applicable accounts. Use CloudFormation to perform drift detection frequently to ensure consistency.
- **E.** Use AWS Config to deploy an organization conformance pack that uses a CloudFormation template across all the accounts. Include a list of accounts to exclude.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** A, B

🔑 **Key words:** deploy AWS Config rules to almost all accounts incl. management, exclude a few, prevent unauthorized modification, Select TWO

🪤 **Your trap:** Picked StackSets + drift detection; drift detection only detects changes, it does not prevent them.

🧠 **Rule:** Org-wide Config rules that member accounts cannot change = organization conformance pack (with excluded accounts) via a delegated admin with trusted access.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Organization (nhiều account, gồm management account)
   │
   │  deploy bộ AWS Config rules (đã có CloudFormation template)
   ▼
 ~tất cả account, TRỪ vài account loại trừ
 Yêu cầu: áp dụng nhất quán + NGĂN sửa trái phép
```

Multi-select chọn 2. Đáp án đúng: **B + E**. Anh chọn A + B (đúng B, sai ở chỗ chọn A thay vì E).

#### Công cụ quản trị đúng cho tình huống

Đề yêu cầu **Config rules cho toàn org**, **gồm management account**, **loại trừ một số account**, **chống sửa trái phép**. Công cụ gốc cho việc này là **AWS Config organization conformance pack**, không phải StackSets.

- **E:** Config triển khai conformance pack từ CloudFormation template đến mọi account trong org, có **danh sách account loại trừ** và bao gồm management account. **Chỉ delegated administrator mới sửa được rule** đã deploy, nên member account không thể thay đổi. Đó là lớp "ngăn" mà đề muốn.
- **B:** bật **trusted access** cho Config trong Organizations và đăng ký **delegated administrator** để quản lý conformance pack tập trung.

Hai bước này ghép thành một giải pháp: trusted access + delegated admin (B) là điều kiện, organization conformance pack (E) là phần triển khai.

#### Vì sao A (anh chọn) không đạt

StackSets triển khai được stack đa account, nhưng **drift detection chỉ phát hiện thay đổi, không ngăn** thay đổi. Rule trong member account vẫn có thể bị sửa rồi mới bị báo. Đề nói "prevent", nên phát hiện sau không đủ.

#### Các đáp án còn lại

- **C sai:** tắt trusted access thì các dịch vụ không thể thực hiện tác vụ đa account; admin từng account làm riêng sẽ không nhất quán và không chống sửa.
- **D sai:** Service Catalog giúp tuân thủ chính sách, nhưng cũng dùng drift detection, không ngăn sửa trái phép.

| Cách | Triển khai org-wide | Loại trừ account | Ngăn sửa trái phép |
|---|---|---|---|
| **Org conformance pack (E)** | Có | Có | Có (chỉ delegated admin sửa) |
| StackSets + drift (A) | Có | Có | Không (chỉ phát hiện) |
| Service Catalog + drift (D) | Một phần | Khó | Không |

#### Lưu ý thực tế

- Conformance pack và trusted access đều cần thiết lập ở management account; delegated administrator giảm việc dùng management account hằng ngày.
- Drift detection vẫn hữu ích để giám sát, chỉ là không thay thế cơ chế ngăn.

#### Quy tắc nhớ cho thi

- **Thấy "Config rules toàn org, ngăn sửa"** → **organization conformance pack** + delegated admin
- **Thấy "prevent unauthorized modification"** → drift detection là sai (chỉ detect)
- **Thấy "trusted access"** cho dịch vụ đa account → bật, không tắt
- **Exclude accounts** → có sẵn trong conformance pack org

### TD explanation

A. CloudFormation StackSets gives you the ability to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation. Drift detection does not prevent unauthorized modifications.
  For more information about CloudFormation StackSets drift detection, see Detecting Unmanaged Configuration Changes in Stack Sets. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html
  For more information about how to create a stack set, see Create a Stack Set with Service-Managed Permissions. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html#stacksets-orgs-associate-stackset-with-org

B ✔. Organizations is an account-management service in which trusted access allows supported AWS services such as AWS Config to perform tasks across accounts in the organization. AWS Config also supports a delegated administrator that can implement conformance packs across multiple accounts and achieve consistent compliance without any unauthorized modifications.
  For more information about trusted access in Organizations, see AWS Services That You Can Use with AWS Organizations. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_integrate\_services\_list.html

C. Organizations is an account-management service in which trusted access allows supported AWS services such as AWS Config and CloudFormation to perform tasks across accounts in the organization. Performance of these tasks requires trusted access. Individual account administrators are not able to perform these tasks.
  For more information about trusted access in AWS Organizations, see AWS Services That You Can Use with AWS Organizations. https://docs.aws.amazon.com/organizations/latest/userguide/orgs\_integrate\_services\_list.html

D. AWS Service Catalog creates and manages catalogs of IT services and solutions. This service helps achieve compliance with organizational business policies. Drift detection does not prevent unauthorized modifications.
  For more information about CloudFormation drift detection, see Detecting Unmanaged Configuration Changes to Stacks and Resources. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html

E ✔. AWS Config gives you the ability to continuously asses, audit, and evaluate the configurations of your AWS resources. AWS Config can deploy rules in a conformance pack across all AWS accounts within an organization. AWS Config can include the management account of Organizations and exclude other accounts by using the exclusion list. Only the delegated administrator account can modify the rules deployed by AWS Config. This limit ensures consistent compliance and prevents unauthorized modifications.
  For more information about application of AWS Config rules across accounts in an organization, see Enabling AWS Config Rules Across All Accounts in Your Organization. https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html
  For more information about management of conformance packs within an organization, see Managing Conformance Packs Across All Accounts in Your Organization. https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-organization-apis.html

</details>

<a id="q57"></a>

## Q57

<!-- source: OFF1Q57 · Multi-Select · 3 minutes 27 seconds -->



A company plans to migrate 500 workloads to the AWS Cloud. The company creates separate accounts for different workloads by using AWS Organizations. The company has teams that focus solely on security and infrastructure. Most workloads fall into well-defined environments such as production, development, or testing. There are a few unique workloads that require specific security policies. The company is not sure how to organize the workloads and teams. A solutions architect needs to design an account structure.

Which combination of steps should the solutions architect take to set up the correct account structure?

- **A.** Create OUs for each environment. Add workload accounts to the appropriate environment OUs. Apply appropriate SCPs at the OU level.
- **B.** Set up a centralized security account for logging, tooling, and audit-related activities.
- **C.** Set up separate security accounts for logging, tooling, and audit-related activities.
- **D.** Create accounts for unique workloads in a separate OU that is named "Exceptions." Apply appropriate SCPs at the account level.
- **E.** Create accounts for unique workloads in the same OUs as the regular workloads. Apply appropriate SCPs at the account level.
- **F.** Create one OU for each workload. Add each workload account into each workload OU. Apply appropriate SCPs at the OU level.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, D · **You picked:** A, B, D

🔑 **Key words:** 500 workloads, separate accounts, security and infra teams, unique workloads, account structure, Select THREE

🪤 **Your trap:** Picked one centralized security account for logging, tooling and audit; best practice separates them to limit blast radius.

🧠 **Rule:** Account layout = OUs per environment + SCPs at OU; separate Log Archive, Security Tooling, Audit accounts; Exceptions OU for unique workloads.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Organization root
 ├── OU Prod ─ OU Dev ─ OU Test      (workload accounts)
 ├── OU Exceptions                    (workload đặc thù)
 └── OU Security
        ├── Log Archive account
        ├── Security Tooling account
        └── Audit account
```

Multi-select chọn 3. Đáp án đúng: **A + C + D**. Anh chọn A + B + D (đúng 2/3, sai ở B thay vì C).

#### Công cụ quản trị đúng cho tình huống

Thiết kế account structure theo hướng dẫn **AWS SRA / Organizing Your AWS Environment**:

- **A đúng:** tạo OU theo môi trường (production/dev/test), gán SCP ở cấp OU để áp một lần cho nhiều account cùng vai trò.
- **D đúng:** workload đặc thù vào một **Exceptions OU** riêng, SCP riêng ở cấp account. Không làm rối chính sách của OU chuẩn.
- **C đúng:** tách **các account bảo mật riêng**: Log Archive, Security Tooling, Audit (và có thể cả read-only/break-glass).

#### Vì sao C thắng B (chỗ anh sai)

B gộp logging, tooling và audit vào **một** security account. Điều này mất đi:

- **Workload isolation** và **giảm blast radius**: một account bị lộ thì cả log lẫn công cụ và audit bị ảnh hưởng.
- **Phân quyền đơn giản**: mỗi account có nhóm người truy cập khác nhau (người audit chỉ đọc, đội tooling có quyền chạy công cụ, log archive gần như bất biến).

Tách ra thì log không thể bị xóa bởi người đang vận hành công cụ bảo mật.

#### Các đáp án còn lại

- **E sai:** đặt workload đặc thù cùng OU với workload thường nên phải gán SCP trực tiếp từng account, quản lý chính sách rối.
- **F sai:** một OU cho mỗi workload (500 OU) bắt buộc gán SCP chung (prod/test) ở cấp account, không tận dụng được kế thừa.

| Lựa chọn | Kết quả |
|---|---|
| **A** OU theo môi trường | Đúng, SCP kế thừa |
| **C** account bảo mật tách riêng | Đúng, blast radius nhỏ |
| **D** Exceptions OU | Đúng, cô lập ngoại lệ |
| B account bảo mật gộp | Sai, mất cô lập |
| E ngoại lệ chung OU | Sai, SCP ở từng account |
| F OU theo từng workload | Sai, không kế thừa chính sách |

#### Lưu ý thực tế

- SCP không áp dụng cho management account, nên đừng đặt workload ở đó.
- Security OU thường là OU nền tảng đầu tiên, và log archive nên có bảo vệ chống xóa (ví dụ S3 Object Lock) kết hợp SCP.

#### Quy tắc nhớ cho thi

- **Thấy "OU" + môi trường** → OU theo prod/dev/test, **SCP ở OU**
- **Thấy "workload đặc thù"** → **Exceptions OU**
- **Thấy "logging, tooling, audit"** → **các account riêng** (Log Archive, Security Tooling, Audit), không gộp
- **Một OU cho mỗi workload** → luôn sai (không mở rộng được)

### TD explanation

A ✔. Organizations provides centralized account management in a hierarchical fashion through OUs and policies. A solution that creates OUs based on functional roles would give you the ability to apply common SCPs across the accounts with the same functional role.
  For more information about the design of AWS accounts within Organizations, see Design Principles for Organizing Your AWS Accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-organizing-your-aws-accounts.html

B. Organizations provides centralized account management in a hierarchical fashion through OUs and policies. You cannot achieve workload isolation, minimal blast radius, and simpler access management by creating a single account for all logging, tooling, and audit activities.
  For more information about security account structure, see Security OU and accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/security-ou-and-accounts.html

C ✔. Organizations provides centralized account management in a hierarchical fashion through OUs and policies. You should create separate security accounts for logging, security tooling, read-only access, and emergency access (break-glass access), especially for advanced organizations.
  For more information about security account structure, see Security OU and accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/security-ou-and-accounts.html

D ✔. Organizations provides centralized account management in a hierarchical fashion through OUs and policies. The creation of a separate OU for any exception accounts would reduce the effort necessary for you to apply SCPs to the relevant accounts as needed.
  For more information about accounts that have unique requirements, see Exceptions OU. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/exceptions-ou.html

E. Organizations provides centralized account management in a hierarchical fashion through OUs and policies. A solution that creates accounts for unique exception workloads in the same OU as the regular workloads would require you to apply common and unique SCPs directly to the accounts. This solution would complicate policy management.
  For more information about the design of AWS accounts within AWS Organizations, see Design Principles for Organizing Your AWS Accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-organizing-your-aws-accounts.html

F. Organizations provides centralized account management in a hierarchical fashion through OUs and policies. A solution that creates OUs based on workloads would require you to apply common production and testing SCPs at the account level. This solution would complicate policy management.
  For more information about the design of AWS accounts within Organizations, see Design Principles for Organizing Your AWS Accounts. https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-organizing-your-aws-accounts.html

</details>

<a id="q62"></a>

## Q62

<!-- source: OFF1Q62 · Multiple Choice · 3 minutes 11 seconds -->



A company uses AWS Organizations to manage multiple AWS accounts. The accounts share an Amazon SQS queue. The SQS queue is also shared with other AWS accounts outside the organization. All internal and external accounts have access to send and receive messages according to a permissions policy that is attached to the SQS queue. The company wants to identify any external principals that have access to the SQS queue.

How should a solutions architect meet this requirement?

- **A.** Set up an AWS CloudTrail trail that logs management events. Use CloudTrail logs to track Amazon SQS API activities by any external principals.
- **B.** Use AWS Identity and Access Management Access Analyzer to create an analyzer with the current account as a zone of trust. Filter by external findings on the SQS queue.
- **C.** Set up an AWS CloudTrail trail that logs data events. Use CloudTrail logs to track Amazon SQS API activities by any external principals.
- **D.** Use AWS Identity and Access Management Access Analyzer to create an analyzer with the current organization as a zone of trust. Filter by external findings on the SQS queue.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** SQS queue shared across org accounts, identify external principals with access

🪤 **Your trap:** Picked CloudTrail data events; logs only show who called the API, not who is allowed by the policy.

🧠 **Rule:** Who outside the org CAN access a resource = IAM Access Analyzer with the organization as zone of trust (external access findings).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
SQS queue (resource-based policy)
   ├── account trong Organization   (internal)
   └── account NGOÀI Organization   (external)

Yêu cầu: tìm ra các principal BÊN NGOÀI có quyền truy cập queue
```

Đáp án đúng: **D (IAM Access Analyzer, zone of trust = organization)**. Anh chọn C (CloudTrail data events).

#### Công cụ quản trị đúng cho tình huống

Câu hỏi là **"ai CÓ THỂ truy cập"** (dựa trên permission policy), không phải "ai ĐÃ gọi API". Công cụ phân tích policy để tìm quyền truy cập từ bên ngoài là **IAM Access Analyzer**.

- Access Analyzer xét resource policy và tạo **finding** cho resource chia sẻ ra ngoài **zone of trust**.
- Với **zone of trust = organization**: account trong org được coi là đáng tin, nên finding chỉ gồm **principal ngoài organization**. Đây đúng là thứ đề cần. Lọc theo resource type SQS queue và external findings.

#### Vì sao C (anh chọn) không đạt

CloudTrail ghi lại **hoạt động thực tế** (SendMessage, ReceiveMessage). Principal ngoài có quyền nhưng chưa từng gọi sẽ không xuất hiện, nên không biết được "ai có quyền". Ngoài ra AWS chỉ ra lựa chọn C không cho ra đúng dữ liệu cần cho yêu cầu này.

#### Các đáp án còn lại

- **A sai:** trail chỉ ghi management events, không bao gồm các data events của SQS như SendMessage/ReceiveMessage.
- **B sai:** analyzer với **account hiện tại** làm zone of trust sẽ coi cả account khác trong org là "external", gây finding thừa, không tách được đúng nhóm bên ngoài organization.

| Cách | Trả lời "ai có quyền" | Tách ngoài org đúng |
|---|---|---|
| **Access Analyzer, zone = organization (D)** | Có | Có |
| Access Analyzer, zone = account (B) | Có | Không (lẫn account nội bộ) |
| CloudTrail data events (C) | Không (chỉ hoạt động đã xảy ra) | Không |
| CloudTrail management events (A) | Không | Không |

#### Lưu ý thực tế

- Analyzer với zone of trust là organization phải tạo ở management account hoặc delegated administrator.
- Access Analyzer là phân tích tĩnh policy, nên bổ sung chứ không thay CloudTrail khi cần điều tra hành vi thực tế.

#### Quy tắc nhớ cho thi

- **Thấy "ai bên ngoài có thể truy cập resource"** → **IAM Access Analyzer**
- **Zone of trust = organization** → chỉ báo principal ngoài org; **= account** → lẫn account nội bộ
- **CloudTrail** = "ai ĐÃ làm gì", không phải "ai CÓ QUYỀN"
- **SQS/S3/KMS/IAM role chia sẻ ra ngoài** → external access finding

### TD explanation

A. CloudTrail records account activity and service events from most AWS services. A trail that logs management events does not capture data events such as SendMessage and ReceiveMessage activities.
  For more information about CloudTrail management events, see CloudTrail Concepts. https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

B. IAM Access Analyzer helps identify the resources that are shared with an external entity. An analyzer with a specific account as the zone of trust will generate findings for other internal accounts along with external accounts. This solution does not meet the company's requirements.
  For more information about IAM Access Analyzer, see Using AWS IAM Access Analyzer. https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html

C. CloudTrail records account activity and service events from most AWS services. A trail that logs data events does not capture data events from Amazon SQS such as SendMessage and ReceiveMessage activities.
  For more information about CloudTrail data events, see CloudTrail Concepts.
  https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-data-events

D ✔. IAM Access Analyzer helps identify the resources that are shared with an external entity. An analyzer with the organization as the zone of trust will generate findings only for external accounts. It will not include the findings of the internal accounts within the organization.
  For more information about IAM Access Analyzer, see Using AWS IAM Access Analyzer. https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
  For more information about IAM Access Analyzer resource types, see Access Analyzer Resource Types. https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html
  For more information about filtering IAM Access Analyzer findings, see Filtering Findings. https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-filter.html

</details>

---

# 📌 Câu đúng cần ôn thêm (3 câu)

Ba câu bạn trả lời đúng nhưng muốn hiểu kỹ hơn. Không tính vào bảng theo dõi làm lại.

<a id="q47"></a>

## Q47 · câu đúng — ôn thêm

<!-- source: OFF1Q47 · Multiple Choice · 2 minutes 18 seconds -->

A company has migrated most of its on-premises infrastructure to the AWS Cloud. The company is planning to complete the migration soon. After the migration, the company will retire its on-premises infrastructure. The company currently uses Active Directory to manage and authenticate its users. The company wants an AWS solution to manage users on AWS. The company has hundreds of users and needs only basic LDAP functionality. The company wants to implement multi-factor authentication (MFA) as part of the solution.

Which solution will meet these requirements with the LEAST operational effort?

- **A.** Configure an Active Directory Connector directory in AWS Directory Service. Connect the Active Directory Connector directory to the on-premises Active Directory.
- **B.** Configure a directory with AWS Managed Microsoft AD. Use the Active Directory Migration Toolkit to migrate the users from the on-premises Active Directory to AWS.
- **C.** Configure a Simple Active Directory directory in AWS Directory Service. Use the Comma Separated Value Directory Exchange (CSVDE) utility to migrate the users from the on-premises Active Directory to AWS.
- **D.** Configure an AWS IAM Identity Center identity store to manage the users in AWS. Provision users, groups, and entitlements in IAM Identity Center.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** B (right)

🔑 **Key words:** on-prem AD being retired, hundreds of users, basic LDAP, MFA, LEAST operational effort

👀 **Watch:** AD Connector needs the on-prem AD that is being retired; Simple AD has no MFA/RADIUS support; IAM Identity Center store is not LDAP and needs users recreated.

🧠 **Rule:** Retiring on-prem AD + LDAP + MFA = AWS Managed Microsoft AD (migrate with ADMT, MFA via RADIUS). AD Connector only while on-prem AD stays.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại                                  Sau khi migrate xong
┌──────────────────────┐                  ┌──────────────────────────┐
│ On-prem Active Dir.  │  ── migrate ──►  │ Directory trên AWS       │
│ (hàng trăm user)     │                  │ - basic LDAP             │
└──────────────────────┘                  │ - MFA                    │
   SẼ BỊ RETIRE (tắt hẳn)                 │ - ÍT công vận hành nhất  │
                                          └──────────────────────────┘
```

Từ khóa quyết định: **on-prem bị retire** + **basic LDAP** + **MFA** + **LEAST operational effort**. Đáp án đúng: **B (AWS Managed Microsoft AD + ADMT)**. Anh chọn đúng B.

#### Vì sao B thắng

- **AWS Managed Microsoft AD** chạy Active Directory thật (managed service), nên đáp ứng LDAP (dư sức cho "basic LDAP") và **hỗ trợ MFA** (qua RADIUS).
- **Active Directory Migration Toolkit (ADMT)** là công cụ chính thức để chuyển user từ on-prem AD sang Managed Microsoft AD, giữ nguyên user/group, không phải tạo lại bằng tay.
- AWS lo patch, HA, backup cho domain controller, nên công vận hành thấp.
- Không phụ thuộc on-prem: phù hợp với việc tắt hạ tầng on-prem.

📝 Ghi chú kỹ thuật: MFA trên Managed Microsoft AD hoạt động bằng cách tích hợp với hạ tầng **RADIUS** (RADIUS server của anh hoặc dịch vụ MFA), đề chỉ cần biết "có hỗ trợ MFA".

#### Vì sao các option còn lại sai

- **A. AD Connector:** chỉ là gateway/proxy chuyển request về on-prem AD, không cache gì trên cloud. On-prem bị retire thì Connector không còn gì để kết nối tới.
- **C. Simple AD + CSVDE:** Simple AD là directory chạy Samba 4, chỉ có tập con tính năng của Managed Microsoft AD và **không hỗ trợ MFA**, nên loại ngay vì MFA là yêu cầu bắt buộc.
- **D. IAM Identity Center identity store:** phải **tạo lại** user, group, assignment (entitlement) vì không migrate trực tiếp từ AD, tốn công hơn mức cần thiết, và đây là identity store cho SSO chứ không phải LDAP directory.

#### Bảng so sánh

| Option | Giải pháp | Hết phụ thuộc on-prem? | MFA | Công migrate / vận hành |
|---|---|---|---|---|
| A | AD Connector | Không, cần on-prem AD sống | Phụ thuộc AD đích | Dễ, nhưng vô nghĩa khi retire on-prem |
| **B** | **AWS Managed Microsoft AD + ADMT** | **Có** | **Có (RADIUS)** | **Thấp, công cụ migrate chính thức** |
| C | Simple AD + CSVDE | Có | Không | Loại vì thiếu MFA |
| D | IAM Identity Center store | Có | Có ở mức SSO, nhưng không phải LDAP | Cao: tạo lại user/group/entitlement |

#### Biến thể đề có thể gặp

- **On-prem AD vẫn tiếp tục dùng** (không retire, chỉ cho AWS dùng chung identity) → **AD Connector** (proxy, không cache, ít công nhất). Khi đó A trở thành đáp án.
- **Cần trust/đồng bộ hai chiều với on-prem AD, workload cần full AD feature** → **AWS Managed Microsoft AD** với trust, không dùng Connector.
- **Bỏ yêu cầu MFA, vài trăm user, chỉ cần LDAP cơ bản, chi phí thấp** → **Simple AD** mới hợp lý. Chỉ thêm chữ "MFA" là Simple AD bị loại.
- **Chỉ cần SSO vào AWS account/ứng dụng SaaS, không cần LDAP/Windows domain** → **IAM Identity Center** (có thể dùng built-in store).

#### Quy tắc nhớ cho thi

- **Thấy "on-prem AD sẽ bị retire/migrate hết"** → **AWS Managed Microsoft AD** (migrate bằng ADMT), không phải AD Connector.
- **Thấy "on-prem AD vẫn giữ, không muốn cache/ không muốn replicate"** → **AD Connector**.
- **Thấy "MFA" trong câu có Directory Service** → loại **Simple AD** (không hỗ trợ MFA).
- **Thấy "LDAP" + "directory"** → họ Directory Service; **IAM Identity Center** là SSO, không phải LDAP.
- **Mẹo nhớ:** Simple = đơn giản = thiếu MFA; Connector = ống dẫn = cần nguồn phía sau.

### TD explanation

A. Active Directory Connector is a directory gateway that can redirect directory requests to an on-premises Active Directory without the need to cache any information in the cloud. However, the company plans to retire its on-premises infrastructure.
  For more information about Active Directory Connector, see Active Directory Connector
  .

B ✔. AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, runs Active Directory as a managed service. The Active Directory Migration Toolkit can migrate users from an on-premises Active Directory to AWS Managed Microsoft AD. This solution also supports MFA.
  For more information about AWS Managed Microsoft AD, see AWS Managed Microsoft AD
  .
  For more information about user migration, see Migrating Active Directory users to AWS Managed Microsoft AD
  .

C. Simple Active Directory is a standalone managed directory that is powered by a Samba 4 Active Directory Compatible Server. Simple Active Directory provides a subset of the features that AWS Managed Microsoft AD offers. However, Simple Active Directory does not support MFA, which is one of the requirements.
  For more information about Simple Active Directory, see Simple Active Directory
  .

D. You configure an identity store when you configure IAM Identity Center. However, migration from Active Directory to the identity store used by IAM Identity Center would require recreation of the users, groups, and assignments (entitlements). This solution requires more operational effort than necessary.
  For more information about how to configure an identity store, see Manage Identities in IAM Identity Center
  .
  For more information about how to change identity stores from Active Directory to IAM Identity Center, see Considerations for Changing Your Identity Source
  .

</details>

<a id="q49"></a>

## Q49 · câu đúng — ôn thêm

<!-- source: OFF1Q49 · Multiple Choice · 3 minutes 4 seconds -->

A company deploys a new internal application on two Amazon EC2 instances behind an Application Load Balancer (ALB). The ALB and the EC2 instances operate across two Availability Zones. The company's employees depend on the application to perform their work.

When workloads are high, employees report slow response times and reliability issues with the application. Some incoming requests can generate significant compute activity on the EC2 instances. The workload can increase by 2 to 10 times the typical load in a matter of minutes. A solutions architect needs to change the configuration so that the application will scale in response to multiple workload changes in the least amount of time possible.

How should the solutions architect configure Amazon EC2 Auto Scaling to meet these requirements?

- **A.** Configure a simple scaling policy that scales EC2 instances based on the CPUUtilization metric.
- **B.** Configure a simple scaling policy that scales EC2 instances based on the RequestCountPerTarget metric from the ALB.
- **C.** Configure a step scaling policy that scales EC2 instances based on the CPUUtilization metric.
- **D.** Configure a step scaling policy that scales EC2 instances based on the RequestCountPerTarget metric from the ALB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** C (right)

🔑 **Key words:** requests generate different CPU load, scale on multiple workload changes, least time

👀 **Watch:** Simple scaling waits for the cooldown after each activity; request count does not reflect load because each request costs a different amount of CPU.

🧠 **Rule:** Fast reaction to repeated changes = step scaling (no cooldown wait, step adjustments by breach size). Pick the metric that tracks real load — here CPU, not request count.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
         ┌───────────────┐
Users ──►│     ALB       │   (2 AZ)
         └───┬───────┬───┘
             ▼       ▼
          EC2 #1   EC2 #2     ◄── Auto Scaling group
   Có request tốn rất nhiều CPU, có request nhẹ
   Tải tăng 2x – 10x chỉ trong vài phút, nhiều đợt liên tiếp
   Yêu cầu: scale kịp NHIỀU lần thay đổi, thời gian NGẮN NHẤT
```

Hai trục quyết định: (1) **loại policy** phản ứng nhanh, nhiều lần liên tiếp; (2) **metric** phản ánh tải thật. Đáp án đúng: **C (step scaling + CPUUtilization)**. Anh chọn đúng C.

#### Vì sao C thắng

- **Trục policy:** step scaling phản ứng theo mức vượt ngưỡng của alarm (vượt ít thì thêm ít, vượt nhiều thì thêm nhiều), và **vẫn phản ứng với thay đổi mới ngay cả khi một scale-out đang chạy**. Đúng với "nhiều đợt tăng tải liên tiếp".
- **Trục metric:** request có mức tốn CPU khác nhau, vài request có thể gây ra rất nhiều activity. Vậy **CPUUtilization** mới phản ánh tải thật trên instance.

```
Simple scaling:  alarm ─► scale ─► CHỜ hoàn tất + COOLDOWN ─► mới xử lý alarm kế
Step scaling:    alarm ─► scale theo bậc ─► alarm mới vẫn xử lý được ngay
```

#### Vì sao các option còn lại sai

- **A. Simple + CPU:** metric đúng nhưng policy sai. Simple scaling phải đợi scaling activity xong rồi đến **cooldown** mới đáp ứng được thay đổi tiếp theo, trong khi tải tăng 2-10x trong vài phút.
- **B. Simple + RequestCountPerTarget:** sai cả hai trục. Vừa bị cooldown, vừa dùng metric không phản ánh tải khi mỗi request tốn CPU khác nhau.
- **D. Step + RequestCountPerTarget:** policy đúng nhưng metric sai. Vài request nặng có thể làm CPU quá tải trong khi request count vẫn thấp, nên scale không kịp.

#### Bảng so sánh

| Option | Policy | Metric | Phản ứng nhiều đợt tăng tải | Metric phản ánh tải thật |
|---|---|---|---|---|
| A | Simple | CPUUtilization | Chậm (chờ activity + cooldown) | Có |
| B | Simple | RequestCountPerTarget | Chậm | Không |
| **C** | **Step** | **CPUUtilization** | **Nhanh, xử lý cả khi đang scale-out** | **Có** |
| D | Step | RequestCountPerTarget | Nhanh | Không |

#### Biến thể đề có thể gặp

- **Mỗi request tốn CPU gần như nhau** (request đồng đều) → **target tracking trên ALBRequestCountPerTarget** là lựa chọn tự nhiên, vì số request/target tỷ lệ với tải thật, và target tracking lo cả scale-out lẫn scale-in.
- **Đề nói "giữ CPU ở khoảng 50%, ít cấu hình nhất"** → **target tracking** trên CPU, không cần tự định nghĩa step.
- **Tải theo lịch cố định (9h sáng mỗi ngày)** → **scheduled scaling**.
- **Cần chuẩn bị trước theo mẫu lặp lại** → **predictive scaling**.
- **Đề không có chữ "multiple/least time" và chỉ một đợt tăng** → simple scaling cũng chấp nhận được, nhưng thường vẫn không phải đáp án tốt nhất.

#### Quy tắc nhớ cho thi

- **Thấy "nhiều thay đổi tải liên tiếp / phản ứng nhanh nhất"** → **step scaling** (loại simple vì cooldown).
- **Thấy "mỗi request tốn tải khác nhau"** → dùng **CPUUtilization**, đừng dùng RequestCountPerTarget.
- **Thấy "request đồng đều" hoặc "giữ metric ở mức mục tiêu"** → **target tracking**.
- **Mẹo nhớ:** Simple = một bậc, chờ cooldown; Step = nhiều bậc, không đợi.
- **Cách làm bài hai trục:** loại theo policy trước (A, B), rồi chọn metric (C hơn D).

### TD explanation

A. EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. CPU utilization is the correct policy basis because requests can generate different amounts of activity on the instances. However, an Auto Scaling group with a simple scaling policy must wait for scaling activity to finish running, followed by a cooldown period, before the Auto Scaling group can respond to additional workload changes. The requirement is that the solution must respond to multiple workload changes in the least amount of time possible. A step scaling policy would respond faster to workload changes.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

B. EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. However, an Auto Scaling group with a simple scaling policy must wait for scaling activity to finish running, followed by a cooldown period, before the Auto Scaling group can respond to additional alarms. The requirement is that the solution must respond to multiple workload changes in the least amount of time possible. A step scaling policy would respond faster to workload changes. Additionally, different requests can generate different levels of activity on the instances, so a few requests could generate a lot of activity. A policy that is based on the RequestCountPerTarget metric would not be as effective as a policy that is based on CPU utilization.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

C ✔. EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. An Auto Scaling group with a step scaling policy would quickly respond to multiple workload changes, even while another scale-out activity is in progress. CPU utilization is the correct policy basis because requests can generate different amounts of activity on the instances.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

D. EC2 Auto Scaling helps to ensure that the correct number of instances are available to handle the load for an application. An Auto Scaling group with a step scaling policy would quickly respond to multiple workload changes, even while another scale-out activity is in progress. However, different requests can generate different levels of activity on the instances, and a few requests could generate a lot of activity. A policy that is based on the RequestCountPerTarget metric would not be as effective as a policy that is based on CPU utilization.
  For more information about Auto Scaling groups, see What Is Amazon EC2 Auto Scaling? https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
  For more information about step and simple scaling policies, see Step and Simple Scaling Policies for Amazon EC2 Auto Scaling. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

</details>

<a id="q59"></a>

## Q59 · câu đúng — ôn thêm

<!-- source: OFF1Q59 · Multiple Choice · 2 minutes 28 seconds -->

A company has resources in on-premises networks and in multiple VPCs on AWS. The company needs a networking solution that will give the on-premises resources the ability to communicate with the VPC resources. The VPC resources also must be able to communicate with each other.

The company has configured a customer gateway device on premises and has attached virtual private gateways to each VPC. The company wants a scalable solution so that the company can easily add more VPCs in the future.

How should a solutions architect configure the network connectivity to meet these requirements with the LEAST operational overhead?

- **A.** Set up a connection through AWS Direct Connect. Create VIFs to provide access to the virtual private gateways. Configure VPC peering connections between all the VPCs.
- **B.** Create a transit VPC. Create VPN connections from the transit VPC to each virtual private gateway. Create AWS Site-to-Site VPN connections between the customer gateway device and the transit VPC.
- **C.** Create an individual AWS Site-to-Site VPN connection between the customer gateway device and each of the virtual private gateways. Configure VPC peering connections between all the VPCs.
- **D.** Create a transit gateway. Create an AWS Site-to-Site VPN attachment between the customer gateway device and the transit gateway. Attach the VPCs to the transit gateway. Remove the virtual private gateways.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** D (right)

🔑 **Key words:** on-prem + multiple VPCs with VGWs, VPCs talk to each other, easily add VPCs, LEAST overhead

👀 **Watch:** VPC peering is non-transitive and grows as a full mesh; transit VPC needs self-managed appliances; per-VGW VPNs multiply tunnels.

🧠 **Rule:** Hub-and-spoke for many VPCs + on-prem = Transit Gateway with one Site-to-Site VPN (or DX) attachment; attach each new VPC and drop the VGWs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem ── customer gateway
    │
    ?   (cần nối tới TẤT CẢ VPC, hiện mỗi VPC có một VGW)
    │
 ┌──┴───┬───────┬───────┐
VPC-A  VPC-B  VPC-C   ... thêm VPC mới trong tương lai
   ▲ các VPC cũng phải nói chuyện với nhau ▲
```

Từ khóa quyết định: **on-prem + nhiều VPC**, **VPC nói chuyện với nhau**, **dễ thêm VPC**, **LEAST operational overhead**. Đáp án đúng: **D (Transit Gateway + Site-to-Site VPN attachment, gỡ các VGW)**. Anh chọn đúng D.

#### Vì sao D thắng

- **Transit Gateway** là network transit hub: nối VPC với VPC và với on-prem qua một điểm trung tâm.
- Chỉ cần **một VPN attachment** từ customer gateway tới TGW; mỗi VPC mới chỉ cần **attach** vào TGW, không phải tạo thêm VPN hay peering.
- Không có EC2 để quản lý, nên overhead thấp nhất.
- Gỡ VGW vì không còn dùng; VPC attach vào TGW thay cho VGW.

```
On-prem ──(1 Site-to-Site VPN)──► Transit Gateway ◄── VPC-A
                                       ▲  ▲   ▲
                                       │  └── VPC-B
                                       └── VPC mới: chỉ thêm 1 attachment
```

#### Vì sao các option còn lại sai

- **A. Direct Connect + VIF tới VGW + VPC peering:** phải dựng và quản lý Direct Connect, lại còn mạng lưới peering giữa tất cả VPC, nên overhead tăng đáng kể. Peering cũng **non-transitive** nên số kết nối tăng theo kiểu full mesh khi thêm VPC.
- **B. Transit VPC:** vẫn chạy được (hub-and-spoke) nhưng phải tự quản lý **EC2 instance** (appliance VPN) trong transit VPC. Transit Gateway không cần EC2.
- **C. VPN riêng tới từng VGW + VPC peering:** phải tạo và quản lý nhiều VPN và nhiều peering. Càng thêm VPC thì số kết nối càng phình, không scalable.

#### Bảng so sánh

| Option | Mô hình | Kết nối on-prem | Kết nối VPC-VPC | Thêm VPC mới | Overhead |
|---|---|---|---|---|---|
| A | DX + peering | DX + VIF | Peering full mesh | Thêm nhiều peering | Cao |
| B | Transit VPC | VPN tới transit VPC | VPN qua EC2 | Thêm VPN + cấu hình | Cao (quản lý EC2) |
| C | VPN mỗi VGW + peering | Một VPN mỗi VPC | Peering full mesh | Thêm VPN + peering | Rất cao |
| **D** | **Transit Gateway** | **1 VPN attachment** | **Qua TGW** | **Chỉ attach** | **Thấp nhất** |

#### Biến thể đề có thể gặp

- **Chỉ có 2 VPC (và sẽ không thêm)** → **VPC peering giữa hai VPC + VPN tới từng VGW** là hợp lý, rẻ hơn TGW. Lưu ý peering không cho on-prem đi xuyên qua một VPC để sang VPC kia, nên mỗi VPC vẫn cần đường VPN riêng.
- **Cần băng thông lớn, ổn định, độ trễ thấp** → thay VPN bằng **Direct Connect gateway + Transit VIF** tới Transit Gateway; có thể giữ VPN làm backup.
- **Cần tăng throughput của VPN** → dùng nhiều tunnel với **ECMP** trên TGW.
- **VPC ở nhiều Region** → **TGW peering** giữa các Region.
- **Cần cô lập một số VPC với nhau** → dùng nhiều **TGW route table**.

#### Quy tắc nhớ cho thi

- **Thấy "nhiều VPC + on-prem + dễ mở rộng + ít vận hành"** → **Transit Gateway**.
- **Thấy "transit VPC"** → gần như luôn là đáp án cũ, tốn EC2; TGW thắng.
- **Thấy "peering giữa tất cả VPC"** → full mesh, không scalable, và **không transitive**.
- **Thấy "VPN riêng cho từng VPC"** → loại khi đề nhấn mạnh scalable.
- **Chỉ 2 VPC** → peering + VPN vẫn là phương án đơn giản, đừng ép dùng TGW.

### TD explanation

A. Direct Connect can connect on-premises networks to AWS. This solution would require the configuration and management of a Direct Connect connection and multiple VPC peering connections, significantly increasing operational overhead.
  For more information about Direct Connect, see What is AWS Direct Connect? https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

B. A transit VPC is a common way to connect geographically dispersed VPCs and remote networks to create a global network transit center. However, a transit VPC requires additional configuration and operational overhead because you must manage Amazon EC2 instances. With a transit gateway, there are no EC2 instances to manage.
  For more information about transit VPCs, see Transit VPC Solution. https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-vpc-solution.html

C. Site-to-Site VPN is a fully managed service that creates a secure connection between on-premises resources and AWS resources by using IPsec tunnels. A VPC peering connection is a network connection between two VPCs that gives you the ability to route traffic between the VPCs by using private addresses. A significant amount of operational overhead would result from the creation and management of multiple VPN connections and VPC peering connections.
  For more information about Site-to-Site VPN, see What is AWS Site-to-Site VPN? https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC\_VPN.html
  For more information about how to peer VPCs, see What is VPC Peering? https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html

D ✔. A transit gateway is a network transit hub that you can use to interconnect VPCs and on-premises networks. All the necessary connections can occur through a single transit gateway, minimizing operational overhead.
  For more information about transit gateways, see What is a Transit Gateway? https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html

</details>
