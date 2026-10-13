# TD Set 6 (16 questions, Gate 1) — Wrong Answer Review (5 questions)

Source: `td6_isolated_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td6_isolated_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q1](#q1) | ✅ 10-13 | ☐ | ☐ |
| A | [Q11](#q11) | ✅ 10-13 | ☐ | ☐ |
| A | [Q16](#q16) | ✅ 10-13 | ☐ | ☐ |
| B | [Q6](#q6) | ✅ 10-13 | ☐ | ☐ |
| B | [Q15](#q15) | ✅ 10-13 | ☐ | ☐ |

---

# Group A — Overbuilt — cheapest/lightest managed option wins (3)

<a id="q1"></a>

## Q1

A research company specializing in agricultural innovation operates a fleet of IoT devices across experimental farms to automate and monitor water distribution, temperature regulation, and humidity control. The collected telemetry data is stored in Optimized Row Columnar (ORC) format within the Hadoop Distributed File System (HDFS), running on a persistent Amazon EMR cluster. The company’s data analytics team runs SQL queries using Apache Presto on the same always-on EMR environment. These queries scan large datasets, complete within 15 minutes, and are executed only between 6 PM and 2 AM as part of the company’s nightly analysis routine.
With cloud costs climbing, the research company’s leadership seeks a more cost-effective solution to support these recurring SQL-based data queries. A solutions architect must recommend the most economical approach while maintaining query performance and compatibility with the existing ORC data format.
What is the most cost-effective recommendation that the solutions architect can make?

- **A.** Persist data in Amazon S3, and execute SQL-based analytics through Amazon Athena, using schema definitions stored in the AWS Glue Data Catalog.
- **B.** Load your datasets into Amazon Redshift and perform analytics directly within the Redshift data warehouse environment.
- **C.** Use AWS Glue ETL jobs to ingest the ORC files into Amazon Aurora and enable SQL-based querying.
- **D.** Use AWS Lambda functions to convert the ORC files into JSON and store them in Amazon DynamoDB for querying.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** queries only 6 PM–2 AM, ORC format, most cost-effective

🪤 **Your trap:** Redshift = always-on cluster + data loading; paying 24/7 for a nightly window

🧠 **Rule:** Occasional SQL on ORC/Parquet → S3 + Athena + Glue Data Catalog (pay per scan)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IoT devices ──► ORC trên HDFS (EMR luôn bật)
                     │
                     ▼
        Presto SQL: 6 PM ─────────► 2 AM   (mỗi query < 15 phút)
        |<-- 8 tiếng/ngày có query -->|    16 tiếng còn lại: KHÔNG ai query
                     
Yêu cầu: RẺ NHẤT + giữ performance + tương thích định dạng ORC
```

Từ khóa quyết định: **"chỉ query 6 PM–2 AM"** + **"ORC"** + **"most cost-effective"**. Đáp án đúng: **A (S3 + Athena + Glue Data Catalog)**. Anh chọn B (Redshift).

⚠️ Lỗi lặp lại: stem nói "rẻ nhất" nhưng Anh chọn option nặng hơn, over-scoped (cùng pattern với TD3 group A). Khi thấy chữ "cheapest / least overhead", hãy tự hỏi "có phương án serverless, trả theo lần dùng không?" trước khi chọn service provisioned.

#### Vì sao A đúng

```
ORC files ──► S3 bucket ◄── Athena (serverless, SQL chuẩn)
                  ▲               │
                  └── Glue Data Catalog (schema/metadata cho ORC)
Chi phí = số data Athena scan mỗi query. Không query = không tốn phí compute.
```

- **Athena đọc thẳng ORC trên S3**, nên không cần chuyển đổi định dạng và không cần load dữ liệu.
- **Glue Data Catalog** là metadata store để Athena hiểu cấu trúc bảng.
- **Serverless**: không có cluster nào chạy 24/7. Workload chỉ 8 tiếng/đêm, query dưới 15 phút, rất hợp mô hình pay-per-query.
- Giữ nguyên ORC nên không phải viết lại pipeline dữ liệu.

#### Vì sao B (Redshift) sai

Redshift là **provisioned data warehouse**: tốn phí compute + storage kể cả khi không có query nào chạy. Dùng cho workload liên tục, throughput cao, không hợp với pattern "8 tiếng/đêm".

Ngoài ra, dữ liệu đang nằm trên HDFS, nên phải **load vào bảng Redshift** trước. Đây là thêm công sức ETL và thêm chi phí lưu trữ, trong khi đề chỉ hỏi cách rẻ nhất.

Anh nhìn thấy "SQL analytics trên dataset lớn" và nghĩ ngay "data warehouse = Redshift". Nhưng đề lại nhấn mạnh **tần suất sử dụng thấp + cost**, nên phải ưu tiên mô hình trả theo lượng dùng.

#### Các option còn lại

- **C (Glue ETL vào Aurora):** Aurora tối ưu cho OLTP, không phải scan analytics trên khối dữ liệu lớn. ETL thêm chi phí xử lý và lưu trữ không cần thiết.
- **D (Lambda convert ORC sang JSON, lưu DynamoDB):** DynamoDB là NoSQL key-value cho truy vấn độ trễ thấp, không hỗ trợ SQL analytics. Lambda bị giới hạn memory/thời gian khi xử lý file ORC lớn. Chuyển đổi định dạng là việc thừa.

#### So sánh nhanh

| Phương án | Mô hình tính phí | Cần load/convert dữ liệu | Hợp với query 8 tiếng/đêm |
|---|---|---|---|
| **A. S3 + Athena + Glue** | Theo data scan mỗi query | Không (đọc ORC trực tiếp) | Rất hợp |
| B. Redshift | Cluster provisioned, tính phí liên tục | Có (load vào bảng) | Không hợp |
| C. Glue ETL + Aurora | ETL + DB instance + storage | Có | Không hợp |
| D. Lambda + DynamoDB | Lambda + DynamoDB | Có (ORC sang JSON) | Không hợp |

#### Lưu ý thực tế

