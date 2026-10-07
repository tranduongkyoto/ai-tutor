# TD Set 2 — Correct Answer Review (43 questions)

Source: `TD_SAP_Review_Set2_Full.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/⚠️/🧠 are study notes. Wrong answers: `td_set_2_review.md`.

## Purpose

Confirm each correct answer was **knowledge, not a guess**. Answer again without looking; if you can't justify why every wrong option fails, tick **Guessed** and treat it as a wrong answer.

## ⚠️ Inconsistent concepts (right here, wrong elsewhere in this test)

| Right | Wrong | Concept |
|---|---|---|
| Q72, Q55 | Q15 | EC2/app access via IAM role / STS temporary credentials |
| Q57 | Q31 | SAML federation → AssumeRoleWithSAML |
| Q69, Q53 | Q44 | OAC vs signed URLs (path vs specific client) |
| Q65 | Q1 | ACM public certificates |
| Q11, Q13, Q46 | Q68, Q14 | Multi-AZ = HA, not DR / not RMAN |
| Q19 | Q75, Q66 | IAM policies with conditions grant access; SCPs don't |
| Q58, Q70 | Q24 | Streaming ingestion (Kinesis / Firehose) |

These are partial knowledge — review each pair together.

## Tracker

| Group | Q | Guessed? | Pass 1 | Pass 2 |
|---|---|---|---|---|
| A | [Q5](#q5) | ☐ | ☐ | ☐ |
| A | [Q19](#q19) | ☐ | ☐ | ☐ |
| A | [Q22](#q22) | ☐ | ☐ | ☐ |
| A | [Q35](#q35) | ☐ | ☐ | ☐ |
| A | [Q55](#q55) | ☐ | ☐ | ☐ |
| A | [Q57](#q57) | ☐ | ☐ | ☐ |
| A | [Q72](#q72) | ☐ | ☐ | ☐ |
| B | [Q6](#q6) | ☐ | ☐ | ☐ |
| B | [Q42](#q42) | ☐ | ☐ | ☐ |
| B | [Q53](#q53) | ☐ | ☐ | ☐ |
| B | [Q54](#q54) | ☐ | ☐ | ☐ |
| B | [Q65](#q65) | ☐ | ☐ | ☐ |
| B | [Q69](#q69) | ☐ | ☐ | ☐ |
| C | [Q10](#q10) | ☐ | ☐ | ☐ |
| C | [Q11](#q11) | ☐ | ☐ | ☐ |
| C | [Q13](#q13) | ☐ | ☐ | ☐ |
| C | [Q29](#q29) | ☐ | ☐ | ☐ |
| C | [Q46](#q46) | ☐ | ☐ | ☐ |
| C | [Q48](#q48) | ☐ | ☐ | ☐ |
| C | [Q63](#q63) | ☐ | ☐ | ☐ |
| D | [Q39](#q39) | ☐ | ☐ | ☐ |
| D | [Q51](#q51) | ☐ | ☐ | ☐ |
| D | [Q52](#q52) | ☐ | ☐ | ☐ |
| D | [Q61](#q61) | ☐ | ☐ | ☐ |
| D | [Q71](#q71) | ☐ | ☐ | ☐ |
| E | [Q8](#q8) | ☐ | ☐ | ☐ |
| E | [Q12](#q12) | ☐ | ☐ | ☐ |
| E | [Q20](#q20) | ☐ | ☐ | ☐ |
| E | [Q21](#q21) | ☐ | ☐ | ☐ |
| E | [Q30](#q30) | ☐ | ☐ | ☐ |
| E | [Q40](#q40) | ☐ | ☐ | ☐ |
| E | [Q47](#q47) | ☐ | ☐ | ☐ |
| E | [Q58](#q58) | ☐ | ☐ | ☐ |
| E | [Q64](#q64) | ☐ | ☐ | ☐ |
| E | [Q70](#q70) | ☐ | ☐ | ☐ |
| E | [Q73](#q73) | ☐ | ☐ | ☐ |
| E | [Q74](#q74) | ☐ | ☐ | ☐ |
| F | [Q4](#q4) | ☐ | ☐ | ☐ |
| F | [Q16](#q16) | ☐ | ☐ | ☐ |
| F | [Q25](#q25) | ☐ | ☐ | ☐ |
| F | [Q33](#q33) | ☐ | ☐ | ☐ |
| F | [Q36](#q36) | ☐ | ☐ | ☐ |
| F | [Q60](#q60) | ☐ | ☐ | ☐ |

---

# Group A — Identity, access & federation (7)

<a id="q5"></a>

## Q5

An analytics company plans to create a self-service solution that will provide a safe and cost-effective way for data scientists to access Amazon SageMaker AI on the company’s AWS accounts. The data scientists have limited knowledge of the AWS cloud, so the complex setup requirements for its ML models should not be exposed. The company wants the data scientists to be able to launch a Jupyter notebook instance if needed. The data at rest on the storage volume of the notebook instance must be encrypted with a preconfigured AWS KMS key.
Which of the following solutions will meet the company requirements with the LEAST amount of operational overhead?

- **A.** Create a self-service portal using AWS Proton and upload standardized service templates to Amazon S3. Add IAM permissions to the data scientist IAM group to use Proton. Write a custom AWS CLI script that will take input parameters from the data scientist for the requested Jupyter notebook instance with the pre-configured KMS key. Have the data scientists execute the script locally on their computers.
- **B.** Create an Amazon S3 bucket with website hosting enabled. Create a simple form as a front-end website hosted on the S3 bucket that allows the data scientist to input their request for Jupyter notebook creation. Send the request to an Amazon API Gateway that will invoke an AWS Lambda function with an IAM role permission to create the Jupyter notebook instance with a preconfigured KMS key. Have the Lambda function reply the URL of the notebook instance for display on the front-end website.
- **C.** Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. On the Outputs section of the CloudFormation template, reference the URL of the notebook instance. Rename this template to be more user-friendly and upload it to a shared Amazon S3 bucket for distribution to the data scientists.
- **D.** Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. Create Mappings on the CloudFormation to map simpler parameter names for instance sizes such as Small, Medium, Large. Reference the URL of the notebook instance on the Outputs section of the template. Create a portfolio in AWS Service Catalog and upload the template to be shared with the IAM role of the data scientists.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** self-service SageMaker notebooks; hide complexity; preconfigured KMS key

⚠️ **Watch:** Proton is for platform templates, not end-user self-service

🧠 **Rule:** Governed self-service launch → Service Catalog portfolio of CloudFormation products.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Data scientist (ít biết AWS)          AWS account công ty
┌─────────────────────┐               ┌──────────────────────────┐
│ Chỉ muốn bấm nút     │  self-service │ SageMaker Notebook        │
│ "tạo notebook"       │ ────────────► │ (KMS key preconfigured,   │
│ không muốn thấy       │               │  size: Small/Medium/Large)│
│ CloudFormation/CLI    │               └──────────────────────────┘
└─────────────────────┘
Yêu cầu: LEAST operational overhead, ẩn hết độ phức tạp setup
```

Đáp án đúng: **D — CloudFormation template + AWS Service Catalog portfolio**. Anh chọn đúng D.

#### Vì sao D đúng

```
CloudFormation template
  (AWS::SageMaker::NotebookInstance, KMS key preconfigured)
        │
        ▼
Mappings (Small/Medium/Large — ẩn tên instance type thật)
        │
        ▼
AWS Service Catalog Portfolio
        │ share với IAM role của data scientists
        ▼
Data scientist mở self-service portal → chọn size → bấm Launch
```

AWS Service Catalog sinh ra đúng cho bài toán này: team hạ tầng/an ninh đóng gói sẵn một "sản phẩm" CloudFormation đã cấu hình KMS key, rồi public nó qua portfolio cho end-user dùng qua portal tự phục vụ. Data scientist không cần biết CloudFormation là gì — chỉ thấy tham số đơn giản (Small/Medium/Large) nhờ phần Mappings. Đây chính là mẫu kiến trúc TD nhắc tới: "secured data science using Amazon SageMaker AI, AWS Service Catalog, and AWS KMS" — mã hóa storage volume được Service Catalog product ép dùng, không bao giờ lộ ra ngoài cho data scientist.

#### Vì sao từng đáp án sai bị loại

- **A — Proton + CLI script tự viết:** AWS Proton dùng để tạo self-service portal cho *platform templates* (hạ tầng chuẩn hoá cho dev team), không phải cơ chế end-user tự phục vụ sẵn có. Hơn nữa phải viết CLI script tùy biến và bắt data scientist tự chạy script trên máy họ — ngược hoàn toàn với "LEAST operational overhead" và "ẩn độ phức tạp".
- **B — S3 website + API Gateway + Lambda:** khả thi nhưng tốn công viết website, viết Lambda function đúng logic tạo resource, và quan trọng hơn: công ty có *nhiều account* nên phải lặp lại Lambda cho từng account — overhead nhân lên theo số account.
- **C — CFN template upload lên S3 cho user tự tải về:** user vẫn phải tự download template rồi tự upload vào console CloudFormation và tự điền tham số — không "self-service" đúng nghĩa, vẫn lộ chi tiết CloudFormation ra cho data scientist.

#### So sánh nhanh

| Lựa chọn | Ẩn độ phức tạp? | Multi-account overhead | Self-service thật? |
|---|---|---|---|
| **D. Service Catalog + CFN** | Có (Mappings) | Thấp — share portfolio | Có |
| C. CFN trên S3 | Không | Trung bình | Không (vẫn phải tự upload) |
| B. Website + Lambda | Không hẳn | Cao (per-account) | Có nhưng tốn công build |
| A. Proton + CLI script | Không | Cao (chạy local) | Không |

#### Lưu ý thực tế

- Service Catalog không tự nó "cấp phép" — vẫn cần IAM permission để user được dùng portfolio; đề bài mô tả đúng bước "share với IAM role của data scientists".
- KMS key preconfigured nằm sẵn trong CFN template nên user không bao giờ phải tự chọn/khai báo key — tránh cả lỗi cấu hình sai và lộ thông tin mã hóa.

#### Quy tắc nhớ cho thi

- **"Self-service, ẩn complexity, nhiều account, least overhead"** → **Service Catalog portfolio of CloudFormation products**
- **AWS Proton** → self-service cho *platform/infra templates* của dev team, không phải end-user launch resource đơn giản
- **"Upload template lên S3 cho người dùng tự tải"** → không tính là self-service thật

### TD explanation

AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage deployed IT services and your applications, resources, and metadata.
With AWS Service Catalog, you define your own catalog of AWS services and AWS Marketplace software and make them available for your organization. Then, end users can quickly discover and deploy IT services using a self-service portal.
Amazon SageMaker AI is a fully managed machine learning service. With SageMaker AI, data scientists and developers can quickly and easily build and train machine learning models and then directly deploy them into a production-ready hosted environment. It provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don’t have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. With native support for bring-your-own algorithms and frameworks, SageMaker AI offers flexible distributed training options that adjust to your specific workflows.
You can easily create a self-service, secured data science using Amazon SageMaker AI, AWS Service Catalog, and AWS Key Management Service (KMS). Using AWS Service Catalog, you can use a pre-configured AWS KMS key to encrypt data at rest on the machine learning (ML) storage volume that is attached to your notebook instance without ever exposing the complex, unnecessary details to data scientists. ML storage volume encryption is enforced by an AWS Service Catalog product that is pre-configured by centralized security and/or infrastructure teams.

Hence, the correct answer is: Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. Create Mappings on the CloudFormation to map simpler parameter names for instance sizes such as Small, Medium, Large. Reference the URL of the notebook instance on the Outputs section of the template. Create a portfolio in AWS Service Catalog and upload the template to be shared with the IAM role of the data scientists.
The option that says: Create an Amazon S3 bucket with website hosting enabled. Create a simple form as a front-end website hosted on the S3 bucket that allows the data scientist to input their request for Jupyter notebook creation. Send the request to an Amazon API Gateway that will invoke an AWS Lambda function with an IAM role permission to create the Jupyter notebook instance with a preconfigured KMS key. Have the Lambda function reply the URL of the notebook instance for display on the front-end website is incorrect. Although this is possible, this requires a lot of operational overhead as you need to write a custom website and write a proper Lambda function that has the appropriate code to create the needed resources. Additionally, as the company has several accounts, you will need to create the Lambda function for each AWS account.
The option that says: Write an AWS CloudFormation template that contains the AWS::SageMaker::NotebookInstance resource type to launch a Jupyter notebook instance with a preconfigured KMS key. On the Outputs section of the CloudFormation template, reference the URL of the notebook instance. Rename this template to be more user-friendly and upload it to a shared Amazon S3 bucket for distribution to the data scientists is incorrect. This is possible, however, it is not very user-friendly as the users need to download the appropriate CloudFormation template from Amazon S3 and then upload it to CloudFormation. They just need to input the needed parameters for the creation of their Jupyter notebook instance.
The option that says: Create a self-service portal using AWS Proton and upload standardized service templates to Amazon S3. Add IAM permissions to the data scientist IAM group to use Proton. Write a custom AWS CLI script that will take input parameters from the data scientist for the requested Jupyter notebook instance with the pre-configured KMS key. Have the data scientists execute the script locally on their computers is incorrect. You don’t have to write a custom AWS CLI script to take input parameters and run the script on the local machines. It is only possible to create a self-service portal using AWS Proton. You can use it to speed up the software development lifecycle with pre-approved templates for infrastructure.

References:
https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/
https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html

Check out these Amazon SageMaker AI and AWS Service Catalog Cheat Sheets:
https://tutorialsdojo.com/amazon-sagemaker/
https://tutorialsdojo.com/aws-service-catalog/

</details>

<a id="q19"></a>

## Q19

A pharmaceutical firm must securely store confidential experimental data. The company manages user authentication through AWS IAM Identity Center and has assigned its R&D scientists to a dedicated group.
The firm wants to consolidate all research documents into a shared Amazon S3 bucket while ensuring that each scientist can only access files they own. In addition, the company wants monthly audit reports detailing which users accessed which documents.
What combination of steps will satisfy these requirements? (Select TWO.)

