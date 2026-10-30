# Neal Exam C — 35 questions (2026-10-30) — Wrong Answer Review (10 questions)

Source: `sap-neal-exam-c-2026-10-300938-results.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `neal_c_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q5](#q5) | ☐ | ☐ | ☐ |
| A | [Q7](#q7) | ☐ | ☐ | ☐ |
| A | [Q13](#q13) | ☐ | ☐ | ☐ |
| B | [Q9](#q9) | ☐ | ☐ | ☐ |
| B | [Q12](#q12) | ☐ | ☐ | ☐ |
| B | [Q19](#q19) | ☐ | ☐ | ☐ |
| B | [Q30](#q30) | ☐ | ☐ | ☐ |
| C | [Q11](#q11) | ☐ | ☐ | ☐ |
| C | [Q20](#q20) | ☐ | ☐ | ☐ |
| C | [Q31](#q31) | ☐ | ☐ | ☐ |

---

# Group A — Over-built: added a component the stem never asked for (Multi-AZ, cache, DAX) (3)

<a id="q5"></a>

## Q5

<!-- source: T4Q13 · domain: MIG · time: 2:49 · first: 8:02 · visits: 2 · changes: 1 -->



A Solutions Architect has been tasked with migrating an application to AWS. The application includes a desktop client application and web application. The web application has an uptime SLA of 99.5%. The Solutions Architect must re-architect the application to meet or exceed this SLA.
The application contains a MySQL database running on a single virtual machine. The web application uses multiple virtual machines with a load balancer. Remote users complain about slow load times while using this latency-sensitive application.
The Solutions Architect must minimize changes to the application whilst improving the user experience, minimizing costs, and ensuring the availability requirements are met. Which solutions best meets these requirements?

- **A.** Migrate the database to a MySQL database in Amazon EC2. Host the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Allocate an Amazon WorkSpaces WorkSpace for each end user to improve the user experience.
- **B.** Migrate the database to an Amazon RDS Aurora MySQL configuration. Host the web application on an Auto Scaling configuration of Amazon EC2 instances behind an Application Load Balancer. Use Amazon AppStream 2.0 to improve the user experience.
- **C.** Migrate the database to an Amazon EMR cluster with at least two nodes. Deploy the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Use Amazon CloudFront to improve the user experience.
- **D.** Migrate the database to an Amazon RDS MySQL Multi-AZ configuration. Host the web application on automatically scaled AWS Fargate containers behind a Network Load Balancer. Use Amazon ElastiCache to improve the user experience.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** uptime SLA 99.5%, minimize changes, minimize costs, desktop client, remote users slow, latency-sensitive

🪤 **Your trap:** 🔁 First pick B was right; changed to D. RDS single-AZ already meets 99.5%, so Multi-AZ only adds cost; ElastiCache does not fix a slow remote desktop client. AppStream 2.0 streams the desktop app.

🧠 **Rule:** Match the SLA, do not exceed it at extra cost. Slow desktop client for remote users = AppStream 2.0 (app streaming); WorkSpaces = full desktop.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Remote users (xa, mạng chậm)
   │
   ├── Desktop client app  ──► chậm, "latency-sensitive"
   └── Web app
          │
          ▼
   Load Balancer ──► nhiều VM web
                          │
                          ▼
                 MySQL trên 1 VM duy nhất

Yêu cầu:
  • uptime SLA 99.5%  → ĐẠT hoặc vượt, không cần hơn
  • minimize changes
  • minimize costs
  • cải thiện trải nghiệm remote user
```

Đề có **bốn ràng buộc cùng lúc**: SLA 99.5%, ít thay đổi, chi phí thấp, sửa trải nghiệm desktop client. Đáp án đúng: **B (Aurora MySQL + EC2 Auto Scaling + ALB + AppStream 2.0)**. Anh chọn **D**, nhưng lượt đầu Anh đã chọn B rồi đổi sang D.

#### Vì sao B đúng

| Thành phần | Trong B | Khớp yêu cầu nào |
|---|---|---|
| Database | Amazon RDS Aurora MySQL | Managed, tương thích MySQL → ít đổi code; TD: SLA của RDS là 99.5% → đủ |
| Web tier | EC2 Auto Scaling + ALB | Gần nhất với "nhiều VM + load balancer" hiện tại → minimize changes |
| Trải nghiệm | Amazon AppStream 2.0 | Stream desktop app từ AWS → user xa không phải chạy client nặng qua mạng chậm |

**AppStream 2.0** là dịch vụ **application streaming** (non-persistent): ứng dụng desktop chạy trên VM trong AWS, user chỉ nhận luồng hình ảnh; mỗi phiên tự điều chỉnh theo điều kiện mạng. Đây là cách duy nhất trong 4 option thực sự sửa vấn đề "desktop client chậm với remote users".

#### Vì sao D (Anh chọn) sai — over-built

D thêm những thứ đề **không hỏi**:

```
D = RDS MySQL Multi-AZ   → vượt SLA 99.5%, tốn thêm tiền standby  (trái "minimize costs")
  + Fargate containers   → phải container hóa app                (trái "minimize changes")
  + Network Load Balancer→ Layer 4, đổi kiểu LB không cần thiết
  + ElastiCache          → chỉ tăng tốc truy vấn DB              (KHÔNG sửa desktop client)
```

- **Multi-AZ:** TD nói rõ SLA của RDS đã là 99.5% → thêm Multi-AZ chỉ làm tăng chi phí. Đề yêu cầu "meet or exceed" nhưng kèm "minimize costs" → chọn mức vừa đủ.
- **ElastiCache:** TD: "ElastiCache will just improve database query performance". Vấn đề là client desktop chạy ở xa, không phải DB chậm.

D trông "an toàn hơn" vì có chữ Multi-AZ và cache, nhưng mỗi component thêm vào đều vi phạm một ràng buộc chi phí/thay đổi, và không component nào giải quyết đúng triệu chứng.

#### Các option sai còn lại

- **A:** MySQL tự quản trên EC2 thay vì RDS managed; **WorkSpaces** cấp **cả một desktop ảo cho từng user** → nặng và tốn hơn nhu cầu (chỉ cần stream một app).
- **C:** **EMR** là framework Hadoop/big data analytics, không phải nơi chạy database OLTP MySQL. **CloudFront** tăng tốc nội dung web, không tối ưu được desktop application.

#### WorkSpaces vs AppStream 2.0

| | Amazon WorkSpaces | Amazon AppStream 2.0 |
|---|---|---|
| Cung cấp | Full virtual desktop (DaaS) | Stream **từng ứng dụng** (hoặc desktop) |
| Trạng thái | Persistent, gắn với user | Non-persistent (mặc định) |
| Dùng khi | User cần cả máy làm việc | Cần đưa **một app desktop** đến user ở xa |

> ⚠️ **Lỗi lặp lại (1) — WorkSpaces vs AppStream 2.0:** Anh đã nhầm cặp này ở **Neal B Q34**. Từ khóa "desktop client application" + "remote users slow" → **AppStream 2.0**, không phải WorkSpaces, không phải CloudFront.

> ⚠️ **Lỗi lặp lại (2) — Đổi đáp án đúng khi không có bằng chứng mới:** Lượt đầu Anh chọn B (đúng) rồi đổi sang D. Lỗi này đã xảy ra ở **Udemy #2 Q11/Q67**. Câu single-answer: chỉ đổi khi tìm được **một từ khóa cụ thể trong đề** mà lựa chọn đầu vi phạm. "Multi-AZ nghe an toàn hơn" không phải bằng chứng — đề còn yêu cầu minimize costs.

#### Lưu ý thực tế

- Aurora lưu storage phân tán nhiều bản copy qua nhiều AZ ngay cả khi chỉ có một instance → nền tảng availability đã tốt mà không cần thêm replica.
- "Minimize changes" khi lift-and-shift VM → ưu tiên **EC2 + ALB**; container (ECS/Fargate) là re-platform, nhiều thay đổi hơn.

#### Quy tắc nhớ cho thi

- **Thấy "SLA X%" + "minimize costs"** → chọn mức **vừa đủ** SLA; Multi-AZ/multi-Region khi không cần = over-built
- **Thấy "desktop application" + "remote users slow"** → **AppStream 2.0**
- **Thấy "mỗi user cần full desktop"** → **WorkSpaces**
- **Thấy ElastiCache/DAX** → chỉ sửa **DB read latency**, không sửa client ở xa
- **Thấy EMR làm OLTP database** → loại ngay
- **Mẹo chống đổi đáp án:** "Không có từ khóa mới → giữ lựa chọn đầu"

### TD explanation

The uptime SLA for Amazon RDS is 99.5%. Therefore, it is not necessary to add a Multi-AZ configuration which will increase the solution cost. For the compute layer this could be containers or EC2 instances. To minimize changes to the application using EC2 instances may be slightly easier, but could work. To solve the user experience issues Amazon AppStream 2.0 should be used.
Amazon AppStream 2.0 is a fully managed non-persistent application and desktop streaming service. You centrally manage your desktop applications on AppStream 2.0 and securely deliver them to any computer. Each end user has a fluid and responsive experience because applications run on virtual machines optimized for specific use cases and each streaming sessions automatically adjust to network conditions.
CORRECT:
"Migrate the database to an Amazon RDS Aurora MySQL configuration. Host the web application on an Auto Scaling configuration of Amazon EC2 instances behind an Application Load Balancer. Use Amazon AppStream 2.0 to improve the user experience" is the correct answer.
INCORRECT:
"Migrate the database to a MySQL database in Amazon EC2. Host the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Allocate an Amazon WorkSpaces WorkSpace for each end user to improve the user experience" is incorrect. An RDS managed service would be better for the database and AppStream 2.0 is a better fit for an optimized desktop application.
INCORRECT:
"Migrate the database to an Amazon EMR cluster with at least two nodes. Deploy the web application on automatically scaled Amazon ECS containers behind an Application Load Balancer. Use Amazon CloudFront to improve the user experience" is incorrect. EMR is a hosted Hadoop framework for running analytics on big data and is not suitable for this workload. CloudFront is not well suited to optimizing performance for desktop applications.
INCORRECT:
"Migrate the database to an Amazon RDS MySQL Multi-AZ configuration. Host the web application on automatically scaled AWS Fargate containers behind a Network Load Balancer. Use Amazon ElastiCache to improve the user experience" is incorrect. AppStream 2.0 is a better fit for the desktop application. ElastiCache will just improve database query performance.
References:
https://aws.amazon.com/rds/sla/
https://aws.amazon.com/appstream2/
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-front-end-web-and-mobile-sap/
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-database-sap/

</details>

<a id="q7"></a>

## Q7

<!-- source: T3Q9 · domain: CI · time: 2:32 · first: 12:18 · visits: 1 · changes: 0 -->



A company uses Amazon DynamoDB as the backend for the development environment of a new serverless application. While benchmarking the load, they have configured the RCU and WCU for DynamoDB based on the maximum anticipated load for peak usage.
Peak usage runs over several hours each weekend and is twice the usual load across the week. Within this duration, write operations are significant and take up most of the traffic.
The company must optimize the cost of running the application before releasing to production. Which solution will meet these requirements?

- **A.** Purchase reserved RCU and WCU for the DynamoDB table and use AWS Application Auto scaling to match the increased load during the peak usage period.
- **B.** Configure on-demand capacity mode for the table to enable pay-per-request pricing for read and write requests.
- **C.** Reduce the provisioned read capacity to match the new peak load on the table and configure DynamoDB Accelerator (DAX) in front of the table.
- **D.** Configure on-demand capacity mode for the table and configure DynamoDB Accelerator (DAX) in front of the table.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** DynamoDB dev environment, provisioned for peak, weekend peak 2x, write-heavy, optimize cost before production

🪤 **Your trap:** 🔁 Picked on-demand + DAX. DAX caches reads only; the peak is write-heavy and there is no hot data, so DAX is pure extra cost.

🧠 **Rule:** Dev / spiky / unknown traffic = on-demand capacity. DAX only for read-heavy hot keys; it never helps writes.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
DynamoDB table (môi trường DEV)
  Provisioned RCU/WCU = theo PEAK tối đa  ──► trả tiền cho peak 24/7

Tải theo tuần:
  Mon ─────────────── Fri   Sat─Sun
  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁   ▃▃▃▃ (peak = 2x, vài giờ)
                            └─ chủ yếu là WRITE

Yêu cầu: optimize cost trước khi lên production
```

Vấn đề cốt lõi: đang **trả tiền cho capacity peak suốt cả tuần**, trong khi peak chỉ vài giờ cuối tuần. Đáp án đúng: **B (on-demand capacity mode)**. Anh chọn **D (on-demand + DAX)** — đúng một nửa, nhưng thêm DAX là thành phần đề không cần.

#### Vì sao B đúng

TD giải thích:

- **Provisioned (kể cả có Auto Scaling):** về bản chất Anh trả tiền cho throughput **24/7**.
- **On-demand:** không cần lập kế hoạch throughput, table tự scale phía sau, **trả theo từng request** read/write.
- Với **ứng dụng đang development** hoặc traffic thấp/không đều → on-demand thường kinh tế hơn. Khi traffic đã ổn định ở quy mô lớn thì cán cân có thể đổi.

Đề đúng kiểu này: dev environment + peak ngắn + đang over-provision theo peak → **on-demand**.

#### Vì sao D (Anh chọn) sai — DAX là đồ thừa

```
          Read  ──► DAX (cache hit → không chạm table)
App ──►
          Write ──► DAX ──► DynamoDB (write-through, VẪN ghi xuống table)
```

- **DAX là cache cho READ.** Write đi qua DAX vẫn phải ghi xuống DynamoDB → **không giảm được chi phí write**.
- Peak của đề là **write-heavy** → DAX không đụng tới phần tốn tiền.
- TD: đề không nói gì về **repeated load / hot data** → caching không phù hợp.
- DAX là **cluster tính tiền theo node** chạy liên tục → thêm DAX vào bài toán "optimize cost" là **tăng** chi phí.

D = B + một component đề không hỏi → over-built.

#### Các option sai còn lại

- **A (reserved capacity + Application Auto Scaling):** reserved capacity là cam kết dài hạn cho **provisioned** mode — không hợp với môi trường dev chưa rõ pattern. TD: auto scaling vẫn có thể không kịp với spike rất nhanh, và vẫn là mô hình trả cho throughput liên tục.
- **C (giảm RCU + DAX):** giảm **read** capacity trong khi peak là **write** → sai trục; thêm DAX cũng chỉ giúp read.

| Option | Sửa đúng vấn đề (trả tiền peak 24/7)? | Giúp write-heavy? | Thêm chi phí thừa? |
|---|---|---|---|
| **B. On-demand** | Có | Có (trả theo request) | Không |
| D. On-demand + DAX | Có | DAX không giúp | DAX cluster |
| A. Reserved + Auto Scaling | Một phần | Phải scale kịp | Cam kết dài hạn |
| C. Giảm RCU + DAX | Không | Không | DAX cluster |

> ⚠️ **Lỗi lặp lại — dùng DAX sai chỗ:** Anh đã gặp đúng lỗi này ở **Official exam Q68** (DAX + Savings Plans). Hai lần cùng một pattern: thấy DynamoDB + "cost/performance" là thêm DAX. Phải kiểm tra **read hay write** và **có hot data lặp lại không** trước khi nghĩ tới DAX.

#### Lưu ý thực tế

- DAX chỉ có lợi khi workload **read-heavy**, đọc lặp lại cùng key, cần độ trễ microsecond, và chấp nhận eventually consistent reads.
- On-demand có thể chuyển qua lại với provisioned (có giới hạn tần suất chuyển) → dev dùng on-demand, khi production ổn định có thể cân nhắc lại provisioned + auto scaling.

#### Quy tắc nhớ cho thi

- **Thấy "development" / "unpredictable" / "spiky" / "provisioned for peak" + cost** → **DynamoDB on-demand**
- **Thấy "write-heavy"** → **loại DAX** (DAX không giảm write)
- **Thấy DAX** → chỉ chọn khi đề nói **read-heavy + hot keys + microsecond latency**
- **Thấy "reserved capacity" cho dev/chưa rõ pattern** → sai, cam kết dài hạn
- **Mnemonic:** "DAX chỉ cache **Đọc**, Ghi vẫn trả tiền đủ"

### TD explanation

With a manually set scaling policy, you can set the upper and low limits of the scaling. So, for example, you could set it at a minimum of 1 and a max of 20 read capacity. This would mean that no matter what you would always have at least 1 read capacity but never more than 20.
So now if you receive that same spike but have the max throughput to 20, DynamoDB will throttle those requests and prevent you from going over your max auto scaled threshold.
With On-Demand Scaling you don't need to think about provisioning throughput. Instead, your table will scale all behind the scenes automatically. Extreme spikes in load can occur and be handled seamlessly by AWS. This also brings a change in the cost structure for DynamoDB. With On-Demand Scaling, instead of paying for provisioned throughput, you pay per read or write request.
Remember for Provisioned with Auto-Scaling you are basically paying for throughput 24/7. Whereas for On-Demand Scaling you pay per request. This means for applications still in development or low traffic applications, it might be more economical to use On-Demand Scaling and not worry about provisioning throughput. However, at scale, this can quickly shift once you have a more consistent usage pattern.
CORRECT:
"Configure on-demand capacity mode for the table to enable pay-per-request pricing for read and write requests" is the correct answer (as explained above.)
INCORRECT:
"Purchase reserved RCU and WCU for the DynamoDB table and use AWS Application Auto scaling to match the increased load during the peak usage period" is incorrect.
This is a close option however extremely rapid spikes in load could still occur faster than the table could scale.
INCORRECT:
"Reduce the provisioned read capacity to match the new peak load on the table and configure DynamoDB Accelerator (DAX) in front of the table" is incorrect.
The question doesn’t ask about repeated load, hence caching isn’t appropriate in this case.
INCORRECT:
" Configure on-demand capacity mode for the table and configure DynamoDB Accelerator (DAX) in front of the table" is incorrect.
As mentioned above, since the application doesn’t have repeated load or hot data, caching isn’t appropriate in this case.
References:
https://aws.amazon.com/blogs/aws/amazon-dynamodb-on-demand-no-capacity-planning-and-pay-per-request-pricing/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-dynamodb/

</details>

<a id="q13"></a>

## Q13

<!-- source: T1Q12 · domain: CI · time: 3:18 · first: 73:42 · visits: 3 · changes: 1 -->



A company has deployed an eCommerce application that is used by thousands of customers to place online orders. The application runs on Amazon ECS tasks behind an Application Load Balancer (ALB) and data is stored in an Amazon DynamoDB table.
The application has recently experienced attacks that caused application slowdowns and outages. The company must prevent attacks and ensure business continuity with minimal service interruptions.
Which combination of steps will meet these requirements MOST cost-effectively? (Select TWO.)

- **A.** Create an Amazon CloudFront distribution with the ALB as the origin and configure a custom header and secret value. Configure the ALB to conditionally forward traffic only if the header and value match.
- **B.** Deploy the application in two AWS Regions. Configure Amazon Route 53 to route to both Regions with equal weight.
- **C.** Configure AWS Auto Scaling for Amazon ECS tasks. Create an Amazon DynamoDB Accelerator (DAX) cluster in front of the DynamoDB table.
- **D.** Configure AWS Auto Scaling for Amazon ECS tasks. Configure an Amazon ElastiCache cluster in front of the DynamoDB table.
- **E.** Deploy an AWS WAF web ACL that includes a rule group that blocks the attack traffic. Associate the web ACL with the Amazon CloudFront distribution.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E · **You picked:** A, C

🔑 **Key words:** ECS behind ALB, attacks caused slowdowns and outages, prevent attacks, MOST cost-effective, Select TWO

🪤 **Your trap:** 🔁 Picked auto scaling + DAX; that absorbs load but does not stop attacks. Needed WAF on CloudFront plus the custom-header lock so attackers cannot bypass to the ALB.

🧠 **Rule:** Prevent web attacks = CloudFront (Shield Standard) + WAF web ACL + origin lock (custom header on ALB). Scaling and caching treat symptoms.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                 Attackers ─────────────┐ (bypass thẳng vào ALB?)
                                        │
Users ──► CloudFront ──► AWS WAF        ▼
          (Shield Std)   web ACL ──► ALB (public) ──► ECS tasks ──► DynamoDB
                                     chỉ forward nếu
                                     header bí mật khớp

Yêu cầu: PREVENT attacks + business continuity, MOST cost-effective (Select TWO)
```

Đề bị **tấn công** gây chậm và outage → cần **chặn** tấn công, không phải "chịu đựng" tấn công. Đáp án đúng: **A (CloudFront + custom header lock ALB)** + **E (WAF web ACL trên CloudFront)**. Anh chọn **A, C** — đúng A, sai ở C (Auto Scaling + DAX).

#### A + E tạo thành MỘT giải pháp

**E — WAF chặn traffic tấn công:** CloudFront có sẵn **AWS Shield Standard** chống DDoS cơ bản. Với tấn công web độc hại, gắn **AWS WAF web ACL** có **rule group** phù hợp vào distribution → request xấu bị chặn ngay ở edge, không tới ALB.

**A — Khóa origin để không ai vòng qua CloudFront:**

```
CloudFront  ──(thêm header X-Origin-Secret: <giá trị bí mật>)──► ALB
                                                                  │
ALB listener rule:  header khớp?  ── Có ──► forward tới ECS
                                  └─ Không ─► trả lỗi cố định (vd 403)
```

ALB vẫn là public, nên nếu không có A, attacker chỉ cần gọi thẳng DNS của ALB là **bỏ qua cả WAF lẫn Shield ở edge**. A và E bổ trợ nhau: thiếu A thì E bị bypass; thiếu E thì A chỉ ép traffic qua CloudFront mà không lọc gì.

#### Vì sao C (Anh chọn) sai — chữa triệu chứng

- **Auto Scaling ECS:** thêm task để **hấp thụ** tải tấn công → traffic xấu vẫn vào tới app, và Anh trả tiền cho compute phục vụ attacker. Trái với "prevent" và "cost-effective".
- **DAX:** TD: DAX có thể tăng hiệu năng khi cache request nhưng **không ngăn tấn công** tới ALB hay app server. DAX còn là cluster tính phí thêm.

C trông hợp lý vì đề nói "slowdowns" — nhưng slowdown là **hậu quả**; gốc rễ là traffic tấn công.

#### Các option sai còn lại

- **B (2 Region + Route 53 weighted):** nhân đôi cả stack → **không cost-effective**; tấn công vẫn đánh vào cả hai Region.
- **D (Auto Scaling + ElastiCache):** cùng lỗi với C — không giảm được tác động của tấn công.

| Option | Chặn tấn công? | Chống bypass? | Chi phí |
|---|---|---|---|
| **A. CloudFront + header lock** | Đưa traffic qua edge (Shield Std) | Có | Thấp |
| **E. WAF web ACL** | Có (rule group) | Cần A đi kèm | Thấp |
| B. Multi-Region | Không | Không | Rất cao (2 stack) |
| C. Scaling + DAX | Không (chỉ hấp thụ) | Không | Tăng theo tấn công |
| D. Scaling + ElastiCache | Không (chỉ hấp thụ) | Không | Tăng theo tấn công |

> ⚠️ **Lỗi lặp lại — WAF/CloudFront/Shield:** Anh đã sai nhóm này ở **Neal B Q22**. Pattern chung: đề có "attack / malicious traffic / DDoS" → lớp bảo vệ là **CloudFront + Shield + WAF ở edge** và **khóa origin**. Scaling/caching không bao giờ là câu trả lời cho "prevent attacks".

#### Lưu ý thực tế

- Giá trị header bí mật nên được **xoay vòng** định kỳ (cập nhật cả CloudFront origin custom header và ALB rule).
- Một lớp khóa origin bổ sung thường gặp: Security Group của ALB chỉ cho phép **AWS-managed prefix list của CloudFront** (origin-facing). Đề này dùng custom header — giữ đáp án A.
- WAF có **rate-based rule** để giới hạn số request theo IP — hữu ích cho flood ở layer 7.
- Cần chống DDoS nâng cao + hỗ trợ đội SRT + bảo vệ chi phí khi scale do tấn công → **Shield Advanced** (đắt; đề "most cost-effective" thì không chọn trừ khi được hỏi).

#### Quy tắc nhớ cho thi

- **Thấy "attacks" / "malicious requests" trên web app** → **CloudFront + AWS WAF web ACL** (Shield Standard đi kèm miễn phí)
- **Thấy "ALB public" + CloudFront phía trước** → **custom header bí mật + ALB listener rule** (hoặc SG với CloudFront prefix list)
- **Thấy Auto Scaling / DAX / ElastiCache trong câu hỏi về tấn công** → chữa triệu chứng, loại
- **Thấy multi-Region + "cost-effective"** → thường loại
- **Mnemonic:** "**Chặn ở cửa, khóa cửa sau**" — WAF chặn ở edge, header khóa đường vào ALB

### TD explanation

Amazon CloudFront comes with AWS Shield standard by default which will provide some protection against DDoS attacks. For malicious web attacks an AWS WAF ACL should be associated with the distribution so that it can protect against the attacks using an appropriate rule group.
In this configuration it is important to ensure that the attacks cannot circumvent CloudFront and connect directly to the public ALB. For this, we can create a custom header and secret value in CloudFront. This will be forwarded in requests that originate from CloudFront. The ALB can conditionally forward only if this HTTP header information is present in the request.
CORRECT:
"Create an Amazon CloudFront distribution with the ALB as the origin and configure a custom header and secret value. Configure the ALB to conditionally forward traffic only if the header and value match" is a correct answer (as explained above.)
CORRECT:
"Deploy an AWS WAF web ACL that includes a rule group that blocks the attack traffic. Associate the web ACL with the Amazon CloudFront distribution" is also a correct answer (as explained above.)
INCORRECT:
"Deploy the application in two AWS Regions. Configure Amazon Route 53 to route to both Regions with equal weight" is incorrect. This is not the most cost-effective option as the entire application stack is deployed in two Regions.
INCORRECT:
"Configure AWS Auto Scaling for Amazon ECS tasks. Create an Amazon DynamoDB Accelerator (DAX) cluster in front of the DynamoDB table" is incorrect. DAX may assist with performance when caching requests but doesn’t help with preventing web attacks from reaching the ALB or application servers.
INCORRECT:
"Configure AWS Auto Scaling for Amazon ECS tasks. Configure an Amazon ElastiCache cluster in front of the DynamoDB table" is incorrect. As with the previous answer this solution does not assist with mitigating the impact of the attacks.
References:
https://aws.amazon.com/premiumsupport/knowledge-center/elb-route-traffic-custom-http-header/
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-waf-shield/

</details>

---

# Group B — Security mechanism mismatch: right goal, wrong control or layer (SG, ACL, key type, NLB source IP) (4)

<a id="q9"></a>

## Q9

<!-- source: T5Q1 · domain: CI · time: 2:09 · first: 15:50 · visits: 2 · changes: 0 -->



A company has a security policy that requires that all internal application connectivity must use private IP addresses. A Solutions Architect has created interface endpoints in private subnets to connect to AWS public services. The Solutions Architect tested the configuration and the connectivity failed.
Which configuration change should the Solutions Architect make to resolve the issue?

- **A.** Update the route table for the subnets with a route to the interface endpoint.
- **B.** Enable the private DNS option on the VPC attributes.
- **C.** Configure the security group on the interface endpoint to allow connectivity to the AWS services.
- **D.** Configure an Amazon Route 53 private hosted zone with a conditional forwarder for the internal application.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** interface endpoints in private subnets, private IPs only, connectivity failed, configuration change

🪤 **Your trap:** Picked a route table entry; interface endpoints are ENIs reached through DNS, not routes. Gateway endpoints (S3/DynamoDB) are the ones that use route tables.

🧠 **Rule:** Interface endpoint fails = check the endpoint ENI security group (allow 443 from the VPC) and private DNS. Route table entries = gateway endpoints only.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC
┌──────────────────────────────────────────────────────────┐
│  Private subnet                                          │
│  ┌──────────┐   HTTPS 443   ┌──────────────────────────┐ │
│  │ EC2 app  │ ────────────► │ Interface endpoint (ENI) │ │──► AWS service
│  └──────────┘               │ IP private + SG riêng    │ │    (PrivateLink)
│                             └──────────────────────────┘ │
│  DNS: ec2.us-east-1.amazonaws.com → IP private của ENI   │
└──────────────────────────────────────────────────────────┘
        Yêu cầu: chỉ dùng private IP. Đã tạo endpoint, test FAIL
```

Câu hỏi: **thay đổi cấu hình nào** để kết nối chạy được. Đáp án đúng: **C (security group trên interface endpoint)**. Anh chọn **A (thêm route vào route table)**.

#### Vì sao C đúng

Interface endpoint thực chất là **một hoặc nhiều ENI** đặt trong subnet của Anh, mỗi ENI có IP private và **gắn security group**. Traffic từ EC2 đến endpoint là traffic **trong cùng VPC, đến một ENI** → bị SG của ENI đó lọc như mọi ENI khác.

- Nếu SG của endpoint không cho phép inbound (thường là **TCP 443** từ CIDR của VPC hoặc từ SG của app) → gói tin bị chặn → "connectivity failed".
- TD explanation nói rõ: phải đảm bảo SG gắn vào endpoint network interface cho phép giao tiếp giữa ENI đó và các resource trong VPC.

Đây là lỗi phổ biến nhất khi một interface endpoint "đã tạo nhưng không chạy".

#### Vì sao A (Anh chọn) sai

A nghe hợp lý vì Anh nghĩ "muốn đi đến đâu thì phải có route". Nhưng:

- Interface endpoint **không cần route table**. ENI nằm ngay trong subnet → đã thuộc dải **local route** của VPC (`10.0.0.0/16 → local`).
- Cơ chế "dẫn đường" của interface endpoint là **DNS**: private DNS trả tên dịch vụ mặc định về IP private của ENI.
- **Gateway endpoint** (chỉ S3 và DynamoDB) mới là loại thêm entry vào **route table** (dùng prefix list làm đích).

Anh đã lẫn hai loại endpoint — đúng mục tiêu (đi qua private), sai cơ chế.

#### Các lựa chọn khác

- **B sai:** private DNS **mặc định đã bật** cho endpoint của AWS service. Hơn nữa, đây là option **trên endpoint**, không phải "VPC attribute" (VPC attributes là `enableDnsSupport` / `enableDnsHostnames`, cũng cần bật để private DNS hoạt động, nhưng đề không nói gì cho thấy chúng bị tắt).
- **D sai:** không cần tự tạo Route 53 private hosted zone hay conditional forwarder — khi private DNS bật, AWS tự gắn một private hosted zone (do AWS quản lý) vào VPC. Conditional forwarder là chuyện DNS hybrid on-premises, không liên quan.

#### So sánh hai loại VPC endpoint

| Tiêu chí | **Interface endpoint** | Gateway endpoint |
|---|---|---|
| Bản chất | ENI có IP private trong subnet (PrivateLink) | Đích trong route table |
| Dịch vụ hỗ trợ | Phần lớn AWS service, Marketplace, endpoint service riêng | **Chỉ S3 và DynamoDB** |
| Cách dẫn traffic | **DNS** (private DNS / tên endpoint-specific) | **Route table** (prefix list) |
| Security group | **Có**, gắn trên ENI | Không có |
| Kiểm soát truy cập | SG + endpoint policy | Endpoint policy |
| Truy cập từ on-prem (VPN/DX) | Được | Không |
| Chi phí | Tính phí theo giờ + data | Không tính phí |

#### Lưu ý thực tế

- Checklist khi interface endpoint không chạy: **(1) SG của endpoint cho phép 443 từ client**, (2) private DNS bật trên endpoint, (3) VPC bật `enableDnsSupport` + `enableDnsHostnames`, (4) endpoint policy không chặn, (5) NACL của subnet.
- S3 có **cả hai** loại endpoint. Thấy "on-premises truy cập S3 qua DX/VPN bằng private IP" → S3 **interface** endpoint; thấy "EC2 trong VPC truy cập S3, rẻ nhất" → **gateway** endpoint.

#### Quy tắc nhớ cho thi

- **Thấy "interface endpoint" + "connectivity failed"** → **kiểm tra SG trên endpoint ENI** (rồi đến private DNS)
- **Thấy "route table" + endpoint** → chỉ đúng với **gateway endpoint (S3/DynamoDB)**
- **Thấy "enable private DNS"** cho AWS service → thường là bẫy, vì mặc định đã bật
- Mẹo nhớ: **Interface = ENI = SG + DNS**; **Gateway = Route**

### TD explanation

You must ensure that the security group that's associated with the endpoint network interface allows communication between the endpoint network interface and the resources in your VPC that communicate with the service.
When you create an interface endpoint, endpoint-specific DNS hostnames are generated. For AWS services and AWS Marketplace Partner services, the private DNS option (enabled by default) associates a private hosted zone with your VPC.
The hosted zone contains a record set for the default DNS name for the service (for example, ec2.us-east-1.amazonaws.com) that resolves to the private IP addresses of the endpoint network interfaces in your VPC. This enables you to make requests to the service using its default DNS hostname instead of the endpoint-specific DNS hostnames.
With Private DNS enabled on the endpoint, instances can send requests AWS services through the interface endpoint using either the default DNS hostname or the endpoint-specific DNS hostname.
CORRECT:
"Configure the security group on the interface endpoint to allow connectivity to the AWS services" is the correct answer.
INCORRECT:
"Enable the private DNS option on the VPC attributes" is incorrect. Private DNS is enabled by default for endpoints created for AWS services and AWS Marketplace Partner services.
INCORRECT:
"Update the route table for the subnets with a route to the interface endpoint" is incorrect. You do not need to update the route table for interface endpoints.
INCORRECT:
"Configure an Amazon Route 53 private hosted zone with a conditional forwarder for the internal application" is incorrect. This is unnecessary, a private hosted zone is a private hosted zone is associated with the VPC by default when the private DNS option is enabled (which is a default).
References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html
https://docs.aws.amazon.com/vpc/latest/userguide/verify-domains.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-networking-content-delivery-sap/

</details>

<a id="q12"></a>

## Q12

<!-- source: T4Q5 · domain: NEW · time: 3:03 · first: 70:14 · visits: 2 · changes: 4 -->



A media publishing company has created an online bookstore which gives users access to books and other reference material. These materials can be downloaded by users and new materials can also be uploaded on the portal. According to company requirements, all data must be encrypted in transit and at rest. A solutions architect is building the solution by using Amazon S3 and Amazon CloudFront.
Which combination of steps will meet the encryption requirements? (Select THREE.)

- **A.** Turn on the S3 server-side encryption for the S3 bucket in use.
- **B.** For the read and write operations in the S3 ACLs, add condition "aws:SecureTransport": "true".
- **C.** Create a bucket policy that denies any unencrypted operations in the S3 bucket that the web application uses.
- **D.** Configure encryption at rest on CloudFront by using server-side encryption with AWS KMS keys (SSE-KMS).
- **E.** Configure redirection of HTTP requests to HTTPS requests in CloudFront.
- **F.** Use the RequireSSL option in the creation of presigned URLS for the S3 bucket that the web application uses

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, E · **You picked:** A, B, E

🔑 **Key words:** S3 + CloudFront, encrypt in transit and at rest, Select THREE

🪤 **Your trap:** Picked aws:SecureTransport in S3 ACLs; ACLs cannot hold condition keys, only bucket policies can. Missed the bucket policy denying unencrypted uploads.

🧠 **Rule:** At rest = default bucket encryption + bucket policy denying unencrypted PutObject. In transit = CloudFront redirect HTTP to HTTPS. Conditions live in bucket policies, never ACLs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
 User (upload / download)
      │  HTTP hoặc HTTPS
      ▼
 ┌──────────────┐   HTTPS    ┌─────────────────────────────┐
 │  CloudFront  │ ─────────► │  S3 bucket (origin)         │
 │ (edge cache) │            │  sách, tài liệu tham khảo   │
 └──────────────┘            └─────────────────────────────┘
   IN TRANSIT: ép HTTPS         AT REST: mã hóa object trong S3
```

Yêu cầu: **mọi dữ liệu mã hóa cả in transit và at rest**, chọn **BA** bước. Đáp án đúng: **A + C + E**. Anh chọn **A, B, E** → đúng 2/3, sai ở **B** (thay vì C).

#### Ba bước đúng tạo thành MỘT giải pháp

| Bước | Lớp bảo vệ | Vai trò |
|---|---|---|
| **A.** Bật S3 default encryption (SSE-S3 hoặc SSE-KMS) | At rest | Mọi object lưu vào bucket được mã hóa |
| **C.** Bucket policy deny upload không mã hóa | At rest (cưỡng chế) | Chặn PutObject thiếu header `s3:x-amz-server-side-encryption` |
| **E.** CloudFront redirect HTTP → HTTPS | In transit | Viewer gửi HTTP sẽ nhận 301 sang HTTPS |

A đặt mặc định, C là hàng rào cưỡng chế (và có thể ép dùng đúng một KMS key cụ thể, như TD explanation nói), E lo phần đường truyền phía người dùng.

Ví dụ statement của C:

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::bookstore-bucket/*",
  "Condition": {
    "Null": { "s3:x-amz-server-side-encryption": "true" }
  }
}
```

#### Vì sao B (Anh chọn) sai

B có **mục tiêu đúng** (`aws:SecureTransport` đúng là key để ép HTTPS) nhưng đặt **sai chỗ**:

- **S3 ACL không có phần `Condition`.** ACL chỉ là danh sách *grantee + permission* (READ, WRITE, FULL_CONTROL…). Không thể gắn condition key nào vào ACL.
- Condition key như `aws:SecureTransport` chỉ sống trong **policy JSON** — bucket policy, IAM policy, SCP…
- Kể cả nếu đặt đúng vào bucket policy, TD explanation chỉ ra: nó chỉ lo **in transit**, không ép **at rest** — trong khi phần in transit đã có E lo.

Câu này là kiểu "đúng ý tưởng, sai cơ chế": control đúng, layer sai.

#### Các lựa chọn sai khác

- **D sai:** CloudFront **không có** cài đặt kiểu "encryption at rest bằng SSE-KMS" cho distribution. SSE-KMS là tính năng của **S3 origin**; CloudFront chỉ cần quyền (qua OAC) để đọc object SSE-KMS. Dữ liệu at rest phải được mã hóa ở S3.
- **F sai:** presigned URL **không có option RequireSSL**. Presigned URL chỉ gắn access key, thời hạn và chữ ký SigV4 vào query string để cấp quyền tạm; không cấu hình mã hóa được qua nó.

#### Lưu ý thực tế

- Muốn ép HTTPS khi truy cập **trực tiếp S3** → bucket policy **Deny** khi `"aws:SecureTransport": "false"` (đây mới là chỗ đúng cho ý tưởng của B).
- CloudFront có hai chiều: **Viewer protocol policy** (user → CloudFront: Redirect HTTP to HTTPS / HTTPS only) và **Origin protocol policy** (CloudFront → origin). E thuộc chiều viewer.
- Dùng SSE-KMS với CloudFront → origin phải dùng **OAC** và key policy KMS phải cho phép CloudFront dùng key.

📝 Ghi chú kỹ thuật: từ 01/2023, S3 tự động mã hóa mọi object mới bằng SSE-S3 nên "upload không mã hóa" gần như không còn xảy ra. Trong thực tế, policy kiểu C chủ yếu dùng để **ép đúng loại mã hóa** (ví dụ bắt buộc `aws:kms` với một key cụ thể). Đáp án của đề vẫn là A, C, E.

#### Quy tắc nhớ cho thi

- **Thấy condition key (`aws:SecureTransport`, `aws:SourceIp`, `s3:x-amz-server-side-encryption`) gắn với "ACL"** → sai ngay; condition chỉ có trong **policy**
- **Thấy "encrypt at rest" + S3** → **default encryption + bucket policy deny PutObject không mã hóa**
- **Thấy "encrypt in transit" + CloudFront** → **Viewer protocol policy: Redirect HTTP to HTTPS**
- **Thấy "CloudFront SSE-KMS" hoặc "presigned URL RequireSSL"** → tính năng không tồn tại
- Mẹo nhớ: **ACL = ai + quyền gì; Policy = ai + quyền gì + KHI NÀO**

### TD explanation

For object encryption at rest, you can set the default encryption behavior on an Amazon S3 bucket so that all objects are encrypted when they are stored in the bucket. The objects are encrypted using server-side encryption with either Amazon S3-managed keys (SSE-S3) or AWS Key Management Service (AWS KMS) keys.
To deny unencrypted objects, "s3:x-amz-server-side-encryption" can be added which allows only encrypted object upload and can restrict to a specific KMS key as well.
Amazon CloudFront can use 301 response code to redirect HTTP requests to HTTPS and allows only secured traffic.
CORRECT:
"Turn on S3 server-side encryption for the S3 bucket that the web application uses is a correct answer (as explained above.)
CORRECT:
"Create a bucket policy that denies any unencrypted operations in the S3 bucket that the web application uses" is also a correct answer (as explained above.)
CORRECT:
"Configure redirection of HTTP requests to HTTPS requests in CloudFront" is also a correct answer (as explained above.)
INCORRECT:
"For the read and write operations in the S3 ACLs , add condition "aws:SecureTransport": "true"" is incorrect.
To only allow HTTPS requests, set “true” for key "aws:SecureTransport". When this key is true, the request is sent through HTTPS. This option configures encryption in transit and does not enforce encryption at rest.
INCORRECT:
"Configure encryption at rest on CloudFront by using server-side encryption with AWS KMS keys (SSE-KMS)" is incorrect.
The data must be encrypted at rest in the Amazon S3 origin that is the source for the CloudFront distribution. This configuration does not ensure encryption at rest in the S3 bucket.
INCORRECT:
"Use the RequireSSL option in the creation of presigned URLs for the S3 bucket that the web application uses" is incorrect.
Pre-signed URLs are used to provide short-term access to a private object in your S3 bucket. They work by appending an AWS Access Key, expiration time, and Sigv4 signature as query parameters to the S3 object. Encryption cannot be configured through the pre-signed URL.
References:
https://aws.amazon.com/blogs/networking-and-content-delivery/serving-sse-kms-encrypted-content-from-s3-using-cloudfront/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/data-protection-summary.html
https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-s3-and-glacier/

</details>

<a id="q19"></a>

## Q19

<!-- source: T5Q28 · domain: CI · time: 3:42 · first: 34:24 · visits: 2 · changes: 0 -->



A financial company stores personally identifiable information (PII) in an Amazon S3 bucket which currently does not have versioning enabled. The current configuration has server-side encryption with S3 managed encryption keys (SSE-S3) enabled to encrypt the objects. According to a new requirement, all current and future objects in the S3 bucket must be encrypted by keys that the company's security team manages.
Which solution will meet these requirements?

- **A.** Change the default encryption to SSE-S3 with a customer managed key. Use the AWS CLI to re-upload all objects in the S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests.
- **B.** Change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS) in S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests. Use the AWS CLI to re-upload all objects in the S3 bucket.
- **C.** In the S3 bucket properties, change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS). Set an S3 bucket policy to automatically encrypt objects on GetObject and PutObject requests.
- **D.** Change the default encryption to AES-256 with a customer managed key. Attach a policy to deny unencrypted PutObject requests to any entities that access the S3 bucket. Use the AWS CLI to re-upload all objects in the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** PII, SSE-S3 today, keys managed by the security team, current and future objects

🪤 **Your trap:** Picked 'SSE-S3 with a customer managed key'; SSE-S3 keys are always AWS-owned, so that option is impossible.

🧠 **Rule:** Keys the company manages = SSE-KMS with a customer managed key; deny unencrypted PutObject; re-copy existing objects. SSE-S3 never uses your key.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 bucket (PII, KHÔNG versioning)
┌────────────────────────────────────────────┐
│ Hiện tại: SSE-S3  (key do AWS sở hữu)      │
│   object cũ  ── mã hóa bằng key của AWS    │
│   object mới ── ?                          │
└────────────────────────────────────────────┘
   Yêu cầu: object HIỆN TẠI + TƯƠNG LAI đều mã hóa
            bằng key do SECURITY TEAM quản lý
```

Ba ý phải đạt cùng lúc: **(1) key do công ty quản lý**, **(2) object tương lai**, **(3) object hiện có**. Đáp án đúng: **B**. Anh chọn **A**.

#### Vì sao B đúng

B gom đủ cả ba ý thành một giải pháp:

| Thành phần của B | Đáp ứng ý nào |
|---|---|
| Default encryption → **SSE-KMS** (dùng customer managed key) | (1) key do security team quản lý, (2) object mới |
| Bucket policy **deny PutObject không mã hóa** | (2) cưỡng chế, không ai upload lọt |
| **Re-upload / copy lại** toàn bộ object bằng AWS CLI | (3) object cũ |

Điểm mấu chốt: **đổi default encryption không mã hóa lại object cũ** — nó chỉ áp dụng cho object ghi vào từ thời điểm đó. Object cũ phải được **ghi lại** (copy-in-place) thì mới mang key mới.

```
aws s3 cp s3://pii-bucket/ s3://pii-bucket/ --recursive \
    --sse aws:kms --sse-kms-key-id <customer-managed-key-arn>
```

TD explanation cũng nêu lợi ích thêm của KMS: người truy cập cần **cả** quyền S3 **và** quyền dùng KMS key → một bucket policy lỡ mở quá rộng vẫn chưa đủ để đọc dữ liệu.

#### Vì sao A (Anh chọn) sai

A có đủ "bộ khung" (re-upload + deny unencrypted PutObject) nên trông rất giống B. Nhưng phần lõi là **"SSE-S3 with a customer managed key"** — **cấu hình không tồn tại**:

- **SSE-S3** = key do **S3/AWS sở hữu và quản lý hoàn toàn**. Anh không chọn, không xoay vòng, không viết key policy được.
- Muốn "key do công ty quản lý" → phải là **SSE-KMS với customer managed key** (hoặc SSE-C nếu tự giữ key, nhưng đề không hướng tới).

Đúng mục tiêu, sai cơ chế: tên "SSE-S3" đã loại option ngay từ chữ đầu.

#### Các lựa chọn khác

- **C sai:** không có chuyện "mã hóa object khi **GetObject**" — GetObject là tải xuống, S3 giải mã rồi trả về. Bucket policy cũng không "tự động mã hóa" gì; policy chỉ **cho phép/từ chối**. Thêm nữa C **không xử lý object cũ**.
- **D sai:** SSE trong S3 **luôn dùng AES-256**, dù là SSE-S3 hay SSE-KMS. "AES-256 with a customer managed key" là nói về thuật toán, không phải loại quản lý key — lựa chọn thật sự là ai quản lý key.

#### So sánh các kiểu server-side encryption của S3

| Kiểu | Ai quản lý key | Công ty kiểm soát key policy / rotation? | Audit dùng key qua CloudTrail |
|---|---|---|---|
| SSE-S3 | AWS (S3) | Không | Không |
| SSE-KMS (AWS managed `aws/s3`) | AWS quản lý trong KMS | Không | Có |
| **SSE-KMS (customer managed key)** | **Công ty** | **Có** | **Có** |
| SSE-C | Công ty giữ key, gửi kèm mỗi request | Có (ngoài AWS) | Không áp dụng |

📝 Ghi chú kỹ thuật: option B ghi "AWS KMS managed encryption keys" — nếu hiểu theo nghĩa đen là AWS managed key `aws/s3` thì security team **không** thực sự quản lý key. Trong thực tế phải chọn **customer managed key**. Đề dùng "SSE-KMS" như cách nói chung, và B vẫn là đáp án đúng vì là option duy nhất khả thi.

#### Lưu ý thực tế

- Bucket **không bật versioning** → copy-in-place ghi đè luôn, không còn bản cũ mã hóa SSE-S3. Nếu có versioning thì bản cũ vẫn tồn tại dưới dạng noncurrent version.
- Hàng triệu object → dùng **S3 Inventory + S3 Batch Operations (Copy)** thay vì CLI chạy tay.
- Có thể bật **S3 Bucket Key** để giảm số lần gọi KMS (giảm chi phí request KMS).

⚠️ Lỗi lặp lại: liên quan Official exam **Q43** — ở đó Anh cũng vấp đúng điểm "**object đã có không tự được mã hóa lại**" (đáp án: default encryption + S3 Inventory + **S3 Batch Operations** copy-in-place, không cần bucket mới). Mỗi khi đề nói "current **and** future objects", phải thấy **hai** hành động: đổi default cho tương lai **và** copy lại cho hiện tại.

#### Quy tắc nhớ cho thi

- **Thấy "keys managed by the company / security team"** → **SSE-KMS + customer managed key**
- **Thấy "SSE-S3 with customer managed key"** → không tồn tại, loại ngay
- **Thấy "AES-256 with …"** → bẫy thuật toán; mọi SSE của S3 đều AES-256
- **Thấy "existing objects" + đổi encryption** → **re-copy** (CLI cho ít, **Batch Operations** cho nhiều)
- **Thấy "encrypt on GetObject"** → sai, GetObject chỉ đọc/giải mã

### TD explanation

You can configure your bucket to use an S3 Bucket Key for SSE-KMS on new objects by using the Amazon S3 console, REST API, Amazon SDK, Amazon CLI, or Amazon CloudFormation. If you want to enable or disable an S3 Bucket Key for existing objects, you can use a COPY operation.
Switching to AWS KMS from AWS SSE-S3 can provide some additional benefits, including protection from policies that may be overly permissive. For example, adding a bucket policy allowing overly broad access to the data instead of individual users or roles. By implementing encryption using KMS keys, the accessor of the resources would need Amazon S3 policy access and access to a KMS key to decrypt data.
The KMS key is managed by the company. To encrypt existing objects with this key they would need to be uploaded again and this operation can be performed using the AWS CLI.
CORRECT:
"Change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS) in S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests. Use the AWS CLI to re-upload all objects in the S3 bucket" is the correct answer (as explained above.)
INCORRECT:
"In the S3 bucket properties, change the default encryption to SSE-S3 with a customer managed key. Use the AWS CLI to re-upload all objects in the S3 bucket. Set an S3 bucket policy to deny unencrypted PutObject requests" is incorrect.
You cannot manage your own encryption key with SSE-S3.
INCORRECT:
"Change the default encryption to server-side encryption with AWS KMS managed encryption keys (SSE-KMS) in S3 bucket. Set an S3 bucket policy to automatically encrypt objects on GetObject and PutObject requests" is incorrect.
You cannot encrypt using GetObject requests as this is downloading objects and they are first decrypted. The bucket policy should be setup to enforce encryption for PutObject requests only.
INCORRECT:
"Change the default encryption to AES-256 with a customer managed key. Attach a policy to deny unencrypted PutObject requests to any entities that access the S3 bucket. Use the AWS CLI to re-upload all objects in the S3 bucket" is incorrect.
Server-Side Encryption in S3 is always AES256, whether you are using SSE-S3 or SSE-KMS.
When changing the encryption type, we choose among AWS/ S3 managed or customer managed but the algorithm remains the same hence this is also incorrect.
References:
https://docs.amazonaws.cn/en_us/AmazonS3/latest/userguide/replication-config-for-kms-objects.html
https://aws.amazon.com/blogs/storage/changing-your-amazon-s3-encryption-from-s3-managed-encryption-sse-s3-to-aws-key-management-service-sse-kms/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-s3-and-glacier/

</details>

<a id="q30"></a>

## Q30

<!-- source: T2Q10 · domain: CI · time: 1:31 · first: 50:24 · visits: 1 · changes: 1 -->



A Solutions Architect has deployed an application on Amazon EC2 instances in a private subnet behind a Network Load Balancer (NLB) in a public subnet. Customers have attempted to connect from their office location and are unable to access the application. The targets were registered by instance-id and are all healthy in the associated target group.
What step should the Solutions Architect take to resolve the issue and enable access for the customers?

- **A.** Check the security group for the EC2 instances to ensure it allows ingress from the NLB subnets.
- **B.** Check the security group for the EC2 instances to ensure it allows ingress from the customer office.
- **C.** Check the security group for the NLB to ensure it allows ingress from the EC2 instances’ security group.
- **D.** Check the security group for the NLB to ensure it allows ingress from the NLB elastic IP addresses.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** NLB, targets registered by instance-id, healthy, customers cannot connect from office

🪤 **Your trap:** 🔁 First pick B was right; changed to A. NLB with instance-id targets preserves the client IP, so the EC2 security group must allow the office range, not the NLB subnets.

🧠 **Rule:** NLB + instance-id targets = client IP preserved → EC2 SG allows client CIDRs. Targets healthy = health-check path already open.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
 Văn phòng khách hàng                Public subnet         Private subnet
 (IP: 203.0.113.0/24)              ┌───────────┐         ┌──────────────┐
        │   TCP                    │           │  giữ    │ EC2 targets  │
        └─────────────────────────►│    NLB    │────────►│ (instance-id)│
                                   │           │ src IP  │ SG: ???      │
                                   └───────────┘ = client└──────────────┘
                                         │                     ▲
                                         └── health check ─────┘  → HEALTHY
   Kết quả: khách KHÔNG truy cập được
```

Hai manh mối quyết định: **targets đăng ký theo instance-id** và **tất cả đều healthy**. Đáp án đúng: **B (SG của EC2 phải cho phép IP văn phòng)**. Anh chọn **A**.

⚠️ Lỗi lặp lại: lần đầu Anh đã chọn **B (đúng)**, sau đó **đổi sang A** mà không có thông tin mới. Với câu single-answer, chỉ đổi khi tìm ra một chi tiết cụ thể trong đề làm đáp án cũ sai. Cảm giác "nghe hợp lý hơn" không phải là bằng chứng.

#### Vì sao B đúng

NLB hoạt động ở Layer 4 và với **target type = instance**, **client IP preservation** được bật → gói tin đến EC2 vẫn mang **source IP là IP của văn phòng khách hàng**, không phải IP của NLB.

```
Gói tin đến EC2:  src = 203.0.113.25 (văn phòng)   dst = EC2:listener port
SG của EC2 phải có:  inbound  TCP <port>  từ 203.0.113.0/24
```

Còn health check thì sao? Health check xuất phát **từ chính các node NLB** (IP private trong subnet của NLB). Targets đang **healthy** → chứng tỏ SG của EC2 **đã cho phép** traffic health check. Phần còn thiếu chỉ có thể là **traffic của client**.

#### Vì sao A (Anh chọn) sai

A nghe hợp lý vì Anh hình dung "NLB là proxy, EC2 nhận traffic từ NLB". Đó đúng với **ALB** (ALB kết thúc kết nối và mở kết nối mới từ IP của nó). Nhưng:

- Với NLB + instance-id, source IP **không** phải NLB subnet → rule cho NLB subnet không giúp traffic khách đi qua.
- Hơn nữa, targets **đã healthy** → traffic từ NLB subnet (health check) **đã được cho phép**. A không thay đổi được gì.

#### Các lựa chọn khác

- **C sai:** traffic không đi từ EC2 vào NLB; chiều vào NLB là từ client. Cho phép SG của EC2 vào NLB là sai chiều.
- **D sai:** NLB không cần nhận traffic từ chính Elastic IP của nó; EIP chỉ là địa chỉ công khai của các node NLB theo từng AZ.

#### So sánh: nguồn IP mà target nhìn thấy

| Load balancer / target type | Source IP đến target | SG của target cần cho phép |
|---|---|---|
| **NLB + instance-id** (đề này) | **IP client** (client IP preservation) | **CIDR của client** + health check |
| NLB + IP target (TCP/TLS, mặc định) | IP private của node NLB | Dải IP NLB/VPC |
| ALB (mọi target type) | IP của ALB | SG của ALB |

📝 Ghi chú kỹ thuật: TD explanation nói "NLB không có security group" — điều này đã **lỗi thời**: từ **08/2023**, NLB hỗ trợ gắn security group (phải gắn lúc tạo NLB). Nếu NLB có SG thì SG đó cũng phải cho phép CIDR văn phòng. Tuy nhiên đề không nhắc SG của NLB, và với instance-id targets thì client IP vẫn được giữ → **B vẫn là đáp án đúng**. Lưu ý thêm: với **IP-type targets** (TCP/TLS) client IP preservation mặc định **tắt** → khi đó target thấy IP của NLB, và kiểu suy luận như A mới có ý nghĩa.

#### Lưu ý thực tế

- Client IP preservation có thể được bật/tắt bằng **target group attribute**; luôn đọc kỹ target type trong đề.
- Khi client IP được giữ, rule SG cho phép NLB subnet vẫn cần cho **health check**, nhưng không thay thế được rule cho client.

#### Quy tắc nhớ cho thi

- **Thấy "NLB" + "registered by instance-id"** → client IP được giữ → **SG của EC2 phải cho phép CIDR client**
- **Thấy "targets are healthy"** → health check đã thông → vấn đề nằm ở **traffic client**, không phải traffic từ LB
- **Thấy "ALB"** → target thấy IP của ALB → SG target tham chiếu **SG của ALB**
- **Đổi đáp án** single-answer → chỉ khi chỉ ra được **một chi tiết cụ thể** trong đề làm đáp án đầu sai

### TD explanation

> ⚠️ Says NLBs have no security groups; NLB supports SGs since 2023. Key B still correct.

The Solutions Architect should check that the security group of the EC2 instances is allowing inbound connections from the customer office IP ranges. Note that NLBs do not have security groups configured and pass connections straight to EC2 instances with the source IP of the client preserved (when registered by instance-id).
With NLBs, when you register EC2 instances as targets, you must ensure that the security groups for these instances allow traffic on both the listener port and the health check port. We know that the health check port is already configured correctly as the targets are all healthy.
CORRECT:
"Check the security group for the EC2 instances to ensure it allows ingress from the customer office" is the correct answer.
INCORRECT:
"Check the security group for the EC2 instances to ensure it allows ingress from the NLB subnets" is incorrect. This is not necessary as the source IPs of clients are preserved.
INCORRECT:
"Check the security group for the NLB to ensure it allows ingress from the EC2 instances’ security group" is incorrect. The NLB security group does not receive incoming traffic from EC2, the traffic would come from the client.
INCORRECT:
"Check the security group for the NLB to ensure it allows ingress from the NLB elastic IP addresses. There is no security group associated with an NLB. If using EIPs, these are associated with the nodes in the AZ but the NLB security group would not need to receive incoming traffic from the nodes.
References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html#target-security-groups
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/security-identity-compliance-sap/

</details>

---

# Group C — Resilience and governance design: wrong lever for AZ spread, DX redundancy, cost attribution (3)

<a id="q11"></a>

## Q11

<!-- source: T6Q26 · domain: NEW · time: 3:16 · first: 68:55 · visits: 2 · changes: 0 -->



A business is in the process of setting up an Amazon Elastic Kubernetes Service (Amazon EKS) cluster to manage a specific workload. This workload is expected to generate a highly variable number of stateless pods, with a significant number of these pods being launched in a brief timeframe due to automatic scaling of replicas.
What approach should be taken to optimize the resilience of the nodes in this scenario?

- **A.** Implement a distinct launch template for deploying the EKS control plane in a secondary cluster, separate from the node groups that handle the workload.
- **B.** Modify the node groups for the workload by reducing the number of node groups but opting for larger instances within these groups.
- **C.** Set up the Kubernetes Cluster Autoscaler to maintain the compute capacity of the workload node groups at a consistently under provisioned level.
- **D.** Adjust the workload configuration to utilize topology spread constraints based on different Availability Zones.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** EKS, highly variable stateless pods, many launched quickly, optimize node resilience

🪤 **Your trap:** Picked Cluster Autoscaler under-provisioned; under-provisioning reduces capacity and resilience. Resilience = survive an AZ failure.

🧠 **Rule:** EKS resilience = spread pods across AZs with topology spread constraints (plus node groups in multiple AZs). Autoscaler sizing is about capacity, not fault tolerance.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                 Amazon EKS cluster
   ┌──────────────────────────────────────────────┐
   │  Control plane (AWS quản lý, multi-AZ sẵn)   │
   └──────────────────────────────────────────────┘
        │                 │                 │
   ┌─────────┐       ┌─────────┐       ┌─────────┐
   │  AZ-a   │       │  AZ-b   │       │  AZ-c   │
   │ nodes   │       │ nodes   │       │ nodes   │
   │ pod pod │       │ pod pod │       │ pod pod │
   └─────────┘       └─────────┘       └─────────┘

   Workload: stateless pods, số lượng biến động mạnh,
   scale ra rất nhiều pod trong thời gian ngắn
   Yêu cầu: tối ưu RESILIENCE của nodes
```

Từ khóa quyết định là **resilience** = workload vẫn sống khi một phần hạ tầng (một node, một AZ) gặp sự cố. Đáp án đúng: **D (topology spread constraints theo AZ)**. Anh chọn **C (Cluster Autoscaler giữ capacity ở mức under-provisioned)**.

#### Vì sao D đúng

Topology spread constraints là cấu hình ở **workload** (Pod spec), bảo scheduler rải pod đều theo một "topology domain" — ở đây là AZ (label `topology.kubernetes.io/zone`).

```
Không có spread constraint          Có spread constraint theo AZ
AZ-a: ██████████ (10 pod)           AZ-a: ███ (4 pod)
AZ-b: █ (1 pod)                     AZ-b: ███ (3 pod)
AZ-c: (0 pod)                       AZ-c: ███ (3 pod)
→ AZ-a sập = mất gần hết            → AZ nào sập cũng chỉ mất ~1/3
```

Đặc biệt khi **scale-out nhanh**, scheduler có xu hướng nhét pod vào chỗ còn trống gần nhất → dễ dồn cục vào một AZ. Spread constraint chặn đúng rủi ro đó. Đi kèm (thực tế): node groups phải trải trên nhiều AZ thì mới có chỗ để rải.

#### Vì sao C (Anh chọn) sai

C nghe có vẻ "đúng chủ đề" vì Cluster Autoscaler gắn liền với workload biến động. Nhưng:

- **Under-provisioned** = cố tình giữ ít capacity hơn nhu cầu → khi pod bùng nổ, pod bị `Pending` chờ node mới → giảm khả năng chịu tải, không tăng resilience.
- Autoscaler là chuyện **capacity** (đủ hay thiếu tài nguyên), không phải **fault tolerance** (mất một AZ thì sao). Đây là sai "đòn bẩy": đúng vùng dịch vụ, sai cơ chế.
- Nếu muốn hấp thụ burst nhanh, hướng thực tế là ngược lại: giữ chút **headroom** (over-provision nhẹ), không phải under-provision.

#### Các lựa chọn sai còn lại

- **A** — Control plane của EKS do **AWS quản lý**, tự chạy multi-AZ; Anh không dùng launch template để "deploy control plane". Một cluster thứ hai cũng không làm node của cluster hiện tại bền hơn.
- **B** — Ít node group + instance lớn hơn = **blast radius lớn hơn**: mất một node là mất nhiều pod cùng lúc, và ít node group thì khó trải đều nhiều AZ.

| Phương án | Tác động lên | Có tăng resilience? |
|---|---|---|
| **D. Topology spread theo AZ** | Phân bố pod qua các AZ | Có — chịu được mất 1 AZ |
| C. Autoscaler under-provisioned | Capacity | Không — còn làm thiếu tài nguyên |
| B. Ít node group, node to hơn | Kích thước node | Không — blast radius lớn hơn |
| A. Control plane riêng | Control plane (AWS quản lý) | Không liên quan tới node |

#### Lưu ý thực tế

- Spread constraint chỉ phát huy khi **node groups trải trên nhiều AZ** (subnets ở nhiều AZ).
- Spread constraint lo phần **pod**; Cluster Autoscaler lo phần **thêm node** khi pod `Pending`. Hai thứ bổ trợ nhau, nhưng chỉ spread constraint trả lời câu hỏi "mất một AZ thì sao".
- `whenUnsatisfiable: DoNotSchedule` (cứng) vs `ScheduleAnyway` (mềm) — mềm thì pod vẫn chạy khi không cân bằng được.

#### Quy tắc nhớ cho thi

- **Thấy "EKS/Kubernetes + resilience / high availability"** → **topology spread constraints theo AZ + node groups đa AZ**
- **Thấy "under-provisioned"** → gần như luôn sai khi hỏi resilience/availability
- **Thấy "launch template cho EKS control plane"** → sai, control plane do AWS quản lý
- **Thấy "ít node hơn nhưng to hơn"** → blast radius lớn, không phải resilience
- Mẹo: **Resilience = rải ra (spread), không phải co lại (shrink)**

### TD explanation

Using topology spread constraints based on Availability Zones is a strategic approach to enhance node resilience in an Amazon EKS cluster.
This method ensures that the pods are evenly distributed across different Availability Zones.
By doing so, it reduces the risk of a significant impact on the workload if one Availability Zone experiences issues, thereby maximizing node resilience and ensuring better fault tolerance and high availability.
CORRECT:
"Adjust the workload configuration to utilize topology spread constraints based on different Availability Zones" is the correct answer (as explained above.)
INCORRECT:
"Implement a distinct launch template for deploying the EKS control plane in a secondary cluster, separate from the node groups that handle the workload" is incorrect.
Deploying a separate EKS control plane in a different cluster does not directly contribute to the resilience of the nodes within the workload node groups. The control plane's location and configuration are more about management and orchestration rather than node resilience.
INCORRECT:
"Modify the node groups for the workload by reducing the number of node groups but opting for larger instances within these groups" is incorrect.
Using fewer node groups with larger instances might improve performance but does not necessarily maximize node resilience. Larger instances can still be susceptible to zone-specific issues, and having fewer groups could reduce the distribution and fault tolerance capabilities.
INCORRECT:
"Set up the Kubernetes Cluster Autoscaler to maintain the compute capacity of the workload node groups at a consistently under provisioned level" is incorrect.
Keeping the compute capacity of the workload node groups under provisioned is counterproductive for maximizing node resilience. Under provisioning can lead to insufficient resources during peak demand, potentially causing performance issues or even service disruptions.
References:
https://aws.github.io/aws-eks-best-practices/
Save time with our AWS cheat sheets:
https://digitalcloud.training/amazon-ecs-and-eks/

</details>

<a id="q20"></a>

## Q20

<!-- source: T2Q29 · domain: ORG · flagged · time: 3:49 · first: 77:02 · visits: 3 · changes: 1 -->



A company uses multiple AWS accounts. There are separate accounts for development, staging, and production environments. Some new requirements have been issued to control costs and improve the overall governance of the AWS accounts. The company must be able to calculate costs associated with each project and each environment. Commonly deployed IT services must be centrally managed and business units should be restricted to deploying pre-approved IT services only.
Which combination of actions should be taken to meet these requirements? (Select TWO.)

- **A.** Apply environment, cost center, and application name tags to all resources that accept tags.
- **B.** Configure custom budgets and define thresholds using AWS Cost Explorer.
- **C.** Use AWS Savings Plans to configure budget thresholds and send alerts to management.
- **D.** Create an AWS Service Catalog portfolio for each business unit and add products to the portfolios using AWS CloudFormation templates.
- **E.** Use Amazon CloudWatch to create a billing alarm that notifies managers when a billing threshold is reached or exceeded.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** B, D

🔑 **Key words:** cost per project and per environment, centrally managed IT services, only pre-approved services, Select TWO

🪤 **Your trap:** Picked custom budgets in Cost Explorer; budgets alert on totals, they do not attribute cost per project/environment. (Budgets live in AWS Budgets, not Cost Explorer.)

🧠 **Rule:** Cost per project/environment = cost allocation tags. Pre-approved services = Service Catalog portfolios. Budgets = alert on thresholds.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
        AWS accounts
   ┌────────┐  ┌─────────┐  ┌────────────┐
   │  Dev   │  │ Staging │  │ Production │
   └────────┘  └─────────┘  └────────────┘

   Yêu cầu 1: TÍNH ĐƯỢC chi phí theo từng PROJECT và từng ENVIRONMENT
   Yêu cầu 2: IT services phổ biến được QUẢN LÝ TẬP TRUNG
   Yêu cầu 3: business unit CHỈ được deploy dịch vụ ĐÃ DUYỆT
```

Select TWO → mỗi đáp án phải "gánh" một nhóm yêu cầu. Đáp án đúng: **A (tags)** + **D (Service Catalog)**. Anh chọn **B + D** → đúng nửa governance (D), sai nửa chi phí (B).

#### Ghép hai đáp án thành MỘT giải pháp

| Yêu cầu | Đáp án gánh | Cơ chế |
|---|---|---|
| Chi phí theo project / environment | **A** | Tag `environment`, `cost center`, `application` → activate làm **cost allocation tags** → cost được nhóm theo tag |
| Quản lý tập trung + chỉ dịch vụ đã duyệt | **D** | **Service Catalog** portfolio cho từng BU, product = CloudFormation template đã duyệt |

**A đúng** vì muốn "calculate costs associated with each project and each environment" thì mỗi resource phải mang thông tin project/environment. Đó chính là tag. Sau khi **activate** cost allocation tags trong Billing console, AWS dùng tag để phân loại chi phí trong cost allocation report (và Anh có thể group by tag trong Cost Explorer).

**D đúng** vì Service Catalog được thiết kế đúng cho câu "centrally managed" + "pre-approved IT services only": admin định nghĩa product (CloudFormation template), gom vào portfolio, cấp quyền portfolio cho từng BU; end user chỉ launch được những gì có trong portfolio, theo constraints admin đặt.

#### Vì sao B (Anh chọn) sai

B nghe giống "kiểm soát chi phí" nên dễ bị cuốn theo câu mở đầu "control costs". Nhưng:

- **Budgets không tạo trong Cost Explorer** mà trong **AWS Budgets**. Cost Explorer dùng để xem/phân tích chi phí.
- Kể cả tạo đúng chỗ, budget chỉ **cảnh báo khi vượt ngưỡng** — nó không trả lời câu "project X tốn bao nhiêu". Muốn budget theo project thì vẫn phải có **tag trước** → A là nền tảng, B (nếu có) chỉ là lớp bổ sung.

#### Các lựa chọn sai còn lại

- **C** — Savings Plans là **mô hình giá** (cam kết sử dụng để được giảm giá), không phải công cụ đặt ngưỡng hay gửi alert.
- **E** — CloudWatch billing alarm chỉ báo khi tổng hóa đơn chạm ngưỡng; đề **không yêu cầu alert**, và nó cũng không chia cost theo project/environment.

| Công cụ | Làm được gì | Đáp ứng "cost theo project/env"? |
|---|---|---|
| **Cost allocation tags** | Gắn nhãn → phân loại cost | Có |
| AWS Budgets | Alert khi vượt ngưỡng | Không tự làm được (cần tag) |
| Cost Explorer | Xem / phân tích cost | Chỉ khi đã có tag |
| Savings Plans | Giảm giá theo cam kết | Không |
| CloudWatch billing alarm | Alert tổng hóa đơn | Không |

#### ⚠️ Lỗi lặp lại

Ở Official exam Anh cũng trượt nhóm **governance tooling của Organizations** (conformance packs, IAM Access Analyzer). Lỗi chung: chọn công cụ "nghe đúng chủ đề" (cost → budgets) thay vì đọc **từng requirement cần công cụ nào**. Thói quen nên tập: gạch từng yêu cầu ra, rồi ghi tên đúng một dịch vụ cho mỗi yêu cầu — option nào không map được vào yêu cầu cụ thể thì loại.

#### Lưu ý thực tế

- Cost allocation tags phải **activate** (trong Organizations: ở management account) mới xuất hiện trong báo cáo; chi phí phát sinh trước khi activate không được gắn tag hồi tố.
- Có thể ép buộc gắn tag bằng **Tag Policies** (Organizations) hoặc tag mặc định trong Service Catalog product — kết hợp A + D rất tự nhiên.
- Tách account theo environment đã giúp chia cost theo env; nhưng **theo project** trong cùng account thì bắt buộc cần tag.

#### Quy tắc nhớ cho thi

- **Thấy "cost per project / department / environment / cost center"** → **cost allocation tags**
- **Thấy "pre-approved services / centrally managed IT services / self-service có kiểm soát"** → **AWS Service Catalog** (portfolio + CloudFormation product)
- **Thấy "alert khi vượt ngưỡng chi phí"** → **AWS Budgets** (không phải Cost Explorer)
- **Thấy "Savings Plans" kèm "alert / threshold"** → sai, đó là pricing model
- Mẹo: **Tag để ĐẾM, Budget để BÁO, Catalog để CHẶN**

### TD explanation

AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures.
AWS Service Catalog allows organizations to centrally manage commonly deployed IT services, and helps organizations achieve consistent governance and meet compliance requirements. End users can quickly deploy only the approved IT services they need, following the constraints set by the organization.
To track the costs associated with projects and environments cost allocation tags should be applied to the relevant resources. Cost allocation tags are used to track AWS costs on a detailed level. After you activate cost allocation tags, AWS uses the cost allocation tags to organize your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs.
CORRECT:
"Apply environment, cost center, and application name tags to all resources that accept tags" is a correct answer.
CORRECT:
"Create an AWS Service Catalog portfolio for each business unit and add products to the portfolios using AWS CloudFormation templates" is also a correct answer.
INCORRECT:
"Configure custom budgets and define thresholds using AWS Cost Explorer" is incorrect. Cost Explorer is used for viewing cost related information but not for creating budgets.
INCORRECT:
"Use AWS Savings Plans to configure budget thresholds and send alerts to management" is incorrect as this is not a service but a pricing model and cannot be used for sending alerts.
INCORRECT:
"Use Amazon CloudWatch to create a billing alarm that notifies managers when a billing threshold is reached or exceeded" is incorrect. There is no requirement to create billing alarms specified in the scenario.
References:
https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/category/aws-cheat-sheets/aws-solutions-architect-professional/aws-management-tools-sap/

</details>

<a id="q31"></a>

## Q31

<!-- source: T1Q14 · domain: ORG · flagged · time: 3:51 · first: 53:56 · visits: 2 · changes: 0 -->



A company has established a 10 Gbps AWS Direct Connect (DX) connection to a single VPC in an AWS Region. A single private VIF has been created for the existing DX connection. The company requires redundancy for the existing DX connection and needs to connect to an additional VPC in a second Region.
Which solution meets these requirements?

- **A.** Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region.
- **B.** Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a transit gateway in the VPCs in each Region.
- **C.** Create a new DX connection to the second Region. Create a new private VIF across the new DX connection to a virtual private gateway in the VPC in the second Region.
- **D.** Create a new DX connection to the second Region. Provision a transit gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** 10 Gbps DX, single VPC, single private VIF, redundancy for the existing DX, additional VPC in a second Region

🪤 **Your trap:** Picked a new DX to the second Region; that adds a path to a different VPC, not redundancy for the existing one.

🧠 **Rule:** DX redundancy = second connection to the same Region/location. Reach VPCs in other Regions = Direct Connect gateway (global) + private VIF to each VGW. TGW only when many VPCs per Region.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:
On-prem ══ DX #1 (10 Gbps) ══► Region 1 ── private VIF ──► VGW ─ VPC-1

Yêu cầu:
  (1) REDUNDANCY cho DX hiện tại (Region 1)
  (2) Kết nối thêm VPC-2 ở Region 2
```

Hai yêu cầu, một giải pháp. Đáp án đúng: **A (DX mới cùng Region + Direct Connect gateway + private VIF tới VGW mỗi Region)**. Anh chọn **C (DX mới tới Region 2)**.

#### Vì sao A đúng

```
                                  ┌──────────────────────────┐
On-prem ══ DX #1 ══╗              │ Direct Connect gateway   │
                   ╠═ private VIF ═►│ (global resource)       │
On-prem ══ DX #2 ══╝  (mỗi DX 1)  └──────┬─────────────┬─────┘
   (cùng Region/location                 │             │
    với DX #1 → redundancy)          association   association
                                         ▼             ▼
                                   VGW ─ VPC-1    VGW ─ VPC-2
                                    (Region 1)     (Region 2)
```

- **Yêu cầu (1)**: DX #2 tới **cùng Region** với DX #1 → nếu DX #1 hỏng, traffic đi DX #2. Đó mới là redundancy "cho existing DX connection".
- **Yêu cầu (2)**: **Direct Connect gateway là global** — tạo ở một Region nhưng associate được với VGW ở Region khác. Vậy từ cùng các DX ở Region 1 vẫn vào được VPC-2 ở Region 2, không cần DX riêng sang Region 2.
- Mỗi Region chỉ có **một VPC** → VGW là đủ, đơn giản nhất.

#### 📝 Ghi chú kỹ thuật

Đề ghi "private VIFs to a virtual private gateway in the VPCs in each Region". Thực tế: private VIF gắn vào **Direct Connect gateway**, rồi DX gateway **associate** với các VGW. Giữ đáp án A theo đề; cơ chế đúng là VIF → DXGW → VGW.

#### Vì sao C (Anh chọn) sai

C trông hợp lý vì "cần vào Region 2 thì kéo DX tới Region 2". Nhưng:

- DX mới đi tới **Region khác, VPC khác** → nếu DX #1 hỏng, VPC-1 vẫn mất kết nối. Không có redundancy cho kết nối hiện tại.
- Nó chỉ giải yêu cầu (2), bỏ trống yêu cầu (1). Đọc lại câu: "redundancy **for the existing** DX connection" — chữ "existing" chốt location.

#### Các lựa chọn sai còn lại

- **B** — Đúng phần DX cùng Region + DXGW, nhưng **transit gateway là thừa**: chỉ có một VPC mỗi Region. Hơn nữa, kết nối DXGW tới TGW dùng **transit VIF**, không phải private VIF → wording "private VIFs to a transit gateway" không khớp.
- **D** — DX mới tới Region 2 (lại không redundancy cho DX #1) và dùng **transit gateway** thay cho **Direct Connect gateway** để nối cross-Region — sai thành phần; TGW là regional, không phải điểm kết thúc của private VIF.

| Phương án | DX mới ở đâu | Redundancy DX #1? | Vào VPC Region 2 bằng | Hợp lý? |
|---|---|---|---|---|
| **A** | Cùng Region | Có | DXGW + VGW | Đúng, đơn giản nhất |
| B | Cùng Region | Có | DXGW + TGW (private VIF) | Thừa TGW, sai loại VIF |
| C | Region 2 | Không | DX riêng + VGW | Thiếu redundancy |
| D | Region 2 | Không | TGW + private VIF | Sai cả hai yêu cầu |

#### Lưu ý thực tế

- Redundancy mạnh hơn nữa: DX thứ hai ở **Direct Connect location khác** (khác thiết bị/khác site) — AWS khuyến nghị cho workload quan trọng. Trong đề, "same Region" là đủ để phân biệt với C/D.
- DX gateway **không** cho VPC-1 nói chuyện trực tiếp với VPC-2 qua nó; nó phục vụ on-prem ↔ VPC. Cần VPC ↔ VPC thì dùng peering hoặc TGW.
- Nhiều VPC mỗi Region → DXGW + **transit VIF** + TGW.

#### Quy tắc nhớ cho thi

- **Thấy "redundancy for existing DX"** → **thêm DX tới cùng Region/location** (tốt hơn: location khác)
- **Thấy "DX tới VPC ở Region khác"** → **Direct Connect gateway (global)**, không cần DX mới sang Region đó
- **Thấy "1 VPC mỗi Region"** → **private VIF + DXGW + VGW**
- **Thấy "nhiều VPC mỗi Region"** → **transit VIF + DXGW + TGW**
- Mẹo: **Redundancy = cùng chỗ, nhân đôi; Cross-Region = DX gateway**

### TD explanation

Use AWS Direct Connect gateway to connect your VPCs. You associate an AWS Direct Connect gateway with either of the following gateways:
A transit gateway when you have multiple VPCs in the same Region
A virtual private gateway
A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any Region and access it from all other Regions.
In this case the architecture should include a second DX connection from the on-premises network to the same Region as the existing DX connection to add redundancy. A DX GW can be provisioned and private VIFs can be created to virtual private gateways (VGWs) in the two AWS Regions the company wants to access.
CORRECT:
"Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region" is the correct answer (as explained above.)
INCORRECT:
"Create a new DX connection to the same Region. Provision a Direct Connect gateway and establish new private VIFs to a transit gateway in the VPCs in each Region" is incorrect.
The transit gateway is not required in this scenario as the company only has a single VPC they need to connect to in each Region.
INCORRECT:
"Create a new DX connection to the second Region. Create a new private VIF across the new DX connection to a virtual private gateway in the VPC in the second Region" is incorrect.
This does not provide the DX redundancy the company requires for the existing DX connection as the connection goes to a different Region and VPC.
INCORRECT:
"Create a new DX connection to the second Region. Provision a transit gateway and establish new private VIFs to a virtual private gateway in the VPCs in each Region" is incorrect.
The company requires redundancy for the existing DX connection in the same Region and will then need ta DX gateway to connect across Regions.
References:
https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html
Save time with our AWS cheat sheets:
https://digitalcloud.training/aws-direct-connect/

</details>