- Bước chuyển từ HDFS sang S3 là phần di chuyển dữ liệu một lần; sau đó EMR cluster luôn bật không còn cần thiết cho workload này.
- Vì Athena tính phí theo lượng data scan, các định dạng columnar như **ORC/Parquet** (và partition) giúp giảm data scan nên giảm chi phí. Đây là lý do giữ ORC là lợi thế.

#### Quy tắc nhớ cho thi

- **Thấy "query thưa / theo lịch / ad-hoc" + "ORC/Parquet" + "cost-effective"** → **S3 + Athena + Glue Data Catalog**
- **Thấy "cheapest" / "least overhead"** → loại ngay service provisioned chạy 24/7 nếu có lựa chọn serverless
- **Redshift** chỉ thắng khi đề nói workload analytics liên tục, nặng, nhiều user đồng thời
- **Aurora / DynamoDB cho analytics trên file lớn** → gần như luôn sai

### TD explanation

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds.
Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. Athena scales automatically, running queries in parallel, so results are fast, even with large datasets and complex queries.

Athena can read data directly from Amazon S3 in ORC format, making it highly compatible with the company’s existing dataset. The AWS Glue Data Catalog serves as the centralized metadata store, allowing Athena to interpret and query the structure of the ORC files. Since the research company only needs to run queries during a narrow time window each night, keeping a persistent EMR cluster active is simply wasteful. Athena is cost-effective because the company is billed just for the data scanned per query, and the infrastructure does not need to run continuously, reducing compute-related expenses.
Hence, the correct answer is: Persist data in Amazon S3, and execute SQL-based analytics through Amazon Athena, using schema definitions stored in the AWS Glue Data Catalog.
The option that says: Load your datasets into Amazon Redshift and perform analytics directly within the Redshift data warehouse environment is incorrect. Amazon Redshift is a provisioned data warehouse that incurs ongoing compute and storage costs, regardless of whether queries are being executed. It is primarily designed for high-throughput, continuous analytical workloads, not intermittent query patterns that only occur during a specific time window. Additionally, Redshift does not natively support querying ORC files stored in HDFS. The data must be loaded into Redshift tables, introducing unnecessary overhead.
The option that says: Use AWS Glue ETL jobs to ingest the ORC files into Amazon Aurora and enable SQL-based querying is incorrect. Amazon Aurora is a relational database optimized for transactional workloads, not for large-scale analytics on ORC-formatted files. Using AWS Glue ETL jobs to transform and load ORC data into Aurora introduces processing and storage costs that are simply unnecessary for the use case. Aurora does not support the high-volume data scanning common in big data SQL workloads, making this solution technically inappropriate and financially inefficient.
The option that says: Use AWS Lambda functions to convert the ORC files into JSON and store them in Amazon DynamoDB for querying is incorrect. Amazon DynamoDB is a NoSQL key-value and document database optimized primarily for low-latency, high-throughput transactional operations, not for complex SQL-based analytics across large datasets. Converting ORC files to JSON introduces unnecessary transformation overhead, and using Lambda for this task is simply unsuitable due to its memory and execution time limits, especially when handling large ORC files. Additionally, DynamoDB does not support SQL or efficient data scanning for analytical queries, making this solution technically invalid and economically impractical for the company’s use case.

References:
https://docs.aws.amazon.com/athena/latest/ug/what-is.html
https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html

Check out this Amazon Athena Cheat Sheet:
https://tutorialsdojo.com/amazon-athena/

</details>

<a id="q11"></a>

## Q11

An international e-commerce company relies on Amazon CloudFront to deliver its multi-regional Amazon ECS-based web store with fast, scalable performance. Over recent months, customers around the globe have started reporting sluggish page load times, particularly during flash sales and heavy promotional events.
The performance reliability team has spotted a troubling pattern: CloudFront’s cache hit ratio has consistently decreased. Amazon CloudWatch metrics reveal the root cause: query strings in some request URLs are inconsistent. Parameter order shifts unpredictably, and values alternate between mixed-case and lowercase.
Which steps should be implemented to rapidly restore CloudFront’s cache hit/ratio with the least operational overhead and cost?

- **A.** Configure a CloudFront Function on the Viewer Request event that alphabetically sorts all query parameter keys and enforces lowercase for both parameter names and values
- **B.** Attach a Lambda@Edge handler to the CloudFront distribution’s Viewer Request event that alphabetically sorts each query string parameter and converts all names and values to lowercase to ensure consistent cache key generation
- **C.** Place a reverse proxy layer downstream of the load balancer to intercept incoming URLs and rewrite all query string characters to lowercase
- **D.** Modify the CloudFront distribution’s cache or origin-request policy to stop including query-string parameters in the cache key

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** normalize query strings, least overhead AND cost

🪤 **Your trap:** Lambda@Edge works but is heavier and pricier than needed

🧠 **Rule:** Lightweight viewer-request rewrites → CloudFront Functions; Lambda@Edge only for network calls/body/longer runtime

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Viewer ──► CloudFront (edge) ──► ECS web store (nhiều Region)
              │
   cache key = path + query string
   /p?color=Red&size=L      ─┐
   /p?size=l&color=red       ├─► 3 cache key khác nhau cho CÙNG nội dung
   /p?SIZE=L&Color=RED      ─┘   => cache hit ratio giảm