- **A.** Create a custom IAM Identity Center role with a permission set granting access to the S3 bucket. Use an identity-based policy restricting data access to prefixes identified by each user’s tag, such as the ${aws:PrincipalTag/userNameID}/*condition.
- **B.** Use S3 Object Lock in Governance mode to prevent unauthorized research data modification. Use AWS Config rules to monitor and report on S3 object access patterns every week.
- **C.** Create an S3 Access Point for each scientist with a resource policy restricting access to objects with matching prefixes. Enable S3 Server Access Logging and use Amazon QuickSight to visualize access patterns.
- **D.** Turn on S3 server access logging and store the logs in an EMRFS (EMR File System ). Use Amazon Athena to query the EMRFS logs directly for monthly usage reporting.
- **E.** Enable AWS CloudTrail data event logging for the S3 bucket and store these logs in a separate bucket. Use Amazon Athena (with an Amazon Athena connector) to query the CloudTrail logs monthly and generate comprehensive user access reports.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E (you answered correctly)

🔑 **Key words:** Identity Center group; each scientist only own files; monthly access reports (Select TWO)

⚠️ **Watch:** Server access logs lack IAM identity detail; ⚠️ resource-level IAM conditions also decide Q75

🧠 **Rule:** Per-user prefix → ${aws:PrincipalTag/...} policy; who accessed what → CloudTrail data events + Athena.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IAM Identity Center group (R&D scientists)
        │
        ▼
S3 bucket chung (research documents)
   ├── scientist-1/*   ← chỉ scientist-1 đọc được
   ├── scientist-2/*   ← chỉ scientist-2 đọc được
   └── ...
        │
        ▼
Yêu cầu thêm: báo cáo HÀNG THÁNG ai đã truy cập file nào
```

Đáp án đúng (Select TWO): **A + E**. Anh chọn đúng cả hai.

#### Vì sao A đúng — IAM policy với condition tag là thứ THỰC SỰ cấp quyền

```
Identity-based policy gắn vào permission set của Identity Center role:

Resource: arn:aws:s3:::bucket/${aws:PrincipalTag/userNameID}/*
Effect: Allow
```

Đây là điểm mấu chốt: **IAM policy (có Condition dựa trên tag của principal) là công cụ GRANT quyền thực tế** — nó cho phép từng scientist chỉ đọc đúng prefix gắn với tag riêng của họ, dùng chính session từ IAM Identity Center. Không cần tạo bucket riêng, không cần Access Point riêng cho từng người — một policy dùng biến `${aws:PrincipalTag/...}` là đủ.

#### Vì sao E đúng — CloudTrail data events mới ghi được "ai, truy cập gì"

```
S3 bucket  → CloudTrail data event logging (object-level API) → log bucket riêng
                                                                      │
                                                                      ▼
                                                      Amazon Athena (Athena connector)
                                                                      │
                                                                      ▼
                                                      Monthly report: user X đã GetObject file Y lúc nào
```

CloudTrail data events ghi chi tiết **identity của caller** cho từng S3 API call (GetObject, PutObject...) — đúng loại thông tin "ai truy cập file nào" mà audit hàng tháng cần. Athena truy vấn trực tiếp log này bằng SQL, serverless, trả chính xác báo cáo yêu cầu.

#### Vì sao từng đáp án sai bị loại

- **B — S3 Object Lock Governance + AWS Config weekly:** Object Lock chỉ chống sửa/xoá dữ liệu, không liên quan access control theo từng user. AWS Config đánh giá compliance cấu hình resource, không sinh ra báo cáo "ai đã đọc file nào" — sai cả hai vế của yêu cầu.
- **C — S3 Access Point mỗi scientist + Server Access Logging + QuickSight:** Access Point riêng cho mỗi người có thể kiểm soát access nhưng cồng kềnh hơn một policy dùng tag; quan trọng hơn, **S3 Server Access Logging không có đủ chi tiết identity** để audit "ai" truy cập, và QuickSight là BI visualization chứ không phải công cụ audit report chi tiết.
- **D — Server access logging lưu vào EMRFS, query bằng Athena:** EMRFS là hệ thống file cho EMR, hoàn toàn không cần thiết ở đây — Athena query trực tiếp S3 log được, không phải đi qua EMRFS; lại dùng server access logging (thiếu chi tiết identity) thay vì CloudTrail data events.

#### So sánh nhanh

| Lựa chọn | Cấp quyền per-user? | Audit "ai truy cập gì"? |
|---|---|---|
| **A. IAM policy + tag condition** | Có (prefix theo tag) | — |
| **E. CloudTrail data events + Athena** | — | Có (identity-level) |
| C. Access Point + Server Access Logging + QuickSight | Có nhưng cồng kềnh | Không đủ chi tiết |
| B. Object Lock + Config | Không | Không |

#### ⚠️ Dễ nhầm

Mặt trái của bài học này: **IAM policy (identity-based, có Condition) GRANT quyền thật** — khác hẳn với SCP (Service Control Policy), vốn **không bao giờ grant quyền**, chỉ giới hạn trần quyền ở cấp account/OU. Ở Q75 và Q66 trong cùng bộ đề này, anh đã nhầm khi chọn đáp án dùng SCP để "authorize access cho một business unit/team cụ thể" — SCP không làm được việc đó, phải dùng IAM policy (như đúng cách Q19 này làm với tag condition).

#### Quy tắc nhớ cho thi

- **"Mỗi user chỉ truy cập file của chính mình, cùng một bucket"** → IAM policy với `${aws:PrincipalTag/...}` hoặc biến tương tự trên prefix
- **"Ai đã truy cập resource nào, khi nào"** → CloudTrail data events + Athena, không phải Server Access Logging hay AWS Config
- **"SCP authorizes/grants access cho một team"** → luôn SAI, SCP không grant; IAM policy mới grant

### TD explanation

AWS IAM Identity Center centralizes access management for various AWS accounts and applications. It provides single sign-on (SSO) access, enabling users to manage all their assigned accounts from a single location. Users can synchronize with an existing identity provider or create new users and groups directly within the service.
IAM Identity Center utilizes permission sets—collections of IAM policies—to manage user access across AWS Organizations. It includes a user-friendly AWS Access Portal for easy access to applications and supports deployment for both organization and account instances. Designed for high availability across multiple availability zones, the service ensures secure access through AWS Identity and Access Management (IAM) roles and policies.

CloudTrail data events are detailed records of resource operations in AWS services. They provide visibility into specific actions performed on or within a resource, such as Amazon S3 object-level API activity, Lambda function executions, or DynamoDB table operations.

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. It’s serverless, so there’s no infrastructure to manage, and you pay only for the queries you run.
Hence, the correct answers are:
– Create a custom IAM Identity Center role with a permission set granting access to the S3 bucket. Use an identity-based policy restricting data access to prefixes identified by each user’s tag, such as the ${aws:PrincipalTag/userNameID}/*condition. This approach uses the IAM Identity Center for authentication and leverages identity-based policies with user tags to restrict access to specific prefixes in the S3 bucket. This meets the requirement of ensuring each scientist can only access their own files.
– Enable AWS CloudTrail data event logging for the S3 bucket and store these logs in a separate bucket. Use Amazon Athena (with an Amazon Athena connector) to query the CloudTrail logs monthly and generate comprehensive user access reports. CloudTrail can log all data events (object-level API activity) in the S3 bucket, and Athena can be used to query these logs and generate detailed reports on user access patterns.
The option that says: Use S3 Object Lock in Governance mode to prevent unauthorized research data modification. Use AWS Config rules to monitor and report on S3 object access patterns every week is incorrect. While S3 Object Lock can typically prevent modifications, it doesn’t address the access control requirements. Additionally, AWS Config rules don’t provide detailed access reports as required.
The option that says: Create an S3 Access Point for each scientist with a resource policy restricting access to objects with matching prefixes. Enable S3 Server Access Logging and use Amazon QuickSight to visualize access patterns is incorrect. This option could only work for access control, it doesn’t provide the detailed monthly audit reports required. QuickSight is more suited for business intelligence than detailed access auditing.
The option that says: Turn on S3 server access logging and store the logs in an EMRFS (EMR File System ). Use Amazon Athena to query the EMRFS logs directly for monthly usage reporting is incorrect. While S3 server access logging can provide detailed logs, storing them in EMRFS is unnecessary and complicates the solution. Athena can query S3 logs directly without EMRFS.

References:
https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging-console.html
https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html

Check out the following Cheat Sheets:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/
https://tutorialsdojo.com/amazon-athena/
https://tutorialsdojo.com/aws-cloudtrail/

</details>

<a id="q22"></a>

## Q22

A company is using Microsoft Active Directory to manage all employee accounts and devices. The IT department instructed the solutions architect to implement a single sign-on feature to allow the employees to use their existing Windows account password to connect and use the various AWS resources. 
Which of the following options is the recommended way to extend the current Active Directory domain to AWS?

- **A.** Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.
- **B.** Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps' backend resources in AWS.
- **C.** Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account.
- **D.** Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** existing Windows AD passwords for AWS SSO

⚠️ **Watch:** Cognito is for customer-facing apps

🧠 **Rule:** Extend on-prem AD → AWS Managed Microsoft AD with trust relationship.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises Microsoft Active Directory
        │  employees login bằng password Windows hiện có
        ▼
   Trust relationship cần được thiết lập
        │
        ▼
AWS resources / Management Console / CLI
Yêu cầu: SSO dùng NGUYÊN mật khẩu Windows đang có, "recommended way to extend"
```

Đáp án đúng: **A — AWS Directory Service tích hợp AD hiện có qua trust relationship, enable SSO bằng Managed Microsoft AD**. Anh chọn đúng A.

#### Vì sao A đúng

```
On-prem AD domain  ◄──── trust relationship ────►  AWS Managed Microsoft AD
                                                      (AWS Directory Service)
                                                              │
                                                              ▼
                                            SSO vào AWS Management Console,
                                            AWS CLI, Windows-based workloads
```

Vì công ty **đã có sẵn Microsoft AD**, cách "recommended" đúng nghĩa là dùng **AWS Directory Service for Microsoft AD** để thiết lập secure Windows trust giữa AD on-premises và AWS Managed Microsoft AD domain trên cloud. Trust relationship này chính là cơ chế "extend domain hiện tại sang AWS" — không tạo thêm hệ thống authentication mới, employees dùng nguyên password Windows.

#### Vì sao từng đáp án sai bị loại

- **B — Amazon Cognito:** Cognito dành cho **customer-facing web/mobile app** (đăng nhập qua social identity provider như Facebook/Google), không phải giải pháp extend corporate AD cho nhân viên nội bộ.
- **C — IAM Identity Center + AWS Organizations:** chỉ dùng Identity Center *một mình* là không đủ — Identity Center vẫn cần tích hợp với AD thông qua AWS Directory Service ở bên dưới. Đề bài hỏi cách "extend AD domain", mà bước extend đó chính là AWS Directory Service, không phải Identity Center.
- **D — IAM Roles cross-account:** cross-account access dùng để chia sẻ resource giữa các AWS account khác nhau, không liên quan gì đến việc đồng bộ authentication với AD on-premises.

#### So sánh nhanh

| Lựa chọn | Giải quyết đúng "extend AD hiện có"? | Vai trò thực sự |
|---|---|---|
| **A. AWS Directory Service + trust** | Có | Cầu nối trust giữa on-prem AD và AWS |
| C. IAM Identity Center + Organizations | Không đủ một mình | SSO đa account, vẫn cần Directory Service bên dưới |
| B. Cognito | Không | Auth cho app khách hàng |
| D. IAM cross-account role | Không | Chia sẻ resource giữa account |

#### Lưu ý thực tế

- AWS Directory Service hỗ trợ cả hai mô hình: (1) standalone AWS Managed Microsoft AD, hoặc (2) kết nối tới AD on-premises có sẵn qua trust relationship — đề bài rơi vào trường hợp (2) vì công ty "đang dùng Microsoft Active Directory".
- IAM Identity Center có thể tích hợp AD **thông qua** AWS Directory Service — hai dịch vụ này bổ sung cho nhau, không thay thế nhau; nếu đề chỉ cho một lựa chọn "Identity Center alone" thì vẫn thiếu bước AD integration.

#### Quy tắc nhớ cho thi

- **"Công ty đã có Microsoft AD, muốn SSO bằng password hiện có"** → **AWS Directory Service + trust relationship**
- **"Customer-facing app, social login"** → Cognito, không phải Directory Service
- **"IAM Identity Center" xuất hiện một mình không kèm Directory Service** → thường là lựa chọn thiếu, vì Identity Center cần tích hợp AD qua Directory Service

### TD explanation

Because the company is using Microsoft Active Directory already, you can use AWS Directory Service for Microsoft AD to create secure Windows trusts between your on-premises Microsoft Active Directory domains and your AWS Microsoft AD domain in the AWS Cloud. By setting up a trust relationship, you can integrate SSO to the AWS Management Console and the AWS Command Line Interface (CLI), as well as your Windows-based workloads.

AWS Directory Service helps you to set up and run a standalone AWS Managed Microsoft AD directory hosted in the AWS Cloud. You can also use AWS Directory Service to connect your AWS resources with an existing on-premises Microsoft Active Directory. To configure AWS Directory Service to work with your on-premises Active Directory, you must first set up trust relationships to extend authentication from on-premises to the cloud.
Therefore, the correct answer is: Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.
The option that says: Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps’ backend resources in AWS is incorrect because Cognito is primarily used for federation to your web and mobile apps running on AWS. It allows you to authenticate users through social identity providers. But since the company is already using Microsoft AD, AWS Directory Service is the better choice here.
The option that says: Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts is incorrect because using the AWS IAM Identity Center service alone is not enough to meet the requirement. Although it can help you manage SSO access and user permissions across all your AWS accounts in AWS Organizations, you still have to use the AWS Directory Service to integrate your on-premises Microsoft AD. AWS IAM Identity Center integrates with Microsoft AD using AWS Directory Service so there is no need to create users and groups.
The option that says: Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account is incorrect because setting up cross-account access allows you to share resources in one AWS account with users in a different AWS account. Since the company is already using Microsoft AD then, the better choice to use here is the AWS Directory Service.

References:
https://aws.amazon.com/directoryservice/
https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-directory-connected.html

Check out this AWS Directory Service Cheat Sheet:
https://tutorialsdojo.com/aws-directory-service/

</details>

<a id="q35"></a>

## Q35

A financial startup offers flexible short-term loans of up to $5,000 to its users. Their online portal is hosted in AWS which uses S3 for scalable storage, DynamoDB as a NoSQL database, and a fleet of EC2 instances to host their web servers. To meet the financial regulation, the company is required to undergo a compliance audit. 
In this scenario, how will you provide the auditor access to the logs of your AWS resources?

- **A.** 1. Create an SNS Topic. 2. Configure the SNS to send out an email with the attached CloudTrail log files to the auditor’s email every time the CloudTrail delivers the logs to S3.
- **B.** 1. Enable CloudTrail logging to required AWS resources. 2. Create an IAM user with read-only permissions to the required AWS resources. 3. Provide the access credential to the auditor.
- **C.** 1. Contact AWS and inform them of the upcoming audit activities. 2. AWS will grant required access to the third-party auditor to see the logs.
- **D.** 1. Create an IAM role that has the required permissions for the auditor. 2. Attach the roles to the EC2, S3, and DynamoDB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** auditor needs log access

⚠️ **Watch:** Never call AWS to grant access

🧠 **Rule:** CloudTrail + least-privilege read-only IAM identity for the auditor.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS resources (S3, DynamoDB, EC2)
        │
        ▼
   AWS CloudTrail (ghi log mọi API call)
        │
        ▼
   Auditor bên ngoài cần XEM log để compliance audit
        │
Yêu cầu: cách an toàn, đúng chuẩn để cấp quyền xem log cho auditor
```

Đáp án đúng: **B — Enable CloudTrail + tạo IAM user read-only + đưa access credential cho auditor**. Anh chọn đúng B.

#### Vì sao B đúng

```
CloudTrail logging ON
      │
      ▼
IAM User (riêng cho auditor)
      │ policy: read-only trên các resource cần audit
      ▼
Access credential → đưa cho auditor
      │
      ▼
Auditor tự xem log trong S3 bucket, không cần ai hỗ trợ thủ công
```

Đây là mô hình chuẩn: CloudTrail tự động ghi lịch sử API call liên tục; việc còn lại chỉ là **cấp một identity least-privilege (read-only)** cho auditor để họ tự truy cập log — không cần công ty can thiệp gì thêm mỗi lần auditor cần xem.

#### Vì sao từng đáp án sai bị loại

- **A — SNS gửi email kèm file log mỗi khi CloudTrail delivery:** rủi ro bảo mật rõ ràng — log compliance nhạy cảm không nên gửi qua email đính kèm; nên giữ log trong S3 bucket và cấp read access trực tiếp thay vì phát tán qua email.
- **C — Liên hệ AWS để AWS tự cấp quyền cho auditor bên thứ ba:** không cần và không đúng quy trình — compliance audit không yêu cầu AWS phải "authorize" bên ngoài; AWS chỉ cần liên hệ trong trường hợp pentest, không phải audit log thông thường.
- **D — Tạo IAM role gán cho EC2/S3/DynamoDB:** IAM role ở đây gắn sai đối tượng — role nên gắn (hoặc identity tương đương) cho chính auditor, không phải attach vào các resource EC2/S3/DynamoDB; auditor cần một identity để đăng nhập/gọi API, không phải resource cần role.

#### So sánh nhanh

| Lựa chọn | Đúng cơ chế cấp quyền? | Rủi ro bảo mật |
|---|---|---|
| **B. IAM user read-only + CloudTrail** | Có | Thấp |
| A. SNS email log | Không cần thiết | Cao (lộ log qua email) |
| C. Liên hệ AWS cấp quyền | Sai quy trình | — |
| D. Role gắn vào EC2/S3/DynamoDB | Gắn sai đối tượng | — |

#### Lưu ý thực tế

- CloudTrail chỉ cần **enable logging to required resources** — không cần thiết lập gì đặc biệt để phục vụ audit, log tự được ghi liên tục vào S3.
- Nguyên tắc least privilege: credential cấp cho auditor chỉ nên có quyền **read-only** trên đúng phạm vi tài nguyên cần audit, không hơn.

#### Quy tắc nhớ cho thi

- **"Auditor cần xem log compliance"** → CloudTrail (đã ghi log) + IAM identity read-only, không cần gọi AWS hỗ trợ
- **"Gửi log qua email/SNS cho người ngoài"** → luôn là bẫy rủi ro bảo mật, loại ngay
- **"Liên hệ AWS để cấp quyền"** → chỉ đúng cho pentest, không đúng cho audit log thông thường

### TD explanation

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain events related to API calls across your AWS infrastructure. CloudTrail provides a history of AWS API calls for your account, including API calls made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This history simplifies security analysis, resource change tracking, and troubleshooting.

Therefore the correct answer is:
1. Enable CloudTrail logging to required AWS resources.
2. Create an IAM user with read-only permissions to the required AWS resources.
3. Provide the access credential to the auditor.
The following option is incorrect because you do not need to contact AWS for any audit activities since you can just use CloudTrail:
1. Contact AWS and inform them of the upcoming audit activities.
2. AWS will grant required access to the third-party auditor to see the logs.
You can contact AWS in case you will perform penetration testing to or originating from any of your AWS resources as part of the shared responsibility model, but for audit activities like this, an authorization is not required.
The following option is incorrect because it is a security risk to send the CloudTrail logs via email:
1. Create an SNS Topic.
2. Configure the SNS to send out an email with the attached CloudTrail log files to the auditor’s email every time the CloudTrail delivers the logs to S3.
It is best to keep them stored inside an S3 bucket and just provide read access to the bucket to the auditor.
The following option is incorrect because an IAM role should be attached to the IAM user of the auditor but the most preferred way to do this is still to use CloudTrail:
1. Create an IAM role that has the required permissions for the auditor.
2. Attach the roles to the EC2, S3, and DynamoDB.

References:
https://aws.amazon.com/cloudtrail/
https://aws.amazon.com/blogs/security/how-to-audit-cross-account-roles-using-aws-cloudtrail-and-amazon-cloudwatch-events/
https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html

Check out this AWS CloudTrail Cheat Sheet:
https://tutorialsdojo.com/aws-cloudtrail/

</details>

<a id="q55"></a>

## Q55

An advertising company plans to release a new photo-sharing app that will be hosted on the AWS Cloud. The app will store all pictures directly uploaded by users in a single Amazon S3 bucket, and users will also be able to view and download uploaded pictures directly from the S3 bucket. The company uses Amazon Fraud Detector to identify and prevent fraudulent account registrations and suspicious user activities at scale. The development team also uses AWS Device Farm to test the application on a wide range of real mobile devices before launch.
The solutions architect must ensure the security of the application, and it should be able to handle potentially millions of users in the most secure manner.
How should the solutions architect set up the user registration flow in AWS for this mobile app?

- **A.** Generate long-term credentials using AWS STS and apply the appropriate permissions. Store the credentials in the mobile app, and use them to access S3.
- **B.** Store user information in Amazon RDS and create an IAM Role with appropriate permissions. Generate new temporary credentials using the AWS Security Token Service AssumeRole function each time the user opens the mobile app. These credentials will be stored in the mobile app’s memory and will be used to access S3.
- **C.** Create an IAM user, assign appropriate permissions to it, and generate an access key and a secret key that will be stored in the mobile app and used to access S3.
- **D.** Create an IAM user and generate an access key and a secret key to be stored in the mobile app for the IAM user. After applying the appropriate permissions to the S3 bucket policy, use the generated credentials to access S3.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** millions of mobile users; most secure S3 access

⚠️ **Watch:** Never embed long-term access keys in an app

🧠 **Rule:** Mobile clients → temporary STS credentials (AssumeRole / Cognito).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile app (triệu users)
        │  upload/download ảnh
        ▼
Amazon S3 bucket
Yêu cầu: "millions of users", "most secure manner" cho user registration flow
```

Đáp án đúng: **B — IAM Role + STS AssumeRole sinh temporary credentials MỖI LẦN mở app, lưu trong memory app**. Anh chọn đúng B.

#### Vì sao B đúng

```
User mở app
      │
      ▼
App gọi STS AssumeRole (dùng IAM Role đã gán quyền S3)
      │
      ▼
Temporary credentials (access key + secret key + session token)
      │  lưu TRONG MEMORY app, không ghi ra file
      ▼
App dùng credentials này để upload/download ảnh trên S3
      │
Lần mở app tiếp theo → sinh credentials MỚI
```

Vì đây là mobile app public cho triệu người, **không bao giờ được nhúng credential tĩnh vào app** — mọi thiết bị cài app đều có thể bị decompile hoặc bị tấn công để lấy ra. STS AssumeRole giải quyết đúng vấn đề: mỗi lần app mở, sinh một bộ temporary credentials mới, có hạn dùng, không tồn tại lâu dài trên thiết bị.

#### Vì sao từng đáp án sai bị loại

- **A — "long-term credentials using AWS STS":** tự mâu thuẫn ngay trong câu chữ — STS sinh ra là để cấp **temporary** credentials, "long-term credentials từ STS" không đúng với bản chất dịch vụ và đi ngược yêu cầu "most secure" khi lưu credential dài hạn trong app.
- **C — IAM user + access/secret key tĩnh nhúng vào app:** đây chính là kiểu credential tĩnh nguy hiểm nhất — một khi app bị reverse-engineer, key này không bao giờ đổi, kẻ tấn công dùng vĩnh viễn.
- **D — Giống C nhưng thêm bucket policy:** vẫn là IAM user với key tĩnh nhúng trong app, bucket policy không giải quyết được vấn đề gốc là static credential bị lộ.

#### So sánh nhanh

| Lựa chọn | Loại credential | Vòng đời | An toàn cho app công khai? |
|---|---|---|---|
| **B. IAM Role + AssumeRole** | Temporary | Ngắn, sinh mới mỗi lần mở app | Có |
| A. "Long-term STS" | Mâu thuẫn khái niệm | Dài hạn | Không |
| C. IAM user key | Static | Vĩnh viễn | Không |
| D. IAM user key + bucket policy | Static | Vĩnh viễn | Không |

#### ⚠️ Dễ nhầm

Nguyên tắc "EC2/app → AWS resource = IAM Role, lấy temp credentials qua STS/instance metadata" cũng chính là chỗ anh từng vấp ở **Q15** trong bộ đề này: dù đã chọn đúng hướng IAM Role + instance profile, anh lại **thêm một bước thừa** (lưu ARN của role vào SSM Parameter Store) — trong khi instance profile một mình đã đủ, không cần cơ chế nào khác để "gán" role. Ở Q55 này anh đã áp dụng đúng và gọn: chỉ IAM Role + AssumeRole, không thêm bước phụ nào. Ghi nhớ: khi đã có IAM Role gắn đúng cơ chế (instance profile cho EC2, AssumeRole cho app/mobile), đừng tự thêm bước "lưu/truyền ARN" — đó là dấu hiệu over-engineering trong các câu hỏi dạng này.

#### Quy tắc nhớ cho thi

- **"Mobile app / nhiều user, cần S3 access an toàn nhất"** → IAM Role + STS AssumeRole, credentials tạm trong memory
- **"Long-term credentials" đi cùng STS** → mâu thuẫn, luôn là đáp án sai
- **IAM user + access/secret key nhúng trong app** → luôn là bẫy kém an toàn nhất trong các câu dạng này

### TD explanation

In this scenario, the best solution is to use a combination of an IAM Role and STS for authentication. The STS AssumeRole returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use AssumeRole for cross-account access or federation.

Therefore, the correct answer is: Store user information in Amazon RDS and create an IAM Role with appropriate permissions. Generate new temporary credentials using the AWS Security Token Service AssumeRole function each time the user opens the mobile app. These credentials will be stored in the mobile app’s memory and will be used to access S3. It creates an IAM Role with appropriate permissions and then generates temporary security credentials using STS AssumeRole. Then, it generates new credentials when the user runs the app the next time.
The option that says: Create an IAM user and generate an access key and a secret key to be stored in the mobile app for the IAM user. After applying the appropriate permissions to the S3 bucket policy, use the generated credentials to access S3 is incorrect. It simply suggests creating an IAM User, not the IAM Role, which is not a good solution. You should create an IAM Role so that the app can access the AWS Resource using STS AssumeRole.
The option that says: Generate long-term credentials using AWS STS and apply the appropriate permissions. Store the credentials in the mobile app, and use them to access S3 is incorrect. You should always grant short-term or temporary credentials for the mobile application. This option recommends creating long-term credentials.
The option that says: Create an IAM user, assign appropriate permissions to it, and generate an access key and a secret key that will be stored in the mobile app and used to access S3 is incorrect. It typically does not create the required IAM Role, but instead, an IAM user.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html
https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q57"></a>

## Q57

A company has an on-premises identity provider (IdP) used for authenticating employees. The Solutions Architect has created a SAML 2.0 based federated identity solution that integrates with the company IdP. This solution is used to authenticate users’ access to the AWS environment. Upon initial testing, the Solutions Architect has been successfully granted access to the AWS environment through the federated identity web portal. However, other test users who tried to authenticate through the federated identity web portal are not given access to the AWS environment.
Which of the following options must be checked to ensure the proper configuration of identity federation? (Select THREE.)

- **A.** Ensure that the ARN of the SAML provider, the ARN of the created IAM role, and SAML assertion from the IdP are all included when the federated identity web portal calls the AWS STS AssumeRoleWithSAML API.
- **B.** Ensure that the IAM policy for that user has “Allow” permissions to use SAML federation.
- **C.** Ensure that the trust policy of the IAM roles created for the federated users or groups has set the SAML provider as principal.
- **D.** Check the company’s IdP to ensure that the users are all part of the default AWSFederatedUser IAM group which is readily available in AWS.
- **E.** Ensure that the appropriate IAM roles are mapped to company users and groups in the IdP’s SAML assertions.
- **F.** Ensure that the resources on the AWS environment Amazon VPC can reach the on-premises IdP using its DNS hostname.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, E (you answered correctly)

🔑 **Key words:** SAML federation works for admin but not other users (Select THREE)

⚠️ **Watch:** ⚠️ Same SAML family you missed in Q31 — AssumeRoleWithSAML, not WebIdentity

🧠 **Rule:** Check AssumeRoleWithSAML params, role trust policy principal = SAML provider, role mapping in assertions.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises IdP (SAML 2.0)
      │ SAML assertion
      ▼
Federated identity web portal
      │ gọi STS AssumeRoleWithSAML
      ▼
AWS environment
      │
Solutions Architect: login OK      Other test users: KHÔNG vào được
Yêu cầu: kiểm tra config nào để sửa lỗi (Select THREE)
```

Đáp án đúng: **A, C, E**. Anh chọn đúng cả ba.

#### Vì sao A, C, E đúng — ba mảnh ghép bắt buộc của luồng AssumeRoleWithSAML

```
1) IAM role trust policy    → Principal = SAML provider      (C)
2) IdP's SAML assertion     → map user/group → đúng IAM role  (E)
3) Portal gọi STS           → AssumeRoleWithSAML(
                                 SAMLProviderArn,
                                 RoleArn,
                                 SAMLAssertion)                (A)
```

Ba điều kiện này phải đồng thời đúng mới federation chạy được cho MỌI user, không chỉ admin:
- **C** — trust policy của role phải set SAML provider làm Principal, đây là "cửa" cho phép AssumeRoleWithSAML được gọi thành công.
- **E** — IdP phải định nghĩa assertion mapping user/group ↔ IAM role; nếu user khác không được map đúng role trong assertion, họ sẽ không AssumeRole được dù trust policy đúng.
- **A** — client (portal) gọi API đúng cách: phải truyền đủ ARN của SAML provider, ARN của role, và SAML assertion — thiếu bất kỳ phần nào, STS từ chối.

Vì SA (admin) vào được còn user khác thì không, nhiều khả năng là role mapping trong SAML assertion của IdP (E) chưa đúng cho các user/group khác, hoặc trust policy/role tương ứng của họ chưa đúng — đây đúng là phạm vi 3 điểm cần check.

#### Vì sao từng đáp án sai bị loại

- **B — "IAM policy của user phải Allow SAML federation":** sai vì user ở đây không có IAM user — quyền của họ nằm trong **IAM role được map qua assertion**, không có "IAM policy riêng của test user" nào để kiểm tra; phải xem role policy, không phải user policy.
- **D — "users phải thuộc default AWSFederatedUser IAM group":** không tồn tại nhóm mặc định này trong AWS — bẫy tên nhóm giả.
- **F — "VPC resources phải reach được IdP qua DNS hostname":** không liên quan trực tiếp tới việc federation hoạt động hay không; đây không phải điều kiện bắt buộc của luồng SAML.

#### So sánh nhanh

| Thành phần cần đúng | Vai trò |
|---|---|
| **C. Trust policy = SAML provider** | Cho phép role được AssumeRoleWithSAML |
| **E. Role mapping trong SAML assertion** | Xác định user/group nào được role nào |
| **A. ARN SAML provider + ARN role + assertion khi gọi API** | Đảm bảo lời gọi AssumeRoleWithSAML hợp lệ |

#### ⚠️ Dễ nhầm

Đây cùng họ SAML federation với **Q31** mà anh từng chọn sai: ở Q31 bẫy là nhầm **AssumeRoleWithWebIdentity** (dành cho web identity provider như Google/Facebook) với luồng SAML doanh nghiệp đúng phải là **AssumeRoleWithSAML** (qua IAM Identity Center hoặc trực tiếp). Ở Q57, anh đã nhận diện đúng rằng mọi cấu hình xoay quanh AssumeRoleWithSAML — không lẫn sang WebIdentity. Ghi nhớ chắc: **SAML corporate IdP luôn đi với AssumeRoleWithSAML**, không bao giờ đi với AssumeRoleWithWebIdentity.

#### Quy tắc nhớ cho thi

- **SAML federation không hoạt động cho một số user** → kiểm tra trust policy (Principal = SAML provider), role mapping trong assertion, và tham số gọi AssumeRoleWithSAML
- **"SAML 2.0-compliant IdP"** → luôn gắn với **AssumeRoleWithSAML**, không phải AssumeRoleWithWebIdentity
- **"Default AWSFederatedUser group"** → không tồn tại, luôn là bẫy

### TD explanation

AWS supports identity federation with SAML 2.0 (Security Assertion Markup Language 2.0), an open standard that many identity providers (IdPs) use. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without having to create an IAM user for everyone in your organization. By using SAML, you can simplify the process of configuring federation with AWS because you can use the IdP’s service instead of writing custom identity proxy code.
IAM federation supports these use cases:
– Federated access allows a user or application in your organization to call AWS API operations. You use a SAML assertion (as part of the authentication response) that is generated in your organization to get temporary security credentials.
– Web-based single sign-on (SSO) to the AWS Management Console from your organization. Users can sign in to a portal in your organization hosted by a SAML 2.0–compatible IdP, select an option to go to AWS, and be redirected to the console without having to provide additional sign-in information. You can use a third-party SAML IdP to establish SSO access to the console or you can create a custom IdP to enable console access for your external users.

The diagram illustrates the following steps:

The user browses to your organization’s portal and selects the option to go to the AWS Management Console. In your organization, the portal is typically a function of your IdP that handles the exchange of trust between your organization and AWS.
The portal verifies the user’s identity in your organization.
The portal generates a SAML authentication response that includes assertions that identify the user and include attributes about the user. The portal sends this response to the client browser.
The client browser is redirected to the AWS IAM Identity Center endpoint and posts the SAML assertion.
The endpoint requests temporary security credentials on behalf of the user and creates a console sign-in URL that uses those credentials.
AWS sends the sign-in URL back to the client as a redirect.
The client browser is redirected to the AWS Management Console. If the SAML authentication response includes attributes that map to multiple IAM roles, the user is first prompted to select the role for accessing the console.

Before you can use SAML 2.0-based federation, you must configure your organization’s IdP and your AWS account to trust each other. Inside your organization, you must have an IdP that supports SAML 2.0, like Microsoft Active Directory Federation Service (AD FS, part of Windows Server), Shibboleth, or another compatible SAML 2.0 provider. In your organization’s IdP, you define assertions that map users or groups in your organization to the IAM roles. Note that different users and groups in your organization might map to different IAM roles. The exact steps for performing the mapping depend on what IdP you’re using.
The role or roles that you create in IAM define what federated users from your organization are allowed to do in AWS. When you create the trust policy for the role, you specify the SAML provider that you created earlier as the Principal. You can additionally scope the trust policy with a Condition element to allow only users that match certain SAML attributes to access the role.
Hence, the correct answers are:
– Ensure that the trust policy of the IAM roles created for the federated users or groups has set the SAML provider as principal. In IAM, you create one or more IAM roles for the federated users. In the role’s trust policy, you need to set the SAML provider as the principal, which establishes a trust relationship between your organization and AWS.
– Ensure that the ARN of the SAML provider, the ARN of the created IAM role, and SAML assertion from the IdP are all included when the federated identity web portal calls the AWS STS AssumeRoleWithSAML API. These items should all be passed by the client calling the AWS STS AssumeRoleWithSAML API.
– Ensure that the appropriate IAM roles are mapped to company users and groups in the IdP’s SAML assertions. In your organization’s IdP, you should define assertions that map users or groups in your organization to the IAM roles.
The option that says: Ensure that the IAM policy for that user has “Allow” permissions to use SAML federation is incorrect because the test user’s permissions are mapped to IAM roles, so we need to take a look at the IAM role policies and not the individual user IAM permission policies.
The option that says: Check the company’s IdP to ensure that the users are all part of the default AWSFederatedUser IAM group which is readily available in AWS is incorrect because there is no such thing as a default AWSFederatedUser IAM group. You only need to define assertions in your organization’s IdP that map users or groups in your organization to the IAM roles.
The option that says: Ensure that the resources on the AWS environment Amazon VPC can reach the on-premises IdP using its DNS hostname is incorrect as this is not primarily a requirement for the identity federation to work.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html
https://aws.amazon.com/blogs/security/how-to-set-up-federated-single-sign-on-to-aws-using-google-workspace/

Check out these AWS Security and Identity Services Cheat Sheet:
https://tutorialsdojo.com/aws-cheat-sheets-security-identity-services/

</details>

<a id="q72"></a>

## Q72

A company is planning to launch a mobile app for the Department of Transportation that allows government staff to upload the latest photos of ongoing construction works such as bridges, roads culverts, and dams all over the country. The mobile app should send the photos to a web server hosted on an EC2 instance which then adds a watermark to each photo that contains the project details and the date it was taken. The solutions architect must design a solution in which the photos generated by the server will be uploaded to an S3 bucket for durable storage. 
Which of the following solutions is a secure architecture and allows the EC2 instance to upload photos to S3?

- **A.** Set up a service control policy (SCP) with permissions to list and write objects to the S3 bucket. Attach the SCP to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket.
- **B.** Set up an IAM role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket.
- **C.** Set up an IAM user with permissions to list and write objects to the S3 bucket. Launch the instance as the IAM user which will enable the EC2 instance to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket.
- **D.** Set up an IAM service role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** EC2 watermarks photos then uploads to S3 securely

⚠️ **Watch:** ⚠️ Q15: the instance profile alone is enough

🧠 **Rule:** EC2 → S3 access = IAM role; credentials from instance metadata (not userdata).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile app               EC2 instance (web server)            S3 bucket
┌───────────┐            ┌───────────────────┐                ┌─────────┐
│ Upload ảnh│ ─────────► │ Thêm watermark,    │ ─────────────► │ Durable │
└───────────┘            │ rồi upload S3      │                │ storage │
                          └───────────────────┘                └─────────┘
Yêu cầu: kiến trúc BẢO MẬT cho phép EC2 upload ảnh lên S3
```

Đáp án đúng: **B — IAM Role gán cho EC2, lấy temporary credentials từ instance metadata**. Anh chọn đúng B.

#### Vì sao B đúng

```
IAM Role (permissions: s3:ListBucket, s3:PutObject)
      │
      ▼
Attach vào EC2 instance (instance profile)
      │
      ▼
App trên EC2 gọi instance metadata service
      │
      ▼
Temporary security credentials → upload ảnh lên S3
```

EC2 instance gọi AWS resource (S3) thì cách chuẩn và an toàn nhất luôn là **IAM Role** — không bao giờ nhúng credential tĩnh vào application code. Role gắn vào instance qua instance profile; mọi process chạy trên instance tự lấy được temporary credentials từ **instance metadata**, không cần quản lý key thủ công, credentials tự xoay vòng.

#### Vì sao từng đáp án sai bị loại

- **A — Service Control Policy (SCP) gắn vào EC2 instance:** sai cả về bản chất SCP — SCP chỉ hoạt động ở cấp **account/OU** trong AWS Organizations, nó giới hạn hành động được phép, **không grant quyền cho bất kỳ user/role nào**, và càng không thể "attach" trực tiếp vào một EC2 instance.
- **C — IAM user + launch instance "as the IAM user" + lấy credentials từ instance userdata:** sai hai lần — nên dùng IAM Role, không phải IAM user; và credentials phải lấy từ **instance metadata**, không phải userdata (userdata chỉ là script khởi tạo, không phải nơi lưu/lấy credentials).
- **D — IAM service role đúng nhưng lấy credentials từ instance userdata:** gần đúng (có dùng IAM Role) nhưng sai điểm mấu chốt — vẫn ghi "lấy từ userdata" thay vì metadata, nên vẫn bị loại.

#### So sánh nhanh

| Lựa chọn | Cơ chế cấp quyền | Nguồn lấy credentials | Đúng? |
|---|---|---|---|
| **B. IAM Role** | Instance profile | Instance metadata | Có |
| A. SCP | Không grant quyền | — | Không |
| C. IAM user | Launch as IAM user | Instance userdata | Không |
| D. IAM role | Instance profile | Instance userdata (sai) | Không |

#### ⚠️ Dễ nhầm

Nguyên tắc "EC2/app → S3 = IAM Role qua instance profile/metadata, không cần gì khác" chính là nơi anh từng vấp ở **Q15**: dù chọn đúng hướng IAM Role, anh lại thêm một bước thừa (lưu ARN role vào SSM Parameter Store) tưởng như "chắc chắn hơn" nhưng thực ra không cần thiết — instance profile một mình đã đủ để instance "mặc" role đó vào. Ở Q72 này anh làm đúng và gọn: chỉ IAM Role + instance metadata, không thêm cơ chế phụ. Ghi nhớ: câu hỏi IAM Role cho EC2 luôn chỉ cần **Role + instance profile + instance metadata** — bất kỳ bước "thêm" nào khác (SSM Parameter, userdata, SCP) đều là dấu hiệu sai hoặc dư thừa.

#### Quy tắc nhớ cho thi

- **"EC2 cần truy cập S3/AWS resource an toàn"** → IAM Role, credentials lấy từ **instance metadata**
- **"SCP attach vào EC2/instance"** → luôn sai, SCP chỉ hoạt động ở cấp account/OU và không grant quyền
- **"Credentials từ instance userdata"** → luôn sai, phải là instance **metadata**

### TD explanation

This question tests your understanding of IAM, specifically on when to use an IAM Role over an SCP. Since the server is running on an EC2 instance and the application makes requests to S3 to store the photos, the more suitable option to use here is an IAM Role.

In addition, don’t create an IAM user and pass the user’s credentials to the application or embed the credentials in the application. That will create a security risk because if an attacker had unauthorized access to that EC2 instance then the user credentials can easily be acquired and exploited. The better way is to create an IAM role that you can attach to the EC2 instance to give applications running on the instance temporary security credentials which can be used to access other AWS resources such as an S3 bucket. The credentials have the permissions specified in the policies attached to the role.
The option that says: Set up an IAM role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket is correct as it uses an IAM Role and fetches the temporary security credentials from the instance metadata.
The option that says: Set up a service control policy (SCP) with permissions to list and write objects to the S3 bucket. Attach the SCP to the EC2 instance which will enable it to retrieve temporary security credentials from the instance metadata and use that access to upload the photos to the S3 bucket is incorrect as SCPs simply enable you to restrict, at the account level of granularity, what services and actions the users, groups, and roles in those accounts can do. SCPs don’t grant permissions to any user or role because this is handled through IAM policies.
The option that says: Set up an IAM user with permissions to list and write objects to the S3 bucket. Launch the instance as the IAM user which will enable the EC2 instance to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket is incorrect as an IAM Role is a better option to use instead of an IAM User. Plus, you should always retrieve the temporary security credentials from the instance metadata and not from the user data.
The option that says: Set up an IAM service role with permissions to list and write objects to the S3 bucket. Attach the IAM role to the EC2 instance which will enable it to retrieve temporary security credentials from the instance userdata and use that access to upload the photos to the S3 bucket is incorrect because although it uses an IAM Role, the temporary security credentials should be retrieved from the instance metadata and not from the user data.

References:
https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-service-control-policy/
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-roles

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

Here is a deep dive on IAM Policies:
https://youtu.be/YQsK4MtsELU

</details>

---

# Group B — Edge & data protection (6)

<a id="q6"></a>

## Q6

A company has recently released a new mobile game. With the boost in marketing, the mobile game suddenly became viral. The registration webpage is bombarded with user registrations from around the world. The registration website is hosted on a fleet of Amazon EC2 instances created as an Auto Scaling group. This cluster is behind an Application Load Balancer to balance the user traffic. The website contains static content that is loaded differently depending on the user’s device type. With the sudden increase in user traffic, the fleet of Amazon EC2 instances experienced high CPU usage and users are reporting sluggishness on the website.
Which of the following options should the Solutions Architect implement to improve the website response time?

- **A.** Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Write a Lambda@Edge function to parse the User-Agent HTTP header and serve the appropriate contents based on the user’s device type.
- **B.** Use a Network Load Balancer (NLB) instead of an ALB to distribute the user traffic. Create a dedicated Auto Scaling group for the different device types. Configure the NLB to parse the User-Agent HTTP header to route the users to the appropriate EC2 Auto Scaling groups.
- **C.** Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Configure CloudFront to deliver different contents depending on the user’s User-Agent HTTP header.
- **D.** Create a dedicated Auto Scaling group for the different device types and create separate Application Load Balancers (ALB) for each group. Create an Amazon Route 53 entry to route the users to the appropriate ALB depending on their User-Agent HTTP header.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** viral signups; static content by device type; EC2 CPU high

⚠️ **Watch:** CloudFront can't natively route on full User-Agent logic

🧠 **Rule:** Offload static to S3 + CloudFront; Lambda@Edge to vary content by device.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile game viral → traffic đăng ký bùng nổ
        │
ALB ──► ASG EC2 (CPU cao, user bị sluggish)
        │
Website có static content theo device type (desktop/mobile/tablet...)
```

Yêu cầu: giảm tải cho EC2, cải thiện response time, mà vẫn phải phục vụ **nội dung static khác nhau theo User-Agent** của từng loại device. Đáp án đúng: **A** — đưa static content ra S3 + CloudFront, dùng **Lambda@Edge** để parse User-Agent và trả nội dung phù hợp. Anh chọn đúng A.

#### Vì sao A đúng

- **Tách static content ra S3**: EC2 không còn phải tự phục vụ ảnh/CSS/JS tĩnh → giảm hẳn CPU load, đúng với nguyên nhân gốc "EC2 CPU cao vì traffic viral".
- **CloudFront làm CDN phía trước S3**: cache tại edge, giảm số request chạm tới origin, cải thiện response time toàn cục.
- **Lambda@Edge**: chạy function tại edge location, đọc header `User-Agent` của viewer request, từ đó quyết định trả về nội dung nào (ảnh độ phân giải khác, layout khác...) theo device type — đúng yêu cầu "load khác nhau theo device type" mà đề đặt ra.
- Lambda@Edge tự scale từ vài request/ngày tới hàng nghìn request/giây, không cần quản lý server — phù hợp traffic viral tăng vọt bất ngờ.

#### Vì sao từng đáp án sai bị loại

- **B sai** vì Network Load Balancer hoạt động ở **Layer 4** (TCP) — không đọc được HTTP header như `User-Agent` nằm ở **Layer 7**. NLB không thể route theo nội dung header này.
- **C sai** vì tuy cũng dùng S3 + CloudFront, nhưng lại dựa vào việc **CloudFront cache theo giá trị header User-Agent** — AWS khuyến cáo **không nên làm vậy**: User-Agent có vô số giá trị khác nhau, cache theo nó khiến cache-hit-ratio giảm mạnh và CloudFront phải forward nhiều request hơn về origin, phản tác dụng với mục tiêu giảm tải.
- **D sai** vì **Route 53 không có khả năng routing dựa trên HTTP header** — Route 53 chỉ hoạt động ở tầng DNS (domain → IP), không đọc được nội dung request HTTP.

#### So sánh nhanh

| Đáp án | Cơ chế | Vấn đề |
|---|---|---|
| **A (đúng)** | S3 + CloudFront + Lambda@Edge đọc User-Agent | Không có |
| B | NLB cố đọc User-Agent | NLB là Layer 4, không đọc được header |
| C | CloudFront cache theo User-Agent | Cache-hit-ratio tệ, nhiều request hơn tới origin |
| D | Route 53 route theo header | Route 53 không đọc HTTP header |

#### Lưu ý thực tế

- Lambda@Edge chạy tại 4 điểm trong luồng CloudFront: viewer request, origin request, origin response, viewer response — dùng viewer request để đọc User-Agent sớm nhất và trả content phù hợp trước khi forward đi origin.
- Nếu không cấu hình cache theo header, CloudFront tự ghi đè `User-Agent: Amazon CloudFront` khi forward về origin — nên muốn xử lý theo device type phải làm ở Lambda@Edge, không thể trông chờ vào origin đọc header gốc.

#### Quy tắc nhớ cho thi

- **"Nội dung khác nhau theo thiết bị/User-Agent trên CloudFront"** → **Lambda@Edge**, không phải CloudFront cache-by-header
- **"Route/parse theo HTTP header"** → chỉ có thể làm ở Layer 7 (ALB rules hoặc Lambda@Edge), **không bao giờ** ở NLB hay Route 53
- **"Giảm tải EC2 do static content"** → tách ra **S3 + CloudFront**

### TD explanation

Lambda@Edge is an extension of AWS Lambda, a compute service that lets you execute functions that customize the content that CloudFront delivers. You can author Node.js or Python functions in one Region, US-East-1 (N. Virginia), and then execute them in AWS locations globally that are closer to the viewer, without provisioning or managing servers. Lambda@Edge scales automatically, from a few requests per day to thousands per second. Processing requests at AWS locations closer to the viewer instead of on origin servers significantly reduces latency and improves the user experience.

When you associate a CloudFront distribution with a Lambda@Edge function, CloudFront intercepts requests and responses at CloudFront edge locations. You can execute Lambda functions when the following CloudFront events occur:
– When CloudFront receives a request from a viewer (viewer request)
– Before CloudFront forwards a request to the origin (origin request)
– When CloudFront receives a response from the origin (origin response)
– Before CloudFront returns the response to the viewer (viewer response)
There are many uses for Lambda@Edge processing. For example:
– A Lambda function can inspect cookies and rewrite URLs so that users see different versions of a site for A/B testing.
– CloudFront can return different objects to viewers based on the device they’re using by checking the User-Agent header, which includes information about the devices. For example, CloudFront can return different images based on the screen size of their device. Similarly, the function could consider the value of the Referer header and cause CloudFront to return the images to bots that have the lowest available resolution.
– Or you could check cookies for other criteria. For example, on a retail website that sells clothing, if you use cookies to indicate which color a user chose for a jacket, a Lambda function can change the request so that CloudFront returns the image of a jacket in the selected color.
– A Lambda function can generate HTTP responses when CloudFront viewer request or origin request events occur.
– A function can inspect headers or authorization tokens, and insert a header to control access to your content before CloudFront forwards the request to your origin.
– A Lambda function can also make network calls to external resources to confirm user credentials, or fetch additional content to customize a response.
You can configure CloudFront to cache objects based on values in the User-Agent header, but AWS doesn’t recommend it. The User-Agent header has many possible values, and caching based on those values would cause CloudFront to forward significantly more requests to your origin. If you do not configure CloudFront to cache objects based on values in the User-Agent header, CloudFront adds a User-Agent header with the following value before it forwards a request to your origin: User-Agent = Amazon CloudFront.
Therefore, the correct answer is: Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Write a Lambda@Edge function to parse the User-Agent HTTP header and serve the appropriate contents based on the user’s device type. CloudFront will run the Lamda@Edge function for every request to serve the appropriate content to the user. This will lessen the load on the EC2 instances of the Auto Scaling group.
The option that says: Use a Network Load Balancer (NLB) instead of an ALB to distribute the user traffic. Create a dedicated Auto Scaling group for the different device types. Configure the NLB to parse the User-Agent HTTP header to route the users to the appropriate EC2 Auto Scaling groups is incorrect. An NLB operates at Layer 4 of the OSI network model so it can’t read the User-Agent HTTP header which is present at Layer 7.
The option that says: Create a dedicated Auto Scaling group for the different device types and create separate Application Load Balancers (ALB) for each group. Create an Amazon Route 53 entry to route the users to the appropriate ALB depending on their User-Agent HTTP header is incorrect. This is not possible because Amazon Route 53 does not have a way to direct users based on HTTP headers.
The option that says: Create an Amazon S3 bucket to host the static contents. Set this bucket as the origin for an Amazon CloudFront distribution. Configure CloudFront to deliver different contents depending on the user’s User-Agent HTTP header is incorrect. This may be possible as you can configure CloudFront to cache objects based on values in the Date and User-Agent headers, but AWS doesn’t recommend it. These headers have many possible values, and caching based on their values would cause CloudFront to forward significantly more requests to your origin.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-user-agent-header

Check out these AWS Lambda and Amazon CloudFront Cheat Sheets:
https://tutorialsdojo.com/aws-lambda/
https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q42"></a>

## Q42

A leading commercial bank has a hybrid cloud architecture and is using a Volume Gateway under the AWS Storage Gateway service to store their data via the Internet Small Computer Systems Interface (ISCSI). The security team has detected a series of replay attacks to your network, which is basically a form of network attack in which a valid data transmission is maliciously or fraudulently repeated or delayed. After their investigation, they detected that the originator of the attack is trying to intercept the data with an intention to re-transmit it, which is possibly part of a masquerade attack by IP packet substitution. 
As a Solutions Architect of the bank, how can you secure your AWS Storage Gateway from these types of attacks?

- **A.** Replace ISCSI with more secure protocols like Common Internet File System (CIFS) Protocol or Server Message Block (SMB).
- **B.** Replace the current ISCSI Block Interface with an ISCSI Virtual Tape Library Interface.
- **C.** Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate NFS connections and safeguard your network from replay attacks.
- **D.** Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSI and initiator connections.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** replay attacks on Volume Gateway iSCSI

⚠️ **Watch:** CHAP for NFS is wrong — CHAP applies to iSCSI

🧠 **Rule:** Secure iSCSI targets → CHAP authentication.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises ──iSCSI──► AWS Storage Gateway (Volume Gateway)
                              │
                     Bị replay attack: kẻ tấn công bắt data transmission
                     rồi re-transmit / giả mạo IP packet
```

Yêu cầu: chặn replay attack trên kết nối **iSCSI** của Volume Gateway. Đáp án đúng: **D** — dùng **CHAP (Challenge-Handshake Authentication Protocol)** để xác thực kết nối iSCSI và initiator. Anh chọn đúng D.

#### Vì sao D đúng

- Volume Gateway expose volume ra ngoài dưới dạng **iSCSI target**, client (initiator) kết nối vào bằng protocol iSCSI.
- **CHAP** là cơ chế xác thực được Storage Gateway hỗ trợ sẵn cho chính kết nối iSCSI đó — mỗi volume target có thể gán một hoặc nhiều cặp CHAP credentials.
- CHAP có cơ chế challenge-response (không truyền lại password/secret dạng cố định qua mạng mỗi lần), nên **chống được replay attack**: kẻ tấn công bắt được một transmission cũ không thể dùng lại để giả mạo kết nối mới.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì đổi sang **CIFS/SMB** không liên quan gì đến cơ chế chống replay attack — đây là đổi protocol file-sharing, không giải quyết vấn đề xác thực kết nối iSCSI.
- **B sai** vì đổi sang **iSCSI Virtual Tape Library (VTL) Interface** — VTL là interface dành cho **Tape Gateway**, không áp dụng cho Volume Gateway đang dùng trong bài.
- **C sai** vì CHAP được dùng để xác thực **iSCSI**, không phải **NFS**. NFS là protocol khác (dùng cho File Gateway), CHAP không áp dụng ở đó.

#### Lưu ý thực tế

- ⚠️ Trong bài, dễ nhầm giữa "CHAP cho NFS" (sai — C) và "CHAP cho iSCSI" (đúng — D): CHAP luôn gắn với iSCSI/initiator connections, không bao giờ với NFS.
- Volume Gateway dùng iSCSI block interface; Tape Gateway mới dùng iSCSI-VTL interface — hai loại gateway khác mục đích, không hoán đổi cơ chế bảo mật cho nhau.

#### Quy tắc nhớ cho thi

- **"Replay attack trên Volume Gateway / iSCSI"** → **CHAP authentication**
- **"CHAP"** → luôn gắn với **iSCSI**, tuyệt đối không phải NFS
- **"VTL interface"** → chỉ dành cho **Tape Gateway**, không phải Volume Gateway

### TD explanation

In AWS Storage Gateway, your iSCSI initiators connect to your volumes as iSCSI targets. Storage Gateway uses Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSI and initiator connections. CHAP provides protection against playback attacks by requiring authentication to access storage volume targets. For each volume target, you can define one or more CHAP credentials. You can view and edit these credentials for the different initiators in the Configure CHAP credentials dialog box.

Therefore the correct answer is: Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSl and initiator connections.
The option that says: Replace lSCSl with more secure protocols like Common Internet File System (CIFS) Protocol or Server Message Block (SMB) is incorrect. Replacing ISCSI with CIFS and SMB would be irrelevant since these two do not provide the required security mechanism in the scenario. It is best to use Challenge-Handshake Authentication Protocol (CHAP) instead.
The option that says: Replace the current lSCSl Block Interface with an lSCSl Virtual Tape Library Interface is incorrect. ISCSI Virtual Tape Library Interface is primarily used for Tape Gateways and not for Volume Gateways. It is better to use Challenge-Handshake Authentication Protocol (CHAP) instead.
The option that says: Configure a Challenge-Handshake Authentication Protocol (CHAP) to authenticate NFS connections and safeguard your network from replay attacks is incorrect. CHAP is primarily used to authenticate iSCSI and not NFS.

References:
https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedConfigureChap.html
https://docs.aws.amazon.com/storagegateway/latest/vgw/initiator-connection-common.html

Check out this AWS Storage Gateway Cheat Sheet:
https://tutorialsdojo.com/aws-storage-gateway/

</details>

<a id="q53"></a>

## Q53

A finance company plans to launch a new website to let users view tutorials promoting proper use of the mobile app. The website contains static media files stored in a private Amazon S3 bucket, while dynamic content is hosted on an AWS Fargate cluster. The Fargate tasks are accepting traffic behind an Application Load Balancer (ALB). To improve the user experience, static and dynamic content are served via an Amazon CloudFront distribution. An Amazon Route 53 Alias record has already been created to point the website URL to the CloudFront distribution. The company wants to ensure that access to both static and dynamic content is handled exclusively through CloudFront.
Which of the following options should the Solutions Architect implement to meet this requirement? (Select TWO.)

- **A.** Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution.
- **B.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer.
- **C.** Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC.
- **D.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution.
- **E.** Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C (you answered correctly)

🔑 **Key words:** static (S3) + dynamic (ALB) only via CloudFront (Select TWO)

⚠️ **Watch:** ⚠️ Q44: OAC enforces the CloudFront path, not a specific client

🧠 **Rule:** S3 origin → OAC; ALB origin → CloudFront custom header checked by WAF on the ALB.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                 CloudFront distribution
                 /                    \
   S3 (static media, private)    ALB ──► Fargate tasks (dynamic content)

Route 53 Alias record ──► CloudFront (đã đúng)
Yêu cầu: static VÀ dynamic đều chỉ truy cập được qua CloudFront (không đi tắt vào S3 hay ALB)
```

Chọn **HAI** giải pháp — một cho origin S3, một cho origin ALB. Đáp án đúng: **B (custom header + WAF trên ALB)** + **C (OAC cho S3)**. Anh chọn đúng B, C.

#### Vì sao B, C đúng

**C — origin S3:**
- Tạo **Origin Access Control (OAC)**, gắn vào CloudFront distribution, rồi set bucket policy của S3 chỉ cho phép access từ OAC đó.
- OAC dùng SigV4-signed request để CloudFront gọi S3 — ai request trực tiếp bằng S3 URL (không qua CloudFront, không có signature) sẽ bị từ chối.

**B — origin ALB (Fargate phía sau):**
- ALB không hỗ trợ cơ chế OAC như S3. Giải pháp tương đương là: CloudFront **thêm custom header** vào mọi origin request gửi tới ALB → gắn **AWS WAF web ACL** vào **ALB** với rule: request **không có custom header đó** thì bị deny.
- Vì chỉ CloudFront (được cấu hình thêm header) mới gửi request có header này, bất kỳ ai gọi trực tiếp vào ALB (bỏ qua CloudFront) sẽ bị WAF chặn ở tầng ALB.

Hai giải pháp này bổ sung cho nhau: một khóa đường vào S3, một khóa đường vào ALB — đúng yêu cầu "cả static và dynamic chỉ qua CloudFront".

#### Vì sao từng đáp án sai bị loại

- **D sai** vì web ACL lại gắn vào **CloudFront distribution** thay vì ALB. Request mới tới CloudFront chưa có custom header (CloudFront mới là bên *thêm* header rồi mới forward đi origin) → WAF trên CloudFront có thể chặn ngay cả request hợp lệ ban đầu từ user. Header chỉ tồn tại ở đoạn **CloudFront → origin**, nên WAF phải đặt ở phía origin (ALB), không phải phía CloudFront.
- **E sai** vì CloudFront **không có IP range cố định** — nếu set NACL chỉ cho phép IP của CloudFront, phải tự cập nhật liên tục theo AWS IP pool, không bền vững và dễ lỗi.
- **A sai** vì **S3 bucket ACL không có khả năng giới hạn truy cập chỉ từ CloudFront** — cơ chế đúng cho việc này là OAC + bucket policy, không phải ACL.

#### So sánh nhanh

| Origin | Cơ chế khóa | Đáp án |
|---|---|---|
| S3 (static) | OAC + bucket policy | **C (đúng)** |
| ALB (dynamic) | CloudFront custom header + WAF trên **ALB** | **B (đúng)** |
| ALB (dynamic) | WAF trên **CloudFront** (sai vị trí) | D (sai) |
| ALB (dynamic) | NACL theo IP CloudFront | E (sai — IP không cố định) |
| S3 (static) | Bucket ACL | A (sai — không hỗ trợ) |

#### Lưu ý thực tế

⚠️ Dễ nhầm: OAC chỉ đảm bảo request **đi qua đúng đường CloudFront**, chứ không giới hạn **ai** được dùng CloudFront URL đó (xem Q44 ở nhóm wrong-answer — OAC + HTTPS thôi không đủ để giới hạn "chỉ một client cụ thể"). Ở Q53 này, yêu cầu chỉ là "chỉ qua CloudFront" (không giới hạn client nào), nên OAC (cho S3) + custom header/WAF (cho ALB) là đủ — khác bài toán của Q44 cần thêm signed URL/cookie để giới hạn đúng một người dùng.

#### Quy tắc nhớ cho thi

- **"S3 origin chỉ truy cập qua CloudFront"** → **OAC** + bucket policy
- **"ALB/custom origin chỉ truy cập qua CloudFront"** → CloudFront thêm **custom header** + **WAF web ACL gắn vào ALB** (không gắn vào CloudFront)
- **"Giới hạn theo IP CloudFront"** → sai, vì CloudFront không có IP cố định

### TD explanation

AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the values of query strings or the IP addresses that requests originate from, CloudFront responds to requests either with the requested content or with an HTTP status code 403(Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked.
After you create an AWS WAF web access control list (web ACL), create or update a web distribution to associate the distribution with the web ACL. You can associate as many CloudFront distributions as you want with the same web ACL or with different web ACLs.
On Amazon CloudFront, you can control user access to your private content in two ways:

Restrict access to files in CloudFront caches.
Restrict access to files in your origin by doing one of the following:

– Set up an origin access control (OAC) for your Amazon S3 bucket.
– Configure custom headers for a private HTTP server (a custom origin).
CloudFront provides two ways to send authenticated requests to an Amazon S3 origin: origin access control (OAC) and origin access identity (OAI). OAC helps you secure your origins, such as Amazon S3.
AWS recommends that you use OAC instead because it supports the following features:

All Amazon S3 buckets in all AWS Regions, including opt-in Regions launched after December 2022
Amazon S3 server-side encryption with AWS KMS (SSE-KMS)
Dynamic requests (PUT and DELETE) to Amazon S3

Origin Access Identity (OAI) is considered a legacy, not-recommended mechanism due to its functional limitations.
You can secure the content in your Amazon S3 bucket so that users can access it through CloudFront, but cannot access it directly by using Amazon S3 URLs. This prevents someone from bypassing CloudFront and using the Amazon S3 URL to get content that you want to restrict access to. To require that users access your content through CloudFront URLs, you do the following tasks:

Create an origin access control and associate it with your CloudFront distribution.
Give the origin access control permission to read the files in your bucket.
Remove permission for anyone else to use Amazon S3 URLs to read the files.

If you use a custom origin, you can optionally set up custom headers to restrict access. For CloudFront to get your files from a custom origin, the files must be accessible by CloudFront using a standard HTTP (or HTTPS) request. But by using custom headers, you can further restrict access to your content so that users can access it only through CloudFront, not directly. This step isn’t required to use signed URLs, but it is recommended. To require that users access content through CloudFront, change the following settings in your CloudFront distributions:
Origin Custom Headers – Configure CloudFront to forward custom headers to your origin.
Viewer Protocol Policy – Configure your distribution to require viewers to use HTTPS to access CloudFront.
Origin Protocol Policy – Configure your distribution to require CloudFront to use the same protocol as viewers to forward requests to the origin.
Hence, the correct answers are:
– Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer. After you create an AWS WAF web access control list (web ACL), create or update a web distribution to associate the distribution with the ALB. Associating the Web ACL with the ALB ensures that only requests from CloudFront will reach the ALB. Any request going to the ALB without the custom header will be denied by WAF.
– Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC. OAC enables CloudFront to use SigV4-signed requests to access private S3 content, and the S3 bucket policy can explicitly allow access only from CloudFront via that OAC. This prevents users from retrieving objects directly from S3 and forces access through CloudFront.
The option that says: Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution is incorrect. If any new requests are going to CloudFront, they won’t have the custom header initially, so AWS WAF may block the request immediately. This could deny any new connections to CloudFront. Therefore, you need to associate the web ACL to the ALB, which is after CloudFront adds the custom header.
The option that says: Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets is incorrect. This will limit all resources inside the ALB subnets to accept only traffic from the CloudFront distribution. However, there are no fixed IP addresses for Amazon CloudFront, and if you manually add AWS IP addresses, you will have to update the NACL as AWS updates its IP pool.
The option that says: Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution is incorrect. You can’t directly configure a bucket ACL to allow access only from Amazon CloudFront. You typically need an origin access control (OAC) for this setup.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html
https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#forward-custom-headers-restrict-access

Check out these Amazon CloudFront and AWS WAF Cheat Sheets:
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/aws-waf/

</details>

<a id="q54"></a>

## Q54

A health insurance company has recently adopted a hybrid cloud architecture which connects their on-premises network and their cloud infrastructure in AWS. They have an ELB which has a set of EC2 instances behind them. As the cloud engineer of the company, your manager instructed you to ensure that the SSL key used to encrypt data is always kept secure at all times. In addition, the application logs should only be decrypted by a handful of key users.
In this scenario, which of the following meets all of the requirements?

- **A.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
- **B.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic. 3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
- **C.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot. 3. Persist your application server logs to a private S3 bucket using SSE.
- **D.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to a private S3 bucket using SSE.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** SSL key always secure; logs decrypted by few users

⚠️ **Watch:** Ephemeral volumes lose logs

🧠 **Rule:** Key never leaves → CloudHSM with TCP LB; logs → private S3 with SSE.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises ──hybrid──► AWS
                          │
                   ELB ──► EC2 instances

Yêu cầu:
1. SSL key luôn được giữ AN TOÀN tuyệt đối
2. Application logs chỉ một số ít người dùng được decrypt
```

Đáp án đúng: **D** — ELB **TCP load balancing** + **AWS CloudHSM** xử lý SSL transactions + logs lưu trên **S3 private với SSE**. Anh chọn đúng D.

#### Vì sao D đúng

- **CloudHSM** cho phép tạo và lưu giữ private key trong một hardware security module FIPS 140-2 Level 3 — **private key không bao giờ rời khỏi HSM**, đáp ứng đúng yêu cầu "SSL key luôn giữ an toàn tuyệt đối" tốt hơn là upload key vào EC2 hay S3.
- **ELB chạy TCP load balancing (Layer 4)**: vì CloudHSM là bên thực hiện SSL/TLS handshake (offload SSL), ELB chỉ cần forward traffic ở layer TCP, không terminate SSL tại ELB.
- **Logs lưu trên S3 private + SSE (Server-Side Encryption)**: S3 là storage bền (durable), SSE mã hóa dữ liệu tại rest, và việc ai được decrypt (qua quyền KMS/key) có thể giới hạn cho một nhóm nhỏ người dùng — đáp ứng "chỉ một số ít người dùng decrypt được logs".

#### Vì sao từng đáp án sai bị loại

- **A sai** vì logs được lưu trên **ephemeral volume** — loại storage tạm, dữ liệu mất khi instance dừng/terminate, không đảm bảo logs được giữ lại lâu dài hay durable.
- **B sai** vì **upload private key lên EC2 instance** để tự offload SSL — vi phạm trực tiếp yêu cầu "SSL key luôn an toàn", vì key nằm trên OS của EC2, dễ bị truy cập hơn CloudHSM. Thêm vào đó logs cũng lưu ephemeral volume như A.
- **C sai** vì EC2 **retrieve private key từ một S3 bucket non-public khi boot** — về nguyên tắc **không nên lưu private key nhạy cảm trên S3**, dù bucket có private hay không, vì rủi ro rò rỉ lớn hơn CloudHSM.

#### So sánh nhanh

| Đáp án | Nơi xử lý SSL key | Nơi lưu logs | Vấn đề |
|---|---|---|---|
| **D (đúng)** | CloudHSM | S3 private + SSE | Không |
| A | CloudHSM | Ephemeral volume | Logs không durable |
| B | Private key trên EC2 | Ephemeral volume | Key không an toàn + logs không durable |
| C | Private key trên S3, load khi boot | S3 private + SSE | Key không nên lưu trên S3 |

#### Lưu ý thực tế

- CloudHSM tự động hóa các việc vận hành HSM phức tạp: hardware provisioning, patching, high availability, backup — và tự đồng bộ key giữa các HSM trong cluster, nên vẫn scale và HA được dù key "không rời HSM".
- Nguyên tắc chung khi thấy đề nhắc "private key phải luôn an toàn tuyệt đối": loại ngay các lựa chọn để key trên EC2 hoặc S3 — chỉ CloudHSM (hoặc KMS cho các trường hợp khác) mới đáp ứng.

#### Quy tắc nhớ cho thi

- **"SSL/TLS key phải tuyệt đối an toàn"** → **AWS CloudHSM**, không bao giờ để private key trên EC2 hoặc S3
- **"CloudHSM xử lý SSL"** → ELB chạy **TCP load balancing** (Layer 4), không terminate SSL tại ELB
- **"Logs cần durable + decrypt hạn chế"** → **S3 private + SSE**, không dùng ephemeral volume

### TD explanation

AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. With CloudHSM, you can manage your own encryption keys using FIPS 140-2 Level 3 validated HSMs. CloudHSM offers you the flexibility to integrate with your applications using industry-standard APIs, such as PKCS#11, Java Cryptography Extensions (JCE), and Microsoft CryptoNG (CNG) libraries.
You can use AWS CloudHSM to offload SSL/TLS processing for your web servers. Using CloudHSM for this processing reduces the burden on your web server and provides extra security by storing your web server’s private key in CloudHSM. Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are used to confirm the identity of web servers and establish secure HTTPS connections over the Internet.

AWS CloudHSM automates time-consuming HSM administrative tasks for you, such as hardware provisioning, software patching, high availability, and backups. You can scale your HSM capacity quickly by adding and removing HSMs from your cluster on-demand. AWS CloudHSM automatically load balances requests and securely duplicates keys stored in any HSM to all of the other HSMs in the cluster.
CloudHSM provides a better and more secure way of offloading the SSL processing for the web servers and ensures the application logs are durably and securely stored.
In this scenario, the following option is the best choice because it uses CloudHSM and the application server logs are persisted in an S3 bucket with a Server Side Encryption (SSE):
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Configure the ELB to perform TCP load balancing.
3. Use an AWS CloudHSM instance to perform the SSL transactions.
4. Persist your application server logs to a private S3 bucket using SSE.
The following sets of options are incorrect because the ephemeral volume is just temporary storage and hence, not a suitable option for durable storage:
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic.
3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
as well as this option:
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Configure the ELB to perform TCP load balancing.
3. Use an AWS CloudHSM instance to perform the SSL transactions.
4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
The following option is incorrect because you should never store sensitive private keys in S3:
1. Use the ELB to distribute traffic to a set of EC2 instances.
2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot.
3. Persist your application server logs to a private S3 bucket using SSE.

References:
https://aws.amazon.com/cloudhsm/
https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-overview.html

</details>

<a id="q65"></a>

## Q65

A company runs a cryptocurrency analytics website and uses a CloudFront distribution with a custom domain name (tutorialsdojo.com) to speed up the loading time of the site. Since the data being distributed are quite confidential, the management instructed the solutions architect to require HTTPS communication between the viewers (web visitors) and the CloudFront distribution. Additionally, it is required to improve the performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers. 
Which of the following are the recommended actions to accomplish the above requirement? (Select TWO.)

- **A.** Configure the CloudFront origin to add a Cache-Control max-age directive to your objects and specify the longest practical value for max-age.
- **B.** Use an SSL/TLS certificate provided by AWS Certificate Manager (ACM).
- **C.** Import an SSL/TLS certificate from a third-party certificate authority into a private S3 bucket with versioning and MFA enabled.
- **D.** Associate your CloudFront web distribution with Lambda@Edge which provides automatic scalability from a few requests per day to thousands of requests per second.
- **E.** Integrate your CloudFront web distribution with Amazon OpenSearch to cache recent requests and improve the performance of your origin servers. Use Kibana to visualize the cache hit-ratio graph in real time.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B (you answered correctly)

🔑 **Key words:** HTTPS viewer↔CloudFront with custom domain; higher cache hit ratio (Select TWO)

⚠️ **Watch:** ⚠️ Q1: public ACM certs are free; import third-party certs into ACM, not S3

🧠 **Rule:** ACM certificate + long Cache-Control max-age.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Viewer ──HTTPS?──► CloudFront (custom domain: tutorialsdojo.com) ──► Origin
```

Hai yêu cầu riêng biệt (chọn HAI):
1. Bắt buộc **HTTPS** giữa viewer và CloudFront, dùng **custom domain**
2. Tăng **cache hit ratio** để giảm request chạm tới origin

Đáp án đúng: **A (Cache-Control max-age dài)** + **B (ACM certificate)**. Anh chọn đúng A, B.

#### Vì sao A, B đúng

**B — custom domain + HTTPS:**
- Khi dùng domain riêng (không phải `*.cloudfront.net`), CloudFront **không thể tự cấp SSL/TLS certificate** như trường hợp domain mặc định — phải **dùng certificate từ AWS Certificate Manager (ACM)**, hoặc import certificate bên thứ ba **vào ACM** (hoặc IAM certificate store).
- Đây là bước bắt buộc để cấu hình Viewer Protocol Policy yêu cầu HTTPS trên custom domain.

**A — tăng cache hit ratio:**
- Cấu hình origin thêm **Cache-Control max-age** với giá trị càng dài càng tốt (trong giới hạn hợp lý) → CloudFront giữ object trong cache lâu hơn, giảm số lần phải forward request về origin để kiểm tra object có thay đổi hay không.
- max-age ngắn → CloudFront phải "hỏi lại" origin thường xuyên hơn → cache hit ratio thấp hơn.

#### Vì sao từng đáp án sai bị loại

- **C sai** vì **import SSL/TLS certificate vào S3** — về nguyên tắc **không nên lưu certificate (public hay private) trên S3 bucket**; certificate bên thứ ba phải import **vào ACM**, không phải S3.
- **D sai** vì **Lambda@Edge** dùng để tùy biến nội dung CloudFront trả về (ví dụ theo User-Agent, theo cookie...), không liên quan đến việc cải thiện cache hit ratio.
- **E sai** vì **Amazon OpenSearch + Kibana** dùng cho log analytics / monitoring thời gian thực, không phải cơ chế cache của CloudFront — không ảnh hưởng gì tới cache hit ratio.

#### So sánh nhanh

| Đáp án | Mục tiêu nhắm tới | Vấn đề |
|---|---|---|
| **A (đúng)** | Tăng cache hit ratio | Không |
| **B (đúng)** | HTTPS cho custom domain | Không |
| C | "HTTPS" nhưng sai nơi lưu cert | Cert không nên lưu trên S3 |
| D | Không liên quan cache hit ratio | Lambda@Edge dùng để customize content |
| E | Không liên quan cache hit ratio | OpenSearch/Kibana chỉ để phân tích log |

#### Lưu ý thực tế

⚠️ Dễ nhầm (liên quan Q1 — nhóm wrong-answer): **ACM public certificate hoàn toàn miễn phí**, chỉ cần verify quyền sở hữu domain qua DNS hoặc email — không có lý do gì phải trả phí hoặc dùng S3 để lưu certificate. Ngược lại, **ACM Private Certificate** mới tính phí theo tháng (cần Private CA) và chỉ cần thiết cho PKI nội bộ, không áp dụng cho website public như bài này. Việc "import certificate bên thứ ba" luôn đưa **vào ACM**, chưa từng có chuyện lưu certificate trực tiếp trên S3 trong bất kỳ ngữ cảnh AWS hợp lệ nào.

#### Quy tắc nhớ cho thi

- **"Custom domain + HTTPS trên CloudFront"** → **ACM certificate** (public, free), attach vào distribution
- **"Tăng cache hit ratio"** → **Cache-Control max-age** dài nhất có thể trên origin
- **"Certificate của bên thứ ba"** → import **vào ACM**, tuyệt đối không lưu trên S3
- **"Lambda@Edge" / "OpenSearch+Kibana"** → không liên quan đến cache hit ratio, chỉ là bẫy

### TD explanation

You can configure one or more cache behaviors in your CloudFront distribution to require HTTPS for communication between viewers and CloudFront. You also can configure one or more cache behaviors to allow both HTTP and HTTPS so that CloudFront requires HTTPS for some objects but not for others. The configuration steps depend on which domain name you’re using in object URLs:
– If you’re using the domain name that CloudFront assigned to your distribution, such as d111111abcdef8.cloudfront.net, you change the Viewer Protocol Policy setting for one or more cache behaviors to require HTTPS communication. In that configuration, CloudFront provides the SSL/TLS certificate.
– If you’re using your own domain name, such as tutorialsdojo.com, you need to change several CloudFront settings. You also need to use an SSL/TLS certificate provided by AWS Certificate Manager (ACM), or import a certificate from a third-party certificate authority into ACM or the IAM certificate store.

You can improve performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers for content; that is, by improving the cache hit ratio for your distribution. To increase your cache hit ratio, you can configure your origin to add a Cache-Control max-age directive to your objects and specify the longest practical value for max-age. The shorter the cache duration, the more frequently CloudFront forwards another request to your origin to determine whether the object has changed and, if so, to get the latest version.
Therefore, the correct answers are:
-Use an SSL/TLS certificate provided by AWS Certificate Manager (ACM)
-Configure the CloudFront origin to add a Cache-Control max-age directive to your objects and specifying the longest practical value for max-age.
The option that says: Associate your CloudFront web distribution with Lambda@Edge which provides automatic scalability from a few requests per day to thousands of requests per second is incorrect because Lambda@Edge is an extension of AWS Lambda which lets you execute functions that customize the content that CloudFront delivers. This feature does not improve the cache hit ratio of your CloudFront distribution.
The option that says: Integrate your CloudFront web distribution with Amazon OpenSearch to cache recent requests and improve the performance of your origin servers. Use Kibana to visualize the cache hit-ratio graph in real time is incorrect. Amazon OpenSearch service is used to perform interactive log analytics, real-time application monitoring, and more. This service will not improve the cache hit ratio of your CloudFront distribution. The built-in Kibana support only provides a way to get faster and better insights into your data and thus, not relevant to this scenario.
The option that says: Import an SSL/TLS certificate from a third-party certificate authority into a private S3 bucket with versioning and MFA enabled is incorrect. For an SSL certificate, whether it is public or private, is not recommended to store it on an Amazon S3 bucket.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/aws-certificate-manager/

</details>

<a id="q69"></a>

## Q69

A company stores several terabytes of data on an Amazon S3 bucket. The data will be made available to respective partner companies, however, the management doesn’t want the partner companies to access the files directly from Amazon S3 URLs. The solutions architect has been asked to ensure that all confidential files shared via Amazon S3 should only be accessible through CloudFront. 
Which of the following options could satisfy this requirement?

- **A.** Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission.
- **B.** Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access.
- **C.** Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront.
- **D.** Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN).

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** files only accessible through CloudFront

⚠️ **Watch:** Distribution ID is not a valid S3 principal

🧠 **Rule:** S3 origin locked to CloudFront → Origin Access Control + bucket policy.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Partner companies ──┬──► S3 URL trực tiếp (KHÔNG được phép)
                     │
                     └──► CloudFront distribution ──► S3 bucket (origin)

Yêu cầu: tất cả file confidential chỉ được truy cập qua CloudFront.
```

Đáp án đúng: **A** — tạo **Origin Access Control (OAC)**, gắn vào CloudFront distribution, đổi quyền S3 bucket chỉ cho OAC đọc. Anh chọn đúng A.

#### Vì sao A đúng

- Mặc định, nếu S3 bucket cho phép "everyone" đọc object, user vẫn có thể truy cập trực tiếp qua **S3 URL** dù CloudFront không hề expose URL đó công khai — vì S3 URL vẫn tồn tại độc lập và có thể bị lộ (ứng dụng trả về trực tiếp, hoặc ai đó share link).
- **OAC** là một "CloudFront user" đặc biệt, được CloudFront dùng để ký (SigV4) các request gửi tới S3. Khi gắn OAC vào distribution và **đổi permission S3 bucket chỉ cho OAC đọc**, mọi request trực tiếp bằng S3 URL (không có signature của OAC) sẽ bị từ chối.
- Kết quả: file chỉ truy cập được **qua CloudFront** — đúng yêu cầu đề bài, dù không cần giới hạn một client cụ thể nào (khác với bài toán "chỉ một client" ở Q44).

#### Vì sao từng đáp án sai bị loại

- **D sai** vì **CloudFront Distribution ID không phải là một Principal hợp lệ** trong S3 bucket policy — cú pháp này không hoạt động về mặt kỹ thuật, cần dùng OAC (được AWS cung cấp đúng cơ chế) thay vì tự viết policy với Distribution ID.
- **C sai** vì gán một **IAM user** có quyền truy cập bucket cho CloudFront không tạo ra cơ chế **loại trừ** truy cập trực tiếp — IAM user chỉ quản lý quyền của "ai" gọi API, không chặn được việc người dùng cuối (viewer) gõ thẳng S3 URL.
- **B sai** vì không cần viết **policy riêng cho từng bucket** — đây là việc làm thừa, không giải quyết gốc vấn đề (chặn truy cập trực tiếp vào S3), lại tốn công vận hành khi có nhiều bucket.

#### So sánh nhanh

| Đáp án | Cơ chế | Chặn được S3 URL trực tiếp? |
|---|---|---|
| **A (đúng)** | OAC + bucket policy chỉ cho OAC | Có |
| B | Policy riêng từng bucket cho CloudFront | Không hợp lý, thừa thao tác |
| C | Gán IAM user cho CloudFront | Không chặn trực tiếp S3 URL |
| D | Bucket policy với Distribution ID là Principal | Sai cú pháp, không hoạt động |

#### Lưu ý thực tế

⚠️ Dễ nhầm: **OAC chỉ đảm bảo request đi đúng đường qua CloudFront**, nó không giới hạn **AI** được dùng CloudFront URL đó. Nếu đề yêu cầu thêm "chỉ MỘT client cụ thể" (như Q44 ở nhóm wrong-answer) thì phải bổ sung **CloudFront signed URL/signed cookie** mới đủ — OAC một mình không đáp ứng được mức giới hạn đó. Ở Q69 này, đề chỉ yêu cầu "chặn truy cập trực tiếp S3, buộc đi qua CloudFront" (không giới hạn client nào), nên OAC một mình là đủ và đúng.

#### Quy tắc nhớ cho thi

- **"Chỉ truy cập được qua CloudFront, chặn S3 URL trực tiếp"** → **OAC** + sửa bucket policy chỉ cho OAC đọc
- **"Chỉ MỘT client cụ thể truy cập được"** → cần thêm **signed URL / signed cookie**, OAC không đủ
- **CloudFront Distribution ID** không bao giờ là một **Principal** hợp lệ trong IAM/bucket policy

### TD explanation

To restrict access to content that you serve from Amazon S3 buckets, you create CloudFront signed URLs or signed cookies to limit access to files in your Amazon S3 bucket, and then you create a special CloudFront user called an origin access control (OAC) and associate it with your distribution. Then you configure permissions so that CloudFront can use the OAC to access and serve files to your users, but users can’t use a direct URL to the S3 bucket to access a file there. Taking these steps helps you maintain secure access to the files that you serve through CloudFront.
In general, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you can either allow everyone to have access to the files there, or you can restrict access. If you limit access by using, for example, CloudFront signed URLs or signed cookies, you also won’t want people to be able to view files by simply using the direct URL for the file. Instead, you want them to only access the files by using the CloudFront URL, so your protections work.

Typically, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you grant everyone permission to read the objects in your bucket. This allows anyone to access your objects either through CloudFront or using the Amazon S3 URL. CloudFront doesn’t expose Amazon S3 URLs, but your users might have those URLs if your application serves any objects directly from Amazon S3 or if anyone gives out direct links to specific objects in Amazon S3.
Therefore, the correct answer is: Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission. It gives CloudFront exclusive access to the S3 bucket and prevents other users from accessing the public content of S3 directly via S3 URL.
The option that says: Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN) is incorrect. Creating a bucket policy is unnecessary and it does not prevent other users from accessing the public content of S3 directly via S3 URL.
The option that says: Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront is incorrect. This does not give CloudFront exclusive access to the S3 bucket.
The option that says: Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access is incorrect. You do not need to create any individual policies for each bucket.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amazon-s3/

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

S3 Pre-signed URLs vs CloudFront Signed URLs vs Origin Access Control (OAC)
https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services/

</details>

---

# Group C — DR / HA / database resilience (7)

<a id="q10"></a>

## Q10

A leading media company is building a collaborative news website that is expected to have over 5 million readers per month globally. Each article contains a cover image and has at least 200 words. Based on the trend of their other websites, the new articles are highly browsed in the first 2 months and the authors tend to frequently update the articles on the first month after its publication. The readership is also expected to drop on the 3rd month and the articles are usually rarely accessed after a year. The readers are also leaving a lot of comments within the first 3 months of publishing. 
In this scenario, which of the following items can you use to build a durable, highly available, and scalable architecture for the news website? (Select TWO.)

- **A.** Use Lambda with Auto-Healing enabled.
- **B.** Use Amazon RDS Multi-AZ deployments with Read Replicas. Use S3 to store the static data such as the cover images and other media.
- **C.** Launch an RDS Oracle Real Application Clusters (RAC) with Read Replicas.
- **D.** Use CloudFront as a Content Delivery Network to load the articles much faster anywhere in the globe.
- **E.** Use EBS Volumes in RAID 0 configuration to store the static data such as the cover images and other media.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D (you answered correctly)

🔑 **Key words:** 5M readers; durable, HA, scalable news site (Select TWO)

⚠️ **Watch:** RAID 0 has no redundancy

🧠 **Rule:** RDS Multi-AZ + read replicas, S3 for media, CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
News website, 5M readers/tháng, global
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│ Cover image │     │ Article text │     │ Comments      │
│ (static)    │     │ (DB record)  │     │ (3 tháng đầu) │
└─────────────┘     └──────────────┘     └──────────────┘
Yêu cầu: durable + highly available + scalable (Select TWO)
```

Đề cho 5 lựa chọn nhưng chỉ cần đúng 2 cấu phần: nơi lưu **ảnh/media tĩnh** và nơi chạy **database**. Đáp án đúng: **B** (RDS Multi-AZ + Read Replicas, S3 cho media) + **D** (CloudFront). Anh chọn đúng cả hai.

#### Vì sao B và D đúng

- **B — RDS Multi-AZ + Read Replicas, S3 cho media:** Multi-AZ cho **high availability** (failover tự động khi AZ gặp sự cố), Read Replicas cho **scalability** (san tải đọc cho lượng truy cập khổng lồ hàng tháng). S3 lưu ảnh bìa và media đạt **11 số 9 durability**, đúng yêu cầu "durable".
- **D — CloudFront:** bài viết được đọc nhiều nhất trong 2 tháng đầu, độc giả ở khắp toàn cầu → CDN cache nội dung gần người dùng, tải trang nhanh hơn bất kể vị trí địa lý — đúng yêu cầu "scalable" cho lưu lượng global.

Hai lựa chọn này bổ sung cho nhau: D xử lý **tầng phân phối** (network/CDN), B xử lý **tầng lưu trữ** (data layer) — tạo thành một giải pháp hoàn chỉnh.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì Lambda **không có khái niệm Auto-Healing** — Lambda là serverless, function chỉ chạy theo event, không có "instance" nào cần tự hồi phục.
- **C sai** vì **RDS không hỗ trợ Oracle RAC (Real Application Clusters)**. RAC là tính năng cluster của Oracle chạy trên hạ tầng riêng mà RDS không cung cấp.
- **E sai** vì **RAID 0 không có redundancy** — một disk hỏng là mất toàn bộ dữ liệu (ngược hẳn với yêu cầu "durable"). TD giải thích thêm: dù dùng RAID 1 (mirroring) thì EBS vẫn kém durable và kém scalable hơn S3.

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** RAID 0 trên EBS tăng **IOPS/throughput** (striping), không tăng độ bền — đề thi hay gài "RAID 0 để lưu dữ liệu quan trọng" như một cái bẫy. Muốn durable thật, phải dùng S3 hoặc ít nhất RAID 1/EBS snapshot, chứ RAID 0 không bao giờ là lựa chọn cho "durable storage".

#### Quy tắc nhớ cho thi

- **"Static media (ảnh, video) + cần durable + scalable"** → **Amazon S3**, không phải EBS
- **"Global readers, cần tải nhanh mọi nơi"** → **CloudFront**
- **"RDS + Oracle RAC"** → luôn là **bẫy sai**, RDS không hỗ trợ RAC
- **"RAID 0"** → chỉ tăng performance, **không tăng độ bền dữ liệu**
- **Lambda** → không có "Auto-Healing", vì nó không chạy instance thường trực

### TD explanation

In this scenario, the main objective is to provide a durable, highly-available and scalable architecture for the website. You can use CloudFront as a CDN, then Amazon RDS with Multi-AZ deployments and Read Replicas to provide scalability and high-availability for the millions of incoming traffic every month. Lastly, you can use an S3 bucket to durably store the images and other static media content of the website.

Therefore, the correct answer is: Use CloudFront as a Content Delivery Network to load the articles much faster anywhere in the globe and Use Amazon RDS Multi-AZ deployments with Read Replicas. Use S3 to store the static data such as the cover images and other media.
The option that says: Launch an RDS Oracle Real Application Clusters (RAC) with Read Replicas is incorrect because Oracle RAC is not supported in RDS.
The option that says: Use Lambda with Auto-Healing enabled is incorrect. AWS Lambda is serverless and it does not have Auto-Healing option since functions are event-driven.
The option that says: Use EBS Volumes in RAID 0 configuration to store the static data such as the cover images and other media is incorrect because EBS Volumes are not as durable and not as scalable compared with S3, even with a RAID 1 (mirroring) configuration.

References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
https://aws.amazon.com/s3/

Check out these Amazon RDS and Amazon S3 Cheat Sheets:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q11"></a>

## Q11

A company hosts its main web application on the AWS cloud which is composed of web servers and database servers. To ensure high availability, the web servers are deployed on an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones with an Application Load Balancer in front. For the database, it is deployed on a Multi-Availability Zone configuration in Amazon RDS. During the RDS maintenance window, the operating system of the primary DB instance undergoes software patching that triggers the failover process.
What would happen to the database during failover?

- **A.** A new DB instance will be created and immediately replace the primary database.
- **B.** The RDS DB instance will automatically reboot.
- **C.** The IP address of the primary DB instance is switched to the standby DB instance.
- **D.** The canonical name record (CNAME) is changed from the primary database to standby database.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** what happens during RDS Multi-AZ failover

⚠️ **Watch:** IP address does not move

🧠 **Rule:** Multi-AZ failover flips the DB endpoint CNAME to the standby.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Web tier: ASG multi-AZ + ALB
DB tier:  RDS Multi-AZ
              │
   Maintenance window → patch OS trên primary
              │
          FAILOVER xảy ra
              │
   Điều gì thay đổi để app vẫn kết nối được DB?
```

Câu hỏi thuần lý thuyết: cơ chế failover của RDS Multi-AZ hoạt động **như thế nào** ở tầng network. Đáp án đúng: **D** — CNAME record của DB endpoint được đổi từ primary sang standby. Anh chọn đúng D.

#### Vì sao D đúng

RDS Multi-AZ tạo **một DB endpoint duy nhất** mà ứng dụng luôn kết nối tới (ví dụ `mydb.xxxxx.rds.amazonaws.com`). Endpoint này thực chất là một **CNAME record**, trỏ tới IP của instance đang là primary tại thời điểm đó. Khi failover xảy ra (do patch OS, do AZ down, do primary lỗi…), RDS **không tạo instance mới**, không cần ứng dụng đổi connection string — RDS chỉ **cập nhật lại CNAME** để nó trỏ sang standby instance vừa được promote thành primary mới. Ứng dụng "vô tình" kết nối đúng chỗ vì DNS tự cập nhật.

#### Vì sao từng đáp án sai bị loại

- **C sai** vì IP address **không di chuyển** — chỉ CNAME đổi hướng, không có việc "switch IP của primary sang standby". Đây là điểm TD nhấn mạnh rõ: CNAME thay đổi, không phải IP.
- **B sai** vì RDS instance **không tự reboot** trong quá trình failover — standby vốn đã chạy sẵn (đồng bộ dữ liệu liên tục), chỉ cần được promote, không cần khởi động lại.
- **A sai** vì **không có instance mới nào được tạo** — standby đã tồn tại từ trước (đó chính là ý nghĩa của Multi-AZ: luôn có bản sao đồng bộ sẵn sàng), failover chỉ là việc promote standby có sẵn.

#### So sánh nhanh

| Đáp án | Cơ chế đề xuất | Đúng không? |
|---|---|---|
| **D (đúng)** | Đổi CNAME từ primary sang standby | ✅ |
| C | Đổi IP address | ❌ — IP không đổi, chỉ CNAME đổi |
| B | Tự động reboot | ❌ — standby đã chạy sẵn, không cần reboot |
| A | Tạo instance mới | ❌ — standby có sẵn từ lúc tạo Multi-AZ |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** Multi-AZ chỉ là cơ chế **High Availability (HA)**, giúp failover nhanh trong **cùng Region** — nó **không phải Disaster Recovery (DR)** giữa các Region. Nếu đề hỏi về khôi phục sau khi **toàn bộ Region** sập, câu trả lời phải xoay quanh **Read Replica cross-region**, snapshot cross-region, hoặc Aurora Global Database — không phải Multi-AZ.

#### Quy tắc nhớ cho thi

- **"RDS Multi-AZ failover"** → chỉ đổi **CNAME endpoint**, IP và instance ID không đổi
- **"Standby instance"** → luôn đã tồn tại và đồng bộ sẵn, failover là **promote**, không phải **tạo mới**
- **"Multi-AZ" ≠ "Disaster Recovery"** — Multi-AZ là HA trong 1 Region, DR cần giải pháp cross-region

### TD explanation

Amazon RDS Multi-AZ deployments provide enhanced availability and durability for Database (DB) Instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of Amazon Aurora), so that you can resume database operations as soon as the failover is complete.

When automatic failover occurs, your application can remain unaware of what’s happening behind the scenes. The CNAME record for your DB instance will be altered to point to the newly promoted standby.
Therefore, the correct answer is: The canonical name record (CNAME) is changed from the primary database to standby database.
The option that says: The IP address of the primary DB instance is switched to the standby DB instance is incorrect because the Canonical Name Record (CNAME) will be changed and not the IP address.
The option that says: The RDS DB instance will automatically reboot is incorrect because the RDS instance will not automatically reboot.
The option that says: A new DB instance will be created and immediately replace the primary database is incorrect because there is no new DB instance that will be created.

References:
https://aws.amazon.com/rds/details/multi-az/
https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-deployment/

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q13"></a>

## Q13

An enterprise software company has just recently started using AWS as its cloud infrastructure. The company is building an enterprise proprietary issue tracking system which would be accessed by its customers worldwide. Hence, the CTO carefully instructed the team to ensure that the architecture of the issue tracking system is both scalable and highly available to avoid any complaints from the clients. It is expected that the application will have steady-state usage, and the database would be used for online transaction processing (OLTP). The team recently used the AWS Well-Architected Tool to review its architecture, which highlighted the need for a highly available and fault-tolerant design.
Which of the following would be the best architecture setup to satisfy the above requirement?

- **A.** Launch an Auto Scaling group of Spot Amazon EC2 instances with an ELB in front to handle the load balancing. Leverage on Amazon CloudFront in distributing your static content and an Amazon RDS instance with Read Replicas.
- **B.** Use an AWS CloudFormation template to launch an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones, which are all connected via an ELB to handle the load balancing. Leverage Amazon CloudFront for distributing your static content and an Amazon RDS instance with a Multi-AZ deployment configuration.
- **C.** Use a Dedicated Amazon EC2 instance as the application server and Amazon Redshift as a petabyte-scale data warehouse service. Use Amazon ElastiCache for in-memory data caching for your database to improve performance.
- **D.** Use multiple On-Demand Amazon EC2 instances to host the application and a highly scalable Amazon DynamoDB for the database. Use Amazon ElastiCache for in-memory data caching for your database to improve performance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** issue tracker; steady state; OLTP; HA + fault tolerant

⚠️ **Watch:** Spot for a steady-state HA tier is risky

🧠 **Rule:** Multi-AZ ASG + ELB + CloudFront + RDS Multi-AZ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Issue tracking system — khách hàng toàn cầu
Yêu cầu: scalable + highly available + fault-tolerant
Database: OLTP, steady-state usage
AWS Well-Architected Tool → cần HA + fault-tolerant design
```

Đề cho 4 kiến trúc khác nhau, mỗi cái khác ở: loại EC2 (Spot/On-Demand), DB (RDS Multi-AZ/Read Replica/DynamoDB), và deploy tool. Đáp án đúng: **B** — CloudFormation + ASG multi-AZ + ELB + CloudFront + RDS Multi-AZ. Anh chọn đúng B.

#### Vì sao B đúng

- **ASG multi-AZ + ELB**: đúng cả hai yêu cầu "scalable" (auto scaling theo tải) và "highly available" (instance phân tán nhiều AZ, ELB route traffic tránh AZ lỗi).
- **CloudFront**: giảm tải cho origin, cải thiện tốc độ cho khách hàng toàn cầu.
- **RDS Multi-AZ**: đúng với đặc tính **OLTP steady-state** — Multi-AZ đảm bảo DB luôn có failover sẵn sàng khi 1 instance down, đúng yêu cầu "fault-tolerant".
- **CloudFormation**: TD khuyến nghị dùng IaC để launch kiến trúc, dù không phải điểm quyết định chính nhưng là best practice được đề cập.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng **Spot Instances** — Spot không phù hợp cho workload **steady-state** (ổn định, liên tục) vì có thể bị interrupt bất cứ lúc nào, phá vỡ tính "highly available" cho hệ thống OLTP chạy liên tục. Ngoài ra chỉ dùng **Read Replicas** thay vì Multi-AZ — Read Replica chỉ phục vụ đọc, availability kém hơn Multi-AZ nhiều.
- **C sai** vì **Dedicated EC2 instance không có Auto Scaling** → không scalable, không HA. Ngoài ra **Redshift dùng cho OLAP** (data warehouse phân tích), không phù hợp cho **OLTP** như đề yêu cầu.
- **D sai** vì chỉ dùng **"multiple On-Demand instances"** không qua Auto Scaling Group, và **không triển khai across multiple AZs** → thiếu cả tính scalable và HA theo đúng nghĩa.

#### So sánh nhanh

| Đáp án | EC2 | Multi-AZ? | DB | Vấn đề |
|---|---|---|---|---|
| **B (đúng)** | ASG + ELB, multi-AZ | Có | RDS Multi-AZ | Không có |
| A | ASG Spot | — | RDS Read Replica | Spot không ổn định cho steady-state; Read Replica ≠ HA |
| C | Dedicated, không ASG | — | Redshift (OLAP) | Không scalable; sai loại DB |
| D | On-Demand, không ASG | Không rõ multi-AZ | DynamoDB | Thiếu ASG, thiếu multi-AZ |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** **Multi-AZ (HA)** và **Read Replica (scale đọc)** giải quyết hai bài toán khác nhau — Multi-AZ không cải thiện read performance, Read Replica không tự động failover thành primary khi chính nó gặp sự cố (phải manual promote). Đề hay gài: "dùng Read Replica để tăng availability" — sai, Read Replica chỉ tăng khả năng đọc, không thay thế được Multi-AZ cho HA.

#### Quy tắc nhớ cho thi

- **"Steady-state workload"** → **Reserved/On-Demand + Auto Scaling**, tránh Spot làm nền tảng chính
- **"OLTP"** → RDS/Aurora; **"OLAP/data warehouse"** → Redshift
- **"HA + fault-tolerant cho RDS"** → **Multi-AZ**, không phải Read Replica
- **"Scalable + HA cho web tier"** → luôn cần **ASG trải nhiều AZ + ELB**

### TD explanation

It is recommended to use a CloudFormation template to launch your architecture in AWS. An Auto Scaling group of EC2 instances across multiple Availability Zones with an ELB in front is a highly available and scalable architecture. In addition, leveraging on CloudFront in distributing your static content improves the load times of the system. Finally, an RDS instance with Multi-AZ deployments configuration can ensure the availability of your database in case one instance goes down.

Therefore, the correct answer is: Use an AWS CloudFormation template to launch an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones, which are all connected via an ELB to handle the load balancing. Leverage Amazon CloudFront for distributing your static content and an Amazon RDS instance with a Multi-AZ deployment configuration. This offers high availability and scalability for the application.
The option that says: Use a Dedicated Amazon EC2 instance as the application server and Amazon Redshift as a petabyte-scale data warehouse service. Use Amazon ElastiCache for in-memory data caching for your database to improve performance is incorrect. Using Dedicated EC2 instances without Auto Scaling is not a scalable nor a highly available architecture. In addition, RedShift is not applicable to OLTP but rather with OLAP.
The option that says: Launch an Auto Scaling group of Spot Amazon EC2 instances with an ELB in front to handle the load balancing. Leverage on Amazon CloudFront in distributing your static content and an Amazon RDS instance with Read Replicas is incorrect. Spot EC2 instances are just not suitable for steady state usage and Read Replicas only provide limited availability compared to Multi-AZ Deployments.
The option that says: Use multiple On-Demand Amazon EC2 instances to host the application and a highly scalable Amazon DynamoDB for the database. Use Amazon ElastiCache for in-memory data caching for your database to improve performance is incorrect. This does not use Auto Scaling and is not deployed across multiple Availability Zones.

References:
https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf
https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-best-practices.html
https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/architecting-for-high-availability.html

Check out this Amazon EC2 Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q29"></a>

## Q29

A company runs a popular photo-sharing site hosted on the AWS cloud. There are user complaints about the frequent downtime of the site considering the hefty price for using their service. The company is using a MySQL RDS instance to record user details and other data analytics. A standard S3 storage class bucket is used to store the photos and user metadata, which are frequently accessed only in the first month. The website is also capable of immediately retrieving the images no matter how long they were stored. The RDS instance is always affected and sometimes goes down when there is a problem in the Availability Zone. The solutions architect was tasked to analyze the current architecture and to solve the user complaints about the website. In addition, the solutions architect should also implement a system that automatically discovers, classifies, and protects personally identifiable information (PII) data in the Amazon S3 bucket. 
Which of the following options offers the BEST solution for this scenario?

- **A.** Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Amazon S3 Glacier Deep Archive after a month. Re-configure the existing database to use RDS Multi-AZ Deployments.
- **B.** Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket.  Replace the S3 Standard bucket with an Infrequent Access storage class. Re-configure the existing database to use RDS Read Replicas.
- **C.** Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Infrequent Access storage class after a month. Re-configure the existing database to use RDS Multi-AZ Deployments.
- **D.** Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 bucket with EBS Volumes and use Redshift instead of RDS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** RDS down on AZ issue; photos retrievable immediately; PII discovery

⚠️ **Watch:** Inspector ≠ PII; Glacier Deep Archive isn't immediate

🧠 **Rule:** Macie for PII; S3 IA after 1 month; RDS Multi-AZ for AZ failure.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Photo-sharing site
┌─────────────────────┐        ┌─────────────────────────┐
│ MySQL RDS            │        │ S3 Standard bucket       │
│ (user data)           │        │ (photos + PII metadata)  │
│ → down khi AZ lỗi     │        │ → chỉ hot 1 tháng đầu    │
└─────────────────────┘        └─────────────────────────┘
Yêu cầu: (1) tự động phát hiện/bảo vệ PII trong S3
         (2) retrieve ảnh NGAY LẬP TỨC bất kể lưu bao lâu
         (3) hết downtime khi AZ gặp sự cố
```

Đáp án đúng: **C** — Amazon Macie (PII) + lifecycle sang S3 Infrequent Access sau 1 tháng + RDS Multi-AZ. Anh chọn đúng C.

#### Vì sao C đúng

- **Amazon Macie**: đây là dịch vụ **chuyên biệt** để tự động discover, classify, protect PII trong S3 bằng machine learning — đúng chính xác yêu cầu đề bài.
- **S3 Standard → Infrequent Access (IA) sau 1 tháng**: dữ liệu chỉ "hot" trong tháng đầu rồi giảm truy cập, nhưng vẫn cần **retrieve ngay lập tức** — IA vẫn cho **millisecond access**, chỉ khác Standard ở giá lưu trữ/giá truy xuất, không có delay retrieval như Glacier.
- **RDS Multi-AZ**: giải quyết đúng vấn đề "RDS luôn down khi AZ gặp sự cố" — Multi-AZ failover sang standby tự động, giữ site luôn hoạt động.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng **Amazon Inspector** thay vì Macie — Inspector là dịch vụ **đánh giá bảo mật tự động cho EC2/container**, không liên quan gì tới phát hiện PII. Ngoài ra dùng **Glacier Deep Archive** cho ảnh cũ — vi phạm yêu cầu "retrieve ngay lập tức", vì Glacier Deep Archive có retrieval time hàng giờ.
- **B sai** vì vẫn dùng **Inspector** sai dịch vụ cho PII, và thay RDS Multi-AZ bằng **Read Replicas** — Read Replica chỉ cho phép đọc, nếu primary down thì **không ghi được** (ví dụ user mới không đăng ký được), không giải quyết downtime như yêu cầu.
- **D sai** vì thay S3 bằng **EBS Volumes** (không scalable bằng S3 cho lưu trữ media) và thay RDS bằng **Redshift** — Redshift là data warehouse phân tích (OLAP), không phải nơi lưu transactional user data.

#### So sánh nhanh

| Đáp án | Dịch vụ PII | Storage class | DB fix |
|---|---|---|---|
| **C (đúng)** | Macie | S3 IA sau 1 tháng | RDS Multi-AZ |
| A | Inspector (sai) | Glacier Deep Archive (chậm) | RDS Multi-AZ |
| B | Inspector (sai) | S3 IA | Read Replica (không fix write-down) |
| D | Macie | EBS + Redshift (sai service) | — |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** Amazon Inspector và Amazon Macie dễ bị gài nhầm vào nhau trên đề thi — **Inspector = security assessment cho EC2/ECR** (tìm lỗ hổng phần mềm), **Macie = phát hiện & bảo vệ dữ liệu nhạy cảm (PII) trong S3**. Thấy từ khóa "PII" hoặc "sensitive data trong S3" → luôn là Macie.

#### Quy tắc nhớ cho thi

- **"Tự động phát hiện PII trong S3"** → **Amazon Macie**, không phải Inspector
- **"Access ngay lập tức dù ít dùng"** → **S3 Standard-IA**, không dùng Glacier (có retrieval delay)
- **"RDS down khi AZ lỗi"** → fix bằng **Multi-AZ**, Read Replica không giải quyết được write-availability
- **Redshift** → chỉ dùng cho data warehouse/OLAP, không phải thay thế cho RDS OLTP

### TD explanation

Amazon Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. Amazon Macie recognizes sensitive data such as personally identifiable information (PII) or intellectual property and provides you with dashboards and alerts that give visibility into how this data is being accessed or moved. The fully managed service continuously monitors data access activity for anomalies and generates detailed alerts when it detects the risk of unauthorized access or inadvertent data leaks. Today, Amazon Macie is available to protect data stored in Amazon S3, with support for additional AWS data stores soon.

In this scenario, the best way to solve the issue is to: Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Infrequent Access storage class after a month. Re-configure the existing database to use RDS Multi-AZ Deployments. Keep in mind that the website should be able to immediately retrieve the images no matter how long they were stored. This means that you should not archive the images.
The option that says: Use Amazon Macie to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 bucket with EBS Volumes and use Redshift instead of RDS is incorrect because EBS Volumes are not as scalable as S3 and Redshift is not a suitable storage option as it is mainly used as a petabyte-scale data warehouse service.
The option that says: Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Use a lifecycle policy in S3 to move the old photos to Amazon S3 Glacier Deep Archive after a month. Re-configure the existing database to use RDS Multi-AZ Deployments is incorrect because although it is right to use Amazon RDS Multi-AZ deployments configuration, the use of Glacier Deep Archive is not preferred for this scenario. Take note that Glacier is primarily used for archiving and the retrieval times are much slower compared to S3. Implementing this solution means that the users will have to wait a long time to retrieve their photos. In addition, Amazon Inspector is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS, especially in Amazon EC2 instances. You have to use Amazon Macie instead.
The option that says: Use Amazon Inspector to automatically discover, classify, and protect personally identifiable information (PII) data in the Amazon S3 bucket. Replace the S3 Standard bucket with an Infrequent Access storage class. Re-configure the existing database to use RDS Read Replicas is incorrect because although it is right to use Infrequent Access storage class, the use of Read Replica is not suitable for this scenario. Although it may improve availability, you are only limited to use read operations when you use Read Replicas. This means when the primary database is down, the Read Replica would not be available to register new users since read operations are only allowed. Moreover, you have to use Amazon Macie and not Amazon Inspector, since this is just an automated security assessment service that helps improve the security and compliance of applications deployed on AWS.

References:
https://aws.amazon.com/s3/storage-classes/
https://aws.amazon.com/macie/
https://aws.amazon.com/macie/details/

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

Check out this Amazon Macie Cheat Sheet:
https://tutorialsdojo.com/amazon-macie/

</details>

<a id="q46"></a>

## Q46

A company located on the west coast of North America plans to release a new online service for its customers. The company already created a new VPC in the us-west-1 region where they will launch the Amazon EC2 instances that will host the web application. The application must be highly-available and must dynamically scale based on user traffic. In addition, the company wants to have a disaster recovery site in the us-east-1 region that will act as a passive backup of the running application.
Which of the following options should the Solutions Architect implement in order to achieve the requirements?

- **A.** Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB.
- **B.** Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create separate record entries for each region’s ALB on Amazon Route 53 and enable health checks to ensure high-availability for both regions.
- **C.** Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create record entries in Amazon Route 53 pointing to the ALBs with health check enabled and a failover routing policy.
- **D.** Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) that spans multiple Availability Zones (AZs) on both VPCs. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB. Create an Alias record entry in Amazon Route 53 that points to the DNS name of the ALB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** us-east-1 passive DR site

⚠️ **Watch:** An ALB can't span Regions

🧠 **Rule:** Separate ALB+ASG per Region + Route 53 failover routing.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
us-west-1 (primary)                us-east-1 (DR, passive)
┌─────────────────────┐            ┌─────────────────────┐
│ ALB (multi-AZ)        │            │ ALB (multi-AZ)        │
│ ASG (multi-AZ)        │            │ ASG (multi-AZ)        │
└─────────────────────┘            └─────────────────────┘
          │                                   │
          └────────── Route 53 ───────────────┘
        Record trỏ tới 2 ALB, health check,
        yêu cầu: us-east-1 là PASSIVE backup
```

Yêu cầu chốt: us-east-1 chỉ **đứng dự phòng (passive)**, nhận traffic khi us-west-1 fail — đây chính xác là bài toán **active-passive failover**. Đáp án đúng: **C** — mỗi Region có ALB+ASG riêng, Route 53 health check + **failover routing policy**. Anh chọn đúng C.

#### Vì sao C đúng

- **Mỗi Region tự có ALB + ASG multi-AZ riêng**: vì ALB và Auto Scaling group **chỉ hoạt động trong một Region** — không có "cross-region ALB" hay "cross-region ASG".
- **Route 53 health check + failover routing policy**: đây là cơ chế chính xác để tạo **active-passive**: Route 53 chỉ trả về record của resource "healthy primary"; khi primary down, mới chuyển sang secondary. Điều này khớp hoàn toàn với yêu cầu "DR site đóng vai trò passive backup" — tức bình thường **không nhận traffic**, chỉ nhận khi primary fail.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì cố gắng dùng **Inter-Region VPC peering** để một ASG "trải" cả hai Region và một ALB phục vụ cả hai — nhưng **Auto Scaling group không thể span nhiều Region**, và **ALB không thể route traffic sang EC2 instance ở Region khác**, dù có VPC peering.
- **D sai** cùng lỗi: ALB không span được multiple Region, ASG cũng không deploy instance xuyên Region được, VPC peering không thay đổi được giới hạn này.
- **B sai** vì kiến trúc kỹ thuật đúng (ALB+ASG riêng mỗi Region) nhưng **không chỉ rõ routing policy** — chỉ "tạo record riêng + enable health check" là chưa đủ để tạo **active-passive**; nếu không chọn đúng failover routing policy, Route 53 có thể trả về cả hai record (giống active-active), vi phạm yêu cầu "passive backup".

#### So sánh nhanh

| Đáp án | VPC peering? | ALB/ASG span region? | Routing policy |
|---|---|---|---|
| **C (đúng)** | Không cần | Riêng mỗi Region | **Failover** (đúng active-passive) |
| B | Không cần | Riêng mỗi Region | Không chỉ rõ policy (sai) |
| A | Có (vô nghĩa) | Cố span region (không thể) | — |
| D | Có (vô nghĩa) | Cố span region (không thể) | Alias đơn giản (không failover) |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** ALB có thể "span multiple Availability Zones" **trong cùng một Region**, nhưng **không bao giờ span được nhiều Region** — dù có VPC peering kết nối hai VPC ở hai Region, ALB vẫn chỉ route traffic tới target trong cùng Region của nó. VPC peering chỉ giải quyết network connectivity, không thay đổi được giới hạn scope của ALB/ASG.

#### Quy tắc nhớ cho thi

- **"DR site là passive backup"** → Route 53 **failover routing policy** + health check
- **ALB / Auto Scaling group** → luôn giới hạn trong **một Region**, không bao giờ span cross-region
- **"VPC peering"** → chỉ giải quyết network connectivity, **không** làm ALB/ASG hoạt động cross-region
- **"Active-active" vs "active-passive"** → active-active dùng routing policy khác (weighted, latency…), active-passive **bắt buộc dùng failover policy**

### TD explanation

On Amazon Route 53, after you create a hosted zone for your domain, such as tutorialsdojo.com, you create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain. You can create a record that points to the DNS name of your Application Load Balancer on AWS.
When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:

Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.
Failover routing policy – Use when you want to configure active-passive failover.
Geolocation routing policy – Use when you want to route traffic based on the location of your users.
Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
Latency routing policy – Use when you have resources in multiple AWS Regions, and you want to route traffic to the region that provides the best latency.
Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify.

You can use Route 53 health checks to configure active-active and active-passive failover configurations. You configure active-active failover using any routing policy (or combination of routing policies) other than failover, and you configure active-passive failover using the failover routing policy.

Use an active-passive failover configuration when you want a primary resource or group of resources to be available the majority of the time, and you want a secondary resource or group of resources to be on standby in case all the primary resources become unavailable. When responding to queries, Route 53 includes only the “healthy primary” resources. If all the primary resources are unhealthy, Route 53 begins to include only the healthy secondary resources in response to DNS queries.
This way, you can create a failover routing policy that will direct traffic to the backup region when your primary region fails.
Amazon EC2 Auto Scaling integrates with Elastic Load Balancing to enable you to insert one or more Application Load Balancer, Network Load Balancer, or Gateway Load Balancer with multiple target groups in front of your Auto Scaling group.
Creating an Application Load Balancer on each region with an Auto Scaling group that spans multiple Availability Zones ensures that your application will be highly available and will scale based on the user traffic.
Therefore, the correct answer is: Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create record entries in Amazon Route 53 pointing to the ALBs with health check enabled and a failover routing policy.
The option that says: Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB is incorrect because an Auto Scaling group cannot span AZs on multiple regions, and the Application Load Balancer cannot serve traffic to EC2 instances on a different region even with Inter-Region VPC peering.
The option that says: Configure an Inter-Region VPC peering between the us-west-1 VPC and a new VPC in the us-east-1 region. Create an Application Load Balancer (ALB) that spans multiple Availability Zones (AZs) on both VPCs. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs of both regions and place it behind the ALB. Create an Alias record entry in Amazon Route 53 that points to the DNS name of the ALB is incorrect because an Application Load Balancer cannot span to multiple regions, only multiple AZs on the same region. An Auto Scaling group also cannot span multiple regions as it can only deploy EC2 instances in one region.
The option that says: Create an Application Load Balancer (ALB) in the us-west-1 region that spans multiple Availability Zones (AZs) of the VPC. Create an Auto Scaling group that will deploy EC2 instances across the multiple AZs and place it behind the ALB. Set up the same configuration to the us-east-1 region VPC. Create separate record entries for each region’s ALB on Amazon Route 53 and enable health checks to ensure high-availability for both regions is incorrect. Although this setup is possible, it does not mention the routing policy to be used on Amazon Route 53. The question requires that the second region acts as a passive backup, which means only the main region receives all the traffic so you need to specifically use a failover routing policy in Amazon Route 53.

References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html

Check out the Amazon Route 53 Cheat Sheet:
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q48"></a>

## Q48

A hospital chain in London uses an online central hub for its doctors and nurses. The application interacts with millions of requests per day to fetch various medical data of their patients. The system is composed of a web tier, an application tier, and a database tier that receives large and unpredictable traffic demands. The Solutions Architect must ensure that this infrastructure is highly-available and scalable enough to handle web traffic fluctuations automatically. 
Which of the following options should the solutions architect implement to meet the above requirements?

- **A.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas.
- **B.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **C.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **D.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** unpredictable traffic; HA and auto scaling all tiers

⚠️ **Watch:** Stateful instances break scaling

🧠 **Rule:** Stateless tiers + ElastiCache for state + RDS Multi-AZ with read replicas.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Web tier ── App tier ── DB tier
  │             │           │
 ASG           ASG       RDS
Traffic: large + unpredictable
Yêu cầu: HA + auto-scale mọi tầng
```

Bốn lựa chọn khác nhau ở 3 trục: **stateful vs stateless** instance, **có/không có caching** cho tier sync, và **RDS Read Replica + Multi-AZ hay chỉ một trong hai**. Đáp án đúng: **D** — stateless + ElastiCache Serverless + RDS Read Replicas **và** Multi-AZ. Anh chọn đúng D.

#### Vì sao D đúng

- **Stateless web/app tier**: với traffic "lớn và không thể đoán trước", instance phải **stateless** để Auto Scaling group có thể scale-in/scale-out tự do — bất kỳ instance nào cũng xử lý được request tiếp theo, không cần biết lịch sử phiên trước.
- **Amazon ElastiCache Serverless**: dùng để đồng bộ dữ liệu session/trạng thái giữa các tier thay vì lưu trong instance → giữ instance stateless mà vẫn chia sẻ được thông tin dùng chung.
- **RDS Read Replicas + Multi-AZ cùng lúc**: đây là điểm khác biệt chính so với các lựa chọn khác — **Read Replicas xử lý workload đọc nhiều** (fetch dữ liệu bệnh nhân khổng lồ mỗi ngày), **Multi-AZ đảm bảo high availability** khi một AZ gặp sự cố. Hai cơ chế **giải quyết hai vấn đề khác nhau** (scale đọc vs HA) nên cần **cả hai**, không phải chọn một.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng **stateful instance** (phá vỡ khả năng auto scale linh hoạt) và chỉ dùng **Read Replicas** (không có Multi-AZ → thiếu HA).
- **B sai** cùng lỗi stateful, và chỉ có **Multi-AZ** (không có Read Replica → DB vẫn là bottleneck cho lượng đọc lớn, vì Multi-AZ không cải thiện read performance).
- **C sai** vì dùng stateless + ElastiCache đúng, nhưng DB tier **chỉ có Multi-AZ, thiếu Read Replicas** — Multi-AZ chỉ cải thiện Availability, không cải thiện khả năng đọc dữ liệu lớn như đề yêu cầu ("millions of requests per day to fetch data").

#### So sánh nhanh

| Đáp án | Instance | Caching | RDS |
|---|---|---|---|
| **D (đúng)** | Stateless | ElastiCache Serverless | Read Replicas + Multi-AZ |
| C | Stateless | ElastiCache Serverless | Chỉ Multi-AZ |
| B | Stateful | Không | Chỉ Multi-AZ |
| A | Stateful | Không | Chỉ Read Replicas |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** **RDS Multi-AZ không cải thiện read throughput** — nó chỉ tạo bản sao đồng bộ (synchronous) dùng cho failover, standby không phục vụ query đọc thông thường. Muốn tăng khả năng đọc, phải dùng **Read Replicas** (bản sao bất đồng bộ, phục vụ SELECT). Đề thi hay đưa 2 lựa chọn "chỉ Multi-AZ" hoặc "chỉ Read Replica" làm mồi nhử — thực tế khi cả HA và scale-đọc đều cần, phải chọn đáp án có **cả hai**.

#### Quy tắc nhớ cho thi

- **"Unpredictable traffic + cần auto scale"** → instance phải **stateless**
- **State cần share giữa instance** → **ElastiCache** (không lưu trong local instance)
- **"Đọc nhiều + cần HA"** → RDS cần **cả Read Replicas (đọc) và Multi-AZ (HA)**, không phải chỉ một
- **Multi-AZ** ≠ tăng read performance; **Read Replica** ≠ tự động failover thành primary

### TD explanation

When users or services interact with an application, they will often perform a series of interactions that form a session. A session is unique data for users that persists between requests while they use the application. A stateless application is an application that does not need knowledge of previous interactions and does not store session information.

For example, an application that, given the same input, provides the same response to any end user, is a stateless application. Stateless applications can scale horizontally because any of the available compute resources (such as EC2 instances and AWS Lambda functions) can service any request. Without stored session data, you can simply add more compute resources as needed. When that capacity is no longer required, you can safely terminate those individual resources, after running tasks have been drained. Those resources do not need to be aware of the presence of their peers—all that is required is a way to distribute the workload to them.
In this scenario, the best option is to use a combination of Amazon ElastiCache Serverless, Cloudwatch, and RDS Read Replica.
Therefore, the correct answer is: Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled. It uses stateless instances. The web server uses ElastiCache Serverless for read operations and relies on CloudWatch for monitoring traffic fluctuations. When variations in traffic occur, CloudWatch notifies the autoscaling group to perform scale-in or scale-out actions accordingly. ElastiCache Serverless is a robust cache solution that ensures high availability by automatically replicating data across multiple Availability Zones. Furthermore, it leverages read replicas for RDS to efficiently handle read-heavy workloads and utilizes Multi-AZ configurations to ensure high availability.
The option that says: Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled is incorrect because it uses stateful instances. It also does not use any caching mechanism for web and application tiers, and multi-AZ RDS does not improve read performance.
The option that says: Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas is incorrect because it uses stateful instances and it does not use any caching mechanism for web and application tiers.
The option that says: Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled. is incorrect because multi-AZ RDS only improves Availability, not read performance.

References:
https://aws.amazon.com/elasticache/
https://aws.amazon.com/rds/details/read-replicas/
https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/amazon-elasticache/
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q63"></a>

## Q63

A company hosts a stateful licensing application on an Amazon EC2 instance.
The application is tied to the instance’s existing network configuration, and client systems must continue connecting to the same IP address after recovery. The company wants the instance to recover automatically when the underlying AWS hardware fails.
Which solution will meet the given requirements?

- **A.** Configure an Amazon CloudWatch alarm to invoke an AWS Lambda function that runs the aws ec2 reboot-instances command whenever the EC2 instance reports a system status check failure.
- **B.** Associate an Elastic IP address with the EC2 instance and configure an Amazon CloudWatch alarm to stop and start the instance after a system status check failure.
- **C.** Configure an Amazon CloudWatch alarm that monitors the StatusCheckFailed_System metric and triggers the EC2 instance recovery action.
- **D.** Use AWS Systems Manager Automation to patch the EC2 instance when the system status check fails.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** keep same IP after hardware failure; auto recovery

⚠️ **Watch:** Stop/start may change host and private IP behavior; reboot doesn't move hosts

🧠 **Rule:** StatusCheckFailed_System alarm → EC2 recover action (keeps IPs, metadata).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Stateful licensing app trên 1 EC2 instance
Client luôn kết nối tới CÙNG MỘT IP
AWS hardware bên dưới gặp lỗi (hardware failure)
   → cần instance TỰ ĐỘNG recover, giữ nguyên cấu hình network
```

Yêu cầu chốt: recovery phải **tự động**, và instance phải giữ nguyên **instance ID, private IP, Elastic IP** sau khi phục hồi. Đáp án đúng: **C** — CloudWatch alarm theo dõi **StatusCheckFailed_System** để trigger **EC2 recovery action**. Anh chọn đúng C.

#### Vì sao C đúng

- **StatusCheckFailed_System** là metric chuyên biệt để phát hiện lỗi ở **tầng hạ tầng AWS** (hardware/host), khác với StatusCheckFailed_Instance (lỗi ở tầng OS/instance).
- **EC2 recovery action** (gắn trực tiếp vào CloudWatch alarm) sẽ **tự động di chuyển instance sang host vật lý khác** mà vẫn **giữ nguyên instance ID, private IP address, và Elastic IP** — đúng chính xác yêu cầu "client phải tiếp tục connect vào cùng IP sau khi recover".
- Đây là cơ chế **native, tự động hoàn toàn**, không cần Lambda hay script trung gian — đúng yêu cầu "recover automatically".

#### Vì sao từng đáp án sai bị loại

- **A sai** vì lệnh **`reboot-instances`** chỉ khởi động lại instance **trên cùng host vật lý đang lỗi** — không giải quyết được vấn đề hardware failure, vì phần cứng hỏng vẫn còn đó.
- **B sai** vì **stop/start** instance sẽ đưa nó lên **host mới** (đúng hướng), và Elastic IP vẫn giữ được IP public — nhưng đây là giải pháp **thủ công/gián tiếp** (phải tự dựng CloudWatch alarm gọi stop rồi start), kém tin cậy hơn recovery action native, và theo TD "disrupts the ephemeral state" — tức có thể mất dữ liệu ephemeral (như instance store) trong quá trình stop/start.
- **D sai** vì **Systems Manager patch** chỉ xử lý lỗi **software/OS-level** — một status check failure ở tầng **System (hardware)** thì patch OS hoàn toàn không liên quan, không giải quyết được gốc vấn đề.

#### So sánh nhanh

| Đáp án | Cơ chế | Giữ IP? | Tự động? | Giải quyết hardware failure? |
|---|---|---|---|---|
| **C (đúng)** | CloudWatch alarm + EC2 recovery action | ✅ (instance ID, private IP, EIP) | ✅ | ✅ — di chuyển sang host mới |
| B | Stop/start qua alarm | ✅ (chỉ EIP, nhờ gán sẵn) | Có cấu hình nhưng gián tiếp | ✅ nhưng kém tin cậy, mất ephemeral state |
| A | Lambda gọi reboot | — | ✅ | ❌ — reboot vẫn trên host hỏng |
| D | SSM patch | — | ✅ | ❌ — patch không fix hardware |

#### Lưu ý thực tế

⚠️ **Dễ nhầm:** `StatusCheckFailed_System` (lỗi hạ tầng AWS) khác hẳn `StatusCheckFailed_Instance` (lỗi OS/cấu hình bên trong instance) — chỉ loại đầu mới cần đến **EC2 recovery action** (di chuyển host). Ngoài ra, **stop/start** đưa instance lên host mới giống recovery, nhưng **private IP sẽ bị đổi nếu không dùng Elastic IP** — còn recovery action native thì **giữ nguyên cả private IP** mà không cần Elastic IP.

#### Quy tắc nhớ cho thi

- **"Giữ nguyên IP sau khi hardware failure, cần tự động"** → **CloudWatch alarm + StatusCheckFailed_System + EC2 recovery action**
- **Reboot** → chỉ fix lỗi mềm, **không di chuyển host**, vô dụng với hardware failure
- **Stop/start** → có thể dùng tạm nhưng là giải pháp thủ công, kém hơn recovery action native
- **SSM patching** → chỉ dành cho lỗi OS/software, không liên quan tới hardware check

### TD explanation

If AWS detects that an instance is unavailable due to an underlying hardware or software issue, CloudWatch action-based recovery can automatically restore the instance’s availability by migrating it from the affected host to a different host.

You can configure CloudWatch action-based recovery to add recovery actions to Amazon CloudWatch alarms. CloudWatch action-based recovery works with the StatusCheckFailed_System metric. CloudWatch action-based recovery provides to-the-minute recovery response time granularity and Amazon Simple Notification Service (Amazon SNS) notifications of recovery actions and outcomes.

These configuration options enable quicker recovery attempts and provide more precise control over how the system responds to status check failures, compared to simplified automatic recovery.
Hence, the correct answer is: Configure an Amazon CloudWatch alarm that monitors the StatusCheckFailed_System metric and triggers the EC2 instance recovery action. The recovery action automatically moves the instance to healthy hardware while preserving the instance ID, private IP, and Elastic IP. This ensures the licensing application continues to use the same network configuration, and client systems can reconnect seamlessly.
The option that says: Associate an Elastic IP address with the EC2 instance and configure an Amazon CloudWatch alarm to stop and start the instance after a system status check failure is incorrect because stopping and starting the instance will launch it on new hardware, but this disrupts the ephemeral state and is not the intended automatic recovery mechanism. While the Elastic IP ensures the same public IP, this approach is manual and less reliable compared to the native recovery action.
The option that says: Use AWS Systems Manager Automation to patch the EC2 instance when the system status check fails is incorrect because patching typically addresses software or OS-level issues, not hardware failures. A system status check failure indicates underlying AWS hardware problems, which patching cannot resolve.
The option that says: Configure an Amazon CloudWatch alarm to invoke an AWS Lambda function that runs the aws ec2 reboot-instances command whenever the EC2 instance reports a system status check failure is incorrect because rebooting the instance only restarts it on the same faulty hardware. This does not resolve system-level failures and does not guarantee recovery.

References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cloudwatch-recovery.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html

Check out these Amazon EC2 and Amazon CloudWatch Cheat Sheets:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/
https://tutorialsdojo.com/amazon-cloudwatch/

</details>

---

# Group D — Networking (5)

<a id="q39"></a>

## Q39

A company is using AWS Managed Active Directory Service to host the company AD in the AWS Cloud with a custom AD domain name private.tutorialsdojo.com. A pair of domain controllers are launched with the default configuration inside the VPC. A VPC interface endpoint was also created for the Amazon Kinesis using AWS Private Link to allow instances to connect to Kinesis service endpoints from inside the VPC. The solutions architect launched several EC2 instances in the VPC, however, the instances were not able to resolve the company’s custom AD domain name.
Which of the following steps should the Solutions Architect implement to allow the instances to resolve both AWS VPC endpoints and the AWS Managed Microsoft AD domain’s FQDN? (Select TWO.)

- **A.** Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.
- **B.** Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.
- **C.** Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries.
- **D.** Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.
- **E.** Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D (you answered correctly)

🔑 **Key words:** resolve both VPC endpoints and AD domain FQDN (Select TWO)

⚠️ **Watch:** Inbound endpoint is for on-prem → AWS queries

🧠 **Rule:** Route 53 Resolver outbound endpoint + forwarding rule to AD DNS; keep AmazonProvidedDNS.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC
┌─────────────────────────────────────────────────────┐
│ EC2 instances                                         │
│    │  cần resolve:                                    │
│    │   1) private.tutorialsdojo.com (AD domain FQDN)   │
│    │   2) VPC interface endpoint (Kinesis via PrivateLink)│
│    ▼                                                   │
│ Route 53 Resolver (AmazonProvidedDNS)                  │
└─────────────────────────────────────────────────────┘
      Domain controllers (AWS Managed Microsoft AD) trong VPC
Yêu cầu: resolve CẢ HAI loại domain (Select TWO)
```

Đáp án đúng: **A + D**. Anh chọn đúng cả hai.

#### Vì sao A + D đúng — outbound endpoint và forwarding rule là hai nửa của một giải pháp

```
Route 53 Resolver (AmazonProvidedDNS mặc định của VPC)
      │
      ├── tự resolve: VPC-local domain, private hosted zone, VPC endpoint  ✓ (có sẵn)
      │
      └── domain KHÁC (private.tutorialsdojo.com) → cần forward ra ngoài
                │
                ▼
        Outbound Endpoint (D)  ─── tạo trên Route 53 console
                │
                ▼
        Forwarding Rule (A) ─── forward query private.tutorialsdojo.com
                │              tới IP của 2 domain controllers
                ▼
        AD domain controllers trả lời FQDN
```

- **D (Outbound Endpoint)** là hạ tầng bắt buộc để Resolver có thể gửi query ra ngoài VPC-local domain tới DNS resolver khác (ở đây là domain controllers của AD).
- **A (Forwarding Rule)** là luật cụ thể đặt trên outbound endpoint: query nào khớp `private.tutorialsdojo.com` thì forward tới IP của domain controllers.

Khi có cả hai, AmazonProvidedDNS vẫn giữ nguyên là DNS resolver của VPC — Resolver tự biết: domain AD thì forward theo rule, còn VPC endpoint và các domain AWS khác vẫn tự resolve như bình thường (vì đó là khả năng có sẵn của Resolver, không cần cấu hình thêm).

#### Vì sao từng đáp án sai bị loại

- **B — "Conditional forwarder inside the endpoint":** sai vị trí cấu hình — **conditional forwarder được cấu hình bên trong chính AD server**, không phải trên Route 53 Resolver endpoint. Route 53 side dùng "forwarding rule", không phải "conditional forwarder".
- **C — Tự cấu hình split DNS trên từng client:** khả thi về lý thuyết nhưng tạo quá nhiều **operational overhead** — phải sửa DNS config trên từng instance thủ công, trong khi outbound endpoint + forwarding rule làm việc này tập trung, tự động cho toàn VPC.
- **E — Inbound Endpoint:** sai chiều hoàn toàn — **Inbound Endpoint dùng để on-premises network query vào AWS resource**, không phải để VPC resolve ra domain bên ngoài VPC-local.

#### So sánh nhanh

| Loại endpoint | Chiều resolve | Dùng khi nào |
|---|---|---|
| **Outbound Endpoint (D)** | VPC → domain bên ngoài VPC-local (AD, on-prem) | VPC cần resolve custom domain |
| Inbound Endpoint (E) | On-premises → AWS resource | Mạng ngoài cần resolve tên trong VPC |

#### Lưu ý thực tế

- Nếu nhiều forwarding rule cùng khớp một query (ví dụ `tutorialsdojo.com` và `portal.tutorialsdojo.com`), Resolver luôn chọn **rule khớp cụ thể nhất** (most specific match) để forward.
- Instance vẫn khai báo DNS resolver là **AmazonProvidedDNS** như cũ — không cần đổi DNS server trên từng client, vì toàn bộ logic forward nằm ở outbound endpoint + rule.

#### Quy tắc nhớ cho thi

- **"VPC cần resolve domain AD/on-prem + vẫn giữ AmazonProvidedDNS"** → **Outbound Endpoint + Forwarding Rule**
- **"Conditional forwarder"** → cấu hình trong AD server, không phải trên Route 53 Resolver
- **"On-prem cần resolve tên trong AWS"** → Inbound Endpoint, chiều ngược lại với bài này

### TD explanation

When you create a VPC using Amazon VPC, Route 53 Resolver automatically answers DNS queries for local VPC domain names for EC2 instances (ec2-192-0-2-44.compute-1.amazonaws.com) and records in private hosted zones (private.tutorialsdojo.com). For all other domain names, Resolver performs recursive lookups against public name servers.
You also can integrate DNS resolution between Resolver and DNS resolvers on your network by configuring forwarding rules. Your network can include any network that is reachable from your VPC, such as the following:

The VPC itself
Another peered VPC
An on-premises network that is connected to AWS with AWS Direct Connect, a VPN, or a network address translation (NAT) gateway.

A Route 53 Resolver Endpoint is a customer-managed resolver consisting of one or more Elastic Network Interfaces (ENIs) deployed on your VPC. Resolver Endpoints are classified into two types:

Inbound Endpoint – provides DNS resolution of AWS resources, such as EC2 instances, for your corporate network.
Outbound Endpoint – provides resolution of specific DNS names that you configure using forwarding rules to your VPC.

Outbound Resolver Endpoints host Forwarding Rules that forward queries for specified domain names to specific IP addresses. You create forwarding rules when you want to forward DNS queries for specified domain names to DNS resolvers on your network.
To forward selected queries, you create Resolver rules that specify the domain names for the DNS queries that you want to forward (such as example.com), and the IP addresses of the DNS resolvers on your network that you want to forward the queries to. If a query matches multiple rules (tutorialsdojo.com, portal.tutorialsdojo.com), the Resolver chooses the rule with the most specific match (portal.tutorialsdojo.com) and forwards the query to the IP addresses that you specified in that rule.

When Outbound Endpoint and Forwarding Rule are created, any resource in the VPC that queries the AmazonProvidedDNS as its DNS resolver is able to seamlessly resolve for AWS Managed Microsoft AD domain’s FQDN, as well as any AWS resources on the VPC such as (interface) VPC Endpoints.
The option that says: Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC is correct. You need an outbound endpoint to forward and resolve custom domain names inside your VPC.
The option that says: Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers is correct. The forwarding rules will handle queries for a given DNS domain and forward them to the AD server to resolve them.
The option that says: Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC is incorrect. An inbound endpoint is used for DNS resolution of AWS services. You need an outbound endpoint for this scenario.
The option that says: Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries is incorrect. It is not recommended to manually configure resources to split DNS queries. This entails a lot of management overhead. You just need to set the Active Directory servers as the DNS servers and the requests will be forwarded to the VPC resolver accordingly.
The option that says: Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers is incorrect. A conditional forwarder is configured inside the AD servers, not on the Route 53 resolver endpoint.
References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-configuring
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html
https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/

Check out these Amazon VPC and Amazon Route 53 Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q51"></a>

## Q51

An online gambling site is hosted in two Elastic Compute Cloud (EC2) instances inside a Virtual Private Cloud (VPC) in the same Availability Zone (AZ) but in different subnets. The first EC2 instance is running a database and the other EC2 instance is a web application that fetches data from the database. You are required to ensure that the two EC2 instances can connect with each other in order for your application to work properly. You also need to track historical changes to the security configurations associated to your instances.
Which of the following options below can meet this requirement? (Select TWO.)

- **A.** Check and configure the network ACL to allow communication between the two subnets. Ensure that the security groups allow the application host to talk to the database on the right port and protocol.
- **B.** Use AWS Config to track historical changes to the security configurations associated to your instances.
- **C.** Use Route 53 to ensure that there is proper routing between the two subnets.
- **D.** Use AWS Systems Manager to track historical changes to the security configurations associated to your instances.
- **E.** Ensure that the default route is set to a NAT instance or Internet Gateway (IGW).

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B (you answered correctly)

🔑 **Key words:** two subnets can't talk; track SG changes (Select TWO)

⚠️ **Watch:** Route 53 doesn't route between subnets

🧠 **Rule:** Fix NACL + SG; AWS Config for configuration history.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC, cùng Availability Zone
┌──────────────────┐        ┌──────────────────┐
│ Subnet A          │        │ Subnet B          │
│  EC2: database    │ ◄────► │ EC2: web app      │
└──────────────────┘        └──────────────────┘
Hai yêu cầu:
  1) Hai instance phải connect được với nhau
  2) Phải TRACK lịch sử thay đổi của security config (Select TWO)
```

Đáp án đúng: **A + B**. Anh chọn đúng cả hai.

#### Vì sao A đúng — NACL + Security Group là nơi quyết định traffic đi được hay không

```
Web app (Subnet B) ──► Network ACL của Subnet A/B (cho phép traffic giữa 2 subnet)
                   ──► Security Group của DB instance (cho phép port/protocol đúng)
                   ──► DB instance (Subnet A)
```

Hai instance nằm ở hai subnet khác nhau trong cùng VPC/AZ thì về routing mặc định đã thông nhau (route table local); vấn đề connect được hay không nằm ở **tầng filtering**: Network ACL (chặn/cho phép theo subnet) và Security Group (chặn/cho phép theo instance, theo port/protocol cụ thể). Cả hai phải được cấu hình đúng cùng lúc.

#### Vì sao B đúng — AWS Config là dịch vụ chuyên biệt cho lịch sử cấu hình

```
EC2 instance / Security Group
        │
        ▼
   AWS Config
        │ liên tục record configuration
        ▼
   Configuration history + compliance evaluation
```

AWS Config được thiết kế đúng cho yêu cầu "track historical changes to security configurations" — nó liên tục ghi nhận thay đổi cấu hình resource (bao gồm Security Group rules) và cho phép xem lại lịch sử, đánh giá compliance.

#### Vì sao từng đáp án sai bị loại

- **C — Route 53 để routing giữa hai subnet:** Route 53 là DNS service, **không có khả năng routing network giữa các subnet** — việc đó thuộc về route table (đã có sẵn, local route) và NACL/Security Group cho filtering.
- **D — AWS Systems Manager để track lịch sử security config:** Systems Manager phục vụ quản lý vận hành (patch, session, automation...), **không phải công cụ theo dõi lịch sử thay đổi cấu hình** — đúng việc này phải dùng AWS Config.
- **E — NAT instance/Internet Gateway (IGW):** không cần thiết cho giao tiếp NỘI BỘ giữa hai instance trong VPC — NAT/IGW chỉ liên quan khi cần đi ra Internet, không liên quan đến traffic giữa hai subnet private.

#### So sánh nhanh

| Lựa chọn | Giải quyết connectivity? | Giải quyết audit history? |
|---|---|---|
| **A. NACL + SG** | Có | — |
| **B. AWS Config** | — | Có |
| C. Route 53 | Không (DNS, không routing) | — |
| D. Systems Manager | — | Không (sai dịch vụ) |
| E. NAT/IGW | Không (chỉ cho Internet-bound traffic) | — |

#### Lưu ý thực tế

- Security Group là **stateful** và hoạt động ở tầng instance; Network ACL là **stateless** và hoạt động ở tầng subnet — trong hầu hết trường hợp Security Group đủ dùng, nhưng NACL là lớp bảo vệ bổ sung khi cần kiểm soát ở cấp subnet.
- AWS Config không chỉ lưu lịch sử mà còn so sánh với "desired configuration" để đánh giá compliance — hữu ích hơn việc chỉ xem log thủ công.

#### Quy tắc nhớ cho thi

- **"Hai instance cùng VPC khác subnet không connect được"** → kiểm tra Network ACL (subnet-level) + Security Group (instance-level)
- **"Track lịch sử thay đổi cấu hình security"** → **AWS Config**, không phải Systems Manager
- **Route 53 / NAT / IGW** → không liên quan đến connectivity nội bộ giữa subnet trong cùng VPC

### TD explanation

AWS provides two features that you can use to increase security in your VPC: security groups and network ACLs. Security groups control inbound and outbound traffic for your instances, and network ACLs control inbound and outbound traffic for your subnets. In most cases, security groups can meet your needs; however, you can also use network ACLs if you want an additional layer of security for your VPC.

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting.
The option that says: Check and configure the network ACL to allow communication between the two subnets. Ensure that the security groups allow the application host to talk to the database on the right port and protocol is correct. NACLs and security groups act like firewalls for communication within your instances and subnets.
The option that says: Use AWS Config to track historical changes to the security configurations associated to your instances is correct. AWS Config can help you maintain compliance with your security setting by monitoring and detecting violations on your security groups depending on the rules you have specified.
The option that says: Use Route 53 to ensure that there is proper routing between the two subnets is incorrect. Route 53 can’t be used to connect two subnets. You should use Network ACLs and Security Groups instead.
The option that says: Ensure that the default route is set to NAT instance or Internet Gateway (IGW) is incorrect. Neither a NAT instance nor an Internet gateway is needed for the two EC2 instances to communicate.
The option that says: Use AWS Systems Manager to track historical changes to the security configurations associated to your instances is incorrect. Using AWS Systems Manager is not suitable to track historical changes to the security configurations associated to your instances. You have to use AWS Config instead.

References:
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html

Check out these Amazon VPC and AWS Config Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/aws-config/

Learn more about AWS Config in this 19-minute video:

</details>

<a id="q52"></a>

## Q52

A company has three AWS accounts each with its own VPCs. There is a requirement for communication between the AWS resources across the accounts, so VPC peering needs to be configured. Please refer to the figure below for details of each VPC:

VPC-B and VPC-C have matching CIDR blocks. For a short-term requirement, VPC-A needs to communicate only with the database instance in VPC-B with an IP address of 10.0.0.77/32 while being able to communicate with all the resources in VPC-C. The Solutions Architect already created the necessary VPC peering links but VPC-A cannot effectively communicate to the VPC-B instance. The Solutions Architect suspects that the routes on each VPC still need proper configuration.
Which of the following solutions will allow VPC-A to communicate with the database instance in VPC-B while being able to communicate with all resources on VPC-C?

- **A.** On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/24) with the target pcx-aaaacccc. Add a network access control list (NACL) on VPC-A to deny all connections to VPC-B except for the IP address 10.0.0.77/32. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc.
- **B.** On VPC-A, add a static route for VPC-B CIDR (10.0.0.77/32) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaacccc.
- **C.** On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc.
- **D.** Enable dynamic route propagation in VPC-A with the peering targets pcx-aaaabbbb and pcx-aaaacccc respectively. On VPC-B, enable dynamic route propagation with peering target pcx-aaaabbbb and add a network acces control list (NACL) that allows only connections to IP address 10.0.0.77/32 from pcx-aaaabbbb. On VPC-C, enable dynamic route propagation with the peering target pcx-aaaacccc.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** VPC-B and VPC-C overlap; VPC-A needs one host in B

⚠️ **Watch:** Overlapping CIDRs need a more specific route

🧠 **Rule:** Longest-prefix match: /32 route to VPC-B host, /16 to VPC-C.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                 VPC-A (172.16.0.0/16)
                       │         │
            pcx-aaaabbbb         pcx-aaaacccc
                 │                     │
       VPC-B (10.0.0.0/16)     VPC-C (10.0.0.0/16)   ← CÙNG CIDR, overlap!
  DB instance: 10.0.0.77/32            (toàn bộ resource)

Yêu cầu: VPC-A chỉ cần nói với MỘT host (10.0.0.77) trong VPC-B,
         nhưng cần nói với TOÀN BỘ VPC-C
```

Đáp án đúng: **B**. Anh chọn đúng B.

#### Vì sao B đúng — longest prefix match giải quyết overlap CIDR

```
VPC-A route table:
  10.0.0.77/32   → pcx-aaaabbbb   (route cụ thể nhất, chỉ 1 host trong VPC-B)
  10.0.0.0/16    → pcx-aaaacccc   (route rộng, cho toàn bộ VPC-C)

VPC-B route table:
  172.16.0.0/16  → pcx-aaaabbbb   (route về lại VPC-A)

VPC-C route table:
  172.16.0.0/16  → pcx-aaaacccc   (route về lại VPC-A)
```

Vì VPC-B và VPC-C có CIDR **trùng nhau** (10.0.0.0/16), VPC-A không thể có hai route cùng đích 10.0.0.0/16 chỉ tới hai peering connection khác nhau — sẽ xung đột. Giải pháp là dùng **longest prefix match**: route `/32` (cụ thể nhất, chỉ trúng đúng 10.0.0.77) trỏ về VPC-B qua `pcx-aaaabbbb`; mọi traffic khác trong dải `10.0.0.0/16` (route rộng hơn) tự động đi qua `pcx-aaaacccc` tới VPC-C. VPC router luôn ưu tiên route khớp cụ thể nhất.

Lưu ý: vì AWS **không hỗ trợ unicast reverse path forwarding** trong VPC peering, VPC-B và VPC-C vẫn cần có static route riêng trỏ ngược về VPC-A (172.16.0.0/16) qua đúng peering connection của mình — route table của B và C trong đáp án B đã làm đúng việc này.

#### Vì sao từng đáp án sai bị loại

- **A — Route /24 cho cả B và C + thêm NACL để chặn:** route 10.0.0.0/24 trỏ tới cả hai peering connection sẽ **xung đột ngay trên VPC-A** (không rõ traffic đi đường nào); và NACL chỉ có khả năng **chặn (deny) traffic ra**, hoàn toàn không thể "redirect" traffic sang target khác — dùng NACL để sửa vấn đề routing là sai công cụ.
- **C — Route /24 cho B, /16 cho C:** phần route cho VPC-C đúng, nhưng route `10.0.0.0/24` cho VPC-B lại quá rộng — nó bao trùm cả những IP thuộc dải `/24` đó mà thực ra nằm trong VPC-C (vì hai VPC trùng CIDR), khiến traffic đến các IP đó trong VPC-C bị route sai sang VPC-B.
- **D — Dynamic route propagation:** dynamic route propagation chủ yếu dùng cho **Direct Connect hoặc Site-to-Site VPN**, không áp dụng cho VPC peering — peering luôn cần static route; thêm NACL cũng không đúng vai trò routing như đã nói ở A.

#### So sánh nhanh

| Lựa chọn | Route VPC-B | Route VPC-C | Vấn đề |
|---|---|---|---|
| **B. Đúng** | /32 (host cụ thể) | /16 (toàn VPC-C) | Không |
| A | /24 (quá rộng) | /24 (quá rộng) | Xung đột + dùng NACL sai mục đích |
| C | /24 (quá rộng) | /16 | Route B đè lên IP thuộc C |
| D | Dynamic propagation | Dynamic propagation | Sai cơ chế (chỉ dùng cho DX/VPN) |

#### Lưu ý thực tế

- Đây là tình huống kinh điển "partial access with overlapping CIDR" trong VPC peering — AWS chính thức hỗ trợ route tới **một phần CIDR hoặc một instance cụ thể** của VPC peer, không bắt buộc share toàn bộ CIDR.
- Luôn kiểm tra cả ba chiều route (A→B, A→C, và ngược lại) vì thiếu route ngược chiều ở B hoặc C sẽ làm response traffic không về được VPC-A.

#### Quy tắc nhớ cho thi

- **"Hai VPC peer có CIDR trùng nhau, cần route khác nhau cho từng cái"** → dùng **longest prefix match**: route cụ thể hơn (ví dụ /32) ưu tiên trước route rộng hơn
- **NACL** → chỉ chặn (deny), không bao giờ dùng để "redirect" traffic sang peering connection khác
- **Dynamic route propagation** → chỉ cho Direct Connect / VPN, VPC peering luôn cần static route

### TD explanation

You can configure VPC peering connections to provide access to part of the CIDR block, a specific CIDR block (if the VPC has multiple CIDR blocks), or a specific instance within the peer VPC. In this scenario, a central VPC is peered to two or more VPCs that have overlapping CIDR blocks.
You have a central VPC (VPC A) with one subnet, and you have a VPC peering connection between VPC A and VPC B (pcx-aaaabbbb), and between VPC A and VPC C (pcx-aaaacccc). VPC B and VPC C have matching CIDR blocks. You want to use a VPC peering connection pcx-aaaabbbb to route traffic between VPC A and a specific instance in VPC B. All other traffic destined for the 10.0.0.0/16 IP address range is routed through pcx-aaaacccc between VPC A and VPC C.
VPC route tables use the longest prefix match to select the most specific route across the intended VPC peering connection. All other traffic is routed through the next matching route, in this case, across the VPC peering connection pcx-aaaacccc.

If you have a VPC peered with multiple VPCs that have overlapping or matching CIDR blocks, ensure that your route tables are configured to avoid sending response traffic from your VPC to the incorrect VPC. AWS currently does not support unicast reverse path forwarding in VPC peering connections that check the source IP of packets and route reply packets back to the source. You still need to configure static routes on VPC-B and VPC-C going to VPC-A, respectively.
Therefore, the correct answer is: On VPC-A, add a static route for VPC-B CIDR (10.0.0.77/32) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/16) with the target pcx-aaaacccc. The standard VPC peering configuration will be done for VPC-A and VPC-C. As for VPC-B, only the static route to the specific should be configured on VPC-A. AWS will handle the longest prefix match to route the traffic.
The option that says: On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/24) with the target pcx-aaaacccc. Add a network access control list (NACL) on VPC-A to deny all connections to VPC-B except for the IP address 10.0.0.77/32. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc is incorrect. This will only result in a conflict on the routing configuration on VPC-A. Network ACLs can block connections going out of your VPC, however, they can’t redirect connections out to specific targets.
The option that says: Enable dynamic route propagation in VPC-A with the peering targets pcx-aaaabbbb and pcx-aaaacccc respectively. On VPC-B, enable dynamic route propagation with peering target pcx-aaaabbbb and add a network acces control list (NACL) that allows only connections to IP address 10.0.0.77/32 from pcx-aaaabbbb. On VPC-C, enable dynamic route propagation with the peering target pcx-aaaacccc is incorrect. Dynamic route propagation is primarily used for Direct Connection connections or Site-to-Site VPNs. In this scenario, you want to force a specific route to a specific instance on a specific peering target, thus, you need to configure static routes.
The option that says: On VPC-A, add a static route for VPC-B CIDR (10.0.0.0/24) with the target pcx-aaaabbbb and another static route for VPC-C CIDR (10.0.0.0/16) with the target pcx-aaaacccc. On VPC-B, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaabbbb. On VPC-C, add a static route for VPC-A CIDR (172.16.0.0/24) with the target pcx-aaaacccc is incorrect. Route configuration for VPC-A and VPC-C is correct here, however, the route configuration of VPC-A and VPC-B is not. This will make traffic to other instances in the CIDR (10.0.0.0/24), which is under VPC-C, to be routed to VPC-B.

References:
https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html#one-to-two-vpcs-lpm
https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html
https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

<a id="q61"></a>

## Q61

A company has launched a web service in the cloud that analyzes tweets filtered by keywords. This service is hosted on a fleet of on-demand EC2 instances running in multiple Availability Zones with Auto Scaling, and are load-balanced by an application load balancer. After checking the load balancer logs, the solutions architect noticed that on-demand EC2 instances in one of the AZ’s are not receiving requests. 
Which of the following option is the most likely cause of this issue?

- **A.** Multi-AZ autoscaling only works in the North Virginia region.
- **B.** You have to manually add instances in each AZ for them to receive traffic.
- **C.** The availability zone that is not receiving traffic was not associated with the application load balancer.
- **D.** Amazon EC2 Auto scaling does not span multiple availability zones.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** instances in one AZ get no traffic

⚠️ **Watch:** ASG spans AZs fine

🧠 **Rule:** ALB must have that AZ (subnet) enabled.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Application Load Balancer
        │
   ┌────┴────┐
   AZ-1       AZ-2
   EC2 ✓      EC2 ✗ (không nhận request nào)
   (ASG trải nhiều AZ, có traffic)   (ASG trải nhiều AZ, KHÔNG có traffic)
```

Đáp án đúng: **C — AZ đó chưa được associate với Application Load Balancer**. Anh chọn đúng C.

#### Vì sao C đúng

```
ALB chỉ route traffic tới các AZ (subnet) mà nó đã được CẤU HÌNH để dùng
      │
      ▼
Nếu AZ-2 chưa add vào ALB (chưa chọn subnet của AZ-2 khi config ALB)
      │
      ▼
Instance trong AZ-2 dù healthy, dù nằm trong ASG, vẫn KHÔNG nhận traffic
```

Load balancer phải được add Availability Zone (chọn subnet tương ứng) trước khi nó route request tới instance trong AZ đó. Đây là nguyên nhân phổ biến nhất khi "ASG trải nhiều AZ nhưng một AZ không có traffic dù healthy" — vấn đề nằm ở cấu hình ALB, không phải ASG.

#### Vì sao từng đáp án sai bị loại

- **A — "Multi-AZ autoscaling chỉ hoạt động ở N. Virginia":** sai hoàn toàn — Auto Scaling multi-AZ hoạt động ở **mọi region**, không giới hạn region cụ thể nào.
- **B — "Phải thêm instance vào từng AZ thủ công":** sai — Auto Scaling Group tự launch instance vào các AZ đã cấu hình, không cần thêm tay.
- **D — "EC2 Auto Scaling không trải qua nhiều AZ":** sai bản chất — ASG **được thiết kế để trải nhiều AZ** nhằm tăng tính sẵn sàng, đây chính là tính năng cốt lõi của dịch vụ.

#### So sánh nhanh

| Lựa chọn | Nguyên nhân thật của vấn đề? |
|---|---|
| **C. AZ chưa add vào ALB** | Đúng |
| A. Giới hạn region | Sai, không có giới hạn này |
| B. Phải add instance thủ công | Sai, ASG tự quản lý |
| D. ASG không multi-AZ | Sai, ASG hỗ trợ multi-AZ |

#### Lưu ý thực tế

- Khi cross-zone load balancing **tắt**, mỗi load balancer node chỉ route 50% traffic của nó cho target trong AZ riêng của node đó — số target không đều giữa các AZ sẽ dẫn tới tỷ lệ traffic/target không đồng đều (ví dụ 2 target ở AZ-A nhận 25% mỗi target, 8 target ở AZ-B chỉ nhận 6.25% mỗi target).
- Khi cross-zone load balancing **bật**, traffic chia đều cho tất cả target bất kể AZ nào — nên luôn kiểm tra cả hai: (1) AZ đã add vào ALB chưa, (2) cross-zone load balancing bật hay tắt, khi debug traffic phân bổ lệch.

#### Quy tắc nhớ cho thi

- **"Instance trong một AZ không nhận traffic dù ASG khỏe mạnh"** → kiểm tra AZ đó đã được **add vào load balancer** chưa
- **"ASG không hỗ trợ multi-AZ" / "chỉ hoạt động ở N. Virginia"** → luôn là bẫy sai, loại ngay
- Phân bổ traffic lệch giữa AZ → cân nhắc thêm **cross-zone load balancing**

### TD explanation

You can set up your load balancer in EC2-Classic to distribute incoming requests across EC2 instances in a single Availability Zone or multiple Availability Zones. First, launch EC2 instances in all the Availability Zones that you plan to use. Next, register these instances with your load balancer. Finally, add the Availability Zones to your load balancer. After you add an Availability Zone, the load balancer starts routing requests to the registered instances in that Availability Zone. Note that you can modify the Availability Zones for your load balancer at any time. By default, the load balancer routes requests evenly across its Availability Zones. To route requests evenly across the registered instances in the Availability Zones, enable cross-zone load balancing.
If cross-zone load balancing is disabled:

– Each of the two targets in Availability Zone A receives 25% of the traffic.
– Each of the eight targets in Availability Zone B receives 6.25% of the traffic.

This is because each load balancer node can route 50% of its client traffic only to targets in its Availability Zone.

If cross-zone load balancing is enabled, each of the 10 targets receives 10% of the traffic. This is because each load balancer node can route 50% of its client traffic to all 10 targets.
Therefore, the correct answer is: The availability zone that is not receiving traffic was not associated with the application load balancer. Most likely, the reason is that the specific AZ is not added to the ELB.
The option that says: Amazon EC2 Auto Scaling does not span multiple availability zones is incorrect because autoscaling can work with multiple AZs.
The option that says: Multi-AZ autoscaling only works in the North Virginia region is incorrect because autoscaling can be enabled for multi AZ in any single region, not just N. Virginia.
The option that says: You have to manually add instances in each AZ for them to receive traffic is incorrect because instances need not be added manually to AZ.
References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html/
https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html

Check out this AWS Elastic Load Balancing Cheat Sheet:
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

</details>

<a id="q71"></a>

## Q71

An electronics and communications company in Japan has several VPCs in the AWS cloud. It uses NAT instances to allow multiple EC2 instances from the private subnet to initiate connections to the Internet while also restricting any requests coming from the outside network. However, there are numerous incidents where the NAT instance is not available, which affects the batch processing of critical applications. 
Which is the most suitable solution that provides better availability and bandwidth to the current infrastructure with minimal administrative effort?

- **A.** Create a NAT gateway then specify its corresponding subnet and Elastic IP address. Update the route tables of the private subnet to point the Internet traffic to the NAT gateway.
- **B.** Launch two large NAT instances in two separate public subnets and add a route from the private subnet to each NAT instance to make it more fault-tolerant and highly available.
- **C.** Launch a larger NAT instance with the enhanced networking feature enabled to improve the availability and performance of the NAT device.
- **D.** Create an egress-only Internet gateway. Update the route tables of the private subnet to point the Internet traffic to the egress-only Internet gateway.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** NAT instance keeps failing; least effort

⚠️ **Watch:** Egress-only IGW is for IPv6

🧠 **Rule:** Replace NAT instances with NAT Gateway (per AZ).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Private subnet
┌──────────────┐
│ EC2 instances │ ──► NAT instance (hay bị down) ──► Internet
└──────────────┘
Yêu cầu: tăng availability + bandwidth, MINIMAL administrative effort
```

Đáp án đúng: **A — NAT Gateway, update route table trỏ Internet traffic qua NAT Gateway**. Anh chọn đúng A.

#### Vì sao A đúng

```
NAT Gateway (managed service của AWS)
      │  tự có HA trong AZ, băng thông scale tự động
      ▼
Private subnet route table → đích Internet → target: NAT Gateway
```

AWS khuyến nghị **NAT Gateway thay cho NAT instance** chính vì hai lý do đề bài yêu cầu: (1) availability và bandwidth tốt hơn — NAT Gateway là managed service, không phải một EC2 instance đơn lẻ có thể down; (2) **không cần admin effort** — không phải patch OS, không phải scale size thủ công như NAT instance.

#### Vì sao từng đáp án sai bị loại

- **B — Hai NAT instance ở hai subnet, route riêng tới từng NAT instance:** đúng là high availability và fault-tolerant hơn một NAT instance, nhưng đòi hỏi **rất nhiều effort quản lý** — phải tự theo dõi health, failover, patch OS cho cả hai instance; ngược hẳn với yêu cầu "minimal administrative effort".
- **C — NAT instance lớn hơn + enhanced networking:** chỉ cải thiện performance của **một component đơn lẻ**, vẫn là single point of failure — nếu instance đó down, không có gì thay thế, nên vẫn không đạt yêu cầu "better availability".
- **D — Egress-only Internet Gateway:** sai mục đích — egress-only IGW chỉ dùng cho **IPv6 traffic**, đề bài không nói gì về IPv6, nên không áp dụng.

#### So sánh nhanh

| Lựa chọn | Availability | Bandwidth | Admin effort |
|---|---|---|---|
| **A. NAT Gateway** | Cao (managed) | Tự scale | Thấp nhất |
| B. Hai NAT instance | Cao (nếu config đúng) | Giới hạn theo instance size | Cao (quản lý thủ công) |
| C. NAT instance lớn hơn | Vẫn là SPOF | Cải thiện một phần | Trung bình |
| D. Egress-only IGW | — | — | Sai use case (chỉ cho IPv6) |

#### Lưu ý thực tế

- NAT Gateway được tạo **theo từng subnet/AZ** và gắn Elastic IP — nếu muốn HA across AZ thực sự, nên có một NAT Gateway cho mỗi AZ, nhưng xét trong phạm vi câu hỏi, chỉ cần chuyển từ NAT instance sang NAT Gateway đã giải quyết đúng yêu cầu.
- Egress-only Internet Gateway thường bị nhầm là "phiên bản an toàn hơn" của NAT, nhưng bản chất nó chỉ là tương đương NAT cho **IPv6**, không thay thế NAT Gateway/instance cho IPv4.

#### Quy tắc nhớ cho thi

- **"NAT instance hay down, cần tăng availability, ít effort"** → **NAT Gateway**
- **Egress-only Internet Gateway** → chỉ dành cho IPv6, không áp dụng cho bài toán NAT IPv4
- **Nhiều NAT instance để HA** → về lý thuyết đúng nhưng luôn sai vì "nhiều administrative effort" khi đề yêu cầu minimal effort

### TD explanation

You can use a NAT device to enable instances in a private subnet to connect to the internet (for example, for software updates) or other AWS services, but prevent the internet from initiating connections with the instances. A NAT device forwards traffic from the instances in the private subnet to the internet or other AWS services, and then sends the response back to the instances. When traffic goes to the internet, the source IPv4 address is replaced with the NAT device’s address and similarly, when the response traffic goes to those instances, the NAT device translates the address back to those instances’ private IPv4 addresses.

AWS offers two kinds of NAT devices—a NAT gateway or a NAT instance. It is recommended to use NAT gateways, as they provide better availability and bandwidth over NAT instances. The NAT Gateway service is also a managed service that does not require your administration efforts.
A NAT instance is launched from a NAT AMI and you can choose to use a NAT instance for special purposes. However, this type of NAT device is limited and is not highly available compared with a NAT Gateway.
Therefore, the correct answer is: Create a NAT gateway then specify its corresponding subnet and Elastic IP address. Update the route tables of the private subnet to point the Internet traffic to the NAT gateway.
The option that says: Launch a larger NAT instance with the enhanced networking feature enabled to improve the availability and performance of the NAT device is incorrect. Even if you upgrade your NAT device to a larger instance, it would still be a single component. This means that if your NAT instance goes down, there would be no other instance to handle the requests, which means that your architecture is not highly available. It is better to use a NAT Gateway to provide better availability and bandwidth for your infrastructure.
The option that says: Launch two large NAT instances in two separate public subnets and add a route from the private subnet to each NAT instance to make it more fault-tolerant and highly available is incorrect. Although this solution is indeed highly available and fault-tolerant, this entails a lot of administrative effort to manage those two NAT instances. Hence, it is still better to use the NAT Gateway service since it is a managed service that does not require administrative effort.
The option that says: Create an egress-only Internet gateway. Update the route tables of the private subnet to point the Internet traffic to the egress-only Internet gateway is incorrect because an egress-only Internet gateway is primarily used to handle IPv6 traffic, which is not mentioned in this scenario.
References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

---

# Group E — Service fit (serverless, data, app design) (12)

<a id="q8"></a>

## Q8

A software development company implements cloud best practices on its AWS infrastructure. The solutions architect has been instructed to manage its AWS cloud Infrastructure as code (IAC) to automate its software build, test, and deploy process. The company follows a continuous integration and continuous delivery (CI/CD) practice to streamline its software development lifecycle. The company already uses AWS CodeArtifact to store and version its private software packages.
The company would like to have the ability to easily deploy exact copies of different versions of its cloud infrastructure, stage changes into different environments, revert back to previous versions, and identify the specific versions running in the VPC. Plus, all new public-facing applications should also have a global content delivery network (CDN) service.
Which of the following options is the recommended action to meet the company requirement?

- **A.** Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.
- **B.** Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture.
- **C.** Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.
- **D.** Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** IaC versions, stage, revert; global CDN

⚠️ **Watch:** CloudWatch is not a CDN

🧠 **Rule:** CloudFormation + CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Yêu cầu công ty:
  - Quản lý hạ tầng cloud bằng Infrastructure as Code (IaC)
  - Deploy lại y hệt từng version, stage sang env khác, revert khi cần,
    biết rõ version nào đang chạy trong VPC
  - App public-facing mới → cần CDN toàn cầu

Đáp án đúng: C (AWS CloudFormation quản lý hạ tầng + Amazon CloudFront làm CDN)
Anh chọn đúng C.
```

Đề không hỏi về CodeArtifact hay CI/CD pipeline cụ thể — đó chỉ là ngữ cảnh. Từ khoá quyết định là **"manage cloud infrastructure as code"** + **"global CDN"**.

#### Vì sao C đúng

**AWS CloudFormation** mô tả toàn bộ resource hạ tầng bằng một file text (template) — đây chính là "single source of truth". Vì hạ tầng được code hoá:

```
Template (JSON/YAML)
    → tạo stack mới   = "deploy exact copies of different versions"
    → update stack    = "stage changes into different environments"
    → stack rollback  = "revert back to previous versions"
    → stack events/exports = "identify specific versions running"
```

Tất cả 4 yêu cầu IaC đều map thẳng vào tính năng của CloudFormation.

**Amazon CloudFront** là CDN: phân phối content qua mạng edge location toàn cầu, route user đến edge gần nhất để giảm latency → đúng yêu cầu "global CDN".

#### Vì sao từng đáp án sai bị loại

- **B, D (CloudWatch là CDN):** sai cơ bản — CloudWatch là dịch vụ monitoring/metrics, không phải CDN. Không có nghĩa gì để chọn.
- **A (CloudFront đúng, nhưng dùng Elastic Beanstalk để quản lý hạ tầng):** Elastic Beanstalk giúp deploy và quản lý application nhanh, nhưng **không quản lý hạ tầng cloud dưới dạng application code** như CloudFormation. Beanstalk tập trung vào deploy app, không phải mô hình hoá toàn bộ infrastructure (VPC, network, IAM...) như một template có thể version, stage, rollback.

#### So sánh nhanh

| Đáp án | Quản lý hạ tầng | CDN | Vấn đề |
|---|---|---|---|
| **C** | CloudFormation | CloudFront | Đúng cả hai |
| A | Elastic Beanstalk | CloudFront | Beanstalk không phải IaC đầy đủ cho hạ tầng |
| B | CloudFormation | CloudWatch | CloudWatch không phải CDN |
| D | Elastic Beanstalk | CloudWatch | Sai cả hai |

#### Lưu ý thực tế

- ⚠️ **CloudWatch không bao giờ là CDN** — đây là trap lặp lại nhiều lần trong đề thi SAP-C02 (nhầm CloudWatch với CloudFront). Hễ thấy "CloudWatch" đi kèm từ "CDN" trong option, loại ngay.
- Elastic Beanstalk, OpsWorks, CodeDeploy đều là các lớp "deploy/manage application" cao hơn, khác với CloudFormation ở tầm "mô hình hoá toàn bộ hạ tầng as code".

#### Quy tắc nhớ cho thi

- **Thấy "IaC, version, stage, rollback cho toàn bộ infrastructure"** → **AWS CloudFormation**
- **Thấy "global CDN"** → **Amazon CloudFront**
- **Thấy "CloudWatch" ghép với "CDN"** → luôn sai, CloudWatch chỉ để monitoring

### TD explanation

AWS CloudFormation provides a common language for you to describe and provision all the infrastructure resources in your cloud environment. CloudFormation allows you to use a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This file serves as the single source of truth for your cloud environment.

Amazon CloudFront is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the user is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.
Therefore, the correct answer is: Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.
The option that says: Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture is incorrect. CloudWatch is typically not a CDN service.
The option that says: Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture is incorrect. As with the case above, CloudWatch is not a CDN service.
The option that says: Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture is incorrect. Even though Elastic Beanstalk enables you to quickly deploy and manage applications in the AWS Cloud, you still can’t manage the cloud infrastructure as application code with it. The best option is simply to use CloudFormation.

References:
https://aws.amazon.com/cloudformation/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

Check out this AWS CloudFormation Cheat Sheet:
https://tutorialsdojo.com/aws-cloudformation/

Elastic Beanstalk vs CloudFormation vs  OpsWorks vs CodeDeploy:
https://tutorialsdojo.com/elastic-beanstalk-vs-cloudformation-vs-opsworks-vs-codedeploy/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services/

</details>

<a id="q12"></a>

## Q12

An e-commerce company is having its annual sale event, where buyers will be able to purchase goods at a large discount on its e-commerce website. The e-commerce site will receive millions of visitors in a short period of time when the sale begins. The visitors will first log in to the site using either a Facebook or Google account and add items to the cart. After purchasing, a page will display the cart items along with the discounted prices. The company is also considering using Amazon Translate to support multiple languages for its international visitors. The company needs to build a checkout system that can handle the sudden surge of incoming traffic. The team evaluated Amazon Managed Streaming for Apache Kafka but opted for a simpler message queue for decoupling.
Which of the following is the MOST scalable solution that the company should use?

- **A.** Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito, then process the user's purchases and store them into an Amazon SQS queue using IAM Roles for Amazon EC2 Instances to gain permissions to the queue. Finally, the items from the queue are retrieved by a set of application servers and stored into an Amazon DynamoDB table.
- **B.** Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Lex, then process the user's purchases and store the cart into a Multi-AZ Amazon RDS database.
- **C.** Use the static website hosting feature of Amazon S3 with the Javascript SDK to authenticate the user login with Amazon Cognito. Set up AWS Global Accelerator to deliver the static content stored in the S3 bucket. Store user purchases in an Amazon DynamoDB table and use an IAM Role for managing permissions.
- **D.** Combine an Elastic Load balancer in front of multiple web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito. The web servers will process the user's purchases and store them in an Amazon DynamoDB table. Use an IAM Role to gain permissions to the DynamoDB table.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** sale surge; social login; simple queue for checkout

⚠️ **Watch:** Lex is a chatbot, not auth

🧠 **Rule:** Cognito + SQS buffer + DynamoDB behind ELB/CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
E-commerce sale event → millions visitors trong thời gian ngắn
User flow: login (Facebook/Google) → add to cart → checkout → hiển thị giá discount

Yêu cầu: giải pháp MOST SCALABLE cho checkout, có decouple bằng message queue
(đã loại Kafka, chọn "simpler message queue")

Đáp án đúng: A
  ELB + ASG web servers + CloudFront
  Auth: Cognito (social login Facebook/Google)
  Checkout → SQS queue (IAM Role cho EC2) → application servers đọc queue → DynamoDB
Anh chọn đúng A.
```

#### Vì sao A đúng

Kiến trúc A ghép đủ 4 lớp cần thiết cho "most scalable":

```
CloudFront (fast delivery)
     │
     ELB ── Auto Scaling Group (web servers, auth qua Cognito)
                     │
                     ▼
              Amazon SQS queue  ◄── decouple checkout traffic
                     │
          application servers (đọc queue, dùng IAM Role)
                     │
                     ▼
              Amazon DynamoDB
```

- **Cognito** xử lý social login (Facebook/Google) — đúng chức năng của nó là identity federation.
- **SQS** decouple phần ghi đơn hàng khỏi phần xử lý — đúng vai trò buffer khi traffic tăng đột biến ("decouples the application architecture... allow application servers to process the requests").
- **DynamoDB** + **IAM Role for EC2** scale tốt hơn RDS cho write throughput lớn, đột biến.
- **Auto Scaling Group** cho web servers → scale theo traffic thật.

#### Vì sao từng đáp án sai bị loại

- **B:** dùng **Amazon Lex** để auth — Lex là dịch vụ xây dựng conversational interface (chatbot voice/text), **không dùng cho authentication**. Ngoài ra lưu cart vào **Multi-AZ RDS** — RDS đắt hơn và kém scale hơn DynamoDB khi traffic đột biến.
- **C:** dùng S3 static hosting + JS SDK + Cognito (auth đúng), nhưng **AWS Global Accelerator không phục vụ static content từ S3 bucket** — phải dùng CloudFront. Thêm nữa, ghi trực tiếp vào DynamoDB (không qua queue) tốn read/write capacity, tăng cost khi traffic đột biến, kém scalable hơn phương án có SQS buffer.
- **D:** giống A nhưng web servers **không đặt trong Auto Scaling Group** ("multiple web servers" thường, không ASG) và cũng ghi thẳng vào DynamoDB không qua SQS → không scalable khi traffic tăng vọt.

#### So sánh nhanh

| Đáp án | Auth | Queue/decouple | DB | Vấn đề |
|---|---|---|---|---|
| **A** | Cognito | SQS | DynamoDB (qua queue) | Đúng |
| B | Lex (sai) | — | Multi-AZ RDS | Lex không phải auth; RDS đắt/kém scale |
| C | Cognito | — | DynamoDB (trực tiếp) | Global Accelerator không serve S3 static |
| D | Cognito | — | DynamoDB (trực tiếp) | Không có ASG, không có queue |

#### Lưu ý thực tế

- ⚠️ **Amazon Lex** chỉ để xây conversational interface (voice/text) — không bao giờ dùng để authenticate user. Nếu thấy "integrated in Amazon Lex" cho mục login → loại ngay.
- **AWS Global Accelerator** hoạt động ở network layer (routing traffic đến endpoint tối ưu, dùng cho EC2/ALB/NLB/EIP) — **không phải CDN cho S3 static content**. Muốn CDN cho S3 phải dùng CloudFront.

#### Quy tắc nhớ cho thi

- **Thấy "social login Facebook/Google"** → **Amazon Cognito**, không phải Lex
- **Thấy "decouple checkout/surge traffic"** → thêm **SQS** làm buffer trước khi ghi DB
- **Thấy "deliver static S3 content"** → **CloudFront**, không phải Global Accelerator
- **Thấy "most scalable + cost"** → ưu tiên **DynamoDB** hơn RDS cho ghi khối lượng lớn, đột biến

### TD explanation

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message oriented middleware, and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

In this scenario, the best solution is to use a combination of CloudFront, Elastic Load Balancer and SQS to provide a highly scalable architecture.
Hence, the correct answer is: Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito, then process the user’s purchases and store them into an Amazon SQS queue using IAM Roles for Amazon EC2 Instances to gain permissions to the queue. Finally, the items from the queue are retrieved by a set of application servers and stored into an Amazon DynamoDB table. This is a highly scalable solution and creates an appropriate IAM Role to access the DynamoDB database. In addition, it uses SQS which decouples the application architecture. This will allow the application servers to process the requests.
The option that says: Combine an Elastic Load balancer in front of an Auto Scaling group of web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Lex, then process the user’s purchases and store the cart into a Multi-AZ Amazon RDS database is incorrect because multi-AZ RDS is a more expensive solution when compared to DynamoDB. In addition, Amazon Lex is just a service for building conversational interfaces into any application using voice and text. This is not utilized for user authentication, unlike Amazon Cognito.
The option that says: Use the static website hosting feature of Amazon S3 with the Javascript SDK to authenticate the user login with Amazon Cognito. Set up AWS Global Accelerator to deliver the static content. Store user purchases in an Amazon DynamoDB table and use an IAM Role for managing permissions is incorrect. Although this would work, it is not scalable, and storing all the data directly in DynamoDB would consume read and write capacity and increase the cost. Moreover, you cannot use AWS Global Accelerator to deliver the static content stored in the S3 bucket. You have to use Amazon CloudFront instead.
The option that says: Combine an Elastic Load balancer in front of multiple web servers with Amazon CloudFront for fast delivery. The web servers will first authenticate the users by logging into their social media accounts which are integrated in Amazon Cognito. The web servers will process the user’s purchases and store them in an Amazon DynamoDB table. Use an IAM Role to gain permissions to the DynamoDB table is incorrect because it is not scalable and storing all the data directly in DynamoDB would simply consume read and write capacity and increase the cost. Moreover, the web servers are not placed in an Auto Scaling group, which means that this solution is not scalable.

References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/authentication-and-access-control.html
https://aws.amazon.com/blogs/database/dynamodb-streams-use-cases-and-design-patterns/

Check out this Amazon DynamoDB Cheat Sheet:
https://tutorialsdojo.com/amazon-dynamodb/

</details>

<a id="q20"></a>

## Q20

A media company in South Korea offers high-quality wildlife photos to its clients. Its photographers upload a large number of photographs to the company’s Amazon S3 bucket. Currently, the company is using a dedicated group of on-premises servers to process the photos and uses an open-source messaging system to deliver job information to the servers. After processing, the data would go to a tape library and be stored for long-term archival. The company decided to shift everything to AWS Cloud, and the solutions architect was tasked to implement the same existing infrastructure design and leverage AWS tools such as storage and messaging services to minimize cost. 
Which of the following options is the recommended solution that will meet the requirement?

- **A.** SQS will handle the job messages, while CloudWatch alarms will terminate any idle EC2 worker instances. After the data has been processed, change the storage class of your S3 objects to S3 IA-Standard.
- **B.** SNS will handle the passing of job messages, while CloudWatch alarms will terminate any idle spot worker instances. After the data has been processed, transfer your S3 objects to Amazon Glacier.
- **C.** Create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon Glacier.
- **D.** Initially change the storage class of the S3 objects to S3 IA-Standard. Then create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon S3-IA.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** photo processing jobs; minimize cost; archive

⚠️ **Watch:** SNS isn't a work queue

🧠 **Rule:** SQS depth-scaled Spot ASG workers + Glacier for archive.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại (on-prem):
  photographers upload ảnh → S3 bucket
  servers on-prem xử lý ảnh (lấy job từ open-source messaging system)
  sau xử lý → tape library lưu trữ dài hạn

Mục tiêu: dịch chuyển lên AWS, GIỮ NGUYÊN kiến trúc, nhưng
  minimize cost (storage + messaging)

Đáp án đúng: C
  Auto Scaling group of SPOT instance workers, scale theo SQS queue depth
  Sau xử lý → chuyển S3 objects sang Amazon Glacier (archival)
Anh chọn đúng C.
```

#### Vì sao C đúng

Kiến trúc mô phỏng đúng 1:1 hệ thống cũ, nhưng thay bằng dịch vụ AWS rẻ nhất phù hợp vai trò:

```
open-source messaging system  →  Amazon SQS   (nhận job messages)
on-prem dedicated servers     →  Spot instance workers trong ASG
                                  (scale theo queue depth của SQS)
tape library (lưu trữ lâu dài) →  Amazon Glacier (archival storage rẻ nhất)
```

- **SQS** đóng vai trò hàng đợi job xử lý ảnh — đúng use case kinh điển: "app places raw bitmap data in SQS queue for processing... dynamic scaling của ASG theo activity trong SQS queue".
- **Spot instances** rẻ hơn On-Demand, phù hợp cho workload xử lý ảnh có thể chịu gián đoạn (giống batch processing).
- **Glacier** là "cheapest storage option" cho archival — khớp đúng vai trò "tape library" (lưu dài hạn, không cần truy xuất nhanh).

#### Vì sao từng đáp án sai bị loại

- **A:** dùng SQS đúng, nhưng CloudWatch alarms terminate idle **EC2** instance — không có ASG nên không có khái niệm "idle instance" để scale/terminate hợp lý theo cách này; và chuyển sang **S3 IA-Standard** — S3 IA **không phải storage archival**, không khớp vai trò tape library.
- **D:** chuyển trước sang S3 IA-Standard rồi sau xử lý lại chuyển về S3-IA (storage class không đổi, không có archival) — S3 IA vẫn không phải archival storage.
- **B:** dùng **SNS** để truyền job messages — SNS là pub/sub notification, **không xử lý/queue job messages** như SQS; "Amazon Simple Notification Service cannot be used to process the messages."

#### So sánh nhanh

| Đáp án | Message queue | Compute scaling | Storage cuối |
|---|---|---|---|
| **C** | SQS | ASG Spot theo queue depth | **Glacier** (archival) |
| A | SQS | EC2 + CloudWatch alarm (không ASG) | S3 IA (không phải archival) |
| B | **SNS (sai)** | Spot + CloudWatch alarm | Glacier |
| D | SQS | ASG Spot | S3 IA → S3 IA (không đổi) |

#### Lưu ý thực tế

- ⚠️ **S3 Standard-IA không phải storage class "archival"** — nó vẫn truy xuất nhanh (milliseconds), chỉ rẻ hơn Standard cho dữ liệu truy cập ít. Khi đề nói "tape library" hoặc "long-term archival", chỉ **Glacier** (hoặc Glacier Deep Archive) mới đúng vai trò.
- SNS vs SQS: SNS = pub/sub broadcast (nhiều subscriber nhận cùng message), SQS = work queue (một consumer xử lý rồi xoá message). Khi cần "process job messages" tuần tự → luôn là SQS.

#### Quy tắc nhớ cho thi

- **Thấy "tape library" / "long-term archive" / "cheapest cold storage"** → **Amazon Glacier**
- **Thấy "process job messages", "queue depth scaling"** → **SQS**, không phải SNS
- **Thấy "S3 IA" đi cùng "archival"** → sai, S3 IA không phải lưu trữ lạnh archival

### TD explanation

There are some scenarios where you might think about scaling in response to activity in an Amazon SQS queue. For example, suppose that you have a web app that lets users upload images and use them online. In this scenario, each image requires resizing and encoding before it can be published. The app runs on EC2 instances in an Auto Scaling group, and it’s configured to handle your typical upload rates. Unhealthy instances are terminated and replaced to maintain current instance levels at all times. The app places the raw bitmap data of the images in an SQS queue for processing. It processes the images and then publishes the processed images where they can be viewed by users. The architecture for this scenario works well if the number of image uploads doesn’t vary over time. But if the number of uploads changes over time, you might consider using dynamic scaling to scale the capacity of your Auto Scaling group.

In this scenario, the best option is the combination of SQS and Glacier as a storage option.
Therefore, the correct answer is: Create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon Glacier. It uses SQS to process the messages, and it uses Glacier as the archival storage solution which is the cheapest storage option.
The option that says: SQS will handle the job messages, while CloudWatch alarms will terminate any idle EC2 worker instances. After the data has been processed, change the storage class of your S3 objects to S3 IA-Standard is incorrect. S3 IA is not an archival storage option, and since auto scaling is not mentioned, you cannot use CloudWatch alarms to terminate the idle EC2 instances.
The option that says: Initially change the storage class of the S3 objects to S3 IA-Standard. Then create an Auto-scaling group of spot instance workers that scale according to the queue depth in SQS to process job messages. After the data has been processed, transfer your S3 objects to Amazon S3-IA is incorrect. S3 IA is not an archival storage option.
The option that says: SNS will handle the passing of job messages, while CloudWatch alarms will terminate any idle spot worker instances. After the data has been processed, transfer your S3 objects to Amazon Glacier is incorrect. Amazon Simple Notification Service cannot be used to process the messages.
References:
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
https://aws.amazon.com/glacier
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html

Check out these Amazon SQS and Amazon S3 Glacier Cheat Sheets:
https://tutorialsdojo.com/amazon-sqs/
https://tutorialsdojo.com/amazon-glacier/

</details>

<a id="q21"></a>

## Q21

A company implements best practices and mandates that all of the cloud-related deployments should not be done manually but through the use of CloudFormation. All of the CloudFormation templates should be treated as code and hence, all of them are committed in a private GIT repository. A senior solutions architect has recently left the team. One of the tasks of the junior solutions architect is to handle a distributed system in AWS, in which the architecture is declared in a CloudFormation template. The distributed system needs to be migrated to another VPC and the junior solutions architect tried to read the template to understand the AWS resources that the template will generate. While analyzing the CloudFormation template, he stumbled upon the code below.
What does this code snippet do in CloudFormation?

"SNSTopic" : {
"Type" : "AWS::SNS::Topic",
"Properties" : {
"Subscription" : [{
"Protocol" : "sqs",
"Endpoint" : { "Fn::GetAtt" : [ "TutorialsDojoQueue", "Arn" ] }
}]
}

- **A.** Creates an SNS topic and then adds a subscription using the ARN attribute name for the SQS resource, which is created under the logical name TutorialsDojoQueue.
- **B.** Creates an SNS topic and then invokes the call to create an SQS queue with a logical resource name of TutorialsDojoQueue.
- **C.** Creates an SNS topic which allows SQS subscription endpoints to be added as a parameter on the template.
- **D.** Creates an SNS topic which allows SQS subscription endpoints.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** read a CFN SNS subscription snippet

⚠️ **Watch:** GetAtt references an existing logical resource

🧠 **Rule:** Fn::GetAtt Queue.Arn subscribes the SQS queue to the SNS topic.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```json
"SNSTopic" : {
  "Type" : "AWS::SNS::Topic",
  "Properties" : {
    "Subscription" : [{
      "Protocol" : "sqs",
      "Endpoint" : { "Fn::GetAtt" : [ "TutorialsDojoQueue", "Arn" ] }
    }]
  }
}
```

Câu hỏi: đoạn CloudFormation này **làm gì**?

Đáp án đúng: **A** — Tạo một SNS topic, rồi thêm subscription dùng ARN của resource SQS có logical name `TutorialsDojoQueue` (lấy ARN qua `Fn::GetAtt`).
Anh chọn đúng A.

#### Vì sao A đúng

Phân tích từng phần của template:

```
"Type": "AWS::SNS::Topic"        → resource này TẠO một SNS Topic
"Subscription": [{...}]          → ngay khi tạo topic, thêm 1 subscription
    "Protocol": "sqs"            → subscriber là một SQS queue
    "Endpoint": Fn::GetAtt[
        "TutorialsDojoQueue",    → logical ID của resource KHÁC trong template
        "Arn"                   → attribute cần lấy: ARN của queue đó
    ]
```

`Fn::GetAtt` là intrinsic function của CloudFormation, nhận 2 tham số: `logicalNameOfResource` và `attributeName`. Nó "returns the value of an attribute from a resource in the template" — ở đây lấy **ARN** của resource có logical name `TutorialsDojoQueue` (resource này được khai báo ở nơi khác trong template, không nằm trong đoạn code được trích).

Vậy bản chất: SNS topic này **subscribe** một SQS queue đã tồn tại (logical name TutorialsDojoQueue) thông qua ARN của nó — đúng như đáp án A diễn giải.

#### Vì sao từng đáp án sai bị loại

- **B (tạo SNS topic rồi "invokes the call to create" SQS queue):** sai bản chất. Đoạn code **không tạo** SQS queue — `Fn::GetAtt` chỉ **tham chiếu đến** resource đã có, không khai báo/tạo mới resource đó.
- **C (SNS topic "allows SQS subscription endpoints to be added as a parameter"):** sai — đây không mô tả đúng cơ chế. Endpoint ở đây là giá trị cụ thể lấy từ `Fn::GetAtt`, không phải một "parameter" cho phép người dùng tự thêm.
- **D (SNS topic "allows SQS subscription endpoints"):** quá mơ hồ/chung, không mô tả chính xác việc subscription đã được tạo sẵn ngay trong properties bằng `Fn::GetAtt`.

#### Lưu ý thực tế

- `Fn::GetAtt` chỉ hoạt động với **logical ID của resource được khai báo trong cùng template** — không tự tạo resource đó. Nếu `TutorialsDojoQueue` chưa được khai báo ở `Resources` section, template này sẽ lỗi.
- Pattern "SNS → SQS subscription qua Fn::GetAtt Arn" rất phổ biến trong CloudFormation để fan-out message tới nhiều SQS queue (SNS-to-SQS fanout pattern) — cần nhớ cả cú pháp lẫn ý nghĩa khi đọc code trong đề thi.

#### Quy tắc nhớ cho thi

- **Thấy `Fn::GetAtt [LogicalName, Attr]`** → đây là **tham chiếu** đến resource đã khai báo, KHÔNG phải tạo mới resource đó
- **Thấy `"Protocol": "sqs"` trong `Subscription` của `AWS::SNS::Topic`** → đây là cấu hình **SNS-to-SQS fanout**, topic subscribe sẵn 1 (hoặc nhiều) queue
- Khi đọc code CFN trong đề: tách rõ "cái gì được TẠO" (Type/Properties chính) vs "cái gì được THAM CHIẾU" (các intrinsic function như GetAtt, Ref)

### TD explanation

AWS CloudFormation provides several built-in functions that help you manage your stacks which are called “intrinsic functions”. Use intrinsic functions in your templates to assign values to properties that are not available until runtime.
You can use intrinsic functions only in specific parts of a template. Currently, you can use intrinsic functions in resource properties, outputs, metadata attributes, and update policy attributes. You can also use intrinsic functions to conditionally create stack resources.
The Fn::GetAtt intrinsic function returns the value of an attribute from a resource in the template. It has 2 parameters: the logicalNameOfResource and the attributeName. The logical name (also called logical ID) of the resource contains the attribute that you want to use. The attributeName is the name of the resource-specific attribute whose value you want to utilize.

Therefore, the correct answer is: Create an SNS topic and then add a subscription using the ARN attribute name for the SQS resource, which is created under the logical name TutorialsDojoQueue. The code snippet creates an SNS topic and then adds a subscription using the ARN attribute name for the SQS resource, which is created under the logical name “TutorialsDojoQueue” using the GetAtt intrinsic function.
The following options are all incorrect because these options incorrectly described what the code snippet does:
– Creates an SNS topic which allows SQS subscription endpoints to be added as a parameter on the template.

– Creates an SNS topic which allows SQS subscription endpoints.
– Creates an SNS topic and then invokes the call to create an SQS queue with a logical resource name of TutorialsDojoQueue.

References:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html

Check out this AWS CloudFormation Cheat Sheet:
https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q30"></a>

## Q30

A startup is running a data processing application on AWS. The application is hosted on 25 Amazon EC2 On-Demand Instances, distributed across three Availability Zones, and registered with a target group for a Network Load Balancer (NLB). 
Reports indicate a sharp decline in performance during high-demand periods, with CPU utilization spiking to 90%-100%. During normal operations, utilization averages only 20%. The application is stateless and needs to ensure consistent response times even during peak traffic. The company is also considering scheduled scaling to handle anticipated traffic increases during planned events.
 The company wants to improve application performance while optimizing costs over the next three years. 
Which solution is the most cost-effective for addressing this issue?

- **A.** Replace the On-Demand Instances with a Spot Fleet request type of request and with EBS-optimized enabled. Set the TotalTargetCapacity parameter to 25 and DefaultTargetCapacityType parameter to Spot. Attach the Spot Fleet to the NLB.
- **B.** Replace the On-Demand Instances with a Spot Fleet request type of request. Configure the InstanceInterruptionBehavior to stop and TotalTargetCapacity parameter to 30. Attach the Spot Fleet to the NLB.
- **C.** Configure an Auto Scaling group and attach it to the NLB. Set the minimum capacity to 5 instances and the maximum capacity to 30. Purchase Reserved Instances for 5 instances.
- **D.** Configure an ASG (Auto Scaling Group) and attach it to the Network Load Balancer. Set the capacity to a minimum of 15 instances and a maximum of 25. Purchase Reserved Instances for 15 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** stateless app; CPU spikes; cost over 3 years

⚠️ **Watch:** All-Spot for consistent response time is risky

🧠 **Rule:** ASG min 5/max 30 + Reserved Instances for the baseline.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
25 On-Demand EC2, 3 AZ, đứng sau Network Load Balancer (NLB)
App stateless, cần consistent response time

Bình thường: CPU ~20%
Peak:        CPU 90-100% → performance giảm mạnh
Có kế hoạch scheduled scaling cho các event

Mục tiêu: cải thiện performance + tối ưu cost trong 3 năm tới

Đáp án đúng: C
  ASG (min 5, max 30) gắn NLB + Reserved Instances cho 5 instance baseline
Anh chọn đúng C.
```

#### Vì sao C đúng

```
CPU trung bình 20% của 25 instance hiện tại
        ≈ tải thực tế tương đương khoảng 5 instance hoạt động full tải
                    │
         → min capacity = 5 (RI để tiết kiệm cho baseline)
                    │
Peak CPU 90-100% → cần scale vượt mức 25 hiện tại để tránh nghẽn
                    │
         → max capacity = 30 (có dư địa cho tăng trưởng/peak)
```

- **ASG min 5 / max 30**: baseline 5 instance khớp đúng với CPU trung bình 20% (tải hiện tại ở mức thấp), còn max 30 vượt mức 25 hiện có để giải quyết đúng vấn đề "CPU spike 90-100%" khi traffic cao.
- **Reserved Instances cho 5 instance baseline**: vì hệ thống chạy "over the next three years" → RI 3 năm tiết kiệm hơn nhiều so với On-Demand cho phần tải ổn định, luôn chạy (baseline). Phần vượt baseline vẫn dùng On-Demand linh hoạt theo scale.
- **NLB** phù hợp layer 4, hiệu năng cao, phục vụ đúng yêu cầu "consistent response times".

#### Vì sao từng đáp án sai bị loại

- **A (toàn bộ Spot Fleet, TotalTargetCapacity=25):** Spot Instance có thể bị interrupt bất kỳ lúc nào — **không phù hợp với app cần consistent response time**. Spot thích hợp cho batch/analytics/HPC chịu được gián đoạn, không phải production cần ổn định.
- **B (Spot Fleet, TotalTargetCapacity=30, InstanceInterruptionBehavior=stop):** cùng vấn đề như A — toàn Spot vẫn rủi ro gián đoạn; "stop" chỉ đổi cách xử lý khi bị interrupt (dừng thay vì terminate), **không ngăn được việc bị interrupt**.
- **D (ASG min 15/max 25, RI cho 15 instance):** max 25 **không vượt** mức hiện tại 25 → không giải quyết được vấn đề CPU spike 90-100% khi cần scale cao hơn nữa trong peak demand.

#### So sánh nhanh

| Đáp án | Compute | Min/Max | RI | Vấn đề |
|---|---|---|---|---|
| **C** | ASG (On-Demand mặc định) | 5 / 30 | 5 instance | Đúng — khớp baseline + đủ headroom peak |
| A | 100% Spot | TotalTargetCapacity 25 | — | Spot không ổn định cho consistent performance |
| B | 100% Spot | TotalTargetCapacity 30 | — | Vẫn 100% Spot, rủi ro interrupt |
| D | ASG | 15 / 25 | 15 instance | Max không vượt mức hiện tại, không giải quyết spike |

#### Lưu ý thực tế

- ⚠️ **"Cost-effective" không đồng nghĩa "toàn bộ Spot"** khi đề yêu cầu "consistent response times" — đây là trap thường gặp: Spot rẻ nhưng đổi lại độ tin cậy thấp hơn, không phù hợp app production cần ổn định.
- Reserved Instance hợp lý nhất khi áp cho phần **baseline luôn chạy** (ở đây CPU trung bình 20% ≈ 5 instance), còn phần "burst" vẫn nên linh hoạt On-Demand (hoặc Spot nếu chịu được gián đoạn).

#### Quy tắc nhớ cho thi

- **Thấy "consistent performance/response time" + "cost over 3 years"** → **ASG (On-Demand) + Reserved Instances** cho baseline, không phải toàn Spot
- **"100% Spot Fleet" cho production cần ổn định** → luôn là đáp án gài, loại
- **Tính baseline RI** = dựa vào CPU trung bình/tải bình thường, không phải tổng số instance hiện tại

### TD explanation

An Auto Scaling Group is a feature of Amazon EC2 that automatically manages a collection of EC2 instances, adjusting the number of running instances based on defined conditions. It helps maintain application availability and allows you to automatically increase the number of instances during demand spikes to preserve performance, and decrease capacity during lulls to reduce costs.
A Network Load Balancer (NLB) is a high-performance load-balancing service that operates at the transport layer (Layer 4) of the OSI model and is designed to handle millions of requests per second while maintaining ultra-low latencies. It’s capable of processing TCP, UDP, and TLS traffic, and is ideal for applications requiring extreme performance, such as gaming, IoT, and streaming services, while also providing static IP addresses for each Availability Zone.

The combination of Auto Scaling Groups and Network Load Balancer provides a robust and flexible infrastructure that can adapt to varying workloads while maintaining cost-efficiency. The Auto Scaling Group ensures that the application always has enough resources to handle incoming traffic, scaling up during high-demand periods and down during quieter times. This dynamic scaling addresses the reported performance issues during peak times when CPU utilization spikes to 90-100%.
The Network Load Balancer, meanwhile, efficiently distributes the incoming traffic across the available instances, ensuring that no single instance becomes overwhelmed. This is particularly important for maintaining consistent response times, which is a key requirement for the application.
The minimum capacity of 5 instances aligns well with the average 20% CPU utilization during normal operations. This baseline ensures that the application can handle typical loads without over-provisioning resources. The maximum capacity of 30 instances allows for significant scaling during high-demand periods, exceeding the current setup of 25 instances and providing room for future growth.
Purchasing Reserved Instances for a minimum of five instances is a strategic cost-saving measure. Reserved Instances offer substantial discounts compared to On-Demand pricing, especially over three years. This approach locks in lower prices for the baseline capacity while still allowing for flexible scaling with On-Demand instances when needed.
Hence, the correct answer is: Configure an Auto Scaling group and attach it to the NLB. Set the minimum capacity to 5 instances and the maximum capacity to 30. Purchase Reserved Instances for 5 instances.
The option that says: Replace the On-Demand Instances with a Spot Fleet request type of request and with EBS-optimized enabled. Set the TotalTargetCapacity parameter to 25 and DefaultTargetCapacityType parameter to Spot. Attach the Spot Fleet to the NLB is incorrect. While Spot Instances can offer cost savings, they are unsuitable for applications requiring consistent performance. Spot Instances are primarily used for flexible workloads that can tolerate interruptions. They are ideal for batch processing jobs, big data analytics, and high-performance computing tasks that don’t require continuous availability.
The option that says: Replace the On-Demand Instances with a Spot Fleet request type of request. Configure the InstanceInterruptionBehavior to stop and TotalTargetCapacity parameter to 30. Attach the Spot Fleet to the NLB is incorrect because, similar to the previous option, this solution relies entirely on Spot Instances, which are not suitable for applications requiring consistent performance. Additionally, the stop behavior doesn’t prevent interruptions, and it only changes how instances are handled when interrupted.
The option that says: Configure an ASG (Auto Scaling Group) and attach it to the Network Load Balancer. Set the capacity to a minimum of 15 instances and a maximum of 25. Purchase Reserved Instances for 15 instances is incorrect. While this option uses Auto Scaling and Reserved Instances, which are good practices, it doesn’t allow scaling beyond the current maximum of 25 instances, which may not address the performance issues during peak demand.

References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/
https://tutorialsdojo.com/aws-auto-scaling/

</details>

<a id="q40"></a>

## Q40

An international humanitarian aid organization has a requirement to store 20 TB worth of scanned files for the relief operations, which can grow to a total of 50 TB of data. There is also a requirement to have a website with a search feature in place that can be used to easily find a certain item through the thousands of scanned files. The new system is expected to run for more than three years. 
Which of the following is the most cost-effective option for implementing the search feature in the system?

- **A.** Use S3 for both storing and searching the scanned files by utilizing the native search capabilities of S3.
- **B.** Design the new system using a CloudFormation template. Use an EC2 instance running an NGINX web server and an open-source search application. Launch multiple standard EBS volumes with RAID configuration to store the scanned files with a search index.
- **C.** Use Amazon EFS to store and serve the scanned files. Install a 3rd-party search software on an Auto Scaling group of On-Demand EC2 Instances and an Elastic Load Balancer.
- **D.** Set up a new S3 bucket with standard storage to store and serve the scanned files. Use Amazon OpenSearch Service for query processing and use Elastic Beanstalk to host the website across multiple availability zones.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** 50 TB scanned files + search; >3 years; cost-effective

⚠️ **Watch:** S3 has no native full-text search

🧠 **Rule:** S3 storage + OpenSearch Service + Beanstalk.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
20 TB scanned files (có thể lên 50 TB) + website có search feature
Chạy > 3 năm, cần giải pháp cost-effective nhất cho SEARCH

Đáp án đúng: D
  S3 standard (lưu + serve file)
  Amazon OpenSearch Service (query processing)
  Elastic Beanstalk (host website, multi-AZ)
Anh chọn đúng D.
```

#### Vì sao D đúng

```
S3 Standard  ──────────► lưu trữ scanned files (durable, scalable, rẻ)
     │
     ▼ (metadata/index)
Amazon OpenSearch Service ─► xử lý query/search (search & analytics engine
                              chuyên dụng, có security, HA, durability)
     │
     ▼
Elastic Beanstalk ─────────► host website, multi-AZ (giảm operational overhead)
```

Điểm mấu chốt của câu này: **"S3's native search capability is not effective"** — S3 là object storage, không có full-text search built-in tốt. Vì vậy bắt buộc cần **một dịch vụ search riêng** — đó là Amazon OpenSearch Service, được thiết kế chuyên cho "efficient search and analytics... querying extensive datasets". Elastic Beanstalk đơn giản hoá việc deploy/quản lý website, giảm overhead vận hành — hợp với yêu cầu chạy ổn định > 3 năm mà không cần tự quản lý server.

#### Vì sao từng đáp án sai bị loại

- **A (S3 tự search bằng "native search capabilities"):** sai gốc — S3 **không có khả năng search hiệu quả**; đây chính là lý do cả 3 đáp án còn lại đều cần thêm một search service riêng.
- **B (CloudFormation + EC2 NGINX + open-source search app + EBS RAID):** RAID của **EBS volumes thường (standard) không bền và không scale** như S3 cho việc lưu trữ hàng chục TB file quét.
- **C (EFS + 3rd-party search software + ASG On-Demand EC2 + ELB):** hai vấn đề cost — hệ thống chạy "more than 3 years" nên **Reserved Instances** tiết kiệm hơn On-Demand (đáp án dùng On-Demand); và mua + cài **3rd-party search software có thể tốn kém hơn** so với dùng Amazon OpenSearch Service (managed, sẵn có).

#### So sánh nhanh

| Đáp án | Lưu trữ file | Search | Compute | Vấn đề |
|---|---|---|---|---|
| **D** | S3 Standard | **OpenSearch Service** | Elastic Beanstalk | Đúng |
| A | S3 | S3 "native search" | — | S3 không search hiệu quả |
| B | EBS RAID | open-source app | EC2 (CloudFormation) | EBS RAID kém durable/scalable hơn S3 |
| C | EFS | 3rd-party software | ASG EC2 On-Demand | On-Demand (không RI) + software 3rd-party tốn kém |

#### Lưu ý thực tế

- ⚠️ **S3 không có "native full-text search"** — đây là điểm dễ bị đánh lừa vì S3 rất mạnh về lưu trữ, nhưng search cần dịch vụ riêng (OpenSearch/Elasticsearch, hoặc tự build index).
- Khi đề nói hệ thống chạy "more than X years" (ở đây 3 năm) → đây là tín hiệu kinh điển để chọn **Reserved Instances** thay vì On-Demand khi so sánh cost giữa các đáp án có EC2.

#### Quy tắc nhớ cho thi

- **Thấy "search feature" cho dữ liệu lớn lưu ở S3** → cần thêm **Amazon OpenSearch Service**, S3 không tự search được
- **Thấy "chạy > N năm" + so sánh cost EC2** → ưu tiên đáp án có **Reserved Instances**
- **Thấy "giảm operational overhead" cho website hosting** → **Elastic Beanstalk** thường là lựa chọn phù hợp hơn tự quản lý EC2/NGINX

### TD explanation

Amazon Simple Storage Service (S3) is an excellent object-based storage that is highly durable and scalable. However, its native search capability is not effective. Hence, you need to have a separate service to handle the search feature.
Amazon OpenSearch Service simplifies the deployment, operation, and scaling of OpenSearch, a widely-used open-source search and analytics engine. It provides robust security features, ensures high availability and data durability, and offers direct access to the OpenSearch API.

Amazon S3 offers scalable and cost-effective storage, making it ideal for handling large datasets. It ensures durability and easy access to the scanned files.
Amazon OpenSearch Service is optimized for efficient search and analytics, making it perfect for querying extensive datasets.
Elastic Beanstalk simplifies the deployment and management of the website, significantly reducing operational overhead.
By hosting the website across multiple availability zones, the system ensures high reliability and availability, which is crucial for humanitarian operations.
Hence, the correct answer is: Set up a new S3 bucket with standard storage to store and serve the scanned files. Use Amazon OpenSearch Service for query processing and use Elastic Beanstalk to host the website across multiple availability zones.
The option that says: Use Amazon EFS to store and serve the scanned files. Install a 3rd-party search software on an Auto Scaling group of On-Demand EC2 Instances and an Elastic Load Balancer is incorrect. It is stated in the scenario that the new system is expected to run for more than 3 years which means that using Reserved EC2 instances would typically be a more cost-effective choice than using On-Demand instances. In addition, purchasing and installing a 3rd-party search software might be more expensive than just using Amazon OpenSearch Service.
The option that says: Design the new system using a CloudFormation template. Use an EC2 instance running an NGINX web server and an open-source search application. Launch multiple standard EBS volumes with RAID configuration to store the scanned files with a search index is incorrect because a system composed of RAID configuration of EBS volumes is not a durable and scalable solution compared to S3.
The option that says: Use S3 for both storing and searching the scanned files by utilizing the native search capabilities of S3 is incorrect as the native search capability of S3 is not effective. It is better to use Amazon OpenSearch Service or another service primarily providing search functionality.

References:
https://aws.amazon.com/s3/
https://docs.aws.amazon.com/opensearch-service/
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hawordpress-tutorial.html

Check out this Amazon OpenSearch Service Cheat Sheet:
https://tutorialsdojo.com/amazon-opensearch-service/

</details>

<a id="q47"></a>

## Q47

An insurance company collects contributions from its clients and invests in the stock market. Using the on-premises data center, the company ingests raw data feeds from the stock market, transforms it, and sends it to the internal Apache Kafka cluster for processing. The management wants to send the cluster’s output to Amazon Web Services by building a scalable and near-real-time solution that will provide the stock market data to its web application. The application is a critical production component, so the solution needs to have a consistent high-performance network.
Which of the following actions should the solutions architect implement to fulfill the requirements? (Select THREE.)

- **A.** Fetch the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Consumer Library. Use Kinesis Data Analytics to process and transform the streaming data before delivering it to downstream consumers.
- **B.** Write an AWS Lambda function to process the Amazon Kinesis data stream and create a WebSocket API in Amazon API Gateway to invoke the function. Send the callback messages to connected clients by using the @connections command for the API.
- **C.** To have consistent performance, request for an AWS Direct Connect connection from the on-premises data center to the AWS VPC.
- **D.** Write an AWS Lambda function to process the Amazon Kinesis data stream and write a GraphQL API in AWS AppSync to invoke the function. Send the callback messages to connected clients by using the @connections command for the API.
- **E.** To have a consistent performance while being cost-effective, configure a Site-to-Site VPN from the on-premises data center to the AWS VPC.
- **F.** Pull the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Producer Library.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C, F (you answered correctly)

🔑 **Key words:** on-prem Kafka → near-real-time web app; consistent network (Select THREE)

⚠️ **Watch:** KCL consumes; KPL produces

🧠 **Rule:** EC2 KPL into Kinesis + Direct Connect + Lambda + WebSocket API @connections.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem: raw stock feed → transform → Apache Kafka cluster
Yêu cầu: gửi output lên AWS, xây giải pháp scalable, near-real-time
         cho web app, network phải consistent high-performance

Select THREE → đáp án đúng: B, C, F
Anh chọn đúng cả 3.
```

Đây là multi-select — 3 lựa chọn phải ghép thành **MỘT** giải pháp hoàn chỉnh, mỗi lựa chọn phụ trách một tầng khác nhau: network connectivity, ingestion vào AWS, và delivery real-time tới client.

#### Vì sao B, C, F đúng — từng lựa chọn khớp một tầng

```
[Tầng network]        AWS Direct Connect (C)
  on-prem data center ───dedicated connection───► AWS VPC
  → "reduce network costs, increase bandwidth, more consistent
     network experience than Internet-based connections"

[Tầng ingestion]       EC2 (ASG) + Kinesis Producer Library (F)
  Kafka cluster ──PULL──► EC2 fleet (KPL) ──► Kinesis Data Stream
  → KPL là thư viện dành cho PRODUCER (đẩy data VÀO stream)

[Tầng delivery real-time] Lambda + API Gateway WebSocket (B)
  Kinesis stream ──► Lambda xử lý ──► WebSocket API (API Gateway)
                                      ──@connections──► connected clients
  → WebSocket bidirectional, phù hợp "financial trading platforms"
    kiểu push real-time tới client, dùng @connections để gửi callback
```

Ba lựa chọn này khớp đúng chuỗi: **Direct Connect** (network ổn định) → **EC2 + KPL** (đưa data từ Kafka vào Kinesis) → **Lambda + WebSocket API** (đẩy real-time đến web app).

#### Vì sao từng đáp án sai bị loại

- **A (dùng "Kinesis Consumer Library" để đẩy data vào stream):** sai thuật ngữ bản chất — **Consumer Library (KCL) dùng để ĐỌC/xử lý** data ra khỏi stream, không dùng để **gửi data VÀO** stream. Việc đẩy data vào Kinesis phải dùng **Producer Library (KPL)**, như lựa chọn F.
- **D (AppSync GraphQL API thay cho WebSocket API):** @connections để callback tới client **không phải là tính năng của GraphQL API trong AppSync** — @connections command gắn với WebSocket API của API Gateway, không phải AppSync.
- **E (Site-to-Site VPN "cost-effective + consistent performance"):** VPN **không đảm bảo network connection đáng tin cậy và hiệu năng cao** như yêu cầu "consistent high-performance network" — VPN đi qua Internet nên không ổn định bằng Direct Connect (dedicated line).

#### So sánh nhanh

| Vai trò | Đúng | Vì sao sai (đáp án tương tự) |
|---|---|---|
| Đưa data vào Kinesis | **F: KPL** | A dùng KCL — sai, KCL là để consume |
| Network connectivity | **C: Direct Connect** | E dùng Site-to-Site VPN — không đủ ổn định |
| Push real-time tới client | **B: Lambda + WebSocket API** | D dùng AppSync GraphQL — @connections không thuộc AppSync |

#### Lưu ý thực tế

- ⚠️ **KPL (Producer) vs KCL (Consumer)** là cặp dễ nhầm kinh điển trong Kinesis: KPL = đẩy data VÀO stream, KCL = đọc data RA khỏi stream để xử lý.
- `@connections` API chỉ dùng với **WebSocket API trong API Gateway** để gửi callback message tới client đã connect — không áp dụng cho REST API hay AppSync GraphQL API.
- Direct Connect phù hợp khi đề nhấn mạnh "consistent/reliable high-performance network" cho production — VPN chỉ phù hợp khi yêu cầu chỉ là "cost-effective", không đòi hỏi hiệu năng ổn định cao.

#### Quy tắc nhớ cho thi

- **Thấy "đẩy data vào Kinesis stream"** → **Kinesis Producer Library (KPL)**
- **Thấy "đọc/xử lý data từ Kinesis stream"** → **Kinesis Consumer Library (KCL)**
- **Thấy "push real-time đến client đã connect" + "@connections"** → **WebSocket API trong API Gateway**, không phải AppSync
- **Thấy "consistent, high-performance, production-critical network từ on-prem"** → **AWS Direct Connect**, không phải Site-to-Site VPN

### TD explanation

AWS Direct Connect makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs in the same region. Using private VIF on AWS Direct Connect, you can establish private connectivity between AWS and your data center, office, or colocation environment, as shown in the following figure. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.

A producer puts data records into Amazon Kinesis data streams. For example, a web server sending log data to a Kinesis data stream is a producer. A consumer processes the data records from a stream. To put data into the stream, you must specify the name of the stream, a partition key, and the data blob to be added to the stream. The partition key is used to determine which shard in the stream the data record is added to. All the data in the shard is sent to the same worker that is processing the shard.
A WebSocket API in API Gateway is a collection of WebSocket routes that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can use API Gateway features to help you with all aspects of the API lifecycle, from creation through monitoring your production APIs.

API Gateway WebSocket APIs are bidirectional. A client can send messages to a specific service, and services can independently send messages to clients. This bidirectional behavior enables richer client/service interactions because services can push data to clients without requiring clients to make an explicit request. WebSocket APIs are often used in real-time applications such as chat applications, collaboration platforms, multiplayer games, and financial trading platforms.
You can use the @connections API from your backend service to send a callback message to a connected client, get connection information or disconnect from the client.
Hence, the correct answers are:
– To have consistent performance, request for an AWS Direct Connect connection from the on-premises data center to the AWS VPC.
– Pull the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Producer Library.
– Write an AWS Lambda function to process the Amazon Kinesis data stream and create a WebSocket API in Amazon API Gateway to invoke the function. Send the callback messages to connected clients by using the @connections command for the API.
The option that says: Fetch the messages from the on-premises Apache Kafka cluster by using a fleet of Amazon EC2 instances in an Auto Scaling Group. Send the data into an Amazon Kinesis Data Stream by using the Kinesis Consumer Library. Use Kinesis Data Analytics to process and transform the streaming data before delivering it to downstream consumers is incorrect because you should typically use Amazon Kinesis Producer Library, not Consumer Library.
The option that says: Write an AWS Lambda function to process the Amazon Kinesis data stream and write a GraphQL API in AWS AppSync to invoke the function. Send the callback messages to connected clients by using the @connections command for the API is incorrect because using @connections to have the backend service connect back to the clients is not primarily a feature of the GraphQL API when using AWS AppSync.
The option that says: To have a consistent performance while being cost-effective, configure a Site-to-Site VPN from the on-premises data center to the AWS VPC is incorrect because a Site-to-Site VPN does not provide a reliable and high-performance network connection between the on-premises data center and Amazon VPC.

References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html
https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-producers.html
https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html

Check out these AWS Direct Connect and Amazon Kinesis Cheat Sheets:
https://tutorialsdojo.com/aws-direct-connect/
https://tutorialsdojo.com/amazon-kinesis/

</details>

<a id="q58"></a>

## Q58

An electric utility company deploys smart meters for its customers to easily track electricity usage. Each smart meter sends data every five minutes to an Amazon API Gateway, which is then processed by several AWS Lambda functions before being stored in an Amazon DynamoDB table. The Lambda functions take about 5 to 10 seconds to process the data based on the initial deployment testing. As the company’s customer base grew, the solutions architect noticed that the Lambda functions were now taking 60 to 90 seconds to complete the processing. New metrics are also collected from the smart meters, which further increases the processing time. Errors began showing when running the Lambda function, such as TooManyRequestsException and ProvisionedThroughputExceededException error when performing a PUT operation on the DynamoDB table.
Which combination of the following actions will resolve these issues? (Select TWO.)

- **A.** The new metrics being collected requires more processing power from the Lambda functions. Adjust the memory allocation for the Lambda function to accommodate the surge.
- **B.** Process the data in batches to avoid reaching the write limits to the DynamoDB table. Group the requests from API Gateway by streaming the data into an Amazon Kinesis data stream.
- **C.** Modify the Amazon API Gateway throttling limits and quotas at the stage level to allow a higher request rate and burst capacity so that incoming smart meter data is not throttled before being sent to Lambda.
- **D.** As more customers are sending data, adjust the Write Capacity Unit (WCU) of the DynamoDB table to be able to accommodate all the write requests being processed by the Lambda functions.
- **E.** Since the Lambda functions are being overwhelmed with too many requests, increase the payload size from the meters but send the data less frequently to avoid reaching the concurrency limit.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D (you answered correctly)

🔑 **Key words:** TooManyRequests + ProvisionedThroughputExceeded (Select TWO)

⚠️ **Watch:** ⚠️ Q24: stream ingestion → Kinesis/Firehose batching

🧠 **Rule:** Batch via Kinesis + raise DynamoDB WCU.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Smart meter → API Gateway → Lambda (xử lý) → DynamoDB (PUT)

Ban đầu: Lambda xử lý 5-10s
Hiện tại: khách hàng tăng + metrics mới → Lambda xử lý 60-90s
Lỗi xuất hiện:
  - TooManyRequestsException (Lambda)
  - ProvisionedThroughputExceededException (DynamoDB PUT)

Select TWO → đáp án đúng: B, D
Anh chọn đúng cả 2.
```

#### Vì sao B, D đúng

```
ProvisionedThroughputExceededException
    → nghĩa là "exceeded maximum allowed provisioned throughput"
    → request rate ghi vào DynamoDB quá cao so với WCU hiện có
    → Fix (D): TĂNG Write Capacity Unit (WCU) của bảng

TooManyRequestsException (Lambda)
    → quá nhiều invocation đồng thời, vượt concurrency
    → Fix (B): GOM request từ API Gateway vào Amazon Kinesis Data Stream,
      xử lý theo BATCH → giảm số lần invoke Lambda + giảm số PUT dồn dập
      vào DynamoDB → giảm cả 2 lỗi cùng lúc
```

**D** giải quyết trực tiếp nguyên nhân DynamoDB: PUT request tiêu thụ WCU, tăng WCU = tăng throughput cho phép.

**B** giải quyết nguyên nhân gốc ở tầng ingestion: stream + batch giúp "decrease in requests in Lambda" — giảm tần suất gọi Lambda và giảm tần suất ghi DynamoDB cùng lúc, thay vì mỗi smart meter tạo 1 request riêng lẻ.

#### Vì sao từng đáp án sai bị loại

- **A (tăng memory cho Lambda):** tăng memory có thể cải thiện execution speed ở mức nào đó, nhưng hiệu quả **plateau** ở mức memory cao, không giải quyết triệt để như batching; đồng thời **tăng chi phí đáng kể**.
- **C (tăng throttling limit của API Gateway):** lỗi quan sát được (TooManyRequestsException, ProvisionedThroughputExceededException) **do Lambda concurrency và DynamoDB throughput**, không phải do API Gateway throttling — quota của API Gateway vốn đã cao hơn nhiều so với workload mô tả, nên tăng nó không giải quyết bottleneck thật.
- **E (tăng payload size, giảm tần suất gửi):** có thể giảm số lượng request tới Lambda (giảm TooManyRequestsException), nhưng dễ **chạm giới hạn payload 10MB của API Gateway** nếu gom quá nhiều data trước khi gửi.

#### So sánh nhanh

| Đáp án | Giải quyết đúng lỗi nào | Vấn đề |
|---|---|---|
| **B** | TooManyRequestsException + giảm tải DynamoDB | Đúng — batch qua Kinesis |
| **D** | ProvisionedThroughputExceededException | Đúng — tăng WCU |
| A | Một phần TooManyRequestsException | Hiệu quả giảm dần, tốn chi phí |
| C | Không đúng nguyên nhân | API Gateway không phải bottleneck |
| E | Một phần TooManyRequestsException | Dễ vượt payload limit 10MB |

#### Lưu ý thực tế

⚠️ **Dễ nhầm — liên quan Q24 (sai):** khi đề nói "streaming ingestion" / "gom batch dữ liệu từ nhiều nguồn gửi liên tục" (ví dụ smart meter gửi mỗi 5 phút), giải pháp đúng luôn là **Amazon Kinesis Data Stream / Kinesis Data Firehose** để batch hoá trước khi tới Lambda/DynamoDB — **không phải AWS Step Functions**. Step Functions điều phối workflow (orchestration các bước xử lý có trạng thái), không phải dịch vụ streaming/batching dữ liệu đầu vào. Ở Q58 này, Kinesis Data Stream là lựa chọn B đúng; nếu từng chọn Step Functions cho một tình huống tương tự (như ở Q24), đó là nhầm vai trò dịch vụ.

- Cả hai lỗi (Lambda throttle + DynamoDB throughput) thường xuất hiện cùng lúc khi traffic tăng không kiểm soát — cần xử lý ở **cả hai tầng**: giảm tần suất request (batching) VÀ tăng throughput cho phép (WCU).

#### Quy tắc nhớ cho thi

- **Thấy `ProvisionedThroughputExceededException`** → tăng **WCU/RCU** của DynamoDB (hoặc on-demand capacity)
- **Thấy `TooManyRequestsException` ở Lambda do nhiều IoT/thiết bị gửi liên tục** → batch qua **Kinesis Data Stream/Firehose**, không phải tăng memory hay tăng API Gateway quota
- **Thấy "streaming ingestion từ nhiều device"** → **Kinesis**, KHÔNG phải Step Functions (Step Functions = orchestration, không phải ingestion)

### TD explanation

In Amazon DynamoDB, the ProvisionedThroughputExceededException error means that you exceeded your maximum allowed provisioned throughput for a table or for one or more global secondary indexes. This means that your request rate is too high. The AWS SDKs for DynamoDB automatically retries requests that receive this exception. Your request is eventually successful unless your retry queue is too large to finish.
To solve this, you can increase the write capacity unit (WCU) of your DynamoDB table. Every PutItem request consumes a write capacity unit. A write capacity unit represents one write per second, for an item up to 1 KB in size. For example, suppose that you create a table with 10 write capacity units. This allows you to perform 10 writes per second for items up to 1 KB in size.

In AWS Lambda, the first time you invoke your function, AWS Lambda creates an instance of the function and runs its handler method to process the event. When the function returns a response, it stays active and waits to process additional events. If you invoke the function again while the first event is being processed, Lambda initializes another instance, and the function processes the two events concurrently. Your functions’ concurrency is the number of instances that serve requests at a given time. For an initial burst of traffic, your functions’ cumulative concurrency in a Region can reach an initial level of between 500 and 3000, which varies per Region.
When seeing the TooManyRequestsException in AWS Lambda, it is possible that the throttles that you’re seeing aren’t on your Lambda function. Throttles can also occur on API calls during your function’s invocation or on concurrency limits.
With API Gateway, you can send the stream to an Amazon Kinesis data stream on which you can group requests in batches, so there will be a decrease in requests in Lambda.
Hence, the correct answers are:
– As more customers are sending data, adjust the Write Capacity Unit (WCU) of the DynamoDB table to be able to accommodate all the write requests being processed by the Lambda functions.
– Process the data in batches to avoid reaching the write limits to the DynamoDB table. Group the requests from API Gateway by streaming the data into an Amazon Kinesis data stream.
The option that says: The new metrics being collected requires more processing power from the Lambda functions. Adjust the memory allocation for the Lambda function to accommodate the surge is incorrect. While increasing memory allocation can improve the Lambda function’s execution speed, it can only do so to a certain extent. This improvement may alleviate some occurrences of the TooManyRequestsException error, especially at lower memory configurations. However, as you approach the upper memory limits, the performance gains tend to plateau, making it less effective than solutions such as batching. Moreover, the cost in running the function will also increase significanly.
The option that says: Since the Lambda functions are being overwhelmed with too many requests, increase the payload size from the meters but send the data less frequently to avoid reaching the concurrency limit is incorrect. Although this will solve the TooManyRequestsException for the Lambda function, you may reach the 10MB payload limit on the API gateway if you aggregate too much data before sending it to the API Gateway.
The option that says: Modify the Amazon API Gateway throttling limits and quotas at the stage level to allow a higher request rate and burst capacity so that incoming smart meter data is not throttled before being sent to Lambda is incorrect because the errors observed (TooManyRequestsException and ProvisionedThroughputExceededException) are typically caused by Lambda concurrency limits and DynamoDB throughput, not API Gateway throttling. API Gateway quotas are much higher than the described workload, so increasing them would not resolve the actual bottlenecks.

References:
https://aws.amazon.com/premiumsupport/knowledge-center/lambda-troubleshoot-throttling/
https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html#concurrent-execution-safety-limit
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html

Check out these AWS Lambda and Amazon DynamoDB Cheat Sheets:
https://tutorialsdojo.com/aws-lambda/
https://tutorialsdojo.com/amazon-dynamodb/

</details>

<a id="q64"></a>

## Q64

A company wants to create a new service that will complement the launch of its new product. The site must be highly available and scalable to handle the unpredictable workload, and should also be stateless and REST compliant. The solution needs to have multiple persistent storage layers for service object metadata and durable storage for static content. All requests to the service should be authenticated and securely processed. The company also wants to keep the costs at a minimum. The team considered using an AWS Lambda authorizer for custom authentication logic but wants to minimize operational overhead.
Which of the following is the recommended solution that will meet the company requirements?

- **A.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **B.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **C.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service.
- **D.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** stateless REST, authenticated, lowest cost

⚠️ **Watch:** ElastiCache isn't a durable metadata store

🧠 **Rule:** API Gateway + Lambda + Cognito + DynamoDB + S3 presigned URLs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Yêu cầu service mới:
  - Highly available, scalable, unpredictable workload
  - Stateless, REST compliant
  - 2 persistent storage layer: metadata + static content durable storage
  - Authenticated + secure, minimize operational overhead cho auth
  - Minimize cost

Đáp án đúng: D
  API Gateway + Lambda (unique function/resource, proxy integration)
  Auth: Amazon Cognito user pools
  Metadata: DynamoDB (Auto Scaling)
  Static content: S3 bucket (secured) + presigned URL
Anh chọn đúng D.
```

#### Vì sao D đúng

```
API Gateway (REST, proxy integration)
     │
     ▼
Lambda functions (mỗi resource 1 function riêng)
     │             │
     ▼             ▼
Cognito user pools   DynamoDB (metadata, Auto Scaling)
(auth)                     │
                            ▼
                    S3 bucket (static content, secured)
                            │
                    presigned URL khi reference object
```

- **API Gateway + Lambda** là mô hình serverless, chỉ trả tiền khi có traffic → khớp "unpredictable workload" + "minimize cost" tốt hơn hẳn so với chạy container/server liên tục.
- **Cognito user pools**: cung cấp sẵn "sign-up/sign-in, built-in UI, social sign-in, MFA, user directory..." — tức minimize operational overhead cho việc tự viết authorizer, trong khi vẫn đáp ứng "custom authentication logic" nếu cần (qua Lambda triggers).
- **DynamoDB + Auto Scaling**: lưu metadata, scale theo tải, không cần quản lý capacity tay.
- **S3 + presigned URL**: lưu static content durable, bảo mật qua presigned URL thay vì public access — đúng yêu cầu "securely processed".

#### Vì sao từng đáp án sai bị loại

- **A, C (Fargate + Application Load Balancer):** Fargate chạy container liên tục, **chi phí cao hơn Lambda** — Lambda chỉ chạy on-demand, phù hợp hơn với "keep costs at a minimum" và workload unpredictable. ("Running a Fargate cluster continuously is more expensive than running Lambda functions.")
- **C cụ thể còn dùng "custom authenticator" tự viết:** tăng operational overhead so với việc dùng sẵn Cognito/API Gateway authorizer.
- **B (ElastiCache Multi-AZ cluster lưu metadata):** ElastiCache là **cache in-memory, không phải nơi lưu metadata bền/durable** — không phù hợp vai trò "persistent storage layer for service object metadata".
- **B cũng dùng API Gateway custom authorizer thay Cognito:** custom authorizer đòi hỏi tự code logic xác thực — **kém robust và nhiều operational overhead hơn** Cognito user pools (đã có sẵn tính năng MFA, user directory, social login...).

#### So sánh nhanh

| Đáp án | Compute | Auth | Metadata store | Vấn đề |
|---|---|---|---|---|
| **D** | API Gateway + Lambda | Cognito user pools | DynamoDB | Đúng — rẻ nhất, đủ robust |
| A | Fargate + ALB | Cognito user pools | DynamoDB | Fargate chạy liên tục → đắt hơn Lambda |
| B | API Gateway + Lambda | API Gateway custom authorizer | **ElastiCache** | ElastiCache không durable cho metadata; custom authorizer kém robust |
| C | Fargate + ALB | Custom authenticator tự viết | DynamoDB | Đắt hơn Lambda; custom auth tăng overhead |

#### Lưu ý thực tế

- ⚠️ **ElastiCache không phải nơi lưu metadata bền** — nó là cache tạm thời (in-memory), dữ liệu có thể mất khi node restart/failover (dù Multi-AZ giúp HA, vẫn không đóng vai trò "persistent storage layer" đúng nghĩa cho metadata quan trọng).
- Giữa **Cognito user pools** và **API Gateway custom authorizer**: Cognito được khuyến nghị khi cần tính năng user management đầy đủ (MFA, social login, user directory); custom authorizer phù hợp hơn khi logic auth rất đặc thù và đơn giản, nhưng tăng gánh vận hành.

#### Quy tắc nhớ cho thi

- **Thấy "unpredictable workload" + "minimize cost"** → ưu tiên **Lambda** (serverless) hơn Fargate/EC2 chạy liên tục
- **Thấy "persistent metadata store"** → **DynamoDB**, không phải ElastiCache (cache ≠ persistent store)
- **Thấy "minimize operational overhead cho auth"** → **Cognito user pools** thường thắng custom authorizer tự viết
- **Thấy "securely serve static content từ S3"** → **presigned URL**

### TD explanation

Amazon API Gateway Lambda proxy integration is a simple, powerful, and nimble mechanism to build an API with a setup of a single API method. The Lambda proxy integration allows the client to call a single Lambda function in the backend. The function accesses many resources or features of other AWS services, including calling other Lambda functions.
In Lambda proxy integration, when a client submits an API request, API Gateway passes to the integrated Lambda function the raw request as-is, except that the order of the request parameters is not preserved. This request data includes the request headers, query string parameters, URL path variables, payload, and API configuration data. The configuration data can include current deployment stage name, stage variables, user identity, or authorization context (if any).
A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers. Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).

User pools provide:
– Sign-up and sign-in services.
– A built-in, customizable web UI to sign in users.
– Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple, as well as sign-in with SAML identity providers from your user pool.
– User directory management and user profiles.
– Security features such as multi-factor authentication (MFA), checks for compromised credentials, account takeover protection, and phone and email verification.
– Customized workflows and user migration through AWS Lambda triggers.
Amazon S3 is a simple key-based object store whose scalability and low cost make it ideal for storing large datasets or objects. When finding objects based on attributes or other metadata, a common solution is to build an external index such as a DynamoDB Table that maps queryable attributes to the S3 object key. DynamoDB is a NoSQL data store that can be used for storing the index itself.
One way of securing objects that are shared on S3 buckets is by using presigned URLs. When you create a presigned URL for your object, you must provide your security credentials, specify a bucket name, an object key, specify the HTTP method (GET to download the object), and expiration date and time. The presigned URLs are valid only for the specified duration.
Anyone who receives the presigned URL can then access the object. For example, if you have a video in your bucket and both the bucket and the object are private, you can share the video with others by generating a presigned URL.
Hence, the correct answer is: Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
The option that says: Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service is incorrect. Although running Docker-based containers on Amazon Fargate is possible, this solution does not just offer the lowest possible cost to satisfy the given scenario. AWS Lambda is suited for creating serverless/stateless APIs and costs cheaper than AWS Fargate.
The option that says: Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket is incorrect. Running a Fargate cluster continuously is more expensive than running Lambda functions which only runs on-demand.
The option that says: Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket is incorrect because it is recommended to use Amazon Cognito user pools for user access controls compared to an API Gateway custom authorizer. It is more robust and offers more features because it is designed to handle user access.

References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
https://aws.amazon.com/blogs/big-data/building-and-maintaining-an-amazon-s3-metadata-index-without-servers/

Check out these AWS Comparison Cheat Sheets:
https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai/
https://tutorialsdojo.com/ec2-container-service-ecs-vs-lambda/

</details>

<a id="q70"></a>

## Q70

A leading online media company runs a popular sports news website. The solutions architect has been tasked to analyze each web visitor’s clickstream data on the website to populate user analytics, which gives insights about the sequence of pages and advertisements the visitor has clicked. The data will be processed in real-time which will then transform the page layout as the visitors click through the web portal to increase user engagement and consequently, increase the revenue for the company. 
Which of the following options should the solutions architect implement to meet the above requirements?

- **A.** Publish web clicks by session to an Amazon SQS queue and periodically drain these events to Amazon RDS then analyze with SQL.
- **B.** Log clicks in weblogs by URL and store it in Amazon S3, and then analyze with Elastic MapReduce.
- **C.** Push web clicks by session to Amazon Kinesis and analyze behavior using Amazon Kinesis workers.
- **D.** Publish the web clicks to Amazon Timestream. Run custom analysis, SQL queries and apply machine learning to generate relevant reports regarding user behavior.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** clickstream real-time layout changes

⚠️ **Watch:** SQS/EMR are not real time

🧠 **Rule:** Kinesis + Kinesis consumers.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Sports news website: click stream (sequence pages/ads đã click)
Yêu cầu: xử lý REAL-TIME để biến đổi page layout ngay khi user click
          (tăng engagement, tăng revenue)

Đáp án đúng: C
  Push web clicks by session → Amazon Kinesis
  Analyze behavior bằng Kinesis workers (consumer)
Anh chọn đúng C.
```

#### Vì sao C đúng

```
Browser (click, scroll)
     │  SDK (ví dụ putRecords)
     ▼
Amazon Kinesis Data Stream
     │
     ▼
Kinesis workers (EC2 hoặc consumer app)  ──► xử lý real-time
     │
     ▼
Thay đổi page layout NGAY  +  lưu vào DynamoDB/Redshift (nếu cần)
```

Kinesis được mô tả đúng vai trò: "ingest real-time data such as... website clickstreams... process and analyze data as it arrives and responds instantly instead of having to wait until all your data is collected". Đây khớp 100% với yêu cầu "transform the page layout as the visitors click through" — tức phải xử lý **ngay khi** sự kiện xảy ra, không có khoảng trễ.

#### Vì sao từng đáp án sai bị loại

TD explanation nói rõ: "SQS, EC2, EMR, and Timestream services **do not have the capacity to analyze real-time streaming data**" theo cách phù hợp ở đây.

- **A (SQS → periodically drain → RDS → SQL):** có bước **"periodically drain"** — nghĩa là xử lý theo lô định kỳ, **không phải real-time**. SQS vốn là hàng đợi message, không chuyên cho streaming analytics liên tục.
- **B (weblog → S3 → Elastic MapReduce):** EMR là batch processing framework (Hadoop/Spark trên cluster) — mô hình "ghi log rồi phân tích sau" là **batch, không real-time**.
- **D (publish vào Amazon Timestream, rồi custom SQL/ML):** Timestream là time-series database tối ưu cho lưu & query dữ liệu theo thời gian, nhưng **không phải dịch vụ streaming xử lý real-time** theo mô tả ở đây — vẫn là mô hình lưu rồi phân tích, thiếu lớp xử lý tức thời như Kinesis.

#### So sánh nhanh

| Đáp án | Cơ chế | Real-time? | Vấn đề |
|---|---|---|---|
| **C** | Kinesis + Kinesis workers | **Có** | Đúng |
| A | SQS → drain định kỳ → RDS | Không | "Periodically" = batch, có trễ |
| B | S3 log → EMR | Không | EMR là batch processing |
| D | Timestream → SQL/ML | Không (theo mô tả) | Vẫn là lưu rồi phân tích sau |

#### Lưu ý thực tế

⚠️ **Dễ nhầm — cùng nhóm lỗi với Q24 (sai) và Q58:** khi đề yêu cầu xử lý dữ liệu **streaming/real-time** (clickstream, cảm biến gửi liên tục...), đáp án đúng luôn thuộc nhà **Kinesis** (Data Streams / Firehose / Data Analytics) — **không phải AWS Step Functions**. Step Functions dùng để orchestrate một workflow nhiều bước có trạng thái (state machine), không phải để ingest/xử lý luồng dữ liệu liên tục tốc độ cao. Nếu thấy đề nói "ingest continuous stream of events" → nghĩ ngay Kinesis, không phải Step Functions.

- "SQS + periodically drain" là mẫu câu hay xuất hiện để đánh lừa — trông có vẻ xử lý được nhưng bản chất là batch có độ trễ, không đạt real-time.

#### Quy tắc nhớ cho thi

- **Thấy "real-time" + "clickstream"/"streaming data"** → **Amazon Kinesis** (Data Streams + workers/consumers)
- **Thấy "periodically" / "drain theo lô"** → đó là **batch**, không phải real-time, loại nếu đề yêu cầu real-time
- **Thấy "streaming ingestion"** → luôn là **Kinesis**, không bao giờ là Step Functions

### TD explanation

Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information. Amazon Kinesis offers key capabilities to cost-effectively process streaming data at any scale, along with the flexibility to choose the tools that best suit the requirements of your application. With Amazon Kinesis, you can ingest real-time data such as video, audio, application logs, website clickstreams, and IoT telemetry data for machine learning, analytics, and other applications. Amazon Kinesis enables you to process and analyze data as it arrives and responds instantly instead of having to wait until all your data is collected before the processing can begin.
In this example, a simple HTML page simulates the content of a blog page. As the reader scrolls the simulated blog post, the browser script uses the SDK for JavaScript to record the scroll distance down the page and send that data to Kinesis using the putRecords method of the Kinesis client class. The streaming data captured by Amazon Kinesis Data Streams can then be processed by Amazon EC2 instances and stored in any of several data stores including Amazon DynamoDB and Amazon Redshift.

Therefore, the correct answer is: Push web clicks by session to Amazon Kinesis and analyzing behavior using Amazon Kinesis workers.
The following options are incorrect as SQS, EC2, EMR, and Timestream services do not have the capacity to analyze real-time streaming data:
– Log clicks in weblogs by URL and store it in Amazon S3, and then analyze with Elastic MapReduce.
– Publish the web clicks to Amazon Timestream. Run custom analysis, SQL queries and apply machine learning to generate relevant reports regarding user behavior.
– Publish web clicks by session to an Amazon SQS queue and periodically drain these events to Amazon RDS then analyze with SQL.
References:
https://docs.aws.amazon.com/streams/latest/dev/introduction.html
https://aws.amazon.com/kinesis/data-streams/
https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/kinesis-examples-capturing-page-scrolling.html

Check out this Amazon Kinesis Cheat Sheet:
https://tutorialsdojo.com/amazon-kinesis/

</details>

<a id="q73"></a>

## Q73

A global real estate startup is looking for an option of adding a cost-effective location-based alert to iOS and Android mobile apps. Users will receive push notifications on mobile devices regarding real estate offers in proximity to current locations, with delivery expected in under a minute. The existing mobile app has an initial 2 million users worldwide and is rapidly growing. The team considered using AWS Wavelength for edge processing of location data but chose a simpler queuing approach to reduce costs.
What is the most suitable architecture to use in this scenario?

- **A.** Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app.
- **B.** Set up an architecture where the mobile app will send the user's location to an Amazon API Gateway with AWS Lambda functions that process and retrieve the relevant offers from an Amazon RDS database. Once the data has been processed, use Amazon Pinpoint to send out the offers to the mobile app.
- **C.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use AWS SNS Mobile Push to send out the offers to the mobile app.
- **D.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** location-based push to millions; <1 min; cheap

⚠️ **Watch:** Device Farm is a testing service

🧠 **Rule:** SQS + workers + DynamoDB + SNS Mobile Push.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Real estate app: location-based push notification
2 triệu user toàn cầu, tăng nhanh
Delivery < 1 phút, cost-effective
(team đã loại AWS Wavelength, chọn simple queuing approach)

Đáp án đúng: C
  Mobile app → Amazon SQS queue
  Fleet On-Demand EC2 → đọc offer từ Amazon DynamoDB
  Push offer → AWS SNS Mobile Push
Anh chọn đúng C.
```

#### Vì sao C đúng

```
Mobile app (iOS/Android) gửi location
          │
          ▼
    Amazon SQS queue   ◄── "highly scalable, cost-effective... holding
          │                 the location of millions of users"
          ▼
Fleet EC2 On-Demand ──► query Amazon DynamoDB (offer gần vị trí user)
          │                 (highly scalable NoSQL cho tải lớn, scale)
          ▼
    AWS SNS Mobile Push ──► gửi push notification đến device
```

Mỗi thành phần đóng đúng vai trò: **SQS** chịu tải ghi vị trí từ 2 triệu+ user mà không cần provision trước; **DynamoDB** scale tốt cho truy vấn offer khối lượng lớn; **SNS Mobile Push** "send push notification messages directly to apps on mobile devices" — đúng chính xác chức năng cần: gửi alert đến mobile endpoint.

#### Vì sao từng đáp án sai bị loại

- **A (API Gateway + ASG EC2 + RDS + AppSync để push):** sai ở bước cuối — dùng **AWS AppSync để gửi push notification là không đúng**; AppSync là GraphQL API service, không phải dịch vụ push notification. Phải dùng SNS Mobile Push.
- **B (API Gateway + Lambda + RDS + Amazon Pinpoint):** Pinpoint dùng để push đúng chức năng, nhưng **RDS không scale tốt** cho dữ liệu location từ user toàn cầu so với DynamoDB — "mobile applications do not have complicated table relationships hence, it is recommended to use a NoSQL database like DynamoDB".
- **D (SQS + EC2 + Aurora + AWS Device Farm để push):** **AWS Device Farm là dịch vụ test app** trên nhiều thiết bị thật/ảo — hoàn toàn không liên quan đến gửi push notification. Đây là sai nghiêm trọng nhất về chức năng dịch vụ.

#### So sánh nhanh

| Đáp án | Ingestion | DB | Push service | Vấn đề |
|---|---|---|---|---|
| **C** | SQS | DynamoDB | **SNS Mobile Push** | Đúng |
| A | API Gateway | RDS | AppSync (sai) | AppSync không phải push service |
| B | API Gateway + Lambda | RDS (kém scale) | Pinpoint (đúng chức năng) | RDS kém scale hơn DynamoDB cho data toàn cầu |
| D | SQS | Aurora | Device Farm (sai hoàn toàn) | Device Farm là test service |

#### Lưu ý thực tế

- ⚠️ **AWS Device Farm chỉ là dịch vụ app testing** (test/reproduce issue trên nhiều device thật/giả lập) — tuyệt đối không dùng để gửi notification. Nếu thấy "Device Farm" đi với "send out the offers/push" trong option → luôn sai.
- Amazon Pinpoint và SNS Mobile Push đều push được tới mobile, nhưng khi đề nhấn "cost-effective" + pattern SQS→worker→NoSQL, SNS Mobile Push thường là lựa chọn kinh điển hơn trong các câu dạng pattern cũ của Tutorials Dojo.

#### Quy tắc nhớ cho thi

- **Thấy "push notification tới mobile app"** → **SNS Mobile Push** hoặc **Amazon Pinpoint**, không bao giờ là AppSync hay Device Farm
- **Thấy "location data từ triệu user toàn cầu"** → **DynamoDB** thắng RDS/Aurora vì scale tốt hơn, không cần complex relationship
- **Thấy "Device Farm"** → luôn là app testing service, không liên quan push/notification

### TD explanation

With Amazon SNS Mobile Push Notifications, you have the ability to send push notification messages directly to apps on mobile devices. Push notification messages sent to a mobile endpoint can appear in the mobile app as message alerts, badge updates, or even sound alerts.

Hence, the correct answer is: Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use AWS SNS Mobile Push to send out the offers to the mobile app because SQS is a highly scalable, cost-effective solution for carrying out utility tasks such as holding the location of millions of users. In addition, it uses a highly scalable DynamoDB table and a cost-effective AWS SNS Mobile Push service to send push notification messages directly to the mobile apps.
The option that says: Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app is incorrect. Although a combination of On-Demand EC2 instances and API Gateway can provide a scalable computing system, it is wrong to use AWS AppSync for push notification to mobile devices. You should use AWS SNS Mobile Push service instead.
The option that says: Set up an architecture where the mobile app will send the user’s location to an Amazon API Gateway with AWS Lambda functions that process and retrieve the relevant offers from an Amazon RDS database. Once the data has been processed, use Amazon Pinpoint to send out the offers to the mobile app is incorrect. Although it is correct to use Amazon Pinpoint to send push notifications, RDS is not a suitable database for the mobile app because it is not as scalable enough when processing data from various users around the globe, compared with DynamoDB. Usually, mobile applications do not have complicated table relationships hence, it is recommended to use a NoSQL database like DynamoDB.
The option that says: Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app is incorrect because AWS Device Farm is an app testing service and is not simply used to push notifications to various mobile devices. It only lets you test and interact with your Android, iOS, and web apps on many devices at once, or reproduce issues on a device in real-time.
References:
https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html
https://docs.aws.amazon.com/sns/latest/dg/mobile-push-pseudo.html
https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html

Check out this Amazon SNS Cheat Sheet:
https://tutorialsdojo.com/amazon-sns/

</details>

<a id="q74"></a>

## Q74

A weather forecasting agency established a network of IoT devices in the ocean to help predict incoming typhoons. The IoT devices monitor the sea surface temperature and atmospheric pressure and send the data as messages to AWS IoT Core, which updates an Amazon DynamoDB table. On the weekly monitoring report, a system administrator notices that no new database updates are happening. The agency already uses AWS IoT Device Defender to audit device security policies and detect abnormal behavior, but this does not help diagnose connectivity interruptions.
What should the administrator do to troubleshoot the issue?

- **A.** Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core.
- **B.** Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click.
- **C.** Register the IoT devices to AWS IoT Device Management and monitor the devices' health and ensure the devices are connected to AWS IoT Core.
- **D.** Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** IoT devices stopped updating DynamoDB

⚠️ **Watch:** Device Defender is security auditing

🧠 **Rule:** Device health/connectivity → IoT Device Management.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IoT devices (ngoài biển) → AWS IoT Core → update DynamoDB table
Agency đã dùng AWS IoT Device Defender (audit security policy, detect
abnormal behavior) nhưng KHÔNG giúp chẩn đoán connectivity interruption

Vấn đề: báo cáo hàng tuần cho thấy KHÔNG có update mới nào
Cần: troubleshoot nguyên nhân

Đáp án đúng: C
  Register devices vào AWS IoT Device Management
  Monitor device health, đảm bảo devices connected tới IoT Core
Anh chọn đúng C.
```

#### Vì sao C đúng

```
IoT Device Management
  → "securely register, organize, MONITOR, and remotely manage
     IoT devices at scale throughout their lifecycle"
  → upload/view device info, monitor fleet, TROUBLESHOOT individual
     devices, remotely manage devices deployed across many locations
          │
          ▼
  Xác định: devices có đang connected tới IoT Core không?
          │
          ▼
  → tìm ra nguyên nhân mất update: devices offline/disconnect
```

Đây đúng loại công cụ để chẩn đoán **connectivity** — thứ mà Device Defender (đã dùng, chỉ về security audit) không làm được. Việc không có update mới trong DynamoDB nhiều khả năng do thiết bị **mất kết nối tới IoT Core**, và IoT Device Management là dịch vụ chuyên giám sát health/connectivity của fleet thiết bị ở quy mô lớn.

#### Vì sao từng đáp án sai bị loại

- **D (dùng IoT Device Defender thêm Certificate Authority, "establish connectivity"):** sai bản chất — Device Defender **chỉ dùng cho security audit, alerting, mitigation**, không quản lý Certificate Authority trong IoT Core và **không dùng để establish connectivity** giữa device và IoT Core. Đề bài đã nói rõ Device Defender hiện tại "does not help diagnose connectivity interruptions" — đáp án D cố gắng ép Device Defender làm việc nó không làm được.
- **A (AWS IoT SiteWise thu thập data trực tiếp từ devices):** IoT SiteWise dùng để "collecting and gaining insights to equipment data for **industrial operations management**" — không phải dịch vụ thu thập data từ IoT devices nói chung, và không giải quyết vấn đề connectivity.
- **B (Lambda + IoT 1-Click update trực tiếp vào DynamoDB):** cách này **bypass AWS IoT Core hoàn toàn** — không giải quyết nguyên nhân gốc (connectivity giữa devices và IoT Core), chỉ che giấu triệu chứng bằng cách ghi thẳng vào DB.

#### So sánh nhanh

| Đáp án | Dịch vụ | Vấn đề |
|---|---|---|
| **C** | IoT Device Management | Đúng — chuyên monitor health/connectivity fleet |
| A | IoT SiteWise | Dành cho industrial equipment data, không phải troubleshoot connectivity |
| B | Lambda + IoT 1-Click | Bypass IoT Core, không chẩn đoán được nguyên nhân |
| D | IoT Device Defender (mở rộng sai) | Device Defender chỉ security audit, không quản lý connectivity |

#### Lưu ý thực tế

- ⚠️ **AWS IoT Device Defender vs AWS IoT Device Management** là cặp dễ nhầm: Device Defender = security (audit policy, detect abnormal behavior, certificate/security issue); Device Management = operations (register, organize, monitor health, troubleshoot connectivity, remote manage, OTA update). Khi đề cần "troubleshoot connectivity/health" → luôn là Device Management.
- AWS IoT SiteWise chỉ liên quan ngành công nghiệp (industrial equipment monitoring), không phải dịch vụ ingest chung cho mọi loại IoT sensor.

#### Quy tắc nhớ cho thi

- **Thấy "device ngừng gửi data" / "troubleshoot connectivity/health của fleet IoT"** → **AWS IoT Device Management**
- **Thấy "audit security policy / detect abnormal behavior / certificate security"** → **AWS IoT Device Defender** (nhưng KHÔNG dùng để fix connectivity)
- **Thấy "industrial equipment data"** → **AWS IoT SiteWise**, không phải data IoT chung

### TD explanation

AWS IoT Device Management is a service that makes it easy to securely register, organize, monitor, and remotely manage IoT devices at scale throughout their lifecycle. You can use IoT Device Management to upload and view device information and configuration, organize your device inventory, monitor your fleet of devices, troubleshoot individual devices, and remotely manage devices deployed across many locations, including updating device software over-the-air (OTA).
By registering the IoT devices to AWS IoT Device Management, the system administrator can monitor the health of the devices and ensure connectivity to AWS IoT Core. This will help identify if there are connectivity issues that might be causing the lack of updates in the DynamoDB table.

AWS IoT Device Management has a feature that allows you to group your device fleet based on function, security requirements, or other categories. This makes it easier to manage IoT devices at scale. The groupings allow policy management, viewing metrics, or performing actions on the entire group.
Therefore, the correct answer is: Register the IoT devices to AWS IoT Device Management and monitor the devices’ health and ensure the devices are connected to AWS IoT Core.
The option that says: Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity is incorrect. AWS IoT Defender is primarily used for security audit, alerting, and mitigation of IoT resources and does not directly manage Certificate Authority in AWS IoT Core. It is also not used for establishing connectivity between the devices and AWS IoT Core.
The option that says: Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core is incorrect. AWS IoT SiteWise is simply used for collecting and gaining insights to equipment data for industrial operations management. It is not used for collecting data from IoT devices.
The option that says: Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click is incorrect. Triggering a Lambda function does not address the potential connectivity issue between the IoT devices and AWS IoT Core. Using it to directly update the DynamoDB table will bypass AWS IoT Core and is not the solution to the question.
References:
https://aws.amazon.com/iot-device-management/faq/
https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html

Check out this AWS IoT Core Cheat Sheet:
https://tutorialsdojo.com/aws-iot-core/

</details>

---

# Group F — Storage, migration & ops (6)

<a id="q4"></a>

## Q4

A company is running 150 virtual machines (VMs) using 40 TB of storage on its on-premises data center. The company wants to migrate its whole environment to AWS within the next three months. The VMs are mainly used during business hours only, so these can be taken offline, but some are mission-critical, which means that the downtime needs to be minimized. Since upgrading the Internet connection is quite costly for the company, the on-premises network administrator provisioned only a 12 Mbps Internet bandwidth for the migration. The Solutions Architect must design a cost-effective plan to complete the migration within the target time frame. The migration team has already installed the AWS Application Discovery Agent on its on‑premises servers to collect performance and dependency data.
Which of the following options should the Solutions Architect implement to fulfill the requirements?

- **A.** Deploy the AWS Agentless Discovery connector on the company VMware vCenter to assess each application. With the information gathered, refactor each application to run on AWS services or using AWS Marketplace solutions.
- **B.** Request a 1 Gbps AWS Direct Connect connection from the on-premises data center to AWS. Create a private virtual interface on Direct Connect. Migrate the virtual machines to AWS using the AWS Transform MGN.
- **C.** Create an export of your virtual machines during out of office hours. Use the AWS Transfer service to securely upload the VMs to Amazon S3 using the SFTP protocol. Import the VMs into Amazon EC2 instances using the VM Import/Export service.
- **D.** Use AWS Transform MGN to migrate the mission‑critical virtual machines to AWS. For the non‑mission‑critical VMs, export them and schedule a reservation with AWS Data Transfer Terminal to upload the data at the facility. Once the VMs are on Amazon S3, import the VMs into Amazon EC2 instances using the VM Import/Export service.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** 150 VMs, 40 TB, 12 Mbps, 3 months; some mission-critical

⚠️ **Watch:** DX takes weeks and costs more

🧠 **Rule:** MGN for critical VMs + offline bulk transfer + VM Import for the rest.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: 150 VMs, 40 TB storage
Internet bandwidth: chỉ 12 Mbps (nâng cấp quá đắt)
Deadline: 3 tháng
Một số VM là mission-critical → downtime phải TỐI THIỂU
```

Yêu cầu: kế hoạch migration **cost-effective** mà vẫn kịp deadline. Đáp án đúng: **D** — dùng **AWS Transform MGN** cho VM mission-critical + **AWS Data Transfer Terminal** (chuyển offline vật lý) cho VM còn lại + **VM Import/Export** để đưa vào EC2. Anh chọn đúng D.

#### Vì sao D đúng

- **Bài toán băng thông**: 40 TB qua kết nối 12 Mbps sẽ tốn **nhiều tháng** để truyền qua Internet — vượt xa deadline 3 tháng, nên không thể dùng cách upload online cho toàn bộ 40 TB.
- **Chia hai nhóm xử lý khác nhau theo đúng đặc tính:**
  - VM mission-critical (cần downtime tối thiểu) → **AWS Transform MGN**: replicate server sang AWS rồi launch, hạn chế downtime khi cutover.
  - VM không mission-critical (số lượng/khối lượng còn lại, không cần downtime thấp tuyệt đối) → export VM, **đặt lịch tại AWS Data Transfer Terminal** để upload dữ liệu vật lý tại chỗ (offline, không phụ thuộc 12 Mbps) → sau đó **VM Import/Export** convert VM thành EC2 AMI.
- Kết hợp hai công cụ này vừa đáp ứng deadline (bỏ qua giới hạn băng thông cho phần lớn dữ liệu), vừa giữ downtime thấp cho phần quan trọng, vừa **cost-effective** (không cần nâng cấp Internet connection đắt đỏ).

#### Vì sao từng đáp án sai bị loại

- **B sai** vì yêu cầu **1 Gbps Direct Connect** mới — tuy giải quyết được bài toán băng thông và deadline, nhưng **không cost-effective**: đề đã nói rõ nâng cấp Internet là tốn kém cho công ty, và DX cần thời gian provision + chi phí hàng tháng không nhỏ.
- **A sai** vì **refactor từng application** để chạy trên AWS service/Marketplace là nỗ lực lập kế hoạch rất lớn, tốn effort matching từng app với từng AWS service, dễ gây gián đoạn trong lúc migrate — không phù hợp với deadline 3 tháng chặt.
- **C sai** vì dùng **AWS Transfer (SFTP) để upload toàn bộ 40 TB qua Internet 12 Mbps** — với băng thông này, việc upload sẽ mất **nhiều hơn 3 tháng**, không kịp deadline.

#### So sánh nhanh

| Đáp án | Cách chuyển 40 TB | Đáp ứng deadline 3 tháng? | Cost-effective? |
|---|---|---|---|
| **D (đúng)** | MGN (critical) + Data Transfer Terminal offline (còn lại) | Có | Có |
| B | Direct Connect 1 Gbps | Có | Không — tốn phí DX |
| C | SFTP qua 12 Mbps Internet | Không — quá chậm | — |
| A | Refactor từng app sang AWS service | Không thực tế trong 3 tháng | — |

#### Lưu ý thực tế

- **AWS Data Transfer Terminal** là facility vật lý: đặt lịch, mang thiết bị lưu trữ tới, upload dữ liệu tại chỗ — giải pháp offline khi Internet bandwidth quá thấp so với khối lượng dữ liệu cần chuyển.
- **AWS Transform MGN** chuyên cho lift-and-shift ít downtime; sau khi lên AWS mới replatform/refactor tiếp nếu cần — không nên refactor ngay từ đầu khi mục tiêu chính là di chuyển đúng hạn.

#### Quy tắc nhớ cho thi

- **"Dữ liệu lớn, băng thông thấp, deadline gấp"** → tính thời gian truyền qua Internet trước; nếu vượt deadline → cần giải pháp **offline/vật lý** (Data Transfer Terminal, Snowball...)
- **"VM mission-critical cần downtime tối thiểu"** → **AWS Transform MGN**
- **"Không cost-effective"** → loại ngay phương án yêu cầu nâng cấp kết nối mạng (Direct Connect mới) khi đề đã nói rõ ngân sách hạn chế

### TD explanation

AWS Transform MGN (MGN) is an automated lift-and-shift solution that simplifies and speeds up the migration of applications to AWS, reducing costs. It enables businesses to move physical, virtual, or cloud servers without compatibility issues or performance disruptions. MGN replicates source servers to AWS and automatically launches them, allowing immediate benefits from cloud agility and cost savings. After migration, companies can easily replatform or refactor their applications using AWS services for faster modernization.

The AWS Data Transfer Terminal is a network-ready, physical facility where you can bring your data storage devices for quick transfers to and from AWS Cloud services. This service allows you to upload data collected remotely, making it easier to access that information.

To use the Data Transfer Terminal, schedule a reservation at one of the facilities through the AWS Management Console. Arrive at your scheduled time and upload your data to your AWS Cloud services using your devices. Once your reservation is complete and you leave the facility, it will be re-secured and prepared for the next scheduled appointment.
AWS VM Import/Export enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances and export them back to your on-premises environment. VM Import/Export is available at no additional charge beyond standard usage charges for Amazon EC2 and Amazon S3. As part of the import process, VM Import will convert your VM into an Amazon EC2 AMI, which you can use to run Amazon EC2 instances.
Therefore, the correct answer is: Use AWS Transform MGN to migrate the mission‑critical virtual machines to AWS. For the non‑mission‑critical VMs, export them and schedule a reservation with AWS Data Transfer Terminal to upload the data at the facility. Once the VMs are on Amazon S3, import the VMs into Amazon EC2 instances using the VM Import/Export service. AWS Transform MGN minimizes downtime for mission‑critical workloads, while AWS Data Transfer Terminal provides a cost‑effective offline transfer solution for the bulk 40 TB dataset. This offline transfer is necessary to meet the requirement since the available Internet bandwidth is only 12 Mbps, which would otherwise make the migration impossible within the three‑month timeframe. This hybrid approach meets the deadline and balances both cost and downtime requirements.
The option that says: Request a 1 Gbps AWS Direct Connect connection from the on-premises data center to AWS. Create a private virtual interface on Direct Connect. Migrate the virtual machines to AWS using the AWS Transform MGN is incorrect. Although this is a fast solution that can typically finish the migration within the required time frame, it is not the most cost-effective solution. As stated in the question, upgrading the Internet connection (and probably requesting a new connection) is costly for the company. Moreover, the requirement is to migrate to virtual machines and not to establish a fast, dedicated network connection from the on-premises network to AWS.
The option that says: Deploy the AWS Agentless Discovery connector on the company VMware vCenter to assess each application. With the information gathered, refactor each application to run on AWS services or using AWS Marketplace solutions is incorrect. This requires a lot of effort for planning since you will have to match each application to the AWS service. This will just require changes in the application and can cause possible interruptions during the migration.
The option that says: Create an export of your virtual machines during out of office hours. Use the AWS Transfer service to securely upload the VMs to Amazon S3 using the SFTP protocol. Import the VMs into Amazon EC2 instances using the VM Import/Export service is incorrect. Although this is possible, with the 12 Mbps Internet connection, it will take more than three months to upload all the 40 TB worth of VM storage to an Amazon S3 bucket.

References:
https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html
https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html
https://aws.amazon.com/ec2/vm-import/

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/aws-cheat-sheets/

</details>

<a id="q16"></a>

## Q16

A company uses a CloudFormation script to deploy an online voting application. The app is used for a Nature Photography Contest that accepts high-resolution images, stores them in an S3 bucket, and records a 100-character summary about the image in RDS. The Solutions Architect must ensure that the same online voting application can be deployed once again using the same CloudFormation template for succeeding contests in the future. The photography contest will run for just a month and once it has been concluded, there would be nobody using the online voting application anymore until the next contest. As preparation for the upcoming events next year, the 100-character summaries should be kept and the S3 bucket, which contains the high-resolution photos, should remain. 
Which of the following options is the recommended action to meet the above requirement?

- **A.** 1. Enable Cross-Region Replication (CRR) in the S3 bucket to maintain a copy of all the S3 objects. 2. Set the DeletionPolicy for the RDS instance to Snapshot.
- **B.** 1. Set the DeletionPolicy on the S3 resource declaration in the CloudFormation template to Retain. 2. Set the RDS resource declaration DeletionPolicy to Snapshot.
- **C.** For both the RDS and S3 resource types on the CloudFormation template, set the DeletionPolicy to Retain.
- **D.** 1. Set the DeletionPolicy on the S3 resource to Snapshot. 2. Set the DeletionPolicy on the RDS resource to Snapshot.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** keep S3 photos and RDS summaries after stack delete

⚠️ **Watch:** S3 has no Snapshot policy

🧠 **Rule:** DeletionPolicy: Retain for S3, Snapshot for RDS.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CloudFormation stack: Voting app
   ├── S3 bucket (ảnh độ phân giải cao)
   └── RDS (tóm tắt 100 ký tự)

Contest chạy 1 tháng/năm → stack bị DELETE sau mỗi contest
Yêu cầu: sau khi xóa stack, S3 bucket PHẢI GIỮ, RDS data PHẢI GIỮ (để dùng lại năm sau)
```

Đáp án đúng: **B** — set `DeletionPolicy: Retain` cho resource S3, `DeletionPolicy: Snapshot` cho resource RDS. Anh chọn đúng B.

#### Vì sao B đúng

- `DeletionPolicy` là attribute của CloudFormation cho phép quyết định điều gì xảy ra với resource khi stack bị xóa (hoặc khi resource bị remove khỏi template và update stack).
- **S3 → `Retain`**: S3 **không hỗ trợ snapshot**, nên cách duy nhất để giữ bucket (và toàn bộ object trong đó) khi xóa stack là `Retain` — CloudFormation sẽ không xóa bucket, chỉ gỡ nó khỏi quản lý của stack.
- **RDS → `Snapshot`**: CloudFormation tự động tạo snapshot của DB instance trước khi xóa — vừa giữ lại dữ liệu (tóm tắt 100 ký tự), vừa **không phải duy trì RDS instance chạy liên tục** suốt thời gian không có contest (tiết kiệm chi phí, vì RDS instance tính phí theo giờ chạy dù không ai dùng).

#### Vì sao từng đáp án sai bị loại

- **D sai** vì set `Snapshot` cho **cả S3 và RDS** — nhưng **S3 không hỗ trợ DeletionPolicy Snapshot**; option này không khả thi về mặt kỹ thuật cho resource S3.
- **C sai** vì set `Retain` cho **cả hai resource** — về mặt kỹ thuật vẫn giữ được dữ liệu, nhưng gây **chi phí vận hành không cần thiết**: RDS instance vẫn tiếp tục chạy (và tính phí) suốt cả năm dù contest chỉ diễn ra 1 tháng và không ai dùng ứng dụng ngoài thời gian đó. Nên dùng Snapshot cho RDS để không phải duy trì instance chạy liên tục.
- **A sai** vì dùng **Cross-Region Replication (CRR)** để giữ bản sao S3 object ở region khác — nhưng khi stack bị xóa, **bucket gốc vẫn bị xóa** (CRR chỉ sao chép, không ngăn xóa bucket nguồn); dữ liệu "còn" nhưng ở một bucket/region khác, không đúng ý "S3 bucket vẫn còn" như đề yêu cầu.

#### So sánh nhanh

| Đáp án | DeletionPolicy S3 | DeletionPolicy RDS | Vấn đề |
|---|---|---|---|
| **B (đúng)** | Retain | Snapshot | Không |
| C | Retain | Retain | RDS vẫn chạy tốn phí không cần thiết |
| D | Snapshot | Snapshot | S3 không hỗ trợ Snapshot |
| A | CRR (không phải DeletionPolicy) | Snapshot | Bucket gốc vẫn bị xóa |

#### Lưu ý thực tế

- `DeletionPolicy` cũng áp dụng khi resource bị **remove khỏi template rồi update stack** (không chỉ khi xóa nguyên stack), nhưng **không áp dụng** khi resource bị **replace** trong lúc update (ví dụ đổi property khiến CloudFormation phải tạo lại resource mới).
- Nếu resource không có `DeletionPolicy`, CloudFormation **xóa resource theo mặc định** khi xóa stack — luôn cần set rõ khi muốn giữ dữ liệu quan trọng.

#### Quy tắc nhớ cho thi

- **S3 bucket cần giữ lại khi xóa stack** → `DeletionPolicy: Retain` (S3 không có Snapshot)
- **RDS cần giữ dữ liệu nhưng không cần instance chạy liên tục** → `DeletionPolicy: Snapshot`
- **"Retain cả hai" trông "an toàn" nhưng tốn phí** → cân nhắc Snapshot cho resource có hỗ trợ (RDS, EBS...) để tiết kiệm chi phí vận hành

### TD explanation

With the DeletionPolicy attribute, you can preserve or (in some cases) back up a resource when its stack is deleted. You specify a DeletionPolicy attribute for each resource that you want to control. If a resource has no DeletionPolicy attribute, AWS CloudFormation deletes the resource by default.

Note that this capability also applies to stack update operations that lead to resources being deleted from stacks, for example, if you remove the resource from the stack template and then update the stack with the template. This capability does not apply to resources whose physical instance is replaced during stack update operations. For example, if you edit a resource’s properties such that AWS CloudFormation replaces that resource during a stack update.
In this scenario, you need to keep the data on your S3 bucket and RDS which can be achieved by setting the DeletionPolicy of S3 to Retain and for RDS to use Snapshot.
Setting the DeletionPolicy on the S3 resource to Snapshot and for RDS resource to use Snapshot is incorrect because S3 does not support snapshots. It should be set to Retain.
For both the RDS and S3 resource types on the CloudFormation template, setting the DeletionPolicy to Retain is incorrect. Although you can set Retain on both the DeletionPolicy of the S3 bucket and the RDS database, this entails an unnecessary operating cost since the RDS database will still be running even if it is not used. Take note that the application is meant to run for just a month and once it has been concluded, nobody would be using it until the next contest next year. The RDS should be set to Snapshot.
Enabling Cross-Region Replication (CRR) in the S3 bucket to maintain a copy of all the S3 objects and setting the DeletionPolicy for the RDS instance to Snapshot is incorrect because even though your data will still be available in the other region because of the CRR, the current S3 bucket will still be deleted.

References:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html
https://aws.amazon.com/premiumsupport/knowledge-center/delete-cf-stack-retain-resources/

Check out this AWS CloudFormation Cheat Sheet:
https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q25"></a>

## Q25

A company has a hybrid cloud architecture where their on-premises data center and VPC are connected via multiple AWS Direct Connect ports in a single Link Aggregation Group (LAG). They have an on-premises patch management system that automatically applies the patches to the operating systems of their servers and file systems. You were given a task to synchronize the patch baselines being used on-premises to all of the EC2 instances in your VPC, as well as to automate the patching schedule.
Which of the following methods should you implement to meet the above requirement with the LEAST amount of effort?

- **A.** Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by setting up scheduled jobs using AWS Lambda and AWS Systems Manager Run Command.
- **B.** Use AWS Systems Manager Session Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by using the AWS Systems Manager Maintenance Windows.
- **C.** Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Install the SSM Agent to all of your instances and automate the patching schedule by using AWS Systems Manager Maintenance Windows.
- **D.** Use the AWS Systems Manager State Manager to automate the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define, which includes the OS patches that should be applied in each EC2 instance. Automate the patching schedule by using AWS Systems Manager Distributor, to package and distribute the required patches to your instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** sync on-prem patch baselines to EC2; schedule; least effort

⚠️ **Watch:** Session Manager isn't patching

🧠 **Rule:** Patch Manager + SSM Agent + Maintenance Windows.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises patch management (tự động) ──Direct Connect (LAG)──► VPC
                                                                    │
                                                            EC2 instances

Yêu cầu: sync patch baseline on-premises → EC2, TỰ ĐỘNG hóa lịch patching, LEAST effort
```

Đáp án đúng: **C** — dùng **AWS Systems Manager Patch Manager** (patch baseline on-prem), **cài SSM Agent** lên các EC2, và tự động hóa lịch bằng **Systems Manager Maintenance Windows**. Anh chọn đúng C.

#### Vì sao C đúng

- **Patch Manager** là service được thiết kế đúng cho việc "patch fleet of EC2/on-premises servers theo patch baseline" — hỗ trợ cả patch baseline tùy biến lấy từ môi trường on-premises.
- **SSM Agent phải được cài trên EC2** để Patch Manager hoạt động — đây là điều kiện bắt buộc, option đúng phải nêu rõ bước này.
- **Maintenance Windows** cho phép định nghĩa lịch (schedule), thời gian chạy tối đa (max duration), danh sách target và task — tự động hóa lịch patching mà không cần tự viết thêm logic scheduling nào khác, đúng tiêu chí "LEAST effort".

#### Vì sao từng đáp án sai bị loại

- **B sai** vì dùng **Session Manager** — service này dùng để **truy cập instance an toàn, có audit log** (ví dụ thay SSH/RDP truyền thống), **không phải** để apply OS patch. Dùng sai service cho mục đích patching.
- **A sai** vì tuy dùng đúng Patch Manager, nhưng lại **tự xây lịch bằng Lambda + Run Command** thay vì dùng **Maintenance Windows** có sẵn — tốn effort hơn (phải code, maintain Lambda) trong khi Maintenance Windows đã giải quyết đúng nhu cầu lập lịch. Ngoài ra option này cũng không nhắc tới việc cài SSM Agent.
- **D sai** vì **State Manager** dùng để duy trì EC2/hybrid infrastructure ở một **state định nghĩa sẵn** (config, software khi boot, network settings...) — không phải service chuyên patch OS. **Distributor** dùng để package/distribute software/patches, nhưng kết hợp State Manager + Distributor không phải là cách chuẩn và tối ưu để patch theo baseline như Patch Manager.

#### So sánh nhanh

| Đáp án | Service patch | Cách lập lịch | Vấn đề |
|---|---|---|---|
| **C (đúng)** | Patch Manager + SSM Agent | Maintenance Windows | Không |
| A | Patch Manager | Lambda + Run Command tự viết | Tốn effort hơn cần thiết |
| B | Session Manager (sai mục đích) | Maintenance Windows | Session Manager không patch OS |
| D | State Manager + Distributor | Distributor | Không phải service patch chuyên dụng |

#### Lưu ý thực tế

- SSM Agent là điều kiện bắt buộc cho hầu hết tính năng Systems Manager vận hành trên EC2/hybrid instance — luôn kiểm tra đáp án có nhắc tới việc cài agent khi liên quan tới Patch Manager, State Manager...
- Maintenance Windows còn hỗ trợ chỉ định time zone và các ngày "không chạy", rất phù hợp khi cần đồng bộ lịch patch với chính sách vận hành hiện có của tổ chức.

#### Quy tắc nhớ cho thi

- **"Patch EC2 theo baseline + tự động lịch, LEAST effort"** → **Patch Manager** + **SSM Agent** + **Maintenance Windows**
- **"Session Manager"** → chỉ để truy cập instance an toàn, **không** liên quan patch
- **"State Manager"** → duy trì state định nghĩa sẵn (config), **không** chuyên patch OS như Patch Manager

### TD explanation

AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

AWS Systems Manager Maintenance Windows let you define a schedule for when to perform potentially disruptive actions on your instances such as patching an operating system, updating drivers, or installing software or patches. Each Maintenance Window has a schedule, a maximum duration, a set of registered targets (the instances that are acted upon), and a set of registered tasks. You can also specify dates that a Maintenance Window should not run before or after, and you can specify the international time zone on which to base the Maintenance Window schedule.
Therefore, the correct answer is: Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Install the SSM Agent to all of your instances and automate the patching schedule by using AWS Systems Manager Maintenance Windows.
The option that says: Use AWS Systems Manager Session Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by using the AWS Systems Manager Maintenance Windows is incorrect because the Session Manager is primarily used to comply with corporate policies that require controlled access to instances, strict security practices, and fully auditable logs with instance access details, but not for applying OS patches. Using the AWS Systems Manager Patch Manager is a more appropriate solution to implement.
The option that says: Use AWS Systems Manager Patch Manager to manage and deploy the security patches of your EC2 instances based on the patch baselines from your on-premises data center. Automate the patching schedule by setting up scheduled jobs using AWS Lambda and AWS Systems Manager Run Command is incorrect. Although it properly uses AWS Systems Manager Patch Manager, it is still better to use AWS Systems Manager Maintenance Windows instead of manually creating scheduled jobs using AWS Lambda and AWS Systems Manager Run Command. Take note that the scenario specifies that you have to meet the requirement with the LEAST amount of effort, which can be met by using the AWS Systems Manager Maintenance Windows feature. In addition, installing the SSM Agent to all of your instances is also required when using the AWS Systems Manager Patch Manager, which is not mentioned in this option.
The option that says: Use the AWS Systems Manager State Manager to automate the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define, which includes the OS patches that should be applied in each EC2 instance. Automate the patching schedule by using AWS Systems Manager Distributor, to package and distribute the required patches to your instances is incorrect because the AWS Systems Manager State Manager is primarily used as a secure and scalable configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define. This does not handle patch management, unlike AWS Systems Manager Patch Manager. With the State Manager, you can configure your instances to boot with a specific software at start-up; download and update agents on a defined schedule; configure network settings and many others, but not the patching of your EC2 instances.

References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

Check out this AWS Systems Manager Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q33"></a>

## Q33

A company has built an application that allows painters to upload photos of original creations. The app allows users from North America and European regions to browse the galleries and order chosen artworks. The application is hosted on a fixed set of Amazon EC2 instances in the us-east-1 region. Using mobile phones, the artists can scan and upload large, high-resolution images, which are stored in a centralized Amazon S3 bucket also in the same region. After the initial week of operation, the European artists are reporting slow performance when uploading images.
Which of the following is the best solution to improve the image upload process?

- **A.** Enable S3 Transfer Acceleration on the central S3 bucket. Use the s3-accelerate endpoint to upload the images.
- **B.** Increase the upload capacity by creating an AWS Global Accelerator endpoint in front of the EC2 instances. Create an Auto Scaling Group that can scale automatically based on the users' traffic.
- **C.** Enable multipart upload on S3 and redeploy the application to support it. This allows the transmission of separate parts of the image in parallel.
- **D.** Set the centralized S3 bucket as the custom origin on an Amazon CloudFront distribution. This will use CloudFront’s global edge network to improve the upload speed.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** European artists slow uploading to us-east-1 bucket

⚠️ **Watch:** CloudFront isn't an upload accelerator for S3 here

🧠 **Rule:** Long-distance uploads → S3 Transfer Acceleration.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users (North America + Europe) ──mobile app──► Upload ảnh độ phân giải cao
                                                        │
                                                 S3 bucket tại us-east-1

Sau 1 tuần: European artists báo upload CHẬM
```

Yêu cầu: cải thiện tốc độ upload ảnh, đặc biệt cho người dùng ở xa (Europe) so với region của bucket (us-east-1). Đáp án đúng: **A** — bật **S3 Transfer Acceleration** trên bucket, dùng endpoint `s3-accelerate` để upload. Anh chọn đúng A.

#### Vì sao A đúng

- **S3 Transfer Acceleration** giải quyết chính xác vấn đề "transfer qua khoảng cách địa lý xa": nó tận dụng mạng lưới edge location toàn cầu của CloudFront, dữ liệu đi vào edge gần người dùng nhất rồi được route tới S3 qua **mạng backbone tối ưu của AWS**, thay vì đi theo đường Internet công khai thông thường tới us-east-1.
- Đây đúng use case AWS khuyến nghị: "khách hàng upload vào một bucket trung tâm từ khắp thế giới", "chuyển dữ liệu dung lượng lớn qua các lục địa" — khớp hoàn toàn với bài toán European artist upload ảnh lớn.
- Chỉ cần đổi endpoint upload thành `s3-accelerate.amazonaws.com` (hoặc bản dualstack IPv6), không cần thay đổi kiến trúc gì khác.

#### Vì sao từng đáp án sai bị loại

- **C sai** vì **multipart upload** giúp tăng throughput khi upload (chia file thành nhiều phần, upload song song) nhưng **không giải quyết được giới hạn khoảng cách địa lý** — người dùng Europe vẫn bị giới hạn bởi tốc độ kết nối Internet cố định của họ tới tận us-east-1, dù có chia nhỏ file hay không.
- **D sai** vì CloudFront **được thiết kế cho content delivery/caching**, không phải tối ưu upload. CloudFront hỗ trợ POST/PUT nhưng có **giới hạn timeout kết nối tới origin (60 giây)** — upload file lớn mất vài phút sẽ dễ bị timeout và connection bị cắt. Transfer Acceleration mới là giải pháp chính thức AWS khuyến nghị cho upload lớn, dù cả hai cùng dùng chung mạng lưới edge CloudFront.
- **B sai** vì Global Accelerator đặt trước **EC2 instances**, không liên quan gì tới việc ảnh được upload **trực tiếp vào S3** — tăng EC2 hay Auto Scaling cũng không cải thiện được tốc độ upload S3 từ một continent khác.

#### So sánh nhanh

| Đáp án | Cơ chế | Giải quyết đúng vấn đề? |
|---|---|---|
| **A (đúng)** | S3 Transfer Acceleration (dùng edge CloudFront để route tối ưu tới S3) | Có |
| C | Multipart upload | Không — vẫn bị giới hạn bởi khoảng cách địa lý |
| D | CloudFront làm origin custom cho S3 | Không — timeout 60s, không phải giải pháp upload chính thức |
| B | Global Accelerator trước EC2 | Không liên quan — ảnh upload trực tiếp vào S3, không qua EC2 |

#### Lưu ý thực tế

- Sau khi enable Transfer Acceleration, có thể mất tới **20 phút** mới thấy rõ hiệu năng cải thiện, nhưng **endpoint** đã dùng được ngay khi enable.
- Transfer Acceleration thực chất cũng dùng chung hạ tầng edge location của CloudFront — nhưng nó là một **tính năng riêng của S3** tối ưu cho PUT/GET object, khác với việc dùng CloudFront như một CDN/origin phía trước S3 (vốn có giới hạn timeout khi dùng cho upload).

#### Quy tắc nhớ cho thi

- **"Upload lớn, khoảng cách xa tới S3 bucket"** → **S3 Transfer Acceleration**, dùng endpoint `s3-accelerate`
- **"Multipart upload"** → chỉ tăng throughput cục bộ, không giải quyết latency do khoảng cách địa lý
- **"CloudFront đặt trước S3 để tăng tốc upload"** → sai, CloudFront có timeout 60s tới origin, không phải giải pháp khuyến nghị cho upload

### TD explanation

Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.

You might want to use Transfer Acceleration on a bucket for various reasons, including the following:
– You have customers that upload to a centralized bucket from all over the world.
– You transfer gigabytes to terabytes of data on a regular basis across continents.
– You are unable to utilize all of your available bandwidth over the Internet when uploading to Amazon S3.
You can enable Transfer Acceleration on a bucket in any of the following ways:
– Use the Amazon S3 console.
– Use the REST API PUT Bucket accelerate operation.
– Use the AWS CLI and AWS SDKs.
You can transfer data to and from the acceleration-enabled bucket by using one of the following s3-accelerate endpoint domain names:
- s3-accelerate.amazonaws.com – to access an acceleration-enabled bucket.
- s3-accelerate.dualstack.amazonaws.com – to access an acceleration-enabled bucket over IPv6. Amazon S3 dual-stack endpoints support requests to S3 buckets over IPv6 and IPv4.
You can point your Amazon S3 PUT object and GET object requests to the s3-accelerate endpoint domain name after you enable Transfer Acceleration. After Transfer Acceleration is enabled, it can take up to 20 minutes for you to realize the performance benefit. However, the accelerate endpoint will be available as soon as you enable Transfer Acceleration.
Therefore, the correct answer is: Enable S3 Transfer Acceleration on the central S3 bucket. Use the s3-accelerate endpoint to upload the images.
The option that says: Enable multipart upload on S3 and redeploy the application to support it. This allows the transmission of separate parts of the image in parallel is incorrect. Although multipart upload can improve the upload throughput to an S3 bucket, the European users are still limited on their Internet connection to the S3 bucket in the US region. S3 Transfer acceleration uses the AWS backbone network, which can optimize the transfer from far away regions.
The option that says: Set the centralized S3 bucket as the custom origin on an Amazon CloudFront distribution. This will use CloudFront’s global edge network to improve the upload speed is incorrect. CloudFront distribution is primarily designed for optimizing content delivery and content caching. Although CloudFront supports content uploads via POST, PUT, and other HTTP Methods, there is a limited connection timeout to the origin (60 seconds). If uploads take several minutes, the connection might get terminated. If you want to optimize performance when uploading large files to Amazon S3, it is recommended to use Amazon S3 Transfer Acceleration which can provide fast and secure transfers over long distances. Transfer Acceleration uses Amazon CloudFront’s globally distributed edge locations.
The option that says: Increase the upload capacity by creating an AWS Global Accelerator endpoint in front of the EC2 instances. Create an Auto Scaling Group that can scale automatically based on the users’ traffic is incorrect. Although AWS Global Accelerator can typically help increase network availability and performance, it won’t have an effect on this scenario because the images are directly uploaded to the S3 bucket. Increasing the number of EC2 instances does not necessarily improve the S3 upload speeds. Even if the application is configured to use the EC2 instance as a temporary storage for the images, the upload experience of the users will not improve because they are uploading from a different continent.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration-examples.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html
https://aws.amazon.com/premiumsupport/knowledge-center/s3-upload-large-files/

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q36"></a>

## Q36

A company is running thousands of virtualized Linux and Microsoft Windows servers on its on-premises data center. The virtual servers host a range of Java and PHP applications that use MySQL and Oracle databases. There are also several department services hosted on an external data center. The company uses SAN storage to provide iSCSI disks to its physical servers. The company wants to migrate its data center to the AWS Cloud, but the technical documentation of the systems is incomplete and outdated. The Solutions Architect was tasked to analyze the current environment and estimate the cost of migrating the resources to the cloud.
Which of the following should the Solutions Architect do to effectively plan the cloud migration? (Select THREE.)

- **A.** Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket.
- **B.** Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.
- **C.** Use the AWS Transform discovery tool to gather information about the running virtual machines and running applications inside the servers.
- **D.** Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.
- **E.** Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud.
- **F.** Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C, D (you answered correctly)

🔑 **Key words:** thousands of servers; outdated docs; estimate migration cost (Select THREE)

⚠️ **Watch:** Inspector/X-Ray aren't discovery tools

🧠 **Rule:** Transform discovery + assessment jobs + CART readiness.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: hàng nghìn VM (Linux + Windows), Java/PHP apps, MySQL/Oracle DB
            + vài service ở data center ngoài, SAN storage (iSCSI)
Technical docs: KHÔNG ĐẦY ĐỦ, LỖI THỜI

Nhiệm vụ: PHÂN TÍCH hiện trạng + ƯỚC TÍNH chi phí migration (chưa migrate thật)
```

Chọn **BA** hành động để **lập kế hoạch** migration. Đáp án đúng: **B (AWS Transform assessment jobs)** + **C (AWS Transform discovery tool)** + **D (AWS CART)**. Anh chọn đúng B, C, D.

#### Vì sao B, C, D đúng

- **C — AWS Transform discovery tool**: tự động khám phá server inventory (hỗ trợ VMware vCenter, Hyper-V, imported servers) — giải quyết đúng vấn đề gốc "docs không đầy đủ/lỗi thời": thay vì dựa vào tài liệu cũ, công cụ tự thu thập thông tin thực tế về VM và application đang chạy.
- **D — AWS CART**: khảo sát 16 câu hỏi, đánh giá mức độ sẵn sàng migration theo 6 khía cạnh (business, people, process, platform, operations, security) — giúp phát hiện **gap về kỹ năng/tổ chức**, một phần quan trọng của việc "lập kế hoạch" ngoài yếu tố kỹ thuật.
- **B — AWS Transform migration assessment jobs/workspaces**: dựa trên dữ liệu discovery, đưa ra **ước tính chi phí**, **right-sizing recommendation**, so sánh nhiều scenario, tạo report — đúng chính xác yêu cầu "estimate the cost of migrating" trong đề.

Ba công cụ này hợp thành một luồng: **discovery (C)** → **assessment/cost (B)** → **readiness (D)**, đều thuộc giai đoạn **phân tích & lập kế hoạch**, không phải thực thi migration.

#### Vì sao từng đáp án sai bị loại

- **E sai** vì **AWS Transform MGN** là service dùng cho **thực hiện migration thật** (lift-and-shift VM sang AWS), không phải công cụ lập kế hoạch. Đề yêu cầu rõ: phân tích hiện trạng và ước tính chi phí **trước khi** migrate thật.
- **F sai** vì **AWS X-Ray** dùng để debug ứng dụng production/microservices đang chạy (trace request, tìm lỗi) — không giúp gì cho việc **lập kế hoạch di chuyển hạ tầng** on-premises.
- **A sai** vì **Amazon Inspector** là dịch vụ đánh giá bảo mật tự động cho resource **đang chạy trên AWS** — không áp dụng được để quét/đánh giá application đang chạy **on-premises**.

#### So sánh nhanh

| Đáp án | Vai trò | Thuộc giai đoạn |
|---|---|---|
| **C (đúng)** | Khám phá server/app inventory on-prem | Discovery |
| **D (đúng)** | Đánh giá sẵn sàng tổ chức (CART) | Readiness assessment |
| **B (đúng)** | Ước tính chi phí, right-sizing | Cost/migration assessment |
| E | Thực hiện migration (MGN) | Execution, không phải planning |
| F | Debug app đang chạy (X-Ray) | Không liên quan planning |
| A | Security assessment cho resource trên AWS (Inspector) | Không áp dụng cho on-premises |

#### Lưu ý thực tế

- AWS Transform là một hệ công cụ rộng: discovery, assessment, và cả modernize/migrate (ví dụ MGN cho lift-and-shift, hỗ trợ VMware→EC2, .NET modernization...) — cần phân biệt rõ công cụ nào thuộc **giai đoạn nào** (discovery/planning vs execution) khi đề hỏi cụ thể một giai đoạn.
- CART là một khảo sát độc lập (survey-based), không cần tích hợp kỹ thuật vào hạ tầng — phù hợp đánh giá khía cạnh "con người & tổ chức" mà các tool kỹ thuật như discovery/assessment không đo được.

#### Quy tắc nhớ cho thi

- **"Docs không đầy đủ, cần biết hiện trạng VM/app"** → **AWS Transform discovery tool**
- **"Ước tính chi phí + right-sizing trước khi migrate"** → **AWS Transform assessment jobs**
- **"Đánh giá mức độ sẵn sàng tổ chức/kỹ năng"** → **AWS CART**
- **"MGN / X-Ray / Inspector"** trong câu hỏi về *lập kế hoạch* → hầu như luôn là bẫy (MGN = execution, X-Ray = debug app chạy, Inspector = security cho resource trên AWS)

### TD explanation

The scenario requires tools of services that will help to effectively plan the cloud migration, so the answers should be focused on planning.
AWS Transform is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.
With AWS Transform, you can:
– Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS
– Migrate VMware workloads to Amazon EC2
– Modernize .NET applications to Linux-ready cross-platform .NET
– Assess workloads for migration readiness

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.
The AWS Transform discovery tool assists you in automatically discovering the server inventory within your organization in preparation for migration. This tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To utilize the discovery tool, you need to configure one or more discovery sources, allow the tool to run, and then review the results displayed in the Discovered Inventory pane.
Once you configure a discovery source, the tool will begin collecting information. The time required for the discovery tool to completely analyze your network depends on the size of your environment. For businesses utilizing a directional migration approach, you can leverage the Migration Portfolio Assessment (MPA) files generated by the tool after the server collection is completed.
The AWS Cloud Adoption Readiness Tool (CART) helps organizations of all sizes develop efficient and effective plans for cloud adoption and enterprise cloud migrations. This 16-question online survey and assessment report detail your cloud migration readiness across six perspectives, including business, people, process, platform, operations, and security. Once you complete a CART survey, you can provide your contact details to download a customized cloud migration assessment that charts your readiness and what you can do to improve it. This tool is designed to help organizations assess their progress with cloud adoption and identify gaps in organizational skills and processes.
AWS Transform assessments evaluate the cost, feasibility, and business value of migrating on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinement through chat.
You can apply migration assessments for several objectives:
– Get cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx
– Receive automated right-sizing recommendations
– Assess business value and sustainability impact
– Compare multiple migration scenarios side by side
– Refine assessments interactively through chat
– Generate executive presentations and detailed reports
Therefore, the correct answers are:
– Use the AWS Transform Discovery Tool to gather information about the running virtual machines and running applications inside the servers.
– Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.
– Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.
The option that says: Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud is incorrect because MGN is primarily used for the actual migration of your on-premises virtual machines to the AWS Cloud and not for planning. Take note that in the scenario, the Solutions Architect was tasked to analyze the existing on-premises architecture first before doing the actual migration to AWS.
The option that says: Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration is incorrect because AWS X-Ray is typically used to debug production and distributed applications, such as those built using a microservices architecture. This is not helpful for planning the migration.
The option that says: Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket is incorrect because Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. This is not helpful for assessing the applications on the on-premises data center.

References:
https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html
https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html
https://docs.aws.amazon.com/transform/latest/launchguide/resources.html
https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html

Check out this AWS Migration Strategies Cheat Sheet:
https://tutorialsdojo.com/aws-migration-strategies-the-7-rs/

</details>

<a id="q60"></a>

## Q60

An organization is migrating its on-premises web application to AWS. The application comprises a Java-based backend and a NoSQL MongoDB database. Due to constraints, the application cannot be modified during the migration process, and the migrated solution must maintain an architecture similar to the on-premises setup. Additionally, the application requires high availability for both the backend and the database to ensure continuous operation.
Which solution will meet these requirements while adhering to the constraints?

- **A.** Containerize the Java application using AWS App2Container and deploy it on Amazon Elastic Kubernetes Service (EKS). Use Amazon DynamoDB for the database layer to achieve high availability.
- **B.** Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Use Amazon DocumentDB (with MongoDB compatibility) in a single Availability Zone deployment to host the MongoDB database.
- **C.** Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Migrate the MongoDB database to Amazon DocumentDB (with MongoDB compatibility) across multiple Availability Zones.
- **D.** Use AWS Elastic Beanstalk to deploy the Java application and migrate the MongoDB database to Amazon Aurora with multiple read replicas across different Availability Zones.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** Java + MongoDB; no code change; HA

⚠️ **Watch:** DynamoDB/Aurora require code changes

🧠 **Rule:** Multi-AZ EC2 ASG + DocumentDB across AZs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: Java backend + MongoDB (NoSQL)

Ràng buộc:
- KHÔNG được sửa code ứng dụng
- Kiến trúc sau migrate phải TƯƠNG TỰ on-premises
- Backend VÀ database đều cần HIGH AVAILABILITY
```

Đáp án đúng: **C** — Java app trên **EC2 trong Auto Scaling group, nhiều AZ** + migrate MongoDB sang **Amazon DocumentDB (MongoDB compatibility) nhiều AZ**. Anh chọn đúng C.

#### Vì sao C đúng

- **Amazon DocumentDB (with MongoDB compatibility)**: tương thích JSON-like storage format, query language, và driver của MongoDB → **không cần sửa code ứng dụng**, đúng ràng buộc cứng của đề.
- DocumentDB **mặc định deploy dữ liệu trên 3 Availability Zones** — nếu primary instance fail, tự động promote một replica lên primary, không cần can thiệp thủ công → đáp ứng HA cho database.
- **EC2 trong Auto Scaling group trải nhiều AZ**: giữ được mức độ tùy biến cấu hình gần giống on-premises (so với việc đổi sang container/managed compute), đồng thời Auto Scaling tự thay instance unhealthy, scale theo traffic → đáp ứng HA + khả năng chịu lỗi cho backend.
- Việc deploy resource trên **nhiều AZ** (ít nhất 2) cho cả backend và database là yếu tố quyết định khiến C đúng còn B sai.

#### Vì sao từng đáp án sai bị loại

- **B sai** vì tuy cũng dùng EC2 ASG + DocumentDB đúng loại database, nhưng DocumentDB chỉ deploy ở **single Availability Zone** — **không đáp ứng yêu cầu HA cho database layer**. Đây là điểm khác biệt duy nhất so với C, và chính là điểm làm B sai.
- **A sai** vì đổi database từ MongoDB sang **Amazon DynamoDB** — khác hẳn loại database (DynamoDB có API/model khác MongoDB), buộc phải **sửa code đáng kể** ở tầng data access — vi phạm trực tiếp ràng buộc "không được sửa ứng dụng".
- **D sai** vì đổi MongoDB sang **Amazon Aurora** — Aurora là **relational database**, khác hoàn toàn kiến trúc NoSQL của MongoDB, vừa vi phạm ràng buộc "kiến trúc tương tự on-premises", vừa đòi hỏi sửa code tầng data access.

#### So sánh nhanh

| Đáp án | Backend | Database | AZ cho DB | Cần sửa code? |
|---|---|---|---|---|
| **C (đúng)** | EC2 ASG multi-AZ | DocumentDB | Nhiều AZ | Không |
| B | EC2 ASG multi-AZ | DocumentDB | **Single AZ** | Không, nhưng DB thiếu HA |
| A | EKS (App2Container) | DynamoDB | — | Có — đổi hẳn model DB |
| D | Elastic Beanstalk | Aurora (relational) | Nhiều AZ (read replica) | Có — đổi hẳn loại DB |

#### Lưu ý thực tế

- Đây là bộ ba yêu cầu kinh điển cho câu hỏi dạng "migrate không sửa code + giữ kiến trúc tương tự + cần HA": chọn đúng **managed service tương thích API/protocol gốc** (ở đây là DocumentDB cho MongoDB) rồi mới xét tới việc nó có **deploy multi-AZ** hay không — thiếu một trong hai điều kiện là sai ngay.
- App2Container (trong A) tự nó không sai về nguyên tắc containerize Java app, nhưng điểm chốt làm A sai luôn là việc đổi sang DynamoDB — một lựa chọn tưởng hợp lý (DynamoDB cũng NoSQL, HA sẵn) nhưng không tương thích API với MongoDB.

#### Quy tắc nhớ cho thi

- **"Migrate MongoDB, không sửa code"** → **Amazon DocumentDB (with MongoDB compatibility)**, không phải DynamoDB hay Aurora
- **"HA cho database"** → kiểm tra kỹ xem đáp án có ghi rõ **multi-AZ** hay chỉ "single AZ" — đây thường là điểm phân biệt giữa 2 đáp án gần giống nhau
- **"Giữ kiến trúc tương tự on-premises + không sửa code"** → ưu tiên **EC2 (tự quản lý)** hơn là đổi sang container/serverless hoặc đổi loại database

### TD explanation

Amazon DocumentDB (with MongoDB Compatibility) is a managed NoSQL database service designed to seamlessly support MongoDB workloads. It allows the organization to migrate its existing MongoDB database without requiring application changes, as it is compatible with MongoDB’s JSON-like storage format, query language, and drivers. This service ensures high availability by deploying data across three Availability Zones by default, providing fault tolerance and durability. If a primary instance fails, Amazon DocumentDB automatically promotes a replica to primary, ensuring continuous operations without manual intervention. This makes it an ideal choice for the organization’s needs, as it adheres to the requirement of high availability for the database layer and maintains architectural compatibility.

Amazon EC2 instances: EC2 (Elastic Compute Cloud) provides scalable computing capacity in the AWS cloud. By deploying the Java application on EC2 instances, you retain the flexibility to run custom configurations and setups that closely match your on-premises environment.
An Auto Scaling group manages the fleet of Amazon EC2 instances hosting the Java-based backend application. It ensures that the correct number of instances are always running to handle varying levels of application traffic. By dynamically scaling up during peak traffic and scaling down during lower demand, Auto Scaling optimizes costs while maintaining performance. Moreover, it replaces unhealthy instances automatically, ensuring that the backend application remains operational even in the event of instance failures. This makes Auto Scaling crucial for providing the required scalability and fault tolerance for the application.

Multiple Availability Zones are leveraged to ensure high availability and fault tolerance for both the backend and database. Resources are deployed across at least two physically separate zones within the AWS Region. This setup ensures that the application and database remain operational even if one Availability Zone experiences an outage. The distribution of resources across zones also improves resiliency and fault tolerance while enhancing overall application availability. By deploying in multiple zones, the organization can maintain a highly available architecture similar to the on-premises setup, with the added benefit of AWS’s robust infrastructure.
Hence, the correct answer is: Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Migrate the MongoDB database to Amazon DocumentDB (with MongoDB compatibility) across multiple Availability Zones.
The option that says: Containerize the Java application using AWS App2Container and deploy it on Amazon Elastic Kubernetes Service (EKS). Use Amazon DynamoDB for the database layer to achieve high availability is incorrect because it primarily involves significant changes to the application’s architecture, particularly replacing MongoDB with DynamoDB, which is a different type of database.
The option that says: Use AWS Elastic Beanstalk to deploy the Java application and migrate the MongoDB database to Amazon Aurora with multiple read replicas across different Availability Zones is incorrect because it changes the database from MongoDB to Amazon Aurora, which is a relational database service. This would not maintain the same architecture as the on-premises setup.
The option that says: Deploy the Java application on Amazon EC2 instances within an Auto Scaling group spanning multiple Availability Zones. Use Amazon DocumentDB (with MongoDB compatibility) in a single Availability Zone deployment to host the MongoDB database is incorrect because while it uses Amazon DocumentDB, it only deploys it in a single Availability Zone, which does not meet the high availability requirement for the database.

References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html
https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html

Check out this Amazon DocumentDB Cheat Sheet:
https://tutorialsdojo.com/amazon-documentdb/

</details>
