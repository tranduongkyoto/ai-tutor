# Udemy Test #2 — unseen questions (Gate 1) — Wrong Answer Review (14 questions)

Source: `udemy2_unseen_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `udemy2_unseen_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q1](#q1) | ✅ 10-08 | ✅ 10-12 | ☐ |
| A | [Q6](#q6) | ✅ 10-08 | ✅ 10-12 | ☐ |
| A | [Q8](#q8) | ✅ 10-08 | ✅ 10-12 | ☐ |
| A | [Q13](#q13) | ✅ 10-08 | ✅ 10-12 | ☐ |
| B | [Q4](#q4) | ✅ 10-08 | ✅ 10-12 | ☐ |
| B | [Q15](#q15) | ✅ 10-08 | ✅ 10-12 | ☐ |
| C | [Q9](#q9) | ✅ 10-08 | ✅ 10-12 | ☐ |
| C | [Q22](#q22) | ✅ 10-08 | ✅ 10-12 | ☐ |
| C | [Q26](#q26) | ✅ 10-08 | ✅ 10-12 | ☐ |
| D | [Q12](#q12) | ✅ 10-08 | ✅ 10-12 | ☐ |
| D | [Q20](#q20) | ✅ 10-08 | ✅ 10-12 | ☐ |
| D | [Q21](#q21) | ✅ 10-08 | ✅ 10-12 | ☐ |
| D | [Q24](#q24) | ✅ 10-08 | ✅ 10-12 | ☐ |
| D | [Q27](#q27) | ✅ 10-08 | ✅ 10-12 | ☐ |

---

# Group A — Kinesis family & streaming destinations (4)

<a id="q1"></a>

## Q1

An Internet-of-Things (IoT) company is using Kinesis Data Streams (KDS) to process IoT data from field devices. Multiple consumer applications are using the incoming data streams and the engineers have noticed a performance lag for the data delivery speed between producers and consumers of the data streams.

As a Solutions Architect Professional, which of the following would you recommend to improve the performance for the given use-case?

- **A.** Swap out Kinesis Data Streams with SQS FIFO queues to support the desired read throughput for the downstream applications
- **B.** Swap out Kinesis Data Streams with Kinesis Data Firehose to support the desired read throughput for the downstream applications
- **C.** Swap out Kinesis Data Streams with SQS Standard queues to support the desired read throughput for the downstream applications
- **D.** Use Enhanced Fanout feature of Kinesis Data Streams to support the desired read throughput for the downstream applications

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** multiple consumer apps + read lag on KDS

🪤 **Your trap:** Firehose is a delivery service to S3/Redshift/OpenSearch — consumer apps can't read from it

🧠 **Rule:** Many KDS consumers lagging → Enhanced Fan-Out (dedicated 2 MB/s/shard per consumer)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Producers (IoT devices) ──► Kinesis Data Streams (KDS) ──► Nhiều consumer apps
                                     │
                         Mặc định: 2MB/s/shard CHIA SẺ
                         cho TẤT CẢ consumer app đọc cùng shard
                                     │
                         Nhiều app cùng đọc → tranh băng thông
                         → lag ở phía đọc (read throughput)
```

Yêu cầu: cải thiện **tốc độ đọc** khi nhiều consumer app cùng đọc từ KDS. Đáp án đúng: **D (Enhanced Fan-Out)**. Anh chọn **B (đổi sang Kinesis Data Firehose)** — sai hướng.

#### D đúng — Enhanced Fan-Out giải quyết đúng nút nghẽn

Theo mặc định, mỗi shard của KDS chỉ cấp **2MB/s output** và băng thông này **bị chia sẻ** giữa mọi consumer app đang đọc shard đó — nhiều app cùng đọc thì mỗi app chỉ được một phần nhỏ, gây lag.

**Enhanced Fan-Out (EFO)** cho mỗi consumer đã đăng ký một **đường ống 2MB/s/shard riêng**, tự scale theo số shard. Tức là:

```
Shard ──► Consumer A: 2MB/s riêng
      ──► Consumer B: 2MB/s riêng
      ──► Consumer C: 2MB/s riêng
(không chia sẻ, không tranh băng thông lẫn nhau)
```

Đây đúng là nguyên nhân performance lag trong đề: nhiều consumer app, cùng đọc chung — EFO xử lý chính xác vấn đề này mà không cần đổi service.

#### Vì sao B (Firehose) sai

**Firehose không phải là nơi consumer app đọc được.** Firehose là dịch vụ **delivery/giao hàng một chiều** — nó chỉ ghi dữ liệu xuống S3, Redshift, OpenSearch (Elasticsearch) hoặc Splunk. Không có API cho "nhiều app cùng đọc" từ Firehose như cách consumer app đọc từ KDS qua KCL/GetRecords.

⚠️ **Lỗi lặp lại** — đây là lỗi anh hay mắc: nhầm Firehose (destination service, một chiều, auto-scale, không có khái niệm "consumer đọc lại") với KDS (giữ dữ liệu trong shard, nhiều consumer đọc/replay được).

#### Các option sai khác

- **A, C (SQS FIFO / SQS Standard):** SQS là hàng đợi — khi một consumer nhận message, message đó biến mất khỏi queue (trừ khi dùng nhiều queue riêng). Không hỗ trợ nhiều app đọc **cùng** một message đồng thời như KDS.

#### So sánh nhanh: KDS vs Firehose vs SQS vs Enhanced Fan-Out

| Dịch vụ | Vai trò | Nhiều consumer đọc cùng dữ liệu? | Băng thông đọc |
|---|---|---|---|
| **Kinesis Data Streams (KDS)** | Stream lưu trữ tạm (giữ data 24h–365 ngày), cho phép đọc/replay | Có — mỗi app đọc độc lập, không xóa dữ liệu của app khác | 2MB/s/shard chia sẻ cho mọi consumer |
| **Enhanced Fan-Out (tính năng của KDS)** | Nâng cấp đọc của KDS, không phải service riêng | Có, và mỗi consumer được băng thông riêng | 2MB/s/shard **riêng cho từng consumer** |
| **Kinesis Data Firehose** | Dịch vụ giao dữ liệu một chiều tới S3/Redshift/OpenSearch/Splunk | Không — không có API cho app đọc lại | Không áp dụng (không phải nơi đọc) |
| **Amazon SQS** | Hàng đợi message, decouple microservices | Không — 1 message chỉ được 1 consumer xử lý (trừ fan-out qua SNS) | N/A, theo throughput queue |

#### Lưu ý thực tế

- EFO là tính năng **bật thêm trên KDS**, không phải phải đổi sang service khác — đây là "chi phí thấp nhất, thay đổi kiến trúc ít nhất" nên exam thường ưu tiên.
- Muốn fan-out thật sự kiểu "1 message nhiều consumer" với SQS thì phải kết hợp **SNS + nhiều SQS queue**, không dùng SQS đơn lẻ.

#### Quy tắc nhớ cho thi

- **Nhiều consumer app đọc cùng KDS bị lag** → **Enhanced Fan-Out**, không phải đổi service
- **Thấy "Firehose" và "consumer app đọc lại"** → luôn SAI, Firehose chỉ ghi ra đích cố định
- **Thấy "SQS" cho nhiều app đọc cùng dữ liệu đồng thời** → SAI trừ khi có SNS fan-out
- **KDS = đọc được nhiều lần, nhiều app, có replay; Firehose = ghi một lần, một chiều, auto-scale**

### TD explanation

Correct option:

Use Enhanced Fanout feature of Kinesis Data Streams to support the desired read throughput for the downstream applications

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. By default, the 2MB/second/shard output is shared between all of the applications consuming data from the stream.

You should use enhanced fan-out if you have multiple consumers retrieving data from a stream in parallel. With enhanced fan-out developers can register stream consumers to use enhanced fan-out and receive their own 2MB/second pipe of read throughput per shard, and this throughput automatically scales with the number of shards in a stream.

via - https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

via - https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

Incorrect options:

Swap out Kinesis Data Streams with Kinesis Data Firehose to support the desired read throughput for the downstream applications -  Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security. Kinesis Data Firehose can only write to S3, Redshift, Elasticsearch or Splunk. You can't have applications consuming data streams from Kinesis Data Firehose, that's the job of Kinesis Data Streams. Therefore this option is not correct.

Swap out Kinesis Data Streams with SQS Standard queues to support the desired read throughput for the downstream applications

Swap out Kinesis Data Streams with SQS FIFO queues to support the desired read throughput for the downstream applications

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent. As multiple applications are consuming the same stream concurrently, both SQS Standard and SQS FIFO are not the right fit for the given use-case.

via - https://aws.amazon.com/kinesis/data-streams/faqs/

References:

https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

https://aws.amazon.com/kinesis/data-streams/faqs/

</details>

<a id="q6"></a>

## Q6

A leading internet television network company uses AWS Cloud for analytics, recommendation engines and video transcoding. To monitor and optimize this network, the engineering team at the company has developed a solution for ingesting, augmenting, and analyzing the multiple terabytes of data its network generates daily in the form of virtual private cloud (VPC) flow logs. This would enable the company to identify performance-improvement opportunities such as identifying apps that are communicating across regions and collocating them. The VPC flow logs data is funneled into Kinesis Data Streams which further acts as the source of a delivery stream for Kinesis Firehose. The engineering team has now configured a Kinesis Agent to send the VPC flow logs data from another set of network devices to the same Firehose delivery stream. They noticed that data is not reaching Firehose as expected.

As a Solutions Architect Professional, which of the following options would you identify as the MOST plausible root cause behind this issue?

- **A.** Kinesis Firehose delivery stream has reached its limit and needs to be scaled manually
- **B.** The data sent by Kinesis Agent is lost because of a configuration error
- **C.** Kinesis Agent cannot write to a Kinesis Firehose for which the delivery stream source is already set as Kinesis Data Streams
- **D.** Kinesis Agent can only write to Kinesis Data Streams, not to Kinesis Firehose

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** Firehose source already = Kinesis Data Streams; Agent writes to same Firehose

🪤 **Your trap:** Kinesis Agent CAN write to both KDS and Firehose

🧠 **Rule:** KDS as Firehose source disables Firehose PutRecord/PutRecordBatch → producers must write to the KDS

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC flow logs ──► Kinesis Data Streams (KDS) ──► nguồn (source) của ──► Firehose delivery stream
                                                                              ▲
Network devices khác ──► Kinesis Agent ───────────────────────── (ghi trực tiếp, KHÔNG được) ──┘
```

Khi Firehose delivery stream đã được cấu hình **source = Kinesis Data Streams**, thì API `PutRecord`/`PutRecordBatch` của chính Firehose đó **bị tắt**. Kinesis Agent cố ghi trực tiếp vào Firehose → thất bại, dữ liệu không tới. Đáp án đúng: **C**. Anh chọn **D (Kinesis Agent chỉ ghi được vào KDS, không ghi được vào Firehose)** — sai.

#### C đúng — vì sao

Khi một Kinesis data stream được set làm **source** của Firehose delivery stream, Firehose chuyển sang chế độ "pull" dữ liệu từ KDS — nó tự kéo record, không nhận record đẩy trực tiếp từ bên ngoài nữa. Do đó `PutRecord`/`PutRecordBatch` của Firehose delivery stream đó bị disable. Mọi producer (kể cả Kinesis Agent) muốn gửi dữ liệu để cuối cùng chảy vào Firehose đó **phải ghi vào chính KDS** bằng `PutRecord`/`PutRecords` của Kinesis Data Streams, không phải gọi API của Firehose.

```
Đúng:  Kinesis Agent ──► KDS.PutRecords ──► KDS ──► Firehose (tự kéo) ──► S3/Redshift/...
Sai:   Kinesis Agent ──► Firehose.PutRecord  (bị disable vì Firehose đã có source = KDS)
```

#### Vì sao D (lựa chọn của anh) sai

**Kinesis Agent vốn ghi được vào CẢ HAI: KDS và Firehose.** Đây là một Java application độc lập, hỗ trợ gửi dữ liệu tới Kinesis Data Streams hoặc Kinesis Data Firehose tùy cấu hình. Đề không nói Agent "chỉ ghi được KDS" — vấn đề là Agent đang nhắm ghi vào **Firehose cụ thể này**, mà Firehose này đã bị khóa input trực tiếp vì có nguồn là KDS.

⚠️ **Lỗi lặp lại** — anh đang lẫn giữa "khả năng chung của Kinesis Agent" (ghi được cả KDS và Firehose) với "trạng thái riêng của một Firehose delivery stream cụ thể" (bị khóa PutRecord khi đã gắn nguồn KDS). Đây cùng nhóm lỗi với Q1/Q8: cần phân biệt rõ vai trò/khả năng của KDS vs Firehose.

#### Các option sai khác

- **A (Firehose cần scale thủ công vì đã đạt limit):** sai vì Firehose là **fully managed, tự động scale** theo throughput, không cần Solutions Architect can thiệp scale tay.
- **B (mất dữ liệu do lỗi config, đáp án "bịa"):** đây là distractor vô căn cứ — đề xác nhận explicit đây là option dựng thêm để gây nhiễu, không có cơ chế kỹ thuật cụ thể nào được nêu.

#### So sánh nhanh: KDS vs Firehose (liên quan tới lỗi hay lặp)

| Khía cạnh | Kinesis Data Streams | Kinesis Data Firehose |
|---|---|---|
| Ai ghi vào | Producer dùng `PutRecord`/`PutRecords` | Nhận record đẩy vào qua `PutRecord`/`PutRecordBatch` — **trừ khi** source = KDS |
| Khi source = KDS | — | API Put bị **disable**, Firehose tự pull từ KDS |
| Kinesis Agent ghi được vào đâu | Có | Có (nhưng không ghi được nếu Firehose đó đã gắn nguồn KDS) |
| Scale | Theo shard, cần quản lý | Tự động, fully managed |

#### Lưu ý thực tế

- Đây là một trường hợp **"gotcha" đặc thù** của Firehose: cấu hình nguồn là KDS sẽ tự động vô hiệu hóa đường ghi trực tiếp — một thiết kế một-chiều để tránh trộn hai nguồn ghi đồng thời vào cùng một delivery stream.
- Muốn thêm nguồn dữ liệu mới (network devices khác) khi Firehose đã gắn KDS, phải đưa nguồn đó **vào KDS trước**, không gửi thẳng tới Firehose.

#### Quy tắc nhớ cho thi

- **Firehose có source = Kinesis Data Streams** → PutRecord/PutRecordBatch của Firehose đó bị khóa
- **Muốn thêm producer mới khi Firehose đã gắn KDS** → producer phải ghi vào KDS, không ghi trực tiếp Firehose
- **"Agent không ghi được vào Firehose" (chung)** → SAI, Agent ghi được cả hai, chỉ sai khi Firehose cụ thể đã khóa input
- **Firehose tự scale, không cần can thiệp tay** → loại các đáp án nói "cần scale manual"

### TD explanation

Correct option:

Kinesis Agent cannot write to a Kinesis Firehose for which the delivery stream source is already set as Kinesis Data Streams

Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

When a Kinesis data stream is configured as the source of a Firehose delivery stream, Firehose’s PutRecord and PutRecordBatch operations are disabled and Kinesis Agent cannot write to Firehose delivery stream directly. Data needs to be added to the Kinesis data stream through the Kinesis Data Streams PutRecord and PutRecords operations instead. Therefore, this option is correct.

Incorrect options:

Kinesis Agent can only write to Kinesis Data Streams, not to Kinesis Firehose - Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Kinesis Data Streams or Kinesis Firehose. So this option is incorrect.

Kinesis Firehose delivery stream has reached its limit and needs to be scaled manually - Kinesis Firehose is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. Therefore this option is not correct.

How Kinesis Firehose works:

via - https://aws.amazon.com/kinesis/data-firehose/

The data sent by Kinesis Agent is lost because of a configuration error - This is a made-up option and has been added as a distractor.

References:

https://aws.amazon.com/kinesis/data-firehose/

https://aws.amazon.com/kinesis/data-firehose/faqs/

</details>

<a id="q8"></a>

## Q8

A leading Internet-of-Things (IoT) solutions company needs to develop a platform that would analyze real-time clickstream events from embedded sensors in consumer electronic devices. The company has hired you as an AWS Certified Solutions Architect Professional to consult the engineering team and develop a solution using the AWS Cloud. The company wants to use clickstream data to perform data science, develop algorithms, and create visualizations and dashboards to support the business stakeholders. Each of these groups would work independently and would need real-time access to this clickstream data for their applications.

Which of the following options would provide a highly available and fault-tolerant solution to capture the clickstream events from the source and also provide a simultaneous feed of the data stream to the downstream applications?

- **A.** Use AWS Kinesis Data Analytics to facilitate multiple applications consume and analyze same streaming data concurrently and independently
- **B.** Use AWS Kinesis Data Firehose to allow applications to consume the same streaming data concurrently and independently
- **C.** Use AWS Kinesis Data Streams to facilitate multiple applications consume same streaming data concurrently and independently
- **D.** Use Amazon SQS to facilitate multiple applications process same streaming data concurrently and independently

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** simultaneous feed, each group independent, real-time

🪤 **Your trap:** SQS: one consumer deletes the message — no fan-out of the same record

🧠 **Rule:** Many apps read the same stream concurrently/replay → Kinesis Data Streams

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Sensors (clickstream) ──► 1 nguồn dữ liệu duy nhất
                                   │
            ┌──────────────────────┼──────────────────────┐
            ▼                      ▼                       ▼
     Data science team      Dashboard/visual team    Algorithm team
     (đọc độc lập)          (đọc độc lập)             (đọc độc lập)

Yêu cầu: CÙNG một stream, NHIỀU nhóm đọc ĐỒNG THỜI và ĐỘC LẬP, real-time,
highly available + fault-tolerant
```

Đáp án đúng: **C (Kinesis Data Streams)**. Anh chọn **D (SQS)** — sai vì SQS không cho nhiều consumer cùng đọc một message.

#### C đúng — vì sao KDS khớp đúng yêu cầu

KDS cung cấp **ordering** và khả năng **đọc/replay cùng một record cho nhiều Kinesis Application khác nhau**, mỗi app dùng Kinesis Client Library (KCL) riêng để xử lý độc lập. Ví dụ chuẩn trong tài liệu AWS: một app cập nhật dashboard real-time, một app khác archive vào Redshift — **cả hai đọc cùng stream, đồng thời, độc lập** — đúng khớp "data science + dashboard + algorithm" trong đề.

```
KDS stream (giữ dữ liệu, không xóa khi 1 app đọc xong)
     ├──► App 1 (data science)   — đọc độc lập
     ├──► App 2 (dashboard)       — đọc độc lập
     └──► App 3 (algorithm team)  — đọc độc lập
```

#### Vì sao D (lựa chọn của anh) sai

**SQS không hỗ trợ nhiều consumer cùng xử lý một message.** Theo thiết kế SQS (cả Standard và FIFO), một message khi đã được một consumer nhận và xử lý (và xóa) thì **không còn** cho consumer khác nhận nữa — đây là mô hình "exactly tới một consumer" chứ không phải "broadcast cho nhiều consumer". Mà đề cần đúng ba nhóm khác nhau **cùng đọc chung dữ liệu** chứ không phải chia việc cho nhiều worker xử lý từng phần.

⚠️ **Lỗi lặp lại** — đây là cùng pattern lỗi với Q1: SQS = decouple/queue việc (1 message → 1 consumer); KDS = stream cho nhiều consumer đọc cùng dữ liệu, độc lập, có thể replay. Anh đang nhầm "nhiều consumer" của SQS (nhiều worker chia việc) với "nhiều consumer" của KDS (nhiều app đọc toàn bộ dữ liệu như nhau).

#### Các option sai khác

- **A (Kinesis Data Analytics):** dùng để **chạy SQL/query phân tích trên streaming data**, không phải dịch vụ để nhiều app "tiêu thụ" dữ liệu gốc đồng thời — nó là tầng xử lý/phân tích, không phải tầng phân phối cho nhiều consumer độc lập.
- **B (Kinesis Data Firehose):** chỉ **load dữ liệu vào đích cố định** (S3, Redshift, OpenSearch, Splunk) — không có khái niệm nhiều ứng dụng tiêu thụ cùng dữ liệu đồng thời từ Firehose.

#### So sánh nhanh: KDS / Firehose / SQS / Kinesis Data Analytics

| Dịch vụ | Vai trò chính | Nhiều consumer cùng đọc TOÀN BỘ dữ liệu, độc lập? |
|---|---|---|
| **Kinesis Data Streams** | Stream real-time, giữ dữ liệu, cho đọc/replay | **Có** — đúng use-case của đề |
| **Kinesis Data Firehose** | Giao dữ liệu một chiều tới S3/Redshift/OpenSearch/Splunk | Không |
| **Kinesis Data Analytics** | Chạy SQL/ứng dụng phân tích trên stream | Không — là tầng xử lý, không phải tầng phân phối |
| **Amazon SQS** | Hàng đợi, decouple, chia việc cho worker | Không — 1 message chỉ 1 consumer nhận |

#### Lưu ý thực tế

- Cụm từ "multiple applications consume same streaming data **concurrently and independently**" trong đề chính là định nghĩa gần nguyên văn của KDS trong FAQ AWS — khi gặp cụm này gần như luôn chọn KDS.
- Muốn "nhiều consumer cùng nhận 1 message" với SQS, phải thêm **SNS fan-out** (SNS → nhiều SQS queue) — SQS đơn lẻ không làm được.

#### Quy tắc nhớ cho thi

- **"Nhiều nhóm/app đọc cùng dữ liệu, đồng thời, độc lập"** → **Kinesis Data Streams**
- **"Chia việc cho nhiều worker xử lý"** → SQS (nhưng mỗi message chỉ 1 worker)
- **"Phân tích SQL trên streaming data"** → Kinesis Data Analytics, không phải nơi lưu/phân phối
- **"Load vào S3/Redshift/OpenSearch/Splunk"** → Kinesis Data Firehose

### TD explanation

Correct option:

Use AWS Kinesis Data Streams to facilitate multiple applications consume the same streaming data concurrently and independently

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.

Amazon Kinesis Data Streams enables real-time processing of streaming big data. It provides ordering of records, as well as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications. The Amazon Kinesis Client Library (KCL) delivers all records for a given partition key to the same record processor, making it easier to build multiple applications reading from the same Amazon Kinesis data stream (for example, to perform counting, aggregation, and filtering).

Amazon Kinesis Data Streams is recommended when you need the ability for multiple applications to consume the same stream concurrently. For example, you have one application that updates a real-time dashboard and another application that archives data to Amazon Redshift. You want both applications to consume data from the same stream concurrently and independently.

KDS provides the ability for multiple applications to consume the same stream concurrently

via - https://aws.amazon.com/kinesis/data-streams/faqs/

Incorrect options:

Use AWS Kinesis Data Firehose to allow applications to consume same streaming data concurrently and independently - Amazon Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security. As Kinesis Data Firehose is used to load streaming data into data stores, therefore this option is incorrect.

Use AWS Kinesis Data Analytics to facilitate multiple applications consume and analyze same streaming data concurrently and independently - Amazon Kinesis Data Analytics is the easiest way to analyze streaming data in real-time.  You can quickly build SQL queries and sophisticated Java applications using built-in templates and operators for common processing functions to organize, transform, aggregate, and analyze data at any scale. Kinesis Data Analytics enables you to easily and quickly build queries and sophisticated streaming applications in three simple steps: setup your streaming data sources, write your queries or streaming applications and set up your destination for processed data. As Kinesis Data Analytics is used to build SQL queries on streaming data, therefore this option is incorrect.

Use Amazon SQS to facilitate multiple applications process same streaming data concurrently and independently - Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent. For SQS, you cannot have the same message being consumed by multiple consumers at the same time, therefore this option is incorrect.

References:

https://aws.amazon.com/kinesis/data-streams/faqs/

https://aws.amazon.com/kinesis/data-firehose/faqs/

https://aws.amazon.com/kinesis/data-analytics/faqs/

</details>

<a id="q13"></a>

## Q13

An e-commerce web application is hosted on Amazon EC2 instances that are fronted by Application Load Balancer (ALB) configured with an Auto Scaling group (ASG). Enhanced security is provided to the ALB by AWS WAF web ACLs. As per the company's security policy, AWS CloudTrail is activated and logs are configured to be stored on Amazon S3 and CloudWatch Logs.

A discount sales offer was run on the application for a week. The support team has noticed that a few of the instances have rebooted taking down the log files and all temporary data with them. Initial analysis has confirmed that the incident took place during off-peak hours. Even though the incident did not cause any sales or revenue loss, the CTO has asked the security team to fix the security error that has allowed the incident to go unnoticed and eventually untraceable.

What steps will you implement to permanently record all traffic coming into the application?

- **A.** To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring
- **B.** Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking
- **C.** Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking
- **D.** Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** permanently record all traffic into WAF-protected ALB

🪤 **Your trap:** CloudTrail is not a WAF log destination

🧠 **Rule:** WAF logs → CloudWatch Logs / S3 / Firehose; Firehose → S3 → Athena for analysis

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internet ──► ALB (được bảo vệ bởi WAF web ACL) ──► ASG ──► EC2
                                                      │
                                            Instance reboot
                                            → mất log file + temp data
                                            → traffic KHÔNG bị ghi lại đầy đủ

CloudTrail (đã bật, log tới S3 + CloudWatch Logs) = ghi API calls, KHÔNG ghi traffic HTTP vào ALB
```

Yêu cầu: **ghi lại VĨNH VIỄN (permanently record) toàn bộ traffic đi vào application** qua WAF-protected ALB. Đáp án đúng: **B (WAF → Kinesis Data Firehose → S3, dùng Athena query)**. Anh chọn **C (WAF → CloudTrail)** — sai vì CloudTrail không phải đích hợp lệ cho log của WAF.

#### B đúng — đích log hợp lệ của AWS WAF

Theo tài liệu AWS, các destination hợp lệ cho log của WAF web ACL chỉ gồm:

```
AWS WAF web ACL logs ──► Amazon CloudWatch Logs
                     ──► Amazon S3 (trực tiếp)
                     ──► Amazon Kinesis Data Firehose ──► (ví dụ) S3 ──► Athena query
```

Mỗi log WAF tương ứng 1 record của Firehose; Firehose nhận log qua HTTPS endpoint rồi đẩy vào storage destination (ở đây là S3). Sau đó dùng Athena để truy vấn log, phục vụ điều tra lỗi/traceability — đúng khớp yêu cầu "ghi lại toàn bộ traffic, điều tra được khi có sự cố".

#### Vì sao C (lựa chọn của anh) sai

**Amazon CloudTrail không phải là một trong ba đích log hợp lệ của WAF web ACL.** CloudTrail ghi lại **API calls/management events** (ai gọi API gì, lúc nào), không ghi **nội dung traffic HTTP request** đi vào ứng dụng qua WAF. Việc đề đã nói CloudTrail "đã được kích hoạt" ở phần mô tả tình huống là một cái bẫy — nó mô tả hiện trạng hệ thống, không có nghĩa CloudTrail là nơi WAF gửi log tới.

⚠️ **Lỗi lặp lại** — nhóm lỗi quen thuộc: nhầm vai trò giữa các dịch vụ log/giám sát khác nhau (ở đây là CloudTrail vs CloudWatch Logs/S3/Firehose), tương tự cách anh nhầm Firehose với KDS ở Q1/Q8. Quy tắc chung: mỗi dịch vụ AWS chỉ ghi log cho MỘT loại dữ liệu cụ thể — không thể dùng chéo.

#### Các option sai khác

- **A (VPC Flow Logs → KDS):** VPC Flow Logs chỉ ghi **metadata IP traffic** đi/đến network interface (source/dest IP, port, protocol, action ACCEPT/REJECT) — **không ghi nội dung** request HTTP, nên không thể "record all traffic coming into the application" theo đúng nghĩa. Ngoài ra Flow Logs chỉ publish trực tiếp tới CloudWatch Logs, S3, hoặc Kinesis Data Firehose — không có "stream trực tiếp tới Kinesis Data Streams" như option A nói.
- **D (ELB access logs → Firehose):** Elastic Load Balancing access logs **chỉ ghi được trực tiếp vào S3**, không ghi trực tiếp vào Kinesis Data Firehose — option này sai về cơ chế kỹ thuật.

#### So sánh nhanh: đích log hợp lệ theo từng dịch vụ

| Dịch vụ sinh log | Đích log hợp lệ | Ghi được nội dung traffic HTTP? |
|---|---|---|
| **AWS WAF web ACL** | CloudWatch Logs, S3, Kinesis Data Firehose | Có — log request khớp rule WAF |
| **VPC Flow Logs** | CloudWatch Logs, S3, Kinesis Data Firehose | Không — chỉ metadata IP/port/action |
| **ELB (ALB) access logs** | Chỉ S3 (trực tiếp) | Có, nhưng không qua Firehose |
| **AWS CloudTrail** | S3, CloudWatch Logs | Không — chỉ API/management events |

#### Lưu ý thực tế

- `📝 Ghi chú kỹ thuật`: ba dịch vụ log (WAF, VPC Flow Logs) đều có bộ 3 đích giống nhau (CloudWatch Logs / S3 / Kinesis Data Firehose), dễ gây lẫn lộn — nhưng ELB access logs và CloudTrail có đích log **khác và hẹp hơn**, không nằm trong "bộ 3" đó.
- Khi câu hỏi nêu nhiều dịch vụ logging cùng lúc (CloudTrail, WAF, Flow Logs...), luôn tách riêng: dịch vụ nào sinh log gì, đích nào hợp lệ cho đúng dịch vụ đó.

#### Quy tắc nhớ cho thi

- **Thấy "WAF web ACL logs"** → chỉ 3 đích: **CloudWatch Logs / S3 / Kinesis Data Firehose**
- **Thấy "WAF" + "CloudTrail"** → luôn SAI, CloudTrail không phải đích log của WAF
- **Thấy "VPC Flow Logs"** → chỉ ghi metadata IP, KHÔNG ghi nội dung request
- **Thấy "ELB access logs → Firehose"** → SAI, ELB access logs chỉ ghi trực tiếp vào S3

### TD explanation

Correct option:

Configure the WAF web ACL to deliver logs to Amazon Kinesis Data Firehose, which should be configured to eventually store the logs in an Amazon S3 bucket. Use Athena to query the logs for errors and tracking

The logging destinations that you can choose from for your AWS WAF logs are:

Amazon CloudWatch Logs
Amazon Simple Storage Service
Amazon Kinesis Data Firehose

To send logs to Amazon Kinesis Data Firehose, you send logs from your web ACL to an Amazon Kinesis Data Firehose with a configured storage destination. After you enable logging, AWS WAF delivers logs to your storage destination through the HTTPS endpoint of Kinesis Data Firehose.

One AWS WAF log is equivalent to one Kinesis Data Firehose record. If you typically receive 10,000 requests per second and you enable full logs, you should have 10,000 records per second setting in Kinesis Data Firehose.

Incorrect options:

Configure the WAF web ACL to deliver logs to Amazon CloudTrail and create a trail that applies to all Regions. This delivers log files from all Regions to an S3 bucket. Use Athena to query the logs for errors and tracking - As discussed above, the logging destinations that you can choose from for your AWS WAF logs are Amazon CloudWatch Logs, Amazon Simple Storage Service, and Amazon Kinesis Data Firehose. Amazon CloudTrail is not a valid destination for WAF ACL logs.

To capture information about the IP traffic going to and from network interfaces, configure VPC Flow Logs to be directly streamed to Kinesis Data Streams and create alarms for automatic monitoring - VPC Flow You should also note that VPC Flow Logs cannot capture all traffic coming into the application as these can only capture information about the IP traffic going to and from network interfaces in your VPC. In addition, VPC Flow Logs can be directly published only to the following destinations: Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose. So this option is incorrect.

Configure Elastic Load Balancing to write access logs to Amazon Kinesis Data Firehose. The logs can be further directed from Firehose into an Amazon S3 bucket for further analysis and reporting - Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. Elastic Load Balancing access logs are stored in Amazon S3 buckets and it is not possible to directly write the logs to Kinesis Data Firehose.

References:

https://aws.amazon.com/about-aws/whats-new/2021/12/awf-waf-cloudwatch-log-s3-bucket/

https://docs.aws.amazon.com/waf/latest/developerguide/logging-destinations.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

</details>

---

# Group B — Data transfer sizing (Snow vs network) (2)

<a id="q4"></a>

## Q4

A multi-national digital media company wants to exit out of the business of owning and maintaining its own IT infrastructure so it can redeploy resources toward innovation in Artificial Intelligence and related areas to create a better customer experience. As part of this digital transformation, the media company wants to archive about 9 PB of data in its on-premises data center to durable long term storage.

As a Solutions Architect Professional, what is your recommendation to migrate and store this data in the quickest and MOST cost-optimal way?

- **A.** Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data directly into AWS Glacier
- **B.** Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier
- **C.** Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier
- **D.** Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data directly into AWS Glacier

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** 9 PB, quickest + MOST cost-optimal, archive

🪤 **Your trap:** Snowmobile is for ≥10 PB at a single site

🧠 **Rule:** <10 PB → many Snowball Edge Storage Optimized; Snow lands in S3 → lifecycle to Glacier (never direct to Glacier)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises data center                    AWS Cloud
┌─────────────────────┐                    ┌─────────────────────┐
│   9 PB dữ liệu       │   ─── Snow* ───►   │  Amazon S3           │
│   cần archive        │                    │       │ lifecycle    │
└─────────────────────┘                    │       ▼              │
                                            │  AWS Glacier         │
                                            └─────────────────────┘
Yêu cầu: QUICKEST + MOST COST-OPTIMAL cho 9 PB
```

Đáp án đúng: **C — nhiều Snowball Edge Storage Optimized → copy vào S3 → lifecycle policy chuyển sang Glacier**. Anh chọn **B — Snowmobile → S3 → lifecycle Glacier**. Sai chỉ ở thiết bị (Snowmobile), còn luồng "S3 rồi mới lifecycle sang Glacier" thì đúng.

#### Vì sao C đúng — ngưỡng dung lượng quyết định thiết bị

AWS đưa ra ranh giới dung lượng rõ ràng giữa hai dòng thiết bị:

- **Snowball Edge Storage Optimized:** tối ưu cho "dozens of terabytes to petabytes" — tức là dưới 10 PB, có thể dùng nhiều thiết bị cùng lúc (mỗi thiết bị ~80 TB usable). Với 9 PB, cần nhiều chiếc chạy song song.
- **Snowmobile:** AWS khuyến nghị chỉ dùng khi dữ liệu **≥ 10 PB và nằm tại một địa điểm duy nhất**. Với tập dữ liệu dưới 10 PB (hoặc phân tán nhiều site), Snowball là lựa chọn phù hợp hơn.

9 PB < 10 PB → rơi vào vùng Snowball Edge, không phải Snowmobile. Snowmobile là xe tải container quy mô exabyte, triển khai nặng (cần nhân sự AWS tới tận site, lắp đặt kết nối riêng) — dùng cho 9 PB là lãng phí thời gian và chi phí so với việc đặt vài chục thiết bị Snowball Edge chạy song song, nên "quickest + most cost-optimal" sẽ nghiêng về Snowball Edge.

#### Vì sao B (lựa chọn của Anh) sai

B chọn đúng phần luồng dữ liệu (S3 → lifecycle → Glacier) nhưng chọn sai thiết bị — Snowmobile chỉ nên dùng cho ≥ 10 PB tại một site. Với 9 PB, dùng Snowmobile không phải là lựa chọn "MOST cost-optimal" theo khuyến nghị của AWS.

#### Các lựa chọn sai khác

| Lựa chọn | Thiết bị | Đích copy | Vấn đề |
|---|---|---|---|
| A | Snowmobile | **thẳng vào Glacier** | Sai cả thiết bị (9 PB < 10 PB) và đường đi (xem ghi chú dưới) |
| B (Anh chọn) | Snowmobile | S3 → lifecycle → Glacier | Sai thiết bị, đúng đường đi |
| **C (đúng)** | Snowball Edge (nhiều chiếc) | S3 → lifecycle → Glacier | Đúng cả hai |
| D | Snowball Edge (nhiều chiếc) | **thẳng vào Glacier** | Đúng thiết bị, sai đường đi |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** Với **Snowball Edge**, dữ liệu trên thiết bị **chỉ copy được vào S3**, không thể copy trực tiếp vào Glacier — muốn archive thì phải dùng **lifecycle policy** để S3 tự chuyển object sang Glacier sau đó. Đây là lý do D sai dù chọn đúng thiết bị.

Ngược lại, với **Snowmobile**, TD explanation có ghi chú riêng: *"for Snowmobile, you can import your data directly into Glacier"* — nghĩa là về mặt kỹ thuật Snowmobile hỗ trợ đổ thẳng vào Glacier. Nhưng A vẫn sai vì vướng ở điều kiện dung lượng (9 PB chưa đủ ngưỡng dùng Snowmobile), nên option A bị loại trước khi xét tới đường đi dữ liệu.

#### Quy tắc nhớ cho thi

- **Dữ liệu ≥ 10 PB, một địa điểm** → Snowmobile
- **Dữ liệu < 10 PB (hoặc nhiều địa điểm)** → nhiều Snowball Edge
- **Snowball Edge → Glacier**: luôn phải qua **S3 + lifecycle policy**, không có đường thẳng
- **Snowmobile → Glacier**: AWS cho phép import thẳng, nhưng câu hỏi vẫn ưu tiên đúng ngưỡng dung lượng trước

### TD explanation

Correct option:

Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier

Snowball Edge Storage Optimized is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. It provides up to 80 TB of usable HDD storage, 40 vCPUs, 1 TB of SATA SSD storage, and up to 40 Gb network connectivity to address large scale data transfer and pre-processing use cases.

The data stored on the Snowball Edge device can be copied into the S3 bucket and later transitioned into AWS Glacier via a lifecycle policy. You can't directly copy data from Snowball Edge devices into AWS Glacier.

via - https://docs.aws.amazon.com/whitepapers/latest/aws-overview/migration-services.html

Incorrect options:

Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data into Amazon S3 and create a lifecycle policy to transition the data into AWS Glacier - AWS Snowmobile is an exabyte-scale data transfer service used to move extremely large amounts of data to AWS. You can transfer up to 100 PB per Snowmobile. Snowmobile makes it easy to move massive volumes of data to the cloud, including video libraries, image repositories, or even a complete data center migration.

AWS recommends that you should use Snowmobile to migrate large datasets of 10PB or more in a single location. For datasets less than 10PB or distributed in multiple locations, you should use Snowball. So, this option is not the best fit for the given use-case.

via - https://aws.amazon.com/snowmobile/faqs/

Transfer the on-premises data into a Snowmobile device. Copy the Snowmobile data directly into AWS Glacier - As mentioned above, AWS recommends that you should use Snowmobile to migrate large datasets of 10PB or more in a single location. For datasets less than 10PB or distributed in multiple locations, you should use Snowball. So, this option is not the best fit for the given use-case.

Although you should note that for Snowmobile, you can import your data directly into Glacier.

Transfer the on-premises data into multiple Snowball Edge Storage Optimized devices. Copy the Snowball Edge data directly into AWS Glacier - As mentioned earlier, you can't directly copy data from Snowball Edge devices into AWS Glacier. Hence, this option is incorrect.

References:

https://aws.amazon.com/snowball/

https://docs.aws.amazon.com/snowball/latest/ug/how-it-works.html

https://aws.amazon.com/snowmobile/faqs/

https://docs.aws.amazon.com/whitepapers/latest/aws-overview/migration-services.html

</details>

<a id="q15"></a>

## Q15

A social media company is transitioning its IT infrastructure from its on-premises data center to the AWS Cloud. The company wants to move its data artifacts, 200 TB in total size, to Amazon S3 on the AWS Cloud in the shortest possible time. The company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for this data migration. In terms of the networking infrastructure, the company has a 500 Mbps Direct Connect connection to the AWS Cloud as well as an IPSec based AWS VPN connection using the public internet that supports a bandwidth of 1 Gbps.

Which of the following solutions would you recommend to address the given use-case?

- **A.** Leverage the 500 Mbps Direct Connect connection to transfer the data to S3 over the dedicated connection
- **B.** Leverage the 1Gbps IPSec based AWS VPN connection to transfer the data to S3 over the public internet
- **C.** Order three AWS Snowball Edge appliances, split and transfer the data to these three appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3
- **D.** Leverage S3 Transfer Acceleration to transfer the data to S3

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** 200 TB, shortest time, 500 Mbps DX / 1 Gbps VPN

🪤 **Your trap:** 1 Gbps ≈ 0.125 GB/s → 200 TB ≈ 18.5 days of perfect transfer

🧠 **Rule:** Do the math: if link time > ~1 week, ship Snowball Edge (80 TB each → 3 devices)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises                                   Amazon S3
┌───────────────────┐                        ┌───────────┐
│  200 TB dữ liệu    │   500 Mbps Direct Connect
│                    │ ─────────────────────►│           │
│                    │   1 Gbps IPSec VPN (internet)      │
│                    │ ─────────────────────►│           │
│                    │   3x Snowball Edge (ship)          │
│                    │ ──────📦📦📦──────────►│           │
└───────────────────┘                        └───────────┘
Yêu cầu: chuyển XONG trong thời gian NGẮN NHẤT
```

Đáp án đúng: **C — 3 Snowball Edge appliances**. Anh chọn **B — 1 Gbps VPN qua internet**. Nhìn 1 Gbps có vẻ "nhanh", nhưng phải tính ra số giờ/ngày thực tế mới thấy sai.

#### Quy đổi băng thông sang thời gian — làm toán rõ ràng

Quy tắc đổi đơn vị: **1 Byte = 8 bit**, nên:

```
1 Gbps  = 1 Gbit/giây  = 1 / 8 GB/giây  = 0.125 GB/giây  (GBps)
```

Với 1 Gbps VPN, giả định đạt 100% tải (full utilization):

```
0.125 GBps  × 60 giây × 60 phút  = 450 GB/giờ
450 GB/giờ  × 24 giờ             = 10.800 GB/ngày  ≈ 10,8 TB/ngày
```

Vậy tổng thời gian cho 200 TB:

```
200 TB / 10,8 TB/ngày ≈ 18,5 ngày
```

Với 500 Mbps Direct Connect — bằng nửa băng thông của VPN — thời gian gấp đôi:

```
500 Mbps = 0.5 × 1 Gbps → tốc độ truyền bằng 1/2 → ~37 ngày
```

So với **Snowball turnaround 5–7 ngày** (3 thiết bị Storage Optimized, mỗi thiết bị ~80 TB, đủ chứa 200 TB), chênh lệch là **~18,5 ngày vs 5–7 ngày** — Snowball thắng rõ ràng về thời gian "shortest possible".

#### Vì sao B (lựa chọn của Anh) sai

1 Gbps ≈ 0.125 GB/s nghe tưởng nhanh, nhưng quy đổi ra cả ngày chỉ đạt ~10,8 TB/ngày ở điều kiện full-utilization lý tưởng (thực tế mạng doanh nghiệp hiếm khi đạt 100% liên tục). 200 TB cần ~18,5 ngày — gấp 3–4 lần so với thời gian ship Snowball Edge.

#### Các lựa chọn sai khác

| Lựa chọn | Cơ chế | Thời gian ước tính | Vấn đề |
|---|---|---|---|
| A | 500 Mbps Direct Connect | ~37 ngày | Băng thông bằng nửa VPN → chậm nhất |
| B (Anh chọn) | 1 Gbps VPN qua internet | ~18,5 ngày | Vẫn quá chậm so với yêu cầu "shortest" |
| **C (đúng)** | 3× Snowball Edge, ship vật lý | 5–7 ngày | Không bị giới hạn bởi băng thông mạng |
| D | S3 Transfer Acceleration | ~75 TB/tuần (full 1 Gbps) → 200 TB cần ~2.5+ tuần | Tăng tốc nhưng vẫn bị trần băng thông đường truyền, không đủ nhanh |

#### Lưu ý thực tế

⚠️ **Lỗi lặp lại:** Đây là dạng bài "đổi bandwidth sang thời gian truyền" — nếu không quy đổi ra số liệu cụ thể (TB/ngày), rất dễ bị đánh lừa bởi cảm giác "1 Gbps nghe có vẻ đủ nhanh". Luôn làm phép tính: **Gbps → GBps (chia 8) → GB/giờ (×3600) → TB/ngày**.

📝 **Ghi chú kỹ thuật:** TD explanation nêu rõ mốc chuẩn của exam: *"a 1Gbps connection at full utilization can transfer approximately 10 TB of data in a day"*. Đây là hằng số nên nhớ để áp dụng nhanh cho các câu tương tự (chỉ cần nhân/chia theo tỷ lệ bandwidth khác).

#### Quy tắc nhớ cho thi

- **1 Gbps full-utilization ≈ 10 TB/ngày** — công thức gốc để tính nhanh mọi câu bandwidth-vs-Snow
- **Band hẹp hơn (ví dụ 500 Mbps)** → thời gian tăng theo tỷ lệ nghịch (gấp đôi chậm = nửa băng thông)
- **Thời gian truyền qua mạng > ~1 tuần** → nghiêng về Snowball/Snowball Edge (ship vật lý, turnaround 5–7 ngày cố định, không phụ thuộc kích thước data trong giới hạn thiết bị)
- **S3 Transfer Acceleration** vẫn bị trần bởi băng thông đường truyền — chỉ tăng hiệu năng truyền qua CloudFront edge, không "nhảy cóc" qua giới hạn Gbps vật lý
- **Snow* luôn copy vào S3 trước**, không đổ trực tiếp vào Glacier (trừ Snowmobile như TD note riêng)

### TD explanation

Correct option:

Order three AWS Snowball Edge appliances, split and transfer the data to these three appliances and ship them to AWS which will then copy the data from the Snowball Edge appliances to S3

The AWS Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities. Each Snowball Edge device can transport data at speeds faster than the internet. This transport is done by shipping the data in the appliances through a Regional carrier. The appliances are rugged shipping containers, complete with E Ink shipping labels. Snowball Edge devices have three options for device configurations – storage optimized, compute optimized, and with GPU.

Snowball Edge is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. The AWS Snow Family is ideal for customers moving large batches of data at once. The AWS Snowball has a typical 5-7 days turnaround time. As each Snowball Edge device can handle 80TB of data, you can order 3 such devices to take care of the data transfer for the given use-case.

Incorrect options:

Leverage the 1Gbps IPSec based AWS VPN connection to transfer the data to S3 over the public internet

The given use-case requires transferring 200 TB of archived data within the shortest possible duration. Now, the IPSec based AWS VPN connection assures a speed of 1 Gbps (Gigabits per second). As 1 Byte = 8 bits, therefore you can transfer 0.125 GBps (Gigabytes per second).

So the hourly data transfer is 0.1256060 = 450 GB or approximately 0.45 TB.

So the approximate daily data transfer is 0.45 * 24 = ~ 10 TB

Therefore, the entire archived dataset of 200 TB can be transferred in 20 days. As explained above, using Snowball appliances, you can complete this data transfer in just 5-7 days. So this option is incorrect.

Leverage the 500 Mbps Direct Connect connection to transfer the data to S3 over the dedicated connection - We established above that a 1GBps connection would take 20 days to transfer the dataset, so the 500 Mbps Direct Connect connection would take 40 days to transfer the dataset. So this option is incorrect.

Exam Alert:

The exam would probe you on multiple scenarios around competing options to migrate data from on-premises data centers to AWS Cloud. You should remember that a 1Gbps connection at full utilization can transfer approximately 10 TB of data in a day. You will see questions that tweak the available connection bandwidth or change the available utilization, so you just need to factor these changes into the above-mentioned unit rate to identify the correct answer.

Leverage S3 Transfer Acceleration to transfer the data to S3 - S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and your Amazon S3 bucket. S3 Transfer Acceleration leverages Amazon CloudFront’s globally distributed AWS Edge Locations.

You should note that S3 Transfer Acceleration over a fully-utilized 1 Gbps line can only transfer up to 75 TBs in a week's duration. So this option is not correct for the given use-case.

via - https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration

References:

https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration

</details>

---

# Group C — Ops tooling: monitoring, patching, compliance (3)

<a id="q9"></a>

## Q9

A retail company has hired you as an AWS Certified Solutions Architect Professional to provide consultancy for managing a serverless application that consists of multiple API gateways, Lambda functions, S3 buckets and DynamoDB tables. The company is getting reports from customers that some of the application components seem to be lagging while loading dynamic images and some are timing out with the "504 Gateway Timeout" error. As part of your investigations to identify the root cause behind this issue, you can confirm that DynamoDB monitoring metrics are at acceptable levels.

Which of the following steps would you recommend to address these application issues? (Select two)

- **A.** Process and analyze the VPC Flow Logs to determine if there is packet loss between the Lambda function and S3
- **B.** Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals
- **C.** Enable execution logging for the API Gateway. Process and analyze the execution logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **D.** Enable access logging for the API Gateway. Process and analyze the access logs in the API Gateway for HTTP errors to determine the root cause of the errors
- **E.** Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** D, E

🔑 **Key words:** lag loading dynamic images + 504 timeouts; DynamoDB metrics fine

🪤 **Your trap:** X-Ray (E) right, but API Gateway access logs (D) only show who called what, not why Lambda is slow

🧠 **Rule:** Slow Lambda behind API GW → Lambda CloudWatch Logs (processing time) + X-Ray traces

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──► API Gateway ──► Lambda (xử lý ảnh) ──► S3 / DynamoDB
                │                  │
          504 Gateway Timeout   lag khi load dynamic images
                                (DynamoDB metrics bình thường)
```

Cần chọn **2** cách để tìm root cause. Đáp án đúng: **B (CloudWatch Logs cho Lambda)** và **E (X-Ray traces)**. Anh chọn **D (API Gateway access logs)** và **E** — đúng E, sai D.

#### Vì sao B đúng — CloudWatch Logs của Lambda cho biết "chậm ở đâu bên trong code"

Lambda tự động ghi mọi lần invoke vào CloudWatch Logs, và code trong function có thể tự chèn thêm log (ví dụ log timestamp trước/sau khi xử lý ảnh) để xác định **processing time** tại các mốc thời gian cấu hình trước. Vì DynamoDB đã bị loại (metrics ổn), nghi vấn còn lại là Lambda xử lý ảnh chậm — CloudWatch Logs của chính Lambda là nơi trực tiếp thấy được thời gian xử lý đó.

#### Vì sao E đúng — X-Ray cho bức tranh toàn chuỗi request

X-Ray dựng **service map** và **trace summary** cho từng request đi qua API Gateway → Lambda → các service khác, giúp xác định chính xác bottleneck nằm ở bước nào trong pipeline và truy ra request nào bị lỗi HTTP. Đây là công cụ đúng để "visualize the components... identify performance bottlenecks... troubleshoot requests that resulted in an error" như TD explanation nêu.

#### Vì sao D (lựa chọn của Anh) sai — access logs chỉ biết "ai gọi", không biết "vì sao chậm"

**D sai vì access logs của API Gateway chỉ ghi "ai đã gọi API và gọi như thế nào"** (client, HTTP method, response status, thời gian) — đây là log ở mức request/response ngoài cùng, không phải log nội bộ của Lambda. 504 Gateway Timeout nghĩa là backend (Lambda) phản hồi quá lâu — nguyên nhân gốc nằm **bên trong Lambda** (xử lý ảnh chậm), không nằm ở tầng API Gateway. Access log không nhìn vào được bên trong Lambda, nên không giúp xác định root cause.

Đáp án C (execution logging) cùng nhóm với D cũng bị loại vì lý do tương tự — cả hai loại log ở tầng API Gateway đều không đủ sâu để tìm root cause tại nguồn gây lag (Lambda).

#### Lựa chọn sai khác

| Lựa chọn | Lý do sai |
|---|---|
| A. VPC Flow Logs (packet loss Lambda↔S3) | Phân tâm — VPC Flow Logs không dùng để đo packet loss; muốn đo latency/packet loss giữa các điểm mạng phải dùng công cụ như AWSSupport-SetupIPMonitoringFromVPC |
| C. API Gateway execution logs | Chỉ giúp sửa lỗi ở tầng API Gateway (request mapping, integration errors…), không thấy được logic xử lý ảnh bên trong Lambda |
| D (Anh chọn). API Gateway access logs | Chỉ ghi "ai gọi, gọi thế nào" — không có thông tin về thời gian xử lý nội bộ của Lambda |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** TD explanation còn lưu ý thêm một chi tiết dễ nhầm: **HTTP APIs (API Gateway) chỉ có access logs, không có execution logs** — execution logging chỉ tồn tại cho REST API. Nên nếu đề cho dùng HTTP API, option "execution logging" còn sai thêm một lớp nữa vì tính năng đó không tồn tại.

#### Quy tắc nhớ cho thi

- **504 Gateway Timeout ở API Gateway** → lỗi nằm ở backend (ở đây là Lambda), không nằm ở API Gateway → log của API Gateway (access/execution) không đủ để tìm root cause
- **Muốn biết Lambda xử lý mất bao lâu / lỗi ở đâu trong code** → **CloudWatch Logs** (Lambda tự log + code tự chèn log)
- **Muốn biết bottleneck nằm ở bước nào trong toàn chuỗi request** → **X-Ray traces** (service map + trace theo từng request)
- **"access logs" = ai gọi, gọi kiểu gì** ≠ **"execution logs" = chi tiết xử lý request** — cả hai đều ở tầng API Gateway, không chui được vào logic Lambda

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

<a id="q22"></a>

## Q22

The DevOps team for a CRM SaaS company wants to implement a patching plan on AWS Cloud for a large mixed fleet of Windows and Linux servers. The patching plan has to be auditable and must be implemented securely to ensure compliance with the company's business requirements.

As a Solutions Architect Professional, which of the following options would you recommend to address these requirements with MINIMAL effort? (Select two)

- **A.** Apply patch baselines using the AWS-RunPatchBaseline SSM document
- **B.** Apply patch baselines using the AWS-ApplyPatchBaseline SSM document
- **C.** Set up an OS-native patching service to manage the update frequency and release approval for all instances. Set up AWS Config to provide audit and compliance reporting
- **D.** Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval
- **E.** Configure OpsWorks automatic patching support for all applications which will keep the OS up-to-date following the initial installation. Set up AWS Config to provide audit and compliance reporting

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** B, C

🔑 **Key words:** mixed Windows+Linux fleet, auditable, MINIMAL effort

🪤 **Your trap:** AWS-ApplyPatchBaseline is legacy Windows-only; OS-native patching = more effort

🧠 **Rule:** Patch Manager: AWS-RunPatchBaseline + SSM Agent + maintenance window

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mixed fleet:  Windows servers  +  Linux servers
Yêu cầu: patching plan AUDITABLE, MINIMAL effort, compliance
```

Chọn **2** giải pháp. Đáp án đúng: **A (AWS-RunPatchBaseline)** + **D (SSM Agent + maintenance window task)**. Anh chọn **B (AWS-ApplyPatchBaseline)** + **C (OS-native patching + Config)** — cả hai đều sai.

#### Vì sao A đúng — AWS-RunPatchBaseline hỗ trợ cả Windows và Linux

Systems Manager Patch Manager có hai SSM document cho patching:

```
AWS-RunPatchBaseline       → hoạt động trên CẢ Windows Server và Linux
AWS-ApplyPatchBaseline     → CHỈ hoạt động trên Windows (legacy, không hỗ trợ Linux)
```

Vì fleet là **mixed Windows + Linux**, chỉ có `AWS-RunPatchBaseline` đáp ứng được cả hai OS trong một cơ chế duy nhất — đúng yêu cầu "minimal effort" (không cần hai quy trình riêng cho hai OS).

#### Vì sao D đúng — SSM Agent + maintenance window là quy trình chuẩn, có audit sẵn

D mô tả đúng luồng Patch Manager: cài **SSM Agent** trên mọi instance → test patch ở pre-production → deploy bằng **maintenance window task** kèm approval phù hợp. Đây chính là cách Patch Manager hoạt động theo patch baseline (rules auto-approve theo ngày phát hành + danh sách approved/rejected), và lịch sử patching qua Systems Manager console tự nhiên đã auditable — không cần dựng thêm hệ thống riêng.

#### Vì sao B (lựa chọn của Anh) sai — document legacy, bỏ sót Linux

**AWS-ApplyPatchBaseline chỉ patch được Windows, không hỗ trợ Linux.** Với mixed fleet, chọn B đồng nghĩa với việc nửa fleet (Linux) không được patch qua document này — không thỏa yêu cầu "minimal effort" cho toàn bộ fleet (sẽ phải bù thêm cơ chế khác cho Linux, tức là tăng effort, không giảm).

#### Vì sao C (lựa chọn của Anh) sai — OS-native + Config tốn công hơn, lạc hướng

C đề xuất dùng **OS-native patching service** để quản lý tần suất và approval update, cộng thêm **AWS Config để audit/compliance**. Vấn đề:

- OS-native patching (ví dụ WSUS cho Windows, apt/yum tự quản cho Linux) **đòi hỏi dựng và cấu hình riêng cho từng OS** — ngược hẳn với "MINIMAL effort" mà đề yêu cầu.
- Phần AWS Config trong C "is a distraction" — Config dùng để audit **cấu hình resource** (resource trông như thế nào tại một thời điểm, có đúng guideline không), không phải nơi quản lý hay audit **việc patch** đã chạy; nó không thay thế được cho patch compliance reporting của Patch Manager.

#### Bảng so sánh nhanh

| Lựa chọn | Hỗ trợ OS | Effort | Audit sẵn có |
|---|---|---|---|
| **A. AWS-RunPatchBaseline** | Windows + Linux | Thấp | Có (qua Patch Manager) |
| B (Anh chọn). AWS-ApplyPatchBaseline | Chỉ Windows | Cao hơn (thiếu Linux) | Có nhưng không đủ phạm vi |
| **D. SSM Agent + maintenance window** | Windows + Linux | Thấp | Có |
| C (Anh chọn). OS-native + Config | Windows + Linux (riêng lẻ) | Cao | Config không phải công cụ audit cho patching |
| E. OpsWorks auto-patch + Config | — | — | OpsWorks (Chef/Puppet) không có khả năng auto patch management |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** TD explanation nhấn mạnh nguyên văn: *"The AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only and doesn't support Linux instances. For applying patch baselines to both Windows Server and Linux instances, the recommended SSM document is AWS-RunPatchBaseline."* — đây là điểm phân biệt mấu chốt, dễ nhầm vì cả hai tên document đều nghe giống nhau (Apply vs Run).

#### Quy tắc nhớ cho thi

- **"AWS-ApplyPatchBaseline"** → legacy, **chỉ Windows** → sai nếu đề có Linux
- **"AWS-RunPatchBaseline"** → hiện hành, **Windows + Linux** → đúng cho mixed fleet
- **"Minimal effort" + "mixed OS patching"** → luôn nghĩ tới Patch Manager (SSM Agent + maintenance window + RunPatchBaseline), không phải dựng OS-native riêng
- **AWS Config** → audit **cấu hình resource**, không phải nơi quản lý/audit việc **patch** đã chạy

### TD explanation

Correct options:

Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval

Apply patch baselines using the AWS-RunPatchBaseline SSM document

Systems Manager is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects. AWS Systems Manager Agent (SSM Agent) is Amazon software that can be installed and configured on an EC2 instance, an on-premises server, or a virtual machine (VM). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources.

via - https://aws.amazon.com/systems-manager/

You can use Patch Manager to apply patches for both operating systems and applications. (On Windows Server, application support is limited to updates for Microsoft applications). Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches individually or to large groups of instances by using Amazon EC2 tags.

For the given use-case, you can install patches on a regular basis by scheduling patching to run as a Systems Manager maintenance window task.

Systems Manager supports an SSM document for Patch Manager, AWS-RunPatchBaseline, which performs patching operations on instances for both security-related and other types of updates. When the document is run, it uses the patch baseline currently specified as the "default" for an operating system type.

The AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only and doesn't support Linux instances. For applying patch baselines to both Windows Server and Linux instances, the recommended SSM document is AWS-RunPatchBaseline.

via - https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

via - https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-differences.html

Incorrect options:

Configure OpsWorks automatic patching support for all applications which will keep the OS up-to-date following the initial installation. Set up AWS Config to provide audit and compliance reporting - AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments. You cannot use OpsWorks for automatic patch management, so this option is incorrect.

The part about using AWS Config is a distraction. AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - “What did my AWS resource look like at xyz point in time?”.

Set up an OS-native patching service to manage the update frequency and release approval for all instances. Set up AWS Config to provide audit and compliance reporting - You could use an OS-native patching service to manage the update frequency and release approval for all instances but it would take considerable effort to set up and configure this solution. This violates the minimal effort requirement of the given use-case.

Apply patch baselines using the AWS-ApplyPatchBaseline SSM document - As mentioned in the explanation above, the AWS-ApplyPatchBaseline SSM document supports patching on Windows instances only and doesn't support Linux instances. For applying patch baselines to both Windows Server and Linux instances, the recommended SSM document is AWS-RunPatchBaseline.

References:

https://aws.amazon.com/systems-manager/

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-differences.html

</details>

<a id="q26"></a>

## Q26

An IT company wants to move all its clients belonging to the regulated and security-sensitive industries such as financial services and healthcare to the AWS Cloud as it wants to leverage the out-of-box security-specific capabilities offered by AWS. The Security team at the company is developing a framework to validate the adoption of AWS best practices and industry-recognized compliance standards. The AWS Management Console is the preferred method for the in-house teams wanting to provision resources. You have been hired as an AWS Certified Solutions Architect Professional to spearhead this strategic initiative.

Which of the following strategies would you adopt to address these business requirements for continuously assessing, auditing and monitoring the configurations of AWS resources? (Select two)

- **A.** Leverage CloudTrail integration with SNS to automatically notify unauthorized API activities. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services. Use Lambda functions to automatically revert non-authorized changes in AWS resources
- **B.** Leverage EventBridge events near-real-time capabilities to monitor system events patterns to trigger Lambda functions to automatically revert non-authorized changes in AWS resources. Send notifications via SNS topics to improve the incidence response time
- **C.** Leverage Config rules to audit changes to AWS resources and monitor the compliance of the configuration by running the evaluations for the rule at a frequency that you choose. Develop AWS Config custom rules to establish a test-driven development approach by triggering the evaluation when any resource that matches the rule's scope changes in configuration
- **D.** Enable trails and set up CloudTrail events to review and monitor management activities of all AWS accounts by logging these activities into CloudWatch Logs using a KMS key. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services
- **E.** Leverage CloudWatch Logs agent to collect all the AWS SDK logs. Search the log data using a pre-defined set of filter patterns that match mutating API calls. Use CloudWatch alarms to send notifications via SNS when unintended changes are performed. Archive log data by using a batch export to Amazon S3 and analyze via Athena

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D · **You picked:** A, C

🔑 **Key words:** continuously assess/audit configs, compliance standards

🪤 **Your trap:** Config (C) right; A makes CloudTrail+SNS do auto-revert — CloudTrail only records

🧠 **Rule:** Continuous config compliance → AWS Config rules + CloudTrail trail → CloudWatch Logs (KMS)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Clients: financial services, healthcare (regulated, security-sensitive)
Provisioning: chủ yếu qua AWS Management Console
Yêu cầu: liên tục ASSESS + AUDIT + MONITOR cấu hình resource
          (KHÔNG yêu cầu auto-revert thay đổi)
```

Chọn **2** giải pháp. Đáp án đúng: **C (AWS Config rules)** + **D (CloudTrail trail → CloudWatch Logs, dùng KMS key)**. Anh chọn **A (CloudTrail + SNS + Lambda auto-revert)** + **C** — đúng C, sai A.

#### Vì sao C đúng — Config rules đúng nghĩa "continuously assess, audit, monitor configuration"

AWS Config được thiết kế chính xác cho mục này: liên tục track configuration changes của resource, so khớp với **Config rules** (managed hoặc custom) để đánh giá compliant/non-compliant. Hai kiểu trigger đánh giá:

```
Configuration changes  → đánh giá ngay khi resource thay đổi (matches rule's scope)
Periodic                → đánh giá theo chu kỳ cố định (ví dụ mỗi 24h)
```

Đây đúng là công cụ trả lời câu hỏi "resource này cấu hình thế nào tại thời điểm X, và có đúng guideline nội bộ không" — khớp hoàn toàn với yêu cầu đề bài.

#### Vì sao D đúng — CloudTrail trail ghi lại toàn bộ hoạt động quản trị, mã hóa bằng KMS

D: enable trail cho **tất cả account + tất cả region**, log vào **CloudWatch Logs** có mã hóa bằng **KMS key**. CloudTrail ghi lại mọi action của user/role/service dưới dạng event — kể cả hành động qua **Management Console** (đúng với constraint "console là phương thức provisioning ưa thích"). Đưa log vào CloudWatch Logs cho phép giám sát gần real-time và tạo alert, còn mã hóa KMS đáp ứng yêu cầu bảo mật của ngành tài chính/y tế.

#### Vì sao A (lựa chọn của Anh) sai — thêm hành vi auto-revert không có trong mandate

**A dùng CloudTrail + SNS để tự động phát hiện unauthorized API activity, rồi dùng Lambda để tự động revert (hoàn tác) các thay đổi không được phép.** Hai vấn đề:

1. Đề bài chỉ yêu cầu **assess, audit, monitor** — hoàn toàn không yêu cầu **tự động revert** thay đổi. Thêm hành vi auto-remediation vượt quá mandate, biến giải pháp thành over-engineering so với requirement thực tế.
2. A tập trung vào "unauthorized **API** activities" — nhưng đề nói rõ **AWS Management Console là phương thức provisioning ưa thích** của các team in-house, không đặc biệt nhấn vào SDK/API calls. Thiết kế xoay quanh API activity là lệch trọng tâm.

Lưu ý: bản chất CloudTrail chỉ **ghi lại** (record) hoạt động — nó không có khả năng tự sửa/hoàn tác resource; việc "Lambda functions to automatically revert" là một cơ chế riêng (event-driven remediation) được ghép thêm vào, không phải tính năng của CloudTrail.

#### Các lựa chọn sai khác

| Lựa chọn | Vấn đề |
|---|---|
| A (Anh chọn). CloudTrail + SNS + Lambda auto-revert | Thêm auto-revert không có trong yêu cầu; lệch trọng tâm sang API activity trong khi console là phương thức chính |
| B. EventBridge + Lambda auto-revert + SNS | Cùng lỗi với A: "revert" không phải một phần của mandate (chỉ assess/audit/monitor) |
| E. CloudWatch Logs agent thu log AWS SDK, filter mutating API calls | Tập trung vào AWS SDK logs — nhưng use-case không có yêu cầu riêng về SDK/API vì console là phương thức chính |

#### Lưu ý thực tế

⚠️ **Lỗi lặp lại:** Khi đề liệt kê rất rõ phạm vi công việc (ở đây là "assessing, auditing, and monitoring"), bất kỳ lựa chọn nào **thêm hành động ngoài phạm vi đó** (ví dụ auto-remediate/auto-revert) — dù nghe hợp lý về bảo mật — vẫn bị coi là sai vì không khớp đúng yêu cầu đề ra. Luôn so khớp từng từ khóa hành động trong câu hỏi với option.

📝 **Ghi chú kỹ thuật:** TD explanation nhấn mạnh constraint "AWS Management Console is the preferred method" chính là lý do loại cả A, B, E — những option này đều xoay quanh API/SDK activity, không phù hợp với context console-centric của đề.

#### Quy tắc nhớ cho thi

- **"Continuously assess/audit/monitor configuration"** → **AWS Config rules** (configuration-change hoặc periodic trigger)
- **"Record management activity across accounts, console-based"** → **CloudTrail trail (all regions) → CloudWatch Logs + KMS**
- **Đề không nói "auto-remediate/revert"** → loại ngay các option có Lambda tự động hoàn tác thay đổi
- **"Console là phương thức ưa thích"** → loại các option tập trung vào AWS SDK/API logs

### TD explanation

Correct options:

Leverage Config rules to audit changes to AWS resources and monitor the compliance of the configuration by running the evaluations for the rule at a frequency that you choose. Develop AWS Config custom rules to establish a test-driven development approach by triggering the evaluation when any resource that matches the rule's scope changes in configuration

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. You can use Config to answer questions such as - “What did my AWS resource look like at xyz point in time?”.

How AWS Config Works:

via - https://aws.amazon.com/config/

For the given use-case, you can use AWS Config to evaluate the configuration settings of your AWS resources. You do this by creating AWS Config rules, which represent your ideal configuration settings. AWS Config provides customizable, predefined rules called managed rules to help you get started. You can also create your own custom rules. While AWS Config continuously tracks the configuration changes that occur among your resources, it checks whether these changes violate any of the conditions in your rules. If a resource violates a rule, AWS Config flags the resource and marks the rule as noncompliant.

There are two types of evaluation trigger types for Config rules:

Configuration changes – AWS Config triggers the evaluation when any resource that matches the rule's scope changes in configuration. The evaluation runs after AWS Config sends a configuration item change notification.

Periodic – AWS Config runs evaluations for the rule at a frequency that you choose (for example, every 24 hours).

Enable trails and set up CloudTrail events to review and monitor management activities of all AWS accounts by logging these activities into CloudWatch Logs using a KMS key. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services

CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. An event in CloudTrail is the record of activity in an AWS account. This activity can be an action taken by a user, role, or service that is monitorable by CloudTrail. CloudTrail events provide a history of both API and non-API account activity made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.

CloudTrail data events are disabled by default. You can enable logging at an additional cost. Data events are also known as data plane operations and are often high-volume activities. Data events aren't viewable in CloudTrail event history and are charged for all copies at a reduced rate compared to management events.

CloudTrail records management events for the last 90 days free of charge, and are viewable in the Event History with the CloudTrail console. For Amazon S3 delivery of CloudTrail events, the first copy delivered is free. Additional copies of management events are charged.

via - https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

Incorrect options:

Leverage CloudWatch Logs agent to collect all the AWS SDK logs. Search the log data using a pre-defined set of filter patterns that match mutating API calls. Use CloudWatch alarms to send notifications via SNS when unintended changes are performed. Archive log data by using a batch export to Amazon S3 and analyze via Athena - One of the key constraints for the given scenario is that the AWS Management Console is the preferred method for the in-house teams wanting to provision resources. Although this option is technically feasible, but it focuses on using CloudWatch Logs agent to collect all the AWS SDK logs. The given use-case has no specific requirements for AWS SDKs or AWS APIs because AWS Management Console is the preferred method to provision resources. So this option is not the best fit solution.

Leverage CloudTrail integration with SNS to automatically notify unauthorized API activities. Ensure that CloudTrail is enabled for all accounts as well as all available AWS services. Use Lambda functions to automatically revert non-authorized changes in AWS resources - One of the key constraints for the given scenario is that the AWS Management Console is the preferred method for the in-house teams wanting to provision resources. Although this option is technically feasible, but it focuses on capturing unauthorized API activities. The given use-case has no specific requirements for AWS SDKs or AWS APIs because AWS Management Console is the preferred method to provision resources. In addition, the use-case just talks about assessing, auditing and monitoring the configurations of AWS resources. Reverting non-authorized changes in AWS resources is not part of the mandate. So this option is not correct.

Leverage EventBridge events near-real-time capabilities to monitor system events patterns to trigger Lambda functions to automatically revert non-authorized changes in AWS resources. Send notifications via SNS topics to improve the incidence response time - The use-case just talks about assessing, auditing and monitoring the configurations of AWS resources. Reverting non-authorized changes in AWS resources is not part of the mandate. So this option is not correct.

References:

https://aws.amazon.com/config/

https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_manage-rules.html

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events

</details>

---

# Group D — Exact feature behavior (SQS, CloudFront, tenancy, ASG, deploy routing) (5)

<a id="q12"></a>

## Q12

A leading hotel reviews website has a repository of more than one million high-quality digital images. When this massive volume of images became too cumbersome to handle in-house, the company decided to offload the content to a central repository on Amazon S3 as part of its hybrid cloud strategy. The company now wants to reprocess its entire collection of photographic images to change the watermarks. The company wants to use Amazon EC2 instances and Amazon SQS in an integrated workflow to generate the sizes they need for each photo. The team wants to process a few thousand photos each night, using Amazon EC2 Spot Instances. The team uses Amazon SQS to communicate the photos that need to be processed and the status of the jobs. To handle certain sensitive photos, the team wants to postpone the delivery of certain messages to the queue by one minute while all other messages need to be delivered immediately to the queue.

As a Solutions Architect Professional, which of the following solutions would you suggest to the company to handle the workflow for sensitive photos?

- **A.** Use visibility timeout to postpone the delivery of certain messages to the queue by one minute
- **B.** Use message timers to postpone the delivery of certain messages to the queue by one minute
- **C.** Use delay queues to postpone the delivery of certain messages to the queue by one minute
- **D.** Use dead-letter queues to postpone the delivery of certain messages to the queue by one minute

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** delay CERTAIN messages 1 min, others immediately

🪤 **Your trap:** Delay queue delays EVERY message in the queue

🧠 **Rule:** Per-message delay → message timer (DelaySeconds on send); whole queue → delay queue

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
SQS Queue
┌─────────────────────────────────────────┐
│ Msg 1 (thường)      → hiện ngay          │
│ Msg 2 (thường)      → hiện ngay          │
│ Msg 3 (sensitive)   → PHẢI trễ 1 phút    │
│ Msg 4 (thường)      → hiện ngay          │
└─────────────────────────────────────────┘
Yêu cầu: chỉ TRỄ MỘT SỐ message cụ thể, các message khác vẫn giao ngay
```

Đáp án đúng: **B – message timer**. Anh chọn **C – delay queue**.

#### Vì sao B đúng

**Message timer** = tham số `DelaySeconds` đặt khi **gửi từng message** (`SendMessage`). Nó chỉ ảnh hưởng đúng message đó: message có timer sẽ "vô hình" với consumer trong khoảng thời gian đó (tối đa 15 phút), còn các message khác gửi bình thường (không set `DelaySeconds`) thì hiện ngay lập tức.

```
SendMessage(msg3, DelaySeconds=60)   → msg3 ẩn 60s rồi mới hiện
SendMessage(msg1)                    → msg1 hiện ngay (delay mặc định = 0s)
```

Vì yêu cầu đề bài là "certain messages" (một số message) trễ 1 phút, còn "all other messages" (các message khác) vẫn giao ngay → đây đúng là bài toán của message timer, cấu hình **theo từng message**.

#### Vì sao C (delay queue) sai — cái bẫy của Anh

**Delay queue** cũng tạo độ trễ ban đầu, nhưng độ trễ này là **thuộc tính của CẢ QUEUE**, áp dụng cho **mọi message mới gửi vào queue đó**, không chọn lọc được message nào.

```
Delay queue (DelaySeconds=60 đặt ở cấp QUEUE)
    → Msg 1 cũng trễ 60s
    → Msg 2 cũng trễ 60s
    → Msg 3 cũng trễ 60s
    → KHÔNG thể để Msg 1, 2, 4 giao ngay còn chỉ Msg 3 trễ
```

Đề bài rõ ràng cần "các message khác giao ngay lập tức" → delay queue không làm được điều này vì nó trễ toàn bộ queue. Đây chính là bẫy: cả message timer và delay queue đều dùng cùng tham số `DelaySeconds` và cùng giới hạn tối đa 15 phút, dễ nhầm lẫn vì tên gọi "delay" nghe có vẻ đúng hơn.

#### Các lựa chọn sai khác

- **A. Visibility timeout** — đây là khoảng thời gian **sau khi một consumer đã nhận (receive) message**, SQS ẩn message đó với các consumer khác để tránh xử lý trùng. Nó không liên quan đến việc trì hoãn message *trước khi* nó được giao lần đầu. Mặc định 30s, tối đa 12 giờ.
- **D. Dead-letter queue (DLQ)** — là nơi chứa các message **xử lý thất bại nhiều lần** (quá `maxReceiveCount`) để debug, hoàn toàn không có chức năng trì hoãn giao message.

#### So sánh

| Cơ chế | Phạm vi áp dụng | Thời điểm | Tối đa |
|---|---|---|---|
| **Message timer (B)** | Từng message riêng lẻ | Trước khi message hiện lần đầu | 15 phút |
| Delay queue (C) | Toàn bộ queue | Trước khi message hiện lần đầu | 15 phút |
| Visibility timeout (A) | Từng message, sau khi đã được receive | Sau khi consumer đã lấy message | 12 giờ |
| Dead-letter queue (D) | Message lỗi lặp lại | Sau nhiều lần xử lý thất bại | N/A |

#### Lưu ý thực tế

- Message timer và delay queue dùng cùng tên tham số `DelaySeconds` nhưng set ở hai cấp khác nhau (send-message vs queue attribute) — đề thi hay đánh vào điểm này.
- FIFO queue không hỗ trợ message timer theo từng message giống Standard queue trong một số ngữ cảnh — nhưng đề này không hỏi tới FIFO nên không cần lăn tăn.

#### Quy tắc nhớ cho thi

- **Thấy "chỉ một số message cần trễ, còn lại giao ngay"** → **message timer** (per-message `DelaySeconds`)
- **Thấy "toàn bộ queue cần trễ ban đầu"** → **delay queue** (queue-level `DelaySeconds`)
- **Thấy "tránh xử lý trùng sau khi consumer đã nhận"** → **visibility timeout**
- **Thấy "message xử lý lỗi liên tục, cần cách ly để debug"** → **dead-letter queue**

### TD explanation

Correct option:

Use message timers to postpone the delivery of certain messages to the queue by one minute

You can use message timers to set an initial invisibility period for a message added to a queue. So, if you send a message with a 60-second timer, the message isn't visible to consumers for its first 60 seconds in the queue. The default (minimum) delay for a message is 0 seconds. The maximum is 15 minutes. Therefore, you should use message timers to postpone the delivery of certain messages to the queue by one minute.

Incorrect options:

Use dead-letter queues to postpone the delivery of certain messages to the queue by one minute - Dead-letter queues can be used by other queues (source queues) as a target for messages that can't be processed (consumed) successfully. Dead-letter queues are useful for debugging your application or messaging system because they let you isolate problematic messages to determine why their processing doesn't succeed. You cannot use dead-letter queues to postpone the delivery of certain messages to the queue by one minute.

Use visibility timeout to postpone the delivery of certain messages to the queue by one minute - Visibility timeout is a period during which Amazon SQS prevents other consumers from receiving and processing a given message. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours. You cannot use visibility timeout to postpone the delivery of certain messages to the queue by one minute.

Use delay queues to postpone the delivery of certain messages to the queue by one minute - Delay queues let you postpone the delivery of all new messages to a queue for several seconds, for example, when your consumer application needs additional time to process messages. If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period. The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes. You cannot use delay queues to postpone the delivery of only certain messages to the queue by one minute.

via - https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html

References:

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html

</details>

<a id="q20"></a>

## Q20

An e-commerce company wants to rollout and test a blue-green deployment for its global application in the next couple of days. Most of the customers use mobile phones which are prone to DNS caching. The company has only two days left before the big sale will be launched.

As a Solutions Architect Professional, which of the following options would you suggest to test the deployment on as many users as possible in the given time frame?

- **A.** Use Route 53 weighted routing to spread traffic across different deployments
- **B.** Use AWS CodeDeploy deployment options to choose the right deployment
- **C.** Use Elastic Load Balancer to distribute traffic across deployments
- **D.** Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** mobile clients cache DNS, only 2 days, blue/green

🪤 **Your trap:** Route 53 weighted is DNS-based → stale client caches ignore the new weights

🧠 **Rule:** DNS caching blocks a fast shift → Global Accelerator endpoint weights / traffic dials

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Ứng dụng global, khách hàng chủ yếu dùng MOBILE
Mobile client/resolver → cache DNS LÂU → không biết record vừa đổi

Blue (bản cũ) ──┐
                 ├──► Cần test blue/green, CHỈ CÒN 2 NGÀY
Green (bản mới) ──┘
```

Yêu cầu: chuyển traffic blue/green **nhanh, kiểm soát được, không bị cản bởi DNS caching trên thiết bị client**. Đáp án đúng: **D – AWS Global Accelerator**. Anh chọn **A – Route 53 weighted routing**.

#### Vì sao D đúng

**Global Accelerator** hoạt động ở **network layer**, cấp cho ứng dụng **2 địa chỉ IP anycast tĩnh** làm entry point cố định. Việc chuyển traffic giữa blue và green được thực hiện qua:

- **Traffic dial**: % traffic đổ vào một **endpoint group** (vùng/region)
- **Endpoint weight**: % traffic đổ vào từng **endpoint** trong group (ALB, NLB, EIP, EC2...)

```
Client ──► 2 IP anycast tĩnh (không đổi) ──► Global Accelerator
                                                  │
                                    traffic dial / endpoint weight
                                    (đổi ngay trong vài giây)
                                       ┌──────────┴──────────┐
                                    Blue (cũ)              Green (mới)
```

Vì client luôn gọi vào **cùng 2 IP tĩnh**, không có DNS record nào thay đổi cả — nên **không hề bị ảnh hưởng bởi DNS caching**. Theo tài liệu AWS, thay đổi traffic dial/endpoint weight có hiệu lực **trong vài giây**, đúng với yêu cầu "chỉ còn 2 ngày, cần test nhanh trên nhiều user nhất có thể".

#### Vì sao A (Route 53 weighted routing) sai — cái bẫy của Anh

Route 53 weighted routing hoạt động ở **DNS layer**: đổi % trọng số nghĩa là đổi **giá trị trả về khi resolver query DNS**. Nhưng vấn đề là:

```
Record cũ đã được resolver/mobile client CACHE theo TTL
    → Anh đổi weight trên Route 53
    → Client ĐÃ CACHE vẫn tiếp tục dùng IP cũ cho đến khi cache hết hạn
    → Không kiểm soát được THỜI ĐIỂM traffic thực sự chuyển
```

Đề bài nói rõ "mobile phones which are prone to DNS caching" — đây chính là từ khóa loại bỏ Route 53. Route 53 weighted routing là lựa chọn hợp lý cho blue/green **khi không có vấn đề DNS caching**, nhưng ở đây lại chính là use-case bị DNS caching cản trở.

#### Các lựa chọn sai khác

- **C. Elastic Load Balancer / ALB weighted target groups** — không phụ thuộc DNS, cũng hợp lệ cho blue/green, nhưng **chỉ hoạt động trong một Region**. Đề bài là "global application" nên cần giải pháp multi-Region → ELB không đáp ứng được phạm vi.
- **B. AWS CodeDeploy** — CodeDeploy hỗ trợ kiểu deployment blue/green, nhưng **chỉ deploy trong cùng một Region**, cũng không đủ cho yêu cầu toàn cầu.

#### So sánh

| Giải pháp | Layer | Bị ảnh hưởng bởi DNS caching? | Phạm vi |
|---|---|---|---|
| **Global Accelerator (D)** | Network (anycast IP tĩnh) | Không | Multi-Region |
| Route 53 weighted (A) | DNS | Có — client cache record cũ | Multi-Region |
| ELB / ALB weighted target group (C) | Load balancer | Không | Chỉ 1 Region |
| CodeDeploy blue/green (B) | Deployment orchestration | Không trực tiếp, nhưng hạn chế khác | Chỉ 1 Region |

#### Lưu ý thực tế

- Global Accelerator không "thay thế" ALB/NLB — nó đứng **phía trước** chúng làm entry point cố định, rồi điều traffic vào các endpoint (ALB/NLB/EIP/EC2) ở nhiều Region.
- "IP tĩnh không đổi" là điểm mấu chốt khiến Global Accelerator miễn nhiễm với DNS TTL/caching — vì client không cần resolve lại DNS để lấy IP mới.

#### Quy tắc nhớ cho thi

- **Thấy "mobile client DNS caching" + "cần chuyển traffic nhanh/kiểm soát"** → **Global Accelerator** (traffic dial / endpoint weight), không phải Route 53
- **Thấy "blue/green global, multi-Region"** → loại ELB/ALB weighted (chỉ 1 Region) và CodeDeploy (chỉ 1 Region)
- **Thấy "blue/green trong 1 Region, không ngại DNS"** → Route 53 weighted hoặc ALB weighted target group đều hợp lệ

### TD explanation

Correct option:

Blue/green deployment is a technique for releasing applications by shifting traffic between two identical environments running different versions of the application: "Blue" is the currently running version and "green" the new version. This type of deployment allows you to test features in the green environment without impacting the currently running version of your application. When you’re satisfied that the green version is working properly, you can gradually reroute the traffic from the old blue environment to the new green environment. Blue/green deployments can mitigate common risks associated with deploying software, such as downtime and rollback capability.

Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment - AWS Global Accelerator is a network layer service that directs traffic to optimal endpoints over the AWS global network, this improves the availability and performance of your internet applications. It provides two static anycast IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, such as your Application Load Balancers, Network Load Balancers, Elastic IP addresses or Amazon EC2 instances, in a single or in multiple AWS regions.

AWS Global Accelerator uses endpoint weights to determine the proportion of traffic that is directed to endpoints in an endpoint group, and traffic dials to control the percentage of traffic that is directed to an endpoint group (an AWS region where your application is deployed).

While relying on the DNS service is a great option for blue/green deployments, it may not fit use-cases that require a fast and controlled transition of the traffic. Some client devices and internet resolvers cache DNS answers for long periods; this DNS feature improves the efficiency of the DNS service as it reduces the DNS traffic across the Internet, and serves as a resiliency technique by preventing authoritative name-server overloads. The downside of this in blue/green deployments is that you don’t know how long it will take before all of your users receive updated IP addresses when you update a record, change your routing preference or when there is an application failure.

With AWS Global Accelerator, you can shift traffic gradually or all at once between the blue and the green environment and vice-versa without being subject to DNS caching on client devices and internet resolvers, traffic dials and endpoint weights changes are effective within seconds.

Incorrect options:

Use Route 53 weighted routing to spread traffic across different deployments - Weighted routing lets you associate multiple resources with a single domain name (example.com) or subdomain name (acme.example.com) and choose how much traffic is routed to each resource. This can be useful for a variety of purposes, including load balancing and testing new versions of the software. As discussed earlier, DNS caching is a negative behavior for this use case and hence Route 53 is not a good option.

Use Elastic Load Balancer to distribute traffic across deployments - An ELB can distribute traffic across healthy instances. You can also use the ALB weighted target groups feature for blue/green deployments as it does not rely on the DNS service. In addition you don’t need to create new ALBs for the green environment. As the use-case refers to a global application, so this option cannot be used for a multi-Region solution which is needed for the given requirement.

Use AWS CodeDeploy deployment options to choose the right deployment - In CodeDeploy, a deployment is the process, and the components involved in the process, of installing content on one or more instances. This content can consist of code, web and configuration files, executables, packages, scripts, and so on. CodeDeploy deploys content that is stored in a source repository, according to the configuration rules you specify. Blue/Green deployment is one of the deployment types that CodeDeploy supports. AWS CodeDeploy performs deployments with AWS resources located in the same region, so this option is ruled out.

References:

https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-global-accelerator-to-achieve-blue-green-deployments

https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted

</details>

<a id="q21"></a>

## Q21

A mobile app based social media company is using Amazon CloudFront to deliver media-rich content to its audience across the world. The Content Delivery Network (CDN) offers a multi-tier cache by default, with regional edge caches that improve latency and lower the load on the origin servers when the object is not already cached at the edge. However, there are certain content types that bypass the regional edge cache and go directly to the origin.

Which of the following content types skip the regional edge cache? (Select two)

- **A.** Static content such as style sheets, JavaScript files
- **B.** Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin
- **C.** Dynamic content, as determined at request time (cache-behavior configured to forward all headers)
- **D.** E-commerce assets such as product photos
- **E.** User-generated videos

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, C · **You picked:** A, D

🔑 **Key words:** content that SKIPS the regional edge cache

🪤 **Your trap:** Static files, product photos, user videos all go THROUGH the regional edge cache

🧠 **Rule:** Skip regional edge cache: proxy methods PUT/POST/PATCH/OPTIONS/DELETE + dynamic content forwarding all headers

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──► CloudFront POP (edge location)
               │
               ├── Có trong POP cache? → trả về ngay
               │
               └── Không có / cần kiểm tra?
                        │
                        ▼
              Regional Edge Cache (tầng giữa)
                        │
                        ▼
                     Origin
```

Câu hỏi: loại content nào **bỏ qua regional edge cache**, đi thẳng từ POP đến origin? (Chọn 2). Đáp án đúng: **B, C**. Anh chọn **A, D** — đều sai vì đó chính là nhóm content **ĐI QUA** regional edge cache, ngược với yêu cầu đề bài.

#### Vì sao B và C đúng

**B. Proxy methods PUT/POST/PATCH/OPTIONS/DELETE** — đây là các method **ghi dữ liệu** (không phải GET/HEAD đọc nội dung tĩnh). Theo tài liệu CloudFront, các request dùng method này đi **trực tiếp từ POP đến origin**, không qua regional edge cache — vì về bản chất chúng không phải là "lấy nội dung để cache" mà là chuyển tiếp hành động tới origin xử lý.

**C. Dynamic content, forward all headers** — khi cache behavior cấu hình **forward tất cả headers** lên origin, CloudFront coi đây là nội dung **động, xác định tại thời điểm request** (ví dụ phụ thuộc cookie, user-agent, ngôn ngữ...). Loại content này cũng đi thẳng tới origin, bỏ qua tầng regional edge cache, vì về bản chất nó không "cache được" theo kiểu thông thường.

```
PUT/POST/PATCH/OPTIONS/DELETE  ──┐
                                   ├──► POP ──────────────► Origin (bỏ qua regional edge cache)
Dynamic + forward-all-headers ───┘
```

#### Vì sao A và D sai — cái bẫy của Anh

A (static: CSS, JS) và D (e-commerce: product photos), cùng với E (user-generated videos), đều thuộc nhóm **nội dung có thể cache được** (cacheable static/semi-static content). Theo giải thích TD: "user-generated content (video, photos, artwork), e-commerce assets (product photos/videos), và static content (stylesheets, JavaScript)" đều **ĐI QUA regional edge cache** bình thường — đây chính là mục đích tồn tại của regional edge cache: giữ các nội dung không đủ "hot" để ở lại POP nhưng vẫn được truy cập đủ nhiều để cache gần viewer hơn, giảm tải lên origin.

Cái bẫy ở đây: A, D, E nghe có vẻ "đa dạng, phong phú" dễ liên tưởng đến việc "phải xử lý đặc biệt", nhưng thực chất chúng lại là ví dụ điển hình cho nhóm **tuân theo luồng cache chuẩn (đi qua regional edge cache)**, không phải nhóm ngoại lệ bị skip.

#### Comparison table

| Loại content | Có qua regional edge cache? |
|---|---|
| **B. PUT/POST/PATCH/OPTIONS/DELETE** | **Không — đi thẳng tới origin** |
| **C. Dynamic, forward all headers** | **Không — đi thẳng tới origin** |
| A. Static (CSS/JS) | Có |
| D. E-commerce product photos | Có |
| E. User-generated videos | Có |

#### Lưu ý thực tế

- Quy tắc chung: **GET/HEAD cacheable content** → tận dụng cả POP và regional edge cache; **write methods** (PUT/POST/PATCH/OPTIONS/DELETE) và **dynamic/forward-all-headers content** → bỏ qua tầng giữa, đi thẳng origin.
- "Forward all headers" trong cache behavior là tín hiệu rõ ràng CloudFront coi response là dynamic/per-request, không áp dụng cache đa tầng.

#### Quy tắc nhớ cho thi

- **Thấy "method ghi dữ liệu" (PUT/POST/PATCH/OPTIONS/DELETE)** → **bỏ qua regional edge cache**, đi thẳng origin
- **Thấy "dynamic content, forward all headers"** → **bỏ qua regional edge cache**
- **Thấy "static files / product photos / user-generated videos"** → đây là nội dung **cacheable**, **đi qua** regional edge cache bình thường, KHÔNG phải câu trả lời cho "skip"

### TD explanation

Correct options:

Dynamic content, as determined at request time (cache-behavior configured to forward all headers)

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.
CloudFront points of presence (POPs) (edge locations) make sure that popular content can be served quickly to your viewers. CloudFront also has regional edge caches that bring more of your content closer to your viewers, even when the content is not popular enough to stay at a POP, to help improve performance for that content.

Dynamic content, as determined at request time (cache-behavior configured to forward all headers), does not flow through regional edge caches, but goes directly to the origin. So this option is correct.

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin from the POPs and do not proxy through the regional edge caches. So this option is also correct.

How CloudFront works with regional edge caches:

via - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

Incorrect Options:

E-commerce assets such as product photos

User-generated videos

Static content such as style sheets, JavaScript files

The following type of content flows through the regional edge caches - user-generated content, such as video, photos, or artwork; e-commerce assets such as product photos and videos and static content such as style sheets, JavaScript files. Hence these three options are not correct.

Reference:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html

</details>

<a id="q24"></a>

## Q24

A multi-national bank has recently migrated to AWS Cloud to utilize dedicated instances that are physically isolated at the host hardware level from instances that belong to other AWS accounts. The bank's flagship application is hosted on a fleet of EC2 instances which are part of an Auto Scaling group (ASG). The ASG uses a Launch Configuration (LC-A) with "dedicated" instance placement tenancy but the VPC (VPC-A) used by the Launch Configuration LC-A has the instance tenancy set to default. Later the engineering team creates a new Launch Configuration (LC-B) with "default" instance placement tenancy but the VPC (VPC-B) used by the Launch Configuration LC-B has the instance tenancy set to dedicated.

As a Solutions Architect Professional, which of the following options would you identify as correct regarding the instances launched via Launch Configuration LC-A and Launch Configuration LC-B?

- **A.** The instances launched by Launch Configuration LC-A will have dedicated instance tenancy while the instances launched by the Launch Configuration LC-B will have default instance tenancy
- **B.** The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have default instance tenancy
- **C.** The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have dedicated instance tenancy
- **D.** The instances launched by Launch Configuration LC-A will have default instance tenancy while the instances launched by the Launch Configuration LC-B will have dedicated instance tenancy

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** LC tenancy vs VPC tenancy (dedicated/default mix)

🪤 **Your trap:** Assumed the VPC default overrides the LC (or vice versa)

🧠 **Rule:** Either LC or VPC = dedicated → instances are dedicated

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Launch Configuration LC-A: tenancy = DEDICATED
VPC-A (dùng bởi LC-A):      tenancy = default
                             → Instance từ LC-A trong VPC-A = ???

Launch Configuration LC-B: tenancy = default
VPC-B (dùng bởi LC-B):      tenancy = DEDICATED
                             → Instance từ LC-B trong VPC-B = ???
```

Đáp án đúng: **C — cả hai đều ra instance dedicated**. Anh chọn **B — cả hai đều ra default**, ngược hoàn toàn với quy tắc thật.

#### Vì sao C đúng

Quy tắc AWS: khi tạo Launch Configuration, giá trị tenancy mặc định là **null**, và tenancy thật của instance được quyết định bởi **sự kết hợp giữa LC tenancy và VPC tenancy** theo nguyên tắc **"dedicated thắng"**: chỉ cần **MỘT trong hai** (LC hoặc VPC) là `dedicated`, thì instance launch ra **luôn là dedicated**.

```
LC tenancy    VPC tenancy    →    Instance tenancy
─────────────────────────────────────────────────
dedicated   +  default       →    dedicated   (LC-A)
default     +  dedicated     →    dedicated   (LC-B)
default     +  default       →    default
dedicated   +  dedicated     →    dedicated
```

Áp vào đề bài:
- **LC-A** = dedicated, VPC-A = default → có một bên dedicated → instance **dedicated**
- **LC-B** = default, VPC-B = dedicated → có một bên dedicated → instance **dedicated**

→ Cả LC-A và LC-B đều cho ra instance **dedicated tenancy**, đúng với đáp án C.

#### Vì sao B sai — cái bẫy của Anh

Anh chọn B (cả hai đều default) — tức là Anh có thể đã nghĩ theo một trong hai hướng sai:
1. **VPC tenancy luôn override LC tenancy** (và vì không nhớ VPC nào là dedicated, mặc định coi cả hai thành default), hoặc
2. **Cần CẢ HAI cùng dedicated mới ra dedicated** (giống kiểu AND logic), nên một bên default là "kéo" cả hai về default.

Thực tế quy tắc là **OR logic, dedicated chiếm ưu thế**: chỉ cần 1 phía là dedicated thì kết quả dedicated, không có trường hợp nào trong đề bài mà cả LC và VPC đều default — nên B hoàn toàn không khớp.

#### Các lựa chọn sai khác

- **A. LC-A dedicated, LC-B default** — sai vì bỏ qua ảnh hưởng của VPC-A (default) tới LC-A (đúng ra kết quả LC-A vẫn dedicated vì LC-A tenancy đã là dedicated — nhưng LC-B lại bị đánh giá sai thành default, trong khi VPC-B dedicated đã đủ để khiến LC-B ra dedicated).
- **D. LC-A default, LC-B dedicated** — ngược lại hoàn toàn với thực tế: LC-A có LC tenancy = dedicated nên không thể là default.

#### So sánh

| Cấu hình | LC tenancy | VPC tenancy | Instance tenancy thực tế |
|---|---|---|---|
| **LC-A** | dedicated | default | **dedicated** |
| **LC-B** | default | dedicated | **dedicated** |
| Option A đề xuất | — | — | LC-A dedicated / LC-B default (sai) |
| Option B đề xuất (Anh chọn) | — | — | cả hai default (sai) |
| Option D đề xuất | — | — | LC-A default / LC-B dedicated (sai) |

#### Lưu ý thực tế

- Quy tắc "dedicated thắng" áp dụng đối xứng: không quan trọng dedicated nằm ở LC hay ở VPC, kết quả cuối cùng vẫn là dedicated.
- Launch Template (phiên bản mới hơn Launch Configuration) tuân theo cùng logic tenancy này khi phối hợp với VPC settings.

#### Quy tắc nhớ cho thi

- **Thấy "LC tenancy vs VPC tenancy khác nhau"** → chỉ cần **MỘT bên là dedicated** → kết quả luôn **dedicated**
- **Thấy cả LC và VPC đều default** → mới ra **default**
- **Đừng nhầm đây là AND logic** (cần cả hai dedicated) — đây là **OR logic nghiêng về dedicated**

### TD explanation

Correct option:

The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have dedicated instance tenancy

A launch configuration is an instance configuration template that an Auto Scaling group uses to launch EC2 instances. When you create a launch configuration, you specify information for the instances. Include the ID of the Amazon Machine Image (AMI), the instance type, a key pair, one or more security groups, and a block device mapping. If you've launched an EC2 instance before, you specified the same information to launch the instance.

When you create a launch configuration, the default value for the instance placement tenancy is null and the instance tenancy is controlled by the tenancy attribute of the VPC.  If you set the Launch Configuration Tenancy to default and the VPC Tenancy is set to dedicated, then the instances have dedicated tenancy. If you set the Launch Configuration Tenancy to dedicated and the VPC Tenancy is set to default, then again the instances have dedicated tenancy.

Launch Configuration Tenancy vs VPC Tenancy

via - https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy

Incorrect options:

The instances launched by Launch Configuration LC-A will have dedicated instance tenancy while the instances launched by the Launch Configuration LC-B will have default instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

The instances launched by Launch Configuration LC-A will have default instance tenancy while the instances launched by the Launch Configuration LC-B will have dedicated instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

The instances launched by both Launch Configuration LC-A and Launch Configuration LC-B will have default instance tenancy - If either Launch Configuration Tenancy or VPC Tenancy is set to dedicated, then the instance tenancy is also dedicated. Therefore, this option is incorrect.

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy

</details>

<a id="q27"></a>

## Q27

The engineering team at a retail company has deployed a fleet of EC2 instances under an Auto Scaling group (ASG). The instances under the ASG span two Availability Zones (AZ) within the eu-west-1 region. All the incoming requests are handled by an Application Load Balancer (ALB) that routes the requests to the EC2 instances under the ASG. A planned migration went wrong last week when two instances (belonging to AZ 1) were manually terminated and desired capacity was reduced causing the Availability Zones to become unbalanced. Later that day, another instance (belonging to AZ 2) was detected as unhealthy by the Application Load Balancer's health check.

Which of the following options represent the correct outcomes for the aforesaid events? (Select two)

- **A.** Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance
- **B.** Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously
- **C.** As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched
- **D.** Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it
- **E.** As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E · **You picked:** B, E

🔑 **Key words:** unhealthy instance + AZ rebalancing after manual terminate

🪤 **Your trap:** E right; B wrong — ASG does not terminate+launch in one activity

🧠 **Rule:** Unhealthy → terminate FIRST then launch; AZ rebalancing → launch FIRST then terminate

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ASG span 2 AZ (eu-west-1)
  AZ-1: 2 instance bị TERMINATE THỦ CÔNG + giảm desired capacity
        → AZ bị MẤT CÂN BẰNG (unbalanced)
  AZ-2: 1 instance bị ALB health check đánh dấu UNHEALTHY

Hai sự kiện RIÊNG BIỆT, xảy ra theo 2 cơ chế khác nhau:
  1) AZ rebalancing (do unbalanced)
  2) Unhealthy instance replacement (do health check fail)
```

Đáp án đúng: **A, E**. Anh chọn **B, E** — đúng E, sai ở B (chọn nhầm cơ chế không tồn tại cho trường hợp unhealthy).

#### Vì sao A đúng — xử lý instance unhealthy

Với instance bị đánh dấu unhealthy (do ALB health check), ASG xử lý theo trình tự **TERMINATE TRƯỚC, LAUNCH SAU**, và đây là **hai scaling activity riêng biệt**, không gộp chung:

```
Bước 1: Scaling activity #1 → TERMINATE instance unhealthy
Bước 2: Scaling activity #2 (sau đó) → LAUNCH instance mới để thay thế
```

Lý do: instance đã unhealthy nghĩa là nó không còn phục vụ tốt, nên ASG ưu tiên loại nó ra khỏi target group trước, rồi mới launch instance mới bù vào.

#### Vì sao E đúng — AZ rebalancing (Anh đã chọn đúng)

Khi ASG phát hiện AZ mất cân bằng (do terminate thủ công + giảm desired capacity ở AZ-1), nó tự **rebalance**, nhưng theo trình tự **NGƯỢC LẠI**: **LAUNCH TRƯỚC, TERMINATE SAU**:

```
Bước 1: LAUNCH instance mới ở AZ cần bù
Bước 2: TERMINATE instance dư ở AZ khác
```

Lý do: rebalancing là một thao tác "bảo trì cân bằng", không phải xử lý lỗi — nên ASG launch trước để **không làm giảm capacity/availability** trong lúc đang chuyển đổi.

#### Vì sao B sai — cái bẫy của Anh

B khẳng định "terminate và launch instance mới xảy ra **đồng thời** trong cùng một scaling activity". Đây là **lựa chọn gây nhiễu (made-up distractor)**: thực tế, với unhealthy instance, terminate và launch là **hai scaling activity tách biệt, nối tiếp nhau theo thời gian** (terminate xong rồi mới launch), không phải một hành động đồng thời. Anh có thể đã nhớ đúng "unhealthy → terminate rồi launch" nhưng gộp nhầm thành "một activity làm cả hai cùng lúc" — sai về tính chất hai activity riêng biệt.

#### Các lựa chọn sai khác

- **C.** Nói AZ rebalancing **terminate trước rồi mới launch** — ngược hoàn toàn với quy tắc thật (rebalancing phải launch trước).
- **D.** Nói unhealthy instance **launch trước rồi mới terminate** — ngược hoàn toàn với quy tắc thật (unhealthy phải terminate trước).

#### Comparison table — vì sao thứ tự khác nhau giữa 2 cơ chế

| Cơ chế | Thứ tự | Vì sao |
|---|---|---|
| **Unhealthy replacement (A)** | **Terminate → Launch** (2 activity riêng) | Instance lỗi cần loại khỏi traffic trước |
| **AZ rebalancing (E)** | **Launch → Terminate** | Tránh giảm capacity/availability khi đang cân bằng lại |
| Option B (sai) | Terminate + Launch cùng lúc | Không tồn tại — bị bịa ra để gây nhiễu |
| Option C (sai) | Terminate → Launch (gán cho rebalancing) | Nhầm thứ tự của cơ chế unhealthy sang rebalancing |
| Option D (sai) | Launch → Terminate (gán cho unhealthy) | Nhầm thứ tự của cơ chế rebalancing sang unhealthy |

#### Lưu ý thực tế

- Hai cơ chế này dễ bị đề thi hoán đổi thứ tự cho nhau (C và D chính là phiên bản "đảo ngược" của A và E) — phải nhớ chính xác cơ chế nào đi với thứ tự nào, không suy luận chung một kiểu "logic sẽ giống nhau".
- "Giảm desired capacity cùng lúc terminate thủ công" là nguyên nhân phổ biến gây AZ unbalanced mà đề hay dùng làm tình huống mở đầu.

#### Quy tắc nhớ cho thi

- **Thấy "unhealthy instance"** → **Terminate TRƯỚC, Launch SAU** (2 activity tách biệt)
- **Thấy "AZ rebalancing / unbalanced"** → **Launch TRƯỚC, Terminate SAU** (để không giảm availability)
- **Thấy "terminate + launch đồng thời trong 1 activity"** → luôn là **distractor bịa**, ASG không hoạt động theo kiểu này

### TD explanation

Correct options:

As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application

Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. You create collections of EC2 instances, called Auto Scaling groups. You can specify the minimum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below this size.

Actions such as changing the Availability Zones for your group or explicitly terminating or detaching instances and decrement the desired capacity at the same time, it can lead to the Auto Scaling group becoming unbalanced between Availability Zones. Amazon EC2 Auto Scaling compensates by rebalancing the Availability Zones.

When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that rebalancing does not compromise the performance or availability of your application. Therefore, this option is correct.

Availability Zone Rebalancing Overview:

via - https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html

Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance

However, the scaling activity of Auto Scaling works in a different sequence compared to the rebalancing activity. Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. Later, another scaling activity launches a new instance to replace the terminated instance.

Incorrect options:

Amazon EC2 Auto Scaling creates a new scaling activity for launching a new instance to replace the unhealthy instance. Later, EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it - This option contradicts the correct sequence of events outlined earlier for scaling activity created by EC2 Auto Scaling. Actually, Auto Scaling first terminates the unhealthy instance and then launches a new instance. Hence this is incorrect.

As the Availability Zones got unbalanced, Amazon EC2 Auto Scaling will compensate by rebalancing the Availability Zones. When rebalancing, Amazon EC2 Auto Scaling terminates old instances before launching new instances, so that rebalancing does not cause extra instances to be launched - This option contradicts the correct sequence of events outlined earlier for rebalancing activity. When rebalancing, Amazon EC2 Auto Scaling launches new instances before terminating the old ones. Hence this is incorrect.

Amazon EC2 Auto Scaling creates a new scaling activity to terminate the unhealthy instance and launch the new instance simultaneously - This is a made-up option as both the terminate and launch activities can't happen simultaneously. This option has been added as a distractor.

References:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/common-scenarios-termination.html#common-scenarios-termination-rebalancing

https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-unhealthy-instance.html

</details>