```

Nguyên nhân gốc: query string **thứ tự tham số khác nhau** và **hoa/thường lẫn lộn**, nên CloudFront coi mỗi biến thể là một object riêng. Yêu cầu: khôi phục nhanh cache hit ratio với **overhead VÀ cost thấp nhất**.

Đáp án đúng: **A (CloudFront Function, Viewer Request)**. Anh chọn B (Lambda@Edge, cũng Viewer Request).

⚠️ Lỗi lặp lại: B không sai về mặt kỹ thuật (đề giải thích nó vẫn chuẩn hóa được), nhưng stem hỏi "least overhead and cost" nên phải chọn công cụ nhẹ nhất đủ làm việc. Đây là pattern giống TD3 group A: chọn option nặng/over-scoped khi đề yêu cầu rẻ và gọn.

#### Vì sao A đúng

Tác vụ chỉ là **sort tham số + lowercase** trên request. Đây là chuyển đổi chuỗi thuần, không cần gọi mạng, không đọc body, chạy ngắn.

- **CloudFront Functions** viết bằng JavaScript, chạy ở edge, khởi động dưới 1 ms, scale ngay lập tức cho hàng triệu request/giây.
- Là tính năng gốc của CloudFront: build, test, deploy ngay trong CloudFront, không cần tạo Lambda, IAM role riêng hay replicate qua Region.
- Gắn vào **Viewer Request**, là bước diễn ra trước khi CloudFront tính cache key. Nhờ vậy các URL tương đương sẽ về cùng một key.
- Theo TD, giá khoảng 0.10 USD mỗi triệu request, rẻ hơn Lambda@Edge đáng kể (TD nói Lambda@Edge đắt gấp khoảng 6 lần).

#### Vì sao B (Lambda@Edge) không tối ưu

Về mặt kỹ thuật B làm được, TD thừa nhận đây là cách "sound". Nhưng so với A:

- Nặng hơn: cần deploy Lambda, role, và Lambda@Edge có thêm độ trễ khởi động (TD nêu khoảng 1 đến 2 ms cold start).
- Đắt hơn nhiều cho cùng một việc.
- Lambda@Edge được thiết kế cho các tác vụ CloudFront Functions không làm được: gọi mạng/dịch vụ khác, đọc request body, runtime dài hơn, chạy ở origin request/response.

Với bài toán chỉ chuẩn hóa query string thì dùng Lambda@Edge là "dao mổ trâu giết gà".

#### Hai option còn lại

- **C (reverse proxy sau load balancer):** CloudFront đã tính cache key **trước khi** forward về backend, nên chuẩn hóa ở sau không giúp ích gì cho cache hit ratio. Còn thêm một lớp hạ tầng phải vận hành.
- **D (bỏ query string khỏi cache key):** nghe đơn giản nhưng sai nghiệp vụ. Mọi request dù có tham số khác nhau sẽ nhận cùng một response cache. Ví dụ `?user=alice` có thể bị cache rồi trả cho người khác, tức là phục vụ **sai nội dung**.

#### So sánh CloudFront Functions và Lambda@Edge

| Tiêu chí | CloudFront Functions | Lambda@Edge |
|---|---|---|
| Trigger | Viewer request/response | Viewer + Origin request/response |
| Khởi động | Dưới 1 ms | Có cold start |
| Chi phí | Thấp (theo TD khoảng 0.10 USD/triệu request) | Cao hơn đáng kể |
| Việc phù hợp | Rewrite URL, chuẩn hóa query/header, redirect đơn giản | Gọi network, đọc body, logic nặng/dài |
| Vận hành | Native trong CloudFront | Lambda + role + replicate |

#### Quy tắc nhớ cho thi

- **Thấy "chuẩn hóa query string / header / URL rewrite nhẹ" + "least overhead / cost"** → **CloudFront Functions (Viewer Request)**
- **Cần gọi network, đọc body, xử lý lâu, hoặc hook origin request/response** → **Lambda@Edge**
- **Cache hit ratio thấp vì query string lộn xộn** → chuẩn hóa ở edge, KHÔNG bỏ query string khỏi cache key
- **Backend/proxy rewrite** không ảnh hưởng cache key vì key được tính ở CloudFront trước

### TD explanation

With CloudFront Functions, you can write lightweight functions in JavaScript for high-scale, latency-sensitive CDN customizations. Your functions can manipulate the requests and responses that flow through CloudFront, perform basic authentication and authorization, generate HTTP responses at the edge, and more. The CloudFront Functions runtime environment offers submillisecond startup times, scales immediately to handle millions of requests per second, and is highly secure. CloudFront Functions is a native feature of CloudFront, which means you can build, test, and deploy your code entirely within CloudFront.
When you associate a CloudFront function with a CloudFront distribution, CloudFront intercepts requests and responses at CloudFront edge locations and passes them to your function. You can invoke CloudFront Functions when the following events occur:
When CloudFront receives a request from a viewer (viewer request)
Before CloudFront returns the response to the viewer (viewer response)

Using a CloudFront Function at the Viewer Request event to alphabetically sort and lowercase query parameters is the optimal solution for this specific problem. CloudFront Functions are lightweight, execute in sub-millisecond time, and cost-efficient (~$0.10 per million requests). This option delivers the fastest remediation with minimal complexity or overhead.
Hence, the correct answer is: Configure a CloudFront Function on the Viewer Request event that alphabetically sorts all query parameter keys and enforces lowercase for both parameter names and values.
The option that says: Attach a Lambda@Edge handler to the CloudFront distribution’s Viewer Request event that alphabetically sorts each query string parameter and converts all names and values to lowercase to ensure consistent cache key generation is incorrect. Using Lambda@Edge is actually a technically sound approach: CloudFront calculates the cache key at that viewer-level stage, so normalizing the query string there ensures identical URLs map to the same cache key, reducing cache fragmentation and improving the cache hit ratio. However, this option is suboptimal compared to CloudFront Function. Deploying a CloudFront Function at the Viewer Request event achieves the same normalization (sorting and lowercasing query strings) but is far more lightweight, faster, and cost-effective. A CloudFront Function runs in sub-millisecond time at every edge location, whereas Lambda@Edge incurs a 1 to 2-millisecond cold-start latency and costs around 6 times. For a task as simple as query-string normalization, relying on Lambda@Edge introduces unnecessary latency and overhead compared to the more efficient CloudFront Function alternative.
The option that says: Modify the CloudFront distribution’s cache or origin-request policy to stop including query-string parameters in the cache key is incorrect. Disabling query-string–based caching can lead to wrong content being served, not just performance issues. When CloudFront excludes query strings from the cache key, every request, regardless of its unique query data, receives the same cached response. If one user’s request carries specific parameters (e.g., ?user=alice), CloudFront might cache that particular version and then serve it to another user requesting the same path without those parameters. In effect, CloudFront treats what could be distinct content as identical.
The option that says: Place a reverse proxy layer downstream of the load balancer to intercept incoming URLs and rewrite all query string characters to lowercase is incorrect. Placing a reverse proxy layer downstream of the load balancer to normalize URLs won’t improve cache hit ratios because CloudFront computes its cache key before forwarding requests to any backend. As a result, any normalization done later in the request pipeline simply does not affect caching at all. Without normalization at the edge, cache fragmentation persists. This approach is ineffective.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q16"></a>

## Q16

A game development startup runs a multiplayer gaming platform powered by Amazon EC2 instances and AWS Lambda functions. The EC2 fleet supports always-on services like matchmaking and leaderboards, which run under a consistent and stable workload. In contrast, Lambda functions are triggered by unpredictable, bursty events like player actions, achievements, or chat messages.
To keep gameplay smooth and responsive, the platform uses a high-performance caching layer backed by Amazon MemoryDB for Redis, with dedicated MemoryDB cache nodes storing session data and player stats.
An AWS solutions architect is tasked with designing a cost-optimized infrastructure that cuts down on monthly operating costs without sacrificing performance.
What is the most cost-effective strategy to meet these goals?

- **A.** Use an EC2 instance Savings Plan to commit to the EC2 compute resources financially. Apply a Compute Savings Plan to offset the baseline utilization of Lambda functions. Allocate reserved nodes to provision capacity for the MemoryDB cache nodes.
- **B.** Leverage On-Demand pricing across all services to maintain flexibility. Use Lambda provisioned concurrency for better performance. Rely on auto-scaling EC2 instances instead of committing to Savings Plans.
- **C.** Use a Compute Savings Plan to cover EC2, Lambda, and MemoryDB usage in a single commitment. Configure Lambda reserved concurrency to manage unpredictable workloads. Provision MemoryDB cache nodes by acquiring reserved nodes to ensure dedicated capacity.
- **D.** Use EC2 Spot Instances to reduce compute costs for matchmaking and leaderboard services. Use On-Demand Lambda execution. Replace MemoryDB with Amazon ElastiCache.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** steady EC2 + bursty Lambda + MemoryDB nodes, cheapest

🪤 **Your trap:** Compute Savings Plans do NOT cover MemoryDB

🧠 **Rule:** Steady EC2 → EC2 Instance SP; Lambda → Compute SP; MemoryDB/ElastiCache/RDS → reserved nodes

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
┌─ EC2 fleet (matchmaking, leaderboard) ── ổn định, luôn bật
├─ Lambda (player actions, chat)         ── bursty, khó đoán
└─ MemoryDB for Redis (session, stats)   ── cache node chạy liên tục

Yêu cầu: giảm chi phí hàng tháng NHIỀU NHẤT, không đổi performance
```

