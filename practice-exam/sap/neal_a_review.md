# Neal Exam A — 75 questions (2026-10-22) — Wrong Answer Review (21 questions)

Source: `sap-neal-exam-a-2026-10-221021-results.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `neal_a_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q11](#q11) | ☐ | ☐ | ☐ |
| A | [Q13](#q13) | ☐ | ☐ | ☐ |
| A | [Q32](#q32) | ☐ | ☐ | ☐ |
| A | [Q34](#q34) | ☐ | ☐ | ☐ |
| A | [Q41](#q41) | ☐ | ☐ | ☐ |
| B | [Q1](#q1) | ☐ | ☐ | ☐ |
| B | [Q4](#q4) | ☐ | ☐ | ☐ |
| B | [Q16](#q16) | ☐ | ☐ | ☐ |
| B | [Q22](#q22) | ☐ | ☐ | ☐ |
| B | [Q27](#q27) | ☐ | ☐ | ☐ |
| B | [Q37](#q37) | ☐ | ☐ | ☐ |
| B | [Q44](#q44) | ☐ | ☐ | ☐ |
| C | [Q5](#q5) | ☐ | ☐ | ☐ |
| C | [Q17](#q17) | ☐ | ☐ | ☐ |
| C | [Q53](#q53) | ☐ | ☐ | ☐ |
| C | [Q70](#q70) | ☐ | ☐ | ☐ |
| D | [Q15](#q15) | ☐ | ☐ | ☐ |
| D | [Q55](#q55) | ☐ | ☐ | ☐ |
| D | [Q56](#q56) | ☐ | ☐ | ☐ |
| D | [Q72](#q72) | ☐ | ☐ | ☐ |
| D | [Q74](#q74) | ☐ | ☐ | ☐ |

---

# Group A — Known rule, new wording (VM Import, Budgets, Service Catalog, DR tier, WAF + usage plan) (5)

<a id="q11"></a>

## Q11

<!-- source: T4Q30 · domain: MIG -->



A company is running an application on an on-premises VMware cluster that must be migrated to an Amazon EC2 instance. While migrating, they wish to preserve the software and configuration settings.
What is the best strategy to meet these requirements?

- **A.** Configure the AWS DataSync agent to start replicating the data store to Amazon FSX for Windows File Server. Use the SMB share to host the VMware data store. Use VM Import/Export to move the VMs to Amazon EC2.
- **B.** Use the VMware vSphere client to export the application as an image in Open Virtualization Format (OVF) format. Create an Amazon S3 bucket to store the image in the destination AWS Region. Create and apply an IAM role for VM Import. Use the AWS CLI to run the EC2 import command.
- **C.** Configure AWS Storage Gateway for files service to export a Common Internet File System (CIFS) share. Create a backup copy to the shared folder. Sign into the AWS Management Console and create an AMI from the backup copy. Launch an EC2 instance that is based on the AMI.
- **D.** Create a managed-instance activation for a hybrid environment in AWS Systems Manager. Download and install Systems Manager Agent on the on-premises VM. Register the VM with Systems Manager to be a managed instance. Use AWS Backup to create a snapshot of the VM and create an AMI. Launch an EC2 instance that is based on the AMI.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** on-premises VMware app to EC2, preserve software and configuration

🪤 **Your trap:** 🔁 Picked DataSync + FSx for Windows datastore: wrong tool, VMware data store is not a file share. Intended path is OVF export to S3 then VM Import.

🧠 **Rule:** VM as-is to EC2: export OVF/OVA to S3, VM Import role, import-image.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem VMware cluster ──► (di chuyển 1 VM) ──► Amazon EC2
        Yêu cầu: GIỮ NGUYÊN software + configuration settings
```

Đáp án đúng: **B (export OVF + VM Import/Export)**. Anh chọn A.

#### Vì sao B đúng

Chuỗi bước: xuất VM từ vSphere client thành OVF, upload lên S3 bucket cùng Region đích, tạo IAM role cho VM Import (`vmimport`), chạy lệnh import bằng AWS CLI (ví dụ `import-image`). Kết quả là AMI chứa nguyên bản đĩa VM, nên phần mềm và cấu hình được giữ nguyên.

```
vSphere ──export OVF──► S3 ──VM Import (IAM role vmimport)──► AMI ──► EC2
```

#### Vì sao A (anh chọn) sai

A ghép DataSync + FSx for Windows File Server + SMB share làm VMware datastore rồi mới VM Import/Export. Điểm sai:
- DataSync/FSx lo chuyển dữ liệu file; đề giải thích chỉ hợp khi migrate dữ liệu trên file share Windows, không phải để chuyển VM VMware.
- Nó thêm các bước thừa mà bản thân VM Import đã làm được trực tiếp từ image.

#### Các phương án còn lại

- **C. Storage Gateway File (CIFS):** dùng cho hybrid storage; không có đường "tạo AMI từ backup trong share" như mô tả.
- **D. SSM hybrid activation + AWS Backup + AMI:** hợp khi cần giữ môi trường hybrid; đề giải thích khi đã có EC2 thì phần setup này thừa. Ngoài ra AWS Backup không snapshot VM on-prem thành AMI theo cách mô tả.

#### So sánh

| Phương án | Công cụ chính | Phù hợp migrate VM VMware? |
|---|---|---|
| **B** | OVF + S3 + VM Import | Có |
| A | DataSync + FSx + SMB | Không (cho file share) |
| C | Storage Gateway | Không (hybrid storage) |
| D | SSM + AWS Backup | Không (hybrid mgmt) |

#### Lưu ý thực tế

- VM Import cần IAM role `vmimport` với trust cho `vmie.amazonaws.com` và quyền đọc S3 bucket.
- Với migration quy mô lớn/liên tục, dịch vụ chuyên dụng (Application Migration Service) hay hơn; ở đề này chỉ một VM nên VM Import là đáp án.

#### Quy tắc nhớ cho thi

- **Thấy "VMware VM → EC2, giữ software + config"** → **export OVF + S3 + VM Import/Export**
- **Thấy DataSync/Storage Gateway trong bài migrate VM** → thường là bẫy (chuyển file, không chuyển VM)
- **Thấy IAM role cho VM Import** → `vmimport`

### TD explanation

You can use VM Import/Export to import virtual machine (VM) images from your virtualization environment to Amazon EC2 as Amazon Machine Images (AMI), which you can use to launch instances. Subsequently, you can export the VM images from an instance back to your virtualization environment. This enables you to leverage your investments in the VMs that you have built to meet your IT security, configuration management, and compliance requirements by bringing them into Amazon EC2. In this case the settings are preserved during the migration as per the requirement.
CORRECT:
"Use the VMware vSphere client to export the application as an image in Open Virtualization Format (OVF) format. Create an Amazon S3 bucket to store the image in the destination AWS Region. Create and apply an IAM role for VM Import. Use the AWS CLI to run the EC2 import command" is the correct answer (as explained above.)
INCORRECT:
"Configure the AWS DataSync agent to start replicating the data store to Amazon FSX for Windows File Server. Use the SMB share to host the VMware data store. Use VM Import/Export to move the VMs to Amazon EC2." is incorrect.
Since the question is specifically targeting a VMware instance, this option is incorrect, this would have been applicable only in case of a Windows based instance where the data on a file share must be migrated.
INCORRECT:
"Configure AWS Storage Gateway for files service to export a Common Internet File System (CIFS) share. Create a backup copy to the shared folder. Sign into the AWS Management Console and create an AMI from the backup copy. Launch an EC2 instance that is based on the AMI" is incorrect.
Storage Gateway is used for creating hybrid storage solutions and is unsuitable for migrating a VM into Amazon EC2.
INCORRECT:
"Create a managed-instance activation for a hybrid environment in AWS Systems Manager. Download and install Systems Manager Agent on the on-premises VM. Register the VM with Systems Manager to be a managed instance. Use AWS Backup to create a snapshot of the VM and create an AMI. Launch an EC2 instance that is based on the AMI." is incorrect.
This may be a suitable solution if the requirement is to maintain a hybrid environment where the instance running on-premises. As soon as the backup is complete and we spin up an instance in EC2, the entire setup before this step becomes redundant and might not be needed at a later stage.
References:
https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-migration-services/

</details>

<a id="q13"></a>

## Q13

<!-- source: T2Q19 · domain: ORG -->



A company uses Amazon RedShift for analytics. Several teams deploy and manage their own RedShift clusters and management has requested that the costs for these clusters is better managed. The management team has set budgets and once the budgetary thresholds have been reached a notification should be sent to a distribution list for managers. Teams should be able to view their RedShift cluster’s expenses to date. A Solutions Architect needs to create a solution that ensures the policy is centrally enforced in a multi-account environment.
Which combination of steps should the solutions architect take to meet these requirements? (Select TWO.)

- **A.** Update the AWS CloudFormation template to include the AWS::Budgets::Budget::resource with the NotificationsWithSubscribers property.
- **B.** Install the unified CloudWatch Agent on the RedShift cluster hosts. Track the billing metric data in CloudWatch and trigger an alarm when a threshold is reached.
- **C.** Create an AWS CloudTrail trail that tracks data events. Configure Amazon CloudWatch to monitor the trail and trigger an alarm when billing metrics exceed a certain threshold.
- **D.** Create an Amazon CloudWatch metric for billing. Create a custom alert when costs exceed the budgetary threshold.
- **E.** Create an AWS Service Catalog portfolio for each team. Add each team's Amazon RedShift cluster as an AWS CloudFormation template to their Service Catalog portfolio as a Product.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E · **You picked:** C, D

🔑 **Key words:** Redshift cost per team, budget threshold notification, view spend, multi-account, select two

🪤 **Your trap:** 🔁 Picked C (CloudTrail data events plus billing alarm): CloudTrail logs API calls, not cost. Missed Budgets resource in CloudFormation (A) plus Service Catalog products (E).

🧠 **Rule:** Cost alerts = AWS Budgets, not CloudTrail or CloudWatch agent; self-service enforced centrally = Service Catalog products with budgets attached.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhiều team ── mỗi team tự dựng Redshift cluster ── nhiều account
   Cần: (1) budget + thông báo khi chạm ngưỡng tới distribution list
        (2) team xem chi phí cluster của mình tới hiện tại
        (3) chính sách áp dụng TẬP TRUNG, multi-account
```

Đáp án đúng: **A + E**. Anh chọn C, D: cả hai đều sai.

#### Hai đáp án đúng ghép thành một giải pháp

- **E. Service Catalog portfolio mỗi team, cluster Redshift là Product (CloudFormation template):** tập trung hóa cách team dựng cluster, và Service Catalog cho gắn budget vào product/portfolio. Team xem được budgeted amount, current spend, forecasted spend ngay trên trang Product/Portfolio details.
- **A. Template CloudFormation có `AWS::Budgets::Budget` với `NotificationsWithSubscribers`:** budget được tạo cùng template, gửi thông báo tới subscribers (distribution list) khi chạm ngưỡng. Mọi cluster dựng từ template đều tự kèm budget, nên chính sách được thi hành tập trung.

```
Service Catalog Product (CFN template)
   ├── Redshift cluster
   └── AWS::Budgets::Budget ──► NotificationsWithSubscribers ──► email/DL
```

#### Vì sao C và D (anh chọn) sai

**C. CloudTrail data events + CloudWatch alarm:** CloudTrail ghi API call, không theo dõi dữ liệu billing.

**D. Tạo CloudWatch metric cho billing:** dữ liệu billing được thu thập tự động, không thể tự tạo metric billing (chỉ tạo alarm trên metric có sẵn). Hơn nữa không có phần xem chi phí theo team hay thi hành tập trung.

**B. CloudWatch agent trên Redshift hosts:** agent dành cho EC2, dùng gửi metric/log bổ sung, không dùng cho budgeting; cluster Redshift managed cũng không cài agent được.

#### So sánh

| Công cụ | Dùng để | Đáp ứng budget? |
|---|---|---|
| **AWS Budgets (A)** | Đặt ngưỡng + notify | Có |
| **Service Catalog (E)** | Chuẩn hóa deploy + hiển thị budget | Có |
| CloudTrail (C) | Ghi API call | Không |
| CloudWatch metric/agent (B, D) | Metric vận hành | Không phải budgeting |

#### Quy tắc nhớ cho thi

- **Thấy "budget + thông báo khi chạm ngưỡng"** → **AWS Budgets** (CFN: `AWS::Budgets::Budget`)
- **Thấy "team xem chi phí, kiểm soát tập trung, multi-account"** → **Service Catalog + budget gắn vào portfolio/product**
- **Thấy CloudTrail / CloudWatch agent cho chi phí** → loại
- Multi-select: chọn cặp "công cụ đo ngưỡng" + "cơ chế phân phối đồng nhất".

### TD explanation

You can use AWS Budgets to track your service costs and usage within AWS Service Catalog. You can associate budgets with AWS Service Catalog products and portfolios.
AWS Budgets gives you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.
If a budget is associated to a product, you can view information about the budget on the
Products
and
Product details
page. If a budget is associated to a portfolio, you can view information about the budget on the
Portfolios
and
Portfolio details
page.
When you click on a product or portfolio, you are taken to a detail page. These
Portfolio detail
and
Product detail
pages have a section with detailed information about the associated budget. You can see the budgeted amount, current spend, and forecasted spend. You also have the option to view budget details and edit the budget.
CORRECT:
"Update the AWS CloudFormation template to include the AWS::Budgets::Budget::resource with the NotificationsWithSubscribers property" is a correct answer.
CORRECT:
"Create an AWS Service Catalog portfolio for each team. Add each team's Amazon RedShift cluster as an AWS CloudFormation template to their Service Catalog portfolio as a Product" is also a correct answer.
INCORRECT:
"Install the unified CloudWatch Agent on the RedShift cluster hosts. Track the billing metric data in CloudWatch and trigger an alarm when a threshold is reached" is incorrect. This agent is used on EC2 instances for sending additional metric data and logs to CloudWatch. However, it is not used for budgeting.
INCORRECT:
"Create an AWS CloudTrail trail that tracks data events. Configure Amazon CloudWatch to monitor the trail and trigger an alarm when billing metrics exceed a certain threshold" is incorrect. CloudTrail tracks API calls, it cannot be used for tracking billing data.
INCORRECT:
"Create an Amazon CloudWatch metric for billing. Create a custom alert when costs exceed the budgetary threshold" is incorrect. Billing data is automatically collected, you cannot create a metric for billing but you can create an alarm.
References:
https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_budgets.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

</details>

<a id="q32"></a>

## Q32

<!-- source: T4Q23 · domain: CI -->



A company runs a single application in an AWS account. The application uses an Auto Scaling Group of Amazon EC2 instances with a combination of Reserved Instances (RIs) and On-Demand instances. To maintain cost-effectiveness the RIs should cover 70% of the workload. The solution should include the ability to alert the DevOps team if coverage drops below the 70% threshold.
Which set of steps should a Solutions Architect take to create the report and alert the DevOps team?

- **A.** Use AWS Budgets to create a budget for Rl coverage and set the threshold to 70%. Configure an alert that notifies the DevOps team.
- **B.** Use AWS Cost Explorer to configure a report for RI utilization and set the utilization target to 70%. Configure an alert that notifies the DevOps team.
- **C.** Use the AWS Billing and Cost Management console to create a reservation budget for RI utilization, set the utilization to 70%. Configure an alert that notifies the DevOps team.
- **D.** Use AWS Cost Explorer to create a budget for Rl coverage and set the threshold to 70%. Configure an alert that notifies the DevOps team.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** Reserved Instances should cover 70% of workload, alert DevOps if coverage drops

🪤 **Your trap:** 🔁 Picked Cost Explorer RI utilization report: utilization is purchased RI hours used, not coverage, and Cost Explorer does not alert. Use a Budgets RI coverage budget.

🧠 **Rule:** RI coverage threshold alert = AWS Budgets coverage budget; utilization is a different metric.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ASG: Reserved Instances (RI) + On-Demand
Mục tiêu: RI phủ 70% workload
Cần: báo cáo + ALERT cho DevOps khi coverage < 70%
```

Đáp án đúng: **A (AWS Budgets, RI coverage)**. Anh chọn B (Cost Explorer, RI utilization).

#### Hai trục cần phân biệt, và công cụ đúng

**Coverage vs Utilization:**
- **RI coverage:** bao nhiêu phần giờ chạy instance được RI chi trả. Đề yêu cầu "RI cover 70% workload", đây là coverage.
- **RI utilization:** bao nhiêu phần giờ RI đã mua được dùng bởi instance khớp. Không phải điều đề hỏi.

**Công cụ:** **AWS Budgets** có loại budget cho RI coverage, đặt ngưỡng và alert khi coverage rơi dưới ngưỡng (gửi email hoặc SNS topic). Đề nêu mỗi budget định nghĩa tối đa 5 notification.

#### Vì sao B (anh chọn) sai

B sai hai chỗ:
1. Dùng **Cost Explorer** để đặt ngưỡng và alert. Cost Explorer dùng để xem và phân tích; đặt ngưỡng cảnh báo là việc của AWS Budgets.
2. Chọn **utilization** thay vì **coverage**.

#### Các phương án còn lại

- **C. Reservation budget cho RI utilization:** đúng chỗ (Budgets) nhưng sai metric (utilization). Đề còn nhắc cần thêm cost allocation tags để báo cáo; theo đề, đây là điểm phương án bỏ sót.
- **D. Cost Explorer tạo budget cho RI coverage:** đúng metric nhưng sai công cụ; budget được tạo trong AWS Budgets (trong Billing and Cost Management console), không phải Cost Explorer.

#### Bảng đối chiếu cụm từ khác nhau

| Phương án | Công cụ | Metric | Kết luận |
|---|---|---|---|
| **A** | AWS Budgets | Coverage | Đúng |
| B | Cost Explorer | Utilization | Sai cả hai |
| C | Budgets (reservation budget) | Utilization | Sai metric |
| D | Cost Explorer | Coverage | Sai công cụ |

#### Quy tắc nhớ cho thi

- **Thấy "alert khi vượt/dưới ngưỡng"** → **AWS Budgets**, không phải Cost Explorer
- **Thấy "RI cover X% workload"** → **coverage**
- **Thấy "RI đã mua có được dùng hết không"** → **utilization**
- Mẹo: coverage = "workload được RI che bao nhiêu"; utilization = "RI mua về có dùng hết không".

### TD explanation

AWS Budgets allows customers to monitor how much of their Amazon EC2 instance usage is covered by reservations and to receive alerts when coverage falls below a specified threshold.
Reserved Instance (RI) coverage tracks the number of running instance hours that are covered by RIs, and can be measured over a daily, monthly, quarterly or yearly cadence. For example, you can monitor your RI coverage either at an aggregate level (e.g., monthly coverage of your entire Amazon EC2 RI fleet) or at a more granular level of detail (e.g., monthly coverage of Amazon RDS db.r3.large instances running in US East region).
You can then define up to five notifications per budget. Each notification can be sent to ten email subscribers and broadcast to an Amazon SNS topic of your choice.
Note: Cost Allocation Tags are not required for monitoring RI coverage. However, they are useful when you need to include detailed cost reporting for your EC2 instances.
CORRECT:
"Use AWS Budgets to create a budget for Rl coverage and set the threshold to 70%. Configure an alert that notifies the DevOps team" is the correct answer.
INCORRECT:
"Use AWS Cost Explorer to configure a report for RI utilization and set the utilization target to 70%. Configure an alert that notifies the DevOps team" is incorrect. You should use AWS Budgets not Cost Explorer for configuring a threshold of RI usage (should also user
coverage
not
utilization
).
INCORRECT:
"Use the AWS Billing and Cost Management console to create a reservation budget for RI utilization, set the utilization to 70%. Configure an alert that notifies the DevOps team" is incorrect. This answer misses the steps required to add cost allocation tags so there is no way to report on usage. RI coverage should be configured, not RI utilization. Utilization is simply the percentage of purchased RI hours that were used by matching instances. In this case we want to monitor coverage which is how much EC2 instance usage is covered by RIs.
INCORRECT:
"Use AWS Cost Explorer to create a budget for Rl coverage and set the threshold to 70%. Configure an alert that notifies the DevOps team" is incorrect. AWS Budgets should be used which can be found in the AWS Billing and Cost Management Console.
References:
https://aws.amazon.com/about-aws/whats-new/2017/08/monitor-your-reserved-instance-utilization-by-receiving-alerts-via-aws-budgets
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

</details>

<a id="q34"></a>

## Q34

<!-- source: T2Q23 · domain: NEW -->



A Solutions Architect needs to design the architecture for an application that requires high availability within and across AWS Regions. The design must support failover to the second Region within 1 minute and must minimize the impact on the user experience. The application will include three tiers, the web tier, application tier and NoSQL data tier.
Which combination of steps will meet these requirements? (Select THREE.)

- **A.** Use an Amazon Route 53 weighted routing policy set to 100/0 across the two selected Regions. Set Time to Live (TTL) to 30 minutes.
- **B.** Use an Amazon Route 53 failover routing policy for failover from the primary Region to the disaster recovery Region. Set Time to Live (TTL) to 30 seconds.
- **C.** Use Amazon DynamoDB with a global table across both Regions so reads and writes can occur in either location.
- **D.** Use an Amazon Aurora global database across both Regions so reads and writes can occur either location.
- **E.** Run the web and application tiers in both Regions in an active/passive configuration. Use Auto Scaling groups for the web and application layers across multiple Availability Zones in the Regions. Use zonal Reserved Instances for the minimum number of servers and On-Demand Instances for any additional resources.
- **F.** Run the web and application tiers in both Regions in an active/active configuration. Use Auto Scaling groups for the web and application layers across multiple Availability Zones in the Regions. Use Spot Instances for the required resources.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C, E · **You picked:** B, C, F

🔑 **Key words:** three-tier app, two Regions, failover within 1 minute, NoSQL tier, select three

🪤 **Your trap:** 🔁 Picked F (active/active on Spot): Spot capacity can be reclaimed, unacceptable for the always-on production tier. Pick active/passive ASG with zonal RIs plus On-Demand (E).

🧠 **Rule:** Always-on production tier: Reserved baseline + On-Demand, never Spot; DR tier matches 1-minute RTO with failover record and low TTL.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
        Route 53 (health check + failover, TTL 30s)
              │ primary                │ secondary
              ▼                        ▼
   Region 1: Web+App (ASG, Multi-AZ)   Region 2: Web+App (ASG, Multi-AZ)
              │                        │
              └──── DynamoDB global table (NoSQL, ghi 2 phía) ────┘
   Yêu cầu: HA trong + giữa Region, failover trong 1 PHÚT, tầng data NoSQL
```

Chọn đúng **3 mảnh ghép** cho 3 việc: DNS failover, tầng data, tầng web/app. Đáp án đúng: **B + C + E**. Anh chọn B, C đúng; sai ở tầng web/app (chọn **F** thay vì **E**).

#### Ba mảnh ghép đúng

- **B (failover routing + TTL 30s):** failover record dùng health check để tự chuyển sang secondary khi primary unhealthy. TTL 30s nghĩa là client cache kết quả DNS tối đa 30 giây, nên phù hợp mục tiêu 1 phút.
- **C (DynamoDB global table):** DynamoDB là NoSQL, global table cho phép đọc/ghi ở cả hai Region.
- **E (active/passive + ASG Multi-AZ):** Region phụ chạy sẵn nhóm tối thiểu, scale thêm khi có tải. Đề bài dùng mô hình này để cân bằng RTO và chi phí.

#### Vì sao F (anh chọn) sai

F trông hợp lý vì active/active nghe "HA hơn". Nhưng điểm gãy là **Spot Instances cho toàn bộ tài nguyên bắt buộc**: Spot có thể bị thu hồi hoặc không có capacity khi giá vượt mức đặt. Khi đó web/app tier có thể không có instance đúng lúc cần, phá yêu cầu "minimize impact on user experience". E dùng **zonal Reserved Instances** cho mức tối thiểu (zonal RI có reserve capacity trong AZ) + **On-Demand** cho phần dư, nên capacity luôn sẵn.

#### Các phương án sai còn lại

- **A:** weighted 100/0 không tự chuyển khi lỗi (phải sửa weight thủ công), và TTL 30 **phút** thì client giữ cache DNS quá lâu, vượt xa 1 phút.
- **D:** Aurora là relational, không phải NoSQL; Aurora global database chỉ có **một writer Region**, không ghi được ở cả hai nơi như đáp án mô tả.

| Phương án | Điểm quyết định | Kết quả |
|---|---|---|
| A. Weighted 100/0, TTL 30 phút | Không tự failover, cache DNS 30 phút | Sai |
| **B. Failover, TTL 30s** | Health check + cache ngắn | Đúng |
| **C. DynamoDB global table** | NoSQL, ghi 2 Region | Đúng |
| D. Aurora global DB | Relational, 1 writer Region | Sai |
| **E. Active/passive, RI + On-Demand** | Capacity chắc chắn có | Đúng |
| F. Active/active, toàn Spot | Spot có thể mất | Sai |

#### Lưu ý thực tế

- 📝 **Ghi chú kỹ thuật:** E gọi là "active/passive", trong thực tế gần với **warm standby**. Quy tắc đề: theo đáp án của đề.
- Failover thực tế còn phụ thuộc thời gian health check phát hiện lỗi (interval x ngưỡng fail), không chỉ TTL. Đề đơn giản hóa phần này.

#### Quy tắc nhớ cho thi

- **Thấy "NoSQL + ghi ở nhiều Region"** → **DynamoDB global tables**
- **Thấy "relational + cross-Region"** → Aurora global database nhưng chỉ **1 writer Region**
- **Thấy "failover trong ~1 phút"** → **Route 53 failover + TTL thấp (giây)**, không phải weighted/TTL phút
- **Thấy "Spot" cho phần bắt buộc, luôn phải có** → loại; Spot chỉ cho phần dư/chịu gián đoạn

### TD explanation

The requirements can be achieved by using an Amazon DynamoDB database with a global table. DynamoDB is a NoSQL database so it fits the requirements. A global table also allows both reads and writes to occur in both Regions.
For the web and application tiers Auto Scaling groups should be configured. Due to the 1-minute RTO these must be configured in an active/passive state. The best pricing model to lower price but ensure resources are available when needed is to use a combination of zonal reserved instances and on-demand instances.
To failover between the Regions, a Route 53 failover routing policy can be configured with a TTL configured on the record of 30 seconds. This will mean clients must resolve against Route 53 every 30 seconds to get the latest record. In a failover scenario the clients would be redirected to the secondary site if the primary site is unhealthy.
CORRECT:
"Use an Amazon Route 53 failover routing policy for failover from the primary Region to the disaster recovery Region. Set Time to Live (TTL) to 30 seconds" is a correct answer.
CORRECT:
"Use Amazon DynamoDB with a global table across both Regions so reads and writes can occur in either location" is also a correct answer.
CORRECT:
"Run the web and application tiers in both Regions in an active/passive configuration. Use Auto Scaling groups for the web and application layers across multiple Availability Zones in the Regions. Use zonal Reserved Instances for the minimum number of servers and On-Demand Instances for any additional resources" is also a correct answer.
INCORRECT:
"Use an Amazon Route 53 weighted routing policy set to 100/0 across the two selected Regions. Set Time to Live (TTL) to 30 minutes" is incorrect. A weighted routing policy would need to be updated to change the weightings and the TTL here is too high as clients will cache the result for 30 minutes.
INCORRECT:
"Use an Amazon Aurora global database across both Regions so reads and writes can occur either location" is incorrect. An Aurora database is a relational DB, not a NoSQL DB. Also, Aurora global database does not allow writes in multiple Regions, only reads.
INCORRECT:
"Run the web and application tiers in both Regions in an active/active configuration. Use Auto Scaling groups for the web and application layers across multiple Availability Zones in the Regions. Use Spot Instances for the required resources" is incorrect. Spot instances may not be available if the maximum price configured is exceeded. This could result in instances not being available when needed.
References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q41"></a>

## Q41

<!-- source: T4Q9 · domain: CI · flagged -->



A Solutions Architect has deployed a REST API using an Amazon API Gateway Regional endpoint. The API will be consumed by a growing number of US-based companies. Each company will use the API twice each day to get the latest data.
Following the deployment of the API the operations team noticed thousands of requests coming from hundreds of IP addresses around the world. The traffic is believed to be originating from a botnet. The Solutions Architect must secure the API while minimizing cost.
Which approach should the company take to secure its API?

- **A.** Create an Amazon CloudFront distribution with the API as the origin. Create an AWS WAF web ACL with a rule to block clients that submit more than ten requests per day. Associate the web ACL with the CloudFront distribution. Configure CloudFront with an origin access identity (OAI) and associate it with the distribution. Configure API Gateway to ensure only the OAI can execute the GET method.
- **B.** Create an Amazon CloudFront distribution with the API as the origin. Create an AWS WAF web ACL with a rule to block clients that submit more than ten requests per day. Associate the web ACL with the CloudFront distribution. Add a custom header to the CloudFront distribution populated with an API key. Configure the API to require an API key on the GET method.
- **C.** Create an AWS WAF web ACL with a rule to allow access to the IP addresses used by the companies. Associate the web ACL with the API. Create a resource policy with a request limit and associate it with the API. Configure the API to require an API key on the POST method.
- **D.** Create an AWS WAF web ACL with a rule to allow access from the IP addresses used by the companies. Associate the web ACL with the API. Create a usage plan with a request limit and associate it with the API. Create an API key and add it to the usage plan.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** API Gateway Regional REST API, botnet traffic, few US companies twice daily, secure at minimum cost

🪤 **Your trap:** 🔁 Picked CloudFront + WAF per-day rate rule: WAF rate rules use short windows, not per day; CloudFront adds cost. Needs WAF IP allow-list plus usage plan and API key.

🧠 **Rule:** Known client IPs + low volume: WAF IP allow-list on the API, usage plan + API key; skip CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client (hàng trăm IP toàn cầu, nghi botnet) ──► API Gateway Regional (REST)
Người dùng hợp lệ: vài công ty US, mỗi công ty gọi 2 lần/ngày
Yêu cầu: bảo vệ API, CHI PHÍ THẤP NHẤT
```

Đáp án đúng: **D**. Anh chọn **B**.

#### Vì sao D đúng

D ghép ba lớp, mỗi lớp một việc, không thừa dịch vụ:

- **WAF web ACL allow-list IP** gắn trực tiếp vào API: traffic từ IP lạ (botnet) bị chặn trước khi vào API. Nguồn hợp lệ là công ty US biết trước IP.
- **Usage plan với request limit** (throttle/quota): giới hạn mức dùng của mỗi client.
- **API key** gắn usage plan: nhận diện client để áp hạn mức.

Không có CloudFront nên không tốn thêm chi phí, khớp "minimize cost".

#### Vì sao B (anh chọn) sai

B trông hợp lý vì CloudFront + WAF + API key đều là kiểu bảo vệ quen thuộc. Nhưng:

1. **WAF rate-based rule không đặt được giới hạn theo ngày.** Rule đếm request theo cửa sổ thời gian ngắn tính bằng phút, nên "10 request/ngày" không thể cấu hình.
2. **Thêm CloudFront chỉ để bảo vệ API là chi phí không cần thiết**, trái với yêu cầu chi phí thấp nhất.
3. B cũng không allow-list IP, nên botnet vẫn tới được CloudFront.

#### Các phương án sai còn lại

- **A:** cùng lỗi "10 request/ngày" của rate-based rule, thêm lỗi **OAI chỉ dùng cho S3**, không dùng được với API Gateway.
- **C:** **resource policy** chỉ cho phép/chặn principal hoặc IP, **không có request limit**; request limit nằm ở usage plan hoặc WAF rate-based rule. API key nên yêu cầu trên GET (API để lấy dữ liệu), không phải POST.

| Cơ chế | Giới hạn theo ngày? | Chặn IP lạ? |
|---|---|---|
| WAF rate-based rule | Không (cửa sổ phút) | Theo tốc độ |
| **Usage plan (quota/throttle)** | Có (quota theo ngày/tuần/tháng) | Không |
| **WAF IP allow-list** | Không | Có |
| Resource policy | Không | Có (IP/principal) |

#### Lưu ý thực tế

> ⚠️ Giải thích của vendor trộn lẫn WAF rate-based rule với usage plan, và coi API key như xác thực.

📝 **Ghi chú kỹ thuật:** rate-based rule thuộc **WAF**, không "gắn vào usage plan". **API key không phải cơ chế authentication**; nó dùng để nhận diện client và áp usage plan. Phần bảo vệ thật sự khỏi botnet ở D là **WAF IP allow-list**; usage plan lo hạn mức. Đáp án D giữ nguyên.

Đề này anh đã đánh dấu chưa chắc. Điểm phân biệt nhanh: nếu một phương án có "per day" gắn với WAF, hoặc OAI với API Gateway, loại ngay.

#### Quy tắc nhớ cho thi

- **Thấy "giới hạn theo ngày/tháng cho từng client API"** → **usage plan + API key**
- **Thấy "WAF rate-based"** → cửa sổ ngắn tính theo phút, không phải ngày
- **Thấy "OAI + API Gateway"** → sai; OAI cho S3
- **Thấy "minimize cost" + chỉ cần bảo vệ API** → không thêm CloudFront
- **API key** = nhận diện/hạn mức, **không** = authentication

### TD explanation

> ⚠️ Explanation conflates WAF rate-based rules with usage plans; API keys are not authentication.

The rate-based rules associated with usage plans specify the number of web requests that are allowed by each client IP in a trailing, continuously updated, 5-minute period. The API key associated with the usage plan ensures that only clients who are using the API key in their requests are granted access. This solution requires that the IP addresses of clients are whitelisted and the API key is distributed to clients to use in their requests to the API.
CORRECT:
"Create an AWS WAF web ACL with a rule to allow access from the IP addresses used by the companies. Associate the web ACL with the API. Create a usage plan with a request limit and associate it with the API. Create an API key and add it to the usage plan" is correct.
INCORRECT:
"Create an Amazon CloudFront distribution with the API as the origin. Create an AWS WAF web ACL with a rule to block clients that submit more than ten requests per day. Associate the web ACL with the CloudFront distribution. Add a custom header to the CloudFront distribution populated with an API key. Configure the API to require an API key on the GET method" is incorrect answer.
A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action on IPs with rates that go over a limit. You set the limit as the number of requests per 5-minute time span. You cannot configure an AWS WAF rate-based rule to limit request to 10 per day. Also, to minimize cost CloudFront is not required in this solution.
INCORRECT:
"Create an Amazon CloudFront distribution with the API as the origin. Create an AWS WAF web ACL with a rule to block clients that submit more than ten requests per day. Associate the web ACL with the CloudFront distribution. Configure CloudFront with an origin access identity (OAI) and associate it with the distribution. Configure API Gateway to ensure only the OAI can execute the GET method" is incorrect.
As above for rate-based rules. An OAI is a special CloudFront user that is used with Amazon S3 buckets to prevent direct access using S3 URLs. It is usually used along with other protections such as signed URLs and signed cookies. It is not possible to use an OAI with API Gateway APIs.
INCORRECT:
"Create an AWS WAF web ACL with a rule to allow access to the IP addresses used by the companies. Associate the web ACL with the API. Create a resource policy with a request limit and associate it with the API. Configure the API to require an API key on the POST method" is incorrect.
AWS WAF resource policies control whether or not a principal or source IP address/CIDR block is allowed to invoke the API. A resource policy does not have a request limit associated with it, use a Web ACL rate-based rule for that. The API key should be configured on the GET method as this API is being used to get data and not post it.
References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html
https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

---

# Group B — Multi-select half right (one correct pick, one plausible distractor kept) (7)

<a id="q1"></a>

## Q1

<!-- source: T6Q30 · domain: NEW -->



A rapidly growing company has registered 10 new domain names for multiple applications soon to be productionized. The company uses the domains for online marketing. The company needs a solution that will redirect online visitors to a specific URL and route combination for each domain. The URL and route combinations are defined in a JSON document. All DNS records are managed by Amazon Route 53. They also need to accept HTTP and HTTPS requests.
Which combination of steps should a solutions architect take to meet these requirements with the LEAST amount of operational effort? (Select THREE.)

- **A.** Create a dynamic webpage and host it on an Amazon EC2 instance. Configure the webpage to use the JSON document in combination with the event message to look up and respond with a redirect URL.
- **B.** Create an Application Load Balancer that includes HTTP and HTTPS listeners.
- **C.** Create an AWS Lambda function that uses the event message and specified JSON document to look up and respond with a redirect URL.
- **D.** Use an Amazon API Gateway API with a custom domain to publish an AWS Lambda function.
- **E.** Create an Amazon CloudFront distribution and deploy a Lambda@Edge function.
- **F.** Create an SSL certificate by using AWS Certificate Manager (ACM). Include the domains as Subject Alternative Names.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E, F · **You picked:** C, D, E

🔑 **Key words:** redirect 10 domains by JSON route, HTTP and HTTPS, least operational effort, select three

🪤 **Your trap:** Picked C and D: a plain Lambda or API Gateway needs code change per JSON update and misses the edge. Missed ALB HTTP/HTTPS listeners (B) and ACM SAN certificate (F).

🧠 **Rule:** Many domains: ACM cert with SANs + CloudFront Lambda@Edge for redirect logic; ALB needs both HTTP and HTTPS listeners.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Visitor ──► domain1..domain10 (Route 53) ──► ??? ──► redirect tới URL + route
                                               │
                     mapping URL/route nằm trong 1 file JSON
        Yêu cầu: nhận HTTP + HTTPS, ÍT công vận hành NHẤT, chọn 3
```

Đáp án đúng: **B + E + F**. Anh chọn C, D, E: đúng E, nhưng thiếu B và F, và chọn thừa C, D.

#### Ba lựa chọn đúng ghép thành một giải pháp

- **E. CloudFront + Lambda@Edge:** function chạy ở edge, đọc request (domain + path), tra JSON rồi trả redirect. Một distribution phục vụ cả 10 domain, thêm domain chỉ sửa mapping.
- **F. ACM certificate với Subject Alternative Names:** một cert chứa cả 10 domain để HTTPS hoạt động cho mọi domain trên cùng distribution. Route 53 trỏ alias các domain về distribution.
- **B. ALB có listener HTTP và HTTPS:** theo đáp án của đề, đây là phần "accept HTTP and HTTPS requests"; listener HTTPS cũng cần cert (dùng lại cert ACM ở F được).

#### Vì sao C và D (anh chọn) sai

**C. Lambda đơn thuần:** đề giải thích Lambda phải sửa mỗi khi file cấu hình đổi, tăng công sức, và Lambda không tự có endpoint HTTP/HTTPS cho 10 domain.

**D. API Gateway + custom domain + Lambda:** mỗi lần thêm hoặc đổi domain phải cấu hình lại custom domain và deploy stage, nên không phải "ít công vận hành nhất".

**A. EC2 dynamic webpage:** phải quản lý server, đề yêu cầu hướng serverless.

#### So sánh vai trò từng phần

| Nhu cầu | Thành phần | Ghi chú |
|---|---|---|
| Logic redirect theo domain + path | Lambda@Edge (E) | Chạy gần viewer, dựa trên request |
| HTTPS cho nhiều domain | ACM SAN cert (F) | Một cert nhiều tên |
| Nhận HTTP + HTTPS | ALB 2 listener (B) | HTTPS listener cần cert |
| Lambda/API Gateway riêng lẻ (C, D) | Phải sửa/deploy lại | Nhiều công vận hành |

#### Lưu ý thực tế

- 📝 Ghi chú kỹ thuật: trong thực tế CloudFront cũng tự redirect HTTP sang HTTPS (viewer protocol policy), và ALB có redirect rule gốc. Đề này vẫn lấy B, E, F làm đáp án, nên giữ theo đề.
- Cert dùng cho CloudFront phải được tạo ở **us-east-1**.
- Lambda@Edge tạo ở us-east-1 rồi được replicate ra các edge location.

#### Quy tắc nhớ cho thi

- **Thấy "redirect nhiều domain theo JSON/mapping, ít vận hành"** → **CloudFront + Lambda@Edge**
- **Thấy "nhiều domain, HTTPS"** → **ACM cert với SAN**
- **Thấy "Lambda/API Gateway phải sửa mỗi khi cấu hình đổi"** → loại, vì tăng công vận hành
- Multi-select 3 đáp án: ghép thành một chuỗi hoàn chỉnh (routing + cert + listener), không chọn các mảnh rời nhau.

### TD explanation

Lambda@Edge allows you to execute custom business logic closer to the viewer. This capability enables intelligent/programmable processing of HTTP requests at locations that are closer (for the purpose of latency) to your viewer. In this case the Lambda@Edge function can be written so that it redirects viewers based on information in the request based on domain and path.
To accept multiple custom domains on the CloudFront distribution a certificate can be created in ACM that includes multiple subject alternative names. These names can then be used in Route 53 records pointing to the distribution.
The ALB may will need to be configured with both an HTTP and an HTTPS listener. The HTTPS listener will also require a certificate, and this could use the same certificate used in the CloudFront distribution or it could be a separate certificate.
CORRECT:
"Create an Application Load Balancer that includes HTTP and HTTPS listeners" is a correct answer (as explained above.)
CORRECT:
"Create an Amazon CloudFront distribution and deploy a Lambda@Edge function" is also a correct answer (as explained above.)
CORRECT:
"Create an SSL certificate by using AWS Certificate Manager (ACM). Include the domains as Subject Alternative Names" is also a correct answer (as explained above.)
INCORRECT:
"Create a dynamic webpage and host it on an Amazon EC2 instance. Configure the webpage to use the JSON document in combination with the event message to look up and respond with a redirect URL" is incorrect.
While designing such a solution, serverless should be utilized and hence EC2 isn’t an appropriate use case for this scenario.
INCORRECT:
"Create an AWS Lambda function that uses the event message and specified JSON document to look up and respond with a redirect URL" is incorrect.
With this solution, Lambda would need a change every time config file changes and would increase effort, hence this is not an efficient option.
INCORRECT:
"Use an Amazon API Gateway API with a custom domain to publish an AWS Lambda function" is incorrect.
With this option as well, for each domain addition or change, API gateway stages would have to be re deployed hence this is again an ineffective choice.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/elb-redirect-to-another-domain-with-alb/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-cloudfront/

</details>

<a id="q4"></a>

## Q4

<!-- source: T6Q1 · domain: NEW -->



An application generates around 15 GB of statistical data each day and this is expected to increase over time. A Solutions Architect plans to store the data in Amazon S3 and use Amazon Athena to analyze the data. The data will be analyzed using date ranges.
Which combination of steps will ensure optimal performance as the data grows? (Select TWO.)

- **A.** Store each object in Amazon S3 with a key that uses a random string.
- **B.** Store the data in separate buckets for each date range.
- **C.** Store the data in Amazon S3 using Apache Parquet or Apache ORC formats.
- **D.** Store the data in Amazon S3 compressed files less than 10 MB in size.
- **E.** Store the data using Apache Hive partitioning in Amazon S3 using a key that includes a date.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E · **You picked:** B, C

🔑 **Key words:** 15 GB/day statistics, S3 plus Athena, date-range queries, optimal performance, select two

🪤 **Your trap:** Picked B: a bucket per date range is not an Athena tuning practice. Missed Hive-style date partitioning (E), which prunes scans for date queries.

🧠 **Rule:** Athena speed: columnar Parquet/ORC + date partitions so date-range queries scan less data.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
App ──► 15 GB/ngày ──► S3 ──► Athena (query theo khoảng ngày)
                       Dữ liệu tăng dần theo thời gian
        Yêu cầu: hiệu năng tối ưu khi data lớn, chọn 2
```

Đáp án đúng: **C + E**. Anh chọn B, C: đúng C, sai B (thiếu E).

#### Hai đáp án đúng, mỗi cái giải quyết một việc

**C. Parquet hoặc ORC (columnar):** Athena tính tiền và tốn thời gian theo lượng dữ liệu quét. Định dạng cột chỉ đọc các cột cần dùng, lại nén tốt, nên quét ít hơn nhiều so với CSV/JSON.

**E. Hive partitioning theo ngày:** key dạng `year=2026/month=10/day=22/`. Khi query có điều kiện ngày, Athena chỉ quét các partition khớp (partition pruning), bỏ qua phần còn lại.

```
s3://bucket/stats/year=2026/month=10/day=22/part-0.parquet
WHERE day BETWEEN ... --> chỉ đọc đúng các prefix đó
```

#### Vì sao B (anh chọn) sai

Tách mỗi khoảng ngày thành một bucket trông giống partition, nhưng:
- Athena table trỏ vào một location; nhiều bucket nghĩa là nhiều bảng hoặc phải quản lý thủ công, không có partition pruning.
- Đề giải thích đây "không phải khuyến nghị hiệu năng". Cách đúng là **một bucket, nhiều prefix partition**.

#### Các phương án còn lại

- **A. Key ngẫu nhiên:** không phải khuyến nghị tối ưu Athena; key ngẫu nhiên làm mất tính phân vùng theo ngày nên không thể pruning.
- **D. File nén dưới 10 MB:** nhiều file nhỏ làm tăng overhead mở file; đề xếp vào nhóm không phải khuyến nghị hiệu năng.

#### So sánh

| Cách | Giảm dữ liệu quét? | Hợp query theo ngày? |
|---|---|---|
| **C. Parquet/ORC** | Có (chỉ đọc cột cần) | Trung tính |
| **E. Hive partition theo ngày** | Có (chỉ đọc partition khớp) | Có |
| B. Bucket riêng mỗi khoảng ngày | Không | Không |
| A. Key ngẫu nhiên | Không | Không |
| D. File nhỏ | Không | Không |

#### Quy tắc nhớ cho thi

- **Thấy "Athena tối ưu hiệu năng/chi phí"** → **columnar (Parquet/ORC) + partition + (nén)**
- **Thấy "query theo date range"** → **partition key theo ngày**
- **Thấy "mỗi khoảng ngày một bucket"** → bẫy, đúng là một bucket nhiều prefix
- Multi-select: đáp án đúng thường bổ sung nhau (định dạng + phân vùng), không trùng chức năng.

### TD explanation

There are several recommendations for optimizing the performance of Athena (see link below). These include storing data in a columnar format such as Apache Parquet or Apache ORC and using Apache Hive partitioning in Amazon S3 using a key that includes a date.
CORRECT:
"Store the data in Amazon S3 using Apache Parquet or Apache ORC formats" is a correct answer.
CORRECT:
"Store the data using Apache Hive partitioning in Amazon S3 using a key that includes a date" is also a correct answer.
INCORRECT:
"Store each object in Amazon S3 with a key that uses a random string" is incorrect. This is not a performance recommendation.
INCORRECT:
"Store the data in Amazon S3 compressed files less than 10 MB in size" is incorrect. This is not a performance recommendation
INCORRECT:
"Store the data in separate buckets for each date range" is incorrect. This is not a performance recommendation.
References:
https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

</details>

<a id="q16"></a>

## Q16

<!-- source: T2Q7 · domain: CI -->



A company has deployed two Microsoft Active Directory Domain Controllers into an Amazon VPC with a default configuration. The DHCP options set associated with the VPC has been configured to assign the IP addresses of the Domain Controllers as DNS servers. A VPC interface endpoint has been created but EC2 instances within the VPC are unable to resolve the private endpoint addresses.
Which strategies could a Solutions Architect use to resolve the issue? (Select TWO.)

- **A.** Define an outbound Amazon Route 53 Resolver. Set a conditional forwarding rule for the Active Directory domain to the Active Directory servers. Configure the DNS settings in the VPC DHCP options set to use the AmazonProvidedDNS servers.
- **B.** Define an inbound Amazon Route 53 Resolver. Set a conditional forwarding rule for the Active Directory domain to the Active Directory servers. Configure the DNS settings in the VPC DHCP options set to use the AmazonProvidedDNS servers.
- **C.** Update the DNS service on the Active Directory servers to forward all queries to the VPC Resolver.
- **D.** Update the DNS service on the Active Directory servers to forward all non-authoritative queries to the VPC Resolver.
- **E.** Configure the DNS service on the EC2 instances in the VPC to use the VPC resolver server as the secondary DNS server.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** A, E

🔑 **Key words:** AD domain controllers as DHCP DNS, interface endpoint names not resolving, select two

🪤 **Your trap:** Picked E (VPC resolver as secondary DNS): a secondary DNS is only a failover, not split by query. Fix is DC forwarding of non-authoritative queries (D).

🧠 **Rule:** Custom DNS servers need a forward path to the VPC resolver; secondary DNS does not split queries.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC: DHCP options set ──► DNS = 2 Domain Controller (AD)
EC2 ──hỏi DNS──► DC ──?──► tên VPC interface endpoint (private)
DC không có record của endpoint ⇒ EC2 không resolve được
```

Đáp án đúng: **A + D** (hai cách độc lập, mỗi cách tự giải quyết vấn đề). Anh chọn A, E: đúng A, sai E.

#### Gốc vấn đề

EC2 chỉ hỏi DC. DC không biết tên của VPC interface endpoint (tên này do VPC resolver phân giải). Cần để truy vấn tới được VPC resolver, hoặc theo chiều DC chuyển tiếp ra, hoặc EC2 hỏi resolver trước.

#### Hai cách đúng

**D. DC forward truy vấn non-authoritative sang VPC Resolver:** DC trả lời theo zone của mình; tên nào không có thì chuyển tiếp sang VPC resolver. Vẫn giữ được phân giải nội bộ AD.

**A. Outbound Route 53 Resolver + conditional forwarding rule:** đổi DHCP options sang `AmazonProvidedDNS`, rồi tạo outbound endpoint với rule chuyển tiếp riêng domain AD tới các DC. Tên AD đi tới DC, mọi tên khác (kể cả endpoint) do VPC resolver tự xử lý.

```
EC2 ──► AmazonProvidedDNS ──┬── tên AD  ──(forward rule, outbound)──► DC
                            └── tên khác (interface endpoint) ──► tự resolve
```

#### Vì sao E (anh chọn) sai

Đặt VPC resolver làm DNS **phụ** (secondary): secondary chỉ là dự phòng khi primary không phản hồi, không dùng để chia truy vấn. DC vẫn trả lời (từ chối/không có record) nên client không chuyển sang secondary theo tên.

#### Các phương án còn lại

- **B. Inbound resolver + forwarding rule:** inbound endpoint nhận truy vấn từ ngoài vào VPC; không cấu hình forwarding rule trên inbound resolver. Forwarding rule thuộc về outbound.
- **C. Forward TẤT CẢ truy vấn sang VPC resolver:** DC sẽ không trả lời từ zone của chính nó nữa, phá phân giải tên AD.

#### So sánh

| Hướng | Có forwarding rule? | Dùng để |
|---|---|---|
| **Outbound resolver** | Có | VPC hỏi DNS bên ngoài (on-prem/AD) |
| Inbound resolver | Không | Mạng ngoài hỏi vào VPC |
| Forward non-authoritative (D) | Cấu hình tại DC | Chỉ phần DC không biết |
| Forward ALL (C) | Cấu hình tại DC | Phá zone nội bộ |

#### Quy tắc nhớ cho thi

- **Thấy "VPC hỏi DNS on-prem/AD"** → **outbound resolver + rule**
- **Thấy "on-prem hỏi tên trong VPC"** → **inbound resolver**
- **Thấy "forward non-authoritative"** → đúng; **"forward ALL"** → sai
- **Secondary DNS** → dự phòng, không phải chia truy vấn

### TD explanation

The EC2 instances are unable to resolve the DNS name of the VPC interface endpoint to an IP address as they are configured to use the Domain Controllers for DNS and the DCs do not have a record for the VCP interface endpoint.
There are two solutions to this problem that both achieve the same outcome. The first involves modifying the DNS service on the DCs to forward non-authoritative queries to the VPC resolver. This simply means if the DNS service on the DC does not have the record in its zone file it will forward the query to another DNS service.
The second solution uses an outbound Route 53 resolver. With outbound resolvers (but not with inbound resolvers) you can configure forwarding rules. In this case you would need to modify the EC2 instances (via the DHCP options set) to use the Amazon provided DNS servers. These servers would be able to resolve the VPC interface endpoint. The forwarding rule will forward any traffic for the Domain Controllers to those servers.
CORRECT:
"Update the DNS service on the Active Directory servers to forward all non-authoritative queries to the VPC Resolver" is a correct answer.
CORRECT:
"Define an outbound Amazon Route 53 Resolver. Set a conditional forwarding rule for the Active Directory domain to the Active Directory servers. Configure the DNS settings in the VPC DHCP options set to use the AmazonProvidedDNS servers" is also a correct answer.
INCORRECT:
"Define an inbound Amazon Route 53 Resolver. Set a conditional forwarding rule for the Active Directory domain to the Active Directory servers. Configure the DNS settings in the VPC DHCP options set to use the AmazonProvidedDNS servers" is incorrect. You cannot configure a forwarding rule on an inbound resolver.
INCORRECT:
"Configure the DNS service on the EC2 instances in the VPC to use the VPC resolver server as the secondary DNS server" is incorrect. A secondary DNS server is used as a backup for the primary DNS server that is configured on a client. It is not meant for splitting queries.
INCORRECT:
"Update the DNS service on the Active Directory servers to forward all queries to the VPC Resolver" is incorrect. This would mean the DNS server on the DCs does not respond to queries from its own zone file as it will forward ALL queries to the VPC resolver.
References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q22"></a>

## Q22

<!-- source: T4Q25 · domain: NEW -->



A company requires an application in which employees can log expense claims for processing. The expense claims are typically submitted each week on a Friday. The application must store data in a format that will allow the finance team to be able to run end of month reports. The solution should be highly available and must scale seamlessly based on demand.
Which combination of solution options meets these requirements with the LEAST operational overhead? (Select TWO.)

- **A.** Deploy the application to Amazon EC2 On-Demand Instances behind an Application Load Balancer. Use Amazon EC2 Auto Scaling and schedule additional capacity ahead of peak usage periods.
- **B.** Deploy the application in a container using Amazon ECS behind an Application Load Balancer. Use Service Auto Scaling and schedule additional capacity ahead of peak usage periods.
- **C.** Deploy the application front end to an Amazon S3 bucket served by Amazon CloudFront. Deploy the application backend using Amazon API Gateway with an AWS Lambda proxy integration.
- **D.** Store the expense claim data in Amazon EMR. Use Amazon QuickSight to generate the reports using Amazon EMR as the data source.
- **E.** Store the expense claim data in Amazon S3. Use Amazon Athena and Amazon QuickSight to generate the reports using Amazon S3 as the data source.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E · **You picked:** B, E

🔑 **Key words:** expense app Friday bursts, finance month-end reports, HA, least operational overhead, select two

🪤 **Your trap:** Picked B (ECS behind ALB): containers still need cluster or capacity management unless Fargate. Serverless S3/CloudFront + API Gateway + Lambda (C) has least overhead.

🧠 **Rule:** Least overhead + bursty: serverless front/back end (S3, CloudFront, API Gateway, Lambda); S3 + Athena + QuickSight for reports.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhân viên nộp expense claim (cao điểm mỗi thứ Sáu)
   ──► ứng dụng ──► lưu dữ liệu ──► báo cáo cuối tháng
Yêu cầu: highly available, scale liền mạch, ÍT vận hành nhất (chọn 2)
```

Đáp án đúng: **C + E**. Anh chọn B, E: đúng E, sai B.

#### Hai đáp án đúng

- **C. Front end trên S3 + CloudFront, backend API Gateway + Lambda proxy:** toàn bộ serverless, tự scale theo tải, không phải quản lý server. Hợp mẫu tải theo đợt (cao điểm thứ Sáu).
- **E. Lưu trên S3, dùng Athena + QuickSight:** S3 lưu dữ liệu bền vững, Athena truy vấn trực tiếp, QuickSight vẽ báo cáo cuối tháng. Không cần cluster nào.

#### Vì sao B (anh chọn) sai

ECS sau ALB với Service Auto Scaling tuy scale được, nhưng đề giải thích ECS cần quản lý instance (trừ khi dùng Fargate, mà phương án không nêu). Phương án còn **lên lịch tăng capacity trước cao điểm**: đó là công việc vận hành, trái với "scale liền mạch theo demand, ít overhead".

#### Các phương án còn lại

- **A. EC2 On-Demand + ASG theo lịch:** phải bảo trì instance, patch; nhiều overhead hơn.
- **D. Lưu trong EMR + QuickSight:** EMR tốn chi phí và công bảo trì hơn nhiều so với S3 + Athena.

#### So sánh tầng ứng dụng

| Phương án | Quản lý server? | Scale |
|---|---|---|
| **C. S3+CloudFront+API GW+Lambda** | Không | Tự động |
| B. ECS + ALB + lịch | Có (nếu không Fargate) | Cấu hình + lên lịch |
| A. EC2 + ALB + lịch | Có | Cấu hình + lên lịch |

#### So sánh tầng dữ liệu

| Phương án | Chi phí/vận hành |
|---|---|
| **E. S3 + Athena + QuickSight** | Thấp, trả theo truy vấn |
| D. EMR | Cao hơn, phải quản lý cluster |

#### Quy tắc nhớ cho thi

- **Thấy "ÍT operational overhead, scale theo demand"** → **serverless** (S3 + CloudFront, API Gateway + Lambda)
- **Thấy "báo cáo cuối tháng trên dữ liệu trong S3"** → **Athena + QuickSight**
- **Thấy "schedule thêm capacity"** → dấu hiệu vận hành thủ công, không phải scale liền mạch
- **ECS không nhắc Fargate** → vẫn là quản lý instance

### TD explanation

Using serverless technologies is the best option to reduce the operational overhead. Therefore, using S3 with CloudFront for the front-end and API Gateway with Lambda for the back-end offers seamless scalability with low maintenance.
For the data storage layer S3 can again be used in combination with Athena and QuickSight. This meets the requirement of storing the data in a format the can be used to generate reports.
CORRECT:
"Deploy the application front end to an Amazon S3 bucket served by Amazon CloudFront. Deploy the application backend using Amazon API Gateway with an AWS Lambda proxy integration" is a correct answer.
CORRECT:
"Store the expense claim data in Amazon S3. Use Amazon Athena and Amazon QuickSight to generate the reports using Amazon S3 as the data source" is a correct answer.
INCORRECT:
"Deploy the application in a container using Amazon ECS behind an Application Load Balancer. Use Service Auto Scaling and schedule additional capacity ahead of peak usage periods" is incorrect. Amazon ECS requires instances to be managed (except when using Fargate which isn’t specified), so this option requires more operational overhead.
INCORRECT:
"Deploy the application to Amazon EC2 On-Demand Instances behind an Application Load Balancer. Use Amazon EC2 Auto Scaling and schedule additional capacity ahead of peak usage periods" is incorrect. Amazon EC2 requires instance maintenance so is another option that requires more operational overhead.
INCORRECT:
"Store the expense claim data in Amazon EMR. Use Amazon QuickSight to generate the reports using Amazon EMR as the data source" is incorrect. Amazon EMR can be used with QuickSight but storing data in EMR is going to be much more expensive and require more maintenance than using S3 with Athena.
References:
https://aws.amazon.com/quicksight/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

</details>

<a id="q27"></a>

## Q27

<!-- source: T3Q22 · domain: NEW -->



A university is running computational algorithms that require large amounts of compute power. The algorithms are being run using a high-performance compute cluster on Amazon EC2 Spot instances. Each time an instance launches a DNS record must be created in an Amazon Route 53 private hosted zone. When the instance is terminated the DNS record must be deleted.
The current configuration uses an Amazon CloudWatch Events rule that triggers an AWS Lambda function to create the DNS record. When scaling the solution to thousands of instances the university has experienced “HTTP 400 error (Bad request)” errors in the Lambda logs. The response header also includes a status code element with a value of "Throttling" and a status message element with a value of "Rate exceeded".
Which combination of steps should the Solutions Architect take to resolve these issues? (Select THREE.)

- **A.** Configure an Amazon SQS FIFO queue and configure a CloudWatch Events rule to use this queue as a target. Remove the Lambda target from the CloudWatch Events rule.
- **B.** Configure an Amazon Kinesis data stream and configure a CloudWatch Events rule to use this queue as a target. Remove the Lambda target from the CloudWatch Events rule.
- **C.** Update the CloudWatch Events rule to trigger on Amazon EC2 "Instance Launch Successful" and "Instance Terminate Successful" events for the Auto Scaling group used by the cluster.
- **D.** Configure a Lambda function to retrieve messages from an Amazon SQS queue. Modify the Lambda function to retrieve a maximum of 10 messages then batch the messages by Amazon Route 53 API call type and submit. Delete the messages from the SQS queue after successful API calls.
- **E.** Configure an Amazon SQS standard queue and configure the existing CloudWatch Events rule to use this queue as a target. Remove the Lambda target from the CloudWatch Events rule.
- **F.** Configure a Lambda function to read data from the Amazon Kinesis data stream and configure the batch window to 5 minutes. Modify the function to make a single API call to Amazon Route 53 with all records read from the Kinesis data stream.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D, E · **You picked:** A, C, D

🔑 **Key words:** Route 53 API throttling from Lambda at thousands of Spot instances, buffering, select three

🪤 **Your trap:** Picked A (SQS FIFO): FIFO is not required here, ordering is irrelevant; a standard queue buffers the events. Rule intended is standard SQS as the target (E).

🧠 **Rule:** Route 53 API rate limit: buffer events in SQS (standard is enough), batch API calls from Lambda.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Spot instance launch/terminate ─► CloudWatch Events rule ─► Lambda ─► Route 53 API
                                                              │
                          Hàng nghìn instance ⇒ "HTTP 400 ... Throttling, Rate exceeded"
```

Throttle xảy ra ở **Route 53 API** (đề nêu giới hạn mặc định 5 request/giây/account), không phải ở Lambda. Giải pháp: đệm sự kiện vào queue rồi gom batch. Đáp án đúng: **C + D + E**. Anh chọn A, C, D: đúng C và D, sai A (thay vì E).

#### Ba bước ghép thành một giải pháp

- **C. Rule bắt "Instance Launch Successful" và "Instance Terminate Successful" của ASG:** chỉ bắt sự kiện thật sự cần tạo/xóa DNS.
- **E. SQS standard queue làm target của rule, gỡ Lambda target:** queue đệm sự kiện, không gọi Route 53 trực tiếp theo từng instance.
- **D. Lambda đọc queue, lấy tối đa 10 message, gom theo loại Route 53 API call rồi gửi, xóa message khi API thành công:** giảm số request ra Route 53 để tránh throttle.

```
ASG events ─► EventBridge rule ─► SQS standard ─► Lambda (batch 10, gom theo API call) ─► Route 53
```

#### Vì sao A (SQS FIFO, anh chọn) sai

📝 Ghi chú kỹ thuật: đề viết FIFO "may not support the rate (up to 3,000 messages per second)". Theo audit, SQS FIFO ở chế độ high-throughput vượt con số 3,000 msg/s mà đề nêu, nên lý do "không đủ tốc độ" của vendor không chính xác. Lý do đúng để loại A: bài **không yêu cầu thứ tự hay khử trùng lặp nghiêm ngặt**, nên FIFO là thừa; **standard queue (E)** đủ và đơn giản hơn.

#### Các phương án còn lại

- **B/F. Kinesis Data Streams (+ batch window 5 phút):** đề coi đây là use case decoupling, SQS phù hợp hơn Kinesis (streaming).

#### So sánh

| Phương án | Vai trò | Kết luận |
|---|---|---|
| **E. SQS standard** | Đệm decoupling | Đúng, đủ dùng |
| A. SQS FIFO | Đệm có thứ tự | Thừa, đề không cần thứ tự |
| B/F. Kinesis | Streaming | Không phải lựa chọn tốt nhất cho decoupling |

#### Quy tắc nhớ cho thi

- **Thấy "Throttling / Rate exceeded" khi gọi API hạ nguồn** → **SQS đệm + Lambda xử lý batch**
- **Thấy "decoupling" đơn thuần** → **SQS standard**, FIFO chỉ khi cần thứ tự/exactly-once
- **Thấy "Route 53 API bị throttle"** → giảm số call bằng batch

### TD explanation

> ⚠️ SQS FIFO high-throughput mode exceeds the 3,000 msg/s figure quoted in the explanation.

The errors in the Lambda logs indicate that throttling is occurring. Throttling is intended to protect your resources and downstream applications. Though Lambda automatically scales to accommodate incoming traffic, functions can still be throttled for various reasons.
In this case it is most likely that the throttling is not occurring in Lambda itself but in API calls made to Amazon Route 53. In Route 53 you are limited (by default) to five requests per second per AWS account. If you submit more than five requests per second, Amazon Route 53 returns an HTTP 400 error (Bad request). The response header also includes a Code element with a value of Throttling and a Message element with a value of Rate exceeded.
The resolution here is to place the data for the DNS records into an SQS queue where they can buffer. AWS Lambda can then poll the queue and process the messages, making sure to batch the messages to reduce the likelihood of receiving more errors.
CORRECT:
"Update the CloudWatch Events rule to trigger on Amazon EC2 "Instance Launch Successful" and "Instance Terminate Successful" events for the Auto Scaling group used by the cluster" is a correct answer.
CORRECT:
"Configure a Lambda function to retrieve messages from an Amazon SQS queue. Modify the Lambda function to retrieve a maximum of 10 messages then batch the messages by Amazon Route 53 API call type and submit. Delete the messages from the SQS queue after successful API calls" is also a correct answer.
CORRECT:
"Configure an Amazon SQS standard queue and configure the existing CloudWatch Events rule to use this queue as a target. Remove the Lambda target from the CloudWatch Events rule" is also a correct answer.
INCORRECT:
"Configure an Amazon SQS FIFO queue and configure a CloudWatch Events rule to use this queue as a target. Remove the Lambda target from the CloudWatch Events rule" is incorrect. A FIFO queue is not necessary and may not support the rate of messages (up to 3,000 messages per second).
INCORRECT:
"Configure an Amazon Kinesis data stream and configure a CloudWatch Events rule to use this queue as a target. Remove the Lambda target from the CloudWatch Events rule" is incorrect. As this is a decoupling use case and SQS queue is a better fit.
INCORRECT:
"Configure a Lambda function to read data from the Amazon Kinesis data stream and configure the batch window to 5 minutes. Modify the function to make a single API call to Amazon Route 53 with all records read from the Kinesis data stream" is incorrect. For decoupling use cases SQS is a better fit than using Kinesis.
References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-compute-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-application-integration-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q37"></a>

## Q37

<!-- source: T4Q7 · domain: NEW -->



A Solutions Architect must enable an AWS CloudHSM M of N access control—also named a quorum authentication mechanism—to allow security officers to make administrative changes to a hardware security module (HSM). The new security policy states that at least two of the four security officers must authorize any administrative changes to CloudHSM. This is the first time this configuration has been setup. Which steps must be taken to enable quorum authentication (Select TWO.)

- **A.** Using the cloudhsm_mgmt_util command line tool, enable encrypted communication, login as a CO, and register a key for signing with the registerMofnPubKey command.
- **B.** Using the cloudhsm_mgmt_util command line tool, enable encrypted communication, login as a CO, and set the Quorum minimum value to two using the setMValue command.
- **C.** Using the cloudhsm_mgmt_util command line tool, enable encrypted communication, login as a CO, and get a Quorum token with the getToken command.
- **D.** Use AWS IAM to create a policy that requires a minimum of three crypto officers (COs) to configure the minimum number of approvals required to perform HSM user management operations.
- **E.** Edit the cloudhsm_client.cfg document to import a key and register the key for signing.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B · **You picked:** B, D

🔑 **Key words:** CloudHSM M of N quorum authentication first-time setup, two of four officers, select two

🪤 **Your trap:** Picked D (IAM policy): the quorum value is set inside the HSM by a CO, not in IAM. Missed registering the signing key with registerMofnPubKey (A).

🧠 **Rule:** CloudHSM quorum setup: CO registers signing keys, then sets M value in the HSM; token comes after setup.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
4 Crypto Officers (CO) trên CloudHSM
   Chính sách: cần >= 2 CO duyệt mọi thay đổi quản trị (M of N, M=2, N=4)
   Lần đầu thiết lập quorum authentication
   Chọn 2 bước
```

Đáp án đúng: **A (đăng ký signing key) + B (đặt Quorum minimum value)**. Anh chọn B đúng, sai ở D (IAM).

#### Hai bước đúng tạo thành một setup

```
Bước 1 (A): mỗi CO tạo signing key (asymmetric, ngoài HSM)
            → CO login, registerMofnPubKey để đăng ký public key lên HSM
Bước 2 (B): một CO login → setMValue = 2  (m value = số CO tối thiểu phải duyệt)
```

- **A** cần thiết vì quorum xác minh chữ ký của CO; HSM phải biết public key của từng CO.
- **B** đặt ngưỡng M. Theo giải thích: bất kỳ CO nào cũng đặt được m value, kể cả CO chưa đăng ký signing key.

#### Vì sao D (anh chọn) sai

D trông giống vì AWS thường dùng IAM policy để giới hạn quyền. Nhưng **quản trị user bên trong HSM** (CO, CU) là cơ chế của chính HSM, không đi qua IAM. IAM kiểm soát API của dịch vụ CloudHSM (tạo cluster, HSM) chứ không đặt quorum minimum value. Ngoài ra D nói "tối thiểu **ba** CO" trong khi chính sách yêu cầu **hai**.

#### Các phương án sai còn lại

- **C (getToken):** dùng **sau khi** quorum đã setup xong, khi CO cần token để thực thi thao tác cần quorum. Không phải bước thiết lập.
- **E (cloudhsm_client.cfg):** file cấu hình client (đồng bộ key phía client), không liên quan quorum authentication.

| Lệnh / thành phần | Vai trò | Thời điểm |
|---|---|---|
| **registerMofnPubKey** | Đăng ký signing public key của CO | Setup |
| **setMValue** | Đặt ngưỡng M tối thiểu | Setup |
| getToken | Lấy token để thực thi thao tác | Sau setup |
| IAM policy | Không đặt quorum | Không liên quan |

#### Lưu ý thực tế

> ⚠️ **cloudhsm_mgmt_util** là công cụ legacy; **CloudHSM CLI** là công cụ thay thế hiện tại.

📝 **Ghi chú kỹ thuật:** tên lệnh `registerMofnPubKey`, `setMValue`, `getToken` thuộc `cloudhsm_mgmt_util` mà đề dùng. Với CloudHSM CLI, khái niệm giữ nguyên (đăng ký signing key, đặt quorum value, dùng token) nhưng tên lệnh khác. Khi thi, đáp án theo đề, tức giữ A và B.

#### Quy tắc nhớ cho thi

- **Thấy "M of N / quorum" trên CloudHSM** → **đăng ký signing key** + **đặt m value**
- **Thấy "getToken"** → bước dùng **sau** setup, không phải setup
- **Thấy "IAM" cho user bên trong HSM** → sai; quản trị user HSM do HSM tự quản
- **Thấy "cloudhsm_client.cfg"** → cấu hình client, không phải quorum

### TD explanation

> ⚠️ cloudhsm_mgmt_util is legacy; the CloudHSM CLI replaces it.

The first time setup for M of N authentication involves creating and registering a key for signing and setting the minimum value on the HSM. This involves the following high-level steps:
• To use quorum authentication, each CO must create an asymmetric key for signing (a
signing key
). This is done outside of the HSM. Keys can be personal keys or public keys.
• A CO must log in to the HSM and then set the
quorum minimum value
, also known as the
m value
. This is the minimum number of CO approvals that are required to perform HSM user management operations. Any CO on the HSM can set the quorum minimum value, including COs that have not registered a key for signing.
CORRECT:
"Using the cloudhsm_mgmt_util command line tool, enable encrypted communication, login as a CO, and register a key for signing with the registerMofnPubKey command" is a correct answer.
CORRECT:
"Using the cloudhsm_mgmt_util command line tool, enable encrypted communication, login as a CO, and set the Quorum minimum value to two using the setMValue command" is a correct answer.
INCORRECT:
"Using the cloudhsm_mgmt_util command line tool, enable encrypted communication, login as a CO, and get a Quorum token with the getToken command" is incorrect. The getToken command is used by a CO to get a token after the quorum authentication has been setup successfully.
INCORRECT:
"Use AWS IAM to create a policy that requires a minimum of three crypto officers (COs) to configure the minimum number of approvals required to perform HSM user management operations" is incorrect. IAM is not used to configure the quorum minimum value.
INCORRECT:
"Edit the cloudhsm_client.cfg document to import a key and register the key for signing" is incorrect. This document is used for specifying client-side synchronization for keys and is not related to setting up quorum authentication.
References:
https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-authentication-crypto-officers.html#quorum-crypto-officers-use-token
https://docs.aws.amazon.com/cloudhsm/latest/userguide/quorum-authentication-crypto-officers-first-time-setup.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

</details>

<a id="q44"></a>

## Q44

<!-- source: T1Q29 · domain: CI · flagged -->



A company has deployed a SAML 2.0 federated identity solution with their on-premises identity provider (IdP) to authenticate users' access to the AWS environment. A Solutions Architect ran authentication tests through the federated identity web portal and access to the AWS environment was granted. When a test users attempt to authenticate through the federated identity web portal, they are not able to access the AWS environment.
Which items should the solutions architect check to ensure identity federation is properly configured? (Select THREE.)

- **A.** The IAM users are providing the time-based one-time password (TOTP) codes required for authenticated access.
- **B.** The IAM roles created for the federated users' or federated groups' trust policy have set the SAML provider as the principal.
- **C.** The IAM users permissions policy has allowed the sts:AssumeRoleWithSAML API action allowed in their permissions policy.
- **D.** The web portal calls the AWS STS AssumeRoleWithSAML API with the ARN of the SAML provider, the ARN of the IAM role, and the SAML assertion from IdP.
- **E.** The AWS STS service has the on-premises IdP configured as an event source for authentication requests.
- **F.** The company's IdP defines SAML assertions that properly map users or groups in the company to IAM roles with appropriate permissions.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D, F · **You picked:** B, C, D

🔑 **Key words:** SAML 2.0 federation fails for test users, what to check, select three

🪤 **Your trap:** Picked C (users' permission policy for AssumeRoleWithSAML): federated users are not IAM users; trust and mapping matter. Missed IdP assertions mapping users to roles (F).

🧠 **Rule:** SAML federation checks: role trust policy names SAML provider, IdP assertion maps to roles, portal calls AssumeRoleWithSAML.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
User ──► Federated web portal ──► IdP on-prem (xác thực OK, SAML assertion)
                                        │
                                        ▼
                    Portal gọi AWS STS AssumeRoleWithSAML
                    (ARN SAML provider + ARN role + SAML assertion)
                                        │
                                        ▼
                    Temporary credentials ──► AWS Console / API
Triệu chứng: IdP test OK nhưng user không vào được AWS. Chọn 3 thứ cần kiểm tra.
```

Đáp án đúng: **B + D + F**. Anh chọn B, D đúng; sai ở **C** (thiếu **F**).

#### Ba điểm cấu hình đúng, mỗi điểm ở một mắt xích

- **B (trust policy của role):** trong IAM role, trust policy đặt **SAML provider làm principal**. Đây là quan hệ tin cậy giữa tổ chức và AWS.
- **D (portal gọi API):** portal phải gọi `AssumeRoleWithSAML` với đủ ba tham số: ARN SAML provider, ARN role, SAML assertion.
- **F (assertion ở phía IdP):** IdP phải định nghĩa assertion map user/group trong công ty sang IAM role phù hợp. Thiếu map này, AWS không biết user được assume role nào.

#### Vì sao C (anh chọn) sai và F làm gì

C trông hợp lý vì "muốn gọi API thì cần quyền". Nhưng với SAML federation, người dùng **không phải IAM user**. Call `AssumeRoleWithSAML` không dùng AWS credentials; nó được xác thực bằng SAML assertion. Quyền nằm ở **role**: role phải cho phép federate qua SAML (trust policy, ý B), còn permissions policy của role quyết định user làm được gì sau khi assume. Đặt `sts:AssumeRoleWithSAML` vào permissions policy của "IAM user" là sai đối tượng.

F là mảnh anh thiếu: nó kiểm tra phía **IdP**, chỗ quyết định user nào ánh xạ vào role nào. Cấu hình chạy được cần cả hai phía tin nhau: AWS (B), IdP (F), cầu nối (D).

#### Các phương án sai còn lại

- **A (TOTP):** TOTP thuộc MFA của IAM user; giải pháp này không có MFA kiểu đó, và triệu chứng không nói tới MFA.
- **E (STS event source):** STS không có "event source" để cấu hình; đây là khái niệm của Lambda/EventBridge, không phải STS.

| Mắt xích | Đáp án | Kiểm tra gì |
|---|---|---|
| AWS (IAM role) | **B** | Trust policy: SAML provider là principal |
| Cầu nối (portal) | **D** | Gọi AssumeRoleWithSAML đủ 3 tham số |
| IdP | **F** | Assertion map user/group tới role |
| IAM user permission | C | Sai; không có IAM user trong luồng này |
| MFA / STS event | A, E | Không liên quan |

#### Lưu ý thực tế

- Khi debug SAML, lỗi thường gặp là role/provider ARN trong assertion không khớp với role trong IAM. Kiểm tra attribute `Role` mà IdP gửi.
- Đề này anh đã đánh dấu chưa chắc. Mẹo: nếu phương án nhắc "IAM users" trong luồng federation, nghi ngờ ngay, vì federation tồn tại để không cần IAM user.

#### Quy tắc nhớ cho thi

- **Thấy "SAML federation"** → 3 mắt xích: **trust policy (SAML provider principal)**, **AssumeRoleWithSAML**, **assertion map role**
- **Thấy "IAM users" trong federation** → thường sai
- **Thấy "STS event source"** → bịa, loại
- **Thấy "TOTP/MFA" khi đề không nhắc MFA** → loại

### TD explanation

AWS supports identity federation with SAML 2.0 (Security Assertion Markup Language 2.0), an open standard that many identity providers (IdPs) use. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without you having to create an IAM user for everyone in your organization.
In the diagram below the process of authentication is depicted in a situation where a client is authorized temporary access to an Amazon S3 bucket.
The correct answers are validated based on the following facts:
·
During step 4, the
client app calls the AWS STS
AssumeRoleWithSAML
API, passing the ARN of the SAML provider, the ARN of the role to assume, and the SAML assertion from IdP.
·
When configuring the IdP and AWS to trust each other,
in IAM, you create one or more IAM roles. In the role's trust policy, you set the SAML provider as the principal, which establishes a trust relationship between your organization and AWS. And…
·
In your organization's IdP, you define assertions that map users or groups in your organization to the IAM roles.
CORRECT:
"The IAM roles created for the federated users' or federated groups' trust policy have set the SAML provider as the principal" is a correct answer.
CORRECT:
"The web portal calls the AWS STS AssumeRoleWithSAML API with the ARN of the SAML provider, the ARN of the IAM role, and the SAML assertion from IdP" is also a correct answer.
CORRECT:
"The company's IdP defines SAML assertions that properly map users or groups in the company to IAM roles with appropriate permissions" is also a correct answer.
INCORRECT:
"The IAM users are providing the time-based one-time password (TOTP) codes required for authenticated access" is incorrect. TOTPs are used with multi-factor authentication which is not included in this solution.
INCORRECT:
"The IAM users permissions policy has allowed the sts:AssumeRoleWithSAML API action allowed in their permissions policy" is incorrect. Users need to have permissions to access the role; the role that is being assumed must be allowed to federate using SAML as it is the role that performs the sts:AssumeRoleWithSAML action.
INCORRECT:
"The AWS STS service has the on-premises IdP configured as an event source for authentication requests" is incorrect. It is not necessary to configure the AWS STS service with event sources.
References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

</details>

---

# Group C — Access & security design (no open ports, multi-AZ + WAF logging, cross-account write) (4)

<a id="q5"></a>

## Q5

<!-- source: T5Q29 · domain: CI -->



A start-up company has been using bastion hosts to connect to EC2 instances which are based on the latest Amazon Linux 2 AMI. They use these bastion hosts to SSH into EC2 instances to view logs and other troubleshooting activities.
So far, they have configured a VPC with private and public subnets, and a NAT gateway. Also, they have a Site-to-Site VPN for connectivity with the on-premises environment and EC2 security groups with direct SSH access from the on-premises environment
To increase security control and comply with auditing requirements around access to instances, which strategy should a solutions architect use?

- **A.** Install and configure EC2 Instance Connect on the fleet of EC2 instances. Remove all security group rules attached to EC2 instances that allow inbound TCP on port 22. Advise the engineers to remotely access the instances by using the EC2 Instance Connect CLI.
- **B.** Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's devices. Install the Amazon CloudWatch agent on all EC2 instances and send operating system audit logs to CloudWatch Logs.
- **C.** Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's devices. Enable AWS Config for EC2 security group resource changes. Enable AWS Firewall Manager and apply a security group policy that automatically remediates changes to rules.
- **D.** Create an IAM role with the AmazonSSMManagedInstanceCore managed policy attached. Attach the IAM role to all the EC2 instances. Remove all security group rules attached to the EC2 instances that allow inbound TCP on port 22. Have the engineers install the AWS Systems Manager Session Manager plugin for their devices and remotely access the instances by using the start-session API call from Systems Manager.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** bastion SSH replacement, auditing, increase security control, Amazon Linux 2, VPN

🪤 **Your trap:** Picked EC2 Instance Connect: it needs inbound port 22 reachable and gives weaker audit than Session Manager. Session Manager uses IAM role, no inbound ports, logged sessions.

🧠 **Rule:** Auditable access without open ports or bastions: SSM role + Session Manager; remove port 22 rules.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Engineer ──► bastion host ──► SSH (22) ──► EC2 (Amazon Linux 2, private)
              Site-to-Site VPN + SG mở 22 trực tiếp từ on-prem
        Yêu cầu: tăng kiểm soát bảo mật + tuân thủ AUDIT truy cập
```

Đáp án đúng: **D (Session Manager)**. Anh chọn A (EC2 Instance Connect).

#### Vì sao D đúng

- Session Manager cho truy cập an toàn và có thể audit **không cần mở inbound port, không bastion, không quản lý SSH key**.
- Cách làm: IAM role có `AmazonSSMManagedInstanceCore` gắn vào EC2 (instance profile), xóa rule inbound 22, engineer cài Session Manager plugin và dùng `start-session`.
- Amazon Linux 2 AMI đã có sẵn SSM Agent. Quyền truy cập do IAM kiểm soát, nên audit theo danh tính IAM.

#### Vì sao A (anh chọn) trông đúng nhưng sai

EC2 Instance Connect đẩy public key tạm thời qua API với quyền IAM, nghe gần giống D. Nhưng:
- Đề giải thích: phải cài trên từng instance, còn phải có SSH client và key phía engineer; số máy tăng thì quản lý key trở thành rủi ro.
- 📝 Ghi chú kỹ thuật: Instance Connect vẫn dùng giao thức SSH nên cần kết nối tới port 22. Phương án A vừa dùng Instance Connect vừa "xóa mọi rule inbound 22" là mâu thuẫn trong thực tế (trừ khi dùng thêm EC2 Instance Connect Endpoint, đề không nhắc). Đáp án đề vẫn là D.

#### Các phương án còn lại

- **B:** SG chỉ cho IP thiết bị engineer, thêm CloudWatch agent gửi OS audit log. SG gắn với IP từng máy, đổi người là phải sửa; đề không yêu cầu OS audit log.
- **C:** SG theo IP + AWS Config + Firewall Manager auto-remediate. Vẫn phụ thuộc IP thiết bị, quản lý firewall tập trung không phải trọng tâm.

#### So sánh

| Cách | Port 22 | Quản lý key | Danh tính audit |
|---|---|---|---|
| **D. Session Manager** | Đóng | Không | IAM |
| A. EC2 Instance Connect | Vẫn cần (SSH) | Key tạm, cần SSH client | IAM |
| B/C. SG theo IP | Mở theo IP | Key SSH | Khó theo người |

#### Quy tắc nhớ cho thi

- **Thấy "bastion host", "audit truy cập", "không mở port 22"** → **Systems Manager Session Manager**
- **Thấy "AmazonSSMManagedInstanceCore"** → instance profile cho SSM
- **Instance Connect vs Session Manager:** Instance Connect vẫn là SSH qua port 22; Session Manager thì không cần inbound
- **SG theo IP của từng thiết bị** → thường là đáp án sai

### TD explanation

Session Manager is a fully managed AWS Systems Manager capability. With Session Manager, you can manage your Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and virtual machines (VMs).
You can use either an interactive one-click browser-based shell or the AWS Command Line Interface (AWS CLI). Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.
To use Session Manager you must have the client installed, and this is installed by default on instances launched form the Amazon Linux 2 AMI, and you must have permissions to communicate with AWS Systems Manager. The permissions should be assigned using an IAM role attached using an instance profile.
CORRECT:
"Create an IAM role with the AmazonSSMManagedInstanceCore managed policy attached. Attach the IAM role to all the EC2 instances. Remove all security group rules attached to the EC2 instances that allow inbound TCP on port 22. Have the engineers install the AWS Systems Manager Session Manager plugin for their devices and remotely access the instances by using the start-session API call from Systems Manager" is the correct answer (as explained above.)
INCORRECT:
"Install and configure EC2 Instance Connect on the fleet of EC2 instances. Remove all security group rules attached to EC2 instances that allow inbound TCP on port 22. Advise the engineers to remotely access the instances by using the EC2 Instance Connect CLI" is incorrect.
With this option, you’d need to install Instance connect on each EC2 instance and SSH client with client & key on each of the machines intending to connect with instance.
If number of terminals increase, this would mean maintaining a lot of keys which could become a security risk, hence this is not an appropriate option in above scenario.
INCORRECT:
"Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's devices. Install the Amazon CloudWatch agent on all EC2 instances and send operating system audit logs to CloudWatch Logs" is incorrect.
Security groups should be generic in nature and not dependent on specific hosts. If engineers change within the team, security groups would require a change every time. Hence this is not a clean solution. Since audit logs requirement is not specified, this is not very relevant in this context.
INCORRECT:
"Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's devices. Enable AWS Config for EC2 security group resource changes. Enable AWS Firewall Manager and apply a security group policy that automatically remediates changes to rules" is incorrect.
Like above option, this would create dependency on engineer’s device and hence pose a security risk. Firewall rules are same to all instances in this case and centralized firewall management is not the intended solution here.
References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html
https://github.com/aws/session-manager-plugin
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-systems-manager/

</details>

<a id="q17"></a>

## Q17

<!-- source: T4Q10 · domain: CI -->



An application currently runs on Amazon EC2 instances in a single Availability Zone. A Solutions Architect has been asked to re-architect the solution to make it highly available and secure. The security team has requested that all inbound requests are filtered for common vulnerability attacks and all rejected requests must be sent to a third-party auditing application.
Which solution meets the high availability and security requirements?

- **A.** Configure a Multi-AZ Auto Scaling group using the application's AMI. Create an Application Load Balancer (ALB) and select the previously created Auto Scaling group as the target. Use Amazon Inspector to monitor traffic to the ALB and EC2 instances. Create a web ACL in WAF. Create an AWS WAF using the web ACL and ALB. Use an AWS Lambda function to frequently push the Amazon Inspector report to the third-party auditing application.
- **B.** Configure an Application Load Balancer (ALB) and add the EC2 instances as targets. Create a web ACL in WAF. Create an AWS WAF using the web ACL and ALB name and enable logging with Amazon CloudWatch Logs. Use an AWS Lambda function to frequently push the logs to the third-party auditing application.
- **C.** Configure an Application Load Balancer (ALB) along with a target group adding the EC2 instances as targets. Create an Amazon Kinesis Data Firehose with the destination of the third-party auditing application. Create a web ACL in WAF. Create an AWS WAF using the web ACL and ALB then enable logging by selecting the Kinesis Data Firehose as the destination. Subscribe to AWS Managed Rules in AWS Marketplace, choosing the WAF as the subscriber.
- **D.** Configure a Multi-AZ Auto Scaling group using the application's AMI. Create an Application Load Balancer (ALB) and select the previously created Auto Scaling group as the target. Create an Amazon Kinesis Data Firehose with a destination of the third-party auditing application. Create a web ACL in WAF. Create an AWS WAF using the WebACL and ALB then enable logging by selecting the Kinesis Data Firehose as the destination. Subscribe to AWS Managed Rules in AWS Marketplace, choosing the WAF as the subscriber.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** highly available EC2 app, filter common vulnerabilities, send rejected requests to third-party audit

🪤 **Your trap:** Picked B: ALB with instances but no multi-AZ Auto Scaling group, and WAF logs via CloudWatch plus Lambda polling. Needs multi-AZ ASG, managed rules, WAF logging to Firehose.

🧠 **Rule:** HA = multi-AZ Auto Scaling group; WAF logs go to Kinesis Data Firehose, which can deliver to third-party endpoints.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 một AZ ──► tái kiến trúc:
   1) High availability (Multi-AZ)
   2) Lọc request theo lỗ hổng phổ biến (WAF managed rules)
   3) Request bị chặn ──► gửi tới ứng dụng audit bên thứ ba
```

Đáp án đúng: **D**. Anh chọn B.

#### Vì sao D đúng

- **HA:** Multi-AZ Auto Scaling group làm target của ALB.
- **Lọc lỗ hổng phổ biến:** AWS WAF web ACL gắn vào ALB, subscribe **AWS Managed Rules** từ Marketplace.
- **Gửi dữ liệu request bị chặn:** bật WAF logging với **Kinesis Data Firehose** làm destination; Firehose hỗ trợ destination HTTP endpoint cũng như Datadog, New Relic, Splunk, nên đẩy được sang ứng dụng audit bên thứ ba.

```
Client ──► WAF (managed rules) ──► ALB ──► ASG Multi-AZ
              │ logging
              └──► Kinesis Data Firehose ──► third-party audit app
```

#### Vì sao B (anh chọn) sai

B có WAF + logging CloudWatch Logs + Lambda đẩy log đi, nên phần bảo mật và audit nghe hợp lý. Lỗi nằm ở **HA**: B chỉ nói ALB với EC2 instances làm target, không có Multi-AZ Auto Scaling. Mẹo của đề: phương án không nhắc nhiều AZ thì loại ngay. Ngoài ra B tự dựng Lambda đẩy log định kỳ, kém trực tiếp hơn Firehose.

#### Các phương án còn lại

- **A:** có Multi-AZ ASG, nhưng dùng Amazon Inspector cho dữ liệu request bị chặn. Inspector đánh giá mức phơi nhiễm/lỗ hổng của instance, không ghi log request, nên không đáp ứng yêu cầu audit rejected requests.
- **C:** có WAF + Firehose + Managed Rules, nhưng thiếu Multi-AZ nên không đạt HA.

#### So sánh

| | Multi-AZ ASG | WAF + Managed Rules | Log rejected request |
|---|---|---|---|
| **D** | Có | Có | Firehose tới audit app |
| A | Có | WAF (không managed rules) | Inspector (không ghi request) |
| B | Không | WAF | CloudWatch Logs + Lambda |
| C | Không | Có | Firehose |

#### Quy tắc nhớ cho thi

- **Thấy "high availability"** → tìm ngay chữ **Multi-AZ**; không có thì loại
- **Thấy "lọc common vulnerability"** → **AWS WAF + Managed Rules**
- **Thấy "đẩy WAF log sang bên thứ ba"** → **Kinesis Data Firehose**
- **Amazon Inspector** → đánh giá lỗ hổng, không phải log request
- Bốn đáp án gần giống nhau: gạch chân từ khóa khác nhau (Multi-AZ, Inspector, CloudWatch Logs vs Firehose).

### TD explanation

The high availability requirement can be easily met by ensuring the solution includes deploying EC2 instances across multiple AZs. Answers that don’t mention multiple AZs can be quickly eliminated.
For the security requirements, we must use AWS WAF to filter based on common vulnerabilities. An easy way to set this up is to subscribe to the AWS Managed Rules via the marketplace.
The requirement to send rejected request data to a third-party auditing application can be met by configuring logging in AWS WAF to Kinesis Data Firehose. The destination in Firehose can be configured as the third-party auditing application. Kinesis Firehose supports HTTP destinations as well as Datadog, New Relic, and Splunk.
CORRECT:
"Configure a Multi-AZ Auto Scaling group using the application's AMI. Create an Application Load Balancer (ALB) and select the previously created Auto Scaling group as the target. Create an Amazon Kinesis Data Firehose with a destination of the third-party auditing application. Create a web ACL in WAF. Create an AWS WAF using the WebACL and ALB then enable logging by selecting the Kinesis Data Firehose as the destination. Subscribe to AWS Managed Rules in AWS Marketplace, choosing the WAF as the subscriber" is the correct answer.
INCORRECT:
"Configure a Multi-AZ Auto Scaling group using the application's AMI. Create an Application Load Balancer (ALB) and select the previously created Auto Scaling group as the target. Use Amazon Inspector to monitor traffic to the ALB and EC2 instances. Create a web ACL in WAF. Create an AWS WAF using the web ACL and ALB. Use an AWS Lambda function to frequently push the Amazon Inspector report to the third-party auditing application" is incorrect.
Amazon Inspector can be used to assess instances for exposure; however, it does not actually log request data. Therefore, inspector cannot be used to send data about rejected requests to the third-party auditing application.
INCORRECT:
"Configure an Application Load Balancer (ALB) and add the EC2 instances as targets. Create a web ACL in WAF. Create an AWS WAF using the web ACL and ALB name and enable logging with Amazon CloudWatch Logs. Use an AWS Lambda function to frequently push the logs to the third-party auditing application" is incorrect.
This solution does not include high availability as there is no mention of adding the EC2 instances to multiple AZs.
INCORRECT:
"Configure an Application Load Balancer (ALB) along with a target group adding the EC2 instances as targets. Create an Amazon Kinesis Data Firehose with the destination of the third-party auditing application. Create a web ACL in WAF. Create an AWS WAF using the web ACL and ALB then enable logging by selecting the Kinesis Data Firehose as the destination. Subscribe to AWS Managed Rules in AWS Marketplace, choosing the WAF as the subscriber" is incorrect.
This solution does not include high availability as there is no mention of adding the EC2 instances to multiple AZs.
References:
https://docs.aws.amazon.com/waf/latest/developerguide/logging.html
https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-analytics-sap/

</details>

<a id="q53"></a>

## Q53

<!-- source: T2Q26 · domain: CI -->



A company currently manages a fleet of Amazon EC2 instances running Windows and Linux in public and private subnets. The operations team currently connects over the Internet to manage the instances as there is no connection to the corporate network.
Security groups have been updated to allow the RDP and SSH protocols from any source IPv4 address. There have been reports of malicious attempts to access the resources as the company wishes to implement the most secure solution for managing the instances.
Which strategy should a Solutions Architect recommend?

- **A.** Deploy a server on the corporate network that can be used for managing EC2 instances. Update the security groups to allow connections over SSH and RDP from the on-premises management server only.
- **B.** Deploy the AWS Systems Manager Agent on the EC2 instances. Access the EC2 instances using Session Manager restricting access to users with permission to manage the instances.
- **C.** Deploy a Linux bastion host with an Elastic IP address in the public subnet. Allow access to the bastion host from 0.0.0.0/0.
- **D.** Configure an IPSec Virtual Private Network (VPN) connecting the corporate network to the Amazon VPC. Update security groups to allow connections over SSH and RDP from the corporate network only.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** Windows and Linux EC2, RDP/SSH open to world, most secure management, no corporate connection

🪤 **Your trap:** Picked VPN with RDP/SSH open from corporate range: ports still open and weaker auditing. Session Manager needs no inbound ports and logs sessions.

🧠 **Rule:** Most secure instance admin: Session Manager with IAM permissions; no inbound RDP/SSH, no bastion.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:  Ops team ──Internet──► SG mở RDP/SSH từ 0.0.0.0/0 ──► EC2 (Windows + Linux)
                                  (public + private subnet, chưa có kết nối corporate)
Vấn đề: bị tấn công dò quét. Yêu cầu: cách quản lý instance AN TOÀN NHẤT
```

Đáp án đúng: **B (Systems Manager Session Manager)**. Anh chọn **D (Site-to-Site VPN)**.

#### Vì sao B đúng

Session Manager cho shell tương tác (browser hoặc AWS CLI) mà **không cần mở inbound port**, không cần bastion host, không cần quản lý SSH key. Ngoài ra:

- Quyền truy cập do **IAM** kiểm soát (ai được mở session vào instance nào).
- Mọi session có thể ghi log để audit (access detail, command).
- Dùng được cho cả Windows và Linux, và instance ở private subnet.

Kết quả: có thể **đóng hẳn port 22/3389** trong security group.

#### Vì sao D (anh chọn) sai

D trông an toàn vì giới hạn nguồn là corporate network qua IPSec VPN, và đúng là tốt hơn nhiều so với 0.0.0.0/0. Nhưng đề hỏi "**most secure**": D vẫn để **SSH/RDP mở** trên instance, vẫn phải quản lý key/password, và không có kiểm soát/audit chi tiết như Session Manager. Ngoài ra, giả thiết đề cho là "chưa có kết nối corporate", nên D cần dựng thêm hạ tầng mạng.

#### Các phương án sai còn lại

- **A:** server quản lý on-prem vẫn cần mở SSH/RDP trên instance, và chưa có đường kết nối corporate tới VPC.
- **C:** bastion với EIP cho phép 0.0.0.0/0 giữ nguyên bề mặt tấn công; bastion chỉ tốt hơn nếu giới hạn IP, nhưng vẫn kém Session Manager.

| Cách | Port inbound | Quản lý key | Audit |
|---|---|---|---|
| **B. Session Manager** | Không cần | Không | Có (IAM + log) |
| D. VPN + SG giới hạn | Vẫn mở (từ corporate) | Có | Hạn chế |
| A. Server on-prem | Vẫn mở | Có | Hạn chế |
| C. Bastion 0.0.0.0/0 | Mở toàn cầu | Có | Hạn chế |

#### Lưu ý thực tế

- Để Session Manager hoạt động, instance cần **SSM Agent**, một **IAM instance profile** có quyền SSM, và đường ra tới endpoint của Systems Manager (qua Internet/NAT hoặc **VPC endpoint**). Instance ở private subnet không có NAT thì dùng VPC endpoint.
- Đề chỉ nói "deploy SSM Agent", cần nhớ phần quyền IAM đi kèm.

#### Quy tắc nhớ cho thi

- **Thấy "most secure" truy cập EC2 / bỏ SSH-RDP / bỏ bastion** → **Session Manager**
- **Thấy "không mở inbound port" + "audit"** → **Session Manager**
- **VPN/Direct Connect + SG hạn chế** → tốt, nhưng **không** bằng Session Manager khi đề nhấn "most secure"
- **Bastion 0.0.0.0/0** → tệ nhất

### TD explanation

The most secure option presented is to use AWS Systems Manager Session Manager. Session Manager is a fully managed AWS Systems Manager capability that lets you manage Amazon EC2 instances, on-premises instances, and virtual machines (VMs) through an interactive one-click browser-based shell or through the AWS Command Line Interface (AWS CLI).
Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys. Session Manager also makes it easy to comply with corporate policies that require controlled access to instances, strict security practices, and fully auditable logs with instance access details, while still providing end users with simple one-click cross-platform access to your managed instances.
CORRECT:
"Deploy the AWS Systems Manager Agent on the EC2 instances. Access the EC2 instances using Session Manager restricting access to users with permission to manage the instances" is the correct answer.
INCORRECT:
"Deploy a server on the corporate network that can be used for managing EC2 instances. Update the security groups to allow connections over SSH and RDP from the on-premises management server only" is incorrect. This is less secure compared to using session manager as the SSH and RDP ports must still be open on instances and it does not offer the robust controls offered by session manager.
INCORRECT:
"Deploy a Linux bastion host with an Elastic IP address in the public subnet. Allow access to the bastion host from 0.0.0.0/0" is incorrect. This is less secure compared to using session manager as the SSH and RDP ports must still be open on instances and it does not offer the robust controls offered by session manager. This solution could be better secured by restricting access to the corporate IP ranges.
INCORRECT:
"Configure an IPSec Virtual Private Network (VPN) connecting the corporate network to the Amazon VPC. Update security groups to allow connections over SSH and RDP from the corporate network only" is incorrect. This is less secure compared to using session manager as the SSH and RDP ports must still be open on instances and it does not offer the robust controls offered by session manager.
References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

</details>

<a id="q70"></a>

## Q70

<!-- source: T3Q4 · domain: ORG -->



An advertising company hosts static content in an Amazon S3 bucket that is served by Amazon CloudFront. The static content is generated programmatically from a Development account, and the S3 bucket and CloudFront are in a Production account. The build pipeline uploads the files to Amazon S3 using an IAM role in the Development Account. The S3 bucket has a bucket policy that only allows CloudFront to read objects using an origin access identity (OAI). During testing all attempts to upload objects using the to the S3 bucket are denied..
How can a Solutions Architect resolve this issue and allow the objects to be uploaded to Amazon S3?

- **A.** Modify the S3 upload process in the Development account to add the bucket-owner-full-control ACL to the objects at upload.
- **B.** Create a new cross-account IAM role in the Production account with write access to the S3 bucket. Modify the build pipeline to assume this role to upload the files to the Production Account.
- **C.** Modify the S3 upload process in the Development account to set the object owner to the Production Account.
- **D.** Create a new IAM role in the Development account with read access to the S3 bucket. Configure S3 to use this new role as its OAI. Modify the build pipeline to assume this role when uploading files from the Development Account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** Dev account pipeline upload to Prod S3 bucket, OAI-only policy, uploads denied

🪤 **Your trap:** Picked bucket-owner-full-control ACL: the bucket policy allows only the OAI, so Dev role is denied before any ACL applies. Needs a Prod-account role to write.

🧠 **Rule:** Cross-account S3 write when bucket only trusts OAI: assume a role in the bucket account.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Development account                    Production account
┌────────────────────┐                 ┌─────────────────────────────┐
│ Build pipeline     │ ──upload──✗──►  │ S3 bucket (bucket policy:   │
│ (IAM role dev)     │                 │  chỉ cho CloudFront OAI đọc)│──► CloudFront
└────────────────────┘                 └─────────────────────────────┘
Triệu chứng: mọi upload bị từ chối. Cần cho phép pipeline upload.
```

Đáp án đúng: **B (role cross-account trong Production, pipeline assume role)**. Anh chọn **A (bucket-owner-full-control ACL)**.

#### Vì sao B đúng

Bucket policy hiện chỉ cấp quyền **đọc** cho OAI, không có quyền ghi nào cho principal khác. Muốn upload, cần một danh tính được phép ghi. B tạo **IAM role trong Production** có quyền ghi vào bucket, pipeline ở Dev **assume role** đó (cross-account access). Khi đó đối tượng được ghi bởi một principal của chính Production account, nên **object thuộc Production** và không phát sinh vấn đề sở hữu.

#### Vì sao A (anh chọn) sai

A trông hợp lý vì `bucket-owner-full-control` là cách kinh điển để chủ bucket sở hữu quyền với object do account khác upload. Nhưng ACL đó chỉ xử lý **quyền trên object sau khi đã upload được**. Ở đây lỗi xảy ra **trước đó**: không có thứ gì cho phép role Dev ghi vào bucket (bucket policy không cấp quyền ghi cho nó). Thêm ACL vào request bị từ chối vẫn bị từ chối.

📝 **Ghi chú kỹ thuật:** lý do vendor nêu ("không thể thêm permission khi upload") không chính xác hoàn toàn, vì `PutObject` có hỗ trợ tham số ACL. Lý do đúng là ACL không thay thế cho việc cấp quyền ghi ban đầu. Ngoài ra bucket mới mặc định tắt ACL (bucket owner enforced), và cross-account cần cả identity policy phía Dev lẫn bucket policy phía Production cho phép. Đáp án B giữ nguyên.

#### Các phương án sai còn lại

- **C:** không thể đặt chủ sở hữu object thành Production chỉ bằng thao tác upload; quyền sở hữu do cấu hình bucket (Object Ownership) và danh tính ghi quyết định.
- **D:** OAI là danh tính đặc biệt của CloudFront, không gán cho role cross-account được; ngoài ra D chỉ cấp quyền **đọc**, không giúp upload.

| Phương án | Giải quyết "không có quyền ghi"? | Vấn đề |
|---|---|---|
| A. ACL bucket-owner-full-control | Không | Xử lý ownership, không cấp quyền ghi |
| **B. Role Production + assume** | Có | Không |
| C. Set owner khi upload | Không | Không làm được theo cách đó |
| D. Role Dev làm OAI | Không | OAI chỉ cho CloudFront, chỉ đọc |

#### Quy tắc nhớ cho thi

- **Thấy "OAI chỉ đọc" + cần upload** → danh tính khác có quyền ghi, không phải OAI
- **Thấy "upload cross-account bị denied"** → **assume role trong account chứa bucket**, hoặc bucket policy cấp cho principal
- **Thấy "bucket-owner-full-control"** → vấn đề ownership, không phải cấp quyền ghi
- **OAI** = cho CloudFront, không dùng cho role

### TD explanation

In the current configuration the S3 bucket will not allow any uploads. The only way to access the bucket is by using the OAI through CloudFront and this method only allows read access.
To be able to access the bucket directly and upload objects, a new IAM role can be created in the Production account with the necessary permissions to access the bucket. The role can then be assumed by the build pipeline using cross-account access.
The diagram below depicts how a user in one account can assume a role in a second account. In this case of the scenario in this question, rather than a user assuming the role a service principal can assume the role.
CORRECT:
"Create a new cross-account IAM role in the Production account with write access to the S3 bucket. Modify the build pipeline to assume this role to upload the files to the Production Account" is the correct answer.
INCORRECT:
"Create a new IAM role in the Development account with read access to the S3 bucket. Configure S3 to use this new role as its OAI. Modify the build pipeline to assume this role when uploading files from the Development Account" is incorrect. You cannot use a cross-account role for an OAI. An OAI is a special user account that is associated with a CloudFront distribution.
INCORRECT:
"Modify the S3 upload process in the Development account to add the bucket-owner-full-control ACL to the objects at upload" is incorrect. You cannot add permissions when uploading an object. The permissions must be previously specified on the bucket.
INCORRECT:
"Modify the S3 upload process in the Development account to set the object owner to the Production Account" is incorrect. You cannot modify bucket ownership as part of an object upload.
References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

</details>

---

# Group D — Service fit / hidden constraint (Lambda vs Fargate, Snowball tuning, DX carriers, licensing, PHZ association) (5)

<a id="q15"></a>

## Q15

<!-- source: T6Q32 · domain: MIG -->



A legacy application consists of a series of batch scripts that coordinate multiple application components. Each application component processes data within a few seconds before passing it on to the next component. The application has become complex and difficult to update. A Solutions Architect plans to migrate the application to the AWS Cloud. The application should be refactored into serverless microservices and be fully coordinated using cloud-native services.
Which approach meets these requirements most cost-effectively?

- **A.** Refactor the application onto Docker containers running on AWS Fargate. Use AWS Step Functions to orchestrate the application.
- **B.** Refactor the application onto AWS Lambda functions. Use AWS Step Functions to orchestrate the application.
- **C.** Refactor the application onto Docker containers running on Amazon ECS. Use Amazon SQS to decouple the application components.
- **D.** Refactor the application onto AWS Lambda functions. Use Amazon EventBridge to automate the application.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** batch scripts to serverless microservices, steps take seconds, most cost-effective, orchestrate

🪤 **Your trap:** Picked Fargate containers + Step Functions: serverless but costlier than Lambda for seconds-long steps. Lambda fits under the 15-minute limit; Step Functions orchestrates.

🧠 **Rule:** Short steps + serverless + orchestration: Lambda + Step Functions; Fargate costs more, EventBridge is not an orchestrator.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Batch scripts điều phối nhiều component ──► refactor thành
   serverless microservices + điều phối bằng cloud-native service
   Mỗi component xử lý chỉ vài GIÂY
   Yêu cầu: serverless + tiết kiệm chi phí NHẤT
```

Đáp án đúng: **B (Lambda + Step Functions)**. Anh chọn A (Fargate + Step Functions).

#### Vì sao B đúng

- Mỗi bước chỉ chạy vài giây, nằm xa giới hạn thời gian tối đa của Lambda (đề nêu 900 giây), nên Lambda hợp lý.
- Lambda tính tiền theo số lần gọi và thời gian chạy, không tốn khi nhàn rỗi.
- **Step Functions** điều phối các bước theo state machine, đúng nhu cầu "coordinate application components".

#### Vì sao A (anh chọn) gần đúng nhưng sai

Fargate cũng serverless và Step Functions đúng chỗ điều phối. Chỉ khác ở compute: đề giải thích Fargate nhiều khả năng đắt hơn Lambda. Với tác vụ ngắn vài giây, trả tiền cho container (vCPU/memory theo thời gian chạy task, cộng thời gian khởi động task) kém hiệu quả hơn Lambda.

#### Các phương án còn lại

- **C. ECS + SQS:** ECS (EC2 launch type) không phải serverless; SQS là decoupling, đề chỉ yêu cầu orchestration.
- **D. Lambda + EventBridge:** EventBridge phản ứng với sự kiện/trạng thái, không dùng để điều phối trình tự các component của một ứng dụng.

#### So sánh

| Phương án | Compute | Điều phối | Kết luận |
|---|---|---|---|
| **B** | Lambda | Step Functions | Rẻ nhất, serverless |
| A | Fargate | Step Functions | Serverless nhưng đắt hơn |
| C | ECS (EC2) | SQS | Không serverless |
| D | Lambda | EventBridge | Không phải orchestrator |

#### Lưu ý thực tế

- Lambda không hợp khi tác vụ chạy vượt giới hạn timeout hoặc cần container image lớn; lúc đó Fargate mới đáng cân nhắc.
- Step Functions là orchestrator (state machine); EventBridge là event bus; SQS là queue. Ba thứ khác vai trò.

#### Quy tắc nhớ cho thi

- **Thấy "tác vụ vài giây, serverless, rẻ nhất"** → **Lambda**, không phải Fargate
- **Thấy "coordinate/orchestrate các bước, workflow"** → **Step Functions**
- **Thấy "decoupling"** → SQS; **"phản ứng sự kiện"** → EventBridge

### TD explanation

The application components process data within a few seconds, and therefore can easily be migrated to AWS Lambda without hitting the maximum execution time (i.e. 900 seconds). The various Lambda functions can then be orchestrated using AWS Step Functions. This is the most cost-effective solution that meets the requirements.
CORRECT:
"Refactor the application onto AWS Lambda functions. Use AWS Step Functions to orchestrate the application" is the correct answer.
INCORRECT:
"Refactor the application onto Docker containers running on AWS Fargate. Use AWS Step Functions to orchestrate the application" is incorrect. AWS Fargate is a serverless service but it is likely to be more expensive in comparison to AWS Lambda.
INCORRECT:
"Refactor the application onto Docker containers running on Amazon ECS. Use Amazon SQS to decouple the application components" is incorrect. Amazon ECS (EC2 launch type) is not serverless. SQS is not needed here as there is no mention of decoupling, only orchestration.
INCORRECT:
"Refactor the application onto AWS Lambda functions. Use Amazon EventBridge to automate the application" is incorrect. EventBridge (CloudWatch Events) is used to respond to state changes in AWS infrastructure. It is not used for coordinating components of an application.
References:
https://aws.amazon.com/step-functions/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-application-integration-sap/

</details>

<a id="q55"></a>

## Q55

<!-- source: T2Q5 · domain: MIG -->



A company has an NFS file server on-premises with 50 TB of data that is being migrated to Amazon S3. The data is made up of many millions of small and files and a Snowball Edge device is being used for the migration. A shell script is being used to copy data using the file interface of the Snowball Edge device. Data transfer times are very slow and the Solutions Architect suspects this may be related to the overhead of encrypting all the small files and copying them over the network.
What change should be made to improve data transfer times?

- **A.** Cluster two Snowball Edge devices together to increase the throughput of the devices.
- **B.** Modify the shell script to ensure that individual files are being copied rather than directories.
- **C.** Perform multiple copy operations at one time by running each command from a separate terminal window, in separate instances of the Snowball client.
- **D.** Connect directly to the USB interface on the Snowball Edge device and copy the files locally.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** 50 TB millions of small files, Snowball Edge copy slow, encryption overhead

🪤 **Your trap:** Picked USB direct copy: Snowball Edge has no USB data interface. Intended speedup is parallel copy operations from separate Snowball client instances.

🧠 **Rule:** Snowball small-file speed: run multiple parallel copy commands, batch small files, copy directories.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
NFS server on-prem (50 TB, hàng triệu file NHỎ)
      │  shell script copy qua file interface
      ▼
Snowball Edge ──ship──► Amazon S3
Triệu chứng: chậm, nghi do overhead mã hóa từng file nhỏ + truyền qua mạng
```

Đáp án đúng: **C (chạy nhiều lệnh copy song song)**. Anh chọn **D (USB)**.

#### Vì sao C đúng

Theo hướng dẫn hiệu năng Snowball, các cách tăng tốc, xếp từ tác động lớn đến nhỏ:

1. Dùng Snowball client mới nhất (Mac/Linux)
2. Gom file nhỏ lại (batch)
3. **Thực hiện nhiều thao tác copy cùng lúc**
4. Copy từ nhiều workstation
5. Chuyển thư mục, không chuyển từng file

C chính là mục 3: chạy từng lệnh `snowball cp` trong các cửa sổ terminal riêng, mỗi cái một instance Snowball client, cùng kết nối tới một thiết bị. Với hàng triệu file nhỏ, overhead mỗi file là nút thắt; song song hóa che bớt overhead đó.

#### Vì sao D (anh chọn) sai

D trông hợp lý vì "cắm trực tiếp thì nhanh hơn qua mạng". Nhưng **Snowball Edge không có cổng USB** để copy. Thiết bị chỉ có các cổng mạng Ethernet SFP, QSFP, RJ45. Vì vậy mọi cách copy đều đi qua mạng; việc cần làm là tối ưu cách copy, không phải đổi cổng.

#### Các phương án sai còn lại

- **A (cluster hai thiết bị):** cluster của Snowball Edge phục vụ độ bền và tính sẵn sàng của dữ liệu lưu cục bộ, không phải tăng tốc độ copy.
- **B (copy file thay vì thư mục):** ngược với khuyến nghị; nên copy **thư mục**, không phải từng file riêng lẻ.

| Cách | Tác động | Đánh giá |
|---|---|---|
| Gom file nhỏ (batch) | Rất lớn | Tốt, nhưng không có trong lựa chọn |
| **C. Copy song song** | Lớn | Đúng |
| B. Copy từng file | Làm xấu đi | Sai |
| A. Cluster | Không tăng tốc copy | Sai |
| D. USB | Không tồn tại | Sai |

#### Lưu ý thực tế

> ⚠️ Giải thích vendor dựa trên quy trình Snowball client; dòng sản phẩm Snow Family đã đóng với khách hàng mới.

📝 **Ghi chú kỹ thuật:** đáp án C theo quy trình Snowball client như đề. Thực tế hiện nay, với khách hàng mới, nên cân nhắc **AWS DataSync** cho nhu cầu tương tự, và vẫn nên **gom file nhỏ** (batch) trước khi chuyển nếu có thể. Khi thi, giữ C.

#### Quy tắc nhớ cho thi

- **Thấy "Snowball chậm + nhiều file nhỏ"** → **copy song song** (nhiều terminal) và **gom file nhỏ**
- **Thấy "copy từng file"** → ngược, phải copy thư mục
- **Thấy "USB trên Snowball Edge"** → không tồn tại
- **Thấy "cluster để tăng throughput"** → sai; cluster là cho durability/HA

### TD explanation

> ⚠️ Snowball client workflow; Snow Family closed to new customers.

In general, you can improve the transfer speed from your data source to the Snowball in the following ways, ordered from largest to smallest positive impact on performance:
1. Use the latest Mac or Linux Snowball client
2. Batch small files together
3. Perform multiple copy operations at one time
4. Copy from multiple workstations
5. Transfer directories, not files
Option 3 entails performing multiple snowball cp commands at one time. You can do this by running each command from a separate terminal window, in separate instances of the Snowball client, all connected to the same Snowball.
CORRECT:
"Perform multiple copy operations at one time by running each command from a separate terminal window, in separate instances of the Snowball client" is the correct answer.
INCORRECT:
"Modify the shell script to ensure that individual files are being copied rather than directories" is incorrect. This is the opposite of what you should do to improve performance. Copy directories rather than individual files
INCORRECT:
"Connect directly to the USB interface on the Snowball Edge device and copy the files locally" is incorrect. The Snowball Edge device does not come with a USB interface. It has SFP, QSFP, and RJ45 connections for Ethernet networking.
INCORRECT:
"Cluster two Snowball Edge devices together to increase the throughput of the devices" is incorrect. You cannot cluster these devices for throughput.
References:
https://docs.aws.amazon.com/snowball/latest/ug/performance.html
https://docs.aws.amazon.com/snowball/latest/developer-guide/specifications.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-migration-sap/

</details>

<a id="q56"></a>

## Q56

<!-- source: T6Q20 · domain: ORG -->



A company has connected their on-premises data center to AWS using a single AWS Direct Connect (DX) connection using a private virtual interface. The company is hosting the front end for a business-critical application in an Amazon VPC. The back end is hosted on-premises and the company requires consistent, reliable, and redundant connectivity between the front end and back end of the application.
Which design would provide the MOST resilient connectivity between AWS and the on-premises data center?

- **A.** Use multiple IPSec VPN connections to separate virtual private gateways and configure BGP to prioritize the DX connection.
- **B.** Add an additional physical connection for the existing DX connection using the same network carrier and join the connections to a link aggregation group (LAG) on the same private virtual interface.
- **C.** Create an AWS Managed VPN connection that uses the public internet and attach it to the same virtual private gateway as the DX connection.
- **D.** Install a second DX connection from a different network carrier and attach it to the same virtual private gateway as the first DX connection.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** single Direct Connect private VIF, business-critical, most resilient connectivity

🪤 **Your trap:** Picked VPN to separate VGWs: internet VPN is a less reliable backup than a second DX. Second DX from a different carrier gives physical diversity; VGW is already redundant.

🧠 **Rule:** Most resilient hybrid link: second Direct Connect from a different carrier/location; VPN is a cheaper backup only.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem DC ══ 1 DX connection (private VIF) ══► VGW ──► VPC (front end)
                  ▲ single point of failure
Back end on-prem. Yêu cầu: kết nối ổn định, nhất quán, dự phòng — MOST resilient
```

Đáp án đúng: **D (DX thứ hai từ carrier khác, gắn cùng VGW)**. Anh chọn **A (nhiều VPN tới các VGW riêng)**.

#### Vì sao D đúng

Hai kết nối DX từ **hai carrier khác nhau** cho phép tách vật lý, loại bỏ điểm lỗi chung của đường cáp/carrier. VGW đã có dự phòng sẵn, nên hai DX cùng gắn một VGW là chấp nhận được. Đề ưu tiên "consistent, reliable", đúng thế mạnh của DX (đường riêng, không qua Internet).

#### Vì sao A (anh chọn) sai

A trông hợp lý vì VPN là phương án dự phòng kinh điển cho DX, và BGP ưu tiên DX khi DX còn sống. Nhưng:

1. VPN chạy trên **Internet public**, nên băng thông và độ trễ biến động, không đạt "consistent" khi DX chết.
2. "Nhiều VPN tới các VGW riêng" không khả thi theo cách đó: **một VPC chỉ gắn được một VGW**.

VPN dự phòng thường dùng khi ưu tiên chi phí; đề này đòi mức dự phòng cao nhất.

#### Các phương án sai còn lại

- **B (LAG cùng carrier):** LAG gom nhiều kết nối cùng location để tăng băng thông và chịu lỗi từng link, nhưng cùng carrier thì đường vật lý và thiết bị có thể chung; không loại bỏ điểm lỗi.
- **C (một VPN trên cùng VGW):** dùng Internet nên không đạt độ tin cậy yêu cầu; đề không nhắc chi phí nên DX thứ hai được ưu tiên.

| Phương án | Loại bỏ SPOF carrier/đường vật lý? | Đường truyền ổn định? |
|---|---|---|
| **D. DX thứ 2, carrier khác** | Có | Có (DX) |
| B. LAG cùng carrier | Không | Có |
| C. VPN backup | Có | Không (Internet) |
| A. Nhiều VPN, nhiều VGW | Không khả thi | Không |

#### Lưu ý thực tế

- Theo khuyến nghị resiliency của AWS, mức cao nhất là **các kết nối ở nhiều DX location** trên các thiết bị riêng. Đề chỉ yêu cầu chọn phương án tốt nhất trong danh sách, và D gần nhất.
- Giữ nguyên ý: VPN là backup rẻ, DX thứ hai là backup mạnh. Bảng chi phí nằm ngoài đề.

#### Quy tắc nhớ cho thi

- **Thấy "MOST resilient" + DX** → **DX thứ 2, location/carrier khác**
- **Thấy "consistent / reliable" network** → loại VPN Internet
- **Thấy "LAG"** → tăng băng thông / chịu lỗi link, **không** phải đa dạng carrier
- **Thấy "VPN backup cho DX"** → đáp án rẻ hơn, không phải resilient nhất

### TD explanation

Another DX connection should be established from a different carrier. This will provide physical separation and redundancy for the DX connections and is preferable to using the same carrier which could result in sharing the same physical pathways. The virtual private gateway has built in redundancy so sharing a VGW is acceptable.
CORRECT:
"Install a second DX connection from a different network carrier and attach it to the same virtual private gateway as the first DX connection" is the correct answer.
The diagram below depicts the most highly available and redundant configuration for Direct Connect with multiple DX locations, physical connections and data centers. Note the single points of failure that must be eliminated for maximum redundancy.
INCORRECT:
"Use multiple IPSec VPN connections to separate virtual private gateways and configure BGP to prioritize the DX connection" is incorrect. Separate DX links a preferable to using the internet for better reliability as the internet can be subject to various bandwidth and latency constraints.
INCORRECT:
"Add an additional physical connection for the existing DX connection using the same network carrier and join the connections to a link aggregation group (LAG) on the same private virtual interface" is incorrect. This does not provide as much redundancy as the same network carrier is used which means the physical pathways may be the same.
INCORRECT:
"Create an AWS Managed VPN connection that uses the public internet and attach it to the same virtual private gateway as the DX connection" is incorrect. Using the internet does not provide the reliability that the solution requires and cost is not mentioned so another DX connection is preferable.
References:
https://aws.amazon.com/directconnect/resiliency-recommendation/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q72"></a>

## Q72

<!-- source: T5Q4 · domain: MIG -->



A company has a line of business (LOB) application that is used for storing sales data for an eCommerce platform. The data is unstructured and stored in an Oracle database running on a single Amazon EC2 instance. The application front end consists of six EC2 instances in three Availability Zones (AZs). Each week the application receives bursts of traffic and application performance suffers. A Solutions Architect must design a solution to address scalability and reliability. The solutions should also eliminate licensing costs.
Which set of steps should the Solutions Architect take?

- **A.** Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce costs. Migrate the Oracle database into a single Amazon RDS reserved DB instance.
- **B.** Create an Auto Scaling group for the front end with a combination of Reserved instances and Spot Instances to reduce costs. Convert the tables in the Oracle database into Amazon DynamoDB tables.
- **C.** Create an Auto Scaling group for the front end with a combination of Reserved instances and Spot Instances to reduce costs. Migrate the Oracle database into an Amazon RDS multi-AZ deployment.
- **D.** Use Spot Instances for the front end to reduce costs. Convert the tables in the Oracle database into Amazon DynamoDB tables.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** Oracle on EC2, eliminate licensing costs, scalability and reliability, unstructured data

🪤 **Your trap:** Picked RDS Oracle Multi-AZ: still licensed Oracle, so licensing cost is not eliminated. Unstructured data moves to DynamoDB.

🧠 **Rule:** Eliminate Oracle licensing: move to open-source engine or DynamoDB; RDS Oracle keeps license cost.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Front end: 6 EC2 / 3 AZ           Burst hàng tuần → chậm
Database:  Oracle trên 1 EC2      Dữ liệu unstructured
Yêu cầu: scalability + reliability + LOẠI BỎ chi phí license
```

Đáp án đúng: **B (ASG Reserved + Spot, chuyển Oracle sang DynamoDB)**. Anh chọn **C (RDS Oracle Multi-AZ)**.

#### Vì sao B đúng

- **Front end:** ASG giải quyết burst. Là ứng dụng LOB dùng lâu dài nên **Reserved Instances** cho phần nền ổn định, **Spot** cho phần burst để giảm chi phí.
- **Database:** dữ liệu **unstructured** hợp NoSQL. **DynamoDB** scale tốt cho tải burst, có HA sẵn, và **không có phí license Oracle**. Có thể dùng AWS DMS (kèm SCT) để chuyển đổi và migrate.

#### Vì sao C (anh chọn) sai

C có ASG tốt và Multi-AZ tăng độ tin cậy, nhìn rất đúng. Nhưng yêu cầu rõ ràng là **loại bỏ licensing cost**: Oracle chạy trên RDS vẫn chịu license (license included hoặc bring your own). Multi-AZ chỉ tăng availability, không giải quyết license, và cũng không tăng khả năng scale cho tải burst. Chưa kể dữ liệu unstructured không cần engine relational Oracle.

#### Các phương án sai còn lại

- **A:** Oracle trên RDS vẫn có license, và **một** DB instance đơn không đáp ứng reliability.
- **D:** DynamoDB đúng hướng, nhưng front end chỉ dùng **Spot**: Spot có thể bị thu hồi, không tăng reliability.

| Phương án | Front end | Database | License bỏ được? |
|---|---|---|---|
| A | On-Demand + Spot | RDS Oracle đơn | Không |
| **B** | **Reserved + Spot** | **DynamoDB** | **Có** |
| C | Reserved + Spot | RDS Oracle Multi-AZ | Không |
| D | Chỉ Spot | DynamoDB | Có, nhưng front end không đáng tin |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** giải thích vendor thừa nhận không phải tính năng Oracle nào cũng chuyển sang DynamoDB được. Trong thực tế, nếu dữ liệu quan hệ cần SQL thì thường chọn **Aurora PostgreSQL/MySQL** (cũng hết license Oracle). Ở đề này chữ "unstructured" dẫn tới DynamoDB, nên giữ đáp án B.

#### Quy tắc nhớ cho thi

- **Thấy "eliminate licensing cost" + Oracle/SQL Server** → bỏ engine thương mại: **Aurora** hoặc **DynamoDB**, không phải RDS cùng engine
- **Thấy "unstructured data"** → **NoSQL / DynamoDB**
- **Thấy "Spot only" cho tầng cần reliable** → loại
- **Thấy "LOB lâu dài"** → **Reserved Instances** cho phần nền

### TD explanation

The front end can be served by a combination of reserved instances and spot instances to reduce cost. As this is a LOB application we can assume that it will be around for a long time so an RI is suitable.
For the database layer this can be migrated to DynamoDB. In the case of Oracle not all features are supported when migrating to DynamoDB but for hosting unstructured data and eliminating licensing costs this could be a good solution. AWS DMS can be used to migrate the database and convert the tables.
CORRECT:
"Create an Auto Scaling group for the front end with a combination of Reserved instances and Spot Instances to reduce costs. Convert the tables in the Oracle database into Amazon DynamoDB tables" is the correct answer.
INCORRECT:
"Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce costs. Migrate the Oracle database into a single Amazon RDS reserved DB instance" is incorrect. This will not eliminate the licensing costs as Oracle on RDS is still subject to licensing.
INCORRECT:
"Create an Auto Scaling group for the front end with a combination of Reserved instances and Spot Instances to reduce costs. Migrate the Oracle database into an Amazon RDS multi-AZ deployment" is incorrect. As above, Oracle on RDS does not eliminate licensing.
INCORRECT:
"Use Spot Instances for the front end to reduce costs. Convert the tables in the Oracle database into Amazon DynamoDB tables" is incorrect. Spot instances reduce cost but do not increase reliability as they are subject to termination of the maximum configured price is exceeded.
References:
https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-an-on-premises-oracle-database-or-amazon-rds-for-oracle-to-amazon-dynamodb-using-aws-dms-and-aws-sct.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-migration-sap/

</details>

<a id="q74"></a>

## Q74

<!-- source: T6Q31 · domain: ORG -->



A company which recently moved to AWS is trying to build a hybrid DNS solution. An AWS Direct Connect (DX) connection between the on-premises corporate network and an AWS Transit Gateway is established.
This solution will use an Amazon Route 53 private hosted zone for the domain internal.company.local for the resources stored within Amazon VPCs. The company has the following DNS resolution requirements:
· On-premises systems should be able to resolve and connect to internal.company.local.
· All VPCs should be able to resolve internal.company.local.
Which architecture should the company use to meet these requirements with the HIGHEST performance?

- **A.** Associate the private hosted zone to all the VPCs. Create a Route 53 inbound resolver in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for internal.company.local that point to the inbound resolver.
- **B.** Associate the private hosted zone to all the VPCs. Deploy an Amazon EC2 conditional forwarder in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for internal.company.local that point to the conditional forwarder.
- **C.** Associate the private hosted zone to the shared services VPC. Create a Route 53 outbound resolver in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for internal.company.local that point to the outbound resolver.
- **D.** Associate the private hosted zone to the shared services VPC. Create a Route 53 inbound resolver in the shared services VPC. Attach the shared services VPC to the transit gateway and create forwarding rules in the on- premises DNS server for internal.company.local that point to the inbound resolver.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** hybrid DNS, private hosted zone, on-premises and all VPCs resolve internal.company.local, highest performance

🪤 **Your trap:** Picked D: PHZ associated only to the shared services VPC, so other VPCs cannot resolve. Associate the PHZ with all VPCs and use inbound endpoint.

🧠 **Rule:** On-premises to PHZ = inbound resolver endpoint; PHZ must be associated with every VPC that should resolve it.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem DNS ══ DX ══► Transit Gateway ══► Shared services VPC (Route 53 Resolver endpoints)
                                     ╠══► VPC 1, VPC 2, ...
Zone: Route 53 PHZ  internal.company.local
Yêu cầu: (1) on-prem resolve được zone  (2) mọi VPC resolve được zone   — HIGHEST performance
```

Đáp án đúng: **A**. Anh chọn **D**.

#### Vì sao A đúng

A tách hai hướng truy vấn rõ ràng:

- **VPC resolve PHZ:** **associate PHZ với tất cả VPC**, mỗi VPC tự trả lời truy vấn qua Route 53 Resolver của nó, không qua hop trung gian. Đây là cách nhanh, ổn định, rẻ nhất.
- **On-prem resolve PHZ:** tạo **inbound resolver endpoint** trong shared services VPC; DNS on-prem đặt **forwarding rule** cho `internal.company.local` trỏ tới endpoint này. VPC được attach vào TGW để đường mạng thông.

#### Vì sao D (anh chọn) sai

D đúng một nửa: inbound resolver cho on-prem là đúng. Nhưng D chỉ associate PHZ với **shared services VPC**, nên các VPC khác không resolve được trực tiếp; muốn được phải thêm cơ chế forward (ví dụ outbound endpoint và rule), tức thêm hop, thêm chi phí và độ trễ. Điều đó trái với "HIGHEST performance". Hơn nữa D chỉ attach shared services VPC vào TGW.

#### Các phương án sai còn lại

- **B:** EC2 conditional forwarder cần tự vận hành, trả tiền, tự lo HA; Route 53 đã có inbound resolver managed.
- **C:** **outbound** resolver dùng cho VPC forward truy vấn ra ngoài (sang on-prem). On-prem cần đưa truy vấn **vào** AWS nên phải trỏ tới **inbound** endpoint.

| Phương án | PHZ associate | Endpoint cho on-prem | Vấn đề |
|---|---|---|---|
| **A** | Tất cả VPC | Inbound | Không |
| B | Tất cả VPC | EC2 forwarder | Tự vận hành, tốn phí |
| C | Chỉ shared VPC | Outbound | Sai hướng |
| D | Chỉ shared VPC | Inbound | VPC khác thêm hop, chậm hơn |

#### Lưu ý thực tế

> ⚠️ Giải thích vendor nhắc `cloud.example.com`, là sót từ một câu hỏi khác; lập luận còn lại đúng. Domain của đề này là `internal.company.local`.

- Nếu PHZ và VPC ở **account khác nhau**, cần tạo authorization (`CreateVPCAssociationAuthorization`) ở account chứa zone trước khi associate.

#### Quy tắc nhớ cho thi

- **Thấy "on-prem resolve tên AWS"** → **inbound endpoint**
- **Thấy "AWS resolve tên on-prem"** → **outbound endpoint + rule**
- **Thấy "PHZ cho nhiều VPC, performance"** → **associate PHZ trực tiếp với từng VPC**
- **Thấy "EC2 DNS forwarder"** khi có Route 53 Resolver → loại

### TD explanation

> ⚠️ Expl cites cloud.example.com, a leftover from another question; reasoning otherwise ok.

With an inbound Route 53 resolver the DNS servers in the on-premises network will forward queries for the custom domain name to the inbound resolver endpoint. The private hosted zone for cloud.example.com is associated with the VPC and will provide responses to DNS queries. For routing traffic, the VPCs must be attached to the transit gateway.
CORRECT:
"Associate the private hosted zone to all the VPCs. Create a Route 53 inbound resolver in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for internal.company.local that point to the inbound resolver" is the correct answer (as explained above.)
INCORRECT:
"Associate the private hosted zone to all the VPCs. Deploy an Amazon EC2 conditional forwarder in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for internal.company.local that point to the conditional forwarder" is incorrect.
Since Route 53 provides an inbound resolver, adding EC2 would add cost and extra effort.
INCORRECT:
"Associate the private hosted zone to the shared services VPC. Create a Route 53 outbound resolver in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for internal.company.local that point to the outbound resolver" is incorrect.
When associating on-premises DNS server, the inbound resolver needs to be added to the forwarding rules which acts as a destination for the traffic hence this is an incorrect option.
INCORRECT:
"Associate the private hosted zone to the shared services VPC. Create a Route 53 inbound resolver in the shared services VPC. Attach the shared services VPC to the transit gateway and create forwarding rules in the on- premises DNS server for internal.company.local that point to the inbound resolver" is incorrect.
Although it is possible to use forwarding rules to resolve private hosted zones in other VPCs, the most reliable, performant, and low-cost approach is to share and associate private hosted zones directly to all VPCs that need them.
References:
https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-dns-management-of-hybrid-cloud-with-amazon-route-53-and-aws-transit-gateway/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-route-53/

</details>
