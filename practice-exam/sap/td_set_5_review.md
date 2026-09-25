# TD Set 5 — Wrong Answer Review (44 questions)

Source: `TD_SAP_Timed_Set5_Full.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td_set_5_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q1](#q1) | ✅ 09-25 | ☐ | ☐ |
| A | [Q8](#q8) | ✅ 09-25 | ☐ | ☐ |
| A | [Q10](#q10) | ✅ 09-25 | ☐ | ☐ |
| A | [Q14](#q14) | ✅ 09-25 | ☐ | ☐ |
| A | [Q35](#q35) | ✅ 09-25 | ☐ | ☐ |
| A | [Q28](#q28) | ✅ 09-25 | ☐ | ☐ |
| A | [Q38](#q38) | ✅ 09-25 | ☐ | ☐ |
| A | [Q51](#q51) | ✅ 09-25 | ☐ | ☐ |
| A | [Q68](#q68) | ✅ 09-25 | ☐ | ☐ |
| A | [Q72](#q72) | ✅ 09-25 | ☐ | ☐ |
| A | [Q73](#q73) | ✅ 09-25 | ☐ | ☐ |
| A | [Q24](#q24) | ✅ 09-25 | ☐ | ☐ |
| B | [Q16](#q16) | ✅ 09-25 | ☐ | ☐ |
| B | [Q29](#q29) | ✅ 09-25 | ☐ | ☐ |
| B | [Q19](#q19) | ✅ 09-25 | ☐ | ☐ |
| B | [Q31](#q31) | ✅ 09-25 | ☐ | ☐ |
| B | [Q67](#q67) | ✅ 09-25 | ☐ | ☐ |
| B | [Q18](#q18) | ❌ 09-25 | ☐ | ☐ |
| B | [Q54](#q54) | ✅ 09-25 | ☐ | ☐ |
| B | [Q36](#q36) | ✅ 09-25 | ☐ | ☐ |
| B | [Q62](#q62) | ✅ 09-25 | ☐ | ☐ |
| C | [Q9](#q9) | ☐ | ☐ | ☐ |
| C | [Q61](#q61) | ☐ | ☐ | ☐ |
| C | [Q42](#q42) | ☐ | ☐ | ☐ |
| C | [Q20](#q20) | ☐ | ☐ | ☐ |
| C | [Q57](#q57) | ☐ | ☐ | ☐ |
| D | [Q4](#q4) | ☐ | ☐ | ☐ |
| D | [Q32](#q32) | ☐ | ☐ | ☐ |
| D | [Q33](#q33) | ☐ | ☐ | ☐ |
| D | [Q63](#q63) | ☐ | ☐ | ☐ |
| D | [Q49](#q49) | ☐ | ☐ | ☐ |
| D | [Q55](#q55) | ☐ | ☐ | ☐ |
| D | [Q74](#q74) | ☐ | ☐ | ☐ |
| E | [Q5](#q5) | ☐ | ☐ | ☐ |
| E | [Q58](#q58) | ☐ | ☐ | ☐ |
| E | [Q30](#q30) | ☐ | ☐ | ☐ |
| E | [Q13](#q13) | ☐ | ☐ | ☐ |
| F | [Q12](#q12) | ☐ | ☐ | ☐ |
| F | [Q22](#q22) | ☐ | ☐ | ☐ |
| F | [Q23](#q23) | ☐ | ☐ | ☐ |
| F | [Q69](#q69) | ☐ | ☐ | ☐ |
| F | [Q21](#q21) | ☐ | ☐ | ☐ |
| F | [Q15](#q15) | ☐ | ☐ | ☐ |
| F | [Q48](#q48) | ☐ | ☐ | ☐ |

---

# Group A — DIY over managed service (12)

<a id="q1"></a>

## Q1

A company offers financial services and big data analytics for its partners. It receives about 4,000 credit card transaction records every 15 minutes from its partners which are stored on an encrypted Amazon S3 bucket. This data contains sensitive information such as the primary account number (PAN). The company needs to mask the PAN immediately before sending the data to another S3 bucket for additional processing. The next step is to remove and merge specific fields, and then transform each transaction record in JSON format. More fields are expected to be added in the future so the solution must be easily expandable to accommodate the transformation requirements.

Which of the following options is the recommended solution to meet the company requirements?

- **A.** Use AWS Data Exchange to acquire the data and store it in an Amazon S3 bucket. Upon file delivery, perform an Amazon Athena query to start an Amazon EMR ETL job to transform each record according to requirements. Set the output to JSON format, and send it to another S3 bucket for additional processing. Scale down the EMR cluster afterward.
- **B.** Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. Configure AWS Fargate to automatically scale depending on the number of messages on the SQS queue. Have the Fargate application transform each record according to requirements and send the JSON formatted output to another S3 bucket for additional processing.
- **C.** Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. For each message received on the SQS queue, run another Lambda function to transform the data according to requirements and store the results in a temporary S3 bucket. Trigger a final Lambda function for each delivery on the temporary S3 bucket to convert the data into JSON format. Send the final output to another S3 bucket.
- **D.** Configure an AWS Glue crawler and add a custom classifier based on the data format to build a matching table definition. Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it trigger an AWS Glue ETL job to transform each record according to requirements. Set the output to JSON format. After completion, configure the ETL job to send the results to another S3 bucket for additional processing.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** mask + remove/merge fields + JSON = ETL; every 15 min batch; 'easily expandable'

🪤 **Your trap:** Lambda→SQS→Fargate = self-built ETL; every new field = code change + redeploy

🧠 **Rule:** ETL + expandable/least overhead → Glue crawler + classifier + Glue ETL job. Data Exchange never transforms.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Partner data (4,000 records / 15 phút)
        │
        ▼
S3 bucket (encrypted) ── chứa PAN (sensitive)
        │
        ▼
Yêu cầu:
  1. Mask PAN NGAY
  2. Remove/merge fields
  3. Transform → JSON
  4. Gửi sang S3 bucket khác để xử lý tiếp
  5. Sẽ có thêm field mới trong tương lai
     → solution phải DỄ MỞ RỘNG
```

Đây là một bài toán **ETL (Extract – Transform – Load)** kinh điển, không phải bài toán về event processing hay data transfer. Đáp án đúng: **D (Glue crawler + classifier + Glue ETL job)**. Anh chọn **B (Lambda → SQS → Fargate)** — đúng kiểu "tự dựng ETL bằng compute service" mà đề không cần.

#### Vì sao D đúng

AWS Glue là dịch vụ ETL **serverless, managed**, có sẵn:

```
S3 (raw) → Glue Crawler + Custom Classifier → Glue Data Catalog (table + schema)
                                                      │
                                                      ▼
                                    Glue ETL Job (transform: mask PAN, remove/merge fields)
                                                      │
                                                      ▼
                                          Output JSON → S3 (processed)
```

- **Crawler + classifier**: tự động nhận diện format dữ liệu, sinh schema, cập nhật Data Catalog — không cần code quản lý schema thủ công.
- **Glue ETL job**: engine tự sinh code Python/Scala để transform (mask, remove, merge field). Khi có field mới, chỉ cần **sửa job script/mapping**, không phải viết lại toàn bộ pipeline.
- Lambda chỉ đóng vai trò **trigger** khi có file mới, gọi Glue ETL job chạy — không phải nơi làm transform logic.

#### Vì sao B (Anh chọn) sai

```
Lambda (trigger) → SQS → Fargate (tự scale) → transform → S3
```

Về mặt kỹ thuật **chạy được**, nhưng:
- Anh phải **tự viết và maintain code transform** trong ứng dụng Fargate. Mỗi lần thêm field mới → sửa code ứng dụng, build lại image, deploy lại — không phải "dễ mở rộng" như đề yêu cầu.
- Duy trì một Fargate service (dù serverless-ish) vẫn tốn kém hơn một Glue job chỉ chạy theo lịch/khi có trigger — **không cost-effective** so với Glue.
- Đây chính là pattern DIY ETL bằng compute service thay vì dùng managed ETL service có sẵn.

#### Vì sao các lựa chọn khác sai

| Đáp án | Vấn đề |
|---|---|
| A. Data Exchange + Athena + EMR | Data Exchange chỉ để **acquire/transfer** dữ liệu, không transform. Dùng Athena để "kích hoạt" EMR ETL cho job định kỳ 15 phút là **không cost-effective** — overkill so với Glue. |
| B. Lambda→SQS→Fargate | Tự viết code transform, mỗi field mới phải sửa code + deploy lại — không dễ mở rộng. |
| C. Lambda→SQS→Lambda→Lambda (chuỗi 3 Lambda) | Có thể chạy được nhưng "cumbersome to expand": thêm field = sửa code Lambda, nhiều điểm lỗi hơn, không có data catalog/schema quản lý tập trung. |
| **D. Glue crawler + classifier + Glue ETL job** | Managed, schema tự động, transform logic tách biệt dễ mở rộng — đúng đáp án. |

#### Quy tắc nhớ cho thi

- **"transform/mask/remove/merge fields" + "easily expandable"** → nghĩ ngay đến **AWS Glue ETL**, không phải Lambda/Fargate tự viết code.
- **AWS Data Exchange** chỉ dùng để **mua/nhận dữ liệu từ bên thứ ba**, không bao giờ transform dữ liệu.
- Thấy chuỗi **Lambda → SQS → Lambda/Fargate làm transform logic** trong đề về ETL có yêu cầu mở rộng → đây là bẫy "tự dựng lại Glue bằng tay", gần như luôn sai.
- **Glue crawler** = tự động phát hiện schema; **classifier** = nhận diện định dạng dữ liệu (bao gồm cả việc xác định output là JSON).

### TD explanation

AWS Glue is a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams. AWS Glue consists of a central metadata repository known as the AWS Glue Data Catalog, an ETL engine that automatically generates Python or Scala code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries. AWS Glue is serverless, so there’s no infrastructure to set up or manage.

You can use a crawler to populate the AWS Glue Data Catalog with tables. This is the primary method used by most AWS Glue users. A crawler can crawl multiple data stores in a single run. Upon completion, the crawler creates or updates one or more tables in your Data Catalog. A classifier reads the data in a data store. If it recognizes the format of the data, it generates a schema. The classifier also returns a “certainty” number to indicate how certain the format recognition was.

Therefore, the correct answer is: Configure an AWS Glue crawler and add a custom classifier based on the data format to build a matching table definition. Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it trigger an AWS Glue ETL job to transform each record according to requirements. Set the output to JSON format. After completion, configure the ETL job to send the results to another S3 bucket for additional processing. AWS Glue is designed for these ELT jobs and the crawler helps build a data catalog. The output of a classifier includes a string that indicates the file’s classification such as JSON format.

The option that says: Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. For each message received on the SQS queue, run another Lambda function to transform the data according to requirements and store the results in a temporary S3 bucket. Trigger a final Lambda function for each delivery on the temporary S3 bucket to convert the data into JSON format. Send the final output to another S3 bucket is incorrect. It is possible to use a series of functions for the transform job, however, this can be cumbersome to expand in the future as you will need to update the Lambda functions code for every field that needs to be transformed.

The option that says: Trigger an AWS Lambda function for every file delivery to the S3 bucket. Have it extract each record and send the data to an Amazon SQS queue. Configure and AWS Fargate service to automatically scale depending on the number of messages on the SQS queue. Have the Fargate application transform each record according to requirements and send the JSON formatted output to another S3 bucket for additional processing is incorrect. This may be possible, however, you will need to update the application and deploy the Fargate service for any transformation requirements in the future. Maintaining a Fargate cluster is not cost-effective compared to other solutions.

The option that says: Use AWS Data Exchange to acquire the data and store it in an Amazon S3 bucket. Upon file delivery, perform an Amazon Athena query to start an Amazon EMR ETL job to transform each record according to requirements. Set the output to JSON format, and send it to another S3 bucket for additional processing. Scale down the EMR cluster afterward is incorrect because AWS Data Exchange, which is primarily used for data transfer, does not provide any functionality to process or transform the data before it is stored in the S3 bucket. Moreover, it is not cost-effective to use Amazon Athena queries and an Amazon EMR cluster for a periodic ETL job. An AWS Glue ETL job is a more cost-effective solution.

 

References:

https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html

https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html

https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html

 

Check out this AWS Glue Cheat Sheet:

https://tutorialsdojo.com/aws-glue/

</details>

<a id="q8"></a>

## Q8

A company uses an AWS Step Functions workflow for its transaction processing system, which relies on several interconnected Lambda functions. The company wants to understand the memory consumption patterns of these Lambda functions to optimize cost.

They require a weekly CSV report detailing the average memory utilization of each function, recommended memory configurations based on historical performance, and potential cost savings between the current and recommended settings.

How can the company achieve this reporting requirement in the least amount of development overhead?

- **A.** Enroll in the AWS Business Support plan. Collaborate with AWS support to analyze the Lambda function's resource utilization. Manually document insights and optimization suggestions in a CSV file stored in an Amazon S3 bucket.
- **B.** Analyze the Lambda function’s resource utilization using AWS Compute Optimizer. Set up an EventBridge rule to trigger a Lambda function weekly. Use the ExportLambdaFunctionRecommendations API within the function to export recommendations as CSV files in an Amazon S3 bucket.
- **C.** Extract the Billed Duration and Max Memory Use metrics from the Lambda function logs in CloudWatch Logs using a weekly scheduled job. Use this data with Amazon SageMaker Canvas to predict future memory usage patterns and estimate potential savings. Download the forecast as a CSV file.
- **D.** Enable CloudWatch Lambda Insights for the Lambda functions. Configure an EventBridge rule to trigger a Lambda function weekly, which compiles the findings into a CSV file and stores them in an Amazon S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** weekly CSV; avg memory; RECOMMENDED config; cost savings; least dev overhead

🪤 **Your trap:** Lambda Insights = monitoring only, no recommendations/savings

🧠 **Rule:** Right-sizing recommendations + savings → Compute Optimizer (ExportLambdaFunctionRecommendations → S3).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Step Functions workflow ──► nhiều Lambda functions (transaction processing)

Yêu cầu báo cáo CSV hàng tuần gồm:
  1. Avg memory utilization mỗi function
  2. RECOMMENDED memory config (dựa trên lịch sử)
  3. Potential cost savings (current vs recommended)

Ràng buộc: LEAST development overhead
```

Đáp án đúng: **B (AWS Compute Optimizer + ExportLambdaFunctionRecommendations API)**. Anh chọn **D (CloudWatch Lambda Insights)** — bị vướng đúng cái bẫy "monitoring tool nhưng không sinh ra recommendation".

#### Vì sao B đúng

**AWS Compute Optimizer** dùng machine learning để phân tích historical utilization và sinh ra **khuyến nghị resource tối ưu** (bao gồm cả Lambda memory size) — đây chính xác là 3 thứ đề bài cần: avg utilization, recommended config, cost savings, tất cả **có sẵn**, không cần tự tính.

```
Lambda functions ──(chạy, ghi metric)──► Compute Optimizer (ML phân tích)
                                                │
                                    ExportLambdaFunctionRecommendations API
                                                │
        EventBridge rule (weekly) ──► Lambda function gọi API này
                                                │
                                                ▼
                                    CSV file → S3 bucket
```

Toàn bộ phần "phân tích và tính recommendation" đã được Compute Optimizer làm sẵn — team chỉ cần một Lambda nhỏ gọi API export theo lịch EventBridge. Đây là **least development overhead** thật sự.

#### Vì sao D (Anh chọn) sai

**CloudWatch Lambda Insights** chỉ là công cụ **monitoring/troubleshooting** — cung cấp visibility sâu hơn vào execution environment (CPU, memory, cold start...) để debug, nhưng **không sinh ra khuyến nghị memory tối ưu hay ước tính cost savings**. Nếu chọn D, team vẫn phải tự viết logic phân tích dữ liệu Insights để suy ra "recommended memory" — tức là **tăng development overhead**, ngược lại với yêu cầu đề bài.

#### Vì sao các lựa chọn khác sai

| Đáp án | Vấn đề |
|---|---|
| A. AWS Business Support thủ công | Phải liên hệ support hàng tuần, ghi chép thủ công vào CSV — hoàn toàn không phải mục đích của Business Support plan (dùng cho technical guidance/escalation, không phải weekly reporting). |
| C. CloudWatch Logs metrics + SageMaker Canvas | Phải tự parse log, tích hợp thêm SageMaker Canvas để "dự đoán" — nhiều bước hơn, không trực tiếp cho ra memory recommendation. |
| **B. Compute Optimizer + Export API** | Managed, có sẵn recommendation + savings estimate, chỉ cần lịch trigger export → đúng đáp án. |
| D. Lambda Insights | Chỉ monitoring, không có recommendation/savings. |

#### Lưu ý thực tế

- Compute Optimizer không chỉ áp dụng cho Lambda — còn cho EC2 instance type, EBS volume, ECS on Fargate task size. Khi đề nói "recommend optimal configuration + cost savings" cho bất kỳ resource nào trong nhóm này, Compute Optimizer gần như luôn là câu trả lời.
- `ExportLambdaFunctionRecommendations` xuất trực tiếp ra S3 dưới dạng file — không cần custom logic để format CSV.

#### Quy tắc nhớ cho thi

- **"recommended configuration" + "cost savings" + "least overhead"** → **AWS Compute Optimizer**, không phải CloudWatch Insights/Logs.
- **CloudWatch Lambda Insights / Container Insights** = chỉ để **quan sát, debug**, không đưa ra khuyến nghị tối ưu hóa.
- Thấy "Export...Recommendations API" trong đáp án đúng của các câu về Compute Optimizer → đây là API pattern chuẩn để tự động hóa export báo cáo định kỳ.

### TD explanation

AWS Compute Optimizer helps you identify the optimal AWS resource configurations, such as Amazon Elastic Compute Cloud (EC2) instance types, Amazon Elastic Block Store (EBS) volume configurations, task sizes of Amazon Elastic Container Service (ECS) services on AWS Fargate, and AWS Lambda function memory sizes, using machine learning to analyze historical utilization metrics. AWS Compute Optimizer provides a set of APIs and a console experience to help you reduce costs and increase workload performance by recommending the optimal AWS resources for your AWS workloads.

In the scenario, utilizing the ExportLambdaFunctionRecommendations API within a scheduled function ensures an automated approach to data extraction. Automating the export process through a scheduled function eliminates the need for manual intervention and ensures that the report is generated consistently on a weekly basis, as required

Hence, the correct answer in this scenario is: Analyze the Lambda function’s resource utilization using AWS Compute Optimizer. Set up an EventBridge rule to trigger a Lambda function weekly. Use the ExportLambdaFunctionRecommendations API within the function to export recommendations as CSV files in an Amazon S3 bucket.

The option that says: Enroll in the AWS Business Support plan. Collaborate with AWS support to analyze the Lambda function’s resource utilization. Manually document insights and optimization suggestions in a CSV file stored in an Amazon S3 bucket is incorrect. Engaging AWS support every week would be cumbersome. AWS Business Support is generally meant to provide technical assistance, architectural guidance, and escalated issue resolution rather than weekly performance analysis and manual report generation. Additionally, AWS support doesn’t have access to your function logs, so you would need to share any relevant logs or data, which adds extra steps to the process.

The option that says: Enable CloudWatch Lambda Insights for the Lambda functions. Configure an EventBridge rule to trigger a Lambda function weekly, which compiles the findings into a CSV file and stores them in an Amazon S3 bucket is incorrect. CloudWatch Lambda Insights is primarily designed for monitoring and troubleshooting Lambda functions. It provides deeper visibility into the execution environment of your Lambda functions, allowing you to diagnose and resolve issues more efficiently. However, it’s not capable of generating recommendations for memory configurations or potential cost savings between current and recommended settings.

The option that says: Extract the Billed Duration and Max Memory Use metrics from the Lambda function logs in CloudWatch Logs using a weekly scheduled job. Use this data with Amazon SageMaker Canvas to predict future memory usage patterns and estimate potential savings. Download the forecast as a CSV file is incorrect. This option typically requires parsing and managing logs and integrating with Amazon SageMaker Canvas adds more overhead compared to simply using AWS Compute Optimizer. Furthermore, it doesn’t directly provide memory configuration recommendations.

 

References:

https://aws.amazon.com/compute-optimizer/

https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportLambdaFunctionRecommendations.html

 

Check out this AWS Compute Optimizer Cheat Sheet:

https://tutorialsdojo.com/aws-compute-optimizer/

</details>

<a id="q10"></a>

## Q10

A company hosts an SFTP server in an Amazon EC2 instance with an Elastic IP address inside a VPC. The SFTP server acts as a central repository for uploading inventory data of its partners. The partner companies connect to the server via the Elastic IP address and use SSH for authentication. The security group of the EC2 instance is restricted to allow only the IP addresses of the partner companies. The solutions architect has been tasked to improve the current solution, increase the availability of the server, and minimize the management complexity of the infrastructure. The company wants minimal disruption for its partners and it should retain the current process on how the partners connect to the SFTP server.

Which of the following implementations will meet the company requirements?

- **A.** Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family SFTP-enabled server with a publicly accessible endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket.
- **B.** Create an Auto Scaling group of Amazon EC2 instances that run the SFTP server and place it behind a Network Load Balancer. Create a multi-attach Amazon EBS volume to be mounted on all the EC2 instances in the cluster. Sync all the SFTP server files to the multi-attach volume. Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Auto Scaling group to allow only the IP addresses of the partner companies.
- **C.** Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family server inside the VPC with an internet-facing endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Create a security group for the endpoint to allow only the IP addresses of the partner companies. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket.
- **D.** Create an AWS Fargate task definition to run the SFTP server. Create a new Amazon Elastic File System (EFS) volume and add it as a mount point in the task definition. Sync all the SFTP server files to the EFS volume. Create a Fargate service using the task definition and place it behind a Network Load Balancer (NLB). Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Fargate service to allow only the IP addresses of the partner companies.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** SFTP; keep Elastic IP; partner IP allowlist via SG; HA; minimize management

🪤 **Your trap:** Public Transfer Family endpoint can't attach EIP/SG

🧠 **Rule:** Transfer Family VPC endpoint, internet-facing → attach EIP + security group; S3 as storage.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:
  EC2 instance + Elastic IP  ──SFTP/SSH──► Partner companies
                                    (SG chỉ allow IP của partner)

Yêu cầu cải tiến:
  - Tăng availability
  - Giảm management complexity
  - Partner KHÔNG bị gián đoạn, vẫn kết nối theo cách cũ
    (cùng EIP, cùng cơ chế allowlist IP qua SG)
```

Đáp án đúng: **C (AWS Transfer Family, VPC-hosted, internet-facing endpoint)**. Anh chọn **A (Transfer Family với "publicly accessible endpoint")** — sai vì loại endpoint này **không gắn được Elastic IP và Security Group** như yêu cầu.

#### Điểm mấu chốt: 2 loại endpoint của AWS Transfer Family

```
1) Public endpoint (internet-facing, KHÔNG trong VPC)
   → AWS quản lý toàn bộ networking
   → KHÔNG gắn được Elastic IP
   → KHÔNG gắn được Security Group tùy chỉnh
   → không thể replicate "chỉ allow IP đối tác" như yêu cầu

2) VPC-hosted endpoint, internet-facing
   → Endpoint nằm TRONG VPC của anh
   → CÓ THỂ gắn Elastic IP (client bên ngoài VPC vẫn kết nối được)
   → CÓ THỂ gắn Security Group để allowlist IP đối tác
   → Đúng yêu cầu: giữ nguyên EIP, giữ nguyên cơ chế IP allowlist
```

**C đúng** vì dựng Transfer Family server **inside VPC, endpoint internet-facing**, sau đó disassociate EIP từ EC2 cũ và gắn sang endpoint mới, tạo Security Group riêng cho endpoint để allow IP đối tác — đúng 100% những gì đối tác đang quen dùng, mà server phía sau lại serverless/managed (S3 làm storage).

**A sai** vì "SFTP-enabled server with a **publicly accessible endpoint**" chính là loại (1) ở trên — không có chỗ để gắn Elastic IP hay Security Group, nên **không an toàn và không giữ được quy trình kết nối cũ**.

#### Vì sao các lựa chọn khác sai

| Đáp án | Vấn đề |
|---|---|
| B. ASG + NLB + multi-attach EBS | Multi-attach EBS phải tự quản lý (resize, đồng bộ), tăng độ phức tạp vận hành — ngược lại yêu cầu "minimize management complexity". |
| D. Fargate + EFS + NLB | Phải tự dựng Fargate cluster, EFS, cấu hình NLB — nhiều thành phần cần quản lý hơn hẳn so với dịch vụ managed sẵn có. |
| **C. Transfer Family VPC-hosted + EIP + SG** | Managed hoàn toàn, HA, giữ nguyên EIP và cơ chế allowlist → đúng đáp án. |
| A. Transfer Family public endpoint | Không gắn được EIP/SG → không an toàn, không giữ nguyên quy trình cũ. |

#### Lưu ý thực tế

- AWS Transfer Family hỗ trợ SFTP/FTPS/FTP, lưu trữ đích là **S3 hoặc EFS**. Ở đây S3 là lựa chọn tự nhiên vì server cũ vốn chỉ lưu file, không cần POSIX file system đầy đủ như EFS.
- Việc "associate Elastic IP" chỉ khả dụng khi server **nằm trong VPC** — đây là chi tiết dễ bị bỏ qua khi đọc lướt các đáp án gần giống nhau.

#### Quy tắc nhớ cho thi

- **"Transfer Family" + "cần Elastic IP / Security Group tùy chỉnh"** → phải chọn **VPC-hosted endpoint**, không phải "publicly accessible endpoint".
- **"giữ nguyên cách partner kết nối" (same EIP, same IP allowlist)** → tín hiệu cho thấy đáp án cần replicate đúng cơ chế mạng cũ, loại ngay các phương án đổi hẳn kiến trúc (ASG, Fargate tự quản lý).
- SFTP server tự quản lý trên EC2 → AWS Transfer Family gần như luôn là câu trả lời "giảm management overhead" trong các câu hỏi dạng này.

### TD explanation

AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services. AWS Transfer Family supports transferring data from or to the following AWS storage services – Amazon Simple Storage Service (Amazon S3) storage and Amazon Elastic File System (Amazon EFS) Network File System (NFS) file system.

AWS Transfer Family supports transferring data over the following protocols:

-Secure Shell (SSH) File Transfer Protocol (SFTP) (AWS Transfer for SFTP)

-File Transfer Protocol Secure (FTPS) (AWS Transfer for FTPS)

-File Transfer Protocol (FTP) (AWS Transfer for FTP)

You can host your server’s endpoint inside a virtual private cloud (VPC) to use for transferring data to and from an Amazon S3 bucket or Amazon EFS file system without going over the public internet. If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and a server. You can then use this server to transfer data over your client to and from your Amazon S3 bucket without going over the public internet.

Using Amazon VPC, you can launch AWS resources in a custom virtual network. You can use a VPC to control your network settings, such as the IP address range, subnets, route tables, and network gateways. In addition, if you choose to make your server’s endpoint internet-facing, you can associate Elastic IP addresses with your endpoint. Doing this lets clients outside of your VPC connect to your server. You can use VPC security groups to control access to authenticated users whose requests originate only from allowed addresses.

Therefore, the correct answer is: Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family server inside the VPC with an internet-facing endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Create a security group for the endpoint to allow only the IP addresses of the partner companies. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket. Creating an internet-facing endpoint inside a VPC allows you to associate an Elastic IP address and security groups to the AWS Transfer Family server. This is highly available, scalable, and has less operational overhead.

The option that says: Create an Auto Scaling group of Amazon EC2 instances that run the SFTP server and place it behind a Network Load Balancer. Create a multi-attach Amazon EBS volume to be mounted on all the EC2 instances in the cluster. Sync all the SFTP server files to the multi-attach volume. Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Auto Scaling group to allow only the IP addresses of the partner companies is incorrect. This may be possible as the Auto Scaling group increases the availability but it adds complexity to the overall infrastructure. You will have to manage the multi-attach EBS manually should you need to increase volume size in the future. 

The option that says: Create an AWS Fargate task definition to run the SFTP server. Create a new Amazon Elastic File System (EFS) volume and add it as a mount point in the task definition. Sync all the SFTP server files to the EFS volume. Create a Fargate service using the task definition and place it behind a Network Load Balancer (NLB). Disassociate the Elastic IP address from the EC2 instance and associate it to the NLB. Create a security group for the Fargate service to allow only the IP addresses of the partner companies is incorrect. Although this may be possible, this increases operation complexity since you will have to create a Fargate cluster, EFS volume, and the NLB configuration. 

The option that says: Create a new Amazon S3 bucket to host the files for the SFTP server. Create an AWS Transfer Family SFTP-enabled server with a publicly accessible endpoint. Disassociate the Elastic IP address from the EC2 instance and associate it to the new endpoint. Set the S3 bucket as the destination for the AWS Transfer Family server and copy all the SFTP server files to the S3 bucket is incorrect. It is not safe to have a public-facing AWS Transfer family endpoint without any restrictions. 

 

References:

https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html

https://aws.amazon.com/premiumsupport/knowledge-center/sftp-enable-elastic-ip-addresses/

https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html

 

Check out this AWS Transfer Family Cheat Sheet:

https://tutorialsdojo.com/aws-transfer-family/

</details>

<a id="q14"></a>

## Q14

A global streaming company uses a Java application on an Amazon EC2 instance to transcode videos for its platform. The application starts processing the videos to different resolutions every time they are uploaded to an Amazon S3 bucket. It takes approximately 40 minutes to transcode each video. The application keeps track of the transcoded videos and will only process each file once.

Upon reviewing Amazon CloudWatch metrics, a solutions architect noted that the EC2 instance is idle for 35% of the time on average. The solutions architect is required to make the workload highly available and scalable, and reduce management overhead.

What should the architect recommend for the MOST cost-effective solution?

- **A.** Build a container image out of the video transcoding application. Deploy and run the container image on an EC2 instance. Configure the container to continuously poll the S3 bucket for new videos and to transcode the files.
- **B.** Create an equivalent script of the application workflow and deploy it as an AWS Lambda function. Use an S3 event notification to start the processing when a new video is uploaded.
- **C.** Build a container image out of the video transcoding application. Deploy and run the container image on Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. Create an AWS Lambda function that calls the Fargate RunTask API operation when the S3 bucket receives the file upload event notification.
- **D.** Create an Amazon Simple Queue Service (Amazon SQS) queue and configure Amazon S3 to send event notifications to the SQS queue. Set up an EC2 Auto Scaling group with a minimum size of one instance. Modify the video transcoding application to continuously poll the SQS queue, and start transcoding the files in S3 that the SQS message links to.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** 40-min transcode; idle 35%; HA + scalable + reduce management; most cost-effective

🪤 **Your trap:** EC2 ASG polling SQS still = managing EC2; Lambda max 15 min

🧠 **Rule:** Long job (>15 min), event-driven → container on Fargate, Lambda calls ECS RunTask.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 upload video ──► Java app trên EC2 transcode video (~40 phút/video)
                     EC2 idle 35% thời gian trung bình

Yêu cầu: HA + scalable + giảm management overhead + MOST cost-effective
```

Đáp án đúng: **C (Container hóa app → ECS trên Fargate, Lambda gọi RunTask khi có S3 event)**. Anh chọn **D (SQS + EC2 Auto Scaling Group polling)** — vẫn là quản lý EC2, không đạt yêu cầu "giảm management overhead" và "cost-effective".

#### Vì sao C đúng

Hai giới hạn cần vượt qua:
1. **Lambda tối đa 15 phút / lần chạy** → job 40 phút chắc chắn không chạy được trên Lambda thuần.
2. Vẫn muốn **serverless, không quản lý server** → loại EC2 khỏi phương án.

```
S3 upload video
      │ (event notification)
      ▼
Lambda function (nhẹ, chỉ để trigger)
      │  gọi ECS RunTask API
      ▼
ECS task chạy trên AWS FARGATE (container hóa transcoding app, image trong ECR)
      │  chạy bao lâu tùy cần (không giới hạn 15 phút)
      ▼
Ghi kết quả vào DynamoDB
```

- **Fargate** loại bỏ hoàn toàn việc quản lý EC2/cluster — tự động scale theo số task được gọi.
- **Lambda chỉ đóng vai trò trigger** (gọi RunTask), không xử lý transcoding nên không dính giới hạn 15 phút.
- Vì task chỉ chạy khi có video mới (event-driven), không tốn chi phí compute lúc idle — giải quyết đúng vấn đề "EC2 idle 35%" trong đề.

#### Vì sao D (Anh chọn) sai

```
S3 event → SQS queue → EC2 Auto Scaling Group (poll liên tục) → transcode
```

- Vẫn phải **quản lý EC2**: AMI, patching, scaling policy, lifecycle — không giảm được management overhead như yêu cầu.
- EC2 trong ASG cần **liên tục polling SQS** để chờ việc mới → tốn chi phí ngay cả khi không có video để xử lý → **không cost-effective** bằng Fargate task chỉ chạy khi được gọi.
- Về mặt kỹ thuật vẫn "chạy được, decoupled, scalable, xử lý đúng 1 lần", nhưng thua managed/serverless option (C) ở đúng hai tiêu chí đề bài nhấn mạnh: overhead và cost.

#### Vì sao các lựa chọn khác sai

| Đáp án | Vấn đề |
|---|---|
| A. Container trên EC2, tự poll S3 | Vẫn phải EC2 chạy liên tục — không cost-effective, có thêm overhead quản lý scaling. |
| B. Lambda script trực tiếp | Vi phạm giới hạn 15 phút của Lambda — job 40 phút chắc chắn timeout. |
| D. SQS + EC2 ASG polling | Vẫn quản lý EC2, EC2 phải chạy để poll liên tục dù không có việc — không cost-effective. |
| **C. Fargate + Lambda trigger RunTask** | Serverless hoàn toàn, event-driven, không giới hạn thời gian chạy → đúng đáp án. |

#### Quy tắc nhớ cho thi

- **Job > 15 phút** → loại Lambda ngay, nghĩ đến **Fargate (ECS/EKS)**.
- **"reduce management overhead" + "event-driven" + long-running task** → pattern chuẩn: **Lambda (trigger nhẹ) → gọi ECS RunTask trên Fargate**.
- Thấy **"EC2 Auto Scaling Group polling SQS"** trong đáp án của câu về giảm overhead/cost-effective → đây gần như luôn là bẫy, vì bản chất vẫn là tự quản lý EC2.
- **"idle X% thời gian"** trong đề là gợi ý mạnh cho hướng **pay-per-use / serverless** thay vì always-on EC2.

### TD explanation

AWS Fargate is a service that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. With AWS Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing. Amazon ECS, using Fargate, allows you to run containers without managing the underlying infrastructure. It automatically scales based on demand.

One use case for ECS task definitions is on video transcoding workloads. To use video transcoding workloads on Amazon ECS, register Amazon EC2 VT1 instances. This will allow running live and pre-rendered video transcoding workloads as tasks on Amazon ECS.

Because of its scaling capability, AWS Fargate can be used to run event-driven workloads at scale. For use cases when a workload cannot be run by AWS Lambda alone because of limitations on runtime, such as Lambda’s current 15-minute memory limit, a Lambda function can be triggered and invoke an ECS task.

Using S3 event notifications to trigger the Lambda function ensures that the transcoding process starts as soon as a new video is uploaded, improving efficiency.

Therefore, the correct answer is: Build a container image out of the video transcoding application. Deploy and run the container image on Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. Create an AWS Lambda function that calls the Fargate RunTask API operation when the S3 bucket receives the file upload event notification.

The option that says: Create an Amazon Simple Queue Service (Amazon SQS) queue and configure Amazon S3 to send event notifications to the SQS queue. Set up an EC2 Auto Scaling group with a minimum size of one instance. Modify the video transcoding application to continuously poll the SQS queue, and start transcoding the files in S3 that the SQS message links to is incorrect. Although this approach decouples the components, is scalable, and ensures each file is processed only once, it is not cost-effective for the EC2 instances to continuously poll the SQS queue.

The option that says: Create an equivalent script of the application workflow and deploy it as an AWS Lambda function. Use an S3 event notification to start the processing when a new video is uploaded is incorrect. AWS Lambda currently has a function execution time limit of 900 seconds or 15 minutes before it is automatically terminated. The scenario talks about a long-running workload, and using AWS Lambda cannot fulfill this requirement.

The option that says: Build a container image out of the video transcoding application. Deploy and run the container image on an EC2 instance. Configure the container to continuously poll the S3 bucket for new videos and to transcode the files is incorrect. This solution allows for full control of the container application in the EC2 image, but it is not cost-effective as it requires the EC2 instance to be constantly running. There is also an additional management overhead of scaling the EC2 instances, which is not the best practice.

References:

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-vt1.html

https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-event-driven-and-scheduled-workloads-at-scale-with-aws-fargate.html

 

Check out this article on Amazon Elastic Container Service:

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

</details>

<a id="q35"></a>

## Q35

A media company has a serverless video encoding system. When a video clip is uploaded to an S3 bucket, an AWS Lambda function written in Python is automatically invoked to process the clip. The Lambda function encodes the video for different aspect ratios suitable for various screen devices. After processing, the application saves the S3 location of the encoded videos into a DynamoDB table.

Recently, the company started processing longer video clips, leading to Lambda function timeouts despite having set the maximum timeout limit. The company wants a redesigned architecture that ensures timeout issues will never happen again, all without having to manage the underlying infrastructure.

Which combination of actions should be taken to redesign the application’s architecture? (Select TWO.)

- **A.** Implement an AWS Step Functions state machine. Use a combination of Map and Parallel states to break down the video encoding process into smaller tasks. Configure provisioned concurrency to pre-warm Lambda functions associated with each state.
- **B.** Containerize the video encoding logic into a Docker image. Push the Docker image to the Amazon Elastic Container Registry (Amazon ECR).
- **C.** Rewrite the existing code to use Java. Update the Lambda function’s runtime setting to use the Java runtime. Enable AWS Lambda SnapStart
- **D.** Use Amazon SQS to queue the video encoding tasks and deploy an auto-scaling group of EC2 instances running the encoding logic. Set CloudWatch alarms to scale in and out based on the queue length and use S3 event notifications to enqueue tasks.
- **E.** Create an ECS task definition to use the new image stored in ECR and configure it to run tasks using the Fargate launch type. Create a Lambda function that is triggered by S3 PUT events to initiate the ECS task.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** D, E

🔑 **Key words:** Lambda timeout on long videos; never time out again; no servers to manage

🪤 **Your trap:** SQS + EC2 ASG = managing EC2

🧠 **Rule:** Lambda timeout → containerize (ECR) + Fargate task started by Lambda. Both picks = one solution.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 upload video clip ──► Lambda (Python) encode nhiều aspect ratio ──► ghi kết quả vào DynamoDB

Vấn đề: video ngày càng dài → Lambda TIMEOUT dù đã set max timeout

Yêu cầu: redesign để timeout KHÔNG BAO GIỜ xảy ra nữa, KHÔNG quản lý infrastructure
(Select TWO)
```

Đáp án đúng: **B + E** (container hóa + đẩy lên ECR, rồi chạy trên ECS Fargate được Lambda trigger). Anh chọn **D + E** — đúng E nhưng sai B, chọn nhầm D (SQS + EC2 ASG) là phương án "tự quản lý EC2".

#### Vì sao B + E đúng — và phải đi cùng nhau

Đây là câu **Select TWO** mà 2 đáp án đúng thực chất là **một giải pháp duy nhất** được tách làm hai bước:

```
Bước B: Container hóa video encoding logic → Docker image → push lên Amazon ECR
                                    │
Bước E: Tạo ECS task definition dùng image trong ECR
        → chạy bằng launch type FARGATE
        → Lambda function (trigger bởi S3 PUT event) gọi ECS RunTask để khởi động task
```

- Lambda tối đa 15 phút execution time → **không thể sửa được** bằng cấu hình, runtime hay optimization nào — đây là giới hạn cứng của Lambda, "sẽ không bao giờ timeout nữa" chỉ đạt được khi **loại Lambda ra khỏi phần xử lý nặng**.
- **Fargate** = chạy container mà **không quản lý server/cluster** — đúng yêu cầu "no infrastructure to manage".
- Lambda vẫn được giữ lại, nhưng chỉ với vai trò **trigger nhẹ** (gọi RunTask), không làm encoding logic nữa.

#### Vì sao D (Anh chọn) sai

**D = SQS + EC2 Auto Scaling Group** chạy encoding logic. Về mặt kỹ thuật giải quyết được vấn đề timeout (EC2 không có giới hạn 15 phút), nhưng:

> "this approach requires the management of EC2 instances, including their scaling policies and lifecycle"

Đề bài yêu cầu rõ **"without having to manage the underlying infrastructure"** — EC2 ASG vi phạm trực tiếp yêu cầu này dù giải quyết được timeout. Đây là mẫu bẫy quen thuộc: đáp án nghe hợp lý về mặt kỹ thuật (decoupled, scalable) nhưng bỏ qua ràng buộc "serverless/no infra management" trong đề.

#### Vì sao A, C sai

| Đáp án | Vấn đề |
|---|---|
| A. Step Functions Map/Parallel + provisioned concurrency | Chia nhỏ task và pre-warm Lambda giúp giảm cold start, nhưng **mỗi Lambda instance vẫn bị giới hạn timeout tối đa** — không loại bỏ được rủi ro timeout với video rất dài. |
| C. Đổi sang Java + Lambda SnapStart | SnapStart chỉ cải thiện **cold start latency**, không ảnh hưởng đến **maximum execution timeout** — vẫn là Lambda, vẫn bị giới hạn. |
| D. SQS + EC2 ASG | Giải quyết timeout nhưng vi phạm "no infrastructure management". |
| **B + E. ECR container + ECS Fargate task, Lambda chỉ trigger** | Loại hoàn toàn giới hạn timeout của Lambda, không quản lý server → đúng đáp án. |

#### Quy tắc nhớ cho thi

- **"Lambda timeout dù đã set max"** → không có cách "tối ưu" nào khắc phục (SnapStart, provisioned concurrency, runtime khác đều không giúp) — chỉ có cách **đưa phần việc nặng ra khỏi Lambda**.
- **"never time out again" + "no infrastructure to manage"** → kết hợp chuẩn: **container (ECR) + ECS/Fargate**, Lambda chỉ giữ vai trò trigger qua RunTask.
- Thấy đáp án dạng **"SQS + EC2 Auto Scaling Group"** giải quyết đúng vấn đề kỹ thuật nhưng đề có câu "no server/infrastructure management" → gần như luôn là bẫy, loại ngay.
- Với câu Select TWO có 2 đáp án bổ trợ nhau tạo thành 1 giải pháp hoàn chỉnh (containerize + deploy), hãy tìm cặp "nguyên nhân – kết quả" logic thay vì 2 đáp án độc lập.

### TD explanation

Elastic Container Registry (ECR) serves as a fully-managed Docker container registry, making it easier for developers to store, manage, and deploy Docker container images. Amazon Elastic Container Service (ECS) is a container management service that enables you to run Docker containers in a distributed manner across a fleet.

ECS and ECR work seamlessly together: ECS can pull Docker images stored in ECR to instantiate containers as part of tasks defined in ECS.

In the scenario, the company is experiencing timeouts with AWS Lambda due to the processing of longer video clips. Using ECS with the Fargate launch type allows for long-running tasks that go beyond the 15-minute limit imposed by Lambda. Containerizing the video encoding logic and storing the image in ECR simplifies the deployment and scaling of this service. A Lambda function triggered by S3 events can initiate these ECS tasks, thus providing a serverless architecture that satisfies the requirements of not having to manage the underlying infrastructure while eliminating the timeout issue.

Thus, the correct answers are:

– Containerize the video encoding logic into a Docker image. Push the Docker image to the Amazon Elastic Container Registry (Amazon ECR).

– Create an ECS task definition to use the new image stored in ECR, and configure it to run tasks using the Fargate launch type. Create a Lambda function that is triggered by S3 PUT events to initiate the ECS task.

The option that says: Implement an AWS Step Functions state machine. Use a combination of Map and Parallel states to break down the video encoding process into smaller tasks. Configure provisioned concurrency to pre-warm Lambda functions associated with each state is incorrect. AWS Step Functions with Map and Parallel states can indeed help break down tasks into smaller parts that can be executed by individual Lambda functions. However, even with provisioned concurrency, Lambda functions would still be subjected to a maximum execution timeout, making this option not entirely reliable for longer videos.

The option that says: Rewrite the existing code to use Java. Update the Lambda function’s runtime setting to use the Java runtime. Enable AWS Lambda SnapStart is incorrect. While switching to Java and enabling AWS Lambda SnapStart could reduce start-up latency, this approach doesn’t eliminate the risk of timeout errors. Lambda functions remain constrained by a maximum execution time, regardless of the runtime or optimizations used.

The option that says: Use Amazon SQS to queue the video encoding tasks and deploy an auto-scaling group of EC2 instances running the encoding logic. Set CloudWatch alarms to scale in and out based on the queue length and use S3 event notifications to enqueue tasks is incorrect. Using Amazon SQS with an auto-scaling group of EC2 instances does enable the handling of long-running tasks, but this approach requires the management of EC2 instances, including their scaling policies and lifecycle

 

References:

https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html

https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html

 

Check out this Amazon ECR and AWS Fargate Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-container-registry-amazon-ecr/

https://tutorialsdojo.com/aws-fargate/

</details>

<a id="q28"></a>

## Q28

A company is managing a hybrid environment comprising on-premises servers and Amazon EC2 instances. Their servers are a mix of Linux and Windows systems. The company utilizes AWS Security Hub as its cloud security posture management (CSPM) service to automate security best practice checks, aggregate alerts, and enables automated remediation.

Separate teams handle the environment, each using different tools for patching. The company wants to simplify this process and requires a consolidated view of patch statuses across all servers.

Which combination of actions will meet the requirements? (Select TWO.)

- **A.** Create an AWS Systems Manager Automation document for running patching jobs. Use Amazon EventBridge to schedule these jobs and configure the AWS Systems Manager OpsCenter to generate patch compliance reports.
- **B.** Generate patch compliance reports using AWS System Manager Patch Manager.
- **C.** Register all servers as managed nodes in AWS System Manager. Use AWS System Manager Patch Manager for handling patch operations.
- **D.** Create a custom AWS Config rule for detecting non-compliant patches across servers. Set up an AWS Config remediation rule using AWS Systems Manager Automation documents to apply patches. Configure AWS Config to send patch compliance reports to an Amazon S3 bucket.
- **E.** Generate patch compliance reports using Amazon Inspector. Use Amazon Athena for aggregating and viewing patch compliance reports.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C · **You picked:** B, D

🔑 **Key words:** hybrid Linux+Windows; different patch tools; consolidated patch status

🪤 **Your trap:** Config = config compliance, not patch operations

🧠 **Rule:** Patching + patch compliance (EC2 + on-prem) → SSM managed nodes + Patch Manager.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hybrid environment: on-premises servers (Linux + Windows) + EC2 instances
Đã có: AWS Security Hub (CSPM — security posture, không phải patch tool)

Vấn đề: nhiều team dùng nhiều tool patching khác nhau
Yêu cầu: đơn giản hóa quy trình + CONSOLIDATED VIEW patch status trên tất cả server
(Select TWO)
```

Đáp án đúng: **B + C** (Patch Manager để cả patching lẫn báo cáo, cần đăng ký server làm managed node trước). Anh chọn **B + D** — đúng B nhưng chọn nhầm D (AWS Config) vào vai trò mà Config không thực sự đảm nhiệm.

#### Vì sao B + C đúng — và vì sao phải đi cùng nhau

```
Bước C: Register TẤT CẢ server (EC2 + on-prem Linux/Windows) làm MANAGED NODE trong SSM
              │ (điều kiện tiên quyết — SSM chỉ patch được managed node)
              ▼
         AWS Systems Manager PATCH MANAGER
              │  → thực hiện patch operations (cả OS lẫn 1 số app)
              │
Bước B: PATCH MANAGER cũng chính là nơi generate patch compliance reports
              → console view + export CSV — CONSOLIDATED, một nguồn duy nhất
```

- **SSM quản lý được cả hybrid environment**: EC2 lẫn on-premises server (Linux + Windows), miễn là đăng ký làm managed node (qua SSM Agent).
- **Patch Manager** vừa **thực hiện patching** (thay thế nhiều tool rời rạc của các team), vừa **sinh báo cáo compliance tập trung** — giải quyết đúng cả hai vế của yêu cầu: "simplify process" và "consolidated view".
- C là điều kiện bắt buộc để B hoạt động — không có managed node thì Patch Manager không patch/scan được gì.

#### Vì sao D (Anh chọn) sai

**AWS Config** dùng để **assess/audit/evaluate configuration** của AWS resource (compliance theo rule), **không phải công cụ patch operations**. Dùng Config rule + remediation qua SSM Automation document để "vá lỗi" là một pattern có thể làm được về mặt kỹ thuật, nhưng:
- Không **đơn giản hóa** quy trình patch hiện có — vẫn phải xây thêm custom Config rule, remediation logic.
- Không cho cái nhìn patch status **trực tiếp, tập trung** như Patch Manager vốn đã có sẵn — phải tự đẩy report ra S3 rồi tổng hợp.
- Về bản chất, D là dùng sai công cụ: Config trả lời "resource có compliant với rule không", không phải "server đã patch đến đâu".

#### Vì sao các lựa chọn khác sai

| Đáp án | Vấn đề |
|---|---|
| A. SSM Automation doc + EventBridge + OpsCenter | Có thể patch được, nhưng OpsCenter không phải công cụ chuyên cho compliance report — overhead cao hơn Patch Manager vốn làm sẵn cả hai việc. |
| D. AWS Config rule + remediation | Config để audit config compliance, không phải patch operations — không đúng công cụ, thêm overhead. |
| E. Amazon Inspector + Athena | Inspector là vulnerability assessment, **không quét được on-premises server**, và cũng không phải patch management tool. |
| **B + C. Patch Manager (patching + report) + managed node registration** | Đúng công cụ, đúng phạm vi hybrid, đơn giản và tập trung → đúng đáp án. |

#### Lưu ý thực tế

- Amazon Inspector chỉ hoạt động trên tài nguyên AWS (EC2, ECR image, Lambda...) — không có agent/coverage cho on-premises server, nên bất kỳ đề nào có "hybrid" + "on-premises" mà đáp án dùng Inspector để quét toàn bộ đều sai.
- Patch Manager cho phép **scan-only** (chỉ báo cáo thiếu patch gì) hoặc **scan-and-install** tự động — linh hoạt theo nhu cầu từng team.

#### Quy tắc nhớ cho thi

- **"hybrid" (on-prem + EC2) + "patch"** → luôn nghĩ đến **SSM (managed node) + Patch Manager**, không phải Config hay Inspector.
- **AWS Config** = configuration compliance/audit, không phải patch tool — dù có thể "remediate" qua SSM, nó không phải lựa chọn tối ưu khi đã có Patch Manager chuyên dụng.
- **Amazon Inspector** = vulnerability scanning cho AWS resource, **không cover on-premises**.
- Thấy "consolidated patch status report" → Patch Manager tự nó đã cung cấp cả patching lẫn report, không cần ghép thêm service khác.

### TD explanation

AWS Systems Manager allows you to manage your hybrid environment as it can work with both on-premises servers and AWS instances. AWS Systems Manager Patch Manager, a feature of AWS Systems Manager, enables you to automate the process of patching managed instances with both security related and other types of updates.

You can use Patch Manager to apply patches for both operating systems and applications (On Windows Server, application support is limited to updates for applications released by Microsoft.) You can use Patch Manager to install Service Packs on Windows nodes and perform minor version upgrades on Linux nodes. You can patch fleets of Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, on-premises servers, and virtual machines (VMs) by operating system type. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

Patch Manager provides a convenient view of patch status in the console and lets you export this data as a CSV file for analysis.

In the scenario, using Patch Manager allows you to both conduct patching operations and generate a consolidated view of patch statuses. This simplifies the overall patching process.

Hence, the correct answers are:

– Register all servers as managed nodes in AWS System Manager. Use AWS System Manager Patch Manager for handling patch operations.

– Generate patch compliance reports using AWS System Manager Patch Manager.

The option that says: Create a custom AWS Config rule for detecting non-compliant patches across servers. Set up an AWS Config remediation rule using AWS Systems Manager Automation documents to apply patches. Configure AWS Config to send patch compliance reports to an Amazon S3 bucket is incorrect. AWS Config is primarily designed for assessing, auditing, and evaluating the configurations of AWS resources, not specifically for managing patch operations. While it could provide some level of oversight for patch compliance, it would not simplify the patching process itself nor provide a straightforward, consolidated view of patch statuses.

The option that says: Create an AWS Systems Manager Automation document for running patching jobs. Use Amazon EventBridge to schedule these jobs and configure the AWS Systems Manager OpsCenter to generate patch compliance reports is incorrect. This option would simplify the patching process to some extent. However, setting up this integration would likely have more overhead compared to using AWS Systems Manager Patch Manager, which is designed specifically for managing patches and can provide a more streamlined and integrated solution.

The option that says: Generate patch compliance reports using Amazon Inspector. Use Amazon Athena for aggregating and viewing patch compliance reports is incorrect. Amazon Inspector is mainly a security vulnerability assessment service, not a tool for patch management. Moreover, Amazon Inspector is not capable of scanning on-premises servers.

 

References:

https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-reports.html

 

Check out this AWS Systems Manager Cheat Sheet:

https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q38"></a>

## Q38

A company manages thousands of AWS accounts using AWS Organizations. To ensure compliance and maintain a uniform environment, each member account requires a standardized Virtual Private Cloud (VPC) with specific networking configurations.

The company’s DevOps team has already prepared an AWS CloudFormation template for creating the VPC. They want the deployment of the CloudFormation template to be automated in a consistent manner across the organization. Moreover, the template must be automatically deployed in newly joined accounts.

Which combination of actions will meet the requirements? (Select TWO.)

- **A.** Enable Service Catalog as a trusted service on AWS Organizations. Provision service-managed permissions.
- **B.** Enable CloudFormation StackSet as a trusted service on AWS Organizations.
- **C.** Create a portfolio in AWS Service Catalog and associate the CloudFormation template as a product. Grant access to this portfolio to all AWS accounts in the organization.
- **D.** In the management account, set up a stack set using the CloudFormation template. Use the service-managed permission model to create the stack. Activate Automatic deployment and set the Organizations as the deployment target.
- **E.** In the member accounts, set up a stack set using the CloudFormation template. Use a self-managed permission model to create the stack. Use Stackset drift detection to enable deployment to new accounts. Specify each Organization Unit (OU) as a deployment target.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** D, E

🔑 **Key words:** thousands of accounts; standardized VPC; auto-deploy to NEW accounts

🪤 **Your trap:** Self-managed stack sets in member accounts

🧠 **Rule:** Org-wide CFN → StackSets trusted access + service-managed permissions in mgmt account + automatic deployment.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
┌─────────────────────────────────────────────┐
│  Management Account                          │
│    └── CloudFormation StackSet (VPC template) │
│                                                │
│  Member Account 1, 2, 3, ... (hàng nghìn)     │
│  Member Account MỚI (join sau)  ← phải TỰ ĐỘNG có VPC chuẩn │
└─────────────────────────────────────────────┘

Yêu cầu:
  - Deploy VPC template nhất quán trên TOÀN organization
  - Account mới join → tự động được deploy, không cần thao tác thủ công
```

Đáp án đúng: **B (bật StackSets làm trusted service)** + **D (tạo stack set ở management account, service-managed, automatic deployment, target = Organizations)**. Anh chọn đúng D nhưng chọn sai B, chọn nhầm **E** (self-managed stack set đặt ở member accounts).

#### Vì sao E sai — trap kinh điển

E mô tả việc **tạo stack set ngay trong từng member account**, dùng **self-managed permission model**, rồi dùng "drift detection" để "enable deployment to new accounts". Sai ở ba điểm:

```
Self-managed stack set trong member account
    → đi ngược lại chính mục đích của StackSets
       (StackSets sinh ra để quản lý TẬP TRUNG từ 1 account)
    → phải tạo thủ công ở TỪNG account, không scale cho "thousands of accounts"
    → drift detection chỉ dùng để PHÁT HIỆN lệch cấu hình,
       không có chức năng tự động deploy cho account mới
```

Đây đúng là "trap": nhìn thấy "StackSet" + "self-managed" tưởng là giải pháp hợp lệ, nhưng self-managed permission model đòi hỏi tạo IAM role thủ công ở từng account (administrator role ở nguồn, execution role ở đích) — không tận dụng được tích hợp trực tiếp với Organizations.

#### Vì sao B + D đúng

**Service-managed permission model** cho phép StackSets dùng **trusted access với AWS Organizations** — không cần tạo IAM role thủ công ở từng account. Điều kiện tiên quyết là **bật CloudFormation StackSets làm trusted service trong Organizations** (đáp án B).

Sau đó ở **management account**, tạo stack set:

```
Stack set (service-managed permissions)
    → Deployment target: Organizations (chọn root hoặc OU)
    → Automatic deployment: ON
    → Kết quả: account mới join Organizations/OU
              → CloudFormation tự động deploy stack, KHÔNG cần thao tác gì thêm
```

Đây chính là cơ chế duy nhất trong AWS đáp ứng "tự động deploy cho account mới join" mà không cần con người can thiệp.

#### Vì sao A và C sai (Service Catalog)

Service Catalog cho phép chuẩn hóa danh mục sản phẩm IT (bao gồm CloudFormation template), nhưng **không có cơ chế tự động deploy khi account mới join organization**. Cấp quyền hay share portfolio là hành động thủ công, phải lặp lại cho từng account mới — không thỏa "automatically deployed in newly joined accounts".

| Đáp án | Cơ chế | Tự động cho account mới? | Quản lý tập trung? |
|---|---|---|---|
| **B+D. StackSets trusted access + service-managed + auto deploy** | Native Organizations integration | Có | Có (từ management account) |
| E. Self-managed stack set trong member account | IAM role thủ công | Không | Không |
| A/C. Service Catalog portfolio | Cấp quyền catalog | Không | Một phần |

#### Quy tắc nhớ cho thi

- **"Org-wide, tự động deploy cho account mới join"** → **StackSets + trusted access + service-managed permissions + automatic deployment, target = Organizations/OU**
- **"self-managed permission model"** trong ngữ cảnh Organizations-wide → hầu như luôn là bẫy, vì đòi hỏi IAM role thủ công từng account
- **Service Catalog** → chuẩn hóa "self-service catalog cho end user chọn sản phẩm", không phải "tự động rollout khi có account mới"
- **"drift detection"** → chỉ để phát hiện lệch cấu hình so với template, không liên quan đến việc mở rộng deployment

### TD explanation

AWS CloudFormation StackSets extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation. Using an administrator account, you define and manage an AWS CloudFormation template and use the template as the basis for provisioning stacks into selected target accounts across specified regions.

A stack set lets you create stacks in AWS accounts across regions by using a single AWS CloudFormation template. All the resources included in each stack are defined by the stack set’s AWS CloudFormation template. As you create the stack set, you specify the template to use, as well as any parameters and capabilities that the template requires.

In the scenario, in order for StackSets to have the necessary permissions to perform operations in AWS Organizations’ accounts, it must be enabled as a trusted service. To ensure the template is automatically deployed to all accounts (including newly joined ones), a stack set should be created in the management account with service-managed permissions. The AWS Organizations should be set as the deployment target, and automatic deployments should be enabled.

Hence, the correct answers are:

– Enable CloudFormation StackSet as a trusted service on AWS Organizations.

– In the management account, set up a stack set using the CloudFormation template. Use the service-managed permission model to create the stack. Activate Automatic deployment and set the Organizations as the deployment target.

The option that says: Enable Service Catalog as a trusted service on AWS Organizations. Provision service-managed permissions is incorrect. While AWS Service Catalog can be used to create and manage catalogs of IT services, it doesn’t inherently offer a solution for automatic deployments across AWS accounts in an organization, especially for newly joined accounts. The requirement in the question is specifically about deploying AWS CloudFormation templates across multiple accounts and not about managing a service catalog.

The option that says: In the member accounts, set up a stack set using the CloudFormation template. Use a self-managed permission model to create the stack. Use Stackset drift detection to enable deployment to new accounts. Specify each Organization Unit (OU) as a deployment target is incorrect. Setting up a stack set in each member account manually defeats the purpose of AWS CloudFormation StackSets, which is designed to manage resources centrally from a single AWS account. Additionally, StackSet drift detection is used for checking configuration consistency, not for enabling deployment to new accounts.

The option that says: Create a portfolio in AWS Service Catalog and associate the CloudFormation template as a product. Grant access to this portfolio to all AWS accounts in the organization is incorrect. While this option might provide a way to standardize the deployment of services, it still doesn’t address the need for automatic deployment, especially for new accounts joining the organization.

 

References:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started.html

 

Check out this AWS CloudFormation Cheat Sheet:

https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q51"></a>

## Q51

A company hosts its core business applications on a fleet of Linux-based Amazon EC2 instances managed in AWS Systems Manager Fleet Manager. One day, an employee who maintained these instances abruptly resigned. The company is concerned that the employee who left might still possess a copy of the key pairs used to SSH to these instances, as this raises a security risk.
Which of the following options should the Solutions Architect implement to rotate the SSH keys successfully?

- **A.** Generate a new key pair in the EC2 Console. Extract the public key from the newly created key pair and write a shell script that will update the authorized_keys in the .ssh directory with the new public key. Utilize AWS Systems Manager Run Command and choose the AWS-RunShellScript document to execute the shell script on these EC2 instances.
- **B.** Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances.
- **C.** Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Run Command and choose AWS-RunShellScript document to execute the shell script on these EC2 instances.
- **D.** Manually generate a new key pair and write a shell script that will update the authorized_keys in the .ssh directory based on the new public key value. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** rotate SSH keys on fleet managed by SSM Fleet Manager

🪤 **Your trap:** Downloaded .pem = PRIVATE key; authorized_keys needs PUBLIC key

🧠 **Rule:** Key rotation → new key pair, extract public key, push via SSM Run Command (AWS-RunShellScript).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Fleet Linux EC2 instances (SSM Fleet Manager)
    Nhân viên phụ trách SSH key đã nghỉ việc
    Lo ngại: người này có thể vẫn giữ private key
    → cần XOAY VÒNG (rotate) SSH key trên toàn bộ fleet
```

Đáp án đúng: **A**. Anh chọn **C** — sai vì hiểu nhầm bản chất của file `.pem` tải về khi tạo key pair.

#### Bẫy cốt lõi: .pem là PRIVATE key, không phải PUBLIC key

Khi tạo key pair mới trong EC2 Console, file `.pem` bạn tải về là **private key**, EC2 chỉ giữ lại **public key**. Cơ chế boot của Linux EC2:

```
Lúc EC2 instance khởi động lần đầu:
    public key của key pair
        → được ghi vào ~/.ssh/authorized_keys trên instance
    private key (.pem)
        → chỉ nằm ở máy người dùng, dùng để SSH vào
```

Muốn **rotate** SSH access, việc cần làm là cập nhật **authorized_keys** trên từng instance với **public key mới**. Đáp án C (và cả B, D) viết "cập nhật authorized_keys dựa trên downloaded pem key" — nghĩa là định dùng private key để ghi vào authorized_keys, điều này sai về bản chất kỹ thuật: `authorized_keys` chỉ chấp nhận **public key**, không phải private key.

Đáp án A viết đúng quy trình: "Extract the public key from the newly created key pair" rồi mới đưa vào authorized_keys.

#### Vì sao dùng SSM Run Command (AWS-RunShellScript), không phải Automation

```
AWS Systems Manager
├── Run Command          → chạy shell script trực tiếp trên managed node
│     └── Document: AWS-RunShellScript  ← dùng được ở đây
└── Automation            → chạy "runbook" (workflow các bước SSM tự động,
                             ví dụ patch, snapshot, restart...)
      └── AWS-RunShellScript KHÔNG dùng được trong Automation runbook
```

B và D đều chọn "SSM Automation" + document "AWS-RunShellScript" — đây là kết hợp không hợp lệ: `AWS-RunShellScript` là một **Run Command document**, không phải một Automation runbook step. Automation dùng runbook riêng (ví dụ `AWS-RunPatchBaseline`, `AWS-RestartEC2Instance`...) chứ không nhận document Run Command trực tiếp.

#### Bảng so sánh 4 đáp án

| Đáp án | Nguồn key đưa vào authorized_keys | Cơ chế SSM | Hợp lệ? |
|---|---|---|---|
| **A** | Public key (extract đúng) | Run Command + AWS-RunShellScript | Đúng |
| B | .pem (private key — sai) | Automation + AWS-RunShellScript (sai kết hợp) | Sai 2 lỗi |
| C | .pem (private key — sai) | Run Command + AWS-RunShellScript | Sai 1 lỗi (đây là lỗi Anh mắc) |
| D | Public key (đúng) | Automation + AWS-RunShellScript (sai kết hợp) | Sai 1 lỗi |

#### Quy tắc nhớ cho thi

- **File .pem tải về từ EC2 Console = PRIVATE key**, luôn luôn. Không bao giờ đưa .pem vào `authorized_keys`.
- **`authorized_keys` chỉ chứa PUBLIC key.**
- **Chạy shell script trực tiếp trên fleet EC2/on-prem** → SSM **Run Command**, document `AWS-RunShellScript`.
- **SSM Automation** = chạy runbook đa bước (thường có sẵn hoặc tự viết bằng SSM document loại Automation), **không nhận** `AWS-RunShellScript` làm step.
- Thấy đề nói "rotate SSH key trên fleet do SSM quản lý" → nghĩ ngay: tạo key pair mới → lấy public key → Run Command đẩy vào từng instance.

### TD explanation

A key pair, consisting of a public key and a private key, is a set of security credentials that you use to prove your identity when connecting to an Amazon EC2 instance. Amazon EC2 stores the public key on your instance, and you store the private key. For Linux instances, the private key allows you to securely SSH into your instance.

AWS Systems Manager has an extensive collection of features and capabilities to manage your AWS and hybrid systems. This service allows you to centralize operational data from various AWS services and automate manual tasks on both your on-premises and AWS resources. One of its capabilities is the AWS Run Command, which can be used to remotely and securely manage the configuration of your managed nodes.

A managed node is any Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, or on-premises server or virtual machine (VM) in your hybrid environment that has been configured for Systems Manager. Run Command allows you to automate common administrative tasks and perform one-time configuration changes at scale. You can use Run Command from the AWS Management Console, the AWS Command Line Interface (AWS CLI), AWS Tools for Windows PowerShell, or the AWS SDKs. Run Command is offered at no additional cost.

AWS Run Command has a document called AWS-RunShellScript that can be used to run Linux shell scripts or specify the path to a script to run.

Therefore, the correct answer is: Generate a new key pair in the EC2 Console. Extract the public key from the newly created key pair and write a shell script that will update the authorized_keys in the .ssh directory with the new public key. Utilize AWS Systems Manager Run Command and choose the AWS-RunShellScript document to execute the shell script on these EC2 instances.

The option that says: Manually generate a new key pair and write a shell script that will update the authorized_keys in the .ssh directory based on the new public key value. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances is incorrect because the AWS-RunShellScript document can’t be used in SSM Automation runbooks.

The option that says: Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Run Command and choose AWS-RunShellScript document to execute the shell script on these EC2 instances is incorrect because the downloaded pem key from the EC2 Console is just a private key. When your instance boots for the first time, the public key is placed on the Linux instance in an entry within ~/.ssh/authorized_keys, not the private key.

The option that says: Create a new key pair in the EC2 Console. Write a shell script that will update the authorized_keys in the .ssh directory based on the new downloaded pem key. Utilize AWS Systems Manager Automation and choose AWS-RunShellScript document to execute the shell script on these EC2 instances is incorrect because the downloaded pem key from the EC2 Console is only a private key. When your instance boots for the first time, the public key is placed on the Linux instance in an entry within ~/.ssh/authorized_keys, not the private key. Also, the AWS-RunShellScript document can’t be used in SSM Automation runbooks.

 

References:

https://aws.amazon.com/systems-manager/

https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-plugins.html

 

Check out these AWS Systems Manager Cheat Sheets:

https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q68"></a>

## Q68

A company hosts its application on a fleet of Amazon EC2 instances in an Auto Scaling group. The Quality Assurance (QA) team performs stress tests on the application. As part of the testing, several temporary environments are created from multiple AWS regions. With the current process, only the QA manager assumes an IAM role that has permission to use AWS CloudFormation, Amazon EC2, and Auto Scaling APIs. The QA manager launches CloudFormation stacks to create temporary environments. The upper management wants to make the testing process more efficient by allowing the QA members to create their own environments.

Which of the following options is the recommended action to allow the QA members to create their own temporary environments while following the principle of least privilege?

- **A.** Use the environment templates to create applications in AWS Elastic Beanstalk. Grant the QA team’s IAM group permission to use only Elastic Beanstalk APIs. Instruct the QA members to use Elastic Beanstalk CLI for a secure and automated launching of multiple environments.
- **B.** Create a dedicated Amazon S3 bucket to store the AWS CloudFormation templates. Grant permissions for the QA members to assume the QA Manager’s IAM role but add restrictions to allow access to the templates and only the resources they created. Instruct the QA members to launch the templates using the CloudFormation console.
- **C.** Create multiple Amazon EC2 instances for each environment. Use AWS Systems Manager Automation runbook to configure the environments. Grant the QA team’s IAM group permission to use Amazon EC2 and AWS SSM APIs. Instruct the QA members to launch the environments by provisioning the EC2 instances.
- **D.** Create a product catalog that includes the AWS CloudFormation templates in AWS Service Catalog. Configure a launch constraint to the AWS Service Catalog product and grant the QA team’s IAM group permission to use Service Catalog APIs. Instruct the QA members to launch the templates using the AWS Service Catalog console only.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** QA members create own environments from CFN templates; no broad permissions

🪤 **Your trap:** Elastic Beanstalk = convert templates, grants broad perms

🧠 **Rule:** Self-service provisioning with least privilege → Service Catalog product + launch constraint.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
QA Manager (hiện tại)
    IAM role duy nhất → CloudFormation + EC2 + Auto Scaling APIs
    → tự tay launch CloudFormation stack cho môi trường test tạm

Yêu cầu mới:
    Cho phép QA MEMBERS tự tạo môi trường riêng
    Vẫn phải theo NGUYÊN TẮC LEAST PRIVILEGE
    (mỗi người chỉ launch/quản lý được resource của MÌNH)
```

Đáp án đúng: **D (Service Catalog product + launch constraint)**. Anh chọn **A (Elastic Beanstalk)** — hợp lý về mặt "tự động hóa" nhưng sai vì đi lệch khỏi asset đã có (CloudFormation template) và không thực sự giải quyết bài toán phân quyền.

#### Vì sao D đúng — đúng bài toán "self-service + least privilege"

AWS Service Catalog được thiết kế chính xác cho ngữ cảnh này: catalog administrator (QA Manager) chuẩn bị sẵn CloudFormation template, đóng gói thành **product** trong **portfolio**, rồi gắn **launch constraint** — launch constraint gán một IAM role cụ thể mà Service Catalog sẽ dùng để tạo resource khi end-user launch product đó.

```
QA Manager (catalog admin)
    → tạo Portfolio + Product (từ CFN template có sẵn)
    → gắn Launch Constraint (IAM role riêng cho việc launch)
    → cấp quyền Service Catalog APIs cho IAM group của QA members

QA member
    → chỉ cần quyền gọi Service Catalog APIs (rất hẹp)
    → launch product qua Service Catalog console
    → Service Catalog dùng launch constraint role để tạo resource
    → QA member KHÔNG cần quyền trực tiếp lên CloudFormation/EC2/ASG
```

Đây là điểm mấu chốt: end-user chỉ cần quyền Service Catalog, không cần quyền trực tiếp lên CloudFormation hay EC2 — đúng nguyên tắc least privilege, đồng thời tận dụng được CFN template đã có sẵn.

#### Vì sao A (Elastic Beanstalk) sai dù nghe hợp lý

Elastic Beanstalk cũng "tự động hóa" việc launch môi trường, nhưng:

```
CloudFormation template có sẵn
    → phải CONVERT sang Elastic Beanstalk application
    → khó bảo trì, tốn công mỗi khi cần sửa nhiều EB application
```

Đề bài nói rõ QA Manager "đã có" CloudFormation template — chuyển hướng sang Elastic Beanstalk bỏ phí tài sản này và tạo thêm một tầng chuyển đổi không cần thiết, khó đồng bộ khi template gốc thay đổi.

#### Vì sao B và C sai

- **B (assume QA Manager's role)**: mọi member dùng chung 1 role → mọi resource do member A tạo cũng thuộc quyền truy cập của member B, C... — vi phạm trực tiếp least privilege, không cô lập được resource theo từng người.
- **C (SSM Automation runbook + tự provision EC2)**: bỏ hẳn CloudFormation, quay về quản lý thủ công từng EC2 instance — không scalable, không tận dụng được automation/resource management đã có của CloudFormation.

| Đáp án | Có dùng lại CFN template? | Cô lập resource theo người dùng? | Quyền end-user |
|---|---|---|---|
| **D. Service Catalog + launch constraint** | Có | Có | Chỉ Service Catalog APIs |
| A. Elastic Beanstalk | Không (phải convert) | Một phần | Chỉ EB APIs nhưng phải quản lý nhiều app |
| B. Assume QA Manager role | Có | Không — dùng chung role | Toàn quyền CFN/EC2/ASG qua assumed role |
| C. EC2 + SSM Automation | Không | Không | EC2 + SSM APIs (rộng) |

#### Quy tắc nhớ cho thi

- **"Cho end-user tự launch resource từ template có sẵn, nhưng giới hạn quyền"** → **AWS Service Catalog + Launch Constraint**
- **"Nhiều người share chung 1 IAM role"** → luôn là dấu hiệu vi phạm least privilege
- **"Đã có CloudFormation template, đừng convert sang thứ khác"** nếu đề không yêu cầu đổi công nghệ nền
- Service Catalog = catalog admin chuẩn bị product + constraint, end-user chỉ cần quyền catalog rất hẹp

### TD explanation

AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for AWS. These IT services can include everything from virtual machine images, servers, software, databases, and more to complete multi-tier application architectures.

AWS Service Catalog allows organizations to centrally manage commonly deployed IT services and helps organizations achieve consistent governance and meet compliance requirements. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.

AWS Service Catalog supports the following types of users:

Catalog administrators (administrators) – Manage a catalog of products (applications and services), organizing them into portfolios and granting access to end users. Catalog administrators prepare AWS CloudFormation templates, configure constraints, and manage IAM roles for products to provide for advanced resource management.

End users – Receive AWS credentials from their IT department or manager and use the AWS Management Console to launch products to which they have been granted access. Sometimes referred to as simply users, end users may be granted different permissions depending on your operational requirements. For example, a user may have the maximum permission level (to launch and manage all of the resources required by the products they use) or only permission to use particular service features.

Therefore, the correct answer is: Create a product catalog that includes the AWS CloudFormation templates in AWS Service Catalog. Configure a launch constraint to the AWS Service Catalog product and grant the QA team’s IAM group permission to use Service Catalog APIs. Instruct the QA members to launch the templates using the AWS Service Catalog console only. With Service Catalog, the users can use CloudFormation templates to launch the environments. Access can be restricted by the Service Catalog administrator.

The option that says: Create a dedicated Amazon S3 bucket to store the AWS CloudFormation templates. Grant permissions for the QA members to assume the QA Manager’s IAM role but add restrictions to allow access to the templates and only the resources they created. Instruct the QA members to launch the templates using the CloudFormation console is incorrect. This is possible; however, it is not recommended. Assuming a role will mean that all resources will be created by that role. Therefore, all other members assuming the role will have access to all resources created by other team members.

The option that says: Create multiple Amazon EC2 instances for each environment. Use AWS Systems Manager Automation runbook to configure the environments. Grant the QA team’s IAM group permission to use Amazon EC2 and AWS SSM APIs. Instruct the QA members to launch the environments by provisioning the EC2 instances is incorrect. This approach would not be efficient or scalable, as it would require manual management of each EC2 instance. Also, it doesn’t take advantage of the automation and resource management features provided by AWS CloudFormation, which can simplify the process of creating and managing AWS resources.

The option that says: Use the environment templates to create applications in AWS Elastic Beanstalk. Grant the QA team’s IAM group permission to use only Elastic Beanstalk APIs. Instruct the QA members to use Elastic Beanstalk CLI for a secure and automated launching of multiple environments is incorrect. This may be possible but not recommended, as this will require converting the CloudFormation templates to Elastic Beanstalk applications. This is difficult to maintain and time-consuming in case you need to modify multiple EB applications.

 

References:

https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html

https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html

https://docs.aws.amazon.com/servicecatalog/latest/userguide/launch-stacksets.html

 

Check out this AWS Service Catalog Cheat Sheet:

https://tutorialsdojo.com/aws-service-catalog/

</details>

<a id="q72"></a>

## Q72

An IT company provides on-demand video training materials to its employees. High-resolution MP4 format videos are created monthly to increase the topics covered in the video library. Most employees that will view the videos are working remotely from different countries. The video application installed on the employee laptops requires the videos to be in HTTP Live Streaming (HLS) format. The management asked the solutions architect to design a cost-effective solution that will transcode the training videos into the proper format.

Which of the following architectures meet the above requirements while maintaining high availability and good quality video transmission?

- **A.** Create a pipeline in AWS CodePipeline with stages that transcode the high-resolution MP4 videos into the HLS format and send the transcoded videos to an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Then, set up an endpoint in AWS Wavelength and configure it to serve the transcoded videos from the S3 bucket.
- **B.** Create a pipeline on Amazon Elastic Transcoder to transcode the high-resolution MP4 videos into the HLS format. Host the transcoded videos on large EBS volumes attached to Amazon EC2 instances. Configure automated EBS snapshots to back up the video files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos.
- **C.** Create a Jenkins pipeline to transcode the high-resolution MP4 videos. Use an SQS queue to distribute the transcoding job to a set of Amazon EC2 instances in an Auto Scaling group that scales based on the length of the queue. Store the transcoded videos on EBS volumes and configure automated snapshots to back up the files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos.
- **D.** Create a queue in AWS Elemental MediaConvert to transcode the high-resolution MP4 videos into the HLS format. Store the transcoded videos on an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Create an Amazon CloudFront distribution and set the S3 bucket as the origin to serve the transcoded videos.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** MP4 → HLS; cost-effective; HA; global remote viewers

🪤 **Your trap:** Jenkins + EC2 + EBS = DIY, low HA

🧠 **Rule:** Video transcoding → Elemental MediaConvert + S3 + CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Video training MP4 (độ phân giải cao, sinh mới hàng tháng)
    → cần TRANSCODE sang HLS (HTTP Live Streaming)
    → người xem: nhân viên remote, nhiều quốc gia
    → yêu cầu: cost-effective + high availability + good quality delivery
```

Đáp án đúng: **D (AWS Elemental MediaConvert + S3 + CloudFront)**. Anh chọn **C (Jenkins + SQS + EC2 Auto Scaling + EBS + CloudFront)** — giải pháp DIY tái tạo lại đúng những gì MediaConvert đã làm sẵn.

#### Vì sao C sai — mẫu hình "tự xây lại managed service"

```
C tự xây:
  Jenkins pipeline (tự quản lý CI server)
      → SQS queue phân phối job
      → EC2 Auto Scaling group xử lý transcode
      → EBS volumes lưu video đã transcode
      → EBS snapshot định kỳ để backup
      → CloudFront trỏ origin vào EC2

Vấn đề:
  - Toàn bộ hạ tầng transcode phải tự vận hành, tự scale, tự vá lỗi
  - Lưu trữ video trên EBS đắt hơn nhiều so với S3, lại giới hạn theo AZ
  - Origin là EC2 → phụ thuộc tải, không có độ bền/HA như S3
  - Đây chính xác là công việc AWS Elemental MediaConvert làm sẵn, managed, pay-as-you-go
```

AWS đã có dịch vụ managed transcoding chuyên dụng (MediaConvert) — khi đề hỏi "cost-effective" và "high availability" cho một tác vụ có sẵn managed service tương ứng, tự dựng pipeline bằng EC2/Jenkins gần như luôn là đáp án sai.

#### Vì sao D đúng

```
AWS Elemental MediaConvert (queue)
    → transcode MP4 → HLS, pay-as-you-go, không cần quản lý hạ tầng
    → output lưu trên S3 (durable, rẻ hơn EBS nhiều)
    → Lifecycle Management: video gốc → S3 Glacier Instant Retrieval (giảm chi phí lưu trữ)
    → CloudFront (origin = S3 bucket) phân phối toàn cầu cho remote viewers
```

MediaConvert được AWS định vị là dịch vụ kế thừa thay thế Elastic Transcoder, tối ưu cho scale và xử lý song song nhiều file — đúng use case "hàng tháng có thêm video mới cần transcode".

#### Vì sao B sai (Elastic Transcoder + EBS)

Dù dùng đúng dịch vụ transcode chuyên dụng (Elastic Transcoder), nhưng vẫn lưu video trên **EBS volumes gắn EC2** — kém cost-effective hơn S3, và hiệu năng phục vụ phụ thuộc tải của EC2 instance (không tách biệt storage/serving như kiến trúc S3 + CloudFront).

#### Vì sao A sai (CodePipeline + Wavelength)

CodePipeline là dịch vụ CI/CD để triển khai ứng dụng, không có cơ chế transcode video trực tiếp trong stage. AWS Wavelength phục vụ ứng dụng cần độ trễ cực thấp qua mạng 5G — không liên quan đến nhân viên remote phân tán nhiều quốc gia dùng mạng thông thường.

| Đáp án | Dịch vụ transcode | Nơi lưu output | Origin CloudFront | Vấn đề |
|---|---|---|---|---|
| **D. MediaConvert** | Managed, pay-as-you-go | S3 | S3 bucket | Không có |
| B. Elastic Transcoder | Managed | EBS (EC2) | EC2 | Lưu trữ/serving kém cost-effective |
| C. Jenkins + EC2 | Tự xây (DIY) | EBS (EC2) | EC2 | DIY thay managed service, tốn vận hành |
| A. CodePipeline | Không có tính năng transcode | S3 | Wavelength (sai use case) | Sai công cụ cho cả 2 phần |

#### Quy tắc nhớ cho thi

- **"Transcode video MP4 → HLS/khác, cost-effective, HA"** → **AWS Elemental MediaConvert** (dịch vụ kế thừa Elastic Transcoder)
- **Lưu video/static asset để CloudFront phân phối toàn cầu** → **S3**, không phải EBS/EC2
- **Jenkins/SQS/EC2 Auto Scaling tự dựng pipeline xử lý file** → dấu hiệu DIY, kiểm tra xem AWS có managed service tương đương không
- **AWS Wavelength** chỉ dùng khi đề nói rõ 5G / ultra-low-latency edge, không phải cho remote worker thông thường

### TD explanation

AWS Elemental MediaConvert is a file-based video transcoding service with broadcast-grade features. It provides a comprehensive suite of advanced transcoding features with on-demand rates. It allows you to easily create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale. The service combines advanced video and audio capabilities with a simple web services interface and pay-as-you-go pricing. With AWS Elemental MediaConvert, you can focus on delivering compelling media experiences without having to worry about the complexity of building and operating your own video processing infrastructure. MediaConvert is optimized to improve scalability, which allows you to process more files in parallel.

Amazon Elastic Transcoder uses pipelines to manage transcoding jobs. When you create a job, you specify the pipeline that you want to submit the job to. Pipelines are closely tied to an S3 bucket that you specify. Queues in AWS Elemental MediaConvert are similar to pipelines. The number of concurrent jobs processed in a given queue is determined based on the number of queues in your account. However, one of the key differences is that queues are not tied to a specific S3 bucket. This means that you can submit jobs that reference input files in different S3 buckets to the same queue. In Elastic Transcoder, you select the playlist version upon job creation. In MediaConvert, the HLS version will change as you enable features that require a specific version.

Therefore, the correct answer is: Create a queue in AWS Elemental MediaConvert to transcode the high-resolution MP4 videos into the HLS format. Store the transcoded videos on an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Create an Amazon CloudFront distribution and set the S3 bucket as the origin to serve the transcoded videos. AWS Elemental MediaConvert is a new file-based video transcoding service aimed to replace Amazon Elastic Transcoder. Additionally, storing the transcoded videos on S3 buckets is highly durable and cost-effective, as you don’t have to pay for EC2 instance costs.

The option that says: Create a Jenkins pipeline to transcode the high-resolution MP4 videos. Use an SQS queue to distribute the transcoding job to a set of Amazon EC2 instances in an Auto Scaling group that scales based on the length of the queue. Store the transcoded videos on EBS volumes and configure automated snapshots to back up the files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos is incorrect. AWS has managed services to automate video transcoding for you. Additionally, using large EBS volumes to store the transcoded videos is not very cost-effective compared to using an S3 bucket.

The option that says: Create a pipeline on Amazon Elastic Transcoder to transcode the high-resolution MP4 videos into the HLS format. Host the transcoded videos on large EBS volumes attached to Amazon EC2 instances. Configure automated EBS snapshots to back up the video files every few days. Create an Amazon CloudFront distribution and set the EC2 instances as the origin to serve the transcoded videos is incorrect. This may be possible, however, using large EBS volumes to store the transcoded videos is not very cost-effective compared to using an S3 bucket. Additionally, the performance of the EC2 instance may vary depending on the traffic load.

The option that says: Create a pipeline in AWS CodePipeline with stages that transcode the high-resolution MP4 videos into the HLS format and send the transcoded videos to an Amazon S3 bucket. Configure Lifecycle Management on the bucket to move the original videos to Amazon S3 Glacier Instant Retrieval. Then, set up an endpoint in AWS Wavelength and configure it to serve the transcoded videos from the S3 bucket is incorrect. AWS CodePipeline is primarily designed for CI/CD pipelines to deploy new application versions. You can’t directly create a stage that will transcode videos to a specific format. Moreover, AWS Wavelength is designed to provide ultra-low latency for applications on 5G networks. It’s ideal for applications that require minimal latency over mobile networks. However, in your scenario, the employees are located in various countries and may not necessarily be using 5G networks.

 

References:

https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/

https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-s3-glacier-storage-class-amazon-s3-glacier-flexible-retrieval/

 

Check out this Amazon CloudFront Cheat Sheet:

https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q73"></a>

## Q73

A company has a marketing service that schedules and posts content on a social media platform. The service currently runs on a collection of Amazon EC2 instances within an Auto Scaling group behind an Application Load Balancer (ALB). This ALB responds to webhook calls from the social media platform when specific events occur, such as mentions, shares, or specific hashtag uses. The company wants to migrate this service to a serverless architecture to lessen administrative overhead.

Which action would be the most operationally efficient way to meet the requirements?

- **A.** Run the service using AWS Lambda. Generate a Lambda Function URL for each webhook. Configure the platform to send webhook calls to the function URLs.
- **B.** Use AWS Lambda to run the service. Create a single AWS AppSync GraphQL API endpoint and connect it to the Lambda functions. Configure the platform to send webhook calls to the AppSync endpoint.
- **C.** Run the service using AWS Lambda. Create an Amazon Gateway REST API that uses proxy integration with AWS Lambda. Create an API resource for each webhook. Configure the platform to send webhook calls to the REST API endpoint.
- **D.** Replace the Amazon EC2 instances with AWS Fargate tasks. Create an Amazon Gateway HTTP API and integrate it with the Application Load Balancer. Configure the platform to send webhook calls to the HTTP API endpoint.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** webhooks; migrate to serverless; most operationally efficient

🪤 **Your trap:** Fargate + HTTP API + ALB = over-engineered

🧠 **Rule:** Simple HTTPS endpoint for a function → Lambda Function URL.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Marketing service hiện tại:
    EC2 fleet (Auto Scaling group) sau ALB
    → nhận webhook từ social media platform (mention, share, hashtag...)

Yêu cầu: migrate sang SERVERLESS
    → giảm administrative overhead
    → chọn kiến trúc "most operationally efficient"
```

Đáp án đúng: **A (Lambda Function URL cho mỗi webhook)**. Anh chọn **D (Fargate + API Gateway HTTP API + ALB)** — đây là kiểu "serverless nửa vời", vẫn giữ nhiều thành phần cũ và phức tạp hơn mức cần thiết.

#### Vì sao D sai — vẫn còn container hóa + nhiều tầng thừa

```
D: EC2 → Fargate (vẫn phải containerize app)
       → API Gateway HTTP API
       → tích hợp với ALB
       → ALB → Fargate tasks

Vấn đề:
  - Phải đóng gói ứng dụng thành container → thêm một lớp dev/ops
  - Vẫn giữ ALB (một thành phần của kiến trúc cũ) làm trung gian
  - Nhiều tầng hơn cần thiết cho việc đơn giản là "nhận webhook → xử lý"
```

Đề hỏi thẳng "most operationally efficient" — Fargate tuy serverless-ish (không cần quản lý server) nhưng vẫn đòi hỏi containerize và duy trì ALB, không phải lựa chọn tối giản nhất so với chuyển thẳng sang Lambda.

#### Vì sao A đúng — Lambda Function URL là lựa chọn tối giản nhất

```
Lambda Function URL: HTTP(S) endpoint gắn trực tiếp vào 1 Lambda function
    → không cần API Gateway, không cần ALB, không cần containerize
    → mỗi webhook → 1 Lambda function → 1 Function URL riêng
    → social platform gọi thẳng function URL khi có event
```

Vì webhook chỉ cần một endpoint HTTPS đơn giản để nhận call và xử lý — không cần các tính năng nâng cao của API Gateway (throttling phức tạp, request validation, nhiều stage...) hay GraphQL của AppSync. Function URL loại bỏ hoàn toàn tầng trung gian, giảm latency và giảm overhead vận hành — đúng tinh thần "eliminate the need for intermediaries" mà TD explanation nhấn mạnh.

#### Vì sao B và C sai

- **B (AppSync GraphQL)**: AppSync dùng cho ứng dụng client cần query GraphQL linh hoạt, không phù hợp để nhận webhook đơn giản — thêm phức tạp không cần thiết cho use case này.
- **C (API Gateway REST API + proxy integration)**: về mặt kỹ thuật chạy được, nhưng tạo API resource riêng cho từng webhook rồi qua REST API là dư thừa khi có thể trigger Lambda trực tiếp bằng Function URL — REST API phù hợp hơn khi cần các tính năng quản lý API đầy đủ (không phải trường hợp này).

| Đáp án | Cần containerize? | Cần API Gateway/AppSync? | Cần giữ ALB? | Mức phức tạp |
|---|---|---|---|---|
| **A. Lambda Function URL** | Không | Không | Không | Thấp nhất |
| B. Lambda + AppSync | Không | Có (AppSync GraphQL) | Không | Cao — sai use case |
| C. Lambda + API Gateway REST | Không | Có | Không | Cao hơn cần thiết |
| D. Fargate + HTTP API + ALB | Có | Có | Có | Cao nhất |

#### Quy tắc nhớ cho thi

- **"Webhook đơn giản, chỉ cần 1 HTTPS endpoint gọi 1 Lambda"** → **Lambda Function URL**, không cần API Gateway
- **"Most operationally efficient" / "least overhead"** → ưu tiên phương án ít thành phần nhất vẫn đáp ứng yêu cầu
- **Fargate** vẫn đòi hỏi containerize app → không phải lựa chọn "serverless tối giản nhất" khi Lambda thuần đã đủ
- **AppSync** chỉ chọn khi đề thực sự cần GraphQL cho client, không phải cho webhook nhận event một chiều
- **API Gateway (REST/HTTP API)** cần khi có nhiều route phức tạp, cần throttling/API management thật sự — nếu chỉ để "trigger Lambda", Function URL đơn giản hơn

### TD explanation

Lambda function URLs are HTTP(S) endpoints dedicated to your Lambda function. You can easily create and set up a function URL using the Lambda console or API. Once created, Lambda generates a unique URL endpoint for your use.

Function URLs are dual stack-enabled, supporting IPv4 and IPv6. After you configure a function URL for your function, you can invoke your function through its HTTP(S) endpoint via a web browser, curl, Postman, or any HTTP client.

In the scenario, exposing Lambda functions directly using function URLS eliminates the need for intermediaries like Amazon API Gateway. This approach significantly simplifies the architecture, reduces latency, and lessens administrative overhead. Each webhook can be configured to send calls to specific Lambda function URLs, providing a response mechanism for various social media events.

Hence, the correct answer is: Run the service using AWS Lambda. Generate a Lambda Function URL for each webhook. Configure the platform to send webhook calls to the function URLs.

The option that says: Use AWS Lambda to run the service. Create a single AWS AppSync GraphQL API endpoint and connect it to the Lambda functions. Configure the platform to send webhook calls to the AppSync endpoint is incorrect. AWS AppSync is a just managed service that uses GraphQL to make it easy for applications to get exactly the data they need. While you can use it with Lambda, this solution is not as straightforward as directly triggering Lambda functions using function URLs. Using AppSync might introduce unnecessary complexity for this use case which is about responding to webhook calls from a social media platform, not handling GraphQL queries from a client application.

The option that says: Replace the Amazon EC2 instances with AWS Fargate tasks. Create an Amazon Gateway HTTP API and integrate it with the Application Load Balancer. Configure the platform to send webhook calls to the HTTP API endpoint is incorrect. While AWS Fargate is a serverless compute engine for containers, it wouldn’t be the most efficient choice in the scenario. Using Fargate would require you to containerize the application, which adds an additional layer of development and management overhead

The option that says: Run the service using AWS Lambda. Create an Amazon Gateway REST API that uses proxy integration with AWS Lambda. Create an API resource for each webhook. Configure the platform to send webhook calls to the REST API endpoint is incorrect. Although this option could work, it introduces additional complexity by using Amazon API Gateway as an intermediary. In this scenario, a fully-fledged REST API is not necessary. Instead of creating an API resource for each webhook, it would be simpler and more efficient to directly trigger specific AWS Lambda functions thru Lambda function URLs.

 

References:

https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html

https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html

 

Check out this AWS Lambda Cheat Sheet:

https://tutorialsdojo.com/aws-lambda/

</details>

<a id="q24"></a>

## Q24

A company is planning to use Amazon WorkSpaces along with virtual desktop infrastructure (VDI) to replace their outdated workstations. The employees use these workstations to access proprietary software that handles sensitive financial data. The company’s security policy mandates that access to this software must be limited to only the corporate headquarters and its satellite offices. The corporation is also considering opening a new satellite office in the next quarter.

Which solution would provide the highest operational efficiency while meeting these requirements?

- **A.** Establish a connection using Amazon WorkSpaces with a WorkSpaces directory and AWS Direct Connect for secure access to the proprietary software from the corporate headquarters and its satellite offices.
- **B.** Utilize Windows Firewall with a custom WorkSpace image to restrict access to the proprietary software from the corporate headquarters and its satellite offices.
- **C.** Configure Amazon WorkSpaces with a WorkSpaces directory and apply IP access control group rules to restrict access to the proprietary software from the corporate headquarters and its satellite offices.
- **D.** Deploy Amazon EC2 instances with Elastic IP addresses for each employee, and restrict access to the proprietary software to these IP addresses.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** WorkSpaces; restrict to HQ + satellite offices; new office soon; operational efficiency

🪤 **Your trap:** Windows Firewall in custom image = per-WorkSpace management

🧠 **Rule:** Restrict WorkSpaces by source network → WorkSpaces IP access control groups.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Amazon WorkSpaces (VDI) thay thế workstation cũ
    → truy cập phần mềm sở hữu độc quyền chứa dữ liệu tài chính nhạy cảm

Security policy:
    → chỉ cho phép truy cập từ Corporate HQ + Satellite Offices
    → sắp mở thêm 1 satellite office mới trong quý tới

Yêu cầu: giải pháp có OPERATIONAL EFFICIENCY cao nhất
```

Đáp án đúng: **C (WorkSpaces directory + IP access control group rules)**. Anh chọn **B (Windows Firewall trong custom WorkSpace image)** — giải pháp per-instance, không phải giải pháp quản lý tập trung.

#### Vì sao B sai — quản lý theo từng WorkSpace, không theo network

```
Windows Firewall trong custom image:
    → rule cấu hình CỨNG trong image
    → mỗi khi cần thêm/bớt văn phòng (ví dụ satellite office mới)
       → phải sửa lại image, rebuild, redeploy cho từng WorkSpace
    → Windows Firewall lọc theo địa chỉ/port ở tầng OS,
       KHÔNG có khái niệm "vị trí địa lý / văn phòng nào" một cách tập trung
```

Đề bài nói rõ công ty **sắp mở thêm satellite office mới** — đây là tín hiệu quan trọng: giải pháp đúng phải cho phép **cập nhật một chỗ** để áp dụng ngay cho toàn bộ WorkSpaces, không phải sửa từng image/từng máy. Windows Firewall trong custom image thất bại chính ở tiêu chí "operational efficiency" khi công ty mở rộng.

#### Vì sao C đúng — kiểm soát tập trung theo network, gắn 1 lần vào directory

```
WorkSpaces IP access control group
    → định nghĩa các dải CIDR được phép (HQ, satellite office 1, 2...)
    → gắn (associate) group này với WorkSpaces directory
    → MỌI WorkSpace trong directory đó tự động áp dụng rule

Khi mở satellite office mới:
    → chỉ cần THÊM 1 rule CIDR mới vào access control group
    → không cần đụng tới từng WorkSpace, không cần rebuild image
```

Đây chính là dịch vụ "virtual firewall" tích hợp sẵn của WorkSpaces, thiết kế đúng cho việc giới hạn truy cập theo mạng nguồn (trusted network) một cách tập trung — vừa đáp ứng yêu cầu bảo mật vừa tối ưu vận hành khi mở rộng văn phòng.

#### Vì sao A và D sai

- **A (Direct Connect)**: Direct Connect chỉ tạo kết nối mạng riêng/ổn định từ HQ đến AWS, **không tự nó giới hạn truy cập chỉ từ HQ + satellite office** — vẫn cần cấu hình thêm (ví dụ chính IP access control group) để thực sự enforce việc giới hạn nguồn truy cập. Dùng Direct Connect một mình không giải quyết đúng yêu cầu.
- **D (EC2 + Elastic IP riêng cho từng nhân viên)**: đi ngược lại chính định hướng công ty đã chọn (WorkSpaces/VDI), lại phải quản lý EC2 + EIP theo từng người — cực kỳ tốn kém và không scalable, sai cả về kiến trúc lẫn hiệu quả vận hành.

| Đáp án | Cơ chế | Cập nhật khi thêm office mới | Tập trung? |
|---|---|---|---|
| **C. IP access control group** | Virtual firewall gắn vào directory | Thêm 1 CIDR rule | Có |
| B. Windows Firewall trong image | Rule cứng trong OS image | Rebuild/redeploy image | Không |
| A. Direct Connect | Kết nối mạng riêng | Không tự giới hạn truy cập | Không đủ |
| D. EC2 + EIP mỗi nhân viên | Hạ tầng riêng lẻ | Quản lý từng instance | Không |

#### Lưu ý thực tế

- Mỗi directory WorkSpaces có sẵn 1 **default IP access control group** cho phép truy cập từ bất kỳ đâu; khi gắn 1 group tùy chỉnh vào directory, default group sẽ bị gỡ (disassociate) — đúng cơ chế để "khóa" truy cập theo whitelist.
- Một access control group có thể gắn với nhiều directory, và một directory có thể gắn tối đa 25 group — đủ linh hoạt cho nhiều văn phòng khác nhau.

#### Quy tắc nhớ cho thi

- **"Giới hạn WorkSpaces truy cập theo network nguồn (HQ + branch offices)"** → **WorkSpaces IP access control groups**
- **"Sắp mở rộng thêm địa điểm"** → ưu tiên giải pháp cấu hình tập trung 1 chỗ, tránh giải pháp phải sửa từng máy/image
- **Windows Firewall / cấu hình OS-level trong image** → luôn là dấu hiệu quản lý phân tán, kém operational efficiency khi cần scale
- **Direct Connect** giải quyết bài toán kết nối mạng riêng, không tự động giải quyết bài toán kiểm soát truy cập theo nguồn

### TD explanation

Amazon WorkSpaces allows you to control which IP addresses your WorkSpaces can be accessed from. By using IP address-based control groups, you can define and manage groups of trusted IP addresses and only allow users to access their WorkSpaces when connected to a trusted network.

An IP access control group acts as a virtual firewall that controls the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can associate each IP access control group with one or more directories. You can create up to 100 IP access control groups per Region per AWS account. However, you can only associate up to 25 IP access control groups with a single directory.

Each directory is associated with a default IP access control group, which includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory. If you don’t associate an IP access control group with your directory, the default group is used. If you associate an IP access control group with a directory, the default IP access control group is disassociated.

Hence, the correct answer is: Configure Amazon WorkSpaces with a WorkSpaces directory and apply IP access control group rules to restrict access to the proprietary software from the corporate headquarters and its satellite offices.

The option that says: Deploy Amazon EC2 instances with Elastic IP addresses for each employee, and restrict access to the proprietary software to these IP addresses is incorrect because while it’s possible to use Amazon EC2 instances with Elastic IP addresses, this approach doesn’t align with the company’s plan to use Amazon WorkSpaces and VDI. Moreover, managing individual EC2 instances for each employee can be operationally inefficient and costly.

The option that says: Establish a connection using Amazon WorkSpaces with a WorkSpaces directory and AWS Direct Connect for secure access to the proprietary software from the corporate headquarters and its satellite offices is incorrect. Although AWS Direct Connect provides a dedicated network connection from the corporate headquarters to AWS, it doesn’t inherently limit access to the proprietary software to only the corporate headquarters and its satellite offices. Additional configuration would be needed to enforce this restriction, which could complicate the setup and management.

The option that says: Utilize Windows Firewall with a custom WorkSpace image to restrict access to the proprietary software from the corporate headquarters and its satellite offices is incorrect because while Windows Firewall can help secure a system, it’s not designed to restrict access based on geographic location. Moreover, managing firewall rules on individual WorkSpaces can be operationally complex and doesn’t provide a centralized way to enforce the company’s security policy.

 

References:

https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html

https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html

 

Check out this Amazon WorkSpaces Cheat Sheet:

https://tutorialsdojo.com/amazon-workspaces/

</details>

---

# Group B — Multi-account governance (9)

<a id="q16"></a>

## Q16

A multinational company has hundreds of AWS accounts that are managed under one AWS Organization. The company has 25 technical teams that are designated with their own Organization Unit (OU) in the AWS Organizations. Each team manages several AWS accounts to be used for their projects. The upper management wants a solution that enables each Team Leader to examine the breakdown of AWS resource charges across all the AWS accounts under their OU.

Which of the following options should the solutions architect implement to meet this requirement?

- **A.** Using AWS Resource Access Manager, generate an AWS Cost and Usage Report (CUR) for each OU. Upload the report in Amazon QuickSight and create the dashboard. Share the dashboard with each OU Team Lead.
- **B.** Using AWS Systems Manager in the management account, generate an AWS Cost and Usage Report (CUR) for each OU. Create a dashboard on AWS Systems Manager OpsCenter to visualize the report. Share the dashboard with each OU Team Lead.
- **C.** For each member account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in AWS Systems Manager Explorer and create a dashboard. Allow each Team Leader to view the dashboards.
- **D.** From the management account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in Amazon QuickSight and create a dashboard. Allow each Team Leader to view the dashboard.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** hundreds of accounts; OU per team; team lead sees charges across OU accounts

🪤 **Your trap:** RAM cannot generate CUR

🧠 **Rule:** Org-wide cost breakdown → CUR from management account + QuickSight dashboard.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organization
 ├─ OU "Team 1"  ─ nhiều accounts
 ├─ OU "Team 2"  ─ nhiều accounts
 ├─ ... (25 OU/teams, hàng trăm account)

Mỗi Team Leader cần xem: breakdown chi phí AWS
                          CHỈ trong OU của mình
```

Đáp án đúng: **D** (tạo CUR ở management account + QuickSight dashboard). Anh chọn **A** (RAM tạo CUR).

#### Vì sao A sai — RAM không liên quan đến billing

**AWS Resource Access Manager (RAM)** chỉ dùng để **share resource** giữa các account (Transit Gateway, subnet, License Manager configuration, Route 53 Resolver rules, Aurora cluster…). RAM **không có khả năng tạo Cost and Usage Report**. Đây là bẫy kinh điển: đề nhắc "Organization" + "nhiều account" khiến người học phản xạ nghĩ tới RAM, nhưng RAM chỉ share resource kỹ thuật, không đụng tới billing/cost data.

#### Vì sao D đúng

```
Management account (root của Organization)
    │
    ├─ Bật Cost and Usage Report (CUR)
    │     → CUR gom dữ liệu billing của TẤT CẢ account thành viên
    │     (từ 12/2020, CUR hỗ trợ cả linked/member account)
    │
    ├─ CUR delivery → S3 bucket
    │
    └─ Import vào Amazon QuickSight → tạo dashboard
            → filter/breakdown theo OU hoặc account
            → share dashboard cho từng Team Leader
```

CUR là báo cáo chi phí chi tiết nhất của AWS (product code, usage type, operation, Reserved Instance, Savings Plan…), và **chỉ management account (hoặc account có quyền phù hợp) mới nên tạo một CUR duy nhất cho toàn Organization** — tránh phải tạo CUR riêng lẻ cho từng account.

#### Vì sao các phương án khác sai

- **B — Systems Manager + OpsCenter:** Systems Manager **không tạo được CUR**. OpsCenter cũng không hỗ trợ import CUR để visualize. Sai hoàn toàn về mặt dịch vụ.
- **C — Tạo CUR riêng cho từng member account + Systems Manager Explorer:** Về mặt kỹ thuật có thể tạo CUR ở từng account, nhưng **không tối ưu** — Team Leader phải xem nhiều dashboard rời rạc thay vì một dashboard tổng hợp theo OU → tăng operational overhead không cần thiết. Ngoài ra, **Systems Manager Explorer chỉ báo cáo tình trạng resource (EC2, RDS…)**, không thu thập dữ liệu cost/billing.

| Phương án | Vấn đề |
|---|---|
| A | RAM không tạo được CUR |
| B | Systems Manager không tạo CUR, OpsCenter không import CUR |
| C | Đúng hướng nhưng tạo CUR lẻ tẻ từng account → thừa thao tác |
| **D** | CUR từ management account (gồm toàn bộ member accounts) + QuickSight |

#### Quy tắc nhớ cho thi

- **"cost breakdown toàn Organization / theo OU"** → CUR tạo từ **management account**, không phải từng member account
- **"visualize CUR thành dashboard"** → luôn là **Amazon QuickSight**, không phải Systems Manager/OpsCenter/Explorer
- **RAM** → chỉ share resource kỹ thuật (TGW, subnet, License Manager, Resolver rules, Aurora cluster…), **không liên quan billing**
- Thấy "Systems Manager" đi kèm "cost/billing" → gần như luôn là đáp án nhiễu, vì Systems Manager là công cụ operations, không phải billing

### TD explanation

The AWS Cost & Usage Report contains the most comprehensive set of AWS cost and usage data available, including additional metadata about AWS services, pricing, credit, fees, taxes, discounts, cost categories, Reserved Instances, and Savings Plans. The AWS Cost & Usage Report (CUR) itemizes usage at the account or Organization level by product code, usage type, and operation. With the right access, users can access CUR at management and member account levels, which saves management account holders from having to generate CUR reports for member accounts.

AWS delivers the AWS Cost & Usage Report to whichever Amazon Simple Storage Service (S3) bucket you specify during setup and updates the reports at least once per day. You can configure your Cost & Usage Reports to integrate with Amazon Athena. When you integrate with Redshift, all the necessary commands are provided to you in the RedshiftCommands.sql file that is stored alongside your manifest file in S3 and in the Redshift fileHelper file in the Billing and Cost Management console. Your AWS Cost & Usage Report can also be integrated directly with Amazon QuickSight.

Therefore, the correct answer is: From the management account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in Amazon QuickSight and create a dashboard. Allow each Team Leader to view the dashboard. The management account can create a dashboard based on the CUR to allow the team leaders to visualize the AWS charges under their OU.

The option that says: Using AWS Resource Access Manager, generate an AWS Cost and Usage Report (CUR) for each OU. Upload the report in Amazon QuickSight and create the dashboard. Share the dashboard with each OU Team Lead is incorrect. AWS Resources Access Manager (RAM) is used to share AWS resources such as transit gateways, subnets, AWS License Manager license configurations, and Amazon Route 53 Resolver rules. It can’t be used to generate an AWS Cost and Usage Report.

The option that says: For each member account of the AWS Organizations, create an AWS Cost and Usage Report (CUR). Upload the report in AWS Systems Manager Explorer and create a dashboard. Allow each Team Leader to view the dashboards is incorrect. Using a member account may be possible but is not optimal because there will be a CUR dashboard for each account, and the team leader will have to view them individually. You have to create a CUR for each management account instead to avoid this unnecessary operational overhead. Moreover, the AWS Systems Manager Explorer is a customizable operations dashboard that reports information about your actual AWS resources (e.g., Amazon EC2, Amazon RDS, etc.). This service does not gather cost and management information of the member accounts within your AWS Organization.

The option that says: Using AWS Systems Manager in the management account, generate an AWS Cost and Usage Report (CUR) for each OU. Create a dashboard on AWS Systems Manager OpsCenter to visualize the report. Share the dashboard with each OU Team Lead is incorrect. You can’t generate an AWS Cost and Usage Report in AWS Systems Manager. Additionally, the Systems Manager OpsCenter does not support importing CUR. A better solution for this is to use an Amazon QuickSight dashboard instead.

 

References:

https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html

https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/

https://aws.amazon.com/about-aws/whats-new/2020/12/cost-and-usage-report-now-available-to-member-linked-accounts/

 

Check out these AWS Organizations and AWS Billing and Cost Management Cheat Sheets:

https://tutorialsdojo.com/aws-organizations/

https://tutorialsdojo.com/aws-billing-and-cost-management/

</details>

<a id="q29"></a>

## Q29

An enterprise uses AWS Organizations to manage hundreds of AWS accounts. Each division falls under a corresponding Organizational Unit (OU) with different permissions for accessing AWS services.

The analytics division has a data analysis tool within each VPC where the enterprise has its workloads running. This tool operates on EC2 instances and runs at least once a week. The collected data is sent to an AWS account dedicated to the analytics division and stored in an Amazon Redshift data warehouse.

The accounting division needs to determine how much it costs to run the analysis tool, so they can bill the analytics division accordingly. All analytics-related resources are already tagged using the AWS tag "expenseUnit": "analytics".

Which set of actions would meet the requirements?

- **A.** Enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console of the management account. Use AWS Cost and Usage Reports to generate the monthly billing report to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics".
- **B.** In the AWS account of the accounting division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. In the management account, generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics".
- **C.** Create an AWS Resource group of resources tagged with the "expenseUnit": "analytics" in the management account. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics".
- **D.** In the AWS account of the analytics division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics".

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** bill analytics division by tag 'expenseUnit: analytics'

🪤 **Your trap:** Resource Groups ≠ billing tool

🧠 **Rule:** Cost by tag → activate user-defined cost allocation tag in mgmt account + CUR tag breakdown.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organization
 ├─ Analytics division account  (chạy tool, resource tag "expenseUnit": "analytics")
 ├─ Accounting division account (cần BIẾT chi phí để bill lại cho Analytics)
 └─ Management account (root)

Yêu cầu: Accounting tính được chi phí chạy tool của Analytics
         dựa trên tag "expenseUnit": "analytics"
```

Đáp án đúng: **A** — bật **cost allocation tag ở management account** + CUR + filter theo tag. Anh chọn **C** (Resource Group + Athena).

#### Vì sao A đúng

```
Management account
    │
    ├─ Billing and Cost Management console
    │     → Cost allocation tags
    │     → Activate tag "expenseUnit": "analytics"   (user-defined tag)
    │
    ├─ AWS Cost and Usage Reports (CUR)
    │     → monthly billing report → S3 bucket
    │     → CUR có cột riêng cho mỗi active cost allocation tag
    │
    └─ Filter CUR theo tag breakdown "expenseUnit": "analytics"
            → ra đúng tổng chi phí của Analytics division
```

Điểm mấu chốt: **chỉ management account (hoặc single account không thuộc Organization) mới có quyền truy cập Cost Allocation Tags Manager** trong Billing and Cost Management console. Vì đây là bài toán cross-account (resource của Analytics account cần bill sang Accounting account), chỉ management account mới có visibility toàn Organization để làm việc này.

#### Vì sao anh chọn C sai

**AWS Resource Groups không phải công cụ billing.** Resource Group chỉ dùng để **quản lý và tự động hóa tác vụ** trên một tập hợp resource được gom theo tag (ví dụ: chạy SSM Automation hàng loạt, xem CloudWatch dashboard theo group…). Nó **không tính toán chi phí**. Việc dùng Athena để "tính tổng cost" trên dữ liệu CUR về mặt kỹ thuật khả thi (CUR có thể integrate Athena), nhưng bước Resource Group ở đây là thừa và sai bản chất — đề chỉ cần filter tag breakdown trực tiếp trên CUR, không cần dựng Resource Group trước.

#### Vì sao B, D sai

- **B — bật tag ở account Accounting:** sai vì Accounting không sở hữu resource được tag, activate tag ở đó vô nghĩa. Chỉ management account có quyền activate cost allocation tag ở cấp Organization.
- **D — bật tag ở account Analytics:** cùng lỗi — activate tag chỉ ảnh hưởng phạm vi account đó, không kéo được dữ liệu billing tổng hợp toàn Organization mà CUR ở management account cung cấp.

| Phương án | Vấn đề |
|---|---|
| **A** | Đúng: activate tag ở management account + CUR filter tag |
| B | Activate tag ở account Accounting — sai account |
| C | Resource Group không phải công cụ billing, thừa bước |
| D | Activate tag ở account Analytics — chỉ management account mới đủ quyền/scope |

#### Quy tắc nhớ cho thi

- **Cost allocation tag chỉ activate được ở management account** (hoặc standalone account) — không phải ở member account
- **"bill chi phí resource theo tag, cross-account trong Organization"** → activate tag ở management account + CUR + tag breakdown
- **Resource Groups** → công cụ operations/automation, **không phải** billing tool
- **Athena trên CUR** → hợp lệ về kỹ thuật (CUR hỗ trợ Athena integration) nhưng không phải bước bắt buộc khi đề chỉ cần "filter theo tag"

### TD explanation

A tag is a label that you or AWS assigns to an AWS resource. Each tag consists of a key and a value. For each resource, each tag key must be unique, and each tag key can have only one value. You can use tags to organize your resources and cost allocation tags to track your AWS costs on a detailed level.

After you or AWS applies tags to your AWS resources (such as Amazon EC2 instances or Amazon S3 buckets) and you activate the tags in the Billing and Cost Management console, AWS generates a cost allocation report as a comma-separated value (CSV file) with your usage and costs grouped by your active tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services.

In the scenario, the organization is using AWS Organizations to manage multiple accounts, necessitating cross-account cost calculation. The management account, with its organization-wide visibility, is best suited for this task. By enabling the "expenseUnit": "analytics" cost allocation tag at this level, all analytics-related resources across accounts can be tracked. AWS Cost and Usage Reports can then be generated from the management account, with data filtered by the tag, yielding the precise cost for running the analysis tool.

Hence, the correct answer is: Enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console of the management account. Use AWS Cost and Usage Reports to generate the monthly billing report to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics".

Only a management account in an organization and single accounts that aren’t members of an organization have access to the cost allocation tags manager in the Billing and Cost Management console. Hence, the following options are both incorrect:

– In the AWS account of the analytics division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics".

– In the AWS account of the accounting division, enable the user-defined "expenseUnit": "analytics" cost allocation tag on the Billing and Cost Management console. In the management account, generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Filter the data using tag breakdown to get the total cost associated with the resources tagged with "expenseUnit": "analytics".

The option that says: Create an AWS Resource group of resources tagged with the "expenseUnit": "analytics" in the management account. Generate the monthly billing report using AWS Cost and Usage Reports and save it to an S3 bucket. Use Amazon Athena to calculate the total cost associated with the resources tagged with "expenseUnit": "analytics" is incorrect. AWS Resource Groups are typically used to manage and automate tasks on a large collection of AWS resources at once. They are not primarily used for cost calculation purposes. It is more straightforward and accurate to use the AWS Cost and Usage Reports, which provide detailed cost information and allow filtering by tags.

 

References:

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html

https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-allocation-blog-series-2-aws-generated-vs-user-defined-cost-allocation-tag/

 

Check out this AWS Billing and Cost Management Cheat sheet:

https://tutorialsdojo.com/aws-billing-and-cost-management/

</details>

<a id="q19"></a>

## Q19

A company has hundreds of AWS accounts in an organization in AWS Organizations. The accounts are associated with one of the three Organization Units (OU): PROD, DEV, and UAT. The company uses the vpc-sg-open-only-to-authorized-ports AWS Config managed rule, deployed as part of a Config conformance pack, to determine if a security group that allows incoming traffic at ‘0.0.0.0/0’ is created on any of the OUs. An Amazon SNS topic is configured to send email alerts to the security team when a security group is flagged as non-compliant.

There are critical security groups that must not be modified by users. The security team wants to prevent accounts in the PROD OU from altering the rules of these security groups.

Which solution would meet the requirements?

- **A.** Apply a remediation action to the Config rule using the AWSConfigRemediation-RemoveUnrestrictedSourceIngressRules AWS System Manager Automation document.
- **B.** Tag the security groups using the key value ‘scope:private’. Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:ResourceTag/scope”: “private” condition key. Attach the SCP to the PROD OU.
- **C.** Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:SourceIp”: “0.0.0.0/0” condition key. Attach the SCP to the PROD OU.
- **D.** Create an AWS Lambda function that calls the RevokeSecurityGroupIngress on security groups that have an inbound rule allowing traffic from 0.0.0.0/0. Subscribe the Lambda function to the SNS topic.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** critical SGs must not be modified; only PROD OU

🪤 **Your trap:** aws:SourceIp condition doesn't target specific resources

🧠 **Rule:** Protect specific resources → tag them + SCP deny with aws:ResourceTag condition, attach to OU.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organization
 ├─ OU: PROD  ← chỉ OU này bị hạn chế
 ├─ OU: DEV
 └─ OU: UAT

Config rule "vpc-sg-open-only-to-authorized-ports"
    → phát hiện SG mở 0.0.0.0/0 → SNS alert (REACTIVE, sau khi đã tạo)

Yêu cầu MỚI: một số SG "critical" TUYỆT ĐỐI không được users
             trong PROD OU sửa đổi rule (PROACTIVE, ngăn trước)
```

Đáp án đúng: **B** (tag SG + SCP deny với `aws:ResourceTag` condition, attach vào PROD OU). Anh chọn **C** (SCP deny với `aws:SourceIp` condition).

#### Vì sao B đúng

```
Bước 1: Tag các SG "critical"     → key/value: scope:private
Bước 2: Viết SCP
    Effect: Deny
    Action: ec2:AuthorizeSecurityGroup*   (Ingress/Egress)
    Condition:
        "aws:ResourceTag/scope": "private"
Bước 3: Attach SCP vào OU "PROD"
```

SCP là công cụ **chặn ở tầng permission, trước khi hành động xảy ra** (không phải phát hiện sau). Bằng cách tag đúng các SG cần bảo vệ và dùng condition key `aws:ResourceTag/<tag-key>`, SCP chỉ target **chính xác những SG được tag** — không ảnh hưởng SG khác trong cùng OU, và chỉ áp dụng cho PROD OU vì SCP được attach ở đó.

#### Vì sao anh chọn C sai

`aws:SourceIp` là condition key kiểm tra **địa chỉ IP mà request gọi API xuất phát từ đó** (tức IP của người/hệ thống gọi `AuthorizeSecurityGroupIngress`), **không phải** IP CIDR được cấu hình trong rule của security group. Vì vậy SCP này không hề nhắm đúng vào "SG có rule cho phép traffic từ 0.0.0.0/0" như đề yêu cầu — nó chỉ chặn ai gọi API mà đến từ chính IP `0.0.0.0/0` (thực tế điều kiện này gần như luôn đúng/luôn sai một cách vô nghĩa vì không match đúng ngữ cảnh). Nói cách khác: **C dùng sai loại condition key** — cần match theo **resource/tag**, không phải theo **source IP của caller**. Ngoài ra C cũng không có cơ chế target "chỉ những SG cụ thể" — nó áp dụng chung chung, không phân biệt SG nào là "critical".

#### Vì sao A, D sai

- **A — Remediation qua SSM Automation document:** đây vẫn là hành động **reactive** — Config rule phát hiện SG không tuân thủ SAU KHI nó đã được tạo, rồi mới remediate. Đề yêu cầu **ngăn chặn (prevent)** việc sửa đổi ngay từ đầu, không phải "phát hiện rồi sửa".
- **D — Lambda gọi RevokeSecurityGroupIngress qua SNS trigger:** cùng bản chất reactive như A — SG vẫn bị mở trước, Lambda chỉ dọn dẹp sau. Không thỏa yêu cầu "must not be modified".

| Phương án | Cơ chế | Proactive hay Reactive | Target đúng SG cụ thể? |
|---|---|---|---|
| **B** | SCP deny + `aws:ResourceTag` | Proactive | Có (nhờ tag) |
| C | SCP deny + `aws:SourceIp` | Proactive nhưng sai condition | Không |
| A | Config remediation (SSM Automation) | Reactive | Không |
| D | Lambda + SNS | Reactive | Không |

#### Quy tắc nhớ cho thi

- **"must not be modified" / "prevent"** → cần cơ chế **chặn trước** (SCP/IAM deny), không phải Config rule + remediation (đó là **phát hiện sau**)
- **Bảo vệ resource cụ thể** trong số nhiều resource cùng loại → **tag resource + SCP condition `aws:ResourceTag/<key>`**
- **`aws:SourceIp`** = IP của người gọi API, **không phải** CIDR trong SG rule — đừng nhầm hai khái niệm này
- SCP chỉ áp dụng đúng phạm vi khi **attach vào đúng OU/account** — nhớ kiểm tra SCP có "quá rộng" (áp lên cả org) hay đúng target không

### TD explanation

Service control policies (SCPs) in AWS Organizations are a means of centrally controlling permissions to services and actions across multiple AWS accounts. They allow you to manage permissions in your organization centrally by applying policies to organizational units (OUs) and accounts.

In this scenario, the company wants to prevent specific security groups within the PROD OU from being modified. To achieve this, you can implement a Service Control Policy (SCP) that denies the ec2:AuthorizeSecurityGroup* actions. This policy targets only the security groups tagged with a specific label, such as ‘scope:private’. Note that ‘scope:private’ is merely an example of a tag name; you can choose any name that fits your organizational structure or naming conventions. By tagging the crucial security groups accordingly and referencing this tag in the SCP, you can prevent unauthorized modifications.

Hence, the correct answer is: Tag the security groups using the key value ‘scope:private’. Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:ResourceTag/scope”: “private” condition key. Attach the SCP to the PROD OU.

The option that says: Apply a remediation action to the Config rule using the AWSConfigRemediation-RemoveUnrestrictedSourceIngressRules AWS System Manager Automation document is incorrect. This option is a reactive measure, not a proactive one. It does not prevent security groups that allow traffic from 0.0.0.0/0 being created in the first place. Instead, it identifies non-compliant resources after they’ve been created and then attempts to fix them. Therefore, it does not meet the security team’s requirement to prevent the creation of such security groups.

The option that says: Create a Service control policy (SCP) that denies the ec2:AuthorizeSecurityGroup* action with the “aws:SourceIp”: “0.0.0.0/0” condition key. Attach the SCP to the PROD OU is incorrect. This option would restrict modification of security groups that have a source IP of 0.0.0.0/0 for everyone in the organization, not just the PROD OU. It’s too broad and doesn’t specifically target the critical security groups.

The option that says: Create an AWS Lambda function that calls the RevokeSecurityGroupIngress on security groups that have an inbound rule allowing traffic from 0.0.0.0/0. Subscribe the Lambda function to the SNS topic is incorrect. Similar to one of the incorrect options, this one is only a reactive measure rather than a proactive one. The security group allowing all incoming traffic would still be created initially, and then the Lambda function would remove the ingress rule.

 

References:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html

https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/

 

Check out this AWS Organizations Cheat Sheet:

https://tutorialsdojo.com/aws-organizations/

</details>

<a id="q31"></a>

## Q31

A company has a designated AWS account for each project of its development team. All of these AWS accounts are linked to the main AWS account under the same AWS Organizations. The CFO allocates a budget for each project owner. Each project owner is allowed to provision any cloud resources that they need but all resources should have the Project tag which is used for cost allocation. After a recent audit, several team members are not adding the Project tag on their Amazon EC2 instances which results in inaccurate cost reports.

Which of the following steps should be implemented to identify instances with the missing tag and to prevent the creation of instances without the Project tag? (Select THREE.)

- **A.** Apply an SCP to the AWS Organization that will deny the ec2:RunInstances action if the Project tag is not applied.
- **B.** Configure an AWS Config aggregator for the AWS organization to generate a list of all EC2 instances without the Project tag.
- **C.** Create an IAM policy on each project account that will deny the ec2:RunInstances action if the Project tag is not applied.
- **D.** Create an AWS Config rule on each project account to flag any resources if the Project tag is not applied.
- **E.** Leverage AWS Security Hub as an aggregator to generate a list of all EC2 instances without the Project tag.
- **F.** Create an assessment in Amazon Inspector to scan the AWS Organization and generate a list of all EC2 instances with the missing Project tag.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B, D · **You picked:** D, E, F

🔑 **Key words:** IDENTIFY instances missing tag AND PREVENT creation; org-wide list

🪤 **Your trap:** Security Hub / Inspector don't check tags

🧠 **Rule:** Prevent → SCP deny RunInstances w/o tag; Detect → Config rule; org-wide list → Config aggregator.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organization
 ├─ Project account 1
 ├─ Project account 2
 ├─ ... nhiều project account

Yêu cầu: mọi EC2 instance PHẢI có tag "Project"
    1) IDENTIFY  — tìm ra instance nào đang THIẾU tag (org-wide list)
    2) PREVENT   — chặn KHÔNG cho tạo instance mới thiếu tag
```

Chọn **BA (3)** đáp án đúng: **A, B, D**. Anh chọn **D, E, F** — đúng D, sai E và F.

#### Ghép đúng 2 yêu cầu với 3 công cụ

```
PREVENT (ngăn tạo mới)
    → SCP deny ec2:RunInstances nếu thiếu tag "Project"     (A)
    → Attach ở cấp Organization → áp dụng mọi account

DETECT (phát hiện instance hiện có thiếu tag)
    → AWS Config rule ở TỪNG account, flag non-compliant     (D)

AGGREGATE (gom danh sách toàn Organization)
    → AWS Config AGGREGATOR ở cấp Organization                (B)
    → gom compliance data từ tất cả account có Config bật
```

- **A đúng:** SCP là cơ chế duy nhất **chặn hành động trước khi nó xảy ra** ở cấp Organization. Chỉ cần một SCP, áp lên toàn bộ project accounts, không phải làm thủ công từng account.
- **D đúng:** Config rule (custom hoặc managed) đánh giá continuous compliance của resource hiện có — đúng công cụ để "flag any resources if the Project tag is not applied".
- **B đúng:** Config **aggregator** là tính năng chuyên biệt để gom dữ liệu compliance từ **nhiều account/nhiều region, hoặc toàn bộ Organization** thành một view duy nhất — đúng cái đề cần: "generate a list of all EC2 instances without the Project tag" trên **toàn tổ chức**, chứ không phải xem từng account riêng lẻ.

#### Vì sao anh chọn E, F sai

- **E — Security Hub làm aggregator:** Security Hub đúng là có khả năng tổng hợp finding từ nhiều account (giống aggregator), nhưng **Security Hub được thiết kế để chạy security best-practice checks** (CIS, PCI-DSS, các control bảo mật…), **không kiểm tra việc gắn tag cost-allocation**. Đây là bẫy: "aggregator" nghe giống đúng chức năng nhưng sai domain — Security Hub không có control kiểm tra tag tùy ý như "Project".
- **F — Amazon Inspector:** Inspector là dịch vụ **quét lỗ hổng bảo mật (vulnerability) bên trong EC2/container/Lambda**, hoàn toàn không liên quan đến việc kiểm tra tag. Chọn Inspector cho bài toán tagging là sai domain hoàn toàn.

**C sai vì kém hiệu quả hơn A:** IAM policy deny cũng có thể chặn `ec2:RunInstances` thiếu tag, nhưng phải **cấu hình riêng lẻ trên từng account** — không mở rộng tốt bằng một SCP duy nhất ở cấp Organization.

| Phương án | Đúng vai trò gì | Vấn đề nếu chọn |
|---|---|---|
| **A. SCP deny RunInstances** | Prevent, org-wide | — |
| **B. Config aggregator** | Aggregate list toàn org | — |
| **D. Config rule mỗi account** | Detect/flag non-compliant | — |
| C. IAM policy mỗi account | Prevent nhưng không scale | Phải làm lại ở từng account |
| E. Security Hub | Security checks, không phải tag checks | Sai domain |
| F. Inspector | Vulnerability scanning | Sai domain hoàn toàn |

#### Quy tắc nhớ cho thi

- **"Prevent creation of non-compliant resource, org-wide"** → **SCP**, không phải IAM policy từng account
- **"Detect/flag resource hiện có không tuân thủ"** → **AWS Config rule**
- **"Gom danh sách compliance từ nhiều account/toàn Organization"** → **AWS Config aggregator** (không phải Security Hub, không phải Inspector)
- **Security Hub** = security posture/best-practice checks; **Inspector** = vulnerability scanning — cả hai **không** kiểm tra resource tag
- Câu hỏi "Select THREE" thường ghép đúng 3 vai trò khác nhau (prevent / detect / aggregate) — đọc kỹ xem đề cần bao nhiêu hành vi riêng biệt

### TD explanation

Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. SCPs help you to ensure your accounts stay within your organization’s access control guidelines. SCPs are available only in an organization that has all features enabled. SCPs aren’t available if your organization has enabled only the consolidated billing features.

By denying the action to run instances without the Project tag, you enforce tagging policies and prevent non-compliant resource creation.

An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from the following:

-Multiple accounts and multiple regions.

-Single account and multiple regions.

-An organization in AWS Organizations and all the accounts in that organization which have AWS Config enabled.

Hence, the correct answers are:

– Create an AWS Config rule on each project account to flag any resources if the Project tag is not applied. AWS Config rules allow you to continuously monitor and evaluate your AWS resource configurations. By setting up a rule to flag resources without the Project tag, you ensure that any non-compliant resources are identified promptly.

– Apply an SCP to the AWS Organization that will deny the ec2:RunInstances action if the Project tag is not applied. The SCP applied to the organization will deny members from spawning EC2 instances without the Project tag.

– Configure an AWS Config aggregator for the AWS organization to generate a list of all EC2 instances without the Project tag. An aggregator can collect AWS Config configuration and compliance data from multiple AWS accounts and regions. AWS Config can identify EC2 instances if they have the required Project tag or not.

The option that says: Create an assessment in Amazon Inspector to scan the AWS Organization and generate a list of all EC2 instances with the missing Project tag is incorrect. AWS Inspector is primarily used for scanning vulnerabilities inside EC2 instances, and not about proper cost allocation tagging.

The option that says: Create an IAM policy on each project account that will deny the ec2:RunInstances action if the Project tag is not applied is incorrect because while IAM policies can control access, using SCPs at the organization level is typically more effective for enforcing such rules across multiple accounts. IAM policies would need to be individually managed in each account, which is less efficient.

The option that says: Leverage AWS Security Hub as an aggregator to generate a list of all EC2 instances without the Project tag is incorrect. This service performs security best practice checks, aggregates alerts, and enables automated remediation, but it is not suitable for tag checking of AWS resources.

 

References:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html
https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html

Check out these AWS Config Cheat Sheet and SCP vs IAM comparison:

https://tutorialsdojo.com/aws-config/
https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

</details>

<a id="q67"></a>

## Q67

A company uses AWS Organizations to manage hundreds of AWS accounts. The company plans to designate a central network account where a shared VPC will be created. Accounts under the Customers Organization Unit (OU) are allowed to create resources on the shared VPC, but they should not be able to manage it.

The AWS Security Hub has also been configured to provide the company with a comprehensive view of their security state in AWS and to help them verify their AWS workloads against security industry standards and best practices. There’s also a Security Hub administrator account that has already been designated in AWS Organizations to view data from its member accounts.

Which combination of steps would meet the company’s objectives? (Select TWO.)

- **A.** Create a separate VPC within each individual account in the Customers OU. Set up a Resource Access Manager (RAM) resource share for a Transit Gateway in the management account and share it with the Customers OU. Establish VPC peering connections between all VPCs.
- **B.** Create a service control policy (SCP) within AWS Organizations and attach it to the Customers OU. This SCP should contain statements for denying management actions to a VPC.
- **C.** Configure a managed prefix list in the central network account, specifying the IP ranges that align with the desired network configuration. Use AWS Resource Access Manager (RAM) to share this prefix list with the Customers OU.
- **D.** Configure the management account to enable AWS Resource Access Manager (RAM) resource sharing with AWS Organizations.
- **E.** Use AWS Resource Access Manager (RAM) to create a resource share in the management account. Include all subnets of the shared VPC and set the Customers OU as the principal.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D, E · **You picked:** B, D

🔑 **Key words:** central shared VPC; Customers OU create resources but not manage

🪤 **Your trap:** SCP not needed — shared-VPC participants can't modify VPC anyway

🧠 **Rule:** VPC sharing → enable RAM sharing with Organizations + RAM share subnets to OU principal.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Central network account
    └─ Shared VPC  ──────share──────►  Customers OU (nhiều account)

Yêu cầu:
    - Account trong Customers OU: TẠO ĐƯỢC resource trong shared VPC
                                   (VD: EC2 instance trong subnet share)
    - Nhưng KHÔNG được QUẢN LÝ VPC (sửa route table, SG của VPC, subnet, IGW…)

Ngoài lề: Security Hub administrator account đã có sẵn (không liên quan lời giải)
```

Chọn **HAI (2)** đáp án đúng: **D, E**. Anh chọn **B, D** — đúng D, sai B.

#### Cơ chế VPC Sharing qua RAM

```
Bước 1 (D): Management account
    → Enable "RAM resource sharing with AWS Organizations"
      (bật tính năng share tự động trong phạm vi Organization,
       không cần từng account phải accept lời mời thủ công)

Bước 2 (E): Trong management/owner account
    → RAM resource share: gồm SUBNET của shared VPC
    → Principal = Customers OU
    → Account trong Customers OU giờ tạo được resource (EC2, RDS…)
      TRONG các subnet đó
```

Đây chính là **VPC Sharing**: chủ sở hữu VPC (owner) share **subnet** (không phải toàn VPC) cho account khác qua RAM. Participant account **chỉ thấy và dùng được subnet để launch resource**, nhưng **không có quyền quản lý VPC** (không sửa route table, NACL, VPC peering, IGW…) — quyền quản lý VPC luôn thuộc về owner account. Đây là hành vi **mặc định của VPC sharing**, không cần thêm bước gì khác để "khóa" quyền quản lý.

#### Vì sao anh chọn B (SCP deny VPC management) sai

Đây đúng là bẫy được thiết kế riêng cho câu này: **SCP để deny "management actions to a VPC" là THỪA**, vì bản chất VPC Sharing qua RAM **đã không cấp quyền quản lý VPC cho participant account ngay từ đầu**. Participant account không có API permission nào để sửa route table/SG của VPC thuộc account khác — không phải vì bị SCP chặn, mà vì **về mặt kiến trúc, VPC vẫn thuộc sở hữu (và chỉ owner mới quản lý được) của central network account**. Viết thêm SCP để "deny" một hành động vốn dĩ họ không có quyền làm là dư thừa, không giải quyết thêm vấn đề gì.

#### Vì sao A, C sai

- **A — Peering qua Transit Gateway, mỗi account có VPC riêng:** sai mô hình — đề yêu cầu **một VPC trung tâm dùng chung**, không phải nhiều VPC riêng lẻ kết nối với nhau qua TGW/peering. Cách này tạo ra nhiều VPC phải quản lý riêng rẽ, phức tạp hơn, không đáp ứng "central shared VPC".
- **C — Share managed prefix list:** prefix list chỉ chứa danh sách CIDR để dùng trong SG/route table rules — **không cấp quyền tạo resource trong VPC**, cũng không ngăn được việc quản lý VPC. Hoàn toàn lạc đề.

| Phương án | Vấn đề |
|---|---|
| **D** | Đúng: bật RAM sharing với Organizations |
| **E** | Đúng: RAM share subnet, principal = Customers OU |
| A | Sai mô hình — nhiều VPC + peering, không phải 1 shared VPC |
| B | Thừa — VPC sharing vốn đã không cấp quyền quản lý cho participant |
| C | Prefix list không liên quan đến việc tạo resource/quản lý VPC |

#### Quy tắc nhớ cho thi

- **"central/shared VPC, participant account tạo resource nhưng không quản lý VPC"** → **VPC Sharing qua RAM** (share subnet, không share toàn VPC)
- Trong Organization: bật **"enable resource sharing with AWS Organizations"** ở management account trước, rồi mới tạo resource share
- **VPC Sharing mặc định đã không cho participant quyền quản lý VPC** — thấy đáp án thêm SCP để "deny VPC management" trong bối cảnh VPC sharing → thường là **đáp án dư thừa/nhiễu**
- **Managed prefix list** → chỉ dùng cho SG/route table rules, không liên quan đến việc share VPC hay cấp quyền tạo resource

### TD explanation

AWS Resource Access Manager (AWS RAM) helps you securely share your resources (e.g., AWS Transit Gateways, Subnets, AWS License Manager configurations) across AWS accounts, within your organization or organizational units (OUs), and with AWS Identity and Access Management (IAM) roles and users for supported resource types. If you have multiple AWS accounts, you can create a resource once and use AWS RAM to make that resource usable by those other accounts. If your account is managed by AWS Organizations, you can share resources with all the other accounts in the organization or only those accounts contained by one or more specified organizational units (OUs).

In this scenario, the company wants to have a central shared VPC that other AWS accounts can use, but not manage. We can use AWS RAM to achieve this. By enabling resource sharing with AWS Organizations from the management account, the company can share the resources, like subnets of the shared VPC, across the entire organization. Creating a resource share in the management account, including all subnets of the shared VPC, and setting the Customers OU as the principal would allow the accounts under the Customers OU to use the shared VPC without having the ability to manage it.

Hence, the correct answers are:

– Configure the management account to enable AWS Resource Access Manager (RAM) resource sharing with AWS Organizations.

– Use AWS Resource Access Manager (RAM) to create a resource share in the management account. Include all subnets of the shared VPC and set the Customers OU as the principal.

The option that says: Create a service control policy (SCP) within AWS Organizations and attach it to the Customers OU. This SCP should contain statements for denying management actions to a VPC is incorrect. SCPs are used to set fine-grained permissions for AWS Organizations and can indeed deny specific actions. However, in the context of a shared VPC using AWS RAM, it’s AWS RAM that manages the permissions, and the shared accounts do not have management permissions for the VPC by default. Therefore, denying VPC management actions via an SCP would be unnecessary in this scenario.

The option that says: Create a separate VPC within each individual account in the Customers OU. Set up a Resource Access Manager (RAM) resource share for a Transit Gateway in the management account and share it with the Customers OU. Establish VPC peering connections between all VPCs is incorrect. While this setup would enable network communication between all the accounts in the Customers OU, it doesn’t meet the company’s stated objective to use a central shared VPC. Furthermore, this approach would result in multiple VPCs that need to be individually managed rather than a single shared VPC, thus increasing complexity and potentially introducing configuration inconsistencies.

The option that says: Configure a managed prefix list in the central network account, specifying the IP ranges that align with the desired network configuration. Use AWS Resource Access Manager (RAM) to share this prefix list with the Customers OU is incorrect. Sharing a managed prefix list doesn’t prevent the individual accounts from managing the shared VPC, nor does it provide them with the ability to use a centrally managed shared VPC. The managed prefix list can control what IP ranges are allowed or denied access, but it doesn’t restrict the ability to create or manage resources within the VPC itself.

 

References:

https://docs.aws.amazon.com/ram/latest/userguide/what-is.html

https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/

 

Check out the AWS Resource Access Manager (RAM) Cheat Sheet:

https://tutorialsdojo.com/aws-resource-access-manager/

</details>

<a id="q18"></a>

## Q18

An international enterprise is leveraging AWS Organizations for the administration of its various AWS accounts. Their primary IT operations account has a VPC where multiple applications are deployed. This VPC is linked to a transit gateway. As part of a new initiative, they have established a staging server environment in a staging account that requires connectivity to the applications in the primary IT operations account.

Due to the nature of the staging process, resources in the staging account will be frequently terminated and re-provisioned. The staging team also requires the capability to reconfigure their connection to the primary IT operations account as needed.

What approach would satisfy these conditions?

- **A.** Enable automatic acceptance for the transit gateway attachments in the staging account and share the transit gateway with the staging account using AWS Resource Access Manager (AWS RAM).
- **B.** Establish Direct Connect connections from the staging account to each application in the primary IT operations account.
- **C.** Create a new transit gateway from the staging account to the primary IT operations account for each connection. For each connection, send a peering request from the staging account’s transit gateway to the primary IT operations account’s transit gateway.
- **D.** Enable automatic acceptance for the transit gateway attachments in the staging account and create a VPC endpoint in the staging account for each application in the primary IT operations account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** staging account frequently re-provisioned; connect to TGW in IT ops account

🪤 **Your trap:** VPC endpoint per application doesn't scale

🧠 **Rule:** Cross-account TGW → share TGW via RAM + auto-accept attachments.

### 🇻🇳 Phân tích chi tiết

> Lưu ý: anh chọn **D** cả ở bài timed test lẫn hôm nay redo — đây là câu cần khắc kỹ khái niệm, vì D **nghe rất hợp lý** nhưng sai bản chất.

#### Tình huống

```
Primary IT Ops account                    Staging account
┌─────────────────────────┐               ┌─────────────────────┐
│ VPC (nhiều applications) │               │ Staging servers      │
│    │                     │               │  → tạo/xóa LIÊN TỤC  │
│    └── Transit Gateway   │◄── cần kết nối──│  → cấu hình lại      │
└─────────────────────────┘   linh hoạt    │    connection thường  │
                                            │    xuyên              │
                                            └─────────────────────┘

Yêu cầu: kết nối staging ↔ TGW của IT Ops,
         dễ dàng TÁI CẤU HÌNH mỗi khi staging bị rebuild
```

Đáp án đúng: **A** (share TGW qua RAM + auto-accept attachment). Anh chọn **D** (auto-accept + VPC endpoint cho từng application).

#### Vì sao A đúng — đúng bài toán "môi trường build lại liên tục"

```
Bước 1: Primary IT Ops account
    → AWS RAM: share Transit Gateway với staging account
      (retain ownership, có thể revoke access bất kỳ lúc nào)

Bước 2: Staging account
    → Enable "automatic acceptance" cho TGW attachment
    → Mỗi lần VPC staging bị tạo lại (rebuild):
        tạo attachment mới → TỰ ĐỘNG được accept
        → không cần người IT Ops account thủ công approve mỗi lần
```

Điểm mấu chốt: **Transit Gateway attachment auto-accept** giải quyết đúng vấn đề "resources trong staging account bị terminate/re-provision liên tục". Mỗi lần dựng lại VPC staging, chỉ cần tạo attachment mới tới TGW đã được share — không phải làm lại thủ tục share/approve từ đầu. Đây chính là cơ chế được thiết kế cho **kết nối network linh hoạt, tái lập nhiều lần, ít thao tác thủ công.**

#### Vì sao D (lựa chọn của anh) sai — điểm cần khắc sâu

D có **một nửa đúng** (auto-accept TGW attachment) nhưng nửa còn lại — **VPC endpoint (PrivateLink) cho từng application** — sai bản chất bài toán:

```
Interface VPC Endpoint (PrivateLink)
    = kết nối PRIVATE tới MỘT SERVICE CỤ THỂ
      (service đó phải được publish như một "endpoint service"
       qua Network Load Balancer, hoặc là AWS service như S3/DynamoDB Gateway,
       hoặc AWS PrivateLink-ready service)

    ≠ kết nối VPC-to-VPC tổng quát
    ≠ routing giữa 2 mạng (đó là việc của TGW/VPC peering)
```

- **Không scale:** đề nói "multiple applications" trong VPC của IT Ops account. Dùng VPC endpoint nghĩa là phải: (1) đưa từng application ra sau một Network Load Balancer, (2) publish nó thành một **endpoint service** riêng, (3) tạo một **interface endpoint** riêng trong staging account cho từng service đó. Có bao nhiêu application thì có bấy nhiêu bước cấu hình lặp lại — hoàn toàn ngược lại với yêu cầu "dễ tái cấu hình, ít thao tác".
- **Sai loại kết nối:** PrivateLink chỉ mở một "lỗ" hẹp tới **một service endpoint cụ thể** (giống như gọi một API private), không phải một đường kết nối mạng đầy đủ giữa hai VPC như TGW cung cấp. Nếu ứng dụng trong IT Ops account cần giao tiếp qua nhiều port/protocol khác nhau (không chỉ một endpoint service), PrivateLink không đáp ứng được.
- **Không tận dụng TGW đã có sẵn:** đề đã nói rõ VPC của IT Ops account "linked to a transit gateway" — chìa khóa của bài là **share cái TGW đó**, không phải dựng thêm một cơ chế PrivateLink song song.

Tóm lại: TGW = "mở đường cao tốc dùng chung, share 1 lần, attachment tái lập tự động". VPC endpoint/PrivateLink = "mở 1 cổng nhỏ riêng cho từng dịch vụ cụ thể, phải publish + tạo endpoint riêng cho mỗi service". Bài toán ở đây cần đường cao tốc dùng chung, tái lập nhanh — không phải cổng nhỏ nhân bản theo từng app.

#### Vì sao B, C sai (ngắn gọn)

- **B — Direct Connect tới từng application:** DX là kết nối vật lý dedicated, thiết lập chậm, dùng cho kết nối ổn định lâu dài — hoàn toàn không phù hợp với môi trường "terminate/re-provision liên tục".
- **C — Tạo TGW riêng cho staging + peering TGW-to-TGW mỗi connection:** vừa tốn kém (mỗi TGW attachment/peering đều có chi phí & thời gian cấu hình), vừa không cần thiết vì chỉ cần **share TGW hiện có**, không cần TGW mới.

| Phương án | Cơ chế | Vấn đề |
|---|---|---|
| **A** | RAM share TGW + auto-accept attachment | — |
| D | Auto-accept + VPC endpoint mỗi application | Không scale, sai loại kết nối (service-specific, không phải VPC-to-VPC) |
| B | Direct Connect | Quá chậm/cứng nhắc cho môi trường thay đổi liên tục |
| C | TGW riêng + peering mỗi connection | Thừa, tốn kém, không tận dụng TGW có sẵn |

> 📝 **Ghi chú kỹ thuật:** trong thực tế, *Auto accept shared attachments* là thuộc tính của **Transit Gateway**, do account **sở hữu TGW (IT Ops)** bật. Đáp án của đề ghi "in the staging account" — khi thi cứ nhận diện cặp **RAM share TGW + auto-accept attachments** là đáp án đúng.

#### Quy tắc nhớ cho thi

- **"Đã có Transit Gateway ở account A, cần account B (môi trường build lại liên tục) kết nối vào"** → **RAM share TGW + auto-accept attachment**, KHÔNG PHẢI VPC endpoint
- **Ghi nhớ:** *"VPC endpoint = một service, một cổng nhỏ" / "Transit Gateway = một mạng, một đường cao tốc dùng chung"* — đề cần kết nối tới "nhiều applications" (network-level) thì nghĩ TGW; đề cần kết nối tới "một service cụ thể" (ví dụ một API nội bộ, DynamoDB, một SaaS partner service) thì mới nghĩ PrivateLink/VPC endpoint
- **"auto-accept"** chỉ nói lên việc attachment được accept tự động — không tự nhiên suy ra đáp án đúng là VPC endpoint; phải xét tiếp cơ chế kết nối có đúng loại kết nối cần hay không
- **Frequently re-provisioned / reconfigure often** → tín hiệu mạnh cho **TGW attachment auto-accept**, vì đây chính là tính năng được thiết kế để giảm thao tác thủ công khi attachment được tạo lại nhiều lần

### TD explanation

AWS Transit Gateway is a service that enables customers to connect their Amazon Virtual Private Clouds (VPCs) and their on-premises networks to a single gateway. When you create attachments to a transit gateway, you can configure automatic acceptance for shared attachments, which means that the attachments are automatically accepted and the connection is established.

AWS RAM is a service that enables you to easily and securely share AWS resources with any AWS account or within your AWS Organization. You can share AWS Transit Gateways, Subnets, AWS License Manager configurations, and more. You retain ownership of shared resources, and you can revoke access at any time.

Hence, the correct answer is: Enable automatic acceptance for the transit gateway attachments in the staging account and share the transit gateway with the staging account using AWS Resource Access Manager (AWS RAM). By enabling automatic acceptance for the transit gateway attachments, the staging account can easily connect to the primary IT operations account. This approach allows for easy reconfiguration of connections as needed, which is a requirement in the question. Furthermore, by sharing the transit gateway with the staging account using AWS RAM, the staging account can access the resources in the primary IT operations account, providing the necessary connectivity for the staging process.

The option that says: Create a new transit gateway from the staging account to the primary IT operations account for each connection. For each connection, send a peering request from the staging account’s transit gateway to the primary IT operations account’s transit gateway is incorrect because creating a new transit gateway for each connection would be inefficient and unnecessary. It would also complicate the process of reconfiguring connections, which is something the staging team needs to be able to do easily.

The option that says: Enable automatic acceptance for the transit gateway attachments in the staging account and create a VPC endpoint in the staging account for each application in the primary IT operations account is incorrect because while this option does involve enabling automatic acceptance for the transit gateway attachments, creating a VPC endpoint in the staging account for each application in the primary IT operations account is not the most efficient or flexible solution. It would require a significant amount of configuration and wouldn’t easily allow for reconfiguration of connections.

The option that says: Establish Direct Connect connections from the staging account to each application in the primary IT operations account is incorrect because while Direct Connect does provide a dedicated network connection from a network to AWS, it’s not as flexible or easily reconfigurable. It’s also typically used for more stable, long-term connections rather than a frequently changing staging environment.

 

References:

https://repost.aws/knowledge-center/transit-gateway-sharing

https://docs.aws.amazon.com/ram/latest/userguide/what-is.html

 

Check out these AWS Transit Gateway and AWS Resource Access Manager Cheat Sheets:

https://tutorialsdojo.com/aws-transit-gateway/

</details>

<a id="q54"></a>

## Q54

A company that operates a multi-cloud environment uses an on-premises Microsoft Active Directory for user authentication. As part of its expansion plans, the company is preparing to launch services in AWS. They want to leverage its existing Active Directory to control the permissions of those who wish to access AWS resources. There’s already a Direct Connect connection in place between the company’s on-premises data center and its AWS networks.

The company wants to enforce a security policy where access to accounts is regulated based on user group membership and assigned roles. Moreover, they must have the ability to manage user identities in a centralized location.

Which solution will meet these requirements?

- **A.** Export the user list from the on-premises Active Directory and import it into a new AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). Configure trust relationships between AWS Managed Microsoft AD and AWS accounts. Use AWS Identity and Access Management (IAM) to manage user access and permissions.
- **B.** Connect to the Active Directory using AWS IAM Identity Center with SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use attribute-based access controls (ABACs) to grant access to the AWS accounts.
- **C.** Create a PowerShell script that creates a separate identity provider for connecting to the Active Directory. Set up IAM user accounts manually in each AWS account and synchronize them with the identities in Active Directory.
- **D.** Create an AWS Cognito User Pool and connect it to Active Directory using SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use a Cognito Identity pool to grant access to the AWS accounts.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** existing on-prem AD; group/role-based access; manage identities in one place

🪤 **Your trap:** Import users into AWS Managed AD = duplicate identity store

🧠 **Rule:** Existing IdP → IAM Identity Center + SAML 2.0 + SCIM auto-provisioning + ABAC.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises Active Directory (multi-cloud company)
        │
        │  Direct Connect (đã có sẵn)
        ▼
AWS accounts

Yêu cầu:
    1) Dùng AD hiện có để control quyền truy cập AWS resources
    2) Access theo GROUP MEMBERSHIP + ROLE
    3) Quản lý identity TẬP TRUNG một chỗ (single source of truth)
```

Đáp án đúng: **B** (IAM Identity Center + SAML 2.0 + SCIM + ABAC). Anh chọn **A** (import user vào AWS Managed Microsoft AD).

#### Vì sao B đúng

```
On-prem AD  ──SAML 2.0──►  AWS IAM Identity Center
                                │
                                ├─ SCIM v2.0: tự động đồng bộ user/group
                                │   attributes từ AD sang Identity Center
                                │   (không cần export/import thủ công)
                                │
                                └─ ABAC (attribute-based access control):
                                    policy cấp quyền dựa trên
                                    group membership / role attribute
                                    → đúng account/role tương ứng
```

- **SAML 2.0** thiết lập trust relationship, cho phép user login AWS access portal bằng chính credential AD hiện có.
- **SCIM v2.0** tự động hóa việc đồng bộ user & group — đây chính là "quản lý identity ở MỘT nơi tập trung" (AD vẫn là nguồn dữ liệu gốc, Identity Center chỉ đồng bộ theo).
- **ABAC** cho phép cấp quyền theo attribute (group, role) thay vì phải viết permission cứng cho từng user — đúng yêu cầu "regulated based on user group membership and assigned roles".

IAM Identity Center (tên cũ: AWS SSO) là dịch vụ **được thiết kế riêng** cho bài toán "một AD/IdP hiện có, cần centralize quyền truy cập nhiều AWS account trong Organization" — đây là use case chuẩn mực nhất của dịch vụ này.

#### Vì sao anh chọn A sai — "duplicate identity store"

```
A: Export user list từ AD  →  Import vào AWS Managed Microsoft AD
                                (một bản AD MỚI, riêng biệt, chạy trong AWS)
```

Vấn đề cốt lõi: **A tạo ra một identity store thứ hai**, tách biệt khỏi AD gốc on-premises. Ngay khi có user mới, đổi mật khẩu, hoặc thay đổi group membership ở AD gốc, không có gì tự động đồng bộ sang AWS Managed Microsoft AD — phải làm lại export/import thủ công. Điều này **trực tiếp vi phạm yêu cầu "manage user identities in a centralized location"**, vì giờ có 2 nơi cần quản lý identity thay vì 1. Ngoài ra, A dùng IAM để cấp quyền — IAM policy không có cơ chế ABAC tự nhiên gắn với group AD như Identity Center cung cấp, nên việc "regulate theo group membership + role" cũng khó triển khai gọn gàng bằng B.

#### Vì sao C, D sai

- **C — PowerShell script tự viết + IAM user thủ công từng account:** cách làm thủ công, tốn công sức, dễ lỗi/đồng bộ trễ, và **hoàn toàn không có identity quản lý tập trung** — mỗi account tự có tập IAM user riêng.
- **D — Cognito User Pool + Cognito Identity Pool:** Cognito được thiết kế cho **authentication của end-user trong ứng dụng web/mobile** (customer-facing), không phải để quản lý quyền truy cập **AWS Console/account cho nhân viên nội bộ (workforce identity)**. Dù kỹ thuật có thể kết nối SAML + SCIM tương tự, Cognito không cung cấp mức độ centralized control qua AWS Organizations như IAM Identity Center.

| Phương án | Vấn đề |
|---|---|
| **B** | Đúng: Identity Center + SAML + SCIM + ABAC |
| A | Tạo AD thứ hai → duplicate identity store, không centralized |
| C | Thủ công, không centralized, dễ lỗi |
| D | Cognito dành cho customer-facing app, không phải workforce/AWS account access |

#### Quy tắc nhớ cho thi

- **"Đã có on-prem AD/IdP, muốn dùng nó để login/quản lý quyền vào nhiều AWS account"** → **IAM Identity Center + SAML 2.0**
- **"Tự động đồng bộ user/group từ IdP"** → **SCIM v2.0**
- **"Cấp quyền theo group/role/attribute"** → **ABAC** trong Identity Center
- **"Import/export user thủ công sang một AD mới trong AWS"** → luôn là bẫy vì tạo **duplicate identity source**, đi ngược "centralized identity management"
- **Cognito** → dành cho end-user của ứng dụng (customer identity), không phải workforce identity cho AWS account access

### TD explanation

With AWS IAM Identity Center (successor to AWS Single Sign-On), you can manage sign-in security for your workforce identities, also known as workforce users. IAM Identity Center provides one place where you can create or connect workforce users and centrally manage their access across all their AWS accounts and applications.

Both SCIM and SAML are important considerations for configuring IAM Identity Center.

You can use AWS IAM Identity Center (successor to AWS Single Sign-On) to authenticate identities from the IdPs through the Security Assertion Markup Language (SAML) 2.0 standard. This enables your users to sign in to the AWS access portal with their corporate credentials. They can then navigate to their assigned accounts, roles, and applications hosted in external IdPs.

IAM Identity Center supports automatic provisioning (synchronization) of user and group information from your identity provider (IdP) into IAM Identity Center using the System for Cross-domain Identity Management (SCIM) v2.0 protocol. When you configure SCIM synchronization, you create a mapping of your identity provider (IdP) user attributes to the named attributes in IAM Identity Center. This causes the expected attributes to match between IAM Identity Center and your IdP.

To allow users to use their Active Directory credentials in accessing AWS Accounts within AWS Organizations, you should establish a trust relationship between your on-premises Active Directory and AWS by setting up AWS IAM Identity Center with SAML 2.0.

To synchronize user attributes, such as username, email address, or group membership, enable System for Cross-domain Identity Management (SCIM) v2.0 automatic provisioning, which allows the management of user identities in a centralized location. To ensure access to accounts is constrained based on the user’s membership in particular groups and assigned roles AWS IAM Identity Center provides attribute-based access controls (ABACs), which let you define policies that grant access to AWS Accounts based on attributes like group membership or assigned roles in the Active Directory.

Hence, the correct answer is: Connect to the Active Directory using AWS IAM Identity Center with SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use attribute-based access controls (ABACs) to grant access to the AWS accounts.

The option that says: Create an AWS Cognito User Pool and connect it to Active Directory using SAML 2.0. Use the System for Cross-domain Identity Management (SCIM) v2.0 protocol to enable automatic provisioning. Use a Cognito Identity pool to grant access to the AWS accounts is incorrect. Although AWS Cognito can integrate with an existing Active Directory, it’s typically used for building sign-up and sign-in functionality for mobile app and web app users. Cognito can be an alternative solution when you want to authenticate users using their Active Directory credentials, but it will not provide the same level of centralized control as AWS IAM Identity Center in terms of user management and access control across AWS Organizations.

The option that says: Create a PowerShell script that creates a separate identity provider for connecting to the Active Directory. Set up IAM user accounts manually in each AWS account and synchronize them with the identities in Active Directory is incorrect. This approach is labor-intensive and could lead to consistency issues due to manual synchronization. Furthermore, this does not provide centralized identity management, as you would need to manage IAM user accounts in each AWS account separately

The option that says: Export the user list from the on-premises Active Directory and import it into a new AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). Configure trust relationships between AWS Managed Microsoft AD and AWS accounts. Use AWS Identity and Access Management (IAM) to manage user access and permissions is incorrect. This option doesn’t fully leverage the existing Active Directory, as it requires creating a new AWS Managed Microsoft AD. While AWS Managed Microsoft AD could potentially serve the requirements, this approach would likely lead to redundant management and potential synchronization issues. This also increases the complexity and cost of the solution, as the company would have to manage two separate Active Directory environments (on-premises and AWS Managed Microsoft AD).

 

References:

https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html

https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html

 

Check out this AWS IAM Cheat Sheet:

https://tutorialsdojo.com/aws-identity-and-access-management-iam

</details>

<a id="q36"></a>

## Q36

A company plans to migrate an application consisting of an AWS Lambda function and an Amazon Aurora MySQL database from one AWS account to another. Both accounts belong to the same organization in AWS Organizations. The company intends for the target account to deploy the application in the same AWS region as the source account. The Lambda function is created from a ZIP deployment package stored in Amazon S3.

Which combination of actions should be performed to migrate the application with the least amount of downtime? (Select TWO.)

- **A.** Use AWS Resource Access Manager (AWS RAM) to share the Aurora MySQL DB cluster with the target AWS account. Create an Aurora clone in the target account.
- **B.** Use the mysqldump utility to export the data and schema from the Aurora MySQL database into a SQL dump file. Transfer the SQL dump file to the target AWS account and import it into a newly created Aurora MySQL database instance.
- **C.** Use AWS Resource Access Manager (AWS RAM) to share the Lambda function with the target account.
- **D.** Download the ZIP deployment package and upload it to the target account's S3 bucket. Create a new Lambda function in the target account using the ZIP package.
- **E.** Create a snapshot of the existing Aurora MySQL database and share the snapshot with the target AWS account. Restore the database from the snapshot in the target account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** D, E

🔑 **Key words:** move Lambda + Aurora to another account, same org + Region; least downtime

🪤 **Your trap:** Snapshot share + restore = slower

🧠 **Rule:** Aurora cross-account copy fast → share cluster via RAM + Aurora clone.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Source Account                       Target Account
┌───────────────────────┐            ┌───────────────────────┐
│ Lambda (ZIP trên S3)  │   ──────►  │ Lambda ?              │
│ Aurora MySQL cluster  │   ──────►  │ Aurora MySQL ?        │
└───────────────────────┘            └───────────────────────┘
        Cùng Organization, cùng Region
        Yêu cầu: downtime ÍT NHẤT
```

Phải chọn **một cách cho Lambda** và **một cách cho Aurora**. Đáp án đúng: **A (Aurora clone qua RAM)** + **D (tạo lại Lambda từ ZIP)**. Anh chọn đúng D, sai ở phần database (chọn E – snapshot).

#### Phần Lambda — D đúng, C sai

**C sai vì Lambda không chia sẻ được qua RAM.** RAM chỉ hỗ trợ một danh sách resource nhất định (subnet, Transit Gateway, Route 53 Resolver rules, License Manager, Aurora DB cluster…). Lambda function không nằm trong danh sách. Hơn nữa, "share" không phải "migrate" — function vẫn thuộc account nguồn.

**D đúng** vì Lambda thực chất chỉ là code + cấu hình. Code đã có sẵn trong file ZIP:

```
Tải ZIP từ S3 account nguồn
    → upload vào S3 bucket account đích
    → create-function trong account đích, trỏ đến ZIP đó
    → tạo lại execution role, env vars, trigger, VPC config
```

#### Phần Aurora — Vì sao Clone (A) nhanh hơn Snapshot (E)

Mấu chốt là hiểu **Aurora tách compute và storage** (storage phân tán 6 bản copy trên 3 AZ).

**Aurora Clone — copy-on-write:**

```
Cluster nguồn                      Clone (account đích)
     │                                  │
     └──────────► Storage volume ◄──────┘
                  (DÙNG CHUNG các trang dữ liệu)

Lúc tạo clone:
    → Không copy data
    → Tạo xong nhanh, KHÔNG phụ thuộc kích thước DB
Sau đó:
    → Bên nào ghi thay đổi thì mới tạo trang mới riêng cho bên đó
```

Cross-account clone: account nguồn **share cluster qua RAM** cho account đích → account đích tạo clone từ cluster được share. (RAM cũng share được cho account ngoài Organization, nhưng khi đó account đích phải chấp nhận lời mời; trong cùng Organization thì đơn giản hơn.)

**Snapshot share + restore (E):** tạo snapshot → share → restore thành cluster mới với volume mới → chậm hơn clone. Snapshot phù hợp hơn khi cần **cross-region** hoặc backup lâu dài; clone chỉ trong cùng region.

**mysqldump (B) chậm nhất:** export/import logic từng câu lệnh; `--single-transaction` cho bản dump nhất quán nhưng dữ liệu ghi sau đó vẫn bị thiếu → vẫn phải dừng ghi khi cutover.

| Cách | Cơ chế | Tốc độ | Phụ thuộc kích thước DB |
|---|---|---|---|
| **A. Clone qua RAM** | Copy-on-write, dùng chung storage | Nhanh nhất | Không |
| E. Snapshot + restore | Chụp → share → dựng cluster mới | Trung bình | Có |
| B. mysqldump | Export/import logic | Chậm nhất | Rất nhiều |

#### Lưu ý thực tế (đề không hỏi nhưng dễ vấp)

- **Mã hóa KMS:** cluster/snapshot mã hóa bằng **AWS managed key (aws/rds)** không share cross-account được → phải dùng **customer managed key** và cấp quyền key cho account đích.
- **Clone là bản chụp tại một thời điểm:** cutover thực tế: dừng ghi ngắn → clone → trỏ Lambda mới vào clone. Cần gần zero downtime → thêm **binlog replication** từ nguồn sang clone rồi mới cắt chuyển.

#### Quy tắc nhớ cho thi

- **"copy Aurora sang account khác, cùng region, nhanh nhất"** → **share cluster qua RAM + Aurora clone**
- **"cross-region" / "long-term backup"** → **snapshot**
- **"mysqldump / pg_dump"** → gần như luôn là đáp án chậm nhất
- **"share Lambda via RAM"** → sai, RAM không hỗ trợ Lambda
- **"encrypted cross-account"** → cần **customer managed KMS key**

### TD explanation

Amazon Aurora cloning allows you to create a new cluster that uses the same Aurora cluster volume and has the same data as the original. The process is designed to be fast and cost-effective. The new cluster with its associated data volume is called a clone.

Creating a clone is faster and more space-efficient than physically copying the data using other techniques, such as restoring from a snapshot like you would in Amazon RDS or using the native mysqldump utility.

AWS Resource Access Manager (AWS RAM) is a service that enables you to securely share your AWS resources across AWS accounts or within your organization. It simplifies the resource and policy management required for sharing resources, ensuring that only intended accounts have access to shared items. It’s important to note that only certain types of resources can be shared using AWS RAM, and a list of these resources is available on the AWS documentation.

In the scenario, by using AWS RAM to share the existing Aurora MySQL DB cluster with the target account, the database can be cloned swiftly in the target account. This cloning process is recommended for cross-account migrations within the same AWS region. Moreover, for the Lambda function, the ZIP deployment package can be downloaded and uploaded to the S3 bucket in the target AWS account. A new Lambda function can then be created using this deployment package.

Therefore, the correct answers are:

– Use AWS Resource Access Manager (AWS RAM) to share the Aurora MySQL DB cluster with the target AWS account. Create an Aurora clone in the target account.

– Download the ZIP deployment package and upload it to the target account’s S3 bucket. Create a new Lambda function in the target account using the ZIP package.

The option that says: Use the mysqldump utility to export the data and schema from the Aurora MySQL database into a SQL dump file. Transfer the SQL dump file to the target AWS account and import it into a newly created Aurora MySQL database instance is incorrect. This approach is more time-consuming, particularly for large databases. Restoring from a SQL dump file into a newly created Aurora MySQL database instance in the target account would also require additional time, extending the duration of the migration process.

The option that says: Create a snapshot of the existing Aurora MySQL database and share the snapshot with the target AWS account. Restore the database from the snapshot in the target account is incorrect. While restoring from a snapshot is a viable method for data migration, sharing the snapshot won’t be helpful in this scenario as both the source and target accounts are within the same organization and AWS region already. Performing Aurora Cloning via AWS RAM offers a quicker approach since the source and target accounts are in the same AWS region.

The option that says: Use AWS Resource Access Manager (AWS RAM) to share the Lambda function with the target account is incorrect because AWS AWS RAM does not support direct sharing of Lambda functions between accounts.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.html

https://aws.amazon.com/blogs/aws/amazon-aurora-fast-database-cloning/

https://aws.amazon.com/blogs/database/cross-account-amazon-aurora-mysql-migration-with-aurora-cloning-and-binlog-replication-for-reduced-downtime/

 

Check out this Amazon Aurora Cheat Sheet:

https://tutorialsdojo.com/amazon-aurora/

</details>

<a id="q62"></a>

## Q62

An organization uses AWS Organizations and the Organizations API to manage its IT resources across multiple member accounts. The management account occasionally uses the RemoveAccountFromOrganization operation to detach member accounts when necessary. In addition, the organization deploys virtual appliances as part of its centralized networking strategy. The appliances are critical for the company’s network security and must scale dynamically to meet fluctuating traffic demands. The virtual appliances operate in a centralized networking account connected through a transit gateway to various member account VPCs.

Recently, a misconfigured script accidentally terminated all instances of the virtual appliances, causing operational downtime. In response, the organization revised the startup scripts for the appliances to enhance resilience and scalability.

A solutions architect must find a solution to efficiently scale the virtual appliances horizontally, ensure secure and private connections across accounts, and minimize manual configuration.

Which combination of steps will meet these requirements? (Select TWO.)

- **A.** Configure VPC peering between the centralized networking account and member accounts to streamline network traffic routing.
- **B.** Use an Application Load Balancer to distribute traffic to the virtual appliances based on demand.
- **C.** Set up an Auto Scaling group using a launch template with the updated script as user data to automate the configuration of virtual appliances, linking to a target group with instance-based targets.
- **D.** Provision a Gateway Load Balancer within the centralized networking account and integrate it with an endpoint service via AWS PrivateLink for secure traffic routing.
- **E.** Implement AWS Direct Connect to establish a dedicated network connection between the centralized networking account and member account VPCs.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D · **You picked:** D, E

🔑 **Key words:** virtual appliances; scale dynamically; centralized networking account via TGW

🪤 **Your trap:** Direct Connect = on-prem link, not appliance scaling

🧠 **Rule:** Scalable 3rd-party appliances → Gateway Load Balancer (+ PrivateLink endpoint) + ASG launch template.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Centralized networking account
    └─ Virtual appliances (firewall/IPS ảo, third-party)
         │
         ▼ Transit Gateway
    Member account VPCs (nhiều account trong Organization)

Sự cố gần đây: script lỗi → terminate hết appliance instances → downtime
Sau sự cố: đã cải tiến startup script cho resilient/scalable hơn

Yêu cầu MỚI:
    1) Scale appliance HORIZONTALLY (ngang) linh hoạt theo traffic
    2) Kết nối SECURE & PRIVATE giữa các account
    3) TỐI THIỂU cấu hình thủ công
```

Chọn **HAI (2)** đáp án đúng: **C, D**. Anh chọn **D, E** — đúng D, sai E.

#### Vì sao C và D đúng — đúng bộ đôi cho kiến trúc virtual appliance

```
D: Gateway Load Balancer (GWLB) trong centralized networking account
      + tích hợp Endpoint Service qua AWS PrivateLink
   → GWLB hoạt động ở Network Layer (OSI layer 3)
   → chuyên dùng để phân phối traffic đến virtual appliance
     (firewall, IPS, deep packet inspection…)
   → PrivateLink cho phép member account VPC gọi tới appliance
     một cách PRIVATE, không cần internet gateway/NAT/VPN/DX

C: Auto Scaling group + launch template (chứa script mới làm user data)
      + target group với instance-based targets (gắn vào GWLB)
   → Tự động scale số lượng appliance instance theo traffic
   → Launch template = tự động hoá cấu hình mỗi khi có instance mới
     (không cần config tay từng instance — đáp ứng "minimize manual configuration")
```

GWLB + ASG là **kiến trúc chuẩn của AWS cho third-party virtual appliances**: GWLB tự động phân phối traffic vào các appliance instance đứng sau nó, ASG tự động thêm/bớt instance theo demand, và launch template đảm bảo mỗi instance mới lên đều tự cấu hình đúng — không cần con người can thiệp thủ công sau sự cố "misconfigured script terminate all instances" trước đó.

#### Vì sao anh chọn E (Direct Connect) sai

**Direct Connect là kết nối vật lý dedicated giữa mạng on-premises (data center của công ty) và AWS**, không phải công cụ để kết nối **giữa các account/VPC trong cùng AWS Organization**. Đây là bẫy: đề có nhắc "secure and private connections across accounts" khiến dễ liên tưởng tới DX vì DX cũng "private", nhưng DX **không giải quyết bài toán scale appliance, cũng không phải cách kết nối chuẩn giữa VPC-to-VPC nội bộ AWS** — với nhu cầu này, PrivateLink (qua GWLB endpoint service) mới là công cụ đúng.

#### Vì sao A, B sai

- **A — VPC peering:** giúp routing traffic giữa VPC, nhưng **không hỗ trợ scale hay tự động cấu hình appliance**. Đây là giải pháp networking thuần túy, không đáp ứng yêu cầu "scale horizontally" và "minimize manual configuration" của bài toán appliance.
- **B — Application Load Balancer:** ALB hoạt động ở **layer 7 (application layer)**, phù hợp cho HTTP/HTTPS traffic của ứng dụng web, **không phù hợp cho virtual network appliance** (firewall/IPS) vốn cần xử lý mọi loại traffic ở layer 3/4 và giữ nguyên thông tin gói tin gốc (GENEVE encapsulation của GWLB). ALB không có cơ chế này.

| Phương án | Vấn đề |
|---|---|
| **C** | Đúng: ASG + launch template tự động scale & cấu hình |
| **D** | Đúng: GWLB + PrivateLink cho secure/private routing |
| A | VPC peering không scale/tự động hóa appliance |
| B | ALB là layer 7, sai loại load balancer cho network appliance |
| E | Direct Connect dùng cho on-prem ↔ AWS, không phải account-to-account trong AWS |

#### Quy tắc nhớ cho thi

- **"virtual appliance / firewall / IPS ảo cần scale + traffic layer 3"** → **Gateway Load Balancer** (không phải ALB/NLB)
- **"kết nối private tới appliance từ nhiều account/VPC khác"** → **GWLB endpoint + AWS PrivateLink**
- **"tự động scale + tự động cấu hình, giảm thao tác tay"** → **Auto Scaling group + launch template (user data)**
- **Direct Connect** → chỉ dùng khi cần nối **on-premises ↔ AWS**, không phải giải pháp cho kết nối nội bộ giữa các AWS account
- Thấy "Application Load Balancer" đi cùng bối cảnh network/security appliance → gần như luôn là đáp án nhiễu, đúng phải là Gateway Load Balancer

### TD explanation

A Gateway Load Balancer operates at the network layer (layer 3) of the OSI model to distribute traffic to virtual appliances like firewalls and intrusion prevention systems. Gateway Load Balancer Endpoints provide private connectivity between appliances in one VPC and servers in another VPC.

PrivateLink enables private connectivity between VPCs and AWS services without an internet gateway, NAT device, VPN connection, or AWS Direct Connect. Interface endpoints provide a private IP address from your VPC that acts as an entry point for the service.

An Auto Scaling group is a collection of EC2 instances that are managed together by Auto Scaling. It ensures the number of instances matches the target capacity. Auto Scaling groups can be configured to scale based on metrics, schedules or other triggers.

To provide scalability of virtual appliances while maintaining consistent security policies across different accounts, a solutions architect should use a combination of Gateway Load Balancer, AWS PrivateLink, and Auto Scaling group. The Gateway Load Balancer would distribute traffic to the virtual appliances, allowing them to scale horizontally behind the load balancer as traffic increases. Using AWS PrivateLink, the virtual appliances would be accessible to other accounts in a private and secure manner without exposing them publicly. Configuring an Auto Scaling group with the updated startup script would enable automatic scaling of the virtual appliance instances, linking to a target group associated with the Gateway Load Balancer. Together, these steps would eliminate manual work and provide scalability of the appliances, along with secure and private connections across accounts.

Hence, the correct answers are:

– Set up an Auto Scaling group using a launch template with the updated script as user data to automate the configuration of virtual appliances, linking to a target group with instance-based targets.

– Provision a Gateway Load Balancer within the centralized networking account and integrate it with an endpoint service via AWS PrivateLink for secure traffic routing.

The option that says: Implement AWS Direct Connect to establish a dedicated network connection between the centralized networking account and member account VPCs is incorrect because AWS Direct Connect primarily facilitates a dedicated network link between the AWS environment and an organization’s data center, not specifically for scaling virtual appliances within AWS.

The option that says: Configure VPC peering between the centralized networking account and member accounts to streamline network traffic routing is incorrect. While VPC peering typically helps in traffic routing between VPCs, it does not aid in scaling or automated configuration of virtual appliances.

The option that says: Use an Application Load Balancer to distribute traffic to the virtual appliances based on demand is incorrect because an Application Load Balancer is more suitable for application-level traffic management and does not specifically cater to the unique requirements of network appliances or inter-VPC network security and routing capabilities that a Gateway Load Balancer offers.

 

References:

https://aws.amazon.com/blogs/publicsector/implementing-third-party-firewall-appliances-aws-comparing-two-methods/

https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-gateway-load-balancer/

https://tutorialsdojo.com/aws-auto-scaling/

</details>

---

# Group C — DR / Route 53 (5)

<a id="q9"></a>

## Q9

An organization is redesigning its application to a multi-region architecture to enhance disaster recovery and high availability. The application’s infrastructure, which includes an Amazon RDS for MySQL database, is managed across primary and secondary regions using AWS CloudFormation. The architecture must meet a Recovery Time Objective (RTO) of 30 minutes and a Recovery Point Objective (RPO) of 1 hour. The application’s traffic is managed using Amazon Route 53.

What combination of actions should a Solutions Architect take to meet the requirements? (Select TWO.)

- **A.** Create a cross-region read replica of the Amazon RDS for the MySQL database in the secondary region. Promote the cross-region RDS for MySQL database read replica automatically via an AWS Lambda Function.
- **B.** Create an AWS Lambda function to backup the database to S3 in the secondary region every hour. Create Amazon Route 53 to perform health checks and redirect traffic to the standby database if the primary database fails.
- **C.** Create a Route 53 failover policy for the database DNS record with the primary database endpoint as the main and the read replica endpoint as backup.
- **D.** Provision an additional RDS instance in the primary region for redundancy, configuring bi-directional replication between it and the primary database.
- **E.** Create an AWS Lambda function to perform database health checks. If a failure is detected, restore the latest snapshot from the secondary region and update Route 53 DNS records accordingly.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C · **You picked:** B, E

🔑 **Key words:** multi-Region DR; RDS MySQL; RTO 30 min; RPO 1 h; Route 53

🪤 **Your trap:** Snapshot/S3 restore > 30 min

🧠 **Rule:** RTO < ~1 h → cross-Region read replica + automated promotion + Route 53 failover record.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Primary Region                         Secondary Region
┌─────────────────────┐                ┌─────────────────────┐
│ RDS MySQL (primary)  │  async repl.  │ RDS MySQL read       │
│                       │ ─────────────►│ replica (cross-region)│
└─────────────────────┘                └─────────────────────┘
        ▲                                        ▲
        └──────────── Route 53 (DNS record) ─────┘
Yêu cầu: RTO 30 phút · RPO 1 giờ
```

Đề chọn HAI hành động. Đáp án đúng: **A** (cross-region read replica + tự động promote bằng Lambda) và **C** (Route 53 failover policy: primary là main, read replica là backup). Anh chọn **B, E** — cả hai đều dựa trên snapshot/backup phục hồi, không phải một database đang chạy sẵn.

#### Vì sao A đúng, E và B sai

Cốt lõi của câu này là phân biệt giữa **"có sẵn một bản sao database đang chạy"** và **"phải phục hồi từ bản sao lưu"**:

- **A — Cross-region read replica:** đây là một **instance database đang chạy thật sự** ở region phụ, nhận dữ liệu replicate bất đồng bộ liên tục từ primary. Khi có sự cố, chỉ cần **promote** (chuyển từ read replica thành standalone/primary) — thao tác này diễn ra trong vài phút, không phải khởi tạo lại từ đầu. Điều này đáp ứng RTO 30 phút.
- **E — Restore từ snapshot:** phải chờ Lambda phát hiện lỗi, sau đó **restore toàn bộ snapshot** thành một instance mới — quá trình này gần như luôn vượt quá 30 phút với DB có kích thước thực tế.
- **B — Backup ra S3 mỗi giờ + Route 53 health check:** backup ra S3 không phải là một database instance có thể phục vụ traffic ngay. Muốn dùng được, vẫn phải restore từ backup đó → cũng vượt RTO.

**D sai** vì "bi-directional replication" giữa hai RDS instance trong cùng primary region không phải là tính năng chuẩn của RDS, dễ gây xung đột dữ liệu (write conflict) và không giải quyết được yêu cầu multi-region.

#### Vai trò của Route 53 (đáp án C)

Route 53 **failover routing policy** cấu hình active-passive: bản ghi chính trỏ đến primary DB endpoint, bản ghi backup trỏ đến read replica endpoint. Route 53 dùng health check để tự động chuyển traffic sang backup khi primary "unhealthy" — đúng nghĩa DR chứ không phải chỉ định tuyến theo độ trễ hay tỷ trọng.

| Cách | Có sẵn instance chạy? | Thời gian phục hồi | Đáp ứng RTO 30' |
|---|---|---|---|
| **A. Cross-region read replica + promote** | Có | Vài phút (chỉ promote) | Đạt |
| E. Restore snapshot | Không | Thường > 30 phút | Không đạt |
| B. Restore S3 backup | Không | Thường > 30 phút | Không đạt |
| D. Bi-directional replication trong cùng region | — | Không phải giải pháp multi-region | Không đạt |

#### Quy tắc nhớ cho thi

- **RTO ngắn (dưới ~1 giờ)** → cần một **database đang chạy sẵn** ở nơi backup (read replica), không phải backup tĩnh (snapshot/S3).
- **"promote read replica"** → thao tác nhanh, khác hẳn "restore from snapshot" (chậm).
- **Route 53 failover routing policy** = active-passive DR, khác với latency-based (chọn gần nhất) hay weighted (chia tỷ lệ).
- **"bi-directional replication" giữa 2 RDS** → gần như luôn là bẫy, RDS không hỗ trợ chuẩn.

### TD explanation

AWS Lambda is a service that enables you to write and execute code without worrying about managing servers. You can write Lambda functions in Node.js, Python, Java, and other languages.

Amazon RDS is an AWS database service for setting up, operating, and scaling relational databases like MySQL, MariaDB, Oracle, SQL Server, and PostgreSQL in the cloud.

A cross-region read replica is a read-only copy of the source database that is replicated to a different AWS region. This allows serving reads from the secondary region for lower latency and acts as a disaster recovery solution if the primary region goes down. The replication is asynchronous and cross-region read replicas can be created for MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server databases on Amazon RDS.

Amazon Route 53 is a highly scalable and available DNS service provided by AWS. Route 53 can be used for domain registration, where you can register domain names and select domain registrars. It also provides DNS routing capabilities, where you can route traffic to different resources like web servers, load balancers, etc., based on various factors.

Some common routing policies in Route 53 include simple routing to direct traffic to a single resource, failover routing to configure active-passive failover for high availability, latency routing to route traffic to regions providing the lowest latency, and weighted routing to distribute traffic among multiple resources in specified proportions.

To create a highly available architecture that meets specified RTO and RPO requirements, the Solutions Architect should create a cross-region read replica of the Amazon RDS for MySQL database in the secondary region. This would allow serving reads from that region to improve latency for users there. Promoting the read replica automatically via an AWS Lambda function would enable failing over to the secondary region in case of a primary region outage, meeting the 30-minute RTO. Additionally, configuring a Route 53 failover policy with the primary database endpoint as the main and read replica endpoint as backup would route traffic to the available region based on health checks, improving availability.

Hence, the correct answers are:

– Create a cross-region read replica of the Amazon RDS for the MySQL database in the secondary region. Promote the cross-region RDS for MySQL database read replica automatically via an AWS Lambda Function.

– Create a Route 53 failover policy for the database DNS record with the primary database endpoint as the main and the read replica endpoint as backup.

The option that says: Create an AWS Lambda function to backup the database to S3 in the secondary region every hour. Create Amazon Route 53 to perform health checks and redirect traffic to the standby database if the primary database fails is incorrect because backing up the database to S3 does not provide a live database instance that can serve traffic immediately after a failover. The time to restore a database from an S3 backup would likely exceed the specified RTO.

The option that says: Create an AWS Lambda function to perform database health checks. If a failure is detected, restore the latest snapshot from the secondary region and update Route 53 DNS records accordingly is incorrect as the time to restore from a snapshot typically exceeds 30 minutes, thus failing to meet the RTO requirement.

The option that says: Provision an additional RDS instance in the primary region for redundancy, configuring bi-directional replication between it and the primary database is incorrect. While it suggests redundancy, the use of bi-directional replication is not a standard practice with Amazon RDS and can lead to data conflicts.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

https://tutorialsdojo.com/aws-lambda/

https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q61"></a>

## Q61

A forecasting agency is struggling to meet the Service Level Agreement (SLA) of its online platform. To avoid penalties and maintain credibility, they aim to develop a recovery plan that assures a Recovery Time Objective (RTO) of no more than 30 minutes.

Their platform runs on an Auto Scaling Group (ASG) connected to an Application Load Balancer (ALB). Data is stored in an Amazon RDS PostgreSQL database. An identical environment exists in a secondary region where the ASG’s capacity limits are set to zero. A read replica of the RDS database is deployed in this backup region as well. A Route 53 alias record is configured to route domain traffic to the ALB.

The agency cannot afford an active-active failover and is opting for a more cost-effective way of switching over to the backup region.

Which strategy would meet these requirements?

- **A.** Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Set up a CloudWatch alarm that triggers the function when the HTTPCode_ELB_502_Count ALB metric becomes greater than or equal to 1.
- **B.** Set up an Amazon CloudWatch alarm that tracks the HTTPCode_Target_5XX_Count metric of the ALB in the primary Region. Create a secondary Route 53 record with identical values as the primary record. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Route 53 health check that sends an Amazon SNS notification to a Lambda function that will promote the read replica to the primary.
- **C.** Update the routing policy of the alias record to Weight with a value of 100. Create a new alias record for the application’s domain with a Weight routing policy initialized to 0. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Lambda function for weight adjustment and read replica promotion. Set up a Route 53 health check that sends an Amazon SNS notification to the Lambda function.
- **D.** Add a failover policy in the alias record to redirect traffic to the Application Load Balancer in the secondary Region. Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Monitor the application status with a Route 53 health check that uses Amazon SNS to invoke the Lambda function when the application becomes unhealthy.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** RTO ≤ 30 min; secondary ASG capacity 0; read replica in DR Region

🪤 **Your trap:** Weighted routing ≠ failover

🧠 **Rule:** Pilot light → Route 53 failover policy + Lambda scales ASG + promotes replica.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Primary Region                         Secondary Region (pilot light)
┌───────────────────────┐              ┌───────────────────────┐
│ ASG (đầy đủ capacity)  │              │ ASG (capacity = 0)     │
│ ALB                    │              │ ASG giống hệt cấu hình │
│ RDS PostgreSQL (primary)│ ──repl.───► │ Read replica RDS       │
└───────────────────────┘              └───────────────────────┘
              ▲
        Route 53 alias record → ALB
Yêu cầu: RTO ≤ 30 phút, KHÔNG active-active (tiết kiệm chi phí)
```

Đáp án đúng: **D**. Anh chọn **C** (weighted routing).

#### Vì sao D đúng

Đây chính là mô hình DR **pilot light**: hạ tầng phụ tồn tại sẵn nhưng ở trạng thái "tắt bớt" (ASG capacity = 0), chỉ "bật lên" (scale up + promote replica) khi có sự cố — rẻ hơn active-active nhưng vẫn nhanh hơn build lại từ đầu.

D dùng đúng cơ chế cho việc này:
- **Route 53 failover routing policy** trên alias record → đúng nghĩa active-passive, mặc định trỏ ALB primary, tự chuyển sang ALB secondary khi primary unhealthy.
- **Lambda** được trigger qua **Route 53 health check → SNS → Lambda** để: (1) tăng capacity limits của ASG ở secondary region, (2) promote read replica thành primary.
- Cách này không tốn chi phí chạy song song (vì ASG secondary capacity = 0 lúc bình thường).

#### Vì sao C (anh chọn) sai

C dùng **Weighted routing** (100/0) rồi đổi trọng số khi failover: đây thực chất mô phỏng failover bằng weighted policy — không cần thiết vì Route 53 đã có **failover routing policy chuyên dụng**, đơn giản và nhanh hơn (weighted routing về bản chất không phải cơ chế health-check chủ động chuyển hẳn traffic, mà là chia tỷ trọng — thao tác đổi trọng số qua Lambda tốn thêm bước, có thể làm chậm RTO). Weighted routing phù hợp cho A/B testing hoặc canary release hơn là failover.

#### Vì sao các phương án khác sai

- **A** — CloudWatch alarm trên metric `HTTPCode_ELB_502_Count` quá cụ thể, không bao quát được mọi kiểu lỗi khiến ứng dụng "unhealthy" (timeout, 5xx khác, DB down mà không sinh 502...).
- **B** — Record thứ hai có **cùng giá trị, cùng routing policy** với record chính, cộng thêm ASG secondary được set full capacity ngay từ đầu → đây là kiến trúc **active-active**, đi ngược yêu cầu "không active-active, cần tiết kiệm chi phí".

| Phương án | Cơ chế chuyển traffic | Kiến trúc | Phù hợp yêu cầu? |
|---|---|---|---|
| **D. Failover routing + Lambda scale/promote** | Health check → failover record | Pilot light | Đạt |
| C. Weighted routing đổi trọng số | Đổi weight qua Lambda | Pilot light nhưng cơ chế sai | Không tối ưu |
| B. Record giống hệt + ASG full capacity | Cả 2 luôn active | Active-active | Sai yêu cầu chi phí |
| A. CloudWatch alarm 502 | Alarm hẹp, thiếu bao quát | Pilot light | Không đáng tin cậy |

#### Lưu ý thực tế

- Route 53 hỗ trợ **active-active** (dùng bất kỳ routing policy nào khác failover, kết hợp health check) và **active-passive** (dùng đúng failover routing policy).
- Với DR chi phí thấp (pilot light/warm standby), luôn tìm "failover routing policy", không phải weighted hay latency.

#### Quy tắc nhớ cho thi

- **"Không active-active", "cost-effective DR", "ASG capacity = 0"** → pilot light → **Route 53 failover routing policy**.
- **Weighted routing** → dùng cho canary/A-B test, không phải cơ chế failover chính thống.
- CloudWatch alarm dựa trên **một mã lỗi HTTP cụ thể** → thường là bẫy vì không bao quát đủ tình huống lỗi.

### TD explanation

On Amazon Route 53, after you create a hosted zone for your domain, such as tutorialsdojo.com, you create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain. You can create a record that points to the DNS name of your Application Load Balancer on AWS.

When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:

Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.

Failover routing policy – Use when you want to configure active-passive failover.

Geolocation routing policy – Use when you want to route traffic based on the location of your users.

Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.

Latency routing policy – Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.

Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.

Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify.

You can use Route 53 health checks to configure active-active and active-passive failover configurations. You configure active-active failover using any routing policy (or combination of routing policies) other than failover, and you configure active-passive failover using the failover routing policy.

In the scenario, an active-passive failover can be achieved by adding a failover policy to the existing record. This policy will redirect traffic to the Application Load Balancer in the secondary region when the primary application becomes unhealthy. A Lambda function is used to increase the Auto Scaling Group’s capacity limits in the secondary region and to promote the RDS read replica to become the primary database. The application’s health status is monitored by a Route 53 health check, which uses Amazon SNS to invoke the Lambda function in case of any issues. This strategy ensures a swift response to application failures, meeting the required Recovery Time Objective (RTO) in a cost-effective manner.

Therefore, the correct answer is: Add a failover policy in the alias record to redirect traffic to the Application Load Balancer in the secondary Region. Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Monitor the application status with a Route 53 health check that uses Amazon SNS to invoke the Lambda function when the application becomes unhealthy.

The option that says: Create a Lambda function that updates the ASG’s capacity limits and promotes the read replica to primary in the secondary Region. Set up a CloudWatch alarm that triggers the function when the HTTPCode_ELB_502_Count ALB metric becomes greater than or equal to 1 is incorrect. This ALB metric is too specific and may not cover all the potential reasons for a failover. The application could become unhealthy due to various other reasons not related to HTTP 502 errors. Therefore, this solution does not provide comprehensive coverage for application health monitoring.

The option that says: Update the routing policy of the alias record to Weight with a value of 100. Create a new alias record for the application’s domain with a Weight routing policy initialized to 0. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Lambda function for weight adjustment and read replica promotion. Set up a Route 53 health check that sends an Amazon SNS notification to the Lambda function is incorrect. This is not cost-effective since you’re constantly running and paying for a minimal capacity in the secondary region. The process of adjusting weights also could potentially delay the recovery time, affecting the desired RTO.

The option that says: Set up an Amazon CloudWatch alarm that tracks the HTTPCode_Target_5XX_Count metric of the ALB in the primary Region. Create a secondary Route 53 record with the same name, the same type, and the same routing policy as the primary record. Adjust the Auto Scaling Group (ASG) in the secondary Region to match the capacity limits of the ASG in the primary Region. Create a Route 53 health check that sends an Amazon SNS notification to a Lambda function that will promote the read replica to primary is incorrect. This option actually suggests an active-active setup, where both environments are running simultaneously. In this setup, Route 53’s health checks would monitor both environments and if one becomes unhealthy, Route 53 will route traffic only to the healthy environment. This setup costs a lot more since two environments are running at the same time. The scenario specifically mentioned that the agency cannot afford an active-active failover and is opting for a more cost-effective way of switching over to the backup region.

 

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html

https://aws.amazon.com/blogs/networking-and-content-delivery/manual-failover-and-failback-strategy-with-amazon-route53/

 

Check out the Amazon Route 53 Cheat Sheet:

https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q42"></a>

## Q42

An e-commerce company runs its website on Amazon EC2 instances. Each of the two AWS Regions has its own set of instances managed by an Application Load Balancer (ALB). The company wants to ensure that customers are served by the closest region for the fastest response times. Customers should be served from the other Region if the website becomes unavailable in the closest Region.

Which of the following solutions should be implemented?

- **A.** Create geolocation-based routing records in Amazon Route 53 to direct users to the nearest ALB and rely on periodic Amazon Route 53 health checks to remove an ALB from service during outages.
- **B.** Configure an Amazon Route 53 health check for each Region and use a Route 53 failover routing record with Evaluate Target Health enabled to switch traffic only when the primary Region becomes unhealthy.
- **C.** Use Amazon API Gateway in front of both ALBs and configure a regional endpoint to redirect users to the nearest Region.
- **D.** Configure Amazon Route 53 health checks for each ALB and create a Route 53 latency alias record with Evaluate Target Health enabled to route traffic to the closest healthy Region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** serve from CLOSEST Region (fastest); fail over if unavailable

🪤 **Your trap:** Geolocation = location, not latency

🧠 **Rule:** Fastest + failover → latency alias record + Evaluate Target Health (+ health checks).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Region A (gần khách hàng)          Region B
┌──────────────┐                  ┌──────────────┐
│ EC2 + ALB     │                  │ EC2 + ALB     │
└──────────────┘                  └──────────────┘
Yêu cầu: (1) phục vụ khách hàng từ region GẦN NHẤT (nhanh nhất)
         (2) nếu region đó "down" → chuyển sang region còn lại
```

Đáp án đúng: **D** (Route 53 health check cho từng ALB + **latency alias record** + **Evaluate Target Health**). Anh chọn **A** (geolocation routing).

#### Vì sao D đúng

Hai yêu cầu tách biệt cần Route 53 xử lý đồng thời:

1. **"Fastest response time" / "closest region"** → đây là bài toán **độ trễ mạng (latency)**, không phải vị trí địa lý. Route 53 giải quyết bằng **latency-based routing**: đo latency thực tế giữa user và các region đã có latency record, chọn region trả lời nhanh nhất.
2. **"Failover nếu region đó down"** → bật **Evaluate Target Health** trên latency alias record: Route 53 sẽ kiểm tra sức khỏe target (ALB) trước khi route, nếu region gần nhất unhealthy thì tự động chuyển sang region khỏe còn lại — cơ chế failover "gắn kèm" ngay trong latency routing, không cần policy riêng.

Kết hợp cả hai trong **latency alias record + Evaluate Target Health + health checks cho từng ALB** = D.

#### Vì sao A (anh chọn) sai

**Geolocation routing định tuyến theo vị trí địa lý (IP mapping ra khu vực), không theo độ trễ mạng thực tế.** Một khách hàng có thể "gần" về địa lý nhưng đường mạng lại có latency cao hơn region khác (ví dụ do tuyến cáp, peering). Đề bài yêu cầu rõ "fastest response times" — đây là latency, geolocation không đảm bảo điều đó. Geolocation phù hợp hơn cho các use-case cần kiểm soát nội dung/pháp lý theo khu vực (ví dụ chặn theo quốc gia), không phải tối ưu tốc độ.

#### Vì sao B và C sai

- **B — Failover routing với Evaluate Target Health:** failover routing chỉ hỗ trợ cấu hình **primary/secondary cố định** — traffic luôn đi region primary bất kể latency, chỉ chuyển sang secondary khi primary unhealthy. Không đáp ứng yêu cầu "luôn phục vụ từ region gần nhất".
- **C — API Gateway regional endpoint:** API Gateway không có cơ chế tự động định tuyến người dùng đến region gần nhất; vẫn cần một lớp DNS-based latency routing phía trước, nên bản thân giải pháp này không đủ.

| Routing policy | Cơ sở định tuyến | Có tự failover khi bật Evaluate Target Health? | Phù hợp yêu cầu? |
|---|---|---|---|
| **Latency (D)** | Độ trễ mạng thực tế | Có | Đạt cả 2 yêu cầu |
| Geolocation (A) | Vị trí địa lý IP | Có (health check) nhưng không đảm bảo nhanh nhất | Không đạt yêu cầu "fastest" |
| Failover (B) | Primary/secondary cố định | Có (đúng mục đích của nó) | Không phục vụ theo latency |
| API Gateway regional (C) | Không tự định tuyến theo latency | Không | Thiếu cơ chế |

#### Quy tắc nhớ cho thi

- **"Fastest response time" / "lowest latency" / "closest region"** → **Latency-based routing**, không phải Geolocation.
- **Geolocation routing** → dùng khi cần kiểm soát theo vị trí địa lý/pháp lý, không phải để tối ưu tốc độ.
- **"Evaluate Target Health"** → cờ bật thêm trên bất kỳ routing policy dựa vào alias record để Route 53 bỏ qua target không khỏe, kể cả với latency routing (không chỉ failover routing).
- **Failover routing policy** → chỉ dùng cho active-passive cố định, không cân nhắc độ trễ.

### TD explanation

Amazon Route 53 health checks monitor the health of your resources, such as web servers and email servers. You can specify values that define how you want the health check to work, such as the IP address or domain name of the endpoint that you want Route 53 to monitor, the protocol that you want Amazon Route 53 to use to perform the check, how often you want Route 53 to send a request to the endpoint, and how many consecutive times the endpoint must fail to respond to requests before Route 53 considers it unhealthy. If a health check determines that the underlying resource is unhealthy, Route 53 routes traffic from the associated record. This ensures high availability and failover support for DNS records.

Latency-based routing in Amazon Route 53 allows you to improve performance for your users by serving their requests from the AWS Region that provides the lowest latency. When Route 53 receives a DNS query for your domain or subdomain, it determines which AWS Regions you’ve created latency records for, determines which Region gives the user the lowest latency, and then selects a latency record for that Region. Route 53 responds with the value from the selected record, such as the IP address for a web server. This ensures customers are served by the region closest to them for the fastest response times.

If you enabled the Evaluate Target Health, this causes Route 53 to determine whether there are any healthy resources in a region before trying to route traffic there. If not, Route 53 chooses a healthy resource in the other region.

Hence, the correct answer is: Configure Amazon Route 53 health checks for each ALB and create a Route 53 latency alias record with Evaluate Target Health enabled to route traffic to the closest healthy Region. Latency-based routing ensures customers are directed to the Region with the lowest latency, while health checks with Evaluate Target Health provide automatic failover to the other Region if the closest one becomes unhealthy.

The option that says: Create geolocation-based routing records in Amazon Route 53 to direct users to the nearest ALB and rely on periodic Amazon Route 53 health checks to remove an ALB from service during outages is incorrect because geolocation routing in Route 53 primarily directs traffic based on the user’s IP location mapping to a geographic region, not on actual network latency. This means a customer might be routed to a Region that is geographically closest, but not necessarily the one with the lowest latency.

The option that says: Use Amazon API Gateway in front of both ALBs and configure a regional endpoint to redirect users to the nearest Region is incorrect because API Gateway does not have built-in functionality to route users to the nearest Region. It can expose endpoints regionally, but DNS-based latency routing is still required. This solution does not meet the requirement for automatic latency-based routing and failover.

The option that says: Configure an Amazon Route 53 health check for each Region and use a Route 53 failover routing record with Evaluate Target Health enabled to switch traffic only when the primary Region becomes unhealthy is incorrect because failover routing only supports primary/secondary configurations. It does not consider latency, so customers would always be directed to the primary Region regardless of proximity, which fails the requirement for fastest response times.

 

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html

 

Check out this Amazon Route 53 Cheat Sheet:

https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q20"></a>

## Q20

A global financial institution hosts a critical trading platform in a single AWS Region. The platform uses Amazon EC2 instances behind an Application Load Balancer (ALB) for the front end, an Amazon RDS SQL Server for the database, and an Amazon S3 bucket for storing compliance reports.

The market analysis team performs extensive data analysis on the database, especially during market volatility which impacts platform performance. Regulatory requirements demand data availability and integrity during disasters. A solutions architect must develop a disaster recovery plan that minimizes data loss during regional disruptions and addresses the slowdown caused by the team’s data analysis.

What approach would best satisfy these requirements?

- **A.** Establish a scheduled job that generates snapshots of the RDS DB instance on an hourly basis. Copy the snapshots to another Region. Integrate Amazon ElastiCache with the RDS database. Create AMIs from the EC2 instances and replicate them in another Region. Enable S3 Cross-Region Replication (CRR) to sync data from the primary S3 bucket to a bucket in the other Region. In case of a regional disruption, restore the database from the latest RDS snapshot, launch EC2 instances from the replicated AMIs, set up an ALB to serve the application, and update the application to use the new S3 bucket.
- **B.** In a different AWS Region, establish a read replica of the RDS DB instance. Direct the market analysis team to execute their queries on this read replica. Generate AMIs from the EC2 instances that are running the application frontend and replicate these AMIs to the new Region. Implement S3 Cross-Region Replication (CRR) to duplicate data from the original S3 bucket to a newly created S3 bucket in the new Region. In the event of a disaster, promote the read replica to a standalone DB instance. Create EC2 instances using the replicated AMIs and set up an ALB to serve the application to the end users. Adjust the application settings to reference the new S3 bucket.
- **C.** Take a snapshot of the RDS DB instance and export it to an S3 bucket. Direct the market analysis team to perform their queries on the exported snapshot. Schedule an AWS Lambda function to periodically sync the data from the primary S3 bucket to a new S3 bucket in the alternate Region. Launch EC2 instances and set up an ALB in the alternate Region. Reconfigure the application to access data from the new S3 bucket.
- **D.** Migrate the existing database to Amazon DynamoDB and utilize DynamoDB global tables. Direct the market analysis team to interact with a global table in an alternate Region. Establish an AWS Lambda function that periodically syncs the data of the primary S3 bucket with a secondary S3 bucket in the alternate Region. Initiate EC2 instances and establish an ALB in the alternate Region. Adjust the application’s settings to reference the secondary S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** DR with minimal data loss + analytics slowing primary

🪤 **Your trap:** Migrate to DynamoDB = massive rework

🧠 **Rule:** DR + read offload → cross-Region read replica (analysts query it) + copied AMIs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Single Region (hiện tại)
┌────────────────────────────────────────┐
│ EC2 (frontend) ← ALB                     │
│ RDS SQL Server ← team phân tích query nặng, gây chậm hệ thống │
│ S3 (compliance reports)                  │
└────────────────────────────────────────┘

Yêu cầu:
  1. DR: giảm thiểu mất dữ liệu khi region gặp sự cố
  2. Giải quyết luôn vấn đề: query phân tích của team làm chậm platform
```

Đáp án đúng: **B**. Anh chọn **D** (migrate sang DynamoDB Global Tables).

#### Vì sao B đúng — giải quyết đồng thời 2 vấn đề

B dùng **cross-region read replica của RDS SQL Server**, đây là nước đi "hai trong một":

- **Offload traffic phân tích:** đội market analysis chạy query nặng trực tiếp trên **read replica** ở region khác → không còn cạnh tranh tài nguyên với database chính, giải quyết đúng vấn đề "slowdown caused by data analysis".
- **DR với RPO thấp:** read replica cross-region nhận replication liên tục (gần thời gian thực), khi có sự cố chỉ cần **promote read replica** thành standalone instance — nhanh và ít mất dữ liệu hơn nhiều so với restore từ snapshot.
- Kèm theo: replicate AMI của EC2 frontend sang region mới, và **S3 Cross-Region Replication (CRR)** cho bucket compliance reports.
- Khi có disaster: promote replica → dựng EC2 từ AMI đã replicate → tạo ALB → trỏ ứng dụng sang S3 bucket mới. Đầy đủ tất cả thành phần được khôi phục ở region phụ.

#### Vì sao D (anh chọn) sai

Di chuyển từ RDS SQL Server (relational) sang **DynamoDB (NoSQL)** đúng là có sẵn multi-region redundancy nhờ Global Tables, nhưng đây là một cuộc **migrate kiến trúc database hoàn toàn khác mô hình dữ liệu** — đòi hỏi viết lại schema, query, logic ứng dụng, kiểm thử lại toàn bộ hệ thống trading. Với yêu cầu đề bài chỉ là "thiết kế DR plan", đây là giải pháp quá cồng kềnh, rủi ro cao, không phải lựa chọn thực tế khi đã có RDS đang chạy tốt.

#### Vì sao A và C sai

- **A — Snapshot hàng giờ + copy sang region khác:** RPO tối đa 1 giờ (mất dữ liệu giữa 2 lần snapshot), và quan trọng hơn — **không giải quyết được vấn đề chậm do phân tích dữ liệu** vì team vẫn query trực tiếp trên DB chính. Thời gian phục hồi cũng lâu hơn vì phải restore từ snapshot.
- **C — Export snapshot ra S3, phân tích trên snapshot; Lambda sync S3 định kỳ:** đội phân tích không thể chạy query linh hoạt/tương tác trên file snapshot tĩnh trong S3 — mất khả năng phân tích gần thời gian thực. Đồng bộ S3 định kỳ qua Lambda cũng không đảm bảo khôi phục nhanh khi có sự cố.

| Phương án | Giải quyết slowdown do phân tích? | RPO/RTO | Độ phức tạp |
|---|---|---|---|
| **B. Cross-region read replica** | Có (đội phân tích query trên replica) | Thấp, promote nhanh | Vừa phải |
| A. Snapshot hourly | Không | RPO ~1h, restore chậm | Vừa phải |
| C. Export snapshot ra S3 | Không (không tương tác được) | Restore chậm | Vừa phải |
| D. Migrate sang DynamoDB | Có nhưng đổi cả kiến trúc | Tốt (Global Tables) | Rất cao, rủi ro lớn |

#### Bảng chiến lược DR tổng quát (tham khảo khi gặp dạng câu tương tự)

| Chiến lược | Cơ chế | RTO điển hình | Chi phí |
|---|---|---|---|
| Backup & Restore | Snapshot/backup định kỳ, restore khi cần | Hàng giờ | Thấp nhất |
| Pilot Light | Hạ tầng lõi (DB) chạy sẵn thu nhỏ, phần còn lại tắt (capacity 0) | Vài chục phút | Thấp |
| Warm Standby | Bản sao thu nhỏ chạy sẵn toàn bộ stack, scale lên khi failover | Vài phút | Trung bình |
| Multi-site (Active-Active) | Chạy song song đầy đủ ở nhiều region | Gần như 0 | Cao nhất |

Câu Q20 nằm giữa **Pilot Light** và **Warm Standby**: read replica DB "sống" sẵn (đóng vai trò pilot light cho DB), còn EC2/ALB thì dựng lại từ AMI khi cần (backup & restore cho tier ứng dụng).

#### Quy tắc nhớ cho thi

- **"Analytics/reporting làm chậm DB chính"** → đưa read replica ra để offload, không phải backup/snapshot.
- **DR + cần giảm downtime lẫn data loss, không đổi kiến trúc** → cross-region read replica + promote khi cần, không phải "migrate sang NoSQL" trừ khi đề yêu cầu rõ ràng đổi database.
- **Trước khi chọn "migrate database engine" để giải DR** → luôn kiểm tra xem đề có yêu cầu giữ nguyên hệ thống hiện tại không; nếu chỉ cần DR, đây thường là phương án quá mức cần thiết (over-engineering).

### TD explanation

Amazon RDS Read Replica allows you to create one or more read-only copies of your database instance. This can be within the same AWS Region or in a different one. This helps to offload read traffic from the primary database instance, thereby improving the performance of the application.

An Amazon Machine Image (AMI) contains the necessary information to launch a virtual server instance in the cloud. You must specify an AMI when you launch an instance. In the context of the question, AMIs of the EC2 instances that host the application frontend are created and copied to a separate Region.

Amazon S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different AWS Regions. CRR can help ensure that data is available in different regions and can be accessed with minimal latency. In the given scenario, CRR duplicates data from the original S3 bucket to a newly created S3 bucket in the new Region.

In the scenario, by creating a read replica of the RDS SQL Server in a different AWS Region, the analysis team can perform their intensive queries without affecting the primary database’s performance. This setup also enhances disaster recovery capabilities; in the event of a regional disruption, the read replica can be quickly promoted to a standalone DB instance, minimizing downtime and data loss. Additionally, replicating AMIs of the EC2 instances and implementing S3 Cross-Region Replication for compliance reports ensures that all components of the application can be redeployed in the secondary region, maintaining data integrity and availability as per regulatory requirements.

Hence, the correct answer is: In a different AWS Region, establish a read replica of the RDS DB instance. Direct the market analysis team to execute their queries on this read replica. Generate AMIs from the EC2 instances that are running the application frontend and replicate these AMIs to the new Region. Implement S3 Cross-Region Replication (CRR) to duplicate data from the original S3 bucket to a newly created S3 bucket in the new Region. In the event of a disaster, promote the read replica to a standalone DB instance. Create EC2 instances using the replicated AMIs and set up an ALB to serve the application to the end users. Adjust the application settings to reference the new S3 bucket.

The option that says: Migrate the existing database to Amazon DynamoDB and utilize DynamoDB global tables. Direct the market analysis team to interact with a global table in an alternate Region. Establish an AWS Lambda function that periodically syncs the data of the primary S3 bucket with a secondary S3 bucket in the alternate Region. Initiate EC2 instances and establish an ALB in the alternate Region. Adjust the application’s settings to reference the secondary S3 bucket is incorrect. While this setup provides built-in multi-region redundancy, the migration from a relational database system to a NoSQL database could involve substantial changes to the application architecture, potentially introducing significant complexity and compatibility issues.

The option that says: Establish a scheduled job that generates snapshots of the RDS DB instance on an hourly basis. Copy the snapshots to another Region. Integrate Amazon ElastiCache with the RDS database. Create AMIs from the EC2 instances and replicate them in another Region. Enable S3 Cross-Region Replication (CRR) to sync data from the primary S3 bucket to a bucket in the other Region. In case of a regional disruption, restore the database from the latest RDS snapshot, launch EC2 instances from the replicated AMIs, set up an ALB to serve the application, and update the application to use the new S3 bucket. is incorrect because while this could help in a disaster recovery scenario, it won’t much help with the performance issues due to the market analysis team’s operations. Additionally, the recovery time could be longer compared to the correct option, as it involves restoring the database from a snapshot.

The option that says: Take a snapshot of the RDS DB instance and export it to an S3 bucket. Direct the market analysis team to perform their queries on the exported snapshot. Schedule an AWS Lambda function to periodically sync the data from the primary S3 bucket to a new S3 bucket in the alternate Region. Launch EC2 instances and set up an ALB in the alternate Region. Reconfigure the application to access data from the new S3 bucket is incorrect This approach is not practical for a trading platform that requires near-real-time data analysis. Querying directly on exported snapshots does not allow for dynamic or interactive querying capabilities which is important for timely market analysis. Furthermore, the periodic sync of S3 data via Lambda does not enhance the platform’s ability to handle regional disruptions smoothly or efficiently.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html

 

Check out this AWS Disaster Recovery Cheat Sheet:

https://tutorialsdojo.com/aws-well-architected-framework-disaster-recovery/

</details>

<a id="q57"></a>

## Q57

A company has an on-premises data center and uses a single 1 Gbps AWS Direct Connect connection to connect to its cloud resources in the us-east-1 region. The AWS Direct Connect connection uses a single private virtual interface to establish a connection to the VPC in us-east-1. The company has plans to expand and create a new VPC in the us-west-1 region. The solutions architect must design a solution that will add redundancy to the current AWS Direct Connect connection and use the same network to provide connectivity to the new VPC in the new region.

Which of the following should the solutions architect implement to meet the requirements?

- **A.** Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection. Create a Direct Connect gateway. Create a new private virtual interface for each connection and associate them both to the Direct Connect gateway. Create a virtual private gateway for each region’s VPC and connect them to the Direct Connect gateway.
- **B.** Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new public virtual interface for the second connection. Connect the us-west-1 VPC to the new public virtual interface.
- **C.** Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for the second connection. Create virtual private gateways on each VPC and associate both of them to the two private VIFs.
- **D.** Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for each Direct Connect connection. Create a transit gateway for each region’s VPC. Connect both private VIFs to the transit gateways.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** single DX + private VIF; add redundancy; new VPC in another Region

🪤 **Your trap:** One private VIF can't reach VGWs in 2 Regions

🧠 **Rule:** Multi-Region over DX → 2nd DX connection + Direct Connect Gateway + VIF per connection.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises DC
      │
      │ 1x DX connection (1 Gbps) + 1 private VIF
      ▼
   VGW ── VPC (us-east-1)

Yêu cầu:
  1. Thêm redundancy cho DX connection hiện tại
  2. Dùng CÙNG một mạng để kết nối thêm VPC mới ở us-west-1
```

Đáp án đúng: **A**. Anh chọn **C**.

#### Vì sao A đúng

Vấn đề cốt lõi: **một private VIF chỉ liên kết được với virtual private gateway (VGW) của MỘT VPC**, và VGW luôn thuộc về một region cụ thể. Muốn từ on-premises với qua cùng một mạng DX vươn tới VPC ở **region khác**, bắt buộc phải có **Direct Connect Gateway (DXGW)** — tài nguyên global, cho phép một private VIF kết nối tới nhiều VGW ở nhiều region khác nhau.

A thực hiện đúng trình tự:
1. Bỏ private VIF cũ (vì sẽ tái cấu trúc qua DXGW).
2. Thêm DX connection thứ 2 → có redundancy vật lý.
3. Tạo Direct Connect Gateway.
4. Mỗi DX connection có một private VIF riêng, cả hai đều gắn vào DXGW.
5. Mỗi VPC (us-east-1 và us-west-1) có VGW riêng, cả hai VGW đều associate với DXGW.

Kết quả: cả hai DX connection đều có thể vươn tới cả hai VPC qua DXGW → vừa redundant, vừa multi-region trên cùng hạ tầng mạng.

#### Vì sao C (anh chọn) sai

C giữ nguyên private VIF cũ, thêm DX connection thứ 2 với private VIF mới, rồi **gắn VGW của cả hai VPC (2 region) trực tiếp vào 2 private VIF** mà không qua DXGW. Đây là điểm sai: **một private VIF không thể kết nối trực tiếp tới VGW ở một region khác** — private VIF gắn trực tiếp với VGW chỉ hoạt động trong phạm vi region đó. Không có DXGW làm cầu nối, thiết lập này không thể vươn sang us-west-1.

#### Vì sao B và D sai

- **B** — dùng **public VIF** cho VPC us-west-1: public VIF dùng để truy cập các dịch vụ AWS public (S3, DynamoDB endpoint công khai...) qua DX, không dùng để kết nối trực tiếp vào một VPC riêng tư. Kết nối VPC cần private VIF (hoặc transit VIF), không phải public VIF.
- **D** — dùng **Transit Gateway** thay vì VGW: TGW đúng là dùng để kết nối *nhiều VPC trong cùng một region*, và khi kết hợp với DX cần **transit VIF** (không phải private VIF) cùng với DXGW. Ở đây mỗi region chỉ có 1 VPC nên không cần TGW; dùng TGW+private VIF ở đây là sai loại VIF cần thiết.

| Phương án | Có DXGW? | Loại VIF | Kết nối VPC cross-region được không? |
|---|---|---|---|
| **A. DXGW + VGW mỗi region** | Có | Private VIF (2x) | Đạt |
| C. Không qua DXGW | Không | Private VIF (2x) | Không (1 VIF không tới VGW region khác) |
| B. Public VIF cho VPC mới | Không | Public VIF | Sai loại VIF, không dùng cho VPC riêng tư |
| D. Transit Gateway mỗi region | Có | Private VIF (nhưng cần Transit VIF) | Sai loại VIF khi dùng với TGW |

#### Lưu ý thực tế

- Direct Connect Gateway là **global resource**: tạo ở bất kỳ region nào, dùng được từ mọi region khác.
- Quy tắc liên kết: DXGW ↔ VGW (khi 1 VPC/region) dùng **private VIF**; DXGW ↔ Transit Gateway (khi nhiều VPC cùng region) dùng **transit VIF**.

#### Quy tắc nhớ cho thi

- **"Kết nối on-premises tới VPC ở nhiều region qua cùng DX"** → luôn cần **Direct Connect Gateway**.
- **Private VIF** → chỉ nối tới VGW trong cùng region, không tự vươn sang region khác nếu thiếu DXGW.
- **Public VIF** → dùng cho dịch vụ AWS public, không dùng để nối vào VPC riêng.
- **Transit Gateway + DX** → cần **Transit VIF**, không phải private VIF, và chỉ cần khi có nhiều VPC trong cùng một region.

### TD explanation

AWS Direct Connect makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs in the same region.

A Direct Connect gateway is a globally available resource to enable connections to multiple Amazon VPCs across different regions or AWS accounts. This feature also allows you to connect to any participating VPCs from one private VIF, reducing AWS Direct Connect management, as shown in the following figure.

Use AWS Direct Connect gateway to connect your VPCs. You associate an AWS Direct Connect gateway with either of the following gateways:

-A transit gateway when you have multiple VPCs in the same Region

-A virtual private gateway

A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any Region and access it from all other Regions. In the diagram, each VPC has a virtual private gateway that connects to the Direct Connect gateway using a virtual private gateway association. The Direct Connect gateway uses a private virtual interface for the connection to the AWS Direct Connect location. There is an AWS Direct Connect connection from the location to the customer data center.

Therefore, the correct answer is: Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection. Create a Direct Connect gateway. Create a new private virtual interface for each connection and associate them both to the Direct Connect gateway. Create a virtual private gateway for each region’s VPC and connect them to the Direct Connect gateway. A Direct Connect gateway is needed to connect VPCs from separate regions into a single (or redundant) Direct Connect connection using a private virtual interface.

The option that says: Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for the second connection. Create virtual private gateways on each VPC and associate both of them to the two private VIFs is incorrect. You can’t directly connect two virtual private gateways from two different regions to a private VIF. You will need to have a Direct Connect gateway for this.

The option that says: Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for each Direct Connect connection. Create a transit gateway for each region’s VPC. Connect both private VIFs to the transit gateways is incorrect. Transit gateway can be used to connect multiple VPCs from multiple regions, however, you will need a Direct Connect gateway and a transit virtual interface for this, not a private virtual interface.

The option that says: Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new public virtual interface for the second connection. Connect the us-west-1 VPC to the new public virtual interface is incorrect. Depending on the configuration for the VPCs in each region, you will only use a private VIF or a transit VIF to meet the company requirements. You do not need a public VIF. 

 

References:

https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html

https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html

https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html

https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html

 

Check out this AWS Direct Connect Cheat Sheet:

https://tutorialsdojo.com/aws-direct-connect/

</details>

---

# Group D — Migration (7)

<a id="q4"></a>

## Q4

A company operates an on-premises VMware vSphere environment and is now mandated to move certain applications to Amazon EC2 instances. Any software stacks and configurations installed on the VMs must be preserved on the EC2 instances.

Which set of actions will meet the requirements?

- **A.** Export Virtual Machines as an Open Virtualization Format (OVF). Create an S3 bucket in the same AWS Region as the target EC2 instances. Set up an IAM role for the VM Import/Export service. Run the AWS CLI import-image command.
- **B.** Set up AWS Storage Gateway File Gateway on the on-premises VMware environment. Expose a Common Internet File System (CIFS) to share data to an S3 bucket. Run the CreateRestoreImageTask EC2 command.
- **C.** Install the Systems Manager Agent on the on-premises virtual machines and perform hybrid activation to register them as managed instances. Utilize EC2 Image Builder to create a golden AMI that mirrors the on-premises setup. Deploy EC2 instances using the golden AMI.
- **D.** Deploy an AWS DataSync agent to facilitate the synchronization of the on-premises Server Message Block (SMB) share to an S3 bucket. Spin up an EC2 instance and utilize the AWS SDK to access the data stored in the S3 bucket. Create an Amazon Machine Image (AMI) from the configured EC2 instance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** VMware → EC2; preserve software stacks + configuration

🪤 **Your trap:** SSM + Image Builder builds NEW AMI, doesn't preserve VM

🧠 **Rule:** Lift VM as-is → VM Import/Export (export OVF → S3 → import-image).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises                              AWS
┌───────────────────────┐               ┌───────────────────────┐
│ VMware vSphere VM      │   ────────►   │ EC2 instance          │
│ (OS + software stack   │               │ PHẢI giữ nguyên OS,   │
│  + config đã cài sẵn)  │               │ phần mềm, cấu hình    │
└───────────────────────┘               └───────────────────────┘
        Yêu cầu: preserve software stacks & configurations
```

Đây là bài toán "lift-and-shift" kinh điển: không phải build lại server, mà **bê nguyên cái VM đang chạy** sang EC2. Đáp án đúng là **A (VM Import/Export)**. Anh chọn **C (SSM hybrid activation + EC2 Image Builder)** — hướng đi hoàn toàn khác bản chất.

#### VM Import/Export là gì

Đây là dịch vụ chuyên biệt để đưa VM image từ môi trường ảo hóa (VMware, Hyper-V, Xen…) đang có sẵn vào EC2, biến chúng thành EC2 instance sẵn sàng chạy ngay — và ngược lại (export EC2 về on-premises). Vì đây là **import y nguyên**, toàn bộ OS, phần mềm cài đặt, cấu hình hệ thống trong VM được giữ lại.

#### Vì sao A đúng

Quy trình chuẩn:

```
1. Export VM ở on-prem sang định dạng hỗ trợ (OVF/OVA, VHD, VMDK, raw…)
2. Tạo S3 bucket ở đúng Region muốn import EC2 vào
3. Tạo IAM role cấp quyền cho VM Import/Export service truy cập bucket đó
4. Chạy AWS CLI `import-image` → VM image được convert thành EC2 AMI/instance
```

Không có bước "build lại" nào ở đây — image gốc được convert trực tiếp, nên mọi phần mềm/cấu hình cài sẵn trong VM tự động có mặt trên EC2.

#### Vì sao C (đáp án anh chọn) sai

C dùng **SSM hybrid activation + EC2 Image Builder** để tạo "golden AMI mô phỏng lại" cấu hình on-premises. Vấn đề cốt lõi:

- SSM giúp **quản lý** server (automation, patch compliance…), không phải công cụ **import** VM.
- Image Builder **tạo mới** một AMI theo pipeline (cài đặt lại từng phần mềm, từng bước cấu hình) — đây là quá trình **tái tạo**, không phải **di dời nguyên trạng**.
- Việc tái tạo dễ sai lệch: thiếu 1 bản vá, 1 config file, 1 biến môi trường… là đã không còn "preserve" như đề yêu cầu, và tốn nhiều công sức hơn nhiều so với import trực tiếp.

Đây chính là bẫy: SSM + Image Builder nghe có vẻ "chuẩn AWS, dùng dịch vụ quản lý chính thống" nhưng sai bản chất yêu cầu — đề cần **bê nguyên VM**, không cần **dựng lại từ đầu**.

#### Các phương án sai còn lại

- **B (Storage Gateway File Gateway + CreateRestoreImageTask):** File Gateway chỉ để nối storage on-prem với S3 (chia sẻ file qua CIFS/NFS), không import VM. `CreateRestoreImageTask` dùng để khôi phục AMI đã có sẵn trong AWS, không phải để tạo AMI từ VM image bên ngoài.
- **D (DataSync + tự dựng EC2 rồi chụp AMI):** DataSync chỉ đồng bộ **dữ liệu file** (SMB share → S3), không capture được trạng thái/cấu hình của VM. Việc tự dựng EC2 rồi cài SDK để đọc S3 không tái tạo được software stack đã cài trên VM gốc.

| Phương án | Bản chất | Giữ nguyên software stack? |
|---|---|---|
| **A. VM Import/Export** | Convert trực tiếp VM image → EC2 | Có, đầy đủ |
| B. Storage Gateway | Chia sẻ file storage, không phải import VM | Không |
| C. SSM + Image Builder | Dựng lại AMI từ đầu theo pipeline | Không đảm bảo |
| D. DataSync + tự build EC2 | Chỉ đồng bộ dữ liệu file | Không |

#### Quy tắc nhớ cho thi

- **"preserve software stack/configuration as-is" + VMware/Hyper-V → EC2"** → **VM Import/Export** (export OVF → S3 → `import-image`)
- **Image Builder / golden AMI** → dùng khi muốn **chuẩn hóa/tạo mới** AMI, không dùng khi cần giữ nguyên VM gốc
- **DataSync / Storage Gateway** → chỉ giải quyết bài toán **dữ liệu file**, không giải quyết bài toán **di dời cả VM**
- **CreateRestoreImageTask** → phục hồi AMI đã tồn tại trong AWS, không liên quan import từ bên ngoài

### TD explanation

VM Import/Export enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances and export them back to your on-premises environment. This offering allows you to leverage your existing investments in the virtual machines that you have built to meet your IT security, configuration management, and compliance requirements by bringing those virtual machines into Amazon EC2 as ready-to-use instances. You can also export imported instances back to your on-premises virtualization infrastructure, allowing you to deploy workloads across your IT infrastructure.

The general steps for importing using VM Import/Export are as follows:

Export your existing VM using a supported format.
Create an S3 bucket in the Region where you want to import your VMs
Set up an IAM role that gives the VM Import/Export service permission to access the S3 bucket.
Run the AWS CLI import-image command to import the VM image into an EC2 instance.

Hence, the correct answer in this scenario is: Export Virtual Machines as an Open Virtualization Format (OVF). Create an S3 bucket in the same AWS Region as the target EC2 instances. Set up an IAM role for the VM Import/Export service. Run the AWS CLI import-image command.

The option that says: Set up AWS Storage Gateway File Gateway on the on-premises VMware environment. Expose a Common Internet File System (CIFS) to share data to an S3 bucket. Run the CreateRestoreImageTask EC2 command is incorrect. AWS Storage Gateway File Gateway is primarily used for connecting on-premises systems with cloud-based storage. It’s not designed to import VM images and their configurations into EC2, which is what the scenario calls for. Moreover, the CreateRestoreImageTask EC2 command is used for restoring an Amazon Machine Image (AMI), not an imported VM image.

The option that says: Deploy an AWS DataSync agent to facilitate the synchronization of the on-premises Server Message Block (SMB) share to an S3 bucket. Spin up an EC2 instance and utilize the AWS SDK to access the data stored in the S3 bucket. Create an Amazon Machine Image (AMI) from the configured EC2 instance is incorrect. AWS DataSync is simply a data transfer service that makes it easier for you to move data between on-premises storage and Amazon S3 or Amazon EFS. While it’s effective for data synchronization, it doesn’t capture the state or configuration of a VM.

The option that says: Install the Systems Manager Agent on the on-premises virtual machines and perform hybrid activation to register them as managed instances. Utilize EC2 Image Builder to create a golden AMI that mirrors the on-premises setup. Deploy EC2 instances using the golden AMI is incorrect. AWS Systems Manager primarily helps you manage AWS resources and on-premises servers. While it does provide functionalities like automation, configuration, and patch compliance, it does not facilitate the direct import of virtual machines (VMs) from an on-premises environment to EC2 instances. Moreover, creating a golden AMI that mirrors an on-premises setup is a complicated and error-prone process. Even if you manage to create an AMI that is functionally similar, it won’t be a direct import of the on-premises VM. This means there’s a risk that the software stacks and configurations may not be preserved exactly as they are.

 

References:

https://aws.amazon.com/ec2/vm-import/

https://docs.aws.amazon.com/vm-import/latest/userguide/how-vm-import-export-works.html

https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html

</details>

<a id="q32"></a>

## Q32

A company is using an on-premises Windows file server to store 1 TB of data. About 5 GB worth of new data is being produced every day. The company has an AWS Direct Connect connection from the on-premises network to the AWS VPC. As part of the ongoing migration process, about half of its Windows-based workload has been migrated to the AWS cloud. The data stored on the on-premises server needs to be available on a file system for the servers in AWS.

Which of the following options is the recommended migration strategy for this scenario?

- **A.** Create a new Amazon Elastic File System (EFS) share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon EFS. Mount the EFS share on the Windows servers.
- **B.** Create an Amazon S3 bucket on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon S3. Use AWS Transfer Family to access the files.
- **C.** Create an Amazon FSx for Windows File Server share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon FSx.
- **D.** Use AWS Storage Gateway – File Gateway to create an SMB share on the on-premises data center to replace the existing Windows file server. Point the existing file shares to the new file gateway share.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** on-prem Windows file server; data needed by servers in AWS; Direct Connect

🪤 **Your trap:** File Gateway stores data in S3, not a Windows file system in AWS

🧠 **Rule:** Windows files in AWS → FSx for Windows + DataSync scheduled replication.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises Windows                    AWS
┌───────────────────────┐             ┌───────────────────────┐
│ Windows file server    │  Direct    │ ~50% workload đã       │
│ 1 TB data              │  Connect   │ migrate lên AWS        │
│ +5 GB dữ liệu mới/ngày │ ─────────► │ Servers cần TRUY CẬP   │
└───────────────────────┘             │ file system này        │
                                       └───────────────────────┘
Yêu cầu: dữ liệu on-prem PHẢI sẵn có trên một FILE SYSTEM cho server AWS dùng
```

Đáp án đúng là **C (FSx for Windows File Server + DataSync)**. Anh chọn **D (Storage Gateway File Gateway)** — nghe hợp lý vì cũng là giải pháp hybrid storage, nhưng sai vì bản chất dữ liệu cuối cùng nằm ở S3, không phải một Windows file system thật.

#### AWS DataSync là gì

DataSync là dịch vụ chuyển dữ liệu online, dùng để đồng bộ dữ liệu giữa on-premises và AWS (hoặc giữa các dịch vụ storage của AWS với nhau). Nó hỗ trợ nhiều nguồn/đích: NFS, SMB, HDFS, self-managed object storage, S3, EFS, và **FSx for Windows File Server**. Điểm mạnh: có thể lên lịch (scheduled task) để đồng bộ định kỳ — đúng nhu cầu "5 GB dữ liệu mới mỗi ngày" trong đề.

#### Amazon FSx for Windows File Server là gì

Đây là dịch vụ file server Windows được AWS quản lý hoàn toàn, chạy trên **native Windows file system thật** (không phải giả lập). Vì vậy nó hỗ trợ đầy đủ SMB, tính năng NTFS, Active Directory integration — tức là tương thích 100% với ứng dụng Windows đang chạy on-premises, "lift-and-shift" gần như không cần sửa gì.

#### Vì sao C đúng

```
On-prem Windows file server  ──DataSync (daily task)──►  FSx for Windows File Server
                                                                    │
                                                          Windows servers trên AWS
                                                          mount trực tiếp qua SMB
```

FSx for Windows là **file system Windows thật**, có thể mount bằng SMB y như file server gốc. DataSync lo việc đồng bộ định kỳ dữ liệu mới. Khi migration hoàn tất, các server Windows trên AWS dùng ngay FSx share với dữ liệu đã đồng bộ đầy đủ — không gián đoạn.

#### Vì sao D (Storage Gateway File Gateway) sai

File Gateway tạo SMB/NFS share ở phía on-premises, nhưng **dữ liệu thực chất được lưu trong S3** ở background — không phải một Windows file system. Vấn đề: khi toàn bộ workload di chuyển hết lên AWS, công ty vẫn phải dựng **một Windows file server mới** trong AWS để phục vụ SMB cho các server đó, vì S3 (object storage) không đóng vai trò file system cho ứng dụng Windows. Điều này gây gián đoạn ứng dụng — đúng như bẫy đã ghi.

#### Vì sao A và B sai

- **A (EFS):** EFS là file system Linux (NFS), Windows server **không mount NFS mặc định**. Sai công nghệ hoàn toàn cho môi trường Windows.
- **B (S3 + AWS Transfer Family):** S3 là **object storage**, không phải file system — ứng dụng Windows cần giao diện file system (SMB) chứ không phải object API. Transfer Family (SFTP/FTPS) thêm vào chỉ làm phức tạp hóa mà không giải quyết đúng nhu cầu.

| Phương án | Đích lưu trữ | Có phải Windows file system thật? |
|---|---|---|
| **C. FSx for Windows + DataSync** | FSx (native Windows FS) | Có |
| A. EFS + DataSync | EFS (NFS/Linux) | Không — Windows không mount NFS |
| B. S3 + Transfer Family | S3 (object storage) | Không |
| D. Storage Gateway File Gateway | S3 (ẩn sau SMB share) | Không — vẫn cần dựng Windows FS mới sau này |

#### Quy tắc nhớ cho thi

- **"Windows file server cần lift-and-shift lên AWS, giữ SMB"** → **FSx for Windows File Server**
- **"đồng bộ định kỳ on-prem ↔ AWS storage"** → **AWS DataSync** (hỗ trợ NFS/SMB/S3/EFS/FSx)
- **Windows + NFS (EFS)** → sai, Windows không hỗ trợ NFS mặc định
- **File Gateway** → dữ liệu cuối cùng nằm ở **S3**, không phải file system thật — chỉ phù hợp khi ứng dụng chấp nhận object storage phía sau, không phù hợp khi cần Windows FS lâu dài

### TD explanation

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS storage services, and also between AWS storage services. DataSync can copy data between Network File System (NFS), Server Message Block (SMB) file servers, Hadoop Distributed File System (HDFS), self-managed object storage, AWS Snowcone, Amazon Simple Storage Service (Amazon S3) buckets, Amazon EFS file systems, and Amazon FSx for Windows File Server file systems.

Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system. FSx for Windows File Server has the features, performance, and compatibility to easily lift and shift enterprise applications to the AWS Cloud. A Windows file share is a specific folder (and its subfolders) within your file system that you make accessible to your compute instances with SMB.

The primary resources in Amazon FSx are file systems and backups. A file system is where you store and access your files and folders. A file system is made up of one or more Windows file servers and storage volumes. FSx for Windows File Server backups are file-system-consistent, highly durable, and incremental. To ensure file system consistency, Amazon FSx uses the Volume Shadow Copy Service (VSS) in Microsoft Windows.

Therefore, the correct answer is: Create an Amazon FSx for Windows File Server share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon FSx. Amazon FSx for Windows File Server can replicate data between on-premises networks and AWS. Once the whole migration is complete, all Windows-based servers on the cloud can seamlessly use the FSx shares with completely synced data.

The option that says: Create a new Amazon Elastic File System (EFS) share on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon EFS. Mount the EFS share on the Windows servers is incorrect. Windows servers by default do not typically support the mounting of NFS shares.

The option that says: Create an Amazon S3 bucket on the AWS management console. Schedule a daily task on AWS DataSync that will replicate the data between the on-premises Windows file server and Amazon S3. Use AWS Transfer Family to access the files is incorrect because Amazon S3 is an object storage service, not a file system. While S3 is primarily used for storing and retrieving large amounts of data, it doesn’t provide the same file system interface that Windows applications typically require. Additionally, using AWS Transfer Family adds unnecessary complexity to the setup.

The option that says: Use AWS Storage Gateway – File Gateway to create an SMB share on the on-premises data center to replace the existing Windows file server. Point the existing file shares to the new file gateway share is incorrect. This may be possible, however, the data in the file gateway is sent to Amazon S3. Once all Windows-based workloads are migrated to the AWS cloud, you will still need to set up a new Windows File server for file sharing. This can cause an interruption to your applications.

 

References:

https://aws.amazon.com/fsx/windows/

https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html

https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html

 

Check out these Amazon FSx and AWS DataSync Cheat Sheets:

https://tutorialsdojo.com/amazon-fsx/

https://tutorialsdojo.com/aws-datasync/

</details>

<a id="q33"></a>

## Q33

A solutions architect is planning the migration of hundreds of Hyper-V servers from an on-premises data center to AWS. To design an effective AWS infrastructure, the solutions architect needs to understand the type of running processes, CPU and memory load, and network dependencies between each server. 

What steps should the architect take to collect and analyze this data? (Select THREE.)

- **A.** Create a custom PowerShell script to collect basic server inventory from the Hyper-V servers. Upload the generated inventory file to AWS Transform for migration assessment.
- **B.** Create a migration assessment job in AWS Transform by using the discovery data.
- **C.** Deploy the AWS Transform discovery tool on the on-premises Hyper-V servers to collect server data.
- **D.** Use AWS Transform migration assessment results, chat-based analysis, and generated reports to evaluate right-sizing recommendations, dependencies, costs, and migration wave plans.
- **E.** Install the Amazon CloudWatch agent on the on-premises Hyper-V servers to collect system-level metrics. Use AWS System Manager OpsCenter to export the collected data to an Amazon S3 bucket.
- **F.** Create an AWS Glue Extract, Transform, Load (ETL) job to prepare the data for querying. Use Amazon Athena to run SQL queries on the transformed data for deeper analysis.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C, D · **You picked:** D, E, F

🔑 **Key words:** hundreds of Hyper-V servers; processes, CPU/memory, network dependencies

🪤 **Your trap:** CloudWatch agent / Glue+Athena ≠ migration discovery

🧠 **Rule:** Migration discovery + assessment → AWS Transform discovery tool + assessment job + reports.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: hàng trăm Hyper-V servers
Cần biết: running processes, CPU/memory load, network dependencies giữa các server
Mục tiêu: thiết kế hạ tầng AWS hiệu quả trước khi migrate
→ Chọn ĐÚNG BA bước để thu thập + phân tích dữ liệu này
```

Đáp án đúng: **B, C, D** (đều xoay quanh **AWS Transform**). Anh chọn **D, E, F** — đúng D nhưng sai ở E (CloudWatch agent + OpsCenter) và F (Glue + Athena), vì cả hai đều không phải công cụ discovery/migration chuyên dụng.

#### AWS Transform là gì (dịch vụ mới, chưa quen)

AWS Transform là dịch vụ dùng AI agent để tăng tốc và đơn giản hóa việc hiện đại hóa/di dời hạ tầng, ứng dụng và code. Nó gom nhiều khả năng modernization/migration vào một trải nghiệm web thống nhất, gồm:

- Hiện đại hóa & migrate IBM z/OS, Fujitsu GS21 lên AWS
- Migrate VMware workloads sang EC2
- Hiện đại hóa ứng dụng .NET sang .NET cross-platform chạy trên Linux
- **Đánh giá mức độ sẵn sàng migration (assessment)**

Trong phạm vi câu hỏi, ta chỉ cần quan tâm hai mảnh của Transform: **discovery tool** (thu thập inventory server) và **migration assessment** (đánh giá chi phí, right-sizing, kế hoạch di dời).

#### Vì sao B, C, D đúng

**C — AWS Transform discovery tool:**
```
Discovery tool cài trên các nguồn (VMware vCenter, Hyper-V, imported servers)
    → tự động quét: process đang chạy, CPU/memory load, network dependency
    → kết quả xem trong "Discovered Inventory" pane
```
Đây chính xác là bước thu thập dữ liệu thô mà đề yêu cầu (process, CPU/memory, dependency).

**B — Tạo migration assessment job từ discovery data:** sau khi có dữ liệu discovery, Transform dùng nó để tạo assessment — sinh ra ước tính chi phí (RDS, EC2, EBS, S3, FSx…), right-sizing, so sánh nhiều kịch bản.

**D — Dùng kết quả assessment + chat-based analysis + report:** Transform cho phép tinh chỉnh assessment qua chat, và xuất báo cáo/executive presentation để đánh giá right-sizing, dependency, cost, migration wave plan — đúng bước "phân tích dữ liệu" cuối cùng đề yêu cầu.

Ba bước này khớp thành một luồng liền mạch: **thu thập (C) → tạo đánh giá (B) → phân tích/khai thác kết quả (D)**.

#### Vì sao E và F (anh chọn) sai

- **E (CloudWatch agent + SSM OpsCenter):** CloudWatch agent chỉ lấy được metric hệ thống cơ bản (CPU%, memory% theo thời gian thực), **không** thu thập được network dependency giữa các server hay cấu hình chi tiết cần cho migration planning. OpsCenter là công cụ quản lý sự cố vận hành (operational issues), hoàn toàn không phải công cụ di dời.
- **F (Glue ETL + Athena):** Đây là công cụ xử lý/truy vấn dữ liệu tổng quát. Vấn đề là dữ liệu do Transform sinh ra **đã sẵn sàng để phân tích**, không cần thêm bước ETL trung gian — dùng Glue/Athena ở đây là thừa và lệch mục tiêu.

#### Vì sao A sai

A dùng PowerShell script tự viết để lấy inventory cơ bản rồi upload cho Transform — về mặt kỹ thuật khả thi, nhưng phức tạp và kém đầy đủ hơn nhiều so với dùng thẳng discovery tool chuyên dụng của Transform (vốn tự động quét toàn diện process/CPU/memory/dependency).

| Bước | Công cụ | Vai trò |
|---|---|---|
| Thu thập dữ liệu | **AWS Transform discovery tool (C)** | Quét tự động server inventory, process, CPU/memory, dependency |
| Tạo đánh giá | **Migration assessment job (B)** | Sinh cost estimate, right-sizing từ dữ liệu discovery |
| Phân tích kết quả | **Assessment results + chat + report (D)** | Tinh chỉnh, xuất báo cáo cho quyết định migration wave |
| Sai — không đủ chi tiết | CloudWatch agent + OpsCenter (E) | Chỉ có metric cơ bản, không có dependency; OpsCenter không phải tool migration |
| Sai — thừa bước | Glue ETL + Athena (F) | Dữ liệu Transform đã sẵn sàng phân tích, không cần ETL |

#### Bảng so sánh công cụ discovery/assessment cho migration (tổng hợp kiến thức chung)

| Công cụ | Mục đích chính | Đầu ra |
|---|---|---|
| **AWS Transform discovery tool** | Quét chi tiết server (process, CPU/memory, network dependency) từ VMware/Hyper-V/imported servers | Discovered Inventory, dữ liệu nạp cho assessment |
| **AWS Transform assessment** | Đánh giá cost, feasibility, business value dựa trên dữ liệu discovery | Right-sizing, multi-scenario comparison, report/chat |
| **Migration Evaluator** | Ước tính TCO (Total Cost of Ownership) khi so sánh on-prem vs AWS | Quick Insights report (TCO) |
| **AWS Application Discovery Service** | Thu thập chi tiết môi trường on-prem (dependency, resource utilization, config) cho việc lập kế hoạch migration | Dữ liệu discovery (không tự sinh TCO report) |
| **Migration Hub** | Theo dõi tiến độ migration tập trung, tổng hợp trạng thái từ nhiều công cụ | Dashboard trạng thái migration |

Ghi nhớ: Migration Evaluator trả lời câu hỏi "**tốn bao nhiêu tiền**" (TCO); Application Discovery Service và Transform discovery tool trả lời câu hỏi "**hệ thống đang chạy gì, phụ thuộc gì**"; Migration Hub chỉ là nơi theo dõi tiến độ tổng thể.

#### Quy tắc nhớ cho thi

- **"thu thập process/CPU/memory/network dependency trước migrate"** → **AWS Transform discovery tool**
- **"assessment job dùng discovery data → cost, right-sizing, wave plan"** → **AWS Transform migration assessment**
- **CloudWatch agent / OpsCenter** → chỉ là giám sát vận hành, không phải discovery cho migration
- **Glue + Athena** → công cụ ETL/query tổng quát, không cần khi dữ liệu nguồn đã sẵn sàng phân tích
- **Cần TCO cụ thể** → nghĩ đến **Migration Evaluator**, không phải Application Discovery Service hay Transform discovery

### TD explanation

AWS Transform is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.

With AWS Transform, you can:

Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS
Migrate VMware workloads to Amazon EC2
Modernize .NET applications to Linux-ready cross-platform .NET
Assess workloads for migration readiness

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.

The AWS Transform discovery tool automatically identifies server inventory within your organization to prepare for migration. The tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To use the discovery tool, you’ll configure one or more discovery sources, let the tool run, and then review the results in the Discovered Inventory pane.

Once you’ve set up a discovery source, the discovery tool begins collecting information. The time required for the tool to analyze your network completely depends on the size of your environment. For a directional migration business case, you can utilize the Migration Portfolio Assessment (MPA) files that the tool generates once server collection is complete.

AWS Transform assessments help you evaluate the cost, feasibility, and business value of migrating your on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinements through chat.

You can use migration assessments to:

– Obtain cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx

– Receive automated right-sizing recommendations

– Assess business value and sustainability impact

– Compare multiple migration scenarios side by side

– Refine assessments interactively through chat

– Generate executive presentations and detailed reports

Hence, the correct answers are:

– Deploy the AWS Transform discovery tool on the on-premises Hyper-V servers to collect server data.

– Create a migration assessment job in AWS Transform by using the discovery data.

– Use AWS Transform migration assessment results, chat-based analysis, and generated reports to evaluate right-sizing recommendations, dependencies, costs, and migration wave plans.

The option that says: Create a custom PowerShell script to collect basic server inventory from the Hyper-V servers. Upload the generated inventory file to AWS Transform for migration assessment is incorrect. While it’s technically possible, this approach is significantly more complex and less comprehensive than using the AWS Transform discovery tool.

The option that says: Install the Amazon CloudWatch agent on the on-premises Hyper-V servers to collect system-level metrics. Use AWS System Manager OpsCenter to export the collected data to an Amazon S3 bucket is incorrect. Although CloudWatch can be used to collect system-level metrics, it doesn’t provide detailed, in-depth discovery information needed for migration planning, such as dependencies, configurations, and utilization of on-premises servers. Furthermore, AWS Systems Manager OpsCenter typically provides a central location where you can manage and resolve operational issues, but it’s not a migration tool.

The option that says: Create an AWS Glue Extract, Transform, Load (ETL) job to prepare the data for querying. Use Amazon Athena to run SQL queries on the transformed data for deeper analysis is incorrect. AWS Glue’s ETL capabilities are unnecessary for this task because AWS Transform primarily provides the data in a format that is ready for analysis. There is no need to transform the data before running SQL queries.

 

References:

https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html

https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html

https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html

 

Check out the AWS Migration Services Cheat Sheet:

https://tutorialsdojo.com/aws-cheat-sheets-migration-services/

</details>

<a id="q63"></a>

## Q63

A manufacturing company operates an on-premises application on a self-managed Kubernetes cluster. The application includes a MySQL database for order processing and a MongoDB database for inventory tracking. The company plans to migrate the workloads to Amazon Elastic Kubernetes Service (Amazon EKS) cluster to improve scalability and manageability. Both environments are expected to maintain a fixed number of nodes to meet performance and capacity requirements.

Before proceeding with the migration, the company must assess the Total Cost of Ownership (TCO) for running the Kubernetes clusters and databases on AWS.

Which solution provides the most effective way to assess the Total Cost of Ownership (TCO)?

- **A.** Use AWS Transform MGN to initiate the migration process for your on-premises servers. Add the servers as source instances and perform a test migration. Generate a TCO report from Transform MGN to evaluate the cost of running your workloads in AWS.
- **B.** Ask for access to the Migration Evaluator to begin the TCO assessment. Use the Migration Evaluator Collector to gather data from your on-premises and then import the data. Export a Migration Evaluator Quick Insights report to evaluate the Total Cost of Ownership (TCO) for migrating workloads to AWS.
- **C.** Leverage AWS Application Discovery Service (Application Discovery Service) to collect detailed information about your on-premises environment. Use the data from the discovery service to assess migration costs and generate a TCO report for moving to AWS.
- **D.** Visit the AWS Cloud Economics Center to explore the AWS Cloud Value Framework. Use this framework to understand the economic benefits of cloud migration. From there, create an AWS Cost and Usage report to assess the costs of running your Kubernetes clusters and databases on AWS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** assess TCO before migrating K8s + DBs

🪤 **Your trap:** Application Discovery Service = inventory/dependencies, not TCO

🧠 **Rule:** TCO / business case → Migration Evaluator (Collector + Quick Insights).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: self-managed Kubernetes cluster
    ├── MySQL database (order processing)
    └── MongoDB database (inventory tracking)
Kế hoạch: migrate sang Amazon EKS, fixed số lượng node cả 2 bên

Trước khi migrate → cần đánh giá TCO (Total Cost of Ownership)
    "chạy K8s cluster + databases trên AWS tốn bao nhiêu so với hiện tại?"
```

Đáp án đúng là **B (Migration Evaluator)**. Anh chọn **C (Application Discovery Service)** — dễ nhầm vì cả hai đều là công cụ "discovery" trước migration, nhưng chúng trả lời hai câu hỏi khác nhau.

#### Migration Evaluator là gì

Trước đây gọi là "TCO Calculator" — đúng như tên cũ, mục đích chính là **ước tính chi phí** khi chuyển workload on-premises lên AWS. Nó thu thập dữ liệu hạ tầng hiện tại (số server, storage, network config…) qua **Migration Evaluator Collector**, sau đó import vào Migration Evaluator để phân tích.

```
On-prem infra  ──Migration Evaluator Collector──►  Import dữ liệu
                                                          │
                                                          ▼
                                          Quick Insights report
                                (so sánh side-by-side: chi phí on-prem vs AWS)
```

Kết quả là **Quick Insights report** — báo cáo TCO trực tiếp, giúp doanh nghiệp ra quyết định ngân sách và chiến lược migration.

#### Vì sao B đúng

Quy trình khớp chính xác với luồng chuẩn của Migration Evaluator:
```
1. Xin quyền truy cập Migration Evaluator
2. Dùng Collector thu thập dữ liệu on-prem → import vào tool
3. Export Quick Insights report → có ngay số liệu TCO
```
Đây là công cụ **được thiết kế riêng** để trả lời câu hỏi "tốn bao nhiêu tiền khi migrate" — đúng trọng tâm đề bài.

#### Vì sao C (Application Discovery Service — anh chọn) sai

Application Discovery Service thu thập thông tin **chi tiết về môi trường** on-premises: dependency giữa các ứng dụng, resource utilization, cấu hình hệ thống. Đây là công cụ cực kỳ hữu ích để **lập bản đồ migration** (biết cái gì phụ thuộc cái gì, thứ tự di dời ra sao) — nhưng **bản thân nó không sinh ra TCO report**. Nó chỉ cung cấp dữ liệu thô; muốn có con số so sánh chi phí on-prem vs AWS, vẫn cần một công cụ khác xử lý tiếp (chính là Migration Evaluator). Đây là bẫy kinh điển: nhầm "công cụ thu thập dữ liệu môi trường" với "công cụ tính TCO".

#### Vì sao A và D sai

- **A (Transform MGN):** MGN (Migration Service) tập trung vào **thực thi migration** (rehost workload thật sự qua test migration), không phải công cụ tạo TCO report chính thức trước khi quyết định migrate.
- **D (Cloud Economics Center + Cost and Usage Report):** Cloud Value Framework cho cái nhìn **kinh tế tổng quát, ở tầm cao** (lợi ích chung của việc lên cloud), không đi sâu vào con số TCO chi tiết cho từng workload cụ thể như Kubernetes cluster + database trong đề. Cost and Usage Report chỉ theo dõi chi phí **sau khi đã chạy trên AWS**, không dùng để ước tính trước khi migrate.

| Công cụ | Trả lời câu hỏi gì | Sinh TCO report? |
|---|---|---|
| **Migration Evaluator (B)** | "Tốn bao nhiêu khi chuyển lên AWS?" | Có — Quick Insights report |
| Application Discovery Service (C) | "Hệ thống hiện tại có gì, phụ thuộc gì?" | Không — chỉ cung cấp dữ liệu thô |
| Transform MGN (A) | "Làm sao thực thi việc migrate?" | Không — tập trung execution |
| Cloud Economics Center + CUR (D) | "Lợi ích tổng quát của cloud là gì? Chi phí thực tế sau khi chạy?" | Không — ở tầm framework/report vận hành, không phải TCO trước migrate |

#### Lưu ý thực tế

Application Discovery Service và Migration Evaluator thường **đi cùng nhau** trong một dự án migration thực tế: Application Discovery Service trả lời "cái gì đang chạy, phụ thuộc ra sao" để lập kế hoạch kỹ thuật; Migration Evaluator trả lời "tốn bao nhiêu tiền" để thuyết phục ban lãnh đạo phê duyệt ngân sách. Đề thi hay tách riêng hai vai trò này để kiểm tra xem thí sinh có phân biệt được không.

#### Quy tắc nhớ cho thi

- **"TCO / business case / so sánh chi phí on-prem vs AWS"** → **Migration Evaluator** (Collector + Quick Insights report)
- **"dependency mapping / resource utilization / cấu hình chi tiết"** → **Application Discovery Service**
- **"thực thi migration thật sự (rehost)"** → **Transform MGN**, không phải công cụ TCO
- Discovery Service cho dữ liệu, Migration Evaluator cho **tiền** — đừng nhầm hai vai trò này

### TD explanation

AWS Migration Evaluator, formerly the TCO Calculator, is a tool designed to help businesses estimate the total cost of ownership (TCO) for migrating their on-premises workloads to AWS. This service allows users to assess the financial implications of moving their infrastructure and applications from on-premises data centers to the AWS cloud.

By collecting key data points about an organization’s current infrastructure, such as the number of servers, storage requirements, and network configuration, the Migration Evaluator generates detailed reports comparing the costs of running workloads on AWS with those of the existing on-premises environment.

The Migration Evaluator Collector facilitates the gathering of data from on-premises environments. It collects detailed information on infrastructure usage and resource consumption, which can then be imported into the Migration Evaluator. Once the data is collected, the tool analyzes it. Produces a Quick Insights report, highlighting potential cost savings and providing a side-by-side comparison of the on-premises environment versus the proposed AWS environment. This analysis helps businesses make informed decisions about migration, budgeting, and resource planning, ensuring they understand the financial benefits and trade-offs of moving to the cloud.

In addition to cost estimates, the tool offers insights into optimization opportunities, assisting companies in refining their cloud strategy. It simplifies the complex process of evaluating cloud costs, enabling businesses to make more informed choices about their infrastructure and future cloud investments.

Hence, the correct answer is: Ask for access to the Migration Evaluator to begin the TCO assessment. Use the Migration Evaluator Collector to gather data from your on-premises and then import the data. Export a Migration Evaluator Quick Insights report to evaluate the Total Cost of Ownership (TCO) for migrating workloads to AWS.

The option that says: Use AWS Transform MGN to initiate the migration process for your on-premises servers. Add the servers as source instances and perform a test migration. Generate a TCO report from Transform MGN to evaluate the cost of running your workloads in AWS is incorrect. AWS Transform MGN is primarily focused on migration execution and rehosting workflows, not simply producing a formal pre-migration TCO assessment for Kubernetes clusters and databases.

The option that says: Visit the AWS Cloud Economics Center to explore the AWS Cloud Value Framework. Use this framework to understand the economic benefits of cloud migration. From there, create an AWS Cost and Usage report to assess the costs of running your Kubernetes clusters and databases on AWS is incorrect. While this option offers valuable insights into the general economic advantages of migrating to AWS, such as cost savings and flexibility, it does not focus on detailed, granular TCO calculations for specific workloads. The AWS Cloud Value Framework helps organizations evaluate cloud adoption at a high level, but it lacks the comprehensive cost estimation and comparison features Migration Evaluator offers for TCO assessment.

The option that says: Leverage AWS Application Discovery Service (Application Discovery Service) to collect detailed information about your on-premises environment. Use the data from the discovery service to assess migration costs and generate a TCO report for moving to AWS is incorrect. AWS Application Discovery Service gathers detailed information about your on-premises environment, including application dependencies, resource utilization, and system configurations. It is a critical tool for planning and mapping out complex migration scenarios but does not generate TCO reports alone. The service only focuses on discovering and cataloging the environment rather than directly assessing migration costs. While it helps gather the data necessary for a TCO analysis, it does not provide the final cost comparison or detailed TCO insights, which is the primary need in the scenario.

 

References:

https://aws.amazon.com/migration-evaluator/

https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-pricingtco-tools.html

 

Check out this Migration Evaluator Cheat Sheet:

https://tutorialsdojo.com/migration-evaluator-cheat-sheet/

</details>

<a id="q49"></a>

## Q49

A financial services company is migrating 18 internal business applications to AWS as part of a data center consolidation project. The applications include Spring Boot Java and Node.js services that currently run across several virtual machine clusters.

The majority of the applications are used only during weekly financial reconciliation and quarter-end reporting, with minimal usage outside those periods. Most services require less than 1 GiB of memory, but a few Java-based applications can temporarily require up to 3 GiB of memory while generating large reports. One Java application produces regulatory compliance reports by aggregating data from multiple databases and typically runs for 2 to 4 hours. The company wants to minimize infrastructure costs, standardize deployment across all applications, and automatically adjust compute capacity based on demand.

Which solution will meet these requirements in the MOST cost-effective way?

- **A.** Deploy all applications on Amazon EC2 instances behind Application Load Balancers. Use EC2 Auto Scaling with an Auto Scaling group, and purchase Reserved Instance capacity matching the maximum capacity defined by the Auto Scaling group’s GroupMaxSize parameter.
- **B.** Containerize each application and deploy it as an Amazon ECS task on an Amazon EC2 cluster. Configure EC2 Auto Scaling to scale cluster capacity based on memory utilization and monitor workloads by using Amazon CloudWatch.
- **C.** Deploy the Java applications on Amazon EC2 instances and the Node.js applications on AWS App Runner to optimize each runtime separately. Use separate deployment pipelines for each platform.
- **D.** Containerize each application and deploy it to AWS Lambda as container images. Configure provisioned concurrency for all functions to reduce startup latency during reporting periods.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** 18 apps; mostly idle except weekly/quarter-end; <1–3 GiB; most cost-effective

🪤 **Your trap:** RIs sized to ASG max = paying for idle capacity

🧠 **Rule:** Many small intermittent apps → containerize, ECS on EC2 cluster (bin-packing) + scale on memory.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
18 internal apps (Spring Boot Java + Node.js) migrate lên AWS
    - Đa số chỉ chạy trong tuần đối soát tài chính + cuối quý, còn lại IDLE
    - Hầu hết cần <1 GiB memory, một số Java app cần TẠM THỜI tới 3 GiB
    - 1 app Java báo cáo compliance: chạy 2-4 GIỜ liên tục
Mục tiêu: giảm chi phí + chuẩn hóa deployment + tự động điều chỉnh compute theo demand
```

Đáp án đúng là **B (ECS task trên EC2 cluster, Auto Scaling theo memory)**. Anh chọn **A (EC2 + ASG + Reserved Instance theo GroupMaxSize)** — sai vì RI mua theo capacity tối đa nghĩa là trả tiền cho cả lúc hệ thống idle, đi ngược lại chính yêu cầu "cost-effective" của đề.

#### Vì sao B đúng

Ý tưởng cốt lõi: 18 ứng dụng nhỏ, phần lớn idle, nhu cầu memory khác nhau (dưới 1 GiB đến 3 GiB) → đây là bài toán **bin-packing** kinh điển. Amazon ECS trên EC2 cluster giải quyết rất tốt vì:

```
ECS cluster (EC2 instances, managed scaling)
    ├── Task 1 (app nhỏ, <1 GiB)  ┐
    ├── Task 2 (app nhỏ, <1 GiB)  ├─► nhiều task chia sẻ chung 1 EC2 instance
    ├── Task 3 (app nhỏ, <1 GiB)  ┘   (bin-packing theo memory)
    └── Task Java (3 GiB lúc peak) → ECS tự co giãn container/node khi cần
```

- **Containerize hóa** → chuẩn hóa deployment cho cả Java và Node.js trên cùng một nền tảng, thay vì quản lý riêng lẻ từng runtime.
- **ECS cluster auto-scaling** (managed scaling qua capacity provider) tự động scale-in/scale-out EC2 instance dựa trên % utilization của target — khi phần lớn app idle, cluster co lại; khi vào mùa cao điểm (đối soát, cuối quý), cluster phình ra.
- **Scale theo memory utilization** khớp đúng đặc điểm bài toán: ràng buộc chính là RAM (<1 GiB → 3 GiB), không phải CPU.
- CloudWatch giám sát toàn bộ cluster/service theo thời gian gần thực (1 phút/lần) để hỗ trợ scaling.

#### Vì sao A (đáp án anh chọn) sai

A mua **Reserved Instance khớp với GroupMaxSize của Auto Scaling group** — nghĩa là trả tiền cố định cho **công suất tối đa** dù phần lớn thời gian trong tuần hệ thống gần như không dùng gì (chỉ hoạt động mạnh vào tuần đối soát + cuối quý). Đây chính là bẫy: nghe có vẻ "tối ưu vì có Reserved Instance giảm giá", nhưng bản chất là **overprovisioning cố định**, triệt tiêu hoàn toàn lợi ích của việc scale-down khi idle — ngược hẳn yêu cầu "cost-effective" và "tự động điều chỉnh theo demand".

#### Vì sao C sai

C tách Java chạy trên EC2, Node.js chạy trên App Runner, dùng **hai pipeline deploy riêng biệt**. Điều này vi phạm trực tiếp yêu cầu "**standardize deployment across all applications**" — thêm độ phức tạp vận hành, hai hệ thống khác nhau cần quản lý, giám sát, bảo trì riêng.

#### Vì sao D sai

D containerize và deploy hết lên **Lambda dưới dạng container image**, kèm provisioned concurrency:

- Lambda có **giới hạn thực thi tối đa 15 phút/lần gọi** — không thể chạy app compliance report kéo dài **2-4 giờ**. Đây là điểm loại trực tiếp, bất kể memory hay giá cả.
- Provisioned concurrency cho **tất cả** function nghĩa là giữ sẵn capacity ngay cả lúc idle → tốn chi phí không cần thiết, phản lại đúng mục tiêu "minimize infrastructure costs" khi phần lớn ứng dụng chỉ chạy theo đợt.

| Phương án | Vấn đề chính |
|---|---|
| **B. ECS trên EC2, scale theo memory** | Đúng — bin-packing nhiều task nhỏ, tự scale theo nhu cầu thực tế, 1 nền tảng chuẩn hóa |
| A. EC2 + RI theo GroupMaxSize | Trả tiền cho công suất tối đa dù phần lớn thời gian idle |
| C. EC2 (Java) + App Runner (Node.js) | Hai pipeline, không chuẩn hóa được deployment |
| D. Lambda container + provisioned concurrency toàn bộ | Vượt giới hạn 15 phút/invocation; giữ capacity không cần thiết khi idle |

#### Lưu ý thực tế

Job chạy 2-4 giờ là tín hiệu loại trừ Lambda gần như ngay lập tức trong mọi bài toán SAP-C02 — hễ thấy thời lượng thực thi vượt quá vài chục phút, gạch bỏ mọi đáp án Lambda mà không cần đọc tiếp phần còn lại của option đó.

#### Quy tắc nhớ cho thi

- **"nhiều app nhỏ, phần lớn idle, cần standardize + auto scale"** → **containerize + ECS trên EC2 cluster (bin-packing) + scale theo memory/CPU utilization**
- **"Reserved Instance theo GroupMaxSize / max capacity"** → gần như luôn là bẫy overprovisioning, không cost-effective
- **"job chạy >15 phút"** → loại ngay mọi đáp án Lambda
- **"standardize deployment across all apps"** → loại các đáp án tách nền tảng/pipeline riêng theo từng runtime

### TD explanation

Amazon ECS (Elastic Container Service) can manage the scaling of Amazon EC2 (Elastic Compute Cloud) instances that are registered to your cluster, a feature known as Amazon ECS cluster auto-scaling. To enable managed scaling, you activate it when creating the Amazon ECS Auto Scaling group capacity provider. After that, you set a target percentage (the targetCapacity) for instance utilization within this Auto Scaling group. Amazon ECS generates two custom CloudWatch metrics and establishes a target tracking scaling policy for your Auto Scaling group. This allows Amazon ECS to automatically manage the scale-in and scale-out actions based on the resource utilization of your tasks.

When using Amazon EC2 instances for your capacity, Auto Scaling groups help in managing the EC2 instances registered to your clusters. Auto Scaling ensures you have the appropriate number of Amazon EC2 instances available to handle your application load effectively.

You have the option to use the managed scaling feature to allow Amazon ECS to manage the scale-in and scale-out actions of the Auto Scaling group, or you can choose to handle the scaling actions manually.

A task definition serves as a blueprint for your application. It is a text file in JSON format that outlines the parameters and configurations for one or more containers that make up your application.

You can monitor your Amazon ECS resources through Amazon CloudWatch, which collects and processes raw data from Amazon ECS into readable, near-real-time metrics. These statistics are recorded for two weeks, enabling you to access historical information and gain better insights into the performance of your clusters or services. Amazon ECS metric data is automatically sent to CloudWatch at one-minute intervals.

Hence, the correct answer is: Containerize each application and deploy it as an Amazon ECS task on an Amazon EC2 cluster. Configure EC2 Auto Scaling to scale cluster capacity based on memory utilization and monitor workloads by using Amazon CloudWatch. Containerization standardizes deployment across all applications, Auto Scaling ensures compute capacity adjusts automatically to demand, and EC2 scaling based on memory utilization minimizes costs by scaling down during idle periods while still supporting applications that temporarily need more memory.

The option that says: Deploy the Java applications on Amazon EC2 instances and the Node.js applications on AWS App Runner to optimize each runtime separately. Use separate deployment pipelines for each platform is incorrect because it introduces operational complexity by splitting runtimes and pipelines. This prevents standardized deployment across all applications and increases management overhead, which goes against the requirement to minimize costs and streamline operations.

The option that says: Containerize each application and deploy it to AWS Lambda as container images. Configure provisioned concurrency for all functions to reduce startup latency during reporting periods is incorrect because although AWS Lambda primarily supports container images and can handle workloads up to 10 GiB of memory, it is not well‑suited for long‑running applications like the Java compliance report that runs for 2–4 hours. Lambda has a maximum execution time of 15 minutes per invocation, which makes it incompatible with multi‑hour reporting jobs. Additionally, configuring provisioned concurrency for all functions would keep capacity allocated even during idle periods, increasing costs unnecessarily. This contradicts the requirement to minimize infrastructure costs while supporting variable workloads.

The option that says: Deploy all applications on Amazon EC2 instances behind Application Load Balancers. Use EC2 Auto Scaling with an Auto Scaling group, and purchase Reserved Instance capacity matching the maximum capacity defined by the Auto Scaling group’s GroupMaxSize parameter is incorrect because purchasing Reserved Instances for maximum capacity typically locks in costs even when workloads are idle. This eliminates the cost savings from scaling down and leads to overprovisioning, making it the least cost‑effective choice.

 

References:

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-auto-scaling.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html

 

Check out this Amazon Elastic Container Service Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

</details>

<a id="q55"></a>

## Q55

An organization operates web and mobile platforms for online sales, inventory management, order processing, and shipping logistics. The platforms are running on Amazon EC2 instances across multiple regions. The organization’s databases include a MySQL database for the e-commerce site and a PostgreSQL database for analytics, both managed on EC2 instances.

A solutions architect requires a solution to transition the organization’s architecture to an event-driven, serverless architecture to improve efficiency and data processing speeds, enable real-time analytics, and streamline application data flows. The company also plans to launch a multi-cloud configuration that runs additional clusters on other cloud service providers to further improve the site’s performance.

Which of the following options would most efficiently meet these requirements?

- **A.** Migrate to microservices with Amazon EKS and Fargate. Use Aurora Serverless MySQL for e-commerce and Redshift Serverless for analytics. Use Amazon EventBridge to streamline and manage data flows.
- **B.** Create Auto Scaling groups for each platform component with specific EC2 instance numbers. Migrate e-commerce MySQL and analytics PostgreSQL databases to Amazon Aurora PostgreSQL. Use Amazon SNS to route incoming data to the right EC2 instances and databases.
- **C.** Use Amazon ECS with Fargate to repackage applications as microservices. Migrate e-commerce and analytics databases to Aurora Serverless MySQL and Redshift Serverless. Manage data flow between services using Amazon EventBridge.
- **D.** Migrate app components to microservices with Amazon EKS using AWS Fargate. Change e-commerce MySQL to Amazon Aurora MySQL and analytics DB to Amazon Redshift. Use Amazon Kinesis for real-time data streaming.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** event-driven SERVERLESS; real-time analytics; streamline data flows

🪤 **Your trap:** Aurora/Redshift provisioned ≠ serverless

🧠 **Rule:** 'Serverless' in question → pick serverless variants: Aurora Serverless, Redshift Serverless, EventBridge.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 instances, multi-region
    ├── MySQL (e-commerce) trên EC2
    └── PostgreSQL (analytics) trên EC2

Yêu cầu:
    → event-driven, SERVERLESS architecture
    → real-time analytics
    → streamline data flow giữa các service
    → PLUS: multi-cloud (chạy thêm cluster ở cloud provider khác)
```

Đáp án đúng là **A (EKS + Fargate, Aurora Serverless MySQL, Redshift Serverless, EventBridge)**. Anh chọn **D (EKS + Fargate nhưng Aurora MySQL/Redshift bản thường + Kinesis)** — đúng phần container, sai vì thiếu tính "serverless" ở tầng database và chọn sai dịch vụ điều phối sự kiện.

#### Vì sao A đúng — ghép đúng từng mảnh yêu cầu

```
Microservices (EKS + Fargate) ──event──► Amazon EventBridge (event bus)
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
              Aurora Serverless MySQL                        Redshift Serverless
              (transactional, e-commerce)                    (analytics, real-time)
```

- **Amazon EKS + AWS Fargate:** EKS chạy Kubernetes control plane được AWS quản lý; Fargate là compute engine serverless cho container (không cần quản lý server/cluster EC2). Điểm mấu chốt cho yêu cầu **multi-cloud**: EKS dựa trên Kubernetes chuẩn, nên **cloud-agnostic** — dễ tích hợp/di chuyển sang cluster ở Azure, GCP hơn so với ECS (vốn là dịch vụ AWS-specific, khó mở rộng multi-cloud).
- **Aurora Serverless MySQL:** vẫn là MySQL nhưng tự động scale capacity theo tải, không cần provisioning cố định — khớp đúng chữ "serverless" trong yêu cầu.
- **Redshift Serverless:** data warehouse cho phân tích, không cần quản lý infrastructure, phù hợp cho "real-time analytics" mà không phải lo capacity planning.
- **Amazon EventBridge:** serverless event bus — nơi các microservice bắn event, rồi route dữ liệu tới đúng đích (Aurora Serverless cho giao dịch, Redshift Serverless cho phân tích). Đây chính là "streamline application data flows" mà đề yêu cầu.

#### Vì sao D (đáp án anh chọn) sai

D dùng đúng EKS + Fargate (tốt cho multi-cloud), nhưng:

1. **Aurora MySQL và Redshift ở dạng thường** (không phải Serverless) — vẫn cần provisioning, quản lý capacity, không đạt được mục tiêu "serverless" mà đề nhấn mạnh rõ ràng ngay từ đầu. Đây chính là bẫy: chọn đúng loại database engine (MySQL, Redshift) nhưng quên phần "Serverless" đi kèm.
2. **Amazon Kinesis** phù hợp cho real-time **data streaming** thuần túy, nhưng đề cần một cơ chế **điều phối sự kiện giữa nhiều service** (event-driven orchestration) — đây là vai trò của **EventBridge**, không phải Kinesis. Kinesis xử lý luồng dữ liệu thô; EventBridge định tuyến sự kiện có ngữ nghĩa (event routing) giữa các microservice.

#### Vì sao C sai

C gần giống A về database (Aurora Serverless + Redshift Serverless + EventBridge) nhưng dùng **Amazon ECS + Fargate** thay vì EKS. ECS là dịch vụ container đặc thù của AWS, **thường không hỗ trợ tốt cho kịch bản multi-cloud** — trong khi đề bài nêu rõ công ty muốn chạy thêm cluster ở cloud provider khác. EKS (dựa trên Kubernetes mở) phù hợp hơn nhiều cho mục tiêu portability này.

#### Vì sao B sai

B gần như đi ngược hoàn toàn yêu cầu: dùng **Auto Scaling group với EC2 instance cố định số lượng**, migrate cả hai database về **Aurora PostgreSQL** (không phải serverless, và MySQL bị đổi engine không cần thiết), dùng **SNS** để route dữ liệu tới EC2/database cụ thể — vẫn là kiến trúc dựa trên quản lý server truyền thống, không đạt yêu cầu serverless/event-driven.

| Phương án | Container platform | Database | Event/data flow | Vấn đề |
|---|---|---|---|---|
| **A. Đúng** | EKS + Fargate | Aurora Serverless + Redshift Serverless | EventBridge | Không có |
| B | EC2 + ASG | Aurora PostgreSQL (cả 2 DB, không serverless) | SNS | Không serverless, không event-driven đúng nghĩa |
| C | **ECS** + Fargate | Aurora Serverless + Redshift Serverless | EventBridge | ECS kém phù hợp multi-cloud hơn EKS |
| D | EKS + Fargate | Aurora MySQL + Redshift (không serverless) | Kinesis | Thiếu "serverless" ở DB; Kinesis không phải công cụ điều phối event |

#### Quy tắc nhớ cho thi

- **Đề nói "serverless" rõ ràng** → luôn ưu tiên biến thể Serverless của mọi dịch vụ được nhắc tới (Aurora Serverless, Redshift Serverless, Fargate…), đừng chọn bản provisioned dù cùng engine.
- **"multi-cloud" / cloud-agnostic** → **EKS** thắng **ECS** vì dựa trên Kubernetes chuẩn.
- **"streamline/route data flow giữa các service" (event-driven orchestration)** → **EventBridge**; **Kinesis** chỉ dùng khi cần streaming dữ liệu thô theo thời gian thực, không phải điều phối sự kiện.
- Thấy đáp án đổi engine không cần thiết (MySQL → PostgreSQL khi đề không yêu cầu) → nghi ngờ ngay, thường là bẫy.

### TD explanation

Amazon EKS is a service that helps you run Kubernetes on AWS without having to set up or manage your own Kubernetes control plane. EKS allows you to concentrate on containers while AWS handles the underlying Kubernetes infrastructure. Amazon ECS on the other hand supports Docker containers, making it easier to run and scale containerized applications without worrying about managing virtual machine clusters.

ECS may be better if you want to use AWS-specific features. At the same time, EKS gives you more portability to move workloads on and off AWS if needed.

AWS Fargate is a serverless compute engine for containers. You can use containers without having to manage servers or clusters. AWS manages your containers, you only pay for the resources needed to run them. Fargate works with ECS and EKS.

Aurora Serverless is a serverless database that automatically scales capacity up or down to match your application’s needs. It is fully managed by AWS and provides high availability and auto-scaling for databases. Amazon Redshift Serverless is a fully managed serverless data warehousing service from AWS. With Redshift Serverless, you can run analytics and get insights from data without needing to provision and manage data warehouse infrastructure.

Amazon EventBridge is a serverless event bus service that allows you to connect applications together using data from various sources.

To improve the system, the applications can be migrated to a microservices architecture. By doing this, each microservice can be containerized and deployed to EKS on AWS Fargate, providing scalability and high availability without the need to manage servers. Additionally, the EKS is cloud-agnostic —meaning it is easier to integrate with other cloud service providers like Azure and GCP. For easy management, the transactional MySQL database can be migrated to Aurora Serverless. It provides the same capabilities as MySQL in a managed database that automatically scales based on usage. Similarly, the analytics data from transactions can be migrated to Redshift Serverless, which enables running ad-hoc queries and analytics on the data without having to worry about managing database capacity. To capture events from microservices and send relevant data to Aurora Serverless for transactions and Redshift Serverless for analytics, use EventBridge. This provides a central way to capture and route events and data between various services.

Hence, the correct answer is: Migrate to microservices with Amazon EKS and Fargate. Use Aurora Serverless MySQL for e-commerce and Redshift Serverless for analytics. Use Amazon EventBridge to streamline and manage data flows.

The option that says: Use Amazon ECS with Fargate to repackage applications as microservices. Migrate e-commerce and analytics databases to Aurora Serverless MySQL and Redshift Serverless. Manage data flow between services using Amazon EventBridge is incorrect. Although this option also suggests using Aurora Serverless, Amazon EventBridge, and Redshift Serverless, the container service being used is Amazon ECS, which typically does not support multi-cloud deployments, unlike EKS. While ECS with Fargate allows for container orchestration and management, it doesn’t fully address the requirement of explicit multi-cloud integration. In contrast, Amazon EKS (Elastic Kubernetes Service) with Fargate offers a more suitable platform for multi-cloud configuration with cost-effective serverless computing.

The option that says: Create Auto Scaling groups for each platform component with specific EC2 instance numbers. Migrate e-commerce MySQL and analytics PostgreSQL databases to Amazon Aurora PostgreSQL. Use Amazon SNS to route incoming data to the right EC2 instances and databases is incorrect. This solution fails to meet the serverless and event-driven architecture requirement as it still primarily relies on managing EC2 instances.

The option that says: Migrate app components to microservices with Amazon EKS using AWS Fargate. Change e-commerce MySQL to Amazon Aurora MySQL and analytics DB to Amazon Redshift. Use Amazon Kinesis for real-time data streaming is incorrect. Although the option suggests changing the e-commerce MySQL database to Amazon Aurora MySQL and the analytics database to Amazon Redshift, it doesn’t specifically mention utilizing the serverless variants of these databases. Leveraging Aurora Serverless MySQL and Redshift Serverless would provide better scalability and cost optimization, aligning more closely with the organization’s goal of streamlining data processing and achieving real-time analytics. Additionally, while Amazon Kinesis is suitable for real-time data streaming, it doesn’t address the requirement for efficient event-driven data flow management and integration between services in an event-driven architecture. Utilizing Amazon EventBridge would be more appropriate for managing data flows in such an architecture. Therefore, this option lacks full alignment with the requirements for transitioning to an event-driven, serverless architecture due to the omission of specific serverless database options and the choice of real-time data streaming service.

 

References:

https://docs.aws.amazon.com/solutions/latest/constructs/aws-fargate-eventbridge.html

https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/event-driven-architectures.html

https://aws.amazon.com/blogs/mt/moving-to-event-driven-architectures-with-serverless-event-aggregators/

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/amazon-redshift/

https://tutorialsdojo.com/amazon-elastic-kubernetes-service-eks/

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

https://tutorialsdojo.com/aws-fargate/

</details>

<a id="q74"></a>

## Q74

A company recently migrated a legacy application from a data center to AWS. The application, which is hosted on an EC2 instance, uses a Simple Mail Transfer Protocol (SMTP) server for sending promotional emails. The application communicates with the SMTP server over port 25 without TLS encryption. As part of its replatforming strategy, the company has opted to replace the SMTP server with Amazon Simple Email Service (SES). The SES domain is already created and has been validated.

What steps should be taken next to enable communication between the application and Amazon SES?

- **A.** Create an IAM Role for the application with ses:SendEmail and ses:SendRawEmail permissions and attach it to the EC2 instance. Update the SMTP settings in the application to connect to the Amazon SES SMTP. Update the port number to 465 to use TLS Wrapper.
- **B.** Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential. Use the AWS SDK for Amazon SES to send emails.
- **C.** Create an IAM user and grant it permission to send emails through Amazon SES. Generate access keys for this IAM user. Update the application to use these access keys and connect to the Amazon SES SMTP endpoint. Change the port to 587 to use STARTTLS.
- **D.** Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential and update the connection to the Amazon SES SMTP endpoint. Change the port settings to 587 to use STARTTLS.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** legacy app SMTP port 25 no TLS → SES

🪤 **Your trap:** IAM role doesn't work for SMTP interface

🧠 **Rule:** App speaking SMTP → SES SMTP credentials + SES SMTP endpoint + port 587 STARTTLS.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Legacy app trên EC2
    ── kết nối SMTP server qua port 25, KHÔNG có TLS ──

Replatform: thay SMTP server bằng Amazon SES (domain đã tạo + validated)
Cần: bước tiếp theo để app kết nối được với SES qua giao thức SMTP
```

Đáp án đúng là **D (SMTP credential + SES SMTP endpoint + port 587 STARTTLS)**. Anh chọn **A (IAM Role + SES SMTP + port 465 TLS Wrapper)** — sai ở điểm mấu chốt: **giao diện SMTP của SES không dùng IAM credentials**.

#### Amazon SES hỗ trợ hai giao diện gửi mail khác nhau

```
Amazon SES
   ├── SMTP interface   ──► cần SMTP credential (username/password riêng)
   └── SES API          ──► cần IAM credentials (access key / IAM role)
```

Đây là điểm cốt lõi của cả câu hỏi: **hai interface dùng hai loại credential khác nhau, không thể lẫn lộn**. Vì legacy app "communicates with the SMTP server" — tức app đang nói giao thức SMTP thuần, không gọi API — nên phải dùng **SMTP credential**, không phải IAM role/IAM user access key.

#### Vì sao D đúng

```
1. Tạo SMTP credential qua SES console (riêng biệt với IAM access key)
2. Cấu hình app dùng SMTP credential đó để authenticate
3. Trỏ app tới SES SMTP endpoint
4. Đổi port 25 → 587, dùng STARTTLS để mã hóa kết nối
```

STARTTLS là cách **nâng cấp kết nối chưa mã hóa thành kết nối mã hóa**: client connect vào SES SMTP endpoint (port 25, 587, hoặc 2587), gửi lệnh EHLO, server báo có hỗ trợ STARTTLS, client gửi lệnh STARTTLS để bắt đầu đàm phán TLS, sau đó phiên SMTP tiếp tục như bình thường nhưng đã được mã hóa.

Vì sao chọn port 587 thay vì giữ port 25: EC2 instance mặc định bị **throttle (giới hạn)** trên port 25 (để chống spam) — dùng port 587 tránh việc phải xin AWS gỡ giới hạn đó, đồng thời đạt luôn yêu cầu bảo mật TLS mà đề đặt ra (app hiện tại không có TLS).

#### Vì sao A (đáp án anh chọn) sai

A gắn **IAM Role có quyền `ses:SendEmail`/`ses:SendRawEmail`** cho EC2 instance, rồi vẫn cấu hình app trỏ vào **SES SMTP** endpoint. Đây là mâu thuẫn nội tại: quyền IAM (dù là role hay user) chỉ có tác dụng khi gọi qua **SES API**, hoàn toàn không dùng được để authenticate vào **SMTP interface**. Giao diện SMTP đòi hỏi **SMTP credential riêng** (một cặp username/password được sinh ra đặc biệt từ IAM secret key qua thuật toán ký, không phải access key thông thường). Ngoài ra A chọn port 465 (TLS Wrapper) — không sai về mặt kỹ thuật (SES cũng hỗ trợ TLS Wrapper), nhưng vấn đề chính vẫn là thiếu SMTP credential.

#### Vì sao C sai

C tạo **IAM user** với quyền gửi email, sinh access key, rồi vẫn kết nối vào **SES SMTP endpoint** với access key đó — cùng lỗi bản chất như A: access key của IAM user không phải là SMTP credential, không dùng được để authenticate SMTP session, dù port 587 + STARTTLS được chọn đúng.

#### Vì sao B sai

B tạo đúng **SMTP credential**, nhưng bước sau lại dùng **AWS SDK for Amazon SES để gửi email** — nghĩa là chuyển hẳn sang gọi **API**, không còn là giao tiếp SMTP nữa. Khi dùng SDK/API, phải chuyển sang dùng **IAM credentials** (role hoặc access key), SMTP credential lúc này trở nên vô dụng. B tự mâu thuẫn: tạo đúng loại credential nhưng lại dùng sai interface tương ứng.

| Phương án | Loại credential | Interface sử dụng | Khớp nhau? |
|---|---|---|---|
| **D. Đúng** | SMTP credential | SES SMTP endpoint, port 587 STARTTLS | Có |
| A | IAM Role (`ses:SendEmail`) | SES SMTP endpoint | Không — IAM không dùng cho SMTP |
| B | SMTP credential | AWS SDK (API) | Không — SMTP credential không dùng cho API |
| C | IAM user access key | SES SMTP endpoint | Không — access key không dùng cho SMTP |

#### Lưu ý thực tế

Quy tắc phân biệt gọn nhất: **"app nói SMTP" → cần SMTP credential; "app gọi SDK/API" → cần IAM credential (role hoặc access key)**. Không có chuyện trộn lẫn hai loại. Đề thường cài bẫy bằng cách giữ nguyên interface (SMTP) nhưng đổi loại credential, hoặc ngược lại — cần đọc kỹ xem app "connect to SMTP endpoint" hay "use SDK".

#### Quy tắc nhớ cho thi

- **App legacy nói SMTP → chuyển sang SES** → luôn cần **SMTP credential** (tạo riêng qua SES console), không phải IAM role/access key
- **Port 587 + STARTTLS** → lựa chọn mặc định khuyến nghị cho SES SMTP (tránh throttle port 25 trên EC2, có TLS)
- **Port 465 (TLS Wrapper) hoặc 2587** → vẫn hợp lệ về mặt kỹ thuật nhưng ít khi là đáp án "khuyến nghị" trong đề thi
- **Dùng AWS SDK để gửi email** → luôn cần IAM credentials, SMTP credential vô nghĩa ở đây

### TD explanation

Amazon Simple Email Service (Amazon SES) is a scalable and secure cloud-based email-sending service designed to help businesses send marketing, transactional, and other types of professional emails.

The Amazon SES SMTP endpoint requires that all connections be encrypted using Transport Layer Security (TLS). Amazon SES supports two mechanisms for establishing a TLS-encrypted connection: STARTTLS and TLS Wrapper.

STARTTLS is a means of upgrading an unencrypted connection to an encrypted connection. To set up a STARTTLS connection, the SMTP client connects to the Amazon SES SMTP endpoint on port 25, 587, or 2587, issues an EHLO command, and waits for the server to announce that it supports the STARTTLS SMTP extension. The client then issues the STARTTLS command, initiating TLS negotiation. When negotiation is complete, the client issues an EHLO command over the new encrypted connection, and the SMTP session proceeds normally.

Amazon SES supports sending emails through two main interfaces: the Simple Mail Transfer Protocol (SMTP) and the SES API.

In the scenario, since the company’s legacy application is already configured to connect to an SMTP server, they can simply replace the existing SMTP settings with those of Amazon SES. This involves generating new SMTP credentials via the Amazon SES console and updating the application to use them. Additionally, it is recommended to switch from the currently used port 25 to port 587 for STARTTLS encryption. This is beneficial not only for enhanced security but also because Amazon EC2 instances are throttled on port 25, and using port 587 avoids the need to request the lifting of these limitations.

Hence, the correct answer is: Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential and update the connection to the Amazon SES SMTP endpoint. Change the port settings to 587 to use STARTTLS.

When using the SMTP interface to send email through Amazon SES, SMTP credentials should be used, and not IAM roles or IAM user credentials. SMTP credentials are separate and are used specifically for connecting to the Amazon SES SMTP interface. Thus, the following options are incorrect:

– Create an IAM Role for the application with ses:SendEmail and ses:SendRawEmail permissions and attach it to the EC2 instance. Update the SMTP settings in the application to connect to the Amazon SES SMTP. Update the port number to 465 to use TLS Wrapper.

– Create an IAM user and grant it permission to send emails through Amazon SES. Generate access keys for this IAM user. Update the application to use these access keys and connect to the Amazon SES SMTP endpoint. Change the port to 587 to use STARTTLS.

The option that says: Create an SMTP credential through the Amazon SES console. Configure the application to use the SMTP credential. Use the AWS SDK for Amazon SES to send emails  is incorrect. This approach would mean that you’re sending through the API and not through the SMTP interface. This would require the application to use AWS access key credentials, either from an IAM role attached to the EC2 instance or from an IAM user, not an SMTP credential.

References:

https://docs.aws.amazon.com/ses/latest/DeveloperGuide/security.html

https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-connect.html

https://docs.aws.amazon.com/ses/latest/dg/send-using-smtp-programmatically.html

 

Check out this Amazon SES Cheat Sheet:

https://tutorialsdojo.com/amazon-ses/

</details>

---

# Group E — Serverless + DB (4)

<a id="q5"></a>

## Q5

A media company has a pipeline that extracts information on photos uploaded to an Amazon S3 bucket. Each upload on the S3 bucket sends a notification to an Amazon SNS topic. The pipeline includes several AWS Lambda functions that are subscribed to the SNS topic. For each notification message, the functions are triggered to extract the metadata information from the corresponding S3 object which is then written to the Amazon RDS MySQL DB instance. During peak traffic, the users complain that metadata updates are slow or are sometimes lost. This is because the RDS CPU utilization becomes very high which causes the AWS Lambda invocations to fail.

Which of the following steps should be implemented to resolve this issue? (Select TWO.)

- **A.** Create additional Amazon RDS read replicas in order to accommodate the increased load traffic during peak hours.
- **B.** Configure the Delivery Retry Policy of the SNS Topic to have multiple retries with exponential backoff. Set the Message Delivery Status Logging option of the SNS topic to allow the Lambda functions to retry processing the object.
- **C.** Implement an Amazon RDS Proxy in front of the Amazon RDS instance. Configure the AWS Lambda functions to use this proxy when connecting to the RDS instance.
- **D.** For each AWS Lambda function, implement an Amazon SQS standard queue that is subscribed to the Amazon SNS topic. Configure each Lambda function to consume the message from their corresponding SQS queue.
- **E.** Ensure that RDS Data API is enabled for the Amazon RDS instance. Configure the AWS Lambda functions to use RDS Data API when connecting to the RDS instance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D · **You picked:** B, C

🔑 **Key words:** SNS → many Lambdas → RDS; CPU high; slow/lost updates at peak

🪤 **Your trap:** SNS retry policy doesn't reduce DB load

🧠 **Rule:** Lambda overwhelming RDS → RDS Proxy + SQS queue per Lambda to buffer.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 upload → SNS topic → nhiều Lambda functions (mỗi ảnh trigger nhiều function)
                              │
                              ▼
                    Amazon RDS MySQL (ghi metadata)

Peak traffic:
  RDS CPU tăng cao → Lambda ghi thất bại → metadata cập nhật chậm/mất
```

Đề chọn HAI hành động. Đáp án đúng: **C** (RDS Proxy) và **D** (SQS queue đệm cho mỗi Lambda). Anh chọn **B, C** — đúng C nhưng sai ở B.

#### Vì sao C và D đúng — giải quyết đúng gốc rễ: quá nhiều Lambda mở connection cùng lúc

Vấn đề thực chất là **lượng connection tới RDS tăng đột biến** khi traffic đỉnh (mỗi lần SNS publish trigger hàng loạt Lambda, mỗi Lambda cố mở connection riêng tới DB) — vượt quá khả năng RDS xử lý, khiến CPU cao và Lambda bị fail.

- **D — SQS standard queue đệm giữa SNS và mỗi Lambda:** biến luồng "nổ" tức thời thành hàng đợi được xử lý tuần tự/có kiểm soát tốc độ (Lambda kéo message theo nhịp độ nó có thể xử lý, không bị dồn tất cả cùng lúc). Đây là bước **giảm tải trực tiếp** áp lực ghi vào RDS.
- **C — RDS Proxy:** tạo **connection pool** dùng chung giữa các lần Lambda invoke, tránh việc mỗi invocation mở connection mới tốn CPU/memory của RDS. RDS Proxy còn tự động **queue/throttle** các connection request không phục vụ được ngay, giúp DB "chịu đựng" traffic đột biến mà không sập.

Kết hợp D (giảm tốc độ dồn request) + C (giảm chi phí mỗi connection) → giải quyết cả hai chiều của vấn đề.

#### Vì sao B (anh chọn) sai

B chỉ cấu hình **retry policy của SNS** (exponential backoff) và logging — về bản chất đây là **retry khi Lambda fail**, không hề giảm tải cho RDS. Ngược lại, retry nhiều lần vào một DB đang quá tải CPU chỉ khiến tình trạng ghi chậm/mất dữ liệu kéo dài thêm, không giải quyết nguyên nhân gốc.

#### Vì sao A và E sai

- **A — Thêm RDS read replica:** read replica **chỉ đọc**, không nhận được **write** từ Lambda. Vấn đề ở đây là ghi metadata (write), read replica hoàn toàn không giúp gì.
- **E — RDS Data API:** Data API chỉ dùng được với **Aurora Serverless**, không áp dụng cho RDS MySQL thông thường như trong đề.

| Phương án | Giải quyết đúng vấn đề? | Vì sao |
|---|---|---|
| **C. RDS Proxy** | Có | Connection pooling, giảm CPU/memory overhead mỗi connection |
| **D. SQS đệm trước mỗi Lambda** | Có | Giảm tốc độ dồn request tới RDS |
| B. SNS retry policy | Không | Chỉ retry, không giảm tải |
| A. Thêm read replica | Không | Không xử lý được write |
| E. RDS Data API | Không | Chỉ dùng cho Aurora Serverless |

#### Quy tắc nhớ cho thi

- **"Nhiều Lambda cùng ghi vào RDS, CPU cao, connection storm"** → **RDS Proxy** (pooling) là gần như luôn đúng.
- **"SNS fan-out gây quá tải downstream"** → chèn **SQS** vào giữa để buffer/throttle tốc độ xử lý.
- **Retry policy (SNS/SQS)** → chỉ giúp không mất message, không giúp giảm tải hệ thống downstream.
- **Read replica** → chỉ giải quyết vấn đề đọc (read), không bao giờ giúp với write bottleneck.
- **RDS Data API** → chỉ dành cho Aurora Serverless, không áp dụng RDS MySQL/PostgreSQL thường.

### TD explanation

Amazon RDS Proxy is a fully managed, highly available database proxy for Amazon Relational Database Service (RDS) that makes applications more scalable, more resilient to database failures, and more secure. Many applications, including those built on modern serverless architectures, can have a large number of open connections to the database server and may open and close database connections at a high rate, exhausting database memory and compute resources. By using Amazon RDS Proxy, you can allow your applications to pool and share database connections to improve their ability to scale.

RDS Proxy makes applications more resilient to database failures by automatically connecting to a standby DB instance while preserving application connections. RDS Proxy also enables you to enforce AWS Identity and Access Management (IAM) authentication for databases and securely store credentials in AWS Secrets Manager.

Using RDS Proxy, you can handle unpredictable surges in database traffic that otherwise might cause issues due to oversubscribing connections or creating new connections at a fast rate. RDS Proxy establishes a database connection pool and reuses connections in this pool without the memory and CPU overhead of opening a new database connection each time. To protect the database against oversubscription, you can control the number of database connections that are created.

RDS Proxy queues or throttles application connections that can’t be served immediately from the pool of connections. Although latencies might increase, your application can continue to scale without abruptly failing or overwhelming the database.

The option that says: Implement an Amazon RDS Proxy in front of the Amazon RDS instance. Configure the AWS Lambda functions to use this proxy when connecting to the RDS instance is correct. RDS Proxy allows applications to pool and share connections established with the database, improving database efficiency and application scalability, especially during write operations. 

The option that says: For each AWS Lambda function, implement an Amazon SQS standard queue that is subscribed to the Amazon SNS topic. Configure each Lambda function to consume the message from their corresponding SQS queue is correct. This will help pool the metadata information until the AWS Lambda functions can process and write them to the Amazon RDS instance.

The option that says: Configure the Delivery Retry Policy of the SNS Topic to have multiple retries with exponential backoff. Set the Message Delivery Status Logging option of the SNS topic to allow the Lambda functions to retry processing the object is incorrect. The retries from Lambda functions may alleviate the lost metadata problem; however, this will still result in slow metadata updates because the RDS instance is overwhelmed with write requests. 

The option that says: Ensure that RDS Data API is enabled for the Amazon RDS instance. Configure the AWS Lambda functions to use RDS Data API when connecting to the RDS instance is incorrect. RDS Data API is designed to be used for Aurora Serverless service, not for RDS instances. 

The option that says: Create additional Amazon RDS read replicas in order to accommodate the increased load traffic during peak hours is incorrect. RDS read replicas are read-only instances, they can’t accept the write requests from the Lambda functions. 

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html

https://aws.amazon.com/rds/proxy/

https://aws.amazon.com/about-aws/whats-new/2021/03/amazon-rds-proxy-adds-read-only-endpoints-for-amazon-aurora-replicas/

 

Check out the Amazon RDS Cheat Sheet:

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q58"></a>

## Q58

A company has built a REST API that retrieves data from an Amazon Aurora MySQL database. The API uses an AWS Lambda function as its backend and is served via an API Gateway Regional endpoint. The API is deployed in an AWS region close to its primary user base for optimal performance. During beta testing, the developers have noticed many idle database connections during periods of high demand, which impacts the application.

Which set of solutions could the company take to fix the issue? (Select TWO)

- **A.** Reconfigure the API Gateway to use an edge-optimized endpoint and set a larger rate limit value.
- **B.** Initialize the code for database connection outside the event handler of the Lambda function.
- **C.** Allocate Provisioned Concurrency for the Lambda function.
- **D.** Increase the Reserved Concurrency for the Lambda function and set a higher memory allocation.
- **E.** Create an RDS Proxy for the Aurora database. Modify the function to use the proxy endpoint.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** A, E

🔑 **Key words:** Lambda + Aurora; many idle DB connections at high demand

🪤 **Your trap:** API Gateway endpoint type/rate limits irrelevant

🧠 **Rule:** Connection storm → init DB connection outside handler (reuse) + RDS Proxy.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client → API Gateway (Regional endpoint) → Lambda → Aurora MySQL

Beta test, high demand:
  → Nhiều connection tới DB bị IDLE, ảnh hưởng ứng dụng
```

Đề chọn HAI hành động. Đáp án đúng: **B** (khởi tạo connection ngoài event handler) và **E** (RDS Proxy). Anh chọn **A, E** — đúng E nhưng sai ở A.

#### Vì sao B và E đúng — cùng nhắm vào "tái sử dụng connection"

Vấn đề là **nhiều connection idle** khi traffic cao — dấu hiệu kinh điển của việc Lambda **mở connection mới ở mỗi lần invoke** thay vì tái sử dụng.

- **B — Khởi tạo code kết nối DB bên ngoài event handler:** Lambda tái sử dụng **execution environment** (container) giữa các lần gọi liên tiếp khi container còn "ấm" (warm). Nếu đoạn code mở connection nằm ngoài handler (ở phần khởi tạo/global scope), connection được giữ và tái dùng cho các invocation tiếp theo trên cùng container — giảm số connection cần mở mới, giảm cold-start overhead, và tránh làm cạn giới hạn connection của DB.
- **E — RDS Proxy:** khi Lambda scale ra hàng nghìn instance đồng thời (mỗi container/mỗi instance có thể vẫn cần connection riêng dù đã tối ưu B), RDS Proxy đứng giữa Lambda và Aurora, duy trì một **connection pool ấm sẵn**, cho phép nhiều Lambda function dùng chung pool thay vì mỗi cái tự mở/đóng connection trực tiếp tới DB.

Hai giải pháp này bổ trợ nhau: B giảm số connection cần mở ở tầng từng container Lambda, E xử lý phần còn lại ở tầng tổng thể khi Lambda scale rộng.

#### Vì sao A (anh chọn) sai

**Edge-optimized endpoint + tăng rate limit của API Gateway** không liên quan gì đến vấn đề connection tới database. Edge-optimized chỉ giúp giảm latency cho client ở nhiều vị trí địa lý (dùng CloudFront phía trước). Tăng rate limit thậm chí có thể **làm trầm trọng thêm** vấn đề vì cho phép nhiều request hơn tới Lambda, kéo theo nhiều connection tới DB hơn trong lúc DB đã quá tải.

#### Vì sao C và D sai

- **C — Provisioned Concurrency:** giữ sẵn một số lượng instance Lambda "ấm", giảm cold start, nhưng **không giải quyết vấn đề idle connection** — vẫn có thể có nhiều connection mở đồng thời nếu code không tái sử dụng đúng cách.
- **D — Tăng Reserved Concurrency + memory:** tăng concurrency cho phép **nhiều Lambda instance chạy song song hơn**, tức là **tăng thêm số connection đồng thời tới DB** — phản tác dụng. Tăng memory chỉ giúp Lambda chạy nhanh hơn, không liên quan đến connection pooling.

| Phương án | Giải quyết idle connections? | Vì sao |
|---|---|---|
| **B. Init connection ngoài handler** | Có | Tái sử dụng connection giữa các invocation trên cùng container |
| **E. RDS Proxy** | Có | Connection pooling dùng chung cho nhiều Lambda |
| A. Edge-optimized + rate limit | Không | Không liên quan tầng DB, có thể làm nặng thêm |
| C. Provisioned Concurrency | Không | Chỉ giảm cold start |
| D. Reserved Concurrency + memory | Không | Có thể tăng thêm số connection đồng thời |

#### Lưu ý thực tế

- Best practice của AWS Lambda: mọi kết nối tới tài nguyên bên ngoài (DB, API...) nên được khởi tạo **ở ngoài handler function**, tận dụng container reuse, thay vì mở lại mỗi lần invoke.
- RDS Proxy đặc biệt hữu ích với kiến trúc serverless (Lambda) vì Lambda có thể scale ra rất nhanh, dễ vượt giới hạn connection tối đa mà RDS/Aurora cho phép.

#### Quy tắc nhớ cho thi

- **"Nhiều idle connection tới DB khi traffic cao, dùng Lambda"** → luôn nghĩ tới: (1) khởi tạo connection ngoài handler, (2) RDS Proxy.
- **API Gateway endpoint type (edge/regional) và rate limit** → không liên quan đến connection pooling ở tầng database.
- **Provisioned/Reserved Concurrency** → giải quyết vấn đề cold start/độ song song, không giải quyết vấn đề connection pooling.

### TD explanation

When using AWS Lambda, initializing the database connection outside the event handler leverages Lambda’s ability to reuse containers for multiple invocations. This approach promotes connection reuse, reducing the overhead of constantly establishing new connections with every invocation. By doing so, you can minimize cold start latencies and avoid rapidly exhausting the database’s connection limits, especially during traffic spikes.

Another way of fixing many idle connections is to use RDS Proxy. Opening a connection consumes resources on the database server. Since Lambda functions can scale to tens of thousands of concurrent connections, your database needs more resources to open and maintain connections instead of executing queries. The maximum number of connections a database can support is largely determined by the amount of memory allocated to it. Upgrading to a database instance with higher memory is a straightforward way of solving the problem. Another approach would be to maintain a connection pool that clients can reuse.

RDS Proxy helps you manage a large number of connections from Lambda to an RDS database by establishing a warm connection pool to the database. Your Lambda functions interact with RDS Proxy instead of your database instance. It handles the connection pooling necessary for scaling many simultaneous connections created by concurrent Lambda functions. This allows your Lambda applications to reuse existing connections rather than creating new connections for every function invocation.

Thus, the correct answers are:

– Initialize the code for database connection outside the event handler of the Lambda function.

– Create an RDS Proxy for the Aurora database. Modify the function to use the proxy endpoint.

The option that says: Allocate Provisioned Concurrency for the Lambda function is incorrect. This option ensures that a specified number of Lambda instances are always warm and ready to serve requests. While this could reduce cold start latencies, it wouldn’t resolve the issue of many idle database connections.

The option that says: Reconfigure the API Gateway to use an edge-optimized endpoint and set a larger rate limit value is incorrect. Using an Edge-optimized endpoint would simply help decrease latency for clients in multiple geographical locations. It’s not a solution for the issue of many idle database connections. Moreover, increasing the rate limit may exacerbate the problem if the Lambda function creates more connections during periods of high demand.

The option that says: Increase the Reserved Concurrency for the Lambda function and set a higher memory allocation is incorrect. Increasing the reserved concurrency limit without connection pooling might lead to more simultaneous database connections, which is counterproductive. Also, increasing the Lambda function’s memory would only make it run processes faster and won’t have a significant effect on getting rid of the error.

 

References:

https://aws.amazon.com/rds/proxy/

https://aws.amazon.com/blogs/compute/using-amazon-rds-proxy-with-aws-lambda/

https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html

 

Check out this Amazon RDS Cheat Sheet:

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q30"></a>

## Q30

A company is running a stateless application on Amazon ECS with AWS Fargate. The Fargate cluster runs behind an Application Load Balancer (ALB) that serves internet traffic. The Amazon Aurora MySQL database cluster is on a private subnet in the same VPC.  To connect to the database, the database hostname is passed to the application using the DB_HOST environment variable. The database password is encrypted in AWS Secrets Manager and is passed to the application using the DB_PASSWORD environment variable. Upon running the Fargate tasks, the application was unable to access the database.

Which of the following actions should be taken in order to resolve this issue? (Select THREE.)

- **A.** Set the “DB_PASSWORD” environment variable as “ValueFrom” with the secret name from AWS Secrets Manager.
- **B.** Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database instance endpoint.
- **C.** Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database cluster endpoint.
- **D.** Configure the Aurora MySQL database security group to allow inbound traffic from the AWS Fargate cluster on the TCP port 3306.
- **E.** Set the “DB_PASSWORD” environment variable as “ValueFrom” with the ARN of the secret from AWS Secrets Manager.
- **F.** Configure the AWS Fargate cluster security group to allow inbound traffic from the Amazon Aurora MySQL cluster on the TCP port 3306.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D, E · **You picked:** D, E, F

🔑 **Key words:** Fargate can't reach Aurora; DB_HOST env var; password in Secrets Manager

🪤 **Your trap:** SG direction reversed (inbound on Fargate SG)

🧠 **Rule:** Fix = cluster endpoint in DB_HOST + DB SG inbound from Fargate:3306 + secret via ValueFrom.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internet → ALB → ECS Fargate task (private subnet, cùng VPC)
                        │  env vars:
                        │   DB_HOST = ???
                        │   DB_PASSWORD = ValueFrom ???
                        ▼
                 Aurora MySQL cluster (private subnet)

Kết quả: ứng dụng KHÔNG kết nối được database
```

Đề chọn BA hành động. Đáp án đúng: **C, D, E**. Anh chọn **D, E, F** — sai ở F, thiếu C (chọn nhầm B).

#### Sai lầm 1 — hướng security group (F vs D)

Đây là lỗi hay gặp nhất: **phải mở inbound trên security group của bên NHẬN kết nối, không phải bên KHỞI TẠO kết nối.**

```
Fargate task  ───(khởi tạo kết nối tới)───►  Aurora DB
   (client)                                    (server)

Cần: SG của Aurora  → cho phép INBOUND từ SG của Fargate, port 3306
KHÔNG cần: SG của Fargate → cho phép inbound từ Aurora
```

- **D đúng:** mở inbound trên **Aurora security group**, nguồn là Fargate cluster, cổng 3306 — đúng hướng, vì Fargate là bên chủ động kết nối tới DB.
- **F sai (anh chọn):** mở inbound trên **Fargate security group** cho phép traffic từ Aurora — ngược hướng hoàn toàn. Security group hoạt động stateful nên response traffic tự động được phép, không cần rule inbound riêng cho chiều trả lời.

#### Sai lầm 2 — DB_HOST dùng instance endpoint hay cluster endpoint (C vs B)

Aurora có nhiều loại endpoint khác nhau: **cluster endpoint (writer endpoint)** luôn trỏ tới instance primary hiện tại và là **endpoint duy nhất chấp nhận write**; **instance endpoint** trỏ tới một instance cụ thể (có thể là replica, không hỗ trợ ghi).

- **C đúng:** `DB_HOST` phải dùng **cluster endpoint** — đây là endpoint chính xác cho cả đọc và ghi, và tự động trỏ đúng instance primary hiện tại kể cả khi có failover.
- **B sai:** dùng **instance endpoint** — không đảm bảo là instance ghi được, và nếu instance đó thay đổi vai trò (failover), endpoint này không tự cập nhật theo.

#### Sai lầm 3 — ValueFrom dùng tên secret hay ARN (E vs A)

Trong container definition của ECS, khi inject secret làm environment variable, trường `ValueFrom` phải là **ARN đầy đủ của secret** trong Secrets Manager, không phải tên secret (secret name).

- **E đúng:** `DB_PASSWORD` = `ValueFrom` = **ARN của secret**.
- **A sai (đây là điểm anh chưa xét tới):** dùng tên secret thay vì ARN — ECS sẽ không resolve đúng, task sẽ không lấy được giá trị mật khẩu.

| Điểm quyết định | Đáp án đúng | Đáp án sai tương ứng | Vì sao sai |
|---|---|---|---|
| Hướng SG | D (SG Aurora ← Fargate) | F (SG Fargate ← Aurora) | Ngược hướng, SG là stateful nên không cần rule chiều ngược |
| DB_HOST | C (cluster endpoint) | B (instance endpoint) | Instance endpoint không đảm bảo ghi được, không tự theo failover |
| ValueFrom | E (ARN của secret) | A (tên secret) | ECS cần ARN để resolve secret, không nhận tên |

#### Lưu ý thực tế

- Security group luôn **stateful**: chỉ cần mở inbound ở phía server (Aurora) cho traffic tới từ client (Fargate); traffic phản hồi được tự động cho phép, không cần thêm rule.
- Với Aurora, luôn ưu tiên **cluster endpoint** cho write, chỉ dùng instance endpoint khi cần trỏ đích danh một instance cụ thể (ví dụ để đọc từ một replica nhất định).

#### Quy tắc nhớ cho thi

- **"Ứng dụng không kết nối được DB" trong VPC** → kiểm tra ngay: SG của DB có mở inbound từ SG của app không (không phải chiều ngược lại).
- **"DB_HOST cho Aurora"** → mặc định dùng **cluster endpoint**, trừ khi đề yêu cầu rõ ràng đọc từ replica cụ thể.
- **ECS secrets `ValueFrom`** → luôn là **ARN**, không phải tên secret.

### TD explanation

Amazon Aurora typically involves a cluster of DB instances instead of a single instance. Each connection is handled by a specific DB instance. When you connect to an Aurora cluster, the host name and port that you specify point to an intermediate handler called an endpoint.

Each Aurora DB cluster has one cluster endpoint and one primary DB instance. A cluster endpoint (or writer endpoint) for an Aurora DB cluster connects to the current primary DB instance for that DB cluster. This endpoint is the only one that can perform write operations such as DDL statements. Because of this, the cluster endpoint is the one that you connect to when you first set up a cluster or when your cluster only contains a single DB instance.

An instance endpoint connects to a specific DB instance within an Aurora cluster. Each DB instance in a DB cluster has its own unique instance endpoint. So there is one instance endpoint for the current primary DB instance of the DB cluster, and there is one instance endpoint for each of the Aurora Replicas in the DB cluster.

Amazon ECS enables you to inject sensitive data into your containers by storing your sensitive data in AWS Secrets Manager secrets and then referencing them in your container definition. Sensitive data stored in Secrets Manager secrets can be exposed to a container as environment variables or as part of the log configuration.

When you inject a secret as an environment variable, you can specify the full contents of a secret, a specific JSON key within a secret, or a specific version of a secret to inject.

Within your container definition, you can specify the following:

-The secrets object containing the name of the environment variable to set in the container.

-The Amazon Resource Name (ARN) of the Secrets Manager secret.

-Additional parameters that contain the sensitive data to present to the container.

The option that says: Set the “DB_PASSWORD” environment variable as “ValueFrom” with the ARN of the secret from AWS Secrets Manager is correct. The environment variable should contain the ARN from AWS Secrets Manager.

The option that says: Configure the Aurora MySQL database security group to allow inbound traffic from the AWS Fargate cluster on the TCP port 3306 is correct. You need to ensure that the Aurora database is open to accept connections from the Fargate cluster.

The option that says: Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database cluster endpoint is correct. The cluster endpoint should be used as “Value” of the environment variable. This is the main endpoint that accepts read/write connections. 

The option that says: Set the “DB_PASSWORD” environment variable as “ValueFrom” with the secret name from AWS Secrets Manager is incorrect. You should use the ARN of the secret from the Secrets Manager, not the secret name.

The option that says: Ensure that the “DB_HOST” environment variable is configured with the hostname of the Aurora database instance endpoint is incorrect. Amazon Aurora has different instance endpoints for write and reader nodes. It is recommended to use the cluster endpoint here because this is the one that can perform both read/write operations. 

The option that says: Configure the AWS Fargate cluster security group to allow inbound traffic from the Amazon Aurora MySQL cluster on the TCP port 3306 is incorrect. The AWS Fargate cluster will connect to the database, therefore, the database must allow connections from the Aurora cluster.

 

References:

https://aws.amazon.com/premiumsupport/knowledge-center/ecs-data-security-container-task/

https://docs.aws.amazon.com/AmazonECS/latest/userguide/specifying-sensitive-data-secrets.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html

 

Check out these Amazon Aurora and AWS Fargate Cheat Sheets:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/aws-fargate/

</details>

<a id="q13"></a>

## Q13

A company is planning to host a two-tier application on AWS. They’ve chosen to use the LAMP (Linux, Apache, MySQL, PHP) stack, wherein a stateful application will run on Amazon EC2 instances, and the database will be managed using Amazon Aurora.

The customer base is expected to grow rapidly, which would likely result in unprecedented traffic spikes. The design must ensure that both the application and the database tiers can scale automatically in response to changes in demand.

Which combination of solutions will meet the requirements? (Select TWO.)

- **A.** Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy that will automatically scale the Aurora writer instances
- **B.** Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy and apply it to the Amazon Aurora DB cluster to automatically scale Aurora read replicas.
- **C.** Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable Client Port preservation and select round-robin as the load balancing algorithm.
- **D.** Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to a Network Load Balancer (NLB). Enable sticky sessions and select Least Outstanding Requests (LOR) as the load balancing algorithm.
- **E.** Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable sticky sessions and select round-robin as the load balancing algorithm for the target groups.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** A, D

🔑 **Key words:** stateful LAMP on EC2 + Aurora; both tiers auto-scale

🪤 **Your trap:** Aurora can't auto-scale writers; NLB = L4 no HTTP stickiness

🧠 **Rule:** Aurora Auto Scaling = READ replicas only; stateful web tier → ALB + sticky sessions + ASG.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
LAMP stack, 2-tier:
  EC2 (Apache/PHP) ── STATEFUL (session lưu tại instance) ── phía trước ALB/NLB?
        │
        ▼
  Aurora MySQL

Yêu cầu: CẢ HAI tầng đều phải auto-scale khi traffic tăng đột biến
```

Đề chọn HAI hành động. Đáp án đúng: **B** (Aurora Auto Scaling cho read replicas) + **E** (ASG + ALB + sticky sessions + round-robin). Anh chọn **A, D** — sai cả hai.

#### Vì sao A (anh chọn) sai — Aurora không auto-scale writer

Aurora Auto Scaling **chỉ điều chỉnh số lượng Aurora Replica (read replicas)** trong cluster theo policy dựa trên CloudWatch metrics — nó **không** hỗ trợ tự động thêm/bớt writer instance. Aurora (giống RDS nói chung) chỉ có **một writer instance chính** tại một thời điểm; không có khái niệm "nhiều writer auto-scale". Vì vậy A mô tả một tính năng không tồn tại.

**B đúng** vì áp policy Aurora Auto Scaling đúng đối tượng: scale **read replicas**, giúp tầng đọc chịu được traffic tăng.

#### Vì sao D (anh chọn) sai — NLB không phù hợp cho ứng dụng LAMP stateful qua HTTP

NLB hoạt động ở **Layer 4 (transport)**, xử lý TCP/UDP thuần, **không có khái niệm HTTP/HTTPS session hay cookie-based stickiness** đúng nghĩa ứng dụng web. Với một ứng dụng LAMP điển hình (HTTP/HTTPS, cần duy trì session ở tầng ứng dụng), NLB thiếu tính năng cần thiết để đảm bảo đúng UX cho ứng dụng web layer 7.

**E đúng** vì dùng **ALB (Layer 7)** — hỗ trợ đầy đủ HTTP, có tính năng **sticky sessions** (session affinity dựa trên cookie) để đảm bảo một user luôn được route về đúng instance đang giữ session của họ — điều bắt buộc với ứng dụng "stateful" như đề mô tả (không dùng external session store).

#### Vì sao C sai

C dùng ALB nhưng chọn **"Enable Client Port preservation"** thay vì sticky sessions. Client Port Preservation chỉ giữ nguyên source port gốc của client khi forward tới backend — mục đích hoàn toàn khác (phục vụ logging/tracing/troubleshooting mạng), **không có tác dụng "ghim" session người dùng vào một instance cụ thể**. Ứng dụng stateful cần đúng cơ chế sticky sessions của ALB, không phải Client Port Preservation.

| Vấn đề | Lựa chọn đúng | Lựa chọn sai tương ứng | Vì sao sai |
|---|---|---|---|
| Scale tầng Aurora | B: Auto Scaling cho **read replicas** | A: Auto Scaling cho **writer** | Aurora không hỗ trợ multi-writer auto-scale |
| Scale + giữ session tầng EC2 | E: **ALB** + sticky sessions + round-robin | D: **NLB** + sticky sessions + LOR | NLB là Layer 4, thiếu HTTP session stickiness thật sự |
| — | — | C: ALB + Client Port Preservation | Client Port Preservation ≠ session stickiness |

#### Quy tắc nhớ cho thi

- **"Aurora Auto Scaling"** → luôn hiểu là scale **read replicas**, không bao giờ là writer.
- **Ứng dụng "stateful", session lưu tại instance, không có session store ngoài** → cần **ALB + sticky sessions**, không dùng NLB (thiếu tầng L7).
- **NLB** → chọn khi cần hiệu năng TCP cực cao, giữ nguyên IP nguồn, không cần logic HTTP — không phải lựa chọn cho ứng dụng web cần session affinity thực sự.
- **Client Port Preservation** → tính năng khác hẳn sticky sessions, dễ gây nhầm lẫn trên đề thi vì tên nghe giống "giữ trạng thái kết nối".

### TD explanation

Aurora Auto Scaling enables your Aurora DB cluster to handle sudden increases in connectivity or workload by dynamically adjusting the number of its Aurora Replicas. This feature is available for both Aurora MySQL and Aurora PostgreSQL. You define and apply a scaling policy to an Aurora DB cluster. The scaling policy defines the minimum and maximum number of Aurora Replicas that Aurora Auto Scaling can manage. Based on the policy, Aurora Auto Scaling adjusts the number of Aurora Replicas up or down in response to actual workloads, determined by using Amazon CloudWatch metrics and target values.

An Auto Scaling group contains a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

Target groups route requests to one or more registered targets, such as EC2 instances, using the protocol and port number that you specify. You can register a target with multiple target groups. You can configure health checks on a per-target group basis. Health checks are performed on all targets registered to a target group that is specified in a listener rule for your load balancer.

By default, the round-robin routing algorithm is used to route requests at the target group level. You can specify the least outstanding requests routing algorithm instead.

Consider using least outstanding requests (LOR) when the requests for your application vary in complexity or your targets vary in processing capability. Round robin is a good choice when the requests and targets are similar or if you need to distribute requests equally among targets. You can compare the effect of round robin versus the least outstanding requests using the following CloudWatch metrics: RequestCount, TargetConnectionErrorCount, and TargetResponseTime.

In the scenario, using Auto Scaling groups would help ensure that you have the correct number of Amazon EC2 instances available to handle the load for the application. By attaching the ASG to an ALB, you can distribute incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. Sticky sessions enable the load balancer to bind a user’s session to a specific instance, ensuring that all requests from the user during the session are sent to the same instance. This is crucial for the correct operation of stateful applications, especially if you’re not using any external session store.

Hence the correct answers are:

– Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy and apply it to the Amazon Aurora DB cluster to automatically scale Aurora read replicas.

– Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable sticky sessions and select round-robin as the load-balancing algorithm for the target groups.

The option that says: Launch a new Amazon Aurora MySQL database. Create an Aurora Auto Scaling policy that will automatically scale the Aurora writer instances is incorrect because having multiple Amazon Aurora writer instances is not fully supported in Amazon Aurora or Amazon RDS. You can only enable Aurora Auto Scaling at the DB cluster level, not on the writer instances.

The option that says: Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to a Network Load Balancer (NLB). Enable sticky sessions and select Least Outstanding Requests (LOR) as the load balancing algorithm is incorrect. A Network Load Balancer (NLB) operates at the transport layer (Layer 4) of the OSI model and is primarily designed to handle TCP traffic. It lacks built-in support for HTTP and HTTPS protocols, which is a crucial requirement for a LAMP-based application.

The option that says: Use an Auto Scaling Group (ASG) for the EC2 instances. Attach the ASG to an Application Load Balancer (ALB). Enable Client Port preservation and select round-robin as the load balancing algorithm is incorrect. Client Port Preservation simply preserves the source client port, allowing backend applications to see the original client-side source port. It’s not for binding user sessions to a specific EC2 instance.

 

References:

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html

 

Check out these Cheat sheets for Amazon Aurora and AWS Auto Scaling:

https://tutorialsdojo.com/amazon-aurora/

https://tutorialsdojo.com/aws-auto-scaling/

</details>

---

# Group F — Networking / S3 / perf (7)

<a id="q12"></a>

## Q12

A company hosts a web application service in the AWS eu-east-1 region. The application serves weather maps to users. The maps are updated every 1 hour and are stored in an Amazon S3 bucket along with static web content. The web application is behind an Amazon CloudFront distribution. The company has expanded and now provides the same service to North American users. Reports indicate that the viewing experience for weather maps is slow at times in this region.

Which combination of actions can provide the LEAST latency between the users and the application? (Select TWO.)

- **A.** Configure S3 cross-region replication from the eu-east-1 bucket to a new bucket in the us-east-1 region.
- **B.** Create a new AWS Global Accelerator endpoint for the us-east-1 bucket and add it as an origin for the CloudFront distribution. Use Lambda@Edge to modify North American requests to use this new origin.
- **C.** Create a Lambda@Edge function that modifies requests from North American users to use the S3 Transfer Acceleration endpoint of the S3 bucket in the us-east-1 region.
- **D.** Create a Lambda@Edge that modifies requests from North American users to retrieve files from a new us-east-1 S3 bucket.
- **E.** Create a new AWS Global Accelerator endpoint for the eu-west-1 S3 bucket. Configure additional endpoint groups in the us-east-1 S3 bucket for TCP port 443.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** B, C

🔑 **Key words:** S3 origin in EU; NA users slow; LEAST latency

🪤 **Your trap:** Global Accelerator can't front S3; S3TA doesn't move data (REPEAT)

🧠 **Rule:** Move data close → S3 CRR to us-east-1 + Lambda@Edge switches origin for NA users.

### 🇻🇳 Phân tích chi tiết

> ⚠️ **Lỗi lặp lại:** Đây là lần thứ hai (ít nhất) Anh vấp đúng combo "Global Accelerator không front được S3" + "S3 Transfer Acceleration không di chuyển dữ liệu". Cần khắc sâu quy tắc này trước khi vào phòng thi thật.

#### Tình huống

```
eu-east-1 (origin gốc)                    us-east-1 (users NA)
┌─────────────────────┐                   ┌──────────────────┐
│ S3 bucket            │   CloudFront      │  Người dùng NA    │
│ (weather maps,       │◄─────────────────►│  phàn nàn: chậm   │
│  update mỗi 1h)      │   distribution     │                  │
└─────────────────────┘                   └──────────────────┘

Yêu cầu: LEAST latency cho NA users
→ Chọn 2 hành động
```

Đáp án đúng: **A (S3 CRR sang us-east-1) + D (Lambda@Edge đổi origin sang bucket us-east-1)**. Anh chọn **B, C** — cả hai đều sai vì cùng một lý do gốc: **không có bước nào đưa dữ liệu đến gần user hơn**.

#### Vì sao A + D đúng — phải "di chuyển dữ liệu", không chỉ "di chuyển đường đi"

Vấn đề gốc: dữ liệu vật lý (object trong S3) vẫn nằm ở eu-east-1. Muốn giảm latency thực sự, phải có bản copy dữ liệu ở gần user (us-east-1), rồi định tuyến user đến đúng bản copy đó.

```
D: Lambda@Edge (chạy tại edge location gần user)
   → khi thấy request đến từ NA
   → sửa request để lấy file từ BUCKET us-east-1 (không phải bucket EU)

A: S3 Cross-Region Replication (CRR)
   → tự động, bất đồng bộ copy object từ bucket eu-east-1
   → sang bucket mới us-east-1
   → NHỜ ĐÓ bucket mà D trỏ tới thực sự có dữ liệu gần user
```

A và D là hai nửa của cùng một giải pháp: A tạo ra bản dữ liệu gần user, D điều hướng user đến bản đó. Thiếu một trong hai thì vô nghĩa.

#### Vì sao B sai — Global Accelerator không front được S3

**B: "Global Accelerator endpoint cho bucket us-east-1 → add làm origin cho CloudFront"** — sai vì AWS Global Accelerator được thiết kế để front **ứng dụng chạy trên compute** (ALB, NLB, EC2 Elastic IP), **không hỗ trợ Amazon S3 làm endpoint**. Không thể tạo Global Accelerator endpoint trỏ thẳng vào một bucket S3. Kể cả giả sử làm được, GA chỉ tối ưu **đường đi mạng** (dùng AWS global network để route nhanh hơn) — nó không giải quyết việc dữ liệu vẫn nằm ở EU, không thay thế cho việc replicate dữ liệu.

#### Vì sao C sai — S3 Transfer Acceleration không di chuyển dữ liệu

**C: Lambda@Edge trỏ request NA sang S3 Transfer Acceleration endpoint của bucket us-east-1"** — nghe rất hợp lý vì tên gọi "Transfer Acceleration" dễ khiến nghĩ nó "tăng tốc" truy cập. Nhưng bản chất S3TA chỉ tối ưu **đường truyền TCP qua mạng edge của CloudFront/AWS backbone** giữa client và **một bucket cố định** — nó **không thay đổi vị trí địa lý của dữ liệu**. Trong câu này bucket đích của C vẫn ngầm hiểu là bucket EU gốc (vì C không nói gì về việc tạo/replicate bucket us-east-1 có dữ liệu) — nên user NA vẫn kéo dữ liệu xuyên lục địa, chỉ là đường truyền có tối ưu hơn một chút. Vẫn chậm hơn nhiều so với việc dữ liệu đã nằm sẵn ở us-east-1.

| Lựa chọn | Cơ chế thật | Có di chuyển dữ liệu không? | Kết quả |
|---|---|---|---|
| **A + D (đúng)** | CRR nhân bản data + Lambda@Edge đổi origin | **Có** | Dữ liệu nằm ngay tại us-east-1 → nhanh nhất |
| B | Global Accelerator "front" S3 | Không hỗ trợ S3 | Không khả thi |
| C | S3TA tăng tốc đường truyền tới bucket cũ | **Không** | Vẫn kéo dữ liệu từ xa, chỉ nhanh hơn chút |
| E | Global Accelerator cho bucket EU + endpoint group | Không hỗ trợ S3 | Không khả thi |

#### Lưu ý thực tế

- Global Accelerator hỗ trợ: Application Load Balancer, Network Load Balancer, EC2 instance (qua Elastic IP). **Không hỗ trợ S3, không hỗ trợ Lambda trực tiếp.**
- S3 Transfer Acceleration dùng khi: client ở xa upload/download lên **một bucket duy nhất, không có bản sao khác** — tối ưu đường truyền qua edge location gần client, sau đó đi qua AWS backbone tới bucket. Không thay thế cho CRR khi cần bản sao gần user để phục vụ đọc lặp lại nhiều lần (weather maps update mỗi giờ, đọc liên tục → CRR hợp lý hơn nhiều).

#### Quy tắc nhớ cho thi

- **"Global Accelerator + S3"** → luôn sai, GA không front S3 (chỉ ALB/NLB/EC2 EIP).
- **"S3 Transfer Acceleration = tăng tốc transfer đường truyền"**, KHÔNG PHẢI "đưa dữ liệu đến gần user hơn" — phân biệt rõ hai khái niệm.
- **"Users ở xa origin, cần LEAST latency, đọc lặp lại nhiều"** → nghĩ ngay đến **replicate dữ liệu gần user** (S3 CRR) + **route request đến bản gần** (Lambda@Edge / Route 53 latency routing / CloudFront origin group).
- Thấy đề có chữ "Transfer Acceleration" xuất hiện như một "trick answer" gần giống đáp án đúng → cảnh giác, đọc kỹ xem có thực sự tạo bản sao dữ liệu hay không.

### TD explanation

Lambda@Edge is a feature of Amazon CloudFront that lets you run code closer to your application’s users, improving performance and reducing latency. With Lambda@Edge, you don’t have to provision or manage infrastructure in multiple locations around the world. You pay only for the compute time you consume—there is no charge when your code is not running.

One of the use cases for Lambda@Edge is for intelligent request routing. This capability allows developers to customize how requests are handled at AWS network edge locations, making it possible to dynamically alter the flow of traffic based on various criteria, such as the geographic location of the requester, device type, or request headers. By processing these requests closer to the user, Lambda@Edge enables the implementation of optimizations like content localization, A/B testing, and adaptive responses based on user-agent.

Amazon S3 Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. Buckets that are configured for object replication can be owned by the same AWS account or by different accounts. Objects may be replicated to a single destination bucket or multiple destination buckets. Destination buckets can be in different AWS Regions or within the same Region as the source bucket.

S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different AWS Regions. CRR can help you do the following:

– Meet compliance requirements — Although Amazon S3 stores your data across multiple geographically distant Availability Zones by default, compliance requirements might dictate that you store data at even greater distances.

– Minimize latency — If your customers are in two geographic locations, you can minimize latency in accessing objects by maintaining object copies in AWS Regions that are geographically closer to your users.

– Increase operational efficiency — If you have compute clusters in two different AWS Regions that analyze the same set of objects, you might choose to maintain object copies in those Regions.

In the scenario, by setting up Cross-Region Replication (CRR), you replicate the weather map data to a bucket in us-east-1, bringing it geographically closer to North American users. Then, you can configure a Lambda@Edge function to reroute requests from North American users to the us-east-1 bucket. Together, this solution significantly reduces latency, as the data being accessed is much closer to the users, ensuring an improved user experience.

Hence, the correct answers are:

– Create a Lambda@Edge that modifies requests from North American users to retrieve files from a new us-east-1 S3 bucket. By having the data replicated in a geographically closer region (us-east-1), the data retrieval time is significantly decreased for users in that region.

– Configure S3 cross-region replication from the eu-east-1 bucket to a new bucket in the us-east-1 region. This approach dynamically routes requests based on the user’s geographic location. By using the S3 Transfer Acceleration endpoint, which is designed to speed up the transfer of files over long distances between the client and the S3 bucket, North American users can experience faster access to the weather maps.

The option that says: Create a new AWS Global Accelerator endpoint for the us-east-1 bucket and add it as an origin for the CloudFront distribution. Use Lambda@Edge to modify North American requests to use this new origin is incorrect. While AWS Global Accelerator can improve performance for some use cases, it typically front-ends applications or load balancers. Simply creating a Global Accelerator endpoint for a new S3 bucket does not address the crucial need to replicate or store the updated objects in a bucket closer to the users.

The option that says: Create a new Global Accelerator endpoint for the eu-west-1 S3 bucket. Configure additional endpoint groups in the us-east-1 S3 bucket for TCP port 443 is incorrect because it references a different region (eu-west-1) instead of the specified eu-east-1 origin, and configuring additional endpoint groups for a bucket alone does not resolve the fundamental latency issue.

The option that says: Create a Lambda@Edge function that modifies requests from North American users to use the S3 Transfer Acceleration endpoint of the S3 bucket in the us-east-1 region is incorrect. While S3 Transfer Acceleration (S3TA) can typically optimize the transfer of data to and from S3 buckets, especially over long distances, it does not change the geographic location of the data. With this approach, you are still essentially retrieving files from a distant bucket. Consequently, the latency experienced will likely be higher compared to retrieving data from a source that is geographically closer to you.

 

References:

https://aws.amazon.com/blogs/networking-and-content-delivery/dynamically-route-viewer-requests-to-any-origin-using-lambdaedge/

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html

 

Check out these Amazon S3 and Amazon CloudFront Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q22"></a>

## Q22

An aerospace company launched hundreds of satellites into orbit. At regular intervals, the satellites send telemetry data to the earth base station which then uploads everything to an Amazon S3 bucket. Each satellite has a unique identification number that is used as a prefix for the data being received. For compliance purposes, another S3 bucket was created in a secondary region and S3 replication was configured to copy all data from the primary S3 bucket. One of the satellites was identified as a “master” satellite and its data must be completely replicated to the secondary bucket within 30 minutes of the initial upload to the primary S3 bucket.

Which of the following options is the recommended solution in order to meet the above requirements?

- **A.** Configure AWS DataSync agent on the earth base station to copy the data from the primary Amazon S3 bucket to the secondary S3 bucket. Choose “Use available” to allow DataSync to use all network bandwidth for copying data. Monitor the status of the task using Amazon EventBridge. Create a rule that will trigger an alert when the TRANSFERRING status exceeds 30 minutes.
- **B.** Create another Amazon S3 bucket to store the data from the “master” satellite. Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold.
- **C.** Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Select the S3 Replication Time Control option when setting the destination bucket. Monitor the maximum replication time to the secondary bucket by creating an Amazon EventBridge rule that will trigger an alert when the replication time exceeds the 30 min threshold.
- **D.** On the primary S3 bucket, enable Amazon S3 Transfer Acceleration. Configure the base station to filter the data based on the prefix of the “master” satellite and upload this data to the transfer acceleration endpoint. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** only 'master' satellite prefix; replicated within 30 min; monitor

🪤 **Your trap:** Transfer Acceleration ≠ replication speed (REPEAT)

🧠 **Rule:** Replication SLA → prefix-filtered replication rule + S3 Replication Time Control (15 min) + metrics.

### 🇻🇳 Phân tích chi tiết

> ⚠️ **Lỗi lặp lại:** Lại là "Transfer Acceleration ≠ tốc độ replication" — cùng gốc rễ nhầm lẫn như Q12 nhưng áp vào ngữ cảnh khác (SLA replication thay vì latency đọc). Cần khắc sâu: S3TA chỉ liên quan đến **upload/download**, không liên quan gì đến **S3 Replication**.

#### Tình huống

```
Earth base station → upload → Primary S3 bucket (prefix = satellite ID)
                                      │
                                      │ S3 Replication (đã bật cho toàn bucket)
                                      ▼
                              Secondary S3 bucket (compliance)

Yêu cầu riêng cho "master" satellite:
   → replicate HOÀN TẤT trong vòng 30 phút kể từ lúc upload
   → cần: lọc đúng prefix + đảm bảo SLA thời gian + giám sát
```

Đáp án đúng: **C**. Anh chọn **D** (S3 Transfer Acceleration).

#### Vì sao C đúng — cần đúng 3 thành phần

```
1) Replication rule filter theo prefix "master"
   → chỉ áp riêng SLA cho satellite này, không ảnh hưởng object khác
2) S3 Replication Time Control (S3 RTC)
   → SLA: 99.99% object replicate xong trong 15 phút
   → ĐÂY LÀ THỨ DUY NHẤT trong các lựa chọn có cam kết thời gian
3) EventBridge rule cảnh báo khi vượt 30 phút
   → giám sát, không tự nó tạo ra tốc độ
```

S3 RTC là tính năng **của S3 Replication**, đi kèm SLA rõ ràng và replication metrics qua CloudWatch. Không có RTC, S3 Replication vẫn chạy nhưng **không có cam kết thời gian** — đôi khi có thể mất vài giờ tùy tải hệ thống.

#### Vì sao D sai — Transfer Acceleration không liên quan đến Replication

**D: bật S3 Transfer Acceleration trên bucket primary, base station upload qua endpoint accelerate** — đây là nhầm lẫn kinh điển. S3TA chỉ tăng tốc **hành động upload/download giữa client và MỘT bucket**, dùng đường truyền qua CloudFront edge network để traffic vào AWS backbone nhanh hơn thay vì đi qua internet công cộng thông thường. Nó **không có bất kỳ liên hệ nào với cơ chế S3 Cross-Region Replication** — sau khi object đã nằm trong bucket primary (dù upload nhanh hay chậm nhờ S3TA), việc replicate nó sang bucket secondary là một quy trình hoàn toàn khác, chạy bất đồng bộ ở backend, và **không được S3TA tăng tốc**. Vì vậy D "involves unnecessary changes to the base station" và vẫn **không đảm bảo được SLA 30 phút** cho replication.

#### Vì sao A, B sai

- **A (DataSync):** copy toàn bộ dữ liệu không phân biệt, không có cách ưu tiên riêng cho "master" satellite → dữ liệu master có thể bị xếp hàng sau các object khác, không đảm bảo 30 phút.
- **B:** đúng ý tưởng lọc theo prefix, nhưng **thiếu S3 RTC** — không có SLA. Replication thường vẫn có thể xảy ra trong vài phút, nhưng "occasionally" có thể mất "a couple of hours" — không đủ tin cậy để cam kết 30 phút.

| Lựa chọn | Lọc theo prefix "master"? | Có SLA thời gian? | Đạt yêu cầu 30 phút? |
|---|---|---|---|
| **C (đúng)** | Có | Có (S3 RTC: 99.99% trong 15 phút) | Có |
| B | Có | Không | Không đảm bảo |
| A (DataSync) | Không | Không | Không đảm bảo |
| D (S3TA) | Có (chỉ ở bước upload) | Không (S3TA không tác động replication) | Không đảm bảo |

#### Quy tắc nhớ cho thi

- **"Replication phải hoàn tất trong X phút" / SLA thời gian cho replication** → chỉ có **S3 Replication Time Control (RTC)** đáp ứng (99.99% trong 15 phút).
- **S3 Transfer Acceleration** = tăng tốc **upload/download** giữa client và bucket. Không bao giờ là câu trả lời cho câu hỏi về **tốc độ replication**.
- **Chỉ replicate một phần dữ liệu (ví dụ theo satellite/tenant)** → dùng **replication rule với prefix filter**, không phải bucket riêng hay công cụ đồng bộ ngoài (DataSync) trừ khi đề yêu cầu khác.
- Thấy "monitor replication time" → nghĩ **S3 replication metrics + CloudWatch/EventBridge**, đi kèm RTC.

### TD explanation

S3 Replication Time Control (S3 RTC) helps you meet compliance or business requirements for data replication and provides visibility into Amazon S3 replication times. S3 RTC replicates most objects that you upload to Amazon S3 in seconds and 99.99 percent of those objects within 15 minutes.

With S3 RTC, you can monitor the total number and size of objects that are pending replication and the maximum replication time to the destination Region. Replication metrics are available through the AWS Management Console and Amazon CloudWatch, in which you can configure alerts. S3 RTC by default, includes S3 replication metrics and S3 event notifications, with which you can monitor the total number of S3 API operations that are pending replication, the total size of objects pending replication, and the maximum replication time. Replication metrics can be enabled independently of S3 RTC.

With S3 RTC, Amazon S3 events can notify you in the rare instance when objects do not replicate within 15 minutes and when those objects replicate successfully to their destination Region.

Therefore, the correct answer is: Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Select the S3 Replication Time Control option when setting the destination bucket. Monitor the maximum replication time to the secondary bucket by creating an Amazon EventBridge rule that will trigger an alert when the replication time exceeds the 30 min threshold. S3 RTC is backed by an SLA that ensures most objects uploaded in S3 are replicated within seconds, with 99.99 percent of those objects in within 15 minutes.

The option that says: Configure AWS DataSync agent on the earth base station to copy the data from the primary Amazon S3 bucket to the secondary S3 bucket. Choose “Use available” to allow DataSync to use all network bandwidth for copying data. Monitor the status of the task using Amazon EventBridge. Create a rule that will trigger an alert when the TRANSFERRING status exceeds 30 minutes is incorrect. This approach does not have a distinction for the “master” satellite’s data and just replicates everything. The replication for the “master” satellite’s data can be delayed if other objects are replicated first.

The option that says: Create another Amazon S3 bucket to store the data from the “master” satellite. Create a new S3 replication rule on the primary S3 bucket that will only copy data with the prefix of the “master” satellite. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold is incorrect. Without S3 RTC, you can’t guarantee the replication to be completed in 30 minutes because S3 replication can sometimes take a couple of hours.

The option that says: On the primary S3 bucket, enable Amazon S3 Transfer Acceleration. Configure the base station to filter the data based on the prefix of the “master” satellite and upload this data to the transfer acceleration endpoint. Monitor the maximum replication time to the secondary bucket with Amazon EventBridge. Create a rule that will trigger an alert when the replication time exceeds the 30 min threshold is incorrect. This may be possible, but it involves unnecessary changes to the base station configuration. Without S3 RTC, you can’t guarantee the replication to be completed in 30 minutes because S3 replication can sometimes take a couple of hours.

 

References:

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-time-control.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough-5.html

https://aws.amazon.com/s3/features/replication/

 

Check out these Amazon S3 and Amazon CloudWatch Cheat Sheets:

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-cloudwatch/

</details>

<a id="q23"></a>

## Q23

A global energy firm aggregates sensor readings from its offshore wind turbines and stores the data in an Amazon S3 data lake governed by AWS Lake Formation. The research department runs analytics on Amazon EC2 instances in two private subnets within a VPC. The EC2 instances already have an IAM role with permission to access the S3 bucket.

Corporate security mandates that only specific, approved networks be used when retrieving turbine data. The research team must be able to continue to access the data lake without exposing it to public internet traffic.

What combination of actions will meet these requirements? (Select THREE.)

- **A.** Configure a Gateway VPC endpoint for Amazon S3 within the research team's VPC.
- **B.** Update the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointArn matches the correct S3 access point.
- **C.** Create a NAT Gateway and modify the VPC’s route table to direct traffic from the private subnets to the NAT Gateway.
- **D.** Modify the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointAccount matches the research team’s AWS account.
- **E.** Encrypt the data lake objects using AWS Key Management Service (AWS KMS) and reassign the key to the research team's IAM role
- **F.** Set up an S3 access point in the research team's AWS account and reference its Amazon Resource Name (ARN) when retrieving objects.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B, F · **You picked:** A, B, C

🔑 **Key words:** Lake Formation data lake; only approved networks; no public internet

🪤 **Your trap:** NAT Gateway = internet path (REPEAT)

🧠 **Rule:** Private + network-restricted S3 → Gateway endpoint + S3 access point + bucket policy s3:DataAccessPointArn.

### 🇻🇳 Phân tích chi tiết

> ⚠️ **Lỗi lặp lại:** Vẫn là "NAT Gateway = đường ra internet" — Anh chọn NAT Gateway trong khi đề rõ ràng cấm public internet traffic. Đây là lỗi đã gặp ở các bài trước về network isolation cho S3. Cần khắc sâu: **NAT Gateway KHÔNG BAO GIỜ là câu trả lời khi đề cấm internet**, vì bản chất NAT Gateway luôn cần Internet Gateway ở đầu kia.

#### Tình huống

```
VPC (research team)
┌───────────────────────────────────────────┐
│  Private subnet A       Private subnet B   │
│  ┌────────────┐         ┌────────────┐     │
│  │ EC2 (IAM    │         │ EC2 (IAM    │     │
│  │  role OK)   │         │  role OK)   │     │
│  └─────┬──────┘         └─────┬──────┘     │
│        │                       │            │
│        └───────────┬───────────┘            │
└────────────────────┼─────────────────────────┘
                      │  chỉ được đi qua network ĐÃ DUYỆT
                      │  KHÔNG được ra public internet
                      ▼
        S3 Data Lake (Lake Formation quản lý)

Yêu cầu: chỉ mạng approved mới truy cập được S3, vẫn không public internet
Chọn BA hành động
```

Đáp án đúng: **A, B, F**. Anh chọn **A, B, C** — sai ở C (NAT Gateway).

#### Vì sao A, F, B đúng — 3 lớp phòng thủ bổ trợ nhau

```
A) Gateway VPC Endpoint cho S3
   → traffic từ EC2 trong private subnet đến S3
   → đi qua AWS network nội bộ (prefix list trong route table)
   → KHÔNG đi qua internet, không cần NAT/IGW

F) S3 Access Point riêng cho research team
   → endpoint riêng, có policy riêng, gắn "network origin control"
   → giới hạn access point này chỉ dùng được từ VPC cụ thể (VPC restriction)

B) Bucket policy điều kiện s3:DataAccessPointArn
   → buộc mọi request GetObject phải đi qua ĐÚNG access point (ARN cụ thể)
   → chặn truy cập trực tiếp vào bucket, bỏ qua access point
```

Ba thứ này khớp với nhau: Gateway endpoint đảm bảo đường đi private; Access Point tạo ra một "cổng" có thể giới hạn theo VPC; Bucket policy bắt buộc truy cập phải qua đúng cổng đó — tạo thành network + identity control hoàn chỉnh mà Lake Formation data lake cần.

#### Vì sao C (NAT Gateway) sai — bản chất là lối ra internet

**C: tạo NAT Gateway, sửa route table trỏ traffic từ private subnet qua NAT Gateway** — sai trực tiếp với yêu cầu. NAT Gateway tồn tại để cho instance trong private subnet **khởi tạo kết nối ra internet** (qua Internet Gateway ở tầng VPC), đồng thời chặn chiều ngược lại (internet không tự kết nối vào được). Nhưng bản chất route traffic của NAT Gateway **vẫn đi qua Internet Gateway ra ngoài internet công cộng** trước khi đến S3 (trừ khi dùng VPC endpoint) — hoàn toàn trái với yêu cầu "không được đi qua public internet traffic". Đây chính là bẫy: nhiều người nghĩ "cần NAT Gateway để EC2 trong private subnet gọi ra được S3", nhưng thực chất **Gateway VPC Endpoint mới là cách đúng để truy cập S3 riêng tư mà không cần NAT/IGW.**

#### Vì sao D, E sai

- **D (s3:DataAccessPointAccount):** chỉ giới hạn theo **account** sở hữu access point, không giới hạn theo **network/VPC cụ thể** — bất kỳ resource nào trong account đó (kể cả VPC khác) có quyền IAM đều dùng được access point, không đạt yêu cầu "chỉ mạng đã duyệt".
- **E (KMS encryption):** cải thiện bảo mật dữ liệu khi lưu trữ (data at rest), nhưng **không kiểm soát đường mạng truy cập** — không giải quyết yêu cầu chính của đề là giới hạn network.

| Lựa chọn | Chặn được public internet? | Giới hạn theo network cụ thể? |
|---|---|---|
| **A. Gateway VPC Endpoint (đúng)** | Có | Có (route qua AWS network nội bộ) |
| **F. S3 Access Point (đúng)** | — | Có (VPC restriction trên access point) |
| **B. Bucket policy DataAccessPointArn (đúng)** | — | Có (buộc đi qua đúng access point) |
| C. NAT Gateway | **Không** — vẫn qua Internet Gateway | Không |
| D. DataAccessPointAccount | Không tự nó | Chỉ theo account, không theo VPC |
| E. KMS encryption | Không | Không (không kiểm soát network) |

#### Lưu ý thực tế

- Gateway VPC Endpoint chỉ hỗ trợ S3 và DynamoDB; các service khác cần Interface Endpoint (PrivateLink, dùng ENI, có phí theo giờ + theo GB).
- S3 Access Point + VPC restriction là cách chuẩn để tạo "private front door" cho bucket dùng chung nhiều team/nhiều VPC mà không phải chỉnh sửa bucket policy gốc liên tục.

#### Quy tắc nhớ cho thi

- **"Không được đi qua public internet" + cần gọi ra ngoài VPC** → NAT Gateway **luôn sai**; nghĩ ngay **VPC Endpoint** (Gateway cho S3/DynamoDB, Interface/PrivateLink cho service khác).
- **"Chỉ approved network mới truy cập S3 dùng chung"** → **S3 Access Point** + bucket policy check `s3:DataAccessPointArn`.
- **`s3:DataAccessPointAccount`** chỉ giới hạn theo account, không đủ chặt khi đề yêu cầu giới hạn theo **VPC/network cụ thể**.
- Mã hóa (KMS) là kiểm soát **data at rest**, không thay thế được kiểm soát **network access**.

### TD explanation

S3 Access Points are unique network endpoints for Amazon S3 buckets that make data access management easier for shared datasets. Each access point is linked to a single S3 bucket and has its own access policy. This allows you to create custom access policies tailored to different applications or user groups that access the same bucket. Access points also include network origin control and Block Public Access settings, making them beneficial for managing access in complex scenarios, such as multi-tenant applications or data lakes.

Gateway VPC Endpoints are specifically designed for Amazon S3 and DynamoDB. They enable resources within a Virtual Private Cloud (VPC) to communicate with S3 or DynamoDB without going through the public internet. Gateway endpoints use prefix lists in the VPC route table to direct traffic to the target service. This setup provides a secure and cost-effective way to access S3 or DynamoDB from within a VPC. Unlike interface endpoints, gateway endpoints do not require elastic network interfaces and do not utilize AWS PrivateLink technology.

Combining S3 Access Points with Gateway VPC Endpoints enhances security and simplifies access management for applications using shared datasets in Amazon S3.

Creating a Gateway VPC endpoint for Amazon S3 within the research team’s VPC ensures that all traffic between the EC2 instances and the S3 data lake remains private and does not traverse the public internet. Setting up an S3 access point simplifies access management and enforces restrictions by allowing policies tied to VPCs, ensuring only approved networks can retrieve the data. Additionally, updating the S3 bucket policy to validate the s3:DataAccessPointArn ensures data access is explicitly routed through the approved access point. Together, these measures fulfill the requirements for secure, restricted, and private access to the S3 data lake while maintaining compliance with corporate policies.

Therefore, the correct answers are:

– Configure a Gateway VPC endpoint for Amazon S3 within the research team’s VPC.

– Set up an S3 access point in the research team’s AWS account and reference its Amazon Resource Name (ARN) when retrieving objects.

– Update the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointArn matches the correct S3 access point.

The option that says: Modify the S3 bucket policy to include a condition that allows s3:GetObject only if the s3:DataAccessPointAccount matches the research team’s AWS account is incorrect. Using the condition s3:DataAccessPointAccount allows access based on the AWS account associated with the S3 access point. While this limits access to resources within the specified account, it does not enforce fine-grained control. This means that resources in other VPCs within the account could potentially use the access point to retrieve data, provided they have permissions.

The option that says: Encrypt the data lake objects using AWS Key Management Service (AWS KMS) and reassign the key to the research team’s IAM role is incorrect. While encryption improves security, it does not directly address the requirement to restrict network access to the data lake. The research team’s IAM role already has permissions to access the bucket, so this step is unnecessary.

The option that says: Create a NAT Gateway and modify the VPC’s route table to direct traffic from the private subnets to the NAT Gateway is incorrect because. A NAT Gateway would allow resources in the private subnets to access the internet, contradicting the requirements. Using a Gateway VPC endpoint would solve this problem as it provides a private connection between the VPC and Amazon S3.

 

References:

https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html

 

Check out these Amazon VPC and Amazon S3 Cheat Sheets:

https://tutorialsdojo.com/amazon-vpc/

</details>

<a id="q69"></a>

## Q69

An e-commerce company operates its core infrastructure within a private data center. This infrastructure is linked to AWS through a combination of AWS Direct Connect and a secure IPSec VPN, ensuring that sensitive customer data remains off the public internet. As part of its strategic growth, the company aims to extend its proprietary services to other e-commerce businesses hosted on AWS.

Which networking solution aligns with the company’s requirements?

- **A.** Establish a VPC Endpoint Service for the company’s applications and associate it with a Network Load Balancer that manages TCP traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect.
- **B.** Set up a NAT Gateway in a VPC for the company’s applications and secure it with network access control and security group rules.
- **C.** Set up a VPC Endpoint Service for the company’s applications and link it with an Application Load Balancer that handles HTTP or HTTPS traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect.
- **D.** Use AWS Direct Connect to link the company’s data center to a VPC in AWS. Within the VPC, set up security group rules to manage access to the company’s applications.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** expose services to other AWS customers; stay off internet

🪤 **Your trap:** ALB cannot back a VPC endpoint service

🧠 **Rule:** PrivateLink endpoint service → Network Load Balancer (or GWLB), never ALB.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Company data center                    AWS
┌──────────────────┐   Direct Connect  ┌────────────────────────┐
│  Core systems      │ + IPSec VPN     │  VPC Endpoint Service    │
│  (dữ liệu nhạy cảm)│◄───────────────►│  (expose ứng dụng ra    │
└──────────────────┘   (off public net)│   các AWS customer khác)│
                                        └────────────────────────┘
Mục tiêu: mở rộng dịch vụ cho các e-commerce khác trên AWS
          KHÔNG đi qua public internet
```

Đáp án đúng: **A** (VPC Endpoint Service + **Network Load Balancer**). Anh chọn **C** (VPC Endpoint Service + **Application Load Balancer**) — sai duy nhất ở loại load balancer.

#### Vì sao A đúng, C sai — PrivateLink chỉ chấp nhận NLB (hoặc GWLB)

Đây là một giới hạn kỹ thuật cứng của AWS PrivateLink: khi tạo **VPC Endpoint Service** để expose ứng dụng cho account khác qua Interface Endpoint, service đứng sau **bắt buộc phải là Network Load Balancer** (hoặc Gateway Load Balancer cho use case appliance) — **không hỗ trợ Application Load Balancer**.

```
VPC Endpoint Service ──── chỉ chấp nhận ────► Network Load Balancer (Layer 4, TCP)
                     ──── chỉ chấp nhận ────► Gateway Load Balancer (appliance)
                     ──── KHÔNG chấp nhận ──► Application Load Balancer (Layer 7)
```

Lý do kỹ thuật: PrivateLink hoạt động ở tầng network (TCP), NLB có Elastic Network Interface cố định với IP tĩnh cho mỗi AZ — phù hợp để làm target ổn định cho endpoint service. ALB không có cấu trúc ENI/IP cố định tương thích với cơ chế này. Vì vậy phương án C — dù đúng về ý tưởng dùng VPC Endpoint Service và Direct Connect — **sai hoàn toàn vì chọn nhầm loại load balancer**, khiến giải pháp không triển khai được trên thực tế.

Phương án A giữ nguyên toàn bộ logic đúng: VPC Endpoint Service (để account khác kết nối riêng tư vào ứng dụng qua Interface Endpoint) + Network Load Balancer (loại LB duy nhất PrivateLink hỗ trợ) + Direct Connect (giữ kết nối riêng tư giữa data center và AWS).

#### Vì sao B, D sai

- **B (NAT Gateway):** NAT Gateway cho phép instance trong private subnet **chủ động ra ngoài** (internet hoặc service khác), không có cơ chế nào để account khác **kết nối vào** ứng dụng của công ty. Không giải quyết yêu cầu "expose service cho AWS customer khác".
- **D (chỉ Direct Connect + security group):** chỉ giải quyết kết nối riêng tư data center ↔ AWS, nhưng **không có cơ chế nào để các AWS customer khác (ngoài công ty) kết nối vào** ứng dụng — thiếu hẳn phần "mở rộng dịch vụ ra ngoài" là yêu cầu chính của đề.

| Lựa chọn | VPC Endpoint Service? | Loại LB | Cho phép customer khác kết nối vào? |
|---|---|---|---|
| **A (đúng)** | Có | **NLB** | Có |
| C | Có | ALB (không hỗ trợ) | Không triển khai được |
| B | Không | — | Không |
| D | Không | — | Không |

#### Lưu ý thực tế

- Nếu ứng dụng gốc chạy sau ALB (HTTP/HTTPS), muốn expose qua PrivateLink thì cần đặt **NLB phía trước ALB** (NLB → ALB → ứng dụng) — một pattern rất phổ biến trong thực tế và hay bị hỏi dưới dạng biến thể của câu này.
- Gateway Load Balancer cũng được PrivateLink hỗ trợ, nhưng dùng cho kiến trúc chèn network appliance (firewall, IDS/IPS) chứ không phải cho việc expose ứng dụng business thông thường.

#### Quy tắc nhớ cho thi

- **"VPC Endpoint Service" / "expose ứng dụng cho account khác qua PrivateLink"** → luôn đi kèm **Network Load Balancer** (hoặc Gateway Load Balancer). **Application Load Balancer không bao giờ đúng ở vị trí này.**
- Nếu ứng dụng vốn dùng ALB mà cần PrivateLink → thêm NLB đứng trước ALB, chứ không thay ALB.
- **"NAT Gateway"** → chỉ giải quyết outbound, không bao giờ là câu trả lời cho yêu cầu "cho bên ngoài kết nối vào".

### TD explanation

A VPC Endpoint Service allows the company’s applications to be accessed securely within the AWS network. This is a crucial component in the solution as it enables the company’s services to be exposed to other businesses on AWS without exposing the data to the public internet. This is particularly important given the sensitive nature of the data handled by the company.

The Network Load Balancer operates at the fourth layer of the Open Systems Interconnection (OSI) model and can handle millions of requests per second. By efficiently managing TCP traffic, the Network Load Balancer ensures high availability and fault tolerance of the applications. This is critical for maintaining a high-quality user experience, especially as the company expands its services to other businesses on AWS.

AWS Direct Connect provides a dedicated, private link from the company’s data center to AWS. This ensures secure and efficient data transfer, which is vital for the company given the sensitive nature of its data. By maintaining a secure connection between the company’s data center and AWS using Direct Connect, the company can ensure that its sensitive data remains secure while still being able to extend its services to other businesses on AWS.

Hence, the correct answer is: Establish a VPC Endpoint Service for the company’s applications and associate it with a Network Load Balancer that manages TCP traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect.

The option that says: Set up a VPC Endpoint Service for the company’s applications and link it with an Application Load Balancer that handles HTTP or HTTPS traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect is incorrect because the Application Load Balancer cannot be used to create a VPC Endpoint Service. VPC Endpoint Services require Network Load Balancers.

The option that says: Use AWS Direct Connect to link the company’s data center to a VPC in AWS. Within the VPC, set up security group rules to manage access to the company’s applications is incorrect because it does not provide a way for the company to extend its services to other businesses on AWS. While AWS Direct Connect and security group rules provide secure connectivity and access control, they do not enable the company to expose its applications as services that other AWS users can consume.

The option that says: Set up a NAT Gateway in a VPC for the company’s applications and secure it with network access control and security group rules is incorrect because a NAT Gateway is used to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances. However, the question specifies that the company’s data cannot traverse the public internet. While network access control and security group rules add a layer of security, they do not provide the necessary private connectivity for the company’s sensitive data.

 

References:

https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.htmhttps://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html
https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

 

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/aws-direct-connect/
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

</details>

<a id="q21"></a>

## Q21

A media organization operates a content delivery system that experiences peak loads whenever new content is released. The release dates and times for the content are pre-set and automatically triggered. The system is hosted on an Amazon ECS (Elastic Container Service) cluster, consisting of Amazon EC2 On-Demand Instances within an ASG (Auto Scaling Group) that uses a predictive scaling policy. The Amazon ECS cluster frequently retrieves data from an Amazon S3 bucket located in the same AWS Region. All traffic routes through a NAT gateway.

The organization aims to reduce platform costs, all while ensuring that availability is not compromised.

What combination of steps can be taken to achieve this goal? (Select TWO.)

- **A.** Enable S3 Intelligent-Tiering to move objects to cheaper storage tiers automatically.
- **B.** Replace the NAT gateway with a NAT instance hosted on an Amazon EC2 On-Demand Capacity Reservation.
- **C.** Switch from the predictive scaling policy to a scheduled scaling policy.
- **D.** Create a new ECS capacity provider using an Auto Scaling Group of Spot Instances, and adjust the strategy to distribute weight evenly.
- **E.** Replace the NAT gateway with a Gateway VPC Endpoint for Amazon S3.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E · **You picked:** A, E

🔑 **Key words:** release times pre-set; ECS on EC2; S3 in same Region via NAT; reduce cost

🪤 **Your trap:** Intelligent-Tiering doesn't address NAT/scaling cost

🧠 **Rule:** Known schedule → scheduled scaling; S3 via NAT → free Gateway VPC endpoint.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Content release: lịch biết trước, cố định (pre-set dates/times)
        │
        ▼
Amazon ECS cluster (EC2 On-Demand, trong ASG)
   scaling policy hiện tại: PREDICTIVE SCALING (dùng ML để dự báo)
        │
        ▼
Amazon S3 (cùng Region) ◄──── qua NAT Gateway ────

Mục tiêu: giảm chi phí, KHÔNG được ảnh hưởng availability
Chọn HAI hành động
```

Đáp án đúng: **C (scheduled scaling) + E (Gateway VPC Endpoint)**. Anh chọn **A, E** — đúng E, sai A (chọn nhầm S3 Intelligent-Tiering thay vì đổi scaling policy).

#### Vì sao C đúng — biết lịch trước thì không cần ML dự báo

```
Predictive Scaling: dùng machine learning để DỰ ĐOÁN traffic tương lai
                     → hữu ích khi traffic có pattern nhưng KHÔNG biết chính xác thời điểm
                     → có overhead/chi phí vận hành ML cao hơn

Scheduled Scaling:   scale đúng vào thời điểm ĐÃ BIẾT TRƯỚC
                     → đơn giản, rẻ hơn, chính xác tuyệt đối vì thời điểm đã cố định
```

Đề nói rõ: "release dates and times... are pre-set and automatically triggered" — tức công ty **đã biết chính xác** khi nào traffic tăng. Dùng predictive scaling (ML dự báo) trong trường hợp này là **overkill và tốn kém không cần thiết** — không tận dụng được lợi thế đã biết trước lịch. Scheduled scaling cho kết quả chính xác hơn (vì không cần "đoán") và rẻ hơn.

#### Vì sao E đúng — Gateway VPC Endpoint miễn phí, thay NAT Gateway tốn phí

Traffic từ ECS cluster đến S3 (cùng Region) hiện phải đi qua **NAT Gateway**, tốn phí theo giờ + theo GB xử lý. Vì S3 và DynamoDB có **Gateway VPC Endpoint miễn phí**, thay NAT Gateway bằng Gateway VPC Endpoint cho S3 sẽ loại bỏ hoàn toàn chi phí data processing qua NAT cho luồng traffic này, mà vẫn giữ nguyên tính riêng tư và availability (Gateway Endpoint không phải điểm lỗi đơn — nó gắn vào route table, có tính sẵn sàng cao theo AWS quản lý).

#### Vì sao A sai — Anh chọn nhầm

**A: bật S3 Intelligent-Tiering** — đây là tối ưu **chi phí lưu trữ (storage cost)** của các object trong bucket, hoàn toàn không liên quan đến hai nguồn chi phí chính trong bài: (1) phí **NAT Gateway** cho traffic ECS↔S3, và (2) chi phí vận hành **predictive scaling**. TD explanation nói rõ: "it does not address the NAT Gateway charges or the immediate scaling needs." Đây là một "đáp án đúng về mặt kỹ thuật nhưng lạc đề" — Intelligent-Tiering không sai bản chất, chỉ là **không giải quyết cost driver chính** mà đề đang nhắm tới.

#### Vì sao B, D sai

- **B (NAT instance trên On-Demand Capacity Reservation):** rẻ hơn NAT Gateway nhưng là **single point of failure**, cần tự vận hành/patch → tăng rủi ro availability, lại đắt hơn Gateway VPC Endpoint (miễn phí) rất nhiều.
- **D (ECS capacity provider dùng Spot Instances, chia đều weight):** Spot rẻ nhưng có rủi ro bị **reclaim/interrupt** bất cứ lúc nào — đề yêu cầu rõ "availability is not compromised", nên Spot không phù hợp trừ khi có chiến lược fallback mạnh (đề không đề cập).

| Lựa chọn | Giải quyết đúng cost driver nào? | Ảnh hưởng availability? |
|---|---|---|
| **C. Scheduled scaling (đúng)** | Chi phí vận hành predictive scaling không cần thiết | Không — vẫn scale đúng lúc vì lịch biết trước |
| **E. Gateway VPC Endpoint (đúng)** | Phí NAT Gateway cho traffic S3 | Không — miễn phí, có sẵn tính sẵn sàng |
| A. S3 Intelligent-Tiering | Chi phí lưu trữ S3 (không phải cost driver chính) | Không ảnh hưởng nhưng lạc đề |
| B. NAT instance | Rẻ hơn NAT Gateway nhưng vẫn tốn phí | Có rủi ro — SPOF |
| D. Spot capacity provider | Compute cost | Có rủi ro — bị interrupt |

#### Quy tắc nhớ cho thi

- **"Biết trước chính xác thời điểm traffic tăng"** → **Scheduled Scaling**, không phải Predictive Scaling (predictive dùng khi biết pattern nhưng không biết chính xác thời điểm).
- **"Traffic đến S3/DynamoDB qua NAT Gateway, cùng Region, muốn giảm cost"** → **Gateway VPC Endpoint** (miễn phí) luôn là lựa chọn tốt hơn NAT Gateway/NAT instance.
- **"Giảm cost nhưng không được ảnh hưởng availability"** → loại ngay Spot Instances (trừ khi có robust fallback) và NAT instance tự quản lý (SPOF).
- S3 Intelligent-Tiering chỉ tối ưu **storage cost**, không liên quan gì đến network/NAT hay scaling cost — cẩn thận với các đáp án "đúng nhưng lạc đề".

### TD explanation

Amazon EC2 Auto Scaling provides several methods to scale your Auto Scaling group. Here are the main ways you can scale your Auto Scaling group:

Manual Scaling: You can manually adjust the desired capacity of your Auto Scaling group. This method is useful when you need to make immediate changes to your group’s capacity.
Scheduled Scaling: This method allows you to set up scheduled actions to scale your group at specific times. It’s ideal for predictable load changes that occur at fixed times.
Dynamic Scaling: This approach automatically adjusts capacity in response to changing demand. There are three types of dynamic scaling policies: a. Target Tracking Scaling: Adjusts capacity to maintain a specific metric at a target value. b. Step Scaling: Uses step adjustments to scale based on the size of the alarm breach. c. Simple Scaling: Adjusts capacity based on a single scaling adjustment.
Predictive Scaling: This method uses machine learning to forecast future traffic and automatically provisions the right number of EC2 instances in advance. It’s useful for handling cyclical traffic patterns.

In this case, the organization is aware of the specific dates and times for content releases, enabling them to predict peak loads accurately. Currently, the Auto Scaling Group (ASG) employs a predictive scaling policy, which uses machine learning to anticipate traffic patterns. While this approach is effective, it can be more expensive compared to scheduled scaling, especially when the timing of peak loads is known. Transitioning to a scheduled scaling policy would allow the organization to scale resources precisely when needed, thereby reducing unnecessary scaling and costs.

Gateway VPC Endpoints are specifically designed for Amazon S3 and DynamoDB. They enable resources within a Virtual Private Cloud (VPC) to communicate with S3 or DynamoDB without going through the public internet. Gateway endpoints use prefix lists in the VPC route table to direct traffic to the target service. This setup provides a secure and cost-effective way to access S3 or DynamoDB from within a VPC.

The media organization frequently retrieves data from an Amazon S3 bucket. Their current setup involves a NAT gateway, which can lead to significant data transfer costs. By replacing the NAT gateway with a Gateway VPC Endpoint for Amazon S3, the organization can keep data traffic within the AWS network, thereby reducing data transfer costs and improving performance. This change maintains availability while aligning with the goal of cost reduction.

Hence, the correct answers are:

– Replace the NAT gateway with a Gateway VPC Endpoint for Amazon S3.

– Switch from the predictive scaling policy to a scheduled scaling policy.

The option that says: Replace the NAT gateway with a NAT instance hosted on an Amazon EC2 On-Demand Capacity Reservation is incorrect. While NAT instances may be less expensive than NAT gateways, they can also pose a single point of failure. Moreover, managing and patching a NAT instance typically involves extra operational overhead, which can lead to potential availability risks. Also, since Gateway VPC Endpoint is free, it’s a much cheaper alternative to using a NAT instance or NAT gateway.

The option that says: Create a new ECS capacity provider using an Auto Scaling Group of Spot Instances, and adjust the strategy to distribute weight evenly is incorrect. While spot instances can significantly reduce costs, there is a risk of interruption. If capacity is reclaimed, availability can suffer unless a robust fallback plan exists. The question’s scenario explicitly states that the organization wants to maintain availability without interruption.

The option that says: Enable S3 Intelligent-Tiering to move objects to cheaper storage tiers automatically is incorrect. Although S3 Intelligent-Tiering can primarily reduce S3 storage costs, it does not address the NAT Gateway charges or the immediate scaling needs. The main cost driver in the scenario is traffic going through the NAT gateway and the ECS cluster’s scaling strategy.

 

References:

https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-create-scheduled-action.html

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-vpc/

https://tutorialsdojo.com/amazon-s3/

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

</details>

<a id="q15"></a>

## Q15

An e-commerce platform experiences significant traffic spikes during peak shopping seasons, leading to performance bottlenecks and impacting user experience. The application is hosted on Amazon ECS and uses Amazon CloudFront as its CDN. The platform has two main modules: product browsing and checkout, with the browsing module experiencing substantially higher loads. Sessions are managed using JSON Web Tokens (JWT), which encodes user roles and access levels. This load imbalance causes performance issues, affecting overall availability.
A Solutions Architect needs to enhance scalability and reliability for both modules during high-traffic periods to maintain optimal performance and cost efficiency.

Which solution will most effectively address this challenge?

- **A.** Implement API Gateway in front of ECS services, using AWS Lambda authorizer to authenticate users based on JWT. Utilize API Gateway's caching and traffic management capabilities, directing requests based on JWT attributes to the correct module.
- **B.** Refactor the application to use AWS Lambda for both modules, with API Gateway routing requests based on JWT. Use CloudFront for static content delivery and JWT validation.
- **C.** Create separate ECS services for browsing and checkout modules, each with its own auto-scaling configuration. Use CloudFront Functions to inspect JWT, route requests to the appropriate ECS service based on the requested module, user access level, and load.
- **D.** Transition the platform to Amazon Elastic Kubernetes Service, separating the product browsing and checkout functionalities into distinct Kubernetes pods. Implement ECS Service Connect to orchestrate service communication within the cluster, enabling mutual TLS (mTLS) to secure pod-to-pod interactions. Configure the Service Connect virtual service to utilize JWT for authenticating requests, directing them from the browsing pod to the checkout pod based on user permissions and session data encoded in the JWT.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** browsing vs checkout load imbalance; JWT; CloudFront already in front

🪤 **Your trap:** API Gateway + Lambda authorizer adds latency/complexity

🧠 **Rule:** Independent scaling → separate ECS services; lightweight edge routing on JWT → CloudFront Functions.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
E-commerce platform (Amazon ECS, sau CloudFront)
┌───────────────────────────────────────────────┐
│  Module: BROWSING (load cao, biến động mạnh)    │
│  Module: CHECKOUT  (load thấp hơn, ổn định)     │
└───────────────────────────────────────────────┘
Session: JWT (chứa user role, access level)

Yêu cầu: mỗi module scale ĐỘC LẬP theo tải riêng
         routing dựa trên JWT phải NHẸ, không thêm latency/complexity thừa
```

Đáp án đúng: **C** (tách 2 ECS service + CloudFront Functions đọc JWT để route). Anh chọn **A** (API Gateway + Lambda authorizer) — sai vì thêm một tầng nặng không cần thiết.

#### Vì sao C đúng — tách service để scale độc lập, dùng công cụ edge nhẹ nhất phù hợp

```
Bước 1 — Tách hạ tầng:
   ECS service "browsing"  (auto-scaling riêng, tune theo tải cao/biến động)
   ECS service "checkout"  (auto-scaling riêng, tách biệt hoàn toàn)
   → browsing tăng tải KHÔNG kéo checkout theo (và ngược lại)

Bước 2 — Routing tại edge:
   CloudFront Function (JS nhẹ, chạy tại edge, chi phí/latency thấp nhất)
   → đọc JWT ngay tại edge
   → route request đến đúng ECS service (browsing / checkout)
   → dựa trên: module được yêu cầu + user access level + tải hiện tại
```

Hai quyết định này khớp nhau: tách service giải quyết vấn đề **scaling độc lập** (nguyên nhân gốc của "load imbalance" trong đề), còn CloudFront Functions giải quyết vấn đề **routing dựa trên JWT với chi phí/latency thấp nhất**, tận dụng đúng lớp CloudFront đã có sẵn — không cần thêm hạ tầng mới.

#### Vì sao A sai — Anh chọn nhầm vì thêm tầng trung gian không cần thiết

**A: đặt API Gateway trước ECS, dùng Lambda authorizer xác thực JWT, tận dụng caching/traffic management của API Gateway** — về mặt kỹ thuật *có thể chạy được*, nhưng đây là lựa chọn sai vì:

1. **Thêm một tầng hoàn toàn mới (API Gateway + Lambda authorizer)** giữa client và ECS trong khi CloudFront **đã đứng sẵn ở đó** — tăng độ phức tạp vận hành và thêm điểm có thể lỗi (operational overhead, potential points of failure).
2. **Lambda authorizer chạy Lambda thật** cho mỗi request cần xác thực → có **cold start và latency cao hơn** đáng kể so với CloudFront Function (chạy JS thuần tại edge, không có runtime Lambda phía sau).
3. **API Gateway caching/traffic management không hiệu quả bằng CloudFront edge caching/routing** cho use case này — CloudFront vốn đã tối ưu cho việc này.

Nói ngắn gọn: A đúng về mặt "có xử lý được JWT và routing", nhưng **sai về mức độ phù hợp** — dùng công cụ nặng hơn mức cần thiết trong khi đã có công cụ nhẹ hơn, sẵn có, rẻ hơn.

#### Vì sao B, D sai

- **B (Lambda cho cả 2 module + API Gateway):** yêu cầu **refactor toàn bộ ứng dụng** sang serverless — không khả thi/tốn kém cho platform e-commerce hiện có, lại gặp khó khăn quản lý state và long-running process vốn phổ biến trong ứng dụng thương mại điện tử.
- **D (chuyển sang EKS + ECS Service Connect):** sai về mặt kỹ thuật cơ bản — **ECS Service Connect chỉ hoạt động trong cụm ECS**, không tương thích với Kubernetes/EKS. EKS dùng cơ chế service discovery/communication riêng của Kubernetes. Đây là đáp án "nghe hoành tráng" nhưng vi phạm ràng buộc kỹ thuật rõ ràng.

| Lựa chọn | Scale 2 module độc lập? | Routing layer | Vấn đề |
|---|---|---|---|
| **C (đúng)** | Có — 2 ECS service riêng | CloudFront Functions (nhẹ, tại edge) | — |
| A | Không (không tách ECS service) | API Gateway + Lambda authorizer | Thêm tầng nặng, tăng latency/complexity |
| B | Không (refactor hết sang Lambda) | API Gateway | Refactor toàn bộ ứng dụng, không thực tế |
| D | Có (nhưng đổi hẳn nền tảng) | ECS Service Connect trên EKS | Không tương thích kỹ thuật (ECS SC ≠ EKS) |

#### Quy tắc nhớ cho thi

- **CloudFront Functions**: JS nhẹ, chạy tại edge, phù hợp cho việc **đọc header/JWT đơn giản, sửa request/response, routing nhẹ**, chi phí và latency thấp nhất trong các lựa chọn CloudFront-side.
- **Lambda@Edge**: xử lý logic phức tạp hơn, tích hợp với service khác, nhưng **latency và chi phí cao hơn** CloudFront Functions.
- **"Load imbalance giữa 2 module trong cùng ứng dụng"** → tách thành **service riêng, auto-scaling riêng** — không cố scale chung một service.
- **Thấy giải pháp thêm hẳn một tầng service mới (API Gateway, chuyển nền tảng) trong khi hạ tầng hiện tại đã đủ** → nghi ngờ, đây thường là đáp án "over-engineering".
- **ECS Service Connect** chỉ dùng trong ECS, không áp dụng được cho EKS/Kubernetes.

### TD explanation

Amazon ECS is a fully managed, opinionated container orchestration service that delivers the easiest way for organizations to build, deploy, and manage containerized applications at any scale on AWS. By creating separate ECS services for the browsing and checkout modules, you can independently scale each service based on its specific load requirements, ensuring optimal resource utilization and cost-efficiency.

Automatic scaling is the ability to automatically increase or decrease the desired count of tasks in your Amazon ECS service. Amazon ECS leverages the Application Auto Scaling service to provide this functionality.

Amazon CloudFront Functions allow lightweight JavaScript code to run directly at CloudFront edge locations. This enables fast, low-latency customization of requests and responses—such as inspecting JWTs, modifying headers, or routing—without invoking additional services.

Lambda@Edge, by contrast, runs more powerful AWS Lambda functions associated with CloudFront events. While Lambda@Edge supports more complex logic and integrations, it generally has higher latency and cost than CloudFront Functions.

JSON Web Tokens (JWT) is a popular open standard for securely sharing information as a JSON object between different parties.

By creating separate ECS services for the browsing and checkout modules, you can effectively isolate the two components, allowing them to scale independently based on their respective load requirements. This separation of concerns ensures that the high-traffic browsing module does not adversely impact the performance of the checkout module and vice versa.

Each ECS service can have its own auto-scaling configuration tailored to its specific load patterns and resource requirements. This ensures that resources are allocated efficiently, preventing over-provisioning or under-provisioning of resources for either module. During peak traffic periods, the browsing module can scale up seamlessly without affecting the checkout module’s performance.

By leveraging CloudFront Functions, you can inspect the JWT to extract user roles, access levels, and the requested module. Based on this information, CloudFront Functions can intelligently route requests to the appropriate ECS service, ensuring that users are directed to the correct module based on their permissions and the requested functionality.

This solution leverages the existing infrastructure, including Amazon ECS and Amazon CloudFront, minimizing the need for significant architectural changes or migrations. This approach reduces complexity and potential risks associated with transitioning to new services or platforms.

Hence, the correct answer is: Create separate ECS services for browsing and checkout modules, each with its own auto-scaling configuration. Use CloudFront Functions to inspect JWT, route requests to the appropriate ECS service based on the requested module, user access level, and load.

The option that says: Transition the platform to Amazon Elastic Kubernetes Service, separating the product browsing and checkout functionalities into distinct Kubernetes pods. Implement ECS Service Connect to orchestrate service communication within the cluster, enabling mutual TLS (mTLS) to secure pod-to-pod interactions. Configure the Service Connect virtual service to utilize JWT for authenticating requests, directing them from the browsing pod to the checkout pod based on user permissions and session data encoded in the JWT is incorrect because Amazon ECS Service Connect is primarily designed to work with Amazon ECS clusters, not Kubernetes clusters. EKS uses Kubernetes-native tools for service communication and discovery, not ECS-specific services. Therefore, ECS Service Connect cannot be used in an EKS environment.

The option that says: Implement API Gateway in front of ECS services, using AWS Lambda authorizer to authenticate users based on JWT. Utilize API Gateway’s caching and traffic management capabilities, directing requests based on JWT attributes to the correct module is incorrect. While API Gateway and Lambda authorizers can handle JWT authentication and request routing, this approach may simply introduce additional latency and complexity compared to using CloudFront Functions. Additionally, API Gateway’s caching and traffic management capabilities may not be as efficient as CloudFront’s edge caching and routing capabilities for this specific use case. Lastly, introducing API Gateway as an additional layer between the client and ECS services may increase operational overhead and potential points of failure.

The option that says: Refactor the application to use AWS Lambda for both modules, with API Gateway routing requests based on JWT. Use CloudFront for static content delivery and JWT validation is incorrect. This option requires a significant refactoring of the application to use AWS Lambda, which may not be feasible or cost-effective for an existing e-commerce platform. Transitioning to a serverless architecture with Lambda may only introduce challenges in managing state and handling long-running processes, which are common in e-commerce applications.

 

References:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html

https://aws.amazon.com/ecs/faqs/

 

Check out the following Cheat Sheets:

https://tutorialsdojo.com/amazon-cloudfront/

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

</details>

<a id="q48"></a>

## Q48

A retail company is using Amazon OpenSearch Service to analyze its sales and inventory data. Every week, new data from an Amazon S3 Standard bucket is indexed and loaded into a 20-data node Amazon OpenSearch cluster. Read-only queries are performed on this data to monitor recent trends. After 1 week, it’s occasionally accessed for identifying long-term patterns. After three months, the index containing the older data is deleted from the system. However, due to audit requirements, the company needs to keep a complete copy of all processed data.

The company is looking for strategies to reduce storage costs without abandoning Amazon OpenSearch. A slower query response time on infrequently accessed data is acceptable as long as it can be retrieved on demand.

Which solution fits the requirements while being the MOST cost-effective?

- **A.** Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Infrequently Access tier.
- **B.** Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive.
- **C.** Reconfigure the OpenSearch cluster by replacing all data nodes with a mix of UltraWarm nodes and cold storage nodes. Use the UltraWarm node for indexing and the cold storage for reading. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive.
- **D.** Upsize the OpenSearch cluster by adding UltraWarm nodes to improve read performance. Use an S3 lifecycle policy to delete data older than 3 months.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** OpenSearch read-only after 1 wk; delete index after 3 mo; keep full audit copy

🪤 **Your trap:** S3 IA pricier than Deep Archive for rarely-read audit copy

🧠 **Rule:** OpenSearch tiering → UltraWarm + ISM to cold; audit archive → S3 Glacier Deep Archive.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 Standard (raw data) → index vào OpenSearch (20 data node)

Vòng đời truy cập dữ liệu trong OpenSearch:
   Tuần 1        : truy vấn thường xuyên (read-only, theo dõi trend gần đây)
   Sau 1 tuần    : occasionally accessed (tìm pattern dài hạn)
   Sau 3 tháng   : index bị XÓA khỏi OpenSearch
                   NHƯNG vẫn phải giữ bản đầy đủ cho AUDIT

Yêu cầu: giảm chi phí lưu trữ, KHÔNG rời bỏ OpenSearch,
         chấp nhận query chậm hơn cho dữ liệu ít truy cập
```

Đáp án đúng: **B** (downsize + UltraWarm + ISM sang cold sau 1 tuần + S3 lifecycle sang **Glacier Deep Archive** sau 3 tháng). Anh chọn **A** — giống hệt B nhưng chọn nhầm **S3 Infrequent Access (IA)** thay vì Glacier Deep Archive.

#### Vì sao B đúng — khớp đúng 3 tầng chi phí với 3 giai đoạn truy cập

```
Data node (hot)  → UltraWarm (sau 1 tuần, đọc ít, dùng S3 + cache)
                          │ ISM policy tự động chuyển
                          ▼
                   Cold storage (detach index, chỉ cần khi query, reattach khi cần)
                          │ (index bị xóa sau 3 tháng, nhưng vẫn cần audit copy)
                          ▼
              S3 Glacier Deep Archive (rẻ nhất, phù hợp audit — truy cập 1-2 lần/năm)
```

OpenSearch có 3 tier lưu trữ: **Hot** (EBS/instance store, nhanh nhất, đắt nhất), **UltraWarm** (dùng S3 + caching, rẻ hơn nhiều cho dữ liệu read-only ít truy vấn), **Cold** (rẻ nhất trong OpenSearch, phải "reattach" mới query được, phù hợp dữ liệu gần như không đụng tới). ISM (Index State Management) tự động hóa việc chuyển index giữa các tier theo tuổi/điều kiện.

Sau khi index bị xóa khỏi OpenSearch (3 tháng), yêu cầu audit chỉ cần **giữ bản sao**, KHÔNG cần truy vấn nhanh — đây chính xác là use case của **S3 Glacier Deep Archive**: rẻ nhất trong các storage class S3, cho dữ liệu truy cập 1-2 lần/năm hoặc gần như không bao giờ, chấp nhận thời gian phục hồi (retrieval) chậm.

#### Vì sao A sai — Anh chọn nhầm S3 IA thay vì Glacier Deep Archive

**A** giống hệt B ở phần OpenSearch (downsize + UltraWarm + ISM), chỉ khác duy nhất ở đích lifecycle S3: **A dùng S3 Infrequent Access (IA)**. Vấn đề: dữ liệu ở đây là **bản audit lưu trữ dài hạn, gần như không bao giờ được đọc** (chỉ audit khi cần) — đây là kịch bản kinh điển của Glacier Deep Archive, không phải IA. S3 IA rẻ hơn Standard nhưng **đắt hơn đáng kể so với Glacier Deep Archive**, trong khi đề đã nói rõ "slower query response time... is acceptable" — tức công ty sẵn sàng đánh đổi tốc độ lấy chi phí thấp nhất. Chọn IA ở đây là bỏ lỡ mức tiết kiệm lớn nhất có thể mà không đánh đổi thêm gì (đằng nào cũng không cần đọc nhanh).

#### Vì sao C, D sai

- **C:** "replace all data nodes with a mix of UltraWarm + cold storage nodes, dùng UltraWarm để index" — sai về bản chất kỹ thuật: **UltraWarm được thiết kế cho dữ liệu read-only**, không dùng để index (ghi) dữ liệu mới. Đây là một constraint kỹ thuật cứng của OpenSearch tier.
- **D:** "upsize cluster bằng UltraWarm để tăng read performance, xóa dữ liệu sau 3 tháng bằng S3 lifecycle" — sai hai điểm: (1) **upsize thay vì downsize** đi ngược mục tiêu giảm chi phí; (2) chỉ **xóa** dữ liệu sau 3 tháng, không hề giữ bản audit — vi phạm thẳng yêu cầu "keep a complete copy of all processed data".

#### Bảng so sánh storage class S3 liên quan (kiến thức nền)

| Storage class | Chi phí lưu trữ | Thời gian truy xuất | Phù hợp khi |
|---|---|---|---|
| S3 Standard | Cao nhất trong nhóm | Ngay lập tức (ms) | Truy cập thường xuyên |
| S3 Standard-IA | Thấp hơn Standard | Ngay lập tức (ms) | Truy cập không thường xuyên nhưng cần nhanh khi cần |
| S3 One Zone-IA | Thấp hơn Standard-IA | Ngay lập tức (ms) | Dữ liệu không thường xuyên, chấp nhận rủi ro 1 AZ |
| S3 Glacier Instant Retrieval | Thấp hơn IA | Ngay lập tức (ms) | Archive nhưng thi thoảng cần truy cập tức thì |
| S3 Glacier Flexible Retrieval | Thấp hơn Instant Retrieval | Phút → giờ | Archive, truy cập vài lần/năm, không cần tức thì |
| **S3 Glacier Deep Archive** | **Thấp nhất** | **Giờ** (thường 12h) | **Lưu trữ dài hạn, audit/compliance, truy cập 1-2 lần/năm** |

#### Quy tắc nhớ cho thi

- **OpenSearch tiering theo độ mới của dữ liệu** → Hot → **UltraWarm** (read-only, ít truy vấn) → **Cold** (gần như không truy vấn, cần reattach) → dùng **ISM** để tự động hóa.
- **UltraWarm chỉ dùng cho dữ liệu read-only** — không index/ghi mới trên UltraWarm.
- **"Audit/compliance copy, truy cập 1-2 lần/năm hoặc gần như không bao giờ, chấp nhận chậm"** → luôn nghĩ **S3 Glacier Deep Archive**, không phải S3 IA (IA vẫn còn đắt và có tốc độ truy xuất nhanh mà đề không cần).
- Thấy hai đáp án giống hệt nhau chỉ khác storage class cuối cùng → đọc kỹ yêu cầu về tần suất truy cập và độ chấp nhận chậm để chọn đúng tier rẻ nhất phù hợp.

### TD explanation

Amazon OpenSearch Service offers three storage tiers:

-Hot – provides the fastest possible performance for indexing and searching new data. Standard data nodes use hot storage, which takes the form of instance store or Amazon EBS volumes attached to each node.

-UltraWarm – uses Amazon S3 with related caching solutions to improve performance. UltraWarm offers significantly lower costs per GiB for read-only data that you query less frequently and don’t need the same performance as hot storage. Data stored in UltraWarm is immutable.

-Cold – optimized to store infrequently accessed or historical data at a cheaper price per GB per month. When you use cold storage, you detach your indexes from the UltraWarm tier, making them inaccessible. You can reattach these indexes when you need to query that data.

In the scenario, since the company is primarily performing read-only queries and the data is less frequently accessed after 1 week, it would benefit from reducing the number of data nodes and adding more cost-effective UltraWarm storage. Using Index State Management (ISM) policies to transition data to cold storage after 1 week would ensure efficient use of resources. Moreover, transitioning data older than 3 months to the S3 Glacier Deep Archive meets the company’s requirements to keep a complete copy of all processed data for audit purposes. Amazon S3 Glacier Deep Archive is a secure, durable, and extremely low-cost Amazon S3 cloud storage class, designed for the long-term retention of data that is accessed once or twice a year.

Therefore, the correct answer is: Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive.

The option that says: Upsize the OpenSearch cluster by adding UltraWarm nodes to improve read performance. Use an S3 lifecycle policy to delete data older than 3 months is incorrect. This option is not cost-effective as it would increase the infrastructure costs without necessarily bringing significant benefits, as the company is okay with slower query response times for infrequently accessed data. Moreover, it only uses an S3 lifecycle policy to delete data older than 3 months, which does not fulfill the company’s requirement to keep a complete copy of all processed data for auditing purposes.

The option says: Downsize the OpenSearch cluster by reducing the number of its data nodes. Add UltraWarm nodes to compensate for the read capacity. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Infrequently Access tier is incorrect. Although the S3 IA tier costs less than Standard S3, it is more expensive than the S3 Glacier Deep Archive. Considering the company’s requirement to store data for at least three months and only occasionally access it, the Glacier Deep Archive would be a more cost-effective choice.

The option that says: Reconfigure the OpenSearch cluster by replacing all data nodes with a mix of UltraWarm nodes and cold storage nodes. Use the UltraWarm node for indexing and the cold storage for reading. Create an Index State Management (ISM) policy that moves data to cold storage after 1 week. Use an S3 lifecycle policy to transition data older than 3 months to the S3 Glacier Deep archive is incorrect. This approach is not valid because UltraWarm nodes are designed to work on read-only data.

 

References:

https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html

https://aws.amazon.com/blogs/big-data/choose-the-right-storage-tier-for-your-needs-in-amazon-opensearch-service/

 

Check out this Amazon OpenSearch Cheat Sheet:

https://tutorialsdojo.com/amazon-opensearch-service/

</details>