Mỗi thành phần có pattern sử dụng khác nhau, nên cần **mô hình mua khác nhau cho từng service**. Đáp án đúng: **A**. Anh chọn C.

⚠️ Lỗi lặp lại: chọn gói "gộp một cam kết cho tất cả" (over-scoped, nghe gọn) trong khi stem hỏi "most cost-effective". Cùng pattern với TD3 group A: option rộng/tiện hơn nhưng bỏ lỡ mức giảm sâu hơn.

#### Vì sao A đúng, ghép theo từng thành phần

```
EC2 ổn định  ──► EC2 Instance Savings Plan  (giảm sâu nhất cho EC2, gắn instance family + Region)
Lambda bursty ─► Compute Savings Plan       (chỉ cam kết mức baseline dự đoán được)
MemoryDB     ──► Reserved nodes             (giảm giá theo node type + Region)
```

- **EC2 Instance Savings Plan:** giảm tới 72% so với On-Demand (theo TD) khi cam kết một instance family trong một Region. Workload EC2 ổn định thì cam kết này an toàn.
- **Compute Savings Plan cho Lambda:** áp dụng cho Lambda (cùng Fargate, EC2). Vì Lambda bursty, chỉ cam kết phần baseline có thể dự báo, tránh cam kết dư.
- **MemoryDB reserved nodes:** reserved node không phải node vật lý mà là giảm giá billing áp lên On-Demand node, gắn với node type và Region.

#### Vì sao C (đáp án Anh chọn) sai

C có hai điểm yếu:

1. **Compute Savings Plan không phủ MemoryDB.** Savings Plans chỉ cho compute (EC2, Fargate, Lambda). MemoryDB dùng reserved nodes. Dù vậy C vẫn nhắc reserved nodes ở cuối, nên lỗi chính nằm ở điểm 2.
2. **Dùng Compute SP cho EC2 bỏ lỡ mức giảm sâu hơn.** Compute SP linh hoạt nhưng mức giảm thấp hơn (TD nêu tới 66% so với 72% của EC2 Instance SP). Workload EC2 đã ổn định, không cần sự linh hoạt đó, nên "để tiền trên bàn".

Thêm nữa, **Lambda reserved concurrency không tiết kiệm tiền**, nó chỉ đảm bảo/giới hạn concurrency.

Với C, cả câu mô tả "một cam kết cho EC2, Lambda và MemoryDB" là sai ngay từ đầu vì Compute SP không đụng tới MemoryDB.

#### Các option còn lại

- **B (On-Demand hết):** đắt nhất, trái mục tiêu giảm chi phí. Lambda provisioned concurrency còn tăng chi phí. Auto scaling không thay thế được cam kết khi EC2 ổn định.
- **D (Spot + On-Demand Lambda + thay MemoryDB bằng ElastiCache):** Spot có thể bị thu hồi bất cứ lúc nào, không hợp dịch vụ luôn bật như matchmaking/leaderboard. Lambda On-Demand là trả giá đầy đủ. Thay MemoryDB bằng ElastiCache làm mất độ bền và multi-AZ replication mà game real-time thường cần.

#### Bảng chọn mô hình mua theo service

| Service | Mô hình giảm giá | Ghi chú |
|---|---|---|
| EC2 ổn định | **EC2 Instance Savings Plan** | Gắn instance family + Region, giảm sâu nhất |
| EC2 cần linh hoạt family/Region | Compute Savings Plan | Giảm thấp hơn, linh hoạt hơn |
| Lambda | **Compute Savings Plan** | Chỉ cam kết baseline |
| MemoryDB / ElastiCache / RDS | **Reserved nodes (RI)** | Savings Plans không áp dụng |

#### Quy tắc nhớ cho thi

- **Thấy "EC2 steady, predictable"** → **EC2 Instance Savings Plan**
- **Thấy "Lambda / Fargate" muốn giảm giá** → **Compute Savings Plan** (chỉ phủ baseline)
- **Thấy MemoryDB / ElastiCache / RDS / Redshift** → **Reserved nodes**, không phải Savings Plans
- **"Reserved concurrency"** là kiểm soát concurrency, không phải công cụ tiết kiệm chi phí
- **Savings Plans = compute (EC2, Fargate, Lambda)**; database/cache dùng reserved node

### TD explanation

Savings Plans provide savings beyond On-Demand rates in exchange for a commitment to using a specified amount of compute power (measured per hour) for one or three years. Savings Plans offer a flexible pricing model that provides savings on AWS usage. You can save up to 72 percent on your AWS compute workloads.
EC2 Instance Savings Plans provide savings up to 72 percent off On-Demand, in exchange for a commitment to a specific instance family in a chosen AWS Region (for example, m5 in Virginia).
Compute Savings Plans provide the most flexibility and prices up to 66 percent off of On-Demand rates. These plans automatically apply to your EC2 instance usage, regardless of instance family (for example, m5, c5, etc.), instance size (for example, c5.large, c5.xlarge, etc.), Region (for example, us-east-1, us-east-2, etc.), operating system (for example, Windows, Linux, etc.), or tenancy (for example, Dedicated, default, Dedicated Host). They also apply to your Fargate and Lambda usage.
MemoryDB Reserved nodes, on the other hand, provide you with a significant discount compared to On-Demand node pricing. Reserved nodes are not physical nodes but a billing discount applied to using On-Demand nodes in your account. Discounts for reserved nodes are tied to node type and AWS Region.

Since the EC2 instances handle consistent and predictable workloads like matchmaking and leaderboards, committing to an EC2 instance Savings Plan is the most economical approach, as it offers the highest discount specifically for EC2 usage. The Lambda functions, which respond to bursty and inconsistent traffic patterns, should be covered using a Compute Savings Plan, but only up to the minimum baseline usage that can be forecasted. This configuration still allows cost savings without overcommitting. Finally, MemoryDB cache nodes, part of a caching layer with stable demand, are best supported through reserved nodes, ensuring provisioned capacity at a reduced cost compared to On-Demand.
This combination of service-specific purchase models aligns well with the application’s usage patterns, optimizing spending without compromising performance.
Hence, the correct answer is: Use an EC2 instance Savings Plan to commit to the EC2 compute resources financially. Apply a Compute Savings Plan to offset the baseline utilization of Lambda functions. Allocate reserved nodes to provision capacity for the MemoryDB cache nodes.
The option that says: Use a Compute Savings Plan to cover EC2, Lambda, and MemoryDB usage in a single commitment. Configure Lambda reserved concurrency to manage unpredictable workloads. Provision MemoryDB cache nodes by acquiring reserved nodes to ensure dedicated capacity is incorrect. This option is tempting at first glance because it offers a consolidated Compute Savings Plan, but this plan only gives moderate discounts. It does not take full advantage of workload predictability. EC2 instance Savings Plans offer deeper savings for EC2 workloads, so relying on Compute Savings Plans across all three services simply leaves potential savings on the table. Additionally, configuring Lambda reserved concurrency does not save money; it just reserves capacity. The answer also correctly suggests reserved nodes for MemoryDB, but this partial correctness isn’t enough to make it the best solution.
The option that says: Use EC2 Spot Instances to reduce compute costs for matchmaking and leaderboard services. Use On-Demand Lambda execution. Replace MemoryDB with Amazon ElastiCache is incorrect. This option makes several risky trade-offs in the name of savings, but they are inappropriate for the scenario. EC2 Spot Instances are not recommended for critical, always-on services like matchmaking or leaderboards because Spot capacity can be interrupted anytime. Using On-Demand Lambda means you’re just paying full price with no cost optimization, and replacing MemoryDB with ElastiCache is misleading. While ElastiCache is a Redis-compatible caching service, it lacks the high durability and multi-AZ replication features of MemoryDB, which are often essential in real-time gaming environments.
The option that says: Leverage On-Demand pricing across all services to maintain flexibility. Use Lambda provisioned concurrency for better performance. Rely on auto-scaling EC2 instances instead of committing to Savings Plans is incorrect. This option sacrifices cost savings entirely in the name of flexibility, which directly contradicts the goal of minimizing monthly expenses. Relying on On-Demand pricing across all services is simply the most expensive route. Using Lambda provisioned concurrency adds cost without addressing the variable, event-driven nature of Lambda workloads. Lastly, just depending on EC2 auto-scaling does not remove the need for committing to Savings Plans, especially when the EC2 usage is described as stable and predictable. This option misses the opportunity to optimize spend where it clearly could be.

References:
https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html
https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reservednodes.html

Check out this AWS Savings Plan Cheat Sheet:
https://tutorialsdojo.com/aws-savings-plan/

</details>

---

# Group B — Governance & security tooling scope (2)

<a id="q6"></a>

## Q6

A financial institution is running multiple AWS Lambda functions. These functions are packaged as .zip archives and rely on a shared Lambda layer that contains common libraries.
Security compliance requires that the development team must:


Continuously monitor the Lambda functions and the shared Lambda layer for current common vulnerabilities and exposures (CVEs).


Perform additional automated code scans on a subset of Lambda functions to detect data leaks and injection flaws.


Ensure that not all Lambda functions are scanned for code issues, since some workloads handle non-sensitive test data.


The company wants a fully managed AWS-native solution to meet these requirements.


Which of the following will meet the given requirements? (Select THREE.)

- **A.** Apply an Amazon Inspector exclusion tag with a key of InspectorCodeExclusion and a value of LambdaCodeScanning to Lambda functions that should not be code-scanned.
- **B.** Enable Amazon Inspector Lambda code scanning to detect code-level vulnerabilities.
- **C.** Use AWS IAM policies to restrict Amazon Inspector from scanning specific Lambda functions.
- **D.** Use Amazon GuardDuty Lambda Protection to monitor for CVEs and data leaks.
- **E.** Enable AWS Config with a custom rule to check Lambda deployment packages for CVEs.
- **F.** Enable Amazon Inspector and activate Lambda standard scanning for CVE detection.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B, F · **You picked:** A, B, C

🔑 **Key words:** CVEs in functions + layers, code scans on a subset only

🪤 **Your trap:** A+B right; IAM (C) isn't how you exclude Inspector targets; missed standard scanning (F) for CVEs

🧠 **Rule:** Inspector Lambda = standard scan (CVEs) + code scan (code flaws) + InspectorCodeExclusion tag

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Lambda functions (.zip) + shared Lambda layer
        │
        ├─ (1) Quét CVE liên tục: functions + layer       ──► Inspector standard scanning
        ├─ (2) Quét code: data leak, injection flaw       ──► Inspector code scanning
        └─ (3) Chỉ một TẬP CON function bị quét code      ──► tag loại trừ
                (function test data không nhạy cảm bỏ qua)
Yêu cầu: fully managed, AWS-native, chọn 3 đáp án
```

Đáp án đúng: **A, B, F**. Anh chọn **A, B, C**. Tức là hai đáp án đầu đúng, nhưng **C sai** và **bỏ sót F**.

#### Ba lựa chọn đúng ghép thành một giải pháp

Ba đáp án phải ghép thành MỘT luồng, mỗi mảnh đáp ứng một yêu cầu:

```
F: bật Inspector + Lambda standard scanning
        └─► quét dependency/package trong functions VÀ layers (CVE)  [yêu cầu 1]
B: bật Lambda code scanning
        └─► phân tích code tìm injection, data leak                   [yêu cầu 2]
        (điều kiện: phải bật standard scanning trước)
A: gắn tag InspectorCodeExclusion = LambdaCodeScanning
        └─► function nào có tag thì bị loại khỏi code scan            [yêu cầu 3]
```

- **F (standard scanning):** là loại scan mặc định của Lambda, quét lỗ hổng package/dependency trong function và layer. Đây là phần đáp ứng yêu cầu "monitor CVE liên tục cho cả function và shared layer".
- **B (code scanning):** quét code tùy chỉnh để tìm lỗi code như injection và data leak. Theo TD, muốn bật code scanning thì **phải bật standard scanning trước**. Vì vậy B không đứng được nếu thiếu F.
- **A (exclusion tag):** key `InspectorCodeExclusion`, value `LambdaCodeScanning`. Gắn lên function không nhạy cảm để chúng không bị code scan, đáp ứng "không phải function nào cũng bị quét code".

#### Pick của Anh sai ở đâu: C thay cho F

**Anh đã chọn đúng A và B**, nhưng chọn C thay vì F.

**C sai: IAM policy không phải cách loại trừ target của Inspector.** Phạm vi quét ở mức function được điều khiển bằng **tag** (exclusion tag), không phải bằng IAM policy. Anh nhầm "hạn chế/quyền truy cập" với "phạm vi quét". Mà yêu cầu 3 đã được A giải quyết bằng tag rồi, nên C vừa sai cơ chế vừa thừa.

**Hệ quả:** vì dùng một slot cho C, Anh bỏ lỡ F. Thiếu F nghĩa là không có standard scanning cho CVE. Lúc đó yêu cầu 1 không đáp ứng, và B cũng phụ thuộc vào F nên cả chuỗi bị vỡ.

Mẹo khi multi-select: sau khi chọn, hãy đối chiếu **từng yêu cầu của đề với một đáp án**. Yêu cầu CVE chưa có ai phụ trách thì chưa đủ.

#### Hai option sai còn lại

- **D (GuardDuty Lambda Protection):** tập trung phát hiện **mối đe dọa lúc runtime** và hành vi bất thường, không quét CVE trong package hay lỗi code tĩnh.
- **E (AWS Config + custom rule kiểm tra CVE):** Config theo dõi thay đổi cấu hình và compliance, không phải công cụ quét lỗ hổng. Muốn quét CVE bằng Config phải tự dựng logic hoặc công cụ ngoài, không còn "fully managed".

#### Bảng chọn service

| Nhu cầu | Service / tính năng | Đúng/Sai |
|---|---|---|
| CVE trong function + layer | Inspector Lambda **standard scanning** (F) | Đúng |
| Lỗi code: injection, data leak | Inspector Lambda **code scanning** (B) | Đúng |
| Loại function khỏi code scan | Tag **InspectorCodeExclusion** (A) | Đúng |
| Loại trừ bằng IAM policy (C) | Không phải cơ chế của Inspector | Sai |
| Runtime threat | GuardDuty Lambda Protection (D) | Không phải CVE/code scan |
| Config rule quét CVE (E) | Config không quét lỗ hổng | Sai |

#### Quy tắc nhớ cho thi

- **Thấy "CVE trong Lambda function và layer"** → **Inspector Lambda standard scanning**
- **Thấy "lỗi code, injection, data leak trong Lambda"** → **Inspector Lambda code scanning** (phải bật standard trước)
- **Thấy "loại function khỏi code scan"** → tag **InspectorCodeExclusion = LambdaCodeScanning**, không dùng IAM
- **GuardDuty** = runtime threat; **Config** = cấu hình/compliance; **Inspector** = vulnerability scanning
- **Multi-select:** mỗi yêu cầu trong đề phải có đúng một đáp án phụ trách, kiểm tra trước khi nộp

### TD explanation

Amazon Inspector is a vulnerability management service that automatically identifies workloads and continuously scans them for software vulnerabilities and unintended network exposure. It can discover and scan Amazon EC2 instances, container images in Amazon ECR, and Lambda functions. When Amazon Inspector detects a software vulnerability or unintended network exposure, it generates a finding—a detailed report that outlines the issue. You can manage these findings through the Amazon Inspector console or API.
Amazon Inspector supports security vulnerability assessments for AWS Lambda functions and layers, providing continuous automated scanning. It offers two types of scanning for Lambda functions:
– Amazon Inspector Lambda standard scanning – This scan type is the default Lambda scan type. It scans application dependencies in Lambda functions and layers for package vulnerabilities.
– Amazon Inspector Lambda code scanning – This scan type scans custom application code in your Lambda functions and layers for code vulnerabilities. You can activate Lambda standard scanning or Lambda standard scanning with Lambda code scanning.
If you want to activate Lambda code scanning, you must first enable standard scanning.

You can add tags to Lambda functions to exclude them from Amazon Inspector’s Lambda code scans. Excluding functions from scans can help prevent receiving unactionable alerts. To tag a function for exclusion, use the following key-value pair for the tag.
– Key – InspectorCodeExclusion
– Value – LambdaCodeScanning
Hence, the correct answers are:
– Enable Amazon Inspector and activate Lambda standard scanning for CVE detection. It enables continuous, automated scanning of Lambda function deployment packages and layers for known vulnerabilities (CVEs).
– Enable Amazon Inspector Lambda code scanning to detect code-level vulnerabilities. It allows Amazon Inspector to perform static code analysis on Lambda functions to detect issues like injection flaws and data leaks. This meets the requirement for automated code scans on a subset of functions handling sensitive data.
– Apply an Amazon Inspector exclusion tag with a key of InspectorCodeExclusion and a value of LambdaCodeScanning to Lambda functions that should not be code-scanned. It provides a native way to exclude specific Lambda functions from code scanning. This ensures that functions handling non-sensitive test data are not unnecessarily scanned, aligning with the compliance requirement.
The option that says: Enable AWS Config with a custom rule to check Lambda deployment packages for CVEs is incorrect because AWS Config does not primarily support vulnerability scanning. While it can track configuration changes and compliance, it cannot inspect Lambda packages for CVEs without external tooling or custom logic.
The option that says: Use Amazon GuardDuty Lambda Protection to monitor for CVEs and data leaks is incorrect because GuardDuty focuses on detecting runtime threats and anomalous behavior, not static vulnerabilities like CVEs or code-level flaws. It does not scan deployment packages or source code for vulnerabilities.
The option that says: Use AWS IAM policies to restrict Amazon Inspector from scanning specific Lambda functions is incorrect because Amazon Inspector does not use IAM policies to control scanning scope at the function level. Instead, it typically relies on tagging mechanisms for exclusions.

References:
https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html
https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html
https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_code_exclude_functions.html

Check out this Amazon Inspector Cheat Sheet:
https://tutorialsdojo.com/amazon-inspector/

</details>

<a id="q15"></a>

## Q15

A global enterprise manages multiple AWS accounts under a single organization using AWS Organizations. The enterprise leverages AWS CloudFormation to automate infrastructure provisioning and centrally manages permissions and roles using AWS Identity and Access Management (IAM).
As part of a new chargeback model, the finance department requires each department to apply project tags selected from a predefined list of tag values to every newly created resource.
When analyzing spending using the AWS Cost and Usage Report in AWS Cost Explorer, the finance team identified non-compliant tag values that disrupted cost attribution.
To enforce compliance, the company needs a scalable way to validate and implement resource tagging based on these project values.
Which approach offers the easiest and most effective way to enforce this?

- **A.** Enable resource tagging enforcement using AWS Config rules. Integrate the rules with Organizations to evaluate tag compliance across accounts. Use automation documents to prevent cloudformation:CreateStack unless tags meet policy requirements.
- **B.** In the organization’s management account, define a tag policy with valid project tag values. Then, create a Service Control Policy (SCP) to deny cloudformation:CreateStack except if the required project tag is included. Attach the created SCP to the root of the organization.
- **C.** Configure a tag policy in the Organizations management account to specify the approved project tag values. Then, implement an SCP that blocks the cloudformation:DetectStackResourceDrift operation unless a compliant project tag is part of the request. Apply this SCP at the organization’s root level.
- **D.** Use the AWS Tag Editor to audit and correct resource tags across all accounts. Schedule periodic reviews to identify non-compliant tags and update them to match the predefined project tag list

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** ENFORCE approved project tag values on new resources, org-wide

🪤 **Your trap:** Config + automation detects after creation; can't block CreateStack

🧠 **Rule:** Enforce at creation → tag policy (allowed values) + SCP denying cloudformation:CreateStack without the tag

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations (nhiều account) + CloudFormation
        │
Finance: mỗi tài nguyên MỚI phải có tag "project" với giá trị
         thuộc danh sách cho phép (chargeback)
        │
Hiện trạng: Cost Explorer thấy giá trị tag sai -> sai phân bổ chi phí
Yêu cầu: ENFORCE (ép buộc), scalable, dễ nhất, toàn org
```

Từ khóa quyết định: **"enforce"** + **"newly created resource"** + **"organization-wide"**. Đáp án đúng: **B (tag policy + SCP deny cloudformation:CreateStack nếu thiếu tag)**. Anh chọn A (AWS Config).

#### Vì sao B đúng: hai lớp làm hai việc khác nhau

```
Tag policy (Organizations)
   └─► định nghĩa chuẩn: key "project" + danh sách giá trị hợp lệ
       (governance: định nghĩa chuẩn, báo cáo non-compliance)
SCP trên root
   └─► Deny cloudformation:CreateStack nếu request KHÔNG có tag project
       (enforcement: chặn ngay tại thời điểm tạo)
```

- Theo TD, **tag policy tự nó không ép buộc** việc phải gắn tag, nó chuẩn hóa giá trị và cho visibility về compliance.
- **SCP** là cơ chế ép buộc: chặn hành động bất kể IAM permission của user. Deny `cloudformation:CreateStack` khi thiếu tag nghĩa là stack không tạo được nếu không có tag đúng yêu cầu.
- Gắn SCP ở **root** của org thì phủ mọi account, đáp ứng "scalable".

#### Vì sao A (Config + automation) sai

Anh nhìn thấy "AWS Config + tích hợp Organizations + automation" và thấy đủ cho "validate". Nhưng:

- **AWS Config đánh giá SAU khi tài nguyên đã được tạo.** Nó không chặn được API call như `cloudformation:CreateStack`.
- **Automation document (SSM)** có thể remediate hoặc thông báo, nhưng không chặn việc tạo stack theo thời gian thực.
- Vậy tài nguyên vi phạm vẫn được launch, trái yêu cầu "enforce at creation".

Câu cuối trong A nói "dùng automation documents để prevent CreateStack" nghe như chặn được, nhưng thực tế cơ chế đó chỉ phản ứng sau, không phải chặn trước.

#### Hai option còn lại

- **C (SCP deny `cloudformation:DetectStackResourceDrift`):** sai API. DetectStackResourceDrift dùng để chẩn đoán drift, không tạo, sửa hay gắn tag tài nguyên. Chặn nó không ngăn việc triển khai tài nguyên thiếu tag.
- **D (Tag Editor + review định kỳ):** Tag Editor chỉ tìm và sửa tag thủ công, không có cơ chế ép buộc hay kiểm tra theo danh sách giá trị. Tốn công vận hành, dễ sai sót, và không tích hợp với tag policy/SCP.

#### Khi nào detect-after (Config) lại là đáp án đúng?

Đây là chỗ dễ nhầm giữa hai kiểu đề:

| Dấu hiệu trong stem | Hướng đúng |
|---|---|
| "**enforce** / **prevent** / **must not be created** without tag" | **Preventive**: SCP (kèm tag policy) |
| "**do not block / không cản trở developers**", "**audit**", "**detect and report/remediate**" | **Detective**: AWS Config (rule + remediation) |
| Chỉ cần "chuẩn hóa giá trị tag, xem báo cáo" | Tag policy |

Các đề nói rõ "không được chặn developer" hoặc chỉ cần phát hiện/báo cáo thì Config thắng, vì SCP deny sẽ cản công việc. Đề này nói "enforce" cho tài nguyên mới nên preventive control (SCP) thắng.

📝 Ghi chú kỹ thuật: ngoài đời, tag policy có thể bật enforcement cho một số loại resource nhất định, nhưng không phải tất cả. Theo đúng đáp án đề, hãy nhớ bộ đôi "tag policy (giá trị hợp lệ) + SCP (chặn thiếu tag)".

#### Quy tắc nhớ cho thi

- **Thấy "enforce tag at creation, org-wide"** → **Tag policy + SCP deny khi thiếu tag**
- **Thấy "detect / audit / không chặn developer"** → **AWS Config** (rule + remediation)
- **Config** = đánh giá sau khi tạo, không chặn API; **SCP** = chặn trước, bất kể IAM
- **Tag policy** = định nghĩa chuẩn giá trị; **SCP** = ép buộc có tag
- Đọc kỹ **API bị deny** trong SCP: phải là hành động tạo tài nguyên (`CreateStack`), không phải hành động chẩn đoán (`DetectStackResourceDrift`)

### TD explanation

Defining a tag policy in the AWS Organizations management account ensures all accounts have standardized approved project tag values. Although tag policies alone cannot enforce tag usage, they enable visibility into tag compliance across the organization.
Enforcing tag compliance, on the other hand, is effectively handled using a Service Control Policy (SCP) that denies the cloudformation:CreateStack operation unless a required project tag is included.
AWS separates governance from enforcement to provide organizations with flexibility, gradual adoption, and control over how policies are introduced and applied across accounts. Regarding tag policies within AWS Organizations, governance tools are designed to define standards, guide behavior, and report compliance without immediately disrupting workflows. This allows organizations to monitor tagging hygiene, educate teams, and identify non-compliant patterns before applying hard restrictions. In contrast, Service Control Policies (SCPs) are enforcement mechanisms that strictly prevent specific actions, such as creating resources without required tags, regardless of IAM permissions. By separating these functions, AWS enables a phased approach: organizations can start with visibility and alignment through governance and then escalate to enforcement when ready, reducing the risk of unintended disruptions while improving long-term operational consistency.

A combination of Organization Tag Policy and SCPs uses a combined governance and enforcement approach that meets the question’s scalability, compliance, and effectiveness requirements.
Hence, the correct answer is: In the organization’s management account, define a tag policy with valid project tag values. Then, create a Service Control Policy (SCP) to deny cloudformation:CreateStack except if the required project tag is included. Attach the created SCP to the root of the organization.
The option that says: Enable resource tagging enforcement using AWS Config rules. Integrate the rules with Organizations to evaluate tag compliance across accounts. Use automation documents to prevent cloudformation:CreateStack unless tags meet policy requirements is incorrect. AWS Config rules operate after resource creation and do not natively prevent API actions like cloudformation:CreateStack. While integrating AWS Config with AWS Organizations enables centralized tag compliance checks, it only provides post-creation evaluation. Automation documents (SSM documents) can remediate or notify but cannot block the initial stack creation in real-time. As a result, non-compliant resources can still be launched, violating the requirement to enforce tagging at creation.
The option that says: Configure a tag policy in the Organizations management account to specify the approved project tag values. Then, implement an SCP that blocks the cloudformation:DetectStackResourceDrift operation unless a compliant project tag is part of the request. Apply this SCP at the organization’s root level is incorrect. It targets an API operation unrelated to resource creation where tag enforcement must occur. While defining a tag policy in the AWS Organizations management account helps establish governance, denying cloudformation:DetectStackResourceDrift is ineffective. This action is used for diagnostics and does not create, modify, or tag resources. Blocking it does nothing to prevent the deployment of resources with invalid or missing tags.
The option that says: Use the AWS Tag Editor to audit and correct resource tags across all accounts. Schedule periodic reviews to identify non-compliant tags and update them to match the predefined project tag list is incorrect. While AWS Tag Editor can be used to search and edit tags across multiple accounts and regions, it does not provide any mechanism for enforcement. It cannot block resource creation or validate tag values against a predefined list. It only allows administrators to inspect and modify tags manually after the fact. Also, relying on scheduled manual reviews introduces operational overhead, delays in enforcement, and a high risk of human error or oversight. Finally, although Tag Editor supports visibility, it offers no integration with AWS Organizations governance policies like tag policies or SCPs, and it does not prevent the use of non-compliant project tags during provisioning.

References:
https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html

Check out this AWS Organizations Cheat Sheet:
https://tutorialsdojo.com/aws-organizations/

</details>
